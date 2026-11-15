# Capabilities — Manufacturing and production

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `mfg.bom` | Build a bill of materials | api | yes | reversible | `docs/erpnext/erpnext__bill-of-materials.md` | https://docs.frappe.io/erpnext/bill-of-materials |
| `mfg.bomcreator` | Design a BOM with the BOM creator | browser | yes | irreversible | `docs/erpnext/erpnext__bom-creator-new.md` (ERPNext 16.53 and later; older screen: `docs/erpnext/erpnext__bom-creator.md`) | https://docs.frappe.io/erpnext/bom-creator-new |
| `mfg.bomupdate` | Update BOMs in bulk | browser | yes | reversible | `docs/erpnext/erpnext__bom-update-tool.md` | https://docs.frappe.io/erpnext/bom-update-tool |
| `mfg.workorder` | Run a work order | api | yes | irreversible | `docs/erpnext/erpnext__work-order.md` | https://docs.frappe.io/erpnext/work-order |
| `mfg.jobcard` | Record work on a job card | api | yes | irreversible | `docs/erpnext/erpnext__job-card.md` | https://docs.frappe.io/erpnext/job-card |
| `mfg.productionplan` | Plan production | api | yes | reversible | `docs/erpnext/erpnext__production-plan.md` | https://docs.frappe.io/erpnext/production-plan |
| `mfg.mrp` | Plan material requirements | guide | no | reversible | `docs/erpnext/erpnext__material-requirements-planning-mrp.md` | https://docs.frappe.io/erpnext/material-requirements-planning-mrp |
| `mfg.workstation` | Set up workstations | browser | yes | reversible | `docs/erpnext/erpnext__workstation.md` | https://docs.frappe.io/erpnext/workstation |
| `mfg.operation` | Define operations and routing | browser | yes | reversible | `docs/erpnext/erpnext__routing.md` | https://docs.frappe.io/erpnext/routing |
| `mfg.capacity` | Plan capacity | guide | no | reversible | `docs/erpnext/erpnext__capacity-planning.md` | https://docs.frappe.io/erpnext/capacity-planning |
| `mfg.plantfloor` | Watch the plant floor | browser | no | reversible | `docs/erpnext/erpnext__plant-floor.md` | https://docs.frappe.io/erpnext/plant-floor |
| `mfg.scrap` | Handle scrap and disassembly | browser | yes | reversible | `docs/erpnext/erpnext__scrap-management.md` | https://docs.frappe.io/erpnext/scrap-management |
| `mfg.settings` | Configure manufacturing settings | browser | yes | reversible | `docs/erpnext/erpnext__manufacturing-settings.md` | https://docs.frappe.io/erpnext/manufacturing-settings |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

