<!-- Frappe documentation: erpnext, part 23 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__domain-settings.md -->
---
title: "Domain Settings | ERPNext Documentation"
description: "Use ERPNext Domain Settings to keep relevant business domains active and understand how domains differ from modules, workspaces, and permissions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/domain-settings"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. Its employees sell devices, manage warehouses, assemble selected products, and maintain equipment. They do not run a school or a healthcare facility. If every industry-specific feature is shown, a warehouse user may waste time searching through Student, Patient, or other records that have nothing to do with the job.



Domain Settings lets the administrator keep only the relevant business domains active across the site. This makes navigation and available business features easier to understand. It is not a security boundary: roles, permissions, User Permissions, and Workspace rules must still control who may read or change data.

## Select active domains

Open **Domain Settings**, review the domains available from the installed apps, and select only the domains the organisation genuinely uses. Nova keeps manufacturing and distribution-related functionality available while leaving unrelated industry domains inactive.

![Active Domains area in ERPNext Domain Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-domain-settings.png)


| Setting        | What it means                         | Nova example                                                                                               |
| -------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Active Domains | Business domains enabled for the site | Nova enables a relevant manufacturing domain but does not enable Education merely to explore its DocTypes. |


After saving, reload Desk and verify the affected workspaces, DocTypes, and navigation. Also test with a normal user's roles. A domain can make a feature available, while permission still decides whether the user can access it.

## Domain Settings versus nearby controls


| Control                    | Use it for                                                                        | Do not use it for                    |
| -------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| Domain Settings            | Activating an installed business domain                                           | Restricting one user's data          |
| Module Settings            | Changing process behaviour within a module                                        | Hiding data from unauthorised users  |
| Roles and Role Permissions | Granting DocType actions                                                          | Selecting which industry is relevant |
| User Permissions           | Restricting particular Companies, territories, customers, or other linked records | Enabling an installed domain         |
| Workspace configuration    | Controlling navigation and cards                                                  | Replacing server-side permissions    |


## Troubleshooting

### A DocType disappeared after changing domains

Re-enable the required domain and reload Desk. Then verify that the app remains installed and the user has the required role.

### A user can access a record even though its workspace is hidden

Navigation visibility is not permission. Review Role Permissions and User Permissions for the DocType and record.

### A domain is not available to select

Confirm that the app supplying it is installed and compatible with the current version. Domain Settings cannot activate code that is not installed.

## Frequently asked questions

### Should every available domain be enabled?

Enable only the domains the organisation uses. Extra domains add navigation and records that can confuse users.

### Does disabling a domain delete data?

Do not treat domain selection as deletion. Existing records may remain in the database even when the related interface becomes unavailable. Re-enable the domain and verify before making structural changes.

### Can one user have a different domain?

Domain Settings is site-wide. Use roles, permissions, and workspace configuration for user-specific access and navigation.

### Is a domain the same as a module?

A domain represents a business context that can activate related functionality. A module groups application features. They overlap, but they are not interchangeable.

## Related topics

- [Module Settings](/erpnext/module-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [User Permissions](/erpnext/user-permissions)
- [Workspace](/erpnext/workspace)
- [System Settings](/erpnext/system-settings)
- [Adding Users](/erpnext/adding-users)

<!-- page: erpnext/erpnext__download-backup.md -->
---
title: "Downloading Backups"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/download-backup"
updated: "2026-02-26"
---

In ERPNext, you can manually download a database backup.

To get the latest database backup, go to:

> Home  > Download Backups

Backup available for the download is updated every eight hours. Click on the link to download the backup at a given time.

If you want to set the number of Backups available for download at a time, then click on 'Set Number of Backups', which will navigate you to 'System Settings', where you can set the number.

![](/files/imageb48716.png)
*Download backup post backup taken*

![](/files/imageef9524.png)

## Downloading Files Backup

Clicking on Download Files Backup will send an email with links to the backup for both private and public files. Email must be configured for this to work.

![](/files/image0646b1.png)

## Getting Backup Encryption Key

In order to get the backup encryption key, click on the designated button. Upon getting your system password validated, the system will provide you with the encryption key.

![](/files/imageed3623.png)

## Automating Backups to Cloud Storage

You can also automate your backups to be uploaded directly to a cloud storage platform. Currently, ERPNext supports:

1. Amazon S3
2. Dropbox
3. Google Drive

<!-- page: erpnext/erpnext__downtime-analysis.md -->
---
title: "Downtime Analysis\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/downtime-analysis"
updated: "2026-03-02"
---


To access the Downtime Analysis report, go to:

> Home > Manufacturing > Reports > Downtime Analysis

![Task](/files/downtime-analysis.png)

This report will give information about the captured Machines Downtime in hours. Using Downtime analysis report, operators will know which machine was not performing well and needs maintenance.

<!-- page: erpnext/erpnext__downtime-entry.md -->
---
title: "Downtime Entry\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/downtime-entry"
updated: "2026-02-26"
---


To access the Downtime Entry, go to:

> Home > Manufacturing > Production > Downtime Entry

![Production Forecasting](/files/downtime-entry.png)

Downtime Entry document is used to capture the machine's Downtime in minutes. User needs to manually create the downtime record by selecting the proper machine alongwith the machine's down time. Using Downtime entry data operator knows which machine not performing well and needs maintenance.

<!-- page: erpnext/erpnext__drop-shipping-in-erpnext.md -->
---
title: "Drop Ship | ERPNext Documentation"
description: "Set up drop shipping in ERPNext so suppliers deliver items directly to customers through linked Sales Orders and Purchase Orders."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/drop-shipping-in-erpnext"
updated: "2026-07-23"
---

Drop shipping lets a Supplier deliver an item directly to your Customer. Your company creates the Sales Order and Purchase Order, but the goods do not pass through your warehouse. ERPNext links the two transactions so purchasing and sales teams can follow the same fulfilment.

![Drop-ship Sales Order with the customer, delivery date, supplier-delivered items, quantities, rates, and stock indicators.](/files/drop-ship-sales-order76e80b.webp)

## Before you begin

Create the [Customer](/erpnext/customer), Supplier, [Item](/erpnext/item), selling and buying prices, Customer shipping address, and Supplier contact details. The Item must have a Default Supplier or an appropriate supplier must be selected during purchasing.

## Create a drop-ship Sales Order

1. Go to **Selling > Sales > Sales Order** and select **Add Sales Order**.
2. Select the Customer, Company, and delivery date.
3. Add the Item and Quantity.
4. Open the item row with the pencil icon.
5. Enable **Deliver to Customer** for the row.
6. Select the Supplier and confirm the Customer shipping address.
7. Save and submit the Sales Order.

![The highlighted pencil icon opens the complete Sales Order item row.](/files/drop-ship-item-pencil.webp)

The stock indicator before an Item Code is green when the item is in stock and red when it is out of stock. Drop shipping does not require the item to be received into your warehouse, but the indicator can still help users understand the item’s current availability.

![The item row with Supplier delivers to Customer enabled and Apex Devices selected as the Supplier.](/files/drop-ship-item-fields.webp)

![The Customer and company address information used for the drop-ship transaction.](/files/drop-ship-customer-address.webp)

## Create the Purchase Order

From the submitted Sales Order, select **Create > Purchase Order**. In the dialog, select the Supplier and the drop-ship items, then create the Purchase Order.

Review the following before submission:

- **Is Subcontracted** should remain disabled unless the transaction is genuinely subcontracting.
- **Supplier** must be the party that will ship the goods.
- **Customer** and **Customer Address** must identify the final delivery destination.
- The items, quantities, rates, taxes, schedule dates, and terms must match the supplier agreement.

Submit the Purchase Order and send the approved document or instructions to the Supplier.

## Important fields and what they mean


| Field                 | What it means                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Deliver to Customer   | Marks the Sales Order item for direct delivery by a Supplier.                                                               |
| Supplier              | The Supplier expected to fulfil that item.                                                                                  |
| Customer              | The party receiving the goods. It is mapped to the Purchase Order for drop shipping.                                        |
| Customer Address      | The shipping destination printed or shared with the Supplier.                                                               |
| Schedule Date         | The date by which the Supplier should deliver the item.                                                                     |
| Warehouse             | Usually not used to receive a drop-shipped item because it does not enter your stock.                                       |
| Delivered By Supplier | Indicates that fulfilment is performed by the Supplier. Availability and wording can depend on the transaction and version. |


## Complete the sales cycle

A drop-ship Purchase Order does not create a stock receipt for your company. When the Supplier confirms delivery, use the actions available on the linked Sales Order or Purchase Order to record the delivery status according to your ERPNext version and process.

Create the [Sales Invoice](/erpnext/sales-invoice) for the Customer and the Purchase Invoice for the Supplier. Verify linked quantities so the Sales Order, Purchase Order, receivable, and payable all represent the same fulfilment.

If only part of an order is drop shipped, keep the remaining items on the normal warehouse fulfilment path. Each row can follow the appropriate route, but teams should verify the linked documents carefully.

## Returns and exceptions

If the Customer returns a drop-shipped item, coordinate the commercial and physical return with the Supplier. Create the appropriate return or credit documents for both sides. Because the goods did not enter your warehouse during the original delivery, do not create a warehouse receipt unless your return process actually brings them into your stock.

If the Supplier cannot fulfil the order, update or cancel the affected Purchase Order and resolve the Customer commitment on the Sales Order. Do not leave an open quantity without an owner or revised delivery date.

## Frequently asked questions

### Does drop shipping update stock?

Normally no. The Supplier delivers directly to the Customer, so the item does not pass through your warehouse.

### Can one Sales Order contain warehouse and drop-ship items?

Yes. Mark only the rows that the Supplier will deliver directly. Fulfil the other rows through Delivery Notes from your warehouse.

### Can different Suppliers fulfil different items?

Yes. Create the required Purchase Orders by Supplier and confirm that each item row is linked correctly.

### Why is the Purchase Order not available from the Sales Order?

Check that the Sales Order is submitted, the item row is marked for delivery to the Customer, a Supplier is selected or available, and the quantity is not already fully ordered.

### Who sends the invoice to the Customer?

Your company normally invoices the Customer. The Supplier invoices your company under the linked purchase transaction.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Drop Ship Between Subsidiary Companies](/erpnext/drop-ship-between-subsidiary-companies)

<!-- page: erpnext/erpnext__dropbox-backup.md -->
---
title: "Setting Up Dropbox Backups"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dropbox-backup"
updated: "2026-03-06"
---

We always recommend customers to maintain backup of their data in ERPNext. The database backup is downloaded in the form of an SQL file. If needed, this SQL file of backup can be restored in the another ERPNext account as well.

You can automate database backup download of your ERPNext account into your Dropbox account.


&gt; Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: &lt;https://frappecloud.com/docs/sites/backups&gt;
&gt; 
&gt; 

To setup Dropbox Backup, &gt; Home &gt; Integrations &gt; Dropbox Settings

  


#### Step 1: Login to Dropbox Developer area

&lt;https://www.dropbox.com/developers/apps&gt;

  


#### Step 2: Create a new Dropbox app

![Create new](/files/dropbox-open-3.png)  


  


#### Step 3: Fill in the details for your new app

![Choose Dropbox API and type as APP Folder](/files/dropbox-open-1.png) ![Setup APP Name](/files/dropbox-open-2.png)  


![https://support.frappe.io/files/nBdh7wu.png](https://support.frappe.io/files/nBdh7wu.png)  


#### Step 4: Insert your custom domain Redirect URI

`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish` ![Set Redirect URL](/files/dropbox_redirect_uri.png)  


  


#### Step 5: In a new window, open the Dropbox Settings page in your ERPnext installation

  


#### Step 6: Set backup frequency and email

Set the frequency to download your site backups to your Dropbox account. ![set frequency](/files/setup-backup-frequency.png)  


#### Step 7: Input Keys from your Dropbox App window

From your Dropbox App page, enter the app key and (unhidden) app secret into the ERPnext Dropbox settings page.

Alternatively, you can enter it manually in `sites/{sitename}/site_config.json` as follows,


```
       {
 "db_name": "demo",
 "db_password": "DZ1Idd55xJ9qvkHvUH",
 "dropbox_access_key": "ACCESSKEY",
 "dropbox_secret_key": "SECRECTKEY"
}

    
```
  


#### Step 8: Click Save before continuing

  


#### Step 9: After saving, click "Allow Dropbox Access"

The Dropbox login page will open in the new tab. This might require you to allow pop-up for your ERPNext account.

  


#### Step 11: Allow Dropbox Access

On successful login, you will find a confirmation message as following. Click on "Allow" to let your ERPNext account have access to your Dropbox account. ![Allow](/files/dropbox-3.png)  


  


#### Step 12: Confirm Backups Work

From the ERPnext Dropbox page, click `Take Backup Now` and then go to you Dropbox files view. You should see a new folder in Dropbox named `Apps` and inside of it your {New App} folder. Inside of it should be backup folders for both files and database. So for an app named `erpnext`, following are the folder locations:


```
Database files: /Apps/erpnext/database
Public files: /Apps/erpnext/files
Private files: /Apps/erpnext/private/files
  

```
&gt; **Note**: If the compressed backup size exceeds 1GB (Gigabyte), the system will upload the latest available backup to Dropbox instead of generating a new backup file.

<!-- page: erpnext/erpnext__dunning.md -->
---
title: "Sales Interest and Dunning | ERPNext Documentation"
description: "Set up formal overdue-payment reminders with interest, fees, letter text, and payment processing in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dunning"
updated: "2026-08-14"
---

Northstar Retail has not paid an invoice by its due date. Nova Industries can see the overdue balance in Accounts Receivable, but the customer now needs a formal notice that states what is overdue, the interest or reminder fee being charged, and the amount required to settle it.



A **Dunning** turns that overdue balance into a traceable collection document. It brings the relevant Sales Invoice instalments into a formal reminder, calculates optional interest and fees, stores the letter sent to the Customer, and links the eventual payment back to the demand.



Use Dunning when ordinary follow-up is no longer enough and your collection policy requires a formal reminder. It does not replace the Sales Invoice or create another sale. This guide explains how to configure reusable Dunning Types, issue the notice, and record the payment that resolves it.

## Before you begin

- The [Sales Invoice](/erpnext/sales-invoice) must be submitted and overdue.
- Create at least one Dunning Type.
- Choose the income account and Cost Center that should receive interest and dunning fees.

## Set up a Dunning Type

A Dunning Type stores reusable defaults for the reminder. Create different types for stages such as first reminder, second reminder, and final notice.


| Field                       | What it controls                                  |
| --------------------------- | ------------------------------------------------- |
| Is Default                  | Applies this type automatically when appropriate  |
| Dunning Fee                 | Fixed charge added to the reminder                |
| Rate of Interest (%) Yearly | Annual rate used to calculate interest            |
| Dunning Letter              | Language-specific body and closing text           |
| Income Account              | Account credited when fees and interest are paid  |
| Cost Center                 | Cost Center used for the fee and interest posting |


![Dunning Type with fee, interest, reminder text, and accounting defaults](https://novacompanies.m.frappe.cloud/files/dunning-type-clean.png)

## Create a Dunning

### From an overdue Sales Invoice

1. Open the overdue Sales Invoice.
2. Select **Create &gt; Dunning**.
3. Review the overdue payment schedule rows fetched into the document.
4. Select a **Dunning Type**, or enter the fee, interest, and letter text manually.
5. Save and submit.

### From the Dunning list

1. Open the Dunning list and select **Add Dunning**.
2. Select the Customer.
3. Select **Fetch Overdue Payments**.
4. Choose the overdue rows and select **Get Items**.
5. Complete the reminder details, then save and submit.

The Dunning must reflect the amount you intend to collect. Review the invoice rows, interest, fee, total outstanding, income account, and Cost Center before submission.

## Record payment

When the customer pays the invoice together with the interest and fee:

1. Open the submitted Dunning.
2. Select **Create &gt; Payment**.
3. Review the referenced invoices and the additional amount.
4. Submit the Payment Entry.

ERPNext records the interest and fee through the deductions or loss section of the Payment Entry and resolves the Dunning after the full amount is received.

## Statuses


| Status     | Meaning                                                   |
| ---------- | --------------------------------------------------------- |
| Draft      | Reminder has not been submitted                           |
| Unresolved | Submitted, but the required payment has not been received |
| Resolved   | Outstanding amount, interest, and fee have been settled   |
| Cancelled  | Submitted Dunning was cancelled                           |


## Troubleshooting

**Create Dunning is not available**

Confirm that the Sales Invoice is submitted, has an outstanding amount, and is past its due date.

**Interest or fee posts to the wrong account**

Review the Income Account and Cost Center on both the Dunning Type and the Dunning before creating the Payment Entry.

**The Dunning remains unresolved**

Open the linked Payment Entry and verify that it is submitted and covers all referenced invoice, interest, and fee amounts.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Accounts Receivables](/erpnext/accounts-receivables)
- [Process Statement Of Accounts](/erpnext/process-statement-of-accounts)
- [Payment Terms](/erpnext/payment-terms)

<!-- page: erpnext/erpnext__duplicate-record.md -->
---
title: "Duplicate Records\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/duplicate-record"
updated: "2026-03-04"
---


**'Duplicate' is a feature that helps you to copy values of existing document as-is into a new document.**

## Scenario

A customer has placed a 'reorder' for certain items with an electronic items supplier.

Since the new Sales Order will have all the details the same as that of the original Sales order, the supplier can simply open the original one and 'Duplicate' the order. The values of the original document will get updated as it is in the new Sales Order. Any changes, if required can be made thereafter.

To make a Duplicate document, you can go to the original document and click on 'Duplicate' from the Drop-Down menu.

![Duplicate Record](/files/using-duplicate-record-1.gif)

<!-- page: erpnext/erpnext__dynamic-link-fields.md -->
---
title: "Dynamic Link Fields\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dynamic-link-fields"
updated: "2026-03-04"
---


Dynamic Link field is a field which can search and hold the value of any DocType. Let's consider an example to learn how Dynamic Link field works.

While creating Opportunity or Quotation, we have to explicitly define if it is for a Lead or a Customer. Based on our selection (Lead/Customer), another link field shows up where we can select the actual Lead or Customer.

If you set the former field as Dynamic Link, where we select actual Lead or Customer, then the later field will be automatically linked to master selected in the first field, i.e. Leads or Customers. Hence we need not insert separate link fields for Customer and Lead.

Below are the steps to insert Custom Dynamic Field. For instance, we will insert Dynamic Link Field in Journal Entry.

#### Step 1: Insert Link Field for DocType

First, we will create a link field that will be linked to the DocType.

![Custom Link Field](/files/customize-dynamic-link-1.gif)

By **DocType** mentioned in the Option field, we mean parent DocType. So, just like Quotation is one DocType, which has multiple Quotation under it. Same way, DocType is also a DocType which has Sales Order, Purchase Order and other doctypes created as DocType records.

**DocType**  

---- Sales Order  

---- Purchase Invoice  

---- Quotation  

---- Sales Invoice  

---- Employee  

---- Work Order  

.. and so on.

So linking this field with parent DocType will list all the DocType records.

![journal Voucher Link Field](/files/customize-dynamic-link.png)

#### Step 2: Insert Dynamic Link Field

This custom field's type will be "Dynamic Link". In the Option field, the name of the Doctype link field will be mentioned.

![Custom Dynamic Field](/files/customize-dynamic-link-2.gif)

This field will allow selecting document id, based on the value selected in the Doctype link field. For example, if we select Sales Order in the prior field, the Dynamic Link field will list all the Sales Orders ids.

![Custom Dynamic Field](/files/customize-dynamic-link-3.gif)

**Customizing options in the Doctype Link field**

By default, the DocType link field will provide all the forms/docTypes for selection. If you wish this field to show certain specific docTypes in the search result, you will need to write Custom Script for it.

<!-- page: erpnext/erpnext__e-commerce-integrations-for-erpnext.md -->
---
title: "E-commerce Integrations for ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e-commerce-integrations-for-erpnext"
updated: "2026-07-04"
---

ERPNext is easy to integrate with recommerce and ecommerce platforms because business data in ERPNext is available through the Frappe Framework REST API. Products, customers, orders, invoices, payments, shipments, returns, and stock movements are stored as DocTypes, and DocTypes can be read or updated through standard API endpoints.

This makes ERPNext a practical backend for recommerce platforms that handle refurbished, pre-owned, rental, buyback, resale, or reverse-logistics workflows. The storefront can focus on customer experience, while ERPNext manages inventory, accounting, fulfillment, purchasing, returns, and reporting.

## Why Integration Is Straightforward

- **REST APIs are available by default:** External systems can create and update ERPNext records without direct database access.
- **Commerce records already exist:** Items, Customers, Sales Orders, Sales Invoices, Delivery Notes, Payment Entries, Stock Entries, and Warehouses are standard ERPNext records.
- **Recommerce data can be added:** Fields such as condition, grade, serial inspection, refurbishment status, warranty, buyback source, and resale channel can be added with custom fields or DocTypes.
- **Sync can be automated:** Webhooks, scheduled jobs, and background workers can sync orders, stock, payment status, shipment updates, and returns between systems.

## Common Integration Flows

- **Catalog sync:** Send item details, prices, images, condition, and stock availability from ERPNext to the platform.
- **Order sync:** Create Sales Orders or Sales Invoices in ERPNext when orders are placed.
- **Inventory sync:** Update the platform when stock is reserved, sold, returned, refurbished, or made available again.
- **Fulfillment sync:** Send shipment and tracking details from ERPNext back to the platform.
- **Returns and buybacks:** Track incoming goods using Stock Entries, Purchase Receipts, Quality Inspections, or custom DocTypes.

## Ready-Made Marketplace Options

Before building a custom connector, check whether an existing Frappe Marketplace app already covers the workflow:

- [Ecommerce Integrations](https://cloud.frappe.io/marketplace/apps/ecommerce_integrations): E-commerce marketplace integrations for ERPNext.
- [WooCommerce Connector](https://cloud.frappe.io/marketplace/apps/woocommerceconnector): Synchronizes items, stock, customers, addresses, sales orders, sales invoices, and payment entries with WooCommerce.
- [ERPNext Shipping](https://cloud.frappe.io/marketplace/apps/erpnext_shipping): Shipping integration for ERPNext, useful for fulfillment and tracking.
- [Frappe Paystack](https://cloud.frappe.io/marketplace/apps/frappe_paystack): Payment gateway integration for ERPNext and Frappe.

## When To Build A Custom Connector

Build a custom connector when the recommerce platform has unique flows such as device grading, serialized refurbishment, trade-in pricing, warranty tracking, marketplace-specific listing rules, or reverse logistics. In most cases, the connector maps platform events to ERPNext documents and calls the REST API securely.

## Best Practices

- Keep ERPNext as the source of truth for stock and accounting.
- Use stable external IDs to match ERPNext records with platform records.
- Log every sync attempt so failed updates can be retried.
- Use API keys with limited permissions and test on a staging site before going live.

## Related Topics

- [Frappe REST API](/framework/user/en/api/rest)
- [Sales Order](/erpnext/sales-order)
- [Item](/erpnext/item)
- [Stock Entry](/erpnext/stock-entry)
- [Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace)

<!-- page: erpnext/erpnext__e_commerce_search.md -->
---
title: "E-commerce Search"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e_commerce_search"
updated: "2026-03-02"
---

All Product Listing pages contain a **Search bar** that lets users quickly search for Website Items or Item Groups. It also stores recent searches that you can click on and reuse.

![Search](/files/e-commerce-search.png)

## RediSearch

> **Experimental**: Requires Redis 6+


By default ERPNext performs a simple DB search but you can **optionally** choose to use [RediSearch](https://redis.com/modules/redis-search/) for super fast search instead. You can refer to RediSearch's [installation documentation](/erpnext/installing_redisearch_to_enable_super_fast_e_commerce_search).


> Go to > **E Commerce Settings** > **Item Search Settings** > Check **Enable Redisearch**

![Item Search Settings with RediSearch](/files/item-search-settings-enabled.png)

#### Settings without RediSearch
If RediSearch is not installed, this is what the **Item Search Settings** will look like:
![Item Search Settings without RediSearch](/files/item-search-settings.png)

#### Configurable Fields
Along with fast search you get the option to configure fields that you want search to consider. Add comma separated fields in the **Search Index Fields** text box to make them searchable.

E.g. Adding **brand** to these fields makes it searchable. Typing a brand, e.g. 'Apple', should give results where the brand is 'Apple'.

The results will be based on values in all the fields mentioned in the **Search Index Fields** text box.

> Fields of the foll.g types are supported: **Link**, **Table MultiSelect**, **Data**, **Small Text**, **Text Editor**

<!-- page: erpnext/erpnext__e_commerce_settings.md -->
---
title: "E Commerce Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e_commerce_settings"
updated: "2026-03-02"
---

The legacy **Shopping Cart Settings** and **Products Settings** are combined into a single **E -Commerce Settings** page. 

The e-commerce settings in ERPNext can be leveraged by users to manage and streamline the online sales processes. These settings can enable users to efficiently manage product listing, customer management and integration with other ERPNext modules seamlessly.


> **E Commerce Settings / Webshop Settings** in the awesomebar (search bar)
> 
> 

![E Commerce Settings](/files/e_commerce_settings_overview.png) *E Commerce Settings*

### Products Per Page

Define how many products to show per page on the Product Listing in the **All Products** page (`/all-products`).

### Filters and Categories

![Filters and Categories](/files/filters_and_categories.png) *Filters and Categories*

You can also add filters to your listing. There are two types of filters:

1. **Field Filters**: Enable the **Field Filters** checkbox and add the fields based on which you want to have filters. These fields will also be used as categories for the **Shop by Category** page.
2. **Attribute Filters**: Enable the **Attribute Filters** checkbox and add the attributes based on which you want to have filters.

### Display Settings

1. **Hide Variants**: Only show Website Item Templates on the Product Listing.
2. **Enable Variant Selection**: Show a configure button if the Item has variants. It can be used to narrow down the specific item based on Attributes.
3. **Show Price**: Show Item Price on the product page.
4. **Show Stock Availability**: Show whether the Item is in stock.
5. **Show Stock Quantity**: Show available stock on the product page.
6. **Allow items not in stock to be added to cart**: Allow items not in stock to be added to Cart.
7. **Show Apply Coupon Code**: Additional provision to apply coupon code at checkout.
8. **Show Contact Us Button**: Show a contact us button which customers can use to enquire about the Item. It will create a Lead in the system.
9. **Show Public Attachments**: Show public attachments in the Sales Order generated, after checkout, for Customers.


> You can **Hide Variants** only when Attribute Filters are disabled.
> 
> 

### Shopping Cart

1. **Company**: Specify the company that the web shop is set up for.
2. **Price List**: Mention Price List to consider while fetching Item Prices.
3. **Enable Shopping Cart**: Add the provision to add items to Cart.
4. **Default Customer Group**: Add the Default Customer Group to be set while auto creating customers on adding to Cart.

### Checkout Settings

1. **Enable Checkout**: If checkout is disabled, when your customers add an item to Cart, they can click on the **Request for Quotation** button to get a quote for it. A [Quotation](/erpnext/quotation) is generated in the system. If enabled, a [Sales Order](/erpnext/sales-order) is generated on clicking on the **Place Order** button in the Cart.
2. **Payment Gateway Account**: If checkout is enabled, you must have [PayPal Integration](/erpnext/paypal-integration) or [Razorpay Integration](/erpnext/razorpay-integration).
3. **Payment Success Url**: After payment completion redirect users to the selected option.
4. **Show Price in Quotation**: If checkout is disabled, you can choose whether or not to show prices against Website Items in the Quotation.
5. **Save Quotations as Draft**: If checkout is disabled, on clicking on the **Request for Quotation** button, you can choose whether the auto-generated Quotation must be auto-submitted or kept in the Draft state.

### Add-ons

1. **Enable Wishlist**: Add the provision to add items to a Wishlist
2. **Enable Reviews and Ratings**: Add the privision for **customers** to leave reviews and ratings against Website Items.
3. **Enable Recommendations**: Add the provision to show manually selected **recommended items** against a Website Item.

### Shop By Category

The **Shop By Category** page is an out-of-the-box page that lists categories linked to Website Items. These categories can be configured in the **Filters and Categories** section's **Field Filters** table.

You can also select a slideshow as the banner of the page.

### Guest Display Settings

1. **Hide Price for Guest**: You can show or hide prices against Website Items for guest users (users who are not logged in).
2. **Redirect on Action**: If a guest user tries to add a Website Item to Cart or to the Wishlist, you can select a URL to redirect them to. By default, guest users are redirected to the `/login` page. You can instead redirect them to a custom Web Form of choice by adding a URL here e.g. `/contact-us`

<!-- page: erpnext/erpnext__easy-steps-to-setup-workflow.md -->
---
title: "Easy steps to setup Workflow"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/easy-steps-to-setup-workflow"
updated: "2026-03-04"
---

When a company has multiple levels of approval for a document, a Workflow can be set.   
In ERPNext, you can go to Workflow list --> Create New --> Name the workflow and define :1. States
2. Transition rules.

  
1. States :

When a document is passed on for different levels of approval, there are states defined at each level for the role of the user.   
![](/files/Y3TzzU2.png)  
  
1. Transition Rules :

For instance: A **Sales user** is only allowed to create a **Quotation** and it can be saved in the **Draft** state. Further, it can be sent to the **Sales Manager** for approval and the User with this role can have the permission to either **Approve** or **Reject** the Quotation after which it can either be sent to the **Draft** State if **Rejected** or final **Approved** State.   
![](/files/xJUtkGy.png)  
Error Messages: **A document cannot be Cancelled before it is Submitted.**   
[This is a typical error faced by users who define the state of the Document cancelled before Submitting it. Doc Status 1 defines that the Document will be Submitted at that State, thus the State with Doc status 2 should only be defined in the Transition after the State with Doc status 1. ]  
Setup a Simple Workflow to begin with and let us know what you think more on Workflows! We love to see our Users Happy!! ;)   
  

<!-- page: erpnext/erpnext__edit-submitted-document.md -->
---
title: "Edit Submitted Document\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/edit-submitted-document"
updated: "2026-03-04"
---


To edit a submitted document, you need to cancel it first. Following are steps to edit submitted document. These steps assume you have the appropriate permissions for cancelling and editing a document.

#### Step 1: Cancel Submitted Document

You will find Cancel button on upper right corner of submitted document.

![Cancel Doc](/files/edit-submitted-doc-1.png)

#### Step 2: Amend the document

On cancellation of submitted document, Amend button will be became visible.

![Amend Doc](/files/edit-submitted-doc-2.png)

#### Step 3: Save and Submit the document

On clicking Amend button, same document will become editable again. After Making required changes, save and submit the document.

![Resave and Submit Doc](/files/edit-submitted-doc-3.png)
Note: If your document is linked with other documents, then you will need to cancel the dependant document before cancelling the parrent document.

Example: If you have created Delivery Note and Sales Invoice against Sales Order, which you need to amend, then you should first Cancel Delivery Note and Sales Invoice made for that Sales Order. Then amend Sales Order, re-save and re-submit it.

<!-- page: erpnext/erpnext__editing-a-field-after-submission.md -->
---
title: "Edit a Field after Submission "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/editing-a-field-after-submission"
updated: "2026-03-04"
---

In ERPNext, once a document is submitted, you can only edit it through Cancel > Amend. However, you can still make certain fields (custom fields) editable after submission using the **Allow on Submit** feature. For example, we have created a custom field called "Supplier ID" in Supplier Quotation. To allow editing of this field after submission, follow the following steps:  
1) Go to Settings > Customize Form and select the Form Type (Supplier Quotation in this case).  
2) Expand the field row and check the "Allow on Submit" checkbox.  
![](/files/hyYfSoc.png)  
![](/files/dp37Dab.png)  
  
3) Click on Update.  
This setting will allow you to edit this field even after submitting the document without amending it.  
**Note:** The Allow on Submit feature works only for non-standard fields (custom fields).

<!-- page: erpnext/erpnext__education-module-in-erpnext.md -->
---
title: "Education Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/education-module-in-erpnext"
updated: "2026-07-04"
---

## Overview

Frappe Education is an open-source education management app for the Frappe and ERPNext ecosystem. It helps schools, colleges, coaching institutes, and other academic institutions manage academic administration, student information, courses, admissions, fees, scheduling, and student self-service in one system.

The app is built on Frappe Framework and works alongside ERPNext, so institutions can manage academic operations while still using ERPNext for accounting and other business processes.

## GitHub Repository

Source code: [github.com/frappe/education](https://github.com/frappe/education)

The repository describes Frappe Education as an open-source Education Management System for streamlining administrative and academic processes in educational institutions.

## When To Use Frappe Education

Use Frappe Education when an institution needs an ERPNext-backed system for academic operations, not just a learning management system. It is useful when student records, instructors, courses, admissions, fee collection, and academic schedules need to be managed in a structured way.

## Key Features

- **Student and teacher management:** Maintain profiles and academic records for students, guardians, and instructors.
- **Admissions:** Manage student applications and admission workflows from enquiry to enrollment.
- **Programs and courses:** Define academic programs, courses, batches, terms, and course schedules.
- **Attendance:** Track student attendance and use it for academic administration and reporting.
- **Fee management:** Create fee structures, schedule fee collection, and track payment status.
- **Student portal:** Let students access information such as timetables, attendance, fees, and grades.

## How It Fits With ERPNext

Frappe Education extends ERPNext for education-specific workflows. ERPNext provides the broader ERP foundation, while Frappe Education adds the academic objects and flows needed by educational institutions. This makes it suitable for organizations that want both education management and ERP-style accounting or operations in the same ecosystem.

## Related Links

- [Frappe Education on GitHub](https://github.com/frappe/education)
- [Frappe Education website](https://frappe.io/education)
- [Frappe Education documentation](https://docs.frappe.io/education)

<!-- page: erpnext/erpnext__electronic-signature.md -->
---
title: "Signature Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/electronic-signature"
updated: "2026-03-04"
---

  


Electronic signature can be created in ERPNext using the Signature field type. This field allows you to write a signature in a block, just like the signature on a paper.

To create an electronic signature, follow the following steps:

1. Open the DocType and go to Customise Form.
2. In the Form view or Fields table, create a new field called Signature and select the Field Type as **Signature.**

![Screenshot 2024-06-21 at 5.32.17 PM](/files/Screenshot 2024-06-21 at 5.32.17 PM.png)  


![Screenshot 2024-06-21 at 5.29.51 PM](/files/Screenshot 2024-06-21 at 5.29.51 PM.png)  


3. Click on Update.
4. Refresh the page and put your signature.

![Screenshot 2024-06-21 at 5.27.47 PM](/files/Screenshot 2024-06-21 at 5.27.47 PM.png)  


  
