<!-- Frappe documentation: erpnext, part 12 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__buying-settings.md -->
---
title: "Buying Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying-settings"
updated: "2026-05-27"
---

ERPNext allows you to configure various settings and configurations that help streamline and automate the purchasing workflow.

## Naming Series and Price Defaults

[Screenshot on the live page: Screenshot 2024-08-29 at 1.23.09 PM]  

### 1. Supplier Naming By

When a Supplier is saved, system generates a unique identity or name for that Supplier which can be used to refer the Supplier in various Buying transactions.

If not configured otherwise, ERPNext uses the Supplier's Name as the unique name. If you want to identify Suppliers using names like SUPP-00001, SUPP-00002, or such other patterned series, select the value of Supplier Naming By as "Naming Series".

### 2. Default Supplier Group

Configure what should be the default value of Supplier Group when creating a new Supplier. For example, if most of your suppliers supply you hardware, you can set the default as 'Hardware'.

### 3. Default Buying Price List

Configure what should be the default Price List when creating a new Buying transaction, the default is set as 'Standard Buying'. Item prices will be fetched from this Price List. You can modify the 'Price List' by using the arrow at the right-end of the field to change the currency and country.

### 4. Action if Same Rate is Not Mentioned

It defines the action the should take when it encounters a purchase order, material request, or any other buying transaction where the same rate of an item is not mentioned.

There are two possible actions the user can take.

- **Stop**: The system will stop the transaction preventing the user from proceeding without specifying a rate. This ensures that all transactions have explicit rates mentioned, avoiding potential discrepancies.
- **Warn**: The system will allow the transaction happen but will display a warning message to alert the user that the same rate has not been mentioned.

### 5. Role Allowed to Override Stop Action

This setting specifies which user roles have the permission to override the "Stop" action in the buying transaction due to discrepancy in the rate.

## Transaction Settings

[Screenshot on the live page: Screenshot 2024-08-29 at 1.24.53 PM]  

### 1. Is Purchase Order Required for Purchase Invoice & Receipt Creation?

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice or a Purchase Receipt directly without creating a Purchase Order first.

If retail transactions are involved where the order happens offline, then Purchase Orders can be skipped. If you're accepting sample Items, you can directly create a Purchase Receipt to receive the Items to your Warehouse.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Order" checkbox in supplier master

### 2. Is Purchase Receipt Required for Purchase Invoice Creation?

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice without creating a Purchase Receipt first. In case the Item being transacted is a service, it'll not require a receipt, you can directly create an Invoice.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Receipt" checkbox in the supplier master

### 3. Blanket Order Allowance (%)

You can set the percentage you are allowed to order more against the Blanket Order Quantity. For example: If you have a Blanket Order of Quantity 100 units. and your Allowance is 10% then you are allowed to order 110 units.

### 4. Update frequency of Project

It indicates how often should Project be updated of Total Purchase Cost.

### 5. Maintain Same Rate Throughout Purchase Cycle

If this is enabled, ERPNext will validate whether an Item's price is changing in a Purchase Invoice or Purchase Receipt created from a Purchase Order, i.e. it will help you maintain the same rate throughout the purchase cycle.

You can configure the action that system should take if the same rate is not maintained in the "Action If Same Rate is Not Maintained" field:

- **Stop**: ERPNext will stop you from changing the price by throwing a validation error.
- **Warn**: The system will let you save the transaction but warn you with a message if the rate is changed.

Note: This field will only be visible if Maintain Same Rate Throughout Purchase Cycle is enabled.

### 6. Allow Item to be added multiple times in a transaction

When this checkbox is unchecked, an item cannot be added multiple times in the same Purchase Order. However, you can still explicitly change the quantity. This is a validation checkbox for preventing accidental purchase of the same item. This can be checked for specific use cases where there are multiple sources for the same material, for example in manufacturing.

### 7. Bill for Rejected Quantity in Purchase Invoice

If checked, Rejected Quantity will be included while making Purchase Invoice from Purchase Receipt.  



### 7.1 Set Valuation Rate for Rejected Materials

For rejected materials, the valuation rate is set to zero, and no accounting ledger entry is created for them in the Purchase Receipt. To apply a valuation rate and generate accounting entries for rejected materials, enable the 'Set Valuation Rate for Rejected Materials' option in Buying Settings. This option is only applicable when `Bill for Rejected Quantity in Purchase Invoice` has enabled in the Buying Settings.

[Screenshot on the live page]

##### 8. **Set Landed Cost Based on Purchase Invoice Rate**

If the 'Maintain Same Rate Throughout the Purchase Cycle' is disabled then this field shows in the buying settings. If user wants to adjust the product valuation as per the purchase invoice cost then this option needs to be enable.

How It Works

- Created Purchase Receipt for item A with rate as 100
- System has booked Stock In Hand with 100 rate
- After 2 days, user has created purchase invoice against the above purchase receipt
- After 2 days because of change in exchange rate the rate in the invoice changed to 150
- Now purchase receipt has rate 100 where as Purchase invoice has rate 150
- If you want to adjust the Stock In Hand with Purchase invoice Rate (150) then enable "Set Landed Cost Based on Purchase Invoice Rate".

Note: on submission of the purchase invoice, system creates the repost item valuation record to update the cost of the purchase receipt. User has to wait to complete the repost item valuation to see the impact of the invoice cost on the stock in hand.

### 9. **Disable Last Purchase Rate**

It prevents the system from automatically using the rate from the last purchase transaction when creating new purchase orders or transactions.

### 10. Use Transaction Date Exchange Rate

While making Purchase Invoice from Purchase Order, use Exchange Rate on Invoice's transaction date rather than inheriting it from Purchase Order. Only applies for Purchase Invoice.

### 11. Over Order Allowance (%)

The percentage by which you are allowed to order more on a Purchase Order than the quantity requested on the originating Material Request. For example, if the Material Request has 100 units and the allowance is 10%, you can order up to 110 units.

## Subcontracting Settings

[Screenshot on the live page: Screenshot 2024-08-29 at 1.32.06 PM]  

### 1. Backflush Raw Materials of Subcontract Based On

1. BOM: system will consume raw materials in the subcontracting receipt as per the FG BOM
2. Material Transferred for Subcontract: system will consume raw materials based on the materials transferred against the Subcontracting Order. If no stock transferred then no materials will be consume at the time of Subcontracting Receipt.

### 2. **Auto Create Subcontracting Order**

System will auto create the subcontracting order in a Draft state on submission of the purchase order which has "Is Subcontracted" enabled.

### 3. **Auto Create Purchase Receipt**

System will auto create the purchase receipt for the service items in a Draft state on submission of the subcontracting receipt.

### 4. Over Transfer Allowance (%)

It is the percentage you are allowed to transfer more against the quantity ordered. For example: If you have ordered 100 units. and your Allowance is 10% then you are allowed to transfer 110 units.

<!-- page: erpnext/erpnext__buying.md -->
---
title: "Introduction to Buying Module"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying"
updated: "2026-02-28"
---

The Buying module in ERPNext is designed to manage procurement processes and optimise supplier relationships. 

- **Requests for Quotation (RFQs)**: Evaluate quotations from suppliers to make informed purchasing decisions.
- **Supplier Management**: Maintain detailed records of suppliers, including contact details, terms, and performance metrics.
- **Purchase Orders**: Create and track purchase orders to ensure timely and accurate order fulfillment.
- **Purchase Invoices**: Process and manage invoices from suppliers, including payment handling.
- **Stock Management**: Update inventory levels and manage stock replenishment.

The Buying module helps businesses streamline their procurement activities, control purchasing costs, and strengthen supplier relationships.



Watch this [Frappe School Course on Procurement](https://school.frappe.io/lms/courses/procurement)  to learn more.

<!-- page: erpnext/erpnext__buying_reports.md -->
---
title: "Buying Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/buying_reports"
updated: "2026-04-03"
---

Data pertaining to purchases made by an organization can be analyzed and visualized through various reports available in the buying modules. Normally, each report has three sections: Filter toolbar, a chart, and data. Changes in the filters and selections are immediately reflected in the chart.

## Purchase Analytics

To access the report, go to:

> Home > Buying > Key Reports > Purchase Analytics

[Screenshot on the live page]

Through the Purchase Analytics report, the purchase-related data against the supplier, supplier groups, items and item group can be analyzed over a given period and frequency.

## Purchase Order Analysis

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Analysis

[Screenshot on the live page]

This report is helpful in analyzing the items and their billing status in a purchase order over a given period.

## Supplier-Wise Sales Analytics

To access the report, go to:

> Home > Buying > Key Reports > Sales-Wise Sales Analytics

[Screenshot on the live page]

This report provides extensive data on different items purchased from the suppliers.

## Items to Order and Receive

To access the report, go to:

> Home > Buying > Key Reports > Items to Order and Receive

[Screenshot on the live page]

This report visualizes and shows data for the purchase requests created.

## Purchase Order Trends

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Trends

[Screenshot on the live page]

Through this report, the trends for purchase orders for a given financial year can be visualized. The trend can be grouped based on Suppliers, Supplier Group, Item, Item Group, and Project.

## Procurement Tracker

To access the report, go to:

> Home > Buying > Key Reports > Purchase Order Trends

[Screenshot on the live page]

This report presents extensive purchase-related data including material requests, purchase orders created for the items.

## Other Reports

To access, go to:

> Home > Buying > Other Reports

In other reports section, the following reports can be accessed:

1. Items To Be Requested
2. Item-Wise Purchase History
3. Purchase Receipt Trends
4. Purchase Invoice Trends
5. Subcontracted Item To Be Received
6. Supplier Quotation

<!-- page: erpnext/erpnext__calculate-incentive-for-sales-team.md -->
---
title: "Calculate Incentive For Sales Team\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculate-incentive-for-sales-team"
updated: "2026-07-24"
---

ERPNext can calculate incentives for an internal sales team directly from the **Sales Team** child table on supported transactions. Each Sales Person receives a contribution percentage, contribution amount, commission rate, and calculated incentive.

The earlier documentation relied on an obsolete client script and legacy APIs. For standard percentage-based incentives, use the native Sales Person and Sales Team fields. Create custom logic only when the incentive policy cannot be represented by the standard calculation.

## Before you begin

Set up:

- An enabled [Sales Person](/erpnext/sales-person) for every eligible team member.
- A **Commission Rate** on each Sales Person.
- A written incentive policy that defines the qualifying transaction, contribution rules, approval point, returns, cancellations, and payment timing.
- User permissions to edit the Sales Team table on sales transactions.

Decide whether incentives are earned from a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), or [Sales Invoice](/erpnext/sales-invoice). Use the same event consistently so the same sale is not rewarded more than once.

## Set the Sales Person commission rate

1. Open the required Sales Person.
2. Enter the default **Commission Rate**.
3. Save.

ERPNext fetches this rate into new Sales Team rows. Review the policy before changing a rate because existing submitted transactions should retain their approved incentive basis.

## Add the Sales Team to a transaction

1. Open a supported sales transaction.
2. Select **More Info**.
3. Expand **Sales Team**.
4. Select **Add row**.
5. Choose the Sales Person and enter **Contribution (%)**.
6. Add other team members when the sale is shared.
7. Use the highlighted pencil icon to open the full child-row editor when needed.
8. Confirm that the contribution percentages total 100% when the full net total must be allocated.
9. Save.

[Screenshot on the live page: Sales Team contribution, commission rate, and incentives on a Sales Order]

In this example, Alex Morgan receives 60% of the net total and Jordan Lee receives 40%.

## How ERPNext calculates incentives

ERPNext calculates the contribution amount from the transaction's net total:

**Contribution to Net Total = Net Total × Contribution (%) ÷ 100**

It then applies the Sales Person's commission rate:

**Incentive = Contribution to Net Total × Commission Rate ÷ 100**

For a net total of $4,164:


| Sales Person | Contribution | Contribution amount | Commission rate | Incentive |
| ------------ | ------------ | ------------------- | --------------- | --------- |
| Alex Morgan  | 60%          | $2,498.40           | 2.5%            | $62.46    |
| Jordan Lee   | 40%          | $1,665.60           | 2%              | $33.31    |


The total calculated incentive is $95.77.

## Sales Team fields and what they mean


| Field                     | Meaning                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| Sales Person              | Individual receiving sales attribution and possible incentive        |
| Contribution (%)          | Share of the transaction credited to the Sales Person                |
| Contribution to Net Total | Currency value calculated from net total and contribution percentage |
| Commission Rate           | Rate fetched from the Sales Person master                            |
| Incentives                | Calculated or approved incentive amount for the row                  |


The Sales Team table is a child table. Selecting the pencil opens the full row editor for the chosen Sales Person.

## Submit and review the transaction

Before submission:

- Verify that the correct people are included.
- Check that contribution percentages match the approved split.
- Confirm the net total and commission rates.
- Review the calculated incentive amounts.

After submission, treat the Sales Team allocation as part of the transaction's audit trail. If the sale is cancelled, amended, returned, or credited, apply the incentive policy before paying or reversing an incentive.

Read [Amending Sales Order after Submit](/erpnext/amending-sales-order-after-submit) before changing a submitted order.

## Review team performance and incentives

Use [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions) and relevant sales reports to verify transaction attribution. Use [Sales Person Target Allocation](/erpnext/sales-person-target-allocation) when the organization also tracks quantity or amount targets by Fiscal Year and Item Group.

The incentive field records a transaction-level value. It does not automatically create a payroll component, salary slip, expense, payable, or payment.

For payroll-based settlement, define a controlled process with the HR and finance teams. A common approach is to review approved incentives for the period, then include the approved amount through a configured [Additional Salary](/hr/additional-salary) or another organization-approved payroll process in Frappe HR.

## When custom logic is needed

The native calculation suits a fixed commission rate applied to the credited net total. Customization may be needed for policies such as:

- Tiered rates after revenue thresholds.
- Rates based on gross profit or collected payment.
- Different rates by Item Group, territory, or customer segment.
- Incentives paid only after the return period.
- Team bonuses triggered by a common target.
- Caps, floors, clawbacks, or manager approval.

Document the policy before implementation. Prefer a maintained server-side customization or custom app with tests over an unversioned client script. Client-side calculations alone can be bypassed by imports, integrations, background jobs, or API-created transactions.

See [Server Script](/framework/user/en/desk/scripting/server-script) and [Custom App Development](/framework/user/en/tutorial/create-an-app) when technical customization is required.

## Accounting and payroll impact

Calculated incentives have no automatic accounting or payroll impact. Do not assume that saving or submitting the sales transaction pays the employee.

The settlement process should define:

1. Which submitted documents qualify.
2. Who reviews and approves the amounts.
3. How returns and cancellations are handled.
4. Which payroll or accounting document records the approved expense.
5. When payment occurs.
6. How paid amounts are reconciled with source transactions.

## Troubleshooting

### Commission Rate is zero

Open the Sales Person and enter the approved Commission Rate. Re-add or refresh the Sales Team row when the transaction does not fetch the updated value.

### Contribution amount is incorrect

Check the transaction net total and Contribution (%). Discounts, pricing rules, and taxes can make net total different from grand total.

### Contributions do not total 100%

Review every Sales Team row. Decide whether the unallocated percentage is intentional. For full allocation, correct the rows before submission.

### Incentive is not recalculated

Save the transaction after changing contribution or team members. Reopen the row and confirm the commission rate. Avoid manually overriding calculated values without approval.

### The incentive was paid before a return

Follow the organization's clawback or adjustment policy. Link the review to the [Sales Return](/erpnext/sales-return) and the original transaction.

## Frequently asked questions

### Is this the same as Sales Partner commission?

No. Sales Team incentives apply to Sales Persons. [Sales Commission](/erpnext/how-to-give-commission-to-sales-partner) covers external Sales Partners.

### Can several people share one sale?

Yes. Add several Sales Team rows and divide contribution among them.

### Does ERPNext pay the incentive automatically?

No. It calculates the transaction-level value only.

### Can the incentive be based on collected payment?

Not with the standard net-total calculation. Use a verified customization and finance-approved policy.

### Should incentives be calculated on Sales Orders or Sales Invoices?

Choose one qualifying event and apply it consistently. Sales Invoices are generally closer to recognized billing, while Sales Orders represent confirmed bookings.

## Related topics

- [Sales Person](/erpnext/sales-person)
- [Sales Persons in Sales Transactions](/erpnext/sales-persons-in-the-sales-transactions)
- [Sales Person Target Allocation](/erpnext/sales-person-target-allocation)

<!-- page: erpnext/erpnext__calculatin-freight-in-taxes-in-erpnext.md -->
---
title: "Calculating Freight in taxes in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculatin-freight-in-taxes-in-erpnext"
updated: "2026-03-02"
---

**Use case: To calculate freight forwarding charges with tax rate**
-------------------------------------------------------------------

  
When freight is supposed to be calculated in forwarding charges as a tax rate, we can follow the steps as below:   
* You can create a ledger in the taxes account specifically in Chart of Accounts, else you can consider GST tax account in the taxations for calculation of the Freight charges.

  
[Screenshot on the live page]  
* Now create an Item with the name : **Freight and Forwarding**

[Screenshot on the live page]  
* You can now create Purchase Invoice for the Supplier and add this item to calculate the Taxes related to the freight. You can set the freight tax based on the Net total or Item Quantity as per the company policy.

  
[Screenshot on the live page]   
  

<!-- page: erpnext/erpnext__calculation-of-valuation-rate-in-fifo-and-moving-average.md -->
---
title: "FIFO and Moving Average calculation difference"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average"
updated: "2026-03-02"
---

Valuation Rate of an item is calculated based on the total expense incurred to make the product available for sale like freight, labour, cost of raw materials, etc.

In ERPNext, Valuation Rate is calculated based on the valuation method selected for the particular item. 

An item can have either FIFO or Moving Average selected as a valuation method. 

Consider the following example to know how it impacts your stock:


```
| Date      | Transaction | Qty | Unit Cost |
| 1-4-2020  | Purchase    | 10  | 100       |
| 6-4-2020  | Purchase    | 20  | 120       |
| 10-4-2020 | Sale        | 15  | ?         |
```

  
Calculating Valuation Rate at the time of sale:

**As per FIFO:**

Since this is FIFO, we will consume quantities from the *earliest* transactions, therefore, to make a sale of 15 qty, we will take 10 qty from the first transaction and 5 qty from the second one. 

(10 * 100) + (5 * 120) = 1600, which leaves us 15 qty in stock at cost of 120 amounting to **1800**.

**As per Moving Average:**

In the Moving Average method, the value of an item is *recalculated* *every time* when an item is acquired. This is done by adding the cost of the newly acquired items to the existing inventory’s value and then dividing it by the total quantity available. 

((10 * 100) + (20 * 120)) / 30 = 113.33

To make a sale of 15 qty, we will directly multiply it by the average value we received just now. 

15 * 113.33 = 1700, which leaves us 15 qty in stock amounting to **1700**.

If you check, even though the quantity is same the stock value is different but both amounts to a total of 3400 only.  

<!-- page: erpnext/erpnext__campaign.md -->
---
title: "Campaign | ERPNext Documentation"
description: "Learn how to create and use Campaigns in ERPNext to organize marketing activity and measure generated leads and opportunities."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/campaign"
updated: "2026-07-23"
---

**A Campaign is a full-scale implementation of a sales strategy to promote a**  
**product or service.**

In ERPNext CRM, a campaign refers to a structured marketing initiative aimed at achieving specific business objectives, such as generating leads, increasing sales, or promoting brand awareness.

The Campaign feature allows users to plan, execute, and monitor marketing campaigns effectively within the CRM module. By leveraging the Campaign feature in ERPNext CRM, organizations can streamline their marketing efforts, target the right audience with personalized messages, track campaign performance, and ultimately drive business growth through effective marketing initiatives.

This is done in a market segment of a particular geographical area to achieve specified objectives.

To access Campaign, go to:

> Home > CRM > Campaign > Campaign

[Screenshot on the live page: Campaign]

## How to Create a Campaign

- Go to the Campaign list, select new.
- Enter a name for the campaign.
- Enter a description to describe what the campaign is about.
- Save.

## Features

### Tag Campaign in Lead, Opportunity, and Quotation

When a marketing campaign generates a lead or an opportunity, you can tag the campaign while creating the [Lead](/erpnext/lead) or [Opportunity](/erpnext/opportunity). You can also tag the campaign in [Quotation](/erpnext/quotation).

This helps in assessing the effectiveness of a marketing campaign by calculating the return on investment.

[Screenshot on the live page: Campaign in Lead]

### View Leads Generated by a Campaign

- select 'View Leads' button in the campaign.Campaign - View Leads (picture on the live page)
- You will see a filtered list of leads made against the campaign.
- You can also create new leads against the campaign by clicking on 'New'

Campaign - New Lead (picture on the live page)

### Set up email schedules for Email Campaigns

If you want to carry out a campaign using emails for your leads or contacts, [Email Campaign](/erpnext/email-campaign) serves the purpose.

You will have to set up a schedule for the campaign. select 'Add Row' to add an entry to the campaign schedule.

[Screenshot on the live page: Campaign Schedule]

- In **Email Template**, select an 'Email Template' which you would like to send via email to the lead or contact. You can create one as follows:

[Screenshot on the live page: Campaign - Email Template]

- In **Send After (days)**, specify the number of days after which the respective email should be sent. Using this field, the day on which email is to be sent is calculated relative to the **Start Date** of **Email Campaign**.

### Dashboard

The Campaign dashboard shows you all the Email Campaigns and Social Media Post linked to the Campaign. You can also create a new Email Campaign and Social Media Post from here.

[Screenshot on the live page: Campaign Dashboard]

## Related Topics

- [Lead](/erpnext/lead)
- [Opportunity](/erpnext/opportunity)
- [Quotation](/erpnext/quotation)
- [Email Campaign](/erpnext/email-campaign)

Next: [Email Campaign](/erpnext/email-campaign)

<!-- page: erpnext/erpnext__can-we-fetch-shipping-charges-based-items-value-or-weight-in-po.md -->
---
title: "Fetch shipping charges based item's value or weight "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/can-we-fetch-shipping-charges-based-items-value-or-weight-in-po"
updated: "2026-03-02"
---

In a Purchase order, we can fetch the **Shipping Charges** of an item based on its Value or weight.  
Go to **Shipping Rule list** --> **Calculate based on : Net Total or Net Weight** --> Select Shipping rule conditions --> Fill table  
[Screenshot on the live page]  
This way, while creating a PO, shipping charges will be fetched for the item based on item's weight or Value. 

<!-- page: erpnext/erpnext__capacity-planning-based-on-production-order.md -->
---
title: "Capacity Planning based on Production Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/capacity-planning-based-on-production-order"
updated: "2026-02-26"
---

Capacity Planning functionality helps you in tracking production jobs allocated on each Workstation.

[Screenshot on the live page]

Follow are the steps to use Capacity Planning Feature in your ERPNext account.

**Operations**

To add operations, go to: Manufacturing > Bill of Materials > Operations

**Workstation**

Add each Workstation in your ERPNext account from: Manufacturing > Bill of Materials > Workstation

In the Workstation master, you can define which operations will be performed on it, what are the cost associated with it, and what are the working hours of that Workstation.

**Bill of Materials (BOM)**

In a BOM, with the list of raw material needed, for manufacturing, you can also list operation and workstations through which those raw materials will be processed.

**Production Order**

On submission of Production Order, Timesheet for Operations. This helps you allocate production jobs on each Workstation, as well as you can update actual time taken for each Operation.

 

\--

**Question** : On Submission of Production Order, we are getting following error message.

[Screenshot on the live page]

**Answer** : Please check if you have updated Working Hours in the Workstation master? If not, then please update it and then try to submit Production Order. On submission of Production Order, Operations (as added in the BOM) are allocated on the workstation. Each operation should start and end on the same day. If a system is not able to schedule that operation in a day, then system request you to divide that Project, so that system can allocate smaller operations in a day. If you have update working hours in the Workstation, but still getting this issue, that because one of your operation is taking too long, and cannot be completed in a day. Please divide that operation into smaller operations, so that it can be allocated on Workstation and completed on the same day.

<!-- page: erpnext/erpnext__capacity-planning.md -->
---
title: "Capacity Planning based on Work Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/capacity-planning"
updated: "2026-02-26"
---

Capacity Planning functionality helps you in tracking production jobs allocated on each Workstation.

[Screenshot on the live page: Role Desk Permission]  


Follow are the steps to use Capacity Planning Feature in your ERPNext account.

1. Operations

To add operations, go to:

`Manufacturing -> Bill of Materials -> Operations`
2. Workstation

Add each Workstation in your ERPNext account from:

`Manufacturing -> Bill of Materials -> Workstation`

In the Workstation master, you can define which operations will be performed on it, what are the cost associated with it, and what are the working hours of that Workstation.
3. Bill of Materials (BOM):

In a BOM, with the list of raw material needed, for manufacturing, you can also list operation and workstations through which those raw materials will be processed.
4. Work Order:

On submission of Work Order, Timesheet for Operations. This helps you allocate production jobs on each Workstation, as well as you can update actual time taken for each Operation.

  
**Error due to Capacity Planning**

**Question:** On Submission of Work Order, we are getting following error message.

[Screenshot on the live page: Role Desk Permission]  


**Answer: **Please check if you have updated Working Hours in the Workstation master? If not, then please update it and then try to submit Work Order.

On submission of Work Order, Operations (as added in the BOM) are allocated on the workstation. Each operation should start and end on the same day. If a system is not able to schedule that operation in a day, then system request you to divide that Project, so that system can allocate smaller operations in a day.

If you have update working hours in the Workstation, but still getting this issue, that because one of your operation is taking too long, and cannot be completed in a day. Please divide that operation into smaller operations, so that it can be allocated on Workstation and completed on the same day.

  
**Avoid Working Hours of Workstation**

If you want to ignore above validation and allow scheduling of production job beyond the working hours of the Workstation, enable Overtime in the Manufacturing Settings.

[Screenshot on the live page: Role Desk Permission]  


If you want to complete disable Capacity Planning feature, in the Manufacturing Settings, check field "Disable Capacity Planning and Time Tracking".

<!-- page: erpnext/erpnext__cash-flow-report.md -->
---
title: "Cash Flow Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/cash-flow-report"
updated: "2026-08-14"
---

Nova Industries earned $109,440 in 2026, yet cash from operations fell by $117,866. The owner needs to understand where the profit went before approving more spending.



The Cash Flow report explains changes in cash and cash equivalents through operating, investing, and financing activities. It starts from accounting results and adjusts for non-cash items and working-capital movement. Use the [Profit and Loss Report](/erpnext/profit-and-loss-report) to measure earnings and the [Balance Sheet](/erpnext/balance-sheet) to review financial position.

## Run Cash Flow

1. Open **Accounting** and select **Cash Flow**.
2. Select **Nova Industries** and the required fiscal year or date range.
3. Choose periodicity and optional [Finance Book](/erpnext/finance-book), [Cost Center](/erpnext/cost-center), Project, Department, or [Accounting Dimension](/erpnext/accounting-dimensions).
4. Enable opening and closing balances when the cash reconciliation requires them.
5. Refresh and wait for totals, chart, and report sections to load.

[Screenshot on the live page: Loaded Nova Industries Cash Flow report showing negative operating cash flow]

## Interpret Nova's cash movement


| Line                          | Value     | Interpretation                                             |
| ----------------------------- | --------- | ---------------------------------------------------------- |
| Profit for the year           | $109,440  | Accounting profit before cash-flow adjustments.            |
| Change in Accounts Receivable | -$316,212 | Income was recognized, but much of it remains uncollected. |
| Change in Accounts Payable    | $184,293  | Unpaid supplier balances temporarily preserved cash.       |
| Net Cash from Operations      | -$117,866 | Core operations consumed cash despite positive profit.     |


The largest pressure is receivables. Nova should review [Accounts Receivable](/erpnext/accounts-receivable), prioritize collections, and verify old balances before committing to new cash expenditure. Review [Accounts Payable](/erpnext/accounts-payable) before using delayed supplier payments as a source of cash.

## Understand the three sections


| Section   | Typical movements                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------- |
| Operating | Profit, depreciation, receivables, payables, inventory, and taxes arising from ordinary operations. |
| Investing | Purchases and disposals of equipment, investments, and other long-term assets.                      |
| Financing | Owner capital, borrowings, repayments, dividends, and similar funding movements.                    |


## Trace a line to accounting evidence

Select an account or supporting value to inspect its [General Ledger](/erpnext/general-ledger) activity. Review source [Payment Entries](/erpnext/payment-entry) and approved [Journal Entries](/erpnext/journal-entry) when they explain a material movement. Working-capital lines are changes between reporting dates, so also compare the relevant Balance Sheet accounts and party reports.

[Screenshot on the live page: General Ledger report showing the accounting entries behind Cash Flow movements]

## Default and customised formats

The standard report classifies accounts using ERPNext's financial-statement logic. When the organisation needs approved labels or more precise classifications, configure [Customise Cash Flow Report](/erpnext/customise-cash-flow-report). A [Financial Report Template](/erpnext/financial-report-template) can control presentation where supported. Customisation changes classification and layout, not the underlying ledger entries.

## Troubleshooting

### Profit and operating cash flow differ sharply

Review receivables, payables, inventory, depreciation, taxes, and other non-cash or working-capital lines. The difference is often expected and should be explained, not forced to match.

### A cash movement is in the wrong section

Review the account's mapping and report configuration. Confirm whether a custom cash-flow format is enabled before changing any classification.

### Net change does not reconcile to cash balances

Match Company, dates, Finance Book, currency, dimensions, and opening or closing balance options. Look for omitted bank or cash accounts and overlapping custom mappings.

## Frequently asked questions

### Does positive profit guarantee positive cash flow?

Credit sales, inventory purchases, debt payments, asset purchases, and other timing differences can make cash flow negative while profit is positive.

### Is Accounts Payable growth always good for cash?

Unpaid bills preserve cash temporarily but create obligations and may harm supplier relationships. Interpret the change with due dates and payment plans.

### Does a report mapping change ledger entries?

Mappings change how existing balances are classified and displayed. They do not repost transactions.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Profit and Loss Report](/erpnext/profit-and-loss-report)
- [Balance Sheet](/erpnext/balance-sheet)
- [Accounts Receivable](/erpnext/accounts-receivable)
- [Accounts Payable](/erpnext/accounts-payable)
- [Customise Cash Flow Report](/erpnext/customise-cash-flow-report)

<!-- page: erpnext/erpnext__centavo-being-printed-in-words-for-usd.md -->
---
title: "Print \"Centavo\" in Words for USD"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/centavo-being-printed-in-words-for-usd"
updated: "2026-03-02"
---

For currencies not present in the Currency list doctype:

You can go to Currency list doctype --> Add the currency --> Add Exchange rate --> Enable the currency --> You can then add the currency in any transaction required.

[Screenshot on the live page]

For instance:

[Screenshot on the live page]

Print format:

[Screenshot on the live page]

<!-- page: erpnext/erpnext__change-existing-users-email-id.md -->
---
title: "Change existing user's email ID or Rename User"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/change-existing-users-email-id"
updated: "2026-07-02"
---

The User ID is created based on the email address. When a user is renamed, its value is updated in all existing records, including change logs. As a result, this is a resource-intensive action. If you encounter time-out issues while renaming a user, consider creating a new User ID using the updated email address and disabling the old user.

If you need to change a user's email address or username, use ERPNext's built-in **Rename** tool. This updates the user's unique ID across all linked records while preserving assignments, permissions, and historical data.



To change a User's Email Id, follow the steps: 

> **User List -> Open the User** **> Click on Menu -> Rename > Enter the New Email Id . Save** 

#### Prerequisites

You must have **Administrator** privileges to rename a user.

#### Steps

1. Go to **Settings > Users and Permissions > User**.
2. Open the user you want to rename.
3. Click **Menu** (⋮) in the top-right corner of the form.
4. Select **Rename**.
5. Enter the new email address or username.
6. Click **Save**.

#### What Happens After Renaming?

ERPNext automatically updates all references to the user across the system. This ensures that:

- Existing document links remain intact.
- Assignments continue to work.
- User permissions are preserved.
- Historical records continue to reference the renamed user correctly.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__change-password.md -->
---
title: "Change User Password"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/change-password"
updated: "2026-02-26"
---

**'Change Password' is used to change the password of any existing user.**

Each ERPNext user can change password for his/her ERPNext account. Also user with System Manager role will be able to reset password for himself as well as for other users.

**How to change password?**
---------------------------

1. Go to User List
2. Open the user for whom the password needs to be changed
3. Go to 'Settings', and expand the section named 'Change Password'
4. Enter the new password and save the form

**Note:-** Based on the complexity of the password, the system indicates whether the entered password is Weak or Strong

[Screenshot on the live page: Screenshot 2023-12-27 at 4.39.12 PM]  

<!-- page: erpnext/erpnext__change-the-rate-of-items-in-the-sales-cycle.md -->
---
title: "Control Item Rate Changes Through the Sales Cycle | ERPNext Documentation"
description: "Configure ERPNext to preserve, warn about, or stop item-rate changes between Sales Orders, Delivery Notes, and Sales Invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/change-the-rate-of-items-in-the-sales-cycle"
updated: "2026-07-25"
---

ERPNext can validate whether an Item's rate changes as it moves from a [Sales Order](/erpnext/sales-order) to a [Delivery Note](/erpnext/delivery-note) or [Sales Invoice](/erpnext/sales-invoice). Use this control when confirmed order rates should remain consistent through fulfilment and billing.

## Before you begin

Confirm:

- Item Prices and the intended [Price List](/erpnext/price-lists).
- The roles permitted to approve price exceptions.
- Whether your process requires a warning or a hard stop.
- How legitimate amendments and returns should be handled.

This setting does not replace pricing governance. Document when a rate may change and who may approve it.

## Configure rate validation

1. Open [Selling Settings](/erpnext/selling-settings).
2. Open the Item Price Settings section.
3. Enable **Maintain Same Rate Throughout Sales Cycle**.
4. Set **Action If Same Rate Is Not Maintained** to:
  - **Warn** to allow saving after notifying the user.
  - **Stop** to block the inconsistent rate.
5. When Stop is selected, choose the role allowed to override the action if your version provides that field.
6. Save.

[Screenshot on the live page: Selling Settings with the same-rate controls highlighted.]

## Test the control

1. Create and submit a Sales Order with an Item rate.
2. Create a Delivery Note or Sales Invoice from the Sales Order.
3. Select the highlighted pencil icon to open the complete Item row.
4. Change the Rate.
5. Save and confirm that ERPNext warns or stops the change according to Selling Settings.

[Screenshot on the live page: A mapped Sales Invoice item row with the Rate field highlighted.]

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## When a rate legitimately changes

Use the workflow that preserves the audit trail:

- Amend the confirmed Sales Order when the commercial agreement changed before fulfilment.
- Use [Update Items](/erpnext/amending-sales-order-after-submit) when the supported after-submit workflow fits the change.
- Create a Credit Note or return when correcting a submitted invoice.
- Use an authorized override only when policy permits it.

Do not silently change a downstream rate simply to make totals match.

## How pricing sources interact

A transaction rate can be influenced by:

- Item Price and Price List.
- [Pricing Rules](/erpnext/pricing-rule).
- [Promotional Schemes](/erpnext/promotional-scheme).
- Item-level margin or discount.
- Additional Discount.
- Currency conversion.
- A manually entered Rate when permissions allow it.

The same-rate validation compares the mapped sales-cycle rate. It does not prevent every possible upstream pricing configuration.

## Important settings


| Setting                                   | Effect                                                                             |
| ----------------------------------------- | ---------------------------------------------------------------------------------- |
| Maintain Same Rate Throughout Sales Cycle | Enables comparison against the upstream rate                                       |
| Action: Warn                              | Shows a warning but permits the user to continue                                   |
| Action: Stop                              | Blocks the rate change                                                             |
| Override Role                             | Lets authorized users bypass Stop when supported                                   |
| Allow User to Edit Price List Rate        | Controls editing of the Price List Rate field, not the complete sales-cycle policy |


## Troubleshooting


| Problem                                | What to check                                                                            |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| No warning appears                     | Confirm the downstream document was mapped from the Sales Order and the setting is saved |
| Authorized user cannot override        | Confirm the configured role and the user's assigned roles                                |
| Rate changes before mapping            | Review Item Prices, Pricing Rules, discounts, currency, and the source document          |
| Return or credit correction is blocked | Use the appropriate return or amendment workflow                                         |
| Users confuse Rate and Price List Rate | Explain the reference rate, margin, discount, and final transaction rate                 |


## Frequently asked questions

### Does the setting apply to unrelated standalone invoices?

It is intended to validate rates through a linked sales cycle. A standalone invoice has no Sales Order rate to compare.

### Should I choose Warn or Stop?

Use Warn where exceptions are common and reviewed later. Use Stop where approval must happen before the document is saved.

### Can a role override Stop?

Yes, when the override-role field is available and configured in your ERPNext version.

### Does the setting stop Pricing Rules?

No. Pricing Rules remain part of rate calculation. Test the combined workflow.

## Related topics

- [Selling Settings](/erpnext/selling-settings)
- [Sales Order](/erpnext/sales-order)
- [Amending Sales Order after Submit](/erpnext/amending-sales-order-after-submit)
- [Pricing Rule](/erpnext/pricing-rule)
- [Applying a Discount](/erpnext/applying-discount)
