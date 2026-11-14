# frappectl adapter — Frappe's official command-line client

## Contents

- when this applies
- first two commands, every session
- signing in
- read-only and writable profiles
- how the calls in `api.md` map to commands
- reports and read-only SQL
- writing through frappectl: what the tool does not do for you
- errors

`frappectl` is Frappe's own command-line client for REST API v2, built for agents that can run shell
commands. Secrets stay in the operating system's keyring or in a browser sign-in, so the agent never
sees them, and a new profile is **read-only**: write requests are stopped on the user's machine
before they are sent.

Sources: https://github.com/frappe/frappectl (v0.24.0, MIT) and
https://docs.frappe.io/framework/guides-integration/mcp (read 2026-11-14). The tool is young and
changes quickly; `frappectl guide` on the user's machine is the authority. If it disagrees with this
file, follow the guide and say so.

## When this applies

`state.json.active_adapter` is `frappectl`. **frappe-connect** sets that when this session can run
shell commands and `frappectl` is installed. It needs a site on Frappe v16 or later.

## First two commands, every session

```bash
frappectl guide
```

```bash
frappectl auth list
```

The guide prints the current command set on one screen and lists the user's site profiles, with
`[writable]` beside any profile that allows changes. Pass `-s <profile>` on every command when the
user has more than one site. Add `--json` to get clean JSON; errors go to stderr.

## Signing in

The user runs this themselves, in their own terminal. It opens a browser:

```bash
frappectl auth login https://erp.example.com --oauth --name erp --description "Production ERPNext"
```

Never put a key or secret in a command, a file or the chat. If `frappectl` is not installed, tell the
user the install command (`uv tool install frappectl` or `pip install frappectl`) and let them run
it; do not install software on their machine yourself.

## Read-only and writable profiles

- A profile is read-only unless the user created it with `--writable`.
- Reading always works: `doc list`, `doc get`, `doctype show`, `report run`.
- To call a whitelisted read method on a read-only profile, make the verb explicit:
  `frappectl api method/<dotted.path> -X GET`.
- **Only the user makes a profile writable**, with `frappectl auth configure <profile> --writable`.
  Never run that command yourself. If a change is refused because the profile is read-only, say so
  and tell the user the command; do not look for another route.
- Recommend that production stays read-only and changes go through a separate writable profile the
  user switches to on purpose.

## How the calls in `api.md` map

Keep the DocType from the skill's `api.md`, swap the call:

| `api.md` says | Command |
|---|---|
| `GET /api/v2/doctype/{doctype}/meta` | `frappectl doctype show "<DocType>" --json` |
| `GET /api/v2/document/{doctype}` (list) | `frappectl doc list "<DocType>" -f field=value --fields a,b,c --json` |
| every page of a list | add `--all` |
| `GET /api/v2/document/{doctype}/{name}` | `frappectl doc get "<DocType>" <name> --json` |
| `POST /api/v2/document/{doctype}` | `frappectl doc create "<DocType>" --set field=value`, or pipe JSON for child tables |
| `PUT /api/v2/document/{doctype}/{name}` | `frappectl doc update "<DocType>" <name> --set field=value` |
| `DELETE /api/v2/document/{doctype}/{name}` | `frappectl doc delete "<DocType>" <name>` |
| submit, cancel, amend | `frappectl doc submit|cancel|amend "<DocType>" <name>` |
| `GET` or `POST /api/v2/method/{dotted.path}` | `frappectl method call <dotted.path> -F key=value`, or `frappectl api method/<dotted.path> -X GET` |
| find a method | `frappectl method search --query="<word>"`, `frappectl method show <dotted.path>` |

Filters: repeat `-f field=value`; `>`, `<`, `>=`, `<=` and `like` also work. For `in`, `between` or
child-table filters pass `--filters-json '[["status","in",["Paid","Overdue"]]]'`.

`doc update` fails when someone else changed the document in the meantime. That is the tool
protecting the user: re-read the document and show both versions. Use `--force` only when the user
says to overwrite.

## Reports and read-only SQL

```bash
frappectl report run "Accounts Receivable" -f company="<Company>" --json
```

This is the supported way to read a report (Profit and Loss, Balance Sheet, General Ledger and the
rest) without opening the Desk. Report filters take `field=value` only; use `--filters-json` with a
JSON object for anything else.

`frappectl query '<select ...>'` runs read-only SQL and needs the System Manager role. Prefer a
report or `doc list`; use SQL only when neither can answer, show the query to the user first, and
never select columns that hold passwords, keys or tokens.

## Writing through frappectl: what the tool does not do for you

The tool's own documentation says it never asks for confirmation; the caller must. Here the caller
is this plugin:

1. `doc get` the current record and save the snapshot (see the snapshot spec).
2. State the reversibility class and the number of records, and wait for a clear yes.
3. Run the change, then `doc get` again and check the result.
4. Write the audit and activity log entries.

On sites that record it, changes made through `frappectl` show "via API" with the agent's name on
the document's timeline, so the user can see afterwards which changes an agent made.

## Errors

Exit code 0 is success, 1 is a failure reported by the site, 2 is a mistake in the command.

| You see | It means | Do this |
|---|---|---|
| a refusal mentioning read-only | the profile blocks writes | tell the user; only they make it writable |
| 401 or "not logged in" | the sign-in expired | ask the user to run `frappectl auth login` again |
| 403 / permission | the user lacks the role | name the DocType and permission; do not retry |
| 404 on a DocType | the app is not installed, or the name is wrong | `frappectl doctype list` and check |
| a concurrent-edit failure on update | someone changed the record | re-read, show both, ask |
