<!-- Frappe documentation: framework, part 18 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__guides__integration__webhooks.md -->
---
title: "Webhooks"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/integration/webhooks"
updated: "2026-02-17"
---


Webhooks are "user-defined HTTP callbacks". For a select DocType, you can create a webhook that triggers on specific document events under certain conditions, if required.

When the `doc_event` occurs, the source site makes an HTTP request to the URI configured for the webhook. Users can configure these webhooks to use events on one site to invoke behaviour on another.

## Configuring a Webhook

To add a Webhook, go to:

> Integrations > Webhook > Webhook

[Screenshot on the live page]

1. Select the DocType for which the Webhook needs to be triggered (e.g. `Quotation`).
1. Select the Doc Event that will trigger the Webhook (e.g. `on_update`).
1. Optionally, you can set additional document Conditions to trigger Webhooks for specific scenarios.
1. Enter a valid request URL that will receive the Webhook data.
1. Select the Request Method. `POST` is the default method.
1. Optionally, you can add HTTP headers to the request. (e.g. useful for sending an API key, if required).

You can also disable a webhook by unchecking the `Enabled` checkbox. Only webhooks that are enabled get triggered.

### Data Structure

- If your request structure is based on forms, you can select fields from the document in the table, which uses the fieldname as the `key`.
- If your request structure is based on JSON, you can insert fields from the document using jinja templating (make sure to wrap your fields with double-quotes).

### Webhook Security

To optionally add security to your webhook requests and ensure that the webhook is being sent from Frappe, you can set up a "Webhook Secret" along with the request. Do not share the secret publicly.

If enabled, an additional header (`X-Frappe-Webhook-Signature`) will be added to the request before it's sent out, with its value being generated from the secret as a base64-encoded HMAC-SHA256 hash of the payload.

### Example Webhook Request

- **DocType**: `Quotation`
- **Doc Event**: `on_update`
- **Request URL**: `https://httpbin.org/post`
- **Request Structure**: `Form URL-Encoded`
- **Webhook Headers**:
 1. **Key**: `Content-Type:`, **Value**: `application/x-www-form-urlencoded`
- **Webhook Data**:
 1. **Fieldname**: `name`, **Key**: `id`
 1. **Fieldname**: `items`, **Key**: `lineItems`

The above configuration creates the following JSON request (sent by a Frappe server on `Quotation` - `on_update` to https://httpbin.org/post):

```
{
 "args": {},
 "data": "{"lineItems": [{"stock_qty": 1.0, "base_price_list_rate": 1.0, "image": "", "creation": "2017-09-14 13:41:58.373023", "base_amount": 1.0, "qty": 1.0, "margin_rate_or_amount": 0.0, "rate": 1.0, "owner": "Administrator", "stock_uom": "Unit", "base_net_amount": 1.0, "page_break": 0, "modified_by": "Administrator", "base_net_rate": 1.0, "discount_percentage": 0.0, "item_name": "I1", "amount": 1.0, "actual_qty": 0.0, "net_rate": 1.0, "conversion_factor": 1.0, "warehouse": "Finished Goods - R", "docstatus": 0, "prevdoc_docname": null, "uom": "Unit", "description": "I1", "parent": "QTN-00001", "brand": null, "gst_hsn_code": null, "base_rate": 1.0, "item_code": "I1", "projected_qty": 0.0, "margin_type": "", "doctype": "Quotation Item", "rate_with_margin": 0.0, "pricing_rule": null, "price_list_rate": 1.0, "name": "QUOD/00001", "idx": 1, "item_tax_rate": "{}", "item_group": "Products", "modified": "2017-09-14 17:09:51.239271", "parenttype": "Quotation", "customer_item_code": null, "net_amount": 1.0, "prevdoc_doctype": null, "parentfield": "items"}], "id": "QTN-00001"}",
 "files": {},
 "form": {},
 "headers": {
 "Accept": "*/*",
 "Accept-Encoding": "gzip, deflate",
 "Connection": "close",
 "Content-Length": "1075",
 "Host": "httpbin.org",
 "User-Agent": "python-requests/2.18.1"
 },
 "json": {
 "id": "QTN-00001",
 "lineItems": [
 {
 "actual_qty": 0.0,
 "amount": 1.0,
 "base_amount": 1.0,
 "base_net_amount": 1.0,
 "base_net_rate": 1.0,
 "base_price_list_rate": 1.0,
 "base_rate": 1.0,
 "brand": null,
 "conversion_factor": 1.0,
 "creation": "2017-09-14 13:41:58.373023",
 "customer_item_code": null,
 "description": "I1",
 "discount_percentage": 0.0,
 "docstatus": 0,
 "doctype": "Quotation Item",
 "gst_hsn_code": null,
 "idx": 1,
 "image": "",
 "item_code": "I1",
 "item_group": "Products",
 "item_name": "I1",
 "item_tax_rate": "{}",
 "margin_rate_or_amount": 0.0,
 "margin_type": "",
 "modified": "2017-09-14 17:09:51.239271",
 "modified_by": "Administrator",
 "name": "QUOD/00001",
 "net_amount": 1.0,
 "net_rate": 1.0,
 "owner": "Administrator",
 "page_break": 0,
 "parent": "QTN-00001",
 "parentfield": "items",
 "parenttype": "Quotation",
 "prevdoc_docname": null,
 "prevdoc_doctype": null,
 "price_list_rate": 1.0,
 "pricing_rule": null,
 "projected_qty": 0.0,
 "qty": 1.0,
 "rate": 1.0,
 "rate_with_margin": 0.0,
 "stock_qty": 1.0,
 "stock_uom": "Unit",
 "uom": "Unit",
 "warehouse": "Finished Goods - R"
 }
 ]
 },
 "url": "https://httpbin.org/post"
}
```

### Example _JSON Request Body_

For a Webhook on a sales transaction, we could construct the JSON data as follows: 

```JSON
{
 "id": "{{ doc.name }}",
 "total": "{{ doc.total }} EUR",
 "total_net_weight": "{{ doc.total_net_weight }} kg",
 "customer": "{{ doc.customer }}",
 "created": "{{ doc.creation }}",
 "items": {{ doc["items"] | tojson }}
}
```

### Webhook Request Log

A webhook request log is created for every successful request with all the relevant details

[Screenshot on the live page]

<!-- page: framework/framework__user__en__guides__portal-development.md -->
---
title: "Pages\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development"
updated: "2026-02-17"
---


You can make your website by adding pages to the `/www` folder of your website. The urls of your site will match the path of your pages within the `/www` folder.

Pages must be `.html` or `.md` (Markdown) files. Basic HTML template is provided in frappe in `frappe/templates/base_template.html`

<!-- page: framework/framework__user__en__guides__portal-development__adding-pages.md -->
---
title: "Adding Pages\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/adding-pages"
updated: "2026-02-17"
---


To add pages, just add `.html` or `.md` files in the `www` folder. The pages must only have the content, not the `` and `` tags.

You can also write markdown pages

### Index

The first file in a folder must be called `index.md` or `index.html`

Either file must be present for the system to make this a valid folder to build pages.

### Markdown

 # This is a title

 This is some page content
 a [link](/link/to/page)

### Adding Links

Links urls to pages can be given without the `.html` extension for example `/home/link`

### Title

The first `` block if present will be the page title if not specified in a special tag. If no `
====================================================================================

` or title is specified, the file name will be the title.

### Adding CSS

You can also add a `.css` file with the same filename (e.g. `index.css` for `index.md`) that will be rendered with the page.

### Special Tags

1. `` will make the page render in Jinja
2. `` will add a custom title
3. `` will not add breadcrumbs in the page
4. `` will enable caching (if you have used Jinja templating)
==========================================================================================================================================================================================================================================================================================================================================================================================================

<!-- page: framework/framework__user__en__guides__portal-development__context.md -->
---
title: "Dynamic Pages\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/context"
updated: "2026-02-17"
---


You can render pages dynamically using Jinja templating language. To query data, you can update that `context` object that you pass to the template.

This can be done by adding a `.py` file with the same filename (e.g. `index.py` for `index.md`) with a `get_context` method.

### Example

If you want to show a page to see users, make a `users.html` and `users.py` file in the `www/` folder.

In `users.py`:

```python
import frappe
def get_context(context):
 context.users = frappe.get_list("User", fields=["first_name", "last_name"])
```

In `users.html`:

```html
### List of Users



{% for user in users %}
 2. {{ user.first_name }} {{ user.get("last_name", "") }}

{% endfor %}


```

<!-- page: framework/framework__user__en__guides__portal-development__generators.md -->
---
title: "Generators"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/generators"
updated: "2026-02-17"
---

If every document in a table (DocType) corresponds to a web-page, you can setup generators.

To setup a generator you must:

1. Add a field `route` that specifies the route of the page
2. Add a condition field to indicate whether a page is viewable or not.
3. Add the doctype name in `website_generators` in `hooks.py` of your app.
4. Subclass the controller from `frappe.website.website_generator.WebsiteGenerator`
5. Create a template for your page
6. Add custom properties (context) for the template
7. Customize route and list view

Let us see this with the help of an example:

Example
-------

#### 1. Add fields

We added `published`, `route` in the DocType

**Note:** The field `route` is mandatory

[Screenshot on the live page: Generator fields]  


#### 2. Added Website Generator to Hooks

Since Job Opening is in `erpnext`, we have added to the list of existing generator hooks:


```
website_generators = ["Item Group", "Item", "Sales Partner", "Job Opening"]
  

```
If the `website_generators` property does not exist in your hooks.py, add it!

#### 3. Controller

We add the `website` property to the **JobOpening** class in `job_opening.py`

In `get_context`, `parents` property will indicate the breadcrumbs


```
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

# subclass from WebsiteGenerator, not Document
class JobOpening(WebsiteGenerator):
    website = frappe._dict(
        template = "templates/generators/job_opening.html",
        condition_field = "published",
        page_title_field = "job_title",
    )

    def get_context(self, context):
        # show breadcrumbs
        context.parents = [{'name': 'jobs', 'title': _('All Jobs') }]
  

```
**Note:** Once you do this, you should see the "See in Website" link on the document form.

#### 4. Add the template

Add the template in `erpnext/templates/generators/job_opening.html`


```
{% raw %}{% extends "templates/web.html" %}

{% block breadcrumbs %}
    {% include "templates/includes/breadcrumbs.html" %}
{% endblock %}

{% block header %}
<h1>{{ job_title }}</h1>
{% endblock %}

{% block page_content %}

<div>{{ description }}</div>

<a class="btn btn-primary" href="/job_application?job_title={{ doc.job_title }}">
    {{ _("Apply Now") }}</a>

{% endblock %}
{% endraw %}
  

```
#### 5. Customizing List View

If you add a method `get_list_view` in the controller file (job_opening.py), you can set properties for the listview


```
def get_list_context(context):
    context.title = _("Jobs")
    context.introduction = _('Current Job Openings')
  

```

<!-- page: framework/framework__user__en__guides__portal-development__ordering.md -->
---
title: "Ordering\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/ordering"
updated: "2026-02-17"
---


You can defining the ordering of pages in index by defining the index.txt file in your folder. The index.txt file must have the names (without extensions) of the pages in that folder indicating the order.

For example for this folder the `index.txt` looks like:

 adding-pages
 ordering
 contents
 context
 building

<!-- page: framework/framework__user__en__guides__portal-development__portal-roles.md -->
---
title: "Portal Roles\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/portal-roles"
updated: "2026-02-17"
---


Version: 7.1+

Roles can be assigned to Website Users and they will see menu based on their role

1. A default role can be set in **Portal Settings**
1. Each Portal Menu Item can have a role associated with it. If that role is set, then only those users having that role can see that menu item
1. Rules can be set for default roles that will be set on default users on hooks

[Screenshot on the live page: Portal Settings]

#### Rules for Default Role

For example if the Email Address matches with a contact id, then set role Customer or Supplier:

 default_roles = [
 {'role': 'Customer', 'doctype':'Contact', 'email_field': 'email_id',
 'filters': {'ifnull(customer, "")': ('!=', '')}},
 {'role': 'Supplier', 'doctype':'Contact', 'email_field': 'email_id',
 'filters': {'ifnull(supplier, "")': ('!=', '')}},
 {'role': 'Student', 'doctype':'Student', 'email_field': 'student_email_id'}
 ]

<!-- page: framework/framework__user__en__guides__portal-development__redirects.md -->
---
title: "Redirects"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/redirects"
updated: "2026-02-17"
---

You can add redirects by adding the `website_redirects` hook.

The optional field `redirect_http_status` will allow you to specify a custom HTTP status code to use for the redirect - if not specified, the fallback is 301

### Examples


```
website_redirects = [
    # absolute location
    {"source": "/from", "target": "https://mysite/from"},

    # relative location
    {"source": "/from", "target": "/main", "redirect_http_status": 307},

    # use regex
    {"source": "/from/(.*)", "target": "/main/\1"}
]
  

```
  

<!-- page: framework/framework__user__en__guides__portal-development__table-of-contents.md -->
---
title: "Table of Contents\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/table-of-contents"
updated: "2026-02-17"
---


You can add a table of contents by adding `{index​}` string on a new line.

You can also make Previous and Next buttons by adding `previous` or `next` in `{}`

### Showing contents

 # This is a title

 Hello paragraph

 ### Contents:

 {index​} will render as a numbered list of pages, but works only in `index.md` or `index.html`.

 {next​} for this Page will render as:

 {next}

<!-- page: framework/framework__user__en__guides__portal-development__web-forms.md -->
---
title: "Customizing Web Forms"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/portal-development/web-forms"
updated: "2026-02-17"
---

Web Forms are a powerful way to add forms to your website. Web forms are powerful and scriptable and from Version 7.1+ they also include tables, paging and other utilities

[Screenshot on the live page: Web Form]  


### Standard Web Forms

If you check on the "Is Standard" checkbox, a new folder will be created in the `module` of the Web Form for that web form. In this folder, you will see a `.py` and `.js` file that you can customize the web form with.

### Web Form Settings

* **Allow Edit**: Allow each user to have one instance and edit it
* **Allow Multiple**: Allow users to view and edit multiple instances of the web form
* **Show as Grid**: Show table view of the web form values (only if "Allow Multiple" is set)
* **Allow Incomplete Forms**: For very long forms, you can allow the user to save without throwing validation for mandatory. The user will still see the fields as manadatory.

### Client Script

You can also add a custom client script to the web form

API
---

##### Event Handler

Write an event handler to do actions when a field is changed.


```
frappe.web_form.on([fieldname], [handler]);
  

```
##### Get Value

Get value of a particular field


```
value = frappe.web_form.get_value([fieldname]);
  

```
##### Set Value

Set value of a particular field


```
frappe.web_form.set_value([fieldname], [value])
  

```
##### Validate

`frappe.web_form.validate` is called before the web_form is saved. Add custom validation by overriding the `validate` method. To stop the user from saving, return `false`;


```
frappe.web_form.validate = () => {
    // return false if not valid
}
  

```
##### Set Field Property


```
frappe.web_form.set_df_property([fieldname], [property], [value]);
  

```
##### Trigger script when form is loaded

Initialize form with customisation after it is loaded


```
frappe.web_form.after_load = () => {
    // init script here
}
  

```
Examples
--------

##### Reset value if invalid


```
frappe.web_form.on('amount', (field, value) => {
    if (value < 1000) {
        frappe.msgprint('Value must be more than 1000');
        field.set_value(0);
    }
});
  

```
##### Custom Validation


```
frappe.web_form.validate = () => {
    let data = frappe.web_form.get_values();
    if (data.amount < 1000) {
        frappe.msgprint('Value must be more than 1000');
        return false;
    }
});
  

```
##### Hide a field based on value


```
frappe.web_form.on('amount', (field, value) => {
    if (value < 1000) {
        frappe.web_form.set_df_property('rate', 'hidden', 1);
    }
});
  

```
##### Show a message on startup


```
frappe.web_form.after_load = () => {
    frappe.msgprint('Please fill all values carefully');
}
  

```
### Breadcrumbs

You can customize the breadcrumbs in a Web Form by adding JSON object.

Example:


```
[{"label": "Home", "route":"/" }]
  

```

<!-- page: framework/framework__user__en__guides__reports-and-printing__getting-information-from-another-document-in-print-format.md -->
---
title: "Getting Information From Another Document In Print Format"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/reports-and-printing/getting-information-from-another-document-in-print-format"
updated: "2026-02-17"
---

In a print format, you can get data from another document. For example, if you have a field called `sales_order` in Sales Invoice, then you can get the sales order details using `frappe.get_doc`:


```
{% set sales_order_doc = frappe.get_doc("Sales Order", sales_order) %}

{{ sales_order_doc.customer }}
```

<!-- page: framework/framework__user__en__guides__reports-and-printing__how-to-make-query-report.md -->
---
title: "How To Make Query Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/reports-and-printing/how-to-make-query-report"
updated: "2026-02-17"
---


You can create tabulated reports using complex SQL queries by creating a new Report. These reports can be created by a System Manager and are stored in the Database

> Note: You will need System Manager Permissions for this.

To create a new Query Report:

### 1. Create a new Report

[Screenshot on the live page: Query Report]

1. Set type as "Query Report"
1. Set the reference DocType - Users that have access to the reference DocType will have access to the report
1. Set the module - The report will appear in the "Custom Reports" section of the module.
1. Add your Query

### 2. Set the Query

You can define complex queries such as:


 SELECT
 `tabProduction Order`.name as "Production Order:Link/Production Order:200",
 `tabProduction Order`.creation as "Date:Date:120",
 `tabProduction Order`.production_item as "Item:Link/Item:150",
 `tabProduction Order`.qty as "To Produce:Int:100",
 `tabProduction Order`.produced_qty as "Produced:Int:100"
 FROM
 `tabProduction Order`
 WHERE
 `tabProduction Order`.docstatus=1
 AND ifnull(`tabProduction Order`.produced_qty,0) = `tabProduction Order`.qty
 AND EXISTS (SELECT name from `tabStock Entry` where production_order =`tabProduction Order`.name)

1. To format the columns, set labels for each column in the format: [Label]:[Field Type]/[Options]:[Width]

### 3. Check the Report

[Screenshot on the live page: Query Report]

### 4. Advanced (adding filters)

If you are making a standard report, you can add filters in your query report just like [script reports](https://frappe.io/docs/v14/user/en/guides/reports-and-printing/how-to-make-script-reports) by adding a `.js` file in your query report folder. To include filters in your query, use `%(filter_key)s` where your filter value will be shown.

For example

 SELECT ... FROM ... WHERE item_code = %(item_code)s ORDER BY ...

---

### Note: Standard Script Report

If you are developing a standard report for an app, make sure to set "Is Standard" as "Yes"

<!-- page: framework/framework__user__en__guides__reports-and-printing__how-to-make-script-reports.md -->
---
title: "Script Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/reports-and-printing/how-to-make-script-reports"
updated: "2026-06-04"
---

You can create tabulated reports using server side scripts by creating a new Report.

> Note: You will need Administrator Permissions for this.

Since these reports give you unrestricted access via Python scripts, they can only be created by Administrators. The script part of the report becomes a part of the repository of the application. If you have not created an app, read this.

> Note: You must be in Developer Mode to do this

### 1. Create a new Report

[Screenshot on the live page: Script Report]

1. Set Report Type as "Script Report"
2. Set "Is Standard" as "Yes"
3. Select the Module in which you want to add this report
4. In the module folder (for example if it is Accounts in ERPnext the folder will be `erpnext/accounts/report/[report-name]`) you will see that templates for the report files will be created.
5. In the `.js` file, you can set filters for the reports
6. In the `.py` file, you can write the script that will generate the report

### 2. Add Filters

You can add filters in the `.js`. See an example below:

```javascript
frappe.query_reports["Accounts Receivable"] = {
    "filters": [
        {
            "fieldname":"company",
            "label": ("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.getuserdefault("company")
        },
    ]
}
```

1. These properties are the same as you would set in a DocField in a DocType

### 3. Add the Script

In the `.py` file you can add the script for generating the report.

1. In the `execute` method, two lists `columns` and `data` are returned
2. Columns must be a list of dictionaries containing fields like fieldname, label, fieldtype, options,width. For example:

```python
[
	{
		"fieldname": "account",
		"label": _("Account"),
		"fieldtype": "Link",
		"options": "Account",
		"width": 300,
	},
	{
		"fieldname": "currency",
		"label": _("Currency"),
		"fieldtype": "Link",
		"options": "Currency",
	},
]
```

1. You can use all server side modules to build your report.
2. For example see existing reports. (Balance Sheet)

### 4. Add link for your report on the module page

[Screenshot on the live page: Module Page]

1. In the module folder (for example if it is Accounts in ERPNext the folder will be `erpnext/config/accounts.py`) you will see labels and items for various sections. The new report can be added in the item list as show in the example:

```python
def get_data():
	return [
		{
			"label": _("Accounting Statements"),
			"items": [
				{
					"type": "report",
					"name": "Balance Sheet",
					"doctype": "GL Entry",
					"is_query_report": True,
				}
			],
		}
	]
```

## Prepared Reports

Some script reports take too long to run in the browser. **Prepared Report** moves execution to a background job so users are not blocked while the report runs.

When *Prepared Report* is checked on a **Report**, each run is queued instead of executed synchronously. The user sees a progress indicator and gets a notification when the result is ready. Completed results are stored as **Prepared Report** documents and can be reopened later with the same filters.

*Prepared Report* also unlocks:

- *Generate CSV* — optionally produce a CSV attachment alongside the JSON result
- *Timeout (In Seconds)* — how long the background job may run before it is considered failed (default: 1500 seconds)

Prepared reports are intended for reports that are slow but stable. Users should expect to wait and come back for the result, not get an instant table in the browser.

<!-- page: framework/framework__user__en__guides__reports-and-printing__print-format-for-reports.md -->
---
title: "Report Print Formats"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/reports-and-printing/print-format-for-reports"
updated: "2026-02-17"
---


In version 4.1 we introduce Report Print Formats. These are HTML templates that you can use to format Query Report data for printing.

### 1. Creating New Print Formats

To create a new Print Format, just drop in a `.html` file in the folder of the query report. For example, for the [General Ledger](https://github.com/frappe/erpnext/tree/develop/erpnext/accounts/report/general_ledger) report in ERPNext, you can drop in a file called `general_ledger.html` along side the `.js` and `.py` files.

##### Tree Of `erpnext/accounts/general_ledger`

 
 ```
 general_ledger/
 ├── __init__.py
 ├── general_ledger.html
 ├── general_ledger.js
 ├── general_ledger.json
 └── general_ledger.py
 ```


### 2. Templating

For templating, we use an adapted version of [John Resig's microtemplating script](http://ejohn.org/blog/javascript-micro-templating/). If you know Javascript, it is very easy to follow this templating language.

##### Here are some examples (from John Resig's Blog):

Example: Properities:

```
[Screenshot on the live page]

**[<%=from_user%>](<%=from_user%>):** <%=text%>
```


Example: Code structures, Loops

 ```markdown
 <% for ( var i = 0; i < users.length; i++ ) { %>
 - [<%=users[i].name%>](<%=users[i].url%>)
 <% } %>
 ```

> **Note**: It is important to note that you should not use single quotes (') in your template as the engine cannot handle them effectively.

### 3. Data

Data is available to the template as:

- `data`: this is a list of records, with each record as an object with slugified properties from labels. For example "Posting Date" becomes "posting_date"
- `filters`: filters set in the report
- `report`: reportview object

### 4. Example

Here is how the General Ledger Report is built:

[General Ledger Print Format Template](https://github.com/frappe/erpnext/blob/develop/erpnext/accounts/report/general_ledger/general_ledger.html)

Here is what the report looks like:

[Screenshot on the live page: General Ledger]

##### Comments:

1. [Bootstrap Stylesheet](http://getbootstrap.com) is pre-loaded.
1. You can use all global functions like `fmt_money` and dateutil.
1. Translatable strings should be written as `__("text")`
1. You can create modules and import using `{% include "templates/includes/formats/common_format" %}`

<!-- page: framework/framework__user__en__guides__reports-and-printing__where-do-i-find-standard-print-formats.md -->
---
title: "Where Do I Find Standard Print Formats\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/reports-and-printing/where-do-i-find-standard-print-formats"
updated: "2026-02-17"
---

Standard Print formats are **auto generated** from the layout of the DocType. You can customize the standard format by

#### 1\. Customizing Standard Print

Go to **Setup > Customize > Customize Form View** and you can:

1. Re-arranging fields by dragging and dropping
2. Add static elements by adding **HTML** type fields and adding your HTML in **Options**
3. Hiding fields by setting the **Print Hide** property

#### 2\. Creating new layouts based on Print Formats

As there are not templates that are generated for standard Print Formats, you will have to create new templates from scratch using the [Jinja Templating Language](http://jinja.pocoo.org/) via

**Setup > Printing and Branding > Print Format**

1. [See Print Format help](https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/print-format).
2. You can use the [Bootstrap CSS framework](http://getbootstrap.com) to layout your print formats

**Tip: You can import [Standard Template macros](https://github.com/frappe/frappe/blob/develop/frappe/templates/print_formats/standard_macros.html) for building your print formats.**

Example, adding the standard header:

```
{%- from "templates/print_formats/standard_macros.html" import add_header -%}

{{ add_header() }}
```

<!-- page: framework/framework__user__en__hidden-features__desk.md -->
---
title: "Desk"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/hidden-features/desk"
updated: "2026-02-17"
---

## Quick Select Rows on Frappe List View

- Click on the checkbox and drag through the rows to select multiple rows.
- To unselect, again click and drag on the selected rows.

[Screenshot on the live page: Frappe List View]

## Quick View Database Field Name

- When viewing a form, hold down `alt` and hover over fields to field name as it is stored in the database.

[Screenshot on the live page]

<!-- page: framework/framework__user__en__how_to_contribute.md -->
---
title: "Contribute to Documentation for Frappe Apps"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/how_to_contribute"
updated: "2026-02-17"
---

The documentation for Frappe Apps is maintained in Frappe Wiki. This allows each community member to contribute documentation of a new application or enhance the existing ones. Just like a Wiki community, there are editors and reviewers. As an individual, you can build your reputation by editing documentation for the new features and enhancements, till graduating to the reviewer's role.

## Steps to contribute to the documentation

### Login and Access page

Before editing documentation, ensure to sign up. You can login/sign up from [here](https://docs.frappe.io/login).

Once logged in, you will be able to see the option for editing existing doc pages.

### Editing a Page

At the bottom of the page, click the ellipsis menu (...) and choose `edit`.
 
#### Markdown Editor

On clicking the Edit button, you should see a UI like this[Screenshot on the live page]

Now you can edit the markdown code and check the preview on the \`Preview Tab\`[Screenshot on the live page]

### WYSIWYG Editor

If you do not want to edit markdown and want to edit via the WYSIWYG Editor, click on the switcher and choose Rich-Text[Screenshot on the live page]

#### Uploading Media In Markdown

Step for uploading images in Markdown mode.

 1. Click on the “add attachment” button to upload an image
 2. Use the copy link button to get the link copied! [](https://docs.erpnext.com/files/CJr6HKz.png)
 3. Then paste the link in the editor to display the image

#### In WYSIWYG editor

Step for uploading images in WYSIWYG mode

1. You can either paste a copied image
2. List item: Drag and drop an image
3. Use the image button on top of the editor

### Submit a Doc

After editing the file, click on the Submit button and wait for your change to get submitted. Once submitted, you will see this screen[Screenshot on the live page]

On this screen, you can track all your contributions and wait for a reviewer to review your changes and either approve, reject or request changes.

You can click on open contribution to continue your work or use the comment system to communicate with the reviewer.

## Create a New Wiki Page

If you want to create a new page instead of editing a page, you will find the New Page link at the bottom of the Left Sidebar. The process is then similar to editing.

### Editing Sidebar

You can also drag and drop sidebars on the edit/ new page to rearrange them(Use this only when necessary)[Screenshot on the live page]

Hoping to see lots of contributions!

<!-- page: framework/framework__user__en__installation.md -->
---
title: "Installation"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/installation"
updated: "2026-08-24"
---

## System Requirements

This guide assumes you are using a personal computer, VPS or a bare-metal server. You also need to be on a \*nix system, so any Linux Distribution and macOS is supported. If you're a Windows user, you could use Ubuntu in WSL. We officially support only the following distributions.

1. macOS
2. Debian / Ubuntu

> Learn more about the architecture here. 

## Pre-requisites


| Dependency     | Frappe v14/v15 | Frappe v16/develop |
| -------------- | -------------- | ------------------ |
| MariaDB        | 10.6.6+        | 11.8               |
| Python         | 3.10+          | 3.14               |
| NodeJS         | 18+            | 24                 |
| Redis / valkey | 6              | 6+                 |
| Yarn           | 1.12+          | 1.22+              |
| pip            | 20+            | 25.3+              |


- wkhtmltopdf: version 0.12.6 with patched qt - for pdf generation
- cron: bench's scheduled jobs - automated certificate renewal, scheduled backups

### macOS

Install command line version of Xcode tools.

```
xcode-select --install
```

Install Homebrew. It makes it easy to install packages on macOS.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

(It may prompt you to run some additional commands at the end, which will ensure `brew` is available in your PATH)

Install wkhtmltopdf

```
curl -L https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-2/wkhtmltox-0.12.6-2.macos-cocoa.pkg -O

installer -pkg wkhtmltox-0.12.6-2.macos-cocoa.pkg -target ~
```

Now, you can easily install the required packages by running the following command

```
brew install git redis mariadb@11.8 pkg-config mariadb-connector-c
```

If you plan to use PostgreSQL instead of MariaDB, then you can include `postgresql`

During this installation you'll be prompted to set the MySQL root password. If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command:

```
sudo mariadb-secure-installation
```

> Remember: only run it if you're not prompted the password during setup.
>
>

Then, move on to the common steps

### Debian / Ubuntu

You should be running Debian 13+ or Ubuntu 24.04+, otherwise you may have issues with some of the packages.

Update your system's package index

```
sudo apt update
```

Install `git`, `redis`, and `mariadb`

```
sudo apt install git redis-server libmariadb-dev mariadb-server mariadb-client pkg-config
```

During this installation you'll be prompted to set the MySQL root password. If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command:

```
sudo mariadb-secure-installation
```

> Remember: only run it if you're not prompted the password during setup.
>
>

It is really important that you remember this password, since it'll be useful later on.

**Install wkhtmltopdf**

```
sudo apt install xvfb libfontconfig
```

Download and install wkhtmltopdf package from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html), then run this command to install the package.

```
sudo dpkg -i wkhtmltox_file.deb
```

### Common dependencies

**Install nvm, node, and yarn**

We recommend installing node using nvm

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

After nvm is installed, you may have to close your terminal and open another tab/window, or `source` your shell's rc file (example: `~/.bashrc` or `~/.zshrc`. Then run the following command to install node.

```
nvm install 24
```

Verify the installed version, by running:

```
$ node -v
v24.12.0
```

Finally, install `yarn` using `npm`

```
npm install -g yarn
```

\*\* Install uv and python \*\*

We recommend using python using uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After uv is installed, you may have to close your terminal and open another tab/window, or `source` your shell's rc file (example: `~/.bashrc` or `~/.zshrc`. Then run the following command to install python.

```
uv python install 3.14 --default
```

Alternatively, you can choose between 3.10-3.13 for version 15.

## Install Bench CLI

Install bench via pip

```
uv tool install frappe-bench
```

Confirm the bench installation by checking the version

```
bench --version
```

Create your first bench.

```
mkdir ~/frappe
cd ~/frappe
bench init my-bench
```

Congratulations, you have installed bench onto your system.

<!-- page: framework/framework__user__en__integration__google_drive.md -->
---
title: "Google Drive"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/integration/google_drive"
updated: "2026-02-17"
---

Google Drive is a file storage and synchronization service developed by Google. It allows users to store, synchronize and share files. Google Drive is a key component of Google Workspace, Google's monthly subscription offering for businesses.

You can use Frappe Framework's file picker to select any file from Google Drive and attach it to the current DocType. For example, you can attach the invoice PDF stored in Google Drive to a **Purchase Invoice** in your Frappe app.

Setup
-----

### Google Cloud Console

First we need to get some credentials that will allow us to access Google Drive. You can [use the setup tool](https://console.cloud.google.com/flows/enableapi?apiid=picker&credential=client_key), which guides you through creating a project in the Google Cloud Console, enabling the API, and creating credentials.

If you haven't done so already, create your application's API key by clicking **Create credentials > API key**. Next, look for your API key in the **API keys** section. You can open the API Key and restrict it.

1. Under **Application restrictions** choose "HTTP referrers",
2. under **Website restrictions** add your frappe instance's hostname and
3. under **API restrictions** choose "Restrict key" and select the "Google Picker API".

[Screenshot on the live page: API Key configuration]  


If you haven't done so already, create your OAuth 2.0 credentials by clicking **Create credentials > OAuth client ID**.

1. Under **Application type** choose "Web application" and
2. under **Authorized JavaScript origins** add your frappe instance's hostname.

[Screenshot on the live page: OAuth Client configuration]  


After you've created the credentials, you can see your client ID on the [Credentials page](https://console.cloud.google.com/apis/credentials).

Last but not least you need to configure the [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent). This is the page that users will see when they are using the Google Drive Picker for the first time. It asks them to grant access to their Google Drive. You can configure this as you like, just take care to add the scope `https://www.googleapis.com/auth/drive.readonly` on the **Scopes** page.

You will also need your App ID at hand. This is your project number which you can find under **IAM & Admin > Settings**.


> Portions of this section are modifications based on work created and [shared by Google](https://developers.google.com/picker/docs) and used according to terms described in the [Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
> 
> 

### Frappe instance

Now that the Google Picker API is enabled and we have the necessary credentials we can go ahead and configure the **Google Settings** in you Frappe instance.

1. Open **Google Settings**.
2. Check the *Enable* checkbox.
3. In the "Google Drive Picker" section, check the *Google Drive Picker Enabled* checkbox.
4. Enter your *App ID,* *Client ID* and *API Key*.
5. Save the **Google Settings** and reload your browser window.

[Screenshot on the live page: Google Settings]  


Now when you click on "Attach file" in the sidebar, you should see the Google Drive icon.

[Screenshot on the live page: Attach File Dialog]  


If you click on it for the first time, you have to authorize the Frappe app to access your Google Drive files.

[Screenshot on the live page: Google Sign In]  


Then the Google Drive Picker opens and you can choose a file.

[Screenshot on the live page: Google Drive Picker]  


Click the blue button on the bottom left to attach a link to this file to the current DocType.

[Screenshot on the live page: File Attached to DocType]  



> In case you're looking for technical details, Google Drive was introduced in [Pull Request #12715](https://github.com/frappe/frappe/pull/12715).
> 
> 
