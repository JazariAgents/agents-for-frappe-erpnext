<!-- Frappe documentation: erpnext, part 21 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__difference-in-total-and-valuation-in-tax-and-charges.md -->
---
title: "Include Tax or Charge in Valuation or Total?"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-in-total-and-valuation-in-tax-and-charges"
updated: "2026-08-03"
---

On a purchase transaction, a tax or charge can affect what you owe the supplier, the value assigned to received stock, or both. ERPNext separates these effects through **Consider Tax or Charge for** on each row of the [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template).

This choice matters because supplier payable and inventory valuation answer different questions:


| Question                                           | ERPNext value |
| -------------------------------------------------- | ------------- |
| How much must the company pay this supplier?       | Total         |
| How much did it cost to bring the item into stock? | Valuation     |


The available choices are **Total**, **Valuation**, and **Valuation and Total**.

## Before you begin

Confirm who is charging the amount and whether the cost should form part of inventory value. Ask your accountant how the cost must be treated under your accounting policy. Also confirm that the relevant tax, freight, or expense account exists in the [Chart of Accounts](/erpnext/chart-of-accounts).

Use **Total** or **Valuation and Total** only when the amount belongs in the payable created by this purchase document. Use **Valuation** when the amount should be allocated to stock but is not payable to this supplier on this document.

The examples below use:


| Component             | Amount  |
| --------------------- | -------: |
| Item net value        | $800.00 |
| Recoverable tax at 4% | $32.00  |
| Freight               | $100.00 |


The $32 tax is added to Total in every example. The difference is how the $100 freight row is treated.

## Choose the correct treatment


| Setting             | Supplier total    | Stock valuation   | Typical use                                                                |
| ------------------- | ----------------- | ----------------- | -------------------------------------------------------------------------- |
| Total               | Increases         | Does not increase | A charge payable to the supplier that should not be capitalized into stock |
| Valuation           | Does not increase | Increases         | Freight paid separately but allocated through this receipt or invoice      |
| Valuation and Total | Increases         | Increases         | The supplier charges freight and it forms part of landed inventory cost    |


The **Type** determines how ERPNext calculates the row amount. **Consider Tax or Charge for** determines where that amount has an effect. These are separate decisions. See [Types in Tax Template](/erpnext/types-in-tax-template) for the calculation options.

## Add a Total-only charge

Select **Total** when the charge should increase the amount payable on the [Purchase Invoice](/erpnext/purchase-invoice) but should not be allocated into item valuation.

For the example:

`$800 item value + $32 tax + $100 freight = $932 payable`

The freight does not increase the item's valuation through this row. This treatment can be appropriate for a fee that is expensed directly instead of capitalized.

1. Add or open a row in **Purchase Taxes and Charges**.
2. Select the required Account Head.
3. Set the calculation Type, such as **Actual** for a fixed $100 charge.
4. Set **Consider Tax or Charge for** to **Total**.
5. Review the row Amount and the document Grand Total.

Do not use Total merely because money was paid. The accounting treatment depends on whether the cost belongs in inventory value.

## Add a Valuation-only charge

Select **Valuation** when the cost should increase inventory value but should not increase the payable on this document. A common example is freight paid to a separate carrier while the purchase invoice being processed belongs to the item supplier.



[Screenshot on the live page: Purchase tax rows with freight considered for valuation]

Open the freight row using its pencil icon. Set the row to **Valuation**, then enter the amount and the correct expense or clearing account.



[Screenshot on the live page: Freight row configured for valuation only]

In this example, the supplier payable remains:

`$800 item value + $32 tax = $832 payable`

The $100 freight is allocated into valuation but is excluded from the supplier total.



[Screenshot on the live page: Valuation-only freight excluded from the purchase invoice total]

Use a suitable clearing or expense account for the valuation row. The source of the separately paid freight must still be recorded correctly, such as through another supplier invoice or a [Landed Cost Voucher](/erpnext/landed-cost-voucher), depending on the workflow.

## Add a charge to Valuation and Total

Select **Valuation and Total** when the same amount must increase both the supplier payable and the item's valuation. This is common when the item supplier arranges freight, includes it on the invoice, and the freight forms part of landed cost.



[Screenshot on the live page: Purchase tax rows with freight included in valuation and total]

Open the freight row and select **Valuation and Total**. Confirm the Account Head, Type, description, and amount before closing the row editor.



[Screenshot on the live page: Freight row configured for valuation and total]

The supplier payable becomes:

`$800 item value + $32 tax + $100 freight = $932 payable`

The $100 freight is also allocated into inventory valuation.



[Screenshot on the live page: Freight included in both purchase invoice total and valuation]

## Understand the accounting and stock effect

A submitted purchase transaction may affect both the [General Ledger](/erpnext/general-ledger) and the [Stock Ledger](/erpnext/stock-ledger). The exact posting depends on whether stock is updated through a [Purchase Receipt](/erpnext/purchase-receipt), through **Update Stock** on a Purchase Invoice, or through another perpetual-inventory workflow.


| Treatment           | Payable effect                        | Inventory-value effect      |
| ------------------- | ------------------------------------- | --------------------------- |
| Total               | Included in the document's payable    | Not allocated by this row   |
| Valuation           | Excluded from this document's payable | Allocated to received items |
| Valuation and Total | Included in the document's payable    | Allocated to received items |


The valuation amount is distributed across eligible items according to ERPNext's valuation logic. Review the item valuation and ledger entries after submitting a controlled test. Do not infer the final accounting entry only from Grand Total.

## When to use a Landed Cost Voucher instead

Use a Landed Cost Voucher when additional costs become known after the receipt, come from another supplier, or must be allocated across one or more submitted receipts or invoices. It is designed to update the landed value of received stock.

Use the purchase tax table when the charge is known while creating the transaction and belongs naturally on that document. Avoid recording the same freight through both methods, because that can capitalize the cost twice.

## Verify the result before wider use

Create a draft with one item and easy numbers. Then:

1. Confirm the item Net Total.
2. Review each tax row's Amount and Total.
3. Compare the Grand Total with the expected supplier payable.
4. Submit the controlled transaction.
5. Open **Accounting Ledger** and confirm the payable and tax postings.
6. Open the stock ledger or valuation report and confirm the inventory effect.

If a template is reused automatically, test it before setting it as the company default or applying it through a [Tax Rule](/erpnext/tax-rule).

## Troubleshooting

### Freight increased the supplier payable unexpectedly

Open the freight row and check **Consider Tax or Charge for**. Use Valuation instead of Valuation and Total only when the amount must not be payable on this document and the accounting source is handled elsewhere.

### Freight did not increase item valuation

The row may be set to Total. Confirm that it is Valuation or Valuation and Total, that the transaction updates or receives stock, and that the selected account and item are eligible for the intended treatment.

### The payable is correct but the freight cost has no accounting source

A Valuation-only row does not make the amount payable to this supplier. Record the actual carrier or other cost source through the appropriate document, or use a Landed Cost Voucher when that better matches the workflow.

### Inventory appears to include the charge twice

Check whether the same cost was included in a valuation tax row and again in a Landed Cost Voucher. Keep only the posting that reflects the real source and timing of the charge.

## Frequently asked questions

### Should recoverable tax be included in valuation?

Usually a recoverable input tax is not part of inventory cost, but treatment depends on local rules and your accounting policy. Confirm the setup with your accountant.

### Can a fixed freight charge use Valuation and Total?

Y

es. Set Type to Actual, enter the freight amount, and use Valuation and Total when the supplier charges it and it must also form part of inventory value.

### Does Valuation-only mean the freight is free?

1. It means the amount is not payable on this particular purchase document. The actual payment or supplier liability must be recorded through its proper source.

### Is Consider Tax or Charge for available on sales transactions?

The valuation choice is relevant to purchase-side stock cost. Sales tax rows primarily affect the transaction total rather than incoming inventory valuation.

### Can I change the setting after submission?

Submitted accounting and stock transactions should not be edited casually. Cancel and amend where permitted, or use the appropriate correction process after reviewing the ledger impact.

## Related topics

- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)
- [Types in Tax Template](/erpnext/types-in-tax-template)
- [Perpetual Inventory](/erpnext/perpetual-inventory)

<!-- page: erpnext/erpnext__difference_between_lead_contact_and_customer.md -->
---
title: "Difference between Lead, Contact, and Customer | ERPNext Documentation"
description: "Understand when to use a Lead, Contact, or Customer in ERPNext and how these records relate."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference_between_lead_contact_and_customer"
updated: "2026-07-23"
---

A Lead, Contact, and Customer represent different parts of a relationship in ERPNext. Use the record that matches the party's current role instead of treating the three DocTypes as interchangeable.

## Lead

A [Lead](/erpnext/lead) is an unqualified person or organization that may become a customer. Use a Lead while your sales team is still confirming the requirement, interest, timing, or fit.

A Lead can be converted into an Opportunity and, when appropriate, a Customer.

## Contact

A [Contact](/erpnext/contact) is a person with communication details such as email addresses and phone numbers. A Contact can be linked to a Customer, Supplier, Lead, or another party.

Creating a Contact does not create a customer account or accounting relationship. Use Contacts to store the people your team communicates with at an organization.

## Customer

A [Customer](/erpnext/customer) is the commercial party used in selling and accounting transactions. Quotations, Sales Orders, Delivery Notes, Sales Invoices, pricing, credit controls, Addresses, and Contacts can be linked to the Customer.

Create a Customer when the party is sufficiently qualified and your process needs a reusable customer account.

## Comparison


| Record   | Represents                               | Use it when                                                                    |
| -------- | ---------------------------------------- | ------------------------------------------------------------------------------ |
| Lead     | An unqualified prospect                  | Interest has been captured but the party still needs qualification             |
| Contact  | A person and their communication details | You need to record the individual you communicate with                         |
| Customer | The party you sell to                    | You need sales transactions, pricing, delivery, billing, or accounting history |


## Common workflow

1. Capture an enquiry as a Lead.
2. Qualify the requirement and create an [Opportunity](/erpnext/opportunity).
3. Create or select the Customer when a customer account is required.
4. Link the relevant Contacts and [Addresses](/erpnext/address) to the Customer.
5. Continue with a [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order).

You can also create an Opportunity directly for an existing Customer. A Contact may be linked to multiple organizations when the same person legitimately represents more than one party.

## Related topics

- [Automate Lead Creation](/erpnext/automate_lead_capturing)
- [Customer Group](/erpnext/customer-group)
- [CRM Settings](/erpnext/crm-settings)

<!-- page: erpnext/erpnext__disable-rounded-total.md -->
---
title: "Disable Rounded Total\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disable-rounded-total"
updated: "2026-03-04"
---


All the sales transactions like Sales Order, Sales Invoice have Rounded Total in it. It is calculated based on the value of Grand Total. Moreover, Rounded Total is also visible in the Standard Print Formats.

> Note: The Rounded Total is a feature present in **Sales** transactions.

[Screenshot on the live page: Print Preview]

However, if you wish to disable the same, you may follow the steps given below to hide the rounded total from Standard Print Formats, for all the sales transactions.

#### Step 1: Go to Global Defaults

From the Awesome Bar search for Global Defaults

#### Step 2: Disable Rounded Total

Check Disable Rounded Total, and click on save.

[Screenshot on the live page: Print Preview]

To verify the changes, you should clear the cache and/or refresh your ERPNext account. Then your print formats shall not render value for the Rounded Total.

> Note: This setting will only affect Standard print formats.

<!-- page: erpnext/erpnext__disable-signup.md -->
---
title: "Disable Signup on ERPNext Website\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disable-signup"
updated: "2026-02-28"
---


ERPNext has portal feature available which allows third parties like Customers and Suppliers sign, place new orders and track updates on the previous orders.

[Screenshot on the live page: Website signup]

To allow new Customer and Supplier to Signup, the login page of your ERPNext account has Signup link avaiable. However, if you wish to disbale this feature, you can achieve it by following the steps given below.

### Steps

1. Go To

> Website > Setup > Website Settings `

2. In the Website Settings page, scroll down upto `More Information` section.

3. Check fied `Disable Signup`.

[Screenshot on the live page: Disable signup]

4. Save Website Settings.

<!-- page: erpnext/erpnext__disassembly-order.md -->
---
title: "Disassembly Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/disassembly-order"
updated: "2026-02-26"
---

The 'Disassembly Order' in ERPNext is used to dismantle finished goods and return the components that are in good condition back to the store. The system allows users to change the valuation rate of the components when adding them back to the store.

To create the "Disassembly Order", open the work order which are in **Completed** state or **Closed** state. Click on create button and after that "Disassembly Order"

[Screenshot on the live page: work-order-disassembly-order]  


Once user clicked on the "Disassembly Order" button, the system will open the stock entry with type as "Disassemble"

  


[Screenshot on the live page: stock-entry-disassembly-order]  


* Users can manually removed items which are not in a good condition
* The system, by default, fetches the basic rate based on past transactions. If users want, they can edit the basic rate for the raw materials.

<!-- page: erpnext/erpnext__discount_accounting.md -->
---
title: "Discount Accounting | ERPNext Documentation"
description: "Configure ERPNext discount accounting to post sales discounts separately, then verify item, invoice total, and General Ledger values with a clear example."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/discount_accounting"
updated: "2026-08-03"
---

Discount Accounting lets ERPNext show a sales discount separately in the [General Ledger](/erpnext/general-ledger) instead of posting only the reduced revenue. Use it when finance needs to report gross sales and discounts allowed as distinct amounts.



This setting changes accounting presentation. It does not decide who receives a discount or calculate promotional eligibility. Configure the commercial discount using the normal [discount fields](/erpnext/applying-discount), a [Pricing Rule](/erpnext/pricing-rule), or another approved pricing method.



For example, Nova Electronics Trading invoices two phones at a list price of $699 each. It applies a 10% item discount and then a 5% additional discount. With Discount Accounting enabled, ERPNext posts:


| Account                 | Debit     | Credit    | Meaning                                                      |
| ----------------------- | ---------: | ---------: | ------------------------------------------------------------ |
| Debtors                 | $1,195.29 | $0.00     | Amount owed by the Customer.                                 |
| Sales                   | $0.00     | $1,398.00 | Revenue before the discounts.                                |
| Sales Discounts Allowed | $202.71   | $0.00     | Item discount of $139.80 plus additional discount of $62.91. |


Without separate discount accounting, the same commercial discount normally reduces the net revenue represented by the invoice lines instead of appearing as a separate discount-account debit.

## Before you begin

Confirm the following:

1. The discount account exists in the [Chart of Accounts](/erpnext/chart-of-accounts) for each Company that will use it. Confirm with your accountant whether it should be an expense account or a contra-revenue account in your reporting structure.
2. The [Item](/erpnext/item) has an applicable [Item Price](/erpnext/item-price) in the intended [Price List](/erpnext/price-lists). Item discounts use Price List Rate as their reference.
3. Users can create and submit a [Sales Invoice](/erpnext/sales-invoice) and view its ledger.
4. You have tested the expected posting with representative taxes, currencies, rounding, and discounts before enabling the workflow for regular transactions.

## Enable Discount Accounting for selling

Two settings control the current workflow.

1. Open [Selling Settings](/erpnext/selling-settings).
2. Select **Advanced Features**.
3. Enable **Enable discount accounting for selling** and save.

[Screenshot on the live page: Selling Settings with Enable discount accounting for selling highlighted]

This setting tells ERPNext to create additional ledger entries for sales discounts in the selected Discount Account.

4. Open [Accounts Settings](/erpnext/accounts-settings).
5. Select **Invoice and Billing**.
6. Enable **Enable Discounts and Margin** and save.

[Screenshot on the live page: Accounts Settings with Enable Discounts and Margin highlighted]

This setting makes the discount and margin controls available for transaction items. It does not, by itself, create a separate discount-account posting.

## Set a default Discount Account for an Item

A default avoids selecting the account on every invoice row.

1. Open the Item.
2. Select **Accounting**.
3. In **Item Defaults**, find the row for the Company.
4. Select the highlighted pencil icon to open the complete row editor.

[Screenshot on the live page: Item Defaults row with the pencil icon highlighted]

5. Set **Discount Account** to the Company account that should receive item-level and invoice-level sales discounts.
6. Save the Item.

[Screenshot on the live page: Item Default with Discount Account highlighted]

The Item Default is Company-specific. Configure a valid account and other defaults for each Company rather than copying an account from a parent or sibling Company.

## Record an item-level discount

1. Create a Sales Invoice and select the Company and Customer.
2. Add the Item to the **Items** table.
3. Select the highlighted pencil icon on the item row.

[Screenshot on the live page: Sales Invoice item row with the pencil icon highlighted]

4. Expand **Discount and Margin**.
5. Enter **Discount (%) on Price List Rate with Margin** or **Discount Amount**.

[Screenshot on the live page: Sales Invoice item discount percentage highlighted]

6. Expand **Accounting Details**.
7. Confirm the **Discount Account**. ERPNext fetches the Item Default when one is configured, but you remain responsible for verifying the account on the transaction.

[Screenshot on the live page: Sales Invoice item Discount Account highlighted]

In the example, the Price List Rate is $699 and the item discount is 10%. For two units, ERPNext records an item discount of $139.80 and an amount of $1,258.20 before the invoice-wide discount.

## Record an additional discount on the invoice

Use an additional discount when the reduction applies to the complete transaction instead of one item row.

1. Expand **Additional Discount** on the Sales Invoice.
2. Set **Apply Additional Discount On** to **Net Total** or **Grand Total**.
3. Enter **Additional Discount Percentage** or **Additional Discount Amount**.
4. Select the **Discount Account**.

[Screenshot on the live page: Sales Invoice Additional Discount fields and Discount Account highlighted]

In the example, 5% of the $1,258.20 Net Total is $62.91. The item and additional discounts therefore total $202.71.

Apply on Net Total and Apply on Grand Total can produce different tax and net-value results. Review the tax breakup, rounding, and final amount with the configuration used by your business.

## Submit and verify the ledger

1. Review the discount amounts, taxes, Grand Total, and Discount Accounts.
2. Save and submit the Sales Invoice.
3. Open **View &gt; Ledger**, or run General Ledger for the invoice voucher.

The submitted example has a Grand Total and outstanding amount of $1,195.29.



[Screenshot on the live page: Submitted Sales Invoice total after discounts]

The ledger shows gross Sales of $1,398.00, a $202.71 debit to Sales Discounts Allowed, and a $1,195.29 debit to Debtors.



[Screenshot on the live page: General Ledger showing the separate Sales Discounts Allowed entry]

Do not treat the invoice as verified merely because its total looks correct. Confirm that the discount account, gross revenue, receivable, tax, currency, Cost Center, and any other [accounting dimensions](/erpnext/accounting-dimensions) appear as intended.

## Important fields and what they mean


| Field                                    | What it controls                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Enable discount accounting for selling   | Creates separate sales-discount ledger entries when the required Discount Accounts are present.                                 |
| Enable Discounts and Margin              | Makes discount and margin controls available on supported transaction item rows.                                                |
| Price List Rate                          | Reference rate before item discount and margin. Overwriting Rate can change the calculated discount relative to this reference. |
| Discount Percentage                      | Percentage reduction calculated against the Price List Rate after applicable margin behavior.                                   |
| Discount Amount                          | Monetary reduction represented on the item row.                                                                                 |
| Item Discount Account                    | Account used for the item-level discount ledger posting.                                                                        |
| Apply Additional Discount On             | Chooses whether the transaction-level discount uses Net Total or Grand Total as its basis.                                      |
| Additional Discount Percentage or Amount | Transaction-wide reduction after item-level pricing has been calculated.                                                        |
| Additional Discount Account              | Account used for the invoice-wide discount ledger posting.                                                                      |


## Purchase discounts

The current ERPNext develop version supports separate Discount Account posting for selling. A [Purchase Invoice](/erpnext/purchase-invoice) still supports item and additional discount values, but its current standard fields do not provide the equivalent Purchase Invoice Item Discount Account or Additional Discount Account used by this sales workflow.

Do not force a sales-only field into a Purchase Invoice through customization without reviewing the accounting logic. If your organization must report purchase discounts separately, define the required treatment with your accountant and validate the supported transaction or [Journal Entry](/erpnext/journal-entry) process in a test Company.

## Troubleshooting


| Issue                                                     | What to check                                                                                                                                                                                              |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Discount and Margin is unavailable                        | Confirm **Enable Discounts and Margin** is enabled, the invoice is in Draft, and Price List Rate is not zero. Open the item row with the pencil icon.                                                      |
| Discount Account is unavailable                           | Confirm **Enable discount accounting for selling** is enabled, reload the invoice after saving the setting, and expand **Accounting Details** in the item row.                                             |
| No separate discount ledger entry is posted               | Verify the selling setting, the item or additional Discount Account, and the submitted invoice ledger. A visible commercial discount does not automatically prove separate accounting is enabled.          |
| The discount amount is unexpectedly negative or too large | Compare Price List Rate, Margin, Rate, Discount Percentage, and Discount Amount. ERPNext treats the difference between the reference Price List Rate and the entered Rate as part of pricing calculations. |
| The wrong Company account is selected                     | Correct the Company-specific Item Default and the invoice row before submission. Accounts cannot be shared across unrelated Companies.                                                                     |


## Frequently asked questions

### Does Discount Accounting change the amount the Customer owes?

No, it changes how the discount is presented in the ledger. The invoice total still reflects the commercial discount entered on the transaction.

### Can I use both an item discount and an additional discount?

Yes, ERPNext applies both. Review the effective discount and the ledger, because both values can post to the selected discount account.

### Why is the calculated discount different after I overwrite Rate?

Item discount is based on Price List Rate and margin behavior. If you replace Rate directly, ERPNext can represent the difference from Price List Rate as a discount or negative discount. Set an intentional Item Price or editable Price List Rate when that better represents the commercial baseline.

### Should the Discount Account be an expense or contra-revenue account?

That depends on your chart and reporting policy. ERPNext posts the value to the account you select. Your accountant should decide its classification and where it appears in financial reports.

### Does the same separate-account workflow work for Purchase Invoices?

Not in the current standard develop fields. Purchase transactions support commercial discount values, but the equivalent purchase-side Discount Account controls documented on older versions are no longer present.

## Related topics

- [Apply Discounts to Sales Transactions](/erpnext/applying-discount)
- [Sales Invoice](/erpnext/sales-invoice)
- [Pricing Rule](/erpnext/pricing-rule)
- [Selling Settings](/erpnext/selling-settings)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__distributed-cost-center.md -->
---
title: "Distributed Cost Center"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/distributed-cost-center"
updated: "2026-08-14"
---

Nova Electronics Trading pays $10,000 each month for software used by two teams. Retail Operations uses most of it, while Online Sales uses the rest. If Nova charges the complete bill to Retail Operations, that team's expenses look too high and Online Sales appears to use the software for free.



Nova can record the bill once against a shared main [Cost Center](/erpnext/cost-center). A [Cost Center Allocation](/erpnext/cost-center-allocation) then distributes 60% to Retail Operations and 40% to Online Sales. The source bill remains one transaction, but management reports show $6,000 against Retail Operations and $4,000 against Online Sales.



A distributed cost center is not a separate ERPNext record. It describes the accounting result of posting to one main Cost Center and letting an allocation rule divide the amount among receiving Cost Centers.

## Before you begin

Create the main Cost Center and every receiving Cost Center in the same [Company](/erpnext/company). Choose a percentage that the business can explain, such as employee count, floor area, revenue, or actual software usage.



The percentages must add up to 100%. Choose the effective date carefully. ERPNext compares the transaction's **Posting Date** with **Valid From** to decide which allocation to use.

## Set up the distribution

Open the Cost Center Allocation list and select **Add Cost Center Allocation**.



[Screenshot on the live page: Cost Center Allocation list in ERPNext]

Select the shared **Main Cost Center**, the **Company**, and the **Valid From** date.



[Screenshot on the live page: Main Cost Center and Valid From fields for a distributed cost center]

In the allocation table, add each receiving cost center and its percentage. Save the record after the total reaches 100%.



[Screenshot on the live page: Receiving cost centers and their allocation percentages]

## What happens in a transaction

When you enter a supported accounting transaction, select only the main Cost Center. This can apply to a [Purchase Invoice](/erpnext/purchase-invoice), [Sales Invoice](/erpnext/sales-invoice), or [Journal Entry](/erpnext/journal-entry). You do not need to calculate and enter every receiving share manually.



When the transaction posts, ERPNext applies the allocation valid on that date. The resulting [General Ledger](/erpnext/general-ledger) entries carry the receiving Cost Centers and their calculated shares. The allocation changes the reporting classification, not the supplier, invoice total, taxes, or payment due.

## Example result


| Posting            | Cost center             | Amount  |
| ------------------ | ----------------------- | ------- |
| Original selection | Shared Services - NET   | $10,000 |
| Distributed share  | Retail Operations - NET | $6,000  |
| Distributed share  | Online Sales - NET      | $4,000  |


Use the [Profit and Loss Statement](/erpnext/profit-and-loss-statement) with a Cost Center filter to compare each team's expense. Open the General Ledger when you need to inspect the individual debit and credit lines behind the report. The [Accounts Payable](/erpnext/accounts-payable) amount remains $10,000 because the supplier is still owed one complete invoice.

## Change the distribution later

Create a new allocation with a later **Valid From** date when the ratio changes. For example, if Online Sales grows, Nova may change the split from 60:40 to 50:50 from the next month. The earlier allocation remains available to explain transactions posted under the old arrangement.



Do not change old submitted transactions merely to apply a new allocation. Review the business effective date with the finance team before changing the rule.

## Troubleshooting

### The amount was not distributed

Confirm that the transaction used the exact main cost center, its posting date falls on or after the allocation's Valid From date, and the allocation belongs to the same company.

### The percentages cannot be saved

Check that every row has a receiving cost center and that the total is exactly 100%.

### The report shows an unexpected split

Check which allocation was valid on the transaction's posting date. Then inspect the voucher and its General Ledger entries to confirm the cost center stored on each line.

## Frequently asked questions

### Does distribution create several invoices?

ERPNext keeps one invoice. It distributes the accounting entries across the receiving Cost Centers.

### Can the receiving cost centers belong to different companies?

The main and receiving Cost Centers must belong to the same Company. Use an [inter-company workflow](/erpnext/inter-company-invoices) when separate companies need to charge one another.

### Can I use a different ratio next month?

You can create a new allocation with the revised ratio and the correct Valid From date. ERPNext uses the allocation applicable to each transaction's Posting Date.

## Related topics

- [Cost Center Allocation](/erpnext/cost-center-allocation)
- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [General Ledger](/erpnext/general-ledger)
- [Budget](/erpnext/budget)

<!-- page: erpnext/erpnext__do-i-need-an-erp.md -->
---
title: "Do I Need ERPNext?"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/do-i-need-an-erp"
updated: "2026-08-14"
---

Are you still using multiple specialised tools/platforms for managing your operations and finding it challenging to maintain data consistency?

Are you hesitant to go paperless by digitising all your operations?

Are you fed up with your legacy system which is difficult to cater to your ever evolving business needs?



ERPNext will help you get rid of these pain points as it is an open source platform which will act as a single source of truth for all your operational needs. ERPNext can host all your data and replicate business processes to make them operate seamlessly. Since it covers a wide range of business functions/departments like Accounting, Procurement, Sales, HR, Inventory Management etc, ERPNext is a system that can be setup by any organisation.

### Benefits over traditional accounting software:

- **Integrated Modules:** ERPNext provides a complete package integrated modules including accounting, sales, purchasing, inventory, manufacturing, HR, CRM, and project management. This integration ensures that there is seamless data flow across various departments, reducing data silos and improving efficiency.
- **Easy Customisation:** Highly customisable to fit specific business needs where tailored workflows can be designed
- **Scalability:** the system can be scaled up with the growth of the business by accommodating increasing transaction volumes and additional functional requirements.
- **Unified Platform:** ERPNext facilitates better collaboration across departments as all data and processes reside on the same platform.
- **Real-Time Data:** Provides real-time visibility and accessibility to the business data allowing quick data driven decision making.
- **Comprehensive Reports:** Offers detailed reports and dashboards covering all aspects of the business providing deeper insights and analytics capabilities.

### Benefits over big ERPs

- **Minimum Investment**: Since it is open source, ERPNext eliminates the need for expensive licensing fees unlike big ERPs.
- **Affordable Implementation and Maintenance**: The implementation and maintenance cost of ERPNext is generally lower.
- **Open Source Nature**: ERPNext allows complete access to the source code, enabling deep customisations and integrations.
- **Faster Deployment Cycle**: ERPNext can be implemented more quickly unlike most of the big ERPs.
- **Active Community**: There is a widespread community of users and developers around the globe which provides support and contributes to the continuous improvement of the platform.
- **No Vendor Lock-In:** The open-source nature of ERPNext ensures that businesses are not locked into long-term contracts with a single vendor even through there is less satisfaction

<!-- page: erpnext/erpnext__doctype.md -->
---
title: "DocType\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/doctype"
updated: "2026-03-04"
---


**A DocType is the core building block of any application based on the Frappe Framework.**

It describes the Model and the View of your data. It contains what fields are stored for your data, and how they behave with each other. It contains information about how your data is named. The forms like Sales Order, Sales Invoices, Work Order are added as DocTypes in the backend.

DocType allows you to insert custom forms in ERPNext as per your requirement.

To create a new DocType, go to:

> Setup > Customize > Doctype > New

## 1. How to create a New DocType:

1. **Name**: Enter the name of the new DocType.
1. **Module**: Enter which module would you like the new DocType to be added to.
1. Save.

[Screenshot on the live page: Custom DocType]

### 1.1. Additional Details

1. **Fields**

 You can choose to add as many fields as you want. The Label, Field Type, Mandatory Fields and other associated Options can also be added here. Learn more about field types [here](/erpnext/field-types.html).

 [Screenshot on the live page: Fields in Custom DocType]

1. **Naming**

 Here you can choose if you would want each of your forms within this DocType to be named automatically. As given in the description, you can select the pattern for naming of the forms. The same can be a Field within the DocType, Naming Series, Prompt, A defined Naming Series, or a Format based Name. For Naming, you can also add a Description and the Name Case (as a Title Case or UPPER CASE)for your convenience.

 [Screenshot on the live page: Naming Custom DocType]

1. **Form Settings**

 Additional Settings for the Form, Image Fields, Attachments, Timeline etc. can be configured here. To know more about Form, visit [Customize Form](/erpnext/customize-form).

 [Screenshot on the live page: Custom DocType Form Settings]

1. **View Settings**

 Here, you can define the View settings for the DocType, like, Search Fields, Default Sort Field, Default Sort Order etc.

1. **Permission Rules**

 You can define the Permission Rules for the DocType here, and configure which users would be able to use or make changes to this DocType. Learn more about [Users and Permissions](/erpnext/users-and-permissions) here.

 [Screenshot on the live page: Custom DocType Permissions]

1. **Web View**

 You can select whether you would want a Web View of this DocType or no. Having a Web View for a DocType will allow your website users to have access to the Forms. Feel free to learn more about [Website Users](/erpnext/difference-between-system-user-and-website-user).

### 1.2. More Properties

1. **Is Submittable**: You can select if you want this DocType to only be 'Saved' or to also be 'Submitted' by checking and un-checking this box.
1. **Is Child Table**: You can define if you want the New DocType to be a Child Table within another DocType. Checkout [Child Table](/erpnext/customizing-data-visibility-in-child-table) for more information.
1. **Is Single**: If checked, this Doctype will become a single form, like Sales Order, which user will
not be able to re-produce. For e.g., Selling Settings in Sales Module is a Single DocType.
1. **Is Tree**: A few DocTypes in ERPNext are structured as Trees, wherein there are some Parent DocTypes and some Children DocTypes. E.g., Doctype Company is structured as Tree, there are Parent Companies as well as Child Companies, which we call subsidiaries. If you want your DocTypes to be structured similarly, you can enable this option.

 [Screenshot on the live page: DocType Tree View]

1. **Quick Entry**: You can select if you want a Quick Entry to be made for this DocType. This will allow you to enter only a few mandatory details and save the DocType, so that a Quick Entry is made. For example, check Quick Entry in [Journal Entry](/erpnext/journal-entry#11-quick-entry).
1. **Track Changes**: You can select this option if you want to maintain a log of the changes made to each Form. Check Out [Document Versioning](/erpnext/document-versioning) for more understanding on this.
1. **Track Seen**: You can select this option if you want to maintain a log of all the Users who have seen this Form.
1. **Track Views**: You can select this option if you want to maintain a log of all the times each User has Viewed this Form.

 [Screenshot on the live page: DocType Tree View]

1. **Custom?**: This field will be checked by default when adding Custom Doctype. Similarly, if you are customizing a DocType which already exists in the system, this field by default would be unchecked.

## 2. Videos


<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/WSzkpPm3iIU?start=585" width="560"></iframe>

<!-- page: erpnext/erpnext__document-follow.md -->
---
title: "Document Follow\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-follow"
updated: "2026-03-02"
---


> Introduced in v12

**Document Follow is a feature that allows users to track changes in documents via email notifications.**

## 1. How to Activate Document Follow
1. Go to: **Settings > My Settings**.
1. In the Document Follow section, tick the 'Send Notifications for documents followed by me' checkbox.
1. Set the frequency at which you want to receive emails.
1. Now, you can receive emails for the documents you follow.

## 1.1 How to Follow documents
1. Go to any document, you'll see an option to follow the document.
1. Click on 'Follow'.

[Screenshot on the live page: Defining Criteria]

1. After following, you can also unfollow a document.

1. Note that you can only follow documents for which track changes are on.
1. To enable track changes, go to **Menu > Customize > *tick the Track Changes checkbox***.

### 1.2 Automatic Follow
Cases where the document will be __automatically__ followed after activating Document Follow:

* When you create a new document.
* When you modify a document.
* When you like a document using the heart icon.
* When another user shares a document with you or assigns you to a document, you'll be following the document.

This is what an email notification for Document Follow will look like:

[Screenshot on the live page: Defining Criteria]

### 2. Related Topics
1. [Linking Emails to Document](/erpnext/linking-emails-to-document)
1. [Notifications](/erpnext/notifications)
