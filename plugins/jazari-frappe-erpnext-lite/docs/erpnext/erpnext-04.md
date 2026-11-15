<!-- Frappe documentation: erpnext, part 4 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__add-remove-fields-from-print-format.md -->
---
title: "Add/Remove Fields from Print Format"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/add-remove-fields-from-print-format"
updated: "2026-03-02"
---

To explain, let's consider Purchase Order which has the following fields in the Print Format, and here, I want to add 'Supplier's Contact Name' under Supplier Name and remove the 'Weight Per Unit' column from the Item's table.
 

[Screenshot on the live page]

**Step 1:** Navigate to the Print View of the document you want to change the Print Format of -> Menu (...) -> Customize

[Screenshot on the live page]

**Step 2:** Search for the field by name and add it to the desired location

[Screenshot on the live page]

_Follow the same drag and drop method to remove the fields as well._

 

**Step 3:** To add/remove the fields from the child table of the document: Locate the table -> Select Columns -> Check/Uncheck as you wish.

[Screenshot on the live page]

 

**The result:**

[Screenshot on the live page]

<!-- page: erpnext/erpnext__adding-attachments-to-outgoing-messages.md -->
---
title: "Adding Attachments to Outgoing Messages\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/adding-attachments-to-outgoing-messages"
updated: "2026-03-04"
---


**You can add attachments to outgoing emails on-the-go in ERPNext.**

If you have certain files attached to your document and wish to attach the same to the outgoing email, you can do so by simply picking it from the attachments list.

[Screenshot on the live page: Attachments in Outgoing Messages]

<!-- page: erpnext/erpnext__adding-margin.md -->
---
title: "Add Margin to Quotations and Sales Orders | ERPNext Documentation"
description: "Add percentage or fixed margins to ERPNext quotation and sales order items manually or through Pricing Rules, with calculation examples."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/adding-margin"
updated: "2026-07-25"
---

Margin increases an item's transaction Rate above its Price List Rate. ERPNext can apply a percentage or fixed amount directly on a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order) item, or apply it automatically through a [Pricing Rule](/erpnext/pricing-rule).

## Before you begin

Create:

- The required [Item](/erpnext/item).
- A selling [Price List](/erpnext/price-lists).
- An [Item Price](/erpnext/item-price) that supplies the Price List Rate.

Margin needs a reference Price List Rate. If no rate is fetched, verify the Item Price before troubleshooting the margin calculation.

## Add margin directly to an item

1. Create a Quotation or Sales Order.
2. Select the Customer, Price List, and Item.
3. Select the highlighted pencil icon to open the complete item-row editor.
4. Set **Margin Type** to **Percentage** or **Amount**.
5. Enter **Margin Rate or Amount**.
6. Review the calculated Rate and Amount.
7. Save.

[Screenshot on the live page: A Sales Order item row with its pencil icon highlighted.]

[Screenshot on the live page: The item row editor with Margin Type and Margin Rate or Amount highlighted.]

## Margin calculation

For a fixed margin:

`Rate = Price List Rate + Margin Amount`

For a percentage margin:

`Rate = Price List Rate + (Price List Rate × Margin Percentage ÷ 100)`

Example:


| Value           | Amount |
| --------------- | ------ |
| Price List Rate | $1,000 |
| Margin          | 15%    |
| Margin amount   | $150   |
| Resulting Rate  | $1,150 |


Any item discount is evaluated separately. Review Price List Rate, Margin, Discount, Rate, and Net Rate together when both are used.

## Apply margin automatically with a Pricing Rule

Use a Pricing Rule when the same margin should apply under repeatable conditions.

1. Create or open a Pricing Rule.
2. Configure its applicability, such as Item, Item Group, Customer, Customer Group, quantity, amount, and validity.
3. In the **Margin** section, select Percentage or Amount.
4. Enter the Margin Rate or Amount.
5. Save and enable the rule.
6. Test it on a new Quotation or Sales Order.

[Screenshot on the live page: A Pricing Rule with its Margin settings highlighted.]

When several rules can match, review their priorities and conditions. A more specific rule may need a higher priority than a general Item Group rule.

## Margin and discounts

Margin and discount solve different pricing needs:

- Margin adds a markup to the Price List Rate.
- [Applying a Discount](/erpnext/applying-discount) reduces a price or total.
- A fixed Pricing Rule Rate can replace the fetched rate.

Avoid combining them without a documented pricing policy. Users should be able to explain how the final Rate was reached.

## Downstream transactions

When a Sales Order is created from a Quotation, or a [Sales Invoice](/erpnext/sales-invoice) is created later in the cycle, verify the mapped Rate. [Selling Settings](/erpnext/selling-settings) can warn or stop users when the rate changes through the sales cycle.

## Troubleshooting


| Problem                             | What to check                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| Margin fields do not affect Rate    | Confirm that a Price List Rate was fetched                                     |
| Margin is not applied automatically | Verify the Pricing Rule is enabled, valid, and matches the transaction         |
| A different rule wins               | Review rule priority, Item or party specificity, and overlapping conditions    |
| The downstream rate changes         | Review mapped values and the Maintain Same Rate setting                        |
| Final profitability is unclear      | Margin is based on Price List Rate, not necessarily valuation or purchase cost |


## Frequently asked questions

### Is margin calculated from valuation rate?

No. The item margin fields use Price List Rate as their pricing reference.

### Can I add a fixed dollar margin?

Yes. Select Amount as the Margin Type.

### Can margin apply to Sales Invoices?

Margin fields are primarily entered on Quotation and Sales Order items. Downstream documents can carry the resulting rate.

### How do I enforce a minimum selling price?

Review the selling-price validation in Selling Settings and test it against your purchase or valuation rates.

## Related topics

- [Price Lists](/erpnext/price-lists)
- [Item Price](/erpnext/item-price)
- [Pricing Rule](/erpnext/pricing-rule)
- [Applying a Discount](/erpnext/applying-discount)
- [Change the Rate of Items in the Sales Cycle](/erpnext/change-the-rate-of-items-in-the-sales-cycle)

<!-- page: erpnext/erpnext__adding-reference-to-journal-entry.md -->
---
title: "Add a Reference to a Journal Entry | ERPNext Documentation"
description: "Learn how to add invoice and document references to Journal Entry rows in ERPNext, allocate receivables or payables, and verify outstanding balances safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/adding-reference-to-journal-entry"
updated: "2026-08-03"
---

A reference connects one accounting row in a [Journal Entry](https://docs.frappe.io/erpnext/journal-entry) to the ERPNext document that explains the amount. On a receivable or payable row, the reference can also allocate the debit or credit against a specific invoice and update its outstanding balance when the Journal Entry is submitted.

Add a reference only when the Journal Entry genuinely settles, adjusts, transfers, or reverses an amount related to that document. A reference is not a general-purpose note. Use **User Remark** and attachments for supporting context that should not affect invoice allocation.

## Before you begin

Confirm the following:

1. The referenced document belongs to the same company and is eligible for the intended adjustment.
2. The account, party, debit or credit direction, and amount are correct.
3. A dedicated document such as a [Payment Entry](https://docs.frappe.io/erpnext/payment-entry), return, [Credit Note](https://docs.frappe.io/erpnext/credit-note), or [Debit Note](https://docs.frappe.io/erpnext/debit-note) is not more appropriate.
4. The invoice has enough outstanding amount for the allocation.
5. You have accounting approval and supporting evidence for a write-off or manual adjustment.

The example below writes off $221 from Northstar Retail's submitted Sales Invoice `ACC-SINV-2026-00009` using a draft Journal Entry.



[Screenshot on the live page: Outstanding amount on the Sales Invoice used as the Journal Entry reference]

## Add the reference

Create or open the Journal Entry. Add the balanced accounting rows and enter the approved debit or credit amounts.

For an invoice-related adjustment, use the receivable or payable account on the party row. Select the pencil icon to open the full child-row editor.



[Screenshot on the live page: Pencil icon for opening the Journal Entry accounting row]

Set **Party Type** to **Customer** or **Supplier**, then select the corresponding party. ERPNext uses these fields with the receivable or payable account to update the correct party ledger.



[Screenshot on the live page: Party Type and Party on the Journal Entry accounting row]

In the **Reference** section:

1. Set **Reference Type** to the document type, such as **Sales Invoice**.
2. Set **Reference Name** to the exact document, such as `ACC-SINV-2026-00009`.
3. Review the reference due date when ERPNext fetches it.
4. Confirm that the row amount is the amount you intend to allocate.

[Screenshot on the live page: Reference Type and Reference Name on a Journal Entry accounting row]

Collapse the row and verify that total debit equals total credit. Save the draft, review all accounts and references, then submit.

## What the reference changes

The effect depends on the referenced document and the accounting row.

For a Sales Invoice write-off:


| Account                                  | Debit | Credit | Reference effect                                                                 |
| ---------------------------------------- | -----: | ------: | -------------------------------------------------------------------------------- |
| Approved write-off expense               | $221  |        | Records the loss or adjustment.                                                  |
| Accounts Receivable for Northstar Retail |       | $221   | Allocates $221 to the selected Sales Invoice and reduces its outstanding amount. |


For a supplier adjustment, the payable row and debit or credit direction depend on the business event. Do not reverse the signs merely to make the voucher submit. Confirm the intended ledger effect with your accountant.

After submission, open the referenced invoice and confirm its outstanding amount. You can also use **View &gt; Ledger**, the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), and the [Accounts Receivable or Payable report](https://docs.frappe.io/erpnext/accounts-receivable-and-payable) to verify the allocation.

## Documents that can be referenced

Current ERPNext provides these Reference Type options on a Journal Entry accounting row:


| Group                        | Reference types                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sales and purchases          | [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice), [Purchase Invoice](https://docs.frappe.io/erpnext/purchase-invoice), [Sales Order](https://docs.frappe.io/erpnext/sales-order), Purchase Order |
| Accounting and payments      | Journal Entry, Payment Entry, Bank Transaction, Exchange Rate Revaluation, Invoice Discounting                                                                                                                |
| Expenses and payroll         | Expense Claim, Payroll Entry, Employee Advance, Full and Final Statement                                                                                                                                      |
| Assets, loans, and education | Asset, Loan, Fees                                                                                                                                                                                             |


The presence of an option does not mean every combination is valid. ERPNext filters Reference Name choices and validates the account, party, company, status, and amount according to the selected document.

Orders can be referenced for traceability, but they do not have an invoice outstanding balance to settle. Use an invoice reference when the Journal Entry must update receivables or payables.

## Important fields and what they mean


| Field              | Meaning                                                         | Guidance                                                              |
| ------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------- |
| Account            | Ledger account affected by the row                              | Use the correct receivable or payable account for invoice allocation. |
| Party Type         | Type of counterparty                                            | Required for customer or supplier ledger allocation.                  |
| Party              | Specific Customer, Supplier, Employee, or other supported party | Must match the referenced transaction where applicable.               |
| Reference Type     | DocType connected to the row                                    | Select the business document that explains the adjustment.            |
| Reference Name     | Specific document connected to the row                          | Select the exact submitted transaction.                               |
| Reference Due Date | Due date fetched from the reference                             | Useful for receivable and payable ageing.                             |
| Debit or Credit    | Amount posted and allocated by the row                          | Direction must match the intended accounting effect.                  |


## Troubleshooting

### Reference Name is empty

Set Reference Type first. Confirm that the source document is submitted, belongs to the same company, matches the selected party, and is available for that account and adjustment.

### ERPNext says the reference has no outstanding amount

The invoice may already be fully paid, written off, returned, or allocated. Open the invoice and inspect its outstanding amount and payment references before adding another adjustment.

### The Journal Entry submits but the invoice outstanding amount is unchanged

Confirm that the receivable or payable row contains the correct Party Type, Party, Reference Type, and Reference Name. A reference on an unrelated expense, income, bank, or cash row does not allocate the party invoice.

### The allocated amount is more than the outstanding amount

Reduce the Journal Entry row to the intended outstanding amount or investigate prior allocations. Do not over-allocate merely to absorb a difference.

### The wrong invoice was referenced

If the Journal Entry is still a draft, correct the row. If it is submitted, follow the controlled cancellation and amendment process, considering the [immutable ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext) and closed-period restrictions.

## FAQs

### Is a reference required on every Journal Entry row?

No, Use it when the row relates to a supported ERPNext document. Ordinary accruals, transfers, and opening adjustments may not require a document reference.

### Should I use a Journal Entry to record normal customer payments?

Prefer Payment Entry. It is designed for bank or cash movement, invoice allocation, advances, currencies, and reconciliation. Use a Journal Entry for an approved accounting adjustment that is not better handled by a dedicated transaction.

### Can one Journal Entry reference several invoices?

Yes, Add separate accounting rows with the appropriate party, invoice reference, and allocation amount. Keep the voucher balanced and verify every invoice afterward.

### Can I reference a Sales Order or Purchase Order?

Yes, for traceability where supported. Orders are commitments, so referencing one does not settle an invoice outstanding balance.

### Does saving a draft change the invoice balance?

No, The allocation affects accounting and outstanding balances when the Journal Entry is submitted.

## Related topics

- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [Payment Entry](https://docs.frappe.io/erpnext/payment-entry)
- [Accounting for Bad Debts](https://docs.frappe.io/erpnext/accounting-for-bad-debts)
- [Payment Reconciliation](https://docs.frappe.io/erpnext/payment-reconciliation)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Immutable Ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext)

<!-- page: erpnext/erpnext__adding-users.md -->
---
title: "Adding Users"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/adding-users"
updated: "2026-03-29"
---

User management in ERPNext includes creating and managing user accounts, defining roles, and assigning these roles to users based on their responsibilities. Administrators can configure detailed permissions for each role by specifying the level of access to modules within the system.



Users can be added by the System Manager. To add users go to: > Home > Users and Permissions > User

There are two main types of users:

**Website users**: Customers, Suppliers, Students, etc., who have access only to the portal and not to any modules. **System Users**: People using ERPNext in the Company with access to modules, company data, etc.

Read more about [difference between system and website user](/erpnext/difference-between-system-user-and-website-user).

Under User, a lot of info can be entered. For the sake of usability, the information entered for web users is minimal: First Name and Email.

An Email address is the unique key (ID) identifying the Users.

### 1. Creating New User

1. Go to the User list, click on New.
2. Add an Email address and name of the user.
3. Save.

[Screenshot on the live page]
*Details like Username and Language can also be changed.*



### 2. Features

### 2.1 Setting Roles

After saving, you will see a list of roles and checkboxes next to them. Just check the roles you want the user to have and save the document. The roles have pre-defined permissions, to know more about roles, [click here](/erpnext/role-based-permissions). You can set [Role profiles](/erpnext/role-and-role-profile) to use as a template which selects multiple roles together.

[Screenshot on the live page]



### 2.2 More Information

More information about the employee can be set from this section:

- Gender
- Phone
- Mobile No
- Birth Date
- Location
- Interests
- Bio

Ticking on 'Mute Sounds' will mute sounds that play on interacting with documents. The user may need to do a Settings > Reload for the changes to take place.

### 2.3 Change Password

- **Set New Password**: As a System Manager, you can set a new password for the user if it needs to be changed.
- **Send Password Update Notification**: Send an email notification to the user that their password has been changed.
- **Log out from all devices while changing Password**: When changing the user's password, this logs out the user from PC and any mobile device they may have logged into.

### 2.4 Document Follow

With this option you can follow various documents in the system and get email notifications when they are updated. Know more [here](/erpnext/document-follow).

### 2.5 Email Settings

- **Send Notifications for Email threads**: The user will get notifications for Email conversations that take place in document types like Opportunities.
- **Send Me A Copy of Outgoing Emails**: Sends the user a copy of the emails they send. This is useful for keeping track if the email got sent.
- **Allowed In Mentions**: Allow this user's name to appear in thread conversations so that they can be mentioned using '@'.
- **Email Signature**: Adding an email signature here will set it as default for all outgoing emails for the user. This is different from a footer which is set from the [Company master](/erpnext/company-setup).

### 2.6 Email Inbox

Subscribe the user to different mailing lists of your company from this section. Add a new row and select the mailing list to assign this user. For example, mailing lists can be jobs, support, sales, etc. To know more about Email Inbox, [click here](/erpnext/email-inbox).

### 2.7 Allow Module Access

Users will have access to all modules for which they have role-based access. If you want to restrict access of certain modules for this user, un-check the modules from this list.

[Screenshot on the live page]



#### 2.7.1 Module Profiles

Role Profiles act as a template to store and select access to multiple modules. This Role Profile can then be assigned to a User. For example, HR Users will have access to multiple modules like HR, Payroll, etc. Role Profiles are useful to provide access to multiple modules at once when adding multiple users.

[Screenshot on the live page]



### 2.8 Security Settings

- **Simultaneous Sessions**: Simultaneous login sessions the user is allowed. You can use the same set of credentials for multiple users by allowing more sessions. This can be restricted from [System Settings](/erpnext/system-settings#15-security) globally. For cloud account, the total number of simultaneous sessions cannot exceed the total number of subscribed users.
- **User Type**: If the user has any role checked other than Customer, Supplier, Patient, or Student they automatically become a System User. This field is read-only.
- **Login After, Login Before**: If you wish to give the user access to the system only between office hours, or during weekends, specify it here. For example, if office hours are from 10 am to 6 pm, set the Login After, Login Before hours as 10:00 and 18:00.
- **Restrict IP**: Restrict user login to the IPs specified here. This can be used so that the user can log in only from office computers. Multiple IPs can be added separated by commas.

This section also shows other details like Last Login, Last IP, and Last Active time for the user.

### 2.9 Third Party Authentication

This will allow users to use Facebook, Google, or GitHub to log in. To use this feature, signup for a developer account with Facebook, Google, GitHub, etc. Create an app on their console, specify an app name, the originating URL and callback URL, copy the client ID and client secret info here to start using.

For more details, go to [this page](/framework/user/en/guides/deployment/how-to-enable-social-logins).

### 2.10 API Access

You can generate API Secret keys from this section using the Generate Keys button. This can be used to access your account's data from another application, for example, an offline POS system.

### 2.11 After saving

After saving a user, these buttons will be seen on the dashboard area of the User master.

[Screenshot on the live page]

#### Permissions

- **Set User Permissions**: Will take you to the [User Permissions](/erpnext/user-permissions) page of Bruce from where you can restrict Bruce's access to documents.
- **View Permitted Documents**: Will take you to the 'Permitted Documents For User' report for this user. Here you can see which documents does Bruce have access to. For example, on selected Sales Order, the list of Sales Orders Bruce has access to will be displayed.

#### Password

- **Reset Password**: An email with instructions to reset the user's password will be sent to the user's [Email Account](/erpnext/email-account).
- **Reset OTP Secret**: Reset OTP Secret for logging in via Two Factor Authentication.

Create User Email will let you create an [Email Account](/erpnext/email-account) for the user based on the email entered in the User master.

#### Impersonate

> New in version 15.

Sometimes to understand a specific problem a user is facing, you might have to log in as that user. Administrator user can impersonate as any other user using the "Impersonate" button on the user document. 

Note:

- An activity log will be created whenever Administrators use "Impersonate" feature.
- Any document change where track changes are enabled will also indicate original user who impersonated someone else while modifying the document.
- The user you're impersonating will be notified.

### 3. Login Methods

In System Settings, under the Security section, if you check the 'Allow Login using Mobile No' checkbox, a mobile number can also be used to log in. While a Mobile No will be unique, it will not be treated as a user ID.

Login with Email:

[Screenshot on the live page: Email Login]



Login with Email or Mobile:

[Screenshot on the live page: Mobile No Login]



After adding these details, save the user.

### 4. Related Topics

1. [Role Based Permissions](/erpnext/role-based-permissions)
2. [User Permissions](/erpnext/user-permissions)
3. [Document Follow](/erpnext/document-follow)

<!-- page: erpnext/erpnext__address-template.md -->
---
title: "Address Template | ERPNext Documentation"
description: "Learn how ERPNext Address Templates use country-specific Jinja and HTML to format addresses, configure a default fallback, and verify printed results."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/address-template"
updated: "2026-07-23"
---

An **Address Template** controls how ERPNext formats an [Address](/erpnext/address) when it appears on transactions, print formats, previews, and communications. Country-specific templates let each region use the expected order, labels, and optional fields.

ERPNext selects a template from the Address's Country. If no country-specific template exists, it uses the template marked as default.

[Screenshot on the live page: United States Address Template editor with Jinja fields and default status.]

## Before you begin

You need:

- System Manager or equivalent permission;
- the Country for which the format applies;
- a sample Address containing all relevant fields;
- basic HTML and [Jinja template](https://jinja.palletsprojects.com/en/stable/templates/) knowledge; and
- a test transaction or print format on which to verify the result.

Copy the existing template text before making a substantial change. A syntax error can affect every document that renders an Address for that country.

## Create an Address Template

1. Open **CRM > Address Template**.
2. Select **Add Address Template**.
3. Choose the **Country**.
4. Enter the Jinja and HTML template.
5. Enable **Is Default** only when this should be the fallback for countries without a specific template.
6. Save the Address Template.

Normally, create one template per Country. Keep only one appropriate default fallback.

## Edit an existing template

1. Open the template for the required Country.
2. Copy the current template for rollback.
3. Make the smallest required change.
4. Save.
5. Open a representative Customer or Supplier Address and verify the rendered result.
6. Test at least one [Quotation](/erpnext/quotation), [Sales Invoice](/erpnext/sales-invoice), or relevant print preview.

[Screenshot on the live page: Formatted billing and shipping Addresses shown on a Customer.]

Do not treat a successful save as proof that the output is correct. Verify line breaks, missing values, labels, punctuation, and narrow print layouts.

## Important fields and concepts


| Field or concept | What it controls                                                         |
| ---------------- | ------------------------------------------------------------------------ |
| **Country**      | Determines which Addresses use this template                             |
| **Is Default**   | Makes the template the fallback when no country-specific template exists |
| **Template**     | Jinja and HTML used to render the formatted Address                      |
| `address_line1`  | First street or building line                                            |
| `address_line2`  | Optional second address line                                             |
| `city`           | City or town                                                             |
| `county`         | County or equivalent regional division                                   |
| `state`          | State, province, or region                                               |
| `pincode`        | Postal, ZIP, or PIN code                                                 |
| `country`        | Country name                                                             |
| Contact fields   | Optional phone, fax, and email values available to the template          |
| Custom Fields    | Additional Address fields available by their fieldnames                  |


Fieldnames are case-sensitive. Use the fieldname shown in Customize Form or DocType metadata, not the field label visible to users.

## Write safe Jinja

Wrap optional values in conditions so empty fields do not produce blank labels or punctuation:

```jinja
{{ address_line1 }}<br>
{% if address_line2 %}{{ address_line2 }}<br>{% endif %}
{{ city }}{% if state %}, {{ state }}{% endif %} {{ pincode }}<br>
{{ country }}
```

Use `<br>` for deliberate address line breaks. Keep complex business logic out of the template; store normalized data in the Address instead.

The template engine exposes standard and Custom Fields from Address. See [Customize Form](/framework/customize-a-doctype) before referencing a custom field.

## Country-specific and default behaviour

For a United States Address, a template may render City, State, and ZIP on one line and include County only when required. Another Country may place the postal code before the city.

ERPNext determines the template at render time using the Country on the Address. Therefore:

- correct the Country when the wrong template appears;
- create a country-specific template for a real regional difference;
- use the default template as a safe general fallback; and
- avoid marking several conflicting templates as default.

Address Templates affect [Customers](/erpnext/customer), [Suppliers](/erpnext/supplier), [Companies](/erpnext/company), Warehouses, Contacts, and transactions such as [Delivery Notes](/erpnext/delivery-note) wherever formatted Addresses are rendered.

## Save and next steps

Address Template is saved rather than submitted. After saving:

- check several complete and incomplete Addresses;
- verify billing and shipping results;
- preview a [Sales Order](/erpnext/sales-order) and a [Purchase Invoice](/erpnext/purchase-invoice);
- test any relevant custom print format; and
- document custom field dependencies for future administrators.

## Troubleshooting


| Problem                               | What to check                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| The wrong format appears              | Verify the Address Country and country-specific template                       |
| No country-specific template exists   | ERPNext should use the template marked default                                 |
| Blank labels or punctuation appear    | Wrap the entire optional line or label in a Jinja condition                    |
| A field never appears                 | Confirm its exact fieldname and that the Address contains a value              |
| Save succeeds but print output breaks | Check HTML structure, Jinja blocks, and the print format's available width     |
| A custom field causes an error        | Confirm the field exists in every target environment or guard it appropriately |


## Frequently asked questions

### Can I use Custom Fields?

Yes. Address Custom Fields are available to the template by fieldname.

### Should every Country have a template?

No. Create country-specific templates only where formatting differs; the default handles the rest.

### Can the template change field labels such as PIN to ZIP?

Yes. Write the desired label directly in the country-specific template.

### Do template changes update submitted documents?

They can change newly rendered address output, depending on how a document or print format stores or fetches the address. Test the exact document type before relying on historical behaviour.

### Can CSS be used?

Keep styling restrained and compatible with the target print format. Prefer semantic HTML and simple line breaks for addresses.

## Related topics

- [Address](/erpnext/address)
- [Customer](/erpnext/customer)
- [Supplier](/erpnext/supplier)
- [Print Formats](/framework/print-format)

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

[Screenshot on the live page: Billing Address for Summit Digital Stores with preferred billing status.]

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

[Screenshot on the live page: Links menu showing the Address connected to Summit Digital Stores.]

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
