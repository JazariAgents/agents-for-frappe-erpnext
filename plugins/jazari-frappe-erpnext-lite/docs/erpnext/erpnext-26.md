<!-- Frappe documentation: erpnext, part 26 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__exotel_integration.md -->
---
title: "Exotel Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/exotel_integration"
updated: "2026-02-26"
---


This integration allows you to integrate Exotel into your ERPNext account. Leads and their phone numbers captured via Exotel can be saved directly to your ERPNext.

## 1. Features

- Track incoming calls in your ERPNext account.
- Shows existing lead/customer information pop-up to employees when an incoming call is received.

## 2. How to setup

### 2.1 Setup your Exotel account

- Login to your Exotel account and go to App Bazar.
- Create a new App for a new flow.
- Setup the flow as you wish it to be.
- In your connect API under "Create popup..." and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

![Connect Applet](/files/connect_applet.png)
![Call Popup Section](/files/create_popup_section.png)

> **Note:** Replace `<your-site>` in URL with your site name. For example, if the site name is **frappe.erpnext.com** then the URL will be:
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- After that add a Passthru applet under "After Call Conversation ends" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

![After Conversation Ends Section](/files/after_conversation_ends_section.png)

![After call ends section](/files/passthru_end_call.png)

> **Note:** Make sure to check "Make Passthru Async".

- Similary, add a Passthru applet under "If nobody answers..." section and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

![No Response Section](/files/no_response.png)

![After call ends section](/files/passthru_missed_call.png)

> **Note:** Make sure to check "Make Passthru Async".

- Save the flow.
- Now assign this newly created app to your ExoPhone from which you receive your business calls.

### 2.2 Setup in ERPNext

- From Awesome Bar, go to 'Exotel Settings'.
- Set your "Exotel SID" and "Exotel Token". You can find your Exotel API key and token on your [Exotel Dashboard](https://my.exotel.com/apisettings/site#api-credentials).
- Go to Communication Medium.
- Add your ExoPhone and schedule that number. Based on this schedule employees will receive the popup.

<!-- page: erpnext/erpnext__expense_report.md -->
---
title: "Deferred Revenue/Expense Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/expense_report"
updated: "2026-08-14"
---

Nova Industries sells a $1,200 annual warranty service and also prepays $1,200 for a year of software support. The invoices show the full contractual amounts, but finance should recognise only the portion earned or consumed in each accounting period.





The Deferred Revenue and Expense Report compares the expected recognition schedule with actual deferred-accounting postings. It helps finance identify what has already been recognised, what remains deferred, and which invoice or item requires investigation.

## Before you begin

Configure deferred accounts in [Accounts Settings](/erpnext/accounts-settings), enable deferred accounting on the relevant Item or invoice row, and enter valid service start and end dates. Submit the invoice and run [Process Deferred Accounting](/erpnext/process-deferred-accounting) according to the company's schedule.

## Review deferred revenue

![Open the Sales Invoice Item row to review deferred accounting fields](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-item-pencil.png)



![Deferred revenue account and service period on a Sales Invoice Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-service-period.png)



1. Open the Deferred Revenue and Expense Report.
2. Select Nova Industries and the reporting period.
3. Choose the revenue view or filter for Sales Invoices.
4. Review the invoice, item, service dates, expected recognition, actual posting, and remaining amount.
5. Open the invoice or generated Journal Entry when a line needs explanation.

![Loaded Deferred Revenue and Expense Report for Nova annual service revenue](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-deferred-revenue-report.png)

## Review deferred expense

![Deferred expense account and service period on a Purchase Invoice Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-service-period.png)





Use the expense view for prepaid costs from Purchase Invoices. The same report logic shows the portion already recognised as expense and the amount that remains in the deferred asset account.

![Loaded Deferred Revenue and Expense Report for Nova prepaid service expense](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-deferred-expense-report.png)

## Understand the result


| Value                        | What to check                                                 |
| ---------------------------- | ------------------------------------------------------------- |
| Invoice amount               | The original deferred item value and currency.                |
| Service period               | The dates over which revenue or expense should be recognised. |
| Expected amount              | The schedule amount calculated for the selected period.       |
| Actual amount                | The value already posted by deferred accounting entries.      |
| Upcoming or remaining amount | The portion still expected in future periods.                 |


## Verify the accounting

Open the generated Journal Entry and compare the deferred account with the income or expense account in the [General Ledger](/erpnext/general-ledger). Revenue recognition normally debits the deferred revenue liability and credits income. Expense recognition normally credits the deferred expense asset and debits expense.

## Troubleshooting

### An invoice does not appear

Confirm that it is submitted, its item row has deferred accounting enabled, deferred and income or expense accounts are set, and the service dates overlap the report period.

### Expected and actual values differ

Run Process Deferred Accounting for the missing period and inspect failed or draft entries. Also check the Accounts Settings basis and whether generated Journal Entries require submission.

### The same amount appears in the wrong period

Review posting date, service start and end dates, and the deferred-recognition basis. Correct the source through the approved amendment process rather than editing ledger rows.

## Frequently asked questions

### Does this report create accounting entries?

The report explains expected and actual recognition. Process Deferred Accounting creates the recognition entries.

### Can one invoice contain deferred and immediate items?

Deferred behavior is configured at item-row level, allowing other rows to post immediately when their settings and accounts require it.

### Why is the full invoice still visible as receivable or payable?

Deferral changes when income or expense is recognised. It does not normally change the customer's or supplier's contractual invoice balance.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Revenue](/erpnext/deferred-revenue)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__export-data-for-specific-year-or-filter.md -->
---
title: "Export Data for Specific Year or Filter"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/export-data-for-specific-year-or-filter"
updated: "2026-03-29"
---

**Question:** I need to export Sales Invoices for Particular Fiscal Year only.

**Answer:**

The system allows you to use any combination of filters including a Date Range to extract the data whether from the List view or from the Report View.

**List View**

![](/files/image36316a.png)



**Report View**

![](/files/imagebb9c64.png)

<!-- page: erpnext/erpnext__fairlogin-integration.md -->
---
title: "Setting up fairlogin\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fairlogin-integration"
updated: "2026-02-26"
---


fairlogin is an GDPR aware oAuth provider by fairkom.eu.

To setup fairlogin as an oAuth provider, go to:
> Home > Integrations > Social Login Key

## Setup keycloak

fairlogin is based on keycloak, so the parameters may be similar for any custom oAuth setting facilitating keycloak.

There you add a new client, select open-id as client protocol and enter the address of your ERPnext instance as the Root, Redirect and Base URL.

Adding your ERNext service as a client is being [offered as a service by fairkom](https://erp.fairkom.net/cloud/fairlogin-client).

![ERPnext keycloak Settings](/files/fairloginKeycloakERPnext.png)

## Setup fairlogin

To enable fairlogin as an ERPNext login option, you need to configure the following parameters:

- Base URL https://id.fairkom.net/auth/realms/fairlogin/
- Authorize URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/auth
- Redirect URL /api/method/frappe.integrations.oauth2_logins.login_via_fairlogin
- Access Token URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/token
- API Endpoint https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/userinfo

![ERPnext fairlogin Settings](/files/fairloginERPnextSettings.png)

On enabling service, the system will allow to login with any fairlogin account.

The default role of a new user is Blogger (currently hardcoded).

<!-- page: erpnext/erpnext__faqs.md -->
---
title: "Stock FAQs"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/faqs"
updated: "2026-07-02"
---

Is any integration required for using Barcode reader in ERPNext?  
How Valuation Rate is Calculated for an Item  
How to Update valuation after purchase transaction

<!-- page: erpnext/erpnext__feedback-request-using-web-form.md -->
---
title: "Feedback Request Using a Web Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/feedback-request-using-web-form"
updated: "2026-03-04"
---

In the ERPNext version 11, we have a feature which allowed collecting a Feedback from a Customer and users. In ERPNext, this feature is now manageable using built-in customisation tools like:  
* Custom DocType
* Web Form
* Notification

  
Following are the steps on how you should configure a feature and start collecting feedback.  
**Feedback as a DocType**  
Create a Custom DocType for Rating on these lines  
![](/files/oUDbd8e.png)  
1. In the first fields, list a DocTypes for which you want to collect a rating
2. In the Document Name field, just enter the name of first field "document", so that it becomes a [Dynamic Link](https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/articles/dynamic-link-fields) field.
3. Enter a Rating field. You can also choose other data or select field, if you wish to take rating on those lines.

  
**Web Form for Feedback Form**  
Once a DocType is created, simply create a Web Form by fetching all the standard fields from Feedback doctype.  
![](/files/eWKqJ50.png)  
**Create a Notification**  

A Notification should be created to send a link to a user following which they will submit a rating. You can define the conditions for triggering an email based on standard features of [Notification](/erpnext/notifications). Following is the help on how to define a message and link which would take user to a Web Form and allow submitting a rating.  

```
https://example.erpnext.com/feedback?new=1&document=Sales%20Order&document_name={{doc.name}}
```
  
Where:  
* **example.erpnext.com** will be URL of your ERPNext account
* **feedback** will be the name of custom doctype added for collecting a feedback
* **document=Sales%20Order&** will be a name of DocType for which you want to sent a notification
* document_name={{doc.name}} will pick-up specific document name and update in the Document Name field of Feedback form.

  
![](/files/UDBhIaK.png)  
  
**Quick Demo:**  
Here is the demo of how link would be generated, Web Form would be filled and capture in ERPNext.  
![](/files/hEbdh6c.gif)

<!-- page: erpnext/erpnext__fetch-child-table-values-using-jinja-tags.md -->
---
title: "Fetch child table values using Jinja tags"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-child-table-values-using-jinja-tags"
updated: "2026-03-04"
---

Jinja templating can be used to reference any field on any DocType in ERPNext. This can simply be done by calling {{doc.field_name}} on a print format, where 'doc.name' is the variable name for a certain field.

 

However this approach does not work for Child Tables inside a DocType. This article will help you traverse and display all rows pertaining to a child table inside any DocType.

 

**Pre Requisites**

 

We would require the variable name of the child table on the corresponding DocType. This can be viewed from the 'Customize Form' section for the required DocType. The same is illustrated below

![](/files/f7Xxz1S.png)

We will also require the variable names of all the fields inside the child table which need to be referenced. This can be obtained from the 'Customize Form' section of the corresponding child table as shown below

![](/files/tzloEh2.png)

 

![](/files/wPB82f0.png)

 

![](/files/AV0308f.png)

 

![](/files/CW0oEUo.png)

**Method 1. Displaying rows of a Child Table on an unordered list**



{% for row in doc.items %}

* Item Code: {{ row.get_formatted("item_code", doc) }}

Quantity: {{ row.get_formatted("qty", doc) }}

Rate: {{ row.get_formatted("rate", doc) }}

Amount: {{ row.get_formatted("amount", doc) }}


{% endfor %}




 

The output on a print format would be as follows

![](/files/lgLjE7u.png)

 

 

**Method 2. Displaying rows of a Child Table as a table**

 



  

   

  

  

 

 

| Item Code | Quantity | Rate | Amount |
| --- | --- | --- | --- |
| {{item.item_code }} | {{item.qty}} | {{item.rate}} | {{item.amount}} |



 

The output on a print format would be as follows

 

![](/files/GS00WlC.png)

 

This template can be used for reference. Any additional fields on the child table field can be fetched in a similar manner, by amending the Jinja template.

<!-- page: erpnext/erpnext__fetch-the-entire-address-text-on-a-custom-field.md -->
---
title: "Fetch the entire address text on a custom field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-the-entire-address-text-on-a-custom-field"
updated: "2026-03-02"
---

This article will help you to add a custom field for fetching full addresses on any DocType, using a 3 step approach.





**Step 1. Cosmetic customisations on the required DocType**





We would first need to add two new fields on the DocType for fetching addresses:-





a) A field of type 'Link' which points to our Address master

b) A field of type 'Read Only' which would display the full address





Take note of the variable names of the new fields you create. This information will be required later in the process.





![](/files/q90efZM.png)





For information on creating custom fields on a DocType you can refer to the following link - [Custom Fields in ERPNext](https://docs.erpnext.com/docs/v13/user/manual/en/customize-erpnext/custom-field)





Once this step is done you should have two new fields on the selected DocType, as illustrated below:-





![](/files/SabQi7A.png)











**Step 2. Adding a Client Script for fetching the full address from our Address master**





Search for 'Client Script' on the search bar, and create a new Client Script. Select the required DocType on which we need to fetch the address on.





In the section for the script paste the following Client Script:-







```
frappe.ui.form.on("DocType Name", "address_link_field", function(frm, cdt, cdn) {    if(frm.doc.address_link_field){     return frm.call({      method: "frappe.contacts.doctype.address.address.get_address_display",      args: {       "address_dict": frm.doc.address_link_field      },      callback: function(r) {       if(r.message)           frm.set_value("full_address_field", r.message);              }     });    }    else{        frm.set_value("full_address_field", "");    }});
```





Here we will need to replace the the following changes based on your use case:-

a) Replace 'DocType Name' with the Name of the DocType we need to fetch the address on. Eg. Sales Invoice, Purchase Order etc.

b) Replace 'addresslinkfield' with the variable name of the custom link field we created in Step 1

c) Replace 'fulladdressfield' with the variable name of the custom read only field we created in Step 1





Once this is done, you would have a Client Script which looks as below:-





![](/files/VukPzs4.png)





**Step 3. Save, enable and test the Client Script**





Once the Client Script is amended as per your use case, we can Save it and enable it by clicking the 'Enabled' checkbox.

Go to the required DocType and refresh the page for the changes to take effect.





Now when an address is selected on our custom link field, the entire address will be fetched on our custom read only field, as illustrated below:-





![](/files/W3kxhT2.gif)

<!-- page: erpnext/erpnext__fetch-values-from-master.md -->
---
title: "Fetching Values From Master"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-values-from-master"
updated: "2026-03-02"
---


To pull a value of a link on selection, use the `add_fetch` method.

 
 
 add_fetch(link_fieldname, source_fieldname, target_fieldname)
 

### Example

Let' say you have created a Custom Field **VAT ID** (`vat_id`) in **Customer** and **Sales Invoice** and want to make sure that this value gets updated every time you select a Customer in a Sales Invoice.

To configure this, in the Sales Invoice Custom Script, you can add this line:

 
 
 cur_frm.add_fetch('customer','vat_id','vat_id')
 

<!-- page: erpnext/erpnext__fetching-data-from-a-document.md -->
---
title: "Fetching Data from a Document\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetching-data-from-a-document"
updated: "2026-03-04"
---


**Question:** We track Customer's PO Number and PO Date field in the Sales Order. To have these values fetched into Sales Invoice as well, we have inserted Custom Field in the Sales Invoice. However, when we create Sales Invoice from the Sales Order, Customer's PO details are not being fetched.

**Answer:** When data is fetched from one transaction to the another, then mapping of the data is done based on the field names. If two transactions have fields with the exact same name, then it's values are mapped.

For example, if you want Customer's PO No. and PO Date to be fetched from Sales Order to Sales Invoice, then you should ensure that Custom Fields added in the Sales Invoice has an exact same field name as in the Sales Order.

Sales Order (standard fields)

![Standard fields in Sales Order](/files/customize-fetch-data-1.png)

Sales Invoice (custom fields)

![Custom Field in Sales Invoice](/files/customize-fetch-data-2.png)

Since names for the Customer's PO related fields are same in the Sales Order and Sales Invoice, when creating Sales Invoice from the Sales Order, values in these fields are auto-fetched.

![Values fetching from Sales Order to Sales Invoice](/files/customize-fetch-data-3.png)
![Values fetching from Sales Order to Sales Invoice](/files/customize-fetching-data.gif)

<!-- page: erpnext/erpnext__fichier_des_ecritures_comptables.md -->
---
title: "Le Fichier des \u00c9critures Comptables [FEC]\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fichier_des_ecritures_comptables"
updated: "2026-07-02"
---


Since 2014, a legal requirement makes it mandatory for companies operating in France to provide a file of their general accounting postings by fiscal year corresponding to an electronic accounting journal.

For ERPNext users this file can be generated using a report available if you system's country is France.


### Requirements

To generate the report correctly, your Chart of Account needs to be setup according to the french accounting rules.

All accounts need to have a number in line with the General Chart of Account (PCG) and a name.

The SIREN number of your company can be added in the "Company" doctype.


### CSV generation

You can generate the required CSV file by clicking on "Export" in the top right corner of the report.


### Testing Instructions

To test the validity of your file, the tax administration provides a testing tool at the following address: [Outil de test des fichiers des écritures comptables (FEC)](http://www.economie.gouv.fr/dgfip/outil-test-des-fichiers-des-ecritures-comptables-fec)

<!-- page: erpnext/erpnext__field-types.md -->
---
title: "Field Types"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/field-types"
updated: "2026-03-04"
---

The following are the types of fields you can define while creating new ones, or while amending standard ones.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](/erpnext/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](/erpnext/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here.

![Check Field TYpe](/files/field-type-check.png)  


#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

![Select Field Type](/files/field-type-select.png)  


#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

![Table Field Type](/files/field-type-table.png)  


#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

![Attach Field Type](/files/field-type-attach.png)  


#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

![Field Type Image](/files/field-type-image.png)  


#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

![Field Type Text Editor](/files/field-type-text-editor.png)  


#### Date

This field will enable you to enter the Date in this field.

![Field Type Date](/files/field-type-date.png)  


#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

![Field Type Date and Time](/files/field-type-date-and-time.png)  


#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number.

![Field Type Barcode](/files/field-type-barcode.png)  


#### Button

This kind of field will be an action button, like Save, Submit, etc.

![Field Type Button](/files/field-type-button.png)  


#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

![Field Type Code](/files/field-type-code.png)  


#### Color

You will have the option of specifying the color for this Form.

![Field Type Colour](/files/field-type-colour.png)  


#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns.

![Field Type Column Break](/files/field-type-column-break.png)  


#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

![Field Type Currency](/files/field-type-currency.png)  


#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters, making this the most generic field type. To enable validations for Email, Name, or Phone Number inputs, set options to "Email", "Name", "Phone" in Settings > DocType.

![Field Type Data](/files/field-type-data.png)  


#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](/erpnext/set-precision)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

![Field Type Float](/files/field-type-float.png)  


#### Geolocation

Use Geolocation field to store GeoJSON [feature_collection](https://tools.ietf.org/html/rfc7946#section-3.3). Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

Read [Geolocation field](/erpnext/geolocation-field) for more understanding.

![Field Type Geolocation](/files/field-type-geolocation.png)  


#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

![Field Type HTML](/files/field-type-html.png)  


#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

![Field Type Image](/files/field-type-image2.png)  


#### Int (Integer)

The integer field holds numeric value, without decimal place.

![Field Type Integer](/files/field-type-integer.png)  


#### Small Text

Small Text field carries text content and has more character limit than the Data field.

![Field Type Small Text](/files/field-type-small-text.png)  


#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

![Field Type Long Text](/files/field-type-long-text.png)  


#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

![Field Type Text](/files/field-type-text.png)  


#### Markdown Editor

This field will allow you to add the text in Markup language.

![Field Type Markdown Editor](/files/field-type-markdown-editor.png)  


#### Password

The password field will have decoded value in it.

![Field Type Password](/files/field-type-password.png)  


#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

![Field Type Percent](/files/field-type-percent.png)  


#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

![Field Type Rating](/files/field-type-rating.png)  


#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

![Field Type Read Only](/files/field-type-read-only.png)  


#### Section Break

Section Break is used to divide the form into multiple sections.

![Field Type Section Break](/files/field-type-section-break.png)  


#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field.

![Screenshot 2024-08-28 at 3.01.56 PM](/files/Screenshot 2024-08-28 at 3.01.56 PM.png)  


#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

![Field Type Table MultiSelect](/files/field-type-table-multiselect.png)  


#### Time

This is a Time field where you can define the Time in the field.

![Field Type Time](/files/field-type-time.png)  


#### Duration

You can use the Duration field if you want to define a timespan.

![Field Type Duration](/files/field-type-duration.png)  


If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

![Field Type Duration Options](/files/field-type-duration-options.png)  


This is how the duration field looks after the above changes.

![Field Type Duration](/files/field-type-duration2.png)  

<!-- page: erpnext/erpnext__fifo-and-moving-average.md -->
---
title: "FIFO and Moving Average"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fifo-and-moving-average"
updated: "2026-06-28"
---

# FIFO & Moving Average Valuation Methods

## 1. Overview

ERPNext values stock **perpetually**: every stock movement (receipt, issue, transfer, manufacture) updates the item's quantity *and* its monetary value in real time through the **Stock Ledger**. The **Valuation Method** decides *how the value of each outgoing unit is calculated* and therefore what your remaining inventory is worth and what your Cost of Goods Sold (COGS) becomes.

ERPNext supports three valuation methods:

- **FIFO** (First In, First Out)
- **Moving Average**
- **Standard Cost** *(covered in a separate guide)*

This guide explains **FIFO** and **Moving Average** — how each works, the accounting they produce, their behavior with backdated entries and reposting, and the pros and cons of each so you can choose the right one per item.

> **Where to set it:** Valuation Method can be set per **Item** (Item master → *Valuation Method*), or defaulted at the **Company** level, or globally in **Stock Settings**. The most specific setting wins (Item → Company → Stock Settings).

---

## 2. FIFO (First In, First Out)

### 2.1 How it works

FIFO assumes the **oldest stock is consumed first**. ERPNext maintains a **FIFO queue** of `[quantity, rate]` layers for each item-warehouse. Every receipt adds a layer at its actual incoming rate; every issue consumes layers from the **front** (oldest) of the queue at *their original rates*.

The valuation rate reported at any moment is the **weighted average of the layers currently remaining** in the queue, but each outgoing unit is costed at the *specific* rate of the layer it is drawn from.

### 2.2 Worked example


| Step | Transaction      | Queue after              | Stock value |
| ---- | ---------------- | ------------------------ | ----------- |
| 1    | Receive 10 @ 100 | `[10 @ 100]`             | 1,000       |
| 2    | Receive 10 @ 120 | `[10 @ 100], [10 @ 120]` | 2,200       |
| 3    | Issue 15         | `[5 @ 120]`              | 600         |


At step 3, the 15 issued units are costed as **10 @ 100 + 5 @ 120 = 1,600** (oldest first). The remaining 5 units stay valued at their original 120.

### 2.3 Accounting impact

In a perpetual-inventory company, the issue posts COGS at the **actual layered cost** of the consumed units:

- COGS (step 3) = 1,600
- Inventory is credited 1,600; remaining inventory asset = 600.

Because outgoing cost reflects the **actual historical purchase price** of the specific units leaving stock, FIFO closely tracks real acquisition cost and is widely accepted for statutory/tax reporting.

### 2.4 Pros

- **Closely matches actual cost flow** — the cost of goods sold reflects the genuine price paid for the specific units consumed.
- **Realistic ending inventory value** — remaining stock is valued at the most **recent** purchase prices, so the balance sheet reflects current replacement-ish cost.
- **Widely accepted** for accounting standards and tax authorities; intuitive and auditable (you can trace which layers were consumed).
- **Good for items with shelf life / lot rotation** (food, pharma, perishables) where you physically issue oldest-first anyway.

### 2.5 Cons

- **Sensitive to backdated entries** — inserting or editing a past transaction changes which layers later issues consume, so **every subsequent ledger entry must be recomputed (reposted)**. On long, dense ledgers this reposting is slow and resource-intensive.
- **Volatile COGS in rising-price environments** — older, cheaper layers are expensed first, which can understate COGS and overstate profit during inflation.
- **More computation / storage** — the layer queue must be maintained and serialized for every item-warehouse.
- **Heavier reposting load** when corrections, cancellations, or landed-cost vouchers touch historical entries.

---

## 3. Moving Average

### 3.1 How it works

Moving Average maintains a **single blended average rate** per item-warehouse. On **every receipt**, the average is recomputed:

```
new average = (existing qty × existing avg rate + incoming qty × incoming rate)
              ──────────────────────────────────────────────────────────────
                             existing qty + incoming qty
```

Issues are costed at the **current average rate** and do **not** change the average; only receipts (and revaluations) move it.

### 3.2 Worked example


| Step | Transaction      | Qty on hand | Avg rate | Stock value |
| ---- | ---------------- | ----------- | -------- | ----------- |
| 1    | Receive 10 @ 100 | 10          | 100      | 1,000       |
| 2    | Receive 10 @ 120 | 20          | 110      | 2,200       |
| 3    | Issue 15         | 5           | 110      | 550         |


At step 2 the average becomes `(10×100 + 10×120) / 20 = 110`. The 15 issued units at step 3 are each costed at **110** → COGS = 1,650; remaining 5 units valued at 110 = 550.

### 3.3 Accounting impact

- COGS (step 3) = **1,650** (15 × average 110).
- Inventory credited 1,650; remaining inventory asset = 550.

Compared with FIFO on the same data, Moving Average **smooths** the cost: COGS is 1,650 vs FIFO's 1,600, and the difference flows into the value of remaining stock.

### 3.4 Pros

- **Smooths out price fluctuations** — a single blended rate dampens the impact of volatile purchase prices, giving steadier COGS and margins.
- **Simpler and lighter** — only one rate per item-warehouse to maintain; no layer queue to store or walk.
- **Easier to understand and reconcile** — "one item, one current cost" is intuitive for operations and reporting.
- **Good for homogeneous, fast-moving, commoditized items** where individual lots are indistinguishable (bulk fasteners, fuel, raw chemicals).

### 3.5 Cons

- **Still requires reposting on backdated entries** — because a past receipt changes the running average for **all later** transactions, ERPNext must recompute the forward chain. Like FIFO, this can be slow on long ledgers.
- **Does not track actual lot cost** — outgoing cost is a blend, so it can diverge from the real price paid for the specific units shipped; less precise for lot-traceable or high-value items.
- **Average can lag reality** — in fast-moving price environments the blended rate trails current market cost, which may misstate margins on individual sales.
- **Less granular audit trail** — you cannot point to "these specific units left at this specific cost," only to the average at that time.

---

## 4. FIFO vs Moving Average — at a glance


| Aspect                           | FIFO                                            | Moving Average                               |
| -------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| **Outgoing cost basis**          | Actual rate of the oldest remaining layer       | Current blended average rate                 |
| **Tracks real lot cost?**        | Yes (layer-accurate)                            | No (blended)                                 |
| **COGS behavior**                | Reflects oldest prices first                    | Smoothed across all receipts                 |
| **Ending inventory value**       | At most recent purchase prices                  | At the blended average                       |
| **Data maintained**              | Queue of `[qty, rate]` layers                   | Single average rate                          |
| **Backdated entry → reposting?** | **Yes** (recompute forward chain)               | **Yes** (recompute forward chain)            |
| **Computation cost**             | Higher (layer walking)                          | Lower (single rate)                          |
| **Best for**                     | Perishables, lot-rotated, audit-sensitive items | Homogeneous, high-volume, commoditized items |
| **Statutory acceptance**         | Very widely accepted                            | Widely accepted                              |


---

## 5. The shared limitation: backdated entries trigger reposting

This is the most important operational characteristic both methods share — and the key contrast with **Standard Cost**.

With **both FIFO and Moving Average**, the value of any stock ledger entry depends on **the entries before it** (which layers exist, or what the running average is). So when you:

- insert a **backdated** transaction,
- **cancel** or **amend** a historical voucher,
- apply a **Landed Cost Voucher** to a past receipt, or
- change a past valuation rate,

…ERPNext must **repost** — recompute the quantity, rate, value, and GL impact of **every subsequent stock ledger entry** for that item-warehouse (a *Repost Item Valuation* job). On items with long, dense histories this is **slow, resource-heavy, and temporarily changes the value of stock you considered settled**.

> If your organization frequently records **backdated corrections** and this reposting cost is painful, consider the **Standard Cost** method (see the separate *Standard Valuation Rate* guide), where the rate is known by date and backdated entries do **not** trigger reposting.

---

## 6. Choosing a method — recommendations


| Your situation                                                     | Recommended method                   |
| ------------------------------------------------------------------ | ------------------------------------ |
| Perishable / shelf-life items, physically issued oldest-first      | **FIFO**                             |
| High-value or lot-traceable items needing precise cost             | **FIFO**                             |
| Statutory/tax regime that expects actual cost flow                 | **FIFO**                             |
| Homogeneous, commoditized, fast-moving items                       | **Moving Average**                   |
| You want smoother, more stable margins                             | **Moving Average**                   |
| You want minimal valuation maintenance overhead                    | **Moving Average**                   |
| You frequently post **backdated** entries and reposting hurts      | **Standard Cost** *(separate guide)* |
| You want predictable, fixed product cost & isolated price variance | **Standard Cost** *(separate guide)* |


### Best practices (both methods)

- **Set the method before the item transacts.** Changing an item's valuation method while stock exists is disruptive and may be blocked.
- **Enable perpetual inventory accounts** (warehouse/stock, stock-received-but-not-billed, COGS, stock adjustment) so valuation and GL stay in lock-step.
- **Batch your historical corrections** and run them in low-traffic windows, since they trigger reposting.
- **Use Landed Cost Vouchers promptly** after receipt to avoid large retroactive revaluations later.
- **Reconcile stock value vs. GL** periodically (Stock Ledger / Stock Balance vs. the inventory account) to catch drift early.
- **Be consistent per item category** so reporting and margins are comparable across similar items.

---

## 7. Summary

- **FIFO** costs outgoing stock at the **actual rate of the oldest remaining layer** — precise, audit-friendly, ideal for perishables and lot-traceable goods, but layer-heavy and reposting-sensitive.
- **Moving Average** costs outgoing stock at a **single blended rate** — simple, smooth, ideal for commoditized high-volume items, but less precise and still reposting-sensitive.
- **Both** recompute (repost) the forward ledger when the past changes. If that cost is the deciding factor, the **Standard Cost** method avoids it entirely — see the *Standard Valuation Rate* guide.

<!-- page: erpnext/erpnext__filter-options-in-select-field.md -->
---
title: "Filter Options in Select Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/filter-options-in-select-field"
updated: "2026-03-02"
---

Let's say you have two drop-down fields named State and City. State has two values Karnataka and Maharashtra and City has four values, Bangalore, Mysore, Mumbai, and Pune. If you would like to filter options in City based on the value chosen in State, you can write custom script as shown below.

```
frappe.ui.form.on("Lead", "state", function(frm) {
  if(frm.doc.state == "Karnataka") {
    set_field_options("city", ["Bangalore","Mysore"])
  } else if(frm.doc.state == "Maharashtra") {
    set_field_options("city", ["Mumbai","Pune"])
  } else if(frm.doc.state == "") {
    set_field_options("city", ["","Bangalore","Mysore","Mumbai","Pune"])
  }
});
  

```

![Opening Account](/files/filter_dropdown.gif)



Here’s an example of a custom script that filters options in a Select field within a child table:

```
frappe.ui.form.on('Parent DocType', {
    refresh: function (frm) {
        // Trigger this function when the form is refreshed or reloaded
        frm.fields_dict['child_table_fieldname'].grid.get_field('select_fieldname').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Some Field', '=', 'Some Value'] // Replace with your filter criteria
                ]
            };
        };
    }
});
```

### Example Scenario

Suppose you have a parent DocType called **Sales Order** with a child table field called **items**. The child table has a Select field named **itemcode**, and you want to filter the options to show only items from a specific category.

Here’s how your script might look:

```
frappe.ui.form.on('Sales Order', {
    refresh: function (frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Item Group', '=', 'Specific Category'] // Adjust the filter criteria as needed
                ]
            };
        };
    }
});
  

```
