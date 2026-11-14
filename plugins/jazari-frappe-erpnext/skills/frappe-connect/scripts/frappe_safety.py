"""The plugin's one set of snapshot rules, shared by the API helper (frappe_call.py) and the MCP guard hook
(hooks/frappe_guard.py), so the two can never disagree about which calls change existing records.

A call is classified as one of:
  ("allow", [])      reads, creates something new, or returns an unsaved draft (ERPNext's make_* mappers)
  ("need", pairs)    changes these existing records: each (doctype, name) needs a snapshot from the last hour
  ("unnamed", [])    a known write that does not say which records it touches, or names them inconsistently:
                     refused
  ("unknown", [])    not a known read or write and names no record: the MCP guard asks the user first
  ("import", pairs)  starts a Data Import: pairs is the import record. What else it needs depends on the
                     import's type, which only the site knows: see import_targets()
"""
import json
import time
from pathlib import Path

WINDOW = 3600  # a snapshot counts for one hour

# Known writes by full dotted name, with the arguments that name what each one changes.
#   "doc": a whole document in `doc`; "flat": `doctype` and `name`; "rename": `doctype` and `old_name`
#   (and `new_name` too when merging)
WRITE_TARGETS = {
    "frappe.client.submit": "doc", "frappe.client.save": "doc",
    "frappe.client.cancel": "flat", "frappe.client.delete": "flat", "frappe.client.set_value": "flat",
    "frappe.client.rename_doc": "rename", "frappe.model.rename_doc": "rename",
    "frappe.client.bulk_update": "bulk_update", "frappe.desk.reportview.delete_items": "delete_items",
    "frappe.core.doctype.data_import.data_import.form_start_import": "import",
}
WRITE_METHODS = set(WRITE_TARGETS)
# the same last part under any other module path is treated as the same write, with the same arguments
WRITE_LAST = {m.rsplit(".", 1)[-1]: rule for m, rule in WRITE_TARGETS.items()}
# create only, by full name: nothing that exists is changed, unless a row is added to an existing parent
CREATE_ONLY = {"frappe.client.insert", "frappe.client.insert_many", "upload_file", "frappe.handler.upload_file"}
READ_ONLY_EXACT = {
    "frappe.desk.query_report.run", "frappe.client.get", "frappe.client.get_count", "frappe.client.get_list",
    "frappe.client.get_value", "frappe.client.get_single_value", "frappe.desk.reportview.get",
    "frappe.desk.reportview.get_count", "frappe.auth.get_logged_user", "ping", "trial_run", "get_runs",
    "get_automation_capabilities",
}
READ_ONLY_PREFIXES = ("get_", "make_")  # make_* are ERPNext's mappers: they return an unsaved draft
# document methods (/document/<doctype>/<name>/method/<m>) that only read; every other one changes the record
READ_ONLY_DOC_METHODS = {"get_preview_from_template"}


def _last(method):
    return str(method).rsplit(".", 1)[-1]


def write_rule(method):
    return WRITE_TARGETS.get(method) or WRITE_LAST.get(_last(method))


def is_write(method):
    return write_rule(method) is not None


def is_read_only(method):
    if is_write(method):
        return False
    last = _last(method)
    return method in READ_ONLY_EXACT or last in READ_ONLY_EXACT or last.startswith(READ_ONLY_PREFIXES)


def _as_obj(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def _pair(dt, name):
    return (str(dt), str(name)) if dt and name not in (None, "") else None


def _parent_pairs(docs):
    """Rows added under an existing parent (they carry parent and parenttype) change that parent."""
    return [(str(d["parenttype"]), str(d["parent"])) for d in docs
            if isinstance(d, dict) and d.get("parent") and d.get("parenttype")]


def _named(args):
    """The one record a call names, from `doc` or from doctype/name (dt/dn on v1); None when it names none or
    names two different ones."""
    inner = _as_obj(args.get("doc"))
    from_doc = _pair(inner.get("doctype"), inner.get("name")) if isinstance(inner, dict) else None
    from_flat = _pair(args.get("doctype") or args.get("dt"), args.get("name") or args.get("dn"))
    if from_doc and from_flat and from_doc != from_flat:
        return "conflict"
    return from_doc or from_flat


def classify_method(method, args):
    """A whitelisted method call: POST /api/(v2/)method/<method>, or Frappe MCP's call_method."""
    method = str(method or "")
    args = _as_obj(args)
    args = args if isinstance(args, dict) else {}
    rule = write_rule(method)
    if rule is None and method in CREATE_ONLY:
        docs = [_as_obj(args.get("doc"))] if "doc" in args else (_as_obj(args.get("docs")) or [])
        docs = docs if isinstance(docs, list) else []
        if method.endswith("upload_file") and args.get("fieldname") and (args.get("doctype") or args.get("docname")):
            p = _pair(args.get("doctype"), args.get("docname"))
            return ("need", [p]) if p else ("unnamed", [])   # setting a field on a record changes it
        parents = _parent_pairs(docs)
        return ("need", parents) if parents else ("allow", [])
    if rule is None and is_read_only(method):
        return "allow", []
    if rule == "doc":
        inner = _as_obj(args.get("doc"))
        p = _pair(inner.get("doctype"), inner.get("name")) if isinstance(inner, dict) else None
        flat = _pair(args.get("doctype"), args.get("name"))
        if not p or (flat and flat != p):
            return "unnamed", []
        return "need", [p]
    if rule == "flat":
        p = _pair(args.get("doctype"), args.get("name"))
        inner = _as_obj(args.get("doc"))
        other = _pair(inner.get("doctype"), inner.get("name")) if isinstance(inner, dict) else None
        if not p or (other and other != p):
            return "unnamed", []
        return "need", [p]
    if rule == "rename":
        dt, old, new = args.get("doctype"), args.get("old_name"), args.get("new_name")
        p = _pair(dt, old)
        if not p or (args.get("name") and str(args.get("name")) != str(old)):
            return "unnamed", []
        merge = str(args.get("merge")).lower() in ("1", "true", "yes")
        if merge:
            q = _pair(dt, new)
            return ("need", [p, q]) if q else ("unnamed", [])
        return "need", [p]
    if rule == "delete_items":
        dt, items = args.get("doctype"), _as_obj(args.get("items"))
        names = [str(i) for i in items] if isinstance(items, list) else []
        return ("need", [(str(dt), n) for n in names]) if dt and names else ("unnamed", [])
    if rule == "bulk_update":
        docs = _as_obj(args.get("docs"))
        pairs = [_pair(d.get("doctype"), d.get("docname") or d.get("name")) for d in docs if isinstance(d, dict)] \
            if isinstance(docs, list) else []
        return ("need", pairs) if pairs and all(pairs) else ("unnamed", [])
    if rule == "import":
        di = args.get("data_import")
        return ("import", [("Data Import", str(di))]) if di else ("unnamed", [])
    named = _named(args)
    if named == "conflict":
        return "unnamed", []
    if named:
        return "need", [named]
    return "unknown", []


def classify_doc_method(doctype, name, method):
    """A method run on one record: /document/<doctype>/<name>/method/<method>, or MCP's call_document_method."""
    if str(method or "") in READ_ONLY_DOC_METHODS:
        return "allow", []
    return ("need", [(str(doctype), str(name))]) if doctype and name else ("unnamed", [])


def import_targets(import_record, preview):
    """What starting a Data Import needs snapshots of: the import record, and for an update import every record
    the file changes, read from the import's dry run (get_preview_from_template), which saves nothing.
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
    idx = [i for i, c in enumerate(cols) if isinstance(c, dict) and (c.get("df") or {}).get("fieldname") == "name"
           and (c.get("df") or {}).get("parent") in (None, "", dt)]   # the record's own ID, not a child row's
    rows = preview.get("data") or []
    if not idx or not rows:
        return None
    names = {str(r[idx[0]]) for r in rows if isinstance(r, list) and len(r) > idx[0] and r[idx[0]] not in (None, "")}
    if len(names) != len(rows):
        return None                             # a row without an ID: cannot tell what it changes
    return pairs + [(str(dt), n) for n in sorted(names)]


def snapshot_pairs(data, inherited=None, out=None):
    """Every (doctype, name) a snapshot holds. A record counts when it names both, or when it sits in a list
    under something that names the doctype (a list read returns names without the doctype)."""
    out = set() if out is None else out
    if isinstance(data, dict):
        dt = data.get("doctype") if isinstance(data.get("doctype"), str) else inherited
        if dt and isinstance(data.get("name"), (str, int)):
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
            yield json.loads(raw.read_text(encoding="utf-8", errors="replace"))
        except (OSError, ValueError):
            continue


def snapshotted(ws, window=WINDOW):
    """All (doctype, name) pairs in the workspace's snapshots from the last `window` seconds."""
    found = set()
    for data in _snapshots(ws, window):
        found |= snapshot_pairs(data)
    return found


def snapshotted_record(ws, doctype, name, window=WINDOW):
    """The fields of one snapshotted record (merged from every copy of it), or {} when none holds it."""
    fields = {}

    def walk(v):
        if isinstance(v, dict):
            if v.get("doctype") == doctype and str(v.get("name")) == str(name):
                fields.update({k: x for k, x in v.items() if not isinstance(x, (dict, list))})
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)

    for data in _snapshots(ws, window):
        walk(data)
    return fields


def missing_snapshots(ws, pairs, window=WINDOW):
    """The pairs that no snapshot from the last `window` seconds holds exactly."""
    have = snapshotted(ws, window)
    return [(str(a), str(b)) for a, b in pairs if (str(a), str(b)) not in have]
