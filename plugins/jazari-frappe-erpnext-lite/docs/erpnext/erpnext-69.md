<!-- Frappe documentation: erpnext, part 69 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__woocommerce_integration.md -->
---
title: "WooCommerce Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/woocommerce_integration"
updated: "2026-02-27"
---


> Deprecated in Version 15
> 
> 

Using WooCommerce Integration, the system creates Sales Orders in ERPNext for the orders created on WooCommerce using the WooCommerce webhook.

While creating a Sales Order from WooCommerce, if the Customer or Item is missing in ERPNext, the system will create new Customer/Item by using the respective details from WooCommerce order data. It also creates Address linked to the Customer using the shipping details from the order data.

1. How to set up WooCommerce?
-----------------------------

### 1.1 Generate API Key and API Secret

1. From your WooCommerce site's sidebar, click on Settings.
2. Click on the "Advanced" tab then click on the REST API link.

[Screenshot on the live page: Woocommerce API]
3. Click on "Add key" button. Provide the necessary details and click on "Generate API key" button.

[Screenshot on the live page: Woocommerce API Key]

### 1.2 Woocommerce Settings

1. On your ERPNext site, go to: **Home > Integrations > Settings > Woocommerce Settings**.
2. Paste the API key and secret generated in the previous step into the "API consumer key" and "API consumer secret" fields.
3. In the "Woocommerce Server URL" paste the url of your WooCommerce site.
4. Make sure "Enable Sync" is checked.
5. Select the "Tax Account" and "Freight and Forwarding Account" in the Account Details Section.
6. Select the "Creation User" in Defaults section. This user will be used to create Customers, Items and Sales Orders. Ensure that the user has the relevant permissions.
7. Select the "Company" that will be used to create the Sales Orders.
8. Click Save.
9. After saving the Woocommerce Settings, "Secret" and "Endpoint" are generated automatically.

[Screenshot on the live page: Woocommerce Settings]  


### 1.3 Woocommerce Webhook Settings

1. Now from your woocommerce site's sidebar, go to Settings.
2. Click on the "Advanced" tab then click on the Webhooks link and then click on "Add webhook" button.
3. Give the webhook a name of your choice.
4. Click on Status dropdown and select "Active".
5. Select Topic as "Order created".
6. Copy the "Endpoint" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Delivery URL" field.
7. Copy "Secret" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Secret" field.
8. Keep API VERSION as it is and click on Save Webhook. Now it is successfully set up.

[Screenshot on the live page: Woocommerce Webhook]  


A GIF below to show the entire process:

[Screenshot on the live page: Woocommerce Set Up]  



> **Note:** In the above screenshot and GIF, in place of delivery url on woocommerce website, you need to paste the url you will obtain after saving the "Woocommerce Settings" in the "Endpoint" field in your ERPNext instance. Here other URL was pasted as localhost was being used.
> 
> 

### 1.4 Woocommerce order creation and syncing

1. From your Woocommerce website, register yourself as a user on the Account page.
2. Now Click on Addresses option and provide the required details.
3. Click on "Shop" option and now available products can be seen.
4. Add the desired products into the cart and click on **View Cart**.
5. From the cart, once you have added the desired products, you can click on "Proceed to Checkout".
6. All billing details and Order details can be seen now. Once you are ok with it, click on **Place Order** button.
7. "Order Received" message can been seen indicating that the order has been placed successfully.
8. Now on your ERPNext instance, check the following Document Types: Customer, Address, Item, Sales Order. They will be fetched and created from the webhook data.
9. In case the orders are not synced, you can check the error in **Home > Settings > Core > Error Log**.

[Screenshot on the live page: Woocommerce Set Up]  


2. Features
-----------

### 2.1 Defaults

In the Woocommerce Settings DocType:

* **Warehouse**: This Warehouse will be used to create Sales Orders. The default Warehouse is "Stores".
* **Delivery After (Days)**: This is the default offset (days) for the Delivery Date in Sales Orders. The default offset is 7 days from the order placement date.
* **Sales Order Series**: You can set a separate series for Sales Orders created via woocommerce. The default series is "SO-WOO-".
* **UOM**: This is the default UOM used for Items and Sales Orders. The default UOM is "Nos".

[Screenshot on the live page: Woocommerce Defaults]  


3. Related Topics
-----------------

1. [Sales Order](/erpnext/sales-order)
2. [Item](/erpnext/item)
3. [Customer](/erpnext/customer)
4. [Address](/erpnext/address)

<!-- page: erpnext/erpnext__work-order-consumed-materials.md -->
---
title: "Work Order Consumed Materials"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order-consumed-materials"
updated: "2026-03-02"
---


To access the Work Order Consumed Materials, go to:

> Home > Manufacturing > Reports > Work Order Consumed Materials

[Screenshot on the live page: Task]

This report shows the information about the raw materials which has been transfer to work in progress warhouse as well consumed in manufacturing process.

<!-- page: erpnext/erpnext__work-order-summary.md -->
---
title: "Work Order Summary\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order-summary"
updated: "2026-02-26"
---


To access the Work Order Summary, go to:

> Home > Manufacturing > Reports > Work Order Summary


[Screenshot on the live page: Task]

This report will give information about the Work Order. Using this report user will understand the number of produced quantity against each Work Order as well the status of the Work Order.

Using this report user can check the status of the Work Orders which are linked to the Sales Order. Also using this report users can check the Work Orders based on the status like Not Started, In Process, Completed, and Stopped.

<!-- page: erpnext/erpnext__work-order.md -->
---
title: "Work Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order"
updated: "2026-02-27"
---

**A Work Order is a document given to the manufacturing shop floor by the Production Planner as a signal to manufacture a certain quantity of a certain Item.**

[Screenshot on the live page: Work Order]  


The Work Order also helps generate the material requirements (Stock Entry) for the Item to be produced from its **Bill of Materials**.

The **Work Order** can be generated from the [Production Plan](/erpnext/production-plan) based on Sales Orders.

To access the Work Order list, go to:

> Home > Manufacturing > Production > Work Order

1. Prerequisites
----------------

Before creating and using a Work Order, it is advised that you create the following first:

* [Bill Of Materials](/erpnext/bill-of-materials)
* [Operation](/erpnext/operation)
* [Workstation](/erpnext/workstation)

2. How to Create a Work Order
-----------------------------

1. Go to the Work Order list, click on New.
2. Select the Item to be manufactured.
3. The default BOM for that item will be fetched by the system. You can also change the BOM.
4. Enter the quantity to manufacture. Raw material Items will be fetched only when this is set.
5. If the selected BOM has Operations mentioned in it, the system will fetch all Operations from BOM, these values can be changed. Refer [section 3.2](/erpnext/work-order#32-operations-table) to know more.
6. Set the Planned Start Date (an Estimated Date at which you want the Production to begin). [Screenshot on the live page: Work Order]
7. **Use Multi-Level BOM**: This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately, you can disable this checkbox. To know more, visit [this page](/erpnext/managing-multi-level-bom).
8. Select Warehouses:


	1. **Source Warehouses**: Select this Warehouse in the Item row. The warehouse where you store your raw materials. Each required item can have a separate source warehouse. Group warehouse also can be selected as source warehouse. On submission of the Work Order, the raw materials will be reserved in these warehouses for production usage.
	2. **Work-in-Progress Warehouse**: The warehouse where your Items will be transferred when you begin production. Group Warehouse can also be selected as a Work in Progress warehouse.
	3. **Target Warehouse**: The warehouse where you store finished Items before they are shipped.
	4. **Scrap Warehouse**: If the BOM results in Scrap material, the Scrap Warehouse needs to be selected.
9. **Required Items**: All the required items (raw materials) will be fetched from BOM and populated in this table. Here you can also change the Source Warehouse for any item. And during the production, you can track transferred raw materials from this table.

> Note: You can save a Work Order without selecting the Warehouses, but Warehouses are mandatory for submitting a Work Order.

A Work Order can also be directly created from a [Sales Order](/erpnext/sales-order#214-after-submitting).

### 2.1 Additional Options when Creating a Work Order

* **Sales Order**: If you create a Work Order from a Sales Order, it will be fetched here. You can also link an existing Sales Order which has the Item to be manufactured to this Work Order.
* **Project**: Link the Work Order to a Project to track progress in cases like engineer to order.
* **Allow Alternative Item**: Sometimes when manufacturing a finished good, specific materials may not be available. For example, using plastic beads instead of plastic crystals. The finished good itself could be different. Ticking this checkbox will allow you the select an Alternative Item. To know more, visit [this page](/erpnext/item-alternative).
* **Skip Material Transfer to WIP Warehouse**: Usually, a Stock Entry is created when the raw materials are transferred to a Work In Progress Warehouse. In this case, the raw material is considered to be consumed hence the Stock Entry is skipped. The next option will be shown if you tick this checkbox.
* **Backflush Raw Materials From Work-in-Progress Warehouse**: Ticking this checkbox will automatically create a Stock Entry with the type 'Manufacture'. This means that the raw materials were consumed from the Source Warehouse, used to manufacture finished goods and another Stock Entry was created for your Target Warehouse. [Screenshot on the live page: Options when creating WO]

3. Features
-----------

### 3.1 Time

The Planned Start Date and Expected Delivery Date can be set here. The default for Planned Start Date is the current date and time at the time of creating the Work Order.

### 3.2 Required Items table

The Source Warehouse can be changed for the raw material items used here. The default Warehouse can be set at the Item level in the [Item](/erpnext/item#28-item-defaults) master or globally in [Stock Settings](/erpnext/stock-settings#23-default-warehouse).

* **Required Quantity**: This will be calculated automatically based on the [Bill Of Materials](/erpnext/bill-of-materials).
* **Transferred Quantity**: Once the Work Order starts and Job Cards are run, items are transferred from the Source Warehouse to Work In Progress Warehouse. This field shows the quantity in the WIP Warehouse. Note that if you tick on 'Skip Material Transfer to WIP Warehouse', this column will not be updated.
* **Consumed Quantity**: When the Item from the WIP Warehouse is consumed and the finished product is manufactured, this field will be updated.
* **Allow Alternative Item**: If a particular Item (raw material or sub-assembly) is not available, ticking this checkbox will allow you to select an alternative item defined in the Item Alternative list.
* **Skip Material Transfer**: If you don't want to transfer the specific raw material to the work in progress warehouse then you need to enable this checkbox.

Once uncheck this checkbox for an Item, you can still select it in the BOM and Work Order, but no Stock Entries will be created against it.

Once the Work Order is saved the following two fields will also show the availability in the respective Warehouses in the Required Items table:

* Available Qty at Source Warehouse
* Available Qty at WIP Warehouse

[Screenshot on the live page: WO material Qty]  


### 3.2 Operations table

Materials can be transferred against a Work Order or a Job Card. This is usually fetched from the [Bill Of Materials](/erpnext/bill-of-materials), but you can change it in the Work Order also.

The following will be fetched from the BOM:

* In the Operations table: The Workstations where the Operations will be performed [Screenshot on the live page: PO Opeartions]
* In the Items table: The Operations which will be performed on the Items [Screenshot on the live page: PO reassigning Operations]

These values can also be changed.

Once the Work Order is saved the following fields will be shown:

* **Completed Qty**: The number of Items on which this Operation was performed.
* **Status**: Whether the Operation is Pending, Work In Progress, or Completed. The status here is updated when the Job Cards are updated.
* **Operation Time**: This is fetched from the BOM, but can be changed.
* **Planned Operating Cost**: This is calculated based on the Operating Time, Hourly Rate, Quantity being manufactured, etc.

The Actual Operation Time, Actual Operating Cost, Actual Start Time, and Actual End Time are updated when Job Cards are updated.

### 3.3 Operation Cost

In this section, the following are shown:

* **Planned Operating Cost**: This is fetched as per the BOM and the Operations defined in it.
* **Actual Operating Cost**: This is fetched from the Job Cards based on the Operations run on the Items.
* **Additional Operating Cost**: Any additional expenses you may have incurred when manufacturing the Item can be added here.
* **Total Operating Cost**: This is calculated as Actual Operating Cost + Additional Operating Cost.

These values are calculated as per the Job Cards.

[Screenshot on the live page: Work Order Operation Costs]  


### 3.4 More Information

Here the Item Description and Stock UOM is shown for the Item being manufactured.

When a Work Order is created from a [Material Request](/erpnext/material-request), it'll be shown here.

### 3.5 Transferring Materials for Manufacturing

* Once you have submitted your Work Order, you need to Transfer the Raw Materials to initiate the Manufacturing Process.
* This will create a Stock Entry with all the Items required to complete this Work Order to be added to the WIP Warehouse. This will add the sub-assembly Items as is or explode them to show the raw materials depending on whether you ticked 'Use Multi-Level BOM' or not.
* Click on 'Start'. Once you click on Start, Job Cards will be created for the [Operations](/erpnext/job-card) involved.

[Screenshot on the live page: Transfer Materials]
* Mention the quantity of materials to be transferred in this run.

[Screenshot on the live page: Material Transfer Qty]
* You'll be taken to a Stock Entry for 'Material Transfer for Manufacture'. Submit it.
* Material Transferred for Manufacturing will be updated in the Work Order based on the Stock Entry.

[Screenshot on the live page: Stock Entry for PO]
* **Note:** User can only transfer items which has "Include Item In Manufacturing" enabled in the item master

### 3.6 Material Transfer through Stock Entry

Use cases for this option are:

* If a material transfer is done in bulk and/or is not required to be tracked against a particular Work Order.
* If the responsibility for Material Transfer and Production Entry lies with two separate Users.

If this is the case, you can tick the 'Skip Material Transfer' checkbox, which will allow you to make the Stock Entry of type 'Manufacture' directly by clicking on the ‘Finish’ button.

### 3.7 Creating Job Cards

* Progress in the Work Order can be tracked using Job Cards
* Drafts of Job Cards are created based on when a Work Order is Submitted.
* To create more Job Cards against a Work Order click on the plus sign next to Job Card on the Work Order dashboard.

To know more about Job Cards, visit [this page](/erpnext/job-card).

### 3.8 Updating Finished Goods

* Once you are done with the Work Order you need to update the Finished Goods.
* This will create a Stock Entry that will deduct all the items and sub-assemblies from the WIP Warehouse and add them to the Finished Goods Warehouse.
* Click on 'Finish'.

[Screenshot on the live page: Update Finished Goods]
* Mention the quantity of materials to be transferred.

> Tip: You can also partially complete a Work Order by updating the Finished Goods stock creating a Stock Entry.

### 3.9 Capacity Planning in Work Order

* When a Work Order is submitted, based on the Planned Start Date and the availability of the Workstations, the system schedules all operations for the Work Order (if Work Order has Operations specified).
* Drafts of Time Logs are also created based on the scheduled operations.

On Submitting the Work Order, the system will reserve a slot for each of the Work Order Operations serially after the planned start date based on the Workstation availability. The Workstation availability depends on the Workstation timings, holiday list, and if some other Work Order Operation is scheduled in that slot.

You can mention the number of days for the system to try scheduling the operations in the Manufacturing Settings. This is set to 30 Days by default. If the operation requires time exceeding the available slot, the system will ask you to break the operations. Once the scheduling is done the system will create Time Logs and save them. You can Modify them and submit them later.

### 4.0 Stopping a Work Order

When you stop a Work Order its status is changed to Stopped indicating that all production process against that Work Order has stopped. But before stopping the work order user has to make sure that the raw materials which were transferred to the Work In Progress warehouse have been returned or not. In case, if the user has tried to stop the work order without returning the raw materials then the system will throw the error and not allow the user to stop the work order.

To stop a Work Order, click on the 'Stop' button.

[Screenshot on the live page: PO - stop]  


You can also re-open the stopped Work Order.

[Screenshot on the live page: Reopen Work Order]  


### 4.1 Return Non Consumed Materials to the Stores from WIP Warehouse

If you have transferred extra materials to the Work In Progress warehouse and after completion of the work order you want to return it to the Store warehouse. Then you have to goto the Work Order and click on Return Components. After that system creates the return stock entry with type as Material Transfer for Manufacture.

[Screenshot on the live page: Return Components]  


You can also checks the returned components against the work order using Work Order Consumed Materials report

[Screenshot on the live page: Return Components Qty]  


### 4.2 Transfer Addtional Materials

The Transfer Materials button is not showing because all required materials have already been transferred from Store to WIP warehouse against the work order, but the user wants to transfer additional materials since some are damaged.


[Screenshot on the live page]

**Configuration**

To fixed the issue, user has to set the percentage for 'Transfer Extra Raw Materials to WIP (%)' in Manufacturing Settings.


[Screenshot on the live page]

Once the user sets the 'Transfer Extra Raw Materials to WIP (%)' in Manufacturing Settings, they can transfer additional materials from the store to WIP against the work order.


[Screenshot on the live page]



5. Related Topics
-----------------

1. [Job Card](/erpnext/job-card)
2. [Pick List](/erpnext/pick-list#22-create-pick-list-from-work-order)

<!-- page: erpnext/erpnext__workflow-actions.md -->
---
title: "Workflow Actions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-actions"
updated: "2026-03-02"
---


> Introduced in Version 11
> 
> 

**'Workflow Actions' is a single place where you can track and manage all pending actions you have to take on Workflows.**

Workflow Actions will send email notifications only if the 'Send Email Alert' checkbox is ticked in the Workflow that you've created.

To access Workflow Actions, go to:


> Home > Settings > Workflow Actions
> 
> 

If a User is eligible to take action on some workflows, emails will be sent to the user with the relevant document as attachment. From there the user can `Approve` or `Reject` the Workflow.

[Screenshot on the live page: Workflow Action Email]  


Also the users will see entries in their Workflow Action list:

[Screenshot on the live page: Screenshot 2024-06-03 at 10.47.43 AM]  


**Note:**

* You can set email template for Workflow Actions on each state. The template might consist of a message for users to proceed with the next Workflow Actions.
* Workflow Actions will not be created for a transition to optional states.

### Related Topics

1. [Workflows](/erpnext/workflows)
2. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workflow-state.md -->
---
title: "Workflow State"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-state"
updated: "2026-03-02"
---

**A 'Workflow State' is a specific status that a document (such as a sales order, purchase order, or leave application) can be in during its lifecycle.**

Workflow states are crucial for managing multi stage approval processes, ensuring proper checks and balances, and maintaining the flow of operations.

Different Workflow States may be achieved before or after applying different Workflow Actions on them. If you want to create a Workflow where there are multiple approvals from manager, senior manager, general manager, etc, you can set the states for it from Workflow States.

[Screenshot on the live page: Screenshot 2024-05-27 at 10.12.28 AM]  


The system represents different states in different colours based on the Style tagged to each stage.

* Success - Green
* Danger - Red
* Inverse - Black
* Primary - Dark Blue
* Info - Light Blue
* Warning - Orange

### Related Topics

1. [Workflows](/erpnext/workflows)
2. [Workflow Actions](/erpnext/workflow-actions)
3. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workflow-transition-tasks.md -->
---
title: "Workflow Transition Tasks"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-transition-tasks"
updated: "2026-03-02"
---

> Note: To be added in version 16
>
>

## Introduction
Workflow Transition Tasks are actions that can be run during state transitions in workflows. Each Workflow Transition can link to a set of transition tasks.
[Screenshot on the live page: Link to Workflow Transition Tasks]

[Screenshot on the live page: A Typical set of transition tasks]

Each Workflow Transition Task can have tasks of the following types:

1. App-Defined Actions (specified by each Frappe app through hooks.py)
2. [Server Scripts](/framework/user/en/desk/scripting/server-script)
3. [Webhooks](/framework/user/en/guides/integration/webhooks)

[Screenshot on the live page: A server script transition task]

On top of this, each transition task can be either:

1. **Synchronous**: This is the default mode of transition tasks. All of the transition tasks run one-by-one when the state transition is initiated. Even if one of them fails, the transition is reversed.
2. **Asynchronous**: This mode can be enabled using the 'Asynchronous' checkbox. Each asynchronous transition task runs after the state transition is completed, meaning it has zero influence over state completion, and is run in a separate background job of its own.

### App-Defined Actions
Each Frappe app defines them using the 'workflow_methods' [hook](/framework/user/en/python-api/hooks).

Any dotted path method defined through the workflow_methods hook has to accept `doc: Document` as the parameter, which is the document on which the transition is being applied.

An example of an app-defined task is:

```python 
# hooks.py
workflow_methods = [{"name": "Create a customer", "method":
					 "myapp.shop.doctype.kirana.create_customer"}]

# myapp/shop/doctype/kirana.py
def create_customer(doc):
    customer = frappe.new_doc("Customer")
    customer.customer_name = "Customer " + doc.name
    customer.customer_type = "Individual"

    customer.save()
```

These will be available in the 'Tasks' drop-down if any of the apps has provided them.
[Screenshot on the live page: app-defined tasks]

If you are an end user, you can not create app-defined actions on your own and will have to use server scripts as mentioned below.



### Server Scripts
These also take the `doc: Document` parameter and can be set using the 'Workflow Task' Script Type.
[Screenshot on the live page: server script tasks]

And then these have to be linked to in the transition task:
[Screenshot on the live page: A server script transition task]


### Webhooks
These can be created by setting the 'Doc Event' field of the webhook to 'workflow_transition':
[Screenshot on the live page: workflow_transition webhook]

And then these have to be linked to in the transition task:
[Screenshot on the live page: link to webhook]

### Related Topics
* [Workflow State](/erpnext/user/manual/en/workflow-state)
* [Workflow Actions](/erpnext/user/manual/en/workflow-actions)
* [Workflows](/erpnext/user/manual/en/workflows)

<!-- page: erpnext/erpnext__workflow.md -->
---
title: "Workflow"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow"
updated: "2026-03-02"
---

A typical 'Workflow' in ERPNext involves various stages to manage different aspects of business operations. It starts with creating a document and taking it through series of steps. Users can track the status of each document and collaborate with team members by assigning tasks and tracking their progress.

ERPNext streamlines processes by automating repetitive tasks that need multi phase attention by different people. ERPNext offers a comprehensive workflow to enhance productivity and efficiency across various departments within an organisation.

* [Workflow State](/erpnext/user/manual/en/workflow-state)
* [Workflow Actions](/erpnext/user/manual/en/workflow-actions)
* [Workflows](/erpnext/user/manual/en/workflows)
* [Workflow Transition Tasks](/erpnext/user/manual/en/workflow-transition-tasks)

<!-- page: erpnext/erpnext__workflows.md -->
---
title: "Workflows"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflows"
updated: "2026-03-02"
---

**With workflows you can rewrite how a particular process/workflow is approved in ERPNext.**

You can set multiple levels of approval for an ERPNext Workflow. To allow multiple people to submit multiple requests, for approvals by multiple users, ERPNext requires you to fill the Workflow conditions. ERPNext tracks the multiple permissions before submission.

Consider a scenario, where multiple levels of approval are required for a quotation. A sales person (user with 'Sales User' role) will create a quotation. Then it is either approved or rejected by a sales lead (user with 'Sales Manager' role). If approved by sales lead, it is further approved or rejected by regional manager (user with 'Regional Manager' role).

To make a Workflow and transition rules go to:

> Home > Settings > Workflow

Once a Workflow is created, you can take actions on it via [Workflow Actions](/erpnext/workflow-actions).

1. Prerequisites
----------------

Before creating a Workflow, it is advised to create these first:

* [Workflow Actions](/erpnext/workflow-actions)
* Workflow States like Approved, Canceled, etc.

2. How to Create a Workflow
---------------------------

1. Go to the Workflow list, click on New.
2. Enter a name for the **Workflow** and select the DocType on which to be applied.
3. Enter the different states of the Workflow. Enter Doc Status for them, select which field to update from the Update Field column, enter what the value will be updated to under Update Value.

The Workflow States can have different colors according to the state. Eg: Green for success. Document statuses: Saved = 0, Submitted = 1, Cancelled = 2.

[Screenshot on the live page: Workflow]
4. Enter the Transition Rules.

[Screenshot on the live page: Workflow Transition Rules]

### 2.2 Things to note when creating a Workflow

* Creating a Workflow in ERPNext essentially overrides the regular Save and Submit workflow. Thus the document will function based on your Workflow and not based on the pre-set code workflow. Hence there might be no Submit button/option if you have not specified it in the Workflow you create.

If you don't apply a Workflow to a document, and that document is submittable, then it has the default workflow with states: Draft - Submitted - Cancelled. If you are applying a Workflow to a submittable document, then those default states should be handled by the user.
* A document cannot be canceled unless it is submitted.
* If you wish to give the option to cancel, you will have to write a workflow transition step that says from submitted you can cancel.
* If fields under Update Field column are not updated, a new custom field will be created with the name you set in the 'Workflow State Field' field.

### 2.3 Other options for a Workflow

1. Is Active: On ticking this, all other Workflows for the selected DocType become inactive.
2. Don't Override Status: This Workflow's status will not override the status of the document (Quotation) in the list view.
3. Send Email Alerts: Emails will be sent to the user with next possible workflow actions.

3. Features
-----------

### 3.1 Enable/Disable Optional Workflow State

> Introduced in Version 12

In States, optional Workflow state means that the state may not be a part of final approval.

E.g. states like Canceled or Rejected can be optional. [Screenshot on the live page: Optional State]  


**Note:** Workflow Actions are not created for optional states.

### 3.2 Conditions

You can also add a condition for the Transition to be applicable. For example, in this case, if sales executive creates a quotation with grand total of $100,000 or more, a particular role must approve. For this to happen in the particular transition, you can set a property for **Condition**:


```
doc.grand_total <= 100000
  

```
Here, `grand_total` is the field name of the field 'Grand Total' of Quotation. To see the field name of a field go to Menu > Customize.

This can be extended to any property of the document.

> Introduced in Version 13

In Version 13, you can use date/time, session, get*value and get*list functions in your condition expressions.

Allowed functions:

* frappe.db.get_value
* frappe.db.get_list
* frappe.session
* frappe.utils.now_datetime
* frappe.utils.get_datetime
* frappe.utils.add*to*date
* frappe.utils.now

Examples:


```
doc.creation > frappe.utils.add_to_date(frappe.utils.now_datetime(), days=-5, as_string=True, as_datetime=True)
  

```
4. Example of a Quotation Approval Process
------------------------------------------

When a quotation is saved by sales user, the status of the document changes to "Draft" and when clicked on submit the status changes to 'Approval Pending By Sales Manager':

[Screenshot on the live page: Workflow State in Transaction]  


When the Sales Manager logs in, he can either Approve or Reject. If approved the status of the document changes to "Approval Pending By Regional Manager".

[Screenshot on the live page: Workflow Action Options]  


When the Regional Manager opens the quotation, he can finally "Approve" or "Reject" it.

[Screenshot on the live page: Workflow Action Options]  


5. Video
--------

### 6. Related Topics

1. [Workflow Actions](/erpnext/workflow-actions)
2. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workspace.md -->
---
title: "Customizing Workspace"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workspace"
updated: "2026-03-04"
---

When you log in, you're presented with the Desk. It features a persistent sidebar sorted into categories. Each sidebar item links to a page called Workspace.

A Workspace represents a module (for example CRM in ERPNext). A Workspace includes the following:

* A dashboard section for that particular module.
* A shortcut section for frequently used masters, transactions or pages.
* A masters section where all the reports and masters are grouped and listed.

Standard Workspace
------------------

Every module in ERPNext has its own Standard Workspace which is generated with appropriate shortcuts and links.

Any customization to be made to the Standard Workspace can be done with Customize Workspace option in the top right corner of the Workspace.


> Note: These customizations will be user-specific and will only be visible to that user.
> 
> 

Custom Workspace
----------------

You can also create your own Workspaces by simply creating a new Workspace document.

1. Go to the Workspace list and click on New.
2. **Name**: The text you enter here will be shown in the sidebar.
3. **Module**: Select the module which the Workspace will represent.
4. ***Is Standard***: If checked, this Workspace will be shown in the sidebar. Otherwise it will be treated as a customized version of a Standard Workspace.
5. ***Extends Another Page***: If checked, this Workspace will be treated as a customized version of another Workspace.
6. ***Is Default***: If checked, this Workspace will be the default Workspace displayed to all users for a particular module.
7. ***Dashboard***: Add a Dashboard to display it on the top of the Workspace.
8. ***Shortcuts***: Add Shortcuts to a specific page, reports or list which will be displayed below the dashboard.
9. ***Link Cards***: You can add cards that will display a list that links to a specific page, report, or list.

<!-- page: erpnext/erpnext__workstation.md -->
---
title: "Workstation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workstation"
updated: "2026-02-28"
---

**A Workstation stores information regarding the place where the workstation operations are carried out.**

Data regarding the operation cost, rent, electricity can be stored here.

An Operation takes place at a Workstation. The Operation is the work performed and the Workstation is the place/machine where it is performed. For example, melting is an Operation that can be done at 10 different Workstations.

:::note
An Operation can take place at multiple Workstations.
:::























## How to create a Workstation

1. Go to the Workstation list, click on New.
2. Enter a name for the Workstation.
3. Under Operating Costs, enter operating component with the cost:
  1. Electricity
  2. Rent
  3. Consumables
  4. Wages
4. Save.

Optionally, you can enter a description for the Workstation.

---

### Operating Components

Using this table you can divide the different cost components and set it to the Operation.

[Screenshot on the live page]

### Workstation Operating Component

User can also define the expense account per component company wise in the Workstation Operating Component.

[Screenshot on the live page]

---

A [Holiday List](/hr/holiday-list) can be added to exclude counting these days for the Workstation.















The hours when the Workstation will be Operational can be added. On adding a Holiday list, the days listed as holidays won't be counted as working for the Workstation.

Under Working Hours table, you can add start and end times for a Workstation. For example, a Workstation may be active from 9 am to 1 pm, then 2 pm to 5 pm. You can also specify the working hours based on shifts. While scheduling a [Work Order](/erpnext/work-order), the system will check for the availability of the Workstation based on the working hours specified.

:::note
You can enable overtime for a Workstation in Manufacturing Settings.
:::









[Screenshot on the live page]

After saving the Workstation, the following actions can be performed against it:

[Screenshot on the live page]

---

## Features

### Production Capacity

Production Capacity is the total number of jobs can be executed at the same time in the respective workstation.

[Screenshot on the live page]

---



---

## Related Topics

1. [Bill Of Materials](/erpnext/bill-of-materials)
2. [Operation](/erpnext/operation)
3. [Routing](/erpnext/routing)
4. [Work Order](/erpnext/work-order)
5. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__workstation_type.md -->
---
title: "Workstation Type"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workstation_type"
updated: "2026-02-26"
---

If users have the same types of multiple Workstations (Machines) and users want to auto-assign jobs to the available workstation based on workstation type then this feature is the good option for them. A Workstation Type document will allow you to set the same operating cost to multiple operations by just setting the Workstation Type in the Operations table in [BOM](https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials) or [Routing](https://docs.frappe.io/erpnext/user/manual/en/routing).

[Screenshot on the live page]

After adding Workstation Type, users has to assign the Workstation Type to the respective Workstation and set the Workstation Type to the respective Operation in the BOM.

[Screenshot on the live page]

After setting up Workstation Type when user make the Work Order with Operations system will create Job Cards against the Operation and set the available Workstation based on the Workstation Type set in the BOM.

[Screenshot on the live page]

<!-- page: erpnext/erpnext__zenoti_integration.md -->
---
title: "Zenoti Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/zenoti_integration"
updated: "2026-02-26"
---

>Introduced in version 13.

Zenoti Integration pulls the purchase orders and sales invoices from Zenoti and creates Purchase Order and Sales Invoice against them in ERPNext.

While creating these records if Customer, Supplier or Item is missing in ERPNext the system will create new Customer, Supplier or Item by pulling respective details from Zenoti.

### How to Setup?
Zenoti Integration is available through *Ecommerce Integrations* on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).

### App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).
- If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`

The repository for app is hosted on GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/).

### Prerequisite

1. For each center in Zenoti there should be a cost center and a warehouse created in ERPNext which will be used in Cost Center and Warehouse Mapping table in Zenoti Settings in ERPNext.
2. Items*(alteast those having stock impact)* have to be created. Data import can be used for this.
3. Opening stock entries have to be created using Stock Reconciliation in ERPNext.
4. Item Tax Templates have to be created from Tax Groups in Zenoti with proper accounts and tax rates.
5. Create an account to book liability for the sales of gift or prepaid cards and tips, this is to be set as *Liability Income Account to book Gift & Prepaid cards* in Zenoti Settings.
6. Set appropriate accounts in the mode of payments. Also add "Card", "Custom" and "Points" as Mode of Payment.
7. "Enable Perpetual Inventory" should be unchecked in Company Master.

### Important details for setting up Zenoti on ERPNext

> To access Zenoti Settings, go to: Awesome search bar > Zenoti Settings.

[Screenshot on the live page: Zenoti setting page]

1. **Last Sync:** Date and time of when the invoices were synced last.
2. **API Key:** API Key from Zenoti. If you do not have an API Key, you can easily generate one by going to Admin > Setup > API section.
3. **Sync Interval:** Duration in hours between each syncing. Following options are avaliable *(1, 3, 6, 12, 24)*
4. **Default Purchase Warehouse:** Warehouse to be set for all the Purchase Orders. Usually this is the main center in Zenoti so put the one you created for main center.
5. **Default Buying Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Buying* provided by ERPNext.
6. **Default Selling Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Selling* provided by ERPNext.
7. **Liability Income Account to book Tips, Gift & Prepaid cards:** Add here the account you created to book Tips and sales of Gift & Prepaid cards.
8. **Default Customer Group:** If on creation of new customer while syncing sales invoice a specific customer group is to be assigned to them then add that here. If nothing is added then the default *All Customer Group* will be set for those new customer.
9. **Default Supplier Group:** If on creation of new supplier while syncing purchase order a specific supplier group is to be assigned to them then add that here. If nothing is added then the default *All Supplier Group* will be set for those new supplier.
10. **Cost Center and Warehouse Mapping:** In this table map all the Centers of Zenoti to their corresponding Cost Centers and Warehouses in ERPNext.

### What will be synced or will have to be created manually

#### Item
Items will have to be created manually into ERPNext from Zenoti one time at the start. Then it will be created on a demand basis when syncing sales /purchase orders.

#### Item Tax Template
Item Tax Template will be created manually based on Tax Groups on zenoti.

#### Customer
Customer and Customer Group will be created on demand basis while syncing sales invoices. If there are no customer groups in Zenoti, “Default Customer Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Customer Groups” will be used.

#### Supplier
Supplier and Supplier Group will be created on demand basis while syncing purchase orders. If there are no supplier groups in Zenoti, “Default Supplier Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Supplier Groups” will be used.

#### Warehouse
Warehouses will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.

#### Cost Center
Cost Centers will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.

#### Employees
Employees will have to be created manually into ERPNext from Zenoti one time at the start. Then it can be created on a demand basis when syncing sales/purchase records. For Employees fields "Date of Birth", "Date of Joining" are mandatory. Hence when creating employee from sales/purchase records "Date of Joining" will be set as the day the employee is created and "Date of Birth" as 25 years before "Date of Joining". These can be changed later on.

#### Purchase Order
Purchase Order will be created in Zenoti and sync into the ERPNext at the end of the day.
Supplier and Item will be created on demand basis if new.

> Note: Purchase Invoice from the Purchase Order have to be created manually.

#### Debit Note
Debit Note will be created automatically and remain in Draft mode based for Return Purchase Order in Zenoti.

#### Sales Invoice
Invoice will be created automatically via API on the given interval set in Zenoti Settings.
Customer and Item will be created on demand basis if new.

#### Credit Note
Credit Note will be created automatically based on Return Invoice in Zenoti and will only contain products and not services.

#### Gift/Prepaid Card Sales
Each Gift/Prepaid card will be treated as Items.
Gift/Prepaid Cards will be treated as mode of payment for future invoices where the payment was done using these in Zenoti.

#### Stock Reconciliation
At the end of the day, stock will be synced via Stock Reconciliation.
