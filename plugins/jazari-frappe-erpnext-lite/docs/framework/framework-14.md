<!-- Frappe documentation: framework, part 14 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__desk__reports__query-report.md -->
---
title: "Query Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/query-report"
updated: "2026-04-21"
---

Query Reports are reports that can be generated using a single SQL query. The
query can be simple or complex as long as it generates columns and records.
These reports can only be created by a System Manager and are stored in the database.

To create a Query Report, type "new report" in the awesomebar and hit enter.

1. Set Report Type as "Query Report"
2. Set the Reference DocType - Users that have access to the Reference DocType will have access to the report
3. Set the Module - The report will appear in the "Custom Reports" section of the module.
4. Write your query

> If you set Standard as "Yes" and Developer Mode is enabled, then a JSON file
> will be generated which you will have to check in to your version control. You
> should do this only if you want to bundle Query Reports with your app. The
> Module will decide where the JSON file will go.

[Screenshot on the live page: New Query Report]

### Columns and Filters

> Added in Version 13

You can configure the columns and filters in the Report document. Here you can set the label, width, format (fieldtype) for the columns and filters.

Filters can be used as formatting variables in the query. For example a filters of type `customer` can be used as `%(customer)s` in the query.

[Screenshot on the live page: Standard Columns and Filters]

#### Example

```sql
SELECT
 name, creation, production_item, qty, produced_qty, company
FROM
 `tabWork Order`
WHERE
 docstatus=1
 AND ifnull(produced_qty,0) < qty
```

### Formatting columns (Old Style)

Alternatively columns can also be formatted by specifying the label of the column in a particular format: `{label}:{optional fieldtype}{optional /}{optional options}:{optional width}`

If you have configured the fields and columns in the Report itself, you do not need to use this style.

#### Example (Old Style)

Here is what a query may look like:

```sql
SELECT
 `tabWork Order`.name as "Work Order:Link/Work Order:200",
 `tabWork Order`.creation as "Date:Date:120",
 `tabWork Order`.production_item as "Item:Link/Item:150",
 `tabWork Order`.qty as "To Produce:Int:100",
 `tabWork Order`.produced_qty as "Produced:Int:100",
 `tabWork Order`.company as "Company:Link/Company:"
FROM
 `tabWork Order`
WHERE
 `tabWork Order`.docstatus=1
 AND ifnull(`tabWork Order`.produced_qty,0) < `tabWork Order`.qty
 AND NOT EXISTS (SELECT name from `tabStock Entry` where work_order =`tabWork Order`.name)
```

If you notice there is a special syntax for each column, we use this information
to format the Report View.

For example: The first column `Work Order:Link/Work Order:200` will be rendered
as a Link Field with the DocType Work Order and the column width would be 200px.

[Screenshot on the live page: Query Report View]
*Query Report View*

<!-- page: framework/framework__user__en__desk__reports__report-builder.md -->
---
title: "Report Builder\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/report-builder"
updated: "2026-02-17"
---


Report Builder is the simplest type of Report and can be created without any
code. It will only show the records of single DocType as well as child records of
Child Tables.

#### Saving Reports

By default a Report View is generated for all DocTypes. The user can also save
multiple Reports based on different combination of filters, ordering, columns,
etc.

[Screenshot on the live page: Report Builder]
*Report Builder*

#### Updating or Deleting Custom Reports

Any custom report created by a user using Report Builder can be then updated or deleted by them from the Report View.

[Screenshot on the live page: Update or Delete a Custom Report]
*Update or Delete a Custom Report*

#### Printing

Reports can be printed from the Menu.

[Screenshot on the live page: Report Builder Print]
*Report Builder Print*

#### Group By

You can also apply group by clause on columns and use aggregate functions like Count, Sum and Average.

[Screenshot on the live page: Report Builder Group By]
*Report Builder Group By*

#### Keyboard Navigation and Editing

Since report builder is a view of single DocType, they can also be edited.

[Screenshot on the live page: Report Builder Editing]
*Report Builder Editing*

<!-- page: framework/framework__user__en__desk__reports__script-report.md -->
---
title: "Script Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/script-report"
updated: "2026-07-22"
---

Anything that can't be achieved using Report Builder or Query Report can be  
achieved using Script Reports. As the name suggests, these reports are built  
using Python scripts. Since these reports give you unrestricted access via  
Python scripts, they can only be created by Administrators. These reports are  
meant to be written during development and be a part of your app.

> To create Script Reports you must enable Developer Mode.

To create a Script Report, type "new report" in the awesomebar and hit enter.

1. Set Report Type as "Script Report"
2. Set "Is Standard" as "Yes"
3. Select the Module in which you want to add this report
4. In the module folder (for example if it is Accounts in ERPnext the folder
  ill be `erpnext/accounts/report/[report-name]`) you will see that templates  
  or the report files will be created.
5. Write your python script in the generated `{report-name}.py` file.
6. You can add filters to your report by adding them to `{report-name}.js`

[Screenshot on the live page]
*Script Report*

### Standard and Custom Reports

> Added in Version 12

Verson 12 onwards, you can make custom Query and Script reports in Frappe Framework. In custom reports, the script can be added directy in the Report itself and you can use the [Script API](/framework/v14/user/en/desk/scripting/script-api) functions of Frappe Framework.

### Columns and Filters

> Added in Version 13

You can configure the columns and filters in the Report document. Here you can set the label, width, format (fieldtype) for the columns and filters.

Filters can be used as formatting variables in the query. For example a filters of type `customer` can be used as `%(customer)s` in the query.

[Screenshot on the live page]

### Writing the script

#### Custom Report

In custom reports, you can use the [Script API](/framework/v14/user/en/desk/scripting/script-api) and write the script directly in the Code section.

```python
return frappe.db.get_all('User', ['first_name', 'last_name'], filters = filters)
```

#### Standard Report

The generated `.py` file comes with a boilerplate for your report. There is one method named `execute` which takes `filters` and returns `columns` and `data`. You can use any combination of python modules and SQL queries to generate your report. The `execute` function looks like this

```python
from __future__ import unicode_literals
# import frappe

def execute(filters=None):
 columns, data = [], []
 return columns, data

```

The `execute` function is supposed to return the `columns` and the `data` to be shown in the report by default. A developer can optionally return a few paramters like `message`, `chart`, `report_summary`, `skip_total_rows`.

The following are the parameters that can be returned by the execute function

#### columns

This is a list of dictionaries. This holds all the columns that are to be displayed in the datatable in an order.

**Note:** You only need to return columns if you have not specified them in the Report

Example:

```python
columns = [
 {
 'fieldname': 'account',
 'label': _('Account'),
 'fieldtype': 'Link',
 'options': 'Account'
 },
 {
 'fieldname': 'currency',
 'label': _('Currency'),
 'fieldtype': 'Link',
 'options': 'Currency'
 },
 {
 'fieldname': 'balance',
 'label': _('Balance'),
 'fieldtype': 'Currency',
 'options': 'currency'
 }
 ]
```

#### Results

This can be a list of lists or a list of dictionaries. This holds the data to be displayed in the report

Example:

```python
data = [
 {
 'account': 'Application of Funds (Assets)',
 'currency': 'INR',
 'balance': '15182212.738'
 },
 {
 'account': 'Current Assets - GTPL',
 'currency': 'INR',
 'balance': '17117932.738'
 },
 ...
 ]
```

#### chart

Contains the configuration for the default chart to be shown in the report.

#### report_summary

This is a list of dictionaries that stores the important values in the report and is shown separately in the top section on the UI.

Example:

```python
[{
 "value": profit,
 "indicator": "Green" if profit > 0 else "Red",
 "label": _("Total Profit This Year"),
 "datatype": "Currency",
 "currency": "INR"
}]
```

> Note: These arguments are supposed to be returned in the specific order as follows

Here is a script report from ERPNext: [Balance Sheet](https://github.com/frappe/erpnext/blob/develop/erpnext/accounts/report/balance_sheet/balance_sheet.py)

#### Adding filters

To add filters in your report define the fields and their fieldtypes in the  
`{report-name}.js` file. The filter values will be available in the `execute`  
method as a dict.

```js
frappe.query_reports['Balance Sheet'] = {
 filters: [
 {
 fieldname: 'company',
 label: __('Company'),
 fieldtype: 'Link',
 options: 'Company',
 default: frappe.defaults.get_user_default('company')
 },
 {
 fieldname: 'periodicity',
 label: __('Periodicity'),
 fieldtype: 'Select',
 options: [
 'Monthly',
 'Quarterly',
 'Half-Yearly',
 'Yearly'
 ],
 default: 'Yearly',
 depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
 }
 ]
}
```

Similar to the `depends_on` property that controls the display of fields, in  
Version 13 we have introduced `depends_on` for Script Report filters. This can  
be used to determine whether the filter will be visible based on the value of the  
condition in `depends_on`.

[Screenshot on the live page]
*Balance Sheet*

[Screenshot on the live page]
*Balance Sheet*



> *Protip*: To navigate directly to a Report of any of the above type, type its  
> name in the awesomebar and hit enter.



## Snapshot Reports

An advanced report generation engine. It requires manually rewriting report to use OLAP databases.



1. Enable 'Snapshot Report' in System Settings -> Advanced. This sets up a background job that syncs data from MariaDB to DuckDB
  [Screenshot on the live page]
2. Enable 'Snapshot Report' checkbox in Report master
  [Screenshot on the live page]
3. Rewrite the report using the `execute_snapshot_report` method in your report module.

```python
def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.
    
    This is the main entry point for snapshot report. When 'Synced
    Report' is enabled in report, framework will call this method 
    every time the report is refreshed or a filter is updated. It 
    accepts the same filters as normal execute. But a utility method - 
    get_latest_sync, is also imported.
    """

    from frappe.database.duckdb.database import get_latest_sync
    columns = get_columns()
    data = get_data()

    return columns, data
```

<!-- page: framework/framework__user__en__desk__scripting.md -->
---
title: "Scripting\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting"
updated: "2026-02-17"
---


Frappe framework allows you to script the standard models and views directly within the framework without additional code.

Different ways of Scripting:

1. [Client Script](/framework/v14/user/en/desk/scripting/client-script)
1. [Server Script](/framework/v14/user/en/desk/scripting/server-script)
1. [Script Report](/framework/v14/user/en/desk/reports/script-report)
1. [System Console](/framework/v14/user/en/desk/scripting/system-console)

<!-- page: framework/framework__user__en__desk__scripting__client-script.md -->
---
title: "Client Script"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/client-script"
updated: "2026-02-17"
---

A Client Script lets you dynamically define a custom Form Script that is executed on a user's browser. If you choose to utilize non standard tools or libraries, make sure to test them on different browsers to ensure compatibility across your userbase.


> In Version 13, **Custom Script** was renamed to **Client Script**
> 
> 

1. How to create a Client Script
--------------------------------

To create a Client Script

1. To add/edit Client Script, ensure your role is System Manager.
2. Type "New Client Script" in the awesomebar and hit enter to create a new Client Script document.
3. Select the DocType whose form you wish to customize.
4. Update the script using the preset template and save.
5. Head over to the DocType you've customized and see the changes.

2. Features
-----------

As compared to the restrictive nature of Server Scripts, everything is fair game in Client Scripts. This is because the frontend APIs are secure by design. You can utilize all of JavaScript APIs, along with Frappe's and any other JS or CSS library you might've customized Desk with.


> The validations you add through Client Script will only be applied while using the standard form view accessible through the browser. In case you wish for those to be applied through API or [System Console](/framework/v14/user/en/desk/scripting/system-console) access too, use [Server Scripts](/framework/v14/user/en/desk/scripting/server-script).
> 
> 

3. Examples
-----------

### 3.1 Custom validation

Add additional form validations while creating or updating a document from Frappe's standard form view.


```
// additional validation on Task dates
frappe.ui.form.on('Task', 'validate', function(frm) {
    if (frm.doc.from_date < get_today()) {
        msgprint('You can not select past date in From Date');
    }
});
  

```
### 3.2 Fetching values on field updates

Fetch `local_tax_no` on changing value of the `customer` field.


```
cur_frm.add_fetch('customer', 'local_tax_no', 'local_tax_no');
  

```
### 3.3 Customize field properties

Make a field `ibsn` read only after creating the document.


```
// make a field read-only after saving
frappe.ui.form.on('Task',  {
    refresh: function(frm) {
        frm.set_df_property('ibsn', 'read_only', !frm.is_new());
    }
});
  

```
### 3.4 Customize field properties

Calculate incentives on a Sales Invoice form on save.


```
// calculate sales incentive
frappe.ui.form.on('Sales Invoice',  {
    validate: function(frm) {
        // calculate incentives for each person on the deal
        total_incentive = 0
        $.each(frm.doc.sales_team,  function(i,  d) {
            // calculate incentive
            let incentive_percent = 2;
            if(frm.doc.base_grand_total > 400) incentive_percent = 4;
            // actual incentive
            d.incentives = flt(frm.doc.base_grand_total) * incentive_percent / 100;
            total_incentive += flt(d.incentives)
        });
        frm.doc.total_incentive = total_incentive;
    }
});
```
### 3.5 Filter email recipients

You can restrict the available emails via a **Client Script**. Every form can specify what email addresses should be selectable. This reduces the cognitive load for the user and avoids sending emails to wrong recipients.

`CommunicationComposer` (the email dialog) will check if there is a **Client Script** supplying filters for the "recipients", "cc" and "bcc" fields. For example, if a **Quotation** should only show email addresses linked to the recipient of the **Quotation**, we can add the following script:


```
frappe.ui.form.on("Quotation", {
    get_email_recipient_filters: function (frm, field) {
        // field can be "recipients", "cc" or "bcc"
        if (field === "recipients") {
            return [
                [
                    "Dynamic Link",
                    "link_doctype",
                    "=",
                    frm.doc.quotation_to
                ],
                [
                    "Dynamic Link",
                    "link_name",
                    "=",
                    frm.doc.party_name
                ],
            ];
        }
    },
    // ...
};
```
The filters are referring to the **Contact** DocType and it's *Links* child table.

Even with filters, it remains possible to paste arbitrary recipients.

### 3.6 Set default email recipients

In standard processes like **Sales Order** -> **Delivery Note** -> **Sales Invoice**, the email recipients are often pre-defined. For example, this could be done in advance by the account manager.

You can set default email recipients via a **Client Script**. Every form can programmatically supply it's own default recipients.

`CommunicationComposer` (the email dialog) will check if there is a **Client Script** supplying default recipients. For example, if your **Quotation** DocType contains a field named *BCC* (`"custom_bcc"`), you can add the following **Client Script** to use it as default BCC in the email dialog:


```
frappe.ui.form.on("Quotation", {
    get_email_recipients: function (frm, field) {
        // field can be "recipients", "cc" or "bcc"
        if (field === "bcc") {
            return [frm.doc.custom_bcc]
        }
    },
    // ...
};
```
  

<!-- page: framework/framework__user__en__desk__scripting__script-api.md -->
---
title: "Script API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/script-api"
updated: "2026-02-17"
---

List of restricted commands that be called in Frappe Framework Server Script, Print Formats and Script Reports

**Note:** This is only applicable for in-app scripting. If you want more features, you will have to create an "Application" and write the event handlers inside Python Modules

### Python Modules

Following python modules are available

#### `json`

Python standard module `json`

### Formatting

#### _ (Translate)

Translate a string

Example: `_("This is translatable")`

#### frappe.format

Format a value based on its datatype

Example: `frappe.format_value(value, dict(fieldtype='Currency'))`

#### frappe.date_format

Format as default date format

#### frappe.format_date

Returns date as "1st September 2019"

### Session

#### frappe.form_dict

Form / request parameters

Example: Request parameter `/page?name="test"` can be accesssed as `frappe.form_dict.name`

#### frappe.request

Request object

#### frappe.response

Response object

#### frappe.session.user

Current user

#### frappe.session.csrf_token

CSRF token of the current session

#### frappe.user

Current user

#### frappe.get_fullname

Returns fullname of the current user

#### frappe.get_gravatar

Gets the user display image from `frappe.utils.get_gravatar_url`

#### frappe.full_name

Fullname of the current user

### Documents (ORM)

Document access and editing

#### frappe.get_meta

Get metadata object

#### frappe.new_doc

Create a new Document record.

#### frappe.get_doc

Get Document. You can also save or execute any method exposed by the document.

Example: `frappe.get_doc("User", frappe.session.user)`

#### frappe.get_last_doc

Get the last Document of a particular DocType with a given set of filters. Defaults to last created.

Example: `frappe.get_last_doc("User", filters={"name": ("like", "%@apple.com")})`

#### frappe.get_cached_doc

Get Document (or cached)

#### frappe.get_mapped_doc

#### frappe.rename_doc

#### frappe.delete_doc

#### frappe.get_system_settings

Get system default settings

### Database

Database access API

#### frappe.db.get_list

Get list of record filtered by current user's permissions

Example: `frappe.db.get_list("Customer")` will return list of customers

#### frappe.db.get_all

Get list of all records

#### frappe.db.sql

Run a SELECT query

Example: `frappe.db.sql("select name from Customer where name like 'm%'")`

#### frappe.db.get_value

Get a value from a record

Example: `frappe.db.get_value("User", frappe.session.user, "first_name")`

#### frappe.db.get_single_value

Get value from a single type document

Example: `frappe.db.get_single_value("System Settings", "default_currency")`

#### frappe.db.get_default

Get default value

#### frappe.db.escape

Sanitize value for database queries to prevent SQL injection

#### frappe.db.set_value

Set a value

#### frappe.db.exists

Checks for existence of a document. Returns `name` of the document if exists else `None`.

#### frappe.db.commit

Allow users to make explicit commits in server scripts like custom scheduler scripts.  
Note: This won't work in any DocType Event server scripts

#### frappe.db.rollback

Allow users to rollback changes via server scripts.  
Note: This won't work in any DocType Event server scripts

### Query Builder

#### frappe.qb

Query builder API to run SELECT queries.

Example: `frappe.qb.from_("Task").select("*").run()`

### Utilities

Utility methods and functions

#### run_script

Run a server script (return values in `frappe.flags`)

#### frappe.msgprint

Show a modal on the server side after as a part of the response.

Example: `frappe.msgprint("Hello")`

#### frappe.get_hooks

Get application hooks

#### frappe.utils

Methods in frappe.utils

#### frappe.render_template

Render a Jinja template

#### frappe.get_url

Get url of the current site via `frappe.utils.get_url`

#### socketio_port

Port for socketio

#### style.border_color

Returns '#d1d8dd'

#### guess_mimetype

Returns mimetypes.guess_type

#### html2text

Encode HTML as text (markdown)

#### dev_server

True if in developer mode

#### frappe.log_error

Generate Error Log with a traceback

#### FrappeClient

Connect to a Frappe site using a requests session

### API

Make external API calls from Frappe.

#### frappe.make_get_request

Make a GET request.

Example: `frappe.make_get_request('https://example.com')`

#### frappe.make_post_request

Make a POST request.

Example: `frappe.make_post_request('https://example.com', data={'username: 'test'})`

#### frappe.make_put_request

Make a PUT request.

Example: `frappe.make_put_request('https://example.com', headers={'Auth': 'Bearer xyz'})`

### Email

#### frappe.sendmail

Send an email. [See docs](https://frappeframework.com/docs/v14/user/en/api/utils#frappesendmail)

Example: `frappe.sendmail(recipients=['test@example.com'], sender='sender@example.com', subject='My Subject', message='<p>Hello</p>')`

<!-- page: framework/framework__user__en__desk__scripting__server-script.md -->
---
title: "Server Script"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/server-script"
updated: "2026-04-27"
---

> Note: Starting from version 15, Server Scripts are disabled by default to improve security on shared benches.
>
> You can enable them on your bench using following command.
>
> ```
> bench set-config -g server_script_enabled 1
> ```
>
> If you're hosted on Frappe Cloud you need to [create a private bench](https://frappecloud.com/docs/benches) in order to enable server scripts. Public shared benches DO NOT allow use of server scripts.





A Server Script lets you dynamically define a Python Script that is executed on the server on a document event or API

## How to create a Server Script

---

To create a Server Script

1. If your site is being hosted on [frappe cloud](https://frappe.io/cloud) here is the [help article](https://docs.frappe.io/cloud/enable-server-script) explaining the steps to enable server script, In case of self-hosted accounts, set `server_script_enabled` as true in site_config.json of your site.
2. To add/edit Server Script, ensure your role is System Manager.
3. Type "New Server Script" in the awesomebar and hit enter to create a new Server Script document.
4. Set the type of server script (Document Event / API).
5. Set the document type and event name, or method name, script and save.
6. Features

---

### 2.1 Enabling Server Script

Server script must be enabled via site_config.json

```
bench --site site1.local set-config server_script_enabled true
  

```

### 2.2 Document Events

For scripts that are to be called via document events, you must set the Reference Document Type and Event Name to define the trigger

- Before Insert
- After Insert
- Before Validate
- Before Save
- After Save
- Before Submit
- After Submit
- Before Cancel
- After Cancel
- Before Delete
- After Delete
- Before Save (Submitted Document)
- After Save (Submitted Document)
- Before Print

### 2.3 API Scripts

API endpoints can be created on the fly by using the **Script Type** `"API"`. The name of the endpoint depends on field **API Method**. All APIs created using Server Scripts will be automatically prefixed with `/api/method`.

For instance, a script with the **API Method** `"delete-note"` may be accessed via `/api/method/delete-note`. Using Frappe's frontend request library, you could use `frappe.call("delete-note")` in your client scripts.

Guest access may be enabled by checking **Allow Guest** for the created APIs. The response can be set via `frappe.response["message"]` object.

API server scripts also support IP-based rate limiting which you can enable by checking "Enable Rate Limit" and specifying how many calls can be made in a given time window.

### 2.3 Security

Frappe Framework uses the RestrictedPython library to restrict access to methods available for server scripts. Only the safe methods, listed below are available in server scripts.

For allowed methods, see [Script API](/framework/v14/user/en/desk/scripting/script-api)

### 2.4 Using Server Scripts as libraries

You can use a server script as an internal method by setting `frappe.flags` value in script.

### 2.5 Comparing changes

You can diff two versions of server scripts using "Compare Versions" button.

[Screenshot on the live page: Server script diff]



## Examples

---

### 3.1 Change the value of a property before change

Script Type: Before Save

```
if "test" in doc.description:
    doc.status = 'Closed'
  

```

### 3.2 Custom validation

Script Type: "Before Save"

```
if "validate" in doc.description:
    raise frappe.ValidationError
  

```

### 3.3. Auto Create To Do

Script Type: "After Save"

```
if doc.allocted_to:
    frappe.get_doc(dict(
        doctype = 'ToDo',
        owner = doc.allocated_to,
        description = doc.subject
    )).insert()
  

```

### 3.4 API

- Script Type: API
- Method Name: `test_method`

```
frappe.response['message'] = "hello"
  

```

Request: `/api/method/test_method`

### 3.5 Internal Library

> New in version 13

Call one (`script_1` script from another `script_2`)

Script 1:

```
frappe.flags.my_key = 'my value'
  

```

Script 2:

```
my_key = run_script('script_1').get('my_key')
  

```

<!-- page: framework/framework__user__en__desk__scripting__system-console.md -->
---
title: "System Console\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/system-console"
updated: "2026-02-17"
---

System Console helps you run Python commands for debugging based on [Script API](/framework/v14/user/en/desk/scripting/script-api)
. It is allowed only for users with role System Manager.

To access the System Console, search for it on the Search Bar.

[Screenshot on the live page: System Console]

### API

The methods exposed by the [Script API](/framework/v14/user/en/desk/scripting/script-api)
 can be accessed via the System Console

### Logging response

To print the response, use the `log` method.

<!-- page: framework/framework__user__en__desk__workspace.md -->
---
title: "Workspace"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace"
updated: "2026-02-17"
---

Workspace is the first page you land on when you log in.
It also has a dedicated sidebar where you can rearrange the workspace position according to your convenience.

The workspace itself is a tool to build user-specific pages. 
It comes with some standard workspaces which are listed in the `PUBLIC` section in the sidebar and are visible to all users.
You can also create private workspaces which will only be visible to the logged-in user(owner) in the `MY WORKSPACES` section. 

Let's build one and check out some cool features.

###Create New Workspace
1. Click on **Create Workspace** button.
2. Enter Title and click on Create.

[Screenshot on the live page: Create Workspace]

###Create Child Workspace
1. Click on **Create Workspace** button.
2. Enter Title.
3. Select Home in the Parent field and click on Create.

[Screenshot on the live page: Create Child Workspace]

###Workspace Blocks
The workspace block is a building block for the workspace page.
These blocks can be placed in different variations to build an ideal workspace for a specific use case.

[Learn More →](/framework/v14/user/en/desk/workspace/blocks)

[Screenshot on the live page: Workspace Blocks]
###Sidebar


[Screenshot on the live page: Workspace Sidebar]


There are two sections in the sidebar `MY WORKSPACES` & `PUBLIC`.


You can create as many private workspaces as you want.
It will only be visible to the currently logged-in user(owner) under the `MY WORKSPACES` section


All the standard workspaces comes under `PUBLIC` section. 
You can also create more public workspaces. These workspaces will be visible to all users.
 


[More →](/framework/v14/user/en/desk/workspace/customization#customizing-workspaces) 



>Only users with **Workspace Manager Role** can create, edit or delete public workspaces

###Customization
Workspace has two modes **Read Only Mode** and **Edit Mode**. You can start customizing your workspace by clicking on the **Edit** button.
[Customizing Workspaces](/framework/v14/user/en/desk/workspace/customization#customizing-workspaces) and [Customizing Workspace Page](/framework/v14/user/en/desk/workspace/customization#customizing-workspace-page) are two different things.

>Adding new blocks from the workspace document will not work as the new workspace doesn't know exactly where to add that block (at which position). You can update the existing blocks from the workspace document but it is not recommended either. The best practice would be to use the new workspace builder UI to do all kinds of customization.

<!-- page: framework/framework__user__en__desk__workspace__access.md -->
---
title: "Access"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/access"
updated: "2026-02-17"
---

Workspaces can be restricted based on Modules and Roles.

### Modules

Users can have access to different modules and standard workspaces are visible based on access to those modules.

In the below GIF you can see when Website Module access was removed for user John Doe, he was not able to see Website Workspace. [Screenshot on the live page: Module Access]  


### Roles

Users can have access to modules but what if you still want those users to not see the standard workspace of that module. Then you can restrict access based on the roles given to that user.

Check below Example:

Jack Doe is a manager with Workspace Manager Role. He only wants user with Website Manager Role to see the Website Workspace.ence such a configuration is made as follows: [Screenshot on the live page: Role Access 1]  


To test this, Jane Doe is given the Website Module access and not given the Website Manager role. Due to the configuration done above, she will not be able to see Website Workspace as shown below. Where as John Doe who has Website Module access and Website Manager role, will be able to see the Website Workspace. [Screenshot on the live page: Role Access 2]  


### Default Workspace

The default workspace that will be shown when the user first logs in can be configured for each user. By default, the user will be shown the workspace they were last in. The default workspace can be selected using the "Default Workspace" field of the User settings form, that can be accessed through the "My Settings" option of your avatar menu.

<!-- page: framework/framework__user__en__desk__workspace__blocks.md -->
---
title: "Blocks"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/blocks"
updated: "2026-04-14"
---

Blocks as the name suggest are the building blocks of the workspace.  
You can add different types of blocks, edit them, and arrange them as per your need to build a fully customizable workspace.

There are currently 9 blocks. We will keep adding new blocks in the coming future.





Let's go through each of them:



[Screenshot on the live page: Blocks]



### Heading

A heading block is used as a header for any section or paragraph.

[Screenshot on the live page: Section Header]

[Screenshot on the live page: Paragraph Header]

### Text

Text block is used as a paragraph or description for any section.

[Screenshot on the live page: Paragraph Block]

Both **Heading** and **Text** has an inline toolbar.  
Currently, we have limited tools like header size from H1 to H6, bold, italic and links.

[Screenshot on the live page: Inline Toolbar]

### Card

A card contains several links that can be used for quick navigation.  
The link item can be a DocType, Report or Page.

[Screenshot on the live page: Card Block]

### Chart

You can add any **Dashboard Chart** on the workspace using this block. 

[Screenshot on the live page: Chart Block]

### Shortcut

Shortcut block is used to quickly navigate to any DocType, Report or Page.

[Screenshot on the live page: Shortcut Block]

Shortcuts can be customized too.  
You can select the view in which it should open, and can add filters that will be applied when you open the selected view.  
You can see the number of records based on the filters applied on the shortcut as a pill.

[Screenshot on the live page: Shortcut Features]

### Spacer

It is used to add some space between two blocks.

[Screenshot on the live page: Spacer Block]

It can also be used to position other blocks by adding white space before or after the block.

[Screenshot on the live page: Spacer Separator]

[Screenshot on the live page: Spacer Separator Output]

### Onboarding

The onboarding block is used to guide first-time users when they land on your page.  
It has steps to follow to learn a specific module.  
For each step, there is some description on the right section or there can be a link to a video.

[Screenshot on the live page: Onboarding Block]

### Quick List

In the quick list block, we can see recently updated records of selected doctype.  
We can also add some filters.  
While in the read-only mode we have the option to refresh the list, update the applied filters, create a new record and open doctype's list view.

[Screenshot on the live page: Quick List Block]

### Number Card

You can add any existing **Number Card** on the workspace using this block.

[Screenshot on the live page: Number Card Block]

<!-- page: framework/framework__user__en__desk__workspace__customization.md -->
---
title: "Customization"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/customization"
updated: "2026-02-17"
---

Workspace has two modes **Read Only Mode** and **Edit Mode**. You can start customizing your workspace by clicking on the **Edit** button.
Customizing Workspaces and Customizing Workspace Page are two different things. 

##Customizing Workspaces
All customization done to the workspaces can be done through the sidebar except for creating a workspace.

Let's see what all customizations we can do:

###Edit workspace details
You can update the title, and icon, make it parent or child and can make it public or private.
[Screenshot on the live page: Edit Workspace Details]
###Create Duplicate
You can create a duplicate of an existing workspace and can add or remove some blocks from it as per your need.
[Screenshot on the live page: Duplicate Workspace]
###Delete Workspace
Delete an existing workspace.
[Screenshot on the live page: Delete Workspace]
###Hide Workspace
Hide your private workspaces.
[Screenshot on the live page: Hide Workspace As User]

Only `Workspace Manager` can hide public workspaces.
[Screenshot on the live page: Hide Workspace As Workspace Manager]

###Rearrange Position:
You can drag & drop the workspace from the sidebar to change its position or make it a child/parent workspace.
[Screenshot on the live page: Rearrage Workspace]

>**Save/Discard** buttons are only used to save workspace page customizations. All workspace changes done from the sidebar get saved as you make them.

##Customizing Workspace Page
Customizing blocks in a particular workspace comes under this category.

Let's see what all customizations we can do:

###Add a new block
[Screenshot on the live page: Add Block]
###Edit an existing block
[Screenshot on the live page: Edit Block]
###Remove or delete an existing block
[Screenshot on the live page: Delete Block]
###Resize the width of a block
[Screenshot on the live page: Resize Block]
###Rearrange the position of a block
[Screenshot on the live page: Rearrange Block]

<!-- page: framework/framework__user__en__discussions.md -->
---
title: "Discussions"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/discussions"
updated: "2026-02-17"
---

You can now add a discussions component on any web page of the portal. The discussions component allows logged in users to enter and share messages with other users. This component can be used for discussions or to setup a portal where users help each other with their queries.

[Screenshot on the live page: Discussions Component]

### Steps to Setup the Discussions Component

1. Open the web page document on which you want to add the discussions component or create a new web page and save it.
2. Scroll to the Page Building Blocks table.
3. Under Web Template select Discussions.
[Screenshot on the live page: Page Building Blocks]
4. Click on Edit values.
[Screenshot on the live page: Edit Values]
5. Enter a Title, CTA Title and select the Web Page as the current web page name.
6. You can check Single Thread if you want the discussion to be single threaded.
7. Save the page.

<!-- page: framework/framework__user__en__email-groups.md -->
---
title: "Email Groups"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/email-groups"
updated: "2026-02-17"
---

Email Groups are a powerful tool for managing and automating email communication with subscribers, clients, or any group of contacts.

The **Email Group** is created under the Email module, where it's set up with a unique title. Each **Email Group** is automatically named using the 'Title' field, ensuring easy identification and management. Managed primarily by the "Newsletter Manager" role, this ensures that only authorized personnel can create, modify, or delete the groups.

The *Total Subscribers* field dynamically displays the number of subscribers in the group, offering a quick view of the group's reach. **Email Groups** are linked to individual **Email Group Members**, allowing for easy management and segmentation of subscribers.

The *Confirmation Email Template* field links to a specific email template used for sending confirmation emails.

The *Welcome Email Template* is used for initial engagement with new subscribers. It is sent immediately after they have confirmed their email address and sets the tone for future communication.

After successful confirmation, subscribers can be directed to a custom *Welcome URL*. This can be a landing page or any relevant content, providing immediate engagement with the new subscriber. If the *Welcome URL* is not set, subscribers will be taken to a generic confirmation page.

The option to add query parameters to the *Welcome URL* enables personalized interactions and tracking of subscriber engagement.

[Screenshot on the live page: email_group_with_welcome_url]  

<!-- page: framework/framework__user__en__form-tours.md -->
---
title: "Form Tours"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/form-tours"
updated: "2026-02-17"
---

Frappe provides an easy way to generate form tutorials for your complex doctype with very little configuration.

[Screenshot on the live page: Form Tour]  


Creating a Form Tour
--------------------

To create a Form Tour, type "new form tour" in awesomebar and hit enter.

1. Enter Title. For eg., 'Creating a Custom Field'
2. Select Reference DocType.
3. Add steps defining each fields.
4. Save the document.

[Screenshot on the live page: Custom Field Form Tour] *A Tour to explain creation of Custom Fields*

Configuration Options
---------------------

### Form Tour

1. **Is Standard**: To make a standard Form Tour which will be stored as JSON. Can only be set while developer mode is on.
2. **Save on Completion**: If checked, the last step of the Form Tour will prompt the user to save the document.
3. **Show First Document Tour**: If you want to show the tour of an existing document instead of a new form, enable this. As the name suggests, it gives the tour of the very first document created for this DocType.
4. **Include Name Field**: For some doctypes, the name is set by the user. On enabling this, the name field becomes the first step of the tour.

### Form Tour Steps

1. **Field**: A field from the selected doctype. This will be highlighted with a Title & Description.
2. **Title** & **Description**: To describe the field for its use, impact, and other hidden wirings of the field.
3. **Position**: The position of the highlighting popover is decided by this field. There are multiple options to choose depending upon the position of the highlighted field.
4. **Next Condition**: A code field which expects a valid JS condition which applies on the document. For eg., for a Task DocType Tour, we can check if task priority is set before going to the next condition by setting next condition as follows:

`eval: doc.priority != ""`
5. **Is Table Field**: To be checked if the field to be highlighted is under a child table.
6. **Parent Field**: Table field from the selected doctype. Only visible if **Is Table Field** is checked. Allows user to select a child table field.

Triggering the Tours
--------------------

Once you are done describing the Form & its fields, you are now ready to trigger the tour by using Form API. You just have to initialize the tour with appropriate `tour_name` and then simply start the tour with `frm.tour.start()`.


```
frappe.ui.form.on('Your DocType', {
    onload: function(frm) {
        const tour_name = 'Your Form Tour Name';
        frm.tour.init({ tour_name }).then(() => frm.tour.start());
    }
});
```

<!-- page: framework/framework__user__en__guides.md -->
---
title: "Guides"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides"
updated: "2026-02-17"
---

Frappe is a full-stack "batteries included" framework. It has libraries and APIs for everything from authentication and scheduled jobs to managing different currencies, reports, as well as building forms.

In this section we will try and cover the most commonly used API on client and server side that will be useful for app development.

1. [Basics](/framework/v14/user/en/guides/basics/apps)
2. [App Development](/framework/v14/user/en/guides/app-development/custom_action_link_field)
3. [Deployment](/framework/v14/user/en/guides/deployment/packages)
4. [Reports and Printing](/framework/v14/user/en/guides/reports-and-printing/getting-information-from-another-document-in-print-format)
5. [Portal Development](/framework/v14/user/en/guides/portal-development/)
6. [Data](/framework/v14/user/en/guides/data/using-data-migration-tool)
7. [Integration](/framework/v14/user/en/guides/integration/google_gsuite)
8. [Database Settings](/framework/v14/user/en/guides/database-settings/setup-read-from-secondary-db)
9. [Automated Testing](/framework/v14/user/en/guides/automated-testing)
10. [Desk](/framework/v14/user/en/guides/desk)

<!-- page: framework/framework__user__en__guides__app-development__adding-custom-button-to-form.md -->
---
title: "Adding Custom Button To Form"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-custom-button-to-form"
updated: "2026-02-17"
---


To create a custom button on your form, you need to edit the javascript file associated to your doctype. For example, If you want to add a custom button to User form then you must edit `user.js`.

In this file, you need to write a new method `add_custom_button` which should add a button to your form.

#### Function Signature for `add_custom_button(...)`
 ```js
 frm.add_custom_button(__(buttonName), function() {
 // perform desired action such as routing to new form or fetching etc.
 }, __(groupName));
 ```

#### Example-1: Adding a button to User form
We should edit `frappe/core/doctype/user/user.js`

 ```js
 frappe.ui.form.on('User', {
    refresh: function(frm) {
        frm.add_custom_button(__('Get User Email Address'), function() {
            frappe.msgprint(frm.doc.email);
        }, __("Utilities"));
    }
 });
 ```

You should be seeing a button on user form as shown below,

[Screenshot on the live page: Custom Button]

<!-- page: framework/framework__user__en__guides__app-development__adding-module-icons-on-desktop.md -->
---
title: "Adding Module Icons On Desktop\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-module-icons-on-desktop"
updated: "2026-02-17"
---


> Frappe version 12

To create an icon for your app, you have to edit your app's `config/desktop.py`. In this file you can add a `get_data` method returns a dictionary with the module icon parameters.

You can also create a dropdown list of actions available on this module and actions available on the page when you click on this module. To achieve this, create a file `config/MODULE_NAME.py` (replace `MODULE_NAME` with the name of one of your app's modules).

## Example App Library Management

`config/desktop.py`:

```python
def get_data():
 return [
 {
 "module_name": "Library Management",
 "category": "Modules",
 "label": _("Library Management"),
 "color": "#589494",
 "icon": "octicon octicon-book",
 "type": "module",
 "description": "Library management"
 }
 ]
```

`config/library_management.py`:

```python
def get_data():
 return [
 {
 "label": _("Library Management"),
 "icon": "octicon octicon-book",
 "items": [
 {
 "type": "doctype",
 "name": "Article",
 "label": _("Article"),
 "description": _("Manage Books"),
 "onboard": 1,
 },
 {
 "type": "doctype",
 "name": "Library Member",
 "label": _("Library Member"),
 "description": _("Manage Members"),
 # Not displayed on dropdown list action but on page after click on module
 "onboard": 0,
 }
 ]
 }
 ]
```

Note: Module views are visible based on permissions.
