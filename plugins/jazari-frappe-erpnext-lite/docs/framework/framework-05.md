<!-- Frappe documentation: framework, part 5 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__api__form.md -->
---
title: "Form Scripts"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/form"
updated: "2026-02-17"
---

Form Scripts lets you add client side logic to your Forms. You can write Form Scripts for automatically fetching values, adding validation or adding contextual actions to your Form.

Standard Form Scripts
---------------------

When you create a new DocType, a `{doctype}.js` is created where you can write your form script.

Syntax:


```
frappe.ui.form.on(doctype, {
    event1() {
        // handle event 1
    },
    event2() {
        // handle event 2
    }
})
  

```
For example, `todo.js` which is located at `frappe/desk/doctype/todo/todo.js` may look like this:


```
// Script for ToDo Form
frappe.ui.form.on('ToDo', {
    // on refresh event
    refresh(frm) {
        // if reference_type and reference_name are set,
        // add a custom button to go to the reference form
        if (frm.doc.reference_type &amp;&amp; frm.doc.reference_name) {
            frm.add_custom_button(__(frm.doc.reference_name), () => {
                frappe.set_route("Form", frm.doc.reference_type, frm.doc.reference_name);
            });
        }
    }
})
  

```
### Child Table Scripts

Child Table Scripts should be written in the same file as their parent.


```
frappe.ui.form.on('Quotation', {
    // ...
})

frappe.ui.form.on('Quotation Item', {
    // cdt is Child DocType name i.e Quotation Item
    // cdn is the row name for e.g bbfcb8da6a
    item_code(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
    }
})
  

```
Custom Form Scripts
-------------------

You can also write form scripts by creating **Client Script** in the system. You should write Client Scripts if the logic is specific to your site. If you want to share Form Scripts across sites, you must include them via Apps.

To create a new Client Script, go to

**Home > Customization > Client Script > New**

[Screenshot on the live page: New Client Script] *New Client Script for Form*

Form Events
-----------

Form Scripts depend on events to trigger. Here are the list of all Form Events that are triggered by Form.

These events will get `frm` as the first parameter in their handler functions.


```
frappe.ui.form.on('ToDo', {
    // frm passed as the first parameter
    setup(frm) {
        // write setup code
    }
})
  

```


| Event Name | Description |
| --- | --- |
| `setup` | Triggered once when the form is created for the first time |
| `before_load` | Triggered before the form is about to load |
| `onload` | Triggered when the form is loaded and is about to render |
| `refresh` | Triggered when the form is loaded and rendered. |
| `onload_post_render` | Triggered after the form is loaded and rendered |
| `validate` | Triggered before before_save |
| `before_save` | Triggered before save is called |
| `after_save` | Triggered after form is saved |
| `before_submit` | Triggered before submit is called |
| `on_submit` | Triggered after form is submitted |
| `before_cancel` | Triggered before cancel is called |
| `after_cancel` | Triggered after form is cancelled |
| `before_discard` | Triggered before discard is called |
| `after_discard` | Triggered after form is discarded |
| `timeline_refresh` | Triggered after form timeline is rendered |
| `{fieldname}_on_form_rendered` | Triggered when a row is opened as a form in a Table field |
| `{fieldname}` | Triggered when the value of fieldname is changed |
| `get_email_recipient_filters` | Called by the email dialog to fetch default filters for email recipients. Should accept two parameters `frm` (the current form) and `field` ("recipients", "cc" or "bcc"), and return an array or dict of filters (related to the **Contact** doctype). |
| `get_email_recipients` | Called by the email dialog to fetch default recipients. Should accept two parameters `frm` (the current form) and `field` ("recipients", "cc" or "bcc"), and return a list of email addresses for this field. |

### Child Table Events

These events are triggered in the context of a Child Table. Hence, along with `frm`, they will also get the `cdt` (Child DocType) and `cdn` (Child Docname) parameters in their handler functions.

Imagine our "ToDo" DocType has a field called "links" that contains a Child Table. This Child Table is defined in a DocType called "Dynamic Link". We want our code to run whenever a row is added to the table.


```
// this code is located inside `todo.js`

frappe.ui.form.on('Dynamic Link', { // The child table is defined in a DoctType called "Dynamic Link"
    links_add(frm, cdt, cdn) { // "links" is the name of the table field in ToDo, "_add" is the event
        // frm: current ToDo form
        // cdt: child DocType 'Dynamic Link'
        // cdn: child docname (something like 'a6dfk76')
        // cdt and cdn are useful for identifying which row triggered this event

        frappe.msgprint('A row has been added to the links table 🎉 ');
    }
});
  

```


| Event Name | Description |
| --- | --- |
| `before_{fieldname}_remove` | Triggered when a row is about to be removed from a Table field |
| `{fieldname}_add` | Triggered when a row is added to a Table field |
| `{fieldname}_remove` | Triggered when a row is removed from a Table field |
| `{fieldname}_move` | Triggered when a row is reordered to another location in a Table field |
| `form_render` | Triggered when a row is opened as a form in a Table field |

> **Note:** The first three events listed in the above table, `before_{fieldname}_remove`, `{fieldname}_add` and `{fieldname}_remove`, are triggered for fields of fieldtype **Table MultiSelect** also. (Version 16 onwards)
>
>

Form API
--------

Here are a list of common methods that are available on the `frm` object.

### frm.set_value

Set the value of a field. This will trigger the field change event in the form.


```
// set a single value
frm.set_value('description', 'New description')

// set multiple values at once
frm.set_value({
    status: 'Open',
    description: 'New description'
})

// returns a promise
frm.set_value('description', 'New description')
    .then(() => {
        // do something after value is set
    })
  

```
### frm.refresh

Refresh the form with the latest values from the server. Will trigger `before_load`, `onload`, `refresh`, `timeline_refresh` and `onload_post_render`.


```
frm.refresh();
  

```
### frm.save

Trigger form save. Will trigger `validate`, `before_save`, `after_save`, `timeline_refresh` and `refresh`.

It can be used to trigger other save actions like Submit, Cancel and Update. In that case, the relevant events will be triggered.


```
// save form
frm.save();

// submit form
frm.save('Submit');

// cancel form
frm.save('Cancel');

// update form (after submit)
frm.save('Update');

// all methods returns a promise
  

```
### frm.enable_save / frm.disable_save

Methods to enable / disable the Save button in the form.


```
if (frappe.user_roles.includes('Custom Role')) {
    frm.enable_save();
} else {
    frm.disable_save();
}
  

```
### frm.email_doc

Open Email dialog for this form.


```
// open email dialog
frm.email_doc();

// open email dialog with some message
frm.email_doc(`Hello ${frm.doc.customer_name}`);
  

```
### frm.reload_doc

Reload document with the latest values from the server and call `frm.refresh()`.


```
frm.reload_doc();
  

```
### frm.refresh_field

Refresh the field and it's dependencies.


```
frm.refresh_field('description');
  

```
### frm.is_dirty

Check if form values has been changed and is not saved yet.


```
if (frm.is_dirty()) {
    frappe.show_alert('Please save form before attaching a file')
}
  

```
### frm.dirty

Set form as "dirty". This is used to set form as dirty when document values are changed. This triggers the ***"Not Saved"*** indicator in the Form Views.


```
frm.doc.browser_data = navigator.appVersion;
frm.dirty();
frm.save();
  

```
Calling save without setting the form dirty will trigger a ***"No changes in document"*** toast.

### frm.is_new

Check if the form is new and is not saved yet.


```
// add custom button only if form is not new
if (!frm.is_new()) {
    frm.add_custom_button('Click me', () => console.log('Clicked custom button'))
}
  

```
### frm.set_intro

Set intro text on the top of the form. The function takes two parameters: `message` (string, required) and `color` (string, optional).

Color can be 'blue', 'red', 'orange', 'green' or 'yellow'. Default is blue.


```
if (!frm.doc.description) {
    frm.set_intro('Please set the value of description', 'blue');
}
  

```
[Screenshot on the live page: Intro text example] *Intro Text Example*

### frm.add_custom_button

Add a custom button in the inner toolbar of the page. Alias to [page.add_inner_button](/framework/v14/user/en/api/page#pageadd_inner_button).


```
// Custom buttons
frm.add_custom_button('Open Reference form', () => {
    frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
})

// Custom buttons in groups
frm.add_custom_button('Closed', () => {
    frm.doc.status = 'Closed'
}, 'Set Status');
  

```
### frm.change_custom_button_type

Change a specific custom button type by label (and group).


```
// change type of ungrouped button
frm.change_custom_button_type('Open Reference form', null, 'primary');

// change type of a button in a group
frm.change_custom_button_type('Closed', 'Set Status', 'danger');
  

```
### frm.remove_custom_button

Remove a specific custom button by label (and group).


```
// remove custom button
frm.remove_custom_button('Open Reference form');

// remove custom button in a group
frm.remove_custom_button('Closed', 'Set Status');
  

```
### frm.clear_custom_buttons

Remove all custom buttons from the inner toolbar.


```
frm.clear_custom_buttons();
  

```
### frm.set_df_property

Change the docfield property of a field and refresh the field.


```
// change the fieldtype of description field to Text
frm.set_df_property('description', 'fieldtype', 'Text');

// set the options of the status field to only be [Open, Closed]
frm.set_df_property('status', 'options', ['Open', 'Closed'])

// set a field as mandatory
frm.set_df_property('title', 'reqd', 1)

// set a field as read only
frm.set_df_property('status', 'read_only', 1)
  

```
### frm.toggle_enable

Toggle a field or list of fields as `read_only` based on a condition.


```
// set status and priority as read_only
// if user does not have System Manager role
let is_allowed = frappe.user_roles.includes('System Manager');
frm.toggle_enable(['status', 'priority'], is_allowed);
  

```
### frm.toggle_reqd

Toggle a field or list of fields as mandatory (`reqd`) based on a condition.


```
// set priority as mandatory
// if status is Open
frm.toggle_reqd('priority', frm.doc.status === 'Open');
  

```
### frm.toggle_display

Show/hide a field or list of fields based on a condition.


```
// show priority and due_date field
// if status is Open
frm.toggle_display(['priority', 'due_date'], frm.doc.status === 'Open');
  

```
### frm.set_query

Apply filters on a Link field to show limited records to choose from. You must call `frm.set_query` very early in the form lifecycle, usually in `setup` or `onload`.


```
// show only customers whose territory is set to India
frm.set_query('customer', () => {
    return {
        filters: {
            territory: 'India'
        }
    }
})

// show customers whose territory is any of India, Nepal, Japan
frm.set_query('customer', () => {
    return {
        filters: {
            territory: ['in', ['India', 'Nepal', 'Japan']]
        }
    }
})

// set filters for Link field item_code in
// items field which is a Child Table
frm.set_query('item_code', 'items', () => {
    return {
        filters: {
            item_group: 'Products'
        }
    }
})
  

```
You can also override the filter method and provide your own custom method on the server side. Just the set the query to the module path of your python method.


```
// change the filter method by passing a custom method
frm.set_query('fieldname', () => {
    return {
        query: 'dotted.path.to.custom.custom_query',
        filters: {
            field1: 'value1'
        }
    }
})
  

```

```
# python method signature
def custom_query(doctype, txt, searchfield, start, page_len, filters):
    # your logic
    return filtered_list
  

```
### frm.add_child

Add a row with values to a Table field.


```
let row = frm.add_child('items', {
    item_code: 'Tennis Racket',
    qty: 2
});

frm.refresh_field('items');
  

```
### frm.call

Call a server side controller method with arguments.


> **Note:** While accessing any server side method using `frm.call()`, you need to whitelist such method using the `@frappe.whitelist` decorator.
> 
> 

For the following controller code:


```
class ToDo(Document):
    @frappe.whitelist()
    def get_linked_doc(self, throw_if_missing=False):
        if not frappe.db.exists(self.reference_type, self.reference_name):
            if throw_if_missing:
                frappe.throw('Linked document not found')

        return frappe.get_doc(self.reference_type, self.reference_name)
  

```
You can call it from client using `frm.call`.


```
frm.call('get_linked_doc', { throw_if_missing: true })
    .then(r => {
        if (r.message) {
            let linked_doc = r.message;
            // do something with linked_doc
        }
    })
  

```
### frm.trigger

Trigger any form event explicitly.


```
frappe.ui.form.on('ToDo', {
    refresh(frm) {
        frm.trigger('set_mandatory_fields');
    },

    set_mandatory_fields(frm) {
        frm.toggle_reqd('priority', frm.doc.status === 'Open');
    }
})
  

```
### frm.get_selected

Get selected rows in Child Tables in an object where key is the table fieldname and values are row names.


```
let selected = frm.get_selected()
console.log(selected)
// {
// items: ["bbfcb8da6a", "b1f1a43233"]
// taxes: ["036ab9452a"]
// }
  

```
### frm.ignore_doctypes_on_cancel_all

To avoid cancellation of linked documents during cancel all, you need to set the `frm.ignored_doctypes_on_cancel_all` property with an array of DocTypes of linked documents.


```
frappe.ui.form.on("DocType 1", {
    onload: function(frm) {
        // Ignore cancellation for all linked documents of respective DocTypes.
        frm.ignore_doctypes_on_cancel_all = ["DocType 2", "DocType 3"];
    }
}
  

```
In the above example, the system will avoid cancellation for all documents of 'DocType 2' and 'DocType 3' which are linked with document of 'DocType 1' during cancellation.

<!-- page: framework/framework__user__en__api__full-text-search.md -->
---
title: "FullTextSearch API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/full-text-search"
updated: "2026-02-17"
---

Frappe Wrapper for [Whoosh](https://pypi.org/project/Whoosh/)

### `update_index_by_name(self, doc_name)`

Wraps `update_index` method, gets the document from name and updates the index. This function changes the current user and should only be run as administrator or in a background job.

Args:

- self (object): FullTextSearch Instance
- doc_name (str): name of the document to be updated

### `remove_document_from_index(self, doc_name)`
Remove document from search index

Args:

- self (object): FullTextSearch Instance
- doc_name (str): name of the document to be removed

### `update_index(self, document)`
Update search index for a document

Args:

- self (object): FullTextSearch Instance
- document (_dict): A dictionary with title, path and content


### `build_index(self)`
Build index for all parsed documents

### `search(self, text, scope=None, limit=20)`
Search from the current index

Args:

- text (str): String to search for
- scope (str, optional): Scope to limit the search. Defaults to None.
- limit (int, optional): Limit number of search results. Defaults to 20.

Returns:

- [list(_dict)]: Search results

<!-- page: framework/framework__user__en__api__jinja.md -->
---
title: "Jinja API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/jinja"
updated: "2026-02-17"
---


These are the whitelisted methods that frappe provides to use them in Jinja
Templates.

## frappe.format
`frappe.format(value, df, doc)`

Formats a raw value (stored in database) to a user presentable format.
For example, convert 2019-09-08 to 08-09-2019

Usage
```html
{{ frappe.format('2019-09-08', {'fieldtype': 'Date'}) }}

09-08-2019
```

## frappe.format_date
`frappe.format_date(date_string)`

Formats date into a human readable long format.

Usage

```html
{{ frappe.format_date('2019-09-08') }}

September 8, 2019
```

## frappe.get_url
`frappe.get_url()`

Returns the site url

Usage
```html
{{ frappe.get_url() }}

https://frappe.io
```

## frappe.get_doc
`frappe.get_doc(doctype, name)`

Returns a document by its name.

Usage
```html

 {% set doc = frappe.get_doc('Task', 'TASK00002') %}
 {{ doc.title }} - {{ doc.status }}



 Buy Eggs - Open

```

## frappe.get_all
`frappe.get_all(doctype, filters, fields, order_by, start, page_length, pluck)`

Returns a list of all records of a DocType. Only returns the document `name`s if the `fields` argument is not given.

Signature
```python
frappe.get_all(doctype, filters, fields, order_by, start, page_length)
```

Usage

```html

 {% set tasks = frappe.get_all('Task', filters={'status': 'Open'}, fields=['title', 'due_date'], order_by='due_date asc') %}
 {% for task in tasks %}
 
### {{ task.title }}


Due Date: {{ frappe.format_date(task.due_date) }}



 {% endfor %}




### Redesign Website


Due Date: September 8, 2019




### Add meta tags on websites


Due Date: September 22, 2019




```

## frappe.get_list
`frappe.get_list(doctype, filters, fields, order_by, start, page_length)`

Similar to `frappe.get_all` but will filter records for the current session user
based on permissions.

## frappe.db.get_value
`frappe.db.get_value(doctype, name, fieldname)`

Returns a single field value (or a list of values) from a document.

Usage

```html


 {% set company_abbreviation = frappe.db.get_value('Company', 'TennisMart', 'abbr') %}
 {{ company_abbreviation }}
 

 {% set title, description = frappe.db.get_value('Task', 'TASK00002', ['title', 'description']) %}
 ### {{ title }}


{{ description }}






TM

```

## frappe.db.get_single_value
`frappe.db.get_single_value(doctype, fieldname)`

Returns a field value from a Single DocType.

Usage
```html


 {% set timezone = frappe.db.get_single_value('System Settings', 'time_zone') %}
 {{ timezone }}
 




 Asia/Kolkata
 

```

## frappe.get_system_settings
`frappe.get_system_settings(fieldname)`

Returns a field value from System Settings.

Usage
```html

 {% if frappe.get_system_settings('country') == 'India' %}
 Pay via Razorpay
 {% else %}
 Pay via PayPal
 {% endif %}



Pay via Razorpay

```

## frappe.get_meta
`frappe.get_meta(doctype)`

Returns a doctype meta. It contains information like fields, title_field,
image_field, etc.

Usage
```html


 {% set meta = frappe.get_meta('Task') %}
 Task has {{ meta.fields | len }} fields.
 {% if meta.get_field('status') %}
 It also has a Status field.
 {% endif %}
 




 Task has 18 fields. It also has a Status field.
 

```

## frappe.get_fullname
`frappe.get_fullname(user_email)`

Returns the fullname of the user email passed. If user is not passed, assumes
current logged in user.

Usage
```html

The fullname of faris@erpnext.com is {{ frappe.get_fullname('faris@erpnext.com') }}
The current logged in user is {{ frappe.get_fullname() }}



The fullname of faris@erpnext.com is Faris Ansari
The current logged in user is John Doe

```

## frappe.render_template
`frappe.render_template(template_name, context)`

Render a jinja template string or file with context.

Usage
```html


 {{ frappe.render_template('templates/includes/footer/footer.html', {}) }}

 
{{ frappe.render_template('{{ foo }}', {'foo': 'bar'}) }}








bar



```

## frappe._
`frappe._(string)` or `_(string)`

Usage
```html

{{ _('This string should get translated') }}





इस तार का अनुवाद होना चाहिए



```

## frappe.session.user

Returns the current session user

## frappe.session.csrf_token

Returns the current session's CSRF token

## frappe.form_dict

If the template is being evaluated in a web request, `frappe.form_dict` is a
dict of query parameters, else it is `None`.

## frappe.lang

Current language used by the translation function. Two letter, lowercase code.

<!-- page: framework/framework__user__en__api__js-utils.md -->
---
title: "Common Utilities API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/js-utils"
updated: "2026-02-17"
---


## frappe.get_route
`frappe.get_route()`

Returns the current route as an array.
```js
frappe.get_route()
// ["List", "Task", "List"]
```

## frappe.set_route
`frappe.set_route(route)`

Changes the current route to `route`.
```js
// route in parts
frappe.set_route('List', 'Task', 'List')

// route as array
frappe.set_route(['List', 'Task', 'Gantt'])

// route as string
frappe.set_route('List/Event/Calendar')

// route with options
frappe.set_route(['List', 'Task', 'Task'], { status: 'Open' })
```

## frappe.format
`frappe.format(value, df, options, doc)`

Format a raw value into user presentable format.

```js
frappe.format('2019-09-08', { fieldtype: 'Date' })
// "09-08-2019"

frappe.format('2399', { fieldtype: 'Currency', options: 'currency' }, { inline: true })
// "2,399.00"
```

## frappe.provide
`frappe.provide(namespace)`

Creates a namespace attached to the window object if it doesn't exist.

```js
frappe.provide('frappe.ui.form');

// has the same effect as
window.frappe = {}
window.frappe.ui = {}
window.frappe.ui.form = {}
```

## frappe.require
`frappe.require(asset_path, callback)`

Load a JS or CSS asset asynchronously. It is used for libraries that are not
used often.

```js
// load a single asset
frappe.require('/assets/frappe/chat.js', () => {
 // chat.js is loaded
})

// load multiple assets
frappe.require(['/assets/frappe/chat.js', '/assets/frappe/chat.css'], () => {
 // chat.js and chat.css are loaded
})
```

<!-- page: framework/framework__user__en__api__list.md -->
---
title: "List"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/list"
updated: "2026-02-17"
---

The List View is generated for all DocTypes except Child Tables and Single DocTypes.

The List view is packed with features. Some of them are:

* Filters
* Sorting
* Paging
* Filter by tags
* Switch view to Report, Calendar, Gantt, Kanban, etc.

[Screenshot on the live page: List View] *List View*

Standard List JS
----------------

To customize the List View you must have a `{doctype}_list.js` file in the doctype directory. Below are all the options that can be customized.

For instance, if you want to customize the Note DocType, you'll have to create a file `note_list.js` with the following contents.


```
frappe.listview_settings['Note'] = {
    // add fields to fetch
    add_fields: ['title', 'public'],
    // set default filters
    filters: [
        ['public', '=', 1]
    ],
    hide_name_column: true, // hide the last column which shows the `name`
    hide_name_filter: true, // hide the default filter field for the name column
    onload(listview) {
        // triggers once before the list is loaded
    },
    before_render() {
        // triggers before every render of list records
    },

    // set this to true to apply indicator function on draft documents too
    has_indicator_for_draft: false,

    get_indicator(doc) {
        // customize indicator color
        if (doc.public) {
            return [__("Public"), "green", "public,=,Yes"];
        } else {
            return [__("Private"), "darkgrey", "public,=,No"];
        }
    },
    primary_action() {
        // triggers when the primary action is clicked
    },
    get_form_link(doc) {
        // override the form route for this doc
    },
    // add a custom button for each row
    button: {
        show(doc) {
            return doc.reference_name;
        },
        get_label() {
            return 'View';
        },
        get_description(doc) {
            return __('View {0}', [`${doc.reference_type} ${doc.reference_name}`])
        },
        action(doc) {
            frappe.set_route('Form', doc.reference_type, doc.reference_name);
        }
    },
    // format how a field value is shown
    formatters: {
        title(val) {
            return val.bold();
        },
        public(val) {
            return val ? 'Yes' : 'No';
        }
    }
}
  

```
Custom List JS
--------------

You can also customize the list view by creating **Client Script** in the system. You should write Client Scripts if the logic is specific to your site. If you want to share List view customization across sites, you must include them via Apps.

To create a new Client Script, go to

**Home > Customization > Client Script > New**

[Screenshot on the live page: New Client Script] *New Client Script for List*

The above customization will result in a list view that looks like this:

[Screenshot on the live page: List View Customized] *List View Customized*

Multiple Buttons in the List JS
-------------------------------


> This feature is available on [Develop](https://github.com/frappe/frappe/tree/develop) version.
> 
> 

You now have the capability to add multiple buttons within a dropdown menu in the list view row through the use of the list view client script. This feature enhances the user experience by providing convenient access to various actions directly from the list view.


```
frappe.listview_settings["ToDo"] = {
    hide_name_column: true,
    add_fields: ["reference_type", "reference_name"],

    button: {
      show: function(doc) {
        return doc.reference_name;
      },
      get_label: function() {
        return __("Open", null, "Access");
      },
      get_description: function(doc) {
        return __("Open {0}", [
          `${__(doc.reference_type)}: ${doc.reference_name}`
        ]);
      },
      action: function(doc) {
        frappe.set_route("Form", doc.reference_type, doc
          .reference_name);
      },
    },
    dropdown_button: {
      get_label: __("Dropdown"),
      buttons: [{
          get_label: __("Button 1"),
          show: function(doc) {
            return true;
          },
          get_description: function(doc) {
            return "Open Button 1 " + doc.reference_name;
          },
          action: function(doc) {
            frappe.msgprint("Dropdown Button 1 Clicked " +
              doc.reference_name);
          }
        },
        {
          get_label: __("Button 2"),
          show: function(doc) {
            return doc.status != "Closed";
          },
          get_description: function(doc) {
            return "Open Button 2 " + doc.reference_name;
          },
          action: function(doc) {
            frappe.msgprint("Dropdown Button 2 Clicked " +
              doc.reference_name);
          }
        },
        {
          get_label: __("Button 3"),
          show: function(doc) {
            return doc.status != "Cancelled";
          },
          get_description: function(doc) {
            return "Open Button 3 " + doc.reference_name;
          },
          action: function(doc) {
            frappe.msgprint("Dropdown Button 3 Clicked " +
              doc.reference_name);
          }
        },
      ]
    }
  };
```
[Screenshot on the live page]  

<!-- page: framework/framework__user__en__api__logging.md -->
---
title: "Logging"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/logging"
updated: "2026-02-17"
---

Logging is a means of tracking events that happen when some software runs. Under the bench architecture, with multitenancy, it might get really complicated really fast to track down and eliminate any uncertainties. You may wan't to log events along with circumstantial, variable data.

Frappe implements Python's [logging module](https://docs.python.org/3/howto/logging.html) to maintain bench and site wise logs. `Version 13` uses Log Rotation to maintain the last 20 files along with the current running of *100kB* each for the *out of the box* log files.

frappe.log_level
-----------------

Maintains the log level of Frappe processes. To learn more about logging levels, you can check out Python's [documentation](https://docs.python.org/dev/library/logging.html#logging.Logger.setLevel).

frappe.utils.logger.set_log_level
-----------------------------------

`frappe.utils.logger.set_log_level(level)` can be used to set the log level and regenerate the loggers dynamically.

frappe.loggers
--------------

`frappe.loggers` maintains a `dict` of active loggers in your process. The key is the name of the logger, typically "{module}-{site}" and the value holds the Logger instance.

A web worker may have `frappe.loggers` such as the following if [docs.erpnext.com](https://docs.erpnext.com/) and [frappeframework.com](https://frappeframework.com) are the sites on the bench.


```
{
    "frappe.web-docs.erpnext.com": <logger frappe.web-docs.erpnext.com="" (debug)="">,
    "frappe.web-frappeframework.com": <logger frappe.web-frappeframework.com="" (debug)="">
}
```
frappe.logger
-------------

`frappe.logger(module, with_more_info, allow_site, filter, max_size, file_count)`

Returns a `logging.Logger` object with Site and Bench level logging capabilities. If logger doesn't already exist, creates and updates`frappe.loggers`.

Arguments:

* **module**: Name of your logger and consequently your log file.
* **with_more*_*info**: Will log the `Form Dict` as additional information, typically useful for requests.
* **allow_site**: Pass site name to explicitly log under it's logs. If `True` and unspecified, guesses which site the logs would be saved under.
* **filter**: Add a filter function for your logger.
* **max_size**: Max file size of each log file in bytes.
* **file_count**: Max count of log files to be retained via Log Rotation.

### Usage


```
frappe.logger("frappe.web").debug({
    "site": "frappeframework.com",
    "remote_addr": "192.148.1.7",
    "base_url": "https://frappeframework.com/docs/v14/user/en/api/logging",
    "full_path": "/docs/v14/user/en/api/logging",
    "method": "POST",
    "scheme": "https",
    "http_status_code": 200
})
```

```
2020-07-31 16:06:55,067 DEBUG frappe.web {'site': 'frappeframework.com', 'remote_addr': '192.148.1.7', 'base_url': 'https://frappeframework.com/docs/v14/user/en/api/logging', 'full_path': '/docs/v14/user/en/api/logging', 'method': 'POST', 'scheme': 'https', 'http_status_code': 200}
```
The above entry would be logged under `./logs/frappe.web.log` and `./sites/frappeframework.com/logs/frappe.web.log` files.


> Usage specified as implemented in [app.py#L102-L110](https://github.com/frappe/frappe/blob/fe22595e854e3fb3fa4dbcbd6d9dacdf94e73462/frappe/app.py#L102-L110)
> 
> 

### Example

Consider a scenario where you've written an API for updating a counter with the value sent by the user and return the updated value. Now you want to log information in the API, to make sure it's working as expected. So, you create a logger `api` to track events for the same.


```
frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger("api", allow_site=True, file_count=50)


@frappe.whitelist()
def update(value):
    user = frappe.session.user
    logger.info(f"{user} accessed counter_app.update with value={value}")

    current_value = frappe.get_single_value("Value", "counter")
    updated_value = current_value + value
    logger.debug(f"{current_value} + {value} = {updated_value}")
    frappe.db.set_value("Value", "Value", "counter", updated_value)
    logger.info(f"{user} updated value to {value}")

    return updated_value
```
API calls made to this endpoint will now start getting logged in your `api.log` as follows


```
2020-07-31 16:06:55,067 INFO api gavin@frappe.io accessed counter_app.update with value 100
2020-07-31 16:06:55,067 DEBUG api 1000 + 100 = 1100
2020-07-31 16:06:55,068 INFO api gavin@frappe.io updated value to 1100
```

> Learn more about Logging in Frappe [here](/framework/v14/user/en/logging)
> 
> 

<!-- page: framework/framework__user__en__api__page.md -->
---
title: "Page API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/page"
updated: "2026-02-17"
---

Every screen inside the Desk is rendered inside a `frappe.ui.Page` object.

frappe.ui.make_app_page
-------------------------

Creates a new Page and attaches it to parent.


```
let page = frappe.ui.make_app_page({
    title: 'My Page',
    parent: wrapper // HTML DOM Element or jQuery object
    single_column: true // create a page without sidebar
})
  

```
[Screenshot on the live page: New Page] *New Page*

Page methods
------------

This section lists out the common methods available on the page instance object.

page.set_title
---------------

Set the page title along with the document title. The document title is shown in browser tab.


```
page.set_title('My Page')
  

```
[Screenshot on the live page: Page Title] *Page Title*

page.set_title_sub
--------------------

Set the secondary title of the page. It is shown on the right side of the page header.


```
page.set_title_sub('Subtitle')
  

```
[Screenshot on the live page: Page Subtitle] *Page Subtitle*

page.set_indicator
-------------------

Set the indicator label and color.


```
page.set_indicator('Pending', 'orange')
  

```
[Screenshot on the live page: Page Indicator] *Page Indicator*

page.clear_indicator
---------------------

Clear the indicator label and color.


```
page.clear_indicator()
  

```
page.set_primary_action
-------------------------

Set the primary action button label and handler. The third argument is the icon class which will be shown in mobile view.


```
let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')
  

```
[Screenshot on the live page: Page Primary Action] *Page Primary Action*

page.clear_primary_action
---------------------------

Clear primary action button and handler.


```
page.clear_primary_action()
  

```
page.set_secondary_action
---------------------------

Set the secondary action button label and handler. The third argument is the icon class which will be shown in mobile view.


```
let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
  

```
[Screenshot on the live page: Page Secondary Action] *Page Secondary Action*

page.clear_secondary_action
-----------------------------

Clear secondary action button and handler.


```
page.clear_secondary_action()
  

```
page.add_menu_item
--------------------

Add menu items in the Menu dropdown.


```
// add a normal menu item
page.add_menu_item('Send Email', () => open_email_dialog())

// add a standard menu item
page.add_menu_item('Send Email', () => open_email_dialog(), true)
  

```
[Screenshot on the live page: Page Menu Dropdown] *Page Menu Dropdown*

page.clear_menu
----------------

Remove Menu dropdown with items.


```
page.clear_menu()
  

```
page.add_action_item
----------------------

Add menu items in the Actions dropdown.


```
// add a normal menu item
page.add_action_item('Delete', () => delete_items())
  

```
[Screenshot on the live page: Page Actions Dropdown] *Page Actions Dropdown*

page.clear_actions_menu
-------------------------

Remove Actions dropdown with items.


```
page.clear_actions_menu()
  

```
page.add_inner_button
-----------------------

Add buttons in the inner toolbar.


```
// add a normal inner button
page.add_inner_button('Update Posts', () => update_posts())
  

```
[Screenshot on the live page: Page Inner Button] *Page Inner Button*


```
// add a dropdown button in a group
page.add_inner_button('New Post', () => new_post(), 'Make')
  

```
[Screenshot on the live page: Page Inner Button Group] *Page Inner Button Group*

### page.change_custom*button*type

Change a specific custom button type by label (and group).


```
// change type of ungrouped button
page.change_inner_button_type('Update Posts', null, 'primary');

// change type of a button in a group
page.change_inner_button_type('Delete Posts', 'Actions', 'danger');
  

```
page.remove_inner_button
--------------------------

Remove buttons in the inner toolbar.


```
// remove inner button
page.remove_inner_button('Update Posts')

// remove dropdown button in a group
page.remove_inner_button('New Posts', 'Make')
  

```
page.clear_inner_toolbar
--------------------------

Remove the inner toolbar.


```
page.clear_inner_toolbar()
  

```
page.add_field
---------------

Add a form control in the page form toolbar.


```
let field = page.add_field({
    label: 'Status',
    fieldtype: 'Select',
    fieldname: 'status',
    options: [
        'Open',
        'Closed',
        'Cancelled'
    ],
    change() {
        console.log(field.get_value());
    }
});
  

```
[Screenshot on the live page: Page Form Toolbar] *Page Form Toolbar*

page.get_form_values
----------------------

Get all form values from the page form toolbar in an object.


```
let values = page.get_form_values()
// { status: 'Open', priority: 'Low' }
  

```
page.clear_fields
------------------

Clear all fields from the page form toolbar.


```
page.clear_fields()
  

```

<!-- page: framework/framework__user__en__api__py-dialog.md -->
---
title: "Dialog API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/py-dialog"
updated: "2026-02-17"
---

Frappe provides a group of standard, interactive and flexible dialogs that are easy to configure and use. There's also a more extensive API for [Javascript](/framework/v14/user/en/api/dialog).

### frappe.msgprint

`frappe.msgprint(msg, title, raise_exception, as_table, as_list, indicator, primary_action, is_minimizable, wide, realtime)`

This method works only within a request / response cycle. It shows a message to the user logged in to Desk who initiated the request.

The argument list includes:

* `msg`: The message to be displayed
* `title`: Title of the modal
* `as_table`: If `msg` is a list of lists, render as HTML table
* `as_list`: If `msg` is a list, render as HTML unordered list
* `primary_action`: Bind a primary server/client side action.
* `raise_exception`: Exception
* `is_wide`: Show a wide modal
* `is_minimizable`: Allow users to minimize the modal
* `realtime`: publish immediately using websocket instead of adding to response message log


```
frappe.msgprint(
    msg='This file does not exist',
    title='Error',
    raise_exception=FileNotFoundError
)
  

```
[Screenshot on the live page: frappe.msgprint] *frappe.msgprint*

`primary_action` can contain a `server_action` **or** `client_side` action which must contain dotted paths to the respective methods. The JavaScript function must be a globally available function. You can also pass `hide_on_success` to close the message after the action is successfully completed.


```
# msgprint with server and client side action
frappe.msgprint(msg='This file does not exist',
    title='Error',
    raise_exception=FileNotFoundError
    primary_action={
        'label': _('Perform Action'),
        'server_action': 'dotted.path.to.server.method',
        'client_action': 'dotted.path.to.client.method',
        'hide_on_success': True,
        'args': args
    }
)
  

```
[Screenshot on the live page: frappe.msgprint with primary action] *frappe.msgprint with primary action*

### frappe.throw

`frappe.throw(msg, exc, title, is_minimizable, wide, as_list, primary_action)`

This method will raise an exception as well as show a message in Desk. It is essentially a wrapper around `frappe.msgprint`.

`exc` can be passed an optional exception. By default it will raise a `ValidationError` exception.


```
frappe.throw(
    title='Error',
    msg='This file does not exist',
    exc=FileNotFoundError
)
  

```
[Screenshot on the live page: Throw-py] *frappe.throw*
