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

The snapshot rule is enforced in code, not just asked for. In a folder connected to a Frappe site:

- The plugin's hook refuses a change or delete made through Frappe's MCP tools unless that exact record is in
  a snapshot from the last hour. A method it does not recognise is put to you first.
- The plugin's API helper (`frappe_call.py`) applies the same rule to calls made with an API key, for every
  HTTP verb and every form of the address, and refuses a call it does not recognise. It also keeps the key
  out of everything it prints.
- A snapshot counts only when it holds the record in full, as read from the site. A list of names does not.
- The yes is held too. A change waits until you have replied after its snapshot was saved: through the MCP
  tools you get Claude Code's own permission prompt, and the API helper refuses the call. This shows that
  you replied, not what you said; reading your answer is still Claude's job.
- If the hook cannot run (no Python, or an error), it asks you instead of letting the change through.

Both use one set of rules, `skills/frappe-connect/scripts/frappe_safety.py`.

What this does not cover:

- The hook runs in Claude Code and Cowork. In claude.ai chat, hooks do not run, so there the rule is an
  instruction Claude follows.
- Saying whether a change can be undone, and the 25-record stop, are instructions that Claude follows, not
  locks. Creating a new record is not held: nothing existing changes.
- A snapshot covers its record for an hour, so a second change to the same record in that hour is not
  backed up again.
- A hook cannot stop a request sent some other way, such as a command you approve in your terminal.

For a hard guarantee on a production site, connect with a read-only `frappectl` profile: it stops write
requests on your machine before they are sent.
