# API adapter — Courses and students

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
| Enrol students | Student | `POST /api/v2/document/Student` (and the list/read/update calls above) | `docs/education/education__student.md` |
| Set up programs and courses | Program | `POST /api/v2/document/Program` (and the list/read/update calls above) | `docs/education/education__program.md` |
| Collect fees | Fees | `POST /api/v2/document/Fees` (and the list/read/update calls above) | `docs/education/education__fees.md` |

## Capabilities that need a schema lookup first

These are real actions on the site, but the documentation page describes a process rather than one
record type — often several DocTypes at once, or a setting inside a Settings document. They ARE reachable
over the API: identify the DocType from the page below, confirm it with `/meta`, then use the six calls.
Do not guess the name.

| Capability | Where to look | Bundled page (read this) |
|---|---|---|
| Create a course | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__create-a-course.md` |
| Add chapters and lessons | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__add-a-chapter.md` |
| Run a batch of learners | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__create-a-batch.md` |
| Host a live class | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__create-a-live-class.md` |
| Assess learners with quizzes | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__quizzes.md` |
| Set assignments | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__assignments.md` |
| Issue certificates | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__issue-a-certificate.md` |
| Group courses into a program | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__add-a-program.md` |
| Charge for a course | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/learning/learning__setting-up-payment-gateway.md` |
| Run assessments | read the bundled page, then `GET /api/v2/doctype/<name>/meta` to confirm | `docs/education/education__assessment-introduction.md` |
