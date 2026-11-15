<!-- Frappe documentation: erpnext, part 48 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__purchase-taxes-and-charges-template.md -->
---
title: "Purchase Taxes and Charges Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template"
updated: "2026-08-14"
---

A Purchase Taxes and Charges Template is a reusable set of tax and charge rows for buying transactions. Use it for input tax, duties, freight, insurance, handling, or another cost that should affect the supplier total, item valuation, or both.



The template can be used on Requests for Quotation, Supplier Quotations, Purchase Orders, Purchase Receipts, and Purchase Invoices where the field is available. Selecting it copies the rows into the transaction and calculates them from the actual items and quantities.



Purchase templates require one decision that sales templates normally do not: whether a cost affects only the amount payable to the supplier, only stock valuation, or both.

## Before you begin

Create the required accounts in the [Chart of Accounts](/erpnext/chart-of-accounts). An input tax account should normally have **Account Type** set to **Tax**. A freight or duty row used in item valuation may use an account whose type and accounting treatment are appropriate for expenses included in valuation.

Confirm whether the supplier price is tax-exclusive or tax-inclusive. Identify known landed costs that should be included during the purchase transaction and costs that will be added later through a [Landed Cost Voucher](/erpnext/landed-cost-voucher). Recording the same cost in both places will double-count it.

Create a [Tax Category](/erpnext/tax-category) when the template represents a specific purchase treatment. A [Tax Rule](/erpnext/tax-rule) can select the template from the supplier, address, category, item, date, company, and priority.

## Create a Purchase Taxes and Charges Template

Go to **Accounting &gt; Taxes &gt; Purchase Taxes and Charges Template** and select **Add Purchase Taxes and Charges Template**.

1. Enter a clear **Title**, such as `Nova Standard Purchase Tax 5%`.
2. Select the **Company**.
3. Select the applicable **Tax Category**, when used.
4. Enable **Default** only when this is the normal template for new buying transactions for the company.
5. Add a row under **Purchase Taxes and Charges**.
6. Open the row with the pencil icon.
7. Configure its valuation treatment, add or deduct direction, calculation type, account, rate, and description.
8. Add dependent rows in their intended calculation order.
9. Save.

[Screenshot on the live page: Purchase tax template title, company, and Tax Category]

Use **Disabled** to stop new selection while preserving transactions that already reference the template.

## Open and configure a row

The table provides a compact view of the formulas. Use the pencil icon to open fields that do not fit in the grid.



[Screenshot on the live page: Open a Purchase Taxes and Charges row]

Set the calculation type, account, and rate. The row values remain zero on the master because Net Amount, Amount, and Total are calculated only in a transaction.



[Screenshot on the live page: Purchase tax calculation type, account, and rate]

## Decide whether the row affects Total, Valuation, or both

The **Consider Tax or Charge for** field controls the accounting purpose of the row:


| Value               | Supplier total                    | Item valuation                              | Typical use                                                         |
| ------------------- | --------------------------------- | ------------------------------------------- | ------------------------------------------------------------------- |
| Total               | Affects the amount payable        | Does not allocate the cost into stock value | Recoverable input tax or a charge billed without capitalization     |
| Valuation           | Does not affect the payable total | Allocates the cost into item valuation      | A known cost capitalized separately from the supplier invoice total |
| Valuation and Total | Affects the amount payable        | Also allocates the cost into item valuation | Freight or duty billed by the supplier and capitalized into stock   |


The correct choice depends on whether the amount is recoverable, expensed, capitalized, and included in what you owe the supplier. Verify the expected debit and credit entries on a small submitted example.

Use **Add or Deduct** to determine whether the row increases or reduces the relevant base.



[Screenshot on the live page: Purchase valuation, add or deduct, description, and inclusive pricing]

For example, a recoverable input tax normally affects **Total** because it is part of the supplier payable but is posted to an input tax asset rather than added to stock value. Known inbound freight can use **Valuation and Total** when it is charged by the supplier and should increase both payable and item value.

## Important row fields and what they mean


| Field                               | What it controls                                                                        |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| Consider Tax or Charge for          | Whether the row affects the supplier Total, item Valuation, or both                     |
| Add or Deduct                       | Whether the row increases or reduces the selected base                                  |
| Type                                | The calculation base, such as Net Total, fixed amount, previous row, or quantity        |
| Account Head                        | The ledger account to which the row posts                                               |
| Description                         | The explanation that can appear in the purchase document                                |
| Tax Rate                            | The percentage or per-unit amount used by the selected Type                             |
| Tax Amount                          | The fixed amount used when Type is Actual                                               |
| Reference Row #                     | The earlier row used by a previous-row calculation                                      |
| Is this Tax included in Basic Rate? | Back-calculates net value when the entered supplier price already includes the tax      |
| Considered In Paid Amount           | Treats the row as included in the paid amount for supported payment behavior            |
| Is Tax Withholding Account          | Identifies a withholding-account row when the withholding workflow uses it              |
| Cost Center                         | Allocates an income or expense charge when required by the account and reporting design |


## Choose the calculation type

Purchase and sales templates use the same five Types:


| Type                   | Calculation                                           | Common purchase use                                    |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| Actual                 | A fixed amount entered directly                       | Fixed freight, customs handling, or documentation fee  |
| On Net Total           | Net Total multiplied by Tax Rate                      | Standard input tax on purchased items                  |
| On Previous Row Amount | An earlier row's Amount multiplied by Tax Rate        | A levy calculated only on another duty or tax          |
| On Previous Row Total  | An earlier row's running Total multiplied by Tax Rate | A levy calculated on the subtotal after an earlier row |
| On Item Quantity       | Total quantity multiplied by the entered rate         | A fixed charge per unit                                |


See [Types in Tax Template](/erpnext/types-in-tax-template) for worked examples. For either previous-row type, set **Reference Row #** and keep the referenced row earlier in the table.

## Include known freight or duty in valuation

When a freight or duty amount is known while creating the Purchase Order, Purchase Receipt, or Purchase Invoice, add it in the purchase tax table and select the appropriate valuation treatment.

Use **Valuation and Total** when the supplier bills the amount and it should increase both payable and stock value. Use **Valuation** when it should affect stock value without changing that document's payable.

Use a [Landed Cost Voucher](/erpnext/landed-cost-voucher) when costs become known after receipt, are billed by another party, or must be allocated later. Never record the same freight in both places.

Valuation rows matter only for stock items and stock-impacting transactions. A service Purchase Invoice can still use Total rows for input tax or charges, but there is no stock value to increase.

## Configure inclusive supplier prices

Enable **Is this Tax included in Basic Rate?** when the supplier's item rate already includes the tax. ERPNext back-calculates the net amount and tax instead of adding the tax again.

For an entered rate of $105 that includes 5% input tax, the net amount is $100 and tax is $5. Review the Item table's Net Rate, the tax row, and the Grand Total to confirm the back-calculation.

The inclusive setting belongs to the transaction tax row. An [Item Tax Template](/erpnext/item-tax-template) can override an item's rate, but it follows the matching row's inclusive or exclusive behavior.

## Use the template on a purchase transaction

Create a draft [Purchase Invoice](/erpnext/purchase-invoice), Purchase Order, or Purchase Receipt.

1. Select the company, supplier, and supplier address.
2. Confirm the Tax Category and Purchase Taxes and Charges Template.
3. Add representative stock and service items.
4. Review each row's valuation purpose, Add or Deduct choice, Type, account, and rate.
5. Check Net Total, Total Taxes and Charges, Grand Total, and valuation impact.
6. Submit only after the payable and stock values agree with the supplier document and accounting policy.

In this example, a 5% input-tax row calculates $26 on a $520 net purchase, creating a Grand Total and supplier outstanding amount of $546.



[Screenshot on the live page: Purchase tax and Grand Total result]

For a submitted Purchase Invoice, review the [General Ledger](/erpnext/general-ledger). A recoverable input tax normally debits the input tax asset, the purchased stock or expense debits the relevant account, and the supplier payable is credited for the Grand Total.

## Apply different item rates

Use Item Tax Templates when individual items require rates different from the standard purchase template. The Item Tax Template and transaction tax row must use the same Account Head, and their Tax Categories and validity dates must match the transaction context.

On a Purchase Invoice, Supplier Invoice Date has priority over Posting Date when ERPNext selects a valid item assignment. This supports supplier invoices dated before a rate change but entered later.

## Regional selection

Regional apps can add country-specific fields. India localization, for example, can use **Is Inter State** and address or place-of-supply information to distinguish tax templates. Such behavior is not universal.

Follow the installed localization's documentation and validate tax identifiers, addresses, place of supply, and invoice type. Keep country-neutral templates free of inapplicable regional assumptions.

## Troubleshooting

### Freight did not increase item valuation

Check **Consider Tax or Charge for**. A row set to Total affects the payable but not stock value. Confirm that the transaction affects stock and that the selected account and valuation policy are appropriate.

### The payable total is wrong

Review Add or Deduct, inclusive pricing, fixed Amount rows, and any previous-row references. Compare the supplier's net, tax, freight, and total values line by line.

### The input tax posts to the wrong account

Check Account Head in the copied transaction row, not only in the master. Confirm that the account belongs to the correct company and has the intended account type and reporting treatment.

### An Item Tax Template is ignored

Confirm the matching tax account, Tax Category, assignment validity, and Supplier Invoice Date. Reselect the transaction template or re-add the affected item after changing tax context.

## Frequently asked questions

### Should recoverable input tax be included in stock valuation?

Normally recoverable input tax is recorded separately rather than capitalized into stock, but the correct treatment depends on local law and your accounting policy. Configure and validate it with your accountant.

### When should I use a Landed Cost Voucher instead of the template?

Use the purchase tax table for known costs included in or associated with the transaction. Use a Landed Cost Voucher for later or separately billed costs that must be allocated to received stock.

### Can a Purchase Order and Purchase Invoice use different tax rows?

Yes, but differences should reflect the supplier document or a real change. Review copied rows carefully when creating the invoice from an order or receipt.

### Why are the template's calculated Amount columns zero?

The master stores reusable formulas. Amounts are calculated after the rows are copied into a transaction containing item values and quantities.

### Can one template handle both purchases and sales?

1. Use Purchase Taxes and Charges Templates for buying transactions and Sales Taxes and Charges Templates for selling transactions because their document contexts and valuation behavior differ.

## Related topics

- [Taxes](/erpnext/taxes)
- [Types in Tax Template](/erpnext/types-in-tax-template)
- [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)
- [Include Tax or Charge in Valuation or Total?](/erpnext/include-tax-or-charge-in-valuation-or-total)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Purchase Order](/erpnext/purchase-order)

<!-- page: erpnext/erpnext__purchase-transactions.md -->
---
title: "Purchase Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-transactions"
updated: "2026-02-26"
---

Purchase transactions in ERPNext encompass the various activities involved in acquiring goods or services from suppliers.

These transactions typically include creating purchase orders to specify the items or services needed, receiving goods against these orders to update inventory levels, and processing purchase invoices for payment. Additionally, ERPNext facilitates communication with suppliers, tracks purchase history, and integrates with accounting modules for seamless financial management.

* [Material Request](/erpnext/user/manual/en/material-request)
* [Purchase Order](/erpnext/user/manual/en/purchase-order)
* [Purchase Invoice](/erpnext/user/manual/en/purchase-invoice)
* [Debit Note](/erpnext/user/manual/en/debit-note)
* [Request for Quotation](/erpnext/user/manual/en/request-for-quotation)
* [Supplier Quotation](/erpnext/user/manual/en/supplier-quotation)
* [Supplier Quotation Through Portal](/erpnext/user/manual/en/how-to-create-a-supplier-quotation-through-the-supplier-portal)
* [Purchase Return](/erpnext/user/manual/en/purchase-return)

<!-- page: erpnext/erpnext__purchasing-an-asset.md -->
---
title: "Purchasing an Asset | ERPNext Documentation"
description: "Purchase and capitalize fixed assets in ERPNext using correctly configured Items, Purchase Receipts, and Purchase Invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchasing-an-asset"
updated: "2026-08-15"
---

Let's say you're recording two purchases for Nova Industries: 50 phones that will be sold to customers and one packaging machine that the company will use for five years. The phones should increase inventory. The machine should become a fixed asset and its cost should be spread across the years in which it is used.



ERPNext handles this difference from the Item setup onward. When the machine is marked as a fixed asset and purchased correctly, ERPNext can create its Asset record, place its cost in the right account, and prepare its depreciation schedule.

## Before you begin

Create the [Asset Category](https://docs.frappe.io/erpnext/asset-category), its accounts, the [Asset Location](https://docs.frappe.io/erpnext/asset-location), the supplier, and a fixed-asset Item.

## Mark the Item as a fixed asset

1. Open or create the Item.
2. Enable **Is Fixed Asset**.
3. Select the Asset Category.
4. Enable **Auto Create Assets on Purchase** when every purchased unit should create an Asset automatically. Leave it disabled when the asset must be created or grouped manually.

[Screenshot on the live page: ERPNext Item marked as a fixed asset with an Asset Category]

## Record the purchase

1. Create a [Purchase Invoice](https://docs.frappe.io/erpnext/purchase-invoice) or a [Purchase Receipt](https://docs.frappe.io/erpnext/purchase-receipt) for the fixed-asset Item.
2. Select the correct company and supplier.
3. Enter quantity, rate, and the intended asset location.
4. Submit the document. If auto creation is enabled, open the created Asset from the document links.
5. If auto creation is disabled, create the Asset and link the source purchase document.

## Review the Asset before submission

Check the location, purchase date, available-for-use date, quantity, net purchase amount, and depreciation settings. The Available for Use Date determines when depreciation can start.

[Screenshot on the live page: Purchased Asset details and depreciation controls in ERPNext]

Review each Finance Book row before submission. The row is the source of the schedule for that reporting basis.

[Screenshot on the live page: Finance Book rows on an ERPNext Asset]

## What happens after submission

The Asset becomes part of the fixed-asset register. When CWIP accounting is enabled, ERPNext can move value from Capital Work in Progress to the Fixed Asset Account when the asset is capitalized or becomes available for use. Depreciation entries follow the active schedule rather than the purchase date alone.

## Troubleshooting

### The purchase posts to an expense or inventory account

Check **Is Fixed Asset**, the selected Asset Category, and the category's company accounts before submission.

### No Asset was created from the purchase

Check **Auto Create Assets on Purchase** on the Item. If it was intentionally disabled, create the Asset manually and preserve the purchase link.

### The depreciation schedule starts on the wrong date

Correct the Available for Use Date and Finance Book start date while the relevant records are still editable.

## Frequently asked questions

### Should I use Purchase Receipt or Purchase Invoice?

Use the document that matches your control flow. A Purchase Receipt proves physical receipt; a Purchase Invoice records the supplier liability. Some organizations use both.

### Can one purchase create multiple Assets?

In ERPNext, yes. Quantity and grouped-asset settings determine whether ERPNext creates individual assets or a grouped asset.

### Can I enter an asset already owned before ERPNext?

In ERPNext, yes. Create an [existing Asset](https://docs.frappe.io/erpnext/asset) and provide purchase value, opening accumulated depreciation, and booked depreciation count.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__purchasing-in-different-unit.md -->
---
title: "Purchasing in Different UoM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchasing-in-different-unit"
updated: "2026-03-02"
---

Each item has a stock unit of measurement (UoM) associated with it. For example, the UoM of pen could be numbers (Nos) and sand could be stocked kg. However, when we place an order with a supplier, the UoM for an item could change. Like we can order 1 set/box of pens, or one truck of sand to our supplier. When creating a purchase transaction, you can change Purchase UoM for an item.

Scenario:

Item Pen is stocked in Nos, but purchased in Box. Hence, we will make a Purchase Order for a Pen in a box.

#### Step 1: Edit UoM in the Purchase Order

In the Purchase Order, you will find two UoM fied.

* UoM
* Stock UoM

  
In both fields, the default UoM of an item will be fetched by default. You should edit UoM field, and select Purchase UoM (Box in this case). Updating Purchase UoM is mainly for the reference of the supplier. In the print format, you will see item qty in the Purchase UoM.

[Screenshot on the live page: Item Purchase UoM]  


#### Step 2: Update UoM Conversion Factors

In one Box, if you get 20 Nos. of Pen, UoM Conversion Factor will be 20.

[Screenshot on the live page: Item Conversion Factor]  


Based on the Qty and Conversion Factor, qty will be calculated in the Stock UoM of an item. If you purchase just one Box, then the Qty in the stock UoM will be set as 20.

[Screenshot on the live page: Purchase Qty in Default UoM]  


### Stock Ledger Posting

Irrespective of the Purchase UoM selected, stock ledger posting will be done in the Default UoM of an item. Hence, you should ensure that the conversion factor is entered correctly while purchasing an item in a different UoM.

[Screenshot on the live page: Print Format in Purchase UoM]  


### Set Conversion Factor in Item

In the Item master, under the Purchase section, you can list all the possible UOM purchases of an item, with its UoM Conversion Factor.

[Screenshot on the live page: Purchase UoM master]  

<!-- page: erpnext/erpnext__purpose-of-stock-delivered-but-not-billed.md -->
---
title: "Purpose of Stock Delivered But Not Billed"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purpose-of-stock-delivered-but-not-billed"
updated: "2026-07-02"
---

## Stock Delivered but Not Billed

The **Stock Delivered but Not Billed** account is an adjustment account used to record the value of delivered items before a bill has been raised. Rather than debiting an expense account directly at the time of delivery, the system routes the entry through this intermediate account to keep the sales cycle accounting clean and consistent.

The balance in this account at any point represents the value of items for which Delivery Notes have been submitted, but Sales Invoices have not yet been raised.

### How It Works

[Screenshot on the live page]



**On Delivery Note submission:** The warehouse's **Stock In Hand** account is credited, and the full stock value is debited to the **Stock Delivered but Not Billed** account.

*Example: A Delivery Note worth ₹400 → Stock In Hand credited ₹400, Stock Delivered but Not Billed debited ₹400.*

**On Sales Invoice submission:** The **Stock Delivered but Not Billed** account is credited as a reversal, and the **Cost of Goods Sold (COGS)** account is debited for the same amount.

*Example: Sales Invoice raised for ₹400 → Stock Delivered but Not Billed credited ₹400, COGS debited ₹400.*

[Screenshot on the live page]

### Configuration

- The Stock Delivered but Not Billed account can be configured at the **Company** level using **Enable Stock Delivered But Not Billed** check.
- To exclude this account from Sales Return entries, enable the **Disable Stock Delivered but Not Billed in Sales Return** checkbox in the Company.

### Backdated Entries and Reposting

If a backdated entry changes the valuation rate on a Delivery Note, the system automatically updates the billed value on the corresponding Sales Invoice through reposting. This ensures that the accounting entries across the Delivery Note and Sales Invoice remain consistent throughout the entire sales cycle.

<!-- page: erpnext/erpnext__putaway-rule.md -->
---
title: "Putaway Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/putaway-rule"
updated: "2026-02-27"
---


**A Putaway Rule defines a Warehouse Assignment Strategy for incoming stock.**

A Putaway Rule is uniquely defined for an Item-Warehouse combination in a Company. It takes Warehouse Capacity and Priority into consideration.

In **Purchase Receipts** and **Stock Entries** (Material Receipt & Material Transfer), the Putaway Rules are applied and Items are **auto-assigned** to Warehouses based on the given strategy.

This is particularly useful for capacity management in large Warehouses with multiple locations.

To access a Putaway Rule, go to:

> Home > Stock > Stock Transactions > Putaway Rule

## 1. Prerequisites

Before creating and using a Putaway Rule, it is advised that you create the following first:

- [Stock Item](/erpnext/item)
- [Warehouse](/erpnext/warehouse)

## 2. How to create a Putaway Rule

1. Go to the Putaway Rule list, click on New.
 [Screenshot on the live page: Unsaved Putaway Rule]

1. Set the Company and Select an Item.
1. Select the Warehouse on which this rule is applicable.
1. Set the Capacity. You can also select a UOM if you want to set the Capacity in a different UOM. The Capacity in Stock UOM will be set automatically.
 [Screenshot on the live page: Multi UOM Putaway Rule]

1. Set the Priority. This can begin from 1 onwards, 1 being the highest priority.
1. Save.
1. You can additionally Disable a Putaway Rule as well.

The rule is unique to each Item-Warehouse combination.

## 3. How Putaway is strategized
1. Here the strategy is purely based on **Capacity** and **Priority**.
1. Warehouses will be auto-assigned until they reach full capacity.
1. Priority will be considered first. Followed by free space. If two rules have the same priority, the rule with more free space available will be assigned.
1. If you are running at full capacity (no free space in any Warehouse), ERPNext will let you know.

## 4. How it works

As mentioned before, the Putaway Rules are applied on **Purchase Receipts** and **Stock Entries** (Material Receipt & Material Transfer).

A checkbox called **Apply Putaway Rule** will allocate items to Warehouses based on the Putaway Rules.
 [Screenshot on the live page: Apply Putaway Rule checkbox]

Putaway Rules are applied on checking this checkbox. They are also re-applied on save if this checkbox is enabled.

Let us see the same in action:

1. Here is a Purchase Order with a requirement of 5 Cartons (60 Nos) of Mineral Water.
 [Screenshot on the live page: Purchase Order]

1. Two active Putaway Rules have been created below with capacity 4 Cartons (48 Nos) each. One has a higher priority than the other.
 [Screenshot on the live page: Active Putaway Rules List]

1. A Purchase Receipt is created from this Purchase Order.

1. On checking **Apply Putaway Rule**, one row of 5 Cartons is split and assigned according to the rules.
 [Screenshot on the live page: Putaway Rules applied in a Purchase Receipt]

1. First, 4 out of 5 Cartons are accommodated in the 'Finished Goods - UPI' Warehouse. Once this Warehouse is at capacity, it assigns the rest (1 Carton) to the 'Stores - UPI' Warehouse.

## 5. Warehouse Capacity Summary

The **Warehouse Capacity Summary** Report shows Warehouse capacities and their respective stock levels.

Only Warehouses having Putaway Rules will be listed here. The **Edit Capacity** button gives provision to edit the Putaway Rule capacity.

 [Screenshot on the live page: Warehouse Capacity Summary]


## 6. Types of Putaway Application

### 6.1. Direct Putaway

1. The example in the previous section explains **Direct Putaway**.
1. It is, essentially, directly assigning incoming stock to certain Warehouses based on a strategy.
1. This can easily be exercised via a Purchase Receipt.

### 6.2. Indirect (Combined) Putaway

1. Stock is often received into **temporary** or **staging** Warehouses first.
1. From here it is placed into appropriate locations within the Warehouse.
1. This is called **Indirect or Combined** Putaway.
1. To simulate this within ERPNext, a simple Purchase Receipt can be created into the temporary Warehouse, without Putaway applied.
1. From here, a Stock Entry (Material Transfer) can be done, where Putaway Rules can be applied similar to Purchase Receipts.

## 7. Related Topics

1. [Purchase Receipt](/erpnext/purchase-receipt)
1. [Stock Entry](/erpnext/stock-entry)

<!-- page: erpnext/erpnext__quality-feedback-template.md -->
---
title: "Quality Feedback Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality-feedback-template"
updated: "2026-02-26"
---

For creating the Quality Feedback first you must decide the parameters by creating the Quality Feedback Template. The templates generally contain the name the template, scope and the different parameters to be entered. The different parameters can be decided on the basis of different occasions and survey.

To access the Quality Feedback Template, go to:

> Home > Quality > Quality Feedback Template

## 1. How to create a Quality Feedback Template

1. Go to the Quality Feedback Template list, click on New.
2. Enter a name for the template.
3. In the Parameters table, list down the various processes/parameters on which you want the user to rate and give the feedback.
4. Save.

[Screenshot on the live page]

## 2. Related Topics

- [Quality Feedback](https://docs.frappe.io/erpnext/user/manual/en/quality_feedback)

<!-- page: erpnext/erpnext__quality-inspction-summary.md -->
---
title: "Quality Inspection Summary"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality-inspction-summary"
updated: "2026-03-02"
---


To access the Quality Inspction Summary, go to:

> Home > Manufacturing > Reports > Quality Inspction Summary

[Screenshot on the live page: Task]

This report will give information about the Quality Inspections as well as the status of the Quality Inspections like Accepted or Rejected.

<!-- page: erpnext/erpnext__quality-inspection.md -->
---
title: "Quality Inspection"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality-inspection"
updated: "2026-02-27"
---

In ERPNext, you can mark your incoming or outgoing products for Quality Inspection.

To access this feature go to: 


> Home > Stock > Tools > Quality Inspection
> 
> 

1. Prerequisites
----------------

Before creating and using a Quality Inspection, it is advised that you do the following first:

* **Create an** [**Item**](/erpnext/item).
* **Enable Quality Inspection Criteria in the Item master**. On enabling either checkboxes, **submission** of a stock delivery/receipt document will be allowed only after a Quality Inspection is done against it: [Screenshot on the live page: Enable Quality Inspection]
* (Optional) **Create a Quality Inspection Template**. You can add inspection parameters and acceptance criteria in the template, which can be easily fetched into any Quality Inspection. After saving the template, you can set this template in the Item Master (as shown above). [Screenshot on the live page: Quality Inspection Template]

2. How to create a new Quality Inspection
-----------------------------------------

1. From a **Draft** Purchase/Subcontracting Receipt or Delivery Note, go to the Item table's Quality Inspection field and click on Create a New Quality Inspection. You can also create a Quality Inspection for Job Card in order to monitor the quality of in-process items. In this case, you can create a Quality Inspection for the Production Item in Job Card.
2. Select the inspection type whether Incoming (Purchase), Outgoing (Sales), or In Process (Manufacturing).
3. Select the Reference Document Type whether Purchase Receipt, Purchase Invoice, Delivery Note, Sales Invoice, Stock Entry, or Job Card.
4. Select the Item and set the sample size which will be inspected. Note that only Items having Inspection Criteria enabled in the Item master, will be fetched.
5. The Quality Inspection Template set in the Item master will be fetched.
6. You can change who it's inspected by and also add who it's verified by.
7. Any additional Remarks about the Inspection can be added.
8. Save. Set the Status. Submit.

[Screenshot on the live page: Quality Inspection]  


3. Features
-----------

A single Quality Inspection consists of many Quality Checks (Parameters) within it. Each of these checks could be [Numeric](#31-numeric-quality-checks), [Non-numeric](#32-non-numeric-value-based-quality-checks) or [Formula Based](#33-formula-based-quality-checks).

### 3.1 Numeric Quality Checks

Numeric Quality Checks include all checks that require number-based readings and acceptance criteria.

E.g. checking if a reading is in a certain range.

By default the checks are numeric. There are two fields: **Minimum Value** and **Maximum Value**, to define a range that **each** reading must be in. These fields can be set in the Quality Inspection Template once and be simply fetched into the Quality Inspection.

[Screenshot on the live page: Numeric Quality Check]  


If any of the readings entered are not within this range, the status on the row will be set to 'Rejected' automatically on Save.

### 3.2 Non-numeric (Value-Based) Quality Checks

Non-numeric Quality Checks include checks that require alphabetical values or those that do not require any mathematical calculations.

E.g. checking if the color is white in a color quality check, Yes/No values for certain parameters, etc.

For Non-numeric checks, enable the 'Non-numeric' checkbox. You will notice the field **Acceptance Criteria Value** and the section **Value-Based Inspection** are visible.

Enter the field Reading Value. The Acceptance Criteria Value can be set in the Quality Inspection Template once and then be fetched into the Quality Inspection.

[Screenshot on the live page: Non-numeric Quality Check]  


If the Reading Value does not match the Acceptance Criteria Value, the status on the row will be set to 'Rejected' automatically on Save.

### 3.3 Formula-Based Quality Checks

Formula-Based Quality Checks are useful for more complex scenarios where just specifying a range or an acceptance value is not enough.

E.g. checking if the grade of a material is A/B/C, checking if the mean of some readings is within a certain range, etc.

Formula-Based Quality Checks are applicable to Numeric and Non-numeric Quality Checks.

Enable the 'Formula Based Criteria' checkbox to perform a Formula-Based Quality Check. You will then notice a field called **Acceptance Criteria Formula** where you can specify a formula that determines whether a certain check is Accepted or Rejected. This formula can be set in the Quality Inspection Template once and then be fetched into the Quality Inspection.

[Screenshot on the live page: Acceptance Criteria Formula]  


This formula depends on the many Reading fields in the Readings table.

For Numeric readings, `reading_1`, `reading_2` and so on are accepted in the formula.

For Non-numeric readings, only `reading_value` is accepted in the formula.

Here are some examples of formulas:


```
# Numeric
(reading_1 + reading_2) < 10 # sum of both readings is less than 10
(reading_1 + reading_2) <= 10 # sum of both readings is less than or equal to 10
mean < 15  # mean of non empty numeric readings is less than 15
(reading_1 * 2) < 20 # Reading 1 multiplied by 2 is less than 20
(reading_1) / 2 < 20 # Reading 1 divided by 2 is less than 20

# Non-numeric
reading_value in ("A", "B", "C") # Reading Value is either A / B / C
reading_value != "Red" # Reading Value is not equal to Red
  

```
Update the readings and Save. The Status field in the Readings table rows is set automatically based on the formula for acceptance.

### 3.3 Manual Inspection

So far, all the Quality Checks have automatic acceptance/rejection on Save. In the real world, there could be cases where a check is rejected but yet will be accepted because there is some tolerance.

Such cases will require the user to determine the row-level status. To avoid any system interference in such checks, enable the 'Manual Inspection' checkbox. You can now set the status manually and it will be untouched on Save.

[Screenshot on the live page: Manual Inspection]  


Here Reading 1 is outside the defined range, this check would be rejected. But, since it is not very far from 0.153 we accept it manually.

The status for the entire Quality Inspection can then be decided by the user.

4. Video
--------

### 5. Related Topics

1. [Purchase Receipt](/erpnext/purchase-receipt)
2. [Delivery Note](/erpnext/delivery-note)
3. [Stock Entry](/erpnext/stock-entry)
4. [Sales Invoice](/erpnext/sales-invoice)
5. [Purchase Invoice](/erpnext/purchase-invoice)
6. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__quality-management.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality-management"
updated: "2026-02-26"
---

Quality management in ERPNext focuses on maintaining high standards throughout the production and procurement processes.

- **Quality Checks**: Implement checks at various stages to ensure products and materials meet quality standards.
- **Inspection Templates**: Standardize quality assessments with predefined criteria and parameters.
- **Non-Conformance Management**: Track and address quality issues, managing corrective actions to prevent recurrence.
- **Batch Tracking**: Monitor and manage quality by tracking specific batches of products.
- **Supplier Quality Management**: Evaluate and manage the quality of materials from suppliers.
- **Reporting and Analytics**: Generate reports and analyze data to monitor quality performance.

These features help businesses ensure consistent product quality, improve operational efficiency, and enhance customer satisfaction.

<!-- page: erpnext/erpnext__quality_action.md -->
---
title: "Quality Action\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_action"
updated: "2026-02-26"
---

**A Quality Action is taken on a Quality Review to correct unsatisfactory results or prevent them from happening.**

Quality Action is a standard feature to allow implementation of corrective and preventive actions. This will meet compliance with industry regulations including GMP, ISO 9001 and 14001, TSCA, REACH, etc.

Quality Action workflows provide a controlled environment and reduce the risk of repeat issues by ensuring that defined solutions and processes are met.

Quality Actions can be initialized for a Quality Goal or for a Customer Feedback which may not meet the expected quality standards. Depending on that a Corrective or Preventive Action can be started.

To access Quality Action, go to:

> Home > Quality > Review and Action > Quality Action

## 1. Prerequisites

Before creating and using a Quality Action it is advised to create the following first:

- [Quality Review](https://docs.frappe.io/erpnext/user/manual/en/quality_review) or [Quality Feedback](https://docs.frappe.io/erpnext/user/manual/en/quality_feedback)

## 2. How to create a Quality Action

1. Go to the Quality Action list, click on New.
2. Select whether it's a Corrective or Preventive action. This indicates whether the action is being scheduled for Corrective or for Preventive Purpose.
3. Select the Document Type whether a Quality Review or a Quality Feedback.
4. Select the actual Quality Review or Feedback under Document Name.
5. Enter a Resolution proposed for the problem in the Resolution field.
6. Save.

[Screenshot on the live page]

The Status field indicates whether the Quality Action is Open and ongoing or Closed.

## 3. Related Topics

- [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)
- [Quality Review](https://docs.frappe.io/erpnext/user/manual/en/quality_review)
- [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)

<!-- page: erpnext/erpnext__quality_feedback.md -->
---
title: "Quality Feedback\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_feedback"
updated: "2026-02-26"
---

**Quality Feedback is the information that a Customer expresses about the satisfaction or dissatisfaction about the products or services you offer.**

Quality Feedback has different fields to rate different parameters. The Customer/User can easily give their feedback by selecting their template to rate on different parameters and also provide qualitative feedback on these parameters.

You can also fetch the parameters using a [Quality Feedback Template](https://docs.frappe.io/erpnext/user/manual/en/quality-feedback-template). The templates store preset information for you to select in the Quality Feedback.

If the Feedback is not as per expectations, a Quality Action may be initialized on the basis of the seriousness of the Feedback.

To access Quality Feedback, go to:

> Home > Quality > Feedback > Quality Feedback

## 1. How to create a Quality Feedback

1. Go to the Quality Feedback list, click on New.
2. Select whether Feedback is by a Customer or a User (ERPNext account User).
3. Select the particular Customer or User.
4. Selecting a Quality Feedback Template will automatically populate the parameters for the Quality Feedback.
5. The date will be automatically set to the current date.
6. The Parameters table has the following columns:
  Parameter: Various Parameters that are pre-defined in the Quality Feedback Template you create.
   Rating: Rating for a parameter from 1 to 5.
   Feedback: Feedback based on the given Rating.
7. Save.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__quality_goal.md -->
---
title: "Quality Goal\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_goal"
updated: "2026-02-27"
---

It is a collection of individual metrics that helps to define your quality goals. It is a basic quality management process to establish a set of quality objectives.

You can create a Quality Goal for your business having multiple Quality Objectives. Different Quality Objectives for a Goal can have definite numeric target or target measured in terms of completion status(yes or no). It is monitored based on Frequency which is set for that Goal.

If you set the frequency, a [Quality Review](https://docs.frappe.io/erpnext/user/manual/en/quality_review) document will be created automatically periodically where you can maintain the actual performance measures.

To access the Quality Goal list, go to:

> Home > Quality > Quality Goal

[Screenshot on the live page]

## 1. How to Create a Quality Goal

1. Go to the Quality Goal list, click on New.
2. Enter a name for the goal.
3. Select a [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure) to be followed to achieve the Goal.
4. Created By is the Person responsible for the creation of the Goal.
5. Enter a Monitoring Frequency from 'Daily', 'Weekly', 'Monthly', or 'Quarterly'. Select 'None' if no monitoring is needed.

In the Objectives table, enter:

1. The Objectives which consist the various Objectives that need to be completed to meet the a Quality Goal.
2. The Target which consists of the numeric target value of an Objective that is to be met.
3. The Unit of Measurement to measure the Target. Eg: Leads, Hours, etc.

The Revision field shows The number of times the document was saved.

Creating a Quality Goal:

[Screenshot on the live page]

## 2. Related Topics

1. [Quality Procedure](/erpnext/quality_procedure)
2. [Quality Review](/erpnext/quality_review)

<!-- page: erpnext/erpnext__quality_meeting.md -->
---
title: "Quality Meeting"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_meeting"
updated: "2026-02-26"
---

It is an assembly of people for a particular purpose or agenda, especially for formal discussion about Quality aspects.

Quality Meetings are conducted to review the Quality Reviews that have been generated. The minutes (summary) of these meetings would include the discussion on the various Quality Reviews.

To access Quality Meeting, go to:

> Home > Quality > Meeting > Quality Meeting

## 1. How to Create a Quality Meeting

1. Go to the Quality Meeting list, click on New.
2. Enter an Agenda. It is a list of meeting activities in the order in which they are to be taken up.
3. In the Minutes table, select the Quality Review, Action, Feedback discussed inthe meeting along with the references to the appropriate documents.
4. Save.

[Screenshot on the live page]

The Status of the Meeting can be set to Closed once the agenda is done.

<!-- page: erpnext/erpnext__quality_procedure.md -->
---
title: "Quality Procedure"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_procedure"
updated: "2026-02-26"
---

**A Quality Procedure is a Standard Operating Procedure (SOP) used as a reference to carry out routine actions**

A standard operating procedure (SOP) is a set of step-by-step instructions compiled by an organization to help the employees execute routine operations. SOPs aim to achieve efficiency, quality output and uniformity of performance while reducing miscommunication and failure to comply with industry regulations.

A Quality Procedure can be of two types:

1. A Procedure consisting of simple steps that you must follow to achieve a [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)
2. A procedure having sub-Procedures which may also have its own steps

To access the Quality Procedure list, go to:

> Home > Quality > Goal and Procedure > Quality Procedure

## How to create a Quality Procedure

1. Go to the Quality Procedure list, click on New.
2. Enter a name for the Quality Procedure.
3. In the Processes table, enter Process Descriptions.
4. **Child Procedure**: If the Quality Procedure being created a is a parent procedure that contains sub-procedures, link the sub-procedure here. On doing this, the current procedure becomes a parent and the 'Is Group' checkbox is enabled.
5. Save.
  Quality Procedure can also be saved without entering the Process descriptions if the title is self explanatory.

[Screenshot on the live page]

The 'Parent Procedure' is linked to the child procedure. For example 'Issue Classification' needs to be done before a resolution and hence 'Issue Resolution' is the parent here:

[Screenshot on the live page]

## Features

#### 1. Using Quality Procedure in Quality Goal

Once a Quality Procedure is created, it can be used in a [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal):

[Screenshot on the live page]

#### 2. Sub Procedures

Process can either be just a instruction or a different Quality Procedure. You can link a Quality Procedure as a sub-procedure to another one:

[Screenshot on the live page]
