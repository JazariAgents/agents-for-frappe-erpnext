# API adapter — Bulk import and migration

## Contents

- authentication
- the six calls everything is made of
- payload shape and how to get the real fields
- listing, filtering, paging
- errors
- capability to DocType and call
- capabilities that need a schema lookup first

Base URL is the site itself: `https://your-site`. Every path below is appended to it.

## Authentication

Token: `Authorization: token <api_key>:<api_secret>` — generated at User → Settings → API Access → Generate Keys.

**Make every API-key call through the plugin's helper; never write your own code that reads
`.frappe/credentials.txt`.** In testing, a hand-written script put the whole credentials file into a header
and the error message printed the key. The helper reads the key itself and removes it from all output:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/frappe-connect/scripts/frappe_call.py" GET /api/v2/document/Customer --query '{"fields": ["name"], "limit": 20}'
python "${CLAUDE_PLUGIN_ROOT}/skills/frappe-connect/scripts/frappe_call.py" GET /api/v2/document/ToDo --query '{"filters": [["status", "=", "Open"]]}' --all
python "${CLAUDE_PLUGIN_ROOT}/skills/frappe-connect/scripts/frappe_call.py" snapshot --op <name> --request "<user's words>" --class <reversible|recreate|irreversible> --doc <DocType> <name>
python "${CLAUDE_PLUGIN_ROOT}/skills/frappe-connect/scripts/frappe_call.py" PUT /api/v2/document/ToDo/<name> --data '{"status": "Closed"}' --write
```

Run it from the workspace folder (the one holding `.frappe/`). If `CLAUDE_PLUGIN_ROOT` is not set, the
script is in the `frappe-connect/scripts/` folder beside this skill. Anything but GET is refused unless
`--write` is given: add it only after the snapshot is verified and the user has said yes. `--all` follows
every page of a list; `UPLOAD <file> --write` uploads a file; `whoami` tests the key.

The helper also enforces the snapshot rule, whatever the verb or the form of the address: a call that
changes or deletes an existing record is refused unless that exact record is in a snapshot from the last
hour. Creating a settings record (a Single) or a row inside an existing record counts as a change. A call
the helper does not recognise is refused too: if it changes a record, use the record's own address
(`PUT` or `DELETE /api/v2/document/<DocType>/<name>`, or `.../method/<method>`); if it only reads or creates
something new, tell the user the plugin cannot check that call, get a clear yes, and repeat it with
`--unlisted-method`.

The yes is held in code as well. Save the snapshot **before** you ask: a change is refused until the user
has replied after its snapshot was saved, and the request itself never counts as that reply. If the helper
says the user has not replied, say what will change and stop; repeat the same command after their answer,
without taking the snapshot again.
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

- **403** — the API user lacks the role, or the method is not whitelisted. Name the missing permission.
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
- **404 on /api/v2/** — the site is v14 or older; switch to the v1 paths.
- **"Please set the document name"** — this record type is named by the user (POS Profile, Email Template, Notification, Assignment Rule and others). Put the chosen name in the body as `"name": "..."` (tested on v16).
- A submitted document (docstatus 1) rejects edits. Amend or cancel instead, and say which before acting.

## Import a spreadsheet: the tested recipe

This is Frappe's own Data Import, driven through the API. Every step was run on a live Frappe 16.56 site.
It gives the dry run this skill promises: the preview checks every row and saves nothing.

1. **Upload the file.** `POST /api/v2/method/upload_file` as `multipart/form-data` with `file` (a `.csv` or
   `.xlsx`) and `is_private` = `1`. Keep the `file_url` from the answer.
2. **Make the import record.** `POST /api/v2/document/Data%20Import` with `reference_doctype` (for example
   `Customer`), `import_type` (`Insert New Records` or `Update Existing Records`) and `import_file` (the
   `file_url`). Its name contains spaces and colons: URL-encode it in every later call.
3. **Dry run.** `POST /api/v2/document/Data%20Import/<name>/method/get_preview_from_template`. The answer
   lists the columns it matched, the rows, and `warnings` (a wrong value, an unknown column). **Nothing is
   saved.** Show the user the row count and every warning.
4. **Fix every warning first.** If there is any warning, the import is accepted in step 5 but **never runs**:
   it stays `Pending` with no log. Correct the file, upload it again, and repeat from step 2.
5. **Snapshot, then sample, then the rest.** Snapshot the Data Import record (`--doc "Data Import" <name>`)
   and, for `Update Existing Records`, every record the file changes; the plugin's safety check refuses the
   start call otherwise. `frappe_call.py` reads the records an update import changes and names any
   without a snapshot. The dry run shows only the first 10 rows, so for a longer update import the helper
   reads every ID from the file itself: **use a `.csv` file for an update import of more than 10 rows**
   (it refuses an `.xlsx` or a Google Sheet, because it cannot read their rows). Through Frappe's MCP
   server an update import is refused, because the plugin cannot list those records there: start it with
   `frappe_call.py`, or ask the user to start it from the Data Import screen. Import a file with the first
   few rows, check them, then the full file:
   `POST /api/v2/method/frappe.core.doctype.data_import.data_import.form_start_import` with
   `{"data_import": "<name>"}`. It runs in the background, so the scheduler and workers must be running.
6. **Check the result.** Read the record's `status` (`Success`, `Partial Success`, `Error`) and the log:
   `GET /api/v2/document/Data%20Import%20Log` filtered on `data_import`. Each row says `success` and the
   record it made. Re-read a few of those records from the site before telling the user it worked.

More than 25 rows stops and shows the count first, as the guardrails say. An import adds records; it does
not undo itself. To remove an import, the records it made must be deleted one by one (recreate class).

## Capability → call

| Capability | DocType | Call | Docs |
|---|---|---|---|
| Import a chart of accounts | Chart of Accounts Importer | `PUT /api/v2/document/Chart%20of%20Accounts%20Importer/Chart%20of%20Accounts%20Importer` — Single DocType, update only | `docs/erpnext/erpnext__chart-of-accounts-importer.md` |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Import records from a spreadsheet | Data Import — follow "Import a spreadsheet: the tested recipe" above | `docs/erpnext/erpnext__data-import.md` |
| Export records to a spreadsheet | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__data-export.md` |
| Update many records at once | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__bulk-update.md` |
| Rename records in bulk | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__bulk-rename.md` |
| Import accounting masters | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__import-accounting-masters.md` |
| Import advances, payments and balances | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__import-advances-unallocated-payments-bank-stock-and-asset-balances.md` |
| Migrate from QuickBooks | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__quickbooks-migrator.md` |

## Not an API job

- Prepare and map legacy data — explanation, see guide.md
- Validate a migration — explanation, see guide.md
