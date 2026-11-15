<!-- Frappe documentation: erpnext, part 38 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__multi-currency-accounting.md -->
---
title: "Multi Currency Accounting | ERPNext Documentation"
description: "Set up and operate ERPNext accounting for foreign customers, suppliers, bank accounts, invoices, payments, and revaluation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/multi-currency-accounting"
updated: "2026-08-14"
---

Nova Industries manufactures electronics, buys components abroad, and distributes finished products in several currencies.



Nova buys components and sells finished products internationally. A customer may need an invoice in EUR, a supplier may expect payment in JPY, and Nova must still report one consistent set of books in USD. Multi-currency accounting keeps each foreign amount together with its Company-currency value.



For example, Nova invoices EuroTech Retail for EUR 1,200 at `1 EUR = 1.15 USD`. The customer sees EUR 1,200 while ERPNext records USD 1,380 for reporting. This page explains how Company, account, transaction, and pricing currencies work together from setup through payment and revaluation.

## The three currencies to distinguish


| Currency             | What it controls                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Company currency     | The base accounting currency configured on the [Company](/erpnext/company-setup). Financial statements and base debit and credit values use it.              |
| Account currency     | The fixed currency of a ledger in the [Chart of Accounts](/erpnext/chart-of-accounts). A bank, receivable, or payable account should represent one currency. |
| Transaction currency | The currency shown on the invoice, order, or quotation. Its amount is converted to Company currency using the document's Exchange Rate.                      |


A [Price List](/erpnext/price-lists) adds another pricing currency. If it differs from the transaction currency, **Price List Exchange Rate** converts item prices separately from the document's accounting conversion rate.

## Before you begin

Enable the required [Currency](/erpnext/currency) records. Decide whether each Customer and Supplier will normally transact in one foreign currency or several currencies. Agree on the source and approval policy for exchange rates, the realized Exchange Gain/Loss account, the unrealized Exchange Gain/Loss account, and the revaluation frequency.

Do not change an Account's currency after ledger entries exist. Current ERPNext prevents this because old balances would become ambiguous. Create a correctly denominated account instead.

## Set up foreign-currency accounts

Create separate ledgers for each currency that must retain an account-currency balance. Examples include a EUR bank account, EUR receivable account, and EUR payable account.



[Screenshot on the live page: EUR bank account with its fixed account currency]

Each bank or cash account has one currency. If the real bank provides separate USD and EUR balances, represent them with separate ERPNext accounts. This keeps [Bank Reconciliation](/erpnext/bank-reconciliation) and audit trails intelligible.

## Configure Customers and Suppliers

Set a foreign Customer's **Billing Currency**, then add the matching receivable account in the Customer's Default Accounts child table. For a Supplier, use Billing Currency and the Per-Company Accounts table with the matching payable account.



[Screenshot on the live page: Customer billing currency]



[Screenshot on the live page: Open the Customer default-account row]

Select the highlighted pencil to open the full child-row editor.



[Screenshot on the live page: Customer linked to a EUR receivable account]

If a party account is in a foreign currency, the transaction must normally use that currency. If the account is in Company currency, **Allow multi-currency invoices against single party account** can permit invoices in other currencies, but the General Ledger entry remains in the party account's currency. Use that option only after testing invoicing, payment, ageing, and reconciliation behavior for your process.

## Configure exchange-rate behavior

Use [Currency Exchange](/erpnext/currency-exchange) for approved manual rates. If no eligible stored record exists, ERPNext can call the provider configured in [Currency Exchange Settings](/erpnext/currency-exchange-settings). Accounts Settings controls stale records and the posting date inherited by exchange-gain-or-loss entries.

For the demo, the approved rate is `1 EUR = 1.15 USD`.

## Create a foreign-currency Sales Invoice

1. Create a [Sales Invoice](/erpnext/sales-invoice) for the foreign Customer.
2. Confirm the transaction Currency and Exchange Rate.
3. Select a Price List and verify its currency and conversion rate.
4. Confirm that **Debit To** is the intended receivable account.
5. Add items, taxes, terms, and the payment schedule.
6. Compare the transaction and Company-currency totals before submission.

[Screenshot on the live page: EUR Sales Invoice and conversion rates]

The Exchange Rate converts EUR 1,200 to USD 1,380. The Price List Exchange Rate is 1 because both the Price List and invoice use EUR.



[Screenshot on the live page: EUR and USD totals on the Sales Invoice]

On submission, the receivable is maintained in the account currency and base debit and credit values are recorded in USD. The [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) report shows party or account-currency amounts according to its filters.

## Record foreign-currency purchases and payments

A [Purchase Invoice](/erpnext/purchase-invoice) follows the same pattern using the Supplier's payable account and buying rate. Outstanding and advance values follow the party account currency.

In a Payment Entry, currencies come from the selected accounts. Receiving EUR from a EUR receivable into a USD bank produces a paid amount in EUR, a received amount in USD, and a source exchange rate.



[Screenshot on the live page: Currencies of the paid-from and paid-to accounts]



[Screenshot on the live page: Exchange rate and converted amounts in Payment Entry]

When the payment rate differs from the invoice rate, ERPNext can calculate a realized exchange difference. Use **Set Exchange Gain/Loss** where available, then inspect the Payment Deductions or Loss row and make the Difference Amount zero before submitting. Do not put a bank charge into the exchange account merely because it appears on the same bank statement. Bank fees and exchange differences are different expenses.

## Use multi-currency Journal Entries

Select **Multi Currency** on a [Journal Entry](/erpnext/journal-entry) when account rows use different currencies. Enter debit or credit in each account's currency and verify the exchange rate and calculated Company-currency amount. A Journal Entry requires deliberate debit and credit selection, so prefer Payment Entry for normal customer and supplier payments.

## Revalue open foreign balances

Exchange-rate movement after a transaction creates two kinds of difference:


| Difference | When it arises                                       | Typical tool                                                    |
| ---------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| Realized   | An invoice or payable is settled at a different rate | Payment Entry and Exchange Gain/Loss                            |
| Unrealized | A foreign balance remains open at a reporting date   | [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) |


Revaluation changes the Company-currency carrying value. It does not change the foreign amount. For example, EUR 1,000 remains EUR 1,000 while its USD value moves from USD 1,100 to USD 1,150.

## Verify reports

Filter the [General Ledger](/erpnext/general-ledger) by the foreign account to view debit, credit, and balance in account currency. Financial statements remain grounded in Company currency, while the Accounts Receivable and Payable report exposes party and account-currency values.



[Screenshot on the live page: EUR values in the General Ledger]

## Troubleshooting

### The party can be selected but the invoice currency is rejected

Check Billing Currency, the default receivable or payable account, and that account's currency. The transaction currency must be compatible with the party account unless the single-party-account option applies.

### Payment Entry shows the wrong currency

The paid-from and paid-to account currencies determine the amount fields. Select the intended bank, cash, receivable, or payable account instead of trying to type an independent Payment Entry currency.

### The foreign balance is zero but Company currency is not

This can occur after currency movements. Run Exchange Rate Revaluation at the reporting date and inspect the zero-balance treatment introduced for this situation.

## FAQs

### Can one bank account hold several currencies?

One ERPNext Account has one account currency. Use separate ledger accounts for separately maintained bank currency balances.

### Can one Customer receive invoices in several currencies?

It is possible in specific configurations, including the single-party-account setting, but a dedicated receivable account per regularly used currency gives clearer account-currency balances and payment behavior.

### Why is an exchange rate required even if payment will happen later?

ERPNext must record the Company's base-currency value on the invoice date. The payment can use a later rate, with the difference recorded as realized gain or loss.

### Does revaluation change the invoice amount?

No, it adjusts the base-currency carrying value of eligible accounts. The original invoice and foreign-currency amount remain unchanged.

### Can I change an account from USD to EUR after posting entries?

No, create a new EUR account and move future activity to it. Consult your accountant before transferring an existing balance.

## Related topics

- [Multi Currency Setup](/erpnext/multi-currency-setup)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)
- [Currency Exchange](/erpnext/currency-exchange)

<!-- page: erpnext/erpnext__multi-currency-setup.md -->
---
title: "Multi Currency Setup | ERPNext Documentation"
description: "Configure ERPNext for foreign-currency accounts, parties, rates, transactions, payments, and reporting in a reliable order."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/multi-currency-setup"
updated: "2026-08-14"
---

Before Nova Industries begins foreign-currency sales, its accounts, parties, Price Lists, rates, and payment settings must agree.



Nova wants to invoice EuroTech Retail in EUR while reporting its accounts in USD. Enabling EUR alone is not enough. The Customer, receivable account, Price List, rate source, payment account, and gain-or-loss accounts must agree, or the first invoice or payment can fail with a currency mismatch.



This page connects those settings in a safe order. By the end, Nova can create a EUR invoice, receive payment, record any exchange difference, and report the result in USD. Complete the sequence in a test Company before applying it to live Companies.

## Decide the accounting model

Answer these questions before configuring ERPNext:


| Decision                                    | Recommended starting point                                                                    |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| What is the Company's base currency?        | Use the statutory or primary reporting currency. Do not treat it as a per-transaction choice. |
| Which foreign balances must be retained?    | Create a separate account for each currency-specific bank, receivable, or payable balance.    |
| Does each party normally use one currency?  | Set its Billing Currency and matching default account.                                        |
| Are rates market-based or finance-approved? | Use the provider for market rates and Currency Exchange for controlled rates.                 |
| How are closing balances revalued?          | Configure unrealized gain or loss and a review frequency.                                     |


For the concepts behind these choices, read [Multi Currency Accounting](/erpnext/multi-currency-accounting).

## 1. Confirm the Company currency

Open the [Company](/erpnext/company-setup) and verify **Default Currency**. ERPNext uses it for base debit and credit values and Company financial statements. Changing it after transactions exist is a migration decision, not ordinary setup.

## 2. Enable required currencies

Open [Currency](/erpnext/currency), enable EUR, and review its symbol, fraction, and number format. Enabling a currency only makes it selectable. It creates no accounts or rates.



[Screenshot on the live page: EUR formatting and fractional-unit settings]

## 3. Create foreign-currency accounts

In the [Chart of Accounts](/erpnext/chart-of-accounts), create the ledgers that must keep foreign balances. For the example:

- Euro Bank, Account Type Bank, Currency EUR
- Euro Receivables, Account Type Receivable, Currency EUR
- Euro Payables, Account Type Payable, Currency EUR



[Screenshot on the live page: Foreign-currency bank account]

Do this before posting entries. ERPNext does not allow an account's currency to be changed once ledger entries exist. Keep separate accounts for separate bank currencies even when the same institution supplies both balances.

## 4. Configure Customers and Suppliers

On the [Customer](/erpnext/customer), set Billing Currency to EUR. In Default Accounts, link Nova Electronics Distribution to Euro Receivables. Use the pencil in the child row to open the full editor.



[Screenshot on the live page: Billing Currency on the Customer]



[Screenshot on the live page: Customer default EUR account]

Apply the corresponding setup on the Supplier with Euro Payables. A party's billing currency and account currency should agree with the normal invoice currency.

## 5. Create currency-specific prices

Create a EUR [Price List](/erpnext/price-lists) when you maintain contractual or market prices in euros. Add EUR Item Prices. This is independent from the accounting rate. On a transaction:

- Exchange Rate converts the transaction total to Company currency.
- Price List Exchange Rate converts item prices when Price List currency differs from transaction currency.

When both the transaction and Price List use EUR, the Price List Exchange Rate is 1.

## 6. Define the exchange-rate policy

Create [Currency Exchange](/erpnext/currency-exchange) records for approved or historical rates. Configure [Currency Exchange Settings](/erpnext/currency-exchange-settings) for provider fallback. Decide how **Allow Stale Exchange Rates** and **Stale Days** should work in [Accounts Settings](/erpnext/accounts-settings).



[Screenshot on the live page: Approved EUR to USD rate]

Document who may update manual rates, how often rates are reviewed, and whether buying and selling use the same rate. Store both directions when processes request both EUR to USD and USD to EUR.

## 7. Configure gain and loss accounts

In Company accounting defaults, set:


| Field                                 | Purpose                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| Exchange Gain / Loss Account          | Realized differences, commonly when a payment settles an invoice at a different rate. |
| Unrealized Exchange Gain/Loss Account | Reporting-date revaluation of balances that remain open.                              |


[Screenshot on the live page: Company exchange gain and loss accounts]

Use accounts approved by your accountant and local reporting policy. Some organizations separate gain and loss accounts or realized and unrealized presentation further through their chart and reporting design.

## 8. Test the complete cycle

Before importing or entering live data:

1. Create a draft EUR [Sales Invoice](/erpnext/sales-invoice) and verify EUR and USD totals.
2. Confirm Debit To is Euro Receivables.
3. Create a draft EUR [Purchase Invoice](/erpnext/purchase-invoice) and confirm Credit To is Euro Payables.
4. Create a [Payment Entry](/erpnext/payment-entry) using the intended bank account and verify paid, received, and Company-currency amounts.
5. Run the [General Ledger](/erpnext/general-ledger) and [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) reports.
6. Test [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) in Draft for a closing date.

Do not stop at a successfully saved invoice. The payment and reporting tests reveal account-currency mismatches that are easy to miss during setup.

Record the tested document names, expected rates, account balances, and report filters in the implementation checklist. Repeat the test for each regularly used currency and for both receipts and payments. A EUR sales test does not prove that a GBP supplier payment or a foreign bank transfer is configured correctly.

## Setup checklist


| Area     | Verification                                                                                   |
| -------- | ---------------------------------------------------------------------------------------------- |
| Currency | Required codes are enabled and display correctly.                                              |
| Company  | Base currency is correct and stable.                                                           |
| Accounts | Each foreign bank, receivable, and payable account has the intended currency and Account Type. |
| Parties  | Billing Currency and per-Company default account match.                                        |
| Pricing  | Price List currency and item prices match the commercial agreement.                            |
| Rates    | Manual records, provider, direction, date, and buying or selling flags are understood.         |
| Payments | Source and target account currencies produce the intended amounts.                             |
| Closing  | Realized and unrealized gain or loss accounts are configured.                                  |
| Reports  | Finance has verified account-currency and Company-currency views.                              |


## Troubleshooting

### ERPNext prevents changing an Account currency

The Account already has ledger entries. Create a new account with the correct currency and plan the transition with your accountant.

### The Customer defaults to EUR but the invoice uses USD

Check the selected Company, Debit To account, Billing Currency, transaction Currency, and whether the multi-currency-single-party-account setting changes the normal restriction.

### A Payment Entry has unexpected paid and received currencies

Review the paid-from and paid-to accounts. Their account currencies drive those fields.

## FAQs

### Do I need a separate receivable account for every Customer?

No, you can share one EUR receivable account across EUR Customers and use party dimensions in receivable reports. Separate accounts by currency or accounting need, not automatically by Customer.

### Should I enable Allow multi-currency invoices against single party account?

Only when the business genuinely invoices the same party in multiple currencies and has tested payment, outstanding, reconciliation, and reporting behavior. A dedicated account per regular currency is easier to reason about.

### Can the provider replace all manual Currency Exchange records?

It can supply market rates for supported pairs. Manual records remain useful for approved, historical, unsupported, or contract rates.

### Should revaluation be automatic?

Start with a reviewed manual process. Enable automatic creation only after the rate source, accounts, frequency, journal submission policy, and period-close controls are proven.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Currency Exchange](/erpnext/currency-exchange)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__naming-series-as-per-gst-rules.md -->
---
title: "Naming Series as Per GST Rules"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series-as-per-gst-rules"
updated: "2026-07-31"
---

Rule 46 (b) of the CGST **Rules** 2017 specifies that the tax **invoice** issued by a registered person should have a consecutive serial **number**, not exceeding sixteen characters, in one or multiple series, containing alphabets or numerals or special characters – hyphen or dash and slash symbolized as “-” and “/” respectively

  


This validation will come into effect in ERPNext from the new fiscal year i.e FY 2021-22. If you encounter an error similar to one shown in the screenshot below, follow the below steps to resolve the issue and add a new naming series for Sales and Purchase Invoices

  


[Screenshot on the live page]

  


Step 1: Go to "Naming Series" doctype and select transaction as "Sales Invoice"

  


[Screenshot on the live page]

  


Step 2: Add a new naming series having maximum upto 16 characters. For eg INV-.YYYY.-.#####. Add this as the first option and don't check "User must always select" inorder to make this as the defaut naming series

  


[Screenshot on the live page]

  


  

<!-- page: erpnext/erpnext__naming-series-current-value.md -->
---
title: "Set Current Value for Naming Series"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series-current-value"
updated: "2026-03-04"
---


Naming Series feature allows you to define prefix for naming of a documents. For example, if a Sales Order has prefix "SO", then the series will be generated as SO-00001, SO-00002... and so on. Click [here](/erpnext/document-naming-settings) to learn how you can customize Number Series for a transaction/master in ERPNext.

### 1. Setting the Current Value

Naming Series feature also offers a tool where you can set Current Value for specific prefix. This is generally required if you have recently started using ERPNext, and have old transactions in the previous system, and you want the numbering series to start in from where it ended in the old system. Let's consider a scenario to learn this better.

For example, you have 322 Sales Orders created in your old system with SO00322 as highest Sales Order Id. In ERPNext, you need the first Sales Order to pick up #323 when it is saved. To enable this, you should set Current Value for SO series in following steps.

#### Go to Naming Series Tool

`Setup > System > Naming Series`

#### Update Series Section

[Screenshot on the live page: Update Series Section]

#### Select Prefix

Considering our scenario, prefix for Sales Order will be "SO".

[Screenshot on the live page: Series Prefix]

#### Current Value

If you have currently 12 Sales Orders created in your account, then current value updated will be 12. You can edit Current Value to 322, and then click on Update Series Number.

[Screenshot on the live page: Series Current Value]

With this setting, you will have numbering for the New Sales Orders starting with #323.

### 2. Error Due Series Number

If you receive a Duplicate Name error while saving a transaction, for example, while saving Item Price, you receive an error saying:

`Duplicate name Item Price RFD/00016`

This error message indicates that when you are saving Item Price, system is trying to allocate "RFD/00016" to that Item Price record. But it is finding that Item Price with this ID is already existing in your system.

This error could arise because Current Value for Series/Prefix of Item Price is disturbed and not in sync with actual Current Value. While actual Current Value for Item Price could be 20 (or any number more than 16), someone has set Current Value for this series as 15.

To confirm actual Current Value for particular Series, you should check report for document in question (Item Price in this case), and check for the Item Price ID with highest value.

Let's assume we find that actual Current Value for Item price is 22, then you go Naming Series, and set Current Value for the Prefix/Series of Item Price to 22, and Update Series Number.

These instructions is applicable for all the documents in ERPNext for which user can customize Series and its Current Value.

Let's consider another scenario to learn this better. On assigning a document to another user, error message says:

`Duplicate name ToDo TDI00014286`

This indicate the Current Value for Series/Prefix of ToDo (TDI) has been disturbed. You should follow these steps to correct value for Current Value for TDI prefix.

1. Check ToDo report for the highest ToDo id value.
1. Setup >> Settings >> Naming Series
1. Check section B of Update Series
1. Select Prefix for ToDo "TDI"
1. Ensure that highest number for ToDo is updated as Current Value in Naming Series. If not, correct Current Value, and click on "Update Series Numbering".

<!-- page: erpnext/erpnext__naming-series.md -->
---
title: "Naming Series\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/naming-series"
updated: "2026-03-04"
---


**Masters and transactions can be given prefixes in the form of naming series.**

ERPNext allows you to make prefixes to your documents, with each prefix
forming its own series. For example, a series with prefix INV12#### will have
numbers INV120001, INV120002, and so on.

You can have multiple series for all your transactions. For example, Sales Invoice IDs like these can be generated:

* ACC-SINV-.YYYY.-
* SINV12####
* SALESINV-00####

You can define or select the Naming Series pattern from:

> Home > Settings > Naming Series

## 1. Setting up Naming Series for Documents

1. Select the transaction for which you want to make the series. The system will update the current series in the text box.
2. Edit the series as required with unique prefixes for each series.
 The first prefix will be the default prefix. Each new prefix Naming Series must be added on a new line. The newly added naming series will be available in the document.
 [Screenshot on the live page: Multiple naming series]

3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox.
 There will be no default naming series if this is ticked.

1. You can also update the starting point of a series by entering the series name and the starting point in the “Update Series” section.

1. Click on the Update button to update the set of Naming Series for the selected document.

> Note: To see the newly added Naming Series, click on Settings > Reload.

## 2. Financial Year in Naming Series
You can also show the financial year in the Naming Series. By default, if you enter 'YYYY' in the naming series, it'll pick up the current year. To set naming series based on the fiscal year, enter something like 'ACC-SINV-.FY.-' where 'FY' will be resolved to match the current Fiscal Year. It is common to have a separate series for each financial year.

Alternatively it is also possible to manually embed the fiscal year in the naming series, for example by entering something like 'ACC-SINV-.19-20.-' where 19-20 is the current Fiscal Year.

As you can see, in the following screenshot of a Sales Invoice, the year 2019 is listed:

[Screenshot on the live page: Fiscal year in Naming Series]


## 3. Updating the current value for existing Naming Series

You can change the starting/current sequence number of an existing series.

1. Under the Update Series section, select the prefix whose sequence is to be changed.
1. The current value will be fetched and displayed.
1. Change starting/existing sequence number if needed.
1. Click on Update Series Number.

For example, if the current Sales Order series number is at 16, and you want to restart or set it as 50, enter 0 or 50 depending on your case. Any new Sales Order created will start from the new sequence number.

To know more about this, [visit this article](/erpnext/naming-series-current-value).

> Tip: You could have a separate series for each type of Customer or for
each of your retail outlets.

## 4. Using Field Values in Naming Series

Some companies prefer to make use of "short-codes" for suppliers, i.e. WN for company "Web Notes" that later can be used in naming series for quick identification.

For example:

 A custom field "Vendor ID" is created under Document: Supplier.
 Then under Naming Series, we allow something like
 PO-.YY.MM.-.vendor_id.-.####
 Resulting in "PO-1503-WN-00001"

## 5. Video


<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//IGyISSfI1qU">
</iframe>

<!-- page: erpnext/erpnext__newsletter.md -->
---
title: "Newsletter | ERPNext Documentation"
description: "Learn how to create, test, schedule, and send Newsletters to subscribed Email Groups in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/newsletter"
updated: "2026-07-23"
---

**Newsletter is an email which is sent to a specific group of subscribers periodically.**

In the context of CRM, its is an informational and product-focused email that is sent to existing and potential customers with an intention of softly pushing the subscriber to do required actions.

Newsletter can also be used to share information to employees, investors etc.

You need to create [Email Groups](/erpnext/email_group) before sending the newsletters.

To access the Newsletter list, go to:

> Home > Settings > Email > Newsletter

## How to Create a Newsletter

- Go to the Newsletter list and select New.
- Select the Email Group in RECIPIENT table.
- Enter 'Subject'.
- Enter 'Message'.
- 'Publish' the newsletter to make it available on the web.
- Tick 'Send Unsubscribe Link' if you would like to include unsubscribe link in the email.
- 'Send Web View Link' will include a link in the email to open the newsletter on the web. This option is only visible when the newsletter is published.

[Screenshot on the live page: Newsletter]

Below is the screenshot of the email received with link to unsubscribe and a link to open the email on the web.

[Screenshot on the live page: Newsletter With Unsubscribe Link]

## Features

### Create Subscriber Groups

You can manage subscribers by grouping them into different [Email Groups](/erpnext/email_group).

You can select multiple email groups in the 'RECIPIENT' tables in the newsletter.

### Schedule Send

You can choose to send your newsletter at any future datetime by specifying time in hourly steps.

[Screenshot on the live page: Scheduled Newsletter]

### Test Newsletter Before Sending to Subscribers

Once the newsletter is ready you can provide a 'Test Email Address' and select 'Test'.

You can review the newsletter received in the test email, verify it and then send it to all subscribers by clicking on 'Send'.

[Screenshot on the live page: Newsletter Test]

<!-- page: erpnext/erpnext__non-conformance.md -->
---
title: "Non Conformance\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/non-conformance"
updated: "2026-02-26"
---

*A Non Conformance is a observation that can be filed by any person in the organization to note non compliance to a specific procedure*

Once Quality Procedures are defined, the goal of a quality focussed organization is to ensure that they hare followed. This ensures consistent quality and parameters as per the customer's expectation. If these procedures are not followed, an observation is recorded via a *Non Conformance* or called NC in quality systems.

In ERPNext, you can create a Non Conformance by selecting the Quality Procedure against which it was observed, maintain its status and record corrective and preventive actions

## 1. Prerequisites

1. [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)

## 2. How to Create a Non Conformance

1. Go to Quality > Non Conformance or find the Quality Procedure and click on + from the dashboard.
2. Record your observations
3. Record corrective / preventive actions if any
4. Update status

[Screenshot on the live page]

## 3. Related Topics

1. [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)

<!-- page: erpnext/erpnext__non-profit.md -->
---
title: "Non-profit Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/non-profit"
updated: "2026-07-02"
---

ERPNext can be used by non-profit organizations to manage their operations, accounting, donations, memberships, projects, and reporting. The non-profit features were historically provided through a separate custom app called Non Profit.

The app is not part of the standard ERPNext installation. It needs to be installed separately, and it may not be available or compatible with the latest versions of ERPNext and Frappe Framework.

GitHub app: [https://github.com/frappe/non_profit](https://github.com/frappe/non_profit)

## What the Non Profit app was designed for

The Non Profit app was built on top of Frappe Framework and ERPNext to support organizations that manage donors, members, grants, chapters, volunteers, and social impact programs.

It was meant to help non-profit teams use ERPNext for both financial and operational work, instead of managing donor and program records separately from accounting.

## Typical areas covered

The app may help with workflows such as:

- Donor and member management
- Donation tracking
- Membership records
- Grant and program tracking
- Volunteer or chapter-related records
- Accounting and reporting through ERPNext
- Linking operational records with invoices, payments, and accounts

The exact feature set depends on the version of the app installed and the ERPNext version it is used with.

## Important compatibility note

The Non Profit app repository is currently archived and read-only. This means it may not receive regular updates for newer ERPNext versions.

Before using it on a production site, check whether the app is compatible with your ERPNext and Frappe version. If it is not compatible, the recommended approach may be to build a small custom app or customizations for the specific non-profit workflows needed by your organization.

## When should you consider it?

Consider the Non Profit app if you are running an older compatible ERPNext version, or if you want to study the app as a reference for building non-profit workflows.

For newer ERPNext versions, treat it carefully and verify compatibility before installation.

## Learn more

You can view the app repository here:

[https://github.com/frappe/non_profit](https://github.com/frappe/non_profit)

<!-- page: erpnext/erpnext__not-able-to-select-has-serial-no-batch-option-in-item-list.md -->
---
title: "Cannot enable Serial and Batch Number"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/not-able-to-select-has-serial-no-batch-option-in-item-list"
updated: "2026-03-02"
---

It is quite possible at times that you do not want to start tracking the inventory as batched and/or serialized but want to start doing so at a later stage.   
The system, by design, doesn't allow you to activate these options once stock transactions have been made.[Screenshot on the live page]You can read more about why the same is disabled [here](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html).  
To enable the options again, you can either delete all stock transactions for this item, or if that is not an option, you can duplicate the same item and inward the stock with these options checked.  
**STEPS:****﻿**1. You will have to first stock out the current item using Stock Reconciliation Tool (make current stock zero). You can also stock out the item by making a stock entry of type **Material issue**.
2. Then using material receipt, inward the serialized inventory. Refer the following link for help on the same: [Opening Stock Balance Entry for Serialized and Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
3. Disable the old items so it cannot be selected in transactions again.

  
**Note:** If you want to maintain the same item code, you will need to rename the existing items, and then create the new item as per the actual item code. Otherwise, you will be maintaining the item under a new code.

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

[Screenshot on the live page: Setting Subject]  


### 1.2 Setting Conditions

Notifications allow you to set conditions according to the field data in your documents. For example, if you want to receive an Email if a Lead has been saved as "Interested" as it's status, you put `doc.status == "Interested"` in the conditions textbox. You can also set more complex conditions by combining them with the operator **and** or **or**.

[Screenshot on the live page: Setting Condition]  


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

[Screenshot on the live page: Setting Property in Notification]  


### 1.5 Example

1. Defining the Criteria [Screenshot on the live page: Defining Criteria]
2. Setting the Recipients and Message [Screenshot on the live page: Set Message]



---

2. Slack Notifications
----------------------

If you prefer to have your notifications sent to a dedicated Slack channel, you can also choose the option "Slack" in the channel options and select the appropriate Slack Webhook URL.

### 2.1 Slack Webhook URL

A Slack webhook URL is a URL pointing directly to a Slack channel.

To generate webhook URLs, you need to create a new Slack App:

1. Go to https://api.slack.com/slack-apps.
2. Click on "Create a Slack App". [Screenshot on the live page: Set Message]
3. Give your App a name and choose the right workspace. Once your app is created, go to the "Incoming Webhooks" section and add a new Webhook to Workspace. [Screenshot on the live page: Set Message]
4. Copy the created link, go back to ERPNext and use it to create a new Slack Webhook URL in Integrations > Slack Webhook URL. [Screenshot on the live page: Set Message]
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
[Screenshot on the live page: Set Message]  




---

3. System Notifications
-----------------------

In **Version 12** we introduced System notifications for **Assignments**, **mentions**, **documents shared**, and **Energy Points**. These notifications show up in the notifications dropdown on the the navigation bar's top right corner.

In **Version 13** we have introduced an additional channel to send alerts - **System Notifications**:

[Screenshot on the live page: Notifications Dropdown]  


Choosing this channel will send a system notification when a notification is triggered, instead of an Email or a Slack notification.

[Screenshot on the live page: Notifications Dropdown]  


Clicking on the notification routes to the **Notification Log** document which contains the configured subject, message as well as the attached file, if Attach Print is set:

[Screenshot on the live page: Notifications Dropdown]  


If Email/Slack alerts and System Notifications both are required, the main channel can be set as Email or Slack and this option can be checked:

[Screenshot on the live page: Notifications Dropdown]  


4. WhatsApp
-----------

In **Version 13** we have introduced an additional channel to send alerts - **WhatsApp**: [Screenshot on the live page: Notifications WhatsApp Channel]  


If you prefer to have your notifications sent to a WhatsApp number, you can also choose the option "WhatsApp" in the channel options and select the appropriate Twilio Number. Twilio Numbers can be added to Twilio settings in Frappe. WhatsApp messages can only be sent to numbers which have country codes in them.

[Screenshot on the live page: Twilio Settings]  


### 4.1 Twilio Settings

In order to configure Twilio settings, you need to first obtain Twilio credentials from your Twilio Account's account settings. You can only add those phone numbers that have been activated in your Twilio Account with WhatsApp access. [Screenshot on the live page: Twilio Credentials]  


### 4.2 Message Format

WhatsApp allows their users to only send those message templates that are pre-approved by them to your customers. Failure to do so might result in restrictions on you Twilio account. [Screenshot on the live page: Pre Approved Message Template]  


5. SMS
------

In **Version 13** we have introduced an additional channel to send alerts - **SMS**: [Screenshot on the live page: SMS Channel]  


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
