<!-- Frappe documentation: erpnext, part 45 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__production-plan-schedule.md -->
---
title: "Production Plan Schedule"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan-schedule"
updated: "2026-08-25"
---

The Production Plan Scheduler calculates realistic start and end dates for everything in your Production Plan - finished items, sub-assemblies, and even the purchase of raw materials - based on how much your machines can actually handle. Instead of typing dates in manually and hoping the shop floor can keep up, you get a schedule that respects machine capacity, working shifts, holidays, and work that is already booked.



[Screenshot on the live page]

---

## 1. Why use it

Without scheduling, a Production Plan only says *what* to make and *how much*. It cannot answer the questions a planner actually has:

- **When will this order be finished?**
- **Which machine will be busy, and when?**
- **Do we need to order material before we can start?**
- **Can we take on another order this week, or are the machines full?**

The scheduler answers all of these before a single Work Order is created - and when you do create Work Orders, they automatically follow the same dates.

---

## 2. What you need to set up first

You don't need all of this, the scheduler uses the best information available for each item. But the more you maintain, the more accurate your dates become.

### For machine-level scheduling (most accurate)


| Setup                    | Where         | What it does                                                                                                                                                                                                                     |
| ------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Working Hours**        | Workstation   | Your shifts, e.g. one row for 8 AM–4 PM and another for 4 PM–12 AM means the machine runs two shifts. Work is only scheduled inside these hours.                                                                                 |
| **Holiday List**         | Workstation   | Days the machine doesn't run. The schedule skips them.                                                                                                                                                                           |
| **Job Capacity**         | Workstation   | How many jobs can run on the machine at the same time. Capacity 2 = two job cards side by side.                                                                                                                                  |
| **Operations with time** | BOM           | Each operation's time in minutes, with either a specific **Workstation** or a **Workstation Type**.                                                                                                                              |
| **Workstation Type**     | BOM Operation | Leave the specific Workstation blank and set a type (e.g. "Molding"), the scheduler automatically picks whichever machine of that type is free first. With 2 molding machines of capacity 2, four jobs can run at the same time. |


### For items without BOM operations (day-level estimate)


| Setup                | Where           | What it does                                                                                               |
| -------------------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| **Capacity Per Day** | Item Lead Time  | How many units you can produce per day. 120 pcs at 60/day = 2 days.                                        |
| **Daily Yield %**    | Item Lead Time  | Reduces effective capacity (note: it defaults to 90%). Set 100 if you don't use yield.                     |
| **Buffer Time**      | Item Lead Time  | Extra safety days added to the duration.                                                                   |
| **No of Shifts**     | Production Plan | If your Item Lead Time capacity was recorded for 1 shift and this plan runs 2, the daily capacity doubles. |


### For raw materials


| Setup                           | Where          | What it does                                                                                      |
| ------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- |
| **Purchase Time + Buffer Time** | Item Lead Time | How many days it takes to procure the material. Production that consumes it cannot start earlier. |
| **Lead Time in Days**           | Item master    | Used as a fallback when there is no Item Lead Time record.                                        |


### Supplier Lead Time

[Screenshot on the live page]

Not every supplier delivers at the same speed - a local dealer may ship in 2 days while an importer needs 15. The Supplier Lead Times table lets the schedule reflect that difference:

- Each row is one supplier with its own purchase and buffer days. The same supplier cannot be added twice, and only one row can be the default.
- When you fetch materials in the Production Plan, each purchase row gets a **Supplier** filled in automatically - from the default Supplier Lead Times row, or from the item's **Default Supplier** (Item Defaults) if no lead-time default exists. You can change it per row before scheduling.
- The scheduler then uses **that supplier's** lead time. If the chosen supplier isn't in the table, it falls back to the default supplier's row, then to the item-level Purchase Time, and finally to the Item master's Lead Time in Days.

If an item has neither operations nor lead-time data, the scheduler assumes 1 day, so the schedule always completes, it just tells you less.

---

## 3. Creating a schedule

1. Submit your **Production Plan** as usual.
2. Click the **Schedule Items** button in the toolbar.
3. Pick a **Start Date** - the earliest moment any work may begin.
4. *(Optional)* Tick **Use Item Wise Start Dates** if different items should start on different dates. A small table appears where you can set a date per item; its sub-assemblies follow the same date.
5. Click **Preview**.

Nothing is saved at this point, the preview is a safe "what-if". You can close it, change the dates, and preview again as many times as you like.



[Screenshot on the live page]

### Reading the preview

- The list is a **tree**: finished items in bold, their sub-assemblies indented below them, and **Procurement** rows showing when purchased material will be available.
- **Start / End** show the calculated dates for each item.
- **Starts In** shows how soon each item begins **green** when it starts in more than a day, **orange** when it's less than a day away.
- The tiles at the top show the **Expected Completion** date, the **Total Duration**, and the number of items.
- If something could not be scheduled (for example, no machine can fit the work within the planning horizon), a red banner explains why, and the Apply button is hidden until the problem is fixed.

6. Click **Apply Schedule**. Now the dates are saved:
  - Every item row in the plan gets its **Planned Start / End Date**.
  - A **Production Plan Schedule** entry is created for every block of work, these are what you see on the calendar.

---

## 4. The Production Schedule calendar

Open it from the plan via **View → Production Schedule**, or from the new **Schedule** section in the plan's connections area. Each entry reads *Item · Activity* for example "Bicycle · Assembly", "Chain · Production", or "Front Wheel · Procurement". You can filter the calendar by **Production Plan**, **Workstation**, or **Item** filtering by workstation gives you that machine's day/week view, exactly like a booking calendar. A job that spans two shifts appears as two blocks, so shift handovers are visible at a glance.

[Screenshot on the live page]

---

## 5. What happens when you create Work Orders

When you create and submit Work Orders from a scheduled plan, the schedule flows with them:

- Each Work Order takes its **Planned Start Date** from the plan.
- The **Job Cards** created on submission are placed on the **same machines at the same times** as the plan's calendar the shop floor sees exactly what the planner promised.

### Re-scheduling rules

- **Before** Work Orders exist: re-run Schedule Items freely. Each Apply replaces the previous schedule completely.
- **After** Work Orders exist: the schedule is **locked**. The preview still works for what-if analysis, but it shows a banner explaining that orders already exist, and Apply is disabled because the job cards on the shop floor are already following the old dates. Cancel the Work Orders if you genuinely need to re-plan.

[Screenshot on the live page]

---

## 6. How the dates are calculated (in plain words)

For every item in the plan, the scheduler asks, in order:

1. **Does its BOM have operations?** Then each operation's time (multiplied by the quantity) is booked on a machine, inside its working hours, skipping holidays, waiting its turn if the machine is busy with other job cards, and leaving the standard gap between operations.
2. **No operations?** Then the Item Lead Time capacity is used: quantity ÷ capacity per day = number of days, plus buffer.
3. **Is it subcontracted or purchased?** Then it is a waiting period: purchase time + buffer days.

On top of that, three rules connect everything together:

- A **parent cannot start before its children finish** - the Bicycle waits for the Chain and the Wheel.
- **Production cannot start before its raw material arrives** - the procurement time pushes everything that depends on it.
- **A machine is never double-booked** beyond its Job Capacity, if two items need the same machine, the second one waits (or moves to another machine of the same type, if one exists).

The finish date you see on the preview is simply the end of the longest chain.

---

<!-- page: erpnext/erpnext__production-plan-visualizer.md -->
---
title: "Production Plan Visualizer"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan-visualizer"
updated: "2026-08-31"
---



[Screenshot on the live page]

## What is this feature?

A Production Plan tells you what you plan to make. After you submit it, the work is spread across several documents — Work Orders for items you make in-house, Purchase Orders for items you subcontract, and Material Requests for raw materials you need to buy.

To answer a simple question like *"Can I start building this today?"*, you normally have to open the plan, then open each Work Order, check each Material Request, and check the stock for every raw material. For a plan with a few finished goods, this can mean dozens of clicks, and it is easy to miss the one item that is holding everything up.

**The Production Plan Visualizer puts all this information on one screen.** It shows you, at a glance:

- How much of the plan has been produced.
- Whether the raw materials are available or something still needs to be ordered.
- Which Work Orders and Purchase Orders exist and which ones have not been created yet.
- When each job is scheduled on the shop floor.

Nothing on this screen changes your data. It is a **read-only view**, you can view the information, but you cannot accidentally edit anything.

## 2. When should you use it?

Use it when you want to quickly answer questions like:

- *Is this plan on track?*
- *What is stopping me from starting production?*
- *Have all the Work Orders been created, or did someone miss one?*
- *Which raw material is short?*
- *What is scheduled on which machine this week?*

It is most useful for **production planners, plant managers, and supervisors** who need to track a plan until completion. You do not need it if you only create a plan and hand it over.

## 3. How to open it

There are two ways.

**From a Production Plan (easiest):**

1. Open the Production Plan you want to view.
2. Click the **View** menu at the top right.
3. Click **Plan Visualizer**.

<!-- page: erpnext/erpnext__production-plan.md -->
---
title: "Production Plan"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-plan"
updated: "2026-02-27"
---

**A Production Plan helps in production and material planning for the Items planned for manufacturing. These production items can be committed via Sales Order (to Customers) or Material Requests (internally).**

Production Plan helps the user to plan production against multiple Sales Orders or the Material Requests. Also, it helps in Material Procurement planning for the raw material item, based on the quantity of finished products to be manufactured.

To access the Production Plan list, go to:

> Home > Manufacturing > Production > Production Plan

1. Prerequisites
----------------

Before creating and using a Production Plan, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Material Request](/erpnext/material-request)
* [Sales Order](/erpnext/sales-order)
* [Bill Of Materials](/erpnext/bill-of-materials)
* [Routing](/erpnext/routing)

2. How to Create a Production Plan
----------------------------------

As mentioned earlier, a Production Plan can be used for planning the manufacture of Items against Sales Orders or Material Requests.

The common steps are:

1. Go to the Production Plan list, click on New.
2. Select whether to get items from a [Sales Order](/erpnext/sales-order) or a [Material Request](/erpnext/material-request).

A Production Plan can also be created manually where you can select the Items to manufacture.

### 2.1 Production Against Sales Orders

1. Select option as Sales Order from the 'Get Items From' drop-down list. The system will show the filters, using that you can pull the Sales Orders for the production. You don't need to use all these filters if you have only a few Sales Orders in a particular time frame.

[Screenshot on the live page: Production Plan fetch items]
2. Click on Get Sales Orders to fetch sales orders based on the above filters.

[Screenshot on the live page: Sales Order Filters]
3. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched. [Screenshot on the live page: Get items for Production Plan]
4. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process.
5. If "Consolidate Items" is ticked and saved, items with the same BOM are combined into a single item with the combined total planned quantity. [Screenshot on the live page: Get items Combined for Production Plan]

### 2.2 Production Against Material Requests

1. Select option as Material Request from the Get Items From drop-down list. The system will show the filters, using that we can pull the Material Requests for the production.

[Screenshot on the live page: Material Request Filters]
2. Click on 'Get Material Request' to fetch material requests based on the above filters.

[Screenshot on the live page: Material Requests]
3. Click on Get Items for Work Order to fetch the items from the above material requests.

[Screenshot on the live page: Material Request Item]

### 2.3 Fetching Sub Assembly Items

Clicking on 'Get Sub Assembly Items' will fetch Sub Assembly Items from the BOM of the Finished Good Items, in the table above. [Screenshot on the live page: Get Sub Assembly Items]  


#### 2.3.1 Sub Assembly Items

User will get option to make In House (Work Order) / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type.

[Screenshot on the live page]


If user wants to make Material Request for their Sub-assembly items as well their Final Raw Materials then they have to select the Manufacturing Type as "Material Request" for Sub-assembly items and then they have to click on the button "Get Items for Purchase Only" to fetch Sub-assembly items in the Material Request Plan Item table.


[Screenshot on the live page]


#### 2.3.2 Combining Sub Assembly Items

If there are Finished Goods that share the same Sub Assembly Item, the Sub Assembly Items can be combined. The criteria for combination would be to have the same Item, Warehouse, BOM and Manufacturing Type.

[Screenshot on the live page: Combine Sub Assemby Items]  


In this way a common Work Order can be made to bulk create Sub Assemblies for various Finished Goods.

#### 2.3.3 Skip Available Sub Assembly Items or Skip Available Raw Materials



[Screenshot on the live page]


If users enable the checkbox 'Skip Available Sub-Assembly Items' or 'Skip Available Raw Materials', the system will consider the Projected Qty which is available in the bin to calculate the required quantity for sub-assembly items or raw materials. To understand this, consider the following case.

##### Example

To produce 1 qty of Item A, 1 qty of Item B (sub-assembly) is required, and to produce 1 qty of Item B, 1 qty of Item C is required.


* In the production plan, Item A has a quantity of 100 to produce.
* Against Item B already work order created for 20 qty which is not completed and 20 more qty available in the stock. Which meant total 40 qty is available in the Projected Qty
* Against Item C already purchase order created for 40 qty which is not completed and 20 more qty available in the stock. Which meant total 60 qty is available in the Projected Qty
* If Skip Available Sub Assembly Items enabled, while calculating the required qty for Item B
    * Reqd Qty = Required Qty (as per BOM) - [Projected Qty](https://docs.frappe.io/erpnext/user/manual/en/projected-quantity) (in BIN) 
    * Reqd Qty = 100 - 40
    * **Reqd Qty = 60**

* If Skip Available Raw Materials enabled, while calculating the required qty for Item C
    * Reqd Qty = Required Qty (as per BOM) - [Projected Qty](https://docs.frappe.io/erpnext/user/manual/en/projected-quantity) (in BIN)  
    * Reqd Qty = 100 - 60
    * **Reqd Qty = 40**

### 2.4 Planning for Material Requests

Clicking on the 'Get Items for Purchase Only' button will fetch the required raw material Items in the Material Request Plan table. For example, to manufacture 200 plastic canes, you need 100 raw plastic Nos but have only 20 in your Warehouse, then clicking this button will add a row with 80 in the Required Quantity column (make sure Skip Available Raw Materials is enabled).


[Screenshot on the live page]

If partial materials are available in a different warehouse and you want to perform a material transfer and create a purchase entry for the remaining quantity, use the "Get Items for Purchase / Transfer" button. Here, you need to specify the warehouse from which the transfer should be made. If you select the parent warehouse, the system will check stock availability in its child warehouses and suggest transferring materials from those child warehouses.


[Screenshot on the live page]


Use the following checkboxes to perform certain actions:

* **Include Non Stock Items**: To include non-stock items in the material request planning. i.e. Items for which 'Maintain Stock' checkbox is unticked. Refer the [Item page](/erpnext/item#12-options-when-creating-an-item) for more details.
* **Include Subcontracted Items**: To add subcontracted Item's raw materials if include exploded items is disabled.
* **Skip Available Raw Materials**: 
If enabled, the system will consider items with a shortfall in quantity.
Formula to calculate Required Qty:
Required Qty = BOM Required Qty – Projected Qty 

* Example: Item A has 50 qty in stock and 20 qty in a Material Request (with a pending Purchase Order). To complete production, 100 qty is required.

    * If the "Skip Available Raw Materials" checkbox is enabled, the system will calculate the required quantity as: 100 - (50 + 20) = 30
    
    * If the "Skip Available Raw Materials" checkbox is not enabled, the system will calculate the required quantity as: 100, ignoring the available stock or incoming quantities.

* **For Warehouse**: User can set the Warehouse for which they want to create the material request. When creating Stock Entries during the production process, the system will look for raw material stock in this Warehouse.

#### 2.4.1 Download Material Request Plan

[Screenshot on the live page]


On click of "Download Material Request Plan" button the User will get the Excel sheet with the raw materials that are needed to complete this Production Plan. User can select the Warehouse to check the available quantity in the respective Warehouse. On click of "Download Material Request Plan" a popup will open to select warehouses. If user wants to Run plan for multiple warehouses then they can select those warehouses in the Popup to download the plan in the excel sheet format. Excel sheet will look similar to:

[Screenshot on the live page: Material Request Plan]  


### 2.5 After Submitting

Once the Production Plan is submitted, the User gets an option to make Work Orders for the production items and Material Requests for the raw materials. Users can also set the Status as **Closed** in the Production Plan.

[Screenshot on the live page]


#### 2.5.1 Closing a Production Plan

There could be occurrences where a Production Plan is partially complete and is going to be discontinued. This could happen due to reasons such as:

* One of the items was independently produced outside the Production Plan.
* A change in plans occurred and pending items will not be produced.

In cases like these, Users can set the Production Plan status to **Closed**, so that no new Work Orders or Material Requests are created against it.

[Screenshot on the live page: Closing a Production Plan]  


The same can be **Re-opened**.

### 2.6 Making work order for the sub-assembly items

User will get option to make Work Order / Sub-contract Purchase Order / Material Request for Purchase against the Sub-assembly items using Manufacturing Type.


If user wants to make Work Order for sub-assembly items then select the Manufacturing Type as In House and submit it. After Submit you have to click on the button Create -> Work Order / Subcontract PO

[Screenshot on the live page]







3. Related Topics
-----------------

1. [Work Order](/erpnext/work-order)
2. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__production-planning-report.md -->
---
title: "Production Planning Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/production-planning-report"
updated: "2026-03-02"
---


To access the Production Planning Report, go to:

> Home > Manufacturing > Reports > Production Planning Report

[Screenshot on the live page: Task]

This report will help users plan the finished good as well as the raw materials against the Sales Order / Work Order / Material Request (with the request type as Manufactured) data. Mostly, in the case of make to order, this report helps you plan the production of the finished goods as well the raw materials.

Using this report user will get the information about the available finished goods as well as available raw materials that are required in the production process. The unavailable finished good or raw materials will be highlighted in the red color.

In this report system will allocate the available stock to the order based on the sorting. The **Order By** filter will be use to sort the orders based upon the Delivery Date, Order Amount.

For example, Bob works in the Furniture Manufacturing company. Their organization follows the make to order production planning. On Monday, Bob received the Sales Orders for tables and chairs from different customers. So Bob has checked the production planning report to check the availability of the raw materials and he found that either table or chair can be manufactured with the available raw materials. Bob used the 'based on' filter to know which Finished Good order's delivery date is earlier. He has found that he has to deliver the Table earlier so he has started working on it and his colleague has created the purchase order for raw materials which will be used to make chair.

Using the **Production Planning Report**, this report auto allocate the raw materials to the order once it's available in the respective warehouse.

<!-- page: erpnext/erpnext__profit-and-loss-report.md -->
---
title: "Profit and Loss Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/profit-and-loss-report"
updated: "2026-08-14"
---

Nova Industries recorded $363,200 of income and $253,760 of expenses in 2026. The business earned $109,440, but the owner wants to know where that profit came from and whether a particular product line, department, or period performed better than another.



The Profit and Loss Statement summarizes income minus expenses over a period. It answers whether the company earned a profit, which accounts produced it, and how results compare across periods or reporting dimensions. It does not show what the company owns and owes at one date, which belongs in the [Balance Sheet](/erpnext/balance-sheet), or explain when cash moved, which belongs in [Cash Flow](/erpnext/cash-flow).

## Before you begin

Submit the relevant [Sales Invoices](/erpnext/sales-invoice), [Purchase Invoices](/erpnext/purchase-invoice), stock transactions, payroll entries, depreciation, and approved [Journal Entries](/erpnext/journal-entry). Confirm that Income and Expense accounts use the correct root and report type in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Run the report

1. Open **Accounting** and select **Profit and Loss Statement**.
2. Select **Nova Industries**.
3. Choose Fiscal Year or Date Range and set the required period.
4. Select Yearly, Half-Yearly, Quarterly, or Monthly periodicity.
5. Apply Finance Book, Cost Center, Department, Project, or another [Accounting Dimension](/erpnext/accounting-dimensions) only when the question requires that slice.
6. Refresh and wait for the totals, chart, and account rows to load.

[Screenshot on the live page: Loaded Profit and Loss Statement for Nova Industries showing income, expenses and profit]

## Interpret the Nova Industries result


| Result        | Value    | Interpretation                                                      |
| ------------- | -------- | ------------------------------------------------------------------- |
| Total Income  | $363,200 | Revenue and other income recognized during the selected period.     |
| Total Expense | $253,760 | Cost of goods sold and other expenses recognized during the period. |
| Profit        | $109,440 | Income exceeds expenses by this amount for the selected scope.      |


The profit is approximately 30.1% of income. That ratio is useful only after confirming that all period expenses, stock costs, depreciation, accruals, and adjustments are posted. A positive profit also does not mean the same amount is available in the bank. Credit sales can increase profit before customers pay.

## Read the account hierarchy

Expand Income and Expense groups to see the accounts behind each total. Direct Income and Direct Expense usually describe core trading or service activity. Indirect Income and Indirect Expense normally contain supporting or non-core items. The exact meaning depends on how your organisation designed its accounts.



Select an account value to drill into the entries that produced it. The linked [General Ledger](/erpnext/general-ledger) should use the same Company, dates, Finance Book, and dimensions as the Profit and Loss Statement.

[Screenshot on the live page: General Ledger drill-down opened from a Profit and Loss account value]

## Understand the important filters


| Filter                                           | Effect                                                                                               |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Fiscal Year or Date Range                        | Defines which accounting period is included.                                                         |
| Periodicity                                      | Splits results into yearly, half-yearly, quarterly, or monthly columns.                              |
| Accumulated Values                               | Shows cumulative balances through each displayed period instead of each period in isolation.         |
| Finance Book                                     | Restricts entries to the selected accounting book, subject to the default-book option.               |
| Cost Center, Project, Department, and dimensions | Shows the profit result for a selected operational segment.                                          |
| Currency                                         | Changes presentation currency without changing the underlying ledger entries.                        |
| Report Template                                  | Applies a configured [Financial Report Template](/erpnext/financial-report-template) when available. |


## Profit and cash are different

The Profit and Loss Statement recognizes income and expenses according to accounting dates. [Accounts Receivable](/erpnext/accounts-receivable) may show that customers still owe part of the reported income, while [Accounts Payable](/erpnext/accounts-payable) may show unpaid supplier expenses. Use Cash Flow to explain how those outstanding balances affect actual cash movement.

## Troubleshooting

### The report is empty

Confirm that submitted transactions exist inside the selected period and Company. Remove Finance Book and dimension filters one at a time, then verify that the affected accounts use Income or Expense roots.

### Profit and General Ledger do not agree

Match Company, dates, Finance Book, dimensions, currency, and period-closing options. A drill-down that loses a dimension filter can show a broader ledger scope than the original report.

### A monthly result looks cumulative

Review the Accumulated Values setting. Enable it for year-to-date columns and disable it when each month should show only that month's activity.

### Previous-year income or expense appears

Review fiscal-year dates and [Period Closing Voucher](/erpnext/period-closing-voucher) status. Income and Expense accounts normally begin the new fiscal year without the previous year's operating balance.

## Frequently asked questions

### Can a profitable company have negative cash flow?

Credit sales can create income before customers pay, while inventory purchases and other cash outflows may occur earlier. Cash Flow explains the difference.

### Does changing a report filter alter accounting entries?

Filters change which entries are selected and how they are presented. They do not repost submitted transactions.

### Should tax appear as income or expense?

The answer depends on the tax type, recoverability, and account configuration. Review regional accounting rules and the accounts used by the source transactions.

### Can the report compare departments or product lines?

Cost Centers, Projects, and custom Accounting Dimensions can segment the result when those values were recorded consistently on transactions.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Balance Sheet](/erpnext/balance-sheet)
- [Cash Flow](/erpnext/cash-flow)
- [General Ledger](/erpnext/general-ledger)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Financial Report Template](/erpnext/financial-report-template)

<!-- page: erpnext/erpnext__proforma-invoice.md -->
---
title: "Proforma Invoice | ERPNext Documentation"
description: "Create and manage Proforma Invoices from Sales Orders in ERPNext, including quantity-based and amount-based advance documents."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/proforma-invoice"
updated: "2026-07-24"
---

A **Proforma Invoice** is a preliminary, non-binding invoice sent to a customer before the goods are delivered or the final (tax) invoice is raised. It is commonly used to request an advance payment, to support a letter of credit or customs paperwork, or to give the customer a formal statement of what an order will cost.

In ERPNext, a Proforma Invoice is raised against a **Sales Order**. It is a purely informational document: it does **not** post any accounting (General Ledger) or stock entries, does not affect the delivery or billing status of the Sales Order, and does not consume the ordered quantity. You can raise as many proformas against a Sales Order as you need.

To create a Proforma Invoice, you must first enable the feature, and then create it from a submitted Sales Order.

---

## Enable Proforma Invoice

The feature is off by default. To turn it on, go to:

> **Selling Settings > Transaction**

Select **Enable Proforma Invoice**.

You can optionally set a **Default Proforma Print Format** that will be pre-selected whenever a proforma is created.

[Screenshot on the live page]
*Enable Proforma Invoice*

### **Naming Series**

The naming series used for Proforma Invoices can be configured under:

> **Selling Settings > Document Naming > Proforma Invoice**

By default, proformas are named using the `PRO-.YYYY.-` series.

---

## Create a Proforma Invoice

Open a **submitted** Sales Order and click:

> **Create > Proforma Invoice**

A dialog opens where you configure the proforma.

[Screenshot on the live page]
*Proforma creation dialog*

The dialog has the following fields:

- **Series**: the naming series for this proforma.
- **Print Format** and **Letter Head**: control how the printed proforma looks. The default print format from Selling Settings is pre-selected; you can override it per proforma.
- **Based On**: whether you specify each line by **Quantity** or by **Amount** (see below).
- **Items**: the Sales Order lines. Each line is pre-filled with its **remaining** value (ordered minus what has already been proforma'd).

Enter the quantity or amount for the lines you want to include (set a line to `0` to leave it out), then click **Create**. The proforma is created, its PDF is generated and attached, and the **Proforma** tab of the Sales Order opens automatically.

### Based On: Quantity

This is the default. Enter the **Quantity** for each item; the amount is calculated automatically from the Sales Order rate (`Amount = Quantity × Rate`).

Use this when the proforma represents a partial (or full) shipment of the ordered items, for example a staged delivery.

### Based On: Amount

Switch **Based On** to **Amount** to enter a monetary **Amount** per line directly. Both **Quantity** and **Amount** are editable, and the rate is derived from them (`Rate = Amount ÷ Quantity`).

Use this for value-based or advance proformas, for example "30% advance against this order".

### Hide Item Quantity in Print

When **Based On** is **Amount**, an additional option, **Hide Item Quantity in Print**, becomes available. Enable it to omit the quantity and rate columns from the printed proforma, so it shows only the item and the amount. This produces a clean value-based document where you do not want to disclose a per-unit rate.

## Quantity/Amount Warning

Proforma quantities and amounts are **not** enforced; a proforma is informational. However, if the **total** proforma quantity or amount for a line (this proforma plus any previously issued proformas) exceeds the ordered value, a warning is shown below the items table. You can still create the proforma; the warning is only there to flag it.

---

## The Proforma Tab

Once at least one proforma exists for a Sales Order, a **Proforma** tab appears on the Sales Order. It lists every proforma raised against that order, showing the number, date, grand total and status.

[Screenshot on the live page]
*Proforma lists*

From this list you can:

- **View PDF**: open the attached proforma PDF.  
- **Send Email**: email the proforma PDF to the customer.
- **New**: create another proforma.

---

## Print and Email

Every proforma has its PDF generated and attached automatically on creation, using the selected print format and letterhead. You can:

- Open the PDF from the **Proforma** tab (**View PDF**) or from the Proforma Invoice record.
- Email it to the customer using **Send Email** from the tab, or the standard print/email options on the Proforma Invoice record.

[Screenshot on the live page]
*Proforma Invoice PDF*

## Cancel a Proforma Invoice

To void a proforma, open the Proforma Invoice record and **Cancel** it. Cancelling marks the proforma as **Cancelled** but keeps its PDF for reference, and cancelled proformas remain listed in the Proforma tab (shown with a red *Cancelled* status) so you retain a full audit trail. A cancelled proforma no longer counts towards the total proforma quantity/amount used by the warning.

---

## Related Topics

1. [Sales Order](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/sales-order)
2. [Sales Invoice](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/sales-invoice)
3. [Selling Settings](https://file+.vscode-resource.vscode-cdn.net/docs/user/manual/en/selling-settings)

<!-- page: erpnext/erpnext__project-costing.md -->
---
title: "Project Costing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-costing"
updated: "2026-02-26"
---

Each project has multiple tasks associated with it. To track the actual cost of a Project, primarily in terms of services, a User has to create a Timesheet based on the time spent on a Task within a Project. You can track the service cost against a Project in the following ways.

## Activity Type

Activity Type is a master of services offered by your personnel. You can add a new Activity type from:

> Home > Projects > Activity Type > New

[Screenshot on the live page: Screenshot 2024-06-21 at 3.13.26 PM]

## Activity Cost

Activity Cost is a master where you can track billing and costing rate for each Employee, for each Activity Type.

[Screenshot on the live page]

## Timesheet

Based on the time spent on the Project-Task, an Employee will create a Timesheet.

[Screenshot on the live page]

On selection of the Activity Type in the Time Log, Billing and Costing Rate will be fetched for that Employee from the respective Activity Cost.

Multiplying these rates with total no. of hours in the Time Log gives Costing Amount and Billing Amount for the specific Time Log.

## Costing in Project and Task

Based on all the Timesheets created for specific Tasks, its costing will be updated in the respective Task.

[Screenshot on the live page]

Same way, the Project cost will be updated based on Timesheets created against each of its associated tasks and the cost of the Project gets updated simultaneously.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__project-customer-portal.md -->
---
title: "Project from Customer Portal\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-customer-portal"
updated: "2026-02-26"
---

If you are working on a Project for a Customer, then they need to be updated on its progress from time-to-time. You can achieve this in ERPNext via the Customer Portal.

### Add User as a Website User

To access a project from the portal, a customer must be added as a Website User. A Customer can also sign up from the Login Page of your ERPNext account, using the same Email ID as mentioned in the Contact. You can also send an invite to the contact using the **Invite User** button in Contact.

[Screenshot on the live page]

### Add Customer and User in Project

In the Project, check Customer Details section. Select a Customer and Sales Order associated with this Project.

[Screenshot on the live page]

Under the User table, select the contacts who can access this project.

### Portal View of Project

When a Customer logins from the Portal, they will be able to view all the tasks for that project along with the associated timesheets. Also, the customer will be able to update the status of the tasks or comment when needed.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__project-expense-claims.md -->
---
title: "Project and Managing Expenses\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-expense-claims"
updated: "2026-02-26"
---

Employees working on a Project incur various expenses, sometimes from their pockets and then can claim such expenses using Expense Claim.

While filling up the claim, they can specify the Project for which they have made the expense.

[Screenshot on the live page]

Based on the Expense Claims made for a particular project, total Expense Claim Amount is updated in the Project master, under project costing section.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__project-profitability.md -->
---
title: "Project Profitability\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-profitability"
updated: "2026-02-26"
---

Project and related activities are generally active for longer periods. While developments keep happening on the Project, various transactions are done against each project. While new developments keep happening on a project, it may lead to more investment in terms of time, money, and material. Hence, it becomes important to track the Profitability of a Project to ensure that you don't overspend.

In simple terms, Project Profitability is the difference between the revenue generated from a project versus the costs associated with it.

### Project in Sales Transactions

You can link a Project in all sales transactions like Sales Order, Delivery Note, Sales Invoice, and Payment. Linking your project with the sales transactions will help you track the income received against that Project.

In sales transactions, Project field is generally available in the More Information section.

[Screenshot on the live page]

#### Project in Purchase Transactions

You can also link your project to the purchase transactions like Purchase Order, Purchase Receipt, and Purchase Invoice.

In the purchase transactions, the option to link a project is available in the Item table. This is because you could be procuring material for multiple projects from the same purchase entry.

[Screenshot on the live page]

### Budgeting against Project

You can create a Budget for a project as well. The expense limit defined in the Budget will be validated in the expense transactions.

[Screenshot on the live page]

### Project Profitability

Based on all the income and expense entries created for the Project, you can get its profitability.

> Accounting > Profitability Analysis

You can filter the report by Project to check Project-wise Profitability.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__project-reports.md -->
---
title: "Project Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-reports"
updated: "2026-02-26"
---

These reports help track project progress, project status, and key metrics such as timelines, costs, and resource allocation

## Project Summary

The **Project Summary** provides an overview of key project information, including the current project status, start and end dates, and a consolidated view of related records. It displays the number of associated **Tasks** and **Timesheets**, allowing users to quickly assess project progress and activity at a glance.

The image below shows the summary of the example we discussed in Getting started for the Rack Storage manufacturing. 

[Screenshot on the live page]
*Project Summary*

## Daily Timesheet Summary

The **Daily Timesheet Summary** provides a consolidated view of all tasks recorded in a timesheet for a selected time period. It displays the timesheet activities along with the logged hours and the corresponding linked tasks and projects, enabling users to review daily time allocation at a glance.

[Screenshot on the live page]
*Daily Timesheet Summary*

## Timesheet Billing Summary

This report provides a summary of t**imesheet-based billing** for a selected time period. It displays the total working hours along with the corresponding billable hours, billing rates, and calculated billing amounts, enabling users to review and analyze time-and-material billing at a glance.

[Screenshot on the live page]
*Timesheet Billing Summary*

## Project Wise Stock Tracking

This report provides visibility into stock movements associated with projects, including purchased items and issued items. It also displays key project information such as the project status, total project value, and the project start and completion dates, enabling effective tracking of material usage and overall project progress.

[Screenshot on the live page]
*Project wise stock tracking*

## Delayed Task Summary

The Delayed Tasks Summary report helps identify the tasks which have exceeded their Expected End Dates. It provides visibility into both on-track and delayed tasks, along with their current progress and the expected start and end dates, enabling users to identify schedule deviations and take corrective action.

To view this report, you can go to:

> Home > Projects > Reports > Delayed Tasks Summary

The report is generated based on the Task Doctype.

### Calculation of Delay

Tasks have a date field called **Completed On**, which becomes visible when a Tasks status is changed to Completed.

##### Scenario 1

If a task is marked as Completed and the Completed On field is set, then the delay is calculated as the difference between the Completed On and the Expected End Date.

```
Delay = Completed On - Expected End Date
```

##### Scenario 2

If the Completed On field is not set, then the delay is calculated as the difference between the current date and the Expected End Date.

```
Delay = Current Date - Expected End Date
```

### Chart

The chart shows the number of tasks that are On Track or Delayed based on the report generated after applying the filters.

[Screenshot on the live page: Delayed Tasks Summary]
*Delayed Tasks Summary*

<!-- page: erpnext/erpnext__project-template.md -->
---
title: "Project Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-template"
updated: "2026-02-26"
---

**A Project Template is a predefined sequence of tasks arranged in stipulated schedule.**

These templates can be pulled for similar kind of Projects and the tasks therein get auto-populated at the time of creation of each new project.

To access Project Template, go to:

> Home > Projects > Projects > Project Template

[Screenshot on the live page]

## How to Create A New Project Template:

1. Go to the Project Template List and click on New.
2. Add the following details:

- **Project Template Name**: Title of the Project Template
- **Project Type**: Project Templates, just like projects can be classified into different project types, e.g., Internal or External.
- **Tasks**: Each Project Template will have a set of a predefined sequence of tasks. In this table, you can select the tasks you want for this template.

## Related Topics

1. [Project](/erpnext/user/manual/en/project)
2. [Task](/erpnext/user/manual/en/tasks)
