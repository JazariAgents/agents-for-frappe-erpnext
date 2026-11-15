<!-- Frappe documentation: erpnext, part 55 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__scrap-management.md -->
---
title: "Production Scrap Management\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/scrap-management"
updated: "2026-03-02"
---


Scrap means waste that either has no economic value or only the value of its basic material content recoverable through recycling.

Scrap is generally availed at the end of the manufacture process. Also you can find some products that are damaged or that are unusable due to expiry or for some other reason, which needs to be scraped.

In ERPNext, at the end of manufacturing process, scrap items are accounted in the scrap warehouses.

## Scrap in Bill of Materials

You can update estimated scrap quantity of an item in the BOM, Scrap table. If required, you can reselect a raw-material item as scrap.

[Screenshot on the live page: Scrap in BOM]

## Scrap in Manufacture Entry

When production is completed, Finish / Manufacture Entry is created against a Production Order. In this entry, scrap item is fetched in the Item table, with only Target Warehouse updated for it. Ensure that Valuation Rate is updated for this item for the accounts posting purposes.

[Screenshot on the live page: Scrap in Manufacture Entry]

> Scrap from the BOM will only work if Manufacture Entry is created based on BOM, and not based on Material Transfer. This is configurable from Manufacturing Settings.

[Screenshot on the live page: Manufacturing Settings]

<!-- page: erpnext/erpnext__scrapping-an-asset.md -->
---
title: "Scrapping an Asset | ERPNext Documentation"
description: "Scrap an unusable ERPNext Asset and verify the write-off, status, and remaining book value."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/scrapping-an-asset"
updated: "2026-08-15"
---

Imagine a Nova Industries machine is damaged beyond repair and has no resale value. It is still shown in the accounts with some remaining value, so simply throwing it away would leave the books saying the company owns something that no longer exists.



Scrapping an Asset closes that gap. ERPNext marks the asset as scrapped, removes its remaining carrying value through the correct accounts, and keeps the disposal history for audit.

## Before you begin

Confirm the Asset is physically retired, approvals are complete, depreciation is current, and the correct loss or disposal account is configured. Scrapping is an accounting action, not a way to hide a missing asset.

## Scrap the Asset

1. Open the submitted Asset.
2. Use the **Scrap Asset** action.
3. Confirm the posting or disposal date.
4. Review the generated Journal Entry before final submission where the workflow allows.
5. Complete the action.

[Screenshot on the live page: Asset status and scrap Journal Entry fields]

## Verify the write-off

The Asset status becomes **Scrapped**. The entry removes the remaining carrying value using the fixed-asset, accumulated depreciation, and loss accounts.

[Screenshot on the live page: Asset balances used to check carrying value before scrapping]

Confirm the Fixed Asset Register no longer treats the asset as active after the disposal date.

[Screenshot on the live page: Fixed Asset Register used after scrapping]

## Troubleshooting

### The Scrap action is unavailable

Confirm the Asset is submitted, not already disposed, and has no blocking draft or submitted lifecycle documents.

### The write-off amount is unexpected

Reconcile capitalized value, booked depreciation, value adjustments, and the disposal date before proceeding.

## Frequently asked questions

### Is scrapping the same as selling for zero?

In ERPNext, no. Scrapping is a write-off workflow without customer proceeds.

### Can a fully depreciated asset be scrapped?

In ERPNext, yes. The remaining carrying value may be only the residual value, but status and disposal history still need to be closed correctly.

### Can a scrapped asset be used again?

Treat scrapping as a final disposal. Reverse only through the supported accounting correction process when the original action was genuinely wrong.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__search-record-by-specific-field.md -->
---
title: "Search Record by Specific Field\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/search-record-by-specific-field"
updated: "2026-03-04"
---


While creating any DocType, you may want to link a particular field to another DocType. For example, in Sales Order DocType, 'Customer' field allows you to select an existing customer. Such fields are called [Link Fields](/erpnext/field-types#link).

Using Link Fields you can create a


Let's assume that you want to see that Item in a Sales Order along with its Item Group. The steps to do this are given below:

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Select the Document for which you want multiple fields to be visible in the Search Field

Here, we will select the Document Item.

#### Step 3: Search Field

Update Warehouse field name in the Search By field.

[Screenshot on the live page: Search By in Customize Form]
[Screenshot on the live page: Search By in Customize Form]

Once these settings have been updated, while creating a Sales Order, when you select the Item, you will also be able to the warehouse there.

[Screenshot on the live page: Search By in Customize Form]

<!-- page: erpnext/erpnext__secondary-items.md -->
---
title: "Secondary Items"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/secondary-items"
updated: "2026-08-26"
---

:::note
**Available only in version 16 of ERPNext**
:::



Starting from version 16, Scrap Items table in the BOM DocType has been renamed to Secondary Items table. The secondary items table now includes items of 3 more types: `Co-Product`, `By-Product` and `Additional Finished Good` . Using this table, users can now specify the distribution of the outgoing cost (or raw material cost) amongst all the outputs based on a percentage system.

Let's first understand the difference between `Scrap`, `Co-Product` , `By-Product` and `Additional Finished Good`.

1. Scrap: An item which is produced alongside the Finished Good which, in most cases, does not have much value.
2. Co-Product: Item produced alongside the main Finished Good which is planned and has significant value.
3. By-Product: This item is produced alongside the finished good which is not planned. This item may or may not have significant value.
4. Additional Finished Good: This item is planned and has significant value. It is usually produced separately from extra materials, leftover capacity or further processing.

In ERPNext, there is virtually no difference on how these secondary items' value and quantity is calculated. The different names are merely for distinction purposes.

You can specify the process loss percentage and cost allocation percentage of each secondary item in the table.

[Screenshot on the live page]

In this example, we are saying that in manufacturing petrol, 10% of the outgoing (raw material) cost should be allocated to LPG and 5% to Bitumen. The remaining 85% will be allocated to the actual finished good (Petrol).

Let's see it in action:

[Screenshot on the live page]

Here, the outgoing cost is Rs. 100. 10% of 100 is 10 which is allocated to LPG and 5% is 5 which is allocated to Bitumen. Since we specified a 5% process loss for Bitumen, it's quantity has been calculated as 9.5 ( `10 - (5% * 10)`).

:::note
**If you are migrating from earlier versions of ERPNext, the scrap items table will stay as it was. The calculations in Manufacture Entry and Subcontracting Receipt will stay the same as it was before migrating.**
:::

<!-- page: erpnext/erpnext__selling-an-asset.md -->
---
title: "Selling an Asset | ERPNext Documentation"
description: "Sell an ERPNext Asset, calculate gain or loss, and verify its disposal and ledger impact."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-an-asset"
updated: "2026-08-15"
---

Imagine Nova Industries sells an old inspection camera for $1,500. The camera originally cost more, but part of that cost has already been recorded as depreciation. The accountant cannot treat the $1,500 like an ordinary product sale because the remaining asset value must also be removed.



Selling an Asset records the customer amount, removes the asset's cost and accumulated depreciation, and calculates the gain or loss. The Asset remains in the register with a **Sold** status so its history is not lost.

## Before you begin

Confirm the Asset is submitted, not already sold or scrapped, and that depreciation is posted up to the disposal date according to policy. Prepare the customer and disposal accounts.

## Create the sale

1. Open the Asset and use **Create &gt; Sales Invoice**, or create a [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice) and select the fixed-asset Item and Asset.
2. Enter the customer, posting date, Asset, quantity, and sale rate.
3. Review taxes and disposal accounts.
4. Submit the Sales Invoice.

[Screenshot on the live page: Asset selected before disposal through a Sales Invoice]

## Verify the disposal

The Asset status becomes **Sold** and its disposal date is recorded. Review the Sales Invoice, Journal Entry or General Ledger to confirm receivable, asset cost, accumulated depreciation, and gain or loss.

[Screenshot on the live page: ERPNext Asset disposal status fields]

Use the Fixed Asset Register to confirm the asset no longer appears as an active existing asset for the relevant date.

[Screenshot on the live page: Fixed Asset Register used to verify disposal]

## Troubleshooting

### The Asset cannot be selected on the Sales Invoice

Confirm the Item is a fixed asset, the Asset is submitted and available, and the company matches.

### Gain or loss looks wrong

Check sale proceeds, disposal date, net book value, booked depreciation, taxes, and selected accounts.

## Frequently asked questions

### Should I create a normal sales item for the asset?

Use the fixed-asset Item and link the specific Asset so ERPNext can perform disposal accounting.

### Does selling cancel the Asset?

In ERPNext, no. It changes lifecycle status to Sold and preserves the history.

### Can I sell a partially depreciated asset?

In ERPNext, yes. Gain or loss is based on sale proceeds versus carrying value at disposal.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__selling-cycle-ledger-impact.md -->
---
title: "Selling Cycle Ledger Impact"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-cycle-ledger-impact"
updated: "2026-08-14"
---

The selling cycle begins with a commercial commitment and ends when the customer pays. Not every document creates an accounting entry. 



A Sales Order records what you have agreed to sell, while Delivery Notes, Sales Invoices, and Payment Entries record the financial events that follow.



The examples below use common account names and exclude sales tax to keep the entries easy to follow. Your account names may differ. ERPNext posts to the accounts configured for your Company, Item, Item Group, warehouse, and transaction.

## Understand when the ledger changes

ERPNext creates General Ledger entries when an accounting or stock transaction is submitted. Saving a draft does not affect the ledger.


| Document                      | Typical ledger impact                                                         | What it represents                                                        |
| ----------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Sales Order                   | No General Ledger entry                                                       | A commitment to supply goods or services at an agreed quantity and price. |
| Delivery Note for stock items | Debit Cost of Goods Sold; credit Stock In Hand                                | The inventory has left the company and its valuation becomes an expense.  |
| Sales Invoice                 | Debit Accounts Receivable; credit Sales. Credit Tax Payable when tax applies. | Revenue is recognized and the customer now owes the invoiced amount.      |
| Payment Entry, Receive        | Debit Bank or Cash; credit Accounts Receivable                                | Money is received and the customer's outstanding balance is reduced.      |


The debit and credit are two sides of the same event. For example, receiving a customer payment increases Bank, so Bank is debited. It also reduces the customer's receivable balance, so Accounts Receivable is credited.

## Example 1: Manufacturing company selling finished goods

Assume a manufacturer sells two finished phones to Cedar Commerce for $699 each, for a total selling price of $1,398. ERPNext values the two finished units at $866.76. The manufacturing costs were accumulated into inventory before this selling cycle began.

### 1. Submit the Sales Order

The submitted Sales Order records the customer's order for two finished phones. It reserves the commercial commitment, but it does not recognize revenue, reduce inventory, or create a receivable.

**Ledger impact:** None.



[Screenshot on the live page: Submitted Sales Order for two finished phones]

### 2. Submit the Delivery Note

The Delivery Note confirms that the finished goods have left the warehouse. ERPNext removes their current valuation from the stock asset and recognizes that valuation as the cost of the sale.


| Account            | Debit   | Credit  | Explanation                                           |
| ------------------ | -------: | -------: | ----------------------------------------------------- |
| Cost of Goods Sold | $866.76 |         | The inventory cost becomes an expense.                |
| Stock In Hand      |         | $866.76 | The value of inventory held by the company decreases. |


[Screenshot on the live page: General Ledger entries created by the Delivery Note]

The debit is based on valuation, not the customer selling price. That is why the Delivery Note posts $866.76 even though the customer will be invoiced $1,398.

### 3. Submit the Sales Invoice

The Sales Invoice recognizes revenue and creates the amount due from the customer.


| Account                       | Debit     | Credit    | Explanation                          |
| ----------------------------- | ---------: | ---------: | ------------------------------------ |
| Accounts Receivable (Debtors) | $1,398.00 |           | The customer now owes the company.   |
| Sales                         |           | $1,398.00 | Revenue from the sale is recognized. |


[Screenshot on the live page: General Ledger entries created by the goods Sales Invoice]

Ignoring tax and other costs, the gross profit visible from these two events is $531.24: sales of $1,398.00 less cost of goods sold of $866.76.

### 4. Receive the customer payment

When the customer pays the full invoice, submit a Receive-type Payment Entry and allocate it to the Sales Invoice.


| Account                       | Debit     | Credit    | Explanation                                 |
| ----------------------------- | ---------: | ---------: | ------------------------------------------- |
| Bank                          | $1,398.00 |           | Money received increases the bank balance.  |
| Accounts Receivable (Debtors) |           | $1,398.00 | The amount owed by the customer is cleared. |


[Screenshot on the live page: General Ledger entries created by the customer Payment Entry]

The Payment Entry does not recognize sales income again. The Sales Invoice already recorded the income. The payment only moves the balance from Accounts Receivable to Bank.

## Example 2: Services company

Assume a service company agrees to perform 20 device-setup sessions for Bluewave Systems at $150 each. The total contract value is $3,000.

Services do not normally move inventory, so this workflow can go directly from Sales Order to Sales Invoice and Payment Entry. A Delivery Note is unnecessary unless the company uses it as an operational confirmation of service delivery.

### 1. Submit the Sales Order

The Sales Order records the agreed scope, quantity, rate, and delivery date. It does not create revenue or a receivable.

**Ledger impact:** None.



[Screenshot on the live page: Submitted Sales Order for device setup services]

### 2. Submit the Sales Invoice

After completing the agreed work, submit the Sales Invoice. Because the Item is a non-stock service, no Stock In Hand or Cost of Goods Sold entry is created by this invoice.


| Account                       | Debit     | Credit    | Explanation                                 |
| ----------------------------- | ---------: | ---------: | ------------------------------------------- |
| Accounts Receivable (Debtors) | $3,000.00 |           | The customer owes the invoiced service fee. |
| Sales or Service Income       |           | $3,000.00 | Service revenue is recognized.              |


[Screenshot on the live page: General Ledger entries created by the service Sales Invoice]

Employee costs, contractor charges, travel, and other delivery expenses are recorded through their own payroll, expense, purchase, or journal workflows. They are not automatically posted as Cost of Goods Sold merely because a service Sales Invoice is submitted.

### 3. Receive the customer payment

The Payment Entry has the same basic effect as it does for a goods sale.


| Account                       | Debit     | Credit    | Explanation                                    |
| ----------------------------- | ---------: | ---------: | ---------------------------------------------- |
| Bank                          | $3,000.00 |           | The company's bank balance increases.          |
| Accounts Receivable (Debtors) |           | $3,000.00 | The customer's outstanding balance is cleared. |


[Screenshot on the live page: General Ledger entries created by the service Payment Entry]

## Compare the two workflows


| Stage       | Manufacturing or stock goods                                      | Services                                                       |
| ----------- | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| Sales Order | No ledger impact                                                  | No ledger impact                                               |
| Delivery    | Delivery Note reduces Stock In Hand and debits Cost of Goods Sold | Usually no stock Delivery Note or stock posting                |
| Invoice     | Debits Accounts Receivable and credits Sales                      | Debits Accounts Receivable and credits Sales or Service Income |
| Payment     | Debits Bank and credits Accounts Receivable                       | Debits Bank and credits Accounts Receivable                    |


If a stock-item Sales Invoice is submitted with **Update Stock** enabled, ERPNext combines the stock effect of the Delivery Note with the revenue and receivable effect of the Sales Invoice. The result is valid, but the company loses a separate delivery document in the audit trail.

If users create a Sales Invoice directly without a Sales Order, the Sales Invoice still creates the same ledger entries. What is missing is the earlier commercial commitment, order tracking, and link between ordered and billed quantities.

## Frequently asked questions

### Does submitting a Sales Order affect the General Ledger?

A Sales Order is a commercial commitment. It can influence order, delivery, reservation, and billing reports, but it does not create debit or credit entries.

### Why is Cost of Goods Sold different from the selling price?

Cost of Goods Sold uses the item's stock valuation. Sales uses the price charged to the customer. The difference contributes to gross profit.

### What changes when sales tax is included?

Accounts Receivable is debited for the full invoice total. Sales is credited for the net revenue, and the applicable tax liability account is credited for the tax collected from the customer.

### Can a services company use a Delivery Note?

Yes, if it wants a separate operational record confirming service delivery. A non-stock service Delivery Note does not reduce Stock In Hand. Many service companies invoice directly from the Sales Order instead.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)
- [Selling cycle](/erpnext/selling)

<!-- page: erpnext/erpnext__Selling-in-different-UOM.md -->
---
title: "Sell Items in Different Units of Measure | ERPNext Documentation"
description: "Configure ERPNext UOM conversions, UOM-specific Item Prices, and sales transaction quantities for packs, cartons, units, and fractional measures."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/Selling-in-different-UOM"
updated: "2026-07-25"
---

ERPNext can sell the same Item in different Units of Measure while maintaining stock in one Stock UOM. Configure each allowed UOM and conversion factor on the Item, then select the selling UOM in a transaction.

## Before you begin

Confirm:

- The required [Units of Measure](/erpnext/unit-of-measure-uom).
- The Item's Stock UOM.
- Accurate conversion factors.
- UOM-specific [Item Prices](/erpnext/item-price) or a conversion-based pricing policy.
- Whether fractional quantities are allowed.

Changing a conversion factor affects how transaction quantity translates into stock quantity. Test it before use.

## Add an alternative UOM to an Item

1. Open the [Item](/erpnext/item).
2. Confirm the Stock UOM.
3. In the **UOMs** table, add the selling UOM.
4. Enter the Conversion Factor relative to one Stock UOM.
5. Save.

[Screenshot on the live page: The UOM conversion table on an Item.]

Example: if one Carton contains 10 Units and Unit is the Stock UOM, set the Carton conversion factor to 10.

## Create UOM-specific prices

Create one Item Price for each deliberately priced UOM:

1. Open Item Price.
2. Select the Item and selling Price List.
3. Select the UOM.
4. Enter the Rate.
5. Save.

[Screenshot on the live page: Item Prices for an Item and Price List.]

Use separate prices when a carton has a negotiated price rather than exactly ten times the unit price.

Alternatively, enable **Price Not UOM Dependent** on the [Price List](/erpnext/price-lists) when ERPNext should derive the alternate-UOM price using the conversion factor.

## Sell in an alternative UOM

1. Create a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice).
2. Add the Item.
3. Select the highlighted pencil icon to open the complete row editor.
4. Select the UOM.
5. Confirm the Conversion Factor, Quantity, Stock Qty, and Rate.
6. Save or submit.

[Screenshot on the live page: The Sales Order Items table where the transaction UOM is selected.]

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## Understand transaction and stock quantities

If one Carton equals 10 Units:


| Transaction value | Result   |
| ----------------- | -------- |
| UOM               | Carton   |
| Qty               | 3        |
| Conversion Factor | 10       |
| Stock Qty         | 30 Units |


Inventory reports and stock ledgers use the Stock UOM. The sales document can display the selected selling UOM.

## Fractional quantities

Use fractional quantities only when the UOM and Item allow them. For example, a service can be billed as 1.5 Hours, while a serialized laptop cannot usually be sold as 0.5 Unit.

Review UOM **Must be Whole Number** behavior and Item serialization or batching requirements.

## Troubleshooting


| Problem                                       | What to check                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| Alternative UOM is unavailable                | Add it to the Item's UOM table and save                                     |
| Stock Qty is incorrect                        | Correct the conversion factor                                               |
| No rate is fetched                            | Create an Item Price for the selected UOM or review Price Not UOM Dependent |
| Fractional quantity is rejected               | Check the UOM whole-number setting and Item constraints                     |
| Delivered stock differs from ordered quantity | Compare transaction Qty, UOM, Conversion Factor, and Stock Qty              |


## Frequently asked questions

### Can I keep stock in cartons and sell in units?

Yes. Choose the most appropriate Stock UOM and define the reciprocal business conversion accurately.

### Do I need a separate Item Price for every UOM?

Use separate Item Prices for deliberate UOM pricing. Use Price Not UOM Dependent for conversion-based pricing.

### Can the UOM change after submission?

Submitted stock and sales quantities should not be reinterpreted. Use the supported amendment or return workflow.

### Which quantity appears in the stock ledger?

Stock Qty in the Item's Stock UOM.

## Related topics

- [Unit of Measure](/erpnext/unit-of-measure-uom)
- [Item](/erpnext/item)
- [Item Price](/erpnext/item-price)
- [Price Lists](/erpnext/price-lists)
- [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__selling-settings.md -->
---
title: "Selling Settings | ERPNext Documentation"
description: "Configure ERPNext Selling Settings for customer defaults, pricing, transaction rules, commissions, subcontracting, and document naming."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-settings"
updated: "2026-08-25"
---

Selling Settings controls the defaults and validations used across the ERPNext sales cycle. These settings affect customers, pricing, quotations, sales orders, delivery notes, sales invoices, returns, commissions, and document naming.

Review the settings with your sales, fulfilment, and finance teams before enabling them. A validation that improves control for one business can interrupt a different sales process.

## Before you begin

- You need permission to edit Selling Settings.
- Create the required [Customer Groups](/erpnext/customer-group), [Territories](/erpnext/territory), and [Price Lists](/erpnext/price-list) first.
- Test changes with representative transactions before applying them to production users.

To open the page, go to **Selling &gt; Settings &gt; Selling Settings**. Settings are organized into six tabs. Select **Save** after making changes.

## Customer Defaults

Customer defaults reduce data entry when creating a [Customer](/erpnext/customer) or converting a Lead or Quotation into a Customer.



[Screenshot on the live page: Customer Defaults tab in ERPNext Selling Settings]


| Field                  | What it means                                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Naming By     | Choose Customer Name, Naming Series, or Auto Name for the customer ID. Customer Name is the default. Naming Series produces IDs such as CUST-00001.                   |
| Default Customer Group | Sets the Customer Group on new customers when another value is not provided. It is also used when ERPNext creates a Customer while converting a Lead-based Quotation. |
| Default Territory      | Sets the Territory on new customers and supports automatic Customer creation from a Lead-based Quotation.                                                             |


If Default Customer Group or Default Territory is blank, automatic conversion can stop and ask for the missing value.

## Pricing

The Pricing tab determines how ERPNext fetches and validates item rates throughout the sales cycle.



[Screenshot on the live page: Pricing tab in ERPNext Selling Settings]


| Field                                                     | What it means                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default Price List                                        | Provides the default selling Price List for a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), Delivery Note, and Sales Invoice.                                                                                                                           |
| Use prices from Default Price List as fallback            | Fetches an Item Price from the default Price List when the transaction’s selected Price List has no matching Item Price. Do not combine it with automatic insertion of missing Item Prices in Stock Settings, because a fallback rate could be written into another Price List. |
| Allow editing Price List rate in transactions             | Makes Price List Rate editable in sales item tables. Keep it disabled when rates must always come from [Item Price](/erpnext/item-price) records.                                                                                                                               |
| Maintain same rate throughout sales cycle                 | Checks whether an item rate changes in a Delivery Note or Sales Invoice created from a Sales Order.                                                                                                                                                                             |
| Action if same rate is not maintained                     | Appears after maintaining the same rate is enabled. Warn allows the transaction after showing a message. Stop prevents the change.                                                                                                                                              |
| Role allowed to override Stop action                      | Appears when the action is Stop. Users with the selected role can override the validation.                                                                                                                                                                                      |
| Validate selling price against purchase or valuation rate | Blocks a sale when the selling rate is below the relevant purchase or valuation rate. Test this carefully for promotions and clearance items.                                                                                                                                   |
| Calculate Product Bundle price based on child Item rates  | Makes packed-item rates editable and calculates the [Product Bundle](/erpnext/product-bundle) price from its child items. A manually changed bundle rate is recalculated when the document is saved.                                                                            |
| Allow negative rates for Items                            | Permits negative item rates for supported adjustments, refunds, returns, or special pricing. Use this only with appropriate accounting review.                                                                                                                                  |


## Transaction

Transaction settings define which documents are required and which exceptions users may use.



[Screenshot on the live page: Transaction tab in ERPNext Selling Settings]


| Field                                                             | What it means                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Is Sales Order required to create Sales Invoice or Delivery Note? | Set to Yes to require a Sales Order before a [Sales Invoice](/erpnext/sales-invoice) or [Delivery Note](/erpnext/delivery-note). A Customer can allow Sales Invoice creation without a Sales Order as an exception. |
| Is Delivery Note required to create Sales Invoice?                | Set to Yes to require a Delivery Note before invoicing. A Customer can allow invoicing without a Delivery Note as an exception.                                                                                     |
| How often should sales data be updated in Company or Project?     | Choose Each Transaction, Daily, or Monthly. Daily or Monthly can reduce repeated updates on sites with a high transaction volume.                                                                                   |
| Allow same Item to be added multiple times                        | Allows the same item on more than one row of a transaction. Disable it when duplicate lines are usually an error.                                                                                                   |
| Allow multiple Sales Orders against a customer’s Purchase Order   | Allows several Sales Orders to use the same customer purchase order number and date.                                                                                                                                |
| Hide Customer’s Tax ID from sales transactions                    | Stops the Customer Tax ID from appearing in selling transactions when your process does not require it.                                                                                                             |
| Allow Sales Order creation for expired Quotation                  | Allows an expired Quotation to be converted. Users should still confirm that the rate and terms remain valid.                                                                                                       |
| Don’t reserve Sales Order qty on sales return                     | Prevents a return from automatically reserving quantity against the linked Sales Order.                                                                                                                             |
| Enable cut-off date on creating bulk Delivery Notes               | Adds a cut-off date to bulk Delivery Note creation so only eligible Sales Orders up to that date are processed.                                                                                                     |
| Set incoming rate as zero for expired Batch                       | Sets the incoming rate to zero for a stand-alone credit note containing an item from an expired Batch.                                                                                                              |
| Allow Quotation with zero quantity                                | Allows zero-quantity lines when the rate is agreed before the quantity, such as a rate contract.                                                                                                                    |
| Allow Sales Order with zero quantity                              | Allows zero-quantity Sales Order lines for a similar rate-contract workflow.                                                                                                                                        |
| Blanket Order Allowance (%)                                       | Controls how much a Sales Order may exceed the quantity agreed in a [Blanket Order](/erpnext/blanket-order).                                                                                                        |


## **Skip Delivery Note Creation for Service Items**

[Screenshot on the live page]

Sales Orders that contain services no longer wait for a delivery that will never happen. When this setting is on, non-stock items are excluded from delivery tracking, and an order made up entirely of them completes as soon as it is fully billed.

### The problem it solves

A Sales Order for services — consulting, installation, an AMC — has nothing to deliver. Without this feature the order still expects a Delivery Note, so after billing it sits at **To Deliver** and eventually shows as **Overdue**, even though the work is done and paid for.

### Enabling it

> **Selling Settings → Skip Delivery Note for Service Items**

The switch applies to all order types — Sales, Maintenance, and Shopping Cart alike. No per-order checkbox is needed; each order works it out from its items.

### How items qualify

Every time a Sales Order is saved, each item row is marked with a hidden `Skip Delivery` flag. A row is exempt from delivery only when **all** of these hold:

- the item is not a stock item
- the item is not a fixed asset
- the item is not a Product Bundle that contains stock items
- the row is not delivered by the supplier (drop shipping)

Anything failing a check keeps normal delivery tracking. The flags refresh on every save — including **Update Items** on a submitted order — so changing the item mix or the setting is always reflected.

### Order status

When every row on the order is exempt, the order needs no delivery at all: **% Delivered** is set to 100 and the delivery status shows **Not Applicable**.

```
To Bill  →  (Sales Invoice for the full amount)  →  Completed
```

On a mixed order, only the deliverable rows count toward **% Delivered**, and the Delivery Note picks up only those rows. The order completes once the stock items are delivered and everything is billed.

### Examples


| Order contents         | Delivery Note   | Completed when                        |
| ---------------------- | --------------- | ------------------------------------- |
| Services only          | Not required    | Fully billed                          |
| Stock items + services | Stock rows only | Stock rows delivered and fully billed |
| Setting disabled       | All rows        | Fully delivered and fully billed      |


## Advanced Features

Use these settings when your implementation requires commission tracking, separate discount accounting, or campaign attribution.



[Screenshot on the live page: Advanced Features tab in ERPNext Selling Settings]


| Field                                  | What it means                                                                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Enable tracking sales commissions      | Enables commission management for Sales Partners and the sales team.                                                                      |
| Enable discount accounting for selling | Creates additional ledger entries to post discounts to a separate Discount Account.                                                       |
| Enable UTM                             | Adds UTM attribution fields to supported documents including Lead, Quotation, Sales Order, Delivery Note, Sales Invoice, and POS Invoice. |
| Use Legacy (Client side) Reactivity    | An experimental compatibility option. Keep the default unless a tested customization requires the legacy behavior.                        |


## Subcontracting Inward

These controls apply when your company receives materials from a customer, processes them, and delivers finished goods back to that customer.



[Screenshot on the live page: Subcontracting Inward tab in ERPNext Selling Settings]


| Field                                   | What it means                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Allow delivery of overproduced quantity | Allows the entire produced quantity to be delivered even when it exceeds the Subcontracting Inward Order quantity. |
| Deliver secondary Items                 | Adds secondary items generated with a finished good to the Stock Entry used for delivery.                          |


## Document Naming

This tab shows the current naming series for Quotation, Sales Order, Sales Invoice, and Delivery Note, including separate return series where applicable.



[Screenshot on the live page: Document Naming tab in ERPNext Selling Settings]

Configure or extend naming series according to your company’s document-control policy. Avoid changing an active series without checking reporting, integrations, and print formats.

## Frequently asked questions

### Can I require a Sales Order for most customers but allow exceptions?

Y

es. Set the global requirement in Selling Settings, then use the relevant exception on the Customer record for approved cases.

### Why are some pricing fields not visible?

Action and override-role fields appear only after Maintain same rate throughout sales cycle is enabled. The override role is relevant when the selected action is Stop.

### Should I allow users to edit Price List Rate?

Enable it only when users are authorized to depart from maintained Item Prices. Otherwise, keep the field controlled and use Pricing Rules for repeatable exceptions.

### When should zero-quantity transactions be allowed?

Use them for rate contracts or agreements where the unit rate is confirmed before the final quantity. They should not replace quantities in normal orders.

### What should I test after changing Selling Settings?

Create a test Customer, Quotation, Sales Order, Delivery Note, Sales Invoice, and return that reflect your normal and exception workflows. Confirm rates, document links, accounting entries, and permissions before production use.
