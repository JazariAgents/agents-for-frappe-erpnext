<!-- Frappe documentation: erpnext, part 12 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__process-deferred-accounting.md -->
---
title: "Process Deferred Accounting | ERPNext Documentation"
description: "Run and verify ERPNext deferred income or expense recognition manually, with date ranges, account filters, processing logs, and ledger checks."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/process-deferred-accounting"
updated: "2026-08-03"
---

Process Deferred Accounting runs recognition for eligible deferred revenue or deferred expense schedules. Each submitted process record is also a log of the run.

ERPNext can create these records automatically through a background job. Create one manually when automatic processing is disabled, a scheduled run was missed, or you need a controlled run for a specific date range or deferred account.

This tool does not create deferred schedules by itself. The schedules come from submitted [Sales Invoice](/erpnext/sales-invoice) or [Purchase Invoice](/erpnext/purchase-invoice) rows whose [Item](/erpnext/item) and transaction settings enable deferred accounting, specify a deferred account, and provide valid service dates.

## Before you begin

Confirm:

- [Deferred Revenue](/erpnext/deferred-revenue) or [Deferred Expense](/erpnext/deferred-expense) is configured.
- The Item and invoice row have the applicable deferred option enabled.
- The deferred account and final income or expense account are correct.
- The Sales Invoice or Purchase Invoice is submitted.
- The service start and end dates cover the period you intend to process.
- [Accounts Settings](/erpnext/accounts-settings) reflect the approved day/month and direct/Journal Entry policy.

If Journal Entry posting is enabled but automatic submission is disabled, generated [Journal Entries](/erpnext/journal-entry) will remain Draft and will not affect the General Ledger until reviewed and submitted.

## Create a processing run

Go to **Accounting &gt; Deferred Accounting &gt; Process Deferred Accounting**, then select **New**.

The list contains automatic and manual processing logs. Review recent records before creating another run so you understand what was already processed.



![Process Deferred Accounting list](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-process-deferred-accounting-list.png)

Complete the fields:


| Field              | What it controls                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| Company            | Limits processing to one Company and its accounting records                                                    |
| Type               | Select **Income** for deferred revenue or **Expense** for deferred expense                                     |
| Account            | Optional [Chart of Accounts](/erpnext/chart-of-accounts) filter that limits processing to one deferred account |
| Posting Date       | Date used for the recognition posting or generated Journal Entry                                               |
| Service Start Date | Beginning of the service period to evaluate                                                                    |
| Service End Date   | End of the service period to evaluate                                                                          |


For deferred revenue, select **Income**. The example limits processing to **Customer Advances - NET**.



![Manual deferred-income processing run](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-process-deferred-income.png)

For prepaid costs, select **Expense** and use the applicable deferred asset account, such as **Prepaid Expenses - NET**.



![Manual deferred-expense processing run](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-process-deferred-expense.png)

Use the Account filter when you deliberately want a narrow run. Leave it blank when all eligible deferred accounts for the Company and date range should be processed.

## Choose the dates carefully

The service date range decides which eligible invoice schedules the run evaluates. The posting date decides when the recognition effect appears in the ledger.

For a month-end run, the service range normally covers the period being recognized and the posting date normally falls in that accounting period. Follow your organization's closing policy.

Do not use a future posting date merely to make a missing entry appear. First confirm whether the prior run, invoice dates, and service period were correct.

## Save and submit

Save the document and review all fields. Submission starts the processing behavior. Depending on Accounts Settings, ERPNext either:

- posts the recognition directly to the General Ledger; or
- creates Journal Entry documents.

When Journal Entries are created, **Submit Journal entries** determines whether they are submitted automatically. Draft Journal Entries provide a review gate but leave the recognition unposted until someone submits them.

The original documentation correctly described Process Deferred Accounting as a log created on every processing run. Retain the submitted process document for audit instead of treating it as a disposable utility record.

## What the run processes

ERPNext looks for eligible submitted invoices whose deferred Item rows overlap the selected service range and match the Company, Type, and optional Account filter. It calculates the portion allowed by the service dates and the **Days** or **Months** basis.

For Income:


| Debit                      | Credit                                     |
| -------------------------- | ------------------------------------------ |
| Deferred Revenue liability | Income Account from the Sales Invoice Item |


For Expense:


| Debit                                       | Credit                 |
| ------------------------------------------- | ---------------------- |
| Expense Head from the Purchase Invoice Item | Deferred Expense asset |


The tool should not recognize an amount twice. ERPNext uses prior processing and recognized amounts to determine what remains. If a repeated run produces an unexpected result, stop and review the underlying documents and earlier logs.

## Verify the completed run

After submission:

1. Check whether Journal Entries were generated and whether they are Draft or Submitted.
2. Run the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report) for the Company and period.
3. Open the [General Ledger](/erpnext/general-ledger) for the deferred account and final income or expense account.
4. Compare the recognized amount with the service days or months included in the run.
5. Confirm that the pending amount and remaining service period are reasonable.

If the process creates a Draft Journal Entry, the report and ledger may not show the final recognition until that Journal Entry is submitted.

## Automatic processing

Enable **Automatically process deferred Accounting entry** in Accounts Settings when ERPNext should run the process through scheduled background jobs.

Automatic processing reduces month-end manual work, but it still requires monitoring. Confirm that the scheduler is active, processing logs are being created, generated Journal Entries are handled, and the deferred report agrees with the ledger.

Manual processing is useful for controlled cutoffs, recovery after a scheduler interruption, or a filtered run. It should not become a substitute for fixing background-job failures.

## Corrections

If a run is wrong, first identify the source:

- incorrect service dates or stop date on the invoice row;
- wrong deferred or income/expense account;
- wrong Days/Months policy;
- incorrect process range or posting date;
- generated Journal Entries left Draft;
- cancelled or amended source invoice;
- a prior run already covering the same period.

Correct the source through the supported workflow. Do not delete General Ledger entries or force a balancing Journal Entry without understanding the deferred schedule.

## Troubleshooting


| Problem                                         | What to check                                                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| No entries were generated                       | Verify submitted eligible invoices, service overlap, Type, Company, Account filter, and pending deferred amount |
| Journal Entries exist but ledger did not change | Check whether the generated documents are still Draft                                                           |
| Only one account was processed                  | Check whether the optional Account filter was set                                                               |
| Amount differs from a simple monthly division   | Check whether processing is based on Days or includes a partial month                                           |
| Automatic runs are missing                      | Check the Accounts Setting, scheduler, background jobs, and error logs                                          |


## FAQs

### Should I create this document every month?

Not when automatic processing is enabled and working. Use manual records for controlled processing, recovery, or deliberate account/date filtering.

### What is the difference between Posting Date and Service End Date?

Service End Date limits the service period evaluated. Posting Date determines when the resulting accounting entry is recorded.

### Can one run process both revenue and expense?

No, select either Income or Expense. Use separate runs when both sides require manual processing.

### Does submitting the process always create a Journal Entry?

Only when Accounts Settings enables Journal Entry posting. Otherwise ERPNext posts the recognition directly.

### Why does a repeated run not post the same amount again?

ERPNext considers the amount already recognized and processes only the eligible remainder. Verify the prior logs and deferred report if the result is unexpected.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Revenue](/erpnext/deferred-revenue)
- [Deferred Expense](/erpnext/deferred-expense)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Accounts Settings](/erpnext/accounts-settings)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__process-payment-reconciliation-tool.md -->
---
title: "Process Payment Reconciliation Tool | ERPNext Documentation"
description: "Run queued payment reconciliations and monitor their results in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/process-payment-reconciliation-tool"
updated: "2026-08-14"
---

Use the Process Payment Reconciliation Tool when you have several submitted payments and invoices that ERPNext can match for the same party and account. You define the scope once, queue the process, and review the completed allocations.



This example uses **Northstar Retail**. The customer has an unallocated payment of **USD 600** and an outstanding sales invoice of **USD 3,753**.

## Before you begin

Confirm that the payments and invoices are submitted, use the same Company and party account, and have an amount available to reconcile.

Open **Accounts Settings**, select the **Payments** tab, enable **Auto reconcile Payments**, and save. The job trigger controls how often queued work is picked up. The queue size controls how many documents are processed in each run.

![Auto reconcile Payments enabled in the Payments tab of Accounts Settings](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-05-enable-auto-reconciliation-v3.png)

## Create and run a reconciliation process

### 1. Open the tool

Open **Process Payment Reconciliation** and click **Add Process Payment Reconciliation**.

![Process Payment Reconciliation list with the add action highlighted](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-01-open-process-payment-reconciliation-v3.png)

### 2. Define the scope

Select the **Company**, **Party Type**, **Party**, and **Receivable/Payable Account**. Add date, Cost Center, or Bank/Cash Account filters when you need to narrow the eligible entries.

In this example, select **Nova Electronics Trading**, **Customer**, **Northstar Retail**, **Debtors - NET**, and **Nova Operating Bank - NET**.

![Process Payment Reconciliation configured for Northstar Retail](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-02-select-party-and-account-v3.png)

### 3. Save and submit

Save the record, review the scope, and click **Submit**. Submitting places the process in the queue. It does not itself confirm that every entry was reconciled.

![Saved Process Payment Reconciliation with Submit highlighted](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-03-save-and-submit-process-v3.png)

### 4. Start the queued process

When the status is **Queued**, click **Start / Resume** to begin processing immediately.

![Queued reconciliation process with Start or Resume and the status highlighted](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-04-start-queued-reconciliation-v3.png)

### 5. Monitor progress

Keep the record open while ERPNext processes the eligible entries. The progress area, reconciliation log count, and **Running** status show that the job is active.

![Running reconciliation process with progress and reconciliation log](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-06-monitor-reconciliation-progress-v3.png)

### 6. Review the completed process

Wait for the status to become **Completed**. In this example, ERPNext processed **2/2** eligible entries.

![Completed reconciliation process showing two of two entries processed](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-07-review-completed-reconciliation-v3.png)

### 7. Verify the accounting result

Open the affected Payment Entry or invoice and verify the allocation. Payment Entry **ACC-PAY-2026-00006** now contains a USD 600 reference to **ACC-SINV-2026-00008**. Its **Unallocated Amount** is USD 0, and the invoice outstanding amount is USD 3,153.

![Payment Entry showing the invoice reference, allocated amount, and zero unallocated amount](https://novacompanies.m.frappe.cloud/files/docs-process-payment-reconciliation-08-verify-payment-allocation-v3.png)

## Important fields and what they mean


| Field                         | What it controls                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------- |
| Company                       | Company whose receivable or payable entries are included.                        |
| Party Type                    | Whether the process is for a Customer or Supplier.                               |
| Party                         | Customer or Supplier whose entries are evaluated.                                |
| Receivable/Payable Account    | Party account that must match the eligible invoices and payments.                |
| Default Advance Account       | Limits the process to Payment Entries made against the selected advance account. |
| Invoice Date and Payment Date | Optional ranges that narrow the documents included.                              |
| Cost Center                   | Optional filter for entries assigned to a specific Cost Center.                  |
| Bank/Cash Account             | Optional filter for payments made through a specific bank or cash ledger.        |
| Status                        | Shows whether the process is Queued, Running, Paused, Completed, or failed.      |


## Troubleshooting

### The process remains queued

Enable **Auto reconcile Payments** in the Payments tab of Accounts Settings. Then return to the submitted process and click **Start / Resume**. Also confirm that background jobs are running on the site.

### The process finds no eligible entries

Check the Company, Party Type, Party, receivable or payable account, date range, Cost Center, and Bank/Cash Account. The source invoices and payments must be submitted. The payment must still have an unallocated amount, and the invoice must still have an outstanding amount.

### The process completes but an expected payment is unchanged

Open the reconciliation log and compare the payment with the process filters. Check the party, currency, account, posting dates, and remaining amounts. Use [Payment Reconciliation](/erpnext/payment-reconciliation) when the match needs manual judgment.

### A process is paused or interrupted

Correct the underlying data or background-job issue, then use **Start / Resume**. Review the existing log and current outstanding amounts before rerunning the same scope.

## Frequently asked questions

### How does this differ from Payment Reconciliation?

Process Payment Reconciliation handles eligible entries automatically for a defined scope. Payment Reconciliation lets you manually select exact payments, invoices, and allocation amounts for one party.

### Does submitting the process change the ledger immediately?

Submission queues the process. Review the status, progress, reconciliation logs, Payment Entry references, and outstanding amounts before treating the work as complete.

### Can I restrict the process to one bank account or date range?

You can use the Bank/Cash Account and invoice or payment date filters before saving the process.

### Does the tool import bank transactions?

The tool does not import bank transactions. It allocates existing accounting entries. Use [Bank Transaction](/erpnext/bank-transaction) and [Bank Reconciliation](/erpnext/bank-reconciliation) for statement import and bank matching.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Unreconcile Payment](/erpnext/unreconcile-payment)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)

<!-- page: erpnext/erpnext__process-statement-of-accounts.md -->
---
title: "Process Statement Of Accounts | ERPNext Documentation"
description: "Generate, download, and email customer account statements and ageing summaries in bulk with ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/process-statement-of-accounts"
updated: "2026-07-31"
---

Use **Process Statement Of Accounts** to generate and send account statements to several customers at once. Each customer receives a PDF based on the General Ledger, with an optional ageing summary. You can send the statements immediately or schedule them weekly, monthly, or quarterly.

## Before you begin

- Configure an outgoing [Email Account](/framework/user/en/email/email-account).
- Add a billing email to each customer's [Contact](/erpnext/contact). If **Send To Primary Contact** is enabled, the customer also needs a primary contact email.
- Submit the transactions that should appear in the statement.

## Create a statement process

1. Search for **Process Statement Of Accounts** and select **Add Process Statement Of Accounts**.
2. Enter a recognizable **Name**.
3. Select the report and set the date, Company, account, currency, Cost Center, or Project filters.
4. Use **Categorize By** to control how entries are grouped in the PDF.

![Process Statement Of Accounts report filters](https://novacompanies.m.frappe.cloud/files/process-statement-of-accounts-statement-filters.png)

## Select customers

Add customers individually, or use **Select Customers By** to fetch customers from a Customer Group, Territory, Sales Partner, or Sales Person. The customer table displays the billing and primary email addresses that ERPNext will use.

If a customer cannot be added, check the Contact linked to that Customer. A billing email is required, and a primary email is required when **Send To Primary Contact** is selected.

## Configure the PDF and email


| Setting                   | Use                                                                   |
| ------------------------- | --------------------------------------------------------------------- |
| Orientation               | Choose Landscape for wider ledgers or Portrait for shorter statements |
| Include Ageing Summary    | Adds receivable ageing to the statement                               |
| Page Break After Each SoA | Keeps each customer's statement on a separate page                    |
| Enable Auto Email         | Sends statements on a schedule                                        |
| Sender                    | Outgoing email account used to send the message                       |
| PDF Name                  | File name shown to the customer                                       |
| Subject and Body          | Email content; both support Jinja values                              |


![Customer selection, print preferences, and email settings](https://novacompanies.m.frappe.cloud/files/process-statement-of-accounts-customer-email-settings.png)

Save the document. Use **Download** to review the consolidated PDF before sending. Use **Send Emails** for an immediate batch. Scheduled emails are queued by the background job at the configured frequency.

## What the customer receives

ERPNext creates a separate email and PDF for each customer. The PDF contains only that customer's ledger for the selected period. If **Include Ageing Summary** is enabled, the same PDF also shows how much is current and how much falls into each overdue bucket.

The example below shows the email composer with the customer-specific statement attached. This is a preview from the demo site. On a production site with an outgoing Email Account, **Send Emails** queues the message for delivery.



![Customer statement email preview](https://novacompanies.m.frappe.cloud/files/customer-email-preview.png)

The attached statement shows the opening balance, each invoice or payment in the selected period, and the closing balance. Its ageing summary groups the outstanding amount by due date so the customer can see what needs attention.



![Customer ledger and ageing summary](https://novacompanies.m.frappe.cloud/files/customer-ledger-and-ageing.png)

## Use dynamic values

You can personalize the subject and body with Jinja. For example:

```text
Statement of Account for {{ customer.customer_name }}

```

```text
Hello {{ customer.customer_name }},
Please find your statement from {{ doc.from_date }} to {{ doc.to_date }} attached.

```

Test the output with a small customer set before enabling automatic email for all customers.

## Troubleshooting

**A customer is missing from the selection**

Check the Customer's billing Contact and its email address. Also review the grouping filter used to fetch customers.

**The PDF is empty or incomplete**

Confirm the Company, date range, currency, and account filters. Only submitted ledger entries are included.

**Emails do not arrive**

Check the outgoing Email Account and the Email Queue. Scheduled messages are not sent when the document is merely saved; the background scheduler must be running.

## Related topics

- [Accounts Receivables](/erpnext/accounts-receivables)
- [Customer](/erpnext/customer)
- [Contact](/erpnext/contact)
- [General Ledger](/erpnext/general-ledger)
- [Email Account](/framework/user/en/email/email-account)
- [Sales Interest / Dunning](/erpnext/dunning)

<!-- page: erpnext/erpnext__procurement-cycle-overview.md -->
---
title: "Procurement Cycle Overview"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/procurement-cycle-overview"
updated: "2026-03-02"
---

For a beginner level understanding of the flow of process in the Procurement cycle, there are a total of 7 Stages:   
1. Material Request
2. Request For Quotation
3. Supplier Quotation
4. Purchase Order
5. Purchase Receipt
6. Purchase Invoice
7. Payment Entry

  
To begin with, considering the standard flow of the Purchase cycle, let's say you raise a **Material request** in ERPNext depending upon the item to be Purchased.   
Once a Material request is raised, there can be multiple cases like Multiple Suppliers bidding or selling same item, in this case a **Request for Quotation[RFQ]** is opened up.   
Once an RFQ is raised, suppliers post their rates against the required quantity against it. The rates from the different Suppliers can be sent by the users within ERPNext or even using the Web portal. Also, once quotations are received, they can be compared using **Supplier Quotation.** After comparing the best quote, a **Purchase Order** is raised against it. After a PO is raised, an **Invoice** can be generated or a **Purchase Receipt** depending upon the flow of process in the organisation, subsequently **Payment Entry** is made.   
   
  

<!-- page: erpnext/erpnext__procurement-tracker-report.md -->
---
title: "Procurement Tracker Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/procurement-tracker-report"
updated: "2026-03-02"
---


This report lists all the transactions related to goods that are currently in the process of procurement.

To access this report, go to:

> Home > Buying > Procurement Tracker

The procurement tracker allows a user to monitor the process of obtaining goods. It provides information about the user requesting the purchase, the warehouse it was requested from, along with the quantity of the requested item. It also provides a comparison between the estimated cost of the goods at the time of requisition versus actual cost of obtaining them along with the date at which the goods where obtained. This ensures reviewing, ordering, delivery, and billing management for goods involved in the procurement process.

![Procurement Tracker](/files/procurement_tracker.png)

<!-- page: erpnext/erpnext__product-bundle.md -->
---
title: "Product Bundle"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/product-bundle"
updated: "2026-02-27"
---

**A Product Bundle is a master where you can list existing items which are bundled together and sold as a set (or bundle).**

For instance, when you sell a smartphone, you need to ensure that the charger, cable, and sim ejector pin are delivered with it and stock levels of these items get affected. To address this scenario, you can create a Product Bundle for the main item, i.e. smartphone. Then list deliverable items i.e. smartphone + charger + cable + sim ejector pin as so-called "Child Items".

A Product Bundle can be seen as a "Bill-of-Materials" on the Sales side.

Following are the steps to set up a Product Bundle and using it in sales transactions.

To access product bundle, go to:


> Home > Selling > Items and Pricing > Product Bundle
> 
> 

1. Prerequisites
----------------

Before creating and using a Product Bundle, it is advised that you create the following first:

* [Item](/erpnext/item)

2. How to create a Product Bundle
---------------------------------

1. Go to the Product Bundle list, click on Add Product Bundle.
2. Select a Parent Item, create one if not already created. Make sure Maintain Stock unchecked when creating a Parent Item. eg: Dinner Set.
3. Enter a price for the parent item, this will be fetched when making a transaction.
4. You can enter a description for internal use.
5. Enter the products to be bundled in the Items table and enter their quantities.
6. Save.

![Screenshot 2024-08-29 at 11.41.56 AM](/files/Screenshot 2024-08-29 at 11.41.56 AM.png)  


### 2.1 Selecting Parent Item

In Product Bundle master, there are two sections. The "Parent Item" and a List of items to be shipped (Child Items).

The "Parent Item" should be seen more like a vessel or virtual item and not a physical product. The "Parent Item" must be a **non-stock item**. To create a **non-stock item** you have to unmark "Maintain Stock" in the Item Form. This is a non-stock item because there is no stock maintained for it but only for the "Child Items".

If you want to maintain stock for the Parent Item, then you must create a regular Bill of Material (BOM) and package them using Stock Entry Transactions.

### 2.2 Selecting Child Items

In the Items table, you have to list all the child items for which we maintain stock and is delivered to customer. Remember: The "Parent Item" is just virtual, so your main product (a smartphone in our example here) also has to be listed on the List of Child (or Package) Items.

3. Features
-----------

### 3.1 Product Bundle in the Sales Transactions

When making Sales transactions (Sales Invoice, Sales Order, Delivery Note) the Parent Item will be selected in the main item table.

![Screenshot 2024-08-29 at 11.42.41 AM](/files/Screenshot 2024-08-29 at 11.42.41 AM.png)  


On selection of a Parent Item in the main item table, its child items will be fetched in Packing List table of the transaction. If child item is the serialized item, you will be able to specify its Serial No. in packing List table itself. On submission of the transaction, the system will reduce the stock level of child items from warehouse specified in Packing List table.

![Screenshot 2024-08-29 at 11.44.47 AM](/files/Screenshot 2024-08-29 at 11.44.47 AM.png)  


**Use Product Bundle to Manage Offers/Schemes:**   
This was discovered when a customer dealing into nutrition products asked for a feature to manage offers like "Buy One Get One Free".

To manage the same, he created a non-stock item which was used as Parent Item. In description of item, he entered offer details with the item's image displaying the offer. The sellable product was selected in Package Item where qty was two. Hence every time they sold one qty of Parent item under this offer, the system deducted two quantities of product from Warehouse.

### 4. Related Topics

1. [Item](/erpnext/item)

<!-- page: erpnext/erpnext__product-listing.md -->
---
title: "Product Listing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/product-listing"
updated: "2026-03-02"
---

ERPNext provides a product listing page where your customers can discover your
products. It is enabled by default if you have published **Website Items** on your system.

You can go to the product listing visiting the **/all-products** route. For example,
`https://apple.erpnext.com/all-products`. 

> Actions are visible only on hovering over the card in the new Product Listing.

Here there are two views available that can be toggled:

### Product List View
The List View can hold additional data in it such as a short description which can be mentioned in the Website Item's **Short Website Description** field. 
![Product List View](/files/product-list-2.png)
*Product List View*

### Product Grid View
![Product Grid View](/files/product-grid.png)
*Product Grid View*

### Filters
This page also shows filters alongside the products. There are three types of filters visible here: **Field Filters**, **Attribute Filters** and **Discount Filters**.

- **Field Filters** and **Attribute Filters** can be configured in the [Filters and Categories](/erpnext/e_commerce_settings#filters-and-categories) section of **E Commerce Settings**.
- **Discount Filters** are automatically generated based on the discounts applied on the products. They do not require any configuration.

<!-- page: erpnext/erpnext__production-analytics.md -->
---
title: "Production Analytics\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-analytics"
updated: "2026-03-02"
---


To access the Production Analytics, go to:

> Home > Manufacturing > Reports > Production Analytics

![Task](/files/production-analytics.png)

This report shows the overall analytics of all Work Orders.

<!-- page: erpnext/erpnext__production-and-material-planning-capacity-planning.md -->
---
title: "Capacity Planning\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-and-material-planning-capacity-planning"
updated: "2026-02-26"
---

Capacity planning is the process in which an organization decides whether or not to accept the new orders based on the resources and existing work orders.

Capacity planning has been enabled by default in your account, to know more go to:

> Home > Manufacturing > Settings > Manufacturing Settings

![Work Order](/files/capacity_planning_settings.png)

## 1. Prerequisites

Before creating and using a Work Order, it is advised that you create the following first:

- Bill Of Materials
- Operation
- Workstation
- Work Order

## 2. How Capacity Planning Works in ERPNext

The user has to define the number of days in the "Capacity Planning For" field under manufacturing settings to plan the upcoming work orders. For example, if you have kept the Capacity Planning For 30 days and to make 1 finished good it requires 5 days then on the current date user can only accept the 6 work orders (30/5 = 6). You can take the next Work Order when your Workstation gets free.

### 2.1 Create Work Order With Operations

User needs to create the Work Orders with Operations so that the system will track the Job Card timings against the Work Order.

![Work Order](/files/work_order_with_operations.png)

Once the user submits the Work Order, system will generate the Job Card with the available Workstation's time details. If 'Allow Overtime' is disabled in Manufacturing Settings then the system schedules the job as per the timings defined in the Workstation. If "Allow Production on Holidays" is disabled then the system schedules job only on working days.

### 2.2 Workstation's Production Capacity

In the Workstation, the user can set the 'Production Capacity'. This is the number of Operations the system will allow you work on in this Workstation. For example, if a certain Workstation can handle 10 operations at the same time, enter the 'Production Capacity' as 10.

![Work Order](/files/work_station_capacity.png)

### 2.3 Job Card With Timing

The system will auto-create the Job Card with timing against each operation based upon the time required to complete that operation and Workstation's availability. The user has to set the planned start date and based on the operation time, system calculates the planned end date.

![Work Order](/files/job_card_timing.png)

### 2.4 Work Order Planned Start Date and End Date

Based on the planned start date and end date, users can calculate the capacity of their work stations. Also, they can track the status of the work order using the Calendar.

To view calendar, goto:

> Work Order List > Calendar > Default

![Work Order](/files/work_order_calendar.png)

### 2.5 Capacity Planning Error

If the Production Capacity days is less than time required to complete the operation then system throws a capacity planning error. In this case, user has to increase the number under "Production Capacity" days in the Manufacturing Settings or reduce the number of finished goods as per the capacity of the Workstations

![Work Order](/files/capacity_planning_error.png)

<!-- page: erpnext/erpnext__production-and-material-planning.md -->
---
title: "Production and Material Planning"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-and-material-planning"
updated: "2026-02-26"
---

Production and material planning in ERPNext is a comprehensive process that integrates various aspects of manufacturing, inventory management, and resource allocation.

It involves creating production schedules, determining material requirements, and optimizing resources to meet production goals efficiently. ERPNext streamlines this process by providing tools for capacity planning, work order creation, and tracking of inventory levels.

By centralising data and automating workflows, ERPNext enables businesses to enhance productivity, reduce lead times, minimise costs, and improve overall operational efficiency in their production processes.

* [Work Order](/erpnext/user/manual/en/work-order)
* [Work Order Summary](/erpnext/user/manual/en/work-order-summary)
* [Production Plan](/erpnext/user/manual/en/production-plan)
* [Plant floor](/erpnext/user/manual/en/plant-floor)
* [Capacity Planning](/erpnext/user/manual/en/production-and-material-planning-capacity-planning)
* [Capacity Planning Based On Production Order](/erpnext/user/manual/en/capacity-planning-based-on-production-order)
* [Capacity Planning Based On Work Order](/erpnext/user/manual/en/capacity-planning)
* [Downtime Entry](/erpnext/user/manual/en/downtime-entry)
* [Downtime Analysis](/erpnext/user/manual/en/downtime-analysis)
* [Job Card](/erpnext/user/manual/en/job-card)
* [Job Card Summary](/erpnext/user/manual/en/job-card-summary)
* [Stock Entry](/erpnext/user/manual/en/stock-entry)

  

<!-- page: erpnext/erpnext__production-plan-schedule.md -->
---
title: "Production Plan Schedule"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan-schedule"
updated: "2026-08-25"
---

The Production Plan Scheduler calculates realistic start and end dates for everything in your Production Plan - finished items, sub-assemblies, and even the purchase of raw materials - based on how much your machines can actually handle. Instead of typing dates in manually and hoping the shop floor can keep up, you get a schedule that respects machine capacity, working shifts, holidays, and work that is already booked.



![](/files/Screen Recording 2026-08-12 at 4.23.05 PM.mov)

---

## 1. Why use it

Without scheduling, a Production Plan only says *what* to make and *how much*. It cannot answer the questions a planner actually has:

- **When will this order be finished?**
- **Which machine will be busy, and when?**
- **Do we need to order material before we can start?**
- **Can we take on another order this week, or are the machines full?**

The scheduler answers all of these before a single Work Order is created - and when you do create Work Orders, they automatically follow the same dates.

---

## 2. What you need to set up first

You don't need all of this, the scheduler uses the best information available for each item. But the more you maintain, the more accurate your dates become.

### For machine-level scheduling (most accurate)


| Setup                    | Where         | What it does                                                                                                                                                                                                                     |
| ------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Working Hours**        | Workstation   | Your shifts, e.g. one row for 8 AM–4 PM and another for 4 PM–12 AM means the machine runs two shifts. Work is only scheduled inside these hours.                                                                                 |
| **Holiday List**         | Workstation   | Days the machine doesn't run. The schedule skips them.                                                                                                                                                                           |
| **Job Capacity**         | Workstation   | How many jobs can run on the machine at the same time. Capacity 2 = two job cards side by side.                                                                                                                                  |
| **Operations with time** | BOM           | Each operation's time in minutes, with either a specific **Workstation** or a **Workstation Type**.                                                                                                                              |
| **Workstation Type**     | BOM Operation | Leave the specific Workstation blank and set a type (e.g. "Molding"), the scheduler automatically picks whichever machine of that type is free first. With 2 molding machines of capacity 2, four jobs can run at the same time. |


### For items without BOM operations (day-level estimate)


| Setup                | Where           | What it does                                                                                               |
| -------------------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| **Capacity Per Day** | Item Lead Time  | How many units you can produce per day. 120 pcs at 60/day = 2 days.                                        |
| **Daily Yield %**    | Item Lead Time  | Reduces effective capacity (note: it defaults to 90%). Set 100 if you don't use yield.                     |
| **Buffer Time**      | Item Lead Time  | Extra safety days added to the duration.                                                                   |
| **No of Shifts**     | Production Plan | If your Item Lead Time capacity was recorded for 1 shift and this plan runs 2, the daily capacity doubles. |


### For raw materials


| Setup                           | Where          | What it does                                                                                      |
| ------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- |
| **Purchase Time + Buffer Time** | Item Lead Time | How many days it takes to procure the material. Production that consumes it cannot start earlier. |
| **Lead Time in Days**           | Item master    | Used as a fallback when there is no Item Lead Time record.                                        |


### Supplier Lead Time

![](/files/Screenshot 2026-08-25 at 11.33.20 AM.webp)

Not every supplier delivers at the same speed - a local dealer may ship in 2 days while an importer needs 15. The Supplier Lead Times table lets the schedule reflect that difference:

- Each row is one supplier with its own purchase and buffer days. The same supplier cannot be added twice, and only one row can be the default.
- When you fetch materials in the Production Plan, each purchase row gets a **Supplier** filled in automatically - from the default Supplier Lead Times row, or from the item's **Default Supplier** (Item Defaults) if no lead-time default exists. You can change it per row before scheduling.
- The scheduler then uses **that supplier's** lead time. If the chosen supplier isn't in the table, it falls back to the default supplier's row, then to the item-level Purchase Time, and finally to the Item master's Lead Time in Days.

If an item has neither operations nor lead-time data, the scheduler assumes 1 day, so the schedule always completes, it just tells you less.

---

## 3. Creating a schedule

1. Submit your **Production Plan** as usual.
2. Click the **Schedule Items** button in the toolbar.
3. Pick a **Start Date** - the earliest moment any work may begin.
4. *(Optional)* Tick **Use Item Wise Start Dates** if different items should start on different dates. A small table appears where you can set a date per item; its sub-assemblies follow the same date.
5. Click **Preview**.

Nothing is saved at this point, the preview is a safe "what-if". You can close it, change the dates, and preview again as many times as you like.



![](/files/Screenshot 2026-08-12 at 5.18.19 PM.webp)

### Reading the preview

- The list is a **tree**: finished items in bold, their sub-assemblies indented below them, and **Procurement** rows showing when purchased material will be available.
- **Start / End** show the calculated dates for each item.
- **Starts In** shows how soon each item begins **green** when it starts in more than a day, **orange** when it's less than a day away.
- The tiles at the top show the **Expected Completion** date, the **Total Duration**, and the number of items.
- If something could not be scheduled (for example, no machine can fit the work within the planning horizon), a red banner explains why, and the Apply button is hidden until the problem is fixed.

6. Click **Apply Schedule**. Now the dates are saved:
  - Every item row in the plan gets its **Planned Start / End Date**.
  - A **Production Plan Schedule** entry is created for every block of work, these are what you see on the calendar.

---

## 4. The Production Schedule calendar

Open it from the plan via **View → Production Schedule**, or from the new **Schedule** section in the plan's connections area. Each entry reads *Item · Activity* for example "Bicycle · Assembly", "Chain · Production", or "Front Wheel · Procurement". You can filter the calendar by **Production Plan**, **Workstation**, or **Item** filtering by workstation gives you that machine's day/week view, exactly like a booking calendar. A job that spans two shifts appears as two blocks, so shift handovers are visible at a glance.

![](/files/Screenshot 2026-08-12 at 5.23.35 PM.webp)

---

## 5. What happens when you create Work Orders

When you create and submit Work Orders from a scheduled plan, the schedule flows with them:

- Each Work Order takes its **Planned Start Date** from the plan.
- The **Job Cards** created on submission are placed on the **same machines at the same times** as the plan's calendar the shop floor sees exactly what the planner promised.

### Re-scheduling rules

- **Before** Work Orders exist: re-run Schedule Items freely. Each Apply replaces the previous schedule completely.
- **After** Work Orders exist: the schedule is **locked**. The preview still works for what-if analysis, but it shows a banner explaining that orders already exist, and Apply is disabled because the job cards on the shop floor are already following the old dates. Cancel the Work Orders if you genuinely need to re-plan.

![](/files/Screenshot 2026-08-12 at 4.38.21 PM.webp)

---

## 6. How the dates are calculated (in plain words)

For every item in the plan, the scheduler asks, in order:

1. **Does its BOM have operations?** Then each operation's time (multiplied by the quantity) is booked on a machine, inside its working hours, skipping holidays, waiting its turn if the machine is busy with other job cards, and leaving the standard gap between operations.
2. **No operations?** Then the Item Lead Time capacity is used: quantity ÷ capacity per day = number of days, plus buffer.
3. **Is it subcontracted or purchased?** Then it is a waiting period: purchase time + buffer days.

On top of that, three rules connect everything together:

- A **parent cannot start before its children finish** - the Bicycle waits for the Chain and the Wheel.
- **Production cannot start before its raw material arrives** - the procurement time pushes everything that depends on it.
- **A machine is never double-booked** beyond its Job Capacity, if two items need the same machine, the second one waits (or moves to another machine of the same type, if one exists).

The finish date you see on the preview is simply the end of the longest chain.

---

<!-- page: erpnext/erpnext__production-plan-visualizer.md -->
---
title: "Production Plan Visualizer"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan-visualizer"
updated: "2026-08-31"
---



![](/files/Screen Recording 2026-08-31 at 4.18.06 PM.mov)

## What is this feature?

A Production Plan tells you what you plan to make. After you submit it, the work is spread across several documents — Work Orders for items you make in-house, Purchase Orders for items you subcontract, and Material Requests for raw materials you need to buy.

To answer a simple question like *"Can I start building this today?"*, you normally have to open the plan, then open each Work Order, check each Material Request, and check the stock for every raw material. For a plan with a few finished goods, this can mean dozens of clicks, and it is easy to miss the one item that is holding everything up.

**The Production Plan Visualizer puts all this information on one screen.** It shows you, at a glance:

- How much of the plan has been produced.
- Whether the raw materials are available or something still needs to be ordered.
- Which Work Orders and Purchase Orders exist and which ones have not been created yet.
- When each job is scheduled on the shop floor.

Nothing on this screen changes your data. It is a **read-only view**, you can view the information, but you cannot accidentally edit anything.

## 2. When should you use it?

Use it when you want to quickly answer questions like:

- *Is this plan on track?*
- *What is stopping me from starting production?*
- *Have all the Work Orders been created, or did someone miss one?*
- *Which raw material is short?*
- *What is scheduled on which machine this week?*

It is most useful for **production planners, plant managers, and supervisors** who need to track a plan until completion. You do not need it if you only create a plan and hand it over.

## 3. How to open it

There are two ways.

**From a Production Plan (easiest):**

1. Open the Production Plan you want to view.
2. Click the **View** menu at the top right.
3. Click **Plan Visualizer**.

<!-- page: erpnext/erpnext__production-plan.md -->
---
title: "Production Plan"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan"
updated: "2026-02-27"
---

**A Production Plan helps in production and material planning for the Items planned for manufacturing. These production items can be committed via Sales Order (to Customers) or Material Requests (internally).**

Production Plan helps the user to plan production against multiple Sales Orders or the Material Requests. Also, it helps in Material Procurement planning for the raw material item, based on the quantity of finished products to be manufactured.

To access the Production Plan list, go to:

> Home > Manufacturing > Production > Production Plan

1. Prerequisites
----------------

Before creating and using a Production Plan, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Material Request](/erpnext/material-request)
* [Sales Order](/erpnext/sales-order)
* [Bill Of Materials](/erpnext/bill-of-materials)
* [Routing](/erpnext/routing)

2. How to Create a Production Plan
----------------------------------

As mentioned earlier, a Production Plan can be used for planning the manufacture of Items against Sales Orders or Material Requests.

The common steps are:

1. Go to the Production Plan list, click on New.
2. Select whether to get items from a [Sales Order](/erpnext/sales-order) or a [Material Request](/erpnext/material-request).

A Production Plan can also be created manually where you can select the Items to manufacture.

### 2.1 Production Against Sales Orders

1. Select option as Sales Order from the 'Get Items From' drop-down list. The system will show the filters, using that you can pull the Sales Orders for the production. You don't need to use all these filters if you have only a few Sales Orders in a particular time frame.

![Production Plan fetch items](/files/pp_fetch_from.png)
2. Click on Get Sales Orders to fetch sales orders based on the above filters.

![Sales Order Filters](/files/sales_order_filter.png)
3. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched. ![Get items for Production Plan](/files/get_items_wo.png)
4. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process.
5. If "Consolidate Items" is ticked and saved, items with the same BOM are combined into a single item with the combined total planned quantity. ![Get items Combined for Production Plan](/files/get_items_combined_wo.png)

### 2.2 Production Against Material Requests

1. Select option as Material Request from the Get Items From drop-down list. The system will show the filters, using that we can pull the Material Requests for the production.

![Material Request Filters](/files/material_request_filter.png)
2. Click on 'Get Material Request' to fetch material requests based on the above filters.

![Material Requests](/files/material_requests.png)
3. Click on Get Items for Work Order to fetch the items from the above material requests.

![Material Request Item](/files/material_request_items.png)

### 2.3 Fetching Sub Assembly Items

Clicking on 'Get Sub Assembly Items' will fetch Sub Assembly Items from the BOM of the Finished Good Items, in the table above. ![Get Sub Assembly Items](/files/get-subassembly-items.png)  


#### 2.3.1 Sub Assembly Items

User will get option to make In House (Work Order) / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type.

![](/files/Screenshot%202025-04-08%20at%204.43.43%20PM.png)


If user wants to make Material Request for their Sub-assembly items as well their Final Raw Materials then they have to select the Manufacturing Type as "Material Request" for Sub-assembly items and then they have to click on the button "Get Items for Purchase Only" to fetch Sub-assembly items in the Material Request Plan Item table.


![](/files/Screenshot%202025-04-08%20at%204.44.08%20PM.png)


#### 2.3.2 Combining Sub Assembly Items

If there are Finished Goods that share the same Sub Assembly Item, the Sub Assembly Items can be combined. The criteria for combination would be to have the same Item, Warehouse, BOM and Manufacturing Type.

![Combine Sub Assemby Items](/files/consolidate-subassembly-items.png)  


In this way a common Work Order can be made to bulk create Sub Assemblies for various Finished Goods.

#### 2.3.3 Skip Available Sub Assembly Items or Skip Available Raw Materials



![](/files/Screenshot%202025-04-08%20at%204.24.08%20PM.png)


If users enable the checkbox 'Skip Available Sub-Assembly Items' or 'Skip Available Raw Materials', the system will consider the Projected Qty which is available in the bin to calculate the required quantity for sub-assembly items or raw materials. To understand this, consider the following case.

##### Example

To produce 1 qty of Item A, 1 qty of Item B (sub-assembly) is required, and to produce 1 qty of Item B, 1 qty of Item C is required.


* In the production plan, Item A has a quantity of 100 to produce.
* Against Item B already work order created for 20 qty which is not completed and 20 more qty available in the stock. Which meant total 40 qty is available in the Projected Qty
* Against Item C already purchase order created for 40 qty which is not completed and 20 more qty available in the stock. Which meant total 60 qty is available in the Projected Qty
* If Skip Available Sub Assembly Items enabled, while calculating the required qty for Item B
    * Reqd Qty = Required Qty (as per BOM) - [Projected Qty](https://docs.frappe.io/erpnext/user/manual/en/projected-quantity) (in BIN) 
    * Reqd Qty = 100 - 40
    * **Reqd Qty = 60**

* If Skip Available Raw Materials enabled, while calculating the required qty for Item C
    * Reqd Qty = Required Qty (as per BOM) - [Projected Qty](https://docs.frappe.io/erpnext/user/manual/en/projected-quantity) (in BIN)  
    * Reqd Qty = 100 - 60
    * **Reqd Qty = 40**

### 2.4 Planning for Material Requests

Clicking on the 'Get Items for Purchase Only' button will fetch the required raw material Items in the Material Request Plan table. For example, to manufacture 200 plastic canes, you need 100 raw plastic Nos but have only 20 in your Warehouse, then clicking this button will add a row with 80 in the Required Quantity column (make sure Skip Available Raw Materials is enabled).


![](/files/Screenshot%202025-04-08%20at%204.36.30%20PM.png)

If partial materials are available in a different warehouse and you want to perform a material transfer and create a purchase entry for the remaining quantity, use the "Get Items for Purchase / Transfer" button. Here, you need to specify the warehouse from which the transfer should be made. If you select the parent warehouse, the system will check stock availability in its child warehouses and suggest transferring materials from those child warehouses.


![](/files/Screenshot%202025-04-08%20at%204.42.00%20PM.png)


Use the following checkboxes to perform certain actions:

* **Include Non Stock Items**: To include non-stock items in the material request planning. i.e. Items for which 'Maintain Stock' checkbox is unticked. Refer the [Item page](/erpnext/item#12-options-when-creating-an-item) for more details.
* **Include Subcontracted Items**: To add subcontracted Item's raw materials if include exploded items is disabled.
* **Skip Available Raw Materials**: 
If enabled, the system will consider items with a shortfall in quantity.
Formula to calculate Required Qty:
Required Qty = BOM Required Qty – Projected Qty 

* Example: Item A has 50 qty in stock and 20 qty in a Material Request (with a pending Purchase Order). To complete production, 100 qty is required.

    * If the "Skip Available Raw Materials" checkbox is enabled, the system will calculate the required quantity as: 100 - (50 + 20) = 30
    
    * If the "Skip Available Raw Materials" checkbox is not enabled, the system will calculate the required quantity as: 100, ignoring the available stock or incoming quantities.

* **For Warehouse**: User can set the Warehouse for which they want to create the material request. When creating Stock Entries during the production process, the system will look for raw material stock in this Warehouse.

#### 2.4.1 Download Material Request Plan

![](/files/Screenshot%202025-04-08%20at%204.43.08%20PM.png)


On click of "Download Material Request Plan" button the User will get the Excel sheet with the raw materials that are needed to complete this Production Plan. User can select the Warehouse to check the available quantity in the respective Warehouse. On click of "Download Material Request Plan" a popup will open to select warehouses. If user wants to Run plan for multiple warehouses then they can select those warehouses in the Popup to download the plan in the excel sheet format. Excel sheet will look similar to:

![Material Request Plan](/files/material_request_excel.png)  


### 2.5 After Submitting

Once the Production Plan is submitted, the User gets an option to make Work Orders for the production items and Material Requests for the raw materials. Users can also set the Status as **Closed** in the Production Plan.

![](/files/Screenshot%202025-04-08%20at%204.49.56%20PM.png)


#### 2.5.1 Closing a Production Plan

There could be occurrences where a Production Plan is partially complete and is going to be discontinued. This could happen due to reasons such as:

* One of the items was independently produced outside the Production Plan.
* A change in plans occurred and pending items will not be produced.

In cases like these, Users can set the Production Plan status to **Closed**, so that no new Work Orders or Material Requests are created against it.

![Closing a Production Plan](/files/production_plan_status.gif)  


The same can be **Re-opened**.

### 2.6 Making work order for the sub-assembly items

User will get option to make Work Order / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type.


If user wants to make Work Order for sub-assembly items then select the Manufacturing Type as In House and submit it. After Submit you have to click on the button Create -> Work Order / Subcontract PO

![](/files/Screenshot%202025-04-08%20at%204.44.08%20PM.png)







3. Related Topics
-----------------

1. [Work Order](/erpnext/work-order)
2. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__production-planning-report.md -->
---
title: "Production Planning Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-planning-report"
updated: "2026-03-02"
---


To access the Production Planning Report, go to:

> Home > Manufacturing > Reports > Production Planning Report

![Task](/files/production-planning-report.png)

This report will help users plan the finished good as well as the raw materials against the Sales Order / Work Order / Material Request (with the request type as Manufactured) data. Mostly, in the case of make to order, this report helps you plan the production of the finished goods as well the raw materials.

Using this report user will get the information about the available finished goods as well as available raw materials that are required in the production process. The unavailable finished good or raw materials will be highlighted in the red color.

In this report system will allocate the available stock to the order based on the sorting. The **Order By** filter will be use to sort the orders based upon the Delivery Date, Order Amount.

For example, Bob works in the Furniture Manufacturing company. Their organization follows the make to order production planning. On Monday, Bob received the Sales Orders for tables and chairs from different customers. So Bob has checked the production planning report to check the availability of the raw materials and he found that either table or chair can be manufactured with the available raw materials. Bob used the 'based on' filter to know which Finished Good order's delivery date is earlier. He has found that he has to deliver the Table earlier so he has started working on it and his colleague has created the purchase order for raw materials which will be used to make chair.

Using the **Production Planning Report**, this report auto allocate the raw materials to the order once it's available in the respective warehouse.

<!-- page: erpnext/erpnext__profit-and-loss-report.md -->
---
title: "Profit and Loss Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/profit-and-loss-report"
updated: "2026-08-14"
---

Nova Industries recorded $363,200 of income and $253,760 of expenses in 2026. The business earned $109,440, but the owner wants to know where that profit came from and whether a particular product line, department, or period performed better than another.



The Profit and Loss Statement summarizes income minus expenses over a period. It answers whether the company earned a profit, which accounts produced it, and how results compare across periods or reporting dimensions. It does not show what the company owns and owes at one date, which belongs in the [Balance Sheet](/erpnext/balance-sheet), or explain when cash moved, which belongs in [Cash Flow](/erpnext/cash-flow).

## Before you begin

Submit the relevant [Sales Invoices](/erpnext/sales-invoice), [Purchase Invoices](/erpnext/purchase-invoice), stock transactions, payroll entries, depreciation, and approved [Journal Entries](/erpnext/journal-entry). Confirm that Income and Expense accounts use the correct root and report type in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Run the report

1. Open **Accounting** and select **Profit and Loss Statement**.
2. Select **Nova Industries**.
3. Choose Fiscal Year or Date Range and set the required period.
4. Select Yearly, Half-Yearly, Quarterly, or Monthly periodicity.
5. Apply Finance Book, Cost Center, Department, Project, or another [Accounting Dimension](/erpnext/accounting-dimensions) only when the question requires that slice.
6. Refresh and wait for the totals, chart, and account rows to load.

![Loaded Profit and Loss Statement for Nova Industries showing income, expenses and profit](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-profit-and-loss-loaded.png)

## Interpret the Nova Industries result


| Result        | Value    | Interpretation                                                      |
| ------------- | -------- | ------------------------------------------------------------------- |
| Total Income  | $363,200 | Revenue and other income recognized during the selected period.     |
| Total Expense | $253,760 | Cost of goods sold and other expenses recognized during the period. |
| Profit        | $109,440 | Income exceeds expenses by this amount for the selected scope.      |


The profit is approximately 30.1% of income. That ratio is useful only after confirming that all period expenses, stock costs, depreciation, accruals, and adjustments are posted. A positive profit also does not mean the same amount is available in the bank. Credit sales can increase profit before customers pay.

## Read the account hierarchy

Expand Income and Expense groups to see the accounts behind each total. Direct Income and Direct Expense usually describe core trading or service activity. Indirect Income and Indirect Expense normally contain supporting or non-core items. The exact meaning depends on how your organisation designed its accounts.



Select an account value to drill into the entries that produced it. The linked [General Ledger](/erpnext/general-ledger) should use the same Company, dates, Finance Book, and dimensions as the Profit and Loss Statement.

![General Ledger drill-down opened from a Profit and Loss account value](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-profit-and-loss-drilldown.png)

## Understand the important filters


| Filter                                           | Effect                                                                                               |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Fiscal Year or Date Range                        | Defines which accounting period is included.                                                         |
| Periodicity                                      | Splits results into yearly, half-yearly, quarterly, or monthly columns.                              |
| Accumulated Values                               | Shows cumulative balances through each displayed period instead of each period in isolation.         |
| Finance Book                                     | Restricts entries to the selected accounting book, subject to the default-book option.               |
| Cost Center, Project, Department, and dimensions | Shows the profit result for a selected operational segment.                                          |
| Currency                                         | Changes presentation currency without changing the underlying ledger entries.                        |
| Report Template                                  | Applies a configured [Financial Report Template](/erpnext/financial-report-template) when available. |


## Profit and cash are different

The Profit and Loss Statement recognizes income and expenses according to accounting dates. [Accounts Receivable](/erpnext/accounts-receivable) may show that customers still owe part of the reported income, while [Accounts Payable](/erpnext/accounts-payable) may show unpaid supplier expenses. Use Cash Flow to explain how those outstanding balances affect actual cash movement.

## Troubleshooting

### The report is empty

Confirm that submitted transactions exist inside the selected period and Company. Remove Finance Book and dimension filters one at a time, then verify that the affected accounts use Income or Expense roots.

### Profit and General Ledger do not agree

Match Company, dates, Finance Book, dimensions, currency, and period-closing options. A drill-down that loses a dimension filter can show a broader ledger scope than the original report.

### A monthly result looks cumulative

Review the Accumulated Values setting. Enable it for year-to-date columns and disable it when each month should show only that month's activity.

### Previous-year income or expense appears

Review fiscal-year dates and [Period Closing Voucher](/erpnext/period-closing-voucher) status. Income and Expense accounts normally begin the new fiscal year without the previous year's operating balance.

## Frequently asked questions

### Can a profitable company have negative cash flow?

Credit sales can create income before customers pay, while inventory purchases and other cash outflows may occur earlier. Cash Flow explains the difference.

### Does changing a report filter alter accounting entries?

Filters change which entries are selected and how they are presented. They do not repost submitted transactions.

### Should tax appear as income or expense?

The answer depends on the tax type, recoverability, and account configuration. Review regional accounting rules and the accounts used by the source transactions.

### Can the report compare departments or product lines?

Cost Centers, Projects, and custom Accounting Dimensions can segment the result when those values were recorded consistently on transactions.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Balance Sheet](/erpnext/balance-sheet)
- [Cash Flow](/erpnext/cash-flow)
- [General Ledger](/erpnext/general-ledger)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Financial Report Template](/erpnext/financial-report-template)

<!-- page: erpnext/erpnext__proforma-invoice.md -->
---
title: "Proforma Invoice | ERPNext Documentation"
description: "Create and manage Proforma Invoices from Sales Orders in ERPNext, including quantity-based and amount-based advance documents."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/proforma-invoice"
updated: "2026-07-24"
---

A **Proforma Invoice** is a preliminary, non-binding invoice sent to a customer before the goods are delivered or the final (tax) invoice is raised. It is commonly used to request an advance payment, to support a letter of credit or customs paperwork, or to give the customer a formal statement of what an order will cost.

In ERPNext, a Proforma Invoice is raised against a **Sales Order**. It is a purely informational document: it does **not** post any accounting (General Ledger) or stock entries, does not affect the delivery or billing status of the Sales Order, and does not consume the ordered quantity. You can raise as many proformas against a Sales Order as you need.

To create a Proforma Invoice, you must first enable the feature, and then create it from a submitted Sales Order.

---

## Enable Proforma Invoice

The feature is off by default. To turn it on, go to:

> **Selling Settings > Transaction**

Select **Enable Proforma Invoice**.

You can optionally set a **Default Proforma Print Format** that will be pre-selected whenever a proforma is created.

![](/files/Screenshot 2026-07-19 at 12.27.14 PM.webp)
*Enable Proforma Invoice*

### **Naming Series**

The naming series used for Proforma Invoices can be configured under:

> **Selling Settings > Document Naming > Proforma Invoice**

By default, proformas are named using the `PRO-.YYYY.-` series.

---

## Create a Proforma Invoice

Open a **submitted** Sales Order and click:

> **Create > Proforma Invoice**

A dialog opens where you configure the proforma.

![](/files/Screenshot 2026-07-19 at 7.07.40 PM.webp)
*Proforma creation dialog*

The dialog has the following fields:

- **Series**: the naming series for this proforma.
- **Print Format** and **Letter Head**: control how the printed proforma looks. The default print format from Selling Settings is pre-selected; you can override it per proforma.
- **Based On**: whether you specify each line by **Quantity** or by **Amount** (see below).
- **Items**: the Sales Order lines. Each line is pre-filled with its **remaining** value (ordered minus what has already been proforma'd).

Enter the quantity or amount for the lines you want to include (set a line to `0` to leave it out), then click **Create**. The proforma is created, its PDF is generated and attached, and the **Proforma** tab of the Sales Order opens automatically.

### Based On: Quantity

This is the default. Enter the **Quantity** for each item; the amount is calculated automatically from the Sales Order rate (`Amount = Quantity × Rate`).

Use this when the proforma represents a partial (or full) shipment of the ordered items, for example a staged delivery.

### Based On: Amount

Switch **Based On** to **Amount** to enter a monetary **Amount** per line directly. Both **Quantity** and **Amount** are editable, and the rate is derived from them (`Rate = Amount ÷ Quantity`).

Use this for value-based or advance proformas, for example "30% advance against this order".

### Hide Item Quantity in Print

When **Based On** is **Amount**, an additional option, **Hide Item Quantity in Print**, becomes available. Enable it to omit the quantity and rate columns from the printed proforma, so it shows only the item and the amount. This produces a clean value-based document where you do not want to disclose a per-unit rate.

## Quantity/Amount Warning

Proforma quantities and amounts are **not** enforced; a proforma is informational. However, if the **total** proforma quantity or amount for a line (this proforma plus any previously issued proformas) exceeds the ordered value, a warning is shown below the items table. You can still create the proforma; the warning is only there to flag it.

---

## The Proforma Tab

Once at least one proforma exists for a Sales Order, a **Proforma** tab appears on the Sales Order. It lists every proforma raised against that order, showing the number, date, grand total and status.

![](/files/Screenshot 2026-07-19 at 7.09.53 PM.webp)
*Proforma lists*

From this list you can:

- **View PDF**: open the attached proforma PDF.  
- **Send Email**: email the proforma PDF to the customer.
- **New**: create another proforma.

---

## Print and Email

Every proforma has its PDF generated and attached automatically on creation, using the selected print format and letterhead. You can:

- Open the PDF from the **Proforma** tab (**View PDF**) or from the Proforma Invoice record.
- Email it to the customer using **Send Email** from the tab, or the standard print/email options on the Proforma Invoice record.

![](/files/Screenshot 2026-07-19 at 7.10.31 PM.webp)
*Proforma Invoice PDF*

## Cancel a Proforma Invoice

To void a proforma, open the Proforma Invoice record and **Cancel** it. Cancelling marks the proforma as **Cancelled** but keeps its PDF for reference, and cancelled proformas remain listed in the Proforma tab (shown with a red *Cancelled* status) so you retain a full audit trail. A cancelled proforma no longer counts towards the total proforma quantity/amount used by the warning.

---

## Related Topics

1. [Sales Order](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/sales-order)
2. [Sales Invoice](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/sales-invoice)
3. [Selling Settings](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/selling-settings)

<!-- page: erpnext/erpnext__project-costing.md -->
---
title: "Project Costing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-costing"
updated: "2026-02-26"
---

Each project has multiple tasks associated with it. To track the actual cost of a Project, primarily in terms of services, a User has to create a Timesheet based on the time spent on a Task within a Project. You can track the service cost against a Project in the following ways.

## Activity Type

Activity Type is a master of services offered by your personnel. You can add a new Activity type from:

> Home > Projects > Activity Type > New

![Screenshot 2024-06-21 at 3.13.26 PM](/files/Screenshot 2024-06-21 at 3.13.26 PM.png)

## Activity Cost

Activity Cost is a master where you can track billing and costing rate for each Employee, for each Activity Type.

![](/files/Screenshot 2026-01-09 at 11.59.23 AM.png)

## Timesheet

Based on the time spent on the Project-Task, an Employee will create a Timesheet.

![](/files/Screenshot 2026-01-09 at 12.04.13 PM.png)

On selection of the Activity Type in the Time Log, Billing and Costing Rate will be fetched for that Employee from the respective Activity Cost.

Multiplying these rates with total no. of hours in the Time Log gives Costing Amount and Billing Amount for the specific Time Log.

## Costing in Project and Task

Based on all the Timesheets created for specific Tasks, its costing will be updated in the respective Task.

![](/files/Screenshot 2026-01-09 at 12.12.15 PM.png)

Same way, the Project cost will be updated based on Timesheets created against each of its associated tasks and the cost of the Project gets updated simultaneously.

![](/files/Screenshot 2026-01-09 at 12.49.27 PM.png)

<!-- page: erpnext/erpnext__project-customer-portal.md -->
---
title: "Project from Customer Portal\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-customer-portal"
updated: "2026-02-26"
---

If you are working on a Project for a Customer, then they need to be updated on its progress from time-to-time. You can achieve this in ERPNext via the Customer Portal.

### Add User as a Website User

To access a project from the portal, a customer must be added as a Website User. A Customer can also sign up from the Login Page of your ERPNext account, using the same Email ID as mentioned in the Contact. You can also send an invite to the contact using the **Invite User** button in Contact.

![](/files/Screenshot 2026-01-09 at 12.27.52 PM.png)

### Add Customer and User in Project

In the Project, check Customer Details section. Select a Customer and Sales Order associated with this Project.

![](/files/Screenshot 2026-01-09 at 12.24.13 PM.png)

Under the User table, select the contacts who can access this project.

### Portal View of Project

When a Customer logins from the Portal, they will be able to view all the tasks for that project along with the associated timesheets. Also, the customer will be able to update the status of the tasks or comment when needed.

![](/files/customer_portal.gif)

<!-- page: erpnext/erpnext__project-expense-claims.md -->
---
title: "Project and Managing Expenses\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-expense-claims"
updated: "2026-02-26"
---

Employees working on a Project incur various expenses, sometimes from their pockets and then can claim such expenses using Expense Claim.

While filling up the claim, they can specify the Project for which they have made the expense.

![](/files/Screenshot 2026-01-09 at 12.18.22 PM.png)

Based on the Expense Claims made for a particular project, total Expense Claim Amount is updated in the Project master, under project costing section.

![](/files/Screenshot 2026-01-09 at 12.19.33 PM.png)

<!-- page: erpnext/erpnext__project-profitability.md -->
---
title: "Project Profitability\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-profitability"
updated: "2026-02-26"
---

Project and related activities are generally active for longer periods. While developments keep happening on the Project, various transactions are done against each project. While new developments keep happening on a project, it may lead to more investment in terms of time, money, and material. Hence, it becomes important to track the Profitability of a Project to ensure that you don't overspend.

In simple terms, Project Profitability is the difference between the revenue generated from a project versus the costs associated with it.

### Project in Sales Transactions

You can link a Project in all sales transactions like Sales Order, Delivery Note, Sales Invoice, and Payment. Linking your project with the sales transactions will help you track the income received against that Project.

In sales transactions, Project field is generally available in the More Information section.

![](/files/Screenshot 2026-01-09 at 11.33.39 AM.png)

#### Project in Purchase Transactions

You can also link your project to the purchase transactions like Purchase Order, Purchase Receipt, and Purchase Invoice.

In the purchase transactions, the option to link a project is available in the Item table. This is because you could be procuring material for multiple projects from the same purchase entry.

![](/files/Screenshot 2026-01-09 at 11.39.19 AM.png)

### Budgeting against Project

You can create a Budget for a project as well. The expense limit defined in the Budget will be validated in the expense transactions.

![](/files/Screenshot 2026-01-09 at 11.42.35 AM.png)

### Project Profitability

Based on all the income and expense entries created for the Project, you can get its profitability.

> Accounting > Profitability Analysis

You can filter the report by Project to check Project-wise Profitability.

![](/files/Screenshot 2026-01-09 at 11.40.53 AM.png)

<!-- page: erpnext/erpnext__project-reports.md -->
---
title: "Project Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-reports"
updated: "2026-02-26"
---

These reports help track project progress, project status, and key metrics such as timelines, costs, and resource allocation

## Project Summary

The **Project Summary** provides an overview of key project information, including the current project status, start and end dates, and a consolidated view of related records. It displays the number of associated **Tasks** and **Timesheets**, allowing users to quickly assess project progress and activity at a glance.

The image below shows the summary of the example we discussed in Getting started for the Rack Storage manufacturing. 

![](/files/project_summary.png)
*Project Summary*

## Daily Timesheet Summary

The **Daily Timesheet Summary** provides a consolidated view of all tasks recorded in a timesheet for a selected time period. It displays the timesheet activities along with the logged hours and the corresponding linked tasks and projects, enabling users to review daily time allocation at a glance.

![](/files/daily_timesheet_summary.png)
*Daily Timesheet Summary*

## Timesheet Billing Summary

This report provides a summary of t**imesheet-based billing** for a selected time period. It displays the total working hours along with the corresponding billable hours, billing rates, and calculated billing amounts, enabling users to review and analyze time-and-material billing at a glance.

![](/files/timesheet_billing_summary.png)
*Timesheet Billing Summary*

## Project Wise Stock Tracking

This report provides visibility into stock movements associated with projects, including purchased items and issued items. It also displays key project information such as the project status, total project value, and the project start and completion dates, enabling effective tracking of material usage and overall project progress.

![](/files/project_wise_stock_tracking.png)
*Project wise stock tracking*

## Delayed Task Summary

The Delayed Tasks Summary report helps identify the tasks which have exceeded their Expected End Dates. It provides visibility into both on-track and delayed tasks, along with their current progress and the expected start and end dates, enabling users to identify schedule deviations and take corrective action.

To view this report, you can go to:

> Home > Projects > Reports > Delayed Tasks Summary

The report is generated based on the Task Doctype.

### Calculation of Delay

Tasks have a date field called **Completed On**, which becomes visible when a Tasks status is changed to Completed.

##### Scenario 1

If a task is marked as Completed and the Completed On field is set, then the delay is calculated as the difference between the Completed On and the Expected End Date.

```
Delay = Completed On - Expected End Date
```

##### Scenario 2

If the Completed On field is not set, then the delay is calculated as the difference between the current date and the Expected End Date.

```
Delay = Current Date - Expected End Date
```

### Chart

The chart shows the number of tasks that are On Track or Delayed based on the report generated after applying the filters.

![Delayed Tasks Summary](/files/delayed-tasks-summary.png)
*Delayed Tasks Summary*

<!-- page: erpnext/erpnext__project-template.md -->
---
title: "Project Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-template"
updated: "2026-02-26"
---

**A Project Template is a predefined sequence of tasks arranged in stipulated schedule.**

These templates can be pulled for similar kind of Projects and the tasks therein get auto-populated at the time of creation of each new project.

To access Project Template, go to:

> Home > Projects > Projects > Project Template

![](/files/image9c09a2.png)

## How to Create A New Project Template:

1. Go to the Project Template List and click on New.
2. Add the following details:

- **Project Template Name**: Title of the Project Template
- **Project Type**: Project Templates, just like projects can be classified into different project types, e.g., Internal or External.
- **Tasks**: Each Project Template will have a set of a predefined sequence of tasks. In this table, you can select the tasks you want for this template.

## Related Topics

1. [Project](/erpnext/user/manual/en/project)
2. [Task](/erpnext/user/manual/en/tasks)

<!-- page: erpnext/erpnext__project-type.md -->
---
title: "Project Type\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-type"
updated: "2026-02-26"
---

**A Project Type is the classification of projects into different types to group similar kind of projects.**

Internal Projects, External Projects could be examples of Project types and are already created in the system. You can choose to add more Project Types. This comes handy when you are reviewing the Projects, and you want to filter the information based on Project Types.

![](/files/imagec36751.png)

To access Project Type, go to:

> Home > Projects > Projects > Project Type

## How to Create a Project Type

1. Go to the Project Type List and click on New.
2. Add the name of the Project Type and description
3. Save.

## Related Topics

1. [Project](https://docs.frappe.io/erpnext/user/manual/en/project)
2. [Project Template](https://docs.frappe.io/erpnext/user/manual/en/project-template)

<!-- page: erpnext/erpnext__project-update.md -->
---
title: "Project Update"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-update"
updated: "2026-02-26"
---

**A Project Update is the status of the Project which can be sent to all the stakeholders of the Project.**

Each time you want to update the stakeholders about the project, you can send a Project Update to them.

![](/files/imagee61c72.png)

To access Project Update, go to:

> Home > Projects > Projects > Project Update

## How to Create a Project Update

---

1. Go to the Project Update List and click on New.
2. Add the name of the Project for which you want to send an update.
3. Add the name of the Users to whom you want to send the Project Update in the Child Table. These Users could be your Customers or any other Internal or External Stake Holders.
4. Save and Submit.

Once you have submitted the Project Update, an email is sent to the selected stakeholders with project updates.

### Additional Details

When you expand the table which has the names of the Users, you will be able to add the following details:

1. You can select whether you want to send a Welcome Email to any particular User while sending them the Project Update.
2. You can select whether you want any particular User to view Attachments in the Project Update.
3. You can add the description of the Current Status of the Project in the 'Project Status' field which will indicate the progress of the project.

<!-- page: erpnext/erpnext__project-views.md -->
---
title: "Project Views\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-views"
updated: "2026-02-26"
---

As projects are time-sensitive, we need different kind of views to convey information in a visual manner to users viewing them.

Apart from the generic list and report views for projects and tasks, ERPNext also provides Gantt, Kanban, and Calendar views for tasks. You can access these views by going to the Task list and selecting them via the left sidebar.

## Gantt View

A Gantt Chart shows how tasks are linked to each other and shows their execution sequence, based on start and end dates set in the tasks along with any dependencies, if available.

![](/files/image6344a3.png)
*Gantt Chart View*

You can update the range of the chart by selecting one of Quarter Day, Half Day, Day, Week, or Month.

Dragging a task along the dates will update the start and end date of a task.

If you want to further customize the chart and make it more colorful, read this article

## Kanban View

Kanban in Japanese means "billboard" or "signboard" as the task management method traces its origin back to Toyota's lean manufacturing process. In a typical kanban board setup, you have a board or wall which is divided into section which represent different stages of execution or realization. Tasks go up on the board as sticky notes or Post Its and move through the board updating its current stage in the process.

![](/files/image8704a3.png)
*Kanban View*

ERPNext renders the Kanban view for tasks based on its status. You can update the status of a task by moving the representative card from one column to the next. You can also assign colors to these columns for visual reference.

Read customizing Kanban board to learn more.

## Calendar View

Like the Gantt chart, the calendar view also shows the task and the planned number of days it'll take to complete. However, this one shows the task spread across your regular calendar.

![](/files/image5e941a.png)
*Calendar view *

<!-- page: erpnext/erpnext__project.md -->
---
title: "Project\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project"
updated: "2026-02-28"
---

**A Project is a planned piece of work that is designed to find information about something, to produce something new, or to improve something.**

In ERPNext, project management is task-driven. You can create a Project and divide it into multiple Tasks.

A Project has a broad scope and hence can be divided into tasks. Think of coming up with a new smartphone for the next year as a Project. Then things like designing, prototyping, testing, delivery, etc. become tasks under the project.

Whilst each task within a Project can be assigned to an individual or a group of individuals, the assignment can also be done at the project level.

These Tasks can be created from a Project itself or a Task can be created separately as well.

To access Projects, go to:

> Home > Projects > Project

![](/files/imagec3fe96.png)

## How to Create a Project

1. Go to the Project list and click on New.
2. Add the following details:

- **Project Name**: Title of the Project.
- **Status**: The default status of a Project is going to be 'Open', which can later be changed to 'Completed' or 'Cancelled'.
- **Expected End Date**: Enter the date on which you aim to finish the project.

### Additional Options while creating a Project

1. **From Template**: If you have an existing [Project Template](/erpnext/project-template), you can choose to create your project using this template.
2. **Expected Start Date**: If you have a time-line fixed for the project, you can define both expected Start Date and Expected End Date in the form.
3. **Project Type**: You can classify your projects into different [types](/erpnext/project-type), e.g., Internal or External.
4. **Priority**: You can select the priority level of the Project based on how crucial it is. You can also add more priority levels.
5. **Department**: If the project belongs to, or is owned by a [Department](/hr/department) in the organization, you can add that here.
6. **Is Active**: A Yes/No tab, which lets you change the active status of the project at any later stage.
7. **Completion Method**: You can track the % completion of your project based on one of the three methods, viz. **Manual, Task Completion, Task Progress and Task Weight**.

![](/files/image2d8eef.png)

Some examples of how the Percentage Completion is calculated based on Tasks:


| Project | Activity | % Progress | Weight | Status    |
| ------- | -------- | ---------- | ------ | --------- |
| SC001   | Build    | 100        | 0.4    | Completed |
| SC001   | Operate  | 100        | 0.2    | Completed |
| SC001   | Transfer | 50         | 0.2    | Open      |



| Method              | Formula                                             | Calculation                         | % Task Completed |
| ------------------- | --------------------------------------------------- | ----------------------------------- | ---------------- |
| **Manual**          | -                                                   | -                                   | Manual           |
| **Task Completion** | Task completed / Total no. of Tasks                 | 2/3                                 | 66.66            |
| **Task Progress**   | Sum of % Progress of all Tasks / Total No. of Tasks | (100+100+50)/3                      | 83.33            |
| **Task Weight**     | Sum of (Task weight + % Progress)                   | (0.4 * 100 + 0.2 * 100 + 0.2 * 100) | 70               |


**Note:** If the total weight of the Tasks is not 100, then the calculated result will be divided by the total weight. For example, if the total of task weights is 70, then the percentage completed = (70/0.8)% = 87.5%.

## Project Configuration

### Customer, Sales, and Access Control

- **Customer**: If a Project is being carried out for a particular Customer, the details can be fed in here.
- **Sales Order**: If the Project originates from a Sales Order, you can fetch its details here.  This allows you to:
  - Track Project execution against the Sales Order
  - Update Customers on progress as per the agreed scope
- **Project Users and Access**:  You can add Website Users to the Project to grant them access. This is useful for:
  - Customers who want to monitor progress or provide feedback
  - Suppliers, Freelancers, or Contractual Employees working on the Project. You can also: 
    - Send a **Welcome Email** when adding a user
    - Control **Attachment Viewing permissions** for each user
- **Notes**: You can add any additional notes to the project.

> Learn more about allowing users to view projects - click [here](/erpnext/project-customer-portal)

![](/files/imagebf5e91.png)

### **Project Timeline Tracking**

- **Actual Start Date**: The Actual Start Date and Time are automatically captured based on the first Timesheet entry linked to the Project.
- **Actual End Date**: The Actual End Date and Time are automatically recorded based on the latest Timesheet update for the Project.

> To learn more about Timesheets, click [here](/erpnext/timesheets).

![](/files/image1e72e3.png)

### Costing, Billing, and Financial Tracking

- **Estimated Cost**: Enter the Estimated Cost of the Project.
- **Total Sales Amount**: If you have already linked the Project with a Sales Order, the Total Sales Order Amount will be auto-populated here.
- **Total Costing Amount**: The system will automatically fetch the Total Costing Amount from all the Timesheets linked to this project.
- **Total Billable Amount**: The system will automatically fetch the Total Billable Amount from all the Timesheets linked to this project.
- **Total Expense Claim**: Based on the expenses claimed by an Employee for the completion of the Project, the Total Expense Claim will be auto-calculated.
- **Total Billed Amount**: The Total Billed Amount gets auto-populated in the system using the Sales Invoice created against the Sales Order.
- **Total Purchase Cost**: The Total Purchase Cost of a Project is the cost fetched from the Purchase Invoices that get created against a Purchase Order issued for supply of Materials required for a Project.
- **Total Consumed Material Cost**: Using the Stock Entry made as per the requirement of Materials in the Project, the Total Consumed Material Cost gets captured.

### Margin

**Gross Margin**: Gross Margin would give you the margin you have between your Total Costing Amount and the Total Billed Amount.

```
Gross Margin = (Total Sales Amount + Total Billable Amount) 
                - Total Costing Amount 
                + Total Billable Amount 
                + Total Expense Claim 
                + Total Purchase Cost + Total Consumed Material Cost)
```

**Gross %**: The percentage of the Total Billed Amount spent in the Total Costing Amount makes for the Gross %.

```
 ((Total Sales Amount + Total Billable Amount)
 - Total Costing Amount + Total Billable Amount
 + Total Expense Claim + Total Purchase Cost 
+ Total Consumed Material Cost) / Total Sales Amount) 100*
```

![](/files/imagecf9da7.png)

### Monitor progress

When you enable the 'Collect Progress' option by checking the box, it will enable you to add monitoring details to the project. A report on the progress of the project shall be sent to all stakeholders of the project.

- **Holiday List**: You can select the Holiday List for your company. This will allow you to collect the Progress Reports only on the Working Days.
- **Frequency**: You can set the frequency at which you wish to get the reports. It can be set to an hourly, twice daily, daily or on a weekly frequency.

![](/files/imagebeb9e1.png)

## Related Topics

1. [Task](/erpnext/tasks)
2. [Project Type](/erpnext/project-type)
3. [Project Template](/erpnext/project-template)

<!-- page: erpnext/erpnext__projected-quantity.md -->
---
title: "Projected Quantity\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projected-quantity"
updated: "2026-03-02"
---


**Projected Quantity is the level of stock that is predicted for a particular Item based on the current stock levels and other requirements.**

It is the quantity of gross inventory that includes supply and demand in the past which
is done as part of the planning process.

The projected inventory is used by the planning system to monitor the reorder
point and to determine the reorder quantity. The projected Quantity is used by
the planning engine to monitor the safety stock levels. These levels are
maintained to serve unexpected demands.

Having tight control of the projected inventory is crucial to determine
shortages and to calculate the right order quantity.

![Projected Quantity](/files/projected_quantity.png)

The formula to calculate projected quantity is as follows:

*Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty - Reserved Qty for Production - Reserved Qty for Subcontracting - Reserved Qty for Production Plan*

* **Actual Qty**: Quantity available in the Warehouse. This is the actual physical stock you have.
* **Planned Qty**: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
* **Requested Qty**: Quantity requested via a [Material Request](/erpnext/material-request). It is added on submission of Material Request and subtracted when Purchase Order/Work Order/Stock Entry is created against it based on the Material Request type.
* **Ordered Qty**: Quantity ordered for purchase ([Purchase Order](/erpnext/purchase-order)), but not received (via a [Purchase Receipt](/erpnext/purchase-receipt) or a [Purchase Invoice](/erpnext/purchase-invoice).
* **Reserved Qty**: Quantity ordered for sale by your Customer ([Sales Order](/erpnext/sales-order)), but not delivered (via a [Delivery Note](/erpnext/delivery-note)). This quantity increases when a Sales Order is submitted and decreases when a Delivery Note or Sales Invoice is created against that Sales Order is submitted.
* **Reserved Qty for Production**: Raw materials are reserved on submission of [Work Order](/erpnext/work-order) and is reduced when raw materials are transfered to Work in Progress warehouse via a Stock Entry.
* **Reserved Qty for Subcontracting**: Raw materials reserved when a subcontracting Purchase Order is submitted. When raw materials are transfered to Supplier Warehouse via a Stock Entry, this quantity reduces. To know more about subcontracting [click here](/erpnext/subcontracting).
* **Reserved Qty for Production Plan**: Raw materials are reserved when a Production Plan is submitted. When materials are reserved for the production against the work order then the system will reduce the "Reserved Qty for Production Plan" in the respective BIN. The system reduces the quantity if the work order was made against the production plan.

#### Related Topics
1. [Warehouse](/erpnext/warehouse)
1. [Material Request](/erpnext/material-request)

<!-- page: erpnext/erpnext__projects-introduction.md -->
---
title: "Project Overview"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects-introduction"
updated: "2026-02-26"
---

### **Overview**

The Project Module in ERPNext is used to plan, track, and manage projects within the system. It helps organize project work, monitor progress, and keep track of time and costs, while remaining closely integrated with other ERPNext modules.

Projects in ERPNext act as a central point for tasks, timesheets, expenses, and billing. This makes it easier to track work progress and understand the project's actual cost and outcome without relying on external tools.

### **Key Features**

The Project Module offers a comprehensive set of features to manage projects end-to-end:

- **Projects and Tasks**  
Create projects and define tasks with assigned users, status, and timelines.
- **Timesheets**  
Log time spent on tasks and associate it with projects.
- **Cost Tracking**  
Record project-related expenses and material usage.
- **Billing**  
Create invoices based on time logs, milestones, or fixed project values.
- **Integration with ERPNext**  
Projects are linked with Accounting, HR, Sales, Purchase, and Inventory modules.

<!-- page: erpnext/erpnext__projects__introduction__getting-started.md -->
---
title: "Getting Started"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects/introduction/getting-started"
updated: "2026-02-06"
---

The Project Module in ERPNext is used to track work that involves multiple steps, people, and transactions. A project brings together tasks, time, materials, deliveries, and billing under a single reference.

The example below shows how a simple manufacturing job can be managed as a project and how it connects with other ERPNext modules.

## Scenario**:**

A manufacturing company receives an order to make a **custom metal storage rack** for a warehouse customer.

### **Prerequisites**:

- Create an [Item](https://docs.frappe.io/erpnext/user/manual/en/item) - Storage Rack

### Step 1: Create a Sales Order for the rack

- To create a sales order, go to:

> Home > Selling  > Sales Order

![](/files/sales_order.png)
*Sales order with the Storage Rack*

### Step 2: **Create the project from the Sales Order**

- After the sales order is submitted, we can create the project from it
- ![](/files/project from sales order.png)
*Creating project from Sales Order*
- Once the project is created, the dashboard will be created, which will allow the creation of tasks and timesheets
- ![](/files/project dashboard.png)
*Project Dashboard*

### Step 3:  **Creating the Basic Tasks for the project**

- We create separate tasks for the project, like cutting and welding, painting, and final assembly. 
- ![](/files/taskf4bc2a.png)
*Task for Cutting & welding*

### **Step 4: Create purchase orders for the raw materials and respective stock entries as well**

- The raw material required for making the Storage rack would be purchased, therefore the purchase order would be made for the same 
- ![](/files/purchase order.png)
*Purchase order for raw material*

### Step 5: **Create a timesheet to record the execution of steel sections and paints**

- To maintain the execution of the steel sections and the painting of the storage rack, we create a timesheet 
- The changes made in this project will reflect the costing and billing details
- ![](/files/timesheet.png)
*Execution details in timesheet*

### **Step 6: As the process continues, we update the task with its progress**

![](/files/task status.png)
*Task Status *

- Once all the tasks are completed, the project moves into a fully completed state as well

![](/files/completed project.png)
*Final Project Status*

<!-- page: erpnext/erpnext__projects__project-settings.md -->
---
title: "Project Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects/project-settings"
updated: "2026-02-25"
---

# Settings

There are certain settings that are available for the Project module, which allow for handling overlap time scenarios, and the billing settings control whether logged time can be invoiced. These are all disabled by default. 

The settings available are: 

![](/files/imagee007f5.png)
*Project Settings*

### Ignore Workstation Time Overlap

When **enabled**, ERPNext allows multiple overlapping time logs against the same workstation. It would be useful in places where workstations are shared

### Ignore User Time Overlap

When **enabled**, ERPNext allows overlapping time entries for the same user. It would be useful for users who log time on behalf of multiple employees or teams.

### Ignore Employee Time Overlap

When **enabled**, ERPNext allows overlapping time entries for the same employee. This can be useful at times activity tracking is done and no strict hour validation is required like the HR use cases

### Fetch Timesheet in Sales Invoice

When **enabled**, billable Timesheet entries can be fetched directly into a **Sales Invoice**.

This allows:

- Billing customers based on logged hours
- Automatic population of invoice items from Timesheet Details linked to a Project

<!-- page: erpnext/erpnext__promotional-scheme.md -->
---
title: "Create Promotional Schemes and Discount Slabs | ERPNext Documentation"
description: "Configure ERPNext Promotional Schemes with quantity and amount slabs, party conditions, validity, priorities, and generated Pricing Rules."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/promotional-scheme"
updated: "2026-07-25"
---

A Promotional Scheme manages one or more discount slabs and generates the corresponding [Pricing Rules](/erpnext/pricing-rule). Use it when an offer needs several quantity or amount tiers, mixed-item conditions, cumulative purchases, or a discount on another Item.

## Before you begin

Create the required:

- [Items](/erpnext/item), Item Groups, or Brands.
- [Customers](/erpnext/customer), Customer Groups, Territories, Sales Partners, or Campaigns used as conditions.
- Selling or buying [Price Lists](/erpnext/price-lists) and Item Prices.

Define the business rule in plain language before configuring slabs. Include eligible parties, items, dates, currency, warehouses, thresholds, and whether purchases accumulate.

## Create a Promotional Scheme

1. Open the Promotional Scheme list and select **Add Promotional Scheme**.
2. Enter a descriptive title.
3. Select what the scheme applies on: Item Code, Item Group, Brand, or Transaction.
4. Add the eligible values in the table.
5. Select Selling, Buying, or both.
6. Add party conditions when the scheme is restricted.
7. Add Price Discount or Product Discount slabs.
8. Set validity, currency, warehouse, and priority when applicable.
9. Save.

![An ERPNext Promotional Scheme with applicability and party settings.](https://novacompanies.m.frappe.cloud/files/promotional-scheme-form.png)

Saving the scheme creates linked Pricing Rules. Manage the scheme as the source of the slab configuration instead of editing generated rules independently without understanding the relationship.

## Configure discount slabs

Each slab can use minimum and maximum quantity or amount thresholds.


| Field             | What it controls                                      |
| ----------------- | ----------------------------------------------------- |
| Min Qty / Max Qty | Quantity range that qualifies                         |
| Min Amt / Max Amt | Value range that qualifies                            |
| Rate or Discount  | Price reduction for the qualifying slab               |
| Product Discount  | Free Item and quantity for the slab                   |
| Rule Description  | Operational explanation of the offer                  |
| Warehouse         | Limits the rule to Items selected from that Warehouse |
| Priority          | Resolves conflicts with other applicable rules        |


Leave a maximum blank only when the slab should have no upper limit. Avoid overlapping slabs unless the intended priority is explicit.

## Mixed Conditions

Enable **Mixed Conditions** when quantities or values from several eligible Items should be combined before testing a threshold.

For example, if laptop sleeves and docks are both eligible and Min Qty is 10, the rule can qualify when their combined quantity reaches 10.

## Cumulative purchases

Enable **Is Cumulative** when ERPNext should evaluate qualifying transactions over time for a party. Define amount thresholds and the applicable period. The discount applies to the transaction that crosses the threshold, not retroactively to earlier transactions.

Verify which submitted transaction types your current version includes in cumulative evaluation before launching the program.

## Apply a scheme to another Item

Use **Apply Rule On Other** when the condition is based on one set of Items but the discount applies to another. Test the transaction with all required Items present.

## Test the scheme

Create a new [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order), select an eligible party, and add Items around each slab boundary.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock. Use the highlighted pencil icon to open the full row editor when reviewing applied pricing details.

## Troubleshooting


| Problem                          | What to check                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| No discount is applied           | Verify generated Pricing Rules, eligibility, thresholds, dates, currency, warehouse, and transaction type |
| The wrong slab applies           | Check overlapping ranges and boundary values                                                              |
| Cumulative totals seem incorrect | Confirm party, period, included transaction types, and submitted status                                   |
| Another offer wins               | Review priorities and overlapping Pricing Rules                                                           |
| A scheme change has no effect    | Save the scheme and inspect its generated rules                                                           |


## Frequently asked questions

### When should I use a Promotional Scheme instead of a Pricing Rule?

Use a Promotional Scheme for several slabs or when one managed offer needs multiple generated rules.

### Can a scheme apply to buying transactions?

Yes. Configure Buying applicability and the appropriate Supplier conditions.

### Can a scheme give free Items?

Yes. Use Product Discount slabs.

### Does a cumulative discount adjust earlier invoices?

No. It applies to the qualifying transaction that crosses the threshold.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Applying a Discount](/erpnext/applying-discount)
- [Coupon Code](/erpnext/coupon-code)
- [Buy 1 Get 1 Free Pricing Rule](/erpnext/setting-up-buy-1-get-1-free-pricing-rule)
- [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__purchase-cycle-ledger-impact.md -->
---
title: "Purchase Cycle Ledger Impact"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-cycle-ledger-impact"
updated: "2026-08-02"
---

The purchase cycle begins when you commit to buy from a supplier and ends when the supplier is paid. Not every document creates an accounting entry. A Purchase Order records the commitment, while the Purchase Receipt, Purchase Invoice, and Payment Entry record the inventory, liability, expense, and cash effects that follow.

The examples below use common account names and exclude taxes to keep the entries easy to follow. Your account names may differ. ERPNext uses the accounts configured for the Company, Item, Item Group, warehouse, and transaction.

## Understand when the ledger changes

ERPNext creates General Ledger entries when an accounting or stock transaction is submitted. Saving a draft does not affect the ledger.


| Document                                    | Typical ledger impact                                        | What it represents                                                                                   |
| ------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Purchase Order                              | No General Ledger entry                                      | A commitment to buy goods or services at an agreed quantity, rate, and schedule.                     |
| Purchase Receipt for stock items            | Debit Stock In Hand; credit Stock Received But Not Billed    | Inventory has been received, but the supplier invoice may not have arrived.                          |
| Purchase Invoice against a Purchase Receipt | Debit Stock Received But Not Billed; credit Accounts Payable | The temporary receipt liability is cleared and the confirmed amount becomes payable to the supplier. |
| Purchase Invoice for a service              | Debit the relevant Expense; credit Accounts Payable          | The service cost is recognized and the supplier is owed the invoice amount.                          |
| Payment Entry, Pay                          | Debit Accounts Payable; credit Bank or Cash                  | The supplier liability is reduced and money leaves the company.                                      |


The debit and credit are two sides of the same event. For example, paying a supplier reduces Accounts Payable, so Accounts Payable is debited. It also reduces Bank, so Bank is credited.

## Example 1: Manufacturing company purchasing stock items

Assume a manufacturer purchases five stock-controlled electronic units from Apex Devices at $520 each, for a total of $2,600. The same accounting flow applies when the purchased stock consists of raw materials, components, consumables, or finished goods.

### 1. Submit the Purchase Order

The Purchase Order records what the company agreed to buy, the supplier, rate, warehouse, and expected receipt date. It does not increase inventory, create an expense, or create a supplier payable.

**Ledger impact:** None.



![Submitted Purchase Order for stock-controlled electronic items](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662878970-01-goods-purchase-order-commitment.png)

### 2. Submit the Purchase Receipt

The Purchase Receipt confirms that the stock has physically arrived. ERPNext increases the stock asset and records an equal temporary liability in **Stock Received But Not Billed**.


| Account                       | Debit     | Credit    | Explanation                                                                                     |
| ----------------------------- | ---------: | ---------: | ----------------------------------------------------------------------------------------------- |
| Stock In Hand                 | $2,600.00 |           | Inventory controlled by the company increases.                                                  |
| Stock Received But Not Billed |           | $2,600.00 | The goods have arrived, but the supplier invoice is not yet represented as a confirmed payable. |


![General Ledger entries created by the Purchase Receipt](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879163-02-goods-purchase-receipt-ledger.png)

**Stock Received But Not Billed** is a clearing account. It allows the physical receipt and the supplier invoice to be recorded on different dates without losing the liability created by the receipt.

### 3. Submit the Purchase Invoice

When the supplier invoice is recorded against the Purchase Receipt, ERPNext moves the amount from the temporary receipt liability to the supplier's payable account.


| Account                       | Debit     | Credit    | Explanation                                                         |
| ----------------------------- | ---------: | ---------: | ------------------------------------------------------------------- |
| Stock Received But Not Billed | $2,600.00 |           | The temporary liability created by the Purchase Receipt is cleared. |
| Accounts Payable (Creditors)  |           | $2,600.00 | The confirmed amount is now owed to the supplier.                   |


![General Ledger entries created by the stock Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879221-03-goods-purchase-invoice-ledger.png)

The Stock In Hand debit is not repeated on the invoice because the Purchase Receipt already increased inventory. Across the receipt and invoice together, Stock In Hand remains debited and Accounts Payable remains credited, while Stock Received But Not Billed returns to zero.

### 4. Pay the supplier

Submit a Pay-type Payment Entry and allocate it to the Purchase Invoice.


| Account                      | Debit     | Credit    | Explanation                                 |
| ---------------------------- | ---------: | ---------: | ------------------------------------------- |
| Accounts Payable (Creditors) | $2,600.00 |           | The amount owed to the supplier is cleared. |
| Bank                         |           | $2,600.00 | Money leaves the company's bank account.    |


![General Ledger entries created by the supplier Payment Entry](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879279-04-goods-supplier-payment-ledger.png)

The Payment Entry does not increase inventory or recognize the purchase again. Those effects were already recorded by the Purchase Receipt and Purchase Invoice. The payment only settles the supplier liability.

## Example 2: Services company purchasing a service

Assume a services company purchases ten device-setup support sessions from Vertex Components at $200 each. The total supplier charge is $2,000.

A non-stock service does not increase inventory, so a stock Purchase Receipt is normally unnecessary. The company can move from Purchase Order to Purchase Invoice and Payment Entry. Use a receipt or acceptance workflow only when the business needs a separate operational confirmation that the service was delivered.

### 1. Submit the Purchase Order

The Purchase Order records the scope, quantity, rate, supplier, and expected completion date. It does not create an expense or supplier payable.

**Ledger impact:** None.



![Submitted Purchase Order for externally supplied services](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879418-05-service-purchase-order-commitment.png)

### 2. Submit the Purchase Invoice

When the supplier invoice is accepted, ERPNext recognizes the service expense and creates the supplier liability.


| Account                                         | Debit     | Credit    | Explanation                                   |
| ----------------------------------------------- | ---------: | ---------: | --------------------------------------------- |
| Administrative or Professional Services Expense | $2,000.00 |           | The service cost is recognized in the period. |
| Accounts Payable (Creditors)                    |           | $2,000.00 | The company now owes the supplier.            |


![General Ledger entries created by the service Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879498-06-service-purchase-invoice-ledger.png)

Choose the expense account that describes the service and supports useful reporting. For example, legal work may use Legal Expenses, rent may use Office Rent, and outsourced implementation may use Professional Services or an appropriate project expense account.

### 3. Pay the supplier

The supplier payment has the same basic effect as it does for a stock purchase.


| Account                      | Debit     | Credit    | Explanation                        |
| ---------------------------- | ---------: | ---------: | ---------------------------------- |
| Accounts Payable (Creditors) | $2,000.00 |           | The supplier liability is cleared. |
| Bank                         |           | $2,000.00 | The bank balance decreases.        |


![General Ledger entries created by the service supplier payment](https://novacompanies.m.frappe.cloud/files/purchase-cycle-ledger-1785662879568-07-service-supplier-payment-ledger.png)

## Compare the two workflows


| Stage          | Manufacturing or stock purchase                                   | Service purchase                                         |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| Purchase Order | No ledger impact                                                  | No ledger impact                                         |
| Receipt        | Debits Stock In Hand and credits Stock Received But Not Billed    | Usually no stock receipt or inventory posting            |
| Invoice        | Debits Stock Received But Not Billed and credits Accounts Payable | Debits the selected Expense and credits Accounts Payable |
| Payment        | Debits Accounts Payable and credits Bank                          | Debits Accounts Payable and credits Bank                 |


If a stock-item Purchase Invoice is submitted with **Update Stock** enabled, ERPNext can combine the stock effect of a Purchase Receipt with the payable effect of the Purchase Invoice. The simplified posting is debit Stock In Hand and credit Accounts Payable. This is useful for direct purchases, but it removes the separate receipt document from the audit trail.

If a Purchase Invoice is created directly without a Purchase Order, it still creates its normal ledger entries. What is missing is the earlier procurement commitment, approval trail, expected delivery tracking, and comparison of ordered, received, and invoiced quantities.

## Frequently asked questions

### Does submitting a Purchase Order affect the General Ledger?

1. A Purchase Order records a procurement commitment. It does not create inventory, expense, tax, payable, or bank entries.

### Why is Stock Received But Not Billed used?

It bridges the timing difference between receiving stock and receiving the supplier invoice. The Purchase Receipt credits it, and the linked Purchase Invoice debits it. The account should clear when receipts and invoices match.

### What changes when purchase tax is included?

Accounts Payable is credited for the full supplier invoice. The purchase or expense amount is debited to its normal account, and recoverable input tax is debited to the configured tax asset account. Non-recoverable tax may instead become part of the item cost or expense, depending on configuration and local rules.

### Why does Stock Received But Not Billed have a remaining balance?

Check for Purchase Receipts that have not yet been invoiced, Purchase Invoices that do not reference the correct receipts, quantity or rate differences, returns, and backdated cancellations. Use the Purchase Receipt and Purchase Invoice references to reconcile the difference.

## Related topics

- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)
- [Buying module](/erpnext/buying)

<!-- page: erpnext/erpnext__purchase-invoice-account-type-error.md -->
---
title: "Purchase Invoice - Account Type Error\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-invoice-account-type-error"
updated: "2026-08-14"
---

Nova Industries receives a supplier bill from Apex Components, its regular parts supplier. ERPNext blocks the Purchase Invoice with the message that **Credit To must be a Balance Sheet account**. The message is protecting the payable: the supplier amount must sit in a liability account until Nova pays it.

## Fix the error

1. Open the Purchase Invoice and check **Credit To**.
2. Select the supplier payable account for the company, commonly Creditors or Accounts Payable.
3. Open that account in the Chart of Accounts and confirm it is under Liabilities and has Account Type **Payable**.
4. Set the correct default payable account on the Supplier or Company if the wrong account keeps returning.
5. Save and submit the invoice again.

![Purchase Invoice with the complete Credit To field highlighted](https://novacompanies.m.frappe.cloud/files/purchase-invoice-credit-to-v2.png)



## Why the account must be a liability


| Entry            | Debit                                     | Credit           |
| ---------------- | ----------------------------------------- | ---------------- |
| Supplier invoice | Expense, stock, asset, or service account | Supplier payable |
| Supplier payment | Supplier payable                          | Bank or cash     |


## Troubleshooting

### The correct account does not appear

Confirm that the account belongs to the invoice company, is not a group, is enabled, and has Account Type Payable. Also check the Supplier’s company-specific default account.

## Frequently asked questions

### Can I credit an expense account instead?

Use an expense or stock account on the debit side for what was purchased. The unpaid supplier balance belongs in a payable liability account.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__purchase-invoice.md -->
---
title: "Purchase Invoice | ERPNext Documentation"
description: "Create, verify, submit, pay, return, and track supplier Purchase Invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-invoice"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, sends a bill for phone screens that have already been received. Until that bill is recorded, Nova Industries has stock but no formal payable showing how much it owes the supplier.



A Purchase Invoice records the supplier's bill, creates the payable, and posts the expense, asset value, and taxes. It can be created from a Purchase Order, a Purchase Receipt, or entered directly.



Use a Purchase Invoice when a supplier has billed your company for goods or services. Submission updates the supplier balance and the General Ledger.



## Before you begin

You need:

- a [Supplier](/erpnext/supplier) with the correct currency and payment terms;
- Items or expense accounts for the purchase;
- a Company with a default payable account and Cost Center;
- applicable [Purchase Taxes and Charges Templates](/erpnext/purchase-taxes-and-charges-template);
- a Purchase Order or Purchase Receipt when the invoice must update an earlier buying document.

Confirm whether the goods have already been received. If a Purchase Receipt exists, invoice from it. If goods and the bill arrive together, you may use **Update Stock** on the Purchase Invoice instead of creating a separate receipt.

## Create a Purchase Invoice

1. Go to **Accounting &gt; Purchase Invoice**.
2. Select **Add Purchase Invoice**.

![Purchase Invoice list with Add Purchase Invoice highlighted](https://novacompanies.m.frappe.cloud/files/purchase-payables-01-purchase-invoice-list.png)

3. Select the **Supplier**. ERPNext fetches the payable account, currency, price list, addresses, and payment terms from the relevant defaults.
4. Enter the Supplier's invoice number in **Supplier Invoice No** and its date in **Supplier Invoice Date**. Use the date printed on the Supplier's bill, not the date on which you enter it.
5. Review the **Posting Date** and **Due Date**.

![Supplier, bill reference, and due date on a Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-02-supplier-bill-and-dates.png)

6. Add the Items. Enter the billed quantity and rate, then verify the expense account, Cost Center, Warehouse, and tax treatment.

The colored dot before an Item Code shows stock availability at a glance. Green means in stock and red means out of stock.

Select the highlighted pencil icon to open the full Item row. This is where you can review fields that are not shown as columns in the table.

![Purchase Invoice Items table with the row pencil highlighted](https://novacompanies.m.frappe.cloud/files/purchase-payables-03-items-and-edit-row.png)

Check the **Accepted Qty**, **Rate**, UOM, expense account, Cost Center, and any linked Purchase Order or Purchase Receipt row. ERPNext calculates the amount from the quantity and rate.

![Quantity and rate in a Purchase Invoice Item row](https://novacompanies.m.frappe.cloud/files/purchase-payables-04-item-quantity-and-rate.png)

7. Review taxes, discounts, additional charges, payment schedule, rounding, and the Grand Total.
8. Save the draft and compare it with the Supplier's bill.
9. Select **Submit** when the document is correct.

## Alternative ways to create a Purchase Invoice

### From a Purchase Order

Open a submitted Purchase Order and select **Create &gt; Purchase Invoice**. ERPNext copies the Supplier, Items, quantities, rates, taxes, and references. Adjust only the quantities that are being billed now. This method updates the order's billed percentage after submission.

Use this route when the invoice arrives before receipt, or when your business does not use Purchase Receipts for that purchase.

### From a Purchase Receipt

Open a submitted Purchase Receipt and select **Create &gt; Purchase Invoice**. This carries the received quantities and receipt references into the invoice. The invoice normally clears the **Stock Received But Not Billed** value created by the receipt and establishes the Supplier payable.

This is the preferred route when receiving and invoice verification are separate responsibilities.

### Using Get Items From

In a new Purchase Invoice, select **Get Items From** to fetch one or more eligible Purchase Orders or Purchase Receipts for the same Supplier. Use this when a single Supplier invoice covers several orders or receipts.

### Direct Purchase Invoice

Create the invoice directly when there is no preceding order or receipt, such as a utility bill, professional service, rent, or a small approved expense. A direct invoice creates the payable but does not update a Purchase Order's billed status.

### Recurring supplier invoices

Use [Auto Repeat](/erpnext/auto-repeat) or a Supplier [Subscription](/erpnext/subscription) for recurring charges. Choose Auto Repeat when you want scheduled copies of a reference document. Choose Subscription when billing follows a defined subscription plan and service period.

## Important fields and what they mean


| Field                        | What it controls                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Supplier                     | The party to whom the amount is payable. It also provides currency, payable account, tax, and payment defaults.                                  |
| Supplier Invoice No          | The Supplier's own bill reference. It helps prevent duplicate entry and supports audit matching.                                                 |
| Supplier Invoice Date        | The date on the Supplier's bill. Use it for document reference and ageing controls.                                                              |
| Posting Date and Time        | The accounting and optional stock posting date. Closed periods and frozen accounts can restrict it.                                              |
| Due Date                     | The date by which payment is expected. Payment terms can calculate it automatically.                                                             |
| Credit To                    | The payable ledger credited when the invoice is submitted. Normally use a common payable account with the Supplier recorded as the party.        |
| Update Stock                 | Posts receipt of stock through the Purchase Invoice. Leave it clear when a Purchase Receipt already records the stock movement.                  |
| Is Paid                      | Records payment with the invoice when this workflow is enabled and the required payment account is selected.                                     |
| Is Return (Debit Note)       | Converts the Purchase Invoice into a Debit Note that reduces or reverses a Supplier bill.                                                        |
| Apply Tax Withholding Amount | Calculates configured Supplier withholding tax. Verify the category and applicable threshold before submission.                                  |
| Items                        | The products, services, assets, or expenses being billed. Each row can carry its own account, Warehouse, Cost Center, Project, and tax template. |
| Taxes and Charges            | Tax, freight, duty, and other additions or deductions. The charge type determines how each row is calculated.                                    |
| Payment Schedule             | Splits the amount across one or more due dates based on payment terms.                                                                           |
| Accounting Dimensions        | Attributes such as Cost Center, Project, Branch, or custom dimensions used for reporting and controls.                                           |
| On Hold                      | Prevents the invoice from being selected for payment until the hold is released.                                                                 |


## Taxes, currency, and additional charges

Select the correct buying price list and transaction currency before adding Items. ERPNext stores the exchange rate used to convert the invoice into Company currency. Review it when the invoice is in a foreign currency.

Apply the correct tax template or add tax rows manually. Charges can be based on Net Total, a previous row, Actual amount, or other supported calculation types. Check whether freight or duty should affect Item valuation. Use a [Landed Cost Voucher](/erpnext/landed-cost-voucher) when additional costs must be allocated after receipt.

For country-specific taxes, use the regional documentation and fields supplied by the installed localization. Do not copy tax examples from another jurisdiction without confirming the legal and accounting treatment.

## Submit and next steps

Submitting a Purchase Invoice normally:

- credits the Supplier payable account;
- debits expense, asset, stock, or Stock Received But Not Billed accounts based on the workflow;
- posts tax and additional-charge ledgers;
- updates billed quantities on linked Purchase Orders or Purchase Receipts;
- creates Payment Ledger entries used by Accounts Payable and reconciliation.

After submission, use **Create &gt; Payment** to make a [Payment Entry](/erpnext/payment-entry). You can also include the invoice in a [Payment Order](/erpnext/payment-order), reconcile an existing payment, place it on hold, or create a return.

To reduce or reverse the bill, open the submitted invoice and select **Create &gt; Return / Debit Note**.

![Create Return or Debit Note from a submitted Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-05-create-debit-note.png)

Use **View &gt; Accounting Ledger** to inspect the General Ledger effect. If stock was updated, review the Stock Ledger as well.

## Status


| Status            | Meaning                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Draft             | Saved but not posted to the ledgers.                                                           |
| Unpaid            | Submitted with an outstanding payable amount.                                                  |
| Partly Paid       | Payments or credits cover only part of the invoice.                                            |
| Paid              | The outstanding amount is zero.                                                                |
| Overdue           | The invoice remains outstanding after its due date.                                            |
| Return            | The document is a submitted Debit Note.                                                        |
| Debit Note Issued | A Debit Note has been created against the invoice.                                             |
| Canceled          | The submitted document was canceled and its ledger effect reversed according to ERPNext rules. |


## Troubleshooting

### The invoice duplicates stock value

Check whether a Purchase Receipt already exists. Do not enable **Update Stock** on the Purchase Invoice when the receipt already posted the same stock movement.

### A Purchase Order or Purchase Receipt is missing from Get Items From

Confirm that it is submitted, belongs to the same Supplier and Company, has a billable balance, and is not closed. Also verify user permissions.

### The expense account is unexpected

ERPNext can fetch it from the Item, Item Group, Company defaults, or linked receipt accounting. Open the Item row and verify the account and accounting dimensions before submission.

### Payment cannot be created

Confirm that the invoice is submitted, not on hold, has an outstanding amount, and uses a payable account valid for the Supplier and Company.

### Supplier invoice number is rejected as a duplicate

Search existing Purchase Invoices for the same Supplier and bill number. Do not change the reference only to bypass the warning. Confirm whether the bill was already entered.

## Frequently asked questions

### Can I invoice only part of a Purchase Order?

You can. Create the Purchase Invoice from the order and retain only the quantity billed now. Later invoices can bill the remaining quantity.

### Should services use Update Stock?

They should not. Service Items do not require a stock receipt. Post them to the appropriate expense or asset account.

### Can one Purchase Invoice cover several Purchase Receipts?

You can. Use **Get Items From &gt; Purchase Receipt** and select eligible receipts for the same Supplier.

### Can I edit a submitted Purchase Invoice?

Submitted accounting fields are protected. Use Cancel and Amend when permitted, or issue a Debit Note when you need a traceable reduction or return.

## Related topics

- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Debit Note](/erpnext/debit-note)
- [Payment Entry](/erpnext/payment-entry)
- [Accounts Payable](/erpnext/accounts-payable)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)

<!-- page: erpnext/erpnext__purchase-order.md -->
---
title: "Purchase Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-order"
updated: "2026-02-28"
---

**A Purchase Order is a binding contract with your Supplier that you promise to buy a set of items under given conditions.**

It is similar to a Sales Order but instead of sending it to an external party, you keep it for internal records.

> Home > Buying > Purchasing > Purchase Order

![Buying Flow](/files/buying_flow_po.png)

1. Prerequisites

---

Before creating and using a Purchase Order, it is advised that you create the following first:

- [Supplier](/erpnext/supplier)
- [Item](/erpnext/item)

1. How to create a Purchase Order

---

A Purchase Order can be automatically created from a Material Request or Supplier Quotation.

1. Go to the Purchase Order list, click on New.
2. Select the Supplier, required by date.
3. In the items table, select the item by code, you can change the required by date for each item.
4. Set the quantity and the price will be fetched automatically if set in the Item master.
5. Set taxes.
6. Save and Submit. 

![](/files/Screenshot 2026-01-19 at 12.13.45 PM.png)

### 2.1 Setting Warehouses

- **Set Target Warehouse**: Optionally, you can set the default target Warehouse where the purchased Items will be delivered. This will be fetched into the Item table rows.

### 2.2 Fetching Items from Open Material Requests

Items can be fetched into the Purchase Order automatically from open [Material Requests](/erpnext/material-request). For this to work, the following steps need to be done:

1. Select a Supplier in the Purchase Order.
2. Set default Supplier in the Item form under [Item Defaults](/erpnext/item#39-item-defaults).
3. A [Material Request](/erpnext/material-request) needs to be present of type 'Purchase'.
4. Click on the **Get Items from open Material Requests** button below the Supplier name. Now a dialog will appear with Material Requests containing Items for which the default Supplier is the same as the one selected in the Purchase Order. On selecting the Material Requests and clicking on **Get Items**, the Items will be fetched from the Material Requests. 

> **Note:** The **Get Items from Open Material Requests** button is visible as long as the Items table is empty.



![](/files/Screenshot 2026-01-19 at 12.20.15 PM.png)



1. Features

---

### 3.1 Address and Contact

- **Select Supplier Address**: The Supplier's billing address.
- **Select Shipping Address**: The Supplier's shipping address from which they'll be sending the items.
- Address, Shipping Address, Contact, Contact Email will be fetched if saved in the Supplier master.

For India:

- **Supplier and Company GSTIN**: The GST Identification Number of your Supplier and your company.
- **Place of Supply**: For GST, Place of Supply is necessary. It consists of the state's name and number.

### 3.2 Currency and Price List

You can set the currency in which the purchase order is to be stored. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Read about [Price Lists](/erpnext/price-lists) and [Multi-Currency Transactions](/erpnext/accounts/articles/managing-transactions-in-multiple-currencies) to know more.

### 3.3 Subcontracting or 'Supply Raw Materials'

Setting 'Supply Raw Materials' option is useful for subcontracting where you provide the raw materials for manufacturing an item. To know more, visit the [Subcontracting page](/erpnext/subcontracting).

### 3.4 The Items table

- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for [tracking items using barcode](/erpnext/track-items-using-barcode) to know more.
- **Quantity and Rate**: When you select the Item code, its name, description, and UOM will be fetched. The 'UOM Conversion Factor' is set to 1 by default, you can change it depending on the UOM received from the seller, more in the next section.

'Price List Rate' will be fetched if a Standard Buying rate is set. 'Last Purchase Rate' shows the rate of the item from your last Purchase Order. Rate is fetched if set in the item master. You can attach an Item Tax Template to apply a specific tax rate to the item.

- **Item weights** will be fetched if set in the Item master else enter manually.
- **Warehouse**: The warehouse where the items will be delivered, will be auto filled if 'Set Target Warehouse' was set in the Purchase Order. Via Blanket Order, a Blanket Order can be linked, to know more [click here](/erpnext/blanket-order). A 'Project' can be linked to track progress. A 'BOM' or Bill of Materials can also be linked to track progress.
- 'Qty as per Stock UOM' will show the current stock as per the UOM set in the Item master. 'Received Qty' will be updated when the items are billed.
- **Accounting Details**: This section is auto filled for a Purchase Order. 'Expense Account' is the account against which the PO is billed, and Cost Center is the CC against which the PO is charged.

A “Required By” date on each Item: If you are expecting part delivery, your Supplier will know how much quantity to deliver at which date. This will help you from preventing over-supply. It will also help you to track how well your Supplier is doing on timeliness.

**Allow Zero Valuation Rate**: Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

### 3.5 Purchase UOM and Stock UOM Conversion

You can change your UOM as per your stock requirements in the Purchase Order.

For example, if you have bought your raw material in large quantities with UOM - boxes and wish to stock them in UOM - Nos; you can do so while making your Purchase Order.

1. Store UOM as Nos in the Item master. Note that the UOM in the Item master is the stock UOM.
2. In the Purchase Order mention UOM as Box. (Since material arrives in Boxes)
3. In the Warehouse and Reference section, the UOM will be pulled in as Nos (from the Item form):

![Purchase Order - UOM](/files/purchase-order-uom.png)

1. Mention the UOM conversion factor. For example, (1); If one box has 1 kilo.
2. Notice that the stock quantity will be updated accordingly.

![Purchase Order - UOM](/files/po-stock-uom.png)

### 3.6 Taxes and Charges

If your Supplier is going to charge you additional taxes or charge like a shipping or insurance charge, you can add it here. It will help you to accurately track your costs. Also, if some of these charges add to the value of the product you will have to mention them in the Taxes table.

Visit the [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit [this page](/erpnext/tax-category).

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/erpnext/shipping-rule) page.

![Purchase Order Taxes](/files/po-taxes.png)

For example, you buy Items worth X and sell them for 1.3X. So, your Customer pays 1.3 times the tax you pay your Supplier. Since you have already paid tax to your Supplier for X, what you owe your government is only the tax on 0.3X.

This is very easy to track in ERPNext since each tax head is also an Account. Ideally you must create two Accounts for each type of VAT you pay and collect, “Purchase VAT-X” (asset) and “Sales VAT-X” (liability), or something to that effect.

### 3.7 Additional Discount

Other than recording discount per item, you can add a discount to the whole purchase order in this section. This discount could be based on the Grand Total i.e., post-tax/charges or Net total i.e., pre-tax/charges. The additional discount can be applied as a percentage or an amount.

Read [Applying Discount](/erpnext/applying-discount) for more details.

### 3.8 Payment Terms

Sometimes payment is not done all at once. Depending on the agreement, half of the payment may be made before shipment and the other half after receiving the goods/services. You can add a Payment Terms template or add the terms manually in this section.

Read [Payment Terms](/erpnext/payment-terms) to know more.

### 3.9 Terms and Conditions

In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/erpnext/terms-and-conditions)

### 3.10 Print Settings

#### Letterhead

You can print your request for quotation / purchase order on your company's letterhead. Know more [here](/erpnext/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

#### Print Headings

Titles of your documents can be changed. Know more [here](/erpnext/print-headings).

The seller's Additional Discount, Payment Terms, Terms and Conditions can be recorded in your Purchase Order.

### 3.11 More Information

This section shows the status of the Purchase Order, percentage of items received, and percentage of items billed. If this is an Inter-Company Order, the Sales Order can be linked here.

### 3.12 After Submitting

Once you “Submit” your Purchase Order, you can trigger actions these actions:

- You can Add, Update, Delete items in the Purchase Order by clicking on the **Update Items** button. However, you cannot delete items which has already been received.
- Status: Once submitted, you can hold a Purchase Order or Close it.
- Create: From a submitted Purchase Order, you can create the following:
  - [Purchase Receipt](/erpnext/purchase-receipt) - A receipt indicating you've received the items.
  - [Purchase Invoice](/erpnext/purchase-invoice) - An invoice/bill for the purchase order.
  - [Payment Entry](/erpnext/payment-entry) - A payment entry indicates that payment has been made against a purchase order.
  - [Journal Entry](/erpnext/journal-entry) - A Journal Entry is recorded in the general ledger.

![](/files/Screenshot 2026-01-19 at 12.22.53 PM.png)

### 4. Related Topics

1. [Request For Quotation](/erpnext/request-for-quotation)
2. [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
3. [Purchasing In Different Unit](/erpnext/purchasing-in-different-unit)
4. [Amending Purchase Order After Submit](/erpnext/amending-purchase-order-after-submit)

<!-- page: erpnext/erpnext__purchase-receipt.md -->
---
title: "Purchase Receipt\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-receipt"
updated: "2026-06-18"
---

**Purchase Receipts are made when you accept Items from your Supplier usually against a Purchase Order.**

You can also accept Purchase Receipts directly without the need for a Purchase Order. To do this, set Purchase Order  
Required as “No” in Buying Settings.

To access the Purchase Receipt list, go to:

> Home > Stock > Stock Transactions > Purchase Receipt

![Purchase Receipt flow](/files/purchase-receipt-flow.png)

## 1. Prerequisites

Before creating and using a Purchase Receipt, it is advised that you create the following first:

- Purchase Order

> Note: From version-13 onwards we have introduced immutable ledger which changes the rules for cancellation of stock entries and posting backdated stock transactions in ERPNext. Learn more here.

## 2. How to create a Purchase Receipt

A Purchase Receipt is usually created from a Purchase Order. In the Purchase Order, click on Create > Purchase Receipt.

To create a Purchase Receipt manually (not recommended), follow these steps:

1. Go to the Purchase Receipt list, click on New.
2. The Supplier name and the Items can be fetched from the Purchase Order by clicking on 'Get Items from > Purchase Order'.
3. You can set the Accepted Warehouse for all items in this Purchase Receipt. This is fetched if set in Purchase Order.
4. In case any Items are defective, set the Rejected Warehouse where those Items will be stored.
5. Select the Item and enter the quantity in the Items table.
6. The rate will be fetched and the amount will be calculated automatically.
7. You can expand the item row to change the Accepted Warehouse for an Item.
8. Save and submit.
  Purchase Receipt

You can also add a 'Supplier Delivery Note' to the Purchase Receipt if your Supplier has added some notes.  
Using the 'Edit Posting Date and Time' checkbox you can edit the posting time and date of the Purchase Receipt. By default, the date and time are set when you click on the New button.

Is Return: Tick this checkbox if you're returning Items that were not accepted to your Warehouse.

### 2.1 Statuses

These are the statuses a Purchase Receipt can be in:

- **Draft**: A draft is saved but yet to be submitted to the system.
- **To Bill**: Yet to be billed using a Purchase Invoice.
- **Completed**: Submitted and received all the Items.
- **Return Issued**: All the Items have been returned.
- **Cancelled**: Cancelled the Purchase Receipt.
- **Closed**: The purpose of the Close is to manage short-closing. For example, you ordered 20 qty, but closing at 15 qty. The remaining 5 is not to be received or billed.

## 3. Features

### 3.1 Currency and Price List

The currency of the Purchase Receipt is shown in this section, it is fetched from the Purchase Order. The item prices will be fetched from the set Price list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Since the incoming Item affects the value of your inventory, it is important to convert it into your base currency if you have ordered in another Currency. You will need to update the Currency Conversion Rate if applicable.

Read about Price Lists  
and Multi-Currency Transactions  
to know more.

### 3.2 Warehouse details

The following Warehouses set will apply to all Items in the Items table of the Purchase Receipt. You can change the Warehouses for individual Items via the table.

- **Accepted Warehouse**: This is the Warehouse in which you'll accept and store the incoming Items. Usually, this is the 'Stores' Warehouse.
- **Rejected Warehouse:** This is the Warehouse in which you'll keep the rejected Items which were either defective or not up to the quality mark.

#### Subcontracting

- **Raw Materials Consumed**: In case you're subcontracting, select 'Yes' to consume the Raw Materials from the vendor. Read Subcontracting to know more.

### 3.3 Items table

- **Barcode**: You can track Items using barcodes.
- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for tracking items using barcode to know more.
- The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.
- **Received and Accepted**: Set the received, accepted and rejected quantity. The UoM is fetched from the Item master. You will need to update the “UOM Conversion Factor” if your Purchase Order for an Item is in a different Unit of Measure (UOM) than what you stock (Stock UOM).



![Purchase Receipt Items table](/files/purchase-receipt-item.png)

- **Rate**: The Rate is fetched if set in the Price List and the total Amount is calculated.
- **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit this page.
- The Item Weight details per unit and Weight UOM are fetched if set in the Item master.
- **Warehouse and Reference**: You can set the accepted and rejected Warehouses and also add a Quality Inspection, see next section.
- **Serial No, Batch No, and BOM**: If your Item is serialized or batched, you will have to enter Serial Number  
and Batch in the Items table. You are allowed to enter multiple Serial Numbers  
in one row (each on a separate line) and you must enter the same number of  
Serial Numbers as the quantity.

 There are separate fields for entering Serial Numbers of both accepted and rejected Items here. A Batch Number can also be set if you're storing a batch of plastic medicines for example.

 Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

- You can link a BOM here if the Item is being subcontracted. Linking the BOM here will affect the Stock ledger, i.e. the raw material stock will be deducted from the Supplier Warehouse.

 **Note**: The Item has to be serialized or batched for these features to work. If the Item is serialized a popup will appear where you can enter the Serial Numbers.

- Accounting Dimensions help to tag each transaction with different Dimensions without the need for creating new Cost Centers. You need to create Accounting Dimensions first, to know more, visit this page.
- Page Break will create a page break just before this item when printing.

### 3.4 Tracking Quality Inspection

If for certain Items, it is mandatory to record Quality Inspections (if you have set it in your Item master), you will need to update the “Quality Inspection" field. The system will only allow you to “Submit” the  
Purchase Receipt if you update the “Quality Inspection”.

After enabling Inspection Criteria in the Item form for Purchase and attaching a Quality Inspection Template there, Quality Inspections can be recorded in Purchase Receipts.

To know more, visit the Quality Inspection page.

![Quality Inspection](/files/quality-inspection.png)

### 3.5 Raw Materials Consumed

- The **Consumed Items** table contains the Raw Materials consumed by the Supplier in order to receive the Finished Item.
- The **Get Current Stock** button will fetch the current stock of the Consumed Items from the Supplier Warehouse.  
 ![Purchase Receipt](/files/purchase-receipt-consumed-items.png)

### 3.6 Taxes and Valuation

The Taxes and Charges will be fetched from the Purchase Order.

Visit the Purchase Taxes and Charges Template page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit this page.

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the Shipping Rule page.

### 3.6.1 Allocate full Actual Charge to Stock Items Only

#### Problem

For an "Actual" tax/charge under **Consider Tax or Charge for = Valuation / Valuation and Total**, the amount is distributed across **all** items by net amount. Only stock/asset items can carry valuation, so a non-stock (service) item's share is silently dropped from the stock valuation.

That is correct for a genuine tax, but wrong for a charge like **Freight** that should be fully capitalized into the stock items — there was no way to express "put the entire amount into stock valuation".



##### Example — Purchase Receipt


| Item   | Type    | Net Amount |
| ------ | ------- | ---------- |
| Item A | Stock   | 100        |
| Item B | Stock   | 100        |
| Item C | Service | 100        |


Actual valuation charge = **30**

**Before (only behaviour available)** — 30 / 300 = 10 per item; Item C's 10 is dropped:


| Item | Valuation |
| ---- | --------- |
| A    | 110       |
| B    | 110       |
| C    | 0         |


Only 20 is capitalized; 10 is lost from inventory cost.

## Solution

Add an **"Allocate Full Amount to Stock Items"** checkbox on *Purchase Taxes and Charges* rows of type **Actual** (shown only for category Valuation / Valuation and Total).

**Checked (default)** — the amount is distributed over **stock & asset items only**, so the whole charge is capitalized. The freight case now works:


| Item | Valuation |
| ---- | --------- |
| A    | 115       |
| B    | 115       |
| C    | 0         |


30 / 200 = 15 per stock item; the entire 30 is capitalized.

**Unchecked** — previous behaviour is preserved (spread across all items; the non-stock share is not capitalized → 110 / 110 / 0).

Both modes can coexist on one document (e.g. a real tax + a freight charge); each item's share is summed across the charges.

### 3.7 Additional Discount

Any additional discounts to the whole order can be set in this section.  
Read Applying Discount for more details.

### 3.8 More Information

The Status of the Purchase Receipt is shown here and at the top. The various statuses are: Draft, To Bill, Completed, Canceled, and Closed. This section also shows % Amount Billed, i.e. the percentage of amount for which Sales Invoices are created.

### 3.9 Printing Settings

#### Letterhead

You can print your Purchase Receipt on your company's letterhead. Know more here.

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more here.

### 3.10 After Submitting

A Stock Ledger Entry is created for each Item adding the Item in the Warehouse  
by the “Accepted Quantity” If you have rejections, a Stock Ledger Entry is  
made for each Rejection. The “Pending Quantity” is updated in the Purchase  
Order.

After submitting the Purchase Receipt, the following can be created:

- Purchase Return
- Stock Entry
- Purchase Invoice
- Retaining Sample Stock

![Purchase Receipt submit](/files/purchase-receipt-submit.png)

### 3.11 Returning a Purchase Order

Once you've received a Purchase Order using a Purchase Receipt, you can create a return entry in case the Item needs to be returned to the Supplier. To know more, visit the Purchase Return page.

### 3.12 Skipping Purchase Receipt

If you don't want to create a Purchase Receipt after a Purchase Order and directly want to create a Purchase Invoice, enable the feature for it in Buying Settings.

---

#### Changing the value of Items post Purchase Receipt:

Sometimes, certain expenses that add to the total of your purchased Items are known  
only after a while. Common example is, if you are importing the Items, you  
will come to know of Customs Duty, etc only when your “Clearing Agent” sends  
you a bill. If you want to attribute this cost to your purchased Items, you  
will have to use the Landed Cost Voucher. Why “Landed Cost”? Because it represents the charges that you paid when it landed in your possession.

## 4. Related Topics

1. Delivery Note
2. Purchase Order
3. Purchase Invoice
4. Supplier
5. Landed Cost Voucher

<!-- page: erpnext/erpnext__purchase-return.md -->
---
title: "Purchase Return\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-return"
updated: "2026-03-02"
---


**A purchased Item being returned is known as a Purchase Return.**

With the Purchase Return feature, you can return products to the
Supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc.

## 1. Prerequisites
Before creating and using a Purchase Return, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Purchase Invoice](/erpnext/purchase-invoice)

 Or

 [Purchase Receipt](/erpnext/purchase-receipt)


## 2. How to create a Purchase Return
1. First open the original Purchase Receipt, against which supplier delivered the Items.

 ![Original Purchase Receipt](/files/purchase-return-original-purchase-receipt.png)

1. Click on 'Create > Return', it will open a new Purchase Receipt with 'Is Return' checked. Items, Rate, and taxes will negative numbers.

 ![Return Against Purchase Receipt](/files/purchase-return-against-purchase-receipt.png)

1. On submission of Return Purchase Return, the system will decrease item quantity from the mentioned Warehouse. To maintain correct stock valuation, stock balance will also go up according to the original purchase rate of the returned items.

 ![Return Stock Ledger](/files/purchase-return-stock-ledger.png)

1. In the Accounting Ledger, the Stock In Hand account will be credited and the Stock Received but Not Billed account will be debited.

 ![Return Stock Ledger](/files/purchase-return-general-ledger.png)

If Perpetual Inventory enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.

## 3. Impact on Stock Return via Purchase Receipt
On Creating a Purchase Return against a Purchase Receipt:

* The **Returned Quantity** in the original Purchase Receipt along with any Purchase Order linked to it, is updated.

* The original Purchase Receipt's status is changed to **Return Issued** if 100% returned:
 ![Return Issued](/files/purchase-return-issue.png)

### 4. Related Topics
1. [Sales Return](/erpnext/sales-return)
1. [Perpetual Inventory](/erpnext/perpetual-inventory)
