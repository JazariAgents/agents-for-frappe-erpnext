<!-- Frappe documentation: erpnext, part 10 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__manufacturing-dashboard.md -->
---
title: "Manufacturing Dashboard\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-dashboard"
updated: "2026-02-26"
---

![](/files/image077385.png)

---

## Number Cards

In ERPNext, Number Cards are a type of widget or visual component that displays key metrics or numerical data in a dashboard. They are typically used to show quick, high-level insights that help users keep track of important business performance indicators or operational statistics.

![](/files/CleanShot 2026-02-19 at 11.41.16@2x.png)

1. **Monthly Total Work Order** :- You will get the total count of Work Orders which are in Open, In Progress, and Completed state. The Work Orders created one month before the current date will be displayed in the number card.
2. **Monthly Completed Work Order** :- The user will get the total count of Work Orders which are in the Completed state. The Work Orders created one month before the current date will be displayed in the number card.
3. **Ongoing Job Card** :- The user will get the total count of Job Cards that are not in the Completed state.
4. **Monthly Quality Inspection** :- The user will get the total count of Quality Inspection records which are in the Submitted state. The Work Orders created one month before the current date will be displayed in the number card.

---

## Dashboard

You can see some predefined graph reports in the dashboard when you open the Manufacturing module. These reports are fully customizable, you can choose what to show or hide and also configure the metrics on which the reports are shown.

![](/files/CleanShot 2026-02-19 at 11.52.51@2x.png)

### Produced Quantity

The chart will give the information about the total quantity produced (using Work Order) in the last year on a Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

### Completed Operation

The chart will give information about the total number of operations completed in the last year on Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

---

![](/files/image31eb3a.png)

### Work Order Analysis

This chart will give the information about the number of Work Orders based on Not Started, In Process, Stopped, Completed statuses. This Donut chart will provide the information based on the last year's Work Order data. Your can also change the date range by clicking on the **Filter** button.

### Quality Inspection Analysis

This chart will give information about the number of Quality Inspections based on Accepted and Rejected status. The chart type is a donut and it will provide the information based on the last year's quality inspection data. Your can change the date range by clicking on the **Filter** button.

### Pending Work Orders

The chart will give information about the number of Work Orders that are pending based on the aging days. The number of aging days is calculated based on the difference between the current date and planned start / actual start date days.

### Last Month Downtime Analysis

The chart will give information about the total number of minutes a machine was not working in the last month. This helps the operator to know which machine has not performed well and requires maintenance.

---

![](/files/image60f6db.png)

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

![Open Work Orders](/files/open-wo.png)

## Work in Progress Report

This report shows any work orders that have started and are in progress. The status of these Work Orders is 'In Process'.

![WIP report](/files/wip-report.png)

## Issued Items Against Work Order
Items that are issued to a Work Order and are transferred to the Work in Progress Warehouse are shown here.
![Items Against WO](/files/items-against-wo.png)


## Completed Work Orders
Work Orders which are completed with all the quantities in it manufactured are shown in this report.

![Completed Work Orders](/files/completed-wo.png)

## Production Analytics
This report shows the overall analytics of all Work Orders.

![Production Analytics](/files/production-analytics.png)

## BOM Search
In this report, you can search for specific BOMs based on the raw materials items used in them, then open it. Useful if you have a lot of BOMs.
![BOM search](/files/bom-search.png)

## BOM Stock Report
On selecting a BOM in this report, the raw material quantity in Warehouses will be shown. As you can see, the items which have insufficient quantity are shown in red and ones with enough quantity to manufacture the BOM Item are shown in green.

![BOM Stock Report](/files/bom-stock-report.png)

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

![Screenshot 2024-08-29 at 3.28.09 PM](/files/Screenshot 2024-08-29 at 3.28.09 PM.png)  


### 1. Allow Continuous Material Consumption

If enabled, materials can be consumed without immediately manufacturing finished goods in a single Work Order. This is useful if one or more time consuming products are being manufactured.

For example a single product takes a month to manufacture and the raw materials are consumed daily. In a regular scenario, this won't be feasible with stock entries. Enabling this option will allow you to create stock entries for **Material Consumption** without having to create an entry to backflush. End result is that you can see the stock being consumed in the Warehouses and can update the final manufacture entry for finished goods at a later stage.

### 2. Backflush raw materials based on

The method selected here will be chosen for backflushing raw materials : 1. Material Transferred for Manufacture 2. BOM

### 3. Validate Components and Quantities Per BOM

Note: This feature will be available from the version V15

![](/files/validate_component_and_qty_as_per_bom.png)

If "Backflush Raw Materials Based On" as BOM, then users can validate component quantity according to BOM. To do that they have to enable "Validate Components Quantities Per BOM" checkbox in the "Manufacturing Settings".

If user has changed the quantity in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

![component-qty-validation](/files/component-qty-validation.png)  

If user has removed the item in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

![](/files/Screenshot%202025-01-02%20at%2012.54.40%20PM.png)


### 4. Get Raw Materials Cost from Consumption Entry

![](/files/Screenshot%202025-01-02%20at%201.28.32%20PM.png)

If the 'Allow Continuous Material Consumption' is enabled then user can see the option 'Get Raw Materials Cost from Consumption Entry'.

The 'Get Raw Materials Cost from Consumption Entry', determines whether the cost of raw materials used in production should be automatically derived from the consumption entries recorded during the manufacturing process. When enabled, ERPNext calculates the cost based on the actual materials consumed, ensuring accurate cost tracking and financial reporting.

Capacity Planning
-----------------

Capacity planning is the process in which an organisation decides whether or not to accept the new orders based on the resources and existing work orders.

![Screenshot 2024-08-29 at 3.30.52 PM](/files/Screenshot 2024-08-29 at 3.30.52 PM.png)  


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

![Screenshot 2024-08-29 at 3.32.55 PM](/files/Screenshot 2024-08-29 at 3.32.55 PM.png)  


### 1. Default Work In Progress Warehouse

This Warehouse will be auto-updated in the 'Work In Progress' Warehouse field of Work Orders.

### 2. Default Finished Goods Warehouse

This Warehouse will be auto-updated in the 'Target Warehouse' field of Work Order.

### 3. Default Scrap Warehouse

This Warehouse will be auto-updated in the 'Scrap Warehouse' field of Work Order.

Over Production for Sales and Work Order
----------------------------------------

![Screenshot 2024-08-29 at 3.36.10 PM](/files/Screenshot 2024-08-29 at 3.36.10 PM.png)  


### 1. Overproduction Percentage For Sales Order

It allows you to specify a percentage by which production can exceed the sales order quantity.

### 2. Overproduction Percentage For Work Order

It defines the allowable percentage by which the actual production quantity can exceed the planned quantity specified in a work order.

Job Card
--------

![Screenshot 2024-08-29 at 3.38.32 PM](/files/Screenshot 2024-08-29 at 3.38.32 PM.png)  


### 1. Add Corrective Operation Cost in Finished Good Valuation

If enabled then the cost for a corrective operation type will also be included while calculating finished goods valuation

### 2. Allow Excess Material Transfer

If enabled, the **Material Transfer** button will be visible and will allow you to transfer raw materials even if after the raw material requirement is fulfilled against a Job Card.

This is particularly useful in cases where the transferred raw materials are damaged and additional raw materials need to be transferred to produce the same amount of finished goods as intended.

Other Settings
--------------

![Screenshot 2024-08-29 at 3.39.41 PM](/files/Screenshot 2024-08-29 at 3.39.41 PM.png)  


### 1. Update BOM Cost Automatically

If ticked, the BOM cost will be automatically updated based on Valuation Rate / Price List Rate / last purchase rate of raw materials.

### 2. Set Operating Cost / Scrape Items From Sub-assemblies

In the case of 'Use Multi-Level BOM' in a work order, if the user wishes to add sub-assembly costs to Finished Goods items without using a job card as well the scrap items, then this option needs to be enable.

### 3. Make Serial No/Batch from Work Order

If checked, system will automatically create the serial numbers / batches for finished goods on submission of Work Order

### 4. Allow Editing of Items and Quantities in Work Order

If enabled, the system will allow users to edit the raw materials and their quantities in the Work Order. The system will not reset the quantities as per the BOM, if the user has changed them in the work order materials table.


![Screenshot 2025 11 07 at 3.25.52 PM](/files/Screenshot%202025-11-07%20at%203.25.52%20PM.png)

<!-- page: erpnext/erpnext__manufacturing-without-creating-bom.md -->
---
title: "Manufacturing without creating BOM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-without-creating-bom"
updated: "2026-03-02"
---

**It is recommended to use BOM for Manufacturing for consistency and to avoid repetitive work.**   
However, if you wish to perform it manually, the workaround is to create Stock Entries:1) Create a **Stock Entry** with **Purpose** as **Material Transfer to Manufacture.**![](/files/EsxLtl4.png)2) Create a **Stock Entry** with **Purpose** as **Manufacture, the Item which is being Manufactured will have a Target Warehouse and other Items(Raw Materials) will have a Source Warehouse.**   
![](/files/voUKccc.png)  
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

<!-- page: erpnext/erpnext__moving-asset-from-stock-item-to-fixed-asset-item.md -->
---
title: "Moving Asset from Stock Item to Fixed Asset Item | ERPNext Documentation"
description: "Correct an ERPNext Item that was treated as stock but should be a fixed asset without losing accounting control."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/moving-asset-from-stock-item-to-fixed-asset-item"
updated: "2026-08-15"
---

Imagine Nova Industries bought a laptop intending to sell it, so it was received as inventory. Later, the company decides to give that laptop to an employee. It is no longer stock for sale, but simply selecting **Is Fixed Asset** can leave the same value appearing in both inventory and fixed assets.



The correction must remove the approved inventory position first, then create the fixed-asset Item and Asset record with the right original cost and opening depreciation. This keeps the Stock Ledger, General Ledger, and Asset Register from counting the laptop twice.

## Before you begin

Back up the site, identify every stock transaction for the Item, reconcile its current quantity and valuation, and agree the correction date and accounts with the accounting owner. Do not use this procedure to rewrite genuine historical sales inventory.

## Correct the stock position

1. Stop new transactions for the Item during the correction.
2. Use the appropriate [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation) or supported stock transaction to bring the stock position to the approved result.
3. Verify Stock Ledger and General Ledger impact.
4. If submitted transactions prevent changing Item type, create a new fixed-asset Item rather than forcing the existing record.

## Configure the fixed-asset Item

Enable **Is Fixed Asset**, select the Asset Category, and decide whether future purchases should auto-create Assets.

![ERPNext Item configured as a fixed asset](https://novacompanies.m.frappe.cloud/files/06-fixed-asset-item.png)

## Create the Asset

Create an Existing Asset using the approved original cost, available-for-use date, opening accumulated depreciation, and number of already booked depreciation entries.

![Existing Asset created after reclassification](https://novacompanies.m.frappe.cloud/files/07-asset-core-details.png)

## Verify the correction

Confirm stock quantity is no longer carried incorrectly, the Asset appears in the register, opening value and depreciation reconcile, and no cost was counted twice.

![Asset list used to verify the reclassified item](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### Is Fixed Asset cannot be enabled

The Item has submitted stock transactions or quantity. Create a new fixed-asset Item and use controlled accounting entries instead of forcing the flag.

### The asset cost appears in both stock and fixed assets

Reverse or correct the stock side, then reconcile Stock Ledger, General Ledger, and Fixed Asset Register on the same date.

### Opening depreciation is missing

Enter approved opening accumulated depreciation and the number of booked depreciations on the Existing Asset before final submission.

## Frequently asked questions

### Can I convert an Item after years of stock transactions?

Usually a new fixed-asset Item is safer because historical inventory transactions must remain valid.

### Should the reclassification use a Journal Entry only?

A Journal Entry may correct accounts but does not create the operational Asset history or remove stock quantity. Use the full controlled process.

### What date should the Asset use?

Use the approved original purchase and available-for-use dates, with opening depreciation as of the migration or correction cut-off.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__mpesa-integration.md -->
---
title: "M-Pesa Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/mpesa-integration"
updated: "2026-02-26"
---


**M-Pesa integration allows processing transactions with the payment gateway provider M-Pesa.**

M-Pesa Integration facilitates the processing of payments between the M-Pesa application and ERPNext. M-Pesa Integration only works with the POS to facilitate the payments for the same. This feature doesn't work with the shopping cart.

To set up M-Pesa, go to:
> Integrations > Payments > M-Pesa Settings

## 1.How to get your M-Pesa credentials?
1. In order to activate your API credentials, you need to log in to your M-Pesa account.
2. Then, open the Go Live section of the application and follow the steps to get the approval for the app.
3. When all the test cases are satisfied and expected results match the final results, you need to submit the document and follow the steps to get the final credentials for your application.
4. Details mentioned in the Production URL and Credentials section are the credentials that you are supposed to use in M-Pesa Settings.

![Mpesa Credentials](/files/mpesa_credentials.png)


## 2.Setting up M-Pesa

To enable M-Pesa Express, you need to configure all the mandatory parameters which you have received from M-Pesa. If you want to use the staging environment of the integration, you can select the staging option and use the staging credentials provided by M-Pesa by creating a separate application for the same.
![Mpesa Settings](/files/mpesa_settings.png)

On enabling the M-Pesa integration in ERPNext, the system will create a Payment Gateway record and an Account head in the Chart of Accounts with the Account type as Bank as seen in the following screenshot.

![Mpesa COA](/files/mpesa_coa.png)
![Mpesa POS Settings](/files/mpesa_pos_settings.png)

It will also create a Mode of Payment with the same name and account as the payment gateway's, along with certain custom fields in POS Settings to handle the POS payments.

![Payment Gateway Account](/files/payment_gateway_account_mpesa.png)

After configuring the Payment Gateway Account, you will be able to accept online payments via M-Pesa.


## 3. M-Pesa POS Payments

On setting up the POS profile with M-Pesa mode of payment, the POS checkout would show an additional information section. This section contains two fields that were automatically set-up on adding M-Pesa settings.

![POS Additional Information](/files/additional-information.png)

As soon as a POS user fills the mobile number of the customer, they can initiate a request for payment from the customer. A request is sent to the customer's M-Pesa mobile application linked with the specified mobile number. Once the payment is processed by the user, the user is prompted by a confirmation dialog to submit the payment.

## 4. M-Pesa Account Balance

Account balance linked with an individual M-Pesa can be fetched via the Get Account Balance button. This will load the M-Pesa account balance details in the dashboard.

![POS Account Balance](/files/mpesa_account_balance.png)


## 5. Supporting transaction currencies

M-Pesa will only work for the Company which has KSH (Kenyan Shilling) as the Company Currency.

<!-- page: erpnext/erpnext__multi-currency-accounting.md -->
---
title: "Multi Currency Accounting | ERPNext Documentation"
description: "Set up and operate ERPNext accounting for foreign customers, suppliers, bank accounts, invoices, payments, and revaluation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/multi-currency-accounting"
updated: "2026-08-14"
---

Nova Industries manufactures electronics, buys components abroad, and distributes finished products in several currencies.



Nova buys components and sells finished products internationally. A customer may need an invoice in EUR, a supplier may expect payment in JPY, and Nova must still report one consistent set of books in USD. Multi-currency accounting keeps each foreign amount together with its Company-currency value.



For example, Nova invoices EuroTech Retail for EUR 1,200 at `1 EUR = 1.15 USD`. The customer sees EUR 1,200 while ERPNext records USD 1,380 for reporting. This page explains how Company, account, transaction, and pricing currencies work together from setup through payment and revaluation.

## The three currencies to distinguish


| Currency             | What it controls                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Company currency     | The base accounting currency configured on the [Company](/erpnext/company-setup). Financial statements and base debit and credit values use it.              |
| Account currency     | The fixed currency of a ledger in the [Chart of Accounts](/erpnext/chart-of-accounts). A bank, receivable, or payable account should represent one currency. |
| Transaction currency | The currency shown on the invoice, order, or quotation. Its amount is converted to Company currency using the document's Exchange Rate.                      |


A [Price List](/erpnext/price-lists) adds another pricing currency. If it differs from the transaction currency, **Price List Exchange Rate** converts item prices separately from the document's accounting conversion rate.

## Before you begin

Enable the required [Currency](/erpnext/currency) records. Decide whether each Customer and Supplier will normally transact in one foreign currency or several currencies. Agree on the source and approval policy for exchange rates, the realized Exchange Gain/Loss account, the unrealized Exchange Gain/Loss account, and the revaluation frequency.

Do not change an Account's currency after ledger entries exist. Current ERPNext prevents this because old balances would become ambiguous. Create a correctly denominated account instead.

## Set up foreign-currency accounts

Create separate ledgers for each currency that must retain an account-currency balance. Examples include a EUR bank account, EUR receivable account, and EUR payable account.



![EUR bank account with its fixed account currency](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-account.png)

Each bank or cash account has one currency. If the real bank provides separate USD and EUR balances, represent them with separate ERPNext accounts. This keeps [Bank Reconciliation](/erpnext/bank-reconciliation) and audit trails intelligible.

## Configure Customers and Suppliers

Set a foreign Customer's **Billing Currency**, then add the matching receivable account in the Customer's Default Accounts child table. For a Supplier, use Billing Currency and the Per-Company Accounts table with the matching payable account.



![Customer billing currency](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-billing-currency.png)



![Open the Customer default-account row](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-account-pencil.png)

Select the highlighted pencil to open the full child-row editor.



![Customer linked to a EUR receivable account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-eur-receivable.png)

If a party account is in a foreign currency, the transaction must normally use that currency. If the account is in Company currency, **Allow multi-currency invoices against single party account** can permit invoices in other currencies, but the General Ledger entry remains in the party account's currency. Use that option only after testing invoicing, payment, ageing, and reconciliation behavior for your process.

## Configure exchange-rate behavior

Use [Currency Exchange](/erpnext/currency-exchange) for approved manual rates. If no eligible stored record exists, ERPNext can call the provider configured in [Currency Exchange Settings](/erpnext/currency-exchange-settings). Accounts Settings controls stale records and the posting date inherited by exchange-gain-or-loss entries.

For the demo, the approved rate is `1 EUR = 1.15 USD`.

## Create a foreign-currency Sales Invoice

1. Create a [Sales Invoice](/erpnext/sales-invoice) for the foreign Customer.
2. Confirm the transaction Currency and Exchange Rate.
3. Select a Price List and verify its currency and conversion rate.
4. Confirm that **Debit To** is the intended receivable account.
5. Add items, taxes, terms, and the payment schedule.
6. Compare the transaction and Company-currency totals before submission.

![EUR Sales Invoice and conversion rates](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-currency-rate.png)

The Exchange Rate converts EUR 1,200 to USD 1,380. The Price List Exchange Rate is 1 because both the Price List and invoice use EUR.



![EUR and USD totals on the Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-totals.png)

On submission, the receivable is maintained in the account currency and base debit and credit values are recorded in USD. The [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) report shows party or account-currency amounts according to its filters.

## Record foreign-currency purchases and payments

A [Purchase Invoice](/erpnext/purchase-invoice) follows the same pattern using the Supplier's payable account and buying rate. Outstanding and advance values follow the party account currency.

In a Payment Entry, currencies come from the selected accounts. Receiving EUR from a EUR receivable into a USD bank produces a paid amount in EUR, a received amount in USD, and a source exchange rate.



![Currencies of the paid-from and paid-to accounts](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![Exchange rate and converted amounts in Payment Entry](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

When the payment rate differs from the invoice rate, ERPNext can calculate a realized exchange difference. Use **Set Exchange Gain/Loss** where available, then inspect the Payment Deductions or Loss row and make the Difference Amount zero before submitting. Do not put a bank charge into the exchange account merely because it appears on the same bank statement. Bank fees and exchange differences are different expenses.

## Use multi-currency Journal Entries

Select **Multi Currency** on a [Journal Entry](/erpnext/journal-entry) when account rows use different currencies. Enter debit or credit in each account's currency and verify the exchange rate and calculated Company-currency amount. A Journal Entry requires deliberate debit and credit selection, so prefer Payment Entry for normal customer and supplier payments.

## Revalue open foreign balances

Exchange-rate movement after a transaction creates two kinds of difference:


| Difference | When it arises                                       | Typical tool                                                    |
| ---------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| Realized   | An invoice or payable is settled at a different rate | Payment Entry and Exchange Gain/Loss                            |
| Unrealized | A foreign balance remains open at a reporting date   | [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) |


Revaluation changes the Company-currency carrying value. It does not change the foreign amount. For example, EUR 1,000 remains EUR 1,000 while its USD value moves from USD 1,100 to USD 1,150.

## Verify reports

Filter the [General Ledger](/erpnext/general-ledger) by the foreign account to view debit, credit, and balance in account currency. Financial statements remain grounded in Company currency, while the Accounts Receivable and Payable report exposes party and account-currency values.



![EUR values in the General Ledger](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-general-ledger.png)

## Troubleshooting

### The party can be selected but the invoice currency is rejected

Check Billing Currency, the default receivable or payable account, and that account's currency. The transaction currency must be compatible with the party account unless the single-party-account option applies.

### Payment Entry shows the wrong currency

The paid-from and paid-to account currencies determine the amount fields. Select the intended bank, cash, receivable, or payable account instead of trying to type an independent Payment Entry currency.

### The foreign balance is zero but Company currency is not

This can occur after currency movements. Run Exchange Rate Revaluation at the reporting date and inspect the zero-balance treatment introduced for this situation.

## FAQs

### Can one bank account hold several currencies?

One ERPNext Account has one account currency. Use separate ledger accounts for separately maintained bank currency balances.

### Can one Customer receive invoices in several currencies?

It is possible in specific configurations, including the single-party-account setting, but a dedicated receivable account per regularly used currency gives clearer account-currency balances and payment behavior.

### Why is an exchange rate required even if payment will happen later?

ERPNext must record the Company's base-currency value on the invoice date. The payment can use a later rate, with the difference recorded as realized gain or loss.

### Does revaluation change the invoice amount?

No, it adjusts the base-currency carrying value of eligible accounts. The original invoice and foreign-currency amount remain unchanged.

### Can I change an account from USD to EUR after posting entries?

No, create a new EUR account and move future activity to it. Consult your accountant before transferring an existing balance.

## Related topics

- [Multi Currency Setup](/erpnext/multi-currency-setup)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)
- [Currency Exchange](/erpnext/currency-exchange)

<!-- page: erpnext/erpnext__multi-currency-setup.md -->
---
title: "Multi Currency Setup | ERPNext Documentation"
description: "Configure ERPNext for foreign-currency accounts, parties, rates, transactions, payments, and reporting in a reliable order."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/multi-currency-setup"
updated: "2026-08-14"
---

Before Nova Industries begins foreign-currency sales, its accounts, parties, Price Lists, rates, and payment settings must agree.



Nova wants to invoice EuroTech Retail in EUR while reporting its accounts in USD. Enabling EUR alone is not enough. The Customer, receivable account, Price List, rate source, payment account, and gain-or-loss accounts must agree, or the first invoice or payment can fail with a currency mismatch.



This page connects those settings in a safe order. By the end, Nova can create a EUR invoice, receive payment, record any exchange difference, and report the result in USD. Complete the sequence in a test Company before applying it to live Companies.

## Decide the accounting model

Answer these questions before configuring ERPNext:


| Decision                                    | Recommended starting point                                                                    |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| What is the Company's base currency?        | Use the statutory or primary reporting currency. Do not treat it as a per-transaction choice. |
| Which foreign balances must be retained?    | Create a separate account for each currency-specific bank, receivable, or payable balance.    |
| Does each party normally use one currency?  | Set its Billing Currency and matching default account.                                        |
| Are rates market-based or finance-approved? | Use the provider for market rates and Currency Exchange for controlled rates.                 |
| How are closing balances revalued?          | Configure unrealized gain or loss and a review frequency.                                     |


For the concepts behind these choices, read [Multi Currency Accounting](/erpnext/multi-currency-accounting).

## 1. Confirm the Company currency

Open the [Company](/erpnext/company-setup) and verify **Default Currency**. ERPNext uses it for base debit and credit values and Company financial statements. Changing it after transactions exist is a migration decision, not ordinary setup.

## 2. Enable required currencies

Open [Currency](/erpnext/currency), enable EUR, and review its symbol, fraction, and number format. Enabling a currency only makes it selectable. It creates no accounts or rates.



![EUR formatting and fractional-unit settings](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-eur-settings.png)

## 3. Create foreign-currency accounts

In the [Chart of Accounts](/erpnext/chart-of-accounts), create the ledgers that must keep foreign balances. For the example:

- Euro Bank, Account Type Bank, Currency EUR
- Euro Receivables, Account Type Receivable, Currency EUR
- Euro Payables, Account Type Payable, Currency EUR



![Foreign-currency bank account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-account.png)

Do this before posting entries. ERPNext does not allow an account's currency to be changed once ledger entries exist. Keep separate accounts for separate bank currencies even when the same institution supplies both balances.

## 4. Configure Customers and Suppliers

On the [Customer](/erpnext/customer), set Billing Currency to EUR. In Default Accounts, link Nova Electronics Distribution to Euro Receivables. Use the pencil in the child row to open the full editor.



![Billing Currency on the Customer](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-billing-currency.png)



![Customer default EUR account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-eur-receivable.png)

Apply the corresponding setup on the Supplier with Euro Payables. A party's billing currency and account currency should agree with the normal invoice currency.

## 5. Create currency-specific prices

Create a EUR [Price List](/erpnext/price-lists) when you maintain contractual or market prices in euros. Add EUR Item Prices. This is independent from the accounting rate. On a transaction:

- Exchange Rate converts the transaction total to Company currency.
- Price List Exchange Rate converts item prices when Price List currency differs from transaction currency.

When both the transaction and Price List use EUR, the Price List Exchange Rate is 1.

## 6. Define the exchange-rate policy

Create [Currency Exchange](/erpnext/currency-exchange) records for approved or historical rates. Configure [Currency Exchange Settings](/erpnext/currency-exchange-settings) for provider fallback. Decide how **Allow Stale Exchange Rates** and **Stale Days** should work in [Accounts Settings](/erpnext/accounts-settings).



![Approved EUR to USD rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-exchange-rate.png)

Document who may update manual rates, how often rates are reviewed, and whether buying and selling use the same rate. Store both directions when processes request both EUR to USD and USD to EUR.

## 7. Configure gain and loss accounts

In Company accounting defaults, set:


| Field                                 | Purpose                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| Exchange Gain / Loss Account          | Realized differences, commonly when a payment settles an invoice at a different rate. |
| Unrealized Exchange Gain/Loss Account | Reporting-date revaluation of balances that remain open.                              |


![Company exchange gain and loss accounts](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-company-exchange-gain-loss-accounts.png)

Use accounts approved by your accountant and local reporting policy. Some organizations separate gain and loss accounts or realized and unrealized presentation further through their chart and reporting design.

## 8. Test the complete cycle

Before importing or entering live data:

1. Create a draft EUR [Sales Invoice](/erpnext/sales-invoice) and verify EUR and USD totals.
2. Confirm Debit To is Euro Receivables.
3. Create a draft EUR [Purchase Invoice](/erpnext/purchase-invoice) and confirm Credit To is Euro Payables.
4. Create a [Payment Entry](/erpnext/payment-entry) using the intended bank account and verify paid, received, and Company-currency amounts.
5. Run the [General Ledger](/erpnext/general-ledger) and [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) reports.
6. Test [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) in Draft for a closing date.

Do not stop at a successfully saved invoice. The payment and reporting tests reveal account-currency mismatches that are easy to miss during setup.

Record the tested document names, expected rates, account balances, and report filters in the implementation checklist. Repeat the test for each regularly used currency and for both receipts and payments. A EUR sales test does not prove that a GBP supplier payment or a foreign bank transfer is configured correctly.

## Setup checklist


| Area     | Verification                                                                                   |
| -------- | ---------------------------------------------------------------------------------------------- |
| Currency | Required codes are enabled and display correctly.                                              |
| Company  | Base currency is correct and stable.                                                           |
| Accounts | Each foreign bank, receivable, and payable account has the intended currency and Account Type. |
| Parties  | Billing Currency and per-Company default account match.                                        |
| Pricing  | Price List currency and item prices match the commercial agreement.                            |
| Rates    | Manual records, provider, direction, date, and buying or selling flags are understood.         |
| Payments | Source and target account currencies produce the intended amounts.                             |
| Closing  | Realized and unrealized gain or loss accounts are configured.                                  |
| Reports  | Finance has verified account-currency and Company-currency views.                              |


## Troubleshooting

### ERPNext prevents changing an Account currency

The Account already has ledger entries. Create a new account with the correct currency and plan the transition with your accountant.

### The Customer defaults to EUR but the invoice uses USD

Check the selected Company, Debit To account, Billing Currency, transaction Currency, and whether the multi-currency-single-party-account setting changes the normal restriction.

### A Payment Entry has unexpected paid and received currencies

Review the paid-from and paid-to accounts. Their account currencies drive those fields.

## FAQs

### Do I need a separate receivable account for every Customer?

No, you can share one EUR receivable account across EUR Customers and use party dimensions in receivable reports. Separate accounts by currency or accounting need, not automatically by Customer.

### Should I enable Allow multi-currency invoices against single party account?

Only when the business genuinely invoices the same party in multiple currencies and has tested payment, outstanding, reconciliation, and reporting behavior. A dedicated account per regular currency is easier to reason about.

### Can the provider replace all manual Currency Exchange records?

It can supply market rates for supported pairs. Manual records remain useful for approved, historical, unsupported, or contract rates.

### Should revaluation be automatic?

Start with a reviewed manual process. Enable automatic creation only after the rate source, accounts, frequency, journal submission policy, and period-close controls are proven.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Currency Exchange](/erpnext/currency-exchange)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__naming-series-as-per-gst-rules.md -->
---
title: "Naming Series as Per GST Rules"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series-as-per-gst-rules"
updated: "2026-07-31"
---

Rule 46 (b) of the CGST **Rules** 2017 specifies that the tax **invoice** issued by a registered person should have a consecutive serial **number**, not exceeding sixteen characters, in one or multiple series, containing alphabets or numerals or special characters – hyphen or dash and slash symbolized as “-” and “/” respectively

  


This validation will come into effect in ERPNext from the new fiscal year i.e FY 2021-22. If you encounter an error similar to one shown in the screenshot below, follow the below steps to resolve the issue and add a new naming series for Sales and Purchase Invoices

  


![](/files/Nr1n53j.png)

  


Step 1: Go to "Naming Series" doctype and select transaction as "Sales Invoice"

  


![](/files/1KrOqdx.png)

  


Step 2: Add a new naming series having maximum upto 16 characters. For eg INV-.YYYY.-.#####. Add this as the first option and don't check "User must always select" inorder to make this as the defaut naming series

  


![](/files/hrHZ0Rv.png)

  


  

<!-- page: erpnext/erpnext__naming-series-current-value.md -->
---
title: "Set Current Value for Naming Series"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series-current-value"
updated: "2026-03-04"
---


Naming Series feature allows you to define prefix for naming of a documents. For example, if a Sales Order has prefix "SO", then the series will be generated as SO-00001, SO-00002... and so on. Click [here](/erpnext/document-naming-settings) to learn how you can customize Number Series for a transaction/master in ERPNext.

### 1. Setting the Current Value

Naming Series feature also offers a tool where you can set Current Value for specific prefix. This is generally required if you have recently started using ERPNext, and have old transactions in the previous system, and you want the numbering series to start in from where it ended in the old system. Let's consider a scenario to learn this better.

For example, you have 322 Sales Orders created in your old system with SO00322 as highest Sales Order Id. In ERPNext, you need the first Sales Order to pick up #323 when it is saved. To enable this, you should set Current Value for SO series in following steps.

#### Go to Naming Series Tool

`Setup > System > Naming Series`

#### Update Series Section

![Update Series Section](/files/current-no-1.png)

#### Select Prefix

Considering our scenario, prefix for Sales Order will be "SO".

![Series Prefix](/files/current-no-2.png)

#### Current Value

If you have currently 12 Sales Orders created in your account, then current value updated will be 12. You can edit Current Value to 322, and then click on Update Series Number.

![Series Current Value](/files/current-no-3.png)

With this setting, you will have numbering for the New Sales Orders starting with #323.

### 2. Error Due Series Number

If you receive a Duplicate Name error while saving a transaction, for example, while saving Item Price, you receive an error saying:

`Duplicate name Item Price RFD/00016`

This error message indicates that when you are saving Item Price, system is trying to allocate "RFD/00016" to that Item Price record. But it is finding that Item Price with this ID is already existing in your system.

This error could arise because Current Value for Series/Prefix of Item Price is disturbed and not in sync with actual Current Value. While actual Current Value for Item Price could be 20 (or any number more than 16), someone has set Current Value for this series as 15.

To confirm actual Current Value for particular Series, you should check report for document in question (Item Price in this case), and check for the Item Price ID with highest value.

Let's assume we find that actual Current Value for Item price is 22, then you go Naming Series, and set Current Value for the Prefix/Series of Item Price to 22, and Update Series Number.

These instructions is applicable for all the documents in ERPNext for which user can customize Series and its Current Value.

Let's consider another scenario to learn this better. On assigning a document to another user, error message says:

`Duplicate name ToDo TDI00014286`

This indicate the Current Value for Series/Prefix of ToDo (TDI) has been disturbed. You should follow these steps to correct value for Current Value for TDI prefix.

1. Check ToDo report for the highest ToDo id value.
1. Setup >> Settings >> Naming Series
1. Check section B of Update Series
1. Select Prefix for ToDo "TDI"
1. Ensure that highest number for ToDo is updated as Current Value in Naming Series. If not, correct Current Value, and click on "Update Series Numbering".

<!-- page: erpnext/erpnext__naming-series.md -->
---
title: "Naming Series\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series"
updated: "2026-03-04"
---


**Masters and transactions can be given prefixes in the form of naming series.**

ERPNext allows you to make prefixes to your documents, with each prefix
forming its own series. For example, a series with prefix INV12#### will have
numbers INV120001, INV120002, and so on.

You can have multiple series for all your transactions. For example, Sales Invoice IDs like these can be generated:

* ACC-SINV-.YYYY.-
* SINV12####
* SALESINV-00####

You can define or select the Naming Series pattern from:

> Home > Settings > Naming Series

## 1. Setting up Naming Series for Documents

1. Select the transaction for which you want to make the series. The system will update the current series in the text box.
2. Edit the series as required with unique prefixes for each series.
 The first prefix will be the default prefix. Each new prefix Naming Series must be added on a new line. The newly added naming series will be available in the document.
 ![Multiple naming series](/files/multiple-naming-series.gif)

3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox.
 There will be no default naming series if this is ticked.

1. You can also update the starting point of a series by entering the series name and the starting point in the “Update Series” section.

1. Click on the Update button to update the set of Naming Series for the selected document.

> Note: To see the newly added Naming Series, click on Settings > Reload.

## 2. Financial Year in Naming Series
You can also show the financial year in the Naming Series. By default, if you enter 'YYYY' in the naming series, it'll pick up the current year. To set naming series based on the fiscal year, enter something like 'ACC-SINV-.FY.-' where 'FY' will be resolved to match the current Fiscal Year. It is common to have a separate series for each financial year.

Alternatively it is also possible to manually embed the fiscal year in the naming series, for example by entering something like 'ACC-SINV-.19-20.-' where 19-20 is the current Fiscal Year.

As you can see, in the following screenshot of a Sales Invoice, the year 2019 is listed:

![Fiscal year in Naming Series](/files/year-naming-series.png)


## 3. Updating the current value for existing Naming Series

You can change the starting/current sequence number of an existing series.

1. Under the Update Series section, select the prefix whose sequence is to be changed.
1. The current value will be fetched and displayed.
1. Change starting/existing sequence number if needed.
1. Click on Update Series Number.

For example, if the current Sales Order series number is at 16, and you want to restart or set it as 50, enter 0 or 50 depending on your case. Any new Sales Order created will start from the new sequence number.

To know more about this, [visit this article](/erpnext/naming-series-current-value).

> Tip: You could have a separate series for each type of Customer or for
each of your retail outlets.

## 4. Using Field Values in Naming Series

Some companies prefer to make use of "short-codes" for suppliers, i.e. WN for company "Web Notes" that later can be used in naming series for quick identification.

For example:

 A custom field "Vendor ID" is created under Document: Supplier.
 Then under Naming Series, we allow something like
 PO-.YY.MM.-.vendor_id.-.####
 Resulting in "PO-1503-WN-00001"

## 5. Video


<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//IGyISSfI1qU">
</iframe>

<!-- page: erpnext/erpnext__newsletter.md -->
---
title: "Newsletter | ERPNext Documentation"
description: "Learn how to create, test, schedule, and send Newsletters to subscribed Email Groups in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/newsletter"
updated: "2026-07-23"
---

**Newsletter is an email which is sent to a specific group of subscribers periodically.**

In the context of CRM, its is an informational and product-focused email that is sent to existing and potential customers with an intention of softly pushing the subscriber to do required actions.

Newsletter can also be used to share information to employees, investors etc.

You need to create [Email Groups](/erpnext/email_group) before sending the newsletters.

To access the Newsletter list, go to:

> Home > Settings > Email > Newsletter

## How to Create a Newsletter

- Go to the Newsletter list and select New.
- Select the Email Group in RECIPIENT table.
- Enter 'Subject'.
- Enter 'Message'.
- 'Publish' the newsletter to make it available on the web.
- Tick 'Send Unsubscribe Link' if you would like to include unsubscribe link in the email.
- 'Send Web View Link' will include a link in the email to open the newsletter on the web. This option is only visible when the newsletter is published.

![Newsletter](/files/newsletter-doc.png)

Below is the screenshot of the email received with link to unsubscribe and a link to open the email on the web.

![Newsletter With Unsubscribe Link](/files/newsletter-doc-web-link.png)

## Features

### Create Subscriber Groups

You can manage subscribers by grouping them into different [Email Groups](/erpnext/email_group).

You can select multiple email groups in the 'RECIPIENT' tables in the newsletter.

### Schedule Send

You can choose to send your newsletter at any future datetime by specifying time in hourly steps.

![Scheduled Newsletter](/files/scheduled-newsletter.png)

### Test Newsletter Before Sending to Subscribers

Once the newsletter is ready you can provide a 'Test Email Address' and select 'Test'.

You can review the newsletter received in the test email, verify it and then send it to all subscribers by clicking on 'Send'.

![Newsletter Test](/files/newsletter-test.png)

<!-- page: erpnext/erpnext__non-conformance.md -->
---
title: "Non Conformance\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/non-conformance"
updated: "2026-02-26"
---

*A Non Conformance is a observation that can be filed by any person in the organization to note non compliance to a specific procedure*

Once Quality Procedures are defined, the goal of a quality focussed organization is to ensure that they hare followed. This ensures consistent quality and parameters as per the customer's expectation. If these procedures are not followed, an observation is recorded via a *Non Conformance* or called NC in quality systems.

In ERPNext, you can create a Non Conformance by selecting the Quality Procedure against which it was observed, maintain its status and record corrective and preventive actions

## 1. Prerequisites

1. [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)

## 2. How to Create a Non Conformance

1. Go to Quality > Non Conformance or find the Quality Procedure and click on + from the dashboard.
2. Record your observations
3. Record corrective / preventive actions if any
4. Update status

![](/files/Screenshot 2026-01-23 at 1.47.10 AM.png)

## 3. Related Topics

1. [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)

<!-- page: erpnext/erpnext__non-profit.md -->
---
title: "Non-profit Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/non-profit"
updated: "2026-07-02"
---

ERPNext can be used by non-profit organizations to manage their operations, accounting, donations, memberships, projects, and reporting. The non-profit features were historically provided through a separate custom app called Non Profit.

The app is not part of the standard ERPNext installation. It needs to be installed separately, and it may not be available or compatible with the latest versions of ERPNext and Frappe Framework.

GitHub app: [https://github.com/frappe/non_profit](https://github.com/frappe/non_profit)

## What the Non Profit app was designed for

The Non Profit app was built on top of Frappe Framework and ERPNext to support organizations that manage donors, members, grants, chapters, volunteers, and social impact programs.

It was meant to help non-profit teams use ERPNext for both financial and operational work, instead of managing donor and program records separately from accounting.

## Typical areas covered

The app may help with workflows such as:

- Donor and member management
- Donation tracking
- Membership records
- Grant and program tracking
- Volunteer or chapter-related records
- Accounting and reporting through ERPNext
- Linking operational records with invoices, payments, and accounts

The exact feature set depends on the version of the app installed and the ERPNext version it is used with.

## Important compatibility note

The Non Profit app repository is currently archived and read-only. This means it may not receive regular updates for newer ERPNext versions.

Before using it on a production site, check whether the app is compatible with your ERPNext and Frappe version. If it is not compatible, the recommended approach may be to build a small custom app or customizations for the specific non-profit workflows needed by your organization.

## When should you consider it?

Consider the Non Profit app if you are running an older compatible ERPNext version, or if you want to study the app as a reference for building non-profit workflows.

For newer ERPNext versions, treat it carefully and verify compatibility before installation.

## Learn more

You can view the app repository here:

[https://github.com/frappe/non_profit](https://github.com/frappe/non_profit)

<!-- page: erpnext/erpnext__not-able-to-select-has-serial-no-batch-option-in-item-list.md -->
---
title: "Cannot enable Serial and Batch Number"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/not-able-to-select-has-serial-no-batch-option-in-item-list"
updated: "2026-03-02"
---

It is quite possible at times that you do not want to start tracking the inventory as batched and/or serialized but want to start doing so at a later stage.   
The system, by design, doesn't allow you to activate these options once stock transactions have been made.![](/files/a0VHlSB.png)You can read more about why the same is disabled [here](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html).  
To enable the options again, you can either delete all stock transactions for this item, or if that is not an option, you can duplicate the same item and inward the stock with these options checked.  
**STEPS:****﻿**1. You will have to first stock out the current item using Stock Reconciliation Tool (make current stock zero). You can also stock out the item by making a stock entry of type **Material issue**.
2. Then using material receipt, inward the serialized inventory. Refer the following link for help on the same: [Opening Stock Balance Entry for Serialized and Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
3. Disable the old items so it cannot be selected in transactions again.

  
**Note:** If you want to maintain the same item code, you will need to rename the existing items, and then create the new item as per the actual item code. Otherwise, you will be maintaining the item under a new code.

<!-- page: erpnext/erpnext__notifications.md -->
---
title: "Notification"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/notifications"
updated: "2026-03-02"
---

**You can configure various notifications in your system to remind you of important activities.**

1. The completion date of a Task.
2. Expected Delivery Date of a Sales Order.
3. Expected Payment Date.
4. A reminder of follow up.
5. If an Order greater than a particular value is received or sent.
6. Expiry notification for a Contract.
7. Completion/Status change of a Task.

To access notification setup, go to:

> Home > Settings > Notification

1. Setting Up An Alert
----------------------

To set up a Notification:

1. Define what events you want to watch under Send Alert On. Events are:


	1. New: When a new document of the selected type is made.
	2. Save/Submit/Cancel: When a document of the selected type is saved, submitted, or canceled.
	3. Days Before/Days After: Trigger this alert a few days before or after the **Reference Date.** To set the days, set **Days Before or After**. This can be useful in reminding you of upcoming due dates or reminding you to follow up on certain leads of quotations.
	4. Value Change: When a particular value in the selected type changes.
	5. Method: Sends notification when a specific method is triggered. Eg: before_insert.
	6. Custom: Send a notification to an [Email Account](/erpnext/email-account) selected.
2. Select the Document Type you want to watch changes on. From Version 16, You can also select child Document Types if Send Alert On is set to *Days Before*or *Days After*.
3. Set additional Conditions if required.
4. Set the recipients of this alert. The recipient could either be a field of the document or a list of fixed Email Addresses.
5. Compose the message.
6. Save.

### 1.1 Setting a Subject

You can retrieve the data for a particular field by using `doc.[field_name]`. To use it in your subject/message, you have to surround it with `{% raw %}{{ }}{% endraw %}`. These are called [Jinja](http://jinja.pocoo.org/) tags. For example, to get the name of a document, you use `{% raw %}{{ doc.name }}{% endraw %}`. The following example sends an email on saving a Task with the Subject, "TASK#### has been created"

![Setting Subject](/files/email-alert-subject.png)  


### 1.2 Setting Conditions

Notifications allow you to set conditions according to the field data in your documents. For example, if you want to receive an Email if a Lead has been saved as "Interested" as it's status, you put `doc.status == "Interested"` in the conditions textbox. You can also set more complex conditions by combining them with the operator **and** or **or**.

![Setting Condition](/files/notification screenshotb9a4a2.jpg)  


The above example will send a Notification when a Task is saved with the status "Open" and the "Expected End Date" for the Task is the date on or before the date on which it was saved on.

### 1.3 Setting a Message

You can use both Jinja Tags (`{% raw %}{{ doc.[field_name] }}{% endraw %}`) and HTML tags in the message textbox.


```
{% raw %}<h3>Order Overdue</h3>
  

```
Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.

{% if comments %} Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }} {% endif %}


```
<h4>Details</h4>
  

```
  


* Customer: {{ doc.customer }}
* Amount: {{ doc.total_amount }}

{% endraw %}

  


### 1.4 Setting a Value after the Alert is Set

Sometimes to make sure that the Notification is not sent multiple times, you can define a custom property (via Customize Form) like "Notification Sent" and then set this property after the alert is sent by setting the **Set Property After Alert** field.

Then you can use that as a condition in the **Condition** rules to ensure emails are not sent multiple times

![Setting Property in Notification](/files/email-alert-subject.png)  


### 1.5 Example

1. Defining the Criteria ![Defining Criteria](/files/email-alert-1.png)
2. Setting the Recipients and Message ![Set Message](/files/email-alert-2.png)



---

2. Slack Notifications
----------------------

If you prefer to have your notifications sent to a dedicated Slack channel, you can also choose the option "Slack" in the channel options and select the appropriate Slack Webhook URL.

### 2.1 Slack Webhook URL

A Slack webhook URL is a URL pointing directly to a Slack channel.

To generate webhook URLs, you need to create a new Slack App:

1. Go to https://api.slack.com/slack-apps.
2. Click on "Create a Slack App". ![Set Message](/files/slack_notification_1.png)
3. Give your App a name and choose the right workspace. Once your app is created, go to the "Incoming Webhooks" section and add a new Webhook to Workspace. ![Set Message](/files/slack_notification_2.png)
4. Copy the created link, go back to ERPNext and use it to create a new Slack Webhook URL in Integrations > Slack Webhook URL. ![Set Message](/files/slack_notification_3.png)
5. Select Slack and your Slack channel in the channel and Slack channel fields within your notification

### 2.2 Message Format

Unlike Email messages, Slack doesn't allow HTML formatting.

Instead, you can use markdown formatting: [Slack Documentation](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)

Example: {% raw %} *Order Overdue*


```
Transaction {{ doc.name }} has exceeded Due Date. Please take the necessary action.


{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

*Details*

• Customer: {{ doc.customer }}
• Amount: {{ doc.grand_total }}
{% endraw %}
  

```
![Set Message](/files/slack_notification_4.png)  




---

3. System Notifications
-----------------------

In **Version 12** we introduced System notifications for **Assignments**, **mentions**, **documents shared**, and **Energy Points**. These notifications show up in the notifications dropdown on the the navigation bar's top right corner.

In **Version 13** we have introduced an additional channel to send alerts - **System Notifications**:

![Notifications Dropdown](/files/system-notifications-channel.png)  


Choosing this channel will send a system notification when a notification is triggered, instead of an Email or a Slack notification.

![Notifications Dropdown](/files/system-notification.png)  


Clicking on the notification routes to the **Notification Log** document which contains the configured subject, message as well as the attached file, if Attach Print is set:

![Notifications Dropdown](/files/notification-log.png)  


If Email/Slack alerts and System Notifications both are required, the main channel can be set as Email or Slack and this option can be checked:

![Notifications Dropdown](/files/send-system-notification.png)  


4. WhatsApp
-----------

In **Version 13** we have introduced an additional channel to send alerts - **WhatsApp**: ![Notifications WhatsApp Channel](/files/twilio-channel.png)  


If you prefer to have your notifications sent to a WhatsApp number, you can also choose the option "WhatsApp" in the channel options and select the appropriate Twilio Number. Twilio Numbers can be added to Twilio settings in Frappe. WhatsApp messages can only be sent to numbers which have country codes in them.

![Twilio Settings](/files/twilio-settings.png)  


### 4.1 Twilio Settings

In order to configure Twilio settings, you need to first obtain Twilio credentials from your Twilio Account's account settings. You can only add those phone numbers that have been activated in your Twilio Account with WhatsApp access. ![Twilio Credentials](/files/twilio-credentials.png)  


### 4.2 Message Format

WhatsApp allows their users to only send those message templates that are pre-approved by them to your customers. Failure to do so might result in restrictions on you Twilio account. ![Pre Approved Message Template](/files/twilio-pre-approved-message.png)  


5. SMS
------

In **Version 13** we have introduced an additional channel to send alerts - **SMS**: ![SMS Channel](/files/sms-notification-channel.png)  


In order to use this channel, you would need to complete the configuration of [SMS Settings](/erpnext/sms-setting).

### 6. Related Topics

1. [SMS Settings](/erpnext/sms-setting)
2. [Document Follow](/erpnext/document-follow)

### 7. One-off Reminders

> Note: This feature is only available in nightly version as of now.

Since setting up notifications is quite involved process, Frappe Framework also provides a way to setup one-off reminders on documents. Example of such notification would be "Remind me to follow up about this lead in 4 hour"

To set up one-off reminder on document:

1. Open the document on which you want to set a reminder
2. Click on menu (three dots) > "Remind Me"
3. Select time and add a description for yourself and click "Create"
4. System will send you a system notification around the time you've configured with reminder description as subject.

<!-- page: erpnext/erpnext__open-source.md -->
---
title: "Open Source"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/open-source"
updated: "2026-02-26"
---

The term open source refers to those software where the source code is available to the public for inspection, modification, enhancement and distribution to the software. This is contrast to the proprietary systems where the code is highly restricted.

ERPNext is a free and open source software published under [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

It grants you the freedom to..

* Use the software for any purpose
* Change the software to suit your needs
* Share the software with anyone
* Share the changes you make

The source code of ERPNext is available on [GitHub.](https://github.com/frappe/erpnext)

#### System Security

ERPNext uses encryption to protect all data at rest and in transit. This means that even if a hacker gains access to your data, they will not be able to read it without the correct key.

There are two main types of encryption used by ERPNext:

* **Symmetric encryption:** This uses the same key to encrypt and decrypt data. This is a simpler and more efficient type of encryption, but it requires that both the sender and receiver of the data have the same key.
* **Asymmetric encryption:** This uses two different keys, one for encryption and one for decryption. This is a more secure type of encryption, but it is also more complex and less efficient.

ERPNext uses a combination of symmetric and asymmetric encryption to protect data. For example, symmetric encryption is used to encrypt data at rest, while asymmetric encryption is used to encrypt data in transit.

In addition to encryption, ERPNext also uses other security features to protect data, such as:

* **Access control:** This allows you to control who has access to your data. You can create different user roles and permissions, so that only authorized users can access the data they need.
* **Intrusion detection:** This monitors your system for suspicious activity. If a hacker attempts to breach your security, ERPNext will alert you so that you can take action.
* **Regular security audits:** ERPNext is regularly audited by independent security firms to ensure that its security is up to date.

These security features make ERPNext one of the most secure ERP solutions on the market. If you are looking for a secure way to manage your business data, ERPNext is a good choice.

**Here are some additional benefits of using encryption in ERPNext:**

* It can help to protect sensitive data, such as customer information, financial data, and intellectual property.
* It can help to prevent data breaches, which can damage a company's reputation and financial bottom line.
* It can help to comply with data privacy regulations, such as the General Data Protection Regulation (GDPR).

#### Advantages of an open source software are:

1. There is no lock-in with one specific vendor.
2. You can host the application anywhere, including your own server to gain complete ownership and privacy of the data.
3. You can access a [community](https://discuss.erpnext.com/) for help.
4. You can benefit from using a product that is critiqued and used by a wide range of people, who have reported hundreds of issues and suggestions to improve the product.

While ERPNext is free and open source, running a server for ERPNext, implementing it and, supporting it is not an easy task. You can opt for professional help at [erpnext.com](https://erpnext.com/) or find a suitable service provider. This will allow you to reduce your risk and focus on delivering business value.

<!-- page: erpnext/erpnext__open-work-orders.md -->
---
title: "Open Work Order Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/open-work-orders"
updated: "2026-03-02"
---


We can easily identify the manufacturing progress of certain items in our organizations using **Open Work Orders** in ERPNext.

![Open Work Orders](/files/open-work-order.png)

In this report users are able to see:

- Items that need to be produced
- The total quantity to produce 
- The quantity that has already been produced

For further details, users can proceed to click on the work order and expand it e.g. MFG-WO-2018-00009. This helps you prioritise Work Orders by their date

<!-- page: erpnext/erpnext__opening-and-closing.md -->
---
title: "Opening and Closing During Migration | ERPNext Documentation"
description: "Close the legacy accounting period, load ERPNext opening data in sequence, reconcile it, freeze the accepted period, and control later corrections."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opening-and-closing"
updated: "2026-07-31"
---

Opening activities establish the first reliable ERPNext balances. Closing activities finalize the legacy period and prevent changes after reconciliation.

## Close the legacy system

Before extracting final balances:

1. Enter all approved transactions through the cutover date.
2. Reconcile bank and cash.
3. Complete stock count and valuation.
4. Post depreciation, payroll, tax, accruals, prepayments, and exchange adjustments.
5. Reconcile Customer and Supplier control accounts.
6. Run final Trial Balance and supporting schedules.
7. Lock the legacy period and restrict new entries.

Record late invoices or payments in a cutover log and decide which system will receive them.

## Open ERPNext

Use the opening tools in this order:

1. Chart of Accounts Importer
2. Opening Invoice Creation Tool
3. Opening payments and advances
4. Stock Reconciliation
5. Asset opening records
6. Opening Journal Entry for remaining balances

Run the Trial Balance after each stage so errors are isolated to the current batch.

## Opening Invoice Creation Tool

This tool creates outstanding Customer and Supplier invoices without historical Item detail. It is appropriate for opening ageing but not for historical sales analytics or stock.

## Chart of Accounts Importer

Use it before balances are loaded. Review account types and Company defaults after import.

## Period Closing Voucher

The Period Closing Voucher transfers the net balance of income and expense accounts to a closing account. It is not an opening-balance import tool.

Use it only when the ERPNext period itself needs to be closed. If ERPNext starts at the beginning of a new fiscal year, the legacy system may already contain the year-end closing.

## Freeze the accepted opening

After reconciliation and sign-off:

- save the approved reports;
- restrict the migration user;
- freeze accounts through the cutover date;
- create an Accounting Period if selected transactions must be blocked;
- document authorized correction procedures.

Do not freeze before reconciliation is complete because correction then requires privileged overrides.

## Reopen only with approval

If an accepted opening period must be corrected:

1. document the error and financial impact;
2. obtain finance approval;
3. temporarily permit the authorized role;
4. cancel and amend or post a referenced correction;
5. rerun all affected reconciliations;
6. restore the freeze;
7. update sign-off evidence.

## Related topics

- [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)
- [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher)
- [Accounting Period](https://docs.frappe.io/erpnext/accounting-period)
- [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings)

<!-- page: erpnext/erpnext__opening-balance.md -->
---
title: "Opening Balance in Accounts | ERPNext Documentation"
description: "Enter ERPNext opening accounting balances without double counting invoices, payments, stock, or assets, then reconcile the opening Trial Balance."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opening-balance"
updated: "2026-08-14"
---

Opening balances tell ERPNext where the company stands at the migration cut-off date. They should reproduce the verified closing position from the old system, not introduce new income or expense into the first reporting period.



If Nova Industries begins on 1 January, its bank, loans, fixed assets, inventory, equity, receivables, and payables must agree with the old books as of 31 December. Customer and supplier balances should be loaded through outstanding invoices where future settlement and ageing matter, while other ledger balances can be brought across through the appropriate opening tools.



This page explains the balance types, temporary opening account, posting approach, and checks needed to confirm that total debits equal total credits.

## Before entering balances

Complete the Chart of Accounts, company defaults, Fiscal Year, Cost Centers, parties, taxes, and opening document imports.

Obtain an approved Trial Balance and supporting schedules at the cutover date. The Trial Balance must balance before it is entered in ERPNext.

## Choose the correct import method


| Balance                           | Recommended method                                       |
| --------------------------------- | -------------------------------------------------------- |
| Outstanding Customer invoices     | Opening Invoice Creation Tool                            |
| Outstanding Supplier invoices     | Opening Invoice Creation Tool                            |
| Unallocated payments and advances | Opening Payment Entry or approved opening journal method |
| Stock quantity and value          | Stock Reconciliation with opening purpose                |
| Fixed assets                      | Asset opening records                                    |
| Other ledger balances             | Opening Journal Entry                                    |


Do not include a control-account balance in the Journal Entry if another opening document already creates it.

## Create the opening Journal Entry

1. Go to **Home &gt; Accounting &gt; General Ledger &gt; Journal Entry**.
2. Create a Journal Entry.
3. Select the Company and cutover date.
4. Set **Is Opening** to **Yes**.
5. Add one row for each residual ledger balance.
6. Enter debit or credit, not both, on each row.
7. Select party, Cost Center, Project, or Accounting Dimensions when required.
8. Add the source report and migration batch reference in **User Remark**.
9. Confirm total debit equals total credit.
10. Save, review, and submit after other opening documents are complete.

![Opening Journal Entry for a migration batch](/files/opening-journal-entry.webp)

## Use Temporary Opening

ERPNext uses a Temporary Opening account to balance opening entries while detailed balances are loaded. After all opening documents are posted, its balance should be zero unless the approved migration design explains a temporary difference.

Do not hide an unexplained difference in retained earnings, suspense, or rounding.

## Example

Assume balances not created by invoices, stock, assets, or payments are:


| Account           | Debit  | Credit |
| ----------------- | ------: | ------: |
| Prepaid Insurance | 12,000 |        |
| Security Deposit  | 5,000  |        |
| Accrued Expenses  |        | 7,000  |
| Retained Earnings |        | 10,000 |


The Journal Entry debits 17,000 and credits 17,000.

## Mid-year opening

If migrating mid-year, decide how year-to-date income and expense will appear. Importing balances into individual income and expense accounts preserves current-year Profit and Loss totals but does not reproduce transaction-level history.

Document the method and reconcile it to the source Profit and Loss Statement.

## Verify

After submission:

1. Run Trial Balance at the cutover date.
2. Compare every account with the approved source Trial Balance.
3. Run Balance Sheet and Profit and Loss Statement.
4. Verify party, bank, stock, and asset control accounts against their schedules.
5. Confirm Temporary Opening and migration-clearing accounts are zero.

## Correcting an opening balance

If the period is still open, cancel and amend the incorrect opening document or post an approved correcting opening entry. Keep the original and correction references in the migration log.

Do not edit submitted ledger rows or use reposting as a substitute for correcting the source document.

## Related topics

- [Opening Invoice Creation Tool](https://docs.frappe.io/erpnext/opening-invoice-creation-tool)
- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation)
- [Validate and Correct the Migration](https://docs.frappe.io/erpnext/validate-and-correct-the-migration)

<!-- page: erpnext/erpnext__opening-invoice-creation-tool.md -->
---
title: "Import Outstanding Invoices | ERPNext Documentation"
description: "Import outstanding Sales and Purchase Invoices into ERPNext with correct parties, dates, currencies, ageing, and reconciliation controls."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opening-invoice-creation-tool"
updated: "2026-08-14"
---

One total receivable balance is not enough to continue collections after migration. ERPNext needs each unpaid customer invoice, and each unpaid supplier invoice, when users must see due dates, ageing, references, and later allocate payments accurately.



At the cut-off date, Northstar Retail owes Nova Industries for three invoices with different dates and due amounts. The Opening Invoice Creation Tool brings those invoices across without recreating the historical sales and stock workflow that originally produced them.



This page shows how to prepare the invoice file, create opening receivables and payables, verify party balances and ageing, and correct rejected or duplicated rows before go-live.

## When to use it

Use this tool for unpaid or partly paid invoices that must appear in Accounts Receivable or Accounts Payable after cutover.

Do not use it for:

- fully paid invoices;
- quotations or orders;
- detailed historical sales analysis;
- stock movement;
- invoice rows that must preserve Item-level tax or revenue detail.

## Prepare the invoice file

Include:

- Customer or Supplier;
- invoice number;
- posting date;
- due date;
- invoice currency;
- exchange rate;
- outstanding amount;
- receivable or payable account;
- Cost Center where required;
- legacy reference.

The amount entered should be the amount still outstanding at cutover, not the original invoice total, unless the entire invoice remains unpaid.

## Reconcile the source file

Before import:

- total Customer rows by currency and compare with receivable ageing;
- total Supplier rows by currency and compare with payable ageing;
- separate debit and credit notes;
- remove zero-outstanding rows;
- confirm party names match ERPNext;
- confirm dates fall in a valid Fiscal Year;
- confirm accounts belong to the selected Company.

## Import invoices

1. Go to **Home &gt; Accounting &gt; Opening and Closing &gt; Opening Invoice Creation Tool**.
2. Select the Company.
3. Select **Sales** or **Purchase**.
4. Enable **Create Missing Party** only if the migration plan permits the tool to create basic parties. Importing reviewed Customer and Supplier masters first is safer.
5. Download the template or add rows in the Invoices table.
6. Upload the completed file.
7. review the preview and errors.
8. Start invoice creation.
9. Wait for background processing to finish.

![Opening Invoice Creation Tool](/files/opening-invoice-creation-tool7c01cb.webp)

Run Sales and Purchase imports as separate controlled batches.

## After import

Open representative invoices and confirm:

- party and party account;
- posting and due dates;
- currency and exchange rate;
- opening status;
- outstanding amount;
- legacy invoice number;
- Cost Center or dimensions where used.

Run Accounts Receivable and Accounts Payable at the cutover date. Compare party totals, invoice counts, currency totals, ageing buckets, and due dates with the source schedules.

## Partly paid invoices

Import only the outstanding portion. If the legacy system must preserve the original invoice and payment amounts for audit, record them in the migration workbook or custom reference fields.

## Credit notes

Prepare credit notes with the correct sign and party. Test one Sales credit and one Purchase credit before the full batch. Confirm they reduce the party’s outstanding balance.

## Foreign currency

Retain the invoice currency, outstanding foreign amount, exchange rate, and company-currency balance. After import, reconcile both currency values. Record any approved exchange difference separately.

## Avoid double counting

The tool creates receivable or payable ledger balances. Exclude the same control-account balance from the opening Journal Entry.

## Correcting failures

Download the failure log, correct the approved import file, and rerun only failed rows. If an invoice was created with the wrong amount or party, cancel and correct it before go-live.

## Related topics

- [Accounts Receivable](https://docs.frappe.io/erpnext/accounts-receivable)
- [Accounts Payable](https://docs.frappe.io/erpnext/accounts-payable)
- [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)
- [Payment Reconciliation](https://docs.frappe.io/erpnext/payment-reconciliation)

<!-- page: erpnext/erpnext__opening-stock-balance-entry-for-serialized-and-batch-item.md -->
---
title: "Opening Stock Balance Entry for Serialized and Batch Item\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item"
updated: "2026-03-02"
---


Items for which Serial No. and Batch No. is maintained, opening stock balance entry for them is update via Stock Entry. [Click here to learn how serialized inventory is managed in ERPNext](/erpnext/serial-no.html).

**Question:** Why Opening Balance entry for the Serialized and Batch Item cannot be updated via Stock Reconciliation?

In the ERPNext, stock level of a serialized item is derived based on the count of Serial Nos for that item. Hence, unless Serial Nos. are created for the serialized item, its stock level will not be updated. In the Stock Reconciliation Tool, you can only update opening quantity of an item, but not the Serial No. and Batch No.

### Opening Balance for the Serialized Item

Following are the steps to create opening stock balance entry for the Serialized and Batch item.

#### Step 1: New Stock Entry

`Stock > Stock Entry > New`

#### Step 2: Select Purpose

Stock Entry Purpose should be updated as `Material Receipt`.

#### Step 3: Update Posting Date

Posting Date should be date on which you wish to update opening balance for an item.

#### Step 4: Update Target Warehouse

Target Warehouse will be one in which opening balance of an item will be updated.

#### Step 5: Select Items

Select Items for which opening balance is to be updated.

#### Step 6: Update Opening Qty

For the serialized item, update quantity as many Serial Nos are their.

For the serialized item, mention Serial Nos. equivalent to it's Qty. Or if Serial Nos. are configured to be created based on Prefix, then no need to mention Serial Nos. manually. Click [here](/erpnext/serial-no-naming.html) to learn more about Serial No. naming.

For a batch item, provide Batch ID in which opening balance will be updated. Keep batch master ready, and updated it for the Batch Item. To create new Batch, go to:

`Stock > Setup > Batch > New`

[Click here to learn how Batchwise inventory is managed in ERPNext.](/erpnext/managing-batch-wise-inventory.html)

#### Step 7: Update Item Valuation Rate

Update valuation rate, which will be per unit value of item. If different units of the same items having different valuation rate, they should be updated in a separate row, with different Valuation Rates.

#### Step 8: Difference Account

As per perpetual inventory valuation system, accounting entry is created for every stock transaction. Double entry accounting system requires Total Debit matching with Total Credit in an entry. On the submission of Stock Entry, system debits Warehouse account by total value of items. To balance the same, we use Temporary Opening account as a Difference Account.

![Difference Account](/files/difference-account-1.png)

#### Step 9: Save and Submit Stock Entry

On submission of Stock Entry, stock ledger posting will be posted, and opening balance will be updated for the items on a given Posting Date.




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/nlHX0ZZ84Lw?start=120">
</iframe>

<!-- page: erpnext/erpnext__opening-stock.md -->
---
title: "Opening Stock"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opening-stock"
updated: "2026-03-06"
---

**Opening Stock is the amount and value of materials that a company has available for sale or use at the beginning of an accounting period.**

The closing Stock of the previous accounting period becomes the opening Stock of the current accounting period.

## 1. Prerequisites

- Create [Warehouses](/erpnext/warehouse).
- Link Warehouse to the appropriate accounting ledgers.

## 2. Opening Stock for Non-serialised Items

To post opening stock, visit the [Stock Reconciliation](/erpnext/stock-reconciliation) page.

## 3. Opening Stock for Serialised and Batched Items

Create the [Batch](/erpnext/batch) and [Serial No](/erpnext/serial-no) records beforehand. To post opening stock for serialised and batched items:

1. Go to **Stock > Stock Transactions > Stock Entry > New**.
2. Select 'Material Receipt' in 'Stock Entry Type'.
3. Set `Is Opening`as `Yes`.
4. Select the Warehouse in 'Default Target Warehouse'.
5. In the Items table, select Item Code, Qty and Basic rate.
6. For batched items, select Batch No.
7. For serialised items, select Serial No.
8. Save and Submit.



### 5. Related Topics

1. [Accounting Of Inventory Stock](/erpnext/accounting-of-inventory-stock)
2. [Stock Entry](/erpnext/stock-entry)
3. [Stock Reconciliation](/erpnext/stock-reconciliation)

<!-- page: erpnext/erpnext__operation.md -->
---
title: "Manufacturing Operation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/operation"
updated: "2026-07-05"
---

**An Operation refers to any manufacturing operation performed on the raw materials to process it further in the manufacturing path.**

The Operation master stores a single manufacturing operation, its description and the Default Workstation for the Operation. 

![](/files/CleanShot 2026-02-19 at 12.45.22@2x.png)

---

## Prerequisites

Before creating and using an Operation, it is advised that you create a [Workstation](https://docs.frappe.io/erpnext/user/manual/en/workstation) first.

---

## How to create an Operation

1. Go to the Operation list, click on New.
2. Enter a name for the Operation, for example, cutting.
3. Select the Default Workstation where the Operation will be performed. This will be fetched in BOMs and Work Orders.
4. Select a Quality Inspection Template for the operation in the Job Card section. It will be fetched on the Job Card for that particular operation when Work Order is created. When a new Quality Inspection is created from the Job card, then the same Quality Inspection Template is set for the Quality Inspection.
5. Optionally, add a description to describe what the Operation involves.
6. Save.

---

Once saved, the following can be created against an Operation:

![](/files/CleanShot 2026-02-19 at 12.17.04@2x.png)

<!-- page: erpnext/erpnext__opportunity.md -->
---
title: "Opportunity | ERPNext Documentation"
description: "Learn how to create, track, quote, and close sales Opportunities in ERPNext CRM."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opportunity"
updated: "2026-07-23"
---

**Opportunity is a qualified lead.**

When you get a hint that lead is looking for a product/service that you offer, you can convert that lead into an opportunity. You can also create an opportunity against an existing customer. Multiple Opportunities can be collected against a lead or a customer.

To access the Opportunity list, go to:

> Home > CRM > Sales Pipeline > Opportunity

## How to Create an Opportunity

- Go to the Opportunity list and select 'Add Opportunity'.
- In 'Opportunity From', select Lead if opportunity is from a lead.[Creating New Opportunity](/files/creating-opportunity.gif)
- You can also go to a Lead with 'Open' status and select “Opportunity” under **Create** dropdown as shown below.

[Create Opportunity From Lead](/files/lead-to-opportunity.png)

- In 'Opportunity From', select Customer if opportunity is from a customer.
- Select Opportunity Type. This indicates the broad category of opportunity like Sales, Support, Maintenance etc.
- You can add more details like Opportunity Amount, Probability (of conversion), Currency in 'SALES' section.
- You can capture the details of the products/services needed by clicking on 'With Items' checkbox and adding the item and quantity details in 'Items' section.

[Item Details in Opportunity](/files/item-details-in-opportunity.png)

- Enter the Source of the opportunity in the SOURCE section.

## Features

### Reminders to Follow Up on Opportunities

It is important to reach out to opportunities from time to time and build the relationship. You can set the 'Next Contact Date' and 'Next Contact By' fields and a calendar event will be added for the user chosen in 'Next Contact By' field and a notification is shown on the that Date.

### Auto-assign Opportunities to Sales Executives

> Introduced in Version 12

You can define [Assignment Rules](/erpnext/assignment-rule) to automatically assign the opportunities to sales executives.

![Opportunity Assignment](/files/opportunity-assignment-rule.png)

### Auto-close Opportunities

If you do not receive a response from an opportunity for a certain number of days, you may want that opportunity to be closed automatically.

You can set the number of days in [Selling Settings](/erpnext/selling-settings).

![Auto Close Opportunities](/files/auto-close-opportunities.png)

### Create a Quotation

You can create a [Quotation](/erpnext/quotation) from the **Make** dropdown. Relevant field values will be copied over.

![Create Quotation From Opportunity](/files/create-quotation-from-opportunity.png)

### Create a Supplier Quotation

You may need to get a quotation from your supplier against the customer requirement and based on that, prepare the quotation for your customer. With ERPNext, you can make a [Supplier Quotation](/erpnext/supplier-quotation) from the opportunity itself.

> Best Practice: Leads and Opportunities are often referred as your “Sales  
> Pipeline” this is what you need to track if you want to be able to predict how  
> much business you are going to get in the future. Its always a good idea to be  
> able to track what is coming in order to adjust your resources.

### 6 Capture the Reasons and Competitors for Lost Opportunities

When an opportunity is lost, you can capture the reasons, competitors and detail reason for losing. This will help you to analyse the trends over a long period of time and identify the insights needed for improvements at various areas in the organisation.

![Opportunity Lost Reason](/files/opportunity-lost-reason.png)

### Minutes to First Response

When you send the first reply(email) to an Opportunity, it calculates Mins to First Response and is displayed in a field.

A report is generated called 'Minutes to First Response for Opportunity'. Read [CRM Reports](/erpnext/crm_reports) for more details.

### Related Topics

- [Quotation](/erpnext/quotation.html)
- [Customer](/erpnext/customer)
- [Lead](/erpnext/lead)
- [Supplier Quotation](/erpnext/supplier-quotation)
- [Difference between Lead, Contact, and Customer](/erpnext/difference_between_lead_contact_and_customer)

<!-- page: erpnext/erpnext__opportunity_type.md -->
---
title: "Opportunity Type | ERPNext Documentation"
description: "Learn how to configure Opportunity Types in ERPNext and categorize sales opportunities consistently."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/opportunity_type"
updated: "2026-07-23"
---

**'Opportunity Type' indicates the broad category of opportunity like Sales, Support, Maintenance, Partnership etc.**

Adding the appropriate opportunity type helps in assigning the opportunity to the right sales executive and also categorise opportunities in different groups.

To access the Opportunity Type, go to:

> Home > CRM > Settings > Opportunity Type

## How to create an Opportunity Type

- Go to the Opportunity list and select New.
- Enter 'Name'.
- Enter 'Description' to elaborate more on the type.

![Screenshot 2023-12-28 at 11.14.56 AM](/files/Screenshot 2023-12-28 at 11.14.56 AM.png)

The system allows you to maintain a list of different Opportunity Types.

![Screenshot 2023-12-28 at 11.15.46 AM](/files/Screenshot 2023-12-28 at 11.15.46 AM.png)

<!-- page: erpnext/erpnext__packing-list.md -->
---
title: "Packing List | ERPNext Documentation"
description: "Learn how ERPNext Packing Lists expand Product Bundles into their component Items for accurate picking, packing, delivery, and shipment records."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/packing-list"
updated: "2026-07-25"
---

# Packing List

The **Packing List** in an ERPNext Sales Order shows the individual stock Items that must be delivered when the Customer orders a [Product Bundle](/erpnext/product-bundle). It converts the bundled parent Item into an exploded list of its components for stock fulfillment.

The Packing List appears only when the Sales Order contains a Product Bundle.

## Before you begin

Create the Product Bundle before creating the [Sales Order](/erpnext/sales-order). The bundle should have:

- a non-stock parent Item that appears on the Customer-facing order;
- the stock Items contained in the bundle;
- the required quantity of every component.

Maintain stock and Warehouse details for the component Items.

## Generate the Packing List

1. Create a Sales Order and select the Customer.
2. Add the Product Bundle's parent Item under **Items**.
3. Enter the ordered quantity and selling rate.
4. Select a **Delivery Warehouse** for the Product Bundle Item.
5. Save the Sales Order.
6. Open the **Packing List** section and review the generated component rows.

ERPNext generates the Packing List when the Sales Order is saved. It multiplies each component quantity by the ordered quantity of the Product Bundle.



![Packing List generated from a Product Bundle in a Sales Order.](/files/image33d548.png)

## Review Packing List fields


| Field         | What it means                                                           |
| ------------- | ----------------------------------------------------------------------- |
| Parent Item   | The Product Bundle Item entered in the Sales Order Items table.         |
| Item Code     | A stock Item contained in the Product Bundle.                           |
| Quantity      | The total component quantity required for the ordered bundles.          |
| Warehouse     | The Warehouse from which the component will be delivered.               |
| Serial Number | Identifies serialized units selected for the component when applicable. |
| Batch Number  | Identifies the batch selected for a batched component when applicable.  |


The Delivery Warehouse selected for the Product Bundle is copied to its Packing List rows. Components can use different Warehouses when required.

Select the **pencil icon** at the end of a Packing List row to open the full row editor and review fields that are not visible in the table.

## Deliver and invoice the order

Create a [Delivery Note](/erpnext/delivery-note) from the submitted Sales Order. ERPNext uses the Packing List components for stock movement while retaining the Product Bundle parent on the commercial transaction.

Create the [Sales Invoice](/erpnext/sales-invoice) from the Sales Order or Delivery Note according to your process. Review the selected print format to control whether the Customer sees the parent Item, components, or both.

## Troubleshooting

### The Packing List is empty

Confirm that the Item in the Sales Order is an active Product Bundle with valid component Items. If the bundle was created or changed later, remove and add the parent Item again on the draft Sales Order, then save it.

### A component uses the wrong Warehouse

Open the component row with the pencil icon and select the correct Warehouse. Confirm that sufficient stock exists there before delivery.

### A component is out of stock

Choose another Warehouse with suitable stock or complete the required procurement or manufacturing process before creating the Delivery Note.

## Frequently asked questions

### Does the Product Bundle parent Item create a stock movement?

The component Items in the Packing List drive the stock movement. The parent Item represents the bundle sold to the Customer.

### Can components come from different Warehouses?

Yes. Review and change the Warehouse on individual Packing List rows when the components will be fulfilled from different locations.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Product Bundle](/erpnext/product-bundle)
- [Delivery Note](/erpnext/delivery-note)
- [Warehouse](/erpnext/warehouse)

<!-- page: erpnext/erpnext__packing-slip.md -->
---
title: "Packing Slip\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/packing-slip"
updated: "2026-02-27"
---


**A packing slip is a document that lists the items in a shipment.**

It is usually attached to the goods delivered.

From a single Delivery Note, multiple Packing Slips can be created. It is useful when the shipment is packed in different boxes. Each box can have a weight and number of Items it contains. For example, if you're shipping 20 chairs in 4 boxes, each box can contain 5 chairs with different Packing Slips for each box.

To access the Packing Slip list, go to:
> Home > Stock > Tools > Packing Slip

> Note: In order to create Packing Slips from a Delivery Note, the Delivery Note needs to be in the Draft stage.

## 1. Prerequisites
Before creating and using a Packing Slip, it is advised that you create the following first:

* [Delivery Note](/erpnext/delivery-note)


## 2. How to create a new Packing Slip
Usually, you should create a Packing Slip from a Delivery Note when it is in the Draft stage, however, if you want to create a Packing Slip manually, follow these steps.

1. Go to the Packing Slip list, click on New.
1. Select the Delivery Note.
1. Enter the From Package No of this Packing Slip.
1. Click on the Get Items button to fetch the Items and Quantities into the Items table.
1. Save.

Most of these details will be fetched if you create the Packing Slip from the Delivery Note.

![Packing Slip](/files/packing-slip.png)


### 1.1 Additional options when creating a Packing Slip
**To Package No**: If there are multiple packages of the same type to be shipped at once then set the From and To Package numbers. For example, package numbers 1 to 5 in one Packing Slip, then package numbers 6 to 10 in the next Packing Slip and so on. This will be shown if you print then Packing Slip. Note that this will only work if you Shipment has that many quantities of the Items.

## 2. Features

### 2.1 Items table

* If this is a Batched Item, you'll have to select the Batch Number.
* The Quantity, UoM, Net Weight, and Weight UoM will be fetched from the Delivery Note.
* Page Break will create a page break just before this item when printing.

### 2.2 Package weight details

These details will be shown when printing the Packing Slip.

**Net Weight**: This is calculated as the sum of weights of all Items in the table.
**Gross Weight**: This is the final total weight including the weight of the packing materials used.
**Gross Weight UOM**: A UoM can be set here for the final weight of the product.

### 2.3 Letterhead
You can print your Packing Slip on your company's letterhead. Know more [here](/erpnext/letter-head).


### 2. Related Topics
1. [Quality Inspection](/erpnext/quality-inspection)
1. [Delivery Note](/erpnext/delivery-note)

<!-- page: erpnext/erpnext__partial-fulfilment-of-sales-order.md -->
---
title: "Partial Fulfilment of Sales Order | ERPNext Documentation"
description: "Learn how to partially deliver and invoice ERPNext Sales Orders using multiple documents, decimal quantities, returns, and mixed fulfilment."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/partial-fulfilment-of-sales-order"
updated: "2026-07-23"
---

A submitted [Sales Order](/erpnext/sales-order) does not need to be delivered or billed in one transaction. In ERPNext, you can fulfil selected Items and quantities through several [Delivery Notes](/erpnext/delivery-note), create several [Sales Invoices](/erpnext/sales-invoice), return delivered stock, and close a balance that the customer no longer wants.

ERPNext calculates the remaining quantity from the submitted documents linked to each Sales Order row. This preserves one confirmed order while giving the warehouse and billing teams the flexibility to work in stages.

![A partially fulfilled Sales Order for Northstar Retail, containing stock and drop-ship Items.](https://novacompanies.m.frappe.cloud/files/sales-order-overview-collapsed.png)

## Before you begin

You need:

- a submitted Sales Order with at least one outstanding Item quantity;
- permission to create and submit the required delivery, invoice, return, and purchasing documents;
- available stock in the selected [Warehouse](/erpnext/warehouse) for warehouse-fulfilled [Items](/erpnext/item); and
- a [Supplier](/erpnext/supplier) and purchasing setup for [drop-shipped Items](/erpnext/drop-shipping).

Confirm the customer's requested quantities and dates before creating downstream documents. You cannot reduce an order below quantities that are already delivered, billed, picked, or assigned to production.

## One Sales Order, multiple Delivery Notes

Use multiple Delivery Notes when Items ship in batches, on different dates, or from different warehouses.

1. Open the submitted Sales Order.
2. Select **Create > Delivery Note**.
3. In the new Delivery Note, keep only the lines being dispatched.
4. Enter the quantity being delivered for each retained line.
5. Confirm the source Warehouse, posting date, delivery address, and transporter details.
6. Save and submit the Delivery Note.
7. Repeat the process from the same Sales Order when the next batch is ready.

The mapped Delivery Note starts with quantities that remain deliverable. Before submission, remove lines that are not part of the current shipment and reduce a line's **Quantity** when only part of it is being delivered.

After each submission, ERPNext updates **% Delivered** on the Sales Order. The Sales Order remains **To Deliver and Bill** or **To Deliver** until its delivery requirement is complete.

## Deliver selected lines or quantities

Suppose an order contains 10 phones, 6 laptop docks, and 4 headphones, but the first shipment contains only 4 phones and 2 docks. Create a Delivery Note, remove the headphone row, and set the two retained quantities to 4 and 2.

The dot before an Item Code shows stock availability at a glance: green means the Item is in stock, while red means it is out of stock.

Select the **pencil icon** at the end of an Item row when the field you need—such as Warehouse, serial number details, or a row-level reference—is not shown as a table column.

Do not change the original ordered quantity merely to record a partial dispatch. The Sales Order should continue to show what the customer confirmed; the Delivery Note records what was dispatched now.

## One Sales Order, multiple Sales Invoices

You can split billing independently of physical delivery:

1. Open the submitted Sales Order.
2. Select **Create > Sales Invoice**.
3. Keep only the lines being billed.
4. Enter the quantity to invoice now.
5. Review taxes, payment terms, income accounts, and cost centers.
6. Save and submit the invoice.
7. Create another invoice from the same Sales Order for the next billing stage.

![A Sales Invoice billing selected lines and quantities from the Sales Order.](https://novacompanies.m.frappe.cloud/files/partial-sales-invoice.png)

ERPNext updates **% Billed** from submitted invoices. A direct invoice from the Sales Order does not create a stock movement unless **Update Stock** is enabled. When your process uses Delivery Notes, create the invoice from the relevant Delivery Note when you want its delivered quantities and references carried into billing.

Avoid billing the same quantity through two routes. Review the source references and remaining quantity before submitting each invoice.

## Partial fulfilment for services and projects

Service and project-based companies can represent one engagement with a single Sales Order line whose quantity is **1**, then use decimal quantities to record progress. For example, invoice **0.25** after completing 25% of the work, **0.35** at the next milestone, and the remaining **0.40** at completion. If your process records service delivery separately, use the same decimal quantities on Delivery Notes.

Use a decimal-friendly UOM and ensure **Must be Whole Number** is not enabled for that UOM. The Item should normally be configured as a non-stock service Item. Each submitted document updates the delivered or billed percentage against the same Sales Order, so the order remains the common reference for the full engagement.

Before using this method, define what each decimal represents in the contract—for example, accepted effort, a completed milestone, or a percentage of the total service. Use [Payment Terms](/erpnext/payment-terms) when the schedule is purely date- or milestone-based and does not need partial quantities.

## Review linked fulfilment documents

Open the **Connections** tab on the Sales Order to see the Delivery Notes, Sales Invoices, [Pick Lists](/erpnext/pick-list), and purchasing documents linked to it. This is the quickest way to confirm how many stages have been completed and open the underlying transactions.

![The Connections tab showing multiple Sales Invoices and Delivery Notes linked to one Sales Order.](https://novacompanies.m.frappe.cloud/files/linked-deliveries-and-invoices.png)

The Delivery Note count can include a return because a sales return is recorded as a return Delivery Note. Use the document list and its **Is Return** value to distinguish outbound deliveries from returned stock.

## Reduce an outstanding quantity

Use **Update Items** when the customer and seller agree to reduce the ordered quantity but want the Sales Order to remain the controlling document.

1. Open the submitted Sales Order.
2. Select **Update Items**.
3. Change the Item quantity to the revised total quantity—not the remaining quantity.
4. Review the revised totals and save the update.

For example, if 7 of 10 phones were delivered and the customer now wants only 8 in total, update the Sales Order quantity to 8. The outstanding delivery becomes 1. Do not enter 1 as the revised order quantity.

ERPNext prevents a reduction that conflicts with quantities already delivered, billed, picked, or produced. If the commercial value changes after an invoice was submitted, handle the financial adjustment with a [Credit Note](/erpnext/credit-note) instead of forcing the order below its billed quantity.

## Close the undelivered balance

Close the Sales Order when the customer no longer wants any outstanding quantity and you want to preserve the original order as submitted.

1. Confirm that no further Delivery Note or Sales Invoice should be created.
2. Open the Sales Order and select **Status > Close**.
3. Confirm the action.

The status becomes **Closed**, and ERPNext stops treating the remaining balance as work to be fulfilled. Closing does not cancel submitted Delivery Notes or Sales Invoices, return stock, or create a financial adjustment. Complete those actions separately when required.

Use **Update Items** when the agreed order itself changed and the revised total should be visible. Use **Close** when the original commitment should remain visible but its remainder will not be completed.

## Returns after partial or complete delivery

Create a [Sales Return](/erpnext/sales-return) against the Delivery Note that originally moved the stock:

1. Open the submitted Delivery Note.
2. Select **Create > Sales Return**.
3. Keep only the returned lines and enter the returned quantities.
4. Confirm the receiving Warehouse.
5. Save and submit the return.

The return Delivery Note uses negative quantities, adds accepted stock back to the Warehouse, and reduces the net delivered quantity against the Sales Order. A return can therefore make a previously completed delivery partially outstanding again.

For money already invoiced, create a Credit Note against the relevant Sales Invoice. The stock return and financial credit are related business actions, but they affect different ledgers.

## Mixed warehouse and drop-ship fulfilment

A Sales Order can contain some Items supplied from your Warehouse and other Items shipped directly by a Supplier.

- For warehouse lines, set the source Warehouse and create Delivery Notes as each batch leaves your premises.
- For drop-ship lines, mark the Item row for Supplier delivery and create the required [Purchase Order](/erpnext/purchase-order) for the selected Supplier.
- Keep the delivery address and Supplier instructions accurate because the goods bypass your Warehouse.
- Review each line's fulfilment route before creating documents; do not include a drop-ship line in a normal warehouse Delivery Note.

This mixed model is useful when Nova Electronics Trading ships accessories from stock but asks a distributor to send a tablet directly to the customer. The Sales Order remains the common commercial reference while the operational documents follow different routes.

## Status and progress


| Sales Order indicator   | What it means                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------- |
| **% Delivered**         | Net quantity delivered through submitted Delivery Notes, adjusted for submitted returns |
| **% Billed**            | Quantity or value billed through submitted Sales Invoices, adjusted by relevant credits |
| **To Deliver and Bill** | Both delivery and billing are incomplete                                                |
| **To Deliver**          | Billing is complete, but delivery remains                                               |
| **To Bill**             | Delivery is complete, but billing remains                                               |
| **Completed**           | Delivery and billing requirements are complete                                          |
| **Closed**              | The remaining balance was intentionally closed                                          |


## Troubleshooting


| Problem                                          | What to check                                                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| The mapped document includes unwanted Items      | Remove those rows before submission; do not set them to an arbitrary value                                   |
| The remaining quantity is not what you expect    | Check submitted Delivery Notes, returns, Sales Invoices, and cancelled documents in **Connections**          |
| ERPNext will not let you reduce the order        | The proposed total may be below a quantity already delivered, billed, picked, or produced                    |
| The Sales Order did not become Completed         | Check both **% Delivered** and **% Billed**; one side may still have a balance                               |
| A drop-ship Item appears in a warehouse shipment | Review the Item row's drop-ship setting, Supplier, and purchasing document                                   |
| A return changed the order back to To Deliver    | The return reduced net delivered quantity; close the balance or create a replacement delivery as appropriate |


## Frequently asked questions

### Can I invoice before delivering?

Yes. You can create a Sales Invoice directly from the Sales Order. Whether this is appropriate depends on your accounting policy and whether stock movement must be recorded separately.

### Can one invoice cover quantities from several Delivery Notes?

Yes, provided the invoice references the correct delivered quantities and does not exceed what remains billable. Review the linked source rows before submission.

### Should I cancel the Sales Order when only the balance is cancelled?

Usually no. Close the order or reduce its total quantity, depending on whether you need to preserve the original commitment. Cancel the Sales Order only when the whole transaction should be reversed and linked documents allow it.

### Does a return automatically create a refund?

No. A return Delivery Note reverses stock movement. Use a Credit Note and the appropriate payment process for the financial reversal.

### Can I reopen a closed Sales Order?

Use **Status > Re-open** when the option is available and your permissions allow it. Recheck the outstanding quantities before creating more documents.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Drop Shipping](/erpnext/drop-shipping)

<!-- page: erpnext/erpnext__party-specific-item.md -->
---
title: "Party Specific Item"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/party-specific-item"
updated: "2026-07-04"
---

Party Specific Item is used to restrict which items, item groups, or brands can be used for a particular party. A party can be a **Customer** or a **Supplier**. This is useful when a business wants certain customers or suppliers to transact only in an approved set of items.

## When To Use Party Specific Item

- Use it when a customer should only be allowed to buy selected items, item groups, or brands.
- Use it when a supplier should only be used for selected purchase items, item groups, or brands.
- Use it when different parties have different product restrictions because of contracts, territory rules, compliance, or commercial agreements.
- Use it to reduce mistakes while creating sales and purchase transactions.

## Where To Find It

Open the Awesomebar and search for **Party Specific Item**, or go to **Selling > Item and Pricing > Party Specific Item**. The list view shows all configured party-specific item rules.

## How It Works

A Party Specific Item rule combines two decisions:

- **Party:** Select whether the rule applies to a Customer or Supplier, then choose the specific party.
- **Restriction Basis:** Choose whether the restriction is based on Item, Item Group, or Brand.

After the rule is saved, ERPNext can use it to control which items are allowed for that party in relevant sales or purchase transactions.



![](/files/party specific item225519.webp)

## Creating A Rule

1. Click **Add Party Specific Item**.
2. Select the **Party Type**: Customer or Supplier.
3. Select the **Party Name**.
4. Choose **Restrict Items Based On**: Item, Item Group, or Brand.
5. Select the corresponding value in **Based On Value**.
6. Save the document.

![](/files/Party specific item 2.webp)





## Example

If **Mirae Fashion** is allowed to transact only in the item **Table**, create a Party Specific Item with:

- **Party Type:** Customer
- **Party Name:** Mirae Fashion
- **Restrict Items Based On:** Item
- **Based On Value:** Table

You can also create broader rules by selecting **Item Group** or **Brand** instead of a single item.

## Good Practices

- Use **Item** when the restriction is very specific.
- Use **Item Group** when the party is allowed to transact in a full product category.
- Use **Brand** when the restriction follows brand-level agreements.
- Keep the rules easy to audit by avoiding duplicate or overlapping restrictions for the same party.
- Test the rule in a sales or purchase transaction after saving it.

## Related Topics

- [Item](https://docs.frappe.io/erpnext/user/manual/en/item)
- [Customer](https://docs.frappe.io/erpnext/user/manual/en/customer)
- [Supplier](https://docs.frappe.io/erpnext/user/manual/en/supplier)
- [Item Group](https://docs.frappe.io/erpnext/user/manual/en/item-group)
- [Brand](https://docs.frappe.io/erpnext/user/manual/en/brand)

<!-- page: erpnext/erpnext__payment-entry-for-capital-account.md -->
---
title: "Payment Entry for Capital Account | ERPNext Documentation"
description: "Record owner or shareholder capital introduced into ERPNext bank or cash accounts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/payment-entry-for-capital-account"
updated: "2026-08-01"
---

Use an internal transfer or a suitable accounting entry when an owner or shareholder contributes capital. The correct method depends on whether the contributor is maintained as a party and how the equity account is configured.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Payment Entry for Capital Account

1. Confirm the equity or capital ledger with your accountant.
2. Create a Payment Entry when the transfer fits the supported party or internal-transfer flow.
3. Set the bank or cash account receiving the money and the capital account as the counterpart.
4. Enter the bank reference and posting date.
5. Submit and verify the General Ledger.

![Payment Entry for Capital Account in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-04-payment-entry-party-amount.png)

## Important fields and what they mean


| Field                 | What it controls                                |
| --------------------- | ----------------------------------------------- |
| Paid From             | Capital or source account.                      |
| Paid To               | Company bank or cash account receiving funds.   |
| Party                 | Shareholder or other supported party when used. |
| Amount                | Capital introduced.                             |
| Reference No and Date | Bank evidence for the contribution.             |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The shareholder or partner is not available as a party

Create the supported party master and confirm the user's permissions. Do not substitute a Supplier or Customer merely to make the transaction selectable.

### The contribution was posted as sales income

Use the correct equity or capital account. Owner contributions and withdrawals are financing transactions, not customer revenue or supplier expense.

### The Payment Entry does not balance

Check the bank or cash account, capital account, party type, amount, and currency. Obtain accounting advice before using a temporary receivable or payable account as a workaround.

## Frequently asked questions

### Is owner capital recorded with a Receive Payment Entry?

A cash contribution commonly debits bank and credits the appropriate capital or equity account. Configure the exact accounts according to the legal entity and accounting policy.

### How is an owner's withdrawal recorded?

Use an approved payment or Journal Entry against the owner's drawings or capital account. Do not record it as an operating expense unless it genuinely is one.

### Can capital contributions be allocated to invoices?

Capital is not normally a customer or supplier settlement. Keep it separate from receivable and payable allocations.

### Should every shareholder have a separate capital account?

Use the account structure required for ownership reporting and local compliance. Separate ledgers can improve traceability, but confirm the design with your accountant.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)
