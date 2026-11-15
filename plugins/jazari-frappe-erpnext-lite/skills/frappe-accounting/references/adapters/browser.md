# Interface adapter — Accounting, invoicing and tax

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Raise a sales invoice
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Sales Invoice**, or type *Sales Invoice* in the search bar at the top
- **Record type:** Sales Invoice
- **Documented steps:**
  1. Go to Accounting > Sales and Receivables > Sales Invoice
  2. Click Add Sales Invoice
  3. Select the Company and Customer. ERPNext fetches the Customer's billing address, contact, currency, price list, and receivable account when defaults exist
  4. Check the Posting Date and Payment Due Date. The posting date decides the accounting period. The due date is used to determine whether the invoice is overdue
  5. In Items, add each product or service. Check the Quantity, Rate, Amount, and Warehouse
  6. Click the pencil icon to edit a row. This opens fields that do not fit in the table, including UOM, Income Account, Cost Center, Project, Warehouse, serial or batch details, and deferred revenue settings
  7. Add the applicable taxes or select a Sales Taxes and Charges Template. Review the tax amount and Grand Total
  8. Open the Payments tab. Review the payment schedule, allocate any advances, and confirm the payment terms
  9. Review the billing and shipping addresses, Customer purchase order details, currency, terms, and totals
  10. Save the draft, then click Submit when the invoice is ready to affect the books
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-52.md` lines 306–524  (https://docs.frappe.io/erpnext/sales-invoice)

### Record a purchase invoice
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Purchase Invoice**, or type *Purchase Invoice* in the search bar at the top
- **Record type:** Purchase Invoice
- **Documented steps:**
  1. Go to Accounting > Purchase Invoice
  2. Select Add Purchase Invoice
  3. Select the Supplier. ERPNext fetches the payable account, currency, price list, addresses, and payment terms from the relevant defaults
  4. Enter the Supplier's invoice number in Supplier Invoice No and its date in Supplier Invoice Date. Use the date printed on the Supplier's bill, not the date on which you enter it
  5. Review the Posting Date and Due Date
  6. Add the Items. Enter the billed quantity and rate, then verify the expense account, Cost Center, Warehouse, and tax treatment
  7. Review taxes, discounts, additional charges, payment schedule, rounding, and the Grand Total
  8. Save the draft and compare it with the Supplier's bill
  9. Select Submit when the document is correct
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-47.md` lines 3–202  (https://docs.frappe.io/erpnext/purchase-invoice)

### Issue a credit note
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Sales Invoice**, or type *Sales Invoice* in the search bar at the top
- **Record type:** Sales Invoice
- **Documented steps:**
  1. Open the original Sales Invoice
  2. Select Create > Return / Credit Note
  3. Review the Customer, Company, posting date, return Warehouse, and reference invoice
  4. Keep only the returned lines and enter the returned quantity. ERPNext displays return quantities and amounts as negative values
  5. Enable Update Stock when the goods physically return to inventory
  6. Review taxes and totals, then save and submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-15.md` lines 715–814  (https://docs.frappe.io/erpnext/credit-note)

### Issue a debit note
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Purchase Invoice**, or type *Purchase Invoice* in the search bar at the top
- **Record type:** Purchase Invoice
- **Documented steps:**
  1. Open the submitted Purchase Invoice that must be reduced
  2. Select Create > Return / Debit Note
  3. ERPNext creates a new Purchase Invoice with Is Return (Debit Note) selected and Return Against Purchase Invoice linked to the original invoice. Verify both fields before changing the Items
  4. Keep only the Items being returned. Remove unaffected rows
  5. Enter the return quantity as a negative number. For example, use `-2` to return two units from an original quantity of ten
  6. Select the pencil icon on the Item row to open the full row editor. Verify the returned quantity, original rate, Warehouse, expense account, Cost Center, and source-document references
  7. If the return must move stock out, select Update Stock and verify the Warehouse. Leave it clear when stock was already returned through a Purchase Return against the Purchase Receipt
  8. Review taxes and totals. A return should have negative amounts
  9. Save and submit the Debit Note
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-19.md` lines 3–148  (https://docs.frappe.io/erpnext/debit-note)

### Record a payment entry
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Payment Entry**, or type *Payment Entry* in the search bar at the top
- **Record type:** Payment Entry
- **Documented steps:**
  1. Select Receive, Pay, or Internal Transfer
  2. Set the Company, posting date, Mode of Payment, and party
  3. Check the paid-from and paid-to accounts and currencies
  4. Enter the amount and reference details
  5. Use Get Outstanding Invoices or add references manually
  6. Review allocations and deductions, then submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-40.md` lines 353–551  (https://docs.frappe.io/erpnext/payment-entry)

### Send a payment request
- **Path (checked on v16.55):** https://your-site/desk → type *Payment Request* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open the submitted Sales Order or Sales Invoice
  2. Choose Create > Payment to create the Payment Request
  3. Confirm the amount, currency, recipient, and reference document
  4. Select the payment gateway account when collecting online
  5. Save and send the request
  6. Track its status and verify the resulting payment before treating the source document as paid
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-41.md` lines 164–306  (https://docs.frappe.io/erpnext/payment-request)

### Post a journal entry
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Journal Entry**, or type *Journal Entry* in the search bar at the top
- **Record type:** Journal Entry
- **Documented steps:**
  1. Open the Journal Entry list and select Add Journal Entry
  2. Select the Company, Entry Type, and Posting Date. For a general adjustment, keep Entry Type as Journal Entry
  3. In Accounting Entries, add the account to debit and enter the debit amount. Add the offsetting account and enter the credit amount. Total Debit and Total Credit must be equal before submission
  4. In the row editor, confirm the Account and enter either a debit or a credit, never both on the same row. In the example, Office Maintenance Expenses is debited by $845
  5. Add a clear User Remark and, when applicable, a Reference Number, Reference Date, Bill Number, Bill Date, and Due Date. These supporting fields do not replace a formal link to an ERPNext document
  6. Save, review the accounts and dimensions, then submit. Submission posts the debit and credit to the General Ledger
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-34.md` lines 395–566  (https://docs.frappe.io/erpnext/journal-entry)

### Set payment terms
- **Path (checked on v16.55):** https://your-site/desk → type *Payment Term* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open Payment Terms Template
  2. Add terms in the required order
  3. Enter the invoice portion for each row
  4. Confirm that the total allocation is 100%
  5. Mark it as default only if it should apply broadly
  6. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-41.md` lines 402–476  (https://docs.frappe.io/erpnext/payment-terms)

### Reconcile the bank
- **Path (checked on v16.55):** https://your-site/desk → type *Bank Reconciliation Tool* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Select the Company Bank Account and statement date range
  2. Import or synchronize Bank Transactions
  3. Match each statement line with the correct Payment Entry, Journal Entry, or other supported voucher
  4. Create a missing voucher only after checking that it does not already exist
  5. Record bank fees, interest, and timing differences explicitly
  6. Confirm that the closing balance agrees with the bank statement
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-08.md` lines 735–822  (https://docs.frappe.io/erpnext/bank-reconciliation)

### Reconcile payments against invoices
- **Path (checked on v16.55):** https://your-site/desk → type *Payment Reconciliation* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-41.md` lines 3–162  (https://docs.frappe.io/erpnext/payment-reconciliation)

### Enter opening balances
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Journal Entry**, or type *Journal Entry* in the search bar at the top
- **Documented steps:**
  1. Go to Home > Accounting > General Ledger > Journal Entry
  2. Create a Journal Entry
  3. Select the Company and cutover date
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-39.md` lines 390–493  (https://docs.frappe.io/erpnext/opening-balance)

### Import opening invoices
- **Path (checked on v16.55):** https://your-site/desk → type *Opening Invoice Creation Tool* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Go to Home > Accounting > Opening and Closing > Opening Invoice Creation Tool
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-39.md` lines 495–610  (https://docs.frappe.io/erpnext/opening-invoice-creation-tool)

### Set up cost centers
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Setup > Chart of Cost Centers**, or type *Cost Center* in the search bar at the top
- **Record type:** Cost Center
- **Documented steps:**
  1. Select the parent Cost Center
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-15.md` lines 3–98  (https://docs.frappe.io/erpnext/cost-center)

### Set and track a budget
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Budgeting > Budget**, or type *Budget* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-11.md` lines 541–701  (https://docs.frappe.io/erpnext/budget)

### Use accounting dimensions
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Setup > Accounting Dimension**, or type *Accounting Dimension* in the search bar at the top
- **Documented steps:**
  1. Open the Accounting Dimension list and select Add Accounting Dimension
  2. Select the Reference Document Type. ERPNext uses records from this DocType as the available dimension values
  3. Confirm the Dimension Name, then save. ERPNext creates the corresponding fields on accounting transactions and supported reports
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-01.md` lines 226–369  (https://docs.frappe.io/erpnext/accounting-dimensions)

### Close an accounting period
- **Path (checked on v16.55):** https://your-site/desk → type *Period Closing Voucher* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open Period Closing Voucher and click Add Period Closing Voucher
  2. Select the company and the fiscal year being closed
  3. Set the posting date to the last day of the period
  4. Select the closing account that will receive the net profit or loss
  5. Enable Book Cost Center Wise Profit/Loss when retained earnings must preserve the cost center split
  6. Add a clear remark, save, review, and submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-42.md` lines 3–85  (https://docs.frappe.io/erpnext/period-closing-voucher)

### Freeze accounting entries
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Setup > Settings**, or type *Accounts Settings* in the search bar at the top
- **On this screen:** On the Accounts Settings form, the date field is **Accounts Frozen Till Date**.
- **Documented steps:**
  1. Open the Company record
  2. Open the Accounts Closing tab
  3. Set Accounts Frozen Till Date to the last protected date
  4. Select Roles Allowed to Set and Edit Frozen Account Entries
  5. Save the Company and test with a non-privileged account before relying on the control
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-27.md` lines 633–688  (https://docs.frappe.io/erpnext/freeze-accounting-entries)

### Set up deferred revenue and expense
- **Path (checked on v16.55):** https://your-site/desk → type *Process Deferred Accounting* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open the invoice and confirm the deferred account and service dates on each affected row
  2. Review the Deferred Revenue/Expense Report for invoiced, recognized, and pending amounts
  3. Open the General Ledger for the deferred account and the final income or expense account
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-19.md` lines 252–410  (https://docs.frappe.io/erpnext/deferred-accounting)

### Chase overdue invoices with dunning
- **Path (checked on v16.55):** https://your-site/desk → type *Dunning* in the search bar at the top and open the doctype
- **Record type:** Dunning
- **Documented steps:**
  1. Open the overdue Sales Invoice
  2. Select Create > Dunning
  3. Review the overdue payment schedule rows fetched into the document
  4. Select a Dunning Type, or enter the fee, interest, and letter text manually
  5. Save and submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-23.md` lines 386–490  (https://docs.frappe.io/erpnext/dunning)

### Send a statement of accounts
- **Path (checked on v16.55):** https://your-site/desk → type *Process Statement Of Accounts* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Search for Process Statement Of Accounts and select Add Process Statement Of Accounts
  2. Enter a recognizable Name
  3. Select the report and set the date, Company, account, currency, Cost Center, or Project filters
  4. Use Categorize By to control how entries are grouped in the PDF
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-44.md` lines 568–672  (https://docs.frappe.io/erpnext/process-statement-of-accounts)

### Bill customers on a subscription
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > Subscription**, or type *Subscription* in the search bar at the top
- **Record type:** Subscription
- **Documented steps:**
  1. Search for Subscription and select Add Subscription
  2. Select Customer or Supplier, then choose the Party and Company
  3. Enter the subscription start date and, if applicable, the end date
  4. Configure when invoices should be generated
  5. Add one or more Subscription Plans
  6. Add taxes, a Cost Center, or an additional discount when needed
  7. Save
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-61.md` lines 735–838  (https://docs.frappe.io/erpnext/subscription)

### Manage fixed assets
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Assets > Asset**, or type *Asset* in the search bar at the top
- **Record type:** Asset
- **Documented steps:**
  1. Open Asset and select Add Asset
  2. Select the Item and company
  3. Enter a recognizable Asset Name and current Location
  4. Select Existing Asset only when bringing an already-owned asset into ERPNext. Use Composite Asset when the asset is assembled by capitalization
  5. Enter purchase and available-for-use dates, value, and quantity
  6. Enable maintenance and depreciation only when they apply
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-07.md` lines 254–357  (https://docs.frappe.io/erpnext/asset)

### Run asset depreciation
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Assets > Asset**, or type *Asset* in the search bar at the top
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-06.md` lines 407–498  (https://docs.frappe.io/erpnext/asset-depreciation)

### Track shareholders and share transfers
- **Path (checked on v16.55):** https://your-site/desk → type *Share Transfer* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-58.md` lines 67–140  (https://docs.frappe.io/erpnext/share-transfer)

### Set up taxes
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Sales Tax Template**, or type *Sales Taxes and Charges Template* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-57.md` lines 755–833  (https://docs.frappe.io/erpnext/setting-up-taxes)

### Create a sales tax template
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Sales Tax Template**, or type *Sales Taxes and Charges Template* in the search bar at the top
- **Record type:** Sales Taxes and Charges Template
- **Documented steps:**
  1. Enter a clear Title, such as Nova Standard Sales Tax 8%
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-54.md` lines 510–706  (https://docs.frappe.io/erpnext/sales-taxes-and-charges-template)

### Create a purchase tax template
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Purchase Tax Template**, or type *Purchase Taxes and Charges Template* in the search bar at the top
- **Documented steps:**
  1. Enter a clear Title, such as Nova Standard Purchase Tax 5%
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-48.md` lines 3–215  (https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template)

### Set item-level tax
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Item Tax Template**, or type *Item Tax Template* in the search bar at the top
- **Record type:** Item Tax Template
- **Documented steps:**
  1. Enter a descriptive Title, such as Nova Reduced Item Tax 4%
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-33.md` lines 3–215  (https://docs.frappe.io/erpnext/item-tax-template)

### Use tax categories
- **Path (checked on v16.55):** https://your-site/desk → type *Tax Category* in the search bar at the top and open the doctype
- **Record type:** Tax Category
- **Documented steps:**
  1. The preferred billing or shipping Address selected by Determine Address Tax Category from
  2. The other applicable transaction context and party Address
  3. The Tax Category on the Customer or Supplier when no Address category is available
  4. A category manually selected on the transaction
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-63.md` lines 3–195  (https://docs.frappe.io/erpnext/tax-category)

### Apply tax rules automatically
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Tax Rule**, or type *Tax Rule* in the search bar at the top
- **Record type:** Tax Rule
- **Documented steps:**
  1. Set Tax Type to Sales or Purchase
  2. Select the corresponding Sales Tax Template or Purchase Tax Template
  3. Enable Use for Shopping Cart only when the rule must also apply to website checkout transactions
  4. Add the conditions that identify the intended transaction
  5. Set validity dates when the rule is temporary or changes by tax period
  6. Set the priority and company
  7. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-63.md` lines 566–765  (https://docs.frappe.io/erpnext/tax-rule)

### Set up withholding tax
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Taxes > Tax Withholding Category**, or type *Tax Withholding Category* in the search bar at the top
- **Record type:** Tax Withholding Category
- **Documented steps:**
  1. Create a Payment Entry with Payment Type Pay
  2. Select Party Type Supplier and the supplier
  3. Enter the advance amount before withholding
  4. Select Consider for Tax Withholding
  5. Confirm the Tax Withholding Category
  6. Save and review the generated Tax Withholding Entry before submission
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-64.md` lines 3–239  (https://docs.frappe.io/erpnext/tax-withholding-category)

### Set up UAE VAT
- **Path (checked on v16.55):** https://your-site/desk → type *UAE VAT Settings* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Select the correct Customer and Item and the address where the transaction will happen
  2. Check if the TRN of your Company and Supplier have been correctly set
  3. Check if the TAX Code has been set in the Item
  4. Select the template that you have created based on the type of transaction
  5. Save and Submit the Invoice
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-66.md` lines 287–343  (https://docs.frappe.io/erpnext/uae-vat-setup)

### Set up KSA VAT reporting
- **Path (checked on v16.55):** **Not part of ERPNext v16.** KSA VAT Setting and the KSA VAT report moved out of ERPNext into a separate app (Frappe's `KSA` app; ZATCA e-invoicing apps are made by other vendors). Check `installed_apps` first. If none of them is installed, say so plainly and do not improvise the report.
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-58.md` lines 718–751  (https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting)

## What cannot be done in the interface

- Handle multi-currency accounting — an explanation, not an action (guide.md)
