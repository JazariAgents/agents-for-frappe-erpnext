<!-- Frappe documentation: erpnext, part 28 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__handing-deductions-in-payment-entry.md -->
---
title: "Additional Charges in Payment | ERPNext Documentation"
description: "Record bank fees, withholding, write-offs, and other payment differences in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/handing-deductions-in-payment-entry"
updated: "2026-08-01"
---

A payment can differ from an invoice because of bank charges, withholding, exchange differences, or an approved write-off. Record each difference explicitly in the Deductions or Loss table instead of changing the invoice value.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Additional Charges in Payment

1. Enter the actual amount paid or received.
2. Allocate the intended amount against the invoice references.
3. Open **Deductions or Loss** and add one row for each difference.
4. Select the correct ledger, amount, Cost Center, and explanation.
5. Confirm that the Difference Amount is zero and submit.

[Screenshot on the live page: Additional Charges in Payment in ERPNext]

## Important fields and what they mean


| Field                 | What it controls                                          |
| --------------------- | --------------------------------------------------------- |
| Account               | Ledger that explains the charge or deduction.             |
| Cost Center           | Required reporting dimension for the amount.              |
| Amount                | Signed value needed to balance the Payment Entry.         |
| Difference Amount     | Balance still unexplained.                                |
| Exchange Gain or Loss | Difference caused by currency conversion when applicable. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### Difference Amount is not zero after adding a deduction

Confirm the actual bank amount, invoice allocation, and whether the deduction should be added or subtracted. The allocated amount commonly represents the amount clearing the invoice, while the bank amount reflects cash movement.

### A bank charge was posted as a tax

Use **Deductions or Losses** with the bank charges account. Taxes and Charges is for amounts connected to the party transaction, not a fee retained by the bank.

### A deduction unexpectedly changes the customer or supplier balance

Review the account head and whether it is a party receivable or payable account. Deductions such as fees, withholding, discounts, and exchange differences require different ledger accounts.

## Frequently asked questions

### Which differences belong in Deductions or Losses?

Common examples include bank charges, exchange gains or losses, write-offs, withholding, and approved settlement differences. Each line should have an explicit account and business explanation.

### Should the source invoice be edited to match the payment?

Keep a valid submitted invoice unchanged. Record the actual payment and account for the legitimate difference in the Payment Entry or another supported adjustment.

### Can several deductions be recorded in one Payment Entry?

Several lines can be used when the settlement contains distinct components. Use separate accounts so the ledger and audit trail remain clear.

### Can deductions be negative?

Use signs and Add or Deduct behavior only according to the field's accounting logic. Preview the ledger impact because a negative amount can reverse the intended account effect.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__handling-excess-customer-payments.md -->
---
title: "Handling Excess Customer Payments | ERPNext Documentation"
description: "Record overpayments and keep the excess available for future ERPNext invoices or refunds."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/handling-excess-customer-payments"
updated: "2026-08-01"
---

If a Customer pays more than the invoice balance, allocate only the amount that clears the invoice. Leave the excess unallocated as a Customer advance, then apply it to a future invoice or refund it through an approved payment.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Handling Excess Customer Payments

1. Record the full amount received in one Payment Entry.
2. Allocate the invoice balance in References.
3. Leave the remaining amount unallocated.
4. Use Payment Reconciliation to apply the balance to a later invoice, or create a controlled refund.
5. Review the Customer ledger after the allocation or refund.

[Screenshot on the live page: Customer payment with the invoice allocated and the excess left unallocated]

## Important fields and what they mean


| Field              | What it controls                         |
| ------------------ | ---------------------------------------- |
| Paid Amount        | Full cash received.                      |
| Allocated Amount   | Amount used to clear current invoices.   |
| Unallocated Amount | Customer credit available for later use. |
| Party              | Customer who owns the credit.            |
| Reference No       | Bank evidence for the overpayment.       |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The excess amount does not appear on a later invoice

Confirm that it remains unallocated for the same Customer, Company, currency, and receivable account. Fetch advances on a draft invoice or use Payment Reconciliation for a submitted invoice.

### An extra gateway surcharge appears as a customer advance

ERPNext treats money received above invoice allocations as an unallocated balance. If the extra amount is revenue or fee recovery rather than customer credit, invoice or account for it through the appropriate supported workflow.

### The excess was allocated to the wrong invoice

Use Unreconcile Payments and then Payment Reconciliation when only the allocation is wrong. Cancel and amend the Payment Entry when the money, party, or ledger account is incorrect.

## Frequently asked questions

### What happens when a customer pays more than the invoice total?

Allocate the invoice amount and leave the remainder unallocated. ERPNext can treat that balance as an advance available to the same Customer.

### Can the excess be refunded?

Use a traceable outgoing payment or approved adjustment that clears the customer balance. Preserve the original receipt and reference the reason for the refund.

### Can an excess payment be transferred to another customer?

Do not change the party on the original receipt. Use an approved accounting transfer with a clear audit trail and authorization when the credit genuinely belongs to another party.

### Does an unallocated payment reduce a specific invoice's outstanding amount?

It does not reduce an invoice until it is allocated. The party may have an overall credit while individual invoices remain outstanding.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__help-articles.md -->
---
title: "Help Articles Index"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/help-articles"
updated: "2026-07-05"
---

Below is a few help articles which can help you configure the system as per your requirements.

### System

- [Document Versioning](/erpnext/document-versioning)
- [Adding Attachment to Ongoing Messages](/erpnext/adding-attachments-to-outgoing-messages)
- [Copy Pasting Multiple Records](/erpnext/copy-pasting-multiple-records-from-excel)
- [Renaming Documents](/erpnext/renaming-documents)
- [Bulk Rename](/erpnext/bulk-rename)
- [Deleting and restoring Documents](/erpnext/how-to-restore-deleted-documents-in-erpnext)
- [Deleting Custom Reports](/erpnext/deleting-custom-reports)
- [Restore Deleted Documents](/erpnext/how-to-restore-deleted-documents-in-erpnext)
- [Duplicate Records](/erpnext/duplicate-record)
- [Checking Link Between Documents](/erpnext/check-link-between-documents)
- [Filter Option in Select Field](/erpnext/filter-options-in-select-field)
- [Automating Assignment](/erpnext/automating-issue-assignments-to-support-team-in-erpnext)
- [Email Error in Sending and Receiving](/erpnext/email-error)
- [Maximum User Limit Issue](/erpnext/how-to-fix-the-reached-maximum-user-limit-for-your-subscription-issue)
- [Perm Level Error](/erpnext/perm-level-error-in-permission-manager)
- [Permission Error Problems](/erpnext/report-permission-error)
- [Using Prepared Report](/erpnext/prepared-report)
- [Emails Are Not Received](/erpnext/what-if-emails-are-not-being-received-by-the-recipients)
- [Maximum Number of Fields in a Form](/erpnext/maximum-number-of-fields-in-a-form)
- [Making Custom Reports](/erpnext/making-custom-reports)
- [Deleting Custom Reports](/erpnext/deleting-custom-reports)
- [Reports Showing Multiple Lines for One Document](/erpnext/reports-showing-multiple-lines-for-one-document)
- [Add Columns in Standard Reports](/erpnext/how-to-add-columns-in-the-standard-report-and-export)
- [Fetch Child Table Values Using Jinja](/erpnext/fetch-child-table-values-using-jinja-tags)
- [Change Custom Field Datatype After Field Creation](/erpnext/change-custom-field-datatype-after-field-creation)
- [Company Wise Naming Series](/erpnext/company-wise-naming-series)
- [Feedback Request Using Web Form](/erpnext/feedback-request-using-web-form)
- [Manage Tree Structure of Masters](/erpnext/managing-tree-structure-masters)
- [Set Default Value for Any Field](/erpnext/setting-default-values-for-any-field-in-erpnext)
- [Set Precision](/erpnext/set-precision)
- [Set Language](/erpnext/set-language)
- [Edit Submitted Documents](/erpnext/edit-submitted-document)
- [Delete Submitted Documents](/erpnext/delete-submitted-document)
- [Set Current Value for Naming series](/erpnext/naming-series-current-value)
- [Easy Steps To Setup Workflow](/erpnext/easy-steps-to-setup-workflow)
- [Tree Master Renaming](/erpnext/tree-master-renaming)
- [Letter Head in Report](/erpnext/letter-head-in-the-report)
- [Sync Doctypes with Events Calendar](/erpnext/how-to-sync-doc-types-with-calendar)
- [User Permissions Based on Hierarchy](/erpnext/user-permission-based-on-hierarchy)
- [Add/Remove Fields from Print Format](/erpnext/add-remove-fields-from-print-format)
- [Customise Tables in Print Format](/erpnext/customise-your-items-tables-within-your-print-format-builder)
- [Customise Field Visibility in Print Format](/erpnext/making-fields-visible-in-print-format)
- [Remove Description in Print Format](/erpnext/removing-description-removed-item-code-and-name)
- [Print 'Centavo' in Words for USD](/erpnext/centavo-being-printed-in-words-for-usd)

### Accounting

- [Merging Accounts](/erpnext/merging-accounts)
- [Changing Parent Account](/erpnext/changing-parent-account)
- [Freeze an Account](/erpnext/freeze-account)
- [Freeze Accounting Entries](/erpnext/freeze-accounting-entries)
- [Common Receivable Account](/erpnext/common-receivable-account)
- [Sales Return Management](/erpnext/sales-return-use-cases)
- [Delivery From Sales Invoice](/erpnext/update-stock-option-in-sales-invoice)
- [Default Receivable / Payable Account](/erpnext/accounts/articles/default-receivable-payable-account)
- [Payment Entry for Capital Account](/erpnext/payment-entry-for-capital-account)
- [Book Petty Cash Entry](/erpnext/petty-cash-entry-in-erpnext)
- [Accounting for Bad Debts](/erpnext/accounting-for-bad-debts)
- [Purchase Invoice Account Type Error](/erpnext/purchase-invoice-account-type-error)
- [Book Discount Allowed and Received Separately](/erpnext/book-discount-allowed-and-received-separately)
- [Adding Reference To Journal Entry](/erpnext/adding-reference-to-journal-entry)
- [Invoice Discount in Payment Entry](/erpnext/adding-reference-to-journal-entry)
- [Withdrawing Salary from Owner's Equity Account](/erpnext/withdrawing-salary-from-owners-equity-account)
- [Buy 1 Get 1 Free Pricing Rule](/erpnext/setting-up-buy-1-get-1-free-pricing-rule)
- [Adjusting Without Amount](/erpnext/adjusting-withhold-amount)
- [Post Dated Cheque Entry](/erpnext/post-dated-cheque-entry)
- [Difference Entry](/erpnext/difference-entry-button)
- [Setting Up Taxes](/erpnext/setting-up-taxes)
- [Unreconciled](/erpnext/unreconciliation)
- [Period Closing Voucher](/erpnext/period-closing-voucher)
- [ERPNext QuickBooks Migrator](/erpnext/quickbooks-migrator)
- [Process Statement of Accounts](/erpnext/process-statement-of-accounts)
- [Payment Terms Status Report](/erpnext/payment_terms_status_report)
- [Inter Company Journal Entry](/erpnext/inter-company-journal-entry)
- [Advance in Separate Party Account](/erpnext/advance-in-separate-party-account)
- [Fiscal Year Error](/erpnext/fiscal-year-error)
- [Round Off Account Validation Message](/erpnext/round-off-account-validation)
- [Delete Entries Linked With GL Entries](/erpnext/delete-entries-linked-with-gl-entries)
- [Invoice Rounding Issue](/erpnext/invoice-rounding-issue)
- [Customise Cash Flow Report](/erpnext/customise-cash-flow-report)
- [Export Data for Specific Year or Filter](/erpnext/export-data-for-specific-year-or-filter)
- [Allocating Credit Note and Payment](/erpnext/allocating-credit-note-and-payment)
- [Reconcile Advance Payment to Supplier](/erpnext/reconcile-advance-payment-made-to-the-supplier)
- [Balance in Temporary Account](/erpnext/balance-in-temporary-account)
- [Calculate Freight Taxes](/erpnext/calculatin-freight-in-taxes-in-erpnext)
- [Purpose of Stock Received But Not Billed](/erpnext/stock-received-but-not-billed)
- [Closing Accounting Books](/erpnext/closing-accounting-books-in-erpnext)

### Buying

- [Purchase Invoice for Services](/erpnext/item-creation-not-required-in-purchase-invoice)
- [Debit Note for Price Adjustment](/erpnext/debit-note-for-price-adjustment)
- [Procurement Tracker Report](/erpnext/procurement-tracker-report)
- [Amending Purchase Order After Submit](/erpnext/amending-purchase-order-after-submit)

### Selling

- [Sales Person Target Allocation](/erpnext/sales-person-target-allocation)
- [Change The Rate Of Item in Sales Cycle](/erpnext/need-to-change-rate-of-items-during-sales-cycle)
- [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions)
- [Record Commission to Sales Partner](/erpnext/how-to-give-commission-to-sales-partner)
- [Short Close Multiple Orders](/erpnext/how-to-short-close-multiple-orders-in-erpnext)
- [Close Sales Order](/erpnext/close-sales-order)
- [Amending Sales Order After Submit](/erpnext/amending-sales-order-after-submit)
- [Applying A Discount](/erpnext/applying-discount)
- [Request for Raw Materials from Sales Order](/erpnext/request-for-raw-materials-from-sales-order)
- [Setting Company Sales Goal](/erpnext/setting-company-sales-goal)
- [Sales Invoice Without an Item](/erpnext/sales-invoice-without-an-item)
- [Drop Ship Between Subsidiary](/erpnext/assistance-sales-purchase-between-companies)
- [Loyalty Points Redemption in POS](/erpnext/loyalty-points-redemption-in-pos)
- [Selling in Different UOM](/erpnext/Selling-in-different-UOM)

### Assets

- [Moving Asset from Stock Item to Fixed Asset Item](/erpnext/moving-asset-from-stock-item-to-fixed-asset-item)

### CRM

- [Automate Lead Creation](/erpnext/automate_lead_capturing)
- [Difference Between Lead, Contact and Customer](/erpnext/difference_between_lead_contact_and_customer)

### Stock

- [Track Items Using Barcode](/erpnext/track-items-using-barcode)
- [Item Valuation Setup and Transactions](/erpnext/item-valuation-transactions)
- [Raw Material Valuation](/erpnext/valuation-based-on-field-in-bom)
- [Return Rejected Items](/erpnext/sales-return-use-cases)
- [Repack Entry](/erpnext/repack-entry)
- [Incoterm and Named Place](/erpnext/incoterm-and-named-place)
- [Quick Stock Balance](/erpnext/quick-stock-balance)
- [Quality Inspection Summary](/erpnext/quality-inspction-summary)
- [Migrate to Perpetual Inventory](/erpnext/migrate-to-perpetual-inventory)
- [FIFO and Moving Average](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average)
- [Perpetual Inventory for Non Stock Items](/erpnext/perpetual-inventory-for-non-stock-item)
- [Projected Quantity](/erpnext/projected-quantity)
- [Opening Stock Balance entry for Serialised and Batch Items](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
- [Linking Stock Warehouse and Accounts](/erpnext/warehouse-ledger-link)
- [Maintaining Supplier Item Code in Item Master](/erpnext/maintaining-suppliers-part-no-in-item)
- [Purchasing in Different UOM](/erpnext/purchasing-in-different-unit)
- [Production Scrap Management](/erpnext/scrap-management)
- [Customer Provided Items](/erpnext/customer-provided-items)
- [Multiple Finished Goods With Single Raw Material](/erpnext/how-to-handle-a-scenario-of-1-raw-material-multiple-finish-goods)
- [Manufacturing Without Creating BOM](/erpnext/manufacturing-without-creating-bom)
- [Material Consumption](/erpnext/material_consumption)
- [Production Analytics](/erpnext/production-analytics)
- [Open Work Order Report](/erpnext/open-work-orders)
- [Demand Driven Forecasting](/erpnext/demand-driven-forecasting)
- [Product Planning Report](/erpnext/production-planning-report)
- [Downtime Analysis](/erpnext/downtime-analysis)
- [Work Order Consumed Materials](/erpnext/work-order-consumed-materials)
- [Returned Material Against Work Order](/erpnext/returned_materials_against_work_order)
- [Issued Items Against Work Order](/erpnext/consumed-materials-in-production)
- [Material Transfer from Delivery Note and Purchase Receipt](/erpnext/material-transfer-from-delivery-note)
- [Allow Over Delivery / Billing](/erpnext/allow-over-delivery-billing-against-sales-order-upto-certain-limit)
- [Item Codification](/erpnext/item-codification)

### Project

- [Make a Colourful Gantt Chart](/erpnext/make-a-colorful-gantt-chart)
- [Bulk Assign Tasks in Projects](/erpnext/bulk-assign-tasks-in-a-project)
- [Project Profitability Report](/erpnext/project-profitability-report)
- [Project and Managing Expenses](/erpnext/project-expense-claims)
- [Project from Customer Portal](/erpnext/project-customer-portal)

### Website

- [Disable Signup in ERPNext Website](/erpnext/disable-signup)
- [Website Homepage](/erpnext/website-home-page)
- [Website Banner Resizing](/erpnext/website-banner)
- [SEO for ERPNext](/erpnext/how-to-setup-seo-for-your-website-on-erpnext)
- [301 Redirect in ERPNext](/erpnext/2-step-301-redirect-in-your-erpnext-website)

<!-- page: erpnext/erpnext__homepage.md -->
---
title: "Homepage\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/homepage"
updated: "2026-02-28"
---


**A homepage is the default landing page of your website.**

ERPNext's Website Module generates a default landing page for your website. You
can customize it in Homepage.

To access the Homepage page in ERPNext, go to:

> Home > Website > Portal > Homepage

## 1. How to setup Home Page
1. Select the Company.
1. Set the Title. This will be shown in the Browser Tab.
1. Configure the Hero Section as explained in the next section.

[Screenshot on the live page: Homepage]
*Homepage*

> Make sure your default 'Home Page' is set as `home` in Website Settings for
> this to work.

## 2. Hero Section

There are three ways in which you can customize the way the Hero Section looks:

1. Tag Line and Description (Default).
1. Homepage Slideshow.
1. Custom Hero Section.

### 2.1 Tag Line and Description

After you set your Tag Line, Description and Hero Image you'll have a decent
looking front page. You can also change the URL for the Explore button under **URL for "All Products"**.

[Screenshot on the live page: Website Homepage]
*Website Homepage*

### 2.2 Homepage Slideshow

Set the **Hero Section Based On** to **Slideshow** and the **Homepage Slideshow**
field will appear.

[Screenshot on the live page: Homepage Slideshow Setting]
*Homepage Slideshow Setting*

Now, select an existing Slideshow or create a new one shown as follows:

[Screenshot on the live page: Website Slideshow]
*Website Slideshow*

> For best results, make sure all of your slideshow images have same height and
> their width is greater than the height.

[Screenshot on the live page: Website Homepage with Slideshow]

### 2.3 Custom Hero Section

The third type of Hero Section allows you to write your own HTML.

Set **Hero Section Based On** to **Hero Section**.

Now create a new Hero Section. Set **Section Based On** as **Custom HTML**.
Write your custom HTML in the Section HTML field.

[Screenshot on the live page: Homepage Settings]
*Homepage Settings*

You can write any valid [Bootstrap 4](https://getbootstrap.com/) markup here.

[Screenshot on the live page: New Hero Section]
*New Hero Section*

It will look something like this:
[Screenshot on the live page: Homepage Hero Custom]
*Homepage Hero Custom*

## 3. Featured Products

You can also show featured products on your Homepage by adding them to the
Products table.

[Screenshot on the live page: Homepage Products Table]
*Homepage Products Table*

It will look something like this:
[Screenshot on the live page: Featured Products on Homepage]
*Featured Products on Homepage*

## 4. Homepage Section

You can add custom sections on your Homepage by creating new Homepage Sections.

> Go to Website > Portal > Homepage Section

A homepage section can consist of cards or Custom HTML. Set **Section Based On**
to **Cards**.

[Screenshot on the live page: New Homepage Section]
*New Homepage Section*

Add details for each card like Title, Subtitle, Image, Content and Route in the
Section Cards table.

It will look something like this:
[Screenshot on the live page: Homepage Section]
*Homepage Section*

You can also control the order in which these sections appear by setting the
**Section Order**. 0 will be shown first, followed by 1, and so on.

> To add Sections with Custom HTML refer [Custom Hero Section](#23-custom-hero-section).

## 5. Custom Homepage

ERPNext allows you to have a completely different homepage if you don't want to
use the default one described above.

To setup a custom homepage:

1. Create a [Web Page](/erpnext/web-page).
1. Go to Website > Setup > Website Settings.
1. Set Home Page as the `route` of your Web Page.
 [Screenshot on the live page]

<!-- page: erpnext/erpnext__how-is-valuation-rate-of-serialised-item-calculated-in-erpnext.md -->
---
title: "Serialised Item Valuation Rate calculation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-is-valuation-rate-of-serialised-item-calculated-in-erpnext"
updated: "2026-03-02"
---

In ERPNext, Item's stock **valuation rate** is updated on creation of the following transaction:  
1. Purchase Receipt
2. Stock Entry of type Material Receipt
3. Stock Reconciliation made for updating stock opening balance

  
ERPNext supports 2 valuation types: FIFO & Moving Average.   
You can select valuation method based on which item's value will be calculated. It can be set as per individual item as well as globally for all the items from Stock Settings.  
[Screenshot on the live page]  
  
Item valuation rates are calculated as per the valuation method set for them. However, in the case of **serialised Item**, these settings are *ignored*. The below Item, "Macbook Pro" is a serialised Item and it's valuation rate is not fetched from Item master. Instead, the valuation rate is updated from the *first incoming stock entry rate*, RS 199.80. Consequently, it is updated as per the other transactions carried out on this Item.  
Item Master:  
[Screenshot on the live page]  
[Screenshot on the live page]  
Stock Ledger:  
[Screenshot on the live page]  
To learn more about ERPNext Stocks module, click [here](https://erpnext.com/docs/user/manual/en/stock)

<!-- page: erpnext/erpnext__how-to-add-columns-in-the-standard-report-and-export.md -->
---
title: "Add columns in Standard Report and Export"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-add-columns-in-the-standard-report-and-export"
updated: "2026-03-04"
---

In **Standard Reports** of **ERPNext** such as *SOA, Accounts Receivable/Payable etc*, we provide an option to **Add/Remove Columns** from the documents and display it in the Report, these columns are only meant for reference at that particular moment of time.  
[Screenshot on the live page]  
If the User needs to *Export* along with the changes made by him in the Report, the User needs to Save the Report and then *Export* it.   
[Screenshot on the live page]  
  

<!-- page: erpnext/erpnext__how-to-add-master-link-and-fetch-data-from-the-same.md -->
---
title: "Fetching data from a linked master"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-add-master-link-and-fetch-data-from-the-same"
updated: "2026-03-04"
---

**Question:** How to add terms and conditions in driver form?  
**Steps:**  
1. Go to the doctype where you want the to add the terms and conditions.
2. Go to Menu > Customize

[Screenshot on the live page]  
1. You will see a table with a list of fields. These are the fields in your driver page.
2. Scroll down to the section/field after which you want to add terms and conditions.
3. Click on the small icon on the right side. This will expand the selected field.
4. You can add a new field above on below by clicking on *Insert Above/Below*.[Screenshot on the live page]
5. Add a new field as show below:[Screenshot on the live page]For more details on adding a custom link field, refer [this link](/erpnext/creating-custom-link-field).
6. Add a second field below this:[Screenshot on the live page]How does this work? In Fetch from, we are adding the following details: doctype.field. In the Terms and Conditions doctype, the field where we add the terms is named *terms* and it is of type: Text Editor. For *fetch from*to work, the data must be in the following format: link_field_name.field_to_fetch
7. Once this is done, click on **Update**, and go back to your list. Click on Ctrl + Shift + R to reload.
8. When you select the terms template in the driver, the system will fetch the conditions from the selected template:[Screenshot on the live page]

<!-- page: erpnext/erpnext__how-to-apply-tax-on-tax.md -->
---
title: "Apply Tax on Another Tax or Charge"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-apply-tax-on-tax"
updated: "2026-08-14"
---

Use **On Previous Row Total** when a tax or charge must be calculated on the running total after an earlier row. The base includes the item Net Total and every amount included up to the referenced row.



Consider Nova Industries, an electronics manufacturer and distributor. a transaction has a Net Total of $1,000. Row 1 adds an 8% tax of $80, bringing the running total to $1,080. Row 2 applies 2% to that $1,080:



`$1,080 × 2% = $21.60`



The Grand Total becomes $1,101.60.



This calculation is often described as tax on tax or a compound tax. Use it only when the applicable rule requires the later tax to include the earlier tax or charge in its base.

## Before you begin

Confirm the required calculation order with your accountant or tax adviser. A different row order can change the result even when the same rates are used.

You need:

- An Account Head for each tax or charge that must be posted separately.
- A [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template) or [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template), or a transaction where tax rows can be entered directly.
- The earlier tax or charge above the compound row.
- A small manual example with an expected result.

Review [Types in Tax Template](/erpnext/types-in-tax-template) if the calculation bases are unfamiliar.

## Understand the calculation

The example produces:


| Row | Type                  | Calculation base | Rate | Amount | Running Total |
| --- | --------------------- | ----------------: | ----: | ------: | -------------: |
| 1   | On Net Total          | $1,000.00        | 8%   | $80.00 | $1,080.00     |
| 2   | On Previous Row Total | $1,080.00        | 2%   | $21.60 | $1,101.60     |


The formula for row 2 is:

`Referenced row Total × Tax Rate ÷ 100`

The referenced row's **Total** is the cumulative transaction total after that row. It is not the $80 Amount produced by row 1.

## Configure the earlier tax or charge

Create or open the reusable tax template.

1. Add the tax or charge that must be included first.
2. Choose its calculation Type, such as **On Net Total**.
3. Select the correct Account Head.
4. Enter the Tax Rate and a clear Description.
5. Save the row.

In the worked example, row 1 applies 8% to the $1,000 Net Total and produces $80. The resulting row Total is $1,080.

## Add the compound-tax row

Add the later tax below the row it depends on.

1. Set **Type** to **On Previous Row Total**.
2. Set **Reference Row #** to the earlier row. Enter 1 for this example.
3. Select the Account Head for the compound tax.
4. Enter the Tax Rate, such as 2.
5. Confirm whether ERPNext should add or deduct the row.
6. Save the template.

Reference Row # refers to the numbered row in the tax table. It must point to an earlier row. Recheck it whenever rows are inserted, deleted, moved, or duplicated.

## Apply the template to a transaction

Select the template on a draft [Sales Invoice](/erpnext/sales-invoice), [Quotation](/erpnext/quotation), Sales Order, Purchase Invoice, or another supported transaction.

Use one item with a Net Total of $1,000 for the first test. ERPNext should show:

- Row 1 Amount: $80.00.
- Row 1 Total: $1,080.00.
- Row 2 Net Amount: $1,080.00.
- Row 2 Amount: $21.60.
- Total Taxes and Charges: $101.60.
- Grand Total: $1,101.60.



[Screenshot on the live page: A 2 percent compound tax calculated on the $1,080 running total]

The row 2 Net Amount is a useful verification point because it exposes the base used by the formula.

## Compare it with tax on another tax amount

**On Previous Row Total** and **On Previous Row Amount** are not interchangeable.


| Type for row 2         | Base from row 1  | 2% result | Grand Total |
| ---------------------- | ----------------: | ---------: | -----------: |
| On Previous Row Amount | Amount: $80.00   | $1.60     | $1,081.60   |
| On Previous Row Total  | Total: $1,080.00 | $21.60    | $1,101.60   |


Use [Tax on Another Tax Amount](/erpnext/tax-on-another-tax-amount) when the later levy applies only to the earlier $80 tax. Use Previous Row Total when it applies to the full $1,080 subtotal after that tax.

## Build a longer calculation sequence

A later row can reference the Total after any earlier row. For example:


| Row | Purpose                             |
| --- | ----------------------------------- |
| 1   | Base tax on Net Total               |
| 2   | Fixed charge added after the tax    |
| 3   | Percentage on the Total after row 2 |


If row 3 references row 2, its base includes the item value, row 1, and row 2. If it references row 1, it excludes row 2. This lets ERPNext model ordered calculations, but it also makes templates sensitive to row sequence.

Keep descriptions explicit. A description such as “2% on total after base tax” is easier to audit than a generic “Tax 2%”.

## Account for item-specific tax rates

When items have different rates, use an [Item Tax Template](/erpnext/item-tax-template) for the base row. ERPNext first determines the referenced row's actual Amount and Total, then calculates the later row from the configured reference.

Test taxable, exempt, and reduced-rate items together before reusing the template. Confirm that the compound row's legal base should include the mix of earlier item-wise amounts.

## Verify the submitted result

Before applying the template widely:

1. Calculate a small draft manually.
2. Compare each row's Net Amount, Amount, and Total.
3. Confirm Reference Row # and row order.
4. Review Grand Total.
5. Submit a controlled transaction.
6. Open the [General Ledger](/erpnext/general-ledger) and confirm each tax account and the party balance.

If a [Tax Rule](/erpnext/tax-rule) selects the template automatically, test every relevant party, item, and transaction combination. A correct template can still be unexpected when the wrong rule applies it.

## Troubleshooting

### The compound tax is too small

The row may be set to On Previous Row Amount, which uses only the earlier row's charge. Change it to On Previous Row Total only when the required base is the cumulative total.

### The compound tax includes an unwanted charge

Check Reference Row #. It may point to a later running total than intended. Reference the row whose Total contains exactly the components required by the rule.

### The result changed after editing the template

Row numbers can change after inserting, deleting, or moving rows. Reopen every previous-row calculation and verify its Type and Reference Row #.

### ERPNext rejects the reference row

The referenced row must come earlier. Reference Row # is supported only for On Previous Row Amount and On Previous Row Total.

## Frequently asked questions

### Does On Previous Row Total always mean tax on tax?

It means tax or charge on a running total. That running total can include item value, taxes, and other charges through the referenced row.

### Can I reference row 2 from row 4?

Yes, provided row 2 comes earlier. Row 4 then uses row 2's Amount or Total according to the selected Type.

### Should the compound tax use a separate ledger account?

Use the accounts required by your chart of accounts and reporting rules. Separate accounts generally make distinct liabilities easier to inspect.

### Does a discount change the compound-tax base?

It can, depending on where and how the discount is applied. Test the actual discount workflow and inspect the tax rows rather than assuming the pre-discount base remains unchanged.

### Can I use this calculation on purchase documents?

Y

es. On purchase rows, also decide whether each calculated amount affects the supplier Total, stock Valuation, or both. See [Include Tax or Charge in Valuation or Total?](/erpnext/include-tax-or-charge-in-valuation-or-total).

## Related topics

- [Tax on Another Tax Amount](/erpnext/tax-on-another-tax-amount)
- [Types in Tax Template](/erpnext/types-in-tax-template)
- [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Item Tax Template](/erpnext/item-tax-template)
- [Tax Rule](/erpnext/tax-rule)

<!-- page: erpnext/erpnext__how-to-create-a-supplier-quotation-through-the-supplier-portal.md -->
---
title: "Create Supplier Quotation through Supplier Portal"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-create-a-supplier-quotation-through-the-supplier-portal"
updated: "2026-02-26"
---

In ERPNext, Supplier Quotations can either be created manually or via the Supplier Portal. Suppliers can create Quotations via the Supplier Portal once they have logged into the system. 

Pre-requisites:

* The Supplier must be a registered Website User with "Supplier" role.
* Supplier user account's Contact must be linked to the Supplier document.

[Screenshot on the live page]

[Screenshot on the live page]  


For a Supplier to create a Quotation, there should be an existing Request for Quotation (RFQ) against them. To do this entire process, follow the following steps:

  


1) Create a Request for Quotation for the Supplier in the system. For example, we are creating an RFQ for "MNO Suppliers".

  


[Screenshot on the live page]

  


2) Now, the Supplier (MNO Suppliers in our case) has to log into the Supplier Portal using their login credentials. There, the Supplier will be able to view the RFQ

  


[Screenshot on the live page]

The Supplier has to enter the Item Rate and submit the RFQ.

  


[Screenshot on the live page]

  


  


[Screenshot on the live page]

  


Once the RFQ is submitted, a Supplier Quotation gets automatically created in the system against this RFQ. Click on the "View" option.

  


[Screenshot on the live page]

  


Observe that the Supplier Quotation is in the Draft state. After reviewing the Supplier Quotation, the user can submit it. This will also be reflected in the Supplier Portal.

  


[Screenshot on the live page]

  


[Screenshot on the live page]

  

<!-- page: erpnext/erpnext__how-to-create-and-print-proforma-invoice-in-erpnext.md -->
---
title: "How to create and print proforma invoice in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-create-and-print-proforma-invoice-in-erpnext"
updated: "2026-07-02"
---

ERPNext does not have a dedicated "Proforma Invoice" document. To print one, you can simulate it by opening a **Quotation** or **Sales Order**, changing the document's Print Heading to "Proforma Invoice", and printing the document.

Follow these exact steps to print a proforma invoice for a customer:

**1. Create and Open the Document**

- Navigate to the Quotation or Sales Order you wish to send.
- Open the specific document record you want to print.

**2. Update the Print Heading**

- Scroll down to the Printing Settings section in the Quotation or Sales Order.
- In the Print Heading field, click the dropdown and select Create a new Print Heading.
- Type Proforma Invoice as the new heading name and save.
- Select this newly created Proforma Invoice heading from the dropdown and save your document.

**3. Print or Save as PDF**

- Click the Menu button (three dots) or the Print icon at the top left of the screen.
- Ensure you have the proper Letterhead selected if you need your company logo and contact details.
- Click PDF to download it to your computer, or click Print to send it directly to your hardware.

---

**Additional Customization Resources**

- **[ERPNext Print Designer Tutorial (Video Guide)](https://www.youtube.com/watch?v=-wH9jAUP4CE)**
- **[Frappe Customize Print Format Guide (Official Documentation)](https://docs.frappe.io/erpnext/records-print-format)**

<!-- page: erpnext/erpnext__how-to-disable-users-in-the-erpnext-system.md -->
---
title: "Disable Any User"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-disable-users-in-the-erpnext-system"
updated: "2026-02-26"
---

If you want to prohibit an ERPNext user from using the system then you can follow the below steps. This will be useful when your employees resign or in case you want to ban certain users from accessing the system.

**How to disable a user?**
--------------------------

1. Type ‘User List’ in the awesome bar
2. Select the user you want to disable
3. Uncheck the ‘Enabled’ checkbox for the selected user
4. Save your changes

Once the changes are saved, the user will be marked as 'Disabled' in the list which can always be re-enabled as per the need. After re-enabling a user, all the configurations associated with it will be retrieved as is.

[Screenshot on the live page: Screenshot 2023-12-27 at 3.51.59 PM]  

<!-- page: erpnext/erpnext__how-to-fix-the-reached-maximum-user-limit-for-your-subscription-issue.md -->
---
title: "Maximum User Limit Issue"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/how-to-fix-the-reached-maximum-user-limit-for-your-subscription-issue"
updated: "2026-03-04"
---

Your ERPNext subscription depends on the number of System Users you subscribe for. Once you cross that limit, the system will not let you create any further number of users. For example, you have subscribed for 10 users. If you already have already created 10 System Users in your account, the system wont let you create the 11th System User, and you will get the below message.

  


[Screenshot on the live page]

  


To fix this, you will either have to:

1) Buy new users or

2) Disable the current users

  


However, sometimes, you may still face this issue even when you have not exhausted the number of System Users as per your subscription plan. For example, you have a limit of 5 System Users and you have only created 3 users. Yet while creating the 4th user, you get the above message. The reason for this can be that for some of the uses, the field of "Simultaneous Sessions" is greater than 1.

  


Every simultaneous session is considered as 1 System User. For example, if you have created 3 users and one of them has "Simultaneous Session" set to 3, then you have a total of 5 users, i.e. 3 + 1 + 1 = 5 simultaneous sessions/system users.

  


To allow the system to let you create more users, you will have to reduce the simultaneous sessions of these users. To do so, go to the User's profile, under Security Settings, set/reduce the "Simultaneous Session" accordingly.

  


[Screenshot on the live page]

  


**Note:** You will still be able to create Website Users as there is no limit for the same.
