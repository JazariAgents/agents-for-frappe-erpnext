<!-- Frappe documentation: books, part 3 of 3. Index: docs/INDEX.md -->

<!-- page: books/books__purchase-receipt.md -->
---
title: "Purchase Receipt"
space: "Books"
url: "https://docs.frappe.io/books/purchase-receipt"
updated: "2026-01-30"
---

Purchase Receipt is an inventory transaction that records the receipt stock from a supplier after a purchase has been made.

Purchase Receipts record inward movement of stock.

Creating a Purchase Receipt
---------------------------

There are two ways to create a Purchase Receipt.

### From a Purchase Invoice

Since a receipt of stock follows a purchase, you can create a Purchase Receipt after submitting a Purchase Invoice.

To do this select Purchase Receipt from under the Create menu button.

[[Screenshot on the live page: Create Purchase Receipt From a Purchase Invoice]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/from-purchase-invoice.png)  


::: tip Back Reference

This will create a Purchase Receipt with a reference to the Purchase Invoice and allows you to view all created Purchase Receipts from the Purchase Invoice. :::

### From the List View

To do this first navigate to the Purchase Receipt page: `Inventory > Purchase Receipt` then click on the blue `+` button.

The creation method is shared with with other transactional entries, for more information check [this link](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries.html#creating-an-entry).

::: warning No Back Reference

This method doesn't create links to any Purchase Invoices and is an isolated entry. :::

### Purchase Receipt Form

After selecting one of the above two methods of creating a Purchase Receipt, you will see the Purchase Receipt form.

[[Screenshot on the live page: Purchase Receipt Form]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-form.png)  


If you created the Purchase Receipt from a Purchase Invoice, all the rows will be filled out for you. Else you will have to enter the Purchase Receipt details.

Once the Purchase Receipt details have been entered, click on Save and then Submit to make the Purchase Receipt entry.

A Purchase Receipt can have one of the four following statuses:



| Status | Description |
| --- | --- |
| Submitted | Purchase Receipt entry submitted |
| Return | Purchase Receipt Return entry submitted |
| Return Issued | Return entry created against Purchase Receipt |
| Cancelled | Purchase Receipt entry cancelled |

Purchase Receipt Return
-----------------------

If you created a Purchase Receipt for an item that you returned, you can create a Purchase Receipt Return entry to reflect the return.

A Purchase Receipt Return entry can be created from an existing Purchase Receipt entry that has been submitted or from a new Purchase Receipt entry.

### Enable Stock Returns

To create Purchase Receipt Returns the Stock Returns feature needs to be enabled. To do this, check the **Enable Stock Returns** option in [Inventory Settings](https://github.com/frappe/books_docs/blob/master/inventory/settings.html#inventory-settings) under the Features section.

### Creating a Purchase Receipt Return

1. Open the Purchase Receipt entry to be returned.
2. Click on `Create > Return`. [[Screenshot on the live page: Create Purchase Receipt Return]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/create-purchase-receipt-return.png)
3. The Party and Item details will be fetched from the original Purchase Receipt entry. You can set the quantity of Items returned. [[Screenshot on the live page: Purchase Receipt Return Form]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-return-form.png)
4. Save and Submit.

::: info Item quantity and Payment amount will be in negative to indicate that it is a return. :::

How does Purchase Receipt Return affect General Ledger
------------------------------------------------------

The Purchase Receipt Return entry will create General Ledger entries to reverse the impact of the original Purchase Receipt.

[[Screenshot on the live page: Purchase Receipt Return in General Ledger]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-return-in-general-ledger.png)  


View Ledger Entries
-------------------

After a Purchase Receipt is submitted, both Stock Ledger and General Ledger entries are created.

To view these you can click on the View button and select the one you would like to see.

[[Screenshot on the live page: View Ledger Entries]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-purchase-receipt-ledger-entries.png)  


  

<!-- page: books/books__quick-search.md -->
---
title: "Quick Search"
space: "Books"
url: "https://docs.frappe.io/books/quick-search"
updated: "2026-01-30"
---

The Quick Search interface is a quick way to navigate around in Frappe Books. To activate it you can click on the search button in the header:

[[Screenshot on the live page: Quick Search Bar]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-bar.png)  


Or you can press `Ctrl + K` or `Cmd + K` depending on your operating system.

Dialog
------

[[Screenshot on the live page: Quick Search Dialog]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-dialog.png)  


To search for anything type what you are looking for in the input bar at the top.

::: tip Fuzzy Search Because of the fuzzy search method used, you don't have to type the exact name of the thing you are searching.

So if you make spelling mistakes it is fine, you will still find what you are looking for. :::

Each row in the search results is classified as one of the following Types:



| # | Type | Color | Purpose | Example |
| --- | --- | --- | --- | --- |
| 1 | Docs* | blue | Opens the selected entry | PAY-1001 |
| 2 | List | teal | Opens the List View | Sales Items |
| 3 | Create | green | Opens a Form or Quick Edit Form to create an entry | Purchase Invoice |
| 4 | Report | yellow | Opens the selected report | General Ledger |
| 5 | Page | red | Opens the page | Dashboard |

::: info Docs* Rows of the *Docs* type will show they type of entry it is. For example, Item or Purchase Invoice. :::

In the bottom section you will find the filters which will help you narrow your search results.

Filters
-------

Clicking on More Filters will display all the filters.

[[Screenshot on the live page: Quick Search Filters]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-filters.png)  


There are two kinds of filters here.

1. Regular Filters: coloured buttons in the first row.
2. Doc Filters: blue coloured buttons after the first row.

::: tip Skip Filters Skip Child Tables and Skip Transactions are used to toggle multiple Doc Filters at once. :::

### Regular Filters

Clicking on one of the regular filters will exclude that type from the search.

For example, if you unselect Doc then only List, Create, Report and Page type rows will show in the suggestions.

### Doc Filters

Clicking on a Doc filter will exclude that kind of entry from the search.

For example, if you unselect Payment, all Payments will be excluded from the search.

Examples
--------

The Quick Search functionality is very powerful, you can run various kind of queries just by entering a few letters.

Here are a few examples.

 1. Finding all the Sales Invoices created for Karen 2. Finding all the Purchases Invoices with the item Jacket 3. Finding the Payment for Purchase Invoice PINV-1099 4. Finding all Payments received from Jack 

::: tip Keyword Order The order of the keyword doesn't matter. You can enter the search keywords in any order. :::

  

<!-- page: books/books__reports.md -->
---
title: "Reports"
space: "Books"
url: "https://docs.frappe.io/books/reports"
updated: "2026-01-30"
---

Frappe Books has 4 financial reports. Each report is calculated using the General Ledger Entries that are created when any [Transactional Entry](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries) is made.

Sections
--------

All reports have two sections:

1. Filter Section
2. Report Section

[[Screenshot on the live page: Report Sections]](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/report-sections.png)  


The **Filter Section** allows for setting filters such as the Date Range between which a report is to be generated.

::: tip Setting Filters To generate a report after setting a filter, just click outside the filter box. :::

The **Report Section** shows the generated report.

::: info Pagination The **General Ledger** report also shows a paginator at the bottom which allows for viewing only sections of the report. :::

Exporting a Report
------------------

All reports can be exported as a `CSV` or a `JSON` file. To do so just click on the blue Export button and select the file path.

After exporting the report you may open it in any software of your choice such as Libreoffice Calc, Google Sheets or Microsoft Excel.

Report Links
------------

Check the following links to understand these reports:

1. [General Ledger](https://github.com/frappe/books_docs/blob/master/analytics/general-ledger)
2. [Profit and Loss](https://github.com/frappe/books_docs/blob/master/analytics/profit-and-loss)
3. [Balance Sheet](https://github.com/frappe/books_docs/blob/master/analytics/balance-sheet)
4. [Trial Balance](https://github.com/frappe/books_docs/blob/master/analytics/trial-balance)

  

<!-- page: books/books__sales-invoices.md -->
---
title: "Sales Invoices"
space: "Books"
url: "https://docs.frappe.io/books/sales-invoices"
updated: "2026-01-30"
---

Sales Invoices are bills that are sent to your customers when an income is booked.

It is a transactional entry that denotes a sale.

Creating Sales Invoices
-----------------------

If you have set up your Frappe Books with Accounts, Taxes, Sales Items, and Customers, creating a Sales Invoice is as simple as it gets. If not you can the follow the steps [here](https://github.com/frappe/books_docs/blob/master/setting-up/getting-started).

First navigate to the Sales Invoices page

`Sales > Sales Invoices`

Then click on the blue `+` button to open the Sales Invoice form.

[[Screenshot on the live page: Sales Invoice Form]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-invoice.png)  


1. Select the Customer to whom you will be making a sale.
2. Click on Add Row and select the Item being sold. Default Tax will be fetched you can change it if required.
3. Enter the Quantity.
4. You can add more items or if you are done, click on Save.
5. Once finalized, click on Submit. Frappe Books will do the required ledger entries against the appropriate accounts.

This invoice is now in *“Submitted”* state, it cannot be edited. The sales transaction has been recorded.

Editing an Invoice Item
-----------------------

To edit the values of an Invoice Item click on the edit button on the item row [[Screenshot on the live page: Edit Invoice Item]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/invoice-item.png)  


From here you can change the item description, HSN code check the Taxed Amount, etc.

::: tip Setting the Taxed Amount You can directly set the Taxed Amount, Frappe Books will calculate the Rate of the Item automatically. :::

Making Sales Payments
---------------------

Once a sales invoice has been submitted, you’ll need to record payment against it to denote that you’ve received the money.

To make a Payment first navigate to the Sales Invoice, then click on the `...` menu button. Then click the Make Payment option.

[[Screenshot on the live page: Sales Invoice Status]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-payment.png)  


This will open the Payment quick edit form with the outstanding amount auto-filled.

[[Screenshot on the live page: Sales Invoice Payment]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-payment-quickedit.png)  


You can change the values and click on Save. This will Save and Submit the Payment.

On making the Payment, Frappe Books will make the necessary ledger entries to reduce the payment amount from Accounts Receivable and increase the amount in your Bank or Cash Account.

It will also update the Outstanding Amount on the invoice form.

::: info Sales Invoice Status Until Payments are made to settle the Outstanding Amount, the Sales Invoice will be in the **Unpaid** state.

Once the Outstanding Amount reaches 0, the status will change to **Paid**. :::

### Auto Payments

You can simplify the *Sales Invoice → Payment* workflow by using Auto Payments. For this you just need to set the default accounts for Sales Payment.

This can be done in `Setup > Settings > Defaults > Auto Payments`: [[Screenshot on the live page: Payment Accounts]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/payment-accounts.png)  


Once this is set, whenever you Submit a Sales Invoice a Payment entry will automatically be created.

::: tip Disable Auto Payment for a Sales Invoice

You can disable Auto Payment for a single Sales Invoice by unchecking the Make Payment On Submit check box in the Settings tab before Submitting a Sales Invoice entry.

[[Screenshot on the live page: Disable Auto Payment]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/auto-payment.png) :::

Sales Invoice Return
--------------------

The customer could return an already sold Item due to quality issues or any other reasons.

To reflect this you can create a Sales Invoice Return from the original Sales Invoice entry or manually create one from a new Sales Invoice Entry.

### Creating a Sales Invoice Return

1. Open the original Sales Invoice document, against which customer returned the Items.
2. Click on **Create > Return**. [[Screenshot on the live page: Create Sales Invoice Return]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-create-return.png)
3. The Party and Item details will be fetched as set in the original Sales Invoice document. You can set the quantity of Items returned in negative numbers. [[Screenshot on the live page: Sales Invoice Return Form]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-return-form.png)
4. Save and Submit.

::: info The Item quantity and Payment amount will be in negative figures to indicate that it's a return. :::

### Creating Manually

1. Navigate to the Sales Invoice page `Sales > Sales Invoice`
2. Click on **Return Against** then select the target Sales Invoice against which customer returned the Items. [[Screenshot on the live page: Select return invoice]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-select-return-against.png)
3. Fill Item details.
4. Save and Submit.

Sales Invoice Return impact on General Ledger
---------------------------------------------

The Sales Invoice Return entry will create General Ledger entries to reverse the impact of the original Sales Invoice.

[[Screenshot on the live page: Sales Invoice Return in General Ledger]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-return-in-gl.png)  


Printing the Sales Invoice
--------------------------

To export the Sales Invoice as a PDF, click on the Print button next to the `...` menu above the Sales Invoice Form.

This will open the Print View, you can click on the Customize button to customize it.

[[Screenshot on the live page: Print View]](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/print-view.png)  


You can now add your company logo and select a brand color that matches your business’ primary color. You can also change the style by selecting one of the given Templates. Choose any that fits your style.

Once you have completed customizing, click on Save as PDF to save the Sales Invoice.

After saving the PDF you can take a print out of it using your printer's software.

  

<!-- page: books/books__serial-number.md -->
---
title: "Serial Number"
space: "Books"
url: "https://docs.frappe.io/books/serial-number"
updated: "2026-01-30"
---

If an Item is serialized, a Serial Number record is maintained for each unit of quantity of that Item. This information helps to track the location of the Serial Number. The Serial Number status will tell you its current Inventory status.

Enable Serial Numbers
---------------------

The Serial Number feature needs to be enabled first by checking the Enable Serial Number option under [Inventory Settings](https://github.com/frappe/books_docs/blob/master/inventory/settings)

To navigate to the list of Serial Numbers, open [Quick Search](https://github.com/frappe/books_docs/blob/master/miscellaneous/search) and then type "serial number list" and select the first option.

Serialized Items
----------------

Once you've [enabled](https://github.com/frappe/books_docs/blob/master/inventory/serial-number#enable-serial-number) Serial Number, you can mark an item as a serialized item by first checking **Track Item** and then **Has Serial Number**

[[Screenshot on the live page: Enable Has Serial Number]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/item-has-serial-number.png)  


::: info Track Item **Has Serial Number** can be enabled only if **Track Item** is set. :::

Mentioning Item Serial Number
-----------------------------

Once a Serial Number has been enabled for an [Item](https://github.com/frappe/books_docs/blob/master/entries/items), transactions involving the Item that update Inventory (such as Stock Movements, Shipments, and Purchases) must include the Serial Number.

This can be done by clicking the edit button on the table row and entering the Serial Number one per quantity.

[[Screenshot on the live page: Mentioning Serial Numbers]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/mentioning-serial-number.png)  


::: info Serial Number Entry For each unit of quantity of a serialized Item a single Serial Number should be provided on a separate line. :::

Serial Number Status
--------------------

The status of a Serial Number changes depending on whether the transaction is an inward transaction (eg Purchase Receipt), or an outward transaction (eg Shipment).

A Serial Number can have one of three Status:



| Status | Description |
| --- | --- |
| Active | Serial Number is in stock and can be used only for outward transactions. |
| Inactive | Serial Number is not in stock and can be used only for inward transactions. |
| Delivered | Serial Number has been used for an outward transaction and cannot be used. |

Here is a table that shows how the status of a Serial Number changes:



| Status Change | Transaction |
| --- | --- |
| Inactive → Active | Inward transactions: Material Receipt or Manufacture (created) Stock Movement, Purchase Receipt |
| Active → Delivered | Outward transactions: Material Issue or Manufacture (used up) Stock Movement, Shipment |

If a transaction is cancelled then the Serial Number status is reverted.

  

<!-- page: books/books__settings.md -->
---
title: "Settings"
space: "Books"
url: "https://docs.frappe.io/books/settings"
updated: "2026-01-30"
---

To navigate to the settings use the Sidebar: `Setup > Settings`

There are a few tabs under Settings

1. General: Settings used to customize accounting defaults and enable features.
2. Defaults: Settings that are used to set defaults.
3. Print: Settings that are used to customize the Invoice Print View.
4. System: Settings used to customize System defaults.

:::tip Inventory Settings

[Inventory Settings](https://github.com/frappe/books_docs/blob/master/inventory/settings) are visible only when Inventory has been enabled. :::

General Settings
----------------

[[Screenshot on the live page: General Settings]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/general-settings.png)  


These settings are used to set and customize accounting defaults.

**Settings that cannot be changed**

1. Full Name
2. Company Name
3. Country
4. Bank Name

::: info Setup Wizard These values are set when setting up a new instance using the Setup Wizard. :::

**Settings that can be changed**

1. Fiscal Year Start Date: used as the start date when displaying the reports by fiscal year.
2. Fiscal Year End Date: used as the end date when displaying the reports by fiscal year.
3. Write Off Account: account used when a Write Off amount is set when making a Payment
4. Round Off Account: account used to settle the credit and debit difference when the General Ledger is updated.
5. Enable Discount Accounting: used to enable the setting of discounts in invoices. ([link](https://github.com/frappe/books_docs/blob/master/transactions/discount-accounting))
6. Enable Inventory: used to enable inventory management features. ([link](https://github.com/frappe/books_docs/blob/master/inventory/introduction))

::: info GSTIN GSTIN setting is available only when the country is set to India.

Setting this value will enable the GST Reports. :::

Defaults
--------

[[Screenshot on the live page: Defaults]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/defaults.png)  


These settings are used to set default values that are selected when creating an entry. They allow for quicker creation of entries but can be changed when making entries.

The following Defaults can be set:

1. Accounts used for Auto Payments.
2. Locations used for Auto Stock Transfers.
3. [Number Series](https://github.com/frappe/books_docs/blob/master/miscellaneous/number-series) for transactional entries.
4. Terms to be used for certain transactional entries.
5. [Print Templates](https://github.com/frappe/books_docs/blob/master/miscellaneous/print-templates) to be used when printing an entry.

:::warning Auto Stock Transfer items

An Item from an Invoice is included in the auto Stock Transfer only if these conditions are met:

1. The item does not use Batches.
2. The item does not use Serial Numbers.
3. There is sufficient quantity of the item at the set default Location.

:::

Print Settings
--------------

[[Screenshot on the live page: Invoice Settings]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/print-settings.png)  


Settings here can be altered to customize the Print View of an Invoice.

::: tip Print View These settings can also be altered from the [Print View](https://github.com/frappe/books_docs/blob/master/transactions/sales-invoices#printing-the-sales-invoice) of an Invoice :::

System Settings
---------------

[[Screenshot on the live page: System Settings]](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/system-settings.png)  


These settings are used to alter how values such as currency and time are displayed.

1. Date Format: used to set how dates are displayed.
2. Hide Get Started: used to hide the Get Started section from the Sidebar.
3. Version: this is a read only field which tells you the current version of Frappe Books.
4. Locale: used to set the currency format, by default locale of the selected country is used.
5. Display Precision: used to set the number of digits are shown after the decimal.
6. Currency: used to set the currency used for all transactions.

::: info Get Started Get Started is auto hidden on completion. :::

  

<!-- page: books/books__setup-opening-balances.md -->
---
title: "Setup Opening Balances"
space: "Books"
url: "https://docs.frappe.io/books/setup-opening-balances"
updated: "2026-01-30"
---

If you are moving from an existing accounting system over to Frappe Books, you will need to enter the account balances from your previous system.

To set the Opening Balances you can follow the steps below.

Get The Starting Balances
-------------------------

Get the starting balances from your previous accounting system in the form of Trial Balances report.

Add Additional Accounts
-----------------------

Add any accounts from your previous system that do not exist in Frappe Books by navigating to the Chart of Accounts.

You can follow the steps shown [here](https://github.com/frappe/books_docs/blob/master/setting-up/initial-entries#add-additional-bank-accounts). Make sure you create the Accounts under the correct Account groups.

Create a Journal Entry
----------------------

First navigate to the **Journal Entry** page.

`Common > Journal Entry`

Then click on the blue `+` button to open the **Journal Entry** form.

[[Screenshot on the live page: Journal Entry Form]](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/journal-entry.png)  


1. Set the Entry Type as Opening Entry.
2. Add a row for each line from your Trial Balances report, select the appropriate Account and the Debit or Credit amount.
3. Click on Save. Review it once before clicking on Submit.

You can set a Reference Number and Reference Date to mark the entry.

This will create a Journal Transaction in the system with all your previous statements.



---

Congratulations! You have now set your Opening Balances. 🎉

This brings your books to the same position that was present in your previous accounting system.

You are now ready to record your business activities by making transactions.

  

<!-- page: books/books__shipment.md -->
---
title: "Shipment"
space: "Books"
url: "https://docs.frappe.io/books/shipment"
updated: "2026-01-30"
---

Shipment is an inventory transaction that records the delivery of stock to a customer after a sale has been made.

Shipments record outward movement of stock. Hence a shipment can take place only if there is sufficient quantity of an Item at the selected Location.

Creating a Shipment
-------------------

There are two ways to create a Shipment.

### From a Sales Invoice

Since a shipment of stock follows a sale, you can create a Shipment after submitting a Sales Invoice.

To do this select Shipment from under the Create menu button.

[[Screenshot on the live page: Create Shipment From a Sales Invoice]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/from-sales-invoice.png)  


::: tip Back Reference

This will create a Shipment with a reference to the Sales Invoice and allows you to view all created Shipments from the Sales Invoice. :::

### From the List View

To do this first navigate to the Shipment page: `Inventory > Shipment` then click on the blue `+` button.

The creation method is shared with with other transactional entries, for more information check [this link](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries.html#creating-an-entry).

::: warning No Back Reference

This method doesn't create links to any Sales Invoices and is an isolated entry. :::

### Shipment Form

After selecting one of the above two methods of creating a Shipment, you will see the Shipment form.

[[Screenshot on the live page: Shipment Form]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-form.png)  


If you created the Shipment from a Sales Invoice, all the rows will be filled out for you. Else you will have to enter the Shipment details.

Once the Shipment details have been entered, click on Save and then Submit to make the Shipment entry.

A Shipment can have one of the four following statuses:



| Status | Description |
| --- | --- |
| Submitted | Shipment entry submitted |
| Return | Shipment Return submitted |
| Return Issued | Return entry created against Shipment |
| Cancelled | Shipment entry cancelled |

Shipment Return
---------------

The customer can return an already shipped Item due to quality issues, delay in delivery, or some other issue.

To reflect this you can create a Shipment Return from the original Shipment entry or manually create one from a new Shipment Entry.

### Enable Stock Returns

To create Shipment Returns the Stock Returns feature needs to be enabled. To do this, check the **Enable Stock Returns** option in [Inventory Settings](https://github.com/frappe/books_docs/blob/master/inventory/settings.html#inventory-settings) under the Features section.

### Creating a Shipment Return

1. Open the Shipment entry to be returned.
2. Click on `Create > Return`. [[Screenshot on the live page: Create Shipment Return]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/create-shipment-return.png)
3. The Party and Item details will be fetched from the original Shipment entry. You can set the quantity of Items returned. [[Screenshot on the live page: Shipment Return Form]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-return-form.png)
4. Save and Submit.

::: info Item quantity and Payment amount will be in negative to indicate that it is a return. :::

Shipment Return impact on General Ledger
----------------------------------------

The Shipment Return entry will create General Ledger entries to reverse the impact of the original Shipment.

[[Screenshot on the live page: Shipment Return in General Ledger]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-return-in-general-ledger.png)  


View Ledger Entries
-------------------

After a Shipment is submitted, both Stock Ledger and General Ledger entries are created.

To view these you can click on the View button and select the one you would like to see.

[[Screenshot on the live page: View Ledger Entries]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-shipment-ledger-entries.png)  


  

<!-- page: books/books__stock-balance.md -->
---
title: "Stock Balance"
space: "Books"
url: "https://docs.frappe.io/books/stock-balance"
updated: "2026-01-30"
---

Stock Balance is a report that displays the current stock quantities, value and valuation rate by Item and Location.

[[Screenshot on the live page: Stock Balance]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-balance.png)  


Filters
-------

The Stock Balance has filters which can help you narrow the generated report to the entries you would like to see.

### Item

Selecting a Item will display only entries involving the selected item.

### Location

Selecting a Location will display only entries involving the selected location.

### From Date

The date from which all the stock balance is calculated. The default value is one year before tomorrow.

Stock balance from before this date is used to set the Opening Quantity and Opening Value.

### To Date

The date until which all the stock balance is calculated. The default value is one day after today.

Values after this date are ignored.

::: tip

If you are getting insufficient quantity for backdated inventory entries, you can use this filter to identify future negative quantity. :::

  

<!-- page: books/books__stock-ledger.md -->
---
title: "Stock Ledger"
space: "Books"
url: "https://docs.frappe.io/books/stock-ledger"
updated: "2026-01-30"
---

Stock Ledger is a report that displays all the stock entries that are recorded whenever an inventory transaction such as a Shipment or a Stock Movement is submitted.

The Stock Ledger shows you the change in quantity, value and valuation rate over the course of various inventory transactions.

[[Screenshot on the live page: Stock Ledger]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-ledger.png)  


Filters
-------

The Stock Ledger has several filters which can help you narrow the generated report to the entries you would like to see.

### Ref Type

Setting Ref Type as anything other than All will display entries only of that Transactional entry type.

Example setting Ref Type as Shipment will display only entries created due to Shipment.

### Ref Name

Ref Name filter allows to display all ledger entries that were generated due to a single Transactional Entry.

To enable this you need to first set Ref Type.

### Item

Selecting a Item will display only entries involving the selected item.

### Location

Selecting a Location will display only entries involving the selected location.

### From Date

The initial date after which all the entries are to be displayed. The default value is one year before tomorrow.

### To Date

The final date before which all the entries are to be displayed. The default value is one day after today.

### Group By

Selecting a Group By option other than None groups the entry according to the selected option.

For instance setting Group By as Reference will group the entries by the Name of the Transactional entry.

### Ascending Order

By default the entries are displayed by newest entry first, i.e. descending order of Date.

Checking this will display the entries in ascending order of entry date.

  

<!-- page: books/books__stock-movement.md -->
---
title: "Stock Movement"
space: "Books"
url: "https://docs.frappe.io/books/stock-movement"
updated: "2026-01-30"
---

Stock Movement is an inventory transaction that records the movement of stock to and from a location.

Unlike the other inventory transactions, stock movement is not linked to a Customer or a Supplier through a Sale or a Purchase.

Movement Types
--------------

Before creating a Stock Movement you need to know about its Movement Types. There are three types of Stock Movements that you can create:

1. Material Issue: stock is moved out of a location.
2. Material Receipt: stock is moved into a location.
3. Material Transfer: stock is moved from one location to another.
4. Manufacture: stock of items are moved out of a location and stock of different items are moved into a location.

Depending on the Movement Type you have to set the From and To movement locations



| Movement Type | From | To |
| --- | --- | --- |
| Material Issue | `set` | `not set` |
| Material Receipt | `not set` | `set` |
| Material Transfer | `set` | `set` |
| Manufacture | `set` | `set` |

::: tip Manufacture For the Manufacture type, both From and To are set but for **different items**.

This reflects the stock movements of a manufacturing process where a set of raw materials are converted into finished goods.

The inventory quantities of the raw material will go down and that of the finished goods will go up. :::

Creating Stock Movements
------------------------

To create a Stock Movement, first navigate to the stock movement List View: `Inventory > Stock Movement` then click on the blue `+` button in the title bar.

[[Screenshot on the live page: Stock Movement]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-movement.png)  


After clicking the blue `+` button:

1. Select the Movement Type
2. Add a row by clicking on Add Row
3. Select an Item
4. Select the movement locations
5. Set the quantity and rate
6. Click on Save and then on Submit

After clicking on submit the Stock Movement entry will be recorded.

View Stock Entries
------------------

New entries will be created in the Stock Ledger and the Stock Balance will be updated.

To View the Stock Ledger entries click on Stock Entries under the `...` menu

[[Screenshot on the live page: View Stock Entries]](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-stock-entries.png)  

<!-- page: books/books__taxes.md -->
---
title: "Taxes"
space: "Books"
url: "https://docs.frappe.io/books/taxes"
updated: "2026-01-30"
---

To calculate the amount of tax on an Item's purchase or sale, a Tax entry has to be selected on the invoice row.

[[Screenshot on the live page: Invoice Row]](https://github.com/frappe/books_docs/blob/master/docs/entries/images/invoice-row.png)  


::: tip Auto Set Tax If the Tax has been set on the Item then it will be auto set in the invoice row. :::

Tax entries can be made from the Tax page: `Setup > Taxes`

Tax Fields
----------

A Tax entry has just two fields

1. Tax Name: a unique name to identify the tax by.
2. Tax Detail: a table where the Tax account along with the Tax rate is set.

::: info Tax Detail Tax Detail is a table as a single tax can have multiple components each with a separate account and rate. :::

  

<!-- page: books/books__transactional-entries.md -->
---
title: "Point of Sale (POS)"
space: "Books"
url: "https://docs.frappe.io/books/transactional-entries"
updated: "2026-01-30"
---

**POS** (Point of Sale) refers to the time and place where retail transactions occur. This system enables efficient sales processing, payment reconciliation, and shift management for retail environments.

### 1. Open POS Shift

   [Screenshot on the live page]

Before initiating sales, a POS shift must be opened to record opening balances and enable accurate tracking of cash and other payment methods throughout the session.

**Steps to Create an Open POS Shift**

1. Cash in Denominations

Enter the quantity of each currency denomination (e.g., ₹1000, ₹500, ₹100). The system will automatically calculate the total opening cash amount based on these inputs.

2. Opening Amounts by Payment Method

* The calculated cash amount is automatically populated under the “Cash” payment method.

* Opening balances for other payment methods (e.g., Card, UPI, Wallet) can be entered if applicable.

3. Once all amounts are verified, click Submit. The POS shift will be marked as open, recording the shift’s opening date and time.


### 2. Creating a POS Invoice

[Screenshot on the live page]

After opening a POS shift, sales billing can begin through the POS interface.

**How to create a POS Invoice ?**

1. Go to the POS interface and choose a customer for the sale.
2. From the item list displayed on the left, click on the items to add them to the cart.
3. Adjust the quantity for each item as needed.
4. To change item rates or apply discounts, ensure these options are enabled in the POS Settings.
5. Verify the grand total and the total quantity in the summary section at the bottom.
6. Click the Pay button and select the desired payment method.
7. Submit the sales invoice when prompted to complete the transaction.
8. Once the invoice is submitted, you can print the POS invoice directly by selecting the Pay and Print option.



### 3. Adding an Item

   [Screenshot on the live page]


Items can be selected in two ways: by clicking on the item name or by scanning the barcode.

* Enter Barcode / Weight-enabled barcode in the box as shown in the image, the item will be automatically added to the cart.

* If the product list in the dropdown is very long, use the search field by typing the product name in the search box.

**Filter by Group:** A field that allows filtering and displaying items based on their assigned item group. When an item group is selected from the dropdown list, only items belonging to that group are shown.

[Screenshot on the live page]

* To change the quantity of an item, click the expand arrow and either enter the desired quantity in the **Transfer Quantity** field or use the up/down arrows to adjust it.

* To remove an item from the cart, click the delete button next to the corresponding item.

### 4. Additional POS Features


[Screenshot on the live page]

**1.Grid View:** Displays items in a grid format with images when the grid view icon is clicked.

**2.[Sales Invoice](https://docs.frappe.io/books/sales-invoices) List:** Redirects to the Sales Invoice List.

**3.[Loyalty Program](https://docs.frappe.io/books/loyalty-program):** Shows the loyalty points earned by the selected customer. Points can be redeemed from this view. The button is disabled if the customer has no loyalty points.

**4.[Coupon Code](https://docs.frappe.io/books/coupon-code):** Allows redemption and application of available coupon codes for the selected items. The button is disabled if no coupon codes are available.

**5.[Price List](https://docs.frappe.io/books/price-list):** Displays applicable price lists for the selected items, allowing you to apply them. The button is disabled if no price list is available.

**6.[Item Enquiry](https://docs.frappe.io/books/item-enquiry):** Allows the user to record and track specific item-related queries.This feature helps maintain detailed records of customer enquiries for better follow-up and service.

### 5. Cart Actions

   [Screenshot on the live page]
   
* Total Quantity: The Total Quantity refers to the combined number of all items included in a transaction or order.

* Item Discounts: The Item Discounts refer to price reductions applied to specific products or services in the order.

* Grand Total: The Grand Total is the final amount payable after applying all discounts, charges, and taxes to the subtotal.

* Save Button: The system immediately stores the current transaction as a Draft Invoice, retaining all entered details for future review, modification, or completion.

* Cancel Button: The system discards the current transaction and resets the POS interface to its default state, ready for a new entry.

* Held Button: The system displays two sections: 

  * Saved - Shows all transactions that have been saved but not yet submitted.
  
  * Submitted – Displays all submitted invoices, including those that are partially paid.


[Screenshot on the live page]

A search function is available within the Held section to quickly locate invoices by their invoice name.

* Return Button: It displays a list of all return invoices, and selecting an invoice will redirect the user and add its items to the POS cart.


[Screenshot on the live page]

A search function is available to quickly locate invoices by their invoice name.

* PAY Button: After adding items and selecting the customer, click the **Pay** button to view available payment methods, including **Cash**, **Bank**, and **Transfer**; upon selection, the payable amount will be displayed for confirmation.

### 6. Payment Workflow

[Screenshot on the live page]

1. Click Pay after adding items and selecting the customer.

2. Choose a payment method (e.g., Cash, Bank, Transfer). The payable amount is displayed for confirmation.

Available payment actions:

* Submit: Marks the invoice as submitted and saves it under Held > Submitted.

* Cancel: Cancels the payment process and closes the payment interface.

* Pay: Completes the payment and generates the invoice.

* Pay & Print: Completes the payment, generates the invoice, and prints it immediately.

### 7. Close POS Shift

[Screenshot on the live page]


The Close POS Shift feature is used to end a POS shift by recording final cash counts, calculating payment totals, and reconciling amounts.

1. Closing Cash

* The cashier can manually enter the quantity of each cash note or coin, with values initially pre-filled from the Opening Cash.

* When the counts are updated, the system automatically recalculates the total Closing Cash and displays the difference between the Closing Amount and the Expected Amount.

2. Closing Amounts

* It displays a read-only table showing the Payment Method, Opening Amount, Expected Amount, Closing Amount, and Difference Amount for each payment type.

* This section is used for reconciliation, helping identify any cash shortages or surpluses by comparing the Closing Amount (entered for Cash; zero for non-cash) against the Expected Amount.


The **Submit** button validates all closing amounts, sets the Closing Date, and links the record to the Opening Shift.

<!-- page: books/books__trial-balance.md -->
---
title: "Trial Balance"
space: "Books"
url: "https://docs.frappe.io/books/trial-balance"
updated: "2026-01-30"
---

A Trial Balance is an accounting report which lists account balances for all your Accounts (both Ledger and Group) for any given reporting period.

A company prepares a trial balance periodically, usually at the end of every reporting period. The general purpose of producing a trial balance is to ensure the entries in a company's bookkeeping system are mathematically correct.

The totals of Debit and Credit columns must be the same for any given period, to ensure the entries are correct.

Navigate to this report from the sidebar: `Reports > Trial Balance`

[[Screenshot on the live page: Trial Balance]](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/trial-balance.png)  


Filters
-------

The Trial Balance report has filters which can help you narrow the date range between which to display the report.

### From Date

The initial date after which the Trial Balance has to be calculated. The default value is the first day of the current fiscal year.

### To Date

The final date before which all the Trial Balance has to be calculated. The default value is the last day of the current fiscal year.

### Hide Group Amounts

The Trial Balance report format displays the group accounts such as Current Liabilities along with the non group accounts such as Secured Loans and Creditors.

Group account balances depend on the non group account balances under them, group account balances are not directly updated.

So clicking on **Hide Group Amounts** will display only the non group account amounts making the report a bit easier to read.

Folding Rows
------------

[[Screenshot on the live page: Trial Balance Folded Rows]](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/trial-balance-folded.png)  


Rows in the Trial Balance report which display group accounts can be clicked to fold all the rows underneath them.

  
