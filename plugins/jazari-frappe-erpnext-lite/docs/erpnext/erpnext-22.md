<!-- Frappe documentation: erpnext, part 22 of 69. Index: docs/INDEX.md -->

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
