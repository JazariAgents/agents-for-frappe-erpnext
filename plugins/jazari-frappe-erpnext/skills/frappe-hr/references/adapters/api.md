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

## Run payroll: the tested recipe

Run on a live Frappe HR 16.53 site on 2026-11-14: four employees, four salary slips, one accrual journal
entry. Creating a Payroll Entry alone makes no slips; these are the steps the Desk's buttons perform.

**Before the first payroll run, check these three settings. Each one stopped the test run:**

1. **Holiday lists are assigned, not just set.** On Frappe HR 16 an employee's or company's holiday list
   comes from a submitted **Holiday List Assignment** (`applicable_for` Company or Employee, `assigned_to`,
   `holiday_list`, `from_date`). Setting `holiday_list` on the Employee or the Company is not enough.
   Page: `docs/frappe-hr/hr__hr__leave-management__holiday-list-assignment.md`.
2. **The payroll payable account must have account type Payable.** ERPNext's standard chart creates
   "Payroll Payable" without it.
3. **Every salary component needs an account for the company** (its `accounts` table).

Then:

1. `POST /api/v2/document/Payroll%20Entry` with `company`, `posting_date`, `payroll_frequency`, `start_date`,
   `end_date`, `currency`, `exchange_rate`, `payroll_payable_account` and `cost_center`.
2. Snapshot the Payroll Entry (the plugin's safety check refuses every later step on it otherwise), then
   `POST /api/v2/document/Payroll%20Entry/<name>/method/fill_employee_details`. It fills the employee list
   **in the answer only** (`docs[0].employees`); it does not save it. Save it:
   `PUT /api/v2/document/Payroll%20Entry/<name>` with that `employees` list.
3. Submit the entry (`.../method/submit`). This creates the draft salary slips.
4. `POST /api/v2/document/Payroll%20Entry/<name>/method/submit_salary_slips`. This submits the slips and
   posts the accrual journal entry. It is irreversible: cancel the slips and the journal entry to undo it.
5. **Re-read the entry after steps 3 and 4.** Both calls can answer OK while the work fails: the entry then
   shows `status` = `Failed` and the reason in `error_message`. Read it to the user word for word.

Employees are picked by company, currency, payroll frequency, dates **and** the payroll payable account
on their Salary Structure Assignment. If none are found, check those match.

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
| Run payroll | Payroll Entry | follow "Run payroll: the tested recipe" above | `docs/frappe-hr/hr__payroll-entry.md` |
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
