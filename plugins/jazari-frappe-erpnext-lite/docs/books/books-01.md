<!-- Frappe documentation: books, part 1 of 1. Index: docs/INDEX.md -->

<!-- page: books/books__accounting-basics.md -->
---
title: "Accounting Basics"
space: "Books"
url: "https://docs.frappe.io/books/accounting-basics"
updated: "2026-01-30"
---

A small primer to get you up to speed on the concepts of accounting.

Let's understand the concept of accounting with the example of an imaginary business that is just starting out.

**Owner Investment**: Let’s say we’re starting a Home Interior business and we have ₹5,00,000 of capital to start our business.


> Bank balance will initially be ₹5,00,000.
> 
> 

**First Expense**: We will need an operating place where we can work and meet clients. For this, we rent out a co-working space for ₹40,000 per month. This is our first expense.


> Bank balance will now be ₹5,00,000 - ₹40,000 = ₹4,60,000.
> 
> 

**First Income**: We have invested some cash, and we have a working place. Now we make our first sale having a value of ₹30,000. We earned ₹30,000 from our first customer. This is our first income.


> Bank balance at this point will be ₹4,60,000 + ₹30,000 = ₹4,90,000.
> 
> 

**Accounts Payable**: Finally, Let’s say we decided to hire a Web Agency to build a website for us, they charge ₹50,000 which will be paid after 2 months from current date.

At this point we haven’t paid them any money, but we are liable to pay them in the future. This is a liability and will be recorded under Accounts Payable.

Events and Accounts
-------------------

Let’s list these events down in a table:



| # | Event | Amount |
| --- | --- | --- |
| 1 | Owner Investment | + ₹5,00,000 |
| 2 | Rent | - ₹40,000 |
| 3 | Sales | + ₹30,000 |
| 4 | Accounts Payable | - ₹50,000 |
| 5 | *Total* | *₹4,40,000* |

Now, let's categorize these into the five types of Accounts and list their final balances:



| # | Account | Amount |
| --- | --- | --- |
| 1 | Asset (Bank) | ₹4,90,000 |
| 2 | Liabilities (Accounts Payable) | ₹50,000 |
| 3 | Equity (Owner Investment) | ₹5,00,000 |
| 4 | Income (Sales) | ₹30,000 |
| 5 | Expense (Rent) | ₹40,000 |

Impact on Accounts
------------------

Let’s take a look at each transaction and understand which accounts will get affected, from an accounting point-of-view:

### 1. Cash Investment

Since you, the owner, invested money into the business, it is a liability. So, Accounts Payable, which is a Liability account, is increased by ₹5,00,000.

Also, the money in the Bank Account, which is an Asset account, is increased by ₹5,00,000.



| Account | Credit | Debit |
| --- | --- | --- |
| Accounts Payable | ₹5,00,000 | 0 |
| Bank Account | 0 | ₹5,00,000 |

### 2. Rent

Rent is an immediate expense, so it is recorded in the Rent Account, which is an Expense account, it is increased by ₹40,000.

Also, the money is spent from the Bank Account, which is an Asset account, it is decreased by ₹40,000.



| Account | Credit | Debit |
| --- | --- | --- |
| Rent Account | 0 | ₹40,000 |
| Bank Account | ₹40,000 | 0 |

### 3. First Sale

We got an immediate payment, it is recorded in Sales Account, which is an Income account, the balance is increased by ₹30,000.

Also, we received the money in our Bank Account directly, so it’s balance increases by ₹30,000.



| Account | Credit | Debit |
| --- | --- | --- |
| Income Account | ₹30,000 | 0 |
| Bank Account | 0 | ₹30,000 |

### 4. Hiring a Web Agency

We hired a Web Agency for some work, and we are liable to pay them in the future. This is recorded in Accounts Payable by increasing the amount by ₹50,000.

Since this is an expense for us, we also increase the balance in the Vendor Expense Account by ₹50,000.



| Account | Credit | Debit |
| --- | --- | --- |
| Accounts Payable | ₹50,000 | 0 |
| Expense Account | 0 | ₹50,000 |



---

As you might have noticed, every transaction we do in our business affects two accounts. This is the basis of double-entry bookkeeping system.

You can test this out by creating a **Sales Invoice** in Frappe Books, and then check the **General Ledger Report** to see which accounts were affected.

Credit and Debit
----------------

The words Credit and Debit mean different things when applied to different accounts.

* For **Assets** and **Expense** accounts Credit implies a decrease in balance and Debit implies an increase in balance.
* For **Liabilities** and **Income** accounts Credit implies an increase in balance and Debit implies and decrease in balance.

::: tip AEDLIC You can remember this by the abbreviation **AEDLIC** which would stand for:

**A**ssets and **E**xpenses **D**ebit, **L**iabilities and **I**ncome **C**redit :::

  

<!-- page: books/books__balance-sheet.md -->
---
title: "Balance Sheet"
space: "Books"
url: "https://docs.frappe.io/books/balance-sheet"
updated: "2026-01-30"
---

A Balance Sheet is the financial statement of a company which states assets, liabilities and equity at a particular point in time.

In Frappe Books, you can view the balance sheet for your accounts based on monthly, quarterly, half-yearly, and yearly periods.

Navigate to this report from the sidebar: `Reports > Balance Sheet`

[![Balance Sheet](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/balance-sheet.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/balance-sheet.png)  


Filters
-------

The Balance Sheet report has several filters which can help you narrow the date range between which to display the report.

### Based On

This allows for toggling betwee the kind of filters used set the date range. It has 2 values:

1. Until Date
2. Fiscal Year

### Periodicity

This selects the interval for which the Balance Sheet values have to be calculated.

Example setting this to Monthly will display columns on a monthly basis.

### Date Range Filters

These filters depend on the value of Based On



| Based On | Date Range Filters |
| --- | --- |
| Until Date | To Date and Count |
| Fiscal Year | To Year and From Year |

#### To Date and Count

**To Date** is the final date until which the report is to be displayed, by default the values is tomorrow's date.

**Count** depends on Periodicity so if Count is 3 and Periodicity is Monthly then the report will display Balance Sheet columns for the last three months starting from **To Date**

#### To Year and From Year

These decide the fiscal year between which the Balance Sheet report has to be displayed. The number of columns will depend on the Periodicity.

### Consolidate Columns

Checking this this will sum up all the values for each row and display a single column.

### Hide Group Amounts

The Balance Sheet report format displays the group accounts such as Current Assets along with the non group accounts such as Cash and Debtors.

Group account balances depend on the non group account balances under them, group account balances are not directly updated.

So clicking on **Hide Group Amounts** will display only the non group account amounts making the report a bit easier to read.

Folding Rows
------------

[![Balance Sheet Folded Rows](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/balance-sheet-folded.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/balance-sheet-folded.png)  


Rows in the Balance Sheet report which display group accounts can be clicked to fold all the rows underneath them.

  

<!-- page: books/books__batches.md -->
---
title: "Batches"
space: "Books"
url: "https://docs.frappe.io/books/batches"
updated: "2026-01-30"
---

Inventory in Frappe Books can be maintained on the basis of Batches. Here a Batch of some Item is a uniquely grouped collection of those Items.

Enable Batches
--------------

The Batch feature needs to be enabled first by checking the Enable Batches option under [Inventory Settings](https://github.com/frappe/books_docs/blob/master/inventory/settings).

To navigate to the list of Batches, open [Quick Search](https://github.com/frappe/books_docs/blob/master/miscellaneous/search) and then type "batch list" and select the first option.

Batched Items
-------------

Once Batch has been enabled, you can mark an Item as a Batched Item by first checking Track Item and then Has Batch.

[![Enable Has Batch](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/item-has-batch.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/item-has-batch.png)  


::: info Track Item

Has Batch can be enabled only if Track Item is set. :::

Mentioning Item Batch
---------------------

Once Batch has been enabled for an Item, transactions involving the item that update inventory such as Stock Movements, Shipments and Purchase Receipts will require mentioning the Item's Batch.

This can be done by clicking the edit button on the table row and selecting the batch.

[![Mentioning Batches](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/mentioning-batches.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/mentioning-batches.png)  


Batch-wise Reports
------------------

After batches have been enabled, the inventory reports i.e. Stock Ledger and Stock Balance will both have an additional column that mentions the Item's Batch.

You can also set Batch specific filters to show information that relates only to the selected Batch.

[![Batch-wise Report](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/batchwise-report.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/batchwise-report.png)  


  

<!-- page: books/books__chart-of-accounts.md -->
---
title: "Chart of Accounts"
space: "Books"
url: "https://docs.frappe.io/books/chart-of-accounts"
updated: "2026-01-30"
---

Chart of Accounts is used to refer to the organization of all accounts in a financial system.

Navigate to the chart of accounts from the Sidebar: `Setup > Chart of Accounts`

Organization of Accounts
------------------------

There are two types of accounts in the Chart of Accounts

1. **Ledger Accounts**: Accounts that are used in the transactional entries and that appear in the General Ledger.
2. **Group Accounts**: Accounts that are used to group other Group and Ledger accounts.

### Root Accounts

At the upper most level there are 4 Group Accounts. These can be thought of as the *Root Accounts*. These *Root Accounts* have all the other accounts grouped underneath them.

[![Root Accounts](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/root-accounts.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/root-accounts.png)  


::: info Number of Root Accounts The number of Root Accounts depends on your country's CoA.

For example: The Indian CoA has only 4. Whereas the Standard Chart of Accounts has 5. :::

Each Root Account is either a Credit or a Debit account. If a Root Account is a Credit account all the accounts underneath it will also be a Credit Account. ([Credit and Debit](https://github.com/frappe/books_docs/blob/master/basics/accounting-basics#credit-and-debit))

### Other Accounts

Clicking on a Root Account will reveal the accounts other it. This goes for the other Group Accounts too.

[![Other Accounts](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/other-accounts.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/other-accounts.png)  


Clicking on a Ledger Account will open that accounts Quick Edit Form where the details of the account can be viewed.

[![Ledger Account](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/ledger-account.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/ledger-account.png)  


Creating a New Account
----------------------

To create a new account

1. Hover over a Group Account
2. Click on Add Account or Add Group

[![Create a New Account](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/create-new-account.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/create-new-account.png)  


This will display a new row where you can enter the account name. After you are done press Save to create the account.

  

<!-- page: books/books__coupon-code.md -->
---
title: "Coupon Code"
space: "Books"
url: "https://docs.frappe.io/books/coupon-code"
updated: "2026-01-30"
---

A coupon code can be used to get a discount. To use a coupon, you must first
set up a pricing rule. This rule determines the specific discount or offer
associated with the coupon. When you apply the coupon, it will follow the rules
you set up.

## Enabling Coupon Code

1. Go to `Setup > Settings`.
2. Navigate to the **Features** section.
3. Check the boxes for the **Enable Discount Accounting**,
   **Enable Pricing Rule**, and **Enable Coupon Code**.

> Note: **Discount Accounting** and **Pricing Rule** should be enabled to use **Coupon Codes**


![Enable Coupon Codes](https://raw.githubusercontent.com/frappe/books_docs/5601f51269118621cdd73b3ad47f2033c1eff868/docs/entries/images/enable-coupon-code.png)

Once that is done you will have to restart Frappe Books to see the Coupon Code
in the sidebar.

> Note: Coupon Code cannot be disabled once it has been enabled.

## Creating Coupon Code

To create a Coupon Code first navigate to the Coupon Code page

> **Sales > Coupon Code**

Then click on the `+` button to open the Coupon Code form.

![Coupon Code](https://raw.githubusercontent.com/frappe/books_docs/5601f51269118621cdd73b3ad47f2033c1eff868/docs/entries/images/coupon-code.png)

- **Is Enabled:** To mark the Coupon Code as active.
- **Pricing Rule:** Select the pricing rule that applies when a specific coupon
  code is used.
- **Min Amount:** Minimum order value for the rule to be applied.
- **Max Amount:** Maximum order value for the rule to be applied.
- **Valid From:** The start date for the pricing rule to be active.
- **Valid To:** End date for the pricing rule to be inactive.
- **Maximum Use:** Maximum use for the coupon to be applied.
- **Used:** Count of times the coupon has been applied.

## Apply Coupon Code

You can select coupons to get discounts. The coupon will apply a discount based
on the rules set for that coupon.

![Coupon Code](https://raw.githubusercontent.com/frappe/books_docs/5601f51269118621cdd73b3ad47f2033c1eff868/docs/entries/images/choose-coupon-code.png)

Applied Pricing rule can be viewed in the Pricing Rule Detail section.

![Coupon Code](https://raw.githubusercontent.com/frappe/books_docs/5601f51269118621cdd73b3ad47f2033c1eff868/docs/entries/images/applyed-coupon-code.png)

<!-- page: books/books__create-initial-entries.md -->
---
title: "Create Initial Entries"
space: "Books"
url: "https://docs.frappe.io/books/create-initial-entries"
updated: "2026-01-30"
---

Let’s create some initial entries before you can start recording your transactions.

Add Additional Bank Accounts
----------------------------

Add any bank accounts your business has apart from the one already added in the Setup.

Navigate to the **Chart of Accounts** page from the sidebar.

`Setup > Chart of Accounts`

[![Chart of Accounts](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/coa.png)](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/coa.png)  


Then open the **Bank Accounts** group and click on **Add Account**.

`Application of Funds (Assets) > Current Assets > Bank Accounts > Add Account`

Enter the bank account name and press enter to create it. You can now transfer funds in and out of this bank account.

Add Taxes
---------

If your company charges or will recover Sales Taxes, add any taxes that you will use. First navigate to the **Taxes** page.

`Setup > Taxes`

[![Tax](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/tax.png)](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/tax.png)  


1. **Create a New Tax Entry**: Click on the blue `+` button. Enter a name which will make it easier to identify. You can also mention the rate in the name. for e.g. Service Tax - 5%.
2. **Select the Tax Account and Rate**: You can add multiple rows with different Tax Accounts. This will make it easier to apply a set of Taxes which are frequently applied together on an Item. You can even create different taxes for different Items or a class of Items.
3. **Click on Save**

For more information on Taxes in Frappe Books click [here](https://github.com/frappe/books_docs/blob/master/entries/taxes).

Add Sales Items
---------------

One of the most important things you will add in Books are your products or services that you provide to your customers. Navigate to **Sales Items**

`Sales > Sales Items`

[![Sales Item](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/sales-item.png)](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/sales-item.png)  


1. **Create a New Item Entry**: Click on the blue `+` button. Enter the Name and the Rate
2. **Select Type**: Select if your Item is a Product or Service.
3. **Set Default Tax**: Setting the default Tax for your Item will fetch it automatically when you create an Invoice.
4. **Click on Save**

You can set or change the other details for the item. Such as the Income or Expense accounts.

You can even set an image for the item.

For more information on Sales Items in Frappe Books click [here](https://github.com/frappe/books_docs/blob/master/entries/items).

Add Customers
-------------

Add your Customers to record their details and select them in Sales Invoices. First navigate to Customers

`Sales > Customers`

[![Customer](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/customer.png)](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/customer.png)  


1. **Create a New Customer Entry**: Click on the blue `+` button. Enter the name of of the customer
2. **Click on Save**

You can enter additional details such as Email and Phone in the Customer entry. This will be shown when creating a Sales Invoice PDF.

For more information on Customers in Frappe Books click [here](https://github.com/frappe/books_docs/blob/master/entries/party).



---

You can now move onto the next step to set your Opening Balances.

  

<!-- page: books/books__customize-form.md -->
---
title: "Customize Form"
space: "Books"
url: "https://docs.frappe.io/books/customize-form"
updated: "2026-01-30"
---

Frappe Books allows you to customize all forms whether it's Invoice, or Party, or Item you can use the Customize Form feature to add additional fields to it.

Enable Form Customization
-------------------------

To be able to customize a form you need to enable it from the General Settings.

`Setup > Settings > General`

After you have navigated to the General Settings tab, click on the Enable Form Customization checkbox.

[![Enable Form Customization](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/enable-form-customization.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/enable-form-customization.png)  


You will have to reload Frappe Books to see the option, you can press `Ctrl + R` if you are on Windows or linux, or `command + R` on macOS.

::: warning Disabling Form Customization

Disabling Form Customization will just hide the form customization option from the sidebar and search, it will not disable the customizations. :::

Customizing Forms
-----------------

After enabling form customization and reloading Frappe Books navigate to the Customize Form list view using the sidebar.

`Setup > Customize Form`

After that click on the blue `+` button to customize a form type. This will open a new Custom Form entry.

[![Custom Form](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/custom-form.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/custom-form.png)  


Select a Form Type to customize.

::: info Form Type

Form Type refers to the form that you want to add fields to such as Item, Party, Sales Invoice, etc.

Each Form Type can have only one Custom Form entry associated with it. :::

Once you select the Form Type you can add Custom Fields

Custom Fields
-------------

Each Form Type can have multiple custom fields. Click on the Add Row button to add a new Custom Field.

Enter its Label, for example if we want to add a color field to Item, we will set the Label as "Color".

:::tip Fieldname

Setting the Label will auto set the Fieldname value. The Fieldname is a name used to refer to the field internally. :::

After setting the Label and the Fieldname, you can select the fieldtype, for more information on fieldtype and the other fields that you can set for each Custom Field row check the sections below.

[![Custom Fields](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/custom-fields.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/custom-fields.png)  


Once you are done click on the blue Save button.

:::warning Reload App

After customizing a form you must reload Frappe Books to view the added fields in the forms. :::

[![Customized Form](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/customized-form.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/customized-form.png)  


After reloading the app, you will see the new fields in the form.

Custom Field Fieldtypes
-----------------------

Custom Forms support 16 different Fieldtypes, each field type defines the behavior and UI of the field.

For some fields you will have to enter additional details, here's a table the describes the different Fieldtypes.



| Fieldtype | Description | Example | Additional |
| --- | --- | --- | --- |
| Data | Field used for regular text input. | Full Name in Customer | - |
| Text | Field with larger area of input for longer text. | Notes in Sales Invoice | - |
| Date | Field used to input only date. | Date in Sales Invoice | - |
| Date Time | Field used to input date and time. | Date in Stock Movement | - |
| Int | Field used to input integer such as -1, 0, 3, etc. | HSN/SAC Code in Item | - |
| Float | Field used to input fractional numbers such as 0.12, -9.33, 100.1, etc. | Quantity in Sales Invoice Item | - |
| Currency | Field used to input monetary amounts. | Amount in Sales Invoice Item | - |
| Check | Field used to display a checkbox. | Track Item in Item | - |
| Select | Field used to select an item from multiple choices. Requires Options value to be set | Entry Type in Journal Entry | Options |
| Autocomplete | Same as Select but with autocomplete. Used for larger number of options. | Country in Address | Options |
| Color | Field used to select a color. Can set options to select color from. | Color in Print Settings | Options |
| Link | Field used to mention links to other entries. Requires Target to be set. | Customer in Sales Invoice | Target |
| Dynamic Link | Field used to mention links depending on a dynamic target. Requires References to be set. | Name in Payment Reference | References |
| Attach Image | Field used to select an image. | Image in Item | - |
| Attachment | Field used to select any type of file. | Add Attachment in Sales Invoice | - |
| Table | Field used to display a Table. This is currently not supported. | Items in Sales Invoice | Target |

Other Custom Form Fields
------------------------

Fields that describe behaviour:

* **Is Required**: Whether this field is required for a form to be saved.
* **Options**: New line separated list of options required by Select and Autocomplete and used by Color.
* **Target**: Form type from which Link field value is selected. If Table then the name of the Table form type.
* **References**: Fieldname of the reference field which sets the Dynamic Link target type. Eg Type in Payment Reference.

Fields that describe UI:

* **Form Tab**: Tab on the form under which the field is displayed.
* **Form Section**: Section under the entered tab where the field is displayed.

Deleting Customizations
-----------------------

You can delete a forms customizations by deleting its Custom Form entry:

[![Delete Customizations](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/delete-customizations.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/delete-customizations.png)  


:::danger Data Loss

Deleting customizations will also delete data that had been stored in the custom fields. :::

  

<!-- page: books/books__dashboard.md -->
---
title: "Dashboard"
space: "Books"
url: "https://docs.frappe.io/books/dashboard"
updated: "2026-01-30"
---

Dashboard show an overview of Cash Flow, Profit and Loss, Pending Payments and Expenses.

You can access the Dashboard from the sidebar.

[![Dashboard](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/dashboard.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/dashboard.png)  


Period Selector
---------------

All sections of the Dashboard have a Period Selector. The default value is **This Year**. There are three options.

Consider today's date as 16 Jun, 2022. The three options will show analytics for the given range:



| # | Option | From | Until (Today) |
| --- | --- | --- | --- |
| 1 | This Year | 16 Jun, 2021 | 16 Jun, 2022 |
| 2 | This Quarter | 16 Mar, 2022 | 16 Jun, 2022 |
| 3 | This Month | 16 May, 2022 | 16 Jun, 2022 |

::: info Options The Cashflow and the Profit and Loss chart don't show the **This Month** option. :::

Cashflow
--------

[![Cashflow](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/cashflow.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/cashflow.png)  


The Cashflow chart shows the total amount of money being transferred into and out of your company over a period.

::: tip Cashflow The Cashflow chart is calculated from the Cash and Bank account balances. :::

::: info Hover Hover tooltip shows the Inflow or Outflow amount for that month. :::

Pending Payments
----------------

[![Pending Payments](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/pending-payments.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/pending-payments.png)  


Pending Payments shows the invoice paid and unpaid (outstanding) amounts. It has two sub-sections

1. The Sales Invoice section shows the total outstanding amount which is pending from your customers for your sales.
2. The Purchase Invoice section shows the total outstanding amount that you have to pay to your suppliers for your purchases.

::: info Hover Hover tooltip shows the number of Paid and Unpaid invoices. :::

Profit and Loss
---------------

[![Profit and Loss Bar](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/pnl-bar.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/pnl-bar.png) This chart shows the profit (or loss) per month for a given period.

::: tip Profit and Loss Profit and Loss is the difference between the Income and Expense accounts. :::

::: info Hover Hover tooltip shows the Profit or Loss amount for that month. :::

Top Expenses
------------

[![Top Expenses](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/top-expenses.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/top-expenses.png)  


This section shows your top five expenses sorted from your highest expenses to lowest expenses by category.

::: tip Expenses The Top Expenses chart is calculated from the Expense account balances. :::

  

<!-- page: books/books__discount-accounting.md -->
---
title: "Discount Accounting"
space: "Books"
url: "https://docs.frappe.io/books/discount-accounting"
updated: "2026-01-30"
---

Discount is a deduction that is applied to the cost of an item. Frappe Books supports applying discount to an invoice on an item-wise basis.

Enable Discount Accounting
--------------------------

To enable discount accounting, first navigate to General Settings: `Setup > Settings > General`

Then check the Enable Discount Accounting checkbox.

[![Enable Discount Accounting](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/enable-discount-accounting.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/enable-discount-accounting.png)  


::: warning Once Discount Accounting is enabled, it cannot be disabled. :::

After that set the account that will be used for discounts

[![Set Discount Account](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/set-discount-account.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/set-discount-account.png)  


::: info The discount account is an Indirect Income account, you can create it using the [Chart of Accounts](https://github.com/frappe/books_docs/blob/master/miscellaneous/chart-of-accounts) :::

Setting Discount Amount
-----------------------

Discount is applied on an item-wise basis. After you have enabled discount click on the edit button on the item row to set the discount.

[![Setting the Discount](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/set-discount.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/set-discount.png)  


This will open Quick Edit Form to edit the invoice item values. Discount can be set in two ways:

1. Setting a Discount Percent (default)
2. Setting a Discount Amount

To set the Discount Amount click on Set Discount Amount. Once the Discount Amount or Percent is set the Discounted Amount will be shown.

::: tip Setting Discounted Amount You can directly set the Discounted Amount, Frappe Books will automatically calculate the item rate. :::

Discount After Tax
------------------

By default the Discount is applied before the Tax is calculated.

To apply the Discount after the Tax, select the Discount After Tax checkbox after opening the settings for the Invoice.

[![Discount after Tax](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/discount-after-tax.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/discount-after-tax.png)  


  

<!-- page: books/books__general-ledger.md -->
---
title: "General Ledger"
space: "Books"
url: "https://docs.frappe.io/books/general-ledger"
updated: "2026-01-30"
---

The General Ledger is a detailed report for all transactions posted to each account and for every transaction there is a Credit and Debit account so it lists them all up.

This helps you to get a full update for all entries posted in a period against any account.

[![General Ledger](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/general-ledger.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/general-ledger.png)  


Navigate to the General Ledger from the sidebar: `Report > General Ledger`

Filters
-------

The General Ledger has several filters which can help you narrow the generated report to the entries you would like to see.

### Ref Type

Setting Ref Type as anything other than All will display entries only of that Transactional entry type.

Example setting Ref Type as Journal Entry will display only entries created due to Journal Entries.

### Ref Name

Ref Name filter allows to display all ledger entries that were generated due to a single Transactional Entry.

To enable this you need to first set Ref Type.

### Account

Selecting an Account will display only entries where an amount is being credited or debited from this account.

### Party

Selecting a Party will display only entries involving them.

### From Date

The initial date after which all the entries are to be displayed. The default value is one year before tomorrow.

### To Date

The final date before which all the entries are to be displayed. The default value is one day after today.

### Group By

Selecting a Group By option other than None groups the entry according to the selected option.

[![Group By Reference](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/groupby-ref.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/groupby-ref.png)  


For instance setting Group By as Reference will group the entries by the Name of the transactional entry.

### Include Cancelled

Checking this will include the cancelled entries in the report.

::: info Reverted Column A new column **Reverted** is added to indicate which of the entries have been cancelled. :::

### Ascending Order

By default the entries are displayed by newest entry first, i.e. descending order of Date.

Checking this will display the entries in ascending order of entry date.

  

<!-- page: books/books__getting-started-with-frappe-books.md -->
---
title: "Getting Started with Frappe Books"
space: "Books"
url: "https://docs.frappe.io/books/getting-started-with-frappe-books"
updated: "2026-01-30"
---

Let’s start applying what we have learned so far by setting up your company in Frappe Books.

If you have not downloaded Frappe Books, you can download it from the [GitHub releases](https://github.com/frappe/books/releases/latest).

## Setup Instance

When you open Frappe Books, you’ll be presented two options: **New File** and **Existing File**. If this is the first time you are opening Frappe Books, click on **New File**.

Now select an appropriate location where you want to store the file and give it a name.

[

![New File](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/new-file.png)

]([https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/new-file.png](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/new-file.png))  

::: tip File Location Frappe Books stores all your company data and transactions on a local `.db` file on your computer.

You can change the location of this `.db` file. If you have done so you can find it again by selecting the **Existing File** option. 
:::

Now, enter your Business Name, Business Email and Country Information. This will help set up the correct Chart of Accounts based on your country.

[

![Setup Wizard](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/setup-wizard.png)

]([https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/setup-wizard.png](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/setup-wizard.png))  

::: tip Chart of Accounts If you don't find the Chart of Accounts of your country, you can select the **Standard Chart of Accounts**. 
:::

---

Congratulations! You now have a company set up on Frappe Books.

You can now move onto the next step to create some initial entries before you can start recording your invoices and transactions.

<!-- page: books/books__import-wizard.md -->
---
title: "Import Wizard"
space: "Books"
url: "https://docs.frappe.io/books/import-wizard"
updated: "2026-01-30"
---

The Import Wizard is a powerful tool that can allow you to:

1. Import Data from a `.csv` file
2. Make multiple entries quickly

Basics
------

To use the Import Wizard navigate to it using the sidebar: `Setup > Import Wizard`. Or alternatively open the Quick Search, type "Import Wizard" and hit enter.

### The Interface

Once the Import Wizard has been opened you will have to select and Import Type which decides the kind of entries to be imported.

[![Select Import Type](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/select-import-type.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/select-import-type.png)  


After selecting the import type, you'll see the additional controls that are now available.

[![Import Wizard Controls](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-wizard-controls.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-wizard-controls.png)  


### Using a Template

To import data you, it needs to fit some template for this, first click on the Save Import Template button.

This will download a `.csv` template file.

:::tip The Template.csv file The Template.csv file can be filled using any spreadsheet software.

[![Import Template CSV](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-template-csv.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-template-csv.png)  


The Import Template has three rows:

1. Entry type row: Some entries have child tables and this indicates whether the column belongs to the child table.
2. Field label row: This tells us which field of the entry (or its child table) does the column belong to.
3. Field key row: This row allows the Import Wizard to auto assign the columns when the file is selected. If this row is not present then Column Assignment Bar can be used to assign the fields.

:::

To use the Template.csv file you must

1. Import it into your spreadsheet software of choice
2. Enter the values in the spreadsheet cells
3. Export the sheet as a `.csv` file

Once you have exported the `.csv` file, click on Select File to select the file. The Import Wizard will read the file and add rows to the table.

### Verifying and Importing

You can now check the imported values and if everything seems right. If you want to remove a row, click on the row index to delete it.

[![Import File Selected](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-file-selected.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-file-selected.png)  


:::tip The Add Row button You can click on the Add Row button to add an additional empty row to the bottom of the import table which can be edited to enter the required values.

This feature can be used for making multiple entries quickly without even selecting a file. :::

:::info Fixing Conversion Errors If the Import Wizard couldn't convert a value then it will be marked with a red border.

[![Conversion Error](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-conversion-error.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-conversion-error.png)  


You can hover over the field to view what the raw value was and fix the value to remove the error :::

Finally if everything is fine, click on Import Data to begin importing the data.

### After Importing

Once import is done, you'll see the Import Complete modal

[![Import Complete](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-complete.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-complete.png)  


Clicking on Show Me will take you to the List View of the newly created entries. Clicking on Done will reset the Import Wizard allowing you to make more entries.

:::info Fixing Failed Imports If certain entries could not be imported then you can click on the Fix Failed button that is visible only on failed imports.

Clicking it will clear all the successful imports and allow you to fix the failed ones and retry. :::

Picking Import Columns
----------------------

You can pick the specific columns you want to import by clicking on the `...` button and then clicking on `Pick Import Columns`.

This will open the Pick Import Columns modal

[![Pick Import Column](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/picking-import-columns.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/picking-import-columns.png)  


The fields marked by the red `*` are required fields and cannot be unselected. Other than these you can choose to keep or remove the rest of the columns.

Removing a column will:

1. Remove it from the exported template.
2. Prevent it from being assigned to a column.

Column Assignment Bar
---------------------

The Column Assignment Bar is used to mark a column in the table as a certain field. This is useful if the file you have selected doesn't use the Import Wizard's template.

Along with assigning columns you can even de-assign columns by selecting None [![Import Column Assignment](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/import-column-assignment.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/import-column-assignment.png)  


If None is selected then that column is ignored while importing data.

Importing Entries with Child Tables
-----------------------------------

Sales Invoice is an example of an entry with a child table. Here child table refers to the items table which lists all the items included in the sale.

When importing entry with a child table:

1. Unique placeholder names should be provided even if the entry uses a Number Series.
2. Each row in the child table should be one row.
3. All rows of an entry should have the same non child table row data.

For Example



| Invoice Name | Customer | Item (Table Row) | Amount (Table Row) |
| --- | --- | --- | --- |
| A | Lin | Bat | 100 |
| A | Lin | Ball | 50 |
| B | Andy | Pen | 200 |
| B | Andy | Pencil | 10 |
| B | Andy | Ink | 80 |

Here the import table has two Sales Invoices with unique names A, and B.

Invoice A has two items and Invoice B has three items. Each item is a single row in the import table.

And for every child table row in the import table the non child table data, i.e. Invoice Name and Customer are repeated.

::: warning Not following these guidelines may either cause the data to not be imported properly or to fail altogether. :::

  

<!-- page: books/books__introduction-to-inventory.md -->
---
title: "Introduction to Inventory"
space: "Books"
url: "https://docs.frappe.io/books/introduction-to-inventory"
updated: "2026-01-30"
---

Frappe Books' inventory features allows you to track the movement of your items as you perform your business transactions.

Inventory Features
------------------

The inventory module of Frappe Books consists of the following features:

1. [Stock Movement](https://github.com/frappe/books_docs/blob/master/inventory/stock-movement): transaction that records the movement of Items to and from selected Locations.
2. [Shipment](https://github.com/frappe/books_docs/blob/master/inventory/shipment): transaction that records the movement of Items to a Customer after a sale has been made.
3. [Purchase Receipt](https://github.com/frappe/books_docs/blob/master/inventory/purchase-receipt): transaction that records the movement of Items from a Supplier after a purchase has been made.
4. [Stock Ledger](https://github.com/frappe/books_docs/blob/master/inventory/stock-ledger): report that keeps a record of all the stock transactions.
5. [Stock Balance](https://github.com/frappe/books_docs/blob/master/inventory/stock-balance): report that displays the stock balance quantities.

Enabling Inventory
------------------

To enable inventory you will have to first check the Enable Inventory. To navigate: `Setup > Settings > General Tab`.

[![Enable Inventory](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/enable-inventory.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/enable-inventory.png)  


Once that is done you will have to restart Frappe Books to see the Inventory item in the sidebar.

::: warning

Inventory cannot be disabled once it has been enabled. :::

Tracking an Item
----------------

Since you may not want to track the movement of all items, item tracking has to be enabled by setting the Track Item checkbox when creating an item.

[![Track Item](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/track-item.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/track-item.png)  


::: info

Track Item can be enabled only while creating the item. :::

Once you have created an item with tracking enabled, you can track its movement by making inventory specific transactions.

Location
--------

In Frappe Books the movement of an item takes place to and from a *Location*. There are two kinds of movements that can take place:

1. Inward movement: When you move an item to a *Location*, the quantity of the item at that location increases.
2. Outward movement: When you move an item from a *Location*, the quantity of the item at that location decreases.

The source or destination location for an outward or inward transaction is selected when making the transaction.

::: info Default Location

Frappe Books has a default location called Stores set. This can be changed from the Inventory tab under Settings. :::

::: tip Creating Locations

Additional locations can be created when making an inventory transaction. To do so click the Create option in the Location selection dropdown. :::

Stock Quantity
--------------

Since an outward movement reduces the stock quantity at a location, if the location has an insufficient quantity of stock, the transaction will not be allowed.

This means that negative stock movement will not be allowed. This applies even to backdated entries that may cause negative stock in the future.

To enable the outward movement, two things can be done:

1. Change the location to one that has sufficient quantity.
2. Create an inward movement of the selected Item to the selected Location before the blocked transaction.

::: tip Stock Balance

To check which Location has sufficient quantity of an Item check the Stock Balance report. :::



---

Now that you know how to enable inventory and are familiar with the basic concepts, you can move onto reading about the inventory transactions.

  

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

  

<!-- page: books/books__purchase-invoices.md -->
---
title: "Purchase Invoices"
space: "Books"
url: "https://docs.frappe.io/books/purchase-invoices"
updated: "2026-01-30"
---

Purchase Invoices are bills that your supplier sends you when you make a purchase.

It is a transactional entry that denotes a purchase.

Creating Purchase Invoices
--------------------------

If you have set up your Frappe Books with Accounts, Taxes, Purchase Items, and Suppliers, creating a Purchase Invoice is as simple as it gets.

First navigate to the Purchase Invoices page

`Purchases > Purchase Invoices`

Then click on the blue `+` button to open the Purchase Invoice form.

[![Purchase Invoice Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/purchase-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/purchase-invoice.png)  


1. Select the Supplier from whom you will be making a purchase.
2. Click on Add Row and select the Item being purchased. Default Tax will be fetched you can change it if required.
3. Enter the Quantity.
4. You can add more items or if you are done, click on Save.
5. Once finalized, click on Submit. Frappe Books will do the required ledger entries against the appropriate accounts.

This invoice is now in *“Submitted”* state, it cannot be edited. The purchase transaction has been recorded.

Making Purchase Payments
------------------------

Once a purchase invoice has been submitted, you’ll need to record payment against it to denote that you’ve paid the money.

To make a Payment first navigate to the Purchase Invoice, then click on the `...` menu button. Then click the Make Payment option.

[![Purchase Invoice Status](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/purchase-payment.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/purchase-payment.png)  


This will open the Payment quick edit form with the outstanding amount auto-filled.

[![Purchase Invoice Payment](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/purchase-payment-quickedit.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/purchase-payment-quickedit.png)  


You can change the values and click on Save. This will Save and Submit the Payment.

On making the Payment, Frappe Books will make the necessary ledger entries to increase the payment amount in Accounts Payable and decrease the amount in your Bank or Cash Account.

It will also update the Outstanding Amount on the invoice form.

::: info Purchase Invoice Status Until Payments are made to settel the Outstanding Amount, the Purchase Invoice will be in the **Unpaid** state.

Once the Outstanding Amount reaches 0, the status will change to **Paid**. :::

### Auto Payments

You can simplify the *Purchase Invoice → Payment* workflow by using Auto Payments. For this you just need to set the default accounts for Purchase Payment.

This can be done in `Setup > Settings > Defaults > Auto Payments`: [![Payment Accounts](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/payment-accounts.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/payment-accounts.png)  


Once this is set, whenever you Submit a Purchase Invoice a Payment entry will automatically be created.

::: tip Disable Auto Payment for a Purchase Invoice

You can disable Auto Payment for a single Purchase Invoice by unchecking the Make Payment On Submit check box in the Settings tab before Submitting the Purchase Invoice entry.

[![Disable Auto Payment](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/auto-payment.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/auto-payment.png) :::

Purchase Invoice Return
-----------------------

The user can create a Purchase Invoice Return directly from the original Purchase Invoice document or manually from the New Purchase Invoice Entry.

### Creating a Purchase Invoice Return

1. Open the original Purchase Invoice document.
2. Click on **Create > Return**. [![Create Purchase Invoice Return](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/pinv-create-return.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/pinv-create-return.png)
3. The Party and Item details will be fetched as set in the original Purchase Invoice document. You can set the quantity of Items returned in negative numbers. [![Purchase Invoice Return Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/pinv-return-form.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/pinv-return-form.png)
4. Save and Submit.

::: info The Item quantity and Payment amount will be in negative figures to indicate that it's a return. :::

### Creating Manually

1. Navigate to the Purchase Invoice page `Purchases > Purchase Invoice`
2. Click on **Return Against** then select the target Purchase Invoice against which you returned the Items. [![Set Is Return](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/pinv-select-return-against-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/pinv-select-return-against-invoice.png)
3. Fill Item details.
4. Save and Submit.

Purchase Invoice impact on General Ledger
-----------------------------------------

The Purchase Invoice Return entry will create General Ledger entries to reverse the impact of the original Purchase Invoice.

[![Purchase Invoice Return in General Ledger](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/pinv-return-in-gl.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/pinv-return-in-gl.png)  


  

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

[![Create Purchase Receipt From a Purchase Invoice](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/from-purchase-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/from-purchase-invoice.png)  


::: tip Back Reference

This will create a Purchase Receipt with a reference to the Purchase Invoice and allows you to view all created Purchase Receipts from the Purchase Invoice. :::

### From the List View

To do this first navigate to the Purchase Receipt page: `Inventory > Purchase Receipt` then click on the blue `+` button.

The creation method is shared with with other transactional entries, for more information check [this link](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries.html#creating-an-entry).

::: warning No Back Reference

This method doesn't create links to any Purchase Invoices and is an isolated entry. :::

### Purchase Receipt Form

After selecting one of the above two methods of creating a Purchase Receipt, you will see the Purchase Receipt form.

[![Purchase Receipt Form](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/purchase-receipt-form.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-form.png)  


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
2. Click on `Create > Return`. [![Create Purchase Receipt Return](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/create-purchase-receipt-return.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/create-purchase-receipt-return.png)
3. The Party and Item details will be fetched from the original Purchase Receipt entry. You can set the quantity of Items returned. [![Purchase Receipt Return Form](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/purchase-receipt-return-form.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-return-form.png)
4. Save and Submit.

::: info Item quantity and Payment amount will be in negative to indicate that it is a return. :::

How does Purchase Receipt Return affect General Ledger
------------------------------------------------------

The Purchase Receipt Return entry will create General Ledger entries to reverse the impact of the original Purchase Receipt.

[![Purchase Receipt Return in General Ledger](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/purchase-receipt-return-in-general-ledger.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/purchase-receipt-return-in-general-ledger.png)  


View Ledger Entries
-------------------

After a Purchase Receipt is submitted, both Stock Ledger and General Ledger entries are created.

To view these you can click on the View button and select the one you would like to see.

[![View Ledger Entries](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/view-purchase-receipt-ledger-entries.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-purchase-receipt-ledger-entries.png)  


  

<!-- page: books/books__quick-search.md -->
---
title: "Quick Search"
space: "Books"
url: "https://docs.frappe.io/books/quick-search"
updated: "2026-01-30"
---

The Quick Search interface is a quick way to navigate around in Frappe Books. To activate it you can click on the search button in the header:

[![Quick Search Bar](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/search-bar.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-bar.png)  


Or you can press `Ctrl + K` or `Cmd + K` depending on your operating system.

Dialog
------

[![Quick Search Dialog](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/search-dialog.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-dialog.png)  


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

[![Quick Search Filters](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/search-filters.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/search-filters.png)  


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

[![Report Sections](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/report-sections.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/report-sections.png)  


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

[![Sales Invoice Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sales-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-invoice.png)  


1. Select the Customer to whom you will be making a sale.
2. Click on Add Row and select the Item being sold. Default Tax will be fetched you can change it if required.
3. Enter the Quantity.
4. You can add more items or if you are done, click on Save.
5. Once finalized, click on Submit. Frappe Books will do the required ledger entries against the appropriate accounts.

This invoice is now in *“Submitted”* state, it cannot be edited. The sales transaction has been recorded.

Editing an Invoice Item
-----------------------

To edit the values of an Invoice Item click on the edit button on the item row [![Edit Invoice Item](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/invoice-item.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/invoice-item.png)  


From here you can change the item description, HSN code check the Taxed Amount, etc.

::: tip Setting the Taxed Amount You can directly set the Taxed Amount, Frappe Books will calculate the Rate of the Item automatically. :::

Making Sales Payments
---------------------

Once a sales invoice has been submitted, you’ll need to record payment against it to denote that you’ve received the money.

To make a Payment first navigate to the Sales Invoice, then click on the `...` menu button. Then click the Make Payment option.

[![Sales Invoice Status](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sales-payment.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-payment.png)  


This will open the Payment quick edit form with the outstanding amount auto-filled.

[![Sales Invoice Payment](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sales-payment-quickedit.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sales-payment-quickedit.png)  


You can change the values and click on Save. This will Save and Submit the Payment.

On making the Payment, Frappe Books will make the necessary ledger entries to reduce the payment amount from Accounts Receivable and increase the amount in your Bank or Cash Account.

It will also update the Outstanding Amount on the invoice form.

::: info Sales Invoice Status Until Payments are made to settle the Outstanding Amount, the Sales Invoice will be in the **Unpaid** state.

Once the Outstanding Amount reaches 0, the status will change to **Paid**. :::

### Auto Payments

You can simplify the *Sales Invoice → Payment* workflow by using Auto Payments. For this you just need to set the default accounts for Sales Payment.

This can be done in `Setup > Settings > Defaults > Auto Payments`: [![Payment Accounts](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/payment-accounts.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/payment-accounts.png)  


Once this is set, whenever you Submit a Sales Invoice a Payment entry will automatically be created.

::: tip Disable Auto Payment for a Sales Invoice

You can disable Auto Payment for a single Sales Invoice by unchecking the Make Payment On Submit check box in the Settings tab before Submitting a Sales Invoice entry.

[![Disable Auto Payment](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/auto-payment.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/auto-payment.png) :::

Sales Invoice Return
--------------------

The customer could return an already sold Item due to quality issues or any other reasons.

To reflect this you can create a Sales Invoice Return from the original Sales Invoice entry or manually create one from a new Sales Invoice Entry.

### Creating a Sales Invoice Return

1. Open the original Sales Invoice document, against which customer returned the Items.
2. Click on **Create > Return**. [![Create Sales Invoice Return](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sinv-create-return.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-create-return.png)
3. The Party and Item details will be fetched as set in the original Sales Invoice document. You can set the quantity of Items returned in negative numbers. [![Sales Invoice Return Form](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sinv-return-form.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-return-form.png)
4. Save and Submit.

::: info The Item quantity and Payment amount will be in negative figures to indicate that it's a return. :::

### Creating Manually

1. Navigate to the Sales Invoice page `Sales > Sales Invoice`
2. Click on **Return Against** then select the target Sales Invoice against which customer returned the Items. [![Select return invoice](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sinv-select-return-against.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-select-return-against.png)
3. Fill Item details.
4. Save and Submit.

Sales Invoice Return impact on General Ledger
---------------------------------------------

The Sales Invoice Return entry will create General Ledger entries to reverse the impact of the original Sales Invoice.

[![Sales Invoice Return in General Ledger](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/sinv-return-in-gl.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/sinv-return-in-gl.png)  


Printing the Sales Invoice
--------------------------

To export the Sales Invoice as a PDF, click on the Print button next to the `...` menu above the Sales Invoice Form.

This will open the Print View, you can click on the Customize button to customize it.

[![Print View](https://github.com/frappe/books_docs/raw/master/docs/transactions/images/print-view.png)](https://github.com/frappe/books_docs/blob/master/docs/transactions/images/print-view.png)  


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

[![Enable Has Serial Number](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/item-has-serial-number.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/item-has-serial-number.png)  


::: info Track Item **Has Serial Number** can be enabled only if **Track Item** is set. :::

Mentioning Item Serial Number
-----------------------------

Once a Serial Number has been enabled for an [Item](https://github.com/frappe/books_docs/blob/master/entries/items), transactions involving the Item that update Inventory (such as Stock Movements, Shipments, and Purchases) must include the Serial Number.

This can be done by clicking the edit button on the table row and entering the Serial Number one per quantity.

[![Mentioning Serial Numbers](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/mentioning-serial-number.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/mentioning-serial-number.png)  


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

[![General Settings](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/general-settings.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/general-settings.png)  


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

[![Defaults](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/defaults.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/defaults.png)  


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

[![Invoice Settings](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/print-settings.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/print-settings.png)  


Settings here can be altered to customize the Print View of an Invoice.

::: tip Print View These settings can also be altered from the [Print View](https://github.com/frappe/books_docs/blob/master/transactions/sales-invoices#printing-the-sales-invoice) of an Invoice :::

System Settings
---------------

[![System Settings](https://github.com/frappe/books_docs/raw/master/docs/miscellaneous/images/system-settings.png)](https://github.com/frappe/books_docs/blob/master/docs/miscellaneous/images/system-settings.png)  


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

[![Journal Entry Form](https://github.com/frappe/books_docs/raw/master/docs/setting-up/images/journal-entry.png)](https://github.com/frappe/books_docs/blob/master/docs/setting-up/images/journal-entry.png)  


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

[![Create Shipment From a Sales Invoice](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/from-sales-invoice.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/from-sales-invoice.png)  


::: tip Back Reference

This will create a Shipment with a reference to the Sales Invoice and allows you to view all created Shipments from the Sales Invoice. :::

### From the List View

To do this first navigate to the Shipment page: `Inventory > Shipment` then click on the blue `+` button.

The creation method is shared with with other transactional entries, for more information check [this link](https://github.com/frappe/books_docs/blob/master/transactions/transactional-entries.html#creating-an-entry).

::: warning No Back Reference

This method doesn't create links to any Sales Invoices and is an isolated entry. :::

### Shipment Form

After selecting one of the above two methods of creating a Shipment, you will see the Shipment form.

[![Shipment Form](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/shipment-form.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-form.png)  


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
2. Click on `Create > Return`. [![Create Shipment Return](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/create-shipment-return.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/create-shipment-return.png)
3. The Party and Item details will be fetched from the original Shipment entry. You can set the quantity of Items returned. [![Shipment Return Form](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/shipment-return-form.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-return-form.png)
4. Save and Submit.

::: info Item quantity and Payment amount will be in negative to indicate that it is a return. :::

Shipment Return impact on General Ledger
----------------------------------------

The Shipment Return entry will create General Ledger entries to reverse the impact of the original Shipment.

[![Shipment Return in General Ledger](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/shipment-return-in-general-ledger.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/shipment-return-in-general-ledger.png)  


View Ledger Entries
-------------------

After a Shipment is submitted, both Stock Ledger and General Ledger entries are created.

To view these you can click on the View button and select the one you would like to see.

[![View Ledger Entries](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/view-shipment-ledger-entries.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-shipment-ledger-entries.png)  


  

<!-- page: books/books__stock-balance.md -->
---
title: "Stock Balance"
space: "Books"
url: "https://docs.frappe.io/books/stock-balance"
updated: "2026-01-30"
---

Stock Balance is a report that displays the current stock quantities, value and valuation rate by Item and Location.

[![Stock Balance](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/stock-balance.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-balance.png)  


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

[![Stock Ledger](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/stock-ledger.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-ledger.png)  


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

[![Stock Movement](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/stock-movement.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/stock-movement.png)  


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

[![View Stock Entries](https://github.com/frappe/books_docs/raw/master/docs/inventory/images/view-stock-entries.png)](https://github.com/frappe/books_docs/blob/master/docs/inventory/images/view-stock-entries.png)  

<!-- page: books/books__taxes.md -->
---
title: "Taxes"
space: "Books"
url: "https://docs.frappe.io/books/taxes"
updated: "2026-01-30"
---

To calculate the amount of tax on an Item's purchase or sale, a Tax entry has to be selected on the invoice row.

[![Invoice Row](https://github.com/frappe/books_docs/raw/master/docs/entries/images/invoice-row.png)](https://github.com/frappe/books_docs/blob/master/docs/entries/images/invoice-row.png)  


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

   ![](/private/files/Screenshot%20from%202025-08-11%2009-48-11.png)

Before initiating sales, a POS shift must be opened to record opening balances and enable accurate tracking of cash and other payment methods throughout the session.

**Steps to Create an Open POS Shift**

1. Cash in Denominations

Enter the quantity of each currency denomination (e.g., ₹1000, ₹500, ₹100). The system will automatically calculate the total opening cash amount based on these inputs.

2. Opening Amounts by Payment Method

* The calculated cash amount is automatically populated under the “Cash” payment method.

* Opening balances for other payment methods (e.g., Card, UPI, Wallet) can be entered if applicable.

3. Once all amounts are verified, click Submit. The POS shift will be marked as open, recording the shift’s opening date and time.


### 2. Creating a POS Invoice

![](/private/files/Screenshot%20from%202025-08-11%2010-16-20.png)

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

   ![](/private/files/Screenshot%20from%202025-08-11%2011-24-53.png)


Items can be selected in two ways: by clicking on the item name or by scanning the barcode.

* Enter Barcode / Weight-enabled barcode in the box as shown in the image, the item will be automatically added to the cart.

* If the product list in the dropdown is very long, use the search field by typing the product name in the search box.

**Filter by Group:** A field that allows filtering and displaying items based on their assigned item group. When an item group is selected from the dropdown list, only items belonging to that group are shown.

![](/private/files/Screenshot%20from%202025-08-11%2011-10-06.png)

* To change the quantity of an item, click the expand arrow and either enter the desired quantity in the **Transfer Quantity** field or use the up/down arrows to adjust it.

* To remove an item from the cart, click the delete button next to the corresponding item.

### 4. Additional POS Features


![](/private/files/Screenshot%20from%202025-08-12%2011-30-14.png)

**1.Grid View:** Displays items in a grid format with images when the grid view icon is clicked.

**2.[Sales Invoice](https://docs.frappe.io/books/sales-invoices) List:** Redirects to the Sales Invoice List.

**3.[Loyalty Program](https://docs.frappe.io/books/loyalty-program):** Shows the loyalty points earned by the selected customer. Points can be redeemed from this view. The button is disabled if the customer has no loyalty points.

**4.[Coupon Code](https://docs.frappe.io/books/coupon-code):** Allows redemption and application of available coupon codes for the selected items. The button is disabled if no coupon codes are available.

**5.[Price List](https://docs.frappe.io/books/price-list):** Displays applicable price lists for the selected items, allowing you to apply them. The button is disabled if no price list is available.

**6.[Item Enquiry](https://docs.frappe.io/books/item-enquiry):** Allows the user to record and track specific item-related queries.This feature helps maintain detailed records of customer enquiries for better follow-up and service.

### 5. Cart Actions

   ![](/private/files/Screenshot%20from%202025-08-11%2012-06-19.png)
   
* Total Quantity: The Total Quantity refers to the combined number of all items included in a transaction or order.

* Item Discounts: The Item Discounts refer to price reductions applied to specific products or services in the order.

* Grand Total: The Grand Total is the final amount payable after applying all discounts, charges, and taxes to the subtotal.

* Save Button: The system immediately stores the current transaction as a Draft Invoice, retaining all entered details for future review, modification, or completion.

* Cancel Button: The system discards the current transaction and resets the POS interface to its default state, ready for a new entry.

* Held Button: The system displays two sections: 

  * Saved - Shows all transactions that have been saved but not yet submitted.
  
  * Submitted – Displays all submitted invoices, including those that are partially paid.


![](/private/files/Screenshot%20from%202025-08-11%2014-22-42.png)

A search function is available within the Held section to quickly locate invoices by their invoice name.

* Return Button: It displays a list of all return invoices, and selecting an invoice will redirect the user and add its items to the POS cart.


![](/private/files/Screenshot%20from%202025-08-11%2014-28-48.png)

A search function is available to quickly locate invoices by their invoice name.

* PAY Button: After adding items and selecting the customer, click the **Pay** button to view available payment methods, including **Cash**, **Bank**, and **Transfer**; upon selection, the payable amount will be displayed for confirmation.

### 6. Payment Workflow

![](/private/files/Screenshot%20from%202025-08-11%2014-30-54.png)

1. Click Pay after adding items and selecting the customer.

2. Choose a payment method (e.g., Cash, Bank, Transfer). The payable amount is displayed for confirmation.

Available payment actions:

* Submit: Marks the invoice as submitted and saves it under Held > Submitted.

* Cancel: Cancels the payment process and closes the payment interface.

* Pay: Completes the payment and generates the invoice.

* Pay & Print: Completes the payment, generates the invoice, and prints it immediately.

### 7. Close POS Shift

![](/private/files/Screenshot%20from%202025-08-11%2014-53-23.png)


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

[![Trial Balance](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/trial-balance.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/trial-balance.png)  


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

[![Trial Balance Folded Rows](https://github.com/frappe/books_docs/raw/master/docs/analytics/images/trial-balance-folded.png)](https://github.com/frappe/books_docs/blob/master/docs/analytics/images/trial-balance-folded.png)  


Rows in the Trial Balance report which display group accounts can be clicked to fold all the rows underneath them.

  
