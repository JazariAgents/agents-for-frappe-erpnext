<!-- Frappe documentation: erpnext, part 22 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__document-naming-for-avoiding-tab-series-issues.md -->
---
title: "Document Naming for Avoiding tabSeries Issues"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming-for-avoiding-tab-series-issues"
updated: "2026-08-12"
---

When you save a document in ERPNext a Sales Invoice, Stock Entry, Payment, anything with an auto-generated number, the system has to figure out the next number in the sequence (eg. 0001, 0002, 0003 and so on).



To make sure two documents never get the same number, ERPNext keeps a single counter for each naming series in a table called tabSeries. Before giving out the next number, it locks that counter so nobody else can touch it, adds 1, and then unlocks it. This happens in a fraction of a second, so normally you never notice it.



If hundreds of documents are being created at the same time and they all use the same naming series, they all need the same counter. Only one can hold the lock at a time, so everyone else has to wait in line.



When the line gets long, you start seeing:

- Documents that take a long time to save
- Bulk imports or bulk submissions that crawl or get stuck
- Errors like "Record has changed since last read in table 'tabSeries'" or database lock/deadlock timeouts
- Background jobs piling up in the queue



This gets much worse after busy periods, month-end, or when more workers are added to handle load, because now even more transactions are fighting over that one counter.



### **Why it happens more with customisation**

A very common cause is a customisation that forces a lot of transactions through a single, restricted naming series. Everything funnels into one counter, so one counter becomes the bottleneck for the whole operation. The more you scale up, the longer the queue behind that single row.



### **The simple fix: use more than one naming series**

The counter is locked per naming series. So the trick is easy:

Give different groups of transactions their own naming series, so they use different counters and stop waiting on each other.

Instead of one big line at one counter, you open several counters. Each line moves independently and in parallel.



### **Good ways to split series**

Pick whatever naturally divides your transactions. For example:


|              |                                              |
| ------------ | -------------------------------------------- |
| **Split by** | **Example series**                           |
| Branch       | SINV-MUM-.YYYY.-.####, SINV-DEL-.YYYY.-.#### |
| Project      | SINV-PROJ-A-.####, SINV-PROJ-B-.####         |
| Cost Center  | SINV-CC01-.####, SINV-CC02-.####             |
| Department   | SINV-SALES-.####, SINV-SUPPORT-.####         |


The idea is the same in every case: transactions that run at the same time should not all sit on the same counter. The more you spread them out, the less each one has to wait.



### **Extra tips for very large operations**

If you regularly create huge batches of documents at once:



- Spread big imports across multiple series so the load is shared, instead of importing everything under one series.
- Provide the name yourself during imports/API calls where possible. If a document already has a name, ERPNext skips the counter entirely. No lock, no waiting. For example, customer ID is generated based on Customer Name itself.
- Avoid customisations that force everything into one narrow series. Review any custom naming logic to make sure it isn't funnelling all transactions through a single counter.
- Stagger very large jobs slightly rather than firing them all in the same instant, if the process allows it.

<!-- page: erpnext/erpnext__document-naming-settings.md -->
---
title: "Document Naming Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming-settings"
updated: "2026-03-04"
---

**Masters and transactions can be given prefixes in the form of naming series.**

ERPNext allows you to make prefixes to your documents, with each prefix  
forming its own series. For example, a series with prefix INV12#### will have  
numbers INV120001, INV120002, and so on.

You can have multiple series for all your transactions. For example, Sales Invoice IDs like these can be generated:

- ACC-SINV-.YYYY.-
- SINV12####
- SALESINV-00####

You can define or select the Naming Series pattern from:

> Home > Settings > Document Naming Settings

## 1. Setting up Naming Series for Documents

1. Select the transaction for which you want to make the series. The system will update the current series in the text box.
2. Edit the series as required with unique prefixes for each series.
  he first prefix will be the default prefix. Each new prefix Naming Series must be added on a new line. The newly added naming series will be available in the document.

[Screenshot on the live page: document naming settings]

3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox.
  here will be no default naming series if this is ticked.
4. You can also update the starting point of a series by entering the series name and the starting point in the “Update Series” section.
5. Click on the Update button to update the set of Naming Series for the selected document.

> Note: To see the newly added Naming Series, click on Settings > Reload.

## 2. Financial Year in Naming Series

You can also show the financial year in the Naming Series. By default, if you enter 'YYYY' in the naming series, it'll pick up the current year. To set naming series based on the fiscal year, enter something like 'ACC-SINV-.19-20.-' where 19-20 is the current Fiscal Year. It is common to have a separate series for each financial year.

As you can see, in the following screenshot of a Sales Invoice, the year 2019 is listed:

[Screenshot on the live page: Fiscal year in Naming Series]

## 3. Updating the current value for existing Naming Series

You can change the starting/current sequence number of an existing series.

1. Under the Update Series section, select the prefix whose sequence is to be changed.
2. The current value will be fetched and displayed.
3. Change starting/existing sequence number if needed.
4. Click on Update Series Number.

For example, if the current Sales Order series number is at 16, and you want to restart or set it as 50, enter 0 or 50 depending on your case. Any new Sales Order created will start from the new sequence number.

To know more about this, [visit this article](/erpnext/naming-series-current-value).

> Tip: You could have a separate series for each type of Customer or for  
each of your retail outlets.

## 4. Using Field Values in Naming Series

Some companies prefer to make use of "short-codes" for suppliers, i.e. WN for company "Web Notes" that later can be used in naming series for quick identification.

For example:

 A custom field "Vendor ID" is created under Document: Supplier.  
 Then under Naming Series, we allow something like  
 PO-.YY.MM.-.vendorid.-.####  
 Resulting in "PO-1503-WN-00001"

## 5. Updating Amended Documents

Some companies prefer naming amended documents as new documents. ERPNext provides a feature to configure this setting based on your requirements.

To configure the naming of amended documents:

1. Navigate to the Amended Documents section.
2. Choose one of the following options:
  1. Apply the Default Amend Counter to change the naming for all doctypes.
  2. Customize naming for specific doctypes by selecting the relevant doctypes and defining their naming methods.

[Screenshot on the live page: Amended Naming Series]



3. Click "Update Amendment Counter" to save your changes.

## 6. Video


<iframe allowfullscreen="" height="315" width="100%" frameborder="0" src="https://www.youtube.com/embed/IGyISSfI1qU"></iframe>


## 7. Related Topics

1. [Bulk Rename](/erpnext/bulk-rename)

<!-- page: erpnext/erpnext__document-naming.md -->
---
title: "Document Naming Rule"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming"
updated: "2026-03-04"
---

In ERPNext, managing naming conventions systematically helps maintain consistency and traceability across your records. The Document Naming Rule feature allows you to set up dynamic naming based on conditions, offering more flexibility than the standard Document Naming Settings (Series).

✨ Key Differences from Traditional Naming Settings
While Document Naming Settings apply a prefix or pattern globally to a doctype, Document Naming Rule introduces conditional logic to apply naming series based on specific field values within the document.

🛠️ How to Set Up a Document Naming Rule
Follow the steps below to configure a Document Naming Rule:

**Steps:**

1. Select the Document Type
Choose the Doctype (e.g., Sales Invoice, Customer, etc.) where the rule will apply.


2. Set Priority
Assign a Priority number to the rule.

🔹 Higher priority rules (e.g., 10) are applied before lower ones (e.g., 5).
🔹 If multiple rules match, the one with the highest priority is used.

[Screenshot on the live page: Selsct a DocType]

3. Add Rule Conditions
➕ You can add multiple conditions per rule. The rule is applied only when all conditions are satisfied.

🔍 Example Use Case
Scenario: You want to name Customers based on their location.

If the customer's Country is India, the naming format should be:
CUST-INDIA-00001, CUST-INDIA-00002, ...

This can be achieved using two Document Naming Rules:

Rule 1: Prefix = CUST-INDIA-, Condition = Country = India

Rule 2: Prefix = CUST-USA-, Condition = Country = USA

If the Country is USA, the format should be:
CUST-USA-00001, CUST-USA-00002, ...

4. Define the Prefix
Enter the desired prefix in the Prefix field under the Naming section.
Example: PSI/


5. Set the Serial Number Start
Specify the starting serial number in the field next to the prefix.
Example: 5 → The first document will be named PSI/00005

[Screenshot on the live page]

Here is an Example:


✅ Benefits
Automates naming based on document fields

Reduces manual selection and human error

Supports multiple naming patterns within the same Doctype

Useful for companies with multi-branch, multi-country, or multi-category document types

📝 Notes
Always ensure the conditions are specific enough to avoid conflicts between rules.

If no rule matches, the system will fall back to the default Naming Series (if configured).

<!-- page: erpnext/erpnext__document-title-with-multiple-fields.md -->
---
title: "Document Title with multiple fields"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-title-with-multiple-fields"
updated: "2026-03-04"
---

Ever wondered about creating a document title with more than one field? For example, let's say your sales invoice should have the title of the customer name (which is present by default) and its tax ID.

How will you do this? Well, here's an interesting customisation ability of the framework which can do this without any need of scripting.

 

Here are the steps,

1. Make sure you have a field that is going to be referred to for creating the title of the document.
2. The basic setup ends by adding this field name in the view settings of the doctype for the title.
3. If you want to add more to it,
4. Add the field links in the **default** of the field in this format **{field_name}**

 

**_Here's an example of how it looks_**

[Screenshot on the live page]

 

         b. This will result in a multifield title for the selected doctype.

 

This can be extended to creating a custom field with consolidated values of different fields and merging them to a completely new field. The best use case is creating addresses for custom doctypes easily without any custom scripting.

 

This is how the field configuration will look

 

[Screenshot on the live page]

 

Note: We are using options for adding values because it updates the field by changing its source fields. (Doest work with defaults)

Also, the field type should not be data. (Could be read-only or HTML)

 

Here's the output of the above configuration

 

[Screenshot on the live page]

<!-- page: erpnext/erpnext__document-title.md -->
---
title: "Document Title\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-title"
updated: "2026-02-26"
---


**You can customize the title of documents based on properties so that you have meaningful information for the list views.**

For example, the default title on a Quotation is the customer name, but if you are dealing with only a few customers and sending lots of quotations to each customer, you may want to customize.

[Screenshot on the live page: Document Title]

## Setting Title Fields

From ERPNext Version 6.0 onwards, all transactions have a 'Title' property. If there is not a title property, you can add a **Custom Field** as title and set the **Title Field** via **Customize Form**.

You can set the default value of that property by using Python style string formatting in **Default** or **Options**

1. To edit a default title, go to Customize Form
2. Select the Form for which you would like to change the Title Field.
3. Edit the **Title Field** in the form.

## Defining Titles

You can define the title by setting document properties in braces `{}`. For example, if your document has fields `customer_name`, you can specify that as the Title of the Form.

[Screenshot on the live page: Set Document Title]

Alternatively, you can also define a particular field as the 'Title Field' in Customize Form.

[Screenshot on the live page: Title Field] 

## Fixed or Editable Titles

If your title is generated as a default title, it can be edited by the user by clicking on the heading of the document.

[Screenshot on the live page: Editable Title]

If you want a fixed title, you can set the rule in the **Options** property. In this way, the title will be automatically updated every time the document is updated.

<!-- page: erpnext/erpnext__document-versioning.md -->
---
title: "Document Versioning\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-versioning"
updated: "2026-03-04"
---

**In ERPNext, Document Versioning is a feature that allows you to track all the changes made in a form or a document.**

This feature comes handy while conducting an Audit Tail to check on what changes were made in a document along with the time of change and the stakeholder responsible.

[Screenshot on the live page: Document Versioning]

## How to Enable Document Versioning

Let's assume that we need to enable Document Versioning for Purchase Order.

1. Go to Purchase Order List.
2. Click on Customize from the drop-down menu.
3. You shall be directed to the [Customize Form](/erpnext/customize-form) page for Purchase Order.
4. Check the field "Track changes" in the Properties.
  Document Versioning (picture on the live page)

With this, Document Versioning shall be enabled for all the Purchase Orders edited henceforth.

### Version Log

For each document that has Document Versioning enabled, a Version Log is created. Herein, there will be links to specific versions of the document.

When you click on these links, you will be directed to a log of all the fields and the changes made therein.

[Screenshot on the live page: Document Versioning]

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

[Screenshot on the live page: Active Domains area in ERPNext Domain Settings]


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

[Screenshot on the live page]
*Download backup post backup taken*

[Screenshot on the live page]

## Downloading Files Backup

Clicking on Download Files Backup will send an email with links to the backup for both private and public files. Email must be configured for this to work.

[Screenshot on the live page]

## Getting Backup Encryption Key

In order to get the backup encryption key, click on the designated button. Upon getting your system password validated, the system will provide you with the encryption key.

[Screenshot on the live page]

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

[Screenshot on the live page: Task]

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

[Screenshot on the live page: Production Forecasting]

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

[Screenshot on the live page: Drop-ship Sales Order with the customer, delivery date, supplier-delivered items, quantities, rates, and stock indicators.]

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

[Screenshot on the live page: The highlighted pencil icon opens the complete Sales Order item row.]

The stock indicator before an Item Code is green when the item is in stock and red when it is out of stock. Drop shipping does not require the item to be received into your warehouse, but the indicator can still help users understand the item’s current availability.

[Screenshot on the live page: The item row with Supplier delivers to Customer enabled and Apex Devices selected as the Supplier.]

[Screenshot on the live page: The Customer and company address information used for the drop-ship transaction.]

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

[Screenshot on the live page: Create new]  


  


#### Step 3: Fill in the details for your new app

[Screenshot on the live page: Choose Dropbox API and type as APP Folder] [Screenshot on the live page: Setup APP Name]  


[Screenshot on the live page: https://support.frappe.io/files/nBdh7wu.png]  


#### Step 4: Insert your custom domain Redirect URI

`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish` [Screenshot on the live page: Set Redirect URL]  


  


#### Step 5: In a new window, open the Dropbox Settings page in your ERPnext installation

  


#### Step 6: Set backup frequency and email

Set the frequency to download your site backups to your Dropbox account. [Screenshot on the live page: set frequency]  


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

On successful login, you will find a confirmation message as following. Click on "Allow" to let your ERPNext account have access to your Dropbox account. [Screenshot on the live page: Allow]  


  


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


[Screenshot on the live page: Dunning Type with fee, interest, reminder text, and accounting defaults]

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

[Screenshot on the live page: Duplicate Record]

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

[Screenshot on the live page: Custom Link Field]

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

[Screenshot on the live page: journal Voucher Link Field]

#### Step 2: Insert Dynamic Link Field

This custom field's type will be "Dynamic Link". In the Option field, the name of the Doctype link field will be mentioned.

[Screenshot on the live page: Custom Dynamic Field]

This field will allow selecting document id, based on the value selected in the Doctype link field. For example, if we select Sales Order in the prior field, the Dynamic Link field will list all the Sales Orders ids.

[Screenshot on the live page: Custom Dynamic Field]

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

[Screenshot on the live page: Search]

## RediSearch

> **Experimental**: Requires Redis 6+


By default ERPNext performs a simple DB search but you can **optionally** choose to use [RediSearch](https://redis.com/modules/redis-search/) for super fast search instead. You can refer to RediSearch's [installation documentation](/erpnext/installing_redisearch_to_enable_super_fast_e_commerce_search).


> Go to > **E Commerce Settings** > **Item Search Settings** > Check **Enable Redisearch**

[Screenshot on the live page: Item Search Settings with RediSearch]

#### Settings without RediSearch
If RediSearch is not installed, this is what the **Item Search Settings** will look like:
[Screenshot on the live page: Item Search Settings without RediSearch]

#### Configurable Fields
Along with fast search you get the option to configure fields that you want search to consider. Add comma separated fields in the **Search Index Fields** text box to make them searchable.

E.g. Adding **brand** to these fields makes it searchable. Typing a brand, e.g. 'Apple', should give results where the brand is 'Apple'.

The results will be based on values in all the fields mentioned in the **Search Index Fields** text box.

> Fields of the foll.g types are supported: **Link**, **Table MultiSelect**, **Data**, **Small Text**, **Text Editor**
