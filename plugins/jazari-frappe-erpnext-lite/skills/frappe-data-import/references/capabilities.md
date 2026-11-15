# Capabilities — Bulk import and migration

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `imp.dataimport` | Import records from a spreadsheet | browser | yes | reversible | `docs/erpnext/erpnext-05.md` lines 1481–1721 | https://docs.frappe.io/erpnext/data-import |
| `imp.dataexport` | Export records to a spreadsheet | browser | no | reversible | `docs/erpnext/erpnext-05.md` lines 1453–1479 | https://docs.frappe.io/erpnext/data-export |
| `imp.bulkupdate` | Update many records at once | browser | yes | reversible | `docs/erpnext/erpnext-03.md` lines 2885–2915 | https://docs.frappe.io/erpnext/bulk-update |
| `imp.bulkrename` | Rename records in bulk | browser | yes | reversible | `docs/erpnext/erpnext-03.md` lines 2821–2883 | https://docs.frappe.io/erpnext/bulk-rename |
| `imp.coaimport` | Import a chart of accounts | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 720–773 | https://docs.frappe.io/erpnext/chart-of-accounts-importer |
| `imp.masters` | Import accounting masters | browser | yes | reversible | `docs/erpnext/erpnext-08.md` lines 1738–1840 | https://docs.frappe.io/erpnext/import-accounting-masters |
| `imp.balances` | Import advances, payments and balances | browser | yes | irreversible | `docs/erpnext/erpnext-08.md` lines 1842–1950 | https://docs.frappe.io/erpnext/import-advances-unallocated-payments-bank-stock-and-asset-balances |
| `imp.legacy` | Prepare and map legacy data | guide | no | reversible | `docs/erpnext/erpnext-11.md` lines 2475–2612 | https://docs.frappe.io/erpnext/prepare-and-map-legacy-data |
| `imp.validate` | Validate a migration | guide | no | reversible | `docs/erpnext/erpnext-17.md` lines 3221–3370 | https://docs.frappe.io/erpnext/validate-the-migration |
| `imp.quickbooks` | Migrate from QuickBooks | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 1006–1204 | https://docs.frappe.io/erpnext/quickbooks-migrator |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

