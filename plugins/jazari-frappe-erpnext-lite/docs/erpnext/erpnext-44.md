<!-- Frappe documentation: erpnext, part 44 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__print-settings.md -->
---
title: "Print Settings\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print-settings"
updated: "2026-03-02"
---


**In Print Settings you can set your printing preferences like Paper Size, default text size, whether you want to output as PDF or HTML, etc.**

Since ERPNext is a browser-based application, the actual print command is executed by the browser you're using.

To edit Print Settings, go to:
> Home > Settings > Print Settings

[Screenshot on the live page: Print Settings]

There are various configurations available in the Print Settings. Let's learn about them.

## 1. PDF Settings

### 1.1 PDF or HTML

When you email any document (like Sales Order/Invoice) from ERPNext, it is sent in the PDF or HTML format. The file is sent in PDF by default. If you wish to send a document in the HTML format, just uncheck the option "Send Print as PDF".

### 1.2 Repeat Header and Footer in PDF

The letterhead is a master where you can define the standard Header and Footer which is appended to the document's Print Format. If this property is enabled, then Header and Footer are added to each page. If you don't want header and footer repeat on each page, just disable this setting.

### 1.3 PDF Page Size
The default size for printing PDF pages is A4, and you can choose any size from the options defined [here](https://doc.qt.io/archives/qt-4.8/qprinter.html#PaperSize-enum), including custom dimensions defined in millimeters.

## 2. Page Settings

### 2.1 Print With Letterhead

Enabling this property will automatically tick the Letter Head option when printing a document. Note that you need to either set Letter Head as default or select one in the transaction for it to appear in the print view.

### 2.2 Compact Item Print

Transactions like sales orders/invoices have a table detailing items bought or sold. It has multiple columns like Item Name, Description, UoM, Rate Amount, etc. If there are many columns in the Item table, then Print Format looks bit cluttered. You can improve the view of the table by enabling Compact Item Print.

As per this setting, there will be only four columns in the Print Format, namely: Description, Qty, Rate, and Amount.

The values of other columns (like name, description, image, serial nos. etc.) are concatenated in the Description column.

When the checkbox is unticked, the print format looks like this:
[Screenshot on the live page: Incompact Print Format Settings]

This is what the Compact Print Format looks like:
[Screenshot on the live page: Compact Print Format Settings]


### 2.3 Allow Print for Draft

The documents (mostly transactions) have two stages of authentication, Save and Submit. The saved documents are the first draft and not submitted to the system. Hence printing is restricted for the documents at this stage. However, if you wish to permit users to print documents at the Draft stage as well, enable this checkbox.

### 2.4 Always add "Draft" Heading for printing draft documents

Enabling this setting also print "Draft" in the Print Format, thus indicating that document shared is not completely authenticated yet.

### 2.5 Allow Page Break Inside Table

If an item's description captures more than usual space of a page, then enabling this setting will split the item's details to the next page. Hence, a page break will be inserted between the Item Description, and the rest of the details will be pushed to the next page.

### 2.6 Allow Print for Canceled

Canceled transactions are the ones which don't have any impact on the reports. If you wish to allow printing for the canceled transactions, then enable this setting. A transaction can be canceled only once it is submitted.

### 2.7 Print Taxes with Zero Amount

In the sales and purchase transactions, you can add apply multiple taxes on the item. By default, in the print format, only taxes which have some amount calculated are visible. If you wish to also print the tax which was not applied and has zero tax amount, enable this setting.

## 3. Network Printer / Print Server

You can enable print server by filling the print server IP and port. Then chose the default printer.

Before enabling this feature you have to install the `pycups` library.

You may need first to install `cups` library if is not already on your system

For Debian OS Family:

`sudo apt-get install libcups2-dev`

For Red Hat OS Family:

`sudo yum install cups-libs`

After that, install `pycups` in the env using the command:

`./env/bin/pip install pycups`

This is executed from the `frappe-bench` directory.

## 4. Raw Printing

You can enable raw printing and print to many supported thermal printers. Read [Raw Printing](/erpnext/raw-printing) to know more.

### 5. Related Topics
1. [Print Format](/erpnext/print-format)
1. [Print Style](/erpnext/print-style)
1. [Print Headings](/erpnext/print-headings)
1. [Custom Translations](/erpnext/custom-translations)

<!-- page: erpnext/erpnext__print-style.md -->
---
title: "Print Style"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print-style"
updated: "2026-03-02"
---

**'Print Style' helps you define custom CSS styles which can be applied to Print Formats.**

ERPNext comes with preset styles for printing documents. You can also create new styles using CSS that can be applied to all your print formats.

The standard print Styles in ERPNext are: Monochrome, Modern, Redesign and Classic. 

To create a new Print Style go to:


> Home > Settings > Print Style
> 
> 

How to create a new Print Style?
--------------------------------

1. Go to the Print Style list and click on New.
2. Enter a name for the Print Style.
3. Enter the CSS that'll define how the style will look like.
4. Save.

The styles you create here apply to both standard and custom print formats. To find out the various CSS classes available, you can make a standard print format, open in a new page and see the source.

A default Print Style, can be set from [Print Settings](/erpnext/print-settings).

All Print Format styles are based on Bootstrap (Version 3) CSS Framework.

[Screenshot on the live page: Screenshot 2023-12-29 at 12.08.10 PM][Screenshot on the live page: Screenshot 2023-12-29 at 12.08.10 PM]  


If you have enabled developer mode and tick on Standard then system will generate the JSON file for the Print Style. You can contribute a default print style with this.

### Related Topics

1. [Print Format](/erpnext/print-format)
2. [Print Headings](/erpnext/print-headings)
3. [Letter Head](/erpnext/letter-head)
4. [Cheque Print Template](/erpnext/cheque-print-template)

<!-- page: erpnext/erpnext__print.md -->
---
title: "Printing and Branding\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print"
updated: "2026-03-02"
---


Documents that you send to your customers carry your brand and image and they must be tailored to your requirements. ERPNext gives you many options so that you can set your oraganization's branding in your documents.

ERPNext also gives you the option to print barcode labels, POS receipts and send other raw commands to printers using the Raw Printing feature.

### Topics

* print-settings
* print-format-builder
* print-style
* print-headings
* letter-head
* address-template
* terms-and-conditions
* cheque-print-template
* custom-translations
* raw-printing

<!-- page: erpnext/erpnext__printing.md -->
---
title: "Printing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/printing"
updated: "2026-03-02"
---

In ERPNext, the printing feature facilitates the generation of desired documents directly from the system pertaining to the business. Users can effortlessly create and customise templates for various documents such as invoices, purchase orders, sales orders, pay slips etc.

The users can build and maintain various print formats as per the company's branding guidelines including relevant information as per business requirements.

* [Print Format Builder](/erpnext/user/manual/en/print-format-builder)
* [Print Style](/erpnext/user/manual/en/print-style)
* [Print Headings](/erpnext/user/manual/en/print-headings)
* [Letterhead](/erpnext/letter-head)
* [Address Template](/erpnext/user/manual/en/address-template)
* [Terms and Conditions](/erpnext/user/manual/en/terms-and-conditions)
* [Cheque Print Template](/erpnext/user/manual/en/cheque-print-template)
* [Custom Translations](/erpnext/user/manual/en/custom-translations)
* [Raw Printing](/erpnext/user/manual/en/raw-printing)
* [Print Settings](/erpnext/user/manual/en/configurations-print-settings)

  

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



[Screenshot on the live page: Process Deferred Accounting list]

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



[Screenshot on the live page: Manual deferred-income processing run]

For prepaid costs, select **Expense** and use the applicable deferred asset account, such as **Prepaid Expenses - NET**.



[Screenshot on the live page: Manual deferred-expense processing run]

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

[Screenshot on the live page: Auto reconcile Payments enabled in the Payments tab of Accounts Settings]

## Create and run a reconciliation process

### 1. Open the tool

Open **Process Payment Reconciliation** and click **Add Process Payment Reconciliation**.

[Screenshot on the live page: Process Payment Reconciliation list with the add action highlighted]

### 2. Define the scope

Select the **Company**, **Party Type**, **Party**, and **Receivable/Payable Account**. Add date, Cost Center, or Bank/Cash Account filters when you need to narrow the eligible entries.

In this example, select **Nova Electronics Trading**, **Customer**, **Northstar Retail**, **Debtors - NET**, and **Nova Operating Bank - NET**.

[Screenshot on the live page: Process Payment Reconciliation configured for Northstar Retail]

### 3. Save and submit

Save the record, review the scope, and click **Submit**. Submitting places the process in the queue. It does not itself confirm that every entry was reconciled.

[Screenshot on the live page: Saved Process Payment Reconciliation with Submit highlighted]

### 4. Start the queued process

When the status is **Queued**, click **Start / Resume** to begin processing immediately.

[Screenshot on the live page: Queued reconciliation process with Start or Resume and the status highlighted]

### 5. Monitor progress

Keep the record open while ERPNext processes the eligible entries. The progress area, reconciliation log count, and **Running** status show that the job is active.

[Screenshot on the live page: Running reconciliation process with progress and reconciliation log]

### 6. Review the completed process

Wait for the status to become **Completed**. In this example, ERPNext processed **2/2** eligible entries.

[Screenshot on the live page: Completed reconciliation process showing two of two entries processed]

### 7. Verify the accounting result

Open the affected Payment Entry or invoice and verify the allocation. Payment Entry **ACC-PAY-2026-00006** now contains a USD 600 reference to **ACC-SINV-2026-00008**. Its **Unallocated Amount** is USD 0, and the invoice outstanding amount is USD 3,153.

[Screenshot on the live page: Payment Entry showing the invoice reference, allocated amount, and zero unallocated amount]

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

[Screenshot on the live page: Process Statement Of Accounts report filters]

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


[Screenshot on the live page: Customer selection, print preferences, and email settings]

Save the document. Use **Download** to review the consolidated PDF before sending. Use **Send Emails** for an immediate batch. Scheduled emails are queued by the background job at the configured frequency.

## What the customer receives

ERPNext creates a separate email and PDF for each customer. The PDF contains only that customer's ledger for the selected period. If **Include Ageing Summary** is enabled, the same PDF also shows how much is current and how much falls into each overdue bucket.

The example below shows the email composer with the customer-specific statement attached. This is a preview from the demo site. On a production site with an outgoing Email Account, **Send Emails** queues the message for delivery.



[Screenshot on the live page: Customer statement email preview]

The attached statement shows the opening balance, each invoice or payment in the selected period, and the closing balance. Its ageing summary groups the outstanding amount by due date so the customer can see what needs attention.



[Screenshot on the live page: Customer ledger and ageing summary]

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

[Screenshot on the live page: Procurement Tracker]

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

[Screenshot on the live page: Screenshot 2024-08-29 at 11.41.56 AM]  


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

[Screenshot on the live page: Screenshot 2024-08-29 at 11.42.41 AM]  


On selection of a Parent Item in the main item table, its child items will be fetched in Packing List table of the transaction. If child item is the serialized item, you will be able to specify its Serial No. in packing List table itself. On submission of the transaction, the system will reduce the stock level of child items from warehouse specified in Packing List table.

[Screenshot on the live page: Screenshot 2024-08-29 at 11.44.47 AM]  


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
[Screenshot on the live page: Product List View]
*Product List View*

### Product Grid View
[Screenshot on the live page: Product Grid View]
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

[Screenshot on the live page: Task]

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

[Screenshot on the live page: Work Order]

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

[Screenshot on the live page: Work Order]

Once the user submits the Work Order, system will generate the Job Card with the available Workstation's time details. If 'Allow Overtime' is disabled in Manufacturing Settings then the system schedules the job as per the timings defined in the Workstation. If "Allow Production on Holidays" is disabled then the system schedules job only on working days.

### 2.2 Workstation's Production Capacity

In the Workstation, the user can set the 'Production Capacity'. This is the number of Operations the system will allow you work on in this Workstation. For example, if a certain Workstation can handle 10 operations at the same time, enter the 'Production Capacity' as 10.

[Screenshot on the live page: Work Order]

### 2.3 Job Card With Timing

The system will auto-create the Job Card with timing against each operation based upon the time required to complete that operation and Workstation's availability. The user has to set the planned start date and based on the operation time, system calculates the planned end date.

[Screenshot on the live page: Work Order]

### 2.4 Work Order Planned Start Date and End Date

Based on the planned start date and end date, users can calculate the capacity of their work stations. Also, they can track the status of the work order using the Calendar.

To view calendar, goto:

> Work Order List > Calendar > Default

[Screenshot on the live page: Work Order]

### 2.5 Capacity Planning Error

If the Production Capacity days is less than time required to complete the operation then system throws a capacity planning error. In this case, user has to increase the number under "Production Capacity" days in the Manufacturing Settings or reduce the number of finished goods as per the capacity of the Workstations

[Screenshot on the live page: Work Order]

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

  
