#!/usr/bin/env python3
"""PreToolUse guard for Frappe's own MCP server.

When the session is in a folder connected to a Frappe site (it, or a folder above it, holds .frappe/state.json),
a change made through an MCP tool (update_document, delete_document, call_document_method, a writing call_method,
or a create_document that adds a row to an existing record or overwrites a settings record) is refused unless a
snapshot of every record it changes was written to .frappe/snapshots/ in the last hour. Creating a new record is
allowed: nothing existing is touched. A method the plugin does not recognise, which names no record, is put to
the user. If the guard itself fails or cannot read the call, the user is asked too: a broken guard never lets a
change through silently.

The yes is checked as well. A change is put to the user (Claude Code's own permission prompt) when its snapshot
was saved after the user's last message: nothing then shows the user was told what will change. The plugin's
other hook (frappe_context.py) records the time of each message and each answered question.

The rules are the plugin's one shared set, skills/frappe-connect/scripts/frappe_safety.py, which the API helper
uses as well. The model still has to state the reversibility and get the user's yes; this hook makes the snapshot
step impossible to skip, which testing showed was needed: with the MCP tools connected, an agent deleted a record
without one. Outside a connected folder the hook does nothing.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills" / "frappe-connect" / "scripts"))


def out(decision=None, reason=""):
    if decision:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                                 "permissionDecisionReason": reason}}))
    sys.exit(0)


def main():
    import frappe_safety as fs                  # if this fails, the handler below asks the user

    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))   # UTF-8 whatever the console's code page
    except (ValueError, OSError):
        data = None
    if not isinstance(data, dict):
        # No readable hook input, so the call cannot be checked. In a connected folder, ask the user.
        if fs.find_workspaces(os.getcwd()):
            out("ask", "The Jazari Agents safety guard could not read this call, so it cannot check it against "
                       "a snapshot. Allow it only if a snapshot of the record exists.")
        out()
    ws = fs.find_workspaces(data.get("cwd") or os.getcwd())   # here, above, or (started above it) just below
    if not ws:
        out()                                   # not a Frappe workspace: nothing to guard
    tool = str(data.get("tool_name") or "").split("__")[-1]
    args = data.get("tool_input")
    if isinstance(args, dict) and ("method" if tool == "call_method" else "doctype") not in args:
        out()                                   # not shaped like a Frappe tool: another server's tool of the same name
    args = args if isinstance(args, dict) else {}
    doctype, name = args.get("doctype"), args.get("name")
    if tool in ("update_document", "delete_document"):
        verdict = fs.classify_doc_method(doctype, name, tool)    # every update and delete needs the record
    elif tool == "call_document_method":
        verdict = fs.classify_doc_method(doctype, name, args.get("method"))
    elif tool == "call_method":
        verdict = fs.classify_method(args.get("method"), args.get("args"))
        made = [d for d in fs.method_creates(args.get("method"), args.get("args")) if fs.settings_like(d)]
        if verdict[0] == "allow" and made:
            out("ask", f"Jazari Agents safety rule: {made[0]} looks like a settings record type. If it is one, "
                       "creating it replaces the stored settings, and the plugin cannot tell from here. Allow it "
                       "only if this is a new record, or snapshot the settings first and update them instead.")
    elif tool == "create_document":
        verdict = fs.classify_create(doctype, args.get("data"))
        if verdict[0] == "allow" and fs.settings_like(doctype):
            out("ask", f"Jazari Agents safety rule: {doctype} looks like a settings record type. If it is one, "
                       "creating it replaces the stored settings, and the plugin cannot tell from here. Allow it "
                       "only if this is a new record, or snapshot the settings first and update them instead.")
    else:
        out()                                   # reads and anything else: allowed
    kind, pairs = verdict
    if kind == "allow":
        out()
    if kind == "unknown":
        out("ask", f"Jazari Agents safety rule: {args.get('method') or 'this method'} is not a known read-only "
                   "call and names no record, so the plugin cannot check it against a snapshot. Allow it only if "
                   "you know it changes nothing you would want back.")
    if kind == "unnamed":
        out("deny", "Jazari Agents safety rule: this call changes records but does not say which ones (record "
                    "type and name), or names them inconsistently, so their snapshot cannot be checked and it is "
                    "blocked. Name the records, snapshot them, and try again.")
    missing = fs.missing_snapshots(ws, pairs)
    if not missing and kind == "import":
        rec = fs.snapshotted_record(ws, *pairs[0])
        if rec.get("import_type") == "Insert New Records":
            out()                               # adds records only; the import record itself is snapshotted
        out("deny", "Jazari Agents safety rule: this import updates existing records (or its type is not in the "
                    "snapshot), and the guard cannot list those records without the site. Start it with the "
                    "plugin's helper, frappe_call.py, which reads them from the import's file and checks each "
                    "one has a snapshot, or ask the user to start it from the Data Import screen.")
    if not missing and len(ws) > 1:
        # Started above several connected folders: a backup in one must not cover a change on another site.
        names = ", ".join(sorted(w.name for w in ws)[:6])
        out("ask", f"Jazari Agents safety rule: this session sits above more than one folder connected to a Frappe "
                   f"site ({names}). A backup of this record exists in one of them, but the plugin cannot tell "
                   "which site this change is for. Allow it only if you are sure. Better: start Claude inside the "
                   "folder of the site you mean.")
    if not missing:
        late = fs.unconfirmed(ws, pairs)
        if late:
            which = ", ".join(f"{a} {b}" for a, b in late[:5]) + (f" and {len(late) - 5} more" if len(late) > 5 else "")
            out("ask", f"Jazari Agents: Claude is about to change {which}. A backup was saved, but you have not "
                       "replied since then, so you may not have been told what will change. Allow it only if you "
                       "want this change made now; otherwise deny it and ask Claude to explain first.")
        out()
    what = ", ".join(f"{a} {b}" for a, b in missing[:5]) + (f" and {len(missing) - 5} more" if len(missing) > 5 else "")
    out("deny",
        f"Jazari Agents safety rule: no snapshot of {what} was saved in the last hour, so this change is blocked. "
        "Load the matching jazari-frappe-erpnext skill, save a snapshot of each record into .frappe/snapshots/ "
        "(raw.json holding each record in full as read from the site, with its doctype, name and modified time; a "
        "list of names is not a snapshot), tell the user the reversibility class and the count, get a clear yes, "
        "then try again.")


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
