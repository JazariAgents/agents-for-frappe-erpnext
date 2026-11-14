# Guide adapter — Bulk import and migration

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Prepare and map legacy data
- **What the page says:** Data exported from an older accounting system rarely matches ERPNext exactly. Preparing and mapping means cleaning that export and translating its customers, suppliers, accounts, tax codes, currencies, and identifiers into values ERPNext can import safely.
- **It covers:** Freeze the source extract, Clean source records, Build mapping tables, Map the Chart of Accounts, Prepare outstanding invoices, Prepare the opening Trial Balance, Prepare stock and assets, Run pre-import checks
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext__prepare-and-map-legacy-data.md`  (https://docs.frappe.io/erpnext/prepare-and-map-legacy-data)

### Validate a migration
- **What the page says:** A successful import only proves that ERPNext accepted the rows. Validation proves that the new books represent the same financial position as the signed-off source system.
- **It covers:** Reconcile in layers, Master validation, Receivables and payables, Bank and cash, Stock, Fixed assets, Trial Balance and financial statements, Test real workflows
- **Documented detail:**
  1. Master counts and mappings
  2. Imported document counts and totals
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext__validate-the-migration.md`  (https://docs.frappe.io/erpnext/validate-the-migration)

