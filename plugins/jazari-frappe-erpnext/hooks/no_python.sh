#!/bin/sh
# Runs only when neither python3 nor python could run the safety guard (hooks/frappe_guard.py).
# Without Python the guard cannot check a change against its snapshot, so the user is asked before any call
# that is shaped like a change to a Frappe site: one that names a doctype, or Frappe's call_method tool.
# It does not look at folders at all, so it works the same wherever the session is. A tool of the same name
# from another server, which names no doctype, is left alone.
# It prints an "ask" decision or nothing: it never approves a call and never changes one.
if grep -q -e '"doctype"' -e '__call_method"'; then
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"The Jazari Agents safety guard needs Python 3.8 or later and could not run it, so it cannot check this change to your Frappe site against a snapshot. Allow it only if a snapshot of the record exists."}}'
fi
exit 0
