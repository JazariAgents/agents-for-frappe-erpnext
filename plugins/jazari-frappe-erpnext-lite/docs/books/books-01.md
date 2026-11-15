<!-- Frappe documentation: books, part 1 of 4. Index: docs/INDEX.md -->

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

  
