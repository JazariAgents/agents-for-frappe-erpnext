<!-- Frappe documentation: erpnext, part 51 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__request-for-quotation.md -->
---
title: "Request for Quotation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/request-for-quotation"
updated: "2026-02-27"
---

**A Request for Quotation is a document that an organization sends to one or more suppliers asking a quotation for items.**

[Screenshot on the live page: Buying Flow]  


To access **Request for Quotation**, open the "Buying" workspace and, under "Reports & Masters" > "Buying", click on "Request for Quotation".

1. Prerequisites
----------------

Before creating and using a **Request for Quotation**, it is advised that you create the following first:

* [Supplier](/erpnext/supplier)
* [Item](/erpnext/item)

2. How to create a Request For Quotation
----------------------------------------

1. Go to the **Request For Quotation** list and click on "+ Add Request for Quotation".
2. Enter the *Required Date*, by which you'll need the requested materials.
3. Fill the "Suppliers" list with possible suppliers.  
If you set a *Contact* and *Email Id*, that can later be used for sending the **Request For Quotation** via email and grant access to the supplier portal.
4. In the next table, enter the required items along with UOM and quantity, as well as the target warehouse.
5. The *Warehouse* can be left blank if *Maintain Stock* is not enabled for the item.
6. If you want to send the **Request for Quotation** to your suppliers as an email, you can create an **Email Template** and select it here. In the template, you can use special variables for supplier specific data:  
  



	1. `{{ update_password_link }}`: A link where your supplier can set a new password to log into your portal.
	2. `{{ portal_link }}`: A link to this RFQ in your supplier portal.
	3. `{{ supplier_name }}`: The company name of your supplier.
	4. `{{ contact.salutation }} {{ contact.last_name }}`: The contact person of your supplier.
	5. `{{ user_fullname }}`: Your full name.  
	  
	Apart from these, you can access all values in this RFQ, like `{{ message_for_supplier }}` or `{{ terms }}`.
7. You can check how the email will look for a specific supplier by using the "Preview Email" button.

[Screenshot on the live page: Preview Email]
8. If you want to send further attachments to your suppliers, you can enable the checkbox   
*Send Attached Files*. This will add each file attached to the **Request for Quotation** as an attachment to each supplier email.
9. Once you're done, save the **Request for Quotation** as a draft.
10. When you're ready, you can submit the **Request for Quotation**. This will trigger an email to each supplier that has *Send Email* enabled.

[Screenshot on the live page: Create RFQ]  


A Request for Quotation (RFQ) can also be created from a submitted Material Request. Once an RFQ is created, you can print and send suppliers the PDF which will have all the details you entered relevant to the RFQ. You can also get their reply (Supplier Quotation) in ERPNext itself, see section [4.1 Supplier Quotation by User](#41-supplier-quotation-by-user). However, for a large number of items, your supplier may be more comfortable with an Excel sheet, etc.

3. Features
-----------

### 3.1 Get items from

The items in the items table can be fetched from other documents. The options are: Material Request, Opportunity, and Possible Supplier.

* **Material Request**: Items will be fetched from a submitted Material Request that you select. A Material Request can be searched with some matching words and a date range can also be selected to filter the Material Requests.
* **Opportunity**: Items will be fetched from a saved Opportunity. A date range can be selected here also.
* **Possible Supplier**: Select a possible supplier. Then if you have any submitted Material Requests against this supplier, items can be fetched from that.

[Screenshot on the live page: RFQ get items]  


### 3.2 Get Suppliers

Instead of entering the suppliers manually in the table, you can also fetch them using the 'Get Suppliers' button. When you click on **Tools > Get Suppliers**, you will see the field 'Get Suppliers By'. There are two options to fetch suppliers: By Tag or By Group.

* **By tag**: Go to 'Tag Category' via searching from the search bar. You must have created tags here first and assigned them to a Supplier in the Buying module. Then you can select 'By Tag'. On clicking Add 'All Suppliers', suppliers with matching tags will be fetched.
* **By Group**: Select 'Supplier Group' and choose the supplier group from which suppliers need to be added. For example, if you select Hardware, all your hardware suppliers will be added so that you can get a quote from all of them.

[Screenshot on the live page: RFQ get suppliers]  


In the Supplier table, on expanding a row with the inverted triangle, you'll see an option 'Download PDF' which will open a PDF of the RFQ.

### 3.3 Link to Material Requests:

When you click on **Tools > Link to Material Requests**, it links the Request for Quotation to available Material Requests. The items should be the same in the Request for Quotation and the Material Request.

[Screenshot on the live page: Link to Material Request]  


Now, when the Request for Quotation is saved, you can see in the Dashboard that it is linked to the Material Request. If there are multiple Material Requests with the same items, then the link will be created with the newest Material Request.

### 3.5 Terms and Conditions

In Sales/Purchase transactions, there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/erpnext/terms-and-conditions)

### 3.6 Print Settings

#### Letterhead

You can print your request for quotation/purchase order on your company's letterhead. Know more [here](/erpnext/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when you print it.

#### Print Headings

Titles of your documents can be changed. Know more [here](/erpnext/print-headings).

#### Special properties

When printing a RFQ via the "Tools > Download PDF" button, you are asked select the specific supplier you want to address. In the **Print Format** for RFQ, this information can be accessed via special properties:

* `{{ doc.vendor }}` holds the selected supplier ID.
* `{{ doc.items[i].supplier_part_no }}` holds the *Supplier Part Number* of a requested line item.

The data of the first supplier will be used while rendering the standard print preview. If you want to print for a different supplier, please use the "Tools > Download PDF" button.

4. Creating a Supplier Quotation after RFQ
------------------------------------------

After creation of Request for Quotation, there are two ways to generate Supplier Quotation from Request for Quotation.

### 4.1 Supplier Quotation by User

1. Open Request for Quotation and click on **Supplier Quotation > Create**.

[Screenshot on the live page: Supplier Quotation from RFQ]
2. Select the Supplier, click on the supplier again. In this page, click on the + next to 'Supplier Quotation'. A new Supplier Quotation page will be opened, user has to enter the quantity, rate and submit it.

[Screenshot on the live page: Supplier Quotation from Supplier]

### 4.2 Supplier Quotation from Supplier

1. If a [Contact](/erpnext/contact) is created for the Supplier and an email address is associated with the Contact, the Contact details and the email address will be fetched on selecting the Supplier. Create a Contact and email address if not present already.
2. Click on **Tools > Send Emails to Suppliers**.

**If the Supplier's account is not present**: The system will create the Supplier's account and send details to the Supplier. The Supplier will need to click on the link (Password Update) present in the email. After the password update, the Supplier can access their portal with the 'Request for Quotation' form. The Supplier will be created as a Website User.

[Screenshot on the live page: Supplier email if account not present]  


**If Supplier's account is present**: The system will send a Request for Quotation link to the Supplier. The Supplier must log in using his credentials to view the Request for Quotation form on the portal.

[Screenshot on the live page: Supplier email if account present]
3. Either way, when the Supplier logs in, the following screen will be shown to them. From here they can send you a quotation:

[Screenshot on the live page: Supplier Quotation Screen]  


The Supplier has to enter the amount and notes (payment terms) on the form and click on Submit. In the Quotations section, previous quotations will be visible.
4. On submission, ERPNext will create a Supplier Quotation (draft mode) against the Supplier. The user has to review the Supplier Quotation and submit it. When all the items from the Request for Quotation have been quoted by a Supplier, the quote status is updated to 'Received' in the 'Suppliers' table of the Request for Quotation.

[Screenshot on the live page: RFQ status after supplier quote]

Read [Supplier Quotation](/erpnext/supplier-quotation) to know more.

5. Video
--------

### 6. Related Topics

1. [Purchase Order](/erpnext/purchase-order)
2. [Supplier](/erpnext/supplier)
3. [Supplier Quotation](/erpnext/supplier-quotation)
4. [Quotation](/erpnext/quotation)
5. [Material Request](/erpnext/material-request)

<!-- page: erpnext/erpnext__request-for-raw-materials-from-sales-order.md -->
---
title: "Request Raw Materials from a Sales Order | ERPNext Documentation"
description: "Create an ERPNext Material Request for BOM raw materials directly from one submitted Sales Order, including exploded-item and ordered-quantity options."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/request-for-raw-materials-from-sales-order"
updated: "2026-07-25"
---

Create a [Material Request](/erpnext/material-request) directly from one submitted [Sales Order](/erpnext/sales-order) when you need to procure raw materials for its manufactured Items. Use a [Production Plan](/erpnext/production-plan) when planning several Sales Orders or broader production demand together.

## Before you begin

Confirm:

- The Sales Order is submitted.
- Each manufactured Item has an active default [Bill of Materials](/erpnext/bill-of-materials).
- BOM quantities and UOMs are correct.
- Warehouses and projected quantities are current.
- You have permission to create and submit Material Requests.

This action is intended for manufactured Items. A purchased finished good without a BOM will not produce raw-material requirements.

## Create the Material Request

1. Open the submitted Sales Order.
2. Select **Create**.
3. Select **Request for Raw Materials**.

[Screenshot on the live page: The Sales Order Create menu with Request for Raw Materials highlighted.]

ERPNext opens a dialog containing eligible finished Items with BOMs.

4. Review the finished Items and required quantities.
5. Change the BOM only when another valid BOM should be used.
6. Select the source and target Warehouses or other options shown by your version.
7. Choose whether to include exploded Items or ignore existing ordered quantity.
8. Select **Create** or **Make**.

ERPNext creates a Material Request containing the calculated raw materials.

## Review the Material Request

Check:

- Material Request Type.
- Schedule Date.
- Item, Quantity, UOM, and Warehouse.
- Links to the Sales Order and BOM.
- Projected stock and existing supply.

[Screenshot on the live page: The generated Material Request with calculated raw-material rows.]

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock. Select the highlighted pencil icon to open the full child-row editor when you need additional planning fields.

Submit the Material Request only after confirming that it will not duplicate existing procurement or production supply.

## Options in the dialog


| Option                      | Effect                                                                                        |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| Include Exploded Items      | Uses lower-level raw materials from multi-level BOMs instead of only the immediate components |
| Ignore Existing Ordered Qty | Requests the calculated requirement without reducing it for quantities already ordered        |
| BOM                         | Selects which active BOM supplies the component structure                                     |


Field labels can vary by version. Review the generated Items rather than relying only on the option name.

## Choose this workflow or Production Plan


| Requirement                                     | Recommended workflow                                   |
| ----------------------------------------------- | ------------------------------------------------------ |
| One Sales Order needs raw-material procurement  | Request for Raw Materials from Sales Order             |
| Several Sales Orders need consolidated planning | Production Plan                                        |
| Manufacture and operations must be scheduled    | Production Plan and [Work Orders](/erpnext/work-order) |
| Replenishment is driven by stock levels         | Reorder or Material Request planning                   |


## Troubleshooting


| Problem                                 | What to check                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------- |
| Menu action is missing                  | Confirm the Sales Order is submitted and contains a manufactured Item with a valid BOM |
| Finished Item is absent from the dialog | Check the default and active BOM                                                       |
| Quantities are unexpected               | Review Sales Order Qty, BOM Qty, conversion factors, scrap, and exploded-item behavior |
| Duplicate procurement is suggested      | Review projected quantity and avoid Ignore Existing Ordered Qty unless intentional     |
| Wrong Warehouse is used                 | Review Item, BOM, Company, and dialog Warehouse defaults                               |


## Frequently asked questions

### Does this create a Purchase Order?

No. It creates a Material Request. Continue through your procurement workflow to create a [Request for Quotation](/erpnext/request-for-quotation) or [Purchase Order](/erpnext/purchase-order).

### Is the Material Request submitted automatically?

Confirm the resulting document's status in your current version and approval workflow. Review it before submission.

### Can I use a non-default BOM?

Yes, when the dialog permits selecting another active BOM.

### Should I enable Ignore Existing Ordered Qty?

Only when you intentionally want to request the full requirement despite existing supply.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Material Request](/erpnext/material-request)
- [Bill of Materials](/erpnext/bill-of-materials)
- [Production Plan](/erpnext/production-plan)
- [Purchase Order](/erpnext/purchase-order)

<!-- page: erpnext/erpnext__restore-deleted-erpnext.md -->
---
title: "Deleting and Restoring Documents\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/restore-deleted-erpnext"
updated: "2026-03-04"
---


**In ERPNext, you can delete a document if not needed. They can be masters like Items, Customer or transactions like Sales Order, Payment Entries, etc.**

To delete a document, you can go to the dropdown menu of the document and select 'Delete'.

[Screenshot on the live page: Restore Deleted Document]

For bulk deletion, you can select multiple Cancelled records and delete them at once from the List View.

[Screenshot on the live page: Restore Deleted Documents]

> Note: Any submittable document will not be deleted after submission. To delete a submitted document, you will be required to first 'cancel' the document.

## Restoration of Deleted Documents

Further, any document, if deleted by mistake, or is required after deletion, can also be restored from the Deleted Documents list.

To access Deleted Documents, go to:

> Home > Settings > Data > Deleted Documents

### 1. How to Restore Deleted Documents

1. Go to Deleted Documents List
2. Open the deleted Document
3. Click on the **Restore** button.

[Screenshot on the live page: Restore Deleted Document]

> Note: If the document was deleted after getting ** canceled**, it would be restored with a new name.

> Further, Only those Users having System Manager Role assigned to them can restore deleted documents.

<!-- page: erpnext/erpnext__retain-sample-stock.md -->
---
title: "Retaining Sample Stock\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/retain-sample-stock"
updated: "2026-02-27"
---


**Sample stock is a batch of any Items stored for analyzing should the need arise later.**

The Item for which sample stock is stored can be raw material, packaging material, or finished product.

## 1. Prerequisites
Before using sample retention, it is advised that you create the following first:

* [Item](/erpnext/item)
* [Batch](/erpnext/batch)
* [Warehouse](/erpnext/warehouse)

## 1. How to Set Sample Retention Warehouse in Stock Settings

It is advised to create a new Warehouse separately for retaining samples and not use it in production.

[Screenshot on the live page: Sample Retention Warehouse]

### 1.2 Enable Retain Sample in Item master
Retain Sample is based on Batch hence Has Batch No should be enabled first. Check Retain Sample and set the Maximum allowed samples for a batch.

[Screenshot on the live page: Retain Sample]

### 1.3 Make Stock Entry

* Whenever a [Stock Entry](/erpnext/stock-entry) is created with the purpose as Material Receipt, for items which have Retain Sample enabled, the Sample Quantity can be set during that Stock Entry. You need to select the Batch Number for the Item/Items. Sample quantity cannot be more than the Maximum sample quantity set in Item Master.

 [Screenshot on the live page: Retain Sample]

* On submission of this Stock Entry, button 'Make Retention Stock Entry' will be available to make another Stock Entry for the transfer of sample items from the mentioned batch to the retention warehouse set in Stock Settings.

 [Screenshot on the live page: Sample Retention Button]

* Clicking this button will direct you to new Stock Entry of type 'Material Transfer'. This entry is transfering your sample retention from your Target Warehouse (Stores) to the Sample Retention Warehouse. It will contain all the information, verify and click Submit.

 [Screenshot on the live page: Retain Sample]

### 2. Related Topics
1. [Warehouse](/erpnext/warehouse)

<!-- page: erpnext/erpnext__return-rejected-item.md -->
---
title: "Return Rejected Items\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/return-rejected-item"
updated: "2026-03-02"
---


In the Purchase Receipt, you can receive the Items in the Accepted or the Rejected Warehouse.

If you are creating Purchase Return for the items received in the Rejected Warehouse, then create return entry following these steps.

1. In the Purchase Receipt Item table, for the item to be returned, in the Received Qty field, enter return entry in negative.
2. In the Accepted Warehouse field, set value as zero.
3. In the Rejected Warehouse field, set the quantity to be returned in negative.

For detailed steps on how to create Purchase Return Entry for the Rejected Item, refer to the below example.

[Screenshot on the live page: Returning Rejected Items]

<!-- page: erpnext/erpnext__returned_materials_against_work_order.md -->
---
title: "Returned Materials Against Work Order\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/returned_materials_against_work_order"
updated: "2026-03-02"
---


To access the Returned Materials Against Work Order, go to:

> Home > Manufacturing > Reports > Returned Materials Against Work Order

[Screenshot on the live page: Task]

This report shows the information about the raw materials which has been returned from the work in progress warhouse against the work orders.

<!-- page: erpnext/erpnext__reverse-charge-mechanism-rcm.md -->
---
title: "Reverse Charge Mechanism (RCM)"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reverse-charge-mechanism-rcm"
updated: "2026-08-14"
---

Nova Industries buys a specialist service from Orion Advisory, a supplier that does not charge tax on its invoice. Local rules require Nova, as the buyer, to recognise and settle the tax itself. Reverse charge accounting separates the supplier payable from the tax liability and, where allowed, records the related input tax credit.



ERPNext provides the accounting building blocks, but the tax rate, eligibility, return reporting, and account classification come from your local tax rules. Have a tax adviser approve the template before production use.

## Set up the accounts


| Account              | Purpose                                    |
| -------------------- | ------------------------------------------ |
| RCM Tax Payable      | Liability for tax the company must settle. |
| RCM Input Tax Credit | Eligible recoverable tax.                  |
| RCM Tax Expense      | Non-creditable portion, when applicable.   |


## Create a purchase tax template

1. Create a Purchase Taxes and Charges Template dedicated to reverse charge.
2. Add a tax row that credits the RCM payable account at the approved rate.
3. Add a matching input-credit row when the tax is recoverable, or use an expense account for the non-creditable portion.
4. Test the supplier payable, tax liability, input credit, and invoice total before enabling the template for routine use.

[Screenshot on the live page: Purchase Taxes and Charges Template used as the base for reverse charge]



[Screenshot on the live page: Purchase tax row with calculation and account fields]



## Apply and verify

1. Create the Purchase Invoice for the supplier’s bill amount.
2. Apply the RCM template in Taxes and Charges.
3. Confirm the supplier outstanding amount does not incorrectly include tax the supplier did not charge.
4. Submit and inspect Accounting Ledger or General Ledger.
5. Settle or adjust the RCM payable through the approved tax-payment process.

[Screenshot on the live page: Transaction result after applying a purchase tax template]



## Troubleshooting

### The supplier payable includes the reverse charge tax

Review Add or Deduct, Included in Print Rate, account heads, and the second input-credit or expense row. The supplier should normally remain payable only for the supplier bill when the supplier did not charge the tax.

### The tax credit is only partly eligible

Split the amount between an input-credit account and a tax-expense account using approved rates or rows.

## Frequently asked questions

### Is this configuration country-neutral?

The accounting pattern is reusable, but the legal rules are not. Use country-specific rates, accounts, returns, and evidence.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__reviews_and_rating.md -->
---
title: "Reviews and Ratings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/reviews_and_rating"
updated: "2026-03-02"
---

Feedback is important to gauge the public sentiment of a product being sold. You can measure your product's performance by adding **Reviews and Ratings** to the Website Item's page. To enable this go to:

> E Commerce Settings > Add-ons > Enable Reviews and Ratings

Once this is done, there will be a provision in every Website Item's page to leave a review on the product.

#### Who can leave reviews?
Users that are also **Customers** in the system will be able to see the **Write a Review** button. These users must also have the **Customer Role** to be permitted to add reviews.

The average reviews are automatically calculated and a summary is displayed.

[Screenshot on the live page: Item Reviews]

<!-- page: erpnext/erpnext__role-and-role-profile.md -->
---
title: "Role and Role Profile\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-and-role-profile"
updated: "2026-02-26"
---

**A Role defines the permissions for accessing various documents in ERPNext.**

Roles define a set of permissions which can be set from the Roles Permission Manager. Most commonly used roles are already defined in ERPNext, you can use the system with them. If needed, you can add more roles. For example, if you assign the Sales User role to a user, they'll be able to access documents like Quotations and Sales Orders since the permissions are already set for the role Sales User.

**Role profiles store different roles so that multiple roles can be assigned at once.**

Role Profiles act as a template to store and select multiple roles. This Role Profile can then be assigned to a User. For example, a Sales Supervisor will have the roles Employee, Sales Manager, Sales User, and Sales Master Manager. Role Profiles are useful to assign multiple roles at once when adding multiple employees.

To access Role, go to:

> Home > Users and Permissions > Role

## 1. How to add a Role

1. Go to the Role list, click on New.
2. Enter a name for the Role.
3. Choose whether the Role has desk access. A role that has desk access can access ERPNext modules and the company's documents. The level of access depends on the roles assigned to the user.
4. Save.

You can add two factor authentication for the role and also restrict it to a specific domain. From here, you can go to the Roles Permission Manager and set permissions for the role across different DocTypes.

[Screenshot on the live page: Permissions for new Role]

## 2. How to add a Role Profile

To access Role Profile, go to:

> Home > Users and Permissions > Permissions > Role Profile

1. Go to the Role Profile list, click on New.
2. Enter a name.
3. Select the roles you want to assign to this profile.
4. Save Role Profile

<!-- page: erpnext/erpnext__role-based-permissions.md -->
---
title: "Role Based Permissions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-based-permissions"
updated: "2026-03-02"
---

**Permission to different documents can be controlled using Role Based Permissions.**

ERPNext has a role-based permission system. It means that you can assign Roles to Users, and Permissions can be set on Roles. The Role Permissions Manager allows you to set which roles can access which documents and with what permissions (read, write, submit, etc.).

Once roles are assigned to a user, their access can be limited to specific documents. The permission structure allows you to define different permission rules for different fields using a concept called **Permission Level** of a field.

1. How to use the Role Permissions Manager
------------------------------------------

To start using the Role Permission Manager, go to: > Home > Users and Permissions > Role Permissions Manager

[Screenshot on the live page: Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager]  


Permissions are applied on a combination of:

* **Roles:** As we saw earlier, Users are assigned Roles and it is on these Roles that permission rules are applied. For example, a sales user may be given the roles of an Employee and a Sales User.

Examples of Roles include Accounts Manager, Employee, HR User, etc.
* **Document Types:** Each type of document, master or transaction, has a separate list of role-based permissions as seen in the preceding screenshot.

Examples of Document Types are Sales Invoice, Leave Application, Stock Entry, etc.
* **Permission Levels:** In each document, you can group fields by "levels". Each group of fields is denoted by a unique number (0 to 9). A separate set of permission rules can be applied to each field group. By default, all fields are of level 0.

Permission "Level" connects fields with level X to a permission rule with level X. To know more click [here](/erpnext/changing-the-properties-of-a-field-based-on-role).
* **Document Stages:** Permissions are applied on each stage of the document like Creation, Saving, Submission, Cancellation, and Amendment. A role can be permitted to Print, Email, Import or Export data, access Reports, or define User Permissions.
* **User Permissions:** Using User Permissions in ERPNext a user can be restricted to access only specific Documents for that Document Type. Eg: Only one Territory from all Territories. User Permissions defined for other Document Types also get applied if they are related to the current Document Type through Link Fields.

For example, a Customer is a link field in a Sales Order or Quotation. In the Role Permissions Manager, User Permissions can be set using the 'Set User Permissions' button.

To set User Permissions based on documents/fields go to: > Home > Users and Permissions > Permissions > [User Permissions](/erpnext/user-permissions)
* **Add a New Rule**: In the Role Permissions Manager, to add a new rule, click on the **Add a New Rule** button and a pop-up box will ask you to select a Role and a Permission Level. Once you select this and click on 'Add', this will add a new row to your rules table.

2. How Role Based Permissions Work
----------------------------------

Leave Application is a good example that encompasses all areas of a Permission System.

* It should be created by an Employee. For this, Employee Role should be given Read, Write, Create permissions.

[Screenshot on the live page: Giving Read, Write and Create Permissions to Employee for Leave Application]
* An **Employee** should only be able to access his/her Leave Application. Hence, User Permissions record should be created for each User-Employee combination.

[Screenshot on the live page: Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager]
* If you want an **Employee** to only select a document in another document and not have read access to that document as a whole, then grant only Select perm to the role, Employee.

[Screenshot on the live page: Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager]
* **HR Manager** should be able to see all Leave Applications. Create a Permission Rule for HR Manager at Level 0, with Read permissions. Apply User Permissions should be disabled.

[Screenshot on the live page: Giving Submit and Cancel permissions to HR Manager for Leave Applications. 'Apply User Permissions' is unchecked to give full access.]
* **Leave Approver** should be able to see and update Leave Applications of employees under him/her. Leave Approver is given Read and Write access at Level 0. Relevant Employee Documents should be enlisted in the User Permissions of Leave Approvers. (This effort is reduced for Leave Approvers mentioned in Employee Documents, by programmatically creating User Permission records).

[Screenshot on the live page: Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.'Apply User Permissions' is checked to limit access based on Employee.]
* It should be Approved/Rejected only by HR User or Leave Approver. The Status field of a Leave Application is set at Level 1. HR User and Leave Approver are given Read and Write permissions for Level 0, while everyone else (All) are given Read permission for Level 1.

[Screenshot on the live page: Limiting read access for a set of fields to certain Roles]
* **HR User** should be able to delegate Leave Applications to his/her subordinates. HR User is given the right to Set User Permissions. A User with HR User role would be able to define User Permissions on Leave Application for other users.

[Screenshot on the live page: Let HR User delegate access to Leave Applications by checking 'Set User Permissions'. This will allow HR User to access User Permissions Manager for 'Leave Application']

In case you have correctly assigned the roles but still you're getting errors when accessing documents, refer [this page](/erpnext/report-permission-error).

### 3. Related Topics

1. [User Permissions](/erpnext/user-permissions)
2. [Role Permission For Page And Report](/erpnext/role-permission-for-page-and-report)

<!-- page: erpnext/erpnext__role-permission-for-page-and-report.md -->
---
title: "Role Permission for Page and Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/role-permission-for-page-and-report"
updated: "2026-03-02"
---

**Access to different pages and reports can be controlled in Role Permission for Page and Report.**

Document types are Sales Order, Customer, Supplier, etc. They are a **document type** meaning they can contain multiple documents of that type. A Page is a single page like [Selling Settings](/erpnext/selling-settings). You cannot create multiple Selling Settings, but you can create multiple Sales Orders.

In ERPNext, user can make a custom user interface using Page and a custom report using [Report Builder](/framework/user/en/desk/reports/report-builder) or [Query Report](/framework/user/en/desk/reports/query-report). ERPNext has a [role-based permission system](/erpnext/role-based-permissions) where you can assign roles to the user. The same role can be assigned to the page and report to access them.

If the user has enabled developer mode, then they can add the roles directly in the page and report record. In that case, the permissions will also be reflected in the JSON file for the page/report. Consider you want to restrict the roles that can access certain pages and reports in ERPNext, this can be done via the Role Permission for Page and Report.

To access Role Permission for Page and Report, go to:

> Home > Users and Permissions > Role Permission for Page and Report

## 1. How to use Role Permission for Page and Report Tool

If developer mode is disabled, the user can assign the roles to the page and report, using "Role Permission for Page and Report" page.

[Screenshot on the live page: Tools to assign custom roles to the page]

### 1.1 Reset to defaults

Using the "Reset to Defaults" button, the user can remove the custom permissions applied on a page or report. Then default permissions will be applicable on that page or report.

[Screenshot on the live page: Reset the default roles]

## Setting Role Permissions from the Page/Report as a Developer

### Role Permissions For Page

1. Go to: Home > Developer > Page.
2. Add a row and select which other roles can access the Page.
  Assign roles to the page (picture on the live page)

### Role Permissions For Report

1. Go to: Home > Developer > Report.
2. Add rows with roles who can access the Report.
  Assign roles to the report (picture on the live page)

<!-- page: erpnext/erpnext__round-off-account-validation.md -->
---
title: "Round off Account Validation Message"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/round-off-account-validation"
updated: "2026-08-14"
---

A Purchase Invoice for Nova Industries contains item calculations, tax, discount, and currency precision. The exact total differs from the payable amount by a few cents, but no account is configured to hold that difference. ERPNext asks for a Round Off Account so the debit and credit totals remain balanced.

## Configure the default

1. Open the Chart of Accounts and create or identify a small rounding expense or income account.
2. Open the Company record for Nova Industries.
3. In the accounting defaults, set the Round Off Account and Round Off Cost Center.
4. Save the Company, reload the invoice, and submit again.

[Screenshot on the live page: Company defaults for Round Off Account and Round Off Cost Center]



## Why rounding appears

Quantity multiplied by rate, taxes, discounts, exchange rates, and currency precision can produce fractions smaller than the currency accepts. ERPNext posts the small difference instead of leaving an unbalanced ledger.

## Troubleshooting

### The error remains after setting the account

Confirm the account and cost center belong to the same company, the account is a ledger account rather than a group, and the transaction was reloaded after the Company was saved.

## Frequently asked questions

### Should I use a large adjustment account?

Round Off is for small precision differences. A material difference usually indicates an incorrect rate, tax, exchange rate, or precision setting and should be investigated.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__routing.md -->
---
title: "Routing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/routing"
updated: "2026-02-27"
---

**Routing is a template of BOM Operations.**

A Routing stores all Operations along with the description, hourly rate, operation time, batch size, etc. Creating a Routing for your BOM Operations is useful when similar Operations are used for manufacturing different items.

---

### Prerequisites

- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)

---

## How to Create a Routing

1. Go to the Routing list, click on New.
2. Enter a name for the Routing.
3. Enter the Operations in the BOM Operation table:
  1. Select the Operation.
  2. The default Workstation will be fetched.
  3. Enter the Hourly Rate for running this Operation.
  4. Enter the Operation Time in minutes.
  5. Enter the Batch Size, i.e. the number of units processed in this Operation.
  6. The Operating Cost will be calculated based on the Hourly Rate and the Operation Time.
  7. Save.

Once created, a Routing can be selected in a BOM to fetch the Operations stored in the Routing.

[Screenshot on the live page]

---

## Sequence ID in Routing

[Screenshot on the live page]

Sequence ID enforces the users to complete the operations sequentially via Job Card. In case a user tries to complete an operation before completing any of its precedent operations as per the Sequence ID, the system throws a validation error.

---

### Related Topics

1. [Work Order](/erpnext/work-order)
2. [Bill Of Materials](/erpnext/bill-of-materials)

<!-- page: erpnext/erpnext__rules.md -->
---
title: "Rules"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/rules"
updated: "2026-02-26"
---

Shipping and pricing rules are essential features in ERPNext's stock module that streamline the management of shipping costs and pricing strategies. 

Shipping rules allow businesses to define various parameters for calculating shipping charges, such as weight, volume, destination, or shipping method. These rules automate the calculation of shipping costs during sales transactions, ensuring accurate and consistent shipping charges based on predefined criteria.

On the other hand, pricing rules in ERPNext empower businesses to create dynamic pricing strategies based on specific conditions or criteria. This includes setting discounts, promotions, bulk pricing, or special pricing for different customer segments, items, or sales channels.

* [Shipping Rule](/erpnext/user/manual/en/setup-shipping-rule)
* [Pricing Rule](/erpnext/user/manual/en/pricing-rule)

<!-- page: erpnext/erpnext__salary-slip-from-timesheet.md -->
---
title: "Salary Slip from Timesheet\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/salary-slip-from-timesheet"
updated: "2026-02-26"
---

**The salary of an employee can be calculated based on the number of hours that he has worked for on a particular project.**

To enable the same, you may choose to create the Employee's Salary Slip directly from a Timesheet.

[Screenshot on the live page: Salary Slip]

## 1. How to Create A Salary Slip from A Timesheet

1. Once the Timesheet is submitted, and an invoice has been generated, go to the Timesheet and click on 'Create Salary Slip'.
2. All the details, like the Employee, Employee Name, Posting Date, Company Name, Letter Head, etc. will get captured from the Timesheet.
3. **Dates**: Since this Salary Slip is getting generated out of a Timesheet, it will auto-fetch the Start Date and End Date from the Timesheet. However, the same can be changed.
4. **Salary Slip Timesheet**: The details of the Timesheet from which the Salary Slip was created will be captured. You can also more Timesheets here to create a single Salary Slip against multiple Timesheets.
5. Save and Submit.

 

[Screenshot on the live page: Salary Slip]

### 1.1. Additional Details while Creating a Salary Slip form a Time Sheet:

1. **Earnings and Deduction**: Any Earnings like HRA, Incentives etc. or Deductions like Income Tax, Provident Fund etc. in the Salary generated from the Timesheet can be mentioned here.
2. **Other Information**: According to the Salary Structure of the Employee, the Gross payment information, the Loan Repayment Information, and the Net Pay information will get auto-captured.
3. For a detailed guide on setting up overtime via timesheets, [click here](https://docs.erpnext.com/docs/v13/user/manual/en/human-resources/articles/create-payroll-entry-with-timesheets).
