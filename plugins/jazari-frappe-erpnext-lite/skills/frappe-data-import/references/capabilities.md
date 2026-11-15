# Capabilities — Bulk import and migration

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `imp.dataimport` | Import records from a spreadsheet | browser | yes | reversible | `docs/erpnext/erpnext-18.md` lines 490–730 | https://docs.frappe.io/erpnext/data-import |
| `imp.dataexport` | Export records to a spreadsheet | browser | no | reversible | `docs/erpnext/erpnext-18.md` lines 462–488 | https://docs.frappe.io/erpnext/data-export |
| `imp.bulkupdate` | Update many records at once | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 858–888 | https://docs.frappe.io/erpnext/bulk-update |
| `imp.bulkrename` | Rename records in bulk | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 794–856 | https://docs.frappe.io/erpnext/bulk-rename |
| `imp.coaimport` | Import a chart of accounts | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 225–278 | https://docs.frappe.io/erpnext/chart-of-accounts-importer |
| `imp.masters` | Import accounting masters | browser | yes | reversible | `docs/erpnext/erpnext-30.md` lines 541–643 | https://docs.frappe.io/erpnext/import-accounting-masters |
| `imp.balances` | Import advances, payments and balances | browser | yes | irreversible | `docs/erpnext/erpnext-30.md` lines 645–753 | https://docs.frappe.io/erpnext/import-advances-unallocated-payments-bank-stock-and-asset-balances |
| `imp.legacy` | Prepare and map legacy data | guide | no | reversible | `docs/erpnext/erpnext-43.md` lines 446–583 | https://docs.frappe.io/erpnext/prepare-and-map-legacy-data |
| `imp.validate` | Validate a migration | guide | no | reversible | `docs/erpnext/erpnext-67.md` lines 434–583 | https://docs.frappe.io/erpnext/validate-the-migration |
| `imp.quickbooks` | Migrate from QuickBooks | browser | yes | reversible | `docs/erpnext/erpnext-49.md` lines 135–333 | https://docs.frappe.io/erpnext/quickbooks-migrator |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

