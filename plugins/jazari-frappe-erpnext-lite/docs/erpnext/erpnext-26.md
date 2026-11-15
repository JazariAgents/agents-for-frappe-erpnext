<!-- Frappe documentation: erpnext, part 26 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__fifo-and-moving-average.md -->
---
title: "FIFO and Moving Average"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fifo-and-moving-average"
updated: "2026-06-28"
---

# FIFO & Moving Average Valuation Methods

## 1. Overview

ERPNext values stock **perpetually**: every stock movement (receipt, issue, transfer, manufacture) updates the item's quantity *and* its monetary value in real time through the **Stock Ledger**. The **Valuation Method** decides *how the value of each outgoing unit is calculated* and therefore what your remaining inventory is worth and what your Cost of Goods Sold (COGS) becomes.

ERPNext supports three valuation methods:

- **FIFO** (First In, First Out)
- **Moving Average**
- **Standard Cost** *(covered in a separate guide)*

This guide explains **FIFO** and **Moving Average** — how each works, the accounting they produce, their behavior with backdated entries and reposting, and the pros and cons of each so you can choose the right one per item.

> **Where to set it:** Valuation Method can be set per **Item** (Item master → *Valuation Method*), or defaulted at the **Company** level, or globally in **Stock Settings**. The most specific setting wins (Item → Company → Stock Settings).

---

## 2. FIFO (First In, First Out)

### 2.1 How it works

FIFO assumes the **oldest stock is consumed first**. ERPNext maintains a **FIFO queue** of `[quantity, rate]` layers for each item-warehouse. Every receipt adds a layer at its actual incoming rate; every issue consumes layers from the **front** (oldest) of the queue at *their original rates*.

The valuation rate reported at any moment is the **weighted average of the layers currently remaining** in the queue, but each outgoing unit is costed at the *specific* rate of the layer it is drawn from.

### 2.2 Worked example


| Step | Transaction      | Queue after              | Stock value |
| ---- | ---------------- | ------------------------ | ----------- |
| 1    | Receive 10 @ 100 | `[10 @ 100]`             | 1,000       |
| 2    | Receive 10 @ 120 | `[10 @ 100], [10 @ 120]` | 2,200       |
| 3    | Issue 15         | `[5 @ 120]`              | 600         |


At step 3, the 15 issued units are costed as **10 @ 100 + 5 @ 120 = 1,600** (oldest first). The remaining 5 units stay valued at their original 120.

### 2.3 Accounting impact

In a perpetual-inventory company, the issue posts COGS at the **actual layered cost** of the consumed units:

- COGS (step 3) = 1,600
- Inventory is credited 1,600; remaining inventory asset = 600.

Because outgoing cost reflects the **actual historical purchase price** of the specific units leaving stock, FIFO closely tracks real acquisition cost and is widely accepted for statutory/tax reporting.

### 2.4 Pros

- **Closely matches actual cost flow** — the cost of goods sold reflects the genuine price paid for the specific units consumed.
- **Realistic ending inventory value** — remaining stock is valued at the most **recent** purchase prices, so the balance sheet reflects current replacement-ish cost.
- **Widely accepted** for accounting standards and tax authorities; intuitive and auditable (you can trace which layers were consumed).
- **Good for items with shelf life / lot rotation** (food, pharma, perishables) where you physically issue oldest-first anyway.

### 2.5 Cons

- **Sensitive to backdated entries** — inserting or editing a past transaction changes which layers later issues consume, so **every subsequent ledger entry must be recomputed (reposted)**. On long, dense ledgers this reposting is slow and resource-intensive.
- **Volatile COGS in rising-price environments** — older, cheaper layers are expensed first, which can understate COGS and overstate profit during inflation.
- **More computation / storage** — the layer queue must be maintained and serialized for every item-warehouse.
- **Heavier reposting load** when corrections, cancellations, or landed-cost vouchers touch historical entries.

---

## 3. Moving Average

### 3.1 How it works

Moving Average maintains a **single blended average rate** per item-warehouse. On **every receipt**, the average is recomputed:

```
new average = (existing qty × existing avg rate + incoming qty × incoming rate)
              ──────────────────────────────────────────────────────────────
                             existing qty + incoming qty
```

Issues are costed at the **current average rate** and do **not** change the average; only receipts (and revaluations) move it.

### 3.2 Worked example


| Step | Transaction      | Qty on hand | Avg rate | Stock value |
| ---- | ---------------- | ----------- | -------- | ----------- |
| 1    | Receive 10 @ 100 | 10          | 100      | 1,000       |
| 2    | Receive 10 @ 120 | 20          | 110      | 2,200       |
| 3    | Issue 15         | 5           | 110      | 550         |


At step 2 the average becomes `(10×100 + 10×120) / 20 = 110`. The 15 issued units at step 3 are each costed at **110** → COGS = 1,650; remaining 5 units valued at 110 = 550.

### 3.3 Accounting impact

- COGS (step 3) = **1,650** (15 × average 110).
- Inventory credited 1,650; remaining inventory asset = 550.

Compared with FIFO on the same data, Moving Average **smooths** the cost: COGS is 1,650 vs FIFO's 1,600, and the difference flows into the value of remaining stock.

### 3.4 Pros

- **Smooths out price fluctuations** — a single blended rate dampens the impact of volatile purchase prices, giving steadier COGS and margins.
- **Simpler and lighter** — only one rate per item-warehouse to maintain; no layer queue to store or walk.
- **Easier to understand and reconcile** — "one item, one current cost" is intuitive for operations and reporting.
- **Good for homogeneous, fast-moving, commoditized items** where individual lots are indistinguishable (bulk fasteners, fuel, raw chemicals).

### 3.5 Cons

- **Still requires reposting on backdated entries** — because a past receipt changes the running average for **all later** transactions, ERPNext must recompute the forward chain. Like FIFO, this can be slow on long ledgers.
- **Does not track actual lot cost** — outgoing cost is a blend, so it can diverge from the real price paid for the specific units shipped; less precise for lot-traceable or high-value items.
- **Average can lag reality** — in fast-moving price environments the blended rate trails current market cost, which may misstate margins on individual sales.
- **Less granular audit trail** — you cannot point to "these specific units left at this specific cost," only to the average at that time.

---

## 4. FIFO vs Moving Average — at a glance


| Aspect                           | FIFO                                            | Moving Average                               |
| -------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| **Outgoing cost basis**          | Actual rate of the oldest remaining layer       | Current blended average rate                 |
| **Tracks real lot cost?**        | Yes (layer-accurate)                            | No (blended)                                 |
| **COGS behavior**                | Reflects oldest prices first                    | Smoothed across all receipts                 |
| **Ending inventory value**       | At most recent purchase prices                  | At the blended average                       |
| **Data maintained**              | Queue of `[qty, rate]` layers                   | Single average rate                          |
| **Backdated entry → reposting?** | **Yes** (recompute forward chain)               | **Yes** (recompute forward chain)            |
| **Computation cost**             | Higher (layer walking)                          | Lower (single rate)                          |
| **Best for**                     | Perishables, lot-rotated, audit-sensitive items | Homogeneous, high-volume, commoditized items |
| **Statutory acceptance**         | Very widely accepted                            | Widely accepted                              |


---

## 5. The shared limitation: backdated entries trigger reposting

This is the most important operational characteristic both methods share — and the key contrast with **Standard Cost**.

With **both FIFO and Moving Average**, the value of any stock ledger entry depends on **the entries before it** (which layers exist, or what the running average is). So when you:

- insert a **backdated** transaction,
- **cancel** or **amend** a historical voucher,
- apply a **Landed Cost Voucher** to a past receipt, or
- change a past valuation rate,

…ERPNext must **repost** — recompute the quantity, rate, value, and GL impact of **every subsequent stock ledger entry** for that item-warehouse (a *Repost Item Valuation* job). On items with long, dense histories this is **slow, resource-heavy, and temporarily changes the value of stock you considered settled**.

> If your organization frequently records **backdated corrections** and this reposting cost is painful, consider the **Standard Cost** method (see the separate *Standard Valuation Rate* guide), where the rate is known by date and backdated entries do **not** trigger reposting.

---

## 6. Choosing a method — recommendations


| Your situation                                                     | Recommended method                   |
| ------------------------------------------------------------------ | ------------------------------------ |
| Perishable / shelf-life items, physically issued oldest-first      | **FIFO**                             |
| High-value or lot-traceable items needing precise cost             | **FIFO**                             |
| Statutory/tax regime that expects actual cost flow                 | **FIFO**                             |
| Homogeneous, commoditized, fast-moving items                       | **Moving Average**                   |
| You want smoother, more stable margins                             | **Moving Average**                   |
| You want minimal valuation maintenance overhead                    | **Moving Average**                   |
| You frequently post **backdated** entries and reposting hurts      | **Standard Cost** *(separate guide)* |
| You want predictable, fixed product cost & isolated price variance | **Standard Cost** *(separate guide)* |


### Best practices (both methods)

- **Set the method before the item transacts.** Changing an item's valuation method while stock exists is disruptive and may be blocked.
- **Enable perpetual inventory accounts** (warehouse/stock, stock-received-but-not-billed, COGS, stock adjustment) so valuation and GL stay in lock-step.
- **Batch your historical corrections** and run them in low-traffic windows, since they trigger reposting.
- **Use Landed Cost Vouchers promptly** after receipt to avoid large retroactive revaluations later.
- **Reconcile stock value vs. GL** periodically (Stock Ledger / Stock Balance vs. the inventory account) to catch drift early.
- **Be consistent per item category** so reporting and margins are comparable across similar items.

---

## 7. Summary

- **FIFO** costs outgoing stock at the **actual rate of the oldest remaining layer** — precise, audit-friendly, ideal for perishables and lot-traceable goods, but layer-heavy and reposting-sensitive.
- **Moving Average** costs outgoing stock at a **single blended rate** — simple, smooth, ideal for commoditized high-volume items, but less precise and still reposting-sensitive.
- **Both** recompute (repost) the forward ledger when the past changes. If that cost is the deciding factor, the **Standard Cost** method avoids it entirely — see the *Standard Valuation Rate* guide.

<!-- page: erpnext/erpnext__filter-options-in-select-field.md -->
---
title: "Filter Options in Select Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/filter-options-in-select-field"
updated: "2026-03-02"
---

Let's say you have two drop-down fields named State and City. State has two values Karnataka and Maharashtra and City has four values, Bangalore, Mysore, Mumbai, and Pune. If you would like to filter options in City based on the value chosen in State, you can write custom script as shown below.

```
frappe.ui.form.on("Lead", "state", function(frm) {
  if(frm.doc.state == "Karnataka") {
    set_field_options("city", ["Bangalore","Mysore"])
  } else if(frm.doc.state == "Maharashtra") {
    set_field_options("city", ["Mumbai","Pune"])
  } else if(frm.doc.state == "") {
    set_field_options("city", ["","Bangalore","Mysore","Mumbai","Pune"])
  }
});
  

```

[Screenshot on the live page: Opening Account]



Here’s an example of a custom script that filters options in a Select field within a child table:

```
frappe.ui.form.on('Parent DocType', {
    refresh: function (frm) {
        // Trigger this function when the form is refreshed or reloaded
        frm.fields_dict['child_table_fieldname'].grid.get_field('select_fieldname').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Some Field', '=', 'Some Value'] // Replace with your filter criteria
                ]
            };
        };
    }
});
```

### Example Scenario

Suppose you have a parent DocType called **Sales Order** with a child table field called **items**. The child table has a Select field named **itemcode**, and you want to filter the options to show only items from a specific category.

Here’s how your script might look:

```
frappe.ui.form.on('Sales Order', {
    refresh: function (frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Item Group', '=', 'Specific Category'] // Adjust the filter criteria as needed
                ]
            };
        };
    }
});
  

```

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



[Screenshot on the live page: Finance Book list with Statutory Reporting and Management Reporting]

## Set the company default

Open the Company record and select the **Accounts** tab. Set **Default Finance Book** to the book that represents normal accounting for that company, then save.



[Screenshot on the live page: Default Finance Book on the Company record]

The default is important because the current [Journal Entry](https://docs.frappe.io/erpnext/journal-entry) Finance Book field is read-only. ERPNext carries the company's default book into new Journal Entries instead of asking users to choose it manually each time.

Do not change the default casually after transactions exist. Review the effect on reports and future entries with your accountant first.

## Record an entry in a Finance Book

Create the transaction using the normal workflow. In a Journal Entry, open **More Info** and review the **Finance Book** value before submission.



[Screenshot on the live page: Finance Book carried into a submitted Journal Entry]

The example posts a $450 maintenance adjustment to **Statutory Reporting**:


| Account                     | Debit | Credit | Finance Book effect            |
| --------------------------- | -----: | ------: | ------------------------------ |
| Office Maintenance Expenses | $450  |        | Appears in the statutory book. |
| Nova Operating Bank         |       | $450   | Appears in the statutory book. |


An entry with a specific Finance Book belongs to that book. An entry whose Finance Book is blank is treated as common and is included in Finance Book report views. This preserves the original ERPNext behavior for transactions that apply to every reporting basis.

## Review reports by Finance Book

Open the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), [Trial Balance](https://docs.frappe.io/erpnext/trial-balance), [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet), or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement). Select the company, dates, and Finance Book, then refresh the report.



[Screenshot on the live page: General Ledger filtered by Statutory Reporting Finance Book]

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

[Screenshot on the live page: Financial Report Template list on the Nova develop demo site]

## Create the template

[Screenshot on the live page: Standard Cash Flow Statement Financial Report Template opened on the Nova Industries demo site]



1. Enter a descriptive Template Name and select the Report Type.
2. Add rows to the Report Line Items table in the order they should appear.
3. Select the Data Source for each row.
4. Give calculated or reusable rows a unique Line Reference.
5. Configure formatting, visibility, sign, and chart options.
6. Save, run the associated report, and reconcile the output with standard financial statements.

## Choose a row data source

[Screenshot on the live page: Report Line Items in the Standard Cash Flow Statement template]




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

[Screenshot on the live page: Cash Flow report for Nova Industries rendered with the Cash Flow Statement IFRS Financial Report Template]

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

[Screenshot on the live page: Fiscal Year start and end dates highlighted]



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

[Screenshot on the live page: Fiscal Year dates and company]

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
