<!-- Frappe documentation: erpnext, part 15 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__cost-center.md -->
---
title: "Cost Center | ERPNext Documentation"
description: "Create a Cost Center hierarchy in ERPNext and use it to analyze income, expense, budgets, and profitability."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/cost-center"
updated: "2026-08-14"
---

The general ledger can tell you what Nova Industries spent. A Cost Center helps answer where the cost arose and which team, branch, project, or business unit is responsible for it.



Most businesses have multiple activities like different product lines, market

segments, areas of business that share some common overheads but should ideally have their own structure to report whether they are profitable or not. For this purpose, there is an alternate structure, called the

Cost Centers. Assigning Cost Centers lets managers compare the operating cost and profitability of each part of the business.



Let's take Nova Industries for example, and assume that their electronics company has multiple products lines - Mobile phones, Laptops and Tablets. Each is headed by a separate head of department who is responsible for the profitability of each of the product lines. Nova's Board and CEO needs the P&amp;L reported by each product line every month. How can this be enabled

Answer: Cost Center. 



Create the cost center for each product line, and tag every revenue or expense invoices to the correct cost center and Nova's finance team will be able to pull a report for profitability by each department. 



This page explains how to build the Cost Center tree, set sensible defaults, use Cost Centers in transactions such as Sales Invoices, and report on performance without creating separate ledger accounts for every internal team.

## Create the Cost Center tree

Go to **Home &gt; Accounting &gt; Accounting Masters &gt; Cost Center** and select the company.

![Cost Center tree](/files/cost-center-tree.webp)

Use group Cost Centers to organize the hierarchy. Use non-group Cost Centers on transactions.

1. Select the parent Cost Center.
2. Click **Add Child**.
3. Enter the name and company.
4. Enable **Is Group** only when the record will contain child Cost Centers.
5. Save.

![Cost Center details](/files/cost-center-details.webp)

## Use Cost Centers in transactions

Cost Centers appear on income and expense rows in Sales Invoices, Purchase Invoices, Journal Entries, and other accounting transactions. A company, Item, or transaction can provide the default.

### Example: assign a Cost Center on a Sales Invoice

Suppose Nova Electronics Trading wants to measure revenue from its online channel separately:

1. Create or open a **Sales Invoice**.
2. Add the Items being sold.
3. In the Items table, click the pencil icon for the required row.
4. Scroll to **Cost Center** and select **Online Sales - NET**.
5. Close the row editor and verify the remaining invoice details.
6. Save and submit the invoice.

![Open a Sales Invoice item row to select its Cost Center](/files/cost-center-sales-invoice.webp)

The Cost Center is stored on the item row. This means one invoice can allocate different lines to different Cost Centers. When the invoice is submitted, ERPNext includes the selected Cost Center in the income and expense ledger entries. You can then filter the Profit and Loss Statement or General Ledger by **Online Sales - NET** without using a separate income account.

If every row normally uses the same Cost Center, configure an appropriate default on the Company or Item. Always review the fetched value before submitting the invoice.

Use [Cost Center Allocation](https://docs.frappe.io/erpnext/cost-center-allocation) when one amount should be distributed among multiple Cost Centers by percentage.

## Reporting and budgets

Filter the Profit and Loss Statement, General Ledger, and other accounting reports by Cost Center. Group Cost Centers can summarize results for their descendants. You can also create [Budgets](https://docs.frappe.io/erpnext/budgeting) against Cost Centers to monitor or restrict spending.

## Design guidance

Use a stable hierarchy that reflects management responsibility. Avoid creating a Cost Center for every short project or customer. Use Project, party, or another Accounting Dimension when it represents the analysis more accurately.

## Troubleshooting

**A Cost Center does not appear**

Confirm it belongs to the transaction company, is enabled, and is not a group.

**The wrong Cost Center is fetched**

Check the Item, company default, and transaction row. The row value is the one used for posting.

## Related topics

- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)
- [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions)
- [Budgeting](https://docs.frappe.io/erpnext/budgeting)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)

<!-- page: erpnext/erpnext__cost_center_allocation.md -->
---
title: "Cost Center Allocation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/cost_center_allocation"
updated: "2026-08-14"
---

Cost Center Allocation automatically splits an amount posted to one main cost center across several receiving cost centers. It is useful when a shared transaction is entered once but management reporting needs the amount distributed consistently.



For example, Nova Electronics Trading may book a shared advertising expense to Main - NET. Instead of manually dividing every invoice, an allocation can send 50% to Retail Operations, 30% to Online Sales, and 20% to Corporate Sales.

## Before you begin

Create the required [Cost Centers](/erpnext/cost-center) and decide which cost center users will select in transactions. The receiving cost centers must belong to the same company.



Choose percentages that represent a defensible business basis, such as revenue, headcount, floor area, or usage. The total allocation must equal 100%.

## Create a Cost Center Allocation

Open the Cost Center Allocation list and select **Add Cost Center Allocation**.



![Cost Center Allocation list in ERPNext](/files/cost-center-allocation-list.webp)



Select the **Main Cost Center**. This is the cost center that users will choose on invoices, journal entries, and other accounting transactions. Set **Valid From** to the date from which the rule should apply.



![Main Cost Center and Valid From fields in a Cost Center Allocation](/files/allocation-main-and-date.webp)



In **Cost Center Allocation Percentages**, add each receiving cost center and its percentage. Use the pencil icon when you need to open a row and edit its details.



![Cost centers and percentages in a Cost Center Allocation](/files/allocation-percentages.webp)



Save and submit the allocation. ERPNext applies only submitted allocations.

## How allocation changes the ledger

The source transaction still shows the main cost center. When ERPNext creates General Ledger entries, it replaces the main cost center on eligible lines with the receiving cost centers and divides the amount using the submitted percentages.



If a $10,000 expense is posted to Main - NET using the example allocation, the expense-side ledger entries are distributed as follows:


| Receiving cost center   | Percentage | Allocated amount |
| ----------------------- | ---------- | ---------------- |
| Retail Operations - NET | 50%        | $5,000           |
| Online Sales - NET      | 30%        | $3,000           |
| Corporate Sales - NET   | 20%        | $2,000           |


The transaction total does not change. Only the cost center classification of the affected ledger amount is split. The payable, receivable, bank, or other balancing account continues to follow the transaction's normal accounting treatment.

## Important fields and what they mean


| Field            | Meaning                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| Main Cost Center | The cost center entered in transactions that triggers the allocation.     |
| Company          | The company to which the allocation and cost centers belong.              |
| Valid From       | The first date on which the allocation can be applied.                    |
| Cost Center      | A receiving cost center that will appear on the resulting ledger entries. |
| Percentage       | The share assigned to that receiving cost center.                         |


## Review the result

After submitting a transaction that uses the main cost center, open its **Accounting Ledger** from the document menu. Confirm that the relevant ledger amount has been divided across the expected cost centers and that the split totals the original amount.



You can also open the [General Ledger](/erpnext/general-ledger) report and filter by each receiving cost center. For period-level comparison, use the [Profit and Loss Statement](/erpnext/profit-and-loss-statement) with a cost center filter.

## Changing an allocation

Do not alter an allocation to rewrite the meaning of transactions already posted. Create a new allocation with a later Valid From date when the business basis changes. This keeps historical and future reporting rules understandable.



ERPNext checks the most recent applicable submitted rule for the transaction date. Avoid overlapping or ambiguous rules for the same main cost center.

## Troubleshooting

### The percentages cannot be saved

Check that every row has a cost center and percentage and that the percentages total exactly 100%.

### The transaction was not split

Confirm that the allocation is submitted, its Valid From date is on or before the transaction posting date, and the transaction uses the exact Main Cost Center from the allocation.

### ERPNext rejects the Valid From date

A new allocation cannot begin before the latest ledger entry already posted against that main cost center. Use a later date, then apply the rule to future transactions.

## Frequently asked questions

### Does allocation split the source invoice into several invoices?

The business document remains one transaction. ERPNext splits the applicable General Ledger amount by cost center.

### Can I allocate between companies?

A Cost Center Allocation works within one company. Use inter-company transactions for cross-company accounting.

### Can I use different percentages from a later date?

Create a new allocation with the revised percentages and a later Valid From date.

### Does the user need to select every receiving cost center?

The user selects the main cost center. The submitted allocation supplies the receiving cost centers automatically.

## Related topics

- [Cost Center](/erpnext/cost-center)
- [Accounting Dimensions](/erpnext/accounting-dimensions)
- [General Ledger](/erpnext/general-ledger)
- [Journal Entry](/erpnext/journal-entry)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Budget](/erpnext/budgeting)

<!-- page: erpnext/erpnext__country.md -->
---
title: "Country"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/country"
updated: "2026-08-14"
---

Country records provide shared localization defaults such as ISO code, date format, time format, and time zones. ERPNext includes a prepared country list, so administrators normally review the required record instead of creating a new one.



For Nova Industries in the United States, the Country record keeps US formatting available wherever ERPNext uses country-level defaults. Company, address, contact, and regional configuration can then refer to the same country consistently.

## Open a Country

Search for **Country** from the Awesomebar and open the list. Select the required record.

![Country list showing included country records and their formatting defaults](https://novacompanies.m.frappe.cloud/files/setup-20260814-country-list.png)



## Review localization fields

![United States Country record showing code, date format, time format, and time zones](https://novacompanies.m.frappe.cloud/files/setup-20260814-country-form.png)




| Field       | What it controls                                                        |
| ----------- | ----------------------------------------------------------------------- |
| Code        | ISO 3166 alpha-2 country code used by integrations and structured data. |
| Date Format | Default date presentation associated with the country.                  |
| Time format | Default presentation of time values.                                    |
| Time Zones  | Recognized time zones for the country.                                  |


## Country versus system defaults

The Country record stores country-level reference data. [System Settings](/erpnext/system-settings) controls the site language, time zone, date format, and number format used by default. [Global Defaults](/erpnext/global-defaults) and user preferences can further determine what a user sees. Review all three when formatting is unexpected.

## Troubleshooting

### The displayed date format is different

Check System Settings and the user’s language or locale. Country reference data does not override every site or user-level display preference.

### A regional feature is unavailable

Country alone may not enable a localization. Confirm the Company country, installed regional app, Domain Settings, and any required tax or compliance setup.

## Frequently asked questions

### Should I add a Country that already exists?

Reuse the prepared record and correct it only when verified country reference data is incomplete or outdated.

### Does changing Country convert existing transaction data?

It changes reference or default behavior. It does not rewrite historical addresses, currencies, taxes, or ledger entries.

## Related topics

- [Company](/erpnext/company-setup)
- [System Settings](/erpnext/system-settings)
- [Global Defaults](/erpnext/global-defaults)
- [Address](/erpnext/address)
- [Currency](/erpnext/currency)

<!-- page: erpnext/erpnext__coupon-code.md -->
---
title: "Create and Apply Coupon Codes | ERPNext Documentation"
description: "Configure ERPNext Coupon Codes with Pricing Rules, validity and usage limits, then apply promotional or gift-card codes in the web store."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/coupon-code"
updated: "2026-07-25"
---

A Coupon Code connects a customer-entered web-store code to a coupon-based [Pricing Rule](/erpnext/pricing-rule). Use it to offer a controlled discount through a promotional code or a customer-specific gift-card-style code.

## Before you begin

Confirm that:

- Your ERPNext web store is configured.
- Coupon entry is enabled in [E-commerce Settings](/erpnext/e-commerce-settings).
- The eligible [Items](/erpnext/item) and prices are available online.
- You have created a Selling Pricing Rule with **Coupon Code Based** enabled.

Coupon Code does not define the discount by itself. The linked Pricing Rule defines eligibility and the price or product discount.

## Create a coupon-based Pricing Rule

1. Open **Pricing Rule** and select **Add Pricing Rule**.
2. Configure the eligible Items, Item Groups, transaction conditions, quantity or amount limits, and validity.
3. Choose Price Discount or Product Discount.
4. Enable **Coupon Code Based**.
5. Save the rule.

![A Pricing Rule with Coupon Code Based highlighted.](https://novacompanies.m.frappe.cloud/files/coupon-pricing-rule.png)

Avoid overlapping coupon rules unless their intended priority is tested.

## Create a Coupon Code

1. Open the **Coupon Code** list and select **Add Coupon Code**.
2. Enter a Coupon Name.
3. Select the Coupon Type:
  - **Promotional** creates a reusable code derived from the name.
  - **Gift Card** generates a random code intended for more controlled distribution.
4. Select the coupon-based Pricing Rule.
5. Set Valid From and Valid Upto.
6. Set Maximum Use when total redemptions must be capped.
7. Add a description that can be reused in campaign communication.
8. Save.

![An ERPNext Coupon Code with type, Pricing Rule, dates, and usage limit.](https://novacompanies.m.frappe.cloud/files/coupon-code-form.png)

The generated Coupon Code is unique and read-only. Review it before sending campaign material.

## Apply a Coupon Code

A shopper can enter the code in the web-store coupon field. After ERPNext validates the code and linked rule, eligible prices are recalculated.

A campaign link can also include a coupon parameter:

`https://shop.example.com/products/aerobook-14?cc=SUMMER20`

Use only URLs supported by your current web-store implementation and test the complete customer journey before distribution.

## Usage and validity


| Field                   | What it controls                                          |
| ----------------------- | --------------------------------------------------------- |
| Coupon Type             | Whether the code is promotional or randomly generated     |
| Pricing Rule            | The discount and eligibility conditions                   |
| Valid From / Valid Upto | The redemption period                                     |
| Maximum Use             | Total number of permitted uses                            |
| Used                    | Number of submitted Sales Orders that consumed the coupon |
| Coupon Code Description | Supporting campaign or email text                         |


The Used count increases when qualifying orders are submitted. Cancelling or amending transactions can affect operational interpretation, so audit the linked sales records when usage appears unexpected.

## Test before launch

Test at least:

- An eligible Item and quantity.
- An ineligible Item.
- Dates before, during, and after validity.
- The maximum-use boundary.
- Logged-in and guest checkout when both are supported.
- Another automatic [Promotional Scheme](/erpnext/promotional-scheme) or discount that could overlap.

## Troubleshooting


| Problem                    | What to check                                                  |
| -------------------------- | -------------------------------------------------------------- |
| Coupon field is missing    | Enable coupon entry in E-commerce Settings                     |
| Code is rejected           | Check spelling, validity, maximum use, and linked Pricing Rule |
| Code applies no discount   | Confirm that the cart satisfies every Pricing Rule condition   |
| The wrong discount applies | Review overlapping Pricing Rules and priority                  |
| Used count is unexpected   | Review submitted Sales Orders that contain the coupon          |


## Frequently asked questions

### Can a Coupon Code be used in Desk sales transactions?

Coupon Code is designed for the web-store application flow. Use a Pricing Rule directly for Desk transactions.

### Is a Gift Card Coupon Code a stored-value payment instrument?

No. In this feature it is a generated code linked to a Pricing Rule, not a financial wallet.

### Can one Coupon Code link to several Pricing Rules?

A Coupon Code links to one Pricing Rule. Use that rule's conditions to define the offer.

### Can I limit one redemption per customer?

Maximum Use caps overall use. Confirm whether your current web-store workflow enforces any customer-specific limit you require.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Applying a Discount](/erpnext/applying-discount)
- [Shopping Cart](/erpnext/shopping-cart)
- [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__creating-custom-link-field.md -->
---
title: "Creating Custom Link Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/creating-custom-link-field"
updated: "2026-03-04"
---

Link fields are the ones linked to another document type. For example, Customer field is a Link Field in Sales Order. This field is linked to the Customer master.

You can insert Custom Link Field by following the steps below.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customize > Customize Form

#### Step 2: Select Form

In Customize Form, select Document Type (Quotation, Sales Order, Purchase Invoice Item etc.). Once fields are updated in the accompanying table below, open a field above the one you wish to insert your Custom Field. Then click on "Insert Above" to insert the new Custom Field.

![Select Docytpe](/files/customize-custom-link-field.gif)  


#### Step 4: Custom Field Values

To set field as Link, enter values as below.

1. Label: Desired label that user wishes to display in the form.
2. Type: Set as 'Link'
3. Name: Desired name for the field
4. Options: Enter the name of the DocType to which the field is linked

![Enter Values](/files/customize-creating-custom-link-fields.png)  


Adding Filters to Link Field
----------------------------


> Note: The feature will be available from version 15 and above.
> 
> 

Frappe provides a user-friendly approach to apply filters on Link Fields using the Form Builder.

You'll notice an action icon on all Link Fields within a Doctype, which gives you the option to select the filters you want to apply.![1](/files/1.png "1.png")  


For example, in the case of "Company", clicking on the icon will open a dialogue box where you can choose your desired filters.

![2](/files/2.png "2.png")  


Once you've made your selection and clicked on apply, the filtered results will be displayed accordingly.

![3](/files/3.png "3.png")  


If you're customizing a form and decide to change the filters, a "Reset To Default" button will appear. Clicking on this will revert the filters back to their original state. **However, it's important to note that any filters in "Customize Form" will override the default filters**

![4](/files/4.png "4.png")  


**Eval Support**

Users can add dynamic filters based on some value from the form.

**Use:**

`eval: doc.fieldname`

or

`eval: doc.fieldname1 + doc.fieldname2`

![Screenshot 2024-03-14 at 11.25.07 PM](/files/Screenshot 2024-03-14 at 11.25.07 PM.png)  


**For Child Tables:**  
2 types of filters can be added.

* From the Child Table Row: to add these filters use `doc.child_table_field_name`
* From Parent Document: to add these use `parent.parent_doc_fieldname`

![Screenshot 2024-03-19 at 12.28.35 PM](/files/Screenshot 2024-03-19 at 12.28.35 PM.png)  


the expression added after "eval:" is evaluated and its value is returned.

  



```
Note: Filters applied through frm.set_query, will take preference over filters applied via the User Interface (UI).
```
  

<!-- page: erpnext/erpnext__credit-limit.md -->
---
title: "Credit Limit | ERPNext Documentation"
description: "Learn how to set customer, customer group, and company credit limits in ERPNext, control sales exposure, and configure authorized overrides."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/credit-limit"
updated: "2026-07-23"
---

A Credit Limit in ERPNext is the maximum credit exposure your business allows for a Customer. When the applicable limit is reached, ERPNext can stop users from submitting a new Sales Order or Sales Invoice until the exposure is reduced or an authorized role approves the exception.

Credit limits help sales and finance teams apply a consistent credit policy without checking each customer balance manually. ERPNext supports limits at the Customer, Customer Group, and Company levels, so you can define a specific limit for an important account and use broader defaults for everyone else.

## Before you begin

- Agree on a credit policy with the finance team, including who can approve exceptions.
- Confirm that opening receivables, Sales Invoices, Payment Entries, and credit notes are current. The control is only as reliable as the outstanding balance.
- Create the relevant [Customer](/erpnext/customer), [Customer Group](/erpnext/customer-group), and [Company](/erpnext/company-setup) records.
- Assign the appropriate Company to each limit when your ERPNext site contains more than one company.
- Decide whether Sales Orders should reserve credit or whether the check should rely mainly on outstanding invoices.

## How ERPNext chooses the credit limit

ERPNext checks the available limits in this order:

1. **Customer:** A company-specific limit on the Customer record has the highest priority.
2. **Customer Group:** If the Customer has no applicable limit, ERPNext checks the Customer Group.
3. **Company:** If neither the Customer nor its group provides a limit, ERPNext uses the Company limit.


| Level          | When to use it                                                                           | Example                                                        |
| -------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Customer       | Use for an account with an individually approved facility.                               | Summit Digital Stores receives a USD 50,000 limit.             |
| Customer Group | Use as a shared policy for a class of customers when individual limits are not required. | Nova Commercial Customers receive a USD 100,000 default limit. |
| Company        | Use as the final fallback for customers without a more specific limit.                   | Nova Electronics Trading uses USD 250,000.                     |


A value of **0** does not create an effective limit at that level. ERPNext continues to the next applicable level. Set an explicit positive amount wherever you want the control to apply.

## Set a Credit Limit for a Customer

1. Open the Customer.
2. Select the **Accounting** tab.
3. In **Credit & Overdue Limits**, select **Add row**.
4. Select the Company.
5. Enter the approved Credit Limit.
6. Choose whether to enable **Bypass credit limit check at sales order**.
7. Save the Customer.

![Customer Accounting tab with the Credit and Overdue Limits table highlighted](https://novacompanies.m.frappe.cloud/files/customer-credit-limit.png)

The highlighted row gives Summit Digital Stores a USD 50,000 limit for Nova Electronics Trading. A Customer can have a different row for each Company.

## Alternative ways to set a Credit Limit

### Set a limit for a Customer Group

1. Go to **Selling > Settings > Customer Group**.
2. Open the required group.
3. In **Credit & Overdue Limits**, select **Add row**.
4. Select the Company and enter the Credit Limit.
5. Save the Customer Group.

![Customer Group with its company-specific Credit Limit row highlighted](https://novacompanies.m.frappe.cloud/files/customer-group-credit-limit.png)

Use a group limit to apply the same policy to customers in that group that do not have a customer-specific limit. It is not a combined pool shared by every customer in the group. The limit is evaluated for each customer.

### Set the Company fallback limit

1. Open the Company record.
2. Select the **Buying and Selling** tab.
3. Enter the fallback value in **Credit Limit**.
4. Save the Company.

![Company Buying and Selling tab with Credit Limit highlighted](https://novacompanies.m.frappe.cloud/files/company-credit-limit.png)

The Company limit is useful as a safety net, but it is usually broader than an individually approved customer facility. Review it together with the more specific limits before changing your credit policy.

## Important fields and what they mean


| Field                                    | What it means                                                                                                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Company                                  | The legal entity for which the limit applies. Add separate rows when the same Customer trades with multiple companies.                                     |
| Credit Limit                             | The maximum credit exposure permitted for that Customer and Company before ERPNext blocks a controlled transaction.                                        |
| Bypass credit limit check at sales order | Stops Sales Orders from reserving or validating against the credit limit for that Customer. Outstanding invoices can still affect the Sales Invoice check. |
| Credit Manager                           | The role allowed to approve and submit a transaction after the credit-limit validation is triggered.                                                       |
| Enable Overdue Billing Threshold         | Activates an additional Sales Invoice check based on the Customer’s overdue amount and configured overdue threshold.                                       |
| Overdue Billing Threshold                | The overdue amount permitted before a new Sales Invoice is blocked when the Accounts Setting is enabled.                                                   |


## Understand what uses the limit

ERPNext performs the credit check when a controlled sales transaction is submitted. The result depends on the Customer configuration and the current exposure for the selected Company.



- **Sales Order:** By default, open order value can use available credit. This helps prevent the business from accepting more commitments than the approved facility supports.
- **Sales Invoice:** Outstanding receivables are checked before a new invoice is submitted.
- **Payments and credit notes:** A submitted [Payment Entry](/erpnext/payment-entry) or [Sales Return](/erpnext/sales-return) can reduce the outstanding balance and restore available credit after ledgers are updated.

For example, if a Customer has a USD 50,000 limit and applicable exposure of USD 42,000, only USD 8,000 remains available. A new controlled transaction for USD 10,000 is blocked unless exposure is reduced or the authorized role approves the exception.

## Bypass the Sales Order check

Enable **Bypass credit limit check at sales order** when your policy should allow Sales Orders without reserving the customer’s credit facility. This can suit businesses that treat an order as a forecast or commitment but apply firm control only when billing.

Use this option carefully. It does not mean the Customer has unlimited credit. A later Sales Invoice may still be blocked when the outstanding exposure exceeds the applicable limit. Explain the policy to users so an accepted order does not create an expectation that finance will approve every invoice.

## Configure the override role

1. Open **[Accounts Settings](/erpnext/accounts-settings)**.
2. Select the **Credit Limits** tab.
3. Select the required role in **Credit Manager**.
4. Save Accounts Settings.

![Accounts Settings Credit Limits tab with the Credit Manager role highlighted](https://novacompanies.m.frappe.cloud/files/credit-manager.png)

When the validation is triggered, a user with the configured role can approve the exception and submit the transaction. Keep membership of this role limited to people who are authorized to accept credit risk. In older ERPNext documentation this setting may be called Credit Controller. The current field is Credit Manager and it selects a role.

## Submit and next steps

After saving the limits, create or open the required [Sales Order](/erpnext/sales-order) or [Sales Invoice](/erpnext/sales-invoice) and submit it normally. If the transaction is within available credit, submission continues. If it exceeds the applicable limit, ERPNext displays a validation message and stops submission for users who cannot approve the exception.

When a transaction is blocked:



1. Review the Customer’s outstanding invoices using [Accounts Receivable](/erpnext/accounts-receivable) or the Customer ledger.
2. Check whether payments, returns, or credit notes have been submitted and allocated correctly.
3. Confirm which Customer, Customer Group, or Company limit is taking precedence.
4. Collect or allocate payment, revise the transaction, change the approved limit, or request an authorized override.

## Good practices

- Record the approved amount in the most specific appropriate level.
- Review limits periodically and after material changes in payment behavior.
- Avoid giving every user the Credit Manager role.
- Use [Payment Terms](/erpnext/payment-terms) together with credit limits. Payment terms define when an amount is due, while the credit limit controls maximum exposure.
- Use [Dunning](/erpnext/dunning) and receivables reports for overdue follow-up rather than relying on the limit alone.
- Document why a limit was raised, lowered, or overridden.

## Troubleshooting

### The Customer limit is ignored

Confirm that the row uses the same Company as the transaction and contains a positive amount. Also check that the row was saved. If no applicable Customer limit exists, ERPNext uses the Customer Group and then the Company fallback.

### A Sales Order is not blocked

Open the Customer’s Accounting tab and check **Bypass credit limit check at sales order**. If it is enabled, the Sales Order check is intentionally bypassed. The later invoice can still be checked.

### A payment has not restored available credit

Confirm that the Payment Entry is submitted, posted to the correct Customer and Company, and allocated against the invoice where required. Review the [General Ledger](/erpnext/general-ledger) and Accounts Receivable report for the resulting balance.

### An authorized user still cannot submit

Check the Credit Manager role in Accounts Settings and confirm that the user has that role. Ask the user to reload ERPNext after a role change so the current session receives the updated permissions.

### The wrong fallback limit is applied

Review the Customer Group assigned to the Customer and the Company selected on the transaction. Remember that Customer takes precedence over Customer Group, and Customer Group takes precedence over Company.

## Frequently asked questions

### Can one Customer have different limits for different companies?

Yes. Add one row per Company on the Customer record. This keeps the credit policy separate for each legal entity.

### Is a Customer Group limit shared by all customers?

No. It acts as the default limit evaluated for each customer in that group when a more specific Customer limit is not available.

### Does setting 0 mean no credit is allowed?

No. A zero value does not create an effective limit at that level. ERPNext continues to the next applicable level.

### Can a user submit a transaction above the limit?

Only a user with the role configured as Credit Manager can approve the exception. Restrict that role according to your credit policy.

### Should I bypass the Sales Order check?

Bypass it only when your business intentionally controls credit at invoicing rather than at order acceptance. Keep the default check when accepted orders should reserve available credit.

<!-- page: erpnext/erpnext__credit-note.md -->
---
title: "Credit Note | ERPNext Documentation"
description: "Create full or partial credit notes in ERPNext, return stock, reverse receivables, and allocate or refund customer credit."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/credit-note"
updated: "2026-08-14"
---

Northstar Retail returns one phone after Nova Industries has already submitted the Sales Invoice. Nova must reduce what the customer owes and, if the phone physically comes back, return it to stock. Editing or deleting the original invoice would hide what actually happened.



A **Credit Note** records the correction while preserving the original sale and its audit trail. It can reduce the Customer's outstanding balance, reverse the related income and tax, and optionally bring returned goods back into the Warehouse.



In ERPNext, a Credit Note is a Sales Invoice marked as a return, with negative quantities and amounts. Use it for a full or partial return, an agreed price reduction, or another post-invoice correction. This guide explains how to create it from the original invoice and decide whether to refund, allocate, or retain the resulting credit.

## Before you begin

Identify the original submitted [Sales Invoice](/erpnext/sales-invoice). If stock is being returned, confirm the receiving Warehouse. If the customer has already paid, decide whether the credit will be refunded or allocated against another invoice.

## Create a Credit Note from a Sales Invoice

1. Open the original Sales Invoice.
2. Select **Create &gt; Return / Credit Note**.

![Create a Return or Credit Note from the submitted Sales Invoice](https://novacompanies.m.frappe.cloud/files/credit-note-credit-note-create-action.png)

3. Review the Customer, Company, posting date, return Warehouse, and reference invoice.
4. Keep only the returned lines and enter the returned quantity. ERPNext displays return quantities and amounts as negative values.
5. Enable **Update Stock** when the goods physically return to inventory.
6. Review taxes and totals, then save and submit.

Creating the Credit Note from the original invoice preserves the reference and copies the original items, rates, taxes, and accounts. This is safer than creating an unreferenced return when the original invoice is known.



![Credit Note with the return reference and Update Stock setting](https://novacompanies.m.frappe.cloud/files/credit-note-credit-note-reference-and-stock.png)

## Full and partial credits

For a full return, return the complete invoiced quantity. For a partial return, remove unaffected lines or reduce the returned quantity. ERPNext prevents the cumulative returned quantity from exceeding the original invoiced quantity.



![Returned quantities, amounts, receiving Warehouse, and the item-row edit action on a Credit Note](https://novacompanies.m.frappe.cloud/files/credit-note-credit-note-negative-items.png)

For price-only corrections where no goods move, leave **Update Stock** off. The Credit Note will reverse the receivable and income or tax effect without changing the Stock Ledger.

When stock is returning, confirm the receiving **Warehouse** shown for each item row before submission. Use the highlighted row edit action when you need to change it.

## Refund or allocate the credit

After submission, the Credit Note creates a negative receivable against the Customer.

- To refund the customer, create a [Payment Entry](/erpnext/payment-entry) against the Credit Note.
- To use the credit against another Sales Invoice, allocate it through [Payment Reconciliation](/erpnext/payment-reconciliation) or a correctly referenced Journal Entry.
- To leave it available for a future purchase, keep the credit unallocated until the next invoice is ready.

Always reference both the Credit Note and the invoice being settled. A general Customer ledger entry without voucher references will not close the individual outstanding documents.

## Ledger and stock effect


| Action                           | Receivable                     | Income and tax               | Stock                                    |
| -------------------------------- | ------------------------------ | ---------------------------- | ---------------------------------------- |
| Credit Note without Update Stock | Reduced                        | Reversed for credited amount | No change                                |
| Credit Note with Update Stock    | Reduced                        | Reversed for credited amount | Returned quantity and stock value posted |
| Refund Payment Entry             | Credit is settled              | No new sales reversal        | No change                                |
| Allocate against new invoice     | Both open vouchers are reduced | No new sales reversal        | No change                                |


## When to cancel instead

If an unpaid invoice was created by mistake and the entire transaction should not exist, cancellation may be simpler. Use a Credit Note when you need to keep the original invoice and record a partial return, a post-invoice adjustment, or a refund after payment.

## Troubleshooting

**The return quantity is rejected**

Check previous Credit Notes against the same invoice. The total returned quantity cannot exceed the invoiced quantity.

**Stock should not move**

Turn off **Update Stock** before submitting. Do not use a stock return for a price-only adjustment.

**The Customer still has an outstanding balance**

Open the Accounts Receivable report and check whether the Credit Note or refund has been allocated to the correct voucher.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Accounts Receivables](/erpnext/accounts-receivables)
- [Debit Note](/erpnext/debit-note)
