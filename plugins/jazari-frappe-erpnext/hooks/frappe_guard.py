#!/usr/bin/env python3
"""PreToolUse guard for Frappe's own MCP server.

When the current folder is connected to a Frappe site (it holds .frappe/state.json), a change made through an MCP
tool such as update_document, delete_document or call_document_method is refused unless a snapshot of that record
was written to .frappe/snapshots/ in the last hour. Creating a new record is allowed: nothing existing is touched.

The model still has to state the reversibility and get the user's yes; this hook makes the snapshot step impossible
to skip, which testing showed was needed: with the MCP tools connected, an agent deleted a record without one.
Outside a connected folder the hook does nothing.
"""
import json
import os
import sys
import time
from pathlib import Path

WINDOW = 3600          # a snapshot counts for one hour
# read-only calls, matched on the method's last part, never as a substring of the whole name
READ_ONLY_PREFIXES = ("get_", "make_")          # make_* are ERPNext's mappers: they return an unsaved draft
READ_ONLY_EXACT = {"frappe.desk.query_report.run", "frappe.client.get", "frappe.client.get_count",
                   "frappe.client.get_list", "frappe.client.get_value", "frappe.client.get_single_value",
                   "frappe.desk.reportview.get", "frappe.desk.reportview.get_count", "trial_run", "get_runs",
                   "get_automation_capabilities", "get_preview_from_template"}
WRITE_METHODS = ("frappe.client.submit", "frappe.client.cancel", "frappe.client.delete", "frappe.client.set_value",
                 "frappe.client.save", "frappe.client.rename_doc", "frappe.model.rename_doc", "form_start_import",
                 "frappe.client.bulk_update", "frappe.desk.reportview.delete_items", "frappe.client.insert_many")


def out(decision=None, reason=""):
    if decision:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                                 "permissionDecisionReason": reason}}))
    sys.exit(0)


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


def snapshot_has(ws, doctype, name):
    """True only when a snapshot from the last hour holds exactly this record."""
    if not (doctype and name):
        return False
    snaps = ws / ".frappe" / "snapshots"
    if not snaps.is_dir():
        return False
    now = time.time()
    for d in snaps.iterdir():
        raw = d / "raw.json"
        try:
            if not raw.is_file() or now - raw.stat().st_mtime > WINDOW:
                continue
            data = json.loads(raw.read_text(encoding="utf-8", errors="replace"))
        except (OSError, ValueError):
            continue
        if (str(doctype), str(name)) in snapshot_pairs(data):
            return True
    return False


def read_only(method):
    last = method.rsplit(".", 1)[-1]
    return method in READ_ONLY_EXACT or last in READ_ONLY_EXACT or last.startswith(READ_ONLY_PREFIXES)


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        out()
    ws = Path(data.get("cwd") or os.getcwd())
    if not (ws / ".frappe" / "state.json").is_file():
        out()                                   # not a Frappe workspace: nothing to guard
    tool = (data.get("tool_name") or "").split("__")[-1]
    args = data.get("tool_input") or {}
    doctype, name = args.get("doctype"), args.get("name")
    if tool == "create_document":
        out()
    if tool == "call_method":
        method = str(args.get("method") or "")
        if method not in WRITE_METHODS and read_only(method):
            out()
        inner = args.get("args") or {}
        if isinstance(inner, str):
            try:
                inner = json.loads(inner)
            except ValueError:
                inner = {}
        doc = inner.get("doc") if isinstance(inner, dict) else None
        if isinstance(doc, dict):
            doctype, name = doc.get("doctype"), doc.get("name")
        elif isinstance(inner, dict):
            doctype, name = inner.get("doctype"), inner.get("name")
        if not (doctype and name):
            if method in WRITE_METHODS:
                out("deny", f"Jazari Agents safety rule: {method} changes a record, but this call does not name "
                            "the record type and name, so its snapshot cannot be checked. Name the record, snapshot "
                            "it, and try again.")
            out("ask", f"Jazari Agents safety rule: {method or 'this method'} is not a known read-only call and "
                       "names no record, so the plugin cannot check it against a snapshot. Allow it only if you "
                       "know it changes nothing you would want back.")
    if tool not in ("update_document", "delete_document", "call_document_method", "call_method"):
        out()
    if tool == "call_document_method" and str(args.get("method") or "").startswith(READ_ONLY_PREFIXES):
        out()                                   # a document method that only reads, such as get_preview_from_template
    if snapshot_has(ws, doctype, name):
        out()
    what = f"{doctype} {name}" if doctype and name else "the records this call changes"
    out("deny",
        f"Jazari Agents safety rule: no snapshot of {what} was saved in the last hour, so this change is blocked. "
        "Load the matching jazari-frappe-erpnext skill, save a snapshot of the record into .frappe/snapshots/ "
        "(raw.json with the record as read from the site, carrying its doctype and name), tell the user the reversibility class and the count, "
        "get a clear yes, then try again.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:                    # a broken guard must not silently allow a change
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask",
                                                 "permissionDecisionReason": "The Jazari Agents safety guard could "
                                                 f"not check this call ({type(exc).__name__}). Allow it only if a "
                                                 "snapshot of the record exists."}}))
        sys.exit(0)
