# API adapter — Accounting, invoicing and tax

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
make it with the return mapper in "Create the next document from the previous one" below rather than copying the original by hand or inventing a `... (return)` type. And a document only
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

## Create the next document from the previous one

In ERPNext a sales or purchase is a chain: quotation, order, delivery, invoice, payment. Each document
must be **made from the one before it**, the way the Desk's **Create** button does it. A document
posted fresh with the same items is **not linked**: on a live site a delivery note posted on its own
left its sales order at 0% delivered and its quotation still "Open" (tested on ERPNext 16.55).

1. Call the mapper with the earlier document's name: `POST /api/v2/method/<mapper>` with the arguments below.
   The answer (`data`) is the new document, filled in and linked, **not yet saved**.
2. Change only what the user asked for (dates, quantities, warehouse), then save it with
   `POST /api/v2/document/<DocType>` and submit it as usual.
3. Re-read the earlier document and check its status moved on (for example `per_delivered`, `per_billed`).

| From → to | Mapper | Arguments |
|---|---|---|
| Quotation → Sales Order | `erpnext.selling.doctype.quotation.quotation.make_sales_order` | `source_name` |
| Sales Order → Delivery Note | `erpnext.selling.doctype.sales_order.sales_order.make_delivery_note` | `source_name` |
| Sales Order → Sales Invoice | `erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice` | `source_name` |
| Delivery Note → Sales Invoice | `erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice` | `source_name` |
| Sales Invoice → credit note | `erpnext.accounts.doctype.sales_invoice.sales_invoice.make_sales_return` | `source_name` |
| Delivery Note → sales return | `erpnext.stock.doctype.delivery_note.delivery_note.make_sales_return` | `source_name` |
| Material Request → Purchase Order | `erpnext.stock.doctype.material_request.material_request.make_purchase_order` | `source_name` |
| Purchase Order → Purchase Receipt | `erpnext.buying.doctype.purchase_order.purchase_order.make_purchase_receipt` | `source_name` |
| Purchase Order → Purchase Invoice | `erpnext.buying.doctype.purchase_order.purchase_order.make_purchase_invoice` | `source_name` |
| Purchase Receipt → Purchase Invoice | `erpnext.stock.doctype.purchase_receipt.purchase_receipt.make_purchase_invoice` | `source_name` |
| Purchase Invoice → debit note | `erpnext.accounts.doctype.purchase_invoice.purchase_invoice.make_debit_note` | `source_name` |
| Purchase Receipt → purchase return | `erpnext.stock.doctype.purchase_receipt.purchase_receipt.make_purchase_return` | `source_name` |
| Sales or Purchase Invoice → Payment Entry | `erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry` | `dt`, `dn` |

Every row above was run on the live site and moved the earlier document's status on. Through the MCP
server use `call_method`; through `frappectl`, `frappectl api method/<mapper> -F source_name=<name> -X POST`.
A **credit note** made this way keeps its own balance by default (**Update Outstanding for Self** is ticked),
so the original invoice still shows the full amount owed: untick it before saving to reduce the invoice,
or reconcile the two afterwards with Payment Reconciliation. Say which to the user.

## Capability → call

| Capability | DocType | Call | Docs |
|---|---|---|---|
| Raise a sales invoice | Sales Invoice | `POST /api/v2/document/Sales%20Invoice` (and the list/read/update calls above) | `docs/erpnext/erpnext__sales-invoice.md` |
| Record a purchase invoice | Purchase Invoice | `POST /api/v2/document/Purchase%20Invoice` (and the list/read/update calls above) | `docs/erpnext/erpnext__purchase-invoice.md` |
| Issue a credit note | Sales Invoice | `POST /api/v2/document/Sales%20Invoice` (and the list/read/update calls above) | `docs/erpnext/erpnext__credit-note.md` |
| Issue a debit note | Purchase Invoice | `POST /api/v2/document/Purchase%20Invoice` (and the list/read/update calls above) | `docs/erpnext/erpnext__debit-note.md` |
| Record a payment entry | Payment Entry | `POST /api/v2/document/Payment%20Entry` (and the list/read/update calls above) | `docs/erpnext/erpnext__payment-entry.md` |
| Post a journal entry | Journal Entry | `POST /api/v2/document/Journal%20Entry` (and the list/read/update calls above) | `docs/erpnext/erpnext__journal-entry.md` |
| Set up cost centers | Cost Center | `POST /api/v2/document/Cost%20Center` (and the list/read/update calls above) | `docs/erpnext/erpnext__cost-center.md` |
| Chase overdue invoices with dunning | Dunning | `POST /api/v2/document/Dunning` (and the list/read/update calls above) | `docs/erpnext/erpnext__dunning.md` |
| Bill customers on a subscription | Subscription | `POST /api/v2/document/Subscription` (and the list/read/update calls above) | `docs/erpnext/erpnext__subscription.md` |
| Manage fixed assets | Asset | `POST /api/v2/document/Asset` (and the list/read/update calls above) | `docs/erpnext/erpnext__asset.md` |
| Create a sales tax template | Sales Taxes and Charges Template | `POST /api/v2/document/Sales%20Taxes%20and%20Charges%20Template` (and the list/read/update calls above) | `docs/erpnext/erpnext__sales-taxes-and-charges-template.md` |
| Set item-level tax | Item Tax Template | `POST /api/v2/document/Item%20Tax%20Template` (and the list/read/update calls above) | `docs/erpnext/erpnext__item-tax-template.md` |
| Use tax categories | Tax Category | `POST /api/v2/document/Tax%20Category` (and the list/read/update calls above) | `docs/erpnext/erpnext__tax-category.md` |
| Apply tax rules automatically | Tax Rule | `POST /api/v2/document/Tax%20Rule` (and the list/read/update calls above) | `docs/erpnext/erpnext__tax-rule.md` |
| Set up withholding tax | Tax Withholding Category | `POST /api/v2/document/Tax%20Withholding%20Category` (and the list/read/update calls above) | `docs/erpnext/erpnext__tax-withholding-category.md` |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Send a payment request | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__payment-request.md` |
| Set payment terms | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__payment-terms.md` |
| Reconcile the bank | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__bank-reconciliation.md` |
| Reconcile payments against invoices | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__payment-reconciliation.md` |
| Enter opening balances | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__opening-balance.md` |
| Import opening invoices | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__opening-invoice-creation-tool.md` |
| Set and track a budget | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__budget.md` |
| Use accounting dimensions | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__accounting-dimensions.md` |
| Close an accounting period | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__period-closing-voucher.md` |
| Freeze accounting entries | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__freeze-accounting-entries.md` |
| Set up deferred revenue and expense | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__deferred-accounting.md` |
| Send a statement of accounts | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__process-statement-of-accounts.md` |
| Run asset depreciation | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__asset-depreciation.md` |
| Track shareholders and share transfers | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__share-transfer.md` |
| Set up taxes | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__setting-up-taxes.md` |
| Create a purchase tax template | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__purchase-taxes-and-charges-template.md` |
| Set up UAE VAT | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__uae-vat-setup.md` |
| Set up KSA VAT reporting | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext__simplified_ksa_vat_management_and_reporting.md` |

## Not an API job

- Handle multi-currency accounting — explanation, see guide.md
