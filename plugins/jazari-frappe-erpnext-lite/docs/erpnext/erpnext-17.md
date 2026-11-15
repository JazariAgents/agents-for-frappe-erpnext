<!-- Frappe documentation: erpnext, part 17 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__custom-field.md -->
---
title: "Custom Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/custom-field"
updated: "2026-03-02"
---

**Every form in ERPNext has a standard set of fields. If you need to capture some information, but there is no standard Field available for it, you can insert Custom Field in a form as per your requirement.**

You can go to [Customize Form](/erpnext/customize-form) and add the Field in a particular Form or a Document type *(hereafter referred to as DocType)* .

To access Custom Field, go to:


> Home > Customization > Form Customization > Custom Field
> 
> 

You can also go to the list view of any DocType and select Customize from the Menu options.

[Screenshot on the live page: Customize Option in List View]  


1. How to create a Custom Field
-------------------------------

1. Go to the Custom Field list and click on New.
2. **Document**: Select the Document in which you need to add the Custom Field.
3. **Label**: Enter what Label would you like to give to your Custom Field.
4. **Field Type**: ERPNext already has a set of Field Types defined which can be fetched from this drop-down menu. You can select the Type of your Custom Field from within this menu.
5. Update.

[Screenshot on the live page: New Custom Field]  


*Learn more about Field types* [*here*](/erpnext/field-types.html)*.*

You can also go to [Customize Form](/erpnext/customize-form) and add, edit or remove a Field in a particular Form.

[Screenshot on the live page: Add Custom Field From Customize Form]  


### 1.1. Additional Details

1. **Options**: This Field comes into picture when you would want your data to be specific or specify the data. E.g., when you have selected the Field to be a 'Select Field', you would be required to enter the selection options here.

[Screenshot on the live page: Custom Field with Fieldtype as Select]
2. **Fetch From**: When you want your Custom Field to be 'Link Field', you would be required to specify the Form to which this Field is to be linked. E.g., you want to create a Custom Field 'Project' in the DocType 'Item'. You would be required to enter to specify your Field Type as 'Link' and enter 'Project' in the Fetch From Field to ensure that the Field is updated with the list of all the required DocTypes.
3. **Fetch If Empty**: This check-box will ensure that this Field will be not overwritten based on Fetch From if a value already exists.
4. **Default Value**: Enter the default value of the Field which you would want to be fetched for this Field.
5. **Depends On**: You can define a condition here for the Field to be displayed. E.g., in the DocType Item, two fields 'Asset Category' and 'Asset Naming Series' will only appear if the Field 'Is Fixed Asset' is checked. The dependency condition here would be `is_fixed_asset`.

[Screenshot on the live page: Depends On Option]
6. **Field Description**: You can add the description of the Field here which can be displayed below this Field.

[Screenshot on the live page: Custom Field Description]
7. **Permission Level**: This will allow you to specify which roles within your organization will be able to edit this Field. You can go through [Role Based Permissions](/erpnext/role-based-permissions) for more understanding on this.
8. **In Preview**: If [Show Preview Popup](/erpnext/customize-form#13-more-properties) for the document type is checked, the Field will be included in the popup that appears on hovering over links of the document type (in list view and other link fields).
9. **Width**: This will define the width allocated to this Field while viewing the Form in a Grid View.

### 1.2. More Properties

* **Is Mandatory Field**: This box can be checked if you want to make this Field mandatory while submitting a DocType.
* **Unique**: Check this box when you want the value of this Field to be unique. This can be done in cases where the Custom Field is for a code or an Identification Number. E.g., Item Code in case of Item, GST Number in case of Customer.
* **Read Only**: When you want this Field to be a read only or a non-editable Field. In this case, the value of the Field shall be auto-fetched from other fields.
* **Hidden**: Check this Field when you want this Field to be hidden, or to hide an existing Field.
* **Print Hide**: In cases that you want the print button to be hidden from the Print Format. Checkout [Fields in Print Format](/erpnext/making-fields-visible-in-print-format) for more information.
* **No Copy**: Checking this box will restrict copying of this Field in the DocType.
* **Allow on Submit**: This will allow you to make changes to the Field even after you have submitted the Form. Checkout [Editing Value in Submitted Document](/erpnext/editing-a-field-after-submission) for more information.
* **In List View**: This will make the field visible in the List View of the DocType.
* **In Standard Filter**: The field will become a standard filter in the List view of the Document.
* **In Global Search**: When this box is checked this Field can be searched form the Global Search.
* **Bold**: This will make this Field type bold, this adds more value to the Field.
* **Report Hide**: This field will not be visible in the reports when you check this box.
* **Ignore XSS Filter**: This will allow you to view this Field without the HTML tags.
* **Translatable**: When this box is checked, it becomes translatable while applying [Custom Translations](/erpnext/custom-translations) to this.

### 1.3 Field name

* Custom fields by default add a prefix of `custom_` to fieldname. This is done to avoid a potential clash with current/future standard fields
* If your customizations require a specific fieldname you can rename any existing custom field by going to Custom Field doctype and clicking the "Rename Fieldname" button.

[Screenshot on the live page]

2. Videos
---------

<!-- page: erpnext/erpnext__custom-translations.md -->
---
title: "Custom Translations in Print Formats"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/custom-translations"
updated: "2026-03-02"
---


**With Custom Translations, user can print the customer's and supplier's document in their local language.**

For example, if you have customers from Germany and France who want quotations in German and French, it's possible using Custom Translations.

## 1. Set the Language

In the Customer master, select the default Language. Say, the default language for the Customer is **Spanish**.

[Screenshot on the live page: Set Customer Language]

Same way, you can also set default language in the Supplier master.

### 1.1 Print Preview in the Party's Language

In the Print Preview of a transaction, values will be translated into the party's language.

Customer Quotation print preview in customer's default language.

[Screenshot on the live page: Invoice in Customer Language]

Supplier Quotation print preview in supplier's default language.

### 1.2 Changing the print language in the preview

User has the option to select an alternate language on print view.

[Screenshot on the live page: Select Language in Invoice]

## 2. Custom Translation

Users can set their custom translations using Custom Translations form. For example, if a user wants to set a description of a product in the customer's language (Spanish). For that, create a new translation with language as Spanish, enter source data and translated information.

> Home > Customization > Other > Custom Translations > New

[Screenshot on the live page: Translation]

The translation is applied when the user selects the language as Spanish on supplier Quotation's print preview. Note that no translation is applied for the second item's description since it wasn't created in the Translation list.

[Screenshot on the live page: Translation in Transaction]

### 3. Related Topics
1. [Address Template](/erpnext/address-template)
1. [Quotation](/erpnext/quotation)
1. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__customer-contact-and-address-relationship.md -->
---
title: "Customer, Contact and Address Relationship | ERPNext Documentation"
description: "Understand how ERPNext links Customers, Contacts, and Addresses, why they are separate, and how primary contact, billing, and shipping records are selected."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer-contact-and-address-relationship"
updated: "2026-07-25"
---

A [Customer](/erpnext/customer), [Contact](/erpnext/contact), and [Address](/erpnext/address) describe different parts of the same business relationship. The Customer is the party you sell to, a Contact is a person you communicate with, and an Address is a location used for billing, shipping, or another purpose.

Keeping these as separate linked records lets one Customer have several people and locations without creating duplicate customer accounts.

## How the three records fit together


| Record       | Represents                                                                                          | Example                        |
| ------------ | --------------------------------------------------------------------------------------------------- | ------------------------------ |
| **Customer** | The commercial party used for quotations, orders, invoices, payments, credit control, and reporting | Summit Digital Stores          |
| **Contact**  | A person you communicate with                                                                       | Morgan Lee, Purchasing Manager |
| **Address**  | A physical or mailing location                                                                      | Harbor Avenue billing office   |


The usual relationship looks like this:

> **Customer**  
> ↳ linked to one or more **Contacts**  
> ↳ linked to one or more **Addresses**

The Contact and Address are not stored inside the Customer. They are independent records connected through **Links**. This matters because the same Contact or Address can be linked to another supported party when the relationship is genuine.

## Why are they separate?

A company can remain the same Customer even when its people or locations change. Separating the records reflects that reality.

- **One Customer can have several Contacts.** A purchasing manager may receive quotations, while an accounts-payable contact receives invoices.
- **One Customer can have several Addresses.** The head office may be used for billing, while goods are delivered to a warehouse or retail branch.
- **People and locations can change independently.** You can replace a Contact or add a delivery location without creating another Customer and splitting the sales history.
- **Transactions can use the appropriate combination.** A Sales Order can use one Contact and shipping Address, while a later order for the same Customer uses another.

Create another Customer only when the party must be treated as a separate commercial or accounting relationship. Do not create a new Customer merely for a new employee, office, or delivery point.

## Example

Nova Electronics Trading sells to **Summit Digital Stores**. ERPNext can model the relationship as follows:

- **Customer:** Summit Digital Stores
- **Primary Contact:** Morgan Lee, Purchasing Manager
- **Other Contact:** Taylor Brooks, Accounts Payable
- **Preferred Billing Address:** Harbor Avenue office
- **Preferred Shipping Address:** Meridian Parkway warehouse

When a user creates a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order) for Summit Digital Stores, ERPNext can fetch Morgan Lee and the preferred Addresses. The user can still select Taylor Brooks or another linked Address when that transaction requires it.

## How primary records are selected

Primary settings tell ERPNext which linked record to use as the normal default. They do not prevent users from selecting another linked record.

### Primary Contact

Enable **Is Primary Contact** on the Contact that should normally be fetched for the linked Customer. If a Customer has several Contacts, use this for the person who usually receives sales communication.

A Contact also has primary email and primary phone selections. These answer a different question:

- **Is Primary Contact** chooses the preferred person for the linked party.
- **Primary email** and **primary phone** choose the preferred details within that person's Contact record.

### Preferred billing and shipping Addresses

An Address can be marked as the **Preferred Billing Address**, the **Preferred Shipping Address**, or both.

- The preferred billing Address is the normal location for invoices and billing communication.
- The preferred shipping Address is the normal delivery destination.

These may be different locations. For example, a Customer may pay invoices from its head office but receive goods at a warehouse.

### Selection on a transaction

When the Customer is selected on a supported sales transaction, ERPNext uses eligible linked records and their primary or preferred settings to provide defaults. A user can replace those defaults with another Contact or Address linked to the same Customer.

Set the primary flags explicitly when a Customer has multiple linked records. This avoids relying on whichever eligible record happens to be available.

Changing a primary Contact or preferred Address affects the defaults used on future documents. It does not rewrite the Contact, Address, or rendered address text already stored on submitted transactions.

## Common mistakes


| Mistake                                              | Better approach                                                                             |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Creating a new Customer for every branch             | Use linked Addresses unless each branch is a separate commercial or accounting party.       |
| Putting a person's details in the Customer name      | Create a Contact and link it to the Customer.                                               |
| Using Address Type alone to choose defaults          | Set the preferred billing and shipping flags explicitly.                                    |
| Assuming the primary Contact is the only Contact     | Keep all relevant Contacts linked and select the appropriate one per transaction.           |
| Editing a submitted document after a default changes | Use the new default on future documents. Submitted documents retain their recorded details. |


## Frequently asked questions

### Can one Customer have multiple Contacts and Addresses?

Y

es. This is the normal setup for organizations with several employees, offices, warehouses, or delivery locations.

### Can a Contact or Address exist without a Customer?

Y

es. Both can exist independently and be linked later.

### Can the same Contact be linked to more than one Customer?

Yes, when the person genuinely represents more than one party. Review the primary setting carefully because it belongs to the Contact record.

### Can users override the primary selection?

Y

es. Primary and preferred records provide defaults. Users can select another eligible linked record for a particular transaction.

## Related topics

- [Customer](/erpnext/customer)
- [Contact](/erpnext/contact)
- [Address](/erpnext/address)
- [Address Template](/erpnext/address-template)
- [Difference between Lead, Contact, and Customer](/erpnext/difference_between_lead_contact_and_customer)

<!-- page: erpnext/erpnext__customer-group.md -->
---
title: "Customer Group | ERPNext Documentation"
description: "Learn how to create hierarchical Customer Groups in ERPNext and configure price lists, payment terms, receivable accounts, and credit limits."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer-group"
updated: "2026-07-23"
---

A **Customer Group** classifies similar [Customers](/erpnext/customer) in a hierarchy. Groups make sales analysis easier and can supply common price, payment, credit, and accounting defaults to Customers and transactions.

Use a group for a stable business distinction—such as retail, wholesale, government, or strategic accounts—not for a temporary campaign or an individual sales territory.

## Why use Customer Groups?

Customer Groups provide five practical benefits:

- **Clearer sales analysis:** compare revenue, order value, and sales trends across customer segments.
- **Consistent defaults:** supply a common price list and payment terms when a Customer does not have more specific settings.
- **Less repetitive setup:** maintain shared commercial defaults once instead of configuring every Customer individually.
- **Group-level controls:** apply company-specific credit limits and, when required, receivable or advance accounts.
- **A scalable hierarchy:** use parent groups for broad categories and leaf groups for the Customers selected in transactions.

For example, Nova Electronics Trading can separate retail, wholesale, government, and marketplace Customers. Management can analyze each segment while sales users receive appropriate defaults when they select a Customer.

[Screenshot on the live page: Customer Group hierarchy with Nova Commercial Customers.]

## Before you begin

Plan the hierarchy before adding groups:

- Choose the parent under which the group belongs.
- Decide whether the new record will contain Customers or only other groups.
- Check whether defaults should be maintained on the group, on each Customer, or on individual transactions.
- Confirm the required [Price List](/erpnext/price-lists), [Payment Terms](/erpnext/payment-terms), receivable account, and credit policy.

ERPNext includes groups such as Commercial, Government, Individual, and Non Profit. You can keep these, rename them carefully, or add groups that match your reporting needs.

## Create a Customer Group

1. Open **Selling > Customer Group**.
2. In Tree view, select the parent group.
3. Select **Add Child** or **New**.
4. Enter the **Customer Group Name**.
5. Select **Is Group** when this node should contain child groups rather than Customers.
6. Save the Customer Group.

Only leaf nodes can be selected on transactions. If **Is Group** is enabled, create at least one child leaf group before assigning Customers.

[Screenshot on the live page: Customer Group form showing its parent, leaf setting, defaults, accounts, and credit limits.]

### Example hierarchy

Nova Electronics Trading can keep **Nova Commercial Customers** as a leaf below **All Customer Groups**. If reporting later needs more detail, it can convert the structure into a parent with Retail, Wholesale, and Marketplace child groups, then move Customers to the appropriate leaves.

## Alternative ways to create Customer Groups

- Use [Data Import](/erpnext/data-import) for a reviewed hierarchy with many groups.
- Create a group from a Customer Group link field when permissions allow, then return to Tree view to confirm its parent.
- Use an approved integration when another master-data system owns customer segmentation.

Create parents before children during imports. Review the resulting tree instead of assuming spreadsheet order produced the intended hierarchy.

## Important fields and what they mean


| Field                                        | What it controls                                                                    |
| -------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Customer Group Name**                      | The label shown on Customers, transactions, filters, and reports                    |
| **Parent Customer Group**                    | The node immediately above this group in the hierarchy                              |
| **Is Group**                                 | Makes the node a parent; group nodes cannot be selected in transactions             |
| **Default Price List**                       | Supplies the selling price list when no more specific Customer default overrides it |
| **Default Payment Terms Template**           | Supplies the payment schedule for Customers in the group                            |
| **Default Account**                          | Uses a company-specific receivable account instead of the normal company default    |
| **Advance Account**                          | Uses a company-specific account for Customer advances                               |
| **Credit Limit**                             | Applies a company-specific group credit limit according to credit-control behaviour |
| **Bypass credit limit check at sales order** | Defers the credit-limit check beyond Sales Order for the configured row             |


Defaults cascade only when a more specific value is not set. Verify the resulting values on a new [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), or [Sales Invoice](/erpnext/sales-invoice) before relying on a new group configuration.

## Configure defaults and credit controls

Use group defaults when most members share the same policy:

- Set a price list for a common pricing segment.
- Set a payment-terms template for a standard due-date schedule.
- Add company-specific accounts only when the group must post differently from the company's default Debtors account in the [Chart of Accounts](/erpnext/chart-of-accounts).
- Add a credit-limit row for each company that needs a group-level limit.

Use [Credit Limit](/erpnext/credit-limit) guidance to define which transactions should be blocked. A payment schedule controls when amounts are due; it does not increase available credit.

Customer-level and transaction-level values can be more specific than the group. Document your precedence policy so users know where to correct an unexpected default.

## Save and next steps

Customer Group is saved rather than submitted. After saving:

- assign new or existing Customers to a leaf group;
- create a test sales document and verify fetched defaults;
- review [Sales Analytics](/erpnext/sales-reports) by Customer Group; and
- keep the tree shallow enough for users to choose the right leaf consistently.

Moving a Customer changes future classification and reporting filters. Existing submitted documents retain their stored values.

## Group node types


| Type              | Use                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| **Group node**    | Organizes other Customer Groups and cannot be selected on transactions                                      |
| **Leaf node**     | Can be assigned to Customers and sales transactions                                                         |
| **Default group** | The fallback group selected through Selling Settings when a Customer does not require a specialized segment |


## Troubleshooting


| Problem                                    | What to check                                                                           |
| ------------------------------------------ | --------------------------------------------------------------------------------------- |
| A group cannot be selected on a Customer   | It may have **Is Group** enabled; select or create a leaf                               |
| A child appears under the wrong parent     | Open it and correct **Parent Customer Group**, then verify Tree view                    |
| A default price list does not appear       | Check Customer-level defaults and transaction-level selections                          |
| Credit control does not behave as expected | Review group and Customer credit rows, company, outstanding amount, and bypass settings |
| A report combines unexpected Customers     | Confirm each Customer's current group and the report's date and company filters         |


## Frequently asked questions

### Should every Customer have its own group?

No. A group should represent a reusable segment. Customer-specific settings belong on the Customer.

### Can a Customer Group contain both Customers and child groups?

No. Use a group node for children and leaf nodes for Customers.

### Can I change a Customer's group later?

Yes. Review reporting and defaulting effects before moving a heavily used Customer.

### Do group defaults change submitted documents?

No. They affect values fetched into new documents; submitted records preserve their stored values.

### Do I need a separate receivable account for each group?

Usually not. ERPNext normally uses the company’s common receivable account while tracking balances by Customer.

## Related topics

- [Customer](/erpnext/customer)
- [Price List](/erpnext/price-lists)
- [Payment Terms](/erpnext/payment-terms)
- [Credit Limit](/erpnext/credit-limit)

<!-- page: erpnext/erpnext__customer-portal.md -->
---
title: "Customer Portal"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer-portal"
updated: "2026-02-28"
---


Customer Portal is designed to give easy accessibility to customers of a company.

This portal allows customers to login and find out information relevant to them. The customers can trace the communication history of their mails. They can also check order status by logging into the website.

## Signup

Your Customer and Suppliers can signup to your ERPNext account by following Signup option on the Login Page.

#### Step 1: Signup

On the Login Page, you will find option to Signup.

[Screenshot on the live page: Website User Signup]

#### Step 2: Enter Customer Name and ID

[Screenshot on the live page: Website User Signup]

After the sign up process, an email will be sent to the customers Email Address with the password details.

## Portal Login

To login into the customer account, the customer has to use his Email Address and the password sent by ERPNext; generated through the sign-up process.

[Screenshot on the live page: Website User Signup]  

## Customer Orders Invoices And Shipping Status

ERPNext Web Portal gives your customers quick access to their Orders, Invoices and Shipments Customers can check the status of their orders, invoices, and shipping status by logging on to the web.

[Screenshot on the live page: Customer Portal]

Once an order is raised, either using the Shopping Cart or from within ERPNext, your customer can view the order and keep an eye on the billing and shipment status. When the invoice and payment against these orders are submitted, the customer can see the updated status on the portal, at a glance.

[Screenshot on the live page: Customer Portal]

#### Outstanding Sales Invoice

[Screenshot on the live page: Customer Portal]

#### Paid Sales Invoice

[Screenshot on the live page: Customer Portal]

## Issues

The customer portal makes it very easy for a customer to raise concerns. A
simple and intuitive interface facilitates your customer to report their
concerns as Issues. They can view the complete thread of their
conversation.

#### Empty Issue List

[Screenshot on the live page: Issue List]

#### New Issue

[Screenshot on the live page: New Issue]

#### Open Issue

[Screenshot on the live page: Issue Raised]

#### Reply on Issue

[Screenshot on the live page: Issue reply]

<!-- page: erpnext/erpnext__customer-provided-items.md -->
---
title: "Customer Provided Items\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer-provided-items"
updated: "2026-03-02"
---


In Contract Manufacturing, in some cases, the Customer provides specific items as one or few of the BOM components. These items cannot be received using a 'Buying Cycle' since that will mean making Customer as a Supplier at the same time. It will also go through each doctype in the cycle.

In this feature, Customer Provided Item is received through 'Stock Entry' with type 'Material Receipt' from a 'Material Request' with type 'Customer provided'. This feature is used when someone subcontracts the manufacturing process to you and supplies the raw materials.

[Screenshot on the live page: Customer Provided Material Request]

Here are the steps on how to setup a 'Customer Provided' item.

1. Got to [Item Doctype](/erpnext/stock) and add a new 'Customer Provided' item.

 > Home > Stock > Items and Pricing > Item

2. In the 'Purchase, Replenishment Details' section, check 'Is Customer
 Provided' and set a default Customer. Note that 'Is Purchase Item' needs to be unticked to use this feature.

 [Screenshot on the live page: Item Purchase Details]

How to receive a 'Customer Provided' Item?

1. If a 'Production Plan' is used, 'Material Request' for this item can be auto created. That is, the item to be manufactured is fetched first via Sales Order or Material Request, Items are fetched for the Work Order using the 'Get Items for Work Order' button, then click on the 'Get Raw Materials for Production' button.

 [Screenshot on the live page: Material Request in Production Plan]

2. Once a component in a BOM is set as 'Customer Provided' and 'Material Request' is created from a 'Production Plan', it will create both 'Material Request' with type 'Purchase' and 'Customer Provided'. From there, a 'Stock Entry' with purpose 'Material Receipt' can be created.

 [Screenshot on the live page: Stock Entry from Material Request]

3. A 'Material Request' can have multiple 'Stock Entry' - Material Receipt. It
 will reflect it in the status.

4. Customer will be able to track their 'Material Requests' in a Web Portal
 'Material Requests'. The portal is filtered to show only the 'Material Request' of the customer.

 

<!-- page: erpnext/erpnext__customer.md -->
---
title: "Customer | ERPNext Documentation"
description: "Learn how to create and configure Customers in ERPNext, add addresses and contacts, set sales defaults, credit limits, payment terms, and accounting."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer"
updated: "2026-07-23"
---

A **Customer** represents a person, business, or other organization that buys goods or services from you. The Customer master gives quotations, orders, invoices, payments, projects, support records, and reports one consistent party reference.

Create a separate Customer for each independently billed party. Store people and locations as linked Contacts and Addresses instead of putting every detail in the Customer name.

[Screenshot on the live page: Customer details and sales defaults for Summit Digital Stores.]

## Before you begin

Confirm the following before creating the record:

- How Customer IDs should be generated in [Selling Settings](/erpnext/selling-settings). ERPNext can use the Customer name or a naming series.
- The correct [Customer Group](/erpnext/customer-group), such as Commercial, Government, or a group designed for your reporting structure.
- The Customer's [Territory](/erpnext/territory), billing currency, price list, payment terms, and expected credit policy.
- Whether the party is a company, individual, partnership, or one of your own companies.

You need permission to create Customer records. Additional permissions may be required to create linked Addresses and Contacts or configure accounting defaults.

## Create a Customer

1. Open the Customer list from **Selling > Customer**.
2. Select **Add Customer**.
3. Enter the **Customer Name**.
4. Select the **Customer Type**, **Customer Group**, and **Territory**.
5. Add the billing currency, price list, and payment terms when they should default on this Customer's transactions.
6. Save the Customer.

After saving, add at least one billing Address and the primary Contact. This makes the correct location and person available when users create quotations and other sales transactions.

### Example

Nova Electronics Trading creates **Summit Digital Stores** as a Company Customer in its commercial customer group. The Customer uses USD, the Nova Retail USD price list, and Net 30 payment terms. Its billing office, receiving warehouse, and purchasing manager are stored as linked records.

## Alternative ways to create a Customer

- **From a Lead:** Convert a qualified [Lead](/erpnext/lead) so the Customer remains connected to the earlier sales activity.
- **During a sales transaction:** Depending on permissions and configuration, create a Customer from the Customer link field without leaving the transaction.
- **Data import:** Use the [Data Import](/erpnext/data-import) tool for a reviewed batch of Customers. Import linked Contacts and Addresses separately and verify their Dynamic Link values.
- **Integration:** Create Customers through an approved API or integration when another system owns customer onboarding. Apply the same validation and duplicate checks as manual entry.

Avoid creating another Customer merely because a Contact or delivery location changes. One Customer can have several Contacts and Addresses.

## Important fields and what they mean


| Field                      | What it controls                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Customer Name**          | The party's readable name. It may also become the Customer ID when naming by Customer Name is enabled. |
| **Customer Type**          | Distinguishes Company, Individual, and Partnership Customers and can affect naming and reporting.      |
| **Customer Group**         | Classifies Customers for defaults, reporting, permissions, and pricing decisions.                      |
| **Territory**              | Places the Customer in the sales territory hierarchy for analysis and assignment.                      |
| **Billing Currency**       | Defaults the transaction currency on new sales documents for this Customer.                            |
| **Price List**             | Selects the default selling [Price List](/erpnext/price-lists) used to retrieve Item prices.           |
| **Payment Terms Template** | Applies the default [Payment Terms](/erpnext/payment-terms) schedule to new orders and invoices.       |
| **Default Account**        | Posts this Customer's receivable entries to a specific company account instead of the company default. |
| **Credit Limit**           | Blocks applicable transactions when outstanding exposure exceeds the configured company limit.         |
| **Disabled**               | Prevents users from selecting the Customer in new transactions without deleting its history.           |
| **Is Internal Customer**   | Identifies a Customer representing one of your companies for inter-company transactions.               |


Leave optional defaults empty when they vary by transaction. A user can select an appropriate value on the sales document instead.

## Add addresses and contacts

[Addresses](/erpnext/address) and [Contacts](/erpnext/contact) are independent records linked to the Customer. This lets a Customer have several offices, delivery locations, buyers, and accounts-payable contacts without duplicating the Customer.

1. Open the saved Customer and select **Address & Contact**.
2. Select **New Address**, enter the location, choose its type, and mark the primary or shipping address when appropriate.
3. Select **New Contact**, enter the person's name and role, then add the primary email address and phone number.
4. Select the Customer's primary Address and Contact when ERPNext does not assign them automatically.

[Screenshot on the live page: Billing and shipping addresses with the primary purchasing contact.]

Review primary flags carefully. Sales documents can fetch the primary billing and shipping details, while users can still choose another linked record for a specific transaction.

## Configure sales, tax, and accounting defaults

Use Customer-level defaults only when they consistently apply to this party:

- Set a Tax Category or regional **Tax Withholding Category** when required by your tax configuration. See [Tax Withholding Category](/erpnext/tax-withholding-category) for the applicable rules.
- Assign a [Sales Person](/erpnext/sales-person) or sales team and ensure contribution percentages total 100%.
- Add a [Sales Partner](/erpnext/sales-partner) and commission rate when an external partner influences the sale.
- Select a [Loyalty Program](/erpnext/loyalty-program) when the Customer earns or redeems loyalty points.
- Use the same Customer across companies. Add a company-specific receivable account only when it is required by your [Chart of Accounts](/erpnext/chart-of-accounts).

ERPNext normally posts Customer receivables to the company's default Debtors account, so a separate ledger is not required for every Customer. A company-specific account is an exception, not a prerequisite.

### Credit limits and payment controls

Add one credit-limit row for each company that needs a limit. ERPNext evaluates submitted exposure against that amount according to the configured credit-control behaviour. Keep the **Bypass credit limit check at sales order** option cleared when orders should be checked before invoicing.

[Screenshot on the live page: Company receivable account and Customer credit limit.]

Use the dedicated [Credit Limit](/erpnext/credit-limit) guidance when defining the policy. The payment terms template controls when amounts are due; it does not increase the Customer's credit limit.

If Selling Settings require a Sales Order or Delivery Note before invoicing, Customer-level settings can allow direct Sales Invoices for an approved exception. Use these overrides deliberately because they change the normal sales controls for this Customer.

## Save and next steps

Customer is a master record and is saved rather than submitted. After saving:

- create a Quotation, Sales Order, or Sales Invoice;
- review the Customer dashboard and Connections for linked transactions;
- use **Accounting Ledger** to inspect entries for this party; and
- use the Accounts Receivable report to review outstanding invoices.

Changes to defaults affect newly created documents. Existing submitted transactions keep the values with which they were posted.

## Customer types and availability


| Value                 | When to use it                                                                   |
| --------------------- | -------------------------------------------------------------------------------- |
| **Company**           | A registered business or organization acting as the buying party                 |
| **Individual**        | A person buying in their own capacity                                            |
| **Partnership**       | A partnership that should be distinguished from other organizations              |
| **Enabled**           | Available for selection in new transactions                                      |
| **Disabled**          | Retained for history but unavailable for new transactions                        |
| **Internal Customer** | Represents another company in the same organization for inter-company processing |


Do not delete a Customer merely because the relationship has ended. Disable it to preserve the audit trail and prevent new use.

## Troubleshooting


| Problem                                          | What to check                                                                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| The Customer already exists                      | Search by Customer name, primary email, mobile number, tax ID, and linked Address before creating another record.        |
| Currency or price list does not default          | Confirm the Customer defaults and verify that the selected price list supports the required currency.                    |
| The wrong address appears on a transaction       | Check the linked Address type and primary or shipping flags, then reselect the address on the Customer if it was edited. |
| A transaction is blocked by credit control       | Review the company credit limit, outstanding invoices, overdue settings, and any permitted bypass.                       |
| A user cannot select the Customer                | Confirm that the Customer is not disabled and that the user has the required role and permissions.                       |
| Accounting posts to the wrong receivable account | Check the company-specific Customer account and the company's default receivable account.                                |


## Frequently asked questions

### Can one Customer have multiple addresses and contacts?

Yes. Link each location and person to the same Customer, then mark the normal billing, shipping, and primary records.

### Should every Customer have a separate receivable ledger?

No. ERPNext normally uses the company's shared Debtors account while tracking the Customer as the accounting party. Configure a separate account only for a specific accounting requirement.

### Can two Customers have the same name?

When naming by Customer Name is enabled, ERPNext keeps IDs unique by adding a suffix when required. Search for an existing party before accepting the duplicate.

### Can I stop new sales without deleting the Customer?

Yes. Enable **Disabled**. Historical documents and ledger entries remain connected to the Customer.

### Can the same Customer be used by multiple companies?

Yes. Company-specific accounts and credit limits are stored in separate rows on the Customer.

## Related topics

- [Customer Group](/erpnext/customer-group)
- [Contact](/erpnext/contact)
- [Address](/erpnext/address)
- [Quotation](/erpnext/quotation)
- [Credit Limit](/erpnext/credit-limit)

<!-- page: erpnext/erpnext__customise-cash-flow-report.md -->
---
title: "Customise Cash Flow Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customise-cash-flow-report"
updated: "2026-08-14"
---

Nova Industries's default Cash Flow report explains how cash moved through operating, investing, and financing activities. Finance wants a reusable IFRS-style presentation with clearer lines for profit before tax, depreciation, finance costs, receivables, payables, inventory, equipment purchases, and financing.



In the current ERPNext develop version, Nova can create or adapt a [Financial Report Template](/erpnext/financial-report-template) with Report Type set to **Cash Flow**. The template controls report headings, account selection, calculations, indentation, signs, hidden rows, and charts. It changes presentation, not the underlying [General Ledger](/erpnext/general-ledger) entries.

## Before you begin

- Run the standard [Cash Flow Report](/erpnext/cash-flow-report) and reconcile it with the General Ledger.
- Have an accountant approve the required headings, classifications, signs, and calculations.
- Review the [Chart of Accounts](/erpnext/chart-of-accounts) and assign consistent Account Categories where template rows use them.
- Test the template with representative transactions before using it for management or external reporting.

## Review the current report

Run Cash Flow for Nova Industries with a period containing operating, investing, and financing transactions. Save the baseline totals before enabling a custom format.

[Screenshot on the live page: Loaded Cash Flow report for Nova Industries before mapping review]

## Create or copy a Cash Flow template

1. Open Financial Report Template.
2. Create a template, or copy an existing Cash Flow template when it is a suitable starting point.
3. Set **Report Type** to **Cash Flow**.
4. Enter a clear Template Name and keep the template enabled.

## Build and arrange the report lines

Add rows to **Report Line Items** in the exact order they should appear. Use blank or visual rows for section headings, Account Data rows for ledger-derived values, and Calculated Amount rows for subtotals. Indent supporting lines beneath their section and use stable Line References for formulas.

[Screenshot on the live page: Standard Cash Flow Statement IFRS template showing its ordered report line items]


| Example line                                    | Typical source      | Presentation                                              |
| ----------------------------------------------- | ------------------- | --------------------------------------------------------- |
| Cash flows from operating activities            | Visual or blank row | Section heading at indent level 0                         |
| Profit before tax                               | Account Data        | Period movement with the appropriate sign                 |
| Depreciation and amortisation                   | Account Data        | Indented non-cash adjustment                              |
| Operating profit before working-capital changes | Calculated Amount   | Formula based on earlier Line References                  |
| Change in trade receivables                     | Account Data        | Working-capital movement with reversed sign when required |


## Verify the custom report

[Screenshot on the live page: Cash Flow report after mapping with an account group opened for verification]



1. Refresh Cash Flow for the same company and period used for the baseline.
2. Confirm every expected line appears under the correct section.
3. Compare section totals and closing cash with the standard report and General Ledger.
4. Open unusual balances and verify the mapped accounts.
5. Repeat the test for a second period before relying on the format.

## Troubleshooting

### A line is missing

Confirm that the row is enabled, its Account Data filter matches the intended accounts, and the selected period contains relevant ledger activity. Check whether **Hide If Zero** is suppressing the row.

### A value appears twice

Review the template's account coverage for overlap. The same account may be included by more than one Account Data row, or a parent account and its children may both be selected.

### Net cash does not reconcile

Run the template and standard Cash Flow report with identical company, dates, Finance Book, dimensions, currency, and opening-balance options. Then check omitted accounts, duplicated coverage, formulas, Line References, and sign reversal.

## Frequently asked questions

### Does customisation change ledger entries?

The configuration changes how existing balances are classified and displayed. It does not repost transactions.

### Can I add a fourth cash-flow section?

The standard structure uses Operating, Investing, and Financing Activities. Use approved labels and mappings inside those sections unless a current product extension explicitly supports another structure.

### Should parent or child accounts be mapped?

Use an approach that avoids overlap and matches how the account tree is maintained. Parent accounts work best when all children share the same cash-flow treatment.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Accounts Settings](/erpnext/accounts-settings)
- [General Ledger](/erpnext/general-ledger)
- [Financial Report Template](/erpnext/financial-report-template)
