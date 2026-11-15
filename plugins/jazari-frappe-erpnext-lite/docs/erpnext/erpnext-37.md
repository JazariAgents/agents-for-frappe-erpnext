<!-- Frappe documentation: erpnext, part 37 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__maximum-number-of-fields-in-a-form.md -->
---
title: "Maximum Number of Fields in a Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maximum-number-of-fields-in-a-form"
updated: "2026-06-10"
---

If you have been customizing ERPNext by adding Custom Fields to forms, you may reach a point where:

- A newly added Custom Field causes a **Server Error** when you try to submit a document, or
- ERPNext refuses to save after the field is added.

 This article explains why this happens and walks you through practical ways to fix it — no database knowledge required. 

## What the Errors Mean

When you hit the limit, ERPNext may show one of these two errors on screen:

### Error 1:  "Unknown column in INSERT INTO"

[Screenshot on the live page]

 This error appears when you submit a form after adding a new Custom Field. ERPNext is trying to save data for a column it cannot find in the database yet,  a sign that the underlying table has hit its structural limit and the new field could not be properly registered.

### Error 2: "Row size too large"

[Screenshot on the live page]

 This error is more direct. The database table's row has exceeded its maximum allowed size of **65,535 bytes**. 

## Why Does This Happen?

In ERPNext (and Frappe), every form, called a **DocType**, corresponds to a table in the database. Each field on that form is a column in that table.



Think of it like a spreadsheet: every row can only hold so many columns before it runs out of space. MySQL (the database ERPNext uses) enforces a hard row size limit of **65,535 bytes** per table row. MySQL also technically supports up to 4,096 columns per table, but in practice the row size limit is hit first.



Here is a concrete example of how quickly that limit is reached:



- Fields of type **Data, Link, Select, Dynamic Link, Password,** and **Read Only** are stored as `VARCHAR(140)` columns in the database.
- A `VARCHAR(140)` column using the `utf8mb3` character set allocates up to **420 bytes** per value (140 characters × 3 bytes each).
- That means a table can hold at most roughly **65,535 ÷ 420 = ~156** such columns before hitting the limit.

The form / doctype in question already has many built-in fields. Installing custom apps adds even more. Once you approach this ceiling, adding even one more Custom Field can push it over the edge, causing the submission errors shown above.

---

## Functional Solutions

There are several ways to address this, ranging from quick fixes to structural changes. Start with the quick fixes if you only need a little more room, or go with the structural options if you need to add many more fields.

### Fix 1: Create a Separate DocType and Link It to Primary DocType

This is the best long-term approach when you need to add a **distinct group of related fields** (e.g., fields for a specific department, process, or compliance requirement).



**Steps:**

1. Go to **Customize > DocType** (or search "New DocType" in the search bar).
2. Create a new DocType with all the fields you need.
3. In the new DocType, add a **Link** field pointing to Primary DocType (in which you wanted to add all the fields), this connects each record back to its parent Stock Entry.
4. Optionally, add a Link field on Stock Entry's Customize Form pointing back to your new DocType for easy navigation.

**Why this works:** Your new DocType gets its own separate database table with its own row size budget, completely independent of Stock Entry's table.



---

### Fix 2: Create a Child Table and Add It to Stock Entry

This approach works best when your extra fields represent **repeating rows of data**. For example, a quality checklist or a list of items, similar to how the Items table works inside Stock Entry.



**Steps:**

1. Go to **Customize > DocType** and create a new DocType. Enable the **"Is Child Table"** checkbox.
2. Add all your fields as columns inside this child table.
3. Go to **Customize Form > Stock Entry**.
4. Add a new field of type **Table** and set its **Options** to point to your newly created child DocType.

**Why this works:** A Child Table is stored in its own separate database table, entirely sidestepping the row size limit of the parent form.

---

## Techical Fixes

### Fix 1: Convert Some Fields to Text-Based Types

Fields of type **Text, Small Text, Text Editor,** or **Code** are stored differently in MySQL (as `TEXT` or `BLOB` columns). Unlike `VARCHAR` columns, their content is stored outside the main row — they only occupy **9–12 bytes** in the row itself instead of up to 420 bytes.



**What to do:** In **Customize Form**, find any Custom Fields that currently use types like Data, Link, or Select, where the value is long or does not need to be filtered/sorted, and replace them with field type to **Small Text** or **Text**. Each conversion frees up significant row space and allows more fields to be added.



---

### Fix 2: Reduce the "Length" Property of Existing Fields

When creating a Data-type Custom Field, ERPNext sets a default **Length** of 140. This directly controls how many bytes MySQL allocates for that column. Reducing it on fields where a shorter input is sufficient (e.g., a code field that will never exceed 20 characters) frees up space proportionally.



**What to do:** In **Customize Form**, open each Custom Field's settings and lower the **Length** value to what is actually needed. For example, changing Length from 140 to 20 reduces that column's allocation from 420 bytes to just 60 bytes.



---

### Fix 3: Remove Unused Custom Fields Using Trim Tables

Custom Fields that are deleted from Customize Form are **not automatically removed from the database table** — their columns remain, still consuming row space.



If you are certain you no longer need the data from some old Custom Fields, you can permanently remove those columns from the database by running the `trim-tables` bench command:



[https://frappeframework.com/docs/user/en/bench/reference/trim-tables](https://frappeframework.com/docs/user/en/bench/reference/trim-tables)



> **Note:** This operation is irreversible. Any data stored in those columns will be permanently deleted. Always take a database backup before running this command.

## Choosing the Right Solution


| Your situation                                              | Recommended approach                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------------- |
| You need many new single-value fields (one value in a form) | Create a Separate Linked DocType                                 |
| You need repeating rows of data per Stock Entry             | Create a Child Table                                             |
| A few fields are pushing you over the limit                 | Convert some fields to Small Text / Text, or reduce field Length |
| You have deleted Custom Fields but their columns remain     | Run `trim-tables` to reclaim space                               |

<!-- page: erpnext/erpnext__merging-accounts.md -->
---
title: "Merge Accounts | ERPNext Documentation"
description: "Learn how to safely merge duplicate Accounts in ERPNext, verify matching properties, choose the correct target, and confirm historical ledger results."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/merging-accounts"
updated: "2026-08-14"
---

Merge Accounts when two Account records in the same [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) represent the same ledger or the same group and you want to keep only one. ERPNext replaces references to the source Account with the target Account, then removes the duplicate source record.



For example, Nova Industries has both **SaaS Subscription Expenses** and **Software Subscription Expenses** for the same recurring software costs. The accounting team decides to retain **Software Subscription Expenses** and merge the duplicate into it.



Merging changes historical links. Treat it as a controlled data-cleanup operation, not a convenient way to rename an Account.

## Before you begin

Confirm the source Account is truly a duplicate. Compare its purpose, parent, currency, account type, tax use, default-account use, and historical transactions with the intended target.

ERPNext allows the merge only when both Accounts have the same:


| Property         | Why it must match                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------- |
| Is Group         | A group cannot be merged into a ledger, and a ledger cannot be merged into a group.          |
| Root Type        | Asset, Liability, Equity, Income, and Expense Accounts cannot be combined across root types. |
| Company          | Each [Company](https://docs.frappe.io/erpnext/company) has a separate Chart of Accounts.     |
| Account Currency | Existing ledger values must retain a consistent currency.                                    |


Run the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) for both Accounts and compare balances in the [Trial Balance](https://docs.frappe.io/erpnext/trial-balance). If either Account has a special purpose or should remain separately reportable, do not merge it.

Take a current [data backup](https://docs.frappe.io/erpnext/setting-up-data-backups) before merging important production Accounts. There is no normal user-interface action that separates the records again.

## Select the source Account

Open **Chart of Accounts**, select the company, and find the Account that should disappear after the merge. You can also open the Account list and filter by name.



[Screenshot on the live page: Filtered Account list showing the duplicate source Account]

Open the source Account and verify its Company, Root Type, Report Type, Currency, Account Type, and whether it is a group. In this example, **SaaS Subscription Expenses - NET** is the duplicate source.

## Open Merge Account

On the source Account, select **Actions &gt; Merge Account**.



[Screenshot on the live page: Merge Account action on an Account record]

Do not use **Update Account Name / Number** for this task. That action renames one Account; it does not combine two existing Account records.

## Choose the target Account

In **Merge with Existing Account**, enter the full name of the Account that must remain. For the example, the target is **Software Subscription Expenses - NET**.



[Screenshot on the live page: Target Account and Merge button in the Merge with Existing Account dialog]

Review the direction before selecting **Merge**:


| Role           | Example                              | Result                                      |
| -------------- | ------------------------------------ | ------------------------------------------- |
| Source Account | SaaS Subscription Expenses - NET     | Removed after references are moved.         |
| Target Account | Software Subscription Expenses - NET | Remains and receives the source references. |


Select **Merge** only after another reviewer confirms the direction and target.

## What changes after the merge

ERPNext updates links that previously pointed to the source Account so they point to the target Account. Existing transactions therefore show the target Account name when opened after the merge.

The [accounting entries](https://docs.frappe.io/erpnext/accounting-entries), debit and credit amounts, voucher dates, and parties do not change merely because the Account master was merged. What changes is the Account under which those entries are grouped and reported.

After the merge:

1. Search for the source Account and confirm it no longer exists as a separate master.
2. Open the target Account and use **View &gt; General Ledger**.
3. Confirm historical entries from both Accounts appear under the target.
4. Re-run the Trial Balance, [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet), or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement), as applicable.
5. Compare totals with the pre-merge reports. Consolidation should change the presentation, not the company's total debit, credit, profit, or net assets.

The [immutable ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext) still preserves submitted accounting effects. Merging the Account master reassigns links; it does not cancel and repost every voucher.

## Important fields and controls


| Field or control | Meaning                                      | Check before merging                         |
| ---------------- | -------------------------------------------- | -------------------------------------------- |
| Source Account   | Account opened when you start the action     | This record will no longer remain separate.  |
| Name             | Full target Account ID entered in the dialog | Confirm the company suffix and exact target. |
| Is Group         | Whether the Account contains child Accounts  | Must match between source and target.        |
| Root Type        | Asset, Liability, Equity, Income, or Expense | Must match between source and target.        |
| Company          | Legal entity that owns the Account           | Must match between source and target.        |
| Currency         | Currency of the Account ledger               | Must match between source and target.        |
| Merge            | Runs the consolidation                       | Select only after review and backup.         |


## Troubleshooting

### ERPNext says the Accounts have different properties

Compare **Is Group**, **Root Type**, **Company**, and **Currency** on both records. Current ERPNext requires all four to match. Do not change a property merely to bypass the validation unless the underlying accounting setup is genuinely wrong.

### ERPNext says the system is in use

Account merging locks and updates many linked records. Current ERPNext blocks the operation when General Ledger entries were updated recently. Stop accounting activity, wait at least five minutes after the last GL update, then retry during a quiet period.

### The target Account is not found

Enter the full Account ID, including its company suffix. Confirm that the target exists in the same company and that your role has write permission for both Accounts.

### Financial totals changed unexpectedly

Stop further cleanup. Compare pre-merge reports, the target General Ledger, and the affected [Journal Entries](https://docs.frappe.io/erpnext/journal-entry). Account merging should consolidate classification without changing the total double-entry amounts. Restore the backup or escalate to an administrator if the result is not understood.

### The Chart of Accounts tree looks incorrect

Reload the tree first. If a structural problem remains, investigate it before using any repair tool. Account merging is not a substitute for correcting parent relationships or rebuilding a damaged tree.

## FAQs

### Can I merge a group Account into a ledger Account?

No, Both Accounts must either be groups or both be ledgers.

### Can I merge Accounts from different companies?

No, The source and target must belong to the same company.

### Does merging delete historical transactions?

No, ERPNext updates their Account references to the target. Verify the target ledger after the merge.

### Can I undo an Account merge?

There is no standard split or unmerge action. A tested backup is the reliable recovery path for an incorrect merge.

### Should I merge an Account when I only want a better name or number?

No, Use **Actions &gt; Update Account Name / Number** when only one Account exists and its identity needs correction.

## Related topics

- [Changing Parent Account](https://docs.frappe.io/erpnext/changing-parent-account)
- [Freeze an Account](https://docs.frappe.io/erpnext/freeze-an-account)
- [Rebuild Tree](https://docs.frappe.io/erpnext/rebuild-tree)
- [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer)
- [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings)

<!-- page: erpnext/erpnext__migrate-to-perpetual-inventory.md -->
---
title: "Migrate To Perpetual Inventory\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/migrate-to-perpetual-inventory"
updated: "2026-03-02"
---


Perpetual Inventory Valuation is activated by default in the system.

For the users who are currently following periodic inventory valuation system, and wish to migrate to perpetual inventory valuation system, please follow the steps explained below.

### 1. How to Migrate to Perpetual Inventory

1. To enable perpetual Inventory, ensure that the Stock in Hand Account is synced with the value of actual stock value in your Warehouse(s). To sync it, you will have to create a Journal Entry for the difference amount against expense account (generally used in Purchase Invoice).

 For example, when perpetual inventory was disabled, you must be having Expense (Cost of Goods Sold) booked via Purchase Invoices. Now, you will have to create a Journal Entry to move the value of existing stock from expense account to stock in hand account.

 Cr. Expense account ......... XXX

 Dr. Stock in Hand account ... XXX

 It can also work other-way round if you were selecting a stock in hand account in the Purchase Invoice.

1. Before enabling Perpetual Inventory, ensure that Stock Accounts (ledger) is linked for the existing Warehouse. The stock account for a Warehouse can be set at three levels.

 * In the Warehouse master itself
 * In the Parent Warehouse master
 * Default Stock in Hand Account in the Company master, if you maintain only one Stock-in-hand account for all the Warehouses.

1. Journal Entry to Update Stock Received but not Billed account

 An account "Stock Received but not Billed" is an adjustment account which reflects the value of the stock for which Purchase Receipt has been submitted, but Purchase Invoice is yet to created. A Journal Entry should be created to update the value open Purchase Receipt pending for billing into "Stock Received but not Billed" account.

 To know the value of the stock received but not billed, you can refer the report "Received Items Pending for Billing" in the Accounts module.

 Create a Journal Entry as follows to update the value in Stock Received but not Billed account.

 Cr. Stock Received but not Billed ........... XXX

 Dr. Expense Account (COGS) .................. XXX

1. Setup the following default accounts for each Company

 * Stock Received But Not Billed
 * Stock Adjustment Account
 * Expenses Included In Valuation
 * Cost Center
 * Activate Perpetual Inventory

1. Go to: **Home > Accounting > Company**

 [Screenshot on the live page: Perpetual Inventory]

#### 2. Related Topics
1. [Accounting Of Inventory Stock](/erpnext/accounting-of-inventory-stock)
1. [Perpetual Inventory](/erpnext/perpetual-inventory)

<!-- page: erpnext/erpnext__milestone-tracker.md -->
---
title: "Milestone Tracking\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/milestone-tracker"
updated: "2026-03-02"
---

> Introduced in Version 12

**You can automatically track milestones based on the lifecycle of a document if it undergoes multiple stages.**

The configuration for Milestone setting can be set in **Milestone Tracking** and each milestone is updated in **Milestone**

To access Milestone Tracker, go to:

> Home > Settings > Milestone Tracker

## 1. Creating a Milestone Tracker

1. Click on New.
2. Set the Document Type to track (example: "Issue").
3. Set the field that represents stages (example: "Status").

> Note: A milestone stage can be defined by Link or Select properties.

Once this is set, a new **Milestone** record is created every time the status of any issue is changed.

The Milestone can be viewed in the timeline of the view:

[Screenshot on the live page: Assign]

Note: Milestones work independently of Versions.

## 2. Features

Milestones can be a great source for reporting and notifying. For example, if Lead Qualification is a milestone on "Lead", milestones can help generate reports on the number of leads being qualified in a period.

### 2.1 Using Milestones with Dashboards

Used along with Dashboards, Milestones can help track the trends in milestones. For example, if "Qualification" is tracked as a "Lead Stage", a Dashboard on Milestone filtered by Qualification will show the trends of leads qualified.

### 2.2 Using Milestones with Energy Points

Energy Point Rules can be defined to automatically give Energy Points to users who achieve a milestone. This can be used to incentivize action on transactions at various levels.

<!-- page: erpnext/erpnext__mode-of-payment.md -->
---
title: "Mode of Payment | ERPNext Documentation"
description: "Set up cash, bank, card, and other payment methods in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/mode-of-payment"
updated: "2026-07-31"
---

A Mode of Payment identifies how money is received or paid, such as cash, bank transfer, card, or check. It also helps ERPNext choose the correct default ledger for each Company when users create a [Payment Entry](/erpnext/payment-entry) or a Point of Sale transaction.

## Before you begin

Create the required cash and bank ledgers in the [Chart of Accounts](/erpnext/chart-of-accounts). Confirm each account's type and currency, and decide which account each [Company](/erpnext/company) should use for the payment method.

## Create a Mode of Payment

1. Open **Mode of Payment** and select **Add Mode of Payment**.
2. Enter a clear name, such as Cash, Bank Transfer, or Corporate Card.
3. Choose the payment **Type**.
4. In **Accounts**, add each Company and its default cash or bank ledger.
5. Save the record, then test it in a Payment Entry or [POS Profile](/erpnext/pos-profile).

[Screenshot on the live page: Mode of Payment list in ERPNext]

## Important fields and what they mean


| Field           | What it controls                                                                |
| --------------- | ------------------------------------------------------------------------------- |
| Mode of Payment | Name users select in transactions.                                              |
| Type            | Classifies the method as Cash, Bank, General, Phone, or another available type. |
| Enabled         | Controls whether users can select it.                                           |
| Company         | Company for which the default account applies.                                  |
| Default Account | Ledger ERPNext proposes when this mode is selected.                             |


The Type describes the method. The Default Account determines which ledger is used. Selecting a Mode of Payment does not by itself create a General Ledger entry. The accounting effect comes from submitting the transaction that uses it.

## Troubleshooting

### ERPNext asks me to set a default Cash or Bank account

Open the selected Mode of Payment and add an **Accounts** row for the transaction's Company. Choose a ledger whose account type and currency match the payment. If the transaction comes from POS, also check the Mode of Payment rows in the POS Profile.

### The wrong account appears in Payment Entry

Check whether the Mode of Payment has a default account for the current Company. A Company-specific row takes effect only for that Company. Also review whether the Payment Entry was created from another document that supplied its own account.

### A cash payment appears in Bank Reconciliation

The label Cash does not make the linked ledger a cash account. Review the Default Account in the Chart of Accounts. If it is configured as a Bank account, transactions can appear in [Bank Reconciliation](/erpnext/bank-reconciliation). Link the mode to the actual cash ledger instead.

### Users cannot select the mode

Confirm that **Enabled** is selected and that the mode is included in the relevant POS Profile or transaction setup. Also check user access to the Company and account.

## Frequently asked questions

### Can one Mode of Payment use different accounts for different companies?

Y

es. Add one Accounts row per Company. ERPNext prevents duplicate rows for the same Company because each mode has one default account per Company.

### Can I assign a different default account for each branch?

The standard Mode of Payment mapping is Company-based, not branch-based. For branch-specific retail payments, use separate POS Profiles with the appropriate payment accounts. More complex branch logic requires a controlled customization.

### Does the Type field decide which ledger is posted?

Type classifies the payment method. The Default Account and the submitted transaction determine the ledger posting. Always verify the proposed Paid From and Paid To accounts before submitting.

### Should I create a Mode of Payment for every bank account?

Usually not. Create names that are meaningful to users, then map each mode to the appropriate Company account. Separate modes are useful when users must deliberately distinguish methods or when different operational flows need different defaults.

### Is a Mode of Payment the same as an online payment gateway?

A Mode of Payment labels and maps the accounting method. An online [Payment Gateway](/erpnext/payment-gateway) also requires integration credentials and gateway configuration. The gateway's completed transaction can then be represented by a suitable Mode of Payment.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [POS Profile](/erpnext/pos-profile)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Payment Gateway](/erpnext/payment-gateway)

<!-- page: erpnext/erpnext__module-settings.md -->
---
title: "Module Settings | ERPNext Documentation"
description: "Learn how ERPNext module settings organise configuration for each business process and how to choose the correct settings page."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/module-settings"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor used throughout this guide. Its sales team prepares quotations, the warehouse dispatches devices, the factory assembles selected products, and the finance team records every result. When the company introduces a repair service, its administrator must decide where to configure the new process. A site-wide security setting, a Selling setting, and a Stock setting can all look like "system settings", but they solve different problems.



Module Settings is the map that takes the administrator to the settings owned by each business process. It helps Nova change how Sales Orders behave without accidentally changing login security, accounting rules, or another module. Use it to find the correct settings page, then test the change in the transaction that consumes it.

[Screenshot on the live page: ERPNext Desk showing the business modules available to Nova Industries]

## How module settings are organised


| Settings page          | What it controls                                                                         | Nova Industries example                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Accounts Settings      | Accounting validations, invoices, deferred accounting, dimensions, and closing behaviour | Finance requires a credit limit check before a Sales Order is submitted.                |
| Selling Settings       | Customer and selling-document defaults                                                   | Sales wants the same territory and price-list behaviour on every quotation.             |
| Buying Settings        | Supplier and purchasing-document behaviour                                               | Purchasing decides whether a Purchase Order is required before invoicing.               |
| Stock Settings         | Warehouses, valuation, reservations, and stock transaction behaviour                     | Warehouse users need serial-number and negative-stock rules to match company policy.    |
| Manufacturing Settings | Production defaults and manufacturing controls                                           | The assembly team wants Work Orders and Job Cards to follow a defined capacity process. |
| Projects Settings      | Project, task, and time-tracking defaults                                                | The repair service bills work from Timesheets linked to Projects.                       |
| Support Settings       | Issue and service-level behaviour                                                        | Support assigns incoming customer issues to a default service team.                     |
| CRM Settings           | Lead, opportunity, and communication behaviour                                           | Sales wants website enquiries to become Leads with consistent ownership.                |


## Choose the correct settings page

Start with the transaction or process that should change. If the change should affect only Sales Orders, open Selling Settings. If it affects every user, such as password policy or date format, use [System Settings](/erpnext/system-settings). If it merely supplies a common Company or Currency on new records, use [Global Defaults](/erpnext/global-defaults). If it should last only for one user session, use [Session Defaults](/erpnext/session-defaults).



After saving a module setting, create a fresh draft transaction and confirm the intended result. Existing submitted transactions normally preserve their earlier state and should not be treated as proof that the new configuration failed.

## Troubleshooting

### A module setting does not affect an existing document

Reload the form and test with a new draft. A setting may apply only when a document is created or when a particular transaction condition is met.

### A settings page is missing

Confirm that the app and module are installed, the relevant domain is active, and the user has the System Manager or other required role.

### A user can still open a module

Module Settings controls behaviour, not access. Configure roles, Role Permissions, User Permissions, and Workspace visibility for access control.

## Frequently asked questions

### Do Module Settings apply to every company?

Many module settings are site-wide, while some rows or defaults are company-specific. Read the field description and test with the affected company before rollout.

### Are Module Settings a replacement for Company defaults?

Company defaults supply accounts and other company-owned values. Module settings control process behaviour. Both can affect the same transaction for different reasons.

### Should administrators change several settings at once?

Change one business decision at a time and verify it in a new transaction. This makes an unexpected result easier to trace.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Global Defaults](/erpnext/global-defaults)
- [Session Defaults](/erpnext/session-defaults)
- [Domain Settings](/erpnext/domain-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [Workspace](/erpnext/workspace)

<!-- page: erpnext/erpnext__moving-asset-from-stock-item-to-fixed-asset-item.md -->
---
title: "Moving Asset from Stock Item to Fixed Asset Item | ERPNext Documentation"
description: "Correct an ERPNext Item that was treated as stock but should be a fixed asset without losing accounting control."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/moving-asset-from-stock-item-to-fixed-asset-item"
updated: "2026-08-15"
---

Imagine Nova Industries bought a laptop intending to sell it, so it was received as inventory. Later, the company decides to give that laptop to an employee. It is no longer stock for sale, but simply selecting **Is Fixed Asset** can leave the same value appearing in both inventory and fixed assets.



The correction must remove the approved inventory position first, then create the fixed-asset Item and Asset record with the right original cost and opening depreciation. This keeps the Stock Ledger, General Ledger, and Asset Register from counting the laptop twice.

## Before you begin

Back up the site, identify every stock transaction for the Item, reconcile its current quantity and valuation, and agree the correction date and accounts with the accounting owner. Do not use this procedure to rewrite genuine historical sales inventory.

## Correct the stock position

1. Stop new transactions for the Item during the correction.
2. Use the appropriate [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation) or supported stock transaction to bring the stock position to the approved result.
3. Verify Stock Ledger and General Ledger impact.
4. If submitted transactions prevent changing Item type, create a new fixed-asset Item rather than forcing the existing record.

## Configure the fixed-asset Item

Enable **Is Fixed Asset**, select the Asset Category, and decide whether future purchases should auto-create Assets.

[Screenshot on the live page: ERPNext Item configured as a fixed asset]

## Create the Asset

Create an Existing Asset using the approved original cost, available-for-use date, opening accumulated depreciation, and number of already booked depreciation entries.

[Screenshot on the live page: Existing Asset created after reclassification]

## Verify the correction

Confirm stock quantity is no longer carried incorrectly, the Asset appears in the register, opening value and depreciation reconcile, and no cost was counted twice.

[Screenshot on the live page: Asset list used to verify the reclassified item]

## Troubleshooting

### Is Fixed Asset cannot be enabled

The Item has submitted stock transactions or quantity. Create a new fixed-asset Item and use controlled accounting entries instead of forcing the flag.

### The asset cost appears in both stock and fixed assets

Reverse or correct the stock side, then reconcile Stock Ledger, General Ledger, and Fixed Asset Register on the same date.

### Opening depreciation is missing

Enter approved opening accumulated depreciation and the number of booked depreciations on the Existing Asset before final submission.

## Frequently asked questions

### Can I convert an Item after years of stock transactions?

Usually a new fixed-asset Item is safer because historical inventory transactions must remain valid.

### Should the reclassification use a Journal Entry only?

A Journal Entry may correct accounts but does not create the operational Asset history or remove stock quantity. Use the full controlled process.

### What date should the Asset use?

Use the approved original purchase and available-for-use dates, with opening depreciation as of the migration or correction cut-off.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__mpesa-integration.md -->
---
title: "M-Pesa Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/mpesa-integration"
updated: "2026-02-26"
---


**M-Pesa integration allows processing transactions with the payment gateway provider M-Pesa.**

M-Pesa Integration facilitates the processing of payments between the M-Pesa application and ERPNext. M-Pesa Integration only works with the POS to facilitate the payments for the same. This feature doesn't work with the shopping cart.

To set up M-Pesa, go to:
> Integrations > Payments > M-Pesa Settings

## 1.How to get your M-Pesa credentials?
1. In order to activate your API credentials, you need to log in to your M-Pesa account.
2. Then, open the Go Live section of the application and follow the steps to get the approval for the app.
3. When all the test cases are satisfied and expected results match the final results, you need to submit the document and follow the steps to get the final credentials for your application.
4. Details mentioned in the Production URL and Credentials section are the credentials that you are supposed to use in M-Pesa Settings.

[Screenshot on the live page: Mpesa Credentials]


## 2.Setting up M-Pesa

To enable M-Pesa Express, you need to configure all the mandatory parameters which you have received from M-Pesa. If you want to use the staging environment of the integration, you can select the staging option and use the staging credentials provided by M-Pesa by creating a separate application for the same.
[Screenshot on the live page: Mpesa Settings]

On enabling the M-Pesa integration in ERPNext, the system will create a Payment Gateway record and an Account head in the Chart of Accounts with the Account type as Bank as seen in the following screenshot.

[Screenshot on the live page: Mpesa COA]
[Screenshot on the live page: Mpesa POS Settings]

It will also create a Mode of Payment with the same name and account as the payment gateway's, along with certain custom fields in POS Settings to handle the POS payments.

[Screenshot on the live page: Payment Gateway Account]

After configuring the Payment Gateway Account, you will be able to accept online payments via M-Pesa.


## 3. M-Pesa POS Payments

On setting up the POS profile with M-Pesa mode of payment, the POS checkout would show an additional information section. This section contains two fields that were automatically set-up on adding M-Pesa settings.

[Screenshot on the live page: POS Additional Information]

As soon as a POS user fills the mobile number of the customer, they can initiate a request for payment from the customer. A request is sent to the customer's M-Pesa mobile application linked with the specified mobile number. Once the payment is processed by the user, the user is prompted by a confirmation dialog to submit the payment.

## 4. M-Pesa Account Balance

Account balance linked with an individual M-Pesa can be fetched via the Get Account Balance button. This will load the M-Pesa account balance details in the dashboard.

[Screenshot on the live page: POS Account Balance]


## 5. Supporting transaction currencies

M-Pesa will only work for the Company which has KSH (Kenyan Shilling) as the Company Currency.
