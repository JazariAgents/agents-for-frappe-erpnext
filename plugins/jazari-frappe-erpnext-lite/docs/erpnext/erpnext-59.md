<!-- Frappe documentation: erpnext, part 59 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__stale-cheque-accounting.md -->
---
title: "Stale Cheque Accounting | ERPNext Documentation"
description: "Reverse or replace an expired check while preserving the ERPNext audit trail."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stale-cheque-accounting"
updated: "2026-08-01"
---

A stale check has passed the validity period and is no longer expected to clear. Do not delete the original entry. Reverse or cancel it according to its status, then issue a replacement when required.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Stale Cheque Accounting

1. Confirm with the bank that the check is stale and has not cleared.
2. Locate the original Payment Entry and its ledger impact.
3. Cancel it when ERPNext permits and your control policy allows cancellation.
4. If cancellation is not appropriate, post an authorized reversing Journal Entry with a clear reference.
5. Create a new Payment Entry for the replacement check and reconcile only when it clears.

![Stale Cheque Accounting in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-14-journal-entry-list.png)

## Important fields and what they mean


| Field                  | What it controls                                    |
| ---------------------- | --------------------------------------------------- |
| Cheque or Reference No | Identifies the original instrument.                 |
| Reference Date         | Issue date of the check.                            |
| Posting Date           | Accounting date of the original or reversal entry.  |
| Remarks                | Reason for reversal and replacement reference.      |
| Clearance Date         | Date the bank confirms settlement, when applicable. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The stale cheque belongs to a closed accounting period

Do not cancel or backdate into a locked period without approval. Record the reversal or reclassification in the current permitted period using the workflow approved by your accountant.

### Reissuing the cheque would pay the invoice twice

First reverse or clear the stale cheque's payment effect, verify that the supplier balance is outstanding, and only then issue the replacement.

### The cheque was actually dishonoured, not merely stale

Record the correct event and supporting evidence. A dishonoured cheque can include bank charges and an immediate restoration of the invoice balance, while a stale cheque has expired without clearing.

## Frequently asked questions

### When does a cheque become stale?

The validity period depends on the bank and jurisdiction. Confirm the date with the bank rather than assuming a universal number of months.

### Should the original Payment Entry be deleted?

Keep the audit trail. Use cancellation, reversal, or a current-period adjustment according to the document status and accounting-period controls.

### Can a replacement cheque reuse the same reference number?

Use the new cheque's actual reference and link it to the reversal or stale cheque explanation. Reusing the old number weakens traceability.

### Does marking a cheque stale automatically reopen the invoice?

The invoice is restored only when the accounting effect of the original payment is properly reversed or unallocated. Verify Accounts Payable afterward.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__standard-valuation-rate.md -->
---
title: "Standard Valuation Rate"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/standard-valuation-rate"
updated: "2026-07-01"
---

# Standard Valuation Rate (Standard Costing)

## 1. Overview

The **Standard Valuation Rate** feature lets you value an item's inventory at a single, pre-defined "standard" cost rather than at the constantly-changing rate produced by **FIFO** or **Moving Average**.

With FIFO or Moving Average, the value of your stock moves every time you receive, consume, or revalue material. With **Standard Cost**, the rate is fixed by you (via an **Item Standard Cost** record) and only changes when *you* deliberately publish a new rate. Every receipt, issue, and balance for that item is carried at the standard rate, and the difference between the actual purchase price and the standard rate is posted to a dedicated **Purchase Price Variance** account instead of silently inflating or deflating your inventory value.

This guide explains what the feature does, why you would choose it, how to set it up, how it behaves during transactions and accounting, and the rules you must follow to keep your standard-cost ledger consistent.

---

## 2. Why choose Standard Cost over FIFO / Moving Average?


| Concern                       | FIFO / Moving Average                                           | Standard Cost                                                                                                |
| ----------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Inventory value stability** | Changes with every receipt and revaluation                      | Fixed until you publish a new rate                                                                           |
| **Backdated transactions**    | Trigger a **full revaluation / reposting** of all later entries | **No reposting** — only a fast quantity/value shift                                                          |
| **Reposting performance**     | Slow on items with long, dense ledgers                          | Fast — the rate is known by date, nothing is recalculated                                                    |
| **Cost predictability**       | Cost of goods varies by lot/average                             | Cost of goods is the standard rate, always                                                                   |
| **Variance visibility**       | Price differences are buried in stock value                     | Price differences are isolated in a **Purchase Price Variance** account                                      |
| **Best suited for**           | Trading, where actual landed cost matters per lot               | Manufacturing & high-volume operations that want predictable product cost and frequent backdated corrections |


### The headline benefit: backdated entries do **not** trigger revaluation

This is the single most important reason to adopt Standard Cost.

- With **FIFO / Moving Average**, inserting a transaction *in the past* changes the average/lot consumption of **every later transaction**. The system must **repost** (recompute) the entire forward chain of stock ledger entries. On an item with months of dense history, this is slow and resource-heavy, and it temporarily changes the value of stock that you thought was settled.
- With **Standard Cost**, the value of every stock ledger entry is simply `quantity × standard rate as of that date`. A backdated entry only shifts the running **quantity** of later entries; their **value** is re-derived directly from the (already known) standard rate. There is **no FIFO/average recomputation and no reposting job**. The update is a single, fast quantity-and-value shift, and your inventory valuation stays stable and predictable.

> In short: Standard Cost trades "perfectly tracked actual cost" for **speed, stability, and predictability** — exactly the trade-off most manufacturing and high-throughput operations want.

---

## 3. Key concept: the **Item Standard Cost** record

The standard rate for an item is published through the **Item Standard Cost** document. Each record carries:

- **Item** — the item being standard-costed (only items whose valuation method resolves to *Standard Cost* are selectable).
- **Company** — the rate is per company.
- **Standard Rate** — the fixed valuation rate (must be greater than zero).
- **Effective Date** — the date from which this rate applies.

Each item+company has a **timeline** of Item Standard Cost records, with **strictly increasing effective dates**. The rate in force on any given date is the latest record whose effective date is on or before that date.

```
Item A (Company X)
 ├─ ISC-2025-0001  Effective 01-Jan-2025  Rate 100   ← rate from 01-Jan-2025 onward
 └─ ISC-2026-0001  Effective 01-Jan-2026  Rate 130   ← rate from 01-Jan-2026 onward
```

---

## 4. Setting up an item's Standard Cost — step by step

### Step 1 — Set the item's valuation method to *Standard Cost*

Set **Valuation Method = Standard Cost** on the item, in one of three ways (most specific wins):

1. **Item master** → *Valuation Method* = `Standard Cost`, **or**
2. Leave the item blank and set the **Company** default valuation method to `Standard Cost`, **or**
3. Leave both blank and set **Stock Settings** → default valuation method to `Standard Cost`.

> **Important:** an item that *already has stock movement* cannot be switched onto Standard Cost retroactively. Enable Standard Cost on a new item, or before any stock transaction exists for it.

### Step 2 — Create the first Item Standard Cost record

1. Go to **Item Standard Cost → New**.
2. Select the **Item** (the dropdown only lists items whose effective valuation method is *Standard Cost*).
3. Select the **Company**.
4. Enter the **Standard Rate** (must be > 0).
5. Set the **Effective Date** (cannot be a future date).
6. **Save** and **Submit**.

> The very first standard cost for an item can only be created **before any stock transaction exists** for that item+company. This guarantees the item starts its life under Standard Cost with nothing to revalue.

### Step 3 — Transact normally

Receive, issue, manufacture, and transfer the item as usual. Every stock ledger entry is automatically valued at the standard rate in force on its posting date.

### Step 4 — Change the rate later (when needed)

When the standard cost needs to change:

1. Create a **new** Item Standard Cost record with the new rate.
2. Give it an **Effective Date after the previous record's effective date** (effective dates must strictly increase) and **on or after the last stock transaction date** for that item.
3. **Submit** it.

On submission, the system automatically creates and submits a **revaluation Stock Reconciliation** that re-states all on-hand stock (across **all warehouses**) from the old rate to the new rate, and books the revaluation gain/loss to the **Stock Adjustment** account. You do not create this reconciliation manually — it is generated for you and linked on the record.

---

## 5. How Standard Cost behaves during transactions & accounting

### Stock ledger valuation

Every stock ledger entry for a standard-cost item is valued at the standard rate, regardless of the document (purchase) rate.

**Example — receive at a price different from standard:**

- Standard rate = **100**
- Purchase Receipt of 10 units billed at **150**
- The stock ledger values the receipt at **100** → stock value increases by **1,000** (not 1,500).

### Accounting — the Purchase Price Variance

The gap between the **document/purchase rate** and the **standard rate** is the *purchase price variance*, and it is posted to the company's **Default Purchase Price Variance Account** (or the item-level override, if set).

**Example — receive 1 unit @ 200, standard 130 (perpetual inventory):**


| Account                       | Debit | Credit |
| ----------------------------- | ----- | ------ |
| Stock (warehouse asset)       | 130   |        |
| Purchase Price Variance       | 70    |        |
| Stock Received But Not Billed |       | 200    |


> The 70 difference lands in **Purchase Price Variance**, *not* in Cost of Goods Sold. This applies to **Purchase Receipts**, and to **Purchase Invoices with "Update Stock"** (both when billed against a receipt and when stand-alone).
>
> **Prerequisite:** the company must have a **Default Purchase Price Variance Account** configured (or an item-level Purchase Price Variance account). If neither is set, the transaction is blocked with a clear error so the variance is never mis-booked.

### Accounting — manufacturing variance

When you manufacture, the finished good is valued at **its own standard rate**, not at the rolled-up cost of the consumed raw materials. Any difference between consumed input value and produced output value is a **manufacturing variance**, posted to the company's **Stock Adjustment** account.

**Example — consume 5 RM @ standard 50 (=250) to produce 1 FG @ standard 200:**

- FG is valued at **200**.
- The **50** difference is booked to **Stock Adjustment**.

### Revaluation on rate change

Publishing a new Item Standard Cost re-values on-hand stock in **every warehouse** to the new rate via the auto-generated revaluation Stock Reconciliation, and posts the gain/loss to **Stock Adjustment**. Serial- and batch-tracked items are revalued across all warehouses too, without requiring serial/batch bundles for the revaluation.

---

## 6. The rules that protect standard-cost integrity

Standard Cost achieves its speed and stability by enforcing a few rules. Understanding *why* they exist makes them easy to live with.

### 6.1 You cannot backdate a transaction before the latest effective rate

> **Rule (R2):** A standard-cost item's stock transaction **cannot be dated before the effective date of its latest Item Standard Cost.**

**Why.** The fast "no-reposting" guarantee depends on the standard rate being **constant** across the window from the latest effective date to today. If you could insert a transaction *before* a rate change:

1. Later stock ledger entries would span **two different rates**, and the fast single-rate value shift would mis-value the entries posted after the rate change; and
2. More seriously, the **revaluation reconciliation** created at the rate change asserted the on-hand quantity *as it was at that moment*. A backdated entry changes that historical quantity, making the revaluation's quantity snapshot — and its GL impact — **stale**. Correcting it would require a full reposting, which is exactly what Standard Cost is designed to avoid.

So the system blocks the entry with a message like:

> **Backdated Entry Not Allowed**  
> Cannot post Standard Cost item *Item A* on **01-06-2025**: it is before **01-01-2026**, the effective date of its latest Standard Valuation Rate *ISC-2026-0001*.  
> Post this entry on or after **01-01-2026**.

**What to do instead:** post the transaction (or a correcting adjustment) **on or after** the latest effective date.

> **Note:** Backdated entries *within the current rate regime* (on or after the latest effective date, but earlier than today) **are** allowed — they only shift later quantities and are handled by the fast quantity/value update with no reposting.

### 6.2 You cannot cancel old stock transactions — create adjustments instead

Once a Standard Cost is established and later transactions exist, you should **not** try to "fix the past" by cancelling old stock vouchers. Cancelling a historical entry is itself a backdated change to the quantity timeline: it would invalidate the on-hand quantity that every later revaluation relied on, and would force a reposting / revaluation cascade — defeating the purpose of standard costing and risking inconsistent inventory value.

**The correct workflow is forward-looking:** record a **new adjustment entry** (e.g. a Stock Entry or Stock Reconciliation) dated **on or after** the latest effective date to reflect the change. This keeps the historical ledger immutable and the standard-cost timeline intact.

Likewise, **Item Standard Cost records cannot be cancelled.** To change a published rate, **submit a new Item Standard Cost** record with the new rate and a later effective date. The new record's revaluation handles the transition cleanly; the old record stays as the historical rate.

---

## 7. Worked scenarios

### Scenario A — Standard purchasing with price variance

1. Set Item A to *Standard Cost*; create Item Standard Cost rate **100**, effective today.
2. Receive 100 units at a billed rate of **120**.
3. **Result:** stock value rises by `100 × 100 = 10,000`; the `100 × 20 = 2,000` price difference is booked to **Purchase Price Variance**. Your inventory is valued at a clean, predictable 100/unit.

### Scenario B — Annual rate revision

1. Item A has run all year at rate **100** (effective 01-Jan-2025), 500 units on hand across two warehouses.
2. On 01-Jan-2026 you publish a new Item Standard Cost rate **130**.
3. **Result:** a revaluation Stock Reconciliation auto-revalues the 500 on-hand units (in both warehouses) from 100 → 130; the `500 × 30 = 15,000` uplift is posted to **Stock Adjustment**. From 01-Jan-2026, new receipts/issues are valued at 130.
4. You now **cannot** post any Item A stock transaction dated before 01-Jan-2026 (see §6.1). A late invoice for December must be recorded with a posting date on/after 01-Jan-2026, or handled as a forward adjustment.

### Scenario C — Backdated correction within the current regime

1. Latest effective rate is **130** (01-Jan-2026); today is 15-Jan-2026.
2. You discover a missed receipt of 20 units dated 05-Jan-2026.
3. **Result:** allowed. The entry posts at rate 130; later entries' running quantities shift forward and their values are re-derived at 130 — **no reposting job**, fast and stable.

### Scenario D — Manufacturing

1. RM standard **50**, FG standard **200**.
2. Repack consumes 5 RM (value 250) and produces 1 FG.
3. **Result:** FG valued at **200**; the **50** manufacturing variance goes to **Stock Adjustment**.

---

## 8. Limitations, best practices & recommendations

### Limitations

- **No retroactive adoption.** An item with existing stock movement cannot be switched to Standard Cost; enable it before the item transacts.
- **The first rate must precede all movement.** The initial Item Standard Cost can only be created before any stock transaction exists for that item+company.
- **Effective dates are strictly increasing**, must not be in the future, and must be on/after the last stock transaction date.
- **No pre-rate-change backdating.** Transactions cannot be dated before the latest effective rate (§6.1).
- **No cancellation** of Item Standard Cost records, and historical stock vouchers should not be cancelled — use forward adjustments (§6.2).

### Best practices

- **Configure accounts up front:** set the company's **Default Purchase Price Variance Account** and **Stock Adjustment Account** before transacting standard-cost items, so variances are booked correctly and the system never blocks a receipt for a missing account.
- **Review variance accounts periodically.** A consistently large Purchase Price Variance signals that your standard rate has drifted from reality — time to publish a new rate.
- **Plan rate changes for clean cut-over dates** (e.g. period/year start). Because you cannot post before the latest effective date, choose an effective date that follows your last booked transaction, ideally after all prior-period entries are in.
- **Make corrections forward, not backward.** Treat the historical ledger as immutable; reflect any change with a new dated adjustment.
- **Use per-item Purchase Price Variance overrides** (via Item Default) only when an item genuinely needs to separate its variance from the company default.

### When to recommend Standard Cost in production

Standard Cost is most beneficial for organizations that:

- run **high transaction volumes** where FIFO/Moving-Average reposting is slow;
- frequently record **backdated corrections** and need them to be cheap and non-disruptive;
- want **predictable, stable product cost** and a clear, isolated view of **price variances**;
- operate **manufacturing** flows where finished goods should carry a planned standard cost.

It is **less suitable** for pure trading operations where the actual landed cost of each lot is the number that matters most.





# Manufacturing Variance (for Standard Cost items)

---

## 1. What is this feature?

When you use the **Standard Cost** valuation method, every finished good is always valued at a fixed **standard rate** that you set — regardless of what it actually cost to make it.

But the real cost of making it (raw materials consumed + any additional/landed costs) is rarely *exactly* equal to that standard rate. There is almost always a small difference.

That difference is called the **Manufacturing Variance**:

- If making the item **cost more** than its standard rate → **unfavourable** variance (you spent more than planned).
- If making the item **cost less** than its standard rate → **favourable** variance (you spent less than planned).

This feature makes sure that difference is booked to a **dedicated Manufacturing Variance account**, so it is easy to see and report on — instead of being quietly mixed into your general Stock Adjustment / cost accounts.

> It is the manufacturing equivalent of the **Purchase Price Variance** you may already use on Purchase Receipts.

---

## 2. A simple example

You value a finished product at a **standard rate of ₹200**.

To produce **1 unit**, you consume raw materials worth **₹250**.

- Finished good goes into stock at its standard value: **₹200**
- Actual cost consumed: **₹250**
- **Manufacturing Variance = ₹50 (unfavourable)** → booked to the Manufacturing Variance account.

If instead the raw materials had only cost **₹180**, the variance would be **₹20 favourable** (a credit in the variance account).

---

## 3. When does it apply?

It applies automatically to a **Manufacture** or **Repack** Stock Entry whenever the **finished good** uses the **Standard Cost** valuation method.

It does **not** apply to items valued using FIFO or Moving Average — those items simply absorb their real cost as usual, so there is no variance to book.

---

## 4. What you need to set up (one time)

The system needs to know **which account** to record the variance in. You can set this in two places:

1. **Company level (recommended default)**
  - Go to **Company** → open your company.
  - In the **Stock Settings** area, set **Default Manufacturing Variance Account**.
  - This account will be used for all Standard Cost items in that company.
2. **Item level (optional override)**
  - Go to the **Item** → **Item Defaults** section (per company).
  - Set **Manufacturing Variance Account** for that specific item.
  - If set, this takes priority over the company default for that item only.

**Which account should it be?** Usually an **Expense-type** account (for example under *Stock Expense* group), chosen together with your accountant.

---

## 5. What happens if the account is not set?

If a Standard Cost item is manufactured/repacked and **no** Manufacturing Variance account is found (neither on the Item nor on the Company), the system will **stop and show an error** asking you to set one.

This is intentional — it prevents the variance from being posted to the wrong place. Simply set the account (Section 4) and submit again.

---

<!-- page: erpnext/erpnext__stock-adjustment-cogs-with-negative-stock.md -->
---
title: "Stock Adjustment / COGS with Negative Stock"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-adjustment-cogs-with-negative-stock"
updated: "2026-07-27"
---

This section explains how negative stock entries lead to stock adjustments. Many users enter negative stock in the system, often by creating delivery notes without existing stock, enabled by activating the 'allow negative stock' option in Stock Settings. 



They do this to dispatch materials to customers with a delivery receipt. To correct negative stock, they usually record a purchase receipt or material receipt. Most users post purchase entries after the delivery note date, resulting in stock adjustments. For example, consider an item called 'Testing Item Stock Adj' with no initial stock. If a delivery note is created for this item, an error appears requiring a valuation rate. The user temporarily sets the valuation rate to 100 to proceed.

![item master](/files/item master.png)

**Delivery Note** 

![](/files/bUy86PL.png)

Since the stock did not exist, the system used a valuation rate of 100 and recorded the stock on hand as shown below.

![gl-entry-negative-stock](/files/gl-entry-negative-stock.png)

Since the stock is negative, we need to record a purchase entry to correct it. We'll do this by creating a purchase receipt with a rate of 300.

![](/files/9e9U8LG.png)

The purchase receipt entry is now created, but it occurs after the Delivery Note (verify the posting date and time for both). The Delivery Note has a valuation rate of 100, while the Purchase Receipt should have a valuation rate of 300 (reflecting the purchase cost). Since the stock was negative, the system applies a valuation rate of 100 (from the previous Delivery Note) for the Purchase Receipt. If it had used 300, the stock quantity would be zero, but the stock value would incorrectly be 200. To avoid this, the system uses a valuation rate of 100, and the discrepancy of 200 is recorded as a stock expense in the Stock Adjustment/COGS account.

![cogs:stock_adjustment](/files/cogs:stock_adjustment.png)

## How to Solve the Problem

Either don't use the negative stock feature or make the purchase entry (backdated) before the dispatch entry, so the system will fix the valuation rate of the delivery note and no adjustment entry will be needed for the Purchase Receipt.



![backdated-pr](/files/backdated-pr.png)



On submission of the above back-dated purchase entry, the system will create a reposting entry that will fix the valuation rate of the delivery note. After the reposting, the Delivery Note's Valuation Rate changes from 100 to 300; therefore, the 'Stock In Hand' changes to 300.

![stock-in-hand-after-repost](/files/stock-in-hand-after-repost.png)

<!-- page: erpnext/erpnext__stock-balance-and-stock-account-balance-syncing.md -->
---
title: "Value Out of Sync Error: Stock Balance and Stock Account Balance Syncing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-balance-and-stock-account-balance-syncing"
updated: "2026-07-02"
---

When [Perpetual Inventory](/erpnext/perpetual-inventory) is enabled, ERPNext keeps the stock ledger and the accounting ledger in sync. If the stock balance and the stock account balance do not match for a company, account, or warehouse, ERPNext stops the transaction and shows a **Value Out of Sync** validation message.

This usually means that older stock or accounting entries created a difference between the stock value and the corresponding stock account balance. The mismatch must be corrected before you can continue posting transactions.

## Why this happens

With Perpetual Inventory, every stock movement also affects accounting. For example, a Purchase Receipt, Delivery Note, Stock Entry, or Sales Invoice with stock impact can update both stock and accounts. If one side was changed, cancelled, reposted, or corrected without the other side matching exactly, the two balances can go out of sync.

ERPNext shows the validation message so that new transactions do not build on an incorrect stock valuation or stock account balance.



![Value out of sync validation message in ERPNext](https://docs.frappe.io/files/kh7A7Gv.png)

## How to fix it

1. Read the validation message carefully and identify the company, stock account, warehouse, and difference amount mentioned in the error.
2. Click **Create Journal Entry** from the validation message.
3. Review the accounts and amounts in the Journal Entry created by ERPNext.
4. Update any missing details, such as cost center or other mandatory accounting dimensions.
5. Save and submit the Journal Entry.
6. Retry the transaction that showed the validation message.

The Journal Entry adjusts the accounting balance so that it matches the stock ledger balance. After the correction is submitted, ERPNext should allow the transaction to proceed.



![Creating a Journal Entry to sync stock and stock account balance](https://docs.frappe.io/files/dd0SQji.gif)

## Before submitting the Journal Entry

- Check that the stock account selected in the Journal Entry is the same account mentioned in the validation message.
- Confirm whether the entry should be a debit or credit based on the difference shown in the error.
- Review accounting dimensions such as cost center, project, or finance book if they are enabled in your setup.
- If the difference is large or unexpected, review recent stock and accounting transactions before submitting the adjustment.

## After the correction

Once the Journal Entry is submitted, open the original document again and try to save or submit it. If the same validation message appears for another account, warehouse, or company, repeat the correction for that specific difference.

If the mismatch keeps returning, check whether older stock reposting, cancelled documents, backdated transactions, or custom accounting entries are affecting the same stock account.

<!-- page: erpnext/erpnext__stock-closing-entry.md -->
---
title: "Stock Closing Entry"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-closing-entry"
updated: "2026-02-25"
---

The purpose of the stock closing entry is to generate the stock closing balance, which includes 
the consolidated stock quantity and consolidated stock value for the selected period. This information will be used to generate the stock reports such as Stock Balance and Batch-Wise Balance History in a short span of time.

## How it Works

The user is required to create a stock closing entry for the desired period, which can span one month, half a month, or an entire year. Upon submission of the stock closing entry, the system generates the stock closing balance for the selected period, including item, batch, inventory dimensions and warehouse wise consolidated closing stock quantities and stock values.

Stock Closing Entry

![](/files/stock-closing-entry.png)

Stock reports, such as Stock Balance and Batch-Wise Balance History, use the Stock Closing Balance data to calculate the opening stock, which is significantly faster than calculating the closing stock using the Stock Ledger Entry.


Note: Will be available in v16

<!-- page: erpnext/erpnext__stock-entry-purpose.md -->
---
title: "Stock Entry Purpose\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-entry-purpose"
updated: "2026-03-12"
---

Stock Entry is a stock transaction, which can be used for multiple purposes. Let's learn about each Stock Entry Purpose below.

#### 1.Purpose: Material Issue

Material Issue entry create to issue item(s) from a warehouse. On submission of Material Issue, stock of item is deducted from the Source Warehouse.

Material Issue is generally made for the low value consumable items like office stationary, product consumables etc. Also you can create Material Issue to reconcile serialized and batched item's stock.

![Material Issue](/files/stock-entry-issue.png)

#### 2.Purpose: Material Receipt

Material Receipt entry is created to inward stock of item(s) in a warehouse. This type of stock entry can be created for updating opening balance of serialized and batched item. Also items purchased without Purchase Order can be inwarded from Material Receipt entry.

For the stock valuation purpose, provided Item Valuation becomes a mandatory field in the Material Receipt entry.

![Material Receipt](/files/stock-entry-receipt.png)

#### 3.Purpose: Material Transfer

Material Transfer entry is created for the inter-warehouse Material Transfer.

![Material Transfer](/files/stock-entry-transfer.png)

#### 4.Purpose: Material Transfer for Manufacture

In the manufacturing process, raw-materials are issued from the stores to the production department (generally WIP warehouse). This Material Transfer entry is created from Work Order. Items in this entry are fetched from the BOM of production Item, as selected in Work Order.

![Transfer for Manufacture](/files/stock-entry-manufacture-transfer.gif)

#### 5.Purpose: Manufacture

Manufacture is created from Work Order. In this entry, both raw-material item as well as production item are fetched from the BOM, selected in the Work Order. For the raw-material items, only Source Warehouse (generally WIP warehouse) is mentioned. For the production item, only target warehouse as mentioned in the Work Order is updated. On submission, stock of raw-material items are deducted from Source Warehouse, which indicates that raw-material items were consumed in the manufacturing process. Production Item is added to the Target Warehouse marking the completion of production cycle.

![Manufacture](/files/stock-entry-manufacture.gif)

#### 6.Purpose: Repack

Repack Entry is created when items purchases in bulk is repacked under smaller packs. [Check this page to know more about Repack entry.](/erpnext/repack-entry.html)

#### 7.Purpose: Subcontract

Subcontracting transaction involves company transfer raw-material items to the sub-contractors warehouse. This requires adding a warehouse for the sub-contractor as well. Sub-contract entry transfers stock from the companies warehouse to the sub-contractors warehouse. [Check this page to know more about Subcontracting](/erpnext/subcontracting.html).

![Subcontract](/files/stock-entry-subcontract.gif)

<!-- page: erpnext/erpnext__stock-entry.md -->
---
title: "Stock Entry"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-entry"
updated: "2026-04-03"
---

**A Stock Entry lets you record Item movement between Warehouses.**

To access the Stock Entry list, go to: 

> Home > Stock > Stock Transactions > Stock Entry

Stock Entries can be made for the following purposes:

- **Material Issue**: If the material is being issued to someone in or outside the company (**Outgoing Material)**. The Items will be deducted from the Warehouse set under Source Warehouse.
- **Material Receipt**: If the material is being received (Incoming Material). The Items will be added to the Warehouse set under Target Warehouse.
- **Material Transfer**: If the material is being moved from one internal Warehouse to another.
- **Material Transfer for Manufacturing**: If raw materials are being transferred for manufacturing. The transfer can happen against a [Work Order](/erpnext/work-order) or a [Job Card](/erpnext/job-card). To know more, visit the [Bill Of Materials](/erpnext/bill-of-materials) page.
- **Material Consumption for Manufacture**: There can be multiple consumption stock entries against a manufacturing Work Order. [Refer this link for more details](/erpnext/material_consumption)
- **Manufacture**: If the Material is being received from a Manufacturing/Production Operation.
- **Repack**: If the Original item/items are being repacked into new item/items.
- **Send to Subcontractor**: If the Material is being issued for a sub-contract activity. This entry is made from a Purchase Order. To know more, visit the [subcontracting](/erpnext/subcontracting) page.

To know more in detail about the stock entry purpose, [visit this page](/erpnext/user/manual/en/stock-entry-purpose).

1. Prerequisites

---

Before creating and using a Stock Entry, it is advised that you create the following first:

- [Warehouse](/erpnext/warehouse)
- [Item](/erpnext/item)

2. How to create a Stock Entry

---

Stock Entries for Manufacturing purposes are usually created from a [Work Order](/erpnext/work-order). To create a Stock Entry manually for other purposes, follow these steps:

1. Go to the Stock Entry list, click on New.
2. Select the Stock Entry Purpose from the ones listed above.
3. If you set the Default Source or Target Warehouses, they'll be automatically filled for the rows in the Items table.
4. Source/Target Warehouses will be available as per the Stock Entry Purpose you selected.
5. Select Items and enter a quantity.
6. The basic rate will be fetched and the amount will be calculated automatically.
7. Save and Submit.

![Stock Entry](/files/stock-entry.png)

Usually, "Source Warehouse" and "Target Warehouse" both are set for recording a movement.

### 2.1 Additional options when creating a Stock Entry

- **Work Order**: If this is a Manufacturing entry, the Work Order will be shown in this field.
- **Edit Posting Date and Time**: Will allow you to edit the Stock Entry's date and time.
- **Inspection Required**: If a [Quality Inspection](/erpnext/quality-inspection) needs to be performed on the Items before submitting the Stock Entry.
- **From BOM**: If this is a Manufacturing entry, the associated BOM for the Item being manufactured will be shown.

### 2.2 Stock Entry Type

You can also create a Stock Entry Type where only the name will be different, for example 'Scrap Entry'. The purpose will be Material Transfer but the name will be different. This is useful if you want certain Users to have access only to specific actions related to stock.

![Stock Entry Type](/files/stock-entry-type.png)



3. Features

---

### 3.1 The Items table

Details about the Item, Rate, Quantity, etc. will be shown here.

Ticking on 'Allow Zero Valuation Rate' will allow submitting the Stock Entry even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

Different Source and Target Warehouses can be set for different Items.

![](/files/imaged7013f.png)

### 3.2 Scrap and Process Loss

- **Scrap Item**: Scrap items are the by-product and can be treated as products. The scrap items will have the valuation rate and they will be added to the scrap warehouse. Users can set the valuation rate for the scrap item manually in the Basic Rate field.
- **Process Loss**: Process Loss has no impact on the stock, this will reduce the number of FG Items. Check the below image, the user has planned to produce 100 FG Items but after the manufacturing process, the quantity has been produced as 80. To produce 80 FG Items, the user has used all raw material quantity. So here 20 quantity has been produced so therefore the system has marked it as Process Loss Qty. The process loss cost of 20 quantities has been added to the 80 quantities of FG Item.

![](/files/CleanShot 2026-04-03 at 10.44.32@2x.png)

### 3.3 Additional Costs

If the stock entry is an incoming entry i.e any item is receiving at a target warehouse, you can add related additional costs (like Shipping Charges, Customs Duty, Operating Costs, etc) associated with the process. The additional costs will be considered to calculate the Valuation Rate of the items.

To add additional costs:

1. Select the Expense Account to which the expense from this Stock Entry will be recorded.
2. Enter the description and amount of the cost in the Additional Costs table.

![Stock Entry Additional Costs](/files/additional-costs-table.png)



The added Additional Costs will be distributed among the receiving items (where the Target Warehouse mentioned) proportionately based on the Basic Amount of the items. And the distributed additional cost will be added to the basic rate of the item, to calculate Valuation Rate.

Quantity and Rate is shown as follows when you expand the Items table. 

![Stock Entry Item Valuation Rate](/files/stock-entry-item-valuation-rate.png)



### 3.4 Accounting Dimensions

You can tag different transactions based on different dimensions. By default, [Projects](/erpnext/project) can be considered as a dimension as it is a common practice to track costs of different projects. To know more about Accounting Dimensions, [visit this page](/erpnext/accounting-dimensions).

### 3.5 Printing Settings

#### Letterhead

You can print your Purchase Receipt on your company's letterhead. Know more [here](/erpnext/letter-head).

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/erpnext/print-headings).

### 3.6 More Information

- **Is Opening**: If this entry is the opening stock entry for the Items.
- **Remarks**: Any additional remarks about the Item.
- **Percentage Transferred**: The percentage of Items transferred depending on Stock Entry purpose.
- **Total Amount**: The total amount of Items transferred.

### 3.7 Perpetual Inventory

If the perpetual inventory system is enabled, additional costs will be booked in Expense Account mentioned in the Additional Costs table .

![Additional Costs General Ledger](/files/stock-entry-additional-cost.png)



![Additional Costs General Ledger](/files/additional-costs-general-ledger.png)



### 3.8 After Submitting

After submitting a Stock Entry, you can go to the stock ledger or the accounting ledger from the dashboard.

![Additional Costs General Ledger](/files/stock-entry-submit.png)



4. Add to Transit

---

If you want to transfer materials from one warehouse to another and you want to make two entries for that then use "Add to Transit" feature.

To use "Add to Transit" feature, make stock entry with type as "Material Transfer" and enable "Add to Transit" checkbox. Next you need to select the source warehouse from where you want to issue the material and then select the warehouse of type "Transit" in the target warehouse. To make transit warehouse you can goto the Warehouse master and select the warehouse type as "Transit". After that add items in the stock entry which needs to be transfer and submit it.

![](/files/CleanShot 2026-04-03 at 11.01.51@2x.png)

To make second stock entry at the destination warehouse, users has two options. Either they can open the Original Stock Entry and click on "End Transit" or they can create new stock entry and click on "Get Items From" -> "Transit Stock Entry". System will fetch items from the original stock entry with the source warehouse (Transit warehouse) same as traget warehouse from the original stock entry. User has to set the target warehouse and save.

![](/files/CleanShot 2026-04-03 at 11.02.51@2x.png)

5. How to update a Stock Entry

---

Once a stock entry is submitted, it can be updated by cancelling and amending the entry

6. Video

---

### 5. Related Topics

1. [Stock Entry Purpose](/erpnext/stock-entry-purpose)
2. [Stock Reconciliation](/erpnext/stock-reconciliation)
3. [Opening Stock Balance Entry For Serialized And Batch Item](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
4. [Stock Reconciliation](/erpnext/stock-reconciliation)
5. [Work Order](/erpnext/work-order)
6. [Production Plan](/erpnext/production-plan)
7. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__stock-inspection.md -->
---
title: "Stock Inspection"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-inspection"
updated: "2026-02-26"
---

Quality inspection in ERPNext stock module involves assessing and ensuring the quality of incoming and outgoing inventory items.

When items are received into stock, quality inspectors can perform inspections based on predefined criteria such as physical condition, specifications, or regulatory standards. Inspection results can be recorded, and items can be accepted, rejected, or placed on hold based on the inspection outcome.

During outgoing transactions such as sales or transfers, quality inspections can be conducted to verify that items meet specified quality standards before being shipped or transferred.

ERPNext facilitates the creation of inspection criteria, inspection plans, and inspection certificates to streamline the quality control process.

* Quality Inspection Template
* [Quality Inspection](/erpnext/user/manual/en/quality-inspection)

<!-- page: erpnext/erpnext__stock-ledger.md -->
---
title: "Stock Ledger Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-ledger"
updated: "2026-02-26"
---


**A Stock Ledger Report is a detailed record that keeps track of stock movements for a company.**

Inward or outward transactions related to Manufacturing, Purchasing, Selling, and Stock Transfers are recorded in the Stock Ledger which then is reflected in the Stock Ledger Report.

It reflects the quantity and value of stock **issued, received, or transferred** along with the stock item and its warehouse details.

It can be referred when the **Perpetual Inventory** system is enabled, as this report reflects the history of all your stock transactions. It presents a more granular view of the stock transactions.

## Stock Ledger Report Attributes

* **Incoming Rate**: It reflects the actual value of the stock at which it was brought under your inventory.
It reflects the same value as entered in the *Rate* field of the document.

* **Balance Value**: It represents the total value of the remainder stock in the inventory. It is the product of Valuation Rate and Balance Quantity of a stock item.

* **Valuation Rate**: It is calculated based upon the valuation method selected.

Here is how Stock Ledger Report represents a **Stock Entry** of type *Material Receipt*.

![Stock Ledger Report](/files/stock-ledger.png)

It reflects an item **Chair** of quantity *1000 units* with Incoming Rate (Basic Rate) as *Rs.3000* received in warehouse *Stores - L* along with calculating Valuation Rate and Balance Value.

You can click on **Voucher #** to open the document this transaction was created from.

Stock Ledger entries are generated from the following transactions:

- Sales Invoice, Purchase Invoice (with *Update Stock* checked)
- Delivery Note
- Purchase Receipt
- Stock Entry
- Stock Reconciliation

You can add fields from the previously mentioned Document Types by clicking on Menu > Add Column.

<!-- page: erpnext/erpnext__stock-level-report.md -->
---
title: "Stock Level Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stock-level-report"
updated: "2026-02-26"
---

Stock Level report list stock item's quantity available in a particular warehouse.

There are multiple reports available you can check for item's stock level.

#### Stock Projected Quantity Report

This report list item wise - warehouse wise stock level of an item considering all the stock transactions. With Actual Quantity of an item, it also provide other details like:

1. Actual Qty: Quantity available in the warehouse.
2. Planned Qty: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
3. Requested Qty: Quantity requested for purchase, but not ordered.
4. Ordered Qty: Quantity ordered for purchase, but not received.
5. Reserved Qty: Quantity ordered for sale, but not delivered.
6. Project Qty: Project Quantity is calculated as

Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty

The projected inventory is used by the planning system to monitor the reorder point and to determine the reorder quantity. The projected Quantity is used by the planning engine to monitor the safety stock levels. These levels are maintained to serve unexpected demands.

Having a tight control of the projected inventory is crucial to determine shortages and to calculate the right order quantity.
