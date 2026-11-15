<!-- Frappe documentation: erpnext, part 38 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__moving-asset-from-stock-item-to-fixed-asset-item.md -->
---
title: "Moving Asset from Stock Item to Fixed Asset Item | ERPNext Documentation"
description: "Correct an ERPNext Item that was treated as stock but should be a fixed asset without losing accounting control."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/moving-asset-from-stock-item-to-fixed-asset-item"
updated: "2026-08-15"
---

Imagine Nova Industries bought a laptop intending to sell it, so it was received as inventory. Later, the company decides to give that laptop to an employee. It is no longer stock for sale, but simply selecting **Is Fixed Asset** can leave the same value appearing in both inventory and fixed assets.



The correction must remove the approved inventory position first, then create the fixed-asset Item and Asset record with the right original cost and opening depreciation. This keeps the Stock Ledger, General Ledger, and Asset Register from counting the laptop twice.

## Before you begin

Back up the site, identify every stock transaction for the Item, reconcile its current quantity and valuation, and agree the correction date and accounts with the accounting owner. Do not use this procedure to rewrite genuine historical sales inventory.

## Correct the stock position

1. Stop new transactions for the Item during the correction.
2. Use the appropriate [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation) or supported stock transaction to bring the stock position to the approved result.
3. Verify Stock Ledger and General Ledger impact.
4. If submitted transactions prevent changing Item type, create a new fixed-asset Item rather than forcing the existing record.

## Configure the fixed-asset Item

Enable **Is Fixed Asset**, select the Asset Category, and decide whether future purchases should auto-create Assets.

![ERPNext Item configured as a fixed asset](https://novacompanies.m.frappe.cloud/files/06-fixed-asset-item.png)

## Create the Asset

Create an Existing Asset using the approved original cost, available-for-use date, opening accumulated depreciation, and number of already booked depreciation entries.

![Existing Asset created after reclassification](https://novacompanies.m.frappe.cloud/files/07-asset-core-details.png)

## Verify the correction

Confirm stock quantity is no longer carried incorrectly, the Asset appears in the register, opening value and depreciation reconcile, and no cost was counted twice.

![Asset list used to verify the reclassified item](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### Is Fixed Asset cannot be enabled

The Item has submitted stock transactions or quantity. Create a new fixed-asset Item and use controlled accounting entries instead of forcing the flag.

### The asset cost appears in both stock and fixed assets

Reverse or correct the stock side, then reconcile Stock Ledger, General Ledger, and Fixed Asset Register on the same date.

### Opening depreciation is missing

Enter approved opening accumulated depreciation and the number of booked depreciations on the Existing Asset before final submission.

## Frequently asked questions

### Can I convert an Item after years of stock transactions?

Usually a new fixed-asset Item is safer because historical inventory transactions must remain valid.

### Should the reclassification use a Journal Entry only?

A Journal Entry may correct accounts but does not create the operational Asset history or remove stock quantity. Use the full controlled process.

### What date should the Asset use?

Use the approved original purchase and available-for-use dates, with opening depreciation as of the migration or correction cut-off.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__mpesa-integration.md -->
---
title: "M-Pesa Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/mpesa-integration"
updated: "2026-02-26"
---


**M-Pesa integration allows processing transactions with the payment gateway provider M-Pesa.**

M-Pesa Integration facilitates the processing of payments between the M-Pesa application and ERPNext. M-Pesa Integration only works with the POS to facilitate the payments for the same. This feature doesn't work with the shopping cart.

To set up M-Pesa, go to:
> Integrations > Payments > M-Pesa Settings

## 1.How to get your M-Pesa credentials?
1. In order to activate your API credentials, you need to log in to your M-Pesa account.
2. Then, open the Go Live section of the application and follow the steps to get the approval for the app.
3. When all the test cases are satisfied and expected results match the final results, you need to submit the document and follow the steps to get the final credentials for your application.
4. Details mentioned in the Production URL and Credentials section are the credentials that you are supposed to use in M-Pesa Settings.

![Mpesa Credentials](/files/mpesa_credentials.png)


## 2.Setting up M-Pesa

To enable M-Pesa Express, you need to configure all the mandatory parameters which you have received from M-Pesa. If you want to use the staging environment of the integration, you can select the staging option and use the staging credentials provided by M-Pesa by creating a separate application for the same.
![Mpesa Settings](/files/mpesa_settings.png)

On enabling the M-Pesa integration in ERPNext, the system will create a Payment Gateway record and an Account head in the Chart of Accounts with the Account type as Bank as seen in the following screenshot.

![Mpesa COA](/files/mpesa_coa.png)
![Mpesa POS Settings](/files/mpesa_pos_settings.png)

It will also create a Mode of Payment with the same name and account as the payment gateway's, along with certain custom fields in POS Settings to handle the POS payments.

![Payment Gateway Account](/files/payment_gateway_account_mpesa.png)

After configuring the Payment Gateway Account, you will be able to accept online payments via M-Pesa.


## 3. M-Pesa POS Payments

On setting up the POS profile with M-Pesa mode of payment, the POS checkout would show an additional information section. This section contains two fields that were automatically set-up on adding M-Pesa settings.

![POS Additional Information](/files/additional-information.png)

As soon as a POS user fills the mobile number of the customer, they can initiate a request for payment from the customer. A request is sent to the customer's M-Pesa mobile application linked with the specified mobile number. Once the payment is processed by the user, the user is prompted by a confirmation dialog to submit the payment.

## 4. M-Pesa Account Balance

Account balance linked with an individual M-Pesa can be fetched via the Get Account Balance button. This will load the M-Pesa account balance details in the dashboard.

![POS Account Balance](/files/mpesa_account_balance.png)


## 5. Supporting transaction currencies

M-Pesa will only work for the Company which has KSH (Kenyan Shilling) as the Company Currency.

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



![EUR bank account with its fixed account currency](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-account.png)

Each bank or cash account has one currency. If the real bank provides separate USD and EUR balances, represent them with separate ERPNext accounts. This keeps [Bank Reconciliation](/erpnext/bank-reconciliation) and audit trails intelligible.

## Configure Customers and Suppliers

Set a foreign Customer's **Billing Currency**, then add the matching receivable account in the Customer's Default Accounts child table. For a Supplier, use Billing Currency and the Per-Company Accounts table with the matching payable account.



![Customer billing currency](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-billing-currency.png)



![Open the Customer default-account row](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-account-pencil.png)

Select the highlighted pencil to open the full child-row editor.



![Customer linked to a EUR receivable account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-eur-receivable.png)

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

![EUR Sales Invoice and conversion rates](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-currency-rate.png)

The Exchange Rate converts EUR 1,200 to USD 1,380. The Price List Exchange Rate is 1 because both the Price List and invoice use EUR.



![EUR and USD totals on the Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-totals.png)

On submission, the receivable is maintained in the account currency and base debit and credit values are recorded in USD. The [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) report shows party or account-currency amounts according to its filters.

## Record foreign-currency purchases and payments

A [Purchase Invoice](/erpnext/purchase-invoice) follows the same pattern using the Supplier's payable account and buying rate. Outstanding and advance values follow the party account currency.

In a Payment Entry, currencies come from the selected accounts. Receiving EUR from a EUR receivable into a USD bank produces a paid amount in EUR, a received amount in USD, and a source exchange rate.



![Currencies of the paid-from and paid-to accounts](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![Exchange rate and converted amounts in Payment Entry](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

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



![EUR values in the General Ledger](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-general-ledger.png)

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



![EUR formatting and fractional-unit settings](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-eur-settings.png)

## 3. Create foreign-currency accounts

In the [Chart of Accounts](/erpnext/chart-of-accounts), create the ledgers that must keep foreign balances. For the example:

- Euro Bank, Account Type Bank, Currency EUR
- Euro Receivables, Account Type Receivable, Currency EUR
- Euro Payables, Account Type Payable, Currency EUR



![Foreign-currency bank account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-account.png)

Do this before posting entries. ERPNext does not allow an account's currency to be changed once ledger entries exist. Keep separate accounts for separate bank currencies even when the same institution supplies both balances.

## 4. Configure Customers and Suppliers

On the [Customer](/erpnext/customer), set Billing Currency to EUR. In Default Accounts, link Nova Electronics Distribution to Euro Receivables. Use the pencil in the child row to open the full editor.



![Billing Currency on the Customer](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-billing-currency.png)



![Customer default EUR account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-customer-default-eur-receivable.png)

Apply the corresponding setup on the Supplier with Euro Payables. A party's billing currency and account currency should agree with the normal invoice currency.

## 5. Create currency-specific prices

Create a EUR [Price List](/erpnext/price-lists) when you maintain contractual or market prices in euros. Add EUR Item Prices. This is independent from the accounting rate. On a transaction:

- Exchange Rate converts the transaction total to Company currency.
- Price List Exchange Rate converts item prices when Price List currency differs from transaction currency.

When both the transaction and Price List use EUR, the Price List Exchange Rate is 1.

## 6. Define the exchange-rate policy

Create [Currency Exchange](/erpnext/currency-exchange) records for approved or historical rates. Configure [Currency Exchange Settings](/erpnext/currency-exchange-settings) for provider fallback. Decide how **Allow Stale Exchange Rates** and **Stale Days** should work in [Accounts Settings](/erpnext/accounts-settings).



![Approved EUR to USD rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-exchange-rate.png)

Document who may update manual rates, how often rates are reviewed, and whether buying and selling use the same rate. Store both directions when processes request both EUR to USD and USD to EUR.

## 7. Configure gain and loss accounts

In Company accounting defaults, set:


| Field                                 | Purpose                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| Exchange Gain / Loss Account          | Realized differences, commonly when a payment settles an invoice at a different rate. |
| Unrealized Exchange Gain/Loss Account | Reporting-date revaluation of balances that remain open.                              |


![Company exchange gain and loss accounts](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-company-exchange-gain-loss-accounts.png)

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

  


![](/files/Nr1n53j.png)

  


Step 1: Go to "Naming Series" doctype and select transaction as "Sales Invoice"

  


![](/files/1KrOqdx.png)

  


Step 2: Add a new naming series having maximum upto 16 characters. For eg INV-.YYYY.-.#####. Add this as the first option and don't check "User must always select" inorder to make this as the defaut naming series

  


![](/files/hrHZ0Rv.png)

  


  

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

![Update Series Section](/files/current-no-1.png)

#### Select Prefix

Considering our scenario, prefix for Sales Order will be "SO".

![Series Prefix](/files/current-no-2.png)

#### Current Value

If you have currently 12 Sales Orders created in your account, then current value updated will be 12. You can edit Current Value to 322, and then click on Update Series Number.

![Series Current Value](/files/current-no-3.png)

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
 ![Multiple naming series](/files/multiple-naming-series.gif)

3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox.
 There will be no default naming series if this is ticked.

1. You can also update the starting point of a series by entering the series name and the starting point in the “Update Series” section.

1. Click on the Update button to update the set of Naming Series for the selected document.

> Note: To see the newly added Naming Series, click on Settings > Reload.

## 2. Financial Year in Naming Series
You can also show the financial year in the Naming Series. By default, if you enter 'YYYY' in the naming series, it'll pick up the current year. To set naming series based on the fiscal year, enter something like 'ACC-SINV-.FY.-' where 'FY' will be resolved to match the current Fiscal Year. It is common to have a separate series for each financial year.

Alternatively it is also possible to manually embed the fiscal year in the naming series, for example by entering something like 'ACC-SINV-.19-20.-' where 19-20 is the current Fiscal Year.

As you can see, in the following screenshot of a Sales Invoice, the year 2019 is listed:

![Fiscal year in Naming Series](/files/year-naming-series.png)


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

![Newsletter](/files/newsletter-doc.png)

Below is the screenshot of the email received with link to unsubscribe and a link to open the email on the web.

![Newsletter With Unsubscribe Link](/files/newsletter-doc-web-link.png)

## Features

### Create Subscriber Groups

You can manage subscribers by grouping them into different [Email Groups](/erpnext/email_group).

You can select multiple email groups in the 'RECIPIENT' tables in the newsletter.

### Schedule Send

You can choose to send your newsletter at any future datetime by specifying time in hourly steps.

![Scheduled Newsletter](/files/scheduled-newsletter.png)

### Test Newsletter Before Sending to Subscribers

Once the newsletter is ready you can provide a 'Test Email Address' and select 'Test'.

You can review the newsletter received in the test email, verify it and then send it to all subscribers by clicking on 'Send'.

![Newsletter Test](/files/newsletter-test.png)

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

![](/files/Screenshot 2026-01-23 at 1.47.10 AM.png)

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
The system, by design, doesn't allow you to activate these options once stock transactions have been made.![](/files/a0VHlSB.png)You can read more about why the same is disabled [here](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html).  
To enable the options again, you can either delete all stock transactions for this item, or if that is not an option, you can duplicate the same item and inward the stock with these options checked.  
**STEPS:****﻿**1. You will have to first stock out the current item using Stock Reconciliation Tool (make current stock zero). You can also stock out the item by making a stock entry of type **Material issue**.
2. Then using material receipt, inward the serialized inventory. Refer the following link for help on the same: [Opening Stock Balance Entry for Serialized and Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
3. Disable the old items so it cannot be selected in transactions again.

  
**Note:** If you want to maintain the same item code, you will need to rename the existing items, and then create the new item as per the actual item code. Otherwise, you will be maintaining the item under a new code.
