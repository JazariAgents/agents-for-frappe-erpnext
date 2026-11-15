<!-- Frappe documentation: erpnext, part 6 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__applying-discount.md -->
---
title: "Apply Discounts to Sales Transactions | ERPNext Documentation"
description: "Apply item-level and transaction-level discounts in ERPNext and understand how discounts affect net rates, taxes, totals, and accounting."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/applying-discount"
updated: "2026-07-25"
---

ERPNext supports discounts on an individual item or on the transaction total. Use a manual discount for a one-off commercial decision. Use a [Pricing Rule](/erpnext/pricing-rule), [Promotional Scheme](/erpnext/promotional-scheme), or [Coupon Code](/erpnext/coupon-code) when eligibility should be evaluated automatically.

## Before you begin

Confirm:

- The Item has an applicable [Item Price](/erpnext/item-price).
- The transaction uses the intended [Price List](/erpnext/price-lists).
- The user may edit discount fields.
- Your tax and discount-accounting policy is configured.

## Apply a discount to one item

1. Create a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice).
2. Add the Item.
3. Select the highlighted pencil icon to open the full row editor.
4. Expand **Discount and Margin**.
5. Enter either **Discount (%)** or **Discount Amount**.
6. Review the resulting Rate, Net Rate, and Amount.
7. Save.

![A Sales Order item row with the pencil icon highlighted.](https://novacompanies.m.frappe.cloud/files/discount-item-pencil.png)

![The item row editor with Discount Percentage and Discount Amount visible.](https://novacompanies.m.frappe.cloud/files/discount-item-fields-v2c94055.png)

Item-level discounts are calculated against the Price List Rate. Use them when different lines require different discounts.

## Apply an additional discount to the transaction

1. Open the **Additional Discount** section.
2. Set **Apply Additional Discount On** to Net Total or Grand Total.
3. Enter an **Additional Discount Percentage** or **Additional Discount Amount**.
4. Review taxes, Net Total, Grand Total, and rounding before submission.

![The expanded Additional Discount section with the calculation basis and percentage visible.](https://novacompanies.m.frappe.cloud/files/discount-additional-section-v2e41c13.png)

### Discount on Net Total

ERPNext distributes the discount across eligible item net values before calculating totals. This changes item Net Rate and Net Amount, which can also change taxes calculated on those values.

### Discount on Grand Total

ERPNext applies the discount with reference to the total after taxes and charges. The system recalculates the relevant item and tax amounts so the document remains internally consistent.

Test the result with your actual tax templates. Inclusive taxes, charge types, rounding, and accounting configuration can affect the displayed breakdown.

## Choose the right discount method


| Requirement                                         | Recommended method                      |
| --------------------------------------------------- | --------------------------------------- |
| One item needs a one-time reduction                 | Item Discount (%) or Discount Amount    |
| The complete transaction needs a one-time reduction | Additional Discount                     |
| A condition should apply automatically              | Pricing Rule                            |
| Several quantity or amount slabs are required       | Promotional Scheme                      |
| A website shopper enters a code                     | Coupon Code                             |
| A free item is offered                              | Product Discount Pricing Rule           |
| A sales price needs a markup                        | [Adding Margin](/erpnext/adding-margin) |


## Discount accounting

By default, a discount changes the net revenue represented by item lines. If your accounting policy requires discounts to be posted separately, review **Enable Discount Accounting for Selling** in [Selling Settings](/erpnext/selling-settings) and configure the required accounts.

Confirm the resulting General Ledger entries in a test transaction before adopting the setting. Do not assume that a visual discount field always posts to a separate discount account.

## Troubleshooting


| Problem                                      | What to check                                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Discount fields are unavailable              | Open the child-row editor and confirm user permissions                                         |
| A manual value is replaced                   | Review Pricing Rules and re-fetch behavior                                                     |
| The final total is unexpected                | Check whether the discount applies on Net Total or Grand Total, then review taxes and rounding |
| The document is discounted twice             | Look for an automatic Pricing Rule plus a manual item or additional discount                   |
| Ledger entries do not use a discount account | Review discount-accounting settings and account configuration                                  |


## Frequently asked questions

### Can I apply both an item discount and an additional discount?

Yes. ERPNext applies both, so review the effective discount and approval policy carefully.

### Can I enter a fixed discount instead of a percentage?

Yes. Item rows and the Additional Discount section support amount-based discounts where available.

### Does a discount change the Price List Rate?

No. Price List Rate remains the reference rate. The transaction's Rate and Net Rate reflect the discount.

### Can ERPNext apply discounts automatically?

Yes. Use Pricing Rules or Promotional Schemes for repeatable conditions.

## Related topics

- [Pricing Rule](/erpnext/pricing-rule)
- [Promotional Scheme](/erpnext/promotional-scheme)
- [Coupon Code](/erpnext/coupon-code)
- [Adding Margin](/erpnext/adding-margin)
- [Selling Settings](/erpnext/selling-settings)

<!-- page: erpnext/erpnext__appointment-booking-settings.md -->
---
title: "Appointment Booking Settings | ERPNext Documentation"
description: "Configure ERPNext Appointment Booking Settings for availability, calendar scheduling, and customer bookings."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/appointment-booking-settings"
updated: "2026-07-23"
---

You can find all settings related to booking appointments in Appointment Booking Settings.

![Appointment Booking Settings](/files/appointment-booking-settings.png)

## Enable Appointment scheduling

This checkbox will enable appointment scheduling and also enable the /book_appointment Route for website users (your customers). Your customers will see a portal view. To know more, visit the [Appointment Page](/erpnext/appointment)

## Agent Details

In this section, you can add details about agents, such as their working hours and holidays.

### Availability of Slots

Here you can set the timing in which your agents are available to attend an appointment. This is set per day of the week. Each row represents a continuous block of time, you can have multiple entries for each day of the week.

For example if your agents work Monday to Friday, 9am to 5pm but with a lunch break at 1.30 for half and hour. You will need to create two entries for each day. One from 9am to 1.30pm and another from 2pm to 5pm.

### Agents

This is the list of agents which will be **autoassigned** to appointments. The number of appointments which can exist in one timeslot also depends upon the number employees in this list.

### Holiday list

You can link a (holiday list)[[https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list]](https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list]) here to apply to the appointment schedule. If the day is a holiday, scheduling an appointment on that day won't be allowed.

## Appointment Details

This section contains details about the appointment themselves.

### Appointment Duration in minutes

The duration of appointment in minutes. This is used to calculate appointment timeslots for the web portal. Changing this does not affect the appointments created before the change.

### Notify Via Email

Enabling this checkbox will send an email to the participants of the appointments i.e. your employee and the customer on the day of the appointment. Changing this checkbox does not affect the appointments created before the change.

### Number of days appointment can be books in advance

This is the number of days the appointment can be booked in advance. If the Holiday List provided above ends before the date calculated using this number, appointment scheduling will be stopped at the end of holiday list end.

## Success settings

### Success Redirect URL

This is the URL where the user will be redirected on creation of successful appointment creation via Web Portal. This redirect will not occur when creating appointments from within Desk UI.  
Leave blank for home. This is relative to site URL, for example "about" will redirect to "[https://yoursitename.com/about](https://yoursitename.com/about)"

<!-- page: erpnext/erpnext__appointment.md -->
---
title: "Appointment | ERPNext Documentation"
description: "Learn how to schedule and manage customer Appointments in ERPNext CRM."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/appointment"
updated: "2026-07-23"
---

**An appointment is a prearranged meeting between a Lead and an Employee of your Company.**

Appointment document type can be used to schedule and manage interaction with a [Lead](/erpnext/lead) or an [Opportunity](/erpnext/opportunity).

To access Appointment list, go to:

> Home > CRM > Sales Pipeline > Appointment

## Prerequisites

- [Appointment Booking Settings](/erpnext/appointment-booking-settings)
- [Holiday List](/hr/holiday-list)
- [Employee](/hr/employee)
- [Lead](/erpnext/lead)
- [Email](/erpnext/email-account)

## How to create an Appointment

- Go to Appointment list, select New
- Select scheduled time of the appointment
- Enter customer details
- In linked documents, if you have already created a Lead for the Customer you can set it here. Otherwise the system will automatically create a new lead with the customer details from previous step.
- Save.[New Appointment](/files/new-appointment.png)

### Creating appointments via website

Your Customers/Leads can create appointment using the webpage yoursitename.com/book_appointment.

First they need to set a date, time.

![Appointment Webform](/files/appointment-webform.png)

Then, add more details:

![Appointment Details](/files/appointment-details.png)

It'll match the customer email with leads in the system and if one is found, it is linked with the document.  
If no lead is found, the appointment is marked as "Unverified" and an email is sent to the customer to confirm their email

## Features

### Autoassign

Appointments are automatically assigned to employees as per the Agents list in [Appointment Booking Settings](/erpnext/appointment-booking-settings). The agent with the least number of assignments for the day of the appointment and who is free in the scheduled time is assigned to the appointment.

### Email confirmation

If there is no matching lead in your system, an email will be sent to the email address in the appointment to confirm if the email address is valid. Upon confirmation, a new Lead will also be created in the system along with the Appointment.

<!-- page: erpnext/erpnext__asset-capitalization.md -->
---
title: "Asset Capitalization | ERPNext Documentation"
description: "Combine stock, existing assets, and service costs into a new or composite ERPNext Asset."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-capitalization"
updated: "2026-08-15"
---

Imagine Nova Industries builds a testing machine using purchased components, technician time, and installation services. During construction, those costs are collected separately. Once the machine is ready, the company needs to combine the qualifying costs into one fixed asset.



Asset Capitalization gathers those costs and transfers them to the completed Asset. It shows how the final value was built and prevents the company from treating a long-term asset as an immediate operating expense.

## Before you begin

Confirm the target fixed-asset Item and category, source assets, available stock, service expense accounts, Finance Book, posting date, and capitalization policy.

## Define the target

1. Create an Asset Capitalization.
2. Select the company and posting date.
3. Choose a target Item and enter a recognizable target Asset Name, or select an eligible composite target Asset.
4. Select the Finance Book when required.

![Target Asset details in ERPNext Asset Capitalization](https://novacompanies.m.frappe.cloud/files/19-asset-capitalization-target.png)

## Add source costs

Add stock items, consumed assets, and service expenses. The example combines an existing conveyor with setup services. Use the pencil icon whenever a child row needs account, warehouse, quantity, rate, or cost-center detail.

![Consumed asset and service cost tables in Asset Capitalization](https://novacompanies.m.frappe.cloud/files/20-asset-capitalization-costs.png)

## Submit and verify

ERPNext reduces or updates the source values according to the transaction and capitalizes the total into the target. Verify the target Asset, source Asset statuses, stock impact, Journal Entry or Stock Ledger effect, and future depreciation schedule.

![Asset report used to verify capitalized value](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### The target Asset is not eligible

A selected existing target may need to be a Composite Asset. Otherwise create a new target from the fixed-asset Item.

### A service row cannot be saved

Provide the Item, expense account, quantity, rate, UOM, and cost center required by the row.

### Total value is zero

Add valid source rows and allow ERPNext to calculate their amounts before submission.

## Frequently asked questions

### Can I capitalize only services?

A valid capitalization can include qualifying services, but the target and accounting treatment must still satisfy the organization's policy.

### Can an existing Asset be consumed?

In ERPNext, yes, through the consumed-assets table when the workflow and target asset type permit it.

### Does capitalization immediately start depreciation?

Depreciation follows the target Asset's available-for-use date and Finance Book schedule.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-category.md -->
---
title: "Asset Category | ERPNext Documentation"
description: "Configure ERPNext Asset Categories with depreciation defaults, Finance Books, and company-specific fixed-asset accounts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-category"
updated: "2026-08-15"
---

Imagine Nova Industries buys 100 employee laptops over the next two years. If the accountant has to choose the useful life, depreciation method, and ledger accounts separately for every laptop, the records may become inconsistent and mistakes will be hard to find.



An Asset Category solves this by storing one reusable accounting policy for similar assets. Nova Industries can create an **IT Equipment** category once, then use the same depreciation and account defaults for every laptop added later.

## Before you begin

Confirm the company [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) contains a fixed-asset account, accumulated depreciation account, depreciation expense account, and capital work in progress account when CWIP is used. Create any required [Finance Books](https://docs.frappe.io/erpnext/finance-book) first.

## Create an Asset Category

1. Open **Asset Category** and select **Add Asset Category**.
2. Enter a clear name such as **IT Equipment** or **Production Equipment**.
3. Enable **Capital Work in Progress Accounting** when purchases should remain in CWIP until the asset becomes available for use.
4. Enable **Non Depreciable Category** only for categories such as land where depreciation does not apply.

![Asset Category depreciation options for IT Equipment](https://novacompanies.m.frappe.cloud/files/02-asset-category-overview.png)

## Set depreciation defaults by Finance Book

Add one row for every reporting basis you need. Nova Industries uses Straight Line for Statutory Reporting and Double Declining Balance for Management Reporting. Open the row editor with the pencil icon when you need fields that are not visible in the grid.

![Finance Book depreciation defaults in an ERPNext Asset Category](https://novacompanies.m.frappe.cloud/files/03-asset-category-finance-books.png)


| Field                             | What it means                                                              |
| --------------------------------- | -------------------------------------------------------------------------- |
| **Finance Book**                  | The reporting basis that owns this depreciation policy.                    |
| **Depreciation Method**           | How ERPNext spreads the depreciable value.                                 |
| **Frequency**                     | Months between scheduled depreciation entries.                             |
| **Total Number of Depreciations** | Number of scheduled postings across the useful life.                       |
| **Salvage Value Percentage**      | Expected residual value at the end of useful life.                         |
| **Daily Pro Rata**                | Calculates depreciation by actual days rather than equal periodic amounts. |
| **Shift Based**                   | Allows the depreciation amount to follow machine utilization by shift.     |


## Set company accounts

Each company row determines where acquisition, depreciation, and CWIP entries post. Do not use an inventory account as the Fixed Asset Account.

![Company accounting defaults for an ERPNext Asset Category](https://novacompanies.m.frappe.cloud/files/04-asset-category-accounts.png)


| Field                                | What it means                                                 |
| ------------------------------------ | ------------------------------------------------------------- |
| **Fixed Asset Account**              | Balance Sheet account that holds the capitalized asset value. |
| **Accumulated Depreciation Account** | Contra-asset account that accumulates depreciation.           |
| **Depreciation Expense Account**     | Profit and Loss account charged when depreciation is booked.  |
| **Capital Work in Progress Account** | Temporary asset account used before capitalization.           |


## Troubleshooting

### The Asset has the wrong depreciation defaults

Correct the category for future assets. For an existing draft Asset, reload or update the Finance Book rows before submission.

### ERPNext asks for an account during purchase or capitalization

Check that the category contains an Accounts row for the transaction company and that every linked account belongs to that company.

## Frequently asked questions

### Can two categories use the same accounts?

In ERPNext, yes. Categories may share accounts while keeping different useful lives or depreciation methods.

### Can the same category have two Finance Books?

In ERPNext, yes. Add one row per Finance Book when statutory and management depreciation differ.

### Does changing a category rewrite submitted Asset schedules?

Do not assume it will. Review affected Asset and Asset Depreciation Schedule records explicitly before relying on new defaults.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-depreciation.md -->
---
title: "Depreciation | ERPNext Documentation"
description: "Understand how ERPNext calculates, schedules, and posts fixed-asset depreciation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-depreciation"
updated: "2026-08-15"
---

Imagine you are an accountant at Nova Industries and your team buys laptops for $60,000. Would you show the full $60,000 as an expense in the first year even though the laptops are expected to be used for five years? That would make the first year's expense look unusually high and the next four years look too low.



Depreciation spreads the cost across the periods in which the assets are used. ERPNext creates a schedule and posts part of the cost at each interval, so the accounts show a more realistic expense and the remaining value of the laptops.

## Depreciation methods in brief

The method decides how quickly the asset's cost becomes an expense. Assume an asset costs $50,000, should be worth $5,000 at the end of five years, and therefore has a depreciable value of $45,000.


| Method                       | How the expense is spread                                                | When it is useful                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Straight Line**            | Spreads $45,000 evenly, or $9,000 per year for five years.               | The asset provides a similar benefit each year, such as office furniture.                               |
| **Double Declining Balance** | Records a larger expense in the early years and a smaller expense later. | The asset loses value or productivity quickly when new, such as some machinery or technology equipment. |
| **Written Down Value**       | Applies a fixed percentage to the asset's opening book value each year.  | The accounting or tax policy specifies depreciation as a percentage of carrying value.                  |
| **Manual**                   | Uses the dates and amounts entered by the accountant.                    | A contract, valuation, or special policy requires a custom schedule.                                    |


See [Depreciation Methods](https://docs.frappe.io/erpnext/asset-depreciation-methods) for worked calculations and year-by-year comparisons.

## Calculation inputs


| Field                                | What it means                                         |
| ------------------------------------ | ----------------------------------------------------- |
| **Net Purchase Amount**              | Starting capitalized value.                           |
| **Expected Value After Useful Life** | Residual amount not depreciated.                      |
| **Depreciable Value**                | Net purchase amount less expected residual value.     |
| **Method**                           | Pattern used to allocate depreciation.                |
| **Frequency**                        | Months between entries.                               |
| **Number of Depreciations**          | Number of scheduled postings.                         |
| **Available for Use Date**           | Operational start date that controls schedule timing. |


## Ledger impact

A submitted depreciation entry debits Depreciation Expense and credits Accumulated Depreciation. The original fixed-asset cost remains visible while accumulated depreciation grows.



The submitted schedule below belongs to Nova Industries' $48,000 NovaPack labeler. Each $760 monthly row has produced a linked depreciation Journal Entry, while future rows remain unposted.

![Submitted Asset Depreciation Schedule with posted Journal Entries](https://novacompanies.m.frappe.cloud/files/26-asset-depreciation-schedule-v2.png)

The Asset Depreciation Ledger then shows how the monthly expense increases accumulated depreciation and reduces the asset's carrying value.

![Asset Depreciation Ledger with seven posted entries](https://novacompanies.m.frappe.cloud/files/22-asset-depreciation-ledger-v2.png)

## Troubleshooting

### No depreciation schedule was created

Confirm Calculate Depreciation is enabled and at least one complete Finance Book row exists.

### A scheduled entry did not post

Check Accounts Settings, open periods, account defaults, posting permissions, and the schedule's posting status.

## Frequently asked questions

### Does depreciation start on the purchase date?

Not necessarily. It normally follows the Available for Use Date and schedule configuration.

### Can I post depreciation manually?

Use the Manual method or manage entries deliberately when automatic schedules do not match the policy.

### Does depreciation change inventory value?

Fixed-asset depreciation affects fixed-asset accounting, not stock valuation.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-location.md -->
---
title: "Asset Location | ERPNext Documentation"
description: "Build an ERPNext Asset Location tree and use it to track the physical position of company assets."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-location"
updated: "2026-08-15"
---

Imagine a Nova Industries employee reports that a company laptop is missing. The Asset record proves that the company owns it, but the support team still needs to know whether it was last kept at Nova Headquarters, sent to the Service Workshop, or assigned to another office.



Asset Locations create a simple map of where company assets are kept. When the location is updated through an Asset Movement, the team can find equipment faster and can also see where it was kept earlier.

## Create the location tree

1. Open **Asset Location** in Tree view.
2. Create a group such as **Nova Facilities**.
3. Add operational locations such as **Nova Headquarters**, **Packaging Floor**, and **Service Workshop** below it.
4. Use [Asset Movement](https://docs.frappe.io/erpnext/asset-movement) when an asset changes location so the history remains auditable.

![ERPNext Asset Location tree for Nova Industries facilities](https://novacompanies.m.frappe.cloud/files/05-asset-location-tree.png)


| Field                      | What it means                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Location Name**          | The name users will select on Asset and Asset Movement records.                                                             |
| **Parent Location**        | The group under which the location appears.                                                                                 |
| **Is Group**               | Allows the location to contain child locations. Do not assign an asset to a broad group when a usable leaf location exists. |
| **Area and UOM**           | Optional physical area information.                                                                                         |
| **Latitude and Longitude** | Optional coordinates for map-based identification.                                                                          |


## Keep locations useful

Choose one consistent level of detail. For office assets, a site or floor may be enough. For production equipment, a line or work area may be more useful. When a site closes, move its assets first, then stop using the old location rather than erasing history.

## Troubleshooting

### A new location does not appear in the Link field

Confirm it is saved as a usable location and not only as an unintended group. Reload the form after changing the tree.

### The Asset still shows the old location

Submit the Asset Movement. Saving a draft movement does not complete the transfer.

## Frequently asked questions

### Is Asset Location the same as Warehouse?

In ERPNext, no. Warehouse tracks inventory quantities. Asset Location tracks the physical position of fixed assets.

### Can an asset be assigned to an employee and a location?

In ERPNext, yes. Asset Movement can track custody and location together, depending on the selected purpose.

### Does a location change affect the ledger?

In ERPNext, no. A location transfer is operational and does not change asset value.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance-log.md -->
---
title: "Asset Maintenance Log | ERPNext Documentation"
description: "Complete ERPNext Asset Maintenance Logs with work performed, dates, status, and certificates."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance-log"
updated: "2026-08-15"
---

Imagine a technician completes the monthly inspection of a Nova Industries packaging machine. The schedule says the work was due, but the company still needs proof of what was done, when it was completed, and whether the machine had a problem.



An Asset Maintenance Log records the actual maintenance event. It turns a planned task into a dated service history that the operations and audit teams can check later.

## Open the planned log

Use the Maintenance Log section of the [Asset Maintenance](https://docs.frappe.io/erpnext/asset-maintenance) record or open the Asset Maintenance Log list.

![Planned Asset Maintenance Logs in ERPNext](https://novacompanies.m.frappe.cloud/files/13-maintenance-log-list.png)

## Complete the log

1. Confirm the Asset, task, due date, and assignee.
2. Change status to **Completed** after the work is actually finished.
3. Enter the completion date and actions performed.
4. Attach the certificate when the task requires one.
5. Save the log and review the next due date on the maintenance plan.

![Maintenance plan linked to its recurring logs](https://novacompanies.m.frappe.cloud/files/11-asset-maintenance-plan.png)


| Field         | What it means                                                        |
| ------------- | -------------------------------------------------------------------- |
| **Planned**   | Work is scheduled but not complete.                                  |
| **Completed** | Work and required evidence have been recorded.                       |
| **Overdue**   | The due date passed without completion.                              |
| **Cancelled** | The occurrence will not be performed and the reason should be clear. |


## Troubleshooting

### The log cannot be marked complete

Check required completion date, certificate, and actions fields for the task.

### The next due date is wrong

Review the parent maintenance task's periodicity and the last completion date.

## Frequently asked questions

### Should I create logs manually?

Scheduled plans normally create them. Manual logs can be used for exceptional maintenance when the relationship remains clear.

### Can a completed log be edited?

Follow the document's edit rules and retain audit history. Do not overwrite evidence casually.

### Does a log post to the ledger?

In ERPNext, no. It is an operational record. Repair invoices or capitalized repair costs create accounting effects.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance-team.md -->
---
title: "Asset Maintenance Team | ERPNext Documentation"
description: "Create an ERPNext Asset Maintenance Team with a manager, members, and roles."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance-team"
updated: "2026-08-15"
---

Imagine Nova Industries has electricians, IT technicians, and machine specialists. When a laptop or production machine needs work, assigning the wrong person wastes time and may leave the real problem unresolved.



An Asset Maintenance Team groups the people who can perform a type of maintenance. The team can then be selected on a maintenance plan so everyone knows who is responsible for each scheduled task.

## Create a team

1. Open **Asset Maintenance Team** and select **Add**.
2. Enter a team name and company.
3. Select a Maintenance Manager.
4. Add members and their maintenance roles.
5. Save, then use the team in [Asset Maintenance](https://docs.frappe.io/erpnext/asset-maintenance) plans.

![Nova Facilities Team in ERPNext Asset Maintenance](https://novacompanies.m.frappe.cloud/files/10-maintenance-team.png)


| Field                   | What it means                                                   |
| ----------------------- | --------------------------------------------------------------- |
| **Maintenance Manager** | User who supervises the plan.                                   |
| **Team Member**         | User who can be assigned maintenance work.                      |
| **Maintenance Role**    | Role used to describe or authorize the member's responsibility. |
| **Company**             | Company whose assets the team maintains.                        |


## Troubleshooting

### A user cannot be selected as a member

Confirm the User is enabled and has access to the relevant company and Assets records.

### Tasks are assigned to the wrong person

Correct the task's Assign To field. The team defines available ownership but each task controls its assignee.

## Frequently asked questions

### Can the same user be in more than one team?

In ERPNext, yes, when that reflects operational responsibility.

### Does the team itself create tasks?

In ERPNext, no. The Asset Maintenance plan creates scheduled tasks and logs using the selected team.

### Can teams be company specific?

In ERPNext, yes. Keep the selected company aligned with the Assets the team will maintain.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-maintenance.md -->
---
title: "Asset Maintenance | ERPNext Documentation"
description: "Plan recurring preventive maintenance and calibration for ERPNext Assets."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-maintenance"
updated: "2026-08-15"
---

Imagine a Nova Industries packaging machine needs inspection every month and a belt replacement every six months. If the team depends on memory, a missed service could stop production and cost much more than the maintenance itself.



Asset Maintenance turns those recurring jobs into a planned schedule. It records what must be done, how often it should happen, and who is responsible, helping the team service equipment before it fails.

## Before you begin

Enable **Maintenance Required** on the Asset and create an [Asset Maintenance Team](https://docs.frappe.io/erpnext/asset-maintenance-team).

## Create a maintenance plan

1. Select the Asset and Maintenance Team.
2. Add a task with its type, start date, periodicity, assignee, and description.
3. Mark whether a certificate is required.
4. Save the plan. ERPNext creates planned [Asset Maintenance Logs](https://docs.frappe.io/erpnext/asset-maintenance-log) for the schedule.

![Preventive maintenance plan for a Nova Industries laptop](https://novacompanies.m.frappe.cloud/files/11-asset-maintenance-plan.png)

Use the pencil icon to open the complete child-row editor when the grid hides task fields.

![Pencil icon for the Asset Maintenance task row](https://novacompanies.m.frappe.cloud/files/12-maintenance-task-pencil.png)

## Follow the work

Open the generated log, record actions performed, add a certificate when required, and mark the work completed.

![ERPNext Asset Maintenance Log list](https://novacompanies.m.frappe.cloud/files/13-maintenance-log-list.png)

## Troubleshooting

### No maintenance logs were created

Check the start date, end date, periodicity, and assignee, then save the maintenance plan again.

### The task is overdue

Complete or cancel the correct log. Do not only change the plan because the historical occurrence still needs a result.

## Frequently asked questions

### Is preventive maintenance the same as repair?

In ERPNext, no. Maintenance is planned work. Asset Repair records a failure, downtime, repair cost, and possible capitalization.

### Can one Asset have several tasks?

In ERPNext, yes. Add separate rows for checks, calibration, cleaning, or certification.

### Does maintenance affect asset value?

Routine maintenance normally does not. A qualifying repair cost can be capitalized through the repair workflow.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-movement.md -->
---
title: "Asset Movement | ERPNext Documentation"
description: "Transfer, issue, or receive ERPNext Assets while preserving location and custody history."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-movement"
updated: "2026-08-15"
---

Imagine a laptop moves from Nova Industries' head office to the service workshop, then is issued to a new employee. The problem with editing the location directly is that it would show only where the laptop is now. It would not explain who moved it or where it was before.



Asset Movement records every transfer, issue, and receipt as a separate event. The latest submitted movement updates the asset's location or custodian while keeping the earlier movements available as history.

## Choose the purpose


| Field                  | What it means                                                     |
| ---------------------- | ----------------------------------------------------------------- |
| **Transfer**           | Moves an asset from one location to another.                      |
| **Issue**              | Assigns custody to an employee.                                   |
| **Receipt**            | Returns an issued asset from an employee.                         |
| **Transfer and Issue** | Moves the asset and assigns it to an employee in one transaction. |


## Create an Asset Movement

1. Select the company and purpose.
2. Set the transaction date and time.
3. Add the Asset and its source details.
4. Enter the target location or employee required by the purpose.
5. Submit the movement.

![Asset transfer from Nova Headquarters to Service Workshop](https://novacompanies.m.frappe.cloud/files/14-asset-movement-transfer.png)

Use the pencil icon to review all source, target, employee, and department fields in the child row.

![Asset Movement child-row pencil icon](https://novacompanies.m.frappe.cloud/files/15-asset-movement-pencil.png)

## Verify the result

Open the Asset or Asset list and confirm the current location and status reflect the submitted movement.

![Asset list used to verify current locations](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### The target location did not change

Confirm the Asset Movement was submitted and the correct Asset row was used.

### The movement asks for an employee

The selected purpose includes custody. Use Transfer when only the physical location changes.

## Frequently asked questions

### Can one movement contain several assets?

In ERPNext, yes. Add multiple rows when the assets share the same movement context.

### Does an Asset Movement affect the ledger?

In ERPNext, no. It changes custody and location, not asset value.

### Can I move an out-of-order asset?

Check the operational policy and linked repair state. The system record should match the real handoff.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__asset-repair.md -->
---
title: "Asset Repair | ERPNext Documentation"
description: "Record ERPNext Asset failures, repair work, downtime, costs, consumed items, and capitalization decisions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/asset-repair"
updated: "2026-08-15"
---

Imagine a Nova Industries inspection camera stops working. The team sends it to a repair vendor, pays for replacement parts, and receives it back three days later. The company needs to track the downtime and cost, and it must decide whether the repair is an expense or increases the asset's value.



Asset Repair records the failure, repair work, cost, and completion. It also connects qualifying capital repair costs to the asset when they extend its useful life or improve its capacity.

## Create an Asset Repair

1. Select the Asset and failure date.
2. Enter a clear description of the failure.
3. Save with status **Pending** while work is in progress.
4. Add supplier invoices or consumed stock items where applicable.
5. Record actions performed and completion date.

![Pending Asset Repair for a Nova Industries laptop](https://novacompanies.m.frappe.cloud/files/16-asset-repair-details.png)

## Record cost and capitalization

Routine repair is normally an expense. Enable **Capitalize Repair Cost** only when the cost meets the organization's capitalization policy and increases future economic benefit. If the repair extends useful life, enter the increase in asset life and review the depreciation schedule.

![Repair cost and capitalization fields in ERPNext](https://novacompanies.m.frappe.cloud/files/17-asset-repair-cost.png)

## Complete and verify

Set the repair to **Completed**, confirm downtime, and open the Asset. A pending failure can place the asset out of order; completion should restore the correct operating state.

![Asset status after repair workflow activity](https://novacompanies.m.frappe.cloud/files/01-assets-overview-list.png)

## Troubleshooting

### Repair cost remains zero

Link the relevant Purchase Invoices or consumed items and confirm their rates and amounts.

### The Asset remains Out of Order

Complete the repair and verify no other active repair keeps the asset unavailable.

### Capitalization did not update the schedule

Confirm the repair was submitted with capitalization enabled and review the linked value and schedule documents.

## Frequently asked questions

### Should every repair be capitalized?

In ERPNext, no. Capitalize only costs that meet the accounting policy. Routine repairs are usually expenses.

### Can repair consume stock items?

In ERPNext, yes. Add consumed parts so their cost is included and inventory is reduced through the supported workflow.

### Does Asset Repair replace maintenance logs?

In ERPNext, no. Maintenance logs record planned work. Repair records a failure and its financial or operational recovery.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)
