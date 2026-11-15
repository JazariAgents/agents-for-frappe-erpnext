<!-- Frappe documentation: erpnext, part 1 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__2-step-301-redirect-in-your-erpnext-website.md -->
---
title: "2 Step 301 Redirect in your ERPNext Website"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/2-step-301-redirect-in-your-erpnext-website"
updated: "2026-03-04"
---

  
**What is 301 Redirect?**  
A **301 Redirect** is used to make sure that search engines and users are sent to the correct page. A 301 status code is used when any page has been permanently moved to another location. Users will now see the new URL as it has replaced the old page.  
**2 Step 301 Redirects with ERPNext:**  
**Step 1:** Open Website Settings via the awesome bar (Global Search Bar) and expand the heading, "Redirects"  
[Screenshot on the live page]  
**Step 2:** Enter the old URL in Source and the new URL in Target and save the document.  
[Screenshot on the live page]  
**Watch the Redirect in action:**  
[Screenshot on the live page]  
  
[Screenshot on the live page]

<!-- page: erpnext/erpnext__access-log.md -->
---
title: "Access Log\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/access-log"
updated: "2026-03-04"
---


> Introduced in Version 13

**Access Log is a security feature that logs all data exports by all users in the system.**

It is a tool for System Managers to track which files were accessed or exported by users on the system. This is useful for tracking your company's sensitive information like transactions or financials.

Access logs are created in the following events:

 - Printing of all Forms and Reports
 - Private file downloading
 - Exporting via XLSX/CSV formats

In ERPNext, Access Log is available to System Managers, it can be accessed using the Global Search or through:

> Home > Users and Permissions > Logs > Access Log

[Screenshot on the live page: Access Log]

In case an access log is created on the event of exporting a Report, a **Show Report** button will be generated in the respective log. On clicking this button, the exported report can be viewed along with the set filters.

[Screenshot on the live page: Access Log]

Similarly, a **Show Document** button is generated in case of events related to documents directly such as document Printing and Private File download.

[Screenshot on the live page: Access Log]

Events such as [Raw Printing](/erpnext/raw-printing) save information along with the chosen template for the document.

[Screenshot on the live page: Access Log]

<!-- page: erpnext/erpnext__accounting-dimension-filter.md -->
---
title: "Accounting Dimensions Filters\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-dimension-filter"
updated: "2026-08-14"
---

Imagine Apple pays $1,000 to advertise the iPhone. The company wants its reports to show two simple facts: the money was spent on the **iPhone** product and by the **Marketing** department.



While entering the expense, someone accidentally selects **Mac** and **Engineering**. The payment amount is still correct, so the accounts balance. However, Apple's reports now tell the wrong story. They say the Mac engineering team spent $1,000, even though the money was used to advertise the iPhone.



An Accounting Dimension Filter prevents this mistake. Apple can create a rule that says, “When this iPhone advertising account is used, select the iPhone product and an allowed department.” If someone chooses an incorrect value, ERPNext stops the transaction before it is submitted.



This means the employee does not need to remember every accounting rule. ERPNext guides them while they enter the transaction. At the end of the month, the finance team can trust that the iPhone and Marketing reports include the correct $1,000 expense.



[Accounting Dimensions](/erpnext/accounting-dimensions) record which product and department received or spent the money. Accounting Dimension Filters make sure users choose values that are allowed for the account. This Apple story is only an easy example, not a description of Apple's real accounting system.



In the working example below, Nova Electronics Trading records revenue by department. The Sales - NET account must use the Sales department. The filter places this rule inside ERPNext, so users do not have to remember it for every invoice or journal entry.

## Before you begin

Create and enable the required Accounting Dimension first. Also create the dimension values that users will select, such as Sales, Service, or Operations.



Confirm which ledger accounts need control. A filter can apply to one or more accounts and can either allow selected values or restrict selected values.

## Create an Accounting Dimension Filter

Open the Accounting Dimension Filter list and select **Add Accounting Dimension Filter**.



[Screenshot on the live page: Accounting Dimension Filter list in ERPNext]



Select the **Accounting Dimension** and **Company**. Enable **Apply restriction on dimension values**, then choose how ERPNext should interpret the values:

- **Allow**: only the values listed in the filter can be used with the selected accounts.
- **Restrict**: the values listed in the filter cannot be used with the selected accounts.

Use **Allow** when the permitted list is short and stable. Use **Restrict** when most values are valid and only a few combinations must be blocked.



[Screenshot on the live page: Department Accounting Dimension Filter for Nova Electronics Trading]

### Select the accounts

In **Applicable On Account**, add every account to which the rule applies. Select **Is Mandatory** when the dimension must always be supplied for postings to that account.



In this example, Sales - NET is mandatory. Any transaction that posts to this income account must carry an accepted Department value.



[Screenshot on the live page: Mandatory account selected in an Accounting Dimension Filter]

### Select the dimension values

In **Applicable Dimension**, add the values that ERPNext should allow or restrict. The meaning of this list depends on the choice made in **Allow Or Restrict Dimension**.



Save the filter. Accounting Dimension Filters are configuration records, so they do not require submission.



[Screenshot on the live page: Allowed Department value selected in an Accounting Dimension Filter]

## How the filter works in transactions

When a transaction line uses an account covered by the filter, ERPNext checks its dimension value. With an Allow rule, values outside the permitted list are rejected. With a Restrict rule, values in the restricted list are rejected.



If **Is Mandatory** is selected, ERPNext also prevents submission when the dimension is blank. This check applies at the accounting line level, which matters for documents containing several income, expense, asset, or liability accounts.



The filter does not change the amount, tax, stock movement, or posting account. It validates the accounting classification attached to the posting.

## Important fields and what they mean


| Field                                 | What it controls                                                             |
| ------------------------------------- | ---------------------------------------------------------------------------- |
| Accounting Dimension                  | The dimension whose values are checked, such as Department or Business Unit. |
| Company                               | The company in which the rule applies.                                       |
| Disabled                              | Temporarily stops the filter without deleting it.                            |
| Apply restriction on dimension values | Enables value-level allow or restrict rules.                                 |
| Allow Or Restrict Dimension           | Determines whether listed values are permitted or blocked.                   |
| Accounts                              | The ledger accounts checked by the rule.                                     |
| Is Mandatory                          | Requires a dimension value whenever the account is used.                     |
| Dimensions                            | The allowed or restricted dimension values.                                  |


## Design filters that remain manageable

Start with rules that protect important reporting boundaries. Income and expense accounts are common candidates because missing or incorrect dimensions can distort departmental profit and loss reports.



Avoid creating many overlapping filters for the same account until the expected result is clear. Test each rule using a draft transaction before rolling it out to a large user group. Document why the combination is controlled so finance administrators can maintain it later.



If a valid business combination changes, update the filter before users post the new type of transaction. Disabling the filter removes the validation, so use that option only as a temporary, deliberate exception.

## Troubleshooting

### ERPNext says the dimension is mandatory

The transaction uses an account whose filter has **Is Mandatory** enabled. Enter an allowed dimension value on the affected accounting line.

### A valid value is not available

Check whether the filter uses Allow or Restrict, whether the correct company is selected, and whether the value exists in the Applicable Dimension table. Also confirm that the Accounting Dimension and its value are enabled.

### The filter appears to have no effect

Confirm that the transaction actually posts to an account listed in the filter. Also check that the filter is not disabled and that value restrictions are enabled.

## Frequently asked questions

### Does a filter change existing ledger entries?

It validates new or amended transactions. Existing submitted ledger entries remain unchanged.

### Can I create different rules for different companies?

Each filter is company-specific, which lets a multi-company setup use different accounting controls.

### Should I use Allow or Restrict?

Use Allow when only a small set of values is correct. Use Restrict when most values are acceptable and only known exceptions must be blocked.

### Can the dimension be optional for one account and mandatory for another?

The Is Mandatory setting is stored on each account row, so the requirement can vary by account.

## Related topics

- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [Cost Center](/erpnext/cost-center)
- [General Ledger](/erpnext/general-ledger)
- [Journal Entry](/erpnext/journal-entry)
- [Sales Invoice](/erpnext/sales-invoice)
- [Budget](/erpnext/budgeting)

<!-- page: erpnext/erpnext__accounting-dimensions.md -->
---
title: "Accounting Dimensions | ERPNext Documentation"
description: "Create and use ERPNext Accounting Dimensions to tag transactions, enforce segment rules, and filter financial reports by department or business unit."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-dimensions"
updated: "2026-08-14"
---

Imagine Apple wants to understand whether iPhone, Mac, or Services contributes the most profit, and whether the Americas, Europe, or Greater China performs best. Creating separate Sales, Travel Expense, Bank, and Receivable accounts for every product and region would make its [Chart of Accounts](/erpnext/chart-of-accounts) enormous and difficult to maintain.



Accounting Dimensions solve this by adding business context to the same accounting entry. Apple could tag a sale with Product Line = iPhone and Region = Americas, then filter financial reports by either dimension without duplicating ledger accounts. This is an illustrative example of how a large multi-product company could use dimensions, not a claim about Apple's internal accounting system.



The account tells Apple what happened, such as a sale or an advertising expense. The dimensions tell Apple which product and region it belonged to. This lets one clean set of accounts answer many management questions.



ERPNext already treats [Cost Center](/erpnext/cost-center) and [Project](/erpnext/project) as dimensions. Create a configurable Accounting Dimension when you need an additional segment. In the working example below, Nova Electronics Trading uses **Department** to compare Sales, Operations, and other teams while keeping one clean set of income, expense, asset, and liability accounts.

## Before you begin

Create the records that will supply the dimension values first. An Accounting Dimension must reference a DocType, so a Department dimension uses existing [Department](/hr/department) records. For a new concept such as Product Line, create and populate an appropriate custom DocType before configuring the dimension.



You need the Accounts Manager or System Manager role. Decide whether the dimension is only for analysis or must be entered on every Profit and Loss or Balance Sheet posting. Mandatory settings affect transaction submission, so test them with representative invoices, payments, and journals before enabling them for daily users.

## Create an Accounting Dimension

1. Open the Accounting Dimension list and select **Add Accounting Dimension**.
2. Select the **Reference Document Type**. ERPNext uses records from this DocType as the available dimension values.
3. Confirm the **Dimension Name**, then save. ERPNext creates the corresponding fields on accounting transactions and supported reports.

[Screenshot on the live page: Accounting Dimension list showing the Department dimension in ERPNext]



[Screenshot on the live page: Department selected as the Reference Document Type for an Accounting Dimension]

## Set a company default and mandatory rules

Use the **Dimension Defaults** child table when different companies need different defaults or validation rules. Select the highlighted pencil icon to open the complete row editor.



[Screenshot on the live page: Dimension Defaults row with the pencil icon highlighted]



For Nova Electronics Trading, **Sales - NET** is the default Department. The dimension is mandatory for Profit and Loss accounts, which helps prevent untagged income and expense postings. It is not mandatory for Balance Sheet accounts in this example.



[Screenshot on the live page: Department default and mandatory Profit and Loss setting in the child-row editor]

## Important fields and what they mean


| Field                                         | What it controls                                                                                                                                          |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reference Document Type                       | The DocType whose records become selectable dimension values. This cannot be changed after the dimension is created.                                      |
| Dimension Name                                | The label shown on transactions and report filters. ERPNext derives the generated field name from this value.                                             |
| Company                                       | The company to which a defaults-table row applies. Add separate rows when companies need different defaults or mandatory rules.                           |
| Default Dimension                             | The value ERPNext fetches automatically for the selected company. Users can change it when their role and the transaction permit it.                      |
| Mandatory for Profit and Loss Account         | Requires a dimension for postings to Income and Expense accounts.                                                                                         |
| Mandatory for Balance Sheet                   | Requires a dimension for postings to Asset, Liability, and Equity accounts.                                                                               |
| Automatically post balancing accounting entry | Uses the selected offsetting account to keep entries balanced by dimension. Enable this only after your accounting team validates the intended treatment. |
| Offsetting Account                            | The Asset or Liability ledger used for automatically generated balancing entries.                                                                         |


## Use dimensions in transactions

After the background field-creation job finishes, the new dimension appears in the Accounting Dimensions section of supported transactions such as a [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), [Payment Entry](/erpnext/payment-entry), and [Journal Entry](/erpnext/journal-entry). Choose the value that describes the transaction before submitting it.



Where ERPNext exposes the dimension on item or accounting rows, use row-level values when one document belongs to multiple departments or segments. A document-level value is convenient when the complete transaction belongs to one segment. Review the generated [General Ledger](/erpnext/general-ledger) entries after submission to confirm that the dimension reached the intended debit and credit lines.

## Filter accounting reports by a dimension

The generated dimension becomes a filter on supported reports. Select Department in the General Ledger to inspect detailed postings, or use it on the [Profit and Loss Statement](/erpnext/profit-and-loss-statement) and [Balance Sheet](/erpnext/balance-sheet) to analyse a segment. Report results only include entries that were posted with that dimension value.



[Screenshot on the live page: Profit and Loss Statement showing the generated Department dimension filter]



Accounting Dimensions do not retroactively tag older transactions. If earlier entries have no Department value, selecting a Department filter will exclude them. Treat dimension rollout as a controlled accounting change and decide how your team will handle historical comparisons.

## Disable an Accounting Dimension

Open the dimension and select **Disable** when it is no longer needed. Existing transaction and ledger values remain intact, so historical reports retain their tags. Refresh the browser after disabling if the generated field remains visible on a form.



Prefer disabling to deleting. The dimension is part of posted accounting history and may be referenced by reports or validations.

## Troubleshooting

### The new dimension does not appear on transactions

Field creation runs in the background. Wait for queued jobs to finish, reload the browser, and confirm that the dimension is enabled. If it is still missing, ask an administrator to review failed background jobs and the generated Custom Fields.

### A transaction says the dimension is mandatory

Open each accounting or item row that posts to the affected account type and provide the dimension value. A header value may not replace a missing row-level value when different rows can carry different dimensions.

### A filtered report is empty or incomplete

Confirm the company, date range, and dimension filter. Then inspect the source voucher and its General Ledger entries. Transactions created before the dimension was introduced, or entries saved without a dimension when it was optional, will not appear under that value.

## Frequently asked questions

### Should I create a new ledger account for each department instead?

Usually no. Keep accounts for the economic nature of the posting, such as Sales or Travel Expense, and use dimensions for the responsible department or segment. This avoids an oversized Chart of Accounts while preserving analysis.

### Can one invoice use more than one dimension value?

One invoice can use multiple values when the transaction exposes the dimension on item or accounting rows. Assign the appropriate value to each row and verify the resulting General Ledger entries.

### Will a new dimension classify old transactions automatically?

The generated field does not classify old transactions automatically. It applies to future edits and postings. Existing ledger entries remain unchanged, so plan the effective date and historical reporting approach before rollout.

### Why is a disabled dimension still visible?

Reload the browser after disabling it. If the field remains after a clean reload, confirm that the dimension is actually disabled and review current-version behavior with your administrator before changing generated Custom Fields manually.

### Can I make the dimension mandatory only for income and expenses?

Enable **Mandatory for Profit and Loss Account** and leave the Balance Sheet option cleared. ERPNext then validates postings according to the account type.

## Related topics

- [Accounting Dimensions Filters](/erpnext/accounting-dimensions-filters)
- [Cost Center](/erpnext/cost-center)
- [Budget](/erpnext/budget)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__accounting-entries.md -->
---
title: "Accounting Entries | ERPNext Documentation"
description: "Learn how common ERPNext transactions create balanced debit and credit entries, from owner funding and purchases to sales, expenses, payments, and closing."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-entries"
updated: "2026-08-03"
---

Every submitted accounting transaction in ERPNext creates balanced debit and credit entries in the [General Ledger](https://docs.frappe.io/erpnext/general-ledger). You normally do not post those lines yourself. You create the business document, such as a Sales Invoice or Payment Entry, and ERPNext uses its accounts and amounts to create the ledger effect.



This page follows one small business from owner funding to purchasing, selling, paying expenses, and closing a period. The examples explain the accounting logic behind the documents without requiring you to memorize journal-entry rules.

## Before you begin

Set up the company's [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts), default receivable and payable accounts, bank or cash accounts, stock accounts, income accounts, and expense accounts. Configure items and warehouses when you keep perpetual inventory.



Use the company's accounting currency consistently in these examples. Multi-currency transactions add exchange-rate and exchange-gain-or-loss entries, but the debit and credit principles remain the same.

## Understand debit and credit

A debit is not automatically good or bad, and a credit does not necessarily mean money received. They are the two sides of a balanced accounting entry.


| Account type | Increase is normally recorded as | Decrease is normally recorded as | Common examples                                           |
| ------------ | -------------------------------- | -------------------------------- | --------------------------------------------------------- |
| Asset        | Debit                            | Credit                           | Bank, Cash, Accounts Receivable, Stock in Hand, Equipment |
| Expense      | Debit                            | Credit                           | Rent, Salaries, Cost of Goods Sold                        |
| Liability    | Credit                           | Debit                            | Accounts Payable, Loans, Tax Payable                      |
| Equity       | Credit                           | Debit                            | Capital Stock, Retained Earnings                          |
| Income       | Credit                           | Debit                            | Sales, Service Income                                     |


Every posting must balance: total debits equal total credits. ERPNext validates this before a posting document can be submitted.

## 1. Record the owner's investment

Suppose the owner invests $25,000 in Nova Electronics Trading. The company now has $25,000 more in its bank, and the owner's equity in the business increases by the same amount.


| Account             | Debit   | Credit  | Why                                 |
| ------------------- | -------: | -------: | ----------------------------------- |
| Nova Operating Bank | $25,000 |         | The company's bank asset increases. |
| Capital Stock       |         | $25,000 | The owner's equity increases.       |


Record this with a [Journal Entry](https://docs.frappe.io/erpnext/journal-entry) because it is owner funding, not a customer or supplier payment against an invoice.



[Screenshot on the live page: Owner investment recorded as a balanced Journal Entry in ERPNext]

After submission, **View &gt; Ledger** shows the two balanced General Ledger lines.



[Screenshot on the live page: General Ledger entries created by the owner investment]

## 2. Buy equipment and inventory

Assume Nova buys equipment for $2,800 and phone inventory for $2,200. It pays $2,000 immediately and owes the supplier $3,000.

The purchase increases assets:


| Account          | Debit  | Credit |
| ---------------- | ------: | ------: |
| Equipment        | $2,800 |        |
| Stock in Hand    | $2,200 |        |
| Bank             |        | $2,000 |
| Accounts Payable |        | $3,000 |


Equipment is a fixed asset because the business expects to use it for more than one accounting period. Inventory is a current asset because it is held for sale. Bank decreases for the amount paid now, while Accounts Payable records the unpaid supplier balance.

In ERPNext, use a [Purchase Receipt](https://docs.frappe.io/erpnext/purchase-receipt) to receive stock when your process separates receipt from billing. Use a [Purchase Invoice](https://docs.frappe.io/erpnext/purchase-invoice) to recognize the supplier liability. If **Update Stock** is selected on the Purchase Invoice, the invoice can also receive stock without a separate Purchase Receipt.

The example Purchase Invoice records real NovaPhone inventory from a supplier.



[Screenshot on the live page: Inventory items on a submitted ERPNext Purchase Invoice]

Use a [Payment Entry](https://docs.frappe.io/erpnext/payment-entry) for the $2,000 paid now and allocate it to the supplier invoice. ERPNext debits Accounts Payable and credits Bank for the payment. The remaining $3,000 stays outstanding until it is paid or otherwise adjusted.

## 3. Sell inventory

Suppose Nova sells 325 units during the day for net sales of $1,625. The inventory cost of those units is $800. A stock sale normally has two accounting effects.

### Recognize the sale


| Account                     | Debit  | Credit |
| --------------------------- | ------: | ------: |
| Bank or Accounts Receivable | $1,625 |        |
| Sales                       |        | $1,625 |


If the customer pays immediately, Bank or Cash is debited. If payment is due later, Accounts Receivable is debited. Sales income is credited in both cases.

### Recognize the inventory consumed


| Account            | Debit | Credit |
| ------------------ | -----: | ------: |
| Cost of Goods Sold | $800  |        |
| Stock in Hand      |       | $800   |


The expense records what the sold items cost the business. The stock credit reduces the inventory asset. ERPNext calculates this amount from stock valuation; it is not necessarily the same as the selling price.

A [Sales Order](https://docs.frappe.io/erpnext/sales-order) records the commercial commitment but does not post revenue. A [Delivery Note](https://docs.frappe.io/erpnext/delivery-note) posts the stock and Cost of Goods Sold effect for a perpetual-inventory sale. A [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice) posts revenue, tax, and the customer receivable. When **Update Stock** is selected, the Sales Invoice can also post the stock effect without a separate Delivery Note.



[Screenshot on the live page: Inventory items on a submitted ERPNext Sales Invoice]

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

When the customer pays, submit a Payment Entry linked to the invoice. ERPNext debits Bank and credits Accounts Receivable, reducing the invoice's outstanding amount.

## 4. Record operating expenses

Assume monthly rent is $5,000 and salaries are $8,000. When they are paid from the bank:


| Account        | Debit  | Credit  |
| -------------- | ------: | -------: |
| Rent Expense   | $5,000 |         |
| Salary Expense | $8,000 |         |
| Bank           |        | $13,000 |


Expenses increase with debits, while the bank asset decreases with a credit. Use the most specific standard document available. Payroll documents should record salary liabilities and payments; a Purchase Invoice can record a supplier-billed expense; a Journal Entry can record a valid adjustment or expense for which no dedicated operational document is appropriate.

The following Journal Entry records $845 of office maintenance paid from Nova's operating bank account.



[Screenshot on the live page: Operating expense recorded with a balanced Journal Entry]

## 5. Understand profit during the period

Purchases of raw material or inventory continue to increase Stock in Hand until that stock is sold or consumed. Sales increase income, while Cost of Goods Sold, rent, salary, and other operating costs increase expenses.

Suppose the month's net sales are $40,000 and total expenses are $20,000. The [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement) reports a $20,000 profit for the period. This profit increases the owners' claim on the business, but it remains in the income and expense accounts until the period is closed.

The [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet) shows what the business owns and owes at a point in time. For example, after the transactions above, the company may hold $44,000 in cash and $1,000 in raw-material inventory, alongside its equipment, receivables, payables, and equity. The exact balances depend on every transaction posted during the period.

## 6. Close the period

Use a [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher) after reports have been reviewed and adjustments are complete. It transfers the net balance of income and expense accounts to an Equity or Liability closing account, normally Retained Earnings.

For a $20,000 profit, the simplified closing logic is:


| Account           | Debit   | Credit  |
| ----------------- | -------: | -------: |
| Profit or Loss    | $20,000 |         |
| Retained Earnings |         | $20,000 |


A loss reverses the direction. ERPNext calculates the actual entries from all Profit and Loss accounts for the selected period.

Select the company, fiscal year, period start and end dates, and the closing account. Review the Profit and Loss Statement and General Ledger before submitting.



[Screenshot on the live page: Period dates and Retained Earnings on an ERPNext Period Closing Voucher]

After submission, income and expense balances are closed into the selected balance-sheet account for that period. Do not use a closing voucher merely to hide an unexplained difference. Correct source transactions and complete approved adjustments first.

## Which ERPNext document should you use?


| Business event                        | Usually use            | Main accounting effect on submission                                                         |
| ------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------- |
| Customer commits to buy               | Sales Order            | No General Ledger entry                                                                      |
| Ship stock                            | Delivery Note          | Debit Cost of Goods Sold; credit Stock in Hand                                               |
| Bill a customer                       | Sales Invoice          | Debit Accounts Receivable; credit income and tax liabilities                                 |
| Receive customer money                | Payment Entry          | Debit Bank or Cash; credit Accounts Receivable                                               |
| Receive stock                         | Purchase Receipt       | Debit Stock in Hand; credit Stock Received But Not Billed                                    |
| Record a supplier bill                | Purchase Invoice       | Debit stock, asset, or expense; credit Accounts Payable                                      |
| Pay a supplier                        | Payment Entry          | Debit Accounts Payable; credit Bank or Cash                                                  |
| Record an adjustment or owner funding | Journal Entry          | Accounts depend on the event; debits and credits must balance                                |
| Transfer period profit or loss        | Period Closing Voucher | Close income and expense balances into Retained Earnings or another approved closing account |


Prefer operational documents over manual Journal Entries for routine sales, purchases, and payments. They preserve the customer, supplier, item, stock, tax, outstanding, and reconciliation details that a bare journal entry does not provide as clearly.

## Verify accounting entries

Open a submitted posting document and select **View &gt; Ledger**. Alternatively, run the General Ledger report and filter by company, voucher type, or voucher number.

Check that:

1. Total debit equals total credit.
2. The party and control account are correct.
3. Income, expense, stock, bank, and tax accounts match the transaction.
4. Cost Centers and accounting dimensions are present where required.
5. The posting date and fiscal year are correct.
6. The transaction appears correctly in the Profit and Loss Statement and Balance Sheet.

## Troubleshooting

### A Sales Order does not appear in the General Ledger

This is expected. A Sales Order is a commitment, not a revenue posting. Submit the appropriate Delivery Note and Sales Invoice, or a Sales Invoice with Update Stock, to record the accounting effect.

### The Sales Invoice shows revenue but no stock or Cost of Goods Sold entry

Check whether stock was already posted by a Delivery Note. If there is no Delivery Note, confirm that **Update Stock** was selected on the Sales Invoice and that the item maintains stock.

### A supplier invoice posts directly to an expense instead of inventory

Check whether the item maintains stock, the perpetual-inventory configuration, the selected warehouse, and the item's accounts. Service and non-stock items normally post to expense accounts rather than Stock in Hand.

### The invoice is paid, but an outstanding amount remains

Open the Payment Entry and confirm that the invoice is included in **References** with the correct allocated amount. Use [Payment Reconciliation](https://docs.frappe.io/erpnext/payment-reconciliation) when a standalone or advance payment needs to be allocated later.

### A report balance differs from the transaction

Confirm the report company, date range, finance book, currency, Cost Center, and other filters. Then open the source voucher's ledger and trace every posting. Do not edit General Ledger rows directly.

## FAQs

### Do draft documents affect the General Ledger?

No, Drafts can calculate totals for review, but posting documents affect the ledger only after submission.

### Why does a credit sale debit Accounts Receivable?

Accounts Receivable is an asset because the customer owes the company money. The asset increases with a debit, while Sales income increases with a credit.

### Why are inventory purchases not immediately an expense?

Unsold inventory is an asset. Its cost becomes Cost of Goods Sold when the inventory is sold or otherwise consumed, allowing the expense to be matched with the related revenue.

### Can I use a Journal Entry instead of invoices and Payment Entries?

Technically, some balances can be posted through a Journal Entry, but routine operational transactions should use their dedicated documents. Dedicated documents update outstanding balances, party ledgers, stock, taxes, payment references, and operational reports more safely and clearly.

### Can I submit another transaction after a Period Closing Voucher?

ERPNext applies closing-period controls to protect the closed accounts. Follow your organization's approved reopening or adjustment process rather than inserting transactions into a closed period casually.

## Related topics

- [Understanding Debit and Credit](https://docs.frappe.io/erpnext/understanding-debit-and-credit)
- [How Transactions Affect the Ledger](https://docs.frappe.io/erpnext/how-transactions-affect-the-ledger)
- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts)
- [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher)
- [Payment Entry](https://docs.frappe.io/erpnext/payment-entry)

<!-- page: erpnext/erpnext__accounting-for-bad-debts.md -->
---
title: "Accounting for Bad Debts | ERPNext Documentation"
description: "Write off a customer bad debt in ERPNext with a Journal Entry linked to the outstanding Sales Invoice, then verify the receivable and expense postings."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/accounting-for-bad-debts"
updated: "2026-08-14"
---

Record a bad debt when a customer receivable is no longer expected to be collected. The write-off should close or reduce the specific [Sales Invoice](/erpnext/sales-invoice), post the loss to an approved expense account, and preserve the Customer and invoice references for an auditable trail.



The example below writes off USD 500 from Northstar Retail. The demo company uses **Write Off - NET** as its approved expense account. Your organization may instead use an account named **Bad Debt Expense**.

## Before you begin

Complete your collection and approval process first:

- Review the Customer's [Accounts Receivable](/erpnext/accounts-receivables), Credit Notes, unallocated payments, disputes, and [Dunning](/erpnext/dunning) history.
- Confirm the approved write-off amount, accounting date, Customer, and Sales Invoice.
- Confirm which expense account your accountant wants to use. Create a non-group expense account such as **Bad Debt Expense** if one does not already exist.
- Keep the approval evidence ready to attach to the Journal Entry.

If the amount is being reduced because of a return, pricing dispute, or commercial concession, use a [Credit Note](/erpnext/credit-note) instead. A Credit Note can correct revenue and taxes; a bad-debt Journal Entry records a collection loss.

## Understand the accounting entry

The Journal Entry must balance:


| Row | Account                       | Debit | Credit | Result                                            |
| --- | ----------------------------- | -----: | ------: | ------------------------------------------------- |
| 1   | Bad Debt Expense or Write Off | 500   | 0      | Records the loss in the Profit and Loss statement |
| 2   | Receivable account            | 0     | 500    | Reduces the amount owed by the Customer           |


The receivable row must also contain the **Customer**, **Reference Type**, and **Reference Name**. These fields tell ERPNext which customer's balance and which invoice outstanding amount should be reduced.

## Create the Journal Entry

1. Go to **Accounting &gt; General Ledger, Journals and Adjustments &gt; Journal Entry**.
2. Select **Add Journal Entry**, highlighted below.

[Screenshot on the live page: Journal Entry list with Add Journal Entry highlighted]

3. Select the **Company** and **Posting Date**. Keep **Entry Type** as **Journal Entry** unless your accounting policy requires a different type.
4. In **Accounting Entries**, add the expense row. Select **Bad Debt Expense** or your approved write-off account and enter the approved amount in **Debit**.
5. Add a second row. Select the Company's Receivable account and enter the same amount in **Credit**.
6. Confirm that **Total Debit** equals **Total Credit**.

The example uses **Write Off - NET** for the debit and **Debtors - NET** for the credit. On the receivable row, select the highlighted pencil icon to open the full child-row editor. Fields for the Customer and invoice reference are available inside this editor.

[Screenshot on the live page: Balanced Journal Entry with the receivable-row pencil highlighted]

## Identify the Customer on the receivable row

In the child-row editor:

1. Confirm that **Account** contains the Receivable account used by the Sales Invoice.
2. Set **Party Type** to **Customer**.
3. Select the Customer whose debt is being written off in **Party**.

The highlighted fields identify Northstar Retail inside the shared receivable control account. Without the Party values, ERPNext cannot apply the write-off to the customer's outstanding balance correctly.

[Screenshot on the live page: Receivable account, Party Type, and Customer highlighted in the child-row editor]

## Link the write-off to the Sales Invoice

Continue in the same child-row editor:

1. Confirm that the write-off amount is entered in **Credit**.
2. Set **Reference Type** to **Sales Invoice**.
3. Select the invoice being written off in **Reference Name**.

The highlighted reference fields link the USD 500 credit to Sales Invoice `ACC-SINV-2026-00009`.

[Screenshot on the live page: Credit amount and Sales Invoice reference highlighted in the child-row editor]

This reference is essential. A Journal Entry can balance the General Ledger without it, but the Sales Invoice may remain outstanding in the Accounts Receivable report.

## Save and submit

1. Close the child-row editor and recheck both account rows.
2. Add a clear **User Remark**, such as `Approved partial bad debt write-off for ACC-SINV-2026-00009`.
3. Attach the approval, collection history, or other supporting evidence.
4. Save the Journal Entry.
5. Review the accounts, Customer, invoice reference, and posting date, then select **Submit**.

Submitting creates General Ledger entries. It does not create stock movement and does not alter the original Sales Invoice's item, revenue, or tax values.

## Partial write-off

For a partial bad debt, enter only the approved amount in both Journal Entry rows. The invoice remains outstanding for the balance.

For example, if an invoice has USD 1,200 outstanding and USD 500 is written off, its expected remaining outstanding amount is USD 700. Check the report after submission rather than assuming the reference was applied correctly.

## If the customer pays later

Do not edit or cancel a valid submitted write-off merely because the Customer later pays. Record the recovery using a new entry and the recovery income or expense account required by your accounting policy. Preserve a clear reference to the Customer, original invoice, and bad-debt Journal Entry.

Consult your accountant when a recovery affects tax reporting or a closed accounting period.

## Verify the result

After submission, check the [General Ledger](/erpnext/general-ledger) and Accounts Receivable report using the same Company, posting date, and currency.

Confirm that:

- the Sales Invoice outstanding amount is reduced by the write-off;
- the bad-debt or write-off expense account is debited;
- the Receivable account is credited;
- the ledger entries retain the Customer party;
- the receivable entry retains the Sales Invoice reference;
- no stock movement occurred.

## Troubleshooting

### The Sales Invoice still appears fully outstanding

Open the receivable row and confirm **Party Type**, **Party**, **Reference Type**, and **Reference Name**. Also check that the credit amount was entered on the receivable row rather than the expense row.

### The Customer or invoice cannot be selected

Confirm that the Receivable account, Customer, Sales Invoice, and Journal Entry belong to the same Company. Check the invoice currency and whether the selected account permits the required currency.

### Total Debit and Total Credit do not match

Enter the same approved write-off amount as a debit to the expense account and a credit to the Receivable account. Include any exchange difference required for a foreign-currency invoice according to your accounting policy.

### Accounts Receivable does not match the Receivable control account

Look for Journal Entries posted to a Receivable account without a Party or invoice reference. Compare the same Company, date, currency, and account in both reports.

## Frequently asked questions

### Can I write off the full invoice?

Y

es. Credit the Receivable account for the full outstanding amount and link the row to that Sales Invoice. Verify that the invoice becomes fully settled after submission.

### Can I write off several invoices in one Journal Entry?

Use a separate receivable row for each invoice reference. This keeps the allocation and audit trail clear.

### Does a bad-debt Journal Entry correct tax or revenue?

It normally records a collection loss and reduces the receivable. Use a Credit Note when the underlying sale, price, return, or tax must be corrected.

## Related topics

- [Journal Entry](/erpnext/journal-entry)
- [Accounts Receivables](/erpnext/accounts-receivables)
- [Sales Invoice](/erpnext/sales-invoice)
- [Credit Note](/erpnext/credit-note)
- [Sales Interest and Dunning](/erpnext/dunning)
- [General Ledger](/erpnext/general-ledger)
