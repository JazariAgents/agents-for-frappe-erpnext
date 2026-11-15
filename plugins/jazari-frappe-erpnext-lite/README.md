# Jazari Agents for Frappe & ERPNext Lite

Run ERPNext and the other Frappe apps by talking to Claude. Nine specialist agents know how the work is
really done, ask before they change anything, and keep a copy of what they change. Everything works in
English and Arabic.

This is the **Lite** edition, made for Claude's plugin directory: the same skills, agents and bundled
documentation as the full edition, with no code of its own. The full edition, with a one-page dashboard
and its safety rules locked in code, is at https://github.com/JazariAgents/agents-for-frappe-erpnext.

This is an independent, MIT-licensed project by Jazari Agents. It is not made or endorsed by Frappe
Technologies. Frappe and ERPNext are their trademarks.

## What you can ask for

- **Daily work in ERPNext**: quotations, orders, invoices, payments, purchases, stock, manufacturing,
  projects, and the accounting behind them.
- **The other Frappe apps**: HR and payroll, CRM, Helpdesk, Learning, Lending, Insights, the website and
  Builder.
- **Bulk work**: import a spreadsheet with a dry run first, or change many records at once with a count
  and a confirmation.
- **Setup and administration**: users and permissions, naming, print formats, bench commands, building
  apps and DocTypes.
- **The business at a glance**: ask "how is the business doing?" for a short, read-only table of counts
  from your live site: unpaid and overdue invoices, open orders, people, support and system health.
- **Undo**: ask "what have you done?" or "restore that" to see the log and put a snapshot back.

## What you need

- A site on Frappe v16. For Frappe's MCP connector, v16.53 or later; for `frappectl`, v16 or later.
  Older sites can be worked through the interface, with the agent guiding you.
- For changes to your data: Claude Code or the Code tab of the Claude desktop app, started in your working
  folder, so the safety copies and the `CLAUDE.md` note have a home. Cowork has not been tested with the
  note yet.
- Your own Claude subscription.

## Start

Say **"connect my ERPNext site"**. The agent asks which language you want and picks the best way to
connect, in this order: Frappe's built-in MCP server (you add it as a connector and sign in in your
browser), Frappe's `frappectl` command-line tool (you sign in yourself), or no connection at all (it then
walks you through the screens). You never type a password or an API key into the chat.

## How it protects your data

- It reads the record before it writes, and tells you what will change and how many records.
- It saves a snapshot of every record before changing or deleting it, and tells you first when something
  cannot be undone, such as a submitted invoice.
- It asks, then waits for your reply before it makes the change.
- It treats text inside your records as data, never as instructions.
- It keeps a task log and an audit log in your folder.

In this edition those are rules Claude follows: the plugin has no code that can block a call. The full
edition adds two locks in code, for the snapshot and for your reply.

**Say yes to the `CLAUDE.md` note.** When you connect, the agent asks to add a short note to `CLAUDE.md`
in your working folder, which Claude reads at the start of every session there. It tells Claude to run
the safety steps before any change to your site. In our tests, without it, Claude sometimes made a quick
change ("close this ToDo") straight away, without a snapshot or a question; with it, every change waited
for a snapshot and your reply. Keep your Claude app asking you before a connector's tools change data, as
a second check.

## What it runs, sends and stores

- **It runs** nothing of its own: no scripts, no hooks. Claude uses the connections you set up (Frappe's
  MCP server, or `frappectl` and `bench` commands that your Claude app asks you to allow).
- **It sends** requests only to the Frappe site you connect, through those connections. Nothing is sent
  to Jazari Agents or anyone else. There is no telemetry.
- **It stores** everything in a `.frappe/` folder inside your own working folder: the connection details
  (never a key or a password), snapshots, and the logs. With your OK it also adds one marked note to
  `CLAUDE.md` in that folder; it changes nothing else in that file.

## What is inside

- 24 skills: the full edition's 23, plus `frappe-safe-change`, which holds the safety steps for every
  change. Most carry step-by-step guides for the connection and for the browser; the bench guides cover
  the server.
- 1,612 pages of official Frappe documentation in `docs/`, so the agent reads the real page instead of
  guessing. They are packed into a few files per product, and `docs/INDEX.md` says which file and lines hold
  each page. They are Frappe's, under CC BY-SA; see `NOTICE.md`.
- A manual in English and Arabic (`manual/`): ask any agent to "show the manual".

## Lite or full?

| | Lite | Full |
|---|---|---|
| Skills, agents and documentation | All | All |
| Connects through | Frappe's MCP server, frappectl, the interface, bench | The same, plus an API-key helper |
| Snapshot and your yes before a change | Rules Claude follows, reached through a note in your `CLAUDE.md` | The same rules, plus two locks in code |
| Dashboard | A table of counts in the chat | Jazari Pulse, a one-page dashboard with six screens |
| Needs Python | No | For the locks, the key helper and the dashboard |

Install one of them, not both.

## What was tested

See the manual, "What was tested, and what was not".

## Help

Open an issue at https://github.com/JazariAgents/agents-for-frappe-erpnext/issues, say that you use the
Lite edition, and which Frappe and ERPNext versions you run. For a security problem, see `SECURITY.md`
in that repository.

## Licence

MIT for the plugin (`LICENSE.txt`). The bundled documentation in `docs/` is CC BY-SA, by Frappe
Technologies and contributors (`NOTICE.md`).
