<!-- Frappe documentation: erpnext, part 49 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__quality_procedure.md -->
---
title: "Quality Procedure"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_procedure"
updated: "2026-02-26"
---

**A Quality Procedure is a Standard Operating Procedure (SOP) used as a reference to carry out routine actions**

A standard operating procedure (SOP) is a set of step-by-step instructions compiled by an organization to help the employees execute routine operations. SOPs aim to achieve efficiency, quality output and uniformity of performance while reducing miscommunication and failure to comply with industry regulations.

A Quality Procedure can be of two types:

1. A Procedure consisting of simple steps that you must follow to achieve a [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)
2. A procedure having sub-Procedures which may also have its own steps

To access the Quality Procedure list, go to:

> Home > Quality > Goal and Procedure > Quality Procedure

## How to create a Quality Procedure

1. Go to the Quality Procedure list, click on New.
2. Enter a name for the Quality Procedure.
3. In the Processes table, enter Process Descriptions.
4. **Child Procedure**: If the Quality Procedure being created a is a parent procedure that contains sub-procedures, link the sub-procedure here. On doing this, the current procedure becomes a parent and the 'Is Group' checkbox is enabled.
5. Save.
  Quality Procedure can also be saved without entering the Process descriptions if the title is self explanatory.

![](/files/Screenshot 2026-01-22 at 11.12.11 PM.png)

The 'Parent Procedure' is linked to the child procedure. For example 'Issue Classification' needs to be done before a resolution and hence 'Issue Resolution' is the parent here:

![](/files/Screenshot 2026-01-22 at 11.16.49 PM.png)

## Features

#### 1. Using Quality Procedure in Quality Goal

Once a Quality Procedure is created, it can be used in a [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal):

![](/files/Area3ae47b.gif)

#### 2. Sub Procedures

Process can either be just a instruction or a different Quality Procedure. You can link a Quality Procedure as a sub-procedure to another one:

![](/files/Screenshot 2026-01-22 at 11.24.39 PM.png)

<!-- page: erpnext/erpnext__quality_review.md -->
---
title: "Quality Review\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quality_review"
updated: "2026-02-26"
---

**A Quality Review is a record of the performance against Quality Goal at regular intervals.**

A Quality Review is an inspection with a specific structure, defined roles, and procedure designed to ensure a product's completeness and adherence to quality standards. The Quality Review is used to check if all Objectives of a Quality Goal have been achieved.

To access the Quality Review list, go to:

> Home > Quality > Review and Action > Quality Review

## 1. Prerequisites

Before creating and using a Quality Review it is advised to create the following first:

- [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)

## 2. How to Create a Quality Review

1. Go to the Quality Review list, click on New.
2. Select a Quality Goal which is to be Reviewed.
3. In the Review section of the Reviews table, leave a review about a Quality Objective.
4. Save.

![](/files/review63e6d1.gif)

> Note: If the Quality Procedure is linked to the Quality Goal, the Quality Procedure will be fetched in the Quality Review.

You can also add some notes in the 'Additional Information' section.

## 3. Features

#### Periodic Auto Creation

if you have set the frequency of review in your Quality Goal, then the Quality Review will automatically be created and its status will be set to "Open". The quality manager can then check open reviews and complete the inspection.

## 4. Next Steps

After you have completed a Quality Review, you can create a [Quality Action](https://docs.frappe.io/erpnext/user/manual/en/quality_action) against it if you want to record any corrective or preventive actions

## 5. Related Topics

- [Quality Procedure](https://docs.frappe.io/erpnext/user/manual/en/quality_procedure)
- [Quality Goal](https://docs.frappe.io/erpnext/user/manual/en/quality_goal)
- [Quality Action](https://docs.frappe.io/erpnext/user/manual/en/quality_action)

<!-- page: erpnext/erpnext__quick-stock-balance.md -->
---
title: "Quick Stock Balance\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quick-stock-balance"
updated: "2026-02-27"
---


**Quick Stock Balance is a tool that can be used to quickly retrieve the current stock balance (quantity) and value of an item, in the specified warehouse, on the specified date.**

It comes in handy during audits, while verifying stock details before transactions, etc.

To access this tool, go to:
> Home > Stock > Tools > Quick Stock Balance

## 1. Using Quick Stock Balance
Item and Warehouse are the basic fields required to fully utilize Quick Stock Balance. Item Barcode can also be used to fetch stock details.

![Quick Stock Balance](/files/quick-stock-balance.png)

You can opt to select a different warehouse or date. The stock value and quantity, will be fetched real-time according to the specified values.

You can also view the Stock Balance report by clicking on 'Stock Balance Report' . It will redirect you to the report with the Item and Warehouse filters populated.

![Stock Balance Report](/files/stock-balance-report.png)

### 2. Related Topics
1. [Stock Level Report](/erpnext/stock-level-report)
1. [Stock Entry](/erpnext/stock-entry)

<!-- page: erpnext/erpnext__quickbooks-migrator.md -->
---
title: "QuickBooks Migrator (Deprecated) | ERPNext Documentation"
description: "The built-in ERPNext QuickBooks Migrator has been removed. Review the legacy instructions and use supported ERPNext import tools for current migrations."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quickbooks-migrator"
updated: "2026-07-31"
---

> **Deprecated**
>
> The built-in ERPNext QuickBooks Migrator is no longer available in current ERPNext releases. It was removed from the ERPNext develop branch on January 17, 2025 in [PR #45240](https://github.com/frappe/erpnext/pull/45240). The instructions below apply only to older ERPNext versions that still contain the QuickBooks Migrator and should not be used for a current migration.
>
> For a current QuickBooks migration, export the required data from QuickBooks, clean and map it, then use [Data Import](/erpnext/data-import) for masters, the [Chart of Accounts Importer](/erpnext/chart-of-accounts-importer), the [Opening Invoice Creation Tool](/erpnext/opening-invoice-creation-tool), [Stock Reconciliation](/erpnext/stock-reconciliation), and opening Journal Entries. Follow the [Accounting Migration Overview](/erpnext/accounting-migration-overview) to plan and validate the migration.

## Legacy instructions for older ERPNext versions

## How to Setup QuickBooks Migrator?

### Create a QuickBooks Online App

1. From Awesome-bar, Go to "QuickBooks Migrator" DocType.
2. Go to [Inuit Developer Portal](https://developer.intuit.com)
3. Sign In with your existing account or Sign Up.
4. Go to "My Apps" page.
5. Click on "Select APIs".
6. Under "QuickBooks API" Check "Accounting".
7. Click on "Create App".
  - You'll be taken to the Dashboard of your App.
8. Go to "Keys" tab.
9. Go to "Production Keys" Section.
  - Complete requirements.
10. In "QuickBooks Migrator" DocType a "Redirect URL" will be generated for you and add it in the list of "Redirect URIs" of your Inuit App (under "Production Keys" section). Click Save.
  - Make sure that the Redirect URL starts with `https`.
11. From "Production Keys" section copy "Client ID" and "Client Secret" to "QuickBooks Migrator" DocType.
12. Save "QuickBooks Migrator".

### Connect to QuickBooks Online API

1. Click "Connect to QuickBooks".
2. A new tab will open in your browser and You'll be asked to Log In.
3. If you have more than one companies then Select the company you want to migrate.
4. Click "Connect".
5. Upon successful authorization, the tab will close.
6. The indicator will be set to "Connected to QuickBooks".
7. In "QuickBooks Migrator" select "Company" where you want to migrate your data.
8. Save "QuickBooks Migrator".

### Migrate Data

1. Click the "Fetch Data" button.
2. The indicator will change from "Connected to QuickBooks" to "In Progress".
3. Progress bars will show the status of migration.
4. This will take a few minutes depending on the size of data.
5. After migration is complete, the indicator will change to "Complete" or "Failed".

## What Will Happen when I Click Fetch Data?

## Account

### Existing Chart of Accounts

 Upon creation of a Company ERPNext creates a chart of accounts for that company, these accounts will be kept.

### Account Naming

 To avoid name collision with existing accounts, all accounts from QuickBooks will be assigned "- QB" suffix.

 e.g. `Job Expense` will become `Job Expense - QB`.

 **Note**: ERPNext also encodes account names with Company abbreviation. Taking this into account `Job Expense` will become `Job Expense - QB - AZ` (assuming `AZ` is the company abbreviation).

### Root Accounts

 Five root accounts, namely `Asset`, `Equity`, `Expense`, `Liability`, `Income` will be created and all accounts (depending on the account type) will become children of these accounts.

### Group Accounts

 QuickBooks allows transactions on group accounts, which is not allowed in ERPNext, to handle this, every group account will have a child with a hyphenated name.

 e.g.

 will become

### Name Collisions

 QuickBooks allows multiple accounts to have the same name, which is not allowed in ERPNext, to handle this, every duplicate account will have a hyphenated name.

 e.g.

 will become



## Item

### Naming

 All Items will have company encoded names.

 e.g. `Pen` will become `Pen - AZ` (assuming `AZ` is the company abbreviation).

### UOM

 All Items will be assigned `Unit` as the default UOM.

### Fractional UOM

 `Unit` will be allowed to have fractional value.

### Inventory

 Irrespective of whether Item is an Inventory or Non-Inventory Item in QuickBooks, No Inventory related information will be kept.

## Customer and Supplier

### Naming

 All Customer and Suppliers will have company encoded names.

 e.g. `Pen` will become `Pen - AZ` (assuming `AZ` is the company abbreviation).



## Invoice

### Variants

 QuickBooks has four transactional variants of Invoice, all of these will be saved as Sales Invoice.

- **Invoice** is equivalent to a Sales Invoice.
- **Sales Receipt** is equivalent to a POS Sales Invoice.
- **Credit Memo** is equivalent to a return Sales Invoice (Credit Note).
- **Refund Receipt** is equivalent to a return POS Sales Invoice.

### Discount and Markup

 QuickBooks uses special accounts for both Markup and Discount, ERPNext doesn't handle the discount expense and markup this way, instead, all Item's will see the change in their Income accounts.

### Shipping

 For Invoices with Shipping, an Item with name Shipping will be added in the Item table.

### Round off

 ERPNext uses different rounding method than QuickBooks, because of this, in Invoices with Tax and with a currency different than company currency, Sales Invoice will have different grand total than that of the QuickBooks Invoice.

### Special Case

 If a QuickBooks Invoice is linked to a `Delayed Charge` or `Statement Charge` then an equivalent `Journal Entry` is created for this Invoice.



## Bill

### Variants

 QuickBooks has two transactional variants of Bill, all of these will be saved as Purchase Invoice.

- **Bill** is equivalent to a Purchase Invoice.
- **Supplier Credit** is equivalent to a return Purchase Invoice.



## Other

Following transactions will be saved as Journal Entry

- Advance Payment
- Bill Payment
- Cheque
- Credit Card Credit
- Expense
- Inventory Qty Adjustment
- Journal Entry
- Payment
- Tax Payment



## Tax

For every QuickBooks Tax Rate an ERPNext account will be created.

## Custom Fields

QuickBooks Migrator will add following Custom Fields

- Company field
- Customer
- Item
- Supplier
- QuickBooks ID field
- Customer
- Item
- Journal Entry
- Purchase Invoice
- Sales Invoice
- Supplier

<!-- page: erpnext/erpnext__quotation.md -->
---
title: "Quotation | ERPNext Documentation"
description: "Create, price, submit, share, and convert Quotations in ERPNext, including items, taxes, payment terms, alternatives, and statuses."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/quotation"
updated: "2026-07-24"
---

A Quotation in ERPNext records the products or services, quantities, prices, taxes, validity, delivery expectations, and commercial terms offered to a Lead or Customer. It is a submittable sales transaction that can be shared as a proposal and converted into a [Sales Order](/erpnext/sales-order) after acceptance.

![](/files/order-to-cash-quotation.webp)
*Quotation highlighted within the ERPNext CRM and sales flow.*

## Before you begin

Create or confirm the following records:

- A [Lead](/erpnext/lead) or [Customer](/erpnext/customer).
- The required [Items](/erpnext/item) and selling prices.
- A selling [Price List](/erpnext/price-list) and Currency.
- Applicable [Sales Taxes and Charges Templates](/erpnext/sales-taxes-and-charges-template).
- Approved [Terms and Conditions](/erpnext/terms-and-conditions) and Payment Terms when required.

## Create a Quotation

1. Go to **Selling > Sales > Quotation**.
2. Select **Add Quotation**.
3. In **Quotation To**, select Customer or Lead, then select the party.
4. Enter the Date and **Valid Till** date.
5. Confirm the Order Type and Company.
6. Add each Item, Quantity, Rate, and Warehouse in the Items table.
7. Add taxes, shipping, discounts, payment terms, and terms and conditions as applicable.
8. Review the totals, then save the draft.

![Example Quotation for Northstar Retail with products, services, quantities, rates, and totals.](https://novacompanies.m.frappe.cloud/files/quotation-details.png)

The example quotation combines laptops, accessories, and a setup service. In an Item row, the stock indicator before the Item Code is green when the item is in stock and red when it is out of stock. Select the row's pencil icon to open the full row editor when additional item fields are required.

![The highlighted pencil icon opens the complete Quotation item row.](/files/quotation-item-pencil.webp)

![The Quotation item row with item details, quantity, UOM, rate, and alternative-item settings.](/files/quotation-item-row.webp)

## Alternative ways to create a Quotation

A Quotation can be created from an [Opportunity](/erpnext/opportunity), which carries the party and requested items into the new transaction. You can also use **Get Items From > Opportunity** in a draft Quotation. Review every mapped quantity, rate, date, and term before saving.

For repeated quoting, use reusable masters such as Price Lists, Item Prices, tax templates, payment terms, and terms templates instead of copying an old transaction whose conditions may be outdated.

## Important fields and what they mean


| Field                    | What it means                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Quotation To             | Determines whether the offer is addressed to a Customer or Lead.                                              |
| Party                    | The selected Customer or Lead. Address and contact details can be fetched from this party.                    |
| Valid Till               | The last date on which the offer is valid.                                                                    |
| Order Type               | Identifies Sales, Maintenance, or Shopping Cart usage. Use Shopping Cart only for the relevant website flow.  |
| Currency                 | The currency shown on the Quotation. Conversion rates apply when it differs from the Company currency.        |
| Selling Price List       | Supplies the default item prices for the selected party and currency.                                         |
| Ignore Pricing Rule      | Prevents configured [Pricing Rules](/erpnext/pricing-rule) from changing item prices or discounts.            |
| Item Code                | The product or service being quoted. It fetches the name, description, UOM, and applicable price defaults.    |
| Quantity and UOM         | The amount offered and its unit of measure.                                                                   |
| Rate                     | The offered unit price before multiplying by Quantity.                                                        |
| Warehouse                | The source warehouse used for stock context and downstream mapping where applicable.                          |
| Margin and Discount      | Adjusts the item rate by an amount or percentage.                                                             |
| Shipping Rule            | Applies configured shipping charges based on the selected rule.                                               |
| Incoterm and Named Place | Records the agreed delivery responsibility and location for international or formal trade terms.              |
| Payment Terms Template   | Creates the proposed payment schedule.                                                                        |
| Print Heading            | Displays an approved alternative heading, such as Proposal or Proforma Invoice, without changing the DocType. |


## Items, pricing, and alternatives

ERPNext fetches defaults from the Item and Item Price, but every quoted rate remains the responsibility of the user preparing the offer. Apply an item discount or margin in the row, or use Additional Discount for the transaction total. Confirm whether the additional discount applies to the Net Total or Grand Total.

To offer substitute products, add the alternative immediately after its primary item and enable **Is Alternative** in the row. Alternative items are excluded from the Quotation totals. When a Sales Order is created from an individual Quotation, ERPNext can ask which alternative should be selected.

## Taxes, shipping, and payment terms

Select a tax template or enter rows in the Sales Taxes and Charges table. Use **Tax Breakup** to review the components before sharing the document. A [Shipping Rule](/erpnext/shipping-rule) can calculate freight, while an Incoterm records delivery responsibility.

Use a [Payment Terms Template](/erpnext/payment-terms-template) when payment is divided into deposits or milestones. The resulting schedule is a proposal on the Quotation and should match the commercial agreement.

## Submit and next steps

Before submitting, check the party, validity date, items, quantities, rates, discounts, taxes, payment schedule, terms, delivery expectations, and final print output. Submission freezes the offered transaction as the version sent for approval.

After submission, use **Create > Sales Order** when the Customer accepts the offer. If the deal does not proceed, use **Set as Lost** and record a useful loss reason. Cancel and amend the Quotation when a submitted offer must be formally revised.

## Status


| Status    | Meaning                                                          |
| --------- | ---------------------------------------------------------------- |
| Draft     | The Quotation is editable and has not been confirmed.            |
| Open      | The submitted offer is active and awaits an outcome.             |
| Ordered   | A Sales Order has been created from the Quotation.               |
| Lost      | The offer did not convert. Record the reason for later analysis. |
| Expired   | The Valid Till date has passed.                                  |
| Cancelled | The submitted Quotation was cancelled.                           |


## Print and share

Review the print preview before sending the Quotation. Confirm that the selected [Print Format](/erpnext/print-format), Letter Head, item images, terms, tax details, and Print Heading appear correctly. A Print Heading changes the displayed title only. It does not convert the record into another DocType.

## Frequently asked questions

### Can I quote a Lead without creating a Customer?

Yes. Select Lead in Quotation To. Create the Customer when the party is qualified and your workflow requires customer transactions.

### Can I edit a submitted Quotation?

Cancel and amend it when a formal revision is required. Avoid silently changing an offer that has already been sent.

### Can I create a Sales Invoice directly from a Quotation?

The standard confirmed sales path is normally Quotation to Sales Order, followed by delivery and billing. Use the transaction path approved for your organization and version.

### Why did an item rate change automatically?

Check the Price List, Item Price, Pricing Rules, party, quantity, date, currency, UOM, and whether Ignore Pricing Rule is enabled.

## Related topics

- [Opportunity](/erpnext/opportunity)
- [Sales Order](/erpnext/sales-order)
- [Applying a Discount](/erpnext/applying-discount)
- [Adding Margin](/erpnext/adding-margin)
- [Selling in Different UoM](/erpnext/selling-in-different-uom)

<!-- page: erpnext/erpnext__raw-printing.md -->
---
title: "Raw Printing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/raw-printing"
updated: "2026-03-02"
---


> Introduced in Version 12

**Sending a string of commands to a printer directly in its native language is called Raw Printing.**

Many thermal printers need these raw commands sent to them in order to perform functions like barcode printing, receipt printing, label printing, etc. Raw Printing bypasses the printer's drivers in most cases, making them very fast and reliable. Raw Printing is also capable of doing some advanced features such as cutting receipt paper, kicking out cash drawers, etc.

## 1. Setting up Raw Printing in ERPNext

### 1.1 Installing QZ Tray application on the client computer

Download and install the QZ Tray application on the computer to which your thermal printer is connected. This application can be found at its [official site](https://qz.io/download/). Currently, Windows, macOS, and Linux are supported by QZ Tray. During the installation you will be prompted to install Java if not already installed, please install Java to complete the installation.

Further instructions on installing the QZ Tray Application can be [here](https://qz.io/wiki/using-qz-tray).

### 1.2 Create Raw Commands Print Format

To be able to send raw commands to a printer you need to first create a print format in raw commands. Jinja Templating Language is used in raw commands just like in the [HTML custom print format](/erpnext/print-format).

To create a new print format for Raw Printing:

1. Go to print format list: **Home > Settings > Printing > Print Format**
2. Click on New.
3. Select the relevant DocType.
4. Check the **Custom format** and **Raw Printing** options.
5. Fill in the **Raw Commands** field with the required raw commands to be sent to the printer.
6. Click Save.

 ![Raw Commands Print Format](/files/raw-command-print-format.png)

Currently, any string-based printer languages can be used in the `Raw Commands` field in the print format. Writing raw commands requires knowledge of the printer's native language provided by the printer manufacturer. Please refer to the developer manual provided by the printer manufacturer on how to write their native commands.

### 1.3 Enable Raw Printing in the Print Setting

To enable Raw Printing:

1. Go to: **Home > Settings > Printing > Print Settings > Raw Printing**.
2. Check the **Enable Raw Printing** option.
3. Save.

## 2. Methods to utilize raw printing in ERPNext

There are two ways to send Raw Printing commands to your printer.

### 2.1 Clicking print on the print view page

To print a raw command print format from the Document print view:

1. Select appropriate print format. For print format in Raw Commands, "No Preview available" message is shown in place of the print preview.
2. Click on the print button.
3. Please allow the connection prompt from the QZ Tray for the actions that you initiated (Keyboard Shortcut: Alt + A).
 - ![QZ Tray Prompt](/files/qz-tray-prompt.png)
4. You may be asked to select the "print format - printer mapping".
 - This mapping is used to send the print commands to the appropriate printer.
 - The printer needs to be installed on your computer to be able to map it to a print format.
 ![print format - printer mapping](/files/printer-settings.png)
 - This mapping is stored locally on the same computer and will have to be set on each client machine.
 - You can also edit this by clicking on the **Printer Settings** button.

 ![Raw Printing from Print View](/files/raw-printing-from-print-view.gif)

### 2.2 Calling Raw Print functions from a client script

It is often a requirement that a print command has to be issued on a certain event (like submit, save, amend, etc.). It is possible to write a [client script](/erpnext/client-scripts) to do this for you.

Following are the relevant Raw Print functions:

1. function: `frappe.ui.form.qz_connect`
 - A connection wrapper to establish a connection with the QZ Tray application.
 - Returns a promise which resolves on successful establishment of a connection.
 - Allows active and inactive connections to resolve regardless. Hence it can be called every time before sending a command.
 - Usage example:

```
 frappe.ui.form.qz_connect()
 .then(function () {
 return qz.print(config, data);
 })
 .then(frappe.ui.form.qz_success)
 .catch(err => {
 frappe.ui.form.qz_fail(err);
 });
```

Here, `qz` is a global object provided by the `qz-tray.js` library.

2. function: `frappe.ui.form.qz_get_printer_list`
 - Gives you the list of printers available to the QZ Tray application
 - Returns a promise which resolves to a list of printers

 Usage example:
```
 frappe.ui.form.qz_get_printer_list().then(
 // Required action on getting the printer list.
 // Note: Printer list is a array of strings.
 );
```

3. function: `frappe.ui.form.qz_success`
 - Displays a "Print Sent to the printer!" alert to the user. Can be called after the print command is successful.

4. function: `frappe.ui.form.qz_fail`
 - Displays the error message to the user. Should be called on failure of QZ Tray connection.

You can also directly access the functions provided by the `qz-tray.js` library via the `qz` object. [Click here for qz-tray.js library documentation](https://qz.io/api/). Note: The `qz` object is initialized only after calling the `frappe.ui.form.qz_connect` for the first time. In case you require the `qz` object before that you can use the `frappe.ui.form.qz_init`.

### 3. Related Topics
1. [Print Settings](/erpnext/print-settings)
1. [Print Format](/erpnext/print-format)
1. [Print Style](/erpnext/print-style)

<!-- page: erpnext/erpnext__razorpay-integration.md -->
---
title: "RazorPay Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/razorpay-integration"
updated: "2026-02-26"
---


A payment gateway is an e-commerce application service provider service that authorises credit card payments for e-businesses, online retailers, bricks and clicks, or traditional brick and mortar.

A payment gateway facilitates the transfer of information between a payment portal (such as a website, mobile phone or interactive voice response service) and the Front End Processor or acquiring bank.

To setup RazorPay,

`Explore > Integrations > RazorPay Settings`

![Razorpay Settings](/files/razorpay-api.gif)

#### Setup RazorPay

To enable RazorPay payment service, you need to configure parameters like API Key, API Secret

![Razorpay Settings](/files/razorpay_settings.png)

On enabling service, the system will create Payment Gateway record and Account head in the Chart of Account with account type as Bank.

![Razorpay COA](/files/razorpay_coa.png)

Also, it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

![Payment Gateway Account](/files/payment_gateway_account_razorpay.png)

After enabling service and configuring Payment Gateway Account your system is able to accept online payments.

####Supporting transaction currencies

RazorPay will only work for the company having `INR (Indian Rupee)` as a Currency.

<!-- page: erpnext/erpnext__rebuild-tree.md -->
---
title: "Rebuild the Chart of Accounts Tree | ERPNext Documentation"
description: "Learn when and how to rebuild the Chart of Accounts tree in ERPNext, repair hierarchy indexes, verify General Ledger filters, and avoid unnecessary repairs."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/rebuild-tree"
updated: "2026-08-03"
---

Use **Rebuild Tree** when the parent-child structure of the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts) is correct on the Account records but ERPNext behaves as though some Accounts belong to the wrong branch. The tool recalculates the internal tree indexes that ERPNext uses to organize Accounts and include descendants in accounting reports.



This is a repair tool, not routine accounting maintenance. Do not use it merely because two reports show different totals. First verify their Company, date, Account, Finance Book, currency, Cost Center, Project, and other filters.

## When rebuilding may help

The existing ERPNext guidance describes a case in which the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) is filtered to one Account but rows from a different Account appear. Rebuilding can help when the Account tree indexes no longer match the saved parent relationships.

Other signs can include:

- a child Account is missing from a group total even though its **Parent Account** is correct;
- a parent filter includes Accounts that are no longer below that group;
- an Account appears under the correct parent in the tree, but the [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet) or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement) groups it incorrectly;
- a recent Account-parent change is not reflected consistently across tree-based reports.

> Selecting a group Account in General Ledger intentionally includes its descendant ledgers. Seeing several Accounts is therefore not, by itself, proof that the tree is damaged.

## Before you begin

1. Refresh the report and verify every relevant filter.
2. Confirm whether the selected Account is a group. Group Accounts normally return their descendants.
3. Open each affected Account and confirm its **Parent Account**, **Root Type**, **Report Type**, Company, and group status.
4. Review recent changes made through [Change the Parent Account](https://docs.frappe.io/erpnext/changing-parent-account), imports, patches, or custom applications.
5. If this is a production site, run the repair during a controlled maintenance window and ensure a current backup is available.

Do not edit internal left and right tree-index values through the database. Rebuild Tree exists to recalculate them from the saved hierarchy.

## Rebuild the tree

1. Open **Accounting &gt; Chart of Accounts**.
2. Select the affected Company.
3. Review the visible root groups and confirm the hierarchy is the one you expect.

![Chart of Accounts tree for Nova Electronics Trading](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-chart-of-accounts-tree.png)

4. Select the three-dot menu in the upper-right corner.
5. Select **Rebuild Tree**.

![Chart of Accounts menu with Rebuild Tree highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-rebuild-tree-action.png)

ERPNext recalculates the Account tree indexes. The tool does not create a [Journal Entry](https://docs.frappe.io/erpnext/journal-entry), change debit or credit amounts, move an Account to a different parent, or rewrite existing General Ledger postings.

## Verify the result

Reopen the report that showed the problem and use the same filters as before. In General Ledger, select the exact ledger Account first. Then test its parent group separately so you can distinguish the single ledger from the group and its descendants.



![General Ledger filtered to Office Maintenance Expenses after checking the tree](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-rebuild-tree-general-ledger-after-rebuild.png)

Confirm that:

1. the exact ledger filter shows only that Account's rows;
2. the group filter shows only the correct descendants;
3. opening, debit, credit, and closing balances agree with the expected vouchers;
4. the Account appears under the correct branch in Chart of Accounts;
5. the same filters produce consistent results in the relevant financial statement.

If totals still differ, investigate report filters, [Finance Books](https://docs.frappe.io/erpnext/finance-book), currencies, posting dates, cancelled entries, or an incorrect Account parent. Rebuilding cannot correct a wrong parent selection or an incorrect accounting voucher.

## What Rebuild Tree changes


| Area                  | Result                                                                       |
| --------------------- | ---------------------------------------------------------------------------- |
| Parent Account values | Remain unchanged.                                                            |
| Internal tree indexes | Recalculated from the saved hierarchy.                                       |
| Account balances      | Remain based on existing General Ledger entries.                             |
| Accounting vouchers   | Not created, cancelled, amended, or reposted.                                |
| Report grouping       | May be corrected when it was caused by inconsistent tree indexes.            |
| Wrong Account parent  | Not corrected. Change the Parent Account first, then rebuild only if needed. |


## Troubleshooting


| Issue                                       | What to check                                                                                                                                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Ledger still shows several Accounts | Confirm whether you selected a group Account. A group filter includes descendants by design.                                                                                                   |
| The wrong branch remains                    | Open the Account and correct **Parent Account**. Rebuild Tree does not decide where an Account belongs.                                                                                        |
| A financial statement total still differs   | Compare Company, dates, Finance Book, currency, dimensions, presentation currency, and accumulated-values settings.                                                                            |
| Rebuild Tree is unavailable                 | Confirm you are in the Chart of Accounts tree view and that your role has permission to use the action.                                                                                        |
| The action returns an error                 | Record the traceback, ERPNext and Frappe versions, and affected Company. Review customizations and ask the administrator or support team to investigate instead of modifying indexes manually. |


## Frequently asked questions

### Does Rebuild Tree change General Ledger entries?

No, It recalculates Account hierarchy indexes. Use [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger) only when an authorized repair must regenerate ledger entries for a supported voucher change.

### Why does a parent Account show several ledger Accounts?

Parent Accounts are groups. Reports use the tree to include their descendant ledgers. Select a non-group Account when you need only one ledger.

### Should I rebuild after every Account change?

No, Normal Account creation and parent changes update the hierarchy. Use the repair only when there is evidence that the stored tree indexes are inconsistent.

### Can Rebuild Tree move an Account to the correct parent?

No, Edit the Account's parent through the supported Chart of Accounts workflow. Rebuild Tree then recalculates indexes from that saved relationship.

### Is Rebuild Tree the same as rebuilding the General Ledger?

No, Rebuild Tree repairs hierarchy indexes. Repost Accounting Ledger regenerates accounting entries for supported source-document changes. They solve different problems.

## Related topics

- [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts)
- [Change the Parent Account](https://docs.frappe.io/erpnext/changing-parent-account)
- [Merge Accounts](https://docs.frappe.io/erpnext/merging-accounts)
- [Freeze an Account](https://docs.frappe.io/erpnext/freeze-account)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger)

<!-- page: erpnext/erpnext__receiving-bulk-payments-in-erpnext.md -->
---
title: "Receiving Bulk Payments in ERPNext | ERPNext Documentation"
description: "Record and allocate one customer receipt across multiple invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/receiving-bulk-payments-in-erpnext"
updated: "2026-07-31"
---

When a Customer sends one payment for several invoices, record one Payment Entry and allocate the amount across all matching invoices. This keeps the bank receipt intact while clearing each invoice correctly.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Receiving Bulk Payments in ERPNext

1. Create a **Receive** Payment Entry for the Customer.
2. Enter the actual bank amount and reference.

![Receive Payment Entry for a bulk customer payment in ERPNext](https://novacompanies.m.frappe.cloud/files/bulk-payment-01-bulk-receipt-overview.png)

3. Select **Get Outstanding Invoices**.
4. Choose the invoices covered by the remittance advice.
5. Enter the allocated amount for each row.
6. Confirm that the total allocation, deductions, and unallocated balance explain the receipt, then submit.

![Allocate a bulk customer payment across multiple invoices in ERPNext](https://novacompanies.m.frappe.cloud/files/bulk-payment-02-bulk-receipt-invoice-allocations.png)

## Important fields and what they mean


| Field                  | What it controls                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Total Allocated Amount | Sum assigned to invoice references.                                                |
| Unallocated Amount     | Receipt balance not yet assigned.                                                  |
| Allocated Amount       | Amount clearing a specific invoice.                                                |
| Outstanding Amount     | Invoice balance before this allocation.                                            |
| Difference Amount      | Amount that must be explained by deductions, exchange difference, or a correction. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### One or more invoices are missing from Get Outstanding Invoices

Confirm that every invoice belongs to the same Customer, Company, and receivable account selected in the Payment Entry. Check that it is submitted, has an outstanding balance, and falls within the dialog's date and filter range.

### Selecting invoice rows does not change the payment amount

The row selection controls which references you keep or remove; it does not replace the actual bank amount. Enter the amount received, then set the **Allocated Amount** for each retained invoice and review **Total Allocated Amount**.

### The receipt is smaller than the combined invoice balances

Allocate the receipt according to the customer's remittance advice. An invoice can remain partially outstanding. Do not reduce an invoice or create an unsupported discount merely to make the allocations equal the invoice totals.

### The customer paid more than the selected invoices

Allocate only the amounts that should clear the invoices. Leave the genuine excess as **Unallocated Amount** so it remains available as a customer advance, or record a separately supported deduction when the difference is a fee or adjustment.

## Frequently asked questions

### Can one receipt be allocated across invoices for different customers?

A Payment Entry has one party. Create separate Payment Entries for each Customer, then reconcile those entries with the combined bank deposit if the bank statement shows one total.

### Can one receipt partially pay several invoices?

Partial allocation is supported. Enter the exact allocation for every invoice. ERPNext reduces each invoice's outstanding amount by its allocation and leaves the unpaid balances open.

### How do I decide which invoice receives the payment first?

Follow the customer's remittance advice. If none is provided, use your documented accounting policy, such as oldest due invoice first, and retain evidence of the decision.

### What if the customer deducts bank fees or withholding tax?

Record the bank receipt exactly as received and use the appropriate deduction, withholding, or adjustment workflow with explicit ledger accounts. Do not silently reduce allocations without explaining the difference.

### Should I use this workflow for a bank deposit containing payments from many customers?

Record a Payment Entry per Customer so party ledgers remain correct. Use [Bank Reconciliation](/erpnext/bank-reconciliation) to match the individual accounting entries to the combined bank deposit when required.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__reconcile-advance-payment-made-to-the-supplier.md -->
---
title: "Reconcile Advance Payment Made to the Supplier | ERPNext Documentation"
description: "Allocate a supplier advance to later Purchase Invoices in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reconcile-advance-payment-made-to-the-supplier"
updated: "2026-08-01"
---

A Supplier advance remains unallocated until the Purchase Invoice is posted. Reconcile the advance against the invoice so the Supplier balance and outstanding amount are correct.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Reconcile Advance Payment Made to the Supplier

1. Confirm that the advance Payment Entry is submitted and still unallocated.
2. Open Payment Reconciliation and select Supplier and the relevant Supplier.
3. Load the unallocated advance and outstanding Purchase Invoice.
4. Enter the amount to allocate and reconcile.
5. Verify the Purchase Invoice outstanding amount and Supplier ledger.

![Reconcile Advance Payment Made to the Supplier in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-11-payment-reconciliation.png)

## Important fields and what they mean


| Field               | What it controls                         |
| ------------------- | ---------------------------------------- |
| Unallocated Payment | Advance available for allocation.        |
| Purchase Invoice    | Supplier invoice receiving the advance.  |
| Allocated Amount    | Amount linked during reconciliation.     |
| Posting Date        | Date used for the reconciliation effect. |
| Difference          | Balance remaining after allocation.      |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The supplier advance is not available

Confirm that the Payment Entry is submitted, belongs to the same Supplier and Company, uses a compatible payable or configured advance account, and still has an unallocated balance.

### The Purchase Invoice does not fetch the advance

Check whether the invoice was created from the Purchase Order referenced by the advance. For an already submitted invoice, use Payment Reconciliation instead of the draft invoice's advance table.

### The supplier has several advances and the wrong one was selected

Compare reference numbers, dates, Orders, currencies, and unallocated amounts before processing. Unreconcile and reallocate through the supported workflow when necessary.

## Frequently asked questions

### Must a supplier advance be linked to a Purchase Order?

It can remain unallocated against the Supplier, but linking the relevant Purchase Order improves traceability and downstream matching.

### Can one supplier advance settle several invoices?

It can be allocated in parts across eligible invoices for the same Supplier and compatible account.

### What happens when the final invoice is smaller than the advance?

Allocate only the invoiced amount. The remainder stays as supplier credit until it is applied to another invoice or refunded.

### Can an advance posted to a separate asset account be reconciled?

Use the supported separate party account configuration. A manual entry to an unrelated asset account will not automatically appear in standard payment reconciliation.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)
