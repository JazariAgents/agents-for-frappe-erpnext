# Interface adapter — Bulk import and migration

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

### Import records from a spreadsheet
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Data > Data Import**, or type *Data Import* in the search bar at the top
- **Documented steps:**
  1. Navigate to Data Import
  2. Select the Document Type and the Import Type as *Insert New Records
  3. Click on Save and then download the template
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__data-import.md`  (https://docs.frappe.io/erpnext/data-import)

### Export records to a spreadsheet
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Data > Data Export**, or type *Data Export* in the search bar at the top
- **Documented steps:**
  1. Go to the 'Data Export' DocType
  2. Select the DocType from which the data is to be extracted
  3. Select the file format whether CSV or Excel
  4. Tick the checkbox if you want to export the data without any header notes and column descriptions
  5. Select the fields to export; the red ones are mandatory
  6. You can also add filters to select only specific data. For example, 'Territory = Asia' will export all Customers whose Territory is set as 'Asia'
  7. Click on Export to download the file
- **Full page, bundled offline:** `docs/erpnext/erpnext__data-export.md`  (https://docs.frappe.io/erpnext/data-export)

### Update many records at once
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > Desk > Bulk Update**, or type *Bulk Update* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__bulk-update.md`  (https://docs.frappe.io/erpnext/bulk-update)

### Rename records in bulk
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Data > Rename Tool**, or type *Rename Tool* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__bulk-rename.md`  (https://docs.frappe.io/erpnext/bulk-rename)

### Import a chart of accounts
- **Path (checked on v16.55):** https://your-site/desk → type *Chart of Accounts Importer* in the search bar at the top and open the doctype
- **Record type:** Chart of Accounts Importer
- **Documented steps:**
  1. Select the Company for which you want to import the Chart of Accounts
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__chart-of-accounts-importer.md`  (https://docs.frappe.io/erpnext/chart-of-accounts-importer)

### Import accounting masters
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Data > Data Import**, or type *Data Import* in the search bar at the top
- **Documented steps:**
  1. Groups and parent records
  2. Company-independent masters
  3. Company-specific masters
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__import-accounting-masters.md`  (https://docs.frappe.io/erpnext/import-accounting-masters)

### Import advances, payments and balances
- **Path (checked on v16.55):** https://your-site/desk → type *Opening Invoice Creation Tool* in the search bar at the top and open the doctype
- **On this screen:** Advances and unallocated payments are Payment Entries; bank, stock and asset balances follow the steps in the page.
- **Documented steps:**
  1. Select the cutover date and Company
  2. Add each Item and Warehouse
  3. Enter opening quantity
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__import-advances-unallocated-payments-bank-stock-and-asset-balances.md`  (https://docs.frappe.io/erpnext/import-advances-unallocated-payments-bank-stock-and-asset-balances)

### Migrate from QuickBooks
- **Path (checked on v16.55):** **Not available on ERPNext v16.** The QuickBooks Migrator was removed. Export the QuickBooks lists to spreadsheets and load them with **Data Import** (the frappe-data-import skill) instead. Tell the user this before starting.
- **Documented steps:**
  1. From Awesome-bar, Go to "QuickBooks Migrator" DocType
  2. Go to Inuit Developer Portal
  3. Sign In with your existing account or Sign Up
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__quickbooks-migrator.md`  (https://docs.frappe.io/erpnext/quickbooks-migrator)

## What cannot be done in the interface

- Prepare and map legacy data — an explanation, not an action (guide.md)
- Validate a migration — an explanation, not an action (guide.md)
