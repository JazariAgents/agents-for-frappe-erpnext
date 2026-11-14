# Interface adapter — Reports, dashboards and Insights

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |
| `https://your-site/insights` | the Frappe Insights interface |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Read the general ledger
- **Path:** open https://your-site/app (the Desk) and find *General Ledger* — the documentation page below shows the screen
- **Documented steps:**
  1. Open Accounting and select General Ledger
  2. Select Nova Industries and the required date range
  3. Leave Account and Party blank to review all postings, or narrow the report to the balance you are investigating
  4. Use Voucher No when you already know the source transaction. Select a categorization option when you want entries arranged by Account, Voucher, or Party
  5. Refresh the report and confirm that the result has fully loaded before interpreting it
- **Full page, bundled offline:** `docs/erpnext/erpnext__general-ledger.md`  (https://docs.frappe.io/erpnext/general-ledger)

### Produce a balance sheet
- **Path:** open https://your-site/app (the Desk) and find *Balance Sheet* — the documentation page below shows the screen
- **Documented steps:**
  1. Open Accounting and select Balance Sheet
  2. Select Nova Industries
  3. Choose Fiscal Year or Date Range and the comparison periodicity
  4. Apply Finance Book, Cost Center, Project, Department, or another Accounting Dimension only when required
  5. To get one column per cost center, project or other accounting dimension, choose it in **Group by Dimension** (ERPNext 16.51 and later; absent on older sites)
  6. Refresh and wait for totals, chart, and account rows to load
- **Full page, bundled offline:** `docs/erpnext/erpnext__balance-sheet.md`  (https://docs.frappe.io/erpnext/balance-sheet)

### Produce a profit and loss report
- **Path:** open https://your-site/app (the Desk) and find *Profit and Loss Report* — the documentation page below shows the screen
- **Documented steps:**
  1. Open Accounting and select Profit and Loss Statement
  2. Select Nova Industries
  3. Choose Fiscal Year or Date Range and set the required period
  4. Select Yearly, Half-Yearly, Quarterly, or Monthly periodicity
  5. Apply Finance Book, Cost Center, Department, Project, or another Accounting Dimension only when the question requires that slice
  6. To get one column per cost center, project or other accounting dimension, choose it in **Group by Dimension** (ERPNext 16.51 and later; absent on older sites)
  7. Refresh and wait for the totals, chart, and account rows to load
- **Full page, bundled offline:** `docs/erpnext/erpnext__profit-and-loss-report.md`  (https://docs.frappe.io/erpnext/profit-and-loss-report)

### Produce a cash flow report
- **Path:** open https://your-site/app (the Desk) and find *Cash Flow Report* — the documentation page below shows the screen
- **Documented steps:**
  1. Open Accounting and select Cash Flow
  2. Select Nova Industries and the required fiscal year or date range
  3. Choose periodicity and optional Finance Book, Cost Center, Project, Department, or Accounting Dimension
  4. Enable opening and closing balances when the cash reconciliation requires them
  5. Refresh and wait for totals, chart, and report sections to load
- **Full page, bundled offline:** `docs/erpnext/erpnext__cash-flow-report.md`  (https://docs.frappe.io/erpnext/cash-flow-report)

### Age receivables and payables
- **Path:** open https://your-site/app (the Desk) and find *Accounts Receivable and Payable* — the documentation page below shows the screen
- **Documented steps:**
  1. Open Accounts Receivable or Accounts Payable
  2. Select the Company and reporting date
  3. Choose ageing based on Due Date or Posting Date according to the review
  4. Optionally filter by Party, Account, Territory, Supplier Group, Cost Center, Project, Finance Book, currency, or another available dimension
  5. Refresh the report and open significant invoice references
- **Full page, bundled offline:** `docs/erpnext/erpnext__accounts-receivable-and-payable.md`  (https://docs.frappe.io/erpnext/accounts-receivable-and-payable)

### Use the standard accounting reports
- **Path:** open https://your-site/app (the Desk) and find *Accounting Reports* — the documentation page below shows the screen
- **Full page, bundled offline:** `docs/erpnext/erpnext__accounting-reports.md`  (https://docs.frappe.io/erpnext/accounting-reports)

### Analyse sales
- **Path:** open https://your-site/app (the Desk) and find *Sales Reports and Analytics* — the documentation page below shows the screen
- **Documented steps:**
  1. Open the Selling workspace
  2. Select a report, or search for it by name
  3. Set Company, date range, and other filters
- **Full page, bundled offline:** `docs/erpnext/erpnext__sales-analytics.md`  (https://docs.frappe.io/erpnext/sales-analytics)

### Build a custom report
- **Path:** open https://your-site/app (the Desk) and find *Making Custom Reports* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__making-custom-reports.md`  (https://docs.frappe.io/erpnext/making-custom-reports)

### Email a report on a schedule
- **Path:** https://your-site/app → **Home > Settings > Auto Email Report**
- **Documented steps:**
  1. Go to the Auto Email Report list, click on New
  2. Select the Report for which you want to generate emails
  3. Select the user for which you want to create this report (permissions will apply for this user)
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__auto-email-reports.md`  (https://docs.frappe.io/erpnext/auto-email-reports)

### Build ERPNext dashboards
- **Path:** open https://your-site/app (the Desk) and find *ERPNext Dashboards* — the documentation page below shows the screen
- **Documented steps:**
  1. Use Accounting Reports for financial review
  2. Use Sales Reports for sales performance
  3. Use Buying Reports for procurement tracking
  4. Use Stock Level Report and Stock Ledger Report for inventory monitoring
  5. Use Manufacturing Dashboard and Production Analytics for production review
  6. Use Project Reports for project tracking
  7. Use Support Reports for customer support review
  8. Use Insights Dashboards when you need custom dashboards across modules
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__erpnext-dashboards.md`  (https://docs.frappe.io/erpnext/erpnext-dashboards)

### Connect a data source in Insights
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Add Data Source* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__connect-data__add-data-source.md`  (https://docs.frappe.io/insights/connect-data/add-data-source)

### Write a query in Insights
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Overview* — the documentation page below shows the screen
- **Documented steps:**
  1. Query Builder Visual, no-code interface (recommended for most users)
  2. SQL Editor Write SQL directly (for SQL experts)
  3. Script Editor Python scripts for complex transformations
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__querying__overview.md`  (https://docs.frappe.io/insights/querying/overview)

### Use expressions in a query
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Expressions* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__querying__expressions.md`  (https://docs.frappe.io/insights/querying/expressions)

### Chart a result in Insights
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Overview* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__charts__overview.md`  (https://docs.frappe.io/insights/charts/overview)

### Publish an Insights dashboard
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Overview* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__dashboards__overview.md`  (https://docs.frappe.io/insights/dashboards/overview)

### Share a dashboard and control access
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Sharing and Access Control* — the documentation page below shows the screen
- **Documented steps:**
  1. Click the "Share" button in dashboard header
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__dashboards__sharing-and-access-control.md`  (https://docs.frappe.io/insights/dashboards/sharing-and-access-control)

### Set Insights permissions
- **Path:** open https://your-site/insights (the Frappe Insights interface) and find *Overview* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/insights/insights__permissions-access-control__overview.md`  (https://docs.frappe.io/insights/permissions-access-control/overview)

