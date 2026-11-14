"""The plugin's one set of snapshot rules, shared by the API helper (frappe_call.py) and the MCP guard hook
(hooks/frappe_guard.py), so the two can never disagree about which calls change existing records.

The rule: a call that changes or deletes an existing record needs a snapshot of that exact record, saved in
the workspace's .frappe/snapshots/ within the last hour. Anything the rules do not recognise is not let through
quietly: the helper refuses it and the guard asks the user.

A call is classified as one of:
  ("allow", [])      reads, creates something new, or returns an unsaved draft (ERPNext's mappers)
  ("need", pairs)    changes these existing records: each (doctype, name) needs a snapshot
  ("unnamed", [])    changes records but does not say which, or names them in two ways that disagree: refused
  ("unknown", [])    not a known read or write, and names no record: the helper refuses it unless told the
                     method is unlisted, and the guard asks the user
  ("import", pairs)  starts a Data Import: pairs is the import record. What else it needs depends on the
                     import's type and file, which only the site knows: see import_targets()

A pair's doctype may start with "~": it is then the doctype as it appears in a module path (sales_order) and
is matched against snapshots in that form.

The rules follow how Frappe itself reads a request (checked in Frappe 16.56's source): a JSON body replaces the
query string, a `cmd` argument is run whatever the address says, the v1 method address runs its first part, and
upload_file runs the method named in its `method` argument.
"""
import csv
import io
import json
import os
import re
import time
from pathlib import Path
from urllib.parse import parse_qsl, unquote

WINDOW = 3600  # a snapshot counts for one hour
NO_CHANGE = "allow"  # the kind for a call that changes no existing record: the rules have nothing to say about it

# Known writes by full dotted name, with the rule that says which arguments name the records they change.
WRITE_TARGETS = {
    "frappe.client.submit": "doc", "frappe.client.save": "doc", "frappe.desk.form.save.savedocs": "doc",
    "frappe.model.workflow.apply_workflow": "doc",
    "frappe.client.cancel": "flat", "frappe.client.delete": "flat", "frappe.client.set_value": "flat",
    "frappe.desk.form.save.cancel": "flat",
    "frappe.client.rename_doc": "rename", "frappe.model.rename_doc.rename_doc": "rename",
    "frappe.model.rename_doc.update_document_title": "retitle",
    "frappe.client.bulk_update": "bulk_update",
    "frappe.desk.reportview.delete_items": "delete_items",
    "frappe.desk.doctype.bulk_update.bulk_update.submit_cancel_or_update_docs": "docnames",
    "frappe.core.doctype.data_import.data_import.form_start_import": "import",
    "run_doc_method": "run_doc_method", "frappe.handler.run_doc_method": "run_doc_method",
    "frappe.api.v2.run_doc_method": "run_doc_method",
    "bulk_delete": "bulk_delete",
}
WRITE_METHODS = set(WRITE_TARGETS)
# the same last part under any other module path is treated as the same kind of write
WRITE_LAST = {m.rsplit(".", 1)[-1]: rule for m, rule in WRITE_TARGETS.items()}
# create only, by full name: nothing that exists is changed, unless a row is added to an existing record
CREATE_ONLY = {"frappe.client.insert", "frappe.client.insert_many", "upload_file", "frappe.handler.upload_file",
               "frappe.desk.form.utils.add_comment"}
READ_ONLY_EXACT = {
    "ping", "frappe.ping", "frappe.auth.get_logged_user", "frappe.desk.query_report.run",
    "frappe.client.get", "frappe.client.get_count", "frappe.client.get_list", "frappe.client.get_value",
    "frappe.client.get_single_value", "frappe.client.validate_link", "frappe.desk.reportview.get",
    "frappe.desk.reportview.get_count", "frappe.desk.form.load.getdoc", "frappe.desk.form.load.getdoctype",
    "frappe.desk.search.search_link", "frappe.desk.search.search_widget",
    "frappe.utils.print_format.download_pdf", "frappe.utils.print_format.download_multi_pdf",
    # an automation trial run executes for real inside a savepoint and rolls everything back
    "frappe.automation_engine.api.trial_run", "frappe.automation_engine.api.get_runs",
    "frappe.automation_engine.api.get_automation_capabilities",
}
READ_ONLY_PREFIXES = ("get_",)
# Methods named get_* whose own code writes to the database, found by reading every whitelisted get_* function
# in Frappe 16.56 and its apps on 2026-11-14. They are not treated as reads.
GET_THAT_WRITE = {
    "frappe.utils.goal.get_monthly_goal_graph_data", "frappe.core.api.file.get_files_in_folder",
    "erpnext.accounts.doctype.sales_invoice.sales_invoice.get_loyalty_programs",
    "erpnext.selling.doctype.customer.customer.get_customer_group_details",
    "erpnext.manufacturing.doctype.master_production_schedule.master_production_schedule.get_actual_demand",
    "hrms.api.get_shift_request_approvers", "hrms.api.__init__.get_shift_request_approvers",
    "hrms.hr.doctype.overtime_slip.overtime_slip.get_emp_and_overtime_details",
    "crm.api.doc.get_quick_filters", "helpdesk.api.doc.get_list_data", "helpdesk.api.doc.get_quick_filters",
    "lms.lms.payments.get_payment_link",
    "wiki.frappe_wiki.doctype.wiki_change_request.wiki_change_request.get_or_create_draft_change_request",
}
# the same methods as (doctype in a module path, method), for the address form /method/<doctype>/<method>
GET_THAT_WRITE_BY_DOCTYPE = {(m.group(1), m.group(2)) for m in
                             (re.search(r"\.doctype\.([a-z0-9_]+)\.\1\.([A-Za-z0-9_]+)$", x) for x in GET_THAT_WRITE) if m}
# ERPNext's mappers return an unsaved draft made from an existing record. A make_* method counts as one only
# when it is called the way a mapper is (with source_name); these others were run on a live site and do the same.
KNOWN_DRAFT_MAKERS = {
    "erpnext.manufacturing.doctype.work_order.work_order.make_stock_entry",
    "lending.loan_management.doctype.loan_application.loan_application.create_loan",
    "lending.loan_management.doctype.loan.loan.make_loan_disbursement",
    "lending.loan_management.doctype.loan.loan.make_repayment_entry",
}
# document methods (/document/<doctype>/<name>/method/<m>) that only read; every other one changes the record
READ_ONLY_DOC_METHODS = {"get_preview_from_template"}


def _last(method):
    return str(method).rsplit(".", 1)[-1]


def scrub(doctype):
    """Frappe's own form of a doctype name inside a module path: Sales Order -> sales_order."""
    return str(doctype).replace(" ", "_").replace("-", "_").lower()


def write_rule(method):
    return WRITE_TARGETS.get(method) or WRITE_LAST.get(_last(method))


def is_write(method):
    return write_rule(method) is not None


def is_read_only(method, hint=None):
    if is_write(method) or method in GET_THAT_WRITE:
        return False
    if hint and (scrub(str(hint).lstrip("~")), _last(method)) in GET_THAT_WRITE_BY_DOCTYPE:
        return False
    return method in READ_ONLY_EXACT or _last(method).startswith(READ_ONLY_PREFIXES)


def _as_obj(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def _scalar(v):
    return isinstance(v, (str, int)) and not isinstance(v, bool) and v != ""


def _truthy(v):
    return str(v).lower() in ("1", "true", "yes")


def _pair(dt, name):
    return (str(dt), str(name)) if isinstance(dt, str) and dt and _scalar(name) else None


def _doc_pair(d):
    """The record a document object names; None for a new, unsaved document (it has no name yet)."""
    if not isinstance(d, dict) or d.get("__islocal"):
        return None
    return _pair(d.get("doctype"), d.get("name") if _scalar(d.get("name")) else d.get("docname"))


_SINGLES = None


def singles():
    """Settings record types (Singles) of Frappe's own apps. Creating one overwrites the stored settings."""
    global _SINGLES
    if _SINGLES is None:
        try:
            text = (Path(__file__).resolve().parent / "frappe_singles.txt").read_text(encoding="utf-8")
            _SINGLES = {l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#")}
        except OSError:
            _SINGLES = set()
    return _SINGLES


def settings_like(doctype):
    """A record type the bundled list does not have but whose name says it holds settings. Only the site knows
    whether it is a Single, so the helper asks the site and the guard asks the user."""
    return isinstance(doctype, str) and doctype not in singles() and doctype.strip().lower().endswith("settings")


def classify_create(doctype, data):
    """Creating a record: POST /document/<doctype>, MCP's create_document, frappe.client.insert."""
    data = _as_obj(data)
    data = data if isinstance(data, dict) else {}
    doctype = data.get("doctype") if not doctype and isinstance(data.get("doctype"), str) else doctype
    if data.get("parent") or data.get("parenttype"):
        p = _pair(data.get("parenttype"), data.get("parent"))    # a row added to an existing record changes it
        return ("need", [p]) if p else ("unnamed", [])
    if doctype in singles():
        return "need", [(str(doctype), str(doctype))]            # "creating" a Single replaces its settings
    return "allow", []


def generic_refs(args, hint=None):
    """Every existing record a call's arguments name, for methods the rules have no entry for."""
    refs = []
    dt = next((args.get(k) for k in ("doctype", "dt", "reference_doctype", "ref_doctype")
               if isinstance(args.get(k), str) and args.get(k)), None) or hint
    if dt:
        for k in ("name", "dn", "docname", "old_name", "new_name", "reference_name", "ref_name", "document_name"):
            if _scalar(args.get(k)):
                refs.append((str(dt), str(args[k])))
        for k in ("names", "docnames", "items"):
            v = _as_obj(args.get(k))
            if isinstance(v, list):
                refs += [(str(dt), str(x)) for x in v if _scalar(x)]
    for k in ("doc", "document", "docs"):
        v = _as_obj(args.get(k))
        for d in ([v] if isinstance(v, dict) else v if isinstance(v, list) else []):
            p = _doc_pair(d)
            if p:
                refs.append(p)
    return list(dict.fromkeys(refs))


def _apply_rule(rule, args, hint, exact=True):
    """(kind, pairs) for a known kind of write. Where Frappe could read the record from two arguments and they
    disagree, the call is "unnamed": the check must never look at one record while Frappe changes another."""
    if rule == "doc":
        inner = _as_obj(args.get("doc"))
        if isinstance(inner, dict) and isinstance(inner.get("doctype"), str) and (inner.get("__islocal") or not _scalar(inner.get("name"))):
            return classify_create(inner.get("doctype"), inner)  # saving a document with no name creates it
        p = _doc_pair(inner)
        flat = _pair(args.get("doctype"), args.get("name"))
        return ("need", [p]) if p and (not flat or flat == p) else ("unnamed", [])
    if rule == "flat":
        p = _pair(args.get("doctype"), args.get("name"))
        other = _doc_pair(_as_obj(args.get("doc")))
        return ("need", [p]) if p and (not other or other == p) else ("unnamed", [])
    if rule == "rename":
        dt, old, new = args.get("doctype"), args.get("old_name"), args.get("new_name")
        p = _pair(dt, old)
        if not p or (_scalar(args.get("name")) and str(args.get("name")) != str(old)):
            return "unnamed", []
        if _truthy(args.get("merge")):
            q = _pair(dt, new)
            return ("need", [p, q]) if q else ("unnamed", [])
        return "need", [p]
    if rule == "retitle":                                        # update_document_title(doctype, docname, name=, new_name=)
        dt = args.get("doctype")
        p = _pair(dt, args.get("docname"))
        if not p:
            return "unnamed", []
        if _truthy(args.get("merge")):
            targets = [_pair(dt, args.get(k)) for k in ("name", "new_name") if _scalar(args.get(k))]
            return ("need", [p] + targets) if targets else ("unnamed", [])
        return "need", [p]
    if rule in ("delete_items", "docnames"):
        key = "items" if rule == "delete_items" else "docnames"
        dt, names = args.get("doctype") or hint, _as_obj(args.get(key))
        if hint and isinstance(args.get("doctype"), str) and args.get("doctype") != hint:
            return "unnamed", []
        names = [names] if _scalar(names) else names
        pairs = [_pair(dt, i) for i in names] if isinstance(names, list) else []
        return ("need", pairs) if pairs and all(pairs) else ("unnamed", [])
    if rule in ("bulk_update", "bulk_delete"):
        if hint and isinstance(args.get("doctype"), str) and args.get("doctype") != hint:
            return "unnamed", []                                 # the address says one doctype, the data another
        dt = hint or (args.get("doctype") if isinstance(args.get("doctype"), str) else None)
        docs, names = _as_obj(args.get("docs")), _as_obj(args.get("names"))
        pairs = []
        if isinstance(docs, list):
            for d in docs:
                if isinstance(d, dict):
                    a, b = d.get("docname"), d.get("name")
                    if _scalar(a) and _scalar(b) and str(a) != str(b):
                        return "unnamed", []
                    if exact and rule == "bulk_update" and not hint and not _scalar(a):
                        return "unnamed", []                     # frappe.client.bulk_update reads `docname` only
                    pairs.append(_pair(d.get("doctype") or dt, a if _scalar(a) else b))
                else:
                    pairs.append(_pair(dt, d) if _scalar(d) else None)
        if isinstance(names, list):
            pairs += [_pair(dt, n) for n in names]
        return ("need", pairs) if pairs and all(pairs) else ("unnamed", [])
    if rule == "import":
        di = args.get("data_import")
        return ("import", [("Data Import", str(di))]) if _scalar(di) else ("unnamed", [])
    if rule == "run_doc_method":                                 # v2: (method, document); v1: (method, docs | dt, dn)
        found = set()
        for key in ("document", "docs"):
            doc = _as_obj(args.get(key))
            if isinstance(doc, dict):
                p = _doc_pair(doc)
                if not p:
                    return "unnamed", []
                found.add(p)
            elif doc not in (None, ""):
                return "unnamed", []
        if args.get("dt"):
            p = _pair(args.get("dt"), args.get("dn") if _scalar(args.get("dn")) else args.get("dt"))   # a Single
            if not p:
                return "unnamed", []
            found.add(p)
        if len(found) != 1:
            return "unnamed", []
        p = found.pop()
        return classify_doc_method(p[0], p[1], args.get("method"))
    return "unnamed", []


def classify_method(method, args, hint=None, _depth=0):
    """A whitelisted method call: /api/(v1/|v2/)method/<method>, or Frappe MCP's call_method.
    `hint` is the doctype when the address names one (/method/<doctype>/<method>)."""
    method = str(method or "")
    args = _as_obj(args)
    args = args if isinstance(args, dict) else {}
    rule = WRITE_TARGETS.get(method)
    exact = rule is not None
    rule = rule or WRITE_LAST.get(_last(method))
    if rule:
        kind, pairs = _apply_rule(rule, args, hint, exact)
        if kind == "unnamed" and not exact:                      # another module's method with a familiar name
            refs = generic_refs(args, hint)
            return ("need", refs) if refs else ("unnamed", [])
        return kind, pairs
    if method in CREATE_ONLY:
        last = _last(method)
        if last == "upload_file":
            if args.get("method"):                               # upload_file runs the method named here
                inner = str(args.get("method"))
                if _depth or _last(inner) == "upload_file":
                    return "unknown", []
                return classify_method(inner, args, None, _depth + 1)
            if args.get("fieldname"):                            # sets a field on an existing record
                p = _pair(args.get("doctype"), args.get("docname"))
                return ("need", [p]) if p else ("unnamed", [])
            return "allow", []
        if last == "add_comment":
            return "allow", []                                   # adds a comment; the record itself is not changed
        docs = _as_obj(args.get("docs")) if last == "insert_many" else [_as_obj(args.get("doc"))]
        docs = docs if isinstance(docs, list) else []
        need = []
        for d in docs:
            kind, pairs = classify_create(None, d)
            if kind == "unnamed":
                return "unnamed", []
            need += pairs
        return ("need", need) if need else ("allow", [])
    if is_read_only(method, hint) or method in KNOWN_DRAFT_MAKERS:
        return "allow", []
    if _last(method).startswith("make_") and _scalar(args.get("source_name")):
        return "allow", []                                       # called as a mapper: returns an unsaved draft
    if not hint:
        m = re.search(r"\.doctype\.([a-z0-9_]+)\.\1\.[A-Za-z0-9_]+$", method)
        hint = "~" + m.group(1) if m else None                   # ...doctype.sales_order.sales_order.update_status
    refs = generic_refs(args, hint)
    return ("need", refs) if refs else ("unknown", [])


def classify_doc_method(doctype, name, method):
    """A method run on one record: /document/<doctype>/<name>/method/<method>, or MCP's call_document_method."""
    if str(method or "") in READ_ONLY_DOC_METHODS:
        return "allow", []
    p = _pair(doctype, name)
    return ("need", [p]) if p else ("unnamed", [])


def split_api_path(path):
    """(version, kind, rest, query) for /api/[v1/|v2/]<kind>/<rest>; kind is None when the path is not one of
    the API's method, resource, document or doctype routes."""
    p, _, q = str(path).partition("?")
    m = re.match(r"^/api/(?:(v1|v2)/)?(method|resource|document|doctype)(?:/(.*))?$", unquote(p).rstrip("/"))
    query = dict(parse_qsl(q, keep_blank_values=True))
    if not m:
        return None, None, "", query
    return m.group(1) or "v1", m.group(2), m.group(3) or "", query


def request_args(path, body=None, query=None):
    """The arguments Frappe will read: the JSON body when one is sent (the query string is then ignored),
    otherwise the query string."""
    if body is not None:
        b = _as_obj(body)
        return b if isinstance(b, dict) else {}
    args = dict(split_api_path(path)[3])
    q = _as_obj(query)
    if isinstance(q, dict):
        args.update(q)
    return args


def method_creates(method, args):
    """The record types a method call creates (insert, insert_many, or saving a document that has no name yet)."""
    method = str(method or "")
    args = _as_obj(args)
    args = args if isinstance(args, dict) else {}
    last = _last(method)
    docs = []
    if method == "frappe.client.insert" or last in ("save", "savedocs", "submit"):
        docs = [_as_obj(args.get("doc"))]
    elif method == "frappe.client.insert_many":
        d = _as_obj(args.get("docs"))
        docs = d if isinstance(d, list) else []
    return [d["doctype"] for d in docs if isinstance(d, dict) and isinstance(d.get("doctype"), str)
            and (d.get("__islocal") or not _scalar(d.get("name")))]


def created_doctypes(verb, path, body=None, query=None):
    """The record types this call creates, so the helper can ask the site whether one is a settings type."""
    args = request_args(path, body, query)
    method = None
    if isinstance(args.get("cmd"), str) and args.get("cmd"):
        method = args["cmd"]
    else:
        version, kind, rest, _ = split_api_path(path)
        if kind in ("resource", "document"):
            return [rest] if str(verb).upper() == "POST" and rest and "/" not in rest else []
        if kind == "method" and rest:
            method = rest.split("/")[0] if version == "v1" else rest.rsplit("/", 1)[-1]
    return method_creates(method, args) if method else []


def classify_request(verb, path, body=None, query=None):
    """One HTTP call to a Frappe site. GET is checked too: Frappe accepts GET on most methods."""
    verb = str(verb).upper()
    version, kind, rest, _ = split_api_path(path)
    args = request_args(path, body, query)

    def as_method(method, hint=None):
        result = classify_method(method, args, hint)
        if verb == "GET" and not is_write(method) and not (_last(method) == "upload_file" and args.get("method")):
            return "allow", []                                   # a read; Frappe rolls back what a GET changes
        return result

    if isinstance(args.get("cmd"), str) and args.get("cmd"):
        return as_method(args["cmd"])                            # Frappe runs `cmd` whatever the address says
    if kind is None or kind == "doctype":                        # doctype: meta and count, read only
        return ("allow", []) if verb == "GET" else ("unknown", [])
    if kind == "method":
        if not rest:
            return ("allow", []) if verb == "GET" else ("unknown", [])
        if version == "v1":
            return as_method(rest.split("/")[0])                 # v1 runs the first part of the address
        if "/" in rest:                                          # v2: /method/<doctype>/<method>
            hint, method = rest.rsplit("/", 1)
            return as_method(method, hint)
        return as_method(rest)
    # resource (v1) or document (v2)
    doctype, _, name = rest.partition("/")
    if not doctype:
        return ("allow", []) if verb == "GET" else ("unknown", [])
    if not name:
        if verb == "GET":
            return "allow", []
        return classify_create(doctype, args) if verb == "POST" else ("unnamed", [])
    if kind == "document":
        m = re.match(r"^(.+)/method/([^/]+)$", name)
        if m:
            if verb == "GET" and m.group(2) not in WRITE_LAST:
                return "allow", []                               # Frappe rolls back what a GET changes
            return classify_doc_method(doctype, m.group(1), m.group(2))
        if verb == "GET":
            return "allow", []                                   # read, or .../copy (an unsaved copy)
        if verb == "POST" and name in ("bulk_delete", "bulk_update"):
            return _apply_rule(name, args, doctype, exact=False)
        if verb == "POST":
            return "unknown", []
    else:
        if verb == "GET":
            return "allow", []
        if verb == "POST":                                       # v1 runs a document method named in run_method
            return classify_doc_method(doctype, name, args.get("run_method")) if args.get("run_method") else ("unnamed", [])
    return "need", [(str(doctype), str(name))]                   # PUT, PATCH, DELETE


def _csv_columns(text, titles):
    rows = [r for r in csv.reader(io.StringIO(text)) if any(c.strip() for c in r)]
    if not rows:
        return None, 0
    head = [c.strip() for c in rows[0]]
    cols = []
    for t in titles:
        at = [i for i, c in enumerate(head) if c == t]
        if len(at) != 1:
            return None, 0
        cols.append(at[0])
    return [[(r[i].strip() if len(r) > i else "") for i in cols] for r in rows[1:]], len(rows) - 1


def _ids(rows):
    """One ID per row from the row's ID columns (they must agree); a blank ID continues the record above."""
    ids = []
    for n, vals in enumerate(rows):
        seen = {str(v) for v in vals if v not in (None, "")}
        if len(seen) > 1 or (n == 0 and not seen):
            return None                                          # two ID columns disagree, or the first row names none
        ids += list(seen)
    return ids


def import_targets(import_record, preview, file_text=None, id_field=None):
    """What starting a Data Import needs snapshots of: the import record, and for an update import every record
    the file changes. The IDs come from the import's dry run (get_preview_from_template, which saves nothing);
    the dry run shows only the first rows of a long file, so for those the IDs are read from the file itself.
    `id_field` is the field Frappe identifies a record by: `name`, or the naming field of a record type that is
    named by one of its fields (an Item by its item code). Without it, the column titled ID is used.
    Returns the list of (doctype, name), or None when the records cannot be worked out (the call is refused)."""
    if not isinstance(import_record, dict) or not import_record.get("name"):
        return None
    pairs = [("Data Import", str(import_record["name"]))]
    kind = import_record.get("import_type")
    if kind == "Insert New Records":
        return pairs
    if kind != "Update Existing Records":
        return None
    dt = import_record.get("reference_doctype")
    if not dt or not isinstance(preview, dict):
        return None
    cols = preview.get("columns") or []

    def own(c):
        return isinstance(c, dict) and not c.get("skip_import") and (c.get("df") or {}).get("parent") in (None, "", dt)

    wanted = {id_field} if id_field else {"name"}
    idx = [i for i, c in enumerate(cols) if own(c) and (c.get("df") or {}).get("fieldname") in wanted]
    if not idx:                                                  # the naming field is not known: go by the title
        idx = [i for i, c in enumerate(cols) if own(c) and str(c.get("header_title") or "").strip() == "ID"]
        if idx:
            field = (cols[idx[0]].get("df") or {}).get("fieldname")
            idx = [i for i, c in enumerate(cols) if own(c) and (c.get("df") or {}).get("fieldname") == field]
    rows = preview.get("data") or []
    total = preview.get("total_number_of_rows")
    if not idx or not rows:
        return None
    if preview.get("max_rows_exceeded") or (isinstance(total, int) and total != len(rows)):
        if file_text is None:
            return None                                          # the dry run does not show every row
        data, count = _csv_columns(file_text, [str(cols[i].get("header_title") or "").strip() for i in idx])
        if data is None or (isinstance(total, int) and count != total):
            return None
        ids = _ids(data)
    else:
        ids = _ids([[r[i] if isinstance(r, list) and len(r) > i else None for i in idx] for r in rows])
    if not ids:
        return None
    return pairs + [(str(dt), n) for n in sorted(set(ids))]


def _has_state(d):
    return (d / ".frappe" / "state.json").is_file()


def find_workspaces(start=None):
    """The folders connected to a Frappe site (each holds .frappe/state.json) that this session is working in:
    `start` or the nearest folder above it, else the session's project folder, else any connected folder one or
    two levels below (the session was started above its workspace). Empty when there is none."""
    bases = []
    for base in (start, os.environ.get("CLAUDE_PROJECT_DIR")):
        if not base:
            continue
        try:
            here = Path(base).resolve()
        except OSError:
            continue
        bases.append(here)
        for d in [here, *here.parents]:
            if _has_state(d):
                return [d]
    found, looked = [], 0
    for here in bases:
        level = [here]
        for _ in range(2):
            nxt = []
            for d in level:
                try:
                    kids = [k for k in os.scandir(d) if k.is_dir(follow_symlinks=False)
                            and not k.name.startswith(".") and k.name not in ("node_modules", "__pycache__")]
                except OSError:
                    continue
                for k in kids:
                    looked += 1
                    if looked > 600:                             # a very large folder: stop looking
                        return found
                    p = Path(k.path)
                    if _has_state(p):
                        found.append(p)
                    else:
                        nxt.append(p)
            level = nxt
    return found


def find_workspace(start=None):
    """The one connected folder for `start` (it, or the nearest above it, or the project folder); None when
    there is none or the only ones are below."""
    for base in (start, os.environ.get("CLAUDE_PROJECT_DIR")):
        if not base:
            continue
        try:
            here = Path(base).resolve()
        except OSError:
            continue
        for d in [here, *here.parents]:
            if _has_state(d):
                return d
    return None


def read_json_file(path):
    """A JSON file as written by any tool: UTF-8 with or without a BOM, or UTF-16 (PowerShell's default)."""
    raw = Path(path).read_bytes()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return json.loads(raw.decode("utf-16"))
    return json.loads(raw.decode("utf-8-sig"))


def snapshot_pairs(data, inherited=None, out=None):
    """Every (doctype, name) a snapshot really holds. A record counts only when it is there as read from the
    site: it carries `docstatus` and `modified`, which a list of names does not (such a list can restore
    nothing). A settings record that was never saved has no `modified` yet and still counts. A record that
    does not name its doctype takes it from what it sits under (a list read under a `doctype` key)."""
    out = set() if out is None else out
    if isinstance(data, dict):
        dt = data.get("doctype") if isinstance(data.get("doctype"), str) and data.get("doctype") else inherited
        if dt and _scalar(data.get("name")) and "docstatus" in data and (data.get("modified") or str(data["name"]) == dt):
            out.add((dt, str(data["name"])))
        for v in data.values():
            if isinstance(v, (dict, list)):
                snapshot_pairs(v, dt, out)
    elif isinstance(data, list):
        for v in data:
            snapshot_pairs(v, inherited, out)
    return out


def _snapshots(ws, window):
    snaps = Path(ws) / ".frappe" / "snapshots"
    if not snaps.is_dir():
        return
    now = time.time()
    for d in snaps.iterdir():
        raw = d / "raw.json"
        try:
            if not raw.is_file() or now - raw.stat().st_mtime > window:
                continue
            yield read_json_file(raw)
        except (OSError, ValueError):
            continue


def snapshotted(ws, window=WINDOW):
    """All (doctype, name) pairs in the snapshots of one workspace, or of each in a list, from the last
    `window` seconds."""
    found = set()
    for w in (ws if isinstance(ws, (list, tuple)) else [ws]):
        for data in _snapshots(w, window):
            found |= snapshot_pairs(data)
    return found


def snapshotted_record(ws, doctype, name, window=WINDOW):
    """The fields of one snapshotted record (merged from every copy of it), or {} when none holds it."""
    fields = {}

    def walk(v, inherited=None):
        if isinstance(v, dict):
            dt = v.get("doctype") if isinstance(v.get("doctype"), str) and v.get("doctype") else inherited
            if dt == doctype and str(v.get("name")) == str(name) and "docstatus" in v:
                fields.update({k: x for k, x in v.items() if not isinstance(x, (dict, list))})
            for x in v.values():
                walk(x, dt)
        elif isinstance(v, list):
            for x in v:
                walk(x, inherited)

    for w in (ws if isinstance(ws, (list, tuple)) else [ws]):
        for data in _snapshots(w, window):
            walk(data)
    return fields


STAMP = ".last_user_message"
LIVE = 6 * 3600   # a stamp older than this is from an earlier session, not the one that is running now


def note_user_message(workspaces):
    """Called by the plugin's hooks when the user sends a message or answers a question: the time is kept in
    the workspace, so a change can be held until the user has replied after its snapshot was saved."""
    for w in (workspaces if isinstance(workspaces, (list, tuple)) else [workspaces]):
        try:
            (Path(w) / ".frappe" / STAMP).write_text(repr(time.time()), encoding="utf-8")
        except OSError:
            pass


def last_user_message(ws):
    """When the user last sent a message in any of these workspaces; None when no hook has recorded one.
    It is the time the file system gave the marker file, the same clock a snapshot's time comes from."""
    best = None
    for w in (ws if isinstance(ws, (list, tuple)) else [ws]):
        try:
            t = (Path(w) / ".frappe" / STAMP).stat().st_mtime
        except OSError:
            continue
        best = t if best is None else max(best, t)
    return best


def unlisted_call_allowed(ws, key, flag):
    """A call the rules do not know. It is refused the first time, and that refusal is recorded. It goes through
    only when repeated with the override flag after the user has replied since the refusal (where the plugin's
    hooks record messages; where none runs, the repeat with the flag is enough)."""
    import hashlib
    d = Path(ws) / ".frappe" / ".unlisted"
    mark = d / hashlib.sha1(str(key).encode("utf-8")).hexdigest()[:16]
    now = time.time()
    try:
        refused_at = mark.stat().st_mtime
    except OSError:
        refused_at = None
    if refused_at is not None and now - refused_at > LIVE:
        refused_at = None
    if not flag or refused_at is None:
        try:
            d.mkdir(parents=True, exist_ok=True)
            if refused_at is None:
                mark.write_text(str(key), encoding="utf-8")
        except OSError:
            pass
        return False
    last = last_user_message(ws)
    if last is not None and now - last <= LIVE and last <= refused_at:
        return False                                             # hooks are recording, and the user has not replied
    return True


def snapshot_times(ws, window=WINDOW):
    """{(doctype, name): when its earliest snapshot in the window was saved}."""
    times = {}
    now = time.time()
    for w in (ws if isinstance(ws, (list, tuple)) else [ws]):
        snaps = Path(w) / ".frappe" / "snapshots"
        if not snaps.is_dir():
            continue
        for d in snaps.iterdir():
            raw = d / "raw.json"
            try:
                if not raw.is_file():
                    continue
                at = raw.stat().st_mtime
                if now - at > window:
                    continue
                for p in snapshot_pairs(read_json_file(raw)):
                    times[p] = min(times.get(p, at), at)
            except (OSError, ValueError):
                continue
    return times


def unconfirmed(ws, pairs, window=WINDOW, strict=True):
    """The records whose snapshot was saved after the user's last message: nothing shows the user was told what
    will change and replied. With strict=False (the helper), the check applies only while the plugin's hooks are
    recording messages in this workspace; where no hook runs it cannot be made."""
    last = last_user_message(ws)
    if last is None or time.time() - last > LIVE:
        if not strict:
            return []
        last = None
    times = snapshot_times(ws, window)
    by_scrub = {(scrub(a), b): t for (a, b), t in times.items()}
    out = []
    for a, b in pairs:
        a, b = str(a), str(b)
        at = by_scrub.get((a[1:], b)) if a.startswith("~") else times.get((a, b))
        if at is None:
            continue                                             # no snapshot at all: missing_snapshots reports it
        if last is None or at >= last:
            out.append((a[1:].replace("_", " ").title() if a.startswith("~") else a, b))
    return out


def missing_snapshots(ws, pairs, window=WINDOW):
    """The pairs that no snapshot from the last `window` seconds holds exactly."""
    have = snapshotted(ws, window)
    scrubbed = {(scrub(a), b) for a, b in have}
    out = []
    for a, b in pairs:
        a, b = str(a), str(b)
        ok = (a[1:], b) in scrubbed if a.startswith("~") else (a, b) in have
        if not ok:
            out.append((a[1:].replace("_", " ").title() if a.startswith("~") else a, b))
    return out
