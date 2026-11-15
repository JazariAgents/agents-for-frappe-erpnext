<!-- Frappe documentation: erpnext, part 21 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__depreciation-methods.md -->
---
title: "Depreciation Methods | ERPNext Documentation"
description: "Choose and configure Straight Line, Double Declining Balance, Written Down Value, or Manual depreciation in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/depreciation-methods"
updated: "2026-08-15"
---

Imagine Nova Industries buys two assets for the same price: an office table and a production machine. The table may provide roughly the same value every year. The machine may lose more value in its early years because it works hardest when it is new. Using one depreciation pattern for both may not reflect how they are actually used.



Depreciation Methods let the accountant choose how an asset's cost is spread over its useful life. ERPNext supports methods such as Straight Line and declining balance so the schedule can follow the company's accounting policy and the asset's pattern of use.

## Depreciation methods at a glance


| Method                       | How it works                                                                                    | Best suited for                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Straight Line**            | Records an equal depreciation expense in every complete period.                                 | Assets that provide a similar benefit throughout their life, such as office furniture, air conditioners, and basic equipment. |
| **Double Declining Balance** | Records a larger expense in the early years and a smaller expense later.                        | Assets that lose usefulness or value quickly when new, such as computers, mobile devices, and rapidly ageing machinery.       |
| **Written Down Value**       | Applies a fixed percentage to the asset's opening book value, so the expense reduces over time. | Assets for which the company's accounting or tax policy prescribes depreciation on the remaining book value.                  |
| **Manual**                   | Uses depreciation dates and amounts entered by the accountant instead of a standard formula.    | Assets with a contract-based, valuation-based, or specially approved depreciation schedule.                                   |


Treat this table as a practical starting point. The method used in the accounts should ultimately follow the organization's approved accounting policy and applicable reporting rules.

## Use one example to compare the methods

Assume Nova Industries buys a packaging machine for $50,000. It expects to use the machine for five years and sell it for $5,000 at the end. The amount to depreciate is therefore:



**Depreciable value = $50,000 cost - $5,000 residual value = $45,000**



Every method eventually allocates the same $45,000. What changes is how much expense appears in each year.

## Straight Line

Straight Line records the same expense in every complete year.



**Annual depreciation = $45,000 / 5 years = $9,000**


| Year | Opening book value | Depreciation | Closing book value |
| ---- | ------------------: | ------------: | ------------------: |
| 1    | $50,000            | $9,000       | $41,000            |
| 2    | $41,000            | $9,000       | $32,000            |
| 3    | $32,000            | $9,000       | $23,000            |
| 4    | $23,000            | $9,000       | $14,000            |
| 5    | $14,000            | $9,000       | $5,000             |


Use this method when the asset provides a similar benefit each year. Office furniture, air conditioners, and basic production equipment often fit this pattern.

## Double Declining Balance

Double Declining Balance records more depreciation while the asset is new. For a five-year life, the Straight Line rate is 20 percent. Double Declining uses twice that rate, or 40 percent, on each year's opening book value.



**Year 1 depreciation = $50,000 x 40% = $20,000**



The final expense is limited so the asset never falls below its $5,000 residual value.


| Year | Opening book value | Calculation               | Depreciation | Closing book value |
| ---- | ------------------: | ------------------------- | ------------: | ------------------: |
| 1    | $50,000            | $50,000 x 40%             | $20,000      | $30,000            |
| 2    | $30,000            | $30,000 x 40%             | $12,000      | $18,000            |
| 3    | $18,000            | $18,000 x 40%             | $7,200       | $10,800            |
| 4    | $10,800            | $10,800 x 40%             | $4,320       | $6,480             |
| 5    | $6,480             | Limited to residual value | $1,480       | $5,000             |


Use this method when an asset loses usefulness or market value faster in its early years. Computers, mobile devices, and some high-use machinery are common examples.

## Written Down Value

Written Down Value applies a chosen rate to the opening book value. Assume Nova's policy uses 30 percent per year for this machine.



**Year 1 depreciation = $50,000 x 30% = $15,000**



Because the opening value becomes smaller each year, the depreciation expense also becomes smaller. The last year is again limited so the closing value does not fall below $5,000.


| Year | Opening book value | Calculation               | Depreciation | Closing book value |
| ---- | ------------------: | ------------------------- | ------------: | ------------------: |
| 1    | $50,000            | $50,000 x 30%             | $15,000      | $35,000            |
| 2    | $35,000            | $35,000 x 30%             | $10,500      | $24,500            |
| 3    | $24,500            | $24,500 x 30%             | $7,350       | $17,150            |
| 4    | $17,150            | $17,150 x 30%             | $5,145       | $12,005            |
| 5    | $12,005            | Limited to residual value | $7,005       | $5,000             |


Use this method when the company's accounting or tax policy specifies a percentage on the remaining value. The example rate is illustrative. Use the rate approved for your organization.

## Manual

Manual depreciation lets the accountant define the dates and amounts instead of relying on a standard formula. Nova might use the following schedule when an equipment contract expects heavier use in its first two years.


| Year | Opening book value | Depreciation entered | Closing book value |
| ---- | ------------------: | --------------------: | ------------------: |
| 1    | $50,000            | $15,000              | $35,000            |
| 2    | $35,000            | $10,000              | $25,000            |
| 3    | $25,000            | $8,000               | $17,000            |
| 4    | $17,000            | $7,000               | $10,000            |
| 5    | $10,000            | $5,000               | $5,000             |


Use Manual only when a documented policy, valuation, or contract requires a custom pattern. The entered amounts should still total the $45,000 depreciable value.

## Compare the result


| Method                        | Expense pattern        | Year 1 expense | Year 5 expense                    | Closing value after year 5 |
| ----------------------------- | ---------------------- | --------------: | ---------------------------------: | --------------------------: |
| **Straight Line**             | Equal                  | $9,000         | $9,000                            | $5,000                     |
| **Double Declining Balance**  | Highest in early years | $20,000        | $1,480                            | $5,000                     |
| **Written Down Value at 30%** | Reduces each year      | $15,000        | $7,005 after residual-value limit | $5,000                     |
| **Manual example**            | Set by policy          | $15,000        | $5,000                            | $5,000                     |


## Set the method in ERPNext

Set the default method, useful life, frequency, and residual value in the Asset Category Finance Book row. The Asset can then use those defaults when ERPNext builds its depreciation schedules.

![Different depreciation methods by Finance Book](https://novacompanies.m.frappe.cloud/files/03-asset-category-finance-books.png)

The submitted schedule below uses Straight Line for Nova's packaging equipment. ERPNext has calculated $760 per month, accumulated the amount, and linked each posted row to its Journal Entry.

![Submitted depreciation schedule with calculated amounts](https://novacompanies.m.frappe.cloud/files/26-asset-depreciation-schedule-v2.png)

## Verify the result

Before submission, compare total scheduled depreciation plus residual value with the capitalized value. Also check the last date and the first full or prorated period.

## Troubleshooting

### The last schedule row is unexpectedly small

ERPNext may be limiting the final row so carrying value does not fall below the configured residual value.

### Two Finance Books show different carrying values

That is expected when they use different methods, useful lives, or start dates. Review reports with the intended Finance Book filter.

## Frequently asked questions

### Which method is best?

There is no universal best method. Use the method approved by the organization's accounting policy and reporting requirements.

### Can the method be changed after entries are posted?

A policy change may require cancellation or adjustment of linked schedules and entries. Review the accounting impact before changing a submitted asset.

### Can statutory and management reporting differ?

Separate Finance Books can keep different depreciation policies for the same asset.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__difference-between-system-user-and-website-user.md -->
---
title: "Difference Between System User and Website User"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-between-system-user-and-website-user"
updated: "2026-03-04"
---

**Question:** I have added my Employee as a User and have assigned them Roles as well. Still, they are not able to view Dashboard on the login.

**Answer:**

There are two type of Users in ERPNext.

* **System Users**: They are typically internal users such as employees, managers, and administrators who need extensive access to the ERPNext system to perform various business operations. They have a higher level of access and more detailed permissions, allowing them to interact with multiple modules, generate reports, and customize workflows.
* **Website Users**: They are typically external users like customers or suppliers who interact with the ERPNext system through a web portal. Their access is limited to functionalities relevant to their needs, such as placing orders, viewing order status, or managing their account information. Their interface is simpler compared to the comprehensive backend interface used by system users.

Here is the tabular comparison between System User and Website User in ERPNext



| **System User** | **Website User** |
| --- | --- |
| This type is useful for managing internal activities and operations | It is useful for managing external operations and transactions |
| It provides full access to ERPNext modules and features | It provides restricted access to ERPNext modules and features |
| Typical users in this category are internal employees  | The user persona in this type includes external parties such as customers, clients etc |
| They are created by an administrator within ERPNext | They can be self-registered or created by an administrator |
| It provides access to company-wide data and reports | It provides access to only personal data and limited reports |
| They can view, create, edit, and delete records | They can mostly view and create records relevant to them |
| They have full data entry capabilities across all modules | They have limited to data entry relevant to their role |

<!-- page: erpnext/erpnext__difference-entry-button.md -->
---
title: "Difference Entry | ERPNext Documentation"
description: "Use ERPNext Difference Entry to balance a Journal Entry, select the correct account, avoid masking errors, and verify the submitted General Ledger clearly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-entry-button"
updated: "2026-08-03"
---

The **Make Difference Entry** action helps you complete an unbalanced [Journal Entry](/erpnext/journal-entry). ERPNext calculates the difference between Total Debit and Total Credit, adds a new accounting row for that amount, and leaves the Account blank for you to choose.



It is a balancing aid inside Journal Entry, not a separate transaction and not an automatic correction. You must understand why the difference exists and select the account that represents it. If the source amount, exchange rate, tax, or original account is wrong, correct that value instead of hiding the error in a difference account.



In this example, Nova Electronics Trading pays $1,000 from its bank. The main office-maintenance expense is $990 and the bank charges a $10 fee. The first two rows are therefore out of balance. **Make Difference Entry** adds the missing $10 debit, after which the user selects **Bank Charges - NET**.


| Account                     | Debit         | Credit        | Meaning                              |
| --------------------------- | -------------: | -------------: | ------------------------------------ |
| Office Maintenance Expenses | $990.00       | $0.00         | Main expense paid.                   |
| Bank Charges                | $10.00        | $0.00         | Separate fee deducted by the bank.   |
| Nova Operating Bank         | $0.00         | $1,000.00     | Total reduction in the bank balance. |
| **Total**                   | **$1,000.00** | **$1,000.00** | The Journal Entry is balanced.       |


## Before you begin

Confirm the following:

1. You know what caused the imbalance and have supporting evidence for the amount.
2. The correct ledger exists in the Company's [Chart of Accounts](/erpnext/chart-of-accounts). Use a non-group account belonging to the selected Company.
3. The Posting Date is open and belongs to the intended Fiscal Year and [Accounting Period](/erpnext/accounting-period).
4. Any required Cost Center, Project, Finance Book, or other [Accounting Dimension](/erpnext/accounting-dimensions) is available.
5. For bank entries, you have the bank reference number and date. For ordinary Customer or Supplier receipts, consider whether a [Payment Entry](/erpnext/payment-entry) is the safer transaction.

## Identify the difference

1. Create or open a Draft Journal Entry.
2. Select the Company, Entry Type, and Posting Date.
3. Add the known debit and credit rows under **Accounting Entries**.
4. Review **Total Debit**, **Total Credit**, and **Difference (Dr - Cr)**.

The example has a $990 debit and a $1,000 credit. ERPNext shows a difference of -$10 and makes **Make Difference Entry** available.



![Unbalanced Journal Entry with Make Difference Entry highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-balanced-journal-entry.png)

Before continuing, check whether the difference is legitimate. A missing bank fee is legitimate. A transposed amount, duplicate row, wrong currency, or incorrect exchange rate should be fixed at its source.

## Add and complete the difference row

1. Select **Make Difference Entry**.

ERPNext adds one row for the exact amount required to make Total Debit equal Total Credit. Because credit exceeds debit by $10 in this example, it adds a $10 debit row.

2. Select the highlighted pencil icon on the new row.

![Generated difference row with its pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-row-added.png)

3. Select the Account that explains the difference. In the example, select **Bank Charges - NET**.

![Difference row editor with Bank Charges account highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-account-selected.png)

4. Add the same Cost Center, Project, Finance Book, or other dimensions required by your accounting policy.
5. Close the row editor and review the complete table.

![Balanced Journal Entry after selecting the difference account](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-balanced-journal-entry.png)

Total Debit and Total Credit are now both $1,000. The entry is mathematically balanced, but you must still confirm that every account and amount is economically correct. Balanced totals do not prove correct accounting.

## Submit and verify the result

1. Review the Company, Posting Date, Entry Type, accounts, amounts, references, remarks, currencies, and dimensions.
2. Save and submit the Journal Entry.
3. Confirm that the submitted document contains the original rows and the completed difference row.

![Submitted Journal Entry showing all three accounting rows](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-submitted-difference-journal-entry.png)

4. Open **View &gt; Ledger**, or run the [General Ledger](/erpnext/general-ledger) using the Journal Entry as the voucher filter.
5. Confirm the debit and credit for each account and the zero total balance across the voucher.

![General Ledger showing the Bank Charges difference entry](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-entry-general-ledger.png)

In the example, the ledger shows a $990 debit to Office Maintenance Expenses, a $10 debit to Bank Charges, and a $1,000 credit to the operating bank account.

## Important fields and what they mean


| Field or action                    | What it controls                                                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Total Debit                        | Sum of the debit values in the accounting rows.                                                                                   |
| Total Credit                       | Sum of the credit values in the accounting rows.                                                                                  |
| Difference (Dr - Cr)               | Total Debit minus Total Credit. A negative value means more debit is required; a positive value means more credit is required.    |
| Make Difference Entry              | Adds one debit or credit row for the current difference. It does not select the Account or confirm that the difference is valid.  |
| Account                            | Ledger that receives the difference. Select the account that represents the actual economic event.                                |
| Debit or Credit                    | Amount added by ERPNext to balance the voucher. Review it before submission.                                                      |
| Account Currency and Exchange Rate | Control the account-currency and Company-currency values in a [multi-currency Journal Entry](/erpnext/multi-currency-accounting). |
| Reference Type and Reference Name  | Link an accounting row to a supported document when the adjustment genuinely belongs to that reference.                           |
| Is Advance                         | Marks a party amount as an advance when it is not allocated to a specific invoice.                                                |
| Cost Center and other dimensions   | Classify the posting for management reporting without replacing the ledger account.                                               |


## When not to use Make Difference Entry

Do not use this action merely to make an error disappear.

- If an invoice, payment, or stock transaction is wrong, cancel and amend the source document where permitted instead of creating an unrelated balancing row.
- If a genuine receipt or payment is being recorded, use the purpose-built payment workflow so invoice allocation, party balance, bank reference, and reconciliation remain clear.
- If the difference comes from foreign currency conversion, review the account currency, exchange rate, and Company-currency values first. Use the supported [exchange gain or loss](/erpnext/managing-transactions-in-multiple-currency) process when that is the real cause.
- If a small decimal difference is caused by configured precision, first review the source values and [System Settings](/erpnext/system-settings). Do not change precision casually after live transactions exist.
- If the required treatment is recurring, create a controlled process or [Journal Entry Template](/erpnext/journal-entry-template) rather than repeatedly guessing the balancing account.

## Troubleshooting


| Issue                                            | What to check                                                                                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make Difference Entry is not visible             | The Journal Entry may already be balanced. Review Total Debit, Total Credit, and Difference. Also confirm the document is still in Draft.                           |
| The generated row has no Account                 | This is expected. ERPNext supplies the amount only. Open the row and select the account that explains the difference.                                               |
| The entry is balanced but submission still fails | Check mandatory party, reference, currency, Cost Center, bank-reference, account-type, and frozen-period requirements. Mathematical balance is only one validation. |
| A tiny difference keeps appearing                | Check entered amounts, account currency, exchange rates, and precision. Correct the calculation source before using a rounding account.                             |
| The wrong side was added                         | Review the sign of Difference. Negative means credit is greater than debit, so ERPNext adds a debit. Positive means debit is greater, so it adds a credit.          |


## Frequently asked questions

### Does ERPNext choose the difference account automatically?

No, it adds a row with the required debit or credit and leaves the Account blank. The user must select the correct Company ledger.

### Should every small difference go to a round-off account?

No, first determine whether the cause is rounding. A wrong amount, exchange rate, tax calculation, or missing expense must be corrected or posted to the account that represents it.

### Can Make Difference Entry correct a multi-currency mismatch?

It can make the Company-currency totals balance, but it does not prove that the account-currency amounts and exchange rates are correct. Review both currencies before using it.

### Why can a balanced Journal Entry still be rejected?

ERPNext also validates Company, account type, party, reference, currency, dimensions, posting restrictions, and other mandatory values. Equal totals satisfy only the double-entry balance test.

### Can I edit or remove the generated row?

Yes, while the Journal Entry remains in Draft. You can select its Account, change the row when justified, or remove it and correct the original rows instead.

## Related topics

- [Journal Entry](/erpnext/journal-entry)
- [Understanding Debit and Credit](/erpnext/understanding-debit-and-credit)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Payment Entry](/erpnext/payment-entry)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Journal Entry Template](/erpnext/journal-entry-template)

<!-- page: erpnext/erpnext__difference-in-total-and-valuation-in-tax-and-charges.md -->
---
title: "Include Tax or Charge in Valuation or Total?"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-in-total-and-valuation-in-tax-and-charges"
updated: "2026-08-03"
---

On a purchase transaction, a tax or charge can affect what you owe the supplier, the value assigned to received stock, or both. ERPNext separates these effects through **Consider Tax or Charge for** on each row of the [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template).

This choice matters because supplier payable and inventory valuation answer different questions:


| Question                                           | ERPNext value |
| -------------------------------------------------- | ------------- |
| How much must the company pay this supplier?       | Total         |
| How much did it cost to bring the item into stock? | Valuation     |


The available choices are **Total**, **Valuation**, and **Valuation and Total**.

## Before you begin

Confirm who is charging the amount and whether the cost should form part of inventory value. Ask your accountant how the cost must be treated under your accounting policy. Also confirm that the relevant tax, freight, or expense account exists in the [Chart of Accounts](/erpnext/chart-of-accounts).

Use **Total** or **Valuation and Total** only when the amount belongs in the payable created by this purchase document. Use **Valuation** when the amount should be allocated to stock but is not payable to this supplier on this document.

The examples below use:


| Component             | Amount  |
| --------------------- | -------: |
| Item net value        | $800.00 |
| Recoverable tax at 4% | $32.00  |
| Freight               | $100.00 |


The $32 tax is added to Total in every example. The difference is how the $100 freight row is treated.

## Choose the correct treatment


| Setting             | Supplier total    | Stock valuation   | Typical use                                                                |
| ------------------- | ----------------- | ----------------- | -------------------------------------------------------------------------- |
| Total               | Increases         | Does not increase | A charge payable to the supplier that should not be capitalized into stock |
| Valuation           | Does not increase | Increases         | Freight paid separately but allocated through this receipt or invoice      |
| Valuation and Total | Increases         | Increases         | The supplier charges freight and it forms part of landed inventory cost    |


The **Type** determines how ERPNext calculates the row amount. **Consider Tax or Charge for** determines where that amount has an effect. These are separate decisions. See [Types in Tax Template](/erpnext/types-in-tax-template) for the calculation options.

## Add a Total-only charge

Select **Total** when the charge should increase the amount payable on the [Purchase Invoice](/erpnext/purchase-invoice) but should not be allocated into item valuation.

For the example:

`$800 item value + $32 tax + $100 freight = $932 payable`

The freight does not increase the item's valuation through this row. This treatment can be appropriate for a fee that is expensed directly instead of capitalized.

1. Add or open a row in **Purchase Taxes and Charges**.
2. Select the required Account Head.
3. Set the calculation Type, such as **Actual** for a fixed $100 charge.
4. Set **Consider Tax or Charge for** to **Total**.
5. Review the row Amount and the document Grand Total.

Do not use Total merely because money was paid. The accounting treatment depends on whether the cost belongs in inventory value.

## Add a Valuation-only charge

Select **Valuation** when the cost should increase inventory value but should not increase the payable on this document. A common example is freight paid to a separate carrier while the purchase invoice being processed belongs to the item supplier.



![Purchase tax rows with freight considered for valuation](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-tax-table.png)

Open the freight row using its pencil icon. Set the row to **Valuation**, then enter the amount and the correct expense or clearing account.



![Freight row configured for valuation only](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-freight-fields.png)

In this example, the supplier payable remains:

`$800 item value + $32 tax = $832 payable`

The $100 freight is allocated into valuation but is excluded from the supplier total.



![Valuation-only freight excluded from the purchase invoice total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-result.png)

Use a suitable clearing or expense account for the valuation row. The source of the separately paid freight must still be recorded correctly, such as through another supplier invoice or a [Landed Cost Voucher](/erpnext/landed-cost-voucher), depending on the workflow.

## Add a charge to Valuation and Total

Select **Valuation and Total** when the same amount must increase both the supplier payable and the item's valuation. This is common when the item supplier arranges freight, includes it on the invoice, and the freight forms part of landed cost.



![Purchase tax rows with freight included in valuation and total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-tax-table.png)

Open the freight row and select **Valuation and Total**. Confirm the Account Head, Type, description, and amount before closing the row editor.



![Freight row configured for valuation and total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-freight-fields.png)

The supplier payable becomes:

`$800 item value + $32 tax + $100 freight = $932 payable`

The $100 freight is also allocated into inventory valuation.



![Freight included in both purchase invoice total and valuation](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-result.png)

## Understand the accounting and stock effect

A submitted purchase transaction may affect both the [General Ledger](/erpnext/general-ledger) and the [Stock Ledger](/erpnext/stock-ledger). The exact posting depends on whether stock is updated through a [Purchase Receipt](/erpnext/purchase-receipt), through **Update Stock** on a Purchase Invoice, or through another perpetual-inventory workflow.


| Treatment           | Payable effect                        | Inventory-value effect      |
| ------------------- | ------------------------------------- | --------------------------- |
| Total               | Included in the document's payable    | Not allocated by this row   |
| Valuation           | Excluded from this document's payable | Allocated to received items |
| Valuation and Total | Included in the document's payable    | Allocated to received items |


The valuation amount is distributed across eligible items according to ERPNext's valuation logic. Review the item valuation and ledger entries after submitting a controlled test. Do not infer the final accounting entry only from Grand Total.

## When to use a Landed Cost Voucher instead

Use a Landed Cost Voucher when additional costs become known after the receipt, come from another supplier, or must be allocated across one or more submitted receipts or invoices. It is designed to update the landed value of received stock.

Use the purchase tax table when the charge is known while creating the transaction and belongs naturally on that document. Avoid recording the same freight through both methods, because that can capitalize the cost twice.

## Verify the result before wider use

Create a draft with one item and easy numbers. Then:

1. Confirm the item Net Total.
2. Review each tax row's Amount and Total.
3. Compare the Grand Total with the expected supplier payable.
4. Submit the controlled transaction.
5. Open **Accounting Ledger** and confirm the payable and tax postings.
6. Open the stock ledger or valuation report and confirm the inventory effect.

If a template is reused automatically, test it before setting it as the company default or applying it through a [Tax Rule](/erpnext/tax-rule).

## Troubleshooting

### Freight increased the supplier payable unexpectedly

Open the freight row and check **Consider Tax or Charge for**. Use Valuation instead of Valuation and Total only when the amount must not be payable on this document and the accounting source is handled elsewhere.

### Freight did not increase item valuation

The row may be set to Total. Confirm that it is Valuation or Valuation and Total, that the transaction updates or receives stock, and that the selected account and item are eligible for the intended treatment.

### The payable is correct but the freight cost has no accounting source

A Valuation-only row does not make the amount payable to this supplier. Record the actual carrier or other cost source through the appropriate document, or use a Landed Cost Voucher when that better matches the workflow.

### Inventory appears to include the charge twice

Check whether the same cost was included in a valuation tax row and again in a Landed Cost Voucher. Keep only the posting that reflects the real source and timing of the charge.

## Frequently asked questions

### Should recoverable tax be included in valuation?

Usually a recoverable input tax is not part of inventory cost, but treatment depends on local rules and your accounting policy. Confirm the setup with your accountant.

### Can a fixed freight charge use Valuation and Total?

Y

es. Set Type to Actual, enter the freight amount, and use Valuation and Total when the supplier charges it and it must also form part of inventory value.

### Does Valuation-only mean the freight is free?

1. It means the amount is not payable on this particular purchase document. The actual payment or supplier liability must be recorded through its proper source.

### Is Consider Tax or Charge for available on sales transactions?

The valuation choice is relevant to purchase-side stock cost. Sales tax rows primarily affect the transaction total rather than incoming inventory valuation.

### Can I change the setting after submission?

Submitted accounting and stock transactions should not be edited casually. Cancel and amend where permitted, or use the appropriate correction process after reviewing the ledger impact.

## Related topics

- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)
- [Types in Tax Template](/erpnext/types-in-tax-template)
- [Perpetual Inventory](/erpnext/perpetual-inventory)

<!-- page: erpnext/erpnext__difference_between_lead_contact_and_customer.md -->
---
title: "Difference between Lead, Contact, and Customer | ERPNext Documentation"
description: "Understand when to use a Lead, Contact, or Customer in ERPNext and how these records relate."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference_between_lead_contact_and_customer"
updated: "2026-07-23"
---

A Lead, Contact, and Customer represent different parts of a relationship in ERPNext. Use the record that matches the party's current role instead of treating the three DocTypes as interchangeable.

## Lead

A [Lead](/erpnext/lead) is an unqualified person or organization that may become a customer. Use a Lead while your sales team is still confirming the requirement, interest, timing, or fit.

A Lead can be converted into an Opportunity and, when appropriate, a Customer.

## Contact

A [Contact](/erpnext/contact) is a person with communication details such as email addresses and phone numbers. A Contact can be linked to a Customer, Supplier, Lead, or another party.

Creating a Contact does not create a customer account or accounting relationship. Use Contacts to store the people your team communicates with at an organization.

## Customer

A [Customer](/erpnext/customer) is the commercial party used in selling and accounting transactions. Quotations, Sales Orders, Delivery Notes, Sales Invoices, pricing, credit controls, Addresses, and Contacts can be linked to the Customer.

Create a Customer when the party is sufficiently qualified and your process needs a reusable customer account.

## Comparison


| Record   | Represents                               | Use it when                                                                    |
| -------- | ---------------------------------------- | ------------------------------------------------------------------------------ |
| Lead     | An unqualified prospect                  | Interest has been captured but the party still needs qualification             |
| Contact  | A person and their communication details | You need to record the individual you communicate with                         |
| Customer | The party you sell to                    | You need sales transactions, pricing, delivery, billing, or accounting history |


## Common workflow

1. Capture an enquiry as a Lead.
2. Qualify the requirement and create an [Opportunity](/erpnext/opportunity).
3. Create or select the Customer when a customer account is required.
4. Link the relevant Contacts and [Addresses](/erpnext/address) to the Customer.
5. Continue with a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).

You can also create an Opportunity directly for an existing Customer. A Contact may be linked to multiple organizations when the same person legitimately represents more than one party.

## Related topics

- [Automate Lead Creation](/erpnext/automate_lead_capturing)
- [Customer Group](/erpnext/customer-group)
- [CRM Settings](/erpnext/crm-settings)

<!-- page: erpnext/erpnext__disable-rounded-total.md -->
---
title: "Disable Rounded Total\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disable-rounded-total"
updated: "2026-03-04"
---


All the sales transactions like Sales Order, Sales Invoice have Rounded Total in it. It is calculated based on the value of Grand Total. Moreover, Rounded Total is also visible in the Standard Print Formats.

> Note: The Rounded Total is a feature present in **Sales** transactions.

![Print Preview](/files/customize-disable-rounded-total-2.png)

However, if you wish to disable the same, you may follow the steps given below to hide the rounded total from Standard Print Formats, for all the sales transactions.

#### Step 1: Go to Global Defaults

From the Awesome Bar search for Global Defaults

#### Step 2: Disable Rounded Total

Check Disable Rounded Total, and click on save.

![Print Preview](/files/customize-disable-rounded-total.png)

To verify the changes, you should clear the cache and/or refresh your ERPNext account. Then your print formats shall not render value for the Rounded Total.

> Note: This setting will only affect Standard print formats.

<!-- page: erpnext/erpnext__disable-signup.md -->
---
title: "Disable Signup on ERPNext Website\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disable-signup"
updated: "2026-02-28"
---


ERPNext has portal feature available which allows third parties like Customers and Suppliers sign, place new orders and track updates on the previous orders.

![Website signup](/files/website-signup.png)

To allow new Customer and Supplier to Signup, the login page of your ERPNext account has Signup link avaiable. However, if you wish to disbale this feature, you can achieve it by following the steps given below.

### Steps

1. Go To

> Website > Setup > Website Settings `

2. In the Website Settings page, scroll down upto `More Information` section.

3. Check fied `Disable Signup`.

![Disable signup](/files/disable-signup.png)

4. Save Website Settings.

<!-- page: erpnext/erpnext__disassembly-order.md -->
---
title: "Disassembly Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disassembly-order"
updated: "2026-02-26"
---

The 'Disassembly Order' in ERPNext is used to dismantle finished goods and return the components that are in good condition back to the store. The system allows users to change the valuation rate of the components when adding them back to the store.

To create the "Disassembly Order", open the work order which are in **Completed** state or **Closed** state. Click on create button and after that "Disassembly Order"

![work-order-disassembly-order](/files/work-order-disassembly-orderfe73b5.png)  


Once user clicked on the "Disassembly Order" button, the system will open the stock entry with type as "Disassemble"

  


![stock-entry-disassembly-order](/files/stock-entry-disassembly-order.png)  


* Users can manually removed items which are not in a good condition
* The system, by default, fetches the basic rate based on past transactions. If users want, they can edit the basic rate for the raw materials.
