<!-- Frappe documentation: erpnext, part 35 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__lead.md -->
---
title: "Lead | ERPNext Documentation"
description: "Learn how to create, qualify, assign, and convert Leads in ERPNext CRM."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lead"
updated: "2026-07-23"
---

**A lead is a potential customer who might be interested in your products or services.**

To get the customer through the door, you may be doing all or any of the following:

- Listing your product on directories.
- Maintaining an updated and searchable website.
- Meeting people at trade events.
- Advertising your products or services.

When you send out the word that you are around and have something valuable to offer, people will come in to check out your products. These are your Leads.

They are called Leads because they may lead you to a sale. Sales executives usually work on leads by calling them, building a relationship and sending information about products or services. It is important to track all this conversation to enable another person who may have to follow-up on that contact. The new person is then able to know the history of that particular Lead.

To access the Lead list, go to:

> Home > CRM > Sales Pipeline > Lead

- How to Create a Lead
- Go to the Lead list and select New.
- If the person represents an organization, check the 'Lead is an Organization' checkbox. Notice that when you check, the 'Company Name ' field becomes mandatory. Enter the Company Name.
- If the person is an individual, leave the checkbox unchecked and enter Person Name and Gender.
- Enter the 'Email Address'.
- **Status is the important field** in the Lead. You can set the status manually and also it will be updated automatically based on your actions against the lead. Lead: This is the default status assigned when a Lead is created and it indicates an action is needed against this Lead.  
 Open: Sales executive needs to contact the Lead.  
 Replied: A sales executive has provided the information needed and response from Lead is awaited.  
 Opportunity: If an Opportunity is created against the Lead, the status is set to Opportunity. It indicates that the Lead is qualified and may lead to sales.  
 Quotation: If a quotation is created against a Lead, then the status is set to Quotation.  
 Lost Quotation: If the quotation given to the lead has been marked as lost, then the status is set to 'Lost Quotation'.  
 Interested: The lead is interested in the products or services.  
 Converted: If the quotation given to the Lead has resulted in confirmation of an order and if the Sales Order has been created against the quotation, then the status is set to Converted.  
 Do Not Contact: Lead is not interested and no further communication is needed.
- You can set the Lead Source in Source field.
- Enter email ID for communication.
- select 'Save'.

![Lead](/files/lead.png)

You can also record the details of the conversation in the NOTES section.

Further details like Lead Type, Market Segment, Industry can be added in the 'MORE INFORMATION' section.

If you have a healthy number of leads, all this information will help you prioritize the leads you can pursue.

You can assign the Lead to a user by clicking on 'Assign' button on left bar. You can also attach files/images by clicking on 'Attach File' button.

- Features

### Reminders to Follow Up on the Leads

It is important to reach out to leads from time to time and build the relationship. You can create a calendar event from the **Activities** tab for the user and a notification will be shown on that date.

### Adding Multiple Contacts and Addresses

In Busines-to-business(B2B) scenario, in order to close a sales deal, you will have to contact multiple people working in the prospective company. You can add the details of all such people in the same lead. Once you save a Lead, you will get the option to add [Contact](/erpnext/contact) details by clicking on 'New Contact' button. Similarly, you can add the [Address](/erpnext/address) details by clicking on 'New Address'.

![Multiple Contacts and Addresses in Lead](/files/multiple-addresses-and-contacts-in-lead.png)

### 3 Recording Comments, Emails and Events

- **Comments**: You can write your comment in 'Add a comment' box and select 'Comment'.
- **Emails**: You can send an email to the lead by clicking on the 'New Email' button and when the lead responds to your email, it will be appended to your email creating an email thread.
- **Events**: You can also records the Meetings, Calls etc you have had with the Lead by clicking on 'New Event'

### Creating Opportunity, Customer and Quotation

You can create an Opportunity, Customer or a Quotation from the Make dropdown. Relevant field values will be copied over.

### Auto-assigning the Leads to Sales Executives

> Introduced in Version 12

You can define [Assignment Rules](/erpnext/assignment-rule) to automatically assign the leads to sales executives.

![Lead Assignment Rule](/files/lead-assignment-rule.png)

- Adding Custom Fields

You may need to add custom fields to capture additional details as per your needs.

You can customize the Lead DocType using [Customize Form](/erpnext/custom-field) tool.

- Related Topics
- [Opportunity](/erpnext/opportunity)
- [Customer](/erpnext/customer)
- [Difference between Lead, Contact, and Customer](/erpnext/difference_between_lead_contact_and_customer)

<!-- page: erpnext/erpnext__lead_source.md -->
---
title: "Lead Source | ERPNext Documentation"
description: "Learn how to configure Lead Sources in ERPNext and use them to track where leads and sales opportunities originate."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lead_source"
updated: "2026-07-23"
---

**Lead Source is a channel through which the leads are generated.**

It is important to track the source from which you are getting the leads. This will help in measuring effectiveness of various marketing campaigns and allocate the budgets accordingly.

To access the Lead Source list, go to:

> Home > Selling > Settings > Lead Source

- How to Create a Lead Source
- Go to the Lead Source list, select New.
- Enter 'Source Name'.
- Enter 'Details' if you need to elaborate more on the source.

Typical lead sources are contact forms on your website, marketing campaigns, events, references, ads on social media etc.

![Screenshot 2023-12-28 at 10.30.48 AM](/files/Screenshot 2023-12-28 at 10.30.48 AM.png)

The system will allow you to maintain a list of various lead sources leveraged by you.

![Screenshot 2023-12-28 at 10.35.00 AM](/files/Screenshot 2023-12-28 at 10.35.00 AM.png)

<!-- page: erpnext/erpnext__legacy-controller-for-period-closing-voucher.md -->
---
title: "Legacy Controller for Period Closing Voucher"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/legacy-controller-for-period-closing-voucher"
updated: "2026-08-14"
---

A small company can close its Profit and Loss balances in one operation. A company with millions of General Ledger rows may time out when the same work is attempted as one large database transaction. The Period Closing Voucher controller lets ERPNext use either the legacy single-transaction process or newer batched background processing.



The name is technical, but the decision is operational: keep the familiar legacy process for modest ledgers, or use batched processing when volume and accounting dimensions make one large close unreliable.

## Find the setting

1. Open **Accounts Settings**.
2. Open the **Accounts Closing** or Period Closing section.
3. Find **Use legacy controller for Period Closing Voucher**.
4. Save the setting before creating the next closing voucher.

![Use legacy controller for Period Closing Voucher in Accounts Settings](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-legacy-pcv-setting.png)



## Choose the controller


| Setting  | Processing                                                     | Best fit                                                                      |
| -------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Enabled  | Processes the voucher in one database transaction.             | Small and medium ledgers where closing completes reliably.                    |
| Disabled | Splits work into background batches, including date-wise jobs. | Large ledgers, timeouts, and closes that must preserve dimensional reversals. |


With the legacy controller, reversals are primarily account-based. Batched processing is designed to honour dimensional postings more fully. Test the result in a representative environment and reconcile the closing account before changing a live year-end process.

## Troubleshooting

### The voucher remains queued

Check background workers, failed jobs, error logs, and the voucher status. Do not submit duplicate closing vouchers until you know whether the queued job posted any entries.

### The closing totals differ after switching

Compare company, fiscal year, Finance Book, cost-center option, dimensions, and source ledger entries. Reconcile the General Ledger to the approved Profit and Loss before accepting the result.

## Frequently asked questions

### Should every company disable the legacy controller?

Change it only for a clear reason such as volume, timeout risk, or dimensional processing. A stable close does not need extra complexity.

### Can I switch after a voucher has started?

Do not change processing assumptions mid-run. First confirm the job state and whether entries were posted, then follow an approved recovery plan.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__letter-head-in-the-report.md -->
---
title: "Letter Head in the Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/letter-head-in-the-report"
updated: "2026-03-04"
---


In the reports, Letter Head is fetched from the Company master.

To have the company's Letter Head fetched correctly in the report, please ensure that you have updated the default Letter Head in the Company master.

> Explore > Accounting > Company

![Letter Head](/files/using-print-format.png)

In a Company master, if no Letter Head is set as default, then in the reports, Letter Head having Default field checked will be fetched.

![Letter Head](/files/using-print-format-1.png)

If you are managing multiple companies in a single ERPNext account, then ensure that for each Company, default Letter Head is set in the Company master.

After updating Letter Head in the Company master, refresh your ERPNext account, and then check the print format of a report.

<!-- page: erpnext/erpnext__letter-head.md -->
---
title: "Letter Head\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/letter-head"
updated: "2026-03-02"
---


**A Letter Head contains your organization's name, logo, address, etc which appears at the top portion in documents.**

Every company has a default Letter Head. These Letter Head values are generally set as Header and Footer in the documents. In ERPNext, you can capture these details in the Letter Head master.

These details will appear in the Print Format of transactions like Sales Order, Sales Invoice, Salary Slip, Purchase Order, etc. In ERPNext, the Letter Head is only for setting up the top part of the document, other content is pre-formatted and can be configured via [Print Format](/erpnext/print-format) and [Print Headings](/erpnext/print-headings).

To access Letter Head, go to:
> Home > Settings > Letter Head

## 1. How to create a Letter Head
1. Go to the Letter Head list, click on New.
1. Enter a name for the Letter Head. You can create a separate Letter Head for different office locations.
1. Choose whether based on image or HTML.
1. You can enter details in a Letter Head by using:

 * Logo Image: Click on the Attach button to attach an image. Once the image is inserted, HTML for it will be generated automatically.
 * Other information (like Address, tax ID, etc.) that you want to put on your Letter Head.

 ![Print Heading](/files/letter-head.png)

 > If you want to make this the default Letter Head, click on "Default Letter Head".

1. After entering values in the Header and Footer section, save the Letter Head.

You can set the Letter Head based on HTML to make changes to it:

![Letter Head based on](/files/letter-head-based-on.gif)

This is how the Letter Head looks in a document's print.

![Print Heading](/files/letter-head-1.png)

> Note that Footer will be visible only when the document's print is seen in the PDF. Footer will not be visible in the HTML based print preview.

## 2. Video

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/cKZHcx1znMc?end=58&amp;rel=0">
</iframe>



### 3. Related Topics
1. [Address Template](/erpnext/address-template)
1. [Terms and Conditions](/erpnext/terms-and-conditions)
1. [Cheque Print Template](/erpnext/cheque-print-template)
1. [Print Headings](/erpnext/print-headings)

<!-- page: erpnext/erpnext__linkedin-settings.md -->
---
title: "LinkedIn Settings | ERPNext Documentation"
description: "Configure the LinkedIn integration settings in ERPNext for publishing supported social posts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/linkedin-settings"
updated: "2026-07-23"
---

> Note: This integration is deprecated and will be removed in v15. 

LinkedIn related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

1. How to set up LinkedIn Developer App

---

You must have LinkedIn Developer App for your company. ERPNext interacts with this App for sharing the post.

### Create LinkedIn Developer App

Create App by link `https://www.linkedin.com/developers` fill all the details and verify it. And that App has the following products.

1. Share on LinkedIn
2. Sign In with LinkedIn
3. Marketing Developer Platform ![LinkedIn Developer App Product](/files/linkedin-dev-products.png)

### Configure Redirect URLs:

1. Goto your LinkedIn Developers App then **Auth** tab.
2. In **OAuth 2.0 settings** section add **Redirect URLs**: `https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Click **Update** to make changes. ![LinkedIn Redirect URL](/files/linkedin-redirect-urls.png)
4. How to set up LinkedIn Settings

---

To access LinkedIn Settings, go to:

> Home > CRM > Settings > LinkedIn Settings

Current availability

This integration is deprecated. Confirm support in your ERPNext version and the current LinkedIn API requirements before configuring new credentials.



### Company ID

You get the Company ID from your LinkedIn Company URL. 

![LinkedIn Company ID](/files/linkedin-company-id.png)



### Consumer Key and Consumer Secret

You get **Consumer Key** and **Consumer Secret** from your LinkedIn Developer account go to:

> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

![LinkedIn Client](/files/linkedin-client.png)



Once you save the doc by filling **Company ID**, **Consumer Key**, and **Consumer Secret** it will redirect to LinkedIn's sign-in page by providing valid LinkedIn credentials and clicking Allow, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. 

![Authorize LinkedIn](/files/authorize-linkedin.jpg)

<!-- page: erpnext/erpnext__linking-emails-to-document.md -->
---
title: "Linking Emails to Documents"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/linking-emails-to-document"
updated: "2026-03-02"
---


> Introduced in v12
> 
> 

**An email can be linked to multiple documents in ERPNext.**

This can be done in the following two ways:

* Email Aggregation in Contact, Customer, Supplier.
* Automatic Email Linking.

1. Email Aggregation for Customer and Supplier
----------------------------------------------

Email Aggregation takes place in Contact, Customer, and Supplier. All the Emails sent or received from a Contact can be viewed in that Contact's Timeline and as well as linked Customer's or Supplier's Timeline. To enable Email Aggregation, do the following:

1. In a Contact, add Links for the Customer or Supplier respectively.

![Add Customer/Supplier in Contact](/files/contact-link.png)
2. Now when an Email is sent to or received from the Contact associated with Customer or Supplier, that email is linked to the Customer or Supplier mentioned in the Links section of the Contact.

![With Filters](/files/email_aggregation.gif)

2. Automatic Email Linking to a Document
----------------------------------------

Automatic Email Linking links an Email to the Document specified in the unique Email Address generated by the system for a document. If an Email is sent or received using the unique Email Address, the system will link that Email to the Document.

1. Enable Automatic Email Linking in Email Account. This feature can be used only with one Email Account at a time.

![Add Customer/Supplier in Contact](/files/enable_email_link.png)
2. Once this feature has been enabled, you will see a unique Email ID generated using the Email ID mentioned in the Email Account.
3. Now you can copy the Email ID by clicking on it and you can send or receive Emails using the unique Email ID. If an Email contains this unique Email ID either in the Recipients or Cc section, the system will link that Email to the specified Document.

![Add Customer/Supplier in Contact](/files/email_link.gif)


> Note: Email linking with BCC is not supported. You have to add unique email as receipient in TO or CC.
> 
> 

### 3. Related Topics

1. [Auto Email Reports](/erpnext/auto-email-reports)
2. [Sending Email from any Document](/erpnext/sending-email)
3. [Document Follow](/erpnext/document-follow)

<!-- page: erpnext/erpnext__local_overrides.md -->
---
title: "Sales and Payment Transactions\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/local_overrides"
updated: "2026-07-02"
---


In order to be compliant with the latest finance law applicable to POS software, ERPNext automatically registers all sales and payment transactions in a chained log.

If your country is set to "France", the deletion of sales and payment transactions will also not be permitted, even if the appropriate permissions are given to the user.

Please note that ERPNext is not yet fully compliant with the 2016 Finance Law.

# Chained log Report

A dedicated report called "Transaction Log Report" is available to verify that the logged chain has not been broken.

If the status of the column "Chain Integrity" is "True", the chain has not been broken.
It means that you can consult the full chain of events that occurred in your system.

If the status of the column "Chain Integrity" is "False", it means that there is a discrepancy in the chain.
In this case, the previous row has been removed or altered in the database. It is a probable effect of a fraudulent behavior.

<!-- page: erpnext/erpnext__lower-deduction-certificate.md -->
---
title: "Lower Deduction Certificate\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lower-deduction-certificate"
updated: "2026-02-27"
---


According to the tax withholding category, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the government wants the payers to deduct tax beforehand and deposit it with the government. However this scheme of deducting tax at source may cause issues to a few taxpayers who may not have taxable income for that fiscal year.

Therefore, for such taxpayers, the government provides an option to obtain a certificate confirming to either a lower rate or NIL rate of TDS compared to the rate specified in the tax withholding category.

## 1. Prerequisites
Before creating and using a Lower Deduction Certificate, it is advised to create and study the following first:

1. [Supplier](/erpnext/supplier)
1. [Tax Withholding Category](/erpnext/tax-withholding-category)

## 2. How to create a Lower Deduction Certificate
1. Go to the Lower Deduction Certificate list and click on New.
1. Enter the Certificate No.
1. Select the Section Code.
1. Enter the [Fiscal Year](/erpnext/fiscal-year).
1. Select the Supplier having a valid PAN number. PAN number will be auto fetched on the selection of Supplier.
1. Enter Valid From and Valid Up To dates.
1. Enter rate of TDS as per the certificate and the certificate limit.
1. Click on Save.

 ![Lower Deduction Certificate](/files/lower-deduction-certificate.png)

## 3. Using Lower Deduction Certificate

### 3.1 Use in Purchase Invoice

In the following example, we have selected TDS category as 'TDS - 194D - Individual' which has a rate of 5%.

 ![Tax Withholding Category](/files/tax-withholding-category.png)

1. Set the Tax Withholding Category for the Supplier in the supplier master. Then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not and the TDS category will be auto-fetched.

 ![Supplier With Tax Withholding Category](/files/supplier-with-tax-withholding-category.png)

1. Let's create an invoice for 20,000. Saving the invoice automatically calculates tax and appends it in the Purchase Taxes and Charges table. Although the tax category assigned to the supplier has a tax rate of 5%, the prevailing tax rate is 1% which is mentioned in the Lower Deduction Certificate.

 ![Lower TDS in Purchase Invoice](/files/lower-tax-withholding-in-purchase-invoice.png)

### 4. Related Topics
1. [Tax Withholding Category](/erpnext/tax-withholding-category)

<!-- page: erpnext/erpnext__loyalty-points-redemption-in-pos.md -->
---
title: "Loyalty points redemption in POS"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/loyalty-points-redemption-in-pos"
updated: "2026-03-02"
---

In ERPNext POS module, the invoices are auto generated. You can set your complete POS system right with the following configuration steps:   
* Create a Loyalty program in the doctype: You can set Single Tier or a Multiple Tier Program based on the slabs existing in the amount of Purchase that is done in ERPNext.

![](/files/GPSIGPX.png)* Once the loyalty program is set, you can create a Customer and link the Loyalty program to it.

![](/files/9Wphzgr.png)Once this Customer is linked to the Loyalty program, you can now setup your POS profile if it is not set yet:  
![](/files/Lw5UhFp.png)  
Now, you can go to POS transaction:* Select Customer
* Add items
* Pay
* Check the field --> **Redeem Loyalty Points**

![](/files/s2Jps8N.png)

<!-- page: erpnext/erpnext__loyalty-program.md -->
---
title: "Configure Customer Loyalty Programs | ERPNext Documentation"
description: "Set up ERPNext Loyalty Program tiers, earning and redemption factors, customer enrollment, point expiry, and Sales Invoice redemption."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/loyalty-program"
updated: "2026-07-25"
---

A Loyalty Program awards points from submitted sales and lets eligible Customers redeem those points on later [Sales Invoices](/erpnext/sales-invoice). Programs can use one tier or several tiers based on a Customer's cumulative eligible spend.

## Before you begin

Confirm:

- Eligible [Customers](/erpnext/customer), Customer Groups, and Territories.
- The Company currency and loyalty expense account.
- A Cost Center for redemption when required.
- A policy for earning, redemption value, expiry, returns, and tier upgrades.

Test point creation and accounting on the demo Company before enrolling Customers.

## Create a Loyalty Program

1. Open the Loyalty Program list and select **Add Loyalty Program**.
2. Enter the Program Name.
3. Select **Single Tier** or **Multiple Tier**.
4. Set From Date and To Date.
5. Restrict the Customer Group and Territory when required.
6. Enable **Auto Opt In** only when all eligible Customers should join automatically.
7. Add the tier rows.
8. Configure redemption and expiry.
9. Save.

![An ERPNext Loyalty Program with dates, eligibility, and enrollment settings.](https://novacompanies.m.frappe.cloud/files/loyalty-program-form.png)

## Configure tiers

![The Loyalty Program tier table with collection factors and thresholds.](https://novacompanies.m.frappe.cloud/files/loyalty-program-tiers.png)


| Field             | What it means                                           |
| ----------------- | ------------------------------------------------------- |
| Tier Name         | Label assigned when the Customer reaches the threshold  |
| Collection Factor | Eligible amount required to earn one point              |
| Minimum Amount    | Cumulative spend required for the tier                  |
| Auto Opt In       | Enrolls all Customers that match the program conditions |


Example: with a Collection Factor of $100, an eligible $1,000 invoice earns 10 points.

Minimum Amount is evaluated from cumulative eligible sales for the Customer, not only the current invoice.

## Configure redemption

Set:

- **Conversion Factor** for the monetary value of one point.
- **Expense Account** used for the loyalty benefit.
- **Cost Center** where required.
- **Expiry Duration** in days.

Keep earning and redemption factors distinct. A Customer might spend $100 to earn one point while each redeemed point is worth $1.

## Enroll a Customer

If Auto Opt In is disabled:

1. Open the Customer.
2. Select the Loyalty Program.
3. Save.

![A Customer assigned to the Nova Rewards Loyalty Program.](https://novacompanies.m.frappe.cloud/files/loyalty-program-customer.png)

## Earn points

Create and submit an eligible Sales Invoice. ERPNext creates a Loyalty Point Entry linked to the Customer and invoice.

Open **Loyalty Point Entry** to audit earned and redeemed points. Returns and cancellations can affect the available balance, so use the ledger rather than a manually maintained total.

## Redeem points

1. Create a Sales Invoice for the enrolled Customer.
2. Add the Items.
3. Open the Loyalty Points section.
4. Enable **Redeem Loyalty Points**.
5. Enter the number of points.
6. Confirm the Redemption Account and Cost Center.
7. Review the invoice total and submit.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## Troubleshooting


| Problem                              | What to check                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| No points are earned                 | Confirm enrollment, program dates, eligibility, submitted invoice, and tier factor |
| Redeem Loyalty Points is unavailable | Confirm that the Customer has a program and available points                       |
| The tier is unexpected               | Review cumulative eligible spend and minimum thresholds                            |
| Points expired earlier than expected | Check Expiry Duration and the Loyalty Point Entry dates                            |
| Redemption accounting is incorrect   | Review the program's Expense Account and Cost Center                               |


## Frequently asked questions

### Can a program have several tiers?

Yes. Use Multiple Tier and add each threshold in ascending order.

### Are points awarded on draft invoices?

No. The earning workflow depends on submitted eligible invoices.

### Can every Customer be enrolled automatically?

Yes. Enable Auto Opt In and define the eligible Customer Group and Territory.

### Where can I audit a Customer's points?

Use Loyalty Point Entry and the Customer's linked records.

## Related topics

- [Customer](/erpnext/customer)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Applying a Discount](/erpnext/applying-discount)
- [Point of Sale](/erpnext/point-of-sale)

<!-- page: erpnext/erpnext__maintain-stock-field-frozen-in-item-master.md -->
---
title: "Maintain Stock field Frozen in the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintain-stock-field-frozen-in-item-master"
updated: "2026-02-26"
---


In the item master, you might witness values in the following fields to be frozen.

1. Maintain Stock
1. Has Batch No.
1. Has Serial No.

![Item Field Frozen](/files/maintain-stock-1.png)

For an item, once stock ledger entry is created, values in these fields will be frozen. This is to prevent user from changing the value which can lead to mis-match of actual stock, and stock level in the system of an item.

For the serialized item, since its stock level is calculated based on the count of available Serial Nos., setting Item as non-serialized mid-way will break the sync, and item's stock level shown in the report will not be accurate, hence Has Serial No. field is frozen.

To make these fields editable once again, you should delete all the stock transactions made for this item. For the Serialized and Batch Item, you should also delete Serial No. and Batch No. record for this item.

<!-- page: erpnext/erpnext__maintaining-suppliers-part-no-in-item.md -->
---
title: "Maintaining Supplier's Item Code In the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintaining-suppliers-part-no-in-item"
updated: "2026-03-02"
---


For each item, code assigned might differ from the code your supplier has given to that same item. ERPNext allows you to track Supplier's Item Code in the item master. Also you can fetch Supplier's Item Code in your purchase transactions, so that they can easily recognize item referring to their Item Code.

#### 1. Updating Supplier Item Code In Item

In the Item master, under Supplier Details section, enter Item Code as given by the Supplier to this item.

![Supplier Item Code](/files/supplier-item-code.png)

#### 2. Supplier's Item Code In Transactions

Each purchase transaction has field in the Item table where Supplier's Item Code is fetched. This field is hidden in form as well as in the Standard print format. You can make it visible by changing property for this field from [Customize Form.](/erpnext/customize-form.html)

Go to print view, click on Menu > customize, enter a new print format name, look for the Items table, click on the **Select columns** button in it. You'll see the following screen. Now select the "Supplier Part Number" checkbox.

![Supplier item part print format](/files/supplier-item-code-print-format.png)

Supplier Item Code will only be fetched in the purchase transaction, if both Supplier and Item Code selected in purchase transaction is mapped with value mentioned in the Item master.

![Supplier Item Code in transaction](/files/supplier-item-code-in-purchase-order.png)

<!-- page: erpnext/erpnext__maintenance-sales-orders.md -->
---
title: "Maintenance Sales Orders | ERPNext Documentation"
description: "Learn how to create Maintenance Sales Orders in ERPNext for service visits, maintenance schedules, recurring support, and follow-up activities."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-sales-orders"
updated: "2026-07-23"
---

# Maintenance Sales Orders

A Maintenance Sales Order records an agreed maintenance service for a Customer. It uses the Sales Order workflow while enabling maintenance-related actions and allowing service invoicing without a stock delivery.

## Before you begin

Create the [Customer](/erpnext/customer), service [Item](/erpnext/item), and required serial-number or installation details. Confirm access to the maintenance documents used by your process.

## Create a Maintenance Sales Order

1. Open **Sales Order** and select **Add Sales Order**.
2. Select the Company and Customer.
3. Set **Order Type** to **Maintenance**.
4. Add the maintenance Item, quantity, rate, and service date.
5. Enable **Skip Delivery Note** when no stock delivery is needed.
6. Review taxes, payment terms, addresses, and terms.
7. Save and submit the order.

![A full-screen Maintenance Sales Order showing the Skip Delivery Note checkbox beside Order Type.](/files/sales-order-skip-delivery-note-full.webp)

Leave **Skip Delivery Note** disabled when the order includes goods that must be delivered through a [Delivery Note](/erpnext/delivery-note).

## Create maintenance documents

After submission, use the available **Create** actions. Depending on installed features and document state, these can include:

- a **Maintenance Schedule** to plan recurring service;
- a **Maintenance Visit** to record work performed;
- a **Sales Invoice** to bill the Customer.

Review generated documents and confirm the Customer, Items, dates, assigned personnel, serial numbers, and service details.

## Troubleshooting

### Skip Delivery Note is not visible

Confirm that **Order Type** is **Maintenance**. The checkbox is conditional.

### Maintenance actions are missing

Confirm that the order is submitted, required features are configured, and your role can create the target document.

## Frequently asked questions

### Can a Maintenance Sales Order include parts?

Yes, but use the delivery workflow for stock Items that physically leave your Warehouse.

### Is a Maintenance Schedule mandatory?

No. Use it when service must occur on planned dates. A one-time service may use only the documents required by your process.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Maintenance Schedule](/erpnext/maintenance-schedule)
- [Maintenance Visit](/erpnext/maintenance-visit)

<!-- page: erpnext/erpnext__maintenance-schedule.md -->
---
title: "Maintenance Schedule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-schedule"
updated: "2026-02-28"
---


**The Maintenance Schedule shows all upcoming Maintenance Visits.**

All machines require regular maintenance, especially those that contain a lot
of moving parts, so if you are in the business of maintaining those or have
some of them in your own premises, this is a useful tool to plan a calendar of
activities for its maintenance.

To create a new Maintenance Schedule go to:

> Home > Support > Maintenance > Maintenance Schedule

A Maintenance Schedule is usually created from a Sales Order of type 'Maintenance'.

![SO Maintenance Schedule](/files/so-maintenance-schedule.png)

## 1. Prerequisites
* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

## 2. How to Create a Maintenance Schedule
1. Go to the Maintenance Schedule, click on New.
1. Select the Customer and the Items for which maintenance needs to be done.
1. Set the start and end dates.
1. Select a Periodicity to set how frequently the visits will happen. The options are "Weekly", "Monthly", "Quarterly", "Half Yearly", "Yearly" and "Random". Maintenance Schedule will get generated based on selected Periodicity. Selecting Random will generate random dates
1. The Number of Visits will be set as per the Periodicity selected. Eg: If you selected Weekly and set the whole month between the start and dates, 4 visits are ideal.
1. Select the Sales Person performing the visits.
1. Save.
1. After saving, click on the **Generate Schedule** button to generate a Maintenance Schedule.
1. Submit.

 ![Maintenance Schedule](/files/maintenance-schedule-1.png)

The **Generate Schedule** button will generate a separate row for each maintenance activity. Each Item in a Maintenance Schedule is allocated to a Sales Person.

When the document is Submitted Calendar events are created for the Sales Person User for each maintenance.

## 3. Related Topics
1. [Serial Number](/erpnext/serial-no)
1. [Warranty Claim](/erpnext/warranty-claim)
1. [Maintenance Visit](/erpnext/maintenance-visit)
1. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance-visit.md -->
---
title: "Maintenance Visit"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-visit"
updated: "2026-03-02"
---

**A Maintenance Visit is a visit made by an engineer to a Customer’s premise for maintenance work of an Item.**

To access the Maintenance Visit list, go to:


> Home > Support > Maintenance > Maintenance Visit
> 
> 

A Maintenance Visit is usually created from a Sales Order of type 'Maintenance'. ![SO Maintenance Visit](/files/so-maintenance-visit.png)  


1. Prerequisites
----------------

* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

2. How to create a Maintenance Visit
------------------------------------

1. Go to the Maintenance Visit list, click on New.
2. The current date and time will be recorded, this can be edited.
3. Select the Customer.
4. Select the Maintenance Type whether Scheduled, Unscheduled, or Breakdown.
5. Set the completion status whether 'Partially Completed' or 'Fully Completed'.
6. Select the Item Code and Serial Number.
7. Enter a Description of the maintenance, select the Sales Person performing the maintenance, and enter the work done.
8. Save.

![Maintenance Visit](/files/maintenance-visit.png)

### 2.1 Additional Options when Creating Maintenance Visit

* **Customer Feedback**: You can record any feedback given by the Customer regarding this Maintenance Visit.
* The following fields will be fetched from the [Customer](/erpnext/customer) form:


	+ Customer Address
	+ Contact Person
	+ Territory
	+ Customer Group

3. Related Topics
-----------------

1. [Warranty Claim](/erpnext/warranty-claim)
2. [Maintenance Schedule](/erpnext/maintenance-schedule)
3. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance.md -->
---
title: "Maintenance"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance"
updated: "2026-02-27"
---

The maintenance schedule and maintenance visits are vital parts of the ERPNext support module, ensuring that the ERP system remains operational, secure, and aligned with business needs over time. Efficient management of these aspects contributes to a reliable and optimized ERP environment for users.

* [Maintenance Schedule](/erpnext/user/manual/en/maintenance-schedule)
* [Maintenance Visits](/erpnext/user/manual/en/maintenance-visit)

<!-- page: erpnext/erpnext__make-a-colorful-gantt-chart.md -->
---
title: "Make A Colorful Gantt Chart\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/make-a-colorful-gantt-chart"
updated: "2026-03-02"
---


ERPNext allows users to add colours to certain documents for better visual cues and representation. A good example of this would be the [Event Calendar](/erpnext/how-to-sync-doc-types-with-calendar), where, for each event you can add a colour.

We will be doing so by customizing [Tasks](/erpnext/tasks) under Projects module.

## Steps To Add Colours To The Gantt Chart

1. Go to [Customize Form](/erpnext/customize-form) in the system and select *Task* in _Enter Form Type_ option. Alternatively, you can reach this screen by going to **Menu > Customize** from the Task list or form.

 ![customize-form](/files/project-gantt-customize-form-1.gif)

1. Add a new field in the doctype of fieldtype color.
1. Check *In List View* option.

 ![customize-form](/files/project-gantt-in-list.png)

1. Save the form, go back to the Task list, and reload.
1. When opening an existing or new Task, you should see a color field. Pick a color for the Task.

 ![customize-form](/files/project-gantt-pick-color.png)

1. Go back to the Task list and switch to Gantt view.

 ![customize-form](/files/project-gantt-colors.png)

<!-- page: erpnext/erpnext__making-custom-reports.md -->
---
title: "Making Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-custom-reports"
updated: "2026-03-06"
---


There are three kind of reports in ERPNext.

### 1. Report Builder

Report Builder is an in-built report customization tool in ERPNext. This allows you to define specific fields of the form which shall be added in the report. Also you can set required filters, sorting and give preferred name to report.


&lt;iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0"&gt;
&lt;/iframe&gt;



### 2. Query Report

Query Report is written in SQL which pulls values from account's database and displays the same in the report. Though SQL queries can be written from front end, like HTML, it has been restricted for ERPNext cloud users. This is because it allows users with no access to specific report to fetch data directly from the database.

Check Purchase Order Item to be Received report in Stock module for example of a Query report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/query-report) to learn how to create Query Report.

### 3. Script Report

Script Reports are written in Python and stored on server side. These are complex reports which involves logic and calculation. Since these reports are written on server side, customizing it from hosted account is not possible.

Check Financial Analytics report in Accounts module for an example of Script Report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/script-report) to learn how to create Script Report.

&gt; Note: **Dynamic Filter** is available in Script Reports and Query Reports; however, not in the Report Builder.

<!-- page: erpnext/erpnext__making-fields-visible-in-print-format.md -->
---
title: "Customizing Field Visibility in Print Format\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-fields-visible-in-print-format"
updated: "2026-03-02"
---


Each transaction has a Standard Print Format. In the Standard format, only certain fields are displayed by default. If a user wants to display a particular field in the Standard format, it can be customized by using Customize Form tool.

Let's assume in the Sales order, we need to make Shipping Address field visible in the standard print format.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Document Type

As per our scenario, Sales Order will be selected as Document Type.

![Document Type](/files/customize-make-fields-visible.png)

#### Step 3: Disable Print Hide

Click to open field to be made visible in the Standard Print Format. Disable **Print Hide** field.

![Uncheck Print Hide ](/files/customize-visible in print.gif)

#### Step 4: Update

Update Customize Form to save changed. Reload your ERPNext account, and then check Print Format for confirmation.
