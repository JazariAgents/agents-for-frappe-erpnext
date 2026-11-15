<!-- Frappe documentation: erpnext, part 56 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__selling-settings.md -->
---
title: "Selling Settings | ERPNext Documentation"
description: "Configure ERPNext Selling Settings for customer defaults, pricing, transaction rules, commissions, subcontracting, and document naming."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-settings"
updated: "2026-08-25"
---

Selling Settings controls the defaults and validations used across the ERPNext sales cycle. These settings affect customers, pricing, quotations, sales orders, delivery notes, sales invoices, returns, commissions, and document naming.

Review the settings with your sales, fulfilment, and finance teams before enabling them. A validation that improves control for one business can interrupt a different sales process.

## Before you begin

- You need permission to edit Selling Settings.
- Create the required [Customer Groups](/erpnext/customer-group), [Territories](/erpnext/territory), and [Price Lists](/erpnext/price-list) first.
- Test changes with representative transactions before applying them to production users.

To open the page, go to **Selling &gt; Settings &gt; Selling Settings**. Settings are organized into six tabs. Select **Save** after making changes.

## Customer Defaults

Customer defaults reduce data entry when creating a [Customer](/erpnext/customer) or converting a Lead or Quotation into a Customer.



![Customer Defaults tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/customer-defaults-1440.png)


| Field                  | What it means                                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Naming By     | Choose Customer Name, Naming Series, or Auto Name for the customer ID. Customer Name is the default. Naming Series produces IDs such as CUST-00001.                   |
| Default Customer Group | Sets the Customer Group on new customers when another value is not provided. It is also used when ERPNext creates a Customer while converting a Lead-based Quotation. |
| Default Territory      | Sets the Territory on new customers and supports automatic Customer creation from a Lead-based Quotation.                                                             |


If Default Customer Group or Default Territory is blank, automatic conversion can stop and ask for the missing value.

## Pricing

The Pricing tab determines how ERPNext fetches and validates item rates throughout the sales cycle.



![Pricing tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/pricing-1440.png)


| Field                                                     | What it means                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default Price List                                        | Provides the default selling Price List for a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), Delivery Note, and Sales Invoice.                                                                                                                           |
| Use prices from Default Price List as fallback            | Fetches an Item Price from the default Price List when the transaction’s selected Price List has no matching Item Price. Do not combine it with automatic insertion of missing Item Prices in Stock Settings, because a fallback rate could be written into another Price List. |
| Allow editing Price List rate in transactions             | Makes Price List Rate editable in sales item tables. Keep it disabled when rates must always come from [Item Price](/erpnext/item-price) records.                                                                                                                               |
| Maintain same rate throughout sales cycle                 | Checks whether an item rate changes in a Delivery Note or Sales Invoice created from a Sales Order.                                                                                                                                                                             |
| Action if same rate is not maintained                     | Appears after maintaining the same rate is enabled. Warn allows the transaction after showing a message. Stop prevents the change.                                                                                                                                              |
| Role allowed to override Stop action                      | Appears when the action is Stop. Users with the selected role can override the validation.                                                                                                                                                                                      |
| Validate selling price against purchase or valuation rate | Blocks a sale when the selling rate is below the relevant purchase or valuation rate. Test this carefully for promotions and clearance items.                                                                                                                                   |
| Calculate Product Bundle price based on child Item rates  | Makes packed-item rates editable and calculates the [Product Bundle](/erpnext/product-bundle) price from its child items. A manually changed bundle rate is recalculated when the document is saved.                                                                            |
| Allow negative rates for Items                            | Permits negative item rates for supported adjustments, refunds, returns, or special pricing. Use this only with appropriate accounting review.                                                                                                                                  |


## Transaction

Transaction settings define which documents are required and which exceptions users may use.



![Transaction tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/transaction-1440.png)


| Field                                                             | What it means                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Is Sales Order required to create Sales Invoice or Delivery Note? | Set to Yes to require a Sales Order before a [Sales Invoice](/erpnext/sales-invoice) or [Delivery Note](/erpnext/delivery-note). A Customer can allow Sales Invoice creation without a Sales Order as an exception. |
| Is Delivery Note required to create Sales Invoice?                | Set to Yes to require a Delivery Note before invoicing. A Customer can allow invoicing without a Delivery Note as an exception.                                                                                     |
| How often should sales data be updated in Company or Project?     | Choose Each Transaction, Daily, or Monthly. Daily or Monthly can reduce repeated updates on sites with a high transaction volume.                                                                                   |
| Allow same Item to be added multiple times                        | Allows the same item on more than one row of a transaction. Disable it when duplicate lines are usually an error.                                                                                                   |
| Allow multiple Sales Orders against a customer’s Purchase Order   | Allows several Sales Orders to use the same customer purchase order number and date.                                                                                                                                |
| Hide Customer’s Tax ID from sales transactions                    | Stops the Customer Tax ID from appearing in selling transactions when your process does not require it.                                                                                                             |
| Allow Sales Order creation for expired Quotation                  | Allows an expired Quotation to be converted. Users should still confirm that the rate and terms remain valid.                                                                                                       |
| Don’t reserve Sales Order qty on sales return                     | Prevents a return from automatically reserving quantity against the linked Sales Order.                                                                                                                             |
| Enable cut-off date on creating bulk Delivery Notes               | Adds a cut-off date to bulk Delivery Note creation so only eligible Sales Orders up to that date are processed.                                                                                                     |
| Set incoming rate as zero for expired Batch                       | Sets the incoming rate to zero for a stand-alone credit note containing an item from an expired Batch.                                                                                                              |
| Allow Quotation with zero quantity                                | Allows zero-quantity lines when the rate is agreed before the quantity, such as a rate contract.                                                                                                                    |
| Allow Sales Order with zero quantity                              | Allows zero-quantity Sales Order lines for a similar rate-contract workflow.                                                                                                                                        |
| Blanket Order Allowance (%)                                       | Controls how much a Sales Order may exceed the quantity agreed in a [Blanket Order](/erpnext/blanket-order).                                                                                                        |


## **Skip Delivery Note Creation for Service Items**

![](/files/Screenshot 2026-08-25 at 5.20.08 PM.webp)

Sales Orders that contain services no longer wait for a delivery that will never happen. When this setting is on, non-stock items are excluded from delivery tracking, and an order made up entirely of them completes as soon as it is fully billed.

### The problem it solves

A Sales Order for services — consulting, installation, an AMC — has nothing to deliver. Without this feature the order still expects a Delivery Note, so after billing it sits at **To Deliver** and eventually shows as **Overdue**, even though the work is done and paid for.

### Enabling it

> **Selling Settings → Skip Delivery Note for Service Items**

The switch applies to all order types — Sales, Maintenance, and Shopping Cart alike. No per-order checkbox is needed; each order works it out from its items.

### How items qualify

Every time a Sales Order is saved, each item row is marked with a hidden `Skip Delivery` flag. A row is exempt from delivery only when **all** of these hold:

- the item is not a stock item
- the item is not a fixed asset
- the item is not a Product Bundle that contains stock items
- the row is not delivered by the supplier (drop shipping)

Anything failing a check keeps normal delivery tracking. The flags refresh on every save — including **Update Items** on a submitted order — so changing the item mix or the setting is always reflected.

### Order status

When every row on the order is exempt, the order needs no delivery at all: **% Delivered** is set to 100 and the delivery status shows **Not Applicable**.

```
To Bill  →  (Sales Invoice for the full amount)  →  Completed
```

On a mixed order, only the deliverable rows count toward **% Delivered**, and the Delivery Note picks up only those rows. The order completes once the stock items are delivered and everything is billed.

### Examples


| Order contents         | Delivery Note   | Completed when                        |
| ---------------------- | --------------- | ------------------------------------- |
| Services only          | Not required    | Fully billed                          |
| Stock items + services | Stock rows only | Stock rows delivered and fully billed |
| Setting disabled       | All rows        | Fully delivered and fully billed      |


## Advanced Features

Use these settings when your implementation requires commission tracking, separate discount accounting, or campaign attribution.



![Advanced Features tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/advanced-features-1440.png)


| Field                                  | What it means                                                                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Enable tracking sales commissions      | Enables commission management for Sales Partners and the sales team.                                                                      |
| Enable discount accounting for selling | Creates additional ledger entries to post discounts to a separate Discount Account.                                                       |
| Enable UTM                             | Adds UTM attribution fields to supported documents including Lead, Quotation, Sales Order, Delivery Note, Sales Invoice, and POS Invoice. |
| Use Legacy (Client side) Reactivity    | An experimental compatibility option. Keep the default unless a tested customization requires the legacy behavior.                        |


## Subcontracting Inward

These controls apply when your company receives materials from a customer, processes them, and delivers finished goods back to that customer.



![Subcontracting Inward tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/subcontracting-inward-1440.png)


| Field                                   | What it means                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Allow delivery of overproduced quantity | Allows the entire produced quantity to be delivered even when it exceeds the Subcontracting Inward Order quantity. |
| Deliver secondary Items                 | Adds secondary items generated with a finished good to the Stock Entry used for delivery.                          |


## Document Naming

This tab shows the current naming series for Quotation, Sales Order, Sales Invoice, and Delivery Note, including separate return series where applicable.



![Document Naming tab in ERPNext Selling Settings](https://novacompanies.m.frappe.cloud/files/document-naming-1440.png)

Configure or extend naming series according to your company’s document-control policy. Avoid changing an active series without checking reporting, integrations, and print formats.

## Frequently asked questions

### Can I require a Sales Order for most customers but allow exceptions?

Y

es. Set the global requirement in Selling Settings, then use the relevant exception on the Customer record for approved cases.

### Why are some pricing fields not visible?

Action and override-role fields appear only after Maintain same rate throughout sales cycle is enabled. The override role is relevant when the selected action is Stop.

### Should I allow users to edit Price List Rate?

Enable it only when users are authorized to depart from maintained Item Prices. Otherwise, keep the field controlled and use Pricing Rules for repeatable exceptions.

### When should zero-quantity transactions be allowed?

Use them for rate contracts or agreements where the unit rate is confirmed before the final quantity. They should not replace quantities in normal orders.

### What should I test after changing Selling Settings?

Create a test Customer, Quotation, Sales Order, Delivery Note, Sales Invoice, and return that reflect your normal and exception workflows. Confirm rates, document links, accounting entries, and permissions before production use.

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
