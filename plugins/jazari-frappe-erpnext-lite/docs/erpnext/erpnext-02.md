<!-- Frappe documentation: erpnext, part 2 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__address.md -->
---
title: "Address | ERPNext Documentation"
description: "Learn how to create and link Addresses in ERPNext, choose billing and shipping defaults, apply country templates, and manage regional tax details."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/address"
updated: "2026-07-23"
---

An **Address** stores a physical or mailing location and can be linked to a [Customer](/erpnext/customer), [Supplier](/erpnext/supplier), Lead, shareholder, sales partner, [Warehouse](/erpnext/warehouse), or Company. One party can have several billing, shipping, office, and branch addresses.

Keep locations as linked Address records instead of creating duplicate Customers or Suppliers for each site.

![Billing Address for Summit Digital Stores with preferred billing status.](https://novacompanies.m.frappe.cloud/files/address-details.png)

## Before you begin

Confirm:

- the party or parties to link;
- whether the location is used for billing, shipping, or another purpose;
- which address should be preferred;
- the correct country and postal format; and
- any regional tax identifiers that belong to the location.

The selected Country determines the country-specific [Address Template](/erpnext/address-template) used when ERPNext renders the address.

## Create an Address

1. Open **CRM > Address** and select **Add Address**.
2. Enter the **Address Title** and select the **Address Type**.
3. Enter Address Line 1, optional Address Line 2, City/Town, County, State/Province, Country, and Postal Code.
4. Add phone, fax, email, or tax category when required.
5. Set preferred billing or shipping status when this is the normal location.
6. Add the party link.
7. Save the Address.

When created from a party, ERPNext normally derives a title such as `Party Name-Address Type`. A standalone Address needs a clear manual title.

## Create an Address from a party

1. Open the Customer or Supplier.
2. Select **Address & Contact**.
3. Select **New Address**.
4. Complete the location and save.

ERPNext adds the originating party link automatically. This route reduces link errors and is recommended for normal onboarding.

## Alternative ways to create Addresses

- Use [Data Import](/erpnext/data-import) for a controlled batch and include the correct Dynamic Link rows.
- Create an Address from a sales or purchase transaction when permitted.
- Use an approved integration when another system owns delivery locations.
- Create a standalone location and link it later.

## Important fields and what they mean


| Field                                 | What it controls                                                         |
| ------------------------------------- | ------------------------------------------------------------------------ |
| **Address Title**                     | Searchable label and part of the generated Address ID                    |
| **Address Type**                      | Classifies Billing, Shipping, Office, Personal, or another supported use |
| **Address Line 1 / 2**                | Street, building, suite, floor, or unit information                      |
| **City/Town, County, State/Province** | Regional location components used by templates and tax logic             |
| **Country**                           | Selects the country-specific Address Template and regional fields        |
| **Postal Code**                       | ZIP, PIN, or other postal identifier                                     |
| **Preferred Billing Address**         | Makes the Address the normal billing selection for the linked party      |
| **Preferred Shipping Address**        | Makes the Address the normal shipping selection                          |
| **Disabled**                          | Prevents new selection while retaining history                           |
| **Links**                             | Connects the Address to one or more supported parties or masters         |
| **Is Your Company Address**           | Identifies a facility belonging to your own Company                      |


## Link an Address to multiple parties

Use **Links** to review every party connected to the Address. Add another link only when the same physical location genuinely serves multiple parties.

![Links menu showing the Address connected to Summit Digital Stores.](https://novacompanies.m.frappe.cloud/files/address-linked-parties.png)

Do not link unrelated Customers merely because they share a building. Separate Address records preserve independent primary flags and tax details.

## Preferred billing and shipping addresses

A preferred billing Address can be fetched into [Sales Orders](/erpnext/sales-order), [Sales Invoices](/erpnext/sales-invoice), [Delivery Notes](/erpnext/delivery-note), purchase documents, and other supported transactions. The preferred shipping Address supplies the normal delivery destination.

One location may be both preferred billing and preferred shipping. For Summit Digital Stores, the Harbor Avenue office is billing and the Meridian Parkway warehouse is shipping.

Users can select another linked Address on a transaction. Submitted documents preserve the address text they used.

## Regional tax details

Regional apps can add fields and validation to Address. For India GST, store GSTIN and GST State on the Address—not only on the Customer or Supplier—because one party can have registrations in several states. Sales documents then fetch the registration belonging to the selected location.

For your own facilities, enable **Is Your Company Address** and link the [Company](/erpnext/company). Verify regional requirements against the installed compliance app and current law.

## Save and next steps

Address is saved rather than submitted. After saving:

- verify its Links menu;
- confirm preferred billing and shipping flags;
- select it on a test [Quotation](/erpnext/quotation) or transaction;
- check the formatted result; and
- disable obsolete locations instead of deleting history.

## Address types and availability


| Type or state       | Use                                           |
| ------------------- | --------------------------------------------- |
| **Billing**         | Invoice and statement location                |
| **Shipping**        | Delivery or receiving location                |
| **Office**          | General business location                     |
| **Preferred**       | Normal automatic selection for a linked party |
| **Disabled**        | Retained but unavailable for new selections   |
| **Company Address** | One of your organization's facilities         |


## Troubleshooting


| Problem                                | What to check                                                             |
| -------------------------------------- | ------------------------------------------------------------------------- |
| Wrong Address appears on a transaction | Review party links, preferred flags, and the selected transaction Address |
| Address formatting is wrong            | Check Country and the applicable Address Template                         |
| Address cannot be found                | Search the generated title and verify it is not disabled                  |
| Import creates unlinked Addresses      | Correct Link DocType and Link Name child rows                             |
| Regional tax fields are missing        | Check Country, installed regional app, and company configuration          |


## Frequently asked questions

### Can one party have several billing or shipping Addresses?

Yes. Mark the normal choice as preferred and select alternatives per transaction.

### Can an Address link to multiple Customers or Suppliers?

Yes, when the location is genuinely shared.

### Should I edit an old Address after it changes?

For a minor correction, edit it. For a materially different location, create a new Address and disable the obsolete one.

### Does editing an Address change submitted documents?

No. Submitted documents preserve the address text stored at posting.

### Where should regional tax registration be stored?

Use the Address when the registration belongs to a location, following the relevant regional app.

## Related topics

- [Customer](/erpnext/customer)
- [Contact](/erpnext/contact)
- [Address Template](/erpnext/address-template)
- [Company](/erpnext/company)

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



![Sales Invoice total and outstanding amount before the payment](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-sales-invoice-outstanding.png)

The example invoice has $699 outstanding.

## Create a Payment Entry from the invoice

From the submitted invoice, select **Create &gt; Payment**. ERPNext opens a [Payment Entry](/erpnext/payment-entry) with Payment Type **Receive**, the Customer, receivable account, bank account, and invoice reference.

You can also create the Payment Entry from the list, but starting from the invoice reduces the chance of selecting the wrong party or reference.

Enter the amount that reached the bank. In this example, it is $664.05.



![Enter the amount actually received in the bank](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-payment-entry-bank-amount.png)

Do not enter $699 as the bank amount because the bank did not receive the $34.95 withheld by the customer.

## Allocate the full invoice outstanding

In **Payment References**, keep the Sales Invoice and allocate its full outstanding amount. Select the pencil icon to inspect or edit the child row.



![Open the invoice allocation row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-payment-entry-reference-row.png)

The example allocates $699, not $664.05. This tells ERPNext that the invoice is settled through two components: bank receipt plus withholding-tax receivable.



![Allocate the full $699 outstanding against the Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-payment-entry-reference-fields.png)

The difference is:

`$699.00 allocated - $664.05 received = $34.95`

If the allocated amount automatically changes to match the Payment Amount, reopen the reference row and enter the full amount the payment and withholding jointly settle. This behavior has caused confusion for users expecting the difference to appear automatically.

## Add the withholding adjustment

Open **Deductions or Loss** and add a row in **Payment Deductions or Loss**. Use the pencil icon to edit the complete row.



![Open the deduction or loss row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-payment-entry-deduction-row.png)

Enter:


| Field       | Value in the example                                                 |
| ----------- | -------------------------------------------------------------------- |
| Account     | Input Tax Credit, or the approved withholding-tax receivable account |
| Cost Center | Main, or the Cost Center required by your accounting policy          |
| Amount      | $34.95                                                               |
| Description | Customer withholding tax retained against the invoice                |


![Withholding account, amount, Cost Center, and description](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-adjusting-withhold-amount-payment-entry-deduction-fields.png)

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

![Advance in Separate Party Account in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-04-payment-entry-party-amount.png)

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

![Advance Payment Entry in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-04-payment-entry-party-amount.png)

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



![Payment Reconciliation with open Sales Invoices and an unallocated customer payment](https://novacompanies.m.frappe.cloud/files/sales-receivables-allocating-credit-note-and-payment-payment-reconciliation.png)

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

![Itemised Limit Percentage](/files/limit-1.png)

When creating an invoice, item's rate is also validated based on the preceding transaction like Sales Order. This also applies when creating Purchase Receipt or Purchaes Invoice from Purchase Order. Updating "Allow over delivery or receipt upto this percent" will be affective in all sales and purchase transactions.

For example, if you have ordered 100 units of an item, and if item's over receipt percent is 50, then you are allowed to make Purchase Receipt for upto 150 units.

Update global value for "Allow over delivery or receipt upto this percent" from Stock Settings. Value updated here will be applicable for all the items.

1. Go to `Stock > Setup > Stock Settings`
2. Set `Limit Percentage`.
3. Save Stock Settings.

![](/files/TGPrUJY.png)

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



![](/files/Screenshot 2026-08-28 at 12.15.17 PM.webp)

### Step 2 — Allow alternatives on the planned item

Open the **Item** you normally produce (e.g. *Epoxy Resin – Grade A*) and enable **Allow Alternative Item**, then save.

### Step 3 — Define the allowed grades

Create an **Item Alternative** record for each grade the process may produce:


| Field                 | Example value                                                    |
| --------------------- | ---------------------------------------------------------------- |
| Item Code             | Epoxy Resin – Grade A *(the planned item)*                       |
| Alternative Item Code | Epoxy Resin – Grade B *(the possible actual output)*             |
| Two-way               | Tick only if Grade B Work Orders can also be regraded to Grade A |


![](/files/Screenshot 2026-08-28 at 12.26.21 PM.webp)



Setup is done. You never need to repeat this unless a new grade is introduced.

## Daily usage (Operator / Supervisor)

- **Finish production as usual.** Complete the Work Order's Manufacture entry so the produced quantity is booked.
- **Open the Work Order.** After QC identifies a grade change, open the Work Order and click the **Change Finished Item** button.

![](/files/Screenshot 2026-08-28 at 12.25.21 PM.webp)

- **Fill the dialog.**

![](/files/imagefe13aa.webp)

- **Actual Finished Item** - System will auto default when there's only one alternative or pick the grade QC approved (only pre-approved alternatives are shown).
- **Qty to Convert** - how much of the produced quantity is actually the other grade. The dialog shows how much is available to convert.

  

  
- **Create Stock Entry.** 
  - In the popup, you will see Create Stock Entry, click on it and ERPNext opens a ready-made draft Repack entry. Fill in the **batch / serial numbers** for both rows (the batch being consumed and the new batch being created), then **Submit**.

  
- **Check the report (optional).** Open **Work Order Summary** — the *Actual Finished Goods* column shows the true output

![](/files/Screenshot 2026-08-28 at 12.31.40 PM.webp)

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

Enter the IAM ARN, Refresh Token, Client ID, Client Secret, AWS Access Key, AWS Secret Key and Country. ![Credentials](/files/Credentials.png "Credentials.png")  
  


#### 2. Set up Order Details

Set up Company, Warehouse, Parent Item Group, Price List, Customer Group, Territory, Customer Type and Account Group. The Account Group is used to hold commissions, taxes etc. that Amazon charges. ![setup](/files/Screenshot from 2023-07-31 13-51-36.png "setup.png")  
  


#### 3. Setup Sync Configurations

Using the After Date, you can sync orders created after a particular date. In case you are importing a lot of historic data, it is suggested to start in the reverse chronological order of the After Date and import data in small chunks. ![Syncing](/files/Screenshot from 2023-07-31 13-45-15.png "Syncing.png")After setting up all the configurations, click on Is Active and save the settings. You are now ready to use the integration.

#### 4. Amazon - ERPNext Item Mapping

Both ASIN and SellerSKU can be utilized to map Amazon items with corresponding ERPNext items. For instance, if you have pre-existing items in your system, created through other integrations, you can establish a custom field within the Item Master by using the Customize Form feature and setting the ASIN/SellerSKU as the value.

During the process of syncing orders from Amazon, the system will attempt to find the Item Code using the field configured to find the Item Code in the Amazon - ERPNext Item Mapping table. If the item is not found in the mapping table, you have the option to create a new item by checking the **Create Item If Not Exists** box.

![Screenshot from 2023-07-31 13-52-50](/files/Screenshot from 2023-07-31 13-52-50.png "Screenshot from 2023-07-31 13-52-50.png")  


#### 5. Sync Orders

Click on this button to sync sales orders. Once this is successful you should see your Amazon Orders as Sales Orders in ERPNext. You can also set up a scheduler to sync orders automatically.


&gt; In case your developer account does not have access to personally identifiable information. The customer name would be stored as a combination of the BuyerName + &lt;Order ID&gt; or Marketplace email ID.
&gt; 
&gt; 

![Sales Order](/files/Sales Order.png "Sales Order.png")  
  


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

![Update Items](/files/po-update-items.png)

To Update Rate and Qty in a Submitted Purchase Order, click on the `Update Items` button. A dialog will pop up to let you make the change.

![Update Items](/files/po-update-items-rate-and-qty.gif)

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

![Update Items on a submitted Sales Order](https://novacompanies.m.frappe.cloud/files/update-items-button.png)

3. In the **Update Items** dialog, review the item row.
4. Use the highlighted pencil icon when you need to open the row editor.
5. Change the permitted **Delivery Date**, **Qty**, or **Rate**.
6. Select **Update**.

![Edit quantity and rate in the Update Items dialog](https://novacompanies.m.frappe.cloud/files/update-items-dialog.png)

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

<!-- page: erpnext/erpnext__applying-discount.md -->
---
title: "Apply Discounts to Sales Transactions | ERPNext Documentation"
description: "Apply item-level and transaction-level discounts in ERPNext and understand how discounts affect net rates, taxes, totals, and accounting."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/applying-discount"
updated: "2026-07-25"
---

ERPNext supports discounts on an individual item or on the transaction total. Use a manual discount for a one-off commercial decision. Use a [Pricing Rule](/erpnext/pricing-rule), [Promotional Scheme](/erpnext/promotional-scheme), or [Coupon Code](/erpnext/coupon-code) when eligibility should be evaluated automatically.

## Before you begin

Confirm:

- The Item has an applicable [Item Price](/erpnext/item-price).
- The transaction uses the intended [Price List](/erpnext/price-lists).
- The user may edit discount fields.
- Your tax and discount-accounting policy is configured.

## Apply a discount to one item

1. Create a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice).
2. Add the Item.
3. Select the highlighted pencil icon to open the full row editor.
4. Expand **Discount and Margin**.
5. Enter either **Discount (%)** or **Discount Amount**.
6. Review the resulting Rate, Net Rate, and Amount.
7. Save.

![A Sales Order item row with the pencil icon highlighted.](https://novacompanies.m.frappe.cloud/files/discount-item-pencil.png)

![The item row editor with Discount Percentage and Discount Amount visible.](https://novacompanies.m.frappe.cloud/files/discount-item-fields-v2c94055.png)

Item-level discounts are calculated against the Price List Rate. Use them when different lines require different discounts.

## Apply an additional discount to the transaction

1. Open the **Additional Discount** section.
2. Set **Apply Additional Discount On** to Net Total or Grand Total.
3. Enter an **Additional Discount Percentage** or **Additional Discount Amount**.
4. Review taxes, Net Total, Grand Total, and rounding before submission.

![The expanded Additional Discount section with the calculation basis and percentage visible.](https://novacompanies.m.frappe.cloud/files/discount-additional-section-v2e41c13.png)

### Discount on Net Total

ERPNext distributes the discount across eligible item net values before calculating totals. This changes item Net Rate and Net Amount, which can also change taxes calculated on those values.

### Discount on Grand Total

ERPNext applies the discount with reference to the total after taxes and charges. The system recalculates the relevant item and tax amounts so the document remains internally consistent.

Test the result with your actual tax templates. Inclusive taxes, charge types, rounding, and accounting configuration can affect the displayed breakdown.

## Choose the right discount method


| Requirement                                         | Recommended method                      |
| --------------------------------------------------- | --------------------------------------- |
| One item needs a one-time reduction                 | Item Discount (%) or Discount Amount    |
| The complete transaction needs a one-time reduction | Additional Discount                     |
| A condition should apply automatically              | Pricing Rule                            |
| Several quantity or amount slabs are required       | Promotional Scheme                      |
| A website shopper enters a code                     | Coupon Code                             |
| A free item is offered                              | Product Discount Pricing Rule           |
| A sales price needs a markup                        | [Adding Margin](/erpnext/adding-margin) |


## Discount accounting

By default, a discount changes the net revenue represented by item lines. If your accounting policy requires discounts to be posted separately, review **Enable Discount Accounting for Selling** in [Selling Settings](/erpnext/selling-settings) and configure the required accounts.

Confirm the resulting General Ledger entries in a test transaction before adopting the setting. Do not assume that a visual discount field always posts to a separate discount account.

## Troubleshooting


| Problem                                      | What to check                                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Discount fields are unavailable              | Open the child-row editor and confirm user permissions                                         |
| A manual value is replaced                   | Review Pricing Rules and re-fetch behavior                                                     |
| The final total is unexpected                | Check whether the discount applies on Net Total or Grand Total, then review taxes and rounding |
| The document is discounted twice             | Look for an automatic Pricing Rule plus a manual item or additional discount                   |
| Ledger entries do not use a discount account | Review discount-accounting settings and account configuration                                  |


## Frequently asked questions

### Can I apply both an item discount and an additional discount?

Yes. ERPNext applies both, so review the effective discount and approval policy carefully.

### Can I enter a fixed discount instead of a percentage?

Yes. Item rows and the Additional Discount section support amount-based discounts where available.

### Does a discount change the Price List Rate?

No. Price List Rate remains the reference rate. The transaction's Rate and Net Rate reflect the discount.

### Can ERPNext apply discounts automatically?

Yes. Use Pricing Rules or Promotional Schemes for repeatable conditions.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Coupon Code](/erpnext/coupon-code)
- [Adding Margin](/erpnext/adding-margin)
- [Selling Settings](/erpnext/selling-settings)

<!-- page: erpnext/erpnext__appointment-booking-settings.md -->
---
title: "Appointment Booking Settings | ERPNext Documentation"
description: "Configure ERPNext Appointment Booking Settings for availability, calendar scheduling, and customer bookings."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/appointment-booking-settings"
updated: "2026-07-23"
---

You can find all settings related to booking appointments in Appointment Booking Settings.

![Appointment Booking Settings](/files/appointment-booking-settings.png)

## Enable Appointment scheduling

This checkbox will enable appointment scheduling and also enable the /book_appointment Route for website users (your customers). Your customers will see a portal view. To know more, visit the [Appointment Page](/erpnext/appointment)

## Agent Details

In this section, you can add details about agents, such as their working hours and holidays.

### Availability of Slots

Here you can set the timing in which your agents are available to attend an appointment. This is set per day of the week. Each row represents a continuous block of time, you can have multiple entries for each day of the week.

For example if your agents work Monday to Friday, 9am to 5pm but with a lunch break at 1.30 for half and hour. You will need to create two entries for each day. One from 9am to 1.30pm and another from 2pm to 5pm.

### Agents

This is the list of agents which will be **autoassigned** to appointments. The number of appointments which can exist in one timeslot also depends upon the number employees in this list.

### Holiday list

You can link a (holiday list)[[https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list]](https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list]) here to apply to the appointment schedule. If the day is a holiday, scheduling an appointment on that day won't be allowed.

## Appointment Details

This section contains details about the appointment themselves.

### Appointment Duration in minutes

The duration of appointment in minutes. This is used to calculate appointment timeslots for the web portal. Changing this does not affect the appointments created before the change.

### Notify Via Email

Enabling this checkbox will send an email to the participants of the appointments i.e. your employee and the customer on the day of the appointment. Changing this checkbox does not affect the appointments created before the change.

### Number of days appointment can be books in advance

This is the number of days the appointment can be booked in advance. If the Holiday List provided above ends before the date calculated using this number, appointment scheduling will be stopped at the end of holiday list end.

## Success settings

### Success Redirect URL

This is the URL where the user will be redirected on creation of successful appointment creation via Web Portal. This redirect will not occur when creating appointments from within Desk UI.  
Leave blank for home. This is relative to site URL, for example "about" will redirect to "[https://yoursitename.com/about](https://yoursitename.com/about)"

<!-- page: erpnext/erpnext__appointment.md -->
---
title: "Appointment | ERPNext Documentation"
description: "Learn how to schedule and manage customer Appointments in ERPNext CRM."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/appointment"
updated: "2026-07-23"
---

**An appointment is a prearranged meeting between a Lead and an Employee of your Company.**

Appointment document type can be used to schedule and manage interaction with a [Lead](/erpnext/lead) or an [Opportunity](/erpnext/opportunity).

To access Appointment list, go to:

> Home > CRM > Sales Pipeline > Appointment

## Prerequisites

- [Appointment Booking Settings](/erpnext/appointment-booking-settings)
- [Holiday List](/hr/holiday-list)
- [Employee](/hr/employee)
- [Lead](/erpnext/lead)
- [Email](/erpnext/email-account)

## How to create an Appointment

- Go to Appointment list, select New
- Select scheduled time of the appointment
- Enter customer details
- In linked documents, if you have already created a Lead for the Customer you can set it here. Otherwise the system will automatically create a new lead with the customer details from previous step.
- Save.[New Appointment](/files/new-appointment.png)

### Creating appointments via website

Your Customers/Leads can create appointment using the webpage yoursitename.com/book_appointment.

First they need to set a date, time.

![Appointment Webform](/files/appointment-webform.png)

Then, add more details:

![Appointment Details](/files/appointment-details.png)

It'll match the customer email with leads in the system and if one is found, it is linked with the document.  
If no lead is found, the appointment is marked as "Unverified" and an email is sent to the customer to confirm their email

## Features

### Autoassign

Appointments are automatically assigned to employees as per the Agents list in [Appointment Booking Settings](/erpnext/appointment-booking-settings). The agent with the least number of assignments for the day of the appointment and who is free in the scheduled time is assigned to the appointment.

### Email confirmation

If there is no matching lead in your system, an email will be sent to the email address in the appointment to confirm if the email address is valid. Upon confirmation, a new Lead will also be created in the system along with the Appointment.

<!-- page: erpnext/erpnext__asset-capitalization.md -->
---
title: "Asset Capitalization | ERPNext Documentation"
description: "Combine stock, existing assets, and service costs into a new or composite ERPNext Asset."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-capitalization"
updated: "2026-08-15"
---

Imagine Nova Industries builds a testing machine using purchased components, technician time, and installation services. During construction, those costs are collected separately. Once the machine is ready, the company needs to combine the qualifying costs into one fixed asset.



Asset Capitalization gathers those costs and transfers them to the completed Asset. It shows how the final value was built and prevents the company from treating a long-term asset as an immediate operating expense.

## Before you begin

Confirm the target fixed-asset Item and category, source assets, available stock, service expense accounts, Finance Book, posting date, and capitalization policy.

## Define the target

1. Create an Asset Capitalization.
2. Select the company and posting date.
3. Choose a target Item and enter a recognizable target Asset Name, or select an eligible composite target Asset.
4. Select the Finance Book when required.

![Target Asset details in ERPNext Asset Capitalization](https://novacompanies.m.frappe.cloud/files/19-asset-capitalization-target.png)

## Add source costs

Add stock items, consumed assets, and service expenses. The example combines an existing conveyor with setup services. Use the pencil icon whenever a child row needs account, warehouse, quantity, rate, or cost-center detail.

![Consumed asset and service cost tables in Asset Capitalization](https://novacompanies.m.frappe.cloud/files/20-asset-capitalization-costs.png)

## Submit and verify

ERPNext reduces or updates the source values according to the transaction and capitalizes the total into the target. Verify the target Asset, source Asset statuses, stock impact, Journal Entry or Stock Ledger effect, and future depreciation schedule.

![Asset report used to verify capitalized value](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### The target Asset is not eligible

A selected existing target may need to be a Composite Asset. Otherwise create a new target from the fixed-asset Item.

### A service row cannot be saved

Provide the Item, expense account, quantity, rate, UOM, and cost center required by the row.

### Total value is zero

Add valid source rows and allow ERPNext to calculate their amounts before submission.

## Frequently asked questions

### Can I capitalize only services?

A valid capitalization can include qualifying services, but the target and accounting treatment must still satisfy the organization's policy.

### Can an existing Asset be consumed?

In ERPNext, yes, through the consumed-assets table when the workflow and target asset type permit it.

### Does capitalization immediately start depreciation?

Depreciation follows the target Asset's available-for-use date and Finance Book schedule.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-category.md -->
---
title: "Asset Category | ERPNext Documentation"
description: "Configure ERPNext Asset Categories with depreciation defaults, Finance Books, and company-specific fixed-asset accounts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-category"
updated: "2026-08-15"
---

Imagine Nova Industries buys 100 employee laptops over the next two years. If the accountant has to choose the useful life, depreciation method, and ledger accounts separately for every laptop, the records may become inconsistent and mistakes will be hard to find.



An Asset Category solves this by storing one reusable accounting policy for similar assets. Nova Industries can create an **IT Equipment** category once, then use the same depreciation and account defaults for every laptop added later.

## Before you begin

Confirm the company [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) contains a fixed-asset account, accumulated depreciation account, depreciation expense account, and capital work in progress account when CWIP is used. Create any required [Finance Books](https://docs.frappe.io/erpnext/finance-book) first.

## Create an Asset Category

1. Open **Asset Category** and select **Add Asset Category**.
2. Enter a clear name such as **IT Equipment** or **Production Equipment**.
3. Enable **Capital Work in Progress Accounting** when purchases should remain in CWIP until the asset becomes available for use.
4. Enable **Non Depreciable Category** only for categories such as land where depreciation does not apply.

![Asset Category depreciation options for IT Equipment](https://novacompanies.m.frappe.cloud/files/02-asset-category-overview.png)

## Set depreciation defaults by Finance Book

Add one row for every reporting basis you need. Nova Industries uses Straight Line for Statutory Reporting and Double Declining Balance for Management Reporting. Open the row editor with the pencil icon when you need fields that are not visible in the grid.

![Finance Book depreciation defaults in an ERPNext Asset Category](https://novacompanies.m.frappe.cloud/files/03-asset-category-finance-books.png)


| Field                             | What it means                                                              |
| --------------------------------- | -------------------------------------------------------------------------- |
| **Finance Book**                  | The reporting basis that owns this depreciation policy.                    |
| **Depreciation Method**           | How ERPNext spreads the depreciable value.                                 |
| **Frequency**                     | Months between scheduled depreciation entries.                             |
| **Total Number of Depreciations** | Number of scheduled postings across the useful life.                       |
| **Salvage Value Percentage**      | Expected residual value at the end of useful life.                         |
| **Daily Pro Rata**                | Calculates depreciation by actual days rather than equal periodic amounts. |
| **Shift Based**                   | Allows the depreciation amount to follow machine utilization by shift.     |


## Set company accounts

Each company row determines where acquisition, depreciation, and CWIP entries post. Do not use an inventory account as the Fixed Asset Account.

![Company accounting defaults for an ERPNext Asset Category](https://novacompanies.m.frappe.cloud/files/04-asset-category-accounts.png)


| Field                                | What it means                                                 |
| ------------------------------------ | ------------------------------------------------------------- |
| **Fixed Asset Account**              | Balance Sheet account that holds the capitalized asset value. |
| **Accumulated Depreciation Account** | Contra-asset account that accumulates depreciation.           |
| **Depreciation Expense Account**     | Profit and Loss account charged when depreciation is booked.  |
| **Capital Work in Progress Account** | Temporary asset account used before capitalization.           |


## Troubleshooting

### The Asset has the wrong depreciation defaults

Correct the category for future assets. For an existing draft Asset, reload or update the Finance Book rows before submission.

### ERPNext asks for an account during purchase or capitalization

Check that the category contains an Accounts row for the transaction company and that every linked account belongs to that company.

## Frequently asked questions

### Can two categories use the same accounts?

In ERPNext, yes. Categories may share accounts while keeping different useful lives or depreciation methods.

### Can the same category have two Finance Books?

In ERPNext, yes. Add one row per Finance Book when statutory and management depreciation differ.

### Does changing a category rewrite submitted Asset schedules?

Do not assume it will. Review affected Asset and Asset Depreciation Schedule records explicitly before relying on new defaults.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-depreciation.md -->
---
title: "Depreciation | ERPNext Documentation"
description: "Understand how ERPNext calculates, schedules, and posts fixed-asset depreciation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-depreciation"
updated: "2026-08-15"
---

Imagine you are an accountant at Nova Industries and your team buys laptops for $60,000. Would you show the full $60,000 as an expense in the first year even though the laptops are expected to be used for five years? That would make the first year's expense look unusually high and the next four years look too low.



Depreciation spreads the cost across the periods in which the assets are used. ERPNext creates a schedule and posts part of the cost at each interval, so the accounts show a more realistic expense and the remaining value of the laptops.

## Depreciation methods in brief

The method decides how quickly the asset's cost becomes an expense. Assume an asset costs $50,000, should be worth $5,000 at the end of five years, and therefore has a depreciable value of $45,000.


| Method                       | How the expense is spread                                                | When it is useful                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Straight Line**            | Spreads $45,000 evenly, or $9,000 per year for five years.               | The asset provides a similar benefit each year, such as office furniture.                               |
| **Double Declining Balance** | Records a larger expense in the early years and a smaller expense later. | The asset loses value or productivity quickly when new, such as some machinery or technology equipment. |
| **Written Down Value**       | Applies a fixed percentage to the asset's opening book value each year.  | The accounting or tax policy specifies depreciation as a percentage of carrying value.                  |
| **Manual**                   | Uses the dates and amounts entered by the accountant.                    | A contract, valuation, or special policy requires a custom schedule.                                    |


See [Depreciation Methods](https://docs.frappe.io/erpnext/asset-depreciation-methods) for worked calculations and year-by-year comparisons.

## Calculation inputs


| Field                                | What it means                                         |
| ------------------------------------ | ----------------------------------------------------- |
| **Net Purchase Amount**              | Starting capitalized value.                           |
| **Expected Value After Useful Life** | Residual amount not depreciated.                      |
| **Depreciable Value**                | Net purchase amount less expected residual value.     |
| **Method**                           | Pattern used to allocate depreciation.                |
| **Frequency**                        | Months between entries.                               |
| **Number of Depreciations**          | Number of scheduled postings.                         |
| **Available for Use Date**           | Operational start date that controls schedule timing. |


## Ledger impact

A submitted depreciation entry debits Depreciation Expense and credits Accumulated Depreciation. The original fixed-asset cost remains visible while accumulated depreciation grows.



The submitted schedule below belongs to Nova Industries' $48,000 NovaPack labeler. Each $760 monthly row has produced a linked depreciation Journal Entry, while future rows remain unposted.

![Submitted Asset Depreciation Schedule with posted Journal Entries](https://novacompanies.m.frappe.cloud/files/26-asset-depreciation-schedule-v2.png)

The Asset Depreciation Ledger then shows how the monthly expense increases accumulated depreciation and reduces the asset's carrying value.

![Asset Depreciation Ledger with seven posted entries](https://novacompanies.m.frappe.cloud/files/22-asset-depreciation-ledger-v2.png)

## Troubleshooting

### No depreciation schedule was created

Confirm Calculate Depreciation is enabled and at least one complete Finance Book row exists.

### A scheduled entry did not post

Check Accounts Settings, open periods, account defaults, posting permissions, and the schedule's posting status.

## Frequently asked questions

### Does depreciation start on the purchase date?

Not necessarily. It normally follows the Available for Use Date and schedule configuration.

### Can I post depreciation manually?

Use the Manual method or manage entries deliberately when automatic schedules do not match the policy.

### Does depreciation change inventory value?

Fixed-asset depreciation affects fixed-asset accounting, not stock valuation.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-location.md -->
---
title: "Asset Location | ERPNext Documentation"
description: "Build an ERPNext Asset Location tree and use it to track the physical position of company assets."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-location"
updated: "2026-08-15"
---

Imagine a Nova Industries employee reports that a company laptop is missing. The Asset record proves that the company owns it, but the support team still needs to know whether it was last kept at Nova Headquarters, sent to the Service Workshop, or assigned to another office.



Asset Locations create a simple map of where company assets are kept. When the location is updated through an Asset Movement, the team can find equipment faster and can also see where it was kept earlier.

## Create the location tree

1. Open **Asset Location** in Tree view.
2. Create a group such as **Nova Facilities**.
3. Add operational locations such as **Nova Headquarters**, **Packaging Floor**, and **Service Workshop** below it.
4. Use [Asset Movement](https://docs.frappe.io/erpnext/asset-movement) when an asset changes location so the history remains auditable.

![ERPNext Asset Location tree for Nova Industries facilities](https://novacompanies.m.frappe.cloud/files/05-asset-location-tree.png)


| Field                      | What it means                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Location Name**          | The name users will select on Asset and Asset Movement records.                                                             |
| **Parent Location**        | The group under which the location appears.                                                                                 |
| **Is Group**               | Allows the location to contain child locations. Do not assign an asset to a broad group when a usable leaf location exists. |
| **Area and UOM**           | Optional physical area information.                                                                                         |
| **Latitude and Longitude** | Optional coordinates for map-based identification.                                                                          |


## Keep locations useful

Choose one consistent level of detail. For office assets, a site or floor may be enough. For production equipment, a line or work area may be more useful. When a site closes, move its assets first, then stop using the old location rather than erasing history.

## Troubleshooting

### A new location does not appear in the Link field

Confirm it is saved as a usable location and not only as an unintended group. Reload the form after changing the tree.

### The Asset still shows the old location

Submit the Asset Movement. Saving a draft movement does not complete the transfer.

## Frequently asked questions

### Is Asset Location the same as Warehouse?

In ERPNext, no. Warehouse tracks inventory quantities. Asset Location tracks the physical position of fixed assets.

### Can an asset be assigned to an employee and a location?

In ERPNext, yes. Asset Movement can track custody and location together, depending on the selected purpose.

### Does a location change affect the ledger?

In ERPNext, no. A location transfer is operational and does not change asset value.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance-log.md -->
---
title: "Asset Maintenance Log | ERPNext Documentation"
description: "Complete ERPNext Asset Maintenance Logs with work performed, dates, status, and certificates."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance-log"
updated: "2026-08-15"
---

Imagine a technician completes the monthly inspection of a Nova Industries packaging machine. The schedule says the work was due, but the company still needs proof of what was done, when it was completed, and whether the machine had a problem.



An Asset Maintenance Log records the actual maintenance event. It turns a planned task into a dated service history that the operations and audit teams can check later.

## Open the planned log

Use the Maintenance Log section of the [Asset Maintenance](https://docs.frappe.io/erpnext/asset-maintenance) record or open the Asset Maintenance Log list.

![Planned Asset Maintenance Logs in ERPNext](https://novacompanies.m.frappe.cloud/files/13-maintenance-log-list.png)

## Complete the log

1. Confirm the Asset, task, due date, and assignee.
2. Change status to **Completed** after the work is actually finished.
3. Enter the completion date and actions performed.
4. Attach the certificate when the task requires one.
5. Save the log and review the next due date on the maintenance plan.

![Maintenance plan linked to its recurring logs](https://novacompanies.m.frappe.cloud/files/11-asset-maintenance-plan.png)


| Field         | What it means                                                        |
| ------------- | -------------------------------------------------------------------- |
| **Planned**   | Work is scheduled but not complete.                                  |
| **Completed** | Work and required evidence have been recorded.                       |
| **Overdue**   | The due date passed without completion.                              |
| **Cancelled** | The occurrence will not be performed and the reason should be clear. |


## Troubleshooting

### The log cannot be marked complete

Check required completion date, certificate, and actions fields for the task.

### The next due date is wrong

Review the parent maintenance task's periodicity and the last completion date.

## Frequently asked questions

### Should I create logs manually?

Scheduled plans normally create them. Manual logs can be used for exceptional maintenance when the relationship remains clear.

### Can a completed log be edited?

Follow the document's edit rules and retain audit history. Do not overwrite evidence casually.

### Does a log post to the ledger?

In ERPNext, no. It is an operational record. Repair invoices or capitalized repair costs create accounting effects.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance-team.md -->
---
title: "Asset Maintenance Team | ERPNext Documentation"
description: "Create an ERPNext Asset Maintenance Team with a manager, members, and roles."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance-team"
updated: "2026-08-15"
---

Imagine Nova Industries has electricians, IT technicians, and machine specialists. When a laptop or production machine needs work, assigning the wrong person wastes time and may leave the real problem unresolved.



An Asset Maintenance Team groups the people who can perform a type of maintenance. The team can then be selected on a maintenance plan so everyone knows who is responsible for each scheduled task.

## Create a team

1. Open **Asset Maintenance Team** and select **Add**.
2. Enter a team name and company.
3. Select a Maintenance Manager.
4. Add members and their maintenance roles.
5. Save, then use the team in [Asset Maintenance](https://docs.frappe.io/erpnext/asset-maintenance) plans.

![Nova Facilities Team in ERPNext Asset Maintenance](https://novacompanies.m.frappe.cloud/files/10-maintenance-team.png)


| Field                   | What it means                                                   |
| ----------------------- | --------------------------------------------------------------- |
| **Maintenance Manager** | User who supervises the plan.                                   |
| **Team Member**         | User who can be assigned maintenance work.                      |
| **Maintenance Role**    | Role used to describe or authorize the member's responsibility. |
| **Company**             | Company whose assets the team maintains.                        |


## Troubleshooting

### A user cannot be selected as a member

Confirm the User is enabled and has access to the relevant company and Assets records.

### Tasks are assigned to the wrong person

Correct the task's Assign To field. The team defines available ownership but each task controls its assignee.

## Frequently asked questions

### Can the same user be in more than one team?

In ERPNext, yes, when that reflects operational responsibility.

### Does the team itself create tasks?

In ERPNext, no. The Asset Maintenance plan creates scheduled tasks and logs using the selected team.

### Can teams be company specific?

In ERPNext, yes. Keep the selected company aligned with the Assets the team will maintain.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance.md -->
---
title: "Asset Maintenance | ERPNext Documentation"
description: "Plan recurring preventive maintenance and calibration for ERPNext Assets."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance"
updated: "2026-08-15"
---

Imagine a Nova Industries packaging machine needs inspection every month and a belt replacement every six months. If the team depends on memory, a missed service could stop production and cost much more than the maintenance itself.



Asset Maintenance turns those recurring jobs into a planned schedule. It records what must be done, how often it should happen, and who is responsible, helping the team service equipment before it fails.

## Before you begin

Enable **Maintenance Required** on the Asset and create an [Asset Maintenance Team](https://docs.frappe.io/erpnext/asset-maintenance-team).

## Create a maintenance plan

1. Select the Asset and Maintenance Team.
2. Add a task with its type, start date, periodicity, assignee, and description.
3. Mark whether a certificate is required.
4. Save the plan. ERPNext creates planned [Asset Maintenance Logs](https://docs.frappe.io/erpnext/asset-maintenance-log) for the schedule.

![Preventive maintenance plan for a Nova Industries laptop](https://novacompanies.m.frappe.cloud/files/11-asset-maintenance-plan.png)

Use the pencil icon to open the complete child-row editor when the grid hides task fields.

![Pencil icon for the Asset Maintenance task row](https://novacompanies.m.frappe.cloud/files/12-maintenance-task-pencil.png)

## Follow the work

Open the generated log, record actions performed, add a certificate when required, and mark the work completed.

![ERPNext Asset Maintenance Log list](https://novacompanies.m.frappe.cloud/files/13-maintenance-log-list.png)

## Troubleshooting

### No maintenance logs were created

Check the start date, end date, periodicity, and assignee, then save the maintenance plan again.

### The task is overdue

Complete or cancel the correct log. Do not only change the plan because the historical occurrence still needs a result.

## Frequently asked questions

### Is preventive maintenance the same as repair?

In ERPNext, no. Maintenance is planned work. Asset Repair records a failure, downtime, repair cost, and possible capitalization.

### Can one Asset have several tasks?

In ERPNext, yes. Add separate rows for checks, calibration, cleaning, or certification.

### Does maintenance affect asset value?

Routine maintenance normally does not. A qualifying repair cost can be capitalized through the repair workflow.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-movement.md -->
---
title: "Asset Movement | ERPNext Documentation"
description: "Transfer, issue, or receive ERPNext Assets while preserving location and custody history."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-movement"
updated: "2026-08-15"
---

Imagine a laptop moves from Nova Industries' head office to the service workshop, then is issued to a new employee. The problem with editing the location directly is that it would show only where the laptop is now. It would not explain who moved it or where it was before.



Asset Movement records every transfer, issue, and receipt as a separate event. The latest submitted movement updates the asset's location or custodian while keeping the earlier movements available as history.

## Choose the purpose


| Field                  | What it means                                                     |
| ---------------------- | ----------------------------------------------------------------- |
| **Transfer**           | Moves an asset from one location to another.                      |
| **Issue**              | Assigns custody to an employee.                                   |
| **Receipt**            | Returns an issued asset from an employee.                         |
| **Transfer and Issue** | Moves the asset and assigns it to an employee in one transaction. |


## Create an Asset Movement

1. Select the company and purpose.
2. Set the transaction date and time.
3. Add the Asset and its source details.
4. Enter the target location or employee required by the purpose.
5. Submit the movement.

![Asset transfer from Nova Headquarters to Service Workshop](https://novacompanies.m.frappe.cloud/files/14-asset-movement-transfer.png)

Use the pencil icon to review all source, target, employee, and department fields in the child row.

![Asset Movement child-row pencil icon](https://novacompanies.m.frappe.cloud/files/15-asset-movement-pencil.png)

## Verify the result

Open the Asset or Asset list and confirm the current location and status reflect the submitted movement.

![Asset list used to verify current locations](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### The target location did not change

Confirm the Asset Movement was submitted and the correct Asset row was used.

### The movement asks for an employee

The selected purpose includes custody. Use Transfer when only the physical location changes.

## Frequently asked questions

### Can one movement contain several assets?

In ERPNext, yes. Add multiple rows when the assets share the same movement context.

### Does an Asset Movement affect the ledger?

In ERPNext, no. It changes custody and location, not asset value.

### Can I move an out-of-order asset?

Check the operational policy and linked repair state. The system record should match the real handoff.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-repair.md -->
---
title: "Asset Repair | ERPNext Documentation"
description: "Record ERPNext Asset failures, repair work, downtime, costs, consumed items, and capitalization decisions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-repair"
updated: "2026-08-15"
---

Imagine a Nova Industries inspection camera stops working. The team sends it to a repair vendor, pays for replacement parts, and receives it back three days later. The company needs to track the downtime and cost, and it must decide whether the repair is an expense or increases the asset's value.



Asset Repair records the failure, repair work, cost, and completion. It also connects qualifying capital repair costs to the asset when they extend its useful life or improve its capacity.

## Create an Asset Repair

1. Select the Asset and failure date.
2. Enter a clear description of the failure.
3. Save with status **Pending** while work is in progress.
4. Add supplier invoices or consumed stock items where applicable.
5. Record actions performed and completion date.

![Pending Asset Repair for a Nova Industries laptop](https://novacompanies.m.frappe.cloud/files/16-asset-repair-details.png)

## Record cost and capitalization

Routine repair is normally an expense. Enable **Capitalize Repair Cost** only when the cost meets the organization's capitalization policy and increases future economic benefit. If the repair extends useful life, enter the increase in asset life and review the depreciation schedule.

![Repair cost and capitalization fields in ERPNext](https://novacompanies.m.frappe.cloud/files/17-asset-repair-cost.png)

## Complete and verify

Set the repair to **Completed**, confirm downtime, and open the Asset. A pending failure can place the asset out of order; completion should restore the correct operating state.

![Asset status after repair workflow activity](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### Repair cost remains zero

Link the relevant Purchase Invoices or consumed items and confirm their rates and amounts.

### The Asset remains Out of Order

Complete the repair and verify no other active repair keeps the asset unavailable.

### Capitalization did not update the schedule

Confirm the repair was submitted with capitalization enabled and review the linked value and schedule documents.

## Frequently asked questions

### Should every repair be capitalized?

In ERPNext, no. Capitalize only costs that meet the accounting policy. Routine repairs are usually expenses.

### Can repair consume stock items?

In ERPNext, yes. Add consumed parts so their cost is included and inventory is reduced through the supported workflow.

### Does Asset Repair replace maintenance logs?

In ERPNext, no. Maintenance logs record planned work. Repair records a failure and its financial or operational recovery.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-reports.md -->
---
title: "Asset Reports | ERPNext Documentation"
description: "Use ERPNext Asset reports to reconcile depreciation, balances, fixed-asset registers, and lifecycle activity."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-reports"
updated: "2026-08-15"
---

Imagine the finance head at Nova Industries asks four questions before month-end: what assets do we own, how much depreciation was posted, what value remains, and which assets moved or changed during the month? One list cannot answer all four questions clearly.



ERPNext Asset Reports provide different views for different decisions. Together, the depreciation ledger, depreciation and balances report, fixed asset register, and asset activity report help the team reconcile values and investigate what happened.

## Choose the right report


| Field                                | What it means                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Asset Depreciation Ledger**        | Detailed depreciation schedule and posting history for each Asset and Finance Book.                                     |
| **Asset Depreciations and Balances** | Opening value, additions, depreciation, adjustments, and closing carrying value.                                        |
| **Fixed Asset Register**             | Operational and financial register with category, status, dates, values, cost center, department, vendor, and location. |
| **Asset Activity**                   | Lifecycle events such as purchase, movement, repair, value change, sale, or scrapping.                                  |


## Asset Depreciation Ledger

Use this report to investigate a schedule or reconcile posted and pending depreciation rows. Filter by company, date, Asset, category, or Finance Book.



The example below shows seven submitted monthly depreciation entries for Nova Industries' NovaPack labeler. The report makes it possible to trace each $760 expense to its depreciation Journal Entry and follow the accumulated balance.

![Loaded Asset Depreciation Ledger with seven posted entries](https://novacompanies.m.frappe.cloud/files/22-asset-depreciation-ledger-v2.png)

## Asset Depreciations and Balances

Use it to explain how carrying value changed across a period. It is the strongest starting point for reconciling additions, depreciation, and closing value.

![Loaded Asset Depreciations and Balances report](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Fixed Asset Register

Use it for the controlled asset listing and location or custodian review. The chart gives a quick acquisition view while the rows contain the audit detail.

![Loaded Fixed Asset Register with chart and asset rows](https://novacompanies.m.frappe.cloud/files/24-fixed-asset-register.png)

## Asset Activity

Use this report when the question is "what happened to this asset?" Filter to the asset or period, then open linked documents to verify the event.



The example below contains real lifecycle events for Nova's laptops and production equipment, including creation, location receipt, submission, and a repair event.

![Asset Activity with real lifecycle transactions](https://novacompanies.m.frappe.cloud/files/25-asset-activity-v2.png)

## Read a report safely

1. Select the company and Finance Book explicitly.
2. Set a period that matches the reconciliation.
3. Check whether the report includes default Finance Book assets.
4. Wait for the rows and charts to finish loading.
5. Drill into source documents for material or unexpected values.
6. Export only after the filters and totals are verified.

## Troubleshooting

### The report is empty

Check company, date range, Asset status, Finance Book, and whether depreciation or lifecycle transactions exist in the period.

### Two reports show different totals

Confirm they answer the same question and use identical company, date, Finance Book, and status filters.

### A row shows zero depreciation

Open the Asset Depreciation Schedule and verify that entries have been posted for the selected period.

## Frequently asked questions

### Which report should I give an auditor?

The Fixed Asset Register is a common starting point, supported by depreciation and ledger reports plus source documents.

### Where do I check a single Asset's full history?

Use Asset Activity, then open the linked Asset and transactions.

### Can reports compare Finance Books?

Run or filter the report for each Finance Book so the basis remains explicit and totals are not mixed.

### Why does the chart not match a filtered export?

Refresh after applying filters and ensure the chart and data table finished loading before export.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-shift-allocation.md -->
---
title: "Asset Shift Allocation | ERPNext Documentation"
description: "Allocate ERPNext asset depreciation by machine shifts when utilization changes across periods."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-shift-allocation"
updated: "2026-08-15"
---

Imagine a Nova Industries packaging machine runs one shift in January, three shifts in February, and two shifts in March. If the machine works harder in February, equal depreciation every month may not match how quickly the machine is being used up.



Asset Shift Allocation records the shifts worked during each period. ERPNext uses those allocations with shift-based depreciation so heavier use can produce more depreciation and lighter use can produce less.

## Before you begin

Enable **Shift Based** in the Asset's Finance Book row and confirm the configured shift factors follow the approved accounting policy.

![Asset Finance Book used for shift-based depreciation](https://novacompanies.m.frappe.cloud/files/09-production-asset-depreciation.png)

## Allocate a shift

1. Open **Asset Shift Allocation**.
2. Select the Asset and Finance Book.
3. Choose the shift and effective date range.
4. Save and submit the allocation.
5. Review the regenerated or affected schedule before depreciation is posted.

## Understand the result

The shift factor changes how much depreciation is assigned to the relevant period. It does not change the acquisition cost. The total schedule must still respect the residual value.

![Report used to verify depreciation after shift allocation](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### The depreciation amount did not change

Confirm the Finance Book is shift based, the allocation covers the schedule date, and depreciation has not already been posted for that period.

### The asset is allocated to overlapping shifts

Correct the dates so only the intended shift applies to a given period.

## Frequently asked questions

### Should office laptops use shift allocation?

Usually no. It is most useful for production equipment whose usage is measured by shifts.

### Does a shift allocation create a ledger entry?

The allocation changes the depreciation basis. The ledger entry occurs when depreciation is posted.

### Can future shifts be planned?

In ERPNext, yes, but review them when operational schedules change.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-value-adjustment.md -->
---
title: "Asset Value Adjustment | ERPNext Documentation"
description: "Adjust an ERPNext Asset's carrying value for a selected Finance Book and verify the resulting accounting entry."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-value-adjustment"
updated: "2026-08-15"
---

Imagine an independent valuation shows that a Nova Industries machine is worth $8,000 less than its current book value. If the accountant changes the value only in a spreadsheet, the Asset record and General Ledger will no longer agree.



Asset Value Adjustment records the new value on a specific date and posts the accounting effect through the configured accounts. This keeps the revised carrying value, future depreciation, and ledger history connected.

## Before you begin

Obtain an approved valuation, confirm the effective date, select the correct [Finance Book](https://docs.frappe.io/erpnext/using-finance-book-for-asset-depreciation), and identify the difference account and cost center.

## Create the adjustment

1. Select the Asset and date.
2. Select the Finance Book when the change applies to one reporting basis.
3. Review the Current Asset Value.
4. Enter the New Asset Value.
5. Select the Difference Account and cost center.
6. Submit and open the linked Journal Entry.

![Asset Value Adjustment from 36000 to 39000](https://novacompanies.m.frappe.cloud/files/18-asset-value-adjustment.png)

## Verify the result

Confirm the Asset's carrying value and future depreciation schedule changed only for the intended Finance Book. Use Asset Depreciations and Balances to reconcile the result.

![Asset report used to verify an adjusted value](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### Current value is not what the valuation expected

Check the Finance Book, effective date, booked depreciation, and earlier value adjustments.

### The difference posts to the wrong account

Cancel or reverse according to policy, then correct the category or selected Difference Account before reposting.

## Frequently asked questions

### Is this the same as depreciation?

In ERPNext, no. Depreciation follows a schedule; value adjustment records a separate approved change in carrying value.

### Can I adjust only one Finance Book?

In ERPNext, yes. Select it explicitly and verify reports using the same filter.

### Does the adjustment create a Journal Entry?

A submitted adjustment creates or links the accounting entry for the difference.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset.md -->
---
title: "Asset | ERPNext Documentation"
description: "Create and manage an ERPNext Asset record, including value, location, ownership, depreciation, insurance, and lifecycle status."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset"
updated: "2026-08-15"
---

An Asset record is the operating history of something the company uses. For Nova Industries' staff laptop, it connects the Item and purchase value to a current location, maintenance plan, depreciation schedule, and eventual disposal.



Create one only after deciding whether the item is company equipment rather than inventory held for sale.

## Before you begin

Prepare the fixed-asset Item, [Asset Category](https://docs.frappe.io/erpnext/asset-category), company accounts, and [Asset Location](https://docs.frappe.io/erpnext/asset-location). Use [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset) when the record originates from a new purchase.

## Create an Asset

1. Open **Asset** and select **Add Asset**.
2. Select the Item and company.
3. Enter a recognizable Asset Name and current Location.
4. Select **Existing Asset** only when bringing an already-owned asset into ERPNext. Use **Composite Asset** when the asset is assembled by capitalization.
5. Enter purchase and available-for-use dates, value, and quantity.
6. Enable maintenance and depreciation only when they apply.

![Core ERPNext Asset fields for a Nova Industries laptop](https://novacompanies.m.frappe.cloud/files/07-asset-core-details.png)

## Important fields and what they mean


| Field                                | What it means                                                             |
| ------------------------------------ | ------------------------------------------------------------------------- |
| **Item Code**                        | The reusable Item definition for this asset model.                        |
| **Asset Name**                       | The human-readable identity, such as an internal tag or serial reference. |
| **Location**                         | Current physical position.                                                |
| **Asset Type**                       | Existing, Composite Asset, or Composite Component.                        |
| **Purchase Date**                    | Date the company acquired the asset.                                      |
| **Available for Use Date**           | Date capitalization and depreciation can begin.                           |
| **Net Purchase Amount**              | Capitalized acquisition value before later adjustments.                   |
| **Maintenance Required**             | Allows maintenance planning and logs.                                     |
| **Calculate Depreciation**           | Creates depreciation schedules from Finance Book settings.                |
| **Opening Accumulated Depreciation** | Depreciation already booked before migration to ERPNext.                  |
| **Custodian and Department**         | Operational responsibility and reporting ownership.                       |


## Review depreciation

Each Finance Book may have a different method, useful life, residual value, and posting frequency.

![Finance Book configuration on an ERPNext Asset](https://novacompanies.m.frappe.cloud/files/08-asset-finance-books.png)

## Status and downstream actions


| Field                              | What it means                                                  |
| ---------------------------------- | -------------------------------------------------------------- |
| **Submitted**                      | The asset is active in the register.                           |
| **Partially Depreciated**          | At least one depreciation is booked and value remains.         |
| **Fully Depreciated**              | The scheduled depreciable value has been booked.               |
| **In Maintenance or Out of Order** | Operational condition is restricted.                           |
| **Sold**                           | A disposal sale has completed.                                 |
| **Scrapped**                       | The asset was written off through the scrap workflow.          |
| **Capitalized**                    | The asset was created or updated through Asset Capitalization. |


![Asset statuses in the ERPNext list view](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### The Asset value or account is wrong

Trace the source purchase, category account defaults, and any capitalization or value-adjustment entries. Do not correct only the visible total without understanding the ledger source.

### The Asset cannot be cancelled

Cancel or reverse linked submitted depreciation and disposal documents in the required order first.

## Frequently asked questions

### Can I change the location directly?

Use Asset Movement for a controlled transfer and an auditable history.

### Can I store insurance information?

In ERPNext, yes. Use the insurance fields for insurer, policy dates, insured value, and coverage details.

### Can one Asset contain multiple units?

Grouped assets support quantity-based use cases, but individual assets are clearer when each unit needs its own custodian, maintenance, or disposal history.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__assets__introduction.md -->
---
title: "Overview | ERPNext Documentation"
description: "Understand the ERPNext Assets lifecycle, from purchase and capitalization through depreciation, maintenance, transfer, sale, or scrapping."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assets/introduction"
updated: "2026-08-15"
---

Imagine you are helping the accounts team at Nova Industries, an electronics manufacturing and distribution company. The company buys phones to sell, laptops for employees, and machines for its packaging floor. The phones are inventory because customers will buy them. The laptops and machines are assets because Nova Industries will use them for several years.



The ERPNext Assets module keeps the complete story of those assets in one place. It records what the company owns, where each asset is, who uses it, how its value reduces over time, what it costs to maintain, and whether it is eventually sold or scrapped.

## Understand the asset lifecycle

1. Define an [Asset Category](https://docs.frappe.io/erpnext/asset-category) with the correct asset, accumulated depreciation, expense, and capital work in progress accounts.
2. Organize physical places in the [Asset Location](https://docs.frappe.io/erpnext/asset-location) tree.
3. Mark an Item as a fixed asset, then buy it or create an existing Asset record.
4. Place the asset in service and review its depreciation schedule.
5. Record assignment, [movement](https://docs.frappe.io/erpnext/asset-movement), [maintenance](https://docs.frappe.io/erpnext/asset-maintenance), [repair](https://docs.frappe.io/erpnext/asset-repair), and value adjustments during its life.
6. Finish the lifecycle by [selling](https://docs.frappe.io/erpnext/selling-an-asset) or [scrapping](https://docs.frappe.io/erpnext/scrapping-an-asset) the asset.

![ERPNext Asset list for Nova Industries showing laptops and production equipment](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## What the module records


| Field                | What it means                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Identity**         | Item, asset name, category, company, owner, and status.                                                                |
| **Physical control** | Current location, custodian, department, transfers, issues, and receipts.                                              |
| **Accounting**       | Purchase value, capitalization, Finance Books, depreciation schedules, accumulated depreciation, and disposal entries. |
| **Operations**       | Preventive maintenance plans, maintenance logs, failures, repairs, downtime, and repair cost.                          |
| **Lifecycle result** | Whether the asset remains in use, is out of order, has been sold, or has been scrapped.                                |


## Stock item versus fixed asset

Use a stock item when the company intends to sell or consume the item. Use a fixed-asset Item when the company will use the item to run the business for more than one accounting period. The same laptop model can therefore be inventory in an electronics store and a fixed asset when issued to the store manager.

## Accounting impact at a glance

An Asset record by itself is the operational register. Accounting entries arise from submitted acquisition, depreciation, value adjustment, capitalization, sale, or scrap transactions. Locations and maintenance logs change the operational history but do not normally post to the General Ledger.

## Frequently asked questions

### Can ERPNext manage non-depreciable assets?

In ERPNext, yes. Enable **Non Depreciable Category** when an asset category should not create depreciation schedules.

### Can one asset have different depreciation schedules?

In ERPNext, yes. Finance Books can maintain different methods or useful lives for statutory and management reporting.

### Does moving an asset create a ledger entry?

In ERPNext, no. Asset Movement changes custody or location. It does not change the asset's accounting value.

### Where can I see the complete asset register?

Use the [Fixed Asset Register](https://docs.frappe.io/erpnext/asset-reports) and related Asset reports.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__assignment-rule.md -->
---
title: "Assignment Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assignment-rule"
updated: "2026-03-02"
---


> Introduced in Version 12

**An Assignment Rule lets you set up automatic assignment of documents to Users.**

To assign the support tickets automatically amongst the employees who work on support, an Assignment Rule can be used.

To access Assignment Rule, go to:
> Home > Settings > Assignment Rule

## 1. How to create an Assignment Rule
To set up an automatic assignment:

1. Go to the Assignment Rule list, click on New.
1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do.
1. Select the condition for the assignment.
 You can write simple Python expressions for automatic assignment in the `Assign Rule`, `Close Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, ==, etc and also multiple conditions like `and` and `or`.

 Examples:

 - `status == "Open"`
 - `issue_type == "Technical" and priority=="High" and status == "Open"`

1. Select the assignment rule.

 ![Assignment Rule](/files/assignment-rule-select.png)

 * **Round Robin**: Assign each document to a User in sequence.
 * **Load Balancing**: Assign new documents to the User who has the least number of assignments.

 Select the list of Users to whom this Assignment Rule will apply:
 ![Users in Assignment Rule](/files/auto-assign-2.png)

 * **Based on Field**: Introduced in v13, this rule can be used to assign a document to the User that is set in the configured field.

 Select the User link field which will determine to whom this Assignment Rule will apply:
 ![Field Assign](/files/field-auto-assign.png)


1. Save.

You can use properties of the document in the Description field that will be part of the assignment. Higher 'Priority' Assignment Rules will be applied first.

Example:

High Priority Issue *File Upload not working* has been assigned to you.

### 1.1 Multiple Assignment Rules

You can also set up multiple auto assignments for each Document Type, the one with the highest Priority will be applied first.

![Assignment Rule with Higher Priority](/files/assignment-rule-with-higher-priority.png)


assignment-rule-with-higher-priority

### 1.2 Setting Due Date for assignment

You can auto set due dates for assignments based on the date field in the reference document.

Example:

If you want to set a due date on Issue assignment based on the "Resolution By" date of the Issue, you can do so by selecting "Resolution By" field in `Due Date Based On` option in Assignment Rule.

![Due Date Based On](/files/assignment-rule-due-date-based-on.png)

**Note:**

- "Due Date Based On" option will not be available if "Document Type" is not yet selected or if the selected Document Type does not have any "Date" or "Datetime" field.
- Due Date in the assignment/ToDo will be updated whenever the "Due Date Based On" field value is updated in the reference document.

### 2. Related Topics

1. [Workflows](/erpnext/workflows)
1. [Workflow Actions](/erpnext/workflow-actions)

<!-- page: erpnext/erpnext__assistance-sales-purchase-between-companies.md -->
---
title: "Create a Sales Invoice without an Item Code | ERPNext Documentation"
description: "Create ERPNext Sales Invoices and Credit Notes for one-time charges without an Item Code by completing the required child-row fields."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assistance-sales-purchase-between-companies"
updated: "2026-07-25"
---

Use inter-company drop shipping when one Company sells to a Customer while goods are supplied directly by another Company in the same ERPNext site. This combines the [Drop Ship](/erpnext/drop-shipping-in-erpnext) workflow with inter-company Customer and Supplier relationships.

## Before you begin

Create or confirm:

- Both [Companies](/erpnext/company) in the same site.
- An internal Customer representing the supplying Company.
- An internal Supplier representing the selling Company.
- **Represents Company** and internal-party settings on both masters.
- Items, Warehouses, Price Lists, taxes, and inter-company accounts.
- Permissions for both Companies.

Review [Inter Company Invoices](/erpnext/inter-company-invoices) before using the workflow. Each Company remains a separate accounting entity.

## Configure internal parties

1. Create a Customer for the Company that buys internally.
2. Enable **Is Internal Customer** and select **Represents Company**.
3. Create the reciprocal Supplier.
4. Enable **Is Internal Supplier** and select the represented Company.
5. Save both records.

![](/files/subsidiary-drop-ship-internal-customer-v3.webp)

## Create the customer Sales Order

1. In the selling Company, create a [Sales Order](/erpnext/sales-order) for the external Customer.
2. Add the Items.
3. Select the highlighted pencil icon to open the Item row.
4. Enable **Drop Ship** for the row.
5. Select the Supplier that represents the supplying subsidiary.
6. Save and submit.

![A Sales Order Item with Supplier delivers to Customer and the subsidiary Supplier highlighted.](https://novacompanies.m.frappe.cloud/files/subsidiary-drop-ship-sales-order-v2.png)

In a drop-ship flow, stock availability in the selling Company's Warehouse does not replace Supplier fulfilment planning.

## Create the Purchase Order

From the submitted Sales Order:

1. Select **Create > Purchase Order**.
2. Choose the internal Supplier.
3. Review the mapped external Customer delivery address and Items.
4. Confirm the buying Company, schedule dates, rates, taxes, and terms.
5. Save and submit.

![A Purchase Order created for an internal Supplier with the Customer delivery address.](https://novacompanies.m.frappe.cloud/files/subsidiary-drop-ship-purchase-order.png)

The Purchase Order instructs the supplying subsidiary to deliver directly to the external Customer.

## Complete the inter-company documents

Create the corresponding internal sales and purchase invoices according to your [inter-company transaction](/erpnext/inter-company-invoices) process. Then invoice the external Customer from the selling Company.

Keep these relationships clear:


| Relationship                               | Document                  |
| ------------------------------------------ | ------------------------- |
| External Customer owes selling Company     | External Sales Invoice    |
| Selling Company owes supplying subsidiary  | Internal Purchase Invoice |
| Supplying subsidiary bills selling Company | Internal Sales Invoice    |


Tax and transfer-pricing requirements vary by jurisdiction. Configure them with qualified accounting advice.

## Troubleshooting


| Problem                                | What to check                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------- |
| Internal Supplier cannot be selected   | Confirm Is Internal Supplier, Represents Company, permissions, and disabled status            |
| Purchase Order uses the wrong Company  | Review the internal party relationship and mapped Company                                     |
| Customer address is missing            | Confirm the Sales Order shipping address and drop-ship row                                    |
| Inter-company invoice is not generated | Review reciprocal Customer and Supplier masters and inter-company settings                    |
| Stock is moved in the selling Company  | Confirm that the Item row uses Drop Ship and that no Delivery Note was created for that stock |


## Frequently asked questions

### Does the selling Company receive the goods?

No. In the intended drop-ship flow, the Supplier delivers directly to the external Customer.

### Are inter-company invoices still required?

Yes. The Companies remain separate accounting entities even though they share an ERPNext site.

### Can only selected lines be drop shipped?

Yes. Configure Drop Ship at the Item-row level and plan the remaining lines through the normal warehouse flow.

### Does ERPNext determine legal transfer prices?

No. Configure internal rates and taxes according to your organization's policy and applicable law.

## Related topics

- [Drop Ship](/erpnext/drop-shipping-in-erpnext)
- [Inter Company Invoices](/erpnext/inter-company-invoices)
- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)
- [Company](/erpnext/company)

<!-- page: erpnext/erpnext__authorization-rule.md -->
---
title: "Authorization Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/authorization-rule"
updated: "2026-03-02"
---


**Authorization Rule allows configuring a custom authorization / approval on a documents, based on conditions defined.**

Example: If a Sales Order's Grand Total exceeds $1,000, then it should be verified/submitted by the Sales Manager only, even if the Sales User has "Submit" permission.

On the same lines, you can define Authorization Rule based on the fields like Net Total, Grand Total, Discount % and specify who would be the document approver if the authorization condition is matched.

![Authorization Rule](/files/authorization-rule.png)

Let's consider a detailed example of an Authorization Rule to learn better.

Assume that the Sales Manager needs to authorize Sales Orders, only if it's Grand Total value exceeds 10,000. If the Sales Order value is less than 10,000, then even the Sales User will be able to submit it. This means that the Submit permission of Sales User will be restricted only up to Sales Order of Grand Total less than 10,000.

## 1. How to create an Authorization Rule

1. Go to the Authorization Rule list, click on New.
1. Select the transaction on which Authorization Rule will be applicable. This functionality is available for limited transactions only.
1. Enter the Authorized Value, etc. This depends on the field you selected in Based On.
1. Select Based On. Authorization Rule will be applied based on the value selected in this field.
1. Select Applicable Role. This is the role on which this Authorization Rule will be applicable. As per the example, it'll be Sales User.
1. To be more specific, you can also select Applicable To User if you wish to apply the rule to a specific Sales User, and not to all Sales Users.
1. Select Approving Role. This is the role that can approve forms over the Authorized value. As per our example, it is the Sales Manager.
1. You can also select a specific Sales Manager.
1. Save.

![Authorization Rule](/files/new-authorization-rule.png)

If the Sales User tries submitting the Sales Order of value higher than 10,000, then he will get an error message.

![Authorization Rule Validation Message](/files/authorization-rule-validation-message.png)

> If you wish to restrict Sales User from submitting Sales Orders, then instead of creating Authorization Rule, you should remove submit privilege for Sales User from [Role Permission Manager](/erpnext/role-based-permissions).

### Documents on which Authorization Rule can be applied

1. Sales Order
1. Purchase Order
1. Quotation
1. Delivery Note
1. Sales Invoice
1. Purchase Invoice
1. Purchase Receipt
1. Appraisal

### Fields on which Authorization Condition can be based on

1. Grand Total
1. Average Discount
1. Customer-wise Discount
1. Item-wise Discount

<!-- page: erpnext/erpnext__auto-creation-of-material-request.md -->
---
title: "Auto Creation of Material Request"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-creation-of-material-request"
updated: "2026-02-27"
---

  


To prevent stockouts, you can track item's reorder level. When stock level goes below reorder level, purchase manager is notified and instructed to initiate purchase process for the item.

In ERPNext, you can update item's Reorder Level and Reorder Qty in the Item master. If same item has different reorder level, you can also update warehouse-wise reorder level and reorder qty.

![reorder level](/files/reorder-request-1.png)  


With reorder level, you can also define what should be the next action. Either new purchase or transfer from another warehouse. Based on setting in Item master, purpose will be updated in the Material Request as well.

![reorder level next action](/files/reorder-request-2.png)  


When item's stock reaches reorder level, Material Request is auto-created automatically. You can enable this feature from:

`Stock > Setup > Stock Settings`

![active auto-material request](/files/reorder-request-3.png)  


A separate Material Request will be created for each item. User with Purchase Manager's role will receive email alert about these Material Requests.

If auto creation of Material Request is failed, User with Purchase Manager role will be informed about error message. One of the most encountered error message is:

**An error occurred for certain Items while creating Material Requests based on Re-order level.** **Date 01-04-2016 not in any Fiscal Year.**

One of the reason of error could be Fiscal Year as well. Click [here](/erpnext/fiscal-year-error.html) to learn more about it.

### Note:

The system creates a material request by comparing the projected quantity of the group warehouse with the reorder level. If the group warehouse is not set, then the system compares the projected quantity of the Request for Warehouse with the reorder level. If the projected qty is more than the reorder level then system doesn’t add that item in the material request.

<!-- page: erpnext/erpnext__auto-email-reports.md -->
---
title: "Auto Email Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-email-reports"
updated: "2026-03-02"
---

**Auto Email Reports automatically sends reports for the selected document.**

You can setup **Auto Email Report** to send reports at regular intervals. These must be saved reports of any type (Report Builder, Script or Query Report).

You can find Auto Email Report at:

> Home > Settings > Auto Email Report

1. How to create an Auto Email Report
-------------------------------------

1. Go to the Auto Email Report list, click on New.
2. Select the Report for which you want to generate emails.
3. Select the user for which you want to create this report (permissions will apply for this user).
4. Set the Email Addresses to which you want this report to be emailed and the frequency of the report. Emails will be sent at midnight. The date will be repeated in case of weekly/monthly/yearly frequency.

![With Filters](/files/auto-email-2.png)
5. Save.

You can test the report by clicking on "Download" or "Send Now". Here is an example of the email you will receive for a general ledger report:

![Report by Email](/files/auto-email-4.png)  


2. Features
-----------

### 2.1 Filter Data

* **Send only if there is any data**: If enabled, emails will not be sent if there is no data in the report.
* **Only Send Records Updated in Last X Hours**: If set to 24, an email will contain only records updated in the last 24 hours.
* **No of Rows**: The number of rows to be sent in the email. The maximum is 500.

### 2.2 Report Filters

If your report has filters, you will be able to see them. Click on the table to edit it:

![Edit Filters](/files/auto-email-3.png)  


For example, if the email is on the report 'Project Billing Summary' select the Project. The date range here is the date range of the 'Project Billing Summary'.

### 2.3 Message

A message can also be added to be sent with the email report. For example, 'This is your monthly Project Billing Summary Report:'

You can also change the file format in which the report is created. The available options are HTML, XLSX, and CSV.

### 2. Related Topics

1. [Email Digest](/erpnext/email-digest)
2. [Document Follow](/erpnext/document-follow)

<!-- page: erpnext/erpnext__auto-repeat-recurring-orders-and-invoices.md -->
---
title: "Auto Repeat Recurring Orders and Invoices | ERPNext Documentation"
description: "Schedule ERPNext to create recurring orders, invoices, journals, and other enabled documents from a reference transaction."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-repeat-recurring-orders-and-invoices"
updated: "2026-08-14"
---

Nova Industries bills Northstar Retail, a customer with a monthly device-support contract, on the first day of every month. Recreating the same Sales Invoice by hand risks missed billing and inconsistent terms. Auto Repeat uses an approved source document as a template and creates new orders or invoices on a schedule.



Use Auto Repeat for stable recurring transactions. Use [Subscription](/erpnext/subscription) when the agreement is plan-driven and needs subscription dates, plan quantities, trials, or subscription lifecycle controls.

## Before you begin

- Review the source party, company, items, rates, taxes, payment terms, dimensions, and addresses.
- Decide whether generated documents should stay in Draft for review or submit automatically.
- Confirm who should receive email and which print format should be attached.

## Create the Auto Repeat

1. Open **Auto Repeat** and create a new record.
2. Select the Reference Document Type and the exact order or invoice to repeat.
3. Set the start date and, when the agreement ends, an end date.
4. Enable Submit on Creation only when the generated transaction needs no manual review.

![Auto Repeat reference document and creation settings](https://novacompanies.m.frappe.cloud/files/sales-receivables-auto-repeat-recurring-orders-and-invoices-auto-repeat-details.png)



## Set the schedule

Choose the frequency and the relevant schedule options. For monthly billing, set the expected day or use the last day of the month when that matches the contract.

![Auto Repeat schedule for a recurring invoice](https://novacompanies.m.frappe.cloud/files/sales-receivables-auto-repeat-recurring-orders-and-invoices-auto-repeat-schedule.png)



## Monitor generated documents

Review the next scheduled date and the generated documents. Prices, taxes, addresses, and contract terms can change after the source was approved, so keep a review owner even when creation is automated.

## Troubleshooting

### No document was generated

Check that Auto Repeat is enabled, the start and end dates include today, the schedule is complete, the reference document is valid, and background jobs are running.

### The generated document has old commercial terms

Update the reference document or create a new approved source and point Auto Repeat to it. Do not assume changes in related masters will safely update every copied field.

## Frequently asked questions

### Can it repeat both orders and invoices?

Use supported Sales Orders, Purchase Orders, Sales Invoices, and Purchase Invoices as reference documents. Verify the current DocType’s Auto Repeat support before relying on it.

### Should I enable automatic submission?

Use it only for stable, low-risk transactions with tested taxes and controls. Draft creation is safer when a person must review each cycle.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__auto-repeat.md -->
---
title: "Auto Repeat\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-repeat"
updated: "2026-03-02"
---


Auto Repeat feature helps you create certain documents automatically in a given time period.

From version 12, you can Customize any Form to make the documents **repeatable**.

For Example: Assuming that you follow deferred expense system for some items. It requires you to create same Journal Entry every month to credit Deferred Expense account and debit Expense Account. You can create first Journal Entry manually for it, and then create auto-repeat transaction for it.

To access Auto Repeat, go to:
> Home > Settings > Automation > Auto Repeat

## 1. How to set up Auto Repeat

### 1.1 Customize the Form
1. Go to: **Home > Customization > Form Customization > Customize Form**.
2. Select the form in which you want to allow creation of repeatable documents.
3. Check 'Allow Auto Repeat' to allow the creation of repeatable documents for that Form. This is necessary for the document type to show up in the Reference Document field under the Auto Repeat doctype.

 ![Allow Auto Repeat](/files/allow-auto-repeat.png)

### 1.2 Set up Auto Repeat
1. Go to **Home > Settings > Automation > Auto Repeat > New**.
2. Select the Reference Document Type, like Journal Entry or Sales Invoice, etc.
3. Select the Reference Document. This is the individual document that you want to repeat.
4. Set the Start Date and End Date (optional).
 If End Date is not specified, recurring documents will be created, unless the Auto Repeat is disabled.
5. Set the Frequency for creating repeatable documents
 (Daily, Weekly, Monthly, Quarterly, Half-yearly, Yearly).
6. Save.

### 1.3 Set up Auto Repeat directly from the document
You can also set a document on Auto Repeat by clicking the **Repeat** option from the **Menu** in the Toolbar.

**Note**: If a document is already on Auto Repeat, the Repeat option is not available.

![Repeat in Transactions](/files/repeat-option.png)

Once you click on Repeat, a prompt for Auto Repeat will show up. Fill in the details and click on Save.

![Auto Repeat Prompt](/files/auto-repeat-prompt.png)

## 2. Features


### 2.1 Submit on Creation

If the reference document type is submittable, you get an option called _Submit on Creation_. If this is checked, your document will be submitted on creation.

![Auto Repeat Submit on Creation](/files/submit-on-creation.png)

### 2.2 Notify by Email
If you want to notify certain contacts whenever the recurring documents are created, you can check 'Notify by Email' in the Notification section of Auto Repeat. This will send the auto-generated recurring documents to the specified Email Addresses. Fields for the same are explained below:

- **Recipients**: Defines the Email IDs of the recipients for recurring document creation emails.
- **Get Contacts**: This button will fetch the contacts linked to the document that is set on Auto Repeat and fill up the Recipients field with the same.
- **Template**: You can choose an Email Template for the email. This will fill up the Subject and Message fields as well.
- **Subject**: Subject for your Email (example: Recurring ToDo created successfully).
- **Message**: Message to be sent in the Email.
- **Preview Message**: This button will show a preview of the message.
- **Print Format**: Select a print format to define document view which should be emailed to customer.

> **Note**: If the document you are setting up Auto Repeat for, is submittable, ensure that "Allow Print for Draft" is enabled in [Print Settings](/erpnext/print-settings) to receive the new recurring document in Auto Repeat Notification Email. If this is not enabled, you will be notified about the recurring document creation without the document.

### 2.3 Repeat on a particular day
If the frequency is set as Monthly, Quarterly, Half-yearly or Yearly, then it will create recurring documents in the respective months on the same day as the 'Start Date' of Auto Repeat. If you want to create recurring documents on some other day then you can set one of the following:

- **Repeat on Day**: Day of the month on which recurring document will be created. For example, if frequency is Monthly and you enter 7 then it will generate recurring document on 7th of the respective month.
- **Repeat on Last Day of the Month**: This option is available as the last day of every month is different. For example, in a leap year last day of Feb is 29th, and it is 28th otherwise. If you check this option, it will create recurring documents on the last day of the respective months.

### 2.4 Ability to select weekdays for Auto Repeat

> Introduced in version 13

Auto Repeat with Weekly frequency allows you to select the days on which you want the recurring documents to be created.

![Auto Repeat Weekdays](/files/auto-repeat-weekdays.png)

### 2.5 Dashboard

You can see the Auto Repeat schedule in the Dashboard of Auto Repeat document. If you don't specify the End Date then the schedule will show only the Next Schedule Date.

![Auto Repeat Dashboard](/files/auto-repeat-dashboard.png)

### 2.6 Auto Repeat Frequency on the sidebar
When a document is set on Auto Repeat you can see the Auto Repeat frequency on the sidebar.
You can click on the status to see the linked Auto Repeat document.

![Auto Repeat Frequency](/files/auto-repeat-frequency.png)

### 2.7 Disable Auto Repeat
If you check this field it will stop creating recurring documents and unlink the Auto Repeat document from the Reference Document.

<!-- page: erpnext/erpnext__automate_lead_capturing.md -->
---
title: "Automate Lead Creation | ERPNext Documentation"
description: "Learn how ERPNext can create Leads from email, Web Forms, ecommerce activity, and data imports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automate_lead_capturing"
updated: "2026-07-23"
---

Leads come from many different sources. It is important that all leads are recorded, assigned to sales executives and followed up.

## Create Leads From Emails

You may have an email address like '[sales@yourcompany.com](mailto:sales@yourcompany.com)' which is probably displayed on your website. People may send emails asking information about your products and services. You can enable [Email Account](/erpnext/email-account) to pull these emails and create a lead for each email.

## Create Leads From Webforms

You can also map the Lead form to a [Web Form](/erpnext/web-form) and publish it on your website. When visitors of your website fill the form, it will be automatically added as a Lead.

## Create Leads From Incomplete Orders in E-Commerce Module

You can publish an e-commerce website and allow users to place an order for your products. If a user selects items but doesn't complete the process you can pursue that user as a lead.

## Create Leads By Importing Spreadsheet

If you have a spreadsheet with details of the leads, you can use the [Data Import](/erpnext/data-import) feature to import the leads.

<!-- page: erpnext/erpnext__automating-issue-assignments-to-support-team-in-erpnext.md -->
---
title: "Automating Issue Assignments in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automating-issue-assignments-to-support-team-in-erpnext"
updated: "2026-02-27"
---

Modern support automation tools demonstrably improve customer service. Automating the assignment of support issues ensure that every issue ticket has been assigned a product expert and the customer seeks resolution to their queries faster. Assignment Rule has been introduced in v12 and here's how you can automate your support team's troubles away.  
First, we need to setup an email account that appends the incoming emails received there into the "Issue" DocType of ERPNext.**1) Create an Email Account:**You need to update email domain and setup your support email address in ERPNext's Email Account. To learn about email setup, please check out [this link](https://www.youtube.com/watch?v=ChsFbIuG06g&t=122s)  
![](/files/NPp14kS.png)  
**2) Append to Issue:**The checkbox, "Enable Incoming" has to be selected to allow emails sent on this email address to be received here. We need to capture them in a DocType, which is mentioned under "Appends To". In this case, we want to append all incoming emails to Issue  
![](/files/STAm8ko.png)  
This is a one-time configuration and you won't have to worry about it unless you require to change the password of that email address via third party apps. The Issue List will get populated with the emails that are sent here. With the use of Assignment Rules, we can organise the customer support team's schedule and ensure timely resolution for all open support tickets.  
**3) Setting an Assignment Rule:**  
![](/files/5q4HvOT.gif)  
**4) Based on the rule defined in step (3), the assignments will be done automatically**These are done as in when an Issue is created or updated. Check out below GIF to see automation in action when an issue ticket's status is *updated*:  
![](/files/Qb0kAzo.gif)  
Note: If needed, the rule can also be disabled/updated:  
![](/files/PZbCDuu.png)  
Similarly, you can automate the Sales process in ERPNext for assigning leads to your Sales team and ensure more conversion rates!! Thanks for reading this article! If you need further assistance with this, please reach our community [here](https://discuss.erpnext.com/)

<!-- page: erpnext/erpnext__automation.md -->
---
title: "Automation "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automation"
updated: "2026-03-02"
---

Automation in ERPNext is a game-changer, especially when it comes to streamlining complex processes like milestone tracking, task assignments, repetitive tasks, and event monitoring. These automation features in ERPNext not only save time and effort but also enhance overall efficiency and productivity across the organisation.

* [Assignment Rule](/erpnext/user/manual/en/assignment-rule)
* [Auto Repeat](/erpnext/user/manual/en/auto-repeat)
* [Milestone Tracking](/erpnext/user/manual/en/milestone-tracker)

<!-- page: erpnext/erpnext__awesomebar-global-search.md -->
---
title: "Awesomebar Global Search"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/awesomebar-global-search"
updated: "2026-08-14"
---

The Awesomebar is the fastest way to open a DocType, report, page, workspace, or new record from anywhere in Desk. It reduces menu navigation when you already know what you need.



For example, a billing user can type **Sales Invoice** and choose the list, report, or new-document action directly from the same search.

## Open and use the Awesomebar

1. Select the Search field at the top of Desk, or use the keyboard shortcut shown beside it.
2. Type a DocType, report, page, or action.
3. Use the arrow keys to move through results and press Enter to open the selected result.

![ERPNext Awesomebar showing list, report, and new-document results for Sales Invoice](https://novacompanies.m.frappe.cloud/files/setup-20260814-awesomebar-search.png)



## Understand the results


| Result            | Use it to                                         |
| ----------------- | ------------------------------------------------- |
| List              | Open all records of a DocType.                    |
| New               | Create a new record directly.                     |
| Report            | Open a matching report.                           |
| Page or Workspace | Navigate to a feature or module.                  |
| Search for        | Run a broader global search for matching records. |


## Use global record search

When the direct results do not contain the record you need, choose the broader search action. Search availability depends on the DocType, indexed content, and your permissions. A user will not receive results for records they cannot access.

## Troubleshooting

### A DocType or report is missing

Confirm that the user has the required role and permission. Also check whether the module or workspace is hidden.

### The expected record is not found

Try a distinctive part of its name or identifier. Open the DocType list and apply filters when the record is not included in global search.

## Frequently asked questions

### Does Awesomebar search bypass permissions?

Results respect the current user’s access.

### Can I create a document from the search?

Y

es. Select the **New** result when it is available and you have create permission.

## Related topics

- [Desk](/erpnext/desk)
- [Adding Users](/erpnext/adding-users)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [Show or Hide Modules](/erpnext/show-hide-modules)

<!-- page: erpnext/erpnext__aws_s3.md -->
---
title: "Upload Backups to Amazon S3"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/aws_s3"
updated: "2026-04-15"
---

> Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: [https://frappecloud.com/docs/sites/backups](https://frappecloud.com/docs/sites/backups)

## Prerequisites

- [Email Account](/erpnext/email-account)

To receive emails for failed and successful backups, please create an **Email Account** first.

## Create S3 bucket and set up access

1. Create a new s3 bucket.

In the bucket settings, enable "Block all public access" to keep your data private. Feel free to enable encryption, versioning or object lock as per your requirements (please refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).  
2. Open Identity and Access Management (IAM).  
3. Create a new policy for the Service "S3", allowing the Actions "ListBucket" and "PutObject".

![Screenshot of "Create Policy" in AWS](/files/s3-backup-policy.png)



Or, using the JSON editor:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::YOUR TARGET BUCKET"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "YOUR SERVER IP"
                }
            }
        }
    ]
}
  

```

4. Create a new user for programmatic access.

![Screenshot of "Add User" in AWS](/files/s3_backup_add_user.png)

5. Attach the policy you created to the new user.
6. Copy the user's access key and secret.

To automatically delete old backups or move them to a cheaper storage class, have a look at [lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).



## Create a Hetzner Bucket with Minio

> Capital letters are variables you can choose freely. In this example, we use region nbg1 (Nuremburg).

1. In the Hetzner Console at `https://console.hetzner.com/projects/YOUR_PROJECT/security/s3-credentials` , create some S3 access credentials: key and secret.
2. [Install Minio](https://github.com/minio/minio)
3. Configure Minio to access your Hetzner buckets: `mc alias set MY_ALIAS https://nbg1.your-objectstorage.com YOUR_S3_KEY YOUR_S3_SECRET`
4. Create a bucket with Object Locking enabled: `mc mb MY_ALIAS/BUCKET_NAME --with-lock --region nbg1` . This ensures you cannot accidentally delete your backups.
5. Set Object Locking period to 90 days: `mc retention set GOVERNANCE 90d --default MY_ALIAS/BUCKET_NAME`
6. Check if everything is configured correctly: `mc retention info --json --default MY_ALIAS/BUCKET_NAME`
7. Enter configuration in **S3 Backup Settings**:
  1. *Endpoint URL*: [https://nbg1.your-objectstorage.com/](https://nbg1.your-objectstorage.com/)
  2. *Bucket Name:* `BUCKET_NAME`
  3. *Access Key ID*: `YOUR_S3_KEY`
  4. *Access Key Secret*: `YOUR_S3_SECRET`

## Set up ERPNext

- Open **S3 Backup Settings**.
- Check "Enable Automatic Backup".
- Paste the access key and secret from AWS.
- Set an email address to receive a notification when a backup fails. If you would like an email for successful backups as well, enable "Send Email for Successful Backup".
- Specify the name of the bucket that you created in step 1.
- Choose how often you want to take and upload backups. This can range from monthly to daily. If you only want to take manual backups, set the frequency to "None".

![S3 Backup Settings in ERPNext](/files/s3_backup_settings.png)

## Restore deleted files from versioned bucket

- List all file versions: `mc ls -r --versions MY_ALIAS/BUCKET_NAME/` 
- Download a specific version: `mc get --vid TARGET_VERSION_ID MY_ALIAS/BUCKET_NAME/20260415_162402/20260415_162402-company_frappe_cloud-database.sql.gz ~/Downloads`

<!-- page: erpnext/erpnext__balance-in-temporary-account.md -->
---
title: "Balance in Temporary Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/balance-in-temporary-account"
updated: "2026-07-31"
---

**Question:**

We used Temporary Opening Account for updating opening balance. After having update balance in all the Balance Sheet account, there is still some balance in Temporary Account? What is the cause of this balance, and how to make balance in this account to zero?

 

**Answer:**

When updating an opening balances in ERPNext, you have to first ensure that Balance Sheet in the previous system is tallying (Asset = Liability).

Then you start updating the opening balances for above statement, using Temporary Opening as an account to balance the entry. In the end, when opening is updated for all Asset and Liability accounts, the Temporary account's balance becomes zero automatically.

If you still have balance in the Temporary Account, it could be for one of the two (or both) the reasons.

1. The Balance Sheet followed for updating opening balance was not closed properly and it's Asset and Liability value was not tallying.
2. When updated opening balance in ERPNext, the Temporary Opening Account was not used consistently.

 

Kindly review the above points as they could be the cause of balance left in the Temporary Opening Account.

<!-- page: erpnext/erpnext__balance-sheet.md -->
---
title: "Balance Sheet"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/balance-sheet"
updated: "2026-08-14"
---

Nova Industries ends 2026 with $293,745 of assets, $184,305 of liabilities, and $109,440 of provisional profit. The owner wants to know what the business controls, what it owes, and why its bank balance is negative even though the company is profitable.



The Balance Sheet shows financial position at a point in time. Assets describe resources controlled by the business. Liabilities describe obligations. Equity and current profit explain the owners' residual interest. Use the [Profit and Loss Report](/erpnext/profit-and-loss-report) to explain how profit was earned during a period and [Cash Flow](/erpnext/cash-flow-report) to explain cash movement.

## Before you begin

Submit all relevant [Sales Invoices](/erpnext/sales-invoice), [Purchase Invoices](/erpnext/purchase-invoice), payments, stock transactions, assets, loans, payroll, depreciation, taxes, and approved [Journal Entries](/erpnext/journal-entry). Confirm that accounts have the correct Asset, Liability, or Equity root in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Run the Balance Sheet

1. Open **Accounting** and select **Balance Sheet**.
2. Select **Nova Industries**.
3. Choose Fiscal Year or Date Range and the comparison periodicity.
4. Apply Finance Book, Cost Center, Project, Department, or another [Accounting Dimension](/erpnext/accounting-dimensions) only when required.
5. Refresh and wait for totals, chart, and account rows to load.

![Loaded Nova Industries Balance Sheet with assets liabilities and provisional profit](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-balance-sheet-loaded.png)

## Interpret the Nova Industries result


| Section            | Value    | Meaning                                                           |
| ------------------ | -------- | ----------------------------------------------------------------- |
| Total Assets       | $293,745 | Resources controlled at the reporting date.                       |
| Total Liabilities  | $184,305 | Amounts owed to suppliers and other parties.                      |
| Equity             | $0       | Posted equity balances visible in the selected scope.             |
| Provisional Profit | $109,440 | Current-period profit not yet transferred through period closing. |


Assets equal liabilities plus equity and provisional profit: $293,745 equals $184,305 plus $109,440. This proves the statement balances mathematically. It does not prove that every account is correctly classified.

## Understand the account groups

Current Assets include balances expected to turn into cash or be used soon, such as receivables, bank, cash, and inventory. Fixed Assets support longer-term operations. Current Liabilities include obligations such as supplier payables and taxes. Longer-term loans belong in non-current liabilities. Equity contains owner capital, reserves, retained results, and period-closing transfers according to the organisation's account design.



Nova shows $316,212 in Accounts Receivable and a negative $118,104 Bank Accounts balance. The large receivable explains why the company can own net assets while still facing immediate cash pressure. Open [Accounts Receivable](/erpnext/accounts-receivable) to identify customers to collect from.

## Drill into a balance

Select an account amount to open its [General Ledger](/erpnext/general-ledger) entries. Keep Company, date, Finance Book, currency, and dimensions aligned with the Balance Sheet before comparing values.

![General Ledger drill-down opened from a Balance Sheet account](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-balance-sheet-loaded-drilldown.png)

## Important filters


| Filter                        | Effect                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Reporting date or fiscal year | Sets the point in time and comparison columns.                                                     |
| Accumulated Values            | Shows balances accumulated through each displayed period.                                          |
| Finance Book                  | Restricts entries to a selected accounting book.                                                   |
| Dimensions                    | Shows the financial position for a selected operational segment when entries carry that dimension. |
| Currency                      | Changes presentation without changing ledger postings.                                             |
| Report Template               | Uses a configured [Financial Report Template](/erpnext/financial-report-template).                 |


## Troubleshooting

### The Balance Sheet does not balance

Check provisional profit, opening balances, account roots, period-closing entries, and identical report filters. Trace the difference through Trial Balance and General Ledger.

### An account appears in the wrong section

Review its Root Type and Report Type in Chart of Accounts. Correcting an account can affect reporting and should follow your accounting controls.

### A segment report looks incomplete

Transactions without the selected dimension are excluded. Verify dimension values on source entries before treating the filtered statement as a full-company balance sheet.

## Frequently asked questions

### Why is current profit shown separately from equity?

Profit remains provisional until the period is closed and transferred according to the configured closing process.

### Can a company be profitable but have a negative bank balance?

Profit includes income recognized before collection. Receivables, inventory, debt repayment, and other timing differences can consume cash.

### Does the Balance Sheet show market value?

The statement shows accounting balances produced by recorded transactions and valuation rules, not an automatic market valuation of the business.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Profit and Loss Report](/erpnext/profit-and-loss-report)
- [Cash Flow](/erpnext/cash-flow-report)
- [Trial Balance](/erpnext/trial-balance)
- [General Ledger](/erpnext/general-ledger)
- [Period Closing Voucher](/erpnext/period-closing-voucher)

<!-- page: erpnext/erpnext__bank-account.md -->
---
title: "Bank Account | ERPNext Documentation"
description: "Create ERPNext Company and party Bank Accounts and connect them to the correct bank ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-account"
updated: "2026-07-31"
---

A **Bank Account** represents a real bank or card account held by a Company, Customer, or Supplier. For a Company account, it connects the Bank master to a Bank-type General Ledger account used by payments, statement imports, and reconciliation.

## Before you begin

Create the [Bank](/erpnext/bank) and, for a Company account, a ledger under Bank Accounts in the [Chart of Accounts](/erpnext/chart-of-accounts). Set the ledger's **Account Type** to **Bank** and use the correct Company and currency.

Do not confuse these records:

- the **Bank** is the financial institution;
- the **Bank Account** stores the real account identity and ownership;
- the **Account** is the General Ledger where the Company balance is posted.

## Create a Bank Account

1. Go to **Accounting &gt; Banking &gt; Bank Account**.
2. Select **Add Bank Account**.

![Bank Account list with Add Bank Account highlighted](https://novacompanies.m.frappe.cloud/files/banking-04-bank-account-list.png)

3. Enter an **Account Name** that users can identify, such as `Operating Account` or `Payroll Account`.
4. Select the **Bank**.
5. Select **Is Company Account** when the account belongs to one of your Companies.

![Bank Account ownership and Bank fields](https://novacompanies.m.frappe.cloud/files/banking-05-bank-account-ownership.png)

6. For a Company account, select the **Company** and **Company Account** ledger.
7. Select **Is Default Account** only when this should be the default Bank Account for the Company.

![Company ledger and default Bank Account setting](https://novacompanies.m.frappe.cloud/files/banking-06-bank-account-ledger.png)

8. Enter the account number, routing or branch code, IBAN when applicable, and other non-secret identifiers.
9. Save the Bank Account.

## Create a Customer or Supplier Bank Account

Leave **Is Company Account** clear, then select the **Party Type** and **Party**. Use this for payment instructions, refunds, or other workflows that need the counterparty's banking details.

A party Bank Account does not become a Company ledger and should not be selected as the account that posts Company cash movement.

## Important fields and what they mean


| Field                | What it controls                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Account Name         | Human-readable identifier for the real account.                                                                      |
| Bank                 | Financial institution that holds the account.                                                                        |
| Is Company Account   | Shows Company and ledger fields and marks the account as belonging to your organization.                             |
| Company              | Company that owns the account. It must match the linked General Ledger account.                                      |
| Company Account      | Bank-type General Ledger account used for accounting entries.                                                        |
| Is Default Account   | Makes the Bank Account the default where that workflow uses a Company default. Maintain only one intended default.   |
| Is Credit Card       | Identifies a credit-card account where supported by the workflow.                                                    |
| Party Type and Party | Owner of a Customer, Supplier, Employee, or other party Bank Account.                                                |
| IBAN                 | International account identifier used in participating countries. Leave it empty when the country does not use IBAN. |
| Branch Code          | Routing, sort, transit, or other branch identifier used in your banking system.                                      |
| Bank Account No      | Account number supplied by the institution. Avoid exposing it in public screenshots or broad exports.                |
| Integration ID       | Identifier used by a supported bank integration.                                                                     |
| Disabled             | Prevents the account from being selected for new activity while preserving history.                                  |


## Use the Bank Account

The Company Bank Account is used by:

- [Payment Entry](/erpnext/payment-entry) and payment requests;
- statement synchronization or import;
- [Bank Transaction](/erpnext/bank-transaction) records;
- [Bank Reconciliation](/erpnext/bank-reconciliation);
- [Bank Guarantee](/erpnext/bank-guarantee);
- other banking integrations and reports.

Configure [Mode of Payment](/erpnext/mode-of-payment) Company defaults so cash, check, card, and wire payments use the intended ledger.

## Data protection

Limit access to full bank account numbers and integration identifiers. Documentation and support screenshots should use fictional or masked numbers. Do not store online-banking passwords in the account number, Statement PDF Password, comments, or attachments.

Use **Statement PDF Password** only for the supported encrypted-statement workflow and restrict who can read or modify it.

## Troubleshooting

### The Company Account cannot be selected

Confirm that it belongs to the selected Company, is not a group, is enabled, uses the correct currency, and has **Account Type: Bank**.

### Payments use a different ledger

Check the Mode of Payment Company default, the selected Bank Account, the Company's default Bank Account, and any account filled directly on the transaction.

### Bank Transactions are assigned to the wrong Company

Review the Bank Account ownership and linked ledger. Correct the master before importing more statement lines.

### The IBAN is rejected

Enter an officially valid IBAN without inventing a country prefix. Leave the field empty for accounts in countries that do not use IBAN.

### The account should no longer be used

Disable it instead of deleting it. Historical payments, Bank Transactions, and reconciliation records may still reference it.

## Frequently asked questions

### Can one Bank Account link to several ledgers?

It cannot. Create a separate Bank Account for each real account and Company ledger relationship.

### Can two Companies use accounts at the same Bank?

They can. Use one Bank master and separate Company Bank Accounts and ledgers for each Company.

### Is a credit card a bank or liability account?

The accounting ledger classification depends on your Chart of Accounts and local accounting policy. Mark the Bank Account as a credit card where appropriate and confirm the linked ledger treatment with finance.

## Related topics

- [Bank](/erpnext/bank)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Mode of Payment](/erpnext/mode-of-payment)
- [Payment Entry](/erpnext/payment-entry)
- [Bank Transaction](/erpnext/bank-transaction)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
