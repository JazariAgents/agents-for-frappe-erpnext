# Capabilities — Projects, tasks and timesheets

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `proj.project` | Run a project | api | yes | reversible | `docs/erpnext/erpnext-46.md` lines 144–285 | https://docs.frappe.io/erpnext/project |
| `proj.task` | Manage tasks | api | yes | reversible | `docs/erpnext/erpnext-62.md` lines 741–834 | https://docs.frappe.io/erpnext/tasks |
| `proj.timesheet` | Record timesheets | api | yes | reversible | `docs/erpnext/erpnext-65.md` lines 408–502 | https://docs.frappe.io/erpnext/timesheets |
| `proj.template` | Start from a project template | browser | yes | reversible | `docs/erpnext/erpnext-46.md` lines 3–33 | https://docs.frappe.io/erpnext/project-template |
| `proj.costing` | Track project costing | browser | no | reversible | `docs/erpnext/erpnext-45.md` lines 658–700 | https://docs.frappe.io/erpnext/project-costing |
| `proj.profitability` | Measure project profitability | browser | no | reversible | `docs/erpnext/erpnext-45.md` lines 750–792 | https://docs.frappe.io/erpnext/project-profitability |
| `proj.billing` | Bill a customer from a timesheet | api | yes | irreversible | `docs/erpnext/erpnext-52.md` lines 133–172 | https://docs.frappe.io/erpnext/sales-invoice-from-timesheet |
| `proj.activitycost` | Set activity costs | browser | yes | reversible | `docs/erpnext/erpnext-03.md` lines 757–784 | https://docs.frappe.io/erpnext/activity-cost |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

