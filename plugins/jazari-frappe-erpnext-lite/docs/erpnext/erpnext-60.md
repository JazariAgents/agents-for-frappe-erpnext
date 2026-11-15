<!-- Frappe documentation: erpnext, part 60 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__stock-reconciliation.md -->
---
title: "Stock Reconciliation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reconciliation"
updated: "2026-03-06"
---

**Stock Reconciliation is the process of counting and evaluating material/products, periodically at the year-end.**

This is done in order to:

- Keep the actual physical stock count and book stock count in sync
- Value the stock for the preparation of the accounting statements

The Stock Reconciliation feature in ERPNext is used for:

- Posting opening stock
- Reconciling the book and the actual stock

To access the Stock Reconciliation list, go to: > Home > Stock > Tools > Stock Reconciliation

### 1. Opening Stock

---

Using stock reconciliation, you can update the number of specific items in a warehouse as of a specific time. You can also add Items in the stock that have Serial Numbers or batch numbers.

1. Go to the Stock Reconciliation list, click on New.
2. Select the Purpose as 'Opening Stock'. You can edit the posting Date and Time.
3. Select Item Code, Warehouse, Quantity, and Valuation Rate. If there is a Serial / Batch No involved, add it.
4. If you want to auto-generate Serial No / Batch No. then keep those fields blank.
  For auto-generation of Serial No, you need to set "Serial Number Series" in the Item master. To auto-generate the batch number, enable the "Automatically Create New Batch" checkbox in the item master.
5. The Difference Account will be set as 'Temporary Opening'.
6. Save and Submit.

[Screenshot on the live page]

> Note: Maintain Stock option should be enabled in Item master for this to work.



## 2. Stock Reconciliation

---

Stock Reconciliation is the process of counting and evaluating stock-in-trade, periodically and at year-end, in order to value the total stock for preparing accounting statements. In this process, the actual physical stocks are checked and recorded in the system. The actual stocks and the stock in the system should be in agreement and accurate. If they are not, you can use the Stock Reconciliation tool to reconcile the stock balance and value with actuals.

To reconcile the stock:

1. Go to the Stock Reconciliation list, click on New
2. Select the Purpose as 'Stock Reconciliation'. You can edit the posting Date and Time.
3. Set Item Code, Warehouse.
4. The current Quantity and Valuation Rate will be fetched, and the quantity will be changed as required.
5. The expense account in the Difference Account will be set to 'Stock Adjustment' by default.
6. The Cost Centre default will be 'Main', change if needed.
7. Save and Submit.

[Screenshot on the live page]

## 3. Reconciliation Features

### 3.1 Upload Data Through Spreadsheet

If you have a lot of items, you can upload the details via a spreadsheet.

1. Download Template

Open a new Stock Reconciliation and click on the Download button to download the template in CSV format.

[Screenshot on the live page]

2. Enter Data in CSV Template.

The CSV format is case-sensitive. Do not edit the headers that are preset in the template. In the Item Code and Warehouse column, enter the exact Item Code and Warehouse as created in your ERPNext account. For quantity, enter the stock level you wish to set for that item in a specific warehouse.

[Screenshot on the live page: Stock Reconciliation]

3. Upload the CSV file with the data by clicking on the 'Upload' button.
4. Review, Save and Submit.
5. Check the Stock Ledger Report for the updated stock balance.

[Screenshot on the live page]

### 3.2 Get Stock Balance and Valuation as of Specific Date and Time

You can import the stock balance and valuation as of a specific date and time from a selected Warehouse by clicking on the **Items** button. You can update the Quantity and Valuation Rate as needed.

[Screenshot on the live page]

### 3.3 Using a barcode scanner to scan physical inventory

If you have configured barcodes for your items, you can use a barcode scanner to reconcile physical quantities. To do this, follow these steps:

1. Set default warehouse
2. Enable "Scan Mode" This will disable fetching existing quantity and let you add quantities by incrementally scanning items.
3. Click on the "Scan Barcode" field and use your barcode scanner to send input. The reconciliation items table will keep getting updated as you scan items. The following video demonstrates this process.

[Screenshot on the live page: Stock Reconciliation Scanning]

## 4. Serial and Batch Bundle

In version 15, the [serial and batch bundle](https://docs.erpnext.com/docs/user/manual/en/serial-and-batch-bundle) feature has introduced to make stock transactions against the serial no/batch items. For stock reconciliation, the user gets two options to make a serial and a batch bundle.

- **Use Serial / Batch Fields**

The user can use the old serial/batch fields to make a serial and batch bundle automatically. In this case user has to enable the checkbox "  
Use Serial No / Batch Fields" in the line item

[Screenshot on the live page: Screenshot 2024-05-31 at 10.07.33 AM]

## **5. Use Serial & Batch Bundle**

The user can use the Serial / Batch bundle to make stock reconciliation for serialised/batched items. Here, the user gets the option to either "**Reconcile All Serial Nos / Batches**" or "**Reconcile Selected Serial Nos / Batches**".

Reconcile Selected Serial Nos / Batches: The user needs to disable the "Reconcile All Serial Nos / Batches" checkbox and create a serial and batch bundle for specific serial numbers or batches. By doing this, the system will automatically create the Current Serial / Batch Bundle for the serial numbers or batches that have been selected by the user manually within the Serial and Batch Bundle.

For example, if the user has 10 batches and wants to change the valuation rate of only 2 batches, then the user should disable the "Reconcile All Serial Nos / Batches" checkbox and create the serial and batch bundle for those 2 batches with the new valuation rate.

### **Reconcile All Serial Nos / Batches**

The user needs to enable the checkbox "Reconcile All Serial Nos / Batches" and create a serial and batch bundle.

For example, if the user has 10 batches and wants to reconcile and keep only one batch. Using the stock reconciliation, the user will be able to consume 9 batches automatically and retain one batch. For that, the user has to enable the "Reconcile All Serial Nos / Batches" checkbox in the Stock Reconciliation Item, and then the system will automatically consume 9 batches and add one batch on submission of the stock reconciliation.

[Screenshot on the live page: Screenshot 2024-05-31 at 10.25.35 AM]

<!-- page: erpnext/erpnext__stock-reposting-settings.md -->
---
title: "Stock Reposting Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reposting-settings"
updated: "2026-05-15"
---

[Screenshot on the live page: Screenshot 2024-04-24 at 12.54.08 PM]



### **Limit timeslot for Stock Reposting**

If you want to run the reposting in a specific time then you can enable the checkbox "**Limit timeslot for Stock Reposting**". With this configuration you can avoid deadlock issues which occurs during the reposting.

### Limits don't apply on

If you want to run the reposting full day and not on a specific time, especially when you have weekly off then you can use this configuration.

### Use Item Based Reposting

This option is helpful when you want to speed up reposting. The system skips reposting for duplicate items and warehouses to improve speed.

### Do reposting for each Stock Transaction

The system creates a reposting record for backdated entries. This means that the system only generates a reposting record if a future transaction exists for the same item and warehouse. We have seen cases where system has not created reposting entry for backdated transaction because of concurrency issues. So to solve them added this option which won't check whether the future transaction exists for the same item and warehouse to make reporting record. This is also added for an audit purpose.

### **Notify Reposting Error to Role**

If reposting fails due to any issues, the system sends emails to the system managers. If you don't want to send failure emails to the system managers, you can configure a role, and the system will then send the email to the users assigned to that respective role.

### **Enable Parallel Reposting**

[Screenshot on the live page: Screenshot 2025 12 10 at 5.54.21 PM]

Allows the system to use multiple background workers to repost stock entries in parallel per item. This setting is effective only when Item-Based Reposting is enabled.

#### No of Parallel Reposting (Per Item)

Defines the number of parallel workers that can execute repost item valuation entries in parallel. Higher values may speed up reposting but can increase system load.



### **Note for usage**

Reposting is a tough computational problem to solve because it involves reposting 1000s may be 10,000s of entries depending on volume of transaction. Please use Reposting Wisely. It is recommended to limit back dated entries to not more than one month. Reposting entries with dates ranging more than one month may lead to failure in reposting for multiple reasons including but not limited to 

1. Reposting Time may be limited to prevent utilisation of resources during working hours, therefore the actual reposting may come up at a later date than when it was created, therefore leading to inconsistencies in the vouchers on the system
2. Reposting is limited to a timeout of 1500 seconds, which may be exceeded if the volume of reposting is too long

### **Issue for Legacy Serial Numbers**

For example

- Inward serial number ABC with a rate of 14,000
- Outward transaction for the same serial number with a valuation rate of 14,000 
- Inward the same serial number ABC again with a rate of 4,000 
- Outward transaction for the same serial number with a valuation rate of 4,000



At this point, the incoming rate stored in the serial number becomes 4,000.  If reposting is performed from the second transaction (outward), the valuation rate is calculated incorrectly  

- Inward serial number ABC with a rate of 14,000
- Outward transaction for the same serial number with a valuation rate of 4,000 (**Incorrect because fetched from Serial No document**)
- Inward the same serial number ABC with a rate of 4,000
- Outward transaction for the same serial number with a valuation rate of 4,000



The valuation rate in the second row should be 14,000, not 4,000.  This issue affects legacy serial numbers created before Version 15, when the Serial and Batch Bundle feature was not available.  

**Solution**  

Provided an option to fetch the incoming rate either from the last inward transaction during reposting. To enable this users needs to enable the checkbox "Do not fetch incoming rate from Serial No" in the Stock Reposting Settings

<!-- page: erpnext/erpnext__stock-reposting.md -->
---
title: "Stock Ledger Variance Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reposting"
updated: "2026-02-27"
---



[Screenshot on the live page: Screenshot 2025 12 30 at 12.48.14 PM]


The Stock Ledger Variance report in the ERPNext helps identify incorrect Stock Ledger Entries (SLEs) where the Running Available Stock and Stock Balance are inconsistent. These inconsistencies usually occur due to reposting issues, backdated entries, or data mismatches.

This report allows users to easily detect affected entries and correct them by creating reposting entries.


### Use this report to:


* Identify Stock Ledger Entries with incorrect running balances
* Detect stock quantity mismatches between calculated and stored values
* Repost affected entries to fix stock inconsistencies


### How to Use the Report


* Open the Stock Ledger Variance report.
* Apply filters like 
    Quantity (A - B) to find ledgers with incorrect balance qty
    Value (G - D) to find ledgers with incorrect balance value
    Valuation (I - K) to find ledgers with incorrect valuation rate



### Reposting Affected Entries

To fix the incorrect stock ledger entries:


* Select the rows that show inconsistencies.
* Click on Create Reposting Entries.
* The system will generate reposting entries for the selected records.
* Once reposting is completed, re-run the report to verify that the issue is resolved.

### Notes


* Reposting may take time depending on the number of affected entries.
* It is recommended to perform reposting during non-peak hours.
* Always verify stock balances after reposting.


### When to Use This Report


* After fixing reposting-related issues
* When negative stock errors appear unexpectedly
* After importing or creating backdated stock transactions
* During stock audit or reconciliation

<!-- page: erpnext/erpnext__stock-reservation-for-production-plan.md -->
---
title: "Stock Reservation for Production Plan"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reservation-for-production-plan"
updated: "2026-02-19"
---


> Note: This feature will be available in the ERPNext version 16
> 
> 

Stock reservation in a production plan is important because it ensures that the required raw materials and sub-assemblies are available to start the manufacturing process. It also ensures that the purchased raw materials against the production plan are used exclusively for the respective production plan.

## How it Works in ERPNext 

The user activity diagram for the production plan reservation is shown below.


[Screenshot on the live page]


The user must enable the checkbox "Enable Stock Reservation" in the stock settings to use this feature. After enabling it, the checkbox "Reserve Stock" will appear in the Production Plan.

If the 'Reserve Stock' checkbox is selected, the system will automatically create a stock reservation entry for the sub-assembly items and raw materials if the stock exists.

If stock does not exist for the sub-assemblies or raw materials, the user must create work orders for the sub-assemblies and raise material requests (purchase) for the raw materials. Once the raw materials are purchased through these material requests, they will be automatically reserved against the respective production plan.

The materials reserved against the production plan will then be used for the work orders linked to that specific production plan.

<!-- page: erpnext/erpnext__stock-reservation-for-work-order.md -->
---
title: "Stock Reservation for Work Order\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reservation-for-work-order"
updated: "2026-02-19"
---


> Note: This feature will be available in the ERPNext version 16
> 
> 

Stock reservation for a work order is essential as it ensures that materials are available, enabling the manufacturing process to begin and produce finished goods.

It also helps to improve inventory management and ensures timely fulfillment of customer orders.

## How it Works in ERPNext

The user must enable the checkbox "Enable Stock Reservation" in the stock settings to use this feature. After enabling it, the checkbox "Reserve Stock" will appear in the work order.

If the "Reserve Stock" checkbox is selected, the system will automatically create a stock reservation entry against the source warehouse for the available stock upon submission of the work order.


[Screenshot on the live page]

The reserved stock can only be used for the respective work order and cannot be used in any other transactions.

## Unreserve Stock

If the reserved stock needs to be assigned to another work order, unreserve it from the current work order and assign it to the work order that does not have stock reserved.

[Screenshot on the live page]


## Reservation for WIP

Once the user transfers the materials from the source warehouse to the WIP warehouse using a stock entry with the type "Material Transfer for Manufacture", the system unreserves the stock from the source warehouse and reserves it against the WIP warehouse.

## Finished Goods Reservation

If the sales order is linked to the work order, the system reserves the finished goods against the respective sales order upon completion of the work order.

<!-- page: erpnext/erpnext__stock-reservation.md -->
---
title: "Stock Reservation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-reservation"
updated: "2026-03-02"
---


> Introduced in Version 15
> 
> 

Stock reservation, also known as inventory reservation, refers to the practice of setting aside a specific quantity of stock or inventory for a particular purpose or customer.

### 1. Prerequisites

* Enable Stock Reservation in Stock Settings. [Screenshot on the live page: stock-settings]

### 2. Stock Reservation against Sales Order

* Create a Sales Order. [Screenshot on the live page: sales-order]
* Check the reserve stock for items you want to reserve. [Screenshot on the live page: sales-order-item]
* Click on **Stock Reservation**, then select **Reserve**. Choose the warehouse and quantity, then click on the **Reserve Stock** button. [Screenshot on the live page: sales-order-reserve]
* Stock reservation entries are created against the sales order items. [Screenshot on the live page: stock-reservation-entries]

### 3. Stock Reservation from Pick List

* Create a Sales Order.
* Create a Pick List for the Sales Order.
* In Pick List click on **Stock Reservation**, then select **Reserve**, the Stock Reservation Entries will be created against the Pick List. [Screenshot on the live page: sales-order-pick-list-reserve]

### 4. Auto Reserve Stock on Purchase

* Navigate to Stock Settings and enable **Auto Reserve Stock for Sales Order on Purchase**.
* Create a Sales Order.
* Create a Material Request from the Sales Order.
* Create Purchase Order from Material Request.
* Complete the process by creating a Purchase Receipt for the Purchase Order. The stock will be automatically reserved upon submission of the Purchase Receipt.

### 5. Stock Unreservation

There are two ways to unreserve the stock.

1. Stock Unreservation from Sales Order or Pick List:


	* Open a document and click on **Stock Reservation > Unreserve** button, the listed Stock Reservation Entries get cancelled. [Screenshot on the live page: sales-order-unreserve]
2. Unreserve the stock from the Stock Reservation Entry DocType:


	* 2.1 Open a Stock Reservation Entry and cancel it by clicking the **Cancel** button. [Screenshot on the live page: stock-reservation-entry-cancel]
	* 2.2 Go to the Stock Reservation Entry List, select the entries you wish to cancel, and then click on **Actions > Cancel**. [Screenshot on the live page: stock-reservation-entries-cancel]

### 6. Related Topics

1. [Sales Order](/erpnext/sales-order)
2. [Pick List](/erpnext/pick-list)

<!-- page: erpnext/erpnext__stock-settings.md -->
---
title: "Stock Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-settings"
updated: "2026-06-13"
---

You can set default settings for your stock-related transactions from the Stock Settings page...

### Item Naming By

---

[Screenshot on the live page: Stock Settings]



By default, the Item Name is set as per the Item Code entered. If you want Items to be named by a set [Naming Series,](/erpnext/naming-series) choose the 'Naming Series' option.

## Defaults

---

### Default Item Group

This will be the default item group allocated to a newly created item. Item groups are useful for classification and setting properties for the whole group. To know more visit the [Item Group](/erpnext/item-group) page.

### Default Stock UOM

The default unit of measure for stock is set as numbers (Nos), it can be changed from here.

### Default Warehouse

Set the default Warehouse from which the stock transactions are done. This will be fetched into the Default Warehouse in the Item master: 

[Screenshot on the live page: Stock Settings]



### Sample Retention Warehouse

This is the Warehouse where sample retentions are stored. To know more, visit [this page](/erpnext/retain-sample-stock).

### Default Valuation method

You can choose between FIFO (first in first out), LIFO (last in first out) or moving average valuation for your items. The default method is FIFO. If you select Moving Average or LIFO, new Items will be valuated on new method. You can change this when creating new Items in the Item form. Once the Item is saved, the Valuation Method cannot be changed. Read more [here](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average).

### Limit Percent

---

This is the percentage you are allowed to receive or deliver more against the quantity ordered. For example: If you have ordered 100 units, Supplier sends 120 units and the percentage is set to 10% then you are allowed to receive 110 units. By default, this is set to 0.

### Role Allowed to Over Deliver/Receive

---

Users with this role are allowed to over deliver/receive against orders above the allowance percentage

### Show Barcode Field

---

A field to enter Barcode details for an item. If unticked, the field won't be visible in the Item form.

### Convert Item Description to Clean HTML

---

Usually, descriptions are copy-pasted from a website or Word/PDF file and they contain a lot of embedded styles. This messes up the Print view of your invoices or quotes.

To fix this, you can check "Convert Item Description to Clean HTML" in Stock Settings. This will ensure that when you save the Items, their descriptions will be cleaned up.

If you want to control your description, views, and allow any HTML to be embedded, you can uncheck this property.

### Auto insert

---

[Screenshot on the live page: Stock Settings]



### Auto insert Price List rate if missing

Enabling this will insert an Item Price to the Price List of an Item automatically when using the Item in its first transaction. This price is fetched from the 'Rate' set in the first transaction with the Item. The Price List depends on whether you're using a Purchase or Sales transaction.

Note that, the Item Price will be automatically inserted only in the first transaction if not already present.

If this is unticked, the 'Standard Selling Rate' set in the Item when creating the Item will be added as Item Price.

### Automatically Set Serial Nos based on FIFO

Serial numbers for stock will be set automatically based on the Items entered based on first in first out. The Serial Numbers will be set automatically in transactions like Purchase/Sales Invoices, Delivery Notes, etc.

## Allow Negative Stock

---

This will allow stock items to be displayed in negative values. Using this option depends on your use case. For example, the stock transaction entries are entered at the weekend or month-end. In this case, negative stock needs to be enabled so that you can continue with your purchase/sales transaction entries.

Instead of enabling negative stock globally you can also enable it for specific items.

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15, users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

## Set Qty in Transactions based on Serial No Input

---

The quantity of items will be set according to the serial numbers. For example, if the user has added serial nos like A001, A002, and A003 then the system will set the quantity as 3 in the transaction.

## Automatic Material Request

---

[Screenshot on the live page: Stock Settings]



### Raise Material Request when the stock reaches re-order level

This option is useful if you want to ensure a constant supply of raw materials/products and avoid shortage. A [Material Request](/erpnext/material-request) will be raised automatically when stock reached the re-order level defined in the [Item form](/erpnext/item#34-automatic-reordering).

### Notify by Email on the creation of automatic Material Request

An email will be sent to notify the User with the role 'Purchase Manager' when an automatic Material Request is created.

## Inter Warehouse Transfer Settings

---

[Screenshot on the live page: Delivery Note Material Transfer]



### Enable customer warehouse for material transfer from Delivery Note and Sales Invoice

This option is useful when material transfer needs to be presented as a Delivery Note. For example, if there are statutory requirements where taxes are to be applied on each transfer of Material. It is easier to manage in a transaction like Delivery Note, than in the Stock Entry

### Enable supplier warehouse for material transfer from Purchase Receipt and Purchase Invoice

Similar to above option this option is useful when material transfer needs to be presented as Purchase Receipt.

To know more about inter warehouse material transfer via Delivery Note and Purchase Invoice please refer this article [Material Transfer From Delivery Note](/erpnext/material-transfer-from-delivery-note)

## Freeze Stock Entries

---

The User will not be allowed to make stock postings beyond this date.

[Screenshot on the live page: Stock Settings]



- **Stock Frozen Upto**: A threshold date till which stocks will be frozen.
- **Freeze Stocks Older Than [Days]**: Stocks older than x days will be frozen. This is calculated based on the creation date of the item.
- **Role Allowed to edit frozen stock**: The role you choose here will be allowed to edit frozen stock.

### Batch identification

---

Global setting for batches of stocks to be identified by a [Naming Series](/erpnext/naming-series). You can override this in the Item DocType.

## Allow to Edit Stock Quantity

---





Enable "Allow to Edit Stock UOM Qty for Sales Documents / Allow to Edit Stock UOM Qty for Purchase Documents" in the stock settings.

[Screenshot on the live page: stock_settings_edit_stock_qty]

## Allow to Edit Qty as per Stock UOM in Stock Entry

---

[Screenshot on the live page]



### **Why to Edit Stock Qty / Qty as Per Stock UOM**

If you're using multi-uom and your stock uom is a whole number, then you might face the issue that the Stock UOM should be non-decimal. Users experience this problem when they are unable to set an accurate conversion factor..

**Solution**

User will set the Stock Quantity and system will calculate the conversion factor

[Screenshot on the live page: stock_qty_editable]



### Allow UOM with Conversion Rate Defined in Item

---

If enabled, the system will allow selecting UOMs in sales and purchase transactions only if the conversion rate is set in the item master.

[Screenshot on the live page: UOM Restriction]

<!-- page: erpnext/erpnext__stock-transactions-landed-cost-voucher.md -->
---
title: "Landed Cost Voucher"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-transactions-landed-cost-voucher"
updated: "2026-07-04"
---

**Landed Cost is the final total cost associated with a product for it to reach the buyer’s doorstep.**

Landed costs include the original cost of the item, complete shipping costs, customs duties, taxes, insurance, currency conversion fees, etc. All of these components might not be applicable in every shipment, but relevant components must be considered as a part of the landed cost.

> **What is Landed Cost?**

> To understand landed cost better, let’s take an example based on our daily lives. You need to purchase a new washing machine for your home. Before making an actual purchase, you probably do some research to know the best price. In this process, you often found a better deal from a store which is long away from your home. But you should also consider shipping cost while buying from that store. Total cost including shipping might be more than the price you get in your nearby store. In that case, you will choose to buy from your nearest store, as the landed cost of the item is cheaper in the nearest store.

Similarly in business, identifying landed cost for an Item/product is very crucial, as it helps to decide selling cost of that item and impacts the company’s profitability. Hence all applicable landed cost charges should be included in Item’s valuation rate.

According to the [Third-Party Logistics Study](http://www.3plstudy.com/), only 45% of the respondents stated that they use Landed Cost extensively. The main reasons of not using Landed Cost were unavailability of necessary data (49%), lack of right tools (48%), insufficient time (31%), and not sure how to apply landed cost (27%).

To access the Landed Cost Voucher list, go to: > Home > Stock > Tools > Landed Cost Voucher

1. Prerequisites

---

Before creating and using Landed Cost Voucher, it is advised that you create the following first:

- A **Purchase Receipt** or **Purchase Invoice** with *Update Stock* enabled. This is your original receipt of goods.
- A **Purchase Invoice** for the landed costs (e.g. Freight, Insurance, etc.)

We will then use the **Landed Cost Voucher** to decrease the costs recorded through the second **Purchase Invoice** and increase the stock value. 

2. How to create a Landed Cost Voucher

---

1. Go to the Landed Cost Voucher list, click on New.
2. Select Receipt Document Type whether Purchase Invoice or Receipt. You can select multiple documents.
3. Select the specific Invoice or Receipt. The supplier name and Grand Total will be fetched automatically.
4. Click on the Get Items from Purchase Receipts button to fetch the item details from the Purchase Invoice/Receipt.
5. Select whether Distribute Charges Based On should be on quantity or Amount.
6. Enter the Expense Account and the Amount for Additional Costs in the Taxes and Charges table. The amount will be distributed equally based on the quantity or amount as per your selection.
7. Save and Submit.

[Screenshot on the live page: Landed Cost Voucher]

In the document, you can select multiple Purchase Receipts/Invoices and fetch all items from those Purchase Receipts. Then you should add applicable charges in “Taxes and Charges” table. You can easily delete an item if the added charges do not apply to that item.

The added charges are proportionately distributed among all the items based their amount or quantity. If you selected based on the amount, the Item with the highest amount will be allocated the highest proportion of the charges. In case of quantity, Item with the highest quantity will be allocated most of the charges and the other Items will be allocated lesser amounts. This is shown in the following screenshot:

[Screenshot on the live page: Landed Cost Voucher]



3. Related Actions

---

### 3.1 Adding Landed Cost in the Purchase Receipt itself

In ERPNext, you can add landed cost-related charges in “Taxes and Charges” table while creating Purchase Receipt (PR). You should add those charges for “Total and Valuation” or “Valuation” in the 'Consider Tax or Charge for' field. Charges which are payable to the same Supplier from whom you are buying the items should be tagged as “Total and Valuation”. Otherwise, if applicable charges are payable to a 3rd party, it should be tagged as “Valuation”. On submission of Purchase Receipt, the system will calculate the landed cost of all items, considering those charges. This landed cost will be considered to calculate the item’s Valuation Rate (based on FIFO / Moving Average method).

But in reality, while making Purchase Receipt we might not know all the charges which are applicable for landed cost. Your transporter can send the invoice after 1 month, but there is no point in waiting for booking Purchase Receipt till then. Companies that import their products/parts, pay a huge amount as Customs Duty. And generally, they get invoices from the Customs Department after a while. In these cases, “Landed Cost Voucher” becomes handy, as it allows you to add those additional charges on a later date, and to update landed cost of purchased items.

### 3.2 What happens on submission?

1. Valuation Rate of items is recalculated based on new landed cost.
2. If you are using “Perpetual Inventory”, the system will post general ledger entries to correct Stock-in-Hand balance. It will debit (increase) corresponding “warehouse account” and credit (decrease) **Expense Account** mentioned in Taxes and Charges table. If items are already delivered, the Cost-of-Goods-Sold (CoGS) value has been booked as per the old valuation rate. Hence, general ledger entries are reposted for all future outgoing entries of associated items, to correct CoGS value.

### 3.3 LCV for Stock Entry

From version 16 of ERPNext, users can create a Landed Cost Voucher against a Stock Entry with the purpose set to 'Manufacture'.  
This feature allows users to include additional costs—such as electricity charges or rent—into the final valuation rate of the manufactured product.

### 3.4 LCV for Subcontracting Receipt

From version 16 of ERPNext, users can create a Landed Cost Voucher against a Subcontracting Receipt items which has been manufactured by the subcontractor.

This feature allows users to include additional costs—such as freight charges, excise duty into the final valuation rate of the subcontracted product.

[Screenshot on the live page]

### 3.5 Vendor Invoices

You can link vendor invoices in the Landed Cost Voucher, and the system will ensure that the Landed Cost matches the total vendor invoice amount. Make sure the vendor invoices do not include any stock items.

[Screenshot on the live page]

### 4. Related Topics

1. [Delivery Trip](/erpnext/delivery-trip)
2. [Purchase Receipt](/erpnext/purchase-receipt)

<!-- page: erpnext/erpnext__stock-transactions.md -->
---
title: "Stock Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-transactions"
updated: "2026-02-26"
---

Stock transactions in ERPNext contains a wide range of activities related to managing inventory movements within an organisation. These transactions include stock transfers between warehouses, stock adjustments to correct inventory discrepancies, stock reconciliation to ensure accurate stock levels, and stock entries for recording stock movements such as purchases, sales, production, and consumption.

These transactions play a crucial role in maintaining accurate stock levels, tracking stock movements, analysing inventory performance, and making informed decisions related to procurement, sales, and production planning within the organisation.

- [Material Request](/erpnext/user/manual/en/material-request)
- [Auto Creation of Material Request](/erpnext/user/manual/en/auto-creation-of-material-request)
- [Opening stock](/erpnext/user/manual/en/opening-stock)
- [Stock Entry](/erpnext/user/manual/en/stock-entry)
- [Accounting of Inventory Stock](/erpnext/user/manual/en/accounting-of-inventory-stock)
- [Shipment](/erpnext/user/manual/en/shipment)
- [Delivery Note](/erpnext/user/manual/en/delivery-note)
- [Pick List](/erpnext/user/manual/en/pick-list)
- [Purchase Receipt](/erpnext/user/manual/en/purchase-receipt)
- [Delivery Trip](/erpnext/user/manual/en/delivery-trip)
- [Packing Slip](/erpnext/user/manual/en/packing-slip)
- [Putaway rule](/erpnext/user/manual/en/putaway-rule)
- [Stock Reconcilliation](/erpnext/user/manual/en/stock-reconciliation)
- [Stock Reservation](/erpnext/user/manual/en/stock-reservation)
- [Perpetual Inventory](/erpnext/user/manual/en/perpetual-inventory)
- [Landed Stock Voucher](/erpnext/user/manual/en/stock-transactions-landed-cost-voucher)

<!-- page: erpnext/erpnext__stock-transfer-with-gst.md -->
---
title: "Stock Transfer with GST"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-transfer-with-gst"
updated: "2026-07-31"
---

In certain situations, there are statutory requirements where taxes are to be applied on each transfer of Material. It is easier to manage it in a transaction like a Sales Invoice, than in the Stock Entry. Please follow the following steps to transfer material from one branch to another using Sales and Purchase Invoice

  


**Step 1 - Add default Unrealized Profit and loss account and default In-Transit warehouse in the company master** 

[Screenshot on the live page]

  


[Screenshot on the live page]

  


  


**Step 2 - Create Internal Customer and Supplier and allow them to transact with the same company. Also, link appropriate address and GST details with the respective parties**

  


[Screenshot on the live page]

  


  


[Screenshot on the live page]

  


**Step 3 - Create Sales Invoice (Delivering the items from source)**

  


3.1 Select the internal customer you created in your previous step

3.2 Check update stock

3.3 Add items to be transferred along with the Source Warehouse and Target Warehouse as the In-Transit warehouse

  


[Screenshot on the live page]

  


3.4 Save and Submit

  


Stock Ledger

[Screenshot on the live page]

  


Accounting Ledger

[Screenshot on the live page]

  


**Step 4 - Create Purchase Invoice (Receiving Items at destination)**

  


Use the "Create Internal Purchase Invoice" button from the sales invoice to create Purchase Invoice

  


[Screenshot on the live page]

  


Select the Accepted Warehouse (warehouse at which stock has been received) and save and submit

[Screenshot on the live page]

  


Stock Ledger

[Screenshot on the live page]

  


Accounting Ledger

[Screenshot on the live page]

  


**Note: Application of GST automatically on invoices is subjective to your GST configuration. Make sure you have proper tax templates configurated and appropriate addresses and GST details linked to the internal parties**

<!-- page: erpnext/erpnext__stock-value-account-value-comparison.md -->
---
title: "Stock Value and Account Value Comparison Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-value-account-value-comparison"
updated: "2026-02-27"
---

This report helps the user to understand the difference value between the stock account and stock balance report. At the end of the financial year, every organization has to match its closing stock balance with the closing stock account. Sometimes they do not match due to some issues. In that case, users can view the "Stock Value and Account Value Comparison" report to understand the incorrect transactions. Then, users can make adjustments entries accordingly.

To view the report, go to:

> Home > Stock > Other Reports > Stock and Account Value Comparison

[Screenshot on the live page: Stock Report]

<!-- page: erpnext/erpnext__stock.md -->
---
title: "Introduction to Stock Module"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock"
updated: "2026-03-06"
---

The Stock module in ERPNext is a comprehensive tool designed to manage inventory and streamline supply chain operations. It offers functionalities to handle various aspects of stock management as mentioned below.

1. **Inventory Tracking**: Monitor stock levels, track movements, and manage warehouses effectively.
2. **Item Management**: Define and categorise products, track item variants, and manage pricing.
3. **Stock Transactions**: Record and process transactions, including stock receipts, deliveries, and transfers.
4. **Stock Reconciliation**: Perform periodic audits to ensure stock records align with physical inventory.
5. **Reports and Analytics**: Generate detailed reports on stock levels, valuations, and trends to support decision-making.

Overall, the Stock module helps businesses maintain optimal inventory levels, reduce carrying costs, and improve operational efficiency.

## Video Tutorials

[Frappe School Course on Stock Module](https://frappe.school/courses/inventory-management)

<!-- page: erpnext/erpnext__stock__reports__negative-batch-report.md -->
---
title: "Negative Batch Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock/reports/negative-batch-report"
updated: "2026-02-27"
---

[Screenshot on the live page]

The **Negative Batch Report** is designed to identify and analyze transactions where batch stock has gone into negative quantity. This report helps users detect inconsistencies caused by backdated entries, incorrect stock movements, or improper batch usage, enabling timely corrections and accurate stock valuation.

### Purpose

The main purpose of this report is to:

- Identify batches with negative stock quantities
- Track transactions that caused negative stock
- Help users investigate and resolve stock inconsistencies
- Improve stock accuracy and valuation
- Assist in auditing batch-wise inventory movements

<!-- page: erpnext/erpnext__store-landing-page.md -->
---
title: "Store Landing Page\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/store-landing-page"
updated: "2026-03-02"
---


After enabling Shopping Cart for your app you can create a custom landing page for your
store using the [Web Page Builder](/erpnext/web-page-builder).

[Screenshot on the live page: Store Landing Page]
*Custom Store Landing Page*

## 1. How to create a Custom Store Landing Page

1. Follow the steps mentioned here to [create a Web Page](/erpnext/web-page).
1. Set a Route for your page (eg. */store*).
1. Select Content Type as **Page Builder**.
1. Click on Add Row in the Page Building Blocks Table.
1. Select a Web Template.

 ERPNext comes with a great set of standard web templates that can be used to create your Web Page.

 The configuration for the page in the screenshot above looks like this:

 [Screenshot on the live page: Store Web Templates]
 *Store Page Building Blocks*

1. Add Values.

 Click on the Edit Values button on the right of each block, and enter the values in the dialog to
 set the content for each section.

 The Web Templates that will be useful for building your store landing page are:

 - **Hero Slider:**
 Up to 5 slides can be created. The image, title, primary action, alignment, theme for each slide
 is configurable.
 [Screenshot on the live page: Store Hero Slider]
 *Hero Slider Configuration*

 - **Product Category Cards:**
 Up to 8 product category cards can be configured. Each product categories will link to an
 [Item Group](/erpnext/item-group).
 Ensure that the **Show in Website** option is ticked in the Item Group form so that the
 route for the product category is generated.

 [Screenshot on the live page: Store Product Category Cards]
 *Product Categories Configuration*

 - **Item Card Group:**
 This section can be used to showcase your featured items. Up to 12 cards can be configured.
 Each card will link to an [Item](/erpnext/item). If **featured** is checked,
 the item will take up 2 columns of space.

 [Screenshot on the live page: Store Item Card Group]
 *Item Cards Configuration*


1. Publish your Web Page.

 The web page will be published only when the Published option is checked.
 Once the page is published, click on **See on Website** on the sidebar or visit the configured route
 and check out the page!

 [Screenshot on the live page: Store Page Published]
 *Publish your Web Page*

1. Set as your Home Page.

 Follow the steps [here](/erpnext/website-home-page) to set
 this page as your Website home page.

<!-- page: erpnext/erpnext__stripe-integration.md -->
---
title: "Setting up Stripe"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stripe-integration"
updated: "2026-02-26"
---


To setup Stripe,
`Explore > Integrations > Stripe Settings`

#### Setup Stripe

To enable Stripe payment service, you need to configure parameters like Publishable Key, Secret Key
[Screenshot on the live page: Razorpay Settings]

On enabling service, the system will create Payment Gateway record and Account head in chart of account with account type as Bank.

[Screenshot on the live page: Stripe COA]

Also it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

[Screenshot on the live page: Payment Gateway Account]

After configuring Payment Gateway Account your system is able to accept online payments.

### Setup subscriptions plans

If you need to bill a recurring amount instead of a one-time charge, you can use Stripe's subscription system.

Once you have created your billing plans in Stripe, add one or several new "Payment Plan" in Frappe.

[Screenshot on the live page: Payment Plan]


Afterwards, when you create your payment request, click the check field "Is a subscription" and add the system will fetch the corresponding susbscription plans from within the corresponding subscription.

[Screenshot on the live page: Payment Request]

ERPNext will automatically create a new subscription for this customer in Stripe.


####Supporting transaction currencies
```
 "AED",
 "ALL",
 "ANG",
 "ARS",
 "AUD",
 "AWG",
 "BBD",
 "BDT",
 "BIF",
 "BMD",
 "BND",
 "BOB",
 "BRL",
 "BSD",
 "BWP",
 "BZD",
 "CAD",
 "CHF",
 "CLP",
 "CNY",
 "COP",
 "CRC",
 "CVE",
 "CZK",
 "DJF",
 "DKK",
 "DOP",
 "DZD",
 "EGP",
 "ETB",
 "EUR",
 "FJD",
 "FKP",
 "GBP",
 "GIP",
 "GMD",
 "GNF",
 "GTQ",
 "GYD",
 "HKD",
 "HNL",
 "HRK",
 "HTG",
 "HUF",
 "IDR",
 "ILS",
 "INR",
 "ISK",
 "JMD",
 "JPY",
 "KES",
 "KHR",
 "KMF",
 "KRW",
 "KYD",
 "KZT",
 "LAK",
 "LBP",
 "LKR",
 "LRD",
 "MAD",
 "MDL",
 "MNT",
 "MOP",
 "MRO",
 "MUR",
 "MVR",
 "MWK",
 "MXN",
 "MYR",
 "NAD",
 "NGN",
 "NIO",
 "NOK",
 "NPR",
 "NZD",
 "PAB",
 "PEN",
 "PGK",
 "PHP",
 "PKR",
 "PLN",
 "PYG",
 "QAR",
 "RUB",
 "SAR",
 "SBD",
 "SCR",
 "SEK",
 "SGD",
 "SHP",
 "SLL",
 "SOS",
 "STD",
 "SVC",
 "SZL",
 "THB",
 "TOP",
 "TTD",
 "TWD",
 "TZS",
 "UAH",
 "UGX",
 "USD",
 "UYU",
 "UZS",
 "VND",
 "VUV",
 "WST",
 "XAF",
 "XOF",
 "XPF",
 "YER",
 "ZAR"
```

<!-- page: erpnext/erpnext__subcontracting-in-erpnext.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subcontracting-in-erpnext"
updated: "2026-02-26"
---

## Subcontracting 

Subcontracting is a type of job contract that seeks to **outsource** certain types of work to other companies. It allows work on more than one phase of the project to be done at once, often leading to quicker completion. It is practiced by various industries.

For example, manufacturers who make a number of products from complex components subcontract certain components and package them at their facilities.



[Screenshot on the live page]



If your business involves outsourcing certain processes to a third party Supplier where you supply the raw materials and the third party does the labor/production, you can track this by using the [subcontracting feature](https://docs.frappe.io/erpnext/user/manual/en/subcontracting) of ERPNext. 

## Subcontracting Inward

ERPNext also supports **[Subcontracting Inward](https://docs.frappe.io/erpnext/user/manual/en/subcontracting-inward)**, where your company acts as the subcontractor. In this case, a customer provides materials to you for processing or manufacturing. ERPNext enables you to track customer-supplied materials, manage production activities, and bill for the services performed.
