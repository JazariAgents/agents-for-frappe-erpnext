# Capabilities — Projects, tasks and timesheets

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `proj.project` | Run a project | api | yes | reversible | `docs/erpnext/erpnext__project.md` | https://docs.frappe.io/erpnext/project |
| `proj.task` | Manage tasks | api | yes | reversible | `docs/erpnext/erpnext__tasks.md` | https://docs.frappe.io/erpnext/tasks |
| `proj.timesheet` | Record timesheets | api | yes | reversible | `docs/erpnext/erpnext__timesheets.md` | https://docs.frappe.io/erpnext/timesheets |
| `proj.template` | Start from a project template | browser | yes | reversible | `docs/erpnext/erpnext__project-template.md` | https://docs.frappe.io/erpnext/project-template |
| `proj.costing` | Track project costing | browser | no | reversible | `docs/erpnext/erpnext__project-costing.md` | https://docs.frappe.io/erpnext/project-costing |
| `proj.profitability` | Measure project profitability | browser | no | reversible | `docs/erpnext/erpnext__project-profitability.md` | https://docs.frappe.io/erpnext/project-profitability |
| `proj.billing` | Bill a customer from a timesheet | api | yes | irreversible | `docs/erpnext/erpnext__sales-invoice-from-timesheet.md` | https://docs.frappe.io/erpnext/sales-invoice-from-timesheet |
| `proj.activitycost` | Set activity costs | browser | yes | reversible | `docs/erpnext/erpnext__activity-cost.md` | https://docs.frappe.io/erpnext/activity-cost |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

