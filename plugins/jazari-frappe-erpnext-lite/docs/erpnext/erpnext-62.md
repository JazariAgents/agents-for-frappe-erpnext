<!-- Frappe documentation: erpnext, part 62 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__supplier-quotation.md -->
---
title: "Supplier Quotation\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/supplier-quotation"
updated: "2026-02-27"
---


**A Supplier Quotation is document by a potential supplier specifying the cost of goods or services they'll provide within a specified period.**

A Supplier Quotation may also contain terms of sale, terms of payment, and warranties. Acceptance of quotation by the buyer can be considered as an agreement binding on both parties.

[Screenshot on the live page: Buying Flow]

To access Supplier Quotation, go to:
> Home > Buying > Purchasing > Supplier Quotation

## 1. Prerequisites
Before creating and using a Supplier Quotation, it is advised that you create the following first:

* [Supplier](/erpnext/supplier)
* [Item](/erpnext/item)

## 2. How to create a Supplier Quotation

### 2.1 Supplier Quotation from Material Request

You can make a supplier quotation from a Material Request:
[Screenshot on the live page: Supplier Quotation from Material Receipt]

Or:

A Supplier Quotation can be created from a [Supplier master](/erpnext/supplier).

Or:

The supplier can submit you a quotation himself via ERPNext. To know more about this, see section visit the [Request for Quotation page](/erpnext/request-for-quotation#4-creating-a-supplier-quotation-after-rfq).

### 2.2 Creating a Supplier Quotation manually
1. You can also make a Supplier Quotation directly from:

 **Buying > Purchasing > Supplier Quotation > New**.
1. Select the Supplier who sent you the quotation.
1. The Address and Contact will be fetched if you've saved it in the supplier master.
1. Enter the Item code, select the quantity. Rate will be fetched if you've set the Standard Buying rate for the item in [Item Price](/erpnext/item-price).
 [Screenshot on the live page: Supplier Quotation]

If you have multiple Suppliers who supply you with the same Item, you
usually send out a [Request for Quotation](/erpnext/request-for-quotation) to various Suppliers. In
many cases, especially if you have centralized buying, you may want to record all the quotes so that:

 * You can easily compare prices in the future
 * Audit whether all Suppliers were given the opportunity to quote.

Supplier Quotations are not necessary for most small businesses. Always
evaluate the cost of collecting information to the value it really provides!
As a recommendation, you can do this only for high value items.

## 3. Features
### 3.1 Taxes and Charges
If your Supplier is going to charge you additional taxes or charge like a shipping or insurance charge, you can add it here. This will help you accurately track your costs. Also, if some of these charges add to the value of the product you will have to mention them in the Taxes table. You can also use templates for your taxes. For more information on setting up your taxes see the [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template).

### 3.2 More
There are fields for Tax Category, Shipping Rule, Purchase Taxes and Charges Template, Discount, Terms and Conditions, Quotation Number, Printing Settings. You can fill these fields for your record. Visit the [Quotation](/erpnext/quotation) page to know more about these sections. Note that the details like Shipping Rule, taxes, Discount, Terms and Conditions, Quotation Number, etc., are from your supplier and can be recorded for accurate tracking.

Note:

- Tax Category will be fetched from supplier master if set
- Print settings is for making changes to the supplier quotation print
- The Terms and Conditions here are your supplier's
- The Supplier Quotation can be linked to a Material Request using the 'Link to material requests' button

### 3.3 After Submitting
The following records can be created after submitting a Supplier Quotation:

* Purchase Order - A Purchase Order if you agree with the supplier's quotation.
* Quotation - A quotation to your customer.
* Auto Repeat - Auto Repeat the supplier quotation at specified intervals.

### 4. Related Topics
1. [Supplier](/erpnext/supplier)
1. [Supplier Group](/erpnext/supplier-group)
1. [Purchase Order](/erpnext/purchase-order)
1. [Request for Quotation](/erpnext/request-for-quotation)

<!-- page: erpnext/erpnext__supplier-scorecard.md -->
---
title: "Supplier Scorecard\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/supplier-scorecard"
updated: "2026-02-27"
---


**A Supplier Scorecard is an evaluation tool used to assess the performance of suppliers.**

Supplier scorecards can be used to keep track of item quality, delivery, and responsiveness of suppliers across long periods of time. This data is typically used to help in purchasing decisions.
A Supplier Scorecard is manually created for each supplier.

To access Supplier Scorecard, go to:
> Home > Buying > Supplier Scorecard > Supplier Scorecard


## 1. Prerequisites
Before creating and using a Supplier Scorecard, it is advised that you create the following first:

* [Supplier](/erpnext/supplier)

## 1. How to create Supplier Scorecard

1. Go to the Supplier Scorecard list, click on New.
2. Select a Supplier to score.
3. Select the evaluating period whether weekly, monthly, or yearly.
4. Setup the scoring function (details in next section).
5. A supplier scorecard is created for each supplier individually. Only one supplier scorecard can be created for each supplier.
[Screenshot on the live page: Purchase Order]

## 2. Features
### 2.1 Scoring Setup
The supplier scorecard consists of a set evaluation periods, during which the performance of a supplier is evaluated. This period can be weekly, monthly or yearly. The current score is calculated from the score of each evaluation period based on the weighting function. The default formula is linearly weighed over the previous 12 scoring periods.
[Screenshot on the live page: Purchase Order]
This formula is customizable.

#### Supplier Standings

The supplier standing is used to quickly sort suppliers based on their performance. These are customizable for each supplier.

The scorecard standing of a supplier can also be used to restrict suppliers from being included in Request for Quotations or being issued Purchase Orders. The following screen can be seen on expanding a row in the 'Scoring Standings' table, click on the downward facing arrow.
[Screenshot on the live page: Purchase Order]

### 2.2 Criteria Setup
A supplier can be evaluated on several individual evaluation criteria, including (but not limited to) quotation response time, delivered item quality, and delivery timeliness. These criteria are weighed to determine the final period score.

To create a new Criteria, go to Buying > Supplier Scorecard > Supplier Scorecard Criteria:
[Screenshot on the live page: Purchase Order]

Note: Criteria weights for a scorecard should add up to 100.

### 2.3 Supplier Scorecard Variables
The method for calculating each criteria is determined through the Criteria Formula field, which can use a number of pre-established variables. This can be seen in the preceding screenshot.

The value of each of these variables is calculated over the scoring period for each supplier. Examples of such variables include:

 - The total number of items received from the supplier
 - The total number of accepted items from the supplier
 - The total number of rejected items from the supplier
 - The total number of deliveries from the supplier
 - The total amount (in dollars) received from a supplier

[Screenshot on the live page: Supplier Scorecard variable]

Variables are pre-set, additional variables can be added through server-side customizations. Tick the Custom checkbox if the variable you're creating is for a custom field.

The criteria formula should be customized to evaluate the suppliers in each criteria in a way that best fits the company requirements.

### 2.4 Evaluation Formulas
The evaluation formula uses the pre-established or custom variables to evaluate an aspect of supplier performance over the scoring period. Formulas can use the following mathematical functions:

* addition: +
* subtraction: -
* multiplication: *
* division: /
* min: min(x,y)
* max: max(x,y)
* if/else: (x) if (formula) else (y)
* less than: <
* greater than: >
* variables: {variable_name}

It is crucial that the formula be solvable for all variable values. This is most often an issue if the value resolves to 0. For example:
```
{total_accepted_items} / {total_received_items}
```

This example would resolve to 0 / 0 in periods where there are no received items, and therefore should have a check to protect in this case:
```
({total_accepted_items} / {total_received_items})
if {total_received_items} > 0
else 1.
```

### 2.5 Evaluating the Supplier
An evaluation is generated for each Supplier Scorecard Period by clicking the "Generate Missing Scorecard Periods" button. The supplier's current score can be seen, as well as a visual graphic showing the performance of the supplier over time. Any actions against the supplier are also noted here, including warnings when creating RFQs and POs or preventing these features for this supplier altogether.

### 3. Related Topics
1. [Supplier](/erpnext/supplier)
1. [Supplier Quotation](/erpnext/supplier-quotation)

<!-- page: erpnext/erpnext__supplier.md -->
---
title: "Supplier"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/supplier"
updated: "2026-07-02"
---

**Suppliers are companies or individuals who provide you with products or services.**

To access the Supplier list, go to: > Home > Buying > Supplier > Supplier

1. How to create a Supplier

---

1. Go to the Supplier list and click on New.
2. Enter a name for the supplier.
3. Select the supplier group whether Pharmaceutical, Hardware etc.
4. Save. [Screenshot on the live page: Supplier Master]

The options to Warn RFQs, POs, Prevent RFQs, POs will be available once you create a Supplier Scorecard and transactions are made.

1. Features

---

Fields in future transactions will be auto-populated if the 'Default' fields like Default Bank Account, Default Payment Terms Template etc., are set in Supplier.

### 2.1 Tax details

- **Country**: If the supplier is from another country, you can change it here.
- **Tax ID**: Tax identification number of the supplier.
- **Tax Category**: This is linked to Tax Rule. If a Tax Category is set here, when you select this supplier, the respective Purchase Tax and Charges template will be applied. This template is linked to the Tax Rule and the Tax Rule is linked with a Tax Category. Tax Category can be used to group suppliers to whom same tax will be applied. For example: Government, commercial, etc,.
- **Print Language**: The language in which the document will be printed.
- **Tax Withholding Category**: For India, TDS category for the Supplier. On setting a category here, it will be fetched into the Purchase Invoice. For more information, visit the Tax Withholding Category page.
- **Disabled**: Disables the Supplier and they won't be shown in the Supplier List.
- **Is Transporter**: If the supplier is selling your transport services, tick this box. 'GST Transporter ID' field will be visible if this field is ticked.
- **Internal Supplier**: If the supplier is from a sister or parent/child company, tick this field and select the company which they represent.

For India:

- **GST Category**: Select a GST Category of the supplier.
- **PAN**: For India, PAN (Permanent Account Number) card details of the Supplier.

### 2.2 Allow creation of Purchase Invoice without Purchase Order and Purchase Receipt

If the "Purchase Order Required" or "Purchase Receipt Required" option is configured as "Yes" in Buying Settings, it can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Order" or "Allow Purchase Invoice Creation Without Purchase Receipt" in the Supplier Master.

[Screenshot on the live page: Supplier Master]

### 2.3 Currency and Price List

**Billing Currency**: Your supplier's currency can be different from your company currency. If you choose JPY for a supplier, then the currency will be filled as JPY and the exchange rate shown for future purchase transactions.

[Screenshot on the live page: Supplier Currency]

Each Supplier can have a default **Price List** so that every time you buy a new item from this supplier for different prices, the price list associated with the supplier would be updated as well. Under the price list comes item price, you can see the prices in Buying > Items and Pricing > Item Price.

If you select this particular supplier, then the associated Price List will be fetched in Purchase transactions.

### 2.4 **Payment Terms and Block Supplier**

- **Default Payment Terms Template**: If a Payment Terms template is set here, it'll be automatically selected for future purchase transactions.
- **Block Supplier**: You can block invoices, payments or both from a supplier till specific date. Choose 'Hold Type', if you do not select a hold type, ERPNext will set it to "All". When a supplier is blocked, their status will be shown as 'On Hold'.

The hold types are as follows:

```
+ Invoices: ERPNext will not allow Purchase Invoices or Purchase Orders to be created for the supplier
+ Payments: ERPNext will not allow Payment Entries to be created for the Supplier
+ All: ERPNext will apply both hold types aboveIf you do not set a release date, ERPNext will hold the Supplier **indefinitely**.
```

### 2.5 Default Payable Accounts

Add the default account from which invoices against this supplier will be paid. Add additional rows for more companies, you can select only one account per company.

You can **integrate** a supplier with an account. For all Suppliers, "Creditor" account is set as the default payable Account. When Purchase Invoice is created, payable towards the supplier is booked against "Creditors" account.

If you want to customize payable account for the Supplier, you should first add a payable Account in the Chart of Account, and then select that Payable Account in the Supplier master.

[Screenshot on the live page: Supplier Master]

If you don't want to customize payable account, and proceed with default payable account "Creditor", then do not update any value in the Default Supplier Account's table.

> Tip: Default Payable Account is set in the Company master. If you want to set another account as Account as default for payable instead of Creditors Account, go to Company master, and set that account as "Default Payable Account".

Depending on your plan, you can add multiple companies in your ERPNext instance. One Supplier can be used across multiple companies. In this case, you should define Company-wise Payable Account for the Supplier in the "Default Payable Accounts" table, i.e, add multiple rows.

### 2.6 More Information

You can add the supplier's website and any additional details about your supplier in this section. If you freeze a supplier with the 'Is Frozen' option, accounting entries for the supplier will be frozen. In this case the only user whose entries will surpass the 'freeze' is the role assigned in 'Role Allowed to Set Frozen Accounts & Edit Frozen Entries' in Accounting > Settings > Accounts Settings. This is useful when the supplier's name or bank details are being amended.

### 2.7 Address and Contacts

Contacts and Addresses in ERPNext are stored separately so that you can create multiple Contacts and Addresses for one Supplier. Once Supplier is saved, you will find the option to create Contact and Address for that Supplier.

[Screenshot on the live page: Supplier Master]

> Tip: When you select a Supplier in any transaction, Contact for which "Is Primary" field id checked, it will auto-fetch with the Supplier details.

### 2.8 After saving

Once all the necessary details are filled, save the document. On saving, options to create the following will be seen in the Dashboard:

- **Request for Quotation**: An RFQ against this supplier.
- **Supplier Quotation**: Any quotations that the supplier has sent you and you have submitted into the system.
- **Purchase Order**: Purchase Orders you've made against this supplier.
- **Purchase Receipt**: Purchase receipts given by this supplier that you've saved in the system.
- **Purchase Invoice**: Purchase Invoices you've made against this supplier.
- **Payment Entry**: Payment Entries for the Purchase Invoices against this supplier.
- **Pricing Rule**: Any Pricing Rules linked with this supplier. See section *2.2 Currency and Price List* to know how it works.

[Screenshot on the live page: Supplier Save]

By clicking on the View button, you can view the Accounting Ledger or Accounts Payable directly for this supplier.

There's a button to 'Send GST Update Reminder' to the supplier. You need to have a default email account setup first.

1. Video

---

### 4. Related Topics

1. Supplier Quotation
2. Supplier Scorecard
3. Maintaining Supplier's Item Code In the Item Master

---

## Frequently Asked Questions

### 1. How to add multiple supplier address?

You can link multiple addresses (such as billing, shipping, warehouse, or office locations) to a single supplier in ERPNext using the **Address** doctype.

#### Steps

1. Go to **Buying > Supplier** and open the supplier.
2. In the **Addresses and Contacts** section, click **New Address**.
3. Fill in the address details:
  - **Address Title** (for example, *ABC Suppliers – Mumbai Warehouse*)
  - **Address Line 1 & 2**
  - **City**
  - **State** (if applicable)
  - **Country**
4. (Optional) Configure address preferences:
  - Enable **Is Primary Address** if this is the default address.
  - Mark it as the preferred **Billing** or **Shipping** address if required.
5. In the **Links** table, verify:
  - **Link DocType:** `Supplier`
  - **Link Name:** The supplier's name
6. Click **Save**.

Repeat these steps to add as many addresses as needed.

#### Using Supplier Addresses

When creating documents such as a **Purchase Order** or **Purchase Invoice**, you can select the appropriate supplier address from the dropdown. ERPNext automatically uses the selected address for document printing and applies the relevant regional information, such as taxes, where applicable.

<!-- page: erpnext/erpnext__support-issues.md -->
---
title: "Support Issues"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/support-issues"
updated: "2026-03-02"
---

Managing support issues in ERPNext is a structured process which is aimed at addressing user concerns.

While raising a support issue, it is essential to document and categorise based on its severity and impact on business processes. Assigning the appropriate priority level helps in allocating resources efficiently.

- [Issue Type](/erpnext/user/manual/en/issue-type-and-priority)
- [Issue](/erpnext/user/manual/en/issue)

<!-- page: erpnext/erpnext__support-settings.md -->
---
title: "Support Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/support-settings"
updated: "2026-02-28"
---

**All the global settings for support related documents can be found in Support Settings.**

To access Support Settings, go to:


> Home > Support > Settings > Support Settings
> 
> 

[Screenshot on the live page: Support Settings]  


1. Service Level Agreements
---------------------------

### 1.1 Track Service Level Agreement

Enable this feature to start using and tracking [Service Level Agreement](/erpnext/service-level-agreement) in Issues.

### 1.2 Allow Resetting Service Level Agreement

It enables the support team to reset the SLA timers under specific conditions. This can be particularly useful in scenarios where the initial SLA timers need to be adjusted due to changes in the ticket status or additional information being provided by the customer.

2. Issues
---------

### 2.1 Close Issue After Days

Any "Replied" or "Resolved" issue will be closed after the number of days defined in this field. However, if the Customer replies to a closed Issue, the Issue will Open again.

<!-- page: erpnext/erpnext__support_reports.md -->
---
title: "Support Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/support_reports"
updated: "2026-02-27"
---


The various reports in the Support module help understand data on how quickly support staff responded to customer issues, the issue types, issue priorities, timelines, and more.

## 1. First Response Time for Issues

This report provides a date-wise summary of Average First Response Time for Issues reported during the selected time frame. It will display the date and the "Average First Response Time" taken to respond to all the issues created on the respective date.

To access the First Response Time for Issues report, go to:
> Home > Support > Reports > First Response Time for Issues

[Screenshot on the live page: First Response Time for Issues]

## 2. Issue Summary

This report provides a detailed summary of issues reported based on the filters. You can view the summary based on the following parameters:

1. Customer
2. Assigned To
3. Issue Type
4. Issue Priority

For example, if we select the report based on Customer, it will show a list of all the Customers along with the following details for every customer based on the filters applied:

1. Number of Open, Replied, Resolved, and Closed issues.
2. Total Number of Issues raised by that customer.
3. Number of Issues for which the SLA has been fulfilled, failed, and ongoing.
4. Average support metrics like Avg First Response Time, Avg Response Time, Avg Resolution Time, Avg User Resolution Time, Avg Hold Time.

The stacked chart shows the number of issues classified by status for each customer. Report Summary shows the total number of Open, Replied, Resolved, and Closed issues in the entire report.

To access the Issue Summary report, go to:
> Home > Support > Reports > Issue Summary

[Screenshot on the live page: Issue Summary]

## 3. Issue Analytics

This report provides a count of issues according to weekly, monthly, quarterly, and yearly time series based on the following parameters:

1. Customer
2. Assigned To
3. Issue Type
4. Issue Priority

To access the Issue Analytics report, go to:
> Home > Support > Reports > Issue Analytics

[Screenshot on the live page: Issue Analytics]

<!-- page: erpnext/erpnext__system-settings.md -->
---
title: "System Settings | ERPNext Documentation"
description: "Configure ERPNext site-wide localisation, login security, email, file, backup, display, and advanced system behaviour with practical examples."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/system-settings"
updated: "2026-08-15"
---

Nova Industries is a fictional company that manufactures and distributes electronics. It has just hired 25 employees across sales, warehouse, manufacturing, and finance. One employee reads 08-09-2026 as 8 September, another reads it as 9 August, shared login sessions stay open longer than intended, and customer emails use inconsistent footers. These are not transaction-level problems. They are rules for the whole ERPNext site.



System Settings gives the System Manager one place to define those shared rules. A careful setup makes dates and numbers predictable, limits risky login behaviour, controls files and emails, and establishes operational limits. A careless change can lock users out, weaken security, or change how information is displayed across the site, so record the current value and test sensitive changes with a non-administrator account.

## Before you change System Settings

Use an account with System Manager access. Confirm the intended country, time zone, language, security policy, file policy, and backup policy with the responsible teams. Some settings affect the next login or newly loaded page, so save, reload, and test in a separate user session.

## General and localisation settings

[Screenshot on the live page: General localisation and language fields in ERPNext System Settings]


| Setting                  | What it means                                   | Nova example                                                                                                         |
| ------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Application Name         | Name displayed for the site where supported     | Nova labels the internal site ERPNext rather than changing the legal Company name.                                   |
| Country                  | Site-level localisation context                 | United States is used for the documentation site. Company and transaction tax setup remains separate.                |
| Language                 | Default interface language                      | English is the default, while individual users may select another language.                                          |
| Time Zone                | Time used for timestamps and scheduled activity | Choose the site’s operating time zone before transactions begin. Users can have personal time zones where supported. |
| Currency                 | General site currency context                   | USD is used for display defaults; Company and transaction currencies remain authoritative.                           |
| Enable Onboarding        | Shows setup guidance to new users               | Enable during implementation, then hide it when the team no longer needs the checklist.                              |
| Setup Complete           | Records that initial setup has finished         | Leave this managed by the setup process rather than using it as a daily control.                                     |
| Disable Document Sharing | Removes ad hoc document sharing                 | Nova disables sharing only when access must be governed entirely through roles and permissions.                      |


## Date, time, number, and rounding settings


| Setting                            | What it means                                   | Nova example                                                                                 |
| ---------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Date Format                        | How dates are displayed                         | mm-dd-yyyy shows August 9 as 08-09-2026.                                                     |
| Time Format                        | Whether seconds are displayed                   | HH:mm is simpler for most users; HH:mm:ss helps operational logs.                            |
| Number Format                      | Digit grouping and decimal symbols              | #,###.## displays 1234.5 as 1,234.5.                                                         |
| Use Number Format from Currency    | Uses the linked Currency format where available | Useful when users regularly work with currencies that use different separators.              |
| First Day of the Week              | Starting day for calendars                      | Monday suits Nova’s operational reporting week.                                              |
| Float Precision                    | Decimal places for non-currency values          | Three places show a quantity such as 1.275.                                                  |
| Currency Precision                 | Decimal places for monetary values              | Two places show USD cents; use more only when the business genuinely prices below one cent.  |
| Rounding Method                    | How midpoint values are rounded                 | Finance chooses Banker's or Commercial Rounding according to policy and verifies tax totals. |
| Show Absolute Datetime in Timeline | Shows exact timestamps instead of relative time | An auditor can see the precise date and time rather than “two days ago.”                     |


## Permissions and external links


| Setting                       | What it means                                                            | Nova example                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Apply Strict User Permissions | Applies User Permission restrictions more strictly across linked records | A regional sales user sees only allowed Companies and related records. Test reports and link fields before enabling. |
| Show External Link Warning    | Warns before opening links outside ERPNext                               | Set to Ask when users frequently follow supplier or payment links.                                                   |


## Sessions, login methods, and brute-force protection

[Screenshot on the live page: Session expiry and document-share controls in ERPNext System Settings]


| Setting                         | What it means                                               | Nova example                                                                                                                |
| ------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Session Expiry                  | Idle time before a login expires                            | 08:00 closes a session after eight idle hours. Very long values increase exposure on unattended devices.                    |
| Document Share Key Expiry       | Days before a public share key expires                      | A 7-day quotation review link should not remain valid indefinitely.                                                         |
| Allow only one session per user | Prevents one account from staying active on several devices | Useful for tightly controlled operational accounts, but inconvenient for users switching between office and mobile devices. |
| Disable Username/Password Login | Requires another configured login method                    | Configure and test SSO first. Otherwise users may be locked out.                                                            |
| Max signups allowed per hour    | Limits public account creation                              | A portal can accept genuine registrations without allowing unlimited automated signups.                                     |
| Allow Login using Mobile Number | Accepts a unique mobile number as login                     | Enable only when user mobile numbers are complete and unique.                                                               |
| Allow Login using User Name     | Accepts the configured username                             | Useful when company policy avoids email addresses as the typed login identifier.                                            |
| Login with email link           | Sends a temporary sign-in link                              | Useful for occasional portal users who do not remember a password.                                                          |
| Email-link expiry               | Minutes before that link becomes invalid                    | Ten minutes limits the time an intercepted email link can be used.                                                          |
| Email-link rate limit           | Limits repeated requests                                    | Prevents a user or bot from generating excessive sign-in emails.                                                            |
| Consecutive Login Attempts      | Failed attempts allowed before delay                        | Ten attempts provides a controlled retry window.                                                                            |
| Allow Login After Fail          | Delay before another attempt                                | A 60-second delay slows automated guessing.                                                                                 |


[Screenshot on the live page: Two-factor authentication controls in ERPNext System Settings]

Two-factor settings enable OTP App, SMS, or Email verification. The bypass options change how restricted IP addresses interact with two-factor authentication, so test them with the exact network policy. QR-code expiry limits setup-page lifetime, while OTP Issuer Name is the label users see in the authenticator app. SMS also requires a working SMS configuration and template.

## Password settings

[Screenshot on the live page: Password policy controls in ERPNext System Settings]

Logout All Sessions on Password Reset removes existing sessions after a reset. Force User to Reset Password sets the age after which a reset is required. Reset-link expiry and generation limit reduce the useful life and volume of reset links. Enable Password Policy and Minimum Password Score require stronger passwords. Nova tests these rules with a normal user before enforcing them company-wide.

## Email settings

[Screenshot on the live page: Email footer and delivery controls in ERPNext System Settings]

Email Footer Address supplies the organisation address. Email Retry Limit controls retries after delivery failure. The footer controls determine whether the standard footer, auto-email-report footer, and web-view link appear. Store Attached PDF Document keeps the generated attachment as a File. Welcome and reset-password templates allow approved messages instead of generic text.

## File settings

[Screenshot on the live page: File upload controls in ERPNext System Settings]

Max File Size limits each upload. Guest uploads should be enabled only with an explicit list of allowed DocTypes. Web Capture can prefer a camera on supported devices. EXIF removal strips embedded image metadata, while the public-file restriction limits who may publish files. Allowed File Extensions provides an allow-list, and background export retention removes generated report files after the configured hours.

## Display, backups, and advanced settings

[Screenshot on the live page: Backup retention and encryption controls in ERPNext System Settings]

Display settings can suppress update notices, change-log notices, empty read-only fields, and product suggestions. Number of Backups controls retention; Encrypt Backups protects backup contents but requires secure key handling and a tested restore process.



Advanced controls limit auto-email reports and report rows, enable scheduled report snapshots, configure scheduler behaviour for inactive sites, and control error traceback and telemetry. Link-field result limits and API logging affect performance or storage. Change them only for a measured operational reason and monitor the result.

## Troubleshooting

### Users cannot log in after a security change

Test the alternative login method, restore username and password login if needed, and confirm two-factor delivery. Keep an administrator recovery path before enabling restrictive settings.

### Dates or numbers still appear differently

Reload the page and check the user language, Currency number format, field precision, browser locale, and the relevant report formatting.

### A file upload is rejected

Compare the file size and extension with System Settings. For guest uploads, also verify that the target DocType is explicitly allowed.

### Scheduled work is not running

Confirm Enable Scheduled Jobs, inspect background workers, and check whether the site is treated as inactive under the dormant-days setting.

## Frequently asked questions

### Do System Settings override every Company setting?

System Settings controls site-wide behaviour and presentation. Company, module, user, and transaction settings can still supply more specific business values.

### Can the site time zone be changed later?

Treat the site time zone as an implementation decision. Changing timestamp interpretation after live data exists can be disruptive and should be tested and planned.

### Should backup encryption be enabled immediately?

Enable it only when the encryption key is stored safely and a restore has been tested. An encrypted backup without its key cannot serve as a recovery copy.

### Does hiding update notifications stop updates?

The setting changes the notification display. It does not install, postpone, or manage the software update itself.

## Related topics

- [Global Defaults](/erpnext/global-defaults)
- [Session Defaults](/erpnext/session-defaults)
- [Set Language](/erpnext/set-language)
- [Set Precision](/erpnext/set-precision)
- [User Permissions](/erpnext/user-permissions)
- [Two Factor Authentication](/erpnext/two-factor-authentication)
- [File Manager](/erpnext/file-manager)

<!-- page: erpnext/erpnext__table-multiselect-field.md -->
---
title: "Table MultiSelect Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/table-multiselect-field"
updated: "2026-03-04"
---

The Table MultiSelect field is very similar to Link Field. The key difference is that Table MultiSelect field allows you to select multiple values.

Let us consider an example to understand the same. Let's say you want to assign a ToDo to multiple users, as shown below:

[Screenshot on the live page: Screenshot 2024-06-25 at 4.58.41 PM]  


You can add a Table MultiSelect Field by using the following steps:

Step 1: Create a child DocType.
-------------------------------

Create a new DocType, enable 'Is Child Table' and 'Editable Grid' check-boxes and add a field with 'Link' type as shown below.

Set the link field as mandatory. Ensure that the field within the child table has "In List View" ticked.

[Screenshot on the live page: Screenshot 2024-06-25 at 4.55.49 PM]  


Step 2: Add a field with type 'Table MultiSelect'.
--------------------------------------------------

Create a field with type 'Table MultiSelect' and add the DocType created in first step in 'options'.

[Screenshot on the live page: Screenshot 2024-06-25 at 4.57.08 PM]  


You can remove any selected value by clicking on the cross sign next to selected value or by placing the cursor next to the value and pressing Backspace.

This field allows one value to be selected only once.

> Note: Table MultiSelect fields cannot be added in child DocTypes.

<!-- page: erpnext/erpnext__tasks.md -->
---
title: "Tasks\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/tasks"
updated: "2026-03-02"
---

**In project management, a task is an actionable unit or activity which needs to be completed.**

[Screenshot on the live page]

To access Tasks, go to,

> Home > Projects > Task

## How to Create a Task

1. Go to the Task List and click on New.
2. Add the subject of the task.
3. Save.
  [Screenshot on the live page]

Alternatively, a task can also be created from a Project in the following way:

1. Go to the Project for which you want to create a new task.
2. Go to Task under the Project section on the Dashboard. The plus icon '+' here would direct you to the task creation page.
3. Add the subject of the task.
4. Save.

### Additional Options while creating a Task

The following additional details can be added when editing a new task:

- **Status**: You can add the status of the Project or change the same whenever needed, e.g., from 'Open' to 'Working', 'Overdue','Pending Review','Completed', or 'Cancelled'
- **Project**: In case a task is added independently, you may choose to link the task to a particular Project. If the task is created from a Project, the details of the Project will get automatically added.
- **Priority**: You can choose to define the priority of the task, viz., Low, Medium, High or Urgent.
- **Issue**: If the task is an actionable that arises out of an Issue, that issue can be tagged here with the Task.
- **Weight**: If a particular task carries some weightage out of a project, or otherwise, the weightage can be specified here. This weightage gets calculated in the Percentage Task Completion Method by Task Weight.
- **Type**: If your task can be defined under a particular Task Type, say, User Training or User Demo, you can enter the Task Type here. It can be used to filter the Tasks based on Task Types.
- **Color**: Each task can be recognized by a different color. This helps in identifying a task while creating Gantt Charts.
- **Is Group**: This box can be checked to indicate that a task is a parent task, and can be further divided into multiple sub-tasks.
- **Is Template**: This box can be checked to indicate that this task is a template task, and is meant to be used in a Project Template.
- **Parent Task**: If a particular task is a part of a group task, the parent task can be linked to the task from this field.

## Task Configurations

### Timeline and Details

- **Expected Start Date**: You can enter the date on which you expect the Task to be started.
- **Expected End Date**: You can enter the date on which you expect this Task to be finished.
- **Expected Time**: You can enter the number of hours which you expect are going to be spent on this task.
- **Progress**: You can enter the Progress Percentage of a Task.
- **Begin**: If the task is a template task, this field can be used to specify the day on which this task should begin after the project is commenced.
- **Duration**: If the task is a template task, this field can be used to assign a specific number of days to this task.
- **Is Milestone**: This box can be checked in the cases where a particular task is a Milestone in a Project.
- **Description**: You can add a description of the task here.

> **Note**: Based on the values of **Begin** and **Duration** field, the **Expected Start Date** and **Expected End Date** gets calculated for Project Tasks created using Project Template. This calculation skips holidays based on the holiday list of your company.

[Screenshot on the live page]

### Dependencies and Actual Time Tracking

- **Dependent Tasks**: Dependent tasks indicate that a particular task is dependent on another task, and the former cannot be completed before the completion of the latter.

 Task dependencies can be viewed in the Gantt Charts in the following way.

[Screenshot on the live page]

- **Actual Start Date**: The actual date and time on which the Task is started get recorded basis the Timesheets.
- **Actual End Date**: The actual date and time on which the task was finished get recorded here via the Timesheets.

[Screenshot on the live page]

### Task costing and Billing

- **Total Costing Amount**: The Total Costing Amount gets captured here via the Timesheets submitted by the user while working on this task.
- **Total Billing Amount**: The Total Amount with which the Customer is to be billed via this task gets recorded here form the Timesheets.
- **Total Expense Claim**: The Total Amount of Expense claimed by an Employee for the completion of this Task gets recorded and reflected here.

### More Info

- **Department**: You can enter the Owner Department for the task. Irrespective of the Owner department of the Project, each task can be carried out by a different department.
- **Company**: You can change the Company for which this Task is being carried out. This can be used in cases:
  - One company executes Tasks for its Parent, Subsidiary, or Sister Company
  - Projects span across multiple legal entities

[Screenshot on the live page]

## Related Topics

1. [Project](/erpnext/project)
2. [Timesheet](/erpnext/timesheets)
