# Interface adapter — Projects, tasks and timesheets

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

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Run a project
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Project**, or type *Project* in the search bar at the top
- **Record type:** Project
- **Documented steps:**
  1. Go to the Project list and click on New
  2. Add the following details
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-12.md` lines 1697–1838  (https://docs.frappe.io/erpnext/project)

### Manage tasks
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Task**, or type *Task* in the search bar at the top
- **Record type:** Task
- **Documented steps:**
  1. Go to the Task List and click on New
  2. Add the subject of the task
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-16.md` lines 2564–2657  (https://docs.frappe.io/erpnext/tasks)

### Record timesheets
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Timesheet**, or type *Timesheet* in the search bar at the top
- **Record type:** Timesheet
- **Documented steps:**
  1. Go to the Task for which you want to create a new Timesheet
  2. Go to 'Timesheet' under the Activity section on the Dashboard. The plus icon '+' here would re-direct you to the Timesheet creation page
  3. Follow the steps to create a Time Sheet
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-17.md` lines 1379–1473  (https://docs.frappe.io/erpnext/timesheets)

### Start from a project template
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Setup > Project Template**, or type *Project Template* in the search bar at the top
- **Record type:** Project Template
- **Documented steps:**
  1. Go to the Project Template List and click on New
  2. Add the following details
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-12.md` lines 1556–1586  (https://docs.frappe.io/erpnext/project-template)

### Track project costing
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Project**, or type *Project* in the search bar at the top
- **Full page, bundled offline:** `docs/erpnext/erpnext-12.md` lines 1343–1385  (https://docs.frappe.io/erpnext/project-costing)

### Measure project profitability
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Reports > Profitability Analysis**, or type *Profitability Analysis* in the search bar at the top
- **On this screen:** Set the report's **Project** filter to see one project. ERPNext v16 has no separate Project Profitability report.
- **Full page, bundled offline:** `docs/erpnext/erpnext-12.md` lines 1435–1477  (https://docs.frappe.io/erpnext/project-profitability)

### Bill a customer from a timesheet
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Timesheet**, or type *Timesheet* in the search bar at the top
- **Documented steps:**
  1. Once the Timesheet is submitted, click on 'Create Sales Invoice'
  2. Enter the Item Code and name of the Customer who has to be billed against this Timesheet. The Item could be a Product as well as a Service. Click on 'Create Sales Invoice'
  3. All the details of the Timesheet will get auto-populated in the Sales Invoice
  4. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time
  5. Optionally, you can include payments for POS or make this a credit note
  6. Save and Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-14.md` lines 133–172  (https://docs.frappe.io/erpnext/sales-invoice-from-timesheet)

### Set activity costs
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Projects > Setup > Activity Cost**, or type *Activity Cost* in the search bar at the top
- **Record type:** Activity Cost
- **Documented steps:**
  1. Go to the Activity Cost list and click on New
  2. Add the name of the Employee for whom you are configuring the Activity Cost
  3. Add the Costing Rate and the Billing Rate for the Employee
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-01.md` lines 2191–2218  (https://docs.frappe.io/erpnext/activity-cost)

