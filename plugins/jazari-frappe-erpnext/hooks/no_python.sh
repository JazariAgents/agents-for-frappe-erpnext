#!/bin/sh
# Runs only when neither python3 nor python could run the safety guard (hooks/frappe_guard.py).
# Without Python the guard cannot check a change against its snapshot, so in a folder that is connected to
# a Frappe site the user is asked before the change goes ahead. Anywhere else, nothing happens.
# It prints an "ask" decision or nothing: it never approves a call and never changes one.
if [ -f .frappe/state.json ]; then
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"The Jazari Agents safety guard needs Python 3.8 or later and could not run it, so it cannot check this change against a snapshot. Allow it only if a snapshot of the record exists."}}'
fi
exit 0
