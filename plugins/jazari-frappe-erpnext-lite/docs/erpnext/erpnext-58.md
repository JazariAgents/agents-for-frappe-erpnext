<!-- Frappe documentation: erpnext, part 58 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__shipping-rule.md -->
---
title: "Shipping Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shipping-rule"
updated: "2026-02-26"
---

**Using Shipping Rule, you can define the cost for delivering the product to the customer or the supplier. Its a rule to define shipping charges applied to sales transactions**

Most of the companies (mainly retail) have a shipping charge applied based on the invoice total. You can setup Shipping Rule to address the requirement of varying shipping charges based on the Net Total of sales transactions. Use them to offer discounted shipping rates on high-value orders and standard rates on smaller ones.

To set up a Shipping Rule, go to:

`Selling > Setup > Shipping Rule` or `Accounts > Setup > Shipping Rule`

## How to create a Shipping Rule

1. Go to the Shipping Rule list, click on New.
2. Enter the Shipping Rule label, for example, 'Priority Shipping' or 'Next Day Shipping'.
3. When shipping charges are determined by a Shipping Rule, you must also provide the **Shipping Account**, **Cost Center**, and **Shipping Amount**. These details are required to populate the "Taxes and Other Charges" table in the transaction.
4. Under Calculate Based On, you can also change the calculation on which the Shipping Rule will be applied, like net total quantity or net total weight; by default, it is "Fixed".
5. Save

[Screenshot on the live page: Shipping Rule]

## Features

### Shipping Rule Conditions

On selecting Net Total or Net Weight, a table will appear where you can set the from and to values for the amount or weight. Enter the Shipping Amount to be calculated for the entered range. Add more conditions as necessary. You can select only one of the three calculation methods in one Shipping Rule.

[Screenshot on the live page: Shipping Rule Conditions]

Referring above, you will notice that shipping charges are reducing as the value increases. This shipping charge will only be applied if the transaction total falls under one of the above ranges.

### Valid for Countries

You can restrict the Shipping Rule to certain countries. Add the countries in the table. By default, the Shipping Rule will be applicable globally. If specific countries are mentioned, then Shipping Charges will be applied only if the Customer's country matches the country mentioned in the Shipping Rule.

[Screenshot on the live page: Country Specific Shipping Rules]

### Shipping Rule Application

Following is an example of how shipping charges are auto-applied on a Sales Order based on a Shipping Rule.

[Screenshot on the live page: Shipping Rule in Sales Order]

<!-- page: erpnext/erpnext__shop_by_category.md -->
---
title: "Shop by Category"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shop_by_category"
updated: "2026-03-02"
---

ERPNext offers a **Shop by Category** (`/shop-by-category`) page out of the box, where users can navigate to relevant products based on their needs without having to use filters right away.

To set up the categories (in the tabs) for this page, head over to:
> E Commerce Settings > Filters and Categories

In the **Filters and Categories** section, make sure **Enable Field Filters (Categories)** is enabled. The categories are pulled from the Website Item Fields table. The field filters such as Item Group, Brand, etc. are reused as categories on this page.

Once this is done, you will accordingly see tabs on the **Shop by Category** page (`/shop-by-category`).
[Screenshot on the live page: Shop by Category]

Additionally you can add a slideshow to this page (as seen above) via the **Shop By Category** section in **E Commerce Settings**.

### Fetching records in categories

#### Item Groups
Item Groups are handled a little differently due to its tree structure. Item Group records are fetched if the following conditions are all satisfied:

- The **Show in Website** field is enabled in the Item Group
- Item Group is the **top most group node** (**Is Group** enabled and parent is 'All Item Groups') or **top-most leaf node** (**Is Group** disabled and parent is 'All Item Groups')

Each card links to the respective Item Group page.

#### Other Categories
The other categories' records are simply fetched irrespective. If you want to hide certain records here too (e.g. in **Brand**), you can add a custom **Show in Website** field and it will filter out those records that have this field disabled.

> Custom doctypes **that are linked to Website Item via a link field** can also be included here along with Item Group, Brand, etc.

<!-- page: erpnext/erpnext__shopify_integration.md -->
---
title: "Shopify Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shopify_integration"
updated: "2026-03-02"
---


The Shopify Connector pulls the orders from Shopify and creates Sales Order against them in ERPNext.

While creating the sales order if Customer or Item is missing in ERPNext the system will create new Customer/Item by pulling respective details from Shopify.

### How to Setup Connector?

Shopify Connector is moved out from ERPNext and available through a Frappe App on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)

#### Note to users of old Shopify Connector

If you have not setup Shopify Connector on your ERPNext site you can proceed to next step.

If you are using old Shopify integration that's provided in ERPNext then you will have to disable the connector before proceeding. After installing the app, it will migrate existing data e.g. unique product_id for items to separate doctype. Once you are done configuring new integration, you can confirm the status of migration by going to "Ecommerce Integration Log" doctype.

#### App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
- If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`

The repository for app is hosted on GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/)



#### Create A Custom App in Shopify

1. Click on Apps in menu bar
[Screenshot on the live page: Menu Section]

2. Click on **Develop apps for your store** to create custom app
[Screenshot on the live page: new app]

3. Create New app
 [Screenshot on the live page]

4. Fill up the details and create app. The each app has its own API key, Password and Shared secret
 [Screenshot on the live page]

5. Allow following permissions to the app.
 - Draft Orders - Read and Write
 - Orders - Read and Write
 - Location - Read
 - Customers - Read
 - Assigned fulfillment orders - Read and Write
 - Products - Read and Write
 - Product listings - Read and Write
 - Inventory - Read and Write

 your final admin scopes should look like this:
 
 [Screenshot on the live page]

6. Install the app on your site
 [Screenshot on the live page]

#### Setting Up Shopify on ERPNext:-
Once you have created a Private App on Shopify, setup App Credentials and other details in Shopify Settings in ERPNext.

> To access Shopify Settings, go to:
Awesome search bar > Shopify Setting

1. Fill-up Shopify site URL, Access Token and API Secret from Shopify's Private App.
 [Screenshot on the live page]
 [Screenshot on the live page]

2. Setup Customer, Company and Inventory configurations.
3. 
[Screenshot on the live page: Shopify setting page]

3. Setup Sync Configurations.
 The system pulls Orders from Shopify and creates Sales Order in ERPNext. You can configure ERPNext system to capture payment and fulfilments against orders.
[Screenshot on the live page: Shopify sync config for orders]


4. Setup Tax Mapper.
 Prepare tax and shipping charges mapper for each tax and shipping charge you apply in Shopify. You can find name of your taxes from your Shopify Admin page.
[Screenshot on the live page: Shopify tax mapping]
[Screenshot on the live page: Finding Shopify Tax names]



After setting up all the configurations, enable the Shopify sync and save the settings. This will register the API's to Shopify and the system will start Order sync between Shopify and ERPNext.


### Syncing Old Orders From Shopify

Once you are done with the Shopify configuration and have enabled Shopify Syncing, you also get a provision to sync your old orders from Shopify into ERPNext. This syncing will happen in background and can take few hours depending on number of orders you have.

1. Enable "Sync Old Shopify Orders"
2. Enter the From and To dates between which the orders need to be synced
[Screenshot on the live page: shopify sync old orders] 

### Inventory Sync

You can update your inventory with Shopify for items that are synced from Shopify. Inventory sync is done every hour with a scheduled job. Inventory levels of items that have changed since last sync are pushed to Shopify. Inventory levels of ERPNext warehouses are mapped 1 to 1 with Shopify locations.

1. To enable inventory sync click on the checkbox, this will show you a table to map ERPNext warehouse with Shopify Location.
2. Select sync frequency. 30 to 60 minutes is recommended frequency.
3. Click on "Fetch Shopify Locations" button to populate Shopify locations in the table.
4. Link each location with ERPNext warehouse.
5. Save the settings.

[Screenshot on the live page: Inventory sync with shopify]


> Note: This connector assumes that ERPNext is main source of information about inventory levels, any changes done to Shopify inventory levels will be overwritten by ERPNext if ERPNext inventory levels change.

> Note: Shopify does not support fractional quantity. If fractional quantity is found in ERPNext, the inventory level on Shopify will be set by rounding it down to nearest whole number.


### Item Sync

You can enable sync of new ERPNext items to Shopify by checking "Upload new ERPNext items to Shopify".

You can also update Shopify item upon updating ERPNext item.

Following fields are uploaded / updated:

| ERPNext Field | Shopify Field |
| :-: | :-: |
| Item Name | Title |
| Item Code | SKU |
| Description body | Description |
| Item Group | Product Type |
| Weight per Unit | Weight |
| Weight UOM | Weight UOM |

By default all items are marked as Draft on Shopify and not published in any store.

Purpose of providing this functionality is to sync items with Shopify. It's not possible to map every fields 1-to-1. Upon creation of item on Shopify using this method, it's linked with ERPNext, this eliminates possibility of duplication. You can modify items on Shopify later to add more details.


> Note: This feature is not supported in data import or for variant / template items.


### Cancellation of Orders
This connector handles various cancellation scenario in following manner:

1. If Order on Shopify is cancelled and it doesn't have invoice or Delivery note linked against it then ERPNext Sales Order is cancelled.
2. If ERPNext Sales Order does have any linked document, then status of order on Shopify is added to the respective document. Cancellation and preparation of appropriate documents has to be done by user based on this information.

<!-- page: erpnext/erpnext__shopping-cart.md -->
---
title: "Shopping Cart\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/shopping-cart"
updated: "2026-03-02"
---


In addition to listing products, ERPNext also allows selling them via the Shopping Cart.

To enable Shopping Cart, go to:

> E Commerce Settings > [Shopping Cart](/erpnext/e_commerce_settings#shopping-cart)

You can even build a **landing page** for your store at a custom route (eg. /*store*).
[Learn More](/erpnext/store-landing-page).

## 1. Item Types

Shopping Cart works differently for Items with and without variants.

### 1.1 Items without variants

Items without variants have their dedicated product page and an **Add to Cart** button.

[Screenshot on the live page: Item without Variants]
*Item without Variants*

### 1.2 Items with variants

Since Item Templates can't be bought directly, there is a Configure button to
choose the specific variant and add it to cart.

[Screenshot on the live page: Item with Variants]
*Item with Variants*

## 2. Cart Quotation

If checkout is disabled, when your customers add an item to cart, they can click
on the **Request for Quotation** button to get a quote for it. A [Quotation](/erpnext/quotation)
is generated in the system.

## 3. Cart Checkout

You can enable checkout from the [Checkout Settings](/erpnext/e_commerce_settings#checkout-settings) section in **E Commerce Settings**.

[Screenshot on the live page: Cart Checkout]
*Cart Checkout*

<!-- page: erpnext/erpnext__show-hide-modules.md -->
---
title: "Show or Hide Modules | ERPNext Documentation"
description: "Understand the deprecated ERPNext Show or Hide Modules feature and use current roles, workspaces, domains, and module settings instead."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/show-hide-modules"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. A service coordinator needs Support and Selling, but not Manufacturing. An administrator finds an older instruction that says to open Show or Hide Modules and remove Manufacturing. In current ERPNext versions, that control is deprecated, and hiding a card would not have been a reliable way to protect manufacturing data anyway.



Use the current control that matches the real goal. Domain Settings decides which installed business domains are active for the whole site. Roles and Role Permissions decide which DocTypes a user can access. User Permissions restrict particular records such as a Company or Territory. Workspace configuration controls what appears in navigation. Module Settings changes how a process behaves.

## Current status

The earlier Show or Hide Modules feature is no longer supported or required from version 15 onward. Do not search for the old Show/Hide Cards control or use a legacy screenshot to configure a current develop site.

## Choose the correct replacement


| Goal                                             | Current control                   | Nova example                                                             |
| ------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------------ |
| Remove an irrelevant industry for the whole site | Domain Settings                   | Nova leaves Education inactive because it does not run a school.         |
| Prevent a user from opening a DocType            | Role and Role Permissions Manager | The service coordinator has no Manufacturing transaction permissions.    |
| Restrict records inside an allowed DocType       | User Permissions                  | A sales user can work only with an assigned Company or Territory.        |
| Simplify navigation                              | Workspace visibility and roles    | The service team's workspace shows Support and Selling shortcuts.        |
| Change module behaviour                          | The relevant Module Settings page | Selling Settings controls Sales Order behaviour without changing access. |


## Verify access instead of appearance

Test with the affected user's account or assigned roles. Confirm that an unauthorised DocType cannot be opened through search or a direct route, not merely that its workspace card is absent. A hidden shortcut is a cleaner interface; a denied permission is access control.

[Screenshot on the live page: Current ERPNext Workspace list used when reviewing navigation visibility]

## Troubleshooting

### The old Show or Hide Modules option is missing

The feature is deprecated on current versions. Identify whether the requirement concerns domains, permissions, record restrictions, workspace navigation, or module behaviour, then use the matching current control.

### A hidden workspace is still accessible through search

Workspace visibility does not replace DocType permissions. Remove the inappropriate role or permission and test the direct DocType route.

### A user has the right role but sees too many records

Use User Permissions or document-specific permission logic to restrict linked records such as Company or Territory.

## Frequently asked questions

### Can Module Settings hide a module from one user?

Module Settings changes process behaviour. Use roles and Workspace configuration for user-specific access and navigation.

### Does hiding a workspace secure its data?

A hidden workspace removes a navigation surface. Server-side role and record permissions must protect the data.

### Should old sites keep using Show or Hide Modules?

Plan a move to the current controls before upgrading or maintaining the configuration. Verify the exact supported behaviour on the site's version.

### Why keep this documentation page?

It helps readers who find older instructions understand why the control is missing and where to configure the intended outcome now.

## Related topics

- [Domain Settings](/erpnext/domain-settings)
- [Module Settings](/erpnext/module-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [User Permissions](/erpnext/user-permissions)
- [Workspace](/erpnext/workspace)
- [Adding Users](/erpnext/adding-users)

<!-- page: erpnext/erpnext__simplified_ksa_vat_management_and_reporting.md -->
---
title: "KSA VAT Management and Reporting"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting"
updated: "2026-02-26"
---

Generate report for the **VAT on Sales** and **VAT on Purchases**

[Screenshot on the live page: image-20210819234431755]

Find the new KSA VAT report and KSA vat settings document in the Accounting Workspace

On creation of the first company for the country Saudi Arab. KSA VAT Setting is created automatically. For any new companies create new settings.

KSA VAT Settings is mapping Item Tax Template and Account to the respective title to be shown in the report

[Screenshot on the live page: image-20210819233134033]

Note: Multiple Item Tax Template can be set for each item. 

A good example in the sales cycle would be an item that is treated as a Standard rated Sales and as well as Zero rated domestic Sales. Same case can be applied on the purchase cycle.

[Screenshot on the live page: image-20210819233839064]

Use the Item Tax Templates in the Sales and Purchase Invoice. The data should result in a similar KSA VAT Report

[Screenshot on the live page: image-20210819235844178]

KSA VAT Invoice - Print Format for Sales Invoice

[Screenshot on the live page: ksa-vat-invoice-a4-page-1]
[Screenshot on the live page: ksa-vat-invoice-a4-page-2]

<!-- page: erpnext/erpnext__single-payment-multiple-invoices.md -->
---
title: "Single Payment Against Multiple Invoices | ERPNext Documentation"
description: "Allocate one ERPNext payment across several customer or supplier invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/single-payment-multiple-invoices"
updated: "2026-08-01"
---

A single bank receipt or payment can settle several invoices. Keep it as one Payment Entry and use the References table to show exactly how the amount is distributed.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Single Payment Against Multiple Invoices

1. Create the Payment Entry for the correct party.
2. Enter the actual bank amount and reference.
3. Fetch outstanding invoices.
4. Select the invoices included in the remittance and set each allocation.
5. Record any discount, fee, withholding, or exchange difference explicitly.
6. Confirm totals and submit.

[Screenshot on the live page: One ERPNext Payment Entry allocated across two Sales Invoices]

## Important fields and what they mean


| Field                  | What it controls                                 |
| ---------------------- | ------------------------------------------------ |
| Outstanding Amount     | Balance available to clear on each invoice.      |
| Allocated Amount       | Portion of this payment assigned to the invoice. |
| Total Allocated Amount | Sum across references.                           |
| Unallocated Amount     | Payment balance left for later allocation.       |
| Difference Amount      | Amount that requires an accounting explanation.  |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### Selecting rows does not update the Paid Amount

Enter the actual payment amount, retain the intended invoice references, and set each Allocated Amount. Row selection alone is not a request to recalculate the bank amount.

### The total allocation exceeds the payment

Reduce one or more allocations so the total does not exceed the amount available. Leave unpaid invoice balances outstanding rather than changing their totals.

### One invoice is missing

Check that all references belong to the same party, Company, receivable or payable account, and compatible currency. Confirm submission status and remaining outstanding amount.

## Frequently asked questions

### Can one payment settle both Sales Invoices and credit notes?

Use only reference types supported by the current allocation dialog and confirm the net effect. Reconcile complex credit scenarios carefully and verify the party ledger.

### Can invoices for different customers share one Payment Entry?

A standard Payment Entry has one party. Record separate entries per Customer and reconcile them to a combined bank deposit if necessary.

### Can the payment partially settle every selected invoice?

Enter a partial Allocated Amount for each reference. ERPNext leaves the remaining balances outstanding.

### Which invoice should be allocated first?

Follow remittance advice. Without it, apply the company's documented policy, such as oldest due first, and retain evidence of the decision.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__sms-setting.md -->
---
title: "SMS Settings\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/sms-setting"
updated: "2026-03-02"
---


**You can subscribe to an SMS provider to send SMS to mobile numbers.**

To integrate SMS in ERPNext, approach an SMS Gateway Provider who provides HTTP
API. They will create an account for you and will provide a unique username
and password.

To access SMS settings, go to:
> Home > Settings > SMS Settings

To configure SMS Settings in ERPNext, find out their HTTP API (a document
which describes the method of accessing their SMS interface from 3rd party
applications). In this document, you will get a URL which is used to send the
SMS using HTTP request. Using this URL, you can configure SMS Settings in
ERPNext.

Example SMS Gateway URL:

 http://instant.smses.com/web2sms.php?username=<username>&amp;password;=<password>&to;=<mobilenumber>&amp;sender;=<senderid>&amp;message;=<message>


[Screenshot on the live page: SMS Setting 2]

> Note: For SMS Gateway URL, only include the string before the "?".

Example:

 http://instant.smses.com/web2sms.php?username=abcd&amp;password;=abcd&to;=9900XXXXXX&amp;sender;
 =DEMO&amp;message;=THIS+IS+A+TEST+SMS

The above URL will send SMS from account abcd to mobile number 9900XXXXXX with
sender ID as DEMO with a text message as "THIS IS A TEST SMS".

Note that some parameters in the URL are static. You will get static values
from your SMS Provider like username, password, etc. These static values should
be entered in the Static Parameters table.

[Screenshot on the live page: SMS Setting]

## How to configure ERPNext with Voip.ms

The first step is to login to voip.ms account. Then go **Main menu**, **SOAP and REST/JSON API**.
Enable the API, set a password and whitelist your server ip address.

Then go to DIDs and enable SMS on the number SMS will be sent from.

Set SMS Gateway to **https://voip.ms/api/v1/rest.php**

Set Message Parameter to **message**

Receiver Parameter to **dst**

Create 4 new Static Parameters:

- **api_username** (voip.ms account username

- **api_password** (the API password configured few minutes ago)

- **method** set value to **sendSMS**

- **did** (the 10 digits DID that will be used to send the sms)

[Screenshot on the live page: Voip.MS Setting]

Then go to SMS Center to test if everything works properly.

### Related Topics
1. [Email Account](/erpnext/email-account)
1. [Notifications](/erpnext/notifications)
</message></senderid></mobilenumber></password></username>

<!-- page: erpnext/erpnext__social-media-settings.md -->
---
title: "Social Media Settings | ERPNext Documentation"
description: "Configure Social Media Settings in ERPNext for supported social publishing integrations."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/social-media-settings"
updated: "2026-07-23"
---

Social Media Settings in ERPNext provides access to the supported social publishing integrations configured for your site. Availability depends on the ERPNext version and the external platform's current API requirements.

## Configure a social integration

1. Open the settings page for the required platform.
2. Enter the application credentials and identifiers issued by that platform.
3. Save the settings and test the connection with a non-sensitive post.
4. Restrict access to users responsible for approved company communication.

Never place social platform secrets in documentation, screenshots, comments, or shared messages. If an integration stops working, verify the external platform's API access, callback URL, permissions, and ERPNext version before replacing credentials.

## Related topics

- [LinkedIn Settings](/erpnext/linkedin-settings)
- [Twitter Settings](/erpnext/twitter-settings)
- [Campaign](/erpnext/campaign)

<!-- page: erpnext/erpnext__south_africa.md -->
---
title: "Requirements for South Africa"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/south_africa"
updated: "2026-02-28"
---

ERPNext aims to support local regulation for different regions in the world. In most cases, ERPNext is very flexible, so you can easily add custom fields and make custom reports to support the regulation of your region.

This section contains region-specific features for South Africa.

- [VAT Audit Report](/erpnext/vat_audit_report)

<!-- page: erpnext/erpnext__stale-cheque-accounting.md -->
---
title: "Stale Cheque Accounting | ERPNext Documentation"
description: "Reverse or replace an expired check while preserving the ERPNext audit trail."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stale-cheque-accounting"
updated: "2026-08-01"
---

A stale check has passed the validity period and is no longer expected to clear. Do not delete the original entry. Reverse or cancel it according to its status, then issue a replacement when required.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Stale Cheque Accounting

1. Confirm with the bank that the check is stale and has not cleared.
2. Locate the original Payment Entry and its ledger impact.
3. Cancel it when ERPNext permits and your control policy allows cancellation.
4. If cancellation is not appropriate, post an authorized reversing Journal Entry with a clear reference.
5. Create a new Payment Entry for the replacement check and reconcile only when it clears.

[Screenshot on the live page: Stale Cheque Accounting in ERPNext]

## Important fields and what they mean


| Field                  | What it controls                                    |
| ---------------------- | --------------------------------------------------- |
| Cheque or Reference No | Identifies the original instrument.                 |
| Reference Date         | Issue date of the check.                            |
| Posting Date           | Accounting date of the original or reversal entry.  |
| Remarks                | Reason for reversal and replacement reference.      |
| Clearance Date         | Date the bank confirms settlement, when applicable. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The stale cheque belongs to a closed accounting period

Do not cancel or backdate into a locked period without approval. Record the reversal or reclassification in the current permitted period using the workflow approved by your accountant.

### Reissuing the cheque would pay the invoice twice

First reverse or clear the stale cheque's payment effect, verify that the supplier balance is outstanding, and only then issue the replacement.

### The cheque was actually dishonoured, not merely stale

Record the correct event and supporting evidence. A dishonoured cheque can include bank charges and an immediate restoration of the invoice balance, while a stale cheque has expired without clearing.

## Frequently asked questions

### When does a cheque become stale?

The validity period depends on the bank and jurisdiction. Confirm the date with the bank rather than assuming a universal number of months.

### Should the original Payment Entry be deleted?

Keep the audit trail. Use cancellation, reversal, or a current-period adjustment according to the document status and accounting-period controls.

### Can a replacement cheque reuse the same reference number?

Use the new cheque's actual reference and link it to the reversal or stale cheque explanation. Reusing the old number weakens traceability.

### Does marking a cheque stale automatically reopen the invoice?

The invoice is restored only when the accounting effect of the original payment is properly reversed or unallocated. Verify Accounts Payable afterward.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)
