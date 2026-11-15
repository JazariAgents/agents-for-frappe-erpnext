<!-- Frappe documentation: erpnext, part 64 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__tax-withholding-category.md -->
---
title: "Tax Withholding Category"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/tax-withholding-category"
updated: "2026-08-03"
---

A Tax Withholding Category tells ERPNext when to deduct or collect tax at source, which rate to use, and which account should receive the amount. It is commonly used when a business must withhold part of a supplier payment and remit it to a tax authority.

For example, Nova Electronics Trading receives an $800 professional-services invoice. Its withholding category uses a 5% rate and a $500 transaction threshold. ERPNext deducts $40 and leaves $760 payable to the supplier.

Tax withholding rules vary by country. Treat the examples as ERPNext configuration guidance, then use the rates, thresholds, accounts, and reporting required by your jurisdiction.

## Before you begin

Prepare:

- The relevant [Supplier](/erpnext/supplier) or Customer.
- A liability or tax Account Head in the [Chart of Accounts](/erpnext/chart-of-accounts) for every company using the category.
- The effective dates and withholding rate.
- The transaction and cumulative thresholds, if applicable.
- Confirmation of whether withholding uses Gross Total or Net Total.

Do not confuse Tax Withholding Category with [Tax Category](/erpnext/tax-category). Tax Category and a [Tax Rule](/erpnext/tax-rule) help select normal transaction-tax templates. Tax Withholding Category controls deductions or collections made at source.

## Create a Tax Withholding Category

Go to **Accounting &gt; Taxes &gt; Tax Withholding Category**, then select **New**.



![Tax Withholding Category list](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-category-list.png)

Enter a specific name, such as **Professional Services Withholding**. In **Category Name**, describe the income or payment class covered by the rule.

Set **Deduct Tax On Basis**:


| Basis       | Meaning                                                                              |
| ----------- | ------------------------------------------------------------------------------------ |
| Gross Total | Uses the transaction amount before deductions defined by the withholding calculation |
| Net Total   | Uses the item net value before ordinary taxes and charges                            |


The correct basis depends on the applicable law. Verify it with your accountant.



![Withholding basis and threshold controls](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-category-overview.png)

## Add rates and thresholds

In **Rates**, add one row for every effective date range and rate combination. Select the pencil icon to edit the complete row.



![Open the withholding-rate child row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-rate-row.png)

Complete these fields:


| Field                 | Meaning                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------- |
| From Date and To Date | The dates for which the rate row is valid                                                   |
| Tax Withholding Group | Selects a group-specific rate when parties are classified into different withholding groups |
| Tax Withholding Rate  | The percentage ERPNext withholds                                                            |
| Transaction Threshold | The amount at which one transaction triggers withholding                                    |
| Cumulative Threshold  | The combined amount at which transactions in the applicable period trigger withholding      |


![Effective dates, rate, and withholding thresholds](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-rate-fields.png)

Current ERPNext uses **From Date** and **To Date** rather than the older Fiscal Year field. Keep date ranges continuous when the same category spans several periods.

## Understand the thresholds

Suppose the rate is 5%, the Transaction Threshold is $500, and the Cumulative Threshold is $2,000.

If one invoice is $800, it crosses the transaction threshold, so withholding applies.

If invoices are $400 each, no individual invoice crosses $500. Withholding can still apply when their relevant cumulative amount reaches $2,000.

The category also provides these controls:


| Option                           | Effect                                                            |
| -------------------------------- | ----------------------------------------------------------------- |
| Disable Transaction Threshold    | Ignores the per-transaction threshold                             |
| Disable Cumulative Threshold     | Ignores the cumulative threshold                                  |
| Only Deduct Tax On Excess Amount | Applies withholding only to the portion above the threshold       |
| Round Off Tax Amount             | Rounds the calculated amount according to ERPNext precision rules |


The older **Consider Entire Party Ledger Amount** option is not present in the current develop form. Do not build a new process around that legacy field without verifying the version in use.

## Add the company account

In **Accounts**, add each company and the Account Head where withholding will be credited or debited according to the transaction. Open the child row using its pencil icon.



![Open the company-account child row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-account-row.png)

Select the company and its matching account. The account must belong to that company.



![Company and withholding account](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-tax-withholding-account-fields.png)

For supplier withholding, the account is normally a liability representing tax withheld and payable to the authority. Confirm its root type and reporting position with your accountant.

## Assign the category to a supplier

Open the Supplier and go to the **Tax** tab. Select the Tax Withholding Category.



![Tax Withholding Category assigned to a supplier](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-supplier-tax-withholding.png)

Use **Tax Withholding Group** when one category has group-specific rate rows, such as different rates for organizations and individuals. The supplier's group helps ERPNext select the matching rate row inside the category.

## Apply withholding on a Purchase Invoice

Create a [Purchase Invoice](/erpnext/purchase-invoice) for the supplier. ERPNext shows **Consider for Tax Withholding** when the transaction is eligible.



![Consider a Purchase Invoice for tax withholding](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-purchase-invoice-consider-withholding.png)

When selected, ERPNext evaluates the category, effective rate, group, basis, thresholds, and earlier relevant transactions. In the example:


| Calculation                | Amount  |
| -------------------------- | -------: |
| Net Total                  | $800.00 |
| Withholding at 5%          | $40.00  |
| Amount payable to supplier | $760.00 |


ERPNext adds the $40 as a deduction in Purchase Taxes and Charges.



![Withholding deducted from the Purchase Invoice total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-purchase-invoice-withholding-result.png)

The **Tax Withholding Entries** table records the category, taxable base, rate, amount, and source document. Use it to understand the calculation rather than relying only on Grand Total.



![Detailed withholding entry on the Purchase Invoice](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-purchase-invoice-withholding-entry.png)

On submission, a simple expense invoice normally debits the expense, credits the supplier payable for the net amount, and credits the withholding liability for the withheld amount. Review the [General Ledger](/erpnext/general-ledger) because actual postings depend on the transaction and accounts.

## Withhold tax on a supplier advance

Withholding may be due when an advance is paid against a [Purchase Order](/erpnext/purchase-order), before a Purchase Invoice exists.

1. Create a [Payment Entry](/erpnext/payment-entry) with Payment Type **Pay**.
2. Select Party Type **Supplier** and the supplier.
3. Enter the advance amount before withholding.
4. Select **Consider for Tax Withholding**.
5. Confirm the Tax Withholding Category.
6. Save and review the generated Tax Withholding Entry before submission.

![Apply withholding to a supplier advance in Payment Entry](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-payment-entry-consider-withholding.png)



![Withholding entry calculated for the supplier advance](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-withholding-category-payment-entry-withholding-entry.png)

When the Purchase Invoice is created later, allocate the advance through the normal advance-allocation workflow. ERPNext uses the withholding entries to determine whether additional tax remains. Test this workflow with your jurisdiction's rules because timing requirements differ.

## Customer-side tax collection

Some regional rules require a seller to collect tax from an eligible customer after a threshold. ERPNext can use a Tax Withholding Category on a Customer for such rules where the localization supports the workflow.

Assign the category to the [Customer](/erpnext/customer), configure the correct rate and threshold, and test a [Sales Invoice](/erpnext/sales-invoice). When **Only Deduct Tax On Excess Amount** is enabled, ERPNext applies the rate only to the portion above the threshold.

Do not reuse a supplier-deduction account blindly for customer-side collection. Configure the correct company account and confirm the statutory report supplied by the regional app.

## Override or ignore thresholds carefully

Current transactions can expose **Ignore Tax Withholding Threshold** and **Edit Tax Withholding Entries**. Use them only when a documented exception requires a manual result.

Before overriding, capture the reason, supporting certificate or approval, correct taxable base, effective rate, and expected withholding. Review the resulting taxes table, detailed entries, and ledger posting. Manual edits bypass part of the protection provided by the category.

## Troubleshooting

### Consider for Tax Withholding does not appear

Confirm the party has a Tax Withholding Category, the transaction supports withholding, and the category has a valid rate row and company account.

### No tax is deducted from the invoice

The transaction may be below both thresholds, outside the rate dates, assigned to a group with no matching row, or using a disabled threshold combination. Inspect Tax Withholding Entries and the category settings.

### ERPNext uses the wrong rate

Check Posting Date, From Date, To Date, Tax Withholding Group, and overlapping rate rows. Avoid overlapping rows that could both match the same party and date.

### Advance withholding is repeated on the invoice

Confirm the Payment Entry is allocated correctly and inspect both documents' withholding entries. Do not add a manual deduction when ERPNext has already recognized the advance withholding.

## Frequently asked questions

### What is the difference between transaction and cumulative thresholds?

The transaction threshold evaluates one document. The cumulative threshold evaluates the relevant combined amount across transactions for the party and period.

### Does reaching a threshold apply tax to the entire amount?

Normally it can. Enable Only Deduct Tax On Excess Amount when the governing rule applies tax only to the portion above the threshold.

### Can different companies use the same category?

Y

es. Add a company-specific account row for each company and ensure the rate and legal treatment are genuinely shared.

### Can I withhold at payment instead of invoice?

Yes, Payment Entry supports withholding for supplier advances and payment-time workflows. Avoid applying it again on the invoice for the same taxable amount.

### Why is the supplier paid less than the invoice expense?

The withheld amount is owed to the tax authority instead of the supplier. The expense remains based on the taxable purchase, while payable is split between supplier and withholding liability.

## Related topics

- [Supplier](/erpnext/supplier)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Tax Category](/erpnext/tax-category)
- [Taxes](/erpnext/taxes)
- [Chart of Accounts](/erpnext/chart-of-accounts)

<!-- page: erpnext/erpnext__taxes.md -->
---
title: "Taxes"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/taxes"
updated: "2026-08-03"
---

ERPNext calculates taxes on sales and purchase transactions from reusable accounts, templates, categories, rules, and item-specific rates. The system can select the applicable setup automatically, show the calculation before submission, and post the tax amount to the correct General Ledger account.



ERPNext provides the calculation framework. It does not decide the tax rates, recoverability, filing treatment, or legal rules for your business. Confirm those requirements with a qualified tax adviser and use the relevant [regional documentation](/erpnext/regional) when a localization app changes the standard workflow.

## Understand the tax setup


| Record                                                                              | What it controls                                                    | Typical example                              |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| Tax account                                                                         | Where tax is posted in the ledger                                   | Output Sales Tax Payable or Input Tax Credit |
| [Tax Category](/erpnext/tax-category)                                               | The tax treatment that applies to a party or transaction            | Standard, exempt, domestic, or export        |
| [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)       | Tax rows used on selling transactions                               | 8% sales tax on Net Total                    |
| [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) | Tax rows used on buying transactions                                | 5% recoverable purchase tax                  |
| [Tax Rule](/erpnext/tax-rule)                                                       | Conditions that select a sales or purchase template                 | Apply Standard Tax to a customer category    |
| [Item Tax Template](/erpnext/item-tax-template)                                     | A rate that overrides the transaction tax rate for particular items | A reduced rate or zero-rated item            |
| [Tax Withholding Category](/erpnext/tax-withholding-category)                       | Tax deducted when paying a supplier or receiving certain payments   | Supplier withholding with thresholds         |


A simple setup usually starts with one output tax account, one input tax account, one sales template, one purchase template, and a small number of categories and rules. Add more records only when rates or treatments genuinely differ.

## Before you begin

Confirm the following for every company and tax treatment you intend to use:

- Which sales taxes you collect and which purchase taxes you can recover
- The correct rates, taxable basis, effective dates, and exemptions
- Whether a charge affects the invoice total, item valuation, or both
- The accounts in which output tax, recoverable input tax, and non-recoverable tax must be posted
- The reports, identifiers, and electronic filing features supplied by your localization

Test the setup in a non-production company with representative invoices, discounts, returns, and mixed-rate items before using it for live transactions.

## Create the Tax Accounts

Open the Chart of Accounts and create the accounts required by your accounting policy.

For sales, output tax collected from a customer is normally a liability because it is payable to the tax authority. For purchases, recoverable input tax is normally an asset because it can be claimed or offset. A non-recoverable purchase tax may instead be added to valuation or posted as an expense.

Use separate sales and purchase accounts when you need to report collected and recoverable tax independently. Select the relevant company on each tax account.

## Create a Tax Category

A Tax Category gives a name to a tax treatment. It can be assigned to a Customer, Supplier, Address, tax template, or transaction and used by a Tax Rule to select the correct template.

Create categories that describe the treatment, not a single transaction. Examples include **Standard Tax**, **Export**, and **Exempt**.



![The Standard Tax category in ERPNext](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-tax-category.png)

If a category should no longer be selected, enable **Disabled** instead of deleting a record already referenced by transactions.

## Create sales and purchase tax templates

Create a Sales Taxes and Charges Template for taxes collected from customers. Select the company and Tax Category, then add one row for every tax or charge component. In each row, select the calculation type, account, rate, and description.



![A reusable 8 percent sales tax template](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-sales-tax-template.png)

Create a separate purchase template for taxes charged by suppliers. Use the input tax account when the tax is recoverable. When it is not recoverable, decide with your accountant whether it should affect valuation or an expense account. See [Include Tax or Charge in Valuation or Total?](/erpnext/include-tax-or-charge-in-valuation-or-total) for the available treatments.



![A reusable 5 percent purchase tax template](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-purchase-tax-template.png)

Mark a template as default only if it applies to most transactions for that company. Otherwise, let a Tax Rule select it or choose it manually.

## Select a template automatically with a Tax Rule

A Tax Rule matches transaction context to a template. It can consider the company, tax category, customer or supplier, groups, items, locations, dates, and priority.

In this example, a sales rule applies the **Nova Standard Sales Tax 8%** template to Northstar Retail when **Standard Tax** is selected.



![A Tax Rule that selects the standard sales tax template](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-sales-tax-rule.png)

Keep rules mutually exclusive where possible. If more than one rule can match, use a clear priority and non-overlapping conditions. When troubleshooting, check the transaction date and every condition on the rule, not only the Tax Category.

## Review tax on a transaction

Create a draft [Sales Invoice](/erpnext/sales-invoice) or Purchase Invoice. Select the party and items, then review the Tax Category, selected template, every row under Taxes and Charges, Total Taxes and Charges, and Grand Total.



In the example below, an invoice with a net total of $699 uses an 8% output tax row. ERPNext calculates $55.92 of tax and a grand total of $754.92.



![Tax category, template, row calculation, and invoice totals](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-sales-invoice-tax-row.png)

Do not rely only on the template name. Confirm the account, rate, taxable basis, and amount on the transaction. A user can change a draft transaction, and a category or rule can select a different template from the one expected.

After submission, the calculated amount becomes part of the accounting entry.



![Submitted Sales Invoice tax and grand total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-submitted-sales-invoice-tax-total.png)

## Understand the General Ledger impact

For the example sale, ERPNext posts the following entries:


| Account                  | Debit   | Credit  | Meaning                                     |
| ------------------------ | -------: | -------: | ------------------------------------------- |
| Debtors                  | $754.92 |         | Total amount owed by the customer           |
| Sales                    |         | $699.00 | Revenue before tax                          |
| Output Sales Tax Payable |         | $55.92  | Tax collected and owed to the tax authority |


![General Ledger entries for the taxed Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-taxes-overview-sales-tax-general-ledger.png)

On a purchase with recoverable input tax, ERPNext normally debits the input tax asset and credits the supplier for the tax-inclusive total. The exact entries depend on the selected accounts, perpetual inventory, and whether the tax affects valuation.

## Handle special tax calculations

Use the calculation type in each template row to control the taxable basis.

**On Net Total** calculates a rate on the transaction's net item value. **On Previous Row Total** calculates on the running total after an earlier row. **On Previous Row Amount** calculates only on the amount produced by an earlier row. See [Apply Tax on Another Tax or Charge](/erpnext/how-to-apply-tax-on-tax) and [Tax on another tax amount](/erpnext/v14/user/manual/en/accounts/articles/tax-on-another-tax-amount) for worked examples.



If item rates already include tax, use [Tax Inclusive Accounting](/erpnext/tax-inclusive-accounting) so ERPNext separates the included tax from income or expense. Use [Types in Tax Template](/erpnext/types-in-tax-template) to understand the complete list of row calculation options.



For items with different rates or exemptions on the same transaction, configure Item Tax Templates and ensure the matching tax account is present in the transaction's Taxes and Charges table. An item template overrides the rate for its item; it does not replace the transaction tax row or its account.

## Use withholding and regional tax features

Withholding is different from transaction tax. It records an amount deducted from a payment according to a category, rate, and threshold. For regional Indian requirements, a [Lower Deduction Certificate](/erpnext/lower-deduction-certificate) can apply a reduced or nil withholding rate when the supplier holds a valid certificate.

Local compliance apps can add statutory fields, reports, e-invoicing, withholding behavior, and validations. Follow their documentation where it differs from the generic ERPNext setup.

## Troubleshooting

### The expected tax template is not selected

Check the company, Tax Category, party, address, transaction date, rule validity, and priority. Confirm that the rule points to a template of the same transaction type. If you changed the category after adding items, re-check the tax template and item rows before saving.

### Tax is missing or wrong for one item

Open the item row and verify its Item Tax Template. Confirm that the same tax account exists in the Sales or Purchase Taxes and Charges table. The item template supplies an overriding rate only for matching accounts.

### The tax is calculated on the wrong amount

Check the row's calculation type and Reference Row number. **On Previous Row Total** and **On Previous Row Amount** produce different results. Also confirm whether discounts are applied before or after the referenced tax row.

### The invoice total is correct but the ledger account is wrong

Open the selected tax template and verify the Account Head and company. Then review the submitted transaction's General Ledger. Correct the configuration before cancelling and amending any affected transaction.

## Frequently asked questions

### Does a Tax Category calculate tax by itself?

A Tax Category identifies the treatment. A template contains the calculation rows, while a Tax Rule can use the category and other conditions to select that template.

### Should sales tax and purchase tax use the same account?

That depends on your accounting and reporting requirements. Many businesses use separate output tax liability and input tax asset accounts so collected and recoverable tax remain visible. Confirm the required structure with your accountant.

### Why did changing the Tax Category not refresh every item tax?

Item-specific tax is resolved from the transaction context and the item's matching template. If the category changes after items are added, review the item rows and tax table again. Remove and re-add an affected item when necessary, then confirm the calculation before submission.

### Can ERPNext determine the legally correct tax rate automatically?

ERPNext applies the rates and rules you configure. A localization or integration may supply additional logic, but your organization remains responsible for configuring, validating, and maintaining the correct statutory treatment.

### How do I record a bank fee deducted from a customer payment?

That is a payment difference, not a transaction tax. Record it in the Deductions or Loss section of the Payment Entry as described in [Additional Charges in Payment](/erpnext/handing-deductions-in-payment-entry).

## Related topics

- [Tax Category](/erpnext/tax-category)
- [Tax Rule](/erpnext/tax-rule)
- [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Item Tax Template](/erpnext/item-tax-template)
- [Tax Withholding Category](/erpnext/tax-withholding-category)
- [Tax Inclusive Accounting](/erpnext/tax-inclusive-accounting)

<!-- page: erpnext/erpnext__taxjar_integration.md -->
---
title: "Taxjar Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/taxjar_integration"
updated: "2026-05-29"
---

TaxJar integration allows ERPNext users to auto-calculate taxes based on the addresses of customers, companies and delivery locations.

## How to Setup TaxJar?

### TaxJar Account and API Tokens:

You will need the API tokens from your account to setup Taxjar.

1. Create a [Taxjar account](https://www.taxjar.com/) first as per your requirements.
2. Login to your account dashboard and click on the **Account** button and click on **TaxJar API** in the dropdown list of options.
  ![](/files/CjhmW8k.png)
3. You will now see your API tokens, these tokens would be needed to configure your ERPNext TaxJar integration.
  ![](/files/FVvmUN1.png)

### Adding Nexus and states in TaxJar:

**What is Nexus?**

You don't need to register to collect sales taxes from customers in every state. You'll only collect sales taxes from customers who live in the states where you have nexus!

"Nexus" is a specific type of connection to a state that's significant enough for you to be required to comply with that state's sales tax laws.

**How do I know where I have Nexus?**

You'll always have nexus in your home state where you are located.

For more details, please read up on the official [TaxJar page about Nexus](https://support.taxjar.com/article/115-how-do-i-know-where-i-have-nexus) without fail!

**Adding states:**

Please follow detailed instructions given on the official TaxJar page [here](https://support.taxjar.com/article/116-add-or-remove-states-from-your-dashboard) regarding adding/removing states to your dashboard, please follow their instructions from top to bottom as it will help you set up everything perfectly.

### Setting up TaxJar on ERPNext:

From the Desktop click on the '**TaskJar**' icon. This will redirect you to the TaxJar Workspace.

![](/files/image8570fc.png)
*Frappe Desktop with TaxJar desktop icon*

Click on '**TaxJar Settings**'. This is where you configure your TaxJar integration in ERPNext.

![](/files/image3844e2.png)
*TaxJar Workspace*

Fill

![](/files/image37c2c5.png)
*TaxJar Settings Form View*



**Sandbox Mode:**

TaxJar provides a sandbox environment for automated testing and development. After generating a sandbox API token, point your API client to the sandbox environment: [https://api.sandbox.taxjar.com](https://api.sandbox.taxjar.com)]. Note sandbox transactions will not reflect in your TaxJar dashboard. To troubleshoot during development use the TaxJar API Log.

**Logging:**

- When Enable TaxJar Logging is checked in **TaxJar Settings**, TaxJar requests/responses/skips/errors are written to TaxJar API Log and file logs.
- When Enable TaxJar Logging is unchecked, tax logic still runs, but no new TaxJar log entries are written.

![](/files/image1b3264.png)
*TaxJar API Log List View*

Payload and responsed a stored in the Log,

![](/files/image233747.png)
*TaxJar API Log Form View*

**Setting up tokens and account heads:**

1. Enable Tax Calculation, Create TaxJar Transaction:
2. You need to enable these options for auto tax calculations and these transactions would appear on your TaxJar account transactions page where you can track them and analyse the tax breakdowns.
3. Once you've made some transactions, they would automatically appear on your TaxJar **Transactions** page:![](/files/o54QVVm.gif)
4. You can check out all the transactions made and the detailed tax breakdowns.
5. Copy the API tokens from your TaxJar account as directed above and paste it in the **Live API Key** and **Sandbox API key field.**
6. You will have to set two account heads for Taxes and Shipping, select the accounts as required and once everything has been configured, click on save and you are good to go!

### Setting correct addresses

For the integration to work seamlessly please make sure you have created correct addresses for your company, customers, suppliers, etc.

**Note:**

1. While creating an address, make sure in the **State/Province** field you enter the correct state. TaxJar requires the 2 letter format for the states for ex. New York is considered as NY, but it **need not be** mandatorily entered that way, the system converts it to the 2-letter state code automatically.
  ![](/files/image2b9f56.png)
  *Address Form View*
2. You may check the **Preferred Billing Address** and **Preferred Shipping Address** checkboxes to auto-fill those fields in different invoices and avoid the hassle.
3. Ensure that you have correctly filled the **City/Town, State/Province, Country, Postal Code** fields.
4. You might want to disable the taxes if any, that are set by default.

### TaxJar in Action!

In this instance we have a company that is based out in **New York** and we are issuing a Sales Invoice to a customer based within the same state.

![](/files/SvGCGB3.gif)

As you see, the taxes and charges based on the state and pincode gets applied automatically on saving.

<!-- page: erpnext/erpnext__tds-setup-india.md -->
---
title: "TDS Setup for India"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/tds-setup-india"
updated: "2026-02-26"
---

To setup ***TDS*** in ERPNext follow below steps:

  
  


* First you have to define Tax withholding categories, by default 28 categories are already pre-defined as per Indian statutory compliances. But if you want to add new category then you can create the same by clicking on "New"(button at right top corner)

![](/files/Oq1mP48.png)  


* As per category you have to define Tax withholding rate along with "Single Transaction Threshold" & "Cumulative Transaction Threshold" for Financial/Fiscal year.

![](/files/MELGDIu.png)  


* In same screen you will find another section of "Account Detail" to set company-wise TDS Payable account.

![](/files/IIB6N8R.png)  


* Once you are done with Tax withholding setup go to Supplier master and assign Tax withholding category.

![](/files/aThoNuR.png)  


* Now when you create a Purchase invoice against that supplier make sure "Apply Tax withholding Amount" is checked then only system will auto fetch TDS Payable amount in "Taxes & Charges" table based on Threshold you have defined.

![](/files/zyZdwsr.png)  


![](/files/XUJEgQ7.png)  


Standard report is also available to check monthly payable, just search for "TDS payable monthly" report for the same.

<!-- page: erpnext/erpnext__terms-and-conditions.md -->
---
title: "Terms and Conditions | ERPNext Documentation"
description: "Learn how to create, apply, print, and manage reusable Terms and Conditions templates across ERPNext sales, buying, and HR transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/terms-and-conditions"
updated: "2026-07-23"
---

Terms and Conditions in ERPNext are reusable clauses that describe the commercial, delivery, warranty, return, and other conditions that apply to a transaction. A template helps your team use approved wording consistently instead of rewriting the same text for every Quotation, Sales Order, or purchase document.

ERPNext copies the selected template into the transaction. Users can review or edit the copied text before submitting the document, subject to your organization’s approval process. Because the wording may create legal obligations, have qualified legal or commercial reviewers approve every template used by your business.

## Before you begin

- Confirm the approved wording with your legal, finance, sales, and operations teams.
- Decide which ERPNext modules should be allowed to use the template.
- Create supporting records such as [Payment Terms](/erpnext/payment-terms), [Incoterms](/erpnext/incoterm), and shipping rules separately. Do not rely on narrative wording when ERPNext has a structured field for the same control.
- Choose a clear template naming convention, such as Sales Standard, Export Sales, Purchase Standard, or Service Engagement.
- Review the active [Print Format](/erpnext/print-format) to confirm that it displays Terms and Conditions.

## Create a Terms and Conditions template

1. Go to **Selling > Settings > Terms and Conditions**.
2. Select **Add Terms and Conditions**.
3. Enter a descriptive Title.
4. Select the Applicable Modules.
5. Enable **Copy Attachments to Transaction** when files attached to this template should be copied to documents that use it.
6. Enter and format the approved wording in **Terms and Conditions**.
7. Save the template.

![ERPNext Terms and Conditions template with module and attachment controls highlighted](https://novacompanies.m.frappe.cloud/files/template6d9024.png)

The example is limited to Selling and contains reusable commercial terms for Nova Electronics Trading. 

## Alternative ways to add Terms and Conditions

### Select a template in a transaction

1. Open or create a supported transaction such as a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).
2. Open the **Terms** tab.
3. In the Terms and Conditions section, select the required template in **Terms**.
4. Review the copied text in **Terms and Conditions Details**.
5. Edit transaction-specific details when permitted, then save the document.

![Sales Order Terms tab with the Terms template field highlighted](https://novacompanies.m.frappe.cloud/files/sales-order-termsdec98f.png)

The highlighted field selects Nova Standard Sales Terms. ERPNext copies the template content below it, where the terms can be reviewed before the document is submitted.

### Enter transaction-specific terms without a template

You can enter text directly in Terms and Conditions Details when the conditions apply only to one transaction. Use this for a genuine exception, not as a replacement for an approved reusable template. Ask the appropriate reviewer to approve material changes before the document is sent or submitted.

### Use a template in buying or HR

Enable Buying or HR on the template when its wording is intended for those modules. For example, a Purchase Order may need supplier delivery and inspection clauses, while an HR document may require employment-related wording. Keep unrelated conditions in separate templates so users see only appropriate choices.

## Important fields and what they mean


| Field                           | What it means                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title                           | The name users select in a transaction. Include the purpose, region, or document type when several templates exist.                                               |
| Disabled                        | Prevents new transactions from selecting the template without deleting its historical record.                                                                     |
| Copy Attachments to Transaction | Copies files attached to the template into a transaction that uses it. Use this for approved schedules or policy documents that must travel with the transaction. |
| Selling                         | Makes the template available to supported Selling documents.                                                                                                      |
| Buying                          | Makes the template available to supported Buying documents.                                                                                                       |
| HR                              | Makes the template available to supported HR documents when the installed application supports it.                                                                |
| Terms and Conditions            | The reusable rich-text content copied into a transaction.                                                                                                         |
| Terms                           | The template link selected on a transaction.                                                                                                                      |
| Terms and Conditions Details    | The copied transaction text. Changes here affect this transaction, not the original template.                                                                     |


## What should Terms and Conditions contain?

Avoid copying generic terms from another company or jurisdiction. ERPNext stores and displays your approved text, but it does not determine whether the wording is legally suitable.

## Use structured fields with narrative terms

Terms and Conditions complement ERPNext fields rather than replacing them. Use structured fields wherever possible:


| Requirement             | Recommended ERPNext control                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| When payment is due     | Use a Payment Terms Template and Payment Schedule. Summarize special conditions in the narrative terms only when necessary. |
| Shipping responsibility | Use Incoterm and Named Place fields, then add explanatory wording if required.                                              |
| Delivery commitment     | Use transaction and item Delivery Dates.                                                                                    |
| Tax calculation         | Use the appropriate [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template).                          |
| Currency and pricing    | Use Currency, [Price List](/erpnext/price-list), and transaction rates.                                                     |


Structured fields support calculations, reports, and downstream documents. Narrative terms provide the additional contractual explanation.

## Use attachments with a template

Attach a file to the Terms and Conditions record when users must send an approved schedule, warranty statement, specification, or policy with the transaction. Enable **Copy Attachments to Transaction** so ERPNext copies those files when the template is selected.

Before relying on this option, test the complete workflow. Confirm that the attachment appears on the transaction and that your email or document-sharing process includes it. Review attachment permissions and avoid placing confidential documents in a broadly available template.

## Use variables with Jinja

Terms and Conditions support Jinja expressions, which can insert values from the transaction into the copied content. For example, a Sales Order template can reference its document name or delivery date:

```python
Order reference: {{ name }}
Order date: {{ transaction_date }}
Expected delivery: {{ delivery_date }}
```

Use field names that exist on the transaction. Test the template on a draft document before using it operationally. Keep important obligations understandable even when an optional value is empty. For background, see [Jinja templating in ERPNext](/erpnext/jinja).

## Print and share the terms

Once terms are present in a transaction, they can appear in its print view, PDF, or email attachment if the selected Print Format includes that field.



1. Open the transaction.
2. Select **Print**.
3. Choose the required Print Format and language.
4. Review the Terms and Conditions section.
5. Print the document or generate its PDF.

![ERPNext Sales Order print preview showing the Terms and Conditions section](https://novacompanies.m.frappe.cloud/files/print-preview7724b8.png)

The preview shows the commercial terms after the Sales Order totals. Always inspect the final document before sending it to the Customer.

## Submit and next steps

Review the copied wording together with the Customer, items, delivery dates, payment schedule, taxes, and totals. Save and submit the transaction only after the commercial terms match the agreement. The submitted [Sales Invoice](/erpnext/sales-invoice), Delivery Note, or another downstream document may use its own template and print format, so confirm the terms required at each stage.

Changing the reusable template later does not rewrite already created transactions. Update an existing draft transaction by selecting the template again or editing its copied terms. Do not silently replace terms on a submitted document. Follow the applicable amendment or cancellation process.

## Good practices

- Give every template a clear owner and review date.
- Keep sales, purchase, service, export, and HR wording separate.
- Disable superseded templates instead of deleting records needed for audit history.
- Limit editing permissions for approved templates using [Role-Based Permissions](/erpnext/role-based-permissions).
- Test Jinja variables, attachments, print formats, and translations before rollout.
- Use a short standard template for routine transactions and separate schedules for complex obligations.

## Troubleshooting

### The template does not appear in a transaction

Confirm that it is not disabled and that the correct Applicable Module is enabled. Also check that the transaction supports Terms and Conditions and that the user can read the template.

### Selecting the template does not update the text

Save the template, then select it again in the transaction. If text was already edited in the transaction, confirm before replacing it so approved changes are not lost.

### Terms do not appear in print

Confirm that the transaction contains Terms and Conditions Details. Then inspect the selected Print Format and verify that it displays the terms field. A custom format may omit it.

### Jinja values are blank or incorrect

Verify the field name on the source DocType and confirm that the field contains a value. Test the expression on a draft transaction and avoid using fields that are unavailable on that document type.

### An attachment was not copied

Confirm that the file is attached to the template and that Copy Attachments to Transaction is enabled before selecting the template. Check the Attachments section on the transaction.

## Frequently asked questions

### Can I edit the terms after selecting a template?

Yes. The text is copied into the transaction and can be adjusted before submission, subject to your approval process. The original template is not changed.

### Can I use one template for sales and purchases?

ERPNext allows multiple Applicable Modules, but separate templates are usually clearer because customer and supplier obligations differ.

### Will changing a template update old transactions?

No. Existing transactions keep the text that was copied when the template was selected.

### Can Terms and Conditions replace Payment Terms?

No. Use Payment Terms and the Payment Schedule for due dates and invoice portions. Use narrative terms for the additional contractual explanation.

### Can the same terms be printed in another language?

Create and approve the required translated wording and confirm the selected print language and format. Do not assume that ERPNext will legally translate custom contractual text.
