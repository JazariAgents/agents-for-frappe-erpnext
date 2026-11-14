"""The plugin's one set of snapshot rules, shared by the API helper (frappe_call.py) and the MCP guard hook
(hooks/frappe_guard.py), so the two can never disagree about which calls change existing records.

A call is classified as one of:
  ("allow", [])      reads, creates something new, or returns an unsaved draft (ERPNext's make_* mappers)
  ("need", pairs)    changes these existing records: each (doctype, name) needs a snapshot from the last hour
  ("unnamed", [])    a known write that does not say which records it touches: refused
  ("unknown", [])    not a known read or write and names no record: the MCP guard asks the user first
"""
import json
import time
from pathlib import Path

WINDOW = 3600  # a snapshot counts for one hour

# known writes, by full dotted name; WRITE_LAST also catches the same last part under any other module
WRITE_METHODS = {
    "frappe.client.submit", "frappe.client.cancel", "frappe.client.delete", "frappe.client.set_value",
    "frappe.client.save", "frappe.client.rename_doc", "frappe.model.rename_doc", "frappe.client.bulk_update",
    "frappe.desk.reportview.delete_items", "frappe.core.doctype.data_import.data_import.form_start_import",
}
WRITE_LAST = {m.rsplit(".", 1)[-1] for m in WRITE_METHODS}
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


def is_write(method):
    return method in WRITE_METHODS or _last(method) in WRITE_LAST


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


def classify_method(method, args):
    """A whitelisted method call: POST /api/(v2/)method/<method>, or Frappe MCP's call_method."""
    method = str(method or "")
    args = _as_obj(args)
    args = args if isinstance(args, dict) else {}
    if method in CREATE_ONLY or _last(method) in CREATE_ONLY:
        return "allow", []
    if is_read_only(method):
        return "allow", []
    last = _last(method)
    if last == "delete_items":
        dt, items = args.get("doctype"), _as_obj(args.get("items"))
        names = [str(i) for i in items] if isinstance(items, list) else []
        return ("need", [(dt, n) for n in names]) if dt and names else ("unnamed", [])
    if last == "bulk_update":
        docs = _as_obj(args.get("docs"))
        pairs = [(d.get("doctype"), d.get("docname") or d.get("name")) for d in docs if isinstance(d, dict)] \
            if isinstance(docs, list) else []
        return ("need", pairs) if pairs and all(a and b for a, b in pairs) else ("unnamed", [])
    if last == "form_start_import":
        di = args.get("data_import")
        return ("need", [("Data Import", str(di))]) if di else ("unnamed", [])
    inner = _as_obj(args.get("doc"))
    doc = inner if isinstance(inner, dict) else args
    target = (doc.get("doctype") or doc.get("dt"), doc.get("name") or doc.get("dn"))
    if all(target):
        return "need", [(str(target[0]), str(target[1]))]
    return ("unnamed", []) if is_write(method) else ("unknown", [])


def classify_doc_method(doctype, name, method):
    """A method run on one record: /document/<doctype>/<name>/method/<method>, or MCP's call_document_method."""
    if str(method or "") in READ_ONLY_DOC_METHODS:
        return "allow", []
    return ("need", [(str(doctype), str(name))]) if doctype and name else ("unnamed", [])


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


def snapshotted(ws, window=WINDOW):
    """All (doctype, name) pairs in the workspace's snapshots from the last `window` seconds."""
    found = set()
    snaps = Path(ws) / ".frappe" / "snapshots"
    if not snaps.is_dir():
        return found
    now = time.time()
    for d in snaps.iterdir():
        raw = d / "raw.json"
        try:
            if not raw.is_file() or now - raw.stat().st_mtime > window:
                continue
            found |= snapshot_pairs(json.loads(raw.read_text(encoding="utf-8", errors="replace")))
        except (OSError, ValueError):
            continue
    return found


def missing_snapshots(ws, pairs, window=WINDOW):
    """The pairs that no snapshot from the last `window` seconds holds exactly."""
    have = snapshotted(ws, window)
    return [(str(a), str(b)) for a, b in pairs if (str(a), str(b)) not in have]
