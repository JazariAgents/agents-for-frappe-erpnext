<!-- Frappe documentation: erpnext, part 47 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__purchase-invoice.md -->
---
title: "Purchase Invoice | ERPNext Documentation"
description: "Create, verify, submit, pay, return, and track supplier Purchase Invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-invoice"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, sends a bill for phone screens that have already been received. Until that bill is recorded, Nova Industries has stock but no formal payable showing how much it owes the supplier.



A Purchase Invoice records the supplier's bill, creates the payable, and posts the expense, asset value, and taxes. It can be created from a Purchase Order, a Purchase Receipt, or entered directly.



Use a Purchase Invoice when a supplier has billed your company for goods or services. Submission updates the supplier balance and the General Ledger.



## Before you begin

You need:

- a [Supplier](/erpnext/supplier) with the correct currency and payment terms;
- Items or expense accounts for the purchase;
- a Company with a default payable account and Cost Center;
- applicable [Purchase Taxes and Charges Templates](/erpnext/purchase-taxes-and-charges-template);
- a Purchase Order or Purchase Receipt when the invoice must update an earlier buying document.

Confirm whether the goods have already been received. If a Purchase Receipt exists, invoice from it. If goods and the bill arrive together, you may use **Update Stock** on the Purchase Invoice instead of creating a separate receipt.

## Create a Purchase Invoice

1. Go to **Accounting &gt; Purchase Invoice**.
2. Select **Add Purchase Invoice**.

[Screenshot on the live page: Purchase Invoice list with Add Purchase Invoice highlighted]

3. Select the **Supplier**. ERPNext fetches the payable account, currency, price list, addresses, and payment terms from the relevant defaults.
4. Enter the Supplier's invoice number in **Supplier Invoice No** and its date in **Supplier Invoice Date**. Use the date printed on the Supplier's bill, not the date on which you enter it.
5. Review the **Posting Date** and **Due Date**.

[Screenshot on the live page: Supplier, bill reference, and due date on a Purchase Invoice]

6. Add the Items. Enter the billed quantity and rate, then verify the expense account, Cost Center, Warehouse, and tax treatment.

The colored dot before an Item Code shows stock availability at a glance. Green means in stock and red means out of stock.

Select the highlighted pencil icon to open the full Item row. This is where you can review fields that are not shown as columns in the table.

[Screenshot on the live page: Purchase Invoice Items table with the row pencil highlighted]

Check the **Accepted Qty**, **Rate**, UOM, expense account, Cost Center, and any linked Purchase Order or Purchase Receipt row. ERPNext calculates the amount from the quantity and rate.

[Screenshot on the live page: Quantity and rate in a Purchase Invoice Item row]

7. Review taxes, discounts, additional charges, payment schedule, rounding, and the Grand Total.
8. Save the draft and compare it with the Supplier's bill.
9. Select **Submit** when the document is correct.

## Alternative ways to create a Purchase Invoice

### From a Purchase Order

Open a submitted Purchase Order and select **Create &gt; Purchase Invoice**. ERPNext copies the Supplier, Items, quantities, rates, taxes, and references. Adjust only the quantities that are being billed now. This method updates the order's billed percentage after submission.

Use this route when the invoice arrives before receipt, or when your business does not use Purchase Receipts for that purchase.

### From a Purchase Receipt

Open a submitted Purchase Receipt and select **Create &gt; Purchase Invoice**. This carries the received quantities and receipt references into the invoice. The invoice normally clears the **Stock Received But Not Billed** value created by the receipt and establishes the Supplier payable.

This is the preferred route when receiving and invoice verification are separate responsibilities.

### Using Get Items From

In a new Purchase Invoice, select **Get Items From** to fetch one or more eligible Purchase Orders or Purchase Receipts for the same Supplier. Use this when a single Supplier invoice covers several orders or receipts.

### Direct Purchase Invoice

Create the invoice directly when there is no preceding order or receipt, such as a utility bill, professional service, rent, or a small approved expense. A direct invoice creates the payable but does not update a Purchase Order's billed status.

### Recurring supplier invoices

Use [Auto Repeat](/erpnext/auto-repeat) or a Supplier [Subscription](/erpnext/subscription) for recurring charges. Choose Auto Repeat when you want scheduled copies of a reference document. Choose Subscription when billing follows a defined subscription plan and service period.

## Important fields and what they mean


| Field                        | What it controls                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Supplier                     | The party to whom the amount is payable. It also provides currency, payable account, tax, and payment defaults.                                  |
| Supplier Invoice No          | The Supplier's own bill reference. It helps prevent duplicate entry and supports audit matching.                                                 |
| Supplier Invoice Date        | The date on the Supplier's bill. Use it for document reference and ageing controls.                                                              |
| Posting Date and Time        | The accounting and optional stock posting date. Closed periods and frozen accounts can restrict it.                                              |
| Due Date                     | The date by which payment is expected. Payment terms can calculate it automatically.                                                             |
| Credit To                    | The payable ledger credited when the invoice is submitted. Normally use a common payable account with the Supplier recorded as the party.        |
| Update Stock                 | Posts receipt of stock through the Purchase Invoice. Leave it clear when a Purchase Receipt already records the stock movement.                  |
| Is Paid                      | Records payment with the invoice when this workflow is enabled and the required payment account is selected.                                     |
| Is Return (Debit Note)       | Converts the Purchase Invoice into a Debit Note that reduces or reverses a Supplier bill.                                                        |
| Apply Tax Withholding Amount | Calculates configured Supplier withholding tax. Verify the category and applicable threshold before submission.                                  |
| Items                        | The products, services, assets, or expenses being billed. Each row can carry its own account, Warehouse, Cost Center, Project, and tax template. |
| Taxes and Charges            | Tax, freight, duty, and other additions or deductions. The charge type determines how each row is calculated.                                    |
| Payment Schedule             | Splits the amount across one or more due dates based on payment terms.                                                                           |
| Accounting Dimensions        | Attributes such as Cost Center, Project, Branch, or custom dimensions used for reporting and controls.                                           |
| On Hold                      | Prevents the invoice from being selected for payment until the hold is released.                                                                 |


## Taxes, currency, and additional charges

Select the correct buying price list and transaction currency before adding Items. ERPNext stores the exchange rate used to convert the invoice into Company currency. Review it when the invoice is in a foreign currency.

Apply the correct tax template or add tax rows manually. Charges can be based on Net Total, a previous row, Actual amount, or other supported calculation types. Check whether freight or duty should affect Item valuation. Use a [Landed Cost Voucher](/erpnext/landed-cost-voucher) when additional costs must be allocated after receipt.

For country-specific taxes, use the regional documentation and fields supplied by the installed localization. Do not copy tax examples from another jurisdiction without confirming the legal and accounting treatment.

## Submit and next steps

Submitting a Purchase Invoice normally:

- credits the Supplier payable account;
- debits expense, asset, stock, or Stock Received But Not Billed accounts based on the workflow;
- posts tax and additional-charge ledgers;
- updates billed quantities on linked Purchase Orders or Purchase Receipts;
- creates Payment Ledger entries used by Accounts Payable and reconciliation.

After submission, use **Create &gt; Payment** to make a [Payment Entry](/erpnext/payment-entry). You can also include the invoice in a [Payment Order](/erpnext/payment-order), reconcile an existing payment, place it on hold, or create a return.

To reduce or reverse the bill, open the submitted invoice and select **Create &gt; Return / Debit Note**.

[Screenshot on the live page: Create Return or Debit Note from a submitted Purchase Invoice]

Use **View &gt; Accounting Ledger** to inspect the General Ledger effect. If stock was updated, review the Stock Ledger as well.

## Status


| Status            | Meaning                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Draft             | Saved but not posted to the ledgers.                                                           |
| Unpaid            | Submitted with an outstanding payable amount.                                                  |
| Partly Paid       | Payments or credits cover only part of the invoice.                                            |
| Paid              | The outstanding amount is zero.                                                                |
| Overdue           | The invoice remains outstanding after its due date.                                            |
| Return            | The document is a submitted Debit Note.                                                        |
| Debit Note Issued | A Debit Note has been created against the invoice.                                             |
| Canceled          | The submitted document was canceled and its ledger effect reversed according to ERPNext rules. |


## Troubleshooting

### The invoice duplicates stock value

Check whether a Purchase Receipt already exists. Do not enable **Update Stock** on the Purchase Invoice when the receipt already posted the same stock movement.

### A Purchase Order or Purchase Receipt is missing from Get Items From

Confirm that it is submitted, belongs to the same Supplier and Company, has a billable balance, and is not closed. Also verify user permissions.

### The expense account is unexpected

ERPNext can fetch it from the Item, Item Group, Company defaults, or linked receipt accounting. Open the Item row and verify the account and accounting dimensions before submission.

### Payment cannot be created

Confirm that the invoice is submitted, not on hold, has an outstanding amount, and uses a payable account valid for the Supplier and Company.

### Supplier invoice number is rejected as a duplicate

Search existing Purchase Invoices for the same Supplier and bill number. Do not change the reference only to bypass the warning. Confirm whether the bill was already entered.

## Frequently asked questions

### Can I invoice only part of a Purchase Order?

You can. Create the Purchase Invoice from the order and retain only the quantity billed now. Later invoices can bill the remaining quantity.

### Should services use Update Stock?

They should not. Service Items do not require a stock receipt. Post them to the appropriate expense or asset account.

### Can one Purchase Invoice cover several Purchase Receipts?

You can. Use **Get Items From &gt; Purchase Receipt** and select eligible receipts for the same Supplier.

### Can I edit a submitted Purchase Invoice?

Submitted accounting fields are protected. Use Cancel and Amend when permitted, or issue a Debit Note when you need a traceable reduction or return.

## Related topics

- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Debit Note](/erpnext/debit-note)
- [Payment Entry](/erpnext/payment-entry)
- [Accounts Payable](/erpnext/accounts-payable)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)

<!-- page: erpnext/erpnext__purchase-order.md -->
---
title: "Purchase Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-order"
updated: "2026-02-28"
---

**A Purchase Order is a binding contract with your Supplier that you promise to buy a set of items under given conditions.**

It is similar to a Sales Order but instead of sending it to an external party, you keep it for internal records.

> Home > Buying > Purchasing > Purchase Order

[Screenshot on the live page: Buying Flow]

1. Prerequisites

---

Before creating and using a Purchase Order, it is advised that you create the following first:

- [Supplier](/erpnext/supplier)
- [Item](/erpnext/item)

1. How to create a Purchase Order

---

A Purchase Order can be automatically created from a Material Request or Supplier Quotation.

1. Go to the Purchase Order list, click on New.
2. Select the Supplier, required by date.
3. In the items table, select the item by code, you can change the required by date for each item.
4. Set the quantity and the price will be fetched automatically if set in the Item master.
5. Set taxes.
6. Save and Submit. 

[Screenshot on the live page]

### 2.1 Setting Warehouses

- **Set Target Warehouse**: Optionally, you can set the default target Warehouse where the purchased Items will be delivered. This will be fetched into the Item table rows.

### 2.2 Fetching Items from Open Material Requests

Items can be fetched into the Purchase Order automatically from open [Material Requests](/erpnext/material-request). For this to work, the following steps need to be done:

1. Select a Supplier in the Purchase Order.
2. Set default Supplier in the Item form under [Item Defaults](/erpnext/item#39-item-defaults).
3. A [Material Request](/erpnext/material-request) needs to be present of type 'Purchase'.
4. Click on the **Get Items from open Material Requests** button below the Supplier name. Now a dialog will appear with Material Requests containing Items for which the default Supplier is the same as the one selected in the Purchase Order. On selecting the Material Requests and clicking on **Get Items**, the Items will be fetched from the Material Requests. 

> **Note:** The **Get Items from Open Material Requests** button is visible as long as the Items table is empty.



[Screenshot on the live page]



1. Features

---

### 3.1 Address and Contact

- **Select Supplier Address**: The Supplier's billing address.
- **Select Shipping Address**: The Supplier's shipping address from which they'll be sending the items.
- Address, Shipping Address, Contact, Contact Email will be fetched if saved in the Supplier master.

For India:

- **Supplier and Company GSTIN**: The GST Identification Number of your Supplier and your company.
- **Place of Supply**: For GST, Place of Supply is necessary. It consists of the state's name and number.

### 3.2 Currency and Price List

You can set the currency in which the purchase order is to be stored. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Read about [Price Lists](/erpnext/price-lists) and [Multi-Currency Transactions](/erpnext/accounts/articles/managing-transactions-in-multiple-currencies) to know more.

### 3.3 Subcontracting or 'Supply Raw Materials'

Setting 'Supply Raw Materials' option is useful for subcontracting where you provide the raw materials for manufacturing an item. To know more, visit the [Subcontracting page](/erpnext/subcontracting).

### 3.4 The Items table

- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for [tracking items using barcode](/erpnext/track-items-using-barcode) to know more.
- **Quantity and Rate**: When you select the Item code, its name, description, and UOM will be fetched. The 'UOM Conversion Factor' is set to 1 by default, you can change it depending on the UOM received from the seller, more in the next section.

'Price List Rate' will be fetched if a Standard Buying rate is set. 'Last Purchase Rate' shows the rate of the item from your last Purchase Order. Rate is fetched if set in the item master. You can attach an Item Tax Template to apply a specific tax rate to the item.

- **Item weights** will be fetched if set in the Item master else enter manually.
- **Warehouse**: The warehouse where the items will be delivered, will be auto filled if 'Set Target Warehouse' was set in the Purchase Order. Via Blanket Order, a Blanket Order can be linked, to know more [click here](/erpnext/blanket-order). A 'Project' can be linked to track progress. A 'BOM' or Bill of Materials can also be linked to track progress.
- 'Qty as per Stock UOM' will show the current stock as per the UOM set in the Item master. 'Received Qty' will be updated when the items are billed.
- **Accounting Details**: This section is auto filled for a Purchase Order. 'Expense Account' is the account against which the PO is billed, and Cost Center is the CC against which the PO is charged.

A “Required By” date on each Item: If you are expecting part delivery, your Supplier will know how much quantity to deliver at which date. This will help you from preventing over-supply. It will also help you to track how well your Supplier is doing on timeliness.

**Allow Zero Valuation Rate**: Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

### 3.5 Purchase UOM and Stock UOM Conversion

You can change your UOM as per your stock requirements in the Purchase Order.

For example, if you have bought your raw material in large quantities with UOM - boxes and wish to stock them in UOM - Nos; you can do so while making your Purchase Order.

1. Store UOM as Nos in the Item master. Note that the UOM in the Item master is the stock UOM.
2. In the Purchase Order mention UOM as Box. (Since material arrives in Boxes)
3. In the Warehouse and Reference section, the UOM will be pulled in as Nos (from the Item form):

[Screenshot on the live page: Purchase Order - UOM]

1. Mention the UOM conversion factor. For example, (1); If one box has 1 kilo.
2. Notice that the stock quantity will be updated accordingly.

[Screenshot on the live page: Purchase Order - UOM]

### 3.6 Taxes and Charges

If your Supplier is going to charge you additional taxes or charge like a shipping or insurance charge, you can add it here. It will help you to accurately track your costs. Also, if some of these charges add to the value of the product you will have to mention them in the Taxes table.

Visit the [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit [this page](/erpnext/tax-category).

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/erpnext/shipping-rule) page.

[Screenshot on the live page: Purchase Order Taxes]

For example, you buy Items worth X and sell them for 1.3X. So, your Customer pays 1.3 times the tax you pay your Supplier. Since you have already paid tax to your Supplier for X, what you owe your government is only the tax on 0.3X.

This is very easy to track in ERPNext since each tax head is also an Account. Ideally you must create two Accounts for each type of VAT you pay and collect, “Purchase VAT-X” (asset) and “Sales VAT-X” (liability), or something to that effect.

### 3.7 Additional Discount

Other than recording discount per item, you can add a discount to the whole purchase order in this section. This discount could be based on the Grand Total i.e., post-tax/charges or Net total i.e., pre-tax/charges. The additional discount can be applied as a percentage or an amount.

Read [Applying Discount](/erpnext/applying-discount) for more details.

### 3.8 Payment Terms

Sometimes payment is not done all at once. Depending on the agreement, half of the payment may be made before shipment and the other half after receiving the goods/services. You can add a Payment Terms template or add the terms manually in this section.

Read [Payment Terms](/erpnext/payment-terms) to know more.

### 3.9 Terms and Conditions

In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/erpnext/terms-and-conditions)

### 3.10 Print Settings

#### Letterhead

You can print your request for quotation / purchase order on your company's letterhead. Know more [here](/erpnext/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

#### Print Headings

Titles of your documents can be changed. Know more [here](/erpnext/print-headings).

The seller's Additional Discount, Payment Terms, Terms and Conditions can be recorded in your Purchase Order.

### 3.11 More Information

This section shows the status of the Purchase Order, percentage of items received, and percentage of items billed. If this is an Inter-Company Order, the Sales Order can be linked here.

### 3.12 After Submitting

Once you “Submit” your Purchase Order, you can trigger actions these actions:

- You can Add, Update, Delete items in the Purchase Order by clicking on the **Update Items** button. However, you cannot delete items which has already been received.
- Status: Once submitted, you can hold a Purchase Order or Close it.
- Create: From a submitted Purchase Order, you can create the following:
  - [Purchase Receipt](/erpnext/purchase-receipt) - A receipt indicating you've received the items.
  - [Purchase Invoice](/erpnext/purchase-invoice) - An invoice/bill for the purchase order.
  - [Payment Entry](/erpnext/payment-entry) - A payment entry indicates that payment has been made against a purchase order.
  - [Journal Entry](/erpnext/journal-entry) - A Journal Entry is recorded in the general ledger.

[Screenshot on the live page]

### 4. Related Topics

1. [Request For Quotation](/erpnext/request-for-quotation)
2. [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
3. [Purchasing In Different Unit](/erpnext/purchasing-in-different-unit)
4. [Amending Purchase Order After Submit](/erpnext/amending-purchase-order-after-submit)

<!-- page: erpnext/erpnext__purchase-receipt.md -->
---
title: "Purchase Receipt\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-receipt"
updated: "2026-06-18"
---

**Purchase Receipts are made when you accept Items from your Supplier usually against a Purchase Order.**

You can also accept Purchase Receipts directly without the need for a Purchase Order. To do this, set Purchase Order  
Required as “No” in Buying Settings.

To access the Purchase Receipt list, go to:

> Home > Stock > Stock Transactions > Purchase Receipt

[Screenshot on the live page: Purchase Receipt flow]

## 1. Prerequisites

Before creating and using a Purchase Receipt, it is advised that you create the following first:

- Purchase Order

> Note: From version-13 onwards we have introduced immutable ledger which changes the rules for cancellation of stock entries and posting backdated stock transactions in ERPNext. Learn more here.

## 2. How to create a Purchase Receipt

A Purchase Receipt is usually created from a Purchase Order. In the Purchase Order, click on Create > Purchase Receipt.

To create a Purchase Receipt manually (not recommended), follow these steps:

1. Go to the Purchase Receipt list, click on New.
2. The Supplier name and the Items can be fetched from the Purchase Order by clicking on 'Get Items from > Purchase Order'.
3. You can set the Accepted Warehouse for all items in this Purchase Receipt. This is fetched if set in Purchase Order.
4. In case any Items are defective, set the Rejected Warehouse where those Items will be stored.
5. Select the Item and enter the quantity in the Items table.
6. The rate will be fetched and the amount will be calculated automatically.
7. You can expand the item row to change the Accepted Warehouse for an Item.
8. Save and submit.
  Purchase Receipt

You can also add a 'Supplier Delivery Note' to the Purchase Receipt if your Supplier has added some notes.  
Using the 'Edit Posting Date and Time' checkbox you can edit the posting time and date of the Purchase Receipt. By default, the date and time are set when you click on the New button.

Is Return: Tick this checkbox if you're returning Items that were not accepted to your Warehouse.

### 2.1 Statuses

These are the statuses a Purchase Receipt can be in:

- **Draft**: A draft is saved but yet to be submitted to the system.
- **To Bill**: Yet to be billed using a Purchase Invoice.
- **Completed**: Submitted and received all the Items.
- **Return Issued**: All the Items have been returned.
- **Cancelled**: Cancelled the Purchase Receipt.
- **Closed**: The purpose of the Close is to manage short-closing. For example, you ordered 20 qty, but closing at 15 qty. The remaining 5 is not to be received or billed.

## 3. Features

### 3.1 Currency and Price List

The currency of the Purchase Receipt is shown in this section, it is fetched from the Purchase Order. The item prices will be fetched from the set Price list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Since the incoming Item affects the value of your inventory, it is important to convert it into your base currency if you have ordered in another Currency. You will need to update the Currency Conversion Rate if applicable.

Read about Price Lists  
and Multi-Currency Transactions  
to know more.

### 3.2 Warehouse details

The following Warehouses set will apply to all Items in the Items table of the Purchase Receipt. You can change the Warehouses for individual Items via the table.

- **Accepted Warehouse**: This is the Warehouse in which you'll accept and store the incoming Items. Usually, this is the 'Stores' Warehouse.
- **Rejected Warehouse:** This is the Warehouse in which you'll keep the rejected Items which were either defective or not up to the quality mark.

#### Subcontracting

- **Raw Materials Consumed**: In case you're subcontracting, select 'Yes' to consume the Raw Materials from the vendor. Read Subcontracting to know more.

### 3.3 Items table

- **Barcode**: You can track Items using barcodes.
- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for tracking items using barcode to know more.
- The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.
- **Received and Accepted**: Set the received, accepted and rejected quantity. The UoM is fetched from the Item master. You will need to update the “UOM Conversion Factor” if your Purchase Order for an Item is in a different Unit of Measure (UOM) than what you stock (Stock UOM).



[Screenshot on the live page: Purchase Receipt Items table]

- **Rate**: The Rate is fetched if set in the Price List and the total Amount is calculated.
- **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit this page.
- The Item Weight details per unit and Weight UOM are fetched if set in the Item master.
- **Warehouse and Reference**: You can set the accepted and rejected Warehouses and also add a Quality Inspection, see next section.
- **Serial No, Batch No, and BOM**: If your Item is serialized or batched, you will have to enter Serial Number  
and Batch in the Items table. You are allowed to enter multiple Serial Numbers  
in one row (each on a separate line) and you must enter the same number of  
Serial Numbers as the quantity.

 There are separate fields for entering Serial Numbers of both accepted and rejected Items here. A Batch Number can also be set if you're storing a batch of plastic medicines for example.

 Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

- You can link a BOM here if the Item is being subcontracted. Linking the BOM here will affect the Stock ledger, i.e. the raw material stock will be deducted from the Supplier Warehouse.

 **Note**: The Item has to be serialized or batched for these features to work. If the Item is serialized a popup will appear where you can enter the Serial Numbers.

- Accounting Dimensions help to tag each transaction with different Dimensions without the need for creating new Cost Centers. You need to create Accounting Dimensions first, to know more, visit this page.
- Page Break will create a page break just before this item when printing.

### 3.4 Tracking Quality Inspection

If for certain Items, it is mandatory to record Quality Inspections (if you have set it in your Item master), you will need to update the “Quality Inspection" field. The system will only allow you to “Submit” the  
Purchase Receipt if you update the “Quality Inspection”.

After enabling Inspection Criteria in the Item form for Purchase and attaching a Quality Inspection Template there, Quality Inspections can be recorded in Purchase Receipts.

To know more, visit the Quality Inspection page.

[Screenshot on the live page: Quality Inspection]

### 3.5 Raw Materials Consumed

- The **Consumed Items** table contains the Raw Materials consumed by the Supplier in order to receive the Finished Item.
- The **Get Current Stock** button will fetch the current stock of the Consumed Items from the Supplier Warehouse.  
 [Screenshot on the live page: Purchase Receipt]

### 3.6 Taxes and Valuation

The Taxes and Charges will be fetched from the Purchase Order.

Visit the Purchase Taxes and Charges Template page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit this page.

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the Shipping Rule page.

### 3.6.1 Allocate full Actual Charge to Stock Items Only

#### Problem

For an "Actual" tax/charge under **Consider Tax or Charge for = Valuation / Valuation and Total**, the amount is distributed across **all** items by net amount. Only stock/asset items can carry valuation, so a non-stock (service) item's share is silently dropped from the stock valuation.

That is correct for a genuine tax, but wrong for a charge like **Freight** that should be fully capitalized into the stock items — there was no way to express "put the entire amount into stock valuation".



##### Example — Purchase Receipt


| Item   | Type    | Net Amount |
| ------ | ------- | ---------- |
| Item A | Stock   | 100        |
| Item B | Stock   | 100        |
| Item C | Service | 100        |


Actual valuation charge = **30**

**Before (only behaviour available)** — 30 / 300 = 10 per item; Item C's 10 is dropped:


| Item | Valuation |
| ---- | --------- |
| A    | 110       |
| B    | 110       |
| C    | 0         |


Only 20 is capitalized; 10 is lost from inventory cost.

## Solution

Add an **"Allocate Full Amount to Stock Items"** checkbox on *Purchase Taxes and Charges* rows of type **Actual** (shown only for category Valuation / Valuation and Total).

**Checked (default)** — the amount is distributed over **stock & asset items only**, so the whole charge is capitalized. The freight case now works:


| Item | Valuation |
| ---- | --------- |
| A    | 115       |
| B    | 115       |
| C    | 0         |


30 / 200 = 15 per stock item; the entire 30 is capitalized.

**Unchecked** — previous behaviour is preserved (spread across all items; the non-stock share is not capitalized → 110 / 110 / 0).

Both modes can coexist on one document (e.g. a real tax + a freight charge); each item's share is summed across the charges.

### 3.7 Additional Discount

Any additional discounts to the whole order can be set in this section.  
Read Applying Discount for more details.

### 3.8 More Information

The Status of the Purchase Receipt is shown here and at the top. The various statuses are: Draft, To Bill, Completed, Canceled, and Closed. This section also shows % Amount Billed, i.e. the percentage of amount for which Sales Invoices are created.

### 3.9 Printing Settings

#### Letterhead

You can print your Purchase Receipt on your company's letterhead. Know more here.

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more here.

### 3.10 After Submitting

A Stock Ledger Entry is created for each Item adding the Item in the Warehouse  
by the “Accepted Quantity” If you have rejections, a Stock Ledger Entry is  
made for each Rejection. The “Pending Quantity” is updated in the Purchase  
Order.

After submitting the Purchase Receipt, the following can be created:

- Purchase Return
- Stock Entry
- Purchase Invoice
- Retaining Sample Stock

[Screenshot on the live page: Purchase Receipt submit]

### 3.11 Returning a Purchase Order

Once you've received a Purchase Order using a Purchase Receipt, you can create a return entry in case the Item needs to be returned to the Supplier. To know more, visit the Purchase Return page.

### 3.12 Skipping Purchase Receipt

If you don't want to create a Purchase Receipt after a Purchase Order and directly want to create a Purchase Invoice, enable the feature for it in Buying Settings.

---

#### Changing the value of Items post Purchase Receipt:

Sometimes, certain expenses that add to the total of your purchased Items are known  
only after a while. Common example is, if you are importing the Items, you  
will come to know of Customs Duty, etc only when your “Clearing Agent” sends  
you a bill. If you want to attribute this cost to your purchased Items, you  
will have to use the Landed Cost Voucher. Why “Landed Cost”? Because it represents the charges that you paid when it landed in your possession.

## 4. Related Topics

1. Delivery Note
2. Purchase Order
3. Purchase Invoice
4. Supplier
5. Landed Cost Voucher

<!-- page: erpnext/erpnext__purchase-return.md -->
---
title: "Purchase Return\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-return"
updated: "2026-03-02"
---


**A purchased Item being returned is known as a Purchase Return.**

With the Purchase Return feature, you can return products to the
Supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc.

## 1. Prerequisites
Before creating and using a Purchase Return, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Purchase Invoice](/erpnext/purchase-invoice)

 Or

 [Purchase Receipt](/erpnext/purchase-receipt)


## 2. How to create a Purchase Return
1. First open the original Purchase Receipt, against which supplier delivered the Items.

 [Screenshot on the live page: Original Purchase Receipt]

1. Click on 'Create > Return', it will open a new Purchase Receipt with 'Is Return' checked. Items, Rate, and taxes will negative numbers.

 [Screenshot on the live page: Return Against Purchase Receipt]

1. On submission of Return Purchase Return, the system will decrease item quantity from the mentioned Warehouse. To maintain correct stock valuation, stock balance will also go up according to the original purchase rate of the returned items.

 [Screenshot on the live page: Return Stock Ledger]

1. In the Accounting Ledger, the Stock In Hand account will be credited and the Stock Received but Not Billed account will be debited.

 [Screenshot on the live page: Return Stock Ledger]

If Perpetual Inventory enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.

## 3. Impact on Stock Return via Purchase Receipt
On Creating a Purchase Return against a Purchase Receipt:

* The **Returned Quantity** in the original Purchase Receipt along with any Purchase Order linked to it, is updated.

* The original Purchase Receipt's status is changed to **Return Issued** if 100% returned:
 [Screenshot on the live page: Return Issued]

### 4. Related Topics
1. [Sales Return](/erpnext/sales-return)
1. [Perpetual Inventory](/erpnext/perpetual-inventory)
