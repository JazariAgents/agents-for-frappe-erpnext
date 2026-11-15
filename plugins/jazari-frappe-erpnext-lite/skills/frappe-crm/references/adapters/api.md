# API adapter — CRM and the sales pipeline

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
| Capture leads | CRM Lead | `POST /api/v2/document/CRM%20Lead` (and the list/read/update calls above) | `docs/crm/crm-01.md` lines 1885–1963 |
| Move deals through the pipeline | CRM Deal | `POST /api/v2/document/CRM%20Deal` (and the list/read/update calls above) | `docs/crm/crm-01.md` lines 1069–1144 |
| Track CRM tasks | CRM Task | `POST /api/v2/document/CRM%20Task` (and the list/read/update calls above) | `docs/crm/crm-01.md` lines 2466–2506 |
| Track organizations | CRM Organization | `POST /api/v2/document/CRM%20Organization` (and the list/read/update calls above) | `docs/crm/crm-01.md` lines 2110–2139 |
| Work an opportunity in ERPNext | Opportunity | `POST /api/v2/document/Opportunity` (and the list/read/update calls above) | `docs/erpnext/erpnext-10.md` lines 2809–2898 |
| Run a campaign | Campaign | `POST /api/v2/document/Campaign` (and the list/read/update calls above) | `docs/erpnext/erpnext-04.md` lines 3–79 |
| Send an email campaign | Email Campaign | `POST /api/v2/document/Email%20Campaign` (and the list/read/update calls above) | `docs/erpnext/erpnext-06.md` lines 2952–3045 |
| Send a newsletter | Newsletter | `POST /api/v2/document/Newsletter` (and the list/read/update calls above) | `docs/erpnext/erpnext-10.md` lines 1890–1947 |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Keep notes on a deal | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 2035–2072 |
| Reply with email templates | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 1216–1249 |
| Log calls against a deal | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 42–90 |
| Set a CRM service level agreement | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 2273–2318 |
| Customize deal statuses | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 878–1049 |
| Capture leads from a web form | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 92–176 |
| Invite your sales team | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 1786–1816 |
| Message a contact on WhatsApp | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/crm/crm-01.md` lines 2643–2709 |
