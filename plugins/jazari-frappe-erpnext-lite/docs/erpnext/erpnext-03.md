<!-- Frappe documentation: erpnext, part 3 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__bank-accounts-and-modes-of-payment.md -->
---
title: "Bank Accounts and Modes of Payment | ERPNext Documentation"
description: "Configure banks, company bank accounts, ledger accounts, and Modes of Payment in ERPNext for accurate payment processing and reconciliation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-accounts-and-modes-of-payment"
updated: "2026-08-14"
---

ERPNext needs two related pieces of information to record money correctly: where the money moved and how it moved. A Bank Account represents the real account held with a bank, while a Mode of Payment describes the channel, such as bank transfer, card, cash, or cheque.



Nova Industries may receive a card payment into one clearing account, a wire transfer into its operating bank, and cash at a showroom counter. Mapping each payment method to the right ledger account reduces manual selection and makes bank reconciliation easier later.



This page explains the relationship between Bank, Bank Account, ledger account, and Mode of Payment, then shows how to configure defaults that lead users to the correct account without hiding the accounting trail.

## Understand the records


| Record          | Purpose                                                                              |
| --------------- | ------------------------------------------------------------------------------------ |
| Bank            | Identifies the financial institution                                                 |
| Bank Account    | Stores an account held by a company, Customer, or Supplier                           |
| Account         | The Bank-type ledger in the Chart of Accounts                                        |
| Mode of Payment | Describes how money is paid or received, such as Cash, Check, Card, or Wire Transfer |


## Create a Bank

Go to **Home &gt; Accounting &gt; Bank Statement &gt; Bank** and add the institution.

![Bank master](/files/bank-master.webp)

Add integration details only when you use a supported bank integration.

## Create the company bank account

1. Create a ledger account under Bank Accounts in the company’s [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts). Set **Account Type** to **Bank**.
2. Open **Bank Account** and click **Add Bank Account**.
3. Select the Bank and enter the account name or number.
4. Select **Company** as the party type when it is the company’s own account.
5. Link the corresponding ledger account.
6. Mark it as the company default only when appropriate.

Store only the information required for operations and reconciliation. Restrict access to sensitive bank details.

## Configure Modes of Payment

Open **Mode of Payment**, select the type, and add a default account for each company.

![Mode of Payment default account](/files/mode-of-payment-defaults.webp)

For example, Cash should normally use a Cash-type ledger. A wire transfer or card settlement should use the relevant Bank or clearing account.

## How ERPNext selects the payment account

ERPNext first uses a transaction-specific value when supplied. It can otherwise fetch a company default or the account mapped to the selected Mode of Payment. Always verify the paid-from and paid-to accounts before submitting a Payment Entry.

## Bank statements and reconciliation

Use [Bank Transaction](https://docs.frappe.io/erpnext/bank-transaction) records to import or synchronize statement lines. Then use [Bank Reconciliation](https://docs.frappe.io/erpnext/bank-reconciliation) to match them with Payment Entries and Journal Entries.

## Troubleshooting

**A bank ledger is not selectable**

Confirm it belongs to the same company, is not a group, is enabled, and has Account Type Bank.

**A Mode of Payment selects the wrong account**

Review its company-wise default accounts and the transaction’s company.

## Related topics

- [Payment Entry](https://docs.frappe.io/erpnext/payment-entry)
- [Bank Reconciliation](https://docs.frappe.io/erpnext/bank-reconciliation)
- [Bank Statement Import](https://docs.frappe.io/erpnext/bank-statement-import)
- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)

<!-- page: erpnext/erpnext__bank-guarantee.md -->
---
title: "Bank Guarantee | ERPNext Documentation"
description: "Track guarantees received or provided, their validity, beneficiary, margin, charges, and references in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-guarantee"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, places a large electronics order but wants protection if Nova Industries does not meet the contract. A bank may guarantee Nova Industries' obligation, giving the customer confidence without requiring an immediate payment between the two companies.



A Bank Guarantee records the bank's commitment, its beneficiary, amount, validity, and linked transaction. ERPNext can track guarantees received from customers and guarantees issued on your company's behalf.



Use it to monitor contractual security and expiry dates. The record is operational evidence and does not automatically post accounting entries.



## Before you begin

Collect the guarantee document and confirm:

- whether the guarantee is **Receiving** or **Providing**;
- the underlying Sales Order, Purchase Order, Project, or contract;
- beneficiary and applicant details;
- guaranteed amount, start date, expiry, and claim terms;
- issuing Bank and Bank Account;
- margin money, charges, fixed deposit, and related accounting entries.

Create the [Bank](/erpnext/bank) and [Bank Account](/erpnext/bank-account) first. Confirm with finance how margin money and charges will be recorded through a [Payment Entry](/erpnext/payment-entry) or [Journal Entry](/erpnext/journal-entry).

## Create a Bank Guarantee

1. Go to **Accounting &gt; Banking &gt; Bank Guarantee**.
2. Select **Add Bank Guarantee**.

![Bank Guarantee list with Add Bank Guarantee highlighted](https://novacompanies.m.frappe.cloud/files/banking-07-bank-guarantee-list.png)

3. Choose the **Bank Guarantee Type**:
  - **Receiving** when another party provides the guarantee for your benefit;
  - **Providing** when your Bank issues it for a Customer, Supplier, or other beneficiary.
4. Enter the amount, start date, validity, and end date. Verify the expiry against the issued document.

![Bank Guarantee type, amount, and validity fields](https://novacompanies.m.frappe.cloud/files/banking-08-bank-guarantee-purpose.png)

5. Select the Bank, Bank Account, and related General Ledger account when applicable.

![Bank and Bank Account on the guarantee](https://novacompanies.m.frappe.cloud/files/banking-09-bank-guarantee-bank-details.png)

6. Enter the Bank's guarantee number and the beneficiary name exactly as shown on the issued instrument.

![Guarantee number and beneficiary](https://novacompanies.m.frappe.cloud/files/banking-09b-bank-guarantee-reference.png)

7. Add the reference document, Customer or Supplier, and Project when they identify the underlying obligation.
8. Record margin money, charges, fixed deposit number, clauses, and conditions.
9. Attach the issued guarantee and save the record.

## Important fields and what they mean


| Field                            | What it controls                                                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Bank Guarantee Type              | Distinguishes guarantees received from guarantees provided.                                                            |
| Reference Document Type and Name | Links the guarantee to a Sales Order, Purchase Order, or other supported record.                                       |
| Customer or Supplier             | Party connected to the selected sales or purchase reference.                                                           |
| Project                          | Project or contract supported by the guarantee.                                                                        |
| Amount                           | Maximum guaranteed value. Use the currency and amount shown in the instrument.                                         |
| Start Date                       | Date from which the guarantee is effective.                                                                            |
| Validity in Days                 | Duration used to derive or check the end date.                                                                         |
| End Date                         | Expiry date. Monitor this date before renewal, release, or claim deadlines.                                            |
| Bank and Bank Account            | Institution and account through which the guarantee is issued or tracked.                                              |
| Bank Guarantee Number            | Unique reference assigned by the Bank.                                                                                 |
| Name of Beneficiary              | Party entitled to claim under the guarantee.                                                                           |
| Margin Money                     | Cash or deposit blocked as security. Record its accounting separately.                                                 |
| Charges Incurred                 | Bank fees associated with issuing or maintaining the guarantee.                                                        |
| Clauses and Conditions           | Operational summary of claim, expiry, renewal, and release terms. The attachment remains the authoritative instrument. |


## Receiving versus providing

When **Receiving**, monitor whether the counterparty maintains the guarantee through the required contractual period. Store the original or verified copy and set reminders before expiry.

When **Providing**, monitor the exposure, margin, fees, beneficiary, release documentation, and whether the guarantee should be renewed. A provided guarantee may create a contingent liability even when no payable is posted automatically.

## Accounting and controls

The Bank Guarantee record does not automatically debit margin money or expense charges. Record those movements using the correct accounting voucher:

- transfer blocked cash to a margin or deposit account;
- expense Bank charges to the approved account and Cost Center;
- release margin money when the Bank confirms release;
- recognize a claim only through the approved legal and accounting process.

Reconcile the guarantee register with Bank confirmations and the General Ledger. Restrict access to attachments containing account details, signatures, or confidential contract terms.

## Review and next steps

Review guarantees by expiry date at least monthly. For each guarantee, determine whether to:

- allow it to expire;
- obtain formal release;
- renew or extend it;
- reduce the amount;
- replace it with another instrument;
- prepare for or respond to a claim.

Use assignment, comments, or a workflow to identify the responsible owner. An expiry date without an owner or reminder is easy to miss.

## Troubleshooting

### The Customer or Supplier field does not appear

Select the relevant reference document type first. Customer is shown for supported sales references and Supplier for supported purchase references.

### End date does not match the instrument

Check the start date, validity calculation, inclusivity of dates, and any wording that specifies a fixed calendar expiry. Use the issued instrument as the authoritative source.

### Margin money is missing from the General Ledger

The Bank Guarantee is not an accounting voucher. Create the appropriate Payment Entry or Journal Entry and link it through references or attachments.

### The guarantee has expired but remains active operationally

Obtain the renewal or extension from the Bank, update the tracked dates with supporting evidence, and retain the prior instrument for the audit trail.

## Frequently asked questions

### Does a Bank Guarantee reduce the Bank balance automatically?

It does not. Record margin, deposit, and fee movements through accounting transactions.

### Can one guarantee cover several orders?

It may contractually, but the ERPNext reference field points to one document. Explain the broader coverage in conditions and attachments, or use a Project as the common reference.

### Should the guarantee document be attached?

It should, subject to your access and confidentiality policy. The structured fields support tracking, while the issued document contains the legal terms.

## Related topics

- [Bank](/erpnext/bank)
- [Bank Account](/erpnext/bank-account)
- [Payment Entry](/erpnext/payment-entry)
- [Journal Entry](/erpnext/journal-entry)
- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)

<!-- page: erpnext/erpnext__bank-reconciliation.md -->
---
title: "Bank Reconciliation | ERPNext Documentation"
description: "Match ERPNext accounting vouchers with bank statement transactions and balances."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-reconciliation"
updated: "2026-08-01"
---

Bank Reconciliation compares the bank statement with entries in ERPNext. Match existing vouchers first, create missing accounting entries only when necessary, and finish by explaining every difference between the statement and ledger balances.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Bank Reconciliation

1. Select the Company Bank Account and statement date range.
2. Import or synchronize Bank Transactions.
3. Match each statement line with the correct Payment Entry, Journal Entry, or other supported voucher.
4. Create a missing voucher only after checking that it does not already exist.
5. Record bank fees, interest, and timing differences explicitly.
6. Confirm that the closing balance agrees with the bank statement.

![Bank Reconciliation in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-12-bank-reconciliation.png)

![Bank Reconciliation details](https://novacompanies.m.frappe.cloud/files/payments-13-bank-transactions-for-reconciliation.png)

## Important fields and what they mean


| Field                          | What it controls                           |
| ------------------------------ | ------------------------------------------ |
| Bank Account                   | Company account being reconciled.          |
| Bank Statement Closing Balance | Closing balance from the source statement. |
| Bank Transactions              | Imported statement lines.                  |
| Vouchers                       | Accounting entries available for matching. |
| Unreconciled Amount            | Difference still requiring action.         |
| Clearance Date                 | Date on which a voucher cleared the bank.  |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### A Payment Entry does not appear for reconciliation

Check that it posts to the selected bank account, falls within the date range, is submitted, and has not already been cleared. Also review the banking settings and the Payment Entry's Paid From and Paid To accounts.

### The bank statement balance does not match ERPNext

Confirm the statement opening and closing dates, opening balance, uncleared cheques, bank fees, interest, transfers, and duplicate imports. Do not force the difference into the reconciliation date without identifying it.

### An imported Bank Transaction has no suggested match

Verify the amount, date, currency, reference number, and bank account. Expand the matching date range when settlement dates differ, then select the correct voucher manually if necessary.

### The clearance date changed, but the General Ledger posting date did not

This is expected. Reconciliation records when the bank cleared the transaction; it does not move the original accounting posting date.

## Frequently asked questions

### What is the difference between Payment Reconciliation and Bank Reconciliation?

Payment Reconciliation links party payments to invoices. Bank Reconciliation matches accounting transactions to the bank statement and records clearance.

### Should reconciliation be done daily or monthly?

Use a frequency appropriate to transaction volume and control requirements. High-volume accounts often benefit from daily or weekly work, with a formal month-end completion.

### Can one bank transaction be matched to several Payment Entries?

Use the supported multi-allocation behavior when the bank combined several accounting payments into one statement line. The selected entries must explain the statement amount completely.

### Should unmatched bank fees be entered during reconciliation?

Create the appropriate accounting transaction for the fee, using the bank charges account, and then reconcile it. Reconciliation should not replace the accounting entry.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__bank-transaction.md -->
---
title: "Bank Transaction | ERPNext Documentation"
description: "Import, review, match, reconcile, and troubleshoot bank statement transactions in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-transaction"
updated: "2026-07-31"
---

A **Bank Transaction** is one line from a bank statement or banking integration. It records the date, amount, description, and Bank reference. You reconcile it with a Payment Entry, Journal Entry, or another supported voucher so ERPNext can compare statement activity with the General Ledger.

## Before you begin

Create the [Bank](/erpnext/bank), [Bank Account](/erpnext/bank-account), and linked Bank ledger. Confirm that the statement belongs to the correct Company account and currency.

Set a consistent import process. Keep the original statement file, define who imports it, and prevent the same period from being loaded twice.

## Bring Bank Transactions into ERPNext

Transactions can be synchronized through a supported integration, imported from a statement, loaded with Data Import or API, or entered manually for controlled correction.

The list should show real statement activity rather than an empty example.

![Bank Transaction list with deposits and withdrawals](https://novacompanies.m.frappe.cloud/files/banking-14-bank-transaction-list.png)

Before importing a full statement:

1. check the date and amount formats;
2. confirm whether credits are deposits and debits are withdrawals;
3. map description, reference, and transaction identifier fields;
4. test a few rows;
5. compare the imported total with the source statement.

Use the Bank master's transaction mapping when the source headings differ from the expected fields.

## Review a Bank Transaction

Open a transaction and verify the Date, Bank Account, currency, and amount direction. A receipt is stored as **Deposit**. A payment or charge is stored as **Withdrawal**.

![Date, Bank Account, and deposit amount](https://novacompanies.m.frappe.cloud/files/banking-15-bank-transaction-amount.png)

Review the description, bank reference number, transaction identifier, and transaction type. These fields help find the correct accounting voucher and detect duplicates.

![Description, reference number, and transaction type](https://novacompanies.m.frappe.cloud/files/banking-16-bank-transaction-reference.png)

Do not overwrite the bank's description merely to make matching easier. Preserve original evidence and use party, allocation, or comments for internal classification.

## Important fields and what they mean


| Field                | What it controls                                                               |
| -------------------- | ------------------------------------------------------------------------------ |
| Date                 | Statement value or transaction date supplied by the Bank.                      |
| Bank Account         | Company Bank Account to which the statement line belongs.                      |
| Company              | Derived or selected Company for the transaction.                               |
| Deposit              | Incoming amount on the statement.                                              |
| Withdrawal           | Outgoing amount on the statement. A line should not normally have both values. |
| Currency             | Statement currency. It should agree with the Bank Account and import.          |
| Description          | Narrative supplied by the Bank.                                                |
| Reference Number     | Check, transfer, batch, or other Bank reference.                               |
| Transaction ID       | Stable identifier used for traceability and duplicate control.                 |
| Transaction Type     | Bank-supplied classification such as ACH, wire, fee, or card settlement.       |
| Payment Entries      | Accounting vouchers matched or created against the statement line.             |
| Allocated Amount     | Portion connected to accounting vouchers.                                      |
| Unallocated Amount   | Balance that still needs matching or classification.                           |
| Party Type and Party | Customer, Supplier, Employee, or other identified counterparty.                |
| Included Fee         | Fee already included in the statement amount.                                  |
| Excluded Fee         | Fee reported separately from the main amount.                                  |


## Reconcile a Bank Transaction

Use [Bank Reconciliation](/erpnext/bank-reconciliation) to find candidate vouchers. Compare amount, date, reference, party, and description.

### Match an existing voucher

Choose the existing [Payment Entry](/erpnext/payment-entry) or [Journal Entry](/erpnext/journal-entry) when the books already contain the transaction. One statement line may be matched with several vouchers when the Bank combines activity, and one voucher may require careful treatment when the Bank splits it.

### Create a missing voucher

Create a Payment Entry for a genuine receipt, payment, or transfer that has not been recorded. Create a Journal Entry for an appropriate fee, interest, or adjustment. Verify accounts, party, tax, Cost Center, and references before submission.

Do not create a new voucher until you have searched for an existing one. Duplicate payments are one of the most costly reconciliation mistakes.

## Status


| Status       | Meaning                                                     |
| ------------ | ----------------------------------------------------------- |
| Pending      | Transaction is awaiting processing.                         |
| Unreconciled | It has not been fully matched to accounting vouchers.       |
| Reconciled   | The amount has been matched and accepted in reconciliation. |
| Settled      | The transaction's configured processing is complete.        |
| Cancelled    | The Bank Transaction was canceled under ERPNext rules.      |


## Fees, differences, and combined settlements

When a Customer pays an invoice less a Bank fee, record the gross receipt and fee according to your accounting policy. Do not silently reduce the invoice allocation without recording the difference.

For card or marketplace settlements, one deposit may cover several Sales Invoices after fees and refunds. Use the reconciliation and allocation tools to connect the combined amount to the correct vouchers and record the settlement difference in the correct account.

For foreign currency, verify both statement currency and Company-currency accounting. Record exchange differences through the supported payment workflow rather than editing imported amounts.

## Troubleshooting

### The amount is in the wrong direction

Review import mapping. Incoming money belongs in Deposit and outgoing money in Withdrawal. Correct the mapping before importing more rows.

### The same statement line appears twice

Compare Transaction ID, reference, date, amount, and source file. Keep one valid transaction and remove or cancel the duplicate through your approved process.

### No matching Payment Entry appears

Check Bank Account and ledger, amount, date range, currency, party, document status, and whether the payment is already reconciled.

### A transaction remains partly unallocated

Review fees, deductions, combined payments, split vouchers, and rounding. Allocate only supported amounts and record the remaining difference explicitly.

### The imported list is empty

Confirm the file encoding, heading row, Bank mapping, date format, mandatory columns, and whether the import reported rejected rows.

## Frequently asked questions

### Does a Bank Transaction replace a Payment Entry?

It does not. The Bank Transaction is statement evidence. The Payment Entry normally posts the accounting movement and invoice allocation.

### Can I edit an imported amount?

Correct the source or import error before reconciliation. Preserve the original Bank evidence and avoid changing a valid statement value to force a match.

### Can one deposit pay several invoices?

It can. Match or create the Customer payment and allocate it across the relevant invoices using the supported reconciliation workflow.

## Related topics

- [Bank Account](/erpnext/bank-account)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Payment Entry](/erpnext/payment-entry)
- [Journal Entry](/erpnext/journal-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Data Import](/framework/user/en/guides/data/data-import)

<!-- page: erpnext/erpnext__bank.md -->
---
title: "Bank | ERPNext Documentation"
description: "Create an ERPNext Bank master and configure statement transaction mapping for a financial institution."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank"
updated: "2026-07-31"
---

A **Bank** identifies a financial institution in ERPNext. Bank Accounts, Bank Guarantees, statement mappings, and some integrations reference this master. Create one Bank record per institution, not one per account number.

## Before you begin

Collect the official Bank name, SWIFT or BIC code when applicable, website, and the statement-column names used by your import file. A Bank master does not create a General Ledger account. Create the ledger separately in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Create a Bank

1. Go to **Accounting &gt; Banking &gt; Bank**.
2. Select **Add Bank**.

![Bank list with Add Bank highlighted](https://novacompanies.m.frappe.cloud/files/banking-02-bank-list.png)

3. Enter the Bank name. Use the full institution name so users can distinguish it from similarly named banks.
4. Enter the **SWIFT number** and **Website** when they are relevant.

![SWIFT number and website on the Bank master](https://novacompanies.m.frappe.cloud/files/banking-03-bank-details.png)

5. Save the Bank.
6. Create one or more [Bank Accounts](/erpnext/bank-account) linked to it.

## Important fields and what they mean


| Field                    | What it controls                                                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| Bank Name                | The institution name shown on linked Bank Accounts and banking records.                                                     |
| SWIFT number             | The Bank Identifier Code used for international payment instructions. It does not replace the account number.               |
| Website                  | The institution's public website for reference. Do not store a private online-banking URL.                                  |
| Bank Transaction Mapping | Maps statement columns to ERPNext Bank Transaction fields for supported import flows.                                       |
| Plaid Access Token       | Supports the Plaid integration where configured. Treat integration credentials as secrets and follow the integration setup. |


## Configure Bank Transaction Mapping

Use mapping when the bank statement headings do not match the names expected by ERPNext.

1. Open the Bank record.
2. Expand the statement or Data Import configuration section.
3. Add one row for each required Bank Transaction field.
4. Enter the exact column heading used by the statement file.
5. Save, then test with a small statement.

Typical mappings cover date, deposit, withdrawal, description, reference number, transaction identifier, and party details. Do not map two different source columns to the same target without confirming how the importer handles them.

The mapping belongs to the Bank because different institutions export different layouts. If one institution provides several incompatible statement formats, standardize the files before import or document the supported format clearly.

## Next steps

After saving the Bank:

- create the Bank-type Account in the Company Chart of Accounts;
- create the Company Bank Account and link the ledger;
- create party Bank Accounts when Customer or Supplier banking details must be stored;
- configure a [Mode of Payment](/erpnext/mode-of-payment) for receipts and payments;
- test [Bank Transaction](/erpnext/bank-transaction) import and [Bank Reconciliation](/erpnext/bank-reconciliation).

You can also create linked Bank Accounts or Bank Guarantees from the Bank dashboard.

## Troubleshooting

### The Bank does not appear in Bank Account

Confirm that the Bank record was saved and that the name has not been disabled or renamed during another user's session.

### Imported columns are blank or shifted

Compare the statement headings with the Bank Transaction Mapping. Check whitespace, capitalization, date format, amount direction, and whether the file includes extra heading rows.

### SWIFT validation fails downstream

Use the official BIC supplied by the institution. A SWIFT code normally identifies the Bank, while the account number or IBAN identifies the account.

### Should branches be separate Bank masters?

Usually they should not. Use branch and account identifiers on the Bank Account unless the institutions operate as genuinely separate banks in your process.

## Frequently asked questions

### Can several Company Bank Accounts use the same Bank?

They can. Create separate Bank Account records for each real account and link all of them to the same Bank master.

### Does deleting a Bank remove bank transactions?

Linked records normally prevent deletion. Disable or retain the master when historical transactions depend on it.

### Should login credentials be stored in the Bank record?

They should not. Use the supported integration settings and secret-management approach. Never place usernames, passwords, or tokens in public notes.

## Related topics

- [Bank Account](/erpnext/bank-account)
- [Bank Transaction](/erpnext/bank-transaction)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Guarantee](/erpnext/bank-guarantee)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Mode of Payment](/erpnext/mode-of-payment)

<!-- page: erpnext/erpnext__banking-in-erpnext.md -->
---
title: "Banking in ERPNext | ERPNext Documentation"
description: "Set up bank accounts, import statement transactions, record payments, and reconcile bank activity in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/banking-in-erpnext"
updated: "2026-07-31"
---

ERPNext banking connects your bank statement activity with accounting entries. The workflow has four parts: create the Bank and Bank Account masters, record or import Bank Transactions, create the corresponding payments or journals, and reconcile both sides.

![Bank Transactions with realistic deposits and withdrawals](https://novacompanies.m.frappe.cloud/files/banking-01-banking-overview-transactions.png)

## Before you begin

Set up the Company [Chart of Accounts](/erpnext/chart-of-accounts) and create a ledger with **Account Type** set to **Bank**. You also need appropriate receivable, payable, expense, income, and clearing accounts.

Decide who can:

- maintain Bank and Bank Account masters;
- import statements or synchronize a connected bank;
- create and submit [Payment Entries](/erpnext/payment-entry);
- reconcile statement lines;
- cancel or unreconcile completed matches.

Separate these permissions when your control process requires independent preparation and review.

## Understand the banking records


| Record              | Purpose                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| Bank                | Identifies the financial institution and optional statement-import mapping.                      |
| Bank Account        | Connects a real account to a Company ledger or to a Customer or Supplier.                        |
| Bank Transaction    | Stores one imported or synchronized statement line. It does not replace the accounting voucher.  |
| Payment Entry       | Records money received, paid, or transferred and posts the General Ledger.                       |
| Journal Entry       | Records banking adjustments that do not belong in a Payment Entry.                               |
| Bank Reconciliation | Matches Bank Transactions with accounting vouchers and identifies missing or unmatched activity. |


The Bank Transaction is the statement side of the workflow. The Payment Entry or Journal Entry is the book side. Reconciliation connects them so the ERPNext bank ledger can be compared with the bank statement.

## Set up banking

1. Create a [Bank](/erpnext/bank) for each financial institution.
2. Create a Bank-type ledger account for each Company bank account in the Chart of Accounts.
3. Create a [Bank Account](/erpnext/bank-account) and connect the Bank, Company, and ledger.
4. Mark the correct Company Bank Account as default when appropriate.
5. Map Bank statement columns when you use a statement format that requires custom mapping.
6. Configure [Modes of Payment](/erpnext/mode-of-payment) so each Company uses the correct bank or cash ledger.

Do not use one Bank Account record for several real accounts. Separate accounts make statement import, matching, balances, and access control easier to audit.

## Record money movements

Use a Payment Entry for most receipts, payments, and transfers:

- **Receive** for Customer receipts and other incoming amounts;
- **Pay** for Supplier payments and other outgoing amounts;
- **Internal Transfer** to move money between Company cash or bank accounts.

Create payments from the relevant invoice when possible. This carries the party, account, currency, and reference into the payment and reduces manual allocation.

Use a [Payment Request](/erpnext/payment-request) when you need to request online or portal payment. Use a [Payment Order](/erpnext/payment-order) to organize several payable documents for bank processing.

## Bring in bank statement activity

Bank Transactions can come from:

- a supported bank integration;
- statement import;
- Data Import or API integration;
- controlled manual entry for testing or correction.

Each transaction records a date, deposit or withdrawal, description, reference, transaction identifier, currency, and Bank Account. Preserve the bank's original identifiers because they support duplicate detection and audit tracing.

Use [Bank Transaction](/erpnext/bank-transaction) mapping on the Bank master when imported column names differ from ERPNext's expected fields. Test a small statement before importing a full period.

## Reconcile the bank

Open [Bank Reconciliation](/erpnext/bank-reconciliation) for the Company Bank Account and statement period. ERPNext compares unreconciled Bank Transactions with Payment Entries and Journal Entries.

For each statement line:

1. Match it with an existing voucher when the amount, date, party, and reference agree.
2. Create the missing Payment Entry or Journal Entry only after you identify what the statement line represents.
3. Allocate the amount when one bank line covers several references.
4. Review bank fees, exchange differences, withholding, deductions, and other differences separately.
5. Confirm the ending statement balance and unresolved items.

Do not create a new payment merely because ERPNext does not suggest a match. Search existing vouchers first to avoid duplicate accounting.

## Other banking facilities

Use [Bank Guarantee](/erpnext/bank-guarantee) to track guarantees received from or provided through a bank, including validity, beneficiary, amount, margin, and charges.

Use [Invoice Discounting](/erpnext/invoice_discounting) when unpaid Sales Invoices are assigned as collateral for short-term financing. This requires deliberate account setup and should be reviewed by the finance team before submission.

## Controls and review

Review these regularly:

- unreconciled Bank Transactions;
- old uncleared payments and checks;
- duplicate transaction identifiers;
- Bank Accounts without a valid Company ledger;
- statement balance against the General Ledger;
- stale guarantees and financing arrangements;
- entries created directly in the bank ledger without an appropriate voucher.

The [Payment Ledger](/erpnext/payment-ledger) helps trace allocations between invoices, payments, and credit documents. The General Ledger shows the accounting effect, while Bank Reconciliation explains the difference between the ledger and statement timing.

## Troubleshooting

### A statement line does not find a match

Check the Bank Account, Company, amount direction, date range, currency, party, reference number, and whether the voucher is already reconciled.

### The bank balance differs from the statement

Confirm the statement period and opening balance, then review uncleared vouchers, missing statement lines, duplicate imports, bank fees, interest, and entries posted to the wrong ledger.

### The wrong ledger is selected in a payment

Review the Mode of Payment Company defaults, Company default Bank Account, and the selected Bank Account. Correct the configuration before creating more transactions.

### A Bank Transaction was imported twice

Do not reconcile both copies. Confirm the original transaction identifier and remove or cancel the duplicate using your approved process.

## Frequently asked questions

### Does importing a Bank Transaction post the General Ledger?

It does not by itself. The accounting effect normally comes from a Payment Entry, Journal Entry, or another voucher matched to the statement line.

### Must every payment be reconciled immediately?

Not necessarily. A payment can be submitted before it clears the bank, but the reconciliation should be completed as part of the regular close process.

### Can Customer and Supplier bank accounts be stored?

They can. Create party Bank Accounts separately from Company Bank Accounts and identify the Party Type and Party.

## Related topics

- [Bank](/erpnext/bank)
- [Bank Account](/erpnext/bank-account)
- [Bank Transaction](/erpnext/bank-transaction)
- [Payment Entry](/erpnext/payment-entry)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Payment Ledger](/erpnext/payment-ledger)

<!-- page: erpnext/erpnext__batch-split.md -->
---
title: "Batch Split"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/batch-split"
updated: "2026-08-28"
---

Turn one big batch of material into many small, individually traceable batches, one per piece you cut from it.

## The story: cutting a 50 KG rod

Your factory buys a 50 KG iron rod. It arrives as **one batch**, one purchase, one quality certificate, one batch number. On the shop floor you cut it into **five pieces of 10 KG each**, and from that moment the pieces live separate lives: they go into different machines, different orders, maybe different customers.

If all five pieces keep the rod's single batch number, you lose track of them individually. Batch Split fixes this: at the moment of cutting, ERPNext automatically creates **one new batch per piece**, and every new batch remembers which rod it came from.

```
BCH-000001  Iron Rod · 50 KG
     │
     ✂  cut into pieces of 10 KG
     │
     ├─ BCH-000002  10 KG
     ├─ BCH-000003  10 KG
     ├─ BCH-000004  10 KG
     ├─ BCH-000005  10 KG
     └─ BCH-000006  10 KG
```

Each piece gets its own batch number from the item's normal batch series. Each one records BCH-000001 as its **parent batch**, so a complaint about any piece traces back to the exact rod, its supplier, and its purchase receipt.

## When to use this feature

Use Batch Split whenever bulk material is **physically divided into pieces** and you need to follow each piece on its own:

- Metal rods, bars, or pipes cut to length
- Steel or paper coils slit into smaller coils
- Fabric or film rolls cut into shorter rolls
- Timber planks cut from a log

It is **not** meant for mixing or blending (many inputs becoming one output), or for items you don't track by batch at all.

## Before you start

On the **Item** that represents the cut piece (the output), enable:


| Item setting                       | Why                                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| **Has Batch No**                   | Pieces are tracked by batch.                                                   |
| **Automatically Create New Batch** | ERPNext creates the piece batches for you at the moment of cutting.            |
| **Batch Number Series**            | New piece batches are numbered from the item's own series, e.g. `BCH-.######`. |


The raw material you cut (the rod) must also be a batch-tracked item, so the system knows exactly which rod each piece came from.

## Way 1 - As a step in manufacturing

Use this when cutting is one operation inside a production process, for example, an operation called *Rod Cutting* in the routing of a machined part.

1. **Open the BOM** and enable **Track Semi Finished Goods**, so each operation produces its own output item.
2. **On the cutting operation row**, tick **Batch Split** and set **Weight Per Piece** — for our rod, **10**.
3. **Run production as usual**: create the Work Order, then the Job Card for the cutting operation. Both carry the Batch Split settings automatically.
4. **Complete the Job Card** and make its Stock Entry. Raw material consumption and the produced quantity stay exactly as they always are — producing 50 still consumes 50.
5. **Submit.** ERPNext divides the produced quantity by Weight Per Piece (50 ÷ 10 = 5) and creates five batches of 10 each, every one linked to its parent rod batch.

> **Good to know:** Weight Per Piece only controls how the **output is batched**. It never changes how much raw material is consumed, that still follows your BOM quantities.

## Way 2 - A manual split from the stores

Use this when there is no production order, the storekeeper simply cuts a rod and wants the pieces on the shelf as separate batches.

1. **Create a Stock Entry** and choose the type **Batch Split** (it comes built in, with purpose *Repack*).
2. **Set Weight Per Piece** — the field appears as soon as you pick the Batch Split type.
3. **Add two rows**: the rod being consumed (source warehouse, quantity 50) and the piece item being produced (target warehouse, quantity 50, marked as the finished item).
4. **Submit.** Five 10-unit batches are created and put into stock, each pointing to the rod it was cut from.

## What the system checks for you


| Rule                                                                                                                             | Example                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| The produced quantity must divide evenly by Weight Per Piece.                                                                    | 50 ÷ 10 = 5 pieces ✓ · 55 ÷ 10 is rejected.                                                                   |
| Exactly one batch-tracked raw material may be consumed, so the parentage is unambiguous.                                         | Cutting consumes rod only — not rod and coil together.                                                        |
| Each consumed batch must be able to supply **whole** pieces. A piece is always cut from one rod — never glued together from two. | Two 25 KG rods can yield four whole 10 KG pieces, not five. Asking for five is rejected with a clear message. |
| When several rods are consumed, the pieces are shared out in proportion to what each rod supplied.                               | Rods of 30 KG and 20 KG making five pieces → 3 pieces from the first, 2 from the second.                      |


## Tracing a split afterwards

Open any batch that was part of a split and you'll see a **Batch Split Tree** button. It opens a report showing the full family, top down — the original rod at the root, its pieces indented below, and any further cuts below those:

```
BCH-000001   Iron Rod        50 KG   ← the purchased rod
├─ BCH-000002   10 KG
├─ BCH-000003   10 KG
│  ├─ BCH-000007    5 KG   ← this piece was cut again
│  └─ BCH-000008    5 KG
├─ BCH-000004   10 KG
├─ BCH-000005   10 KG
└─ BCH-000006   10 KG
```

Every batch has exactly **one** parent, because every physical piece was cut from one physical rod. A piece cut again simply becomes a parent itself — the tree can go as deep as your process does.

## If a split entry is cancelled

Cancelling the Stock Entry reverses the stock movement, but the created batch records are kept, this is standard ERPNext behaviour for automatically created batches. They hold no stock, they disappear from the Batch Split Tree, and they don't get in the way. Simply make a fresh entry to split again.

<!-- page: erpnext/erpnext__batch.md -->
---
title: "Batch"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/batch"
updated: "2026-03-06"
---

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

To enable serial / batch feature for the item, first check the 'Enable Serial and Batch No for Item' checkbox in the 'Stock Settings'.

![](/files/Screenshot 2026-03-06 at 11.52.18 AM.png)



**Batch feature in ERPNext allows you to group multiple units of an Item and assign them a unique value/number/tag called Batch No.**

This is done based on the Item. If the Item is batched, then a Batch number must be mentioned in every stock transaction. Batch numbers can be maintained manually or automatically. This feature is useful to set the expiry date of multiple Items or move them together to different Warehouses.

To access the Batch No list, go to: > Home > Stock > Serial No and Batch > Batch

1. Prerequisites

---

Before creating and using a Batch, it is advised that you create the following first:

- [Item](/erpnext/item)
- Enable 'Has Batch No' in the Item master ![Batch No Enabled](/files/batch-no-enabled.png)

2. How to create a new Batch

---

To set item as a batch item, "Has Batch No" field should be checked in the Item master. If you have not selected "Automatically Create New Batch" when creating an Item, you will have to make Batches Manually as you go along.

To create new Batch No. master for an item, go to:

1. Go to the Batch list, click on New.
2. Set the Batch ID.
3. Select the Item.
4. If any transaction is done with an item, the batch cannot be set or unset.
5. Save.

When Batches are enabled for an Item, the option to [retain sample stock](/erpnext/retain-sample-stock) also becomes available.

### 2.1 Batch Auto Creation

If you want automatic batch creation at the time of Purchase Receipt, you must tick 'Automatically Create New Batch' in the Item master:

![Item Setup for Batches](/files/item_setup_for_batch.png)



3. Features

---

### 3.1 Splitting and Moving Batches

When you open a batch, you will see all the quantities that belong to that batch on the page.

![Batch View](/files/batch_view.png)



- To move the batch from one Warehouse to another, you can click on the **Move** button.
- You can also split the batch into smaller one by clicking on the **Split** button. This will create a new Batch based on this Batch and the quantities will be split between the batches.

![Split Batch](/files/batch_split.png)

- If you set expiry date, the Batch will show 'Not Expired' until the expiry date, after which it'll show 'Expired'. If a date is not set, the Batch will show 'Not Set'.

### 3.2 Transacting Items with Batches

A Batch master should be created before the creation of Purchase Receipt. Hence, every time a Purchase Receipt or Work Order is being made for a batch item, you will first create its Batch No, and then select it in the Purchase order or Stock Entry.

On every stock transaction (Purchase Receipt, Delivery Note, Invoice) with a batch item, you should provide the Item's Batch No.

> Note: In stock transactions, Batch IDs will be filtered based on Item Code, Warehouse, Batch Expiry Date (compared with a Posting date of a transaction) and Actual Qty in Warehouse. While searching for Batch ID without value in the Warehouse field, Actual Qty filter won't be applied.

### 4. Related Topics

1. [Serial Number](/erpnext/serial-no)
2. [Opening Stock Balance Entry For Serialized And Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
3. [Managing Batch Wise Inventory](/erpnext/managing-batch-wise-inventory)

<!-- page: erpnext/erpnext__bill-of-materials.md -->
---
title: "Bill Of Materials"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bill-of-materials"
updated: "2026-08-19"
---

**A Bill of Materials is a list of items and sub-assemblies with quantities required to manufacture an Item.**

A BOM may also contain the manufacturing operations required to manufacture the Item.

A **Bill of Materials** (BOM) is at the heart of the Manufacturing system and the most important document that will help to create other document types like Work Orders and Job Cards. ERPNext supports multi-level BOM. To know more, visit [this page](/erpnext/managing-multi-level-bom).

The **BOM** is a list of all materials (either bought or made) and operations  
that go into manufacturing a finished product or sub-assembly. In ERPNext, each item (sub-assembly) could  
have its own BOM hence forming a tree of Items with multiple levels.

![Work Order](/files/manufacturing-flow-bom.png)

To make accurate Purchase Requests, you must always maintain correct BOMs.

To access the BOM list, go to:

> Home &gt; Manufacturing &gt; Bill of Materials &gt; Bill of Materials

> Note that once a BOM is submitted, it cannot be edited. You can only cancel the existing, duplicate it and submit another one. A BOM is also linked to multiple places in the Manufacturing module, so making changes to it can be time-consuming and tedious. Hence it is a good practice to carefully think and fill out the BOMs before submitting.

## 1. Prerequisites

Before creating and using a BOM, it is advised that you create the following first:

- [Item](/erpnext/item)
- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)
- [Routing](/erpnext/routing)

## 2. How to create a Bill of Materials

1. Go to the Bill of Materials list, click on New.
2. Select the Item to be manufactured. The Item name, UoM, company, and currency will be fetched automatically.
3. Enter the quantity of the Item that will be manufactured from this Bill of Materials.
4. Under the Items table, select the raw materials (Items) required to manufacture the Item. Then proceed to:
  1. Select the quantity of Raw Material used.
  2. Set an Item operation here to be fetched in Work Orders later.
  3. If this Item is a sub-assembly, the default BOM for it will be fetched.
  4. Select the Source Warehouse to track inventory.
  5. Enter the scrap percentage that will remain after this raw material is used.  
  BOM Materials\](/files/bom-materials.png)
5. Under the Scrap section, select the scrap Item that will be created when manufacturing and its quantity. The scrap Item can also have a Rate if it is a by-product and not waste. Skip this section if 100% of raw materials are completely utilized. If the scrap Item is the same as the Item to be manufactured, it is set as a Process Loss Item and its quantity is subtracted from the manufactured Item quantity.  
![](/files/imageb61113.png)  
:::note  
**In ERPNext v16, the Scrap Items table has been replaced with Secondary Items. Read more about it here.**  
:::
6. Save and Submit.

In the Items table, you'll see an option 'Include Item in Manufacturing'. Raw Materials need to have this checkbox ticked. In case there are Operations or services you need to include in the BOM that are not necessarily an Item used for manufacturing, uncheck this checkbox. For example, treating the plastic with a chemical involves some cost but it is not an Item and the cost needs to be tracked.



![Task](/files/bom-item-include.png)

### 2.1 **Consume Components Based On**

“Consume Components” in ERPNext automates raw material consumption when a Work Order is completed, reducing the need for manual inventory updates. It consumes stock automatically based on either the Bill of Materials (BOM) or actual material transfers, making it ideal for high-volume, standardized production environments that aim to improve inventory accuracy and minimize manual data entry. 

![](/files/Screenshot 2026-04-20 at 3.21.01 PM.png)

- **Consumption Methods:**
  - **BOM:** Automatically consumes raw materials based on the quantities defined in the BOM, multiplied by the finished goods quantity.
  - **Material Transferred for Manufacture:** Consumes only the materials that are physically transferred to the shop floor (Work In Progress Warehouse) through a stock entry.

If you want to set default "**Consumption Components Based On**" instead of BOM wise, set the "Backflush Raw Materials Based On" in the Manufacturing Settings.

### 2.2 Bill of Materials with Operations

To add [Operations](/erpnext/operation) tick the 'With Operations' checkbox. Now, an Operations table can be seen. This option is useful for tracking the costing of various Operations performed to manufacture the [Item](/erpnext/item). Operations can be added easily by setting a template with the [Routing](/erpnext/routing) master.

![Task](/files/bom-operations.png)

1. In the “Operations” table, add the operations that need to be performed to manufacture this particular Item.
2. For each operation, you will be asked to enter a [Workstation](/erpnext/workstation) where the Operation will be performed. A default Workstation can be set from the [Operation](/erpnext/operation) document.
3. Enter the Operating Hourly Rate, Operation Time in minutes, and the Batch Size created with the Operation. The Operating Cost will be calculated based on these values.

> Note: Workstations are defined only for product costing and Work Order Operations scheduling purposes not tracking inventory. Inventory is tracked in [Warehouses](/erpnext/warehouse) set in the Items table of the BOM.

Transfer Material Against needs to be set for a BOM With Operations. Materials can be transferred against a [Work Order](/erpnext/work-order) in bulk or individual [Job Cards](/erpnext/job-card). Changing this affects whether the 'Material Transfer for Manufacture' is done against the Work Order at once or multiple times against the individual Job Cards. Setting this option depends on factors like time taken to manufacture the item, value of the items manufactured, number of parts used in manufacturing, the skill of your labor involved, etc.

![BOM transfer materials against](/files/bom-transfer-materials.png)

### 2.3 Additional options when creating a Bill of Materials

- **Is Active**: An Item could also be manufactured using an alternate set of materials/operations. In that case, uncheck this checkbox to disable this BOM and use another one.
- **Is Default**: This BOM will be selected by default in Work Orders etc. when the Item selected.
- **Inspection Required**: This will make 'Quality Inspection' mandatory for raw materials and the finished goods. Select the Quality Inspection Template after ticking this checkbox.
- **Allow Alternative Item**: Sometimes when manufacturing a finished good, specific materials may not be available. If you tick this, you can create and select an alternative item from the Item Alternative list. For example, using plastic beads instead of plastic crystals. For more details visit [this page](/erpnext/item-alternative).
- **Allow Same Item Multiple Times**: In some manufacturing cases, the same item needs to be added twice. For example, two metal pipes of length 0.5m each to form another shape. Here the quantity cannot be simply set to 2 and be done since the UoM will show 1m as total but we need 0.5m + 0.5m in the form of two pipes for production. Ticking this checkbox allows you to select the same item multiple times.
- **Set rate of sub-assembly item based on BOM**: Enabling this checkbox will set the rate of sub-assembly items based on their BOMs. If unchecked, the rate will be fetched from the Valuation Rate of the sub-assembly Item. Incase of Phantom Item, this setting is ignored and valuation rate of the phantom item will always be based on the contents of its BOM.
- **Is Phantom BOM**: If this is checked, it means that this BOM does not produce any item. Instead, it is only a logical grouping of raw materials. The Production Item in this BOM should be a non-stock item. If this non-stock item is added as a "raw material" in any other BOM, the BOM will be exploded automatically regardless if explosion or multi-level BOM is enabled or not.
- **Rate Of Materials Based On**: The Rate of raw materials used can be calculated based on different parameters.
- **Valuation Rate**: The Valuation Rate set in the [Item master](/erpnext/item).
- **Last Purchase Rate**: The Rate is fetched from the last Sales [Order](/erpnext/sales-order)/[Invoice](/erpnext/sales-invoice).
- **Price List**: The Rate will be fetched from the [Item Price](/erpnext/item-price).  
 For more details, visit [this page](/erpnext/valuation-based-on-field-in-bom).

## 3. Features

### 3.1 BOM Costing

The Costing section in a BOM gives an approximate cost of manufacturing the Item.

The costing is calculated from the Valuation Rate of the raw materials/sub-assemblies involved and the Operation costs.

![Costing](/files/bom-costing.png)

In case the BOM was submitted when the costs for Items/Operations were not updated, you can update the costs using the **Update Cost** button. This will fetch the latest price/costs.

![Update Cost](/files/bom-update-cost.png)

The BOM cost can also be set to be updated automatically via Manufacturing Settings, 'Update BOM Cost Automatically' option.

### 3.2 Materials Required (Exploded)

This table lists down all the raw materials required to manufacture an Item. It also fetches raw materials for the sub-assemblies/phantom items along with the quantities. The non-exploded table will not list the raw materials required for producing the sub-assemblies.

For example, to manufacture a plastic shaving brush you need some raw materials and the bristles as a sub-assembly. For the handle, you manufacture your own plastic, but for the bristles, you use raw plastic crystals.

![Exploded Section](/files/bom-exploded.png)

#### 3.2.1 Do Not Explode

If user wants to exclude the exploded items then they have to enable the checkbox "Do Not Explode" in the BOM Item table. This option is made read only and is unchecked by default if Item is a Phantom Item.

##### Use Case:

- Laptop
- Motherboard (Kept in stock)
- Keyboard

A company manufacture the Laptop which required two sub-assembly items as Motherboard and Keyboard. The company does the manufacturing once they received the order from the customer. The Manufacturing Time required for the Motherboard is more than the Keyboard, therefore the company does the manufacturing of the Motherboard individually irrespective of the sales orders and kept in the stock. As the item Motherboard is already in stock it helps to reduce the overall Manufacturing Time of the main item Laptop.  
Now while preparing the BOM for the Laptop in the ERPNext, they don't want to Explode the BOM of the item Motherboard but they want to Explode the BOM of the item Keyboard. Therefore we have added the checkbox "Do Not Explode" for the BOM Item. With this user will enable the checkbox "Do Not Explode" for the item Motherboard and not for the item Keyboard.

![Exploded Section](/files/dont_explode_items.png)

### 3.3 Project and Website

The BOM can be linked to a [Project](/erpnext/project) to track progress, Project costing, etc. In case of engineer to order, every order could be a [Project](/erpnext/project) and the sub-assemblies would be [Tasks](/erpnext/tasks). The completion can be tracked by linking to a Project in that case.

The BOM can also be shown in the [Website](/erpnext/website) for Open-source hardware products. Open-source hardware is similar to open-source where the product specifications are listed publicly.

### 3.4 BOM Template

![BOM Template](/files/bom-template.png)

With BOM template you can create BOMs for template items (against which you create variant items). These BOMs can be used as the default BOM while making Work Orders against the template Item's variants. You can also add the template items as raw materials in the template BOM. While making Work Order from the BOM Template, ERPNext gives provision to select the Item Variant against the template Item, for more details check following screenshot.

![Variant Selection](/files/variant-selection-against-template.png)

The user can also make the BOM for the variant item using the template BOM. To make the variant BOM:

- Go to the BOM Template.
- Click on **Create** button.
- Click on Variant BOM.
- Select the Variant Item for which you want to make the BOM.
- If the raw materials in the BOM is a template Item, then system gives provision to select the Item Variant.

![Variant BOM](/files/variant-bom.png)

### 3.5 After Submitting

Once the BOM is submitted, the following document types can be created against the BOM from the Dashboard:

![BOM submit](/files/bom-submit.png)

## 4. **Set Component Quantities Based On Percentage**

- A **Percentage (%)** column appears in the Items table and **Qty** becomes read-only, each row's qty is derived as `percentage / 100 × output qty`, with UOM conversion applied when the component UOM differs from the BOM UOM.
- Percentages must total exactly 100%.
- One row can be marked **Is Balance Item**: it automatically absorbs the percentage remaining after all other rows, so users don't have to hand-balance decimals. Only one balance item is allowed, and the other rows must leave it a positive remainder.
- Every non-balance row must have a percentage mixed percentage/manual-qty BOMs are not allowed.
- Quantities are recomputed on every save, so changing the output qty rescales the whole recipe.

## Example

Output Qty 200 kg: coriander 40% → 80 kg, chilli 35% → 70 kg, turmeric marked as balance item → 25% → 50 kg (if not manually added).

![](/files/Screenshot 2026-08-19 at 12.17.49 PM.webp)

### 5. Related Topics

1. [Scrap Management](/erpnext/scrap-management)
2. [Material Consumption](/erpnext/material_consumption)
3. [Nested BOM Structure](/erpnext/managing-multi-level-bom)

<!-- page: erpnext/erpnext__blanket-order.md -->
---
title: "Blanket Order | ERPNext Documentation"
description: "Create Blanket Orders in ERPNext to manage long-term customer or supplier commitments, negotiated rates, validity, and released quantities."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/blanket-order"
updated: "2026-07-29"
---

A Blanket Order in ERPNext records a long-term commitment to buy or sell specified items within an agreed period and at negotiated rates. It does not deliver, receive, bill, or pay for goods by itself. Instead, it becomes the reference for multiple downstream transactions as quantities are released over time.

![Blanket Order with the selling party, validity period, company, committed items, quantities, rates, and ordered quantities.](/files/blanket-order-overview.webp)

## Before you begin

Create the relevant [Customer](/erpnext/customer) or Supplier, [Items](/erpnext/item), currencies, and agreed rates. Confirm the total committed quantity and validity period before entering the agreement.

## Create a Blanket Order

1. Go to **Selling &gt; Sales &gt; Blanket Order** and select **Add Blanket Order**.
2. Set **Order Type** to **Selling** for a customer agreement or **Purchasing** for a supplier agreement.
3. Select the Customer or Supplier.
4. Enter the **From Date** and **To Date**.
5. Add each Item, committed Quantity, Rate, and item-specific Terms and Conditions.
6. Save and submit the Blanket Order.

![The highlighted pencil icon opens the complete Blanket Order item row.](/files/blanket-order-item-pencil.webp)

When editing an item row, select the pencil icon to open the complete row editor. This is useful when the row contains more fields than the table shows.

![The Blanket Order item row with committed quantity, negotiated rate, ordered quantity, and item-specific terms.](/files/blanket-order-item-row.webp)

## Important fields and what they mean


| Field                | What it means                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------- |
| Order Type           | Determines whether the agreement is for Selling or Purchasing.                                              |
| Customer or Supplier | The party that made the commitment. The available field depends on Order Type.                              |
| From Date            | The first date on which the agreement is valid.                                                             |
| To Date              | The final date on which transactions should be created against the agreement.                               |
| Item Code            | The product covered by the agreement.                                                                       |
| Quantity             | The total quantity committed for the validity period.                                                       |
| Rate                 | The negotiated unit rate used when transactions are created from the Blanket Order.                         |
| Ordered Quantity     | The quantity already referenced by submitted downstream orders. Use it to monitor the remaining commitment. |
| Terms and Conditions | Item-specific commercial terms for the agreement.                                                           |


## Create transactions from a Blanket Order

After submission, use **Create** to generate the appropriate transaction:

- For a Selling Blanket Order, create a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).
- For a Purchasing Blanket Order, create a [Purchase Order](/erpnext/purchase-order).

You can create multiple transactions from the same Blanket Order. ERPNext updates the ordered quantity as linked orders are submitted, making it easier to compare the commitment with actual releases.

You can also select a Blanket Order from an eligible downstream transaction. Always check the mapped item, remaining quantity, rate, schedule date, warehouse, taxes, and terms before saving.

## Monitor the agreement

Use the Blanket Order dashboard to open linked Quotations, Sales Orders, and Purchase Orders. Compare the committed Quantity with Ordered Quantity for each line. The outstanding quantity is the portion that has not yet been released into submitted orders.

A Blanket Order does not replace operational planning. Each Sales Order or Purchase Order still needs its own delivery schedule, warehouse, taxes, and approval before it moves through the standard sales or buying cycle.

## Amend an agreement

If a submitted Blanket Order contains an incorrect party, period, item, quantity, or rate, cancel and amend it according to your permissions and audit policy. Review linked orders before changing the source agreement. Do not create a replacement merely to hide an existing transaction history.

## Status and completion

A draft remains editable. A submitted Blanket Order can be used to create downstream transactions. A cancelled Blanket Order cannot be used for new releases.

ERPNext may not automatically close an agreement when its period ends or its quantity is fully ordered. Use the dates, ordered quantities, dashboard, and internal review process to identify completed or expired commitments.

## Video explaining Blanket Order

![](/files/blanket-order-smooth.mp4)

## Frequently asked questions

### Can one Blanket Order create multiple Sales Orders?

Y

es. Create each release as a separate Sales Order until the commitment is fulfilled or the validity period ends.

### Can I use a Blanket Order for purchasing?

Y

es. Select Purchasing as the Order Type, choose the Supplier, and create Purchase Orders from the submitted record.

### Does a Blanket Order reserve stock?

1. It records a commercial commitment. Stock is reserved or moved only through the applicable downstream processes and settings.

### Why is Ordered Quantity not updated?

Check that the downstream order is submitted, linked to the correct Blanket Order and item row, and not cancelled.

### Can I use different rates in downstream orders?

The negotiated rate is mapped from the Blanket Order. Any change should follow your permissions and commercial approval process.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Quotation](/erpnext/quotation)
- [Purchase Order](/erpnext/purchase-order)
- [Terms and Conditions](/erpnext/terms-and-conditions)
- [Price List](/erpnext/price-list)

<!-- page: erpnext/erpnext__blog-post.md -->
---
title: "Blog Post\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/blog-post"
updated: "2026-02-28"
---


**A Blog Post is an article on your website.**

Blogs are a great way to share your thoughts about your business.
It helps keep your customers and readers updated on news related to your business.

In the age of the internet, writing assumes a lot of significance because when
people come to your website, they want to read about you and your product.

To access the Blog Post, go to:
> Home > Website > Blog > Blog Post

## 1. How to create a Blog Post

1. Go to the Blog Post list and click on New.
1. Enter the Title, Blog Category, Blogger, and the Content.
1. Enable Published and click on Save.

The Blog Intro is a short description of your blog that appears just after the
title and before the content.

![New Blog Post](/files/new-blog-post.png)

You can write your blog in Rich Text, Markdown, or HTML. If you want to write
simple content pages, Rich Text and Markdown are great options. Learn how to
attach images to your blog [here](/erpnext/web-page#images).

> Learn markdown in a few minutes at [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

![Blog Post in Markdown](/files/blog-post-in-markdown.png)
*Blog Post in Markdown*

View your Blog Post by clicking on **See on Website** in the sidebar.
![Blog Post](/files/blog-post.png)
*Blog Post*

Check the **Disable Comments** option if you'd like to disable the ability for readers to add comments to the current blog post.
![Blog Post](/files/blog-post-disable-comments.png)

![Blog Post](/files/blog-post-no-comments.png)
*Adding Comments Disabled*

## 2. Features

### 2.1 Blogger

Blogger is a user who can post blogs. To create a Blogger, go to:

**Home > Website > Blog > Blogger**.

You can mention a short bio about the blogger and also set an avatar here.

![Blogger](/files/blogger.png)
*Blogger*

The preview will be shown at the end of the blog post.
![Blogger Preview](/files/blogger-preview.png)
*Blogger Preview*

### 2.2 Blog Category

You can group your blogs into categories. To create a new Blog Category, go to:

**Home > Website > Blog > Blog Category**.

![Blog Category](/files/blog-category.png)
*Blog Category*

If you click on **See on Website** in the sidebar, you'll be redirected to a
list of blogs under that category.

![Blog Category - General](/files/blog-category-web-view.png)
*Blog Category - General*

### 2.3 Meta Tags

Meta tags are HTML tags which describe a page and its content to a search engine or a social media platform. A meta description provides a brief description of a webpage.

In HTML, the meta description tag will be written as follows:

```
 
 
```

Under the SEO section, you can add the meta description and image for your blog post. ERPNext will generate a preview of the blog when listed as a search result by Google.

If you leave this section empty, the blog introduction or the first 140 characters of the blog will be shown as the meta description. In the same way, if you leave the meta image empty, the first image in the blog will be selected.

![Google Search Preview](/files/blog-post-seo-meta.png)
*Blog Post Google Search Preview*

On submitting the blog, you can also preview how the blog will look when shared on a social media platform like Facebook or Twitter. To check this, use the debugging tools offered by the platforms:

- Facebook: [Sharing Debugger](https://developers.facebook.com/tools/debug/)

- Twitter: [Card Validator](https://cards-dev.twitter.com/validator)

- LinkedIn: [Post Inspector](https://www.linkedin.com/post-inspector/inspect/)

To check the post preview, simply enter the webpage/blog link in the tool:

![Facebook Sharing Debugger](/files/blog-post-facebook-debugger.png)
*Using Facebook's Sharing Debugger Tool*

Using these tools, you can optimize your blog post for sharing.

<!-- page: erpnext/erpnext__blogs.md -->
---
title: "Blogs"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/blogs"
updated: "2026-03-02"
---

Blogs in ERPNext provide a powerful platform for businesses to engage with their audience and share valuable insights to keep the audience informed about valuable updates. By publishing blogs in ERPNext, the users can easily create and publish content such as articles, news updates, tutorials, and case studies. The platform provides customisable templates and formatting options to enhance the visual appeal of blog posts and improve readability.

* [Blog Post](/erpnext/blog-post)

<!-- page: erpnext/erpnext__bom-comparison-tool.md -->
---
title: "BOM Comparison Tool\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-comparison-tool"
updated: "2026-02-27"
---


**Using the BOM Comparison Tool, you can compare two BOMs and see what changed between their iterations.**

A BOM ([Bill of Materials](/erpnext/bill-of-materials)) of an Item undergoes several changes over time. When you need to change something in your BOM, you have to Cancel the BOM, Amend it, make
the change and create a new version of the BOM. Now you have two different BOMs and
change history is lost.

The BOM Comparison Tool lets you compare two different BOMs and will show you
what changed between them.

To use the BOM Comparison Tool, go to:

> Home > Manufacturing > Tools > BOM Comparison Tool

## 1. How to use the BOM Comparison Tool

1. Select the old BOM against which you want to compare in **BOM 1** field.
2. Select the new BOM of which you want to see the changes in **BOM 2** field.
3. The changes will be shown as soon as you select both the values.

![BOM Comparison Tool](/files/bom-comparison-tool.png)

<!-- page: erpnext/erpnext__bom-costing-in-different-currency.md -->
---
title: "BOM Costing in different Currency\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-costing-in-different-currency"
updated: "2026-02-26"
---


User can change the Currency in the BOM *before* submitting. The system calculates the costing based on the Price List currency. You can check the manufacturing cost in a particular Currency by changing the Currency in the BOM.

Consider that you import plastic as a raw material from Japan and the Sales Invoices are in the Yen currency. Your company Currency is INR but you want the BOM costing to be done in Yen. On setting 'Rate Of Materials Based On' to 'Price List' the raw materials used in the BOM will also have rates set in Yen. These rates are fetched from the Price List you create for Japan. In this case, it is a buying Price List called 'Import Japan'.

![BOM in different Currency](/files/bom-currency.png)

If you select 'Rate Of Materials Based On' to 'Valuation Rate' or 'Last Purchase Rate', the prices will be fetched from the Item master or the Sales Invoice respectively. In case of Item master, you'll need to enter the Valuation Rate in **your** Currency. In the BOM, Valuation Rate will be converted to the Currency set in the BOM.

![BOM in different Currency](/files/bom-currency-1.png)

<!-- page: erpnext/erpnext__bom-creator-new.md -->
---
title: "Multi-level BOM Creator (New)"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-creator-new"
updated: "2 weeks before 2026-11-14"
fetched: "2026-11-14"
---

A BOM Creator builds a multi-level Bill of Materials (BOM) in one document. You can read the part tree from a 3D design file, or build the tree by hand. You map each part to an item and submit the document. Then the system creates all the BOMs of the product.

Engineers make the product design in a CAD tool. Without a design file, a user types the BOM into ERPNext again by hand. With a design file, the BOM Creator reads the assemblies, the parts and their quantities from the file. This removes the manual entry and keeps the BOM the same as the design.

You can make the BOMs in two ways:

- **Without Produce an Item at Each Operation:** the part tree is the BOM. Each assembly in the tree gets its own BOM.
- **With Produce an Item at Each Operation:** you add the operations that make the product. Each operation makes an item, and the last operation makes the finished good. The system makes one BOM with **Track Semi Finished Goods** turned on.

### **Why use the BOM Creator?**

Users often question why a separate BOM Creator is needed to create BOMs. The answer lies in eliminating the need for unnecessary back and forth. With the standard BOM screen, users are required to create all sub-assembly BOMs first and then create the BOM for the final product. This process often involves a lot of back and forth. Additionally, sometimes it's challenging to visualize the complete hierarchy using the standard BOM.

To open the list, go to:

> Home > Manufacturing > BOM Creator

## 1\. Prerequisites

Before you create a BOM Creator, prepare these:

1. Optional: a design file of the product. Use a STEP file (`.step` or `.stp`) or a CSV file. Most CAD tools can export an assembly as a STEP file.
2. [Operation](/erpnext/operation) and [Workstation Type](/erpnext/workstation-type) records. You need these only for **Produce an Item at Each Operation**.

Items are not necessary before you start. The system can create the items from the parts.

Note

The system uses the **Default Item Group** in **Stock Settings** for the items that it creates. You can change it in the **Item Group for New Items** field on the **Details** tab.

## 2\. How to create a BOM Creator

1. Go to the BOM Creator list and click **Add BOM Creator**.
2. In **Finished Good**, select the item that the design makes. This field is mandatory.
3. Make sure that **Company** is correct. The system fills it with your default company.
4. Attach the design file in the **Design File** field.
5. The system saves the document and reads the file.

If the STEP file is not complete or is damaged, the system shows the message "The STEP file is incomplete or damaged." Export the file from the CAD tool again.

If **Design Name** is empty, the system fills it with the item name of the finished good. You can change it. If you change the **Finished Good**, the **Design Name** changes with it, unless you typed a different name.

After you save, the form has three tabs:

- **Design:** the main fields, the 3D model and the part tree.
- **Costing:** how the system calculates the cost of the materials.
- **Details:** the other fields. See **Other fields** below.

After the system reads the file, the **Design** tab shows two panels with the same height:

- **3D model (left):** turn the model with the mouse. Zoom with the scroll wheel.
- **Part tree (right):** the top row is the finished good. Under it are the assemblies and the parts, with the quantity from the design file. The **Amount** column shows the cost of each row.

![](/files/bom-creator-tree.webp)

Click a row in the tree to highlight the part in the model. Click a part in the model to select its row in the tree.

### 2.1 Use a CSV file

If your CAD tool cannot export a STEP file, export the BOM as a CSV file. The CSV file must have these columns:

| Column | Necessary | Content |
| --- | --- | --- |
| **Level** or **Item Number** | Yes | The position of the part in the tree. Level 1 is a part directly under the finished good. An item number such as `1.2` means the second part under part `1`. |
| **Part Number** or **Part Name** | Yes | The part. If only one of the two columns is in the file, the system uses it for both. |
| **Quantity** | Yes | The quantity of the part in one unit of its parent. |
| **Description** | No | The description of the part. |

Example:

```csv
Level,Part Number,Part Name,Quantity
1,WB-FRM-ASM,Frame Assembly,1
2,WB-LEG-01,Square Tube Leg 50 x 50,4
2,WB-RAIL-L,Long Rail 40 x 40 x 1050,4
1,WB-SHELF-01,Plywood Lower Shelf 18 mm,1
```

A CSV file has no geometry. Thus the 3D model does not show. Enter the **Design Name** yourself.

### 2.2 Build the tree without a file

Leave the **Design File** empty and select the **Finished Good**. Click **+** on the finished good row and add the materials. Click **+** on a material to add materials under it. A material with materials under it becomes a sub-assembly, and it gets its own BOM.

If you leave the **Design Name** empty, the system uses the item name of the finished good.

## 3\. Map the parts to items

Each part in the tree needs an item before the system can create the BOMs. A part without an item shows **Map Item**.

### 3.1 Select an item

1. Click **Map Item** in the **Item** column. The field is a standard Item link field.
2. Type the item code or the item name.
3. Select the item from the list.

![](/files/bom-creator-map-item.webp)

Use the up and down arrow keys to go to the previous or the next row. The item list of that row opens. This lets you map a long tree with the keyboard only.

### 3.2 Create a new item

If the item does not exist, select **Create a new Item** in the item list. The **New Item** dialog opens with the part number in **Item Code** and the part name in **Item Name**. Click **Save**. The system maps the new item to the part.

![](/files/bom-creator-create-item.webp)

### 3.3 Map many parts at a time

After you submit the document, the **Map Items** menu shows two options:

- **Suggest Items:** maps each part to an item that has the same item code as the part number, or the same item name as the part name.
- **Create Missing Items:** creates an item for each part that has no item. Select the **Item Group** and the **Default Unit of Measure** in the dialog.

![](/files/bom-creator-map-items-menu.webp)_Suggest Items_

![](/files/bom-creator-create-missing-items.webp)_Create Missing Items_

### 3.4 Item images

When the system creates an item from a part, it takes a picture of that part from the 3D model. The picture becomes the item image. Each mapped row shows the image as a small picture.

To take the picture again, click **⋯** on the row and select **Set Item Image**. For a material that is not in the 3D model, select **Upload Item Image**. You can also click the small picture in the row.

![](/files/bom-creator-mapped.webp)

## 4\. Change the tree

You can change the tree before you create the BOMs. The changes apply to the BOMs only. The design file does not change.

Each row has three buttons at the end: **+** adds a material under the row, **×** removes the row from the BOM, and click on **⋯** (3 dots icon) opens more options. The buttons show while you can change the document.

### 4.1 Change a quantity

Click the quantity of a row and type the new quantity. A quantity is always for one unit of the parent row. A dot before the quantity shows that the quantity is different from the design file. Hold the pointer on the dot to see the quantity from the design file.

To make the finished good BOM for more than one unit, change the quantity on the top row. With **Produce an Item at Each Operation**, the tree does not show. Then use the **Finished Good Quantity** field on the **Design** tab.

### 4.2 Add a material

Some materials are not in the design file, for example glue, paint or packing. To add one:

1. Click **+** on the row of the assembly.
2. Type the item in the new row and select it. The new row stays open, so you can add the next material.
3. Click **×** at the end of the row to close it.

![](/files/bom-creator-add-material.webp)

### 4.3 Remove a part from the BOM

Click **×** on a row to remove the part from the BOM. A part from the design file stays in the tree with a line through it, because it is in the design. Click the **Add Back to BOM** button on the row to add it back. A material that you added by hand is deleted.

In this example, the **Galvanised Top Cover Sheet** is removed from the BOM. The **PVA Wood Glue** is a material added by hand, with a quantity of 0.25 Kg.

### 4.4 Change the unit of measure

Click the unit in the **UOM** column and select another unit of the item. The system takes the conversion factor from the item and calculates the stock quantity and the amount again when you save.

If two parts of one assembly have the same item but different units, the BOM gets one row for each unit.

### 4.5 Get items from an existing BOM

You can copy the items of an existing BOM of an item into the tree, and then change them. For example, use the BOM of a sub-assembly that you already make, and remove the items that the new product does not need.

1. Click **⋯** on the row of the finished good or of a part, and select **Get Items from BOM**.
2. In **BOM**, select a submitted BOM of the item. The default is the default BOM of the item.
3. To copy the items of the sub-assemblies too, select **Include Items of Sub-Assemblies**. Otherwise, each sub-assembly uses its own BOM, the same as with **Include Existing BOM**. See **Include an existing BOM** below.
4. Click **Get Items**.

With this feature user can remove items fetched from different BOMs, change the qty

### 4.6 Include an existing BOM

You can use the BOM of a sub-assembly that you already make. The system then does not make a new BOM for the sub-assembly. The BOM of the parent row uses the existing BOM.

1. Click **⋯** on the row of the part and select **Include Existing BOM**.
2. In **BOM**, select an active, submitted BOM of the item of the part. The default is the default BOM of the item.
3. Click **Include**.

With this feature user can not remove items fetched from different BOMs, also will not be able to change the qty

Note

**Include Existing BOM** shows only when **Produce an Item at Each Operation** is off. The tree shows the first level of items of the BOM. If you change the item of the part, the system removes the BOM from the part.

## 5\. Costing

The **Amount** column shows the cost of each row. The amount of an assembly is the cost of its raw materials. The line under the tree shows the **Total Cost** of the finished good. The system calculates the cost again when you save.

Set the costing fields on the **Costing** tab:

| Field | Use |
| --- | --- |
| **Rate Of Materials Based On** | **Valuation Rate**, **Last Purchase Rate** or **Price List**. The default is **Valuation Rate**. |
| **Price List** | Shows when the rate is based on a price list. |
| **Set Valuation Rate Based on Source Warehouse** | Takes the valuation rate of the **Default Source Warehouse**. |
| **Default Source Warehouse** | Shows when the rate is based on **Valuation Rate**. The system sets it on the BOMs as their default source warehouse. |
| **Currency** and **Conversion Rate** | The currency of the costs. The default is the company currency. |
| **Total Cost** | The cost of the materials of the finished good. |

### Other fields

The **Details** tab has these fields:

- **Is Phantom BOM:** makes the finished good BOM a phantom BOM. The finished good must then be a non-stock item.
- **Item Group for New Items:** the item group of the items that the system creates from the parts.
- **Part Number:** shows when a design file is attached. It is the part number of the top assembly in the file.
- **Project:** the system sets it on the BOMs.
- **Routing:** shows when **Produce an Item at Each Operation** is off. The finished good BOM gets its operations from this routing.
- **Remarks:** your notes about the design.
- **More Information:** a collapsed section with **Status**, **Revision**, **Previous Revision** and **Error Log**. Click the section title to open it. The section opens automatically when the BOM creation fails. For revisions, see **Revisions** below.

## 6\. Submit the document

When the tree is correct, click **Submit**. The status changes to **Submitted**.

After you submit the document, you can still map items, change quantities and units, and add or remove materials. You cannot change the design file. To use a new design file, make a new revision. See **Revisions** below.

## 7\. Create BOMs without Produce an Item at Each Operation

Keep **Produce an Item at Each Operation** off when the part tree is the structure that you make. This is the default.

When you click **Create BOMs**, the system:

1. Checks the tree and shows a list of all the problems. For example, a part without an item.
2. Sets the status to **In Progress** and creates the BOMs in the background.
3. Creates one BOM for each assembly in the tree. It starts with the lowest assemblies. A part that uses an existing BOM does not get a new BOM.
4. Uses the BOM of each sub-assembly in the BOM of its parent.
5. Creates the BOM of the finished good last.
6. Submits all the BOMs and sets the status to **Completed**.

The system does not add removed parts to the BOMs.

To click **Create BOMs**, you need the permission to submit a BOM Creator and a BOM.

Note

If two assemblies in the tree have the same item, they must have the same raw materials. The system makes one BOM for the item.

### Example

The design file of the Steel Workbench 1200 with Drawer has four assemblies. The Drawer Handle Assembly is inside the Drawer Assembly. The user adds the Corner Bracket and the PVA Wood Glue by hand.

The line under the tree shows **5 BOMs will be created**. Click **Create BOMs**. When the BOMs are ready, the status changes to **Completed**.

![](/files/bom-creator-completed.webp)

| BOM for | Raw materials |
| --- | --- |
| WB-FRM-ASM Frame Assembly | Square Tube Leg × 4, Leveling Foot × 4, Hex Bolt × 8, Long Rail × 4, Short Rail × 4, Corner Bracket × 4 |
| WB-TOP-ASM Top Assembly | Galvanised Top Cover Sheet × 1, Beech Worktop × 1, PVA Wood Glue × 0.25 Kg |
| WB-HANDLE-ASM Drawer Handle Assembly | Handle Bar × 1, Handle Post × 2 |
| WB-DRW-ASM Drawer Assembly | Front Panel × 1, Side Panel × 2, Back Panel × 1, Bottom Panel × 1, Drawer Slide × 2, Drawer Handle Assembly × 1 |
| WB-1200 Steel Workbench 1200 with Drawer | Frame Assembly × 1, Top Assembly × 1, Plywood Lower Shelf × 1, Drawer Assembly × 1 |

The **Connections** tab shows the BOMs that the system created.

The BOM of the finished good uses the four assembly items. Each assembly item links to its own BOM.

### If the BOMs are not created

If the system cannot create a BOM, the status changes to **Failed**. The page shows a message, and the **Error Log** field on the **Details** tab shows the error. The system keeps no BOM from the failed run. Correct the problem and click **Create BOMs** again.

If the background job stops without a result, for example because the worker restarted, the status stays **In Progress**. **Create BOMs** shows for this status too. Click it again after the job is no longer in the queue. If you cancel a BOMs that the system created, the status changes back to **Submitted**.

## 8\. Create BOMs with Produce an Item at Each Operation

Turn on **Produce an Item at Each Operation** when the product goes through a sequence of operations, and each operation makes an item that you track in stock. Examples are welding, painting and assembly.

In this mode:

- Each operation has raw materials and one output item.
- A later operation can use the output of an earlier operation as a raw material.
- The last operation makes the finished good.

The system makes one BOM for the finished good, with **Track Semi Finished Goods** turned on.

### 8.1 Turn on the option

Select the **Produce an Item at Each Operation** check box on the **Design** tab. The right panel changes and shows two tabs:

- **Operations:** the steps that make the finished good.
- **Parts:** the part tree, with the operation that uses each part.

Before you add operations, the **Operations** tab shows one **Raw Materials** card. The output of this card is the finished good. The **Parts Not Used in Any BOM** list shows the parts that no operation uses yet.

![](/files/bom-creator-operations-empty.webp)

If you clear the check box, the panel shows the part tree again.

### 8.2 Add an operation

1. Click **Add Operation**. A new step card shows at the end.
2. In the first field, select the **Operation**. The system fills the **Workstation Type** and the time from the Operation, if they are set there.
3. Select or change the **Workstation Type**.
4. Type the time in minutes.

![](/files/bom-creator-add-operation.webp)

To delete a step, click **×** at the end of its header.

### 8.3 Add raw materials to an operation

Use one of these methods:

- **Add raw material:** type an item in the field at the end of the raw materials and select it. If a part of the design has this item and no step uses the part yet, the system links the row to that part.
- **Parts Not Used in Any BOM:** in the list under the steps, select the step in the **Add to** field of a part.
- **Step Output:** click **\+ Step 1 Output** to use the output of step 1 as a raw material. The buttons show the outputs of the earlier steps that this step does not use yet.

Change the quantity in the row, or click **×** to remove the raw material.

### 8.4 Set the output item

Each step, except the last, needs an output item. Select it in the **Output** field. The output shows the **Semi-Finished** label. You can select an assembly of the design or any other item.

The output of the last step is always the finished good. It shows the **Finished Good** label.

Click a step card to highlight its raw materials in the 3D model.

### 8.5 Example

The Steel Workbench 1200 with Drawer is made in five operations:

| Step | Operation | Workstation Type | Time | Raw materials | Output |
| --- | --- | --- | --- | --- | --- |
| 1 | Welding | Welding Bay | 60 minutes | Square Tube Leg × 4, Long Rail × 4, Short Rail × 4, Leveling Foot × 4, Hex Bolt × 8 | Frame Assembly |
| 2 | Assembly | Assembly Bench | 20 minutes | Galvanised Top Cover Sheet × 1, Beech Worktop × 1 | Top Assembly |
| 3 | Assembly | Assembly Bench | 10 minutes | Handle Bar × 1, Handle Post × 2 | Drawer Handle Assembly |
| 4 | Drawer Assembly | Assembly Bench | 35 minutes | Front Panel × 1, Side Panel × 2, Back Panel × 1, Bottom Panel × 1, Drawer Slide × 2, Step 3 Output × 1 | Drawer Assembly |
| 5 | Final Assembly | Assembly Line | 45 minutes | Step 1 Output × 1, Step 2 Output × 1, Step 4 Output × 1, Plywood Lower Shelf × 1 | Steel Workbench 1200 with Drawer (finished good) |

Step 1 makes the Frame Assembly. A line under the card shows that a later step uses this output. In the image, step 1 is selected, so the model highlights its raw materials. The line under the steps shows the number of operations, the total time and the **Total Cost**.

![](/files/bom-creator-operations.webp)

The last step uses the outputs of steps 1, 2 and 4. Its output is the finished good.

![](/files/bom-creator-operations-last-step.webp)

The **Parts** tab shows the operation that uses each part. **Output of Welding** means that the Welding step makes this part.

![](/files/bom-creator-parts-tab.webp)

### 8.6 Give a sub-assembly its own BOM

You can make a sub-assembly in a separate BOM, for example when another work order or a subcontractor makes it.

1. Click the **Add Sub-Assembly BOM** button next to the BOM name above the steps.
2. Select the sub-assembly.
3. A new tab with the name of the sub-assembly shows. Add the operations and the raw materials of this BOM.

The system creates the BOM of the sub-assembly first. The BOM of the finished good uses it.

![](/files/bom-creator-sub-assembly-bom.webp)

### 8.7 Create the BOM

1. Submit the document.
2. Click **Create BOMs**.

The system shows a list of the problems if one of these is true:

- A part has no item.
- A step has no workstation type, no time or no output item.
- Two BOMs are for one item. The system can make only one BOM for an item.

Correct the problems and click **Create BOMs** again.

The system creates one BOM with **Track Semi Finished Goods** turned on. Each operation row has the **Output Item** of the step. The last operation makes the finished good. In the BOM, the output of an earlier step has **Do Not Explode** turned on, so the BOM does not use another BOM of that item.

![](/files/bom-creator-bom-operations.webp)

When you make a [Work Order](/erpnext/work-order) from this BOM, each Job Card makes the output item of its operation.

## 9\. Related Topics

1. [Bill of Materials](/erpnext/bill-of-materials)
2. [Operation](/erpnext/operation)
3. [Workstation Type](/erpnext/workstation-type)
4. [Routing](/erpnext/routing)
5. [Work Order](/erpnext/work-order)
6. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__bom-creator.md -->
---
title: "Multi-level BOM Creator"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-creator"
updated: "2026-02-26"
---

The BOM Creator enables users to create multi-level BOMs using a single screen.

![bom_creator_tree](/files/bom_creator_tree.png "bom_creator_tree.png")  


### Why use the BOM Creator?

Users often question why a separate BOM Creator is needed to create BOMs. The answer lies in eliminating the need for unnecessary back and forth. With the standard BOM screen, users are required to create all sub-assembly BOMs first and then create the BOM for the final product. This process often involves a lot of back and forth. Additionally, sometimes it's challenging to visualize the complete hierarchy using the standard BOM.

To address all of these problems, we have introduced the BOM Creator. Within the BOM Creator, users can construct a multi-level BOM using the tree component.

Here's how it works:

* The user selects the Final Product and saves the record.

![bom-creator](/files/bom-creator.png "bom-creator.png")  


* In the form, users will find an option to add Raw Materials and Sub-assembly items related to the Final Product.

![toolbar_bom_creator](/files/toolbar_bom_creator.png "toolbar_bom_creator.png")  


* If a user wants to convert Raw Materials into Sub-assembly items, they need to click on the item first and then click the "Convert to Sub-Assembly" button.

![convert_to_sub_assembly](/files/convert_to_sub_assembly.gif "convert_to_sub_assembly.gif")  


* Users can edit the Quantity as needed.

### Final Step

One the BOM structure has made using the tree component, user has to submit the BOM Creator. On Submission of the BOM Creator, system will generate the BOMs using the background job.

  


![submit-bom](/files/submit-bom.gif "submit-bom.gif")  

<!-- page: erpnext/erpnext__bom-operation-time.md -->
---
title: "BOM Operations Time\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-operation-time"
updated: "2026-02-26"
---


To access the BOM Operations Time, go to:

> Home > Manufacturing > Reports > BOM Operations Time

![Task](/files/bom-operations-time.png)

This report will give the information about the Bill of Material's total expected time in minutes as well the count of the current BOM used as a subassembly item for different Finished Goods.

<!-- page: erpnext/erpnext__bom-search.md -->
---
title: "BOM Search\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-search"
updated: "2026-02-26"
---


To access the BOM Search report, go to:

> Home > Manufacturing > Reports > BOM Search Report

![Task](/files/bom-search.png)

In this report, you can search for specific BOMs based on the Items (raw materials) used in them. This report is useful if you have hundreds or thousands of BOMs.

<!-- page: erpnext/erpnext__bom-stock-analysis.md -->
---
title: "BOM Stock Analysis"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-stock-analysis"
updated: "2026-03-26"
---

BOM Stock Analysis is a manufacturing report in ERPNext that tells you, for a given Bill of Materials (BOM), whether you have enough raw materials to fulfill a production run. 



The report operates in 2 modes: 

1. Detailed Mode - Based on the provided Fg Items to produce, it gives a detailed breakdown of availability, shortfall, and purchase rates  
2. Summarised Mode - Given the BOM and the warehouse, it gives you how much Fg you can actually produce 

To access the report: 

> *Home > Manufacturing > Reports > BOM Stock Analysis*

### Detailed Mode

This mode can be used when you have a set production target and want to know which raw materials are in stock, which are short, and what it would cost to bridge the gap.

:::note
Entering the value in the ***FG Item to make*** directly enters the detailed mode
:::



The maximum producible Item defines the maximum possible items producible based on the raw material availability. The green color indicates that it is possible to produce the FG item based on the Required Qty to make. The value turns red if the producible FG item is less than Required qty. 

![](/files/image0bb381.png)

### Summarised Mode 

This mode can be used for quick answers to questions like - "How many finished goods can we make right now?" without specifying the production target. To enter this mode, we leave the **Fg Item to Make** empty and define the warehouse and BOM. 

![](/files/image5f53bd.png)

<!-- page: erpnext/erpnext__bom-stock-report.md -->
---
title: "BOM Stock Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-stock-report"
updated: "2026-03-26"
---

:::caution
This Report is deprecated in V16, please refer to Bom Stock Analysis for the same
:::



To access the BOM Stock Report, go to:

> Home > Manufacturing > Reports > BOM Stock Report

![Task](/files/bom-stock-report.png)

The BOM Stock Report provides information about the raw materials required quantity and the in-stock quantity of the warehouse (which is selected in the filter). As you can see, the items which have insufficient quantity are shown in red and ones with enough quantity to manufacture the BOM Item are shown in green.

<!-- page: erpnext/erpnext__bom-update-tool.md -->
---
title: "BOM Update Tool\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom-update-tool"
updated: "2026-02-26"
---


**From the BOM Update Tool, you can replace a sub-assembly BOM and update costs of all parent BOMs.**

Using this utility, you can replace an existing BOM of a sub-assembly item which is linked to a parent BOM. The system will update the new BOM in all the parent BOMs where it was used. You need to create a new BOM first.

To use the BOM Update Tool, go to:

> Home > Manufacturing > Tools > BOM Update Tool

## 1. How to use the BOM Update Tool
Let's consider a scenario to understand this better.

Suppose a company manufactures computers, Bill of Materials for the computer will look like this:

1. Monitor
1. Key Board
1. Mouse
1. CPU

Out of all the items above, CPU is assembled separately. Hence separate BOM will be created for the CPU. Following are the items from the BOM of CPU.

1. 250 GB Hard Disk
1. MotherBoard
1. Processor
1. SMTP
1. DVD player

If more items need to be added, or existing items to be edited in the CPU BOM, then create new BOM for it.

1. _950 GB Hard Disk_
1. MotherBoard
1. Processor
1. SMTP
1. DVD player

Select Current BOM and New BOM of the **sub-assembly** Item:

![BOM Update Tool](/files/bom-update-tool.png)

To update the new BOM in all the parent BOMs, where CPU is selected as sub-assembly, you can use the **Replace** button.

On clicking Replace button, old BOM of CPU will be replaced with the new BOM in the BOM of finished Item (Computer).

**Will BOM Replace Tool work for replacing the exploded Items in the parent BOM?**

No, exploded Items which do not have any BOMs of their own cannot be replaced in the parent BOM. For example, consider if the Item Monitor does not have a sub-assembly and it cannot be updated using this tool. For updating exploded Items you should Cancel and Amend current BOM, or create a new BOM for the finished item.

## Update BOM Cost
Using the button **Update latest price in all BOMs**, you can update the cost of all Bill of Materials, based on the latest purchase price/price list rate/valuation rate of raw materials. This is useful if your updated BOM has materials with different Rates.

On clicking this button, the system will create a background process to update all the BOM's cost. It is processed via background jobs because this process can take a few minutes (depending on the number of BOMs) to update all the BOMs.

This functionality can also be executed automatically daily. For that, you need to enable "Update BOM Cost Automatically" from Manufacturing Settings.

<!-- page: erpnext/erpnext__bom_explorer.md -->
---
title: "BOM Explorer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bom_explorer"
updated: "2026-02-26"
---


BOM Explorer Report shows a complete hierarchy of the Bill of Materials (BOM) with its raw materials in the form of the tree view.

You need to select the BOM in the filter then the report will show the quantity of required raw materials and scraps for manufacturing the item. It is the complete tree view of assemblies, sub-assemblies i.e. all exploded items.

Using the BOM Explorer, user can view the quantity of raw materials and scraps from all exploded items and print it.

![reorder level](/files/bom_explorer.png)

<!-- page: erpnext/erpnext__book-discount-allowed-and-received-separately.md -->
---
title: "Book Discounts Allowed and Received Separately | ERPNext Documentation"
description: "Book discounts allowed and received in separate ERPNext accounts using negative charge rows, then verify invoice totals, ledgers, and net payments clearly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/book-discount-allowed-and-received-separately"
updated: "2026-08-03"
---

ERPNext normally records the net value of an invoice after commercial discounts. Use the workflow on this page when your accounting policy requires the discount to appear in a separate ledger account.

A **discount allowed** is a reduction that your Company gives a Customer. It is commonly recorded in an expense or contra-revenue account. A **discount received** is a reduction that a Supplier gives your Company. It is commonly recorded in an income or contra-expense account. Confirm the account classification with your accountant because presentation and tax rules vary by jurisdiction.

This page uses a negative row in the Sales or Purchase Taxes and Charges table. Despite the table name, ERPNext uses it for taxes and other additions or deductions. The negative row reduces the amount payable while posting the discount to the selected Account Head.


| Example          | Gross amount | Separate discount                             | Net amount due       |
| ---------------- | ------------: | ---------------------------------------------: | --------------------: |
| Sales Invoice    | $1,398.00    | $139.80 debit to Sales Discounts Allowed      | $1,258.20 receivable |
| Purchase Invoice | $1,040.00    | $104.00 credit to Purchase Discounts Received | $936.00 payable      |


## Choose the appropriate discount method

Use this negative-charge workflow when you need explicit control over the separate account, especially for Purchase Invoices. ERPNext's newer [Discount Accounting](/erpnext/discount-accounting) workflow provides dedicated sales-side Discount Account fields and can be more convenient for item and invoice-level sales discounts.

Do not use both methods on the same discount. A normal item discount, an [additional discount](/erpnext/applying-discount), a Pricing Rule, and a negative charge row can all reduce the transaction. Combining them without an intentional calculation can double-count the reduction.

This workflow records a transaction-wide discount. It does not allocate a different discount to each item row for margin analysis. If item-level commercial pricing matters, set an intentional [Item Price](/erpnext/item-price) or item discount and decide separately whether the ledger also needs a distinct discount account.

## Before you begin

1. Confirm with your accountant whether discount allowed belongs under Expense or contra-revenue, and whether discount received belongs under Income or contra-expense.
2. Create non-group ledgers in the Company's [Chart of Accounts](/erpnext/chart-of-accounts). The example uses **Sales Discounts Allowed - NET** and **Purchase Discounts Received - NET**.
3. Confirm the discount basis. **On Net Total** applies the rate to the complete Net Total. Other charge types can calculate against a prior row or a fixed amount.
4. Confirm how the discount affects tax. The order and type of rows in the charge table determine the running total used by later taxes.
5. Test a representative transaction and review its ledger before using the method in production.

The sales discount account appears under Expenses in this example.



![Sales Discounts Allowed account highlighted in the Chart of Accounts](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-account.png)

The purchase discount account appears under Income.



![Purchase Discounts Received account highlighted in the Chart of Accounts](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-discount-account.png)

## Book a discount allowed on a Sales Invoice

1. Create a [Sales Invoice](/erpnext/sales-invoice) and add the Items at their gross selling rates.
2. In **Sales Taxes and Charges**, add a row. A reusable [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template) can provide the same row when this treatment is standard.
3. Select the highlighted pencil icon to open the complete row editor.

![Sales Invoice discount row with the pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-row.png)

4. Set **Type** to **On Net Total**.
5. Set **Account Head** to the discount-allowed account.
6. Enter the discount percentage as a negative **Tax Rate**. For a 10% discount, enter **-10**.
7. Enter a clear Description and the required Cost Center or other [Accounting Dimensions](/erpnext/accounting-dimensions).

![Sales discount Type, Account Head, and negative Tax Rate highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-discount-fields.png)

The example starts with two phones at $699 each, or $1,398. A -10% row produces -$139.80, reducing the Grand Total to $1,258.20.



![Submitted Sales Invoice with the discount and Grand Total highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-submitted-total.png)

8. Review taxes, rounding, Grand Total, and the charge row, then submit.
9. Open **View &gt; Accounting Ledger** and verify the result in the [General Ledger](/erpnext/general-ledger).

![Sales Invoice ledger with the separate discount row highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-general-ledger.png)

The ledger debits Debtors by $1,258.20, debits Sales Discounts Allowed by $139.80, and credits Sales by the gross $1,398.00.

## Book a discount received on a Purchase Invoice

1. Create a [Purchase Invoice](/erpnext/purchase-invoice) and add the Items at their gross purchase rates.
2. In **Purchase Taxes and Charges**, add a row. Use a [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) when the same treatment is reusable.
3. Select the pencil icon on the row.
4. Set **Type** to **On Net Total**.
5. Set **Account Head** to the discount-received income or contra-expense account approved by your accountant.
6. Enter the percentage as a negative **Tax Rate**. The example uses **-10**.

![Purchase discount Type, Account Head, and negative Tax Rate highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-discount-fields.png)

The gross purchase is $1,040. The -10% row deducts $104, so the Supplier is owed $936.



![Submitted Purchase Invoice with the discount and Grand Total highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-submitted-total.png)

7. Submit and open the Accounting Ledger.

![Purchase Invoice ledger with the separate discount row highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-general-ledger.png)

The ledger credits Creditors by $936, debits the purchase or stock-received account by $1,040, and credits Purchase Discounts Received by $104.

If a [Purchase Receipt](/erpnext/purchase-receipt) was already posted at a different amount, do not assume the Purchase Invoice discount will correct stock valuation or clear Stock Received But Not Billed automatically. Apply the commercial treatment consistently across the purchase cycle and verify both stock and accounting ledgers.

## Record the net payment

Create a [Payment Entry](/erpnext/payment-entry) for the invoice's final outstanding amount, not its gross amount before discount.

For the sales example, the Customer pays $1,258.20. The Payment References row allocates that amount to the Sales Invoice.



![Customer Payment Entry allocating the net Sales Invoice amount](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-sales-payment-entry.png)

For the purchase example, the Company pays $936 to the Supplier.



![Supplier Payment Entry allocating the net Purchase Invoice amount](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-separate-discount-booking-purchase-payment-entry.png)

The discount was already posted by the invoice. Do not add the same discount again as a deduction in Payment Entry unless a separate payment-time adjustment genuinely occurred.

## Important fields and what they mean


| Field                      | What it controls                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| Type                       | Calculation basis for the row. On Net Total applies the percentage to the invoice Net Total. |
| Account Head               | Ledger that receives the discount posting. It must belong to the selected Company.           |
| Tax Rate                   | Percentage used by the row. Enter a negative value to deduct the discount.                   |
| Amount                     | Calculated or entered deduction. Review its sign and value before submission.                |
| Description                | Text shown on the invoice and useful for reviewers. It does not determine the ledger.        |
| Cost Center and dimensions | Reporting segments applied to the discount posting.                                          |
| Grand Total                | Net amount due after all charge, tax, discount, and rounding rows.                           |
| Payment References         | Invoice allocation on the Payment Entry. Allocate the final outstanding amount.              |


## Troubleshooting


| Issue                                         | What to check                                                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The discount increases the invoice            | Confirm Tax Rate is negative. A positive charge row increases the total.                                                                                |
| The discount posts to the wrong account       | Correct Account Head while the invoice is Draft. After submission, follow the supported cancel-and-amend process.                                       |
| Tax is calculated on the wrong amount         | Review row order, Type, Row ID, and whether the next tax uses Net Total, Previous Row Amount, or Previous Row Total.                                    |
| The purchase clearing account does not settle | Compare Purchase Receipt and Purchase Invoice rates, discounts, taxes, and linked quantities. Verify stock valuation and Stock Received But Not Billed. |
| The payment does not close the invoice        | Allocate the current outstanding amount, use the correct Party and receivable or payable account, and confirm the Payment Entry is submitted.           |


## Frequently asked questions

### Should Discount Allowed always be an expense account?

Not always. Some accounting policies classify it as a contra-revenue account. ERPNext posts to the Account Head you select, so your accountant should determine the correct classification.

### Why is the discount entered in a taxes table?

ERPNext uses the table for taxes and other additions or deductions. A negative row reduces the running total and posts to its Account Head.

### Can I enter a fixed discount instead of a percentage?

Yes, use an appropriate fixed-amount charge type and enter a negative amount. Confirm how later tax rows use the running total.

### Can I reuse the same discount row?

Yes, create a sales or purchase taxes-and-charges template when the account, basis, description, and rate are standard. Review the fetched row on every transaction.

### Does a purchase discount automatically update stock valuation?

Not in every purchase sequence. The outcome depends on whether stock was received separately, the accounts used, and the settings governing receipt and invoice valuation. Verify the Purchase Receipt, Purchase Invoice, stock ledger, and General Ledger together.

## Related topics

- [Discount Accounting](/erpnext/discount-accounting)
- [Applying a Discount](/erpnext/applying-discount)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__booking-customer-deducted-tds-in-payment-entry-in-erpnext.md -->
---
title: "Booking Customer Deducted TDS in Payment Entry in ERPNext | ERPNext Documentation"
description: "Record customer-withheld tax and clear the related ERPNext invoice correctly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/booking-customer-deducted-tds-in-payment-entry-in-erpnext"
updated: "2026-08-01"
---

When a Customer withholds tax from a payment, the bank receives less than the invoice value. Record the cash received, allocate the invoice, and post the withheld amount to the correct tax receivable account.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Booking Customer Deducted TDS in Payment Entry in ERPNext

1. Create a Receive Payment Entry and fetch the Sales Invoice.
2. Enter the net amount received in the bank.
3. Allocate the invoice amount being settled.
4. Add the withheld amount in **Deductions or Loss** using the approved tax receivable account.
5. Attach or reference the withholding certificate when available.
6. Confirm that the Difference Amount is zero and submit.

![Booking Customer Deducted TDS in Payment Entry in ERPNext in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-05-payment-entry-references.png)

## Important fields and what they mean


| Field            | What it controls                               |
| ---------------- | ---------------------------------------------- |
| Paid Amount      | Net cash received.                             |
| Allocated Amount | Invoice amount cleared.                        |
| Account          | Tax receivable ledger for the withheld amount. |
| Amount           | Tax withheld by the Customer.                  |
| Reference        | Certificate or remittance evidence.            |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The invoice remains partly outstanding after the customer deducts tax

The bank receipt and tax deducted must together clear the invoice. Record the withheld amount against the correct tax receivable or recoverable account instead of allocating only the cash received.

### The withholding entry credits or debits the wrong account

Review whether you are recording customer-deducted tax or supplier withholding. Customer-deducted tax is commonly a recoverable asset, while tax withheld from a supplier is commonly a liability. Confirm the local accounting treatment with your adviser.

### The deduction amount is calculated on the wrong base

Check the calculation type, rate, actual amount, partial-payment behavior, and regional tax configuration. Do not reuse a supplier withholding setup without verifying that it fits customer-deducted tax.

## Frequently asked questions

### Should the Payment Entry amount equal the invoice or the bank receipt?

Record the actual cash received in the bank amount. Use the supported deduction or tax fields so the cash plus recoverable tax clears the invoice.

### Is customer-deducted tax an expense?

It is often a recoverable tax asset, but the treatment depends on local law and whether the amount can be claimed. Use an expense account only when advised that it is not recoverable.

### Can the deduction be recorded after the Payment Entry was submitted?

Correct the transaction through cancellation and amendment or another approved accounting adjustment. Do not edit posted ledger values directly.

### Why does this differ from withholding tax on supplier payments?

In a customer receipt, your customer has withheld money from you. In a supplier payment, your company withholds money owed to the supplier and may owe it to a tax authority.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__braintree-integration.md -->
---
title: "Setting up Braintree\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/braintree-integration"
updated: "2026-02-26"
---


To setup Braintree, go to `Explore > Integrations > Braintree Settings`

## Setup Braintree

To enable Braintree in your ERPNext account, you need to configure the following parameters:

- Merchant ID
- Public Key
- Private Key

You can setup several Braintree payment gateways if needed. The choice of payment gateway account will determine which braintree account is used for the payment.

![Braintree Settings](/files/braintree_account.png)

On enabling service, the system will create Payment Gateway record and an Account head in chart of account with account type as Bank.

![Braintree COA](/files/braintree_coa.png)

It will also create a payment gateway account. You can change the default bank account if needed and create a template for the payment request.

![Payment Gateway Account](/files/payment_gateway_account_braintree.png)

After configuring the Payment Gateway Account, your system is able to accept online payments through Braintree.

## Supporting transaction currencies

```
"AED","AMD","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BIF","BMD","BND","BOB",
"BRL","BSD","BWP","BYN","BZD","CAD","CHF","CLP","CNY","COP","CRC","CVE","CZK","DJF","DKK",
"DOP","DZD","EGP","ETB","EUR","FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF","GTQ","GYD",
"HKD","HNL","HRK","HTG","HUF","IDR","ILS","INR","ISK","JMD","JPY","KES","KGS","KHR","KMF",
"KRW","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","MAD","MDL","MKD","MNT","MOP","MUR",
"MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","PAB","PEN","PGK","PHP",
"PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SEK","SGD","SHP","SLL",
"SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TOP","TRY","TTD","TWD","TZS","UAH","UGX",
"USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XOF","XPF","YER","ZAR","ZMK","ZWD"
```

<!-- page: erpnext/erpnext__brand.md -->
---
title: "Brand\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/brand"
updated: "2026-03-06"
---

**A Brand identifies items with a specific name.**

Usually, a Brand is the manufacturer or packer of a specific product. For example, Apple is a brand that manufactures laptops. A Brand is not necessarily the [Manufacturer](/erpnext/manufacturer) of an Item, it's only the name under which a product is sold. For example, if you manufacture plastic cups, you may license them to a big brand so that they sell them under their Brand.

In ERPNext, Brands can be assigned to Items for identifying and assigning certain defaults.

To access the Brand list, go to:

> Home > Selling > Sales > Brand

## 1. How to Create a Brand

1. Go to the Brand list and click on New.
2. Enter a Brand name and enter a description if needed.
3. Save.
  [Brand](/files/brand.png)

Now this Brand can be associated with different Items.

![](/files/item_brand.png)

## 2. Features

### 2.1 Setting defaults for Items of this Brand

![](/files/brand_defaults.png)

The following defaults can be set for a Brand. On assigning this brand to an Item, the set defaults will be fetched when performing Sales/Purchase transactions with Item of this Brand.

- **Default Warehouse**: The Warehouse from which the Item will be sourced/stored depending on the transaction.
- **Default Price List**: The Price List set here will be fetched in Purchase/Sales transactions.

#### Purchase Defaults

When performing Purchase transactions like Purchase Order, Purchase Receipt, or Purchase Invoice, the defaults set here will be fetched on selecting Item of this Brand.

- Default Buying Cost Center
- Default Supplier
- Default Expense Account

#### Sales Defaults

When performing Sales transactions like Sales Order, Delivery Note, or Sales Invoice, the defaults set here will be fetched on selecting Item of this Brand.

- Default Selling Cost Center
- Default Income Account

## 3. Related Topics

1. [Purchase Order](/erpnext/purchase-order)
2. [Sales Order](/erpnext/sales-order)
3. [Purchase Receipt](/erpnext/purchase-receipt)
4. [Delivery Note](/erpnext/delivery-note)
5. [Sales Invoice](/erpnext/sales-invoice)
6. [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__budget-revision.md -->
---
title: "Budget Revision"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget-revision"
updated: "2026-08-14"
---

Nova Electronics Trading approved $120,000 for marketing at the beginning of the year. Six months later, management approves another $30,000 for a new phone launch. The finance team needs to increase the plan without losing the record of what was originally approved.



Use a Budget Revision when management changes an existing approved [Budget](/erpnext/budget). ERPNext creates a connected replacement instead of asking you to overwrite the submitted plan. After you submit the revision, the earlier Budget is cancelled and retained as part of the approval history.



A revision changes the plan and its transaction controls. It does not rewrite invoices, orders, or [General Ledger](/erpnext/general-ledger) entries that have already been posted.

## Before you begin

Start with a submitted Budget. Confirm the revised amount, the reason for the change, the affected [Account](/erpnext/chart-of-accounts) or [Cost Center](/erpnext/cost-center), and the person who approved it.



Review current spending in the [Budget Variance Report](/erpnext/budget-variance-report) before changing the plan. This tells you how much has already been spent and how the proposed amount will change the remaining headroom.

## Revise a Budget

Open the submitted Budget that needs to change. From the actions menu, select **Revise Budget**.



![Submitted Budget opened in ERPNext before revision](/files/budget-scope-and-period.webp)

Confirm that you want to continue. ERPNext creates a new draft based on the existing Budget, so you do not need to enter the complete plan again.



Update the **Budget Amount** and, when required, the monthly distribution. Keep the same account, fiscal year, and reporting scope unless the approved change specifically requires them to differ.



![Budget amount and distribution settings being revised](/files/budget-amount-and-distribution.webp)

Save and submit the revised Budget.

## What changes after submission


| Record                    | Result                                         |
| ------------------------- | ---------------------------------------------- |
| Earlier Budget            | Cancelled and retained as the previous version |
| Revised Budget            | Submitted and used as the active budget        |
| Existing transactions     | Remain unchanged                               |
| Budget checks and reports | Use the revised approved amount                |


Open the revised Budget and follow its amended-from link to trace the earlier approval. Then refresh the Budget Variance Report using the same [Company](/erpnext/company), [Fiscal Year](/erpnext/fiscal-year), Account, and budgeting segment. The report should show the revised approved amount while retaining the same actual spending.

## When to revise instead of creating another Budget

Use a revision when management changes the amount or distribution of the same approved plan. Create a separate Budget when you are controlling a different Company, Fiscal Year, Account, Cost Center, [Project](/erpnext/project), or [Accounting Dimension](/erpnext/accounting-dimensions). This keeps unrelated plans from being joined into one revision history.

## Troubleshooting

### Revise Budget is not available

Confirm that the Budget is submitted and that your role can cancel and create Budget records. A draft budget can be edited directly and does not need a revision.

### The revised amount does not appear in reports

Confirm that the revised Budget was submitted, then check the company, fiscal year, Cost Center, account, and other filters used in the report.

### The earlier Budget still appears

The earlier record is retained for history. Check its status. It should be cancelled after the revised Budget is submitted.

## Frequently asked questions

### Does revising a Budget change posted invoices or journals?

A revision does not change posted invoices or journals. It changes the approved plan and the controls applied to future transactions.

### Can I reduce a Budget below the amount already spent?

You can reduce the approved amount, but first compare it with actual and committed spending. A lower Budget does not reverse existing [Purchase Invoices](/erpnext/purchase-invoice) or [Purchase Orders](/erpnext/purchase-order). It may cause later transactions to warn or stop sooner.

### Why not cancel the Budget and create a new one manually?

The revision action preserves the relationship between the earlier and replacement Budgets. It also copies the existing scope and distribution, which reduces the risk of creating a new plan against the wrong Account or Cost Center.

## Related topics

- [Budget](/erpnext/budget)
- [Budget Variance Report](/erpnext/budget-variance-report)
- [Cost Center and Budgeting](/erpnext/cost-center-and-budgeting)
- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__budget-variance-report.md -->
---
title: "Budget Variance Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget-variance-report"
updated: "2026-08-14"
---

Nova Electronics Trading approved a $120,000 marketing Budget, distributed as $10,000 per month. By the end of March, the team has spent $27,500. The finance manager needs one answer: is marketing spending ahead of plan, behind plan, or exactly where it should be?



The Budget Variance Report puts the approved [Budget](/erpnext/budget) and actual expenses beside each other. Nova can see the planned amount, the amount posted through accounting transactions, and the difference for each period. A positive or negative variance is useful only after you confirm how your organisation interprets the report's sign, so focus first on whether actual spending is above or below the budget.

## Before you begin

Create and submit a Budget against the required [Cost Center](/erpnext/cost-center), [Project](/erpnext/project), or [Accounting Dimension](/erpnext/accounting-dimensions). Actual values come from submitted transactions that post to the same [Account](/erpnext/chart-of-accounts), company, period, and reporting segment.

## Review budget performance

Open **Budget Variance Report** from Accounting. Select the Company, Fiscal Year, Budget Against, and reporting frequency. Use Monthly for operational reviews and Quarterly or Yearly for a higher-level view.

![Budget Variance Report comparing a 120,000 budget with 27,500 of actual marketing expense](https://novacompanies.m.frappe.cloud/files/budgets-capital-equity-20260814-budget-variance-report.png)

Select **Show Cumulative** when you want to compare total budget and total actual spending up to each period. This is useful when spending is seasonal and one month should not be judged in isolation.

## Read the result


| Column            | Meaning                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| Budget            | The amount approved for the period by the applicable Budget.                    |
| Actual            | Submitted expense entries posted to the matching account and reporting segment. |
| Variance          | The difference between the planned and actual amount.                           |
| Cumulative values | The running budget, actual amount, and variance through that period.            |


If actual spending looks incomplete, check the [General Ledger](/erpnext/general-ledger) for the same account, dates, and Cost Center. A [Journal Entry](/erpnext/journal-entry), [Purchase Invoice](/erpnext/purchase-invoice), or other submitted expense transaction contributes only when its dimensions match the Budget.

## Troubleshooting

### The report is empty

Confirm that a submitted Budget exists for the selected Company, Fiscal Year, account, and reporting segment. This report is budget-driven, so actual expenses alone do not create rows.

### The actual amount is lower than expected

Check whether the missing transactions use another Cost Center, Project, Account, Posting Date, or accounting dimension. Compare the report with the General Ledger using identical filters.

## Frequently asked questions

### Does the report enforce the budget?

Budget controls enforce or warn about limits. The report explains performance after transactions have been requested, committed, or posted.

### Should I use monthly or cumulative values?

Monthly values show what happened in one period. Cumulative values show whether the organisation is within its plan overall despite timing differences.

## Related topics

- [Budget](/erpnext/budget)
- [Budget Revision](/erpnext/budget-revision)
- [Cost Center and Budgeting](/erpnext/cost-center-and-budgeting)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__budget.md -->
---
title: "Budget"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/budget"
updated: "2026-08-14"
---

Nova Electronics Trading plans to spend $120,000 on marketing this year. The finance team wants the marketing team to work freely within that amount, but it also wants to know before a purchase pushes spending beyond the approved plan.



A Budget turns that plan into an ERPNext control. Nova can set a $120,000 limit against its Marketing [Cost Center](/erpnext/cost-center) and Advertising [Account](/erpnext/chart-of-accounts). ERPNext can warn the buyer or stop the transaction when a [Material Request](/erpnext/material-request), [Purchase Order](/erpnext/purchase-order), or posted expense exceeds the limit.



The Budget does not hold money in a bank account. It records what the company has approved, compares that plan with commitments and actual expenses, and helps managers act before overspending becomes visible at month-end.

## Before you begin

Set up the [Fiscal Year](/erpnext/fiscal-year), ledger Account, and the segment you want to control. You can create a Budget against a Cost Center, [Project](/erpnext/project), or supported [Accounting Dimension](/erpnext/accounting-dimensions).



Decide where ERPNext should intervene. Use **Warn** when the person submitting the transaction may continue after reviewing the overrun. Use **Stop** when exceeding the approved amount requires the Budget or transaction to be changed first.

## Create a Budget

Open the Budget list and select **Add Budget**.



![Budget list in ERPNext](/files/budget-list.webp)



Select **Budget Against**, then choose the Cost Center, Project, or Accounting Dimension value. Select the **Company** and ledger **Account** whose activity should be measured.



Set **From Fiscal Year** and **To Fiscal Year**. A budget can cover one fiscal year or span several fiscal years when the organisation plans a longer initiative.



![Budget scope, account, and fiscal year fields](/files/budget-scope-and-period.webp)



Enter the **Budget Amount** and choose a **Distribution Frequency**: Monthly, Quarterly, Half-Yearly, or Yearly.



Enable **Distribute Equally** when each period should receive the same share. Otherwise, adjust the generated Budget Distribution rows to reflect seasonality, campaign timing, or another planned pattern.



![Budget amount and distribution settings](/files/budget-amount-and-distribution.webp)

## Choose budget control actions

ERPNext can check the same approved amount at different stages of the buying and accounting cycle. Enable the earliest stage where your company wants control. Checking a Purchase Order helps prevent an excessive commitment before the supplier invoice arrives.


| Stage              | What ERPNext measures                          | Typical use                                    |
| ------------------ | ---------------------------------------------- | ---------------------------------------------- |
| Material Request   | Requested purchasing demand                    | Control spending before approval or ordering.  |
| Purchase Order     | Committed purchase value                       | Prevent commitments beyond an approved amount. |
| Actual expenses    | Posted accounting expense                      | Control Purchase Invoices and Journal Entries. |
| Cumulative expense | Accumulated expense over the configured period | Apply a broader running control.               |


For each enabled stage, choose an action for the annual limit and the accumulated periodic limit. The annual check protects the complete approved amount. The periodic check protects the amount planned for the current month, quarter, or other distribution period.

- **Stop** prevents submission when the limit is exceeded.
- **Warn** informs the user but allows submission.
- **Ignore** performs no warning or block for that check.



![Purchase Order and actual expense controls in a Budget](/files/budget-control-actions.webp)



Save and submit the Budget. Draft budgets do not enforce controls.

## Important fields and what they mean


| Field                             | Meaning                                                             |
| --------------------------------- | ------------------------------------------------------------------- |
| Budget Against                    | The reporting segment controlled by the budget.                     |
| Cost Center or Project            | The specific segment value to which the budget applies.             |
| Account                           | The ledger account whose amount is compared with the budget.        |
| From Fiscal Year / To Fiscal Year | The fiscal-year range covered by the budget.                        |
| Distribution Frequency            | The interval used to divide the budget over time.                   |
| Budget Amount                     | The approved amount for the full budget period.                     |
| Distribute Equally                | Creates equal periodic amounts automatically.                       |
| Budget Distribution               | The dates, percentages, and amounts assigned to individual periods. |


## Review budget performance

Use the [Budget Variance Report](/erpnext/budget-variance-report) to compare the approved amount with actual spending. Filter by company, Fiscal Year, and budgeting segment. If a variance looks incorrect, open the [General Ledger](/erpnext/general-ledger) to inspect the transactions behind it.



A warning answers, “Should this transaction continue?” The variance report answers, “How is the complete plan performing?” Review both committed purchases and posted expenses because an approved order may consume the plan before it becomes an accounting expense through a [Purchase Invoice](/erpnext/purchase-invoice).

## Revise an approved budget

When management approves a genuine change to the amount or distribution, use [Budget Revision](/erpnext/budget-revision). This preserves the relationship between the original plan and the revised plan. Do not change a Budget merely to make one blocked transaction pass.

## What happens after submission

Submitting the Budget activates its checks. When you submit a covered transaction, ERPNext compares its amount with the applicable annual and periodic limits. It then applies the configured Stop, Warn, or Ignore action.



The Budget itself does not create a General Ledger entry, payable, or bank movement. Only the business transactions posted against the controlled Account affect the ledger.

## Troubleshooting

### No warning appears when spending exceeds the budget

Confirm that the Budget is submitted, the correct transaction stage is enabled, and the transaction uses the same company, account, fiscal period, and budget dimension value.

### The budget is triggered for the wrong period

Review the fiscal-year range, posting date, distribution frequency, and Budget Distribution rows. If Distribute Equally is disabled, confirm the manual amounts and percentages.

### ERPNext prevents an authorised exception

Review the configured action and your organisation's approval policy. An administrator can configure the Budget Approver role in Company settings for controlled exceptions.

## Frequently asked questions

### Does a Budget reserve cash?

A Budget does not reserve cash. It is a planning and control record and does not create a bank, payable, or General Ledger entry.

### Can one Budget cover several accounts?

A Budget record is created for a specific account and budget dimension. Create separate records when different accounts require their own limits.

### Can a Budget span multiple fiscal years?

You can span multiple fiscal years by selecting the appropriate From Fiscal Year and To Fiscal Year. Review the generated distribution carefully so that each period receives the intended amount.

### What is the difference between Warn and Stop?

Warn shows the over-budget condition but permits submission. Stop blocks submission until the transaction or budget is changed by an authorised user.

## Related topics

- [Budget Revision](/erpnext/budget-revision)
- [Budget Variance Report](/erpnext/budget-variance-report)
- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [Purchase Order](/erpnext/purchase-order)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__bulk-assign-tasks-in-a-project.md -->
---
title: "Bulk Assign Tasks in a Project"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-assign-tasks-in-a-project"
updated: "2026-02-27"
---

**Use Case**: Need to bulk assign all the Tasks in a Project to aUser.  
**Steps:**   
1) Create a Project.  
2) Create Tasks in that Project.  
3) Go to Task List and filter the Tasks based on the Project as shown below:  
![](/files/JWvaO3x.png)  
4) Select all the Tasks (or the Tasks you wish to assign to the User).  
![](/files/mpSG2p6.png)  
5) Go to Actions > "Assign To" and select the User to whom you wish to assign these Tasks.  
![](/files/GZFTC86.png)  
![](/files/5pvnr02.png)  
You can also enter other details such as Comments, Completed By and bulk set the Priority of the Tasks.  
6) Click on Add.  
**Note:** You can follow the above steps to bulk assign any documents in ERPNext.  
  
  

<!-- page: erpnext/erpnext__bulk-overwrite.md -->
---
title: "Overwrite Data"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-overwrite"
updated: "2026-07-02"
---

Use Data Import when you need to update many existing ERPNext records from a spreadsheet. This is useful for correcting field values, filling missing information, or applying the same change across records without opening each document manually.

Bulk overwrite updates existing records. It does not create a new record for each row when you choose **Update Existing Records**.

## Before You Begin

- Export or download the existing data before making changes, so you have a rollback reference.
- Test the import with a small set of records before updating a large list.
- Keep the record identifier column, such as `ID` or `name`, in the file. ERPNext uses it to find the record to update.
- Only keep the columns you want to update, plus the required identifier columns. Remove unnecessary columns to reduce the chance of overwriting the wrong field.
- Check mandatory fields and linked fields before importing. Invalid values will stop those rows from importing.

## Step 1: Open Data Import

1. Go to **Data Import** from the Data workspace or search for Data Import.
2. Click **Add Data Import**.
3. Select the **Document Type** that you want to update.

## Step 2: Choose Update Existing Records

1. In **Import Type**, select **Update Existing Records**.
2. Keep **Don't Send Emails** enabled unless you intentionally want update notifications to be sent.
3. Use **Submit After Import** only when the imported documents should be submitted immediately after update.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Step 3: Prepare the Import File

1. Download or prepare a spreadsheet for the selected Document Type.
2. Keep the record identifier column unchanged.
3. Enter the new values in the fields you want to overwrite.
4. Remove rows that should not be changed.
5. Save the file as CSV or Excel, depending on the import screen options.

If a field should not be changed, leave that column out of the import file. This is safer than keeping extra columns with stale values.

## Step 4: Upload and Validate

1. Upload the prepared file to the Data Import record.
2. Start the import preview or validation.
3. Review row errors carefully. Fix the file and upload it again if ERPNext reports missing links, invalid values, or permission issues.
4. Start the import only after the preview looks correct.

## What Gets Overwritten

ERPNext updates the fields present in the uploaded file for the matching records. The match is based on the document identifier in the file. For linked fields, the imported value must match an existing linked record.

## Common Issues

- **Record not found:** Check that the ID or name column is present and has the exact existing document ID.
- **Link validation failed:** The value in a linked field does not exist or is misspelled.
- **Mandatory field missing:** A required field is blank or was overwritten with an empty value.
- **Permission error:** Your user role does not have permission to update the selected Document Type or field.

## Recommended Practice

For important records, first run the update on a small sample. After verifying the result, import the remaining rows in batches. Keep the original export and the final import file for audit purposes.

<!-- page: erpnext/erpnext__bulk-rename.md -->
---
title: "Bulk Rename"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-rename"
updated: "2026-02-26"
---

### Renaming a single document

You can rename a document in ERPNext by going to **Menu > Rename**. This option will only be visible if you have the required permissions.

![](/files/image3a97ad.png)

### Rename Tool

Alternatively, using the **Rename Tool**, you can rectify or change multiple document IDs at once. You can rename IDs of up to 500 records at a time. 

:::note
This tool is only accessible to the User who has the System Manager role assigned.

:::



Let's assume you've realized your manual naming convention is making your inventory reports verbose. You need to convert 500 legacy item codes into your new naming standard. Now to rename these items:

#### Step 1: Create the spreadsheet

In a spreadsheet file, enter old Item IDs in the first column, new Item Ids in the second column. Save the spreadsheet file in a **.csv** format without the header.


| Old Name           | New Name     |
| ------------------ | ------------ |
| Large Blue Shirt   | SHIRT-BLUE-L |
| Small Red Shirt    | SHIRT-RED-S  |
| Medium White Shirt | SHIRT-WHT-M  |
| AA Batteries 4pk   | BATT-AA-04   |
| AAA Batteries 8pk  | BATT-AAA-08  |


#### Step 2: Upload data file

To upload the data file, search for "Rename Tool" on the awesomebar.

Select the DocType that you want to rename. Here, DocType will be Item. Then browse and upload the data file and click Rename.

![](/files/image36fdf6.png)

The Bulk Rename Jobs shows the progress of the process for each entry, from the queuing state to either finished or failed.



### Merging Documents

You can also merge documents by renaming them. For example, if you have a customer named Steve and a duplicate named Steve1, you can go to either of them, click on Menu > Rename, and tick the 'Merge with existing' checkbox. This will merge all the linked documents of both documents.

To do this in bulk with the Rename Tool, change the "Merge" column to "1" or "TRUE" and upload this file to trigger renaming.


| Old Name | New Name | Merge |
| -------- | -------- | ----- |
| Steve1   | Steve    | 1     |

<!-- page: erpnext/erpnext__bulk-update.md -->
---
title: "Bulk Update\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bulk-update"
updated: "2026-04-14"
---

**Bulk Update allows you to update a particular field of a DocType for all documents.**

To access Bulk Update, go to:

> Home > Bulk Update

Consider that you have 20 quotations in which you had selected 'All Territories' and now you want to change the Territory to France. Instead of updating the individual quotations manually, you can use Bulk Update to update all 20 Quotations at once.

To do this,

1. Go to Bulk Update.
2. Select the Document Type, like Quotation.
3. Select the field to update, like territory.
4. Enter a **valid** new value to be updated.
5. Enter any conditions that apply, for example: {"status":"Draft"} will only affect documents in the Draft stage.
6. Select the limit, i.e. number of documents (Quotations) to be updated.
7. Click on Save

![](/files/imagea8e50c.png)

:::note
You can only update fields that can be updated normally in a particular stage. For example, valid till date cannot be updated for submitted Quotations.
:::

<!-- page: erpnext/erpnext__buying-settings.md -->
---
title: "Buying Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying-settings"
updated: "2026-05-27"
---

ERPNext allows you to configure various settings and configurations that help streamline and automate the purchasing workflow.

## Naming Series and Price Defaults

![Screenshot 2024-08-29 at 1.23.09 PM](/files/Screenshot 2024-08-29 at 1.23.09 PM.png)  

### 1. Supplier Naming By

When a Supplier is saved, system generates a unique identity or name for that Supplier which can be used to refer the Supplier in various Buying transactions.

If not configured otherwise, ERPNext uses the Supplier's Name as the unique name. If you want to identify Suppliers using names like SUPP-00001, SUPP-00002, or such other patterned series, select the value of Supplier Naming By as "Naming Series".

### 2. Default Supplier Group

Configure what should be the default value of Supplier Group when creating a new Supplier. For example, if most of your suppliers supply you hardware, you can set the default as 'Hardware'.

### 3. Default Buying Price List

Configure what should be the default Price List when creating a new Buying transaction, the default is set as 'Standard Buying'. Item prices will be fetched from this Price List. You can modify the 'Price List' by using the arrow at the right-end of the field to change the currency and country.

### 4. Action if Same Rate is Not Mentioned

It defines the action the should take when it encounters a purchase order, material request, or any other buying transaction where the same rate of an item is not mentioned.

There are two possible actions the user can take.

- **Stop**: The system will stop the transaction preventing the user from proceeding without specifying a rate. This ensures that all transactions have explicit rates mentioned, avoiding potential discrepancies.
- **Warn**: The system will allow the transaction happen but will display a warning message to alert the user that the same rate has not been mentioned.

### 5. Role Allowed to Override Stop Action

This setting specifies which user roles have the permission to override the "Stop" action in the buying transaction due to discrepancy in the rate.

## Transaction Settings

![Screenshot 2024-08-29 at 1.24.53 PM](/files/Screenshot 2024-08-29 at 1.24.53 PM.png)  

### 1. Is Purchase Order Required for Purchase Invoice & Receipt Creation?

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice or a Purchase Receipt directly without creating a Purchase Order first.

If retail transactions are involved where the order happens offline, then Purchase Orders can be skipped. If you're accepting sample Items, you can directly create a Purchase Receipt to receive the Items to your Warehouse.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Order" checkbox in supplier master

### 2. Is Purchase Receipt Required for Purchase Invoice Creation?

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice without creating a Purchase Receipt first. In case the Item being transacted is a service, it'll not require a receipt, you can directly create an Invoice.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Receipt" checkbox in the supplier master

### 3. Blanket Order Allowance (%)

You can set the percentage you are allowed to order more against the Blanket Order Quantity. For example: If you have a Blanket Order of Quantity 100 units. and your Allowance is 10% then you are allowed to order 110 units.

### 4. Update frequency of Project

It indicates how often should Project be updated of Total Purchase Cost.

### 5. Maintain Same Rate Throughout Purchase Cycle

If this is enabled, ERPNext will validate whether an Item's price is changing in a Purchase Invoice or Purchase Receipt created from a Purchase Order, i.e. it will help you maintain the same rate throughout the purchase cycle.

You can configure the action that system should take if the same rate is not maintained in the "Action If Same Rate is Not Maintained" field:

- **Stop**: ERPNext will stop you from changing the price by throwing a validation error.
- **Warn**: The system will let you save the transaction but warn you with a message if the rate is changed.

Note: This field will only be visible if Maintain Same Rate Throughout Purchase Cycle is enabled.

### 6. Allow Item to be added multiple times in a transaction

When this checkbox is unchecked, an item cannot be added multiple times in the same Purchase Order. However, you can still explicitly change the quantity. This is a validation checkbox for preventing accidental purchase of the same item. This can be checked for specific use cases where there are multiple sources for the same material, for example in manufacturing.

### 7. Bill for Rejected Quantity in Purchase Invoice

If checked, Rejected Quantity will be included while making Purchase Invoice from Purchase Receipt.  



### 7.1 Set Valuation Rate for Rejected Materials

For rejected materials, the valuation rate is set to zero, and no accounting ledger entry is created for them in the Purchase Receipt. To apply a valuation rate and generate accounting entries for rejected materials, enable the 'Set Valuation Rate for Rejected Materials' option in Buying Settings. This option is only applicable when `Bill for Rejected Quantity in Purchase Invoice` has enabled in the Buying Settings.

![](/files/Screenshot%202025-06-09%20at%204.49.24%20PM%201.png)

##### 8. **Set Landed Cost Based on Purchase Invoice Rate**

If the 'Maintain Same Rate Throughout the Purchase Cycle' is disabled then this field shows in the buying settings. If user wants to adjust the product valuation as per the purchase invoice cost then this option needs to be enable.

How It Works

- Created Purchase Receipt for item A with rate as 100
- System has booked Stock In Hand with 100 rate
- After 2 days, user has created purchase invoice against the above purchase receipt
- After 2 days because of change in exchange rate the rate in the invoice changed to 150
- Now purchase receipt has rate 100 where as Purchase invoice has rate 150
- If you want to adjust the Stock In Hand with Purchase invoice Rate (150) then enable "Set Landed Cost Based on Purchase Invoice Rate".

Note: on submission of the purchase invoice, system creates the repost item valuation record to update the cost of the purchase receipt. User has to wait to complete the repost item valuation to see the impact of the invoice cost on the stock in hand.

### 9. **Disable Last Purchase Rate**

It prevents the system from automatically using the rate from the last purchase transaction when creating new purchase orders or transactions.

### 10. Use Transaction Date Exchange Rate

While making Purchase Invoice from Purchase Order, use Exchange Rate on Invoice's transaction date rather than inheriting it from Purchase Order. Only applies for Purchase Invoice.

### 11. Over Order Allowance (%)

The percentage by which you are allowed to order more on a Purchase Order than the quantity requested on the originating Material Request. For example, if the Material Request has 100 units and the allowance is 10%, you can order up to 110 units.

## Subcontracting Settings

![Screenshot 2024-08-29 at 1.32.06 PM](/files/Screenshot 2024-08-29 at 1.32.06 PM.png)  

### 1. Backflush Raw Materials of Subcontract Based On

1. BOM: system will consume raw materials in the subcontracting receipt as per the FG BOM
2. Material Transferred for Subcontract: system will consume raw materials based on the materials transferred against the Subcontracting Order. If no stock transferred then no materials will be consume at the time of Subcontracting Receipt.

### 2. **Auto Create Subcontracting Order**

System will auto create the subcontracting order in a Draft state on submission of the purchase order which has "Is Subcontracted" enabled.

### 3. **Auto Create Purchase Receipt**

System will auto create the purchase receipt for the service items in a Draft state on submission of the subcontracting receipt.

### 4. Over Transfer Allowance (%)

It is the percentage you are allowed to transfer more against the quantity ordered. For example: If you have ordered 100 units. and your Allowance is 10% then you are allowed to transfer 110 units.

<!-- page: erpnext/erpnext__buying.md -->
---
title: "Introduction to Buying Module"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying"
updated: "2026-02-28"
---

The Buying module in ERPNext is designed to manage procurement processes and optimise supplier relationships. 

- **Requests for Quotation (RFQs)**: Evaluate quotations from suppliers to make informed purchasing decisions.
- **Supplier Management**: Maintain detailed records of suppliers, including contact details, terms, and performance metrics.
- **Purchase Orders**: Create and track purchase orders to ensure timely and accurate order fulfillment.
- **Purchase Invoices**: Process and manage invoices from suppliers, including payment handling.
- **Stock Management**: Update inventory levels and manage stock replenishment.

The Buying module helps businesses streamline their procurement activities, control purchasing costs, and strengthen supplier relationships.



Watch this [Frappe School Course on Procurement](https://school.frappe.io/lms/courses/procurement)  to learn more.

<!-- page: erpnext/erpnext__buying_reports.md -->
---
title: "Buying Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying_reports"
updated: "2026-04-03"
---

Data pertaining to purchases made by an organization can be analyzed and visualized through various reports available in the buying modules. Normally, each report has three sections: Filter toolbar, a chart, and data. Changes in the filters and selections are immediately reflected in the chart.

## Purchase Analytics

To access the report, go to:

> Home > Buying > Key Reports > Purchase Analytics

![](/files/image3e4322.png)

Through the Purchase Analytics report, the purchase-related data against the supplier, supplier groups, items and item group can be analyzed over a given period and frequency.

## Purchase Order Analysis

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Analysis

![](/files/image65e2f6.png)

This report is helpful in analyzing the items and their billing status in a purchase order over a given period.

## Supplier-Wise Sales Analytics

To access the report, go to:

> Home > Buying > Key Reports > Sales-Wise Sales Analytics

![](/files/imagedb5944.png)

This report provides extensive data on different items purchased from the suppliers.

## Items to Order and Receive

To access the report, go to:

> Home > Buying > Key Reports > Items to Order and Receive

![](/files/image65f1e2.png)

This report visualizes and shows data for the purchase requests created.

## Purchase Order Trends

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Trends

![](/files/image8141ae.png)

Through this report, the trends for purchase orders for a given financial year can be visualized. The trend can be grouped based on Suppliers, Supplier Group, Item, Item Group, and Project.

## Procurement Tracker

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Trends

![](/files/imagebb95af.png)

This report presents extensive purchase-related data including material requests, purchase orders created for the items.

## Other Reports

To access, go to:

> Home > Buying > Other Reports

In other reports section, the following reports can be accessed:

1. Items To Be Requested
2. Item-Wise Purchase History
3. Purchase Receipt Trends
4. Purchase Invoice Trends
5. Subcontracted Item To Be Received
6. Supplier Quotation

<!-- page: erpnext/erpnext__calculate-incentive-for-sales-team.md -->
---
title: "Calculate Incentive For Sales Team\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculate-incentive-for-sales-team"
updated: "2026-07-24"
---

ERPNext can calculate incentives for an internal sales team directly from the **Sales Team** child table on supported transactions. Each Sales Person receives a contribution percentage, contribution amount, commission rate, and calculated incentive.

The earlier documentation relied on an obsolete client script and legacy APIs. For standard percentage-based incentives, use the native Sales Person and Sales Team fields. Create custom logic only when the incentive policy cannot be represented by the standard calculation.

## Before you begin

Set up:

- An enabled [Sales Person](/erpnext/sales-person) for every eligible team member.
- A **Commission Rate** on each Sales Person.
- A written incentive policy that defines the qualifying transaction, contribution rules, approval point, returns, cancellations, and payment timing.
- User permissions to edit the Sales Team table on sales transactions.

Decide whether incentives are earned from a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice). Use the same event consistently so the same sale is not rewarded more than once.

## Set the Sales Person commission rate

1. Open the required Sales Person.
2. Enter the default **Commission Rate**.
3. Save.

ERPNext fetches this rate into new Sales Team rows. Review the policy before changing a rate because existing submitted transactions should retain their approved incentive basis.

## Add the Sales Team to a transaction

1. Open a supported sales transaction.
2. Select **More Info**.
3. Expand **Sales Team**.
4. Select **Add row**.
5. Choose the Sales Person and enter **Contribution (%)**.
6. Add other team members when the sale is shared.
7. Use the highlighted pencil icon to open the full child-row editor when needed.
8. Confirm that the contribution percentages total 100% when the full net total must be allocated.
9. Save.

![Sales Team contribution, commission rate, and incentives on a Sales Order](https://novacompanies.m.frappe.cloud/files/sales-team-table.png)

In this example, Alex Morgan receives 60% of the net total and Jordan Lee receives 40%.

## How ERPNext calculates incentives

ERPNext calculates the contribution amount from the transaction's net total:

**Contribution to Net Total = Net Total × Contribution (%) ÷ 100**

It then applies the Sales Person's commission rate:

**Incentive = Contribution to Net Total × Commission Rate ÷ 100**

For a net total of $4,164:


| Sales Person | Contribution | Contribution amount | Commission rate | Incentive |
| ------------ | ------------ | ------------------- | --------------- | --------- |
| Alex Morgan  | 60%          | $2,498.40           | 2.5%            | $62.46    |
| Jordan Lee   | 40%          | $1,665.60           | 2%              | $33.31    |


The total calculated incentive is $95.77.

## Sales Team fields and what they mean


| Field                     | Meaning                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| Sales Person              | Individual receiving sales attribution and possible incentive        |
| Contribution (%)          | Share of the transaction credited to the Sales Person                |
| Contribution to Net Total | Currency value calculated from net total and contribution percentage |
| Commission Rate           | Rate fetched from the Sales Person master                            |
| Incentives                | Calculated or approved incentive amount for the row                  |


The Sales Team table is a child table. Selecting the pencil opens the full row editor for the chosen Sales Person.

## Submit and review the transaction

Before submission:

- Verify that the correct people are included.
- Check that contribution percentages match the approved split.
- Confirm the net total and commission rates.
- Review the calculated incentive amounts.

After submission, treat the Sales Team allocation as part of the transaction's audit trail. If the sale is cancelled, amended, returned, or credited, apply the incentive policy before paying or reversing an incentive.

Read [Amending Sales Order after Submit](/erpnext/amending-sales-order-after-submit) before changing a submitted order.

## Review team performance and incentives

Use [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions) and relevant sales reports to verify transaction attribution. Use [Sales Person Target Allocation](/erpnext/sales-person-target-allocation) when the organization also tracks quantity or amount targets by Fiscal Year and Item Group.

The incentive field records a transaction-level value. It does not automatically create a payroll component, salary slip, expense, payable, or payment.

For payroll-based settlement, define a controlled process with the HR and finance teams. A common approach is to review approved incentives for the period, then include the approved amount through a configured [Additional Salary](/hr/additional-salary) or another organization-approved payroll process in Frappe HR.

## When custom logic is needed

The native calculation suits a fixed commission rate applied to the credited net total. Customization may be needed for policies such as:

- Tiered rates after revenue thresholds.
- Rates based on gross profit or collected payment.
- Different rates by Item Group, territory, or customer segment.
- Incentives paid only after the return period.
- Team bonuses triggered by a common target.
- Caps, floors, clawbacks, or manager approval.

Document the policy before implementation. Prefer a maintained server-side customization or custom app with tests over an unversioned client script. Client-side calculations alone can be bypassed by imports, integrations, background jobs, or API-created transactions.

See [Server Script](/framework/user/en/desk/scripting/server-script) and [Custom App Development](/framework/user/en/tutorial/create-an-app) when technical customization is required.

## Accounting and payroll impact

Calculated incentives have no automatic accounting or payroll impact. Do not assume that saving or submitting the sales transaction pays the employee.

The settlement process should define:

1. Which submitted documents qualify.
2. Who reviews and approves the amounts.
3. How returns and cancellations are handled.
4. Which payroll or accounting document records the approved expense.
5. When payment occurs.
6. How paid amounts are reconciled with source transactions.

## Troubleshooting

### Commission Rate is zero

Open the Sales Person and enter the approved Commission Rate. Re-add or refresh the Sales Team row when the transaction does not fetch the updated value.

### Contribution amount is incorrect

Check the transaction net total and Contribution (%). Discounts, pricing rules, and taxes can make net total different from grand total.

### Contributions do not total 100%

Review every Sales Team row. Decide whether the unallocated percentage is intentional. For full allocation, correct the rows before submission.

### Incentive is not recalculated

Save the transaction after changing contribution or team members. Reopen the row and confirm the commission rate. Avoid manually overriding calculated values without approval.

### The incentive was paid before a return

Follow the organization's clawback or adjustment policy. Link the review to the [Sales Return](/erpnext/sales-return) and the original transaction.

## Frequently asked questions

### Is this the same as Sales Partner commission?

No. Sales Team incentives apply to Sales Persons. [Sales Commission](/erpnext/how-to-give-commission-to-sales-partner) covers external Sales Partners.

### Can several people share one sale?

Yes. Add several Sales Team rows and divide contribution among them.

### Does ERPNext pay the incentive automatically?

No. It calculates the transaction-level value only.

### Can the incentive be based on collected payment?

Not with the standard net-total calculation. Use a verified customization and finance-approved policy.

### Should incentives be calculated on Sales Orders or Sales Invoices?

Choose one qualifying event and apply it consistently. Sales Invoices are generally closer to recognized billing, while Sales Orders represent confirmed bookings.

## Related topics

- [Sales Person](/erpnext/sales-person)
- [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions)
- [Sales Person Target Allocation](/erpnext/sales-person-target-allocation)

<!-- page: erpnext/erpnext__calculatin-freight-in-taxes-in-erpnext.md -->
---
title: "Calculating Freight in taxes in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculatin-freight-in-taxes-in-erpnext"
updated: "2026-03-02"
---

**Use case: To calculate freight forwarding charges with tax rate**
-------------------------------------------------------------------

  
When freight is supposed to be calculated in forwarding charges as a tax rate, we can follow the steps as below:   
* You can create a ledger in the taxes account specifically in Chart of Accounts, else you can consider GST tax account in the taxations for calculation of the Freight charges.

  
![](/files/4GSyff2.png)  
* Now create an Item with the name : **Freight and Forwarding**

![](/files/xOovUcM.png)  
* You can now create Purchase Invoice for the Supplier and add this item to calculate the Taxes related to the freight. You can set the freight tax based on the Net total or Item Quantity as per the company policy.

  
![](/files/2Nh2r9p.png)   
  

<!-- page: erpnext/erpnext__calculation-of-valuation-rate-in-fifo-and-moving-average.md -->
---
title: "FIFO and Moving Average calculation difference"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average"
updated: "2026-03-02"
---

Valuation Rate of an item is calculated based on the total expense incurred to make the product available for sale like freight, labour, cost of raw materials, etc.

In ERPNext, Valuation Rate is calculated based on the valuation method selected for the particular item. 

An item can have either FIFO or Moving Average selected as a valuation method. 

Consider the following example to know how it impacts your stock:


```
| Date      | Transaction | Qty | Unit Cost |
| 1-4-2020  | Purchase    | 10  | 100       |
| 6-4-2020  | Purchase    | 20  | 120       |
| 10-4-2020 | Sale        | 15  | ?         |
```

  
Calculating Valuation Rate at the time of sale:

**As per FIFO:**

Since this is FIFO, we will consume quantities from the *earliest* transactions, therefore, to make a sale of 15 qty, we will take 10 qty from the first transaction and 5 qty from the second one. 

(10 * 100) + (5 * 120) = 1600, which leaves us 15 qty in stock at cost of 120 amounting to **1800**.

**As per Moving Average:**

In the Moving Average method, the value of an item is *recalculated* *every time* when an item is acquired. This is done by adding the cost of the newly acquired items to the existing inventory’s value and then dividing it by the total quantity available. 

((10 * 100) + (20 * 120)) / 30 = 113.33

To make a sale of 15 qty, we will directly multiply it by the average value we received just now. 

15 * 113.33 = 1700, which leaves us 15 qty in stock amounting to **1700**.

If you check, even though the quantity is same the stock value is different but both amounts to a total of 3400 only.  
