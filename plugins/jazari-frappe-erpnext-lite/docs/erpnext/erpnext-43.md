<!-- Frappe documentation: erpnext, part 43 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__plant-floor.md -->
---
title: "Plant Floor"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/plant-floor"
updated: "2026-02-26"
---

  


Plant Floor feature in the ERPNext is used to visualize the status of machines and workstations within the corresponding plant floor. This feature provides visual interface for processing job cards.

How It Works
------------

* Create the plant floor and set the warehouse (Manufacturing -> Plant Floor -> New)
* Create machine using workstation and select the plant floor.
* Set the Illustration for the active and inactive status in the workstation.

After that you can see the status of machines and workstations using plant floor.

[Screenshot on the live page]


### Visualize Stock Summary

Using plant floor, users can visualize the stock of the corresponding plant floor. Using this feature user can add or move the stock.

[Screenshot on the live page: stock-summary]  


### Visualize Job Cards

[Screenshot on the live page: job_cards]  

<!-- page: erpnext/erpnext__point-of-sale.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/point-of-sale"
updated: "2026-02-28"
---

## **Introduction**

### **What is POS?**

The Point of Sale module in ERPNext offers a streamlined solution for managing retail transactions efficiently. It seamlessly integrates with inventory management, updating stock levels in real-time and preventing stock discrepancies. ERPNext’s POS also supports multiple payment methods, streamlining the payment process for customers and reducing transaction errors.

With built-in reporting and analytics, businesses can gain valuable insights into sales performance, top-selling items, and customer trends, helping them make informed decisions to improve overall efficiency and profitability in their retail operation.

###  **Why Use POS in ERPNext?**

- Seamlessly integrates retail transactions with Inventory and Accounting. 
- Enables real-time or deferred posting depending on session closing. 
- Supports multiple payment methods and loyalty programs. 
- Reduces stock discrepancies and improves operational efficiency. 

<!-- page: erpnext/erpnext__point-of-sale__setup.md -->
---
title: "Getting Started"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/point-of-sale/setup"
updated: "2026-02-28"
---

You require to setup a few things to ensure smooth POS billing. 

Ensure you already have:

1. POS Profile (defined with payment methods & defaults)
2. Items with selling prices in Price Lists
3. Customers defined
4. Warehouse configured (for stock posting)

<!-- page: erpnext/erpnext__portal-login.md -->
---
title: "Portal Login"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/portal-login"
updated: "2026-02-28"
---

To login into the customer account, the customer has to use his Email Address and the password sent by ERPNext; generated through the sign-up process.

[Screenshot on the live page: Website User Signup]  

<!-- page: erpnext/erpnext__pos-invoice-consolidation.md -->
---
title: "POS Invoice Consolidation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/pos-invoice-consolidation"
updated: "2026-02-26"
---

In the version 13 refactor of the Point of Sale, in an effort to add speed to the Point of Sale, the sales from the POS session do not affect the stock and accounting ledgers until a Closing POS Voucher is submitted for that session. It functions like so: 

1. Each transaction from the POS screen now creates an intermediate invoice (called a POS Invoice) which doesn’t update the stock and accounting ledgers to keep it as fast as possible. This is also called a “sub-ledger”. Separating the POS ledger from the General Ledger makes the system a lot more scalable.
2. The stock and accounting entries are now created at the end of day while closing a POS session by a single sales invoice which merges all the intermediate invoices created throughout the day.
3. This single consolidated sales invoice only creates 3-4 ledger entries. The older system would create n x 3 ledger entries where ‘n’ is the number of invoices created throughout the day.
4. Since drastically fewer ledger entries are made, the load on the general ledger is also eased, making it faster.

### How Stock is Tracked Until a POS Session is Closed

While it is true that the Stock Ledger will disclude transactions from any active POS session, the stock levels from this "sub-ledger" update the Stock Projected Quantity Report.

> Stock > Stock Reports > Stock Projected Quantity

[Screenshot on the live page: Stock Projected Quantity Report]

In the above image, the "Actual Qty" column represents the value of the stock ledger. The "Reserved for POS Transactions" represents the "Actual Qty" less what quantities are currently reserved because of active POS sessions that have not yet made entries on the Stock Ledger because the sessions have not been closed. Note also that "Projected Qty" ("Active Qty" less quantities reserved for the POS, production, etc.) adds a quantity of 100 to the first line item because of an order for 100 units that has yet to be received.

Within the Point of Sale, however, quantities on order but not received will not be reflected in the "Available Qty at Warehouse" field in the Item Details view. In the instance below, as there's not enough quantity on-hand, the transaction won't be permitted. This applies to any and all open POS sessions active at any time and is applied globally (as in, the transaction from one session affects the quantities available for all other open sessions).

[Screenshot on the live page: Available Quanity at Warehouse]

[Screenshot on the live page: Item Unavailable]

<!-- page: erpnext/erpnext__pos-profile.md -->
---
title: "POS Profile"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/pos-profile"
updated: "2026-02-26"
---

In ERPNext, a POS profile allows using the Point of Sale feature to some extent for “Paid” Sales Invoice.

POS includes advanced features to cater to different functionality, such as inventory management, financials, warehousing, etc., all built into the POS software. 

If you are in retail operations, you want your Point of Sale to be as quick and efficient as possible. To do this, you can create a POS Profile for a user.

POS Profile is also utilized in 

To access the POS Profile list, go to:

*Home > Selling > POS > POS Profile*

### How to create POS Profile

1. Go to POS Profile List, click on “Add POS Profile”.
2. Select the Company and Warehouse. 
3. Add Payment Methods.
4. Set Currency, Write Off Account, Write Off Cost Center and Write Off Limit.
5. Save.



## Additional Options when creating a POS Profile

*(screenshot — not bundled; see the live page URL in this file's front matter)*

- **Customer:** If a Customer is set on POS Profile, selecting the POS Profile on the Sales Invoice/POS Invoice will set the same Customer.



### Applicable for Users

By default, all Sales Users can access the POS Profiles created in ERPNext. However, if you want only certain Users to access certain POS Profiles, you can add them to the table. Once even one User is set in the POS Profile, other Users cannot use this POS Profile for retail transactions.

Setting POS Profile as default: On ticking the Default checkbox in the table, the current POS Profile becomes the default POS Profile for that User. So, the next time the User logs into the system, the POS Profile will be set by default.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

*Note: If you specify a particular User, the POS setting will be applied only to that User. If the User option is left blank, the setting will be set for all users. To understand how POS works, visit the Point of Sale page.*

### Payment Methods



*(screenshot — not bundled; see the live page URL in this file's front matter)*

  


Set up payment modes in the table; the default will be cash if nothing is set here. Only the modes set here will be available when using POS. After adding payment modes, set one of them as the default payment method by ticking the checkbox.

To allow Payment Methods on Return Invoices, set the “Allow in Returns”.



### Configurations



*(screenshot — not bundled; see the live page URL in this file's front matter)*

The Configurations section in the POS Profile applies only to the Point of Sale (POS) view in ERPNext. These settings control the behavior, layout, and user experience of the POS interface and do not affect standard Sales Invoices or other views.

- **Hide images**: By default, POS displays items in Grid View. However, enabling “Hide images” configuration will switch to List View.
- **Ignore Pricing Rul**e: Any active Pricing Rule will be ignored for this POS Profile.
- **Hide unavailable Items**: Items with non-positive stock will not be displayed.
- **Allow User to Edit Rate**: Users will be allowed to edit the rate on the POS Item Detail View.
- **Automatically Add Filtered Item To Cart**: When enabled, the filtered item is automatically added to the POS cart without manual selection. Applies only to the POS view.
- **Allow User to Edit Discount**: Users will be allowed to edit the discount on the POS Item Detail View.
- **Validate Stock on Save**: Validate stock availability on saving the Invoice.
- **Set Grand Total to Default Payment Method**: Auto-set Grand Total to Default Payment Method during checkout.
- **Print Receipt on Order Complete**: Open Print Preview for Invoice automatically on Order Complete.
- **Allow Partial Payment**: Allow partial payment to POS Invoices.
- **Action on New Invoice**: Action on clicking the New Invoice Button on POS in case of an unsaved invoice for an ongoing Order.
  - **Always Ask**: Ask the user if they want to save the ongoing invoice or discard the invoice and load a new invoice.
  - **Save Changes and Load New Invoice**: Auto-save the ongoing incomplete invoice and load a new invoice.
  - **Discard Changes and Load New Invoice**: Discard the incomplete invoice and load a new invoice.  


### Setting Item Group and Customer Group

On setting an Item Group/Customer Group in a POS Profile, the group will be automatically selected when making transactions with the POS Profile.

  




*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Print Settings



*(screenshot — not bundled; see the live page URL in this file's front matter)*

- **Print Format:** You can set a Print Format which will decide what the layout of the printed document will look like. To know more, visit the Print Format page.
- **Letterhead:** You can print your POS Sales Invoice on your Company's letterhead. Know more here.
- **Print Headings:** POS Sales Invoice headings can also be changed when printing the document. For example, the heading can be 'Invoice', or 'Bill'. You can do this by selecting a Print Heading. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more here.
- **Terms and Conditions:** There may be certain terms and conditions on the Item you're selling, these can be applied here. To know about adding Terms and Conditions, click here.



### **Accounting**

[Screenshot on the live page]

- **Price List**: A Price List stores the Item Prices. Setting a Price List here will fetch the Item Prices for the current POS Profile from that Price List.
- **Currency**: By default, this will be set according to the Company's default currency. However, you can change it. In case you change the currency, remember to change the accounts too.
- **Taxes and Charges**: Selecting a Sales Taxes and Charges Template or Purchase Taxes and Charges Template here will automatically apply the taxes and charges to the POS transaction.
- **Apply Discount On**: Here you can set whether the discount is to be applied on the Grand Total (pre tax amount) or the Net Total (post tax amount).
- **Tax Category**: On selecting a Tax Category here, the Tax Rules associated with the Tax Category will be applied to each transaction performed from this POS Profile.

The following accounts can be set so that the general ledger is updated accordingly:

- Account for Change Amount
- Write Off Account
- Write Off Cost Center
- Income Account
- Expense Account

### **Accounting Dimensions**

Accounting Dimensions lets you tag transactions based on a specific Territory, Branch, Customer, etc. This helps in viewing accounting statements separately based on the criteria selected. To know more, visit the Accounting Dimensions page.

*Note: Cost Center is treated as a dimension by default.*

<!-- page: erpnext/erpnext__pos-workflows.md -->
---
title: "POS Workflows"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/pos-workflows"
updated: "2026-02-28"
---

### **POS Workflows**

#### **Open POS Session**

1. Go to **Point of Sale** workspace.
2. Select a **POS Profile**.
3. Select Customer.
4. Add items from the item list.
5. Edit quantities as needed.

*Note:* You need to set a default Warehouse for stock impact. If both Item and POS Profile define a Warehouse, the POS profile warehouse gets priority. 



 **How to Create a POS Invoice**

1. Add items to cart in the POS screen.
2. If editing rate/discount is needed, enable options in the POS Profile.
3. Click **Pay** and select payment mode.
4. Submit — a **POS Invoice** is created.

**POS Opening Entry**

Before selling, open a session with an **Opening Entry**.  
This sets the session start and can capture opening cash if required. 



**POS Closing Entry**

At the end of the session:

1. Go to **POS Closing Entry**
2. Select the POS Profile and closing period
3. Submit — stock and accounting postings occur.

**Loyalty Integration**

ERPNext supports linkage of loyalty programs to customers, allowing:

- Earning points on POS invoices
- Redemption during checkout  
To set up the loyalty program, follow the ++[Loyalty Program](https://docs.frappe.io/erpnext/user/manual/en/loyalty-points-redemption-in-pos)++ documentation.

<!-- page: erpnext/erpnext__post-dated-cheque-entry.md -->
---
title: "Post Dated Cheque Entry | ERPNext Documentation"
description: "Record and clear post-dated checks without recognizing bank settlement too early in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/post-dated-cheque-entry"
updated: "2026-08-01"
---

A post-dated check is received or issued before the date on which it can be deposited. Record it with its reference date and use a clearing account when your accounting policy requires settlement to be recognized only after the bank clears it.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Post Dated Cheque Entry

1. Create the Payment Entry with the check number and future reference date.
2. Use the configured post-dated check or clearing account when required.
3. Submit only according to your approval and accounting policy.
4. After the bank clears the check, transfer or reconcile the amount to the bank account.
5. If it is returned or becomes stale, reverse it through the approved process.

[Screenshot on the live page: Post Dated Cheque Entry in ERPNext]

## Important fields and what they mean


| Field                 | What it controls                                   |
| --------------------- | -------------------------------------------------- |
| Reference No          | Check number.                                      |
| Reference Date        | Date printed on the check.                         |
| Posting Date          | Accounting date of the entry.                      |
| Paid From and Paid To | Party and clearing or bank accounts.               |
| Clearance Date        | Actual settlement date used during reconciliation. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The cheque affects the ledger earlier than expected

Posting Date controls the General Ledger date. Reference Date records the cheque date but does not move the accounting entry. Follow the documented clearing-account workflow when recognition and bank clearance occur at different times.

### The cheque is missing from Bank Reconciliation

Confirm that the submitted entry uses the selected bank account and has not already been cleared. Check the reconciliation date range and bank clearance status.

### A post-dated cheque was dishonoured

Reverse or cancel it using the approved workflow so the invoice becomes outstanding again, and record bank charges separately when applicable. Preserve the cheque reference and dishonour evidence.

## Frequently asked questions

### What is the difference between Posting Date, Reference Date, and Clearance Date?

Posting Date determines the ledger period. Reference Date records the cheque or bank reference date. Clearance Date records when the bank actually cleared it.

### Can a post-dated cheque remain in draft until it clears?

A draft does not affect the ledger or invoice outstanding amount. Use this only when it matches your accounting policy; otherwise use a clearing account workflow that records receipt without treating the bank as cleared.

### Does setting a Clearance Date change the original ledger date?

It does not. The clearance date supports bank reconciliation while the original posting remains on its Posting Date.

### How can future cheque obligations be reported?

Use consistent cheque references, dates, clearing accounts, and reports. Add a controlled custom report only when standard views do not meet the operational requirement.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__prepare-and-map-legacy-data.md -->
---
title: "Prepare and Map Legacy Accounting Data | ERPNext Documentation"
description: "Clean, map, classify, and validate legacy accounting data before importing masters, invoices, balances, stock, and assets into ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/prepare-and-map-legacy-data"
updated: "2026-08-14"
---

Data exported from an older accounting system rarely matches ERPNext exactly. Preparing and mapping means cleaning that export and translating its customers, suppliers, accounts, tax codes, currencies, and identifiers into values ERPNext can import safely.



Nova Industries may have three spellings for the same customer, inactive ledger accounts, dates in mixed formats, and tax labels that do not exist in the new Chart of Accounts. Resolving those differences before import prevents duplicates and makes validation far easier than correcting submitted records later.



This page shows how to profile the source data, define a mapping workbook, remove unnecessary history, standardize values, and produce import files that can be tested repeatedly.

## Freeze the source extract

Create a dated migration folder and store:

- the original unedited exports;
- cleaned working files;
- approved import files;
- ERPNext import results;
- reconciliation files;
- sign-off evidence.

Never overwrite the original export. Record the source system, report name, filters, company, currency, period, extraction time, and person responsible.

## Clean source records

Standardize:

- names, capitalization, and spaces;
- date format as `YYYY-MM-DD`;
- decimal and thousands separators;
- currency codes;
- tax identifiers;
- country, state, and postal codes;
- units of measure;
- blank values and zero values;
- debit and credit signs.

Remove duplicate parties only after deciding which record survives and how the balances are combined.

## Build mapping tables

Create an approved old-to-new mapping for every controlled field.


| Legacy value    | ERPNext value         | Action        |
| --------------- | --------------------- | ------------- |
| Sales - Devices | Product Sales - NET   | Map           |
| Admin East      | Corporate Sales - NET | Map           |
| Cust-00482      | Northstar Retail      | Merge and map |
| WH-A            | Main Warehouse - NET  | Map           |
| USD             | USD                   | Keep          |


Do not use spreadsheet formulas that silently return blank when a mapping is missing. Add a validation column that marks every unmapped value as an error.

## Map the Chart of Accounts

For every legacy account, record:

- ERPNext account;
- parent group;
- root type;
- group or ledger;
- account type;
- account currency;
- whether it is a control account;
- opening import method;
- whether it will be disabled after migration.

Map retired accounts to an appropriate active account only with finance approval. Keep separate tax, bank, receivable, payable, stock, fixed-asset, depreciation, and equity accounts when reporting requires them.

## Prepare outstanding invoices

Include one row per open invoice or credit note:

- party;
- invoice number;
- posting date;
- due date;
- invoice currency;
- exchange rate;
- original total;
- outstanding amount;
- receivable or payable account;
- Cost Center where required;
- legacy reference.

Do not import paid invoices through the Opening Invoice Creation Tool.

## Prepare the opening Trial Balance

Start from the final Trial Balance after all legacy adjustments. Add columns for:

- legacy account and balance;
- ERPNext account;
- debit;
- credit;
- import method;
- document reference;
- imported amount;
- difference;
- reviewer note.

Classify each line as **Invoice**, **Payment/Advance**, **Bank/Cash**, **Stock**, **Asset**, or **Residual Journal Entry**. Each source balance must appear in one category only.

## Prepare stock and assets

For stock, include Item, Warehouse, quantity, valuation rate, and total value. Reconcile quantity and value separately.

For assets, include asset category, asset name, purchase date, available-for-use date, gross cost, accumulated depreciation, net book value, useful life, remaining periods, location, custodian, and finance book.

## Run pre-import checks

- every required parent exists;
- every linked value uses the exact ERPNext name;
- dates fall in a valid Fiscal Year;
- debit equals credit;
- outstanding invoice totals match ageing;
- stock quantity times rate explains total value;
- asset cost less accumulated depreciation equals net book value;
- no account is assigned to two import methods;
- foreign-currency totals reconcile in both currencies.

## Related topics

- [Import Accounting Masters](https://docs.frappe.io/erpnext/import-accounting-masters)
- [Import Chart of Accounts](https://docs.frappe.io/erpnext/import-chart-of-accounts)
- [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)
- [Data Import](https://docs.frappe.io/erpnext/data-import)

<!-- page: erpnext/erpnext__prepared-report.md -->
---
title: "Using Prepared Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/prepared-report"
updated: "2026-03-04"
---


Many times when generating a report that deals with a large volume of data, say, a GL report for the entire year, you may end up getting the following error message: **Request Timed Out**. This occurs as there is a lot of data to be processed and presented on the report page, but not enough server resource hence resulting in a time out.

For better processing of such reports, ERPNext offers Prepared Reports (since v11). When a report is set as a Prepared Report, it is generated through a [background job](/framework/user/en/guides/app-development/running-background-jobs), and once ready, is available for users to view.

## Steps to Set Up Prepared Reports

1. Go to [Role Permission for Page and Report](/erpnext/role-permission-for-page-and-report).
1. In the field 'Set Role For' select **Report**.
1. In the 'Report' field select the report for which you want to enable/disable prepared report.
1. Use the **Disable Prepared Report** checkbox to enable/disable the prepared report. If the option is checked, the prepared report option will be disabled for the selected report.
1. Click on **Update**.

[Screenshot on the live page: Setup Prepared Report]

## How To Use A Prepared Report

1. Open said report (say General Ledger) and apply all filters needed.
1. If the prepared report option is enabled for that report, you will see a **Generate Report** button. Click on the same.
 [Screenshot on the live page: Generate Prepared Report]
1. You will see a notification on the bottom-right of the screen saying "Report initiated. You can track its status _here_"
 [Screenshot on the live page: Prepared Report Initiated]
1. You can either wait on the said screen or click on _here_ in the above message to open the page for the report. This will open a new page for the report:
 [Screenshot on the live page: Prepared Report Queued]
 As you see, the report page has status as "Queued". Once the report is ready, you will see a **Show Report** button which you can click to view the report:
 [Screenshot on the live page: Prepared Report Initiated]
1. Since Prepared Report is also a doctype, to view the list of Prepared Reports, you can use the [Role Permission Manager](/erpnext/role-based-permissions) to grant access to the same.

<!-- page: erpnext/erpnext__price-lists.md -->
---
title: "Price Lists"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/price-lists"
updated: "2026-03-06"
---

**A Price List is a collection of Item Prices either Selling, Buying, or both.**

ERPNext lets you maintain multiple Selling and Buying [Item Prices](/erpnext/item-price) using Price Lists.

Price Lists can be used in scenarios where you have different prices for different zones (based on the shipping costs), for different currencies, etc. An Item can have multiple prices based on customer, currency, region, shipping cost, etc, which can be stored as different rate plans.

In ERPNext, all the Item Prices are stored separately. Buying Price for an item is different from Selling Price and thus they're stored separately.

To access a Price List go to:

> Home > Selling/Buying/Stock > Items and Pricing > Price List

[Screenshot on the live page]

1. How to use a Price List

---

- Price Lists will be used when creating item prices to track the selling or buying price of an item.
- Specific countries can be assigned in the Price List.
- To disable a specific Price List, untick the 'Enabled' checkbox. The Disabled Price List will not be available for selection in the Sales and Purchase transactions.
- **Price Not UOM Dependent**: Consider an item, Tomatoes, which you buy in Boxes and sell in Kilos. 1 Box = 10 Kilos, and 1 Kilo buying price is 10rs. If this Box is unchecked and you select 1 Box in your transaction, the price will show up only for a Kilo since that's the only Item Price saved.

Now, if you tick this checkbox and make a transaction with a Box of Tomatoes, then the price will be automatically set as 100 since the price of 1 Box (10 Kilos) is 100.

- Standard Buying and Selling Price Lists are created by default.

**Note**: If you have multiple Price Lists, you can select a Price List or tag it to a Customer (so that it is auto-selected). Your Item Prices will automatically be updated from the Price List.

### Related Topics

1. [Item Price](/erpnext/item-price)

<!-- page: erpnext/erpnext__pricing-rule.md -->
---
title: "Pricing Rule | ERPNext Documentation"
description: "Create ERPNext Pricing Rules for rates, discounts, margins, free products, parties, quantities, dates, priorities, and cumulative conditions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/pricing-rule"
updated: "2026-07-24"
---

A Pricing Rule tells ERPNext when to replace a standard rate, apply a discount or margin, or add a free product. The rule can be limited by item, party, quantity, value, date, warehouse, company, currency, or another condition. ERPNext evaluates eligible rules when an item is added or the transaction is recalculated.

Use Pricing Rules for repeatable exceptions. For a one-time adjustment, enter a discount directly on the transaction. For tiered campaigns with several slabs, consider a [Promotional Scheme](/erpnext/promotional-scheme).

## Before you begin

- Create the relevant [Items](/erpnext/item), Item Groups, Brands, Customers, Suppliers, and [Price Lists](/erpnext/price-lists).
- Confirm whether the rule is for selling, buying, or both.
- Decide whether the outcome should be a new rate, a percentage or fixed discount, a margin, or a free product.
- Check for overlapping Pricing Rules. If more than one rule can match, define the intended priority and stacking behavior before using the rule in live transactions.

To open Pricing Rule, use the search bar or go to **Selling > Items and Pricing > Pricing Rule**.

## Create a Pricing Rule

1. Click **Add Pricing Rule**.
2. Enter a clear **Title** that identifies the audience and offer.
3. In **Apply On**, select Item Code, Item Group, Brand, or Transaction.
4. Select **Price** for a rate, discount, or margin. Select **Product** for a free-item offer.
5. Add the Item Codes, Item Groups, or Brands covered by the rule. Select the highlighted pencil icon to edit all fields in a child-table row.
6. Under **Party Information**, enable Selling or Buying and, if required, limit the rule to a Customer, Customer Group, Territory, Sales Partner, Campaign, Supplier, or Supplier Group.
7. Set quantity, amount, validity, company, and currency conditions.
8. Enter the rate, discount, margin, or free-product result.
9. Save the Pricing Rule.

[Screenshot on the live page: Pricing Rule for an item and customer in ERPNext]

## Important fields and what they mean


| Field                      | What it controls                                                                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disable                    | Stops ERPNext from applying the rule without deleting its configuration or history.                                                                       |
| Apply On                   | Chooses whether eligibility is evaluated by Item Code, Item Group, Brand, or the complete transaction.                                                    |
| Price or Product Discount  | **Price** changes the commercial value. **Product** adds a free item according to the configured quantity.                                                |
| Warehouse                  | Restricts the rule to items supplied from a specific Warehouse.                                                                                           |
| Mixed Conditions           | Combines quantities or values across the selected items before checking the threshold.                                                                    |
| Is Cumulative              | Checks eligible transactions cumulatively across the defined period. The rule is applied to the transaction that crosses the threshold.                   |
| Coupon Code Based          | Requires a matching [Coupon Code](/erpnext/coupon-code) before the rule is applied.                                                                       |
| Applicable For             | Limits the rule to a selected sales or purchase party dimension, such as Customer, Customer Group, Territory, Sales Partner, Supplier, or Supplier Group. |
| Min and Max Qty            | Sets the eligible quantity range in the Item's Stock UOM. Leave Max Qty at zero when no upper limit is required.                                          |
| Min and Max Amt            | Sets the eligible value range. Transaction-level rules can apply the discount to Grand Total or Net Total.                                                |
| Valid From and Valid Up To | Defines the active date range. Blank dates leave that side of the range open.                                                                             |
| Company and Currency       | Restricts the rule to the selected Company and currency.                                                                                                  |
| For Price List             | Limits the result to transactions using a specific Price List. Leave it blank only when the rule should work with every eligible Price List.              |
| Priority                   | Resolves overlapping rules when ERPNext needs one rule to take precedence.                                                                                |


## Set quantity, value, and validity conditions

Quantity and amount fields define the threshold for the rule. In this example, Northstar Retail must order at least two AeroBook 14 laptops. The rule is restricted to Nova Electronics Trading, USD, and the 2026 validity period.

[Screenshot on the live page: Pricing Rule quantity and period settings in ERPNext]

If the order falls below Min Qty or Min Amt, or exceeds a non-zero maximum, ERPNext does not apply the rule. When **Mixed Conditions** is enabled, ERPNext checks the combined quantity or amount of the selected items. When **Is Cumulative** is enabled, it checks qualifying transactions across the configured period.

## Choose the pricing result

For a price-based rule, select one of these outcomes:

- **Rate:** replaces the normal Item Price with the rate entered in the rule.
- **Discount Percentage:** reduces the eligible price by a percentage.
- **Discount Amount:** subtracts a fixed amount in the rule currency.
- **Margin:** adds a percentage or amount over the fetched rate. See [Adding Margin](/erpnext/adding-margin).

[Screenshot on the live page: Pricing Rule discount percentage in ERPNext]

A Rate defined in a Pricing Rule takes precedence over the normal Item Price rate when the rule is eligible. Restrict the rule with **For Price List** when the result should not apply to every sales or purchase price list.

## Create a product discount

Select **Product** when the promotion adds a free item.

- Enable **Same Item** for an offer such as buy two of an item and receive one more of the same item.
- Leave Same Item cleared and select **Free Item** when the free product is different.
- Enter the free quantity, UOM, and rate. Use **Round Free Qty** when a fractional calculated quantity is not appropriate.
- Enable **Don't Enforce Free Item Qty** when users may reduce or remove the initially fetched free quantity. This is useful when stock is limited or the seller can vary the giveaway.

For a focused example, see [Setting up a Buy 1 Get 1 Free Pricing Rule](/erpnext/setting-up-buy-1-get-1-free-pricing-rule).

## Apply and verify the Pricing Rule

1. Create or open a supported sales or purchase transaction, such as a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), Purchase Order, or [Sales Invoice](/erpnext/sales-invoice).
2. Select the party, company, currency, price list, and transaction date required by the rule.
3. Add an eligible item and meet the configured quantity or amount threshold.
4. Check the item's rate, discount, or free-product row. Recalculate the transaction after changing a condition.

If the transaction must deliberately bypass all matching rules, use **Ignore Pricing Rule** where that option is available. Use it only for an approved exception.

## Overlapping and advanced rules

Test overlapping rules before activating them. Use **Has Priority** and **Priority** when a more specific rule must win. Enable **Apply Multiple Pricing Rules** only when eligible discounts are intended to stack. With **Apply Discount on Discounted Rate**, ERPNext compounds successive discounts instead of adding their percentages.

**Threshold for Suggestion** can prompt users when the entered quantity or amount is close to the minimum. **Validate Applied Rule** can show the configured Rule Description when a manually entered value does not match the expected rule.

The **Dynamic Condition** tab accepts a single-line Python expression based on fields in the target transaction. Use it only when standard fields cannot express the requirement. Keep the condition simple, test it in a non-production company, and document who maintains it.

## Troubleshooting


| Issue                                            | What to check                                                                                                                                                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The rule is not applied                          | Check Disable, Selling or Buying, item scope, party scope, quantity, amount, validity dates, company, currency, warehouse, and price list. Then remove and re-add the item or recalculate the transaction.   |
| An unexpected rule is applied                    | Search for other active rules matching the same item and party. Review priority and multiple-rule settings.                                                                                                  |
| The discount disappears after changing the order | The updated quantity, value, party, date, or price list may no longer meet the rule. Recheck the eligibility fields.                                                                                         |
| A free item returns after removal                | Enable Don't Enforce Free Item Qty if users are allowed to change or remove the fetched giveaway.                                                                                                            |
| A cumulative rule does not trigger               | Confirm Min Amt, Max Amt, validity period, party, item, and transaction status. The discount is applied to the qualifying transaction that crosses the threshold, not retroactively to earlier transactions. |


## FAQs

### Can one Pricing Rule cover every item?

Yes. Apply the rule to an appropriate parent Item Group, such as All Item Groups, or use a transaction-level rule. Broad rules should have clear party, period, or value limits to avoid unintended discounts.

### Can a rule be limited to one Customer?

Yes. Select Selling, set Applicable For to Customer, and choose the Customer.

### Does a Pricing Rule change the Item Price record?

No. It changes the result on eligible transactions. The underlying Item Price remains available for transactions that do not meet the rule.

### Can I pause a rule and reuse it later?

Yes. Enable Disable. Update its validity dates and review its conditions before reactivating it.

### Should I use a Pricing Rule or a Promotional Scheme?

Use a Pricing Rule for a direct conditional result. Use a Promotional Scheme when a campaign needs several quantity or amount slabs that generate multiple Pricing Rules.

## Related topics

- [Price List](/erpnext/price-lists)
- [Applying a Discount](/erpnext/applying-discount)
- [Adding Margin](/erpnext/adding-margin)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Coupon Code](/erpnext/coupon-code)
- [Loyalty Program](/erpnext/loyalty-program)

<!-- page: erpnext/erpnext__print-format-builder.md -->
---
title: "Print Format Builder\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print-format-builder"
updated: "2026-03-02"
---


**The Print Format builder helps you quickly make a simple customized Print Format by dragging and dropping data fields and adding custom text or HTML.**

The 'Standard' Print Format is created by default, it cannot be edited.

To access the Print Format Builder, go to:

> Home > Settings > Print Format Builder

Or via a document.

## 1. Using the Print Format Builder

###1.1 Via the menu navigation
1. Go to the Print Format Builder.
1. Here you can edit an existing print format or create a new Print Format for a document type like Item, Quotation, etc.
1. Let's see how to edit an existing Print Format in this section. To know about creating a new Print Format, see the next section.
1. Select the Print Format to edit.
 [Screenshot on the live page: Select doctype for editing Print Format]

1. Click on the Edit button, you will be taken to the Print Format Builder UI.
 [Screenshot on the live page: Print Format builder screen]

1. Here you can drag and drop fields from the sidebar to the page and vice versa.
1. After making the changes, click on Save.

### 1.2 Via a document
1. Open the document for which you want to make a Print Format. Click the Printer icon, or go to Menu > Print and click on the Customize... button. Note: You must have System Manager permission to do this.

 [Screenshot on the live page: Send Email]

1. To add a field, just drag it from the left sidebar and add it in your layout. You can edit the layouts in sections or individual fields by clicking on the settings  icon.

1. To remove a field, just drag it back into the fields sidebar.

1. Save.

You can add customized text, HTML in your print format, just drag and drop the **Custom HTML** field (in dark color) and add it to the place where you want to add the Custom HTML content.

Then click on **Edit HTML** to edit your content.

## 2. Video

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/cKZHcx1znMc?start=82&amp;rel=0">
</iframe>



### 3. Related Topics
1. [Print Style](/erpnext/print-style)
1. [Print Headings](/erpnext/print-headings)
1. [Letter Head](/erpnext/letter-head)
1. [Cheque Print Template](/erpnext/cheque-print-template)

<!-- page: erpnext/erpnext__print-format.md -->
---
title: "Print Format\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print-format"
updated: "2026-03-02"
---


**With Print Format, you can set how document types look when printing.**

Every transaction has a default Print Format called 'Standard'. You can change Print Formats by:

* Using the Print Format form
* Using Jinja/JS scripting under Print Format
* Using the [Print Format Builder](/erpnext/print-format-builder) to create print formats with UI
* Using Customize Form to hide/unhide fields

To access Print Format, go to:

> Home > Settings > Print Format

## 1. How to create a Print Format
1. Go to the Print Format List, click on New.
1. Enter a name and select a DocType for which the Print Format is to be used.
1. The module for which it should apply will be selected automatically.

 [Screenshot on the live page: Print Format menu]

1. Save.

Under Style Settings, there are options to change the styling options. With those options, you can change the font, align the labels together on the left or right, add headings for sections, etc.

To style the Print Format using custom Jinja/JS, click on Custom Format. If you select this option, there'll be a checkbox for raw printing. To know more about raw printing, [click here](/erpnext/raw-printing).

If developer mode is enabled, you can select Standard as yes to contribute a print format as a standard (preset) print format in the system.

## 1.1 Using Customize form to change the Print Format items
Fields in the transactions and their child tables can be hidden/shown using Customize Form.
For example, if you want to hide the 'Item Code' when printing a Quotation, click on the print icon to enter the print screen.

Go to Menu > Customize, select Quotation Item in the 'Enter Form Type' field.
[Screenshot on the live page: Print Format Customize]

To know more, visit the [Customize Print Format](/erpnext/print-format) page.

In the fields table, expand the 'Item Code' row, scroll down and tick the 'Print Hide' checkbox.
[Screenshot on the live page: Print Format Print Hide]


A newly created Print Format can be selected on the print screen of a transaction. From there you can see how it looks and proceed to print.
[Screenshot on the live page: Selecting a Print Format]

## 2. Video

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/cKZHcx1znMc?start=82&amp;rel=0">
</iframe>



### 3. Related Topics
1. [Print Style](/erpnext/print-style)
1. [Print Headings](/erpnext/print-headings)
1. [Letter Head](/erpnext/letter-head)
1. [Cheque Print Template](/erpnext/cheque-print-template)
1. [Disabling Line Breaks in Print Format Sections](/erpnext/print-format-sections)

<!-- page: erpnext/erpnext__print-headings.md -->
---
title: "Print Headings\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/print-headings"
updated: "2026-03-02"
---


**Print Headings are the names/titles you can give your transactions.**

These transactions include Sales Invoices, Supplier Quotations, etc. You can create a list of names for different business communications.

If you want to rename a transaction on how it appears when printing, you can do so via Print Headings. For example, a Quotation is also called a "Proposal", Estimate", or "Pro Forma Invoice".

To access Print Headings go to:

> Home > Settings > Print Heading

## 1. How to create a Print Heading
1. Go to the Print Heading list, click on New.
1. Enter the heading that will appear on the document.
1. Save.

 [Screenshot on the live page: Print Heading]

To use the print heading, select the created print heading in the 'Print Heading' field transaction, shown as follows:

[Screenshot on the live page: Using a Print Heading]

Example of a change in print heading is shown as follows:

[Screenshot on the live page: Print Heading]

## 2. Video

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/cKZHcx1znMc?start=58&amp;end=82&amp;rel=0">
</iframe>



### 3. Related Topics
1. [Print Format](/erpnext/print-format)
1. [Print Style](/erpnext/print-style)
1. [Letter Head](/erpnext/letter-head)
1. [Cheque Print Template](/erpnext/cheque-print-template)
1. [Quotation](/erpnext/quotation)
