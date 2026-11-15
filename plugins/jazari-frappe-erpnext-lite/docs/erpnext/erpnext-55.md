<!-- Frappe documentation: erpnext, part 55 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__salesperson-permissions.md -->
---
title: "Restrict Sales Users to Their Customers and Transactions | ERPNext Documentation"
description: "Learn how to use ERPNext roles and User Permissions so sales users see only assigned Leads, Customers, and transactions linked to those Customers."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/salesperson-permissions"
updated: "2026-07-25"
---

Use [User Permissions](/erpnext/user-permissions) when a sales user should work only with named Leads, Customers, and the sales transactions connected to those Customers. A [Sales Person](/erpnext/sales-person) record is useful for targets, commissions, and the Sales Team table, but assigning a Sales Person does not by itself create record-level access restrictions.

This guide uses Avery Stone as a sales user. Avery can work with Northstar Retail, Summit Digital Stores, and two assigned Leads, but not the rest of the sales portfolio.

## Before you begin

- You need System Manager or equivalent permission to manage Users and User Permissions.
- The user must be a System User with the roles required for their work.
- Create the relevant [Customers](/erpnext/customer) and [Leads](/erpnext/lead) first.
- Decide whether access will be maintained customer by customer or through a grouping master such as [Territory](/erpnext/territory).

> **Roles and User Permissions do different jobs.** A role grants access to a document type. A User Permission limits which records of that type the user can access.

## 1. Give the user the required sales role

1. Open **User** and select the sales user.
2. Open **Roles &amp; Permissions**.
3. Enable **Sales User**.
4. Add another role only when the person needs the corresponding actions. For example, do not assign Sales Manager merely to make the workspace visible.
5. Save the User.

![Avery Stone User form with the Sales User role highlighted.](/files/01-sales-user-role.webp)

The Sales User role normally provides access to sales masters and transactions according to the configured [Role Permission Manager](/erpnext/permissions). User Permissions added in the following steps narrow that access.

## 2. Open User Permission

Go to **Users and Permissions &gt; User Permission**, then select **Add User Permission**.

![User Permission list with Add User Permission highlighted.](/files/02-open-user-permissions.webp)

You can also open the User and use **Permissions &gt; Set User Permissions**. Both routes create the same User Permission records.

## 3. Allow the Customers assigned to the sales user

Create one User Permission for each Customer in the user's portfolio:

1. In **User**, select the sales user.
2. Set **Allow** to **Customer**.
3. In **For Value**, select an allowed Customer.
4. Save the User Permission.
5. Repeat for each additional Customer.

![User Permission for Avery Stone allowing access to Northstar Retail, with User, Allow, and For Value highlighted.](/files/03-customer-user-permission.webp)

For example, Avery has separate permissions for Northstar Retail and Summit Digital Stores. ERPNext combines permissions for the same master, so Avery can access either Customer.

### Why this also restricts sales transactions

A Customer is linked from documents such as a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), and [Sales Invoice](/erpnext/sales-invoice). When the user's role applies User Permissions, the Customer restriction is carried into those linked documents.

This means you normally do not create separate User Permissions for every Sales Order or Sales Invoice. Maintain the Customer portfolio, and the restriction follows the Customer link.

## 4. Add Lead permissions separately

A Lead is not yet a Customer. A Customer permission therefore cannot decide which unconverted Leads the user may access.

Create a separate User Permission for each assigned Lead:

1. Select the same sales user.
2. Set **Allow** to **Lead**.
3. Select the permitted Lead in **For Value**.
4. Save and repeat for the user's other Leads.

When a Lead is converted, add the resulting Customer to the user's Customer permissions. Review the old Lead permission according to your retention policy.

## 5. Apply the restriction to linked document types

Keep **Apply To All Document Types** enabled when the Customer permission should restrict every supported document containing a Customer link.

![Apply To All Document Types highlighted on a Customer User Permission.](/files/04-apply-to-all-doctypes.webp)

Clear this option only when the permission must apply to one specific document type. After clearing it, select that document type in **Applicable For**. For example, limiting a Customer permission to Sales Order would not provide the same restriction across Quotations, Delivery Notes, and Sales Invoices.

## 6. Review the complete portfolio

Open the User Permission list and filter by the user. Confirm that every permitted Customer and every unconverted Lead appears once.

![User Permission list showing two Customers and two Leads allowed for Avery Stone.](/files/05-customer-and-lead-permissions.webp)

In this example, Avery can access:

- Northstar Retail and Summit Digital Stores;
- the sales transactions linked to those Customers; and
- Leads CRM-LEAD-2026-00001 and CRM-LEAD-2026-00002.

Avery should not receive a broad Customer, Customer Group, or Territory permission that includes the rest of the portfolio. A broader permission expands access rather than overriding the individual Customer permissions.

## 7. Verify access before handing over the account

Do not assume that a saved permission produces the intended result.

1. Open the User.
2. Select **Permissions &gt; View Permitted Documents**.
3. Check Customer, Lead, Quotation, Sales Order, Delivery Note, and Sales Invoice.
4. Confirm that permitted records appear and an unrelated Customer does not.
5. Test list views and the reports the user will actually use.

![Permissions menu with View Permitted Documents highlighted on the Avery Stone User form.](/files/06-view-permitted-documents.webp)

For a final security check, sign in with a non-administrator test user that has the same roles and permissions. System Manager and Administrator accounts can bypass restrictions and are not suitable for validating a salesperson's experience.

## How access is determined


| Configuration                 | What it controls                                                        |
| ----------------------------- | ----------------------------------------------------------------------- |
| Sales User role               | Which sales document types and actions are available                    |
| Customer User Permission      | Which Customers and Customer-linked transactions the user can access    |
| Lead User Permission          | Which specific unconverted Leads the user can access                    |
| Apply To All Document Types   | Whether the allowed value restricts all supported linked document types |
| Applicable For                | Limits one User Permission to a selected document type                  |
| Apply Strict User Permissions | Controls whether records with a blank restricted link remain visible    |


## When there are many Customers

Individual Customer permissions are precise and easy to audit, but they require maintenance when portfolios change. If Customers and Leads are cleanly divided by region, create a User Permission for the appropriate Territory instead. A parent Territory can also include descendants unless **Hide Descendants** is enabled.

Use a grouping master only when it matches the real access boundary. Do not use [Customer Group](/erpnext/customer-group) for access if the group exists mainly for pricing or reporting and contains Customers belonging to several salespeople.

## Records with a blank Customer or Territory

Review **Apply Strict User Permissions** in [System Settings](/erpnext/system-settings). When strict permissions are enabled, a record with a blank restricted link is hidden. When they are not enabled, records whose restricted link is blank may remain visible.

Before enabling this setting, review integrations and older data for missing Customer or Territory values. Test the effect on all teams because it is a system-level setting.

## Troubleshooting


| Problem                                             | What to check                                                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| The user can still see every Customer               | Check for a broader Customer, Customer Group, or Territory permission. Confirm the user's role has Apply User Permissions enabled. |
| The user cannot open any sales transactions         | Confirm the Sales User role grants Read access and that the transaction contains an allowed Customer.                              |
| The user can see unrelated records with blank links | Review missing Customer or Territory values and the Apply Strict User Permissions setting.                                         |
| Assigned Leads are missing                          | Create Lead User Permissions separately. Customer permissions do not cover unconverted Leads.                                      |
| A report shows more data than expected              | Test the report with the restricted user. Review custom or script reports to confirm they apply permission-aware queries.          |
| A manager cannot see a salesperson's portfolio      | Add the required broader permissions to the manager. A Sales Person hierarchy does not automatically replace User Permissions.     |


## Frequently asked questions

### Is linking a User to a Sales Person enough?

Sales Person assignment supports sales attribution, targets, and commission reporting. Use User Permissions for record-level restrictions.

### Must I add every Sales Order to User Permissions?

Allow the Customer and keep Apply To All Document Types enabled. Supported Customer-linked transactions inherit that restriction.

### Can one salesperson have several Customers and Leads?

Y

es. Create one User Permission for each allowed value, or use a suitable Territory when the portfolio follows that hierarchy.

### Can sales managers see all records?

Yes, if their roles and User Permissions grant the broader access. Test managers separately instead of assuming the Sales Person tree controls visibility.

## Related topics

- [User Permissions](/erpnext/user-permissions)
- [Role Based Permissions](/erpnext/permissions)
- [Adding Users](/erpnext/adding-users)
- [Sales Person](/erpnext/sales-person)
- [System Settings](/erpnext/system-settings)

<!-- page: erpnext/erpnext__scrap-management.md -->
---
title: "Production Scrap Management\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/scrap-management"
updated: "2026-03-02"
---


Scrap means waste that either has no economic value or only the value of its basic material content recoverable through recycling.

Scrap is generally availed at the end of the manufacture process. Also you can find some products that are damaged or that are unusable due to expiry or for some other reason, which needs to be scraped.

In ERPNext, at the end of manufacturing process, scrap items are accounted in the scrap warehouses.

## Scrap in Bill of Materials

You can update estimated scrap quantity of an item in the BOM, Scrap table. If required, you can reselect a raw-material item as scrap.

![Scrap in BOM](/files/scrap-1.png)

## Scrap in Manufacture Entry

When production is completed, Finish / Manufacture Entry is created against a Production Order. In this entry, scrap item is fetched in the Item table, with only Target Warehouse updated for it. Ensure that Valuation Rate is updated for this item for the accounts posting purposes.

![Scrap in Manufacture Entry](/files/scrap-2.gif)

> Scrap from the BOM will only work if Manufacture Entry is created based on BOM, and not based on Material Transfer. This is configurable from Manufacturing Settings.

![Manufacturing Settings](/files/manufacturing-settings.png)

<!-- page: erpnext/erpnext__scrapping-an-asset.md -->
---
title: "Scrapping an Asset | ERPNext Documentation"
description: "Scrap an unusable ERPNext Asset and verify the write-off, status, and remaining book value."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/scrapping-an-asset"
updated: "2026-08-15"
---

Imagine a Nova Industries machine is damaged beyond repair and has no resale value. It is still shown in the accounts with some remaining value, so simply throwing it away would leave the books saying the company owns something that no longer exists.



Scrapping an Asset closes that gap. ERPNext marks the asset as scrapped, removes its remaining carrying value through the correct accounts, and keeps the disposal history for audit.

## Before you begin

Confirm the Asset is physically retired, approvals are complete, depreciation is current, and the correct loss or disposal account is configured. Scrapping is an accounting action, not a way to hide a missing asset.

## Scrap the Asset

1. Open the submitted Asset.
2. Use the **Scrap Asset** action.
3. Confirm the posting or disposal date.
4. Review the generated Journal Entry before final submission where the workflow allows.
5. Complete the action.

![Asset status and scrap Journal Entry fields](https://novacompanies.m.frappe.cloud/files/21-asset-disposal-state.png)

## Verify the write-off

The Asset status becomes **Scrapped**. The entry removes the remaining carrying value using the fixed-asset, accumulated depreciation, and loss accounts.

![Asset balances used to check carrying value before scrapping](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

Confirm the Fixed Asset Register no longer treats the asset as active after the disposal date.

![Fixed Asset Register used after scrapping](https://novacompanies.m.frappe.cloud/files/24-fixed-asset-register.png)

## Troubleshooting

### The Scrap action is unavailable

Confirm the Asset is submitted, not already disposed, and has no blocking draft or submitted lifecycle documents.

### The write-off amount is unexpected

Reconcile capitalized value, booked depreciation, value adjustments, and the disposal date before proceeding.

## Frequently asked questions

### Is scrapping the same as selling for zero?

In ERPNext, no. Scrapping is a write-off workflow without customer proceeds.

### Can a fully depreciated asset be scrapped?

In ERPNext, yes. The remaining carrying value may be only the residual value, but status and disposal history still need to be closed correctly.

### Can a scrapped asset be used again?

Treat scrapping as a final disposal. Reverse only through the supported accounting correction process when the original action was genuinely wrong.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__search-record-by-specific-field.md -->
---
title: "Search Record by Specific Field\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/search-record-by-specific-field"
updated: "2026-03-04"
---


While creating any DocType, you may want to link a particular field to another DocType. For example, in Sales Order DocType, 'Customer' field allows you to select an existing customer. Such fields are called [Link Fields](/erpnext/field-types#link).

Using Link Fields you can create a


Let's assume that you want to see that Item in a Sales Order along with its Item Group. The steps to do this are given below:

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Select the Document for which you want multiple fields to be visible in the Search Field

Here, we will select the Document Item.

#### Step 3: Search Field

Update Warehouse field name in the Search By field.

![Search By in Customize Form](/files/customize-search-record-1.png)
![Search By in Customize Form](/files/customize-search-record-2.png)

Once these settings have been updated, while creating a Sales Order, when you select the Item, you will also be able to the warehouse there.

![Search By in Customize Form](/files/customize-search-record-3.png)

<!-- page: erpnext/erpnext__secondary-items.md -->
---
title: "Secondary Items"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/secondary-items"
updated: "2026-08-26"
---

:::note
**Available only in version 16 of ERPNext**
:::



Starting from version 16, Scrap Items table in the BOM DocType has been renamed to Secondary Items table. The secondary items table now includes items of 3 more types: `Co-Product`, `By-Product` and `Additional Finished Good` . Using this table, users can now specify the distribution of the outgoing cost (or raw material cost) amongst all the outputs based on a percentage system.

Let's first understand the difference between `Scrap`, `Co-Product` , `By-Product` and `Additional Finished Good`.

1. Scrap: An item which is produced alongside the Finished Good which, in most cases, does not have much value.
2. Co-Product: Item produced alongside the main Finished Good which is planned and has significant value.
3. By-Product: This item is produced alongside the finished good which is not planned. This item may or may not have significant value.
4. Additional Finished Good: This item is planned and has significant value. It is usually produced separately from extra materials, leftover capacity or further processing.

In ERPNext, there is virtually no difference on how these secondary items' value and quantity is calculated. The different names are merely for distinction purposes.

You can specify the process loss percentage and cost allocation percentage of each secondary item in the table.

![](/files/image01125b.png)

In this example, we are saying that in manufacturing petrol, 10% of the outgoing (raw material) cost should be allocated to LPG and 5% to Bitumen. The remaining 85% will be allocated to the actual finished good (Petrol).

Let's see it in action:

![](/files/CleanShot 2026-03-11 at 12.31.02@2x.png)

Here, the outgoing cost is Rs. 100. 10% of 100 is 10 which is allocated to LPG and 5% is 5 which is allocated to Bitumen. Since we specified a 5% process loss for Bitumen, it's quantity has been calculated as 9.5 ( `10 - (5% * 10)`).

:::note
**If you are migrating from earlier versions of ERPNext, the scrap items table will stay as it was. The calculations in Manufacture Entry and Subcontracting Receipt will stay the same as it was before migrating.**
:::

<!-- page: erpnext/erpnext__selling-an-asset.md -->
---
title: "Selling an Asset | ERPNext Documentation"
description: "Sell an ERPNext Asset, calculate gain or loss, and verify its disposal and ledger impact."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-an-asset"
updated: "2026-08-15"
---

Imagine Nova Industries sells an old inspection camera for $1,500. The camera originally cost more, but part of that cost has already been recorded as depreciation. The accountant cannot treat the $1,500 like an ordinary product sale because the remaining asset value must also be removed.



Selling an Asset records the customer amount, removes the asset's cost and accumulated depreciation, and calculates the gain or loss. The Asset remains in the register with a **Sold** status so its history is not lost.

## Before you begin

Confirm the Asset is submitted, not already sold or scrapped, and that depreciation is posted up to the disposal date according to policy. Prepare the customer and disposal accounts.

## Create the sale

1. Open the Asset and use **Create &gt; Sales Invoice**, or create a [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice) and select the fixed-asset Item and Asset.
2. Enter the customer, posting date, Asset, quantity, and sale rate.
3. Review taxes and disposal accounts.
4. Submit the Sales Invoice.

![Asset selected before disposal through a Sales Invoice](https://novacompanies.m.frappe.cloud/files/07-asset-core-details.png)

## Verify the disposal

The Asset status becomes **Sold** and its disposal date is recorded. Review the Sales Invoice, Journal Entry or General Ledger to confirm receivable, asset cost, accumulated depreciation, and gain or loss.

![ERPNext Asset disposal status fields](https://novacompanies.m.frappe.cloud/files/21-asset-disposal-state.png)

Use the Fixed Asset Register to confirm the asset no longer appears as an active existing asset for the relevant date.

![Fixed Asset Register used to verify disposal](https://novacompanies.m.frappe.cloud/files/24-fixed-asset-register.png)

## Troubleshooting

### The Asset cannot be selected on the Sales Invoice

Confirm the Item is a fixed asset, the Asset is submitted and available, and the company matches.

### Gain or loss looks wrong

Check sale proceeds, disposal date, net book value, booked depreciation, taxes, and selected accounts.

## Frequently asked questions

### Should I create a normal sales item for the asset?

Use the fixed-asset Item and link the specific Asset so ERPNext can perform disposal accounting.

### Does selling cancel the Asset?

In ERPNext, no. It changes lifecycle status to Sold and preserves the history.

### Can I sell a partially depreciated asset?

In ERPNext, yes. Gain or loss is based on sale proceeds versus carrying value at disposal.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__selling-cycle-ledger-impact.md -->
---
title: "Selling Cycle Ledger Impact"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/selling-cycle-ledger-impact"
updated: "2026-08-14"
---

The selling cycle begins with a commercial commitment and ends when the customer pays. Not every document creates an accounting entry. 



A Sales Order records what you have agreed to sell, while Delivery Notes, Sales Invoices, and Payment Entries record the financial events that follow.



The examples below use common account names and exclude sales tax to keep the entries easy to follow. Your account names may differ. ERPNext posts to the accounts configured for your Company, Item, Item Group, warehouse, and transaction.

## Understand when the ledger changes

ERPNext creates General Ledger entries when an accounting or stock transaction is submitted. Saving a draft does not affect the ledger.


| Document                      | Typical ledger impact                                                         | What it represents                                                        |
| ----------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Sales Order                   | No General Ledger entry                                                       | A commitment to supply goods or services at an agreed quantity and price. |
| Delivery Note for stock items | Debit Cost of Goods Sold; credit Stock In Hand                                | The inventory has left the company and its valuation becomes an expense.  |
| Sales Invoice                 | Debit Accounts Receivable; credit Sales. Credit Tax Payable when tax applies. | Revenue is recognized and the customer now owes the invoiced amount.      |
| Payment Entry, Receive        | Debit Bank or Cash; credit Accounts Receivable                                | Money is received and the customer's outstanding balance is reduced.      |


The debit and credit are two sides of the same event. For example, receiving a customer payment increases Bank, so Bank is debited. It also reduces the customer's receivable balance, so Accounts Receivable is credited.

## Example 1: Manufacturing company selling finished goods

Assume a manufacturer sells two finished phones to Cedar Commerce for $699 each, for a total selling price of $1,398. ERPNext values the two finished units at $866.76. The manufacturing costs were accumulated into inventory before this selling cycle began.

### 1. Submit the Sales Order

The submitted Sales Order records the customer's order for two finished phones. It reserves the commercial commitment, but it does not recognize revenue, reduce inventory, or create a receivable.

**Ledger impact:** None.



![Submitted Sales Order for two finished phones](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702217-01-goods-sales-order-commitment.png)

### 2. Submit the Delivery Note

The Delivery Note confirms that the finished goods have left the warehouse. ERPNext removes their current valuation from the stock asset and recognizes that valuation as the cost of the sale.


| Account            | Debit   | Credit  | Explanation                                           |
| ------------------ | -------: | -------: | ----------------------------------------------------- |
| Cost of Goods Sold | $866.76 |         | The inventory cost becomes an expense.                |
| Stock In Hand      |         | $866.76 | The value of inventory held by the company decreases. |


![General Ledger entries created by the Delivery Note](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702449-02-goods-delivery-note-ledger.png)

The debit is based on valuation, not the customer selling price. That is why the Delivery Note posts $866.76 even though the customer will be invoiced $1,398.

### 3. Submit the Sales Invoice

The Sales Invoice recognizes revenue and creates the amount due from the customer.


| Account                       | Debit     | Credit    | Explanation                          |
| ----------------------------- | ---------: | ---------: | ------------------------------------ |
| Accounts Receivable (Debtors) | $1,398.00 |           | The customer now owes the company.   |
| Sales                         |           | $1,398.00 | Revenue from the sale is recognized. |


![General Ledger entries created by the goods Sales Invoice](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702512-03-goods-sales-invoice-ledger.png)

Ignoring tax and other costs, the gross profit visible from these two events is $531.24: sales of $1,398.00 less cost of goods sold of $866.76.

### 4. Receive the customer payment

When the customer pays the full invoice, submit a Receive-type Payment Entry and allocate it to the Sales Invoice.


| Account                       | Debit     | Credit    | Explanation                                 |
| ----------------------------- | ---------: | ---------: | ------------------------------------------- |
| Bank                          | $1,398.00 |           | Money received increases the bank balance.  |
| Accounts Receivable (Debtors) |           | $1,398.00 | The amount owed by the customer is cleared. |


![General Ledger entries created by the customer Payment Entry](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702572-04-goods-payment-entry-ledger.png)

The Payment Entry does not recognize sales income again. The Sales Invoice already recorded the income. The payment only moves the balance from Accounts Receivable to Bank.

## Example 2: Services company

Assume a service company agrees to perform 20 device-setup sessions for Bluewave Systems at $150 each. The total contract value is $3,000.

Services do not normally move inventory, so this workflow can go directly from Sales Order to Sales Invoice and Payment Entry. A Delivery Note is unnecessary unless the company uses it as an operational confirmation of service delivery.

### 1. Submit the Sales Order

The Sales Order records the agreed scope, quantity, rate, and delivery date. It does not create revenue or a receivable.

**Ledger impact:** None.



![Submitted Sales Order for device setup services](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702644-05-service-sales-order-commitment.png)

### 2. Submit the Sales Invoice

After completing the agreed work, submit the Sales Invoice. Because the Item is a non-stock service, no Stock In Hand or Cost of Goods Sold entry is created by this invoice.


| Account                       | Debit     | Credit    | Explanation                                 |
| ----------------------------- | ---------: | ---------: | ------------------------------------------- |
| Accounts Receivable (Debtors) | $3,000.00 |           | The customer owes the invoiced service fee. |
| Sales or Service Income       |           | $3,000.00 | Service revenue is recognized.              |


![General Ledger entries created by the service Sales Invoice](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661702936-06-service-sales-invoice-ledger.png)

Employee costs, contractor charges, travel, and other delivery expenses are recorded through their own payroll, expense, purchase, or journal workflows. They are not automatically posted as Cost of Goods Sold merely because a service Sales Invoice is submitted.

### 3. Receive the customer payment

The Payment Entry has the same basic effect as it does for a goods sale.


| Account                       | Debit     | Credit    | Explanation                                    |
| ----------------------------- | ---------: | ---------: | ---------------------------------------------- |
| Bank                          | $3,000.00 |           | The company's bank balance increases.          |
| Accounts Receivable (Debtors) |           | $3,000.00 | The customer's outstanding balance is cleared. |


![General Ledger entries created by the service Payment Entry](https://novacompanies.m.frappe.cloud/files/selling-cycle-ledger-1785661703030-07-service-payment-entry-ledger.png)

## Compare the two workflows


| Stage       | Manufacturing or stock goods                                      | Services                                                       |
| ----------- | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| Sales Order | No ledger impact                                                  | No ledger impact                                               |
| Delivery    | Delivery Note reduces Stock In Hand and debits Cost of Goods Sold | Usually no stock Delivery Note or stock posting                |
| Invoice     | Debits Accounts Receivable and credits Sales                      | Debits Accounts Receivable and credits Sales or Service Income |
| Payment     | Debits Bank and credits Accounts Receivable                       | Debits Bank and credits Accounts Receivable                    |


If a stock-item Sales Invoice is submitted with **Update Stock** enabled, ERPNext combines the stock effect of the Delivery Note with the revenue and receivable effect of the Sales Invoice. The result is valid, but the company loses a separate delivery document in the audit trail.

If users create a Sales Invoice directly without a Sales Order, the Sales Invoice still creates the same ledger entries. What is missing is the earlier commercial commitment, order tracking, and link between ordered and billed quantities.

## Frequently asked questions

### Does submitting a Sales Order affect the General Ledger?

A Sales Order is a commercial commitment. It can influence order, delivery, reservation, and billing reports, but it does not create debit or credit entries.

### Why is Cost of Goods Sold different from the selling price?

Cost of Goods Sold uses the item's stock valuation. Sales uses the price charged to the customer. The difference contributes to gross profit.

### What changes when sales tax is included?

Accounts Receivable is debited for the full invoice total. Sales is credited for the net revenue, and the applicable tax liability account is credited for the tax collected from the customer.

### Can a services company use a Delivery Note?

Yes, if it wants a separate operational record confirming service delivery. A non-stock service Delivery Note does not reduce Stock In Hand. Many service companies invoice directly from the Sales Order instead.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)
- [Selling cycle](/erpnext/selling)

<!-- page: erpnext/erpnext__Selling-in-different-UOM.md -->
---
title: "Sell Items in Different Units of Measure | ERPNext Documentation"
description: "Configure ERPNext UOM conversions, UOM-specific Item Prices, and sales transaction quantities for packs, cartons, units, and fractional measures."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/Selling-in-different-UOM"
updated: "2026-07-25"
---

ERPNext can sell the same Item in different Units of Measure while maintaining stock in one Stock UOM. Configure each allowed UOM and conversion factor on the Item, then select the selling UOM in a transaction.

## Before you begin

Confirm:

- The required [Units of Measure](/erpnext/unit-of-measure-uom).
- The Item's Stock UOM.
- Accurate conversion factors.
- UOM-specific [Item Prices](/erpnext/item-price) or a conversion-based pricing policy.
- Whether fractional quantities are allowed.

Changing a conversion factor affects how transaction quantity translates into stock quantity. Test it before use.

## Add an alternative UOM to an Item

1. Open the [Item](/erpnext/item).
2. Confirm the Stock UOM.
3. In the **UOMs** table, add the selling UOM.
4. Enter the Conversion Factor relative to one Stock UOM.
5. Save.

![The UOM conversion table on an Item.](https://novacompanies.m.frappe.cloud/files/selling-uom-item-conversion.png)

Example: if one Carton contains 10 Units and Unit is the Stock UOM, set the Carton conversion factor to 10.

## Create UOM-specific prices

Create one Item Price for each deliberately priced UOM:

1. Open Item Price.
2. Select the Item and selling Price List.
3. Select the UOM.
4. Enter the Rate.
5. Save.

![Item Prices for an Item and Price List.](https://novacompanies.m.frappe.cloud/files/selling-uom-item-prices.png)

Use separate prices when a carton has a negotiated price rather than exactly ten times the unit price.

Alternatively, enable **Price Not UOM Dependent** on the [Price List](/erpnext/price-lists) when ERPNext should derive the alternate-UOM price using the conversion factor.

## Sell in an alternative UOM

1. Create a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice).
2. Add the Item.
3. Select the highlighted pencil icon to open the complete row editor.
4. Select the UOM.
5. Confirm the Conversion Factor, Quantity, Stock Qty, and Rate.
6. Save or submit.

![The Sales Order Items table where the transaction UOM is selected.](https://novacompanies.m.frappe.cloud/files/selling-uom-sales-order.png)

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## Understand transaction and stock quantities

If one Carton equals 10 Units:


| Transaction value | Result   |
| ----------------- | -------- |
| UOM               | Carton   |
| Qty               | 3        |
| Conversion Factor | 10       |
| Stock Qty         | 30 Units |


Inventory reports and stock ledgers use the Stock UOM. The sales document can display the selected selling UOM.

## Fractional quantities

Use fractional quantities only when the UOM and Item allow them. For example, a service can be billed as 1.5 Hours, while a serialized laptop cannot usually be sold as 0.5 Unit.

Review UOM **Must be Whole Number** behavior and Item serialization or batching requirements.

## Troubleshooting


| Problem                                       | What to check                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| Alternative UOM is unavailable                | Add it to the Item's UOM table and save                                     |
| Stock Qty is incorrect                        | Correct the conversion factor                                               |
| No rate is fetched                            | Create an Item Price for the selected UOM or review Price Not UOM Dependent |
| Fractional quantity is rejected               | Check the UOM whole-number setting and Item constraints                     |
| Delivered stock differs from ordered quantity | Compare transaction Qty, UOM, Conversion Factor, and Stock Qty              |


## Frequently asked questions

### Can I keep stock in cartons and sell in units?

Yes. Choose the most appropriate Stock UOM and define the reciprocal business conversion accurately.

### Do I need a separate Item Price for every UOM?

Use separate Item Prices for deliberate UOM pricing. Use Price Not UOM Dependent for conversion-based pricing.

### Can the UOM change after submission?

Submitted stock and sales quantities should not be reinterpreted. Use the supported amendment or return workflow.

### Which quantity appears in the stock ledger?

Stock Qty in the Item's Stock UOM.

## Related topics

- [Unit of Measure](/erpnext/unit-of-measure-uom)
- [Item](/erpnext/item)
- [Item Price](/erpnext/item-price)
- [Price Lists](/erpnext/price-lists)
- [Sales Order](/erpnext/sales-order)
