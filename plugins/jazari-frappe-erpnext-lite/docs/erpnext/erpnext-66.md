<!-- Frappe documentation: erpnext, part 66 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__types-in-tax-template.md -->
---
title: "Types in Tax Template"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/types-in-tax-template"
updated: "2026-08-03"
---

The **Type** on a Sales or Purchase Taxes and Charges row tells ERPNext which amount to use as the calculation base. Choosing the correct Type matters as much as choosing the rate: the same 5 can mean 5%, a fixed $5, or $5 for every item unit. Start with the [Taxes](/erpnext/taxes) overview if the template, rule, and item-override roles are not yet clear.

ERPNext provides five Types:


| Type                   | Formula                                |
| ---------------------- | -------------------------------------- |
| Actual                 | Entered Tax Amount                     |
| On Net Total           | Net Total × Tax Rate ÷ 100             |
| On Previous Row Amount | Referenced row Amount × Tax Rate ÷ 100 |
| On Previous Row Total  | Referenced row Total × Tax Rate ÷ 100  |
| On Item Quantity       | Total item quantity × Tax Rate         |


The same Types are available in [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template) and [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template).



[Screenshot on the live page: All five tax-template calculation types]

## Before you begin

Separate the business question into three parts:

1. What is the base: net value, a fixed amount, another tax, a running total, or quantity?
2. Is the entered value a percentage or an amount per unit?
3. Should the row be added to or deducted from Total, Valuation, or both?

Write a small numerical example and calculate the expected result manually. Configure the rows in the same order as the calculation. For previous-row types, the referenced row must come earlier.

The examples below use a Net Total of $1,000 unless stated otherwise.

## Actual

Use **Actual** when the charge is a fixed amount rather than a percentage.

For example, a fixed shipping charge of $25 produces:


| Value                  | Amount    |
| ---------------------- | ---------: |
| Net Total              | $1,000.00 |
| Actual shipping charge | $25.00    |
| Total after the row    | $1,025.00 |


Enter the value in **Tax Amount**. The Tax Rate is not the calculation base for an Actual row.

Actual is suitable for a known shipping fee, documentation charge, insurance amount, or manual adjustment. If the amount varies by item value or quantity, choose a formula-based type instead.

On purchase documents, also decide whether the fixed amount affects supplier Total, stock Valuation, or both. See [Include Tax or Charge in Valuation or Total?](/erpnext/include-tax-or-charge-in-valuation-or-total).

## On Net Total

Use **On Net Total** for a percentage of the items' net value before taxes and charges.

With Net Total $1,000 and Tax Rate 8%:

`$1,000 × 8 ÷ 100 = $80`

The running Total after the row is $1,080 when the row is added to Total.

This is the usual choice for a standard tax applied uniformly to a [Sales Invoice](/erpnext/sales-invoice), purchase transaction, or order. If item rates differ, keep the transaction row for the tax account and use an [Item Tax Template](/erpnext/item-tax-template) for those amounts.

## On Previous Row Amount

Use **On Previous Row Amount** when the current row is calculated only on the Amount produced by another row.

Suppose row 1 calculates 8% tax on $1,000:


| Row | Calculation                                | Amount | Running Total |
| --- | ------------------------------------------ | ------: | -------------: |
| 1   | 8% On Net Total                            | $80.00 | $1,080.00     |
| 2   | 2% On Previous Row Amount, Reference Row 1 | $1.60  | $1,081.60     |


Row 2 uses `$80 × 2 ÷ 100`, not the $1,080 running total.

Set **Reference Row #** to 1. This type is useful for a surcharge, cess, or levy calculated only on another tax or charge amount.



[Screenshot on the live page: Previous Row Amount with its reference and rate]

## On Previous Row Total

Use **On Previous Row Total** when the current row is calculated on the running Total after an earlier row.

Using the same first row:


| Row | Calculation                               | Amount | Running Total |
| --- | ----------------------------------------- | ------: | -------------: |
| 1   | 8% On Net Total                           | $80.00 | $1,080.00     |
| 2   | 2% On Previous Row Total, Reference Row 1 | $21.60 | $1,101.60     |


Row 2 uses `$1,080 × 2 ÷ 100`. This is very different from the $1.60 result produced by **On Previous Row Amount**.

Use this type when the tax or charge is explicitly based on the subtotal that includes an earlier row. Confirm that this sequence is required by your pricing or tax rules.

## On Item Quantity

Use **On Item Quantity** when the charge is a fixed amount for every unit, regardless of item price.

If the transaction has 5 total units and the Tax Rate is 2:

`5 × $2 = $10`

The field is named Tax Rate, but for this Type it represents an amount per unit, not a percentage. A value of 2 does not mean 2%.

This type is suitable for an environmental fee, packaging charge, excise amount, or another per-unit levy. Check the [Unit of Measure](/erpnext/unit-of-measure-uom), quantities, and conversion factors carefully.

## Understand Amount and Total

Every tax row has two important calculated values:


| Column | Meaning                                                              |
| ------ | -------------------------------------------------------------------- |
| Amount | The tax or charge calculated by that row alone                       |
| Total  | The running transaction total after ERPNext adds or deducts that row |


**On Previous Row Amount** uses the first value. **On Previous Row Total** uses the second. When debugging a compound tax, inspect both columns on the referenced row rather than looking only at Grand Total.

## Use Reference Row # correctly

Reference Row # is valid only for **On Previous Row Amount** and **On Previous Row Total**.

The reference must point to an earlier row. If you insert, delete, duplicate, or move rows, check every dependent reference again. A formula that still points to row 1 may become wrong when a new row is inserted above the intended base.

Keep compound templates short. Use clear descriptions and test a known numerical example before making the template the default or selecting it through a [Tax Rule](/erpnext/tax-rule).

## Inclusive tax does not change the Type

**Is this Tax included in Basic Rate?** changes whether ERPNext adds tax on top of the entered price or back-calculates it from a price that already contains tax. It does not create another calculation Type.

For example, an 8% **On Net Total** row applied to a tax-exclusive net price of $100 adds $8. When the entered price of $108 is tax-inclusive, ERPNext derives the same $100 net and $8 tax from the entered amount.

See [Tax Inclusive Accounting](/erpnext/tax-inclusive-accounting) for the complete transaction effect.

## Purchase valuation is a separate decision

On a purchase tax row, **Consider Tax or Charge for** determines whether the calculated Amount affects supplier Total, stock Valuation, or both. The Type determines how the Amount is calculated; the valuation field determines where its effect goes.

For example, an Actual freight amount of $25 can be:

- Total only, which increases the supplier amount without allocating it into stock value.
- Valuation only, which allocates it into stock value without increasing that document's payable.
- Valuation and Total, which does both.

Configure both fields intentionally.

## Verify the calculation

Create a draft Sales Invoice or [Purchase Invoice](/erpnext/purchase-invoice) with small, easy-to-check values.

1. Confirm the item Net Total and total quantity.
2. Review each row in order.
3. Compare Amount and Total with your manual calculation.
4. Check Reference Row # on compound rows.
5. Confirm Add or Deduct and valuation treatment on purchase rows.
6. Review Total Taxes and Charges and Grand Total.
7. Submit a controlled example and inspect the [General Ledger](/erpnext/general-ledger).

Do not validate a complex template only with a large live invoice. A small example makes an incorrect base or row reference immediately visible. Confirm every Account Head in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Troubleshooting

### ERPNext says a row can be referenced only for a previous-row Type

Either change Type to **On Previous Row Amount** or **On Previous Row Total**, or remove Reference Row #. A fixed or Net Total row must not carry a previous-row reference.

### A compound tax is much larger than expected

You may have selected Previous Row Total when you intended Previous Row Amount. Compare the referenced row's Amount and Total, then recalculate the expected result manually.

### On Item Quantity gives an unexpected value

Treat the entered rate as currency per unit, not a percentage. Check total quantity, stock UOM, transaction UOM, and conversion factor.

### Changing row order changed the result

Previous-row calculations are sequence-dependent. Recheck every Reference Row # and the running Total after moving rows.

## Frequently asked questions

### Which Type should I use for a normal percentage tax?

Use On Net Total when the percentage applies to the transaction's item net value. Use Item Tax Templates when individual item rates differ.

### Which Type should I use for a fixed shipping fee?

Use Actual and enter the amount in Tax Amount. On a purchase document, separately choose whether it affects Total, Valuation, or both.

### What is the simplest difference between the two previous-row Types?

Previous Row Amount uses only the earlier row's charge. Previous Row Total uses the cumulative transaction total after that row.

### Can a later row reference more than one earlier row?

The row stores one Reference Row #. If a calculation needs a combined base, design the preceding running total carefully or use separate supported rows and verify the result.

### Does On Item Quantity apply a percentage to each item?

1. It multiplies quantity by a fixed amount per unit. A rate of 2 and quantity of 5 produces 10.

## Related topics

- [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Item Tax Template](/erpnext/item-tax-template)
- [Apply Tax on Another Tax or Charge](/erpnext/apply-tax-on-another-tax-or-charge)
- [Tax on Another Tax Amount](/erpnext/tax-on-another-tax-amount)
- [Tax Inclusive Accounting](/erpnext/tax-inclusive-accounting)

<!-- page: erpnext/erpnext__UAE-regional-fields.md -->
---
title: "UAE Regional Fields\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/UAE-regional-fields"
updated: "2026-02-26"
---

**Fields added to the Standard DocTypes to help regional compliances.**

1\. Item Master
---------------

1. **Is Zero Rated**: Tick this checkbox for items that are Zero Rated.
2. **Is Exempt**: Tick this checkbox for items that are tax exempted.

2\. Sales Invoice
-----------------

1. **VAT Emirate**: Select the Emirate of Place of Supply.
2. **Refund Provided to Tourists**: Enter the Tax Amount that was refunded to tourists.

3\. Purchase Invoice
--------------------

1. **Recoverable Standard Rated Expense**: Enter the Tax Amount that can be recovered.
2. **Reverse Charge Applicable**: Choose 'Y' if Reverse Charge is applicable. Taxes would be made zero and a reverse GL Entry will be created.
3. **Recoverable Reverse Charge (Percentage)**: Enter the percentage for which the Tax Paid under Reverse Charge is recoverable.

<!-- page: erpnext/erpnext__uae-vat-201-report.md -->
---
title: "UAE VAT 201 Report in ERPNext\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/uae-vat-201-report"
updated: "2026-02-26"
---


To generate UAE VAT 201 Report in ERPNext go to:
> Accounting > Value-Added Tax (VAT UAE) > UAE VAT 201
or simply search for UAE VAT 201 in the awesomebar.

[Screenshot on the live page: UAE VAT 201 Report]

To print the report, go to Menu > Print as shown in the screenshot below.

[Screenshot on the live page: UAE VAT 201 Report Download]

Note: To make sure the calculations in the report are correct, check the following:

1. Correct Emirate is selected in Company Address and Sales Invoice. The Sales Invoice Emirate field is auto filled using the selected Company Address but is editable.

2. Zero Rated or Exempted Items have "Is Zero Rated" or "Is Exempt" checkbox checked in the item master.

3. All VAT accounts are selected in UAE VAT Settings.

[Screenshot on the live page: UAE VAT Account Settings]

<!-- page: erpnext/erpnext__uae-vat-setup.md -->
---
title: "VAT/EXCISE Tax Implementation for UAE/KSA\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/uae-vat-setup"
updated: "2026-02-27"
---


### 1. Setting up Tax Registration No for customer, supplier and company

Set Tax Registration Number in the field, Tax ID for the Customer, Supplier, and Company.

1. For Customer
[Screenshot on the live page: TRN in Customer]

2. For Company
[Screenshot on the live page: TRN in Company]

### 2. Setting up TAX Code for Products
Setup tax code in the item master, system will fetch same code in the sales/purchase invoice on selection of an item.

[Screenshot on the live page: Tax Code in Item]
### 3. Default Tax Templates

ERPNext provides you default tax template for vat(5%, zero, exempted) and excise(50%, 100%). You can create your own [tax template](/erpnext/setting-up-taxes.html).

[Screenshot on the live page: Default Tax Template]

### 3. Making VAT Ready Invoices

If you have setup the TRN of your Customers and Suppliers, and your tax template, you are ready to go for making VAT Ready Invoices!

For **Sales Invoice**,

1. Select the correct Customer and Item and the address where the transaction will happen.
2. Check if the TRN of your Company and Supplier have been correctly set.
3. Check if the TAX Code has been set in the Item
4. Select the template that you have created based on the type of transaction
5. Save and Submit the Invoice

[Screenshot on the live page: VAT Invoice]

### 4. Print Tax Invoice

ERPNext provides two default print format

1. Simplified Tax Invoice
[Screenshot on the live page: Simplified Tax Invoice]

2. Detailed Tax Invoice
[Screenshot on the live page: Detailed Tax Invoice]

### 5. Set-up VAT Accounts
Select the accounts that will be used for creating VAT invoices here.

[Screenshot on the live page: UAE VAT Account Settings]

<!-- page: erpnext/erpnext__understand-debit-and-credit.md -->
---
title: "Understanding Debit and Credit | ERPNext Documentation"
description: "Learn how debit and credit work in ERPNext with balanced examples for sales, purchases, payments, stock, expenses, and depreciation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/understand-debit-and-credit"
updated: "2026-08-14"
---

Debit and credit are the two sides ERPNext uses to keep the books balanced. They do not mean good and bad, or always mean increase and decrease. Their effect depends on the type of account being updated.



For example, when Nova Industries receives $1,000 from a customer, Bank increases with a debit and Accounts Receivable decreases with a credit. The two sides balance, while the business story is simple: cash arrived and the customer now owes less.



This page explains the rules through familiar sales, purchase, expense, asset, liability, and payment examples. The aim is to help you read ERPNext ledger entries confidently, not memorize isolated journal formulas.

## Start with the accounting equation

The balance sheet is built on:

**Assets = Liabilities + Equity**



Income increases profit and therefore increases equity. Expenses reduce profit and therefore reduce equity. This gives the normal behavior of the five account classes:


| Account class | What it represents                     | Increase with | Decrease with | Common examples                               |
| ------------- | -------------------------------------- | ------------- | ------------- | --------------------------------------------- |
| **Asset**     | Resources the company owns or controls | Debit         | Credit        | Cash, bank, receivables, inventory, equipment |
| **Liability** | Amounts the company owes               | Credit        | Debit         | Payables, loans, tax payable                  |
| **Equity**    | Owners' residual interest              | Credit        | Debit         | Capital, retained earnings                    |
| **Income**    | Value earned during a period           | Credit        | Debit         | Sales, service income                         |
| **Expense**   | Value consumed during a period         | Debit         | Credit        | Rent, salaries, cost of goods sold            |


A useful memory aid is: assets and expenses normally increase on the debit side; liabilities, equity, and income normally increase on the credit side.



The word **normally** matters. An account can contain entries on both sides. A Customer payment credits receivables because it reduces an asset. A sales return debits sales because it reduces income.

## Debit and credit are not payment directions

Consider three events:

1. A Customer pays an invoice. Bank is debited because the bank asset increases. Receivables are credited because the amount owed by the Customer decreases.
2. You pay a Supplier. Payables are debited because the liability decreases. Bank is credited because the bank asset decreases.
3. You buy a laptop for cash. Equipment is debited because an asset increases. Bank is credited because another asset decreases.

The same bank account can therefore be debited or credited depending on whether its balance increases or decreases.

## How common ERPNext transactions balance

The examples use simplified values and omit rounding. Account names in your Company may differ.

### Credit sale

Nova Electronics Trading issues a Sales Invoice for USD 1,000 plus USD 80 tax and will collect payment later.


| Account             | Debit     | Credit    |
| ------------------- | ---------: | ---------: |
| Accounts Receivable | 1,080     |           |
| Sales               |           | 1,000     |
| Tax Payable         |           | 80        |
| **Total**           | **1,080** | **1,080** |


Receivables increase because the Customer owes more. Income and tax liability also increase. A submitted [Sales Invoice](/erpnext/sales-invoice) creates these entries automatically from its items, taxes, and configured accounts.

### Receive the Customer payment

The Customer pays USD 1,080.


| Account             | Debit     | Credit    |
| ------------------- | ---------: | ---------: |
| Bank                | 1,080     |           |
| Accounts Receivable |           | 1,080     |
| **Total**           | **1,080** | **1,080** |


Cash at bank increases and the Customer's debt decreases. A [Payment Entry](/erpnext/payment-entry) also links this amount to the invoice so its outstanding balance becomes zero.

### Credit purchase

Nova receives a Supplier invoice for USD 600 of office equipment.


| Account          | Debit   | Credit  |
| ---------------- | -------: | -------: |
| Office Equipment | 600     |         |
| Accounts Payable |         | 600     |
| **Total**        | **600** | **600** |


The equipment asset and Supplier liability both increase. If the purchase were an operating expense, the debit would go to an expense account instead.

### Pay the Supplier


| Account          | Debit   | Credit  |
| ---------------- | -------: | -------: |
| Accounts Payable | 600     |         |
| Bank             |         | 600     |
| **Total**        | **600** | **600** |


Both the liability and the bank asset decrease.

### Deliver stock to a Customer

Suppose a laptop sold for USD 1,000 has a valuation cost of USD 700. With [perpetual inventory](/erpnext/perpetual-inventory), the delivery records the cost separately from the sale:


| Account            | Debit   | Credit  |
| ------------------ | -------: | -------: |
| Cost of Goods Sold | 700     |         |
| Stock Asset        |         | 700     |
| **Total**          | **700** | **700** |


Cost of goods sold increases as an expense; inventory decreases as an asset. This entry can come from a Delivery Note or a stock-updating Sales Invoice.

### Receive stock before the Supplier invoice

When goods are received before billing:


| Account                       | Debit | Credit |
| ----------------------------- | -----: | ------: |
| Stock Asset                   | 700   |        |
| Stock Received But Not Billed |       | 700    |


The Purchase Receipt records the inventory and a temporary liability. The later Purchase Invoice debits Stock Received But Not Billed and credits Accounts Payable. This clears the receipt accrual and establishes the Supplier balance.

### Record an expense paid immediately

Nova pays USD 120 for internet service.


| Account          | Debit | Credit |
| ---------------- | -----: | ------: |
| Internet Expense | 120   |        |
| Bank             |       | 120    |


An expense increases and the bank asset decreases. This can be recorded through a Purchase Invoice followed by payment, or an appropriate payment or journal workflow based on the required controls and evidence.

### Record depreciation


| Account                  | Debit | Credit |
| ------------------------ | -----: | ------: |
| Depreciation Expense     | 100   |        |
| Accumulated Depreciation |       | 100    |


Depreciation expense increases. Accumulated depreciation is a contra-asset account with a normal credit balance, so it reduces the net book value of the Asset without changing its original cost account.

## Contra accounts and unusual balances

A contra account offsets another account while remaining separately visible. Common examples include accumulated depreciation, sales returns, purchase returns, and allowances.

An account can also show an unexpected balance without being invalid:

- A Customer receivable with a credit balance may represent an advance or overpayment.
- A Supplier payable with a debit balance may represent an advance paid.
- A bank account with a credit balance may represent an overdraft.
- Income may be debited by a Credit Note or correction.

Investigate the source vouchers and business meaning before deciding that the sign is wrong.

## How parties and accounts work together

ERPNext usually uses a shared receivable account for many Customers and a shared payable account for many Suppliers. The **Party Type** and **Party** on each ledger entry identify whose balance changed.



This is why the Chart of Accounts does not need one ledger account per Customer. The [Accounts Receivable and Payable reports](/erpnext/accounting-reports) combine account postings with party and payment references to show invoice-level outstanding amounts and ageing.

## Dimensions do not change debit and credit

A Cost Center, Project, or other [Accounting Dimension](/erpnext/accounting-dimensions) tags an entry for analysis. It does not replace the account or change whether the amount is a debit or credit.



For example, one rent expense account can be split across Retail, Online Sales, and Administration Cost Centers. The General Ledger remains balanced, while the Profit and Loss Statement can be filtered or grouped for management reporting.

## Review entries in ERPNext

After submitting a transaction:

1. Open the source document.
2. Select **View &gt; Accounting Ledger**.
3. Confirm the debit and credit totals are equal.
4. Check that each account matches the economic event.
5. Verify the party on receivable or payable rows.
6. Review the Cost Center, Project, Finance Book, and other dimensions where applicable.
7. Open the [General Ledger](/erpnext/general-ledger) to see the entry in account context.

Use the [Trial Balance](/erpnext/accounting-reports) to confirm that total debits and credits remain equal across the selected period. Equality proves mathematical balance, but it does not prove that every account choice is correct.

## When to use a Journal Entry

Use a [Journal Entry](/erpnext/journal-entry) for genuine accounting adjustments such as accruals, provisions, reclassifications, opening balances, and approved write-offs.

Prefer specialized transactions for normal operations:

- Sales Invoice for Customer billing
- Purchase Invoice for Supplier billing
- Payment Entry for receipts, payments, and internal transfers
- Delivery Note, Purchase Receipt, or Stock Entry for inventory movement
- Asset transactions for capitalization, depreciation, sale, and disposal

Specialized documents calculate taxes, update outstanding amounts, preserve operational references, and apply validations that a manual Journal Entry may bypass.

## Common mistakes


| Mistake                                            | Better approach                                                                                                   |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Treating debit as money received                   | Identify the account class, then ask whether that account increased or decreased.                                 |
| Treating credit as a negative amount               | Read debit and credit as sides of an entry, not positive and negative signs.                                      |
| Creating one receivable account for every Customer | Use shared receivable accounts and let the Party identify the Customer unless a separate account is required.     |
| Fixing an invoice with an unrelated Journal Entry  | Correct, return, cancel, or amend the source document where possible so operational and accounting records agree. |
| Checking only that totals balance                  | Also verify accounts, parties, dates, dimensions, references, taxes, and currencies.                              |


## Frequently asked questions

### Why does a bank receipt appear as a debit?

Bank is an asset. Receiving money increases that asset, and an asset increase is a debit.

### Why is sales income a credit?

Income increases profit and equity. Income accounts therefore normally increase with credits.

### Can I enter a negative debit?

ERPNext usually represents the opposite effect on the other side of the entry. Follow the relevant document's return or reversal workflow rather than forcing negative values.

### Does every transaction affect exactly two accounts?

Double entry requires equal totals, not exactly two rows. An invoice with several taxes, income accounts, discounts, and stock effects can create many GL Entries.

## Related topics

- [Accounting Introduction](/erpnext/accounting-introduction)
- [How Transactions Affect the Ledger](/erpnext/how-transactions-affect-the-ledger)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__unicommerce_integration.md -->
---
title: "Unicommerce Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/unicommerce_integration"
updated: "2026-02-26"
---


Unicommerce is aggregator for many e-commerce platforms that allows you to sell items through many supported marketplaces and process order via unified interface called Uniware. Learn more about Unicommerce at [https://unicommerce.com/](https://unicommerce.com/)

## ERPNext Integration with Unicommerce

ERPNext offers a full 2-way integration with Unicommerce using Uniware's REST APIs. This integration is provided using Frappe App officially supported by Frappe team. Broadly this integration covers:

1. Item catalogue syncing with Unicommerce (2-way)
2. Inventory Syncing (1-way from ERPNext to Unicommerce)
3. New Sales Order syncing
4. Sales Invoice syncing OR Sales Invoice generation (Any one option should be used)


## App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
- If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`


## Authentication and basic setup

[Screenshot on the live page: unicommerce auth setup]

1. Once app is installed go to "Unicommerce Settings" page.
2. Click on "Enable Unicommerce" checkbox.
3. Enter your Unicommerce site, username and password.
4. Client ID is added by default, however if you've configured a separate client ID, you need to update it here. If you're unsure about your client ID, please get in touch with Unicommerce support team.
5. Click "Save" this will initiate process of authenticating with Unicommerce and setting up custom fields for integration.
6. Once this setup is finished you'll see access/refresh tokens in "Authentication Details" section. This implies that authentication was successful and you can now start working on further setup.

If authentication fails:

1. Please recheck entered details.
2. Your server might be getting blocklisted by firewall. Get in touch with Unicommerce support team to get your server's IP whitelisted.


## Item Sync

This integration checks for newly created items and uploads them to Unicommerce on hourly basis. To enable this feature you need to setup following:


1. Go to "Unicommerce Settings" and enable "Upload new items to Unicommerce".
2. Set a Default Item Group. This is only used as fallback in case item group is missing.
3. While creating a new item check "Sync with Unicommerce" checkbox, to upload that item to Unicommerce.
4. This checkbox can also be enabled on existing items.

Unicommerce SKU code is immutable, hence you should not change Item Code after creation.


In order to correctly sync item group with product categories you need to map all item groups to their respective product categories on Unicommerce.

To map and item group to product category:

1. First find product category code on Unicommerce.
2. Open related Item Group on ERPNext and update Unicommerce product category code there.

[Screenshot on the live page: Unicommerce product category]
[Screenshot on the live page: ERPNext item group]

Item sync field mapping is as follows:

| ERPNext field | Unicommerce Field | Comments |
| :-: | :-: | --- |
| Item Code | SKU | Unicommerce SKU restrictions apply |
| Item Name | Item Name | |
| Description | Description | |
| Weight per unit | Weight | Only if set in Grams. |
| Shelf life in days | Shelf life | |
| HSN Code | HSN Code | |
| Image | Image | |
| Unicommerce item length | Length | |
| Unicommerce item width | Width | |
| Unicommerce item height | Height | |
| Disabled | Enabled | (opposite is mapped) |
| EAN barcode | EAN | |
| UPC Barcode | UPC-A | |
| Item group | Product category | |



## Inventory Sync

Once Item sync is setup Inventory Sync can be enabled. The integration checks for changes in ERPNext inventory and pushes them to Unicommerce on configured interval. ERPNext inventory levels are considered source of truth by the integration and Unicommerce inventory levels are overwritten by ERPNext's inventory values.

1. Go to "Unicommerce Settings" and scroll down to "Inventory Sync" section.
2. Check "Enable inventory Sync"
3. Configure the sync frequency. Recommended frequency is 15 to 60 minutes.
4. In Warehouse mapping table add all the facility codes you have in Unicommerce and map them with ERPNext warehouse.
5. Check "Enabled" checkbox for all facilities you want to enable.
6. Save the settings.

> Note: All inventory is pushed to "DEFAULT" shelf. Unicommerce Shelves are not supported by this integration, make sure you only have one shelf on Unicommerce called "DEFAULT" to ensure correctness of inventory sync.

> Note: Unicommerce, like other e-commerce intengrations does not support fractional inventory.

## Sales Order Processing - Workflow

Following is workflow for processing orders on ERPNext. You can alternatively also process orders on Unicommerce and only sync finished order. 

[Screenshot on the live page: Unicommerce workflow]

## Sales Order Sync - Channel(s) Setup


Unicommerce Integration supports receiving and processing from multiple channel. To allow this, setup for Sales Order sync also has to be done in multiple stages.


### Defaults for Sales Order Sync

[Screenshot on the live page: default sales order sync]

1. Go to "Unicommerce Settings".
2. Scroll to "Sales Order Sync" setting section.
3. Setup order sync frequency. 30 to 60 minutes is recommended frequency.
4. Setup default customer group and naming series for documents.


### Channel specific Sales Order sync configurations

[Screenshot on the live page: channel specific sales order sync]

To allow for flexible configuration for each channel you need to create "Unicommerce Channel" document for each channel you want to enable for Sales Order sync.


1. Go to "Unicommerce Channel" from searchbar or from Unicommerce settings page.
2. Click "Add Unicommerce Channel"
3. Fill in required details like channel ID, default warehouse, company, accounts and naming series.
4. If Shipping for this channel is handled by marketplace then click "Shipping Handled by marketplace" or uncheck it.
5. After fully configuring the channel click on "Enabled" checkbox.


New Sales Order created in Unicommerce will now start syncing with ERPNext. During this process if new item is encountered then it's created in ERPNext using information from Unicommerce. Relevant information about Unicommerce order is mapped to ERPNext fields, additional information can be found in "Unicommerce Details" section on Sales ORder.


## Sales Invoice Sync

Sales Invoice syncing can be handled in one of two ways. Please select the appropriate option as per your needs.

#### 1. Processing invoice on Unicommerce (recommended)

If you want to process orders and invoices on Unicommerce and only sync fully processed orders in ERPNext then enable "Only Sync Completed Orders" in Unicommerce settings.

#### 2. Processing invoice on ERPNext

 If you want to process orders from ERPNext only then you need to generate invoice from ERPNext's Sales Order.

 In order to generate invoice, go to synced Unicommerce Sales Order, click on "Unicommerce > generate invoice". This will create a Sales Invoice and deduc the stock too.
 
 [Screenshot on the live page: generate invoice button]

## Shipment Manifest

If you're processing orders on ERPNext using method #2 described above then you need to create and submit a shipping manifest to let Unicommerce know you've shipped the orders.

Pre-requisites is to setup following doctypes, you can find code on Unicommerce manifest creation page: 
1. Create Unicommerce Shipping Provider
2. Create Unicommerce Shipping Method


[Screenshot on the live page: Unicommerce shipment manifest]

Process of creating manifest:

1. Once you're ready to dispatch the packages to shipping provider, you should create "Unicommerce Shipment Manifest" document. Go to search bar > "Unicommerce Shipping Manifest" > + Add
2. Select Channel ID, Shipping Method, and Shipping provider code.
3. Now you can either use "Get Package" button to fetch open orders based on selected filters or use "Scan AWB Code" field to scan AWB of packages. Both will auto populate remaining details after saving. 
4. Once you're sure that all details look correct, save and submit the document. 
5. Upon submitting the manifest, same manifest is created and closed on Unicommerce and shipments are marked as "Dispatched". Unicommerce Manifest PDF is also fetched and attached to ERPNext manifest document. 

## Status Updates

[Screenshot on the live page: Unicommerce details section]

Status of Unicommerce is periodically updated in ERPNext, you can see the current status in the "Unicommerce details" section.

## Order Cancellations

When order gets cancelled on Unicommerce, the integration syncs this action and cancels the order on ERPNext as well. Partially cancelled orders are also synced and cancelled items are removed from the ERPNext Sales Order. Both full and partial cancellations are synced on hourly basis and right before generating invoices. 


## Order returns

When return is created on Unicommerce, the integration syncs this action and creates a *Draft* Credit Note in ERPNext. 

Both return cases are handled by integration:

- RTO (return to origin)
 When shipment is returned to origin, shipment status changes and a Credit Note (with Update Stock) is created is created in ERPNext. Credit Note will be full return. 
- CIR (Customer Initiated Return)
 When a customer returns shipment, it is reflected on Unicommerce's Sales Order section. Full or Partial Credit note is created depending upon the nature of customer initated return.

You can view all returns by going to "Sales Invoice" and filtering by "Is Return" set to Yes. Return tracking code is also captured on Credit Note.


While creating returns, the return warehouse is picked based on configured Return Warehouse in Unicommerce settings. If it's not set, original warehouse will be used. 


[Screenshot on the live page: Unicommerce return warehouse]

<!-- page: erpnext/erpnext__united_arab_emirates.md -->
---
title: "Requirements for United Arab Emirates"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/united_arab_emirates"
updated: "2026-02-28"
---


ERPNext aims to support local regulation for different regions in the world. In most cases, ERPNext is very flexible, so you can easily add custom fields and make custom reports to support the regulation of your region.

This section contains region-specific features for the United Arab Emirates.

- [VAT Implementation for UAE/KSA](/erpnext/UAE-vat-setup)
- [UAE VAT 201 Report in ERPNext](/erpnext/UAE-vat-201-report)
- [UAE Regional Fields](/erpnext/UAE-regional-fields)

<!-- page: erpnext/erpnext__unreconciliation.md -->
---
title: "Unreconcile Payments | ERPNext Documentation"
description: "Remove an incorrect ERPNext payment allocation without deleting the original voucher."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/unreconciliation"
updated: "2026-08-01"
---

Unreconciliation removes an allocation between a payment or credit and an invoice. It does not erase the original vouchers. Use it when the payment was linked to the wrong invoice or for the wrong amount.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Unreconcile Payments

1. Identify the incorrect allocation and verify the source documents.
2. Open the unreconciliation tool from the supported voucher or workspace.
3. Select only the allocation that must be removed.
4. Confirm the action and review the resulting outstanding and unallocated balances.
5. Apply the payment to the correct invoice when appropriate.

Before submitting, verify the Payment Entry, the linked invoice, and the amount that will be unlinked.

[Screenshot on the live page: Unreconcile Payment showing the 400 USD allocation that will be removed]

After submission, the example Payment Entry has no invoice allocation and its 400 USD is available again as an unallocated amount.

[Screenshot on the live page: Payment Entry after unreconciliation showing zero allocated and 400 USD unallocated]

## Important fields and what they mean


| Field            | What it controls                                                            |
| ---------------- | --------------------------------------------------------------------------- |
| Voucher          | Payment Entry, Journal Entry, or credit document containing the allocation. |
| Against Voucher  | Invoice from which the allocation will be removed.                          |
| Allocated Amount | Amount to delink.                                                           |
| Posting Date     | Date associated with the original allocation.                               |
| Delinked Status  | Indicates that the allocation is no longer active.                          |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The Unreconcile action is unavailable

Confirm that the payment is currently reconciled, the document and version support unreconciliation, and your role has permission. Some older allocations require cancellation and amendment instead.

### The wrong invoice still shows as paid after unreconciliation

Refresh the report and inspect Payment Ledger for other allocations, credit notes, or payments. Removing one allocation does not remove other valid settlements.

### The payment does not become available for reallocation

Check its unallocated amount, party, account, currency, and document status. Verify that the unreconciliation process completed without an error.

## Frequently asked questions

### Does unreconciliation cancel the Payment Entry?

It does not reverse the bank movement. It removes the selected payment-to-invoice allocation so the amount can be applied correctly.

### Does unreconciliation change General Ledger entries?

The supported process updates the accounting references needed to reverse the allocation. Review General Ledger and Payment Ledger after processing.

### Can only part of an allocation be unreconciled?

Use the controls available in the current version and select only the intended allocation where supported. Verify the resulting outstanding and unallocated amounts.

### What should be done immediately afterward?

Reconcile the payment to the correct invoice or document the reason it remains unallocated. Leaving unexplained credits can distort collection and payable follow-up.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__uom.md -->
---
title: "Unit of Measure (UoM)\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/uom"
updated: "2026-03-06"
---

**A UoM is a unit using which an Item is measured.**

By default, there are many UoMs created in ERPNext. However, more can be added depending on your business use case.  
In the UoM there is an option 'Must be Whole Number'. If this is checked, you cannot use fraction numbers in this UoM. To know more about fractions and UoMs, check out [this page](/erpnext/managing-fractions-in-uom).

The UoM list by itself only stores the name. The actual conversion rates are stored in a document called 'UoM Conversion Factor'. If you add new UoMs and plan to use it in transactions where it'll be converted to other UoMs, it is advised that you add it to this list.

For example, here 1 Kg is approximately 2.2 Pounds and the exact conversion factor is stored:

[Screenshot on the live page]

<!-- page: erpnext/erpnext__update-gstr-1-data-in-gst-offline-tool.md -->
---
title: "Generate GSTR-1 JSON File"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/update-gstr-1-data-in-gst-offline-tool"
updated: "2026-07-31"
---

  
Follow below steps to generate JSON file using ERPNext.  
**Setup GST Parameters:**Go to Accounts > Goods and Services Tax (GST India) > GST Settings and update GST parameters.[Screenshot on the live page]  
**Report GSTR-1:**Go to Accounts > Goods and Services Tax (GST India) > GSTR-1. Also, you can search in awesome bar.[Screenshot on the live page]  
**Select Return period and Type of Business:**Update filters as per return period and type of Business ( invoice Type) to get the required data.[Screenshot on the live page]  
**Download GSTR-1 Data:**Go to Menu and export and download GSTR-1 Data.  
**GST Return Offline Tool:**Open GST Offline Tool. (Download Offline Tool from [GST Portal](https://www.gst.gov.in/download/returns))[Screenshot on the live page]**﻿**Press **New** button and update GST return type, GSTIN Fiscal Year and Tax Period in Offline Tool .[Screenshot on the live page]  
**Select Section and Import GSTR-1 CSV in Offline Tool.**[Screenshot on the live page]  
**Generate and Download JSON file.**[Screenshot on the live page]  
**Upload JSON file on GST Portal.**[Screenshot on the live page]

<!-- page: erpnext/erpnext__update-stock-option-in-sales-invoice.md -->
---
title: "Delivery from Sales Invoice\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/update-stock-option-in-sales-invoice"
updated: "2026-03-02"
---


If you have items delivery and invoicing happening at the same time, you can create delivery from with Sales Invoice itself. Sales Invoice has field called **Update Stock**, just before Item table. If this field is checked, on submission of Sales Invoice, stock of Item will be deducted from selected Warehouse.

[Screenshot on the live page: Update Stock via Sales Invoice]

On checking Update Stock, Sales Invoice Item will show relevant fields like Warehouse, Serial No., Batch No., Item valuation etc.

On submission of Sales Invoice, with general ledger posting, stock ledger posting will happen as well.
