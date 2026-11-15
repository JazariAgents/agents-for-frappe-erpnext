<!-- Frappe documentation: erpnext, part 19 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__debit-note.md -->
---
title: "Debit Note | ERPNext Documentation"
description: "Create and submit an ERPNext Debit Note to return purchases or reduce a Supplier invoice."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/debit-note"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, delivered phone batteries, but two were damaged and must be returned. Nova Industries needs to reduce what it owes the supplier without changing or deleting the original Purchase Invoice.



A Debit Note records that supplier return or credit as a separate return Purchase Invoice. It reverses the relevant payable, tax, expense, and stock effects while preserving the original transaction.



Use a Debit Note when goods are returned to a supplier, a supplier invoice must be reduced, or a supplier credit must be recorded against an earlier Purchase Invoice.



## Before you begin

You need a submitted [Purchase Invoice](/erpnext/purchase-invoice). Confirm:

- which Items and quantities are being returned;
- whether ERPNext must also reverse stock;
- whether a linked Purchase Receipt exists;
- whether the Supplier has already been paid;
- the posting date on which the return should affect the ledgers.

If you are correcting only the price while keeping the goods, follow [Debit Note for price adjustment](/erpnext/debit-note-for-price-adjustment).

## Create a Debit Note

1. Open the submitted Purchase Invoice that must be reduced.
2. Select **Create &gt; Return / Debit Note**.

![Return or Debit Note action on a submitted Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-05-create-debit-note.png)

3. ERPNext creates a new Purchase Invoice with **Is Return (Debit Note)** selected and **Return Against Purchase Invoice** linked to the original invoice. Verify both fields before changing the Items.

![Debit Note return setting and original Purchase Invoice reference](https://novacompanies.m.frappe.cloud/files/purchase-payables-06-debit-note-reference.png)

4. Keep only the Items being returned. Remove unaffected rows.
5. Enter the return quantity as a negative number. For example, use `-2` to return two units from an original quantity of ten.
6. Select the pencil icon on the Item row to open the full row editor. Verify the returned quantity, original rate, Warehouse, expense account, Cost Center, and source-document references.

![Negative quantity and original rate in the Debit Note Item row](https://novacompanies.m.frappe.cloud/files/purchase-payables-07-debit-note-negative-quantity.png)

7. If the return must move stock out, select **Update Stock** and verify the Warehouse. Leave it clear when stock was already returned through a Purchase Return against the Purchase Receipt.
8. Review taxes and totals. A return should have negative amounts.
9. Save and submit the Debit Note.

## What the Debit Note updates

On submission, ERPNext reduces the Supplier payable and reverses the relevant expense, asset, tax, or receipt-clearing values. When **Update Stock** is selected, it also posts the stock movement out of the selected Warehouse.

The original Purchase Invoice remains submitted. Its outstanding amount is reduced by the Debit Note. This maintains a clear audit trail instead of rewriting the original bill.

If the Supplier invoice was unpaid, the Debit Note reduces the amount to pay. If the Supplier was already paid, the result may be a Supplier credit that can be allocated against another invoice or settled through a payment. Use [Payment Reconciliation](/erpnext/payment-reconciliation) when allocations need correction.

## Important fields and what they mean


| Field                                    | What it controls                                                                                                                                                |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Is Return (Debit Note)                   | Marks the Purchase Invoice as a return and changes amounts to reversal values.                                                                                  |
| Return Against Purchase Invoice          | Links the Debit Note to the original invoice and supports outstanding and document-status updates.                                                              |
| Update Outstanding for Self              | Updates the Debit Note's own outstanding amount even when it references an original invoice. Use the default unless your accounting process requires otherwise. |
| Update Billed Amount in Purchase Order   | Reduces the billed amount on the linked Purchase Order when applicable.                                                                                         |
| Update Billed Amount in Purchase Receipt | Reduces the billed amount on the linked Purchase Receipt when applicable.                                                                                       |
| Update Stock                             | Posts the physical purchase return from the Warehouse through this document.                                                                                    |
| Items                                    | Identifies what is returned. Quantities and amounts are normally negative.                                                                                      |
| Posting Date and Time                    | Determines the accounting and optional stock period for the return.                                                                                             |
| Credit To                                | The Supplier payable account affected by the Debit Note.                                                                                                        |


## Partial returns

You can return selected Items or only part of an Item quantity. Retain the original rate unless the Debit Note is specifically a price adjustment. ERPNext limits the return against the quantities and amounts available on the referenced document.

Example: an invoice contains ten phones at $520 each. If two damaged phones are returned, enter quantity `-2` at rate `$520`. The Debit Note total is `$1,040` before tax, and the original payable is reduced by that amount.

## Submit and next steps

After submission:

- check the original invoice's outstanding amount;
- review the Supplier balance in [Accounts Payable](/erpnext/accounts-payable);
- inspect the General Ledger entries from **View &gt; Accounting Ledger**;
- inspect the Stock Ledger when **Update Stock** was enabled;
- allocate any remaining Supplier credit to a later Purchase Invoice or payment.

## Status


| Status   | Meaning                                                                             |
| -------- | ----------------------------------------------------------------------------------- |
| Draft    | The Debit Note has not affected ledgers.                                            |
| Return   | The return Purchase Invoice is submitted.                                           |
| Unpaid   | The submitted Debit Note has an outstanding credit that is not allocated.           |
| Paid     | The Debit Note has been fully allocated or settled.                                 |
| Canceled | Its accounting and stock effect has been reversed under ERPNext cancellation rules. |


## Troubleshooting

### The return quantity is rejected

Confirm that the quantity is negative, does not exceed the remaining returnable quantity, and references the correct original Item row.

### Stock is reversed twice

Use either a stock-updating Debit Note or a Purchase Return against the Purchase Receipt for the same physical movement. Do not post both for the same returned units.

### The original invoice outstanding amount did not change as expected

Check **Return Against Purchase Invoice**, the update-outstanding option, existing payments, and reconciliations. Then review the Payment Ledger entries for both documents.

### The Supplier was already paid

The Debit Note creates a Supplier credit. Reconcile it against a later invoice or record the appropriate refund payment according to your process.

## Frequently asked questions

### Can I create a Debit Note without an original Purchase Invoice?

ERPNext can support an unlinked return in some configurations, but linking the original invoice gives better quantity validation, outstanding updates, and audit evidence. Prefer the linked workflow.

### Can a Debit Note return only one line?

You can. Remove all unaffected rows and retain only the returned line and quantity.

### Does every Debit Note update stock?

It does not. Stock changes only when the document is configured to update stock. A price-only adjustment should not move stock.

## Related topics

- [Purchase Invoice](/erpnext/purchase-invoice)
- [Debit Note for price adjustment](/erpnext/debit-note-for-price-adjustment)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounts Payable](/erpnext/accounts-payable)

<!-- page: erpnext/erpnext__default-receivable-payable-account.md -->
---
title: "Default Receivable / Payable Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/default-receivable-payable-account"
updated: "2026-08-14"
---

ERPNext normally tracks all customer balances in a shared receivable control account and all supplier balances in a shared payable control account. The party on each invoice and payment provides the customer-level or supplier-level detail, so the Chart of Accounts does not need a separate ledger account for every party.



At Nova Industries, invoices for Northstar Retail, Bluewave Systems, and Cedar Commerce can all post to **Debtors - NI**. The [Accounts Receivable report](/erpnext/accounts-receivable) still shows what each customer owes, while the [General Ledger](/erpnext/general-ledger) keeps one reconcilable control balance.



Use a party-specific receivable or payable account only when there is a real accounting reason, such as a different currency, company, legal classification, or reporting requirement. Creating one account per customer or supplier usually makes the Chart of Accounts longer without improving party-level reporting.

## How the default accounts work

The [Company](/erpnext/company) record supplies the normal receivable and payable accounts. ERPNext uses them when a [Customer](/erpnext/customer) or [Supplier](/erpnext/supplier) does not define a more specific account.




| Transaction      | Control account                                              | Party detail         |
| ---------------- | ------------------------------------------------------------ | -------------------- |
| Sales Invoice    | Default Receivable Account                                   | Customer             |
| Purchase Invoice | Default Payable Account                                      | Supplier             |
| Payment Entry    | The receivable or payable account used by the linked invoice | Customer or Supplier |


When an invoice is submitted, the account balance and the party balance are updated together. This is why the [Accounts Receivable and Payable reports](/erpnext/accounts-receivable-and-payable) can show party-wise outstanding amounts even when many parties share one ledger account.

## Configure the company defaults

1. Open the Company record.
2. Go to the **Accounts** tab.
3. Set **Default Receivable Account** to a ledger account whose account type is **Receivable**.
4. Set **Default Payable Account** to a ledger account whose account type is **Payable**.
5. Save the Company.

The accounts must belong to the same company and must not be group accounts. Create or review them in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Assign a different account to one party

A party-specific account overrides the Company default for that Customer or Supplier.

1. Open the Customer or Supplier.
2. Open the **Accounting** section.
3. Add a row for the Company and select the required receivable or payable account.
4. Save the party.

![Customer-specific receivable account with the native modal overlay visible](/files/customer-default-eur-receivable-native-overlay.webp)



Use this option selectively. For example, Nova Industries may use a USD receivable account for domestic customers and an EUR receivable account for a European customer because the account currency must match the transaction workflow. It should not create separate accounts merely to see customer-wise balances.

## Which account does ERPNext select?

ERPNext first checks whether the party has an account for the selected Company. If it does, that account is used. Otherwise, ERPNext uses the Company default. A value deliberately selected on the transaction can provide a more specific choice when the document permits it.



Before submitting an invoice, confirm the receivable or payable account when the party uses a special currency or reporting treatment. After submission, review the resulting posting through **View Ledger** or the General Ledger report.

## Troubleshooting

### The required account is not available

Confirm that it belongs to the transaction Company, is a ledger account, is enabled, and has the correct Receivable or Payable account type. Also check the account currency.

### An invoice selects an unexpected account

Review the Accounting section of the Customer or Supplier. A party-specific row takes precedence over the Company default. Remove or correct the row if it is no longer required.

### Party balances do not agree with the control account

Compare the Accounts Receivable or Accounts Payable report with the General Ledger using the same Company and posting date. Check opening entries, Journal Entries with a party, cancellations, and reconciliation before posting an adjustment.

## Frequently asked questions

### Do I need a separate receivable account for every customer?

Use the Customer dimension in invoices, payments, the Payment Ledger, and receivable reports to see customer-level balances. A shared control account is the normal setup.

### Can multiple companies share the same receivable account?

Ledger accounts belong to one Company. Configure receivable and payable defaults separately for every Company.

### Can a customer use more than one receivable account?

It can have company-specific accounts, and different account currencies may require separate accounting arrangements. Keep the design limited to genuine accounting needs so reconciliation remains clear.

## Related topics

- [Company accounting defaults](/erpnext/company-accounting-defaults)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__deferred-accounting.md -->
---
title: "Deferred Accounting | ERPNext Documentation"
description: "Understand how ERPNext defers invoice income and expense, recognizes it over a service period, and reports the remaining balance."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-accounting"
updated: "2026-08-03"
---

Deferred accounting separates the date you invoice from the period in which you earn revenue or consume an expense. In ERPNext, a qualifying invoice amount is first posted to a balance-sheet account. ERPNext then moves the appropriate portion to income or expense over the service period.

Use it for annual support contracts, warranties, hosting plans, insurance paid in advance, software subscriptions, rent paid ahead, or another service that covers more than one accounting period. Do not use it merely because an invoice will be paid later. Credit terms change when cash is due; deferred accounting changes when income or expense is recognized.

## How deferred accounting works

The same pattern applies on both sides of the business:


| Flow                                          | At invoice submission                                             | During the service period                 |
| --------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| [Deferred Revenue](/erpnext/deferred-revenue) | Credit a deferred revenue liability instead of the Income Account | Debit deferred revenue and credit income  |
| [Deferred Expense](/erpnext/deferred-expense) | Debit a deferred expense asset instead of the Expense Head        | Credit deferred expense and debit expense |


For example, Nova Electronics Trading invoices $1,200 for a 12-month extended warranty. The invoice creates the Customer receivable, but the $1,200 is initially credited to **Customer Advances - NET**, a liability used for the example. ERPNext then recognizes the amount against **Service - NET** over the warranty period.

On the purchase side, a $1,200 annual software subscription is first debited to **Prepaid Expenses - NET**. ERPNext then recognizes it against **Software Subscription Expenses - NET** as the subscription is consumed.

The exact accounts must match your Chart of Accounts and accounting policy. A deferred revenue account is normally a liability. A deferred expense account is normally an asset.

## Before you begin

Prepare the following:

- A Company with the correct [Chart of Accounts](/erpnext/chart-of-accounts).
- A deferred revenue liability account and/or a deferred expense asset account.
- The final income or expense account that should receive each recognition entry.
- A non-stock [Item](/erpnext/item) representing the service, plan, warranty, or prepaid cost.
- A clear service start date and service end date.
- A decision on whether recognition should be calculated by days or by months.

Review the treatment with your accountant. Deferred accounting controls recognition timing, and the appropriate period may differ from the invoice, payment, contract, or delivery dates.

## Configure deferred accounting

Open **Accounts Settings** and find **Deferred Accounting Settings** under **Invoice and Billing**.



![Deferred accounting settings](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-accounts-settings-deferred-accounting.png)


| Setting                                         | What it controls                                                                                                            |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Book Deferred entries based on                  | Selects **Days** or **Months** as the recognition basis                                                                     |
| Automatically process deferred Accounting entry | Allows the scheduled process to book eligible recognition entries                                                           |
| Book deferred entries via Journal Entry         | Creates [Journal Entry](/erpnext/journal-entry) documents instead of posting the recognition directly to the General Ledger |
| Submit Journal entries                          | Automatically submits generated Journal Entries; if cleared, they remain Draft for review                                   |


### Days or months

With **Days**, ERPNext allocates the amount according to the number of service days falling in each period. This produces different amounts for months of different lengths.

The original example remains useful: if $12,000 covers 12 months, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact service dates. The total across the complete period remains $12,000.

With **Months**, a complete 12-month term normally recognizes $1,000 per month. ERPNext still prorates a partial first or last month when the service does not cover the whole month.

Choose one policy and apply it consistently. Changing the setting affects how future processing calculates eligible schedules.

### Direct ledger entries or Journal Entries

Direct posting creates the recognition entries without a separate Journal Entry document. This is simpler when your team trusts the automated calculation and reviews results through the [General Ledger](/erpnext/general-ledger) and deferred report.

Journal Entry posting gives each recognition batch a document that can be reviewed. When **Submit Journal entries** is not selected, generated Journal Entries remain Draft and do not affect the ledger until someone submits them. This adds control but also creates an operational review step.

## Enable the Item

Open the service Item and select **Enable Deferred Revenue**, **Enable Deferred Expense**, or both when the same service can be sold and purchased. The optional month counts can supply a standard duration, but the invoice row's service dates determine the actual recognition period.



![Enable deferred accounting on the Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

Enabling an Item does not post anything. The accounting effect begins when a submitted Sales Invoice or Purchase Invoice contains an enabled row with a valid deferred account and service period.

## Complete the invoice row

In a [Sales Invoice](/erpnext/sales-invoice) or [Purchase Invoice](/erpnext/purchase-invoice), add the Item, then select the pencil icon on the Items row. Complete the deferred account and the **Service Start Date** and **Service End Date** in the row editor.

The service period belongs to each row. This allows one invoice to contain items with different recognition periods. Review every deferred row instead of assuming the dates apply to the whole invoice.

## Process recognition entries

When automatic processing is enabled, ERPNext runs deferred accounting through a background process. You can also create and submit a [Process Deferred Accounting](/erpnext/process-deferred-accounting) document manually.

Select **Income** for deferred revenue or **Expense** for deferred expense. Set the posting date and the service date range that should be processed. Optionally select one deferred account to limit the run.

The process evaluates eligible submitted invoices and creates the recognition entries allowed by the selected settings. A Process Deferred Accounting record is also the processing log, so keep it available for audit and troubleshooting.

## Verify the result

After processing, check all three layers:

1. Open the invoice and confirm the deferred account and service dates on each affected row.
2. Review the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report) for invoiced, recognized, and pending amounts.
3. Open the General Ledger for the deferred account and the final income or expense account.

The deferred balance should reduce as recognition is booked. The final income or expense should increase by the same amount. Across the full service term, the total recognized amount should equal the eligible invoice amount, subject to cancellations, returns, credits, and rounding.

## Corrections and changes

Correct a Draft invoice before submission whenever possible. After submission, use the supported cancellation and amendment process rather than editing ledger entries directly. If the service stops early, use the row's **Service Stop Date** where the transaction and version support it, then process and verify the revised schedule.

Do not post a manual balancing Journal Entry merely to make the deferred report look correct. First find whether the cause is a missing account, wrong service date, unsubmitted generated Journal Entry, disabled automatic processing, an excluded processing range, or an amended invoice.

## Troubleshooting


| Problem                                      | What to check                                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| No deferred fields appear on the invoice row | Confirm the Item has the applicable deferred option enabled and reopen the row editor              |
| Full income or expense posts immediately     | Check the row-level enable option, deferred account, and service dates before submission           |
| No monthly entry appears                     | Check automatic processing, background jobs, the processing range, and Draft Journal Entries       |
| Amounts differ by month                      | Confirm whether **Days** is selected; different month lengths produce different allocations        |
| Deferred report and ledger differ            | Check document status, filters, service dates, generated entries, cancellations, and posting dates |


## FAQs

### Is deferred accounting the same as an advance payment?

No, an advance payment records cash received or paid before it is allocated. Deferred accounting controls when invoice income or expense is recognized. A transaction can involve both concepts, but they solve different accounting problems.

### Can I defer only one line on an invoice?

Yes, deferred controls and service dates are stored on each invoice Item row. Other rows can post normally.

### Should I use days or months?

Use the basis required by your accounting policy. Days follows the exact service days in each period. Months produces equal complete-month allocations and prorates partial months.

### Why are generated Journal Entries still Draft?

**Book deferred entries via Journal Entry** is enabled but **Submit Journal entries** is not. Review and submit the generated documents, or change the setting only after approving the control implications.

### Can I change the account or service dates after submission?

Use the supported cancellation, amendment, or service-stop workflow. Directly changing posted accounting data can break the relationship between the invoice, deferred report, and General Ledger.

## Related topics

- [Deferred Revenue](/erpnext/deferred-revenue)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Accounts Settings](/erpnext/accounts-settings)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__deferred-expense.md -->
---
title: "Deferred Expense | ERPNext Documentation"
description: "Configure ERPNext deferred expense for prepaid costs, create the Purchase Invoice, recognize expense over time, and verify the ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-expense"
updated: "2026-08-14"
---

CloudWorks, a software supplier to Nova Industries, invoices $1,200 for a one-year service plan. Nova Industries owes the supplier now, but the benefit belongs to twelve months rather than only the month in which the Purchase Invoice is posted.



Deferred Expense prevents the full amount from distorting the current month. ERPNext first holds the cost in an asset account, then recognizes a share as expense during each service period.



Use deferred expense for supplier costs paid or invoiced in advance, such as annual software, insurance, rent, maintenance, or support contracts.



## Understand the accounting effect

Assume no tax for simplicity.


| Event                              | Debit                         | Credit                 |
| ---------------------------------- | ----------------------------- | ---------------------- |
| Submit the $1,200 Purchase Invoice | Deferred Expense asset $1,200 | Creditors $1,200       |
| Recognize one eligible period      | Software Subscription Expense | Deferred Expense asset |
| Pay the Supplier                   | Creditors $1,200              | Bank $1,200            |


Payment clears the payable. It does not decide when the expense is consumed. The service period controls recognition.

The older documentation stated that the deferred expense account was credited on Purchase Invoice creation. That would reverse the normal prepaid-cost treatment. Current ERPNext and standard accounting use a debit to the deferred asset at invoice submission, followed by credits to that asset as expense is recognized.

## Before you begin

Prepare:

- A deferred expense asset account, normally under Current Assets, in the [Chart of Accounts](/erpnext/chart-of-accounts).
- The final Expense Head that should receive the recognized cost.
- A non-stock service [Item](/erpnext/item).
- The contract or coverage start and end dates.
- A Supplier and valid [Purchase Invoice](/erpnext/purchase-invoice) setup.
- The day- or month-based recognition policy in [Accounts Settings](/erpnext/accounts-settings).

Do not use this workflow for inventory that should be received and valued through Stock. Deferred expense is for a cost consumed over time, not for a stock quantity waiting to be issued.

## Configure deferred settings

In Accounts Settings, choose whether recognition is calculated by **Days** or **Months**, whether processing runs automatically, and whether ERPNext posts directly or creates [Journal Entries](/erpnext/journal-entry).

The original $12,000 example is retained: with **Months**, a complete 12-month period normally recognizes $1,000 per month. With **Days**, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact service dates. Different monthly amounts are expected when the number of service days differs.

See [Deferred Accounting](/erpnext/deferred-accounting) for the complete setting behavior.

## Enable deferred expense on the Item

Open the Item used for the prepaid service. In **Accounting**, enable **Deferred Expense**. Enter a standard number of expense months when it helps prefill the expected duration.



![Enable deferred expense on the Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

The current Item form identifies the Item as eligible. The actual deferred asset account and service dates are confirmed on each Purchase Invoice Item row.

## Create the Purchase Invoice

Create a Purchase Invoice for the Supplier and add the deferred-expense Item. Confirm the Company, Supplier bill number and date, posting date, currency, rate, taxes, and Cost Center.

In **Items**, select the pencil icon to open the full row editor.



![Open the Purchase Invoice Item row](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-item-pencil.png)

Expand **Deferred Expense** and complete:


| Field                    | What it means                                          |
| ------------------------ | ------------------------------------------------------ |
| Enable Deferred Expense  | Applies deferred treatment to this invoice row         |
| Deferred Expense Account | Asset account holding the unconsumed cost              |
| Service Start Date       | First date on which the purchased service is consumed  |
| Service End Date         | Final date of the service period                       |
| Service Stop Date        | Optional earlier stop date when the service ends early |
| Expense Head             | Final account that receives recognized expense         |


![Deferred expense account and service period](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-service-period.png)

The example uses **Prepaid Expenses - NET** and **Software Subscription Expenses - NET**. The service dates cover one year. Submit only after confirming every eligible row.

## What happens on submission

ERPNext creates the Supplier payable, but the eligible row is debited to the deferred expense asset instead of immediately debiting the final Expense Head. This prevents a full annual cost from distorting one month's Profit and Loss Statement.

Taxes and charges follow their own configured accounts and rules. Deferred expense controls the eligible Item amount; it does not automatically defer every tax, freight, or charge on the invoice.

## Recognize the expense

When automatic processing is enabled, ERPNext processes eligible schedules in the background. Otherwise, create a [Process Deferred Accounting](/erpnext/process-deferred-accounting) record with **Type = Expense**.

For each eligible period, recognition debits the Purchase Invoice row's Expense Head and credits the deferred expense asset. If Accounts Settings uses Journal Entry posting, ERPNext creates Journal Entry documents. They may remain Draft for review or be submitted automatically.

The original page described automatic monthly Journal Entries. That remains the visible document flow when Journal Entry posting is selected. With direct posting, the same debit and credit appear in the General Ledger without a separate Journal Entry document.

## Verify recognized and pending expense

Open the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report) and check the Purchase Invoice, service period, invoiced amount, recognized amount, and pending balance.

Then review the [General Ledger](/erpnext/general-ledger):

- The deferred asset should begin with the eligible invoice amount.
- Each recognition period should credit that asset.
- The same amount should debit the final Expense Head.
- At the end of the full service period, the eligible deferred balance should be fully recognized, subject to approved changes and rounding.

Review the Supplier payable separately. The invoice may be unpaid, partially paid, or fully paid while expense recognition continues independently.

## Other examples and boundaries

The earlier documentation listed insurance paid in advance, internet subscriptions, debt-issuance costs, and intangible-asset amortization. Those remain conceptually relevant, but not every long-term cost should be handled through this invoice feature.

Fixed assets should normally use ERPNext [Asset](/erpnext/asset) and depreciation workflows. Capitalized interest, intangible assets, and debt-issuance costs may require specialized accounting and local reporting. Use deferred expense on Purchase Invoice rows only when it matches the applicable accounting policy.

## Stop, cancel, or amend the service

If service ends early, use **Service Stop Date** where supported, then verify the next processing run. If the invoice amount, dates, or account is wrong, use the supported cancellation and amendment flow.

Do not post an unexplained Journal Entry to remove a residual prepaid balance. First check the processing dates, document status, stop date, generated Draft Journal Entries, and whether the final period was included.

## Troubleshooting


| Problem                                  | What to check                                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Full cost appears in expense immediately | Confirm the row's enable option, deferred asset account, and service dates                      |
| No recognition entry appears             | Check automatic processing, the selected date range, background jobs, and Draft Journal Entries |
| Monthly amounts differ                   | Confirm whether recognition is based on Days                                                    |
| Prepaid balance remains after the term   | Check the final processing date, service stop date, invoice status, and unsubmitted entries     |
| Expense posts to the wrong account       | Review the Expense Head on the Purchase Invoice Item row                                        |


## FAQs

### Is a deferred expense the same as an unpaid Supplier invoice?

No, unpaid describes the payable and cash status. Deferred describes when the cost is recognized. A fully paid invoice may still have a deferred expense balance.

### Can only one Purchase Invoice line be deferred?

Yes, deferred options, accounts, and service dates are set on each Item row.

### Should prepaid insurance use deferred expense?

It is a common use case when the policy covers future periods. Confirm the required treatment and recognition basis with your accountant.

### Why are generated Journal Entries not in the ledger?

They remain Draft when automatic submission is disabled. Review and submit them before expecting a General Ledger effect.

### Should fixed-asset depreciation use this feature?

Normally no. Use ERPNext's Asset and depreciation workflow for fixed assets. Deferred expense is better suited to prepaid services and similar costs consumed over a defined period.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Revenue](/erpnext/deferred-revenue)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)
