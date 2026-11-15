<!-- Frappe documentation: erpnext, part 11 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__book-discount-allowed-and-received-separately.md -->
---
title: "Book Discounts Allowed and Received Separately | ERPNext Documentation"
description: "Book discounts allowed and received in separate ERPNext accounts using negative charge rows, then verify invoice totals, ledgers, and net payments clearly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/book-discount-allowed-and-received-separately"
updated: "2026-08-03"
---

ERPNext normally records the net value of an invoice after commercial discounts. Use the workflow on this page when your accounting policy requires the discount to appear in a separate ledger account.

A **discount allowed** is a reduction that your Company gives a Customer. It is commonly recorded in an expense or contra-revenue account. A **discount received** is a reduction that a Supplier gives your Company. It is commonly recorded in an income or contra-expense account. Confirm the account classification with your accountant because presentation and tax rules vary by jurisdiction.

This page uses a negative row in the Sales or Purchase Taxes and Charges table. Despite the table name, ERPNext uses it for taxes and other additions or deductions. The negative row reduces the amount payable while posting the discount to the selected Account Head.


| Example          | Gross amount | Separate discount                             | Net amount due       |
| ---------------- | ------------: | ---------------------------------------------: | --------------------: |
| Sales Invoice    | $1,398.00    | $139.80 debit to Sales Discounts Allowed      | $1,258.20 receivable |
| Purchase Invoice | $1,040.00    | $104.00 credit to Purchase Discounts Received | $936.00 payable      |


## Choose the appropriate discount method

Use this negative-charge workflow when you need explicit control over the separate account, especially for Purchase Invoices. ERPNext's newer [Discount Accounting](/erpnext/discount-accounting) workflow provides dedicated sales-side Discount Account fields and can be more convenient for item and invoice-level sales discounts.

Do not use both methods on the same discount. A normal item discount, an [additional discount](/erpnext/applying-discount), a Pricing Rule, and a negative charge row can all reduce the transaction. Combining them without an intentional calculation can double-count the reduction.

This workflow records a transaction-wide discount. It does not allocate a different discount to each item row for margin analysis. If item-level commercial pricing matters, set an intentional [Item Price](/erpnext/item-price) or item discount and decide separately whether the ledger also needs a distinct discount account.

## Before you begin

1. Confirm with your accountant whether discount allowed belongs under Expense or contra-revenue, and whether discount received belongs under Income or contra-expense.
2. Create non-group ledgers in the Company's [Chart of Accounts](/erpnext/chart-of-accounts). The example uses **Sales Discounts Allowed - NET** and **Purchase Discounts Received - NET**.
3. Confirm the discount basis. **On Net Total** applies the rate to the complete Net Total. Other charge types can calculate against a prior row or a fixed amount.
4. Confirm how the discount affects tax. The order and type of rows in the charge table determine the running total used by later taxes.
5. Test a representative transaction and review its ledger before using the method in production.

The sales discount account appears under Expenses in this example.



![Sales Discounts Allowed account highlighted in the Chart of Accounts](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-account.png)

The purchase discount account appears under Income.



![Purchase Discounts Received account highlighted in the Chart of Accounts](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-discount-account.png)

## Book a discount allowed on a Sales Invoice

1. Create a [Sales Invoice](/erpnext/sales-invoice) and add the Items at their gross selling rates.
2. In **Sales Taxes and Charges**, add a row. A reusable [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template) can provide the same row when this treatment is standard.
3. Select the highlighted pencil icon to open the complete row editor.

![Sales Invoice discount row with the pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-row.png)

4. Set **Type** to **On Net Total**.
5. Set **Account Head** to the discount-allowed account.
6. Enter the discount percentage as a negative **Tax Rate**. For a 10% discount, enter **-10**.
7. Enter a clear Description and the required Cost Center or other [Accounting Dimensions](/erpnext/accounting-dimensions).

![Sales discount Type, Account Head, and negative Tax Rate highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-fields.png)

The example starts with two phones at $699 each, or $1,398. A -10% row produces -$139.80, reducing the Grand Total to $1,258.20.



![Submitted Sales Invoice with the discount and Grand Total highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-submitted-total.png)

8. Review taxes, rounding, Grand Total, and the charge row, then submit.
9. Open **View &gt; Accounting Ledger** and verify the result in the [General Ledger](/erpnext/general-ledger).

![Sales Invoice ledger with the separate discount row highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-general-ledger.png)

The ledger debits Debtors by $1,258.20, debits Sales Discounts Allowed by $139.80, and credits Sales by the gross $1,398.00.

## Book a discount received on a Purchase Invoice

1. Create a [Purchase Invoice](/erpnext/purchase-invoice) and add the Items at their gross purchase rates.
2. In **Purchase Taxes and Charges**, add a row. Use a [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) when the same treatment is reusable.
3. Select the pencil icon on the row.
4. Set **Type** to **On Net Total**.
5. Set **Account Head** to the discount-received income or contra-expense account approved by your accountant.
6. Enter the percentage as a negative **Tax Rate**. The example uses **-10**.

![Purchase discount Type, Account Head, and negative Tax Rate highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-discount-fields.png)

The gross purchase is $1,040. The -10% row deducts $104, so the Supplier is owed $936.



![Submitted Purchase Invoice with the discount and Grand Total highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-submitted-total.png)

7. Submit and open the Accounting Ledger.

![Purchase Invoice ledger with the separate discount row highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-general-ledger.png)

The ledger credits Creditors by $936, debits the purchase or stock-received account by $1,040, and credits Purchase Discounts Received by $104.

If a [Purchase Receipt](/erpnext/purchase-receipt) was already posted at a different amount, do not assume the Purchase Invoice discount will correct stock valuation or clear Stock Received But Not Billed automatically. Apply the commercial treatment consistently across the purchase cycle and verify both stock and accounting ledgers.

## Record the net payment

Create a [Payment Entry](/erpnext/payment-entry) for the invoice's final outstanding amount, not its gross amount before discount.

For the sales example, the Customer pays $1,258.20. The Payment References row allocates that amount to the Sales Invoice.



![Customer Payment Entry allocating the net Sales Invoice amount](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-payment-entry.png)

For the purchase example, the Company pays $936 to the Supplier.



![Supplier Payment Entry allocating the net Purchase Invoice amount](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-payment-entry.png)

The discount was already posted by the invoice. Do not add the same discount again as a deduction in Payment Entry unless a separate payment-time adjustment genuinely occurred.

## Important fields and what they mean


| Field                      | What it controls                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| Type                       | Calculation basis for the row. On Net Total applies the percentage to the invoice Net Total. |
| Account Head               | Ledger that receives the discount posting. It must belong to the selected Company.           |
| Tax Rate                   | Percentage used by the row. Enter a negative value to deduct the discount.                   |
| Amount                     | Calculated or entered deduction. Review its sign and value before submission.                |
| Description                | Text shown on the invoice and useful for reviewers. It does not determine the ledger.        |
| Cost Center and dimensions | Reporting segments applied to the discount posting.                                          |
| Grand Total                | Net amount due after all charge, tax, discount, and rounding rows.                           |
| Payment References         | Invoice allocation on the Payment Entry. Allocate the final outstanding amount.              |


## Troubleshooting


| Issue                                         | What to check                                                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The discount increases the invoice            | Confirm Tax Rate is negative. A positive charge row increases the total.                                                                                |
| The discount posts to the wrong account       | Correct Account Head while the invoice is Draft. After submission, follow the supported cancel-and-amend process.                                       |
| Tax is calculated on the wrong amount         | Review row order, Type, Row ID, and whether the next tax uses Net Total, Previous Row Amount, or Previous Row Total.                                    |
| The purchase clearing account does not settle | Compare Purchase Receipt and Purchase Invoice rates, discounts, taxes, and linked quantities. Verify stock valuation and Stock Received But Not Billed. |
| The payment does not close the invoice        | Allocate the current outstanding amount, use the correct Party and receivable or payable account, and confirm the Payment Entry is submitted.           |


## Frequently asked questions

### Should Discount Allowed always be an expense account?

Not always. Some accounting policies classify it as a contra-revenue account. ERPNext posts to the Account Head you select, so your accountant should determine the correct classification.

### Why is the discount entered in a taxes table?

ERPNext uses the table for taxes and other additions or deductions. A negative row reduces the running total and posts to its Account Head.

### Can I enter a fixed discount instead of a percentage?

Yes, use an appropriate fixed-amount charge type and enter a negative amount. Confirm how later tax rows use the running total.

### Can I reuse the same discount row?

Yes, create a sales or purchase taxes-and-charges template when the account, basis, description, and rate are standard. Review the fetched row on every transaction.

### Does a purchase discount automatically update stock valuation?

Not in every purchase sequence. The outcome depends on whether stock was received separately, the accounts used, and the settings governing receipt and invoice valuation. Verify the Purchase Receipt, Purchase Invoice, stock ledger, and General Ledger together.

## Related topics

- [Discount Accounting](/erpnext/discount-accounting)
- [Applying a Discount](/erpnext/applying-discount)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__booking-customer-deducted-tds-in-payment-entry-in-erpnext.md -->
---
title: "Booking Customer Deducted TDS in Payment Entry in ERPNext | ERPNext Documentation"
description: "Record customer-withheld tax and clear the related ERPNext invoice correctly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/booking-customer-deducted-tds-in-payment-entry-in-erpnext"
updated: "2026-08-01"
---

When a Customer withholds tax from a payment, the bank receives less than the invoice value. Record the cash received, allocate the invoice, and post the withheld amount to the correct tax receivable account.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Booking Customer Deducted TDS in Payment Entry in ERPNext

1. Create a Receive Payment Entry and fetch the Sales Invoice.
2. Enter the net amount received in the bank.
3. Allocate the invoice amount being settled.
4. Add the withheld amount in **Deductions or Loss** using the approved tax receivable account.
5. Attach or reference the withholding certificate when available.
6. Confirm that the Difference Amount is zero and submit.

![Booking Customer Deducted TDS in Payment Entry in ERPNext in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-05-payment-entry-references.png)

## Important fields and what they mean


| Field            | What it controls                               |
| ---------------- | ---------------------------------------------- |
| Paid Amount      | Net cash received.                             |
| Allocated Amount | Invoice amount cleared.                        |
| Account          | Tax receivable ledger for the withheld amount. |
| Amount           | Tax withheld by the Customer.                  |
| Reference        | Certificate or remittance evidence.            |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The invoice remains partly outstanding after the customer deducts tax

The bank receipt and tax deducted must together clear the invoice. Record the withheld amount against the correct tax receivable or recoverable account instead of allocating only the cash received.

### The withholding entry credits or debits the wrong account

Review whether you are recording customer-deducted tax or supplier withholding. Customer-deducted tax is commonly a recoverable asset, while tax withheld from a supplier is commonly a liability. Confirm the local accounting treatment with your adviser.

### The deduction amount is calculated on the wrong base

Check the calculation type, rate, actual amount, partial-payment behavior, and regional tax configuration. Do not reuse a supplier withholding setup without verifying that it fits customer-deducted tax.

## Frequently asked questions

### Should the Payment Entry amount equal the invoice or the bank receipt?

Record the actual cash received in the bank amount. Use the supported deduction or tax fields so the cash plus recoverable tax clears the invoice.

### Is customer-deducted tax an expense?

It is often a recoverable tax asset, but the treatment depends on local law and whether the amount can be claimed. Use an expense account only when advised that it is not recoverable.

### Can the deduction be recorded after the Payment Entry was submitted?

Correct the transaction through cancellation and amendment or another approved accounting adjustment. Do not edit posted ledger values directly.

### Why does this differ from withholding tax on supplier payments?

In a customer receipt, your customer has withheld money from you. In a supplier payment, your company withholds money owed to the supplier and may owe it to a tax authority.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__braintree-integration.md -->
---
title: "Setting up Braintree\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/braintree-integration"
updated: "2026-02-26"
---


To setup Braintree, go to `Explore > Integrations > Braintree Settings`

## Setup Braintree

To enable Braintree in your ERPNext account, you need to configure the following parameters:

- Merchant ID
- Public Key
- Private Key

You can setup several Braintree payment gateways if needed. The choice of payment gateway account will determine which braintree account is used for the payment.

![Braintree Settings](/files/braintree_account.png)

On enabling service, the system will create Payment Gateway record and an Account head in chart of account with account type as Bank.

![Braintree COA](/files/braintree_coa.png)

It will also create a payment gateway account. You can change the default bank account if needed and create a template for the payment request.

![Payment Gateway Account](/files/payment_gateway_account_braintree.png)

After configuring the Payment Gateway Account, your system is able to accept online payments through Braintree.

## Supporting transaction currencies

```
"AED","AMD","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BIF","BMD","BND","BOB",
"BRL","BSD","BWP","BYN","BZD","CAD","CHF","CLP","CNY","COP","CRC","CVE","CZK","DJF","DKK",
"DOP","DZD","EGP","ETB","EUR","FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF","GTQ","GYD",
"HKD","HNL","HRK","HTG","HUF","IDR","ILS","INR","ISK","JMD","JPY","KES","KGS","KHR","KMF",
"KRW","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","MAD","MDL","MKD","MNT","MOP","MUR",
"MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","PAB","PEN","PGK","PHP",
"PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SEK","SGD","SHP","SLL",
"SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TOP","TRY","TTD","TWD","TZS","UAH","UGX",
"USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XOF","XPF","YER","ZAR","ZMK","ZWD"
```

<!-- page: erpnext/erpnext__brand.md -->
---
title: "Brand\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/brand"
updated: "2026-03-06"
---

**A Brand identifies items with a specific name.**

Usually, a Brand is the manufacturer or packer of a specific product. For example, Apple is a brand that manufactures laptops. A Brand is not necessarily the [Manufacturer](/erpnext/manufacturer) of an Item, it's only the name under which a product is sold. For example, if you manufacture plastic cups, you may license them to a big brand so that they sell them under their Brand.

In ERPNext, Brands can be assigned to Items for identifying and assigning certain defaults.

To access the Brand list, go to:

> Home > Selling > Sales > Brand

## 1. How to Create a Brand

1. Go to the Brand list and click on New.
2. Enter a Brand name and enter a description if needed.
3. Save.
  [Brand](/files/brand.png)

Now this Brand can be associated with different Items.

![](/files/item_brand.png)

## 2. Features

### 2.1 Setting defaults for Items of this Brand

![](/files/brand_defaults.png)

The following defaults can be set for a Brand. On assigning this brand to an Item, the set defaults will be fetched when performing Sales/Purchase transactions with Item of this Brand.

- **Default Warehouse**: The Warehouse from which the Item will be sourced/stored depending on the transaction.
- **Default Price List**: The Price List set here will be fetched in Purchase/Sales transactions.

#### Purchase Defaults

When performing Purchase transactions like Purchase Order, Purchase Receipt, or Purchase Invoice, the defaults set here will be fetched on selecting Item of this Brand.

- Default Buying Cost Center
- Default Supplier
- Default Expense Account

#### Sales Defaults

When performing Sales transactions like Sales Order, Delivery Note, or Sales Invoice, the defaults set here will be fetched on selecting Item of this Brand.

- Default Selling Cost Center
- Default Income Account

## 3. Related Topics

1. [Purchase Order](/erpnext/purchase-order)
2. [Sales Order](/erpnext/sales-order)
3. [Purchase Receipt](/erpnext/purchase-receipt)
4. [Delivery Note](/erpnext/delivery-note)
5. [Sales Invoice](/erpnext/sales-invoice)
6. [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__budget-revision.md -->
---
title: "Budget Revision"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget-revision"
updated: "2026-08-14"
---

Nova Electronics Trading approved $120,000 for marketing at the beginning of the year. Six months later, management approves another $30,000 for a new phone launch. The finance team needs to increase the plan without losing the record of what was originally approved.



Use a Budget Revision when management changes an existing approved [Budget](/erpnext/budget). ERPNext creates a connected replacement instead of asking you to overwrite the submitted plan. After you submit the revision, the earlier Budget is cancelled and retained as part of the approval history.



A revision changes the plan and its transaction controls. It does not rewrite invoices, orders, or [General Ledger](/erpnext/general-ledger) entries that have already been posted.

## Before you begin

Start with a submitted Budget. Confirm the revised amount, the reason for the change, the affected [Account](/erpnext/chart-of-accounts) or [Cost Center](/erpnext/cost-center), and the person who approved it.



Review current spending in the [Budget Variance Report](/erpnext/budget-variance-report) before changing the plan. This tells you how much has already been spent and how the proposed amount will change the remaining headroom.

## Revise a Budget

Open the submitted Budget that needs to change. From the actions menu, select **Revise Budget**.



![Submitted Budget opened in ERPNext before revision](/files/budget-scope-and-period.webp)

Confirm that you want to continue. ERPNext creates a new draft based on the existing Budget, so you do not need to enter the complete plan again.



Update the **Budget Amount** and, when required, the monthly distribution. Keep the same account, fiscal year, and reporting scope unless the approved change specifically requires them to differ.



![Budget amount and distribution settings being revised](/files/budget-amount-and-distribution.webp)

Save and submit the revised Budget.

## What changes after submission


| Record                    | Result                                         |
| ------------------------- | ---------------------------------------------- |
| Earlier Budget            | Cancelled and retained as the previous version |
| Revised Budget            | Submitted and used as the active budget        |
| Existing transactions     | Remain unchanged                               |
| Budget checks and reports | Use the revised approved amount                |


Open the revised Budget and follow its amended-from link to trace the earlier approval. Then refresh the Budget Variance Report using the same [Company](/erpnext/company), [Fiscal Year](/erpnext/fiscal-year), Account, and budgeting segment. The report should show the revised approved amount while retaining the same actual spending.

## When to revise instead of creating another Budget

Use a revision when management changes the amount or distribution of the same approved plan. Create a separate Budget when you are controlling a different Company, Fiscal Year, Account, Cost Center, [Project](/erpnext/project), or [Accounting Dimension](/erpnext/accounting-dimensions). This keeps unrelated plans from being joined into one revision history.

## Troubleshooting

### Revise Budget is not available

Confirm that the Budget is submitted and that your role can cancel and create Budget records. A draft budget can be edited directly and does not need a revision.

### The revised amount does not appear in reports

Confirm that the revised Budget was submitted, then check the company, fiscal year, Cost Center, account, and other filters used in the report.

### The earlier Budget still appears

The earlier record is retained for history. Check its status. It should be cancelled after the revised Budget is submitted.

## Frequently asked questions

### Does revising a Budget change posted invoices or journals?

A revision does not change posted invoices or journals. It changes the approved plan and the controls applied to future transactions.

### Can I reduce a Budget below the amount already spent?

You can reduce the approved amount, but first compare it with actual and committed spending. A lower Budget does not reverse existing [Purchase Invoices](/erpnext/purchase-invoice) or [Purchase Orders](/erpnext/purchase-order). It may cause later transactions to warn or stop sooner.

### Why not cancel the Budget and create a new one manually?

The revision action preserves the relationship between the earlier and replacement Budgets. It also copies the existing scope and distribution, which reduces the risk of creating a new plan against the wrong Account or Cost Center.

## Related topics

- [Budget](/erpnext/budget)
- [Budget Variance Report](/erpnext/budget-variance-report)
- [Cost Center and Budgeting](/erpnext/cost-center-and-budgeting)
- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__budget-variance-report.md -->
---
title: "Budget Variance Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget-variance-report"
updated: "2026-08-14"
---

Nova Electronics Trading approved a $120,000 marketing Budget, distributed as $10,000 per month. By the end of March, the team has spent $27,500. The finance manager needs one answer: is marketing spending ahead of plan, behind plan, or exactly where it should be?



The Budget Variance Report puts the approved [Budget](/erpnext/budget) and actual expenses beside each other. Nova can see the planned amount, the amount posted through accounting transactions, and the difference for each period. A positive or negative variance is useful only after you confirm how your organisation interprets the report's sign, so focus first on whether actual spending is above or below the budget.

## Before you begin

Create and submit a Budget against the required [Cost Center](/erpnext/cost-center), [Project](/erpnext/project), or [Accounting Dimension](/erpnext/accounting-dimensions). Actual values come from submitted transactions that post to the same [Account](/erpnext/chart-of-accounts), company, period, and reporting segment.

## Review budget performance

Open **Budget Variance Report** from Accounting. Select the Company, Fiscal Year, Budget Against, and reporting frequency. Use Monthly for operational reviews and Quarterly or Yearly for a higher-level view.

![Budget Variance Report comparing a 120,000 budget with 27,500 of actual marketing expense](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-budget-variance-report.png)

Select **Show Cumulative** when you want to compare total budget and total actual spending up to each period. This is useful when spending is seasonal and one month should not be judged in isolation.

## Read the result


| Column            | Meaning                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| Budget            | The amount approved for the period by the applicable Budget.                    |
| Actual            | Submitted expense entries posted to the matching account and reporting segment. |
| Variance          | The difference between the planned and actual amount.                           |
| Cumulative values | The running budget, actual amount, and variance through that period.            |


If actual spending looks incomplete, check the [General Ledger](/erpnext/general-ledger) for the same account, dates, and Cost Center. A [Journal Entry](/erpnext/journal-entry), [Purchase Invoice](/erpnext/purchase-invoice), or other submitted expense transaction contributes only when its dimensions match the Budget.

## Troubleshooting

### The report is empty

Confirm that a submitted Budget exists for the selected Company, Fiscal Year, account, and reporting segment. This report is budget-driven, so actual expenses alone do not create rows.

### The actual amount is lower than expected

Check whether the missing transactions use another Cost Center, Project, Account, Posting Date, or accounting dimension. Compare the report with the General Ledger using identical filters.

## Frequently asked questions

### Does the report enforce the budget?

Budget controls enforce or warn about limits. The report explains performance after transactions have been requested, committed, or posted.

### Should I use monthly or cumulative values?

Monthly values show what happened in one period. Cumulative values show whether the organisation is within its plan overall despite timing differences.

## Related topics

- [Budget](/erpnext/budget)
- [Budget Revision](/erpnext/budget-revision)
- [Cost Center and Budgeting](/erpnext/cost-center-and-budgeting)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__budget.md -->
---
title: "Budget"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget"
updated: "2026-08-14"
---

Nova Electronics Trading plans to spend $120,000 on marketing this year. The finance team wants the marketing team to work freely within that amount, but it also wants to know before a purchase pushes spending beyond the approved plan.



A Budget turns that plan into an ERPNext control. Nova can set a $120,000 limit against its Marketing [Cost Center](/erpnext/cost-center) and Advertising [Account](/erpnext/chart-of-accounts). ERPNext can warn the buyer or stop the transaction when a [Material Request](/erpnext/material-request), [Purchase Order](/erpnext/purchase-order), or posted expense exceeds the limit.



The Budget does not hold money in a bank account. It records what the company has approved, compares that plan with commitments and actual expenses, and helps managers act before overspending becomes visible at month-end.

## Before you begin

Set up the [Fiscal Year](/erpnext/fiscal-year), ledger Account, and the segment you want to control. You can create a Budget against a Cost Center, [Project](/erpnext/project), or supported [Accounting Dimension](/erpnext/accounting-dimensions).



Decide where ERPNext should intervene. Use **Warn** when the person submitting the transaction may continue after reviewing the overrun. Use **Stop** when exceeding the approved amount requires the Budget or transaction to be changed first.

## Create a Budget

Open the Budget list and select **Add Budget**.



![Budget list in ERPNext](/files/budget-list.webp)



Select **Budget Against**, then choose the Cost Center, Project, or Accounting Dimension value. Select the **Company** and ledger **Account** whose activity should be measured.



Set **From Fiscal Year** and **To Fiscal Year**. A budget can cover one fiscal year or span several fiscal years when the organisation plans a longer initiative.



![Budget scope, account, and fiscal year fields](/files/budget-scope-and-period.webp)



Enter the **Budget Amount** and choose a **Distribution Frequency**: Monthly, Quarterly, Half-Yearly, or Yearly.



Enable **Distribute Equally** when each period should receive the same share. Otherwise, adjust the generated Budget Distribution rows to reflect seasonality, campaign timing, or another planned pattern.



![Budget amount and distribution settings](/files/budget-amount-and-distribution.webp)

## Choose budget control actions

ERPNext can check the same approved amount at different stages of the buying and accounting cycle. Enable the earliest stage where your company wants control. Checking a Purchase Order helps prevent an excessive commitment before the supplier invoice arrives.


| Stage              | What ERPNext measures                          | Typical use                                    |
| ------------------ | ---------------------------------------------- | ---------------------------------------------- |
| Material Request   | Requested purchasing demand                    | Control spending before approval or ordering.  |
| Purchase Order     | Committed purchase value                       | Prevent commitments beyond an approved amount. |
| Actual expenses    | Posted accounting expense                      | Control Purchase Invoices and Journal Entries. |
| Cumulative expense | Accumulated expense over the configured period | Apply a broader running control.               |


For each enabled stage, choose an action for the annual limit and the accumulated periodic limit. The annual check protects the complete approved amount. The periodic check protects the amount planned for the current month, quarter, or other distribution period.

- **Stop** prevents submission when the limit is exceeded.
- **Warn** informs the user but allows submission.
- **Ignore** performs no warning or block for that check.



![Purchase Order and actual expense controls in a Budget](/files/budget-control-actions.webp)



Save and submit the Budget. Draft budgets do not enforce controls.

## Important fields and what they mean


| Field                             | Meaning                                                             |
| --------------------------------- | ------------------------------------------------------------------- |
| Budget Against                    | The reporting segment controlled by the budget.                     |
| Cost Center or Project            | The specific segment value to which the budget applies.             |
| Account                           | The ledger account whose amount is compared with the budget.        |
| From Fiscal Year / To Fiscal Year | The fiscal-year range covered by the budget.                        |
| Distribution Frequency            | The interval used to divide the budget over time.                   |
| Budget Amount                     | The approved amount for the full budget period.                     |
| Distribute Equally                | Creates equal periodic amounts automatically.                       |
| Budget Distribution               | The dates, percentages, and amounts assigned to individual periods. |


## Review budget performance

Use the [Budget Variance Report](/erpnext/budget-variance-report) to compare the approved amount with actual spending. Filter by company, Fiscal Year, and budgeting segment. If a variance looks incorrect, open the [General Ledger](/erpnext/general-ledger) to inspect the transactions behind it.



A warning answers, “Should this transaction continue?” The variance report answers, “How is the complete plan performing?” Review both committed purchases and posted expenses because an approved order may consume the plan before it becomes an accounting expense through a [Purchase Invoice](/erpnext/purchase-invoice).

## Revise an approved budget

When management approves a genuine change to the amount or distribution, use [Budget Revision](/erpnext/budget-revision). This preserves the relationship between the original plan and the revised plan. Do not change a Budget merely to make one blocked transaction pass.

## What happens after submission

Submitting the Budget activates its checks. When you submit a covered transaction, ERPNext compares its amount with the applicable annual and periodic limits. It then applies the configured Stop, Warn, or Ignore action.



The Budget itself does not create a General Ledger entry, payable, or bank movement. Only the business transactions posted against the controlled Account affect the ledger.

## Troubleshooting

### No warning appears when spending exceeds the budget

Confirm that the Budget is submitted, the correct transaction stage is enabled, and the transaction uses the same company, account, fiscal period, and budget dimension value.

### The budget is triggered for the wrong period

Review the fiscal-year range, posting date, distribution frequency, and Budget Distribution rows. If Distribute Equally is disabled, confirm the manual amounts and percentages.

### ERPNext prevents an authorised exception

Review the configured action and your organisation's approval policy. An administrator can configure the Budget Approver role in Company settings for controlled exceptions.

## Frequently asked questions

### Does a Budget reserve cash?

A Budget does not reserve cash. It is a planning and control record and does not create a bank, payable, or General Ledger entry.

### Can one Budget cover several accounts?

A Budget record is created for a specific account and budget dimension. Create separate records when different accounts require their own limits.

### Can a Budget span multiple fiscal years?

You can span multiple fiscal years by selecting the appropriate From Fiscal Year and To Fiscal Year. Review the generated distribution carefully so that each period receives the intended amount.

### What is the difference between Warn and Stop?

Warn shows the over-budget condition but permits submission. Stop blocks submission until the transaction or budget is changed by an authorised user.

## Related topics

- [Budget Revision](/erpnext/budget-revision)
- [Budget Variance Report](/erpnext/budget-variance-report)
- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [Purchase Order](/erpnext/purchase-order)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__bulk-assign-tasks-in-a-project.md -->
---
title: "Bulk Assign Tasks in a Project"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-assign-tasks-in-a-project"
updated: "2026-02-27"
---

**Use Case**: Need to bulk assign all the Tasks in a Project to aUser.  
**Steps:**   
1) Create a Project.  
2) Create Tasks in that Project.  
3) Go to Task List and filter the Tasks based on the Project as shown below:  
![](/files/JWvaO3x.png)  
4) Select all the Tasks (or the Tasks you wish to assign to the User).  
![](/files/mpSG2p6.png)  
5) Go to Actions > "Assign To" and select the User to whom you wish to assign these Tasks.  
![](/files/GZFTC86.png)  
![](/files/5pvnr02.png)  
You can also enter other details such as Comments, Completed By and bulk set the Priority of the Tasks.  
6) Click on Add.  
**Note:** You can follow the above steps to bulk assign any documents in ERPNext.  
  
  

<!-- page: erpnext/erpnext__bulk-overwrite.md -->
---
title: "Overwrite Data"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-overwrite"
updated: "2026-07-02"
---

Use Data Import when you need to update many existing ERPNext records from a spreadsheet. This is useful for correcting field values, filling missing information, or applying the same change across records without opening each document manually.

Bulk overwrite updates existing records. It does not create a new record for each row when you choose **Update Existing Records**.

## Before You Begin

- Export or download the existing data before making changes, so you have a rollback reference.
- Test the import with a small set of records before updating a large list.
- Keep the record identifier column, such as `ID` or `name`, in the file. ERPNext uses it to find the record to update.
- Only keep the columns you want to update, plus the required identifier columns. Remove unnecessary columns to reduce the chance of overwriting the wrong field.
- Check mandatory fields and linked fields before importing. Invalid values will stop those rows from importing.

## Step 1: Open Data Import

1. Go to **Data Import** from the Data workspace or search for Data Import.
2. Click **Add Data Import**.
3. Select the **Document Type** that you want to update.

## Step 2: Choose Update Existing Records

1. In **Import Type**, select **Update Existing Records**.
2. Keep **Don't Send Emails** enabled unless you intentionally want update notifications to be sent.
3. Use **Submit After Import** only when the imported documents should be submitted immediately after update.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Step 3: Prepare the Import File

1. Download or prepare a spreadsheet for the selected Document Type.
2. Keep the record identifier column unchanged.
3. Enter the new values in the fields you want to overwrite.
4. Remove rows that should not be changed.
5. Save the file as CSV or Excel, depending on the import screen options.

If a field should not be changed, leave that column out of the import file. This is safer than keeping extra columns with stale values.

## Step 4: Upload and Validate

1. Upload the prepared file to the Data Import record.
2. Start the import preview or validation.
3. Review row errors carefully. Fix the file and upload it again if ERPNext reports missing links, invalid values, or permission issues.
4. Start the import only after the preview looks correct.

## What Gets Overwritten

ERPNext updates the fields present in the uploaded file for the matching records. The match is based on the document identifier in the file. For linked fields, the imported value must match an existing linked record.

## Common Issues

- **Record not found:** Check that the ID or name column is present and has the exact existing document ID.
- **Link validation failed:** The value in a linked field does not exist or is misspelled.
- **Mandatory field missing:** A required field is blank or was overwritten with an empty value.
- **Permission error:** Your user role does not have permission to update the selected Document Type or field.

## Recommended Practice

For important records, first run the update on a small sample. After verifying the result, import the remaining rows in batches. Keep the original export and the final import file for audit purposes.

<!-- page: erpnext/erpnext__bulk-rename.md -->
---
title: "Bulk Rename"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-rename"
updated: "2026-02-26"
---

### Renaming a single document

You can rename a document in ERPNext by going to **Menu > Rename**. This option will only be visible if you have the required permissions.

![](/files/image3a97ad.png)

### Rename Tool

Alternatively, using the **Rename Tool**, you can rectify or change multiple document IDs at once. You can rename IDs of up to 500 records at a time. 

:::note
This tool is only accessible to the User who has the System Manager role assigned.

:::



Let's assume you've realized your manual naming convention is making your inventory reports verbose. You need to convert 500 legacy item codes into your new naming standard. Now to rename these items:

#### Step 1: Create the spreadsheet

In a spreadsheet file, enter old Item IDs in the first column, new Item Ids in the second column. Save the spreadsheet file in a **.csv** format without the header.


| Old Name           | New Name     |
| ------------------ | ------------ |
| Large Blue Shirt   | SHIRT-BLUE-L |
| Small Red Shirt    | SHIRT-RED-S  |
| Medium White Shirt | SHIRT-WHT-M  |
| AA Batteries 4pk   | BATT-AA-04   |
| AAA Batteries 8pk  | BATT-AAA-08  |


#### Step 2: Upload data file

To upload the data file, search for "Rename Tool" on the awesomebar.

Select the DocType that you want to rename. Here, DocType will be Item. Then browse and upload the data file and click Rename.

![](/files/image36fdf6.png)

The Bulk Rename Jobs shows the progress of the process for each entry, from the queuing state to either finished or failed.



### Merging Documents

You can also merge documents by renaming them. For example, if you have a customer named Steve and a duplicate named Steve1, you can go to either of them, click on Menu > Rename, and tick the 'Merge with existing' checkbox. This will merge all the linked documents of both documents.

To do this in bulk with the Rename Tool, change the "Merge" column to "1" or "TRUE" and upload this file to trigger renaming.


| Old Name | New Name | Merge |
| -------- | -------- | ----- |
| Steve1   | Steve    | 1     |

<!-- page: erpnext/erpnext__bulk-update.md -->
---
title: "Bulk Update\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-update"
updated: "2026-04-14"
---

**Bulk Update allows you to update a particular field of a DocType for all documents.**

To access Bulk Update, go to:

> Home > Bulk Update

Consider that you have 20 quotations in which you had selected 'All Territories' and now you want to change the Territory to France. Instead of updating the individual quotations manually, you can use Bulk Update to update all 20 Quotations at once.

To do this,

1. Go to Bulk Update.
2. Select the Document Type, like Quotation.
3. Select the field to update, like territory.
4. Enter a **valid** new value to be updated.
5. Enter any conditions that apply, for example: {"status":"Draft"} will only affect documents in the Draft stage.
6. Select the limit, i.e. number of documents (Quotations) to be updated.
7. Click on Save

![](/files/imagea8e50c.png)

:::note
You can only update fields that can be updated normally in a particular stage. For example, valid till date cannot be updated for submitted Quotations.
:::
