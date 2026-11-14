# Security

## Reporting a problem

Please do not open a public issue for a security problem. Write to **hello@jazariagents.com** with what you
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

## What it cannot guarantee

The confirmations, snapshots and refusals are instructions that Claude follows, not locks enforced in code.
For a hard guarantee on a production site, connect with a read-only `frappectl` profile: it stops write
requests on your machine before they are sent.
