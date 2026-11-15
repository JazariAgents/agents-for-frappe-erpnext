<!-- Frappe documentation: erpnext, part 67 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__use-inline-serial-batch-editor.md -->
---
title: "Use Inline Serial / Batch Editor"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/use-inline-serial-batch-editor"
updated: "2026-07-19"
---

The Inline Serial / Batch Editor lets you add and manage Serial Numbers and Batches directly on the item row of your stock documents — no separate pop-up dialog needed. You see your entries in a simple table right where you are working, and everything is saved together when you save the document.

---

## How to Enable It

1. Open **Stock Settings** (search for "Stock Settings" in the search bar).
2. Go to the **Serial & Batch Item** section.
3. Make sure **"Use Serial No / Batch Fields"** is unchecked.
4. Tick the checkbox **"Use Inline Serial / Batch Editor"**.
5. Click **Save**.

That's it — the feature is now on for everyone on your site. (It is enabled by default on new installations.)

> Tip: If you don't see the editor after enabling it, refresh your browser page once.

---

## Where You Will See It

Open any of these documents, then click on an item row to expand it. You will find a **Serial / Batch Entries** table inside the row (for items that have Serial Numbers or Batches):

- Purchase Receipt and Purchase Invoice (including the Rejected quantity section)
- Sales Invoice, POS Invoice and Delivery Note (including bundled / packed items)
- Stock Entry
- Stock Reconciliation
- Subcontracting Receipt (items and supplied items)
- Pick List
- Asset Capitalization and Asset Repair

---

## Why Use It? (Benefits)

- **Everything in one place** — add, edit and remove serial numbers or batches right on the item row. No switching to a pop-up and back.
- **Faster** — your changes are collected as you type and saved to the system in one go when you save the document, instead of one server call per change. Adding 20 batches is one save, not 40 separate updates.
- **Nothing saved by accident** — until you click Save on the document, your serial/batch changes are only on your screen. The Save button appears as soon as you change anything, so you always know there is unsaved work.
- **Handles large lists easily** — entries are shown in pages of 10 with simple navigation buttons, so even hundreds of serial numbers stay easy to browse.
- **Missing serials and batches are created for you** — on incoming documents (like Purchase Receipt), if you enter a serial number or batch that doesn't exist yet, the system creates it automatically when you save.

---

## How to Use It

### Adding entries

1. Click on the item row to expand it and find the **Serial / Batch Entries** table.
2. Click **Add row**.
3. Pick the Serial Number / Batch from the dropdown (or type a new one) and enter the quantity.
4. Repeat for as many entries as you need, then **Save** the document.

The item's quantity and the Total Qty shown under the table update automatically as you add entries.

### Editing entries

- Click directly on a Serial No, Batch No or Qty cell in the table and type the new value — it works just like editing a spreadsheet cell.

### Deleting entries

- Tick the checkbox at the start of one or more rows, then click **Delete row**.
- To clear everything, tick the checkbox in the table header (select all) and click **Delete All**. If you remove all entries and save, the linked Serial and Batch Bundle is removed as well.

### The ⋯ (three dots) menu

At the bottom right of the table you will find a menu with extra tools:

- **Auto Fetch Serial Nos / Batch Nos** *(outgoing documents like Delivery Note)* — enter the quantity you want and the system picks the serial numbers / batches for you, based on the **Pick Serial / Batch Based On** rule in Stock Settings (FIFO, LIFO or Expiry). It replaces whatever is currently in the table, skips reserved stock, and saves the document for you.
- **Scan Serial Nos / Scan Batch Nos** — use a barcode scanner (or type and press Enter) to add entries one by one. Scanning the same batch again simply increases its quantity.
- **Create Serial Nos from Range** *(serial items)* — type a range like `SN-01::10` to add SN-01 through SN-10 in one step.
- **Download** — download the current entries (or a blank template) as a CSV file.
- **Upload** — fill the CSV template and upload it to load many entries at once. Missing serial numbers and batches are created automatically on incoming documents.

### Moving between pages

When there are more than 10 entries, use the arrows at the bottom of the table to move between pages, or type a page number directly. You can jump straight to the first or last page with the outer arrow buttons.

---

## Good to Know

- The editor appears only while the document is in **Draft**. After submission the entries are locked, as usual.
- If an item row has **"Use Serial No / Batch Fields"** ticked, that row keeps the simple text fields and the inline table is hidden for it.
- Prefer the old pop-up dialog? Untick **"Use Inline Serial / Batch Editor"** in Stock Settings and the previous behaviour returns.





![](/files/Screen Recording 2026-07-18 at 1.11.21 PM.mov)

<!-- page: erpnext/erpnext__user-permission-based-on-hierarchy.md -->
---
title: "User Permission based on Hierarchy "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/user-permission-based-on-hierarchy"
updated: "2026-03-04"
---

**Question:**

How to configure User Permissions, so that an Employee can view his Expense Claims, and also of ones who report to him/her?

 

**Answer:**

In the Employee master, for each Employee, you can define who does he/she reports to. Based on the Reports To defined, the Employee hierarchy is built as well.

![](/files/14Khhti.png)

 

 

**Employee Hierarchy**

Also, one a User is linked with the Employee, it creates a User Permission as follows. As per this User Permission, Employee will be allowed to review his/her own document created in the HR module + the document which are created for Employees reporting to hm/her.

 

![](/files/wRl6sKW.png)

As per this configuration, when an Expense Claim is being created by the User reporting to Kenneth, it will also be accessible to Kenneth as well.

![](/files/4L4Co0O.png)

 

Can you please ensure that seniors Employee ID is updated as Reports To in the Employee's who report to him/er? After that, manager should be able to view the Expense Claims and other documents (like Leave Application, Appraisal etc.) made for his/her sub-ordinates.

<!-- page: erpnext/erpnext__user-permissions.md -->
---
title: "User Permissions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/user-permissions"
updated: "2026-02-27"
---

**User permissions is a way of restricting user access to particular documents.**

Role based permissions allow setting complete (by default) access to a document type (doctype) like Sales Invoice, Orders, Quotation, etc. This means that when you assign a Sales User role to a user, they can access all the Sales Orders and Quotations.

User Permissions can be used to restrict access to select documents based on the link fields in the document. For example, consider that you do business with multiple territories and you want to restrict access of certain Sales Users to Quotations/Sales Order belonging to a particular territory. This can be done via User Permissions. The restrictions can be set on Customer, Supplier, Customer Group, Supplier Group, etc.

Setting User Permissions are particularly useful when you want to restrict based on:

1. Allowing user to access data belonging to one Company
2. Allowing user to access data related to a specific Customer or Territory

To access User Permissions, go to: > Home > User and Permissions > User Permissions

1. How to create User Permissions
---------------------------------

1. Go to the User Permissions list, click on New.
2. Select the user for which the rule has to be applied.
3. Select the type of document to be allowed (for example "Company").
4. Under For Value, select the specific item that you want to allow (the name of the "Company).
5. If you check 'Is Default', the value selected in 'For Value' will be used by default for any future transactions by this user. That is if company 'Unico Plastics Inc.' is selected as 'For Value', this Company will be set as default for all future transactions by this user.

![Creating a new user permission](/files/new-user-permission.png)  


> Note: Only a single user permission can be set as default for a particular document type for a specific user.

2. More User Permission actions
-------------------------------

### 2.1 Advanced Control

In Advanced Control, you can have better command over where the User Permission is applied.

### 2.1.1. Applicable For

You can optionally apply user permissions only for specific document type by setting the Document Type after unchecking the Apply To All Document Types checkbox. Setting **Applicable For** option will make the current user permission applicable only under the selected Document Type master.

![Applicable For](/files/advanced-control.png)  


In the above User Permission, the user will be able to access only Sales Orders of the selected company.

**Note:** If **Applicable For** is not set, User Permission will apply across all related Document Types.

### 2.1.2. Hide Descendants

The value of **Allow** could be a DocType with a Tree View, which will have records with a parent-child or ancestor-descendant relationship.

Let's assume **For Value**, 'Unico Plastics Inc.', has a child company 'Unico Toys'. When a User Permission is created for 'Unico Plastics Inc.', permissions for its descendants are granted as well.

**Hide Descendants** is visible only on selecting a Tree View DocType. By enabling this checkbox, permissions for descendants of **For Value** will not be granted.

![Hide Descendant Permissions](/files/hide-descendant-permissions.png)  


A user that can view records of 'Unico Plastics Inc.' will not be able to view those of 'Unico Toys'.

### 2.2 Ignoring User Permissions on Certain Fields

Another way of allowing documents to be seen by everyone that have been restricted by User Permissions is to tick "Ignore User Permissions" on a particular field by going to **Customize Form**.

For example, you don't want Assets to be restricted for any user, then select **Asset** in form type. Under the fields table, expand the Company field and tick on "Ignore User Permissions".

![Ignore User Permissions on specific properties](/files/ignore-user-permissions.png)  


### 2.3 Strict Permissions

When user permissions are defined, for a particular role - the role permissions are only applied when the user permission are defined. When there are no user permissions for a particular user, there could be two interpretations:

1. Show everything (nothing is restricted)
2. Show nothing (nothing is permitted)

You can choose how to interpret this the way you want by checking "Apply strict permissions" on the System Settings page.

To know more, go to the [System Settings page](/erpnext/system-settings#14-permissions).

### 2.4 Checking How User Permissions are Applied

Finally, once you have created your air-tight permission model, and you want to check how it applies to various users. You can see it via the **Permitted Documents for User** report. Using this report, you can select the **User** and document type and view which documents a particular user can access.

Ticking on the Show Permissions checkbox will show the read/write/submit and other access levels.

![Permitted Documents for User report](/files/permitted-documents.png)  


Note: If you cannot access Sales Order or any other document type in this list, make sure you've set the [roles](/erpnext/role-based-permissions) correctly.

For example, the user, Bruce is restricted to Company 'Unico Plastics Inc.' ![User restricted to Company](/files/user-restricted-to-company.png)  


### 3. Related Topics

1. [Adding Users](/erpnext/adding-users)
2. [Role and Role Profile](/erpnext/role-and-role-profile)
3. [Role Based Permissions](/erpnext/role-based-permissions)
4. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__using-custom-api-rows-in-financial-report-template.md -->
---
title: "Using Custom API Rows in Financial Report Template"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/using-custom-api-rows-in-financial-report-template"
updated: "2026-08-14"
---

Nova Industries wants one management-report line that cannot be produced from account categories alone: a specialised budget-adjusted operating metric calculated by its installed custom app. The value must appear beside standard account lines and remain available to later formulas.





A Financial Report Template row with Data Source set to **Custom API** calls an approved server-side Python function. Use it only when Account Data and Calculated Amount rows cannot express the requirement. This is an advanced developer feature, not a way to call an external HTTP endpoint from the report.

## Before you begin

- Use a site where the custom Frappe app can be installed and deployed.
- Implement and test a module-level Python function in that app.
- Confirm the function's performance, permissions, data access, and error handling.
- Create or identify the [Financial Report Template](/erpnext/financial-report-template) that needs the row.

![Financial Report Template list used before adding an advanced Custom API row](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)

## Add the Custom API row

![Financial Report Template form where a Custom API report row is configured](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)



1. Open the Financial Report Template.
2. Add a row in Report Line Items and open its row editor.
3. Set Data Source to **Custom API**.
4. Enter a dotted Python path such as `my_app.financial_report_api.get_budget_variance`.
5. Set a Line Reference when later formula rows need the returned value.
6. Configure Reverse Sign, Hide If Zero, Hidden Line, Include in Charts, and Value Type as required.
7. Save the template and run its financial report.

## Function contract

ERPNext can pass the report `filters`, generated `periods`, and current `row`. Return one numeric value for each period, in the same order.



```
from frappe.utils import flt

def get_budget_variance(filters=None, periods=None, row=None):
    filters = filters or {}
    periods = periods or []
    values = []

    for period in periods:
        variance = calculate_variance(
            company=filters.get("company"),
            from_date=period.from_date,
            to_date=period.to_date,
        )
        values.append(flt(variance))

    return values
```

## Return requirements


| Requirement            | Reason                                                 |
| ---------------------- | ------------------------------------------------------ |
| List of numeric values | The report needs one renderable amount per period.     |
| Same length as periods | Each displayed period must receive exactly one result. |
| Same order as periods  | Values must align with their headings.                 |
| Stable Line Reference  | Later calculated rows use the API result safely.       |


## Important behavior

The path must use the form `app.module.method`. The function must exist in an installed app. `@frappe.whitelist()` is not required solely for the report call. Server Scripts are not supported for Custom API rows. ERPNext processes Custom API rows before account and formula results, so they should not depend on later template lines.

## Secure and test the function

Validate filter values, use permission-aware queries where required, avoid returning sensitive detail, and keep queries bounded. Test no-data periods, multiple periodicities, company separation, foreign currencies, large date ranges, and error conditions. Reconcile the result with an independent calculation before publishing the template.

## Troubleshooting

### The API path is rejected

Use a complete dotted module path and confirm that the function is defined at module level inside an installed app.

### The row shows zeros

Review Error Log for a Custom API error, confirm the function returned one numeric value per period, and test the function with the same report filters.

### A calculated row cannot use the result

Give the Custom API row a unique Line Reference and use that exact reference in the later formula.

## Frequently asked questions

### Can the row call a public REST API directly?

The template calls a Python function on the ERPNext server. That controlled function may integrate with another system according to your app's security and reliability design.

### Can the function change accounting data?

A reporting function should be read-only. Creating or changing transactions during report execution would make results unsafe and unpredictable.

### What happens when the function raises an error?

ERPNext records an error and can fill the row with zeros. Treat that state as a failed report calculation and investigate before sharing the output.

## Related topics

- [Financial Report Template](/erpnext/financial-report-template)
- [Accounting Reports](/erpnext/accounting-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Frappe Framework](/erpnext/frappe-framework)

<!-- page: erpnext/erpnext__using-finance-book-for-asset-depreciation.md -->
---
title: "Using Finance Book for Asset Depreciation | ERPNext Documentation"
description: "Maintain separate statutory and management depreciation schedules for one ERPNext Asset using Finance Books."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/using-finance-book-for-asset-depreciation"
updated: "2026-08-15"
---

Imagine Nova Industries must report a machine one way in its statutory accounts, but management wants a second view for internal planning. The law may allow a ten-year useful life, while managers may prefer five years because they expect to replace the machine sooner.



Finance Books allow both views to exist without changing the original asset cost. ERPNext can keep a separate depreciation schedule for each book, so the finance team can compare statutory reporting with its internal view.

## Configure Finance Books

Create each [Finance Book](https://docs.frappe.io/erpnext/finance-book) and add its depreciation policy to the Asset Category.

![Statutory and management Finance Books on an Asset Category](https://novacompanies.m.frappe.cloud/files/03-asset-category-finance-books.png)

## Apply them to an Asset

Review the rows copied to the Asset. Each row can use its own method, frequency, useful life, residual value, and start date.

![Parallel Finance Book rows on an ERPNext Asset](https://novacompanies.m.frappe.cloud/files/08-asset-finance-books.png)

## Report by Finance Book

Select the intended Finance Book in asset and accounting reports. Leaving the filter blank can include default-book behavior and may not answer a policy-specific question.

![Asset balances report used with Finance Book filters](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### A report shows the wrong depreciation values

Check the report's Finance Book filter and whether **Include Default Finance Book Assets** is enabled.

### Only one schedule exists

Confirm the Asset contains a complete row for every required Finance Book before submission.

## Frequently asked questions

### Does a Finance Book create a separate asset?

In ERPNext, no. It creates a separate accounting schedule for the same Asset.

### Can Finance Books use different methods?

In ERPNext, yes. That is one of their main purposes.

### Which Finance Book posts by default?

The company or transaction defaults determine the default view. Always set an explicit filter when validating a specific reporting basis.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__validate-the-migration.md -->
---
title: "Validate and Correct an Accounting Migration | ERPNext Documentation"
description: "Reconcile ERPNext migration masters, invoices, payments, bank, stock, assets, Trial Balance, and financial statements, then correct errors safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/validate-the-migration"
updated: "2026-08-14"
---

A successful import only proves that ERPNext accepted the rows. Validation proves that the new books represent the same financial position as the signed-off source system.



Nova Industries compares its Trial Balance, customer and supplier ageing, bank balances, stock value, fixed assets, taxes, and equity at the cut-off date. A difference is traced to the import file or mapping rule, corrected, and tested again before normal posting begins.



This page provides a practical reconciliation order, explains how to isolate differences, and distinguishes corrections to imported data from adjustments that require an approved accounting entry.

## Reconcile in layers

Validate in this order:

1. Master counts and mappings
2. Imported document counts and totals
3. Subledger schedules
4. Control accounts
5. Trial Balance
6. Balance Sheet and Profit and Loss Statement
7. Operational testing

An exact Trial Balance can still hide party, Warehouse, or Cost Center mapping errors, so subledger checks come first.

## Master validation

Compare source and ERPNext counts for Customers, Suppliers, Items, Warehouses, accounts, Cost Centers, banks, and assets.

Review:

- duplicates;
- disabled records;
- missing parents;
- wrong companies;
- wrong currencies;
- missing tax IDs;
- incorrect defaults;
- unmapped legacy identifiers.

## Receivables and payables

Run Accounts Receivable and Accounts Payable at cutover. Compare:

- party total;
- invoice count;
- invoice outstanding amount;
- due date;
- ageing bucket;
- currency;
- credit notes;
- unallocated payments and advances.

The receivable and payable control accounts in the Trial Balance must equal their subledger totals.

## Bank and cash

Compare each General Ledger account with the reconciled legacy book balance. Recreate or document outstanding bank items. Confirm the statement balance plus reconciling items equals the ERPNext book balance.

## Stock

Run Stock Balance by Item and Warehouse. Compare quantity and value separately. Investigate zero or negative valuation, wrong Warehouse, serial or batch differences, and rounding.

The stock ledger value must agree with the relevant General Ledger control accounts when perpetual inventory is used.

## Fixed assets

Compare gross cost, accumulated depreciation, net book value, category, location, and next depreciation date with the source asset register.

## Trial Balance and financial statements

Run Trial Balance at the cutover date and compare every mapped account.

![Trial Balance used to validate the migrated balances](/files/trial-balance-validation.webp)

Classify each difference as:

- source adjustment posted after extraction;
- omitted import row;
- duplicate import;
- incorrect sign;
- wrong account mapping;
- exchange-rate difference;
- rounding;
- balance imported through two methods;
- date or company error.

Then compare Balance Sheet and Profit and Loss Statement. Review retained earnings and current-year result carefully.

## Test real workflows

Create controlled transactions after opening:

- sell and receive payment;
- purchase and pay;
- allocate an imported advance;
- return an imported invoice where supported;
- reconcile a bank statement;
- issue stock from an opening quantity;
- post asset depreciation;
- run tax and financial reports.

## Correcting errors

Correct the source document, not the ledger output.


| Error                        | Correction                                                            |
| ---------------------------- | --------------------------------------------------------------------- |
| Wrong master name or default | Rename, merge, or update the master using a supported method          |
| Failed import row            | Correct the approved file and import only the failed row              |
| Wrong opening invoice        | Cancel and recreate or amend before go-live                           |
| Wrong opening journal row    | Cancel and amend the Journal Entry or post an approved correction     |
| Duplicate balance            | Cancel the duplicate opening document                                 |
| Wrong stock opening          | Correct through Stock Reconciliation                                  |
| Wrong asset opening          | Correct the Asset and depreciation opening data before later postings |


After every correction, rerun the affected subledger and the Trial Balance.

## Sign-off

Record:

- report name and filters;
- source total;
- ERPNext total;
- difference;
- explanation;
- preparer;
- reviewer;
- approval date.

Freeze the cutover period only after all unexplained differences are zero and finance has signed off.

## Related topics

- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Trial Balance](https://docs.frappe.io/erpnext/trial-balance)
- [Accounts Receivable](https://docs.frappe.io/erpnext/accounts-receivable)
- [Stock Balance](https://docs.frappe.io/erpnext/stock-balance)
- [Opening and Closing During Migration](https://docs.frappe.io/erpnext/opening-and-closing)

<!-- page: erpnext/erpnext__valuation-based-on-field-in-bom.md -->
---
title: "Raw material valuation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/valuation-based-on-field-in-bom"
updated: "2026-03-02"
---

**Question:** What are for various options in `Valuation Based On` in the Bill Of Materials (BOM)?

**Answer:** There are 3 available options in the *Valuation Based On* field:

![Nested BOM](/files/valuation-based-on-1.png)  


**Valuation Rate:** Item valuation rate is defined based on it's purchase or manufacture value.

For Purchase Item, it is defined based on charges entered in the Purchase Receipt. If you don't have any Purchase Receipt made for an item or a Stock Reconciliation, then there won't be any Valuation Rate for that item.

**Price List Rate:** This option allows to pull item rates from [Price List.](/erpnext/item-price)

**Last Purchase Rate:** It will be the last Purchase (Order) Rate of an item.

<!-- page: erpnext/erpnext__vat_audit_report.md -->
---
title: "VAT Audit Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/vat_audit_report"
updated: "2026-03-02"
---

>Introduced in version 13

VAT Audit Report shows the amount details of each item from the Purchase and Sales invoices for specified time period.

![South Africa VAT Account Settings](/files/Screenshot-2.png)

You need to add the VAT Accounts in the South Africa VAT Settings for which you want to generate the report.

![South Africa VAT Account Settings](/files/Screenshot-1.png)

#### Note:

 

Check the following to make sure the calculations in the report are correct,

1. Zero Rated items have "Is Zero Rated" checkbox checked in the item master.

2. All VAT accounts are selected in South Africa VAT Settings.



Currently, this report only maps invoice data.

<!-- page: erpnext/erpnext__warehouse-ledger-link.md -->
---
title: "Linking stock warehouse and accounts"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warehouse-ledger-link"
updated: "2026-03-02"
---


The value of stock stored in the warehouses needs to be tracked.

Each warehouse is linked to a ledger in chart of accounts through the 'Account' field in the warehouse.

![Stock Asset Ledger in Warehouse](/files/stock-asset-ledger-in-warehouse.png)

If the Account field is empty in a warehouse, then the Account mentioned in the parent of that warehouse is considered. If an Account could not be determined by tracing the hierarchy, then the Default Inventory Account mentioned in the Company record is considered.

![Default Inventory Account in Company](/files/default-inventory-account-in-company.png)

When a company is created, a ledger named 'Stock In Hand' is created by default in Chart of Accounts.

**Chart of Accounts > Assets > Current Assets > Stock Assets > Stock In Hand.**

If required, you can create additional ledgers under 'Stock Assets' group.

![Stock Asset Ledger in Chart of Accounts](/files/stock-asset-ledger-in-coa.png)

<!-- page: erpnext/erpnext__warehouse.md -->
---
title: "Warehouse\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warehouse"
updated: "2026-04-27"
---

**A warehouse is a commercial building for storage of goods. Warehouses are used
by manufacturers, importers, exporters, wholesalers, transport businesses,
customs, etc.**

They are usually large plain buildings in industrial areas of
cities, towns, and villages. They mostly have loading docks to load and unload
goods from trucks.

The terminology of 'Warehouse' in ERPNext is a bit broader though and maybe can be regarded as "storage locations". You can create a sub-Warehouse which could be a shelf inside your actual location.

This can become quite a detailed Tree like the following:

*Warehouse > Room > Row > Shelf > Bin*

To access the Warehouse list, go to:

> Home > Stock > Settings > Warehouse

## 1. How to create a Warehouse

1. Go to the Warehouse list, click on New.
2. Enter a name for the Warehouse.
3. Set/check the Parent Warehouse. If you tick on 'Is Group', you can create sub-Warehouses under this group Warehouse.
4. Save.

Warehouses are saved with their respective Company’s abbreviations. This facilitates
identifying which Warehouse belongs to which company at a glance.

### 1.1 Additional options when creating a Warehouse

**Account**: Set a default account here for all transactions with this Warehouse. Setting this account will show transactions from this Warehouse in the Accounting Ledger.
**Warehouse Type**: You can create a Warehouse Type to classify Warehouses. For example, Supplier Warehouses, Stock Warehouses, WIP Warehouses, Rooms, etc. can be tagged. This classification is useful when generating reports or in certain stock transactions.

#### Address and contact

You can add Billing, Shipping, and other types of addresses for the Warehouse. You can also add a contact, this could be the Warehouse Manager for example.

![Warehouse](/files/warehouse.png)

### 1.2 After Saving

After saving a Warehouse, you'll see the following options:

- **Stock Balance**: This will open the Stock Balance report to display the quantity, valuation, balance, etc.
- **General Ledger**: This will open the General Ledger to display the accounting transactions.
- **Non-Group to Group**: If the Warehouse is a Non-Group Warehouse, i.e. cannot contain other Warehouses under it, this button will make this a Group Warehouse.

## 2. Features

### 2.1 Tree View

You can also switch to 'Tree' View which will show all the group and child Warehouses.

![Warehouse](/files/warehouse-tree.png)

### 2.2 Warehouse Account

In ERPNext, if you enable [Perpetual Inventory](/erpnext/v13/user/manual/en/stock/perpetual-inventory), every Warehouse must belong to a specific company to maintain
company-wise stock balance. To do so, each Warehouse should be linked with an
Account in the Chart of Accounts (the same name as the Warehouse itself). This account captures the monetary equivalent of the goods or materials stored in that specific warehouse.

If you have a more detailed Warehouse Tree, most likely it's a good idea to link the sub-locations (room, row, shelf, etc.) to the account of the actual Warehouse (the root Warehouse of that Tree) as most
scenarios do not require to account for value of stock items per Shelf or Bin. For example, if you have Warehouse A, and the room, rows are B, C, etc., then link B and C to the account of A.

> Tip: ERPNext maintains stock balance for every distinct combination
> of Item and Warehouse. Thus you can get the stock balance for any specific Item in a particular Warehouse on any particular date.

### 3. Related Topics

1. [Stock Entry Purpose](/erpnext/v13/user/manual/en/stock/articles/stock-entry-purpose)
2. [Stock Level Report](/erpnext/v13/user/manual/en/stock/stock-level-report)

<!-- page: erpnext/erpnext__warranty-claim.md -->
---
title: "Warranty Claim"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warranty-claim"
updated: "2026-02-28"
---

**A Warranty Claim is when a Customer claims free repairs within the Warranty Period of the item/service you're providing.**

If you are selling Items under warranty or if you have sold and extended service contract like the Annual Maintenance Contract (AMC), your Customer may contact you about an issue or a break-down of the product and provide you the Serial No of this Item.

To access the Warranty Claim list, go to:


> Home > Support > Warranty > Warranty Claim
> 
> 

1. Prerequisites
----------------

Before creating and using Warranty Claim, it is advised that you create the following first:

* [Customer](/erpnext/customer)
* [Serial Number](/erpnext/serial-no)
* [Item](/erpnext/item)

2. How to Create Warranty Claim
-------------------------------

1. Go to the Warranty Claim list, click on New.
2. Select a Customer.
3. Select the Serial Number of the Item on which Warranty Claim is to be recorded. The system will then automatically fetch the Serial No’s details and indicate whether this is under warranty or AMC.
4. Enter a description of the Issue. User can upload and image and create a table.
5. Save. ![Warranty Claim](/files/warranty-claim.png)

### 2.1 Additional Options when Creating a Warranty Claim

* **Status**: While creating a Warranty Claim, the status will be set as "Open". User can change the status to:


	+ Work In Progress: Fix/repairs are being done on the Item.
	+ Closed: The repairs have been done and the Warranty Claim is now closed.
	+ Cancelled: The Warranty Claim was invalid, and the claim was closed.
* **Issue Date**: While creating the Warranty Claim, the current date will be captured. This field is editable.

3 Features
----------

### 3.1 Item and Warranty Details:

Once a Serial Number is selected, the following details about the Item will be fetched:

* Item Code
* Item Name
* Item Description

The details about Warranty/AMC will be fetched according to the Serial Number.

* **Warranty / AMC Status:** The possible options are "Under Warranty", "Out of Warranty", "Under AMC", or "Out of AMC". The status can be changed to Out of Warranty/AMC if the Item has been tampered with or Warranty is void depending on your terms of service.
* Warranty Expiry Date
* AMC Expiry date

![Warranty Serial](/files/warranty-serial.png)

### 3.2 Resolution

* **Resolution Date:** When the warranty or AMC is Closed, current date and time will be fetched in resolution Date field automatically. This field is also editable.
* **Resolved By:** Set the Email ID of the User who has resolved the Warranty Claim. The email ID is linked with [User](/erpnext/adding-users) created in the system.
* **Resolved Details:** This is a text field. User can enter details about the Warranty or AMC claim. A User can also upload the image, enter or create a table.

![Warranty Resolution](/files/warranty-resolution.png)

### 3.3 Customer Details

The following details of the [Customer](/erpnext/customer) will be fetched:

* Customer Name
* Contact Person
* Territory
* Customer Group
* Customer Address

**Service Address:** User can enter the Service Address if it is different from Customer Address.

![Warranty Customer](/files/warranty-customer.png)  


### 3.4 More Information

* **Company:** The Warranty or AMC is created from the company will be selected automatically.
* **Raised By:** User can enter the Name of the person who has raised the Warranty or AMC in case the Customer is an organization.
* **From Company:** User can enter the name of the company from which the warranty or AMC has been created.

If a Customer visit is required to address the issue, you can create a new Maintenance Visit record from this.

4. Related Topics
-----------------

1. [Issue](/erpnext/issue)
2. [Maintenance Visit](/erpnext/maintenance-visit)

<!-- page: erpnext/erpnext__warranty.md -->
---
title: "Warranty"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warranty"
updated: "2026-02-27"
---

By effectively managing warranty claims and serial numbers within ERPNext's Support module, users can streamline customer support processes, ensure accurate tracking of warranty-related information, and enhance overall customer satisfaction by providing timely and effective resolutions to warranty claims.

* [Warranty Claim](/erpnext/user/manual/en/warranty-claim)
* [Serial Number](/erpnext/user/manual/en/serial-no)

  

<!-- page: erpnext/erpnext__web-form.md -->
---
title: "Web Forms"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/web-form"
updated: "2026-02-28"
---

Stakeholders who are not part of your organization may need to interact with your ERPNext instance. You can authorize customers, suppliers, job applicants, students, and guardians to access certain information or even create certain transactions. For example, you can let anyone create an account on your website (created with ERPNext) and apply for a job. You can let your customers see the details of the complaints they have registered. These can be done using Web Forms.

> There are two types of in-built interfaces available in ERPNext. The > *Desk View* and the *Web View*. Desk is for users who regularly interact > with ERPNext instance, like employees of your organization.

> Web View is for users who need to interact with an ERPNext instance occasionally. > Web forms are similar to the forms you generally fill in various websites on the > internet. Webforms are part of the *Web View* interface in ERPNext.

To create a new **Web Form** go to:


> Home > Website > Web Site > Web Form
> 
> 

![New Web Form](/files/new-web-form-1.png) *New Web Form*

Select the **DocType** based on which you want to build your Web Form. The **Route** will be set based on the **Title** of your Web Form. You can also add an Introduction text to show a friendly message above your form.

Add fields to your Web Form. These are the fields from the DocType you have selected. You can change the Label for these fields. Try to keep number of fields to be minimum as long forms are cumbersome to fill.

![Web Form Fields](/files/new-web-form-2.png) *Web Form Fields*

Click on **See on Website** in the sidebar to view your Web form. ![Web Form](/files/web-form.png) *Web Form*

Here is an explanation of each of the checkboxes on the right.

1. **Published**: Web Form will be accessible only if this is enabled.
2. **Login Required**: User can fill the Web Form only if they are logged in. When Login Required is checked,
3. **Route to Success Link**: Go to Success Link after the form is submitted.
4. **Allow Edit**: If this is unchecked the form becomes read-only once it is saved.
5. **Allow Multiple**: Allow user to create more than one record.
6. **Show as Grid**: Show records in a table format.
7. **Allow Delete**: Allow user to delete the records that he/she has created.
8. **Allow Comments**: Allow user to add comments on the created form.
9. **Allow Print**: Allow user to print the document in the selected Print Format.
10. **Allow Incomplete Forms**: Allow user to submit form with partial data.

2. Features
-----------

### 2.1 Sidebar

You can also show contextual links in a sidebar on your Web Form. Set it up in **Sidebar Settings**.

![Web Form Sidebar](/files/web-form-sidebar.png) *Web Form Sidebar*

![Web Form with Sidebar](/files/web-form-with-sidebar.png) *Web Form with Sidebar*

### 2.2 Creating Web Forms with Child Table

You can add child tables to your web forms, just like regular forms.

![Web form Grid](/files/grid-in-webform.png)  


### 2.3 Payment Gateway Integration

You can now add a Payment Gateway to the web form, so that you can ask users to pay against a web form. A good example for this is a conference ticket.

![Web form payment](/files/payment-in-webform.png)  


### 2.4 Portal User

We have also introduced roles for Website users. Before version 11, if you assigned any 'Role' to a user he would get access to 'Desk View'. From version 11 you can assign a 'Role' but still disallow access to 'Desk View' by unchecking 'Desk Access' in Role.

![Disallow Desk Access](/files/disallow_desk_access.png)  


In Portal Settings, you can set a role against each menu item so that only users with that role will be allowed to see that item.

![portal settings](/files/portal-settings.png)  


### 2.5 Custom Script

You can write custom scripts for your Web Form for things like validating your inputs, auto-filling values, showing a success message, or any arbitrary action.

To learn how to write custom scripts for your Web Forms, read [Custom Scripts documentation](https://frappeframework.com/docs/user/en/desk/scripting/client-script).

### 2.6 Custom CSS

You can customize the look and feel of your Web Form by writing your own Custom CSS. Inspect the elements on the page to see what classes are available for styling. Learn more about CSS [here](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics).

### 2.7 Actions

You can add the text in 'Success Message' field and this text will be shown to user once he successfully submits the web form . And the user is redirected to the URL given at 'Success URL' when clicked on 'Continue' button. This is only applicable to webforms accessible without the user login(webforms with 'Login Required' checkbox unchecked).

![Success Message](/files/success_message.png)  


### 2.8 Result

When a website user submits the form, the data will be stored in the document/doctype for which web form is created.

### 2.9 Customizing

For customizing web forms, see the [Frappe Web Forms Documentation](https://frappeframework.com/docs/user/en/web-form)

<!-- page: erpnext/erpnext__web-page-builder.md -->
---
title: "Web Page Builder\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/web-page-builder"
updated: "2026-02-28"
---


> Introduced in Version 13

**Page Builder lets you quickly create web pages from pre-configured web templates.**

## 1. How to create a page using Page Builder

1. Follow the steps to [create a Web Page](/erpnext/web-page).
1. Enable full width by ticking the "Full Width" checkbox.
1. Select Content Type as **Page Builder**.
1. Click on Add Row in the Page Building Blocks Table.
1. Select a Web Template.
1. Click on the **Edit Values** button.
1. Enter values in the dialog and click on Submit.
1. Click on Save.
1. The web page will be published only when **Published** is ticked.

![New Web Page with Page Builder](/files/new-web-page-with-page-builder.png)
_New Web Page with Page Builder_

![Page Builder Edit Values Dialog](/files/page-builder-edit-values-dialog.png)
_Page Builder Edit Values Dialog_

View your Web Page by clicking on **See on Website** in the sidebar.

![Web Page](/files/web-page-with-page-builder-preview.png)
_Web Page with Page Builder_

### 1.1 Add Sections

You can add more sections to your page by adding more rows in the Page Building Blocks
table. The framework comes with a great set of Web Templates for you to create
all sorts of pages.

![More Sections](/files/web-page-with-more-sections.png)
_Web Page with another section_

![More Sections - Preview](/files/web-page-with-more-sections-preview.png)
_Web Page with another section - Preview_

### 1.2 Section Options

If you click to expand a row in the Page Building Blocks table, you have the
following additional options:

- **Add Container**: If checked, the web template will be rendered in a centered constrained box.
- **Add Space on Top**: If checked, it will add a decent amount of space above the section.
- **Add Space on Bottom**: If checked, it will add a decent amount of space below the section.
- **Add Gray Background**: If checked, it will add a gray background to the section.
- **Hide Block**: If checked, it will hide the section block.
- **CSS Class**: Add any CSS class and style it in the CSS field in the Style section.

![Section Options](/files/page-builder-section-options.png)
_Section Options_
