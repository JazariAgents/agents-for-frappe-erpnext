# API adapter — HR and payroll

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
| Create employee records | Employee | `POST /api/v2/document/Employee` (and the list/read/update calls above) | `docs/frappe-hr/hr__employee.md` |
| Onboard a new employee | Employee Onboarding | `POST /api/v2/document/Employee%20Onboarding` (and the list/read/update calls above) | `docs/frappe-hr/hr__employee-onboarding.md` |
| Run employee separation | Employee Separation | `POST /api/v2/document/Employee%20Separation` (and the list/read/update calls above) | `docs/frappe-hr/hr__employee-separation.md` |
| Mark attendance | Attendance | `POST /api/v2/document/Attendance` (and the list/read/update calls above) | `docs/frappe-hr/hr__attendance.md` |
| Record employee check-ins | Employee Checkin | `POST /api/v2/document/Employee%20Checkin` (and the list/read/update calls above) | `docs/frappe-hr/hr__employee-checkin.md` |
| Plan shifts | Shift Type | `POST /api/v2/document/Shift%20Type` (and the list/read/update calls above) | `docs/frappe-hr/hr__shift-type.md` |
| Define leave types | Leave Type | `POST /api/v2/document/Leave%20Type` (and the list/read/update calls above) | `docs/frappe-hr/hr__leave-type.md` |
| Set a leave policy | Leave Policy | `POST /api/v2/document/Leave%20Policy` (and the list/read/update calls above) | `docs/frappe-hr/hr__leave-policy.md` |
| Allocate leave | Leave Allocation | `POST /api/v2/document/Leave%20Allocation` (and the list/read/update calls above) | `docs/frappe-hr/hr__leave-allocation.md` |
| Approve a leave application | Leave Application | `POST /api/v2/document/Leave%20Application` (and the list/read/update calls above) | `docs/frappe-hr/hr__leave-application.md` |
| Maintain the holiday list | Holiday List | `POST /api/v2/document/Holiday%20List` (and the list/read/update calls above) | `docs/frappe-hr/hr__holiday-list.md` |
| Build a salary structure | Salary Structure | `POST /api/v2/document/Salary%20Structure` (and the list/read/update calls above) | `docs/frappe-hr/hr__salary-structure.md` |
| Define salary components | Salary Component | `POST /api/v2/document/Salary%20Component` (and the list/read/update calls above) | `docs/frappe-hr/hr__salary-component.md` |
| Run payroll | Payroll Entry | `POST /api/v2/document/Payroll%20Entry` (and the list/read/update calls above) | `docs/frappe-hr/hr__payroll-entry.md` |
| Issue salary slips | Salary Slip | `POST /api/v2/document/Salary%20Slip` (and the list/read/update calls above) | `docs/frappe-hr/hr__salary-slip.md` |
| Process expense claims | Expense Claim | `POST /api/v2/document/Expense%20Claim` (and the list/read/update calls above) | `docs/frappe-hr/hr__expense-claim.md` |
| Give an employee advance | Employee Advance | `POST /api/v2/document/Employee%20Advance` (and the list/read/update calls above) | `docs/frappe-hr/hr__employee-advance.md` |
| Run an appraisal cycle | Appraisal Cycle | `POST /api/v2/document/Appraisal%20Cycle` (and the list/read/update calls above) | `docs/frappe-hr/hr__appraisal-cycle.md` |
| Post a job opening | Job Opening | `POST /api/v2/document/Job%20Opening` (and the list/read/update calls above) | `docs/frappe-hr/hr__job-opening.md` |
| Track job applicants | Job Applicant | `POST /api/v2/document/Job%20Applicant` (and the list/read/update calls above) | `docs/frappe-hr/hr__job-applicant.md` |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Automate attendance from check-ins | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/frappe-hr/hr__auto-attendance.md` |
| Collect tax exemption declarations | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/frappe-hr/hr__employee-tax-exemption-declaration.md` |
