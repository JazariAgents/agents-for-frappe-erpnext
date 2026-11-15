# API adapter — running the standard reports

## Contents

- what this adapter covers
- the one call
- filters that were tested
- group by dimension
- reading the answer
- errors
- what stays in the interface

A report is not a record type, so the six document calls do not apply to it. A report is **run**.
Every call in this file was run against a live ERPNext 16.55 site on 2026-11-14 with an API key.

## What this adapter covers

Running the reports that already exist on the site: General Ledger, Balance Sheet, Profit and Loss
Statement, Cash Flow, Accounts Receivable, Accounts Payable, Trial Balance, Sales Analytics and the
other standard reports. Running a report only reads. It changes nothing on the site.

Building a custom report, scheduling an emailed report, ERPNext dashboards and everything in
Insights are done in the interface: see `browser.md`.

## The one call

`GET /api/method/frappe.desk.query_report.run?report_name=<report name>&filters=<json>`

- `report_name` is the report's name exactly as the Desk shows it, for example `Profit and Loss
  Statement`. A wrong name answers 404 with *Report … not found*.
- `filters` is a JSON object using the same names as the filter bar on the report's screen.
- Through Frappe's MCP server use `call_method` with method `frappe.desk.query_report.run` and the
  same two arguments. Through `frappectl` use `frappectl report run`. See the `frappe-connect`
  adapter files.

For a quick figure the **frappe-dashboards** skill is usually the better tool: it reads the
documents themselves and shows where each number came from.

## Filters that were tested

Dates and the fiscal year below are examples. Read the company name and the fiscal years from the
site first; never assume them.

| Report | Filters that ran |
|---|---|
| General Ledger | `company`, `from_date`, `to_date`, `group_by` (`Group by Voucher (Consolidated)`) |
| Balance Sheet, Profit and Loss Statement, Cash Flow | `company`, `filter_based_on` (`Fiscal Year` or `Date Range`), `from_fiscal_year`, `to_fiscal_year`, `period_start_date`, `period_end_date`, `periodicity` (`Yearly`, `Half-Yearly`, `Quarterly`, `Monthly`) |
| Accounts Receivable, Accounts Payable | `company`, `report_date`, `ageing_based_on` (`Due Date`), `range` (`30, 60, 90, 120`) |
| Trial Balance | `company`, `fiscal_year`, `from_date`, `to_date` |
| Sales Analytics | `company`, `tree_type` (`Customer`), `doc_type` (`Sales Invoice`), `value_quantity` (`Value`), `from_date`, `to_date`, `range` (`Monthly`) |

A report not in this table takes the filters its screen shows. Open the report in the Desk with the
user, or read its bundled page, before guessing a filter name. A missing mandatory filter answers
with a validation message that names it; repeat that message to the user.

## Group by dimension

From ERPNext **16.51**, Balance Sheet and Profit and Loss Statement accept `group_by_dimension`:
`Cost Center`, `Project`, or the document type of any Accounting Dimension the site has set up.
The answer then carries one column per value of that dimension and a total column. On the test
site, `"group_by_dimension": "Cost Center"` returned the columns Account, Account Name, Account
Number, Currency, then one column for the cost center, then Total.

On an older site the filter is ignored or refused. Run the report once per cost center instead,
and tell the user why the single view is not available.

## Reading the answer

- `message.columns` — one entry per column: label, fieldname and type. **Read this first.** The
  columns change with the filters (one per period, or one per dimension value).
- `message.result` — the rows. Financial statements include heading and total rows, and indent
  child accounts; do not add a column up yourself when the report already gives the total row.
- Amounts are in the company's currency unless a presentation currency was asked for.
- Say which report, which company, which period and which filters produced a figure whenever you
  quote one.

## Errors

- **403** — the user may not open that report. Name the report; do not retry and do not switch user.
  From ERPNext 16.36 and 16.50 more reports and lookups check permission on the records they read.
- **404** — no report of that name on this site. The app that provides it may not be installed.
- **417** — a filter is missing or wrong; the message names it (`errors[].message` on `/api/v2/`,
  `_server_messages` on `/api/method/`).
- **401 with "Access not allowed from this IP Address"** — the key is fine; the user has a Restrict
  IP list, which applies to API keys from Frappe 16.33.
- **429** — rate limited. Wait for the time in `Retry-After`. Large reports are slow; do not run
  the same one in a loop.
- The **IRS 1099** report (United States) lost its *Print IRS 1099 Forms* button in ERPNext 16.35.
  The report still runs; do not promise printed forms from it.

## What stays in the interface

| Capability | Why |
|---|---|
| Build a custom report | made in the Report Builder or as a Query/Script report |
| Email a report on a schedule | an Auto Email Report record with the user's own choices |
| Build ERPNext dashboards | arranged on screen |
| Everything in Insights | a separate app with its own interface |
