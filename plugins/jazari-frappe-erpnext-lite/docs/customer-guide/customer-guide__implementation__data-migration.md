---
title: "How to migrate data properly?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/data-migration"
updated: "2026-07-21"
---

Data migration is the phase businesses underestimate most, and the one that most often causes delays and go-live stress. Moving from your existing systems into Frappe is rarely just a copy - it's cleaning, mapping, and reconciling data that has usually accumulated inconsistencies over years. Treating it seriously from the start is one of the highest-return things you can do.



## Why it's harder than it looks

The data in your current systems is rarely as clean as you think. Duplicate customers, inconsistent product codes, missing fields, obsolete records, and reconciliation gaps are normal. Migrate that as-is, and you carry every problem into the new system - and undermine trust in it on day one. The work isn't the moving; it's the cleaning and deciding.



## What to migrate - and what not to

A useful discipline: migrate what you *need*, not everything you *have*.



- **Master data** - customers, suppliers, items, employees, the chart of accounts. This you almost always need, and it's worth cleaning thoroughly.
- **Open transactions** - outstanding invoices, open orders, current stock balances. Needed to operate from day one.
- **Opening balances** - financial balances as of go-live, so your books are correct.
- **Historical transactions** - years of closed transactions. Here, be selective. You often *don't* need to migrate full history into the live system; keeping it accessible in an archive or the old system for reference is frequently cheaper and cleaner than migrating it all. Decide based on real need - legal retention, reporting, audit - not on instinct to keep everything.



## How migration works with Frappe

Frappe provides structured ways to import data - typically via spreadsheet-based import tools that map your source columns to the system's fields, with validation to catch errors before they land. For larger or more complex migrations, data can be brought in programmatically through the API. Your partner usually leads this, building and testing the mapping, running trial imports, and reconciling results. 



The pattern that works: **map, trial-import a sample, reconcile, fix, then do the full run** - never a single untested bulk load straight into production.



## A sensible sequence

1. **Audit** your source data and decide what's in scope.
2. **Clean** at source where you can - dedupe, standardise, fill gaps.
3. **Map** source fields to Frappe's structure.
4. **Trial migrate** a representative sample into a test environment.
5. **Reconcile** - do totals, counts, and balances match the source? Have users check records they know.
6. **Fix** mapping and data issues, and repeat the trial until it's clean.
7. **Final migration** as part of go-live, with a final reconciliation before you rely on it.

## For smaller businesses

If you're small and your data lives in a spreadsheet or a simple system, migration may genuinely be straightforward - clean the spreadsheet, use the import tool, check the results. The principles above still apply (clean first, reconcile after), just at a lighter weight. The free onboarding from Frappe can help with a basic import (see [how Frappe works](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company)).



---