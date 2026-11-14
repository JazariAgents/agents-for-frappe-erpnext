# Security

## Reporting a problem

Please do not open a public issue for a security problem. Write to **rami@infoney.tech** with what you
found and how to reproduce it.

## What this plugin does with your data

- **Credentials.** With Frappe's MCP server or `frappectl`, sign-in happens in your browser or your
  system keyring and the plugin never sees a secret. With an API key, the key is kept in
  `.frappe/credentials.txt` in your own workspace; the skills are instructed never to print it, log it or
  copy it into a snapshot, and the workspace folder gets a `.gitignore` that excludes everything in it.
- **Your records.** Snapshots, the audit log, the task log and the activity log are written to the
  `.frappe/` folder on your machine. Nothing is sent to Jazari Agents.
- **The dashboard.** The page carries its figures inside itself. Its only network request is to Google
  Fonts for three typefaces. If you publish the page, you are publishing those figures: check who can
  open the link.
- **Text from your site.** Customer names, notes and messages are treated as data. The skills are
  instructed never to follow instructions found inside a record.

## What it enforces, and what it cannot guarantee

Two safety rules are enforced in code, not just asked for. In a folder connected to a Frappe site, the
plugin's hook refuses any change or delete made through Frappe's MCP tools unless that exact record has a
snapshot from the last hour, and the plugin's API helper (`frappe_call.py`) does the same for calls made
with an API key. The helper also keeps the key out of everything it prints. Both use one set of rules,
`skills/frappe-connect/scripts/frappe_safety.py`.

The other confirmations (stating whether a change can be undone, waiting for your yes) are instructions that
Claude follows, not locks. A hook cannot stop a request sent some other way, such as a command you approve
in your terminal. For a hard guarantee on a production site, connect with a read-only `frappectl` profile:
it stops write requests on your machine before they are sent.
