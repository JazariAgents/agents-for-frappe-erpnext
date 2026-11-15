<!-- Frappe documentation: erpnext, part 19 of 69. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Customer-specific receivable account with the native modal overlay visible]



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



[Screenshot on the live page: Deferred accounting settings]


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



[Screenshot on the live page: Enable deferred accounting on the Item]

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



[Screenshot on the live page: Enable deferred expense on the Item]

The current Item form identifies the Item as eligible. The actual deferred asset account and service dates are confirmed on each Purchase Invoice Item row.

## Create the Purchase Invoice

Create a Purchase Invoice for the Supplier and add the deferred-expense Item. Confirm the Company, Supplier bill number and date, posting date, currency, rate, taxes, and Cost Center.

In **Items**, select the pencil icon to open the full row editor.



[Screenshot on the live page: Open the Purchase Invoice Item row]

Expand **Deferred Expense** and complete:


| Field                    | What it means                                          |
| ------------------------ | ------------------------------------------------------ |
| Enable Deferred Expense  | Applies deferred treatment to this invoice row         |
| Deferred Expense Account | Asset account holding the unconsumed cost              |
| Service Start Date       | First date on which the purchased service is consumed  |
| Service End Date         | Final date of the service period                       |
| Service Stop Date        | Optional earlier stop date when the service ends early |
| Expense Head             | Final account that receives recognized expense         |


[Screenshot on the live page: Deferred expense account and service period]

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

<!-- page: erpnext/erpnext__deferred-revenue.md -->
---
title: "Deferred Revenue | ERPNext Documentation"
description: "Configure ERPNext deferred revenue for prepaid services, invoice the customer, recognize income over time, and verify the ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-revenue"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, pays $1,200 upfront for a one-year warranty program. The invoice is raised today, but Nova Industries earns the revenue month by month as it provides the service.



Deferred Revenue keeps the unearned portion out of current income. ERPNext first posts the invoice amount to a liability account, then recognizes the appropriate share as income over the service period.



Use deferred revenue when a customer pays or is invoiced before your company has completed the related service, such as annual support, maintenance contracts, subscriptions, or prepaid service plans.



## Understand the accounting effect

Assume the invoice has no tax for simplicity.


| Event                           | Debit                      | Credit                            |
| ------------------------------- | -------------------------- | --------------------------------- |
| Submit the $1,200 Sales Invoice | Debtors $1,200             | Deferred Revenue liability $1,200 |
| Recognize one eligible period   | Deferred Revenue liability | Service Income                    |
| Receive the Customer payment    | Bank $1,200                | Debtors $1,200                    |


A [Payment Entry](/erpnext/payment-entry) clears the receivable. It does not determine when the income is earned. Recognition is controlled by the deferred settings and service dates.

## Before you begin

Prepare:

- A deferred revenue liability account in the [Chart of Accounts](/erpnext/chart-of-accounts).
- The final Income Account, such as Service Income.
- A service [Item](/erpnext/item).
- The contract or coverage start and end dates.
- A Customer and a valid [Sales Invoice](/erpnext/sales-invoice) setup.
- The applicable [Accounts Settings](/erpnext/accounts-settings) for automatic processing and day- or month-based allocation.

Do not use an ordinary Income Account as the deferred account. The unearned balance belongs on the Balance Sheet until the service is delivered.

## Configure deferred settings

In Accounts Settings, choose whether ERPNext books deferred entries by **Days** or **Months**, whether processing runs automatically, and whether recognition is posted directly or through [Journal Entries](/erpnext/journal-entry).

If $12,000 covers a 12-month service period, **Months** normally recognizes $1,000 for each complete month. With **Days**, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact dates. This original example is retained because it shows why monthly recognition amounts can differ without being wrong.

See [Deferred Accounting](/erpnext/deferred-accounting) for the full setting behavior.

## Enable deferred revenue on the Item

Open the Item used for the service or plan, select the **Accounting** tab, and enable **Deferred Revenue**. Enter a standard number of revenue months when it is useful for the Item.



[Screenshot on the live page: Enable deferred revenue on the service Item]

Current ERPNext keeps the deferred account and actual service dates on the Sales Invoice Item row. The Item option identifies that the line is eligible for deferred treatment.

## Create the Sales Invoice

Create a Sales Invoice for the Customer and add the deferred-revenue Item. Confirm the Company, posting date, currency, rate, taxes, and Cost Center as you would for any invoice.

In the Items table, select the pencil icon to open the complete row editor.



[Screenshot on the live page: Open the Sales Invoice Item row]

Expand **Deferred Revenue** and complete:


| Field                    | What it means                                                             |
| ------------------------ | ------------------------------------------------------------------------- |
| Enable Deferred Revenue  | Applies deferred treatment to this invoice row                            |
| Deferred Revenue Account | Liability account holding the unearned balance                            |
| Service Start Date       | First date on which the service is provided                               |
| Service End Date         | Final date of the service period                                          |
| Service Stop Date        | Optional earlier stop date when service ends before the original end date |
| Income Account           | Final account that receives recognized revenue                            |


[Screenshot on the live page: Deferred revenue account and service dates]

The screenshot uses **Customer Advances - NET** as the deferred liability and **Service - NET** as the final income account. Use dedicated accounts if that gives your company clearer reporting.

Submit the invoice only after verifying every deferred row. One invoice can contain several rows with different service periods.

## What happens on submission

ERPNext creates the normal Customer receivable, but credits the deferred liability instead of immediately crediting the Income Account for the eligible row. This keeps unearned revenue out of the Profit and Loss Statement.

If tax is present, tax accounting follows the configured tax rules. Deferred revenue controls the eligible Item's net income recognition; it does not automatically defer every tax or charge on the invoice.

## Recognize the revenue

When automatic processing is enabled, ERPNext processes eligible schedules through a background job. Otherwise, create a [Process Deferred Accounting](/erpnext/process-deferred-accounting) document with **Type = Income**.

For each eligible period, the recognition entry debits the deferred revenue account and credits the Sales Invoice row's Income Account. When posting through Journal Entry is enabled, ERPNext creates Journal Entry documents. They either remain Draft for review or are submitted automatically, depending on Accounts Settings.

The original page described monthly Journal Entries. That remains valid when Journal Entry posting is enabled. With direct posting, the same accounting effect appears in the General Ledger without a separate Journal Entry document.

## Verify recognized and pending revenue

Run the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report). Check the invoice, service period, invoiced amount, recognized amount, and pending balance.

Then review the [General Ledger](/erpnext/general-ledger):

- The deferred liability should begin with the invoice amount.
- Each recognition period should reduce that liability.
- The same amount should increase the Income Account.
- After the complete service term, the eligible deferred balance should be fully recognized, subject to rounding or approved changes.

Also verify the Customer receivable separately. The invoice can be unpaid, partially paid, or fully paid while revenue recognition continues according to the service period.

## Stop, cancel, or amend the service

If a service ends early, record the supported **Service Stop Date** and follow your version's processing behavior. Check the deferred report after the next run.

If the invoice itself is wrong, use the normal cancellation and amendment process. Do not manually delete recognition ledger entries. A credit note, cancellation, or amended invoice may need corresponding deferred processing and verification.

## Video

<iframe src="https://www.youtube.com/embed/j6mx-EHU4aY" title="Deferred Revenue in ERPNext" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0"></iframe>

## Troubleshooting


| Problem                                              | What to check                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Full amount appears in income immediately            | Confirm the row has Enable Deferred Revenue, a deferred liability account, and valid service dates |
| No recognition entry appears                         | Check automatic processing, the date range, background jobs, and Draft generated Journal Entries   |
| Monthly amounts are unequal                          | Check whether Accounts Settings uses Days rather than Months                                       |
| Deferred report has a pending balance after the term | Check the processing end date, stop date, invoice status, and unsubmitted Journal Entries          |
| Income posts to the wrong account                    | Review the Income Account on the Sales Invoice Item row                                            |


## FAQs

### Is deferred revenue the same as a Customer advance?

No, a Customer advance is money received before allocation to an invoice. Deferred revenue is an invoiced amount that has not yet been earned. The example account name may include “Customer Advances,” but the underlying concepts and workflows remain different.

### Can revenue be recognized before the Customer pays?

Yes, payment status and revenue recognition are separate. ERPNext follows the service period for recognition and the invoice allocation for receivables.

### Can different invoice lines use different service periods?

Yes, configure deferred revenue and dates on each Item row.

### Why are recognition Journal Entries Draft?

Journal Entry posting is enabled while automatic submission is disabled. Review and submit the generated entries before expecting them in the General Ledger.

### Does deferred revenue defer tax too?

Not automatically. Taxes follow their configured tax and accounting rules. Confirm the required jurisdictional treatment with your accountant.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Sales Invoice](/erpnext/sales-invoice)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__delete-entries-linked-with-gl-entries.md -->
---
title: "Delete entries linked with GL entries"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-entries-linked-with-gl-entries"
updated: "2026-08-14"
---

ERPNext prevents Nova Industries from deleting a cancelled invoice because its accounting and stock ledger rows form part of the audit trail. Deleting a transaction is different from cancelling it, and should be rare. First decide whether you only need to reverse the business effect, which cancellation already does.

## Before enabling deletion

- Confirm the document is cancelled and no statutory or audit rule requires it to remain.
- Take a backup and test in a non-production environment.
- Understand that deleting ledger rows reduces traceability and may allow the naming series number to be reused depending on configuration.

## Enable the setting

1. Open **Accounts Settings**.
2. Find **Delete Accounting and Stock Ledger Entries on deletion of Transaction**.
3. Enable it, save, and reload.
4. Delete only the intended cancelled document.
5. Disable the setting again if it was approved for a one-time cleanup.

[Screenshot on the live page: Accounts Settings option for deleting linked accounting and stock ledger entries]



## Troubleshooting

### The document is still linked

Open the document’s links and identify dependent records, allocations, returns, or amendments. Remove or resolve dependencies in the correct business order. Do not delete database rows directly.

## Frequently asked questions

### Should I delete an incorrect submitted invoice?

Normally cancel and amend it. That preserves the original document, its reversal, and the correction for audit.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__delete-submitted-document.md -->
---
title: "Delete Submitted Document"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-submitted-document"
updated: "2026-03-04"
---

To delete a submitted document, you need to cancel it first. Following are the steps to delete a submitted document.

These steps assume that you have the appropriate permissions on the document that you wish to cancel and delete.

#### Step 1: Cancel Submitted Document

You will find the 'Cancel' button on upper right corner of submitted document.

[Screenshot on the live page: Screenshot 2023-12-27 at 12.24.48 PM]  


#### Step 2: Delete the document

On cancellation of the submitted document, the 'Amend' button becomes visible with the document status set to 'Cancelled'. This means that the document has been cancelled successfully.

To delete the document, now click on Menu, then Delete. This will delete the selected document.

[Screenshot on the live page: Screenshot 2023-12-27 at 12.39.59 PM]  


**Note:** To delete multiple submitted documents in one go, you can select them in the list view and proceed to cancel and delete.

[Screenshot on the live page: Screenshot 2023-12-27 at 12.34.25 PM]  


If your document is linked with other documents, then you will need to cancel dependent document before trying to delete the parent document.

[Screenshot on the live page: Screenshot 2023-12-27 at 12.37.51 PM]  


All deleted documents disappear from the respective DocType but can be seen in 'Deleted Documents'. They can either be deleted permanently or restored.

[Screenshot on the live page: Screenshot 2023-12-27 at 12.53.50 PM]  


The restored documents are indicated in Deleted Documents.

[Screenshot on the live page: Screenshot 2024-08-26 at 4.53.00 PM]  


  

<!-- page: erpnext/erpnext__delete_company_transactions.md -->
---
title: "Delete Company Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete_company_transactions"
updated: "2026-03-12"
---

ERPNext allows you to delete all the transactions like Sales Invoices, Sales Order, Payment Entries etc associated with a company, while keeping the master data intact.



Often, users setup all the master data and then create a few dummy records to test/explore the system. Then, they want to delete the dummy records and start over again.

### Transaction Deletion Record

---

This feature allows you to delete all the records associated with a specified company, except for the ones belonging to the DocTypes listed in the **Excluded DocTypes** table.

If you really want to wipe out the transactions, then follow these steps. However, the deleted transactions can't be restored.

1. Create a new "Transaction Deletion Record" document.
2. Enter the name of the Company whose records you wish to delete.
3. Modify the "Excluded DocTypes" table if needed.
4. Save and Submit.

[Screenshot on the live page]

The **Summary** table displays the names of the DocTypes whose records were deleted as well as the number of records that were deleted.



## Delete Transactions

---

1. Go to **Home > Accounting > Company** and find your company.
2. On the top right, you'll find the **Delete Transactions** button under **Manage**.
3. Enter your password.
4. Enter the company name to confirm.

[Screenshot on the live page]

This will submit a record in the Transaction Deletion Record DocType.

:::note
To perform this action, the user must have the role of System Manager.
:::
