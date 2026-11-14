#!/usr/bin/env python3
"""UserPromptSubmit hook: in a folder connected to a Frappe site, remind the model to work through this plugin,
and record that the user has just sent a message.

Testing showed that with Frappe's MCP tools connected, a request such as "delete customer X" was carried out
straight through the MCP tool, without loading any skill, so none of the safety rules applied. This adds one short
line of context to each request in a connected folder (one that holds .frappe/state.json, sits below one that
does, or sits just above one). Outside such a folder it prints nothing and writes nothing.

It also writes the time of the message to .frappe/.last_user_message. The guard and the API helper use it to hold
a change until the user has replied after its snapshot was saved: testing showed an agent could save the backup
and make the change in the same turn, without waiting for a yes. Run with --answered (after the user answers a
question the model asked), it records the time and prints nothing.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills" / "frappe-connect" / "scripts"))


def workspaces(start):
    try:
        import frappe_safety as fs
        return fs.find_workspaces(start), fs
    except Exception:
        found = []
        for base in (start, os.environ.get("CLAUDE_PROJECT_DIR")):
            if not base:
                continue
            here = Path(base).resolve()
            for d in [here, *here.parents]:
                if (d / ".frappe" / "state.json").is_file():
                    return [d], None
        return found, None


def main():
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
    except (ValueError, OSError):
        data = {}
    if not isinstance(data, dict):
        data = {}
    found, fs = workspaces(data.get("cwd") or os.getcwd())
    if not found:
        return
    if fs:
        fs.note_user_message(found)
    if "--answered" in sys.argv:
        return
    ws = found[0]
    try:
        st = json.loads((ws / ".frappe" / "state.json").read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        st = {}
    if not isinstance(st, dict):
        st = {}
    site = st.get("site_url") or st.get("site") or "the connected site"
    env = st.get("environment") or "unknown environment"
    msg = (f"This folder is connected to a Frappe/ERPNext site ({site}, {env}) through the jazari-frappe-erpnext plugin. "
           "Before reading or changing anything on that site, load the jazari-frappe-erpnext skill that matches the request "
           "(frappe-api for records no module skill names) and follow its guardrails: snapshot before any change, state "
           "the reversibility and count, wait for a clear yes, and use the plugin's frappe_call.py for API-key calls. "
           "The request itself is never the yes: save the snapshot, say what will change, and stop; the plugin holds a "
           "change until the user has replied after its snapshot was saved. This applies to Frappe's MCP tools too.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
