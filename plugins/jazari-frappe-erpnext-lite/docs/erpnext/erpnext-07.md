<!-- Frappe documentation: erpnext, part 7 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__asset-reports.md -->
---
title: "Asset Reports | ERPNext Documentation"
description: "Use ERPNext Asset reports to reconcile depreciation, balances, fixed-asset registers, and lifecycle activity."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-reports"
updated: "2026-08-15"
---

Imagine the finance head at Nova Industries asks four questions before month-end: what assets do we own, how much depreciation was posted, what value remains, and which assets moved or changed during the month? One list cannot answer all four questions clearly.



ERPNext Asset Reports provide different views for different decisions. Together, the depreciation ledger, depreciation and balances report, fixed asset register, and asset activity report help the team reconcile values and investigate what happened.

## Choose the right report


| Field                                | What it means                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Asset Depreciation Ledger**        | Detailed depreciation schedule and posting history for each Asset and Finance Book.                                     |
| **Asset Depreciations and Balances** | Opening value, additions, depreciation, adjustments, and closing carrying value.                                        |
| **Fixed Asset Register**             | Operational and financial register with category, status, dates, values, cost center, department, vendor, and location. |
| **Asset Activity**                   | Lifecycle events such as purchase, movement, repair, value change, sale, or scrapping.                                  |


## Asset Depreciation Ledger

Use this report to investigate a schedule or reconcile posted and pending depreciation rows. Filter by company, date, Asset, category, or Finance Book.



The example below shows seven submitted monthly depreciation entries for Nova Industries' NovaPack labeler. The report makes it possible to trace each $760 expense to its depreciation Journal Entry and follow the accumulated balance.

[Screenshot on the live page: Loaded Asset Depreciation Ledger with seven posted entries]

## Asset Depreciations and Balances

Use it to explain how carrying value changed across a period. It is the strongest starting point for reconciling additions, depreciation, and closing value.

[Screenshot on the live page: Loaded Asset Depreciations and Balances report]

## Fixed Asset Register

Use it for the controlled asset listing and location or custodian review. The chart gives a quick acquisition view while the rows contain the audit detail.

[Screenshot on the live page: Loaded Fixed Asset Register with chart and asset rows]

## Asset Activity

Use this report when the question is "what happened to this asset?" Filter to the asset or period, then open linked documents to verify the event.



The example below contains real lifecycle events for Nova's laptops and production equipment, including creation, location receipt, submission, and a repair event.

[Screenshot on the live page: Asset Activity with real lifecycle transactions]

## Read a report safely

1. Select the company and Finance Book explicitly.
2. Set a period that matches the reconciliation.
3. Check whether the report includes default Finance Book assets.
4. Wait for the rows and charts to finish loading.
5. Drill into source documents for material or unexpected values.
6. Export only after the filters and totals are verified.

## Troubleshooting

### The report is empty

Check company, date range, Asset status, Finance Book, and whether depreciation or lifecycle transactions exist in the period.

### Two reports show different totals

Confirm they answer the same question and use identical company, date, Finance Book, and status filters.

### A row shows zero depreciation

Open the Asset Depreciation Schedule and verify that entries have been posted for the selected period.

## Frequently asked questions

### Which report should I give an auditor?

The Fixed Asset Register is a common starting point, supported by depreciation and ledger reports plus source documents.

### Where do I check a single Asset's full history?

Use Asset Activity, then open the linked Asset and transactions.

### Can reports compare Finance Books?

Run or filter the report for each Finance Book so the basis remains explicit and totals are not mixed.

### Why does the chart not match a filtered export?

Refresh after applying filters and ensure the chart and data table finished loading before export.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-shift-allocation.md -->
---
title: "Asset Shift Allocation | ERPNext Documentation"
description: "Allocate ERPNext asset depreciation by machine shifts when utilization changes across periods."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-shift-allocation"
updated: "2026-08-15"
---

Imagine a Nova Industries packaging machine runs one shift in January, three shifts in February, and two shifts in March. If the machine works harder in February, equal depreciation every month may not match how quickly the machine is being used up.



Asset Shift Allocation records the shifts worked during each period. ERPNext uses those allocations with shift-based depreciation so heavier use can produce more depreciation and lighter use can produce less.

## Before you begin

Enable **Shift Based** in the Asset's Finance Book row and confirm the configured shift factors follow the approved accounting policy.

[Screenshot on the live page: Asset Finance Book used for shift-based depreciation]

## Allocate a shift

1. Open **Asset Shift Allocation**.
2. Select the Asset and Finance Book.
3. Choose the shift and effective date range.
4. Save and submit the allocation.
5. Review the regenerated or affected schedule before depreciation is posted.

## Understand the result

The shift factor changes how much depreciation is assigned to the relevant period. It does not change the acquisition cost. The total schedule must still respect the residual value.

[Screenshot on the live page: Report used to verify depreciation after shift allocation]

## Troubleshooting

### The depreciation amount did not change

Confirm the Finance Book is shift based, the allocation covers the schedule date, and depreciation has not already been posted for that period.

### The asset is allocated to overlapping shifts

Correct the dates so only the intended shift applies to a given period.

## Frequently asked questions

### Should office laptops use shift allocation?

Usually no. It is most useful for production equipment whose usage is measured by shifts.

### Does a shift allocation create a ledger entry?

The allocation changes the depreciation basis. The ledger entry occurs when depreciation is posted.

### Can future shifts be planned?

In ERPNext, yes, but review them when operational schedules change.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-value-adjustment.md -->
---
title: "Asset Value Adjustment | ERPNext Documentation"
description: "Adjust an ERPNext Asset's carrying value for a selected Finance Book and verify the resulting accounting entry."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-value-adjustment"
updated: "2026-08-15"
---

Imagine an independent valuation shows that a Nova Industries machine is worth $8,000 less than its current book value. If the accountant changes the value only in a spreadsheet, the Asset record and General Ledger will no longer agree.



Asset Value Adjustment records the new value on a specific date and posts the accounting effect through the configured accounts. This keeps the revised carrying value, future depreciation, and ledger history connected.

## Before you begin

Obtain an approved valuation, confirm the effective date, select the correct [Finance Book](https://docs.frappe.io/erpnext/using-finance-book-for-asset-depreciation), and identify the difference account and cost center.

## Create the adjustment

1. Select the Asset and date.
2. Select the Finance Book when the change applies to one reporting basis.
3. Review the Current Asset Value.
4. Enter the New Asset Value.
5. Select the Difference Account and cost center.
6. Submit and open the linked Journal Entry.

[Screenshot on the live page: Asset Value Adjustment from 36000 to 39000]

## Verify the result

Confirm the Asset's carrying value and future depreciation schedule changed only for the intended Finance Book. Use Asset Depreciations and Balances to reconcile the result.

[Screenshot on the live page: Asset report used to verify an adjusted value]

## Troubleshooting

### Current value is not what the valuation expected

Check the Finance Book, effective date, booked depreciation, and earlier value adjustments.

### The difference posts to the wrong account

Cancel or reverse according to policy, then correct the category or selected Difference Account before reposting.

## Frequently asked questions

### Is this the same as depreciation?

In ERPNext, no. Depreciation follows a schedule; value adjustment records a separate approved change in carrying value.

### Can I adjust only one Finance Book?

In ERPNext, yes. Select it explicitly and verify reports using the same filter.

### Does the adjustment create a Journal Entry?

A submitted adjustment creates or links the accounting entry for the difference.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset.md -->
---
title: "Asset | ERPNext Documentation"
description: "Create and manage an ERPNext Asset record, including value, location, ownership, depreciation, insurance, and lifecycle status."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset"
updated: "2026-08-15"
---

An Asset record is the operating history of something the company uses. For Nova Industries' staff laptop, it connects the Item and purchase value to a current location, maintenance plan, depreciation schedule, and eventual disposal.



Create one only after deciding whether the item is company equipment rather than inventory held for sale.

## Before you begin

Prepare the fixed-asset Item, [Asset Category](https://docs.frappe.io/erpnext/asset-category), company accounts, and [Asset Location](https://docs.frappe.io/erpnext/asset-location). Use [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset) when the record originates from a new purchase.

## Create an Asset

1. Open **Asset** and select **Add Asset**.
2. Select the Item and company.
3. Enter a recognizable Asset Name and current Location.
4. Select **Existing Asset** only when bringing an already-owned asset into ERPNext. Use **Composite Asset** when the asset is assembled by capitalization.
5. Enter purchase and available-for-use dates, value, and quantity.
6. Enable maintenance and depreciation only when they apply.

[Screenshot on the live page: Core ERPNext Asset fields for a Nova Industries laptop]

## Important fields and what they mean


| Field                                | What it means                                                             |
| ------------------------------------ | ------------------------------------------------------------------------- |
| **Item Code**                        | The reusable Item definition for this asset model.                        |
| **Asset Name**                       | The human-readable identity, such as an internal tag or serial reference. |
| **Location**                         | Current physical position.                                                |
| **Asset Type**                       | Existing, Composite Asset, or Composite Component.                        |
| **Purchase Date**                    | Date the company acquired the asset.                                      |
| **Available for Use Date**           | Date capitalization and depreciation can begin.                           |
| **Net Purchase Amount**              | Capitalized acquisition value before later adjustments.                   |
| **Maintenance Required**             | Allows maintenance planning and logs.                                     |
| **Calculate Depreciation**           | Creates depreciation schedules from Finance Book settings.                |
| **Opening Accumulated Depreciation** | Depreciation already booked before migration to ERPNext.                  |
| **Custodian and Department**         | Operational responsibility and reporting ownership.                       |


## Review depreciation

Each Finance Book may have a different method, useful life, residual value, and posting frequency.

[Screenshot on the live page: Finance Book configuration on an ERPNext Asset]

## Status and downstream actions


| Field                              | What it means                                                  |
| ---------------------------------- | -------------------------------------------------------------- |
| **Submitted**                      | The asset is active in the register.                           |
| **Partially Depreciated**          | At least one depreciation is booked and value remains.         |
| **Fully Depreciated**              | The scheduled depreciable value has been booked.               |
| **In Maintenance or Out of Order** | Operational condition is restricted.                           |
| **Sold**                           | A disposal sale has completed.                                 |
| **Scrapped**                       | The asset was written off through the scrap workflow.          |
| **Capitalized**                    | The asset was created or updated through Asset Capitalization. |


[Screenshot on the live page: Asset statuses in the ERPNext list view]

## Troubleshooting

### The Asset value or account is wrong

Trace the source purchase, category account defaults, and any capitalization or value-adjustment entries. Do not correct only the visible total without understanding the ledger source.

### The Asset cannot be cancelled

Cancel or reverse linked submitted depreciation and disposal documents in the required order first.

## Frequently asked questions

### Can I change the location directly?

Use Asset Movement for a controlled transfer and an auditable history.

### Can I store insurance information?

In ERPNext, yes. Use the insurance fields for insurer, policy dates, insured value, and coverage details.

### Can one Asset contain multiple units?

Grouped assets support quantity-based use cases, but individual assets are clearer when each unit needs its own custodian, maintenance, or disposal history.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__assets__introduction.md -->
---
title: "Overview | ERPNext Documentation"
description: "Understand the ERPNext Assets lifecycle, from purchase and capitalization through depreciation, maintenance, transfer, sale, or scrapping."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assets/introduction"
updated: "2026-08-15"
---

Imagine you are helping the accounts team at Nova Industries, an electronics manufacturing and distribution company. The company buys phones to sell, laptops for employees, and machines for its packaging floor. The phones are inventory because customers will buy them. The laptops and machines are assets because Nova Industries will use them for several years.



The ERPNext Assets module keeps the complete story of those assets in one place. It records what the company owns, where each asset is, who uses it, how its value reduces over time, what it costs to maintain, and whether it is eventually sold or scrapped.

## Understand the asset lifecycle

1. Define an [Asset Category](https://docs.frappe.io/erpnext/asset-category) with the correct asset, accumulated depreciation, expense, and capital work in progress accounts.
2. Organize physical places in the [Asset Location](https://docs.frappe.io/erpnext/asset-location) tree.
3. Mark an Item as a fixed asset, then buy it or create an existing Asset record.
4. Place the asset in service and review its depreciation schedule.
5. Record assignment, [movement](https://docs.frappe.io/erpnext/asset-movement), [maintenance](https://docs.frappe.io/erpnext/asset-maintenance), [repair](https://docs.frappe.io/erpnext/asset-repair), and value adjustments during its life.
6. Finish the lifecycle by [selling](https://docs.frappe.io/erpnext/selling-an-asset) or [scrapping](https://docs.frappe.io/erpnext/scrapping-an-asset) the asset.

[Screenshot on the live page: ERPNext Asset list for Nova Industries showing laptops and production equipment]

## What the module records


| Field                | What it means                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Identity**         | Item, asset name, category, company, owner, and status.                                                                |
| **Physical control** | Current location, custodian, department, transfers, issues, and receipts.                                              |
| **Accounting**       | Purchase value, capitalization, Finance Books, depreciation schedules, accumulated depreciation, and disposal entries. |
| **Operations**       | Preventive maintenance plans, maintenance logs, failures, repairs, downtime, and repair cost.                          |
| **Lifecycle result** | Whether the asset remains in use, is out of order, has been sold, or has been scrapped.                                |


## Stock item versus fixed asset

Use a stock item when the company intends to sell or consume the item. Use a fixed-asset Item when the company will use the item to run the business for more than one accounting period. The same laptop model can therefore be inventory in an electronics store and a fixed asset when issued to the store manager.

## Accounting impact at a glance

An Asset record by itself is the operational register. Accounting entries arise from submitted acquisition, depreciation, value adjustment, capitalization, sale, or scrap transactions. Locations and maintenance logs change the operational history but do not normally post to the General Ledger.

## Frequently asked questions

### Can ERPNext manage non-depreciable assets?

In ERPNext, yes. Enable **Non Depreciable Category** when an asset category should not create depreciation schedules.

### Can one asset have different depreciation schedules?

In ERPNext, yes. Finance Books can maintain different methods or useful lives for statutory and management reporting.

### Does moving an asset create a ledger entry?

In ERPNext, no. Asset Movement changes custody or location. It does not change the asset's accounting value.

### Where can I see the complete asset register?

Use the [Fixed Asset Register](https://docs.frappe.io/erpnext/asset-reports) and related Asset reports.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__assignment-rule.md -->
---
title: "Assignment Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assignment-rule"
updated: "2026-03-02"
---


> Introduced in Version 12

**An Assignment Rule lets you set up automatic assignment of documents to Users.**

To assign the support tickets automatically amongst the employees who work on support, an Assignment Rule can be used.

To access Assignment Rule, go to:
> Home > Settings > Assignment Rule

## 1. How to create an Assignment Rule
To set up an automatic assignment:

1. Go to the Assignment Rule list, click on New.
1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do.
1. Select the condition for the assignment.
 You can write simple Python expressions for automatic assignment in the `Assign Rule`, `Close Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, ==, etc and also multiple conditions like `and` and `or`.

 Examples:

 - `status == "Open"`
 - `issue_type == "Technical" and priority=="High" and status == "Open"`

1. Select the assignment rule.

 [Screenshot on the live page: Assignment Rule]

 * **Round Robin**: Assign each document to a User in sequence.
 * **Load Balancing**: Assign new documents to the User who has the least number of assignments.

 Select the list of Users to whom this Assignment Rule will apply:
 [Screenshot on the live page: Users in Assignment Rule]

 * **Based on Field**: Introduced in v13, this rule can be used to assign a document to the User that is set in the configured field.

 Select the User link field which will determine to whom this Assignment Rule will apply:
 [Screenshot on the live page: Field Assign]


1. Save.

You can use properties of the document in the Description field that will be part of the assignment. Higher 'Priority' Assignment Rules will be applied first.

Example:

High Priority Issue *File Upload not working* has been assigned to you.

### 1.1 Multiple Assignment Rules

You can also set up multiple auto assignments for each Document Type, the one with the highest Priority will be applied first.

[Screenshot on the live page: Assignment Rule with Higher Priority]


assignment-rule-with-higher-priority

### 1.2 Setting Due Date for assignment

You can auto set due dates for assignments based on the date field in the reference document.

Example:

If you want to set a due date on Issue assignment based on the "Resolution By" date of the Issue, you can do so by selecting "Resolution By" field in `Due Date Based On` option in Assignment Rule.

[Screenshot on the live page: Due Date Based On]

**Note:**

- "Due Date Based On" option will not be available if "Document Type" is not yet selected or if the selected Document Type does not have any "Date" or "Datetime" field.
- Due Date in the assignment/ToDo will be updated whenever the "Due Date Based On" field value is updated in the reference document.

### 2. Related Topics

1. [Workflows](/erpnext/workflows)
1. [Workflow Actions](/erpnext/workflow-actions)

<!-- page: erpnext/erpnext__assistance-sales-purchase-between-companies.md -->
---
title: "Create a Sales Invoice without an Item Code | ERPNext Documentation"
description: "Create ERPNext Sales Invoices and Credit Notes for one-time charges without an Item Code by completing the required child-row fields."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/assistance-sales-purchase-between-companies"
updated: "2026-07-25"
---

Use inter-company drop shipping when one Company sells to a Customer while goods are supplied directly by another Company in the same ERPNext site. This combines the [Drop Ship](/erpnext/drop-shipping-in-erpnext) workflow with inter-company Customer and Supplier relationships.

## Before you begin

Create or confirm:

- Both [Companies](/erpnext/company) in the same site.
- An internal Customer representing the supplying Company.
- An internal Supplier representing the selling Company.
- **Represents Company** and internal-party settings on both masters.
- Items, Warehouses, Price Lists, taxes, and inter-company accounts.
- Permissions for both Companies.

Review [Inter Company Invoices](/erpnext/inter-company-invoices) before using the workflow. Each Company remains a separate accounting entity.

## Configure internal parties

1. Create a Customer for the Company that buys internally.
2. Enable **Is Internal Customer** and select **Represents Company**.
3. Create the reciprocal Supplier.
4. Enable **Is Internal Supplier** and select the represented Company.
5. Save both records.

[Screenshot on the live page]

## Create the customer Sales Order

1. In the selling Company, create a [Sales Order](/erpnext/sales-order) for the external Customer.
2. Add the Items.
3. Select the highlighted pencil icon to open the Item row.
4. Enable **Drop Ship** for the row.
5. Select the Supplier that represents the supplying subsidiary.
6. Save and submit.

[Screenshot on the live page: A Sales Order Item with Supplier delivers to Customer and the subsidiary Supplier highlighted.]

In a drop-ship flow, stock availability in the selling Company's Warehouse does not replace Supplier fulfilment planning.

## Create the Purchase Order

From the submitted Sales Order:

1. Select **Create > Purchase Order**.
2. Choose the internal Supplier.
3. Review the mapped external Customer delivery address and Items.
4. Confirm the buying Company, schedule dates, rates, taxes, and terms.
5. Save and submit.

[Screenshot on the live page: A Purchase Order created for an internal Supplier with the Customer delivery address.]

The Purchase Order instructs the supplying subsidiary to deliver directly to the external Customer.

## Complete the inter-company documents

Create the corresponding internal sales and purchase invoices according to your [inter-company transaction](/erpnext/inter-company-invoices) process. Then invoice the external Customer from the selling Company.

Keep these relationships clear:


| Relationship                               | Document                  |
| ------------------------------------------ | ------------------------- |
| External Customer owes selling Company     | External Sales Invoice    |
| Selling Company owes supplying subsidiary  | Internal Purchase Invoice |
| Supplying subsidiary bills selling Company | Internal Sales Invoice    |


Tax and transfer-pricing requirements vary by jurisdiction. Configure them with qualified accounting advice.

## Troubleshooting


| Problem                                | What to check                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------- |
| Internal Supplier cannot be selected   | Confirm Is Internal Supplier, Represents Company, permissions, and disabled status            |
| Purchase Order uses the wrong Company  | Review the internal party relationship and mapped Company                                     |
| Customer address is missing            | Confirm the Sales Order shipping address and drop-ship row                                    |
| Inter-company invoice is not generated | Review reciprocal Customer and Supplier masters and inter-company settings                    |
| Stock is moved in the selling Company  | Confirm that the Item row uses Drop Ship and that no Delivery Note was created for that stock |


## Frequently asked questions

### Does the selling Company receive the goods?

No. In the intended drop-ship flow, the Supplier delivers directly to the external Customer.

### Are inter-company invoices still required?

Yes. The Companies remain separate accounting entities even though they share an ERPNext site.

### Can only selected lines be drop shipped?

Yes. Configure Drop Ship at the Item-row level and plan the remaining lines through the normal warehouse flow.

### Does ERPNext determine legal transfer prices?

No. Configure internal rates and taxes according to your organization's policy and applicable law.

## Related topics

- [Drop Ship](/erpnext/drop-shipping-in-erpnext)
- [Inter Company Invoices](/erpnext/inter-company-invoices)
- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)
- [Company](/erpnext/company)

<!-- page: erpnext/erpnext__authorization-rule.md -->
---
title: "Authorization Rule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/authorization-rule"
updated: "2026-03-02"
---


**Authorization Rule allows configuring a custom authorization / approval on a documents, based on conditions defined.**

Example: If a Sales Order's Grand Total exceeds $1,000, then it should be verified/submitted by the Sales Manager only, even if the Sales User has "Submit" permission.

On the same lines, you can define Authorization Rule based on the fields like Net Total, Grand Total, Discount % and specify who would be the document approver if the authorization condition is matched.

[Screenshot on the live page: Authorization Rule]

Let's consider a detailed example of an Authorization Rule to learn better.

Assume that the Sales Manager needs to authorize Sales Orders, only if it's Grand Total value exceeds 10,000. If the Sales Order value is less than 10,000, then even the Sales User will be able to submit it. This means that the Submit permission of Sales User will be restricted only up to Sales Order of Grand Total less than 10,000.

## 1. How to create an Authorization Rule

1. Go to the Authorization Rule list, click on New.
1. Select the transaction on which Authorization Rule will be applicable. This functionality is available for limited transactions only.
1. Enter the Authorized Value, etc. This depends on the field you selected in Based On.
1. Select Based On. Authorization Rule will be applied based on the value selected in this field.
1. Select Applicable Role. This is the role on which this Authorization Rule will be applicable. As per the example, it'll be Sales User.
1. To be more specific, you can also select Applicable To User if you wish to apply the rule to a specific Sales User, and not to all Sales Users.
1. Select Approving Role. This is the role that can approve forms over the Authorized value. As per our example, it is the Sales Manager.
1. You can also select a specific Sales Manager.
1. Save.

[Screenshot on the live page: Authorization Rule]

If the Sales User tries submitting the Sales Order of value higher than 10,000, then he will get an error message.

[Screenshot on the live page: Authorization Rule Validation Message]

> If you wish to restrict Sales User from submitting Sales Orders, then instead of creating Authorization Rule, you should remove submit privilege for Sales User from [Role Permission Manager](/erpnext/role-based-permissions).

### Documents on which Authorization Rule can be applied

1. Sales Order
1. Purchase Order
1. Quotation
1. Delivery Note
1. Sales Invoice
1. Purchase Invoice
1. Purchase Receipt
1. Appraisal

### Fields on which Authorization Condition can be based on

1. Grand Total
1. Average Discount
1. Customer-wise Discount
1. Item-wise Discount

<!-- page: erpnext/erpnext__auto-creation-of-material-request.md -->
---
title: "Auto Creation of Material Request"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-creation-of-material-request"
updated: "2026-02-27"
---

  


To prevent stockouts, you can track item's reorder level. When stock level goes below reorder level, purchase manager is notified and instructed to initiate purchase process for the item.

In ERPNext, you can update item's Reorder Level and Reorder Qty in the Item master. If same item has different reorder level, you can also update warehouse-wise reorder level and reorder qty.

[Screenshot on the live page: reorder level]  


With reorder level, you can also define what should be the next action. Either new purchase or transfer from another warehouse. Based on setting in Item master, purpose will be updated in the Material Request as well.

[Screenshot on the live page: reorder level next action]  


When item's stock reaches reorder level, Material Request is auto-created automatically. You can enable this feature from:

`Stock > Setup > Stock Settings`

[Screenshot on the live page: active auto-material request]  


A separate Material Request will be created for each item. User with Purchase Manager's role will receive email alert about these Material Requests.

If auto creation of Material Request is failed, User with Purchase Manager role will be informed about error message. One of the most encountered error message is:

**An error occurred for certain Items while creating Material Requests based on Re-order level.** **Date 01-04-2016 not in any Fiscal Year.**

One of the reason of error could be Fiscal Year as well. Click [here](/erpnext/fiscal-year-error.html) to learn more about it.

### Note:

The system creates a material request by comparing the projected quantity of the group warehouse with the reorder level. If the group warehouse is not set, then the system compares the projected quantity of the Request for Warehouse with the reorder level. If the projected qty is more than the reorder level then system doesn’t add that item in the material request.

<!-- page: erpnext/erpnext__auto-email-reports.md -->
---
title: "Auto Email Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-email-reports"
updated: "2026-03-02"
---

**Auto Email Reports automatically sends reports for the selected document.**

You can setup **Auto Email Report** to send reports at regular intervals. These must be saved reports of any type (Report Builder, Script or Query Report).

You can find Auto Email Report at:

> Home > Settings > Auto Email Report

1. How to create an Auto Email Report
-------------------------------------

1. Go to the Auto Email Report list, click on New.
2. Select the Report for which you want to generate emails.
3. Select the user for which you want to create this report (permissions will apply for this user).
4. Set the Email Addresses to which you want this report to be emailed and the frequency of the report. Emails will be sent at midnight. The date will be repeated in case of weekly/monthly/yearly frequency.

[Screenshot on the live page: With Filters]
5. Save.

You can test the report by clicking on "Download" or "Send Now". Here is an example of the email you will receive for a general ledger report:

[Screenshot on the live page: Report by Email]  


2. Features
-----------

### 2.1 Filter Data

* **Send only if there is any data**: If enabled, emails will not be sent if there is no data in the report.
* **Only Send Records Updated in Last X Hours**: If set to 24, an email will contain only records updated in the last 24 hours.
* **No of Rows**: The number of rows to be sent in the email. The maximum is 500.

### 2.2 Report Filters

If your report has filters, you will be able to see them. Click on the table to edit it:

[Screenshot on the live page: Edit Filters]  


For example, if the email is on the report 'Project Billing Summary' select the Project. The date range here is the date range of the 'Project Billing Summary'.

### 2.3 Message

A message can also be added to be sent with the email report. For example, 'This is your monthly Project Billing Summary Report:'

You can also change the file format in which the report is created. The available options are HTML, XLSX, and CSV.

### 2. Related Topics

1. [Email Digest](/erpnext/email-digest)
2. [Document Follow](/erpnext/document-follow)

<!-- page: erpnext/erpnext__auto-repeat-recurring-orders-and-invoices.md -->
---
title: "Auto Repeat Recurring Orders and Invoices | ERPNext Documentation"
description: "Schedule ERPNext to create recurring orders, invoices, journals, and other enabled documents from a reference transaction."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-repeat-recurring-orders-and-invoices"
updated: "2026-08-14"
---

Nova Industries bills Northstar Retail, a customer with a monthly device-support contract, on the first day of every month. Recreating the same Sales Invoice by hand risks missed billing and inconsistent terms. Auto Repeat uses an approved source document as a template and creates new orders or invoices on a schedule.



Use Auto Repeat for stable recurring transactions. Use [Subscription](/erpnext/subscription) when the agreement is plan-driven and needs subscription dates, plan quantities, trials, or subscription lifecycle controls.

## Before you begin

- Review the source party, company, items, rates, taxes, payment terms, dimensions, and addresses.
- Decide whether generated documents should stay in Draft for review or submit automatically.
- Confirm who should receive email and which print format should be attached.

## Create the Auto Repeat

1. Open **Auto Repeat** and create a new record.
2. Select the Reference Document Type and the exact order or invoice to repeat.
3. Set the start date and, when the agreement ends, an end date.
4. Enable Submit on Creation only when the generated transaction needs no manual review.

[Screenshot on the live page: Auto Repeat reference document and creation settings]



## Set the schedule

Choose the frequency and the relevant schedule options. For monthly billing, set the expected day or use the last day of the month when that matches the contract.

[Screenshot on the live page: Auto Repeat schedule for a recurring invoice]



## Monitor generated documents

Review the next scheduled date and the generated documents. Prices, taxes, addresses, and contract terms can change after the source was approved, so keep a review owner even when creation is automated.

## Troubleshooting

### No document was generated

Check that Auto Repeat is enabled, the start and end dates include today, the schedule is complete, the reference document is valid, and background jobs are running.

### The generated document has old commercial terms

Update the reference document or create a new approved source and point Auto Repeat to it. Do not assume changes in related masters will safely update every copied field.

## Frequently asked questions

### Can it repeat both orders and invoices?

Use supported Sales Orders, Purchase Orders, Sales Invoices, and Purchase Invoices as reference documents. Verify the current DocType’s Auto Repeat support before relying on it.

### Should I enable automatic submission?

Use it only for stable, low-risk transactions with tested taxes and controls. Draft creation is safer when a person must review each cycle.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__auto-repeat.md -->
---
title: "Auto Repeat\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/auto-repeat"
updated: "2026-03-02"
---


Auto Repeat feature helps you create certain documents automatically in a given time period.

From version 12, you can Customize any Form to make the documents **repeatable**.

For Example: Assuming that you follow deferred expense system for some items. It requires you to create same Journal Entry every month to credit Deferred Expense account and debit Expense Account. You can create first Journal Entry manually for it, and then create auto-repeat transaction for it.

To access Auto Repeat, go to:
> Home > Settings > Automation > Auto Repeat

## 1. How to set up Auto Repeat

### 1.1 Customize the Form
1. Go to: **Home > Customization > Form Customization > Customize Form**.
2. Select the form in which you want to allow creation of repeatable documents.
3. Check 'Allow Auto Repeat' to allow the creation of repeatable documents for that Form. This is necessary for the document type to show up in the Reference Document field under the Auto Repeat doctype.

 [Screenshot on the live page: Allow Auto Repeat]

### 1.2 Set up Auto Repeat
1. Go to **Home > Settings > Automation > Auto Repeat > New**.
2. Select the Reference Document Type, like Journal Entry or Sales Invoice, etc.
3. Select the Reference Document. This is the individual document that you want to repeat.
4. Set the Start Date and End Date (optional).
 If End Date is not specified, recurring documents will be created, unless the Auto Repeat is disabled.
5. Set the Frequency for creating repeatable documents
 (Daily, Weekly, Monthly, Quarterly, Half-yearly, Yearly).
6. Save.

### 1.3 Set up Auto Repeat directly from the document
You can also set a document on Auto Repeat by clicking the **Repeat** option from the **Menu** in the Toolbar.

**Note**: If a document is already on Auto Repeat, the Repeat option is not available.

[Screenshot on the live page: Repeat in Transactions]

Once you click on Repeat, a prompt for Auto Repeat will show up. Fill in the details and click on Save.

[Screenshot on the live page: Auto Repeat Prompt]

## 2. Features


### 2.1 Submit on Creation

If the reference document type is submittable, you get an option called _Submit on Creation_. If this is checked, your document will be submitted on creation.

[Screenshot on the live page: Auto Repeat Submit on Creation]

### 2.2 Notify by Email
If you want to notify certain contacts whenever the recurring documents are created, you can check 'Notify by Email' in the Notification section of Auto Repeat. This will send the auto-generated recurring documents to the specified Email Addresses. Fields for the same are explained below:

- **Recipients**: Defines the Email IDs of the recipients for recurring document creation emails.
- **Get Contacts**: This button will fetch the contacts linked to the document that is set on Auto Repeat and fill up the Recipients field with the same.
- **Template**: You can choose an Email Template for the email. This will fill up the Subject and Message fields as well.
- **Subject**: Subject for your Email (example: Recurring ToDo created successfully).
- **Message**: Message to be sent in the Email.
- **Preview Message**: This button will show a preview of the message.
- **Print Format**: Select a print format to define document view which should be emailed to customer.

> **Note**: If the document you are setting up Auto Repeat for, is submittable, ensure that "Allow Print for Draft" is enabled in [Print Settings](/erpnext/print-settings) to receive the new recurring document in Auto Repeat Notification Email. If this is not enabled, you will be notified about the recurring document creation without the document.

### 2.3 Repeat on a particular day
If the frequency is set as Monthly, Quarterly, Half-yearly or Yearly, then it will create recurring documents in the respective months on the same day as the 'Start Date' of Auto Repeat. If you want to create recurring documents on some other day then you can set one of the following:

- **Repeat on Day**: Day of the month on which recurring document will be created. For example, if frequency is Monthly and you enter 7 then it will generate recurring document on 7th of the respective month.
- **Repeat on Last Day of the Month**: This option is available as the last day of every month is different. For example, in a leap year last day of Feb is 29th, and it is 28th otherwise. If you check this option, it will create recurring documents on the last day of the respective months.

### 2.4 Ability to select weekdays for Auto Repeat

> Introduced in version 13

Auto Repeat with Weekly frequency allows you to select the days on which you want the recurring documents to be created.

[Screenshot on the live page: Auto Repeat Weekdays]

### 2.5 Dashboard

You can see the Auto Repeat schedule in the Dashboard of Auto Repeat document. If you don't specify the End Date then the schedule will show only the Next Schedule Date.

[Screenshot on the live page: Auto Repeat Dashboard]

### 2.6 Auto Repeat Frequency on the sidebar
When a document is set on Auto Repeat you can see the Auto Repeat frequency on the sidebar.
You can click on the status to see the linked Auto Repeat document.

[Screenshot on the live page: Auto Repeat Frequency]

### 2.7 Disable Auto Repeat
If you check this field it will stop creating recurring documents and unlink the Auto Repeat document from the Reference Document.

<!-- page: erpnext/erpnext__automate_lead_capturing.md -->
---
title: "Automate Lead Creation | ERPNext Documentation"
description: "Learn how ERPNext can create Leads from email, Web Forms, ecommerce activity, and data imports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automate_lead_capturing"
updated: "2026-07-23"
---

Leads come from many different sources. It is important that all leads are recorded, assigned to sales executives and followed up.

## Create Leads From Emails

You may have an email address like '[sales@yourcompany.com](mailto:sales@yourcompany.com)' which is probably displayed on your website. People may send emails asking information about your products and services. You can enable [Email Account](/erpnext/email-account) to pull these emails and create a lead for each email.

## Create Leads From Webforms

You can also map the Lead form to a [Web Form](/erpnext/web-form) and publish it on your website. When visitors of your website fill the form, it will be automatically added as a Lead.

## Create Leads From Incomplete Orders in E-Commerce Module

You can publish an e-commerce website and allow users to place an order for your products. If a user selects items but doesn't complete the process you can pursue that user as a lead.

## Create Leads By Importing Spreadsheet

If you have a spreadsheet with details of the leads, you can use the [Data Import](/erpnext/data-import) feature to import the leads.
