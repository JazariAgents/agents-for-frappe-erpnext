<!-- Frappe documentation: erpnext, part 33 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__item.md -->
---
title: "Item"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item"
updated: "2026-03-12"
---

**An Item is a product or a service offered by your company.**

The term Item is also applicable to raw materials or components of products yet to be produced (before they can be sold to customers). ERPNext allows you to manage all sorts of items like raw-materials, sub-assemblies, finished goods, item variants, and service items.

ERPNext is optimized for itemized management of your sales and purchase. If you are in services, you can create an Item for each service that you offer. Completing the Item Master is very essential for the successful implementation of ERPNext.

To access the Item list, go to: > Home > Stock > Items and Pricing > Item

1. Prerequisites

---

Before creating and using an Item, it is advised that you create the following first:

- [Item Group](/erpnext/item-group)
- [Warehouse](/erpnext/warehouse)
- A Unit of Measure if required

2. How to create an Item

---

1. Go to the Item list, click on new.
2. Enter an Item Code, the name will be auto-filled the same as Item Code on clicking inside the Item Name field.
3. Select an Item Group.
4. Enter the opening stock units and standard selling rate.
5. Save

[Screenshot on the live page]

**2.1 Item Properties**

- **Item Name:** Item name is the actual name of your product or service.
- **Item Code:** Item Code is a short-form to denote your Item. If you have very few Items, it is advisable to keep the Item Name and the Item Code same. This helps new users to recognise and update Item details in all transactions. In case you have a lot of Items with long names and the list runs into hundreds, it is advisable to code. To understand naming Item codes, see [Item Codification](/erpnext/item-codification). You can also generate an Item Code based on a [Naming Series](/erpnext/naming-series) by enabling this feature in [Stock Settings](/erpnext/stock-settings#1-item-naming-by).
- **Item Group:** Item Group is used to categorise an Item under various criteria like products, raw materials, services, sub-assemblies, consumables or all Item groups. Create your default Item Group list under Setup > Item Group and pre-select the option while filling your New Item details under [Item Group](/erpnext/item-group). Item groups can be sub-assemblies, raw materials, etc, or based on your business use case.
- **Default Unit of Measure:** This is the default measuring unit that you will use for your product. It could be Nos, Kgs, Meters, etc. You can store all the UOMs that your product will require under Set Up> Master Data > UOM. These can be preselected while filling New Item by using % sign to get a pop up of the UOM list. Visit the [UoM](/erpnext/uom) page for more details

### 2.2 Options when creating an item

- **Disabled**: If you disable an Item, it cannot be selected in any transaction.
- **Allow Alternative Item**: Sometimes, when manufacturing a finished good, a specific material may not be available. If you tick this, you can create and select an alternative item from the Item Alternative list. To know more, visit the [Item Alternative](/erpnext/item-alternative) page.
- **Maintain Stock:** If you are maintaining stock of this Item in your Inventory, ERPNext will make a stock ledger entry for each transaction of this item. Ensure to keep this option unchecked when creating a non-stock Item (make to order/engineer) or a service.
- **Include Item in Manufacturing**: This is for raw material Items that'll be used to create finished goods. If the Item is an additional service like 'washing' that'll be used in the BOM, keep this unchecked.
- **Valuation Rate**: There are two options to maintain the valuation of the stock. FIFO (first in - first out) and Moving Average. To understand this topic in detail, please visit [Item Valuation, FIFO and Moving Average](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average).
- **Standard Selling Rate**: When *creating* an Item, entering a value for this field will automatically create an [Item Price](/erpnext/item-price) at the backend. Entering a value after the Item has been saved will not work. In this case, the Item Price is created from any transactions with the Item. The rate at which you'll sell the item. This will be fetched in Sales Orders and Sales Invoices.
- **Is Fixed Asset**: Tick this checkbox if this item is a company Asset. Check out the [Asset Module](/erpnext/asset) to know more.
- **Auto Create Assets on Purchase**: If Item is a Company Asset, tick this checkbox if you want to auto-create assets while purchasing this item through [Purchase Cycle](/erpnext/purchase-order). Check out the [Asset Page](/erpnext/asset) to know more.
- **Allowance Percentage**: This option will be available only when you create and save the item. This is the percent by which you will be allowed to over-bill or over-deliver this Item. If not set, it will select from [Stock Settings](/erpnext/stock-settings#3-limit-percent).
- **Uploading an Image**: To upload an image for your icon that will appear in all transactions, save the partially filled form. Only after your file is saved the 'Change' button will appear on the Image icon. Click on Change, then click on Upload, and upload the image.

For India:

- **HSN/SAC**: Harmonized System of Nomenclature (HSN) and Service Accounting Code (SAC) for GST. These numbers are defined by the government and different Items fall under different codes. New HSN codes can be added if not present in the list.
- **Is nil rated or exempted**: For an Item that is under GST, but no tax is applied to it. Eg: Cereals.
- **Is Non GST**: For an item that is not covered under GST. Eg: petrol.

---

### 3.1 Brand and Description

- **Brand**: If you have more than one brand, save them under Selling > Brand and pre-select them while filling a New Item.
- **Description**: Description of the item. The text from the Item Code will be fetched by default.

[Screenshot on the live page]

### 3.2 Barcodes

Barcodes can be recorded in Items to quickly scan and add them in transactions. In the Barcodes table, you can add an Item's [barcode for scanning](/erpnext/track-items-using-barcode). There are two types of barcodes in ERPNext:

- **EAN**: The European Article Number is a 13-digit number. EAN is used internationally and recognised by more POS systems.
- **UPC**: The Universal Product Code is a 12-digit number. UPC is generally used only in the USA and Canada.

### 3.3 Inventory

- **Shelf Life In Days**: This is for a product [Batch](/erpnext/batch). The number of days after which the product batch will be unusable. For example, medicines.
- **End of Life**: For a single item/product, the date after which it'll be completely unusable. That is, the item will be unusable in transactions and manufacturing. For example, you're using plastic crystals for manufacturing Items for the next 5 years, after which you want to use plastic beads.
- **Warranty**: To track a warranty period, it is necessary that the Item is serialised. When this Item is delivered, the delivery date and the expiry period is saved in the Serial Number master. Through the serial number master, you can track the warranty status.

A warranty period is a time period in which a purchased product may be returned or exchanged.

[Screenshot on the live page]

- **Weight UOM:** The Unit of Measure for the item. This can be Nos, Kilo, etc. The Weight UoM which you use internally can be different from the purchase UoM.
- **Weight Per Unit**: The actual weight per unit of the item. Eg: 1 kilo of biscuits or 10 biscuits per pack.
- **Default Material Request Type**: When you create a new Material Request for this item, the field set here will be selected by default in the new Material Request. This is also known as an 'indent'.
- **Valuation Method**: Select the Valuation Method, whether FIFO or Moving Average. Read [Item Valuation methods](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average) to know more.
- **Allow negative stock**: When checked, the item will be allowed to go negative even if negative stock is disabled from Stock Settings. This is useful if you don't want to enable negative stock on high-value items, but a few select low-value items are allowed to go negative for a few days.

### 3.4 Automatic Reordering

When the stock of an item dips under a certain quantity, you can set an automatic reorder under 'Auto Reorder' section. This should be enabled in [Stock Settings](/erpnext/stock-settings#9-automatic-material-request). This will raise a [Material Request](/erpnext/material-request) for the Item. The user with roles Purchase Manager and Stock Manager will be **notified** when the Material Request is created.

- **Check in (group)**: In which group of warehouses to check the quantity of the item?
- **Request for**: Which warehouse to stock the item reorder.
- **Re-order Level**: When this quantity is reached, the reorder will be triggered. The reorder level can be determined based on the lead time and the average daily consumption. For example, you can set the reorder level of Motherboard at 10. When only 10 Motherboards are remaining in stock, the system will either automatically create a Material Request in your ERPNext account.
- **Re-order Qty**: The number of units to be reordered so that the sum of ordering cost and holding cost is at its minimum. The re-order quantity is based on the 'Minimum Order Qty' specified by the supplier and many other factors.

For example, If reorder level is 100 items, your reorder quantity may not necessarily be 100 items. The Reorder quantity can be greater than or equal to the reorder level. It may depend upon lead time, discount, transportation and average daily consumption.

- **Material Request Type**: The [Material Request](/erpnext/material-request) type with which the stock will be reordered. This depends on whether you buy the Item, manufacture it yourself or transfer it between Warehouses.

[Screenshot on the live page]

> **Note**: The Material Request is created at 12 midnight depending on the set reorder level.

### 3.5 Multiple Units of Measure

You can add alternate UoMs for an Item. If the default UoM in which you sell is numbers (NoS) but you receive it in Kilos, you can set an additional UoM with an appropriate conversion factor. For example, 500 Nos of screws = 1 Kilogram, so select Kilogram/Litre as UOM and set the conversion factor as 500. To know more about selling in different UoM, visit [this page](/erpnext/Selling-in-different-UOM).

### 3.6 Serial Numbers

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

With Serial Numbers, you can track warranty and returns. In case any individual Item is recalled by the supplier, the number system helps track that Item. The numbering system also manages expiry dates.

Please note that if you sell your items in thousands and they are very small, such as pens or erasers, you do not need to serialise them.

In ERPNext, you will have to mention the Serial Number in some accounting entries. If your product is not a major consumer durable Item, has no warranty, and has no chance of being recalled, avoid providing serial numbers.

### 3.7 Batches

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

A set of Items can be manufactured in batches. This is useful for moving the batch and associating an expiry date with a certain batch.

- **Has Batch No**: Options for batch number, expiry date, and retaining sample stock will be revealed on ticking this checkbox. You cannot activate this if there is any pre-existing transaction for this item. If this is disabled, you'll have to enter the serial numbers manually for every transaction.
- **Batch Number Series**: Prefix that'll be applied to batch numbers. If you set 5x1SCR, then the first batch will be named like 5x1SCR00001 on the first transaction/manufacture.
- **Automatically Create New Batch**: If the batch number is not specified in transactions, it will be automatically created in a format like AAAA.00001. If you always want to manually create a batch number for this item, leave this field blank. This setting will override 'Naming Series Prefix' in Stock Settings. Batch numbers can be set to be generated automatically if you manufacture the items, or can be entered manually if they come from an external manufacturer.
- **Has Expiry Date**: If you tick this, the batch number will be created according to the expiry date. The expiry dates can be set in the 'Batch' master.
- **Retain Sample**: To retain a minimum number of sample stock of the item. You need to set a Sample Retention Warehouse in Stock Settings for this. To know more, [click here](/erpnext/retain-sample-stock).
- **Has Serial No**: This is similar to the Batch Number Series; it'll be created when you make transactions/manufacture. If you set Serial Number Series as AA, then on the first transaction, a serial number like AA00001 will be created.

> Tip: While entering an Item Code in an Items table, if the table requires inventory details, then depending on whether the entered item is batched or serialized, you can enter serial or batch numbers right away in a pop-up dialog.

[Screenshot on the live page]

> **Note**: Once you mark an item as serialized or batched or neither, you cannot change it after you have made a Stock Entry.

To know more, visit the [Stock Reconciliation](/erpnext/stock-reconciliation) page.

### 3.8 Variants

An Item Variant is a different version of an Item. To learn more about managing variants, see [Item Variants](/erpnext/item-variants).

### 3.9 Item Defaults

In this section, you can define Company-wide transaction-related defaults for this Item.

- **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions with this item.
- **Default Price List:** Whether Standard Selling or Standard Buying. Likewise, you can also set the purchasing and selling default accounts
- **Supplier**: If a default supplier is set, this supplier will be selected for new purchase transactions.
- **Default Expense Account:** It is the account in which cost of the Item will be debited.
- **Default Income Account:** It is the account in which income from selling the Item will be credited.
- **Default Cost Center:** It is used for tracking expense for this Item.

> Tip: You can add more rows for multiple companies.

[Screenshot on the live page]

### 3.10 Purchase, Replenishment Details

- **Default Purchase Unit of Measure**: The default UoM that will be used in Purchase transactions.
- **Minimum Order Qty**: The minimum quantity required for purchase transactions like Purchase Orders. If set, the system will not let you proceed with the purchase transaction if the item quantity in the purchase transaction is lesser than the quantity set in this field.
- **Safety Stock**: “Safety Stock” is used in the report “Itemwise Recommended Reorder Level”. Based on Safety Stock, average daily consumption and the lead time, the system suggests Reorder Level of an item.

Reorder Level = Safety Stock + (Average Daily Consumption * Lead Time)

- **Last Purchase Rate**: The rate at which you last purchased this item using a [Purchase Invoice](/erpnext/purchase-invoice) will be displayed here.
- **Is Purchase Item:** If unticked, you won't be able to use this item in purchase transactions.
- **Is Customer Provided Item:** Checked if Item is provided by a customer and received through **Stock Entry > Material Receipt**. If Checked, **Customer** field is Mandatory as the default customer for **Material Request**. To know more visit [this page](/erpnext/customer-provided-items).
- **Lead time days:** Lead time days are the number of days between ordering the Item and it to reach the Warehouse.

### 3.11 Supplier Details

- **Delivered by Supplier (Drop Ship)**: If the item is delivered directly by the supplier to the customer, tick this checkbox. Read more [here](/erpnext/drop-shipping-in-erpnext).
- **Supplier Codes:** Track Item Code defined by the Suppliers for this Item. In the Purchase transactions, on selecting an Item, a Supplier Part No. will be fetched as well for the Supplier's reference. You can read more about it [here](/erpnext/maintaining-suppliers-part-no-in-item).

[Screenshot on the live page]

[Screenshot on the live page]

### 3.12 Foreign Trade Details

If you're sourcing the item from another country, you can set the details here.

- **Country of Origin**: The country from which you're sourcing the item.
- **Customs Tariff Number**: You can create a customs tariff number with a description and use it for reference here to share with custom agencies. Later it can be used to add in Delivery Notes.

### 3.13 Sales Details

- **Grant Commission**: Grant a commission to [Sales Person](/erpnext/sales-person) and [Sales Partner](/erpnext/sales-partner) when this item is sold. If disabled, the sales generated by this item will be ignored in the calculation of commission.
- **Default Sales Unit of Measure**: The default UoM that'll be fetched for sales transactions.
- **Max Discount (%)**: You can define the maximum discount in % to be applied to an item. Eg: if you set 20%, you cannot sell this item with a discount greater than 20%.
- **Is Sales Item**: If unticked, you won't be able to use this item in sales transactions.

[Screenshot on the live page]

### 3.14 Deferred Revenue and Deferred Expense

You can enable deferred revenue or expense from the item. Once you tick the checkbox, you'll see options to set the Deferred Expense Account and the number of months through which the revenue/expense is deferred.

For example, consider a yearly gym membership, you pay the money upfront at once but the service is given throughout the year. For the gym owner, this is deferred revenue and for the customer, it is a deferred expense.

[Screenshot on the live page]

Check out the pages on [Deferred Revenue](/erpnext/deferred-revenue) for more details.

### 3.15 Customer Details

The Customer may identify an Item with a different Item Code. this is Similar to [Supplier Code](/erpnext/item#311-supplier-details).

- **Customer Name**: Select a customer here.
- **Customer Group**: This will be fetched based on the Customer you selected in the previous field.
- **Ref Code:** A customer can identify this item with a different number. You can track Item Code assigned by the Customer for this Item. When you create a Sales Order, the Customer's Reference Code for this Item will be shown.

### 3.16 Item Tax

These settings are required only if a particular Item has a different tax rate than the rate defined in the standard tax Account.

You need to create a new 'Item Tax Template' or choose an existing one. For example, if you have a tax Account, “VAT 14%” and this particular Item is exempted from tax, then you select “VAT 14%” in the first column, and set “0” as the tax rate in the second column. Visit the [Item Tax Template](/erpnext/item-tax-template) page for more details.

[Screenshot on the live page]

You can also set a [Tax Category](/erpnext/tax-category) for this Item.

### 3.17 Inspection Criteria

- **Inspection Required before Purchase**: If an inspection is mandatory before the item is purchased, i.e., before you generate Purchase Receipt, tick this checkbox.
- **Inspection Required before Delivery**: If an inspection is required at the time of delivery from your Supplier is mandatory for this Item, tick this checkbox. That is, before you generate a Delivery Note.
- **Quality Inspection Template**: If a Quality Inspection is prepared for this Item, then this template of criteria will automatically be updated in the Quality Inspection table of the Quality Inspection. Examples of Criteria are: Weight, Length, Finish, etc.

Quality Inspection can be done with Quick View and you need not go to a different page to update the details inspection in ERPNext.

Read [Quality Inspection](/erpnext/quality-inspection) to know more.

### 3.18 Manufacturing

- **Default BOM**: The default [Bill of Materials](/erpnext/bill-of-materials) used to manufacture this Item.
- **Supply Raw Materials for Purchase**: If you're subcontracting to a vendor, you can choose to provide them with the raw materials to manufacture the item using the default BOM.
- **Manufacturer:** Select the Manufacturer who manufactured this item.
- **Manufacturer Part Number:** Enter the manufacturer's assigned part number for this item.

[Screenshot on the live page]

### 3.19 Publishing Item on Website

> From Version 16 onwards, the Webshop app has been separated from the core ERPNext. To use the functionality of publishing items on a website generated from your ERPNext account, ensure that Frappe’s Webshop app is installed on the site.

**Show on Website**: Choose whether to show this Item on your website; click Action and choose "Publish in Website".

[Screenshot on the live page]

A new record called Website Item is created, containing additional details about the items, and is also published on the web view of the item.

[Screenshot on the live page]

The following fields will be found in the Website Item master.

*Weightage**: Items with higher weight will be displayed first on the website. The limit for the number you can enter here is very high.

- **Slideshow**: A slideshow can be displayed at the top of the page. Visit the [Homepage](/erpnext/homepage) page in the Website module to know more.
- **Image**: You can attach an image instead of a Slideshow.
- **Website Warehouse**: Select an existing warehouse or create a new one for transactions on your website. This Warehouse will be different from your offline Warehouses. Stock for any online transactions will be deducted from the Warehouse set under Website Warehouse.
- **Website Item Groups**: In this table, you can select existing or create new [Item Groups](/erpnext/item-group) to classify items on your website.
- **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/erpnext/web-page) to know how to add them.

Visit [Manufacturing](/erpnext/manufacturing) and [Website](/erpnext/website) to understand these topics in detail.

### 3.20 Website Specifications

This section is for configuring other details about the item.

- **Copy from Item Group:** The 'Website Specifications' details will be fetched as set in a specific Item Group chosen on the previous section (2.17).
- **Website Specifications**: Label and its description for the item. For example, 'Warranty: 1 year'.
- **Website Description**: This will appear on the item page.
- **Website Content**: (*Introduced in v12*) You can create additional styling, etc., use Bootstrap 4 markup to display on the item page.

### 3.21 Hub Publishing Details

The hub is a free online marketplace where Suppliers and Customers can transact. If both parties are on ERPNext, the transactions happen seamlessly. You can visit the hub at: [https://hubmarket.org](https://hubmarket.org).

- **Publish in Hub**: Choose if you want to publish your item on [https://hubmarket.org/](https://hubmarket.org/). It is a free marketplace. If your supplier/customer is also on ERPNext, the transactions will be seamless. For example, on creating a Purchase Order from your end, a Sales Order will be created on the Supplier's end.
- **Hub Warehouse**: This is a separate Warehouse to maintain the stock for your hub transactions.
- **Synced With Hub**: Sync item and other details with the hub when transactions take place.

4. Video

---

### 5. Related Topics

1. [Item Price](/erpnext/item-price)
2. [Item Codification](/erpnext/item-codification)
3. [Item Variants](/erpnext/item-variants)
4. [Item Group](/erpnext/item-group)
5. [Item Attribute](/erpnext/item-attribute)
6. [Item Valuation FIFO And Moving Average](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average)

<!-- page: erpnext/erpnext__item_group_wise_product_listing.md -->
---
title: "Item Group-wise Product Listing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item_group_wise_product_listing"
updated: "2026-03-02"
---

Similar to the [Product Listing](/erpnext/product-listing) at `/all-products`, ERPNext offers Product Listings that are Item Group-wise as well. You can link these pages on your landing page to direct users easily.

### Setting Up an Item Group Page
To provide a Product Listing page for an Item Group (e.g. Products), go to:

> Item Group List > Products

- Enable **Show in Website**.
- Scroll down to the **Website Filters** section and add field and attribute filters similar to E Commerce Settings.
- You can also add a description in the RichText Editor that will show above the product list as a banner.

Now if you click on the **See on Website** link, on the top left, above the image in the current document, you will be redirected to the **Products** Item Group's listing page.

#### Product Visibility
Consider the Item Group **Products** has child Item Groups **Mobile Services** and **Mobiles**. 

Website Items that will be visible on the **Products** page are:

- Those having **Products** as their Item Group
- Those having **Products** in their **Website Item Groups** table.

Website Items having their Item Groups as **Mobile Services** or **Mobiles** will be visible on their respective pages. These pages will be linked in the **Products** page.

> Child Item Groups such as **Mobile Services** and **Mobiles** will be visible as pills above the search bar on the **Producst** page.

[Screenshot on the live page: Item Group-wise Product Listing]

<!-- page: erpnext/erpnext__job-card-summary.md -->
---
title: "Job Card Summary\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card-summary"
updated: "2026-02-26"
---


To access the Job Card Summary, go to:

> Home > Manufacturing > Reports > Job Card Summary

[Screenshot on the live page: Task]

This report will give information about the Job Card as well as their status. Using this report users can check the month's Open and Completed Job Cards for the selected periods.

<!-- page: erpnext/erpnext__job-card.md -->
---
title: "Job Card\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card"
updated: "2026-05-20"
---

**A Job Card stores actual production information about a particular Operation performed on a particular Workstation.**

A Job Card is created from the Work Order and given to each of the Workstations in the manufacturing floor to start the production of an item with a certain quantity in each of the operations defined in the Work Order.

Job Card allows each Operation's workstation to issue a “Material Request” and “Stock Transfer to Manufacture” for raw material required against a “Job Card”.

Job Card completion will change the production status in Work Order, we can track the completion of production progress for each of the Operations defined in the Work Order.

[Screenshot on the live page: Work Order]

To access the Job Card list, go to:

> Home > Manufacturing > Production > Job Card

## 1. Prerequisites

Before creating and using a Job Card, it is advised that you create the following first:

- [Bill Of Materials](/erpnext/bill-of-materials)
- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)
- [Work Order](/erpnext/work-order)

## 2. How to Create a Job Card

Job Card for Operations is automatically created when a Work Order is submitted.

This is what a Job Card looks like:

[Screenshot on the live page: Job Card]

To use a Job Card follow these steps:

1. Click on the Start Job button, then on Complete Job when you're done.
2. Alternatively, you can also fill the From Time and To Time in the Time Logs table.
3. Select the Employee to whom the Job Card was assigned.
4. Enter the Completed Quantity. This is the number of Items on which the Operation was performed for the selected time interval.
5. Add more rows in the Time Logs table and record time using the Start/Completed buttons.
6. Click on Submit.

In a Work Order, the Operations and Workstations are fetched from the BOM of an Item. For ease of use, you should ensure that the [Routing](/erpnext/routing) is configured in the BOM.

Each Job Card created will have Workstation & Operations assigned. The raw material required from each Source Warehouse will be calculated based on quantity required for production.

On submitting a Work Order, Job Cards will be auto-created based on the values in the Operations table.

[Screenshot on the live page: Create Shareholder]

### 2.1 Select Work Order with Item to Manufacture

You can select 'Transfer Material Against' as 'Job Card' on the Bill of Materials to transfer raw materials for Production against Job Cards.

In the Work Order, you can select the option:

[Screenshot on the live page: Create Shareholder]

### 2.3 Using a Job Card

Employee assignment and timing detail will also be defined in Job Card. The time taken to do a job can be recorded. If multiple employees are working on the same Operation, add new job cards by clicking on the 'Create Job' Card button.

[Screenshot on the live page: Create Shareholder]

### 2.4 Material Request against Job Card

A Material Request will be raised from the Job Card as a basis/order to prepare raw material required for the manufacturing process. The Material Request raised will have its reference to the original Job Card number.

[Screenshot on the live page: Create Shareholder]

Track the Manufacturing Progress in The Work Order by The Completion of Each Operations defined in Work Order.

Job Card completion allows you to track the manufacturing progress inside the Work Order by looking at the completion of each Operation related to the Work Order.

[Screenshot on the live page: Work Order Job Card Completion]

### 2.5 Scrap Items

While completing the operations, there might be chances that some scrap materials will be produced. This scrap materials are required to be added in the inventory. For that user needs to put the details of the scrap items in the job card. User can also set the defective materials / broken materials in the scrap items table.

[Screenshot on the live page: Work Order Job Card Completion]

## 3. Features

### 3.1 Tracking Quality Inspection

> Introduced in Version 13

For production orders, the quality of in-process (semi-finished) goods also needs to be tracked. It is defined by the process (operation) performed on it which is in turn defined in the Job Card. In-process tests are different than incoming and outgoing material tests. Monitoring quality during manufacturing helps to make sure that the finished product produced is of the desired quality. You can create a Quality Inspection for the Production Item against the Job Card.

[Screenshot on the live page: Quality Inspection Against Job Card]

[Screenshot on the live page: Quality Inspection link in Job Card]

## **Pending Qty in Job Card**

A new **Pending Qty** field has been introduced in the **Job Card (in Version 16)** to handle partial production and prevent incorrect Process Loss calculation.



#### Problem

Previously, while completing a Job Card, the system automatically considered the **remaining quantity** as **Process Loss Qty**. This caused issues in cases where the operation was only partially completed, preventing users from submitting the Job Card.

#### Solution

To support partial completion, a **Pending Qty** field has been added to the Job Card.

- Users can now specify the quantity that is still pending for the operation. 
- The system will **not treat the remaining quantity as Process Loss** if a **Pending Qty** is specified. 
- **Process Loss Qty** will be calculated **only when the Pending Qty is zero**, indicating that the operation is fully completed.



#### Example

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **4**





In this case, the system will **not calculate Process Loss Qty**, as the remaining quantity is marked as pending.



If:

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **0**



Then the remaining quantity (**4**) will be treated as **Process Loss Qty**.



This enhancement allows users to perform **partial production tracking** without affecting Job Card submission.



[Screenshot on the live page]







For more details, refer the [Quality Inspection](/erpnext/quality-inspection) page.

<!-- page: erpnext/erpnext__journal-entry-template.md -->
---
title: "Journal Entry Template | ERPNext Documentation"
description: "Learn how to create and use Journal Entry Templates in ERPNext to preload recurring accounts, dimensions, entry settings, and other accounting details."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/journal-entry-template"
updated: "2026-08-03"
---

A Journal Entry Template stores the structure of a recurring [Journal Entry](https://docs.frappe.io/erpnext/journal-entry). It can prefill the company, entry type, naming series, opening-entry setting, multi-currency setting, and account rows. Use a template when the same accounts and dimensions recur, but the amount, date, reference, or remark changes each time.



For example, Nova Electronics Trading pays office maintenance from its operating bank account every month. A template can preload **Office Maintenance Expenses** and **Nova Operating Bank**, while the accountant enters the actual amount and reference for that month.

Templates reduce repetitive selection and help users choose the intended accounts consistently. They do not post to the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) by themselves. The resulting Journal Entry must still be reviewed, balanced, saved, and submitted.

## Before you begin

Confirm that:

1. The accounts exist in the company’s [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).
2. Each account is a ledger account, not a group account.
3. You know which account should be debited and which should be credited for the recurring transaction.
4. Any required [Cost Center](https://docs.frappe.io/erpnext/cost-center), [Project](https://docs.frappe.io/erpnext/project), or other [Accounting Dimension](https://docs.frappe.io/erpnext/accounting-dimensions) is available.
5. If the template uses accounts in different currencies, [multi-currency accounting](https://docs.frappe.io/erpnext/multi-currency-accounting) is configured.

## Create a Journal Entry Template

To open the list, search for **Journal Entry Template** from the Awesome Bar. Select **Add Journal Entry Template** or open an existing template.



[Screenshot on the live page: A Journal Entry Template list showing Monthly Office Maintenance highlighted]

Enter a clear **Template Title** that identifies the recurring purpose, such as `Monthly Office Maintenance`.

Select the **Journal Entry Type**, **Series**, and **Company**. Set **Is Opening** to **Yes** only when the resulting Journal Entry records an opening balance. Enable **Multi Currency** when the template uses an account whose currency differs from the company currency.



[Screenshot on the live page: Journal Entry Template fields for entry type, company, and naming series]

In **Accounting Entries**, add the accounts that should be copied to each Journal Entry. Do not enter transaction amounts in the template. Amounts belong to the actual Journal Entry because they can change for every occurrence.

Select the pencil icon to edit a row and add its Party, Cost Center, Project, or other dimensions when required.



[Screenshot on the live page: Accounting Entries with the row edit pencil highlighted]



[Screenshot on the live page: A Journal Entry Template account row editor with the Account field highlighted]

Save the template.

## Important fields and what they mean


| Field                | What it controls                                                                   | Guidance                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Template Title       | The name users select from a Journal Entry                                         | Use a purpose-based name, not a month or voucher number.                                                                |
| Journal Entry Type   | The intended kind of Journal Entry                                                 | Choose the type that matches the transaction. It can also influence defaults such as bank or cash behavior.             |
| Series               | The naming series copied to the new Journal Entry                                  | Use the company’s approved Journal Entry series.                                                                        |
| Company              | The company copied to the new Journal Entry                                        | Accounts in the template must belong to this company.                                                                   |
| Is Opening           | Marks the resulting entry as an opening entry                                      | Use this only for migration or opening balances. See [Opening Balance](https://docs.frappe.io/erpnext/opening-balance). |
| Multi Currency       | Allows accounts in currencies other than the company currency                      | Review exchange rates and account currencies in the resulting entry.                                                    |
| Account              | A ledger account copied into the Journal Entry                                     | Add at least two accounts so the resulting entry can be balanced.                                                       |
| Party Type and Party | Associates the row with a Customer, Supplier, Employee, or another supported party | Set these only when the selected account requires party-wise accounting.                                                |
| Cost Center          | Tracks income or expense by business unit                                          | Set a default here only if it applies to every entry created from the template.                                         |
| Project              | Tracks the row against a project                                                   | Leave it blank when the project changes each time.                                                                      |


## Choose the right entry type

The template supports the Journal Entry types available in the current ERPNext version, including Journal Entry, Inter Company Journal Entry, Bank Entry, Cash Entry, Credit Card Entry, Debit Note, Credit Note, Contra Entry, Write Off Entry, Opening Entry, Depreciation Entry, and Exchange Rate Revaluation.

The most commonly used choices are:


| Entry type                  | When it is useful                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journal Entry               | General adjustments and recurring accruals where a more specific transaction is not available.                                                        |
| Bank Entry                  | A journal-based bank transaction. For routine customer and supplier payments, prefer a [Payment Entry](https://docs.frappe.io/erpnext/payment-entry). |
| Cash Entry                  | A journal-based cash transaction.                                                                                                                     |
| Opening Entry               | Opening balances during setup or migration. ERPNext marks **Is Opening** accordingly.                                                                 |
| Inter Company Journal Entry | Adjustments between companies. See [Inter Company Journal Entry](https://docs.frappe.io/erpnext/inter-company-journal-entry).                         |
| Exchange Rate Revaluation   | Adjustments arising from currency revaluation.                                                                                                        |


Selecting Bank Entry or Cash Entry on a normal Journal Entry can load the company’s default bank or cash account when the account table is still empty. A template can also store the intended account rows directly. Opening Entry identifies the voucher as an opening transaction, but it does not automatically add the entire Chart of Accounts. Add only the accounts needed for the opening entry.

## Create a Journal Entry from the template

1. Create a new Journal Entry.
2. Open the **More Info** tab.
3. Expand **Additional Info**.
4. Select the template in **From Template**.

[Screenshot on the live page: The From Template field highlighted in a new Journal Entry]



[Screenshot on the live page: Monthly Office Maintenance entered in the From Template field]

ERPNext copies the template’s company, entry type, naming series, opening setting, multi-currency setting, and account rows into the new Journal Entry.



[Screenshot on the live page: A new Journal Entry with the template fields and account rows loaded]

Enter the debit and credit amounts, posting date, reference details, and remarks. Add or remove account rows if this occurrence needs them. Confirm that total debit equals total credit, then save and submit the Journal Entry.

## Important warning when selecting a template

Selecting **From Template** clears the existing **Accounting Entries** rows before loading the template’s rows. Choose the template before entering account rows, or copy any work you need to retain.

The template is a starting structure, not a lock. After it loads, you can add more accounts or change copied values before saving. Review every resulting Journal Entry because the template does not validate whether the accounts and dimensions remain appropriate for that month’s transaction.

## Maintain templates safely

Update a template when the recurring accounting treatment changes for future entries. Previously submitted Journal Entries are not changed when a template is edited.

Avoid creating several templates with nearly identical names. Use titles that describe the business event, such as `Monthly Office Maintenance`, `Payroll Accrual`, or `Bank Charges`. Keep one approved template for each recurring pattern and review it when the Chart of Accounts or dimension structure changes.

## Troubleshooting

### The From Template field is not visible

In a new Journal Entry, open **More Info** and expand **Additional Info**. The top-right **Templates** button is the general Frappe form-template feature. It is different from the ERPNext **Journal Entry Template** selected in the **From Template** field.

### The template does not appear in search

Confirm that the Journal Entry Template is saved and that you have permission to read it. Also confirm that the template’s company and accounts are available to your user.

### Existing account rows disappeared

This is expected when **From Template** is selected. ERPNext clears the current Accounting Entries before copying the template’s rows. Select the template first, then add occurrence-specific rows.

### An account cannot be selected

Confirm that it is a non-group ledger account belonging to the template’s company. Also check account currency restrictions when **Multi Currency** is not enabled.

### The Journal Entry is not balanced

The template copies account structure, not debit and credit amounts. Enter the amount on each row and ensure total debit equals total credit before saving.

## FAQs

### Does a Journal Entry Template create or submit entries automatically?

No, It only prefills a new Journal Entry. A user must add the current amounts and references, review the entry, and submit it.

### Can I change the accounts after loading a template?

Yes, You can edit, add, or remove rows before saving the Journal Entry. Treat the template as a reusable starting point.

### Can one template be used for several companies?

No, A template stores one company, and its accounts belong to that company. Create a separate template for each company when the same accounting pattern is needed.

### Should I store amounts in the template?

No, Journal Entry Template account rows define accounts, parties, and dimensions. Enter debit and credit amounts in each actual Journal Entry.

### Can a template include Cost Center or Project?

Yes, Add the dimension on the account row when it should apply every time. Leave it blank when the dimension changes for each transaction.

### Does editing a template update past Journal Entries?

No, Changes affect only entries created from the template after the change. Existing drafts and submitted entries retain their own values.

## Related topics

- [Finance Book](https://docs.frappe.io/erpnext/finance-book)
- [Immutable Ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext)
- [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger)
