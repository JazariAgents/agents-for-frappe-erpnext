<!-- Frappe documentation: erpnext, part 27 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__finance-book.md -->
---
title: "Finance Book | ERPNext Documentation"
description: "Learn how to use Finance Books in ERPNext for alternate accounting views, company defaults, report filters, and separate fixed-asset depreciation schedules."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/finance-book"
updated: "2026-08-14"
---

A Finance Book lets the same [Company](https://docs.frappe.io/erpnext/company) maintain parallel accounting views when a transaction or depreciation schedule must belong to one reporting basis but not another. A business may keep one book for statutory reporting and another for management or shareholder reporting.



Finance Books are optional. Do not create several books merely to separate departments, branches, projects, or product lines. Use [Cost Centers](https://docs.frappe.io/erpnext/cost-center) or [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions) for those reporting segments. Use Finance Books only when the same company needs alternate accounting treatments or report views.



Typical uses include:

- statutory and management depreciation using different methods or useful lives;
- local accounting rules and a separate group-reporting basis;
- an alternate internal balance sheet without changing the company's primary ledger view.

## Before you begin

Agree the purpose and ownership of every book with your accountant. Decide which book is the company default, which entries must be common to all books, and which reports reviewers will run.

The example below uses **Statutory Reporting** as the default Finance Book for Nova Electronics Trading and **Management Reporting** as an alternate book.

## Create Finance Books

Open **Finance Book** and select **Add Finance Book**. Enter a clear name that describes the reporting basis, then save.

Create only the books your reporting policy requires. The Finance Book record itself contains a name; its effect comes from selecting it on accounting transactions, depreciation schedules, and reports.



![Finance Book list with Statutory Reporting and Management Reporting](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-finance-book-list.png)

## Set the company default

Open the Company record and select the **Accounts** tab. Set **Default Finance Book** to the book that represents normal accounting for that company, then save.



![Default Finance Book on the Company record](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-company-default-finance-book.png)

The default is important because the current [Journal Entry](https://docs.frappe.io/erpnext/journal-entry) Finance Book field is read-only. ERPNext carries the company's default book into new Journal Entries instead of asking users to choose it manually each time.

Do not change the default casually after transactions exist. Review the effect on reports and future entries with your accountant first.

## Record an entry in a Finance Book

Create the transaction using the normal workflow. In a Journal Entry, open **More Info** and review the **Finance Book** value before submission.



![Finance Book carried into a submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-journal-entry-finance-book.png)

The example posts a $450 maintenance adjustment to **Statutory Reporting**:


| Account                     | Debit | Credit | Finance Book effect            |
| --------------------------- | -----: | ------: | ------------------------------ |
| Office Maintenance Expenses | $450  |        | Appears in the statutory book. |
| Nova Operating Bank         |       | $450   | Appears in the statutory book. |


An entry with a specific Finance Book belongs to that book. An entry whose Finance Book is blank is treated as common and is included in Finance Book report views. This preserves the original ERPNext behavior for transactions that apply to every reporting basis.

## Review reports by Finance Book

Open the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), [Trial Balance](https://docs.frappe.io/erpnext/trial-balance), [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet), or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement). Select the company, dates, and Finance Book, then refresh the report.



![General Ledger filtered by Statutory Reporting Finance Book](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-general-ledger-finance-book-filter.png)

In General Ledger, **Include Default FB Entries** is enabled by default. When it is enabled, ERPNext uses the company's default Finance Book and includes common entries whose Finance Book is blank. If you select a book different from the company default, clear **Include Default FB Entries** first. ERPNext otherwise stops the report and asks you to clear it.

Use the same filters when comparing reports. A report filtered to one Finance Book cannot be compared reliably with an unfiltered report or a report using a different setting for default-book entries.

## Use Finance Books for depreciation

A company may depreciate the same [Asset](https://docs.frappe.io/erpnext/asset) differently for statutory and management reporting. For example, the statutory book may use Written Down Value while the management book uses Straight Line.

On the asset's Finance Books table, each row can hold its own:


| Field                         | What it controls                                                        |
| ----------------------------- | ----------------------------------------------------------------------- |
| Finance Book                  | Reporting book that receives the depreciation entries.                  |
| Depreciation Method           | Straight Line, Double Declining Balance, Written Down Value, or Manual. |
| Frequency of Depreciation     | Number of months between scheduled postings.                            |
| Total Number of Depreciations | Number of scheduled depreciation entries.                               |
| Depreciation Posting Date     | Date from which the schedule begins.                                    |
| Salvage Value                 | Expected value after the useful life.                                   |
| Rate of Depreciation          | Percentage used where the selected method requires it.                  |


ERPNext can generate a separate [depreciation schedule](https://docs.frappe.io/erpnext/asset-depreciation) for each Finance Book and post the resulting automatic depreciation entries to the corresponding book. This keeps alternate asset values separate without duplicating the asset master.

## Important fields and what they mean


| Field or control           | Where it appears                               | Meaning                                                                                                |
| -------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Name                       | Finance Book                                   | Identifies the reporting basis. Use a stable, policy-oriented name.                                    |
| Default Finance Book       | Company                                        | Default book carried into supported accounting transactions.                                           |
| Finance Book               | Journal Entry and supported accounting records | Book to which the resulting GL entries belong.                                                         |
| Finance Book               | Financial reports                              | Limits the report to the selected book plus common entries.                                            |
| Include Default FB Entries | General Ledger                                 | Includes the company's default book and common entries. Clear it before reporting on a different book. |


## Troubleshooting

### A depreciation entry does not appear in the Trial Balance

Open the report and select the Finance Book used by the asset's depreciation schedule. A Finance Book-specific entry may not appear in a report using another book or no matching book filter.

### ERPNext asks me to clear Include Default FB Entries

The report has a Finance Book different from the company's default while **Include Default FB Entries** is enabled. Clear the checkbox, keep the alternate book selected, and refresh.

### The Journal Entry Finance Book cannot be edited

This is expected in current ERPNext. The field is read-only and comes from the company's **Default Finance Book**. Review the Company setup before creating entries that require a different accounting basis.

### Two Finance Book reports do not reconcile

Confirm that both reports use the same company, date range, accounts, opening-entry settings, and **Include Default FB Entries** choice. Then identify entries assigned exclusively to one book and compare the related asset schedules or Journal Entries.

### An entry appears in more than one Finance Book

Check whether the transaction's Finance Book is blank. Blank entries are common entries and appear with Finance Book report views. Assign a book only when the transaction belongs exclusively to that reporting basis.

## FAQs

### Is a Finance Book mandatory?

No, A company with one accounting basis can operate without creating additional Finance Books.

### Should I create one Finance Book for each department?

No, Use Cost Centers or Accounting Dimensions for departments, branches, projects, and other operational segments. Finance Books are for alternate accounting treatments or reporting bases.

### Can the same asset use different depreciation methods?

Yes, Add separate Finance Book rows to the asset and configure a different depreciation method or schedule for each reporting basis.

### Why does a blank Finance Book entry appear in a filtered report?

A blank Finance Book means the entry is common. ERPNext includes common entries when it builds a Finance Book view so shared transactions are not lost.

### Can I change the default Finance Book after posting transactions?

Technically the Company setting can be changed, but treat it as an accounting-policy change. Review existing entries, future posting behavior, report filters, and audit requirements before changing it.

## Related topics

- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Asset Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions)
- [Cost Center](https://docs.frappe.io/erpnext/cost-center)

<!-- page: erpnext/erpnext__financial-report-template.md -->
---
title: "Financial Report Template"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/financial-report-template"
updated: "2026-08-14"
---

Nova Industries prepares monthly reports for its managers, investors, and lenders. The finance team needs one concise Profit and Loss view for the board and an IFRS-style Cash Flow presentation for external readers. Rebuilding each version in a spreadsheet is slow, makes formulas difficult to govern, and creates uncertainty about whether every report still agrees with the ledger.



A Financial Report Template is a reusable blueprint that turns the same submitted accounting data into different report presentations. Nova can standardise headings across subsidiaries, reuse calculations such as Gross Profit and Operating Margin, hide zero or supporting rows, control signs and charts, and produce the same approved structure every month without changing its Chart of Accounts.



Separate templates can support board packs, investor updates, lender reporting, group reporting, and regional presentation requirements. A template controls grouping, labels, calculations, and layout. It does not by itself make the underlying books compliant with IFRS, US GAAP, or another country's rules because recognition, valuation, depreciation, tax, and disclosure requirements must also be configured and professionally reviewed.

## Before you begin

- Review the [Chart of Accounts](/erpnext/chart-of-accounts) and assign Account Categories where the template will filter by category.
- Decide the report's required lines, calculations, hierarchy, and sign presentation.
- Choose stable Line References that formulas can reuse.
- Test the template on a non-production company and period before relying on it for reporting.

## Start from a template

Open Financial Report Template. ERPNext may provide reusable templates that can be reviewed and adapted, or you can create a new template for a controlled reporting requirement.

![Financial Report Template list on the Nova develop demo site](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-list.png)

## Create the template

![Standard Cash Flow Statement Financial Report Template opened on the Nova Industries demo site](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)



1. Enter a descriptive Template Name and select the Report Type.
2. Add rows to the Report Line Items table in the order they should appear.
3. Select the Data Source for each row.
4. Give calculated or reusable rows a unique Line Reference.
5. Configure formatting, visibility, sign, and chart options.
6. Save, run the associated report, and reconcile the output with standard financial statements.

## Choose a row data source

![Report Line Items in the Standard Cash Flow Statement template](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)




| Data source       | Use it for                                                      | Example                                       |
| ----------------- | --------------------------------------------------------------- | --------------------------------------------- |
| Account Data      | Balances selected through account filters or categories         | All accounts in Revenue from Operations       |
| Calculated Amount | Arithmetic based on referenced rows                             | `REVENUE - COST_OF_GOODS_SOLD`                |
| Custom API        | Approved server-side logic unavailable through standard filters | A specialised regulatory or management metric |
| Visual row        | Headers, blank lines, or layout structure                       | OPERATING EXPENSES                            |


## Important row fields


| Field                     | Meaning                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Display Name              | The line label shown to report readers.                                                                          |
| Line Reference            | A unique code used by calculations and other rows. Start with a letter and use letters, numbers, or underscores. |
| Formula or Account Filter | The expression, filter, or API path used by the selected data source.                                            |
| Balance Type              | Opening balance, closing balance, or movement during the period.                                                 |
| Reverse Sign              | Changes presentation when a line should appear with the opposite sign.                                           |
| Hide If Zero              | Removes an empty line from the rendered report.                                                                  |
| Hidden Line               | Keeps a supporting calculation available without displaying it.                                                  |
| Include in Charts         | Makes the line eligible for the report chart where supported.                                                    |


## Build calculations safely

Nova can define `REVENUE` and `COGS` as account-data rows, then calculate `GROSS_PROFIT` with `REVENUE - COGS`. A margin row can use `(GROSS_PROFIT / REVENUE) * 100 if REVENUE != 0 else 0` to avoid division by zero.

## Validate coverage and output

Check that all intended accounts are included once, formulas reference valid rows, no circular dependency exists, and parentheses are balanced. Compare the template output with the standard [Balance Sheet or Profit and Loss Statement](/erpnext/accounting-reports) for the same company, period, Finance Book, and dimensions.

## See a template in the report

Nova selects the **Cash Flow Statement (IFRS)** template in the Cash Flow report. The report now uses the template's headings, ordering, visual rows, and calculations while continuing to read the same General Ledger entries.

![Cash Flow report for Nova Industries rendered with the Cash Flow Statement IFRS Financial Report Template](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-ifrs-output-v2.png)

The result separates cash flows from operating activities, presents supporting adjustments such as depreciation and finance costs, and retains calculated totals such as operating profit before working-capital changes. Finance can reuse this view for every period and still drill into the underlying accounting values when a number needs investigation.

## Troubleshooting

### A formula references an unknown line

Confirm that the source row has a Line Reference and that the formula uses the exact code. Keep references unique and create source rows before dependent calculations.

### An account is missing from the report

Review its Account Category and the row's account filter. Also check whether a parent or child account was selected and whether Hide If Zero suppresses the line.

### The report total differs from the standard statement

Align company, dates, Finance Book, cost center, dimensions, currency, period-closing treatment, and accumulation options. Then check for omitted or duplicated accounts.

## Frequently asked questions

### Should I edit a built-in template?

Use a controlled copy when the standard template must remain available as a baseline. Document every custom calculation and account category dependency.

### Can one template work across companies?

A category-based design can support comparable charts across companies, but each company must map accounts consistently and the output must be tested separately.

### Can a template replace statutory review?

The template controls presentation and calculations inside ERPNext. It does not determine whether the report meets local statutory, audit, or filing requirements.

## Related topics

- [Using Custom API Rows](/erpnext/using-custom-api-rows-in-financial-report-template)
- [Accounting Reports](/erpnext/accounting-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Finance Book](/erpnext/finance-book)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__fiscal-year-error.md -->
---
title: "Fixing Fiscal Year Error"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fiscal-year-error"
updated: "2026-08-14"
---

Nova Industries creates an invoice dated 2 January 2027, but ERPNext reports that the date is not in the selected fiscal year. The transaction date, the selected Fiscal Year, and the company’s defaults no longer agree. Create the missing year or correct the default instead of changing the document to an inaccurate date.

## Resolve the error

1. Open **Fiscal Year** and confirm a record covers the transaction date.
2. Check the start date, end date, and company assignment.
3. Set the new Fiscal Year as default when it should be used for new transactions.
4. Open Global Defaults and confirm the default Fiscal Year.
5. Reload ERPNext and reopen the transaction.

![Fiscal Year start and end dates highlighted](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-fiscal-year-dates.png)



## Troubleshooting

### The year exists but the error remains

Check whether the Fiscal Year is assigned to the transaction’s company, whether another field explicitly contains the old year, and whether the posting date falls exactly within the configured range.

### The date is intentionally in an older year

Select the appropriate fiscal year and confirm that the period is not frozen or closed. Obtain approval before entering a backdated accounting transaction.

## Frequently asked questions

### Should I change the date just to submit?

The posting date should reflect the real accounting event. Fix the year setup or obtain the required period access instead of using a false date.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__fiscal-year.md -->
---
title: "Fiscal Year | ERPNext Documentation"
description: "Create, assign, and manage fiscal years in ERPNext and understand how they differ from accounting periods and year-end closing."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fiscal-year"
updated: "2026-08-14"
---

A financial report is meaningful only when ERPNext knows where one reporting year ends and the next begins. A Fiscal Year defines that period for transactions, budgets, opening balances, and year-end closing.



For Nova Industries, the finance team may report from January to December while another company on the same site follows April to March. Separate Fiscal Year records let both companies post and compare transactions using the periods required by their owners, auditors, and local regulations.



This page shows how to create the period, assign it to the right companies, control posting dates, and avoid gaps or overlaps that can make transactions fail validation.

## Create a Fiscal Year

1. Go to **Home &gt; Accounting &gt; Accounting Masters &gt; Fiscal Year**.
2. Click **Add Fiscal Year**.
3. Enter a name, start date, and end date.
4. Add the companies that use it.
5. Enable **Is Short Year** only for a genuine transition period shorter than twelve months.
6. Save.

![Fiscal Year dates and company](/files/fiscal-year-dates.webp)

## Set the default Fiscal Year

Open the Fiscal Year and use the action to set it as default. ERPNext uses the default year when it initializes posting dates and report filters.

The posting date still determines the actual fiscal year. A transaction cannot be posted outside a valid Fiscal Year for its company.

## Create the next year

ERPNext can create the next Fiscal Year shortly before the current year ends. Confirm the dates and company assignment before users begin posting in it.

## Fiscal Year, Accounting Period, and closing

These records serve different purposes:


| Record                 | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| Fiscal Year            | Defines the accounting year and reporting period      |
| Accounting Period      | Restricts selected transaction types for a date range |
| Period Closing Voucher | Transfers profit or loss to a closing account         |


Creating a new Fiscal Year does not close the previous one. Complete reconciliation, adjustments, reporting, and the closing voucher as separate activities.

## Troubleshooting

**The posting date is outside the Fiscal Year**

Create or assign the correct Fiscal Year to the company. Do not alter historical dates to bypass the validation.

**A report opens in the wrong year**

Change the report filter or set the intended Fiscal Year as default.

## Related topics

- [Accounting Period](https://docs.frappe.io/erpnext/accounting-period)
- [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher)
- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)
- [Accounting Setup Checklist](https://docs.frappe.io/erpnext/accounting-setup-checklist)

<!-- page: erpnext/erpnext__france.md -->
---
title: "Requirements for France"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/france"
updated: "2026-07-02"
---


ERPNext aims to support local regulation for different regions in the world. In most cases, ERPNext is very flexible, so you can easily add custom fields and make custom reports to support the regulation of your region.

This section contains region specific features for France.

- [Le Fichier des Écritures Comptables (FEC)](/erpnext/fichier_des_ecritures_comptables)
- [Sales and Payment Transactions](/erpnext/local_overrides)

<!-- page: erpnext/erpnext__frappe-healthcare.md -->
---
title: "Healthcare Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/frappe-healthcare"
updated: "2026-07-04"
---

Frappe Healthcare was earlier available as the Healthcare module inside ERPNext. It has now been separated into a dedicated open-source app called Marley Health.

Marley Health is owned and maintained by earthians Health Informatics Private Limited. It can be installed alongside ERPNext when an organization wants to manage healthcare workflows such as patients, appointments, consultations, clinical records, laboratory tests, procedures, and billing.

Marley Health documentation: [https://marley.frappe.cloud/docs](https://marley.frappe.cloud/docs)

## Basic features

### Patient management

Marley Health helps maintain patient records, demographics, contact details, medical history, and related healthcare documents. The patient record becomes the central place from which appointments, consultations, lab tests, procedures, and billing can be tracked.

### Healthcare practitioners

Organizations can maintain doctors, consultants, therapists, and other healthcare practitioners. These records are used for appointments, schedules, consultations, and clinical documentation.

### Appointments and scheduling

The app supports appointment booking and scheduling so front-desk and clinical teams can manage patient visits. Appointments can be linked to patients, practitioners, departments, and service units.

### Patient encounters and consultations

Healthcare teams can record consultations using patient encounters. Encounters help capture symptoms, diagnosis, observations, notes, prescriptions, investigations, and follow-up advice.

### Clinical records

Marley Health helps maintain structured healthcare records such as vital signs, prescriptions, medical observations, and other clinical information. This gives practitioners a clearer view of the patient's treatment history.

### Laboratory tests and procedures

The app supports lab test and clinical procedure workflows. Tests and procedures can be ordered, recorded, and linked back to the patient record.

### Inpatient care

For facilities that admit patients, Marley Health can help manage inpatient records, admissions, service units, and patient movement inside the healthcare facility.

### Billing integration

Because Marley Health works with ERPNext, healthcare services can be connected to ERPNext billing documents such as Sales Invoices. This helps combine clinical operations with accounting and revenue tracking.

## Typical healthcare cycle

```
Patient Registration
        |
        v
Appointment Booking
        |
        v
Patient Encounter / Consultation
        |
        +-------------------+
        |                   |
        v                   v
Prescription          Lab Test / Procedure
        |                   |
        +---------+---------+
                  v
              Billing
                  |
                  v
              Follow-up
```

## When should you install Marley Health?

Install Marley Health if your ERPNext site is used by a clinic, hospital, diagnostic center, therapy center, or any healthcare organization that needs patient and clinical workflows.

Read the Marley Health documentation here:

[https://marley.frappe.cloud/docs](https://marley.frappe.cloud/docs)

<!-- page: erpnext/erpnext__freeze-account.md -->
---
title: "Freeze an Account | ERPNext Documentation"
description: "Learn how to freeze an Account in ERPNext, restrict new postings, authorize exception roles, preserve ledger history, verify defaults, and unfreeze it safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/freeze-account"
updated: "2026-08-03"
---

Freeze an individual ledger Account when users should be able to see its history but should no longer post new transactions to it. This is useful after replacing a bank, expense, income, receivable, or payable account without deleting the older ledger.



Freezing does not remove the Account or its existing [General Ledger](https://docs.frappe.io/erpnext/general-ledger) entries. It prevents ordinary users from using that Account in new accounting transactions. An explicitly authorized role can still set frozen Accounts and create or modify entries against them.

> Freeze only an Account that should no longer receive postings. If you need to prevent entries for a past date range instead, use [Freeze Accounting Entries](https://docs.frappe.io/erpnext/freeze-accounting-entries) or an [Accounting Period](https://docs.frappe.io/erpnext/accounting-period).

## Before you begin

Confirm that:

1. The Account is a ledger Account, not a group used to organize the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).
2. Users should retain access to its historical transactions and balances.
3. A replacement Account is available if future invoices, payments, or journals still need a ledger for the same purpose.
4. Defaults in the Company, Customer, Supplier, Item, tax templates, and [Mode of Payment](https://docs.frappe.io/erpnext/mode-of-payment) no longer point to the Account you plan to freeze.
5. The role permitted to manage frozen Accounts has been reviewed.

## Authorize a role to manage frozen Accounts

The permission is company-specific in the current ERPNext interface.

1. Open the required **Company**.
2. Select the **Accounts Closing** tab.
3. In **Roles Allowed to Set and Edit Frozen Account Entries**, select the role that may freeze Accounts and post or modify entries against them.
4. Save the Company.

![Company Accounts Closing tab with Roles Allowed to Set and Edit Frozen Account Entries highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-role-allowed-for-frozen-accounts.png)

Grant this role sparingly. A user with it can bypass the restriction when posting to a frozen Account. In older ERPNext documentation, this control may be described as an Accounts Settings field. On the current develop interface it appears in the Company's **Accounts Closing** tab.

## Freeze an Account

1. Open **Accounting &gt; Chart of Accounts**.
2. Select the Company.
3. Open the ledger Account that should stop receiving transactions.
4. Set **Frozen** to **Yes**.
5. Save the Account.

![Ledger Account with Frozen set to No before the change](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-account-not-frozen.png)



![Ledger Account with Frozen set to Yes and Save highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-freeze-account-before-save.png)

After saving, ordinary users cannot use the Account in accounting transactions. Existing [Journal Entries](https://docs.frappe.io/erpnext/journal-entry), invoices, payments, and reports remain connected to it.

## What freezing changes


| Area                                | Result                                                                                                                                 |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| New accounting transactions         | Ordinary users cannot post entries against the frozen Account.                                                                         |
| Authorized role                     | Users with the Company role configured for frozen Account entries can set the Account as frozen and post or modify entries against it. |
| Existing ledger history             | Remains available in the General Ledger and financial reports.                                                                         |
| Account master                      | Remains in the Chart of Accounts and can be unfrozen later.                                                                            |
| Defaults that reference the Account | Are not automatically replaced. Update them before users create new transactions.                                                      |
| Date-based locks                    | Are unchanged. Freezing one Account is separate from freezing entries through a date or closing an Accounting Period.                  |


## Verify the change

After saving:

1. Reopen the Account and confirm **Frozen** is **Yes**.
2. Check that active defaults now use the intended replacement ledger.
3. Open the [General Ledger report](https://docs.frappe.io/erpnext/general-ledger) and confirm the historical Account balance remains visible.
4. If your controls require a test, use a draft transaction with a test user who does not have the exception role. Do not submit an incorrect entry merely to test the restriction.

## Unfreeze an Account

An authorized user can reopen the Account, set **Frozen** to **No**, and save. Before unfreezing, confirm why postings need to resume and whether a newer Account has already replaced it. Allowing both Accounts to remain active can split transactions and make [financial statements](https://docs.frappe.io/erpnext/accounting-reports) harder to reconcile.

## Troubleshooting


| Issue                                           | What to check                                                                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Frozen cannot be changed                        | Confirm that your user has the role selected in the Company's Accounts Closing settings.                                                    |
| A transaction still posts to the frozen Account | Check whether the user has the authorized role. Also confirm that the transaction used the Account you froze, not a similarly named ledger. |
| New transactions default to the frozen Account  | Replace the Account in Company and master defaults, tax templates, payment modes, and transaction templates.                                |
| A past period must be locked                    | Use Accounts Frozen Till Date or an Accounting Period. Freezing an Account controls a ledger, not a date range.                             |
| Reports still show the Account                  | This is expected. Freezing stops new postings and does not remove historical balances.                                                      |


## Frequently asked questions

### Does freezing an Account delete it?

No, The Account and its historical ledger entries remain available. The restriction applies to new or modified accounting entries.

### Is a frozen Account the same as a disabled Account?

No, **Frozen** is an accounting control that blocks ordinary postings while permitting a configured role to handle exceptions. **Disable** is a broader master-state control. Use the option that matches your control objective.

### Can an authorized user post to a frozen Account?

Yes, A user with the role configured in **Roles Allowed to Set and Edit Frozen Account Entries** can create or modify entries against it. Keep that role limited and review its assignments.

### Does freezing an Account affect its balance?

No, Existing debits, credits, and balances remain unchanged. The Account continues to appear in reports based on its historical postings.

### When should I use a date freeze instead?

Use **Accounts Frozen Till Date** when the restriction should apply to accounting entries before a cutoff date. Use an Accounting Period when selected transaction types must be closed for a completed period. Use **Frozen** on the Account when one specific ledger should stop receiving entries regardless of date.

## Related topics

- [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts)
- [Freeze Accounting Entries](https://docs.frappe.io/erpnext/freeze-accounting-entries)
- [Accounting Period](https://docs.frappe.io/erpnext/accounting-period)
- [Company](https://docs.frappe.io/erpnext/company-setup)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)

<!-- page: erpnext/erpnext__freeze-accounting-entries.md -->
---
title: "Freeze Accounting Entries                                          "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/freeze-accounting-entries"
updated: "2026-08-14"
---

Nova Industries went live on ERPNext on 1 January. If someone accidentally posts a transaction dated in December, the opening balances and signed-off legacy reports no longer agree. **Accounts Frozen Upto** gives finance a simple cut-off date: ordinary users cannot create or change accounting entries on or before that date.



Use this control for migration cutover dates, completed month-end closes, and audited periods. Unlike an [Accounting Period](/erpnext/accounting-period), it is a broad accounting freeze rather than a list of selected document types.

## Set the frozen date

1. Open the **Company** record.
2. Open the **Accounts Closing** tab.
3. Set **Accounts Frozen Till Date** to the last protected date.
4. Select **Roles Allowed to Set and Edit Frozen Account Entries**.
5. Save the Company and test with a non-privileged account before relying on the control.

![Company Accounts Closing tab showing the frozen date and authorized role](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-company-frozen-period.png)



## Use the exception role carefully

The role is for approved corrections, not a way to continue routine backdated posting. Keep membership small, require supporting evidence, and review the General Ledger and Version history after an exception.

## Troubleshooting

### A user can still post inside the frozen period

Check whether the user has the authorized frozen-entries role. Confirm the document actually posts accounting entries and that its posting date is on or before the configured date.

### The authorized user is still blocked

Check for a submitted Accounting Period, fiscal-year restriction, immutable-ledger rule, or stock reposting restriction. These are separate controls and the frozen-entries role does not override every validation.

## Frequently asked questions

### Does freezing delete or reverse anything?

It prevents new changes through the cut-off date. Existing ledger entries remain unchanged.

### Can I move the date forward every month?

That is a common month-end practice after reconciliations and approval. Record the close checklist and the person who approved each change.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)
