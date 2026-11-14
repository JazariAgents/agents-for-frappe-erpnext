# API adapter — Loans and lending

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

## A loan from product to repayment: the tested recipe

Run on a live Frappe Lending 16.8 site on 2026-11-14, start to finish.

**Set up once per company before the first loan product** (the first attempt failed without it):

1. A **Loan Demand Offset Order** (the order in which a collection pays off what is due), for example
   `{"title": "Standard", "components": [{"demand_type": "EMI (Principal + Interest)"}, {"demand_type": "Penalty"}, {"demand_type": "Charges"}]}`.
2. On the **Company**, Lending tab: set the four `collection_offset_sequence_for_...` fields to it.
   Page: `docs/lending/lending__loan-management__setup__company-level-setup.md`.
3. The accounts the product posts to: a loan account and interest and penalty receivable and accrued
   accounts (Asset), interest, penalty and suspense income accounts (Income), plus the disbursement and
   payment accounts. Ask the user which accounts to use; create any that are missing only after a yes.

Then:

1. `POST /api/v2/document/Loan%20Product` with the code, name, rate, company, `is_term_loan`,
   `repayment_schedule_type` and the accounts above.
2. `POST /api/v2/document/Loan%20Application`, set `status` to `Approved` once the user approves it, then submit.
3. Make the loan **from the application**: `POST /api/v2/method/lending.loan_management.doctype.loan_application.loan_application.create_loan`
   with `{"source_name": "<application>"}`, save the answer as a Loan, and submit it.
4. Disburse **from the loan**: `POST /api/v2/method/lending.loan_management.doctype.loan.loan.make_loan_disbursement`
   with `{"loan": "<loan>", "as_dict": 1}`, save the answer as a Loan Disbursement, and submit it. The loan's
   status becomes `Disbursed`.
5. Repayment **from the loan**: `POST /api/v2/method/lending.loan_management.doctype.loan.loan.make_repayment_entry`
   with `loan`, `applicant_type`, `applicant`, `loan_product`, `company`, `loan_disbursement` and `"as_dict": 1`;
   set `amount_paid`, save it as a Loan Repayment, and submit it.

Submitting a loan, a disbursement or a repayment posts to the ledger: irreversible, as everywhere else.

## Capability → call

| Capability | DocType | Call | Docs |
|---|---|---|---|
| Set up a loan product | Loan Product | `POST /api/v2/document/Loan%20Product` (and the list/read/update calls above) | `docs/lending/lending__loan-product.md` |
| Process a loan application | Loan Application | `POST /api/v2/document/Loan%20Application` (and the list/read/update calls above) | `docs/lending/lending__loan-application.md` |
| Disburse a loan | Loan Disbursement | `POST /api/v2/document/Loan%20Disbursement` (and the list/read/update calls above) | `docs/lending/lending__loan-disbursement.md` |
| Record a loan repayment | Loan Repayment | `POST /api/v2/document/Loan%20Repayment` (and the list/read/update calls above) | `docs/lending/lending__loan-repayment.md` |
| Manage loan security | Loan Security | `POST /api/v2/document/Loan%20Security` (and the list/read/update calls above) | `docs/lending/lending__loan-security.md` |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Accrue interest | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/lending/lending__loan-interest-accrual.md` |
