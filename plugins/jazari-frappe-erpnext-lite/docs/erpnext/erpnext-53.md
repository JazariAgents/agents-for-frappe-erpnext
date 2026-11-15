<!-- Frappe documentation: erpnext, part 53 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__sales-order.md -->
---
title: "Sales Order | ERPNext Documentation"
description: "Learn how to create and submit a Sales Order in ERPNext, add customers and items, apply pricing, and continue to delivery, billing, and payment."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-order"
updated: "2026-08-22"
---

Imagine you manage sales at Nova Chemicals. A customer confirms an order for 200 drums of industrial cleaner, to be delivered next month at an agreed price. If this agreement remains in an email or spreadsheet, the warehouse may not know what to prepare, finance may invoice the wrong quantity, and the sales team cannot easily track what remains to be delivered.



A Sales Order turns this confirmed agreement into a shared operational record. It records the customer, items, quantities, prices, delivery dates, taxes, and terms before the goods are dispatched or the customer is invoiced.



For Nova Chemicals, the Sales Order becomes the starting point for preparing the goods, creating one or more Delivery Notes, billing the customer, and tracking the order until it is fully delivered and invoiced.



A **Sales Order** in ERPNext records a customer's confirmed request, including Items, prices, quantities, delivery dates, shipping details, and terms.



Submitting the Sales Order confirms the commitment and makes it available for the next steps, such as picking, delivery, invoicing, purchasing, manufacturing, or collecting payment.



![ERPNext order-to-cash flow from Quotation through Payment Entry, with Sales Order highlighted as the current stage.](/files/order-to-cash-sales-order.webp)

The standard order-to-cash flow is **[Quotation](/erpnext/quotation) → Sales Order → [Delivery Note](/erpnext/delivery-note) → [Sales Invoice](/erpnext/sales-invoice) → [Payment Entry](/erpnext/payment-entry)**. You can also create a Sales Invoice directly from a submitted Sales Order when a separate delivery transaction is not required. You can also start without a Quotation or add picking, manufacturing, and purchasing steps.

## Before you begin

Create or confirm the following records:

- a [Company](/erpnext/company) and [Customer](/erpnext/customer);
- at least one [Item](/erpnext/item);
- an [Item Price](/erpnext/item-price) or a rate you can enter manually;
- a source [Warehouse](/erpnext/warehouse) if you deliver stock items;
- [taxes](/erpnext/setting-up-taxes), [payment terms](/erpnext/payment-terms), and [shipping rules](/erpnext/shipping-rule) when your sales process requires them.

You need create permission and submit permission to confirm an order.

## Create a Sales Order

1. Open **Sales Order** from the Selling workspace.
2. Select **Add Sales Order**.
3. Select the **Company** and **Customer**.
4. Keep **Order Type** as **Sales** for a standard customer order.
5. Set the transaction **Date** and promised **Delivery Date**.
6. Under **Items**, optionally set **Set Source Warehouse** to apply one warehouse to all stock items.
7. Add each Item and enter its **Quantity**. Review the delivery date, rate, and amount for every row.
8. Review taxes, totals, addresses, and commercial terms.
9. Save the document. ERPNext keeps it in **Draft** status.
10. Select **Submit** when the order is confirmed.

![A draft Sales Order for Northstar Retail showing two item rows, with the pencil icon highlighted for opening the row editor.](/files/sales-order-draft-items.webp)

Select the **pencil icon** at the end of an item row to open its full row editor. Use it when you need to review or update fields that are not visible as table columns.

The dot before an Item Code shows stock availability at a glance: green means the Item is in stock, while red means it is out of stock.

> Saving and submitting are different actions. You can edit a draft freely. Submission confirms the order and enables downstream transactions.

## Alternative ways to create a Sales Order

You can create a Sales Order from a submitted Quotation, which carries forward the customer, items, rates, taxes, and terms. Depending on your configuration, orders can also originate from integrations or the shopping cart.

For recurring requirements, use a Blanket Order or [Auto Repeat](/recurring-sales-orders-with-auto-repeat) only when the corresponding business process calls for it.

## Important fields and what they mean

The table covers fields that affect pricing, fulfillment, accounting, or downstream documents.


| Area               | Field                                    | What it means                                                                                                                                                       |
| ------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Order              | Company                                  | The company fulfilling the order and the basis for its currency, warehouses, and accounting defaults.                                                               |
| Order              | Customer                                 | The party placing the order. ERPNext can fetch its address, contact, territory, price list, and payment terms.                                                      |
| Order              | Order Type                               | Use **Sales** for a normal customer order, **Maintenance** for maintenance work, or **Shopping Cart** for website orders.                                           |
| Order              | Date                                     | The Sales Order transaction date.                                                                                                                                   |
| Order              | Delivery Date                            | The default promised date. An item row can use a different date for split delivery schedules.                                                                       |
| Order              | Customer's Purchase Order                | The customer's purchase-order reference and date, useful for matching documents and communication.                                                                  |
| Pricing            | Currency                                 | The transaction currency used for rates and totals.                                                                                                                 |
| Pricing            | Price List                               | The [Price List](/erpnext/price-lists) from which ERPNext fetches item rates. Whether users can change a fetched Price List Rate is controlled in Selling Settings. |
| Pricing            | Exchange Rate                            | Converts the transaction currency to company currency when they differ.                                                                                             |
| Pricing            | Ignore Pricing Rule                      | Prevents configured [Pricing Rules](/erpnext/pricing-rule) from being applied. Use it only when the order requires an exception.                                    |
| Items              | Scan Barcode                             | Finds and adds an Item using its configured barcode; scanning the same barcode again increases its quantity.                                                        |
| Items              | Set Source Warehouse                     | Applies one source warehouse to stock-item rows and overrides an Item's default warehouse; a row-level Warehouse can override it again.                             |
| Items              | Item Code                                | Identifies the product or service being ordered.                                                                                                                    |
| Items              | Delivery Date                            | Sets the promised date for that item row.                                                                                                                           |
| Items              | Quantity                                 | Records how many units the customer ordered in the selected unit of measure.                                                                                        |
| Items              | Rate                                     | The selling price per unit before row-level taxes; you can change a fetched rate when permissions allow.                                                            |
| Items              | Warehouse                                | Sets the location that will fulfill a stock-item row.                                                                                                               |
| Items              | Reserve Stock                            | Allocates available stock to the order when [stock reservation](/erpnext/stock-reservation) is configured; it does not create a stock-ledger movement.              |
| Address            | Customer Address                         | The customer's billing address used on the order and print format.                                                                                                  |
| Address            | Shipping Address                         | The destination for delivery. Confirm it when it differs from the billing address.                                                                                  |
| Address            | Contact Person                           | The customer contact associated with the order.                                                                                                                     |
| Taxes and delivery | Tax Category                             | Helps ERPNext select the applicable tax treatment or template.                                                                                                      |
| Taxes and delivery | Sales Taxes and Charges Template         | Applies a reusable tax and charge structure; its rows can be adjusted when permitted.                                                                               |
| Taxes and delivery | Sales Taxes and Charges                  | Lets you add tax or charge rows manually when a template is not suitable. Review **Tax Breakup** to understand the calculated taxes.                                |
| Taxes and delivery | Shipping Rule                            | Adds freight or shipping charges according to the rule's conditions.                                                                                                |
| Taxes and delivery | Incoterm and Named Place                 | Records agreed delivery responsibilities and the location to which the Incoterm applies.                                                                            |
| Discount           | Apply Additional Discount On             | Chooses whether an order-level discount applies to the Net Total or Grand Total.                                                                                    |
| Discount           | Additional Discount Percentage or Amount | Reduces the order total by the entered percentage or value; item-level discounts remain on their rows.                                                              |
| Terms              | Payment Terms Template                   | Generates the payment schedule from reusable payment terms.                                                                                                         |
| Terms              | Payment Schedule                         | Shows due dates and amounts generated by a template, or lets you enter the schedule manually.                                                                       |
| Terms              | Terms and Conditions                     | Adds standard or order-specific commercial terms to the document.                                                                                                   |
| Reference          | Project                                  | Links the order to an existing Project for project-based tracking.                                                                                                  |
| Reference          | Inter Company Order Reference            | Links the related Purchase Order when the Sales Order belongs to an inter-company transaction.                                                                      |


X

## Submit and next steps

After submission, the Sales Order normally moves to **To Deliver and Bill**. Available actions depend on the order, installed modules, settings, and your permissions.

From **Create**, ERPNext v17 can offer documents such as:

- **Pick List** to organize item picking;
- **Delivery Note** to record shipment or delivery;
- **Sales Invoice** to bill the customer;
- **Payment Request** or **Payment** to collect or record funds;
- **Material Request** or **Purchase Order** for procurement;
- **Work Order**, **Production Plan**, or **Request for Raw Materials** for manufacturing;
- **Project** for project-based delivery.



![The Create menu on a submitted Sales Order showing available fulfillment, billing, procurement, and production documents.](/files/sales-order-create-actions.webp)

An order can be partially delivered or billed across multiple documents. ERPNext updates its delivery and billing percentages.

### Skip a Delivery Note

For a **Maintenance** Sales Order, enable **Skip Delivery Note** when the service should be invoiced without a separate delivery transaction. See [Maintenance Sales Orders](/erpnext/maintenance-sales-orders) for the complete workflow.



![A full-screen Maintenance Sales Order showing the Skip Delivery Note checkbox beside Order Type.](/files/sales-order-skip-delivery-note-full.webp)

### Update, hold, close, amend, or cancel

- Use **Update Items** after submission when the allowed item values need to change. ERPNext restricts changes that conflict with quantities already picked, delivered, billed, or assigned to production.
- Use **Status &gt; Hold** to pause fulfillment and **Resume** when work can continue.
- Close an order when you intentionally will not fulfill its remaining quantity.
- Cancel a submitted order when the entire transaction should be reversed and its linked-document state permits cancellation.
- To revise a cancelled order, use **Amend**. ERPNext creates a new draft linked to the cancelled order.

## Status

The Sales Order list shows the overall status, delivery date, grand total, percentage delivered, and percentage billed.



![The full Sales Order list showing draft, pending, and completed orders with delivery and billing progress.](/files/sales-order-list-statuses-full.webp)

Important statuses include:


| Status              | Meaning                                        |
| ------------------- | ---------------------------------------------- |
| Draft               | Saved but not confirmed                        |
| To Deliver and Bill | Submitted; delivery and billing are pending    |
| To Deliver          | Billing is complete but delivery remains       |
| To Bill             | Delivery is complete but billing remains       |
| Completed           | Delivery and billing requirements are complete |
| On Hold             | Processing is paused                           |
| Closed              | Remaining fulfillment was intentionally closed |
| Cancelled           | The submitted order was cancelled              |


Use the separate **Delivery Status**, **Billing Status**, and **Advance Payment Status** filters for a more precise view.

## Types of Sales Order

- **Sales** is the standard order for goods or services.
- **Maintenance** supports maintenance-related fulfillment. See [Maintenance Sales Orders](/erpnext/maintenance-sales-orders).
- **Shopping Cart** identifies orders originating from the web-shopping flow.

Downstream actions change with the order type and installed features.

## Troubleshooting

### Item rates are empty

Confirm that the Item has an active price in the selected selling Price List and currency. Otherwise, enter an allowed rate manually. Also check whether a pricing rule changes the expected rate.

### The expected address or contact is unavailable

Open the Customer and confirm that the Address or Contact is linked to that Customer. Then reload or reselect the Customer on the draft Sales Order.

### Submit is unavailable or fails

Confirm that all mandatory fields are complete and that your role has submit permission. Review the validation message for missing delivery dates, invalid items, disabled masters, or other configuration issues.

### A fulfillment option is missing from Create

The menu is conditional. Check the Sales Order's status and order type, your permissions, installed modules, company settings, and whether the relevant quantity has already been delivered or billed.

### The order remains open after delivery or billing

Check both the delivered and billed percentages and review all linked Delivery Notes and Sales Invoices. A partially processed item or an intentionally skipped step can leave a remaining quantity.

## Frequently asked questions

### Does submitting a Sales Order change stock or create accounting entries?

The Sales Order itself records a commitment. Normal submission does not deliver stock or recognize an invoice. Stock and accounting effects occur through the linked fulfillment and billing documents used by your process.

### Can one Sales Order have multiple delivery dates?

Y

es. The order has a default Delivery Date, and individual item rows can use different dates.

### Can I deliver or invoice only part of an order?

Y

es. Create the Delivery Note or Sales Invoice for the required rows and quantities. ERPNext tracks the remaining percentages on the Sales Order.

### Can I edit a Sales Order after submission?

You can use **Update Items** for supported changes, subject to linked-document and fulfilled-quantity restrictions. For broader changes, cancel and amend the order when the transaction state allows it.

### When should I close instead of cancel a Sales Order?

Close the order when the submitted order remains historically valid but you will not fulfill the outstanding quantity. Cancel it when the submitted transaction itself should be reversed.

## Related topics

- [Quotation](/erpnext/quotation)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Partial Fulfilment of a Sales Order](/erpnext/partial-fulfilment-of-sales-order)
- [Close Sales Order](/erpnext/close-sales-order)
- [Amend a Sales Order after submission](/erpnext/amending-sales-order-after-submit)

<!-- page: erpnext/erpnext__sales-partner.md -->
---
title: "Sales Partner Commission | ERPNext Documentation"
description: "Set up Sales Partners, commission, targets, referrals, website details, and performance reports in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-partner"
updated: "2026-07-24"
---

A Sales Partner is an external reseller, dealer, agent, affiliate, implementation partner, or other organization that helps generate business. ERPNext can attribute sales, calculate commission, allocate targets, track referrals, and report partner performance.

Use a [Sales Person](/erpnext/sales-person) for internal sales-team contribution and incentives. Use a Sales Partner when the relationship is external and may require commission settlement through a Supplier.

## Before you begin

Prepare:

- A Sales Partner Type such as Reseller, Dealer, or Affiliate.
- The partner's default [Territory](/erpnext/territory).
- The agreed commission rate and eligible sales basis.
- Address and contact information.
- A [Fiscal Year](/erpnext/fiscal-year) and [Monthly Distribution](/erpnext/monthly-distribution) when partner targets will be used.
- A [Supplier](/erpnext/supplier) when commission must be recorded and paid through Accounts Payable.

## Create a Sales Partner

1. Open **Sales Partner** and select **New**.
2. Enter the **Sales Partner Name**.
3. Select the **Partner Type**.
4. Select the **Territory**.
5. Enter the default **Commission Rate**.
6. Save.

The highlighted fields define the partner category, geographic association, and default commission percentage.

![Sales Partner master with partner type, territory, and commission rate](https://novacompanies.m.frappe.cloud/files/sales-partner-master.png)

## Important fields and what they mean


| Field              | Meaning                                                                   |
| ------------------ | ------------------------------------------------------------------------- |
| Sales Partner Name | Partner shown on transactions, targets, and reports                       |
| Partner Type       | Classification used to organize partners                                  |
| Territory          | Default market area associated with the partner                           |
| Commission Rate    | Default percentage copied to supported sales transactions                 |
| Targets            | Item Group-wise quantity or amount targets for a Fiscal Year              |
| Show in Website    | Exposes website-related partner fields when website publishing is used    |
| Referral Code      | Code used to attribute supported website traffic or orders to the partner |
| Partner Website    | External website maintained by the partner                                |
| Route              | Website route generated for the partner page when applicable              |


## Add addresses and contacts

After saving the Sales Partner, use **New Address** and **New Contact** in **Address & Contacts**.

Create an [Address](/erpnext/address) for the partner's business or payment location and a [Contact](/erpnext/contact) for the person responsible for sales, statements, or commission queries. A partner can have more than one address or contact when different teams handle commercial and finance activities.

Keep legal payment details on the Supplier record when the partner is also paid through Accounts Payable.

## Record Sales Partner commission

Sales Partner fields are available on supported transactions such as a [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), and [Sales Invoice](/erpnext/sales-invoice).

1. Open the sales transaction and select **More Info**.
2. Expand **Commission**.
3. Select the Sales Partner.
4. Review the amount eligible for commission.
5. Confirm the commission rate and calculated total.
6. Save and submit the transaction through the normal approval process.

![Sales Partner commission calculated on a Sales Order](https://novacompanies.m.frappe.cloud/files/sales-order-commission.png)

The commission value is operational data. It does not automatically create an expense, payable, or payment. See [Sales Commission](/erpnext/how-to-give-commission-to-sales-partner) for the accounting handoff.

## Allocate a Sales Partner target

Targets help compare planned partner performance with actual submitted sales.

1. Open the Sales Partner.
2. In **Sales Partner Target**, select **Add row**.
3. Enter the Item Group, Fiscal Year, Target Qty, Target Amount, and Target Distribution.
4. Use the highlighted pencil icon to open the complete child-row editor when needed.
5. Save.

![Item Group-wise target allocated to a Sales Partner](https://novacompanies.m.frappe.cloud/files/sales-partner-target.png)


| Target field        | Meaning                                                   |
| ------------------- | --------------------------------------------------------- |
| Item Group          | Product category measured by the target                   |
| Fiscal Year         | Year in which planned and actual performance are compared |
| Target Qty          | Planned unit volume                                       |
| Target Amount       | Planned sales value                                       |
| Target Distribution | Monthly percentage distribution for the annual target     |


You can set quantity, amount, or both. Avoid overlapping rows unless the reporting design intentionally measures an all-item target and separate Item Group targets.

## Track referrals

A Referral Code can identify traffic or supported e-commerce orders associated with the partner.

1. Enter a unique **Referral Code**, as highlighted.
2. Save the Sales Partner.
3. Give the partner an approved campaign URL containing the referral parameter used by your website implementation.
4. Test the complete checkout flow before launching the campaign.

![Website and referral settings on a Sales Partner](https://novacompanies.m.frappe.cloud/files/sales-partner-referral.png)

A typical parameter uses the partner code, for example:

**[https://shop.example.com/?sp=APEX5](https://shop.example.com/?sp=APEX5)**

Referral behavior depends on the installed website and e-commerce configuration. Test attribution on the current site and confirm that the resulting transaction contains the Sales Partner.

## Show a Sales Partner on the website

Select **Show in Website** when the site should publish partner information and the website implementation supports Sales Partner pages. Complete the route, logo, partner website, introduction, and description fields that appear.

Before publishing:

- Obtain permission to use the partner's name and logo.
- Use approved marketing copy.
- Confirm the route and public page in the current website theme.
- Avoid placing private contacts, commission rates, targets, or internal notes on the public page.

The exact listing route and presentation can vary by ERPNext version and website setup. Verify the rendered page instead of assuming an older default partners page is active.

## Review Sales Partner Commission Summary

Open **Sales Partner Commission Summary** and set:

1. Company.
2. Sales Partner when reviewing one partner.
3. Document type, such as Sales Order, Delivery Note, Sales Invoice, or POS Invoice.
4. From Date and To Date.
5. Optional Customer and Territory filters.

The highlighted result shows the calculated commission for the submitted transaction.

![Sales Partner Commission Summary with a submitted Sales Order](https://novacompanies.m.frappe.cloud/files/commission-summary.png)

Use this report to review transaction-level commission totals. Reconcile approved totals with Supplier invoices and [Payment Entries](/erpnext/payment-entry) before marking the partner as paid.

## Other Sales Partner reports


| Report                            | Use                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------- |
| Sales Partner Commission Summary  | Summarizes commission by sales transaction                                                   |
| Sales Partner Transaction Summary | Reviews partner-attributed transaction details, including item-level context where available |
| Sales Partner Target Variance     | Compares allocated targets with qualifying actual performance by period                      |


For target variance, confirm that transactions are submitted, contain the Sales Partner, fall within the correct period, and use the expected Item Group and company.

## Pay Sales Partner commission

The report does not create accounting entries. A controlled payment workflow usually requires:

1. A Supplier representing the Sales Partner.
2. A dedicated [Supplier Group](/erpnext/supplier-group) when partner payables should be separated.
3. A finance-approved [Purchase Invoice](/erpnext/purchase-invoice) or other payable document for the commission.
4. Applicable tax or withholding treatment.
5. A Payment Entry against the approved payable.
6. Reconciliation to the Sales Partner commission report.

Follow local accounting and tax advice. The commission field itself is not a tax calculation.

## Disable or change a partner relationship

Sales Partner does not have a transactional submission lifecycle. Update master details carefully because defaults affect new transactions.

When a relationship ends:

- Stop selecting the partner on new transactions.
- Remove or deactivate referral campaigns in the website or marketing system.
- Preserve historical transactions and commission records.
- Settle or dispute outstanding commissions through the approved finance process.
- Retain public website content only when the agreement permits it.

## Troubleshooting

### The partner is missing from a transaction

Confirm that the Sales Partner master exists and that the user has read permission. Check link-field filters and spelling.

### The transaction shows zero commission

Review the amount eligible for commission, commission rate, and item eligibility. Save the transaction after correcting the values.

### The report shows no transactions

Check Company, Sales Partner, document type, date range, and submission status. Draft transactions do not appear as confirmed commission activity.

### The referral code does not populate the order

Verify the URL parameter, website implementation, cookies or session behavior, and checkout workflow. Test with a new browser session and confirm the Sales Partner field on the resulting order.

### Target variance is incorrect

Check the target Fiscal Year, Item Group, Monthly Distribution, transaction dates, and Sales Partner attribution.

## Frequently asked questions

### Can a Sales Partner also be a Customer or Supplier?

Yes, but each party role has a separate purpose. Link and reconcile the records according to your master-data policy.

### Can one transaction have both a Sales Partner and Sales Persons?

Yes. The external partner commission and internal Sales Team contribution are separate fields and processes.

### Does ERPNext pay commission automatically?

No. It calculates and reports the value. Finance must record and pay the approved amount.

### Can different transactions use different commission rates?

Yes, when permissions and commercial policy allow an exception to the default rate.

### Can targets be seasonal?

Yes. Link a Monthly Distribution that allocates a larger percentage to peak months.

## Related topics

- [Sales Commission](/erpnext/how-to-give-commission-to-sales-partner)
- [Sales Person](/erpnext/sales-person)
- [Sales Person Target Allocation](/erpnext/sales-person-target-allocation)

<!-- page: erpnext/erpnext__sales-person-target-allocation.md -->
---
title: "Sales Person Target Allocation | ERPNext Documentation"
description: "Allocate Sales Person and Territory targets, apply Monthly Distribution, and review target variance in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-person-target-allocation"
updated: "2026-07-24"
---

Sales targets in ERPNext compare planned quantity or revenue with actual performance from submitted sales transactions. Targets can be assigned to a [Sales Person](/erpnext/sales-person) or a [Territory](/erpnext/territory), then distributed across months for seasonal or uneven sales plans.

## Before you begin

Create or confirm:

- The required Sales Person hierarchy.
- The relevant [Fiscal Year](/erpnext/fiscal-year).
- Item Groups when targets should apply to specific product categories.
- A [Monthly Distribution](/erpnext/monthly-distribution) when the target should not be spread evenly by the report logic.
- Sales transactions that identify the responsible Sales Person in the **Sales Team** table.

Targets are useful only when transaction attribution is consistent. Submitted Sales Orders must contain the correct Sales Person and contribution percentage for Sales Person variance reporting.

## Allocate a target to a Sales Person

1. Open the required Sales Person.
2. Scroll to **Sales Person Targets**.
3. Select **Add row**, as highlighted.
4. Complete the target values. Use the highlighted pencil icon to open the child row when you need the full editor.
5. Save the Sales Person.

![A 2026 laptop target allocated to a Sales Person](https://novacompanies.m.frappe.cloud/files/sales-person-target.png)

## Target fields and what they mean


| Field               | What it controls                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Item Group          | Limits the target to sales of items in that Item Group; leave it blank only when your reporting design expects an all-item target |
| Fiscal Year         | The year in which ERPNext measures target and actual performance                                                                  |
| Target Qty          | Planned sales quantity for the Fiscal Year                                                                                        |
| Target Amount       | Planned sales value for the Fiscal Year                                                                                           |
| Target Distribution | Monthly Distribution used to spread the annual target across months                                                               |


You can enter a quantity target, an amount target, or both. Use quantity when unit volume is meaningful and stable. Use amount when revenue is the primary measure. Use both when managers need to monitor volume and value together.

Avoid overlapping target rows unless you understand how the selected report groups them. For example, an all-item target and a separate Laptops target for the same person and Fiscal Year can represent different management goals, but they should not be interpreted as one simple total without review.

## Distribute the annual target across months

A Monthly Distribution assigns a percentage of the annual target to each month. Use it for seasonal demand, ramp periods, product launches, or quarter-heavy sales cycles.

1. Open **Monthly Distribution**.
2. Select the Fiscal Year.
3. Enter the percentage allocation for every month.
4. Confirm that the full-year allocation totals 100%.
5. Save, then select the record in **Target Distribution** on the Sales Person target row.

![An even Monthly Distribution for fiscal year 2026](https://novacompanies.m.frappe.cloud/files/monthly-distribution.png)

For an annual amount target of $144,000, an even distribution produces roughly $12,000 per month. A seasonal plan might allocate a larger percentage to the months in which demand is expected to peak.

## Record Sales Person contribution on transactions

Actual performance is derived from submitted transactions and their Sales Team allocation.

On each supported [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice), open the **Sales Team** table and:

1. Select the Sales Person.
2. Enter **Contribution (%)**.
3. Add other Sales Persons when the sale is shared.
4. Confirm that the allocation reflects your reporting policy.

For target variance based on Sales Orders, the order must be submitted and contain the relevant Sales Person. Draft orders do not represent confirmed actual performance.

See [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions) for the complete transaction workflow.

## Review Sales Person target variance

Open **Sales Person Target Variance** from Selling reports. Set the company, Fiscal Year, period, and other filters required by your version.

The report compares:


| Measure     | Meaning                                                       |
| ----------- | ------------------------------------------------------------- |
| Target      | Planned quantity or amount for the selected period            |
| Actual      | Performance derived from qualifying submitted transactions    |
| Variance    | Difference between target and actual performance              |
| Achievement | Progress toward the target, often interpreted as a percentage |


If an annual quantity target of 120 is evenly distributed, the monthly target is about 10 units. If qualifying orders contain 8 units for the month, the quantity variance is 2 units below target.

## Allocate a target to a Territory

Territory targets measure sales performance for customers assigned to a geographic or market hierarchy.

1. Open the required Territory.
2. Select a **Territory Manager** for reference when appropriate.
3. In **Territory Targets**, select **Add row**.
4. Enter the Item Group, Fiscal Year, quantity or amount, and Target Distribution.
5. Use the highlighted pencil icon to open the child row when needed.
6. Save.

![Territory manager and target allocation](https://novacompanies.m.frappe.cloud/files/territory-target108e8f.png)

The Territory Manager link is for reference. Territory target variance is driven by the transaction's Territory, not by treating the manager as the Sales Person in a Sales Person variance report.

For accurate Territory reporting:

- Assign the correct Territory to each [Customer](/erpnext/customer).
- Confirm that sales transactions carry the expected Territory.
- Use leaf territories for customer transactions where required by your hierarchy.
- Review the report's company, date, and Item Group filters.

Open **Territory Target Variance Item Group-wise** to compare planned and actual sales for the territory.

## Choose the right target level


| Goal                                     | Recommended target                                        |
| ---------------------------------------- | --------------------------------------------------------- |
| Measure an individual's performance      | Sales Person target                                       |
| Measure a team through hierarchy roll-up | Sales Person targets under a group                        |
| Measure a geographic or market area      | Territory target                                          |
| Measure a company-wide goal              | [Company Sales Goal](/erpnext/setting-company-sales-goal) |
| Spread an annual plan across months      | Monthly Distribution                                      |


## Troubleshooting

### The variance report shows no actual sales

Confirm that the Sales Orders are submitted, fall inside the report period, and contain the Sales Person in the Sales Team table. Also verify company and Fiscal Year filters.

### The target does not appear for a month

Check that the target Fiscal Year matches the report and that the linked Monthly Distribution contains a valid percentage for that month.

### Territory actuals are missing

Verify the Customer and transaction Territory. The Territory Manager alone does not assign sales to a territory report.

### Actual value is lower than expected

Review contribution percentages when several Sales Persons share a transaction. Also confirm which document type and status the report uses in your ERPNext version.

### The annual target is distributed incorrectly

Open the Monthly Distribution and confirm that all monthly percentages total 100%. Check that the intended distribution is selected on the target row.

## Frequently asked questions

### Can I set only an amount target?

Yes. Quantity and amount targets can be used independently or together.

### Can one Sales Person have targets for several Item Groups?

Yes. Add one row for each Item Group and Fiscal Year combination that you need to track.

### Can I use a different monthly distribution for each target row?

Yes. Each target row can link to its own Monthly Distribution.

### Does a Territory Manager automatically receive Sales Person credit?

No. Add the Sales Person to the transaction's Sales Team table when individual credit is required.

### Do draft Sales Orders count as actual performance?

No for the Sales Order target variance workflow described here. Submit the order after approval so it can qualify for actual performance.

## Related topics

- [Sales Person](/erpnext/sales-person)
- [Territory](/erpnext/territory)
- [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions)
