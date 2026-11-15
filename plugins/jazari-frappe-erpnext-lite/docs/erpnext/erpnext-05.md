<!-- Frappe documentation: erpnext, part 5 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__currency-exchange.md -->
---
title: "Currency Exchange | ERPNext Documentation"
description: "Store dated buying and selling exchange rates in ERPNext and understand when a transaction uses them."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/currency-exchange"
updated: "2026-08-14"
---

When Nova Industries sells electronics in EUR but reports in USD, finance needs a controlled conversion rate.



Nova agrees to invoice a customer in EUR while maintaining its books in USD. Finance approves `1 EUR = 1.15 USD` for 3 August 2026, so users should not look up or retype the rate on every transaction. A Currency Exchange record stores the approved rate, its effective date, and the direction in which it applies.



ERPNext checks eligible stored records before asking the configured online provider. This gives finance control when a contract fixes the rate, historical entries need a known rate, or a provider does not cover the pair. Use this page to make transactions apply the correct dated rate consistently.

## Before you begin

Enable both currencies in the [Currency](/erpnext/currency) list. Confirm the intended direction and rate convention. `EUR to USD = 1.15` means one euro equals 1.15 US dollars. The inverse is not automatically the same number, so create `USD to EUR` separately when that direction is needed.

Review [Accounts Settings](/erpnext/accounts-settings), especially **Allow Stale Exchange Rates** and **Stale Days**. These settings decide how old a stored record may be when ERPNext searches for a rate. Also review the active [Currency Exchange Settings](/erpnext/currency-exchange-settings) provider, which is used when no eligible manual record is found.

## Create a Currency Exchange record

1. Open Accounting &gt; Multi Currency &gt; Currency Exchange.
2. Select **Add Currency Exchange**.
3. Enter the date from which the rate applies.
4. Select the From Currency and To Currency.
5. Enter the rate using the relationship shown in the field label.
6. Select **For Buying**, **For Selling**, or both.
7. Save.

The list can contain multiple dated records for the same pair. ERPNext searches by transaction date and chooses the latest eligible matching record.



![Dated Currency Exchange records](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-exchange-list.png)



![EUR to USD exchange rate for buying and selling](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-exchange-rate.png)

## Important fields and what they mean


| Field         | Meaning                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| Date          | The key date used when ERPNext searches for the latest eligible rate on or before a transaction date.               |
| From Currency | The currency representing one unit in the field's relationship.                                                     |
| To Currency   | The currency calculated from the From Currency.                                                                     |
| Exchange Rate | The number of To Currency units equal to one From Currency unit. Read the generated field label before entering it. |
| For Buying    | Makes the record eligible for buying transactions that request a buying rate.                                       |
| For Selling   | Makes the record eligible for selling transactions that request a selling rate.                                     |


If both boxes are selected, the same rate can be used for buying and selling. Use separate records when your approved buying and selling rates differ.

## How ERPNext chooses a rate

For a requested direction, date, and transaction type, current develop behavior follows this pattern:

1. Search Currency Exchange for the latest matching record on or before the transaction date.
2. Apply the stale-rate rule from Accounts Settings.
3. If no eligible stored record exists and the provider is enabled, request the rate from the configured service.
4. If ERPNext still cannot find a rate, ask the user to create a manual Currency Exchange record.

The direction and buying or selling flag matter. A record for EUR to USD does not necessarily satisfy a request for USD to EUR. A record marked only For Buying does not satisfy a selling-rate request.

## Understand stale rates

When **Allow Stale Exchange Rates** is enabled, ERPNext may use the latest matching stored record without an age limit. This is useful for contract rates or finance-approved rates that remain valid until replaced. It can also preserve an old rate longer than intended, so establish a review process.

When the option is disabled, **Stale Days** limits how far back ERPNext searches. If no eligible manual rate remains, ERPNext tries the configured provider. The setting does not create an approval workflow and does not guarantee that a transaction stops when a manual rate expires, because the provider may return a market rate.

See [Freeze Exchange Rate](/erpnext/exchange-rate-field-frozen) if a transaction's Exchange Rate field appears read-only or behaves differently from what the page title suggests.

## Use the rate in a transaction

On a draft [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), [Quotation](/erpnext/quotation), or order, select the foreign currency and confirm the Exchange Rate. ERPNext calculates Company-currency totals using that rate. If the Price List uses a different currency, **Price List Exchange Rate** converts item prices separately.

The same check applies when a [Sales Order](/erpnext/sales-order) becomes the commercial source for a later invoice. A mapped document may carry forward currency and rate context, so verify the new document rather than assuming it refreshed to the latest master.

On a [Payment Entry](/erpnext/payment-entry), the currencies come from the paid-from and paid-to accounts. The source or target exchange rate converts between the account amounts and Company currency. A payment made at a different rate from its invoice can create a realized exchange gain or loss.

## Correct or supersede a rate

If a saved record is wrong and has not been relied on operationally, correct it with appropriate permission. If a new rate becomes valid later, create a new record with the later date rather than overwriting the historical record. Submitted transactions retain their own exchange-rate values; changing the master does not silently revalue old documents.

Use [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) to update the Company-currency carrying value of eligible open foreign-currency accounts at a reporting date. Do not alter historical Currency Exchange records merely to force a current closing balance.

## Troubleshooting

### ERPNext says it cannot find an exchange rate

Check that both currencies are enabled, the direction matches, the date is on or before the transaction date, and the buying or selling flag matches. Then verify stale-rate settings and whether the provider supports the pair.

### ERPNext uses an older manual rate instead of the market rate

An eligible Currency Exchange record is preferred. Review **Allow Stale Exchange Rates**, the latest dated record, and its flags. Create a new dated record or change the stale-rate policy according to your finance process.

### The transaction shows two exchange-rate fields

**Exchange Rate** converts the transaction currency to Company currency. **Price List Exchange Rate** converts the Price List currency for item prices. They can be different when the transaction and Price List use different currencies.

## FAQs

### Must I create a Currency Exchange record every day?

No, if no eligible manual record exists, ERPNext can use the configured provider. Create manual records only when you need controlled, historical, unsupported, or contract rates.

### Does the latest record override submitted invoices?

No, a submitted invoice retains the rate saved on that document. The new master affects later rate lookups.

### Can I store different buying and selling rates?

Yes, create records with the appropriate flags and rates. Do not select both flags if finance uses different rates for purchases and sales.

### Why does the inverse direction use another rate?

The system searches the exact From and To direction. Store the inverse record when that direction is needed, using the approved reciprocal or independently supplied rate.

### Can I type over the fetched rate?

The field may be editable depending on document state, permissions, and stale-rate behavior. Always verify the saved value and Company-currency total before submission.

## Related topics

- [Currency](/erpnext/currency)
- [Multi Currency Setup](/erpnext/multi-currency-setup)
- [Currency Exchange Settings](/erpnext/currency-exchange-settings)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__currency.md -->
---
title: "Currency | ERPNext Documentation"
description: "Configure currency symbols, fractions, and number formats in ERPNext before using a currency in transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/currency"
updated: "2026-08-14"
---

For Nova Industries, an electronics manufacturer and distributor, enabling EUR is the first step toward invoicing European customers.



Nova keeps its books in USD, but a European customer expects an invoice in EUR. Before EUR can appear correctly, ERPNext needs to know its code, symbol, fractional unit, and number format. The Currency record stores these display rules.



Enabling EUR makes it available for selection. It does not convert money, create a EUR ledger, or change the Company currency. Those decisions belong to the [Company](/erpnext/company-setup), foreign-currency [Account](/erpnext/chart-of-accounts), Customer, Price List, transaction, and Currency Exchange records. Use this page to enable a currency and verify how its values will appear throughout ERPNext.

## Before you begin

Confirm the currency's official code, symbol, fractional unit, and display convention. Use the standard three-letter code when it already exists. Changing a widely used Currency record affects how values appear across forms, reports, and print formats, so test presentation before changing a standard definition.

You also need permission to read or update Currency masters. If the purpose is to enter a conversion rate, use [Currency Exchange](/erpnext/currency-exchange) instead. If the purpose is to change a Company's base currency, review the Company and existing ledger entries first. A Currency record does not convert historical accounting data.

## Enable and review a currency

1. Open the Currency list from Accounting &gt; Multi Currency &gt; Currency.
2. Search for the standard code, such as EUR.
3. Open the record and select **Enabled**.
4. Review the fraction, symbol, and number format.
5. Save the record.

![EUR currency settings in ERPNext](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-eur-settings.png)

Enabling a currency makes it available for selection. It does not make it the default currency of any Company, party, account, [Price List](/erpnext/price-lists), or document.

Confirm the saved symbol and separators with a realistic amount, including thousands and decimals, before using the currency in customer-facing documents.

After saving, reload the record and test the formatted value on a Draft transaction and its print preview. This confirms that both Desk and the party-facing output use the expected symbol position, separators, and fraction wording.

## Important fields and what they mean


| Field                              | Meaning                                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Currency Name                      | The standard currency code used as the record name, such as EUR, USD, or GBP.                                                                                |
| Enabled                            | Makes the currency available in Link fields. Disable an unused currency only after confirming that no current process requires it.                           |
| Fraction                           | The singular name used for the sub-currency when amounts are converted to words, such as Cent or Penny.                                                      |
| Fraction Units                     | The number of fractional units in one currency unit. EUR uses 100 because one euro equals 100 cents.                                                         |
| Smallest Currency Fraction Value   | The smallest circulating denomination, entered as a decimal value. For EUR, 0.01 represents one cent. This is not the same setting as calculation precision. |
| Symbol                             | The display symbol, such as €, $, or £.                                                                                                                      |
| Show Currency Symbol on Right Side | Places the symbol after the number where that is the accepted convention.                                                                                    |
| Number Format                      | Defines grouping and decimal separators. For example, `#,###.##` displays 12345.67 as 12,345.67.                                                             |


The system-wide [System Settings](/erpnext/system-settings) and field precision still affect how many decimal places ERPNext calculates or displays. A number format changes presentation; it does not necessarily round the underlying General Ledger value. Test reports if you use a currency with no minor unit or unusually high precision.

## Where currency is selected

Currency has several distinct roles in ERPNext:


| Record                        | What the currency controls                                                                                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Company                       | The base currency used for the Company's accounting books and base-currency values.                                                                       |
| Account                       | The fixed account currency used for that ledger. One bank or cash account should represent one currency.                                                  |
| Customer or Supplier          | The default billing currency and, when configured, the matching receivable or payable account. See [Multi Currency Setup](/erpnext/multi-currency-setup). |
| Price List                    | The currency in which [Item Prices](/erpnext/item-price) are maintained.                                                                                  |
| Sales or Purchase transaction | The currency shown to the party and used for document totals. ERPNext also records the Company-currency equivalent through an exchange rate.              |


Do not assume that enabling EUR automatically creates a EUR bank account or EUR receivable account. Create those ledgers deliberately in the Chart of Accounts, then connect them to the relevant Customer or Supplier.

## Number format and precision

Number format answers how a number is shown. Precision answers how many decimal places are retained or displayed. For example, a format containing two decimal placeholders cannot by itself guarantee that every posting is rounded to two decimals. Review currency precision and the precision of the relevant fields if a report appears to contain unexpected decimals.

Use a format familiar to the people reading the document. `#,###.##` uses a comma for thousands and a period for decimals. `#.###,##` uses a period for thousands and a comma for decimals. Users should enter values according to the locale and input behavior configured for the site, then verify the parsed value before saving a transaction.

## After enabling a currency

Configure the rest of the workflow in this order:

1. Create the required foreign-currency ledger accounts.
2. Set the party's Billing Currency and default account when the party normally uses that currency.
3. Create a matching Price List if prices are maintained in the foreign currency.
4. Add a manual rate in Currency Exchange or verify the configured [exchange-rate provider](/erpnext/currency-exchange-settings).
5. Test a draft [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), or [Payment Entry](/erpnext/payment-entry) and compare the transaction and Company-currency totals.

## Troubleshooting

### The currency does not appear in a transaction

Open the Currency record and confirm that **Enabled** is selected. Then check whether the party account or Price List restricts the transaction to another currency. A foreign-currency party account normally requires the transaction currency to match that account.

### The symbol or separators look wrong

Review the Currency symbol, symbol position, and Number Format. Also check the site's number format and currency precision. Clear the browser cache or reload the document after saving a master change.

### A whole-number currency still has decimals in a report

Hiding decimal places is not the same as changing stored precision. Review System Settings, report behavior, tax rounding, stock valuation, and the relevant field precision before relying on a visually rounded report for statutory output.

## FAQs

### Do I need to create every currency my business may use?

No, most standard currencies already exist. Enable only those required by your Companies, parties, accounts, price lists, transactions, or reports.

### Can I change a Currency code after transactions exist?

Treat the code as a stable identifier. Create or enable the correct standard currency rather than renaming a code used by existing records.

### Does disabling a currency change old transactions?

No, it removes the currency from normal selection but does not translate or delete historical values. Confirm that reports, recurring documents, integrations, and imports no longer need it before disabling it.

### Is Smallest Currency Fraction Value the same as Currency Precision?

No, the smallest fraction describes the circulating denomination. Precision controls numeric calculation or display detail elsewhere in the system.

### Where do I enter the exchange rate?

Use Currency Exchange for a stored rate, or let ERPNext use the active provider when no eligible manual rate exists. The Currency master itself contains no rate.

## Related topics

- [Currency Exchange](/erpnext/currency-exchange)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Currency Exchange Settings](/erpnext/currency-exchange-settings)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

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

![Customize Option in List View](/files/customize-option-in-list-view.png)  


1. How to create a Custom Field
-------------------------------

1. Go to the Custom Field list and click on New.
2. **Document**: Select the Document in which you need to add the Custom Field.
3. **Label**: Enter what Label would you like to give to your Custom Field.
4. **Field Type**: ERPNext already has a set of Field Types defined which can be fetched from this drop-down menu. You can select the Type of your Custom Field from within this menu.
5. Update.

![New Custom Field](/files/new-custom-field.png)  


*Learn more about Field types* [*here*](/erpnext/field-types.html)*.*

You can also go to [Customize Form](/erpnext/customize-form) and add, edit or remove a Field in a particular Form.

![Add Custom Field From Customize Form](/files/customize-erpnext-custom-field-from-customize-form.gif)  


### 1.1. Additional Details

1. **Options**: This Field comes into picture when you would want your data to be specific or specify the data. E.g., when you have selected the Field to be a 'Select Field', you would be required to enter the selection options here.

![Custom Field with Fieldtype as Select](/files/custom-field-with-select-fieldtype.png)
2. **Fetch From**: When you want your Custom Field to be 'Link Field', you would be required to specify the Form to which this Field is to be linked. E.g., you want to create a Custom Field 'Project' in the DocType 'Item'. You would be required to enter to specify your Field Type as 'Link' and enter 'Project' in the Fetch From Field to ensure that the Field is updated with the list of all the required DocTypes.
3. **Fetch If Empty**: This check-box will ensure that this Field will be not overwritten based on Fetch From if a value already exists.
4. **Default Value**: Enter the default value of the Field which you would want to be fetched for this Field.
5. **Depends On**: You can define a condition here for the Field to be displayed. E.g., in the DocType Item, two fields 'Asset Category' and 'Asset Naming Series' will only appear if the Field 'Is Fixed Asset' is checked. The dependency condition here would be `is_fixed_asset`.

![Depends On Option](/files/custom-field-dpends-on.png)
6. **Field Description**: You can add the description of the Field here which can be displayed below this Field.

![Custom Field Description](/files/custom-field-description.png)
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

![](/files/a7pvD6Y.png)

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

![Set Customer Language](/files/set-customer-language.png)

Same way, you can also set default language in the Supplier master.

### 1.1 Print Preview in the Party's Language

In the Print Preview of a transaction, values will be translated into the party's language.

Customer Quotation print preview in customer's default language.

![Invoice in Customer Language](/files/invoice-in-customer-language.png)

Supplier Quotation print preview in supplier's default language.

### 1.2 Changing the print language in the preview

User has the option to select an alternate language on print view.

![Select Language in Invoice](/files/select-language-in-invoice.png)

## 2. Custom Translation

Users can set their custom translations using Custom Translations form. For example, if a user wants to set a description of a product in the customer's language (Spanish). For that, create a new translation with language as Spanish, enter source data and translated information.

> Home > Customization > Other > Custom Translations > New

![Translation](/files/translation.png)

The translation is applied when the user selects the language as Spanish on supplier Quotation's print preview. Note that no translation is applied for the second item's description since it wasn't created in the Translation list.

![Translation in Transaction](/files/translation-in-transaction.png)

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

![Customer Group hierarchy with Nova Commercial Customers.](https://novacompanies.m.frappe.cloud/files/customer-group-tree.png)

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

![Customer Group form showing its parent, leaf setting, defaults, accounts, and credit limits.](https://novacompanies.m.frappe.cloud/files/customer-group-details.png)

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

![Website User Signup](/files/website-login.png)

#### Step 2: Enter Customer Name and ID

![Website User Signup](/files/website-signup-details.png)

After the sign up process, an email will be sent to the customers Email Address with the password details.

## Portal Login

To login into the customer account, the customer has to use his Email Address and the password sent by ERPNext; generated through the sign-up process.

![Website User Signup](/files/website-login.png)  

## Customer Orders Invoices And Shipping Status

ERPNext Web Portal gives your customers quick access to their Orders, Invoices and Shipments Customers can check the status of their orders, invoices, and shipping status by logging on to the web.

![Customer Portal](/files/portal-menu.png)

Once an order is raised, either using the Shopping Cart or from within ERPNext, your customer can view the order and keep an eye on the billing and shipment status. When the invoice and payment against these orders are submitted, the customer can see the updated status on the portal, at a glance.

![Customer Portal](/files/website-login.png)

#### Outstanding Sales Invoice

![Customer Portal](/files/invoice-unpaid.png)

#### Paid Sales Invoice

![Customer Portal](/files/invoice-paid.png)

## Issues

The customer portal makes it very easy for a customer to raise concerns. A
simple and intuitive interface facilitates your customer to report their
concerns as Issues. They can view the complete thread of their
conversation.

#### Empty Issue List

![Issue List](/files/portal-ticket-list-empty.png)

#### New Issue

![New Issue ](/files/portal-new-ticket.png)

#### Open Issue

![Issue Raised](/files/portal-ticket-1.gif)

#### Reply on Issue

![Issue reply](/files/portal-ticket-reply.gif)

<!-- page: erpnext/erpnext__customer-provided-items.md -->
---
title: "Customer Provided Items\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customer-provided-items"
updated: "2026-03-02"
---


In Contract Manufacturing, in some cases, the Customer provides specific items as one or few of the BOM components. These items cannot be received using a 'Buying Cycle' since that will mean making Customer as a Supplier at the same time. It will also go through each doctype in the cycle.

In this feature, Customer Provided Item is received through 'Stock Entry' with type 'Material Receipt' from a 'Material Request' with type 'Customer provided'. This feature is used when someone subcontracts the manufacturing process to you and supplies the raw materials.

![Customer Provided Material Request](/files/material-request-customer-provided.png)

Here are the steps on how to setup a 'Customer Provided' item.

1. Got to [Item Doctype](/erpnext/stock) and add a new 'Customer Provided' item.

 > Home > Stock > Items and Pricing > Item

2. In the 'Purchase, Replenishment Details' section, check 'Is Customer
 Provided' and set a default Customer. Note that 'Is Purchase Item' needs to be unticked to use this feature.

 ![Item Purchase Details](/files/item-customer-provided.png)

How to receive a 'Customer Provided' Item?

1. If a 'Production Plan' is used, 'Material Request' for this item can be auto created. That is, the item to be manufactured is fetched first via Sales Order or Material Request, Items are fetched for the Work Order using the 'Get Items for Work Order' button, then click on the 'Get Raw Materials for Production' button.

 ![Material Request in Production Plan](/files/material-request-production-plan.png)

2. Once a component in a BOM is set as 'Customer Provided' and 'Material Request' is created from a 'Production Plan', it will create both 'Material Request' with type 'Purchase' and 'Customer Provided'. From there, a 'Stock Entry' with purpose 'Material Receipt' can be created.

 ![Stock Entry from Material Request](/files/create-mr-from-production-plan.png)

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

![Customer details and sales defaults for Summit Digital Stores.](https://novacompanies.m.frappe.cloud/files/customer-details-and-defaults.png)

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

![Billing and shipping addresses with the primary purchasing contact.](https://novacompanies.m.frappe.cloud/files/customer-addresses-and-contacts.png)

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

![Company receivable account and Customer credit limit.](https://novacompanies.m.frappe.cloud/files/customer-accounting-and-credit-limit.png)

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

![Loaded Cash Flow report for Nova Industries before mapping review](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-cash-flow-loaded.png)

## Create or copy a Cash Flow template

1. Open Financial Report Template.
2. Create a template, or copy an existing Cash Flow template when it is a suitable starting point.
3. Set **Report Type** to **Cash Flow**.
4. Enter a clear Template Name and keep the template enabled.

## Build and arrange the report lines

Add rows to **Report Line Items** in the exact order they should appear. Use blank or visual rows for section headings, Account Data rows for ledger-derived values, and Calculated Amount rows for subtotals. Indent supporting lines beneath their section and use stable Line References for formulas.

![Standard Cash Flow Statement IFRS template showing its ordered report line items](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)


| Example line                                    | Typical source      | Presentation                                              |
| ----------------------------------------------- | ------------------- | --------------------------------------------------------- |
| Cash flows from operating activities            | Visual or blank row | Section heading at indent level 0                         |
| Profit before tax                               | Account Data        | Period movement with the appropriate sign                 |
| Depreciation and amortisation                   | Account Data        | Indented non-cash adjustment                              |
| Operating profit before working-capital changes | Calculated Amount   | Formula based on earlier Line References                  |
| Change in trade receivables                     | Account Data        | Working-capital movement with reversed sign when required |


## Verify the custom report

![Cash Flow report after mapping with an account group opened for verification](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-ifrs-output-v2.png)



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

<!-- page: erpnext/erpnext__customise-your-items-tables-within-your-print-format-builder.md -->
---
title: "Customize tables within your Print Format Builder"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customise-your-items-tables-within-your-print-format-builder"
updated: "2026-03-02"
---

You can customize the '**Items**' column present your Print Format Builder by navigating as shown below:

  


1. Create your Customized Print Format by going into the '**Settings**' button and clicking on '**Customize**'.
2. Add a relevant name to the new customized Print format you are creating.
3. Once you are inside the New Print Format, you can click on the button '**Select columns**' in the field which says '**Items (Table)**'

  


![](/files/IIunbhn.png)

  


Open the table and you will see a list of columns that are present in the standard format of your Print Format as shown below:

  


![](/files/HCA3S5a.png)

  


  


  


The options you select here will be shown in Print Format.

Select the columns you want to keep in the Table that you are creating for your customized Print Format. You can adjust the Width and their order according to your requirement.

  


![](/files/HEUrHpC.png)

  


Once you have selected the columns you want your Print Format to have, click on '**Update**' and '**Save**' the changes you have made after further modifications in the Print format.

  


Refresh your screen and select the newly created Print Format. In this case, it is the 'Purchase Receipt'.

![](/files/nwQT6g6.png)

  


Once you click on the Print Format you newly created, the changes will be visible in the Items table.

  


![](/files/Bsp6PRj.png)

  


  


  


To see the difference between the **Standard** **Print** **Format** and the one you just created, you can simply click on the Print format Templates present.

<!-- page: erpnext/erpnext__customize-form.md -->
---
title: "Customize Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customize-form"
updated: "2026-02-27"
---

**Customize Form is a tool which enables you to make changes to a Form Type or a Document Type (DocType) on the front-end.**

It allows you to insert [Custom Fields](/erpnext/custom-field) as per your requirement or customize the properties of standard fields.

Before we venture to learn the Form Customization tool, [click here](/erpnext/doctype) to understand the architecture of forms in ERPNext. It will help you in using the Customize Form tool more efficiently.

To access Customize Form, go to:


> Home > Customization > Form Customization > Customize Form
> 
> 

You can also go to the list view of any DocType and select Customize from the Menu options.

![Customize Option in List View](/files/customize-option-in-list-view.png)  


1. How to Customize a Form
--------------------------

1. Click on Customize Form.
2. You will be redirected to a page wherein you will be asked to Enter Form Type.
3. Once you enter the Form Type in this field, the page further expands and you will be able to see multiple features.

![Select DocType in Customize Form](/files/customize-erpnext-custom-field-from-customize-form.gif)

### 1.1. Options While Customizing a Form

1. **Change Label**: This field gets fetched via Custom Translation. You can change the name of the field to suit your industry/language. E.g., if you are a services business and you want to change the Label from 'Customer' to 'Consumer', the same can be done via [Custom Translation](/erpnext/custom-translations) and the same shall be reflected here.

![Change Label](/files/customize-customize-form-label.png)

2. **Title Field**: This field can be used to generate the title while viewing the lists. Any "Data" type field can be set as the Title Field while viewing the forms in the list view. E.g., if you wish to view the list of all your employees with the Title field as the 'Employee Code' instead of Employee Name, the same can be configured here. Check our article on [Document title](/erpnext/document-title) for more information.

*Learn more about field types* [*here*](/erpnext/field-types.html)*.*

3. **Default Print Format**: For a single DocType, there could be multiple Print Formats. Here you can select the default Print Format for the selected DocType. For e.g., a company may have different Letter Heads for different purposes which can be configured through Print Formats. However, you can select two different Default Print Formats for a Sales Order and an Appointment Letter. Check [Custom Print Formats](/erpnext/print-format) for more information.

4. **Image Field**: You can select an "Attach Image" Field for your Image Field. This becomes the Image representing that particular DocType. E.g., the 'Image Field' for an Employee could be their photograph or a snapshot of their ID cards; the same can be configured here.

![Image Field in DocType](/files/customize-form-image-field.png)

5. **Max Attachments**: You can enter the maximum number of attachments that could be added to this DocType.

6. **Search Fields**: While creating any DocType, you may want to link a particular field to another DocType. For ease in selection, you can also ensure that you are able to see the value of another field of the latter DocType in the search result. For more information [click here](/erpnext/search-record-by-specific-field).

7. **Sort Field**: Records in any DocType List are generated based on the Field that you set at the Sort Field over here. E.g., for Items, if you want your list to be generated as per Item Name, you can configure the same here.

![Sort Field](/files/customize-sort-field.png)

8. **Sort Order**: You can select whether you want the Sorting to be done in Ascending Order or Descending Order. To get more understanding on Sort Field and Sort Order, check out [Customizing Sorting Order in the List View](/erpnext/customizing-sorting-order-in-the-list-view).

9. **Default Email Template**: For a single DocType, there could be multiple [Email Templates](/erpnext/email-template). Here you can set the default Email Template for the selected DocType. For example, you can set a different Default Email Template for a Sales Order and an Appointment Letter.

### 1.2. More Properties

* **Hide Copy**: This box, when checked, restricts a User to create a 'Copy' of a particular Form.

* **Is Table**: This option is available only while customizing the Forms which are present in table forms in the system. For e.g., if you are creating an Item Table to be added into a Custom Form, you can enable this option. Check out [Child Table](/erpnext/customizing-data-visibility-in-child-table) for more information.

* **Quick Entry**: Checking this box will allow you to create a 'Quick Entry' using a particular form. This means that whenever a user is creating this Form from another existing Form, a box will Pop Up which will allow the user to create the DocType by entering only the basic details. For example, check Quick Entry in [Journal Entry](/erpnext/journal-entry#11-quick-entry).

* **Track Changes**: Checking this box will ensure that any changes made by any of the users to this DocType will be tracked and displayed.

![Track Changes](/files/customize-track-changes.png)

* **Track Views**: This option will give you a trail of all the views towards this particular DocType.

* **Allow Auto-Repeat**: This option, if checked, will allow you to enable Auto Repetition of a DocType periodically. E.g., if there is a Sales Order which has to be made multiple number of times, you can enable this option and then [Set Up Auto Repeat](/erpnext/auto-repeat) for any particular Sales Order.

* **Allow Import**: This option will allow the user to Import data from any files. Check out [Data Import Tool](/erpnext/data-import) for more information.

* **Show Preview Popup**: This option was introduced in Version 12. If checked, a small popup will appear on hover of links of this document type (in list view and other link fields). This popup will contain the mandatory fields of the document and the fields for which `in_preview` is checked. Check out [Link Preview](https://erpnext.com/version-12/release-notes/features#link-preview) for more information.

Once you click Update, your Customizations will be updated to the Form.

### 1.3. Customizing the Fields

Every form in ERPNext has a standard set of fields. If you need to capture some information, but there is no standard field available for it, you can insert Custom Field in a form as per your requirement. Adding, editing or deleting of Fields can also be done here. You can also place the fields as per your requirement in the form by adding it below or above any other already present fields. [Click here](/erpnext/custom-field) for more information on Custom Fields.

### 1.4. Trim Table, Reset Layout, and Reset All Customizations

![](/files/UcB4Lpm.png)  


* **Trim Table**: To remove unused database columns (fields) that are no longer needed by a doctype. It checks for fields that have been deleted from the form but still exist in the database. If such fields are found, it allows you to permanently delete these columns. This helps keep the database clean and improves performance by removing unnecessary data.
* **Reset Layout:** To revert the form layout to its original, default state. It removes any layout customizations you have made, such as rearranging fields or changing sections, and restores the layout to how it was initially defined by the system. It is useful if your custom layout becomes too complicated or problematic, and you want to start fresh with the standard layout.
* **Reset All Customizations**: To remove all customizations made to a form, including added fields, changes to existing fields, and layout modifications. It completely removes all the custom changes you have applied to the form, resetting it to its default configuration as defined by the system. This is a drastic measure but helpful if you need to return to the system’s default form setup, perhaps because your customizations have caused issues or you want to reconfigure the form from scratch.

2. Videos
---------

<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/WSzkpPm3iIU" width="560">
</iframe>

<!-- page: erpnext/erpnext__customizing-data-visibility-in-child-table.md -->
---
title: "Data Visibility in Child Tables"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-data-visibility-in-child-table"
updated: "2026-03-04"
---


In ERPNext, there is a feature called the editable grid. This allows the user to add values in the child table without opening a dialog box/form for each row.

This is how the Quotation Item table renders value when the Editable Grid is enabled. It will have a maximum of four columns in the table.

![Child Table](/files/customize-child-table-5.png)

As per the default setting, only four columns are listed in the child table. Following is how you can add more columns in the Editable Grid itself.

For the field to be added as a column in the table, enter a value in the Column field. Also, ensure that the "Is List View" property is checked for that field.

![Child Table](/files/customize-child-table-2.png)

Based on the value in the Column field, columns will be added to the child table. Ensure that the total value added in the Column field doesn't exceed 10. Based on the Column value, the width for that column will be set.

![Child Table](/files/customize-child-table-3.png)

**Switch to Un-editable Grid**

To have more values shown in the preview of the Quotation Item table, you can disable Editable Grid for the Quotation Item DocType. Steps below.

![Child Table](/files/customize-child-table.gif)

Once Editable Grid is disabled for the Quotation Item, the values will be rendered in a preview of the Quotation Item table in the following way:

![Child Table](/files/customize-child-table-4.png)

To have a specific field's value shown in the preview, ensure that for that field, in the Customize Form tool, "In List View" property is checked.

![Child Table](/files/customize-child-table-1.png)

<!-- page: erpnext/erpnext__customizing-module-visibility.md -->
---
title: "Customizing Module Visibility\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-module-visibility"
updated: "2026-03-04"
---


**ERPNext as a system can be used by multiple businesses at every scale, Manufacturing, Education, Retail being some of the businesses benefitted the most from the usability of the system.**

Keeping in mind, the interests of all kinds of business owners, the usability of the system for different business has been mapped into different 'Modules' represented as 'Cards' in the system. Similarly the core modules in the system, such as Human Resource, Accounting, CRM etc. are also represented by different cards on the dashboard.

Every ERPNext account holder has the option of customizing the visibility of the different modules based on their business case.

*In Version 12, you can go to Show / Hide Modules on the top right corner of the home screen for checking visibility of modules.**

![Module Visibility](/files/customize-module-visibility-2.png)
![Module Visibility](/files/customize-module-visibility.gif)

> Note: Modules are automatically hidden for users that have no permissions on the documents within that module. For example, if a User has no permissions on Purchase Order, Purchase Request, Supplier, the “Buying” module will automatically hidden for that User.

If you have permissions to a specific module, but it is still not visible, the following could be the possible reasons for it.

Let's consider a scenario that a user has the permission for the Website module, but is not able to access it.

As a basic requirement, ensure that the "Website Manager" role is assigned to that user. It is a standard Role that grants permission on the Website module. If permissions have been customized in your account, check Role Permission Manager to know which Role has permission on Website, and then check if the same Role is assigned to the User.

![Module Visibility](/files/customize-module-visibility-4.png)

Further, you should also check if the under the settings, 'Allow Modules', the required module has been enabled for the user

![Module Visibility](/files/customize-module-visibility-1.png)

Reload tab of your ERPNext account and the changes made will be applied and will be visible in the system.

<!-- page: erpnext/erpnext__customizing-sorting-order-in-the-list-view.md -->
---
title: "Sorting Order in List View"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-sorting-order-in-the-list-view"
updated: "2026-03-04"
---


**Question:** I want records in my Item List sorted based on Descending Order of Item Code.

**Answers:** Following are the steps to customize Sort Order for the Item master. These steps will be applicable for customizing Sort Order for the other documents as well.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Select DocType

Select document type for which Sort Order is to be customized.

![Sort Order field](/files/customize-sorting-order-2.png)

#### Step 3: Update Sort Details

In the Customize Form, you will find these fields.

![Sort Order Field](/files/customize-sort-field.png)
![Sort Order field](/files/customize-sorting-order-1.png)

1. Sort Field: Select the Field based on which sorting will be done. It will be "Item_Code" field in the scenario.
2. Sort Order: Sort Order will be two possible options, **Asc** for ascending, and **Desc** for descending.

<!-- page: erpnext/erpnext__daily-depreciation.md -->
---
title: "Daily Depreciation Calculation | ERPNext Documentation"
description: "Configure daily pro-rata depreciation in ERPNext and understand how actual days affect each period."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/daily-depreciation"
updated: "2026-08-15"
---

Imagine Nova Industries starts using a machine on 20 March. A monthly depreciation calculation may treat March like a full month, even though the machine was used for only 12 days. That small difference can matter when assets are added or sold throughout the year.



Daily Depreciation calculates the expense using the actual number of days the asset was available for use. It gives the accountant a more precise schedule when company policy requires depreciation to follow calendar days.

## Enable daily pro-rata calculation

Open the relevant Asset Category or Asset Finance Book row, enable **Daily Pro Rata Based**, and confirm the depreciation start date. ERPNext then uses actual day counts instead of equal periodic amounts.

![Finance Book settings used for daily depreciation](https://novacompanies.m.frappe.cloud/files/09-production-asset-depreciation.png)

## How the amount is determined

ERPNext calculates the daily amount from the depreciable value and schedule duration, then multiplies it by the eligible days in each period. Leap years and unequal month lengths can make individual rows differ while the total still reconciles.

## Verify the schedule

Check the first and last rows, the total depreciation, and the expected value after useful life. The Asset Depreciations and Balances report should reconcile the opening value, booked depreciation, and closing value.

![Asset Depreciations and Balances report](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### The first period is smaller than expected

Check the Available for Use Date and depreciation start date. A partial first period is normal with daily proration.

### The daily amounts do not match a simple monthly division

Daily calculation follows actual days, so months and leap years do not always carry equal depreciation.

## Frequently asked questions

### Is daily pro-rata mandatory?

In ERPNext, no. Use it only when the accounting policy requires actual-day allocation.

### Does it change the total depreciable value?

In ERPNext, no. It changes timing across rows, not the total value to be depreciated.

### Can different Finance Books use different pro-rata settings?

In ERPNext, yes. Configure the setting independently in each Finance Book row.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__data-export.md -->
---
title: "Data Export"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-export"
updated: "2026-03-02"
---

**'Data Export' helps you extract data from any DocTypes to a CSV or an Excel format.**

To access Data Export, go here.

> Home > Data Export

### How to Use Data Export

1. Go to the 'Data Export' DocType.
2. Select the DocType from which the data is to be extracted.
3. Select the file format whether CSV or Excel.
4. Tick the checkbox if you want to export the data without any header notes and column descriptions.
5. Select the fields to export; the red ones are mandatory.
6. You can also add filters to select only specific data. For example, 'Territory = Asia' will export all Customers whose Territory is set as 'Asia'.
7. Click on Export to download the file.

![](/files/image9dfe7c.png)

After exporting data, you can use the same file to import data using [Data Import](/erpnext/data-import).

<!-- page: erpnext/erpnext__data-import.md -->
---
title: "Data Import"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-import"
updated: "2026-04-27"
---

**The Data Import tool in ERPNext allows users to import records into the system using CSV or Excel files.** 

It provides a convenient way to upload or update large volumes of data at once, especially master data, without the need for manual entry.



This tool is commonly used during initial system setup, data migration, or when bulk updates are required. By using the Data Import tool, users can ensure faster data entry while maintaining consistency across records.



To access the Data Import tool, navigate to:

> Home > Data

‎ Or go to the Document you want to import and click on Menu > Import



Before starting the import process, make sure that all required data is prepared correctly and follows the expected format. The Data Import tool supports two main operations:

## Inserting New Records

The Data Import Tool in ERPNext allows users to upload bulk records into the system using a predefined template. This document outlines the step-by-step process for importing new records.

![](https://docs.frappe.io/files/imagebfd4b7.png)

1. Navigate to Data Import
2. Select the Document Type and the Import Type as *Insert New Records*.
3. Click on Save and then download the template.

### Download Template

We have an option to download the template to insert the records/update the records

1. Clicking on Download Template opens a dialog box

![](/files/image79c0b4.png)
*Download Template Dialog box*

> While inserting new records, the template should be blank. If you have a few records in your system, you can select Export Type as "5 Records" to see the format in which you have to enter the data in the template.

4. *After you choose the export type, every field appears in the list. **Mandatory** fields show a red * next to the name. **Conditional** fields (for example **Depends On** or autoname-related) show a small **info** icon—point at it to read the note.*
5. *Fields that are ticked but not mandatory are ones with **Include in Import Template** on—set on the **DocType** or in **Customize Form**—so they show in the list by default without being required.*
6. Click Export and get the exported file.
7. Now, save your template as an Excel or Comma-Separated Values (CSV) file.

> *You can leave the ID column as blank while inserting new records.* When you import this template, each row will make a record in the system.

8. Once the template is updated and ready with the data, we can import it.

### Importing a Template

Once the data has been added to the downloaded template, the following steps are followed:

1. After updating your template file, go back to the Data Import form and attach the file by clicking on the **Attach** button.
  ![](/files/imagef9ce89.png)
  *Attaching file for import*
2. Select the template file and click on **Upload**, after the upload is successful, click on **Start Import**. There are various ways to import the data; you can refer [here](https://docs.frappe.io/erpnext/data-import#ways-to-import-data)
3. Once the Sheet is uploaded, the system validates the sheet and gives the result on screen before importing the data
  ![](/files/image799c07.png)
4. If there are any errors in your template, they will be shown in the Warnings section. The warnings will be categorized by Row or Column with their number so that you can easily track them down in the template and resolve them. You must resolve all the warnings before you can import the data.
5. After you have resolved the warnings, click on **Start Import** again to import the data. On successful import of the data, you'll see a log of each record that was created in the Import Log section.

## Validations and Errors in Importing

### Duplicate Name

In case we try to add a record with a duplicate name, it will throw an error like this

![](/files/imagebff69b.png)
*Duplicate Name Error*

### Mapping of missed columns

When we add additional columns while downloading the template, or we have renamed a column in the template we are importing, it may throw an error about not being able to match the columns. 



![](/files/Screen Recording 2026-02-18 at 9.43.24 PM.mov)



















> To resolve this, we can click on the **map columns** and manually map the columns to the corresponding columns in the Document. 

## Importing child records

Data in ERPNext is stored in tables like a spreadsheet with columns and rows of data. Each form likes Sales Order, has multiple fields like Customer, Company, etc. It also has tables like the item table, tax table, etc. In Data Import, the set of fields in the Sales Order is treated as the main table, and the rows inside the child table (item table) are treated as the child table for data import.



Each form in ERPNext can have multiple child tables associated with it. The child tables are linked to the parent tables and are implemented where there are multiple values for any property. For example, an Item can have multiple prices, a Sales Invoice has multiple Items, Taxes, and so on.



When you export a document with child tables, for e.g., each child row will appear on a separate row, but it is associated with a single parent row. The subsequent values in the parent columns will remain blank. You must ensure that this order is not broken when you are importing it via Data Import.

---

![](/files/imagedf8b35.png)
*Child records importing*

## Updating Records

Let's say you want to update Customer data in bulk in your system. The first step is to download the template with the data.

1. We start by downloading the template. While doing this, since we want to update, we can use filters to extract the exact records and import them back for updating.
2. First, we select the document type and the import type as **Update Existing Records,** and Save
3. When we try to download the template, we can apply filters, something like this
  ![](/files/image0baff8.png)
4. We click on **Export.**
5. Now, based on the template, the existing records look like this:

![](/files/image7a4518.png)

:::tip
While exporting records for updating them, ensure that the ID column is exported and is untouched. The values in the ID column are used to identify the records in the system. You can update the values in other columns but not in the ID column. If you remove some child table row, the system will consider that the row is supposed to be deleted.
:::

















6. Now, change the values in your template and save the file as Excel or CSV.

![](/files/imageebf859.png)

## Ways to Import Data

### Import from Google Sheets

You can import data directly from Google Sheets by following these steps:

1. Upload or copy your template into Google Sheets.
2. Enter or update your data in the sheet.
3. Ensure the Google Sheet is set to **Public** access.
4. Once confirmed, use the Google Sheets link in the Data Import page to proceed with the import.

![](/files/imaged49cb3.png)
*Google sheet Data File*

:::tip
To verify that the sheet is publicly accessible, open the Google Sheets URL in an incognito/private browser window. If the file opens without requiring login access, it is correctly configured.
:::















![](/files/imagebbb644.png)
*Post Import using google sheets*

### Import from the file system

1. On the **Data Import Page**, there are two available options:
  - Attach File
  - Import Using Google Sheets
    ![](/files/imageb8e55f.png)
2. After clicking **Attach**, you will see multiple upload options:
  ![](/files/imageb4e113.png)
3. Available Upload Options

- **My Device**  
Upload a file directly from your local computer.
- **Library**  
Select a file that has already been uploaded and stored in the system’s file library.
- **Link**  
Provide a direct web URL to a file hosted online.

4. Choose the appropriate option based on where your file is stored, then proceed with the upload.

### Submit After Import

In ERPNext document types are mainly of two types - masters and transactions. The masters are records like Customer and Task which can only be saved not submitted. Transactions like Sales Orders, Purchase Invoices are submittable documents and can be submitted.

When you select a submittable document type for Import, you can tick **Submit After Import** to submit the document after it is imported.

### Don't Send Emails

Let's say you have created a Notification in your system and whenever a Lead is created an email is sent. Now, if you are bulk importing Leads then a lot of emails will be sent, which may not be desired. You can disable this option to avoid sending emails.

## Additional Notes

---

### Upload Limit

There is no hard limit on the number of records that can be imported. But you must try and upload only a few thousand records at a time. Importing a large number of records (let's say 50,000) might slow down the system considerably for the users that are using the system.

### CSV Files

A CSV (Comma Separated Value) file is a data file that you can upload into ERPNext to update various data. Any spreadsheet file from popular spreadsheet applications like MS Excel or Open Office Spreadsheet can be saved as a CSV file.

If you are using Microsoft Excel and using non-English characters, make sure to save your file encoded as UTF-8.

For older versions of Excel, there is no clear way of saving as UTF-8. So save your file as CSV, then open it in Notepad, then save as “UTF-8”. (Or upgrade your Excel!)

<!-- page: erpnext/erpnext__data-management__introduction.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-management/introduction"
updated: "2026-02-23"
---

Data management is essential for effectively using an ERP system. ERP software integrates data from different business functions, such as finance, inventory, sales, and human resources, into a single system. For the system to work reliably, the data must be accurate, consistent, and properly maintained.



In this tutorial, we will learn how users can import data into ERPNext from different sources (like spreadsheet), and ways to export data out of ERPNext.

<!-- page: erpnext/erpnext__datev-integration.md -->
---
title: "DATEV Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/datev-integration"
updated: "2026-07-04"
---

## Overview

The DATEV Integration app connects ERPNext with DATEV workflows used by German accounting teams and tax consultants. The app is listed on Frappe Cloud Marketplace as [DATEV Integration](https://cloud.frappe.io/marketplace/apps/erpnext_datev) and is published by ALYF GmbH, Raffael's team.

## What It Does

- **DATEV Unternehmen Online:** Sends submitted vouchers to DATEV Unternehmen Online by email. Outgoing vouchers can be converted to PDF, while incoming vouchers can send attached files.
- **DATEV CSV Export:** Exports raw General Ledger entries from ERPNext in DATEV CSV format.
- **Tax consultant handoff:** Exports the DATEV report with master data as a ZIP file for import into the tax consultant's DATEV system.

## Setup Summary

Configure DATEV Settings with the client number, tax consultant number, and temporary contra account. For DATEV Unternehmen Online, enable the integration, choose the sending email account, select the voucher type, add the target email address from DATEV, and choose whether to send attachments or generated prints.

## Compatibility

The marketplace listing shows support for ERPNext versions 13, 14, 15, and 16. Test the integration on a staging site before using it for accounting handoff.

## Links

- [DATEV Integration on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/erpnext_datev)

## Disclaimer

DATEV and DATEV Unternehmen Online are trademarks of DATEV eG. The marketplace listing notes that this integration is not approved or endorsed by DATEV eG.

<!-- page: erpnext/erpnext__debit-note-for-price-adjustment.md -->
---
title: "Debit Note for Price Adjustment | ERPNext Documentation"
description: "Reduce a submitted ERPNext Purchase Invoice when a Supplier lowers the agreed price without returning goods."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/debit-note-for-price-adjustment"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, invoiced 10 phones at $520 each. After the Purchase Invoice was submitted, both companies agreed that the correct price was $500 each. No phones are being returned, but Nova Industries should owe the supplier $200 less.



A Debit Note for price adjustment records only that value correction. It reduces the payable and adjusts the relevant expense or asset value without creating a stock return.



Use this workflow when a supplier reduces an agreed price after invoicing and the physical quantity remains unchanged.



## Before you begin

Confirm the revised price with the Supplier and calculate the reduction per unit.

Example:

- original invoice: 10 phones at $520 each;
- revised price: $500 each;
- price reduction: $20 per phone;
- total Debit Note: $200.

The quantity of goods owned by the Company does not change. Therefore, do not select **Update Stock** for this adjustment.

## Create a Debit Note for price adjustment

1. Open the submitted Purchase Invoice.
2. Select **Create &gt; Return / Debit Note**.
3. Confirm that **Is Return (Debit Note)** is selected and **Return Against Purchase Invoice** references the original invoice.

![Price adjustment Debit Note linked to the original Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-08-rate-adjustment-setting.png)

4. Remove Items that are not part of the price correction.
5. Open the affected Item row using its pencil icon.
6. Enter the full original billed quantity as a negative quantity. For the example, enter `-10`.

![Full original quantity entered as a negative quantity](https://novacompanies.m.frappe.cloud/files/purchase-payables-09-rate-adjustment-full-quantity.png)

7. Enter only the price reduction per unit in **Rate**, not the revised unit price. For the example, enter `$20`, which produces an amount of `-$200`.

![Per-unit price difference entered as the Debit Note rate](https://novacompanies.m.frappe.cloud/files/purchase-payables-10-rate-adjustment-difference.png)

8. Leave **Update Stock** clear because the goods are not being returned.
9. Review taxes. Adjust them only when the Supplier's credit document and applicable tax rules require it.
10. Save and submit the Debit Note.

## Why the full quantity and difference rate are used

The Debit Note amount is calculated as quantity multiplied by rate. Using the full affected quantity and only the reduction per unit produces the exact credit:

`10 units × $20 reduction = $200`

Because the quantity is negative on a return Purchase Invoice, the document reduces the payable by $200. It does not mean that ten units were physically returned, provided **Update Stock** remains clear.

Do not enter the revised price of $500 as the Debit Note rate. That would reduce the invoice by $5,000 instead of the intended $200.

## Important fields and what they mean


| Field                           | What it controls                                                        |
| ------------------------------- | ----------------------------------------------------------------------- |
| Is Return (Debit Note)          | Makes the Purchase Invoice a reducing document.                         |
| Return Against Purchase Invoice | Connects the adjustment to the original Supplier invoice.               |
| Accepted Qty                    | Use the negative full quantity affected by the price change.            |
| Rate                            | Enter the reduction per unit, not the original or revised unit price.   |
| Amount                          | The total reduction. Verify it against the Supplier's credit document.  |
| Update Stock                    | Keep this clear for a price-only adjustment.                            |
| Posting Date                    | Determines the accounting period in which the adjustment is recognized. |
| Taxes and Charges               | Reverses applicable tax amounts when included in the adjustment.        |


## Submit and verify

After submission, check:

- the Debit Note total equals the Supplier's agreed credit;
- the original Purchase Invoice outstanding amount is reduced correctly;
- Item stock quantity is unchanged;
- the Supplier balance in [Accounts Payable](/erpnext/accounts-payable) reflects the adjustment;
- the General Ledger shows the intended reduction in payable and expense, asset, or receipt-clearing value.

If the original invoice has already been paid, the Debit Note creates a Supplier credit. Allocate it to a future invoice through [Payment Reconciliation](/erpnext/payment-reconciliation), or record the Supplier refund using the correct payment workflow.

## Troubleshooting

### The Debit Note amount is too large

The revised price may have been entered instead of the price difference. Calculate `original price - revised price` and use that amount as the Rate.

### Stock quantity changed

The Debit Note was submitted with **Update Stock** selected. Review whether cancellation and amendment are allowed in the posting period, then correct the document using your approved process.

### The original invoice still shows the wrong outstanding amount

Verify the **Return Against Purchase Invoice** reference and review existing payments and reconciliations. Use the invoice and Debit Note Payment Ledger entries to trace the balance.

### Only some units received the price reduction

Use the negative number of affected units, not the full invoice quantity. For example, if only four of ten units receive a $20 reduction, enter quantity `-4` and rate `$20`.

## Frequently asked questions

### Is this the same as returning goods?

It is different. A price adjustment changes the payable but keeps stock unchanged. A physical return also reverses the relevant stock movement.

### Can I cancel and amend the original Purchase Invoice instead?

Only when your permissions, posting period, audit policy, and linked documents allow it. A Debit Note usually provides the clearer audit trail after the original invoice has been accepted or posted.

### What document should I request from the Supplier?

Retain the Supplier's credit note, revised invoice, or other approved evidence that explains the price reduction and tax treatment.

## Related topics

- [Purchase Invoice](/erpnext/purchase-invoice)
- [Debit Note](/erpnext/debit-note)
- [Accounts Payable](/erpnext/accounts-payable)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)

<!-- page: erpnext/erpnext__debit-note.md -->
---
title: "Debit Note | ERPNext Documentation"
description: "Create and submit an ERPNext Debit Note to return purchases or reduce a Supplier invoice."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/debit-note"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, delivered phone batteries, but two were damaged and must be returned. Nova Industries needs to reduce what it owes the supplier without changing or deleting the original Purchase Invoice.



A Debit Note records that supplier return or credit as a separate return Purchase Invoice. It reverses the relevant payable, tax, expense, and stock effects while preserving the original transaction.



Use a Debit Note when goods are returned to a supplier, a supplier invoice must be reduced, or a supplier credit must be recorded against an earlier Purchase Invoice.



## Before you begin

You need a submitted [Purchase Invoice](/erpnext/purchase-invoice). Confirm:

- which Items and quantities are being returned;
- whether ERPNext must also reverse stock;
- whether a linked Purchase Receipt exists;
- whether the Supplier has already been paid;
- the posting date on which the return should affect the ledgers.

If you are correcting only the price while keeping the goods, follow [Debit Note for price adjustment](/erpnext/debit-note-for-price-adjustment).

## Create a Debit Note

1. Open the submitted Purchase Invoice that must be reduced.
2. Select **Create &gt; Return / Debit Note**.

![Return or Debit Note action on a submitted Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-05-create-debit-note.png)

3. ERPNext creates a new Purchase Invoice with **Is Return (Debit Note)** selected and **Return Against Purchase Invoice** linked to the original invoice. Verify both fields before changing the Items.

![Debit Note return setting and original Purchase Invoice reference](https://novacompanies.m.frappe.cloud/files/purchase-payables-06-debit-note-reference.png)

4. Keep only the Items being returned. Remove unaffected rows.
5. Enter the return quantity as a negative number. For example, use `-2` to return two units from an original quantity of ten.
6. Select the pencil icon on the Item row to open the full row editor. Verify the returned quantity, original rate, Warehouse, expense account, Cost Center, and source-document references.

![Negative quantity and original rate in the Debit Note Item row](https://novacompanies.m.frappe.cloud/files/purchase-payables-07-debit-note-negative-quantity.png)

7. If the return must move stock out, select **Update Stock** and verify the Warehouse. Leave it clear when stock was already returned through a Purchase Return against the Purchase Receipt.
8. Review taxes and totals. A return should have negative amounts.
9. Save and submit the Debit Note.

## What the Debit Note updates

On submission, ERPNext reduces the Supplier payable and reverses the relevant expense, asset, tax, or receipt-clearing values. When **Update Stock** is selected, it also posts the stock movement out of the selected Warehouse.

The original Purchase Invoice remains submitted. Its outstanding amount is reduced by the Debit Note. This maintains a clear audit trail instead of rewriting the original bill.

If the Supplier invoice was unpaid, the Debit Note reduces the amount to pay. If the Supplier was already paid, the result may be a Supplier credit that can be allocated against another invoice or settled through a payment. Use [Payment Reconciliation](/erpnext/payment-reconciliation) when allocations need correction.

## Important fields and what they mean


| Field                                    | What it controls                                                                                                                                                |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Is Return (Debit Note)                   | Marks the Purchase Invoice as a return and changes amounts to reversal values.                                                                                  |
| Return Against Purchase Invoice          | Links the Debit Note to the original invoice and supports outstanding and document-status updates.                                                              |
| Update Outstanding for Self              | Updates the Debit Note's own outstanding amount even when it references an original invoice. Use the default unless your accounting process requires otherwise. |
| Update Billed Amount in Purchase Order   | Reduces the billed amount on the linked Purchase Order when applicable.                                                                                         |
| Update Billed Amount in Purchase Receipt | Reduces the billed amount on the linked Purchase Receipt when applicable.                                                                                       |
| Update Stock                             | Posts the physical purchase return from the Warehouse through this document.                                                                                    |
| Items                                    | Identifies what is returned. Quantities and amounts are normally negative.                                                                                      |
| Posting Date and Time                    | Determines the accounting and optional stock period for the return.                                                                                             |
| Credit To                                | The Supplier payable account affected by the Debit Note.                                                                                                        |


## Partial returns

You can return selected Items or only part of an Item quantity. Retain the original rate unless the Debit Note is specifically a price adjustment. ERPNext limits the return against the quantities and amounts available on the referenced document.

Example: an invoice contains ten phones at $520 each. If two damaged phones are returned, enter quantity `-2` at rate `$520`. The Debit Note total is `$1,040` before tax, and the original payable is reduced by that amount.

## Submit and next steps

After submission:

- check the original invoice's outstanding amount;
- review the Supplier balance in [Accounts Payable](/erpnext/accounts-payable);
- inspect the General Ledger entries from **View &gt; Accounting Ledger**;
- inspect the Stock Ledger when **Update Stock** was enabled;
- allocate any remaining Supplier credit to a later Purchase Invoice or payment.

## Status


| Status   | Meaning                                                                             |
| -------- | ----------------------------------------------------------------------------------- |
| Draft    | The Debit Note has not affected ledgers.                                            |
| Return   | The return Purchase Invoice is submitted.                                           |
| Unpaid   | The submitted Debit Note has an outstanding credit that is not allocated.           |
| Paid     | The Debit Note has been fully allocated or settled.                                 |
| Canceled | Its accounting and stock effect has been reversed under ERPNext cancellation rules. |


## Troubleshooting

### The return quantity is rejected

Confirm that the quantity is negative, does not exceed the remaining returnable quantity, and references the correct original Item row.

### Stock is reversed twice

Use either a stock-updating Debit Note or a Purchase Return against the Purchase Receipt for the same physical movement. Do not post both for the same returned units.

### The original invoice outstanding amount did not change as expected

Check **Return Against Purchase Invoice**, the update-outstanding option, existing payments, and reconciliations. Then review the Payment Ledger entries for both documents.

### The Supplier was already paid

The Debit Note creates a Supplier credit. Reconcile it against a later invoice or record the appropriate refund payment according to your process.

## Frequently asked questions

### Can I create a Debit Note without an original Purchase Invoice?

ERPNext can support an unlinked return in some configurations, but linking the original invoice gives better quantity validation, outstanding updates, and audit evidence. Prefer the linked workflow.

### Can a Debit Note return only one line?

You can. Remove all unaffected rows and retain only the returned line and quantity.

### Does every Debit Note update stock?

It does not. Stock changes only when the document is configured to update stock. A price-only adjustment should not move stock.

## Related topics

- [Purchase Invoice](/erpnext/purchase-invoice)
- [Debit Note for price adjustment](/erpnext/debit-note-for-price-adjustment)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounts Payable](/erpnext/accounts-payable)

<!-- page: erpnext/erpnext__default-receivable-payable-account.md -->
---
title: "Default Receivable / Payable Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/default-receivable-payable-account"
updated: "2026-08-14"
---

ERPNext normally tracks all customer balances in a shared receivable control account and all supplier balances in a shared payable control account. The party on each invoice and payment provides the customer-level or supplier-level detail, so the Chart of Accounts does not need a separate ledger account for every party.



At Nova Industries, invoices for Northstar Retail, Bluewave Systems, and Cedar Commerce can all post to **Debtors - NI**. The [Accounts Receivable report](/erpnext/accounts-receivable) still shows what each customer owes, while the [General Ledger](/erpnext/general-ledger) keeps one reconcilable control balance.



Use a party-specific receivable or payable account only when there is a real accounting reason, such as a different currency, company, legal classification, or reporting requirement. Creating one account per customer or supplier usually makes the Chart of Accounts longer without improving party-level reporting.

## How the default accounts work

The [Company](/erpnext/company) record supplies the normal receivable and payable accounts. ERPNext uses them when a [Customer](/erpnext/customer) or [Supplier](/erpnext/supplier) does not define a more specific account.




| Transaction      | Control account                                              | Party detail         |
| ---------------- | ------------------------------------------------------------ | -------------------- |
| Sales Invoice    | Default Receivable Account                                   | Customer             |
| Purchase Invoice | Default Payable Account                                      | Supplier             |
| Payment Entry    | The receivable or payable account used by the linked invoice | Customer or Supplier |


When an invoice is submitted, the account balance and the party balance are updated together. This is why the [Accounts Receivable and Payable reports](/erpnext/accounts-receivable-and-payable) can show party-wise outstanding amounts even when many parties share one ledger account.

## Configure the company defaults

1. Open the Company record.
2. Go to the **Accounts** tab.
3. Set **Default Receivable Account** to a ledger account whose account type is **Receivable**.
4. Set **Default Payable Account** to a ledger account whose account type is **Payable**.
5. Save the Company.

The accounts must belong to the same company and must not be group accounts. Create or review them in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Assign a different account to one party

A party-specific account overrides the Company default for that Customer or Supplier.

1. Open the Customer or Supplier.
2. Open the **Accounting** section.
3. Add a row for the Company and select the required receivable or payable account.
4. Save the party.

![Customer-specific receivable account with the native modal overlay visible](/files/customer-default-eur-receivable-native-overlay.webp)



Use this option selectively. For example, Nova Industries may use a USD receivable account for domestic customers and an EUR receivable account for a European customer because the account currency must match the transaction workflow. It should not create separate accounts merely to see customer-wise balances.

## Which account does ERPNext select?

ERPNext first checks whether the party has an account for the selected Company. If it does, that account is used. Otherwise, ERPNext uses the Company default. A value deliberately selected on the transaction can provide a more specific choice when the document permits it.



Before submitting an invoice, confirm the receivable or payable account when the party uses a special currency or reporting treatment. After submission, review the resulting posting through **View Ledger** or the General Ledger report.

## Troubleshooting

### The required account is not available

Confirm that it belongs to the transaction Company, is a ledger account, is enabled, and has the correct Receivable or Payable account type. Also check the account currency.

### An invoice selects an unexpected account

Review the Accounting section of the Customer or Supplier. A party-specific row takes precedence over the Company default. Remove or correct the row if it is no longer required.

### Party balances do not agree with the control account

Compare the Accounts Receivable or Accounts Payable report with the General Ledger using the same Company and posting date. Check opening entries, Journal Entries with a party, cancellations, and reconciliation before posting an adjustment.

## Frequently asked questions

### Do I need a separate receivable account for every customer?

Use the Customer dimension in invoices, payments, the Payment Ledger, and receivable reports to see customer-level balances. A shared control account is the normal setup.

### Can multiple companies share the same receivable account?

Ledger accounts belong to one Company. Configure receivable and payable defaults separately for every Company.

### Can a customer use more than one receivable account?

It can have company-specific accounts, and different account currencies may require separate accounting arrangements. Keep the design limited to genuine accounting needs so reconciliation remains clear.

## Related topics

- [Company accounting defaults](/erpnext/company-accounting-defaults)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__deferred-accounting.md -->
---
title: "Deferred Accounting | ERPNext Documentation"
description: "Understand how ERPNext defers invoice income and expense, recognizes it over a service period, and reports the remaining balance."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-accounting"
updated: "2026-08-03"
---

Deferred accounting separates the date you invoice from the period in which you earn revenue or consume an expense. In ERPNext, a qualifying invoice amount is first posted to a balance-sheet account. ERPNext then moves the appropriate portion to income or expense over the service period.

Use it for annual support contracts, warranties, hosting plans, insurance paid in advance, software subscriptions, rent paid ahead, or another service that covers more than one accounting period. Do not use it merely because an invoice will be paid later. Credit terms change when cash is due; deferred accounting changes when income or expense is recognized.

## How deferred accounting works

The same pattern applies on both sides of the business:


| Flow                                          | At invoice submission                                             | During the service period                 |
| --------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| [Deferred Revenue](/erpnext/deferred-revenue) | Credit a deferred revenue liability instead of the Income Account | Debit deferred revenue and credit income  |
| [Deferred Expense](/erpnext/deferred-expense) | Debit a deferred expense asset instead of the Expense Head        | Credit deferred expense and debit expense |


For example, Nova Electronics Trading invoices $1,200 for a 12-month extended warranty. The invoice creates the Customer receivable, but the $1,200 is initially credited to **Customer Advances - NET**, a liability used for the example. ERPNext then recognizes the amount against **Service - NET** over the warranty period.

On the purchase side, a $1,200 annual software subscription is first debited to **Prepaid Expenses - NET**. ERPNext then recognizes it against **Software Subscription Expenses - NET** as the subscription is consumed.

The exact accounts must match your Chart of Accounts and accounting policy. A deferred revenue account is normally a liability. A deferred expense account is normally an asset.

## Before you begin

Prepare the following:

- A Company with the correct [Chart of Accounts](/erpnext/chart-of-accounts).
- A deferred revenue liability account and/or a deferred expense asset account.
- The final income or expense account that should receive each recognition entry.
- A non-stock [Item](/erpnext/item) representing the service, plan, warranty, or prepaid cost.
- A clear service start date and service end date.
- A decision on whether recognition should be calculated by days or by months.

Review the treatment with your accountant. Deferred accounting controls recognition timing, and the appropriate period may differ from the invoice, payment, contract, or delivery dates.

## Configure deferred accounting

Open **Accounts Settings** and find **Deferred Accounting Settings** under **Invoice and Billing**.



![Deferred accounting settings](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-accounts-settings-deferred-accounting.png)


| Setting                                         | What it controls                                                                                                            |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Book Deferred entries based on                  | Selects **Days** or **Months** as the recognition basis                                                                     |
| Automatically process deferred Accounting entry | Allows the scheduled process to book eligible recognition entries                                                           |
| Book deferred entries via Journal Entry         | Creates [Journal Entry](/erpnext/journal-entry) documents instead of posting the recognition directly to the General Ledger |
| Submit Journal entries                          | Automatically submits generated Journal Entries; if cleared, they remain Draft for review                                   |


### Days or months

With **Days**, ERPNext allocates the amount according to the number of service days falling in each period. This produces different amounts for months of different lengths.

The original example remains useful: if $12,000 covers 12 months, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact service dates. The total across the complete period remains $12,000.

With **Months**, a complete 12-month term normally recognizes $1,000 per month. ERPNext still prorates a partial first or last month when the service does not cover the whole month.

Choose one policy and apply it consistently. Changing the setting affects how future processing calculates eligible schedules.

### Direct ledger entries or Journal Entries

Direct posting creates the recognition entries without a separate Journal Entry document. This is simpler when your team trusts the automated calculation and reviews results through the [General Ledger](/erpnext/general-ledger) and deferred report.

Journal Entry posting gives each recognition batch a document that can be reviewed. When **Submit Journal entries** is not selected, generated Journal Entries remain Draft and do not affect the ledger until someone submits them. This adds control but also creates an operational review step.

## Enable the Item

Open the service Item and select **Enable Deferred Revenue**, **Enable Deferred Expense**, or both when the same service can be sold and purchased. The optional month counts can supply a standard duration, but the invoice row's service dates determine the actual recognition period.



![Enable deferred accounting on the Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

Enabling an Item does not post anything. The accounting effect begins when a submitted Sales Invoice or Purchase Invoice contains an enabled row with a valid deferred account and service period.

## Complete the invoice row

In a [Sales Invoice](/erpnext/sales-invoice) or [Purchase Invoice](/erpnext/purchase-invoice), add the Item, then select the pencil icon on the Items row. Complete the deferred account and the **Service Start Date** and **Service End Date** in the row editor.

The service period belongs to each row. This allows one invoice to contain items with different recognition periods. Review every deferred row instead of assuming the dates apply to the whole invoice.

## Process recognition entries

When automatic processing is enabled, ERPNext runs deferred accounting through a background process. You can also create and submit a [Process Deferred Accounting](/erpnext/process-deferred-accounting) document manually.

Select **Income** for deferred revenue or **Expense** for deferred expense. Set the posting date and the service date range that should be processed. Optionally select one deferred account to limit the run.

The process evaluates eligible submitted invoices and creates the recognition entries allowed by the selected settings. A Process Deferred Accounting record is also the processing log, so keep it available for audit and troubleshooting.

## Verify the result

After processing, check all three layers:

1. Open the invoice and confirm the deferred account and service dates on each affected row.
2. Review the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report) for invoiced, recognized, and pending amounts.
3. Open the General Ledger for the deferred account and the final income or expense account.

The deferred balance should reduce as recognition is booked. The final income or expense should increase by the same amount. Across the full service term, the total recognized amount should equal the eligible invoice amount, subject to cancellations, returns, credits, and rounding.

## Corrections and changes

Correct a Draft invoice before submission whenever possible. After submission, use the supported cancellation and amendment process rather than editing ledger entries directly. If the service stops early, use the row's **Service Stop Date** where the transaction and version support it, then process and verify the revised schedule.

Do not post a manual balancing Journal Entry merely to make the deferred report look correct. First find whether the cause is a missing account, wrong service date, unsubmitted generated Journal Entry, disabled automatic processing, an excluded processing range, or an amended invoice.

## Troubleshooting


| Problem                                      | What to check                                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| No deferred fields appear on the invoice row | Confirm the Item has the applicable deferred option enabled and reopen the row editor              |
| Full income or expense posts immediately     | Check the row-level enable option, deferred account, and service dates before submission           |
| No monthly entry appears                     | Check automatic processing, background jobs, the processing range, and Draft Journal Entries       |
| Amounts differ by month                      | Confirm whether **Days** is selected; different month lengths produce different allocations        |
| Deferred report and ledger differ            | Check document status, filters, service dates, generated entries, cancellations, and posting dates |


## FAQs

### Is deferred accounting the same as an advance payment?

No, an advance payment records cash received or paid before it is allocated. Deferred accounting controls when invoice income or expense is recognized. A transaction can involve both concepts, but they solve different accounting problems.

### Can I defer only one line on an invoice?

Yes, deferred controls and service dates are stored on each invoice Item row. Other rows can post normally.

### Should I use days or months?

Use the basis required by your accounting policy. Days follows the exact service days in each period. Months produces equal complete-month allocations and prorates partial months.

### Why are generated Journal Entries still Draft?

**Book deferred entries via Journal Entry** is enabled but **Submit Journal entries** is not. Review and submit the generated documents, or change the setting only after approving the control implications.

### Can I change the account or service dates after submission?

Use the supported cancellation, amendment, or service-stop workflow. Directly changing posted accounting data can break the relationship between the invoice, deferred report, and General Ledger.

## Related topics

- [Deferred Revenue](/erpnext/deferred-revenue)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Accounts Settings](/erpnext/accounts-settings)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__deferred-expense.md -->
---
title: "Deferred Expense | ERPNext Documentation"
description: "Configure ERPNext deferred expense for prepaid costs, create the Purchase Invoice, recognize expense over time, and verify the ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-expense"
updated: "2026-08-14"
---

CloudWorks, a software supplier to Nova Industries, invoices $1,200 for a one-year service plan. Nova Industries owes the supplier now, but the benefit belongs to twelve months rather than only the month in which the Purchase Invoice is posted.



Deferred Expense prevents the full amount from distorting the current month. ERPNext first holds the cost in an asset account, then recognizes a share as expense during each service period.



Use deferred expense for supplier costs paid or invoiced in advance, such as annual software, insurance, rent, maintenance, or support contracts.



## Understand the accounting effect

Assume no tax for simplicity.


| Event                              | Debit                         | Credit                 |
| ---------------------------------- | ----------------------------- | ---------------------- |
| Submit the $1,200 Purchase Invoice | Deferred Expense asset $1,200 | Creditors $1,200       |
| Recognize one eligible period      | Software Subscription Expense | Deferred Expense asset |
| Pay the Supplier                   | Creditors $1,200              | Bank $1,200            |


Payment clears the payable. It does not decide when the expense is consumed. The service period controls recognition.

The older documentation stated that the deferred expense account was credited on Purchase Invoice creation. That would reverse the normal prepaid-cost treatment. Current ERPNext and standard accounting use a debit to the deferred asset at invoice submission, followed by credits to that asset as expense is recognized.

## Before you begin

Prepare:

- A deferred expense asset account, normally under Current Assets, in the [Chart of Accounts](/erpnext/chart-of-accounts).
- The final Expense Head that should receive the recognized cost.
- A non-stock service [Item](/erpnext/item).
- The contract or coverage start and end dates.
- A Supplier and valid [Purchase Invoice](/erpnext/purchase-invoice) setup.
- The day- or month-based recognition policy in [Accounts Settings](/erpnext/accounts-settings).

Do not use this workflow for inventory that should be received and valued through Stock. Deferred expense is for a cost consumed over time, not for a stock quantity waiting to be issued.

## Configure deferred settings

In Accounts Settings, choose whether recognition is calculated by **Days** or **Months**, whether processing runs automatically, and whether ERPNext posts directly or creates [Journal Entries](/erpnext/journal-entry).

The original $12,000 example is retained: with **Months**, a complete 12-month period normally recognizes $1,000 per month. With **Days**, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact service dates. Different monthly amounts are expected when the number of service days differs.

See [Deferred Accounting](/erpnext/deferred-accounting) for the complete setting behavior.

## Enable deferred expense on the Item

Open the Item used for the prepaid service. In **Accounting**, enable **Deferred Expense**. Enter a standard number of expense months when it helps prefill the expected duration.



![Enable deferred expense on the Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

The current Item form identifies the Item as eligible. The actual deferred asset account and service dates are confirmed on each Purchase Invoice Item row.

## Create the Purchase Invoice

Create a Purchase Invoice for the Supplier and add the deferred-expense Item. Confirm the Company, Supplier bill number and date, posting date, currency, rate, taxes, and Cost Center.

In **Items**, select the pencil icon to open the full row editor.



![Open the Purchase Invoice Item row](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-item-pencil.png)

Expand **Deferred Expense** and complete:


| Field                    | What it means                                          |
| ------------------------ | ------------------------------------------------------ |
| Enable Deferred Expense  | Applies deferred treatment to this invoice row         |
| Deferred Expense Account | Asset account holding the unconsumed cost              |
| Service Start Date       | First date on which the purchased service is consumed  |
| Service End Date         | Final date of the service period                       |
| Service Stop Date        | Optional earlier stop date when the service ends early |
| Expense Head             | Final account that receives recognized expense         |


![Deferred expense account and service period](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-service-period.png)

The example uses **Prepaid Expenses - NET** and **Software Subscription Expenses - NET**. The service dates cover one year. Submit only after confirming every eligible row.

## What happens on submission

ERPNext creates the Supplier payable, but the eligible row is debited to the deferred expense asset instead of immediately debiting the final Expense Head. This prevents a full annual cost from distorting one month's Profit and Loss Statement.

Taxes and charges follow their own configured accounts and rules. Deferred expense controls the eligible Item amount; it does not automatically defer every tax, freight, or charge on the invoice.

## Recognize the expense

When automatic processing is enabled, ERPNext processes eligible schedules in the background. Otherwise, create a [Process Deferred Accounting](/erpnext/process-deferred-accounting) record with **Type = Expense**.

For each eligible period, recognition debits the Purchase Invoice row's Expense Head and credits the deferred expense asset. If Accounts Settings uses Journal Entry posting, ERPNext creates Journal Entry documents. They may remain Draft for review or be submitted automatically.

The original page described automatic monthly Journal Entries. That remains the visible document flow when Journal Entry posting is selected. With direct posting, the same debit and credit appear in the General Ledger without a separate Journal Entry document.

## Verify recognized and pending expense

Open the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report) and check the Purchase Invoice, service period, invoiced amount, recognized amount, and pending balance.

Then review the [General Ledger](/erpnext/general-ledger):

- The deferred asset should begin with the eligible invoice amount.
- Each recognition period should credit that asset.
- The same amount should debit the final Expense Head.
- At the end of the full service period, the eligible deferred balance should be fully recognized, subject to approved changes and rounding.

Review the Supplier payable separately. The invoice may be unpaid, partially paid, or fully paid while expense recognition continues independently.

## Other examples and boundaries

The earlier documentation listed insurance paid in advance, internet subscriptions, debt-issuance costs, and intangible-asset amortization. Those remain conceptually relevant, but not every long-term cost should be handled through this invoice feature.

Fixed assets should normally use ERPNext [Asset](/erpnext/asset) and depreciation workflows. Capitalized interest, intangible assets, and debt-issuance costs may require specialized accounting and local reporting. Use deferred expense on Purchase Invoice rows only when it matches the applicable accounting policy.

## Stop, cancel, or amend the service

If service ends early, use **Service Stop Date** where supported, then verify the next processing run. If the invoice amount, dates, or account is wrong, use the supported cancellation and amendment flow.

Do not post an unexplained Journal Entry to remove a residual prepaid balance. First check the processing dates, document status, stop date, generated Draft Journal Entries, and whether the final period was included.

## Troubleshooting


| Problem                                  | What to check                                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Full cost appears in expense immediately | Confirm the row's enable option, deferred asset account, and service dates                      |
| No recognition entry appears             | Check automatic processing, the selected date range, background jobs, and Draft Journal Entries |
| Monthly amounts differ                   | Confirm whether recognition is based on Days                                                    |
| Prepaid balance remains after the term   | Check the final processing date, service stop date, invoice status, and unsubmitted entries     |
| Expense posts to the wrong account       | Review the Expense Head on the Purchase Invoice Item row                                        |


## FAQs

### Is a deferred expense the same as an unpaid Supplier invoice?

No, unpaid describes the payable and cash status. Deferred describes when the cost is recognized. A fully paid invoice may still have a deferred expense balance.

### Can only one Purchase Invoice line be deferred?

Yes, deferred options, accounts, and service dates are set on each Item row.

### Should prepaid insurance use deferred expense?

It is a common use case when the policy covers future periods. Confirm the required treatment and recognition basis with your accountant.

### Why are generated Journal Entries not in the ledger?

They remain Draft when automatic submission is disabled. Review and submit them before expecting a General Ledger effect.

### Should fixed-asset depreciation use this feature?

Normally no. Use ERPNext's Asset and depreciation workflow for fixed assets. Deferred expense is better suited to prepaid services and similar costs consumed over a defined period.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Revenue](/erpnext/deferred-revenue)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__deferred-revenue.md -->
---
title: "Deferred Revenue | ERPNext Documentation"
description: "Configure ERPNext deferred revenue for prepaid services, invoice the customer, recognize income over time, and verify the ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deferred-revenue"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, pays $1,200 upfront for a one-year warranty program. The invoice is raised today, but Nova Industries earns the revenue month by month as it provides the service.



Deferred Revenue keeps the unearned portion out of current income. ERPNext first posts the invoice amount to a liability account, then recognizes the appropriate share as income over the service period.



Use deferred revenue when a customer pays or is invoiced before your company has completed the related service, such as annual support, maintenance contracts, subscriptions, or prepaid service plans.



## Understand the accounting effect

Assume the invoice has no tax for simplicity.


| Event                           | Debit                      | Credit                            |
| ------------------------------- | -------------------------- | --------------------------------- |
| Submit the $1,200 Sales Invoice | Debtors $1,200             | Deferred Revenue liability $1,200 |
| Recognize one eligible period   | Deferred Revenue liability | Service Income                    |
| Receive the Customer payment    | Bank $1,200                | Debtors $1,200                    |


A [Payment Entry](/erpnext/payment-entry) clears the receivable. It does not determine when the income is earned. Recognition is controlled by the deferred settings and service dates.

## Before you begin

Prepare:

- A deferred revenue liability account in the [Chart of Accounts](/erpnext/chart-of-accounts).
- The final Income Account, such as Service Income.
- A service [Item](/erpnext/item).
- The contract or coverage start and end dates.
- A Customer and a valid [Sales Invoice](/erpnext/sales-invoice) setup.
- The applicable [Accounts Settings](/erpnext/accounts-settings) for automatic processing and day- or month-based allocation.

Do not use an ordinary Income Account as the deferred account. The unearned balance belongs on the Balance Sheet until the service is delivered.

## Configure deferred settings

In Accounts Settings, choose whether ERPNext books deferred entries by **Days** or **Months**, whether processing runs automatically, and whether recognition is posted directly or through [Journal Entries](/erpnext/journal-entry).

If $12,000 covers a 12-month service period, **Months** normally recognizes $1,000 for each complete month. With **Days**, a 30-day month may recognize about $986.30 and a 31-day month about $1,019.17, depending on the exact dates. This original example is retained because it shows why monthly recognition amounts can differ without being wrong.

See [Deferred Accounting](/erpnext/deferred-accounting) for the full setting behavior.

## Enable deferred revenue on the Item

Open the Item used for the service or plan, select the **Accounting** tab, and enable **Deferred Revenue**. Enter a standard number of revenue months when it is useful for the Item.



![Enable deferred revenue on the service Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-item-deferred-accounting.png)

Current ERPNext keeps the deferred account and actual service dates on the Sales Invoice Item row. The Item option identifies that the line is eligible for deferred treatment.

## Create the Sales Invoice

Create a Sales Invoice for the Customer and add the deferred-revenue Item. Confirm the Company, posting date, currency, rate, taxes, and Cost Center as you would for any invoice.

In the Items table, select the pencil icon to open the complete row editor.



![Open the Sales Invoice Item row](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-item-pencil.png)

Expand **Deferred Revenue** and complete:


| Field                    | What it means                                                             |
| ------------------------ | ------------------------------------------------------------------------- |
| Enable Deferred Revenue  | Applies deferred treatment to this invoice row                            |
| Deferred Revenue Account | Liability account holding the unearned balance                            |
| Service Start Date       | First date on which the service is provided                               |
| Service End Date         | Final date of the service period                                          |
| Service Stop Date        | Optional earlier stop date when service ends before the original end date |
| Income Account           | Final account that receives recognized revenue                            |


![Deferred revenue account and service dates](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-service-period.png)

The screenshot uses **Customer Advances - NET** as the deferred liability and **Service - NET** as the final income account. Use dedicated accounts if that gives your company clearer reporting.

Submit the invoice only after verifying every deferred row. One invoice can contain several rows with different service periods.

## What happens on submission

ERPNext creates the normal Customer receivable, but credits the deferred liability instead of immediately crediting the Income Account for the eligible row. This keeps unearned revenue out of the Profit and Loss Statement.

If tax is present, tax accounting follows the configured tax rules. Deferred revenue controls the eligible Item's net income recognition; it does not automatically defer every tax or charge on the invoice.

## Recognize the revenue

When automatic processing is enabled, ERPNext processes eligible schedules through a background job. Otherwise, create a [Process Deferred Accounting](/erpnext/process-deferred-accounting) document with **Type = Income**.

For each eligible period, the recognition entry debits the deferred revenue account and credits the Sales Invoice row's Income Account. When posting through Journal Entry is enabled, ERPNext creates Journal Entry documents. They either remain Draft for review or are submitted automatically, depending on Accounts Settings.

The original page described monthly Journal Entries. That remains valid when Journal Entry posting is enabled. With direct posting, the same accounting effect appears in the General Ledger without a separate Journal Entry document.

## Verify recognized and pending revenue

Run the [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report). Check the invoice, service period, invoiced amount, recognized amount, and pending balance.

Then review the [General Ledger](/erpnext/general-ledger):

- The deferred liability should begin with the invoice amount.
- Each recognition period should reduce that liability.
- The same amount should increase the Income Account.
- After the complete service term, the eligible deferred balance should be fully recognized, subject to rounding or approved changes.

Also verify the Customer receivable separately. The invoice can be unpaid, partially paid, or fully paid while revenue recognition continues according to the service period.

## Stop, cancel, or amend the service

If a service ends early, record the supported **Service Stop Date** and follow your version's processing behavior. Check the deferred report after the next run.

If the invoice itself is wrong, use the normal cancellation and amendment process. Do not manually delete recognition ledger entries. A credit note, cancellation, or amended invoice may need corresponding deferred processing and verification.

## Video

<iframe src="https://www.youtube.com/embed/j6mx-EHU4aY" title="Deferred Revenue in ERPNext" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0"></iframe>

## Troubleshooting


| Problem                                              | What to check                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Full amount appears in income immediately            | Confirm the row has Enable Deferred Revenue, a deferred liability account, and valid service dates |
| No recognition entry appears                         | Check automatic processing, the date range, background jobs, and Draft generated Journal Entries   |
| Monthly amounts are unequal                          | Check whether Accounts Settings uses Days rather than Months                                       |
| Deferred report has a pending balance after the term | Check the processing end date, stop date, invoice status, and unsubmitted Journal Entries          |
| Income posts to the wrong account                    | Review the Income Account on the Sales Invoice Item row                                            |


## FAQs

### Is deferred revenue the same as a Customer advance?

No, a Customer advance is money received before allocation to an invoice. Deferred revenue is an invoiced amount that has not yet been earned. The example account name may include “Customer Advances,” but the underlying concepts and workflows remain different.

### Can revenue be recognized before the Customer pays?

Yes, payment status and revenue recognition are separate. ERPNext follows the service period for recognition and the invoice allocation for receivables.

### Can different invoice lines use different service periods?

Yes, configure deferred revenue and dates on each Item row.

### Why are recognition Journal Entries Draft?

Journal Entry posting is enabled while automatic submission is disabled. Review and submit the generated entries before expecting them in the General Ledger.

### Does deferred revenue defer tax too?

Not automatically. Taxes follow their configured tax and accounting rules. Confirm the required jurisdictional treatment with your accountant.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [Deferred Revenue/Expense Report](/erpnext/deferred-revenue-expense-report)
- [Sales Invoice](/erpnext/sales-invoice)
- [Journal Entry](/erpnext/journal-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__delete-entries-linked-with-gl-entries.md -->
---
title: "Delete entries linked with GL entries"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-entries-linked-with-gl-entries"
updated: "2026-08-14"
---

ERPNext prevents Nova Industries from deleting a cancelled invoice because its accounting and stock ledger rows form part of the audit trail. Deleting a transaction is different from cancelling it, and should be rare. First decide whether you only need to reverse the business effect, which cancellation already does.

## Before enabling deletion

- Confirm the document is cancelled and no statutory or audit rule requires it to remain.
- Take a backup and test in a non-production environment.
- Understand that deleting ledger rows reduces traceability and may allow the naming series number to be reused depending on configuration.

## Enable the setting

1. Open **Accounts Settings**.
2. Find **Delete Accounting and Stock Ledger Entries on deletion of Transaction**.
3. Enable it, save, and reload.
4. Delete only the intended cancelled document.
5. Disable the setting again if it was approved for a one-time cleanup.

![Accounts Settings option for deleting linked accounting and stock ledger entries](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-delete-linked-ledger-setting.png)



## Troubleshooting

### The document is still linked

Open the document’s links and identify dependent records, allocations, returns, or amendments. Remove or resolve dependencies in the correct business order. Do not delete database rows directly.

## Frequently asked questions

### Should I delete an incorrect submitted invoice?

Normally cancel and amend it. That preserves the original document, its reversal, and the correction for audit.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__delete-submitted-document.md -->
---
title: "Delete Submitted Document"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete-submitted-document"
updated: "2026-03-04"
---

To delete a submitted document, you need to cancel it first. Following are the steps to delete a submitted document.

These steps assume that you have the appropriate permissions on the document that you wish to cancel and delete.

#### Step 1: Cancel Submitted Document

You will find the 'Cancel' button on upper right corner of submitted document.

![Screenshot 2023-12-27 at 12.24.48 PM](/files/Screenshot 2023-12-27 at 12.24.48 PM.png)  


#### Step 2: Delete the document

On cancellation of the submitted document, the 'Amend' button becomes visible with the document status set to 'Cancelled'. This means that the document has been cancelled successfully.

To delete the document, now click on Menu, then Delete. This will delete the selected document.

![Screenshot 2023-12-27 at 12.39.59 PM](/files/Screenshot 2023-12-27 at 12.39.59 PM.png)  


**Note:** To delete multiple submitted documents in one go, you can select them in the list view and proceed to cancel and delete.

![Screenshot 2023-12-27 at 12.34.25 PM](/files/Screenshot 2023-12-27 at 12.34.25 PM.png)  


If your document is linked with other documents, then you will need to cancel dependent document before trying to delete the parent document.

![Screenshot 2023-12-27 at 12.37.51 PM](/files/Screenshot 2023-12-27 at 12.37.51 PM.png)  


All deleted documents disappear from the respective DocType but can be seen in 'Deleted Documents'. They can either be deleted permanently or restored.

![Screenshot 2023-12-27 at 12.53.50 PM](/files/Screenshot 2023-12-27 at 12.53.50 PM.png)  


The restored documents are indicated in Deleted Documents.

![Screenshot 2024-08-26 at 4.53.00 PM](/files/Screenshot 2024-08-26 at 4.53.00 PM.png)  


  

<!-- page: erpnext/erpnext__delete_company_transactions.md -->
---
title: "Delete Company Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delete_company_transactions"
updated: "2026-03-12"
---

ERPNext allows you to delete all the transactions like Sales Invoices, Sales Order, Payment Entries etc associated with a company, while keeping the master data intact.



Often, users setup all the master data and then create a few dummy records to test/explore the system. Then, they want to delete the dummy records and start over again.

### Transaction Deletion Record

---

This feature allows you to delete all the records associated with a specified company, except for the ones belonging to the DocTypes listed in the **Excluded DocTypes** table.

If you really want to wipe out the transactions, then follow these steps. However, the deleted transactions can't be restored.

1. Create a new "Transaction Deletion Record" document.
2. Enter the name of the Company whose records you wish to delete.
3. Modify the "Excluded DocTypes" table if needed.
4. Save and Submit.

![](/files/imageaf22f8.png)

The **Summary** table displays the names of the DocTypes whose records were deleted as well as the number of records that were deleted.



## Delete Transactions

---

1. Go to **Home > Accounting > Company** and find your company.
2. On the top right, you'll find the **Delete Transactions** button under **Manage**.
3. Enter your password.
4. Enter the company name to confirm.

![](/files/imagef7bec2.png)

This will submit a record in the Transaction Deletion Record DocType.

:::note
To perform this action, the user must have the role of System Manager.
:::

<!-- page: erpnext/erpnext__deleting-all-transactions-for-the-company.md -->
---
title: "Deleting all transactions for the Company while retaining masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-all-transactions-for-the-company"
updated: "2026-07-02"
---

Use **Delete Transactions** on the Company form when you want to remove transactions for a company while keeping the company setup and master data. This is useful after testing, demo data entry, or sample imports when you want to start entering live transactions without recreating all masters.

This action clears transactional data for the selected company. It does not delete masters such as Company, Customer, Supplier, Item, Account, Warehouse, Cost Center, or other setup records.

## Before You Begin

- Take a full backup before deleting transactions. This action is destructive and should be treated as irreversible unless you restore from backup.
- Use this only when you are sure the selected company's transactions are no longer required.
- Check that users are not creating or submitting new transactions for the company while the deletion is running.
- If the company has been used for live accounting, export the required ledgers and reports before deleting data.
- Make sure you are logged in as a user with permission to delete company transactions.

## What Gets Deleted

ERPNext deletes transactional records linked to the selected company. This can include accounting, stock, buying, selling, payment, manufacturing, and other transaction documents that belong to that company.

The exact records depend on the modules used in your site and the transactions created for the company.

## What Is Not Deleted

Master and setup records are retained. For example, the following records are not deleted just because company transactions are deleted:

- Company
- Customer
- Supplier
- Item
- Account
- Warehouse
- Cost Center
- Territory, Customer Group, Supplier Group, and Item Group

This lets you keep the structure of the company and reuse the same masters after the transactions are cleared.

## Delete Transactions for a Company

### Step 1: Open the Company list

Search for **Company** from the Desk search bar, or open the Company list from the Accounting workspace.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 2: Open the company record

Select the company whose transactions you want to delete. Check the company name carefully before continuing.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 3: Choose Delete Transactions

On the Company form, open **Manage** and click **Delete Transactions**.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 4: Verify your password

ERPNext asks you to verify your password before continuing. Enter your password and click **Verify** only when you are certain you have selected the correct company and have a backup.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

After verification, ERPNext starts deleting the selected company's transactions. Do not close the site or create new transactions for the company while the deletion is in progress.

## After Deletion

- Open key transaction lists, such as Sales Invoice, Purchase Invoice, Payment Entry, Journal Entry, Stock Entry, and Sales Order, and confirm that the company's transactions are removed.
- Check accounting and stock reports for the company to make sure balances are cleared as expected.
- Review retained masters such as Customers, Suppliers, Items, Accounts, and Warehouses before creating new transactions.
- If you plan to start fresh accounting, verify opening balances, stock balances, and fiscal year settings before entering new documents.

## When To Use This

Use this tool when you want to preserve setup and masters but remove transaction history for one company. Common examples include demo data cleanup, testing cleanup, and preparing a configured company for live use.

## When Not To Use This

- Do not use this as a routine data cleanup tool for live companies.
- Do not use it when you only need to cancel or reverse a few specific transactions.
- Do not use it if you need an audit trail of the deleted transactions inside the same site.
- Do not use it without a backup that you know can be restored.

## Common Issues

- **Transactions are still visible:** Check whether those records belong to another company, or whether they are master records rather than transactions.
- **Balances are not cleared:** Recheck linked transactions and reports for the selected company. Also verify whether opening balances or stock balances were entered separately.
- **Permission error:** Your user may not have permission to run the deletion tool. Ask a System Manager or Administrator to review your access.
- **Wrong company selected:** Stop immediately and restore from backup if transactions were deleted for the wrong company.

## Recommended Practice

Before using this on an important site, restore a recent backup on a test site and run the deletion there first. Review the result, confirm that the required masters remain, and then repeat the process on the main site only when you are confident about the outcome.

<!-- page: erpnext/erpnext__deleting-custom-reports.md -->
---
title: "Deleting Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-custom-reports"
updated: "2026-03-04"
---


ERPNext has several [types of reports](/erpnext/making-custom-reports) which can be customized as per the users' requirement.

If there is a custom report which needs to be deleted, it can be achieved by following steps. Please note that its applicable only for the Custom Reports, and not for the standard reports.

#### Step 1: Go to Report List

In the Awesome Bar, type and select "Report List" for an option.

![Report Search](/files/customize-deleting-reports-1.png)

#### Step 2: Delete the Report from the List

The Report List will have all the standard and custom reports of your account. You can select Custom Report to be deleted from the list itself, and click on Delete icon in the Actions Menu.

![Report List](/files/customize-deleting-reports.png)

Or you can open that report, and delete it from File menu.

![Report Delete](/files/customize-deleting-reports-2.png)

<!-- page: erpnext/erpnext__delivery-note-stock-error.md -->
---
title: "Delivery Note Negative Stock Error\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-note-stock-error"
updated: "2026-02-26"
---


**Question**: When submitting a Delivery Note, receiving a message says that item's stock is insufficient, but we have item's stock available in the Warehouse.

**Answer**: On submission of Delivery Note, stock level is checked as on Posting Date and Posting Time of a Delivery Note. It's possible that you have stock of an Item available in the Warehouse. But if you are creating back-dated Delivery Note, and if item was not available in the warehouse on the Posting Date and Posting Time of Delivery Note, you are likely to receive an error message on the negative stock. You can refer to the Stock Ledger report to confirm the same.

If this is the case, you should edit the Posting Date and Time of a Delivery Note, and ensure that it is after the Posting Date and Time of item's receipt entry.
