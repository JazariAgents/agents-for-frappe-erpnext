<!-- Frappe documentation: erpnext, part 57 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__set-precision.md -->
---
title: "Set Precision | ERPNext Documentation"
description: "Configure ERPNext float and currency precision globally or for a specific field, with examples showing the effect on transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set-precision"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. It buys 1,250 metres of cable at USD 1.2375 per metre. If the purchase rate is displayed with only two decimal places, employees see USD 1.24 and may assume the amount was entered incorrectly. If the company increases precision everywhere without a reason, reports become harder to read and users may mistake display detail for accounting accuracy.



Precision controls how many decimal places ERPNext calculates or displays for Float, Currency, and Percent values. Nova uses a sensible site-wide precision for most records and applies a field-specific override only when a real measurement or pricing process needs more detail. Precision is related to rounding, but it is not the same decision as the rounding method.

## Set site-wide precision

Open **System Settings** and review **Float Precision** and **Currency Precision**. Float Precision affects values such as quantity or conversion factor. Currency Precision affects monetary values such as rate and amount.

[Screenshot on the live page: Float and Currency Precision in ERPNext System Settings]


| Setting                | Example                      | Result                                                                                                |
| ---------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| Float Precision = 3    | Quantity 1.275               | ERPNext displays three decimal places where the field follows the global precision.                   |
| Currency Precision = 2 | USD 699.50                   | Common cent-based amounts display two decimal places.                                                 |
| Currency Precision = 4 | Rate USD 1.2375              | Useful when Nova buys a high-volume component priced below one cent increments.                       |
| Rounding Method        | Midpoint value such as 2.345 | Determines how a value is rounded when precision is applied. Review it separately in System Settings. |


## Override one field with Customize Form

Use **Customize Form** only when one field genuinely needs different precision. Select the DocType and field, set its Precision property, save, and reload. For example, Nova can show four decimal places on an Item rate while keeping ordinary financial totals at two decimals.

## Verify the result downstream

Create a draft Purchase Invoice or Purchase Order with quantity 1,250 and rate 1.2375. Confirm the entered rate, calculated amount, taxes, rounded total, print format, and General Ledger result follow the intended policy. Display precision alone is not proof that the stored and posted value is correct.

## Troubleshooting

### A field still shows fewer decimals

The field may have its own Precision property or be formatted by a Currency. Reload metadata and inspect the field through Customize Form.

### The total differs from a manual calculation

Compare quantity, conversion factor, rate, tax precision, smallest currency fraction, rounded total, and rounding method. Do not fix a policy mismatch by adding arbitrary decimals.

### Reports and forms display different precision

Reports may apply their own column precision or Currency formatting. Verify the report definition and linked Currency.

## Frequently asked questions

### Does higher precision make accounting more accurate?

More displayed decimals help only when the source measurement or price is genuinely that precise. False precision can make reports harder to interpret.

### Can quantity and currency use different precision?

Float Precision and Currency Precision are separate controls, and individual fields can have overrides.

### Does changing precision rewrite old transactions?

It can change how values are displayed, but it should not be assumed to recompute or correct submitted accounting entries. Test reports and documents before rollout.

### When should a field-specific override be used?

Use it when one operational value, such as a commodity rate or measurement, requires more detail than the rest of the site.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Customize Form](/erpnext/customize-form)
- [Currency](/erpnext/currency)
- [Global Defaults](/erpnext/global-defaults)
- [Invoice Rounding Issue](/erpnext/invoice-rounding-issue)
- [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__set_up_e_commerce.md -->
---
title: "Set Up E-commerce"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set_up_e_commerce"
updated: "2026-03-02"
---

**If you're using version 15 or migrating to version 15, you need to install the frappe's** [**Webshop**](https://github.com/frappe/webshop) **app first in order to use the E-commerce features**

In addition to tracking Items, ERPNext also has the provision to set up an attractive E-commerce shop to sell them. You can seamlessly publish items onto your web store and configure what to show in clicks. You can also choose to enable/disable features such as Wishlist, Customer Reviews, etc.

Assuming you have some [Items](/erpnext/item) setup in ERPNext, you can follow the steps below to set up your store:

1. [Explore and Configure E Commerce Settings (In v15 E Commerce Settings has renamed to Webshop Settings)](/erpnext/e_commerce_settings)
2. [Publish and Update an Item](/erpnext/website_item)
3. [Explore the Product Listing](/erpnext/product-listing)
4. [Explore Item group wise product listing](/erpnext/item_group_wise_product_listing)
5. [Shopping Cart](/erpnext/shopping-cart)
6. [The Shop by Category page](/erpnext/shop_by_category)
7. [Wishlist](/erpnext/wishlist)
8. [Reviews and Ratings](/erpnext/reviews_and_rating)
9. [Search](/erpnext/e_commerce_search)

<!-- page: erpnext/erpnext__setting-company-sales-goal.md -->
---
title: "Calculate Incentive for Sales Team | ERPNext Documentation"
description: "Calculate Sales Person contribution and incentives in ERPNext using commission rates and the Sales Team table on sales transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-company-sales-goal"
updated: "2026-07-24"
---


**Defining and achieving sales goals/targets can help your company reach new goals and increase revenue.**

1. Monthly sales targets can be set for a Company via the Company master under the Sales Settings section. By default, the Company master dashboard displays month-wise past sales stats.

 [Screenshot on the live page: Sales Graph]

1. You can set the **Sales Target** field to track progress against the graph:

 [Screenshot on the live page: Setting Sales Goal]

1. The target progress is also shown in notifications:

 [Screenshot on the live page: Sales Notification]

### Related Topics
1. [Company Setup](/erpnext/company-setup)
1. [Sales Order](/erpnext/sales-order)
1. [Sales Partner](/erpnext/sales-partner)

<!-- page: erpnext/erpnext__setting-default-values-for-any-field-in-erpnext.md -->
---
title: "Set default values for any field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-default-values-for-any-field-in-erpnext"
updated: "2026-03-04"
---

 

Using **Customize Form**, we can set a _default_ value for any field of any Doctype in ERPNext.

 

**Steps:**

1\. Open Customize Form using awesome search bar or via Menu options of any DocType. This will open a screen where you can view all the fields that comprise in this DocType.

 

[Screenshot on the live page]

 

 

2\. Expand the field for which you want to store a default value and enter it under Display -> Default

 

[Screenshot on the live page]

 

[Screenshot on the live page]

 

 

Check out the below GIF where we have set _default_ value as **Stores - ETL** for field "Default Source Warehouse" in DocType Stock Entry:

 

[Screenshot on the live page]

 

 

To learn more about customisations in ERPNext, check out this [link](https://erpnext.com/docs/user/manual/en/customize-erpnext/customize-form)

<!-- page: erpnext/erpnext__setting-up-buy-1-get-1-free-pricing-rule.md -->
---
title: "Set Up Buy One Get One Free Offers | ERPNext Documentation"
description: "Create and test an ERPNext Product Discount Pricing Rule for buy-one-get-one-free and other free-item promotions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-buy-1-get-1-free-pricing-rule"
updated: "2026-07-25"
---

Use a Product Discount [Pricing Rule](/erpnext/pricing-rule) to add a free item when a transaction meets a purchase condition. The free item can be the same Item or a different promotional Item.

## Before you begin

Create or confirm:

- The qualifying and free [Items](/erpnext/item).
- Selling [Item Prices](/erpnext/item-price).
- Sufficient stock for the free Item when it maintains stock.
- The eligible Customer, Customer Group, Territory, or campaign when the offer is restricted.

Test the rule on a demo transaction before enabling it for users. Product Discount rules can re-add a free row when users remove it while the qualifying condition still applies.

## Create a Buy 1 Get 1 Free rule

1. Open the Pricing Rule list and select **Add Pricing Rule**.
2. Enter a clear title, such as **Buy AeroBook Sleeve, Get One Free**.
3. Set **Apply On** to Item Code and add the qualifying Item.
4. Set **Price or Product Discount** to **Product Discount**.
5. Set the minimum quantity to 1.
6. In the Product Discount section:
  - Enable **Same Item** when the purchased Item is also free.
  - Otherwise select the free Item.
  - Set Free Qty to 1.
7. Configure the Selling or Buying applicability, party conditions, dates, and priority.
8. Save and enable the rule.

[Screenshot on the live page: A Product Discount Pricing Rule configured for Buy 1 Get 1 Free.]

## Test the offer

1. Create a new [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).
2. Select an eligible Customer and add the qualifying Item.
3. Enter the minimum qualifying quantity.
4. Save or select **Apply Pricing Rule** when required by the form.
5. Confirm that ERPNext adds the free row with a zero rate.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

Use the highlighted pencil icon to open the full child-row editor when you need to verify fields that are not shown in the grid.

## Same-item and different-item offers


| Offer                               | Configuration                                                      |
| ----------------------------------- | ------------------------------------------------------------------ |
| Buy one, get the same Item free     | Enable Same Item and set Free Qty                                  |
| Buy one Item, get another Item free | Leave Same Item disabled and select the free Item                  |
| Buy several units, get one free     | Set the qualifying minimum quantity and Free Qty                   |
| Apply the offer to an Item Group    | Apply the condition to the Item Group and test every eligible Item |


## Stock and fulfilment

A zero-rate promotional Item can still require stock. Verify availability before launching the offer and include the free row in downstream [Delivery Notes](/erpnext/delivery-note) and stock updates.

If insufficient stock prevents submission, replenish or change the offer. Do not delete the free row and assume the Pricing Rule is satisfied, because ERPNext can fetch it again.

## Rule priority and overlap

Review other Pricing Rules, [Promotional Schemes](/erpnext/promotional-scheme), and [Coupon Codes](/erpnext/coupon-code) that could match the transaction. Use clear validity periods and priorities, then test whether offers should combine or remain exclusive.

## Troubleshooting


| Problem                               | What to check                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| The free row is not added             | Confirm the rule is enabled and all item, party, quantity, date, and transaction conditions match |
| The free row returns after deletion   | The qualifying condition still applies; change the transaction or disable the rule                |
| Submission reports insufficient stock | Check stock for the free Item and selected Warehouse                                              |
| More than one promotion applies       | Review overlapping rules and priorities                                                           |
| The wrong Item is free                | Review Same Item and the selected free Item                                                       |


## Frequently asked questions

### Can the free Item differ from the purchased Item?

Yes. Leave Same Item disabled and select the promotional Item.

### Can I set Buy 2 Get 1 Free?

Yes. Set the minimum qualifying quantity to 2 and Free Qty to 1.

### Does the free Item appear on delivery documents?

Yes, when the mapped document includes the promotional row.

### Can the free Item have a non-zero rate?

A Product Discount free row is intended to carry a zero promotional rate. Use a Price Discount rule for a reduced, non-zero rate.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Applying a Discount](/erpnext/applying-discount)
- [Sales Order](/erpnext/sales-order)
- [Delivery Note](/erpnext/delivery-note)

<!-- page: erpnext/erpnext__setting-up-email-signature-in-erpnext.md -->
---
title: "Setting Up Email Signature in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-email-signature-in-erpnext"
updated: "2026-03-04"
---

To add your signature, go to your User Profile under **Settings > My Settings**  

[Screenshot on the live page]

Scroll down to the **Email Settings** section where you can add your signature in HTML:  

[Screenshot on the live page]

<!-- page: erpnext/erpnext__setting-up-sendgrid-smtp-email-in-erpnext.md -->
---
title: "Setting up Sendgrid SMTP Email in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-sendgrid-smtp-email-in-erpnext"
updated: "2026-03-06"
---

SMTP, or simple mail transfer protocol, is a quick and easy way to send email from one server to another. SendGrid provides an SMTP service that allows you to deliver your email via our server instead of your client or server. ERPNext comes built-in with a configured email client so that you can send and receive emails in ERPNext and append them to documents if required.

**Integrating SendGrid's Web API**

SendGrid’s SMTP API allows developers to specify custom handling instructions for e-mail using an X-SMTPAPI header inserted into the message.

**Step 1:** You need to create an API key to authenticate your application. In this case, *ERPNext*. Learn more about integrating SendGrid with SMTP [here](https://sendgrid.com/docs/API_Reference/SMTP_API/integrating_with_the_smtp_api.html)

Click on SMTP Relay[Screenshot on the live page: Screenshot 2024-06-01 at 12.44.17 PM]  


Generate an API Key[Screenshot on the live page: Screenshot 2024-06-01 at 12.44.33 PM]  
  
**Step 2:** Once your *API key* has been created, you need to configure it in your ERPNext account &gt; Create a **New** **Email Account.**

  


**Email Address:** *Your Email Address*

**Service:** Select "*SendGrid*"

Check "Use Different Email ID"

**Alternative email ID:** apikey

**Password:** *&lt;API Key Generated in step 1&gt;*

Outgoing server: &lt;server name generated in step 1&gt;

Port: &lt;port number generated above&gt;

[Screenshot on the live page: Screenshot 2024-06-01 at 12.44.45 PM]  


For SSL connections, uncheck the "use TLS" option[Screenshot on the live page: Screenshot 2024-06-01 at 12.45.14 PM]  


Now **save** this information and you have successfully configured the SendGrid SMTP Email in ERPNext.

  
  


Power to you!

  
  


  
  


-----

**﻿**

<!-- page: erpnext/erpnext__setting-up-taxes.md -->
---
title: "Setting Up Taxes | ERPNext Documentation"
description: "Configure tax accounts, sales and purchase tax templates, Tax Categories, Tax Rules, and item-specific rates in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up-taxes"
updated: "2026-08-14"
---

Tax setup connects a legal calculation to the ordinary sales and purchase workflow. The goal is not merely to add a percentage to an invoice, but to calculate the right charge, post it to the right account, and retain enough detail for reporting and compliance.



Nova Industries may sell the same electronics to retail customers, resellers, and customers in another region. The applicable tax can depend on the Item, party, address, transaction type, and jurisdiction. Reusable templates and rules allow ERPNext to choose consistently instead of asking users to rebuild the calculation on every invoice.



This page provides the setup sequence and explains how accounts, templates, Item Tax Templates, Tax Categories, and Tax Rules work together. Confirm the exact rates and legal treatment with a qualified local adviser.

## Before you begin

Confirm the tax registration, rates, place-of-supply rules, recoverability, and reporting requirements with a qualified adviser. Create the required tax ledgers in the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).

## Create sales and purchase tax templates

Open **Sales Taxes and Charges Template** or **Purchase Taxes and Charges Template**.

1. Select the company.
2. Add a row for each tax or charge.
3. Choose the calculation type.
4. Select the tax ledger.
5. Enter the rate and description.
6. Mark a template as default only when it applies to most transactions.
7. Save.

[Screenshot on the live page: Sales tax template]

Review whether purchase tax should be added to valuation, treated as recoverable input tax, or posted as an expense.

## Use Tax Categories

A Tax Category identifies a tax treatment, such as domestic standard, export, or exempt.

[Screenshot on the live page: Tax Category]

Assign the category to parties or transactions. Then use a [Tax Rule](https://docs.frappe.io/erpnext/tax-rule) to choose the correct template based on company, Customer, Supplier, item, territory, billing or shipping location, and validity dates.

## Configure item-specific tax rates

Use an [Item Tax Template](https://docs.frappe.io/erpnext/item-tax-template) when particular Items have a different rate or exemption. Link the template on the Item or transaction row.

## Test the configuration

Create representative draft Sales Invoices and Purchase Invoices for each tax treatment. Check the taxable value, each tax row, grand total, General Ledger preview, and printed tax information. Include discounts, returns, and foreign-currency cases in testing when they apply.

## Withholding and localization

Withholding tax uses separate [Tax Withholding Category](https://docs.frappe.io/erpnext/tax-withholding-category) configuration. Country-specific apps may add tax identifiers, reports, e-invoicing, and statutory validations. Follow the localization documentation when it overrides generic setup.

## Troubleshooting

**The wrong tax template is selected**

Check the Tax Category, Tax Rule priority and validity, party and address data, company, and transaction date.

**Tax is missing for one Item**

Review its Item Tax Template and the tax account mapping in the transaction template.

**Tax is calculated on the wrong value**

Check the row calculation type and whether the charge is based on Net Total, Previous Row Total, Previous Row Amount, or Actual.

## Related topics

- [Tax Rule](https://docs.frappe.io/erpnext/tax-rule)
- [Item Tax Template](https://docs.frappe.io/erpnext/item-tax-template)
- [Sales Taxes and Charges Template](https://docs.frappe.io/erpnext/sales-taxes-and-charges-template)
- [Tax Withholding Category](https://docs.frappe.io/erpnext/tax-withholding-category)

<!-- page: erpnext/erpnext__setting-up.md -->
---
title: "Setting Up\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-up"
updated: "2026-08-14"
---

Setting up ERPNext means turning the way your business already works into reliable masters, defaults, permissions, and opening balances. A good setup begins with the decisions that affect every transaction, then moves into the individual modules your team will use.



For Nova Industries, an electronics manufacturer and distributor, this starts with the legal company, fiscal year, chart of accounts, warehouses, items, customers, suppliers, users, and opening balances. Configure these foundations before importing day-to-day transactions.

[Screenshot on the live page: ERPNext Desk showing the installed applications available after sign-in]



## Plan the setup


| Decision          | Why it matters                                                           | Start here                                      |
| ----------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| Legal entities    | Separates books, tax registrations, currencies, and statutory reporting. | [Company](/erpnext/company-setup)               |
| Accounting period | Controls transaction dates and financial reporting.                      | [Fiscal Year](/erpnext/fiscal-year)             |
| Accounts          | Determines where every financial transaction is posted.                  | [Chart of Accounts](/erpnext/chart-of-accounts) |
| Stock locations   | Defines where inventory is stored and valued.                            | [Warehouse](/erpnext/warehouse)                 |
| Access            | Limits what each user can view and change.                               | [Users and Permissions](/erpnext/adding-users)  |


## Recommended setup order

1. Create or review the [Company](/erpnext/company-setup), Country, currency, time zone, language, and fiscal year.
2. Review [System Settings](/erpnext/system-settings), [Global Defaults](/erpnext/global-defaults), and Domain Settings.
3. Configure the [Chart of Accounts](/erpnext/chart-of-accounts), cost centers, taxes, bank accounts, warehouses, and naming rules.
4. Create essential masters such as [Items](/erpnext/item), [Customers](/erpnext/customer), and [Suppliers](/erpnext/supplier).
5. Add users, roles, and user permissions. Test the setup with the same access your team will use.
6. Prepare clean legacy data and use the [Data Import](/erpnext/data-import) tools for required masters and opening balances.
7. Run a complete sales, purchase, stock, and accounting cycle before going live.

## Do not import everything

Move only the data needed to operate and report from the cutover date. Keep the old system available for historical reporting instead of importing years of low-value transactions. This reduces reconciliation effort and makes problems easier to find.

## Validate before go-live

Confirm opening receivables, payables, bank balances, stock quantities, stock values, fixed assets, taxes, and the trial balance. Ask real users to complete their most common tasks. Correct the setup before the first live transaction, because changing currencies, account structures, or stock rules later can be disruptive.

## Troubleshooting

### A module is missing

Review Domain Settings and Show or Hide Modules. Also confirm that the user has the roles required to access the workspace.

### Defaults are not appearing

Check Company defaults, Global Defaults, user defaults, and the relevant module settings. Reload the session after changing system-wide defaults.

## Frequently asked questions

### Should I set up every module before going live?

Configure the modules needed for the first operational scope, test them thoroughly, and introduce additional modules in controlled phases.

### Can I change the setup later?

Many defaults can be changed, but decisions such as company currency, account structure, stock accounting, and opening balances require careful planning after transactions exist.

## Related topics

- [Company](/erpnext/company-setup)
- [System Settings](/erpnext/system-settings)
- [Data Import](/erpnext/data-import)
- [Adding Users](/erpnext/adding-users)
- [Opening Balances](/erpnext/opening-balance)

<!-- page: erpnext/erpnext__setting-workflows-on-masters.md -->
---
title: "Setting Workflows on Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setting-workflows-on-masters"
updated: "2026-03-04"
---

Workflows are usually set on submittable documents. Once the document is approved, it gets automatically submitted as per the workflow set. However, sometimes, businesses do have use cases where there is a need for approval of masters such as Items, Item Price, Pricing Rule, etc.

  


In ERPNext, these masters are non-submittable. Hence, even on rejection, sometimes, they are still active and you can use them in transactions. In this article, we have taken the example of the Item master. We will set a simple workflow on Item and make it active only when it has been approved. To do so, follow the below steps:

  


1) Make sure the master on which you are going to set the workflow has an Enable/Disable checkbox. If this is not present by default, you need to create one via Customize Form and set the default value as follows:

1. 0 if checkbox is "Disable"
2. 1 if checkbox is "Enable"

In our case, the Item master has a checkbox called "Disabled". We have set the default value as 1 in the Customize Form of the Item DocType as shown below.

  


[Screenshot on the live page]

  


This means that every time a new Item is created, it will be disabled by default, unless approved (as seen in the screenshot below). 

  


[Screenshot on the live page]

  


  


2) Next, set the Workflow.

  


In the States table, on approval, make sure to update the "Disabled" (or Enabled) checkbox to 0 (or 1 in case of enabled) as shown below.

  


  


[Screenshot on the live page]

  


This will ensure that whenever the Item is approved, the Item will automatically be enabled and you will be able to use it in transactions.

  


Check the below GIF to understand the workflow in detail:

  


[Screenshot on the live page]

<!-- page: erpnext/erpnext__setup-two-factor-authentication.md -->
---
title: "Setup Two Factor Authentication\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/setup-two-factor-authentication"
updated: "2026-03-04"
---


##Enable Two Factor Authentication (2FA)

Activate two factor authentication by running the command.

`bench --site [sitename] set-config enable_two_factor_auth true`

Specify the following in System Settings

* The method of OTP validation (OTP App = TOTP using Soft or Hard Token while Email/SMS = HOTP using Email or SMS
* The expiry time for the QR Code on the server if OTP App is specified
* The OTP Issuer Name.

[Screenshot on the live page: Enable Two Factor Auth]


On activation of 2FA from setup, it is also activated for the Role "All". In this way, all users including the Administrator have to perform a 2nd level authentication with a token. By unchecking the "Two Factor Authentication" checkbox in the "All" role and enabling it in other roles, the need to login with a token can be limited to specific roles. 2FA does not apply to login by Web Users and API login

[Screenshot on the live page: Role Enable Two Factor Auth]

If using SMS authentication, please make sure that your SMS settings are updated

[Screenshot on the live page: SMS Settings]

If using Email, make sure that your outgoing Email account settings are updated

[Screenshot on the live page: Email Settings]

When the new user tries to log in for the first time in a system that has two-factor authentication enabled and which has the authentication option as OTP App, an email is sent containing a link to the QR Code.

[Screenshot on the live page: Email Notify Two Factor]
[Screenshot on the live page: QR Code Page]

Scanning the QR Code with an authentication app like Google Authenticator registers the access for the user and automatically starts to generate tokens that can be used to login

[Screenshot on the live page: Two Factor Scan App]

If either of Email/SMS is used as the authentication method, you get notifications also

[Screenshot on the live page: Email and SMS]



### Frequently asked questions (FAQ)

Q. I am unable to login even after following entire process. 

Ans: Frappe uses TOTP based OTP algorithm, which depends on your device's system time. Please make sure that device you're using has same time set as your ERPNext server. 

<!-- page: erpnext/erpnext__share-reports.md -->
---
title: "Share Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/share-reports"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Elena then transfers 1,000 shares to Horizon. The new balances should be 5,000 for Elena, 4,000 for Marcus, and 2,000 for Horizon. Management wants to verify two things. It needs the ownership position today and the transaction trail that explains how that position changed.



ERPNext separates these questions into two reports. Share Balance is the current snapshot. Share Ledger is the history behind the snapshot. Use both when reviewing ownership, investigating a disagreement, or preparing information for professional review.

## Share Balance

Open **Share Balance** and filter by Company or Shareholder. The report shows the shares currently held by each shareholder and their value. Use it to answer “Who owns what now?”

[Screenshot on the live page: Current Nova shareholders used in share reporting]

## Share Ledger

Open **Share Ledger** and filter by Company, date range, or Shareholder. The report lists submitted [Share Transfers](/erpnext/share-transfer) such as issues, purchases, and owner-to-owner transfers. Use it to answer “How did this balance arise?”

[Screenshot on the live page: Submitted share transfer quantity used in the Share Ledger]

## Choose the right report


| Question                                     | Report                                                        |
| -------------------------------------------- | ------------------------------------------------------------- |
| How many shares does each owner hold now?    | Share Balance                                                 |
| Which issue or transfer changed the holding? | Share Ledger                                                  |
| What is one owner's current position?        | Share Balance filtered by [Shareholder](/erpnext/shareholder) |
| What happened during a particular period?    | Share Ledger filtered by date                                 |


## Troubleshooting

### A recently created shareholder does not appear

A shareholder with no submitted share issue has no holding to report. Submit an Issue and refresh the report.

### A transfer is missing

Confirm that the Share Transfer is submitted, the Company and date filters include it, and the correct shareholder is selected.

## Frequently asked questions

### Can Share Balance replace the Share Ledger?

Share Balance shows the result but not the sequence of transactions. Keep the Share Ledger when you need an audit trail.

### Do these reports replace statutory shareholder registers?

ERPNext provides operational ownership records. Confirm the statutory format, approvals, and filing requirements with a qualified professional in your jurisdiction.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Shareholder Management](/erpnext/shareholder-management)
- [Share Transfer](/erpnext/share-transfer)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__share-transfer.md -->
---
title: "Share Transfer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/share-transfer"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Elena now wants to transfer 1,000 of her shares to Horizon Ventures LLC. After the transfer, Elena will hold 5,000 shares, Marcus will still hold 4,000, and Horizon will hold 2,000. The company needs more than a note saying the deal happened. It needs an auditable record of the former owner, new owner, share-number range, quantity, rate, and date.



A Share Transfer records three kinds of ownership movement: the Company issues new shares, buys shares back, or transfers existing shares between Shareholders. Use the correct type because it determines which parties ERPNext requires and how balances change.

## Before you begin

Create the relevant [Shareholders](/erpnext/shareholder). A new owner must first receive an Issue before their folio number and balance become available for later transfers. Confirm the equity or liability [Account](/erpnext/chart-of-accounts), asset account, and Share Type with your accountant.

## Issue shares

Create a Share Transfer and set **Transfer Type** to **Issue**. Select the recipient, Equity or Preference share type, and the Company.

[Screenshot on the live page: Share issue type, recipient, and share type highlighted]

Enter the first and last share numbers, number of shares, and rate. The number range must agree with the quantity and must not overlap an existing issued range.

[Screenshot on the live page: Share number range, quantity, and rate highlighted]

## Transfer shares between owners

Set Transfer Type to **Transfer**. Select the From Shareholder and To Shareholder with their folio numbers.

[Screenshot on the live page: From and to shareholders highlighted]

Enter the share-number range being moved, quantity, and rate, then save and submit. ERPNext reduces the former owner's holding and increases the new owner's holding.

[Screenshot on the live page: Transferred share range and quantity highlighted]

## Transfer types


| Type     | Use it when                                              |
| -------- | -------------------------------------------------------- |
| Issue    | The Company creates and assigns shares to a shareholder. |
| Transfer | Existing shares move from one shareholder to another.    |
| Purchase | The Company buys shares back from a shareholder.         |


## Troubleshooting

### The folio number is missing

Submit an Issue for that shareholder first. A saved Shareholder without an issued holding does not yet have an ownership history.

### The share-number range is rejected

Check that the From No, To No, and No of Shares agree and that the range is available to the source owner.

## Frequently asked questions

### Does submission automatically create General Ledger entries?

The ownership register changes on submission. Use **Create Journal Entry** when the transfer also requires an accounting entry, and review the resulting [General Ledger](/erpnext/general-ledger).

### Can I transfer shares to a newly created shareholder immediately?

The recipient needs an initial Issue so ERPNext can assign a folio number before a later transfer.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Shareholder Management](/erpnext/shareholder-management)
- [Share Reports](/erpnext/share-reports)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__shareholder-management.md -->
---
title: "Shareholder Management"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shareholder-management"
updated: "2026-08-14"
---

Nova Electronics Trading starts with three shareholders: Elena Brooks holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. As Nova raises capital and ownership changes, the finance team must answer three questions reliably: who the owners are, how many shares each one holds, and which transaction changed that balance. Shareholder management connects those answers instead of treating them as separate spreadsheets.



In ERPNext, the workflow has three parts. A [Shareholder](/erpnext/shareholder) identifies the owner. A [Share Transfer](/erpnext/share-transfer) records an Issue, Purchase, or Transfer. [Share Reports](/erpnext/share-reports) show the resulting balances and history.

[Screenshot on the live page: Nova shareholder register in ERPNext]

## Use the records in this order


| Step | Record                                   | Result                                                |
| ---- | ---------------------------------------- | ----------------------------------------------------- |
| 1    | Shareholder                              | Creates the owner master and contact context.         |
| 2    | Share Transfer with Issue                | Creates the first holding and assigns a folio number. |
| 3    | Share Transfer with Transfer or Purchase | Changes ownership or records a company buyback.       |
| 4    | Share Balance and Share Ledger           | Verifies current ownership and transaction history.   |


[Screenshot on the live page: Share issue type, shareholder, and share type highlighted]

## Keep the register reliable

Use submitted Share Transfers for every ownership change. Do not overwrite a shareholder's balance manually. Keep [Contacts](/erpnext/contact) and [Addresses](/erpnext/address) linked to the master, and use a consistent [Fiscal Year](/erpnext/fiscal-year) and posting date when related accounting entries are required.

## Frequently asked questions

### Does creating a Shareholder change the company's equity?

The master itself has no ledger impact. A submitted share issue records the ownership movement, and the related [Journal Entry](/erpnext/journal-entry) is used when accounting entries are required.

### Which report shows the current owner balance?

Share Balance shows current holdings. Share Ledger explains how those holdings changed transaction by transaction.

## Related topics

- [Shareholder](/erpnext/shareholder)
- [Share Transfer](/erpnext/share-transfer)
- [Share Reports](/erpnext/share-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)

<!-- page: erpnext/erpnext__shareholder.md -->
---
title: "Shareholder\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shareholder"
updated: "2026-08-14"
---

Nova Electronics Trading has three shareholders. Elena Brooks initially holds 6,000 shares, Marcus Lee holds 4,000, and Horizon Ventures LLC holds 1,000. Finance needs to know who owns shares, how to contact each owner, and which ownership transactions belong to each one. Keeping names in a spreadsheet makes it easy to lose the connection between the owner, their folio number, and their share history.



A Shareholder is the master record for a person or organisation that owns shares in a Company. It becomes the anchor for [share issues and transfers](/erpnext/share-transfer), balances, and the Share Ledger. Creating the master does not give the owner any shares. Ownership begins only after an Issue is submitted.

## Create a Shareholder

Open the Shareholder list and select **Add Shareholder**. Enter the shareholder's name and Company. Enable **Is Company** when the owner is an organisation rather than an individual.

[Screenshot on the live page: Shareholder list with fictional Nova owners]

Save the record. ERPNext assigns a Shareholder ID using the configured [naming series](/erpnext/document-naming-settings). Add the shareholder's [Contact](/erpnext/contact) and [Address](/erpnext/address) from the linked records so correspondence remains separate from ownership transactions.

[Screenshot on the live page: Shareholder name, company, and folio number highlighted]

## Folio number and share balance

The folio number uniquely connects a shareholder to their ownership transactions. It appears after the first share issue. The Share Balance section then shows holdings created by submitted Share Transfers.

## Frequently asked questions

### Why is the share balance empty after I create a Shareholder?

Saving the master records the owner but does not issue shares. Create a Share Transfer with Transfer Type set to Issue and submit it.

### Can a company be a shareholder?

An organisation can be maintained as a shareholder by enabling Is Company on its master record.

## Related topics

- [Shareholder Management](/erpnext/shareholder-management)
- [Share Transfer](/erpnext/share-transfer)
- [Share Reports](/erpnext/share-reports)
- [Company](/erpnext/company)

<!-- page: erpnext/erpnext__sharing.md -->
---
title: "Sharing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sharing"
updated: "2026-02-27"
---

**'Sharing' allows users to share a particular document with other users in ERPNext.**

In addition to user and role permissions, you can also share a document with another user if you have sharing rights for that document. Note that, a shared document will be visible to the other user even if the document is restricted via [User Permissions](/erpnext/user-permissions).

**How to share a document?**
----------------------------

1. Open the document that you want to share and click on the '+'icon under 'Shared With'.
2. Select the user with whom you need to share the document.
3. If the document is to be shared with all users then just select 'Everyone'.
4. Tick appropriate checkboxes to provide relevant rights to the user with whom the document is getting shared.
5. Click on the Add button to get the user added.
6. You can share the same document with multiple users by adding them one by one.

[Screenshot on the live page: Screenshot 2023-12-28 at 2.39.05 PM]  


**Note:-** The document indicates the users with whom is has been shared.

[Screenshot on the live page: Screenshot 2023-12-28 at 2.54.24 PM]  


### Related Topics

1. [Role and Role Profile](/erpnext/role-and-role-profile)
2. [Role Based Permissions](/erpnext/role-based-permissions)
3. [User Permissions](/erpnext/user-permissions)
4. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__shipment.md -->
---
title: "Shipment\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shipment"
updated: "2026-02-28"
---


**A Shipment is a document that keeps track of real-world Shipments created against a Delivery Note or independently.**

> Introduced in version 13

Shipments are particularly useful for shippers who want to track all their Shipment information such as AWB Number, Shipment Status, Carrier, etc. within ERPNext.

To access the Shipment list, go to:
> Home > Stock > Stock Transactions > Shipment

## 1. Prerequisites
Before creating and using a Shipment, it is advised that you create the following first:

* Company and Customer [Address](/erpnext/address) with Postal Code, Email Address and Phone Number set.
* Customer [Contact](/erpnext/contact).

## 2. How to create a Shipment
A Shipment can be created manually or from a Delivery Note:

### 2.1. Manual Shipment
To create a Shipment manually, follow these steps:

1. Go to the Shipment list, click on New.

 [Screenshot on the live page: Unsaved Shipment]
1. Select an option in the **Pickup from** field. On selecting one of the three options, you will be prompted to select a Company/Supplier/Customer based on your selection.
1. If you select 'Company' in the **Pickup from** field, along with the Address you must also select a **Pickup Contact Person** who will be a user from your organization, in ERPNext. Make sure the Last Name, Email Address and Phone Number are set for this user.
1. You can similarly fill the **Delivery To** section.
1. Add Shipment Parcel Information in the **Shipment Parcel** table.
1. Fill in the Value of Goods.
1. Select a Pickup Date.
1. Add a Description of Contents in this Shipment.
1. You can optionally fill the Shipment Information section if you are tracking Shipments manually.
1. Save and Submit.

 [Screenshot on the live page: Submitted Shipment]

### 2.1. Shipment from Delivery Note
To create a Shipment from a Delivery Note:

1. Click on **Create** > **Shipment** in the Delivery Note.

 [Screenshot on the live page: Submitted Shipment]

1. Fill the form as mentioned in the previous section.

## 3. Features

### 3.1. Shipment Parcel

You can specify the length, width, height and, weight of a parcel in the Shipment. If there are multiple parcels with identical dimensions, the **count** field can be set accordingly.

To automatically fetch frequently used parcel dimensions, a Parcel Template can be created and set in the **Parcel Template** field. After adding the template, click on the **Add template** button.

 [Screenshot on the live page: Submitted Shipment]

### 3.2. Shipment Information / Details
The Shipment Information section is an **optional** section where a user can manually track Shipment information. Here are some of the fields:

1. **Service Provider** (optional): A Service Provider can be a third-party service that provides shipping services from various carriers.
1. **Shipment ID**: The unique Shipment ID on your Shipping platform.
1. **Shipment Amount**: Total cost incurred on Shipment
1. **Carrier**: The Carrier that handles your Shipment and delivers it.
1. **Carrier Service** (optional): The type/category of service provided by the carrier. E.g. some carriers have categories such as Economy, Express, etc.
1. **AWB Number**: An air waybill (AWB) accompanies **international** air cargo. It usually has a unique **AWB Number**, that makes it easy to identify and track an air courier.
1. **Incoterm**: They are a set of internationally recognized rules which define the responsibilities of sellers and buyers. [Know more about it here.](https://iccwbo.org/resources-for-business/incoterms-rules/incoterms-2020/)

### 3.3 Automation

You can also automate rate comparison, label generation, tracking, etc. using our [Shipping Integration](/erpnext/erpnext_shipping).

### 4. Related Topics
1. [Delivery Note](/erpnext/delivery-note)
1. [Packing Slip](/erpnext/packing-slip)
