# API adapter — REST API, webhooks and automation

## Contents

- how these calls are made
- the six calls everything is made of
- payload shape and how to get the real fields
- listing, filtering, paging
- errors
- capability to DocType and call
- capabilities that need a schema lookup first

Base URL is the site itself: `https://your-site`. Every path below is appended to it.

## How these calls are made in this edition

This edition makes no REST calls of its own and never handles an API key. Every call below is made
through Frappe's MCP connector or `frappectl`: `frappe-connect/references/adapters/mcp.md` and
`frappectl.md` map each one to a tool or a command. Keep the DocType, the fields and the arguments from
this file, and swap the call. Never write your own code that calls the site.

Save the snapshot **before** you ask for the yes, then end your turn: make the change only after the
user has replied, and never count the request itself as that reply.
Source: https://docs.frappe.io/framework/user/en/api/rest

## The six calls everything is made of

Frappe generates the same REST surface for every DocType on the site, so these six calls reach ERPNext, HR,
CRM, Helpdesk and any custom app. URL-encode the space in a DocType name: `Sales%20Invoice`.

| What | Endpoint (API v2 — v15 and v16) | v1 fallback (v14 and older) |
|---|---|---|
| list | `GET /api/v2/document/{doctype}` | `GET /api/resource/{doctype}` |
| read one | `GET /api/v2/document/{doctype}/{name}` | `GET /api/resource/{doctype}/{name}` |
| create | `POST /api/v2/document/{doctype}` | `POST /api/resource/{doctype}` |
| update | `PUT /api/v2/document/{doctype}/{name}` | `PUT /api/resource/{doctype}/{name}` |
| delete | `DELETE /api/v2/document/{doctype}/{name}` | `DELETE /api/resource/{doctype}/{name}` |
| submit / cancel | `POST /api/v2/document/{doctype}/{name}/method/submit` · `.../method/cancel` | `run_doc_method` on v1 |

Plus: `GET /api/v2/doctype/{doctype}/meta` (schema), `GET /api/v2/doctype/{doctype}/count`,
`POST /api/v2/method/upload_file`, `GET /api/v2/method/ping`, `GET /api/method/frappe.auth.get_logged_user`.
Source: https://docs.frappe.io/framework/user/en/guides/integration/rest_api

**When submit or cancel answers "not whitelisted" (403).** On v16, **Journal Entry** and **Stock
Reconciliation** replace the standard submit and cancel, so the two calls above are refused for them
(tested on ERPNext 16.55). Use Frappe's general calls instead:

- submit: read the document, then `POST /api/v2/method/frappe.client.submit` with `{"doc": <the whole document as read>}`
- cancel: `POST /api/v2/method/frappe.client.cancel` with `{"doctype": "<DocType>", "name": "<name>"}`

Through the MCP server this is `call_method` with the same method and arguments; through `frappectl`,
`frappectl api method/frappe.client.submit --input -` with the same JSON on standard input. The safety
rules are unchanged: it is still a submit or cancel, with the same reversibility.

## Payload shape, and how to get the real field names

A create is a flat JSON object of fieldname → value; child tables are arrays of objects on the parent:

```json
{ "lead_name": "Mustermann" }
```
(the documented Lead example — https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents)

**Never guess field names, and never guess a DocType name.** Read the schema first — the single most useful
call in the whole API:

```
GET /api/v2/doctype/Sales%20Invoice/meta
```

It returns the fields, their types, which are mandatory, and the child tables. Build the payload from that,
then create. On v14 or older (no API v2), fetch an existing record of that type instead and mirror its shape.

**Single DocTypes** (Manufacturing Settings, Stock Settings, Selling Settings, Accounts Settings, System
Settings, Website Settings and other `... Settings` documents) hold exactly one record. They are updated,
never created: use `PUT /api/v2/document/{doctype}/{doctype}` — the record's name equals the DocType name.
`/meta` tells you: a Single has `issingle: 1`.

**Reports are not DocTypes.** Balance Sheet, Profit and Loss, General Ledger and the rest are Report
definitions, not record types — you cannot POST to them. Run one with
`GET /api/method/frappe.desk.query_report.run?report_name=<name>&filters=<json>` (the answer has
`message.columns` and `message.result`), or in the interface (see `browser.md`), or read the underlying
documents (GL Entry, Sales Invoice) with the list call and aggregate yourself.

Two ERPNext specifics worth knowing before writing: a **return** (credit note, debit note, sales/purchase
return) is not its own DocType — it is the same DocType with the return flag set and negative quantities, so
make it with ERPNext's return mapper (listed under "Create the next document from the previous one" in the `frappe-selling` and `frappe-buying` skills' `api.md`) rather than copying the original by hand or inventing a `... (return)` type. And a document only
affects the ledger once it is **submitted**; a create alone leaves a draft.

## Listing, filtering, paging

- `fields=["name","status"]` — without it only `name` comes back.
- `filters=[["DocType","field","=","value"]]` — SQL-style conditions.
- Paging differs by API version, and the wrong words are **ignored without an error**. On `/api/v2/` use
  `limit` (default 20) and `start`, and read `has_next_page` in the answer. On `/api/resource/` use
  `limit_page_length` and `limit_start`. Always page, and stop when a page comes back short.
Source: https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents

## Errors

- **403** — the signed-in user lacks the role, or the method is not whitelisted. Name the missing permission.
  From ERPNext 16.36 and 16.50 more actions also check permission on the records they touch (the
  account, warehouse, asset, work order or project), so a user who could do this on an older site may
  now be refused. Say which record type the error names; do not retry and do not switch to another user.
- **401 with "Access not allowed from this IP Address"** — the key is fine. The user has a Restrict IP
  list, and from Frappe 16.33 that list applies to API keys and OAuth too. Someone with access adds this
  computer's address on the User record, or the user issues a key from an account without the list.
- **validation (HTTP 417)** — on `/api/v2/` the reason is in `errors[].message`; on `/api/resource/` it is
  in `_server_messages`. Repeat it to the user verbatim.
- **429** — rate limited; `X-RateLimit-Remaining`, `X-RateLimit-Reset` and `Retry-After` say when to
  resume. It is either the site's overall budget or one method's own limit. From Frappe 16.53 a method's
  limit follows the method, not the address, so calling it through `/api/method/` instead of
  `/api/v2/method/` does not get round it. Wait; never retry in a loop.
  Source: https://docs.frappe.io/framework/user/en/rate-limiting
- **404 on /api/v2/** — the site is older than this edition can reach; work through the Desk (`browser.md`).
- **"Please set the document name"** — this record type is named by the user (POS Profile, Email Template, Notification, Assignment Rule and others). Put the chosen name in the body as `"name": "..."` (tested on v16).
- A submitted document (docstatus 1) rejects edits. Amend or cancel instead, and say which before acting.

## Capability → call

| Capability | DocType | Call | Docs |
|---|---|---|---|
| Test the site connection | — | `GET /api/v2/method/ping` | `docs/framework/framework-06.md` lines 660–1163 |
| Authenticate with API key and secret | — | `GET /api/method/frappe.auth.get_logged_user` | `docs/framework/framework-06.md` lines 660–1163 |
| Log in with username and password | — | `POST /api/method/login` — reference only: the user runs it, never ask for, type or send a password | `docs/framework/framework-06.md` lines 660–1163 |
| List documents of any DocType | — | `GET /api/v2/document/{doctype}` | `docs/framework/framework-17.md` lines 494–559 |
| Filter and select fields in a list call | — | `GET /api/resource/{doctype}` | `docs/framework/framework-17.md` lines 494–559 |
| Create a document through the API | — | `POST /api/v2/document/{doctype}` | `docs/framework/framework-17.md` lines 561–734 |
| Read one document through the API | — | `GET /api/v2/document/{doctype}/{name}` | `docs/framework/framework-17.md` lines 561–734 |
| Update a document through the API | — | `PUT /api/v2/document/{doctype}/{name}` | `docs/framework/framework-17.md` lines 561–734 |
| Delete a document through the API | — | `DELETE /api/v2/document/{doctype}/{name}` | `docs/framework/framework-17.md` lines 561–734 |
| Submit a document through the API | — | `POST /api/v2/document/{doctype}/{name}/method/submit` | `docs/framework/framework-17.md` lines 373–492 |
| Cancel a submitted document | — | `POST /api/v2/document/{doctype}/{name}/method/cancel` | `docs/framework/framework-17.md` lines 373–492 |
| Read DocType metadata to discover a site's schema | — | `GET /api/v2/doctype/{doctype}/meta` | `docs/framework/framework-17.md` lines 373–492 |
| Count records of a DocType | — | `GET /api/v2/doctype/{doctype}/count` | `docs/framework/framework-17.md` lines 373–492 |
| Call a whitelisted method on a document | — | `POST /api/v2/method/run_doc_method` | `docs/framework/framework-17.md` lines 373–492 |
| Upload a file through the API | — | `POST /api/v2/method/upload_file` | `docs/framework/framework-17.md` lines 373–492 |
| Build an Automation Flow, switched off | Automation Flow | `POST /api/v2/document/Automation%20Flow` — read `../automation-flows.md` first | `docs/framework/framework-01.md` lines 125–221 |
| Test-run an Automation Flow on a real record | Automation Flow | `POST /api/v2/method/frappe.automation_engine.api.trial_run` | `docs/framework/framework-01.md` lines 395–545 |
| Turn an Automation Flow on or off | Automation Flow | `PUT /api/v2/document/Automation%20Flow/{name}` with `enabled` 1 or 0 — only after a clear yes | `docs/framework/framework-01.md` lines 547–667 |
| Read an Automation Flow's run history | Automation Run | `GET /api/v2/method/frappe.automation_engine.api.get_runs` | `docs/framework/framework-01.md` lines 125–221 |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Authenticate with OAuth 2 | **the user only**: they set up an OAuth Client in the Desk (`browser.md`); never create one yourself, because the answer holds its client secret | `docs/framework/framework-03.md` lines 288–361 |
| Generate API key and secret for a user | **the user only**, in the Desk (`browser.md`): never call `generate_keys` or any method that returns a secret | `docs/framework/framework-17.md` lines 246–291 |
| Respect the site's rate limits | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/framework/framework-22.md` lines 333–393 |
| Create a webhook on document events | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/framework/framework-18.md` lines 3–148 |
| Secure a webhook with a shared secret | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/framework/framework-18.md` lines 3–148 |
| Publish and listen to realtime events | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/framework/framework-06.md` lines 384–658 |
| Queue and monitor background jobs | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/framework/framework-03.md` lines 1299–1508 |

## Not an API job

- Diagnose the scheduler — server command, see bench.md
