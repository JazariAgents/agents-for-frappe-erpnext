<!-- Frappe documentation: erpnext, part 32 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__inventory_dimension.md -->
---
title: "Inventory Dimension"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inventory_dimension"
updated: "2026-02-26"
---


> Introduced in Version 14
> 
> 

Inventory dimensions in ERPNext are used to track an inventory with multiple parameters. By default, ERPNext allows to track an inventory using warehouses, batches, and serial numbers. If users want to track inventory with custom parameters then they can configure it using the Inventory Dimension feature. The user gets an option to select the Inventory Dimension on respective inventory documents as well in the stock ledger and stock balance report. With this feature, you can view dimension-wise stock ledger and stock balance reports.

To access the Inventory Dimension list, go to:


> Stock > Settings > Inventory Dimension
> 
> 

Create Inventory Dimension
--------------------------

![new inventory dimension](/files/new-inventory-dimension.png)  


* Create a new record and select the Reference Document which you want to use as a custom Inventory Dimension.
* You can select any non-child document in the reference document.
* Next, the user has to put the dimension name against which the system will create a custom link field in the Applicable Documents.

Applicable For Documents
------------------------

### Apply to All Inventory Documents

![inventory dimension applicable for all inventory documents](/files/inventory-dimension-applicable-for-all-inventory-documents.png)  


* It will be used to select the custom Dimension in the inventory-related documents.
* For example, the user has created Inventory Dimension with the name "Shelf" and enabled "Apply to All Inventory Document Types". Then the system will create the custom link field with the name "Shelf" in the inventory documents where Batch No and Serial No fields exist.

### Apply to Specific Document

![inventory dimension applicable for](/files/inventory-dimension-applicable-for.png)  


* If the user wants to add Inventory Dimension to a specific document then they have to disable the checkbox "Apply to All Inventory Document Types" and select the respective document in the "Applicable to Document" field.
* Also if you want to add Inventory Dimension for a specific condition like for stock entry type Issue you want separate dimension as "From Shelf" and stock entry type Material Receipt you want separate dimension as "To Shelf" then that can be possible using "Applicable Condition"
* Applicable Condition only can be visible if "Apply to All Inventory Document Types" is disabled
* You can also use the "Type of Transaction" with options such as Inward or Outward for a condition.
 
### Fetch value from

Users can set the 'Fetch Value From' field to fetch data from a field that exists at the parent form level. For example, on the Purchase Receipt form, a user has added a custom field called 'Shelf' and created the inventory dimension to 'Shelf'. If a Purchase Receipt contains 200 line items, the user would typically need to set the 'Shelf' value manually for each row—even if the value is the same across all items. However, by setting the 'Fetch Value From' option in the inventory dimension as 'Shelf' and specifying the value at the parent (Purchase Receipt) level, the system will automatically apply the same 'Shelf' value to all Stock Ledger Entries, even if the user hasn’t entered it in each individual line item.


![](/files/463173872-b10fbcaf-4851-43f0-bcfe-ff1dd2d2ec73.png)

Use of Inventory Dimension
--------------------------

![inventory dimension on transaction](/files/inventory-dimension-on-transaction.png)  


* Once the Inventory Dimension is created system will create the custom field in respective documents
* User gets an option to select the Inventory Dimension in the respective transaction.
* For example, if the user has added Inventory Dimension as "Shelf" in the Stock Entry Detail document. Then in the stock entry, the child table user gets an option to select shelf (see above image). Post submission of the stock entry system will create the stock ledgers with selected inventory dimensions.

Validate Negative Stock
-----------------------

![](/files/fqvxY3m.png)  


If user has enabled the "Validate Negative Stock" checkbox in the inventory dimension, system will not allow to make stock transactions if the respective dimensions has negative stock in the respective warehouse. If user has tried to create the stock transaction with negative stock for the inventory dimension then system will throw the below error

  


![](/files/OKgkIqS.png)  


Stock Balance and Stock Ledger Report
-------------------------------------

* Users can able to filter the Stock Balance and Stock Ledger report using Inventory Dimension
* With this feature, users can able to see Inventory Dimension wise available quantity

### Stock Balance Report

![inventory dimension stock balance](/files/inventory-dimension-stock-balance.png)  


### Stock Ledger Report

![inventory dimension stock ledger](/files/inventory-dimension-stock-ledger.png)  


  


Note:

User can only use the stock reconciliation with inventory dimensions to enter opening values and they can't use the stock reconciliation to modify the available stock or the valuation. Since we are not maintaining inventory dimensions wise valuation rate there is not sense to allow to modify valuation rate through stock reconciliation. in case if they tried to update the quantity or valuation rate through stock reconciliation, system will throw the below error

  


![](/files/cTOHcyI.png)  

<!-- page: erpnext/erpnext__invoice-rounding-issue.md -->
---
title: "Invoice rounding issue"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/invoice-rounding-issue"
updated: "2026-08-14"
---

Nova Industries disables rounded totals, but an invoice print still rounds the amount in words. Two settings can influence the result: the global rounded-total preference and the smallest currency fraction. The currency master must describe the real precision of the transaction currency.

## Check both settings

1. Open Global Defaults and confirm **Disable Rounded Total** matches the company’s policy.
2. Open the Currency used on the invoice.
3. Set **Smallest Currency Fraction Value** correctly, such as 0.01 for a currency whose smallest unit is one cent.
4. Save, reload the invoice, and regenerate the print.

![Currency master with current precision and fraction settings](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-currency-eur-settings.png)



## Troubleshooting

### The printed words still differ

Check the Print Format, currency, precision, Rounded Total field, and cached print preview. Compare the numeric Grand Total, Rounded Total, and amount in words before changing any ledger posting.

## Frequently asked questions

### Does changing currency precision rewrite old invoices?

It changes how later calculations and displays use that currency. Review the effect carefully and do not expect submitted historical ledger entries to be recalculated automatically.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__invoice_discounting.md -->
---
title: "Invoice Discounting | ERPNext Documentation"
description: "Record invoice-backed short-term financing, disbursement, settlement, charges, and receivable accounts in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/invoice_discounting"
updated: "2026-08-01"
---

**Invoice Discounting** uses unpaid Sales Invoices as collateral for short-term financing from a Bank or finance company. ERPNext tracks the financed invoices, loan period, Bank charges, status, and the accounts used when financing is sanctioned, disbursed, and settled.

Use this feature only after finance has approved the accounting design. The receivable remains connected to the Customer while the financing creates a separate obligation to the lender.

## Before you begin

You need:

- one or more submitted [Sales Invoices](/erpnext/sales-invoice) with an outstanding balance;
- a Company Bank Account and Bank ledger;
- short-term loan and Bank charges accounts;
- Accounts Receivable credit, discounted, and unpaid accounts configured for the workflow;
- agreed financing amount, period, fees, recourse terms, and settlement process.

Test the complete lifecycle with finance before using it for live financing. The account names in examples are illustrative and must match your Chart of Accounts and policy.

## Create Invoice Discounting

1. Go to **Accounting &gt; Banking &gt; Invoice Discounting**.
2. Select **Add Invoice Discounting**.

![Invoice Discounting list with Add Invoice Discounting highlighted](https://novacompanies.m.frappe.cloud/files/banking-10-invoice-discounting-list.png)

3. Select the Company and enter the Posting Date.
4. Enter the **Loan Start Date** and **Loan Period (Days)**. Verify the calculated Loan End Date against the lender agreement.

![Invoice Discounting dates and loan period](https://novacompanies.m.frappe.cloud/files/banking-11-invoice-discounting-dates.png)

5. Select **Get Invoices** or add eligible Sales Invoices to the Invoices table.
6. Verify the Customer, date, outstanding amount, and receivable account for every row.
7. Select the highlighted pencil icon to open the full discounted-invoice row when you need to inspect row details.

![Discounted Sales Invoice row and pencil icon](https://novacompanies.m.frappe.cloud/files/banking-12-discounted-invoice-row.png)

8. Enter Bank charges and verify the Total Amount.
9. Select the **Short Term Loan Account**.

![Short-term loan account for Invoice Discounting](https://novacompanies.m.frappe.cloud/files/banking-13-invoice-discounting-loan-account.png)

10. Select the Bank Account that receives the disbursement.

![Bank Account for the financing disbursement](https://novacompanies.m.frappe.cloud/files/banking-13b-invoice-discounting-bank-account.png)

11. Select the Bank Charges Account and the three Accounts Receivable control accounts.

![Bank Charges Account for Invoice Discounting](https://novacompanies.m.frappe.cloud/files/banking-13c-invoice-discounting-charges-account.png)

12. Save and submit after the selected invoices and accounts have been reviewed.

## Important fields and what they mean


| Field                                  | What it controls                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| Posting Date                           | Accounting date for the workflow action.                                             |
| Loan Start Date                        | Date financing begins.                                                               |
| Loan Period                            | Financing duration in days.                                                          |
| Loan End Date                          | Expected maturity or settlement date.                                                |
| Status                                 | Draft, Sanctioned, Disbursed, Settled, or Cancelled stage.                           |
| Invoices                               | Sales Invoices pledged or discounted. Each must have an eligible outstanding amount. |
| Total Amount                           | Total outstanding value represented by selected invoices.                            |
| Bank Charges                           | Fees deducted or charged by the financier.                                           |
| Short Term Loan Account                | Liability account for the financing obligation.                                      |
| Bank Account                           | Ledger receiving the disbursed funds.                                                |
| Bank Charges Account                   | Expense account for financing fees.                                                  |
| Accounts Receivable Credit Account     | Control account used when receivables are credited in the financing entries.         |
| Accounts Receivable Discounted Account | Tracks receivables assigned or discounted.                                           |
| Accounts Receivable Unpaid Account     | Tracks financed invoices that remain unpaid under the configured lifecycle.          |


## Status and lifecycle


| Status     | Operational meaning                                                            |
| ---------- | ------------------------------------------------------------------------------ |
| Draft      | Financing proposal is being prepared and has not posted the lifecycle actions. |
| Sanctioned | Lender has approved the facility or selected invoices.                         |
| Disbursed  | Funds have been received and the financing obligation is active.               |
| Settled    | Customer receipt and lender settlement have completed the financing lifecycle. |
| Cancelled  | The arrangement was canceled under ERPNext cancellation rules.                 |


Use the actions available on the document to move through sanctioned, disbursed, and settled stages. Review every generated [Journal Entry](/erpnext/journal-entry) and [Payment Entry](/erpnext/payment-entry) before submission.

## When the Customer pays

Record the Customer receipt using the agreed collection route. Depending on whether the Customer pays your Company or the lender, the accounting and bank movement may differ. Follow the facility agreement and the configured ERPNext workflow.

After collection:

1. allocate the receipt to the correct Sales Invoice;
2. settle the lender liability and fees;
3. update the Invoice Discounting status;
4. confirm that the Customer outstanding, discounted receivable, Bank, and loan balances are correct;
5. reconcile the bank statement.

Use [Payment Reconciliation](/erpnext/payment-reconciliation) only when allocations need adjustment. Do not use reconciliation to hide an incorrect accounting entry.

## Controls and reporting

Maintain evidence for lender approval, disbursement, charges, pledged invoices, Customer receipts, and settlement. Reconcile:

- the Invoice Discounting register to short-term loan balances;
- discounted and unpaid receivable accounts to individual invoices;
- disbursement and settlement to [Bank Transactions](/erpnext/bank-transaction);
- charges to lender statements and agreements;
- maturity dates to open facilities.

Prevent the same Sales Invoice from being financed twice unless the product and agreement explicitly support it and the remaining eligible balance is clear.

## Troubleshooting

### Get Invoices returns no records

Confirm that Sales Invoices are submitted, belong to the selected Company, have an outstanding balance, and are not already fully allocated to another discounting record.

### An account cannot be selected

Check its Company, root type, group status, and currency. Use ledger accounts, not groups, and confirm the account purpose with finance.

### The disbursed amount differs from the invoice total

Review Bank charges, holdbacks, advance rates, and lender deductions. Record each difference in the correct account instead of forcing the Bank amount to equal the gross invoice value.

### The Customer paid after the loan maturity date

Follow the lender agreement for interest, penalties, or recourse. Record additional charges separately and settle the open liability using supported vouchers.

## Frequently asked questions

### Does Invoice Discounting sell the invoice?

Not always. The legal and accounting substance depends on the agreement, recourse, control, and local standards. Confirm treatment with finance and auditors.

### Can several invoices be financed together?

They can when eligible. Add each invoice row and verify the outstanding amount and Customer.

### Does creating the record receive money automatically?

It does not at the draft stage. Use the documented lifecycle action and verify the generated accounting entries when funds are disbursed.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Bank Account](/erpnext/bank-account)
- [Payment Entry](/erpnext/payment-entry)
- [Journal Entry](/erpnext/journal-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)

<!-- page: erpnext/erpnext__issue-type-and-priority.md -->
---
title: "Issue Type\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/issue-type-and-priority"
updated: "2026-02-28"
---

**Issue Type is useful for tagging and classifying Issues.**

Classifying Issues helps in assigning the concerned team members to specific Issues. Examples of Issue Types can be: 'Functional', 'Technical', 'Hardware', etc. So engineers can be assigned to technical or hardware issues and consultants would be assigned to address functional issues.

To access the Issue Type list, go to:

> Home > Support > Issues > Issue Type

To create an Issue Type, click on New and enter a name for the type. A description can be added.

![](/files/zDMkpfe.png)

Issue Priority
==============

**Issue Priority indicates the urgency of solving an Issue**

User can create priorities like "Low", "Medium", "High", "Critical", etc. Issue Priority will be used while creating the [Service Level Agreement](/erpnext/service-level-agreement).

To access the Issue Priority list, go to:

> Home > Support > Issues > Issue Priority

To create an Issue Priority, click on New and enter a name for the type. A description can be added.

![Issue Priority](/files/issue-priority.png)

**Issue Priority list**

![Issue Priority List](/files/issue-priority-list.png)

### Related Topics

1. [Issue](/erpnext/issue)
2. [Service Level Agreement](/erpnext/service-level-agreement)

<!-- page: erpnext/erpnext__issue.md -->
---
title: "Issue\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/issue"
updated: "2026-02-28"
---


**An Issue is an incoming query from a Customer, usually via email or from the *Contact* section of your website.**

> Tip: A dedicated support Email Address is a good way to keep track of incoming
queries. For example, you can send support queries to ERPNext at
support@erpnext.com and it will automatically create an Issue in our system.

To access the Issue list, go to:
> Home > Support > Issues > Issue

![Issue](/files/issue.png)

## 1. Prerequisites
Before creating and using Issues, it is advised that you create the following first:

* [Customer](/erpnext/customer)
* [Email Account](/erpnext/email-account)

## 2. How to Create Issue
Issues are automatically created if you use the **append to feature** in [Email Account](/erpnext/email-account#32-incoming-email-accounts).

You can also create an Issue manually, to do that:

1. Go to the Issue list, click on New.
1. Enter the Subject, Raised By, and a description of the Issue.

### 2.1 Additional Options when Creating an Issue
* **Status**: When a new Issue is created, its status will be "Open", when it is
replied, its status becomes "Replied".
 * Open: The Issue has been created and yet to be replied to.
 * Replied: A reply has been sent to the Issue.
 * Hold: The Issue is on Hold due to some reason.
 * Resolved: When the users are reasonably sure that they have provided the customer with a solution to their problem but have not received an acknowledgment about the resolution from the customer.
 * Closed: The Customer got a satisfactory resolution that he has indicated with an acknowledgment and the Issue was closed.

 If the sender replies to the thread, the status becomes "Open" again. User can "Close" the Issue manually by clicking on the **Close** button on the top right.

> Note: If SLA has been set up, then the fulfillment status of the SLA will be updated on both, the **Closed** as well as the **Resolved** status.

* **Customer**: If the email was sent from a [Customer](/erpnext/customer) stored in your ERPNext account, then a Customer link will appear in this field.
* **Priority**: Priority can be set as per the requirements. By default, there are three priorities--Low, Medium, and High. You can delete these or add more as needed.
* **Issue Type**: An Issue can be classified using Issue Type. Examples of Issue Types can be: 'Functional', 'Technical', 'Hardware', etc.
* **Raised By (Email)**: The email ID from which the Issue was sent will be shown here.

## 3. Features

### 3.1 Details
* **Description**: This is a text field in which details about the Issue can be seen. This can also contain an image or a table.

### 3.2 Service Level Agreement
It is a contract between a service provider and the end user that defines the level of service expected from the service provider.

User can select the [Service Level Agreement](/erpnext/service-level-agreement) (SLA) from the list.

* Every Issue will have a Time to Response and Time to Resolve within which the Support team has to Respond and Resolve the Issue.
* The Priority can be changed to escalate the Issue. The priorities need to be specified in the Service Level Agreement.
* If needed, the Service Level Agreement can be reset by clicking on the **Reset Service Level Agreement** button in Issues shown as follows:

![SLA](/files/new-issue.gif)

### 3.3 Response
* **Mins to First Response**: Time in minutes from when the Issue was created to when the first reply was sent.

* **First Responded on**: When a Support team member first replies to the issue, first response date and time will be updated.

* **Average Response Time**: The average time taken to respond to the Customer. This is calculated by taking the average of all time spans between Received and Sent Communications. This field will be updated on every reply sent to the customer.

![Response Details](/files/response.png)

### 3.4 Reference
User can filter the issues based on these fields linked to the Issue:

* Lead
* Contact
* Email Account
* Project
* Company

### 3.5 Resolution
* **Opening Date**: When the issue is created or logged the date be posted.
* **Opening Time**: When the issue is created or logged the exact time will automatically be posted.
* **Resolution Date**: When the user resolved the issue, Date and Time will get updated in this field.
* **Resolution Details**: User can enter the details of the issue, once it is resolved. This is a text field. Also, user can upload the image, enter or create a table.
* **Resolution Time**: Total time taken to close the ticket (from Issue creation to closing).
* **User Resolution Time**: Many times a user has to wait for a customer's reply in order to solve some Issue. While measuring User's productivity this wait time shouldn't be taken into consideration. Hence, user resolution time is the total time taken by a user to close the ticket and can be calculated as:

 _Resolution time - Total Time for which the user had to wait for a customer's reply_

The Resolution Time and User Resolution Time metrics are set on "Close". These metrics reset automatically when the Issue reopens or splits.

![Resolution](/files/resolution.png)

#### Via Customer Portal
If the Customer raising the Issue is a Website User (no access to modules), this checkbox will be ticked to indicate that.

## 4. After Saving

### 4.1 Add Comments
Once the Issue is registered, support team Users can add comments for the issue. This field is editable. Comments in Issues are for internal discussions and will not be visible to the Customers.

### 4.2 New Email
Users can compose an email to the person that has raised the Issue. All the mails (received as well as sent) can be seen in a thread in the Issue.

### 4.3 Discussion Thread

The email discussion thread in an Issue maintains all the emails which are sent back and forth against this Issue in the system so that you can track what transpired between the sender and the person responding.

* When a New Email is sent from your mailbox, an automatic reply is sent to the sender with your message and the Support Ticket Number.
* The sender can send additional information to this email.
* All subsequent emails containing this Issue number in the subject will be added to this Issue thread.
* The sender can also add attachments to the email.

### 4.4 Assigning Issues to Users

> Issues can be assigned automatically among Users using [Assignment Rule](/erpnext/assignment-rule).

You can assign an Issue to a specific User by clicking on "Assign" feature in the left sidebar. This will add a new To Do to the user and also send a message indicating that this Issue is allocated.

![Assign Issue](/files/issue-assign.png)


### 4.5 Closing

* You can close the Issue manually by clicking on 'Close' in the toolbar.
* If the sender does not reply in 7 days, then the Issue gets closed automatically.

### 5. Related Topics
1. [Issue Type and Priority](/erpnext/issue-type-and-priority)

<!-- page: erpnext/erpnext__italy.md -->
---
title: "Requirements for Italy"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/italy"
updated: "2026-02-27"
---


ERPNext aims to support local regulation for different regions in the world. In most cases ERPNext is very flexible so you can easily add Custom Fields and make Custom Reports to support the regulation of your region.

This section contains region specific features for Italy. 

- [Importing e-invoice from Supplier](/erpnext/import-e-invoice)

<!-- page: erpnext/erpnext__item-alternative.md -->
---
title: "Item Alternative\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-alternative"
updated: "2026-02-27"
---


**An Item Alternative is an Item similar to the original one and can be used instead of the original Item in manufacturing.**

If the raw material defined in the BOM is not available during the production process then their respective available alternative Item can be used to complete the production process.

First you need to enable the "Allow Alternative Item" in the Item.
![Item](/files/allow-alternative-item.png)

To access the Item alternative list, go to:
> Home > Stock > Items and Pricing > Item Alternative

This can also be done by clicking the plus sign next to 'Item Alternative' from the Item master dashboard.
You can enable Two-Way replacement between an Item and their alternative item if both can be used as an alternative to each other.

![Item Alternative](/files/item-alternative.png)

## 1. Prerequisites
Before creating and using an Item Alternative, it is advised that you create the following first:

* [Item](/erpnext/item)

## 2. Item Alternative for Work Order

To allow to using alternative Items in the manufacturing process, the user can configure to 'Allow Alternative Item' in the BOM/Work Order

### 2.1 Provision to allow alternative item in the BOM
You can enable 'Allow Alternative Item' in a BOM then select the alternative item in the Stock Entry. This can also be done with a Work Order.
![Item](/files/allow-alternative-item-bom.png)


### 2.2 Provision to allow alternative item in the Work Order
User can also enable/disable allow alternative item for individual Work Orders.
![Item](/files/allow-alternative-item-wo.png)


Ticking on the 'Allow Alternative Item' checkbox will show a button named 'Alternate Item'. You can click on this to set the Item Alternative in the Work Order. This is how you use Item Alternative in a Work Order:
![Item](/files/work_order_item_alternative.gif)

This is how you use Item Alternative with a Stock Entry:
![Item](/files/se_item_alternative.gif)

If the 'Allow Alternative Item' checkbox in the Item table is disabled, you cannot set an Alternate Item for this Item.

### 2.3 Item Alternative for subcontract
In subcontract, the user has to transfer raw materials to the subcontracted supplier to get finished good from them. If the raw material is not available in the stock, with this feature, the user can transfer the alternate item of the subcontracted raw material to the supplier. This is done in the Stock Entry.

![Item](/files/purchase_order_item_alternative.gif)

After this, when you create a Purchase Receipt from the Work Order, the alternate item will be shown.

### 3. Related Topics
1. [Bill Of Materials](/erpnext/bill-of-materials)
1. [Work Order](/erpnext/work-order)

<!-- page: erpnext/erpnext__item-attribute.md -->
---
title: "Item Attribute"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-attribute"
updated: "2026-03-06"
---

### **'Item Attributes' are the characteristics based on which Item Variants are created.**

The attributes can be defined based on item's physical appearance and capabilities. Defining item attributes properly will be helpful in creating item variants as a combination of multiple attributes.

![](/files/attributes.png)

To access the Item Attribute list, go to:

> Home > Stock > Settings > Item Attribute

## How to create an Item Attribute?

1. Go to the Item Attribute list, click on 'Add Item Attribute'.
2. Enter a name for the Attribute.
3. Enter the attribute values in the table.
4. Save.

The attribute values can be numeric or non-numeric.

##### Non-Numeric Attributes

For Non-numeric attributes, specify attribute values along with their abbreviations in the Attribute Values table.

![](/files/attribute-code.png)

##### Numeric Attribute

If your attribute is 'Numeric', then specify the range and increment so that the system can generate respective variants.

In the following example, the cable length is of range 1 to 5 and the increment is 1. Hence, the variants will be 1,2,3,4,5.

![](/files/num_attribute.png)

<!-- page: erpnext/erpnext__item-codification.md -->
---
title: "Item Codification\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-codification"
updated: "2026-03-02"
---


If you already have a full-fledged business with a number of physical items,
you would have probably coded your items. If you have not, you have a choice.
We recommend that you should codify if you have lot of products with long or
complicated names. In case you have few products with short names, it is
preferable to keep the Item Code same as Item Name.

Item codification has been a sensitive topic and wars have been fought on this
(not joking). In our experience, when you have items that cross a certain
size, life without codification is a nightmare.

### 1. Benefits

 * Standard way of naming things.
 * Less likely to have duplicates.
 * Explicit definition.
 * Helps to quickly find if a similar item exists.
 * Item names get longer and longer as more types get introduced. Codes are shorter.

### 2. Challenges

 * You have to remember the codes!
 * Harder for new team members to pick up.
 * You have to create new codes all the time.

### 3. Example

You should have a simple manual / cheat-sheet to codify your Items instead of
just numbering them sequentially. Each letter should mean something. Here is
an example:

If your business involves wooden furniture, then you may codify as follows:

Item Codification Summary Sheet (SAMPLE)



 First letter: "Material" Third letter: "Size"

 - W - Wood - 0 - less than 1mm
 - H - Hardware - 1 - 1mm - 5mm
 - G - Glass - 2 - 5mm - 10mm
 - U - Upholstery - 3 - 10mm - 10cm
 - P - Plastic

 Second Letter: "Type"

 For Wood: For Hardware:

 - S - Sheet - S - Screw
 - B - Bar - N - Nut
 - L - L-section - W - Washer
 - M - Molded - B - Bracket
 - R - Round


The last few letters could be sequential. So by looking at code **WM304** \-
you know its a wooden molding less than 10cm in size

### 4. Standardization

If you have more than one person naming items, the style of naming items will
change for everyone. Sometimes, even for one person, he or she may forget how
they had named the item and may create a duplicate name _"Wooden Sheet 3mm" or
"3mm Sheet of Wood"?_

### 5. Rationalizing

It is a good practice to have minimum varieties of items so that you keep
minimum stock, housekeeping is simpler etc. When you are planning a new
product and you want to know if you are already purchasing a part in some
other product, the item codes will help you quickly determine if you are using
a similar raw material in another product.

We believe if you do this small investment, it will help you rationalize
things as your business grows, though its okay not to codify if you have less
items.

#### 6. Related Topics
1. [Item Group](/erpnext/item-group)
1. [Item Attribute](/erpnext/item-attribute)
1. [Item Price](/erpnext/item-price)
1. [Item Variants](/erpnext/item-variants)

<!-- page: erpnext/erpnext__item-creation-not-required-in-purchase-invoice.md -->
---
title: "Purchase invoice for Services"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-creation-not-required-in-purchase-invoice"
updated: "2026-03-02"
---

### **1. Set Up Supplier**

1. **Navigate to Suppliers:**


	* Go to **Buying > Supplier**.
2. **Create New Supplier (if not already created):**


	* Click on **New**.
	* Enter the supplier's details (name, contact information, address).
	* Save the supplier record.

### **2. Create a Service Item**

1. **Navigate to Item Master:**


	* Go to **Stock > Item**.
2. **Create New Item:**


	* Click on **New**.
	* Enter the item code and name.
	* Under the **Item Group** field, select or create a group for services.
	* Set the **Item Type** to **Service**.
	* Fill in other relevant details, such as unit of measure and description.
	* Save the item record.

### **3. Create a Purchase Invoice**

1. **Navigate to Purchase Invoice:**


	* Go to **Buying > Purchase Invoice**.
2. **Start a New Invoice:**


	* Click on **New**.
3. **Enter Basic Information:**


	* **Supplier:** Select the supplier from whom the service was received.
	* **Invoice Date:** Enter the date of the invoice.
	* **Reference Number:** Input any reference number provided by the supplier.
4. **Add Service Details:**


	* **Items Section:** Click on **Add Item**.
	* **Select Service Item:** Choose the service item you created earlier.
	* **Description:** Provide a detailed description of the service.
	* **Rate and Quantity:** Enter the rate and quantity for the service.
	* **Taxes and Charges:** If applicable, add any taxes or additional charges.
5. **Account Details:**


	* **Expense Account:** Ensure the service expense is recorded in the appropriate expense account. This can be configured under the **Accounts** section of the invoice.
6. **Review and Save:**


	* Verify all details for accuracy.
	* Click **Save** to save the draft of the invoice.

### **4. Submit**

1. **Submit Invoice:**


	* Once the details are confirmed, click **Submit** to finalize the invoice.

![](/files/PU1Sggx.gif)  

<!-- page: erpnext/erpnext__item-group.md -->
---
title: "Item Group"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-group"
updated: "2026-03-06"
---

**An Item Group is a way to classify items based on types.**

Depending on the type of product, you can categorize an item under its respective field. If the product is service-oriented, assign it under the Item Group - service. If the product is used as a raw-material, assign it under the Raw Material category. In case, an item is used only in trading, you can categorize it under an Item Group called Trading.

To access the Item Group list, go to: 

> Home > Stock > Items and Pricing > Item Group

This is what the Item Group tree looks like: 

![](/files/item_groups.png)

## How to create an Item Group

---

1. Go to the Item Group list, click on New.
2. Select a group node under which you wish to create the Item Group, the default root is 'All Item Groups'.
3. Select 'Add Child' or click on the New button.
4. To make this child a category/group node, tick on Group Node.
5. Click on Create New.

Note:

- Nodes in different parts of the tree cannot have the same name.
- The child notes get alphabetically arranged

![](/files/item-group-new2af55d.gif)

### 1.2 Delete an Item Group

1. Select the Item Group you want to delete.
2. Select 'Delete'.
3. Click on Yes.
4. Features

---

To see the following options, click on an Item Group, click on Edit.

### 2.1 Parent Item Group

You can change the parent Item Group of an item by choosing another one under General Settings.

### 2.2 Defaults

- **Default Price List**: A default price list that'll determine the Item Prices for this Item Group.
- **Default Warehouse**: The default Warehouse is set in transactions for the items that belong to this group.
- **Default Buying/Selling Cost Centre**: The default Buying/Selling Cost Centre to which items in this group will be billed against.
- **Default Expense/Income Account**: The default accounts for items that belong to this group.
- **Default Supplier**: On setting a Supplier here, this supplier will be chosen in purchase transactions by default for items in this group.

### 2.3 Item Tax

A default item tax template will be applied to all items belonging to this group. Similarly a Tax Category can also be selected, visit [Quotation](/erpnext/quotation) to know more about Tax Categories.

### 2.4 Website Settings

- **Show in Website**: Items belonging to this group will be shown on your website under the Item Group.
- **Weightage**: This is the weight for the Item Groups themselves, item groups with higher weights will be shown first.
- **Slideshow**: A slideshow for the Item Group, just like in an Item. Visit the [Homepage](/erpnext/homepage) page in Website module to know more.
- **Description**: This will appear on the Item Group page.
- **Website Specifications**: Label and its description for an item group.

<!-- page: erpnext/erpnext__item-price.md -->
---
title: "Item Price"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-price"
updated: "2026-03-06"
---

**Item Price is the record in which you can log the selling and buying rate of an item.**

---

There are two ways to reach a new Item Price form:

**Selling/Buying/Stock > Items and Pricing > Item Price > New**.

Or

**Stock > Item > Click on "+" next to Item Price**.  
2. Select the Item. The name, UoM and description will be fetched.  
3. Select the Price List, whether Selling/Buying price or any other price list you may have created.  
4. Enter the actual rate in the Rate field.  
5. Save. 

![](/files/item-price.png)

### 1.1 Selecting the Price List

You can create multiple Price Lists for one Item in ERPNext to track the Selling and Buying Price of an Item separately. Also, if the Item's selling prices change based on Territory or due to other criteria, you can create multiple Selling Price Lists for it.

On selection of Price List, its currency and applicability, whether for selling/buying or both, will be fetched as well. To have Item Price fetching in the sales or purchase transaction, you should have 'Price List' selected in the transaction under Currency and Price List.

To check all Item Prices together, go to:

**Stock > Stock Reports > Item Price Stock**

Visit the [Price Lists](/erpnext/price-lists) page to know more.

---

## 2. Features

### 2.1 Unit of Measurement (UOM)

A price is always specific to a certain UOM. For example, $1 *per KG* or $80 *per hour*. By default, the **Item Price** will fetch the item's *Default Unit of Measure*. You can change it to any UOM from the item's UOM table.

For example, if Rice is sold in 1 KG and 500-gram packets, then you can mention the UOM ("KG" or "grams") in the **Item Price**, and the correct price will be applied based on the UOM selected in the transaction.

### 2.2 Packing Unit

This is the quantity that must be bought or sold per unit of measure. For example, if the Packing Unit is two, and the UOM is one, two items in quantity will be transacted. The default is 0; you can use non-integer UoM like 1.5 kg oats for 1 Packing Unit. If you leave it as 0, it'll not affect any transaction.

### 2.3 Minimum quantity

This is the minimum quantity of items to be transacted for this price to be applicable and updated in the Item Price list.

### 2.4 Applying Price List to a specific Customer/Supplier

If you select a Selling Price list, a customer field will appear where you can assign this Item Price to a specific customer. Likewise, if you select a Buying Price List, a Supplier field will appear where you can select a specific Supplier

### 2.5 Applying Price List to a Specific Batch

You can also link a specific batch to an Item Price, and on the selection of that batch in the transaction, the item price for that specific batch will be applied.

### 2.6 Validity

There are two fields here, ' Valid From' and 'Valid Upto'. Valid from is set to the date you created the Item Price; you can also set the Valid Upto date on which the Item Price will expire.

### 2.7 Lead Time in days

The approximate number of days it takes the product to reach the warehouse. You can set different Item Prices based on how long it takes the same product to reach you from different vendors.

### 2.8 Note

You can add any note about the Item Price in this field.
