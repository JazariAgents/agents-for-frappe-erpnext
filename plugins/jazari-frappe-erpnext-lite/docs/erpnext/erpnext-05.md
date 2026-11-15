<!-- Frappe documentation: erpnext, part 5 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__adjusting-withhold-amount.md -->
---
title: "Adjusting Withhold Amount"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/adjusting-withhold-amount"
updated: "2026-08-14"
---

Sometimes a customer pays less than the Sales Invoice because they retain part of the amount as withholding tax. You can record the bank receipt and the withheld amount in one Payment Entry while allocating the full invoice outstanding.



Consider Nova Industries, an electronics manufacturer and distributor. Northstar Retail has a $699 invoice. It pays $664.05 and withholds $34.95, or 5%. The accounting result is:


| Entry                      | Debit   | Credit  |
| -------------------------- | -------: | -------: |
| Bank                       | $664.05 |         |
| Withholding tax receivable | $34.95  |         |
| Customer receivable        |         | $699.00 |


The customer invoice is settled for $699 even though only $664.05 reaches the bank.

## Before you begin

Confirm that the customer actually deducted tax and obtain the supporting certificate or payment advice required by your jurisdiction. The unpaid difference must not be treated as withholding merely to close an invoice.

Prepare:

- A submitted [Sales Invoice](/erpnext/sales-invoice) with an outstanding amount.
- The customer's bank remittance amount.
- The confirmed withheld amount.
- A suitable asset account in the [Chart of Accounts](/erpnext/chart-of-accounts), such as Withholding Tax Receivable.
- The Cost Center required for the adjustment row.

The receivable account records tax credit expected from the authority or evidenced by the customer's certificate. Ask your accountant where it belongs in your chart and how it must be reconciled.

This procedure is different from configuring a [Tax Withholding Category](/erpnext/tax-withholding-category) for automatic supplier deductions or regional collection rules. Here, you are recording an amount the customer already withheld from its payment.

## Check the invoice outstanding

Open the Sales Invoice and confirm its current Grand Total and Outstanding Amount. Do not rely only on the original invoice value when earlier payments or credit notes may already be allocated.



[Screenshot on the live page: Sales Invoice total and outstanding amount before the payment]

The example invoice has $699 outstanding.

## Create a Payment Entry from the invoice

From the submitted invoice, select **Create &gt; Payment**. ERPNext opens a [Payment Entry](/erpnext/payment-entry) with Payment Type **Receive**, the Customer, receivable account, bank account, and invoice reference.

You can also create the Payment Entry from the list, but starting from the invoice reduces the chance of selecting the wrong party or reference.

Enter the amount that reached the bank. In this example, it is $664.05.



[Screenshot on the live page: Enter the amount actually received in the bank]

Do not enter $699 as the bank amount because the bank did not receive the $34.95 withheld by the customer.

## Allocate the full invoice outstanding

In **Payment References**, keep the Sales Invoice and allocate its full outstanding amount. Select the pencil icon to inspect or edit the child row.



[Screenshot on the live page: Open the invoice allocation row]

The example allocates $699, not $664.05. This tells ERPNext that the invoice is settled through two components: bank receipt plus withholding-tax receivable.



[Screenshot on the live page: Allocate the full $699 outstanding against the Sales Invoice]

The difference is:

`$699.00 allocated - $664.05 received = $34.95`

If the allocated amount automatically changes to match the Payment Amount, reopen the reference row and enter the full amount the payment and withholding jointly settle. This behavior has caused confusion for users expecting the difference to appear automatically.

## Add the withholding adjustment

Open **Deductions or Loss** and add a row in **Payment Deductions or Loss**. Use the pencil icon to edit the complete row.



[Screenshot on the live page: Open the deduction or loss row]

Enter:


| Field       | Value in the example                                                 |
| ----------- | -------------------------------------------------------------------- |
| Account     | Input Tax Credit, or the approved withholding-tax receivable account |
| Cost Center | Main, or the Cost Center required by your accounting policy          |
| Amount      | $34.95                                                               |
| Description | Customer withholding tax retained against the invoice                |


[Screenshot on the live page: Withholding account, amount, Cost Center, and description]

Use an asset account for customer-deducted tax when it represents recoverable or creditable tax. Do not use a supplier withholding liability account, an arbitrary expense account, or the customer receivable account itself unless your accountant has designed that treatment.

## Confirm the Payment Entry balances

After the adjustment:

- Paid Amount equals the bank receipt, $664.05.
- Total Allocated Amount equals the invoice settlement, $699.00.
- Payment Deductions or Loss equals $34.95.
- Difference Amount equals $0.00.

Save the draft and review all three components before submission. A non-zero Difference Amount means the entry is not balanced.

The older ERPNext example used a $20,000 invoice, a $19,600 bank receipt, and a $400 withholding adjustment. That produces the same pattern:

`$19,600 bank + $400 withholding receivable = $20,000 invoice allocation`

## Submit and verify the result

Submit the Payment Entry, then reopen the Sales Invoice. Its outstanding amount should reduce by the full allocation, not only the cash received.

Review the [General Ledger](/erpnext/general-ledger):

1. Bank is debited by the cash received.
2. Withholding tax receivable is debited by the amount retained.
3. Customer receivable is credited by the full invoice allocation.

Also review the customer's [Accounts Receivable](/erpnext/accounts-receivable) balance. The invoice should not remain partially outstanding when the withheld amount was validly accepted as settlement.

Reconcile the withholding-tax receivable account against certificates and statutory filings. A growing balance without supporting evidence can indicate missing certificates or incorrect adjustment entries.

## When not to use this method

Do not use this method for:

- A normal short payment that the customer still owes. Allocate only the cash and leave the balance outstanding.
- A commercial discount. Use an approved discount or write-off workflow and the correct account.
- Bank fees charged to your company. Use the bank-charge account supported by the [Bank Reconciliation](/erpnext/bank-reconciliation) process.
- Exchange differences. Use the appropriate [Exchange Gain or Loss](/erpnext/multi-currency-accounting) treatment.
- Supplier tax you are deducting while paying. Use the supplier withholding workflow described in Tax Withholding Category.

## Correcting a submitted adjustment

Do not edit a submitted Payment Entry directly. If the withholding amount, account, or allocation is wrong, cancel and amend the entry where permitted. If later evidence changes the treatment, use an approved accounting correction with a clear reference to the original documents.

Avoid posting an unrelated [Journal Entry](/erpnext/journal-entry) merely to force the invoice outstanding to zero. The correction should preserve party references and a traceable audit trail.

## Troubleshooting

### Difference Amount does not appear after reducing the payment

ERPNext may also reduce the reference allocation. Open the invoice reference row and set Allocated Amount to the total being settled by cash plus withholding.

### The invoice remains partially outstanding

Check that Allocated Amount equals the full amount settled and that the Payment Entry was submitted. The deduction row alone does not allocate the invoice.

### Difference Amount is not zero

Confirm that bank receipt plus adjustment equals allocated amount. Also check signs, exchange rates, and any other deduction rows.

### The withholding balance appears as an expense

The selected account may have the wrong root type or accounting purpose. Use the approved withholding-tax receivable account and correct the entry through the normal cancellation or adjustment process.

## Frequently asked questions

### Should I allocate the cash received or the full invoice amount?

Allocate the full amount settled by cash and withholding. Enter only the actual bank receipt in Payment Amount.

### Is customer withholding a write-off?

Not usually. A valid withholding amount is tax credit or receivable supported by statutory evidence, not an amount the business has simply forgiven.

### Can one Payment Entry settle several invoices with withholding?

Y

es. Allocate each invoice carefully and ensure the total withholding adjustment matches the customer's payment advice and certificates.

### Can I use the same account as supplier withholding?

Usually no. Customer-deducted tax is commonly an asset, while tax withheld from a supplier is commonly a liability. Confirm the account design with your accountant.

### What happens if the certificate arrives later?

Record the payment only when you have reasonable evidence of the deduction, then reconcile the receivable account when the certificate or statutory credit becomes available.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Sales Invoice](/erpnext/sales-invoice)
- [Tax Withholding Category](/erpnext/tax-withholding-category)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [General Ledger](/erpnext/general-ledger)
- [Accounts Receivable](/erpnext/accounts-receivable)

<!-- page: erpnext/erpnext__administrator.md -->
---
title: "Administrator"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/administrator"
updated: "2026-02-27"
---

**The 'Administrator' in ERPNext is above the System Manager and has all the rights and permissions for an ERPNext account.**

A System Manager also has permissions to most items in the system, but the Administrator has unrestricted access. The administrator ensures that the overall functioning of the ERPNext system meets the needs of the organisation.

1. If your ERPNext account is cloud-hosted with us (Frappe Technologies Pvt. Ltd.), then you can access the "Administrator" user via the Frappe Cloud Dashboard.
2. For cloud-hosted account, upgrades are managed from the backend. We reserve admin login credentials with us so that we can upgrade all the customer's ERPNext accounts from the backend.
3. Since on a single server, we may host many customer's ERPNext accounts, as a security measure, we cannot share the credentials for administrator account with any cloud-hosted user. (an exception would be if you purchase a large number of users and your account is exclusively hosted on one server).
4. For self-hosted on-premises accounts, the admin credentials are with the account user.

### Related Topics

1. [Adding Users](/erpnext/adding-users)
2. [Role and Role Profile](/erpnext/role-and-role-profile)
3. [Role Based Permissions](/erpnext/role-based-permissions)
4. [User Permissions](/erpnext/user-permissions)
5. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__advance-in-separate-party-account.md -->
---
title: "Advance in Separate Party Account | ERPNext Documentation"
description: "Post and allocate advances through a separate receivable or payable account in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/advance-in-separate-party-account"
updated: "2026-08-01"
---

Some organizations keep advances in a separate party account until an invoice is issued. Configure the account carefully so the advance remains tied to the Customer or Supplier and can be reclassified during allocation.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Advance in Separate Party Account

1. Create the separate receivable or payable account with the correct root type and account type.
2. Enable the relevant advance-account setting for the Company or transaction flow.
3. Record the advance against the party and the separate account.
4. When the invoice is posted, reconcile the advance and verify the reclassification entries.
5. Confirm both the party ledger and General Ledger after allocation.

[Screenshot on the live page: Advance in Separate Party Account in ERPNext]

## Important fields and what they mean


| Field                | What it controls                                          |
| -------------------- | --------------------------------------------------------- |
| Party Type and Party | Keeps the advance attributable to a Customer or Supplier. |
| Paid From or Paid To | Separate advance account used by the entry.               |
| Reference            | Order or other commercial commitment.                     |
| Unallocated Amount   | Advance still awaiting an invoice.                        |
| Account Currency     | Currency in which the advance account is maintained.      |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The advance is not available on the invoice

Confirm that the payment and invoice use the same party, Company, currency, and configured advance receivable or payable account. The separate advance feature must be enabled before the payment is posted, and the party's default advance account must be configured correctly.

### The advance remains in the separate account after allocation

Check whether reconciliation completed and review the generated ledger entries. A manual Journal Entry to an unrelated liability or asset account will not participate in the standard clearing workflow.

### Existing advances still use the normal receivable or payable account

Changing the setting does not rewrite historical entries. Apply the new configuration prospectively unless your accountant approves a controlled migration entry.

## Frequently asked questions

### Why use a separate party account for advances?

It presents customer advances as liabilities and supplier advances as assets instead of negative receivable or payable balances. Use it when that presentation matches your accounting policy.

### Can the setting be enabled after transactions already exist?

The setting can be enabled, but existing ledger entries retain their original accounts. Test reporting and reconciliation before changing the treatment on a live site.

### Can one advance be allocated to several invoices?

One advance can be allocated in parts to eligible invoices for the same party and account. The unused balance remains available until it is allocated or refunded.

### Does an Order have to exist before recording the advance?

An Order is not mandatory. Linking the payment to a Sales Order or Purchase Order improves traceability when the commercial commitment already exists.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__advance-payment-entry.md -->
---
title: "Advance Payment Entry | ERPNext Documentation"
description: "Record and later allocate customer or supplier advances in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/advance-payment-entry"
updated: "2026-07-31"
---

An advance is money received from a Customer or paid to a Supplier before the final invoice. Record it against the party, and optionally against an Order, so it remains traceable and can be allocated when the invoice is created.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Advance Payment Entry

1. Create a Payment Entry with the correct party and payment type.
2. Enter the actual amount, accounts, and bank reference.
3. Link a Sales Order or Purchase Order when the advance belongs to a specific commitment.
4. Submit the Payment Entry.
5. When the invoice is available, use Payment Reconciliation or the invoice payment workflow to allocate the advance.

[Screenshot on the live page: Advance Payment Entry in ERPNext]

## Important fields and what they mean


| Field                     | What it controls                                        |
| ------------------------- | ------------------------------------------------------- |
| Party                     | Customer or Supplier associated with the advance.       |
| Reference Document        | Optional Order that explains the advance.               |
| Unallocated Amount        | Advance still available for later invoices.             |
| Advance Taxes and Charges | Tax treatment required by the applicable configuration. |
| Reference No and Date     | External payment evidence.                              |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The advance does not appear on the invoice

Confirm that the submitted Payment Entry uses the same party, Company, receivable or payable account, and currency as the invoice. If it was linked to an Order, verify that the invoice was created from that Order. Otherwise use [Payment Reconciliation](/erpnext/payment-reconciliation) to allocate the available advance.

### The advance was posted to a separate liability or asset account and cannot be allocated

Standard allocation expects a compatible party receivable or payable account. If your accounting policy uses separate advance accounts, configure the supported separate-party-account feature correctly and test the clearing entries. A manual posting to an unrelated account will not automatically become an allocatable customer or supplier advance.

### The advance is linked to the wrong Order

If the Payment Entry is still a draft, correct the reference. If it is submitted, use the supported cancellation, amendment, or unreconciliation workflow. Do not allocate it to an unrelated invoice merely to clear the balance.

### The advance is not fully used by the final invoice

Allocate only the amount due. The remainder stays available for a future invoice or refund. Verify the party ledger and agree the treatment with the Customer or Supplier before returning or reallocating it.

## Frequently asked questions

### Must an advance be linked to a Sales Order or Purchase Order?

An advance can remain unallocated against the party when no Order exists. Linking it to an Order improves traceability and can make later allocation easier when the invoice is created from that Order.

### Can one advance be used against more than one invoice?

One advance can be used across eligible invoices. Allocate part of the available advance to each invoice. ERPNext keeps the unused balance available until it is allocated or refunded.

### Is a customer advance income when it is received?

Not merely because cash was received. Its accounting treatment depends on your chart of accounts, configuration, and applicable accounting policy. The final invoice recognizes the sale according to the configured accounts.

### Can an advance be refunded?

An advance can be refunded through a traceable payment or adjustment workflow that reverses the money movement and clears the party balance. Do not delete or overwrite the original advance.

### Can I receive an advance before creating the Customer or Supplier?

Create the party first. Payment Entry needs the correct party and account so the advance can later be found and allocated without manual cleanup.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__agriculture-module-in-erpnext.md -->
---
title: "Agriculture Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/agriculture-module-in-erpnext"
updated: "2026-07-04"
---

## Overview

The Agriculture module was created as an ERPNext domain app for farms and agriculture-focused organizations. It is intended to help users record crops and land, track agriculture activities, and maintain field-related observations such as plant, soil, water, weather, disease, and fertilizer information.

The app is available as a separate open-source repository under the Frappe organization. However, it should be evaluated carefully before use on a new ERPNext site.

## Maintenance And Compatibility Status

**Important:** The Agriculture app does not appear to be actively maintained at the same level as ERPNext core and other actively developed Frappe apps. The repository has no published releases, and users should not assume that it is compatible with the latest ERPNext or Frappe Framework versions.

If you plan to use it, test it on a staging site first and confirm compatibility with your exact ERPNext, Frappe Framework, and Python versions. For production use, be prepared to review the code, apply fixes, or maintain a fork if required.

## GitHub Repository

Source code: [github.com/frappe/agriculture](https://github.com/frappe/agriculture)

The repository describes the app as the Agriculture Domain for ERPNext.

## Basic Features

- **Crop records:** Maintain information related to crops grown by the organization.
- **Land records:** Track agricultural land or field information.
- **Plant analytics:** Record plant-related observations and measurements.
- **Soil, water, and weather tracking:** Maintain field-level environmental observations that may affect crop planning and operations.
- **Disease tracking:** Record crop or plant disease information for reference and follow-up.
- **Fertilizer tracking:** Track fertilizer-related information as part of agriculture operations.

## When To Use It

Consider this app only if you specifically need the agriculture domain objects and are comfortable validating or maintaining the app yourself. It may be useful as a starting point for custom agriculture workflows, but it should not be treated as a plug-and-play module for current ERPNext versions without testing.

## Installation

The repository README shows the standard Frappe app installation flow:

```
bench get-app agriculture
bench --site your-site-name install-app agriculture
```

Run these commands only on a development or staging bench until compatibility is confirmed.

## Recommended Approach

- Check the repository activity, open issues, and pull requests before installation.
- Install the app on a test site first.
- Run migrations and basic workflows before using it with real data.
- Confirm whether the DocTypes and reports meet your operational needs.
- If the app does not work with your ERPNext version, consider using it as a reference for a custom app instead of installing it directly in production.

## Related Link

- [Frappe Agriculture on GitHub](https://github.com/frappe/agriculture)

<!-- page: erpnext/erpnext__allocating-credit-note-and-payment.md -->
---
title: "Allocating a Credit Note and Payment | ERPNext Documentation"
description: "Allocate customer payments and credit notes against outstanding sales invoices with ERPNext Payment Reconciliation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/allocating-credit-note-and-payment"
updated: "2026-07-31"
---

Allocate a Credit Note or unallocated customer payment when the credit should settle a specific Sales Invoice. Allocation updates the outstanding amounts without creating another sale or payment.

## Before you begin

Confirm that the Sales Invoice, Credit Note, and Payment Entry are submitted for the same Customer, Company, currency, and receivable account. The credit or payment must still have an unallocated amount.

## Allocate with Payment Reconciliation

1. Search for **Payment Reconciliation**.
2. Select the Company, Party Type **Customer**, Customer, and receivable account.
3. Fetch unallocated payments and invoices.
4. Select the Credit Note or Payment Entry in the payments section.
5. Select the Sales Invoice in the invoices section.
6. Enter the amount to allocate.
7. Review the remaining unallocated and outstanding amounts.
8. Select **Reconcile**.

The Payment Reconciliation tool places open invoices and available payments or Credit Notes side by side. Select only the entries that should be matched before allocating the amount.



[Screenshot on the live page: Payment Reconciliation with open Sales Invoices and an unallocated customer payment]

You may allocate one payment across several invoices or combine several credits against one invoice, provided the allocation does not exceed the available or outstanding amount.

## Verify the result

Open the [Accounts Receivable](/erpnext/accounts-receivables) report and confirm:

- the Sales Invoice outstanding amount has reduced;
- the Credit Note or Payment Entry unallocated amount has reduced;
- the Customer's total balance is unchanged by the allocation itself.

Allocation matches existing debit and credit entries. It does not post new income, tax, stock, or cash movement.

## When to use a Journal Entry

Use a Journal Entry only when the accounting adjustment cannot be represented by Payment Reconciliation. Add the Customer as Party and select the correct Sales Invoice or Credit Note in **Reference Type** and **Reference Name**. Missing references leave the vouchers open even when the account balance appears correct.

## Troubleshooting

**The credit or invoice does not appear**

Check submission status, Customer, Company, currency, receivable account, and remaining unallocated or outstanding amount.

**The ledger balances but the invoice stays unpaid**

The entry probably lacks the invoice reference. Reconcile the payment or correct the referenced Journal Entry.

**The wrong allocation was made**

Use the supported unreconcile action where available, then reconcile the correct vouchers. Do not cancel unrelated sales documents.

## Related topics

- [Credit Note](/erpnext/credit-note)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounts Receivables](/erpnext/accounts-receivables)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__allow-over-delivery-billing-against-sales-order-upto-certain-limit.md -->
---
title: "Allow Over Delivery/Billing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/allow-over-delivery-billing-against-sales-order-upto-certain-limit"
updated: "2026-03-02"
---

When creating a Delivery Note, system validates if item's qty is same as in the Sales Order. If item's qty has been increased, you will get the validation message of over-delivery or receipt.

Considering the case fo sales, if you want to be able to deliver more items than mentioned in the Sales Order, you should update "Allow over delivery or receipt upto this percent" in the Item master.

[Screenshot on the live page: Itemised Limit Percentage]

When creating an invoice, item's rate is also validated based on the preceding transaction like Sales Order. This also applies when creating Purchase Receipt or Purchaes Invoice from Purchase Order. Updating "Allow over delivery or receipt upto this percent" will be affective in all sales and purchase transactions.

For example, if you have ordered 100 units of an item, and if item's over receipt percent is 50, then you are allowed to make Purchase Receipt for upto 150 units.

Update global value for "Allow over delivery or receipt upto this percent" from Stock Settings. Value updated here will be applicable for all the items.

1. Go to `Stock > Setup > Stock Settings`
2. Set `Limit Percentage`.
3. Save Stock Settings.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__alternative-finished-goods.md -->
---
title: "Alternative Finished Goods"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/alternative-finished-goods"
updated: "2026-08-28"
---

## **Problem**

In process industries (e.g. chemicals), a Work Order sometimes produces a sellable item that differs from the expected finished good, a different grade or specification identified during QC. It is not scrap but also not the expected finished good. 

## What is this feature?

With this feature you can, in one click, tell ERPNext: *"This Work Order actually produced Item B instead of Item A."* The system creates a stock entry that is **linked to the Work Order**, moves the stock from the planned item to the actual item, carries the production cost over, and shows the real output in production reports.

## When should you use it?

Use **Change Finished Item** when **all** of these are true:

- The Work Order is submitted and some quantity has already been produced.
- QC (or any inspection) found that the output is a **different but sellable item** — a different grade, purity, or specification.
- The actual item is one of the pre-approved alternatives of the planned item.

Do **not** use it when:

- The output is waste or scrap → use the normal scrap flow instead.
- You simply produced less than planned → use process loss.
- You want to repackage into different pack sizes → use a normal Repack Stock Entry.

## Real-life example

**Sunrise Chemicals** runs a Work Order to produce **100 kg of Epoxy Resin – Grade A**.

Production completes and 100 kg is booked into the Finished Goods warehouse. During QC, the lab finds that **20 kg** of the batch does not meet Grade A viscosity limits — but it fully meets **Grade B** specification, which the company also sells (at a lower price).

Without this feature, the store keeper would make a manual Repack entry that has no link to the Work Order — reports would forever say "100 kg Grade A produced", which is wrong.

With this feature, the supervisor opens the Work Order, clicks **Change Finished Item**, selects *Epoxy Resin – Grade B* and enters *20*. ERPNext:

- removes 20 kg of Grade A from the FG warehouse,
- adds 20 kg of Grade B in the FG warehouse **at the same production cost**,
- keeps the entry linked to the Work Order,
- and the **Work Order Summary** report now shows: `Grade A: 80, Grade B: 20`.

---

## One-time setup (Manager)

### Step 1 — Turn the feature on

Open **Manufacturing Settings** and enable **Allow Alternative Finished Goods** (in the *BOM and Production* tab), then save.



[Screenshot on the live page]

### Step 2 — Allow alternatives on the planned item

Open the **Item** you normally produce (e.g. *Epoxy Resin – Grade A*) and enable **Allow Alternative Item**, then save.

### Step 3 — Define the allowed grades

Create an **Item Alternative** record for each grade the process may produce:


| Field                 | Example value                                                    |
| --------------------- | ---------------------------------------------------------------- |
| Item Code             | Epoxy Resin – Grade A *(the planned item)*                       |
| Alternative Item Code | Epoxy Resin – Grade B *(the possible actual output)*             |
| Two-way               | Tick only if Grade B Work Orders can also be regraded to Grade A |


[Screenshot on the live page]



Setup is done. You never need to repeat this unless a new grade is introduced.

## Daily usage (Operator / Supervisor)

- **Finish production as usual.** Complete the Work Order's Manufacture entry so the produced quantity is booked.
- **Open the Work Order.** After QC identifies a grade change, open the Work Order and click the **Change Finished Item** button.

[Screenshot on the live page]

- **Fill the dialog.**

[Screenshot on the live page]

- **Actual Finished Item** - System will auto default when there's only one alternative or pick the grade QC approved (only pre-approved alternatives are shown).
- **Qty to Convert** - how much of the produced quantity is actually the other grade. The dialog shows how much is available to convert.

  

  
- **Create Stock Entry.** 
  - In the popup, you will see Create Stock Entry, click on it and ERPNext opens a ready-made draft Repack entry. Fill in the **batch / serial numbers** for both rows (the batch being consumed and the new batch being created), then **Submit**.

  
- **Check the report (optional).** Open **Work Order Summary** — the *Actual Finished Goods* column shows the true output

[Screenshot on the live page]

## Good to know

- **Cost is transferred automatically.** The actual item is valued at the same cost the Work Order produced — no manual rate entry needed.
- **You cannot convert more than was produced.** The system tracks earlier conversions and blocks anything above the remaining produced quantity.
- **Quantity in = quantity out.** The converted quantity and the new item's quantity must match. (For genuine quantity-changing operations, use a normal Repack entry.)
- **Partial conversions are fine.** You can convert 20 kg today and another 10 kg tomorrow, as long as the total stays within the produced quantity.
- **Wrong entry?** Cancel the conversion Stock Entry - stock and cost return to the planned item, and the converted quantity becomes available again.
- **Nothing changes if the feature is off.** The button and report column appear only when *Allow Alternative Finished Goods* is enabled in Manufacturing Settings.

---

<!-- page: erpnext/erpnext__amazon_integration.md -->
---
title: "Amazon SP-API Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/amazon_integration"
updated: "2026-03-06"
---

The Amazon Connector pulls Products and Sales Orders from the Amazon marketplace.

How to Setup Amazon SP-API Connector?
-------------------------------------

Amazon Connector is moved out from ERPNext and is available through a Frappe App on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)

### App Installation

* If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
* If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
* If you are self-hosting ERPNext you can install the app using Frappe bench. Refer to [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`

The repository for the app is hosted on GitHub: &lt;http://github.com/frappe/ecommerce_integrations/&gt;

### Setting Up Credentials in ERPNext

You can request the developer credentials from Amazon Seller Central once you are a registered seller on their website. For more details on the same, click [here](https://developer.amazonservices.com/).

#### 1. Setup SP-API Credentials

Enter the IAM ARN, Refresh Token, Client ID, Client Secret, AWS Access Key, AWS Secret Key and Country. [Screenshot on the live page: Credentials]  
  


#### 2. Set up Order Details

Set up Company, Warehouse, Parent Item Group, Price List, Customer Group, Territory, Customer Type and Account Group. The Account Group is used to hold commissions, taxes etc. that Amazon charges. [Screenshot on the live page: setup]  
  


#### 3. Setup Sync Configurations

Using the After Date, you can sync orders created after a particular date. In case you are importing a lot of historic data, it is suggested to start in the reverse chronological order of the After Date and import data in small chunks. [Screenshot on the live page: Syncing]After setting up all the configurations, click on Is Active and save the settings. You are now ready to use the integration.

#### 4. Amazon - ERPNext Item Mapping

Both ASIN and SellerSKU can be utilized to map Amazon items with corresponding ERPNext items. For instance, if you have pre-existing items in your system, created through other integrations, you can establish a custom field within the Item Master by using the Customize Form feature and setting the ASIN/SellerSKU as the value.

During the process of syncing orders from Amazon, the system will attempt to find the Item Code using the field configured to find the Item Code in the Amazon - ERPNext Item Mapping table. If the item is not found in the mapping table, you have the option to create a new item by checking the **Create Item If Not Exists** box.

[Screenshot on the live page: Screenshot from 2023-07-31 13-52-50]  


#### 5. Sync Orders

Click on this button to sync sales orders. Once this is successful you should see your Amazon Orders as Sales Orders in ERPNext. You can also set up a scheduler to sync orders automatically.


&gt; In case your developer account does not have access to personally identifiable information. The customer name would be stored as a combination of the BuyerName + &lt;Order ID&gt; or Marketplace email ID.
&gt; 
&gt; 

[Screenshot on the live page: Sales Order]  
  


### Note

The connector won't handle Order cancellation. If you cancel any order in Amazon then manually you have to cancel the respective Sales Order and other documents in ERPNext.

<!-- page: erpnext/erpnext__amending-purchase-order-after-submit.md -->
---
title: "Amending Purchase Order after Submit\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/amending-purchase-order-after-submit"
updated: "2026-03-02"
---

Rate and Qty in Purchase Order can now be amended after Submit using the `Update Items` button.

[Screenshot on the live page: Update Items]

To Update Rate and Qty in a Submitted Purchase Order, click on the `Update Items` button. A dialog will pop up to let you make the change.

[Screenshot on the live page: Update Items]

Please Note the following validations and usecases:

- Update Features checks if Purchase Order has Purchase Receipt and Purchase Invoice.
- Qty can be updated for un-received and for partially-received Purchase Order. For Purchase Order with completed Purchase Receipt, it cannot be updated.
- Rate can be updated for un-invoiced and partially-invoiced Purchase Order. For Purchase Order with submitted Purchase Invoice, it cannot be updated.

<!-- page: erpnext/erpnext__amending-sales-order-after-submit.md -->
---
title: "Amending Sales Order after Submit | ERPNext Documentation"
description: "Learn how to update item values or cancel and amend a submitted Sales Order in ERPNext while preserving linked transactions and the audit trail."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/amending-sales-order-after-submit"
updated: "2026-07-24"
---

After a [Sales Order](/erpnext/sales-order) is submitted, its core values are locked to protect the audit trail. ERPNext provides two ways to make a correction: use **Update Items** for permitted item-level changes, or cancel and amend the document when the change is broader.

## Before you begin

Check whether the Sales Order already has a submitted [Delivery Note](/erpnext/delivery-note), [Sales Invoice](/erpnext/sales-invoice), [Pick List](/erpnext/pick-list), or other linked transaction. Downstream documents determine which quantities and rates ERPNext can safely change.

Also confirm that you have permission to update or cancel submitted Sales Orders.

## Update item quantity, rate, or delivery date

Use this method when the submitted order is correct overall and only an allowed item value needs adjustment.

1. Open the submitted Sales Order.
2. Select **Update Items**, as highlighted.

[Screenshot on the live page: Update Items on a submitted Sales Order]

3. In the **Update Items** dialog, review the item row.
4. Use the highlighted pencil icon when you need to open the row editor.
5. Change the permitted **Delivery Date**, **Qty**, or **Rate**.
6. Select **Update**.

[Screenshot on the live page: Edit quantity and rate in the Update Items dialog]

ERPNext validates the change against linked transactions before saving it.

## Update rules and validations


| Change        | When it is normally allowed                          | Important limit                                                                         |
| ------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Quantity      | The order is undelivered or partly delivered         | The new quantity cannot conflict with quantity already delivered or otherwise fulfilled |
| Rate          | The order is not invoiced or is only partly invoiced | A submitted invoice can prevent changes that would conflict with its billed value       |
| Delivery Date | The order remains open and the revised date is valid | Linked fulfilment documents and permissions can restrict the update                     |


For a partly delivered order, keep the revised quantity at or above the quantity already delivered. For a partly invoiced order, keep the revised values consistent with the amount already billed. If ERPNext rejects the update, review the order's **Connections** tab and the validation message before deciding whether to amend the document.

## Cancel and amend the Sales Order

Use cancel and amend when **Update Items** does not cover the correction, such as changing the customer, company, currency, taxes, or another locked field.

1. Open the submitted Sales Order.
2. Review and handle linked documents first. You may need to cancel a dependent Delivery Note or Sales Invoice before ERPNext allows the order to be cancelled.
3. Select **Cancel** and confirm the action.
4. On the cancelled Sales Order, select **Amend**.
5. ERPNext creates a new draft linked to the cancelled order through **Amended From**.
6. Correct the required values, save, review, and submit the amended order.

The cancelled Sales Order remains in the audit trail. The amended draft receives a new document name based on the original series.

> Do not cancel a submitted order only to reduce an outstanding balance that the customer no longer wants. [Close the Sales Order](/erpnext/close-sales-order) instead.

## Choose the right action


| Situation                                                          | Action                                                           |
| ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Change an allowed item quantity, rate, or delivery date            | Update Items                                                     |
| Correct a locked header, customer, tax, currency, or company value | Cancel and Amend                                                 |
| Stop the remaining undelivered or unbilled balance                 | [Close](/erpnext/close-sales-order)                              |
| Fulfil or bill only part of the order now                          | [Partial Fulfilment](/erpnext/partial-fulfilment-of-sales-order) |
| Temporarily prevent further fulfilment                             | Hold                                                             |
| Reverse goods already delivered                                    | [Sales Return](/erpnext/sales-return)                            |


## Troubleshooting

### Update Items is not visible

Confirm that the Sales Order is submitted, not cancelled or closed, and that your role has the required permissions. An administrator can review [Role-Based Permissions](/erpnext/role-based-permissions).

### ERPNext will not accept the new quantity

The proposed quantity may be lower than a quantity already delivered, picked, manufactured, or otherwise reserved. Review linked documents in **Connections**.

### ERPNext will not accept the new rate

A submitted Sales Invoice may already use the original rate. Reverse or correct the invoice only when the accounting treatment requires it. Do not change submitted accounting records merely to force the order update.

### I cannot cancel the Sales Order

Cancel or unlink dependent transactions in reverse order where appropriate. For example, handle the Sales Invoice and Delivery Note before the Sales Order. Follow your organization's cancellation and accounting controls.

## Frequently asked questions

### Does Update Items create a new Sales Order?

No. It updates allowed values on the same submitted document and records the change in its version history.

### Does Amend overwrite the cancelled order?

No. ERPNext keeps the cancelled document and creates a linked draft.

### Can I reduce quantity after partial delivery?

Yes, provided the revised quantity does not fall below what has already been fulfilled and no linked transaction conflicts with the change.

### Should I amend an order when the customer cancels the remaining quantity?

Usually no. Complete the accepted delivery and billing, then close the remaining balance.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Close Sales Order](/erpnext/close-sales-order)
- [Short Close Multiple Orders](/erpnext/short-close-multiple-orders)
