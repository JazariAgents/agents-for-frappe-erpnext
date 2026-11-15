<!-- Frappe documentation: erpnext, part 20 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__deleting-all-transactions-for-the-company.md -->
---
title: "Deleting all transactions for the Company while retaining masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-all-transactions-for-the-company"
updated: "2026-07-02"
---

Use **Delete Transactions** on the Company form when you want to remove transactions for a company while keeping the company setup and master data. This is useful after testing, demo data entry, or sample imports when you want to start entering live transactions without recreating all masters.

This action clears transactional data for the selected company. It does not delete masters such as Company, Customer, Supplier, Item, Account, Warehouse, Cost Center, or other setup records.

## Before You Begin

- Take a full backup before deleting transactions. This action is destructive and should be treated as irreversible unless you restore from backup.
- Use this only when you are sure the selected company's transactions are no longer required.
- Check that users are not creating or submitting new transactions for the company while the deletion is running.
- If the company has been used for live accounting, export the required ledgers and reports before deleting data.
- Make sure you are logged in as a user with permission to delete company transactions.

## What Gets Deleted

ERPNext deletes transactional records linked to the selected company. This can include accounting, stock, buying, selling, payment, manufacturing, and other transaction documents that belong to that company.

The exact records depend on the modules used in your site and the transactions created for the company.

## What Is Not Deleted

Master and setup records are retained. For example, the following records are not deleted just because company transactions are deleted:

- Company
- Customer
- Supplier
- Item
- Account
- Warehouse
- Cost Center
- Territory, Customer Group, Supplier Group, and Item Group

This lets you keep the structure of the company and reuse the same masters after the transactions are cleared.

## Delete Transactions for a Company

### Step 1: Open the Company list

Search for **Company** from the Desk search bar, or open the Company list from the Accounting workspace.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 2: Open the company record

Select the company whose transactions you want to delete. Check the company name carefully before continuing.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 3: Choose Delete Transactions

On the Company form, open **Manage** and click **Delete Transactions**.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

### Step 4: Verify your password

ERPNext asks you to verify your password before continuing. Enter your password and click **Verify** only when you are certain you have selected the correct company and have a backup.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

After verification, ERPNext starts deleting the selected company's transactions. Do not close the site or create new transactions for the company while the deletion is in progress.

## After Deletion

- Open key transaction lists, such as Sales Invoice, Purchase Invoice, Payment Entry, Journal Entry, Stock Entry, and Sales Order, and confirm that the company's transactions are removed.
- Check accounting and stock reports for the company to make sure balances are cleared as expected.
- Review retained masters such as Customers, Suppliers, Items, Accounts, and Warehouses before creating new transactions.
- If you plan to start fresh accounting, verify opening balances, stock balances, and fiscal year settings before entering new documents.

## When To Use This

Use this tool when you want to preserve setup and masters but remove transaction history for one company. Common examples include demo data cleanup, testing cleanup, and preparing a configured company for live use.

## When Not To Use This

- Do not use this as a routine data cleanup tool for live companies.
- Do not use it when you only need to cancel or reverse a few specific transactions.
- Do not use it if you need an audit trail of the deleted transactions inside the same site.
- Do not use it without a backup that you know can be restored.

## Common Issues

- **Transactions are still visible:** Check whether those records belong to another company, or whether they are master records rather than transactions.
- **Balances are not cleared:** Recheck linked transactions and reports for the selected company. Also verify whether opening balances or stock balances were entered separately.
- **Permission error:** Your user may not have permission to run the deletion tool. Ask a System Manager or Administrator to review your access.
- **Wrong company selected:** Stop immediately and restore from backup if transactions were deleted for the wrong company.

## Recommended Practice

Before using this on an important site, restore a recent backup on a test site and run the deletion there first. Review the result, confirm that the required masters remain, and then repeat the process on the main site only when you are confident about the outcome.

<!-- page: erpnext/erpnext__deleting-custom-reports.md -->
---
title: "Deleting Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/deleting-custom-reports"
updated: "2026-03-04"
---


ERPNext has several [types of reports](/erpnext/making-custom-reports) which can be customized as per the users' requirement.

If there is a custom report which needs to be deleted, it can be achieved by following steps. Please note that its applicable only for the Custom Reports, and not for the standard reports.

#### Step 1: Go to Report List

In the Awesome Bar, type and select "Report List" for an option.

[Screenshot on the live page: Report Search]

#### Step 2: Delete the Report from the List

The Report List will have all the standard and custom reports of your account. You can select Custom Report to be deleted from the list itself, and click on Delete icon in the Actions Menu.

[Screenshot on the live page: Report List]

Or you can open that report, and delete it from File menu.

[Screenshot on the live page: Report Delete]

<!-- page: erpnext/erpnext__delivery-note-stock-error.md -->
---
title: "Delivery Note Negative Stock Error\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-note-stock-error"
updated: "2026-02-26"
---


**Question**: When submitting a Delivery Note, receiving a message says that item's stock is insufficient, but we have item's stock available in the Warehouse.

**Answer**: On submission of Delivery Note, stock level is checked as on Posting Date and Posting Time of a Delivery Note. It's possible that you have stock of an Item available in the Warehouse. But if you are creating back-dated Delivery Note, and if item was not available in the warehouse on the Posting Date and Posting Time of Delivery Note, you are likely to receive an error message on the negative stock. You can refer to the Stock Ledger report to confirm the same.

If this is the case, you should edit the Posting Date and Time of a Delivery Note, and ensure that it is after the Posting Date and Time of item's receipt entry.

<!-- page: erpnext/erpnext__delivery-note.md -->
---
title: "Delivery Note\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-note"
updated: "2026-02-26"
---

**A Delivery Note is made when a shipment is shipped from the company’s Warehouse to the customer.**

A copy of the Delivery Note is usually sent with the transporter. The Delivery
Note contains the list of Items that are sent in the shipment and updates the
inventory. The Delivery Note is an optional step and a Sales Invoice can be created directly from a Sales Order.

To access the Delivery Note list, go to:

> Home > Stock > Stock Transactions > Delivery Note

[Screenshot on the live page: Delivery Note flow]

## Prerequisites

Before creating and using a Delivery Note, it is advised that you create the following first:

- Sales Order

> Note: From version-13 onwards we have introduced immutable ledger which changes the rules for cancellation of stock entries and posting backdated stock transactions in ERPNext. Learn more here.

## How to create a Delivery Note

The entry of the Delivery Note is very similar to a Purchase Receipt. It is usually created from a “Submitted” Sales Order (that is not shipped) by clicking on Create > Delivery.

To create a Delivery Note manually (not recommended), follow these steps:

1. Go to the Delivery Note list, click on New.
2. The Customer and Item details can be fetched by clicking on 'Get Items from > Sales Order'.
3. The UOM and Rates will be fetched automatically.
4. Save and Submit.
  Delivery Note

To fetch Items from a Sales Order, click on Get Items from > Sales Order. This will open a popup from where you can search for Sales Orders and select one.

You will notice that all the information about unshipped Items and other details are carried over from your Sales Order if you create the Delivery Note from there.

You can also edit the posting date and time, the current date and time are set when you create the Delivery Note.

### Statuses

These are the statuses a Delivery Note can be in:

- **Draft**: A draft is saved but yet to be submitted to the system.
- **To Bill**: Yet to be billed using a Sales Invoice.
- **Completed**: Submitted and sent all the Items.
- **Return Issued**: All the Items have been returned.
- **Cancelled**: Cancelled the Delivery Note.
- **Closed**: The purpose of the Close is to manage short-closing. For example, your Customer ordered for 20 qty but closed at 15 qty. The remaining 5 is not to be sent or billed.

### Partial Deliveries

When you create a Delivery Note from a Sales Order, the quantities can be changed. So if the Sales Order contains 10 Items to be delivered and you're delivering only 5 this week and the remaining next week, then you can create 2 Delivery Notes in two weeks.

### From Pick List

You can create Delivery Notes in bulk, from Pick Lists also. From a submitted Pick List, click on Create -> Delivery Note. 

[Screenshot on the live page]

This would create separate Delivery Notes for Sales Orders, grouped by Customer.
If a Pick List Item is not linked to a Sales Order(added manually by user), a separate DN would be created for all those items as well.

## Related Actions

### Customer Purchase Order Details

You can enter the Customer's Purchase Order number here for Reference.

### Address and Contact

- **Shipping Address**: The Customer's address where the Items will be shipped.
- **Contact Person**: If the Customer is an organization, add the Contact person in this field.

For India, the following details can be added for GST:

- Customer GSTIN
- Place of Supply
- Billing Address GSTIN
- Company GSTIN
- Company Address Name

Contacts and Addresses are stored separately so that you can attach multiple Contacts or Addresses to the customer.

### Currency and Price List

You can set the currency in which the Deliver Note is to be sent. This is usually fetched if set in the Sales Order. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

Read about Price Lists
and Multi-Currency Transactions
to know more.

### Warehouses

- **Set Source Warehouse**: This is where the Items will be sourced from to send to the Customer.
- **To Warehouse**: In a regular Sales scenario, the Item exits your Warehouse and reaches the Customer. However, if you wish to retain sample stock, enter a Warehouse here.

### Items Table

- **Barcode**: You can track Items using barcodes.
- The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.
- **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Read documentation for tracking items using barcode to know more.
- **Discount and Margin**: You can apply a discount on individual Items percentage-wise or the total amount of the Item. Read Applying Discount for more details.
- **Rate**: The Rate is fetched if set in the Price List and the total Amount is calculated.
- **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit this page.
- The Item Weight details per unit and Weight UOM are fetched if set in the Item master.
- **Warehouse and Reference**: The Warehouse from which the Items are sent to the Customer is shown. Also, a Sales Order will be shown if this Delivery Note was the creation flow: 'Sales Order > Deliver Note'.
- **Batch No and Serial No**: If your Item is serialized or batched, you will have to enter Serial Number and Batch in the Items table. You are allowed to enter multiple Serial Numbers in one row (each on a separate line) and you must enter the same number of Serial Numbers as the quantity.

 The 'Available Qty at From Warehouse', 'Available Batch Qty at From Warehouse', and 'Installed Qty' will be shown. To know more about installation, visit the Installation Note page.

 **Note**: The Item has to be serialized or batched for these features to work. If the Item is serialized a popup will appear where you can enter the Serial Numbers.

- Expense Account is the account from which the amount will be debited. Ticking on 'Allow Zero Valuation Rate' will allow submitting the Delivery Note even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.
- Accounting Dimensions help to tag each transaction with different Dimensions without the need for creating new Cost Centers. You need to create Accounting Dimensions first, to know more, visit this page.
- **Page Break** will create a page break just before this Item when printing.

### Tracking Quality Inspection

If for certain Items, it is mandatory to record Quality Inspections (if you have set it in your Item master), you will need to update the “Quality Inspection" field. The system will only allow you to “Submit” the
Delivery Note if you update the “Quality Inspection”.

After enabling Inspection Criteria in the Item form for Sales and attaching a Quality Inspection Template there, Quality Inspections can be recorded in Delivery Notes.

### Taxes and Charges

The Taxes and Charges will be fetched from the Sales Order.

Visit the Sales Taxes and Charges Template page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit this page.

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule

A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the Shipping Rule page.

### Additional Discount

Any additional discounts to the whole order can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.
Read Applying Discount for more details.

### Terms and Conditions

In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, click here

### Transporter Information

If you outsource transporting Items to their delivery location, the transporter details can be added. This is not the same as drop shipping.

- **Transporter**: The Supplier who will transport the Item to your Customer. The transporter feature should be enabled in the Supplier master to select the Supplier here.
- **Driver**: You can add a Driver here who will drive the mode of transport.

[Screenshot on the live page]

The following details can be recorded:

- Distance in km
- Mode of Transport whether road, air, rail, or ship.

For India, GST:

- GST Transporter ID
- Transport Receipt No
- Vehicle No
 The GST Vehicle Type can be changed

The Transport Receipt Date and Driver Name will be fetched.

### More Information

The Delivery Note can be linked to the following for tracking purposes:

- Project
- Campaign
- Source

### Printing Settings

#### Letterhead

You can print your Delivery Note on your company's letterhead. Know more here.

'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.

#### Print Headings

Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more here.

There are additional checkboxes for printing the Delivery Note without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.

### Status

The status of the document and installation percentage is shown here. Any additional instructions for delivery can be entered here.

### Commission

If the sale took place via one of your Sales Partners, you can add their commission details here. This is usually fetched from the Sales Order.

### Sales Team

**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal.

This is usually fetched from a Sales Order, for example:

[Screenshot on the live page]

### Shipping Packets or Items with Product Bundle

If you are shipping Items that have a Product Bundle, ERPNext will automatically create a “Packing List” table for you based on the sub-Items in that Item.

If your Items are serialized, then for Product Bundle type of Items, you will have
to update the Serial Number in the “Packing List” table.

### Packing Items into Cases, for Container Shipment

If you are doing making the delivery via container shipment or by weight, then you can use the Packing
Slip to break up your Delivery Note into smaller units. To know more about a Packing Slip, visit this page.
go to:

You can create multiple Packing Slips for your Delivery Note and ERPNext will
ensure that the quantities in the Packing Slip do not exceed the quantities in
the Delivery Note. Note that you can create a Packing Slip from a Delivery Note only when the Delivery Note is in the Draft stage.

### After Submitting

When the Delivery Note is submitted, a Stock Ledger Entry is made for each Item and stock is updated. Pending
Quantity in the Sales Order is updated (if applicable).

The Dashboard will show the following options:

- Installation Note
- Sales Return
- Delivery Trip
- Sales Invoice
  [Screenshot on the live page]

> Tip: To disallow the creation of Delivery Notes without a Sales Order against it:

### Returning a Sales Order

Once you've delivered a Sales Order using a Delivery Note, you can create a return entry in case the Customer returns the Item. To know more, visit the Sales Return page.

### Skipping Delivery Note

If you don't want to create a Delivery Note after a Sales Order and directly want to create a Sales Invoice, enable the feature for it in Selling Settings.

### Related Topics

1. Warehouse
2. Delivery Note Stock Error
3. Material Transfer From Delivery Note and Purchase Receipt
4. Installation Note
5. Delivery Trip

<!-- page: erpnext/erpnext__delivery-trip.md -->
---
title: "Delivery Trip\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/delivery-trip"
updated: "2026-02-27"
---


**A Delivery Trip records Customer Deliveries in one vehicle.**

Multiple stops can also be added and Submitted Delivery Note can be tagged per Customer.

## 1. How to create a Delivery Trip
A Delivery Trip can be created from a [Delivery Note](/erpnext/delivery-note) by clicking on 'Create > Delivery Trip'.

1. Go to: **Stock > Stock Transactions > Delivery Trip > New**
1. Select the Driver and Vehicle, create both if not present.
1. Set the date, departure date and time.
1. Add customers for delivery stops, the address will be fetched if already set. Customers can also be fetched by clicking on 'Get customers from > Delivery Note'. Additional Delivery Stops can be added by clicking on the Add Row button before submitting:

 [Screenshot on the live page: Delivery]

1. Save and submit.

 [Screenshot on the live page: Delivery]

## 2. Features
### 2.1 Calculate Estimated Arrival Times
If the Customer address and the Driver address are set, you can calculate the estimated arrival time for the deliveries. This data is fetched from Google Maps.

### 2.2 Optimize Route
Using Google Maps, the best route for the deliveries will be calculated.


### Related Topics
1. [Packing Slip](/erpnext/packing-slip)
1. [Shipping Rule](/erpnext/shipping-rule)

<!-- page: erpnext/erpnext__demand-driven-forecasting.md -->
---
title: "Forecasting Using Exponential Smoothing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/demand-driven-forecasting"
updated: "2026-03-02"
---

To access the Forecating Report, go to:

> Home > Manufacturing > Reports > Forecasting

[Screenshot on the live page: Production Forecasting]  


Using exponential smoothing method and past Sales Order / Delivery Note / Quotation data, the forecasting will be calculated. The exponential smoothing method formula is as below:

[Screenshot on the live page: Production Forecasting]  


Using exponential smoothing method, system predicts the forecasting for each period and same forecast data will be used to forecast the upcoming period data.

How does the exponential smoothing method works
-----------------------------------------------

[Screenshot on the live page: Production Forecasting]  


For the above example, we have used one-year sales order data every month. The first-month forecast will be calculated based on the average of all total orders. From the second month onward, the difference between the last month's Total Order and Forecast Value will be multiplied with the Smoothing Constant Value (in between 0 to 1). The default value of the Smoothing Constant is 0.3 which gives efficient forecasting data. The last month's Total Order and Forecast Value difference called forecasting error and this error will be added in the same month of forecast value to calculate the forecast of the next month.

How do the filters work
-----------------------

1. **Company** :- user can do forecasting for the specific company by applying the company filter
2. **From Date and To Date** :- for this period system will do the forecasting, the default from date is the current date and to date will be the one year ahead date from the current date.
3. **Based On Document** :- by default system uses sales order past data to forecast. User can select the other document like delivery note / quotation to forecast the data.
4. **Based On** :- based on quantity / amount system shows the forecast data.
5. **Based On Data ( in years )** :- for forecasting requires past data, this filter helps system to check past data for number of years.
6. **Periodicity** :- forecasting data can be viewed in Monthly / Quarterly / Half-Yearly / Yearly basis, the old forecast data can not be displayed for Monthly period for better view.
7. **Smoothing Constant** - the Smoothing Constant will be used to forecast the data, the value should be between 0 and 1.

<!-- page: erpnext/erpnext__depreciation-methods.md -->
---
title: "Depreciation Methods | ERPNext Documentation"
description: "Choose and configure Straight Line, Double Declining Balance, Written Down Value, or Manual depreciation in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/depreciation-methods"
updated: "2026-08-15"
---

Imagine Nova Industries buys two assets for the same price: an office table and a production machine. The table may provide roughly the same value every year. The machine may lose more value in its early years because it works hardest when it is new. Using one depreciation pattern for both may not reflect how they are actually used.



Depreciation Methods let the accountant choose how an asset's cost is spread over its useful life. ERPNext supports methods such as Straight Line and declining balance so the schedule can follow the company's accounting policy and the asset's pattern of use.

## Depreciation methods at a glance


| Method                       | How it works                                                                                    | Best suited for                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Straight Line**            | Records an equal depreciation expense in every complete period.                                 | Assets that provide a similar benefit throughout their life, such as office furniture, air conditioners, and basic equipment. |
| **Double Declining Balance** | Records a larger expense in the early years and a smaller expense later.                        | Assets that lose usefulness or value quickly when new, such as computers, mobile devices, and rapidly ageing machinery.       |
| **Written Down Value**       | Applies a fixed percentage to the asset's opening book value, so the expense reduces over time. | Assets for which the company's accounting or tax policy prescribes depreciation on the remaining book value.                  |
| **Manual**                   | Uses depreciation dates and amounts entered by the accountant instead of a standard formula.    | Assets with a contract-based, valuation-based, or specially approved depreciation schedule.                                   |


Treat this table as a practical starting point. The method used in the accounts should ultimately follow the organization's approved accounting policy and applicable reporting rules.

## Use one example to compare the methods

Assume Nova Industries buys a packaging machine for $50,000. It expects to use the machine for five years and sell it for $5,000 at the end. The amount to depreciate is therefore:



**Depreciable value = $50,000 cost - $5,000 residual value = $45,000**



Every method eventually allocates the same $45,000. What changes is how much expense appears in each year.

## Straight Line

Straight Line records the same expense in every complete year.



**Annual depreciation = $45,000 / 5 years = $9,000**


| Year | Opening book value | Depreciation | Closing book value |
| ---- | ------------------: | ------------: | ------------------: |
| 1    | $50,000            | $9,000       | $41,000            |
| 2    | $41,000            | $9,000       | $32,000            |
| 3    | $32,000            | $9,000       | $23,000            |
| 4    | $23,000            | $9,000       | $14,000            |
| 5    | $14,000            | $9,000       | $5,000             |


Use this method when the asset provides a similar benefit each year. Office furniture, air conditioners, and basic production equipment often fit this pattern.

## Double Declining Balance

Double Declining Balance records more depreciation while the asset is new. For a five-year life, the Straight Line rate is 20 percent. Double Declining uses twice that rate, or 40 percent, on each year's opening book value.



**Year 1 depreciation = $50,000 x 40% = $20,000**



The final expense is limited so the asset never falls below its $5,000 residual value.


| Year | Opening book value | Calculation               | Depreciation | Closing book value |
| ---- | ------------------: | ------------------------- | ------------: | ------------------: |
| 1    | $50,000            | $50,000 x 40%             | $20,000      | $30,000            |
| 2    | $30,000            | $30,000 x 40%             | $12,000      | $18,000            |
| 3    | $18,000            | $18,000 x 40%             | $7,200       | $10,800            |
| 4    | $10,800            | $10,800 x 40%             | $4,320       | $6,480             |
| 5    | $6,480             | Limited to residual value | $1,480       | $5,000             |


Use this method when an asset loses usefulness or market value faster in its early years. Computers, mobile devices, and some high-use machinery are common examples.

## Written Down Value

Written Down Value applies a chosen rate to the opening book value. Assume Nova's policy uses 30 percent per year for this machine.



**Year 1 depreciation = $50,000 x 30% = $15,000**



Because the opening value becomes smaller each year, the depreciation expense also becomes smaller. The last year is again limited so the closing value does not fall below $5,000.


| Year | Opening book value | Calculation               | Depreciation | Closing book value |
| ---- | ------------------: | ------------------------- | ------------: | ------------------: |
| 1    | $50,000            | $50,000 x 30%             | $15,000      | $35,000            |
| 2    | $35,000            | $35,000 x 30%             | $10,500      | $24,500            |
| 3    | $24,500            | $24,500 x 30%             | $7,350       | $17,150            |
| 4    | $17,150            | $17,150 x 30%             | $5,145       | $12,005            |
| 5    | $12,005            | Limited to residual value | $7,005       | $5,000             |


Use this method when the company's accounting or tax policy specifies a percentage on the remaining value. The example rate is illustrative. Use the rate approved for your organization.

## Manual

Manual depreciation lets the accountant define the dates and amounts instead of relying on a standard formula. Nova might use the following schedule when an equipment contract expects heavier use in its first two years.


| Year | Opening book value | Depreciation entered | Closing book value |
| ---- | ------------------: | --------------------: | ------------------: |
| 1    | $50,000            | $15,000              | $35,000            |
| 2    | $35,000            | $10,000              | $25,000            |
| 3    | $25,000            | $8,000               | $17,000            |
| 4    | $17,000            | $7,000               | $10,000            |
| 5    | $10,000            | $5,000               | $5,000             |


Use Manual only when a documented policy, valuation, or contract requires a custom pattern. The entered amounts should still total the $45,000 depreciable value.

## Compare the result


| Method                        | Expense pattern        | Year 1 expense | Year 5 expense                    | Closing value after year 5 |
| ----------------------------- | ---------------------- | --------------: | ---------------------------------: | --------------------------: |
| **Straight Line**             | Equal                  | $9,000         | $9,000                            | $5,000                     |
| **Double Declining Balance**  | Highest in early years | $20,000        | $1,480                            | $5,000                     |
| **Written Down Value at 30%** | Reduces each year      | $15,000        | $7,005 after residual-value limit | $5,000                     |
| **Manual example**            | Set by policy          | $15,000        | $5,000                            | $5,000                     |


## Set the method in ERPNext

Set the default method, useful life, frequency, and residual value in the Asset Category Finance Book row. The Asset can then use those defaults when ERPNext builds its depreciation schedules.

[Screenshot on the live page: Different depreciation methods by Finance Book]

The submitted schedule below uses Straight Line for Nova's packaging equipment. ERPNext has calculated $760 per month, accumulated the amount, and linked each posted row to its Journal Entry.

[Screenshot on the live page: Submitted depreciation schedule with calculated amounts]

## Verify the result

Before submission, compare total scheduled depreciation plus residual value with the capitalized value. Also check the last date and the first full or prorated period.

## Troubleshooting

### The last schedule row is unexpectedly small

ERPNext may be limiting the final row so carrying value does not fall below the configured residual value.

### Two Finance Books show different carrying values

That is expected when they use different methods, useful lives, or start dates. Review reports with the intended Finance Book filter.

## Frequently asked questions

### Which method is best?

There is no universal best method. Use the method approved by the organization's accounting policy and reporting requirements.

### Can the method be changed after entries are posted?

A policy change may require cancellation or adjustment of linked schedules and entries. Review the accounting impact before changing a submitted asset.

### Can statutory and management reporting differ?

Separate Finance Books can keep different depreciation policies for the same asset.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__difference-between-system-user-and-website-user.md -->
---
title: "Difference Between System User and Website User"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-between-system-user-and-website-user"
updated: "2026-03-04"
---

**Question:** I have added my Employee as a User and have assigned them Roles as well. Still, they are not able to view Dashboard on the login.

**Answer:**

There are two type of Users in ERPNext.

* **System Users**: They are typically internal users such as employees, managers, and administrators who need extensive access to the ERPNext system to perform various business operations. They have a higher level of access and more detailed permissions, allowing them to interact with multiple modules, generate reports, and customize workflows.
* **Website Users**: They are typically external users like customers or suppliers who interact with the ERPNext system through a web portal. Their access is limited to functionalities relevant to their needs, such as placing orders, viewing order status, or managing their account information. Their interface is simpler compared to the comprehensive backend interface used by system users.

Here is the tabular comparison between System User and Website User in ERPNext



| **System User** | **Website User** |
| --- | --- |
| This type is useful for managing internal activities and operations | It is useful for managing external operations and transactions |
| It provides full access to ERPNext modules and features | It provides restricted access to ERPNext modules and features |
| Typical users in this category are internal employees  | The user persona in this type includes external parties such as customers, clients etc |
| They are created by an administrator within ERPNext | They can be self-registered or created by an administrator |
| It provides access to company-wide data and reports | It provides access to only personal data and limited reports |
| They can view, create, edit, and delete records | They can mostly view and create records relevant to them |
| They have full data entry capabilities across all modules | They have limited to data entry relevant to their role |

<!-- page: erpnext/erpnext__difference-entry-button.md -->
---
title: "Difference Entry | ERPNext Documentation"
description: "Use ERPNext Difference Entry to balance a Journal Entry, select the correct account, avoid masking errors, and verify the submitted General Ledger clearly."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/difference-entry-button"
updated: "2026-08-03"
---

The **Make Difference Entry** action helps you complete an unbalanced [Journal Entry](/erpnext/journal-entry). ERPNext calculates the difference between Total Debit and Total Credit, adds a new accounting row for that amount, and leaves the Account blank for you to choose.



It is a balancing aid inside Journal Entry, not a separate transaction and not an automatic correction. You must understand why the difference exists and select the account that represents it. If the source amount, exchange rate, tax, or original account is wrong, correct that value instead of hiding the error in a difference account.



In this example, Nova Electronics Trading pays $1,000 from its bank. The main office-maintenance expense is $990 and the bank charges a $10 fee. The first two rows are therefore out of balance. **Make Difference Entry** adds the missing $10 debit, after which the user selects **Bank Charges - NET**.


| Account                     | Debit         | Credit        | Meaning                              |
| --------------------------- | -------------: | -------------: | ------------------------------------ |
| Office Maintenance Expenses | $990.00       | $0.00         | Main expense paid.                   |
| Bank Charges                | $10.00        | $0.00         | Separate fee deducted by the bank.   |
| Nova Operating Bank         | $0.00         | $1,000.00     | Total reduction in the bank balance. |
| **Total**                   | **$1,000.00** | **$1,000.00** | The Journal Entry is balanced.       |


## Before you begin

Confirm the following:

1. You know what caused the imbalance and have supporting evidence for the amount.
2. The correct ledger exists in the Company's [Chart of Accounts](/erpnext/chart-of-accounts). Use a non-group account belonging to the selected Company.
3. The Posting Date is open and belongs to the intended Fiscal Year and [Accounting Period](/erpnext/accounting-period).
4. Any required Cost Center, Project, Finance Book, or other [Accounting Dimension](/erpnext/accounting-dimensions) is available.
5. For bank entries, you have the bank reference number and date. For ordinary Customer or Supplier receipts, consider whether a [Payment Entry](/erpnext/payment-entry) is the safer transaction.

## Identify the difference

1. Create or open a Draft Journal Entry.
2. Select the Company, Entry Type, and Posting Date.
3. Add the known debit and credit rows under **Accounting Entries**.
4. Review **Total Debit**, **Total Credit**, and **Difference (Dr - Cr)**.

The example has a $990 debit and a $1,000 credit. ERPNext shows a difference of -$10 and makes **Make Difference Entry** available.



[Screenshot on the live page: Unbalanced Journal Entry with Make Difference Entry highlighted]

Before continuing, check whether the difference is legitimate. A missing bank fee is legitimate. A transposed amount, duplicate row, wrong currency, or incorrect exchange rate should be fixed at its source.

## Add and complete the difference row

1. Select **Make Difference Entry**.

ERPNext adds one row for the exact amount required to make Total Debit equal Total Credit. Because credit exceeds debit by $10 in this example, it adds a $10 debit row.

2. Select the highlighted pencil icon on the new row.

[Screenshot on the live page: Generated difference row with its pencil icon highlighted]

3. Select the Account that explains the difference. In the example, select **Bank Charges - NET**.

[Screenshot on the live page: Difference row editor with Bank Charges account highlighted]

4. Add the same Cost Center, Project, Finance Book, or other dimensions required by your accounting policy.
5. Close the row editor and review the complete table.

[Screenshot on the live page: Balanced Journal Entry after selecting the difference account]

Total Debit and Total Credit are now both $1,000. The entry is mathematically balanced, but you must still confirm that every account and amount is economically correct. Balanced totals do not prove correct accounting.

## Submit and verify the result

1. Review the Company, Posting Date, Entry Type, accounts, amounts, references, remarks, currencies, and dimensions.
2. Save and submit the Journal Entry.
3. Confirm that the submitted document contains the original rows and the completed difference row.

[Screenshot on the live page: Submitted Journal Entry showing all three accounting rows]

4. Open **View &gt; Ledger**, or run the [General Ledger](/erpnext/general-ledger) using the Journal Entry as the voucher filter.
5. Confirm the debit and credit for each account and the zero total balance across the voucher.

[Screenshot on the live page: General Ledger showing the Bank Charges difference entry]

In the example, the ledger shows a $990 debit to Office Maintenance Expenses, a $10 debit to Bank Charges, and a $1,000 credit to the operating bank account.

## Important fields and what they mean


| Field or action                    | What it controls                                                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Total Debit                        | Sum of the debit values in the accounting rows.                                                                                   |
| Total Credit                       | Sum of the credit values in the accounting rows.                                                                                  |
| Difference (Dr - Cr)               | Total Debit minus Total Credit. A negative value means more debit is required; a positive value means more credit is required.    |
| Make Difference Entry              | Adds one debit or credit row for the current difference. It does not select the Account or confirm that the difference is valid.  |
| Account                            | Ledger that receives the difference. Select the account that represents the actual economic event.                                |
| Debit or Credit                    | Amount added by ERPNext to balance the voucher. Review it before submission.                                                      |
| Account Currency and Exchange Rate | Control the account-currency and Company-currency values in a [multi-currency Journal Entry](/erpnext/multi-currency-accounting). |
| Reference Type and Reference Name  | Link an accounting row to a supported document when the adjustment genuinely belongs to that reference.                           |
| Is Advance                         | Marks a party amount as an advance when it is not allocated to a specific invoice.                                                |
| Cost Center and other dimensions   | Classify the posting for management reporting without replacing the ledger account.                                               |


## When not to use Make Difference Entry

Do not use this action merely to make an error disappear.

- If an invoice, payment, or stock transaction is wrong, cancel and amend the source document where permitted instead of creating an unrelated balancing row.
- If a genuine receipt or payment is being recorded, use the purpose-built payment workflow so invoice allocation, party balance, bank reference, and reconciliation remain clear.
- If the difference comes from foreign currency conversion, review the account currency, exchange rate, and Company-currency values first. Use the supported [exchange gain or loss](/erpnext/managing-transactions-in-multiple-currency) process when that is the real cause.
- If a small decimal difference is caused by configured precision, first review the source values and [System Settings](/erpnext/system-settings). Do not change precision casually after live transactions exist.
- If the required treatment is recurring, create a controlled process or [Journal Entry Template](/erpnext/journal-entry-template) rather than repeatedly guessing the balancing account.

## Troubleshooting


| Issue                                            | What to check                                                                                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make Difference Entry is not visible             | The Journal Entry may already be balanced. Review Total Debit, Total Credit, and Difference. Also confirm the document is still in Draft.                           |
| The generated row has no Account                 | This is expected. ERPNext supplies the amount only. Open the row and select the account that explains the difference.                                               |
| The entry is balanced but submission still fails | Check mandatory party, reference, currency, Cost Center, bank-reference, account-type, and frozen-period requirements. Mathematical balance is only one validation. |
| A tiny difference keeps appearing                | Check entered amounts, account currency, exchange rates, and precision. Correct the calculation source before using a rounding account.                             |
| The wrong side was added                         | Review the sign of Difference. Negative means credit is greater than debit, so ERPNext adds a debit. Positive means debit is greater, so it adds a credit.          |


## Frequently asked questions

### Does ERPNext choose the difference account automatically?

No, it adds a row with the required debit or credit and leaves the Account blank. The user must select the correct Company ledger.

### Should every small difference go to a round-off account?

No, first determine whether the cause is rounding. A wrong amount, exchange rate, tax calculation, or missing expense must be corrected or posted to the account that represents it.

### Can Make Difference Entry correct a multi-currency mismatch?

It can make the Company-currency totals balance, but it does not prove that the account-currency amounts and exchange rates are correct. Review both currencies before using it.

### Why can a balanced Journal Entry still be rejected?

ERPNext also validates Company, account type, party, reference, currency, dimensions, posting restrictions, and other mandatory values. Equal totals satisfy only the double-entry balance test.

### Can I edit or remove the generated row?

Yes, while the Journal Entry remains in Draft. You can select its Account, change the row when justified, or remove it and correct the original rows instead.

## Related topics

- [Journal Entry](/erpnext/journal-entry)
- [Understanding Debit and Credit](/erpnext/understanding-debit-and-credit)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Payment Entry](/erpnext/payment-entry)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Journal Entry Template](/erpnext/journal-entry-template)
