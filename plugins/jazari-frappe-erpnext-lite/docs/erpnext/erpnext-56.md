<!-- Frappe documentation: erpnext, part 56 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__selling.md -->
---
title: "Introduction to Selling Module | ERPNext Documentation"
description: "Learn how ERPNext Selling connects customers, quotations, sales orders, deliveries, invoices, payments, pricing, and sales reports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling"
updated: "2026-08-02"
---

The Selling module in ERPNext brings your customer records, quotations, orders, invoices, pricing, and sales reports into one connected workflow. It helps a sales team move from an enquiry to confirmed revenue while operations and finance work from the same information.

Use the module to prepare professional offers, confirm what a customer has ordered, monitor fulfilment, enforce commercial rules, and understand sales performance. Because each transaction can flow into the next, teams spend less time entering the same data repeatedly and gain a clearer audit trail.

## Before you begin

Complete the following setup before processing live sales:

1. Create your [customers](/erpnext/customer) with their billing and shipping addresses.
2. Add the products and services you sell as [items](/erpnext/item).
3. Configure a selling [Price List](/erpnext/price-list) and item prices.
4. Review [Selling Settings](/erpnext/selling-settings) for transaction defaults and validations.
5. Set up taxes, payment terms, warehouses, and user permissions for your process.

You can begin with a small set of masters and add more controls as your sales process matures. For example, credit limits, sales partners, territories, and promotional schemes are useful but are not required for every implementation.

## Understand the sales cycle

[Screenshot on the live page: ERPNext CRM and sales cycle from Lead through Payment, including the direct Sales Order to Sales Invoice path]

The diagram above is the main ERPNext sales cycle. It provides a common reference for this page and for the detailed documentation of Quotation, Sales Order, Delivery Note, Sales Invoice, and Payment Entry.

ERPNext supports four common variations of this cycle:

- **Standard goods sale:** confirm an order, dispatch stocked goods, invoice the customer, and record payment.
- **Direct invoice with stock update:** use one Sales Invoice to dispatch and bill an immediate stock sale.
- **Service sale without stock delivery:** confirm and bill non-stock work without a Delivery Note.
- **Drop-shipped sale:** ask a Supplier to deliver directly to the Customer while you record the sale and purchase.

Choose the shortest variation that still gives your team the control and audit trail it needs. A [Quotation](/erpnext/quotation) proposes terms. A [Sales Order](/erpnext/sales-order) records the commitment. Delivery, invoice, and payment documents record the operational and financial result.

### Standard goods sale

[Screenshot on the live page: Standard goods sale from Quotation through Sales Order, Delivery Note, Sales Invoice, and Payment Entry]

**Best for:** distributors, wholesalers, manufacturers, and businesses that pick and dispatch stocked goods.

The Sales Order confirms what the customer bought. The Delivery Note records goods leaving the Warehouse. The Sales Invoice bills the customer, and the Payment Entry records payment.

- **Set up:** stock Items, Warehouses, prices, taxes, accounts, and payment terms. Use [Selling Settings](/erpnext/selling-settings) to decide whether Sales Order and Delivery Note are mandatory.
- **Optional:** Quotation can be skipped when the order is already confirmed.
- **Benefit:** clear order, delivery, billing, and payment tracking, including partial fulfilment.
- **Tradeoff:** more documents and approvals than a direct sale.

Sales Order is the commitment. Delivery Note updates stock. Sales Invoice and Payment Entry affect the general ledger. If a Delivery Note or Sales Invoice is created directly, it will not update the Sales Order’s delivered or billed percentage unless it is linked correctly.

### Direct invoice with stock update

[Screenshot on the live page: Direct stock sale using a Sales Invoice with Update Stock followed by Payment Entry]

**Best for:** retail counters, small showrooms, spare-parts desks, and simple cash-and-carry sales where goods are handed over immediately.

Create a [Sales Invoice](/erpnext/sales-invoice) and enable **Update Stock**. The same document reduces stock and bills the customer.

- **Set up:** stock Items, a source Warehouse, prices, taxes, stock and income accounts, and permission in [Selling Settings](/erpnext/selling-settings) to invoice without a Sales Order or Delivery Note.
- **Optional:** Quotation, Sales Order, and Delivery Note are normally skipped.
- **Benefit:** the fastest stock-sale workflow, with one document for delivery and billing.
- **Tradeoff:** no order commitment, reservation, pending-delivery queue, or fulfilment percentage.

The submitted invoice affects both the stock ledger and general ledger. Because it is created directly, users must verify the Warehouse, available stock, rates, taxes, address, and payment terms on the invoice itself. See [Sales Invoice](/erpnext/sales-invoice) for the complete invoicing workflow.

### Service sale without stock delivery

[Screenshot on the live page: Service sale from optional Quotation through Sales Order, Sales Invoice, and Payment Entry without a Delivery Note]

**Best for:** consulting firms, agencies, software companies, maintenance providers, training businesses, and project-based teams.

Use non-stock service Items. The Sales Order records the agreed scope and value, and the Sales Invoice bills the customer without a stock delivery.

- **Set up:** disable **Maintain Stock** on service Items, configure income and receivable accounts, and add Projects or Timesheets when work is tracked by milestone or time. Use **Skip Delivery Note** when the Sales Order should complete through billing.
- **Optional:** Quotation and Sales Order can be skipped for simple recurring or immediately billable work. Delivery Note is normally not required.
- **Benefit:** tracks scope, milestones, and partial billing without unnecessary Warehouse transactions.
- **Tradeoff:** a direct invoice gives less visibility into committed scope and remaining billable quantity.

Sales Order is the commitment. Sales Invoice and Payment Entry affect the general ledger, but no stock-ledger entry is created. If the invoice is created directly, link it to the relevant Project when project reporting matters. See [ERPNext for Service Organizations](/erpnext/erpnext-for-services-organization) and [Maintenance Sales Orders](/erpnext/maintenance-sales-orders).

### Drop-shipped sale

[Screenshot on the live page: Drop-shipped sale using Sales Order, supplier Purchase Order, customer Sales Invoice, and supplier Purchase Invoice]

**Best for:** online sellers, trading companies, distributors with supplier-direct fulfilment, and businesses selling bulky or special-order goods they do not store.

The Sales Order records the customer commitment. A linked Purchase Order instructs the Supplier to deliver directly to the Customer. Customer and supplier invoices record the two financial sides.

- **Set up:** Customer, Supplier, Item, shipping address, buying and selling prices, taxes, and accounts. On the Sales Order item row, enable **Supplier delivers to Customer** and select the Supplier.
- **Optional:** Quotation is optional. Delivery Note and Purchase Receipt are normally omitted because the goods never enter your Warehouse.
- **Benefit:** sell a wider range without holding inventory or handling delivery.
- **Tradeoff:** less control over delivery timing and quality, plus more dependence on correct Supplier and shipping details.

Sales Order and Purchase Order are commitments. Sales Invoice and Purchase Invoice affect the general ledger. A correctly configured drop-shipped row does not affect your stock ledger. Create the Purchase Order from the Sales Order so ERPNext carries the Customer address and source references. See [Drop Shipping](/erpnext/drop-shipping-in-erpnext), [Drop Shipping from a Sales Order](/erpnext/drop-shipping-from-a-sales-order), and [Drop Ship Between Subsidiary Companies](/erpnext/assistance-sales-purchase-between-companies).

Creating the next document from its source carries mapped values and updates progress. Creating it directly is valid for a shorter workflow, but it starts a separate transaction chain unless the correct source is linked.

## Open the Selling workspace

From the ERPNext home screen, open **Selling**. The workspace provides shortcuts to common transactions, masters, settings, and reports. It also displays sales indicators such as order count, total sales amount, and average order value.



[Screenshot on the live page: ERPNext Selling workspace showing the complete Sales Order Trends chart, transactions, masters, settings, and reports]

The primary shortcuts at the top help users open Quotations, Sales Orders, and Sales Invoices quickly. Expand the workspace sections to reach pricing tools, settings, and reports.

## What you can manage in Selling

### Customers and relationships

Maintain customer names, contact details, addresses, tax information, payment terms, and accounting defaults. Customer Groups and [Territories](/erpnext/territory) help segment customers for reporting and commercial policies. Credit limits can prevent or warn against transactions that would exceed an approved exposure.

### Quotations

Prepare offers for leads or customers, add products or services, apply taxes and discounts, and record validity and terms. A submitted quotation can be converted into a Sales Order without re-entering its lines. Use quotation status and reports to follow open proposals.

### Sales Orders

A Sales Order records the items, quantities, delivery dates, prices, and terms accepted by the customer. It becomes the central reference for fulfilment and billing. You can create multiple Delivery Notes and Sales Invoices from one order, deliver selected lines, or close an undelivered balance when the customer no longer requires it.

### Invoices and receivables

Sales Invoices post income, taxes, and the customer receivable to the accounts. Depending on your workflow, the invoice can be created from a Sales Order or Delivery Note. Finance teams can then allocate receipts, issue credit notes for returns, and monitor outstanding balances.

### Pricing, promotions, and loyalty

Use a [Pricing Rule](/erpnext/pricing-rule) to apply discounts, special rates, margins, or product discounts when defined conditions are met. Promotional Schemes help manage offers with multiple price or product slabs. Coupon Codes and the [Loyalty Program](/erpnext/loyalty-program) support customer promotions and repeat purchases.

### Sales team performance

Assign a Sales Person or Sales Partner to transactions and distribute contribution percentages when more than one person is involved. Targets can be set by item group, territory, or period, and reports can compare actual sales against those targets.

### Reports and analytics

The workspace includes reports for sales trends, order analysis, customer acquisition, inactive customers, item-wise history, target variance, and partner commissions. Start with [Sales Reports](/erpnext/sales-reports), then select the report that matches the question you need to answer.

## Good practices

- Convert related documents instead of recreating them. This preserves links and reduces data entry.
- Use clear naming and ownership rules for Customer, Address, and Contact records.
- Define who may change prices, discounts, credit limits, and submitted transactions.
- Review pending delivery, pending billing, and outstanding receivable reports regularly.
- Test pricing and tax rules with representative orders before using them in production.

## Frequently asked questions

### Do I have to create every document in the sales cycle?

ERPNext supports shorter workflows. For example, a service company may create a Sales Order and then a Sales Invoice, while a retail sale may use only a Sales Invoice with stock updated.

### Can I sell to a new prospect before creating a Customer?

You can create a Quotation for a Lead. Create the Customer when the prospect is ready to place an order.

### Can one Sales Order be delivered or billed in parts?

Y

es. Create multiple Delivery Notes or Sales Invoices for the quantities completed at each stage. ERPNext tracks the remaining quantity and updates the order’s fulfilment percentages.

### Where should I configure discounts?

Enter a one-time discount on the transaction. Use Pricing Rules or Promotional Schemes when the discount should be applied consistently under defined conditions.

### How do I know which orders still need action?

Use Sales Order statuses and reports for pending delivery and pending billing. The delivered and billed percentages also show progress on each order.

<!-- page: erpnext/erpnext__semi-auto-payment-reconciliation.md -->
---
title: "Semi-Auto Payment Reconciliation | ERPNext Documentation"
description: "Use ERPNext suggestions to match unallocated payments and invoices efficiently."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/semi-auto-payment-reconciliation"
updated: "2026-08-01"
---

Semi-automatic reconciliation helps match unallocated payments with outstanding invoices using party, amount, and date information. Treat suggestions as candidates and review them before posting allocations.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Semi-Auto Payment Reconciliation

1. Open the reconciliation tool and select Company, party type, and party.
2. Load outstanding invoices and unallocated payments.
3. Review suggested matches and compare remittance references.
4. Adjust allocations when the suggestion is incomplete or incorrect.
5. Reconcile and verify the updated outstanding balances.

[Screenshot on the live page: Semi-Auto Payment Reconciliation in ERPNext]

## Important fields and what they mean


| Field              | What it controls                    |
| ------------------ | ----------------------------------- |
| Invoice Amount     | Original invoice value.             |
| Outstanding Amount | Balance still open.                 |
| Payment Amount     | Unallocated amount available.       |
| Allocated Amount   | Amount the tool will link.          |
| Reference and Date | Evidence used to confirm the match. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### Suggested matches are missing

Confirm the party, account, currency, date range, and outstanding or unallocated balances. Improve reference numbers and imported bank descriptions to make matching more reliable.

### The suggested invoice is incorrect

Reject the suggestion and choose the correct reference. Similar amounts and dates are not sufficient when the payer, invoice number, or remittance advice conflicts.

### A payment matches several possible invoices

Review the customer's remittance advice and allocate manually. Do not accept an ambiguous match solely to clear the queue.

## Frequently asked questions

### What does semi-automatic mean?

ERPNext proposes or filters likely matches, but a user reviews and confirms the allocation before it is processed.

### Is it safe to match only by amount?

Amount is one signal. Also compare party, currency, dates, references, and outstanding balances.

### Can one suggested payment be split across invoices?

Use the available allocation controls to divide an eligible payment when the remittance covers several invoices.

### Does accepting a suggestion change the bank statement?

It does not alter the external bank statement. It records the relationship between existing ERPNext payment and invoice entries.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__sending-email.md -->
---
title: "Sending Email from any Document"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sending-email"
updated: "2026-03-02"
---

In ERPNext you can send any document as email (with a PDF attachment) by clicking on Menu > Email after opening any document.

[Screenshot on the live page: Send Email]  


**Note:** You must have outgoing [Email Accounts](/erpnext/email-account) set up for this.

After you click on send, the email gets added to the email queue. It will be in the Sending status until it is Sent. The status of the email is displayed in the queue, if sending has failed, it can be sent by clicking on Send Now.

[Screenshot on the live page: Email Queue]  


The following options are available when sending an Email.

* **TO:** Recipients of the email.
* **From:** If user has access to multiple outgoing email accounts, the user can select which outgoing email account to use. Multiple outgoing email accounts can be configured from the User document by adding them to the "User Email" table.
* **CC**: Carbon Copy of the email. Useful when you want to keep someone in the conversation loop but don't want to address the email directly to them.
* **BCC**: Blind Carbon Copy is similar to CC but everyone else on the email thread cannot see that the mail was also sent to the BCC recipients. This is useful to hide the email address of certain people if you're sending the email to a lot of people who don't necessarily know each other.
* **Email Template**: You can create preset templates to send out standard replies. Email Templates are already available in the system for Dispatch Notification, Leave Status Notification, and Leave Approval Notification. You can set a Default Email Template via [Customize Form](/erpnext/customize-form).
* **Send me a copy**: This will send a copy to your email address. It's useful to ensure that the email was sent without any errors.
* **Send Read Receipt**: Ticking this checkbox will send you a notification if the receiver has read the email. In case of multiple receivers, even if one has read the email, you'll get a notification.
* **Attach Document Print**: Attach the PDF of the document you're sending via email.
* **Select Attachments**: Any additional attachments can be added here.

The following two fields are the fields which appear on the print screen:

[Screenshot on the live page: Email Print Options]  


* **Select Print Format**: The print format of the document. Know more about Print Format [here](/erpnext/print-format).
* **Select Languages**: The language in which the PDF is to be generated.

### Related Topics

1. [Email Domain](/erpnext/email-domain)
2. [Email Account](/erpnext/email-account)
3. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__serial-and-batch-bundle.md -->
---
title: "Serial and Batch Bundle"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-and-batch-bundle"
updated: "2026-02-26"
---

> NOTE: Users must create a separate **Serial and Batch Bundle** for each stock transaction. They cannot use the same **Serial and Batch Bundle** across multiple stock transactions.
>
> *Allow Negative Stock* has been removed for Serial / Batch Items from version 15. From version 15 onward, users cannot make negative stock transactions for serial / batch items, even if *Allow Negative Stock* is enabled in **Stock Settings**.

---

In version 15, we introduced the **Serial and Batch Bundle**. This feature is used to link Serial / Batch Nos in stock transactions.

Before version 15, the *Serial No* field was a Small Text field, which meant one column could hold more than one serial number. Because of this design, there were a lot of data integrity issues. To solve this, we changed the *Serial No* field from Small Text to a Link field in version 15. Since we can't add a child table inside a child table, we added a new DocType: **Serial and Batch Bundle** to pick/dispatch multiple Serial / Batch numbers.

[Screenshot on the live page: Serial no Configure]

## How does this work?

You need to create a **Serial and Batch Bundle** and link it to stock transactions whenever you deal with Serial / Batch numbers. Users must create a separate **Serial and Batch Bundle** for each transaction, and they can't link the same **Serial and Batch Bundle** to multiple transactions.

### Auto Creation of Serial and Batch Bundle for Inward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an inward entry, they must ensure that *Serial Number Series* is set for the serial item and that the *Automatically Create New Batch* checkbox is enabled (with *Batch Number Series* set) for the batch item.

#### For Serial No

[Screenshot on the live page: Serial no Configure]

#### For Batch No

[Screenshot on the live page: Batch no Configure]

After the configuration, when the user creates a **Purchase Receipt** or a **Stock Entry** with the Type "Material Receipt", the system will automatically create the inward **Serial and Batch Bundle** on submission of the record.

[Screenshot on the live page: Auto Serial Batch Bundle Inward]

### Auto Creation of Serial and Batch Bundle for Outward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an outward entry, they must enable the checkbox *Auto Create Serial and Batch Bundle For Outward* in **Stock Settings**. They can also set *Pick Serial / Batch Based On* to "FIFO / LIFO / Expiry" in **Stock Settings**.

[Screenshot on the live page: Auto Serial Batch Bundle Outward Configure]

After the configuration, when the user creates a **Delivery Note** or a **Stock Entry** with the Type "Material Issue", the system will automatically create the outward **Serial and Batch Bundle** on submission of the record.

[Screenshot on the live page: Auto Serial Batch Bundle Outward]

### Manual Creation of Serial and Batch Bundle for Inward Entry

For the **Serial and Batch Bundle**, both **Serial No** and **Batch** records must already exist in the system. With the manual option, the user must first create the **Serial No** / **Batch** records in the system. Users can use the CSV import option to create **Serial No** / **Batch** records. The blank CSV template can be downloaded using the Serial and Batch Selector.

[Screenshot on the live page: create-using-csv]

Complete GIF for manual creation of a **Serial and Batch Bundle** for an inward entry is as follows:

[Screenshot on the live page: manually-create-serial-no-inward]

### Manual Creation of Serial and Batch Bundle for Outward Entry

Using the Serial and Batch Selector, the user can pick the Serial / Batch Nos based on the "FIFO / LIFO / Expiry" method.

[Screenshot on the live page: serial-batch-selector-outward]

Complete GIF for manual creation of a **Serial and Batch Bundle** for an outward entry is as follows:

[Screenshot on the live page: manually-create-serial-no-outward]

### Serial and Batch Bundle Creation Using CSV for Outward Entry



Now users can create serial and batch bundles for outward entries by importing a CSV file.

[Screenshot on the live page]





## History of Serial Numbers

To check the history of serial numbers, see the report "Serial No Ledger".

[Screenshot on the live page]

## Serial / Batch Selector

This is used to select Serial Nos / Batches manually. This popup is also used to create serial nos / batches automatically if they do not exist.

[Screenshot on the live page: serial-batch-selector]

## Disable Serial / Batch Selector

If users don't want to use the Serial and Batch Selector (popup), they can disable it through **Stock Settings**. To disable it, go to **Stock Settings** > Serial and Batch Item (TAB) > enable *Disable Serial No And Batch Selector*, then save.

[Screenshot on the live page: disable-serial-batch-selector]

## Old Serial / Batch Fields

Many customers requested that we retain the old serial and batch fields to address UX issues. In response to this demand, we retained the old serial/batch fields. These fields are solely used for entering serial numbers and batches. The system will automatically create the **Serial and Batch Bundle** upon submission of the stock transaction. To enable this feature, users must navigate to **Stock Settings** and enable the *Use Serial / Batch Fields* option (see the image below).

[Screenshot on the live page: use-serial-batch-fields-global]

After that, when the user creates a stock transaction (for example, a **Delivery Note**), the system will show the old Serial / Batch fields. For more details, see the GIF below.

[Screenshot on the live page: user-old-serial-batch-fieldsd]

Users can disable the old serial / batch fields at the transaction level too.

[Screenshot on the live page: use-serial-batch-for-dn]

## Update Serial / Batch on Creation of Auto Bundle

If the user wants to automatically update the Serial No / Batch in the Serial / Batch fields when a **Serial and Batch Bundle** is created, go to **Stock Settings** and disable *Do Not Update Serial / Batch on Creation of Auto Bundle*.

[Screenshot on the live page: update-Serial-Batch-on-creation-of-auto-bundle]

Case:

1. User has enabled *Use Serial / Batch Fields* in **Stock Settings**
2. User wants to create the **Serial and Batch Bundle** per single batch
3. User has set the auto-create batch in the **Item** master.
4. On submission of the **Purchase Receipt**, the system has created the auto **Batch** and **Serial and Batch Bundle**, and set the *Batch* and *Serial and Batch Bundle* fields on the **Purchase Receipt** line item.
5. Updating the value of the batch takes time. If you want to skip this step, enable *Do Not Update Serial / Batch on Creation of Auto Bundle* in **Stock Settings**.
6. With this, the batch column remains blank, but the **Serial and Batch Bundle** will have the value of the auto-created bundle.

## How to Use **Serial and Batch Bundle**

[https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s](https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s)

<!-- page: erpnext/erpnext__serial-and-batch-traceability-report.md -->
---
title: "Serial No and Batch Traceability Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-and-batch-traceability-report"
updated: "2026-02-27"
---

The Serial and Batch Traceability Report is used to track the full movement and lifecycle of serialized or batched items across your supply chain. Thre are two types of traceability methods


To view Serial No and Batch Traceability Report GoTo 

> Stock > Serial No and Batch > click on "Serial No and Batch Traceability"


## Backward Traceability 

To find out which components are required to manufacture the batch and where they came from, use the Backward Traceability filter.


[Screenshot on the live page]

## Forward Traceability 

To find out where the batch has been used or to whom it was delivered, use the Forward Traceability filter.


[Screenshot on the live page]

## Backward and Forward (Both) Traceability 


[Screenshot on the live page]

<!-- page: erpnext/erpnext__serial-and-batch.md -->
---
title: "Serial and Batch"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-and-batch"
updated: "2026-03-06"
---

From version 16, to enable serial / batch feature for the item, first check the 'Enable Serial and Batch No for Item' checkbox in the 'Stock Settings'.



In ERPNext, serial and batch tracking are integral features for effectively managing inventory items with unique identifiers.

Serial tracking involves assigning a unique serial number to each individual item, enabling businesses to track its lifecycle from procurement to sale. This allows for precise traceability, warranty tracking, and identification of specific items in case of recalls or quality issues.

However, batch tracking involves grouping items with identical attributes, such as manufacturing date or lot number, into batches. This enables businesses to trace and manage batches of items as they move through the supply chain, ensuring compliance with regulations, managing expiry dates, and facilitating recalls if necessary.

Both serial and batch tracking functionalities in ERPNext provide businesses with granular control over inventory management, enhancing traceability, quality control, and compliance efforts.

- [Serial Number](/erpnext/user/manual/en/serial-no)
- [Serial Number Naming](/erpnext/user/manual/en/serial-no-naming)
- [Batch](/erpnext/user/manual/en/batch)
- [Serial and Batch Bundle](/erpnext/user/manual/en/serial-and-batch-bundle)
- [Serial Number Naming](/erpnext/user/manual/en/serial-no-naming)
- [Installation Notes](/erpnext/user/manual/en/installation-note)
- [Managing Batch Wise Inventory](/erpnext/user/manual/en/managing-batch-wise-inventory)

<!-- page: erpnext/erpnext__serial-no-naming.md -->
---
title: "Serial Number Naming"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-no-naming"
updated: "2026-02-26"
---


Serial Nos. is unique value assigned on each unit of an item. Serial no. helps in tracking item's warranty and expiry details. Generally high value items like machines, computers, costly equipments are serialized.

To make item Serialized, in the Item master, check **Has Serial No**.

There are two ways Serial no. can be generated in ERPNext.

###1. Serializing Purchase Items

If purchased items are received with Serial Nos. applied by OEM (original equipment manufacturer), you can follow same Serial No in ERPNext as well. While creating Purchase Receipt, you shall scan or manually enter Serial nos. for an item. On submitting Purchase Receipt, Serial Nos. will be created in the backend as per Serial Nos. provided for an item. If using OEM' Serial No., then in the Item master, Prefix should not be mentioned for serializalization. As per this scenaio, Prefix field should be left blank.

If received items already has its Serial No. barcoded, you can simply scan that barcode for entering Serial No. in the Purchase Receipt. Click [here](https://frappe.io/blog/management/using-barcodes-to-ease-data-entry) to learn more about it.

On submission of Purchase Receipt or Stock entry for the serialized item, Serial Nos. will be auto-generated.

[Screenshot on the live page: Serial Nos Entry]

Generated Serial numbers will be updated for each item.

[Screenshot on the live page: Serial Nos Created]

###2. Serializing Manufacturing Item

To Serialize Manufacturing Item, you can define Series for Serial No. Generation in the Item master itself. Following that series, system will create Serial Nos. for Item when its Production entry is made.

####2.1 Serial No. Series

When Item is set as serialized, it will allow you to mentioned Series for it.

[Screenshot on the live page: Serial Nos Created]

####2.2 Production Entry for Serialized Item

On submission of production entry for manufacturing item, system will automatically generate Serial Nos. following Series as specified in the Item master.

[Screenshot on the live page: Serial Nos Created]

<!-- page: erpnext/erpnext__serial-no.md -->
---
title: "Serial Number"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-no"
updated: "2026-03-06"
---

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.



To enable serial / batch feature for the item, first check the 'Enable Serial and Batch No for Item' checkbox in the 'Stock Settings'.

[Screenshot on the live page]



As discussed in the [Item](/erpnext/item) page, if an **Item** is *serialized*, a **Serial Number** (Serial No) record is maintained for each quantity of that **Item**. This information helps track the location of the Serial No, its warranty and end-of-life (expiry) information.

You can also track from which **Supplier** you purchased the **Serial No** and to which **Customer** you have sold it. The **Serial No** status will tell you its current inventory status.

If your Item is *serialized* you will have to enter the Serial Nos in the related column with each Serial No in a new line. You can maintain single units of serialized items using Serial Number.

To access the Serial Number list, go to: > Home > Stock > Serial No and Batch > Serial No

1. Prerequisites

---

Before creating and using a Serial Number, it is advised that you create the following first:

- [Item](/erpnext/item)
- Enable 'Has Serial No' in the Item master [Screenshot on the live page: Serial No Enabled]

2. How to create a Serial Number

---

Usually, Serial Numbers are auto-created when transactions are made against a serialized Item. This works only when 'Has Serial No' is enabled and a series is set in the Item master.

For example, a series was set for the following Item as 'PB2L.#####'. Then a Stock Entry was submitted to receive the Item. The Serial Numbers were created accordingly.

[Screenshot on the live page: Serial No Created]



However, if you want to create a Serial No *manually* follow these steps:

1. Go to the Serial Number list, click on New.
2. Enter a Serial Number.
3. Enter the Item Code and details will be fetched.
4. If any transaction is done with an item, Serial No cannot be set or unset.
5. Save.

Inventory of an Item can only be affected if the Serial No is transacted via a Stock transaction (Stock Entry, Purchase Receipt, Delivery Note, Sales Invoice). When a new Serial No is created directly, its Warehouse cannot be set.

[Screenshot on the live page: Serial Number]



### 2.1 Notes about Serial Number

- The Status is set based on Stock Entry.
- Only Serial Numbers with status 'Available' can be delivered.
- Serial Nos can automatically be created from a Stock Entry or Purchase Receipt. If you mention Serial No in the Serial Nos column, it will automatically create those serial Nos.
- If in the Item Master, the Serial No Series is mentioned, you can leave the Serial No column blank in a Stock Entry / Purchase Receipt. Serial Nos will automatically be set from that series.

3. Features

---

### 3.1 Purchase/Manufacture details

The document from which the Serial No was created will be shown. If you purchased it from a Supplier, it'll be linked here.

### 3.2 Delivery Details

If the Serial No was generated from a Sales Order, the Customer will be linked here.

### 3.3 Warranty/AMC Details

If the Item is under warranty or AMC (Annual Maintenance Contract), the expiry dates for these can be set.

### 3.4 More Information

Any additional information about this specific Item unit can be set under 'Serial No Details'.

4. Video

---

### 5. Related Topics

1. [Item Codification](/erpnext/item-codification)
2. [Item Variants](/erpnext/item-variants)
3. [Serial Number Naming](/erpnext/serial-no-naming)

<!-- page: erpnext/erpnext__service-level-agreement.md -->
---
title: "Service Level Agreement\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/service-level-agreement"
updated: "2026-02-28"
---


**A service level agreement (SLA) is a contract between a service provider (either internal or external) and the end user on the level of service expected from the service provider.**

SLAs are output-based, their purpose is specifically to define the timeline in which the Customer will receive the service. SLAs do not define how the service itself is provided or delivered.

To access the Service Level Agreement list, go to:
> Home > Support > Service Level Agreement > Service Level Agreement

## 1.Prerequisites

Before creating and using a Service Level Agreement, it is advised that you create/update the following first:

* [Holiday List](/hr/holiday-list)

* Enable **Track Service Level Agreement** in Support Settings

 [Screenshot on the live page: Service Level Agreement]

## 2. How to Create a Service Level Agreement
1. Go to the Service Level Agreement list, click on New.
1. Enter a name for the Service Level.
1. Select an Employee group, that will handle a particular Service Level.
1. Set a Holiday List. Service Level Agreement won't be applied in the days mentioned in the Holiday List.
1. 'Enable' determines if a Service Level Agreement is enabled or disabled.
1. Ticking 'Default Service Level Agreement' will apply this SLA to a customer if they don't have a particular SLA assigned to them.
1. Entity Type: Service Level Agreements can be assigned to a Customer/Customer Group/Territory enabling you to apply Service Level Agreement based on these factors.
1. Entity: Select the specific Customer/Customer Group/Territory.
1. Start / End Date: Defines the validity of the agreement.
1. Priorities: You can set multiple Issue Priorities and their Time to Respond and Resolve (in hours and mins).

 [Screenshot on the live page: Service Level]
1. Default Priority: Default Priority selected in Priorities table that will be applied in the Service Level Agreement.
1. Support Hours: Contains the Days of the week on which Support is provided. Has a Start Time and End Time of the Working day.

 [Screenshot on the live page: SLA Support Hours]
1. Save.

 [Screenshot on the live page: SLA]

## 3. Features
### 3.1 Applies to New Issues

Once an SLA is saved, it'll be applied to Issues raised by Customers/Territories as per the option you chose in 'Entity Type'.

[Screenshot on the live page: SLA in Issue]

### 3.2 Resetting an SLA
An SLA can also be reset until the time does not fail. For example, if the SLA is 3 days, you can reset the SLA only within 3 days of the Issue being created. After that, the Service Level will display failed.

[Screenshot on the live page: SLA Issue]

### 3.3 Time respond / resolve in Issues
The time to respond to an Issue and the time to resolve will be shown:
 [Screenshot on the live page: SLA in Issue]

These times are based on the timelines set in the 'Priority' field in the Service Level's Priorities table.


### 3.4 Pause SLA on Statuses
From version 13 onwards, ERPNext allows you to pause SLA on issues when you are waiting for an event to happen. You can do this by selecting a status that is configured in this "Pause SLA On" table.

* Set the statuses on which you want to pause SLA in the SLA document. You can also add custom statuses here.
 [Screenshot on the live page: Service Level]
* When the status is changed to any of the above, resolution and response fields are unset and the dashboard indicators change to:
 [Screenshot on the live page: Service Level]
* When the status of the issue changes back to a non-hold status (which is not configured in the "Pause SLA On" table), the **Total Hold time** field will be set in your Issue document.
 [Screenshot on the live page: Service Level]
The Response and Resolution time will be recalculated by adding the hold time, thereby restarting your SLA timers.

> Note: Service Level DocType was removed in version 13 and all functions are handled only with the Service Level Agreement DocType.

<!-- page: erpnext/erpnext__session-defaults.md -->
---
title: "Session Defaults | ERPNext Documentation"
description: "Use ERPNext Session Defaults to temporarily prefill a company or other value for one user session without changing global defaults."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/session-defaults"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor with a child company, Nova Electronics Trading. Priya normally works in the parent company's books, but this afternoon she must enter and review only the subsidiary's transactions. Changing the global Company would affect everyone. Re-selecting the subsidiary on every form and report makes it easy to miss one record.



Session Defaults lets Priya choose Nova Electronics Trading for her current login session. New supported transactions and reports can begin with that Company already selected. Other users keep their own context, and the temporary choice is cleared when Priya logs out.

## Allow a value to be used as a Session Default

Open **Session Default Settings** and add the DocTypes that users may choose temporarily. Company is the most common example. Add only fields that provide a useful and unambiguous working context.

[Screenshot on the live page: Company configured as an available ERPNext Session Default]


| Setting                | What it means                                           | Nova example                                                               |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| Session Defaults table | DocTypes available in the user's session-default menu   | Company allows Priya to choose Nova Electronics Trading for the afternoon. |
| Reference DocType      | The master whose record will become the temporary value | Selecting Company presents Companies the user is permitted to access.      |


## Select the value for the current session

Open the user menu or sidebar Session Defaults control, then choose the permitted value. Create a new transaction or open a report and confirm the Company is prefilled. A submitted record must still be checked before relying on the default.

## Understand the scope

Session Defaults affects the current user and current session. It does not change Global Defaults, does not grant access, and does not rewrite existing records. Logging out clears the temporary choice. A value may also be replaced when a mapped source document or a more specific transaction rule supplies the field.

## Troubleshooting

### The Session Defaults option is missing

A System Manager must first add an allowed Reference DocType in Session Default Settings. The user also needs permission to the referenced records.

### The selected Company is not used

Test with a new supported document. A mapped document, user default, or document-specific rule may supply a more specific Company.

### The old value appears after changing it

Reload the form or create a new draft. Existing open forms can retain values loaded before the session change.

## Frequently asked questions

### Does a Session Default apply to other users?

The value belongs to the current user's session. It does not change the common site default.

### Is a Session Default permanent?

Logging out clears it. Use a user default or Global Defaults when the choice should persist according to policy.

### Can it bypass User Permissions?

A default only suggests a value. The user must still have permission to read and use that record.

### Can several DocTypes be configured?

The settings table can allow more than one reference type, but each should provide a clear working context rather than adding clutter.

## Related topics

- [Global Defaults](/erpnext/global-defaults)
- [System Settings](/erpnext/system-settings)
- [Company](/erpnext/company-setup)
- [User Permissions](/erpnext/user-permissions)
- [Adding Users](/erpnext/adding-users)
- [Reports](/erpnext/reports)

<!-- page: erpnext/erpnext__set-language.md -->
---
title: "Set Language | ERPNext Documentation"
description: "Set the default ERPNext language or a user-specific language and understand translation scope, fallback, and verification."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set-language"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. Most employees use ERPNext in English, but the company hires Sofia to coordinate Spanish-speaking customers and suppliers. Changing the whole site to Spanish would disrupt the rest of the team, while forcing Sofia to translate every menu in her head makes routine work slower and more error-prone.



ERPNext separates the site's default language from a user's preferred language. The System Manager can keep English as the shared fallback and set Spanish only for Sofia. When she signs in again, supported labels and messages appear in her language while other users continue in English.

## Set the default site language

Open **System Settings**, choose **Language**, save, and reload the site. Use this when the chosen language should be the default for users who do not have a personal override.

[Screenshot on the live page: Default Language in ERPNext System Settings]

## Set a language for one user

Open the User record, select the preferred **Language**, save, then ask the user to sign out and sign in again. Nova assigns Spanish to Sofia without changing the default for the finance and warehouse teams.

[Screenshot on the live page: Language field on an ERPNext User record]


| Choice                             | Scope                    | Example                                                                                                        |
| ---------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| System Settings Language           | Default for the site     | English remains Nova's shared default.                                                                         |
| User Language                      | One user                 | Sofia sees Spanish where translations exist.                                                                   |
| Written master or transaction text | The saved content itself | A Customer name or Item description remains the language in which it was entered unless separately translated. |


Translation coverage can vary by app and version. Product labels may be translated while custom fields, user-entered text, print-format content, or a newly released message remains in the source language.

## Troubleshooting

### The interface did not change

Save the User or System Settings record, then sign out and sign in again. Confirm the User record has the expected language and that the translation exists.

### Some labels remain in English

The app, custom field, or new message may not have a translation. Verify the source text and contribute or maintain the translation rather than changing unrelated settings.

### Printed documents use the wrong language

Print Format text, letterheads, Item descriptions, and transaction content may need separate translated templates or records.

## Frequently asked questions

### Can every user choose a different language?

A User record can carry a personal language where the user has permission and translations are available.

### Does changing language translate existing Customer or Item names?

The setting translates supported interface text. It does not rewrite business data entered by users.

### Which language is used when a translation is missing?

ERPNext falls back to the available source text, commonly English.

### Does language change date and number formats?

Language can influence presentation, but System Settings and Currency formatting also matter. Verify both when localisation looks inconsistent.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Adding Users](/erpnext/adding-users)
- [Translations](/erpnext/translations)
- [Country](/erpnext/country)
- [Global Defaults](/erpnext/global-defaults)
- [Print Format](/erpnext/print-format)
