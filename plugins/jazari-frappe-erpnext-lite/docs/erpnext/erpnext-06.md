<!-- Frappe documentation: erpnext, part 6 of 18. Index: docs/INDEX.md -->

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

![Delivery Note flow](/files/delivery-note-flow.png)

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

![](/files/image81aab7.png)

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

![](/files/transportation.png)

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

![](/files/image71a4c0.png)

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
  ![](/files/image4843aa.png)

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

 ![Delivery](/files/delivery_stops.png)

1. Save and submit.

 ![Delivery](/files/delivery_trip.png)

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

![Production Forecasting](/files/production-forecasting-using-sales-order.png)  


Using exponential smoothing method and past Sales Order / Delivery Note / Quotation data, the forecasting will be calculated. The exponential smoothing method formula is as below:

![Production Forecasting](/files/exponential-smoothing-formula041d6b.png)  


Using exponential smoothing method, system predicts the forecasting for each period and same forecast data will be used to forecast the upcoming period data.

How does the exponential smoothing method works
-----------------------------------------------

![Production Forecasting](/files/exponential-smoothing-formula-e.png)  


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

![Different depreciation methods by Finance Book](https://novacompanies.m.frappe.cloud/files/03-asset-category-finance-books.png)

The submitted schedule below uses Straight Line for Nova's packaging equipment. ERPNext has calculated $760 per month, accumulated the amount, and linked each posted row to its Journal Entry.

![Submitted depreciation schedule with calculated amounts](https://novacompanies.m.frappe.cloud/files/26-asset-depreciation-schedule-v2.png)

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



![Unbalanced Journal Entry with Make Difference Entry highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-balanced-journal-entry.png)

Before continuing, check whether the difference is legitimate. A missing bank fee is legitimate. A transposed amount, duplicate row, wrong currency, or incorrect exchange rate should be fixed at its source.

## Add and complete the difference row

1. Select **Make Difference Entry**.

ERPNext adds one row for the exact amount required to make Total Debit equal Total Credit. Because credit exceeds debit by $10 in this example, it adds a $10 debit row.

2. Select the highlighted pencil icon on the new row.

![Generated difference row with its pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-row-added.png)

3. Select the Account that explains the difference. In the example, select **Bank Charges - NET**.

![Difference row editor with Bank Charges account highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-account-selected.png)

4. Add the same Cost Center, Project, Finance Book, or other dimensions required by your accounting policy.
5. Close the row editor and review the complete table.

![Balanced Journal Entry after selecting the difference account](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-balanced-journal-entry.png)

Total Debit and Total Credit are now both $1,000. The entry is mathematically balanced, but you must still confirm that every account and amount is economically correct. Balanced totals do not prove correct accounting.

## Submit and verify the result

1. Review the Company, Posting Date, Entry Type, accounts, amounts, references, remarks, currencies, and dimensions.
2. Save and submit the Journal Entry.
3. Confirm that the submitted document contains the original rows and the completed difference row.

![Submitted Journal Entry showing all three accounting rows](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-submitted-difference-journal-entry.png)

4. Open **View &gt; Ledger**, or run the [General Ledger](/erpnext/general-ledger) using the Journal Entry as the voucher filter.
5. Confirm the debit and credit for each account and the zero total balance across the voucher.

![General Ledger showing the Bank Charges difference entry](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-difference-entry-difference-entry-general-ledger.png)

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



![Purchase tax rows with freight considered for valuation](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-tax-table.png)

Open the freight row using its pencil icon. Set the row to **Valuation**, then enter the amount and the correct expense or clearing account.



![Freight row configured for valuation only](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-freight-fields.png)

In this example, the supplier payable remains:

`$800 item value + $32 tax = $832 payable`

The $100 freight is allocated into valuation but is excluded from the supplier total.



![Valuation-only freight excluded from the purchase invoice total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-only-result.png)

Use a suitable clearing or expense account for the valuation row. The source of the separately paid freight must still be recorded correctly, such as through another supplier invoice or a [Landed Cost Voucher](/erpnext/landed-cost-voucher), depending on the workflow.

## Add a charge to Valuation and Total

Select **Valuation and Total** when the same amount must increase both the supplier payable and the item's valuation. This is common when the item supplier arranges freight, includes it on the invoice, and the freight forms part of landed cost.



![Purchase tax rows with freight included in valuation and total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-tax-table.png)

Open the freight row and select **Valuation and Total**. Confirm the Account Head, Type, description, and amount before closing the row editor.



![Freight row configured for valuation and total](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-freight-fields.png)

The supplier payable becomes:

`$800 item value + $32 tax + $100 freight = $932 payable`

The $100 freight is also allocated into inventory valuation.



![Freight included in both purchase invoice total and valuation](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-tax-calculation-valuation-and-total-result.png)

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

![Print Preview](/files/customize-disable-rounded-total-2.png)

However, if you wish to disable the same, you may follow the steps given below to hide the rounded total from Standard Print Formats, for all the sales transactions.

#### Step 1: Go to Global Defaults

From the Awesome Bar search for Global Defaults

#### Step 2: Disable Rounded Total

Check Disable Rounded Total, and click on save.

![Print Preview](/files/customize-disable-rounded-total.png)

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

![Website signup](/files/website-signup.png)

To allow new Customer and Supplier to Signup, the login page of your ERPNext account has Signup link avaiable. However, if you wish to disbale this feature, you can achieve it by following the steps given below.

### Steps

1. Go To

> Website > Setup > Website Settings `

2. In the Website Settings page, scroll down upto `More Information` section.

3. Check fied `Disable Signup`.

![Disable signup](/files/disable-signup.png)

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

![work-order-disassembly-order](/files/work-order-disassembly-orderfe73b5.png)  


Once user clicked on the "Disassembly Order" button, the system will open the stock entry with type as "Disassemble"

  


![stock-entry-disassembly-order](/files/stock-entry-disassembly-order.png)  


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

![Selling Settings with Enable discount accounting for selling highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-enable-selling-discount-accounting.png)

This setting tells ERPNext to create additional ledger entries for sales discounts in the selected Discount Account.

4. Open [Accounts Settings](/erpnext/accounts-settings).
5. Select **Invoice and Billing**.
6. Enable **Enable Discounts and Margin** and save.

![Accounts Settings with Enable Discounts and Margin highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-enable-discounts-and-margin.png)

This setting makes the discount and margin controls available for transaction items. It does not, by itself, create a separate discount-account posting.

## Set a default Discount Account for an Item

A default avoids selecting the account on every invoice row.

1. Open the Item.
2. Select **Accounting**.
3. In **Item Defaults**, find the row for the Company.
4. Select the highlighted pencil icon to open the complete row editor.

![Item Defaults row with the pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-item-default-row.png)

5. Set **Discount Account** to the Company account that should receive item-level and invoice-level sales discounts.
6. Save the Item.

![Item Default with Discount Account highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-item-default-discount-account.png)

The Item Default is Company-specific. Configure a valid account and other defaults for each Company rather than copying an account from a parent or sibling Company.

## Record an item-level discount

1. Create a Sales Invoice and select the Company and Customer.
2. Add the Item to the **Items** table.
3. Select the highlighted pencil icon on the item row.

![Sales Invoice item row with the pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-sales-invoice-item-row.png)

4. Expand **Discount and Margin**.
5. Enter **Discount (%) on Price List Rate with Margin** or **Discount Amount**.

![Sales Invoice item discount percentage highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-sales-invoice-item-discount-percentage.png)

6. Expand **Accounting Details**.
7. Confirm the **Discount Account**. ERPNext fetches the Item Default when one is configured, but you remain responsible for verifying the account on the transaction.

![Sales Invoice item Discount Account highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-sales-invoice-item-discount-account.png)

In the example, the Price List Rate is $699 and the item discount is 10%. For two units, ERPNext records an item discount of $139.80 and an amount of $1,258.20 before the invoice-wide discount.

## Record an additional discount on the invoice

Use an additional discount when the reduction applies to the complete transaction instead of one item row.

1. Expand **Additional Discount** on the Sales Invoice.
2. Set **Apply Additional Discount On** to **Net Total** or **Grand Total**.
3. Enter **Additional Discount Percentage** or **Additional Discount Amount**.
4. Select the **Discount Account**.

![Sales Invoice Additional Discount fields and Discount Account highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-sales-invoice-additional-discount.png)

In the example, 5% of the $1,258.20 Net Total is $62.91. The item and additional discounts therefore total $202.71.

Apply on Net Total and Apply on Grand Total can produce different tax and net-value results. Review the tax breakup, rounding, and final amount with the configuration used by your business.

## Submit and verify the ledger

1. Review the discount amounts, taxes, Grand Total, and Discount Accounts.
2. Save and submit the Sales Invoice.
3. Open **View &gt; Ledger**, or run General Ledger for the invoice voucher.

The submitted example has a Grand Total and outstanding amount of $1,195.29.



![Submitted Sales Invoice total after discounts](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-submitted-sales-invoice-total.png)

The ledger shows gross Sales of $1,398.00, a $202.71 debit to Sales Discounts Allowed, and a $1,195.29 debit to Debtors.



![General Ledger showing the separate Sales Discounts Allowed entry](https://novacompanies.m.frappe.cloud/files/docs-gl-2026-discount-accounting-discount-account-general-ledger.png)

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



![Cost Center Allocation list in ERPNext](/files/cost-center-allocation-list.webp)

Select the shared **Main Cost Center**, the **Company**, and the **Valid From** date.



![Main Cost Center and Valid From fields for a distributed cost center](/files/allocation-main-and-date.webp)

In the allocation table, add each receiving cost center and its percentage. Save the record after the total reaches 100%.



![Receiving cost centers and their allocation percentages](/files/allocation-percentages.webp)

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

![Custom DocType](/files/doctype-employee-transfer.png)

### 1.1. Additional Details

1. **Fields**

 You can choose to add as many fields as you want. The Label, Field Type, Mandatory Fields and other associated Options can also be added here. Learn more about field types [here](/erpnext/field-types.html).

 ![Fields in Custom DocType](/files/doctype-employee-transfer-fields.png)

1. **Naming**

 Here you can choose if you would want each of your forms within this DocType to be named automatically. As given in the description, you can select the pattern for naming of the forms. The same can be a Field within the DocType, Naming Series, Prompt, A defined Naming Series, or a Format based Name. For Naming, you can also add a Description and the Name Case (as a Title Case or UPPER CASE)for your convenience.

 ![Naming Custom DocType](/files/doctype-employee-transfer-naming.png)

1. **Form Settings**

 Additional Settings for the Form, Image Fields, Attachments, Timeline etc. can be configured here. To know more about Form, visit [Customize Form](/erpnext/customize-form).

 ![Custom DocType Form Settings](/files/doctype-employee-transfer-form-settings.png)

1. **View Settings**

 Here, you can define the View settings for the DocType, like, Search Fields, Default Sort Field, Default Sort Order etc.

1. **Permission Rules**

 You can define the Permission Rules for the DocType here, and configure which users would be able to use or make changes to this DocType. Learn more about [Users and Permissions](/erpnext/users-and-permissions) here.

 ![Custom DocType Permissions](/files/doctype-employee-transfer-permissions.png)

1. **Web View**

 You can select whether you would want a Web View of this DocType or no. Having a Web View for a DocType will allow your website users to have access to the Forms. Feel free to learn more about [Website Users](/erpnext/difference-between-system-user-and-website-user).

### 1.2. More Properties

1. **Is Submittable**: You can select if you want this DocType to only be 'Saved' or to also be 'Submitted' by checking and un-checking this box.
1. **Is Child Table**: You can define if you want the New DocType to be a Child Table within another DocType. Checkout [Child Table](/erpnext/customizing-data-visibility-in-child-table) for more information.
1. **Is Single**: If checked, this Doctype will become a single form, like Sales Order, which user will
not be able to re-produce. For e.g., Selling Settings in Sales Module is a Single DocType.
1. **Is Tree**: A few DocTypes in ERPNext are structured as Trees, wherein there are some Parent DocTypes and some Children DocTypes. E.g., Doctype Company is structured as Tree, there are Parent Companies as well as Child Companies, which we call subsidiaries. If you want your DocTypes to be structured similarly, you can enable this option.

 ![DocType Tree View](/files/doctype-treeview.png)

1. **Quick Entry**: You can select if you want a Quick Entry to be made for this DocType. This will allow you to enter only a few mandatory details and save the DocType, so that a Quick Entry is made. For example, check Quick Entry in [Journal Entry](/erpnext/journal-entry#11-quick-entry).
1. **Track Changes**: You can select this option if you want to maintain a log of the changes made to each Form. Check Out [Document Versioning](/erpnext/document-versioning) for more understanding on this.
1. **Track Seen**: You can select this option if you want to maintain a log of all the Users who have seen this Form.
1. **Track Views**: You can select this option if you want to maintain a log of all the times each User has Viewed this Form.

 ![DocType Tree View](/files/doctype-track-views.png)

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

![Defining Criteria](/files/document-follow-how-to-follow.png)

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

![Defining Criteria](/files/document-follow-email.png)

### 2. Related Topics
1. [Linking Emails to Document](/erpnext/linking-emails-to-document)
1. [Notifications](/erpnext/notifications)

<!-- page: erpnext/erpnext__document-naming-for-avoiding-tab-series-issues.md -->
---
title: "Document Naming for Avoiding tabSeries Issues"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming-for-avoiding-tab-series-issues"
updated: "2026-08-12"
---

When you save a document in ERPNext a Sales Invoice, Stock Entry, Payment, anything with an auto-generated number, the system has to figure out the next number in the sequence (eg. 0001, 0002, 0003 and so on).



To make sure two documents never get the same number, ERPNext keeps a single counter for each naming series in a table called tabSeries. Before giving out the next number, it locks that counter so nobody else can touch it, adds 1, and then unlocks it. This happens in a fraction of a second, so normally you never notice it.



If hundreds of documents are being created at the same time and they all use the same naming series, they all need the same counter. Only one can hold the lock at a time, so everyone else has to wait in line.



When the line gets long, you start seeing:

- Documents that take a long time to save
- Bulk imports or bulk submissions that crawl or get stuck
- Errors like "Record has changed since last read in table 'tabSeries'" or database lock/deadlock timeouts
- Background jobs piling up in the queue



This gets much worse after busy periods, month-end, or when more workers are added to handle load, because now even more transactions are fighting over that one counter.



### **Why it happens more with customisation**

A very common cause is a customisation that forces a lot of transactions through a single, restricted naming series. Everything funnels into one counter, so one counter becomes the bottleneck for the whole operation. The more you scale up, the longer the queue behind that single row.



### **The simple fix: use more than one naming series**

The counter is locked per naming series. So the trick is easy:

Give different groups of transactions their own naming series, so they use different counters and stop waiting on each other.

Instead of one big line at one counter, you open several counters. Each line moves independently and in parallel.



### **Good ways to split series**

Pick whatever naturally divides your transactions. For example:


|              |                                              |
| ------------ | -------------------------------------------- |
| **Split by** | **Example series**                           |
| Branch       | SINV-MUM-.YYYY.-.####, SINV-DEL-.YYYY.-.#### |
| Project      | SINV-PROJ-A-.####, SINV-PROJ-B-.####         |
| Cost Center  | SINV-CC01-.####, SINV-CC02-.####             |
| Department   | SINV-SALES-.####, SINV-SUPPORT-.####         |


The idea is the same in every case: transactions that run at the same time should not all sit on the same counter. The more you spread them out, the less each one has to wait.



### **Extra tips for very large operations**

If you regularly create huge batches of documents at once:



- Spread big imports across multiple series so the load is shared, instead of importing everything under one series.
- Provide the name yourself during imports/API calls where possible. If a document already has a name, ERPNext skips the counter entirely. No lock, no waiting. For example, customer ID is generated based on Customer Name itself.
- Avoid customisations that force everything into one narrow series. Review any custom naming logic to make sure it isn't funnelling all transactions through a single counter.
- Stagger very large jobs slightly rather than firing them all in the same instant, if the process allows it.

<!-- page: erpnext/erpnext__document-naming-settings.md -->
---
title: "Document Naming Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming-settings"
updated: "2026-03-04"
---

**Masters and transactions can be given prefixes in the form of naming series.**

ERPNext allows you to make prefixes to your documents, with each prefix  
forming its own series. For example, a series with prefix INV12#### will have  
numbers INV120001, INV120002, and so on.

You can have multiple series for all your transactions. For example, Sales Invoice IDs like these can be generated:

- ACC-SINV-.YYYY.-
- SINV12####
- SALESINV-00####

You can define or select the Naming Series pattern from:

> Home > Settings > Document Naming Settings

## 1. Setting up Naming Series for Documents

1. Select the transaction for which you want to make the series. The system will update the current series in the text box.
2. Edit the series as required with unique prefixes for each series.
  he first prefix will be the default prefix. Each new prefix Naming Series must be added on a new line. The newly added naming series will be available in the document.

![document naming settings](/files/document_naming_settings.gif)

3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox.
  here will be no default naming series if this is ticked.
4. You can also update the starting point of a series by entering the series name and the starting point in the “Update Series” section.
5. Click on the Update button to update the set of Naming Series for the selected document.

> Note: To see the newly added Naming Series, click on Settings > Reload.

## 2. Financial Year in Naming Series

You can also show the financial year in the Naming Series. By default, if you enter 'YYYY' in the naming series, it'll pick up the current year. To set naming series based on the fiscal year, enter something like 'ACC-SINV-.19-20.-' where 19-20 is the current Fiscal Year. It is common to have a separate series for each financial year.

As you can see, in the following screenshot of a Sales Invoice, the year 2019 is listed:

![Fiscal year in Naming Series](/files/year-naming-series.png)

## 3. Updating the current value for existing Naming Series

You can change the starting/current sequence number of an existing series.

1. Under the Update Series section, select the prefix whose sequence is to be changed.
2. The current value will be fetched and displayed.
3. Change starting/existing sequence number if needed.
4. Click on Update Series Number.

For example, if the current Sales Order series number is at 16, and you want to restart or set it as 50, enter 0 or 50 depending on your case. Any new Sales Order created will start from the new sequence number.

To know more about this, [visit this article](/erpnext/naming-series-current-value).

> Tip: You could have a separate series for each type of Customer or for  
each of your retail outlets.

## 4. Using Field Values in Naming Series

Some companies prefer to make use of "short-codes" for suppliers, i.e. WN for company "Web Notes" that later can be used in naming series for quick identification.

For example:

 A custom field "Vendor ID" is created under Document: Supplier.  
 Then under Naming Series, we allow something like  
 PO-.YY.MM.-.vendorid.-.####  
 Resulting in "PO-1503-WN-00001"

## 5. Updating Amended Documents

Some companies prefer naming amended documents as new documents. ERPNext provides a feature to configure this setting based on your requirements.

To configure the naming of amended documents:

1. Navigate to the Amended Documents section.
2. Choose one of the following options:
  1. Apply the Default Amend Counter to change the naming for all doctypes.
  2. Customize naming for specific doctypes by selecting the relevant doctypes and defining their naming methods.

![Amended Naming Series](/files/Screenshot%202024-11-21%20at%2012.17.06%E2%80%AFPM.png)



3. Click "Update Amendment Counter" to save your changes.

## 6. Video


<iframe allowfullscreen="" height="315" width="100%" frameborder="0" src="https://www.youtube.com/embed/IGyISSfI1qU"></iframe>


## 7. Related Topics

1. [Bulk Rename](/erpnext/bulk-rename)

<!-- page: erpnext/erpnext__document-naming.md -->
---
title: "Document Naming Rule"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-naming"
updated: "2026-03-04"
---

In ERPNext, managing naming conventions systematically helps maintain consistency and traceability across your records. The Document Naming Rule feature allows you to set up dynamic naming based on conditions, offering more flexibility than the standard Document Naming Settings (Series).

✨ Key Differences from Traditional Naming Settings
While Document Naming Settings apply a prefix or pattern globally to a doctype, Document Naming Rule introduces conditional logic to apply naming series based on specific field values within the document.

🛠️ How to Set Up a Document Naming Rule
Follow the steps below to configure a Document Naming Rule:

**Steps:**

1. Select the Document Type
Choose the Doctype (e.g., Sales Invoice, Customer, etc.) where the rule will apply.


2. Set Priority
Assign a Priority number to the rule.

🔹 Higher priority rules (e.g., 10) are applied before lower ones (e.g., 5).
🔹 If multiple rules match, the one with the highest priority is used.

![Selsct a DocType](/files/Screenshot%202025-06-16%20at%205.19.58%E2%80%AFPM.png)

3. Add Rule Conditions
➕ You can add multiple conditions per rule. The rule is applied only when all conditions are satisfied.

🔍 Example Use Case
Scenario: You want to name Customers based on their location.

If the customer's Country is India, the naming format should be:
CUST-INDIA-00001, CUST-INDIA-00002, ...

This can be achieved using two Document Naming Rules:

Rule 1: Prefix = CUST-INDIA-, Condition = Country = India

Rule 2: Prefix = CUST-USA-, Condition = Country = USA

If the Country is USA, the format should be:
CUST-USA-00001, CUST-USA-00002, ...

4. Define the Prefix
Enter the desired prefix in the Prefix field under the Naming section.
Example: PSI/


5. Set the Serial Number Start
Specify the starting serial number in the field next to the prefix.
Example: 5 → The first document will be named PSI/00005

![](/files/Screenshot%202025-06-19%20at%203.44.10%E2%80%AFPM.png)

Here is an Example:


✅ Benefits
Automates naming based on document fields

Reduces manual selection and human error

Supports multiple naming patterns within the same Doctype

Useful for companies with multi-branch, multi-country, or multi-category document types

📝 Notes
Always ensure the conditions are specific enough to avoid conflicts between rules.

If no rule matches, the system will fall back to the default Naming Series (if configured).

<!-- page: erpnext/erpnext__document-title-with-multiple-fields.md -->
---
title: "Document Title with multiple fields"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-title-with-multiple-fields"
updated: "2026-03-04"
---

Ever wondered about creating a document title with more than one field? For example, let's say your sales invoice should have the title of the customer name (which is present by default) and its tax ID.

How will you do this? Well, here's an interesting customisation ability of the framework which can do this without any need of scripting.

 

Here are the steps,

1. Make sure you have a field that is going to be referred to for creating the title of the document.
2. The basic setup ends by adding this field name in the view settings of the doctype for the title.
3. If you want to add more to it,
4. Add the field links in the **default** of the field in this format **{field_name}**

 

**_Here's an example of how it looks_**

![](/files/Eb81KLe.png)

 

         b. This will result in a multifield title for the selected doctype.

 

This can be extended to creating a custom field with consolidated values of different fields and merging them to a completely new field. The best use case is creating addresses for custom doctypes easily without any custom scripting.

 

This is how the field configuration will look

 

![](/files/FXuN3dK.png)

 

Note: We are using options for adding values because it updates the field by changing its source fields. (Doest work with defaults)

Also, the field type should not be data. (Could be read-only or HTML)

 

Here's the output of the above configuration

 

![](/files/gHpmXZY.png)

<!-- page: erpnext/erpnext__document-title.md -->
---
title: "Document Title\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-title"
updated: "2026-02-26"
---


**You can customize the title of documents based on properties so that you have meaningful information for the list views.**

For example, the default title on a Quotation is the customer name, but if you are dealing with only a few customers and sending lots of quotations to each customer, you may want to customize.

![Document Title](/files/document-title.png)

## Setting Title Fields

From ERPNext Version 6.0 onwards, all transactions have a 'Title' property. If there is not a title property, you can add a **Custom Field** as title and set the **Title Field** via **Customize Form**.

You can set the default value of that property by using Python style string formatting in **Default** or **Options**

1. To edit a default title, go to Customize Form
2. Select the Form for which you would like to change the Title Field.
3. Edit the **Title Field** in the form.

## Defining Titles

You can define the title by setting document properties in braces `{}`. For example, if your document has fields `customer_name`, you can specify that as the Title of the Form.

![Set Document Title](/files/set-document-title.gif)

Alternatively, you can also define a particular field as the 'Title Field' in Customize Form.

![Title Field](/files/title-field-in-view-settings.png) 

## Fixed or Editable Titles

If your title is generated as a default title, it can be edited by the user by clicking on the heading of the document.

![Editable Title](/files/customize-document%20title.gif)

If you want a fixed title, you can set the rule in the **Options** property. In this way, the title will be automatically updated every time the document is updated.

<!-- page: erpnext/erpnext__document-versioning.md -->
---
title: "Document Versioning\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/document-versioning"
updated: "2026-03-04"
---

**In ERPNext, Document Versioning is a feature that allows you to track all the changes made in a form or a document.**

This feature comes handy while conducting an Audit Tail to check on what changes were made in a document along with the time of change and the stakeholder responsible.

![Document Versioning](/files/using-document-versioning-1.png)

## How to Enable Document Versioning

Let's assume that we need to enable Document Versioning for Purchase Order.

1. Go to Purchase Order List.
2. Click on Customize from the drop-down menu.
3. You shall be directed to the [Customize Form](/erpnext/customize-form) page for Purchase Order.
4. Check the field "Track changes" in the Properties.
  [Document Versioning](/files/using-document-versioning-2.gif)

With this, Document Versioning shall be enabled for all the Purchase Orders edited henceforth.

### Version Log

For each document that has Document Versioning enabled, a Version Log is created. Herein, there will be links to specific versions of the document.

When you click on these links, you will be directed to a log of all the fields and the changes made therein.

![Document Versioning](/files/using-document-versioning-3.gif)

<!-- page: erpnext/erpnext__domain-settings.md -->
---
title: "Domain Settings | ERPNext Documentation"
description: "Use ERPNext Domain Settings to keep relevant business domains active and understand how domains differ from modules, workspaces, and permissions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/domain-settings"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. Its employees sell devices, manage warehouses, assemble selected products, and maintain equipment. They do not run a school or a healthcare facility. If every industry-specific feature is shown, a warehouse user may waste time searching through Student, Patient, or other records that have nothing to do with the job.



Domain Settings lets the administrator keep only the relevant business domains active across the site. This makes navigation and available business features easier to understand. It is not a security boundary: roles, permissions, User Permissions, and Workspace rules must still control who may read or change data.

## Select active domains

Open **Domain Settings**, review the domains available from the installed apps, and select only the domains the organisation genuinely uses. Nova keeps manufacturing and distribution-related functionality available while leaving unrelated industry domains inactive.

![Active Domains area in ERPNext Domain Settings](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-domain-settings.png)


| Setting        | What it means                         | Nova example                                                                                               |
| -------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Active Domains | Business domains enabled for the site | Nova enables a relevant manufacturing domain but does not enable Education merely to explore its DocTypes. |


After saving, reload Desk and verify the affected workspaces, DocTypes, and navigation. Also test with a normal user's roles. A domain can make a feature available, while permission still decides whether the user can access it.

## Domain Settings versus nearby controls


| Control                    | Use it for                                                                        | Do not use it for                    |
| -------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| Domain Settings            | Activating an installed business domain                                           | Restricting one user's data          |
| Module Settings            | Changing process behaviour within a module                                        | Hiding data from unauthorised users  |
| Roles and Role Permissions | Granting DocType actions                                                          | Selecting which industry is relevant |
| User Permissions           | Restricting particular Companies, territories, customers, or other linked records | Enabling an installed domain         |
| Workspace configuration    | Controlling navigation and cards                                                  | Replacing server-side permissions    |


## Troubleshooting

### A DocType disappeared after changing domains

Re-enable the required domain and reload Desk. Then verify that the app remains installed and the user has the required role.

### A user can access a record even though its workspace is hidden

Navigation visibility is not permission. Review Role Permissions and User Permissions for the DocType and record.

### A domain is not available to select

Confirm that the app supplying it is installed and compatible with the current version. Domain Settings cannot activate code that is not installed.

## Frequently asked questions

### Should every available domain be enabled?

Enable only the domains the organisation uses. Extra domains add navigation and records that can confuse users.

### Does disabling a domain delete data?

Do not treat domain selection as deletion. Existing records may remain in the database even when the related interface becomes unavailable. Re-enable the domain and verify before making structural changes.

### Can one user have a different domain?

Domain Settings is site-wide. Use roles, permissions, and workspace configuration for user-specific access and navigation.

### Is a domain the same as a module?

A domain represents a business context that can activate related functionality. A module groups application features. They overlap, but they are not interchangeable.

## Related topics

- [Module Settings](/erpnext/module-settings)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [User Permissions](/erpnext/user-permissions)
- [Workspace](/erpnext/workspace)
- [System Settings](/erpnext/system-settings)
- [Adding Users](/erpnext/adding-users)

<!-- page: erpnext/erpnext__download-backup.md -->
---
title: "Downloading Backups"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/download-backup"
updated: "2026-02-26"
---

In ERPNext, you can manually download a database backup.

To get the latest database backup, go to:

> Home  > Download Backups

Backup available for the download is updated every eight hours. Click on the link to download the backup at a given time.

If you want to set the number of Backups available for download at a time, then click on 'Set Number of Backups', which will navigate you to 'System Settings', where you can set the number.

![](/files/imageb48716.png)
*Download backup post backup taken*

![](/files/imageef9524.png)

## Downloading Files Backup

Clicking on Download Files Backup will send an email with links to the backup for both private and public files. Email must be configured for this to work.

![](/files/image0646b1.png)

## Getting Backup Encryption Key

In order to get the backup encryption key, click on the designated button. Upon getting your system password validated, the system will provide you with the encryption key.

![](/files/imageed3623.png)

## Automating Backups to Cloud Storage

You can also automate your backups to be uploaded directly to a cloud storage platform. Currently, ERPNext supports:

1. Amazon S3
2. Dropbox
3. Google Drive

<!-- page: erpnext/erpnext__downtime-analysis.md -->
---
title: "Downtime Analysis\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/downtime-analysis"
updated: "2026-03-02"
---


To access the Downtime Analysis report, go to:

> Home > Manufacturing > Reports > Downtime Analysis

![Task](/files/downtime-analysis.png)

This report will give information about the captured Machines Downtime in hours. Using Downtime analysis report, operators will know which machine was not performing well and needs maintenance.

<!-- page: erpnext/erpnext__downtime-entry.md -->
---
title: "Downtime Entry\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/downtime-entry"
updated: "2026-02-26"
---


To access the Downtime Entry, go to:

> Home > Manufacturing > Production > Downtime Entry

![Production Forecasting](/files/downtime-entry.png)

Downtime Entry document is used to capture the machine's Downtime in minutes. User needs to manually create the downtime record by selecting the proper machine alongwith the machine's down time. Using Downtime entry data operator knows which machine not performing well and needs maintenance.

<!-- page: erpnext/erpnext__drop-shipping-in-erpnext.md -->
---
title: "Drop Ship | ERPNext Documentation"
description: "Set up drop shipping in ERPNext so suppliers deliver items directly to customers through linked Sales Orders and Purchase Orders."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/drop-shipping-in-erpnext"
updated: "2026-07-23"
---

Drop shipping lets a Supplier deliver an item directly to your Customer. Your company creates the Sales Order and Purchase Order, but the goods do not pass through your warehouse. ERPNext links the two transactions so purchasing and sales teams can follow the same fulfilment.

![Drop-ship Sales Order with the customer, delivery date, supplier-delivered items, quantities, rates, and stock indicators.](/files/drop-ship-sales-order76e80b.webp)

## Before you begin

Create the [Customer](/erpnext/customer), Supplier, [Item](/erpnext/item), selling and buying prices, Customer shipping address, and Supplier contact details. The Item must have a Default Supplier or an appropriate supplier must be selected during purchasing.

## Create a drop-ship Sales Order

1. Go to **Selling > Sales > Sales Order** and select **Add Sales Order**.
2. Select the Customer, Company, and delivery date.
3. Add the Item and Quantity.
4. Open the item row with the pencil icon.
5. Enable **Deliver to Customer** for the row.
6. Select the Supplier and confirm the Customer shipping address.
7. Save and submit the Sales Order.

![The highlighted pencil icon opens the complete Sales Order item row.](/files/drop-ship-item-pencil.webp)

The stock indicator before an Item Code is green when the item is in stock and red when it is out of stock. Drop shipping does not require the item to be received into your warehouse, but the indicator can still help users understand the item’s current availability.

![The item row with Supplier delivers to Customer enabled and Apex Devices selected as the Supplier.](/files/drop-ship-item-fields.webp)

![The Customer and company address information used for the drop-ship transaction.](/files/drop-ship-customer-address.webp)

## Create the Purchase Order

From the submitted Sales Order, select **Create > Purchase Order**. In the dialog, select the Supplier and the drop-ship items, then create the Purchase Order.

Review the following before submission:

- **Is Subcontracted** should remain disabled unless the transaction is genuinely subcontracting.
- **Supplier** must be the party that will ship the goods.
- **Customer** and **Customer Address** must identify the final delivery destination.
- The items, quantities, rates, taxes, schedule dates, and terms must match the supplier agreement.

Submit the Purchase Order and send the approved document or instructions to the Supplier.

## Important fields and what they mean


| Field                 | What it means                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Deliver to Customer   | Marks the Sales Order item for direct delivery by a Supplier.                                                               |
| Supplier              | The Supplier expected to fulfil that item.                                                                                  |
| Customer              | The party receiving the goods. It is mapped to the Purchase Order for drop shipping.                                        |
| Customer Address      | The shipping destination printed or shared with the Supplier.                                                               |
| Schedule Date         | The date by which the Supplier should deliver the item.                                                                     |
| Warehouse             | Usually not used to receive a drop-shipped item because it does not enter your stock.                                       |
| Delivered By Supplier | Indicates that fulfilment is performed by the Supplier. Availability and wording can depend on the transaction and version. |


## Complete the sales cycle

A drop-ship Purchase Order does not create a stock receipt for your company. When the Supplier confirms delivery, use the actions available on the linked Sales Order or Purchase Order to record the delivery status according to your ERPNext version and process.

Create the [Sales Invoice](/erpnext/sales-invoice) for the Customer and the Purchase Invoice for the Supplier. Verify linked quantities so the Sales Order, Purchase Order, receivable, and payable all represent the same fulfilment.

If only part of an order is drop shipped, keep the remaining items on the normal warehouse fulfilment path. Each row can follow the appropriate route, but teams should verify the linked documents carefully.

## Returns and exceptions

If the Customer returns a drop-shipped item, coordinate the commercial and physical return with the Supplier. Create the appropriate return or credit documents for both sides. Because the goods did not enter your warehouse during the original delivery, do not create a warehouse receipt unless your return process actually brings them into your stock.

If the Supplier cannot fulfil the order, update or cancel the affected Purchase Order and resolve the Customer commitment on the Sales Order. Do not leave an open quantity without an owner or revised delivery date.

## Frequently asked questions

### Does drop shipping update stock?

Normally no. The Supplier delivers directly to the Customer, so the item does not pass through your warehouse.

### Can one Sales Order contain warehouse and drop-ship items?

Yes. Mark only the rows that the Supplier will deliver directly. Fulfil the other rows through Delivery Notes from your warehouse.

### Can different Suppliers fulfil different items?

Yes. Create the required Purchase Orders by Supplier and confirm that each item row is linked correctly.

### Why is the Purchase Order not available from the Sales Order?

Check that the Sales Order is submitted, the item row is marked for delivery to the Customer, a Supplier is selected or available, and the quantity is not already fully ordered.

### Who sends the invoice to the Customer?

Your company normally invoices the Customer. The Supplier invoices your company under the linked purchase transaction.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)
- [Delivery Note](/erpnext/delivery-note)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Drop Ship Between Subsidiary Companies](/erpnext/drop-ship-between-subsidiary-companies)

<!-- page: erpnext/erpnext__dropbox-backup.md -->
---
title: "Setting Up Dropbox Backups"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dropbox-backup"
updated: "2026-03-06"
---

We always recommend customers to maintain backup of their data in ERPNext. The database backup is downloaded in the form of an SQL file. If needed, this SQL file of backup can be restored in the another ERPNext account as well.

You can automate database backup download of your ERPNext account into your Dropbox account.


&gt; Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: &lt;https://frappecloud.com/docs/sites/backups&gt;
&gt; 
&gt; 

To setup Dropbox Backup, &gt; Home &gt; Integrations &gt; Dropbox Settings

  


#### Step 1: Login to Dropbox Developer area

&lt;https://www.dropbox.com/developers/apps&gt;

  


#### Step 2: Create a new Dropbox app

![Create new](/files/dropbox-open-3.png)  


  


#### Step 3: Fill in the details for your new app

![Choose Dropbox API and type as APP Folder](/files/dropbox-open-1.png) ![Setup APP Name](/files/dropbox-open-2.png)  


![https://support.frappe.io/files/nBdh7wu.png](https://support.frappe.io/files/nBdh7wu.png)  


#### Step 4: Insert your custom domain Redirect URI

`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish` ![Set Redirect URL](/files/dropbox_redirect_uri.png)  


  


#### Step 5: In a new window, open the Dropbox Settings page in your ERPnext installation

  


#### Step 6: Set backup frequency and email

Set the frequency to download your site backups to your Dropbox account. ![set frequency](/files/setup-backup-frequency.png)  


#### Step 7: Input Keys from your Dropbox App window

From your Dropbox App page, enter the app key and (unhidden) app secret into the ERPnext Dropbox settings page.

Alternatively, you can enter it manually in `sites/{sitename}/site_config.json` as follows,


```
       {
 "db_name": "demo",
 "db_password": "DZ1Idd55xJ9qvkHvUH",
 "dropbox_access_key": "ACCESSKEY",
 "dropbox_secret_key": "SECRECTKEY"
}

    
```
  


#### Step 8: Click Save before continuing

  


#### Step 9: After saving, click "Allow Dropbox Access"

The Dropbox login page will open in the new tab. This might require you to allow pop-up for your ERPNext account.

  


#### Step 11: Allow Dropbox Access

On successful login, you will find a confirmation message as following. Click on "Allow" to let your ERPNext account have access to your Dropbox account. ![Allow](/files/dropbox-3.png)  


  


#### Step 12: Confirm Backups Work

From the ERPnext Dropbox page, click `Take Backup Now` and then go to you Dropbox files view. You should see a new folder in Dropbox named `Apps` and inside of it your {New App} folder. Inside of it should be backup folders for both files and database. So for an app named `erpnext`, following are the folder locations:


```
Database files: /Apps/erpnext/database
Public files: /Apps/erpnext/files
Private files: /Apps/erpnext/private/files
  

```
&gt; **Note**: If the compressed backup size exceeds 1GB (Gigabyte), the system will upload the latest available backup to Dropbox instead of generating a new backup file.

<!-- page: erpnext/erpnext__dunning.md -->
---
title: "Sales Interest and Dunning | ERPNext Documentation"
description: "Set up formal overdue-payment reminders with interest, fees, letter text, and payment processing in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dunning"
updated: "2026-08-14"
---

Northstar Retail has not paid an invoice by its due date. Nova Industries can see the overdue balance in Accounts Receivable, but the customer now needs a formal notice that states what is overdue, the interest or reminder fee being charged, and the amount required to settle it.



A **Dunning** turns that overdue balance into a traceable collection document. It brings the relevant Sales Invoice instalments into a formal reminder, calculates optional interest and fees, stores the letter sent to the Customer, and links the eventual payment back to the demand.



Use Dunning when ordinary follow-up is no longer enough and your collection policy requires a formal reminder. It does not replace the Sales Invoice or create another sale. This guide explains how to configure reusable Dunning Types, issue the notice, and record the payment that resolves it.

## Before you begin

- The [Sales Invoice](/erpnext/sales-invoice) must be submitted and overdue.
- Create at least one Dunning Type.
- Choose the income account and Cost Center that should receive interest and dunning fees.

## Set up a Dunning Type

A Dunning Type stores reusable defaults for the reminder. Create different types for stages such as first reminder, second reminder, and final notice.


| Field                       | What it controls                                  |
| --------------------------- | ------------------------------------------------- |
| Is Default                  | Applies this type automatically when appropriate  |
| Dunning Fee                 | Fixed charge added to the reminder                |
| Rate of Interest (%) Yearly | Annual rate used to calculate interest            |
| Dunning Letter              | Language-specific body and closing text           |
| Income Account              | Account credited when fees and interest are paid  |
| Cost Center                 | Cost Center used for the fee and interest posting |


![Dunning Type with fee, interest, reminder text, and accounting defaults](https://novacompanies.m.frappe.cloud/files/dunning-type-clean.png)

## Create a Dunning

### From an overdue Sales Invoice

1. Open the overdue Sales Invoice.
2. Select **Create &gt; Dunning**.
3. Review the overdue payment schedule rows fetched into the document.
4. Select a **Dunning Type**, or enter the fee, interest, and letter text manually.
5. Save and submit.

### From the Dunning list

1. Open the Dunning list and select **Add Dunning**.
2. Select the Customer.
3. Select **Fetch Overdue Payments**.
4. Choose the overdue rows and select **Get Items**.
5. Complete the reminder details, then save and submit.

The Dunning must reflect the amount you intend to collect. Review the invoice rows, interest, fee, total outstanding, income account, and Cost Center before submission.

## Record payment

When the customer pays the invoice together with the interest and fee:

1. Open the submitted Dunning.
2. Select **Create &gt; Payment**.
3. Review the referenced invoices and the additional amount.
4. Submit the Payment Entry.

ERPNext records the interest and fee through the deductions or loss section of the Payment Entry and resolves the Dunning after the full amount is received.

## Statuses


| Status     | Meaning                                                   |
| ---------- | --------------------------------------------------------- |
| Draft      | Reminder has not been submitted                           |
| Unresolved | Submitted, but the required payment has not been received |
| Resolved   | Outstanding amount, interest, and fee have been settled   |
| Cancelled  | Submitted Dunning was cancelled                           |


## Troubleshooting

**Create Dunning is not available**

Confirm that the Sales Invoice is submitted, has an outstanding amount, and is past its due date.

**Interest or fee posts to the wrong account**

Review the Income Account and Cost Center on both the Dunning Type and the Dunning before creating the Payment Entry.

**The Dunning remains unresolved**

Open the linked Payment Entry and verify that it is submitted and covers all referenced invoice, interest, and fee amounts.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Accounts Receivables](/erpnext/accounts-receivables)
- [Process Statement Of Accounts](/erpnext/process-statement-of-accounts)
- [Payment Terms](/erpnext/payment-terms)

<!-- page: erpnext/erpnext__duplicate-record.md -->
---
title: "Duplicate Records\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/duplicate-record"
updated: "2026-03-04"
---


**'Duplicate' is a feature that helps you to copy values of existing document as-is into a new document.**

## Scenario

A customer has placed a 'reorder' for certain items with an electronic items supplier.

Since the new Sales Order will have all the details the same as that of the original Sales order, the supplier can simply open the original one and 'Duplicate' the order. The values of the original document will get updated as it is in the new Sales Order. Any changes, if required can be made thereafter.

To make a Duplicate document, you can go to the original document and click on 'Duplicate' from the Drop-Down menu.

![Duplicate Record](/files/using-duplicate-record-1.gif)

<!-- page: erpnext/erpnext__dynamic-link-fields.md -->
---
title: "Dynamic Link Fields\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/dynamic-link-fields"
updated: "2026-03-04"
---


Dynamic Link field is a field which can search and hold the value of any DocType. Let's consider an example to learn how Dynamic Link field works.

While creating Opportunity or Quotation, we have to explicitly define if it is for a Lead or a Customer. Based on our selection (Lead/Customer), another link field shows up where we can select the actual Lead or Customer.

If you set the former field as Dynamic Link, where we select actual Lead or Customer, then the later field will be automatically linked to master selected in the first field, i.e. Leads or Customers. Hence we need not insert separate link fields for Customer and Lead.

Below are the steps to insert Custom Dynamic Field. For instance, we will insert Dynamic Link Field in Journal Entry.

#### Step 1: Insert Link Field for DocType

First, we will create a link field that will be linked to the DocType.

![Custom Link Field](/files/customize-dynamic-link-1.gif)

By **DocType** mentioned in the Option field, we mean parent DocType. So, just like Quotation is one DocType, which has multiple Quotation under it. Same way, DocType is also a DocType which has Sales Order, Purchase Order and other doctypes created as DocType records.

**DocType**  

---- Sales Order  

---- Purchase Invoice  

---- Quotation  

---- Sales Invoice  

---- Employee  

---- Work Order  

.. and so on.

So linking this field with parent DocType will list all the DocType records.

![journal Voucher Link Field](/files/customize-dynamic-link.png)

#### Step 2: Insert Dynamic Link Field

This custom field's type will be "Dynamic Link". In the Option field, the name of the Doctype link field will be mentioned.

![Custom Dynamic Field](/files/customize-dynamic-link-2.gif)

This field will allow selecting document id, based on the value selected in the Doctype link field. For example, if we select Sales Order in the prior field, the Dynamic Link field will list all the Sales Orders ids.

![Custom Dynamic Field](/files/customize-dynamic-link-3.gif)

**Customizing options in the Doctype Link field**

By default, the DocType link field will provide all the forms/docTypes for selection. If you wish this field to show certain specific docTypes in the search result, you will need to write Custom Script for it.

<!-- page: erpnext/erpnext__e-commerce-integrations-for-erpnext.md -->
---
title: "E-commerce Integrations for ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e-commerce-integrations-for-erpnext"
updated: "2026-07-04"
---

ERPNext is easy to integrate with recommerce and ecommerce platforms because business data in ERPNext is available through the Frappe Framework REST API. Products, customers, orders, invoices, payments, shipments, returns, and stock movements are stored as DocTypes, and DocTypes can be read or updated through standard API endpoints.

This makes ERPNext a practical backend for recommerce platforms that handle refurbished, pre-owned, rental, buyback, resale, or reverse-logistics workflows. The storefront can focus on customer experience, while ERPNext manages inventory, accounting, fulfillment, purchasing, returns, and reporting.

## Why Integration Is Straightforward

- **REST APIs are available by default:** External systems can create and update ERPNext records without direct database access.
- **Commerce records already exist:** Items, Customers, Sales Orders, Sales Invoices, Delivery Notes, Payment Entries, Stock Entries, and Warehouses are standard ERPNext records.
- **Recommerce data can be added:** Fields such as condition, grade, serial inspection, refurbishment status, warranty, buyback source, and resale channel can be added with custom fields or DocTypes.
- **Sync can be automated:** Webhooks, scheduled jobs, and background workers can sync orders, stock, payment status, shipment updates, and returns between systems.

## Common Integration Flows

- **Catalog sync:** Send item details, prices, images, condition, and stock availability from ERPNext to the platform.
- **Order sync:** Create Sales Orders or Sales Invoices in ERPNext when orders are placed.
- **Inventory sync:** Update the platform when stock is reserved, sold, returned, refurbished, or made available again.
- **Fulfillment sync:** Send shipment and tracking details from ERPNext back to the platform.
- **Returns and buybacks:** Track incoming goods using Stock Entries, Purchase Receipts, Quality Inspections, or custom DocTypes.

## Ready-Made Marketplace Options

Before building a custom connector, check whether an existing Frappe Marketplace app already covers the workflow:

- [Ecommerce Integrations](https://cloud.frappe.io/marketplace/apps/ecommerce_integrations): E-commerce marketplace integrations for ERPNext.
- [WooCommerce Connector](https://cloud.frappe.io/marketplace/apps/woocommerceconnector): Synchronizes items, stock, customers, addresses, sales orders, sales invoices, and payment entries with WooCommerce.
- [ERPNext Shipping](https://cloud.frappe.io/marketplace/apps/erpnext_shipping): Shipping integration for ERPNext, useful for fulfillment and tracking.
- [Frappe Paystack](https://cloud.frappe.io/marketplace/apps/frappe_paystack): Payment gateway integration for ERPNext and Frappe.

## When To Build A Custom Connector

Build a custom connector when the recommerce platform has unique flows such as device grading, serialized refurbishment, trade-in pricing, warranty tracking, marketplace-specific listing rules, or reverse logistics. In most cases, the connector maps platform events to ERPNext documents and calls the REST API securely.

## Best Practices

- Keep ERPNext as the source of truth for stock and accounting.
- Use stable external IDs to match ERPNext records with platform records.
- Log every sync attempt so failed updates can be retried.
- Use API keys with limited permissions and test on a staging site before going live.

## Related Topics

- [Frappe REST API](/framework/user/en/api/rest)
- [Sales Order](/erpnext/sales-order)
- [Item](/erpnext/item)
- [Stock Entry](/erpnext/stock-entry)
- [Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace)

<!-- page: erpnext/erpnext__e_commerce_search.md -->
---
title: "E-commerce Search"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e_commerce_search"
updated: "2026-03-02"
---

All Product Listing pages contain a **Search bar** that lets users quickly search for Website Items or Item Groups. It also stores recent searches that you can click on and reuse.

![Search](/files/e-commerce-search.png)

## RediSearch

> **Experimental**: Requires Redis 6+


By default ERPNext performs a simple DB search but you can **optionally** choose to use [RediSearch](https://redis.com/modules/redis-search/) for super fast search instead. You can refer to RediSearch's [installation documentation](/erpnext/installing_redisearch_to_enable_super_fast_e_commerce_search).


> Go to > **E Commerce Settings** > **Item Search Settings** > Check **Enable Redisearch**

![Item Search Settings with RediSearch](/files/item-search-settings-enabled.png)

#### Settings without RediSearch
If RediSearch is not installed, this is what the **Item Search Settings** will look like:
![Item Search Settings without RediSearch](/files/item-search-settings.png)

#### Configurable Fields
Along with fast search you get the option to configure fields that you want search to consider. Add comma separated fields in the **Search Index Fields** text box to make them searchable.

E.g. Adding **brand** to these fields makes it searchable. Typing a brand, e.g. 'Apple', should give results where the brand is 'Apple'.

The results will be based on values in all the fields mentioned in the **Search Index Fields** text box.

> Fields of the foll.g types are supported: **Link**, **Table MultiSelect**, **Data**, **Small Text**, **Text Editor**

<!-- page: erpnext/erpnext__e_commerce_settings.md -->
---
title: "E Commerce Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e_commerce_settings"
updated: "2026-03-02"
---

The legacy **Shopping Cart Settings** and **Products Settings** are combined into a single **E -Commerce Settings** page. 

The e-commerce settings in ERPNext can be leveraged by users to manage and streamline the online sales processes. These settings can enable users to efficiently manage product listing, customer management and integration with other ERPNext modules seamlessly.


> **E Commerce Settings / Webshop Settings** in the awesomebar (search bar)
> 
> 

![E Commerce Settings](/files/e_commerce_settings_overview.png) *E Commerce Settings*

### Products Per Page

Define how many products to show per page on the Product Listing in the **All Products** page (`/all-products`).

### Filters and Categories

![Filters and Categories](/files/filters_and_categories.png) *Filters and Categories*

You can also add filters to your listing. There are two types of filters:

1. **Field Filters**: Enable the **Field Filters** checkbox and add the fields based on which you want to have filters. These fields will also be used as categories for the **Shop by Category** page.
2. **Attribute Filters**: Enable the **Attribute Filters** checkbox and add the attributes based on which you want to have filters.

### Display Settings

1. **Hide Variants**: Only show Website Item Templates on the Product Listing.
2. **Enable Variant Selection**: Show a configure button if the Item has variants. It can be used to narrow down the specific item based on Attributes.
3. **Show Price**: Show Item Price on the product page.
4. **Show Stock Availability**: Show whether the Item is in stock.
5. **Show Stock Quantity**: Show available stock on the product page.
6. **Allow items not in stock to be added to cart**: Allow items not in stock to be added to Cart.
7. **Show Apply Coupon Code**: Additional provision to apply coupon code at checkout.
8. **Show Contact Us Button**: Show a contact us button which customers can use to enquire about the Item. It will create a Lead in the system.
9. **Show Public Attachments**: Show public attachments in the Sales Order generated, after checkout, for Customers.


> You can **Hide Variants** only when Attribute Filters are disabled.
> 
> 

### Shopping Cart

1. **Company**: Specify the company that the web shop is set up for.
2. **Price List**: Mention Price List to consider while fetching Item Prices.
3. **Enable Shopping Cart**: Add the provision to add items to Cart.
4. **Default Customer Group**: Add the Default Customer Group to be set while auto creating customers on adding to Cart.

### Checkout Settings

1. **Enable Checkout**: If checkout is disabled, when your customers add an item to Cart, they can click on the **Request for Quotation** button to get a quote for it. A [Quotation](/erpnext/quotation) is generated in the system. If enabled, a [Sales Order](/erpnext/sales-order) is generated on clicking on the **Place Order** button in the Cart.
2. **Payment Gateway Account**: If checkout is enabled, you must have [PayPal Integration](/erpnext/paypal-integration) or [Razorpay Integration](/erpnext/razorpay-integration).
3. **Payment Success Url**: After payment completion redirect users to the selected option.
4. **Show Price in Quotation**: If checkout is disabled, you can choose whether or not to show prices against Website Items in the Quotation.
5. **Save Quotations as Draft**: If checkout is disabled, on clicking on the **Request for Quotation** button, you can choose whether the auto-generated Quotation must be auto-submitted or kept in the Draft state.

### Add-ons

1. **Enable Wishlist**: Add the provision to add items to a Wishlist
2. **Enable Reviews and Ratings**: Add the privision for **customers** to leave reviews and ratings against Website Items.
3. **Enable Recommendations**: Add the provision to show manually selected **recommended items** against a Website Item.

### Shop By Category

The **Shop By Category** page is an out-of-the-box page that lists categories linked to Website Items. These categories can be configured in the **Filters and Categories** section's **Field Filters** table.

You can also select a slideshow as the banner of the page.

### Guest Display Settings

1. **Hide Price for Guest**: You can show or hide prices against Website Items for guest users (users who are not logged in).
2. **Redirect on Action**: If a guest user tries to add a Website Item to Cart or to the Wishlist, you can select a URL to redirect them to. By default, guest users are redirected to the `/login` page. You can instead redirect them to a custom Web Form of choice by adding a URL here e.g. `/contact-us`

<!-- page: erpnext/erpnext__easy-steps-to-setup-workflow.md -->
---
title: "Easy steps to setup Workflow"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/easy-steps-to-setup-workflow"
updated: "2026-03-04"
---

When a company has multiple levels of approval for a document, a Workflow can be set.   
In ERPNext, you can go to Workflow list --> Create New --> Name the workflow and define :1. States
2. Transition rules.

  
1. States :

When a document is passed on for different levels of approval, there are states defined at each level for the role of the user.   
![](/files/Y3TzzU2.png)  
  
1. Transition Rules :

For instance: A **Sales user** is only allowed to create a **Quotation** and it can be saved in the **Draft** state. Further, it can be sent to the **Sales Manager** for approval and the User with this role can have the permission to either **Approve** or **Reject** the Quotation after which it can either be sent to the **Draft** State if **Rejected** or final **Approved** State.   
![](/files/xJUtkGy.png)  
Error Messages: **A document cannot be Cancelled before it is Submitted.**   
[This is a typical error faced by users who define the state of the Document cancelled before Submitting it. Doc Status 1 defines that the Document will be Submitted at that State, thus the State with Doc status 2 should only be defined in the Transition after the State with Doc status 1. ]  
Setup a Simple Workflow to begin with and let us know what you think more on Workflows! We love to see our Users Happy!! ;)   
  

<!-- page: erpnext/erpnext__edit-submitted-document.md -->
---
title: "Edit Submitted Document\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/edit-submitted-document"
updated: "2026-03-04"
---


To edit a submitted document, you need to cancel it first. Following are steps to edit submitted document. These steps assume you have the appropriate permissions for cancelling and editing a document.

#### Step 1: Cancel Submitted Document

You will find Cancel button on upper right corner of submitted document.

![Cancel Doc](/files/edit-submitted-doc-1.png)

#### Step 2: Amend the document

On cancellation of submitted document, Amend button will be became visible.

![Amend Doc](/files/edit-submitted-doc-2.png)

#### Step 3: Save and Submit the document

On clicking Amend button, same document will become editable again. After Making required changes, save and submit the document.

![Resave and Submit Doc](/files/edit-submitted-doc-3.png)
Note: If your document is linked with other documents, then you will need to cancel the dependant document before cancelling the parrent document.

Example: If you have created Delivery Note and Sales Invoice against Sales Order, which you need to amend, then you should first Cancel Delivery Note and Sales Invoice made for that Sales Order. Then amend Sales Order, re-save and re-submit it.

<!-- page: erpnext/erpnext__editing-a-field-after-submission.md -->
---
title: "Edit a Field after Submission "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/editing-a-field-after-submission"
updated: "2026-03-04"
---

In ERPNext, once a document is submitted, you can only edit it through Cancel > Amend. However, you can still make certain fields (custom fields) editable after submission using the **Allow on Submit** feature. For example, we have created a custom field called "Supplier ID" in Supplier Quotation. To allow editing of this field after submission, follow the following steps:  
1) Go to Settings > Customize Form and select the Form Type (Supplier Quotation in this case).  
2) Expand the field row and check the "Allow on Submit" checkbox.  
![](/files/hyYfSoc.png)  
![](/files/dp37Dab.png)  
  
3) Click on Update.  
This setting will allow you to edit this field even after submitting the document without amending it.  
**Note:** The Allow on Submit feature works only for non-standard fields (custom fields).

<!-- page: erpnext/erpnext__education-module-in-erpnext.md -->
---
title: "Education Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/education-module-in-erpnext"
updated: "2026-07-04"
---

## Overview

Frappe Education is an open-source education management app for the Frappe and ERPNext ecosystem. It helps schools, colleges, coaching institutes, and other academic institutions manage academic administration, student information, courses, admissions, fees, scheduling, and student self-service in one system.

The app is built on Frappe Framework and works alongside ERPNext, so institutions can manage academic operations while still using ERPNext for accounting and other business processes.

## GitHub Repository

Source code: [github.com/frappe/education](https://github.com/frappe/education)

The repository describes Frappe Education as an open-source Education Management System for streamlining administrative and academic processes in educational institutions.

## When To Use Frappe Education

Use Frappe Education when an institution needs an ERPNext-backed system for academic operations, not just a learning management system. It is useful when student records, instructors, courses, admissions, fee collection, and academic schedules need to be managed in a structured way.

## Key Features

- **Student and teacher management:** Maintain profiles and academic records for students, guardians, and instructors.
- **Admissions:** Manage student applications and admission workflows from enquiry to enrollment.
- **Programs and courses:** Define academic programs, courses, batches, terms, and course schedules.
- **Attendance:** Track student attendance and use it for academic administration and reporting.
- **Fee management:** Create fee structures, schedule fee collection, and track payment status.
- **Student portal:** Let students access information such as timetables, attendance, fees, and grades.

## How It Fits With ERPNext

Frappe Education extends ERPNext for education-specific workflows. ERPNext provides the broader ERP foundation, while Frappe Education adds the academic objects and flows needed by educational institutions. This makes it suitable for organizations that want both education management and ERP-style accounting or operations in the same ecosystem.

## Related Links

- [Frappe Education on GitHub](https://github.com/frappe/education)
- [Frappe Education website](https://frappe.io/education)
- [Frappe Education documentation](https://docs.frappe.io/education)

<!-- page: erpnext/erpnext__electronic-signature.md -->
---
title: "Signature Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/electronic-signature"
updated: "2026-03-04"
---

  


Electronic signature can be created in ERPNext using the Signature field type. This field allows you to write a signature in a block, just like the signature on a paper.

To create an electronic signature, follow the following steps:

1. Open the DocType and go to Customise Form.
2. In the Form view or Fields table, create a new field called Signature and select the Field Type as **Signature.**

![Screenshot 2024-06-21 at 5.32.17 PM](/files/Screenshot 2024-06-21 at 5.32.17 PM.png)  


![Screenshot 2024-06-21 at 5.29.51 PM](/files/Screenshot 2024-06-21 at 5.29.51 PM.png)  


3. Click on Update.
4. Refresh the page and put your signature.

![Screenshot 2024-06-21 at 5.27.47 PM](/files/Screenshot 2024-06-21 at 5.27.47 PM.png)  


  

<!-- page: erpnext/erpnext__email-account.md -->
---
title: "Email Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-account"
updated: "2026-03-02"
---

**You can sync your email account with ERPNext to send and receive emails from ERPNext.**

You can manage multiple incoming and outgoing Email Accounts in ERPNext. There has to be at least one default outgoing account and one default incoming account. If you are on the ERPNext cloud, the default outgoing email is set by us.

To access Email Accounts, go to:

> Home > Settings > Email Account

1. Prerequisites
----------------

Before creating an Email Account, you need an [Email Domain](/erpnext/email-domain). However, you can skip creating an Email Domain if you're using one of the services listed below, then create [here](/erpnext/email-inbox#2-create-an-email-domain) for set up

* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* [**Outlook.com**](http://Outlook.com)
* **Yandex.mail**

2. How to create an Email Account
---------------------------------

1. Go to the Email Account list, click on New.
2. Enter the email address with the domain. [Domains](/erpnext/email-domain) need to be created in order to create an email account. You don't need to create a domain if you're syncing an email from certain providers as listed [here](/erpnext/email-inbox#2-create-an-email-domain).
3. Enter the email account password.
4. Save. If the credentials are correct, the email account will be synced.


> For some services like Gmail, you may need to enable 2FA and use [App Passwords](https://myaccount.google.com/u/0/apppasswords).
> 
> 

### 2.1 Additional options when creating an Email Account

1. **Use Different Email Login ID**: To use an alternative email login and password to access this account. For example, if you have [notifications@example.com](mailto:notifications@example.com) and you want users to access this email with an alternate email ID, they should tick this checkbox. The recipients will see [notifications@example.com](mailto:notifications@example.com) as the sender.
2. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox. When the other user logs in, they'll be prompted to enter the password.
3. **Use ASCII encoding for password**: Ticking this will use ASCII encoding for the password.

3. Configuration of the Email Account
-------------------------------------

### 3.1 Default Email Accounts

ERPNext will create templates for a bunch of email accounts by default. Not all of them are enabled. To enable them, you must set valid email account details.

There are two types of email accounts, outgoing and incoming. Outgoing email accounts use an SMTP service to send emails and emails are retrieved from your inbox using an IMAP or POP. Most email providers such as Gmail, Outlook, or Yahoo provide these services.

![Defining Criteria](/files/email-account-list.png)  


### 3.2 Incoming Email Accounts

To set up an incoming Email Account, check on **Enable Incoming** and set your POP3 settings, if you are using a popular email service, these will be preset for you.

![Incoming EMail](/files/email-account-incoming.png)  


The following options are available for incoming emails:

1. **Use IMAP**
2. **Use SSL**
3. **Attachment Limit**
4. **Default Incoming**: If ticked, all replies to your company (eg: [replies@yourcomany.com](mailto:replies@yourcomany.com)) will come to this account.
5. **Email Sync Option**: Whether to sync all or only unseen emails.
6. **Initial Sync Count**: Number of emails to sync the first time.

#### Automatic Document Creation Through Linked Emails

This feature creates documents when an email is sent to a particular pre-configured email.

For example, you can link [support@example.com](mailto:support@example.com) to the Issue DocType. After doing this, whenever an email is sent to [support@example.com](mailto:support@example.com), the system will automatically create an Issue is the system.

Similarly, if you link [jobs@example.com](mailto:jobs@example.com), when emails are sent to [jobs@example.com](mailto:jobs@example.com), a Job Applicant document is automatically created.

Enable Automatic Linking in Documents will link emails to documents, to know more [click here](/erpnext/linking-emails-to-document).

### 3.4 Outgoing Email Accounts

All emails sent from the system, either by the user to contact or via notifications or via transaction emails, will be sent from an Outgoing Email Account.

To set up an outgoing Email Account, check on **Enable Outgoing** and set your SMTP server settings, if you are using a popular email service, these will be preset for you.

![Outgoing EMail](/files/email-account-sending.png)  


The following options are available for outgoing emails:

1. **Use TLS**
2. **Port**
3. **Disable SMTP server authentication**
4. **Add Signature**: The default signature is appended to the end of each email.
5. **Default Outgoing**: Notifications and bulk emails will be sent from this outgoing server.
6. **Always use Account's Email Address as Sender**: The email address of this account will be mentioned as the sender for outgoing emails.
7. **Send unsubscribe message in an email**: Send a link to unsubscribe from emails sent from this account.
8. **Track Email Status**: Track if your email has been opened by the recipient. Note that, if you're sending to multiple recipients, even if one recipient reads the email, it'll be considered "Opened".
9. **Enable Auto Reply**: If enabled, enter an auto-reply message.
10. **Append Outgoing Email to Sent Folder**: If using custom email servers like Zimbra or CPanel, SMTP will not automatically append emails to the Sent folder. Enabling this option will ensure all emails are explicitly appended to the email account's Sent folder.
11. **Use SSL for Outgoing Emails**: Use SSL as a standard for outgoing emails. Defaults to port 465.

4. How ERPNext handles replies
------------------------------

In ERPNext when you send an email to contact like a customer, the sender will be the user who sent the email. In the **Reply-To** property, the Email Address will be of the default incoming account (like `[replies@yourcompany.com](mailto:replies@yourcompany.com)`). ERPNext will automatically extract these emails from the incoming account and tag them to the relevant communication.

> **Note for self implementers:** For outgoing emails, you should set up your own SMTP server or sign up with an SMTP relay service like mandrill.com or sendgrid.com that allows a larger number of transactional emails to be sent. Regular email services like Gmail will restrict you to a limited number of emails per day.

If you encounter errors when configuring an email account, refer to [this page](/erpnext/email-error).

5. Video
--------

### 6. Related Topics

1. [Email Inbox](/erpnext/email-inbox)
2. [Email Digest](/erpnext/email-digest)
3. [Auto Email Reports](/erpnext/auto-email-reports)
4. [Sending Email](/erpnext/sending-email)
5. [Email Domain](/erpnext/email-domain)

<!-- page: erpnext/erpnext__email-campaign.md -->
---
title: "Email Campaign | ERPNext Documentation"
description: "Learn how to create an Email Campaign in ERPNext using email templates, schedules, and recipient records."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-campaign"
updated: "2026-07-23"
---

**An Email Campaign is a coordinated set of emails sent to leads or contacts according to a particular schedule.**

Email Campaigns are still one of the most effective ways to reach your Customers, Contacts or Leads and keep them engaged. For example, you could set up Email Campaigns for introducing your product to the customers, with every email revealing an interesting feature of your product.

To create an Email Campaign, go to:

> Home > CRM > Campaign > Email Campaign

## Prerequisites

Before creating and using Email Campaign, these need to be created first:

- [Campaign](/erpnext/campaign)
- [Lead](/erpnext/lead) or [Contact](/erpnext/contact) or [Email Group](/erpnext/email_group)

## How to Create an Email Campaign

- Go to the Email Campaign list, select New.
- Select the [Campaign](/erpnext/campaign) for which you want to set up an Email Campaign.
- Set the 'Start Date' for the Email Campaign.
- In 'Email Campaign For', select whether you want to set up Email Campaign for a Lead or a Contact or for an Email Group to send to multiple email contacts.
- In 'Recipient', select the respective Lead or Contact or Email Group for whom you want to start the Email Campaign.
- In 'Sender', select the user of the system who should be the sender of the emails.
- Save[Email Campaign](/files/email-campaign.png)

he above Email Campaign is for the following Campaign:

[Campaign Schedule](/files/campaign-email-schedule.png)

*Note**: The **Send After (days)** field in Campaign specifies the day on which email is to be sent relative to the **Start Date** of **Email Campaign**. Notice the 'End Date' in the above Email Campaign. It is '26-07-2019', which is 4 days after the 'Start Date', '22-07-2029', as the Campaign Schedule ends on day 4.

### Create multiple Email Campaigns for a Campaign

You can also create new Email Campaigns for different Leads or Contacts for the same Campaign though the Campaign Dashboard.

- Go to the Campaign for which you want to create Email Campaigns.
- select + in front of Email Campaigns to create a new Email Campaign for the Campaign.[Email Campaigns from Dashboard](/files/campaign-dashboard.png)

## Features

### Linked Communication

When emails are sent to the respective leads or contacts, Communication is linked to the Email Campaign document. You can view all the emails sent in your document.

![Linked Communication](/files/email-campaign-linked-comm.png)

### Unsubscribe from Email Campaign

If a lead or contact does not want to continue getting emails regarding the campaign, he or she can unsubscribe from the Email Campaign via the unsubscribe link sent with the email.

![Unsubscribe Link](/files/unsubscribe-link.png)

When the lead or contact unsubscribes, the status of the Email Campaign document changes to 'Unsubscribed'.

![Unsubscribed](/files/email-campaign-unsubscribed.png)

### Use Lead or Contact fields in Email Template

 The Email Template has the context of the document you have specified in the 'Email Campaign For' field. If you want to display the fields from your Lead or Contact document in your Email Template you will have to use doc.fieldname for the same.  
 For example, if 'Email Campaign For' is 'Contact', you can mention the 'first name' of your Contact as doc.first_name in the Email Template as shown below:

![Email Template Document](/files/email-template-doc.png)

Then the emails sent would look like this:

![Email Campaign Doc Data](/files/email-campaign-doc-data.png)

### Status indication

Status indicates the state of the Email Campaign, the various Statuses are:

- **Scheduled**: When the Email Campaign has not yet started but scheduled on a future 'Start Date'.
- **In Progress**: The campaign would be marked as 'In Progress' between 'Start Date' and 'End Date' of the campaign.
- **Completed**: After the 'End Date' of the campaign, the status will be changed to 'Completed'.
- **Unsubscribed**: When the Lead or Contact unsubscribes from the Campaign.

![Email Campaign Status](/files/email-campaign-status.png)

## Related Topics

- [Campaign](/erpnext/campaign)
- [Lead](/erpnext/lead)
- [Contact](/erpnext/contact)

Next: [Newsletter](/erpnext/newsletter)

<!-- page: erpnext/erpnext__email-digest.md -->
---
title: "Email Digest\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-digest"
updated: "2026-03-02"
---


**Email Digests allow you to get regular updates about your sales, expenses and other critical numbers directly in your Email Inbox.**

Email Digests are a great way for top managers to keep track of the big numbers like “Sales Booked” or “Amount Collected” or “Invoices Raised” etc.

To set up Email Digest, go to:

> Home > Settings > Email Digest

1. Enter a name for the Email digest.
1. Set the frequency of mails to be sent.
1. Add or remove recipients.
1. Select the items to be included in the digest.
1. Save.

Example:

![Email Digest](/files/email-digest.png)

### Related Topics
1. [Auto Email Reports](/erpnext/auto-email-reports)
1. [Sending Email](/erpnext/sending-email)

<!-- page: erpnext/erpnext__email-domain.md -->
---
title: "Email Domain"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-domain"
updated: "2026-03-02"
---


**The ``Email Domain`` is the display name of an email network/service account you're setting up for your email services in ERPNex and other Frappe apps.**

You can skip to [Email Account](/erpnext/email-account) creation if you are using one of the services listed [here](/erpnext/email-inbox#2-create-an-email-domain).

You can configure Email Domains in ERPNext for easy setup of all Email Accounts. To find Email Domain settings go to:

> Home > Settings > Email Domain

**What is my Email Domain?:** You might have purchased an Email service from your internet service provider or your IT services provider. For example, if you access your business mailbox with URL like http://mail.yourcompany.com, then yourcompany.com is expected to be used as your email domain. ERPnext tries to guess the ``Email Domain`` from your initially entered example ``Email Address`` if you started from there.

If you want to send and receive emails on your ERPNext account, you need to correctly setup an ``Email Domain``. You may be using free mail services like GMail or Yahoo. In this case, you don't need to create a domain, instead select a service provider from the list. However, you might have to allow access to ERPNext for your GMail account.

ERPNext creates a template ``Email Domain`` using example.com for your reference. You should add your new domain if you want to use it in your ERPNext account.

> **IMPORTANT:** If your actual mail account id differs from the work email address you use in the ``Email Account``setup later, you need to use the option ``Use different Email ID`` when creating the different work mail accounts to communicate with your service and use the related password!

![Email Domain](/files/email-domain.png)

## 1. How to create an Email Domain
1. Go to the Email Domain list, click on New.
1. Enter the Example Email Address. This is where you enter your business email address. For example, if your email ID is yourname@yourcompanyname.com you should enter this.
1. Email Server. This is the URL of your mail server or the email service that you have purchased. For example, it may be mail.yourcompany.com or imap.yourcompany.com.
1. Use IMAP. IMAP and POP are two services used by most mail servers for incoming emails. If your Email server allows IMAP service for the incoming emails keep this checked. Otherwise, leave this unchecked.

1. Use SSL. If your mail server uses SSL (Secure Socket Layer) communication keep this checked.

 **Do I have SSL?:** You may have purchased SSL certificate from your IT service provider for SSL and they may have set up SSL for your mail server. If you're using 'https' while accessing mail server over browser then you might have SSL setup.

1. Use SSL for Outgoing. If your mailserver uses SSL for outgoing, enable this to explicitly use SSL for outgoing emails. Defaults to port 465.

1. Append Outgoing Email to Sent Folder. If you are not using standard mailservers provided by GMail and similar services, you might need to enable this option to append all outgoing emails to the email account's inbox. (Recommended for email servers like Zimbra and CPanel).

1. Attachment Limit (MB). You can limit the size of file attachments in emails sent from ERPNext.

1. SMTP Server is the outgoing email service address of your email server.

1. Tick Use TLS if your SMTP service supports TLS for security.

1. Default port. SMTP service is usually set on port 25. If your email server is set up on a separate port number you can set that up here.

### 1.1 After saving the domain

Once you click on save, these settings are validated by ERPNext and the Email Domain gets saved. Sometimes this could take a few seconds and you might have to wait. This email domain is then available in a dropdown called Domain in the Email Accounts screen.

![Email domain in email account](/files/email-domain1.png)

#### Entered everything but still unable to setup Email Domain?

If you've entered and verified the above settings and are still unable to setup Email Domain, you can contact ERPNext support within your account for help.

### 2. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email-dropbox.md -->
---
title: "Email Dropbox\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-dropbox"
updated: "2026-03-02"
---


When you receive emails from Leads, Customers, Suppliers, or other business partners, you might wish to attach those to their relevant records in ERPNext. One way to do so is to save the email and upload it as an attachment. However, this could turn into a cumbersome process. ERPNext offers a better way to handle this through its "Email Dropbox" feature.

When enabled, each record in ERPNext will have it's own unique email address to which you can forward emails. You can click on the email address to copy it to your clipboard, which can then be added to the "To", "Cc", or "Bcc" field of the email that you wish to send.

## 1. Enable Email Dropbox Feature

In [Email Account](/erpnext/email-account), check 'Enable Email Dropbox'.

![Enable Email Dropbox](/files/enable_email_dropbox.png)

## 2. Copy Unique Email Address in Any Record

Once the Email Dropbox feature is enabled, the unique email address becomes visible in all the records. You can click on the same and the address is copied to your clipboard. You can directly paste it in 'To', 'Cc' or 'Bcc' and send the email.

![Unique Email Address](/files/unique_email_address_dropbox.png)

## 3. Email in Timeline

Once the email is received, ERPNext attaches it to the appropriate record and it will be visible in that record's timeline.

![Email in Timeline](/files/email_in_timeline.png)

### Related Topics
1. [Email Domain](/erpnext/email-domain)
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email-error.md -->
---
title: "Email Error in Sending or Receiving\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-error"
updated: "2026-03-04"
---


In ERPNext, you can customize the Incoming and Outgoing Email Gateway. On saving an Email Account, ERPNext tries establishing a connection with your email gateway. If your ERPNext account is able to connect fine, then Email Account is saved successfully. If not, then you might receive an error as below.

![Email Error](/files/email-error.png)

This indicates that using login credentials and other email gateway details provided in the Email Account, ERPNext is not able to connect to your email server. Please ensure that you have entered valid email credentials for your Email Gateway. Once you have configured Email Account successfully, you should be able to send and receive emails from your ERPNext account fine.

Note: Your ERPNext account is connected with an ERPNext email server by default. If you don't want to use your own email server, you can continue sending emails using ERPNext email server, without any configuration required in the Email Account.

<!-- page: erpnext/erpnext__email-inbox.md -->
---
title: "Email Inbox\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-inbox"
updated: "2026-03-02"
---


**Once an email account is added, the email inbox will be accessible.**

Running a business involves many transactional email exchanges with parties like Customers and Suppliers and other members within the company. Email Inbox feature allows you to pull all your business emails into your ERPNext account. Enabling access to business emails with other transactional details makes ERPNext a single platform for accessing all business information in one place.

In ERPNext, you can configure Email Inbox for each System User. Following are the detailed steps to configure Email Inbox for a User.

## 1. Create a User

You can configure an Email Inbox for a System User only. Hence ensure that you have added yourself and your colleagues as a User and assigned them required permissions.

To know how to add a new User, go to the [User page](/erpnext/adding-users).

## 2. Create an Email Domain

Email Domain for the following Services is available out-of-the-box and you can directly proceed to create an [Email Account](/erpnext/email-account). Know more about creating an Email Domain [here](/erpnext/email-domain).

* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* **Outlook.com**
* **Yandex.mail**

![Email Service](/files/email-service.png)

To be able to send and receive emails into your ERPNext account from other email services (like WebMail or Gmail), you should set up an Email Domain master. In this master, email gateway details like SMTP Address, Port No., IMAP/POP3 address details are captured. If you have ever configured a local email client (like Outlook), Email Domain master requires details to be fed similarly.

To add new Email Domain, go to:

> Home > Settings > Emails > Email Domain > New

![Email Domain](/files/email-domain.png)

Know more about Email Domains [here](/erpnext/email-domain). Once you have configured an Email Domain for your Email Service, it will be used for creating Email Accounts for all the Users in your ERPNext account.

## 3. Email Account

Create an Email Account based on the Email ID of the User. For each User whose email account is to be integrated with ERPNext, an Email Account master should be created for it.

If you are creating an Email Account for your colleague who's Email Password is unknown to you, then check field "Awaiting Password". As per this setting, a User (for whom Email Account is created) will get a prompt to enter email password when accessing his/her ERPNext Account.

![Email Password](/files/email-password.png)

> If you are creating an Email Account for Email Inbox of a User, then leave Append To field as blank.

Read [Email Account documentation](/erpnext/email-account) for more details on how to setup.

## 4. Linking Email Account in the User master

Once an Email Account is created for a User, select that Email Account in the User. This will ensure that emails pulled from the said Email ID will accessible only to this User in your ERPNext account.

![Email User Link](/files/email-user-link.png)

You can link multiple emails with one user.

## 5. Using Email Inbox

If you have correctly configured Email Inbox as instructed above, then on the login of a User, Email Inbox icon will be visible. This will navigate the user to Email Inbox view within the ERPNext account. All the Emails received on that email will be fetched and listed in the Email Inbox view. User will be able to open emails and perform various actions on them.

### 5.1 Folders

In ERPNext, you can link multiple Email Accounts with the single User. To switch to Inbox of a different email account and access other folders like Sent Emails, Spam, Trash, click on Email Inbox option in the left bar.

![Email Folders](/files/email-folders.png)

### 5.2 Actions

On the emails in your inbox, you can take various actions like Reply, Forward, Mark as Spam or Trash.

![Email Actions](/files/email-actions.png)

### 5.3 Relink

You can relink an email to a document like Issue, Lead, Opportunity, etc. based on the context of the email. Select the document type and the document to link the email to.

![Make from Email](/files/make-from-email.png)

### 6. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Sending Email](/erpnext/sending-email)
1. [Email Domain](/erpnext/email-domain)

<!-- page: erpnext/erpnext__email-template.md -->
---
title: "Email Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-template"
updated: "2026-03-02"
---


Every email sent is different but certain emails can be standardized, usually known as Email Template or Standard Reply.

To access the Email Template list, go to:
> Home > Settings > Email > Email Template

## 1. How to create an Email Template
1. Go to the Email Template list, click on New.
1. Enter a name for this Email Template.
1. Enter a Subject for this Email Template.
1. Response is the standard content of the email that will be a part of this template.
1. Save.

![Email Template](/files/email-template-example.png)

**DocType Associated:** (optional) The DocType associated with this template.

### 1.1 How to use Email Template
You can use this Email Template in the Emails that are sent from ERPNext in the "CC, BCC & Email Template" field of the email section of the document. ERPNext will fetch the subject and response as per the template selected.

You can set a Default Email Template for each document type via [Customize Form](/erpnext/customize-form).

### 1.2 How to get fieldnames
The fieldnames you can use in your email template are the fields in the document from which you are sending the email. You can find out the fields of any documents via [Customize Form](/erpnext/customize-form) and selecting the document type (e.g. Sales Order)

### 1.3 Using HTML to build the template

There's a `Use HTML` check that you can toggle to switch from the text editor to a code editor. This allows finer control over the body of the email and makes it easier to use for features like loops in Jinja.

### 1.4 Templating
Templates are compiled using the Jinja. To learn more about Jinja, [visit this page](https://jinja.palletsprojects.com/en/2.10.x/).

## 2. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email.md -->
---
title: "Email Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email"
updated: "2026-03-02"
---

There is a process for configuring email in ERPNext that can greatly enhance communication and productivity within the system. By configuring your email settings, you can seamlessly send and receive emails directly from ERPNext which allows efficient correspondence with clients, suppliers, and team members in order to maintain transparency.

Additionally, the users can personalise email templates, set up auto-replies, and schedule email notifications, enhancing productivity and streamlining communication workflows within the ERP system.

- [Email Domain](/erpnext/user/manual/en/email-domain)
- [Email Account](/erpnext/user/manual/en/email-account)
- [Email Template](/erpnext/user/manual/en/email-template)
- [Email Digest](/erpnext/user/manual/en/email-digest)
- [Newsletter](/erpnext/user/manual/en/newsletter)
- [Notification](/erpnext/user/manual/en/notifications)
- [Auto Email Report](/erpnext/user/manual/en/auto-email-reports)
- [Sending email from documents](/erpnext/user/manual/en/sending-email)
- [Linking email to documents](/erpnext/user/manual/en/linking-emails-to-document)

<!-- page: erpnext/erpnext__email_group.md -->
---
title: "Email Group | ERPNext Documentation"
description: "Learn how to create and manage Email Groups and subscribers for ERPNext newsletters and campaigns."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email_group"
updated: "2026-07-23"
---

**An Email Group is a list of subscriber email IDs to which you send newsletters.**

You can manage subscribers by grouping them into different groups.

You can group existing and potential customers into different groups based on their territory or products they are interested in. You can group the email ID of all employees so that you can share information with them.

To access the Email Group list, go to:

> Home > Settings > Email > Email Group

## How to Create an Email Group

- Go to the Email Group list and select New.
- Enter 'Title'.
- select 'Save'
- select Action > Add Subscribers.
- Enter Email Addresses.
- select 'Add'

## Features

### Import Email IDs from Transactions

You can import email IDs from existing transactions.

select Action > Import Subscribers and select a transaction like Lead. select Import and all the email IDs mentioned in the email IDs will be imported.

### Email Templates

You can specify the confirmation email and welcome email template for the email group. A confirmation email will be sent to confirm a person's subscription to your newsletter. The welcome email is sent when the person confirms their subscription to your email newsletter.

**Confirmation Email Template:** This email template is used to replace the default template sent for newsletter subscription. The confirmation email generated via this template is sent when someone subscribes to the Email Group Website.  
**Welcome Email Template:** Whenever a subscriber is added to an email group after confirmation, the email template set here will be sent to them.

![Email Group Templates](/files/email-group.png)
