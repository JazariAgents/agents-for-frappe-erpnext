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
- **Path:** https://your-site/app → **Home > Projects > Project**
- **Record type:** Project
- **Documented steps:**
  1. Go to the Project list and click on New
  2. Add the following details
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__project.md`  (https://docs.frappe.io/erpnext/project)

### Manage tasks
- **Path:** https://your-site/app → **Home > Projects > Task**
- **Record type:** Task
- **Documented steps:**
  1. Go to the Task List and click on New
  2. Add the subject of the task
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__tasks.md`  (https://docs.frappe.io/erpnext/tasks)

### Record timesheets
- **Path:** https://your-site/app → **Home > Projects > Time Tracking > Timesheet**
- **Record type:** Timesheet
- **Documented steps:**
  1. Go to the Task for which you want to create a new Timesheet
  2. Go to 'Timesheet' under the Activity section on the Dashboard. The plus icon '+' here would re-direct you to the Timesheet creation page
  3. Follow the steps to create a Time Sheet
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__timesheets.md`  (https://docs.frappe.io/erpnext/timesheets)

### Start from a project template
- **Path:** https://your-site/app → **Home > Projects > Projects > Project Template**
- **Record type:** Project Template
- **Documented steps:**
  1. Go to the Project Template List and click on New
  2. Add the following details
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__project-template.md`  (https://docs.frappe.io/erpnext/project-template)

### Track project costing
- **Path:** https://your-site/app → **Home > Projects > Activity Type > New**
- **Full page, bundled offline:** `docs/erpnext/erpnext__project-costing.md`  (https://docs.frappe.io/erpnext/project-costing)

### Measure project profitability
- **Path:** open https://your-site/app (the Desk) and find *Project Profitability* — the documentation page below shows the screen
- **Full page, bundled offline:** `docs/erpnext/erpnext__project-profitability.md`  (https://docs.frappe.io/erpnext/project-profitability)

### Bill a customer from a timesheet
- **Path:** open https://your-site/app (the Desk) and find *Sales Invoice from Timesheet* — the documentation page below shows the screen
- **Documented steps:**
  1. Once the Timesheet is submitted, click on 'Create Sales Invoice'
  2. Enter the Item Code and name of the Customer who has to be billed against this Timesheet. The Item could be a Product as well as a Service. Click on 'Create Sales Invoice'
  3. All the details of the Timesheet will get auto-populated in the Sales Invoice
  4. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time
  5. Optionally, you can include payments for POS or make this a credit note
  6. Save and Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__sales-invoice-from-timesheet.md`  (https://docs.frappe.io/erpnext/sales-invoice-from-timesheet)

### Set activity costs
- **Path:** https://your-site/app → **Home > Projects > Time Tracking > Activity Cost**
- **Record type:** Activity Cost
- **Documented steps:**
  1. Go to the Activity Cost list and click on New
  2. Add the name of the Employee for whom you are configuring the Activity Cost
  3. Add the Costing Rate and the Billing Rate for the Employee
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__activity-cost.md`  (https://docs.frappe.io/erpnext/activity-cost)

