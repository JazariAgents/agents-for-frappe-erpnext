<!-- Frappe documentation: erpnext, part 2 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__accounting-introduction.md -->
---
title: "Accounting Introduction | ERPNext Documentation"
description: "Understand ERPNext Accounting features, ledgers, invoices, payments, taxes, banking, inventory accounting, controls, closing, and financial reports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-introduction"
updated: "2026-08-14"
---

Accounting in ERPNext turns everyday business activity into a reliable financial record. A sale, purchase, stock movement, expense, or payment begins as an operational document and becomes balanced ledger entries when it is submitted.



At Nova Industries, an electronics manufacturer and distributor, the finance team needs to answer simple questions: Are customers paying on time? What do we owe suppliers? Is the business profitable, and does the bank balance agree with the books? ERPNext connects those questions to the transactions that created each amount.



This guide introduces the accounting features, explains how transactions reach the ledger, and shows which workflow fits different kinds of businesses. You can start with the basic sales and purchase cycles, then move into reconciliation, taxes, dimensions, budgets, and financial reporting as your needs grow.

## The accounting model

Each Company has a base currency, fiscal year, default accounts, and its own [Chart of Accounts](/erpnext/chart-of-accounts). The chart groups accounts under Assets, Liabilities, Equity, Income, and Expenses. Ledger accounts hold postings; group accounts organize them for reporting.



ERPNext uses double-entry accounting. Every accounting transaction has equal debit and credit totals, so the books remain balanced. You do not normally create those entries by hand. Submitting a transaction generates them from the document's values and accounting configuration.

Three records are especially useful when tracing a number:


| Record                   | What it tells you                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Source document**      | The business event, amounts, parties, taxes, dates, and references entered by a user                          |
| **GL Entry**             | The debit or credit posted to an account, with its company, party, cost center, project, and other dimensions |
| **Payment Ledger Entry** | How receivables, payables, advances, and payments are linked and allocated                                    |


If stock accounting is enabled, inventory transactions also create Stock Ledger Entries. Stock quantities and values are therefore traceable separately from, but connected to, the General Ledger. Read [How Transactions Affect the Ledger](/erpnext/how-transactions-affect-the-ledger) for posting examples.

## What the Accounting module covers

### Company books and account structure

ERPNext creates a separate set of books for every Company. You can use the standard chart supplied for the selected country, edit it, or use the [Chart of Accounts Importer](/erpnext/chart-of-accounts-importer) during implementation.



Company defaults determine common posting accounts such as receivables, payables, income, expenses, round-off, exchange gain or loss, and retained earnings. [Accounts Settings](/erpnext/accounts-settings) contains controls that apply across transactions, including frozen dates and rules for editing accounting entries.



Use [Finance Books](/erpnext/finance-book) when the same company needs parallel asset depreciation or reporting bases. Use multiple companies and consolidated reports when legal entities must keep independent ledgers but management needs a combined view.

### Sales, purchases, and outstanding amounts

A [Sales Invoice](/erpnext/sales-invoice) records income, tax, and the amount a Customer owes. A [Purchase Invoice](/erpnext/purchase-invoice) records expense or asset value, tax, and the amount owed to a Supplier. Credit Notes and Debit Notes reverse or reduce the effect of invoices while preserving an audit trail.



ERPNext tracks receivables and payables by party, invoice, due date, and payment term. Accounts Receivable and Accounts Payable reports provide ageing and outstanding analysis. Payment terms can divide one invoice into scheduled instalments.



For collection workflows, Payment Requests can share a request or payment link with a Customer. Dunning helps follow up overdue receivables. Supplier payments can be organized with Payment Orders where that approval process is required.

### Payments, advances, and reconciliation

A [Payment Entry](/erpnext/payment-entry) records money received, money paid, or an internal transfer between cash and bank accounts. It can allocate one payment across several invoices, accept a partial payment, record an advance against an order, or retain an excess amount as unallocated credit.



Use [Payment Reconciliation](/erpnext/payment-reconciliation) to match existing unallocated payments, advances, credit notes, and journal entries with invoices. This changes allocation and outstanding balances without creating a second cash movement.



For bank operations, ERPNext stores Bank Accounts and Bank Transactions, imports statement data, and provides a [Bank Reconciliation](/erpnext/bank-reconciliation) tool. Reconciliation matches statement lines with vouchers, creates missing payments where appropriate, and records clearance dates.

### Taxes and regional compliance

Tax templates add sales and purchase taxes to transactions. Tax Categories and Tax Rules can choose the correct template from factors such as party, address, Item, or transaction. Item Tax Templates support different rates for particular products. Tax withholding supports deductions made when paying eligible Suppliers.



Tax reports and statutory behavior vary by country. ERPNext provides the accounting framework, while regional features may come from the selected country configuration or a localization app. Complete [tax setup](/erpnext/setting-up-taxes) before posting live invoices.

### Inventory and cost of goods sold

With perpetual inventory, stock receipts and issues affect both the Stock Ledger and the General Ledger. Purchase Receipts can move value into stock received but not billed. Delivery Notes reduce inventory and recognize cost of goods sold. Stock Entries record transfers, manufacture, repacking, and adjustments.



A Sales Invoice or Purchase Invoice can also update stock when the **Update Stock** option is enabled. This supports a shorter workflow, but it combines billing and stock movement in one document. Choose the workflow deliberately before users begin posting transactions.

### Assets, expenses, and deferred accounting

The Assets module integrates with Accounting for capitalization, depreciation, transfers, disposal, and value adjustments. Depreciation schedules can post entries automatically.



Expense Claims record employee expenses and liabilities. Deferred revenue and deferred expense settings spread eligible invoice amounts across future accounting periods instead of recognizing the full amount on the invoice date.



Subscriptions and recurring documents can automate regular billing. Projects and Timesheets support service billing, cost collection, and profitability analysis.

### Cost control and management reporting

[Cost Centers](/erpnext/cost-center) identify where income and expense belong. Projects track work-specific revenue and cost. Configurable [Accounting Dimensions](/erpnext/accounting-dimensions) add reporting segments such as branch, department, channel, or business unit without expanding the Chart of Accounts.



Budgets can be set by account, cost center, project, or accounting dimension. ERPNext can warn or stop users when an applicable annual or monthly budget is exceeded. Budget Variance reports compare planned and actual values.

### Currencies and intercompany accounting

Companies, parties, bank accounts, and ledger accounts can use different currencies. ERPNext stores transaction currency and company currency values, applies exchange rates, and books realized exchange differences during settlement. Exchange Rate Revaluation handles eligible open foreign-currency balances at a reporting date.



Inter Company Journal Entries and linked sales and purchase invoices help record transactions between entities. Each company still receives its own balanced entries.

### Closing, controls, and auditability

A [Journal Entry](/erpnext/journal-entry) handles adjustments such as accruals, provisions, transfers, write-offs, and corrections that do not belong in a specialized document.



At period end, accountants review reconciliations, depreciation, stock valuation, tax, and adjusting entries. A Period Closing Voucher transfers the period's profit or loss to the selected closing account. An [Accounting Period](/erpnext/accounting-period) can prevent selected transaction types from being posted, amended, or cancelled in a closed period. Frozen-date controls provide another way to restrict backdated accounting.



Submitted documents retain their audit trail. Instead of editing a finalized transaction in place, users cancel and amend it when permissions and period controls allow. ERPNext's immutable-ledger approach creates reversal entries for cancellation rather than deleting the original ledger history.

### Reports and financial statements

The [Accounting Reports](/erpnext/accounting-reports) workspace includes:

- General Ledger and Trial Balance for account-level verification
- Balance Sheet, Profit and Loss Statement, and Cash Flow
- Accounts Receivable and Accounts Payable with ageing
- Sales and Purchase Registers
- Bank reconciliation and payment reports
- Tax, budget, cost center, project, and dimension-based reports
- Consolidated statements and multi-currency display options where supported

Reports read submitted ledger data. A draft document does not affect the books, and cancelling a submitted transaction reverses its accounting effect.

## A practical way to learn the module

Start with [Understanding Debit and Credit](/erpnext/understand-debit-and-credit), then follow one complete business cycle. Create an invoice, submit it, open its **Accounting Ledger**, record a payment, and review the General Ledger and Accounts Receivable or Payable report.

Before a production rollout:

1. Finalize Companies, fiscal years, currency, and the Chart of Accounts.
2. Configure default accounts, taxes, payment terms, cost centers, and dimensions.
3. Decide which sales, purchase, stock, and service workflows users will follow.
4. Import opening balances and outstanding invoices using the appropriate migration tools.
5. Test representative transactions and reconcile their ledger effect.
6. Set roles, approval controls, frozen dates, and period-closing responsibilities.

See [Accounting Workflows by Business Type](/erpnext/accounting-workflows-by-business-type) to choose a starting workflow.

## Related topics

- [Chart of Accounts](/erpnext/chart-of-accounts)
- [How Transactions Affect the Ledger](/erpnext/how-transactions-affect-the-ledger)
- [Understanding Debit and Credit](/erpnext/understand-debit-and-credit)
- [Accounting Reports](/erpnext/accounting-reports)
- [Opening and Closing](/erpnext/opening-and-closing)
- [Accounting Workflows by Business Type](/erpnext/accounting-workflows-by-business-type)

<!-- page: erpnext/erpnext__accounting-migration-overview.md -->
---
title: "Accounting Migration Overview | ERPNext Documentation"
description: "Plan and complete an ERPNext accounting migration using a clear cutover scope, clean source data, the correct import tools, reconciliation, and finance approval."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-migration-overview"
updated: "2026-08-15"
---

An accounting migration is not a project to recreate every screen and transaction from the old system. It is a controlled handover: choose a cut-off date, bring across the information needed to continue operations, prove that the opening position is correct, and start new transactions in ERPNext.



Nova Industries has seven years of invoices in its previous system, but only current masters, open invoices, unallocated payments, stock, assets, bank balances, and verified ledger balances are needed to begin. The old system can remain available for historical reporting until those records are no longer operationally useful.



This guide gives an opinionated migration sequence: decide the scope, export, clean and map the data, import masters, load opening transactions and balances, then validate and correct the result before users begin normal posting.

## The migration process

Do at least one test migration before the final cutover. A migration is complete only after the results have been validated and the finance owner has approved them.

## 1. Choose what you will migrate

Start by choosing a cutover date. A financial-year boundary is convenient, but a month-end can also work if waiting is impractical. Close and reconcile your old system through the day before this date. Enter every new transaction in ERPNext from the cutover date onward.

For most companies, the best scope is:

- active Customers, Suppliers, Items, Warehouses, Accounts, Cost Centers, tax templates, and other masters needed after cutover;
- unpaid customer and supplier invoices;
- unallocated payments and advances;
- bank and cash balances;
- stock quantities and values by Item and Warehouse;
- fixed assets with their accumulated depreciation;
- other asset, liability, and equity balances;
- year-to-date income and expense balances only when you are starting during a financial year and need current-year reporting in ERPNext.

Leave closed invoices, settled payments, old quotations, completed orders, and detailed journal history in the old system unless there is a legal or operational reason to move them.

Before deciding, ask a practical question: **Will someone need this record to complete work in ERPNext after cutover?** If the answer is no, preserve it in the old system or as a secure export instead of importing it.

## 2. Export and preserve the source data

Complete the normal month-end or year-end checks in your existing system before extracting data. Once the final export starts, stop users from changing transactions dated before the cutover.

Keep these source reports:


| Source report                                | Why you need it                                                                    |
| -------------------------------------------- | ---------------------------------------------------------------------------------- |
| Trial Balance                                | Proves that the opening general ledger in ERPNext agrees with the old system.      |
| Balance Sheet and Profit and Loss Statement  | Confirms financial-statement totals and account classifications.                   |
| Customer ageing by invoice                   | Provides each unpaid customer invoice, due date, currency, and outstanding amount. |
| Supplier ageing by invoice                   | Provides each unpaid supplier invoice and outstanding amount.                      |
| Bank reconciliation and statements           | Confirms the bank ledger, statement balance, and uncleared transactions.           |
| Stock report by Item and Warehouse           | Provides the opening quantity and value of inventory.                              |
| Fixed Asset register                         | Provides asset cost, date, accumulated depreciation, and remaining life.           |
| Advances and unallocated payments            | Identifies money received or paid that is not allocated to an invoice.             |
| Tax, loan, accrual, and prepayment schedules | Explains balances that cannot be understood from the Trial Balance alone.          |


Save the final reports as protected spreadsheets or PDFs. Record the exact export time, cutover date, company, currency, and filters used. These files are your migration evidence and your fallback when a total does not agree.

## 3. Clean and map the data

Cleaning and mapping means transforming data exported from your current system into the format ERPNext can import.

Do not edit your only source export. Keep it unchanged, then create a working copy. In the working copy:

1. Remove inactive records that you have decided not to migrate.
2. Remove duplicate Customers, Suppliers, Items, and Accounts.
3. Standardize names, dates, country codes, currencies, units of measure, and tax identifiers.
4. Decide the ERPNext name or code for each legacy record.
5. Map every legacy account to an ERPNext Account.
6. Map Customers, Suppliers, Items, Warehouses, Cost Centers, and currencies to their ERPNext names.
7. Separate outstanding invoices, advances, stock, assets, bank balances, and remaining general-ledger balances because they use different import methods.
8. Compare the cleaned totals with the unchanged source reports.

Create a simple mapping workbook with columns such as `Legacy Type`, `Legacy ID`, `Legacy Name`, `ERPNext Type`, `ERPNext Name`, `Action`, and `Notes`. Use `Action` values such as **Import**, **Merge**, **Rename**, and **Do not migrate**. This gives the migration team one approved answer when a legacy name does not match ERPNext.

## 4. Configure ERPNext before importing

Create the Company and confirm its country, default currency, fiscal year, and accounting defaults. Set up the Chart of Accounts, Cost Centers, Warehouses, units of measure, tax accounts, and naming rules before importing dependent records.

Import masters in dependency order. A practical sequence is:

1. Chart of Accounts and Cost Centers
2. Warehouses and units of measure
3. Item Groups, Customer Groups, Supplier Groups, and Territories
4. Customers and Suppliers
5. Items and Item Prices
6. Bank Accounts, Modes of Payment, tax templates, and remaining masters

Test a few records first. Open them in ERPNext and confirm that links, defaults, addresses, currencies, and accounts are correct before importing the complete file.

## 5. Use the right ERPNext import tool

ERPNext provides different tools because not every opening record should be imported in the same way.


| Tool                                                                                          | Use it for                                                                                                                                               |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Data Import](https://docs.frappe.io/erpnext/data-import)                                     | Import Customers, Suppliers, Items, Warehouses, Cost Centers, and other master records from CSV or Excel templates. It can also update existing records. |
| [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer)       | Import your own account hierarchy before transactions exist for the Company.                                                                             |
| [Opening Invoice Creation Tool](https://docs.frappe.io/erpnext/opening-invoice-creation-tool) | Create outstanding Sales Invoices and Purchase Invoices without recreating their full item history.                                                      |
| [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)                 | Bring in the remaining opening ledger balances through opening entries.                                                                                  |
| [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation)                   | Set opening stock quantities and values by Item and Warehouse.                                                                                           |
| [Asset](https://docs.frappe.io/erpnext/asset)                                                 | Create existing fixed assets with their opening cost and depreciation information.                                                                       |


Use small batches and retain every import file. Give each file a clear sequence number so you can tell which version was tested, corrected, and finally imported.

### Avoid double counting

Opening invoices, stock, assets, and opening payments can create accounting entries. Do not import the same value again in the final opening Journal Entry.

For example, suppose your legacy Trial Balance contains:

- $10,000 in Accounts Receivable from unpaid customer invoices;
- a $2,000 unallocated customer receipt;
- a net Accounts Receivable balance of $8,000.

Create the $10,000 outstanding invoices with the Opening Invoice Creation Tool and bring in the $2,000 receipt using the approved opening-payment method. Do not add another $8,000 Accounts Receivable line to the opening Journal Entry. That would count the balance twice.

After all specialized opening documents are created, use an opening Journal Entry only for balances that have not already been produced by another document. The Temporary Opening account should be zero when the migration is complete.

## 6. Validate and correct

Do not judge the migration by the number of successful imports. Judge it by whether ERPNext agrees with the approved source reports.

Validate in this order:

1. Compare the number of imported masters and outstanding invoices.
2. Compare customer and supplier ageing invoice by invoice.
3. Compare bank, cash, stock, fixed assets, advances, tax balances, loans, and other schedules.
4. Run the ERPNext Trial Balance for the cutover date and compare every account with the source Trial Balance.
5. Compare the Balance Sheet and Profit and Loss Statement.
6. Confirm that Temporary Opening and migration-clearing accounts have no unexplained balance.
7. Test normal work, including creating an invoice, receiving a payment, delivering stock, paying a supplier, and running reports.

If a total does not agree, do not post an unexplained Journal Entry to force the Trial Balance to match. Find the source of the difference. Typical causes are duplicate imports, an incorrect account mapping, a missing invoice, reversed debit and credit values, the wrong currency or exchange rate, or importing a control-account balance after its supporting invoices were already created.

Correct the mapping or import file, cancel or reverse the incorrect migration record using the normal ERPNext controls, import the corrected data, and validate again. Keep a correction log that records the issue, cause, action, owner, and evidence.

## 7. Approve the migration and go live

Before go-live, obtain written approval from the finance owner that:

- the Trial Balance and financial statements agree;
- receivables and payables agree with invoice-level schedules;
- bank, stock, asset, tax, and other control balances agree;
- operational tests have passed;
- correction items are resolved or formally accepted;
- the old system exports and backups are stored securely;
- users know the final cutover time and where new transactions must be entered.

After approval, stop changing migration records except through a controlled correction process. Keep the old system read-only for historical reports. ERPNext is now the source of truth for transactions dated on or after the cutover.

## Related topics

- [Data Import](https://docs.frappe.io/erpnext/data-import)
- [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer)
- [Opening Invoice Creation Tool](https://docs.frappe.io/erpnext/opening-invoice-creation-tool)
- [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)
- [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation)
- [Trial Balance](https://docs.frappe.io/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__accounting-of-inventory-stock.md -->
---
title: "Accounting Of Inventory Stock"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-of-inventory-stock"
updated: "2026-02-27"
---

The value of available inventory is treated as a Current Asset in the company's [Chart of Accounts](/erpnext/chart-of-accounts). To prepare a Balance Sheet, you should make the accounting entries for those assets. There are generally two different methods of  
accounting for inventory.

## Auto/Perpetual Inventory

**Note**: The user must define an inventory account (with Account Type set as Stock) either in the warehouse, the group warehouse, or at the company level (as the Default Inventory Account). If the user hasn't set an account in the warehouse or company, but an inventory account exists, the system will use that account to post GL entries against the respective warehouse.

In this process, for each stock transaction, the system posts relevant  
accounting entries to sync stock balance and accounting balance. This is the  
default setting in ERPNext for new accounts. By default, Perpetual Inventory is enabled in the [Company](/erpnext/company-setup#23-stock-settings).

When you buy and receive items, those items are booked as the company’s assets  
(stock-in-hand). When you sell and deliver those items, an  
expense (Cost of Goods Sold) equal to the landed cost of the items is booked.  
General Ledger entries are created after every stock transaction. As a result,  
the value as per Stock Ledger always remains the same with the relevant account  
balance. This improves the accuracy of the Balance Sheet and the Profit and Loss  
statement.

Read [Perpetual Inventory documentation](/erpnext/perpetual-inventory)  
to check accounting entries for a particular stock transaction.

### Advantages of Perpetual Inventory

Perpetual Inventory system will make it easier for you to maintain the accuracy of the company's asset and expense values. Stock balances will always be synced with relevant account balances, so no more periodic manual entry needs to be done to balance them.

In case of new back-dated stock transactions or cancellation/amendment of an existing transaction, all the future Stock Ledger entries and GL Entries will  
be recalculated for all items of that transaction. The same is applicable if  
any cost is added to the submitted Purchase Receipt later through the Landed  
Cost Voucher.

> Note: Perpetual Inventory completely depends upon the item valuation rate.  
> Hence, you have to be more careful entering the valuation rate while making any  
> incoming stock transactions like Purchase Receipt, Material Receipt, or  
> Manufacturing/Repack.

---

## 2. Periodic Inventory

In this method, accounting entries need to be created manually in order to sync stock balance and relevant account balance. The system does not create  
accounting entries automatically for assets at the time of material purchases  
or sales.

In an accounting period, when you buy and receive items, an expense is booked  
in your accounting system. You sell and deliver some of these items.

At the end of an accounting period, the total value of items to be sold, need  
to be booked as the company’s assets, often known as stock-in-hand.

The difference between the value of the items remaining to be sold and the  
previous period’s stock-in-hand value can be positive or negative. If  
positive, this value is removed from expenses (Cost of Goods Sold) and is  
added to assets (stock-in-hand). If negative, a reverse entry  
is passed.

This complete process is called **Periodic Inventory**.

If you are an existing user using Periodic Inventory and want to use Perpetual  
Inventory, you need to follow [a few steps](/erpnext/migrate-to-perpetual-inventory) to migrate.

<!-- page: erpnext/erpnext__accounting-period.md -->
---
title: "Accounting Period"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-period"
updated: "2026-08-14"
---

Nova Industries has approved its April to June financial statements. The finance team now needs those numbers to remain stable while July transactions continue. An Accounting Period locks selected submittable document types for the finished date range, preventing a late invoice, cancellation, or amendment from changing reports that have already been reviewed.



This is a selective lock. You choose which document types are closed. It is different from a [Period Closing Voucher](/erpnext/period-closing-voucher), which transfers profit or loss, and from [freezing accounting entries](/erpnext/freeze-accounting-entries), which applies a broader date-based posting restriction.

## Before you begin

- Finish reconciliations and approved period-end adjustments.
- Confirm which document types must be blocked with the finance controller.
- Create the record only after the end date has passed. ERPNext does not allow a future end date.

## Create an Accounting Period

1. Open **Accounting Period** and create a new record.
2. Enter a descriptive name, start date, end date, and company.
3. Select an exempted role only when your policy permits controlled exceptions.
4. In **Closed Documents**, add the document types to restrict and keep **Closed** selected.
5. Save, review, and submit the record.

![Current Period Closing settings in ERPNext](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-accounts-settings-closing.png)



## Choose what to close


| Document type                      | Why teams commonly close it                                              |
| ---------------------------------- | ------------------------------------------------------------------------ |
| Sales Invoice and Purchase Invoice | Protect revenue, expense, receivable, payable, and tax balances.         |
| Journal Entry                      | Prevent unapproved backdated adjustments.                                |
| Payment Entry                      | Protect bank, cash, receivable, and payable allocations.                 |
| Stock Entry and stock transactions | Protect valuation and cost of goods sold where stock accounting applies. |


## What users experience

When a selected document is dated inside the closed range, ERPNext blocks creation, amendment, or cancellation after the Accounting Period has ended. A document type that is not listed, or whose **Closed** checkbox is cleared, remains available.

## Troubleshooting

### Users can still post one type of transaction

Open the Accounting Period and confirm that the exact DocType appears in Closed Documents with Closed selected. Also confirm that the posting date falls inside the period and the record is submitted.

### You cannot save the period

Check that the end date is not in the future, the date range is valid, the company is correct, and at least one closed document row is present.

## Frequently asked questions

### Does the exempted role bypass every restriction?

Treat exemptions as controlled finance access and test the exact transaction type. Some period-closing restrictions are intentionally strict and should not be assumed to behave like the broader frozen-accounts role.

### Should I create next month’s Accounting Period in advance?

Create it after the month ends. Use permissions and the frozen-accounts date if you need to control entries during an active month.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__accounting-reports.md -->
---
title: "Accounting Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-reports"
updated: "2026-08-14"
---

It is the end of August at Nova Industries. The sales team says the company had a strong month, but the finance manager sees less cash in the bank than expected. Customers still owe money, several supplier bills are overdue, and the team needs to explain which transactions produced the balances before deciding what to collect and what to pay.



No single report answers all of those questions. ERPNext accounting reports show the same submitted transactions from different angles. This guide helps you begin with the decision you need to make, select the right report, interpret a populated example, and move from a summary number to its source document.

## Begin with the question, not the report name


| Question                                                               | Start with                                                      | Why                                                                     |
| ---------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Which individual entries produced this account balance?                | [General Ledger](/erpnext/general-ledger)                       | It lists debit and credit postings with their source vouchers.          |
| Do debit and credit balances agree at the end of the period?           | Trial Balance                                                   | It summarizes opening, period, and closing balances account by account. |
| What does the company own and owe on a particular date?                | Balance Sheet                                                   | It presents assets, liabilities, and equity at a point in time.         |
| Did the company earn a profit during the period?                       | Profit and Loss Statement                                       | It compares income with expenses for a period.                          |
| Why did cash increase or decrease even when the company made a profit? | Cash Flow                                                       | It explains cash movement through operations, investing, and financing. |
| Which customer invoices need collection follow-up?                     | [Accounts Receivable](/erpnext/accounts-receivable-and-payable) | It shows invoice-level outstanding balances and ageing.                 |
| Which supplier invoices should be paid next?                           | Accounts Payable                                                | It shows supplier balances, due dates, and ageing.                      |
| Why is an invoice still outstanding after a payment was recorded?      | [Payment Ledger](/erpnext/payment_ledger)                       | It shows invoice and payment allocations used by outstanding reports.   |


## Follow Nova's month-end review

The finance manager does not open every report at once. She begins with the broad result, identifies the number that needs explanation, and then moves to a more detailed report.

### Check whether the books balance

Start with Trial Balance after posting the period's invoices, payments, stock transactions, and adjustments. Opening Debit and Opening Credit show the position brought into the period. Debit and Credit show activity during the selected dates. Closing Debit and Closing Credit show the resulting balance.



The total debit and credit columns should agree because every submitted accounting transaction posts equal debits and credits. Agreement proves mathematical balance, but it does not prove that every transaction used the correct account. Use the General Ledger to investigate the composition of a suspicious balance.

### Explain an account with General Ledger

For 13 July to 13 August 2026, Nova's General Ledger contains Sales Invoice, stock, tax, and bank entries. One $20,000 sale debits Debtors and credits Sales. The same invoice credits Stock In Hand by $14,500 and debits Cost of Goods Sold by $14,500. This is why one sales invoice can create more than two ledger rows.

![General Ledger showing debit and credit rows created by Nova sales invoices](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-nova-industries-general-ledger.png)

The report totals show $395,762 of debits and $395,762 of credits. That confirms balance for the selected scope. To investigate the $229,000 sale, open its Voucher No. The voucher explains the business event, while the General Ledger explains its accounting effect.



Use the General Ledger for evidence and tracing. Use Trial Balance when you need one closing balance per account. Selecting different companies, dates, Finance Books, Cost Centers, Projects, or other [Accounting Dimensions](/erpnext/accounting-dimensions) can make two otherwise similar report runs show different totals.

### Decide what to collect with Accounts Receivable

Nova's Accounts Receivable report shows $249,212 outstanding from four customers as of 13 August 2026. The entire visible amount falls in the 0 to 30 day ageing bucket. This tells the finance manager that the invoices are recent. It does not automatically mean they are overdue because due dates and payment terms must also be considered.

![Accounts Receivable showing four customer balances in the 0 to 30 day ageing bucket](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-nova-industries-accounts-receivable.png)

The next action is to review Due Date and outstanding amount for each invoice. A payment that exists but remains unallocated may require [Payment Reconciliation](/erpnext/payment-reconciliation). An overdue customer may require a statement through [Process Statement of Accounts](/erpnext/process-statement-of-accounts) or a [Dunning](/erpnext/dunning) record.



Accounts Receivable is better than General Ledger for collection work because it keeps the invoice, payment allocation, due date, and ageing together. General Ledger remains the better report when the amount itself needs accounting investigation.

### Plan supplier payments with Accounts Payable

Nova's Accounts Payable report shows $184,293 outstanding to Summit Traders Ltd., Zuckerman Security Ltd., and MA Inc. in the 121 days and above bucket. Unlike the recent receivables, these balances are old and require immediate review.

![Accounts Payable showing three supplier balances aged more than 121 days](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-nova-industries-accounts-payable.png)

The finance manager should verify whether the invoices are genuinely unpaid, disputed, or already covered by an unallocated payment. After confirming the balances, she can create a [Payment Entry](/erpnext/payment-entry) for routine settlement or use a [Payment Order](/erpnext/payment-order) when several approved supplier payments need coordinated processing.

### Understand why profit and cash differ

Nova's Cash Flow report shows Profit for the year of $109,440, but Net Cash from Operations is negative $117,866. The largest visible reason is the $316,212 increase in Accounts Receivable. Revenue contributed to profit, but much of the cash has not yet been collected. The $184,293 increase in Accounts Payable offsets part of that pressure because Nova has not yet paid those suppliers.

![Cash Flow showing profit of 109440 dollars and negative operating cash flow of 117866 dollars](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-nova-industries-cash-flow-report.png)

This is the decision the reports enable: profit is positive, but collection must improve before Nova commits to additional cash spending. Profit and Loss explains whether the business earned money. Cash Flow explains why the bank position moved differently.

## Understand the core financial statements


| Statement                 | Period or date                                       | What to read                                                           | What it does not explain alone              |
| ------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------- |
| Trial Balance             | A reporting period with opening and closing balances | Whether debit and credit totals agree and which accounts hold balances | Business meaning of each transaction        |
| Balance Sheet             | A point in time                                      | Assets, liabilities, equity, liquidity, and capital structure          | How profit was earned during the period     |
| Profit and Loss Statement | A period                                             | Income, cost of sales, operating expenses, and profit                  | Whether income has been collected in cash   |
| Cash Flow                 | A period                                             | Cash movement from operations, investing, and financing                | Invoice-level collection or payment details |


## Apply filters consistently


| Filter                                     | Why it matters                                                                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Company                                    | Restricts the report to one legal entity. Use Consolidated Financial Statements for a group view.                    |
| Reporting dates or fiscal year             | Changes the activity and balances included in the result.                                                            |
| Finance Book                               | Includes entries belonging to the selected accounting book and can explain apparent differences between report runs. |
| Cost Center, Project, or another dimension | Shows only the selected operational slice rather than the whole company.                                             |
| Presentation currency                      | Changes displayed amounts without changing the underlying ledger entries.                                            |
| Include or exclude period-closing entries  | Changes whether closed income and expense balances are included in the view.                                         |


When two reports appear not to agree, first match Company, dates, Finance Book, dimensions, currency, and period-closing options. Then check whether one report shows activity during a period while the other shows a balance as of a date.

## Other useful accounting reports


| Decision                                                           | Report                                                    |
| ------------------------------------------------------------------ | --------------------------------------------------------- |
| Compare actual expenses with approved limits                       | [Budget Variance Report](/erpnext/budget-variance-report) |
| Review invoiced sales, purchases, and tax columns                  | Sales Register or Purchase Register                       |
| Review sales or purchase movement by item and period               | Item-wise register or invoice trend report                |
| Find ordered, delivered, or received items that still need billing | To Bill reports                                           |
| Compare several companies under one group                          | Consolidated Financial Statements                         |


## Troubleshooting

### Trial Balance and General Ledger appear different

Run both reports with the same Company, dates, Finance Book, dimensions, and period-closing treatment. Trial Balance separates opening, period, and closing values, while General Ledger lists individual postings. Previous fiscal years that have not been closed can also affect how income and expense balances appear.

### A financial statement is empty

Confirm that submitted transactions exist inside the selected company and period. Remove optional Finance Book and dimension filters one at a time, refresh the report, and verify that the underlying accounts use the correct root and report types.

### A report contains the right total but the wrong account

A balanced total cannot detect incorrect account selection. Open the amount in General Ledger, inspect the source voucher, and correct it through the supported cancellation and amendment or adjustment workflow.

### The report remains in a loading state

Reduce an unusually large period or filter scope and run it again. For large datasets, use the report's prepared-report option when available and wait for completion before interpreting or exporting it.

## Frequently asked questions

### Why can a profitable company have negative cash flow?

Profit records income and expenses when they are recognized. Cash Flow records when cash actually moves. Credit sales can increase profit before customers pay, while unpaid supplier bills can delay cash outflow.

### Which report should an auditor receive?

The exact package depends on the engagement. A common starting set includes Trial Balance, General Ledger, Balance Sheet, Profit and Loss Statement, Cash Flow, Accounts Receivable, Accounts Payable, and the source vouchers supporting material balances.

### Do filters change accounting entries?

Report filters change which entries are selected and how they are presented. They do not modify submitted ledger entries.

### Can I export a report before reviewing it?

ERPNext can export many reports, but first verify the Company, dates, currency, dimensions, grouping, and totals in the application. An export preserves a mistaken filter choice just as accurately as a correct one.

## Related topics

- [General Ledger](/erpnext/general-ledger)
- [Payment Ledger](/erpnext/payment_ledger)
- [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable)
- [Financial Report Template](/erpnext/financial-report-template)
- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [Finance Book](/erpnext/finance-book)
