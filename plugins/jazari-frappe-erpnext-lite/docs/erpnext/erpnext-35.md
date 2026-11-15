<!-- Frappe documentation: erpnext, part 35 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__loyalty-program.md -->
---
title: "Configure Customer Loyalty Programs | ERPNext Documentation"
description: "Set up ERPNext Loyalty Program tiers, earning and redemption factors, customer enrollment, point expiry, and Sales Invoice redemption."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/loyalty-program"
updated: "2026-07-25"
---

A Loyalty Program awards points from submitted sales and lets eligible Customers redeem those points on later [Sales Invoices](/erpnext/sales-invoice). Programs can use one tier or several tiers based on a Customer's cumulative eligible spend.

## Before you begin

Confirm:

- Eligible [Customers](/erpnext/customer), Customer Groups, and Territories.
- The Company currency and loyalty expense account.
- A Cost Center for redemption when required.
- A policy for earning, redemption value, expiry, returns, and tier upgrades.

Test point creation and accounting on the demo Company before enrolling Customers.

## Create a Loyalty Program

1. Open the Loyalty Program list and select **Add Loyalty Program**.
2. Enter the Program Name.
3. Select **Single Tier** or **Multiple Tier**.
4. Set From Date and To Date.
5. Restrict the Customer Group and Territory when required.
6. Enable **Auto Opt In** only when all eligible Customers should join automatically.
7. Add the tier rows.
8. Configure redemption and expiry.
9. Save.

[Screenshot on the live page: An ERPNext Loyalty Program with dates, eligibility, and enrollment settings.]

## Configure tiers

[Screenshot on the live page: The Loyalty Program tier table with collection factors and thresholds.]


| Field             | What it means                                           |
| ----------------- | ------------------------------------------------------- |
| Tier Name         | Label assigned when the Customer reaches the threshold  |
| Collection Factor | Eligible amount required to earn one point              |
| Minimum Amount    | Cumulative spend required for the tier                  |
| Auto Opt In       | Enrolls all Customers that match the program conditions |


Example: with a Collection Factor of $100, an eligible $1,000 invoice earns 10 points.

Minimum Amount is evaluated from cumulative eligible sales for the Customer, not only the current invoice.

## Configure redemption

Set:

- **Conversion Factor** for the monetary value of one point.
- **Expense Account** used for the loyalty benefit.
- **Cost Center** where required.
- **Expiry Duration** in days.

Keep earning and redemption factors distinct. A Customer might spend $100 to earn one point while each redeemed point is worth $1.

## Enroll a Customer

If Auto Opt In is disabled:

1. Open the Customer.
2. Select the Loyalty Program.
3. Save.

[Screenshot on the live page: A Customer assigned to the Nova Rewards Loyalty Program.]

## Earn points

Create and submit an eligible Sales Invoice. ERPNext creates a Loyalty Point Entry linked to the Customer and invoice.

Open **Loyalty Point Entry** to audit earned and redeemed points. Returns and cancellations can affect the available balance, so use the ledger rather than a manually maintained total.

## Redeem points

1. Create a Sales Invoice for the enrolled Customer.
2. Add the Items.
3. Open the Loyalty Points section.
4. Enable **Redeem Loyalty Points**.
5. Enter the number of points.
6. Confirm the Redemption Account and Cost Center.
7. Review the invoice total and submit.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## Troubleshooting


| Problem                              | What to check                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| No points are earned                 | Confirm enrollment, program dates, eligibility, submitted invoice, and tier factor |
| Redeem Loyalty Points is unavailable | Confirm that the Customer has a program and available points                       |
| The tier is unexpected               | Review cumulative eligible spend and minimum thresholds                            |
| Points expired earlier than expected | Check Expiry Duration and the Loyalty Point Entry dates                            |
| Redemption accounting is incorrect   | Review the program's Expense Account and Cost Center                               |


## Frequently asked questions

### Can a program have several tiers?

Yes. Use Multiple Tier and add each threshold in ascending order.

### Are points awarded on draft invoices?

No. The earning workflow depends on submitted eligible invoices.

### Can every Customer be enrolled automatically?

Yes. Enable Auto Opt In and define the eligible Customer Group and Territory.

### Where can I audit a Customer's points?

Use Loyalty Point Entry and the Customer's linked records.

## Related topics

- [Customer](/erpnext/customer)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Applying a Discount](/erpnext/applying-discount)
- [Point of Sale](/erpnext/point-of-sale)

<!-- page: erpnext/erpnext__maintain-stock-field-frozen-in-item-master.md -->
---
title: "Maintain Stock field Frozen in the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintain-stock-field-frozen-in-item-master"
updated: "2026-02-26"
---


In the item master, you might witness values in the following fields to be frozen.

1. Maintain Stock
1. Has Batch No.
1. Has Serial No.

[Screenshot on the live page: Item Field Frozen]

For an item, once stock ledger entry is created, values in these fields will be frozen. This is to prevent user from changing the value which can lead to mis-match of actual stock, and stock level in the system of an item.

For the serialized item, since its stock level is calculated based on the count of available Serial Nos., setting Item as non-serialized mid-way will break the sync, and item's stock level shown in the report will not be accurate, hence Has Serial No. field is frozen.

To make these fields editable once again, you should delete all the stock transactions made for this item. For the Serialized and Batch Item, you should also delete Serial No. and Batch No. record for this item.

<!-- page: erpnext/erpnext__maintaining-suppliers-part-no-in-item.md -->
---
title: "Maintaining Supplier's Item Code In the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintaining-suppliers-part-no-in-item"
updated: "2026-03-02"
---


For each item, code assigned might differ from the code your supplier has given to that same item. ERPNext allows you to track Supplier's Item Code in the item master. Also you can fetch Supplier's Item Code in your purchase transactions, so that they can easily recognize item referring to their Item Code.

#### 1. Updating Supplier Item Code In Item

In the Item master, under Supplier Details section, enter Item Code as given by the Supplier to this item.

[Screenshot on the live page: Supplier Item Code]

#### 2. Supplier's Item Code In Transactions

Each purchase transaction has field in the Item table where Supplier's Item Code is fetched. This field is hidden in form as well as in the Standard print format. You can make it visible by changing property for this field from [Customize Form.](/erpnext/customize-form.html)

Go to print view, click on Menu > customize, enter a new print format name, look for the Items table, click on the **Select columns** button in it. You'll see the following screen. Now select the "Supplier Part Number" checkbox.

[Screenshot on the live page: Supplier item part print format]

Supplier Item Code will only be fetched in the purchase transaction, if both Supplier and Item Code selected in purchase transaction is mapped with value mentioned in the Item master.

[Screenshot on the live page: Supplier Item Code in transaction]

<!-- page: erpnext/erpnext__maintenance-sales-orders.md -->
---
title: "Maintenance Sales Orders | ERPNext Documentation"
description: "Learn how to create Maintenance Sales Orders in ERPNext for service visits, maintenance schedules, recurring support, and follow-up activities."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-sales-orders"
updated: "2026-07-23"
---

# Maintenance Sales Orders

A Maintenance Sales Order records an agreed maintenance service for a Customer. It uses the Sales Order workflow while enabling maintenance-related actions and allowing service invoicing without a stock delivery.

## Before you begin

Create the [Customer](/erpnext/customer), service [Item](/erpnext/item), and required serial-number or installation details. Confirm access to the maintenance documents used by your process.

## Create a Maintenance Sales Order

1. Open **Sales Order** and select **Add Sales Order**.
2. Select the Company and Customer.
3. Set **Order Type** to **Maintenance**.
4. Add the maintenance Item, quantity, rate, and service date.
5. Enable **Skip Delivery Note** when no stock delivery is needed.
6. Review taxes, payment terms, addresses, and terms.
7. Save and submit the order.

[Screenshot on the live page: A full-screen Maintenance Sales Order showing the Skip Delivery Note checkbox beside Order Type.]

Leave **Skip Delivery Note** disabled when the order includes goods that must be delivered through a [Delivery Note](/erpnext/delivery-note).

## Create maintenance documents

After submission, use the available **Create** actions. Depending on installed features and document state, these can include:

- a **Maintenance Schedule** to plan recurring service;
- a **Maintenance Visit** to record work performed;
- a **Sales Invoice** to bill the Customer.

Review generated documents and confirm the Customer, Items, dates, assigned personnel, serial numbers, and service details.

## Troubleshooting

### Skip Delivery Note is not visible

Confirm that **Order Type** is **Maintenance**. The checkbox is conditional.

### Maintenance actions are missing

Confirm that the order is submitted, required features are configured, and your role can create the target document.

## Frequently asked questions

### Can a Maintenance Sales Order include parts?

Yes, but use the delivery workflow for stock Items that physically leave your Warehouse.

### Is a Maintenance Schedule mandatory?

No. Use it when service must occur on planned dates. A one-time service may use only the documents required by your process.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Maintenance Schedule](/erpnext/maintenance-schedule)
- [Maintenance Visit](/erpnext/maintenance-visit)

<!-- page: erpnext/erpnext__maintenance-schedule.md -->
---
title: "Maintenance Schedule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-schedule"
updated: "2026-02-28"
---


**The Maintenance Schedule shows all upcoming Maintenance Visits.**

All machines require regular maintenance, especially those that contain a lot
of moving parts, so if you are in the business of maintaining those or have
some of them in your own premises, this is a useful tool to plan a calendar of
activities for its maintenance.

To create a new Maintenance Schedule go to:

> Home > Support > Maintenance > Maintenance Schedule

A Maintenance Schedule is usually created from a Sales Order of type 'Maintenance'.

[Screenshot on the live page: SO Maintenance Schedule]

## 1. Prerequisites
* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

## 2. How to Create a Maintenance Schedule
1. Go to the Maintenance Schedule, click on New.
1. Select the Customer and the Items for which maintenance needs to be done.
1. Set the start and end dates.
1. Select a Periodicity to set how frequently the visits will happen. The options are "Weekly", "Monthly", "Quarterly", "Half Yearly", "Yearly" and "Random". Maintenance Schedule will get generated based on selected Periodicity. Selecting Random will generate random dates
1. The Number of Visits will be set as per the Periodicity selected. Eg: If you selected Weekly and set the whole month between the start and dates, 4 visits are ideal.
1. Select the Sales Person performing the visits.
1. Save.
1. After saving, click on the **Generate Schedule** button to generate a Maintenance Schedule.
1. Submit.

 [Screenshot on the live page: Maintenance Schedule]

The **Generate Schedule** button will generate a separate row for each maintenance activity. Each Item in a Maintenance Schedule is allocated to a Sales Person.

When the document is Submitted Calendar events are created for the Sales Person User for each maintenance.

## 3. Related Topics
1. [Serial Number](/erpnext/serial-no)
1. [Warranty Claim](/erpnext/warranty-claim)
1. [Maintenance Visit](/erpnext/maintenance-visit)
1. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance-visit.md -->
---
title: "Maintenance Visit"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-visit"
updated: "2026-03-02"
---

**A Maintenance Visit is a visit made by an engineer to a Customer’s premise for maintenance work of an Item.**

To access the Maintenance Visit list, go to:


> Home > Support > Maintenance > Maintenance Visit
> 
> 

A Maintenance Visit is usually created from a Sales Order of type 'Maintenance'. [Screenshot on the live page: SO Maintenance Visit]  


1. Prerequisites
----------------

* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

2. How to create a Maintenance Visit
------------------------------------

1. Go to the Maintenance Visit list, click on New.
2. The current date and time will be recorded, this can be edited.
3. Select the Customer.
4. Select the Maintenance Type whether Scheduled, Unscheduled, or Breakdown.
5. Set the completion status whether 'Partially Completed' or 'Fully Completed'.
6. Select the Item Code and Serial Number.
7. Enter a Description of the maintenance, select the Sales Person performing the maintenance, and enter the work done.
8. Save.

[Screenshot on the live page: Maintenance Visit]

### 2.1 Additional Options when Creating Maintenance Visit

* **Customer Feedback**: You can record any feedback given by the Customer regarding this Maintenance Visit.
* The following fields will be fetched from the [Customer](/erpnext/customer) form:


	+ Customer Address
	+ Contact Person
	+ Territory
	+ Customer Group

3. Related Topics
-----------------

1. [Warranty Claim](/erpnext/warranty-claim)
2. [Maintenance Schedule](/erpnext/maintenance-schedule)
3. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance.md -->
---
title: "Maintenance"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance"
updated: "2026-02-27"
---

The maintenance schedule and maintenance visits are vital parts of the ERPNext support module, ensuring that the ERP system remains operational, secure, and aligned with business needs over time. Efficient management of these aspects contributes to a reliable and optimized ERP environment for users.

* [Maintenance Schedule](/erpnext/user/manual/en/maintenance-schedule)
* [Maintenance Visits](/erpnext/user/manual/en/maintenance-visit)

<!-- page: erpnext/erpnext__make-a-colorful-gantt-chart.md -->
---
title: "Make A Colorful Gantt Chart\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/make-a-colorful-gantt-chart"
updated: "2026-03-02"
---


ERPNext allows users to add colours to certain documents for better visual cues and representation. A good example of this would be the [Event Calendar](/erpnext/how-to-sync-doc-types-with-calendar), where, for each event you can add a colour.

We will be doing so by customizing [Tasks](/erpnext/tasks) under Projects module.

## Steps To Add Colours To The Gantt Chart

1. Go to [Customize Form](/erpnext/customize-form) in the system and select *Task* in _Enter Form Type_ option. Alternatively, you can reach this screen by going to **Menu > Customize** from the Task list or form.

 [Screenshot on the live page: customize-form]

1. Add a new field in the doctype of fieldtype color.
1. Check *In List View* option.

 [Screenshot on the live page: customize-form]

1. Save the form, go back to the Task list, and reload.
1. When opening an existing or new Task, you should see a color field. Pick a color for the Task.

 [Screenshot on the live page: customize-form]

1. Go back to the Task list and switch to Gantt view.

 [Screenshot on the live page: customize-form]

<!-- page: erpnext/erpnext__making-custom-reports.md -->
---
title: "Making Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-custom-reports"
updated: "2026-03-06"
---


There are three kind of reports in ERPNext.

### 1. Report Builder

Report Builder is an in-built report customization tool in ERPNext. This allows you to define specific fields of the form which shall be added in the report. Also you can set required filters, sorting and give preferred name to report.


&lt;iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0"&gt;
&lt;/iframe&gt;



### 2. Query Report

Query Report is written in SQL which pulls values from account's database and displays the same in the report. Though SQL queries can be written from front end, like HTML, it has been restricted for ERPNext cloud users. This is because it allows users with no access to specific report to fetch data directly from the database.

Check Purchase Order Item to be Received report in Stock module for example of a Query report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/query-report) to learn how to create Query Report.

### 3. Script Report

Script Reports are written in Python and stored on server side. These are complex reports which involves logic and calculation. Since these reports are written on server side, customizing it from hosted account is not possible.

Check Financial Analytics report in Accounts module for an example of Script Report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/script-report) to learn how to create Script Report.

&gt; Note: **Dynamic Filter** is available in Script Reports and Query Reports; however, not in the Report Builder.

<!-- page: erpnext/erpnext__making-fields-visible-in-print-format.md -->
---
title: "Customizing Field Visibility in Print Format\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-fields-visible-in-print-format"
updated: "2026-03-02"
---


Each transaction has a Standard Print Format. In the Standard format, only certain fields are displayed by default. If a user wants to display a particular field in the Standard format, it can be customized by using Customize Form tool.

Let's assume in the Sales order, we need to make Shipping Address field visible in the standard print format.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Document Type

As per our scenario, Sales Order will be selected as Document Type.

[Screenshot on the live page: Document Type]

#### Step 3: Disable Print Hide

Click to open field to be made visible in the Standard Print Format. Disable **Print Hide** field.

[Screenshot on the live page: Uncheck Print Hide]

#### Step 4: Update

Update Customize Form to save changed. Reload your ERPNext account, and then check Print Format for confirmation.

<!-- page: erpnext/erpnext__manage-foreign-exchange-difference.md -->
---
title: "Manage Foreign Exchange Difference | ERPNext Documentation"
description: "Record realized foreign-exchange gains or losses in ERPNext when an invoice and its payment use different rates."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manage-foreign-exchange-difference"
updated: "2026-08-14"
---

Because Nova Industries often receives international payments after invoicing, exchange rates can change before settlement.



Nova invoices a customer for EUR 1,200 when `1 EUR = 1.10 USD`, so the receivable is worth USD 1,320. When the customer pays, the rate is 1.15 and the bank receives USD 1,380. The USD 60 difference must be recorded instead of being hidden by changing the payment amount.



The [Payment Entry](/erpnext/payment-entry) settles this realized difference through the configured Exchange Gain/Loss account. This differs from [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation), which measures an unrealized change while a balance remains open. Use this page to record the settlement correctly and keep exchange movement separate from bank fees or write-offs.

## Example

Nova Electronics Distribution issues a EUR 1,200 [Sales Invoice](/erpnext/sales-invoice) when `1 EUR = 1.10 USD`.


| Event                  | EUR   | Rate | USD value |
| ---------------------- | -----: | ----: | ---------: |
| Invoice                | 1,200 | 1.10 | 1,320     |
| Receipt                | 1,200 | 1.15 | 1,380     |
| Realized exchange gain |       |      | 60        |


The Customer has paid the full EUR amount, so its EUR receivable becomes zero. The USD bank receives USD 1,380, while the original receivable carried USD 1,320. The USD 60 difference is a gain.

For a Supplier payment, the debit and credit direction changes. Whether the result is a gain or loss depends on the invoice and payment rates and whether the Company is receiving or paying the foreign currency.

## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup). The foreign Customer or [Supplier](/erpnext/supplier) should use a matching receivable or payable account, and the bank or cash account should have its actual currency.

In the [Company](/erpnext/company-setup), configure **Exchange Gain / Loss Account**. Review **Posting Date inheritance for exchange gain / loss** in [Accounts Settings](/erpnext/accounts-settings), which can use the Invoice, Payment, or Reconciliation Date according to current develop options.



[Screenshot on the live page: Posting-date setting for exchange gain or loss]

Confirm the transaction date and approved rate in [Currency Exchange](/erpnext/currency-exchange), or verify the [provider settings](/erpnext/currency-exchange-settings).

## Create the Payment Entry

The safest route is to create the Payment Entry from the submitted invoice so the reference and outstanding amount are carried forward.

1. Open the submitted Sales Invoice or [Purchase Invoice](/erpnext/purchase-invoice).
2. Select Create &gt; Payment.
3. Confirm Payment Type, Company, Party Type, and Party.
4. Confirm the paid-from and paid-to accounts.
5. Enter the actual amount in each account currency.
6. Enter or verify the payment-date exchange rate.
7. Confirm the invoice in Payment References and its allocated amount.

The currencies are not independent choices on Payment Entry. They come from the selected accounts.



[Screenshot on the live page: EUR receivable and USD bank account currencies]



[Screenshot on the live page: EUR paid amount, USD received amount, and source rate]

## Calculate the exchange difference

When the Payment Entry has a non-zero Difference Amount caused by the rate change, select **Set Exchange Gain/Loss**. ERPNext adds an adjustment row in Payment Deductions or Loss using the configured account. Review the row instead of assuming the label guarantees correct accounting.

The exact sign depends on the workflow. Validate it with the resulting debit and credit rather than forcing a positive or negative amount from memory.

Do not confuse these amounts:


| Difference                                             | Where it belongs                                 |
| ------------------------------------------------------ | ------------------------------------------------ |
| Exchange movement between invoice and payment          | Exchange Gain/Loss account                       |
| Bank fee charged by the bank                           | Bank Charges or another approved expense account |
| Intentional short payment not expected to be collected | Write Off account, subject to policy             |
| Withholding deducted by the Customer                   | Tax withholding workflow and account             |
| Rounding caused by precision                           | Round Off or approved difference handling        |


Several can occur in one payment, but each needs its own row and account. The Payment Entry should end with Difference Amount equal to zero before submission.

Save the Draft and review its preview before submission so finance can verify both account-currency amounts and the balancing Company-currency entry.

## Submit and verify

Submit the Payment Entry, then verify all of the following:

- the invoice outstanding amount is reduced or becomes zero;
- the foreign receivable or payable is cleared by the allocated foreign amount;
- the bank or cash account reflects the actual statement amount;
- the Exchange Gain/Loss account contains only the rate difference;
- the [General Ledger](/erpnext/general-ledger) debit and credit totals balance in Company currency;
- the [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) report agrees with the party statement.

If the payment was entered independently, use [Payment Reconciliation](/erpnext/payment-reconciliation) to allocate it to the invoice. Reconciliation can also generate an exchange difference depending on the account currencies, rates, and posting-date setting.

## Partial and multiple payments

Each payment can use its actual rate. A EUR 1,200 invoice may be settled by EUR 500 at one rate and EUR 700 at another. Each Payment Entry allocates only its portion and realizes the difference for that settlement. Do not change the original invoice rate to match the final bank statement.

When one payment settles multiple invoices, inspect each reference's allocated amount and exchange-rate treatment. Use Payment Entry or the appropriate bulk payment process, then verify that every invoice outstanding balance is correct.

## Advance payments

An advance can be recorded before an invoice exists. Its rate establishes the Company-currency value of the advance. When the advance is later allocated to an invoice, any difference may be recognized according to the reconciliation and posting-date settings. Keep the advance in the correct party account currency and avoid silently changing its historical rate.

## Troubleshooting

### The invoice still has a small outstanding amount after full foreign payment

Check the allocated amount, party account currency, payment rate, and whether the exchange difference was placed in Payment Deductions or Loss. Do not enter exchange differences in Advance Taxes and Charges.

### The bank amount is wrong after adding an adjustment

Separate bank fees, withholding, write-off, and exchange difference. Recalculate the paid and received amounts from the actual bank statement, then use distinct adjustment rows.

### Set Exchange Gain/Loss does not appear

Confirm there is a real currency difference, the Company account is configured, the document is Draft, and the selected accounts and references are correct. Field availability can depend on the Payment Entry state.

### The rate field is read-only

Review [Freeze Exchange Rate](/erpnext/exchange-rate-field-frozen), stale-rate settings, permissions, and the document status. A submitted transaction cannot be casually repriced.

## FAQs

### Should I edit the invoice rate when the bank pays at another rate?

No, keep the invoice rate that represented the invoice date. Use the payment rate and recognize the settlement difference.

### Is an exchange loss always an expense?

It is normally reported through the configured gain or loss account, but presentation depends on your chart and accounting policy. Use accounts approved by finance.

### Can a bank fee be combined with exchange loss?

No, record the bank fee separately so reporting and reconciliation remain clear.

### What if the payment is not linked to the invoice?

Reconcile the unallocated Payment Entry later. The party must match, and the outstanding and unallocated amounts determine what can be allocated.

### Is revaluation required after every payment?

No, a payment realizes its own difference. Revaluation is for eligible balances still open at a reporting date.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Currency Exchange](/erpnext/currency-exchange)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__managing-batch-wise-inventory.md -->
---
title: "Managing Batch wise Inventory\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-batch-wise-inventory"
updated: "2026-02-27"
---


Set of items which has same properties and attributes can be group in a single Batch. For example, pharmaceuticals items are batch, so that it's manufacturing and expiry date can be tracked together.

To maintain batches against an Item you need to mention 'Has Batch No' as yes in the Item Master.

[Screenshot on the live page: Batch Item]

You can create a new Batch from:

`Stock > Documents > Batch > New`

Read [Stock batch](/erpnext/batch.html) to learn more.

For the Batch item, updating Batch No. in the stock transactions (Purchase Receipt &amp; Delivery Note) is mandatory.

#### Purchase Receipt

When creating Purchase Receipt, you should create new Batch, or select one of the existing Batch master. One Batch can be associated with one Batch Item.

[Screenshot on the live page: Batch in Purchase Receipt]

#### Delivery Note

Define Batch in Delivery Note Item table. If Batch item is added under Product Bundle, you can update it's Batch No. in the Packing List table as well.

[Screenshot on the live page: Batch in Delivery Note]

#### Batch-wise Stock Balance Report

To check batch-wise stock balance report, go to:

Stock > Standard Reports > Batch-wise Balance History

[Screenshot on the live page: Batchwise Stock Balance]

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/J0QKl7ABPKM?rel=0">
</iframe>

<!-- page: erpnext/erpnext__managing-fractions-in-uom.md -->
---
title: "Managing Fractions in UOM\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-fractions-in-uom"
updated: "2026-02-26"
---

UoM stands for Unit of Measurement. Few examples of UoM are Numbers (Nos), Kgs, Litre, Meter, Box, Carton etc.

There are few UOMs which cannot have value in decimal places. For example, if we have television for an item, with Nos as its UoM, we cannot have 1.5 Nos. of television, or 3.7 Nos. of computer sets. The value of quantity for these items must be whole number.

You can configure if particular UoM can have value in decimal place or no. By default, value in decimal places will be allowed for all the UOMs. To restrict decimal places or value in fraction for any UoM, you should follow these steps.



### UOM List

For UOM list, go to:

`Stock > Setup > UoM`

From the list of UOM, select UOM for which value in decimal place is to be restricted. Let's assume that UoM is Nos.



### Configure

In the UoOM master, you will find a field called "Must be whole number". Check this field to restrict user from enter value in decimal places in quantity field, for item having this UOM.

[Screenshot on the live page: UoM Must be Whole No]

### Validation

While creating transaction, if you enter value in fraction for item whose UOM has "Must be whole number" checked, you will get error message stating:

`Quantity cannot be a fraction at row #`

[Screenshot on the live page: UoM Validation Message]

<!-- page: erpnext/erpnext__managing-invoice-discount-in-the-payment-entry.md -->
---
title: "Invoice Discount in Payment Entry | ERPNext Documentation"
description: "Record a settlement discount while clearing an ERPNext invoice."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-invoice-discount-in-the-payment-entry"
updated: "2026-08-01"
---

When a Customer pays less because an approved settlement discount applies, allocate the amount received and record the discount in the Deductions or Loss table. This clears the invoice without hiding the difference.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Invoice Discount in Payment Entry

1. Create a Receive Payment Entry and fetch the invoice.
2. Enter the amount received in the bank.
3. Allocate the full amount being settled against the invoice.
4. Add the discount difference with the approved discount account and Cost Center.
5. Confirm that the Difference Amount is zero, then submit.

[Screenshot on the live page: Invoice Discount in Payment Entry in ERPNext]

## Important fields and what they mean


| Field              | What it controls                              |
| ------------------ | --------------------------------------------- |
| Allocated Amount   | Invoice amount cleared by the payment.        |
| Paid Amount        | Cash actually received.                       |
| Deductions or Loss | Accounting rows explaining the shortfall.     |
| Account            | Approved discount allowed account.            |
| Cost Center        | Business unit receiving the discount expense. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The invoice remains outstanding after recording a discount

The cash received plus the approved discount must equal the amount being settled. Allocate the full settlement and post the discount to the configured discount allowed or received account.

### Difference Amount increases when the discount is entered

Check whether the discount should be added or deducted for the Payment Type. Verify the paid amount, received amount, and allocated amount before changing the sign.

### The discount posts to the wrong profit and loss account

Select the correct account for discount allowed or discount received and include the required Cost Center. Do not use a generic write-off account when separate reporting is required.

## Frequently asked questions

### Is a settlement discount the same as changing the invoice price?

It is not the same. The original invoice remains the commercial and tax document; the settlement difference is recorded when payment is received or made.

### Should tax be recalculated when a payment discount is granted?

Tax treatment varies by jurisdiction and discount type. Use the appropriate credit note or regional process when tax must change instead of relying only on a Payment Entry deduction.

### Can only part of an invoice receive a discount?

A partial settlement can include a supported discount, but the remaining invoice balance must be intentional and explainable. Verify the outstanding amount after submission.

### Can discounts allowed and received use different accounts?

Separate accounts are recommended when financial reporting distinguishes customer discounts from supplier discounts.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__managing-multi-level-bom.md -->
---
title: "Managing Multi-level BOM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-multi-level-bom"
updated: "2026-02-26"
---


Consider a scenario where your manufacturing process involves producing sub-assembly items before the final product. In this case, how should you manage the BOM?

First of all, you need to have BOMs for the sub-assemblies, then these BOMs should be linked to the BOM of the final finished product. In the following screenshot, you can see that the BOM for Brush Bristles (subassembly) is linked to the BOM of the Shaving Brush (final product). This is seen in the Materials table in the Bill of Materials master.

[Screenshot on the live page: Multi-level BOM]

The 'Materials' table will only show the sub-assemblies while the 'Materials Required (Exploded)' table will show all the raw materials required to manufacture the final product.

BOM materials table where sub-assembly is shown:
[Screenshot on the live page: Multi-level BOM]

In the exploded view only the raw materials are shown:
[Screenshot on the live page: Multi-level BOM]


To use multi-level BOM in a Work Order, enable the 'Use Multi-Level BOM' checkbox. This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately disable this checkbox.

Let's consider another example to understand this better where a computer is being assembled. The hard disk and DVD drive are also being manufactured and are the sub-assemblies. The multi-level or nested BOM will look like this:

- Personal Computer (FG Item)
 - Mother Board
 - SMTP
 - Accessories and wires
 - Hard Disk (sub-assembly)
 - Item A
 - Item B
 - Item C
 - DVD Drive (sub-assembly)
 - Item X
 - Item Y
 - Item Z


## Caution

Exercise caution when updating the BOM of a sub-assembly. The part which includes the sub assembly with an updated BOM will need to be updated to reference the updated BOM for that part. The practical outcome of this is that changing a screw on a low level assembly will lead to a ripple of updated Bills of Material up through the BOM structure.

Using the example of the personal computer above.
Personal Computer (PC-001 with BOM-PC-001) uses Hard Disk (HDD-001 with BOM-HDD-001).
BOM-HDD-001 includes the three items shown (Item A, B and C).

If we need to exchange Item C for a new item (Item D) then we must update create BOM-HDD-002 (with Items A, B and D). The Hard Disk (HDD-001) is then updated to reference the new BOM-HDD-002. But, BOM-PC-001 is still referencing HDD-001 with BOM-HDD-001. The change from Item C to Item D will not be updated in the Exploded BOM for PC-001.

BOM-PC-002 must be created referencing HDD-001 with BOM-HDD-002 to make this update.
