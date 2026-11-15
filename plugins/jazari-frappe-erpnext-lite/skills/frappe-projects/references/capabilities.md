# Capabilities — Projects, tasks and timesheets

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `proj.project` | Run a project | api | yes | reversible | `docs/erpnext/erpnext-12.md` lines 1697–1838 | https://docs.frappe.io/erpnext/project |
| `proj.task` | Manage tasks | api | yes | reversible | `docs/erpnext/erpnext-16.md` lines 2564–2657 | https://docs.frappe.io/erpnext/tasks |
| `proj.timesheet` | Record timesheets | api | yes | reversible | `docs/erpnext/erpnext-17.md` lines 1379–1473 | https://docs.frappe.io/erpnext/timesheets |
| `proj.template` | Start from a project template | browser | yes | reversible | `docs/erpnext/erpnext-12.md` lines 1556–1586 | https://docs.frappe.io/erpnext/project-template |
| `proj.costing` | Track project costing | browser | no | reversible | `docs/erpnext/erpnext-12.md` lines 1343–1385 | https://docs.frappe.io/erpnext/project-costing |
| `proj.profitability` | Measure project profitability | browser | no | reversible | `docs/erpnext/erpnext-12.md` lines 1435–1477 | https://docs.frappe.io/erpnext/project-profitability |
| `proj.billing` | Bill a customer from a timesheet | api | yes | irreversible | `docs/erpnext/erpnext-14.md` lines 133–172 | https://docs.frappe.io/erpnext/sales-invoice-from-timesheet |
| `proj.activitycost` | Set activity costs | browser | yes | reversible | `docs/erpnext/erpnext-01.md` lines 2191–2218 | https://docs.frappe.io/erpnext/activity-cost |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

