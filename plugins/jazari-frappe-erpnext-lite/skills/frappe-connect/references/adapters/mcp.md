# MCP adapter — Frappe's built-in MCP server

## Contents

- when this applies
- what the server gives you
- how the calls in `api.md` map to MCP tools
- lists and paging
- writing through MCP: what the server does not do for you
- what MCP cannot do
- errors

Frappe ships its own Model Context Protocol server. When the user has added it to Claude as a
connector, its tools are the preferred way to reach the site: sign-in is OAuth in the browser, no
API key is pasted anywhere, and every call runs with that user's own permissions.

Source: https://docs.frappe.io/framework/guides-integration/mcp (read 2026-11-14). Frappe marks the
MCP server **beta**; tool names and behaviour can change. If a tool listed here is missing or
behaves differently, say so and fall back to `frappectl.md`, or to the Desk (`browser.md`).

## When this applies

`state.json.active_adapter` is `mcp`. That is set by **frappe-connect** when this session has the
Frappe MCP tools (`search_doctypes`, `get_doctype_schema`, `list_documents` and the rest).

- The server arrived in Frappe **v16.53.0** (22 October 2026). An older site has no `/api/v2/mcp`.
- The endpoint is `https://<site>/api/v2/mcp`. A System Manager turns it on or off at
  **System Settings → AI Agents → Enable MCP**. New sites have it on by default.
- The user adds the connector themselves (Claude Desktop: Settings → Connectors → Add custom
  connector; Claude Code: `claude mcp add --transport http frappe https://<site>/api/v2/mcp`, then
  `claude mcp login frappe`). Never ask for their password; the browser handles sign-in.

## The 13 tools

| Tool | Use it to |
|---|---|
| `search_doctypes` | find a DocType by name before guessing one |
| `get_doctype_schema` | read a DocType's fields **and this user's permissions on it** |
| `search_methods`, `get_method_schema`, `list_document_methods` | find a whitelisted method and its arguments |
| `list_documents`, `get_document`, `count_documents` | read |
| `create_document`, `update_document`, `delete_document` | write |
| `call_method` | call a whitelisted method by dotted path |
| `call_document_method` | run a method on one document, such as `submit` or `cancel` |

## How the calls in `api.md` map

Every skill's `api.md` names a DocType and a REST call for each capability. Keep the DocType, swap
the call:

| `api.md` says | Through MCP |
|---|---|
| `GET /api/v2/doctype/{doctype}/meta` | `get_doctype_schema` |
| `GET /api/v2/document/{doctype}` (list) | `list_documents` |
| `GET /api/v2/document/{doctype}/{name}` | `get_document` |
| `GET /api/v2/doctype/{doctype}/count` | `count_documents` |
| `POST /api/v2/document/{doctype}` | `create_document` |
| `PUT /api/v2/document/{doctype}/{name}` | `update_document` |
| `DELETE /api/v2/document/{doctype}/{name}` | `delete_document` |
| `.../method/submit`, `.../method/cancel` | `call_document_method` with `submit` or `cancel`. For **Journal Entry** and **Stock Reconciliation** that is refused on v16: use `call_method` with `frappe.client.submit` (`{"doc": <document>}`) or `frappe.client.cancel` (`{"doctype", "name"}`) |
| a mapper such as `make_delivery_note` (see the module's `api.md`) | `call_method` with `{"source_name": "<earlier document>"}`, then `create_document` with the answer |
| `GET` or `POST /api/v2/method/{dotted.path}` | `call_method` |

The rule from `api.md` still holds and is easier here: **read the schema first, never guess a field
name.** `get_doctype_schema` also tells you whether this user may create, write, submit or delete,
so check it before promising an action.

## Lists and paging

`list_documents` returns 20 rows unless told otherwise, and says `has_next_page` when there are
more. Raise `start` for the next page. Ask only for the fields you need. For anything that needs
thousands of rows (a year of invoices, a full stock ledger), do not page them through the
conversation: use `count_documents`, or a report (**frappe-reports**) instead.

## Writing through MCP: what the server does not do for you

The server checks permissions. It does **not** ask "are you sure?", take a backup, or know which
actions cannot be undone. All of that is still this plugin's job:

1. Read the current record with `get_document` and save the snapshot (see the snapshot spec).
   Save the whole record as `get_document` returned it. This applies before every `update_document`,
   `delete_document`, `call_document_method` and `call_method` that changes data, and before a
   `create_document` that adds a row to an existing record or overwrites a settings record. If you cannot
   tell whether a method changes data, treat it as a change.
2. State the reversibility class and the number of records, and wait for a clear yes. Ask after the
   snapshot is saved, then end your turn: the change is made only in a later turn, after the user's reply.
   If the Claude app asks the user before a connector's tool runs, that prompt is a second check, never
   the yes itself.
3. Just before the change, read the record again. If its `modified` time is not the one in the snapshot,
   someone changed it while you waited: snapshot again and ask again. Then make the change,
   `get_document` again, and check it says what was intended.
4. Write the audit and activity log entries.

A submitted document cannot be edited through `update_document`; use `call_document_method` with
`cancel`, or amend, and say which before acting. "Delete All" in the Desk (v16.55 and later)
deletes a record together with every record linked to it — treat any request for it as
**irreversible** and never trigger its method on your own initiative.

## What MCP cannot do

- **Reports are not documents.** There is no report tool, but `call_method` with
  `frappe.desk.query_report.run` runs one (see **frappe-reports**, `api.md`; checked on 2026-11-15).
  `frappectl report run` and the Desk work too.
- **No bench.** Site backups, restores, migrations and app installs run on the server.
- **No files.** Uploading or downloading attachments needs `frappectl file` or the Desk.
- **Bulk reads.** See "Lists and paging".

When a capability needs one of these, say which connection can do it rather than improvising.

## Errors

| The server answers | It means | Do this |
|---|---|---|
| 401 | sign-in expired or was refused | ask the user to reconnect the connector |
| 403 | the user has no Desk access, or lacks the role for that DocType or method | name the DocType or method and the permission needed; do not retry |
| 404 on the endpoint | site older than v16.53, or **Enable MCP** is off | tell the user where the switch is, or use `frappectl.md` |
| a field is missing from a response | since v16.55 responses leave out fields the user may not view | say the field is hidden from this user, do not assume it is empty |
| a method "not found" | it is not whitelisted, or is a Server Script this user cannot read | do not guess another name |
