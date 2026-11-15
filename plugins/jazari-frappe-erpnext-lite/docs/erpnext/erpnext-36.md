<!-- Frappe documentation: erpnext, part 36 of 69. Index: docs/INDEX.md -->

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



![Posting-date setting for exchange gain or loss](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-accounts-settings-exchange-gain-loss-date.png)

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



![EUR receivable and USD bank account currencies](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![EUR paid amount, USD received amount, and source rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

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

![Batch Item](/files/batchwise-stock-1.png)

You can create a new Batch from:

`Stock > Documents > Batch > New`

Read [Stock batch](/erpnext/batch.html) to learn more.

For the Batch item, updating Batch No. in the stock transactions (Purchase Receipt &amp; Delivery Note) is mandatory.

#### Purchase Receipt

When creating Purchase Receipt, you should create new Batch, or select one of the existing Batch master. One Batch can be associated with one Batch Item.

![Batch in Purchase Receipt](/files/batchwise-stock-2.png)

#### Delivery Note

Define Batch in Delivery Note Item table. If Batch item is added under Product Bundle, you can update it's Batch No. in the Packing List table as well.

![Batch in Delivery Note](/files/batchwise-stock-3.png)

#### Batch-wise Stock Balance Report

To check batch-wise stock balance report, go to:

Stock > Standard Reports > Batch-wise Balance History

![Batchwise Stock Balance](/files/batchwise-stock-4.png)

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

![UoM Must be Whole No](/files/uom-fraction-1.png)

### Validation

While creating transaction, if you enter value in fraction for item whose UOM has "Must be whole number" checked, you will get error message stating:

`Quantity cannot be a fraction at row #`

![UoM Validation Message](/files/uom-fraction-2.png)

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

![Invoice Discount in Payment Entry in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-05-payment-entry-references.png)

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

![Multi-level BOM](/files/multi-bom.png)

The 'Materials' table will only show the sub-assemblies while the 'Materials Required (Exploded)' table will show all the raw materials required to manufacture the final product.

BOM materials table where sub-assembly is shown:
![Multi-level BOM](/files/bom-materials.png)

In the exploded view only the raw materials are shown:
![Multi-level BOM](/files/bom-materials-exploded.png)


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

<!-- page: erpnext/erpnext__managing-transactions-in-multiple-currencies.md -->
---
title: "Managing Transactions in Multiple Currencies | ERPNext Documentation"
description: "Create, review, print, pay, and verify foreign-currency sales and purchase transactions in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-transactions-in-multiple-currencies"
updated: "2026-08-14"
---

Nova Industries distributes electronics internationally while keeping its Company accounts in USD.



EuroTech Retail wants to receive and pay a EUR invoice, while Nova must keep its books in USD. Users need to enter, print, collect, and reconcile the sale in EUR without losing the USD value required for accounting.



This guide follows a EUR 1,200 Sales Invoice at `1 EUR = 1.15 USD`. The customer sees EUR 1,200 while ERPNext records USD 1,380 in Company currency. You will see where the currencies and rates come from, how payment is converted, and how to verify the result. The same controls apply to purchases through the corresponding Supplier and payable fields.

## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup):

- EUR is enabled in [Currency](/erpnext/currency).
- EuroTech Retail has Billing Currency EUR.
- Euro Receivables is a EUR Receivable [Account](/erpnext/chart-of-accounts) linked to the Customer.
- Nova Europe EUR is an enabled selling [Price List](/erpnext/price-lists).
- A dated EUR to USD rate exists in [Currency Exchange](/erpnext/currency-exchange), or the configured provider covers it.
- The Company has an Exchange Gain/Loss account.

Test the full invoice and payment cycle in Draft before using imported or live data.

## Create a foreign-currency Sales Invoice

1. Open Accounting &gt; Sales and Receivables &gt; Sales Invoice.
2. Select **Add Sales Invoice**.
3. Choose Nova Electronics Distribution and EuroTech Retail.
4. Confirm the Posting Date, Payment Due Date, and EUR Currency.
5. Review the Exchange Rate field. Its label states the direction.
6. Select Nova Europe EUR and confirm Price List Currency EUR.
7. Add the item, quantity, and rate.
8. Review taxes, payment terms, and totals.

![EUR transaction and price-list rates](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-currency-rate.png)

The screenshot shows two rates:


| Field                    | Purpose in this example                                                             |
| ------------------------ | ----------------------------------------------------------------------------------- |
| Exchange Rate            | Converts the EUR transaction total to the USD Company value. `1 EUR = 1.15 USD`.    |
| Price List Exchange Rate | Converts Price List currency to transaction currency. It is 1 because both are EUR. |


An Actual tax or charge entered directly on the transaction is entered in the transaction currency. Review calculated taxes and Company-currency equivalents according to the tax template and charge type.

## Confirm the receivable account

Open the Accounting section and check **Debit To**. It should be Euro Receivables for this Customer and Company.



![EUR receivable selected on the Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-receivable-account.png)

If the selected account is in a foreign currency, the invoice currency must normally match it. Do not switch only the Currency field and ignore Debit To.

## Compare transaction and Company totals

Before submission, compare the party-facing total and the Company-currency total.



![EUR and USD Sales Invoice totals](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-totals.png)

For EUR 1,200 at 1.15:


| View                        | Amount    |
| --------------------------- | ---------: |
| Customer invoice total      | EUR 1,200 |
| Company-currency total      | USD 1,380 |
| Receivable account currency | EUR       |


Submit only after the rate, account, prices, taxes, and terms are correct. The submitted [Sales Invoice](/erpnext/sales-invoice) retains these values even if a later Currency Exchange record changes.

## Print and send the invoice

Open Print or Preview and confirm that rates, amounts, totals, and amount in words use the expected party-facing currency. The print format should show EUR for the invoice values. Company-currency fields are accounting fields and do not normally replace the agreed invoice currency in the customer-facing document.

If the symbol or number separators are wrong, correct the Currency master or site number format rather than hard-coding symbols into every print format.

## Create the Payment Entry

Create the Payment Entry from the submitted invoice when possible:

1. Open the invoice and select Create &gt; Payment.
2. Confirm Payment Type **Receive** and the Customer.
3. Confirm **Paid From** is the EUR receivable account.
4. Select the actual bank account under **Paid To**.
5. Enter the amount received in the bank account currency.
6. Review Source Exchange Rate and the Company-currency amount.
7. Confirm the invoice reference and allocated amount.

![Account currencies in Payment Entry](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![Paid and received amounts with the source rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

The paid-from and paid-to account currencies control the amount fields. In the example, EUR 1,200 is cleared from the receivable and USD 1,380 is received into the operating bank.

If the payment-date rate differs from the invoice rate, use [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference). Keep bank charges, withholding, write-offs, and exchange difference in their appropriate accounts.

## Enter a foreign-currency purchase

On a [Purchase Invoice](/erpnext/purchase-invoice), select the Supplier, EUR, the buying Price List, and the EUR payable account. Review the Exchange Rate and Price List Exchange Rate exactly as on the sales side.



![EUR Purchase Invoice conversion fields](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-purchase-invoice-eur-currency-rate.png)

On submission, the payable outstanding is maintained according to the party account currency. Create a Pay-type Payment Entry and verify the amount removed from the bank and the EUR amount cleared from the payable.

## Transactions in several currencies for one party

Accounts Settings includes **Allow multi-currency invoices against single party account**.



![Allow invoices in multiple currencies against one party account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-accounts-settings-multi-currency-invoices.png)

This can support a party invoiced in multiple currencies while using a Company-currency party account. It does not make a bank account multi-currency, and it can make outstanding and payment interpretation harder. Use dedicated currency accounts for currencies that the business regularly holds or reconciles. Test [Payment Reconciliation](/erpnext/payment-reconciliation), ageing, credit notes, advances, and returns before enabling the option broadly.

## Verify reports

Use the [General Ledger](/erpnext/general-ledger) filtered by the foreign account. It shows debit, credit, and balance in account currency when appropriate.



![EUR bank balance in the General Ledger](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-general-ledger.png)

Review [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) in the party or account currency. Financial statements use Company currency. At period end, run [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) for eligible open foreign balances.

## Troubleshooting

### Currency changes but item rates look wrong

Check Price List, Price List Currency, and Price List Exchange Rate. The transaction Exchange Rate does not necessarily convert the source Item Price.

### The invoice cannot be saved because account currency differs

Use the matching receivable or payable account, or correct the party's per-Company default. Do not change an account currency after postings exist.

### Payment Entry receives the wrong USD amount

Check the paid-to bank currency, source or target rate, paid amount, received amount, and invoice allocation. Use the actual bank amount and account for legitimate differences separately.

### The printed currency differs from the agreement

Verify the submitted transaction Currency and Price List. Then inspect the print format for hard-coded symbols or base-currency fields.

## FAQs

### Can I omit the invoice exchange rate and convert only at payment?

No, ERPNext needs a Company-currency value when the invoice posts. A later payment can use a different rate and recognize the difference.

### Can the invoice and Price List use different currencies?

Yes, Price List Exchange Rate converts item prices, while Exchange Rate converts the transaction to Company currency.

### Why does Payment Entry not have a free Currency selector?

Its currencies come from the paid-from and paid-to accounts. Select accounts that represent the actual balances.

### Can I show Company currency on the print format too?

Yes, with an appropriate print design, but keep the agreed transaction-currency amount clear and verify custom fields and labels.

### What happens when a foreign invoice remains unpaid at month end?

Its foreign amount remains outstanding. Revalue the eligible account to update its Company-currency carrying value according to your closing policy.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__managing-tree-structure-masters.md -->
---
title: "Manage Tree Structure Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-tree-structure-masters"
updated: "2026-03-04"
---


Some of the masters in ERPNext are maintained in tree structure. Tree structured masters allow you to set Parent master, and Child masters under those Parents. Setting up this structure allows you creating intelligent report, and track growth at each level in the hierarchy.

Following is the partial list of masters which are maintained in the tree structure.

* Chart of Accounts

* Chart of Cost Centers

* Customer Group

* Territory

* Sales Person

* Item Group

Following are the steps to manage and create record in the tree structured master. Let's consider Territory master to understand managing tree masters.

####Step 1 : Go to Master

`Selling > Setup > Territory`

####Step 2 : Parent Territory

![Default Territories](/files/territory-2.png)

When click on Parent territory, you will see option to add child territory under it. All default Territory groups will be listed under Parent group called "All Territories". You can add further Parent or child Territory Groups under it.

####Step 3: Add new Territory

When click on Add Child, a dialog box will provide two fields.

**Territory Group Name**

Territory will be saved with Territory Name provided here.

**Group Node**

If Group Node selected as Yes, then this Territory will be created as Parent, which means you can further create sub-territories under it. If select No, then it will become child Territory which you will be able to select in another masters.

Only child Territory Groups are selectable in another masters and transactions.
![Default Territories](/files/territory-1.gif)

Following is how Child Territories will be listed under a Parent Territory.

![Adding new Territories](/files/territory-3.png)

Following this steps, you can manage other tree masters as well in ERPNext.

<!-- page: erpnext/erpnext__manufacturer.md -->
---
title: "Manufacturer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturer"
updated: "2026-03-06"
---

**A manufacturer created or produces an Item.**

A Manufacturer may not be the same person/company that sells the Item under a specific [Brand](/erpnext/brand). For example, Unico Plastics can be the Manufacturer of plastic brushes but it may be sold under a Brand, say, Super Brushes.

In ERPNext, a Manufacturer can be used to identify Items using a specific part number.

To access the Manufacturer list, go to:

> Home > Stock > Manufacturer

## 1. How to Create a Manufacturer

1. Go to the Manufacturer list and click on New.
2. Enter a Manufacturer name and enter a description if needed.
3. Save.
  [Manufacturer](/files/manufacturer.png)

After creating a Manufacturer, you can create an **Item Manufacturer** record with a Manufacturer Part Number for identification.

![](/files/item_manufacturer.png)

### 1.1 Additional details

The following details can be set for a Manufacturer:

- Website
- Country
- Logo

## 2. Features

### 2.1 Address and Contacts

An [Address](/erpnext/address) and [Contact](/erpnext/contact) can be set for this Manufacturer.

## 3. Related Topics

1. [Item](/erpnext/item)
2. [Supplier](/erpnext/supplier)
3. [Brand](/erpnext/brand)

<!-- page: erpnext/erpnext__manufacturing-dashboard.md -->
---
title: "Manufacturing Dashboard\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-dashboard"
updated: "2026-02-26"
---

![](/files/image077385.png)

---

## Number Cards

In ERPNext, Number Cards are a type of widget or visual component that displays key metrics or numerical data in a dashboard. They are typically used to show quick, high-level insights that help users keep track of important business performance indicators or operational statistics.

![](/files/CleanShot 2026-02-19 at 11.41.16@2x.png)

1. **Monthly Total Work Order** :- You will get the total count of Work Orders which are in Open, In Progress, and Completed state. The Work Orders created one month before the current date will be displayed in the number card.
2. **Monthly Completed Work Order** :- The user will get the total count of Work Orders which are in the Completed state. The Work Orders created one month before the current date will be displayed in the number card.
3. **Ongoing Job Card** :- The user will get the total count of Job Cards that are not in the Completed state.
4. **Monthly Quality Inspection** :- The user will get the total count of Quality Inspection records which are in the Submitted state. The Work Orders created one month before the current date will be displayed in the number card.

---

## Dashboard

You can see some predefined graph reports in the dashboard when you open the Manufacturing module. These reports are fully customizable, you can choose what to show or hide and also configure the metrics on which the reports are shown.

![](/files/CleanShot 2026-02-19 at 11.52.51@2x.png)

### Produced Quantity

The chart will give the information about the total quantity produced (using Work Order) in the last year on a Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

### Completed Operation

The chart will give information about the total number of operations completed in the last year on Quarterly basis. Users can also view the chart data based on Daily, Weekly, Monthly, Yearly basis.

---

![](/files/image31eb3a.png)

### Work Order Analysis

This chart will give the information about the number of Work Orders based on Not Started, In Process, Stopped, Completed statuses. This Donut chart will provide the information based on the last year's Work Order data. Your can also change the date range by clicking on the **Filter** button.

### Quality Inspection Analysis

This chart will give information about the number of Quality Inspections based on Accepted and Rejected status. The chart type is a donut and it will provide the information based on the last year's quality inspection data. Your can change the date range by clicking on the **Filter** button.

### Pending Work Orders

The chart will give information about the number of Work Orders that are pending based on the aging days. The number of aging days is calculated based on the difference between the current date and planned start / actual start date days.

### Last Month Downtime Analysis

The chart will give information about the total number of minutes a machine was not working in the last month. This helps the operator to know which machine has not performed well and requires maintenance.

---

![](/files/image60f6db.png)

### Work Order Quantity Analysis

The chart will give information about the total number of quantities that are Pending and Completed based on the Work Orders every month for the last year.

### Job Card Analysis

The chart will give information about the total number of Job Cards which are in the Pending and Completed states every month for the last year.

<!-- page: erpnext/erpnext__manufacturing-reports.md -->
---
title: "Manufacturing Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-reports"
updated: "2026-02-26"
---


There are various reports in the Manufacturing module that help you track Work Order progress, production analytics, BOM reports, etc.

In all of these reports, you can set a chart to show a visual representation. To do this, click on the Set Chart button.

These reports can be accessed from:
> Home > Manufacturing > Reports

## Open Work Orders
Shows the open Work Orders which have not started production yet.

![Open Work Orders](/files/open-wo.png)

## Work in Progress Report

This report shows any work orders that have started and are in progress. The status of these Work Orders is 'In Process'.

![WIP report](/files/wip-report.png)

## Issued Items Against Work Order
Items that are issued to a Work Order and are transferred to the Work in Progress Warehouse are shown here.
![Items Against WO](/files/items-against-wo.png)


## Completed Work Orders
Work Orders which are completed with all the quantities in it manufactured are shown in this report.

![Completed Work Orders](/files/completed-wo.png)

## Production Analytics
This report shows the overall analytics of all Work Orders.

![Production Analytics](/files/production-analytics.png)

## BOM Search
In this report, you can search for specific BOMs based on the raw materials items used in them, then open it. Useful if you have a lot of BOMs.
![BOM search](/files/bom-search.png)

## BOM Stock Report
On selecting a BOM in this report, the raw material quantity in Warehouses will be shown. As you can see, the items which have insufficient quantity are shown in red and ones with enough quantity to manufacture the BOM Item are shown in green.

![BOM Stock Report](/files/bom-stock-report.png)

<!-- page: erpnext/erpnext__manufacturing-settings.md -->
---
title: "Manufacturing Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-settings"
updated: "2026-02-26"
---

Manufacturing settings in ERPNext configure production workflows, manage bill of materials (BOM), track work orders, and oversee inventory to streamline operations and ensure efficient production management.


> Home > Manufacturing > Settings > Manufacturing Settings
> 
> 

**Raw Materials Consumption**
-----------------------------

![Screenshot 2024-08-29 at 3.28.09 PM](/files/Screenshot 2024-08-29 at 3.28.09 PM.png)  


### 1. Allow Continuous Material Consumption

If enabled, materials can be consumed without immediately manufacturing finished goods in a single Work Order. This is useful if one or more time consuming products are being manufactured.

For example a single product takes a month to manufacture and the raw materials are consumed daily. In a regular scenario, this won't be feasible with stock entries. Enabling this option will allow you to create stock entries for **Material Consumption** without having to create an entry to backflush. End result is that you can see the stock being consumed in the Warehouses and can update the final manufacture entry for finished goods at a later stage.

### 2. Backflush raw materials based on

The method selected here will be chosen for backflushing raw materials : 1. Material Transferred for Manufacture 2. BOM

### 3. Validate Components and Quantities Per BOM

Note: This feature will be available from the version V15

![](/files/validate_component_and_qty_as_per_bom.png)

If "Backflush Raw Materials Based On" as BOM, then users can validate component quantity according to BOM. To do that they have to enable "Validate Components Quantities Per BOM" checkbox in the "Manufacturing Settings".

If user has changed the quantity in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

![component-qty-validation](/files/component-qty-validation.png)  

If user has removed the item in the "Material Transfer for Manufacture" or "Manufacture" stock entry, then system will throw the below error

![](/files/Screenshot%202025-01-02%20at%2012.54.40%20PM.png)


### 4. Get Raw Materials Cost from Consumption Entry

![](/files/Screenshot%202025-01-02%20at%201.28.32%20PM.png)

If the 'Allow Continuous Material Consumption' is enabled then user can see the option 'Get Raw Materials Cost from Consumption Entry'.

The 'Get Raw Materials Cost from Consumption Entry', determines whether the cost of raw materials used in production should be automatically derived from the consumption entries recorded during the manufacturing process. When enabled, ERPNext calculates the cost based on the actual materials consumed, ensuring accurate cost tracking and financial reporting.

Capacity Planning
-----------------

Capacity planning is the process in which an organisation decides whether or not to accept the new orders based on the resources and existing work orders.

![Screenshot 2024-08-29 at 3.30.52 PM](/files/Screenshot 2024-08-29 at 3.30.52 PM.png)  


### 1. Disable Capacity Planning

If checked, capacity planning won't be done. Enabling it will help to decide whether or not to accept the new orders based on the resources and existing work orders.

### 2. Allow Overtime

If enabled it'll allow creating work orders, job cards etc. outside workstation working hours.

### 3. Allow Production on Holidays

If enabled, it'll allow production activities even on those days that are marked as holidays as per the Holiday List of the organisation.

### 4. Capacity Planning For (Days)

The number of days specified here means the number of days in advance when the capacity planning activities will be initiated for production.

### 5. Time Between Operations (Mins)

This specifies the time span that should be kept between two operations in minutes.

Default Warehouses for Production
---------------------------------

![Screenshot 2024-08-29 at 3.32.55 PM](/files/Screenshot 2024-08-29 at 3.32.55 PM.png)  


### 1. Default Work In Progress Warehouse

This Warehouse will be auto-updated in the 'Work In Progress' Warehouse field of Work Orders.

### 2. Default Finished Goods Warehouse

This Warehouse will be auto-updated in the 'Target Warehouse' field of Work Order.

### 3. Default Scrap Warehouse

This Warehouse will be auto-updated in the 'Scrap Warehouse' field of Work Order.

Over Production for Sales and Work Order
----------------------------------------

![Screenshot 2024-08-29 at 3.36.10 PM](/files/Screenshot 2024-08-29 at 3.36.10 PM.png)  


### 1. Overproduction Percentage For Sales Order

It allows you to specify a percentage by which production can exceed the sales order quantity.

### 2. Overproduction Percentage For Work Order

It defines the allowable percentage by which the actual production quantity can exceed the planned quantity specified in a work order.

Job Card
--------

![Screenshot 2024-08-29 at 3.38.32 PM](/files/Screenshot 2024-08-29 at 3.38.32 PM.png)  


### 1. Add Corrective Operation Cost in Finished Good Valuation

If enabled then the cost for a corrective operation type will also be included while calculating finished goods valuation

### 2. Allow Excess Material Transfer

If enabled, the **Material Transfer** button will be visible and will allow you to transfer raw materials even if after the raw material requirement is fulfilled against a Job Card.

This is particularly useful in cases where the transferred raw materials are damaged and additional raw materials need to be transferred to produce the same amount of finished goods as intended.

Other Settings
--------------

![Screenshot 2024-08-29 at 3.39.41 PM](/files/Screenshot 2024-08-29 at 3.39.41 PM.png)  


### 1. Update BOM Cost Automatically

If ticked, the BOM cost will be automatically updated based on Valuation Rate / Price List Rate / last purchase rate of raw materials.

### 2. Set Operating Cost / Scrape Items From Sub-assemblies

In the case of 'Use Multi-Level BOM' in a work order, if the user wishes to add sub-assembly costs to Finished Goods items without using a job card as well the scrap items, then this option needs to be enable.

### 3. Make Serial No/Batch from Work Order

If checked, system will automatically create the serial numbers / batches for finished goods on submission of Work Order

### 4. Allow Editing of Items and Quantities in Work Order

If enabled, the system will allow users to edit the raw materials and their quantities in the Work Order. The system will not reset the quantities as per the BOM, if the user has changed them in the work order materials table.


![Screenshot 2025 11 07 at 3.25.52 PM](/files/Screenshot%202025-11-07%20at%203.25.52%20PM.png)

<!-- page: erpnext/erpnext__manufacturing-without-creating-bom.md -->
---
title: "Manufacturing without creating BOM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing-without-creating-bom"
updated: "2026-03-02"
---

**It is recommended to use BOM for Manufacturing for consistency and to avoid repetitive work.**   
However, if you wish to perform it manually, the workaround is to create Stock Entries:1) Create a **Stock Entry** with **Purpose** as **Material Transfer to Manufacture.**![](/files/EsxLtl4.png)2) Create a **Stock Entry** with **Purpose** as **Manufacture, the Item which is being Manufactured will have a Target Warehouse and other Items(Raw Materials) will have a Source Warehouse.**   
![](/files/voUKccc.png)  
*﻿Blue Dot: Item is being received.* *Orange Dot: Item is being issued.* 

<!-- page: erpnext/erpnext__manufacturing.md -->
---
title: "Manufacturing in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturing"
updated: "2026-02-26"
---

The Manufacturing module in ERPNext is designed to streamline and optimise the production process. It integrates with other modules to conduct various manufacturing operations effectively.

- **Workstations**: Represents the locations or equipment where production activities are carried out.
- **Job Cards**: Provides detailed instructions and tracking for each step in the production process.
- **Bill of Materials (BoM)**: Defines the components and raw materials needed to produce a finished product.
- **Work Orders**: Manages the creation, tracking, and execution of work orders based on MoMs.
- **Production Planning**: Helps in scheduling and optimizing production runs to meet demand and manage resources efficiently.
- **Quality Control**: Ensures products meet quality standards through inspections.
- **Inventory Management**: Integrates with the Inventory module to manage raw materials, work-in-progress, and finished goods.
- **Reporting and Analytics**: Offers insights into production performance, costs, and efficiency to support informed decision-making.

The Manufacturing module in ERPNext helps improve productivity, reduce costs, and enhance overall production efficiency by providing a unified platform for managing all aspects of the manufacturing process.
