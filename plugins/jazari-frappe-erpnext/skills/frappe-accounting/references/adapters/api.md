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
The secret is shown once. Read it from `.frappe/credentials.txt` into a variable; never print it and never
interpolate it into a command you display.
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
definitions, not record types — you cannot POST to them. Run them in the interface (see `browser.md`),
or read the underlying documents (GL Entry, Sales Invoice) with the list call and aggregate yourself.

Two ERPNext specifics worth knowing before writing: a **return** (credit note, debit note, sales/purchase
return) is not its own DocType — it is the same DocType with the return flag set and negative quantities, so
read `/meta` and copy the original document rather than inventing a `... (return)` type. And a document only
affects the ledger once it is **submitted**; a create alone leaves a draft.

## Listing, filtering, paging

- `fields=["name","status"]` — without it only `name` comes back.
- `filters=[["DocType","field","=","value"]]` — SQL-style conditions.
- `limit_page_length` (default 20) and `limit_start` for successive pages. Always page.
Source: https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents

## Errors

- **403** — the API user lacks the role, or the method is not whitelisted. Name the missing permission.
- **validation** — Frappe returns the message in `_server_messages`. Repeat it to the user verbatim.
- **429** — rate limited; `X-RateLimit-Remaining` and `X-RateLimit-Reset` say when to resume.
  Source: https://docs.frappe.io/framework/user/en/rate-limiting
- **404 on /api/v2/** — the site is v14 or older; switch to the v1 paths.
- A submitted document (docstatus 1) rejects edits. Amend or cancel instead, and say which before acting.

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
