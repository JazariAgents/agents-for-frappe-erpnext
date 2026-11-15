<!-- Frappe documentation: erpnext, part 20 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__deferred-revenue.md -->
---
title: "Deferred Revenue | ERPNext Documentation"
description: "Configure ERPNext deferred revenue for prepaid services, invoice the customer, recognize income over time, and verify the ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-revenue"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, pays $1,200 upfront for a one-year warranty program. The invoice is raised today, but Nova Industries earns the revenue month by month as it provides the service.



Deferred Revenue keeps the unearned portion out of current income. ERPNext first posts the invoice amount to a liability account, then recognizes the appropriate share as income over the service period.



Use deferred revenue when a customer pays or is invoiced before your company has completed the related service, such as annual support, maintenance contracts, subscriptions, or prepaid service plans.



## Understand the accounting effect

Assume the invoice has no tax for simplicity.


| Event                           | Debit                      | Credit                            |
| ------------------------------- | -------------------------- | --------------------------------- |
| Submit the $1,200 Sales Invoice | Debtors $1,200             | Deferred Revenue liability $1,200 |
| Recognize one eligible period   | Deferred Revenue liability | Service Income                    |
| Receive the Customer payment    | Bank $1,200                | Debtors $1,200                    |


A [Payment Entry](/erpnext/payment-entry) clears the receivable. It does not determine when the income is earned. Recognition is controlled by the deferred settings and service dates.

## Before you begin

Prepare:

- A deferred revenue liability account in the [Chart of Accounts](/erpnext/chart-of-accounts).
- The final Income Account, such as Service Income.
- A service [Item](/erpnext/item).
- The contract or coverage start and end dates.
- A Customer and a valid [Sales Invoice](/erpnext/sales-invoice) setup.
- The applicable [Accounts Settings](/erpnext/accounts-settings) for automatic processing and day- or month-based allocation.

Do not use an ordinary Income Account as the deferred account. The unearned balance belongs on the Balance Sheet until the service is delivered.

## Configure deferred settings

In Accounts Settings, choose whether ERPNext books deferred entries by **Days** or **Months**, whether processing runs automatically, and whether recognition is posted directly or through [Journal Entries](/erpnext/journal-entry).

If $12,000 covers a 12-month service period, **Months** normally recognizes $1,000 for each complete month. With **Days**, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact dates. This original example is retained because it shows why monthly recognition amounts can differ without being wrong.

See [Deferred Accounting](/erpnext/deferred-accounting) for the full setting behavior.

## Enable deferred revenue on the Item

Open the Item used for the service or plan, select the **Accounting** tab, and enable **Deferred Revenue**. Enter a standard number of revenue months when it is useful for the Item.



![Enable deferred revenue on the service Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

Current ERPNext keeps the deferred account and actual service dates on the Sales Invoice Item row. The Item option identifies that the line is eligible for deferred treatment.

## Create the Sales Invoice

Create a Sales Invoice for the Customer and add the deferred-revenue Item. Confirm the Company, posting date, currency, rate, taxes, and Cost Center as you would for any invoice.

In the Items table, select the pencil icon to open the complete row editor.



![Open the Sales Invoice Item row](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-item-pencil.png)

Expand **Deferred Revenue** and complete:


| Field                    | What it means                                                             |
| ------------------------ | ------------------------------------------------------------------------- |
| Enable Deferred Revenue  | Applies deferred treatment to this invoice row                            |
| Deferred Revenue Account | Liability account holding the unearned balance                            |
| Service Start Date       | First date on which the service is provided                               |
| Service End Date         | Final date of the service period                                          |
| Service Stop Date        | Optional earlier stop date when service ends before the original end date |
| Income Account           | Final account that receives recognized revenue                            |


![Deferred revenue account and service dates](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-service-period.png)

The screenshot uses **Customer Advances - NET** as the deferred liability and **Service - NET** as the final income account. Use dedicated accounts if that gives your company clearer reporting.

Submit the invoice only after verifying every deferred row. One invoice can contain several rows with different service periods.

## What happens on submission

ERPNext creates the normal Customer receivable, but credits the deferred liability instead of immediately crediting the Income Account for the eligible row. This keeps unearned revenue out of the Profit and Loss Statement.

If tax is present, tax accounting follows the configured tax rules. Deferred revenue controls the eligible Item's net income recognition; it does not automatically defer every tax or charge on the invoice.

## Recognize the revenue

When automatic processing is enabled, ERPNext processes eligible schedules through a background job. Otherwise, create a [Process Deferred Accounting](/erpnext/process-deferred-accounting) document with **Type = Income**.

For each eligible period, the recognition entry debits the deferred revenue account and credits the Sales Invoice row's Income Account. When posting through Journal Entry is enabled, ERPNext creates Journal Entry documents. They either remain Draft for review or are submitted automatically, depending on Accounts Settings.

The original page described monthly Journal Entries. That remains valid when Journal Entry posting is enabled. With direct posting, the same accounting effect appears in the General Ledger without a separate Journal Entry document.

## Verify recognized and pending revenue

Run the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report). Check the invoice, service period, invoiced amount, recognized amount, and pending balance.

Then review the [General Ledger](/erpnext/general-ledger):

- The deferred liability should begin with the invoice amount.
- Each recognition period should reduce that liability.
- The same amount should increase the Income Account.
- After the complete service term, the eligible deferred balance should be fully recognized, subject to rounding or approved changes.

Also verify the Customer receivable separately. The invoice can be unpaid, partially paid, or fully paid while revenue recognition continues according to the service period.

## Stop, cancel, or amend the service

If a service ends early, record the supported **Service Stop Date** and follow your version's processing behavior. Check the deferred report after the next run.

If the invoice itself is wrong, use the normal cancellation and amendment process. Do not manually delete recognition ledger entries. A credit note, cancellation, or amended invoice may need corresponding deferred processing and verification.

## Video

<iframe src="https://www.youtube.com/embed/j6mx-EHU4aY" title="Deferred Revenue in ERPNext" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0"></iframe>

## Troubleshooting


| Problem                                              | What to check                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Full amount appears in income immediately            | Confirm the row has Enable Deferred Revenue, a deferred liability account, and valid service dates |
| No recognition entry appears                         | Check automatic processing, the date range, background jobs, and Draft generated Journal Entries   |
| Monthly amounts are unequal                          | Check whether Accounts Settings uses Days rather than Months                                       |
| Deferred report has a pending balance after the term | Check the processing end date, stop date, invoice status, and unsubmitted Journal Entries          |
| Income posts to the wrong account                    | Review the Income Account on the Sales Invoice Item row                                            |


## FAQs

### Is deferred revenue the same as a Customer advance?

No, a Customer advance is money received before allocation to an invoice. Deferred revenue is an invoiced amount that has not yet been earned. The example account name may include “Customer Advances,” but the underlying concepts and workflows remain different.

### Can revenue be recognized before the Customer pays?

Yes, payment status and revenue recognition are separate. ERPNext follows the service period for recognition and the invoice allocation for receivables.

### Can different invoice lines use different service periods?

Yes, configure deferred revenue and dates on each Item row.

### Why are recognition Journal Entries Draft?

Journal Entry posting is enabled while automatic submission is disabled. Review and submit the generated entries before expecting them in the General Ledger.

### Does deferred revenue defer tax too?

Not automatically. Taxes follow their configured tax and accounting rules. Confirm the required jurisdictional treatment with your accountant.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Sales Invoice](/erpnext/sales-invoice)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__delete-entries-linked-with-gl-entries.md -->
---
title: "Delete entries linked with GL entries"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-entries-linked-with-gl-entries"
updated: "2026-08-14"
---

ERPNext prevents Nova Industries from deleting a cancelled invoice because its accounting and stock ledger rows form part of the audit trail. Deleting a transaction is different from cancelling it, and should be rare. First decide whether you only need to reverse the business effect, which cancellation already does.

## Before enabling deletion

- Confirm the document is cancelled and no statutory or audit rule requires it to remain.
- Take a backup and test in a non-production environment.
- Understand that deleting ledger rows reduces traceability and may allow the naming series number to be reused depending on configuration.

## Enable the setting

1. Open **Accounts Settings**.
2. Find **Delete Accounting and Stock Ledger Entries on deletion of Transaction**.
3. Enable it, save, and reload.
4. Delete only the intended cancelled document.
5. Disable the setting again if it was approved for a one-time cleanup.

![Accounts Settings option for deleting linked accounting and stock ledger entries](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-delete-linked-ledger-setting.png)



## Troubleshooting

### The document is still linked

Open the document’s links and identify dependent records, allocations, returns, or amendments. Remove or resolve dependencies in the correct business order. Do not delete database rows directly.

## Frequently asked questions

### Should I delete an incorrect submitted invoice?

Normally cancel and amend it. That preserves the original document, its reversal, and the correction for audit.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__delete-submitted-document.md -->
---
title: "Delete Submitted Document"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-submitted-document"
updated: "2026-03-04"
---

To delete a submitted document, you need to cancel it first. Following are the steps to delete a submitted document.

These steps assume that you have the appropriate permissions on the document that you wish to cancel and delete.

#### Step 1: Cancel Submitted Document

You will find the 'Cancel' button on upper right corner of submitted document.

![Screenshot 2023-12-27 at 12.24.48 PM](/files/Screenshot 2023-12-27 at 12.24.48 PM.png)  


#### Step 2: Delete the document

On cancellation of the submitted document, the 'Amend' button becomes visible with the document status set to 'Cancelled'. This means that the document has been cancelled successfully.

To delete the document, now click on Menu, then Delete. This will delete the selected document.

![Screenshot 2023-12-27 at 12.39.59 PM](/files/Screenshot 2023-12-27 at 12.39.59 PM.png)  


**Note:** To delete multiple submitted documents in one go, you can select them in the list view and proceed to cancel and delete.

![Screenshot 2023-12-27 at 12.34.25 PM](/files/Screenshot 2023-12-27 at 12.34.25 PM.png)  


If your document is linked with other documents, then you will need to cancel dependent document before trying to delete the parent document.

![Screenshot 2023-12-27 at 12.37.51 PM](/files/Screenshot 2023-12-27 at 12.37.51 PM.png)  


All deleted documents disappear from the respective DocType but can be seen in 'Deleted Documents'. They can either be deleted permanently or restored.

![Screenshot 2023-12-27 at 12.53.50 PM](/files/Screenshot 2023-12-27 at 12.53.50 PM.png)  


The restored documents are indicated in Deleted Documents.

![Screenshot 2024-08-26 at 4.53.00 PM](/files/Screenshot 2024-08-26 at 4.53.00 PM.png)  


  

<!-- page: erpnext/erpnext__delete_company_transactions.md -->
---
title: "Delete Company Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete_company_transactions"
updated: "2026-03-12"
---

ERPNext allows you to delete all the transactions like Sales Invoices, Sales Order, Payment Entries etc associated with a company, while keeping the master data intact.



Often, users setup all the master data and then create a few dummy records to test/explore the system. Then, they want to delete the dummy records and start over again.

### Transaction Deletion Record

---

This feature allows you to delete all the records associated with a specified company, except for the ones belonging to the DocTypes listed in the **Excluded DocTypes** table.

If you really want to wipe out the transactions, then follow these steps. However, the deleted transactions can't be restored.

1. Create a new "Transaction Deletion Record" document.
2. Enter the name of the Company whose records you wish to delete.
3. Modify the "Excluded DocTypes" table if needed.
4. Save and Submit.

![](/files/imageaf22f8.png)

The **Summary** table displays the names of the DocTypes whose records were deleted as well as the number of records that were deleted.



## Delete Transactions

---

1. Go to **Home > Accounting > Company** and find your company.
2. On the top right, you'll find the **Delete Transactions** button under **Manage**.
3. Enter your password.
4. Enter the company name to confirm.

![](/files/imagef7bec2.png)

This will submit a record in the Transaction Deletion Record DocType.

:::note
To perform this action, the user must have the role of System Manager.
:::

<!-- page: erpnext/erpnext__deleting-all-transactions-for-the-company.md -->
---
title: "Deleting all transactions for the Company while retaining masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-all-transactions-for-the-company"
updated: "2026-07-02"
---

Use **Delete Transactions** on the Company form when you want to remove transactions for a company while keeping the company setup and master data. This is useful after testing, demo data entry, or sample imports when you want to start entering live transactions without recreating all masters.

This action clears transactional data for the selected company. It does not delete masters such as Company, Customer, Supplier, Item, Account, Warehouse, Cost Center, or other setup records.

## Before You Begin

- Take a full backup before deleting transactions. This action is destructive and should be treated as irreversible unless you restore from backup.
- Use this only when you are sure the selected company's transactions are no longer required.
- Check that users are not creating or submitting new transactions for the company while the deletion is running.
- If the company has been used for live accounting, export the required ledgers and reports before deleting data.
- Make sure you are logged in as a user with permission to delete company transactions.

## What Gets Deleted

ERPNext deletes transactional records linked to the selected company. This can include accounting, stock, buying, selling, payment, manufacturing, and other transaction documents that belong to that company.

The exact records depend on the modules used in your site and the transactions created for the company.

## What Is Not Deleted

Master and setup records are retained. For example, the following records are not deleted just because company transactions are deleted:

- Company
- Customer
- Supplier
- Item
- Account
- Warehouse
- Cost Center
- Territory, Customer Group, Supplier Group, and Item Group

This lets you keep the structure of the company and reuse the same masters after the transactions are cleared.

## Delete Transactions for a Company

### Step 1: Open the Company list

Search for **Company** from the Desk search bar, or open the Company list from the Accounting workspace.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 2: Open the company record

Select the company whose transactions you want to delete. Check the company name carefully before continuing.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 3: Choose Delete Transactions

On the Company form, open **Manage** and click **Delete Transactions**.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 4: Verify your password

ERPNext asks you to verify your password before continuing. Enter your password and click **Verify** only when you are certain you have selected the correct company and have a backup.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

After verification, ERPNext starts deleting the selected company's transactions. Do not close the site or create new transactions for the company while the deletion is in progress.

## After Deletion

- Open key transaction lists, such as Sales Invoice, Purchase Invoice, Payment Entry, Journal Entry, Stock Entry, and Sales Order, and confirm that the company's transactions are removed.
- Check accounting and stock reports for the company to make sure balances are cleared as expected.
- Review retained masters such as Customers, Suppliers, Items, Accounts, and Warehouses before creating new transactions.
- If you plan to start fresh accounting, verify opening balances, stock balances, and fiscal year settings before entering new documents.

## When To Use This

Use this tool when you want to preserve setup and masters but remove transaction history for one company. Common examples include demo data cleanup, testing cleanup, and preparing a configured company for live use.

## When Not To Use This

- Do not use this as a routine data cleanup tool for live companies.
- Do not use it when you only need to cancel or reverse a few specific transactions.
- Do not use it if you need an audit trail of the deleted transactions inside the same site.
- Do not use it without a backup that you know can be restored.

## Common Issues

- **Transactions are still visible:** Check whether those records belong to another company, or whether they are master records rather than transactions.
- **Balances are not cleared:** Recheck linked transactions and reports for the selected company. Also verify whether opening balances or stock balances were entered separately.
- **Permission error:** Your user may not have permission to run the deletion tool. Ask a System Manager or Administrator to review your access.
- **Wrong company selected:** Stop immediately and restore from backup if transactions were deleted for the wrong company.

## Recommended Practice

Before using this on an important site, restore a recent backup on a test site and run the deletion there first. Review the result, confirm that the required masters remain, and then repeat the process on the main site only when you are confident about the outcome.

<!-- page: erpnext/erpnext__deleting-custom-reports.md -->
---
title: "Deleting Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-custom-reports"
updated: "2026-03-04"
---


ERPNext has several [types of reports](/erpnext/making-custom-reports) which can be customized as per the users' requirement.

If there is a custom report which needs to be deleted, it can be achieved by following steps. Please note that its applicable only for the Custom Reports, and not for the standard reports.

#### Step 1: Go to Report List

In the Awesome Bar, type and select "Report List" for an option.

![Report Search](/files/customize-deleting-reports-1.png)

#### Step 2: Delete the Report from the List

The Report List will have all the standard and custom reports of your account. You can select Custom Report to be deleted from the list itself, and click on Delete icon in the Actions Menu.

![Report List](/files/customize-deleting-reports.png)

Or you can open that report, and delete it from File menu.

![Report Delete](/files/customize-deleting-reports-2.png)

<!-- page: erpnext/erpnext__delivery-note-stock-error.md -->
---
title: "Delivery Note Negative Stock Error\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-note-stock-error"
updated: "2026-02-26"
---


**Question**: When submitting a Delivery Note, receiving a message says that item's stock is insufficient, but we have item's stock available in the Warehouse.

**Answer**: On submission of Delivery Note, stock level is checked as on Posting Date and Posting Time of a Delivery Note. It's possible that you have stock of an Item available in the Warehouse. But if you are creating back-dated Delivery Note, and if item was not available in the warehouse on the Posting Date and Posting Time of Delivery Note, you are likely to receive an error message on the negative stock. You can refer to the Stock Ledger report to confirm the same.

If this is the case, you should edit the Posting Date and Time of a Delivery Note, and ensure that it is after the Posting Date and Time of item's receipt entry.

<!-- page: erpnext/erpnext__delivery-note.md -->
---
title: "Delivery Note\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-note"
updated: "2026-02-26"
---

**A Delivery Note is made when a shipment is shipped from the company’s Warehouse to the customer.**

A copy of the Delivery Note is usually sent with the transporter. The Delivery
Note contains the list of Items that are sent in the shipment and updates the
inventory. The Delivery Note is an optional step and a Sales Invoice can be created directly from a Sales Order.

To access the Delivery Note list, go to:

> Home > Stock > Stock Transactions > Delivery Note

![Delivery Note flow](/files/delivery-note-flow.png)

## Prerequisites

Before creating and using a Delivery Note, it is advised that you create the following first:

- Sales Order

> Note: From version-13 onwards we have introduced immutable ledger which changes the rules for cancellation of stock entries and posting backdated stock transactions in ERPNext. Learn more here.

## How to create a Delivery Note

The entry of the Delivery Note is very similar to a Purchase Receipt. It is usually created from a “Submitted” Sales Order (that is not shipped) by clicking on Create > Delivery.

To create a Delivery Note manually (not recommended), follow these steps:

1. Go to the Delivery Note list, click on New.
2. The Customer and Item details can be fetched by clicking on 'Get Items from > Sales Order'.
3. The UOM and Rates will be fetched automatically.
4. Save and Submit.
  Delivery Note

To fetch Items from a Sales Order, click on Get Items from > Sales Order. This will open a popup from where you can search for Sales Orders and select one.

You will notice that all the information about unshipped Items and other details are carried over from your Sales Order if you create the Delivery Note from there.

You can also edit the posting date and time, the current date and time are set when you create the Delivery Note.

### Statuses

These are the statuses a Delivery Note can be in:

- **Draft**: A draft is saved but yet to be submitted to the system.
- **To Bill**: Yet to be billed using a Sales Invoice.
- **Completed**: Submitted and sent all the Items.
- **Return Issued**: All the Items have been returned.
- **Cancelled**: Cancelled the Delivery Note.
- **Closed**: The purpose of the Close is to manage short-closing. For example, your Customer ordered for 20 qty but closed at 15 qty. The remaining 5 is not to be sent or billed.

### Partial Deliveries

When you create a Delivery Note from a Sales Order, the quantities can be changed. So if the Sales Order contains 10 Items to be delivered and you're delivering only 5 this week and the remaining next week, then you can create 2 Delivery Notes in two weeks.

### From Pick List

You can create Delivery Notes in bulk, from Pick Lists also. From a submitted Pick List, click on Create -> Delivery Note. 

![](/files/image81aab7.png)

This would create separate Delivery Notes for Sales Orders, grouped by Customer.
If a Pick List Item is not linked to a Sales Order(added manually by user), a separate DN would be created for all those items as well.

## Related Actions

### Customer Purchase Order Details

You can enter the Customer's Purchase Order number here for Reference.

### Address and Contact

- **Shipping Address**: The Customer's address where the Items will be shipped.
- **Contact Person**: If the Customer is an organization, add the Contact person in this field.

For India, the following details can be added for GST:

- Customer GSTIN
- Place of Supply
- Billing Address GSTIN
- Company GSTIN
- Company Address Name

Contacts and Addresses are stored separately so that you can attach multiple Contacts or Addresses to the customer.

### Currency and Price List

You can set the currency in which the Deliver Note is to be sent. This is usually fetched if set in the Sales Order. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Read about Price Lists
and Multi-Currency Transactions
to know more.

### Warehouses

- **Set Source Warehouse**: This is where the Items will be sourced from to send to the Customer.
- **To Warehouse**: In a regular Sales scenario, the Item exits your Warehouse and reaches the Customer. However, if you wish to retain sample stock, enter a Warehouse here.

### Items Table

- **Barcode**: You can track Items using barcodes.
- The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.
- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for tracking items using barcode to know more.
- **Discount and Margin**: You can apply a discount on individual Items percentage-wise or the total amount of the Item. Read Applying Discount for more details.
- **Rate**: The Rate is fetched if set in the Price List and the total Amount is calculated.
- **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit this page.
- The Item Weight details per unit and Weight UOM are fetched if set in the Item master.
- **Warehouse and Reference**: The Warehouse from which the Items are sent to the Customer is shown. Also, a Sales Order will be shown if this Delivery Note was the creation flow: 'Sales Order > Deliver Note'.
- **Batch No and Serial No**: If your Item is serialized or batched, you will have to enter Serial Number and Batch in the Items table. You are allowed to enter multiple Serial Numbers in one row (each on a separate line) and you must enter the same number of Serial Numbers as the quantity.

 The 'Available Qty at From Warehouse', 'Available Batch Qty at From Warehouse', and 'Installed Qty' will be shown. To know more about installation, visit the Installation Note page.

 **Note**: The Item has to be serialized or batched for these features to work. If the Item is serialized a popup will appear where you can enter the Serial Numbers.

- Expense Account is the account from which the amount will be debited. Ticking on 'Allow Zero Valuation Rate' will allow submitting the Delivery Note even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.
- Accounting Dimensions help to tag each transaction with different Dimensions without the need for creating new Cost Centers. You need to create Accounting Dimensions first, to know more, visit this page.
- **Page Break** will create a page break just before this Item when printing.

### Tracking Quality Inspection

If for certain Items, it is mandatory to record Quality Inspections (if you have set it in your Item master), you will need to update the “Quality Inspection" field. The system will only allow you to “Submit” the
Delivery Note if you update the “Quality Inspection”.

After enabling Inspection Criteria in the Item form for Sales and attaching a Quality Inspection Template there, Quality Inspections can be recorded in Delivery Notes.

### Taxes and Charges

The Taxes and Charges will be fetched from the Sales Order.

Visit the Sales Taxes and Charges Template page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit this page.

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the Shipping Rule page.

### Additional Discount

Any additional discounts to the whole order can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.
Read Applying Discount for more details.

### Terms and Conditions

In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, click here

### Transporter Information

If you outsource transporting Items to their delivery location, the transporter details can be added. This is not the same as drop shipping.

- **Transporter**: The Supplier who will transport the Item to your Customer. The transporter feature should be enabled in the Supplier master to select the Supplier here.
- **Driver**: You can add a Driver here who will drive the mode of transport.

![](/files/transportation.png)

The following details can be recorded:

- Distance in km
- Mode of Transport whether road, air, rail, or ship.

For India, GST:

- GST Transporter ID
- Transport Receipt No
- Vehicle No
 The GST Vehicle Type can be changed

The Transport Receipt Date and Driver Name will be fetched.

### More Information

The Delivery Note can be linked to the following for tracking purposes:

- Project
- Campaign
- Source

### Printing Settings

#### Letterhead

You can print your Delivery Note on your company's letterhead. Know more here.

'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more here.

There are additional checkboxes for printing the Delivery Note without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.

### Status

The status of the document and installation percentage is shown here. Any additional instructions for delivery can be entered here.

### Commission

If the sale took place via one of your Sales Partners, you can add their commission details here. This is usually fetched from the Sales Order.

### Sales Team

**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal.

This is usually fetched from a Sales Order, for example:

![](/files/image71a4c0.png)

### Shipping Packets or Items with Product Bundle

If you are shipping Items that have a Product Bundle, ERPNext will automatically create a “Packing List” table for you based on the sub-Items in that Item.

If your Items are serialized, then for Product Bundle type of Items, you will have
to update the Serial Number in the “Packing List” table.

### Packing Items into Cases, for Container Shipment

If you are doing making the delivery via container shipment or by weight, then you can use the Packing
Slip to break up your Delivery Note into smaller units. To know more about a Packing Slip, visit this page.
go to:

You can create multiple Packing Slips for your Delivery Note and ERPNext will
ensure that the quantities in the Packing Slip do not exceed the quantities in
the Delivery Note. Note that you can create a Packing Slip from a Delivery Note only when the Delivery Note is in the Draft stage.

### After Submitting

When the Delivery Note is submitted, a Stock Ledger Entry is made for each Item and stock is updated. Pending
Quantity in the Sales Order is updated (if applicable).

The Dashboard will show the following options:

- Installation Note
- Sales Return
- Delivery Trip
- Sales Invoice
  ![](/files/image4843aa.png)

> Tip: To disallow the creation of Delivery Notes without a Sales Order against it:

### Returning a Sales Order

Once you've delivered a Sales Order using a Delivery Note, you can create a return entry in case the Customer returns the Item. To know more, visit the Sales Return page.

### Skipping Delivery Note

If you don't want to create a Delivery Note after a Sales Order and directly want to create a Sales Invoice, enable the feature for it in Selling Settings.

### Related Topics

1. Warehouse
2. Delivery Note Stock Error
3. Material Transfer From Delivery Note and Purchase Receipt
4. Installation Note
5. Delivery Trip

<!-- page: erpnext/erpnext__delivery-trip.md -->
---
title: "Delivery Trip\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-trip"
updated: "2026-02-27"
---


**A Delivery Trip records Customer Deliveries in one vehicle.**

Multiple stops can also be added and Submitted Delivery Note can be tagged per Customer.

## 1. How to create a Delivery Trip
A Delivery Trip can be created from a [Delivery Note](/erpnext/delivery-note) by clicking on 'Create > Delivery Trip'.

1. Go to: **Stock > Stock Transactions > Delivery Trip > New**
1. Select the Driver and Vehicle, create both if not present.
1. Set the date, departure date and time.
1. Add customers for delivery stops, the address will be fetched if already set. Customers can also be fetched by clicking on 'Get customers from > Delivery Note'. Additional Delivery Stops can be added by clicking on the Add Row button before submitting:

 ![Delivery](/files/delivery_stops.png)

1. Save and submit.

 ![Delivery](/files/delivery_trip.png)

## 2. Features
### 2.1 Calculate Estimated Arrival Times
If the Customer address and the Driver address are set, you can calculate the estimated arrival time for the deliveries. This data is fetched from Google Maps.

### 2.2 Optimize Route
Using Google Maps, the best route for the deliveries will be calculated.


### Related Topics
1. [Packing Slip](/erpnext/packing-slip)
1. [Shipping Rule](/erpnext/shipping-rule)

<!-- page: erpnext/erpnext__demand-driven-forecasting.md -->
---
title: "Forecasting Using Exponential Smoothing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/demand-driven-forecasting"
updated: "2026-03-02"
---

To access the Forecating Report, go to:

> Home > Manufacturing > Reports > Forecasting

![Production Forecasting](/files/production-forecasting-using-sales-order.png)  


Using exponential smoothing method and past Sales Order / Delivery Note / Quotation data, the forecasting will be calculated. The exponential smoothing method formula is as below:

![Production Forecasting](/files/exponential-smoothing-formula041d6b.png)  


Using exponential smoothing method, system predicts the forecasting for each period and same forecast data will be used to forecast the upcoming period data.

How does the exponential smoothing method works
-----------------------------------------------

![Production Forecasting](/files/exponential-smoothing-formula-e.png)  


For the above example, we have used one-year sales order data every month. The first-month forecast will be calculated based on the average of all total orders. From the second month onward, the difference between the last month's Total Order and Forecast Value will be multiplied with the Smoothing Constant Value (in between 0 to 1). The default value of the Smoothing Constant is 0.3 which gives efficient forecasting data. The last month's Total Order and Forecast Value difference called forecasting error and this error will be added in the same month of forecast value to calculate the forecast of the next month.

How do the filters work
-----------------------

1. **Company** :- user can do forecasting for the specific company by applying the company filter
2. **From Date and To Date** :- for this period system will do the forecasting, the default from date is the current date and to date will be the one year ahead date from the current date.
3. **Based On Document** :- by default system uses sales order past data to forecast. User can select the other document like delivery note / quotation to forecast the data.
4. **Based On** :- based on quantity / amount system shows the forecast data.
5. **Based On Data ( in years )** :- for forecasting requires past data, this filter helps system to check past data for number of years.
6. **Periodicity** :- forecasting data can be viewed in Monthly / Quarterly / Half-Yearly / Yearly basis, the old forecast data can not be displayed for Monthly period for better view.
7. **Smoothing Constant** - the Smoothing Constant will be used to forecast the data, the value should be between 0 and 1.
