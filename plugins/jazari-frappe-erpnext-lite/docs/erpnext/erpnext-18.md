<!-- Frappe documentation: erpnext, part 18 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__customise-cash-flow-report.md -->
---
title: "Customise Cash Flow Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customise-cash-flow-report"
updated: "2026-08-14"
---

Nova Industries's default Cash Flow report explains how cash moved through operating, investing, and financing activities. Finance wants a reusable IFRS-style presentation with clearer lines for profit before tax, depreciation, finance costs, receivables, payables, inventory, equipment purchases, and financing.



In the current ERPNext develop version, Nova can create or adapt a [Financial Report Template](/erpnext/financial-report-template) with Report Type set to **Cash Flow**. The template controls report headings, account selection, calculations, indentation, signs, hidden rows, and charts. It changes presentation, not the underlying [General Ledger](/erpnext/general-ledger) entries.

## Before you begin

- Run the standard [Cash Flow Report](/erpnext/cash-flow-report) and reconcile it with the General Ledger.
- Have an accountant approve the required headings, classifications, signs, and calculations.
- Review the [Chart of Accounts](/erpnext/chart-of-accounts) and assign consistent Account Categories where template rows use them.
- Test the template with representative transactions before using it for management or external reporting.

## Review the current report

Run Cash Flow for Nova Industries with a period containing operating, investing, and financing transactions. Save the baseline totals before enabling a custom format.

![Loaded Cash Flow report for Nova Industries before mapping review](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-cash-flow-loaded.png)

## Create or copy a Cash Flow template

1. Open Financial Report Template.
2. Create a template, or copy an existing Cash Flow template when it is a suitable starting point.
3. Set **Report Type** to **Cash Flow**.
4. Enter a clear Template Name and keep the template enabled.

## Build and arrange the report lines

Add rows to **Report Line Items** in the exact order they should appear. Use blank or visual rows for section headings, Account Data rows for ledger-derived values, and Calculated Amount rows for subtotals. Indent supporting lines beneath their section and use stable Line References for formulas.

![Standard Cash Flow Statement IFRS template showing its ordered report line items](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)


| Example line                                    | Typical source      | Presentation                                              |
| ----------------------------------------------- | ------------------- | --------------------------------------------------------- |
| Cash flows from operating activities            | Visual or blank row | Section heading at indent level 0                         |
| Profit before tax                               | Account Data        | Period movement with the appropriate sign                 |
| Depreciation and amortisation                   | Account Data        | Indented non-cash adjustment                              |
| Operating profit before working-capital changes | Calculated Amount   | Formula based on earlier Line References                  |
| Change in trade receivables                     | Account Data        | Working-capital movement with reversed sign when required |


## Verify the custom report

![Cash Flow report after mapping with an account group opened for verification](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-ifrs-output-v2.png)



1. Refresh Cash Flow for the same company and period used for the baseline.
2. Confirm every expected line appears under the correct section.
3. Compare section totals and closing cash with the standard report and General Ledger.
4. Open unusual balances and verify the mapped accounts.
5. Repeat the test for a second period before relying on the format.

## Troubleshooting

### A line is missing

Confirm that the row is enabled, its Account Data filter matches the intended accounts, and the selected period contains relevant ledger activity. Check whether **Hide If Zero** is suppressing the row.

### A value appears twice

Review the template's account coverage for overlap. The same account may be included by more than one Account Data row, or a parent account and its children may both be selected.

### Net cash does not reconcile

Run the template and standard Cash Flow report with identical company, dates, Finance Book, dimensions, currency, and opening-balance options. Then check omitted accounts, duplicated coverage, formulas, Line References, and sign reversal.

## Frequently asked questions

### Does customisation change ledger entries?

The configuration changes how existing balances are classified and displayed. It does not repost transactions.

### Can I add a fourth cash-flow section?

The standard structure uses Operating, Investing, and Financing Activities. Use approved labels and mappings inside those sections unless a current product extension explicitly supports another structure.

### Should parent or child accounts be mapped?

Use an approach that avoids overlap and matches how the account tree is maintained. Parent accounts work best when all children share the same cash-flow treatment.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Accounts Settings](/erpnext/accounts-settings)
- [General Ledger](/erpnext/general-ledger)
- [Financial Report Template](/erpnext/financial-report-template)

<!-- page: erpnext/erpnext__customise-your-items-tables-within-your-print-format-builder.md -->
---
title: "Customize tables within your Print Format Builder"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customise-your-items-tables-within-your-print-format-builder"
updated: "2026-03-02"
---

You can customize the '**Items**' column present your Print Format Builder by navigating as shown below:

  


1. Create your Customized Print Format by going into the '**Settings**' button and clicking on '**Customize**'.
2. Add a relevant name to the new customized Print format you are creating.
3. Once you are inside the New Print Format, you can click on the button '**Select columns**' in the field which says '**Items (Table)**'

  


![](/files/IIunbhn.png)

  


Open the table and you will see a list of columns that are present in the standard format of your Print Format as shown below:

  


![](/files/HCA3S5a.png)

  


  


  


The options you select here will be shown in Print Format.

Select the columns you want to keep in the Table that you are creating for your customized Print Format. You can adjust the Width and their order according to your requirement.

  


![](/files/HEUrHpC.png)

  


Once you have selected the columns you want your Print Format to have, click on '**Update**' and '**Save**' the changes you have made after further modifications in the Print format.

  


Refresh your screen and select the newly created Print Format. In this case, it is the 'Purchase Receipt'.

![](/files/nwQT6g6.png)

  


Once you click on the Print Format you newly created, the changes will be visible in the Items table.

  


![](/files/Bsp6PRj.png)

  


  


  


To see the difference between the **Standard** **Print** **Format** and the one you just created, you can simply click on the Print format Templates present.

<!-- page: erpnext/erpnext__customize-form.md -->
---
title: "Customize Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customize-form"
updated: "2026-02-27"
---

**Customize Form is a tool which enables you to make changes to a Form Type or a Document Type (DocType) on the front-end.**

It allows you to insert [Custom Fields](/erpnext/custom-field) as per your requirement or customize the properties of standard fields.

Before we venture to learn the Form Customization tool, [click here](/erpnext/doctype) to understand the architecture of forms in ERPNext. It will help you in using the Customize Form tool more efficiently.

To access Customize Form, go to:


> Home > Customization > Form Customization > Customize Form
> 
> 

You can also go to the list view of any DocType and select Customize from the Menu options.

![Customize Option in List View](/files/customize-option-in-list-view.png)  


1. How to Customize a Form
--------------------------

1. Click on Customize Form.
2. You will be redirected to a page wherein you will be asked to Enter Form Type.
3. Once you enter the Form Type in this field, the page further expands and you will be able to see multiple features.

![Select DocType in Customize Form](/files/customize-erpnext-custom-field-from-customize-form.gif)

### 1.1. Options While Customizing a Form

1. **Change Label**: This field gets fetched via Custom Translation. You can change the name of the field to suit your industry/language. E.g., if you are a services business and you want to change the Label from 'Customer' to 'Consumer', the same can be done via [Custom Translation](/erpnext/custom-translations) and the same shall be reflected here.

![Change Label](/files/customize-customize-form-label.png)

2. **Title Field**: This field can be used to generate the title while viewing the lists. Any "Data" type field can be set as the Title Field while viewing the forms in the list view. E.g., if you wish to view the list of all your employees with the Title field as the 'Employee Code' instead of Employee Name, the same can be configured here. Check our article on [Document title](/erpnext/document-title) for more information.

*Learn more about field types* [*here*](/erpnext/field-types.html)*.*

3. **Default Print Format**: For a single DocType, there could be multiple Print Formats. Here you can select the default Print Format for the selected DocType. For e.g., a company may have different Letter Heads for different purposes which can be configured through Print Formats. However, you can select two different Default Print Formats for a Sales Order and an Appointment Letter. Check [Custom Print Formats](/erpnext/print-format) for more information.

4. **Image Field**: You can select an "Attach Image" Field for your Image Field. This becomes the Image representing that particular DocType. E.g., the 'Image Field' for an Employee could be their photograph or a snapshot of their ID cards; the same can be configured here.

![Image Field in DocType](/files/customize-form-image-field.png)

5. **Max Attachments**: You can enter the maximum number of attachments that could be added to this DocType.

6. **Search Fields**: While creating any DocType, you may want to link a particular field to another DocType. For ease in selection, you can also ensure that you are able to see the value of another field of the latter DocType in the search result. For more information [click here](/erpnext/search-record-by-specific-field).

7. **Sort Field**: Records in any DocType List are generated based on the Field that you set at the Sort Field over here. E.g., for Items, if you want your list to be generated as per Item Name, you can configure the same here.

![Sort Field](/files/customize-sort-field.png)

8. **Sort Order**: You can select whether you want the Sorting to be done in Ascending Order or Descending Order. To get more understanding on Sort Field and Sort Order, check out [Customizing Sorting Order in the List View](/erpnext/customizing-sorting-order-in-the-list-view).

9. **Default Email Template**: For a single DocType, there could be multiple [Email Templates](/erpnext/email-template). Here you can set the default Email Template for the selected DocType. For example, you can set a different Default Email Template for a Sales Order and an Appointment Letter.

### 1.2. More Properties

* **Hide Copy**: This box, when checked, restricts a User to create a 'Copy' of a particular Form.

* **Is Table**: This option is available only while customizing the Forms which are present in table forms in the system. For e.g., if you are creating an Item Table to be added into a Custom Form, you can enable this option. Check out [Child Table](/erpnext/customizing-data-visibility-in-child-table) for more information.

* **Quick Entry**: Checking this box will allow you to create a 'Quick Entry' using a particular form. This means that whenever a user is creating this Form from another existing Form, a box will Pop Up which will allow the user to create the DocType by entering only the basic details. For example, check Quick Entry in [Journal Entry](/erpnext/journal-entry#11-quick-entry).

* **Track Changes**: Checking this box will ensure that any changes made by any of the users to this DocType will be tracked and displayed.

![Track Changes](/files/customize-track-changes.png)

* **Track Views**: This option will give you a trail of all the views towards this particular DocType.

* **Allow Auto-Repeat**: This option, if checked, will allow you to enable Auto Repetition of a DocType periodically. E.g., if there is a Sales Order which has to be made multiple number of times, you can enable this option and then [Set Up Auto Repeat](/erpnext/auto-repeat) for any particular Sales Order.

* **Allow Import**: This option will allow the user to Import data from any files. Check out [Data Import Tool](/erpnext/data-import) for more information.

* **Show Preview Popup**: This option was introduced in Version 12. If checked, a small popup will appear on hover of links of this document type (in list view and other link fields). This popup will contain the mandatory fields of the document and the fields for which `in_preview` is checked. Check out [Link Preview](https://erpnext.com/version-12/release-notes/features#link-preview) for more information.

Once you click Update, your Customizations will be updated to the Form.

### 1.3. Customizing the Fields

Every form in ERPNext has a standard set of fields. If you need to capture some information, but there is no standard field available for it, you can insert Custom Field in a form as per your requirement. Adding, editing or deleting of Fields can also be done here. You can also place the fields as per your requirement in the form by adding it below or above any other already present fields. [Click here](/erpnext/custom-field) for more information on Custom Fields.

### 1.4. Trim Table, Reset Layout, and Reset All Customizations

![](/files/UcB4Lpm.png)  


* **Trim Table**: To remove unused database columns (fields) that are no longer needed by a doctype. It checks for fields that have been deleted from the form but still exist in the database. If such fields are found, it allows you to permanently delete these columns. This helps keep the database clean and improves performance by removing unnecessary data.
* **Reset Layout:** To revert the form layout to its original, default state. It removes any layout customizations you have made, such as rearranging fields or changing sections, and restores the layout to how it was initially defined by the system. It is useful if your custom layout becomes too complicated or problematic, and you want to start fresh with the standard layout.
* **Reset All Customizations**: To remove all customizations made to a form, including added fields, changes to existing fields, and layout modifications. It completely removes all the custom changes you have applied to the form, resetting it to its default configuration as defined by the system. This is a drastic measure but helpful if you need to return to the system’s default form setup, perhaps because your customizations have caused issues or you want to reconfigure the form from scratch.

2. Videos
---------

<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/WSzkpPm3iIU" width="560">
</iframe>

<!-- page: erpnext/erpnext__customizing-data-visibility-in-child-table.md -->
---
title: "Data Visibility in Child Tables"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-data-visibility-in-child-table"
updated: "2026-03-04"
---


In ERPNext, there is a feature called the editable grid. This allows the user to add values in the child table without opening a dialog box/form for each row.

This is how the Quotation Item table renders value when the Editable Grid is enabled. It will have a maximum of four columns in the table.

![Child Table](/files/customize-child-table-5.png)

As per the default setting, only four columns are listed in the child table. Following is how you can add more columns in the Editable Grid itself.

For the field to be added as a column in the table, enter a value in the Column field. Also, ensure that the "Is List View" property is checked for that field.

![Child Table](/files/customize-child-table-2.png)

Based on the value in the Column field, columns will be added to the child table. Ensure that the total value added in the Column field doesn't exceed 10. Based on the Column value, the width for that column will be set.

![Child Table](/files/customize-child-table-3.png)

**Switch to Un-editable Grid**

To have more values shown in the preview of the Quotation Item table, you can disable Editable Grid for the Quotation Item DocType. Steps below.

![Child Table](/files/customize-child-table.gif)

Once Editable Grid is disabled for the Quotation Item, the values will be rendered in a preview of the Quotation Item table in the following way:

![Child Table](/files/customize-child-table-4.png)

To have a specific field's value shown in the preview, ensure that for that field, in the Customize Form tool, "In List View" property is checked.

![Child Table](/files/customize-child-table-1.png)

<!-- page: erpnext/erpnext__customizing-module-visibility.md -->
---
title: "Customizing Module Visibility\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-module-visibility"
updated: "2026-03-04"
---


**ERPNext as a system can be used by multiple businesses at every scale, Manufacturing, Education, Retail being some of the businesses benefitted the most from the usability of the system.**

Keeping in mind, the interests of all kinds of business owners, the usability of the system for different business has been mapped into different 'Modules' represented as 'Cards' in the system. Similarly the core modules in the system, such as Human Resource, Accounting, CRM etc. are also represented by different cards on the dashboard.

Every ERPNext account holder has the option of customizing the visibility of the different modules based on their business case.

*In Version 12, you can go to Show / Hide Modules on the top right corner of the home screen for checking visibility of modules.**

![Module Visibility](/files/customize-module-visibility-2.png)
![Module Visibility](/files/customize-module-visibility.gif)

> Note: Modules are automatically hidden for users that have no permissions on the documents within that module. For example, if a User has no permissions on Purchase Order, Purchase Request, Supplier, the “Buying” module will automatically hidden for that User.

If you have permissions to a specific module, but it is still not visible, the following could be the possible reasons for it.

Let's consider a scenario that a user has the permission for the Website module, but is not able to access it.

As a basic requirement, ensure that the "Website Manager" role is assigned to that user. It is a standard Role that grants permission on the Website module. If permissions have been customized in your account, check Role Permission Manager to know which Role has permission on Website, and then check if the same Role is assigned to the User.

![Module Visibility](/files/customize-module-visibility-4.png)

Further, you should also check if the under the settings, 'Allow Modules', the required module has been enabled for the user

![Module Visibility](/files/customize-module-visibility-1.png)

Reload tab of your ERPNext account and the changes made will be applied and will be visible in the system.

<!-- page: erpnext/erpnext__customizing-sorting-order-in-the-list-view.md -->
---
title: "Sorting Order in List View"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/customizing-sorting-order-in-the-list-view"
updated: "2026-03-04"
---


**Question:** I want records in my Item List sorted based on Descending Order of Item Code.

**Answers:** Following are the steps to customize Sort Order for the Item master. These steps will be applicable for customizing Sort Order for the other documents as well.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Select DocType

Select document type for which Sort Order is to be customized.

![Sort Order field](/files/customize-sorting-order-2.png)

#### Step 3: Update Sort Details

In the Customize Form, you will find these fields.

![Sort Order Field](/files/customize-sort-field.png)
![Sort Order field](/files/customize-sorting-order-1.png)

1. Sort Field: Select the Field based on which sorting will be done. It will be "Item_Code" field in the scenario.
2. Sort Order: Sort Order will be two possible options, **Asc** for ascending, and **Desc** for descending.

<!-- page: erpnext/erpnext__daily-depreciation.md -->
---
title: "Daily Depreciation Calculation | ERPNext Documentation"
description: "Configure daily pro-rata depreciation in ERPNext and understand how actual days affect each period."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/daily-depreciation"
updated: "2026-08-15"
---

Imagine Nova Industries starts using a machine on 20 March. A monthly depreciation calculation may treat March like a full month, even though the machine was used for only 12 days. That small difference can matter when assets are added or sold throughout the year.



Daily Depreciation calculates the expense using the actual number of days the asset was available for use. It gives the accountant a more precise schedule when company policy requires depreciation to follow calendar days.

## Enable daily pro-rata calculation

Open the relevant Asset Category or Asset Finance Book row, enable **Daily Pro Rata Based**, and confirm the depreciation start date. ERPNext then uses actual day counts instead of equal periodic amounts.

![Finance Book settings used for daily depreciation](https://novacompanies.m.frappe.cloud/files/09-production-asset-depreciation.png)

## How the amount is determined

ERPNext calculates the daily amount from the depreciable value and schedule duration, then multiplies it by the eligible days in each period. Leap years and unequal month lengths can make individual rows differ while the total still reconciles.

## Verify the schedule

Check the first and last rows, the total depreciation, and the expected value after useful life. The Asset Depreciations and Balances report should reconcile the opening value, booked depreciation, and closing value.

![Asset Depreciations and Balances report](https://novacompanies.m.frappe.cloud/files/23-asset-depreciations-balances-v2.png)

## Troubleshooting

### The first period is smaller than expected

Check the Available for Use Date and depreciation start date. A partial first period is normal with daily proration.

### The daily amounts do not match a simple monthly division

Daily calculation follows actual days, so months and leap years do not always carry equal depreciation.

## Frequently asked questions

### Is daily pro-rata mandatory?

In ERPNext, no. Use it only when the accounting policy requires actual-day allocation.

### Does it change the total depreciable value?

In ERPNext, no. It changes timing across rows, not the total value to be depreciated.

### Can different Finance Books use different pro-rata settings?

In ERPNext, yes. Configure the setting independently in each Finance Book row.

## Related topics

- [Asset Category](https://docs.frappe.io/erpnext/asset-category)
- [Asset Location](https://docs.frappe.io/erpnext/asset-location)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Purchasing an Asset](https://docs.frappe.io/erpnext/purchasing-an-asset)
- [Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Asset Movement](https://docs.frappe.io/erpnext/asset-movement)
- [Asset Repair](https://docs.frappe.io/erpnext/asset-repair)
- [Asset Reports](https://docs.frappe.io/erpnext/asset-reports)

<!-- page: erpnext/erpnext__data-export.md -->
---
title: "Data Export"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-export"
updated: "2026-03-02"
---

**'Data Export' helps you extract data from any DocTypes to a CSV or an Excel format.**

To access Data Export, go here.

> Home > Data Export

### How to Use Data Export

1. Go to the 'Data Export' DocType.
2. Select the DocType from which the data is to be extracted.
3. Select the file format whether CSV or Excel.
4. Tick the checkbox if you want to export the data without any header notes and column descriptions.
5. Select the fields to export; the red ones are mandatory.
6. You can also add filters to select only specific data. For example, 'Territory = Asia' will export all Customers whose Territory is set as 'Asia'.
7. Click on Export to download the file.

![](/files/image9dfe7c.png)

After exporting data, you can use the same file to import data using [Data Import](/erpnext/data-import).

<!-- page: erpnext/erpnext__data-import.md -->
---
title: "Data Import"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-import"
updated: "2026-04-27"
---

**The Data Import tool in ERPNext allows users to import records into the system using CSV or Excel files.** 

It provides a convenient way to upload or update large volumes of data at once, especially master data, without the need for manual entry.



This tool is commonly used during initial system setup, data migration, or when bulk updates are required. By using the Data Import tool, users can ensure faster data entry while maintaining consistency across records.



To access the Data Import tool, navigate to:

> Home > Data

‎ Or go to the Document you want to import and click on Menu > Import



Before starting the import process, make sure that all required data is prepared correctly and follows the expected format. The Data Import tool supports two main operations:

## Inserting New Records

The Data Import Tool in ERPNext allows users to upload bulk records into the system using a predefined template. This document outlines the step-by-step process for importing new records.

![](https://docs.frappe.io/files/imagebfd4b7.png)

1. Navigate to Data Import
2. Select the Document Type and the Import Type as *Insert New Records*.
3. Click on Save and then download the template.

### Download Template

We have an option to download the template to insert the records/update the records

1. Clicking on Download Template opens a dialog box

![](/files/image79c0b4.png)
*Download Template Dialog box*

> While inserting new records, the template should be blank. If you have a few records in your system, you can select Export Type as "5 Records" to see the format in which you have to enter the data in the template.

4. *After you choose the export type, every field appears in the list. **Mandatory** fields show a red * next to the name. **Conditional** fields (for example **Depends On** or autoname-related) show a small **info** icon—point at it to read the note.*
5. *Fields that are ticked but not mandatory are ones with **Include in Import Template** on—set on the **DocType** or in **Customize Form**—so they show in the list by default without being required.*
6. Click Export and get the exported file.
7. Now, save your template as an Excel or Comma-Separated Values (CSV) file.

> *You can leave the ID column as blank while inserting new records.* When you import this template, each row will make a record in the system.

8. Once the template is updated and ready with the data, we can import it.

### Importing a Template

Once the data has been added to the downloaded template, the following steps are followed:

1. After updating your template file, go back to the Data Import form and attach the file by clicking on the **Attach** button.
  ![](/files/imagef9ce89.png)
  *Attaching file for import*
2. Select the template file and click on **Upload**, after the upload is successful, click on **Start Import**. There are various ways to import the data; you can refer [here](https://docs.frappe.io/erpnext/data-import#ways-to-import-data)
3. Once the Sheet is uploaded, the system validates the sheet and gives the result on screen before importing the data
  ![](/files/image799c07.png)
4. If there are any errors in your template, they will be shown in the Warnings section. The warnings will be categorized by Row or Column with their number so that you can easily track them down in the template and resolve them. You must resolve all the warnings before you can import the data.
5. After you have resolved the warnings, click on **Start Import** again to import the data. On successful import of the data, you'll see a log of each record that was created in the Import Log section.

## Validations and Errors in Importing

### Duplicate Name

In case we try to add a record with a duplicate name, it will throw an error like this

![](/files/imagebff69b.png)
*Duplicate Name Error*

### Mapping of missed columns

When we add additional columns while downloading the template, or we have renamed a column in the template we are importing, it may throw an error about not being able to match the columns. 



![](/files/Screen Recording 2026-02-18 at 9.43.24 PM.mov)



















> To resolve this, we can click on the **map columns** and manually map the columns to the corresponding columns in the Document. 

## Importing child records

Data in ERPNext is stored in tables like a spreadsheet with columns and rows of data. Each form likes Sales Order, has multiple fields like Customer, Company, etc. It also has tables like the item table, tax table, etc. In Data Import, the set of fields in the Sales Order is treated as the main table, and the rows inside the child table (item table) are treated as the child table for data import.



Each form in ERPNext can have multiple child tables associated with it. The child tables are linked to the parent tables and are implemented where there are multiple values for any property. For example, an Item can have multiple prices, a Sales Invoice has multiple Items, Taxes, and so on.



When you export a document with child tables, for e.g., each child row will appear on a separate row, but it is associated with a single parent row. The subsequent values in the parent columns will remain blank. You must ensure that this order is not broken when you are importing it via Data Import.

---

![](/files/imagedf8b35.png)
*Child records importing*

## Updating Records

Let's say you want to update Customer data in bulk in your system. The first step is to download the template with the data.

1. We start by downloading the template. While doing this, since we want to update, we can use filters to extract the exact records and import them back for updating.
2. First, we select the document type and the import type as **Update Existing Records,** and Save
3. When we try to download the template, we can apply filters, something like this
  ![](/files/image0baff8.png)
4. We click on **Export.**
5. Now, based on the template, the existing records look like this:

![](/files/image7a4518.png)

:::tip
While exporting records for updating them, ensure that the ID column is exported and is untouched. The values in the ID column are used to identify the records in the system. You can update the values in other columns but not in the ID column. If you remove some child table row, the system will consider that the row is supposed to be deleted.
:::

















6. Now, change the values in your template and save the file as Excel or CSV.

![](/files/imageebf859.png)

## Ways to Import Data

### Import from Google Sheets

You can import data directly from Google Sheets by following these steps:

1. Upload or copy your template into Google Sheets.
2. Enter or update your data in the sheet.
3. Ensure the Google Sheet is set to **Public** access.
4. Once confirmed, use the Google Sheets link in the Data Import page to proceed with the import.

![](/files/imaged49cb3.png)
*Google sheet Data File*

:::tip
To verify that the sheet is publicly accessible, open the Google Sheets URL in an incognito/private browser window. If the file opens without requiring login access, it is correctly configured.
:::















![](/files/imagebbb644.png)
*Post Import using google sheets*

### Import from the file system

1. On the **Data Import Page**, there are two available options:
  - Attach File
  - Import Using Google Sheets
    ![](/files/imageb8e55f.png)
2. After clicking **Attach**, you will see multiple upload options:
  ![](/files/imageb4e113.png)
3. Available Upload Options

- **My Device**  
Upload a file directly from your local computer.
- **Library**  
Select a file that has already been uploaded and stored in the system’s file library.
- **Link**  
Provide a direct web URL to a file hosted online.

4. Choose the appropriate option based on where your file is stored, then proceed with the upload.

### Submit After Import

In ERPNext document types are mainly of two types - masters and transactions. The masters are records like Customer and Task which can only be saved not submitted. Transactions like Sales Orders, Purchase Invoices are submittable documents and can be submitted.

When you select a submittable document type for Import, you can tick **Submit After Import** to submit the document after it is imported.

### Don't Send Emails

Let's say you have created a Notification in your system and whenever a Lead is created an email is sent. Now, if you are bulk importing Leads then a lot of emails will be sent, which may not be desired. You can disable this option to avoid sending emails.

## Additional Notes

---

### Upload Limit

There is no hard limit on the number of records that can be imported. But you must try and upload only a few thousand records at a time. Importing a large number of records (let's say 50,000) might slow down the system considerably for the users that are using the system.

### CSV Files

A CSV (Comma Separated Value) file is a data file that you can upload into ERPNext to update various data. Any spreadsheet file from popular spreadsheet applications like MS Excel or Open Office Spreadsheet can be saved as a CSV file.

If you are using Microsoft Excel and using non-English characters, make sure to save your file encoded as UTF-8.

For older versions of Excel, there is no clear way of saving as UTF-8. So save your file as CSV, then open it in Notepad, then save as “UTF-8”. (Or upgrade your Excel!)

<!-- page: erpnext/erpnext__data-management__introduction.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/data-management/introduction"
updated: "2026-02-23"
---

Data management is essential for effectively using an ERP system. ERP software integrates data from different business functions, such as finance, inventory, sales, and human resources, into a single system. For the system to work reliably, the data must be accurate, consistent, and properly maintained.



In this tutorial, we will learn how users can import data into ERPNext from different sources (like spreadsheet), and ways to export data out of ERPNext.

<!-- page: erpnext/erpnext__datev-integration.md -->
---
title: "DATEV Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/datev-integration"
updated: "2026-07-04"
---

## Overview

The DATEV Integration app connects ERPNext with DATEV workflows used by German accounting teams and tax consultants. The app is listed on Frappe Cloud Marketplace as [DATEV Integration](https://cloud.frappe.io/marketplace/apps/erpnext_datev) and is published by ALYF GmbH, Raffael's team.

## What It Does

- **DATEV Unternehmen Online:** Sends submitted vouchers to DATEV Unternehmen Online by email. Outgoing vouchers can be converted to PDF, while incoming vouchers can send attached files.
- **DATEV CSV Export:** Exports raw General Ledger entries from ERPNext in DATEV CSV format.
- **Tax consultant handoff:** Exports the DATEV report with master data as a ZIP file for import into the tax consultant's DATEV system.

## Setup Summary

Configure DATEV Settings with the client number, tax consultant number, and temporary contra account. For DATEV Unternehmen Online, enable the integration, choose the sending email account, select the voucher type, add the target email address from DATEV, and choose whether to send attachments or generated prints.

## Compatibility

The marketplace listing shows support for ERPNext versions 13, 14, 15, and 16. Test the integration on a staging site before using it for accounting handoff.

## Links

- [DATEV Integration on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/erpnext_datev)

## Disclaimer

DATEV and DATEV Unternehmen Online are trademarks of DATEV eG. The marketplace listing notes that this integration is not approved or endorsed by DATEV eG.

<!-- page: erpnext/erpnext__debit-note-for-price-adjustment.md -->
---
title: "Debit Note for Price Adjustment | ERPNext Documentation"
description: "Reduce a submitted ERPNext Purchase Invoice when a Supplier lowers the agreed price without returning goods."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/debit-note-for-price-adjustment"
updated: "2026-08-14"
---

Apex Components, a supplier to Nova Industries, invoiced 10 phones at $520 each. After the Purchase Invoice was submitted, both companies agreed that the correct price was $500 each. No phones are being returned, but Nova Industries should owe the supplier $200 less.



A Debit Note for price adjustment records only that value correction. It reduces the payable and adjusts the relevant expense or asset value without creating a stock return.



Use this workflow when a supplier reduces an agreed price after invoicing and the physical quantity remains unchanged.



## Before you begin

Confirm the revised price with the Supplier and calculate the reduction per unit.

Example:

- original invoice: 10 phones at $520 each;
- revised price: $500 each;
- price reduction: $20 per phone;
- total Debit Note: $200.

The quantity of goods owned by the Company does not change. Therefore, do not select **Update Stock** for this adjustment.

## Create a Debit Note for price adjustment

1. Open the submitted Purchase Invoice.
2. Select **Create &gt; Return / Debit Note**.
3. Confirm that **Is Return (Debit Note)** is selected and **Return Against Purchase Invoice** references the original invoice.

![Price adjustment Debit Note linked to the original Purchase Invoice](https://novacompanies.m.frappe.cloud/files/purchase-payables-08-rate-adjustment-setting.png)

4. Remove Items that are not part of the price correction.
5. Open the affected Item row using its pencil icon.
6. Enter the full original billed quantity as a negative quantity. For the example, enter `-10`.

![Full original quantity entered as a negative quantity](https://novacompanies.m.frappe.cloud/files/purchase-payables-09-rate-adjustment-full-quantity.png)

7. Enter only the price reduction per unit in **Rate**, not the revised unit price. For the example, enter `$20`, which produces an amount of `-$200`.

![Per-unit price difference entered as the Debit Note rate](https://novacompanies.m.frappe.cloud/files/purchase-payables-10-rate-adjustment-difference.png)

8. Leave **Update Stock** clear because the goods are not being returned.
9. Review taxes. Adjust them only when the Supplier's credit document and applicable tax rules require it.
10. Save and submit the Debit Note.

## Why the full quantity and difference rate are used

The Debit Note amount is calculated as quantity multiplied by rate. Using the full affected quantity and only the reduction per unit produces the exact credit:

`10 units × $20 reduction = $200`

Because the quantity is negative on a return Purchase Invoice, the document reduces the payable by $200. It does not mean that ten units were physically returned, provided **Update Stock** remains clear.

Do not enter the revised price of $500 as the Debit Note rate. That would reduce the invoice by $5,000 instead of the intended $200.

## Important fields and what they mean


| Field                           | What it controls                                                        |
| ------------------------------- | ----------------------------------------------------------------------- |
| Is Return (Debit Note)          | Makes the Purchase Invoice a reducing document.                         |
| Return Against Purchase Invoice | Connects the adjustment to the original Supplier invoice.               |
| Accepted Qty                    | Use the negative full quantity affected by the price change.            |
| Rate                            | Enter the reduction per unit, not the original or revised unit price.   |
| Amount                          | The total reduction. Verify it against the Supplier's credit document.  |
| Update Stock                    | Keep this clear for a price-only adjustment.                            |
| Posting Date                    | Determines the accounting period in which the adjustment is recognized. |
| Taxes and Charges               | Reverses applicable tax amounts when included in the adjustment.        |


## Submit and verify

After submission, check:

- the Debit Note total equals the Supplier's agreed credit;
- the original Purchase Invoice outstanding amount is reduced correctly;
- Item stock quantity is unchanged;
- the Supplier balance in [Accounts Payable](/erpnext/accounts-payable) reflects the adjustment;
- the General Ledger shows the intended reduction in payable and expense, asset, or receipt-clearing value.

If the original invoice has already been paid, the Debit Note creates a Supplier credit. Allocate it to a future invoice through [Payment Reconciliation](/erpnext/payment-reconciliation), or record the Supplier refund using the correct payment workflow.

## Troubleshooting

### The Debit Note amount is too large

The revised price may have been entered instead of the price difference. Calculate `original price - revised price` and use that amount as the Rate.

### Stock quantity changed

The Debit Note was submitted with **Update Stock** selected. Review whether cancellation and amendment are allowed in the posting period, then correct the document using your approved process.

### The original invoice still shows the wrong outstanding amount

Verify the **Return Against Purchase Invoice** reference and review existing payments and reconciliations. Use the invoice and Debit Note Payment Ledger entries to trace the balance.

### Only some units received the price reduction

Use the negative number of affected units, not the full invoice quantity. For example, if only four of ten units receive a $20 reduction, enter quantity `-4` and rate `$20`.

## Frequently asked questions

### Is this the same as returning goods?

It is different. A price adjustment changes the payable but keeps stock unchanged. A physical return also reverses the relevant stock movement.

### Can I cancel and amend the original Purchase Invoice instead?

Only when your permissions, posting period, audit policy, and linked documents allow it. A Debit Note usually provides the clearer audit trail after the original invoice has been accepted or posted.

### What document should I request from the Supplier?

Retain the Supplier's credit note, revised invoice, or other approved evidence that explains the price reduction and tax treatment.

## Related topics

- [Purchase Invoice](/erpnext/purchase-invoice)
- [Debit Note](/erpnext/debit-note)
- [Accounts Payable](/erpnext/accounts-payable)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
