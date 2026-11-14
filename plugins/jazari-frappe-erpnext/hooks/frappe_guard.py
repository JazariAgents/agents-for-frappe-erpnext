#!/usr/bin/env python3
"""PreToolUse guard for Frappe's own MCP server.

When the current folder is connected to a Frappe site (it holds .frappe/state.json), a change made through an MCP
tool such as update_document, delete_document, call_document_method or a writing call_method is refused unless a
snapshot of every record it changes was written to .frappe/snapshots/ in the last hour. Creating a new record is
allowed: nothing existing is touched. A method the plugin does not recognise, which names no record, is put to the
user. If the guard itself fails, the user is asked too: a broken guard never lets a change through silently.

The rules are the plugin's one shared set, skills/frappe-connect/scripts/frappe_safety.py, which the API helper
uses as well. The model still has to state the reversibility and get the user's yes; this hook makes the snapshot
step impossible to skip, which testing showed was needed: with the MCP tools connected, an agent deleted a record
without one. Outside a connected folder the hook does nothing.
"""
import json
import os
import sys
from pathlib import Path


def out(decision=None, reason=""):
    if decision:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                                 "permissionDecisionReason": reason}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        out()
    if not isinstance(data, dict):
        out()
    ws = Path(data.get("cwd") or os.getcwd())
    if not (ws / ".frappe" / "state.json").is_file():
        out()                                   # not a Frappe workspace: nothing to guard
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills" / "frappe-connect" / "scripts"))
    import frappe_safety as fs                  # if this fails, the handler below asks the user

    tool = (data.get("tool_name") or "").split("__")[-1]
    args = data.get("tool_input") or {}
    doctype, name = args.get("doctype"), args.get("name")
    if tool in ("update_document", "delete_document"):
        verdict = ("need", [(doctype, name)]) if doctype and name else ("unnamed", [])
    elif tool == "call_document_method":
        verdict = fs.classify_doc_method(doctype, name, args.get("method"))
    elif tool == "call_method":
        verdict = fs.classify_method(args.get("method"), args.get("args"))
    else:
        out()                                   # reads, create_document and anything else: allowed
    kind, pairs = verdict
    if kind == "allow":
        out()
    if kind == "unknown":
        out("ask", f"Jazari Agents safety rule: {args.get('method') or 'this method'} is not a known read-only "
                   "call and names no record, so the plugin cannot check it against a snapshot. Allow it only if "
                   "you know it changes nothing you would want back.")
    if kind == "unnamed":
        out("deny", "Jazari Agents safety rule: this call changes records but does not say which ones (record "
                    "type and name), so their snapshot cannot be checked and it is blocked. Name the records, "
                    "snapshot them, and try again.")
    missing = fs.missing_snapshots(ws, pairs)
    if not missing:
        out()
    what = ", ".join(f"{a} {b}" for a, b in missing[:5]) + (f" and {len(missing) - 5} more" if len(missing) > 5 else "")
    out("deny",
        f"Jazari Agents safety rule: no snapshot of {what} was saved in the last hour, so this change is blocked. "
        "Load the matching jazari-frappe-erpnext skill, save a snapshot of each record into .frappe/snapshots/ "
        "(raw.json with the record as read from the site, carrying its doctype and name), tell the user the "
        "reversibility class and the count, get a clear yes, then try again.")


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
