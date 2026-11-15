<!-- Frappe documentation: erpnext, part 13 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__change-valuation-method.md -->
---
title: "Change Valuation Method"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/change-valuation-method"
updated: "2026-02-20"
---

In the ERPNext, users can change the valuation method from FIFO to Moving Average, but not from Moving Average to FIFO, for items with existing stock transactions.

If a user changes the valuation method from FIFO to Moving Average for any item, the system will use the Moving Average method for new outward transactions. Additionally, if the user creates backdated transactions, all transactions created after that backdated entry will be reposted using the Moving Average method. This may result in changes to the closing balance value of earlier transactions.

To prevent this, users can freeze stock transactions before a specific date by setting the "Stock Frozen Up To" date in the stock settings.


![](/files/Screenshot%202025-04-29%20at%204.38.39%20PM.png)

<!-- page: erpnext/erpnext__changing-parent-account.md -->
---
title: "Change the Parent Account | ERPNext Documentation"
description: "Learn how to change an Account's parent in ERPNext, understand report reclassification, validate the new group, and verify the saved Chart of Accounts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/changing-parent-account"
updated: "2026-08-03"
---

The Parent Account determines where an Account appears in the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) tree and how its balance rolls up in financial reports. Change it when an existing ledger or group was placed under the wrong branch and must be reclassified.



For example, Nova Electronics Trading initially placed **Warranty Fulfilment Costs** under **Indirect Expenses**. Because these costs arise directly from fulfilling product warranties, the accounting team reclassifies the Account under **Direct Expenses**.



Changing the parent does not create a new Account and does not rewrite transaction amounts. It changes the structural classification of the existing Account, including how its current and historical balances roll up in reports.

## Before you begin

Confirm the accounting reason for the move with your accountant. A parent change can affect subtotals, gross profit, operating expenses, and the presentation of earlier periods even though total debit and credit remain unchanged.

Review the Account in the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), then save the relevant [Trial Balance](https://docs.frappe.io/erpnext/trial-balance) and financial statements before the change. These provide a comparison point after reclassification.

The target parent must:


| Requirement                                                          | Reason                                                                                                                                                                                                       |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Belong to the same [Company](https://docs.frappe.io/erpnext/company) | Each company maintains a separate Chart of Accounts.                                                                                                                                                         |
| Be a group Account                                                   | A ledger cannot contain child Accounts.                                                                                                                                                                      |
| Belong to the correct root branch                                    | The Account must remain under the intended Asset, Liability, Equity, Income, or Expense structure.                                                                                                           |
| Support the intended report classification                           | The parent determines whether balances roll into the [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet) or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement). |


Do not use this procedure to combine duplicate Accounts. Use **Merge Account** for a genuine duplicate. Do not create a new Cost Center merely to repair an Account hierarchy; [Cost Centers](https://docs.frappe.io/erpnext/cost-center) serve a different reporting purpose.

## Open the Account

Open **Chart of Accounts**, select the company, and find the Account to move. Select the Account and open **Edit**, or open the Account directly from the Account list.

The example Account currently has **Indirect Expenses - NET** as its parent.



![Current Parent Account on Warranty Fulfilment Costs](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-changing-parent-account-current-parent-account.png)

Before editing, confirm the Account name, Company, Root Type, Report Type, Currency, Account Type, and whether **Is Group** is enabled. If the Account is a group, the move also repositions every child beneath it.

## Select the new parent

In **Parent Account**, select the correct target group. For this example, choose **Direct Expenses - NET**.



![New Parent Account selected before saving](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-changing-parent-account-change-parent-account-before-save.png)

Review the full target name and company suffix, then select **Save**. ERPNext validates that the target is a group in the same company and updates the tree relationship.

## Confirm the saved result

After saving, the Account retains its identity but shows the new parent. The activity timeline records the Parent Account change.



![Saved Account with Direct Expenses as the new parent](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-changing-parent-account-changed-parent-account-saved.png)

Return to Chart of Accounts and confirm the Account appears under the intended branch. Re-run the same reports used before the change.

For the example:


| Before                                                  | After                                                 | What stays the same                                                                      |
| ------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Warranty Fulfilment Costs rolls into Indirect Expenses. | Warranty Fulfilment Costs rolls into Direct Expenses. | Account identity, linked vouchers, debit and credit amounts, parties, and posting dates. |


The [accounting entries](https://docs.frappe.io/erpnext/accounting-entries) remain linked to the same Account. Their presentation changes because the Account now rolls up through a different parent.

## How the parent affects other fields

ERPNext derives structural values from the parent. Understand the difference before changing anything:


| Field          | Meaning                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Parent Account | Immediate group directly above the Account in the tree.                                                                                   |
| Root Type      | Top-level accounting class: Asset, Liability, Equity, Income, or Expense.                                                                 |
| Report Type    | Balance Sheet or Profit and Loss, derived from the root branch.                                                                           |
| Is Group       | Indicates that the Account contains child Accounts and cannot receive normal transaction postings.                                        |
| Account Type   | Describes a special use such as Bank, Receivable, Payable, Tax, or Cost of Goods Sold. It is not the same as Parent Account or Root Type. |


If you move an Account to a different root branch, ERPNext updates the structural classification from the target parent. Such a move can materially change financial statements and requires careful review.

## Important fields and controls


| Field or control | Guidance                                                                |
| ---------------- | ----------------------------------------------------------------------- |
| Account          | Existing ledger or group being moved. Do not create a duplicate.        |
| Parent Account   | Select the exact group that should contain the Account.                 |
| Company          | Must match the target parent.                                           |
| Root Type        | Review the resulting top-level classification.                          |
| Report Type      | Review whether the balance belongs in Balance Sheet or Profit and Loss. |
| Is Group         | If enabled, all child Accounts move with the group.                     |
| Account Type     | Confirm the special use still makes sense in the new branch.            |
| Save             | Applies the structural change and records it in the timeline.           |


## Troubleshooting

### The target does not appear in Parent Account

Confirm it is a group Account in the same company. A normal ledger cannot be selected as a parent. If the group does not exist, create it from the Chart of Accounts tree before moving the child.

### The Report Type is not editable

This is expected. ERPNext derives Report Type from the parent and root branch. Select the correct Parent Account instead of forcing the field through customization or browser scripts.

### Historical financial statements changed

The Account's balance now rolls up through the new parent, including historical transactions. Compare the before-and-after reports and confirm that this is the intended reclassification. The company's total balanced [Journal Entries](https://docs.frappe.io/erpnext/journal-entry) should not change.

### I moved a group and several Accounts moved with it

That is expected. A group carries its full subtree. Review every child before saving a group-level parent change.

### The tree still shows the previous structure

Reload Chart of Accounts and expand the target branch. If the saved Parent Account is correct but the tree remains inconsistent, investigate before using a repair tool.

## FAQs

### Is Parent Account the same as Root Type?

No, Parent Account is the immediate group above the Account. Root Type is the top-level accounting class inherited through the tree.

### Does changing the parent move existing transactions?

The transactions remain linked to the same Account. Their balances are presented under the Account's new parent hierarchy.

### Can I move an Account from Profit and Loss to Balance Sheet?

Only with a valid accounting reason and careful review. Such a move changes the report classification of all balances linked to the Account.

### Can a ledger Account become a parent?

No, A parent must be a group. Convert or create the correct group only when the Account has no incompatible transactions or children and the accounting design supports it.

### Should I change parents through Data Import?

For a small number of Accounts, use the Account form so each change can be reviewed. For a migration or large redesign, use a tested [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer) plan in a non-production site before updating live data.

## Related topics

- [Merge Accounts](https://docs.frappe.io/erpnext/merging-accounts)
- [Freeze an Account](https://docs.frappe.io/erpnext/freeze-an-account)
- [Rebuild Tree](https://docs.frappe.io/erpnext/rebuild-tree)
- [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions)
- [Accounts Settings](https://docs.frappe.io/erpnext/accounts-settings)

<!-- page: erpnext/erpnext__changing-the-properties-of-a-field-based-on-role.md -->
---
title: "Field Level Permission Management"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/changing-the-properties-of-a-field-based-on-role"
updated: "2026-03-02"
---

Restricting a field based on Roles can be easily configured using Perm Level, which is required by most organizations. To define a **Perm Level**, you can go to the respective form and Customize it.

Let's take a scenario where the organization doesn't want its Employee (Accounts User) to edit the Rate of the item while creating a **Sales** **Invoice**. To do that, we can simply make the **Item Rate** field a read-only.



#### Step 1: Customize Form

To achieve this, go to **Customize Form**, select DocType as **Sales Invoice** **Item**, scroll to the **Item Rate** field and expand it.

![](/files/6eFVMRc.gif)

#### Step 2: Perm Level

Search for the **Perm Level**, enter the number (0, 1, 2, 3, etc), and Save it.

![](/files/6VNnxII.png)

#### Step 3: Permission Rule

Once saved, click on **Add a New Rule** in Role Permission Manager and select the Document Type and the Role, in our case, Accounts User, set the Perm Level as 2 and grant the Employee Read access.

![](/files/jACnHrX.png)

This is how the Role Permissions Manager will display the newly created Rule with Perm Level as 2:

![](/files/qCYWDfK.png)

#### Step 4: Validate View

Now, as you can see in the Sales Invoice the User can only read the Item Rate field which will be fetched automatically from the Price List.

![](/files/86CqBf1.png)

<!-- page: erpnext/erpnext__chart-of-accounts-importer.md -->
---
title: "Chart Of Accounts Importer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/chart-of-accounts-importer"
updated: "2026-02-27"
---

> Introduced in Version 12

When a new company is created in ERPNext, the Chart of Accounts for it is created by default with a pre-set structure. However, if you have your own Chart of Accounts, you can import it using the Chart of Accounts Importer.

It allows you to create your own Chart of Accounts according to your requirement and import it into the system.

Any existing Chart Of Accounts against that company will be overwritten. Make sure the company you are selecting doesn't have any pre-existing transactions otherwise you'll receive a validation error.

To access, go to:

> Home > Getting Started > Chart of Accounts Importer

## 1. How to import Chart Of Accounts

1. Select the Company for which you want to import the Chart of Accounts.
2. Click on "Download Template" button to download the template. Select file type in which you want to download the template. Select the template type and click on "Download". "Sample Template" contains pre-filled sample data so that you get an idea of how to fill the template. You can edit the data in "Sample Template" itself or download "Blank Template" for a fresh template.
  [COA Import](/files/coa-template-download.png)

![COA Import](/files/coa-blank-template.png)

1. Once you download the template, fill in the details in the template as shown in the sample template below. Please make sure to make accounts for account types "Cost of Goods Sold", "Depreciation", "Fixed Asset", "Payable", "Receivable", "Stock Adjustment". Root types for these accounts must be one of Asset, Liability, Income, Expense, and Equity.
  o know more about "Account Types" and "Root Types" click here [click here](/erpnext/chart-of-accounts)

![COA Import](/files/coa-sample-template.png)

Click on "Attach" to upload the template.

[COA Import](/files/coa-attach.png)



Once you upload the template you'll be able to see the preview of the Chart of Accounts in the Chart Preview section.

[COA Import](/files/coa-preview.png)



If everything seems correct in the preview, click on "Import" in the top right corner and the accounts will be created.

[COA Import](/files/coa-start-import.png)



To verify the created accounts you can go to Chart of Accounts and see the newly created accounts for that company.

[COA Import](/files/coa-import.png)

<!-- page: erpnext/erpnext__chart-of-accounts.md -->
---
title: "Chart of Accounts | ERPNext Documentation"
description: "Structure, create, maintain, and verify ledger and group accounts in the ERPNext Chart of Accounts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/chart-of-accounts"
updated: "2026-08-14"
---

The Chart of Accounts forms the *blueprint* of your organization. The overall structure of your Chart of Accounts is based on a system of double entry accounting that has become a standard all over the world to quantify how a company is doing financially.



It groups assets, liabilities, income, expenses, and equity so that a transaction posted today appears in the right place on tomorrow’s financial statements.



When Nova Industries sells a laptop, the system may increase Accounts Receivable, record Sales income, reduce Stock, and recognize Cost of Goods Sold. Those four postings make sense only because each account has the correct parent, root type, currency, and purpose.



A useful chart is detailed enough to answer management questions but not so fragmented that the team cannot reconcile it. This page explains the tree, account types, ledger accounts, safe structural changes, and the choices to make before importing or creating accounts.

## Understand the account tree

Open **Home &gt; Accounting &gt; Accounting Masters &gt; Chart of Accounts** and select the company.

![Chart of Accounts tree](/files/chart-of-accounts-tree773763.webp)

Group accounts organize the tree and cannot receive General Ledger entries. Ledger accounts are the final nodes used in transactions.


| Root type | What it represents                     |
| --------- | -------------------------------------- |
| Asset     | Resources the company controls         |
| Liability | Amounts the company owes               |
| Equity    | Owners’ interest and retained earnings |
| Income    | Revenue and other income               |
| Expense   | Costs incurred by the company          |


## Add an account

1. Select the parent group.
2. Click **Add Child**.
3. Enter the account name and number, if numbering is used.
4. Enable **Is Group** only when the account will contain child accounts.
5. Select an **Account Type** when the account has a specific purpose, such as Bank, Cash, Receivable, Payable, Tax, Stock, or Fixed Asset.
6. Save.

Use account types consistently. ERPNext uses them to filter account fields and determine transaction behavior.

## Plan the structure

Keep the tree detailed enough for reporting but simple enough to use reliably. Prefer Cost Centers, Projects, and [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions) when you need to analyze the same account by department, branch, product line, or initiative.

Do not create a separate receivable or payable ledger for every Customer or Supplier. ERPNext maintains party-wise balances within the designated control accounts.

## Edit or disable an account

You can rename or move an account when there are no conflicting restrictions. Disable an unused account instead of deleting it when it has transaction history. Never convert a ledger into a group, or a group into a ledger, without reviewing its children and postings.

## Importing or migrating a Chart of Accounts

Finalize the structure before importing opening balances. Map accounts from the previous system, create required control accounts, and test financial statements. Avoid importing old transaction-level detail unless it is required for statutory, operational, or audit reasons.

## Verify the Chart of Accounts

Create draft Sales Invoice, Purchase Invoice, Payment Entry, and Journal Entry records. Confirm that account filters show the intended ledgers. Then review the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), Balance Sheet, and Profit and Loss Statement after a controlled test posting.

## Troubleshooting

**An account is missing from a transaction**

Confirm its company, account type, root type, disabled status, and whether it is a group.

**An account cannot be deleted**

It may have child accounts, defaults, or transaction history. Disable it after replacing any defaults.

## Related topics

- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)
- [Cost Center](https://docs.frappe.io/erpnext/cost-center)
- [Opening Balance](https://docs.frappe.io/erpnext/opening-balance)
- [Chart of Accounts Importer](https://docs.frappe.io/erpnext/chart-of-accounts-importer)

<!-- page: erpnext/erpnext__check-link-between-documents.md -->
---
title: "Checking Link Between Documents"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/check-link-between-documents"
updated: "2026-03-04"
---

Every document can be linked to various other documents in ERPNext.

**The 'Links' tool gives you an option to check if the current document is linked to any previous documents and lists down all the forward links.**

To do so, you can simply go to the menu and click on 'Links'. A Pop-Up box will open which will list down all the documents that this document has been linked to.

![Checking Document Links](/files/using-document-links-1.gif)  



> Note: This option will only show you the forward links in a document; the backward links can be found within the document itself.
> 
> 


> **E.g.**, if you want to check, which Sales Invoices are linked to your Sales Order, you can check the 'Links' from the dropdown menu. However, the information about the Quotation with which this Sales Order has been linked shall be present within the Document itself.
> 
> 

<!-- page: erpnext/erpnext__cheque-print-template.md -->
---
title: "Cheque Print Template"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/cheque-print-template"
updated: "2026-03-02"
---

**Cheque Print Template allows defining templates for bank cheques.**

Business involves making payment to various parties like suppliers and employees. Payment can be made in various modes like cash, NEFT or cheque. If you are making a payment via a cheque, you can also create a Print Format for printing Cheques from ERPNext based on the Payment Entry.

To access Cheque Print Template, go to: > Home > Accounting > Cheque Print Template

Using the Cheque Print Template you can generate a new Print Format for cheques. It will be created based on the cheque format provided by your bank.

A sample cheque:

![Sample Cheque](/files/sample-cheque.jpg)  


1. How to create a Cheque Print Template
----------------------------------------

1. Go to the Cheque Print Template list, click on New.
2. You can set the position of various items in the cheque.
3. Save.

In the Cheque Print Template, for each value (say Payee, Date), exact coordinates are provided based on where that value should be printed on a cheque. Co-ordinates are provided in centimeters. Here is a representation the structure:

![Sample Cheque](/files/cheque-1.png)  


### 1.1 New Format by Scanning

To speed up the creation of a new cheque printing format, you can upload a scanned image of the cheque. Considering the scanned image for the cheque, the system automatically updates co-ordinates for each value like party name, amount, date, the amount in words, etc.

### 1.2 New Print Format manually

If the preview looks good, click on the **Create Print Format** button to create a new Print Format for printing the cheque. Based on the values provided in the Cheque Print Template, the system will auto-generate an HTML script for the cheque’s Print Format.

You can manually provide the co-ordinate for each value based on where you want it to be printed on the cheque and customize with HTML/CSS.

#### Preview

Based on coordinates provided for all the values, a preview will be shown as to how the values will be printed on the cheque.

![Sample Cheque](/files/cheque-2.png)  


### 1.3 Printing Cheques

New print format generated for the cheque will be visible in the Payment Entry form. After creating the payment entry, you will be able to print transaction details on the cheque.

![Sample Cheque](/files/cheque-3.gif)  


### 2. Related Topics

1. [Address Template](/erpnext/address-template)
2. [Terms and Conditions Template](/erpnext/terms-and-conditions)

<!-- page: erpnext/erpnext__client-scripts.md -->
---
title: "Client Scripts"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/client-scripts"
updated: "2026-03-02"
---

**Client Scripts are small code snippets that are executed in the browser to extend or customize the standard functionality of ERPNext.**


> Build > Scripting > Client Script
> 
> 

![Client Script](/files/customize-erpnext-client-scripts.png)  


1. How to Create a Custom Script
--------------------------------

Create a Custom Script (you must have System Manager role for this):

1. Go to Custom Script List and click on New.
2. You will be redirected to a page wherein you will be asked to enter the DocType for which you wish to create a Custom Script.
3. Type your Custom Script and make sure it is enabled.
4. Save.

2. Notes
--------

* Server Custom Scripts are only available for the Administrator.
* Client Custom Scripts are in JavaScript and Server Custom Scripts are in Python.
* For testing, make sure to go to Tools > Clear Cache and refresh after updating a Custom Script.

<!-- page: erpnext/erpnext__close-sales-order.md -->
---
title: "Close Sales Order | ERPNext Documentation"
description: "Learn how to close an ERPNext Sales Order, stop outstanding delivery or billing, understand its effects, and reopen the order when required."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/close-sales-order"
updated: "2026-07-24"
---

A submitted [Sales Order](/erpnext/sales-order) can be closed when the customer no longer wants the remaining quantity delivered or billed. Closing preserves the order and its completed transactions while removing the outstanding balance from active fulfilment.

## Before you begin

Confirm that:

- The Sales Order is submitted.
- Any accepted quantity has already been delivered through a [Delivery Note](/erpnext/delivery-note) or billed through a [Sales Invoice](/erpnext/sales-invoice).
- The customer has agreed that the remaining quantity will not be fulfilled.
- You do not need to correct the original order. Use [Cancel and Amend](/erpnext/amending-sales-order-after-submit) when the submitted details themselves are wrong.

> Closing is not the same as cancelling. Closing ends only the outstanding fulfilment. Existing deliveries, invoices, payments, and the audit trail remain intact.

## Close a Sales Order

1. Open the submitted Sales Order.
2. Check the **% Delivered** and **% Amount Billed** values so you know what remains outstanding.
3. Select **Status**, then select **Close**, as highlighted.

![Close a submitted Sales Order from the Status menu](https://novacompanies.m.frappe.cloud/files/status-close-menu.png)

ERPNext changes the order status to **Closed**. You cannot create new Delivery Notes or Sales Invoices against its remaining quantity while it is closed.

![A closed Sales Order](https://novacompanies.m.frappe.cloud/files/closed-status.png)

## What closing changes

After closing the order:

- The undelivered quantity no longer appears as pending in fulfilment reports.
- The unbilled amount no longer appears as pending in billing reports.
- Completed [Delivery Notes](/erpnext/delivery-note), [Sales Invoices](/erpnext/sales-invoice), and [Payment Entries](/erpnext/payment-entry) remain linked to the order.
- The order remains available for reporting and audit history.
- ERPNext blocks new downstream transactions for the closed balance.

For example, if a customer orders 10 laptops, accepts delivery and billing for 7, and cancels the remaining 3, complete the documents for 7 first and then close the Sales Order. The three-unit balance will no longer remain open.

## Reopen a closed Sales Order

If the customer later asks you to fulfil the balance:

1. Open the closed Sales Order.
2. Select **Status**.
3. Select **Re-open**.
4. Create the required Delivery Note or Sales Invoice for the remaining quantity.

The available action can depend on your permissions and the current document state. Ask an administrator to check [Role-Based Permissions](/erpnext/role-based-permissions) if you cannot see it.

## When to use another action


| Situation                                                                         | Recommended action                                                                            |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| The customer no longer wants only the outstanding balance                         | Close the Sales Order                                                                         |
| The submitted order contains an incorrect customer, item, quantity, rate, or date | [Cancel and Amend](/erpnext/amending-sales-order-after-submit)                                |
| Several open orders need to be closed together                                    | [Short Close Multiple Orders](/erpnext/short-close-multiple-orders)                           |
| You need to deliver or invoice only part of the order now                         | Use [Partial Fulfilment](/erpnext/partial-fulfilment-of-sales-order) and leave the order open |
| Goods already delivered are being returned                                        | Create a [Sales Return](/erpnext/sales-return)                                                |
| The order should pause temporarily without ending the balance                     | Put the order on hold                                                                         |


## Frequently asked questions

### Does closing delete the Sales Order?

No. The document and all linked transactions remain available.

### Can I close a partly delivered or partly billed order?

Yes. Complete the documents the customer accepts, then close the remaining balance.

### Can I create another Delivery Note after closing?

Not until you reopen the Sales Order.

### Does closing create a credit note or refund?

No. Closing affects only the outstanding order balance. Use a return or credit note when you need to reverse delivered or invoiced quantities.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Partial Fulfilment of Sales Order](/erpnext/partial-fulfilment-of-sales-order)
- [Sales Order Statuses](/erpnext/sales-order#statuses)

<!-- page: erpnext/erpnext__closing-accounting-books-in-erpnext.md -->
---
title: "Closing Accounting Books in ERPNext in v15"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/closing-accounting-books-in-erpnext"
updated: "2026-08-14"
---

Closing the books is not one button. It is a controlled review that turns a year of operational documents into reliable financial statements. For Nova Industries, that means confirming what customers owe, what the company owes suppliers, whether bank and stock balances agree, whether depreciation and taxes are complete, and only then transferring the year’s profit or loss.

## Year-end sequence

1. Stop routine backdated changes and communicate the close timetable.
2. Review unbilled orders, receivables, payables, advances, credit notes, and debit notes.
3. Reconcile bank accounts with [Bank Reconciliation](/erpnext/bank-reconciliation) and allocate standalone payments with [Payment Reconciliation](/erpnext/payment-reconciliation).
4. Reconcile physical stock, stock valuation, fixed assets, depreciation, loans, payroll, taxes, and deferred balances.
5. Post approved accruals, provisions, write-offs, exchange adjustments, and audit corrections.
6. Validate Trial Balance, General Ledger, Balance Sheet, Profit and Loss, and Cash Flow.
7. Submit the [Period Closing Voucher](/erpnext/period-closing-voucher).
8. Protect the finished dates with an Accounting Period or frozen-accounts date.
9. Confirm the new Fiscal Year and defaults before routine posting resumes.

![Period-end ledger entries after closing](https://novacompanies.m.frappe.cloud/files/accounting-entries-20260802-accounting-entries-period-closing.png)



## What each control does


| Control                | Purpose                                                           | What it does not do                                   |
| ---------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| Period Closing Voucher | Transfers net income or loss to equity.                           | Does not lock later entries.                          |
| Accounting Period      | Blocks selected document types in a finished range.               | Does not transfer profit or loss.                     |
| Accounts Frozen Upto   | Applies a broad posting cut-off with a controlled role exception. | Does not replace reconciliation or closing entries.   |
| Fiscal Year            | Defines valid accounting dates and report periods.                | Does not by itself prove that the books are complete. |


![Fiscal Year dates used for the new accounting year](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-fiscal-year-dates.png)



## Troubleshooting

### Reports changed after the close

Find transactions posted or cancelled after the review date, compare the latest General Ledger with the approved export, post any required correction, submit another Period Closing Voucher for residual Profit and Loss balances, and then apply the appropriate lock.

### The Balance Sheet does not balance

Check incomplete opening balances, temporary opening account balances, cancelled or reposted entries, currency differences, and report filters before closing. Do not use the closing voucher to conceal an unexplained imbalance.

## Frequently asked questions

### Do unpaid invoices carry into the next year?

Receivables and payables are Balance Sheet balances and continue until settled, written off, or otherwise adjusted.

### Do I create opening entries every year?

Opening entries are normally a migration or first-setup activity. Ongoing Balance Sheet balances carry forward through the ledger.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__closing-stock-balance.md -->
---
title: "Closing Stock Balance"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/closing-stock-balance"
updated: "2026-03-02"
---

Note: In v16 the closing stock balance has renamed as [Stock Closing Entry](/erpnext/stock-closing-entry)

#### How the Stock Balance Report is Prepared

The Stock Balance report is a crucial tool for businesses to monitor their inventory levels and make informed decisions. It consists of four main columns: Opening Stock, In Stock, Out Stock, and Balance Stock. The Balance Stock is calculated using the formula Opening Stock + In Stock - Out Stock.

One of the key challenges in preparing the Stock Balance report is the calculation of the Opening Stock. To determine the Opening Stock, the system reads all the rows in the Stock Ledger Entry table that come before the specified From Date filter. However, a potential issue arises when the filter for item code or warehouse is not set, and the Stock Ledger Entry table contains a vast number of records. This situation can significantly slow down the process and cause performance problems.

#### Closing Stock Balance

![](/files/QqWv6uJ.png)

To address this issue, a solution has been introduced - the "Closing Stock Balance" feature. This feature allows the system to prepare the Opening Stock in advance, reducing the time taken to generate the Stock Balance report.

Here's how to use the "Closing Stock Balance" feature effectively:

1. Closing Stock Balance Creation: After the financial year has ended, and the necessary audits have been completed for that year (in this example, the financial year 2022-2023), you should create the Closing Stock Balance. This should be done for the specific end date of the financial year 2022-2023.
2. Data Preparation: Once the Closing Stock Balance is submitted, the system will take some time to prepare the data. During this process, the Opening Stock values are calculated and stored for future use.
3. Utilizing Closing Stock Balance: With the Closing Stock data prepared, the system will utilize this data to generate the Stock Balance report efficiently. Now, whenever a user opens the Stock Balance Report, the system can quickly read the necessary data from the Closing Stock Balance for the Opening Stock values.
4. Annual Closing Stock Balance: It is essential to create the closing stock balance every year after the closing of the financial year. This ensures that the Opening Stock values are updated and accurate for each reporting period.

By implementing the "Closing Stock Balance" feature and following the recommended steps, businesses can significantly improve the performance and efficiency of generating Stock Balance reports, even with a vast amount of data in the Stock Ledger Entry table. 
