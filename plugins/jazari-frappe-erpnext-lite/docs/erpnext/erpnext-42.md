<!-- Frappe documentation: erpnext, part 42 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__period-closing-voucher.md -->
---
title: "Period Closing Voucher\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/period-closing-voucher"
updated: "2026-08-14"
---

At year end, Nova Industries has finished invoicing, posted depreciation and accruals, reconciled its bank accounts, and reviewed receivables and payables. Its income and expense accounts still contain the year’s activity. A Period Closing Voucher transfers their net balance to an equity account so the next period starts with fresh Profit and Loss balances while Balance Sheet balances continue.



The voucher does not erase history or stop backdated entries. It creates balanced General Ledger entries. Use an [Accounting Period](/erpnext/accounting-period) or [Accounts Frozen Upto](/erpnext/freeze-accounting-entries) when the closed period must also be protected from later changes.

## Before you begin

- Complete bank, payment, stock, tax, depreciation, deferred accounting, accrual, and correction entries.
- Review the [Profit and Loss Statement](/erpnext/profit-and-loss-report), [Balance Sheet](/erpnext/balance-sheet), Trial Balance, Accounts Receivable, and Accounts Payable.
- Confirm the closing account with your accountant. It is commonly a Retained Earnings, Reserves and Surplus, or owner’s equity account.
- Take a backup and close only after the period’s adjustments are approved.

## Create a Period Closing Voucher

1. Open **Period Closing Voucher** and click **Add Period Closing Voucher**.
2. Select the company and the fiscal year being closed.
3. Set the posting date to the last day of the period.
4. Select the closing account that will receive the net profit or loss.
5. Enable **Book Cost Center Wise Profit/Loss** when retained earnings must preserve the cost center split.
6. Add a clear remark, save, review, and submit.

[Screenshot on the live page: Period Closing Voucher with the fiscal year and closing account highlighted]



## What submission posts


| Result for the period | Debit                                      | Credit                                     |
| --------------------- | ------------------------------------------ | ------------------------------------------ |
| Net profit            | Net balance of income and expense accounts | Closing equity account                     |
| Net loss              | Closing equity account                     | Net balance of income and expense accounts |


The entries reduce the period’s income and expense balances to zero and move the difference to equity. They do not close receivable, payable, bank, stock, asset, liability, or other Balance Sheet accounts.

[Screenshot on the live page: General Ledger showing the accounting effect of period closing]



## If entries are posted after closing

ERPNext does not silently rewrite the submitted voucher. Complete the new approved adjustments and submit another Period Closing Voucher for the same fiscal year. The later voucher transfers only the remaining Profit and Loss balance.



Do not create a new opening entry every year. Opening entries are for migration or first-time setup. The previous year’s Balance Sheet balances carry forward through the ledger.

## Troubleshooting

### The closing balance is not what you expected

Run Profit and Loss with the same company, dates, Finance Book, and dimensions. Check draft or missing adjustments, unusual income and expense accounts, and entries posted after the earlier closing voucher.

### The voucher takes too long

Review the [Period Closing Voucher controller](/erpnext/legacy-controller-for-period-closing-voucher). Large ledgers can use batched background processing instead of one large database transaction.

## Frequently asked questions

### Does a Period Closing Voucher lock the year?

It transfers Profit and Loss balances. Use Accounting Period or the frozen-accounts date to restrict later postings.

### Can I close monthly or quarterly?

You can, but confirm the policy with your accountant. Year-end closing is the most common use, and extra vouchers add audit activity.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__periodic-inventory.md -->
---
title: "Periodic Inventory"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/periodic-inventory"
updated: "2026-02-20"
---

If you enable Perpetual Inventory in the Company master, the system will automatically create the GL entries for stock transactions. However, if Perpetual Inventory is disabled for your company, you will need to manually create periodic accounting entries.

To make a periodic accounting entry, you must create a Journal Entry manually. For the calculations, you need to compare the closing balance in the Stock Balance Report with the Trial Balance report for stock asset accounts. This process takes time, as it requires verifying and matching the differences in closing balances.

To address this in Version 16, we introduced a new Journal Entry type called 'Periodic Accounting Entry'. With this, users don’t need to perform manual calculations. The system will automatically fetch the difference in balance when the user clicks the 'Get Balance' button.



[Screenshot on the live page]

<!-- page: erpnext/erpnext__perm-level-error-in-permission-manager.md -->
---
title: "Perm Level Error"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/perm-level-error-in-permission-manager"
updated: "2026-03-04"
---


While customizing rules in the [Permission Manager](/erpnext/role-based-permissions), you might receive an error message saying:

> For System Manager _(or any other role)_ at level 2 _(or another level)_ in Customer _(or any other document)_ in row 8: Permission at level 0 must be set before higher levels are set.

Error message indicates problem is in the existing permission setting for this document.

For any role, before assigning permission at Perm Level 1 or 2 (and so on), permission at Perm Level 0 must be assigned. Error message says that System Manager has been assigned permission at Perm Level 1 and 2, but not at level 0. You should first correct the permission for System Manager's role by:

- Assigning permission to System Manager at level 0.

 Or

- By removing permission at level 1 and 2.

After executing one of the above steps, you should be able to successfully add new permissions rules in the Role Permission Manager.

<!-- page: erpnext/erpnext__perm-levels.md -->
---
title: "Perm Levels"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/perm-levels"
updated: "2026-07-04"
---

Perm Level, short for Permission Level, is a field-level permission system in ERPNext and Frappe. It lets administrators control access to sensitive fields within a DocType without hiding or restricting the entire document.

## What Perm Levels Control

Every field in a DocType has a **Perm Level**. By default, fields are at perm level **0**. Fields at level 0 are controlled by the normal permissions for the DocType.

When a field is assigned a higher perm level, such as **1** or **2**, users need a matching permission row for that level in Role Permission Manager. Without that matching permission, the user may still be able to open the document, but the higher-level field can be hidden or read-only depending on the configured permissions.

## Why Perm Levels Are Useful

Perm levels are useful when most users should work with a document, but only some users should see or edit sensitive information. This avoids creating separate DocTypes or custom workflows just to protect a few fields.

- **Sales:** A sales user may create a quotation, while only a manager can edit the discount approval field.
- **HR:** An HR user may view an Employee record, while salary details are available only to payroll roles.
- **Accounts:** A user may view a supplier invoice, while bank or tax-related fields are restricted to accounts managers.
- **Support:** A support user may update ticket details, while internal escalation notes are visible only to senior users.

## How Perm Levels Work

1. A field is assigned a perm level in the DocType or Customize Form.
2. Role Permission Manager is used to define what each role can do at each perm level.
3. When a user opens a document, ERPNext checks both the user's roles and the permission level of each field.
4. If the user has permission for the field's perm level, the field is available according to the allowed actions, such as read or write.
5. If the user does not have permission for that perm level, the field is restricted even if the user can access the document itself.

## Example

Suppose a Sales Order has these fields:

- **Customer** at perm level 0
- **Items** at perm level 0
- **Delivery Date** at perm level 0
- **Approved Discount** at perm level 1
- **Management Remarks** at perm level 2

A Sales User with permission only at level 0 can work with the regular sales order fields. A Sales Manager with level 1 permission can also read or update the Approved Discount field. A Sales Director with level 2 permission can access Management Remarks as well.

## Perm Levels And Role Permission Manager

Perm levels become useful only when they are paired with role permissions. In Role Permission Manager, each permission row has a **Level** value. That value must match the field's perm level.

For example, if a field is set to perm level 1, a role needs a permission row for level 1 on that DocType. The row can then allow actions such as read, write, create, submit, cancel, or amend depending on the DocType and business requirement.

## Good Practices

- Keep most fields at perm level 0.
- Use higher perm levels only for fields that genuinely need extra control.
- Use clear field labels so restricted fields are easy to identify during configuration.
- Test permissions with a non-administrator user before relying on the setup.
- Avoid creating too many levels, because permission rules can become hard to audit.
- Document why each restricted field was assigned a higher perm level.

## Common Mistakes

- **Setting a field to level 1 but not adding level 1 role permissions:** Users may lose access to the field unexpectedly.
- **Assuming document access means field access:** A user can have access to the document but still not have access to higher-level fields.
- **Using perm levels instead of workflow approvals:** Perm levels control field access. They do not replace approval workflows where business process control is required.
- **Testing only as Administrator:** Administrator access can hide permission problems. Always test with the target role.

## Related Topics

- [Users And Permissions](https://docs.frappe.io/erpnext/user/manual/en/setting-up/users-and-permissions)
- [Role Permissions Manager](https://docs.frappe.io/erpnext/user/manual/en/role-permissions-manager)
- [DocType Permissions](https://docs.frappe.io/framework/user/en/basics/doctypes/permissions)
- [Customize Form](https://docs.frappe.io/erpnext/customize-form)

<!-- page: erpnext/erpnext__permissions.md -->
---
title: "Role Based Permissions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/permissions"
updated: "2026-02-28"
---

**Permission to different documents can be controlled using Role Based Permissions.**

ERPNext has a role-based permission system. It means that you can assign Roles to Users, and Permissions can be set on Roles. The Role Permissions Manager allows you to set which roles can access which documents and with what permissions (read, write, submit, etc.).

Once roles are assigned to a user, their access can be limited to specific documents. The permission structure allows you to define different permission rules for different fields using a concept called **Permission Level** of a field.

1. How to use the Role Permissions Manager

---

To start using the Role Permission Manager, go to: > Home > Users and Permissions > Role Permissions Manager

[Screenshot on the live page: Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager]



Permissions are applied on a combination of:

- **Roles:** As we saw earlier, Users are assigned Roles and it is on these Roles that permission rules are applied. For example, a sales user may be given the roles of an Employee and a Sales User.

Examples of Roles include Accounts Manager, Employee, HR User, etc.

- **Document Types:** Each type of document, master or transaction, has a separate list of role-based permissions as seen in the preceding screenshot.

Examples of Document Types are Sales Invoice, Leave Application, Stock Entry, etc.

- **Permission Levels:** In each document, you can group fields by "levels". Each group of fields is denoted by a unique number (0 to 9). A separate set of permission rules can be applied to each field group. By default, all fields are of level 0.

Permission "Level" connects fields with level X to a permission rule with level X. To know more click [here](/erpnext/changing-the-properties-of-a-field-based-on-role).

- **Document Stages:** Permissions are applied on each stage of the document like Creation, Saving, Submission, Cancellation, and Amendment. A role can be permitted to Print, Email, Import or Export data, access Reports, or define User Permissions.
- **User Permissions:** Using User Permissions in ERPNext a user can be restricted to access only specific Documents for that Document Type. Eg: Only one Territory from all Territories. User Permissions defined for other Document Types also get applied if they are related to the current Document Type through Link Fields.

For example, a Customer is a link field in a Sales Order or Quotation. In the Role Permissions Manager, User Permissions can be set using the 'Set User Permissions' button.

To set User Permissions based on documents/fields go to: > Home > Users and Permissions > Permissions > [User Permissions](/erpnext/user-permissions)

- **Add a New Rule**: In the Role Permissions Manager, to add a new rule, click on the **Add a New Rule** button and a pop-up box will ask you to select a Role and a Permission Level. Once you select this and click on 'Add', this will add a new row to your rules table.

2. How Role Based Permissions Work

---

Leave Application is a good example that encompasses all areas of a Permission System.

- It should be created by an Employee. For this, Employee Role should be given Read, Write, Create permissions.

[Screenshot on the live page: Giving Read, Write and Create Permissions to Employee for Leave Application]
* An *

*Employee** should only be able to access his/her Leave Application. Hence, User Permissions record should be created for each User-Employee combination.

[Screenshot on the live page: Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager]
* If you want an *

*Employee** to only select a document in another document and not have read access to that document as a whole, then grant only Select perm to the role, Employee.

[Screenshot on the live page: Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager]
* *

*HR Manager** should be able to see all Leave Applications. Create a Permission Rule for HR Manager at Level 0, with Read permissions. Apply User Permissions should be disabled.

[Screenshot on the live page: Giving Submit and Cancel permissions to HR Manager for Leave Applications. 'Apply User Permissions' is unchecked to give full access.]
* *

*Leave Approver** should be able to see and update Leave Applications of employees under him/her. Leave Approver is given Read and Write access at Level 0. Relevant Employee Documents should be enlisted in the User Permissions of Leave Approvers. (This effort is reduced for Leave Approvers mentioned in Employee Documents, by programmatically creating User Permission records).

[Screenshot on the live page: Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.'Apply User Permissions' is checked to limit access based on Employee.]
* It should be Approved/Rejected only by HR User or Leave Approver. The Status field of a Leave Application is set at Level 1. HR User and Leave Approver are given Read and Write permissions for Level 0, while everyone else (All) are given Read permission for Level 1.

[Screenshot on the live page: Limiting read access for a set of fields to certain Roles]
*

 **HR User** should be able to delegate Leave Applications to his/her subordinates. HR User is given the right to Set User Permissions. A User with HR User role would be able to define User Permissions on Leave Application for other users.

[Screenshot on the live page: Let HR User delegate access to Leave Applications by checking 'Set User Permissions'. This will allow HR User to access User Permissions Manager for 'Leave Application']

In case you have correctly assigned the roles but still you're getting errors when accessing documents, refer [this page](/erpnext/report-permission-error).

### 3. Permission Type

In the Role Permission Manager, multiple permissions can be enabled for each Role. Below are the details of the available permission options and their usage.

[Screenshot on the live page: Screenshot 2025 12 19 at 5.15.56 PM]


| Permission | Description                                                   | Example                                                                                         |
| ---------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Select     | Allows the user to search and see records.                    | The user can select a Customer in Sales Order but cannot open the Customer master.              |
| Read       | Allows the user to view the document.                         | The user can view Sales Invoices but cannot change them.                                        |
| Write      | Allows the user to edit existing records they have access to. | The user can update a Customer address but cannot create a new Customer.                        |
| Create     | Allows the user to create new documents.                      | The user can create a new Item but cannot edit existing items.                                  |
| Delete     | Allows the user to delete documents.                          | The user can delete submitted documents.                                                        |
| Print      | Allows printing or PDF download of documents.                 | The print button is enabled for the user in the document.                                       |
| Email      | Allows the user to email from the document.                   | The email button is enabled for the user in the document.                                       |
| Report     | Allows the user to access reports related to the document.    | If the user has access to Employee and Report is enabled, they can view Employee-based reports. |
| Export     | Allows the user to export data from the Report view.          | The user can export report data.                                                                |
| Import     | Allows the user to import data into the document.             | The user can import data for the document.                                                      |
| Share      | Allows sharing document access with other users.              | The user can share document access with another user.                                           |



|                     |                                                                                                                                                                                                 |                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
|                     |                                                                                                                                                                                                 |                                                                                                              |
| Mask (Data Masking) | In ERPNext Version 16, Data Masking allows configuration of specific fields to display masked or hidden values based on the user's roles and permissions, without restricting field visibility. | Ensures sensitive information remains protected while keeping the user interface consistent and informative. |

<!-- page: erpnext/erpnext__perpetual-inventory-for-non-stock-item.md -->
---
title: "Perpetual Inventory for Non-stock Item"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/perpetual-inventory-for-non-stock-item"
updated: "2026-03-02"
---

  

**Question:**   

We have enabled Perpetual Inventory in the Company master. Still, in some Purchase Invoice, posting if done in the Expense Account.
  

**Answer:**
As per the perpetual inventory, when item is a stock item, then only it's value is booked under Stock-in-hand at the time of Purchase. In this case, the posting in the GL Entry for Purchase Invoice will be as follows.

|  |  |  |
| --- | --- | --- |
| **Account** | **Debit** | **Credit** |
| Creditors |  | 100 |
| Stock Received but not Billed | 90 |  |
| Tax | 10 |  |
|  |  |  |

Perpetual Inventory doesn't apply on the non-stock item, and expense is booked for them as soon as Purchase Invoice is submitted. The posting in General Ledger for in this scenario will look like:

|  |  |  |
| --- | --- | --- |
| **Account** | **Debit** | **Credit** |
| Creditors |  | 100 |
| COGS / Other Expense Account | 90 |  |
| Tax | 10 |  |
|  |  |  |

<!-- page: erpnext/erpnext__perpetual-inventory.md -->
---
title: "Perpetual Inventory\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/perpetual-inventory"
updated: "2026-02-27"
---

As per the perpetual inventory system, accounting entry is done for every stock transaction. Otherwise, it's done in larger intervals for example monthly or quarterly. Each warehouse is linked with a corresponding account head.

On receipt of items in a particular warehouse, the balance in the Warehouse Account will increase. Similarly, when items are delivered from the Warehouse, an expense will be booked, and the balance in the Warehouse Account will reduce.

:::note
In a new ERPNext site, Perpetual Accounting is enabled by default.
:::



### 1. Activate perpetual inventory

1. Go to:
  *Home > Accounting > Company > Enable Perpetual Inventory**
  Perpetual Inventory (picture on the live page)  
  Note that if you disable perpetual inventory, users will have to create manual entry to update actual stock balance in the Stock in hand account (or ledger).
2. Set up the following default accounts for each Company if not set. These accounts are created automatically in the new ERPNext accounts.
  Default Inventory Account (Asset)  
   Stock Received But Not Billed (Liability)  
   Stock Adjustment Account (Expense)  
   Expenses Included In Valuation (Expense)  
   Cost Center
3. If the user wants to set an individual account for each warehouse, create account head for each account. Go to:
  *Accounts > Chart of Accounts > Company > Application of Funds (Assets) > Current Asset > Stock Assets > Create a new account with same name as Warehouse**
  Now, go to a warehouse and link this account to the warehouse. This helps in filtering and viewing statements warehouse-wise.
4. For stock transactions, general ledger entries made against the Account Head set on the warehouse, if the user had not set the account for the warehouse then the system gets the account head from the parent warehouse. If Account was not set for parent warehouse then the system gets the account(Default Inventory Account) from the company master.

---

### 2. Example

Consider the following Chart of Accounts and Warehouse setup for your company:

Chart of Accounts:

- **Assets (Dr)**
  - Current Assets
    - Accounts Receivable
      - Debtors
  - Stock Assets
    - Stores
    - Finished Goods
    - Work In Progress
  - Tax Assets
    - VAT
- **Liabilities (Cr)**
  - Current Liabilities
    - Accounts Payable
      - Creditors
  - Stock Liabilities
    - Stock Received But Not Billed
  - Tax Liabilities
  - Service Tax
    - Income (Cr)
- Direct Income
  - Sales Account
- Expenses (Dr)
  - Direct Expenses
    - Stock Expenses
    - Cost of Goods Sold
    - Expenses Included In Valuation
    - Stock Adjustment
- Indirect Expenses
  - Shipping Charges
  - Customs Duty

#### 2.1 Warehouse - Account Configuration

- Stores
- Work In Progress
- Finished Goods

#### 2.2 Purchase Receipt

Suppose you have purchased 10 nos of item "RM0001" at $200 from supplier "Arcu Vel Quam Fabricators". Following are the details of Purchase Receipt:

**Supplier:** Arcu Vel Quam Fabricators

**Items:**




| Item   | Warehouse | Qty | Rate | Amount | Valuation Amount |
| ------ | --------- | --- | ---- | ------ | ---------------- |
| RM0001 | Stores    | 10  | 200  | 2000   | 2250             |


**Taxes:**


| Account          | Amount | Category            |
| ---------------- | ------ | ------------------- |
| Shipping Charges | 100    | Total and Valuation |
| VAT (10%)        | 200    | Total               |
| Customs Duty     | 150    | Valuation           |




**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

As stock balance increases through Purchase Receipt, "Store" accounts are debited and a temporary account "Stock Receipt But Not Billed" account is credited, to maintain double-entry accounting system. At the same time, the negative expense is booked in account head having category as "Valuation" or "Total and Valuation" in taxes and charges table for the amount added for valuation purpose, to avoid double expense booking.

#### 2.3 Purchase Invoice

On receiving Bill from supplier, for the above Purchase Receipt, you will make Purchase Invoice for the same. The general ledger entries are as follows:

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

Here "Stock Received But Not Billed" account is debited and nullified the  
effect of Purchase Receipt.

#### 2.4 Delivery Note

Let's say, you have an order from "Utah Automation Services" to deliver 5 qty of item "RM0001" at $300. Following are the details of Delivery Note:

**Customer:** Utah Automation Services

**Items:**


| Item   | Warehouse | Qty | Rate | Amount |
| ------ | --------- | --- | ---- | ------ |
| RM0001 | Stores    | 5   | 300  | 1500   |




**Taxes:**


| Account     | Amount |
| ----------- | ------ |
| Service Tax | 150    |
| VAT         | 100    |




**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

As an item is delivered from "Stores" warehouse, "Stores" account is credited and  
an equal amount is debited to the expense account "Cost of Goods Sold". The  
debit/credit amount is equal to the total valuation amount (buying cost) of  
the selling items. And the valuation amount is calculated based on your preferred  
valuation method (FIFO / Moving Average) or actual cost of serialized items.



 In this example, we have considered the valuation method as FIFO.  
 

:::tip
Valuation Rate = Purchase Rate + Charges Included in Valuation
                         = 200 + (250 / 10)
                         = 225

Total Valuation Amount = 225 * 5  = 1,125
:::







---

### 2.5 Sales Invoice with Update Stock

Let's say, you did not make Delivery Note against the above order and instead,  
you have made Sales Invoice directly, with "Update Stock" options. The details  
of the Sales Invoice are same as the above Delivery Note.

**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

Here, apart from normal account entries for an invoice, "Stores" and "Cost of  
Goods Sold" accounts are also affected based on the valuation amount.

#### 2.6 Stock Entry (Material Receipt)

**Items:**




| Item   | Target Warehouse | Qty | Rate | Amount |
| ------ | ---------------- | --- | ---- | ------ |
| RM0001 | Stores           | 50  | 220  | 11000  |


**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

#### 2.7 Stock Entry (Material Issue)

**Items:**




| Item   | Source Warehouse | Qty | Rate | Amount |
| ------ | ---------------- | --- | ---- | ------ |
| RM0001 | Stores           | 10  | 220  | 2200   |


**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

#### 2.8 Stock Entry (Material Transfer)

**Items:**




| Item   | Source Warehouse | Target Warehouse | Qty | Rate | Amount |
| ------ | ---------------- | ---------------- | --- | ---- | ------ |
| RM0001 | Stores           | Work In Progress | 10  | 220  | 2200   |


**Stock Ledger**

[Screenshot on the live page: Perpetual Inventory]

**General Ledger**

[Screenshot on the live page: Perpetual Inventory]

#### 3. Related Topics

1. [Accounting Of Inventory Stock](/erpnext/accounting-of-inventory-stock)
2. [Migrate to Perpetual Inventory](/erpnext/migrate-to-perpetual-inventory)

<!-- page: erpnext/erpnext__personal-data-deletion.md -->
---
title: "Personal Data Deletion\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/personal-data-deletion"
updated: "2026-02-26"
---

Personal data deletion tool enables a user to delete their account and anonymize all the personally identifiable data a user has generated while using ERPNext. That is, personally identifiable information will be randomized. This includes personally identifiable data from your user account like: username, full name, birth date, phone numbers, mobile numbers, location, interests, bio, email signature, Email, Contact, Address, Communication, etc. It also includes data from Leads and Opportunities, the details you have saved like phone numbers, mobile numbers, fax, website, and name.

However, this excludes data that is required by law to be maintained by a business.

## How to request account deletion

1. To begin deleting users account and personally identifiable data, you need to visit [host-name]/request-for-account-deletion (e.g. example.erpnext.com/request-for-account-deletion) in the URL field.
  [Screenshot on the live page]
2. Enter the email associated with your ERPNext account. After submitting your request, you will receive a success response.
  [Screenshot on the live page]
3. This will send an email with a verification link to delete data to the email address associated with the user.
  [Screenshot on the live page]
4. Once the user clicks on the verification link. A confirmation message will be displayed.

## How deleting a user's personal data works

The request to delete data is recorded in the doctype "Personal Data Deletion Request".

[Screenshot on the live page: Personal Data Download Request Doctype]

This doctype maintains three states of status to complete the process of removal of user data.

### Pending Verification

This status indicates that the user has requested data deletion via the web-form. However, verification of this request is still pending. Search for Personal Data Deletion Request from the search bar.

[Screenshot on the live page: Pending Verification]

### Pending Approval

This indicates that the user has verified the request via email. This enables the option of "Delete Data" for System Managers.

[Screenshot on the live page: Pending Approval]

### Deleted

This indicates that the System Manager has clicked on the "Delete Data" button. This means that the user's personally identifiable data has been anonymized.

[Screenshot on the live page: Deleted User]

### Setting SLA for Personal Data Deletion Request.

You can also set an SLA for Personal Data Deletion Request through Website Settings. This will appear on the web form description.

- Go to Website Settings
- Scroll to the section called Account Deletion Settings
- In the **Account Deletion SLA (Days)** field set the number of days within which users request for Account Deletion will be fulfilled.
- If you enable **Show Account Deletion link in My Account page**, the form link will be visible to users on the My Account Page of the website

[Screenshot on the live page: Account Deletion Settings]

<!-- page: erpnext/erpnext__personal-data-download.md -->
---
title: "Personal Data Download\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/personal-data-download"
updated: "2026-02-26"
---

Personal data download tool enables a user to automatically download all the personal data they have generated while using ERPNext. This includes personally identifiable data from your user account like: username, full name, birth date, phone numbers, mobile numbers, location, interests, bio, email signature, Email, Contact, Address, Communication, etc. It also includes data from Leads and Opportunities, the details you have saved like phone numbers, mobile numbers, fax, website, and name.

## How to request a user data download

1. To begin downloading data, the user has to **log in** and visit [host-name]/request-data (e.g. erpnext.com/request-data) in the URL field.
  [Screenshot on the live page]
2. After submitting your request, you will receive a success response.
  [Screenshot on the live page]
3. This will send an email with a download link of the data to the email address associated with the user.The file available for download will be in the JSON format.

## Personal Data Download Request DocType

The request is also recorded in the DocType "Personal Data Download Request", the file link that is sent to the user via email is also attached to the doc. Search for Personal Data Download Request from the search bar.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__petty-cash-entry-in-erpnext.md -->
---
title: "Book Petty Cash Entry | ERPNext Documentation"
description: "Record petty cash funding and expenses with a clear ERPNext audit trail."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/petty-cash-entry-in-erpnext"
updated: "2026-08-01"
---

Petty cash should use a dedicated cash ledger and a controlled custodian process. Record replenishment separately from the expenses paid from the float.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Book Petty Cash Entry

1. Create a dedicated Petty Cash account and assign responsibility for it.
2. Transfer money from the bank or main cash account into Petty Cash.
3. Record each expense with its date, expense account, amount, Cost Center, and receipt.
4. Reconcile the physical cash plus receipts to the ledger balance.
5. Post an approved adjustment only when the difference is explained.

[Screenshot on the live page: Book Petty Cash Entry in ERPNext]

## Important fields and what they mean


| Field              | What it controls                                    |
| ------------------ | --------------------------------------------------- |
| Petty Cash Account | Asset ledger holding the float.                     |
| Expense Account    | Nature of the expense.                              |
| Cost Center        | Team, branch, or function responsible for the cost. |
| Reference          | Receipt or voucher number.                          |
| User Remark        | Business purpose and supporting explanation.        |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### Petty cash shows a negative balance

Check whether the fund was replenished before expenses were posted and whether all entries use the correct petty cash account. Investigate duplicate or backdated expenses rather than forcing the balance.

### An expense was posted without a Cost Center

Correct the draft or amend the submitted transaction through the supported workflow. Configure mandatory dimensions when departmental reporting is required.

### The receipt total does not match the cash issued

Record the actual expense and return or advance balance explicitly. Attach receipts and explain small approved differences according to company policy.

## Frequently asked questions

### Should petty cash use Payment Entry or Journal Entry?

Use the document that best represents the controlled workflow and permissions. Payment Entry suits cash movement, while expense claims or Journal Entries may be appropriate for reimbursement or adjustment scenarios.

### How should the petty cash fund be replenished?

Transfer the approved amount from bank or main cash to the petty cash account and retain the supporting authorization.

### Should every small purchase be entered separately?

Preserve enough detail for receipts, tax, Cost Centers, and audit. A summarized entry should be used only when company policy and local requirements permit it.

### Can employees receive a petty cash advance?

Use Employee Advance and Expense Claim when the money is accountable to a specific employee. That workflow provides clearer settlement than treating it as an ordinary expense immediately.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__pick-list.md -->
---
title: "Pick List"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/pick-list"
updated: "2026-03-02"
---

**A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders.**

This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many Stock Keeping Unit(SKU). Pick list selects Warehouse where an Item is available on FIFO (First-In-First-Out) basis. Selection of Warehouse for a batched item is different. In case of batched items, Warehouse where the batch is nearer to its expiry will be selected.

To access Pick List, go to:


> Home > Stock > Stock Transactions > Pick List
> 
> 

1. Prerequisites
----------------

Before creating and using a Pick List, it is advised that you create the following first:

* [Stock Item](/erpnext/item)
* [Warehouse](/erpnext/warehouse)

2. How to create Pick List
--------------------------

1. Go to the Pick List list, click on New. [Screenshot on the live page: Unsaved Pick List]
2. Set the Company.
3. Select the Purpose of Pick List. These are the options under Purpose:


	* **Delivery:** This option will let you add Items from a Sales Order, to deliver. After submitting Pick List a new Delivery Note can be created based on the Warehouse from which items were picked.
	* **Material Transfer for Manufacture:** This will let you select a Work Order from which raw materials will be pulled for picking. You will be presented with an option to select the number of finished goods for which you want to pick raw materials. After picking the stock you can create Stock Entry for the picked items i.e., raw materials.
	* **Material Transfer:** This will let you select a Material Request for which you want to pick items. After picking the stock you can create a Stock Entry for the picked items.
4. Add Item and the quantity you want to pick in the Item Locations table. Click on **Get Item Locations** to get the Warehouse and other details for each Item.
5. **Parent Warehouse:** If a parent Warehouse is selected, Warehouses only under that parent Warehouse will be suggested.
6. **Get Item Locations:** Once items to be picked is finalized you can click on the **Get Item Locations** button to get Warehouse selection for each item. Since Warehouse will be automatically fetched if you get an Item from any reference document, this button can be useful to manually add additional Items or change the quantity of existing Items in the Item Locations table.
7. **Item Locations:** This will have the information of the item location (Warehouse), Serial Number for serialized items and batch no for batched items. [Screenshot on the live page: Item Locations]  


If Serial Numbers are involved, the Item row will look like this: [Screenshot on the live page: Item Location Detail]
8. Save and Submit. [Screenshot on the live page: Submitted Pick List]

### 2.1 Create Pick List from a Sales Order

1. Go to a [Sales Order](/erpnext/sales-order).
2. Click on the **Create** button on the top right of the form and then click the **Pick List** option.
3. Once you click Pick List, all the data required for Pick List will be fetched from the Sales Order.
4. Alternatively, you can create a new Pick List and click on "Get Items". This would show a popup of all pending Sales Orders.

[Screenshot on the live page]  


1. You should be able to see the Item Locations Table with the Warehouse selected for each item.
2. Save this document and it can be used for stock picking by the person performing this activity.
3. Submit the document once the stock picking is done and picked item quantities are updated in the document.

> **Note:** > > - Pick list can only be created for Sales Orders which has '% picked' < 100 > - A **Delivery Note** can be created only if the Pick List is submitted.

### 2.2 Create Pick List from a Work Order

1. Go to a [Work Order](/erpnext/work-order).
2. Click **Create Pick List** button.
3. You'll see the dialog box asking for the quantity of Finished Goods Item. This is required to calculate the number of raw material items required to manufacture the entered quantity of Finished Goods Item. [Screenshot on the live page: Dialog For qty]
4. You should be able to see the Item locations table with the Warehouse selected for each raw material item.
5. Save this document and then this document can be forwarded to the person who is picking the stock.
6. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:** > > - Pick list can only be created for Work Orders that are still in the state of 'Not Started' or 'In Progress'. > - A **Stock Entry** can be created only after the Pick List is submitted.

### 2.3 Create Pick List from Material Request

1. Go to a [Material Request](/erpnext/material-request).
2. Click on **Create** button and then click **Pick List** option.
3. You should be able to see the Item Locations table with the Warehouse selected for each item in Material Request.
4. Save this document and then this document can be forwarded to the person picking the stock.
5. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:** > > - Only Material Requests with type 'Material Transfer' can be used for Pick List creation. > - A **Stock Entry** of type 'Material Transfer' can be created after the Pick List is submitted.

3. Features
-----------

### 3.1. Update Current Stock

If a Pick List is outdated, there could be a shift in stock availability by the time a Delivery Note or Stock Entry is created against it. Clicking **Update Current Stock** will update the quantities and warehouses in the Item Locations table.

> **Note:** This button is visible as long as there are no Delivery Notes or Stock Entries against the Pick List.

### 3.2 Barcode Scanning

Pick list supports barcode scanning, introducing two check boxes. **Scan Mode**, and **Prompt Qty**.

**Scan Mode**: Scan Mode in ERPNext's Pick List feature is designed to streamline and verify the item-picking process in a warehouse or store environment. When using Scan Mode, users can scan barcodes on items to confirm that they are picking the correct products according to the Picklist. This mode is particularly useful for ensuring accuracy and efficiency during the picking process.

**Prompt Qty**: When enabled, instead of incrementing the scanned items qty by 1, a dialog will prompt the user to enter a qty to increment by.

4. Pick Manually
----------------

In the pick list, if a user manually selects batches, the system overrides the changes upon saving the pick list. To solve this issue added a checkbox 'Pick Manually' in the pick list. If this checkbox is enabled, the system will not override the user's changes in the pick list.

[Screenshot on the live page: pick_manual]  


5. Related Topics
-----------------

1. [Sales Order](/erpnext/sales-order)
2. [Work Order](/erpnext/work-order)
3. [Material Request](/erpnext/material-request)

<!-- page: erpnext/erpnext__plaid_integration.md -->
---
title: "Plaid Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/plaid_integration"
updated: "2026-02-26"
---


ERPNext offers the possibility to synchronize your bank accounts through a service called [Plaid](https://plaid.com/). Please check [the Plaid FAQ](https://support-my.plaid.com/hc/en-us) to see if your country is supported.

If your instance is connected to Plaid, you are able to synchronize your bank account transactions without having to manually import a CSV or XLSX file.


## Settings

In order to give ERPNext access to Plaid, you need to add the following three parameters to your `site_config.json` file.

- `plaid_env`
- `plaid_public_key`
- `plaid_secret`

## Activation

In order to activate Plaid on an instance, click on the button "Enable" in the Plaid Settings DocType.

[Screenshot on the live page: Enable Plaid]

Once activated, you can create a new account directly from the Bank Reconciliation dashboard.


## Bank account creation

In order to link one of your existing bank accounts to ERPNext, click on "Link a new bank account" and follow the steps proposed by Plaid.

[Screenshot on the live page: Link your bank account]


## Bank synchronization

In order to synchronize a bank account with ERPNext, select an account and click on the "Action" button to select "Synchronize this account".

[Screenshot on the live page: Synchronize your bank account]

The synchronization is based on the "Last integration date" available in the "Bank Account" doctype.

If, for any reason, you want to redo a synchronization, you can change this date and synchronize the account again.
Since all bank transactions are tagged with a specific transaction ID, the synchronization will only be incremental.


## Automatic Synchronization

You can allow plaid to synchronize your bank account with ERPNex every hour by selecting "Synchronize all accounts every hour" in Plaid Settings.
