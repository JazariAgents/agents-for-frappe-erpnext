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
READ_ONLY_METHOD_HINTS = (".make_", ".get_", "get_", "frappe.desk.query_report.run", "frappe.client.get",
                          "frappe.client.get_count", "frappe.client.get_list", "frappe.client.get_value",
                          "get_preview_from_template", "trial_run", "get_runs", "get_automation_capabilities")
WRITE_METHODS = ("frappe.client.submit", "frappe.client.cancel", "frappe.client.delete", "frappe.client.set_value",
                 "frappe.client.save", "frappe.client.rename_doc", "frappe.model.rename_doc", "form_start_import",
                 "frappe.client.bulk_update", "frappe.desk.reportview.delete_items", "frappe.client.insert_many")


def out(decision=None, reason=""):
    if decision:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                                 "permissionDecisionReason": reason}}))
    sys.exit(0)


def snapshot_has(ws, doctype, name):
    snaps = ws / ".frappe" / "snapshots"
    if not snaps.is_dir():
        return False
    now = time.time()
    for d in snaps.iterdir():
        raw = d / "raw.json"
        if not raw.is_file() or now - raw.stat().st_mtime > WINDOW:
            continue
        try:
            text = raw.read_text(encoding="utf-8", errors="replace")
            json.loads(text)
        except (OSError, ValueError):
            continue
        if (not doctype or doctype in text) and (not name or str(name) in text):
            return True
    return False


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
        if any(h in method for h in READ_ONLY_METHOD_HINTS) and not any(w in method for w in WRITE_METHODS):
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
        if not (doctype and name) and not any(w in method for w in WRITE_METHODS):
            out()                               # an unknown method that names no record: leave it to the rules
    if tool not in ("update_document", "delete_document", "call_document_method", "call_method"):
        out()
    if snapshot_has(ws, doctype, name):
        out()
    what = f"{doctype} {name}" if doctype and name else "the records this call changes"
    out("deny",
        f"Jazari Agents safety rule: no snapshot of {what} was saved in the last hour, so this change is blocked. "
        "Load the matching jazari-frappe-erpnext skill, save a snapshot of the record into .frappe/snapshots/ "
        "(raw.json with the record as read from the site), tell the user the reversibility class and the count, "
        "get a clear yes, then try again.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:                           # a broken guard must never break the session
        sys.exit(0)
