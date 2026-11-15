<!-- Frappe documentation: erpnext, part 31 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__inter-company-journal-entry.md -->
---
title: "Inter Company Journal Entry | ERPNext Documentation"
description: "Create linked Inter Company Journal Entries in ERPNext, record both companies' debit and credit treatment, and verify each company's separate ledger posting."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inter-company-journal-entry"
updated: "2026-08-14"
---

Nova Industries pays a shared software bill on behalf of Nova Electronics Distribution, another company in the same group. One bank account paid the money, but each legal entity needs its own balanced books and a clear inter-company balance showing who owes whom.



An Inter Company Journal Entry records the two sides as separate linked Journal Entries. The first entry posts only in the first Company; ERPNext then helps you create the corresponding entry for the second Company with opposite totals.



Use this workflow for shared costs, fund transfers, and adjustments between related entities when the event does not originate from an inter-company invoice. The event is complete across the group only after both linked entries are reviewed and submitted.



DIAGRAM\_PLACEHOLDER

## Before you begin

Confirm that:

1. At least two non-group companies exist in ERPNext.
2. Each company has its own [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts), default currency, fiscal year, and Cost Center.
3. The required due-from, due-to, bank, income, and expense accounts exist in the appropriate company.
4. You know the debit and credit treatment required in both companies.
5. Users creating the pair have permission to access both companies and their accounts.
6. If the companies use different currencies, [multi-currency accounting](https://docs.frappe.io/erpnext/multi-currency-accounting) and exchange rates are configured.

For routine trade between group companies, consider [Inter Company Invoices](https://docs.frappe.io/erpnext/inter-company-invoices). Use Inter Company Journal Entry for a deliberate accounting adjustment where invoices are not the appropriate business documents.

## Understand the example

Nova Electronics Trading pays a $1,200 trade show expense on behalf of Nova Electronics Distribution. The first company records the cash outflow and a receivable from the related company. The second company records the expense and an amount payable to the first company.


| Company                       | Account                                | Debit  | Credit | Meaning                                         |
| ----------------------------- | -------------------------------------- | ------: | ------: | ----------------------------------------------- |
| Nova Electronics Trading      | Due from Nova Electronics Distribution | $1,200 |        | The related company owes this amount.           |
| Nova Electronics Trading      | Nova Operating Bank                    |        | $1,200 | Cash leaves the paying company.                 |
| Nova Electronics Distribution | Trade Show Expenses                    | $1,200 |        | The benefiting company recognizes the expense.  |
| Nova Electronics Distribution | Due to Nova Electronics Trading        |        | $1,200 | The benefiting company owes the paying company. |


Each company’s entry balances independently. The linked second entry also reverses the first entry’s total sides: the second entry’s total credit must equal the first entry’s total debit, and its total debit must equal the first entry’s total credit when both companies use the same currency.

## Create the first company’s entry

From the Journal Entry list, select **Add Journal Entry**.

Set **Entry Type** to **Inter Company Journal Entry** and select the company that records the first side. In this example, select **Nova Electronics Trading**.



[Screenshot on the live page: The first submitted Inter Company Journal Entry with Company and Entry Type highlighted]

In **Accounting Entries**, add the accounts and amounts for that company. Add a Cost Center or another [Accounting Dimension](https://docs.frappe.io/erpnext/accounting-dimensions) when required.

For the example:

1. Debit **Due from Nova Electronics Distribution** by $1,200.
2. Credit **Nova Operating Bank** by $1,200.

Select the pencil icon to open a child row when you need to enter a Cost Center, Project, party, currency, reference, or another row-level field.



[Screenshot on the live page: The first company's account rows with the row edit pencil highlighted]

Confirm that **Total Debit** equals **Total Credit**, add a clear remark, then save and submit the first Journal Entry. Submission posts the first company’s [General Ledger](https://docs.frappe.io/erpnext/general-ledger) entries. It does not yet post the other company’s side.

## Create the linked entry for the second company

Open the submitted first entry. Select **Make**, then select **Create Inter Company Journal Entry**.



[Screenshot on the live page: Create Inter Company Journal Entry highlighted in the Make menu]

Select the company that should receive the other side, then select **Create**.



[Screenshot on the live page: Nova Electronics Distribution selected in the Select Company dialog]

ERPNext opens a new draft and carries forward the following context:


| Field                                 | What ERPNext carries forward                              |
| ------------------------------------- | --------------------------------------------------------- |
| Entry Type                            | Inter Company Journal Entry                               |
| Company                               | The company selected in the dialog                        |
| Posting Date                          | The current date used by the linked-entry creation action |
| Inter Company Journal Entry Reference | The submitted first Journal Entry                         |


ERPNext does not copy the first company’s account rows because account names belong to different company ledgers. The draft starts with an empty **Accounting Entries** table. This is intentional.



[Screenshot on the live page: The second company's linked draft with an empty Accounting Entries table]

## Enter the second company’s accounts

Add the second company’s accounting treatment. In this example:

1. Debit **Trade Show Expenses** by $1,200.
2. Credit **Due to Nova Electronics Trading** by $1,200.
3. Use the second company’s Cost Center.

[Screenshot on the live page: The second company's opposite account rows with the row edit pencil highlighted]

The individual accounts do not need to have the same names as the first company’s accounts. What must agree is the economic treatment and, for companies using the same currency, the reversed debit and credit totals.

Review the entry, confirm that it balances, and submit it. ERPNext then stores the link on both Journal Entries.

## Verify the linked pair

On either submitted entry, open **More Info**, then expand **Reference**. **Inter Company Journal Entry Reference** links to the other Journal Entry.



[Screenshot on the live page: The linked Inter Company Journal Entry Reference highlighted]

You can also review both entries from the Journal Entry list.



[Screenshot on the live page: The two linked Inter Company Journal Entries in the list]

Use **View &gt; Ledger** on each entry to confirm the separate [GL Entries](https://docs.frappe.io/erpnext/accounting-entries). If consolidated group reporting is used, review the due-from and due-to balances and apply the organization’s elimination process outside the operating entries where required.

## Important fields and what they mean


| Field                                 | What it means                                                         | Guidance                                                                                                  |
| ------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Company                               | The company whose ledger receives this entry                          | Every account row must belong to this company.                                                            |
| Entry Type                            | Enables the linked inter-company workflow                             | Select Inter Company Journal Entry on the first entry. ERPNext carries it to the linked draft.            |
| Posting Date                          | The accounting date for that company’s entry                          | Review the date on both entries, especially near a period end.                                            |
| Multi Currency                        | Allows account currencies different from the company currency         | Review exchange rates and company-currency totals before submission.                                      |
| Accounting Entries                    | The accounts, parties, dimensions, and amounts posted in this company | The linked draft requires its own rows.                                                                   |
| Inter Company Journal Entry Reference | Links the two submitted Journal Entries                               | ERPNext sets this through the creation workflow and updates the first entry when the second is submitted. |
| Total Debit and Total Credit          | The balanced totals for one company                                   | Both must match within each entry. Same-currency linked entries must also have opposite totals.           |


## When a party is required

If a row uses a Receivable or Payable account, ERPNext requires **Party Type** and **Party**. Select the internal Customer or Supplier that represents the related company. For a dedicated due-from or due-to account that is not configured as a Receivable or Payable account type, a party is not mandatory, but your accounting policy may still require a separate account for each related company.

The earlier ERPNext restriction that exposed only accounts marked specifically for inter-company use was removed. Current versions filter account choices by the selected company and whether the account is a ledger account. Choose accounts that reflect the real accounting treatment instead of duplicating every normal bank or expense account solely for this entry type.

## Cancel or correct a linked pair

The two Journal Entries are separate submitted accounting documents. Cancelling one entry reverses its own ledger effect and removes the inter-company reference from the linked pair. It does not replace the need to review and correct the other company’s entry.

If both sides are wrong, correct both companies using the organization’s cancellation, amendment, or Reverse Journal Entry procedure. Keep the posting dates and explanations aligned so the audit trail remains clear.

## Troubleshooting

### Create Inter Company Journal Entry is not available

Confirm that the first Journal Entry is submitted, its Entry Type is Inter Company Journal Entry, and it does not already have an Inter Company Journal Entry Reference. The action is available only on the first submitted entry before a counterpart is linked.

### The linked draft has no account rows

This is expected in the current workflow. ERPNext cannot reuse accounts from another company’s Chart of Accounts. Add the second company’s own accounts and opposite totals.

### ERPNext says the linked debit and credit amounts do not match

For companies with the same default currency, the second entry’s total debit must equal the first entry’s total credit, and the second entry’s total credit must equal the first entry’s total debit. Check the amounts, precision, and exchange-rate treatment.

### A Receivable or Payable row asks for a party

Select the relevant Customer or Supplier in **Party Type** and **Party**. These fields are mandatory for Receivable and Payable account types unless the transaction is created through a special workflow that explicitly bypasses the requirement.

### I created both entries separately and they are not linked

Use **Make &gt; Create Inter Company Journal Entry** from the first submitted entry. Manually creating two unrelated Journal Entries does not populate the inter-company reference automatically.

## FAQs

### Does one Inter Company Journal Entry post to both companies?

No, The first entry posts only to its selected company. The linked second entry must be completed and submitted to post the other company’s side.

### Does ERPNext create the second entry automatically?

ERPNext creates the linked draft and prefills its company, entry type, posting date, and reference. You must choose the second company’s accounts, enter the amounts, review the entry, and submit it.

### Must the same accounts be used in both companies?

No, Each entry uses accounts from its own company. The accounts should express opposite sides of the same economic event, and the linked totals must agree according to the currency rules.

### Should I use an Inter Company Journal Entry or inter-company invoices?

Use invoices when one entity is selling goods or services to another and the transaction needs commercial documents, taxes, items, and receivable or payable workflow. Use this Journal Entry workflow for a direct accounting adjustment without an invoice.

### Is there a separate inter-company ledger report?

ERPNext posts the entries to the normal General Ledger. Use dedicated due-from and due-to accounts, Company filters, and consolidated reports to analyze inter-company balances.

### What happens if one linked entry is cancelled?

Its own ledger entries are reversed under ERPNext’s cancellation rules, and the reference between the pair is removed. Review the other company’s entry separately and correct it when necessary.

## Related topics

- [Journal Entry Template](https://docs.frappe.io/erpnext/journal-entry-template)
- [Finance Book](https://docs.frappe.io/erpnext/finance-book)
- [Consolidated Financial Statement](https://docs.frappe.io/erpnext/consolidated-financial-statement)

/mermaidTESTCURSOR/mermaid

<!-- page: erpnext/erpnext__introduction.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/introduction"
updated: "2026-04-27"
---

## What is ERPNext?

ERPNext is business management software that helps companies stay on top of their operations, whether it's tracking inventory, managing finances, handling projects, or keeping customers happy. Think of it as the central nervous system for your business, bringing everything together in one place.

Most ERPs are clunky, expensive, and a headache to customize. ERPNext is different. It is open-source, cloud-ready, and built to be flexible. You get the power of an enterprise system without the usual complications.

[Screenshot on the live page: ERPNext]

## Why ERPNext?

Because running a business is already hard enough. Your ERP should not make it harder.

With ERPNext, you get a complete set of tools for all your business needs, built in and ready to use. With ERPNext, you get:

1. A complete suite of tools : From Assets to Accounting to Inventory, everything you need is built-in.
2. No vendor lock-in : Open-source means you own your data and have the freedom to customize.
3. Easy to use : A clean, modern interface that doesn't feel like it was built in the '90s.
4. Cost-effective : No sky-high licensing fees. Just powerful software that works.

Whether you are a small business or a growing enterprise, ERPNext helps you stay organized, automate the boring stuff, and focus on what really matters - running your business.

## Key features

ERPNext will help you:

1. Keep track of the financial indicators of the organization.
2. Track all invoices and payments.
3. Know what quantity of product is available in stock.
4. Identify and track your key performance indicators (KPIs).
5. Identify open customer queries.
6. Manage employee payroll.
7. Assign tasks and follow up on them.
8. Maintain a database of all your customers, suppliers, and contacts.
9. Prepare quotations.
10. Track your budgets and spending.
11. Determine effective selling price based on the actual raw material, machinery, and effort cost.
12. Get reminders on maintenance schedules.
13. Publish your website.

And a ton more.

## **Under the Hood**

- [Frappe Framework](https://github.com/frappe/frappe): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
- [Frappe UI](https://github.com/frappe/frappe-ui): A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/erpnext/#production-setup).

## Learning and community

1. [Frappe School](https://frappe.school/) - Learn Frappe Framework and ERPNext from various courses by the maintainers or from the community.
2. [Documentation](https://docs.frappe.io/erpnext) - Extensive documentation for ERPNext.
3. [User Forum](https://discuss.frappe.io/c/erpnext/6) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/erpnext_public) - Get instant help from the community of users.

<!-- page: erpnext/erpnext__inventory-account.md -->
---
title: "Inventory Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inventory-account"
updated: "2026-02-25"
---

In ERPNext, users can either set up a Warehouse-wise Inventory Account or use the default Inventory Account from the Company master, which is 'Stock In Hand.'


[Screenshot on the live page: warehouse inventory account]

From the Version 16, users can also able to set the Item-wise Inventory Account. To do this, they need to enable the option 'Enable Item-wise Inventory Account' in the Company master.


[Screenshot on the live page: company configuration]

After enabling it, users can define the Default Inventory Account in the Item master. Alternatively, they can set a Default Inventory Account at the Item Group or Brand level if they do not wish to define it for each item individually. 



[Screenshot on the live page: item inventory account]


Users can choose to use either item-wise or warehouse-wise inventory accounts, but not both.

<!-- page: erpnext/erpnext__inventory_dimension.md -->
---
title: "Inventory Dimension"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inventory_dimension"
updated: "2026-02-26"
---


> Introduced in Version 14
> 
> 

Inventory dimensions in ERPNext are used to track an inventory with multiple parameters. By default, ERPNext allows to track an inventory using warehouses, batches, and serial numbers. If users want to track inventory with custom parameters then they can configure it using the Inventory Dimension feature. The user gets an option to select the Inventory Dimension on respective inventory documents as well in the stock ledger and stock balance report. With this feature, you can view dimension-wise stock ledger and stock balance reports.

To access the Inventory Dimension list, go to:


> Stock > Settings > Inventory Dimension
> 
> 

Create Inventory Dimension
--------------------------

[Screenshot on the live page: new inventory dimension]  


* Create a new record and select the Reference Document which you want to use as a custom Inventory Dimension.
* You can select any non-child document in the reference document.
* Next, the user has to put the dimension name against which the system will create a custom link field in the Applicable Documents.

Applicable For Documents
------------------------

### Apply to All Inventory Documents

[Screenshot on the live page: inventory dimension applicable for all inventory documents]  


* It will be used to select the custom Dimension in the inventory-related documents.
* For example, the user has created Inventory Dimension with the name "Shelf" and enabled "Apply to All Inventory Document Types". Then the system will create the custom link field with the name "Shelf" in the inventory documents where Batch No and Serial No fields exist.

### Apply to Specific Document

[Screenshot on the live page: inventory dimension applicable for]  


* If the user wants to add Inventory Dimension to a specific document then they have to disable the checkbox "Apply to All Inventory Document Types" and select the respective document in the "Applicable to Document" field.
* Also if you want to add Inventory Dimension for a specific condition like for stock entry type Issue you want separate dimension as "From Shelf" and stock entry type Material Receipt you want separate dimension as "To Shelf" then that can be possible using "Applicable Condition"
* Applicable Condition only can be visible if "Apply to All Inventory Document Types" is disabled
* You can also use the "Type of Transaction" with options such as Inward or Outward for a condition.
 
### Fetch value from

Users can set the 'Fetch Value From' field to fetch data from a field that exists at the parent form level. For example, on the Purchase Receipt form, a user has added a custom field called 'Shelf' and created the inventory dimension to 'Shelf'. If a Purchase Receipt contains 200 line items, the user would typically need to set the 'Shelf' value manually for each row—even if the value is the same across all items. However, by setting the 'Fetch Value From' option in the inventory dimension as 'Shelf' and specifying the value at the parent (Purchase Receipt) level, the system will automatically apply the same 'Shelf' value to all Stock Ledger Entries, even if the user hasn’t entered it in each individual line item.


[Screenshot on the live page]

Use of Inventory Dimension
--------------------------

[Screenshot on the live page: inventory dimension on transaction]  


* Once the Inventory Dimension is created system will create the custom field in respective documents
* User gets an option to select the Inventory Dimension in the respective transaction.
* For example, if the user has added Inventory Dimension as "Shelf" in the Stock Entry Detail document. Then in the stock entry, the child table user gets an option to select shelf (see above image). Post submission of the stock entry system will create the stock ledgers with selected inventory dimensions.

Validate Negative Stock
-----------------------

[Screenshot on the live page]  


If user has enabled the "Validate Negative Stock" checkbox in the inventory dimension, system will not allow to make stock transactions if the respective dimensions has negative stock in the respective warehouse. If user has tried to create the stock transaction with negative stock for the inventory dimension then system will throw the below error

  


[Screenshot on the live page]  


Stock Balance and Stock Ledger Report
-------------------------------------

* Users can able to filter the Stock Balance and Stock Ledger report using Inventory Dimension
* With this feature, users can able to see Inventory Dimension wise available quantity

### Stock Balance Report

[Screenshot on the live page: inventory dimension stock balance]  


### Stock Ledger Report

[Screenshot on the live page: inventory dimension stock ledger]  


  


Note:

User can only use the stock reconciliation with inventory dimensions to enter opening values and they can't use the stock reconciliation to modify the available stock or the valuation. Since we are not maintaining inventory dimensions wise valuation rate there is not sense to allow to modify valuation rate through stock reconciliation. in case if they tried to update the quantity or valuation rate through stock reconciliation, system will throw the below error

  


[Screenshot on the live page]  

<!-- page: erpnext/erpnext__invoice-rounding-issue.md -->
---
title: "Invoice rounding issue"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/invoice-rounding-issue"
updated: "2026-08-14"
---

Nova Industries disables rounded totals, but an invoice print still rounds the amount in words. Two settings can influence the result: the global rounded-total preference and the smallest currency fraction. The currency master must describe the real precision of the transaction currency.

## Check both settings

1. Open Global Defaults and confirm **Disable Rounded Total** matches the company’s policy.
2. Open the Currency used on the invoice.
3. Set **Smallest Currency Fraction Value** correctly, such as 0.01 for a currency whose smallest unit is one cent.
4. Save, reload the invoice, and regenerate the print.

[Screenshot on the live page: Currency master with current precision and fraction settings]



## Troubleshooting

### The printed words still differ

Check the Print Format, currency, precision, Rounded Total field, and cached print preview. Compare the numeric Grand Total, Rounded Total, and amount in words before changing any ledger posting.

## Frequently asked questions

### Does changing currency precision rewrite old invoices?

It changes how later calculations and displays use that currency. Review the effect carefully and do not expect submitted historical ledger entries to be recalculated automatically.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__invoice_discounting.md -->
---
title: "Invoice Discounting | ERPNext Documentation"
description: "Record invoice-backed short-term financing, disbursement, settlement, charges, and receivable accounts in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/invoice_discounting"
updated: "2026-08-01"
---

**Invoice Discounting** uses unpaid Sales Invoices as collateral for short-term financing from a Bank or finance company. ERPNext tracks the financed invoices, loan period, Bank charges, status, and the accounts used when financing is sanctioned, disbursed, and settled.

Use this feature only after finance has approved the accounting design. The receivable remains connected to the Customer while the financing creates a separate obligation to the lender.

## Before you begin

You need:

- one or more submitted [Sales Invoices](/erpnext/sales-invoice) with an outstanding balance;
- a Company Bank Account and Bank ledger;
- short-term loan and Bank charges accounts;
- Accounts Receivable credit, discounted, and unpaid accounts configured for the workflow;
- agreed financing amount, period, fees, recourse terms, and settlement process.

Test the complete lifecycle with finance before using it for live financing. The account names in examples are illustrative and must match your Chart of Accounts and policy.

## Create Invoice Discounting

1. Go to **Accounting &gt; Banking &gt; Invoice Discounting**.
2. Select **Add Invoice Discounting**.

[Screenshot on the live page: Invoice Discounting list with Add Invoice Discounting highlighted]

3. Select the Company and enter the Posting Date.
4. Enter the **Loan Start Date** and **Loan Period (Days)**. Verify the calculated Loan End Date against the lender agreement.

[Screenshot on the live page: Invoice Discounting dates and loan period]

5. Select **Get Invoices** or add eligible Sales Invoices to the Invoices table.
6. Verify the Customer, date, outstanding amount, and receivable account for every row.
7. Select the highlighted pencil icon to open the full discounted-invoice row when you need to inspect row details.

[Screenshot on the live page: Discounted Sales Invoice row and pencil icon]

8. Enter Bank charges and verify the Total Amount.
9. Select the **Short Term Loan Account**.

[Screenshot on the live page: Short-term loan account for Invoice Discounting]

10. Select the Bank Account that receives the disbursement.

[Screenshot on the live page: Bank Account for the financing disbursement]

11. Select the Bank Charges Account and the three Accounts Receivable control accounts.

[Screenshot on the live page: Bank Charges Account for Invoice Discounting]

12. Save and submit after the selected invoices and accounts have been reviewed.

## Important fields and what they mean


| Field                                  | What it controls                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| Posting Date                           | Accounting date for the workflow action.                                             |
| Loan Start Date                        | Date financing begins.                                                               |
| Loan Period                            | Financing duration in days.                                                          |
| Loan End Date                          | Expected maturity or settlement date.                                                |
| Status                                 | Draft, Sanctioned, Disbursed, Settled, or Cancelled stage.                           |
| Invoices                               | Sales Invoices pledged or discounted. Each must have an eligible outstanding amount. |
| Total Amount                           | Total outstanding value represented by selected invoices.                            |
| Bank Charges                           | Fees deducted or charged by the financier.                                           |
| Short Term Loan Account                | Liability account for the financing obligation.                                      |
| Bank Account                           | Ledger receiving the disbursed funds.                                                |
| Bank Charges Account                   | Expense account for financing fees.                                                  |
| Accounts Receivable Credit Account     | Control account used when receivables are credited in the financing entries.         |
| Accounts Receivable Discounted Account | Tracks receivables assigned or discounted.                                           |
| Accounts Receivable Unpaid Account     | Tracks financed invoices that remain unpaid under the configured lifecycle.          |


## Status and lifecycle


| Status     | Operational meaning                                                            |
| ---------- | ------------------------------------------------------------------------------ |
| Draft      | Financing proposal is being prepared and has not posted the lifecycle actions. |
| Sanctioned | Lender has approved the facility or selected invoices.                         |
| Disbursed  | Funds have been received and the financing obligation is active.               |
| Settled    | Customer receipt and lender settlement have completed the financing lifecycle. |
| Cancelled  | The arrangement was canceled under ERPNext cancellation rules.                 |


Use the actions available on the document to move through sanctioned, disbursed, and settled stages. Review every generated [Journal Entry](/erpnext/journal-entry) and [Payment Entry](/erpnext/payment-entry) before submission.

## When the Customer pays

Record the Customer receipt using the agreed collection route. Depending on whether the Customer pays your Company or the lender, the accounting and bank movement may differ. Follow the facility agreement and the configured ERPNext workflow.

After collection:

1. allocate the receipt to the correct Sales Invoice;
2. settle the lender liability and fees;
3. update the Invoice Discounting status;
4. confirm that the Customer outstanding, discounted receivable, Bank, and loan balances are correct;
5. reconcile the bank statement.

Use [Payment Reconciliation](/erpnext/payment-reconciliation) only when allocations need adjustment. Do not use reconciliation to hide an incorrect accounting entry.

## Controls and reporting

Maintain evidence for lender approval, disbursement, charges, pledged invoices, Customer receipts, and settlement. Reconcile:

- the Invoice Discounting register to short-term loan balances;
- discounted and unpaid receivable accounts to individual invoices;
- disbursement and settlement to [Bank Transactions](/erpnext/bank-transaction);
- charges to lender statements and agreements;
- maturity dates to open facilities.

Prevent the same Sales Invoice from being financed twice unless the product and agreement explicitly support it and the remaining eligible balance is clear.

## Troubleshooting

### Get Invoices returns no records

Confirm that Sales Invoices are submitted, belong to the selected Company, have an outstanding balance, and are not already fully allocated to another discounting record.

### An account cannot be selected

Check its Company, root type, group status, and currency. Use ledger accounts, not groups, and confirm the account purpose with finance.

### The disbursed amount differs from the invoice total

Review Bank charges, holdbacks, advance rates, and lender deductions. Record each difference in the correct account instead of forcing the Bank amount to equal the gross invoice value.

### The Customer paid after the loan maturity date

Follow the lender agreement for interest, penalties, or recourse. Record additional charges separately and settle the open liability using supported vouchers.

## Frequently asked questions

### Does Invoice Discounting sell the invoice?

Not always. The legal and accounting substance depends on the agreement, recourse, control, and local standards. Confirm treatment with finance and auditors.

### Can several invoices be financed together?

They can when eligible. Add each invoice row and verify the outstanding amount and Customer.

### Does creating the record receive money automatically?

It does not at the draft stage. Use the documented lifecycle action and verify the generated accounting entries when funds are disbursed.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Bank Account](/erpnext/bank-account)
- [Payment Entry](/erpnext/payment-entry)
- [Journal Entry](/erpnext/journal-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)

<!-- page: erpnext/erpnext__issue-type-and-priority.md -->
---
title: "Issue Type\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/issue-type-and-priority"
updated: "2026-02-28"
---

**Issue Type is useful for tagging and classifying Issues.**

Classifying Issues helps in assigning the concerned team members to specific Issues. Examples of Issue Types can be: 'Functional', 'Technical', 'Hardware', etc. So engineers can be assigned to technical or hardware issues and consultants would be assigned to address functional issues.

To access the Issue Type list, go to:

> Home > Support > Issues > Issue Type

To create an Issue Type, click on New and enter a name for the type. A description can be added.

[Screenshot on the live page]

Issue Priority
==============

**Issue Priority indicates the urgency of solving an Issue**

User can create priorities like "Low", "Medium", "High", "Critical", etc. Issue Priority will be used while creating the [Service Level Agreement](/erpnext/service-level-agreement).

To access the Issue Priority list, go to:

> Home > Support > Issues > Issue Priority

To create an Issue Priority, click on New and enter a name for the type. A description can be added.

[Screenshot on the live page: Issue Priority]

**Issue Priority list**

[Screenshot on the live page: Issue Priority List]

### Related Topics

1. [Issue](/erpnext/issue)
2. [Service Level Agreement](/erpnext/service-level-agreement)

<!-- page: erpnext/erpnext__issue.md -->
---
title: "Issue\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/issue"
updated: "2026-02-28"
---


**An Issue is an incoming query from a Customer, usually via email or from the *Contact* section of your website.**

> Tip: A dedicated support Email Address is a good way to keep track of incoming
queries. For example, you can send support queries to ERPNext at
support@erpnext.com and it will automatically create an Issue in our system.

To access the Issue list, go to:
> Home > Support > Issues > Issue

[Screenshot on the live page: Issue]

## 1. Prerequisites
Before creating and using Issues, it is advised that you create the following first:

* [Customer](/erpnext/customer)
* [Email Account](/erpnext/email-account)

## 2. How to Create Issue
Issues are automatically created if you use the **append to feature** in [Email Account](/erpnext/email-account#32-incoming-email-accounts).

You can also create an Issue manually, to do that:

1. Go to the Issue list, click on New.
1. Enter the Subject, Raised By, and a description of the Issue.

### 2.1 Additional Options when Creating an Issue
* **Status**: When a new Issue is created, its status will be "Open", when it is
replied, its status becomes "Replied".
 * Open: The Issue has been created and yet to be replied to.
 * Replied: A reply has been sent to the Issue.
 * Hold: The Issue is on Hold due to some reason.
 * Resolved: When the users are reasonably sure that they have provided the customer with a solution to their problem but have not received an acknowledgment about the resolution from the customer.
 * Closed: The Customer got a satisfactory resolution that he has indicated with an acknowledgment and the Issue was closed.

 If the sender replies to the thread, the status becomes "Open" again. User can "Close" the Issue manually by clicking on the **Close** button on the top right.

> Note: If SLA has been set up, then the fulfillment status of the SLA will be updated on both, the **Closed** as well as the **Resolved** status.

* **Customer**: If the email was sent from a [Customer](/erpnext/customer) stored in your ERPNext account, then a Customer link will appear in this field.
* **Priority**: Priority can be set as per the requirements. By default, there are three priorities--Low, Medium, and High. You can delete these or add more as needed.
* **Issue Type**: An Issue can be classified using Issue Type. Examples of Issue Types can be: 'Functional', 'Technical', 'Hardware', etc.
* **Raised By (Email)**: The email ID from which the Issue was sent will be shown here.

## 3. Features

### 3.1 Details
* **Description**: This is a text field in which details about the Issue can be seen. This can also contain an image or a table.

### 3.2 Service Level Agreement
It is a contract between a service provider and the end user that defines the level of service expected from the service provider.

User can select the [Service Level Agreement](/erpnext/service-level-agreement) (SLA) from the list.

* Every Issue will have a Time to Response and Time to Resolve within which the Support team has to Respond and Resolve the Issue.
* The Priority can be changed to escalate the Issue. The priorities need to be specified in the Service Level Agreement.
* If needed, the Service Level Agreement can be reset by clicking on the **Reset Service Level Agreement** button in Issues shown as follows:

[Screenshot on the live page: SLA]

### 3.3 Response
* **Mins to First Response**: Time in minutes from when the Issue was created to when the first reply was sent.

* **First Responded on**: When a Support team member first replies to the issue, first response date and time will be updated.

* **Average Response Time**: The average time taken to respond to the Customer. This is calculated by taking the average of all time spans between Received and Sent Communications. This field will be updated on every reply sent to the customer.

[Screenshot on the live page: Response Details]

### 3.4 Reference
User can filter the issues based on these fields linked to the Issue:

* Lead
* Contact
* Email Account
* Project
* Company

### 3.5 Resolution
* **Opening Date**: When the issue is created or logged the date be posted.
* **Opening Time**: When the issue is created or logged the exact time will automatically be posted.
* **Resolution Date**: When the user resolved the issue, Date and Time will get updated in this field.
* **Resolution Details**: User can enter the details of the issue, once it is resolved. This is a text field. Also, user can upload the image, enter or create a table.
* **Resolution Time**: Total time taken to close the ticket (from Issue creation to closing).
* **User Resolution Time**: Many times a user has to wait for a customer's reply in order to solve some Issue. While measuring User's productivity this wait time shouldn't be taken into consideration. Hence, user resolution time is the total time taken by a user to close the ticket and can be calculated as:

 _Resolution time - Total Time for which the user had to wait for a customer's reply_

The Resolution Time and User Resolution Time metrics are set on "Close". These metrics reset automatically when the Issue reopens or splits.

[Screenshot on the live page: Resolution]

#### Via Customer Portal
If the Customer raising the Issue is a Website User (no access to modules), this checkbox will be ticked to indicate that.

## 4. After Saving

### 4.1 Add Comments
Once the Issue is registered, support team Users can add comments for the issue. This field is editable. Comments in Issues are for internal discussions and will not be visible to the Customers.

### 4.2 New Email
Users can compose an email to the person that has raised the Issue. All the mails (received as well as sent) can be seen in a thread in the Issue.

### 4.3 Discussion Thread

The email discussion thread in an Issue maintains all the emails which are sent back and forth against this Issue in the system so that you can track what transpired between the sender and the person responding.

* When a New Email is sent from your mailbox, an automatic reply is sent to the sender with your message and the Support Ticket Number.
* The sender can send additional information to this email.
* All subsequent emails containing this Issue number in the subject will be added to this Issue thread.
* The sender can also add attachments to the email.

### 4.4 Assigning Issues to Users

> Issues can be assigned automatically among Users using [Assignment Rule](/erpnext/assignment-rule).

You can assign an Issue to a specific User by clicking on "Assign" feature in the left sidebar. This will add a new To Do to the user and also send a message indicating that this Issue is allocated.

[Screenshot on the live page: Assign Issue]


### 4.5 Closing

* You can close the Issue manually by clicking on 'Close' in the toolbar.
* If the sender does not reply in 7 days, then the Issue gets closed automatically.

### 5. Related Topics
1. [Issue Type and Priority](/erpnext/issue-type-and-priority)

<!-- page: erpnext/erpnext__italy.md -->
---
title: "Requirements for Italy"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/italy"
updated: "2026-02-27"
---


ERPNext aims to support local regulation for different regions in the world. In most cases ERPNext is very flexible so you can easily add Custom Fields and make Custom Reports to support the regulation of your region.

This section contains region specific features for Italy. 

- [Importing e-invoice from Supplier](/erpnext/import-e-invoice)

<!-- page: erpnext/erpnext__item-alternative.md -->
---
title: "Item Alternative\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-alternative"
updated: "2026-02-27"
---


**An Item Alternative is an Item similar to the original one and can be used instead of the original Item in manufacturing.**

If the raw material defined in the BOM is not available during the production process then their respective available alternative Item can be used to complete the production process.

First you need to enable the "Allow Alternative Item" in the Item.
[Screenshot on the live page: Item]

To access the Item alternative list, go to:
> Home > Stock > Items and Pricing > Item Alternative

This can also be done by clicking the plus sign next to 'Item Alternative' from the Item master dashboard.
You can enable Two-Way replacement between an Item and their alternative item if both can be used as an alternative to each other.

[Screenshot on the live page: Item Alternative]

## 1. Prerequisites
Before creating and using an Item Alternative, it is advised that you create the following first:

* [Item](/erpnext/item)

## 2. Item Alternative for Work Order

To allow to using alternative Items in the manufacturing process, the user can configure to 'Allow Alternative Item' in the BOM/Work Order

### 2.1 Provision to allow alternative item in the BOM
You can enable 'Allow Alternative Item' in a BOM then select the alternative item in the Stock Entry. This can also be done with a Work Order.
[Screenshot on the live page: Item]


### 2.2 Provision to allow alternative item in the Work Order
User can also enable/disable allow alternative item for individual Work Orders.
[Screenshot on the live page: Item]


Ticking on the 'Allow Alternative Item' checkbox will show a button named 'Alternate Item'. You can click on this to set the Item Alternative in the Work Order. This is how you use Item Alternative in a Work Order:
[Screenshot on the live page: Item]

This is how you use Item Alternative with a Stock Entry:
[Screenshot on the live page: Item]

If the 'Allow Alternative Item' checkbox in the Item table is disabled, you cannot set an Alternate Item for this Item.

### 2.3 Item Alternative for subcontract
In subcontract, the user has to transfer raw materials to the subcontracted supplier to get finished good from them. If the raw material is not available in the stock, with this feature, the user can transfer the alternate item of the subcontracted raw material to the supplier. This is done in the Stock Entry.

[Screenshot on the live page: Item]

After this, when you create a Purchase Receipt from the Work Order, the alternate item will be shown.

### 3. Related Topics
1. [Bill Of Materials](/erpnext/bill-of-materials)
1. [Work Order](/erpnext/work-order)

<!-- page: erpnext/erpnext__item-attribute.md -->
---
title: "Item Attribute"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-attribute"
updated: "2026-03-06"
---

### **'Item Attributes' are the characteristics based on which Item Variants are created.**

The attributes can be defined based on item's physical appearance and capabilities. Defining item attributes properly will be helpful in creating item variants as a combination of multiple attributes.

[Screenshot on the live page]

To access the Item Attribute list, go to:

> Home > Stock > Settings > Item Attribute

## How to create an Item Attribute?

1. Go to the Item Attribute list, click on 'Add Item Attribute'.
2. Enter a name for the Attribute.
3. Enter the attribute values in the table.
4. Save.

The attribute values can be numeric or non-numeric.

##### Non-Numeric Attributes

For Non-numeric attributes, specify attribute values along with their abbreviations in the Attribute Values table.

[Screenshot on the live page]

##### Numeric Attribute

If your attribute is 'Numeric', then specify the range and increment so that the system can generate respective variants.

In the following example, the cable length is of range 1 to 5 and the increment is 1. Hence, the variants will be 1,2,3,4,5.

[Screenshot on the live page]
