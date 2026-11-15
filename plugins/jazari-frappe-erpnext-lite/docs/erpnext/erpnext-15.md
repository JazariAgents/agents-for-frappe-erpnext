<!-- Frappe documentation: erpnext, part 15 of 18. Index: docs/INDEX.md -->

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

![ERPNext CRM and sales cycle from Lead through Payment, including the direct Sales Order to Sales Invoice path](/files/order-to-cash-selling-module-v2.svg)

The diagram above is the main ERPNext sales cycle. It provides a common reference for this page and for the detailed documentation of Quotation, Sales Order, Delivery Note, Sales Invoice, and Payment Entry.

ERPNext supports four common variations of this cycle:

- **Standard goods sale:** confirm an order, dispatch stocked goods, invoice the customer, and record payment.
- **Direct invoice with stock update:** use one Sales Invoice to dispatch and bill an immediate stock sale.
- **Service sale without stock delivery:** confirm and bill non-stock work without a Delivery Note.
- **Drop-shipped sale:** ask a Supplier to deliver directly to the Customer while you record the sale and purchase.

Choose the shortest variation that still gives your team the control and audit trail it needs. A [Quotation](/erpnext/quotation) proposes terms. A [Sales Order](/erpnext/sales-order) records the commitment. Delivery, invoice, and payment documents record the operational and financial result.

### Standard goods sale

![Standard goods sale from Quotation through Sales Order, Delivery Note, Sales Invoice, and Payment Entry](/files/standard-goods-sale.svg)

**Best for:** distributors, wholesalers, manufacturers, and businesses that pick and dispatch stocked goods.

The Sales Order confirms what the customer bought. The Delivery Note records goods leaving the Warehouse. The Sales Invoice bills the customer, and the Payment Entry records payment.

- **Set up:** stock Items, Warehouses, prices, taxes, accounts, and payment terms. Use [Selling Settings](/erpnext/selling-settings) to decide whether Sales Order and Delivery Note are mandatory.
- **Optional:** Quotation can be skipped when the order is already confirmed.
- **Benefit:** clear order, delivery, billing, and payment tracking, including partial fulfilment.
- **Tradeoff:** more documents and approvals than a direct sale.

Sales Order is the commitment. Delivery Note updates stock. Sales Invoice and Payment Entry affect the general ledger. If a Delivery Note or Sales Invoice is created directly, it will not update the Sales Order’s delivered or billed percentage unless it is linked correctly.

### Direct invoice with stock update

![Direct stock sale using a Sales Invoice with Update Stock followed by Payment Entry](/files/direct-invoice-stock.svg)

**Best for:** retail counters, small showrooms, spare-parts desks, and simple cash-and-carry sales where goods are handed over immediately.

Create a [Sales Invoice](/erpnext/sales-invoice) and enable **Update Stock**. The same document reduces stock and bills the customer.

- **Set up:** stock Items, a source Warehouse, prices, taxes, stock and income accounts, and permission in [Selling Settings](/erpnext/selling-settings) to invoice without a Sales Order or Delivery Note.
- **Optional:** Quotation, Sales Order, and Delivery Note are normally skipped.
- **Benefit:** the fastest stock-sale workflow, with one document for delivery and billing.
- **Tradeoff:** no order commitment, reservation, pending-delivery queue, or fulfilment percentage.

The submitted invoice affects both the stock ledger and general ledger. Because it is created directly, users must verify the Warehouse, available stock, rates, taxes, address, and payment terms on the invoice itself. See [Sales Invoice](/erpnext/sales-invoice) for the complete invoicing workflow.

### Service sale without stock delivery

![Service sale from optional Quotation through Sales Order, Sales Invoice, and Payment Entry without a Delivery Note](/files/service-sale.svg)

**Best for:** consulting firms, agencies, software companies, maintenance providers, training businesses, and project-based teams.

Use non-stock service Items. The Sales Order records the agreed scope and value, and the Sales Invoice bills the customer without a stock delivery.

- **Set up:** disable **Maintain Stock** on service Items, configure income and receivable accounts, and add Projects or Timesheets when work is tracked by milestone or time. Use **Skip Delivery Note** when the Sales Order should complete through billing.
- **Optional:** Quotation and Sales Order can be skipped for simple recurring or immediately billable work. Delivery Note is normally not required.
- **Benefit:** tracks scope, milestones, and partial billing without unnecessary Warehouse transactions.
- **Tradeoff:** a direct invoice gives less visibility into committed scope and remaining billable quantity.

Sales Order is the commitment. Sales Invoice and Payment Entry affect the general ledger, but no stock-ledger entry is created. If the invoice is created directly, link it to the relevant Project when project reporting matters. See [ERPNext for Service Organizations](/erpnext/erpnext-for-services-organization) and [Maintenance Sales Orders](/erpnext/maintenance-sales-orders).

### Drop-shipped sale

![Drop-shipped sale using Sales Order, supplier Purchase Order, customer Sales Invoice, and supplier Purchase Invoice](/files/drop-shipped-sale.svg)

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



![ERPNext Selling workspace showing the complete Sales Order Trends chart, transactions, masters, settings, and reports](https://novacompanies.m.frappe.cloud/files/selling-workspace-full.png)

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

![Semi-Auto Payment Reconciliation in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-11-payment-reconciliation.png)

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

![Send Email](/files/send-email.gif)  


**Note:** You must have outgoing [Email Accounts](/erpnext/email-account) set up for this.

After you click on send, the email gets added to the email queue. It will be in the Sending status until it is Sent. The status of the email is displayed in the queue, if sending has failed, it can be sent by clicking on Send Now.

![Email Queue](/files/email-queue.png)  


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

![Email Print Options](/files/email-print-options.png)  


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

![Serial no Configure](/files/serial-and-batch-bundle.png)

## How does this work?

You need to create a **Serial and Batch Bundle** and link it to stock transactions whenever you deal with Serial / Batch numbers. Users must create a separate **Serial and Batch Bundle** for each transaction, and they can't link the same **Serial and Batch Bundle** to multiple transactions.

### Auto Creation of Serial and Batch Bundle for Inward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an inward entry, they must ensure that *Serial Number Series* is set for the serial item and that the *Automatically Create New Batch* checkbox is enabled (with *Batch Number Series* set) for the batch item.

#### For Serial No

![Serial no Configure](/files/auto-serial-creation.png)

#### For Batch No

![Batch no Configure](/files/auto-batch-creation.png)

After the configuration, when the user creates a **Purchase Receipt** or a **Stock Entry** with the Type "Material Receipt", the system will automatically create the inward **Serial and Batch Bundle** on submission of the record.

![Auto Serial Batch Bundle Inward](/files/auto-create-serial-batch-for-inward.gif)

### Auto Creation of Serial and Batch Bundle for Outward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an outward entry, they must enable the checkbox *Auto Create Serial and Batch Bundle For Outward* in **Stock Settings**. They can also set *Pick Serial / Batch Based On* to "FIFO / LIFO / Expiry" in **Stock Settings**.

![Auto Serial Batch Bundle Outward Configure](/files/auto-outward-configuration.png)

After the configuration, when the user creates a **Delivery Note** or a **Stock Entry** with the Type "Material Issue", the system will automatically create the outward **Serial and Batch Bundle** on submission of the record.

![Auto Serial Batch Bundle Outward](/files/auto-create-serial-batch-for-outward.gif)

### Manual Creation of Serial and Batch Bundle for Inward Entry

For the **Serial and Batch Bundle**, both **Serial No** and **Batch** records must already exist in the system. With the manual option, the user must first create the **Serial No** / **Batch** records in the system. Users can use the CSV import option to create **Serial No** / **Batch** records. The blank CSV template can be downloaded using the Serial and Batch Selector.

![create-using-csv](/files/create-using-csv.png)

Complete GIF for manual creation of a **Serial and Batch Bundle** for an inward entry is as follows:

![manually-create-serial-no-inward](/files/manually-create-serial-no-inward.gif)

### Manual Creation of Serial and Batch Bundle for Outward Entry

Using the Serial and Batch Selector, the user can pick the Serial / Batch Nos based on the "FIFO / LIFO / Expiry" method.

![serial-batch-selector-outward](/files/serial-batch-selector-outward.png)

Complete GIF for manual creation of a **Serial and Batch Bundle** for an outward entry is as follows:

![manually-create-serial-no-outward](/files/manually-create-serial-no-outtward.gif)

### Serial and Batch Bundle Creation Using CSV for Outward Entry



Now users can create serial and batch bundles for outward entries by importing a CSV file.

![](/files/Screenshot 2026-01-20 at 12.19.18 PM.png)





## History of Serial Numbers

To check the history of serial numbers, see the report "Serial No Ledger".

![](/files/Screenshot 2026-01-20 at 1.15.35 PM.png)

## Serial / Batch Selector

This is used to select Serial Nos / Batches manually. This popup is also used to create serial nos / batches automatically if they do not exist.

![serial-batch-selector](/files/serial-batch-selector.gif)

## Disable Serial / Batch Selector

If users don't want to use the Serial and Batch Selector (popup), they can disable it through **Stock Settings**. To disable it, go to **Stock Settings** > Serial and Batch Item (TAB) > enable *Disable Serial No And Batch Selector*, then save.

![disable-serial-batch-selector](/files/disable-serial-batch-selector.png)

## Old Serial / Batch Fields

Many customers requested that we retain the old serial and batch fields to address UX issues. In response to this demand, we retained the old serial/batch fields. These fields are solely used for entering serial numbers and batches. The system will automatically create the **Serial and Batch Bundle** upon submission of the stock transaction. To enable this feature, users must navigate to **Stock Settings** and enable the *Use Serial / Batch Fields* option (see the image below).

![use-serial-batch-fields-global](/files/use-serial-batch-fields-global.png)

After that, when the user creates a stock transaction (for example, a **Delivery Note**), the system will show the old Serial / Batch fields. For more details, see the GIF below.

![user-old-serial-batch-fieldsd](/files/user-old-serial-batch-fieldsd.gif)

Users can disable the old serial / batch fields at the transaction level too.

![use-serial-batch-for-dn](/files/use-serial-batch-for-dn.gif)

## Update Serial / Batch on Creation of Auto Bundle

If the user wants to automatically update the Serial No / Batch in the Serial / Batch fields when a **Serial and Batch Bundle** is created, go to **Stock Settings** and disable *Do Not Update Serial / Batch on Creation of Auto Bundle*.

![update-Serial-Batch-on-creation-of-auto-bundle](/files/update-Serial-Batch-on-creation-of-auto-bundle.png)

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


![](/files/backward-tracebility.png)

## Forward Traceability 

To find out where the batch has been used or to whom it was delivered, use the Forward Traceability filter.


![](/files/forward-tracebility.png)

## Backward and Forward (Both) Traceability 


![](/files/both-tracebility.png)

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

![Serial Nos Entry](/files/serial-naming-1.png)

Generated Serial numbers will be updated for each item.

![Serial Nos Created](/files/serial-naming-2.png)

###2. Serializing Manufacturing Item

To Serialize Manufacturing Item, you can define Series for Serial No. Generation in the Item master itself. Following that series, system will create Serial Nos. for Item when its Production entry is made.

####2.1 Serial No. Series

When Item is set as serialized, it will allow you to mentioned Series for it.

![Serial Nos Created](/files/serial-naming-3.png)

####2.2 Production Entry for Serialized Item

On submission of production entry for manufacturing item, system will automatically generate Serial Nos. following Series as specified in the Item master.

![Serial Nos Created](/files/serial-naming-4.png)

<!-- page: erpnext/erpnext__serial-no.md -->
---
title: "Serial Number"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-no"
updated: "2026-03-06"
---

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.



To enable serial / batch feature for the item, first check the 'Enable Serial and Batch No for Item' checkbox in the 'Stock Settings'.

![](/files/Screenshot 2026-03-06 at 11.52.18 AM.png)



As discussed in the [Item](/erpnext/item) page, if an **Item** is *serialized*, a **Serial Number** (Serial No) record is maintained for each quantity of that **Item**. This information helps track the location of the Serial No, its warranty and end-of-life (expiry) information.

You can also track from which **Supplier** you purchased the **Serial No** and to which **Customer** you have sold it. The **Serial No** status will tell you its current inventory status.

If your Item is *serialized* you will have to enter the Serial Nos in the related column with each Serial No in a new line. You can maintain single units of serialized items using Serial Number.

To access the Serial Number list, go to: > Home > Stock > Serial No and Batch > Serial No

1. Prerequisites

---

Before creating and using a Serial Number, it is advised that you create the following first:

- [Item](/erpnext/item)
- Enable 'Has Serial No' in the Item master ![Serial No Enabled](/files/serial-no-enabled.png)

2. How to create a Serial Number

---

Usually, Serial Numbers are auto-created when transactions are made against a serialized Item. This works only when 'Has Serial No' is enabled and a series is set in the Item master.

For example, a series was set for the following Item as 'PB2L.#####'. Then a Stock Entry was submitted to receive the Item. The Serial Numbers were created accordingly.

![Serial No Created](/files/serial-no-created.png)



However, if you want to create a Serial No *manually* follow these steps:

1. Go to the Serial Number list, click on New.
2. Enter a Serial Number.
3. Enter the Item Code and details will be fetched.
4. If any transaction is done with an item, Serial No cannot be set or unset.
5. Save.

Inventory of an Item can only be affected if the Serial No is transacted via a Stock transaction (Stock Entry, Purchase Receipt, Delivery Note, Sales Invoice). When a new Serial No is created directly, its Warehouse cannot be set.

![Serial Number](/files/serial-no.png)



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

 ![Service Level Agreement](/files/sla-setting.png)

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

 ![Service Level](/files/priorities.png)
1. Default Priority: Default Priority selected in Priorities table that will be applied in the Service Level Agreement.
1. Support Hours: Contains the Days of the week on which Support is provided. Has a Start Time and End Time of the Working day.

 ![SLA Support Hours](/files/sla-support-hours.png)
1. Save.

 ![SLA](/files/sla.png)

## 3. Features
### 3.1 Applies to New Issues

Once an SLA is saved, it'll be applied to Issues raised by Customers/Territories as per the option you chose in 'Entity Type'.

![SLA in Issue](/files/sla-entity-type.png)

### 3.2 Resetting an SLA
An SLA can also be reset until the time does not fail. For example, if the SLA is 3 days, you can reset the SLA only within 3 days of the Issue being created. After that, the Service Level will display failed.

![SLA Issue](/files/reset-sla.gif)

### 3.3 Time respond / resolve in Issues
The time to respond to an Issue and the time to resolve will be shown:
 ![SLA in Issue](/files/sla-in-issue.png)

These times are based on the timelines set in the 'Priority' field in the Service Level's Priorities table.


### 3.4 Pause SLA on Statuses
From version 13 onwards, ERPNext allows you to pause SLA on issues when you are waiting for an event to happen. You can do this by selecting a status that is configured in this "Pause SLA On" table.

* Set the statuses on which you want to pause SLA in the SLA document. You can also add custom statuses here.
 ![Service Level](/files/pause-sla.png)
* When the status is changed to any of the above, resolution and response fields are unset and the dashboard indicators change to:
 ![Service Level](/files/hold-indicator.png)
* When the status of the issue changes back to a non-hold status (which is not configured in the "Pause SLA On" table), the **Total Hold time** field will be set in your Issue document.
 ![Service Level](/files/total-hold-time.png)
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

![Company configured as an available ERPNext Session Default](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-session-default-settings.png)


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

![Default Language in ERPNext System Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-system-localisation.png)

## Set a language for one user

Open the User record, select the preferred **Language**, save, then ask the user to sign out and sign in again. Nova assigns Spanish to Sofia without changing the default for the finance and warehouse teams.

![Language field on an ERPNext User record](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-user-language.png)


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

<!-- page: erpnext/erpnext__set-precision.md -->
---
title: "Set Precision | ERPNext Documentation"
description: "Configure ERPNext float and currency precision globally or for a specific field, with examples showing the effect on transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set-precision"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. It buys 1,250 metres of cable at USD 1.2375 per metre. If the purchase rate is displayed with only two decimal places, employees see USD 1.24 and may assume the amount was entered incorrectly. If the company increases precision everywhere without a reason, reports become harder to read and users may mistake display detail for accounting accuracy.



Precision controls how many decimal places ERPNext calculates or displays for Float, Currency, and Percent values. Nova uses a sensible site-wide precision for most records and applies a field-specific override only when a real measurement or pricing process needs more detail. Precision is related to rounding, but it is not the same decision as the rounding method.

## Set site-wide precision

Open **System Settings** and review **Float Precision** and **Currency Precision**. Float Precision affects values such as quantity or conversion factor. Currency Precision affects monetary values such as rate and amount.

![Float and Currency Precision in ERPNext System Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-precision-settings.png)


| Setting                | Example                      | Result                                                                                                |
| ---------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| Float Precision = 3    | Quantity 1.275               | ERPNext displays three decimal places where the field follows the global precision.                   |
| Currency Precision = 2 | USD 699.50                   | Common cent-based amounts display two decimal places.                                                 |
| Currency Precision = 4 | Rate USD 1.2375              | Useful when Nova buys a high-volume component priced below one cent increments.                       |
| Rounding Method        | Midpoint value such as 2.345 | Determines how a value is rounded when precision is applied. Review it separately in System Settings. |


## Override one field with Customize Form

Use **Customize Form** only when one field genuinely needs different precision. Select the DocType and field, set its Precision property, save, and reload. For example, Nova can show four decimal places on an Item rate while keeping ordinary financial totals at two decimals.

## Verify the result downstream

Create a draft Purchase Invoice or Purchase Order with quantity 1,250 and rate 1.2375. Confirm the entered rate, calculated amount, taxes, rounded total, print format, and General Ledger result follow the intended policy. Display precision alone is not proof that the stored and posted value is correct.

## Troubleshooting

### A field still shows fewer decimals

The field may have its own Precision property or be formatted by a Currency. Reload metadata and inspect the field through Customize Form.

### The total differs from a manual calculation

Compare quantity, conversion factor, rate, tax precision, smallest currency fraction, rounded total, and rounding method. Do not fix a policy mismatch by adding arbitrary decimals.

### Reports and forms display different precision

Reports may apply their own column precision or Currency formatting. Verify the report definition and linked Currency.

## Frequently asked questions

### Does higher precision make accounting more accurate?

More displayed decimals help only when the source measurement or price is genuinely that precise. False precision can make reports harder to interpret.

### Can quantity and currency use different precision?

Float Precision and Currency Precision are separate controls, and individual fields can have overrides.

### Does changing precision rewrite old transactions?

It can change how values are displayed, but it should not be assumed to recompute or correct submitted accounting entries. Test reports and documents before rollout.

### When should a field-specific override be used?

Use it when one operational value, such as a commodity rate or measurement, requires more detail than the rest of the site.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Customize Form](/erpnext/customize-form)
- [Currency](/erpnext/currency)
- [Global Defaults](/erpnext/global-defaults)
- [Invoice Rounding Issue](/erpnext/invoice-rounding-issue)
- [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__set_up_e_commerce.md -->
---
title: "Set Up E-commerce"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set_up_e_commerce"
updated: "2026-03-02"
---

**If you're using version 15 or migrating to version 15, you need to install the frappe's** [**Webshop**](https://github.com/frappe/webshop) **app first in order to use the E-commerce features**

In addition to tracking Items, ERPNext also has the provision to set up an attractive E-commerce shop to sell them. You can seamlessly publish items onto your web store and configure what to show in clicks. You can also choose to enable/disable features such as Wishlist, Customer Reviews, etc.

Assuming you have some [Items](/erpnext/item) setup in ERPNext, you can follow the steps below to set up your store:

1. [Explore and Configure E Commerce Settings (In v15 E Commerce Settings has renamed to Webshop Settings)](/erpnext/e_commerce_settings)
2. [Publish and Update an Item](/erpnext/website_item)
3. [Explore the Product Listing](/erpnext/product-listing)
4. [Explore Item group wise product listing](/erpnext/item_group_wise_product_listing)
5. [Shopping Cart](/erpnext/shopping-cart)
6. [The Shop by Category page](/erpnext/shop_by_category)
7. [Wishlist](/erpnext/wishlist)
8. [Reviews and Ratings](/erpnext/reviews_and_rating)
9. [Search](/erpnext/e_commerce_search)

<!-- page: erpnext/erpnext__setting-company-sales-goal.md -->
---
title: "Calculate Incentive for Sales Team | ERPNext Documentation"
description: "Calculate Sales Person contribution and incentives in ERPNext using commission rates and the Sales Team table on sales transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-company-sales-goal"
updated: "2026-07-24"
---


**Defining and achieving sales goals/targets can help your company reach new goals and increase revenue.**

1. Monthly sales targets can be set for a Company via the Company master under the Sales Settings section. By default, the Company master dashboard displays month-wise past sales stats.

 ![Sales Graph](/files/sales_history_graph.png)

1. You can set the **Sales Target** field to track progress against the graph:

 ![Setting Sales Goal](/files/setting_sales_goal.gif)

1. The target progress is also shown in notifications:

 ![Sales Notification](/files/sales_goal_notification.png)

### Related Topics
1. [Company Setup](/erpnext/company-setup)
1. [Sales Order](/erpnext/sales-order)
1. [Sales Partner](/erpnext/sales-partner)

<!-- page: erpnext/erpnext__setting-default-values-for-any-field-in-erpnext.md -->
---
title: "Set default values for any field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-default-values-for-any-field-in-erpnext"
updated: "2026-03-04"
---

 

Using **Customize Form**, we can set a _default_ value for any field of any Doctype in ERPNext.

 

**Steps:**

1\. Open Customize Form using awesome search bar or via Menu options of any DocType. This will open a screen where you can view all the fields that comprise in this DocType.

 

![](/files/6T6CWP6.png)

 

 

2\. Expand the field for which you want to store a default value and enter it under Display -> Default

 

![](/files/TjzsYhu.png)

 

![](/files/th62UXt.png)

 

 

Check out the below GIF where we have set _default_ value as **Stores - ETL** for field "Default Source Warehouse" in DocType Stock Entry:

 

![](/files/wXMccxf.gif)

 

 

To learn more about customisations in ERPNext, check out this [link](https://erpnext.com/docs/user/manual/en/customize-erpnext/customize-form)

<!-- page: erpnext/erpnext__setting-up-buy-1-get-1-free-pricing-rule.md -->
---
title: "Set Up Buy One Get One Free Offers | ERPNext Documentation"
description: "Create and test an ERPNext Product Discount Pricing Rule for buy-one-get-one-free and other free-item promotions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-buy-1-get-1-free-pricing-rule"
updated: "2026-07-25"
---

Use a Product Discount [Pricing Rule](/erpnext/pricing-rule) to add a free item when a transaction meets a purchase condition. The free item can be the same Item or a different promotional Item.

## Before you begin

Create or confirm:

- The qualifying and free [Items](/erpnext/item).
- Selling [Item Prices](/erpnext/item-price).
- Sufficient stock for the free Item when it maintains stock.
- The eligible Customer, Customer Group, Territory, or campaign when the offer is restricted.

Test the rule on a demo transaction before enabling it for users. Product Discount rules can re-add a free row when users remove it while the qualifying condition still applies.

## Create a Buy 1 Get 1 Free rule

1. Open the Pricing Rule list and select **Add Pricing Rule**.
2. Enter a clear title, such as **Buy AeroBook Sleeve, Get One Free**.
3. Set **Apply On** to Item Code and add the qualifying Item.
4. Set **Price or Product Discount** to **Product Discount**.
5. Set the minimum quantity to 1.
6. In the Product Discount section:
  - Enable **Same Item** when the purchased Item is also free.
  - Otherwise select the free Item.
  - Set Free Qty to 1.
7. Configure the Selling or Buying applicability, party conditions, dates, and priority.
8. Save and enable the rule.

![A Product Discount Pricing Rule configured for Buy 1 Get 1 Free.](https://novacompanies.m.frappe.cloud/files/bogo-pricing-rule.png)

## Test the offer

1. Create a new [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).
2. Select an eligible Customer and add the qualifying Item.
3. Enter the minimum qualifying quantity.
4. Save or select **Apply Pricing Rule** when required by the form.
5. Confirm that ERPNext adds the free row with a zero rate.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

Use the highlighted pencil icon to open the full child-row editor when you need to verify fields that are not shown in the grid.

## Same-item and different-item offers


| Offer                               | Configuration                                                      |
| ----------------------------------- | ------------------------------------------------------------------ |
| Buy one, get the same Item free     | Enable Same Item and set Free Qty                                  |
| Buy one Item, get another Item free | Leave Same Item disabled and select the free Item                  |
| Buy several units, get one free     | Set the qualifying minimum quantity and Free Qty                   |
| Apply the offer to an Item Group    | Apply the condition to the Item Group and test every eligible Item |


## Stock and fulfilment

A zero-rate promotional Item can still require stock. Verify availability before launching the offer and include the free row in downstream [Delivery Notes](/erpnext/delivery-note) and stock updates.

If insufficient stock prevents submission, replenish or change the offer. Do not delete the free row and assume the Pricing Rule is satisfied, because ERPNext can fetch it again.

## Rule priority and overlap

Review other Pricing Rules, [Promotional Schemes](/erpnext/promotional-scheme), and [Coupon Codes](/erpnext/coupon-code) that could match the transaction. Use clear validity periods and priorities, then test whether offers should combine or remain exclusive.

## Troubleshooting


| Problem                               | What to check                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| The free row is not added             | Confirm the rule is enabled and all item, party, quantity, date, and transaction conditions match |
| The free row returns after deletion   | The qualifying condition still applies; change the transaction or disable the rule                |
| Submission reports insufficient stock | Check stock for the free Item and selected Warehouse                                              |
| More than one promotion applies       | Review overlapping rules and priorities                                                           |
| The wrong Item is free                | Review Same Item and the selected free Item                                                       |


## Frequently asked questions

### Can the free Item differ from the purchased Item?

Yes. Leave Same Item disabled and select the promotional Item.

### Can I set Buy 2 Get 1 Free?

Yes. Set the minimum qualifying quantity to 2 and Free Qty to 1.

### Does the free Item appear on delivery documents?

Yes, when the mapped document includes the promotional row.

### Can the free Item have a non-zero rate?

A Product Discount free row is intended to carry a zero promotional rate. Use a Price Discount rule for a reduced, non-zero rate.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Applying a Discount](/erpnext/applying-discount)
- [Sales Order](/erpnext/sales-order)
- [Delivery Note](/erpnext/delivery-note)

<!-- page: erpnext/erpnext__setting-up-email-signature-in-erpnext.md -->
---
title: "Setting Up Email Signature in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-email-signature-in-erpnext"
updated: "2026-03-04"
---

To add your signature, go to your User Profile under **Settings > My Settings**  

![](/files/PIoVfY1.png)

Scroll down to the **Email Settings** section where you can add your signature in HTML:  

![](/files/4swM1Yz.png)

<!-- page: erpnext/erpnext__setting-up-sendgrid-smtp-email-in-erpnext.md -->
---
title: "Setting up Sendgrid SMTP Email in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-sendgrid-smtp-email-in-erpnext"
updated: "2026-03-06"
---

SMTP, or simple mail transfer protocol, is a quick and easy way to send email from one server to another. SendGrid provides an SMTP service that allows you to deliver your email via our server instead of your client or server. ERPNext comes built-in with a configured email client so that you can send and receive emails in ERPNext and append them to documents if required.

**Integrating SendGrid's Web API**

SendGrid’s SMTP API allows developers to specify custom handling instructions for e-mail using an X-SMTPAPI header inserted into the message.

**Step 1:** You need to create an API key to authenticate your application. In this case, *ERPNext*. Learn more about integrating SendGrid with SMTP [here](https://sendgrid.com/docs/API_Reference/SMTP_API/integrating_with_the_smtp_api.html)

Click on SMTP Relay![Screenshot 2024-06-01 at 12.44.17 PM](/files/Screenshot 2024-06-01 at 12.44.17 PM.png)  


Generate an API Key![Screenshot 2024-06-01 at 12.44.33 PM](/files/Screenshot 2024-06-01 at 12.44.33 PM.png)  
  
**Step 2:** Once your *API key* has been created, you need to configure it in your ERPNext account &gt; Create a **New** **Email Account.**

  


**Email Address:** *Your Email Address*

**Service:** Select "*SendGrid*"

Check "Use Different Email ID"

**Alternative email ID:** apikey

**Password:** *&lt;API Key Generated in step 1&gt;*

Outgoing server: &lt;server name generated in step 1&gt;

Port: &lt;port number generated above&gt;

![Screenshot 2024-06-01 at 12.44.45 PM](/files/Screenshot 2024-06-01 at 12.44.45 PM.png)  


For SSL connections, uncheck the "use TLS" option![Screenshot 2024-06-01 at 12.45.14 PM](/files/Screenshot 2024-06-01 at 12.45.14 PM.png)  


Now **save** this information and you have successfully configured the SendGrid SMTP Email in ERPNext.

  
  


Power to you!

  
  


  
  


-----

**﻿**

<!-- page: erpnext/erpnext__setting-up-taxes.md -->
---
title: "Setting Up Taxes | ERPNext Documentation"
description: "Configure tax accounts, sales and purchase tax templates, Tax Categories, Tax Rules, and item-specific rates in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-taxes"
updated: "2026-08-14"
---

Tax setup connects a legal calculation to the ordinary sales and purchase workflow. The goal is not merely to add a percentage to an invoice, but to calculate the right charge, post it to the right account, and retain enough detail for reporting and compliance.



Nova Industries may sell the same electronics to retail customers, resellers, and customers in another region. The applicable tax can depend on the Item, party, address, transaction type, and jurisdiction. Reusable templates and rules allow ERPNext to choose consistently instead of asking users to rebuild the calculation on every invoice.



This page provides the setup sequence and explains how accounts, templates, Item Tax Templates, Tax Categories, and Tax Rules work together. Confirm the exact rates and legal treatment with a qualified local adviser.

## Before you begin

Confirm the tax registration, rates, place-of-supply rules, recoverability, and reporting requirements with a qualified adviser. Create the required tax ledgers in the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).

## Create sales and purchase tax templates

Open **Sales Taxes and Charges Template** or **Purchase Taxes and Charges Template**.

1. Select the company.
2. Add a row for each tax or charge.
3. Choose the calculation type.
4. Select the tax ledger.
5. Enter the rate and description.
6. Mark a template as default only when it applies to most transactions.
7. Save.

![Sales tax template](/files/sales-tax-template.webp)

Review whether purchase tax should be added to valuation, treated as recoverable input tax, or posted as an expense.

## Use Tax Categories

A Tax Category identifies a tax treatment, such as domestic standard, export, or exempt.

![Tax Category](/files/tax-category.webp)

Assign the category to parties or transactions. Then use a [Tax Rule](https://docs.frappe.io/erpnext/tax-rule) to choose the correct template based on company, Customer, Supplier, item, territory, billing or shipping location, and validity dates.

## Configure item-specific tax rates

Use an [Item Tax Template](https://docs.frappe.io/erpnext/item-tax-template) when particular Items have a different rate or exemption. Link the template on the Item or transaction row.

## Test the configuration

Create representative draft Sales Invoices and Purchase Invoices for each tax treatment. Check the taxable value, each tax row, grand total, General Ledger preview, and printed tax information. Include discounts, returns, and foreign-currency cases in testing when they apply.

## Withholding and localization

Withholding tax uses separate [Tax Withholding Category](https://docs.frappe.io/erpnext/tax-withholding-category) configuration. Country-specific apps may add tax identifiers, reports, e-invoicing, and statutory validations. Follow the localization documentation when it overrides generic setup.

## Troubleshooting

**The wrong tax template is selected**

Check the Tax Category, Tax Rule priority and validity, party and address data, company, and transaction date.

**Tax is missing for one Item**

Review its Item Tax Template and the tax account mapping in the transaction template.

**Tax is calculated on the wrong value**

Check the row calculation type and whether the charge is based on Net Total, Previous Row Total, Previous Row Amount, or Actual.

## Related topics

- [Tax Rule](https://docs.frappe.io/erpnext/tax-rule)
- [Item Tax Template](https://docs.frappe.io/erpnext/item-tax-template)
- [Sales Taxes and Charges Template](https://docs.frappe.io/erpnext/sales-taxes-and-charges-template)
- [Tax Withholding Category](https://docs.frappe.io/erpnext/tax-withholding-category)

<!-- page: erpnext/erpnext__setting-up.md -->
---
title: "Setting Up\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up"
updated: "2026-08-14"
---

Setting up ERPNext means turning the way your business already works into reliable masters, defaults, permissions, and opening balances. A good setup begins with the decisions that affect every transaction, then moves into the individual modules your team will use.



For Nova Industries, an electronics manufacturer and distributor, this starts with the legal company, fiscal year, chart of accounts, warehouses, items, customers, suppliers, users, and opening balances. Configure these foundations before importing day-to-day transactions.

![ERPNext Desk showing the installed applications available after sign-in](https://novacompanies.m.frappe.cloud/files/setup-20260814-setting-up-desk.png)



## Plan the setup


| Decision          | Why it matters                                                           | Start here                                      |
| ----------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| Legal entities    | Separates books, tax registrations, currencies, and statutory reporting. | [Company](/erpnext/company-setup)               |
| Accounting period | Controls transaction dates and financial reporting.                      | [Fiscal Year](/erpnext/fiscal-year)             |
| Accounts          | Determines where every financial transaction is posted.                  | [Chart of Accounts](/erpnext/chart-of-accounts) |
| Stock locations   | Defines where inventory is stored and valued.                            | [Warehouse](/erpnext/warehouse)                 |
| Access            | Limits what each user can view and change.                               | [Users and Permissions](/erpnext/adding-users)  |


## Recommended setup order

1. Create or review the [Company](/erpnext/company-setup), Country, currency, time zone, language, and fiscal year.
2. Review [System Settings](/erpnext/system-settings), [Global Defaults](/erpnext/global-defaults), and Domain Settings.
3. Configure the [Chart of Accounts](/erpnext/chart-of-accounts), cost centers, taxes, bank accounts, warehouses, and naming rules.
4. Create essential masters such as [Items](/erpnext/item), [Customers](/erpnext/customer), and [Suppliers](/erpnext/supplier).
5. Add users, roles, and user permissions. Test the setup with the same access your team will use.
6. Prepare clean legacy data and use the [Data Import](/erpnext/data-import) tools for required masters and opening balances.
7. Run a complete sales, purchase, stock, and accounting cycle before going live.

## Do not import everything

Move only the data needed to operate and report from the cutover date. Keep the old system available for historical reporting instead of importing years of low-value transactions. This reduces reconciliation effort and makes problems easier to find.

## Validate before go-live

Confirm opening receivables, payables, bank balances, stock quantities, stock values, fixed assets, taxes, and the trial balance. Ask real users to complete their most common tasks. Correct the setup before the first live transaction, because changing currencies, account structures, or stock rules later can be disruptive.

## Troubleshooting

### A module is missing

Review Domain Settings and Show or Hide Modules. Also confirm that the user has the roles required to access the workspace.

### Defaults are not appearing

Check Company defaults, Global Defaults, user defaults, and the relevant module settings. Reload the session after changing system-wide defaults.

## Frequently asked questions

### Should I set up every module before going live?

Configure the modules needed for the first operational scope, test them thoroughly, and introduce additional modules in controlled phases.

### Can I change the setup later?

Many defaults can be changed, but decisions such as company currency, account structure, stock accounting, and opening balances require careful planning after transactions exist.

## Related topics

- [Company](/erpnext/company-setup)
- [System Settings](/erpnext/system-settings)
- [Data Import](/erpnext/data-import)
- [Adding Users](/erpnext/adding-users)
- [Opening Balances](/erpnext/opening-balance)

<!-- page: erpnext/erpnext__setting-workflows-on-masters.md -->
---
title: "Setting Workflows on Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-workflows-on-masters"
updated: "2026-03-04"
---

Workflows are usually set on submittable documents. Once the document is approved, it gets automatically submitted as per the workflow set. However, sometimes, businesses do have use cases where there is a need for approval of masters such as Items, Item Price, Pricing Rule, etc.

  


In ERPNext, these masters are non-submittable. Hence, even on rejection, sometimes, they are still active and you can use them in transactions. In this article, we have taken the example of the Item master. We will set a simple workflow on Item and make it active only when it has been approved. To do so, follow the below steps:

  


1) Make sure the master on which you are going to set the workflow has an Enable/Disable checkbox. If this is not present by default, you need to create one via Customize Form and set the default value as follows:

1. 0 if checkbox is "Disable"
2. 1 if checkbox is "Enable"

In our case, the Item master has a checkbox called "Disabled". We have set the default value as 1 in the Customize Form of the Item DocType as shown below.

  


![](/files/ubLZfPq.png)

  


This means that every time a new Item is created, it will be disabled by default, unless approved (as seen in the screenshot below). 

  


![](/files/yPOQ2fT.png)

  


  


2) Next, set the Workflow.

  


In the States table, on approval, make sure to update the "Disabled" (or Enabled) checkbox to 0 (or 1 in case of enabled) as shown below.

  


  


![](/files/Qf3QXyo.png)

  


This will ensure that whenever the Item is approved, the Item will automatically be enabled and you will be able to use it in transactions.

  


Check the below GIF to understand the workflow in detail:

  


![](/files/olzpAk2.gif)

<!-- page: erpnext/erpnext__setup-two-factor-authentication.md -->
---
title: "Setup Two Factor Authentication\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setup-two-factor-authentication"
updated: "2026-03-04"
---


##Enable Two Factor Authentication (2FA)

Activate two factor authentication by running the command.

`bench --site [sitename] set-config enable_two_factor_auth true`

Specify the following in System Settings

* The method of OTP validation (OTP App = TOTP using Soft or Hard Token while Email/SMS = HOTP using Email or SMS
* The expiry time for the QR Code on the server if OTP App is specified
* The OTP Issuer Name.

![Enable Two Factor Auth](/files/twofactor-1.png)


On activation of 2FA from setup, it is also activated for the Role "All". In this way, all users including the Administrator have to perform a 2nd level authentication with a token. By unchecking the "Two Factor Authentication" checkbox in the "All" role and enabling it in other roles, the need to login with a token can be limited to specific roles. 2FA does not apply to login by Web Users and API login

![Role Enable Two Factor Auth](/files/twofactor-2.png)

If using SMS authentication, please make sure that your SMS settings are updated

![SMS Settings](/files/twofactor-3.png)

If using Email, make sure that your outgoing Email account settings are updated

![Email Settings](/files/twofactor-4.png)

When the new user tries to log in for the first time in a system that has two-factor authentication enabled and which has the authentication option as OTP App, an email is sent containing a link to the QR Code.

![Email Notify Two Factor](/files/twofactor-5.png)
![QR Code Page](/files/twofactor-6.png)

Scanning the QR Code with an authentication app like Google Authenticator registers the access for the user and automatically starts to generate tokens that can be used to login

![Two Factor Scan App](/files/twofactor_app.jpeg)

If either of Email/SMS is used as the authentication method, you get notifications also

![Email and SMS](/files/twofactor-8.png)



### Frequently asked questions (FAQ)

Q. I am unable to login even after following entire process. 

Ans: Frappe uses TOTP based OTP algorithm, which depends on your device's system time. Please make sure that device you're using has same time set as your ERPNext server. 

<!-- page: erpnext/erpnext__share-reports.md -->
---
title: "Share Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/share-reports"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Elena then transfers 1,000 shares to Horizon. The new balances should be 5,000 for Elena, 4,000 for Marcus, and 2,000 for Horizon. Management wants to verify two things. It needs the ownership position today and the transaction trail that explains how that position changed.



ERPNext separates these questions into two reports. Share Balance is the current snapshot. Share Ledger is the history behind the snapshot. Use both when reviewing ownership, investigating a disagreement, or preparing information for professional review.

## Share Balance

Open **Share Balance** and filter by Company or Shareholder. The report shows the shares currently held by each shareholder and their value. Use it to answer “Who owns what now?”

![Current Nova shareholders used in share reporting](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-shareholder-list.png)

## Share Ledger

Open **Share Ledger** and filter by Company, date range, or Shareholder. The report lists submitted [Share Transfers](/erpnext/share-transfer) such as issues, purchases, and owner-to-owner transfers. Use it to answer “How did this balance arise?”

![Submitted share transfer quantity used in the Share Ledger](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-transfer-result.png)

## Choose the right report


| Question                                     | Report                                                        |
| -------------------------------------------- | ------------------------------------------------------------- |
| How many shares does each owner hold now?    | Share Balance                                                 |
| Which issue or transfer changed the holding? | Share Ledger                                                  |
| What is one owner's current position?        | Share Balance filtered by [Shareholder](/erpnext/shareholder) |
| What happened during a particular period?    | Share Ledger filtered by date                                 |


## Troubleshooting

### A recently created shareholder does not appear

A shareholder with no submitted share issue has no holding to report. Submit an Issue and refresh the report.

### A transfer is missing

Confirm that the Share Transfer is submitted, the Company and date filters include it, and the correct shareholder is selected.

## Frequently asked questions

### Can Share Balance replace the Share Ledger?

Share Balance shows the result but not the sequence of transactions. Keep the Share Ledger when you need an audit trail.

### Do these reports replace statutory shareholder registers?

ERPNext provides operational ownership records. Confirm the statutory format, approvals, and filing requirements with a qualified professional in your jurisdiction.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Shareholder Management](/erpnext/shareholder-management)
- [Share Transfer](/erpnext/share-transfer)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__share-transfer.md -->
---
title: "Share Transfer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/share-transfer"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Elena now wants to transfer 1,000 of her shares to Horizon Ventures LLC. After the transfer, Elena will hold 5,000 shares, Marcus will still hold 4,000, and Horizon will hold 2,000. The company needs more than a note saying the deal happened. It needs an auditable record of the former owner, new owner, share-number range, quantity, rate, and date.



A Share Transfer records three kinds of ownership movement: the Company issues new shares, buys shares back, or transfers existing shares between Shareholders. Use the correct type because it determines which parties ERPNext requires and how balances change.

## Before you begin

Create the relevant [Shareholders](/erpnext/shareholder). A new owner must first receive an Issue before their folio number and balance become available for later transfers. Confirm the equity or liability [Account](/erpnext/chart-of-accounts), asset account, and Share Type with your accountant.

## Issue shares

Create a Share Transfer and set **Transfer Type** to **Issue**. Select the recipient, Equity or Preference share type, and the Company.

![Share issue type, recipient, and share type highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-issue-details.png)

Enter the first and last share numbers, number of shares, and rate. The number range must agree with the quantity and must not overlap an existing issued range.

![Share number range, quantity, and rate highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-issue-quantity.png)

## Transfer shares between owners

Set Transfer Type to **Transfer**. Select the From Shareholder and To Shareholder with their folio numbers.

![From and to shareholders highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-transfer-parties.png)

Enter the share-number range being moved, quantity, and rate, then save and submit. ERPNext reduces the former owner's holding and increases the new owner's holding.

![Transferred share range and quantity highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-transfer-result.png)

## Transfer types


| Type     | Use it when                                              |
| -------- | -------------------------------------------------------- |
| Issue    | The Company creates and assigns shares to a shareholder. |
| Transfer | Existing shares move from one shareholder to another.    |
| Purchase | The Company buys shares back from a shareholder.         |


## Troubleshooting

### The folio number is missing

Submit an Issue for that shareholder first. A saved Shareholder without an issued holding does not yet have an ownership history.

### The share-number range is rejected

Check that the From No, To No, and No of Shares agree and that the range is available to the source owner.

## Frequently asked questions

### Does submission automatically create General Ledger entries?

The ownership register changes on submission. Use **Create Journal Entry** when the transfer also requires an accounting entry, and review the resulting [General Ledger](/erpnext/general-ledger).

### Can I transfer shares to a newly created shareholder immediately?

The recipient needs an initial Issue so ERPNext can assign a folio number before a later transfer.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Shareholder Management](/erpnext/shareholder-management)
- [Share Reports](/erpnext/share-reports)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__shareholder-management.md -->
---
title: "Shareholder Management"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shareholder-management"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. As Nova raises capital and ownership changes, the finance team must answer three questions reliably: who the owners are, how many shares each one holds, and which transaction changed that balance. Shareholder management connects those answers instead of treating them as separate spreadsheets.



In ERPNext, the workflow has three parts. A [Shareholder](/erpnext/shareholder) identifies the owner. A [Share Transfer](/erpnext/share-transfer) records an Issue, Purchase, or Transfer. [Share Reports](/erpnext/share-reports) show the resulting balances and history.

![Nova shareholder register in ERPNext](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-shareholder-list.png)

## Use the records in this order


| Step | Record                                   | Result                                                |
| ---- | ---------------------------------------- | ----------------------------------------------------- |
| 1    | Shareholder                              | Creates the owner master and contact context.         |
| 2    | Share Transfer with Issue                | Creates the first holding and assigns a folio number. |
| 3    | Share Transfer with Transfer or Purchase | Changes ownership or records a company buyback.       |
| 4    | Share Balance and Share Ledger           | Verifies current ownership and transaction history.   |


![Share issue type, shareholder, and share type highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-share-issue-details.png)

## Keep the register reliable

Use submitted Share Transfers for every ownership change. Do not overwrite a shareholder's balance manually. Keep [Contacts](/erpnext/contact) and [Addresses](/erpnext/address) linked to the master, and use a consistent [Fiscal Year](/erpnext/fiscal-year) and posting date when related accounting entries are required.

## Frequently asked questions

### Does creating a Shareholder change the company's equity?

The master itself has no ledger impact. A submitted share issue records the ownership movement, and the related [Journal Entry](/erpnext/journal-entry) is used when accounting entries are required.

### Which report shows the current owner balance?

Share Balance shows current holdings. Share Ledger explains how those holdings changed transaction by transaction.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Share Transfer](/erpnext/share-transfer)
- [Share Reports](/erpnext/share-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)

<!-- page: erpnext/erpnext__shareholder.md -->
---
title: "Shareholder\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shareholder"
updated: "2026-08-14"
---

Nova Electronics Trading has three shareholders. Elena Brooks initially holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Finance needs to know who owns shares, how to contact each owner, and which ownership transactions belong to each one. Keeping names in a spreadsheet makes it easy to lose the connection between the owner, their folio number, and their share history.



A Shareholder is the master record for a person or organisation that owns shares in a Company. It becomes the anchor for [share issues and transfers](/erpnext/share-transfer), balances, and the Share Ledger. Creating the master does not give the owner any shares. Ownership begins only after an Issue is submitted.

## Create a Shareholder

Open the Shareholder list and select **Add Shareholder**. Enter the shareholder's name and Company. Enable **Is Company** when the owner is an organisation rather than an individual.

![Shareholder list with fictional Nova owners](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-shareholder-list.png)

Save the record. ERPNext assigns a Shareholder ID using the configured [naming series](/erpnext/document-naming-settings). Add the shareholder's [Contact](/erpnext/contact) and [Address](/erpnext/address) from the linked records so correspondence remains separate from ownership transactions.

![Shareholder name, company, and folio number highlighted](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-shareholder-details.png)

## Folio number and share balance

The folio number uniquely connects a shareholder to their ownership transactions. It appears after the first share issue. The Share Balance section then shows holdings created by submitted Share Transfers.

## Frequently asked questions

### Why is the share balance empty after I create a Shareholder?

Saving the master records the owner but does not issue shares. Create a Share Transfer with Transfer Type set to Issue and submit it.

### Can a company be a shareholder?

An organisation can be maintained as a shareholder by enabling Is Company on its master record.

## Related topics

- [Shareholder Management](/erpnext/shareholder-management)
- [Share Transfer](/erpnext/share-transfer)
- [Share Reports](/erpnext/share-reports)
- [Company](/erpnext/company)

<!-- page: erpnext/erpnext__sharing.md -->
---
title: "Sharing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sharing"
updated: "2026-02-27"
---

**'Sharing' allows users to share a particular document with other users in ERPNext.**

In addition to user and role permissions, you can also share a document with another user if you have sharing rights for that document. Note that, a shared document will be visible to the other user even if the document is restricted via [User Permissions](/erpnext/user-permissions).

**How to share a document?**
----------------------------

1. Open the document that you want to share and click on the '+'icon under 'Shared With'.
2. Select the user with whom you need to share the document.
3. If the document is to be shared with all users then just select 'Everyone'.
4. Tick appropriate checkboxes to provide relevant rights to the user with whom the document is getting shared.
5. Click on the Add button to get the user added.
6. You can share the same document with multiple users by adding them one by one.

![Screenshot 2023-12-28 at 2.39.05 PM](/files/Screenshot 2023-12-28 at 2.39.05 PM.png)  


**Note:-** The document indicates the users with whom is has been shared.

![Screenshot 2023-12-28 at 2.54.24 PM](/files/Screenshot 2023-12-28 at 2.54.24 PM.png "Screenshot 2023-12-28 at 2.54.24 PM.png")  


### Related Topics

1. [Role and Role Profile](/erpnext/role-and-role-profile)
2. [Role Based Permissions](/erpnext/role-based-permissions)
3. [User Permissions](/erpnext/user-permissions)
4. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__shipment.md -->
---
title: "Shipment\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shipment"
updated: "2026-02-28"
---


**A Shipment is a document that keeps track of real-world Shipments created against a Delivery Note or independently.**

> Introduced in version 13

Shipments are particularly useful for shippers who want to track all their Shipment information such as AWB Number, Shipment Status, Carrier, etc. within ERPNext.

To access the Shipment list, go to:
> Home > Stock > Stock Transactions > Shipment

## 1. Prerequisites
Before creating and using a Shipment, it is advised that you create the following first:

* Company and Customer [Address](/erpnext/address) with Postal Code, Email Address and Phone Number set.
* Customer [Contact](/erpnext/contact).

## 2. How to create a Shipment
A Shipment can be created manually or from a Delivery Note:

### 2.1. Manual Shipment
To create a Shipment manually, follow these steps:

1. Go to the Shipment list, click on New.

 ![Unsaved Shipment](/files/unsaved-shipment.png)
1. Select an option in the **Pickup from** field. On selecting one of the three options, you will be prompted to select a Company/Supplier/Customer based on your selection.
1. If you select 'Company' in the **Pickup from** field, along with the Address you must also select a **Pickup Contact Person** who will be a user from your organization, in ERPNext. Make sure the Last Name, Email Address and Phone Number are set for this user.
1. You can similarly fill the **Delivery To** section.
1. Add Shipment Parcel Information in the **Shipment Parcel** table.
1. Fill in the Value of Goods.
1. Select a Pickup Date.
1. Add a Description of Contents in this Shipment.
1. You can optionally fill the Shipment Information section if you are tracking Shipments manually.
1. Save and Submit.

 ![Submitted Shipment](/files/shipment-submitted.png)

### 2.1. Shipment from Delivery Note
To create a Shipment from a Delivery Note:

1. Click on **Create** > **Shipment** in the Delivery Note.

 ![Submitted Shipment](/files/shipment-from-delivery-note.png)

1. Fill the form as mentioned in the previous section.

## 3. Features

### 3.1. Shipment Parcel

You can specify the length, width, height and, weight of a parcel in the Shipment. If there are multiple parcels with identical dimensions, the **count** field can be set accordingly.

To automatically fetch frequently used parcel dimensions, a Parcel Template can be created and set in the **Parcel Template** field. After adding the template, click on the **Add template** button.

 ![Submitted Shipment](/files/shipment-parcel.png)

### 3.2. Shipment Information / Details
The Shipment Information section is an **optional** section where a user can manually track Shipment information. Here are some of the fields:

1. **Service Provider** (optional): A Service Provider can be a third-party service that provides shipping services from various carriers.
1. **Shipment ID**: The unique Shipment ID on your Shipping platform.
1. **Shipment Amount**: Total cost incurred on Shipment
1. **Carrier**: The Carrier that handles your Shipment and delivers it.
1. **Carrier Service** (optional): The type/category of service provided by the carrier. E.g. some carriers have categories such as Economy, Express, etc.
1. **AWB Number**: An air waybill (AWB) accompanies **international** air cargo. It usually has a unique **AWB Number**, that makes it easy to identify and track an air courier.
1. **Incoterm**: They are a set of internationally recognized rules which define the responsibilities of sellers and buyers. [Know more about it here.](https://iccwbo.org/resources-for-business/incoterms-rules/incoterms-2020/)

### 3.3 Automation

You can also automate rate comparison, label generation, tracking, etc. using our [Shipping Integration](/erpnext/erpnext_shipping).

### 4. Related Topics
1. [Delivery Note](/erpnext/delivery-note)
1. [Packing Slip](/erpnext/packing-slip)

<!-- page: erpnext/erpnext__shipping-rule.md -->
---
title: "Shipping Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shipping-rule"
updated: "2026-02-26"
---

**Using Shipping Rule, you can define the cost for delivering the product to the customer or the supplier. Its a rule to define shipping charges applied to sales transactions**

Most of the companies (mainly retail) have a shipping charge applied based on the invoice total. You can setup Shipping Rule to address the requirement of varying shipping charges based on the Net Total of sales transactions. Use them to offer discounted shipping rates on high-value orders and standard rates on smaller ones.

To set up a Shipping Rule, go to:

`Selling > Setup > Shipping Rule` or `Accounts > Setup > Shipping Rule`

## How to create a Shipping Rule

1. Go to the Shipping Rule list, click on New.
2. Enter the Shipping Rule label, for example, 'Priority Shipping' or 'Next Day Shipping'.
3. When shipping charges are determined by a Shipping Rule, you must also provide the **Shipping Account**, **Cost Center**, and **Shipping Amount**. These details are required to populate the "Taxes and Other Charges" table in the transaction.
4. Under Calculate Based On, you can also change the calculation on which the Shipping Rule will be applied, like net total quantity or net total weight; by default, it is "Fixed".
5. Save

![Shipping Rule](/files/shipping-rule.png)

## Features

### Shipping Rule Conditions

On selecting Net Total or Net Weight, a table will appear where you can set the from and to values for the amount or weight. Enter the Shipping Amount to be calculated for the entered range. Add more conditions as necessary. You can select only one of the three calculation methods in one Shipping Rule.

![Shipping Rule Conditions](/files/shipping-rule-conditions.png)

Referring above, you will notice that shipping charges are reducing as the value increases. This shipping charge will only be applied if the transaction total falls under one of the above ranges.

### Valid for Countries

You can restrict the Shipping Rule to certain countries. Add the countries in the table. By default, the Shipping Rule will be applicable globally. If specific countries are mentioned, then Shipping Charges will be applied only if the Customer's country matches the country mentioned in the Shipping Rule.

![Country Specific Shipping Rules](/files/country-specific-shipping-rules.gif)

### Shipping Rule Application

Following is an example of how shipping charges are auto-applied on a Sales Order based on a Shipping Rule.

![Shipping Rule in Sales Order](/files/shipping-rule-in-sales-order.gif)

<!-- page: erpnext/erpnext__shop_by_category.md -->
---
title: "Shop by Category"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shop_by_category"
updated: "2026-03-02"
---

ERPNext offers a **Shop by Category** (`/shop-by-category`) page out of the box, where users can navigate to relevant products based on their needs without having to use filters right away.

To set up the categories (in the tabs) for this page, head over to:
> E Commerce Settings > Filters and Categories

In the **Filters and Categories** section, make sure **Enable Field Filters (Categories)** is enabled. The categories are pulled from the Website Item Fields table. The field filters such as Item Group, Brand, etc. are reused as categories on this page.

Once this is done, you will accordingly see tabs on the **Shop by Category** page (`/shop-by-category`).
![Shop by Category](/files/shop-by-category.png)

Additionally you can add a slideshow to this page (as seen above) via the **Shop By Category** section in **E Commerce Settings**.

### Fetching records in categories

#### Item Groups
Item Groups are handled a little differently due to its tree structure. Item Group records are fetched if the following conditions are all satisfied:

- The **Show in Website** field is enabled in the Item Group
- Item Group is the **top most group node** (**Is Group** enabled and parent is 'All Item Groups') or **top-most leaf node** (**Is Group** disabled and parent is 'All Item Groups')

Each card links to the respective Item Group page.

#### Other Categories
The other categories' records are simply fetched irrespective. If you want to hide certain records here too (e.g. in **Brand**), you can add a custom **Show in Website** field and it will filter out those records that have this field disabled.

> Custom doctypes **that are linked to Website Item via a link field** can also be included here along with Item Group, Brand, etc.

<!-- page: erpnext/erpnext__shopify_integration.md -->
---
title: "Shopify Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shopify_integration"
updated: "2026-03-02"
---


The Shopify Connector pulls the orders from Shopify and creates Sales Order against them in ERPNext.

While creating the sales order if Customer or Item is missing in ERPNext the system will create new Customer/Item by pulling respective details from Shopify.

### How to Setup Connector?

Shopify Connector is moved out from ERPNext and available through a Frappe App on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)

#### Note to users of old Shopify Connector

If you have not setup Shopify Connector on your ERPNext site you can proceed to next step.

If you are using old Shopify integration that's provided in ERPNext then you will have to disable the connector before proceeding. After installing the app, it will migrate existing data e.g. unique product_id for items to separate doctype. Once you are done configuring new integration, you can confirm the status of migration by going to "Ecommerce Integration Log" doctype.

#### App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
- If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`

The repository for app is hosted on GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/)



#### Create A Custom App in Shopify

1. Click on Apps in menu bar
![Menu Section](/files/app_menu.png)

2. Click on **Develop apps for your store** to create custom app
![new app](/files/develop new app.png)

3. Create New app
 ![](/files/new_app.png)

4. Fill up the details and create app. The each app has its own API key, Password and Shared secret
 ![](/files/configure_admin_scope.png)

5. Allow following permissions to the app.
 - Draft Orders - Read and Write
 - Orders - Read and Write
 - Location - Read
 - Customers - Read
 - Assigned fulfillment orders - Read and Write
 - Products - Read and Write
 - Product listings - Read and Write
 - Inventory - Read and Write

 your final admin scopes should look like this:
 
 ![](/files/final_admin_scopes.png)

6. Install the app on your site
 ![](/files/install.png)

#### Setting Up Shopify on ERPNext:-
Once you have created a Private App on Shopify, setup App Credentials and other details in Shopify Settings in ERPNext.

> To access Shopify Settings, go to:
Awesome search bar > Shopify Setting

1. Fill-up Shopify site URL, Access Token and API Secret from Shopify's Private App.
 ![](/files/tokens.png)
 ![](/files/Screenshot 2022-02-16 at 11.57.34 AM.png)

2. Setup Customer, Company and Inventory configurations.
3. 
![Shopify setting page](/files/main-settings.png)

3. Setup Sync Configurations.
 The system pulls Orders from Shopify and creates Sales Order in ERPNext. You can configure ERPNext system to capture payment and fulfilments against orders.
![Shopify sync config for orders](/files/series-setting.png)


4. Setup Tax Mapper.
 Prepare tax and shipping charges mapper for each tax and shipping charge you apply in Shopify. You can find name of your taxes from your Shopify Admin page.
![Shopify tax mapping](/files/tax-mapping.png)
![Finding Shopify Tax names](/files/shopify-tax-names.png)



After setting up all the configurations, enable the Shopify sync and save the settings. This will register the API's to Shopify and the system will start Order sync between Shopify and ERPNext.


### Syncing Old Orders From Shopify

Once you are done with the Shopify configuration and have enabled Shopify Syncing, you also get a provision to sync your old orders from Shopify into ERPNext. This syncing will happen in background and can take few hours depending on number of orders you have.

1. Enable "Sync Old Shopify Orders"
2. Enter the From and To dates between which the orders need to be synced
![shopify sync old orders](/files/sync-old-orders.png) 

### Inventory Sync

You can update your inventory with Shopify for items that are synced from Shopify. Inventory sync is done every hour with a scheduled job. Inventory levels of items that have changed since last sync are pushed to Shopify. Inventory levels of ERPNext warehouses are mapped 1 to 1 with Shopify locations.

1. To enable inventory sync click on the checkbox, this will show you a table to map ERPNext warehouse with Shopify Location.
2. Select sync frequency. 30 to 60 minutes is recommended frequency.
3. Click on "Fetch Shopify Locations" button to populate Shopify locations in the table.
4. Link each location with ERPNext warehouse.
5. Save the settings.

![Inventory sync with shopify](/files/inventory-sync.png)


> Note: This connector assumes that ERPNext is main source of information about inventory levels, any changes done to Shopify inventory levels will be overwritten by ERPNext if ERPNext inventory levels change.

> Note: Shopify does not support fractional quantity. If fractional quantity is found in ERPNext, the inventory level on Shopify will be set by rounding it down to nearest whole number.


### Item Sync

You can enable sync of new ERPNext items to Shopify by checking "Upload new ERPNext items to Shopify".

You can also update Shopify item upon updating ERPNext item.

Following fields are uploaded / updated:

| ERPNext Field | Shopify Field |
| :-: | :-: |
| Item Name | Title |
| Item Code | SKU |
| Description body | Description |
| Item Group | Product Type |
| Weight per Unit | Weight |
| Weight UOM | Weight UOM |

By default all items are marked as Draft on Shopify and not published in any store.

Purpose of providing this functionality is to sync items with Shopify. It's not possible to map every fields 1-to-1. Upon creation of item on Shopify using this method, it's linked with ERPNext, this eliminates possibility of duplication. You can modify items on Shopify later to add more details.


> Note: This feature is not supported in data import or for variant / template items.


### Cancellation of Orders
This connector handles various cancellation scenario in following manner:

1. If Order on Shopify is cancelled and it doesn't have invoice or Delivery note linked against it then ERPNext Sales Order is cancelled.
2. If ERPNext Sales Order does have any linked document, then status of order on Shopify is added to the respective document. Cancellation and preparation of appropriate documents has to be done by user based on this information.

<!-- page: erpnext/erpnext__shopping-cart.md -->
---
title: "Shopping Cart\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shopping-cart"
updated: "2026-03-02"
---


In addition to listing products, ERPNext also allows selling them via the Shopping Cart.

To enable Shopping Cart, go to:

> E Commerce Settings > [Shopping Cart](/erpnext/e_commerce_settings#shopping-cart)

You can even build a **landing page** for your store at a custom route (eg. /*store*).
[Learn More](/erpnext/store-landing-page).

## 1. Item Types

Shopping Cart works differently for Items with and without variants.

### 1.1 Items without variants

Items without variants have their dedicated product page and an **Add to Cart** button.

![Item without Variants](/files/web-item-striked-price.png)
*Item without Variants*

### 1.2 Items with variants

Since Item Templates can't be bought directly, there is a Configure button to
choose the specific variant and add it to cart.

![Item with Variants](/files/variant-selection.gif)
*Item with Variants*

## 2. Cart Quotation

If checkout is disabled, when your customers add an item to cart, they can click
on the **Request for Quotation** button to get a quote for it. A [Quotation](/erpnext/quotation)
is generated in the system.

## 3. Cart Checkout

You can enable checkout from the [Checkout Settings](/erpnext/e_commerce_settings#checkout-settings) section in **E Commerce Settings**.

![Cart Checkout](/files/cart-with-checkout.png)
*Cart Checkout*

<!-- page: erpnext/erpnext__show-hide-modules.md -->
---
title: "Show or Hide Modules | ERPNext Documentation"
description: "Understand the deprecated ERPNext Show or Hide Modules feature and use current roles, workspaces, domains, and module settings instead."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/show-hide-modules"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. A service coordinator needs Support and Selling, but not Manufacturing. An administrator finds an older instruction that says to open Show or Hide Modules and remove Manufacturing. In current ERPNext versions, that control is deprecated, and hiding a card would not have been a reliable way to protect manufacturing data anyway.



Use the current control that matches the real goal. Domain Settings decides which installed business domains are active for the whole site. Roles and Role Permissions decide which DocTypes a user can access. User Permissions restrict particular records such as a Company or Territory. Workspace configuration controls what appears in navigation. Module Settings changes how a process behaves.

## Current status

The earlier Show or Hide Modules feature is no longer supported or required from version 15 onward. Do not search for the old Show/Hide Cards control or use a legacy screenshot to configure a current develop site.

## Choose the correct replacement


| Goal                                             | Current control                   | Nova example                                                             |
| ------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------------ |
| Remove an irrelevant industry for the whole site | Domain Settings                   | Nova leaves Education inactive because it does not run a school.         |
| Prevent a user from opening a DocType            | Role and Role Permissions Manager | The service coordinator has no Manufacturing transaction permissions.    |
| Restrict records inside an allowed DocType       | User Permissions                  | A sales user can work only with an assigned Company or Territory.        |
| Simplify navigation                              | Workspace visibility and roles    | The service team's workspace shows Support and Selling shortcuts.        |
| Change module behaviour                          | The relevant Module Settings page | Selling Settings controls Sales Order behaviour without changing access. |


## Verify access instead of appearance

Test with the affected user's account or assigned roles. Confirm that an unauthorised DocType cannot be opened through search or a direct route, not merely that its workspace card is absent. A hidden shortcut is a cleaner interface; a denied permission is access control.

![Current ERPNext Workspace list used when reviewing navigation visibility](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-workspace-access-listde3985.png)

## Troubleshooting

### The old Show or Hide Modules option is missing

The feature is deprecated on current versions. Identify whether the requirement concerns domains, permissions, record restrictions, workspace navigation, or module behaviour, then use the matching current control.

### A hidden workspace is still accessible through search

Workspace visibility does not replace DocType permissions. Remove the inappropriate role or permission and test the direct DocType route.

### A user has the right role but sees too many records

Use User Permissions or document-specific permission logic to restrict linked records such as Company or Territory.

## Frequently asked questions

### Can Module Settings hide a module from one user?

Module Settings changes process behaviour. Use roles and Workspace configuration for user-specific access and navigation.

### Does hiding a workspace secure its data?

A hidden workspace removes a navigation surface. Server-side role and record permissions must protect the data.

### Should old sites keep using Show or Hide Modules?

Plan a move to the current controls before upgrading or maintaining the configuration. Verify the exact supported behaviour on the site's version.

### Why keep this documentation page?

It helps readers who find older instructions understand why the control is missing and where to configure the intended outcome now.

## Related topics

- [Domain Settings](/erpnext/domain-settings)
- [Module Settings](/erpnext/module-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [User Permissions](/erpnext/user-permissions)
- [Workspace](/erpnext/workspace)
- [Adding Users](/erpnext/adding-users)

<!-- page: erpnext/erpnext__simplified_ksa_vat_management_and_reporting.md -->
---
title: "KSA VAT Management and Reporting"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting"
updated: "2026-02-26"
---

Generate report for the **VAT on Sales** and **VAT on Purchases**

![image-20210819234431755](/files/image-20210819234431755.png)

Find the new KSA VAT report and KSA vat settings document in the Accounting Workspace

On creation of the first company for the country Saudi Arab. KSA VAT Setting is created automatically. For any new companies create new settings.

KSA VAT Settings is mapping Item Tax Template and Account to the respective title to be shown in the report

![image-20210819233134033](/files/image-20210819233134033.png)

Note: Multiple Item Tax Template can be set for each item. 

A good example in the sales cycle would be an item that is treated as a Standard rated Sales and as well as Zero rated domestic Sales. Same case can be applied on the purchase cycle.

![image-20210819233839064](/files/image-20210819233839064.png)

Use the Item Tax Templates in the Sales and Purchase Invoice. The data should result in a similar KSA VAT Report

![image-20210819235844178](/files/image-20210819235844178.png)

KSA VAT Invoice - Print Format for Sales Invoice

![ksa-vat-invoice-a4-page-1](/files/ksa-vat-invoice-page-112b65a.jpg)
![ksa-vat-invoice-a4-page-2](/files/ksa-vat-invoice-page-291464f.jpg)

<!-- page: erpnext/erpnext__single-payment-multiple-invoices.md -->
---
title: "Single Payment Against Multiple Invoices | ERPNext Documentation"
description: "Allocate one ERPNext payment across several customer or supplier invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/single-payment-multiple-invoices"
updated: "2026-08-01"
---

A single bank receipt or payment can settle several invoices. Keep it as one Payment Entry and use the References table to show exactly how the amount is distributed.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Single Payment Against Multiple Invoices

1. Create the Payment Entry for the correct party.
2. Enter the actual bank amount and reference.
3. Fetch outstanding invoices.
4. Select the invoices included in the remittance and set each allocation.
5. Record any discount, fee, withholding, or exchange difference explicitly.
6. Confirm totals and submit.

![One ERPNext Payment Entry allocated across two Sales Invoices](https://novacompanies.m.frappe.cloud/files/docs-single-payment-multiple-invoices-v2.png)

## Important fields and what they mean


| Field                  | What it controls                                 |
| ---------------------- | ------------------------------------------------ |
| Outstanding Amount     | Balance available to clear on each invoice.      |
| Allocated Amount       | Portion of this payment assigned to the invoice. |
| Total Allocated Amount | Sum across references.                           |
| Unallocated Amount     | Payment balance left for later allocation.       |
| Difference Amount      | Amount that requires an accounting explanation.  |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### Selecting rows does not update the Paid Amount

Enter the actual payment amount, retain the intended invoice references, and set each Allocated Amount. Row selection alone is not a request to recalculate the bank amount.

### The total allocation exceeds the payment

Reduce one or more allocations so the total does not exceed the amount available. Leave unpaid invoice balances outstanding rather than changing their totals.

### One invoice is missing

Check that all references belong to the same party, Company, receivable or payable account, and compatible currency. Confirm submission status and remaining outstanding amount.

## Frequently asked questions

### Can one payment settle both Sales Invoices and credit notes?

Use only reference types supported by the current allocation dialog and confirm the net effect. Reconcile complex credit scenarios carefully and verify the party ledger.

### Can invoices for different customers share one Payment Entry?

A standard Payment Entry has one party. Record separate entries per Customer and reconcile them to a combined bank deposit if necessary.

### Can the payment partially settle every selected invoice?

Enter a partial Allocated Amount for each reference. ERPNext leaves the remaining balances outstanding.

### Which invoice should be allocated first?

Follow remittance advice. Without it, apply the company's documented policy, such as oldest due first, and retain evidence of the decision.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__sms-setting.md -->
---
title: "SMS Settings\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sms-setting"
updated: "2026-03-02"
---


**You can subscribe to an SMS provider to send SMS to mobile numbers.**

To integrate SMS in ERPNext, approach an SMS Gateway Provider who provides HTTP
API. They will create an account for you and will provide a unique username
and password.

To access SMS settings, go to:
> Home > Settings > SMS Settings

To configure SMS Settings in ERPNext, find out their HTTP API (a document
which describes the method of accessing their SMS interface from 3rd party
applications). In this document, you will get a URL which is used to send the
SMS using HTTP request. Using this URL, you can configure SMS Settings in
ERPNext.

Example SMS Gateway URL:

 http://instant.smses.com/web2sms.php?username=<username>&amp;password;=<password>&to;=<mobilenumber>&amp;sender;=<senderid>&amp;message;=<message>


![SMS Setting 2](/files/sms-settings2.jpg)

> Note: For SMS Gateway URL, only include the string before the "?".

Example:

 http://instant.smses.com/web2sms.php?username=abcd&amp;password;=abcd&to;=9900XXXXXX&amp;sender;
 =DEMO&amp;message;=THIS+IS+A+TEST+SMS

The above URL will send SMS from account abcd to mobile number 9900XXXXXX with
sender ID as DEMO with a text message as "THIS IS A TEST SMS".

Note that some parameters in the URL are static. You will get static values
from your SMS Provider like username, password, etc. These static values should
be entered in the Static Parameters table.

![SMS Setting](/files/sms-settings1.png)

## How to configure ERPNext with Voip.ms

The first step is to login to voip.ms account. Then go **Main menu**, **SOAP and REST/JSON API**.
Enable the API, set a password and whitelist your server ip address.

Then go to DIDs and enable SMS on the number SMS will be sent from.

Set SMS Gateway to **https://voip.ms/api/v1/rest.php**

Set Message Parameter to **message**

Receiver Parameter to **dst**

Create 4 new Static Parameters:

- **api_username** (voip.ms account username

- **api_password** (the API password configured few minutes ago)

- **method** set value to **sendSMS**

- **did** (the 10 digits DID that will be used to send the sms)

![Voip.MS Setting](/files/voipms sms settings.jpg)

Then go to SMS Center to test if everything works properly.

### Related Topics
1. [Email Account](/erpnext/email-account)
1. [Notifications](/erpnext/notifications)
</message></senderid></mobilenumber></password></username>

<!-- page: erpnext/erpnext__social-media-settings.md -->
---
title: "Social Media Settings | ERPNext Documentation"
description: "Configure Social Media Settings in ERPNext for supported social publishing integrations."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/social-media-settings"
updated: "2026-07-23"
---

Social Media Settings in ERPNext provides access to the supported social publishing integrations configured for your site. Availability depends on the ERPNext version and the external platform's current API requirements.

## Configure a social integration

1. Open the settings page for the required platform.
2. Enter the application credentials and identifiers issued by that platform.
3. Save the settings and test the connection with a non-sensitive post.
4. Restrict access to users responsible for approved company communication.

Never place social platform secrets in documentation, screenshots, comments, or shared messages. If an integration stops working, verify the external platform's API access, callback URL, permissions, and ERPNext version before replacing credentials.

## Related topics

- [LinkedIn Settings](/erpnext/linkedin-settings)
- [Twitter Settings](/erpnext/twitter-settings)
- [Campaign](/erpnext/campaign)

<!-- page: erpnext/erpnext__south_africa.md -->
---
title: "Requirements for South Africa"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/south_africa"
updated: "2026-02-28"
---

ERPNext aims to support local regulation for different regions in the world. In most cases, ERPNext is very flexible, so you can easily add custom fields and make custom reports to support the regulation of your region.

This section contains region-specific features for South Africa.

- [VAT Audit Report](/erpnext/vat_audit_report)

<!-- page: erpnext/erpnext__stale-cheque-accounting.md -->
---
title: "Stale Cheque Accounting | ERPNext Documentation"
description: "Reverse or replace an expired check while preserving the ERPNext audit trail."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stale-cheque-accounting"
updated: "2026-08-01"
---

A stale check has passed the validity period and is no longer expected to clear. Do not delete the original entry. Reverse or cancel it according to its status, then issue a replacement when required.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Stale Cheque Accounting

1. Confirm with the bank that the check is stale and has not cleared.
2. Locate the original Payment Entry and its ledger impact.
3. Cancel it when ERPNext permits and your control policy allows cancellation.
4. If cancellation is not appropriate, post an authorized reversing Journal Entry with a clear reference.
5. Create a new Payment Entry for the replacement check and reconcile only when it clears.

![Stale Cheque Accounting in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-14-journal-entry-list.png)

## Important fields and what they mean


| Field                  | What it controls                                    |
| ---------------------- | --------------------------------------------------- |
| Cheque or Reference No | Identifies the original instrument.                 |
| Reference Date         | Issue date of the check.                            |
| Posting Date           | Accounting date of the original or reversal entry.  |
| Remarks                | Reason for reversal and replacement reference.      |
| Clearance Date         | Date the bank confirms settlement, when applicable. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The stale cheque belongs to a closed accounting period

Do not cancel or backdate into a locked period without approval. Record the reversal or reclassification in the current permitted period using the workflow approved by your accountant.

### Reissuing the cheque would pay the invoice twice

First reverse or clear the stale cheque's payment effect, verify that the supplier balance is outstanding, and only then issue the replacement.

### The cheque was actually dishonoured, not merely stale

Record the correct event and supporting evidence. A dishonoured cheque can include bank charges and an immediate restoration of the invoice balance, while a stale cheque has expired without clearing.

## Frequently asked questions

### When does a cheque become stale?

The validity period depends on the bank and jurisdiction. Confirm the date with the bank rather than assuming a universal number of months.

### Should the original Payment Entry be deleted?

Keep the audit trail. Use cancellation, reversal, or a current-period adjustment according to the document status and accounting-period controls.

### Can a replacement cheque reuse the same reference number?

Use the new cheque's actual reference and link it to the reversal or stale cheque explanation. Reusing the old number weakens traceability.

### Does marking a cheque stale automatically reopen the invoice?

The invoice is restored only when the accounting effect of the original payment is properly reversed or unallocated. Verify Accounts Payable afterward.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__standard-valuation-rate.md -->
---
title: "Standard Valuation Rate"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/standard-valuation-rate"
updated: "2026-07-01"
---

# Standard Valuation Rate (Standard Costing)

## 1. Overview

The **Standard Valuation Rate** feature lets you value an item's inventory at a single, pre-defined "standard" cost rather than at the constantly-changing rate produced by **FIFO** or **Moving Average**.

With FIFO or Moving Average, the value of your stock moves every time you receive, consume, or revalue material. With **Standard Cost**, the rate is fixed by you (via an **Item Standard Cost** record) and only changes when *you* deliberately publish a new rate. Every receipt, issue, and balance for that item is carried at the standard rate, and the difference between the actual purchase price and the standard rate is posted to a dedicated **Purchase Price Variance** account instead of silently inflating or deflating your inventory value.

This guide explains what the feature does, why you would choose it, how to set it up, how it behaves during transactions and accounting, and the rules you must follow to keep your standard-cost ledger consistent.

---

## 2. Why choose Standard Cost over FIFO / Moving Average?


| Concern                       | FIFO / Moving Average                                           | Standard Cost                                                                                                |
| ----------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Inventory value stability** | Changes with every receipt and revaluation                      | Fixed until you publish a new rate                                                                           |
| **Backdated transactions**    | Trigger a **full revaluation / reposting** of all later entries | **No reposting** — only a fast quantity/value shift                                                          |
| **Reposting performance**     | Slow on items with long, dense ledgers                          | Fast — the rate is known by date, nothing is recalculated                                                    |
| **Cost predictability**       | Cost of goods varies by lot/average                             | Cost of goods is the standard rate, always                                                                   |
| **Variance visibility**       | Price differences are buried in stock value                     | Price differences are isolated in a **Purchase Price Variance** account                                      |
| **Best suited for**           | Trading, where actual landed cost matters per lot               | Manufacturing & high-volume operations that want predictable product cost and frequent backdated corrections |


### The headline benefit: backdated entries do **not** trigger revaluation

This is the single most important reason to adopt Standard Cost.

- With **FIFO / Moving Average**, inserting a transaction *in the past* changes the average/lot consumption of **every later transaction**. The system must **repost** (recompute) the entire forward chain of stock ledger entries. On an item with months of dense history, this is slow and resource-heavy, and it temporarily changes the value of stock that you thought was settled.
- With **Standard Cost**, the value of every stock ledger entry is simply `quantity × standard rate as of that date`. A backdated entry only shifts the running **quantity** of later entries; their **value** is re-derived directly from the (already known) standard rate. There is **no FIFO/average recomputation and no reposting job**. The update is a single, fast quantity-and-value shift, and your inventory valuation stays stable and predictable.

> In short: Standard Cost trades "perfectly tracked actual cost" for **speed, stability, and predictability** — exactly the trade-off most manufacturing and high-throughput operations want.

---

## 3. Key concept: the **Item Standard Cost** record

The standard rate for an item is published through the **Item Standard Cost** document. Each record carries:

- **Item** — the item being standard-costed (only items whose valuation method resolves to *Standard Cost* are selectable).
- **Company** — the rate is per company.
- **Standard Rate** — the fixed valuation rate (must be greater than zero).
- **Effective Date** — the date from which this rate applies.

Each item+company has a **timeline** of Item Standard Cost records, with **strictly increasing effective dates**. The rate in force on any given date is the latest record whose effective date is on or before that date.

```
Item A (Company X)
 ├─ ISC-2025-0001  Effective 01-Jan-2025  Rate 100   ← rate from 01-Jan-2025 onward
 └─ ISC-2026-0001  Effective 01-Jan-2026  Rate 130   ← rate from 01-Jan-2026 onward
```

---

## 4. Setting up an item's Standard Cost — step by step

### Step 1 — Set the item's valuation method to *Standard Cost*

Set **Valuation Method = Standard Cost** on the item, in one of three ways (most specific wins):

1. **Item master** → *Valuation Method* = `Standard Cost`, **or**
2. Leave the item blank and set the **Company** default valuation method to `Standard Cost`, **or**
3. Leave both blank and set **Stock Settings** → default valuation method to `Standard Cost`.

> **Important:** an item that *already has stock movement* cannot be switched onto Standard Cost retroactively. Enable Standard Cost on a new item, or before any stock transaction exists for it.

### Step 2 — Create the first Item Standard Cost record

1. Go to **Item Standard Cost → New**.
2. Select the **Item** (the dropdown only lists items whose effective valuation method is *Standard Cost*).
3. Select the **Company**.
4. Enter the **Standard Rate** (must be > 0).
5. Set the **Effective Date** (cannot be a future date).
6. **Save** and **Submit**.

> The very first standard cost for an item can only be created **before any stock transaction exists** for that item+company. This guarantees the item starts its life under Standard Cost with nothing to revalue.

### Step 3 — Transact normally

Receive, issue, manufacture, and transfer the item as usual. Every stock ledger entry is automatically valued at the standard rate in force on its posting date.

### Step 4 — Change the rate later (when needed)

When the standard cost needs to change:

1. Create a **new** Item Standard Cost record with the new rate.
2. Give it an **Effective Date after the previous record's effective date** (effective dates must strictly increase) and **on or after the last stock transaction date** for that item.
3. **Submit** it.

On submission, the system automatically creates and submits a **revaluation Stock Reconciliation** that re-states all on-hand stock (across **all warehouses**) from the old rate to the new rate, and books the revaluation gain/loss to the **Stock Adjustment** account. You do not create this reconciliation manually — it is generated for you and linked on the record.

---

## 5. How Standard Cost behaves during transactions & accounting

### Stock ledger valuation

Every stock ledger entry for a standard-cost item is valued at the standard rate, regardless of the document (purchase) rate.

**Example — receive at a price different from standard:**

- Standard rate = **100**
- Purchase Receipt of 10 units billed at **150**
- The stock ledger values the receipt at **100** → stock value increases by **1,000** (not 1,500).

### Accounting — the Purchase Price Variance

The gap between the **document/purchase rate** and the **standard rate** is the *purchase price variance*, and it is posted to the company's **Default Purchase Price Variance Account** (or the item-level override, if set).

**Example — receive 1 unit @ 200, standard 130 (perpetual inventory):**


| Account                       | Debit | Credit |
| ----------------------------- | ----- | ------ |
| Stock (warehouse asset)       | 130   |        |
| Purchase Price Variance       | 70    |        |
| Stock Received But Not Billed |       | 200    |


> The 70 difference lands in **Purchase Price Variance**, *not* in Cost of Goods Sold. This applies to **Purchase Receipts**, and to **Purchase Invoices with "Update Stock"** (both when billed against a receipt and when stand-alone).
>
> **Prerequisite:** the company must have a **Default Purchase Price Variance Account** configured (or an item-level Purchase Price Variance account). If neither is set, the transaction is blocked with a clear error so the variance is never mis-booked.

### Accounting — manufacturing variance

When you manufacture, the finished good is valued at **its own standard rate**, not at the rolled-up cost of the consumed raw materials. Any difference between consumed input value and produced output value is a **manufacturing variance**, posted to the company's **Stock Adjustment** account.

**Example — consume 5 RM @ standard 50 (=250) to produce 1 FG @ standard 200:**

- FG is valued at **200**.
- The **50** difference is booked to **Stock Adjustment**.

### Revaluation on rate change

Publishing a new Item Standard Cost re-values on-hand stock in **every warehouse** to the new rate via the auto-generated revaluation Stock Reconciliation, and posts the gain/loss to **Stock Adjustment**. Serial- and batch-tracked items are revalued across all warehouses too, without requiring serial/batch bundles for the revaluation.

---

## 6. The rules that protect standard-cost integrity

Standard Cost achieves its speed and stability by enforcing a few rules. Understanding *why* they exist makes them easy to live with.

### 6.1 You cannot backdate a transaction before the latest effective rate

> **Rule (R2):** A standard-cost item's stock transaction **cannot be dated before the effective date of its latest Item Standard Cost.**

**Why.** The fast "no-reposting" guarantee depends on the standard rate being **constant** across the window from the latest effective date to today. If you could insert a transaction *before* a rate change:

1. Later stock ledger entries would span **two different rates**, and the fast single-rate value shift would mis-value the entries posted after the rate change; and
2. More seriously, the **revaluation reconciliation** created at the rate change asserted the on-hand quantity *as it was at that moment*. A backdated entry changes that historical quantity, making the revaluation's quantity snapshot — and its GL impact — **stale**. Correcting it would require a full reposting, which is exactly what Standard Cost is designed to avoid.

So the system blocks the entry with a message like:

> **Backdated Entry Not Allowed**  
> Cannot post Standard Cost item *Item A* on **01-06-2025**: it is before **01-01-2026**, the effective date of its latest Standard Valuation Rate *ISC-2026-0001*.  
> Post this entry on or after **01-01-2026**.

**What to do instead:** post the transaction (or a correcting adjustment) **on or after** the latest effective date.

> **Note:** Backdated entries *within the current rate regime* (on or after the latest effective date, but earlier than today) **are** allowed — they only shift later quantities and are handled by the fast quantity/value update with no reposting.

### 6.2 You cannot cancel old stock transactions — create adjustments instead

Once a Standard Cost is established and later transactions exist, you should **not** try to "fix the past" by cancelling old stock vouchers. Cancelling a historical entry is itself a backdated change to the quantity timeline: it would invalidate the on-hand quantity that every later revaluation relied on, and would force a reposting / revaluation cascade — defeating the purpose of standard costing and risking inconsistent inventory value.

**The correct workflow is forward-looking:** record a **new adjustment entry** (e.g. a Stock Entry or Stock Reconciliation) dated **on or after** the latest effective date to reflect the change. This keeps the historical ledger immutable and the standard-cost timeline intact.

Likewise, **Item Standard Cost records cannot be cancelled.** To change a published rate, **submit a new Item Standard Cost** record with the new rate and a later effective date. The new record's revaluation handles the transition cleanly; the old record stays as the historical rate.

---

## 7. Worked scenarios

### Scenario A — Standard purchasing with price variance

1. Set Item A to *Standard Cost*; create Item Standard Cost rate **100**, effective today.
2. Receive 100 units at a billed rate of **120**.
3. **Result:** stock value rises by `100 × 100 = 10,000`; the `100 × 20 = 2,000` price difference is booked to **Purchase Price Variance**. Your inventory is valued at a clean, predictable 100/unit.

### Scenario B — Annual rate revision

1. Item A has run all year at rate **100** (effective 01-Jan-2025), 500 units on hand across two warehouses.
2. On 01-Jan-2026 you publish a new Item Standard Cost rate **130**.
3. **Result:** a revaluation Stock Reconciliation auto-revalues the 500 on-hand units (in both warehouses) from 100 → 130; the `500 × 30 = 15,000` uplift is posted to **Stock Adjustment**. From 01-Jan-2026, new receipts/issues are valued at 130.
4. You now **cannot** post any Item A stock transaction dated before 01-Jan-2026 (see §6.1). A late invoice for December must be recorded with a posting date on/after 01-Jan-2026, or handled as a forward adjustment.

### Scenario C — Backdated correction within the current regime

1. Latest effective rate is **130** (01-Jan-2026); today is 15-Jan-2026.
2. You discover a missed receipt of 20 units dated 05-Jan-2026.
3. **Result:** allowed. The entry posts at rate 130; later entries' running quantities shift forward and their values are re-derived at 130 — **no reposting job**, fast and stable.

### Scenario D — Manufacturing

1. RM standard **50**, FG standard **200**.
2. Repack consumes 5 RM (value 250) and produces 1 FG.
3. **Result:** FG valued at **200**; the **50** manufacturing variance goes to **Stock Adjustment**.

---

## 8. Limitations, best practices & recommendations

### Limitations

- **No retroactive adoption.** An item with existing stock movement cannot be switched to Standard Cost; enable it before the item transacts.
- **The first rate must precede all movement.** The initial Item Standard Cost can only be created before any stock transaction exists for that item+company.
- **Effective dates are strictly increasing**, must not be in the future, and must be on/after the last stock transaction date.
- **No pre-rate-change backdating.** Transactions cannot be dated before the latest effective rate (§6.1).
- **No cancellation** of Item Standard Cost records, and historical stock vouchers should not be cancelled — use forward adjustments (§6.2).

### Best practices

- **Configure accounts up front:** set the company's **Default Purchase Price Variance Account** and **Stock Adjustment Account** before transacting standard-cost items, so variances are booked correctly and the system never blocks a receipt for a missing account.
- **Review variance accounts periodically.** A consistently large Purchase Price Variance signals that your standard rate has drifted from reality — time to publish a new rate.
- **Plan rate changes for clean cut-over dates** (e.g. period/year start). Because you cannot post before the latest effective date, choose an effective date that follows your last booked transaction, ideally after all prior-period entries are in.
- **Make corrections forward, not backward.** Treat the historical ledger as immutable; reflect any change with a new dated adjustment.
- **Use per-item Purchase Price Variance overrides** (via Item Default) only when an item genuinely needs to separate its variance from the company default.

### When to recommend Standard Cost in production

Standard Cost is most beneficial for organizations that:

- run **high transaction volumes** where FIFO/Moving-Average reposting is slow;
- frequently record **backdated corrections** and need them to be cheap and non-disruptive;
- want **predictable, stable product cost** and a clear, isolated view of **price variances**;
- operate **manufacturing** flows where finished goods should carry a planned standard cost.

It is **less suitable** for pure trading operations where the actual landed cost of each lot is the number that matters most.





# Manufacturing Variance (for Standard Cost items)

---

## 1. What is this feature?

When you use the **Standard Cost** valuation method, every finished good is always valued at a fixed **standard rate** that you set — regardless of what it actually cost to make it.

But the real cost of making it (raw materials consumed + any additional/landed costs) is rarely *exactly* equal to that standard rate. There is almost always a small difference.

That difference is called the **Manufacturing Variance**:

- If making the item **cost more** than its standard rate → **unfavourable** variance (you spent more than planned).
- If making the item **cost less** than its standard rate → **favourable** variance (you spent less than planned).

This feature makes sure that difference is booked to a **dedicated Manufacturing Variance account**, so it is easy to see and report on — instead of being quietly mixed into your general Stock Adjustment / cost accounts.

> It is the manufacturing equivalent of the **Purchase Price Variance** you may already use on Purchase Receipts.

---

## 2. A simple example

You value a finished product at a **standard rate of ₹200**.

To produce **1 unit**, you consume raw materials worth **₹250**.

- Finished good goes into stock at its standard value: **₹200**
- Actual cost consumed: **₹250**
- **Manufacturing Variance = ₹50 (unfavourable)** → booked to the Manufacturing Variance account.

If instead the raw materials had only cost **₹180**, the variance would be **₹20 favourable** (a credit in the variance account).

---

## 3. When does it apply?

It applies automatically to a **Manufacture** or **Repack** Stock Entry whenever the **finished good** uses the **Standard Cost** valuation method.

It does **not** apply to items valued using FIFO or Moving Average — those items simply absorb their real cost as usual, so there is no variance to book.

---

## 4. What you need to set up (one time)

The system needs to know **which account** to record the variance in. You can set this in two places:

1. **Company level (recommended default)**
  - Go to **Company** → open your company.
  - In the **Stock Settings** area, set **Default Manufacturing Variance Account**.
  - This account will be used for all Standard Cost items in that company.
2. **Item level (optional override)**
  - Go to the **Item** → **Item Defaults** section (per company).
  - Set **Manufacturing Variance Account** for that specific item.
  - If set, this takes priority over the company default for that item only.

**Which account should it be?** Usually an **Expense-type** account (for example under *Stock Expense* group), chosen together with your accountant.

---

## 5. What happens if the account is not set?

If a Standard Cost item is manufactured/repacked and **no** Manufacturing Variance account is found (neither on the Item nor on the Company), the system will **stop and show an error** asking you to set one.

This is intentional — it prevents the variance from being posted to the wrong place. Simply set the account (Section 4) and submit again.

---

<!-- page: erpnext/erpnext__stock-adjustment-cogs-with-negative-stock.md -->
---
title: "Stock Adjustment / COGS with Negative Stock"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-adjustment-cogs-with-negative-stock"
updated: "2026-07-27"
---

This section explains how negative stock entries lead to stock adjustments. Many users enter negative stock in the system, often by creating delivery notes without existing stock, enabled by activating the 'allow negative stock' option in Stock Settings. 



They do this to dispatch materials to customers with a delivery receipt. To correct negative stock, they usually record a purchase receipt or material receipt. Most users post purchase entries after the delivery note date, resulting in stock adjustments. For example, consider an item called 'Testing Item Stock Adj' with no initial stock. If a delivery note is created for this item, an error appears requiring a valuation rate. The user temporarily sets the valuation rate to 100 to proceed.

![item master](/files/item master.png)

**Delivery Note** 

![](/files/bUy86PL.png)

Since the stock did not exist, the system used a valuation rate of 100 and recorded the stock on hand as shown below.

![gl-entry-negative-stock](/files/gl-entry-negative-stock.png)

Since the stock is negative, we need to record a purchase entry to correct it. We'll do this by creating a purchase receipt with a rate of 300.

![](/files/9e9U8LG.png)

The purchase receipt entry is now created, but it occurs after the Delivery Note (verify the posting date and time for both). The Delivery Note has a valuation rate of 100, while the Purchase Receipt should have a valuation rate of 300 (reflecting the purchase cost). Since the stock was negative, the system applies a valuation rate of 100 (from the previous Delivery Note) for the Purchase Receipt. If it had used 300, the stock quantity would be zero, but the stock value would incorrectly be 200. To avoid this, the system uses a valuation rate of 100, and the discrepancy of 200 is recorded as a stock expense in the Stock Adjustment/COGS account.

![cogs:stock_adjustment](/files/cogs:stock_adjustment.png)

## How to Solve the Problem

Either don't use the negative stock feature or make the purchase entry (backdated) before the dispatch entry, so the system will fix the valuation rate of the delivery note and no adjustment entry will be needed for the Purchase Receipt.



![backdated-pr](/files/backdated-pr.png)



On submission of the above back-dated purchase entry, the system will create a reposting entry that will fix the valuation rate of the delivery note. After the reposting, the Delivery Note's Valuation Rate changes from 100 to 300; therefore, the 'Stock In Hand' changes to 300.

![stock-in-hand-after-repost](/files/stock-in-hand-after-repost.png)

<!-- page: erpnext/erpnext__stock-balance-and-stock-account-balance-syncing.md -->
---
title: "Value Out of Sync Error: Stock Balance and Stock Account Balance Syncing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-balance-and-stock-account-balance-syncing"
updated: "2026-07-02"
---

When [Perpetual Inventory](/erpnext/perpetual-inventory) is enabled, ERPNext keeps the stock ledger and the accounting ledger in sync. If the stock balance and the stock account balance do not match for a company, account, or warehouse, ERPNext stops the transaction and shows a **Value Out of Sync** validation message.

This usually means that older stock or accounting entries created a difference between the stock value and the corresponding stock account balance. The mismatch must be corrected before you can continue posting transactions.

## Why this happens

With Perpetual Inventory, every stock movement also affects accounting. For example, a Purchase Receipt, Delivery Note, Stock Entry, or Sales Invoice with stock impact can update both stock and accounts. If one side was changed, cancelled, reposted, or corrected without the other side matching exactly, the two balances can go out of sync.

ERPNext shows the validation message so that new transactions do not build on an incorrect stock valuation or stock account balance.



![Value out of sync validation message in ERPNext](https://docs.frappe.io/files/kh7A7Gv.png)

## How to fix it

1. Read the validation message carefully and identify the company, stock account, warehouse, and difference amount mentioned in the error.
2. Click **Create Journal Entry** from the validation message.
3. Review the accounts and amounts in the Journal Entry created by ERPNext.
4. Update any missing details, such as cost center or other mandatory accounting dimensions.
5. Save and submit the Journal Entry.
6. Retry the transaction that showed the validation message.

The Journal Entry adjusts the accounting balance so that it matches the stock ledger balance. After the correction is submitted, ERPNext should allow the transaction to proceed.



![Creating a Journal Entry to sync stock and stock account balance](https://docs.frappe.io/files/dd0SQji.gif)

## Before submitting the Journal Entry

- Check that the stock account selected in the Journal Entry is the same account mentioned in the validation message.
- Confirm whether the entry should be a debit or credit based on the difference shown in the error.
- Review accounting dimensions such as cost center, project, or finance book if they are enabled in your setup.
- If the difference is large or unexpected, review recent stock and accounting transactions before submitting the adjustment.

## After the correction

Once the Journal Entry is submitted, open the original document again and try to save or submit it. If the same validation message appears for another account, warehouse, or company, repeat the correction for that specific difference.

If the mismatch keeps returning, check whether older stock reposting, cancelled documents, backdated transactions, or custom accounting entries are affecting the same stock account.

<!-- page: erpnext/erpnext__stock-closing-entry.md -->
---
title: "Stock Closing Entry"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-closing-entry"
updated: "2026-02-25"
---

The purpose of the stock closing entry is to generate the stock closing balance, which includes 
the consolidated stock quantity and consolidated stock value for the selected period. This information will be used to generate the stock reports such as Stock Balance and Batch-Wise Balance History in a short span of time.

## How it Works

The user is required to create a stock closing entry for the desired period, which can span one month, half a month, or an entire year. Upon submission of the stock closing entry, the system generates the stock closing balance for the selected period, including item, batch, inventory dimensions and warehouse wise consolidated closing stock quantities and stock values.

Stock Closing Entry

![](/files/stock-closing-entry.png)

Stock reports, such as Stock Balance and Batch-Wise Balance History, use the Stock Closing Balance data to calculate the opening stock, which is significantly faster than calculating the closing stock using the Stock Ledger Entry.


Note: Will be available in v16

<!-- page: erpnext/erpnext__stock-entry-purpose.md -->
---
title: "Stock Entry Purpose\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-entry-purpose"
updated: "2026-03-12"
---

Stock Entry is a stock transaction, which can be used for multiple purposes. Let's learn about each Stock Entry Purpose below.

#### 1.Purpose: Material Issue

Material Issue entry create to issue item(s) from a warehouse. On submission of Material Issue, stock of item is deducted from the Source Warehouse.

Material Issue is generally made for the low value consumable items like office stationary, product consumables etc. Also you can create Material Issue to reconcile serialized and batched item's stock.

![Material Issue](/files/stock-entry-issue.png)

#### 2.Purpose: Material Receipt

Material Receipt entry is created to inward stock of item(s) in a warehouse. This type of stock entry can be created for updating opening balance of serialized and batched item. Also items purchased without Purchase Order can be inwarded from Material Receipt entry.

For the stock valuation purpose, provided Item Valuation becomes a mandatory field in the Material Receipt entry.

![Material Receipt](/files/stock-entry-receipt.png)

#### 3.Purpose: Material Transfer

Material Transfer entry is created for the inter-warehouse Material Transfer.

![Material Transfer](/files/stock-entry-transfer.png)

#### 4.Purpose: Material Transfer for Manufacture

In the manufacturing process, raw-materials are issued from the stores to the production department (generally WIP warehouse). This Material Transfer entry is created from Work Order. Items in this entry are fetched from the BOM of production Item, as selected in Work Order.

![Transfer for Manufacture](/files/stock-entry-manufacture-transfer.gif)

#### 5.Purpose: Manufacture

Manufacture is created from Work Order. In this entry, both raw-material item as well as production item are fetched from the BOM, selected in the Work Order. For the raw-material items, only Source Warehouse (generally WIP warehouse) is mentioned. For the production item, only target warehouse as mentioned in the Work Order is updated. On submission, stock of raw-material items are deducted from Source Warehouse, which indicates that raw-material items were consumed in the manufacturing process. Production Item is added to the Target Warehouse marking the completion of production cycle.

![Manufacture](/files/stock-entry-manufacture.gif)

#### 6.Purpose: Repack

Repack Entry is created when items purchases in bulk is repacked under smaller packs. [Check this page to know more about Repack entry.](/erpnext/repack-entry.html)

#### 7.Purpose: Subcontract

Subcontracting transaction involves company transfer raw-material items to the sub-contractors warehouse. This requires adding a warehouse for the sub-contractor as well. Sub-contract entry transfers stock from the companies warehouse to the sub-contractors warehouse. [Check this page to know more about Subcontracting](/erpnext/subcontracting.html).

![Subcontract](/files/stock-entry-subcontract.gif)

<!-- page: erpnext/erpnext__stock-entry.md -->
---
title: "Stock Entry"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-entry"
updated: "2026-04-03"
---

**A Stock Entry lets you record Item movement between Warehouses.**

To access the Stock Entry list, go to: 

> Home > Stock > Stock Transactions > Stock Entry

Stock Entries can be made for the following purposes:

- **Material Issue**: If the material is being issued to someone in or outside the company (**Outgoing Material)**. The Items will be deducted from the Warehouse set under Source Warehouse.
- **Material Receipt**: If the material is being received (Incoming Material). The Items will be added to the Warehouse set under Target Warehouse.
- **Material Transfer**: If the material is being moved from one internal Warehouse to another.
- **Material Transfer for Manufacturing**: If raw materials are being transferred for manufacturing. The transfer can happen against a [Work Order](/erpnext/work-order) or a [Job Card](/erpnext/job-card). To know more, visit the [Bill Of Materials](/erpnext/bill-of-materials) page.
- **Material Consumption for Manufacture**: There can be multiple consumption stock entries against a manufacturing Work Order. [Refer this link for more details](/erpnext/material_consumption)
- **Manufacture**: If the Material is being received from a Manufacturing/Production Operation.
- **Repack**: If the Original item/items are being repacked into new item/items.
- **Send to Subcontractor**: If the Material is being issued for a sub-contract activity. This entry is made from a Purchase Order. To know more, visit the [subcontracting](/erpnext/subcontracting) page.

To know more in detail about the stock entry purpose, [visit this page](/erpnext/user/manual/en/stock-entry-purpose).

1. Prerequisites

---

Before creating and using a Stock Entry, it is advised that you create the following first:

- [Warehouse](/erpnext/warehouse)
- [Item](/erpnext/item)

2. How to create a Stock Entry

---

Stock Entries for Manufacturing purposes are usually created from a [Work Order](/erpnext/work-order). To create a Stock Entry manually for other purposes, follow these steps:

1. Go to the Stock Entry list, click on New.
2. Select the Stock Entry Purpose from the ones listed above.
3. If you set the Default Source or Target Warehouses, they'll be automatically filled for the rows in the Items table.
4. Source/Target Warehouses will be available as per the Stock Entry Purpose you selected.
5. Select Items and enter a quantity.
6. The basic rate will be fetched and the amount will be calculated automatically.
7. Save and Submit.

![Stock Entry](/files/stock-entry.png)

Usually, "Source Warehouse" and "Target Warehouse" both are set for recording a movement.

### 2.1 Additional options when creating a Stock Entry

- **Work Order**: If this is a Manufacturing entry, the Work Order will be shown in this field.
- **Edit Posting Date and Time**: Will allow you to edit the Stock Entry's date and time.
- **Inspection Required**: If a [Quality Inspection](/erpnext/quality-inspection) needs to be performed on the Items before submitting the Stock Entry.
- **From BOM**: If this is a Manufacturing entry, the associated BOM for the Item being manufactured will be shown.

### 2.2 Stock Entry Type

You can also create a Stock Entry Type where only the name will be different, for example 'Scrap Entry'. The purpose will be Material Transfer but the name will be different. This is useful if you want certain Users to have access only to specific actions related to stock.

![Stock Entry Type](/files/stock-entry-type.png)



3. Features

---

### 3.1 The Items table

Details about the Item, Rate, Quantity, etc. will be shown here.

Ticking on 'Allow Zero Valuation Rate' will allow submitting the Stock Entry even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

Different Source and Target Warehouses can be set for different Items.

![](/files/imaged7013f.png)

### 3.2 Scrap and Process Loss

- **Scrap Item**: Scrap items are the by-product and can be treated as products. The scrap items will have the valuation rate and they will be added to the scrap warehouse. Users can set the valuation rate for the scrap item manually in the Basic Rate field.
- **Process Loss**: Process Loss has no impact on the stock, this will reduce the number of FG Items. Check the below image, the user has planned to produce 100 FG Items but after the manufacturing process, the quantity has been produced as 80. To produce 80 FG Items, the user has used all raw material quantity. So here 20 quantity has been produced so therefore the system has marked it as Process Loss Qty. The process loss cost of 20 quantities has been added to the 80 quantities of FG Item.

![](/files/CleanShot 2026-04-03 at 10.44.32@2x.png)

### 3.3 Additional Costs

If the stock entry is an incoming entry i.e any item is receiving at a target warehouse, you can add related additional costs (like Shipping Charges, Customs Duty, Operating Costs, etc) associated with the process. The additional costs will be considered to calculate the Valuation Rate of the items.

To add additional costs:

1. Select the Expense Account to which the expense from this Stock Entry will be recorded.
2. Enter the description and amount of the cost in the Additional Costs table.

![Stock Entry Additional Costs](/files/additional-costs-table.png)



The added Additional Costs will be distributed among the receiving items (where the Target Warehouse mentioned) proportionately based on the Basic Amount of the items. And the distributed additional cost will be added to the basic rate of the item, to calculate Valuation Rate.

Quantity and Rate is shown as follows when you expand the Items table. 

![Stock Entry Item Valuation Rate](/files/stock-entry-item-valuation-rate.png)



### 3.4 Accounting Dimensions

You can tag different transactions based on different dimensions. By default, [Projects](/erpnext/project) can be considered as a dimension as it is a common practice to track costs of different projects. To know more about Accounting Dimensions, [visit this page](/erpnext/accounting-dimensions).

### 3.5 Printing Settings

#### Letterhead

You can print your Purchase Receipt on your company's letterhead. Know more [here](/erpnext/letter-head).

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/erpnext/print-headings).

### 3.6 More Information

- **Is Opening**: If this entry is the opening stock entry for the Items.
- **Remarks**: Any additional remarks about the Item.
- **Percentage Transferred**: The percentage of Items transferred depending on Stock Entry purpose.
- **Total Amount**: The total amount of Items transferred.

### 3.7 Perpetual Inventory

If the perpetual inventory system is enabled, additional costs will be booked in Expense Account mentioned in the Additional Costs table .

![Additional Costs General Ledger](/files/stock-entry-additional-cost.png)



![Additional Costs General Ledger](/files/additional-costs-general-ledger.png)



### 3.8 After Submitting

After submitting a Stock Entry, you can go to the stock ledger or the accounting ledger from the dashboard.

![Additional Costs General Ledger](/files/stock-entry-submit.png)



4. Add to Transit

---

If you want to transfer materials from one warehouse to another and you want to make two entries for that then use "Add to Transit" feature.

To use "Add to Transit" feature, make stock entry with type as "Material Transfer" and enable "Add to Transit" checkbox. Next you need to select the source warehouse from where you want to issue the material and then select the warehouse of type "Transit" in the target warehouse. To make transit warehouse you can goto the Warehouse master and select the warehouse type as "Transit". After that add items in the stock entry which needs to be transfer and submit it.

![](/files/CleanShot 2026-04-03 at 11.01.51@2x.png)

To make second stock entry at the destination warehouse, users has two options. Either they can open the Original Stock Entry and click on "End Transit" or they can create new stock entry and click on "Get Items From" -> "Transit Stock Entry". System will fetch items from the original stock entry with the source warehouse (Transit warehouse) same as traget warehouse from the original stock entry. User has to set the target warehouse and save.

![](/files/CleanShot 2026-04-03 at 11.02.51@2x.png)

5. How to update a Stock Entry

---

Once a stock entry is submitted, it can be updated by cancelling and amending the entry

6. Video

---

### 5. Related Topics

1. [Stock Entry Purpose](/erpnext/stock-entry-purpose)
2. [Stock Reconciliation](/erpnext/stock-reconciliation)
3. [Opening Stock Balance Entry For Serialized And Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
4. [Stock Reconciliation](/erpnext/stock-reconciliation)
5. [Work Order](/erpnext/work-order)
6. [Production Plan](/erpnext/production-plan)
7. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__stock-inspection.md -->
---
title: "Stock Inspection"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-inspection"
updated: "2026-02-26"
---

Quality inspection in ERPNext stock module involves assessing and ensuring the quality of incoming and outgoing inventory items.

When items are received into stock, quality inspectors can perform inspections based on predefined criteria such as physical condition, specifications, or regulatory standards. Inspection results can be recorded, and items can be accepted, rejected, or placed on hold based on the inspection outcome.

During outgoing transactions such as sales or transfers, quality inspections can be conducted to verify that items meet specified quality standards before being shipped or transferred.

ERPNext facilitates the creation of inspection criteria, inspection plans, and inspection certificates to streamline the quality control process.

* Quality Inspection Template
* [Quality Inspection](/erpnext/user/manual/en/quality-inspection)

<!-- page: erpnext/erpnext__stock-ledger.md -->
---
title: "Stock Ledger Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-ledger"
updated: "2026-02-26"
---


**A Stock Ledger Report is a detailed record that keeps track of stock movements for a company.**

Inward or outward transactions related to Manufacturing, Purchasing, Selling, and Stock Transfers are recorded in the Stock Ledger which then is reflected in the Stock Ledger Report.

It reflects the quantity and value of stock **issued, received, or transferred** along with the stock item and its warehouse details.

It can be referred when the **Perpetual Inventory** system is enabled, as this report reflects the history of all your stock transactions. It presents a more granular view of the stock transactions.

## Stock Ledger Report Attributes

* **Incoming Rate**: It reflects the actual value of the stock at which it was brought under your inventory.
It reflects the same value as entered in the *Rate* field of the document.

* **Balance Value**: It represents the total value of the remainder stock in the inventory. It is the product of Valuation Rate and Balance Quantity of a stock item.

* **Valuation Rate**: It is calculated based upon the valuation method selected.

Here is how Stock Ledger Report represents a **Stock Entry** of type *Material Receipt*.

![Stock Ledger Report](/files/stock-ledger.png)

It reflects an item **Chair** of quantity *1000 units* with Incoming Rate (Basic Rate) as *Rs.3000* received in warehouse *Stores - L* along with calculating Valuation Rate and Balance Value.

You can click on **Voucher #** to open the document this transaction was created from.

Stock Ledger entries are generated from the following transactions:

- Sales Invoice, Purchase Invoice (with *Update Stock* checked)
- Delivery Note
- Purchase Receipt
- Stock Entry
- Stock Reconciliation

You can add fields from the previously mentioned Document Types by clicking on Menu > Add Column.

<!-- page: erpnext/erpnext__stock-level-report.md -->
---
title: "Stock Level Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-level-report"
updated: "2026-02-26"
---

Stock Level report list stock item's quantity available in a particular warehouse.

There are multiple reports available you can check for item's stock level.

#### Stock Projected Quantity Report

This report list item wise - warehouse wise stock level of an item considering all the stock transactions. With Actual Quantity of an item, it also provide other details like:

1. Actual Qty: Quantity available in the warehouse.
2. Planned Qty: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
3. Requested Qty: Quantity requested for purchase, but not ordered.
4. Ordered Qty: Quantity ordered for purchase, but not received.
5. Reserved Qty: Quantity ordered for sale, but not delivered.
6. Project Qty: Project Quantity is calculated as

Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty

The projected inventory is used by the planning system to monitor the reorder point and to determine the reorder quantity. The projected Quantity is used by the planning engine to monitor the safety stock levels. These levels are maintained to serve unexpected demands.

Having a tight control of the projected inventory is crucial to determine shortages and to calculate the right order quantity.

<!-- page: erpnext/erpnext__stock-masters.md -->
---
title: "Stock Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-masters"
updated: "2026-03-06"
---

In ERPNext, the masters play a crucial role in managing stock-related data, such as items, warehouses, batches, and stock transactions. They provide a structured way to input, store, and retrieve data related to stock items, their attributes, and movements within the system.

Masters in the stock enables businesses to maintain accurate inventory records, track stock movements, and make informed decisions regarding procurement, sales, and stock optimisation. The following are the quick links to some of the important masters in the stock module.

- [Item](/erpnext/user/manual/en/item)
- [Item Group](/erpnext/user/manual/en/item-group)
- [Brand](/erpnext/user/manual/en/brand)
- [Item Variants](/erpnext/user/manual/en/item-variants)
- [Item Attribute](/erpnext/user/manual/en/item-attribute)
- [Unit of Measure](/erpnext/user/manual/en/uom)

<!-- page: erpnext/erpnext__stock-received-but-not-billed.md -->
---
title: "Purpose of Stock Received but not Billed\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-received-but-not-billed"
updated: "2026-03-02"
---


When purchased items are received, an accounts posting is done based on the value of the purchased items in the Stock-in-hand / fixed-assets account. When you sell and deliver those items, an expense (cost-of-goods-sold) is booked, equal to the buying cost of the items.

As stock balance increases through Purchase Receipt, Warehouse account is debited and an adjustment account called **Stock Received But Not Billed** account is credited. At the same time, the negative expense is booked in account head having category as "Valuation" or "Total and Valuation" in taxes and charges table for the amount added for valuation purpose, to avoid double expense booking.

On receiving Bill from the supplier, you will make Purchase Invoice against a Purchase Receipt. Here **Stock Received But Not Billed** account is debited, hence nullifies the balance in the Stock Received but not Billed Account.

The balance in the Stock Received but not Billed account indicates the value of items for which Purchase Receipt has been made, but billing is pending.
