<!-- Frappe documentation: erpnext, part 9 of 69. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Bank Transaction list with deposits and withdrawals]

Before importing a full statement:

1. check the date and amount formats;
2. confirm whether credits are deposits and debits are withdrawals;
3. map description, reference, and transaction identifier fields;
4. test a few rows;
5. compare the imported total with the source statement.

Use the Bank master's transaction mapping when the source headings differ from the expected fields.

## Review a Bank Transaction

Open a transaction and verify the Date, Bank Account, currency, and amount direction. A receipt is stored as **Deposit**. A payment or charge is stored as **Withdrawal**.

[Screenshot on the live page: Date, Bank Account, and deposit amount]

Review the description, bank reference number, transaction identifier, and transaction type. These fields help find the correct accounting voucher and detect duplicates.

[Screenshot on the live page: Description, reference number, and transaction type]

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

[Screenshot on the live page: Bank list with Add Bank highlighted]

3. Enter the Bank name. Use the full institution name so users can distinguish it from similarly named banks.
4. Enter the **SWIFT number** and **Website** when they are relevant.

[Screenshot on the live page: SWIFT number and website on the Bank master]

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

[Screenshot on the live page: Bank Transactions with realistic deposits and withdrawals]

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

[Screenshot on the live page]



**Batch feature in ERPNext allows you to group multiple units of an Item and assign them a unique value/number/tag called Batch No.**

This is done based on the Item. If the Item is batched, then a Batch number must be mentioned in every stock transaction. Batch numbers can be maintained manually or automatically. This feature is useful to set the expiry date of multiple Items or move them together to different Warehouses.

To access the Batch No list, go to: > Home > Stock > Serial No and Batch > Batch

1. Prerequisites

---

Before creating and using a Batch, it is advised that you create the following first:

- [Item](/erpnext/item)
- Enable 'Has Batch No' in the Item master [Screenshot on the live page: Batch No Enabled]

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

[Screenshot on the live page: Item Setup for Batches]



3. Features

---

### 3.1 Splitting and Moving Batches

When you open a batch, you will see all the quantities that belong to that batch on the page.

[Screenshot on the live page: Batch View]



- To move the batch from one Warehouse to another, you can click on the **Move** button.
- You can also split the batch into smaller one by clicking on the **Split** button. This will create a new Batch based on this Batch and the quantities will be split between the batches.

[Screenshot on the live page: Split Batch]

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

[Screenshot on the live page: Work Order]

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
[Screenshot on the live page]  
:::note  
**In ERPNext v16, the Scrap Items table has been replaced with Secondary Items. Read more about it here.**  
:::
6. Save and Submit.

In the Items table, you'll see an option 'Include Item in Manufacturing'. Raw Materials need to have this checkbox ticked. In case there are Operations or services you need to include in the BOM that are not necessarily an Item used for manufacturing, uncheck this checkbox. For example, treating the plastic with a chemical involves some cost but it is not an Item and the cost needs to be tracked.



[Screenshot on the live page: Task]

### 2.1 **Consume Components Based On**

“Consume Components” in ERPNext automates raw material consumption when a Work Order is completed, reducing the need for manual inventory updates. It consumes stock automatically based on either the Bill of Materials (BOM) or actual material transfers, making it ideal for high-volume, standardized production environments that aim to improve inventory accuracy and minimize manual data entry. 

[Screenshot on the live page]

- **Consumption Methods:**
  - **BOM:** Automatically consumes raw materials based on the quantities defined in the BOM, multiplied by the finished goods quantity.
  - **Material Transferred for Manufacture:** Consumes only the materials that are physically transferred to the shop floor (Work In Progress Warehouse) through a stock entry.

If you want to set default "**Consumption Components Based On**" instead of BOM wise, set the "Backflush Raw Materials Based On" in the Manufacturing Settings.

### 2.2 Bill of Materials with Operations

To add [Operations](/erpnext/operation) tick the 'With Operations' checkbox. Now, an Operations table can be seen. This option is useful for tracking the costing of various Operations performed to manufacture the [Item](/erpnext/item). Operations can be added easily by setting a template with the [Routing](/erpnext/routing) master.

[Screenshot on the live page: Task]

1. In the “Operations” table, add the operations that need to be performed to manufacture this particular Item.
2. For each operation, you will be asked to enter a [Workstation](/erpnext/workstation) where the Operation will be performed. A default Workstation can be set from the [Operation](/erpnext/operation) document.
3. Enter the Operating Hourly Rate, Operation Time in minutes, and the Batch Size created with the Operation. The Operating Cost will be calculated based on these values.

> Note: Workstations are defined only for product costing and Work Order Operations scheduling purposes not tracking inventory. Inventory is tracked in [Warehouses](/erpnext/warehouse) set in the Items table of the BOM.

Transfer Material Against needs to be set for a BOM With Operations. Materials can be transferred against a [Work Order](/erpnext/work-order) in bulk or individual [Job Cards](/erpnext/job-card). Changing this affects whether the 'Material Transfer for Manufacture' is done against the Work Order at once or multiple times against the individual Job Cards. Setting this option depends on factors like time taken to manufacture the item, value of the items manufactured, number of parts used in manufacturing, the skill of your labor involved, etc.

[Screenshot on the live page: BOM transfer materials against]

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

[Screenshot on the live page: Costing]

In case the BOM was submitted when the costs for Items/Operations were not updated, you can update the costs using the **Update Cost** button. This will fetch the latest price/costs.

[Screenshot on the live page: Update Cost]

The BOM cost can also be set to be updated automatically via Manufacturing Settings, 'Update BOM Cost Automatically' option.

### 3.2 Materials Required (Exploded)

This table lists down all the raw materials required to manufacture an Item. It also fetches raw materials for the sub-assemblies/phantom items along with the quantities. The non-exploded table will not list the raw materials required for producing the sub-assemblies.

For example, to manufacture a plastic shaving brush you need some raw materials and the bristles as a sub-assembly. For the handle, you manufacture your own plastic, but for the bristles, you use raw plastic crystals.

[Screenshot on the live page: Exploded Section]

#### 3.2.1 Do Not Explode

If user wants to exclude the exploded items then they have to enable the checkbox "Do Not Explode" in the BOM Item table. This option is made read only and is unchecked by default if Item is a Phantom Item.

##### Use Case:

- Laptop
- Motherboard (Kept in stock)
- Keyboard

A company manufacture the Laptop which required two sub-assembly items as Motherboard and Keyboard. The company does the manufacturing once they received the order from the customer. The Manufacturing Time required for the Motherboard is more than the Keyboard, therefore the company does the manufacturing of the Motherboard individually irrespective of the sales orders and kept in the stock. As the item Motherboard is already in stock it helps to reduce the overall Manufacturing Time of the main item Laptop.  
Now while preparing the BOM for the Laptop in the ERPNext, they don't want to Explode the BOM of the item Motherboard but they want to Explode the BOM of the item Keyboard. Therefore we have added the checkbox "Do Not Explode" for the BOM Item. With this user will enable the checkbox "Do Not Explode" for the item Motherboard and not for the item Keyboard.

[Screenshot on the live page: Exploded Section]

### 3.3 Project and Website

The BOM can be linked to a [Project](/erpnext/project) to track progress, Project costing, etc. In case of engineer to order, every order could be a [Project](/erpnext/project) and the sub-assemblies would be [Tasks](/erpnext/tasks). The completion can be tracked by linking to a Project in that case.

The BOM can also be shown in the [Website](/erpnext/website) for Open-source hardware products. Open-source hardware is similar to open-source where the product specifications are listed publicly.

### 3.4 BOM Template

[Screenshot on the live page: BOM Template]

With BOM template you can create BOMs for template items (against which you create variant items). These BOMs can be used as the default BOM while making Work Orders against the template Item's variants. You can also add the template items as raw materials in the template BOM. While making Work Order from the BOM Template, ERPNext gives provision to select the Item Variant against the template Item, for more details check following screenshot.

[Screenshot on the live page: Variant Selection]

The user can also make the BOM for the variant item using the template BOM. To make the variant BOM:

- Go to the BOM Template.
- Click on **Create** button.
- Click on Variant BOM.
- Select the Variant Item for which you want to make the BOM.
- If the raw materials in the BOM is a template Item, then system gives provision to select the Item Variant.

[Screenshot on the live page: Variant BOM]

### 3.5 After Submitting

Once the BOM is submitted, the following document types can be created against the BOM from the Dashboard:

[Screenshot on the live page: BOM submit]

## 4. **Set Component Quantities Based On Percentage**

- A **Percentage (%)** column appears in the Items table and **Qty** becomes read-only, each row's qty is derived as `percentage / 100 × output qty`, with UOM conversion applied when the component UOM differs from the BOM UOM.
- Percentages must total exactly 100%.
- One row can be marked **Is Balance Item**: it automatically absorbs the percentage remaining after all other rows, so users don't have to hand-balance decimals. Only one balance item is allowed, and the other rows must leave it a positive remainder.
- Every non-balance row must have a percentage mixed percentage/manual-qty BOMs are not allowed.
- Quantities are recomputed on every save, so changing the output qty rescales the whole recipe.

## Example

Output Qty 200 kg: coriander 40% → 80 kg, chilli 35% → 70 kg, turmeric marked as balance item → 25% → 50 kg (if not manually added).

[Screenshot on the live page]

### 5. Related Topics

1. [Scrap Management](/erpnext/scrap-management)
2. [Material Consumption](/erpnext/material_consumption)
3. [Nested BOM Structure](/erpnext/managing-multi-level-bom)
