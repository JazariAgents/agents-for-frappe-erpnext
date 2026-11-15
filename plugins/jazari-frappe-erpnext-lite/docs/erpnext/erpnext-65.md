<!-- Frappe documentation: erpnext, part 65 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__territory.md -->
---
title: "Territory | ERPNext Documentation"
description: "Learn how to create ERPNext Territories, organize regional hierarchies, assign customers, managers, and item-group sales targets."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/territory"
updated: "2026-08-02"
---

A Territory in ERPNext represents a geographic or commercial region in which your company sells. Territories help classify Customers and Addresses, organize reporting, assign responsibility, and compare regional sales with targets.

Territories use a tree structure. A group territory contains lower-level territories, while a leaf territory can be selected on transactions. For example, United States can contain Northeast, which can contain New York Metro.

## Why use Territories?

- Segment customers and sales by region.
- Assign a Territory Manager for reference and accountability.
- Set item-group targets for a fiscal year.
- Compare regional targets with actual sales.
- Use consistent regional values across Customers, Addresses, and sales transactions.

## Before you begin

- Decide whether your hierarchy should follow countries, states, cities, sales zones, or another commercial structure.
- Keep the hierarchy stable enough for meaningful reporting.
- Create the relevant [Item Groups](/erpnext/item-group), Fiscal Years, and Monthly Distributions before adding targets.
- Set a Default Territory in [Selling Settings](/erpnext/selling-settings) if most new Customers should receive the same value.

## Create a Territory

1. Go to **Selling > Settings > Territory**.
2. Select **New**.
3. Enter a Territory Name.
4. Enable **Is Group** when this Territory will contain lower-level territories.
5. Select **Create New**.

[Screenshot on the live page: New Territory form with the Is Group checkbox highlighted]

The deep-red square highlights **Is Group**. A group organizes child territories and is not selected on a transaction. Leave it disabled when creating a leaf territory such as a city, metro area, or final sales zone.

## Alternative way to create a Territory

To create a Territory directly under an existing group:

1. Select the parent Territory in the tree.
2. Select **Add Child**.
3. Enter the child Territory name.
4. Enable Is Group only when the child will contain another level.
5. Create the record.

Using Add Child reduces the chance of placing the record under the wrong parent.

## Important fields and what they mean


| Field               | What it means                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Territory Name      | The name displayed in the tree, Customer master, sales transactions, and reports. Use names that users can identify consistently.                                   |
| Parent Territory    | The group directly above the current Territory. It determines the Territory’s position in the hierarchy.                                                            |
| Is Group            | Allows child Territories below this record. Only leaf nodes are intended for transactions.                                                                          |
| Territory Manager   | A reference to the person responsible for the region. It does not replace user permissions or the [Sales Person](/erpnext/sales-person) assignment on transactions. |
| Item Group          | The product category to which a target applies.                                                                                                                     |
| Fiscal Year         | The period for the target.                                                                                                                                          |
| Target Qty          | The quantity target for the selected Item Group and Fiscal Year.                                                                                                    |
| Target Amount       | The monetary sales target for the selected Item Group and Fiscal Year.                                                                                              |
| Target Distribution | Distributes the annual target across months. Use an even distribution or a seasonal pattern that matches the business.                                              |


## Organize the Territory hierarchy

A well-designed hierarchy moves from broad groups to the lowest reporting level you need. The Nova Electronics Trading demo uses United States as a group, four regional groups below it, and metro areas as leaf Territories.



[Screenshot on the live page: Expanded ERPNext Territory tree with United States regions and metro areas]

You can add multiple levels, but avoid unnecessary depth. A structure such as country → region → metro area is easier to maintain than a different hierarchy for every sales team.

Select a node to access actions such as Edit, Add Child, Rename, or Delete. ERPNext may prevent deletion when a Territory is linked to another record. Rename an existing Territory when the region continues to represent the same business segment.

## Choose an effective Territory structure


| Business model           | Example hierarchy                             |
| ------------------------ | --------------------------------------------- |
| National distributor     | Country → region → state or metro area        |
| International seller     | Global region → country → sales zone          |
| Local service company    | Service region → city → neighborhood or route |
| Account-based sales team | Market segment → named account region         |


Choose one primary purpose for the tree. Mixing geography, customer size, industry, and salesperson names in the same hierarchy makes reports difficult to interpret. Use Customer Group for customer segmentation and Sales Person for individual ownership instead.

Before creating many Territories, test the proposed hierarchy with a few representative Customers and reports. Confirm that users know which leaf to select and that managers can view totals at the group level they need.

## Assign a Territory to a Customer

Select the appropriate Territory on the [Customer](/erpnext/customer) record. The value can then flow into supported sales transactions. A default from Selling Settings helps during Customer creation, including when ERPNext converts a Lead-based [Quotation](/erpnext/quotation) into a Customer.

Use the final selectable Territory rather than a group. For example, select New York Metro instead of Northeast when metro-level reporting is required.

## Set Territory sales targets

1. Open a leaf Territory.
2. In Territory Targets, select **Add row**.
3. Select an Item Group and Fiscal Year.
4. Enter the Target Qty, Target Amount, or both.
5. Select a Target Distribution.
6. Save the Territory.

[Screenshot on the live page: ERPNext Territory target for New York Metro in fiscal year 2026]

The example assigns New York Metro a 2026 target of 3,000 units and 750,000 in sales for All Item Groups, distributed evenly across the year.

For more detail about targets and distributions, see [Sales Person Target Allocation](/erpnext/sales-person-target-allocation). Territory targets can be reviewed using target variance reports in [Sales Reports](/erpnext/sales-reports).

## Good practices

- Use short, recognizable names and avoid two Territories with nearly identical meanings.
- Create a group only when it will contain children or provide a useful reporting subtotal.
- Assign Customers to the lowest meaningful leaf Territory.
- Review unassigned and incorrectly assigned Customers before relying on territory-wise reports.
- Update targets at the start of each Fiscal Year and confirm their Monthly Distributions.
- Document major hierarchy changes so report users understand comparisons with earlier periods.

## Where Territory is used


| Area                 | How Territory helps                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Customer and Address | Classifies the customer or location for regional reporting. See [Address](/erpnext/address).                          |
| Sales transactions   | Carries the regional classification into documents such as Sales Orders and [Sales Invoices](/erpnext/sales-invoice). |
| Targets              | Stores quantity and amount targets by Item Group and Fiscal Year.                                                     |
| Reports              | Supports territory-wise analysis and target variance comparisons.                                                     |


## Troubleshooting

### I cannot select a Territory on a transaction

Confirm that it is a leaf Territory. Group Territories organize the tree but are not intended for transaction selection.

### A new Customer has the wrong Territory

Check the Customer record and the Default Territory in Selling Settings. Users can replace the default when another Territory is appropriate.

### I cannot delete a Territory

The Territory may have child nodes or links from Customers, Addresses, or transactions. Move or update those dependencies before deleting it.

### The target does not reflect seasonality

Review the selected Monthly Distribution. Its monthly percentages must total 100 percent and should match the expected sales pattern.

## Frequently asked questions

### Must a Territory represent a geographic area?

No. It can represent any stable regional or commercial structure, but geographic naming is usually easiest for users and reports.

### Can a Customer’s Territory be changed?

Yes. Change it when the Customer’s ownership or reporting region changes. Review how the change affects future reporting and internal responsibility.

### Is Territory the same as Sales Person?

No. Territory represents the region. Sales Person represents an individual or sales-team hierarchy and can receive contribution percentages and targets.

### How many hierarchy levels should I use?

Use only the levels required for assignment and reporting. Two or three meaningful levels are often easier to maintain than a very deep tree.

<!-- page: erpnext/erpnext__the-champion.md -->
---
title: "The Project Champion"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/the-champion"
updated: "2026-08-14"
---

Implementing ERPNext in any organisation requires clear identification of pain points, meticulous planning and active involvement of all parties associated with the project. It involves the integration of various business processes, data migration, training, and organisational change management.

Since there are so many moving parts in parallel, having a single point of contact for driving the activities plays a huge role. It has been fund that effectiveness of the Project Champion is the key distinguishing factor between Success and Failure.



These are some of the key benefits of having a Project Champion assigned for each project.

1. **Leadership:** Project Champion acts as a single point of contact at customer's end and provides strong leadership by closely adhering to the vision, goals, and objectives for the project.
2. **Stakeholder Buy-In:** Project Champion acts as a liaison between the project team and key stakeholders. He/She works to create more awareness about the project and acquires buy-in from the potential users and stakeholders.
3. **Resource Allocation:** Project Champion ensures that the required resources (man power, funding etc) is allotted as per the requirement to ensure seamless continuation of the project.
4. **Problem-Solving:** Project Champion provides solutions whenever any challenges are faced. They are expected to address burning issues, resolve interpersonal conflicts and make informed decisions to keep the project on track.
5. **Change Management:** ERP implementation involves reasonable changes in the processes and the way teams operate. Project Champion helps employees adapt to the new system, ensuring a seamless transition.
6. **Risk Management:** ERP implementations can be complex and risky as it directly affects business continuity of the user. A project champion identifies potential risks and derives strategies to mitigate them, minimising the likelihood of project delays or failures.
7. **Communication:** Project Champion keeps track of the project and shares updates with the concerned stakeholders.
8. **Accountability:** Project Champion builds the team at their end and ensures that everyone is aware of the role they have to play in the implementation process. They keep track of commitments, deadlines and milestones very closely and call out any potential risks.
9. **Continuous Improvement:** At times, ERP implementation can be an iterative process. So, a Project Champion continues to lead the project involving customisations, localisations and enhancements.

<!-- page: erpnext/erpnext__time-based-payout.md -->
---
title: "Time Based Payout"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/time-based-payout"
updated: "2026-02-26"
---

Time-based payout in ERPNext projects refers to the process of calculating and disbursing payments to employees or contractors based on the time they have spent working on specific projects or tasks.

This feature is particularly useful in industries where billing is tied to hourly rates or milestone achievements. ERPNext facilitates time-based payout by accurately tracking the time logged by individuals against project tasks or milestones. It allows organizations to set hourly rates or payment terms for different roles or projects, ensuring fair compensation for work done.

* [Sales Invoice from Timesheet](/erpnext/user/manual/en/sales-invoice-from-timesheet)
* [Salary Slip from Timesheet](/erpnext/user/manual/en/salary-slip-from-timesheet)

<!-- page: erpnext/erpnext__time-tracking.md -->
---
title: "Time Tracking"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/time-tracking"
updated: "2026-02-26"
---

Project time tracking in ERPNext plays a pivotal role in ensuring accurate project management and resource utilisation.

By allowing employees to log time against specific tasks or projects, ERPNext provides a clear visibility to time spent on various activities. This feature helps in monitoring project progress, identifying bottlenecks, and optimizing resource allocation.Time tracking in the project management modules allows project managers to make informed decisions based on real-time data, ultimately contributing to more efficient project execution and successful outcomes.

* [Activity Type](/erpnext/user/manual/en/activity-type)
* [Activity Cost](/erpnext/user/manual/en/activity-cost)
* [Timesheets](/erpnext/user/manual/en/timesheets)

<!-- page: erpnext/erpnext__timer-in-timesheets.md -->
---
title: "Timer in Timesheets"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/timer-in-timesheets"
updated: "2026-07-05"
---

The Timer in Timesheet helps users record actual working time without manually entering start and end times.

It is useful when employees work on project tasks, support work, consulting, internal activities, or any activity where the exact time spent needs to be captured.

## How The Timer Works

In a Timesheet, click **Start Timer** to open the Timer dialog.

The dialog lets you select:

- Activity Type
- Project
- Task
- Expected Hrs

When you start the timer, ERPNext creates a row in the Timesheet table with the current time as the **From Time**. The timer continues to count the elapsed time.

When you click **Complete**, ERPNext sets the **To Time**, calculates the total hours, and marks the row as completed.

## Starting A New Timer

To start a timer:

1. Create or open a draft Timesheet.
2. Click **Start Timer**.
3. Select the Activity Type.
4. Optionally select the Project and Task.
5. Enter Expected Hrs if you want ERPNext to alert you when the expected time is exceeded.
6. Click **Start**.

ERPNext adds the time log row and starts recording time.

## Completing The Timer

When the work is done, open the Timer and click **Complete**.

ERPNext will:

- Set the To Time.
- Calculate Hours.
- Mark the time log row as completed.
- Save the Timesheet.

You can then submit the Timesheet after reviewing the time logs.

## Resuming A Timer

If a Timesheet has an incomplete time log, ERPNext shows **Resume Timer** instead of Start Timer.

Use this when work was started earlier but not completed. ERPNext resumes the timer from the existing From Time and continues counting elapsed time.

## Expected Hours

Expected Hrs is optional. If it is entered, ERPNext can alert the user when the timer exceeds the expected duration.

This is helpful when work is planned for a fixed amount of time and users need a reminder when the planned time is exceeded.

## Billing And Costing

The timer records working hours. Billing and costing are handled through Timesheet fields such as:

- Is Billable
- Billing Hours
- Billing Rate
- Costing Rate

After the timer is completed, review these fields before submitting or billing the Timesheet.

## Common Checks

If the timer is not working as expected, check the following:

- The Timesheet is still in Draft state.
- An Activity Type is selected.
- The time log is not already completed.
- From Time and To Time are not overlapping with another Timesheet for the same user or employee.
- Project and Task are selected when the time needs to be tracked against a project.

## Summary

Use the Timesheet Timer when users need a simple start-and-stop way to record actual working time. It reduces manual entry, improves accuracy, and keeps time logs connected to the right Activity Type, Project, and Task.

## Related Topics

- [Timesheet](https://docs.frappe.io/erpnext/timesheet)
- [Project](https://docs.frappe.io/erpnext/project)
- [Task](https://docs.frappe.io/erpnext/task)
- [Activity Type](https://docs.frappe.io/erpnext/activity-type)
- [Sales Invoice](https://docs.frappe.io/erpnext/sales-invoice)

<!-- page: erpnext/erpnext__timesheet-against-work-order.md -->
---
title: "Timesheet against Work Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/timesheet-against-work-order"
updated: "2026-07-05"
---

In ERPNext manufacturing, time spent on a Work Order is normally tracked through **Job Cards**. A Job Card is created for a Work Order operation and is used to record the employee, workstation, start time, end time, completed quantity, and operation time.

Timesheets are generally used for recording employee working hours against activities, projects, tasks, or billable work. They are useful for service and project-based tracking. For production operations, Job Cards are the standard document because they are directly connected to Work Orders and manufacturing operations.

## Recommended Flow

Use this flow when you want to record time against a Work Order:

1. Create and submit the **Work Order**.
2. Make sure the Work Order has operations defined in its routing or operations table.
3. Create **Job Cards** for the operations.
4. In the Job Card, record the employee, workstation, start time, end time, and completed quantity.
5. Submit the Job Card after the operation is completed.

The recorded time in the Job Card helps track actual manufacturing time against the planned operation time.

## When To Use Job Card

Use Job Cards when:

- Time is being recorded for a manufacturing operation.
- The work is linked to a Work Order.
- You want to track workstation time, operation time, and completed quantity.
- You want production progress to be reflected against the Work Order.

Job Cards are designed for manufacturing and are the best fit for Work Order execution.

## When To Use Timesheet

Use Timesheet when:

- Employees need to record general working hours.
- Work is tracked against a Project or Task.
- Hours are billable to a customer.
- The activity is service-oriented rather than a manufacturing operation.

If you need to track employee hours for production but do not need operation-level manufacturing tracking, Timesheet can still be used as an internal time record. However, it does not replace Job Card for Work Order operation tracking.

## Important Difference

The key difference is:

- **Work Order + Job Card** tracks manufacturing execution.
- **Timesheet** tracks employee time and billable or costing hours.

For manufacturing, use Job Cards to keep production data accurate. Use Timesheets only when the business also needs a separate employee time-tracking record.

## Common Checks

If you expected to create a Timesheet directly from a Work Order, check the following:

- Whether the requirement is actually to track operation time. If yes, use Job Card.
- Whether the Work Order has operations defined.
- Whether Job Cards have been created for the Work Order operations.
- Whether employees and workstations are selected on the Job Card.
- Whether the Job Card is submitted after work is completed.

## Summary

For Work Orders in ERPNext, use **Job Cards** to record manufacturing time. Use **Timesheets** when the purpose is employee time tracking, billing, or project/task-based work.

## Related Topics

- [Work Order](https://docs.frappe.io/erpnext/work-order)
- [Job Card](https://docs.frappe.io/erpnext/job-card)
- [Timesheet](https://docs.frappe.io/erpnext/timesheet)
- [BOM](https://docs.frappe.io/erpnext/bill-of-materials)
- [Routing](https://docs.frappe.io/erpnext/routing)
- [Workstation](https://docs.frappe.io/erpnext/workstation)

<!-- page: erpnext/erpnext__timesheets.md -->
---
title: "Timesheet\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/timesheets"
updated: "2026-02-26"
---

**A Timesheet is the record of the number of hours spent by an employee on completion of each task.**

The Timesheet can also be used to calculate the billable towards an employee, to calculate their salaries, or to track an employee's contribution towards a Project or a Task.

In ERPNext, a Timesheet can have an account of a particular employee working on multiple Tasks or Projects in a tabular format.

To access Timesheet, go to,

> Home > Projects > Time Tracking > Timesheet

[Screenshot on the live page]

## How to create a Timesheet

- Go to Timesheet list and Click on New.
- Enter the Company name and the Employee Code.
- Add the following details to the field 'Time Sheets'.
  - **Activity Type**: Add the type of activity for which the Time Sheet has been created.
  - **From Time**: Enter the date and time at which the work was started.
  - **Hrs**: Enter the number of hours for which this Time Sheet has been created. One Timesheet can be used to track the work hours on multiple days as well.
  - **Project**: If this Time Sheet needs to be tagged to a particular Project, you can add the name of the Project here.
  - **Bill**: This box needs to be checked if this particular Time Sheet is a billable.
- Click on 'Add Row' to add more such Time Sheets.
- Save.
- After saving the Timesheet, according to the details entered in the different Time Sheets, the Start Date, End Date and the Total Working Hours will get updated automatically. Click Submit.

## Alternatively, a Timesheet can also be created from a Task in the following way:

1. Go to the Task for which you want to create a new Timesheet.
2. Go to 'Timesheet' under the Activity section on the Dashboard. The plus icon '+' here would re-direct you to the Timesheet creation page.
3. Follow the steps to create a Time Sheet.
  [Screenshot on the live page]

## Timer in Timesheet

A Timer can be used to record the actual time taken by an employee to finish a particular activity in a Timesheet.

### Steps to start a Timer:

- In a Timesheet On clicking **Start Timer** a dialog box pops up and you are required to enter the following details:
  - **Activity Type**: The Activity for which you are recording the Time.
  - **Project**: The Project for which you are creating the Timesheet.
  - **Task**: The Task for which you are recording the time in the Timesheet.
  - **Expected Hrs**: Enter the number of hours that you expect the Task to finish in.

[Screenshot on the live page]

- Once you have completed the Task, click on Complete. A new entry will be created in the Timesheet, and the time will get recorded as a Time Sheet in the Time Sheets Table in the Timesheet.
- If the time exceeds the 'Expected Hrs', an alert box appears.

[Screenshot on the live page]

## Additional Options while creating the Timesheet

The Time Sheet when expanded, allows you to enter the following details to it:

- **Expected Hours**: Enter the tentative time required to complete the Tasks on the Time Sheets.
- **To Time**: Enter the date and time at which the work was completed.
- **Completed**: This box needs to be checked if the Task has been completed while submitting the Timesheet.
- **Task**: If this Time Sheet needs to be tagged to a particular Task, you can do it here.
- **Billing Hours**: This number of hours for which the customer needs to be billed for this Timesheet.
- **Billing Rate**: The rate at which the customer needs to be billed for this work.
- **Costing Rate**: This is the actual cost of work done. It is fetched from the activity cost (per employee) or from activity type and can be edited.
- **Billing Amount**: The billing amount gets auto-calculated based on the billable number of hours and the billing Rate.
- **Costing Amount**: The costing amount gets auto-calculated based on the number of hours and the costing rate.

[Screenshot on the live page]

## Timesheet Configurations

### Billing Details

- **Total Billable Hours**: Based on the Timesheet, the Total Billable Hours will be auto-fetched here.
- **Total Billable Amount**: Based on the Timesheet, the Total Billable Amount will be auto-fetched here.
- **Total Billed Hours**: Once the Timesheet has been submitted, you will get an option to create a Sales Invoice from the Timesheet. The number of hours for which the Customer shall be billed will be fetched over here, and once the Sales Invoice is submitted, the Total Billed Hours will be fetched.
- **Total Billed Amount**: In a similar fashion as how the Total Billed Hours are fetched, the Total Billed Amount will also be fetched.
- **Total Costing Amount**: Based on the Timesheet, the Total Costing Amount, as specified by the Employee gets tagged here.
- **% Amount Billed**: Once the Timesheet is submitted, and a Sales Invoice is created from the Timesheet, the percentage of the Amount out of the Total Billable Amount which has been amounted for the Total Billed Amount gets calculated and is reflected here.

[Screenshot on the live page]

## After Saving the Time Sheet

Once a Timesheet is saved and submitted, the details like Billing Rate and Costing rate get locked, and cannot be changed. The following DocTypes can be created after submitting a Timesheet.

- Sales Invoice
- Salary Slip

<!-- page: erpnext/erpnext__track-items-using-barcode.md -->
---
title: "Track Items Using Barcode\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/track-items-using-barcode"
updated: "2026-03-02"
---


A barcode is a value decoded into vertical spaced lines. Barcode scanners are the input medium, like Keyboard. When it scans a barcode, the data appears in the computer screens at the point of a cursor.

## Item Master

To set the barcode of a particular item, you will have to open the Item record. You can also enter barcode while creating a new item.

[Screenshot on the live page: Material Transfer]

Once barcode field is updated in item master, items can be fetched using barcode. This feature will be available in Delivery Note, Sales Invoice, Purchase Receipt, and Stock Reconciliation transactions only.

[Screenshot on the live page: Material Transfer]

### UOM specific barcode 

You can also specify different barcode for different type of packaging of same item like unit and box. Select the UOM in Item Barcode table to get it auto selected when scanning items. 

[Screenshot on the live page: uom specific barcode]


## Using mobile phone / smartphone to scan and add items




Log in to your ERPNext account, go to the Item master and you'll be able to scan barcodes and add Items right from your smartphone!

[Screenshot on the live page: Item Barcode using Smartphone]

<!-- page: erpnext/erpnext__track-purchases-in-accounts.md -->
---
title: "Track Purchases In Accounts"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/track-purchases-in-accounts"
updated: "2026-07-15"
---

:::note
ERPNext version 16 feature
:::



## Overview

According to industry standards, the Cost of Goods Sold is calculated as:

:::note
COGS = Opening + Purchases - Closing
:::



While the opening and closing figures are easily available from the Stock Balance report, determining the purchases component is challenging — the "Stock Received but Not Billed" account may not function properly when using Purchase Invoices with the 'Update Stock' option enabled.

Also, purchases are not the only way stock value changes. Stock Entry, Stock Reconciliation and Landed Cost Voucher also add or remove stock value, and these movements were not visible anywhere in the Profit & Loss or Trial Balance reports.

## Solution

ERPNext addresses this through two pairs of accounts:

- **Purchase Expense Account** and **Purchase Expense Contra Account** — booked when stock is received through a Purchase Receipt or a Purchase Invoice (with 'Update Stock' enabled)
- **Expenses Added To Stock Account** and **Expenses Added To Stock Contra Account** — booked when stock value changes through a Stock Entry, Stock Reconciliation or Landed Cost Voucher

When these vouchers are recorded, the accounts receive equal debits and credits, resulting in **zero net impact** on the books. However, this allows the purchase amounts and the value added to (or removed from) stock to appear in the Profit & Loss and Trial Balance reports, making the COGS components directly visible.

## Enabling the Feature

Go to **Accounts Settings > Stock Expense Accounting** and enable the **Book Stock Expense GL Entries** checkbox.

- When disabled (default), no Purchase Expense or Expenses Added To Stock entries are booked.
- When enabled, the accounts become mandatory depending on the voucher type:


| Voucher Type                                             | Mandatory Accounts                                                         |
| -------------------------------------------------------- | -------------------------------------------------------------------------- |
| Purchase Receipt / Purchase Invoice (Update Stock)       | Purchase Expense Account and Purchase Expense Contra Account               |
| Stock Entry / Stock Reconciliation / Landed Cost Voucher | Expenses Added To Stock Account and Expenses Added To Stock Contra Account |


A company that has not configured a pair of accounts at all is simply skipped — no entries are booked for it. If only one account of a pair is set, the system stops the voucher with a message asking to set the missing account. This way, in a multi-company setup, each company opts in by configuring its accounts.

> **Note for upgrading sites:** if any Company or Item Default already uses a Purchase Expense Account, the checkbox is enabled automatically during migration so that existing purchase expense entries continue to be booked.

## Company Master Configuration

Users can set the default accounts in the Company master:

- **Purchase Expense** section: Purchase Expense Account and Purchase Expense Contra Account
- **Stock Expense** section: Expenses Added To Stock Account and Expenses Added To Stock Contra Account

The accounts can also be set per item or item group in the **Item Defaults** table. The system resolves the accounts in the following order:

1. Item Defaults (on the Item)
2. Item Group Defaults
3. Brand Defaults
4. Company

## Accounting Entries

For a Purchase Receipt of value 10,000 (existing behaviour):


| Account                         | Debit  | Credit |
| ------------------------------- | ------ | ------ |
| Purchase Expense Account        | 10,000 |        |
| Purchase Expense Contra Account |        | 10,000 |


For the stock vouchers, the Expenses Added To Stock pair mirrors the stock value movement:


| Transaction                                          | Entry                                                                        |
| ---------------------------------------------------- | ---------------------------------------------------------------------------- |
| Stock Entry — Material Receipt (10,000 in)           | Dr Expenses Added To Stock 10,000 / Cr Expenses Added To Stock Contra 10,000 |
| Stock Entry — Material Issue (5,000 out)             | Dr Expenses Added To Stock Contra 5,000 / Cr Expenses Added To Stock 5,000   |
| Stock Entry — Manufacture (10,000 finished goods in) | Dr Expenses Added To Stock 10,000 / Cr Expenses Added To Stock Contra 10,000 |
| Stock Reconciliation (Add 10,000)                    | Dr Expenses Added To Stock 10,000 / Cr Expenses Added To Stock Contra 10,000 |
| Stock Reconciliation (Less 5,000)                    | Dr Expenses Added To Stock Contra 5,000 / Cr Expenses Added To Stock 5,000   |
| Landed Cost Voucher (10,000 charges)                 | Dr Expenses Added To Stock 10,000 / Cr Expenses Added To Stock Contra 10,000 |


A plain Material Transfer between warehouses does not change the total stock value, so nothing is booked.

Since every pair nets to zero, the Balance Sheet is unaffected — the accounts exist purely to make the stock value movements visible in the Profit & Loss and Trial Balance reports for COGS analysis.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__track-semi-finished-goods.md -->
---
title: "Track Semi-Finished Goods"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/track-semi-finished-goods"
updated: "2026-02-26"
---

```
Note: This feature will be available in the ERPNext version 16
```

Semi-finished goods are materials that result from the completion of one operation and are used as raw materials to make final products or other semi-finished goods.

In ERPNext, if you want to track semi-finished goods, you need to create an item for each semi-finished good and also have an active Bill of Materials for each one.

So we thought, why can't we have a provision to define the finished/semi-finished goods against the operation as well as raw materials? With this, once we complete the operation, the semi-finished goods will be produced and the raw materials will be consumed. Similarly, after the completion of the last operation, the finished goods will be produced and all semi-finished goods will be consumed.

The user has to create a Bill of Materials for each finished/semi-finished good and assign it to operations of the final Bill of Materials, or they can manually select the raw materials required to produce the finished/semi-finished goods.


BOM (with Operations)
-----------------------------



* If you want to track "Semi Finished Goods", you need to enable "Track Operations" and "Track Semi Finished Goods" while making the BOM.
* While creating a BOM, the user will have the option to define the operation, operation time, workstation, and workstation type.
* The user will also have the option to set default warehouses, such as the source warehouse, work in progress warehouse, and finished goods warehouse.
* If the user has set 'skip material transfer' they can consume materials from the source warehouse or work-in-progress warehouse.
* If users perform specific operations through subcontracting, they will have options to define subcontracted operations. Users will also have the option to create a subcontracted purchase order against the subcontracted job cards.

Work Order
----------

[Screenshot on the live page: work-order-with-semi-fg]  


In the work order, users can see the finished/semi-finished good as well raw materials against each operations. On submission of the work order system will create the job cards automatically and users have to complete the job cards manually. User can complete the job cards using job card view or from workstation dashboard. Below are different ways to complete the job cards

1. If the 'Skip Material Transfer to WIP' checkbox is enabled and the 'Backflush Materials From WIP Warehouse' checkbox is enabled, then users must consume raw materials from the 'WIP Warehouse'. Users need to click the 'Start Job' button to begin the job and the 'Complete Job' button to stop the job. After that, users must submit the job card to create a stock entry to consume materials from the 'WIP Warehouse' and add finished/semi-finished goods to the 'Target Warehouse'.
2. If the 'Skip Material Transfer to WIP' checkbox is enabled and the 'Backflush Materials From WIP Warehouse' checkbox is disabled, then users must consume raw materials from the 'Source Warehouse'. Users need to click the 'Start Job' button to begin the job and the 'Complete Job' button to stop the job. After that, users must submit the job card to create a stock entry to consume materials from the 'Source Warehouse' and add finished/semi-finished goods to the 'Target Warehouse'.
3. If the 'Skip Material Transfer to WIP' is disabled, then users must have to transfer raw materials from the 'Source Warehouse' to 'Wip Warehouse'. After that, users need to click the 'Start Job' button to begin the job and the 'Complete Job' button to stop the job. After that, users must submit the job card to create a stock entry to consume materials from the 'WIP Warehouse' and add finished/semi-finished goods to the 'Target Warehouse'.


Job Card
---------------------

Users have to complete the Job Card, and once all Job Cards are completed, the system will complete the Work Order. From the Job Card, users must transfer materials from the Store to the Work In Progress warehouse, if the Skip Material Transfer option is disabled on the respective job card. After that, users need to create a Manufacture Stock Entry against the Job Card for the semi-finished or finished goods.

While making the Manufacture Stock Entry, the system will prompt the user to confirm whether they want to submit the entry. If the user selects "Yes," the system will create the Stock Entry in a Submitted state; otherwise, it will be created in a Draft state.

Workstation Dashboard
---------------------

[Screenshot on the live page: workstation-dashboard-png] Using the workstation dashboard, users can start, pause, resume, and complete job cards. Also, users can transfer raw materials from the source warehouse to the WIP warehouse against the job cards from the workstation dashboard. If "Skip Material Transfer" has enabled then no need to transfer raw materials. Also users don't get the subcontracted operations in the workstation dashboard.

### Transfer Materials

For the 'Brake Making' operation, the user has not enabled 'Skip Material Transfer', so they must transfer raw materials from the 'Stores' to the 'Work In Progress' warehouse. For the 'Chain Making' operation, the user has enabled 'Skip Material Transfer,' so they do not need to transfer raw materials.

[Screenshot on the live page: transfer-materials]  


### Start Job

To start the job card, click on the 'Start' button from the menu. On start system auto fetch the employee of the logged in user and set it in the modal.

### Pause Job

To pause the job card, click on the 'Pause' button from the menu.

### Resume Job

To resume the job card, click on the 'Resume' button from the menu.


### Complete Job with Auto Stock Entry

On click of 'Complete' button, system asks you to enter the quantity and system creates the auto stock entry with type as 'Manufacture'. This stock entry, consume the raw materials and add finished/semi-finished goods.

------------

Start and Complete Jobs Using **QR code**
-----------------------------------------

If you have QR codes for the job cards, you can use them to start and complete the job cards by scanning the QR codes in the 'Start Job'/'Complete Job' QR code fields.

[Screenshot on the live page: start-complete-job-suing-qrcode]  

<!-- page: erpnext/erpnext__translations.md -->
---
title: "Translations"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/translations"
updated: "2026-07-02"
---

**ERPNext is available in various languages most of which has been contributed by ERPNext community.**

The widely supported translations include French, Spanish, German, Turkish, Bosnian.

1. How to contribute translations?
----------------------------------

1. Open **Translations Tool** from the awesome bar
2. Select the language of your choice
3. Click any source message from left sidebar for which you want to add translation.
4. In the Translated Text field enter your suggested translation and click on **Suggest**.
5. You can click on another source text from left sidebar and add another translation.
6. Once you are done with all the translations you can click on **Contribute Translations** button.
7. You can view the status of your contribution by clicking on the source text under Contributed Translations section.

[Screenshot on the live page: Translation Tool]  


2. Status of the Contributed Translation
----------------------------------------

After you submit your translation, it will be queued for verification. A member of the Frappe team/community will validate the contributed translation and set the status as **Verified** if the translation is **correct**. If the contributed translation is **incorrect**, the member of the Frappe team/community will reject that contributed translation.

Every week the translation server will create a **Pull Request** containing all the **verified translations** that were contributed.

3. Become a Verifier for Translations
-------------------------------------

If you want to **verify** the translations contributed by other members of the community, sign-up on [translate.erpnext.com](https://translate.erpnext.com). Verifiers can verify or reject the contributions.

<!-- page: erpnext/erpnext__tree-master-renaming.md -->
---
title: "Tree Master Renaming\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/tree-master-renaming"
updated: "2026-03-04"
---


**There are various documents in ERPNext which are maintained in a tree structure.**

Read about [managing tree structures](/erpnext/managing-tree-structure-masters.html) to learn more.

Following are the steps to be followed for renaming the ID of a master which is maintained in a tree structure. Let's rename an Account for the instance.

* **Step 1:** Go to the Tree View of the Document

* **Step 2:** Go to the node of the Document which you wish to rename

 When you click on that node, you will have an option to 'Rename' the document.

 [Screenshot on the live page: Tree Master Renaming]

* **Step 3:** Rename Account

 When you click on rename, a box will pop-up wherein you will be allowed to rename the document.

 [Screenshot on the live page: Tree Master Renaming]

<!-- page: erpnext/erpnext__twitter-settings.md -->
---
title: "Twitter Settings | ERPNext Documentation"
description: "Configure the legacy Twitter integration settings in ERPNext and understand current availability limitations."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/twitter-settings"
updated: "2026-07-23"
---

> Note: This integration doesn't work anymore due to Twitter's API changes. This has been removed from ERPNext starting from v15.

Twitter related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

- How to set up Twitter App

You must have Twitter App for your company. ERPNext interacts with this App for sharing Tweet.

### Create Twitter Developer App

Create App by link [https://developer.twitter.com/](https://developer.twitter.com/) and check that the App has **Read and write** Access permission. 

[Screenshot on the live page: Twitter App Permission]

### Configure Callback URL

- Select your App and go to **App Details**.
- Then go to **Edit** and click **Edit Details**.
- Add your website URL in **Callback URLs** like: https://{yoursite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback
- Click **Save** to make changes.

[Screenshot on the live page: Twitter App Callback URL]

- How to set up Twitter Settings

To access Twitter Settings, go to:

> Home > CRM > Settings > Twitter Settings

[Screenshot on the live page: Twitter Settings]

### API Key and API Key Secret

You get **API Key** and **API Key Secret** from your Twitter Developer account go to:

> [https://developer.twitter.com/](https://developer.twitter.com/) > My Apps > {Your App} > Keys and tokens

[Screenshot on the live page: Twitter Keys Tokens]

Once you save the doc by filling **API Key** and **API Key Secret** it will redirect to Twitter's sign-in page by providing valid Twitter credentials and clicking **Authorize app**, the member approves your application's request to access their member data and interact with Twitter. 

[Screenshot on the live page: Twitter Authorize App]
