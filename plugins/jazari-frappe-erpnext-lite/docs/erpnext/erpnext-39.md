<!-- Frappe documentation: erpnext, part 39 of 69. Index: docs/INDEX.md -->

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
