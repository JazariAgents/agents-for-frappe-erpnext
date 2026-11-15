<!-- Frappe documentation: erpnext, part 34 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__item_group_wise_product_listing.md -->
---
title: "Item Group-wise Product Listing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item_group_wise_product_listing"
updated: "2026-03-02"
---

Similar to the [Product Listing](/erpnext/product-listing) at `/all-products`, ERPNext offers Product Listings that are Item Group-wise as well. You can link these pages on your landing page to direct users easily.

### Setting Up an Item Group Page
To provide a Product Listing page for an Item Group (e.g. Products), go to:

> Item Group List > Products

- Enable **Show in Website**.
- Scroll down to the **Website Filters** section and add field and attribute filters similar to E Commerce Settings.
- You can also add a description in the RichText Editor that will show above the product list as a banner.

Now if you click on the **See on Website** link, on the top left, above the image in the current document, you will be redirected to the **Products** Item Group's listing page.

#### Product Visibility
Consider the Item Group **Products** has child Item Groups **Mobile Services** and **Mobiles**. 

Website Items that will be visible on the **Products** page are:

- Those having **Products** as their Item Group
- Those having **Products** in their **Website Item Groups** table.

Website Items having their Item Groups as **Mobile Services** or **Mobiles** will be visible on their respective pages. These pages will be linked in the **Products** page.

> Child Item Groups such as **Mobile Services** and **Mobiles** will be visible as pills above the search bar on the **Producst** page.

![Item Group-wise Product Listing](/files/item-group-page.png)

<!-- page: erpnext/erpnext__job-card-summary.md -->
---
title: "Job Card Summary\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card-summary"
updated: "2026-02-26"
---


To access the Job Card Summary, go to:

> Home > Manufacturing > Reports > Job Card Summary

![Task](/files/job-card-summary.png)

This report will give information about the Job Card as well as their status. Using this report users can check the month's Open and Completed Job Cards for the selected periods.

<!-- page: erpnext/erpnext__job-card.md -->
---
title: "Job Card\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card"
updated: "2026-05-20"
---

**A Job Card stores actual production information about a particular Operation performed on a particular Workstation.**

A Job Card is created from the Work Order and given to each of the Workstations in the manufacturing floor to start the production of an item with a certain quantity in each of the operations defined in the Work Order.

Job Card allows each Operation's workstation to issue a “Material Request” and “Stock Transfer to Manufacture” for raw material required against a “Job Card”.

Job Card completion will change the production status in Work Order, we can track the completion of production progress for each of the Operations defined in the Work Order.

![Work Order](/files/manufacturing-flow-jc.png)

To access the Job Card list, go to:

> Home > Manufacturing > Production > Job Card

## 1. Prerequisites

Before creating and using a Job Card, it is advised that you create the following first:

- [Bill Of Materials](/erpnext/bill-of-materials)
- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)
- [Work Order](/erpnext/work-order)

## 2. How to Create a Job Card

Job Card for Operations is automatically created when a Work Order is submitted.

This is what a Job Card looks like:

![Job Card](/files/job-card.png)

To use a Job Card follow these steps:

1. Click on the Start Job button, then on Complete Job when you're done.
2. Alternatively, you can also fill the From Time and To Time in the Time Logs table.
3. Select the Employee to whom the Job Card was assigned.
4. Enter the Completed Quantity. This is the number of Items on which the Operation was performed for the selected time interval.
5. Add more rows in the Time Logs table and record time using the Start/Completed buttons.
6. Click on Submit.

In a Work Order, the Operations and Workstations are fetched from the BOM of an Item. For ease of use, you should ensure that the [Routing](/erpnext/routing) is configured in the BOM.

Each Job Card created will have Workstation & Operations assigned. The raw material required from each Source Warehouse will be calculated based on quantity required for production.

On submitting a Work Order, Job Cards will be auto-created based on the values in the Operations table.

![Create Shareholder](/files/work-order-job-card-creation.gif)

### 2.1 Select Work Order with Item to Manufacture

You can select 'Transfer Material Against' as 'Job Card' on the Bill of Materials to transfer raw materials for Production against Job Cards.

In the Work Order, you can select the option:

![Create Shareholder](/files/work-order-transfer-against-job-card.png)

### 2.3 Using a Job Card

Employee assignment and timing detail will also be defined in Job Card. The time taken to do a job can be recorded. If multiple employees are working on the same Operation, add new job cards by clicking on the 'Create Job' Card button.

![Create Shareholder](/files/job-card-form.png)

### 2.4 Material Request against Job Card

A Material Request will be raised from the Job Card as a basis/order to prepare raw material required for the manufacturing process. The Material Request raised will have its reference to the original Job Card number.

![Create Shareholder](/files/material-request-against-job-card.png)

Track the Manufacturing Progress in The Work Order by The Completion of Each Operations defined in Work Order.

Job Card completion allows you to track the manufacturing progress inside the Work Order by looking at the completion of each Operation related to the Work Order.

![Work Order Job Card Completion](/files/work-order-job-card-completion.png)

### 2.5 Scrap Items

While completing the operations, there might be chances that some scrap materials will be produced. This scrap materials are required to be added in the inventory. For that user needs to put the details of the scrap items in the job card. User can also set the defective materials / broken materials in the scrap items table.

![Work Order Job Card Completion](/files/job_card_scrap_item.png)

## 3. Features

### 3.1 Tracking Quality Inspection

> Introduced in Version 13

For production orders, the quality of in-process (semi-finished) goods also needs to be tracked. It is defined by the process (operation) performed on it which is in turn defined in the Job Card. In-process tests are different than incoming and outgoing material tests. Monitoring quality during manufacturing helps to make sure that the finished product produced is of the desired quality. You can create a Quality Inspection for the Production Item against the Job Card.

![Quality Inspection Against Job Card](/files/qi-against-job-card.png)

![Quality Inspection link in Job Card](/files/qi-link-in-job-card.png)

## **Pending Qty in Job Card**

A new **Pending Qty** field has been introduced in the **Job Card (in Version 16)** to handle partial production and prevent incorrect Process Loss calculation.



#### Problem

Previously, while completing a Job Card, the system automatically considered the **remaining quantity** as **Process Loss Qty**. This caused issues in cases where the operation was only partially completed, preventing users from submitting the Job Card.

#### Solution

To support partial completion, a **Pending Qty** field has been added to the Job Card.

- Users can now specify the quantity that is still pending for the operation. 
- The system will **not treat the remaining quantity as Process Loss** if a **Pending Qty** is specified. 
- **Process Loss Qty** will be calculated **only when the Pending Qty is zero**, indicating that the operation is fully completed.



#### Example

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **4**





In this case, the system will **not calculate Process Loss Qty**, as the remaining quantity is marked as pending.



If:

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **0**



Then the remaining quantity (**4**) will be treated as **Process Loss Qty**.



This enhancement allows users to perform **partial production tracking** without affecting Job Card submission.



![](/files/Screen Recording 2026-05-20 at 2.07.12 PM.mov)







For more details, refer the [Quality Inspection](/erpnext/quality-inspection) page.

<!-- page: erpnext/erpnext__journal-entry-template.md -->
---
title: "Journal Entry Template | ERPNext Documentation"
description: "Learn how to create and use Journal Entry Templates in ERPNext to preload recurring accounts, dimensions, entry settings, and other accounting details."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/journal-entry-template"
updated: "2026-08-03"
---

A Journal Entry Template stores the structure of a recurring [Journal Entry](https://docs.frappe.io/erpnext/journal-entry). It can prefill the company, entry type, naming series, opening-entry setting, multi-currency setting, and account rows. Use a template when the same accounts and dimensions recur, but the amount, date, reference, or remark changes each time.



For example, Nova Electronics Trading pays office maintenance from its operating bank account every month. A template can preload **Office Maintenance Expenses** and **Nova Operating Bank**, while the accountant enters the actual amount and reference for that month.

Templates reduce repetitive selection and help users choose the intended accounts consistently. They do not post to the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) by themselves. The resulting Journal Entry must still be reviewed, balanced, saved, and submitted.

## Before you begin

Confirm that:

1. The accounts exist in the company’s [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).
2. Each account is a ledger account, not a group account.
3. You know which account should be debited and which should be credited for the recurring transaction.
4. Any required [Cost Center](https://docs.frappe.io/erpnext/cost-center), [Project](https://docs.frappe.io/erpnext/project), or other [Accounting Dimension](https://docs.frappe.io/erpnext/accounting-dimensions) is available.
5. If the template uses accounts in different currencies, [multi-currency accounting](https://docs.frappe.io/erpnext/multi-currency-accounting) is configured.

## Create a Journal Entry Template

To open the list, search for **Journal Entry Template** from the Awesome Bar. Select **Add Journal Entry Template** or open an existing template.



![A Journal Entry Template list showing Monthly Office Maintenance highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-list.png)

Enter a clear **Template Title** that identifies the recurring purpose, such as `Monthly Office Maintenance`.

Select the **Journal Entry Type**, **Series**, and **Company**. Set **Is Opening** to **Yes** only when the resulting Journal Entry records an opening balance. Enable **Multi Currency** when the template uses an account whose currency differs from the company currency.



![Journal Entry Template fields for entry type, company, and naming series](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-details.png)

In **Accounting Entries**, add the accounts that should be copied to each Journal Entry. Do not enter transaction amounts in the template. Amounts belong to the actual Journal Entry because they can change for every occurrence.

Select the pencil icon to edit a row and add its Party, Cost Center, Project, or other dimensions when required.



![Accounting Entries with the row edit pencil highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-account-rows.png)



![A Journal Entry Template account row editor with the Account field highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-row-editor.png)

Save the template.

## Important fields and what they mean


| Field                | What it controls                                                                   | Guidance                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Template Title       | The name users select from a Journal Entry                                         | Use a purpose-based name, not a month or voucher number.                                                                |
| Journal Entry Type   | The intended kind of Journal Entry                                                 | Choose the type that matches the transaction. It can also influence defaults such as bank or cash behavior.             |
| Series               | The naming series copied to the new Journal Entry                                  | Use the company’s approved Journal Entry series.                                                                        |
| Company              | The company copied to the new Journal Entry                                        | Accounts in the template must belong to this company.                                                                   |
| Is Opening           | Marks the resulting entry as an opening entry                                      | Use this only for migration or opening balances. See [Opening Balance](https://docs.frappe.io/erpnext/opening-balance). |
| Multi Currency       | Allows accounts in currencies other than the company currency                      | Review exchange rates and account currencies in the resulting entry.                                                    |
| Account              | A ledger account copied into the Journal Entry                                     | Add at least two accounts so the resulting entry can be balanced.                                                       |
| Party Type and Party | Associates the row with a Customer, Supplier, Employee, or another supported party | Set these only when the selected account requires party-wise accounting.                                                |
| Cost Center          | Tracks income or expense by business unit                                          | Set a default here only if it applies to every entry created from the template.                                         |
| Project              | Tracks the row against a project                                                   | Leave it blank when the project changes each time.                                                                      |


## Choose the right entry type

The template supports the Journal Entry types available in the current ERPNext version, including Journal Entry, Inter Company Journal Entry, Bank Entry, Cash Entry, Credit Card Entry, Debit Note, Credit Note, Contra Entry, Write Off Entry, Opening Entry, Depreciation Entry, and Exchange Rate Revaluation.

The most commonly used choices are:


| Entry type                  | When it is useful                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journal Entry               | General adjustments and recurring accruals where a more specific transaction is not available.                                                        |
| Bank Entry                  | A journal-based bank transaction. For routine customer and supplier payments, prefer a [Payment Entry](https://docs.frappe.io/erpnext/payment-entry). |
| Cash Entry                  | A journal-based cash transaction.                                                                                                                     |
| Opening Entry               | Opening balances during setup or migration. ERPNext marks **Is Opening** accordingly.                                                                 |
| Inter Company Journal Entry | Adjustments between companies. See [Inter Company Journal Entry](https://docs.frappe.io/erpnext/inter-company-journal-entry).                         |
| Exchange Rate Revaluation   | Adjustments arising from currency revaluation.                                                                                                        |


Selecting Bank Entry or Cash Entry on a normal Journal Entry can load the company’s default bank or cash account when the account table is still empty. A template can also store the intended account rows directly. Opening Entry identifies the voucher as an opening transaction, but it does not automatically add the entire Chart of Accounts. Add only the accounts needed for the opening entry.

## Create a Journal Entry from the template

1. Create a new Journal Entry.
2. Open the **More Info** tab.
3. Expand **Additional Info**.
4. Select the template in **From Template**.

![The From Template field highlighted in a new Journal Entry](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-from-template.png)



![Monthly Office Maintenance entered in the From Template field](https://novacompanies.m.frappe.cloud/files/journal-entry-template-20260802-journal-entry-select-template.png)

ERPNext copies the template’s company, entry type, naming series, opening setting, multi-currency setting, and account rows into the new Journal Entry.



![A new Journal Entry with the template fields and account rows loaded](https://novacompanies.m.frappe.cloud/files/journal-entry-template-20260802-journal-entry-template-loaded.png)

Enter the debit and credit amounts, posting date, reference details, and remarks. Add or remove account rows if this occurrence needs them. Confirm that total debit equals total credit, then save and submit the Journal Entry.

## Important warning when selecting a template

Selecting **From Template** clears the existing **Accounting Entries** rows before loading the template’s rows. Choose the template before entering account rows, or copy any work you need to retain.

The template is a starting structure, not a lock. After it loads, you can add more accounts or change copied values before saving. Review every resulting Journal Entry because the template does not validate whether the accounts and dimensions remain appropriate for that month’s transaction.

## Maintain templates safely

Update a template when the recurring accounting treatment changes for future entries. Previously submitted Journal Entries are not changed when a template is edited.

Avoid creating several templates with nearly identical names. Use titles that describe the business event, such as `Monthly Office Maintenance`, `Payroll Accrual`, or `Bank Charges`. Keep one approved template for each recurring pattern and review it when the Chart of Accounts or dimension structure changes.

## Troubleshooting

### The From Template field is not visible

In a new Journal Entry, open **More Info** and expand **Additional Info**. The top-right **Templates** button is the general Frappe form-template feature. It is different from the ERPNext **Journal Entry Template** selected in the **From Template** field.

### The template does not appear in search

Confirm that the Journal Entry Template is saved and that you have permission to read it. Also confirm that the template’s company and accounts are available to your user.

### Existing account rows disappeared

This is expected when **From Template** is selected. ERPNext clears the current Accounting Entries before copying the template’s rows. Select the template first, then add occurrence-specific rows.

### An account cannot be selected

Confirm that it is a non-group ledger account belonging to the template’s company. Also check account currency restrictions when **Multi Currency** is not enabled.

### The Journal Entry is not balanced

The template copies account structure, not debit and credit amounts. Enter the amount on each row and ensure total debit equals total credit before saving.

## FAQs

### Does a Journal Entry Template create or submit entries automatically?

No, It only prefills a new Journal Entry. A user must add the current amounts and references, review the entry, and submit it.

### Can I change the accounts after loading a template?

Yes, You can edit, add, or remove rows before saving the Journal Entry. Treat the template as a reusable starting point.

### Can one template be used for several companies?

No, A template stores one company, and its accounts belong to that company. Create a separate template for each company when the same accounting pattern is needed.

### Should I store amounts in the template?

No, Journal Entry Template account rows define accounts, parties, and dimensions. Enter debit and credit amounts in each actual Journal Entry.

### Can a template include Cost Center or Project?

Yes, Add the dimension on the account row when it should apply every time. Leave it blank when the dimension changes for each transaction.

### Does editing a template update past Journal Entries?

No, Changes affect only entries created from the template after the change. Existing drafts and submitted entries retain their own values.

## Related topics

- [Finance Book](https://docs.frappe.io/erpnext/finance-book)
- [Immutable Ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext)
- [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger)

<!-- page: erpnext/erpnext__journal-entry.md -->
---
title: "Journal Entry | ERPNext Documentation"
description: "Create balanced Journal Entries in ERPNext, understand account rows and references, verify General Ledger postings, and reverse an incorrect entry safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/journal-entry"
updated: "2026-08-14"
---

A Journal Entry records a balanced debit and credit directly in the [General Ledger](/erpnext/general-ledger). Use it for accounting adjustments, accruals, transfers, opening balances, write-offs, revaluations, and other postings that do not belong in a normal sales, purchase, or payment workflow.



For routine money received from Customers or paid to Suppliers, prefer a [Payment Entry](/erpnext/payment-entry). It selects the expected bank, cash, party, currency, and invoice-allocation fields for you. Use a Journal Entry when you need deliberate control over the accounts and understand the accounting effect.



This guide uses a simple example: Nova Industries pays $845 of office-maintenance expense from its operating bank account.


| Account                           | Debit | Credit | Meaning                  |
| --------------------------------- | -----: | ------: | ------------------------ |
| Office Maintenance Expenses - NET | $845  | $0     | Recognizes the expense   |
| Nova Operating Bank - NET         | $0    | $845   | Reduces the bank balance |


## Before you begin

Confirm that the Company, [Chart of Accounts](/erpnext/chart-of-accounts), Fiscal Year, and Posting Date are correct. The accounts must be non-group accounts belonging to the selected Company. Configure a Cost Center, Project, or other [Accounting Dimension](/erpnext/accounting-dimensions) before using it on an account row.

If the entry records a Customer or Supplier balance, use the correct receivable or payable account and select the Party Type and Party. Add a document reference when the entry should change an invoice, order, expense claim, employee advance, asset, or another supported outstanding balance.

## Create a Journal Entry

1. Open the Journal Entry list and select **Add Journal Entry**.  
![Journal Entry list showing the submitted office-maintenance example](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-list.png)
2. Select the **Company**, **Entry Type**, and **Posting Date**. For a general adjustment, keep **Entry Type** as **Journal Entry**.  
![Company and Entry Type selected on a new Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-company-type.png)
3. In **Accounting Entries**, add the account to debit and enter the debit amount. Add the offsetting account and enter the credit amount. Total Debit and Total Credit must be equal before submission.

  The grid shows the main columns. Select the highlighted pencil icon to open the complete row editor when you need Party, reference, currency, Cost Center, Project, or other row-level fields.
  ![Balanced Accounting Entries with the first row pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-accounting-rows.png)
4. In the row editor, confirm the **Account** and enter either a debit or a credit, never both on the same row. In the example, Office Maintenance Expenses is debited by $845.  
![Account and debit fields in the Journal Entry row editor](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-row-editor.png)
5. Add a clear **User Remark** and, when applicable, a Reference Number, Reference Date, Bill Number, Bill Date, and Due Date. These supporting fields do not replace a formal link to an ERPNext document.
6. Save, review the accounts and dimensions, then submit. Submission posts the debit and credit to the General Ledger.  
![Submitted Journal Entry with balanced account rows](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-submitted.png)

## Create a Journal Entry with Quick Entry

Use **Quick Entry** for a straightforward two-account posting. Enter the amount, debit account, credit account, date, and remark. ERPNext fills the Accounting Entries table and saves the draft. Open the full form before submission when you need a Party, document reference, multiple rows, dimensions, or multiple currencies.



![Quick Journal Entry dialog with amount, debit account, and credit account highlighted](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-quick-entry.png)

You can also select a reusable [Journal Entry Template](/erpnext/journal-entry-template). Loading a template replaces the current account rows and brings in its Entry Type, Company, naming series, opening-entry setting, multi-currency setting, and accounts. You can add or edit rows after loading it.

## Important fields and what they mean


| Field                                | What it controls                                                                                                                                                                                                     |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entry Type                           | Classifies the posting and can enable type-specific behavior, such as Inter Company Journal Entry or Opening Entry.                                                                                                  |
| Finance Book                         | Limits the posting to a specific [Finance Book](/erpnext/finance-book). Leave it blank when the entry should appear in every Finance Book.                                                                           |
| Multi Currency                       | Shows account currency, exchange rate, and debit or credit in account currency. The selected accounts determine which currencies are available. See [Multi Currency Accounting](/erpnext/multi-currency-accounting). |
| Party Type and Party                 | Identifies the Customer, Supplier, Employee, or other party represented by a receivable or payable row.                                                                                                              |
| Reference Type and Reference Name    | Links a row to a submitted transaction and can change its outstanding or advance position. Do not select an unrelated document merely as a note.                                                                     |
| Is Advance                           | Identifies an advance against a supported order or party. Prefer the supported advance-payment workflow where available so the amount remains reconcilable.                                                          |
| Cost Center, Project, and dimensions | Attribute income, expense, asset, or liability movement for reporting. These values are stored on each account row.                                                                                                  |
| Mode of Payment and Bank Account     | Add payment context and can fetch configured bank information. For routine payments, a Payment Entry is usually safer.                                                                                               |
| Pay To / Recd From                   | Supplies the name used by applicable print formats, including cheque-oriented formats.                                                                                                                               |
| Is Opening                           | Marks a migrated opening posting. Use the documented [Opening Balance](/erpnext/opening-balance) process and validate the temporary opening account.                                                                 |


Supported references can include Sales Invoice, Purchase Invoice, Journal Entry, Sales Order, Purchase Order, Expense Claim, Asset, Loan, Payroll Entry, Employee Advance, Exchange Rate Revaluation, and Invoice Discounting. Availability depends on the selected account, party, document status, and current outstanding amount.

Do not manually set **Payment Entry** as a Journal Entry row reference. Current ERPNext blocks this because payment-allocation relationships must be created through the supported payment and reconciliation workflow.

## Entry types


| Entry type                                                    | Typical use                                                                                                                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journal Entry                                                 | General accrual, adjustment, direct expense, or multi-account posting                                                                                                       |
| Inter Company Journal Entry                                   | Mirrored posting between related Companies. Follow the [Inter Company Journal Entry](/erpnext/inter-company-journal-entry) workflow.                                        |
| Bank Entry, Cash Entry, Credit Card Entry                     | Classification for account movements using the corresponding account type                                                                                                   |
| Contra Entry                                                  | Cash-to-bank, bank-to-cash, bank-to-bank, or cash-to-cash transfer inside the Company                                                                                       |
| Debit Note and Credit Note                                    | Accounting classification for an adjustment. For invoice returns, use the supported [Debit Note](/erpnext/debit-note) or [Credit Note](/erpnext/credit-note) workflow.      |
| Write Off Entry                                               | Writes off a receivable or payable against an appropriate expense or income account. Review [Accounting for Bad Debts](/erpnext/accounting-for-bad-debts) where applicable. |
| Opening Entry                                                 | Migrates balance-sheet balances and outstanding positions                                                                                                                   |
| Depreciation Entry and Asset Disposal                         | System or controlled postings connected to [Asset Depreciation](/erpnext/asset-depreciation) and disposal                                                                   |
| Exchange Rate Revaluation, Exchange Gain Or Loss              | Currency revaluation and realized or unrealized exchange differences                                                                                                        |
| Deferred Revenue, Deferred Expense, Periodic Accounting Entry | System-supported recognition or periodic stock-accounting postings                                                                                                          |
| Excise Entry                                                  | Legacy or regional classification. Confirm applicability with the relevant localization and tax adviser before use.                                                         |


## Verify the General Ledger impact

On the submitted Journal Entry, open **View &gt; Ledger**.



![Ledger action highlighted in the View menu of a submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-view-ledger-menu.png)

The report should show the same total debit and credit under the Journal Entry voucher. In this example, Office Maintenance Expenses is debited by $845 and Nova Operating Bank is credited by $845.



![General Ledger filtered to the submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-general-ledger.png)

For very large entries with more than 100 account rows, current ERPNext can queue submission or cancellation in the background. Wait for processing to finish before relying on the ledger or financial reports.

## Correct or reverse a Journal Entry

Do not edit a submitted posting. If the original should be cancelled and corrected, follow the permitted cancellation and amendment process, subject to linked documents, frozen periods, and [Immutable Ledger](/erpnext/immutable-ledger-in-erpnext) rules.

Use **Actions &gt; Reverse Journal Entry** when the accounting correction should be recorded as a new posting with the debit and credit sides exchanged. Review the generated draft and its Posting Date before submission. On current develop versions, reversal entries are linked to their originals and protected from casual field changes.



![Reverse Journal Entry action highlighted on a submitted entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-reverse-action.png)

## Troubleshooting

### Total debit and credit do not match

Review each row and confirm that an amount was entered on only one side. Add the intended offsetting account. The difference must be zero; do not use a miscellaneous account merely to force balance without understanding the cause.

### A Customer or Supplier cannot be selected

Select the correct receivable or payable account first. Confirm the account belongs to the Company and that the Party Type is valid for that account.

### A document is missing from Reference Name

The document normally must be submitted, belong to the relevant party and account, and have a compatible outstanding or unbilled position. Confirm the row's Account, Party Type, Party, Reference Type, and Cost Center.

### A foreign-currency account is unavailable

Enable **Multi Currency** and confirm that the account was created with the required currency. ERPNext does not let a transaction arbitrarily override an account's currency.

## Frequently asked questions

### Should I use a Journal Entry for normal Customer receipts and Supplier payments?

Usually no. Use Payment Entry because it handles party accounts, bank or cash accounts, invoice allocations, advances, exchange rates, references, and later reconciliation more explicitly. Use Journal Entry for a deliberate accounting adjustment or a workflow that specifically requires it.

### Does saving a draft affect the General Ledger?

No, The General Ledger is posted when the Journal Entry is submitted. Cancelling or reversing it creates the corresponding accounting effect according to the current ledger rules.

### Can one Journal Entry contain more than two accounts?

Yes, It may contain several debit and credit rows as long as the total debit equals the total credit and every row passes account, party, reference, currency, and dimension validation.

### Can I use a Journal Entry to settle an invoice?

ERPNext can update an invoice's outstanding position when the correct receivable or payable row is linked to the invoice. For an actual receipt or payment, Payment Entry and [Payment Reconciliation](/erpnext/payment-reconciliation) normally provide a clearer audit trail.

### What is the difference between reversing and cancelling?

Cancellation reverses the submitted document under ERPNext's cancellation rules. **Reverse Journal Entry** creates a separate draft with exchanged debit and credit sides so the correction can be reviewed and posted as its own voucher.

## Related topics

- [Journal Entry Template](/erpnext/journal-entry-template)
- [Accounting Entries](/erpnext/accounting-entries)
- [Inter Company Journal Entry](/erpnext/inter-company-journal-entry)
- [General Ledger](/erpnext/general-ledger)
- [Payment Entry](/erpnext/payment-entry)
- [Repost Accounting Ledger](/erpnext/repost-accounting-ledger)
- [Finance Book](/erpnext/finance-book)

<!-- page: erpnext/erpnext__landed-cost-voucher.md -->
---
title: "Landed cost Voucher"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/landed-cost-voucher"
updated: "2026-02-26"
---

For creating a **Landed cost voucher** in ERPNext: You have to create it against a **Purchase Receipt** and **Purchase Invoice.**  
While creating against **Purchase Invoice**: In the Purchase Invoice --> **Update Stock** should be checked.  
![](/files/z3sBK9F.png)  
 If this field is unchecked, the Purchase Invoices will not be fetched in the Landed Cost Voucher  
While creating against **Purchase Receipt**: The Item selected should have **Maintain Stock** checked.  
![](/files/vEwpm61.png)  
 If this field is not checked, the Items will not be displayed when you click **Get items from Purchase Receipt.**   
While creating a Landed cost Voucher, additional costs can be added for the items until they land in our Inventory.  
These additional charges once added, get added in the **Item Valuation rate** and update the Item Rate.  
You can trace this additional charge effect on the Accounting ledger in the **Purchase Receipt --> View --> Accounting Ledger**  
If the additional charges have to be paid against the Landed Cost Voucher, you can:1. You can create a **Payment Entry** directly to complete the payment for additional expenses for the Item and then create a **Purchase Invoice** with **Is Paid** checked --> [In this case, Purchase Invoice is not mandatory unless you want the accounting effect to be seen. ]
2. You can create a **Purchase Invoice** for a **Supplier** for which the **Additional Expenses** are incurred, this way you can see the Accounting effect for the expenses as per the Landed Cost Voucher, then create a Payment entry against it.

  

<!-- page: erpnext/erpnext__ldap-integration.md -->
---
title: "Setting up LDAP\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/ldap-integration"
updated: "2026-02-26"
---


Lightweight Directory Access Protocol (LDAP) is a centralized access control system used by many small and medium-scale organizations.

By settings up LDAP service, you able to login to ERPNext account by using LDAP credentials.

## 1. Prerequisites
To use LDAP, you will first need to install the `ldap3` Python module. To do this, open a terminal session on your server that hosts the ERPNext instance. Go to the `frappe-bench` directory.
run the command: `./env/pip install ldap3`

You are now ready to enable the LDAP service in ERPNext.

## 2. Setting up LDAP
To setup LDAP, go to
> Home > Integrations > LDAP Settings

Many parameters are mandatory to allow ERPNext to connect to LDAP. They are:

 * LDAP Server URL: This is the URL to your LDAP server. Must be in the form of `ldap://yourserver:port` or `ldaps://yourserver:port`

 * Base Distinguished Name (DN): This is the distinguished name of the user that has permissions to look up user details on your LDAP server. This should be a user that only has read-only permissions on your LDAP Server.

 * Password for Base DN: This is the password for the user above, that is used to look up user details on your LDAP server.

 * Organization Unit of Users: This is the DN of the Organizational Unit that all users in your LDAP server must be part of to be able to log into ERPNext.

 * Default Role on Creation: When the user is created in ERPNext, they will be assigned with this default role, the first time they log in.

 * LDAP Search String: This field allows ERPNext to match the user/email entered in the ERPNext login screen, with the LDAP Server. For example, you could use email address, or username depending on your preference.

 It must be entered in the format: `LDAPFIELD={0}`

 Active Directory username example: `sAMAccountName={0}`

 Open LDAP username example: `uid={0}`

 * LDAP Email Field: Specifies the LDAP field that contains the email address of the user.

 Active Directory and Open LDAP example: `mail`

 * LDAP Username Field: Specifies the LDAP field that contains the username of the user.

 Active Directory example : `sAMAccountName`

 Open LDAP example: `uid`

 * LDAP First Name Field: Specifies the LDAP field that contains the first name of the user.

 Active Directory example: `givenName`

 Open LDAP example: `sn`

There are many other non-mandatory fields that you can use to map your LDAP user fields to the ERPNext user fields. They are:

 * Middle Name
 * Phone
 * Mobile



Once your settings are correct, you can click the `Enabled` checkbox at the top. When attempting to enable LDAP, ERPNext will try and connect to the LDAP server to ensure the settings are correct. If it fails, you will not be able to enable LDAP and will receive an error message.

The error message will indicate the issue that needs to be resolved to continue.

After setting enabling LDAP, on the login screen, the system enables **Login Via LDAP** option.



### 2.1 LDAP Security

In the LDAP Security section, You have many options to connect securely to your LDAP server.

 * ##### SSL/TLS Mode
 Specifies whether you want to start a TLS session on initial connection to the LDAP server.

 * ##### Require Trusted Certificate
 Specifies if you require a trusted certificate to connect to the LDAP server


 If you are specifying a trusted certificate, you will need to specify the paths to your certificate files. These files are to be placed on your ERPNext server, and the following fields should be an absolute path to the files on your server.
 The certificate fields are:

 * Path to private Key File

 * Path to Server Certificate

 * Path to CA Certs File


### 2.2 LDAP Group Mappings
ERPNext also allows you to automatically map multiple LDAP groups to the appropriate ERPNext roles.
For example, you may want all of your Accounting employees, to automatically have the Accounts User Role.

Ensure that you fill out the LDAP Group Field to allow this. This is the LDAP field that is found on a user object in LDAP, that has all of the groups the user is a member of.

For Active Directory and Open LDAP, this field should be set to `memberOf`.

Open LDAP may need this field to be enabled on your LDAP server. Please see examples on the internet for more details.

> Note that all ERPNext roles will be checked each time a user logs on and will be removed or added to the user's permissions.



In the LDAP Settings area, there are two dropdowns.
1. SSL/TLS Mode - set this to **StartTLS** to connect to your LDAP server using StartTLS. If your LDAP server does not support StartTLS, setting this to StartTLS will result in an error `StartTLS is not supported`. Check the configuration on your LDAP server if you receive this error.
2. Require Trusted Certificate - if you change this to **Yes** then the certificate provided by the LDAP server must be trusted by the Frappe/ERPNext server. If you would rather use StartTLS with a self-signed (untrusted) certificate, set this to **No**. If you do not use StartTLS, this setting is ignored.
