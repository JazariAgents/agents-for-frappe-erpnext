<!-- Frappe documentation: erpnext, part 13 of 18. Index: docs/INDEX.md -->

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

![Purchase tax template title, company, and Tax Category](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-overview.png)

Use **Disabled** to stop new selection while preserving transactions that already reference the template.

## Open and configure a row

The table provides a compact view of the formulas. Use the pencil icon to open fields that do not fit in the grid.



![Open a Purchase Taxes and Charges row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-tax-row.png)

Set the calculation type, account, and rate. The row values remain zero on the master because Net Amount, Amount, and Total are calculated only in a transaction.



![Purchase tax calculation type, account, and rate](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-calculation-fields.png)

## Decide whether the row affects Total, Valuation, or both

The **Consider Tax or Charge for** field controls the accounting purpose of the row:


| Value               | Supplier total                    | Item valuation                              | Typical use                                                         |
| ------------------- | --------------------------------- | ------------------------------------------- | ------------------------------------------------------------------- |
| Total               | Affects the amount payable        | Does not allocate the cost into stock value | Recoverable input tax or a charge billed without capitalization     |
| Valuation           | Does not affect the payable total | Allocates the cost into item valuation      | A known cost capitalized separately from the supplier invoice total |
| Valuation and Total | Affects the amount payable        | Also allocates the cost into item valuation | Freight or duty billed by the supplier and capitalized into stock   |


The correct choice depends on whether the amount is recoverable, expensed, capitalized, and included in what you owe the supplier. Verify the expected debit and credit entries on a small submitted example.

Use **Add or Deduct** to determine whether the row increases or reduces the relevant base.



![Purchase valuation, add or deduct, description, and inclusive pricing](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-posting-fields.png)

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



![Purchase tax and Grand Total result](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-result.png)

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

![ERPNext Item marked as a fixed asset with an Asset Category](https://novacompanies.m.frappe.cloud/files/06-fixed-asset-item.png)

## Record the purchase

1. Create a [Purchase Invoice](https://docs.frappe.io/erpnext/purchase-invoice) or a [Purchase Receipt](https://docs.frappe.io/erpnext/purchase-receipt) for the fixed-asset Item.
2. Select the correct company and supplier.
3. Enter quantity, rate, and the intended asset location.
4. Submit the document. If auto creation is enabled, open the created Asset from the document links.
5. If auto creation is disabled, create the Asset and link the source purchase document.

## Review the Asset before submission

Check the location, purchase date, available-for-use date, quantity, net purchase amount, and depreciation settings. The Available for Use Date determines when depreciation can start.

![Purchased Asset details and depreciation controls in ERPNext](https://novacompanies.m.frappe.cloud/files/07-asset-core-details.png)

Review each Finance Book row before submission. The row is the source of the schedule for that reporting basis.

![Finance Book rows on an ERPNext Asset](https://novacompanies.m.frappe.cloud/files/08-asset-finance-books.png)

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

![Item Purchase UoM](/files/editing-uom-in-po.gif)  


#### Step 2: Update UoM Conversion Factors

In one Box, if you get 20 Nos. of Pen, UoM Conversion Factor will be 20.

![Item Conversion Factor](/files/po-conversion-factor.png)  


Based on the Qty and Conversion Factor, qty will be calculated in the Stock UoM of an item. If you purchase just one Box, then the Qty in the stock UoM will be set as 20.

![Purchase Qty in Default UoM](/files/po-qty-in-stock-uom.png)  


### Stock Ledger Posting

Irrespective of the Purchase UoM selected, stock ledger posting will be done in the Default UoM of an item. Hence, you should ensure that the conversion factor is entered correctly while purchasing an item in a different UoM.

![Print Format in Purchase UoM](/files/po-stock-uom-ledger.png)  


### Set Conversion Factor in Item

In the Item master, under the Purchase section, you can list all the possible UOM purchases of an item, with its UoM Conversion Factor.

![Purchase UoM master](/files/item-purchase-uom-conversion.png)  

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

![](/files/Delivery Note to Sales Invoice.mp4)



**On Delivery Note submission:** The warehouse's **Stock In Hand** account is credited, and the full stock value is debited to the **Stock Delivered but Not Billed** account.

*Example: A Delivery Note worth ₹400 → Stock In Hand credited ₹400, Stock Delivered but Not Billed debited ₹400.*

**On Sales Invoice submission:** The **Stock Delivered but Not Billed** account is credited as a reversal, and the **Cost of Goods Sold (COGS)** account is debited for the same amount.

*Example: Sales Invoice raised for ₹400 → Stock Delivered but Not Billed credited ₹400, COGS debited ₹400.*

![](/files/Screenshot 2026-07-02 at 12.30.00 PM.webp)

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
 ![Unsaved Putaway Rule](/files/unsaved-putaway-rule.png)

1. Set the Company and Select an Item.
1. Select the Warehouse on which this rule is applicable.
1. Set the Capacity. You can also select a UOM if you want to set the Capacity in a different UOM. The Capacity in Stock UOM will be set automatically.
 ![Multi UOM Putaway Rule](/files/multi-uom-putaway-rule.png)

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
 ![Apply Putaway Rule checkbox](/files/apply-putaway-rule.png)

Putaway Rules are applied on checking this checkbox. They are also re-applied on save if this checkbox is enabled.

Let us see the same in action:

1. Here is a Purchase Order with a requirement of 5 Cartons (60 Nos) of Mineral Water.
 ![Purchase Order](/files/po-putaway-demo.png)

1. Two active Putaway Rules have been created below with capacity 4 Cartons (48 Nos) each. One has a higher priority than the other.
 ![Active Putaway Rules List](/files/active-putaway-rules-list.png)

1. A Purchase Receipt is created from this Purchase Order.

1. On checking **Apply Putaway Rule**, one row of 5 Cartons is split and assigned according to the rules.
 ![Putaway Rules applied in a Purchase Receipt](/files/pr-putaway-apply.gif)

1. First, 4 out of 5 Cartons are accommodated in the 'Finished Goods - UPI' Warehouse. Once this Warehouse is at capacity, it assigns the rest (1 Carton) to the 'Stores - UPI' Warehouse.

## 5. Warehouse Capacity Summary

The **Warehouse Capacity Summary** Report shows Warehouse capacities and their respective stock levels.

Only Warehouses having Putaway Rules will be listed here. The **Edit Capacity** button gives provision to edit the Putaway Rule capacity.

 ![Warehouse Capacity Summary](/files/warehouse-capacity-summary.png)


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

![](/files/Screenshot 2026-01-22 at 11.50.28 PM.png)

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

![Task](/files/quality-inspection-summary.png)

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
* **Enable Quality Inspection Criteria in the Item master**. On enabling either checkboxes, **submission** of a stock delivery/receipt document will be allowed only after a Quality Inspection is done against it: ![Enable Quality Inspection](/files/quality-inspection-pre-requisite.png)
* (Optional) **Create a Quality Inspection Template**. You can add inspection parameters and acceptance criteria in the template, which can be easily fetched into any Quality Inspection. After saving the template, you can set this template in the Item Master (as shown above). ![Quality Inspection Template](/files/quality-inspection-template.png)

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

![Quality Inspection](/files/quality-inspection-1.png)  


3. Features
-----------

A single Quality Inspection consists of many Quality Checks (Parameters) within it. Each of these checks could be [Numeric](#31-numeric-quality-checks), [Non-numeric](#32-non-numeric-value-based-quality-checks) or [Formula Based](#33-formula-based-quality-checks).

### 3.1 Numeric Quality Checks

Numeric Quality Checks include all checks that require number-based readings and acceptance criteria.

E.g. checking if a reading is in a certain range.

By default the checks are numeric. There are two fields: **Minimum Value** and **Maximum Value**, to define a range that **each** reading must be in. These fields can be set in the Quality Inspection Template once and be simply fetched into the Quality Inspection.

![Numeric Quality Check](/files/quality-inspection-numeric-reading.png)  


If any of the readings entered are not within this range, the status on the row will be set to 'Rejected' automatically on Save.

### 3.2 Non-numeric (Value-Based) Quality Checks

Non-numeric Quality Checks include checks that require alphabetical values or those that do not require any mathematical calculations.

E.g. checking if the color is white in a color quality check, Yes/No values for certain parameters, etc.

For Non-numeric checks, enable the 'Non-numeric' checkbox. You will notice the field **Acceptance Criteria Value** and the section **Value-Based Inspection** are visible.

Enter the field Reading Value. The Acceptance Criteria Value can be set in the Quality Inspection Template once and then be fetched into the Quality Inspection.

![Non-numeric Quality Check](/files/quality-inspection-non-numeric-reading.png)  


If the Reading Value does not match the Acceptance Criteria Value, the status on the row will be set to 'Rejected' automatically on Save.

### 3.3 Formula-Based Quality Checks

Formula-Based Quality Checks are useful for more complex scenarios where just specifying a range or an acceptance value is not enough.

E.g. checking if the grade of a material is A/B/C, checking if the mean of some readings is within a certain range, etc.

Formula-Based Quality Checks are applicable to Numeric and Non-numeric Quality Checks.

Enable the 'Formula Based Criteria' checkbox to perform a Formula-Based Quality Check. You will then notice a field called **Acceptance Criteria Formula** where you can specify a formula that determines whether a certain check is Accepted or Rejected. This formula can be set in the Quality Inspection Template once and then be fetched into the Quality Inspection.

![Acceptance Criteria Formula](/files/acceptance-criteria-formula.png)  


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

![Manual Inspection](/files/quality-inspection-manual-reading.png)  


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

![](/files/action0e0bc8.gif)

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

![](/files/feedback58d87a.gif)

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

![](/files/Screenshot 2026-01-23 at 12.16.34 AM.png)

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

![](/files/goal.gif)

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

![](/files/meetingf9c910.gif)

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

![](/files/Screenshot 2026-01-22 at 11.12.11 PM.png)

The 'Parent Procedure' is linked to the child procedure. For example 'Issue Classification' needs to be done before a resolution and hence 'Issue Resolution' is the parent here:

![](/files/Screenshot 2026-01-22 at 11.16.49 PM.png)

## Features

#### 1. Using Quality Procedure in Quality Goal

Once a Quality Procedure is created, it can be used in a [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal):

![](/files/Area3ae47b.gif)

#### 2. Sub Procedures

Process can either be just a instruction or a different Quality Procedure. You can link a Quality Procedure as a sub-procedure to another one:

![](/files/Screenshot 2026-01-22 at 11.24.39 PM.png)

<!-- page: erpnext/erpnext__quality_review.md -->
---
title: "Quality Review\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_review"
updated: "2026-02-26"
---

**A Quality Review is a record of the performance against Quality Goal at regular intervals.**

A Quality Review is an inspection with a specific structure, defined roles, and procedure designed to ensure a product's completeness and adherence to quality standards. The Quality Review is used to check if all Objectives of a Quality Goal have been achieved.

To access the Quality Review list, go to:

> Home > Quality > Review and Action > Quality Review

## 1. Prerequisites

Before creating and using a Quality Review it is advised to create the following first:

- [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)

## 2. How to Create a Quality Review

1. Go to the Quality Review list, click on New.
2. Select a Quality Goal which is to be Reviewed.
3. In the Review section of the Reviews table, leave a review about a Quality Objective.
4. Save.

![](/files/review63e6d1.gif)

> Note: If the Quality Procedure is linked to the Quality Goal, the Quality Procedure will be fetched in the Quality Review.

You can also add some notes in the 'Additional Information' section.

## 3. Features

#### Periodic Auto Creation

if you have set the frequency of review in your Quality Goal, then the Quality Review will automatically be created and its status will be set to "Open". The quality manager can then check open reviews and complete the inspection.

## 4. Next Steps

After you have completed a Quality Review, you can create a [Quality Action](https://docs.frappe.io/erpnext/user/manual/en/quality_action) against it if you want to record any corrective or preventive actions

## 5. Related Topics

- [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)
- [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)
- [Quality Action](https://docs.frappe.io/erpnext/user/manual/en/quality_action)

<!-- page: erpnext/erpnext__quick-stock-balance.md -->
---
title: "Quick Stock Balance\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quick-stock-balance"
updated: "2026-02-27"
---


**Quick Stock Balance is a tool that can be used to quickly retrieve the current stock balance (quantity) and value of an item, in the specified warehouse, on the specified date.**

It comes in handy during audits, while verifying stock details before transactions, etc.

To access this tool, go to:
> Home > Stock > Tools > Quick Stock Balance

## 1. Using Quick Stock Balance
Item and Warehouse are the basic fields required to fully utilize Quick Stock Balance. Item Barcode can also be used to fetch stock details.

![Quick Stock Balance](/files/quick-stock-balance.png)

You can opt to select a different warehouse or date. The stock value and quantity, will be fetched real-time according to the specified values.

You can also view the Stock Balance report by clicking on 'Stock Balance Report' . It will redirect you to the report with the Item and Warehouse filters populated.

![Stock Balance Report](/files/stock-balance-report.png)

### 2. Related Topics
1. [Stock Level Report](/erpnext/stock-level-report)
1. [Stock Entry](/erpnext/stock-entry)

<!-- page: erpnext/erpnext__quickbooks-migrator.md -->
---
title: "QuickBooks Migrator (Deprecated) | ERPNext Documentation"
description: "The built-in ERPNext QuickBooks Migrator has been removed. Review the legacy instructions and use supported ERPNext import tools for current migrations."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quickbooks-migrator"
updated: "2026-07-31"
---

> **Deprecated**
>
> The built-in ERPNext QuickBooks Migrator is no longer available in current ERPNext releases. It was removed from the ERPNext develop branch on January 17, 2025 in [PR #45240](https://github.com/frappe/erpnext/pull/45240). The instructions below apply only to older ERPNext versions that still contain the QuickBooks Migrator and should not be used for a current migration.
>
> For a current QuickBooks migration, export the required data from QuickBooks, clean and map it, then use [Data Import](/erpnext/data-import) for masters, the [Chart of Accounts Importer](/erpnext/chart-of-accounts-importer), the [Opening Invoice Creation Tool](/erpnext/opening-invoice-creation-tool), [Stock Reconciliation](/erpnext/stock-reconciliation), and opening Journal Entries. Follow the [Accounting Migration Overview](/erpnext/accounting-migration-overview) to plan and validate the migration.

## Legacy instructions for older ERPNext versions

## How to Setup QuickBooks Migrator?

### Create a QuickBooks Online App

1. From Awesome-bar, Go to "QuickBooks Migrator" DocType.
2. Go to [Inuit Developer Portal](https://developer.intuit.com)
3. Sign In with your existing account or Sign Up.
4. Go to "My Apps" page.
5. Click on "Select APIs".
6. Under "QuickBooks API" Check "Accounting".
7. Click on "Create App".
  - You'll be taken to the Dashboard of your App.
8. Go to "Keys" tab.
9. Go to "Production Keys" Section.
  - Complete requirements.
10. In "QuickBooks Migrator" DocType a "Redirect URL" will be generated for you and add it in the list of "Redirect URIs" of your Inuit App (under "Production Keys" section). Click Save.
  - Make sure that the Redirect URL starts with `https`.
11. From "Production Keys" section copy "Client ID" and "Client Secret" to "QuickBooks Migrator" DocType.
12. Save "QuickBooks Migrator".

### Connect to QuickBooks Online API

1. Click "Connect to QuickBooks".
2. A new tab will open in your browser and You'll be asked to Log In.
3. If you have more than one companies then Select the company you want to migrate.
4. Click "Connect".
5. Upon successful authorization, the tab will close.
6. The indicator will be set to "Connected to QuickBooks".
7. In "QuickBooks Migrator" select "Company" where you want to migrate your data.
8. Save "QuickBooks Migrator".

### Migrate Data

1. Click the "Fetch Data" button.
2. The indicator will change from "Connected to QuickBooks" to "In Progress".
3. Progress bars will show the status of migration.
4. This will take a few minutes depending on the size of data.
5. After migration is complete, the indicator will change to "Complete" or "Failed".

## What Will Happen when I Click Fetch Data?

## Account

### Existing Chart of Accounts

 Upon creation of a Company ERPNext creates a chart of accounts for that company, these accounts will be kept.

### Account Naming

 To avoid name collision with existing accounts, all accounts from QuickBooks will be assigned "- QB" suffix.

 e.g. `Job Expense` will become `Job Expense - QB`.

 **Note**: ERPNext also encodes account names with Company abbreviation. Taking this into account `Job Expense` will become `Job Expense - QB - AZ` (assuming `AZ` is the company abbreviation).

### Root Accounts

 Five root accounts, namely `Asset`, `Equity`, `Expense`, `Liability`, `Income` will be created and all accounts (depending on the account type) will become children of these accounts.

### Group Accounts

 QuickBooks allows transactions on group accounts, which is not allowed in ERPNext, to handle this, every group account will have a child with a hyphenated name.

 e.g.

 will become

### Name Collisions

 QuickBooks allows multiple accounts to have the same name, which is not allowed in ERPNext, to handle this, every duplicate account will have a hyphenated name.

 e.g.

 will become



## Item

### Naming

 All Items will have company encoded names.

 e.g. `Pen` will become `Pen - AZ` (assuming `AZ` is the company abbreviation).

### UOM

 All Items will be assigned `Unit` as the default UOM.

### Fractional UOM

 `Unit` will be allowed to have fractional value.

### Inventory

 Irrespective of whether Item is an Inventory or Non-Inventory Item in QuickBooks, No Inventory related information will be kept.

## Customer and Supplier

### Naming

 All Customer and Suppliers will have company encoded names.

 e.g. `Pen` will become `Pen - AZ` (assuming `AZ` is the company abbreviation).



## Invoice

### Variants

 QuickBooks has four transactional variants of Invoice, all of these will be saved as Sales Invoice.

- **Invoice** is equivalent to a Sales Invoice.
- **Sales Receipt** is equivalent to a POS Sales Invoice.
- **Credit Memo** is equivalent to a return Sales Invoice (Credit Note).
- **Refund Receipt** is equivalent to a return POS Sales Invoice.

### Discount and Markup

 QuickBooks uses special accounts for both Markup and Discount, ERPNext doesn't handle the discount expense and markup this way, instead, all Item's will see the change in their Income accounts.

### Shipping

 For Invoices with Shipping, an Item with name Shipping will be added in the Item table.

### Round off

 ERPNext uses different rounding method than QuickBooks, because of this, in Invoices with Tax and with a currency different than company currency, Sales Invoice will have different grand total than that of the QuickBooks Invoice.

### Special Case

 If a QuickBooks Invoice is linked to a `Delayed Charge` or `Statement Charge` then an equivalent `Journal Entry` is created for this Invoice.



## Bill

### Variants

 QuickBooks has two transactional variants of Bill, all of these will be saved as Purchase Invoice.

- **Bill** is equivalent to a Purchase Invoice.
- **Supplier Credit** is equivalent to a return Purchase Invoice.



## Other

Following transactions will be saved as Journal Entry

- Advance Payment
- Bill Payment
- Cheque
- Credit Card Credit
- Expense
- Inventory Qty Adjustment
- Journal Entry
- Payment
- Tax Payment



## Tax

For every QuickBooks Tax Rate an ERPNext account will be created.

## Custom Fields

QuickBooks Migrator will add following Custom Fields

- Company field
- Customer
- Item
- Supplier
- QuickBooks ID field
- Customer
- Item
- Journal Entry
- Purchase Invoice
- Sales Invoice
- Supplier

<!-- page: erpnext/erpnext__quotation.md -->
---
title: "Quotation | ERPNext Documentation"
description: "Create, price, submit, share, and convert Quotations in ERPNext, including items, taxes, payment terms, alternatives, and statuses."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quotation"
updated: "2026-07-24"
---

A Quotation in ERPNext records the products or services, quantities, prices, taxes, validity, delivery expectations, and commercial terms offered to a Lead or Customer. It is a submittable sales transaction that can be shared as a proposal and converted into a [Sales Order](/erpnext/sales-order) after acceptance.

![](/files/order-to-cash-quotation.webp)
*Quotation highlighted within the ERPNext CRM and sales flow.*

## Before you begin

Create or confirm the following records:

- A [Lead](/erpnext/lead) or [Customer](/erpnext/customer).
- The required [Items](/erpnext/item) and selling prices.
- A selling [Price List](/erpnext/price-list) and Currency.
- Applicable [Sales Taxes and Charges Templates](/erpnext/sales-taxes-and-charges-template).
- Approved [Terms and Conditions](/erpnext/terms-and-conditions) and Payment Terms when required.

## Create a Quotation

1. Go to **Selling > Sales > Quotation**.
2. Select **Add Quotation**.
3. In **Quotation To**, select Customer or Lead, then select the party.
4. Enter the Date and **Valid Till** date.
5. Confirm the Order Type and Company.
6. Add each Item, Quantity, Rate, and Warehouse in the Items table.
7. Add taxes, shipping, discounts, payment terms, and terms and conditions as applicable.
8. Review the totals, then save the draft.

![Example Quotation for Northstar Retail with products, services, quantities, rates, and totals.](https://novacompanies.m.frappe.cloud/files/quotation-details.png)

The example quotation combines laptops, accessories, and a setup service. In an Item row, the stock indicator before the Item Code is green when the item is in stock and red when it is out of stock. Select the row's pencil icon to open the full row editor when additional item fields are required.

![The highlighted pencil icon opens the complete Quotation item row.](/files/quotation-item-pencil.webp)

![The Quotation item row with item details, quantity, UOM, rate, and alternative-item settings.](/files/quotation-item-row.webp)

## Alternative ways to create a Quotation

A Quotation can be created from an [Opportunity](/erpnext/opportunity), which carries the party and requested items into the new transaction. You can also use **Get Items From > Opportunity** in a draft Quotation. Review every mapped quantity, rate, date, and term before saving.

For repeated quoting, use reusable masters such as Price Lists, Item Prices, tax templates, payment terms, and terms templates instead of copying an old transaction whose conditions may be outdated.

## Important fields and what they mean


| Field                    | What it means                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Quotation To             | Determines whether the offer is addressed to a Customer or Lead.                                              |
| Party                    | The selected Customer or Lead. Address and contact details can be fetched from this party.                    |
| Valid Till               | The last date on which the offer is valid.                                                                    |
| Order Type               | Identifies Sales, Maintenance, or Shopping Cart usage. Use Shopping Cart only for the relevant website flow.  |
| Currency                 | The currency shown on the Quotation. Conversion rates apply when it differs from the Company currency.        |
| Selling Price List       | Supplies the default item prices for the selected party and currency.                                         |
| Ignore Pricing Rule      | Prevents configured [Pricing Rules](/erpnext/pricing-rule) from changing item prices or discounts.            |
| Item Code                | The product or service being quoted. It fetches the name, description, UOM, and applicable price defaults.    |
| Quantity and UOM         | The amount offered and its unit of measure.                                                                   |
| Rate                     | The offered unit price before multiplying by Quantity.                                                        |
| Warehouse                | The source warehouse used for stock context and downstream mapping where applicable.                          |
| Margin and Discount      | Adjusts the item rate by an amount or percentage.                                                             |
| Shipping Rule            | Applies configured shipping charges based on the selected rule.                                               |
| Incoterm and Named Place | Records the agreed delivery responsibility and location for international or formal trade terms.              |
| Payment Terms Template   | Creates the proposed payment schedule.                                                                        |
| Print Heading            | Displays an approved alternative heading, such as Proposal or Proforma Invoice, without changing the DocType. |


## Items, pricing, and alternatives

ERPNext fetches defaults from the Item and Item Price, but every quoted rate remains the responsibility of the user preparing the offer. Apply an item discount or margin in the row, or use Additional Discount for the transaction total. Confirm whether the additional discount applies to the Net Total or Grand Total.

To offer substitute products, add the alternative immediately after its primary item and enable **Is Alternative** in the row. Alternative items are excluded from the Quotation totals. When a Sales Order is created from an individual Quotation, ERPNext can ask which alternative should be selected.

## Taxes, shipping, and payment terms

Select a tax template or enter rows in the Sales Taxes and Charges table. Use **Tax Breakup** to review the components before sharing the document. A [Shipping Rule](/erpnext/shipping-rule) can calculate freight, while an Incoterm records delivery responsibility.

Use a [Payment Terms Template](/erpnext/payment-terms-template) when payment is divided into deposits or milestones. The resulting schedule is a proposal on the Quotation and should match the commercial agreement.

## Submit and next steps

Before submitting, check the party, validity date, items, quantities, rates, discounts, taxes, payment schedule, terms, delivery expectations, and final print output. Submission freezes the offered transaction as the version sent for approval.

After submission, use **Create > Sales Order** when the Customer accepts the offer. If the deal does not proceed, use **Set as Lost** and record a useful loss reason. Cancel and amend the Quotation when a submitted offer must be formally revised.

## Status


| Status    | Meaning                                                          |
| --------- | ---------------------------------------------------------------- |
| Draft     | The Quotation is editable and has not been confirmed.            |
| Open      | The submitted offer is active and awaits an outcome.             |
| Ordered   | A Sales Order has been created from the Quotation.               |
| Lost      | The offer did not convert. Record the reason for later analysis. |
| Expired   | The Valid Till date has passed.                                  |
| Cancelled | The submitted Quotation was cancelled.                           |


## Print and share

Review the print preview before sending the Quotation. Confirm that the selected [Print Format](/erpnext/print-format), Letter Head, item images, terms, tax details, and Print Heading appear correctly. A Print Heading changes the displayed title only. It does not convert the record into another DocType.

## Frequently asked questions

### Can I quote a Lead without creating a Customer?

Yes. Select Lead in Quotation To. Create the Customer when the party is qualified and your workflow requires customer transactions.

### Can I edit a submitted Quotation?

Cancel and amend it when a formal revision is required. Avoid silently changing an offer that has already been sent.

### Can I create a Sales Invoice directly from a Quotation?

The standard confirmed sales path is normally Quotation to Sales Order, followed by delivery and billing. Use the transaction path approved for your organization and version.

### Why did an item rate change automatically?

Check the Price List, Item Price, Pricing Rules, party, quantity, date, currency, UOM, and whether Ignore Pricing Rule is enabled.

## Related topics

- [Opportunity](/erpnext/opportunity)
- [Sales Order](/erpnext/sales-order)
- [Applying a Discount](/erpnext/applying-discount)
- [Adding Margin](/erpnext/adding-margin)
- [Selling in Different UoM](/erpnext/selling-in-different-uom)

<!-- page: erpnext/erpnext__raw-printing.md -->
---
title: "Raw Printing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/raw-printing"
updated: "2026-03-02"
---


> Introduced in Version 12

**Sending a string of commands to a printer directly in its native language is called Raw Printing.**

Many thermal printers need these raw commands sent to them in order to perform functions like barcode printing, receipt printing, label printing, etc. Raw Printing bypasses the printer's drivers in most cases, making them very fast and reliable. Raw Printing is also capable of doing some advanced features such as cutting receipt paper, kicking out cash drawers, etc.

## 1. Setting up Raw Printing in ERPNext

### 1.1 Installing QZ Tray application on the client computer

Download and install the QZ Tray application on the computer to which your thermal printer is connected. This application can be found at its [official site](https://qz.io/download/). Currently, Windows, macOS, and Linux are supported by QZ Tray. During the installation you will be prompted to install Java if not already installed, please install Java to complete the installation.

Further instructions on installing the QZ Tray Application can be [here](https://qz.io/wiki/using-qz-tray).

### 1.2 Create Raw Commands Print Format

To be able to send raw commands to a printer you need to first create a print format in raw commands. Jinja Templating Language is used in raw commands just like in the [HTML custom print format](/erpnext/print-format).

To create a new print format for Raw Printing:

1. Go to print format list: **Home > Settings > Printing > Print Format**
2. Click on New.
3. Select the relevant DocType.
4. Check the **Custom format** and **Raw Printing** options.
5. Fill in the **Raw Commands** field with the required raw commands to be sent to the printer.
6. Click Save.

 ![Raw Commands Print Format](/files/raw-command-print-format.png)

Currently, any string-based printer languages can be used in the `Raw Commands` field in the print format. Writing raw commands requires knowledge of the printer's native language provided by the printer manufacturer. Please refer to the developer manual provided by the printer manufacturer on how to write their native commands.

### 1.3 Enable Raw Printing in the Print Setting

To enable Raw Printing:

1. Go to: **Home > Settings > Printing > Print Settings > Raw Printing**.
2. Check the **Enable Raw Printing** option.
3. Save.

## 2. Methods to utilize raw printing in ERPNext

There are two ways to send Raw Printing commands to your printer.

### 2.1 Clicking print on the print view page

To print a raw command print format from the Document print view:

1. Select appropriate print format. For print format in Raw Commands, "No Preview available" message is shown in place of the print preview.
2. Click on the print button.
3. Please allow the connection prompt from the QZ Tray for the actions that you initiated (Keyboard Shortcut: Alt + A).
 - ![QZ Tray Prompt](/files/qz-tray-prompt.png)
4. You may be asked to select the "print format - printer mapping".
 - This mapping is used to send the print commands to the appropriate printer.
 - The printer needs to be installed on your computer to be able to map it to a print format.
 ![print format - printer mapping](/files/printer-settings.png)
 - This mapping is stored locally on the same computer and will have to be set on each client machine.
 - You can also edit this by clicking on the **Printer Settings** button.

 ![Raw Printing from Print View](/files/raw-printing-from-print-view.gif)

### 2.2 Calling Raw Print functions from a client script

It is often a requirement that a print command has to be issued on a certain event (like submit, save, amend, etc.). It is possible to write a [client script](/erpnext/client-scripts) to do this for you.

Following are the relevant Raw Print functions:

1. function: `frappe.ui.form.qz_connect`
 - A connection wrapper to establish a connection with the QZ Tray application.
 - Returns a promise which resolves on successful establishment of a connection.
 - Allows active and inactive connections to resolve regardless. Hence it can be called every time before sending a command.
 - Usage example:

```
 frappe.ui.form.qz_connect()
 .then(function () {
 return qz.print(config, data);
 })
 .then(frappe.ui.form.qz_success)
 .catch(err => {
 frappe.ui.form.qz_fail(err);
 });
```

Here, `qz` is a global object provided by the `qz-tray.js` library.

2. function: `frappe.ui.form.qz_get_printer_list`
 - Gives you the list of printers available to the QZ Tray application
 - Returns a promise which resolves to a list of printers

 Usage example:
```
 frappe.ui.form.qz_get_printer_list().then(
 // Required action on getting the printer list.
 // Note: Printer list is a array of strings.
 );
```

3. function: `frappe.ui.form.qz_success`
 - Displays a "Print Sent to the printer!" alert to the user. Can be called after the print command is successful.

4. function: `frappe.ui.form.qz_fail`
 - Displays the error message to the user. Should be called on failure of QZ Tray connection.

You can also directly access the functions provided by the `qz-tray.js` library via the `qz` object. [Click here for qz-tray.js library documentation](https://qz.io/api/). Note: The `qz` object is initialized only after calling the `frappe.ui.form.qz_connect` for the first time. In case you require the `qz` object before that you can use the `frappe.ui.form.qz_init`.

### 3. Related Topics
1. [Print Settings](/erpnext/print-settings)
1. [Print Format](/erpnext/print-format)
1. [Print Style](/erpnext/print-style)

<!-- page: erpnext/erpnext__razorpay-integration.md -->
---
title: "RazorPay Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/razorpay-integration"
updated: "2026-02-26"
---


A payment gateway is an e-commerce application service provider service that authorises credit card payments for e-businesses, online retailers, bricks and clicks, or traditional brick and mortar.

A payment gateway facilitates the transfer of information between a payment portal (such as a website, mobile phone or interactive voice response service) and the Front End Processor or acquiring bank.

To setup RazorPay,

`Explore > Integrations > RazorPay Settings`

![Razorpay Settings](/files/razorpay-api.gif)

#### Setup RazorPay

To enable RazorPay payment service, you need to configure parameters like API Key, API Secret

![Razorpay Settings](/files/razorpay_settings.png)

On enabling service, the system will create Payment Gateway record and Account head in the Chart of Account with account type as Bank.

![Razorpay COA](/files/razorpay_coa.png)

Also, it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

![Payment Gateway Account](/files/payment_gateway_account_razorpay.png)

After enabling service and configuring Payment Gateway Account your system is able to accept online payments.

####Supporting transaction currencies

RazorPay will only work for the company having `INR (Indian Rupee)` as a Currency.

<!-- page: erpnext/erpnext__rebuild-tree.md -->
---
title: "Rebuild the Chart of Accounts Tree | ERPNext Documentation"
description: "Learn when and how to rebuild the Chart of Accounts tree in ERPNext, repair hierarchy indexes, verify General Ledger filters, and avoid unnecessary repairs."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/rebuild-tree"
updated: "2026-08-03"
---

Use **Rebuild Tree** when the parent-child structure of the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) is correct on the Account records but ERPNext behaves as though some Accounts belong to the wrong branch. The tool recalculates the internal tree indexes that ERPNext uses to organize Accounts and include descendants in accounting reports.



This is a repair tool, not routine accounting maintenance. Do not use it merely because two reports show different totals. First verify their Company, date, Account, Finance Book, currency, Cost Center, Project, and other filters.

## When rebuilding may help

The existing ERPNext guidance describes a case in which the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) is filtered to one Account but rows from a different Account appear. Rebuilding can help when the Account tree indexes no longer match the saved parent relationships.

Other signs can include:

- a child Account is missing from a group total even though its **Parent Account** is correct;
- a parent filter includes Accounts that are no longer below that group;
- an Account appears under the correct parent in the tree, but the [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet) or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement) groups it incorrectly;
- a recent Account-parent change is not reflected consistently across tree-based reports.

> Selecting a group Account in General Ledger intentionally includes its descendant ledgers. Seeing several Accounts is therefore not, by itself, proof that the tree is damaged.

## Before you begin

1. Refresh the report and verify every relevant filter.
2. Confirm whether the selected Account is a group. Group Accounts normally return their descendants.
3. Open each affected Account and confirm its **Parent Account**, **Root Type**, **Report Type**, Company, and group status.
4. Review recent changes made through [Change the Parent Account](https://docs.frappe.io/erpnext/changing-parent-account), imports, patches, or custom applications.
5. If this is a production site, run the repair during a controlled maintenance window and ensure a current backup is available.

Do not edit internal left and right tree-index values through the database. Rebuild Tree exists to recalculate them from the saved hierarchy.

## Rebuild the tree

1. Open **Accounting &gt; Chart of Accounts**.
2. Select the affected Company.
3. Review the visible root groups and confirm the hierarchy is the one you expect.

![Chart of Accounts tree for Nova Electronics Trading](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-chart-of-accounts-tree.png)

4. Select the three-dot menu in the upper-right corner.
5. Select **Rebuild Tree**.

![Chart of Accounts menu with Rebuild Tree highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-rebuild-tree-action.png)

ERPNext recalculates the Account tree indexes. The tool does not create a [Journal Entry](https://docs.frappe.io/erpnext/journal-entry), change debit or credit amounts, move an Account to a different parent, or rewrite existing General Ledger postings.

## Verify the result

Reopen the report that showed the problem and use the same filters as before. In General Ledger, select the exact ledger Account first. Then test its parent group separately so you can distinguish the single ledger from the group and its descendants.



![General Ledger filtered to Office Maintenance Expenses after checking the tree](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-general-ledger-after-rebuild.png)

Confirm that:

1. the exact ledger filter shows only that Account's rows;
2. the group filter shows only the correct descendants;
3. opening, debit, credit, and closing balances agree with the expected vouchers;
4. the Account appears under the correct branch in Chart of Accounts;
5. the same filters produce consistent results in the relevant financial statement.

If totals still differ, investigate report filters, [Finance Books](https://docs.frappe.io/erpnext/finance-book), currencies, posting dates, cancelled entries, or an incorrect Account parent. Rebuilding cannot correct a wrong parent selection or an incorrect accounting voucher.

## What Rebuild Tree changes


| Area                  | Result                                                                       |
| --------------------- | ---------------------------------------------------------------------------- |
| Parent Account values | Remain unchanged.                                                            |
| Internal tree indexes | Recalculated from the saved hierarchy.                                       |
| Account balances      | Remain based on existing General Ledger entries.                             |
| Accounting vouchers   | Not created, cancelled, amended, or reposted.                                |
| Report grouping       | May be corrected when it was caused by inconsistent tree indexes.            |
| Wrong Account parent  | Not corrected. Change the Parent Account first, then rebuild only if needed. |


## Troubleshooting


| Issue                                       | What to check                                                                                                                                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Ledger still shows several Accounts | Confirm whether you selected a group Account. A group filter includes descendants by design.                                                                                                   |
| The wrong branch remains                    | Open the Account and correct **Parent Account**. Rebuild Tree does not decide where an Account belongs.                                                                                        |
| A financial statement total still differs   | Compare Company, dates, Finance Book, currency, dimensions, presentation currency, and accumulated-values settings.                                                                            |
| Rebuild Tree is unavailable                 | Confirm you are in the Chart of Accounts tree view and that your role has permission to use the action.                                                                                        |
| The action returns an error                 | Record the traceback, ERPNext and Frappe versions, and affected Company. Review customizations and ask the administrator or support team to investigate instead of modifying indexes manually. |


## Frequently asked questions

### Does Rebuild Tree change General Ledger entries?

No, It recalculates Account hierarchy indexes. Use [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger) only when an authorized repair must regenerate ledger entries for a supported voucher change.

### Why does a parent Account show several ledger Accounts?

Parent Accounts are groups. Reports use the tree to include their descendant ledgers. Select a non-group Account when you need only one ledger.

### Should I rebuild after every Account change?

No, Normal Account creation and parent changes update the hierarchy. Use the repair only when there is evidence that the stored tree indexes are inconsistent.

### Can Rebuild Tree move an Account to the correct parent?

No, Edit the Account's parent through the supported Chart of Accounts workflow. Rebuild Tree then recalculates indexes from that saved relationship.

### Is Rebuild Tree the same as rebuilding the General Ledger?

No, Rebuild Tree repairs hierarchy indexes. Repost Accounting Ledger regenerates accounting entries for supported source-document changes. They solve different problems.

## Related topics

- [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts)
- [Change the Parent Account](https://docs.frappe.io/erpnext/changing-parent-account)
- [Merge Accounts](https://docs.frappe.io/erpnext/merging-accounts)
- [Freeze an Account](https://docs.frappe.io/erpnext/freeze-account)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger)

<!-- page: erpnext/erpnext__receiving-bulk-payments-in-erpnext.md -->
---
title: "Receiving Bulk Payments in ERPNext | ERPNext Documentation"
description: "Record and allocate one customer receipt across multiple invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/receiving-bulk-payments-in-erpnext"
updated: "2026-07-31"
---

When a Customer sends one payment for several invoices, record one Payment Entry and allocate the amount across all matching invoices. This keeps the bank receipt intact while clearing each invoice correctly.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Receiving Bulk Payments in ERPNext

1. Create a **Receive** Payment Entry for the Customer.
2. Enter the actual bank amount and reference.

![Receive Payment Entry for a bulk customer payment in ERPNext](https://novacompanies.m.frappe.cloud/files/bulk-payment-01-bulk-receipt-overview.png)

3. Select **Get Outstanding Invoices**.
4. Choose the invoices covered by the remittance advice.
5. Enter the allocated amount for each row.
6. Confirm that the total allocation, deductions, and unallocated balance explain the receipt, then submit.

![Allocate a bulk customer payment across multiple invoices in ERPNext](https://novacompanies.m.frappe.cloud/files/bulk-payment-02-bulk-receipt-invoice-allocations.png)

## Important fields and what they mean


| Field                  | What it controls                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Total Allocated Amount | Sum assigned to invoice references.                                                |
| Unallocated Amount     | Receipt balance not yet assigned.                                                  |
| Allocated Amount       | Amount clearing a specific invoice.                                                |
| Outstanding Amount     | Invoice balance before this allocation.                                            |
| Difference Amount      | Amount that must be explained by deductions, exchange difference, or a correction. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### One or more invoices are missing from Get Outstanding Invoices

Confirm that every invoice belongs to the same Customer, Company, and receivable account selected in the Payment Entry. Check that it is submitted, has an outstanding balance, and falls within the dialog's date and filter range.

### Selecting invoice rows does not change the payment amount

The row selection controls which references you keep or remove; it does not replace the actual bank amount. Enter the amount received, then set the **Allocated Amount** for each retained invoice and review **Total Allocated Amount**.

### The receipt is smaller than the combined invoice balances

Allocate the receipt according to the customer's remittance advice. An invoice can remain partially outstanding. Do not reduce an invoice or create an unsupported discount merely to make the allocations equal the invoice totals.

### The customer paid more than the selected invoices

Allocate only the amounts that should clear the invoices. Leave the genuine excess as **Unallocated Amount** so it remains available as a customer advance, or record a separately supported deduction when the difference is a fee or adjustment.

## Frequently asked questions

### Can one receipt be allocated across invoices for different customers?

A Payment Entry has one party. Create separate Payment Entries for each Customer, then reconcile those entries with the combined bank deposit if the bank statement shows one total.

### Can one receipt partially pay several invoices?

Partial allocation is supported. Enter the exact allocation for every invoice. ERPNext reduces each invoice's outstanding amount by its allocation and leaves the unpaid balances open.

### How do I decide which invoice receives the payment first?

Follow the customer's remittance advice. If none is provided, use your documented accounting policy, such as oldest due invoice first, and retain evidence of the decision.

### What if the customer deducts bank fees or withholding tax?

Record the bank receipt exactly as received and use the appropriate deduction, withholding, or adjustment workflow with explicit ledger accounts. Do not silently reduce allocations without explaining the difference.

### Should I use this workflow for a bank deposit containing payments from many customers?

Record a Payment Entry per Customer so party ledgers remain correct. Use [Bank Reconciliation](/erpnext/bank-reconciliation) to match the individual accounting entries to the combined bank deposit when required.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__reconcile-advance-payment-made-to-the-supplier.md -->
---
title: "Reconcile Advance Payment Made to the Supplier | ERPNext Documentation"
description: "Allocate a supplier advance to later Purchase Invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reconcile-advance-payment-made-to-the-supplier"
updated: "2026-08-01"
---

A Supplier advance remains unallocated until the Purchase Invoice is posted. Reconcile the advance against the invoice so the Supplier balance and outstanding amount are correct.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Reconcile Advance Payment Made to the Supplier

1. Confirm that the advance Payment Entry is submitted and still unallocated.
2. Open Payment Reconciliation and select Supplier and the relevant Supplier.
3. Load the unallocated advance and outstanding Purchase Invoice.
4. Enter the amount to allocate and reconcile.
5. Verify the Purchase Invoice outstanding amount and Supplier ledger.

![Reconcile Advance Payment Made to the Supplier in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-11-payment-reconciliation.png)

## Important fields and what they mean


| Field               | What it controls                         |
| ------------------- | ---------------------------------------- |
| Unallocated Payment | Advance available for allocation.        |
| Purchase Invoice    | Supplier invoice receiving the advance.  |
| Allocated Amount    | Amount linked during reconciliation.     |
| Posting Date        | Date used for the reconciliation effect. |
| Difference          | Balance remaining after allocation.      |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The supplier advance is not available

Confirm that the Payment Entry is submitted, belongs to the same Supplier and Company, uses a compatible payable or configured advance account, and still has an unallocated balance.

### The Purchase Invoice does not fetch the advance

Check whether the invoice was created from the Purchase Order referenced by the advance. For an already submitted invoice, use Payment Reconciliation instead of the draft invoice's advance table.

### The supplier has several advances and the wrong one was selected

Compare reference numbers, dates, Orders, currencies, and unallocated amounts before processing. Unreconcile and reallocate through the supported workflow when necessary.

## Frequently asked questions

### Must a supplier advance be linked to a Purchase Order?

It can remain unallocated against the Supplier, but linking the relevant Purchase Order improves traceability and downstream matching.

### Can one supplier advance settle several invoices?

It can be allocated in parts across eligible invoices for the same Supplier and compatible account.

### What happens when the final invoice is smaller than the advance?

Allocate only the invoiced amount. The remainder stays as supplier credit until it is applied to another invoice or refunded.

### Can an advance posted to a separate asset account be reconciled?

Use the supported separate party account configuration. A manual entry to an unrelated asset account will not automatically appear in standard payment reconciliation.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__records-print-format.md -->
---
title: "Customize Print Format"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/records-print-format"
updated: "2026-03-02"
---

**Print Formats are the layouts that are generated when you want to Print or Email a transaction.**

This feature comes handy for all the transactions in ERPNext like all the sales and purchase transactions, HR documents and lot more.

In ERPNext, there are three types of Print Formats, namely, Standard Print Format, Custom Print Format and HTML Print Format.

Standard Print Format
---------------------

Every Printable Document Type in ERPNext will have it's own Standard Print Format which gets generated by the Frappe Framework. The field placement in the Standard Print Formats will be dependent on the position of the respective fields in the document.

![Standard Print Format](/files/customize-standard-print-format.png)  


Any changes made to the Standard Print Format will have to be done using a Customize Form. You can also checkout [adding fields in Print Formats](/erpnext/making-fields-visible-in-print-format).

Custom Print Format
-------------------

You can also create your own custom Print Formats by using a tool called [Print Format Builder](/erpnext/print-format-builder). This tool will help you in making a simple Customized Print Format by dragging and dropping fields in a format as per your preference.

![Customize Print Format](/files/customize-print-format.gif)  


For creating Custom Print Formats, ERPNext comes with several pre-defined templates in three styles, namely, Modern, Monochrome and Classic.

To create your versions, open an existing template from:

> Build > Views > Print Format

Print Settings
--------------

To edit/update your print and PDF settings, go to:

> Settings > Print Settings

![Print Settings](/files/print-settings.png)  


HTML Print Format
-----------------

For creating an HTML Print Format, you would require some knowledge of HTML, CSS, and Python. Here is an example of how a Print Format can be design which has very specific format.

![HTML Print Format](/files/customize-custom-print-format-1.png)  


Print Formats are provided on the server-side using the [Jinja Templating Language](https://jinja.palletsprojects.com/en/3.0.x/templates/). All forms have access to the doc object which contains information about the document that is being formatted. You can also access common utilities via the frappe module. To avail support when creating an HTML based print format, you can refer to [ERPNext Community forum](https://discuss.erpnext.com/), or start a new post for your query.

For styling, the [Bootstrap CSS Framework](http://getbootstrap.com/) is provided and you can enjoy the full range of classes.

#### References

1. [Jinja Templating Language: Reference](https://jinja.palletsprojects.com/en/3.0.x/templates/)
2. [Bootstrap CSS Framework](http://getbootstrap.com/)

#### Example


```
<h3>{{ doc.select_print_heading or "Invoice" }}</h3>
<div class="row">
    <div class="col-md-3 text-right">Customer Name</div>
    <div class="col-md-9">{{ doc.customer_name }}</div>
</div>
<div class="row">
    <div class="col-md-3 text-right">Date</div>
    <div class="col-md-9">{{ doc.get_formatted("invoice_date") }}</div>
</div>

        {%- for row in doc.items -%}
        
        {%- endfor -%}
    <table class="table table-bordered">
    <tbody>
        <tr>
            <th>Sr</th>
            <th>Item Name</th>
            <th>Description</th>
            <th class="text-right">Qty</th>
            <th class="text-right">Rate</th>
            <th class="text-right">Amount</th>
        </tr><tr>
            <td style="width: 3%;">{{ row.idx }}</td>
            <td style="width: 20%;">
                {{ row.item_name }}
                {% if row.item_code != row.item_name -%}
                <br>Item Code: {{ row.item_code}}
                {%- endif %}
            </td>
            <td style="width: 37%;">
                <div style="border: 0px;">{{ row.description }}</div>
            </td>
            <td style="width: 10%; text-align: right;">
                {{ row.qty }} {{ row.uom or row.stock_uom }}
            </td>
            <td style="width: 15%; text-align: right;">
                {{ row.get_formatted("rate", doc) }}
            </td>
            <td style="width: 15%; text-align: right;">
                {{ row.get_formatted("amount", doc) }}
            </td>
        </tr></tbody>
</table>
```
Notes
-----

1. To get date and currency formatted values use, `doc.get_formatted("fieldname")`
2. For translatable strings, use `{{ _("This string is translated") }}`

  

<!-- page: erpnext/erpnext__regional.md -->
---
title: "Regional"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/regional"
updated: "2026-07-02"
---

ERPNext aims to support local regulation for all the regions in the world. In most cases ERPNext is very flexible so you can easily add Custom Fields and make Custom Reports to support the regulation of your region.

As of mid-2017, ERPNext aims to pre-set additional fields and forms required for companies to easily submit reports to the relevant authorities.

This section is still under-development.

### India

* [India Compliance App](/erpnext/user/manual/en/india)
* [Lower Deduction Certificate](/erpnext/user/manual/en/lower-deduction-certificate)
* [TDS Setup for India](/erpnext/user/manual/en/tds-setup-india)

### United Arab Emirates

* [Requirements for UAE](/erpnext/user/manual/en/united_arab_emirates)
* [UAE Regional Fields](/erpnext/user/manual/en/UAE-regional-fields)
* [UAE VAT 201 Report in ERPNext](/erpnext/user/manual/en/uae-vat-201-report)
* [VAT/Excise Tax Implementation](/erpnext/user/manual/en/uae-vat-setup)

### Saudi Arabia

* [KSA VAT Management and Reporting](/erpnext/user/manual/en/simplified_ksa_vat_management_and_reporting)

### United States of America

* [Taxjar Integration](/erpnext/user/manual/en/taxjar_integration)

### Italy

* [Requirements for Italy](/erpnext/user/manual/en/italy)
* [Importing e-Invoice from Supplier](/erpnext/user/manual/en/import-e-invoice)

### France

* [Requirements for France](/erpnext/user/manual/en/france)
* [Sales and Payment Transactions](/erpnext/user/manual/en/local_overrides)
* [Le Fichier des Écritures Comptables [FEC]](/erpnext/user/manual/en/fichier_des_ecritures_comptables)

<!-- page: erpnext/erpnext__regional__regional-chart-of-accounts.md -->
---
title: "Regional Chart of Accounts"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/regional/regional-chart-of-accounts"
updated: "2026-07-02"
---

**ERPNext provides standard Chart of Accounts which are pre-configured based on the country or region, enabling users to get started quickly.**  

‎ 

Below are the available regional chart of accounts:


| **Region Name**                        | **Region Code** |
| -------------------------------------- | --------------- |
| Algeria                                | DZ              |
| Argentina                              | AR              |
| Australia                              | AU              |
| Benin **#**                            | BJ              |
| Brazil                                 | BR              |
| Burkina Faso **#**                     | BF              |
| Cameroon **#**                         | CM              |
| Canada                                 | CA              |
| Central African Republic **#**         | CF              |
| Chad **#**                             | TD              |
| Colombia                               | CO              |
| Comoros **#**                          | KM              |
| Congo **#**                            | CG              |
| Côte d'Ivoire **#**                    | CI              |
| Democratic Republic of the Congo **#** | CD              |
| El Salvador                            | SV              |
| Equatorial Guinea **#**                | GQ              |
| France                                 | FR              |
| Gabon **#**                            | GA              |
| Germany                                | DE              |
| Guatemala                              | GT              |
| Guinea **#**                           | GN              |
| Guinea-Bissau **#**                    | GW              |
| Hungary                                | HU              |
| India                                  | IN              |
| Indonesia                              | ID              |
| Mali **#**                             | ML              |
| Mexico                                 | MX              |
| Netherlands                            | NL              |
| Nicaragua                              | NI              |
| Niger **#**                            | NE              |
| Portugal                               | PT              |
| Senegal **#**                          | SN              |
| Singapore                              | SG              |
| Sweden                                 | SE              |
| Switzerland                            | CH              |
| Taiwan                                 | TW              |
| Togo **#**                             | TG              |
| Turkey                                 | TR              |
| United Arab Emirates                   | AE              |


:::note[# West and Central Africa]
ERPNext supports the SYSCOHADA (Système Comptable OHADA), which is the mandatory, unified accounting standard and chart of accounts for businesses operating in the 17 member states of the Organization for the Harmonization of Business Law in Africa (OHADA). 


These regions are highlighted in the above table (marked with #).
:::

<!-- page: erpnext/erpnext__remove-link-at-the-bottom-of-the-print-page.md -->
---
title: "Remove Link at the Bottom of the Print Page"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/remove-link-at-the-bottom-of-the-print-page"
updated: "2026-03-04"
---

**Question:**

How to remove the ERPNext link at the bottom of the page while printing it?

![](/files/tlLa26R.png)

 

**Solution:**

To remove the url at the bottom of the print page, following the below steps:

 

1) Click on the Print button.

![](/files/eoC7IPh.png)

 

2) Click on "More Settings"

![](/files/Sq2FLq9.png)

 

3) Uncheck the "Headers and Footers" checkbox.

![](/files/ubOMcEB.png)

 

4) Click on Save.

<!-- page: erpnext/erpnext__removing-description-removed-item-code-and-name.md -->
---
title: "Remove Description in Print Format"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/removing-description-removed-item-code-and-name"
updated: "2026-03-02"
---

 

**Question:**

I want to remove the description from the from my print format since it takes up too much space:

![](/files/cDYxb5o.png)

 

But when I do so using the [print format builder](/erpnext/print-format-builder), I end up losing my Item Code and Name as well. How to fix this?

![](/files/Fredaow.png)

 

 

**Answer:**

This is because you have **Compact Item Print** option enabled in the Print Settings.

![](/files/lCGM2tO.png)

 

You can disable this option and then uncheck the Description in the print format builder. This should solve the issue for you.

![](/files/6MI1aNw.png)

<!-- page: erpnext/erpnext__renaming-documents.md -->
---
title: "Renaming Documents\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/renaming-documents"
updated: "2026-03-04"
---


**Using Renaming feature, you can change the name of a master document.**

Using this feature you can also merge two master documents into a single one.

Check [List of Renamable Documents](/erpnext/renaming-documents#list-of-renamable-documents) for the list of all the documents that can be renamed in the system.

### Steps to rename a Document

**Step 1**: Go to the document that you wish to rename.

**Step 2**: From the drop-down menu, select the option 'Rename'.

![Document Renaming](/files/using-rename-documents-1.gif)

Alternatively, you can also click on the Title of the document, which will result in a pop-up, wherein you will be able to change the name of the document that you wish to rename.

![Document Renaming](/files/using-rename-documents-2.gif)

### Effect of Renaming

Renaming a document will affect all the existing transactions liked to this document. E.g., If you are changing the Item Code for an Item, the same will be updated in all the existing transactions wherein this Item is linked.

### List of Renamable Documents

Following is the list of all the documents that can be renamed.

1. Contact
2. Address
3. Warehouse
4. Supplier
5. Customer
6. User
7. Sales Partner
8. Project
9. Cost Center
10. Item Group
11. Item
12. Company
13. Role
14. Earning Type
15. Note
16. Serial No
17. Account
18. Territory
19. Terms and Conditions
20. Supplier Group
21. Workstation
22. Employee
23. Sales Taxes and Charges Master
24. Purchase Taxes and Charges Master
25. Price List
26. Party Type
27. Mode of Payment
28. Designation
29. Department
30. Deduction Type
31. Customer Group
32. Brand
33. Branch
34. Sales Person

## See also

1. [Bulk Rename](/erpnext/bulk-rename)

<!-- page: erpnext/erpnext__repack-entry.md -->
---
title: "Repack Entry\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/repack-entry"
updated: "2026-03-02"
---


Repack Entry is created for item bought in bulk, which is being packed into smaller packages. For example, item bought in tons can be repacked into Kgs.

Notes:

1. Purchase Item and repack will be have different Item Codes.
2. Repack entry can be made with or without BOM (Bill of Material).

In a Repack Entry, there can be one or more than one repack items. Let's check below scenario to understand this better.

Assume we are buying boxes of spray paint of specific colour (Green, Blue etc). And later re-bundling to create packs having multiple colours of spray paint (Blue-Green, Green-Yellow etc.) in them.

#### 1. New Stock Entry

`Stock > Documents > Stock Entry > New Stock Entry`

#### 2. Enter Items

Select Purpose as 'Repack Entry'.

For raw-material/input item, only Source Warehouse will be provided.

For repacked/output items, only Target Warehouse will be provided. You will have to provide valuation for the repack items.

![Repack Entry](/files/repack-1.png)

Update Qty for all the items selected.

#### 3. Submit Stock Entry

On submitting Stock Entry, stock of input item will be reduced from Source Warehouse, and stock of repack/output item will be added in the Target Warehouse.

![Repack Stock Entry](/files/repack-2.png)

<!-- page: erpnext/erpnext__report-permission-error.md -->
---
title: "Permission Error Problems"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/report-permission-error"
updated: "2026-03-04"
---

**Question:** User has roles like Account User and Account Manager assigned. Still, when accessing  Account Receivable report, User is getting an error message of no permission the territory master.

![Screenshot 2024-06-21 at 2.31.40 PM](/files/Screenshot 2024-06-21 at 2.31.40 PM.png)  


**Answer:**

As per the permission system in ERPNext, for the User to be able to access a form or a report, s(he) should have at-least read permission on all the link field in that form/report. Since Territory is a link field in Account Receivable report, please add a permission rule to let Account User/Manager have at-least Read permission on the Territory master. Please follow below-given steps to resolve this issue.

1. Roles assigned to User are Account User and Account Manager.
2. As indicates in the Error message, the user didn't have permission on the territory master. As per the default permission, none of the above role assigned to that User has any permission on the Territory master.
3. To resolve this issue, I have assigned Account User permission to Read Territory master.

![Screenshot 2024-06-21 at 2.26.27 PM](/files/Screenshot 2024-06-21 at 2.26.27 PM.png)

As per this permission update, User should be able to access Account Receivable report fine.

<!-- page: erpnext/erpnext__report-showing-multiple-rows-for-one-document.md -->
---
title: "Report Showing Multiple Rows for One Document"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/report-showing-multiple-rows-for-one-document"
updated: "2026-07-05"
---

Sometimes a report may show the same document number in multiple rows. This usually does not mean that the document has been duplicated. It means the report is showing more than one matching row of data for that document.

This is common in reports that include child table fields, linked records, or detailed accounting and stock entries.

## Most Common Reason: A Child Table Is Selected

Many ERPNext documents have child tables. For example:

- A **Sales Invoice** has multiple **Sales Invoice Items**.
- A **Purchase Order** has multiple **Purchase Order Items**.
- A **Payment Schedule** can have multiple due dates.
- A transaction can have multiple taxes, deductions, or accounting rows.

When a report includes fields from a child table, the report shows one row for each child row.

For example, if Sales Invoice `SINV-0001` has 3 item rows, and the report includes fields from **Sales Invoice Item**, the report can show:

```text
SINV-0001    Item A
SINV-0001    Item B
SINV-0001    Item C
```

The invoice is still one document. The report is showing the invoice once for every item row.

## Why This Happens

Reports are built from database rows. A parent document and a child table have a one-to-many relationship.

One parent document can have many child rows:

```text
Sales Invoice
  - Item 1
  - Item 2
  - Item 3
```

When the report includes child table data, Frappe needs to display each child row separately so that the child table values are visible. This is expected behavior.

## Other Reasons A Report Can Show Multiple Rows

### 1. Multiple Child Tables Are Included

If a report includes fields from more than one child table, the number of rows can increase further.

For example, if an invoice has 3 item rows and 2 tax rows, a poorly structured custom report may show more rows than expected because both child tables are being joined together.

In such cases, review the report design and include only the child table that is required.

### 2. The Report Shows Ledger Or Detail Entries

Some reports are intentionally detail-level reports. They are not designed to show one row per document.

For example:

- A General Ledger style report may show one row per accounting entry.
- A stock report may show one row per stock ledger entry.
- A receivable or payable report may show rows based on invoices, payments, or outstanding references.

The same voucher number can appear more than once because one document can create multiple ledger entries.

### 3. The Report Includes Linked Records With Multiple Matches

A document may be connected to multiple related records. For example, one invoice can be linked to multiple payment entries, delivery notes, serial numbers, batches, or accounting references.

If the report includes data from those linked records, the parent document can appear once for every matching linked record.

### 4. A Custom Query Report Has A Join Issue

In a custom Query Report, repeated rows may happen if the SQL query joins tables without the correct condition.

For example, joining a parent table and child table without matching the child row to its parent document can produce too many rows.

Check that the query joins child tables using the correct parent fields, such as:

```sql
child.parent = parent.name
```

Also check fields like `parenttype` and `parentfield` when the child table is shared or when the query needs to be more specific.

### 5. The Report Is Not Grouped

If the goal is to see one row per document, the report may need grouping or aggregation.

For example, instead of showing each item row separately, a report can group by Sales Invoice and show:

- Total quantity
- Total amount
- Count of item rows
- First or last date

This depends on whether you need a summary report or a detail report.

## How To Check Why Rows Are Repeating

1. Open one of the repeated documents.
2. Check whether it has multiple rows in a child table, such as Items, Taxes, Payment Schedule, or other detail tables.
3. In the report, check whether any selected column comes from a child table.
4. If it is a custom report, review the joins and filters.
5. Decide whether the report should show detail rows or one summarized row per document.

## How To Show One Row Per Document

If you want one row per document, try one of these approaches:

- Remove child table columns from the report.
- Use only fields from the parent DocType.
- Use grouping, such as grouping by document name.
- Use aggregate values such as sum, count, min, or max.
- Build a custom Query Report or Script Report that returns one row per parent document.

## Summary

Multiple rows for the same document are usually expected when the report includes child table data or other detail-level records.

The key question is: should the report show each detail row, or should it summarize the document into one row?

If the report is meant to answer item-level, tax-level, ledger-level, or stock-entry-level questions, multiple rows are correct. If it is meant to answer document-level questions, use parent fields, grouping, or a custom report design.

## Related Topics

- [Reports](https://docs.frappe.io/framework/user/en/desk/reports)
- [Report Builder](https://docs.frappe.io/framework/user/en/desk/reports/report-builder)
- [Query Report](https://docs.frappe.io/framework/user/en/desk/reports/query-report)
- [Script Report](https://docs.frappe.io/framework/user/en/desk/reports/script-report)
- [Child / Table DocType](https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype)

<!-- page: erpnext/erpnext__repost-accounting-ledger.md -->
---
title: "Repost Accounting Ledger | ERPNext Documentation"
description: "Safely regenerate General Ledger entries with Repost Accounting Ledger in ERPNext, preview old and new postings, process vouchers, and verify reports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/repost-accounting-ledger"
updated: "2026-08-14"
---

Nova Industries corrects a supported accounting field on a submitted transaction, but a report still reflects the earlier ledger values. The business document is now correct, yet its General Ledger entries must be rebuilt so reports agree with it.



Repost Accounting Ledger regenerates ledger entries for selected submitted transactions. It is an administrative repair tool, not a way to change the commercial meaning of a transaction.



Use it only for supported corrections or system repairs, then verify the affected document and accounting reports before treating the issue as resolved.



## Before you begin

Confirm the following:

1. You have the **System Manager** role. Standard Accounts roles do not have permission to create or submit this administrative record.
2. The source transaction is submitted and belongs to the company you will select.
3. The source document now contains the correct accounts, dimensions, amounts, taxes, and valuation information.
4. The voucher type is listed under **Allowed DocTypes** in [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings).
5. The affected posting period is open. ERPNext does not repost vouchers covered by a submitted [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher).
6. You have a backup and a test plan before processing a large or production-critical correction.

Reposting is supported only for configured voucher types. Common examples include [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice), [Purchase Invoice](https://docs.frappe.io/erpnext/purchase-invoice), [Payment Entry](https://docs.frappe.io/erpnext/payment-entry), [Journal Entry](https://docs.frappe.io/erpnext/journal-entry), Purchase Receipt, and Expense Claim.

## Allow a voucher type to be reposted

Open **Accounts Settings** and select the **Payments** tab. In the **Repost** section, add each permitted transaction type to **Allowed DocTypes**, then save.

Changing supported accounting fields after submission can trigger reposting for the DocTypes listed here. Remove a DocType when your organization does not want those post-submit changes to initiate a repost.



![Allowed DocTypes in the Repost section of ERPNext Accounts Settings](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-allowed-doctypes-settings327aa6.png)

Keep the list deliberate. Adding a DocType authorizes a sensitive accounting repair workflow; it is not a requirement to add every accounting transaction.

## Create a Repost Accounting Ledger record

Search for **Repost Accounting Ledger** from the Awesome Bar. The list shows draft and submitted repost records.



![Draft and submitted Repost Accounting Ledger records in ERPNext](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-listbadaf9.png)

Select **Add Repost Accounting Ledger**.

Choose the **Company** that owns the source vouchers. Leave **Delete Cancelled Ledger Entries** cleared for a normal repost.



![Company and Delete Cancelled Ledger Entries fields on a draft repost](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-draft-fields67744b.png)

In **Vouchers**, add the submitted documents that need recalculation. Select a **Voucher Type**, then select the corresponding **Voucher No**. The voucher list is restricted to submitted records from the selected company.

Select the pencil icon when you need to open and review the child-table row.



![A Journal Entry selected in the Vouchers table with the row pencil highlighted](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-voucher-row3d73a8.png)

The example uses Journal Entry `ACC-JV-2026-00005`, a $250 transfer from **Demo Bank Account** to **Cash**.



![The source Journal Entry with its balanced debit and credit highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-repost-accounting-ledger-repost-source-journal-entry.png)

Save the repost as a draft.

## Preview the regenerated entries

Select **Show Preview** before submitting. ERPNext generates the ledger map again from the current source document and compares it with the existing entries.



![Repost preview comparing existing and regenerated General Ledger entries](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-repost-accounting-ledger-repost-preview.png)

In the preview:

- Red rows are the existing General Ledger entries that will be replaced or reversed.
- Green rows are the entries ERPNext will generate from the current source document.

Check the accounts, debit and credit values, voucher number, Cost Center, and other dimensions. If a proposed row is wrong, return to the source transaction and correct it before continuing. Do not submit the repost in the hope that it will correct an incorrect source document.

## Submit and verify the repost

Submit the Repost Accounting Ledger record only after the preview is correct.



![A submitted Repost Accounting Ledger record](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-submittedb002eb.png)

ERPNext processes five or fewer selected vouchers immediately. When the record contains more than five vouchers, it queues the work in the background and displays a message that reposting has started.

After processing, open each source voucher and use **View &gt; Ledger**, or run the General Ledger report with the voucher number. Confirm that:

1. The intended accounts and dimensions are present.
2. Total debit equals total credit.
3. Old values no longer affect the report.
4. The related financial report now shows the expected result.

![General Ledger after reposting the example Journal Entry](https://novacompanies.m.frappe.cloud/files/repost-accounting-ledger-20260802-repost-general-ledgerb20a75.png)

Reposting changes ledger entries, not the submitted status or commercial meaning of the source transaction. If the transaction itself should be reversed, use its supported cancellation, return, credit note, debit note, or amendment workflow instead.

## Important fields and what they mean


| Field                           | What it controls                                                                                   | Guidance                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Company                         | Limits the selectable vouchers and ledger rebuild to one company                                   | Select the company that owns every voucher in the table.                                                                |
| Delete Cancelled Ledger Entries | Deletes existing cancelled GL, Payment Ledger, and Advance Payment Ledger rows before regeneration | Leave this cleared for normal use. Use it only for a diagnosed cleanup case under technical or implementation guidance. |
| Voucher Type                    | Identifies the transaction DocType to regenerate                                                   | The type must be present in Accounts Settings under Allowed DocTypes.                                                   |
| Voucher No                      | Identifies the submitted source document                                                           | Review the source document and its current ledger before adding it.                                                     |
| Show Preview                    | Compares current entries with the newly generated ledger map                                       | Treat the preview as a required review step, especially when accounts or dimensions changed.                            |


## Restrictions and safeguards

### Closed fiscal periods

ERPNext blocks reposting when a selected voucher falls on or before the latest submitted Period Closing Voucher date for that company. Reopen or correct a closed period only through your approved accounting controls.

### Deferred revenue and expense

A Sales Invoice with deferred revenue or a Purchase Invoice with deferred expense cannot be reposted through this tool. Use the supported [Deferred Accounting](https://docs.frappe.io/erpnext/deferred-accounting) workflow and verify the related schedules and entries.

### Immutable ledger

Reposting preserves the audit-oriented behavior of the [immutable ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext). With the normal option, ERPNext reverses the old accounting effect and creates the regenerated effect through supported ledger logic instead of inviting users to edit GL Entry rows directly.

### Large batches

Do not combine unrelated corrections merely to process them together. Test a representative voucher first, process the smallest useful batch, wait for background work to complete, and verify reports before continuing.

## Troubleshooting

### The Voucher Type is not available

Add the DocType to **Accounts Settings &gt; Payments &gt; Repost &gt; Allowed DocTypes**, save the settings, then reopen the repost record. If the type should not permit post-submit accounting changes in your organization, do not add it merely to bypass the restriction.

### The voucher number is not available

Confirm that the Company matches the source document, the voucher is submitted, and the selected Voucher Type is correct. Draft and cancelled vouchers are not offered for a normal repost.

### ERPNext says the voucher is in a closed fiscal year

The voucher date is covered by a submitted Period Closing Voucher. Do not bypass the close casually. Follow your controlled period-reopening process and obtain the required accounting approval.

### ERPNext says deferred accounting is enabled

The selected invoice contains deferred revenue or deferred expense. Reposting that invoice is blocked because it can conflict with its deferred schedules. Review the deferred accounting records and use the appropriate process for that feature.

### The preview does not match the intended correction

Stop and inspect the source transaction. Check its account, amount, tax, Cost Center, dimensions, exchange rate, and linked stock valuation. The preview reflects the source document as it exists now.

### The report still shows an unexpected balance

Refresh the report and confirm its company, date range, finance book, currency, account, and voucher filters. Then compare the source document, preview, and General Ledger. Another voucher may also contribute to the balance.

## FAQs

### Does reposting change the source document?

No, It recalculates ledger entries from the source document's current data. It does not change the document's submitted status, items, party, or commercial purpose.

### Should I use this instead of cancelling and amending a wrong transaction?

No, Correct the transaction through its supported business workflow when the source document itself is wrong. Repost only when the source is correct and its accounting entries need regeneration.

### Can I repost several vouchers together?

Yes, Add multiple vouchers from the same company. Five or fewer are processed immediately; more than five are queued in the background. Smaller, related batches are easier to verify.

### What does Delete Cancelled Ledger Entries do?

It removes existing cancelled GL, Payment Ledger, and Advance Payment Ledger rows for the selected vouchers before rebuilding them. It is an exceptional cleanup option, not the default way to repost.

### Why are the old and new rows identical in the preview?

That can be correct when you are verifying or rebuilding entries without changing their accounting values. If you expected a difference, confirm that the intended source-field correction was saved before generating the preview.

### Does a draft repost affect accounting reports?

No, Saving the record and generating a preview do not replace the ledger entries. The accounting rebuild occurs when the repost is submitted and processed.

## Related topics

- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [Accounting Entries](https://docs.frappe.io/erpnext/accounting-entries)
- [Immutable Ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext)
- [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings)
- [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher)

<!-- page: erpnext/erpnext__repost-item-valuation.md -->
---
title: "Repost Item Valuation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/repost-item-valuation"
updated: "2026-02-11"
---



## Overview

The **Repost Item Valuation** feature in ERPNext is used to recalculate item valuation, stock balances, and related accounting values when inconsistencies occur due to backdated entries or stock ledgers related issues.

This process ensures that inventory valuation and General Ledger (GL) entries remain accurate and consistent.

---

## When to Use Repost Item Valuation

Use this feature in the following scenarios:

* Backdated stock transactions are created or modified
* Stock Ledger Entries (SLEs) have incorrect balances
* Negative stock issues appear due to reposting problems
* After fixing bugs or applying patches related to stock or valuation
* Data migration or bulk import of stock transactions

---

## What Repost Item Valuation Does

Reposting item valuation performs the following actions:

* Recalculates **Stock Ledger Entries (SLEs)** from a specific point in time
* Recomputes **Running Available Stock** and **Stock Balance**
* Re-evaluates item valuation based on the valuation method
* Updates **Stock Value** and **Valuation Rate**
* Reposts related **General Ledger entries**, if required

---

## Types of Reposting

### 1. Automatic Reposting

ERPNext automatically creates reposting entries when:

* Backdated stock transactions are saved
* System detects that reposting is required

These entries are processed in the background by scheduled jobs.

---

### 2. Manual Repost Item Valuation

Users can manually trigger reposting using the **Repost Item Valuation** tool.

#### Steps:

1. Search **Repost Item Valuation**.
2. Click on **New**.
3. Fill in the required details:

   * **Company** – Company for which reposting is required
   * **Item Code** (optional) – Repost valuation for a specific item
   * **Warehouse** (optional) – Limit reposting to a warehouse
   * **Posting Date** and **Posting Time** – Starting point for reposting
4. Save the document.
5. Click on **Start Reposting**.

The system will enqueue reposting jobs based on the provided filters.

---

## Using Stock Ledger Variance Report with Reposting

Before triggering reposting, it is recommended to use the **Stock Ledger Variance** report to:

* Identify incorrect Stock Ledger Entries
* Filter rows with quantity or balance differences
* Select affected entries and create reposting entries directly

This helps reduce the scope of reposting and improves performance.

---

## Performance Considerations

* Reposting can be resource-intensive for large datasets
* It is recommended to:

  * Limit reposting by item, warehouse, or date
  * Run reposting during non-peak hours
* Avoid triggering full reposting unless necessary

---

## Common Issues and Troubleshooting

### Reposting Takes Too Long

* Check the number of affected entries
* Narrow down filters (Item, Warehouse, Date)
* Ensure background workers are running

### Negative Stock Errors After Reposting

* Verify inward entries exist before outward transactions
* Check posting dates and times
* Use Stock Reconciliation if required

### GL Entries Not Updated

* Ensure **Update Stock** is enabled for relevant transactions
* Confirm that accounting reposting is allowed

---

## Best Practices

* Always review stock data using reports before reposting
* Avoid frequent backdated transactions
* Keep ERPNext updated to the latest patch version
* Use reposting tools incrementally instead of full reprocessing

---

## Notes

* Repost Item Valuation affects historical data; use it carefully
* Reposting will change the closing balances of the respective financial year, so use it carefully.
* Avoid using reposting for closed financial years, as it will change the closing balances of the closed financial years.
* Users should have appropriate permissions to perform reposting
* Applicable primarily to stock-impacting transactions

---

The **Repost Item Valuation** feature is a critical maintenance tool that helps ensure inventory accuracy and accounting integrity in ERPNext.

<!-- page: erpnext/erpnext__request-for-quotation.md -->
---
title: "Request for Quotation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/request-for-quotation"
updated: "2026-02-27"
---

**A Request for Quotation is a document that an organization sends to one or more suppliers asking a quotation for items.**

![Buying Flow](/files/buying_flow_rfq.png)  


To access **Request for Quotation**, open the "Buying" workspace and, under "Reports & Masters" > "Buying", click on "Request for Quotation".

1. Prerequisites
----------------

Before creating and using a **Request for Quotation**, it is advised that you create the following first:

* [Supplier](/erpnext/supplier)
* [Item](/erpnext/item)

2. How to create a Request For Quotation
----------------------------------------

1. Go to the **Request For Quotation** list and click on "+ Add Request for Quotation".
2. Enter the *Required Date*, by which you'll need the requested materials.
3. Fill the "Suppliers" list with possible suppliers.  
If you set a *Contact* and *Email Id*, that can later be used for sending the **Request For Quotation** via email and grant access to the supplier portal.
4. In the next table, enter the required items along with UOM and quantity, as well as the target warehouse.
5. The *Warehouse* can be left blank if *Maintain Stock* is not enabled for the item.
6. If you want to send the **Request for Quotation** to your suppliers as an email, you can create an **Email Template** and select it here. In the template, you can use special variables for supplier specific data:  
  



	1. `{{ update_password_link }}`: A link where your supplier can set a new password to log into your portal.
	2. `{{ portal_link }}`: A link to this RFQ in your supplier portal.
	3. `{{ supplier_name }}`: The company name of your supplier.
	4. `{{ contact.salutation }} {{ contact.last_name }}`: The contact person of your supplier.
	5. `{{ user_fullname }}`: Your full name.  
	  
	Apart from these, you can access all values in this RFQ, like `{{ message_for_supplier }}` or `{{ terms }}`.
7. You can check how the email will look for a specific supplier by using the "Preview Email" button.

![Preview Email](/files/email-preview.png)
8. If you want to send further attachments to your suppliers, you can enable the checkbox   
*Send Attached Files*. This will add each file attached to the **Request for Quotation** as an attachment to each supplier email.
9. Once you're done, save the **Request for Quotation** as a draft.
10. When you're ready, you can submit the **Request for Quotation**. This will trigger an email to each supplier that has *Send Email* enabled.

![Create RFQ](/files/rfq-create.png)  


A Request for Quotation (RFQ) can also be created from a submitted Material Request. Once an RFQ is created, you can print and send suppliers the PDF which will have all the details you entered relevant to the RFQ. You can also get their reply (Supplier Quotation) in ERPNext itself, see section [4.1 Supplier Quotation by User](#41-supplier-quotation-by-user). However, for a large number of items, your supplier may be more comfortable with an Excel sheet, etc.

3. Features
-----------

### 3.1 Get items from

The items in the items table can be fetched from other documents. The options are: Material Request, Opportunity, and Possible Supplier.

* **Material Request**: Items will be fetched from a submitted Material Request that you select. A Material Request can be searched with some matching words and a date range can also be selected to filter the Material Requests.
* **Opportunity**: Items will be fetched from a saved Opportunity. A date range can be selected here also.
* **Possible Supplier**: Select a possible supplier. Then if you have any submitted Material Requests against this supplier, items can be fetched from that.

![RFQ get items](/files/rfq-get-items.png)  


### 3.2 Get Suppliers

Instead of entering the suppliers manually in the table, you can also fetch them using the 'Get Suppliers' button. When you click on **Tools > Get Suppliers**, you will see the field 'Get Suppliers By'. There are two options to fetch suppliers: By Tag or By Group.

* **By tag**: Go to 'Tag Category' via searching from the search bar. You must have created tags here first and assigned them to a Supplier in the Buying module. Then you can select 'By Tag'. On clicking Add 'All Suppliers', suppliers with matching tags will be fetched.
* **By Group**: Select 'Supplier Group' and choose the supplier group from which suppliers need to be added. For example, if you select Hardware, all your hardware suppliers will be added so that you can get a quote from all of them.

![RFQ get suppliers](/files/rfq-get-suppliers.png)  


In the Supplier table, on expanding a row with the inverted triangle, you'll see an option 'Download PDF' which will open a PDF of the RFQ.

### 3.3 Link to Material Requests:

When you click on **Tools > Link to Material Requests**, it links the Request for Quotation to available Material Requests. The items should be the same in the Request for Quotation and the Material Request.

![Link to Material Request](/files/link-to-material-request.png)  


Now, when the Request for Quotation is saved, you can see in the Dashboard that it is linked to the Material Request. If there are multiple Material Requests with the same items, then the link will be created with the newest Material Request.

### 3.5 Terms and Conditions

In Sales/Purchase transactions, there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/erpnext/terms-and-conditions)

### 3.6 Print Settings

#### Letterhead

You can print your request for quotation/purchase order on your company's letterhead. Know more [here](/erpnext/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when you print it.

#### Print Headings

Titles of your documents can be changed. Know more [here](/erpnext/print-headings).

#### Special properties

When printing a RFQ via the "Tools > Download PDF" button, you are asked select the specific supplier you want to address. In the **Print Format** for RFQ, this information can be accessed via special properties:

* `{{ doc.vendor }}` holds the selected supplier ID.
* `{{ doc.items[i].supplier_part_no }}` holds the *Supplier Part Number* of a requested line item.

The data of the first supplier will be used while rendering the standard print preview. If you want to print for a different supplier, please use the "Tools > Download PDF" button.

4. Creating a Supplier Quotation after RFQ
------------------------------------------

After creation of Request for Quotation, there are two ways to generate Supplier Quotation from Request for Quotation.

### 4.1 Supplier Quotation by User

1. Open Request for Quotation and click on **Supplier Quotation > Create**.

![Supplier Quotation from RFQ](/files/make-supplier-quotation-from-rfq.png)
2. Select the Supplier, click on the supplier again. In this page, click on the + next to 'Supplier Quotation'. A new Supplier Quotation page will be opened, user has to enter the quantity, rate and submit it.

![Supplier Quotation from Supplier](/files/supplier-quotation-from-sup.png)

### 4.2 Supplier Quotation from Supplier

1. If a [Contact](/erpnext/contact) is created for the Supplier and an email address is associated with the Contact, the Contact details and the email address will be fetched on selecting the Supplier. Create a Contact and email address if not present already.
2. Click on **Tools > Send Emails to Suppliers**.

**If the Supplier's account is not present**: The system will create the Supplier's account and send details to the Supplier. The Supplier will need to click on the link (Password Update) present in the email. After the password update, the Supplier can access their portal with the 'Request for Quotation' form. The Supplier will be created as a Website User.

![Supplier email if account not present](/files/supplier-email-with-update-password.png)  


**If Supplier's account is present**: The system will send a Request for Quotation link to the Supplier. The Supplier must log in using his credentials to view the Request for Quotation form on the portal.

![Supplier email if account present](/files/supplier-email-normal.png)
3. Either way, when the Supplier logs in, the following screen will be shown to them. From here they can send you a quotation:

![Supplier Quotation Screen](/files/rfq-supplier-quotation.png)  


The Supplier has to enter the amount and notes (payment terms) on the form and click on Submit. In the Quotations section, previous quotations will be visible.
4. On submission, ERPNext will create a Supplier Quotation (draft mode) against the Supplier. The user has to review the Supplier Quotation and submit it. When all the items from the Request for Quotation have been quoted by a Supplier, the quote status is updated to 'Received' in the 'Suppliers' table of the Request for Quotation.

![RFQ status after supplier quote](/files/rfq-supplier-quoted.png)

Read [Supplier Quotation](/erpnext/supplier-quotation) to know more.

5. Video
--------

### 6. Related Topics

1. [Purchase Order](/erpnext/purchase-order)
2. [Supplier](/erpnext/supplier)
3. [Supplier Quotation](/erpnext/supplier-quotation)
4. [Quotation](/erpnext/quotation)
5. [Material Request](/erpnext/material-request)

<!-- page: erpnext/erpnext__request-for-raw-materials-from-sales-order.md -->
---
title: "Request Raw Materials from a Sales Order | ERPNext Documentation"
description: "Create an ERPNext Material Request for BOM raw materials directly from one submitted Sales Order, including exploded-item and ordered-quantity options."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/request-for-raw-materials-from-sales-order"
updated: "2026-07-25"
---

Create a [Material Request](/erpnext/material-request) directly from one submitted [Sales Order](/erpnext/sales-order) when you need to procure raw materials for its manufactured Items. Use a [Production Plan](/erpnext/production-plan) when planning several Sales Orders or broader production demand together.

## Before you begin

Confirm:

- The Sales Order is submitted.
- Each manufactured Item has an active default [Bill of Materials](/erpnext/bill-of-materials).
- BOM quantities and UOMs are correct.
- Warehouses and projected quantities are current.
- You have permission to create and submit Material Requests.

This action is intended for manufactured Items. A purchased finished good without a BOM will not produce raw-material requirements.

## Create the Material Request

1. Open the submitted Sales Order.
2. Select **Create**.
3. Select **Request for Raw Materials**.

![The Sales Order Create menu with Request for Raw Materials highlighted.](https://novacompanies.m.frappe.cloud/files/raw-materials-create-menu.png)

ERPNext opens a dialog containing eligible finished Items with BOMs.

4. Review the finished Items and required quantities.
5. Change the BOM only when another valid BOM should be used.
6. Select the source and target Warehouses or other options shown by your version.
7. Choose whether to include exploded Items or ignore existing ordered quantity.
8. Select **Create** or **Make**.

ERPNext creates a Material Request containing the calculated raw materials.

## Review the Material Request

Check:

- Material Request Type.
- Schedule Date.
- Item, Quantity, UOM, and Warehouse.
- Links to the Sales Order and BOM.
- Projected stock and existing supply.

![The generated Material Request with calculated raw-material rows.](https://novacompanies.m.frappe.cloud/files/raw-materials-material-request.png)

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock. Select the highlighted pencil icon to open the full child-row editor when you need additional planning fields.

Submit the Material Request only after confirming that it will not duplicate existing procurement or production supply.

## Options in the dialog


| Option                      | Effect                                                                                        |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| Include Exploded Items      | Uses lower-level raw materials from multi-level BOMs instead of only the immediate components |
| Ignore Existing Ordered Qty | Requests the calculated requirement without reducing it for quantities already ordered        |
| BOM                         | Selects which active BOM supplies the component structure                                     |


Field labels can vary by version. Review the generated Items rather than relying only on the option name.

## Choose this workflow or Production Plan


| Requirement                                     | Recommended workflow                                   |
| ----------------------------------------------- | ------------------------------------------------------ |
| One Sales Order needs raw-material procurement  | Request for Raw Materials from Sales Order             |
| Several Sales Orders need consolidated planning | Production Plan                                        |
| Manufacture and operations must be scheduled    | Production Plan and [Work Orders](/erpnext/work-order) |
| Replenishment is driven by stock levels         | Reorder or Material Request planning                   |


## Troubleshooting


| Problem                                 | What to check                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------- |
| Menu action is missing                  | Confirm the Sales Order is submitted and contains a manufactured Item with a valid BOM |
| Finished Item is absent from the dialog | Check the default and active BOM                                                       |
| Quantities are unexpected               | Review Sales Order Qty, BOM Qty, conversion factors, scrap, and exploded-item behavior |
| Duplicate procurement is suggested      | Review projected quantity and avoid Ignore Existing Ordered Qty unless intentional     |
| Wrong Warehouse is used                 | Review Item, BOM, Company, and dialog Warehouse defaults                               |


## Frequently asked questions

### Does this create a Purchase Order?

No. It creates a Material Request. Continue through your procurement workflow to create a [Request for Quotation](/erpnext/request-for-quotation) or [Purchase Order](/erpnext/purchase-order).

### Is the Material Request submitted automatically?

Confirm the resulting document's status in your current version and approval workflow. Review it before submission.

### Can I use a non-default BOM?

Yes, when the dialog permits selecting another active BOM.

### Should I enable Ignore Existing Ordered Qty?

Only when you intentionally want to request the full requirement despite existing supply.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Material Request](/erpnext/material-request)
- [Bill of Materials](/erpnext/bill-of-materials)
- [Production Plan](/erpnext/production-plan)
- [Purchase Order](/erpnext/purchase-order)

<!-- page: erpnext/erpnext__restore-deleted-erpnext.md -->
---
title: "Deleting and Restoring Documents\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/restore-deleted-erpnext"
updated: "2026-03-04"
---


**In ERPNext, you can delete a document if not needed. They can be masters like Items, Customer or transactions like Sales Order, Payment Entries, etc.**

To delete a document, you can go to the dropdown menu of the document and select 'Delete'.

![Restore Deleted Document](/files/using-restore-1.png)

For bulk deletion, you can select multiple Cancelled records and delete them at once from the List View.

![Restore Deleted Documents](/files/using-restore-3.gif)

> Note: Any submittable document will not be deleted after submission. To delete a submitted document, you will be required to first 'cancel' the document.

## Restoration of Deleted Documents

Further, any document, if deleted by mistake, or is required after deletion, can also be restored from the Deleted Documents list.

To access Deleted Documents, go to:

> Home > Settings > Data > Deleted Documents

### 1. How to Restore Deleted Documents

1. Go to Deleted Documents List
2. Open the deleted Document
3. Click on the **Restore** button.

![Restore Deleted Document](/files/using-restore-2.gif)

> Note: If the document was deleted after getting ** canceled**, it would be restored with a new name.

> Further, Only those Users having System Manager Role assigned to them can restore deleted documents.

<!-- page: erpnext/erpnext__retain-sample-stock.md -->
---
title: "Retaining Sample Stock\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/retain-sample-stock"
updated: "2026-02-27"
---


**Sample stock is a batch of any Items stored for analyzing should the need arise later.**

The Item for which sample stock is stored can be raw material, packaging material, or finished product.

## 1. Prerequisites
Before using sample retention, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Batch](/erpnext/batch)
* [Warehouse](/erpnext/warehouse)

## 1. How to Set Sample Retention Warehouse in Stock Settings

It is advised to create a new Warehouse separately for retaining samples and not use it in production.

![Sample Retention Warehouse](/files/sample-warehouse.png)

### 1.2 Enable Retain Sample in Item master
Retain Sample is based on Batch hence Has Batch No should be enabled first. Check Retain Sample and set the Maximum allowed samples for a batch.

![Retain Sample](/files/retain-sample.png)

### 1.3 Make Stock Entry

* Whenever a [Stock Entry](/erpnext/stock-entry) is created with the purpose as Material Receipt, for items which have Retain Sample enabled, the Sample Quantity can be set during that Stock Entry. You need to select the Batch Number for the Item/Items. Sample quantity cannot be more than the Maximum sample quantity set in Item Master.

 ![Retain Sample](/files/material-receipt-sample.png)

* On submission of this Stock Entry, button 'Make Retention Stock Entry' will be available to make another Stock Entry for the transfer of sample items from the mentioned batch to the retention warehouse set in Stock Settings.

 ![Sample Retention Button](/files/sample-retention-button.png)

* Clicking this button will direct you to new Stock Entry of type 'Material Transfer'. This entry is transfering your sample retention from your Target Warehouse (Stores) to the Sample Retention Warehouse. It will contain all the information, verify and click Submit.

 ![Retain Sample](/files/material-transfer-sample.png)

### 2. Related Topics
1. [Warehouse](/erpnext/warehouse)

<!-- page: erpnext/erpnext__return-rejected-item.md -->
---
title: "Return Rejected Items\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/return-rejected-item"
updated: "2026-03-02"
---


In the Purchase Receipt, you can receive the Items in the Accepted or the Rejected Warehouse.

If you are creating Purchase Return for the items received in the Rejected Warehouse, then create return entry following these steps.

1. In the Purchase Receipt Item table, for the item to be returned, in the Received Qty field, enter return entry in negative.
2. In the Accepted Warehouse field, set value as zero.
3. In the Rejected Warehouse field, set the quantity to be returned in negative.

For detailed steps on how to create Purchase Return Entry for the Rejected Item, refer to the below example.

![Returning Rejected Items](/files/purchase-return.gif)

<!-- page: erpnext/erpnext__returned_materials_against_work_order.md -->
---
title: "Returned Materials Against Work Order\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/returned_materials_against_work_order"
updated: "2026-03-02"
---


To access the Returned Materials Against Work Order, go to:

> Home > Manufacturing > Reports > Returned Materials Against Work Order

![Task](/files/returned-materials-against-work-order.png)

This report shows the information about the raw materials which has been returned from the work in progress warhouse against the work orders.

<!-- page: erpnext/erpnext__reverse-charge-mechanism-rcm.md -->
---
title: "Reverse Charge Mechanism (RCM)"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reverse-charge-mechanism-rcm"
updated: "2026-08-14"
---

Nova Industries buys a specialist service from Orion Advisory, a supplier that does not charge tax on its invoice. Local rules require Nova, as the buyer, to recognise and settle the tax itself. Reverse charge accounting separates the supplier payable from the tax liability and, where allowed, records the related input tax credit.



ERPNext provides the accounting building blocks, but the tax rate, eligibility, return reporting, and account classification come from your local tax rules. Have a tax adviser approve the template before production use.

## Set up the accounts


| Account              | Purpose                                    |
| -------------------- | ------------------------------------------ |
| RCM Tax Payable      | Liability for tax the company must settle. |
| RCM Input Tax Credit | Eligible recoverable tax.                  |
| RCM Tax Expense      | Non-creditable portion, when applicable.   |


## Create a purchase tax template

1. Create a Purchase Taxes and Charges Template dedicated to reverse charge.
2. Add a tax row that credits the RCM payable account at the approved rate.
3. Add a matching input-credit row when the tax is recoverable, or use an expense account for the non-creditable portion.
4. Test the supplier payable, tax liability, input credit, and invoice total before enabling the template for routine use.

![Purchase Taxes and Charges Template used as the base for reverse charge](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-overview.png)



![Purchase tax row with calculation and account fields](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-tax-row.png)



## Apply and verify

1. Create the Purchase Invoice for the supplier’s bill amount.
2. Apply the RCM template in Taxes and Charges.
3. Confirm the supplier outstanding amount does not incorrectly include tax the supplier did not charge.
4. Submit and inspect Accounting Ledger or General Ledger.
5. Settle or adjust the RCM payable through the approved tax-payment process.

![Transaction result after applying a purchase tax template](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-templates-purchase-template-result.png)



## Troubleshooting

### The supplier payable includes the reverse charge tax

Review Add or Deduct, Included in Print Rate, account heads, and the second input-credit or expense row. The supplier should normally remain payable only for the supplier bill when the supplier did not charge the tax.

### The tax credit is only partly eligible

Split the amount between an input-credit account and a tax-expense account using approved rates or rows.

## Frequently asked questions

### Is this configuration country-neutral?

The accounting pattern is reusable, but the legal rules are not. Use country-specific rates, accounts, returns, and evidence.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__reviews_and_rating.md -->
---
title: "Reviews and Ratings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reviews_and_rating"
updated: "2026-03-02"
---

Feedback is important to gauge the public sentiment of a product being sold. You can measure your product's performance by adding **Reviews and Ratings** to the Website Item's page. To enable this go to:

> E Commerce Settings > Add-ons > Enable Reviews and Ratings

Once this is done, there will be a provision in every Website Item's page to leave a review on the product.

#### Who can leave reviews?
Users that are also **Customers** in the system will be able to see the **Write a Review** button. These users must also have the **Customer Role** to be permitted to add reviews.

The average reviews are automatically calculated and a summary is displayed.

![Item Reviews](/files/item-reviews.png)

<!-- page: erpnext/erpnext__role-and-role-profile.md -->
---
title: "Role and Role Profile\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-and-role-profile"
updated: "2026-02-26"
---

**A Role defines the permissions for accessing various documents in ERPNext.**

Roles define a set of permissions which can be set from the Roles Permission Manager. Most commonly used roles are already defined in ERPNext, you can use the system with them. If needed, you can add more roles. For example, if you assign the Sales User role to a user, they'll be able to access documents like Quotations and Sales Orders since the permissions are already set for the role Sales User.

**Role profiles store different roles so that multiple roles can be assigned at once.**

Role Profiles act as a template to store and select multiple roles. This Role Profile can then be assigned to a User. For example, a Sales Supervisor will have the roles Employee, Sales Manager, Sales User, and Sales Master Manager. Role Profiles are useful to assign multiple roles at once when adding multiple employees.

To access Role, go to:

> Home > Users and Permissions > Role

## 1. How to add a Role

1. Go to the Role list, click on New.
2. Enter a name for the Role.
3. Choose whether the Role has desk access. A role that has desk access can access ERPNext modules and the company's documents. The level of access depends on the roles assigned to the user.
4. Save.

You can add two factor authentication for the role and also restrict it to a specific domain. From here, you can go to the Roles Permission Manager and set permissions for the role across different DocTypes.

![Permissions for new Role](/files/role-permissions.png)

## 2. How to add a Role Profile

To access Role Profile, go to:

> Home > Users and Permissions > Permissions > Role Profile

1. Go to the Role Profile list, click on New.
2. Enter a name.
3. Select the roles you want to assign to this profile.
4. Save Role Profile

<!-- page: erpnext/erpnext__role-based-permissions.md -->
---
title: "Role Based Permissions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-based-permissions"
updated: "2026-03-02"
---

**Permission to different documents can be controlled using Role Based Permissions.**

ERPNext has a role-based permission system. It means that you can assign Roles to Users, and Permissions can be set on Roles. The Role Permissions Manager allows you to set which roles can access which documents and with what permissions (read, write, submit, etc.).

Once roles are assigned to a user, their access can be limited to specific documents. The permission structure allows you to define different permission rules for different fields using a concept called **Permission Level** of a field.

1. How to use the Role Permissions Manager
------------------------------------------

To start using the Role Permission Manager, go to: > Home > Users and Permissions > Role Permissions Manager

![Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager](/files/setting-up-permissions-leave-application.png)  


Permissions are applied on a combination of:

* **Roles:** As we saw earlier, Users are assigned Roles and it is on these Roles that permission rules are applied. For example, a sales user may be given the roles of an Employee and a Sales User.

Examples of Roles include Accounts Manager, Employee, HR User, etc.
* **Document Types:** Each type of document, master or transaction, has a separate list of role-based permissions as seen in the preceding screenshot.

Examples of Document Types are Sales Invoice, Leave Application, Stock Entry, etc.
* **Permission Levels:** In each document, you can group fields by "levels". Each group of fields is denoted by a unique number (0 to 9). A separate set of permission rules can be applied to each field group. By default, all fields are of level 0.

Permission "Level" connects fields with level X to a permission rule with level X. To know more click [here](/erpnext/changing-the-properties-of-a-field-based-on-role).
* **Document Stages:** Permissions are applied on each stage of the document like Creation, Saving, Submission, Cancellation, and Amendment. A role can be permitted to Print, Email, Import or Export data, access Reports, or define User Permissions.
* **User Permissions:** Using User Permissions in ERPNext a user can be restricted to access only specific Documents for that Document Type. Eg: Only one Territory from all Territories. User Permissions defined for other Document Types also get applied if they are related to the current Document Type through Link Fields.

For example, a Customer is a link field in a Sales Order or Quotation. In the Role Permissions Manager, User Permissions can be set using the 'Set User Permissions' button.

To set User Permissions based on documents/fields go to: > Home > Users and Permissions > Permissions > [User Permissions](/erpnext/user-permissions)
* **Add a New Rule**: In the Role Permissions Manager, to add a new rule, click on the **Add a New Rule** button and a pop-up box will ask you to select a Role and a Permission Level. Once you select this and click on 'Add', this will add a new row to your rules table.

2. How Role Based Permissions Work
----------------------------------

Leave Application is a good example that encompasses all areas of a Permission System.

* It should be created by an Employee. For this, Employee Role should be given Read, Write, Create permissions.

![Giving Read, Write and Create Permissions to Employee for Leave Application](/files/setting-up-permissions-employee-role.png)
* An **Employee** should only be able to access his/her Leave Application. Hence, User Permissions record should be created for each User-Employee combination.

![Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager](/files/setting-up-permissions-employee-user-permissions.png)
* If you want an **Employee** to only select a document in another document and not have read access to that document as a whole, then grant only Select perm to the role, Employee.

![Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager](/files/setting-up-select-permissions-employee.png)
* **HR Manager** should be able to see all Leave Applications. Create a Permission Rule for HR Manager at Level 0, with Read permissions. Apply User Permissions should be disabled.

![Giving Submit and Cancel permissions to HR Manager for Leave Applications. 'Apply User Permissions' is unchecked to give full access.](/files/setting-up-permissions-hr-manager-role.png)
* **Leave Approver** should be able to see and update Leave Applications of employees under him/her. Leave Approver is given Read and Write access at Level 0. Relevant Employee Documents should be enlisted in the User Permissions of Leave Approvers. (This effort is reduced for Leave Approvers mentioned in Employee Documents, by programmatically creating User Permission records).

![Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.'Apply User Permissions' is checked to limit access based on Employee.](/files/setting-up-permissions-leave-approver-role.png)
* It should be Approved/Rejected only by HR User or Leave Approver. The Status field of a Leave Application is set at Level 1. HR User and Leave Approver are given Read and Write permissions for Level 0, while everyone else (All) are given Read permission for Level 1.

![Limiting read access for a set of fields to certain Roles](/files/setting-up-permissions-level-1.png)
* **HR User** should be able to delegate Leave Applications to his/her subordinates. HR User is given the right to Set User Permissions. A User with HR User role would be able to define User Permissions on Leave Application for other users.

![Let HR User delegate access to Leave Applications by checking 'Set User Permissions'. This will allow HR User to access User Permissions Manager for 'Leave Application'](/files/setting-up-permissions-hr-user-role.png)

In case you have correctly assigned the roles but still you're getting errors when accessing documents, refer [this page](/erpnext/report-permission-error).

### 3. Related Topics

1. [User Permissions](/erpnext/user-permissions)
2. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__role-permission-for-page-and-report.md -->
---
title: "Role Permission for Page and Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-permission-for-page-and-report"
updated: "2026-03-02"
---

**Access to different pages and reports can be controlled in Role Permission for Page and Report.**

Document types are Sales Order, Customer, Supplier, etc. They are a **document type** meaning they can contain multiple documents of that type. A Page is a single page like [Selling Settings](/erpnext/selling-settings). You cannot create multiple Selling Settings, but you can create multiple Sales Orders.

In ERPNext, user can make a custom user interface using Page and a custom report using [Report Builder](/framework/user/en/desk/reports/report-builder) or [Query Report](/framework/user/en/desk/reports/query-report). ERPNext has a [role-based permission system](/erpnext/role-based-permissions) where you can assign roles to the user. The same role can be assigned to the page and report to access them.

If the user has enabled developer mode, then they can add the roles directly in the page and report record. In that case, the permissions will also be reflected in the JSON file for the page/report. Consider you want to restrict the roles that can access certain pages and reports in ERPNext, this can be done via the Role Permission for Page and Report.

To access Role Permission for Page and Report, go to:

> Home > Users and Permissions > Role Permission for Page and Report

## 1. How to use Role Permission for Page and Report Tool

If developer mode is disabled, the user can assign the roles to the page and report, using "Role Permission for Page and Report" page.

![Tools to assign custom roles to the page](/files/role-permission-for-page-and-report.png)

### 1.1 Reset to defaults

Using the "Reset to Defaults" button, the user can remove the custom permissions applied on a page or report. Then default permissions will be applicable on that page or report.

![Reset the default roles](/files/reset-roles-permission-for-page-report.png)

## Setting Role Permissions from the Page/Report as a Developer

### Role Permissions For Page

1. Go to: Home > Developer > Page.
2. Add a row and select which other roles can access the Page.
  [Assign roles to the page](/files/roles-for-page.png)

### Role Permissions For Report

1. Go to: Home > Developer > Report.
2. Add rows with roles who can access the Report.
  [Assign roles to the report](/files/roles-for-report.png)

<!-- page: erpnext/erpnext__round-off-account-validation.md -->
---
title: "Round off Account Validation Message"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/round-off-account-validation"
updated: "2026-08-14"
---

A Purchase Invoice for Nova Industries contains item calculations, tax, discount, and currency precision. The exact total differs from the payable amount by a few cents, but no account is configured to hold that difference. ERPNext asks for a Round Off Account so the debit and credit totals remain balanced.

## Configure the default

1. Open the Chart of Accounts and create or identify a small rounding expense or income account.
2. Open the Company record for Nova Industries.
3. In the accounting defaults, set the Round Off Account and Round Off Cost Center.
4. Save the Company, reload the invoice, and submit again.

![Company defaults for Round Off Account and Round Off Cost Center](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-company-round-off-defaults.png)



## Why rounding appears

Quantity multiplied by rate, taxes, discounts, exchange rates, and currency precision can produce fractions smaller than the currency accepts. ERPNext posts the small difference instead of leaving an unbalanced ledger.

## Troubleshooting

### The error remains after setting the account

Confirm the account and cost center belong to the same company, the account is a ledger account rather than a group, and the transaction was reloaded after the Company was saved.

## Frequently asked questions

### Should I use a large adjustment account?

Round Off is for small precision differences. A material difference usually indicates an incorrect rate, tax, exchange rate, or precision setting and should be investigated.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__routing.md -->
---
title: "Routing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/routing"
updated: "2026-02-27"
---

**Routing is a template of BOM Operations.**

A Routing stores all Operations along with the description, hourly rate, operation time, batch size, etc. Creating a Routing for your BOM Operations is useful when similar Operations are used for manufacturing different items.

---

### Prerequisites

- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)

---

## How to Create a Routing

1. Go to the Routing list, click on New.
2. Enter a name for the Routing.
3. Enter the Operations in the BOM Operation table:
  1. Select the Operation.
  2. The default Workstation will be fetched.
  3. Enter the Hourly Rate for running this Operation.
  4. Enter the Operation Time in minutes.
  5. Enter the Batch Size, i.e. the number of units processed in this Operation.
  6. The Operating Cost will be calculated based on the Hourly Rate and the Operation Time.
  7. Save.

Once created, a Routing can be selected in a BOM to fetch the Operations stored in the Routing.

![](/files/CleanShot 2026-02-19 at 12.31.10@2x.png)

---

## Sequence ID in Routing

![](/files/image2679eb.png)

Sequence ID enforces the users to complete the operations sequentially via Job Card. In case a user tries to complete an operation before completing any of its precedent operations as per the Sequence ID, the system throws a validation error.

---

### Related Topics

1. [Work Order](/erpnext/work-order)
2. [Bill Of Materials](/erpnext/bill-of-materials)

<!-- page: erpnext/erpnext__rules.md -->
---
title: "Rules"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/rules"
updated: "2026-02-26"
---

Shipping and pricing rules are essential features in ERPNext's stock module that streamline the management of shipping costs and pricing strategies. 

Shipping rules allow businesses to define various parameters for calculating shipping charges, such as weight, volume, destination, or shipping method. These rules automate the calculation of shipping costs during sales transactions, ensuring accurate and consistent shipping charges based on predefined criteria.

On the other hand, pricing rules in ERPNext empower businesses to create dynamic pricing strategies based on specific conditions or criteria. This includes setting discounts, promotions, bulk pricing, or special pricing for different customer segments, items, or sales channels.

* [Shipping Rule](/erpnext/user/manual/en/setup-shipping-rule)
* [Pricing Rule](/erpnext/user/manual/en/pricing-rule)

<!-- page: erpnext/erpnext__salary-slip-from-timesheet.md -->
---
title: "Salary Slip from Timesheet\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/salary-slip-from-timesheet"
updated: "2026-02-26"
---

**The salary of an employee can be calculated based on the number of hours that he has worked for on a particular project.**

To enable the same, you may choose to create the Employee's Salary Slip directly from a Timesheet.

![Salary Slip](/files/projects-salary-slip-from-timesheet.png)

## 1. How to Create A Salary Slip from A Timesheet

1. Once the Timesheet is submitted, and an invoice has been generated, go to the Timesheet and click on 'Create Salary Slip'.
2. All the details, like the Employee, Employee Name, Posting Date, Company Name, Letter Head, etc. will get captured from the Timesheet.
3. **Dates**: Since this Salary Slip is getting generated out of a Timesheet, it will auto-fetch the Start Date and End Date from the Timesheet. However, the same can be changed.
4. **Salary Slip Timesheet**: The details of the Timesheet from which the Salary Slip was created will be captured. You can also more Timesheets here to create a single Salary Slip against multiple Timesheets.
5. Save and Submit.

 

![Salary Slip](/files/timesheet-salary-slip-4.gif)

### 1.1. Additional Details while Creating a Salary Slip form a Time Sheet:

1. **Earnings and Deduction**: Any Earnings like HRA, Incentives etc. or Deductions like Income Tax, Provident Fund etc. in the Salary generated from the Timesheet can be mentioned here.
2. **Other Information**: According to the Salary Structure of the Employee, the Gross payment information, the Loan Repayment Information, and the Net Pay information will get auto-captured.
3. For a detailed guide on setting up overtime via timesheets, [click here](https://docs.erpnext.com/docs/v13/user/manual/en/human-resources/articles/create-payroll-entry-with-timesheets).
