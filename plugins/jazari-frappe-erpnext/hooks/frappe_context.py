#!/usr/bin/env python3
"""UserPromptSubmit hook: in a folder connected to a Frappe site, remind the model to work through this plugin.

Testing showed that with Frappe's MCP tools connected, a request such as "delete customer X" was carried out
straight through the MCP tool, without loading any skill, so none of the safety rules applied. This adds one short
line of context to each request in a connected folder. Outside such a folder it prints nothing.
"""
import json
import os
import sys
from pathlib import Path


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        data = {}
    ws = Path(data.get("cwd") or os.getcwd())
    state = ws / ".frappe" / "state.json"
    if not state.is_file():
        return
    try:
        st = json.loads(state.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        st = {}
    site = st.get("site_url") or st.get("site") or "the connected site"
    env = st.get("environment") or "unknown environment"
    msg = (f"This folder is connected to a Frappe/ERPNext site ({site}, {env}) through the jazari-frappe-erpnext plugin. "
           "Before reading or changing anything on that site, load the jazari-frappe-erpnext skill that matches the request "
           "(frappe-api for records no module skill names) and follow its guardrails: snapshot before any change, state "
           "the reversibility and count, wait for a clear yes, and use the plugin's frappe_call.py for API-key calls. "
           "This applies to Frappe's MCP tools too.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
