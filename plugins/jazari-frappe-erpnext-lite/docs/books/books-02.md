<!-- Frappe documentation: books, part 2 of 4. Index: docs/INDEX.md -->

<!-- page: books/books__introduction.md -->
---
title: "Lead"
space: "Books"
url: "https://docs.frappe.io/books/introduction"
updated: "2026-01-30"
---

_Lead_ is a term used in Frappe Books for any potential customer or client who
has shown interest in the products or services offered.

## Lead Status

A Lead can have various statuses based on the stage of engagement:

| Status         | Description                               |
| :------------- | :---------------------------------------- |
| Open           | Newly created and yet to be engaged.      |
| Replied        | Replied to initial engagement.            |
| Interested     | Shown interest in the product or service. |
| Opportunity    | Opportunity for business.                 |
| Converted      | Converted to a Customer or client.        |
| Quotation      | To sent a Quotation.                      |
| Do not Contact | Marked as not to be contacted.            |


> Note: Ensure to update the status of the Lead appropriately as it progresses through
different stages.

## Lead Fields

1. **Name**: The full name of the Lead. This is a required field to uniquely
   identify each Lead.
2. **Status**: The current status of the Lead. It indicates the stage of
   engagement with the Lead and it will be updated automatically based on your
   actions against the lead.
3. **Email**: The email address of the Lead. This is used for communication and
   may be displayed when printing invoices or other documents.
4. **Mobile**: The mobile phone number of the Lead. This is used for quick
   contact and may also be displayed when printing invoices or other documents.
5. **Address**: The physical address associated with the Lead. This can include
   street, city, state, and postal code, and is useful for sending physical
   correspondence or deliveries.

## Actions

The Lead Quick Edit Form includes actions to create associated documents like
Customer or Sales Quote.

![Recent Actions Widget](https://raw.githubusercontent.com/frappe/books_docs/e0ff943f703b37f902f61a0424d1bc2b4cd81183/docs/entries/images/lead.png)

### Create Customer

- Converts the Lead into a Customer, retaining all relevant information.
- Sets the status of the Lead to **Converted**.

### Create Sales Quote

- Creates a Sales Quote against the Lead.
- Links the Sales Quote to the Lead as a reference.

<!-- page: books/books__inventory-settings.md -->
---
title: "Inventory Settings"
space: "Books"
url: "https://docs.frappe.io/books/inventory-settings"
updated: "2026-01-30"
---

Inventory settings will allow you to configure the inventory module to your requirements. To navigate to Inventory Settings: `Setup > Settings` then click on the Inventory tab

[![Inventory Settings](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/inventory-settings.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/inventory-settings.png)  


Setting Items
-------------

The following values can be configured

### Valuation Method

This can be used to select either FIFO or Moving Average valuation methods.

The valuation rate displayed in the Stock Ledger or the Stock Balance report is calculated on the basis of the Valuation Method selected.

### Default Location

This is used to set the location that is used whenever an inventory transaction detail is created.

### Stock In Hand Account

This is used to set the default Stock In Hand Account that is debited whenever stock is received.

### Stock Received But Not Billed Account

This is used to set the default Stock Received But Not Billed Account that is debited on making a Purchase Invoice for a tracked item, and credited when a Purchase Receipt is made.

### Cost Of Goods Sold Account

This is used to set the default Cost of Goods Sold Account that is debited whenever a Shipment is made.

### Enable Barcodes

Checking this will allow you to set barcodes on items. It will also display a barcode input in forms (such as Sales Invoice and Shipment) where items are entered.

### Enable Batches

Checking this will allow the usage of Batches. Items will have a Has Batch option if the item is being tracked.

It will also enable the Batch entry type which can be navigated to by using the Quick Search.

### Enable Serial Numbers

Checking this will allow the usage of Serial Numbers. Items will have a Has Serial Number option if the item is being tracked.

It will also enable the Serial Number entry type which can be navigated to by using the Quick Search.

### Enable UOM Conversion

Checking this will allow setting multiple UOMs for an Items. Then when making a entry that involves the Item, one of the other UOMs can be selected to mention its quantity.

### Enable Stock Returns

Checking this will allow you to create Purchase Receipt and Shipment Returns against the original Purchase Receipts or Shipments.

  

<!-- page: books/books__items.md -->
---
title: "Items"
space: "Books"
url: "https://docs.frappe.io/books/items"
updated: "2026-01-30"
---

*Item* is term used by Frappe Books for anything that is purchased or sold using a Sales or Purchase Invoice.

Types of Items
--------------

An Item is classified by what purpose it's used for.



| # | For | Name | Usage | Navigation |
| --- | --- | --- | --- | --- |
| 1 | Sales | Sales Items | Sales Invoices | `Sales > Sales Items` |
| 2 | Purchases | Purchase Items | Purchase Invoices | `Purchases > Purchase Items` |
| 3 | Both | Common Items | Sales and Purchase Invoices | `Common > Common Items` |


> Usage Make sure that you create the Item under the correct Navigation as this cannot be changed after creation.

Item Fields
-----------

When creating a new Item the following fields are displayed:

1. Item Image: an image to identify the Item by.
2. Item Name: a name to identify the Item by, each Item should have a unique name.
3. Item Code: a unique identifier assigned to each Item for easy tracking, reference, and differentiation.
4. Item Group: a category or classification under which the Item is grouped for better organization and reporting.
5. Purpose: specifies whether the Item is meant for Sales, Purchases, or Both.
6. Type: indicates whether the Item is a Product or a Service.
7. Unit Type: base unit of the Item to which the rate is applied
8. Rate: base cost of an Item, this can be changed in the invoice.
9. Description: textual description of what the Item is.
10. Sales Acc.: the income account that is credited when the Item is sold.
11. Purchase Acc.: the expense account that is debited when the Item is purchased.
12. Tax: tax applied on the Item when making an invoice, this can be changed in the invoice.
13. HSN/SAC: the HSN/SAC code that is used for classifying Items.
14. Barcode: a machine-readable code used to quickly identify and scan the Item in transactions.
15. Track Inventory: enables stock level monitoring for the Item to maintain accurate inventory records.
16. Has Batch: specifies whether the Item is managed in batches for tracking manufacturing or expiry details.
17. UOM Conversions: defines conversion rates between the Item’s base unit and other units of measure.



# Customize Columns

When the **Customize Columns** feature is enabled in system settings, a **“Customize Columns”** button appears in each list view. Clicking this button opens the **Column Selector Modal**, which allows users to choose which columns are shown in the list. The modal provides a simple and interactive way to personalize data views through checkboxes and drag-and-drop actions.

Inside the modal, users see two sections — **Displayed Fields** and **Available Fields**. Displayed Fields show the columns that are currently visible in the list view, while Available Fields contain other fields that can be added. Users can easily reorder displayed columns by dragging them, remove columns by unchecking them or dragging them out, and add new columns by checking or dragging them from the Available Fields section. Required fields are protected from being removed, and hidden or table-type fields are excluded automatically. Once the desired columns are selected and arranged, clicking the **Save** button applies the changes and updates the list view accordingly.

  

![Screenshot from 2025 10 23 11 21 45](/files/Screenshot%20from%202025-10-23%2011-21-45.png)

<!-- page: books/books__journal-entries.md -->
---
title: "Journal Entries"
space: "Books"
url: "https://docs.frappe.io/books/journal-entries"
updated: "2026-01-30"
---

Journal Entries are transactional entries used to record transactions that don’t strictly identify as a Sale or Purchase. Such as the transfer of funds from a Bank Account to a Cash Account.

Creating Journal Entries
------------------------

To create a Journal Entry first navigate to the Journal Entry page

`Common > Journal Entry`

Then click on the blue `+` button to open a new Journal Entry form.

[![Journal Entry Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/journal-entry.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/journal-entry.png)  


1. Set the type of Journal Entry.
2. Add rows for each Account and set the amounts being credited and debited.
3. Click on Save and then Submit.

::: info Double Entry Bookkeeping When making a Journal Entry, you must ensure that the total amount in the Debit column should equal the total amount in the Credit column. :::

After clicking Submit, Frappe Books will the make ledger entries and update the account balances.

You can check the entries by clicking Ledger Entries under the `...` menu.

Examples
--------

These are two examples of how you can make direct Journal Entries to account for transactions that are different from Sales or Purchases.

### Recording Expenses

When you have expenses that you pay at the time of purchase, you can record an Expense directly using Journal Entry.

To do so add two rows to a new Journal Entry form, one for Debit and one for Credit.

Let’s say you incur an expense of ₹5,000 for traveling to a client site, and you paid it directly from your Bank Account, then you must add the following rows:



| Account | Debit | Credit |
| --- | --- | --- |
| Bank Account |  | ₹5,000 |
| Travel Expenses | ₹5,000 |  |

### Recording Prepayments

When a customer pays for a product or service that you haven’t delivered yet, it cannot be booked as Income yet. This is a Liability for your business to fulfill later.

To make an entry that reflects this, add two rows to a new Journal Entry form.

1. One which Debits the amount into the Bank Account because you have received the payment.
2. Another which Credits the amount into a Liability account you may create known as Prepayments.



| Account | Debit | Credit |
| --- | --- | --- |
| Bank Account | ₹5,000 |  |
| Prepayment |  | ₹5,000 |

  

<!-- page: books/books__loyalty-program.md -->
---
title: "Loyalty Program"
space: "Books"
url: "https://docs.frappe.io/books/loyalty-program"
updated: "2026-01-30"
---

Loyalty Program is used to reward customers with points for their purchases,
which can then be redeemed on future purchases.

## Enabling Loyalty Program

To enable Loyalty Program you will have to first check the Enable Loyalty
Program. To
> **Setup > Settings > General Tab.**

![Enable Inventory](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/enable-loyalty-program.png)

Once that is done you will have to restart Frappe Books to see the Loyalty
Program in the sidebar.

> Note: Loyalty Program cannot be disabled once it has been enabled.


## Creating Loyalty Program

To create a Loyalty Program first navigate to the Loyalty Program page

> **Sales > Loyalty Program**

Then click on the blue `+` button to open the Loyalty Program form.

![Sales Invoice Form](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/loyalty-program.png)

1. Enter a unique name for the Loyalty Program.
2. Add the From and To Date for program's validity period.
3. Ensure the **IsEnabled** checkbox is checked. This will mark the program
   active.
4. Collection Rules:

   - **Tier name:** To differentiate between different levels of rewards.
   - **Collection Factor:** How much amount needs to be spent to gain 1 Loyalty
     Point.
   - **Minimum Amount:** Minimum amount to be spent to qualify into a tier.

5. Set an **Expense Account** from where you'll offer the benefits. This is
   useful to track the benefits offered separately.
6. Set the number of days in the Expiry Duration field after which the loyalty
   points will expire.

## Loyalty Program in Customer

Set a Loyalty Program in the Customer to assign a Loyalty Program.

![Sales Invoice Form](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/choose-loyalty-program.png)

Loyalty points earned can be viewed in the Customer.

![Sales Invoice Form](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/loyalty-points.png)

## Loyalty Program Functionality

### Earning Points

1. Assign this Loyalty Program to a Customer.
2. Create a new Sales Invoice for the Customer to whom you have assigned
   Loyalty Program.
3. For this example, an invoice is created with a grand total of 3,000 INR.
   According to the Loyalty Program, if a customer spends a minimum of
   2,000 INR, they are eligible to earn loyalty points. For every 300 INR
   spent, the customer will receive 1 loyalty point. Therefore, with a total
   spend of 3,000 INR, the customer earns 10 loyalty points.
4. Upon submission of the invoice, a Loyalty Point Entry will be created for
   this invoice. This acts as a log to give an overview of which Customer
   earned how many points against which Sales Invoice.

![Sales Invoice Form](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/loyalty-point-entry.png)

### Redeeming Points

1. When creating an invoice for a Customer who has loyalty points, go to the
   Loyalty Point Redemption section and enable the checkbox
   **Redeem Loyalty Points**.
2. The fields for **Loyalty Points** will become visible under this section.
   You can fill in the points to redeem.
3. The total amount of the invoice will be adjusted based on the redeemed
   points, and you will only need to pay the remaining balance after the points
   have been applied.

![Sales Invoice Form](https://raw.githubusercontent.com/frappe/books_docs/00c35515b24bd93d6d4c3ab24602f549e6b23c66/docs/transactions/images/redeem-loyalty-points.png)

<!-- page: books/books__master-data.md -->
---
title: "Master Data"
space: "Books"
url: "https://docs.frappe.io/books/master-data"
updated: "2026-01-30"
---

Besides [Transactional Entries](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries) Frappe Books has regular entries for documents that don't affect any account's balance directly.

Examples of these are:

* [Items](https://github.com/frappe/books_docs/blob/master/entries/items)
* [Party](https://github.com/frappe/books_docs/blob/master/entries/party)
* [Taxes](https://github.com/frappe/books_docs/blob/master/entries/taxes)

Creating a New Entry
--------------------

To create an entry navigate to it's page first, for example for Taxes: `Setup > Taxes`

And click on the blue `+` button, this will open the Quick Edit Form.

[![Quick Edit Form](https://github.com/frappe/books_docs/raw/master/docs/entries/images/quick-edit.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/quick-edit.png)  


Enter the values and click the blue Save button. The entry will now be made and can be used in transactions.

Duplicating an Entry
--------------------

To create the duplicate of an entry, click on the `...` menu button and select Duplicate.

[![Duplicate Button](https://github.com/frappe/books_docs/raw/master/docs/entries/images/duplicate.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/duplicate.png)  


This will create a Draft entry, i.e. it is not yet saved, you can change the values and click on Save.

After the entry has been Saved you can use it in transactions.

Deleting an Entry
-----------------

To delete an entry, click on the `...` menu button and select Delete.

[![Delete Button](https://github.com/frappe/books_docs/raw/master/docs/entries/images/delete.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/delete.png)  


::: warning Entry Deletion Entries used in transactions cannot be deleted.

To delete these entries the Transactions where they are used will have to be deleted first. :::



---

Now that you know the basics of entries you can learn about specific types of entries.

  

<!-- page: books/books__multi-currency-invoicing.md -->
---
title: "Multi Currency Invoicing"
space: "Books"
url: "https://docs.frappe.io/books/multi-currency-invoicing"
updated: "2026-01-30"
---

Frappe Books allows you to create and print invoices in your customers currency.

::: tip Suppliers and Purchase Invoices The same applies procedure applies for creating a Multi Currency Purchase Invoice. Just set a different currency when creating a Supplier entry. :::

Creating a Multi Currency Invoice
---------------------------------

To enable a multi currency invoice you need to do two things:

1. Create a Customer entry with a [different currency](https://github.com/frappe/books_docs/blob/master/transactions/multi-currency-invoicing#customer-and-company-currency) from the company currency.
2. Select the Customer when creating a new invoice.

This will display the [exchange rate](https://github.com/frappe/books_docs/blob/master/transactions/multi-currency-invoicing#exchange-rate) widget.

[![Multi Currency Invoicing](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/multicurrency-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/multicurrency-invoice.png)  


::: info Fields using Company Currency The Base Grand Total and Outstanding Amounts are displayed in the company currency. :::

Printing
--------

After submitting, on clicking Print, the invoice can be printed in the customers currency. [![Multi Currency Invoice Printing](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/multi-currency-print.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/multi-currency-print.png)  


Payments
--------

Payments entries are made in the company currency. The exchange rate set when submitting the invoice is used to decide the amount to be paid.

[![Multi Currency Payment](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/multi-currency-payments.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/multi-currency-payments.png)  


On making the payment the Outstanding Amount will be updated accordingly, and any rounding differences will be balanced using the [Round Off Account](https://github.com/frappe/books_docs/blob/master/miscellaneous/settings#general-settings).

Ledger Entries
--------------

Ledger Entries are created using the company currency. The exchange rate set when submitting the invoice is used to decide the recorded amounts.

[![Multi Currency Ledger Entries](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/multi-currency-ledger-entries.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/multi-currency-ledger-entries.png)  


Exchange Rate
-------------

When a multi currency invoice is made, the ledger entries are created in the company currency.

::: info Exchange Rate Company Currency = Customer Currency ⨉ Exchange Rate :::

Customer and Company Currency
-----------------------------

Multi currency invoice is possible only if the two currencies are different from each other.

### Customer Currency

This is set when a [Customer](https://github.com/frappe/books_docs/blob/master/entries/party) entry is created.

[![Customer Currency](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/customer-currency.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/customer-currency.png)  


### Company Currency

This is set when [initializing](https://github.com/frappe/books_docs/blob/master/setting-up/getting-started) a new Frappe Books instance

[![Company Currency](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/company-currency.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/company-currency.png)  


  

<!-- page: books/books__number-series.md -->
---
title: "Number Series"
space: "Books"
url: "https://docs.frappe.io/books/number-series"
updated: "2026-01-30"
---

Number Series is used as the naming scheme for [transactional entries](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries). Multiple transactions of a single type for example Journal Entry can be grouped under a single Number Series.

[![Number Series](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/number-series.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/number-series.png)  


Default Number Series
---------------------

By default Frappe Books comes with a single Number Series for each of the transactional entry types



| Type | Number Series |
| --- | --- |
| Sales Invoice | SINV- |
| Purchase Invoice | PINV- |
| Payment | PAY- |
| Journal Entry | JE- |

These are selected by default when making a transactional entry. You can create new a Number Series to suit your needs.

::: warning The Number Series of a transactional entry cannot be changed once Save is clicked. :::

Creating a New Number Series
----------------------------

To create a new Number Series for a specific transactional entry

1. Find the Number Series field on the entry form or the Quick Edit Form.
2. Enter the new Number Series you would like to use in the field.
3. Click on Create

[![Number Series Field](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/number-series-field.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/number-series-field.png)  


This will take you to the Number Series Quick Edit Form where you can change the number series configuration.

[![Number Series Form](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/new-number-series.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/new-number-series.png)  


Once you are done editing, click on Save, now you can use the new Number Series for the entry.

Number Series Fields
--------------------

The fields decide how the Number Series is set

1. Prefix: The base prefix applied to the number series for example: *SINV-*
2. Reference Type: The transactional entry type to which this Number Series belongs.
3. Start: The number given to the first entry in the Number Series.
4. Pad Zeros: The number of given as padding to the number part of the Number Series.

For example, if Name is *SALES-PAY-*, Start is 0, and Pad Zeros is 3, then the Number Series values assigned to the transactional entries would be:

*SALES-PAY-000*, *SALES-PAY-001*, *SALES-PAY-002*, *SALES-PAY-003*, etc.

  

<!-- page: books/books__party.md -->
---
title: "Party"
space: "Books"
url: "https://docs.frappe.io/books/party"
updated: "2026-01-30"
---

*Party* is a term used in Frappe Books for any entity to whom a Sale or from whom a Purchase is made.

Types of Party
--------------

A Party is classified by their Role it's used for.



| # | Role | Name | Invoice | Navigation |
| --- | --- | --- | --- | --- |
| 1 | Customer | Customer | Sales Invoices | `Sales > Customers` |
| 2 | Supplier | Supplier | Purchase Invoices | `Purchases > Suppliers` |
| 3 | Both | Party | Sales and Purchase Invoices | `Common > Party` |

::: warning Usage Make sure that you create the Party under the correct Navigation as this cannot be changed after creation. :::

Party Fields
------------

1. Party Image: an image to identify the Party by.
2. Party Name: a name to identify the Party by, each Party should have a unique name.
3. Email: the Party's email address that may be displayed when printing the invoice.
4. Phone: the Party's phone number that may be displayed when printing the invoice.
5. Address: the Party's address that may be displayed when printing the invoice.
6. Default Account: default account that may be credited or debited when a transaction involving the part is made.
7. Currency: the currency in which to create the invoice for the Party.
8. Role: the role of the Party, whether they are a Customer, Supplier or Both.

Recent Invoices
---------------

The Party Quick Edit Form has a Recent Invoices widget. This shows the last three invoices made for a Party.

[![Recent Invoices Widget](https://github.com/frappe/books_docs/raw/master/docs/entries/images/recent-invoices.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/recent-invoices.png)  


Each row shows the following information

* Invoice Name
* Invoice Status
* Date
* Paid Amount
* Outstanding Amount

Clicking on a row will take you to the Invoice from where [Payments can be made](https://github.com/frappe/books_docs/blob/master/transactions/payments#making-payments-from-invoices).

  

<!-- page: books/books__payments.md -->
---
title: "Payments"
space: "Books"
url: "https://docs.frappe.io/books/payments"
updated: "2026-01-30"
---

Payments are a type of transactional entry that indicates the transfer of funds.

Payments usually follow a sale or a purchase, depending on this a Payment entry can be made to either Receive or Pay funds.



| # | Transaction | Payment Type | To Account | From Account |
| --- | --- | --- | --- | --- |
| 1 | Sale | Receive | Bank, Cash Accounts | Accounts Receivable |
| 2 | Purchase | Pay | Accounts Payable | Bank, Cash Accounts |

Making Payments
---------------

To make a Payment first navigate to the Payment page

* For Sales: `Sales > Sales Payments`
* For Purchases: `Purchases > Purchase Payments`

Then click on the blue `+` button. This will open the Payment quick edit form.

[![Payment Quick Edit Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/payment-quick-edit.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/payment-quick-edit.png)  


You can select the Party and enter other the details of the Payment.

Once the details have been set you can click on Save and then Submit to record the Payment.

### Payment Reference

If the Payment is being made for an invoice, you can add a reference to the invoice in the table at the bottom.

This will update the Outstanding Amount on the invoice.

::: tip Invoice Payment A more convenient way of settling an Invoice Payment is to do so using the Make Payment option from the Invoice Form. :::

### Write Off Amount

The write off amount is a deduction on the payment.

[![Payment Write Off](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/payment-writeoff.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/payment-writeoff.png)  


This amount is booked under the Write Off Account that can set under General settings: `Setup > Settings > General`

::: info Transfered Amount The final amount to be paid or received = Amount - Write Off :::

Making Payments from Invoices
-----------------------------

To make an Invoice Payment to settle the Outstanding Amount of a Sales Invoice or a Purchase Invoice, you can navigate to the Invoice form and click on the Make Payment button under the `...` menu.

For more information check these links:

* [Making Sales Payments](https://github.com/frappe/books_docs/blob/master/transactions/sales-invoices#making-sales-payments)
* [Making Purchase Payments](https://github.com/frappe/books_docs/blob/master/transactions/purchase-invoices#making-purchase-payments)

  

<!-- page: books/books__price-list.md -->
---
title: "Price List"
space: "Books"
url: "https://docs.frappe.io/books/price-list"
updated: "2026-01-30"
---

Using Price List, you can keep track of multiple [Item Prices](https://github.com/frappe/books_docs/blob/master/docs/entries/price-list.md#item-price-table-fields) for sales and purchase.

An Item can by priced differently depending on whether it is for sale or purchase, if it is discount season, etc.

A Price List helps by grouping multiple item prices under a single entry. You can then select this entry when making a Sales or a Purchase Invoice, and when an item is selected its rate will be fetched from the Price list.

To use Price Lists you need to first enable them.

Enable Price List
-----------------

The Price List feature needs to be enabled first by checking the **Enable Price List** option in the General Settings.

To navigate: `Setup > Settings > General Tab` [![Enable Price List](https://github.com/frappe/books_docs/raw/master/docs/entries/images/enable-price-list.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/enable-price-list.png)  


Create a Price List
-------------------

To create a Price Lists, go to:`Common > Price List`. And then click on the blue `+` button to open a new Price List creation form.

[![Price List Form](https://github.com/frappe/books_docs/raw/master/docs/entries/images/price-list.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/price-list.png)  


Add Item Prices to your price list, when done click on the Save button.

Price List Fields:

1. **Is Price List Enabled**: enables the Price List, if disabled it cannot be used.
2. **For Sales**: if enabled, the Price List can be selected in Sales Invoices.
3. **For Purchases**: if enabled, the Price List can be selected in Purchase Invoices.

:::tip Multiple Prices

You can add multiple prices for an Item in the Price List. When fetching the price from the Price List, the first Item Price with a matching Unit Type will be selected. :::

Setting a Price List
--------------------

To use a Price List, ou need to select **Price List** in the Sales or Purchase Invoice form.

[![Price List Selection](https://github.com/frappe/books_docs/raw/master/docs/entries/images/price-list-selection.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/price-list-selection.png)  


Once this is done, when a new item is selected it's price will be fetched from the selected Price List.

  

<!-- page: books/books__pricing-rule.md -->
---
title: "Pricing Rule"
space: "Books"
url: "https://docs.frappe.io/books/pricing-rule"
updated: "2026-01-30"
---

Pricing rules allow you to offer flexible discounts and prices based on various
criteria, making your sales promotions more targeted and impactful.

**Common Use Cases:**

- **Quantity Discounts:** Offer a discount (percentage or amount) on items when
  a certain quantity is purchased (e.g., 10% off for buying 5 or more items).
- **Buy-One-Get-One (BOGO) Offers:** Give away a free item or offer a significant
  discount on a second item when a specific item is purchased.
- **Tiered Pricing:** Set different price levels for items based on the total
  order value (e.g., offer a lower price per unit when customers spend above a certain amount).
- **Early Bird Discounts:** Provide a discount for orders placed before a specific date.

## Enable Pricing Rules

1. Go to `Setup > Settings`.
2. Navigate to the **Features** section.
3. Check the boxes for the **Enable Discount Accounting** and **Enable Pricing Rule**.

![Enable Pricing Rule](https://raw.githubusercontent.com/frappe/books_docs/3e7792601503e619e94309eb8a7cab9a50bffd2b/docs/entries/images/enable-pricing-rule.png)

## Creating a Pricing Rule

1. Go to `Common > Pricing Rule`.
2. Click the `+` button to create a new rule.

![Create Pricing Rule](https://raw.githubusercontent.com/frappe/books_docs/3e7792601503e619e94309eb8a7cab9a50bffd2b/docs/entries/images/create-pricing-rule.png)

## Pricing Rule Fields

- **Is Pricing Rule Enabled:** Check this box to activate the rule.
- **Items:** Select the specific items or item groups to which the rule applies.
  Leave blank to apply to all items.
- **Price Discount Type:** Choose the type of discount you want to offer:
  - **Rate:** Set a fixed discount amount (e.g., $5 off).
  - **Discount Percentage:** Apply a percentage discount (e.g., 10% off).
  - **Discount Amount:** Offer a specific discount per unit (e.g., $1 discount per item).
- **Free Item:** Select the item you want to offer for free or at a discount.
- **Quantity:** Enter the number of free items to be given with the purchase.
- **UOM:** Specify the unit of measurement for the free item.
- **Rate:** If offering a discount on the free item, enter the discounted price.
- **Round Free Item Quantity:**
  - **Rounding Method:** Choose how to handle fractional quantities of free items:
    - **Floor:** Round down to the nearest whole number (e.g., 10.1 free items becomes 10).
    - **Round:** Round to the nearest whole number (e.g., 10.1 free items becomes 10, 10.9 becomes 11).
    - **Ceil:** Round up to the nearest whole number (e.g., 10.1 free items becomes 11).
- **Is Recursive:** Enable this option for BOGO offers where buying multiple
  qualifying items triggers the offer multiple times.
- **Recurse Every:** (Applicable only if "Is Recursive" is enabled) Set the number
  of items for which the BOGO offers repeats (e.g., buy 2, get 1 free repeat every 2 purchases).
- **Min Qty:** Minimum quantity of the specified item required to trigger the rule.
- **Max Qty:** Maximum quantity of the specified item to which the rule applies.
- **Min Amount:** Minimum order value for the rule to be applied.
- **Max Amount:** Maximum order value for the rule to be applied.
- **Valid From:** The start date for the pricing rule to be active.
- **Valid Till:** End date for the pricing rule to be inactive.
- **Priority:** Assign a number to determine the order of applying multiple pricing
  rules to the same item. The rule with the highest priority takes precedence.

## Examples

1. BOGO Offer: Buy 3 Get 1

   | Field         | Value            |
   | ------------- | ---------------- |
   | Discount Type | Product Discount |
   | Quantity      | 1                |
   | Rate          | 0                |
   | Recurse Every | 3                |

2. Buy 2 Get 10% Discount

   | Field                       | Value            |
   | --------------------------- | ---------------- |
   | Discount Type               | Price Discount   |
   | Price Discount Type         | Discount Percent |
   | Discount Percentage         | 10               |
   | Min Qty (As Per Stock Unit) | 2                |

<!-- page: books/books__print-templates.md -->
---
title: "Print Templates"
space: "Books"
url: "https://docs.frappe.io/books/print-templates"
updated: "2026-01-30"
---

The Print Template feature in Frappe Books allows you to create personalized print templates for [Invoices](https://github.com/frappe/books_docs/blob/master/transactions/sales-invoices#printing-the-sales-invoice) and a few other [Entries](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries).

To view and create Print Templates navigate to its page using the sidebar: `Setup > Print Templates`. Or alternatively open the Quick Search, type "Print Template" and hit enter.

[![Print Templates](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/print-templates.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/print-templates.png)  


:::tip Preloaded Templates

When you create a new instance of Frappe Books, it comes preloaded with a few templates.

You use these as they are, or you can *Duplicate* and customize them. :::

If you would like to familiarize yourself with the Template Builder interface before learning how to create a Print Template, click [here](https://github.com/frappe/books_docs/blob/master/miscellaneous/print-templates#template-builder-interface).

Creating a Print Template
-------------------------

To create a Print Template, first navigate to the Print Template list and click on the blue `+` button.

You will now see the [Template Builder](https://github.com/frappe/books_docs/blob/master/miscellaneous/print-templates#template-builder-interface) tool.

You can enable the *Edit Mode* by clicking the edit button next to the *Save as PDF* button.

Next, select the template type. Sales Invoice is selected by default, but you can create Print Templates for other entry types too.

[![Template Type](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/template-type.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/template-type.png)  


:::tip Display Entry

You can change the example Entry being displayed. By default Frappe Books selects the latest entry that has been created. :::

:::tip Custom Sizes

You can adjust the size of the Print Template by clicking on the Set Print Size option in the `···` menu.

[![Custom Print Template Size](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/custom-print-size.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/custom-print-size.png) :::

Now you are ready to edit the Print Template

Editing the Template
--------------------

The left pane contains the Template Editor which is used to edit the template. You can remove the preset template and write the template that you want here.

[![Template Editor](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/template-editor.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/template-editor.png)  


:::info Template Syntax

The templates follow the Vue.js template syntax. You can learn more about it [here](https://vuejs.org/guide/essentials/template-syntax.html). :::

:::tip Resizing the Template Editor

You can resize the Template Editor by clicking on the border and dragging it.

[![Resize Template Editor](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/resize-template-editor.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/resize-template-editor.png) :::

### Displaying Values

Values can be displayed by mentioning their keys inside curly braces. For example:


```
<h1>{{ doc.name }}</h1>
```
Here `doc.name` is the key for Invoice No and it will be displayed in an `h1` element.

The Template Editor can help you by autocompleting the keys as you type the name.

There are two sets of keys to display values:

1. `doc`: these keys are used to display values from the entry such as Invoice No, Account, Date, etc. These keys vary depending on the Entry Type.
2. `print`: these keys are used to read Print Settings values such as Logo, Email, Color, etc.

:::tip Key Hints If you want to see the available values you can click on the **Key Hints** section below the Template Editor.

[![Key Hints](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/key-hints.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/key-hints.png) :::

### Template Styling

You can either use [inline CSS styles](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style) or utility classes from [tailwindcss](https://tailwindcss.com/docs/utility-first) to style the different components of your templates.

### Applying Changes

To apply the changes made in the editor, you can:

1. Click outside the template editor
2. Press the shortcut keys (`⌃ return` for macOS and `Ctrl Enter` for other operating systems).

Using the Template
------------------

After you have edited your template and clicked on the blue Save button to save the changes you have made. You can use the templates save your entries as PDFs which you can send to your customers.

To use the template, navigate to the entry and click on the Print button.

[![Print Button](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/print-button.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/print-button.png)  


You will now see the print preview. You can change the template to be used from the list on the left.

[![Print View](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/print-view.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/print-view.png)  


Once you are satisfied with your selection click on the blue Save as PDF button to save it.

Template Builder Interface
--------------------------

When you open any of the Print Templates or when you click on the blue `+` button to create a new Template, you will be shown the Template Builder tool.

[![Template Builder Interface](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/template-builder-interface.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/template-builder-interface.png)  


Here's a list of what each component does:

1. **Template Name**: text input to edit the Print Template name if it has not been saved.
2. **Save as PDF**: button to save the selected entry as a PDF file.
3. **Toggle Edit Mode**: button to toggle edit mode.
4. **More**: dropdown menu with options such as view the print settings, and selecting and saving the template file.
5. **Save**: button to save the Print Template after editing its values.
6. **Template Preview**: preview template after editing without saving it.
7. **Template Editor**: text input to edit the template.
8. **Template Type**: drop selector to set the template type.
9. **Display Entry**: entry to show in the preview area.
10. **Display Scale**: number input to change the Template Preview scale.
11. **Key Hints**: component that shows the available keys (such as `doc.name`, `doc.date`, etc) that can be used in the template.

Tips for Creating Templates
---------------------------

Here are a few tips to help you create custom print templates.

### Duplicating preloaded templates

If you are not familiar with HTML, CSS and Vue.js Template Syntax then you might find creating a custom template to be a bit challenging.

If this is the case, we suggest duplicating one of the Preloaded Templates and editing the duplicate.

[![Duplicating the Templates](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/duplicate-template.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/duplicate-template.png)  


This way you can make and apply small changes and see how it affects the Preview and step by step make the template like how you want it to look.

### Precaution when using tailwindcss

A few of the tailwindcss defaults (for example colors) used in Frappe Books have been overriden using the `tsconfig.js` file.

Since these values are subject to change we suggest not relying on the overriden tailwindcss styles. Not doing this may cause your templates to change when we update the defaults.

  

<!-- page: books/books__profit-and-loss-statement.md -->
---
title: "Profit and Loss Statement"
space: "Books"
url: "https://docs.frappe.io/books/profit-and-loss-statement"
updated: "2026-01-30"
---

All of the money that your business earned from when it started minus the expenses that it incurred will be the total profit (or loss) the business has generated. But we aren’t interested in the total amount, but the amount that is generated last month or last quarter or last year. Hence, Profit and Loss statement is always viewed for a specific time period.

Here are some insights you can gain from this report:

1. Compare this month’s profit with last month.
2. Compare quarter wise or year wise profits or losses.
3. Find out the total profit or loss for a specific time window.

The P&L statement for any period reflects all the income minus all the expenses in that period. At the end of the period, (a fiscal year) the total profit (or loss) goes into Owner’s Equity because the profit in the business belongs to the owners. The owner’s account is a liability to the company since the company has to pay out the profits/losses.

To check your P&L statement, navigate to it using the sidebar: `Reports > Profit And Loss`

[![Profit and Loss](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/profit-and-loss.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/profit-and-loss.png)  


By default the Profit and Loss report will show P&L values for the last 3 months.

As you can clearly see, we have the total Income in the first part which also shows the income coming from each Income account split Monthly so you have a better understanding of your income. The same is done with the Expense section. The report is concluded by the total profit (or loss) incurred which is also split Monthly.

Filters
-------

The Profit and Loss report has several filters which can help you narrow the date range between which to display the report.

### Based On

This allows for toggling betwee the kind of filters used set the date range. It has 2 values:

1. Until Date
2. Fiscal Year

### Periodicity

This selects the interval for which the Profit and Loss has to be calculated.

Example setting this to Monthly will display columns on a monthly basis.

### Date Range Filters

These filters depend on the value of Based On



| Based On | Date Range Filters |
| --- | --- |
| Until Date | To Date and Count |
| Fiscal Year | To Year and From Year |

#### To Date and Count

**To Date** is the final date until which the report is to be displayed, by default the values is tomorrow's date.

**Count** depends on Periodicity so if Count is 3 and Periodicity is Monthly then the report will display Profit and Loss columns for the last three months starting from **To Date**

#### To Year and From Year

These decide the fiscal year between which the Profit and Loss report has to be displayed. The number of columns will depend on the Periodicity.

### Consolidate Columns

Checking this this will sum up all the values for each row and display a single column.

### Hide Group Amounts

The Profit and Loss report format displays the group accounts such as Direct Income along with the non group accounts such as Sales and Services.

Group account balances depend on the non group account balances under them, group account balances are not directly updated.

So clicking on **Hide Group Amounts** will display only the non group account amounts making the report a bit easier to read.

Folding Rows
------------

[![Profit and Loss Folded Rows](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/pnl-folded.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/pnl-folded.png)  


Rows in the Profit and Loss report which display group accounts can be clicked to fold all the rows underneath them.

  
