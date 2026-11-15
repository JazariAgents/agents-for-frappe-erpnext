<!-- Frappe documentation: erpnext, part 57 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__serial-no-naming.md -->
---
title: "Serial Number Naming"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-no-naming"
updated: "2026-02-26"
---


Serial Nos. is unique value assigned on each unit of an item. Serial no. helps in tracking item's warranty and expiry details. Generally high value items like machines, computers, costly equipments are serialized.

To make item Serialized, in the Item master, check **Has Serial No**.

There are two ways Serial no. can be generated in ERPNext.

###1. Serializing Purchase Items

If purchased items are received with Serial Nos. applied by OEM (original equipment manufacturer), you can follow same Serial No in ERPNext as well. While creating Purchase Receipt, you shall scan or manually enter Serial nos. for an item. On submitting Purchase Receipt, Serial Nos. will be created in the backend as per Serial Nos. provided for an item. If using OEM' Serial No., then in the Item master, Prefix should not be mentioned for serializalization. As per this scenaio, Prefix field should be left blank.

If received items already has its Serial No. barcoded, you can simply scan that barcode for entering Serial No. in the Purchase Receipt. Click [here](https://frappe.io/blog/management/using-barcodes-to-ease-data-entry) to learn more about it.

On submission of Purchase Receipt or Stock entry for the serialized item, Serial Nos. will be auto-generated.

![Serial Nos Entry](/files/serial-naming-1.png)

Generated Serial numbers will be updated for each item.

![Serial Nos Created](/files/serial-naming-2.png)

###2. Serializing Manufacturing Item

To Serialize Manufacturing Item, you can define Series for Serial No. Generation in the Item master itself. Following that series, system will create Serial Nos. for Item when its Production entry is made.

####2.1 Serial No. Series

When Item is set as serialized, it will allow you to mentioned Series for it.

![Serial Nos Created](/files/serial-naming-3.png)

####2.2 Production Entry for Serialized Item

On submission of production entry for manufacturing item, system will automatically generate Serial Nos. following Series as specified in the Item master.

![Serial Nos Created](/files/serial-naming-4.png)

<!-- page: erpnext/erpnext__serial-no.md -->
---
title: "Serial Number"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/serial-no"
updated: "2026-03-06"
---

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.



To enable serial / batch feature for the item, first check the 'Enable Serial and Batch No for Item' checkbox in the 'Stock Settings'.

![](/files/Screenshot 2026-03-06 at 11.52.18 AM.png)



As discussed in the [Item](/erpnext/item) page, if an **Item** is *serialized*, a **Serial Number** (Serial No) record is maintained for each quantity of that **Item**. This information helps track the location of the Serial No, its warranty and end-of-life (expiry) information.

You can also track from which **Supplier** you purchased the **Serial No** and to which **Customer** you have sold it. The **Serial No** status will tell you its current inventory status.

If your Item is *serialized* you will have to enter the Serial Nos in the related column with each Serial No in a new line. You can maintain single units of serialized items using Serial Number.

To access the Serial Number list, go to: > Home > Stock > Serial No and Batch > Serial No

1. Prerequisites

---

Before creating and using a Serial Number, it is advised that you create the following first:

- [Item](/erpnext/item)
- Enable 'Has Serial No' in the Item master ![Serial No Enabled](/files/serial-no-enabled.png)

2. How to create a Serial Number

---

Usually, Serial Numbers are auto-created when transactions are made against a serialized Item. This works only when 'Has Serial No' is enabled and a series is set in the Item master.

For example, a series was set for the following Item as 'PB2L.#####'. Then a Stock Entry was submitted to receive the Item. The Serial Numbers were created accordingly.

![Serial No Created](/files/serial-no-created.png)



However, if you want to create a Serial No *manually* follow these steps:

1. Go to the Serial Number list, click on New.
2. Enter a Serial Number.
3. Enter the Item Code and details will be fetched.
4. If any transaction is done with an item, Serial No cannot be set or unset.
5. Save.

Inventory of an Item can only be affected if the Serial No is transacted via a Stock transaction (Stock Entry, Purchase Receipt, Delivery Note, Sales Invoice). When a new Serial No is created directly, its Warehouse cannot be set.

![Serial Number](/files/serial-no.png)



### 2.1 Notes about Serial Number

- The Status is set based on Stock Entry.
- Only Serial Numbers with status 'Available' can be delivered.
- Serial Nos can automatically be created from a Stock Entry or Purchase Receipt. If you mention Serial No in the Serial Nos column, it will automatically create those serial Nos.
- If in the Item Master, the Serial No Series is mentioned, you can leave the Serial No column blank in a Stock Entry / Purchase Receipt. Serial Nos will automatically be set from that series.

3. Features

---

### 3.1 Purchase/Manufacture details

The document from which the Serial No was created will be shown. If you purchased it from a Supplier, it'll be linked here.

### 3.2 Delivery Details

If the Serial No was generated from a Sales Order, the Customer will be linked here.

### 3.3 Warranty/AMC Details

If the Item is under warranty or AMC (Annual Maintenance Contract), the expiry dates for these can be set.

### 3.4 More Information

Any additional information about this specific Item unit can be set under 'Serial No Details'.

4. Video

---

### 5. Related Topics

1. [Item Codification](/erpnext/item-codification)
2. [Item Variants](/erpnext/item-variants)
3. [Serial Number Naming](/erpnext/serial-no-naming)

<!-- page: erpnext/erpnext__service-level-agreement.md -->
---
title: "Service Level Agreement\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/service-level-agreement"
updated: "2026-02-28"
---


**A service level agreement (SLA) is a contract between a service provider (either internal or external) and the end user on the level of service expected from the service provider.**

SLAs are output-based, their purpose is specifically to define the timeline in which the Customer will receive the service. SLAs do not define how the service itself is provided or delivered.

To access the Service Level Agreement list, go to:
> Home > Support > Service Level Agreement > Service Level Agreement

## 1.Prerequisites

Before creating and using a Service Level Agreement, it is advised that you create/update the following first:

* [Holiday List](/hr/holiday-list)

* Enable **Track Service Level Agreement** in Support Settings

 ![Service Level Agreement](/files/sla-setting.png)

## 2. How to Create a Service Level Agreement
1. Go to the Service Level Agreement list, click on New.
1. Enter a name for the Service Level.
1. Select an Employee group, that will handle a particular Service Level.
1. Set a Holiday List. Service Level Agreement won't be applied in the days mentioned in the Holiday List.
1. 'Enable' determines if a Service Level Agreement is enabled or disabled.
1. Ticking 'Default Service Level Agreement' will apply this SLA to a customer if they don't have a particular SLA assigned to them.
1. Entity Type: Service Level Agreements can be assigned to a Customer/Customer Group/Territory enabling you to apply Service Level Agreement based on these factors.
1. Entity: Select the specific Customer/Customer Group/Territory.
1. Start / End Date: Defines the validity of the agreement.
1. Priorities: You can set multiple Issue Priorities and their Time to Respond and Resolve (in hours and mins).

 ![Service Level](/files/priorities.png)
1. Default Priority: Default Priority selected in Priorities table that will be applied in the Service Level Agreement.
1. Support Hours: Contains the Days of the week on which Support is provided. Has a Start Time and End Time of the Working day.

 ![SLA Support Hours](/files/sla-support-hours.png)
1. Save.

 ![SLA](/files/sla.png)

## 3. Features
### 3.1 Applies to New Issues

Once an SLA is saved, it'll be applied to Issues raised by Customers/Territories as per the option you chose in 'Entity Type'.

![SLA in Issue](/files/sla-entity-type.png)

### 3.2 Resetting an SLA
An SLA can also be reset until the time does not fail. For example, if the SLA is 3 days, you can reset the SLA only within 3 days of the Issue being created. After that, the Service Level will display failed.

![SLA Issue](/files/reset-sla.gif)

### 3.3 Time respond / resolve in Issues
The time to respond to an Issue and the time to resolve will be shown:
 ![SLA in Issue](/files/sla-in-issue.png)

These times are based on the timelines set in the 'Priority' field in the Service Level's Priorities table.


### 3.4 Pause SLA on Statuses
From version 13 onwards, ERPNext allows you to pause SLA on issues when you are waiting for an event to happen. You can do this by selecting a status that is configured in this "Pause SLA On" table.

* Set the statuses on which you want to pause SLA in the SLA document. You can also add custom statuses here.
 ![Service Level](/files/pause-sla.png)
* When the status is changed to any of the above, resolution and response fields are unset and the dashboard indicators change to:
 ![Service Level](/files/hold-indicator.png)
* When the status of the issue changes back to a non-hold status (which is not configured in the "Pause SLA On" table), the **Total Hold time** field will be set in your Issue document.
 ![Service Level](/files/total-hold-time.png)
The Response and Resolution time will be recalculated by adding the hold time, thereby restarting your SLA timers.

> Note: Service Level DocType was removed in version 13 and all functions are handled only with the Service Level Agreement DocType.

<!-- page: erpnext/erpnext__session-defaults.md -->
---
title: "Session Defaults | ERPNext Documentation"
description: "Use ERPNext Session Defaults to temporarily prefill a company or other value for one user session without changing global defaults."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/session-defaults"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor with a child company, Nova Electronics Trading. Priya normally works in the parent company's books, but this afternoon she must enter and review only the subsidiary's transactions. Changing the global Company would affect everyone. Re-selecting the subsidiary on every form and report makes it easy to miss one record.



Session Defaults lets Priya choose Nova Electronics Trading for her current login session. New supported transactions and reports can begin with that Company already selected. Other users keep their own context, and the temporary choice is cleared when Priya logs out.

## Allow a value to be used as a Session Default

Open **Session Default Settings** and add the DocTypes that users may choose temporarily. Company is the most common example. Add only fields that provide a useful and unambiguous working context.

![Company configured as an available ERPNext Session Default](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-session-default-settings.png)


| Setting                | What it means                                           | Nova example                                                               |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| Session Defaults table | DocTypes available in the user's session-default menu   | Company allows Priya to choose Nova Electronics Trading for the afternoon. |
| Reference DocType      | The master whose record will become the temporary value | Selecting Company presents Companies the user is permitted to access.      |


## Select the value for the current session

Open the user menu or sidebar Session Defaults control, then choose the permitted value. Create a new transaction or open a report and confirm the Company is prefilled. A submitted record must still be checked before relying on the default.

## Understand the scope

Session Defaults affects the current user and current session. It does not change Global Defaults, does not grant access, and does not rewrite existing records. Logging out clears the temporary choice. A value may also be replaced when a mapped source document or a more specific transaction rule supplies the field.

## Troubleshooting

### The Session Defaults option is missing

A System Manager must first add an allowed Reference DocType in Session Default Settings. The user also needs permission to the referenced records.

### The selected Company is not used

Test with a new supported document. A mapped document, user default, or document-specific rule may supply a more specific Company.

### The old value appears after changing it

Reload the form or create a new draft. Existing open forms can retain values loaded before the session change.

## Frequently asked questions

### Does a Session Default apply to other users?

The value belongs to the current user's session. It does not change the common site default.

### Is a Session Default permanent?

Logging out clears it. Use a user default or Global Defaults when the choice should persist according to policy.

### Can it bypass User Permissions?

A default only suggests a value. The user must still have permission to read and use that record.

### Can several DocTypes be configured?

The settings table can allow more than one reference type, but each should provide a clear working context rather than adding clutter.

## Related topics

- [Global Defaults](/erpnext/global-defaults)
- [System Settings](/erpnext/system-settings)
- [Company](/erpnext/company-setup)
- [User Permissions](/erpnext/user-permissions)
- [Adding Users](/erpnext/adding-users)
- [Reports](/erpnext/reports)

<!-- page: erpnext/erpnext__set-language.md -->
---
title: "Set Language | ERPNext Documentation"
description: "Set the default ERPNext language or a user-specific language and understand translation scope, fallback, and verification."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/set-language"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. Most employees use ERPNext in English, but the company hires Sofia to coordinate Spanish-speaking customers and suppliers. Changing the whole site to Spanish would disrupt the rest of the team, while forcing Sofia to translate every menu in her head makes routine work slower and more error-prone.



ERPNext separates the site's default language from a user's preferred language. The System Manager can keep English as the shared fallback and set Spanish only for Sofia. When she signs in again, supported labels and messages appear in her language while other users continue in English.

## Set the default site language

Open **System Settings**, choose **Language**, save, and reload the site. Use this when the chosen language should be the default for users who do not have a personal override.

![Default Language in ERPNext System Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-system-localisation.png)

## Set a language for one user

Open the User record, select the preferred **Language**, save, then ask the user to sign out and sign in again. Nova assigns Spanish to Sofia without changing the default for the finance and warehouse teams.

![Language field on an ERPNext User record](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-user-language.png)


| Choice                             | Scope                    | Example                                                                                                        |
| ---------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| System Settings Language           | Default for the site     | English remains Nova's shared default.                                                                         |
| User Language                      | One user                 | Sofia sees Spanish where translations exist.                                                                   |
| Written master or transaction text | The saved content itself | A Customer name or Item description remains the language in which it was entered unless separately translated. |


Translation coverage can vary by app and version. Product labels may be translated while custom fields, user-entered text, print-format content, or a newly released message remains in the source language.

## Troubleshooting

### The interface did not change

Save the User or System Settings record, then sign out and sign in again. Confirm the User record has the expected language and that the translation exists.

### Some labels remain in English

The app, custom field, or new message may not have a translation. Verify the source text and contribute or maintain the translation rather than changing unrelated settings.

### Printed documents use the wrong language

Print Format text, letterheads, Item descriptions, and transaction content may need separate translated templates or records.

## Frequently asked questions

### Can every user choose a different language?

A User record can carry a personal language where the user has permission and translations are available.

### Does changing language translate existing Customer or Item names?

The setting translates supported interface text. It does not rewrite business data entered by users.

### Which language is used when a translation is missing?

ERPNext falls back to the available source text, commonly English.

### Does language change date and number formats?

Language can influence presentation, but System Settings and Currency formatting also matter. Verify both when localisation looks inconsistent.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Adding Users](/erpnext/adding-users)
- [Translations](/erpnext/translations)
- [Country](/erpnext/country)
- [Global Defaults](/erpnext/global-defaults)
- [Print Format](/erpnext/print-format)

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

![Float and Currency Precision in ERPNext System Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-precision-settings.png)


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

 ![Sales Graph](/files/sales_history_graph.png)

1. You can set the **Sales Target** field to track progress against the graph:

 ![Setting Sales Goal](/files/setting_sales_goal.gif)

1. The target progress is also shown in notifications:

 ![Sales Notification](/files/sales_goal_notification.png)

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

 

![](/files/6T6CWP6.png)

 

 

2\. Expand the field for which you want to store a default value and enter it under Display -> Default

 

![](/files/TjzsYhu.png)

 

![](/files/th62UXt.png)

 

 

Check out the below GIF where we have set _default_ value as **Stores - ETL** for field "Default Source Warehouse" in DocType Stock Entry:

 

![](/files/wXMccxf.gif)

 

 

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

![A Product Discount Pricing Rule configured for Buy 1 Get 1 Free.](https://novacompanies.m.frappe.cloud/files/bogo-pricing-rule.png)

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

![](/files/PIoVfY1.png)

Scroll down to the **Email Settings** section where you can add your signature in HTML:  

![](/files/4swM1Yz.png)

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

Click on SMTP Relay![Screenshot 2024-06-01 at 12.44.17 PM](/files/Screenshot 2024-06-01 at 12.44.17 PM.png)  


Generate an API Key![Screenshot 2024-06-01 at 12.44.33 PM](/files/Screenshot 2024-06-01 at 12.44.33 PM.png)  
  
**Step 2:** Once your *API key* has been created, you need to configure it in your ERPNext account &gt; Create a **New** **Email Account.**

  


**Email Address:** *Your Email Address*

**Service:** Select "*SendGrid*"

Check "Use Different Email ID"

**Alternative email ID:** apikey

**Password:** *&lt;API Key Generated in step 1&gt;*

Outgoing server: &lt;server name generated in step 1&gt;

Port: &lt;port number generated above&gt;

![Screenshot 2024-06-01 at 12.44.45 PM](/files/Screenshot 2024-06-01 at 12.44.45 PM.png)  


For SSL connections, uncheck the "use TLS" option![Screenshot 2024-06-01 at 12.45.14 PM](/files/Screenshot 2024-06-01 at 12.45.14 PM.png)  


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

![Sales tax template](/files/sales-tax-template.webp)

Review whether purchase tax should be added to valuation, treated as recoverable input tax, or posted as an expense.

## Use Tax Categories

A Tax Category identifies a tax treatment, such as domestic standard, export, or exempt.

![Tax Category](/files/tax-category.webp)

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

![ERPNext Desk showing the installed applications available after sign-in](https://novacompanies.m.frappe.cloud/files/setup-20260814-setting-up-desk.png)



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

  


![](/files/ubLZfPq.png)

  


This means that every time a new Item is created, it will be disabled by default, unless approved (as seen in the screenshot below). 

  


![](/files/yPOQ2fT.png)

  


  


2) Next, set the Workflow.

  


In the States table, on approval, make sure to update the "Disabled" (or Enabled) checkbox to 0 (or 1 in case of enabled) as shown below.

  


  


![](/files/Qf3QXyo.png)

  


This will ensure that whenever the Item is approved, the Item will automatically be enabled and you will be able to use it in transactions.

  


Check the below GIF to understand the workflow in detail:

  


![](/files/olzpAk2.gif)

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

![Enable Two Factor Auth](/files/twofactor-1.png)


On activation of 2FA from setup, it is also activated for the Role "All". In this way, all users including the Administrator have to perform a 2nd level authentication with a token. By unchecking the "Two Factor Authentication" checkbox in the "All" role and enabling it in other roles, the need to login with a token can be limited to specific roles. 2FA does not apply to login by Web Users and API login

![Role Enable Two Factor Auth](/files/twofactor-2.png)

If using SMS authentication, please make sure that your SMS settings are updated

![SMS Settings](/files/twofactor-3.png)

If using Email, make sure that your outgoing Email account settings are updated

![Email Settings](/files/twofactor-4.png)

When the new user tries to log in for the first time in a system that has two-factor authentication enabled and which has the authentication option as OTP App, an email is sent containing a link to the QR Code.

![Email Notify Two Factor](/files/twofactor-5.png)
![QR Code Page](/files/twofactor-6.png)

Scanning the QR Code with an authentication app like Google Authenticator registers the access for the user and automatically starts to generate tokens that can be used to login

![Two Factor Scan App](/files/twofactor_app.jpeg)

If either of Email/SMS is used as the authentication method, you get notifications also

![Email and SMS](/files/twofactor-8.png)



### Frequently asked questions (FAQ)

Q. I am unable to login even after following entire process. 

Ans: Frappe uses TOTP based OTP algorithm, which depends on your device's system time. Please make sure that device you're using has same time set as your ERPNext server. 
