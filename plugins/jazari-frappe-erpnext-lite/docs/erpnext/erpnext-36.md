<!-- Frappe documentation: erpnext, part 36 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__managing-transactions-in-multiple-currencies.md -->
---
title: "Managing Transactions in Multiple Currencies | ERPNext Documentation"
description: "Create, review, print, pay, and verify foreign-currency sales and purchase transactions in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-transactions-in-multiple-currencies"
updated: "2026-08-14"
---

Nova Industries distributes electronics internationally while keeping its Company accounts in USD.



EuroTech Retail wants to receive and pay a EUR invoice, while Nova must keep its books in USD. Users need to enter, print, collect, and reconcile the sale in EUR without losing the USD value required for accounting.



This guide follows a EUR 1,200 Sales Invoice at `1 EUR = 1.15 USD`. The customer sees EUR 1,200 while ERPNext records USD 1,380 in Company currency. You will see where the currencies and rates come from, how payment is converted, and how to verify the result. The same controls apply to purchases through the corresponding Supplier and payable fields.

## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup):

- EUR is enabled in [Currency](/erpnext/currency).
- EuroTech Retail has Billing Currency EUR.
- Euro Receivables is a EUR Receivable [Account](/erpnext/chart-of-accounts) linked to the Customer.
- Nova Europe EUR is an enabled selling [Price List](/erpnext/price-lists).
- A dated EUR to USD rate exists in [Currency Exchange](/erpnext/currency-exchange), or the configured provider covers it.
- The Company has an Exchange Gain/Loss account.

Test the full invoice and payment cycle in Draft before using imported or live data.

## Create a foreign-currency Sales Invoice

1. Open Accounting &gt; Sales and Receivables &gt; Sales Invoice.
2. Select **Add Sales Invoice**.
3. Choose Nova Electronics Distribution and EuroTech Retail.
4. Confirm the Posting Date, Payment Due Date, and EUR Currency.
5. Review the Exchange Rate field. Its label states the direction.
6. Select Nova Europe EUR and confirm Price List Currency EUR.
7. Add the item, quantity, and rate.
8. Review taxes, payment terms, and totals.

[Screenshot on the live page: EUR transaction and price-list rates]

The screenshot shows two rates:


| Field                    | Purpose in this example                                                             |
| ------------------------ | ----------------------------------------------------------------------------------- |
| Exchange Rate            | Converts the EUR transaction total to the USD Company value. `1 EUR = 1.15 USD`.    |
| Price List Exchange Rate | Converts Price List currency to transaction currency. It is 1 because both are EUR. |


An Actual tax or charge entered directly on the transaction is entered in the transaction currency. Review calculated taxes and Company-currency equivalents according to the tax template and charge type.

## Confirm the receivable account

Open the Accounting section and check **Debit To**. It should be Euro Receivables for this Customer and Company.



[Screenshot on the live page: EUR receivable selected on the Sales Invoice]

If the selected account is in a foreign currency, the invoice currency must normally match it. Do not switch only the Currency field and ignore Debit To.

## Compare transaction and Company totals

Before submission, compare the party-facing total and the Company-currency total.



[Screenshot on the live page: EUR and USD Sales Invoice totals]

For EUR 1,200 at 1.15:


| View                        | Amount    |
| --------------------------- | ---------: |
| Customer invoice total      | EUR 1,200 |
| Company-currency total      | USD 1,380 |
| Receivable account currency | EUR       |


Submit only after the rate, account, prices, taxes, and terms are correct. The submitted [Sales Invoice](/erpnext/sales-invoice) retains these values even if a later Currency Exchange record changes.

## Print and send the invoice

Open Print or Preview and confirm that rates, amounts, totals, and amount in words use the expected party-facing currency. The print format should show EUR for the invoice values. Company-currency fields are accounting fields and do not normally replace the agreed invoice currency in the customer-facing document.

If the symbol or number separators are wrong, correct the Currency master or site number format rather than hard-coding symbols into every print format.

## Create the Payment Entry

Create the Payment Entry from the submitted invoice when possible:

1. Open the invoice and select Create &gt; Payment.
2. Confirm Payment Type **Receive** and the Customer.
3. Confirm **Paid From** is the EUR receivable account.
4. Select the actual bank account under **Paid To**.
5. Enter the amount received in the bank account currency.
6. Review Source Exchange Rate and the Company-currency amount.
7. Confirm the invoice reference and allocated amount.

[Screenshot on the live page: Account currencies in Payment Entry]



[Screenshot on the live page: Paid and received amounts with the source rate]

The paid-from and paid-to account currencies control the amount fields. In the example, EUR 1,200 is cleared from the receivable and USD 1,380 is received into the operating bank.

If the payment-date rate differs from the invoice rate, use [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference). Keep bank charges, withholding, write-offs, and exchange difference in their appropriate accounts.

## Enter a foreign-currency purchase

On a [Purchase Invoice](/erpnext/purchase-invoice), select the Supplier, EUR, the buying Price List, and the EUR payable account. Review the Exchange Rate and Price List Exchange Rate exactly as on the sales side.



[Screenshot on the live page: EUR Purchase Invoice conversion fields]

On submission, the payable outstanding is maintained according to the party account currency. Create a Pay-type Payment Entry and verify the amount removed from the bank and the EUR amount cleared from the payable.

## Transactions in several currencies for one party

Accounts Settings includes **Allow multi-currency invoices against single party account**.



[Screenshot on the live page: Allow invoices in multiple currencies against one party account]

This can support a party invoiced in multiple currencies while using a Company-currency party account. It does not make a bank account multi-currency, and it can make outstanding and payment interpretation harder. Use dedicated currency accounts for currencies that the business regularly holds or reconciles. Test [Payment Reconciliation](/erpnext/payment-reconciliation), ageing, credit notes, advances, and returns before enabling the option broadly.

## Verify reports

Use the [General Ledger](/erpnext/general-ledger) filtered by the foreign account. It shows debit, credit, and balance in account currency when appropriate.



[Screenshot on the live page: EUR bank balance in the General Ledger]

Review [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) in the party or account currency. Financial statements use Company currency. At period end, run [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) for eligible open foreign balances.

## Troubleshooting

### Currency changes but item rates look wrong

Check Price List, Price List Currency, and Price List Exchange Rate. The transaction Exchange Rate does not necessarily convert the source Item Price.

### The invoice cannot be saved because account currency differs

Use the matching receivable or payable account, or correct the party's per-Company default. Do not change an account currency after postings exist.

### Payment Entry receives the wrong USD amount

Check the paid-to bank currency, source or target rate, paid amount, received amount, and invoice allocation. Use the actual bank amount and account for legitimate differences separately.

### The printed currency differs from the agreement

Verify the submitted transaction Currency and Price List. Then inspect the print format for hard-coded symbols or base-currency fields.

## FAQs

### Can I omit the invoice exchange rate and convert only at payment?

No, ERPNext needs a Company-currency value when the invoice posts. A later payment can use a different rate and recognize the difference.

### Can the invoice and Price List use different currencies?

Yes, Price List Exchange Rate converts item prices, while Exchange Rate converts the transaction to Company currency.

### Why does Payment Entry not have a free Currency selector?

Its currencies come from the paid-from and paid-to accounts. Select accounts that represent the actual balances.

### Can I show Company currency on the print format too?

Yes, with an appropriate print design, but keep the agreed transaction-currency amount clear and verify custom fields and labels.

### What happens when a foreign invoice remains unpaid at month end?

Its foreign amount remains outstanding. Revalue the eligible account to update its Company-currency carrying value according to your closing policy.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__managing-tree-structure-masters.md -->
---
title: "Manage Tree Structure Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-tree-structure-masters"
updated: "2026-03-04"
---


Some of the masters in ERPNext are maintained in tree structure. Tree structured masters allow you to set Parent master, and Child masters under those Parents. Setting up this structure allows you creating intelligent report, and track growth at each level in the hierarchy.

Following is the partial list of masters which are maintained in the tree structure.

* Chart of Accounts

* Chart of Cost Centers

* Customer Group

* Territory

* Sales Person

* Item Group

Following are the steps to manage and create record in the tree structured master. Let's consider Territory master to understand managing tree masters.

####Step 1 : Go to Master

`Selling > Setup > Territory`

####Step 2 : Parent Territory

[Screenshot on the live page: Default Territories]

When click on Parent territory, you will see option to add child territory under it. All default Territory groups will be listed under Parent group called "All Territories". You can add further Parent or child Territory Groups under it.

####Step 3: Add new Territory

When click on Add Child, a dialog box will provide two fields.

**Territory Group Name**

Territory will be saved with Territory Name provided here.

**Group Node**

If Group Node selected as Yes, then this Territory will be created as Parent, which means you can further create sub-territories under it. If select No, then it will become child Territory which you will be able to select in another masters.

Only child Territory Groups are selectable in another masters and transactions.
[Screenshot on the live page: Default Territories]

Following is how Child Territories will be listed under a Parent Territory.

[Screenshot on the live page: Adding new Territories]

Following this steps, you can manage other tree masters as well in ERPNext.

<!-- page: erpnext/erpnext__manufacturer.md -->
---
title: "Manufacturer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturer"
updated: "2026-03-06"
---

**A manufacturer created or produces an Item.**

A Manufacturer may not be the same person/company that sells the Item under a specific [Brand](/erpnext/brand). For example, Unico Plastics can be the Manufacturer of plastic brushes but it may be sold under a Brand, say, Super Brushes.

In ERPNext, a Manufacturer can be used to identify Items using a specific part number.

To access the Manufacturer list, go to:

> Home > Stock > Manufacturer

## 1. How to Create a Manufacturer

1. Go to the Manufacturer list and click on New.
2. Enter a Manufacturer name and enter a description if needed.
3. Save.
  Manufacturer (picture on the live page)

After creating a Manufacturer, you can create an **Item Manufacturer** record with a Manufacturer Part Number for identification.

[Screenshot on the live page]

### 1.1 Additional details

The following details can be set for a Manufacturer:

- Website
- Country
- Logo

## 2. Features

### 2.1 Address and Contacts

An [Address](/erpnext/address) and [Contact](/erpnext/contact) can be set for this Manufacturer.

## 3. Related Topics

1. [Item](/erpnext/item)
2. [Supplier](/erpnext/supplier)
3. [Brand](/erpnext/brand)

<!-- page: erpnext/erpnext__manufacturing-dashboard.md -->
---
title: "Manufacturing Dashboard\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-dashboard"
updated: "2026-02-26"
---

[Screenshot on the live page]

---

## Number Cards

In ERPNext, Number Cards are a type of widget or visual component that displays key metrics or numerical data in a dashboard. They are typically used to show quick, high-level insights that help users keep track of important business performance indicators or operational statistics.

[Screenshot on the live page]

1. **Monthly Total Work Order** :- You will get the total count of Work Orders which are in Open, In Progress, and Completed state. The Work Orders created one month before the current date will be displayed in the number card.
2. **Monthly Completed Work Order** :- The user will get the total count of Work Orders which are in the Completed state. The Work Orders created one month before the current date will be displayed in the number card.
3. **Ongoing Job Card** :- The user will get the total count of Job Cards that are not in the Completed state.
4. **Monthly Quality Inspection** :- The user will get the total count of Quality Inspection records which are in the Submitted state. The Work Orders created one month before the current date will be displayed in the number card.

---

## Dashboard

You can see some predefined graph reports in the dashboard when you open the Manufacturing module. These reports are fully customizable, you can choose what to show or hide and also configure the metrics on which the reports are shown.

[Screenshot on the live page]

### Produced Quantity

The chart will give the information about the total quantity produced (using Work Order) in the last year on a Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

### Completed Operation

The chart will give information about the total number of operations completed in the last year on Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

---

[Screenshot on the live page]

### Work Order Analysis

This chart will give the information about the number of Work Orders based on Not Started, In Process, Stopped, Completed statuses. This Donut chart will provide the information based on the last year's Work Order data. Your can also change the date range by clicking on the **Filter** button.

### Quality Inspection Analysis

This chart will give information about the number of Quality Inspections based on Accepted and Rejected status. The chart type is a donut and it will provide the information based on the last year's quality inspection data. Your can change the date range by clicking on the **Filter** button.

### Pending Work Orders

The chart will give information about the number of Work Orders that are pending based on the aging days. The number of aging days is calculated based on the difference between the current date and planned start / actual start date days.

### Last Month Downtime Analysis

The chart will give information about the total number of minutes a machine was not working in the last month. This helps the operator to know which machine has not performed well and requires maintenance.

---

[Screenshot on the live page]

### Work Order Quantity Analysis

The chart will give information about the total number of quantities that are Pending and Completed based on the Work Orders every month for the last year.

### Job Card Analysis

The chart will give information about the total number of Job Cards which are in the Pending and Completed states every month for the last year.

<!-- page: erpnext/erpnext__manufacturing-reports.md -->
---
title: "Manufacturing Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-reports"
updated: "2026-02-26"
---


There are various reports in the Manufacturing module that help you track Work Order progress, production analytics, BOM reports, etc.

In all of these reports, you can set a chart to show a visual representation. To do this, click on the Set Chart button.

These reports can be accessed from:
> Home > Manufacturing > Reports

## Open Work Orders
Shows the open Work Orders which have not started production yet.

[Screenshot on the live page: Open Work Orders]

## Work in Progress Report

This report shows any work orders that have started and are in progress. The status of these Work Orders is 'In Process'.

[Screenshot on the live page: WIP report]

## Issued Items Against Work Order
Items that are issued to a Work Order and are transferred to the Work in Progress Warehouse are shown here.
[Screenshot on the live page: Items Against WO]


## Completed Work Orders
Work Orders which are completed with all the quantities in it manufactured are shown in this report.

[Screenshot on the live page: Completed Work Orders]

## Production Analytics
This report shows the overall analytics of all Work Orders.

[Screenshot on the live page: Production Analytics]

## BOM Search
In this report, you can search for specific BOMs based on the raw materials items used in them, then open it. Useful if you have a lot of BOMs.
[Screenshot on the live page: BOM search]

## BOM Stock Report
On selecting a BOM in this report, the raw material quantity in Warehouses will be shown. As you can see, the items which have insufficient quantity are shown in red and ones with enough quantity to manufacture the BOM Item are shown in green.

[Screenshot on the live page: BOM Stock Report]

<!-- page: erpnext/erpnext__manufacturing-settings.md -->
---
title: "Manufacturing Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-settings"
updated: "2026-02-26"
---

Manufacturing settings in ERPNext configure production workflows, manage bill of materials (BOM), track work orders, and oversee inventory to streamline operations and ensure efficient production management.


> Home > Manufacturing > Settings > Manufacturing Settings
> 
> 

**Raw Materials Consumption**
-----------------------------

[Screenshot on the live page: Screenshot 2024-08-29 at 3.28.09 PM]  


### 1. Allow Continuous Material Consumption

If enabled, materials can be consumed without immediately manufacturing finished goods in a single Work Order. This is useful if one or more time consuming products are being manufactured.

For example a single product takes a month to manufacture and the raw materials are consumed daily. In a regular scenario, this won't be feasible with stock entries. Enabling this option will allow you to create stock entries for **Material Consumption** without having to create an entry to backflush. End result is that you can see the stock being consumed in the Warehouses and can update the final manufacture entry for finished goods at a later stage.

### 2. Backflush raw materials based on

The method selected here will be chosen for backflushing raw materials : 1. Material Transferred for Manufacture 2. BOM

### 3. Validate Components and Quantities Per BOM

Note: This feature will be available from the version V15

[Screenshot on the live page]

If "Backflush Raw Materials Based On" as BOM, then users can validate component quantity according to BOM. To do that they have to enable "Validate Components Quantities Per BOM" checkbox in the "Manufacturing Settings".

If user has changed the quantity in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

[Screenshot on the live page: component-qty-validation]  

If user has removed the item in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

[Screenshot on the live page]


### 4. Get Raw Materials Cost from Consumption Entry

[Screenshot on the live page]

If the 'Allow Continuous Material Consumption' is enabled then user can see the option 'Get Raw Materials Cost from Consumption Entry'.

The 'Get Raw Materials Cost from Consumption Entry', determines whether the cost of raw materials used in production should be automatically derived from the consumption entries recorded during the manufacturing process. When enabled, ERPNext calculates the cost based on the actual materials consumed, ensuring accurate cost tracking and financial reporting.

Capacity Planning
-----------------

Capacity planning is the process in which an organisation decides whether or not to accept the new orders based on the resources and existing work orders.

[Screenshot on the live page: Screenshot 2024-08-29 at 3.30.52 PM]  


### 1. Disable Capacity Planning

If checked, capacity planning won't be done. Enabling it will help to decide whether or not to accept the new orders based on the resources and existing work orders.

### 2. Allow Overtime

If enabled it'll allow creating work orders, job cards etc. outside workstation working hours.

### 3. Allow Production on Holidays

If enabled, it'll allow production activities even on those days that are marked as holidays as per the Holiday List of the organisation.

### 4. Capacity Planning For (Days)

The number of days specified here means the number of days in advance when the capacity planning activities will be initiated for production.

### 5. Time Between Operations (Mins)

This specifies the time span that should be kept between two operations in minutes.

Default Warehouses for Production
---------------------------------

[Screenshot on the live page: Screenshot 2024-08-29 at 3.32.55 PM]  


### 1. Default Work In Progress Warehouse

This Warehouse will be auto-updated in the 'Work In Progress' Warehouse field of Work Orders.

### 2. Default Finished Goods Warehouse

This Warehouse will be auto-updated in the 'Target Warehouse' field of Work Order.

### 3. Default Scrap Warehouse

This Warehouse will be auto-updated in the 'Scrap Warehouse' field of Work Order.

Over Production for Sales and Work Order
----------------------------------------

[Screenshot on the live page: Screenshot 2024-08-29 at 3.36.10 PM]  


### 1. Overproduction Percentage For Sales Order

It allows you to specify a percentage by which production can exceed the sales order quantity.

### 2. Overproduction Percentage For Work Order

It defines the allowable percentage by which the actual production quantity can exceed the planned quantity specified in a work order.

Job Card
--------

[Screenshot on the live page: Screenshot 2024-08-29 at 3.38.32 PM]  


### 1. Add Corrective Operation Cost in Finished Good Valuation

If enabled then the cost for a corrective operation type will also be included while calculating finished goods valuation

### 2. Allow Excess Material Transfer

If enabled, the **Material Transfer** button will be visible and will allow you to transfer raw materials even if after the raw material requirement is fulfilled against a Job Card.

This is particularly useful in cases where the transferred raw materials are damaged and additional raw materials need to be transferred to produce the same amount of finished goods as intended.

Other Settings
--------------

[Screenshot on the live page: Screenshot 2024-08-29 at 3.39.41 PM]  


### 1. Update BOM Cost Automatically

If ticked, the BOM cost will be automatically updated based on Valuation Rate / Price List Rate / last purchase rate of raw materials.

### 2. Set Operating Cost / Scrape Items From Sub-assemblies

In the case of 'Use Multi-Level BOM' in a work order, if the user wishes to add sub-assembly costs to Finished Goods items without using a job card as well the scrap items, then this option needs to be enable.

### 3. Make Serial No/Batch from Work Order

If checked, system will automatically create the serial numbers / batches for finished goods on submission of Work Order

### 4. Allow Editing of Items and Quantities in Work Order

If enabled, the system will allow users to edit the raw materials and their quantities in the Work Order. The system will not reset the quantities as per the BOM, if the user has changed them in the work order materials table.


[Screenshot on the live page: Screenshot 2025 11 07 at 3.25.52 PM]

<!-- page: erpnext/erpnext__manufacturing-without-creating-bom.md -->
---
title: "Manufacturing without creating BOM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-without-creating-bom"
updated: "2026-03-02"
---

**It is recommended to use BOM for Manufacturing for consistency and to avoid repetitive work.**   
However, if you wish to perform it manually, the workaround is to create Stock Entries:1) Create a **Stock Entry** with **Purpose** as **Material Transfer to Manufacture.**[Screenshot on the live page]2) Create a **Stock Entry** with **Purpose** as **Manufacture, the Item which is being Manufactured will have a Target Warehouse and other Items(Raw Materials) will have a Source Warehouse.**   
[Screenshot on the live page]  
*﻿Blue Dot: Item is being received.* *Orange Dot: Item is being issued.* 

<!-- page: erpnext/erpnext__manufacturing.md -->
---
title: "Manufacturing in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing"
updated: "2026-02-26"
---

The Manufacturing module in ERPNext is designed to streamline and optimise the production process. It integrates with other modules to conduct various manufacturing operations effectively.

- **Workstations**: Represents the locations or equipment where production activities are carried out.
- **Job Cards**: Provides detailed instructions and tracking for each step in the production process.
- **Bill of Materials (BoM)**: Defines the components and raw materials needed to produce a finished product.
- **Work Orders**: Manages the creation, tracking, and execution of work orders based on MoMs.
- **Production Planning**: Helps in scheduling and optimizing production runs to meet demand and manage resources efficiently.
- **Quality Control**: Ensures products meet quality standards through inspections.
- **Inventory Management**: Integrates with the Inventory module to manage raw materials, work-in-progress, and finished goods.
- **Reporting and Analytics**: Offers insights into production performance, costs, and efficiency to support informed decision-making.

The Manufacturing module in ERPNext helps improve productivity, reduce costs, and enhance overall production efficiency by providing a unified platform for managing all aspects of the manufacturing process.

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

[Screenshot on the live page: Material Request]  


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

[Screenshot on the live page: Screenshot 2024-07-09 at 2.36.44 PM]
5. Select the Item and set the quantity.
6. Select the Warehouse for which Items are required.
7. You can change the Required By date for individual Items in this table.
8. Save and Submit.

[Screenshot on the live page: Screenshot 2024-07-09 at 2.40.52 PM]  


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

[Screenshot on the live page: Screenshot 2024-07-09 at 2.38.58 PM]  


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

[Screenshot on the live page]

## Delivery Schedules

Some customers do not prefer a one time delivery against a sales order and they require multiple deliveries. The delivery schedules are very helpful for MRP because they provide visibility of when materials are actually needed, instead of assuming everything must be delivered at once.  
To make Delivery Schedules, users has to click on Add Schedule button in the sales order item table

[Screenshot on the live page]



## Master Production Schedule

To capture the demand for finished items, the Master Production Schedule (MPS) document was introduced. The system collects data from various sources such as sales orders, material requests, sales forecasts, and delivery schedules to generate the demand in the MPS.

[Screenshot on the live page]

## Material Requirements Planning Report

The Material Requirements Planning (MRP) report calculates the required quantities of raw materials and components, along with the dates when they are needed, based on the demand for finished items.



[Screenshot on the live page]

Users can see the MRP report in the bucket view

[Screenshot on the live page]

## Item Lead Time

To calculate the dates of when to release the purchase order for raw materials and work order for components, the system needs to be aware of the lead time for manufacturing and the lead time for material procurement. For this purpose, a new document Item Lead Time was added.



[Screenshot on the live page]

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

[Screenshot on the live page: Delivery Note Material Transfer]

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

[Screenshot on the live page: Purchase Receipt Material Transfer]

In the Supplier Warehouse, select a Warehouse from where Material is to be transferred.

[Screenshot on the live page: Purchase Receipt Material Transfer]

On submission of the Purchase Receipt, item's stock will be deducted from "Supplier Warehouse" and added to the "Accepted Warehouse".

<!-- page: erpnext/erpnext__material_consumption.md -->
---
title: "Material consumption\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/material_consumption"
updated: "2026-03-02"
---


Material Consumption functionality allows you to have multiple consumption `Stock Entry` against a Work Order. To enable this, go to Manufacturing > Manufacturing Settings.

[Screenshot on the live page: Item Alternative]

Once enabled, a `Material Consumption` button will be available in Work Order once started.

[Screenshot on the live page: Item Alternative]

When button is clicked, it will do the following:

1. It will create Stock Entry with purpose `Material Consumption for Manufacture`.

[Screenshot on the live page: Item Alternative]

2. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `BOM`, if will propose to consume all required qty for manufacture.
3. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `Material Transferred for Manufacture`, if will propose to consume all transferred qty for manufacture.
4. Once submitted, it will update `Consumed Qty` column in the Work Order.

[Screenshot on the live page: Item Alternative]

5. In succeeding Material Consumption, it will suggest unconsumed qty.
6. Once "Finish" button is clicked in Work Order, it will take into account consumed qty.

### Validations

* If "Allow Multiple Material Consumption" is not set in Manufacturing Settings but "Material Consumption for Manufacture" is use in Stock Entry.

[Screenshot on the live page: Item Alternative]

* Cannot cancel "Material Consumption for Manufacture" for completed Work Order.

[Screenshot on the live page: Item Alternative]
