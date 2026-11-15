# API adapter — Inventory and stock

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
| Work Order → Stock Entry (transfer or manufacture) | `erpnext.manufacturing.doctype.work_order.work_order.make_stock_entry` | `work_order_id`, `purpose`, `qty` |

Every row above was run on the live site and moved the earlier document's status on. Through the MCP
server use `call_method`; through `frappectl`, `frappectl api method/<mapper> -F source_name=<name> -X POST`.
A **credit note** made this way keeps its own balance by default (**Update Outstanding for Self** is ticked),
so the original invoice still shows the full amount owed: untick it before saving to reduce the invoice,
or reconcile the two afterwards with Payment Reconciliation. Say which to the user.

## Capability → call

| Capability | DocType | Call | Docs |
|---|---|---|---|
| Create and manage items | Item | `POST /api/v2/document/Item` (and the list/read/update calls above) | `docs/erpnext/erpnext-33.md` lines 3–307 |
| Group items | Item Group | `POST /api/v2/document/Item%20Group` (and the list/read/update calls above) | `docs/erpnext/erpnext-32.md` lines 175–245 |
| Define item attributes | Item Attribute | `POST /api/v2/document/Item%20Attribute` (and the list/read/update calls above) | `docs/erpnext/erpnext-31.md` lines 884–923 |
| Sell a product bundle | Product Bundle | `POST /api/v2/document/Product%20Bundle` (and the list/read/update calls above) | `docs/erpnext/erpnext-44.md` lines 669–746 |
| Set up warehouses | Warehouse | `POST /api/v2/document/Warehouse` (and the list/read/update calls above) | `docs/erpnext/erpnext-67.md` lines 667–745 |
| Make a stock entry | Stock Entry | `POST /api/v2/document/Stock%20Entry` (and the list/read/update calls above) | `docs/erpnext/erpnext-59.md` lines 487–671 |
| Reconcile physical stock | Stock Reconciliation | `POST /api/v2/document/Stock%20Reconciliation` (and the list/read/update calls above) | `docs/erpnext/erpnext-60.md` lines 3–128 |
| Track batches | Batch | `POST /api/v2/document/Batch` (and the list/read/update calls above) | `docs/erpnext/erpnext-09.md` lines 522–608 |
| Track serial numbers | Serial No | `POST /api/v2/document/Serial%20No` (and the list/read/update calls above) | `docs/erpnext/erpnext-56.md` lines 545–641 |
| Set putaway rules | Putaway Rule | `POST /api/v2/document/Putaway%20Rule` (and the list/read/update calls above) | `docs/erpnext/erpnext-48.md` lines 418–520 |
| Inspect incoming quality | Quality Inspection | `POST /api/v2/document/Quality%20Inspection` (and the list/read/update calls above) | `docs/erpnext/erpnext-48.md` lines 566–701 |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Create item variants | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-32.md` lines 575–636 |
| Manage units of measure | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-66.md` lines 918–935 |
| Load opening stock | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-39.md` lines 455–495 |
| Use the serial and batch bundle | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-56.md` lines 304–435 |
| Reserve stock for an order | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-60.md` lines 344–401 |
| Configure stock settings | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-60.md` lines 403–607 |
| Read the stock ledger | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-59.md` lines 692–734 |
| Check stock levels | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-59.md` lines 736–763 |
| Close a stock period | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/erpnext/erpnext-59.md` lines 409–431 |

## Not an API job

- Choose a valuation method — explanation, see guide.md
- Run perpetual inventory — explanation, see guide.md
