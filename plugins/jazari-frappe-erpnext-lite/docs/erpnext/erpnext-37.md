<!-- Frappe documentation: erpnext, part 37 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__material-request.md -->
---
title: "Material Request"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/material-request"
updated: "2026-02-27"
---

**A Material Request is a simple document identifying a requirement of a set of Items (products or services) for a particular reason.**

A Material Request can have the following purposes:

* **Purchase**: If the material being requested is to be purchased.
* **Material Transfer**: If the material being requested is to be shifted from one Warehouse to another.
* **Material Issue**: If the material being requested is to be Issued for some purpose like manufacturing.
* **Manufacture:** If the material being requested is to be produced.
* **Subcontracting:** If the material being requested is to be subcontracted to a vendor.
* **Customer Provided**: If the material being requested is to be provided by Customer. To know more about this, visit the [Customer Provided Item](/erpnext/customer-provided-items) page.

![Material Request](/files/material-request-flowchart.png)  


To access the Material Request list, go to:


> Home > Stock > Stock Transactions > Material Request
> 
> 

1. How to create a Material Request
-----------------------------------

1. Go to the Material Request list, click on Add Material Request.
2. Enter the Required By date.
3. Select the appropriate purpose from the list.
4. You can fetch Items from a BOM, Sales Order, or Product Bundle.

![Screenshot 2024-07-09 at 2.36.44 PM](/files/Screenshot 2024-07-09 at 2.36.44 PM.png)
5. Select the Item and set the quantity.
6. Select the Warehouse for which Items are required.
7. You can change the Required By date for individual Items in this table.
8. Save and Submit.

![Screenshot 2024-07-09 at 2.40.52 PM](/files/Screenshot 2024-07-09 at 2.40.52 PM.png)  


### 1.1 Alternate ways of creating a Material Request

A Material Request can be generated automatically:

* From a [Sales Order](/erpnext/sales-order). While creating MR, user can choose to ignore or include Projected Quantity. Accordingly, Sales Order Items are fetched to MR.
* When the Projected Quantity of an Item in Stores (Warehouses) reaches a particular level.
* From your a [Production Plan](/erpnext/production-plan) to plan your manufacturing activities.

If your Items are inventory items, you must also mention the Warehouse where you expect these Items to be delivered. This helps to keep track of the [Projected Quantity](/erpnext/projected-quantity) for this Item.

> Info: Material Request is not mandatory. It is ideal if you have centralized buying so that you can collect this information from various departments.

### 1.2 Statuses

These are the statuses a Material Request can be in:

* **Draft**: A draft is saved but yet to be submitted to the system.
* **Submitted**: Document is submitted to the system.
* **Stopped**: If no more materials are needed the Material Request can be stopped.
* **Canceled**: The materials are not needed at all and the request is canceled.
* **Pending**: The Purchase/Manufacture is pending to complete the Material Request.
* **Partially Ordered**: Purchase Orders for some Items from the Material Request are made and some are pending.
* **Ordered**: All Items in the Material Request are ordered via Purchase Orders.
* **Issued**: The materials are issued using a Material Issue Stock Entry.
* **Transferred**: The required materials are transferred from one Warehouse to another using a Stock Entry.
* **Received**: The materials were ordered and have been received at your Warehouse using a Purchase Receipt.

2. Features
-----------

### 2.1 Items table

* **Barcode**: You can track Items using [barcodes](/erpnext/track-items-using-barcode).
* The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.
* **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for [tracking items using barcode](/erpnext/track-items-using-barcode) to know more.
* The UoM, Conversion Factor, and Amount will be fetched. You change the Warehouse for which the material is being requested.
* Accounting details like Expense Account and Accounting Dimensions can be set for the Items.
* Page Break will create a page break just before this item when printing.

### 2.2 Setting Warehouses

* **Set Warehouse**: Optionally, you can set the Warehouse where the requested Items will arrive. This will be fetched into the 'For Warehouse' fields in the Item table rows.

### 2.3 More Information

In the 'Job Card' and 'Work Order' fields, it sets a reference from where the Material Request was generated.

### 2.4 Printing Details

#### Letterhead

You can print your Material Request on your company's letterhead. Read [Letter head documentation](/erpnext/letter-head) to learn more.

#### Print Headings

Material Request headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/erpnext/print-headings).

### 2.5 Terms and Conditions

In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/erpnext/terms-and-conditions)

### 2.6 After Submitting

You can create the following documents:

* [Request For Quotation](/erpnext/request-for-quotation)
* [Purchase Order](/erpnext/purchase-order)
* [Supplier Quotation](/erpnext/supplier-quotation)

![Screenshot 2024-07-09 at 2.38.58 PM](/files/Screenshot 2024-07-09 at 2.38.58 PM.png)  


### 2.7 Automatically generate Material Requests

Material Requests can be generated automatically by enabling the setting in [Stock Settings](/erpnext/stock-settings#9-automatic-material-request) and setting the level in the [Item form](/erpnext/item#34-automatic-reordering). When the stock level dips below a certain quantity, setting a reorder will automatically create material requests for the Item.

### Note:
Material Request Purpose "Subcontracting" is newly added and only present in the develop branch of ERPNext. It will be there by default in the next major release i.e v16

A subcontracted Material Request enables the user to create a Subcontracted Purchase Order directly from the Material Request itself after submission.

<!-- page: erpnext/erpnext__material-requirements-planning-mrp.md -->
---
title: "Material Requirements Planning (MRP)"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/material-requirements-planning-mrp"
updated: "2026-04-29"
---

The ERPNext currently have the MRP inside the production plan which is difficult for new users to understand and also it only uses sales order or material request data to generate the MRP.

## Purpose

The main purpose of MRP is to ensure that the right materials are available at the right time, helping the company to avoid the overproduction and delays in delivery. To know how MRP works first needs to understand how demand planning works.

## Demand Planning

We already had sales orders and material requests to generate demand planning. However, this only works for short-term MRP requirements and does not cover longer periods of time. To address this, we have added sales forecasting and delivery schedules to generate demand.

## Sales Forecast

The users has to manually enter the forecasting data by calculating it outside the system.

![](/files/sales%20forcast%20(1)

## Delivery Schedules

Some customers do not prefer a one time delivery against a sales order and they require multiple deliveries. The delivery schedules are very helpful for MRP because they provide visibility of when materials are actually needed, instead of assuming everything must be delivered at once.  
To make Delivery Schedules, users has to click on Add Schedule button in the sales order item table

![](/files/delivery_schedules.png)



## Master Production Schedule

To capture the demand for finished items, the Master Production Schedule (MPS) document was introduced. The system collects data from various sources such as sales orders, material requests, sales forecasts, and delivery schedules to generate the demand in the MPS.

![](/files/mps.png)

## Material Requirements Planning Report

The Material Requirements Planning (MRP) report calculates the required quantities of raw materials and components, along with the dates when they are needed, based on the demand for finished items.



![](/files/mrp_report.png)

Users can see the MRP report in the bucket view

![](/files/mrp-bucket.png)

## Item Lead Time

To calculate the dates of when to release the purchase order for raw materials and work order for components, the system needs to be aware of the lead time for manufacturing and the lead time for material procurement. For this purpose, a new document Item Lead Time was added.



![](/files/item-lead-time.png)

<!-- page: erpnext/erpnext__material-transfer-from-delivery-note.md -->
---
title: "Material Transfer from Delivery Note and Purchase Receipt\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/material-transfer-from-delivery-note"
updated: "2026-03-02"
---



In ERPNext, you can create Material Transfer entry from [Stock Entry](/erpnext/stock-entry.html) document. However, there are some scenarios in the Material Transfer where it needs to be presented as a Delivery Note and Purchase Receipt.

## Material Transfer from Delivery Note

### Scenarios

1. One of the examples is when you transfer a Material from your stores to project site, however, you need to present it as a Delivery Note to the client.

2. Also, there are statutory requirements where taxes are to be applied on each transfer of Material. It is easier to manage in a transaction like Delivery Note, than in the Stock Entry.

Considering these scenarios, the provision of Material Transfer has been added in the Delivery Note as well. Following are the steps to use Delivery Note for creating Material Transfer entry.

### Steps

#### Enable Target Warehouse

Delivery Note Item doctype has a hidden field of Target Warehouse (previously Customer Warehouse). You can enable it from [Stock Settings](/erpnext/stock-settings) by enabling "Allow Material Transfer From Delivery Note and Sales Invoice".

Also note that the selected customer should represent the same company. For this, enable the 'Is Internal Customer' option in the customer form and select your company in the 'Represents Company' field.



### Select Warehouses

When creating a Delivery Note for Material Transfer, for an item select source Warehouse as From Warehouse.

In the Customer Warehouse, select a Warehouse where Material is to be transferred or select a target warehouse.

![Delivery Note Material Transfer](/files/customer-warehouse-2.png)

On the submission of a Delivery Note, item's stock will be deducted from "From Warehouse" and added to the "Customer Warehouse".

## Material Transfer from Purchase Receipt

### Scenarios

There are statutory requirements where taxes are to be applied on each transfer of Material. It is easier to manage a situation like this in a transaction like Purchase Receipt, than in the Stock Entry as taxes cannot be applied on transfers of items via Stock Entry

Following are the steps to use Purchase Receipt for creating Material Transfer Entry.

### Steps

#### Enable Supplier Warehouse

Similar to the Customer Warehouse shown above, the first step is to enable the Supplier Warehouse from [Stock Settings](/erpnext/stock-settings) as shown above.

Also note that the selected supplier should represent the same company. For this, enable the 'Is Internal Supplier' option in the Supplier form and select your company in the 'Represents Company' field.



### Select Warehouses

When creating a Purchase Receipt for Material Transfer, for an Item, select the target Warehouse as Accepted Warehouse.

This is how you create an internal Purchase Receipt from an internal Delivery Note:

![Purchase Receipt Material Transfer](/files/supplier-warehouse-1.png)

In the Supplier Warehouse, select a Warehouse from where Material is to be transferred.

![Purchase Receipt Material Transfer](/files/supplier-warehouse.png)

On submission of the Purchase Receipt, item's stock will be deducted from "Supplier Warehouse" and added to the "Accepted Warehouse".

<!-- page: erpnext/erpnext__material_consumption.md -->
---
title: "Material consumption\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/material_consumption"
updated: "2026-03-02"
---


Material Consumption functionality allows you to have multiple consumption `Stock Entry` against a Work Order. To enable this, go to Manufacturing > Manufacturing Settings.

![Item Alternative](/files/allow-material-consumption.png)

Once enabled, a `Material Consumption` button will be available in Work Order once started.

![Item Alternative](/files/material-consumption-button.png)

When button is clicked, it will do the following:

1. It will create Stock Entry with purpose `Material Consumption for Manufacture`.

![Item Alternative](/files/material-consumption-for-manufacture.png)

2. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `BOM`, if will propose to consume all required qty for manufacture.
3. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `Material Transferred for Manufacture`, if will propose to consume all transferred qty for manufacture.
4. Once submitted, it will update `Consumed Qty` column in the Work Order.

![Item Alternative](/files/consumed-qty.png)

5. In succeeding Material Consumption, it will suggest unconsumed qty.
6. Once "Finish" button is clicked in Work Order, it will take into account consumed qty.

### Validations

* If "Allow Multiple Material Consumption" is not set in Manufacturing Settings but "Material Consumption for Manufacture" is use in Stock Entry.

![Item Alternative](/files/material-consumption-stock-entry.gif)

* Cannot cancel "Material Consumption for Manufacture" for completed Work Order.

![Item Alternative](/files/cancel-material-consumption-stock-entry.gif)

<!-- page: erpnext/erpnext__maximum-number-of-fields-in-a-form.md -->
---
title: "Maximum Number of Fields in a Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maximum-number-of-fields-in-a-form"
updated: "2026-06-10"
---

If you have been customizing ERPNext by adding Custom Fields to forms, you may reach a point where:

- A newly added Custom Field causes a **Server Error** when you try to submit a document, or
- ERPNext refuses to save after the field is added.

 This article explains why this happens and walks you through practical ways to fix it — no database knowledge required. 

## What the Errors Mean

When you hit the limit, ERPNext may show one of these two errors on screen:

### Error 1:  "Unknown column in INSERT INTO"

![](/files/custom field-server error.png)

 This error appears when you submit a form after adding a new Custom Field. ERPNext is trying to save data for a column it cannot find in the database yet,  a sign that the underlying table has hit its structural limit and the new field could not be properly registered.

### Error 2: "Row size too large"

![](/files/row-size-error.png)

 This error is more direct. The database table's row has exceeded its maximum allowed size of **65,535 bytes**. 

## Why Does This Happen?

In ERPNext (and Frappe), every form, called a **DocType**, corresponds to a table in the database. Each field on that form is a column in that table.



Think of it like a spreadsheet: every row can only hold so many columns before it runs out of space. MySQL (the database ERPNext uses) enforces a hard row size limit of **65,535 bytes** per table row. MySQL also technically supports up to 4,096 columns per table, but in practice the row size limit is hit first.



Here is a concrete example of how quickly that limit is reached:



- Fields of type **Data, Link, Select, Dynamic Link, Password,** and **Read Only** are stored as `VARCHAR(140)` columns in the database.
- A `VARCHAR(140)` column using the `utf8mb3` character set allocates up to **420 bytes** per value (140 characters × 3 bytes each).
- That means a table can hold at most roughly **65,535 ÷ 420 = ~156** such columns before hitting the limit.

The form / doctype in question already has many built-in fields. Installing custom apps adds even more. Once you approach this ceiling, adding even one more Custom Field can push it over the edge, causing the submission errors shown above.

---

## Functional Solutions

There are several ways to address this, ranging from quick fixes to structural changes. Start with the quick fixes if you only need a little more room, or go with the structural options if you need to add many more fields.

### Fix 1: Create a Separate DocType and Link It to Primary DocType

This is the best long-term approach when you need to add a **distinct group of related fields** (e.g., fields for a specific department, process, or compliance requirement).



**Steps:**

1. Go to **Customize > DocType** (or search "New DocType" in the search bar).
2. Create a new DocType with all the fields you need.
3. In the new DocType, add a **Link** field pointing to Primary DocType (in which you wanted to add all the fields), this connects each record back to its parent Stock Entry.
4. Optionally, add a Link field on Stock Entry's Customize Form pointing back to your new DocType for easy navigation.

**Why this works:** Your new DocType gets its own separate database table with its own row size budget, completely independent of Stock Entry's table.



---

### Fix 2: Create a Child Table and Add It to Stock Entry

This approach works best when your extra fields represent **repeating rows of data**. For example, a quality checklist or a list of items, similar to how the Items table works inside Stock Entry.



**Steps:**

1. Go to **Customize > DocType** and create a new DocType. Enable the **"Is Child Table"** checkbox.
2. Add all your fields as columns inside this child table.
3. Go to **Customize Form > Stock Entry**.
4. Add a new field of type **Table** and set its **Options** to point to your newly created child DocType.

**Why this works:** A Child Table is stored in its own separate database table, entirely sidestepping the row size limit of the parent form.

---

## Techical Fixes

### Fix 1: Convert Some Fields to Text-Based Types

Fields of type **Text, Small Text, Text Editor,** or **Code** are stored differently in MySQL (as `TEXT` or `BLOB` columns). Unlike `VARCHAR` columns, their content is stored outside the main row — they only occupy **9–12 bytes** in the row itself instead of up to 420 bytes.



**What to do:** In **Customize Form**, find any Custom Fields that currently use types like Data, Link, or Select, where the value is long or does not need to be filtered/sorted, and replace them with field type to **Small Text** or **Text**. Each conversion frees up significant row space and allows more fields to be added.



---

### Fix 2: Reduce the "Length" Property of Existing Fields

When creating a Data-type Custom Field, ERPNext sets a default **Length** of 140. This directly controls how many bytes MySQL allocates for that column. Reducing it on fields where a shorter input is sufficient (e.g., a code field that will never exceed 20 characters) frees up space proportionally.



**What to do:** In **Customize Form**, open each Custom Field's settings and lower the **Length** value to what is actually needed. For example, changing Length from 140 to 20 reduces that column's allocation from 420 bytes to just 60 bytes.



---

### Fix 3: Remove Unused Custom Fields Using Trim Tables

Custom Fields that are deleted from Customize Form are **not automatically removed from the database table** — their columns remain, still consuming row space.



If you are certain you no longer need the data from some old Custom Fields, you can permanently remove those columns from the database by running the `trim-tables` bench command:



[https://frappeframework.com/docs/user/en/bench/reference/trim-tables](https://frappeframework.com/docs/user/en/bench/reference/trim-tables)



> **Note:** This operation is irreversible. Any data stored in those columns will be permanently deleted. Always take a database backup before running this command.

## Choosing the Right Solution


| Your situation                                              | Recommended approach                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------------- |
| You need many new single-value fields (one value in a form) | Create a Separate Linked DocType                                 |
| You need repeating rows of data per Stock Entry             | Create a Child Table                                             |
| A few fields are pushing you over the limit                 | Convert some fields to Small Text / Text, or reduce field Length |
| You have deleted Custom Fields but their columns remain     | Run `trim-tables` to reclaim space                               |

<!-- page: erpnext/erpnext__merging-accounts.md -->
---
title: "Merge Accounts | ERPNext Documentation"
description: "Learn how to safely merge duplicate Accounts in ERPNext, verify matching properties, choose the correct target, and confirm historical ledger results."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/merging-accounts"
updated: "2026-08-14"
---

Merge Accounts when two Account records in the same [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) represent the same ledger or the same group and you want to keep only one. ERPNext replaces references to the source Account with the target Account, then removes the duplicate source record.



For example, Nova Industries has both **SaaS Subscription Expenses** and **Software Subscription Expenses** for the same recurring software costs. The accounting team decides to retain **Software Subscription Expenses** and merge the duplicate into it.



Merging changes historical links. Treat it as a controlled data-cleanup operation, not a convenient way to rename an Account.

## Before you begin

Confirm the source Account is truly a duplicate. Compare its purpose, parent, currency, account type, tax use, default-account use, and historical transactions with the intended target.

ERPNext allows the merge only when both Accounts have the same:


| Property         | Why it must match                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------- |
| Is Group         | A group cannot be merged into a ledger, and a ledger cannot be merged into a group.          |
| Root Type        | Asset, Liability, Equity, Income, and Expense Accounts cannot be combined across root types. |
| Company          | Each [Company](https://docs.frappe.io/erpnext/company) has a separate Chart of Accounts.     |
| Account Currency | Existing ledger values must retain a consistent currency.                                    |


Run the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) for both Accounts and compare balances in the [Trial Balance](https://docs.frappe.io/erpnext/trial-balance). If either Account has a special purpose or should remain separately reportable, do not merge it.

Take a current [data backup](https://docs.frappe.io/erpnext/setting-up-data-backups) before merging important production Accounts. There is no normal user-interface action that separates the records again.

## Select the source Account

Open **Chart of Accounts**, select the company, and find the Account that should disappear after the merge. You can also open the Account list and filter by name.



![Filtered Account list showing the duplicate source Account](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-merging-accounts-account-list-source-account.png)

Open the source Account and verify its Company, Root Type, Report Type, Currency, Account Type, and whether it is a group. In this example, **SaaS Subscription Expenses - NET** is the duplicate source.

## Open Merge Account

On the source Account, select **Actions &gt; Merge Account**.



![Merge Account action on an Account record](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-merging-accounts-account-actions-merge-account.png)

Do not use **Update Account Name / Number** for this task. That action renames one Account; it does not combine two existing Account records.

## Choose the target Account

In **Merge with Existing Account**, enter the full name of the Account that must remain. For the example, the target is **Software Subscription Expenses - NET**.



![Target Account and Merge button in the Merge with Existing Account dialog](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-merging-accounts-merge-account-target-dialog.png)

Review the direction before selecting **Merge**:


| Role           | Example                              | Result                                      |
| -------------- | ------------------------------------ | ------------------------------------------- |
| Source Account | SaaS Subscription Expenses - NET     | Removed after references are moved.         |
| Target Account | Software Subscription Expenses - NET | Remains and receives the source references. |


Select **Merge** only after another reviewer confirms the direction and target.

## What changes after the merge

ERPNext updates links that previously pointed to the source Account so they point to the target Account. Existing transactions therefore show the target Account name when opened after the merge.

The [accounting entries](https://docs.frappe.io/erpnext/accounting-entries), debit and credit amounts, voucher dates, and parties do not change merely because the Account master was merged. What changes is the Account under which those entries are grouped and reported.

After the merge:

1. Search for the source Account and confirm it no longer exists as a separate master.
2. Open the target Account and use **View &gt; General Ledger**.
3. Confirm historical entries from both Accounts appear under the target.
4. Re-run the Trial Balance, [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet), or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement), as applicable.
5. Compare totals with the pre-merge reports. Consolidation should change the presentation, not the company's total debit, credit, profit, or net assets.

The [immutable ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext) still preserves submitted accounting effects. Merging the Account master reassigns links; it does not cancel and repost every voucher.

## Important fields and controls


| Field or control | Meaning                                      | Check before merging                         |
| ---------------- | -------------------------------------------- | -------------------------------------------- |
| Source Account   | Account opened when you start the action     | This record will no longer remain separate.  |
| Name             | Full target Account ID entered in the dialog | Confirm the company suffix and exact target. |
| Is Group         | Whether the Account contains child Accounts  | Must match between source and target.        |
| Root Type        | Asset, Liability, Equity, Income, or Expense | Must match between source and target.        |
| Company          | Legal entity that owns the Account           | Must match between source and target.        |
| Currency         | Currency of the Account ledger               | Must match between source and target.        |
| Merge            | Runs the consolidation                       | Select only after review and backup.         |


## Troubleshooting

### ERPNext says the Accounts have different properties

Compare **Is Group**, **Root Type**, **Company**, and **Currency** on both records. Current ERPNext requires all four to match. Do not change a property merely to bypass the validation unless the underlying accounting setup is genuinely wrong.

### ERPNext says the system is in use

Account merging locks and updates many linked records. Current ERPNext blocks the operation when General Ledger entries were updated recently. Stop accounting activity, wait at least five minutes after the last GL update, then retry during a quiet period.

### The target Account is not found

Enter the full Account ID, including its company suffix. Confirm that the target exists in the same company and that your role has write permission for both Accounts.

### Financial totals changed unexpectedly

Stop further cleanup. Compare pre-merge reports, the target General Ledger, and the affected [Journal Entries](https://docs.frappe.io/erpnext/journal-entry). Account merging should consolidate classification without changing the total double-entry amounts. Restore the backup or escalate to an administrator if the result is not understood.

### The Chart of Accounts tree looks incorrect

Reload the tree first. If a structural problem remains, investigate it before using any repair tool. Account merging is not a substitute for correcting parent relationships or rebuilding a damaged tree.

## FAQs

### Can I merge a group Account into a ledger Account?

No, Both Accounts must either be groups or both be ledgers.

### Can I merge Accounts from different companies?

No, The source and target must belong to the same company.

### Does merging delete historical transactions?

No, ERPNext updates their Account references to the target. Verify the target ledger after the merge.

### Can I undo an Account merge?

There is no standard split or unmerge action. A tested backup is the reliable recovery path for an incorrect merge.

### Should I merge an Account when I only want a better name or number?

No, Use **Actions &gt; Update Account Name / Number** when only one Account exists and its identity needs correction.

## Related topics

- [Changing Parent Account](https://docs.frappe.io/erpnext/changing-parent-account)
- [Freeze an Account](https://docs.frappe.io/erpnext/freeze-an-account)
- [Rebuild Tree](https://docs.frappe.io/erpnext/rebuild-tree)
- [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer)
- [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings)

<!-- page: erpnext/erpnext__migrate-to-perpetual-inventory.md -->
---
title: "Migrate To Perpetual Inventory\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/migrate-to-perpetual-inventory"
updated: "2026-03-02"
---


Perpetual Inventory Valuation is activated by default in the system.

For the users who are currently following periodic inventory valuation system, and wish to migrate to perpetual inventory valuation system, please follow the steps explained below.

### 1. How to Migrate to Perpetual Inventory

1. To enable perpetual Inventory, ensure that the Stock in Hand Account is synced with the value of actual stock value in your Warehouse(s). To sync it, you will have to create a Journal Entry for the difference amount against expense account (generally used in Purchase Invoice).

 For example, when perpetual inventory was disabled, you must be having Expense (Cost of Goods Sold) booked via Purchase Invoices. Now, you will have to create a Journal Entry to move the value of existing stock from expense account to stock in hand account.

 Cr. Expense account ......... XXX

 Dr. Stock in Hand account ... XXX

 It can also work other-way round if you were selecting a stock in hand account in the Purchase Invoice.

1. Before enabling Perpetual Inventory, ensure that Stock Accounts (ledger) is linked for the existing Warehouse. The stock account for a Warehouse can be set at three levels.

 * In the Warehouse master itself
 * In the Parent Warehouse master
 * Default Stock in Hand Account in the Company master, if you maintain only one Stock-in-hand account for all the Warehouses.

1. Journal Entry to Update Stock Received but not Billed account

 An account "Stock Received but not Billed" is an adjustment account which reflects the value of the stock for which Purchase Receipt has been submitted, but Purchase Invoice is yet to created. A Journal Entry should be created to update the value open Purchase Receipt pending for billing into "Stock Received but not Billed" account.

 To know the value of the stock received but not billed, you can refer the report "Received Items Pending for Billing" in the Accounts module.

 Create a Journal Entry as follows to update the value in Stock Received but not Billed account.

 Cr. Stock Received but not Billed ........... XXX

 Dr. Expense Account (COGS) .................. XXX

1. Setup the following default accounts for each Company

 * Stock Received But Not Billed
 * Stock Adjustment Account
 * Expenses Included In Valuation
 * Cost Center
 * Activate Perpetual Inventory

1. Go to: **Home > Accounting > Company**

 ![Perpetual Inventory](/files/perpetual-1.png)

#### 2. Related Topics
1. [Accounting Of Inventory Stock](/erpnext/accounting-of-inventory-stock)
1. [Perpetual Inventory](/erpnext/perpetual-inventory)

<!-- page: erpnext/erpnext__milestone-tracker.md -->
---
title: "Milestone Tracking\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/milestone-tracker"
updated: "2026-03-02"
---

> Introduced in Version 12

**You can automatically track milestones based on the lifecycle of a document if it undergoes multiple stages.**

The configuration for Milestone setting can be set in **Milestone Tracking** and each milestone is updated in **Milestone**

To access Milestone Tracker, go to:

> Home > Settings > Milestone Tracker

## 1. Creating a Milestone Tracker

1. Click on New.
2. Set the Document Type to track (example: "Issue").
3. Set the field that represents stages (example: "Status").

> Note: A milestone stage can be defined by Link or Select properties.

Once this is set, a new **Milestone** record is created every time the status of any issue is changed.

The Milestone can be viewed in the timeline of the view:

![Assign](/files/milestone-in-timeline.png)

Note: Milestones work independently of Versions.

## 2. Features

Milestones can be a great source for reporting and notifying. For example, if Lead Qualification is a milestone on "Lead", milestones can help generate reports on the number of leads being qualified in a period.

### 2.1 Using Milestones with Dashboards

Used along with Dashboards, Milestones can help track the trends in milestones. For example, if "Qualification" is tracked as a "Lead Stage", a Dashboard on Milestone filtered by Qualification will show the trends of leads qualified.

### 2.2 Using Milestones with Energy Points

Energy Point Rules can be defined to automatically give Energy Points to users who achieve a milestone. This can be used to incentivize action on transactions at various levels.

<!-- page: erpnext/erpnext__mode-of-payment.md -->
---
title: "Mode of Payment | ERPNext Documentation"
description: "Set up cash, bank, card, and other payment methods in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/mode-of-payment"
updated: "2026-07-31"
---

A Mode of Payment identifies how money is received or paid, such as cash, bank transfer, card, or check. It also helps ERPNext choose the correct default ledger for each Company when users create a [Payment Entry](/erpnext/payment-entry) or a Point of Sale transaction.

## Before you begin

Create the required cash and bank ledgers in the [Chart of Accounts](/erpnext/chart-of-accounts). Confirm each account's type and currency, and decide which account each [Company](/erpnext/company) should use for the payment method.

## Create a Mode of Payment

1. Open **Mode of Payment** and select **Add Mode of Payment**.
2. Enter a clear name, such as Cash, Bank Transfer, or Corporate Card.
3. Choose the payment **Type**.
4. In **Accounts**, add each Company and its default cash or bank ledger.
5. Save the record, then test it in a Payment Entry or [POS Profile](/erpnext/pos-profile).

![Mode of Payment list in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-01-mode-of-payment-list.png)

## Important fields and what they mean


| Field           | What it controls                                                                |
| --------------- | ------------------------------------------------------------------------------- |
| Mode of Payment | Name users select in transactions.                                              |
| Type            | Classifies the method as Cash, Bank, General, Phone, or another available type. |
| Enabled         | Controls whether users can select it.                                           |
| Company         | Company for which the default account applies.                                  |
| Default Account | Ledger ERPNext proposes when this mode is selected.                             |


The Type describes the method. The Default Account determines which ledger is used. Selecting a Mode of Payment does not by itself create a General Ledger entry. The accounting effect comes from submitting the transaction that uses it.

## Troubleshooting

### ERPNext asks me to set a default Cash or Bank account

Open the selected Mode of Payment and add an **Accounts** row for the transaction's Company. Choose a ledger whose account type and currency match the payment. If the transaction comes from POS, also check the Mode of Payment rows in the POS Profile.

### The wrong account appears in Payment Entry

Check whether the Mode of Payment has a default account for the current Company. A Company-specific row takes effect only for that Company. Also review whether the Payment Entry was created from another document that supplied its own account.

### A cash payment appears in Bank Reconciliation

The label Cash does not make the linked ledger a cash account. Review the Default Account in the Chart of Accounts. If it is configured as a Bank account, transactions can appear in [Bank Reconciliation](/erpnext/bank-reconciliation). Link the mode to the actual cash ledger instead.

### Users cannot select the mode

Confirm that **Enabled** is selected and that the mode is included in the relevant POS Profile or transaction setup. Also check user access to the Company and account.

## Frequently asked questions

### Can one Mode of Payment use different accounts for different companies?

Y

es. Add one Accounts row per Company. ERPNext prevents duplicate rows for the same Company because each mode has one default account per Company.

### Can I assign a different default account for each branch?

The standard Mode of Payment mapping is Company-based, not branch-based. For branch-specific retail payments, use separate POS Profiles with the appropriate payment accounts. More complex branch logic requires a controlled customization.

### Does the Type field decide which ledger is posted?

Type classifies the payment method. The Default Account and the submitted transaction determine the ledger posting. Always verify the proposed Paid From and Paid To accounts before submitting.

### Should I create a Mode of Payment for every bank account?

Usually not. Create names that are meaningful to users, then map each mode to the appropriate Company account. Separate modes are useful when users must deliberately distinguish methods or when different operational flows need different defaults.

### Is a Mode of Payment the same as an online payment gateway?

A Mode of Payment labels and maps the accounting method. An online [Payment Gateway](/erpnext/payment-gateway) also requires integration credentials and gateway configuration. The gateway's completed transaction can then be represented by a suitable Mode of Payment.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [POS Profile](/erpnext/pos-profile)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Payment Gateway](/erpnext/payment-gateway)

<!-- page: erpnext/erpnext__module-settings.md -->
---
title: "Module Settings | ERPNext Documentation"
description: "Learn how ERPNext module settings organise configuration for each business process and how to choose the correct settings page."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/module-settings"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor used throughout this guide. Its sales team prepares quotations, the warehouse dispatches devices, the factory assembles selected products, and the finance team records every result. When the company introduces a repair service, its administrator must decide where to configure the new process. A site-wide security setting, a Selling setting, and a Stock setting can all look like "system settings", but they solve different problems.



Module Settings is the map that takes the administrator to the settings owned by each business process. It helps Nova change how Sales Orders behave without accidentally changing login security, accounting rules, or another module. Use it to find the correct settings page, then test the change in the transaction that consumes it.

![ERPNext Desk showing the business modules available to Nova Industries](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-module-settings-overview411fd1.png)

## How module settings are organised


| Settings page          | What it controls                                                                         | Nova Industries example                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Accounts Settings      | Accounting validations, invoices, deferred accounting, dimensions, and closing behaviour | Finance requires a credit limit check before a Sales Order is submitted.                |
| Selling Settings       | Customer and selling-document defaults                                                   | Sales wants the same territory and price-list behaviour on every quotation.             |
| Buying Settings        | Supplier and purchasing-document behaviour                                               | Purchasing decides whether a Purchase Order is required before invoicing.               |
| Stock Settings         | Warehouses, valuation, reservations, and stock transaction behaviour                     | Warehouse users need serial-number and negative-stock rules to match company policy.    |
| Manufacturing Settings | Production defaults and manufacturing controls                                           | The assembly team wants Work Orders and Job Cards to follow a defined capacity process. |
| Projects Settings      | Project, task, and time-tracking defaults                                                | The repair service bills work from Timesheets linked to Projects.                       |
| Support Settings       | Issue and service-level behaviour                                                        | Support assigns incoming customer issues to a default service team.                     |
| CRM Settings           | Lead, opportunity, and communication behaviour                                           | Sales wants website enquiries to become Leads with consistent ownership.                |


## Choose the correct settings page

Start with the transaction or process that should change. If the change should affect only Sales Orders, open Selling Settings. If it affects every user, such as password policy or date format, use [System Settings](/erpnext/system-settings). If it merely supplies a common Company or Currency on new records, use [Global Defaults](/erpnext/global-defaults). If it should last only for one user session, use [Session Defaults](/erpnext/session-defaults).



After saving a module setting, create a fresh draft transaction and confirm the intended result. Existing submitted transactions normally preserve their earlier state and should not be treated as proof that the new configuration failed.

## Troubleshooting

### A module setting does not affect an existing document

Reload the form and test with a new draft. A setting may apply only when a document is created or when a particular transaction condition is met.

### A settings page is missing

Confirm that the app and module are installed, the relevant domain is active, and the user has the System Manager or other required role.

### A user can still open a module

Module Settings controls behaviour, not access. Configure roles, Role Permissions, User Permissions, and Workspace visibility for access control.

## Frequently asked questions

### Do Module Settings apply to every company?

Many module settings are site-wide, while some rows or defaults are company-specific. Read the field description and test with the affected company before rollout.

### Are Module Settings a replacement for Company defaults?

Company defaults supply accounts and other company-owned values. Module settings control process behaviour. Both can affect the same transaction for different reasons.

### Should administrators change several settings at once?

Change one business decision at a time and verify it in a new transaction. This makes an unexpected result easier to trace.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Global Defaults](/erpnext/global-defaults)
- [Session Defaults](/erpnext/session-defaults)
- [Domain Settings](/erpnext/domain-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [Workspace](/erpnext/workspace)
