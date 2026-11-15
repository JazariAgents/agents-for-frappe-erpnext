<!-- Frappe documentation: erpnext, part 46 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__project-type.md -->
---
title: "Project Type\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-type"
updated: "2026-02-26"
---

**A Project Type is the classification of projects into different types to group similar kind of projects.**

Internal Projects, External Projects could be examples of Project types and are already created in the system. You can choose to add more Project Types. This comes handy when you are reviewing the Projects, and you want to filter the information based on Project Types.

[Screenshot on the live page]

To access Project Type, go to:

> Home > Projects > Projects > Project Type

## How to Create a Project Type

1. Go to the Project Type List and click on New.
2. Add the name of the Project Type and description
3. Save.

## Related Topics

1. [Project](https://docs.frappe.io/erpnext/user/manual/en/project)
2. [Project Template](https://docs.frappe.io/erpnext/user/manual/en/project-template)

<!-- page: erpnext/erpnext__project-update.md -->
---
title: "Project Update"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-update"
updated: "2026-02-26"
---

**A Project Update is the status of the Project which can be sent to all the stakeholders of the Project.**

Each time you want to update the stakeholders about the project, you can send a Project Update to them.

[Screenshot on the live page]

To access Project Update, go to:

> Home > Projects > Projects > Project Update

## How to Create a Project Update

---

1. Go to the Project Update List and click on New.
2. Add the name of the Project for which you want to send an update.
3. Add the name of the Users to whom you want to send the Project Update in the Child Table. These Users could be your Customers or any other Internal or External Stake Holders.
4. Save and Submit.

Once you have submitted the Project Update, an email is sent to the selected stakeholders with project updates.

### Additional Details

When you expand the table which has the names of the Users, you will be able to add the following details:

1. You can select whether you want to send a Welcome Email to any particular User while sending them the Project Update.
2. You can select whether you want any particular User to view Attachments in the Project Update.
3. You can add the description of the Current Status of the Project in the 'Project Status' field which will indicate the progress of the project.

<!-- page: erpnext/erpnext__project-views.md -->
---
title: "Project Views\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project-views"
updated: "2026-02-26"
---

As projects are time-sensitive, we need different kind of views to convey information in a visual manner to users viewing them.

Apart from the generic list and report views for projects and tasks, ERPNext also provides Gantt, Kanban, and Calendar views for tasks. You can access these views by going to the Task list and selecting them via the left sidebar.

## Gantt View

A Gantt Chart shows how tasks are linked to each other and shows their execution sequence, based on start and end dates set in the tasks along with any dependencies, if available.

[Screenshot on the live page]
*Gantt Chart View*

You can update the range of the chart by selecting one of Quarter Day, Half Day, Day, Week, or Month.

Dragging a task along the dates will update the start and end date of a task.

If you want to further customize the chart and make it more colorful, read this article

## Kanban View

Kanban in Japanese means "billboard" or "signboard" as the task management method traces its origin back to Toyota's lean manufacturing process. In a typical kanban board setup, you have a board or wall which is divided into section which represent different stages of execution or realization. Tasks go up on the board as sticky notes or Post Its and move through the board updating its current stage in the process.

[Screenshot on the live page]
*Kanban View*

ERPNext renders the Kanban view for tasks based on its status. You can update the status of a task by moving the representative card from one column to the next. You can also assign colors to these columns for visual reference.

Read customizing Kanban board to learn more.

## Calendar View

Like the Gantt chart, the calendar view also shows the task and the planned number of days it'll take to complete. However, this one shows the task spread across your regular calendar.

[Screenshot on the live page]
*Calendar view *

<!-- page: erpnext/erpnext__project.md -->
---
title: "Project\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/project"
updated: "2026-02-28"
---

**A Project is a planned piece of work that is designed to find information about something, to produce something new, or to improve something.**

In ERPNext, project management is task-driven. You can create a Project and divide it into multiple Tasks.

A Project has a broad scope and hence can be divided into tasks. Think of coming up with a new smartphone for the next year as a Project. Then things like designing, prototyping, testing, delivery, etc. become tasks under the project.

Whilst each task within a Project can be assigned to an individual or a group of individuals, the assignment can also be done at the project level.

These Tasks can be created from a Project itself or a Task can be created separately as well.

To access Projects, go to:

> Home > Projects > Project

[Screenshot on the live page]

## How to Create a Project

1. Go to the Project list and click on New.
2. Add the following details:

- **Project Name**: Title of the Project.
- **Status**: The default status of a Project is going to be 'Open', which can later be changed to 'Completed' or 'Cancelled'.
- **Expected End Date**: Enter the date on which you aim to finish the project.

### Additional Options while creating a Project

1. **From Template**: If you have an existing [Project Template](/erpnext/project-template), you can choose to create your project using this template.
2. **Expected Start Date**: If you have a time-line fixed for the project, you can define both expected Start Date and Expected End Date in the form.
3. **Project Type**: You can classify your projects into different [types](/erpnext/project-type), e.g., Internal or External.
4. **Priority**: You can select the priority level of the Project based on how crucial it is. You can also add more priority levels.
5. **Department**: If the project belongs to, or is owned by a [Department](/hr/department) in the organization, you can add that here.
6. **Is Active**: A Yes/No tab, which lets you change the active status of the project at any later stage.
7. **Completion Method**: You can track the % completion of your project based on one of the three methods, viz. **Manual, Task Completion, Task Progress and Task Weight**.

[Screenshot on the live page]

Some examples of how the Percentage Completion is calculated based on Tasks:


| Project | Activity | % Progress | Weight | Status    |
| ------- | -------- | ---------- | ------ | --------- |
| SC001   | Build    | 100        | 0.4    | Completed |
| SC001   | Operate  | 100        | 0.2    | Completed |
| SC001   | Transfer | 50         | 0.2    | Open      |



| Method              | Formula                                             | Calculation                         | % Task Completed |
| ------------------- | --------------------------------------------------- | ----------------------------------- | ---------------- |
| **Manual**          | -                                                   | -                                   | Manual           |
| **Task Completion** | Task completed / Total no. of Tasks                 | 2/3                                 | 66.66            |
| **Task Progress**   | Sum of % Progress of all Tasks / Total No. of Tasks | (100+100+50)/3                      | 83.33            |
| **Task Weight**     | Sum of (Task weight + % Progress)                   | (0.4 * 100 + 0.2 * 100 + 0.2 * 100) | 70               |


**Note:** If the total weight of the Tasks is not 100, then the calculated result will be divided by the total weight. For example, if the total of task weights is 70, then the percentage completed = (70/0.8)% = 87.5%.

## Project Configuration

### Customer, Sales, and Access Control

- **Customer**: If a Project is being carried out for a particular Customer, the details can be fed in here.
- **Sales Order**: If the Project originates from a Sales Order, you can fetch its details here.  This allows you to:
  - Track Project execution against the Sales Order
  - Update Customers on progress as per the agreed scope
- **Project Users and Access**:  You can add Website Users to the Project to grant them access. This is useful for:
  - Customers who want to monitor progress or provide feedback
  - Suppliers, Freelancers, or Contractual Employees working on the Project. You can also: 
    - Send a **Welcome Email** when adding a user
    - Control **Attachment Viewing permissions** for each user
- **Notes**: You can add any additional notes to the project.

> Learn more about allowing users to view projects - click [here](/erpnext/project-customer-portal)

[Screenshot on the live page]

### **Project Timeline Tracking**

- **Actual Start Date**: The Actual Start Date and Time are automatically captured based on the first Timesheet entry linked to the Project.
- **Actual End Date**: The Actual End Date and Time are automatically recorded based on the latest Timesheet update for the Project.

> To learn more about Timesheets, click [here](/erpnext/timesheets).

[Screenshot on the live page]

### Costing, Billing, and Financial Tracking

- **Estimated Cost**: Enter the Estimated Cost of the Project.
- **Total Sales Amount**: If you have already linked the Project with a Sales Order, the Total Sales Order Amount will be auto-populated here.
- **Total Costing Amount**: The system will automatically fetch the Total Costing Amount from all the Timesheets linked to this project.
- **Total Billable Amount**: The system will automatically fetch the Total Billable Amount from all the Timesheets linked to this project.
- **Total Expense Claim**: Based on the expenses claimed by an Employee for the completion of the Project, the Total Expense Claim will be auto-calculated.
- **Total Billed Amount**: The Total Billed Amount gets auto-populated in the system using the Sales Invoice created against the Sales Order.
- **Total Purchase Cost**: The Total Purchase Cost of a Project is the cost fetched from the Purchase Invoices that get created against a Purchase Order issued for supply of Materials required for a Project.
- **Total Consumed Material Cost**: Using the Stock Entry made as per the requirement of Materials in the Project, the Total Consumed Material Cost gets captured.

### Margin

**Gross Margin**: Gross Margin would give you the margin you have between your Total Costing Amount and the Total Billed Amount.

```
Gross Margin = (Total Sales Amount + Total Billable Amount) 
                - Total Costing Amount 
                + Total Billable Amount 
                + Total Expense Claim 
                + Total Purchase Cost + Total Consumed Material Cost)
```

**Gross %**: The percentage of the Total Billed Amount spent in the Total Costing Amount makes for the Gross %.

```
 ((Total Sales Amount + Total Billable Amount)
 - Total Costing Amount + Total Billable Amount
 + Total Expense Claim + Total Purchase Cost 
+ Total Consumed Material Cost) / Total Sales Amount) 100*
```

[Screenshot on the live page]

### Monitor progress

When you enable the 'Collect Progress' option by checking the box, it will enable you to add monitoring details to the project. A report on the progress of the project shall be sent to all stakeholders of the project.

- **Holiday List**: You can select the Holiday List for your company. This will allow you to collect the Progress Reports only on the Working Days.
- **Frequency**: You can set the frequency at which you wish to get the reports. It can be set to an hourly, twice daily, daily or on a weekly frequency.

[Screenshot on the live page]

## Related Topics

1. [Task](/erpnext/tasks)
2. [Project Type](/erpnext/project-type)
3. [Project Template](/erpnext/project-template)

<!-- page: erpnext/erpnext__projected-quantity.md -->
---
title: "Projected Quantity\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projected-quantity"
updated: "2026-03-02"
---


**Projected Quantity is the level of stock that is predicted for a particular Item based on the current stock levels and other requirements.**

It is the quantity of gross inventory that includes supply and demand in the past which
is done as part of the planning process.

The projected inventory is used by the planning system to monitor the reorder
point and to determine the reorder quantity. The projected Quantity is used by
the planning engine to monitor the safety stock levels. These levels are
maintained to serve unexpected demands.

Having tight control of the projected inventory is crucial to determine
shortages and to calculate the right order quantity.

[Screenshot on the live page: Projected Quantity]

The formula to calculate projected quantity is as follows:

*Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty - Reserved Qty for Production - Reserved Qty for Subcontracting - Reserved Qty for Production Plan*

* **Actual Qty**: Quantity available in the Warehouse. This is the actual physical stock you have.
* **Planned Qty**: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
* **Requested Qty**: Quantity requested via a [Material Request](/erpnext/material-request). It is added on submission of Material Request and subtracted when Purchase Order/Work Order/Stock Entry is created against it based on the Material Request type.
* **Ordered Qty**: Quantity ordered for purchase ([Purchase Order](/erpnext/purchase-order)), but not received (via a [Purchase Receipt](/erpnext/purchase-receipt) or a [Purchase Invoice](/erpnext/purchase-invoice).
* **Reserved Qty**: Quantity ordered for sale by your Customer ([Sales Order](/erpnext/sales-order)), but not delivered (via a [Delivery Note](/erpnext/delivery-note)). This quantity increases when a Sales Order is submitted and decreases when a Delivery Note or Sales Invoice is created against that Sales Order is submitted.
* **Reserved Qty for Production**: Raw materials are reserved on submission of [Work Order](/erpnext/work-order) and is reduced when raw materials are transfered to Work in Progress warehouse via a Stock Entry.
* **Reserved Qty for Subcontracting**: Raw materials reserved when a subcontracting Purchase Order is submitted. When raw materials are transfered to Supplier Warehouse via a Stock Entry, this quantity reduces. To know more about subcontracting [click here](/erpnext/subcontracting).
* **Reserved Qty for Production Plan**: Raw materials are reserved when a Production Plan is submitted. When materials are reserved for the production against the work order then the system will reduce the "Reserved Qty for Production Plan" in the respective BIN. The system reduces the quantity if the work order was made against the production plan.

#### Related Topics
1. [Warehouse](/erpnext/warehouse)
1. [Material Request](/erpnext/material-request)

<!-- page: erpnext/erpnext__projects-introduction.md -->
---
title: "Project Overview"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects-introduction"
updated: "2026-02-26"
---

### **Overview**

The Project Module in ERPNext is used to plan, track, and manage projects within the system. It helps organize project work, monitor progress, and keep track of time and costs, while remaining closely integrated with other ERPNext modules.

Projects in ERPNext act as a central point for tasks, timesheets, expenses, and billing. This makes it easier to track work progress and understand the project's actual cost and outcome without relying on external tools.

### **Key Features**

The Project Module offers a comprehensive set of features to manage projects end-to-end:

- **Projects and Tasks**  
Create projects and define tasks with assigned users, status, and timelines.
- **Timesheets**  
Log time spent on tasks and associate it with projects.
- **Cost Tracking**  
Record project-related expenses and material usage.
- **Billing**  
Create invoices based on time logs, milestones, or fixed project values.
- **Integration with ERPNext**  
Projects are linked with Accounting, HR, Sales, Purchase, and Inventory modules.

<!-- page: erpnext/erpnext__projects__introduction__getting-started.md -->
---
title: "Getting Started"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects/introduction/getting-started"
updated: "2026-02-06"
---

The Project Module in ERPNext is used to track work that involves multiple steps, people, and transactions. A project brings together tasks, time, materials, deliveries, and billing under a single reference.

The example below shows how a simple manufacturing job can be managed as a project and how it connects with other ERPNext modules.

## Scenario**:**

A manufacturing company receives an order to make a **custom metal storage rack** for a warehouse customer.

### **Prerequisites**:

- Create an [Item](https://docs.frappe.io/erpnext/user/manual/en/item) - Storage Rack

### Step 1: Create a Sales Order for the rack

- To create a sales order, go to:

> Home > Selling  > Sales Order

[Screenshot on the live page]
*Sales order with the Storage Rack*

### Step 2: **Create the project from the Sales Order**

- After the sales order is submitted, we can create the project from it
- [Screenshot on the live page]
*Creating project from Sales Order*
- Once the project is created, the dashboard will be created, which will allow the creation of tasks and timesheets
- [Screenshot on the live page]
*Project Dashboard*

### Step 3:  **Creating the Basic Tasks for the project**

- We create separate tasks for the project, like cutting and welding, painting, and final assembly. 
- [Screenshot on the live page]
*Task for Cutting & welding*

### **Step 4: Create purchase orders for the raw materials and respective stock entries as well**

- The raw material required for making the Storage rack would be purchased, therefore the purchase order would be made for the same 
- [Screenshot on the live page]
*Purchase order for raw material*

### Step 5: **Create a timesheet to record the execution of steel sections and paints**

- To maintain the execution of the steel sections and the painting of the storage rack, we create a timesheet 
- The changes made in this project will reflect the costing and billing details
- [Screenshot on the live page]
*Execution details in timesheet*

### **Step 6: As the process continues, we update the task with its progress**

[Screenshot on the live page]
*Task Status *

- Once all the tasks are completed, the project moves into a fully completed state as well

[Screenshot on the live page]
*Final Project Status*

<!-- page: erpnext/erpnext__projects__project-settings.md -->
---
title: "Project Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/projects/project-settings"
updated: "2026-02-25"
---

# Settings

There are certain settings that are available for the Project module, which allow for handling overlap time scenarios, and the billing settings control whether logged time can be invoiced. These are all disabled by default. 

The settings available are: 

[Screenshot on the live page]
*Project Settings*

### Ignore Workstation Time Overlap

When **enabled**, ERPNext allows multiple overlapping time logs against the same workstation. It would be useful in places where workstations are shared

### Ignore User Time Overlap

When **enabled**, ERPNext allows overlapping time entries for the same user. It would be useful for users who log time on behalf of multiple employees or teams.

### Ignore Employee Time Overlap

When **enabled**, ERPNext allows overlapping time entries for the same employee. This can be useful at times activity tracking is done and no strict hour validation is required like the HR use cases

### Fetch Timesheet in Sales Invoice

When **enabled**, billable Timesheet entries can be fetched directly into a **Sales Invoice**.

This allows:

- Billing customers based on logged hours
- Automatic population of invoice items from Timesheet Details linked to a Project

<!-- page: erpnext/erpnext__promotional-scheme.md -->
---
title: "Create Promotional Schemes and Discount Slabs | ERPNext Documentation"
description: "Configure ERPNext Promotional Schemes with quantity and amount slabs, party conditions, validity, priorities, and generated Pricing Rules."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/promotional-scheme"
updated: "2026-07-25"
---

A Promotional Scheme manages one or more discount slabs and generates the corresponding [Pricing Rules](/erpnext/pricing-rule). Use it when an offer needs several quantity or amount tiers, mixed-item conditions, cumulative purchases, or a discount on another Item.

## Before you begin

Create the required:

- [Items](/erpnext/item), Item Groups, or Brands.
- [Customers](/erpnext/customer), Customer Groups, Territories, Sales Partners, or Campaigns used as conditions.
- Selling or buying [Price Lists](/erpnext/price-lists) and Item Prices.

Define the business rule in plain language before configuring slabs. Include eligible parties, items, dates, currency, warehouses, thresholds, and whether purchases accumulate.

## Create a Promotional Scheme

1. Open the Promotional Scheme list and select **Add Promotional Scheme**.
2. Enter a descriptive title.
3. Select what the scheme applies on: Item Code, Item Group, Brand, or Transaction.
4. Add the eligible values in the table.
5. Select Selling, Buying, or both.
6. Add party conditions when the scheme is restricted.
7. Add Price Discount or Product Discount slabs.
8. Set validity, currency, warehouse, and priority when applicable.
9. Save.

[Screenshot on the live page: An ERPNext Promotional Scheme with applicability and party settings.]

Saving the scheme creates linked Pricing Rules. Manage the scheme as the source of the slab configuration instead of editing generated rules independently without understanding the relationship.

## Configure discount slabs

Each slab can use minimum and maximum quantity or amount thresholds.


| Field             | What it controls                                      |
| ----------------- | ----------------------------------------------------- |
| Min Qty / Max Qty | Quantity range that qualifies                         |
| Min Amt / Max Amt | Value range that qualifies                            |
| Rate or Discount  | Price reduction for the qualifying slab               |
| Product Discount  | Free Item and quantity for the slab                   |
| Rule Description  | Operational explanation of the offer                  |
| Warehouse         | Limits the rule to Items selected from that Warehouse |
| Priority          | Resolves conflicts with other applicable rules        |


Leave a maximum blank only when the slab should have no upper limit. Avoid overlapping slabs unless the intended priority is explicit.

## Mixed Conditions

Enable **Mixed Conditions** when quantities or values from several eligible Items should be combined before testing a threshold.

For example, if laptop sleeves and docks are both eligible and Min Qty is 10, the rule can qualify when their combined quantity reaches 10.

## Cumulative purchases

Enable **Is Cumulative** when ERPNext should evaluate qualifying transactions over time for a party. Define amount thresholds and the applicable period. The discount applies to the transaction that crosses the threshold, not retroactively to earlier transactions.

Verify which submitted transaction types your current version includes in cumulative evaluation before launching the program.

## Apply a scheme to another Item

Use **Apply Rule On Other** when the condition is based on one set of Items but the discount applies to another. Test the transaction with all required Items present.

## Test the scheme

Create a new [Quotation](/erpnext/quotation) or [Sales Order](/erpnext/sales-order), select an eligible party, and add Items around each slab boundary.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock. Use the highlighted pencil icon to open the full row editor when reviewing applied pricing details.

## Troubleshooting


| Problem                          | What to check                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| No discount is applied           | Verify generated Pricing Rules, eligibility, thresholds, dates, currency, warehouse, and transaction type |
| The wrong slab applies           | Check overlapping ranges and boundary values                                                              |
| Cumulative totals seem incorrect | Confirm party, period, included transaction types, and submitted status                                   |
| Another offer wins               | Review priorities and overlapping Pricing Rules                                                           |
| A scheme change has no effect    | Save the scheme and inspect its generated rules                                                           |


## Frequently asked questions

### When should I use a Promotional Scheme instead of a Pricing Rule?

Use a Promotional Scheme for several slabs or when one managed offer needs multiple generated rules.

### Can a scheme apply to buying transactions?

Yes. Configure Buying applicability and the appropriate Supplier conditions.

### Can a scheme give free Items?

Yes. Use Product Discount slabs.

### Does a cumulative discount adjust earlier invoices?

No. It applies to the qualifying transaction that crosses the threshold.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Applying a Discount](/erpnext/applying-discount)
- [Coupon Code](/erpnext/coupon-code)
- [Buy 1 Get 1 Free Pricing Rule](/erpnext/setting-up-buy-1-get-1-free-pricing-rule)
- [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__purchase-cycle-ledger-impact.md -->
---
title: "Purchase Cycle Ledger Impact"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-cycle-ledger-impact"
updated: "2026-08-02"
---

The purchase cycle begins when you commit to buy from a supplier and ends when the supplier is paid. Not every document creates an accounting entry. A Purchase Order records the commitment, while the Purchase Receipt, Purchase Invoice, and Payment Entry record the inventory, liability, expense, and cash effects that follow.

The examples below use common account names and exclude taxes to keep the entries easy to follow. Your account names may differ. ERPNext uses the accounts configured for the Company, Item, Item Group, warehouse, and transaction.

## Understand when the ledger changes

ERPNext creates General Ledger entries when an accounting or stock transaction is submitted. Saving a draft does not affect the ledger.


| Document                                    | Typical ledger impact                                        | What it represents                                                                                   |
| ------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Purchase Order                              | No General Ledger entry                                      | A commitment to buy goods or services at an agreed quantity, rate, and schedule.                     |
| Purchase Receipt for stock items            | Debit Stock In Hand; credit Stock Received But Not Billed    | Inventory has been received, but the supplier invoice may not have arrived.                          |
| Purchase Invoice against a Purchase Receipt | Debit Stock Received But Not Billed; credit Accounts Payable | The temporary receipt liability is cleared and the confirmed amount becomes payable to the supplier. |
| Purchase Invoice for a service              | Debit the relevant Expense; credit Accounts Payable          | The service cost is recognized and the supplier is owed the invoice amount.                          |
| Payment Entry, Pay                          | Debit Accounts Payable; credit Bank or Cash                  | The supplier liability is reduced and money leaves the company.                                      |


The debit and credit are two sides of the same event. For example, paying a supplier reduces Accounts Payable, so Accounts Payable is debited. It also reduces Bank, so Bank is credited.

## Example 1: Manufacturing company purchasing stock items

Assume a manufacturer purchases five stock-controlled electronic units from Apex Devices at $520 each, for a total of $2,600. The same accounting flow applies when the purchased stock consists of raw materials, components, consumables, or finished goods.

### 1. Submit the Purchase Order

The Purchase Order records what the company agreed to buy, the supplier, rate, warehouse, and expected receipt date. It does not increase inventory, create an expense, or create a supplier payable.

**Ledger impact:** None.



[Screenshot on the live page: Submitted Purchase Order for stock-controlled electronic items]

### 2. Submit the Purchase Receipt

The Purchase Receipt confirms that the stock has physically arrived. ERPNext increases the stock asset and records an equal temporary liability in **Stock Received But Not Billed**.


| Account                       | Debit     | Credit    | Explanation                                                                                     |
| ----------------------------- | ---------: | ---------: | ----------------------------------------------------------------------------------------------- |
| Stock In Hand                 | $2,600.00 |           | Inventory controlled by the company increases.                                                  |
| Stock Received But Not Billed |           | $2,600.00 | The goods have arrived, but the supplier invoice is not yet represented as a confirmed payable. |


[Screenshot on the live page: General Ledger entries created by the Purchase Receipt]

**Stock Received But Not Billed** is a clearing account. It allows the physical receipt and the supplier invoice to be recorded on different dates without losing the liability created by the receipt.

### 3. Submit the Purchase Invoice

When the supplier invoice is recorded against the Purchase Receipt, ERPNext moves the amount from the temporary receipt liability to the supplier's payable account.


| Account                       | Debit     | Credit    | Explanation                                                         |
| ----------------------------- | ---------: | ---------: | ------------------------------------------------------------------- |
| Stock Received But Not Billed | $2,600.00 |           | The temporary liability created by the Purchase Receipt is cleared. |
| Accounts Payable (Creditors)  |           | $2,600.00 | The confirmed amount is now owed to the supplier.                   |


[Screenshot on the live page: General Ledger entries created by the stock Purchase Invoice]

The Stock In Hand debit is not repeated on the invoice because the Purchase Receipt already increased inventory. Across the receipt and invoice together, Stock In Hand remains debited and Accounts Payable remains credited, while Stock Received But Not Billed returns to zero.

### 4. Pay the supplier

Submit a Pay-type Payment Entry and allocate it to the Purchase Invoice.


| Account                      | Debit     | Credit    | Explanation                                 |
| ---------------------------- | ---------: | ---------: | ------------------------------------------- |
| Accounts Payable (Creditors) | $2,600.00 |           | The amount owed to the supplier is cleared. |
| Bank                         |           | $2,600.00 | Money leaves the company's bank account.    |


[Screenshot on the live page: General Ledger entries created by the supplier Payment Entry]

The Payment Entry does not increase inventory or recognize the purchase again. Those effects were already recorded by the Purchase Receipt and Purchase Invoice. The payment only settles the supplier liability.

## Example 2: Services company purchasing a service

Assume a services company purchases ten device-setup support sessions from Vertex Components at $200 each. The total supplier charge is $2,000.

A non-stock service does not increase inventory, so a stock Purchase Receipt is normally unnecessary. The company can move from Purchase Order to Purchase Invoice and Payment Entry. Use a receipt or acceptance workflow only when the business needs a separate operational confirmation that the service was delivered.

### 1. Submit the Purchase Order

The Purchase Order records the scope, quantity, rate, supplier, and expected completion date. It does not create an expense or supplier payable.

**Ledger impact:** None.



[Screenshot on the live page: Submitted Purchase Order for externally supplied services]

### 2. Submit the Purchase Invoice

When the supplier invoice is accepted, ERPNext recognizes the service expense and creates the supplier liability.


| Account                                         | Debit     | Credit    | Explanation                                   |
| ----------------------------------------------- | ---------: | ---------: | --------------------------------------------- |
| Administrative or Professional Services Expense | $2,000.00 |           | The service cost is recognized in the period. |
| Accounts Payable (Creditors)                    |           | $2,000.00 | The company now owes the supplier.            |


[Screenshot on the live page: General Ledger entries created by the service Purchase Invoice]

Choose the expense account that describes the service and supports useful reporting. For example, legal work may use Legal Expenses, rent may use Office Rent, and outsourced implementation may use Professional Services or an appropriate project expense account.

### 3. Pay the supplier

The supplier payment has the same basic effect as it does for a stock purchase.


| Account                      | Debit     | Credit    | Explanation                        |
| ---------------------------- | ---------: | ---------: | ---------------------------------- |
| Accounts Payable (Creditors) | $2,000.00 |           | The supplier liability is cleared. |
| Bank                         |           | $2,000.00 | The bank balance decreases.        |


[Screenshot on the live page: General Ledger entries created by the service supplier payment]

## Compare the two workflows


| Stage          | Manufacturing or stock purchase                                   | Service purchase                                         |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| Purchase Order | No ledger impact                                                  | No ledger impact                                         |
| Receipt        | Debits Stock In Hand and credits Stock Received But Not Billed    | Usually no stock receipt or inventory posting            |
| Invoice        | Debits Stock Received But Not Billed and credits Accounts Payable | Debits the selected Expense and credits Accounts Payable |
| Payment        | Debits Accounts Payable and credits Bank                          | Debits Accounts Payable and credits Bank                 |


If a stock-item Purchase Invoice is submitted with **Update Stock** enabled, ERPNext can combine the stock effect of a Purchase Receipt with the payable effect of the Purchase Invoice. The simplified posting is debit Stock In Hand and credit Accounts Payable. This is useful for direct purchases, but it removes the separate receipt document from the audit trail.

If a Purchase Invoice is created directly without a Purchase Order, it still creates its normal ledger entries. What is missing is the earlier procurement commitment, approval trail, expected delivery tracking, and comparison of ordered, received, and invoiced quantities.

## Frequently asked questions

### Does submitting a Purchase Order affect the General Ledger?

1. A Purchase Order records a procurement commitment. It does not create inventory, expense, tax, payable, or bank entries.

### Why is Stock Received But Not Billed used?

It bridges the timing difference between receiving stock and receiving the supplier invoice. The Purchase Receipt credits it, and the linked Purchase Invoice debits it. The account should clear when receipts and invoices match.

### What changes when purchase tax is included?

Accounts Payable is credited for the full supplier invoice. The purchase or expense amount is debited to its normal account, and recoverable input tax is debited to the configured tax asset account. Non-recoverable tax may instead become part of the item cost or expense, depending on configuration and local rules.

### Why does Stock Received But Not Billed have a remaining balance?

Check for Purchase Receipts that have not yet been invoiced, Purchase Invoices that do not reference the correct receipts, quantity or rate differences, returns, and backdated cancellations. Use the Purchase Receipt and Purchase Invoice references to reconcile the difference.

## Related topics

- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [General Ledger](/erpnext/general-ledger)
- [Buying module](/erpnext/buying)

<!-- page: erpnext/erpnext__purchase-invoice-account-type-error.md -->
---
title: "Purchase Invoice - Account Type Error\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/purchase-invoice-account-type-error"
updated: "2026-08-14"
---

Nova Industries receives a supplier bill from Apex Components, its regular parts supplier. ERPNext blocks the Purchase Invoice with the message that **Credit To must be a Balance Sheet account**. The message is protecting the payable: the supplier amount must sit in a liability account until Nova pays it.

## Fix the error

1. Open the Purchase Invoice and check **Credit To**.
2. Select the supplier payable account for the company, commonly Creditors or Accounts Payable.
3. Open that account in the Chart of Accounts and confirm it is under Liabilities and has Account Type **Payable**.
4. Set the correct default payable account on the Supplier or Company if the wrong account keeps returning.
5. Save and submit the invoice again.

[Screenshot on the live page: Purchase Invoice with the complete Credit To field highlighted]



## Why the account must be a liability


| Entry            | Debit                                     | Credit           |
| ---------------- | ----------------------------------------- | ---------------- |
| Supplier invoice | Expense, stock, asset, or service account | Supplier payable |
| Supplier payment | Supplier payable                          | Bank or cash     |


## Troubleshooting

### The correct account does not appear

Confirm that the account belongs to the invoice company, is not a group, is enabled, and has Account Type Payable. Also check the Supplier’s company-specific default account.

## Frequently asked questions

### Can I credit an expense account instead?

Use an expense or stock account on the debit side for what was purchased. The unpaid supplier balance belongs in a payable liability account.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)
