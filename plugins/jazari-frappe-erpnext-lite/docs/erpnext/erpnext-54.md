<!-- Frappe documentation: erpnext, part 54 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__sales-persons-in-the-sales-transactions.md -->
---
title: "Add Sales Persons to Sales Transactions | ERPNext Documentation"
description: "Assign ERPNext Sales Persons to quotations, orders, deliveries, and invoices, split contribution, and review salesperson transaction reports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-persons-in-the-sales-transactions"
updated: "2026-07-25"
---

Use the **Sales Team** table to attribute a sales transaction to one or more [Sales Persons](/erpnext/sales-person). ERPNext uses each person's Contribution (%) to calculate their contribution to the transaction's Net Total and to populate salesperson reports.

## Before you begin

Create the required:

- [Sales Person hierarchy](/erpnext/sales-person).
- Employees linked to Sales Persons when employee attribution is required.
- [Customer](/erpnext/customer) records and sales transactions.

Decide how your team will allocate shared sales. The total contribution on a transaction must equal 100%.

## Add a default Sales Team to a Customer

1. Open the Customer.
2. Find the **Sales Team** table.
3. Add the Sales Person and Contribution (%).
4. Add additional rows when several people normally share the Customer.
5. Save.

[Screenshot on the live page: A Customer with a default Sales Team allocation.]

ERPNext can carry this allocation into new sales transactions for that Customer. Review it on each document because responsibility may differ for a particular deal.

## Add Sales Persons to a transaction

The Sales Team table is available in supported transactions such as a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), and [Sales Invoice](/erpnext/sales-invoice).

1. Open or create the transaction.
2. Select the Customer and add the Items.
3. Open the **Sales Team** section or tab.
4. Add a Sales Person.
5. Enter Contribution (%).
6. Add other Sales Persons when the sale is shared.
7. Confirm that the total contribution is 100%, then save or submit the transaction.

[Screenshot on the live page: The Sales Team table on a Sales Order with two contributors.]

Select the highlighted pencil icon to open the full child-row editor when you need fields that are not visible in the table.

## Contribution calculation

ERPNext calculates **Contribution to Net Total** from the document's Net Total and each row's Contribution (%).

For a Sales Order with a Net Total of $20,000:


| Sales Person | Contribution | Contribution to Net Total |
| ------------ | ------------ | ------------------------- |
| Morgan Lee   | 60%          | $12,000                   |
| Jordan Bell  | 40%          | $8,000                    |


Taxes and the Grand Total do not replace the Net Total as the contribution basis shown in the Sales Team table.

## Carrying the Sales Team through the sales cycle

When you create a downstream document from an upstream transaction, verify the mapped Sales Team before submitting. The sales cycle can include:

- Quotation to Sales Order.
- Sales Order to Delivery Note.
- Sales Order or Delivery Note to Sales Invoice.

Changes to the Customer's default Sales Team do not retroactively update existing transactions. Likewise, editing an upstream document does not automatically rewrite already-created downstream documents.

## Review salesperson performance

Open **Sales Person-wise Transaction Summary** from Selling reports. Select the Company, date range, Sales Person, and transaction type required by your analysis.

Use [Sales Person Target Allocation](/erpnext/sales-person-target-allocation) and target-variance reports when planned quantity or revenue must be compared with actual sales.

## Sales Person contribution and commission

Contribution attributes transaction value to internal Sales Persons. It does not by itself calculate a payroll incentive.

For internal incentive calculations, see [Calculate Incentive for Sales Team](/erpnext/calculate-incentive-for-sales-team). For an external reseller or referral partner, use a [Sales Partner](/erpnext/sales-partner) and [Sales Partner Commission](/erpnext/how-to-give-commission-to-sales-partner).

## Troubleshooting


| Problem                                     | What to check                                                                                          |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Contribution total validation appears       | Ensure all Sales Team rows total exactly 100%                                                          |
| A Sales Person is missing from the report   | Confirm the person is on the submitted transaction and the report filters include its date and Company |
| The Customer's default team was not fetched | Save the Customer allocation, then select the Customer again on a new transaction                      |
| Downstream documents show the wrong split   | Review the Sales Team before submitting each mapped document                                           |
| Commission is not calculated                | Sales Person contribution is not the same as Sales Partner commission                                  |


## Frequently asked questions

### Can one transaction have several Sales Persons?

Yes. Add one row per person and divide Contribution (%) so the total is 100%.

### Can I change the Sales Team after submission?

Availability depends on the field's after-submit configuration and your permissions. Prefer correcting attribution before submission.

### Does a Sales Person need to be a system user?

No. A Sales Person can be linked to an Employee without being a login user.

### Which amount is used for contribution?

ERPNext displays contribution against the transaction's Net Total.

## Related topics

- [Sales Person](/erpnext/sales-person)
- [Sales Person Target Allocation](/erpnext/sales-person-target-allocation)
- [Calculate Incentive for Sales Team](/erpnext/calculate-incentive-for-sales-team)
- [Sales Partner Commission](/erpnext/how-to-give-commission-to-sales-partner)
- [Sales Reports](/erpnext/sales-reports)

<!-- page: erpnext/erpnext__sales-pipeline.md -->
---
title: "Sales Pipeline | ERPNext Documentation"
description: "Learn how to manage the ERPNext CRM sales pipeline from lead qualification through opportunity tracking, quotation, and conversion."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-pipeline"
updated: "2026-07-23"
---

ERPNext CRM uses a sales pipeline to track potential business from the first enquiry through qualification and conversion. Keeping each record current gives sales teams a shared view of active work, expected revenue, ownership, and next actions.

## Typical pipeline

1. Capture an enquiry as a [Lead](/erpnext/lead).
2. Qualify genuine demand and create an [Opportunity](/erpnext/opportunity).
3. Record follow-ups, communications, and [Appointments](/erpnext/appointment).
4. Prepare a [Quotation](/erpnext/quotation) when the requirement and pricing are clear.
5. Create or select the [Customer](/erpnext/customer), then continue with a [Sales Order](/erpnext/sales-order) when the proposal is accepted.

Not every enquiry must pass through every record. An Opportunity can also be created for an existing Customer.

## Keep the pipeline accurate

- Assign one owner to every active Lead and Opportunity.
- Record the next action and follow-up date after each meaningful interaction.
- Use Sales Stage, probability, expected closing date, and opportunity value consistently.
- Close stale records and capture a meaningful loss reason.
- Review the pipeline regularly instead of relying on outdated forecasts.

## Related topics

- [Sales Stage](/erpnext/sales-stage)
- [CRM Analytics](/erpnext/crm-analytics)
- [CRM Reports](/erpnext/crm-reports)
- [Appointment Booking Settings](/erpnext/appointment-booking-settings)
- [Contract](/erpnext/contract)

<!-- page: erpnext/erpnext__sales-return.md -->
---
title: "Sales Return | ERPNext Documentation"
description: "Learn how to create complete or partial sales returns in ERPNext, receive returned stock, issue Credit Notes, and handle unpaid or paid invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-return"
updated: "2026-07-29"
---

A **Sales Return** records goods returned by a [Customer](/erpnext/customer) after delivery or invoicing. Depending on how the original sale was processed, ERPNext records the return through a return [Delivery Note](/erpnext/delivery-note), a return [Sales Invoice](/erpnext/sales-invoice) (Credit Note), or both.



Use the original submitted transaction as the starting point. This preserves the link to the sale, fetches the original items and rates, and updates returned quantities correctly.

## Before you begin

Confirm:

- the original Delivery Note or Sales Invoice is submitted;
- which [Items](/erpnext/item) and quantities the Customer is returning;
- whether the goods are physically returning to a [Warehouse](/erpnext/warehouse);
- whether the original invoice is unpaid, partially paid, or fully paid;
- whether the return is a refund, a credit for a future invoice, or only a stock correction; and
- the correct serial numbers or batch numbers for tracked Items.

If local law requires a Credit Note, do not cancel the original invoice merely because it is unpaid. Follow your accounting and tax policy.

## Choose the correct return method


| Situation                                                                           | Recommended document                          | Stock effect                                 | Accounting effect                         |
| ----------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------- | ----------------------------------------- |
| Goods were delivered using a Delivery Note, but the sale should not be credited yet | Return Delivery Note                          | Returned stock enters the selected Warehouse | No Customer credit from the Delivery Note |
| Goods and Customer credit must be recorded together                                 | Return Sales Invoice with **Update Stock**    | Returned stock enters the selected Warehouse | Creates a Credit Note                     |
| Goods already returned through a Delivery Note                                      | Return Sales Invoice without **Update Stock** | No second stock movement                     | Creates a Credit Note                     |
| Price, tax, or billing value must be reduced without receiving goods                | Return Sales Invoice without **Update Stock** | No stock movement                            | Creates a Credit Note                     |


Do not return the same stock through both documents. If a return Delivery Note has already received the goods, leave **Update Stock** cleared on the Credit Note.

## Create a return from a Delivery Note

1. Open the original submitted Delivery Note.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
2. Select **Create &gt; Sales Return**.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
3. Review the Customer, return warehouse, posting date, items, and rates fetched from the original document.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
4. Keep only the returned lines. Enter the returned quantity for each Item. ERPNext represents return quantities as negative values.
5. For serialized or batched Items, select the returned [Serial Numbers](/erpnext/serial-number) or [Batch Numbers](/erpnext/batch).
6. Save and submit the return Delivery Note.

For a partial return, reduce the negative quantity to the amount actually received. For example, if the draft fetches `-10` and the Customer returns 3 units, enter `-3`.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

After submission, the stock balance increases in the selected Warehouse. ERPNext also updates the returned quantity against the original Delivery Note and any linked [Sales Order](/erpnext/sales-order). A fully returned Delivery Note can show **Return Issued**.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Create a return from a Sales Invoice

1. Open the original submitted Sales Invoice.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
2. Select **Create &gt; Return / Credit Note**.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
3. Confirm that **Is Return (Credit Note)** and **Return Against** identify the return and its original invoice.
4. Remove lines that are not being returned and enter negative quantities for the returned lines.
5. Enable **Update Stock** only when the goods must be received into stock through this Credit Note.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*
6. When stock is updated, confirm the Warehouse and any required serial or batch information.
7. Review the rates, taxes, posting date, and returned total.
8. Save and submit the Credit Note.

The submitted Credit Note reverses the applicable receivable, income, and tax amounts. When **Update Stock** is enabled, it also receives the returned Items and creates the corresponding stock movement.

## Important fields and what they mean


| Field                                   | What it controls                                                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Is Return (Credit Note)**             | Identifies a Sales Invoice as a return transaction                                                              |
| **Return Against**                      | Links the return to its original Delivery Note or Sales Invoice                                                 |
| **Update Stock**                        | Receives returned goods through a Credit Note; leave it cleared if a return Delivery Note already updated stock |
| **Posting Date and Time**               | Determines when stock and accounting effects are recorded, subject to posting rules                             |
| **Warehouse**                           | Warehouse receiving the returned goods                                                                          |
| **Quantity**                            | Negative quantity being returned; reduce its magnitude for a partial return                                     |
| **Rate**                                | Original selling rate used to calculate the returned value                                                      |
| **Serial and Batch Bundle**             | Identifies the exact serialized or batched stock returning to the Warehouse                                     |
| **Mode of Payment and Payment Account** | Used when the return transaction itself records an immediate payment or refund                                  |


In an Item table, the dot before an Item Code indicates stock availability: green means in stock and red means out of stock.

## Handle unpaid, partially paid, and paid invoices

### The Sales Invoice is unpaid

Create a Credit Note for the returned quantity or value. If the goods are physically returning, either enable **Update Stock** on the Credit Note or create a separate return Delivery Note.

Cancel the original Sales Invoice only when the entire transaction should be reversed, ERPNext permits cancellation, and your statutory and audit rules allow it. Use a Credit Note when the original invoice must remain in the audit trail or only part of the sale is being returned.

### The Sales Invoice is partially or fully paid

Create the Credit Note against the original invoice. The resulting Customer credit can be:

- allocated against another outstanding Sales Invoice;
- retained for a future sale; or
- refunded through an outgoing [Payment Entry](/erpnext/payment-entry), according to your accounting process.

Use [Payment Reconciliation](/erpnext/payment-reconciliation) when invoices, payments, and credits need to be allocated or corrected. Confirm the Customer, references, and allocated amounts before submitting an adjustment.

### The Customer exchanges an Item

Record the returned Item through the appropriate return document. Create a new Sales Invoice or sales transaction for the replacement Item. Allocate the Customer credit against the new invoice when applicable. Keeping the return and replacement as separate linked transactions makes stock and accounting effects easier to audit.

## Stock and accounting impact

A submitted return Delivery Note increases stock and updates returned quantities, but it does not create a Customer credit.

A submitted Credit Note reverses the applicable receivable, income, and tax amounts. If **Update Stock** is enabled, it also increases stock. With [Perpetual Inventory](/erpnext/perpetual-inventory), ERPNext posts the related warehouse accounting entries so the stock ledger and warehouse account remain synchronized.

Use the [Stock Ledger Report](/erpnext/stock-ledger-report) to verify the quantity and valuation movement. Use the [General Ledger](/erpnext/general-ledger) and Accounts Receivable report to verify the Customer credit and accounting entries.

## Status


| Status                 | Meaning                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| **Draft**              | Return has not affected stock or accounts                                                           |
| **Return**             | Document is a submitted return transaction                                                          |
| **Credit Note Issued** | A Credit Note has been created against the original Sales Invoice                                   |
| **Return Issued**      | A return has been created against the original Delivery Note; a full return can produce this status |
| **Cancelled**          | Submitted return was cancelled and its effects were reversed                                        |


## Troubleshooting


| Problem                               | What to check                                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Stock increased twice                 | Check whether both the return Delivery Note and Credit Note updated stock                            |
| Returned quantity is rejected         | Confirm it does not exceed the quantity available to return against the original document            |
| Serial or batch validation fails      | Select serial or batch records from the original delivery and use the correct receiving Warehouse    |
| Customer credit is not available      | Confirm the Credit Note is submitted and review its outstanding amount and payment-ledger references |
| Return posts on the wrong date        | Check posting date, posting time, closed accounting periods, and stock posting restrictions          |
| Original document cannot be cancelled | Use a return document or Credit Note instead of forcing cancellation                                 |


## Frequently asked questions

### Can I return only some items or part of an item quantity?

Y

es. Remove lines that are not being returned and change the negative quantity to the amount actually returned.  
*(screenshot — not bundled; see the live page URL in this file's front matter)*  
*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Should I use a Delivery Note return or a Credit Note?

Use a return Delivery Note for stock movement and a Credit Note for Customer accounting. Use a Credit Note with **Update Stock** when both effects should happen in one document.

### Can I issue a credit without receiving goods?

Y

es. Create a Credit Note and leave **Update Stock** cleared.

### Can a Customer credit be used on a future invoice?

Y

es. Allocate the submitted Credit Note through the appropriate payment or reconciliation workflow.

### Can I refund a paid Customer?

Y

es. Record the Credit Note first, then process and reconcile the outgoing payment according to your accounting policy.

## Related topics

- [Credit Note](/erpnext/credit-note)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Purchase Return](/erpnext/purchase-return)

<!-- page: erpnext/erpnext__sales-taxes-and-charges-template.md -->
---
title: "Sales Taxes and Charges Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales-taxes-and-charges-template"
updated: "2026-08-14"
---

A Sales Taxes and Charges Template is a reusable set of tax and charge rows for selling transactions. It can calculate sales tax, shipping, insurance, handling, duties, or another amount that belongs in the transaction total.



The template is available in Quotations, Sales Orders, Delivery Notes, Sales Invoices, and other supported selling flows. Selecting it copies its rows into the transaction, where ERPNext calculates the actual amounts from the items and quantities.



Use separate templates when the tax jurisdiction, treatment, company, or commercial charge structure differs. A [Tax Rule](/erpnext/tax-rule) can select the correct template automatically from the customer, address, Tax Category, item context, date, and priority.

## Before you begin

Create or identify the ledger accounts that each row should use. A tax liability account should normally have **Account Type** set to **Tax** in the [Chart of Accounts](/erpnext/chart-of-accounts). Charges such as shipping or insurance may use an income or expense account instead, depending on how your organization recognizes them.

Decide whether prices are tax-exclusive or tax-inclusive, whether a charge is fixed or percentage-based, and whether any row depends on a previous row. Write out one numerical example before configuring compound taxes.

Create the required [Tax Category](/erpnext/tax-category) if the template represents a specific treatment. In current ERPNext, only one Sales Taxes and Charges Template can use a particular Tax Category for the same company, so use categories deliberately rather than as labels for several otherwise identical templates.

## Create a Sales Taxes and Charges Template

Go to **Accounting &gt; Taxes &gt; Sales Taxes and Charges Template** and select **Add Sales Taxes and Charges Template**.

1. Enter a clear **Title**, such as `Nova Standard Sales Tax 8%`.
2. Select the **Company**.
3. Select a **Tax Category**, when the template participates in category-based selection.
4. Enable **Default** only when this should be the normal template for new selling transactions for the company.
5. Add a row under **Sales Taxes and Charges**.
6. Use the pencil icon to open the row and configure its calculation, account, rate, and description.
7. Add more rows in the exact order in which they should calculate.
8. Save.

[Screenshot on the live page: Sales tax template title, company, and Tax Category]

The **Disabled** checkbox makes the template unavailable for new selection without removing its historical references.

## Add and edit a tax or charge row

The table shows the calculation type, account, rate, and calculated values. Values such as Net Amount, Amount, and Total are zero on the template because they are calculated only after the rows are copied into a transaction.

Use the pencil icon to open the complete child-table row.



[Screenshot on the live page: Open a Sales Taxes and Charges row]

Select the calculation type, account, and rate. A clear description is useful because it can appear on quotations and invoices.



[Screenshot on the live page: Calculation type, account, and rate]

## Important row fields and what they mean


| Field                               | What it controls                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Type                                | The base used to calculate the row, such as Net Total, a fixed amount, a previous row, or item quantity |
| Account Head                        | The ledger account to which the tax or charge posts                                                     |
| Description                         | The user-facing explanation that can appear in printed transactions                                     |
| Tax Rate                            | The percentage or per-unit amount used by the selected Type                                             |
| Tax Amount                          | The fixed amount used when Type is Actual                                                               |
| Reference Row #                     | The earlier row whose Amount or Total becomes the base for a dependent calculation                      |
| Is this Tax included in Basic Rate? | Back-calculates the net value when the entered item price already includes this tax                     |
| Considered In Paid Amount           | Treats the row as part of the amount already represented by a payment in supported payment flows        |
| Is Tax Withholding Account          | Identifies a row posted to a withholding account when that behavior is applicable                       |
| Cost Center                         | Allocates an income or expense charge to a Cost Center when the selected account requires one           |


[Screenshot on the live page: Description and tax-inclusive pricing option]

Do not select **Is Tax Withholding Account** merely because the row is a normal sales tax. Withholding is a separate deduction workflow. Use [Tax Withholding Category](/erpnext/tax-withholding-category) and the appropriate party or payment configuration.

## Choose the calculation type

ERPNext provides five calculation types:


| Type                   | Calculation                                                  | Common use                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| Actual                 | A fixed amount entered in Tax Amount                         | Fixed shipping or documentation charge                  |
| On Net Total           | Net Total multiplied by Tax Rate                             | A standard percentage tax on the items                  |
| On Previous Row Amount | The Amount of a referenced row multiplied by Tax Rate        | A levy calculated only on another tax amount            |
| On Previous Row Total  | The running Total of a referenced row multiplied by Tax Rate | A charge on the subtotal after an earlier tax or charge |
| On Item Quantity       | Total item quantity multiplied by Tax Rate                   | A fixed amount per unit                                 |


See [Types in Tax Template](/erpnext/types-in-tax-template) for worked calculations and the difference between the two previous-row options.

The Rate for **On Item Quantity** is an amount per unit, not a percentage. For example, a rate of 2 with a total quantity of 5 adds 10 in the transaction currency.

## Configure inclusive tax

Enable **Is this Tax included in Basic Rate?** when the item rate entered by the user already contains the tax. ERPNext works backwards from the tax-inclusive amount to derive the net amount and tax component.

For example, if a displayed item rate of $108 includes 8% tax, ERPNext derives a net amount of $100 and tax of $8. It does not add another $8.64 on top.

The inclusive setting belongs to the Sales Taxes and Charges row. An [Item Tax Template](/erpnext/item-tax-template) can override the rate for an item, but it follows the inclusive or exclusive calculation behavior of the matching transaction tax row. A single matching tax row therefore cannot be inclusive for some items and exclusive for others without a different transaction structure.

## Configure tax on another tax or charge

Place the base row first. On the dependent row, select **On Previous Row Amount** or **On Previous Row Total**, enter the earlier row number in **Reference Row #**, and set the dependent rate.

If row 1 calculates $200 tax and row 2 is 15% **On Previous Row Amount** with Reference Row 1, row 2 is $30. If row 2 is **On Previous Row Total**, its base is the running total after row 1, not only the $200 tax.

Do not reorder compound rows without reviewing their references. ERPNext validates that Reference Row # is used only with a previous-row calculation type.

## Use the template on a transaction

Create a draft [Sales Invoice](/erpnext/sales-invoice), Sales Order, Quotation, or Delivery Note. Select the company, customer, address, Tax Category, and Sales Taxes and Charges Template.

After the rows are copied:

1. Review every Type, account, rate, and description.
2. Confirm any Reference Row # values.
3. Check Net Total, each row Amount, Total Taxes and Charges, and Grand Total.
4. Verify tax-inclusive rows against the item Net Rate.
5. Review the accounting ledger after submitting an invoice.

In the demo transaction, an 8% row calculates $55.92 on a $699 net item value, producing a Grand Total of $754.92.



[Screenshot on the live page: Sales tax total and Grand Total]

Selecting a template copies its current rows to the transaction. Later edits to the master template do not safely substitute for checking existing drafts. Reselect the template or recreate the draft when configuration has materially changed, then verify the result again.

## Apply different rates to individual items

The rate in the Sales Taxes and Charges Template is the standard rate for the matching account. Assign Item Tax Templates when individual products or services require reduced, zero, or otherwise different rates.

The Item Tax Template account must also appear in the transaction tax table. If the account names do not match, the item override cannot calculate against the row. See [Item Tax Template](/erpnext/item-tax-template) for mixed-rate examples and validity rules.

## Regional selection

Regional apps can add fields and automatic selection behavior to a tax template. For example, India localization can provide **Is Inter State** logic so an inter-state template is selected when the place of supply differs from the relevant customer address.

Treat such fields as localization-specific. Follow the documentation for the installed regional app and verify the party tax identifiers, place of supply, billing or shipping address, and transaction type. Do not reproduce another country's template logic in a country-neutral company merely because the field is visible.

## Troubleshooting

### The template is not selected automatically

Check the company, Default flag, Tax Category, matching Tax Rule, party, address, date, and rule priority. A default is company-specific, while a Tax Rule can select a more appropriate template from the transaction context.

### Tax is calculated twice

Check whether an inclusive tax row was configured as exclusive, whether the same charge appears in two rows, and whether a manually entered row duplicates a template row. Compare the item rate, Net Total, tax Amount, and Grand Total.

### An item-specific rate is ignored

Confirm the Item Tax Template assignment, Tax Category, validity date, and matching Account Head. Recheck the item row after changing the transaction category or template.

### A compound row produces an unexpected amount

Confirm whether the intended base is the previous row's Amount or running Total. Check Reference Row # after inserting, deleting, or moving rows.

## Frequently asked questions

### Can I use the template for shipping or insurance instead of tax?

Y

es. Use an appropriate calculation type and income or expense account. Add a Cost Center when the selected account and accounting policy require one.

### Can more than one template be the default?

Keep one clear default for each company and transaction side. Use Tax Rules and Tax Categories for context-specific selection rather than competing defaults.

### Why are Amount and Total zero on the template?

The master stores reusable formulas. ERPNext calculates monetary values only after it copies the rows into a transaction with actual items, quantities, and net values.

### Does changing a template update submitted invoices?

1. Submitted transactions preserve their own rows and accounting history. Update the master for future transactions and amend or correct existing records only through supported accounting workflows.

### Should each tax rate have a separate ledger account?

Use separate accounts when your reporting or statutory posting requires separate components. Item-wise rate overrides can use the same matching tax account when the rates differ but the ledger destination is the same.

## Related topics

- [Taxes](/erpnext/taxes)
- [Types in Tax Template](/erpnext/types-in-tax-template)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Tax Rule](/erpnext/tax-rule)
- [Tax Inclusive Accounting](/erpnext/tax-inclusive-accounting)
- [Apply Tax on Another Tax or Charge](/erpnext/apply-tax-on-another-tax-or-charge)
- [Sales Invoice](/erpnext/sales-invoice)

<!-- page: erpnext/erpnext__sales_funnel.md -->
---
title: "CRM Analytics | ERPNext Documentation"
description: "Use ERPNext CRM Analytics to review the sales funnel, pipeline value, and opportunities by lead source across a selected period."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales_funnel"
updated: "2026-07-23"
---

For example, if you notice that very few communications with the prospects have taken place in a month which may have led to decrease in the sales. You can make sure that the sales executives reach out and follow-up on the leads and opportunities regularly.

### Sales Funnel

By using the sales funnel report, you can quantify the number of prospects at each stage of the process and you can get an idea of your potential customers.

More than this, by looking at the way these numbers change over time, you can identify problems in the sales pipeline and take any corrective action at an early stage.

Select the Company, select the From Date, To Date and select Sales Funnel in Chart.

[Screenshot on the live page: Sales Funnel]

### Sales Pipeline

An opportunity will pass through many sales stages before it yields any business. Using this report you can visualise the total amount of business the opportunities have and compare them across the stages.

Select the Company, select the From Date, To Date and select Sales Pipeline in Chart.

[Screenshot on the live page: Sales Pipeline]

### Opportunities by Lead Source

This report helps you visualise the business potential of opportunities based on the Lead Sources.

Select the Company, select the From Date, To Date and select 'Opportunities by Lead Source' in Chart.

[Screenshot on the live page: Opportunities By Lead Source]

<!-- page: erpnext/erpnext__sales_stage.md -->
---
title: "Sales Stage | ERPNext Documentation"
description: "Configure Sales Stages in ERPNext to track the progress of opportunities through your sales process."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sales_stage"
updated: "2026-07-23"
---

**A Sales Stage indicates the level at which an opportunity is in the sales cycle.**

Generally high values deals go through a number of stages before the sale is concluded. You will have to nurture high value opportunities over a period of time before you can successfully close a sale.

You can create the sales stages and in each opportunity you can select the stage it is in and update it as you nurture the opportunity. This helps you getting an overview of how many opportunities you have in each stage.

To access Sales Stage, go to:

> Home > CRM > Settings > Sales Stage

- How to Create a Sales Stage
- Go to the Sales Stage and select New.
- Enter the Stage Name.

[Screenshot on the live page: Screenshot 2023-12-28 at 11.08.40 AM]

The system allows you to maintain a list of different sales stages.

[Screenshot on the live page: Screenshot 2023-12-28 at 11.08.14 AM]

<!-- page: erpnext/erpnext__salesperson-permissions.md -->
---
title: "Restrict Sales Users to Their Customers and Transactions | ERPNext Documentation"
description: "Learn how to use ERPNext roles and User Permissions so sales users see only assigned Leads, Customers, and transactions linked to those Customers."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/salesperson-permissions"
updated: "2026-07-25"
---

Use [User Permissions](/erpnext/user-permissions) when a sales user should work only with named Leads, Customers, and the sales transactions connected to those Customers. A [Sales Person](/erpnext/sales-person) record is useful for targets, commissions, and the Sales Team table, but assigning a Sales Person does not by itself create record-level access restrictions.

This guide uses Avery Stone as a sales user. Avery can work with Northstar Retail, Summit Digital Stores, and two assigned Leads, but not the rest of the sales portfolio.

## Before you begin

- You need System Manager or equivalent permission to manage Users and User Permissions.
- The user must be a System User with the roles required for their work.
- Create the relevant [Customers](/erpnext/customer) and [Leads](/erpnext/lead) first.
- Decide whether access will be maintained customer by customer or through a grouping master such as [Territory](/erpnext/territory).

> **Roles and User Permissions do different jobs.** A role grants access to a document type. A User Permission limits which records of that type the user can access.

## 1. Give the user the required sales role

1. Open **User** and select the sales user.
2. Open **Roles &amp; Permissions**.
3. Enable **Sales User**.
4. Add another role only when the person needs the corresponding actions. For example, do not assign Sales Manager merely to make the workspace visible.
5. Save the User.

[Screenshot on the live page: Avery Stone User form with the Sales User role highlighted.]

The Sales User role normally provides access to sales masters and transactions according to the configured [Role Permission Manager](/erpnext/permissions). User Permissions added in the following steps narrow that access.

## 2. Open User Permission

Go to **Users and Permissions &gt; User Permission**, then select **Add User Permission**.

[Screenshot on the live page: User Permission list with Add User Permission highlighted.]

You can also open the User and use **Permissions &gt; Set User Permissions**. Both routes create the same User Permission records.

## 3. Allow the Customers assigned to the sales user

Create one User Permission for each Customer in the user's portfolio:

1. In **User**, select the sales user.
2. Set **Allow** to **Customer**.
3. In **For Value**, select an allowed Customer.
4. Save the User Permission.
5. Repeat for each additional Customer.

[Screenshot on the live page: User Permission for Avery Stone allowing access to Northstar Retail, with User, Allow, and For Value highlighted.]

For example, Avery has separate permissions for Northstar Retail and Summit Digital Stores. ERPNext combines permissions for the same master, so Avery can access either Customer.

### Why this also restricts sales transactions

A Customer is linked from documents such as a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), and [Sales Invoice](/erpnext/sales-invoice). When the user's role applies User Permissions, the Customer restriction is carried into those linked documents.

This means you normally do not create separate User Permissions for every Sales Order or Sales Invoice. Maintain the Customer portfolio, and the restriction follows the Customer link.

## 4. Add Lead permissions separately

A Lead is not yet a Customer. A Customer permission therefore cannot decide which unconverted Leads the user may access.

Create a separate User Permission for each assigned Lead:

1. Select the same sales user.
2. Set **Allow** to **Lead**.
3. Select the permitted Lead in **For Value**.
4. Save and repeat for the user's other Leads.

When a Lead is converted, add the resulting Customer to the user's Customer permissions. Review the old Lead permission according to your retention policy.

## 5. Apply the restriction to linked document types

Keep **Apply To All Document Types** enabled when the Customer permission should restrict every supported document containing a Customer link.

[Screenshot on the live page: Apply To All Document Types highlighted on a Customer User Permission.]

Clear this option only when the permission must apply to one specific document type. After clearing it, select that document type in **Applicable For**. For example, limiting a Customer permission to Sales Order would not provide the same restriction across Quotations, Delivery Notes, and Sales Invoices.

## 6. Review the complete portfolio

Open the User Permission list and filter by the user. Confirm that every permitted Customer and every unconverted Lead appears once.

[Screenshot on the live page: User Permission list showing two Customers and two Leads allowed for Avery Stone.]

In this example, Avery can access:

- Northstar Retail and Summit Digital Stores;
- the sales transactions linked to those Customers; and
- Leads CRM-LEAD-2026-00001 and CRM-LEAD-2026-00002.

Avery should not receive a broad Customer, Customer Group, or Territory permission that includes the rest of the portfolio. A broader permission expands access rather than overriding the individual Customer permissions.

## 7. Verify access before handing over the account

Do not assume that a saved permission produces the intended result.

1. Open the User.
2. Select **Permissions &gt; View Permitted Documents**.
3. Check Customer, Lead, Quotation, Sales Order, Delivery Note, and Sales Invoice.
4. Confirm that permitted records appear and an unrelated Customer does not.
5. Test list views and the reports the user will actually use.

[Screenshot on the live page: Permissions menu with View Permitted Documents highlighted on the Avery Stone User form.]

For a final security check, sign in with a non-administrator test user that has the same roles and permissions. System Manager and Administrator accounts can bypass restrictions and are not suitable for validating a salesperson's experience.

## How access is determined


| Configuration                 | What it controls                                                        |
| ----------------------------- | ----------------------------------------------------------------------- |
| Sales User role               | Which sales document types and actions are available                    |
| Customer User Permission      | Which Customers and Customer-linked transactions the user can access    |
| Lead User Permission          | Which specific unconverted Leads the user can access                    |
| Apply To All Document Types   | Whether the allowed value restricts all supported linked document types |
| Applicable For                | Limits one User Permission to a selected document type                  |
| Apply Strict User Permissions | Controls whether records with a blank restricted link remain visible    |


## When there are many Customers

Individual Customer permissions are precise and easy to audit, but they require maintenance when portfolios change. If Customers and Leads are cleanly divided by region, create a User Permission for the appropriate Territory instead. A parent Territory can also include descendants unless **Hide Descendants** is enabled.

Use a grouping master only when it matches the real access boundary. Do not use [Customer Group](/erpnext/customer-group) for access if the group exists mainly for pricing or reporting and contains Customers belonging to several salespeople.

## Records with a blank Customer or Territory

Review **Apply Strict User Permissions** in [System Settings](/erpnext/system-settings). When strict permissions are enabled, a record with a blank restricted link is hidden. When they are not enabled, records whose restricted link is blank may remain visible.

Before enabling this setting, review integrations and older data for missing Customer or Territory values. Test the effect on all teams because it is a system-level setting.

## Troubleshooting


| Problem                                             | What to check                                                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| The user can still see every Customer               | Check for a broader Customer, Customer Group, or Territory permission. Confirm the user's role has Apply User Permissions enabled. |
| The user cannot open any sales transactions         | Confirm the Sales User role grants Read access and that the transaction contains an allowed Customer.                              |
| The user can see unrelated records with blank links | Review missing Customer or Territory values and the Apply Strict User Permissions setting.                                         |
| Assigned Leads are missing                          | Create Lead User Permissions separately. Customer permissions do not cover unconverted Leads.                                      |
| A report shows more data than expected              | Test the report with the restricted user. Review custom or script reports to confirm they apply permission-aware queries.          |
| A manager cannot see a salesperson's portfolio      | Add the required broader permissions to the manager. A Sales Person hierarchy does not automatically replace User Permissions.     |


## Frequently asked questions

### Is linking a User to a Sales Person enough?

Sales Person assignment supports sales attribution, targets, and commission reporting. Use User Permissions for record-level restrictions.

### Must I add every Sales Order to User Permissions?

Allow the Customer and keep Apply To All Document Types enabled. Supported Customer-linked transactions inherit that restriction.

### Can one salesperson have several Customers and Leads?

Y

es. Create one User Permission for each allowed value, or use a suitable Territory when the portfolio follows that hierarchy.

### Can sales managers see all records?

Yes, if their roles and User Permissions grant the broader access. Test managers separately instead of assuming the Sales Person tree controls visibility.

## Related topics

- [User Permissions](/erpnext/user-permissions)
- [Role Based Permissions](/erpnext/permissions)
- [Adding Users](/erpnext/adding-users)
- [Sales Person](/erpnext/sales-person)
- [System Settings](/erpnext/system-settings)
