<!-- Frappe documentation: framework, part 2 of 6. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__api__document.md -->
---
title: "Document API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/document"
updated: "2026-04-15"
---

A Document is an instance of a DocType. It is derived from the `frappe.model.Document` class and represents a single record in the database table.

## frappe.get_doc

`frappe.get_doc(doctype, name)`

Returns a Document object of the record identified by `doctype` and `name`. If no document is found, a `DoesNotExistError` is raised. If `doctype` is a Single DocType `name` is not required.

```
# get an existing document
doc = frappe.get_doc('Task', 'TASK00002')
doc.title = 'Test'
doc.save()

# get a single doctype
doc = frappe.get_doc('System Settings')
doc.timezone # Asia/Kolkata
```

`frappe.get_doc(dict)`

Returns a new Document object in memory which does not exist yet in the database.

```
# create a new document
doc = frappe.get_doc({
    'doctype': 'Task',
    'title': 'New Task'
})
doc.insert()
  

```

`frappe.get_doc(doctype={document_type}, key1 = value1, key2 = value2, ...)`

Returns a new Document object in memory which does not exist yet in the database.

```
# create new object with keyword arguments
user = frappe.get_doc(doctype='User', email_id='test@example.com')
user.insert()
```

## frappe.get_last_doc

`frappe.get_last_doc(doctype, filters, order_by)`

Returns the last Document object created under the mentioned `doctype`.

```
# get the last Task created
task = frappe.get_last_doc('Task')
```

You can also specify filters to refine your results. For instance, you can retrieve the last canceled Task by adding a filter.

```
# get the last available Cancelled Task
task = frappe.get_last_doc('Task', filters={"status": "Cancelled"})
```

By default, the `order_by` argument is set to `creation desc`, but this value can be overridden to use other non-standard fields that can serve the same purpose. For instance, you have a field `timestamp` under the **Task** DocType that tracks the time it was approved or marked valid instead of the time it was created.

```
# get the last Task created based on a non-standard field
task = frappe.get_last_doc('Task', filters={"Status": "Cancelled"}, order_by="timestamp desc")
```

Alternatively, you can choose to go completely against all of this and as a part of a joke change it to "creation asc" to retrieve the first document instead.

## frappe.get_cached_doc

Similar to `frappe.get_doc` but will look up the document in cache first before hitting the database.

## frappe.new_doc

`frappe.new_doc(doctype)`

Alternative way to create a new Document.

```
# create a new document
doc = frappe.new_doc('Task')
doc.title = 'New Task 2'
doc.insert()
```

## frappe.delete_doc

`frappe.delete_doc(doctype, name)`

Deletes the record and its children from the database. Also deletes other documents like Communication, Comments, etc linked to it.

```
frappe.delete_doc('Task', 'TASK00002')
```

## frappe.rename_doc

`frappe.rename_doc(doctype, old_name, new_name, merge=False)`

Rename a document's `name` (primary key) from `old_name` to `new_name`. If `merge` is `True` and a record with `new_name` exists, will merge the record with it.

```
frappe.rename_doc('Task', 'TASK00002', 'TASK00003')
  

```

> Rename will only work if **Allow Rename** is set in the DocType Form.

## frappe.get_meta

`frappe.get_meta(doctype)`

Returns meta information of `doctype`. This will also apply custom fields and property setters.

```
meta = frappe.get_meta('Task')
meta.has_field('status') # True
meta.get_custom_fields() # [field1, field2, ..]
  

```

To get the original document of DocType (without custom fields and property setters) use `frappe.get_doc('DocType', doctype_name)` 

## frappe.only_for

`frappe.only_for(roles, message=False)` 

Raises `frappe.PermissionError` if the current user does not have any of the permitted roles.

If the current user is `Administrator`, the permission check is skipped.

```
# restrict action to System Manager role
frappe.only_for("System Manager")


```

You can also allow multiple roles:

```
# allow multiple roles
frappe.only_for(["System Manager", "Accounts Manager"])


```

## frappe.get_docs

`frappe.get_docs(doctype, filters, *, chunk_size=1000, limit=None, limit_start=0, order_by="creation asc", as_iterator=False)` 

Returns a list of Document objects. Use `as_iterator=True` to fetch records in chunks for better memory management.

```
# Fetch specific documents with child tables
tasks = frappe.get_docs('Task', filters={'status': 'Open'}, limit=10)

for task in tasks:
    task.status = "Closed"
    task.save()

# Efficiently iterate through large datasets
leads = frappe.get_docs('Lead', as_iterator=True, chunk_size=500)

for lead in leads:
    lead.process_lead() # Custom controller method
```

## Document Methods

This section lists out common methods that are available on the `doc` object.

## doc.insert

This method inserts a new document into the database table. It will check for user permissions and execute `before_insert`, `validate`, `on_update`, `after_insert` methods if they are written in the controller.

It has some escape hatches that can be used to skip certain checks explained below.

```
doc.insert(
    ignore_permissions=True, # ignore write permissions during insert
    ignore_links=True, # ignore Link validation in the document
    ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
    ignore_mandatory=True # insert even if mandatory fields are not set
)
  

```

## doc.save

This method saves changes to an existing document. This will check for user permissions and execute `validate` before updating and `on_update` after updating values.

```
doc.save(
    ignore_permissions=True, # ignore write permissions during insert
    ignore_version=True # do not create a version record
)
  

```

## doc.delete

Delete the document record from the database table. This method is an alias to `frappe.delete_doc`.

```
doc.delete()
  

```

## doc.get_doc_before_save

Will return a version of the doc before the changes were made. You can use it to compare what changed from the last version.

```
old_doc = doc.get_doc_before_save()
if old_doc.price != doc.price:
    # price changed
    pass
```

## doc.has_value_changed

Will return True if the value of the given field was changed before and after saving.

```
price_changed = doc.has_value_changed("price")

if price_changed:
    pass
```

## doc.reload

Will get the latest values from the database and update the doc state.

When you are working with a document, it may happen that some other part of code updates the value of some field directly in the database. In such cases you can use this method to reload the doc.

```
doc.reload()
  

```

## doc.check_permission

Throw if the current user has no permission for the provided permtype.

```
doc.check_permission(permtype='write') # throws if no write permission
```

## doc.get_title

Get the document title based on `title_field` or field named **title** or **name**.

```
title = doc.get_title()
  

```

## doc.notify_update

Publish realtime event to indicate that the document has been modified. Client side event handlers react to this event by updating the form.

```
doc.notify_update()
```

## doc.db_set

Set a field value of the document directly in the database and update the modified timestamp.

> This method does not trigger controller validations and should be used very carefully.

```
# updates value in database, updates the modified timestamp
doc.db_set('price', 2300)

# updates value in database, will trigger doc.notify_update()
doc.db_set('price', 2300, notify=True)

# updates value in database, will also run frappe.db.commit()
doc.db_set('price', 2300, commit=True)

# updates value in database, does not update the modified timestamp
doc.db_set('price', 2300, update_modified=False)
  

```

## doc.append

Append a new item to a child table.

```
doc.append("childtable", {
    "child_table_field": "value",
    "child_table_int_field": 0,
    ...
})
  

```

## doc.get_url

Returns Desk URL for this document. For e.g: `/app/task/TASK00002`

```
url = doc.get_url()
  

```

## doc.add_comment

Add a comment to this document. Will show up in timeline in Form view.

```
# add a simple comment
doc.add_comment('Comment', text='Test Comment')

# add a comment of type Edit
doc.add_comment('Edit', 'Values changed')

# add a comment of type Shared
doc.add_comment("Shared", "{0} shared this document with everyone".format(user))
  

```

## doc.add_seen

Add the given/current user to list of users who have seen this document. Will update the `_seen` column in the table. It is stored as a JSON Array.

```
# add john to list of seen
doc.add_seen('john@doe.com')

# add session user to list of seen
doc.add_seen()
  

```

> This works only if **Track Seen** is enabled in the DocType.

## doc.add_viewed

Add a view log when a user views a document i.e opens the Form.

```
# add a view log by john
doc.add_viewed('john@doe.com')

# add a view log by session user
doc.add_viewed()
  

```

> This works only if **Track Views** is enabled in the DocType.

## doc.add_tag

Add a tag to a document. Tags are generally used to filter and group documents.

```
# add tags
doc.add_tag('developer')
doc.add_tag('frontend')
  

```

## doc.get_tags

Returns a list of tags associated with the specific document.

```
# get all tags
doc.get_tags()
  

```

## doc.run_method

Run method if defined in controller, will also trigger hooks if defined.

```
doc.run_method('validate')
  

```

## doc.queue_action

Run a controller method in background. If the method has an inner function, like `_submit` for `submit`, it will call that method instead.

```
doc.queue_action('send_emails', emails=email_list, message='Howdy')
  

```

## doc.get_children()

> Only available on tree DocTypes (inherited from `NestedSet`).

Returns a generator that yields an instance of `NestedSet` for each child record.

```
for child_doc in doc.get_children():
    print(child_doc.name)
  

```

It can also be applied recursively:

```
for child_doc in doc.get_children():
    print(child_doc.name)
    for grandchild_doc in child_doc.get_children():
        print(grandchild_doc.name)
  

```

## doc.get_parent()

> Only available on tree DocTypes (inherited from `NestedSet`).

Returns an instance of `NestedSet` for the parent record.

```
parent_doc = doc.get_parent()
grandparent_doc = parent_doc.get_parent()
```

## doc.db_insert()

Serialize and insert a document into database. Warning: This bypasses all validations and controller methods that might be required to run before and after inserting. When in doubt use `doc.insert()` instead.

```
doc = frappe.get_doc(doctype="Controller", data="")
doc.db_insert()
```

## doc.db_update()

Serialize and update a document into database. Warning: This bypasses all validations and controller methods that might be required to run before and after updating. When in doubt use `doc.save()` instead.

```
doc = frappe.get_last_doc("User")
doc.last_active = now()
doc.db_update()
  

```

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

![New Client Script](/files/client-script-form.png) *New Client Script for Form*

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
![Intro text example](/files/Screenshot 2022-04-23 at 1.56.04 AM.png) *Intro Text Example*

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

![List View](/files/list-view.png) *List View*

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

![New Client Script](/files/client-script-list.png) *New Client Script for List*

The above customization will result in a list view that looks like this:

![List View Customized](/files/list-view-customized.png) *List View Customized*

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
![](/files/w7DupHw.png)  

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
![New Page](/files/new-page.png) *New Page*

Page methods
------------

This section lists out the common methods available on the page instance object.

page.set_title
---------------

Set the page title along with the document title. The document title is shown in browser tab.


```
page.set_title('My Page')
  

```
![Page Title](/files/page-set-title.png) *Page Title*

page.set_title_sub
--------------------

Set the secondary title of the page. It is shown on the right side of the page header.


```
page.set_title_sub('Subtitle')
  

```
![Page Subtitle](/files/page-set-title-sub.png) *Page Subtitle*

page.set_indicator
-------------------

Set the indicator label and color.


```
page.set_indicator('Pending', 'orange')
  

```
![Page Indicator](/files/page-set-indicator.png) *Page Indicator*

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
![Page Primary Action](/files/page-primary-action.png) *Page Primary Action*

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
![Page Secondary Action](/files/page-secondary-action.png) *Page Secondary Action*

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
![Page Menu Dropdown](/files/page-menu-dropdown.png) *Page Menu Dropdown*

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
![Page Actions Dropdown](/files/page-actions-dropdown.png) *Page Actions Dropdown*

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
![Page Inner Button](/files/page-inner-button.png) *Page Inner Button*


```
// add a dropdown button in a group
page.add_inner_button('New Post', () => new_post(), 'Make')
  

```
![Page Inner Button Group](/files/page-inner-button-group.png) *Page Inner Button Group*

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
![Page Form Toolbar](/files/page-add-field.png) *Page Form Toolbar*

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
![frappe.msgprint](/files/dialog-api-msgprint-py.png) *frappe.msgprint*

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
![frappe.msgprint with primary action](/files/dialog-api-msgprint-py-with-primary-action.png) *frappe.msgprint with primary action*

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
![Throw-py](/files/dialog-api-msgprint-py.png) *frappe.throw*

<!-- page: framework/framework__user__en__api__query-builder.md -->
---
title: "Query Builder\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/query-builder"
updated: "2026-04-23"
---

`frappe.qb` is a query builder written around PyPika to build a single interface for cross-db queries

While developing apps, you'll often need to retrieve some specific data from the database. One way to do this is to use `frappe.db.sql` and write raw SQL queries.

Maybe something like

```python
result = frappe.db.sql(
 f"""
 SELECT `path`,
 COUNT(*) as count,
 COUNT(CASE WHEN CAST(`is_unique` as Integer) = 1 THEN 1 END) as unique_count
 FROM `tabWeb Page View`
 WHERE `creation` BETWEEN {some_date} AND {some_later_date}
 """
)
```

The query builder API makes this easier by providing a simple pythonic API to build SQL queries without limiting the flexibility of handwritten SQL.

The same query in the query builder would look something like

```python
import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count
from pypika.terms import Case

WebPageView = DocType("Web Page View") # you can also use frappe.qb.DocType to bypass an import

count_all = Count('*').as_("count")
case = Case().when(WebPageView.is_unique == "1", "1")
count_is_unique = Count(case).as_("unique_count")

result = (
 frappe.qb.from_(WebPageView)
 .select(WebPageView.path, count_all, count_is_unique)
 .where(Web_Page_View.creation[some_date:some_later_date])
).run()
```

## frappe.qb

Returns a Pypika query object which lets you build queries. Queries built using this object will be a  
type from `pypika.dialects`, sprinkled with some Frappe sugar. Some of its methods are:

### frappe.qb.from_(doctype)

lets you construct a from query to select data

**Select query**

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabCustomer`
```

**A complex Select example**

```python
customers = frappe.qb.DocType('Customer')
q = (
 frappe.qb.from_(customers)
 .select(customers.id, customers.fname,customers.lname, customers.phone)
 .where((customers.fname == 'Max') | (customers.id.like('RA%')) )
 .where(customers.lname == 'Mustermann')
)
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabCustomer` WHERE (`fname`='Max' OR `id` LIKE 'RA%') AND `lname`='Mustermann'
```

Some noteworthy things

- We have created a `customers` variable to refer to the table in the query.
- Select can take any number of arguments, selecting various Fields.
- The '|' (pipe) or '&' (ampersand) operators can be used to refer to 'OR' or 'AND'.
- Chaining the `where()` method appends 'AND' by default

You can read more about the other functions at the [Pypika](https://github.com/kayak/pypika) repo.

### frappe.qb.Doctype(name_of_table)

Returns a PyPika table object which can be used elsewhere. It will automatically add 'tab' if necessary.

### frappe.qb.Table(name_of_table)

Does the same thing as `frappe.qb.DocType` but will not append 'tab'. It's intended to be used with '__Auth' like tables.

> Note: You should only use this if you know what you are doing.

### frappe.qb.Field(name_of_coloum)

Return a PyPika field object, this represents a column. They are usually used to compare columns with values.

One example would be

```python
lname = frappe.qb.Field("lname")
q = frapppe.qb.from_("customers").select("*").where(lname == 'Mustermann')
```

## Executing queries

Queries built using the `frappe.qb` namespace are PyPika objects. They will have to be converted to string objects so that your database management system can recognize them.

To check how your query object translates, you can type cast it with `str` or use the `.get_sql` method they come with.

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')

str(query)
# SELECT "id","fname","lname","phone" FROM "tabCustomer"

query.get_sql()
# SELECT "id","fname","lname","phone" FROM "tabCustomer"

str(query) == query.get_sql()
# True
```

### Walk method

All queries built through `frappe.qb` are parameterized by default. All input fields, raw values, and functions are separated as Named parameters and sent to the database as a dictionary. Parameterization is done to sanitize queries which would prevent SQL injections.

You use the `walk` method to check out which parts are parameterized. It returns the parameterized query and the corresponding dictionary.

```py
doctype = frappe.qb.DocType("DocType")

frappe.qb.from_(doctype).select('*').where(doctype.name == "somename").walk()
# ('SELECT * FROM `tabDocType` WHERE `name`=%(param1)s', {'param1': 'somename'})
```

### Run method

This is the most preferred method to execute your queries. Every valid query has the `run` method which you  
may use to execute the query with.

```python
frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone').run()
```

The `run` method accepts `kwargs` which will be passed on while the query is being executed. You may pass whatever options are available in `frappe.db.sql`, through the `run` method.

To run debug on your query, or get the result in the form of List[Dict], you may use the following respectively:

```python
In [7]: frappe.qb.from_('ToDo').select('name').run(debug=True)
SELECT "name" FROM "tabToDo"
Execution time: 0.0 sec
Out[7]: [('8d765f73a2',)]

In [8]: frappe.qb.from_('ToDo').select('name').run(as_dict=True)
Out[8]: [{'name': '8d765f73a2'}]
```

> The `run` method internally calls the lower level `frappe.db.sql` API.

### frappe.db.sql

ou may choose to directly pass your query objects to `frappe.db.sql` too. This ignores permisions and paramaterisation of queries.

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
frappe.db.sql(query)
```

## frappe.query_builder.functions

This module provides standard functions you might need while building queries, like `Count()` and `Sum().`

### Joins and Sub-queries

You can check [pypika documentation](https://pypika.readthedocs.io/en/latest/2_tutorial.html#joining-tables-and-subqueries) to join tables and add subqueries. Instead of `Table`, use `frappe.qb.DocType`

Example:

```
HasRole = frappe.qb.DocType('Has Role')
CustomRole = frappe.qb.DocType('Custom Role')

query = (frappe.qb.from_(HasRole)
 .inner_join(CustomRole)
 .on(CustomRole.name == HasRole.parent)
 .select(CustomRole.page, HasRole.parent, HasRole.role))
```

### Simple functions

Say you want to count all the entries in a Notes table. You could do something like

```python
from frappe.query_builder.functions import Count

Notes = frappe.qb.DocType("Notes")
count_pages = Count(Notes.content).as_("Pages")

result = frappe.qb.from_(Notes).select(count_pages).run(as_dict=True)
```

### JSON functions

> Note: This is available on v16+

These helpers make JSON queries portable across MariaDB and Postgres by mapping to the correct SQL dialect internally. 

Use cases:

1. Read JSON object values by path
2. Read scalar/text values for filtering
3. Check whether JSON object/array contains a value

Available helpers:

1. `JSONExtract(field, path)`
2. `JSONValue(field, path)`
3. `JSONContains(target, candidate)`

Example: JSON object field

```python
import frappe
from frappe.query_builder.functions import JSONExtract, JSONValue

CustomerProfile = frappe.qb.DocType("Customer Profile")

# preferences_json:
# {"notifications": {"email": true, "sms": false}, "language": "en"}

query = (
    frappe.qb.from_(CustomerProfile)
    .select(
        CustomerProfile.customer_name,
        JSONValue(CustomerProfile.preferences_json, "$.language").as_("preferred_language"),
        JSONValue(CustomerProfile.preferences_json, "$.notifications.email").as_("email_notifications"),
    )
    .where(JSONValue(CustomerProfile.preferences_json, "$.notifications.email") == "true")
)
```

Example: JSON list field

```
import frappe
from frappe.query_builder.functions import JSONContains, JSONExtract

SalesOrder = frappe.qb.DocType("Sales Order")

# applied_discounts_json:
# {"codes": ["WELCOME10", "FREESHIP", "VIP"]}

query = (
    frappe.qb.from_(SalesOrder)
    .select(SalesOrder.name, SalesOrder.customer)
    .where(JSONContains(JSONExtract(SalesOrder.applied_discounts_json, "$.codes"), "FREESHIP"))
)
```

### Custom Functions

`frappe.query_builder.functions` is a superset of `pypika.functions`, so it has all PyPika functions and some custom ones we made. You can make your custom functions by importing the `CustomFunction` class from PyPika

One implementation of the DateDiff function

```python
from pypika import CustomFunction

customers = Tables('Customer')
DateDiff = CustomFunction('DATE_DIFF', ['interval', 'start_date', 'end_date'])

q = Query.from_(customers).select(
 DateDiff('day', customers.created_date, customers.updated_date)
)
```

If we print `q`, we would get

```SQL
SELECT DATE_DIFF('day',"created_date","updated_date") FROM "Customer"
```

> Notice how we specify arguments and the actual SQL text. The exact format might not work for more complex functions. The advanced section covers more complicated methods.

### Constant Column

`ConstantColumn` is a class to define a pseudo column with a constant value. 

```py
from frappe.query_builder.custom import ConstantColumn

frappe.qb.from_("DocType").select("name", ConstantColumn("john").as_("user"))
# SELECT `name`,'john' `user` FROM `tabDocType`
```

Here we define a column user with the value "john."

## Advanced

### Special functions

One such function is [Match Against](https://mariadb.com/kb/en/match-against/). It's different because it has a chained against argument. To implement something like this you need to inherit from PyPika's `DistinctOptionFunction` class.

The current MATCH class looks something like

```python

from pypika.functions import DistinctOptionFunction
from pypika.utils import builder

class MATCH(DistinctOptionFunction):
 def __init__(self, column: str, *args:
 super(MATCH, self)._init_(" MATCH", column, *args)
 self._Against = False

 def get_function_sql(self, **kwargs):
 s = super(DistinctOptionFunction, self).get_function_sql(**kwargs)

 if self._Against:
 return f"{s} AGAINST (f'+{self._Against}*') IN BOOLEAN MODE)"
 return s

 @builder
 def Against(self, text: str):
 self._Against = text
```

- The `__init__()` method works similar to CustomFunction class above. You mention all the arguments and the SQL text.
- The `Against()` method only stores a value that will be used in the `get_function_sql()`
- It also has the `@builder` wrapper. In short, it lets these functions be chainable by making a copy of the object.
- We have wrapped the `get_function_sql()` method, which allows us to append the required SQL text for Against.
- this can further be extended to use any number other chains.

In use, the Match class looks like this

```python
from frappe.query_builder.functions import Match

match = Match("Coloum name").Against("Some_text_match")
# MATCH('Coloum name') AGAINST ('+Some_text_match*' IN BOOLEAN MODE)
```

### Utils

**ImportMapper(dict)**

In the rare case where you have different functions for different SQL dialects, Which do the same thing, you can use the ImportMapper Utility. It maps functions based on the SQL dialect, so one query works across different SQL dialects.

It takes in a dict which maps functions to databases.

For example the the mapping for GroupConat looks like this

```python

from frappe.query_builder.utils import ImportMapper, db_type_is
from frappe.query_builder.custom import GROUP_CONCAT, STRING_AGG

GroupConcat = ImportMapper(
 {
 db_type_is.MARIADB: GROUP_CONCAT,
 db_type_is.POSTGRES: STRING_AGG
 }
)
```

<!-- page: framework/framework__user__en__api__realtime.md -->
---
title: "Realtime (socket.io)"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/realtime"
updated: "2026-06-12"
---

Frappe ships with an API for realtime events based on [socket.io](https://socket.io/). Since socket.io needs a Node server to run, we run a Node process in parallel to the main web server.

## Client APIs (JavaScript)

## frappe.realtime.on

To listen to realtime events on the client (browser), you can use the `frappe.realtime.on` method:

```
frappe.realtime.on('event_name', (data) => {
    console.log(data)
})
```

## frappe.realtime.off

Stop listening to an event you have subscribed to:

```
frappe.realtime.off('event_name')
```

## Server APIs (Python)

## frappe.publish_realtime

To publish a realtime event from the server, you can use the `frappe.publish_realtime` method:

```
frappe.publish_realtime('event_name', data={'key': 'value'})
```

## frappe.publish_progress

You can use this method to show a progress bar in a dialog:

```
frappe.publish_progress(25, title='Some title', description='Some description')
```

![frappe publish realtime](/files/frappe-publish-realtime.png)

## **Custom Event Handlers (Python)**

> Note: This feature is only available in nightly version. This feature is considered experimental.

You can implement custom real-time event handlers by creating a file `your_app/your_app/realtime/handlers.py` in your custom app. The syntax is fairly similar with API whitelists.



```python
from frappe.realtime import realtime

@realtime.on(
  "project_subscribe",
  frappe_context=False,   # open a Frappe context (DB + session) for the handler body
  allow_guest=False,      # if False, the event is dropped when socket.user == "Guest"
)
```

Defaults: `frappe_context=False`, `allow_guest=False`

### **Example**

```python
import frappe
from frappe.realtime import Socket, realtime

@realtime.on("project_subscribe")
def project_subscribe(socket: Socket, project: str) -> None:
    if socket.has_permission("Project", project):
        socket.join(f"project:{project}")
```



The first argument is always the typed `Socket`. The rest are the payload the client sent, positionally. The event name `"project_subscribe"` is what the browser emits with `frappe.realtime.emit(...)`.

### **Working example with frappe_context=True**

With `frappe_context=True` the full ORM is available in the handler body — `frappe.get_doc`, `frappe.local.site`, `frappe.session.user` are all populated and reflect the authenticated socket user.



This example handler loads a doc, checks permission, and emits the result back to the client:  

```python
@realtime.on("test_get_doc", frappe_context=True)
def test_get_doc(socket: Socket, doctype: str, docname: str) -> None:
    import frappe
    try:
        doc = frappe.get_doc(doctype, docname)
        doc.check_permission()
        socket.emit(
            "test_get_doc_result",
            {
                "ok": True,
                "site": frappe.local.site,
                "user": frappe.session.user,
                "doctype": doc.doctype,
                "name": doc.name,
                "modified": str(doc.get("modified")),
            },
        )
    except Exception as e:
        socket.emit("test_get_doc_result", {"ok": False, "error": f"{type(e).__name__}: {e}"})
```



From the browser:

```js
frappe.realtime.on("test_get_doc_result", (r) => console.log(r));
frappe.realtime.emit("test_get_doc", "User", "Administrator");
```

See [Permission checks](#permission-checks-two-ways)  section for the cost and when to prefer the cheap HTTP based permission check instead.



A handler runs only if its owning app is installed on the connecting site. The owning app is detected automatically from the import.

You may have to restart the socketio server to see code changes take effect. See the [Socket.IO docs](https://socket.io/docs/v4/) for more on writing custom event handlers.

### **Socket object**

Read-only identity, populated at connect:

```python
socket.site            # the site this socket is on
socket.user            # "Guest" for anonymous
socket.user_type       # e.g. "System User"
socket.installed_apps  # list of installed apps
```



Rooms, emit and transient state:

```python
socket.join(room)                        # add this socket to a room
socket.leave(room)                       # remove it
socket.emit(event, data=None, room=None) # emit to a room, or to this client if room is None
socket.get(key, default=None)            # read transient per-socket state
socket.set(key, value)                   # persist transient per-socket state (cleared on disconnect)
```



**Permission checks**

There are two ways to perform doctype permission checks.



**A. HTTP (default, recommended)** : `socket.has_permission(doctype, name)` asks the web process, exactly like the core handlers. No DB connection in the realtime process. Cheap. Use this unless you have a reason not to.

```python
if socket.has_permission("Project", project):
    socket.join(f"project:{project}")
```



B. **In-process (`frappe_context=True`)** : opens a full Frappe context for the handler body so you can call `frappe.has_permission(...)`, query the DB, etc. directly. Cost: every such event pays `frappe.init -> connect -> set_user -> commit/rollback -> destroy` and forces a DB connection into the realtime process. Use sparingly.

```python
@realtime.on("project_subscribe", frappe_context=True)
def project_subscribe(socket: Socket, project: str) -> None:
    if frappe.has_permission("Project", doc=project, ptype="read"):
        socket.join(f"project:{project}")
```

Full reference: ++[https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md](https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md)++

## **Custom Event Handlers (NodeJS)**

> **Available from v16.**  Considered experimental. This is the previous implementation and will be phased out in newer version. 
>
> Socket.IO server path; new apps should prefer the Python handlers above.



You can implement custom real-time event handlers by creating a `handlers.js` file in the `realtime` folder of your app.

You need a single export from this file — a function that sets up event handlers on the socket instance. E.g. for an app called "chat":

```javascript
// bench/apps/chat/realtime/handlers.js

function chat_app_handlers(socket) {
    socket.on("hello_chat", () => {
        console.log("hello world!");
    });
}

module.exports = chat_app_handlers;
```

Trigger this event from client-side code with `frappe.realtime.emit("hello_chat")`. You may have to restart the socketio server to see code changes take effect. See the [Socket.IO docs](https://socket.io/docs/v4/) for more on writing custom event handlers.

## **Pushing events to clients**

You do not emit from the web process directly — you publish through Redis, and the realtime server bridges it to the connected sockets. The room string you publish to must match the room your handler `join`-ed.

```python
from frappe.realtime import publish_to_room
publish_to_room("project:PROJ-0001", "project_updated", {"status": "Open"})
```



Other named helpers, each thin wrapper over `publish_realtime`.

```python
publish_to_user(user, event, message=None)
publish_to_doc(doctype, docname, event, message=None)
publish_to_doctype(doctype, event, message=None)
publish_task_progress(task_id, message=None)
publish_to_website(event, message=None)
publish_to_all(event, message=None)
publish_to_room(room, event, message=None)
```

Full reference: ++[https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md](https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md)++



# **Custom Client**

You can write a custom client to connect to the socket.io server if you're developing a SPA or a mobile app that doesn't use the Desk interface. Refer to the official [Socket.IO client docs](https://socket.io/docs/v4/client-initialization/).



Example custom clients:

- [gameplan/frontend/src/socket.js](https://github.com/frappe/gameplan/blob/9f9332cf29496afe5e912e4f1734fbf1142cb18c/frontend/src/socket.js#L13)
- [frappe/socketio_client.js](https://github.com/frappe/frappe/blob/8093a1d0a54900fe4b43b01ae6ffc0adf855da43/frappe/public/js/frappe/socketio_client.js#L49)

## **Authorization in custom clients**

Two ways to authenticate a connection with the socket.io server:

- **Cookies** — in a browser-like environment, the connection automatically sends cookies and the socketio server authenticates using them.
- **Authorization header** — if cookies are unavailable (e.g. mobile apps), use an `Authorization` header just like API requests. See the [REST API authentication docs](https://frappeframework.com/docs/user/en/api/rest#authentication) and [Socket.IO extraHeaders](https://socket.io/docs/v4/client-options/#extraheaders).



# **Implementation Notes**

- Realtime server uses the socket.io server, written in node.js, found in the `/realtime` directory.
- The realtime client is a wrapper around the socket.io client library, found in `public/js/frappe/socketio_client.js`.
- Python processes publish events to the node server over a Redis pub-sub channel. The realtime server subscribes to the Redis channel and republishes to all subscribed clients.
- The realtime server is multi-tenant: all site traffic is namespaced by sitename. Namespaces are created dynamically as `/{sitename}`, where `sitename` is the  site's folder name in the `sites` directory (or `frappe.local.site`).
- The realtime server uses the main Frappe web server to authenticate connections. The SID cookie or authorization header is passed to the client and used to ensure the connection is a valid user that can subscribe to DocTypes/documents per permissions.

## **Available rooms**


| Room                 | Access                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| all                  | Connected by default for all System Users                                                                |
| website              | Accessible to any user, including Guests                                                                 |
| user:{username}      | Per-user room. Allowed without permission checks                                                         |
| doctype:{doctype}    | Per-DocType room. Only users with DocType permission may join; auto-subscribed on opening list/form view |
| doc:{doctype}/{name} | Per-document room. Only users with document permission may join; auto-subscribed on opening form view    |

<!-- page: framework/framework__user__en__api__rest.md -->
---
title: "REST API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/rest"
updated: "2026-05-10"
---

Frappe framework generates REST API for all of your DocTypes out of the box. You can also run arbitrary python methods using their dotted module path.

Authentication
--------------

There are two ways to authenticate through Frappe REST API. Token based authentication and password based authentication.

### 1. Token Based Authentication

A token is a pair of API Key and API Secret. To generate these tokens follow these steps:

1. Go to User list and open a user.
2. Click on the "Settings" tab. (skip this step if you don't see tabs)
3. Expand the API Access section and click on Generate Keys.
4. You will get a popup with the API Secret. Copy this value and keep it somewhere safe (Password Manager).
5. You will also see another field "API Key" in this section.

The token is generated by concatenating `api_key` and `api_secret` with a colon `:`. Pass the string `token api_key:api_secret` to the `Authorization` header in the request.


```
fetch('http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user', {
    headers: {
        'Authorization': 'token api_key:api_secret'
    }
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```

```
➜ curl http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user -H "Authorization: token api_key:api_secret"

```
Every request you make with these tokens will be logged against the user you selected in Step 1. This also means that roles will be checked against this user. You can also create a new user just for API calls.

### 2. Password Based Authentication

Password based authentication relies on cookies and session data to maintain authentication in subsequent requests. In most cases, the library you are using to issue REST calls will handle session data, but if it doesn't you should use Token based authentication.


```
fetch('http://&lt;base-url&gt;/api/method/login', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        usr: 'username or email',
        pwd: 'password'
    })
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```

```
➜ curl --cookie-jar snowcookie --request POST "http://&lt;base-url&gt;/api/method/login" -H 'Content-Type: application/json' -H 'Accept: application/json' --data-raw "{ "usr" : "&lt;username&gt;", "pwd": "&lt;password&gt;" }"
{"message":"Logged In","home_page":"/app","full_name":"&lt;user:full_name&gt;","dashboard_route":"/sites"}

➜ curl --cookie snowcookie --request POST "http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user" -H 'Accept: application/json'
{"message":"&lt;username&gt;"}

```
### 3. Access Token

Refer documentation for [How to setup OAuth](/framework/v14/user/en/guides/integration/how_to_set_up_oauth).

Use the generated `access_token` in request header.


```
fetch('http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user', {
    headers: {
        'Authorization': 'Bearer access_token'
    }
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```
Listing Documents
-----------------

To get a list of records of a DocType, send a GET request at `/api/resource/:doctype`. By default, it will return 20 records and will only fetch the name of the records. The result for the query can be found under `data` of the payload.

We'll be using the ToDo DocType to show example responses for the queries below.


```
GET /api/resource/:doctype

```
Response


```
{
  "data":[
    {"name":"f765eef382"},
    {"name":"2a26fa1c64"},
    {"name":"f32c68060f"},
    {"name":"9065fa9832"},
    {"name":"419082fc38"},
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    ...
  ]
}

```
You can specify which fields to fetch in the `fields` param. It should be a JSON array.


```
GET /api/resource/:doctype?fields=["field1", "field2"]

```
Response


```
{
  "data":[
    {"description":"Business worker talk society. Each try theory prove notice middle. Crime couple trouble guy project hit.","name":"f765eef382"},
    {"description":"This reveal as look near sister. Car staff bar specific address.","name":"2a26fa1c64"},
    {"description":"Wear bag some walk. Movie partner new class tough run. Brother Democrat imagine.","name":"f32c68060f"},
    {"description":"Break laugh apply reveal new now focus heavy. Outside local staff research total. Else point try despite.","name":"9065fa9832"},
    {"description":"Truth reduce baby artist actually model. Cost phone us others himself wife almost. Language thing wonder share talk. Factor glass significant could window certain yet.","name":"419082fc38"},
    {"description":"Tv memory understand opportunity window beat physical.","name":"6234d15099"},
    {"description":"Should floor situation in response sell. Our assume company mean red majority shoulder.","name":"62f2181ee0"},
    {"description":"Performance seem sign recent. Court form me tonight simple trouble. Address job garden play teach. Happy speech amount offer change then.","name":"a50afbbfaa"},
    ...
  ]
}

```

You can specify which fields to expand in the `expand` param. It should be a JSON array.

```
GET /api/resource/:doctype?expand=["priority"]

```
Response


```
{
  "data":[
    {
        "name":"f765eef382"
        "priority": {
            "name":"a1b2c3", 
            "title": "Medium", 
            "creation": "2025-11-05 19:02:19.106966",
        },
    },
    {
        "name":"f765eef393"
        "priority": {
            "name":"a1b2c4", 
            "title": "High", 
            "creation": "2025-11-05 20:02:19.106966",
        },
    },
    ...
  ]
}

```

You can filter the records by passing `filters` param. Filters should be an array, where each filter is of the format: `[field, operator, value]`


```
GET /api/resource/:doctype?filters=[["field1", "=", "value1"], ["field2", "&gt;", "value2"]]

```
Response


```
{
  "data":[
    {"name":"f765eef382"},
    {"name":"2a26fa1c64"},
    {"name":"f32c68060f"},
    {"name":"9065fa9832"},
    {"name":"419082fc38"},
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    ...
  ]
}

```
`filters` parameter joins all the specified filters using `AND` SQL operator, if you want `OR` filters you can use the `or_filters` param. Syntax for `or_filters` is same as `filters.

You can also provide the sort field and order. It should be of the format `fieldname asc` or `fieldname desc`. The space should be URL encoded. In the following line, we're taking fieldname to be `title`.


```
GET /api/resource/:doctype?order_by=title%20desc

```
You can also page the results by providing the `limit_start` and `limit_page_length` params.


```
GET /api/resource/:doctype?limit_start=5&amp;limit_page_length=10

```
Response


```
{
  "data": [
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    {"name":"aa12a5cf71"},
    {"name":"6ac9800d4e"},
    {"name":"4bcf8b701c"},
    {"name":"aee15f4c20"},
    {"name":"6ba753afef"},
    ...
  ]
}

```
`limit` is an alias for `limit_page_length` for accessing `/api/resource` in Version 13. This means the following should also return the same payload as the above query.


```
GET /api/resource/:doctype?limit_start=5&amp;limit=10

```
By default, you will receive the data as `List[dict]`. You can retrieve your data as `List[List]` by passing `as_dict=False`.


```
GET /api/resource/:doctype?limit_start=5&amp;limit=5&amp;as_dict=False

```
Response


```
{
  "data": [
    ["6234d15099"],
    ["62f2181ee0"],
    ["a50afbbfaa"],
    ["aa12a5cf71"],
    ["6ac9800d4e"]
  ]
}

```
To debug the query built for your reqeusts, you can pass `debug=True` with the request. This returns the executed query and execution time under `exc` of the payload.


```
GET /api/resource/:doctype?limit_start=10&amp;limit=5&amp;debug=True

```
Response


```
{
  "data": [
    {"name":"4bcf8b701c"},
    {"name":"aee15f4c20"},
    {"name":"6ba753afef"},
    {"name":"f4b7e24abc"},
    {"name":"bd9156096c"}
  ],
  "exc": "[\"select `tabToDo`.`name`\\n\\t\\t\\tfrom `tabToDo`\\n\\t\\t\\t\\n\\t\\t\\t\\n\\t\\t\\t order by `tabToDo`.`modified` DESC\\n\\t\\t\\tlimit 5 offset 10\", \"Execution time: 0.0 sec\"]"
}

```
CRUD Operations
---------------

Frappe generates REST endpoints for CRUD operations for all DocTypes automatically. Make sure you set the following headers in your requests so that you get proper JSON responses.


```
{
    "Accept": "application/json",
    "Content-Type": "application/json",
}

```
### Create

Create a new document by sending a `POST` request to `/api/resource/:doctype`. Send the document as JSON in the Request Body.


```
POST /api/resource/:doctype

# Body
{"description": "New ToDo"}

```
Response


```
{
  "data": {
    "name": "af2e2d0e33",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "New ToDo",
    "doctype": "ToDo"
  }
}

```
### Read

Get a document by sending a `GET` request to `/api/resource/:doctype/:name`.


```
GET /api/resource/:doctype/:name

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "<p>Test description</p>",
    "doctype": "ToDo"
  }
}

```
Expand all link fields by sending a `GET` request to `/api/resource/:doctype/:name?expand_links=True`.

```
GET /api/resource/:doctype/:name?expand_links=True

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": {
        "name":"a1b2c3", 
        "title": "Medium", 
        "creation": "2025-11-05 19:02:19.106966",
    },
    "description": "<p>Test description</p>",
    "doctype": "ToDo"
  }
}

```

### Update

Update a document by sending a `PUT` request to `/api/resource/:doctype/:name`. You don't need to send the whole document, instead you can just send the fields that you want to update.


```
PUT /api/resource/:doctype/:name

# Body
{"description": "New description"}

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:21:00.785117",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "New description",
    "doctype": "ToDo"
  }
}

```
### Delete

Delete a document by sending a `DELETE` request to `/api/resource/:doctype/:name`.


```
DELETE /api/resource/:doctype/:name

```
Response


```
{"message": "ok"}

```
Remote Method Calls
-------------------

Frappe allows you to trigger arbitrary python methods using the REST API for handling custom logic. These methods must be marked as *whitelisted* to make them accessible via REST.

To run a whitelisted python method at `frappe.auth.get_logged_user`, send a request to the endpoint `/api/method/frappe.auth.get_logged_user`.


```
GET /api/method/frappe.auth.get_logged_user

```
Response


```
{
  "message": "john@doe.com"
}

```
* If your method returns some values, you should send a `GET` request.
* If your method changes the state of the database, use `POST`. After a successful `POST` request, the framework will automatically call `frappe.db.commit()` to commit the changes to the database.
* A successful response will return a JSON object with a `message` key.
* An errored response will return a JSON object with `exc` key which contains the stack trace and `exc_type` which contains the thrown Exception.
* The return value of the method will be converted to a JSON and sent as the response.

File Uploads
------------

There is a dedicated method `/api/method/upload_file` that accepts binary file data and uploads it into the system.

Here is the curl command for it:


```
➜ curl -X POST \
  http://&lt;base-url&gt;/api/method/upload_file \
  -H 'Accept: application/json' \
  -H 'Authorization: token xxxx:yyyy' \
  -F file=@/path/to/file/file.png

```
If you are using client side Javascript to upload files, you can append the uploaded files as FormData and send an XHR request. Here is the [implementation code](https://github.com/frappe/frappe/blob/421f070e78ee1186e7f2f4b2575d8be1d3e2d646/frappe/public/js/frappe/file_uploader/FileUploader.vue#L381-L401) in Frappe Desk.

<!-- page: framework/framework__user__en__api__scanner.md -->
---
title: "Scanner API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/scanner"
updated: "2026-02-17"
---


Frappe uses the open-source library [Html5-QRCode](https://github.com/mebjas/html5-qrcode) to provide a flexible way to handle inputs like Barcodes, QRCodes, etc. using the device camera.



## frappe.ui.Scanner

```
new frappe.ui.Scanner({ ... })
```

Creates a new Scanner instance that can be used to scan single or multiple barcodes.

Options:

- `container`: Dom element under which video feed from the camera will be shown.
- `dialog`: If set as `true`, will open a dialog to show video feed from the camera.
- `multiple`: If set as `false`, will stop scanning after one successful scan.
- `on_scan`: Callback method to handle the scanned input.

Here is a sample client code to scan one single barcode and log it to the console.

```js
new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: false, // stop after scanning one value
 on_scan(data) {
 console.log(data.decodedText);
 }
});
```

The below code can be used to continously scan and handle the scanned input.

```js
const scanner = new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: true, // stop after scanning one value
 on_scan(data) {
 handle_scanned_barcode(data.decodedText);
 }
});
```

To stop the scanning, you can either close the dialog or use `scanner.stop_scan();`

<!-- page: framework/framework__user__en__api__server-calls.md -->
---
title: "Server Calls (AJAX)\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/server-calls"
updated: "2026-04-18"
---

## frappe.call

`frappe.call(method, args)`

Makes an AJAX request to the server, where the `method` which is the dotted path  
to a whitelisted Python method, is executed and it's return value is sent as the  
response.

```js
// call with no parameters
frappe.call('ping')
 .then(r => {
 console.log(r)
 // {message: "pong"}
 })

// call with a single parameter
frappe.call('frappe.core.doctype.user.user.get_role_profile', {
 role_profile: 'Test'
}).then(r => {
 console.log(r.message)
})

// call with all options
frappe.call({
 method: 'frappe.core.doctype.user.user.get_role_profile',
 args: {
 role_profile: 'Test'
 },
 // disable the button until the request is completed
 btn: $('.primary-action'),
 // freeze the screen until the request is completed
 freeze: true,
 callback: (r) => {
 // on success
 },
 error: (r) => {
 // on error
 }
})
```

## frappe.db.get_doc

`frappe.db.get_doc(doctype, name, filters)`

Returns the Document object of `doctype` and `name`. If `name` is not provided,  
gets the first document matched by `filters`.

```js
// get doc by name
frappe.db.get_doc('Task', 'TASK00002')
 .then(doc => {
 console.log(doc)
 })

// get doc by filters
frappe.db.get_doc('Task', null, { status: 'Open' })
 .then(doc => {
 console.log(doc)
 })
```

## frappe.db.get_list

`frappe.db.get_list(doctype, { fields, filters })`

Returns a list of records of `doctype` with `fields` and `filters`.

```js
frappe.db.get_list('Task', {
 fields: ['subject', 'description'],
 filters: {
 status: 'Open'
 }
}).then(records => {
 console.log(records);
})
```

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)`

Returns a document's field value or a list of values.

```js
// single value
frappe.db.get_value('Task', 'TASK00004', 'status')
 .then(r => {
 console.log(r.message.status) // Open
 })

// multiple values
frappe.db.get_value('Task', 'TASK00004', ['status', 'subject'])
 .then(r => {
 let values = r.message;
 console.log(values.status, values.subject)
 })

// using filters
frappe.db.get_value('Task', {status: 'Open'}, 'subject')
 .then(r => {
 let values = r.message;
 console.log(values.subject)
 })
```

## frappe.db.get_single_value

`frappe.db.get_single_value(doctype, field)`

Returns a field value from a Single DocType.

```js
frappe.db.get_single_value('System Settings', 'time_zone')
 .then(time_zone => {
 console.log(time_zone);
 })
```

## frappe.db.set_value

`frappe.db.set_value(doctype, docname, fieldname, value, callback)`

Sets a document's property using `frappe.get_doc` and `doc.save` on server.

```js
// update a field's value
frappe.db.set_value('Task', 'TASK00004', 'status', 'Open')
 .then(r => {
 let doc = r.message;
 console.log(doc);
 })

// update multiple fields
frappe.db.set_value('Task', 'TASK00004', {
 status: 'Working',
 priority: 'Medium'
}).then(r => {
 let doc = r.message;
 console.log(doc);
})
```

## frappe.db.insert

`frappe.db.insert(doc)`

Insert a new document.

```js
frappe.db.insert({
 doctype: 'Task',
 subject: 'New Task'
}).then(doc => {
 console.log(doc);
})
```

## frappe.db.count

`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.

```js
// total number of Task records
frappe.db.count('Task')
 .then(count => {
 console.log(count)
 })

// total number of Open Tasks
frappe.db.count('Task', {
 filters: {
 status: 'Open'
 }
}).then(count => {
 console.log(count);
})
```

## frappe.db.delete_doc

`frappe.db.delete_doc(doctype, name)`

Delete a document identified by `doctype` and `name`.

```js
frappe.db.delete_doc('Task', 'TASK00004')
```

## frappe.db.exists

`frappe.db.exists(doctype, name)`

Returns true if a document record exists.

```js
frappe.db.exists('Task', 'TASK00004')
 .then(exists => {
 console.log(exists) // true
 })
```

<!-- page: framework/framework__user__en__api__tree.md -->
---
title: "Tree\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/tree"
updated: "2026-02-17"
---

The Tree View is generated for all DocTypes that has Is Tree enabled.

![Tree View](/files/treeview.png)
*Tree View*

## Standard Tree JS

To customize the Tree View you must have a `{doctype}_tree.js` file in the doctype directory.
Below are all the options that can be customized.

For instance, if you want to configure the Account DocType, you'll have to create a file `account_tree.js` with the following contents.

```js
frappe.treeview_settings["Account"] = {
	breadcrumb: "Accounting",
	title: "Chart of Accounts",

	filters: [
		{
			fieldname: "company",
			fieldtype: "Select",
			label: "Company",
			options: "Company 1\nCompany 2",
			on_change: handle_company_change(),
		},
	],

	get_tree_nodes: "path.to.whitelisted_method.get_children",
	add_tree_node: "path.to.whitelisted_method.handle_add_account",

	fields: [
		{
			fieldtype: "Data",
			fieldname: "account_name",
			label: "New Account Name",
			reqd: true,
		},
		{
			fieldtype: "Link",
			fieldname: "account_currency",
			label: "Currency",
			options: "Currency",
		},
		{
			fieldtype: "Check",
			fieldname: "is_group",
			label: "Is Group",
		},
	],

	ignore_fields: ["parent_account"],

	menu_items: [
		{
			label: "New Company",
			action: function () {
				frappe.new_doc("Company", true);
			},
			condition: "frappe.boot.user.can_create.indexOf('Company') !== -1",
		},
	],

	onload: function (treeview) {},

	post_render: function (treeview) {},

	onrender: function (node) {},

	on_get_node: function (nodes) {},

	extend_toolbar: true,

	toolbar: [
		{
			label: "Add Child",
			condition: function (node) {
				return node && node.is_group;
			},
			click: function (node) {
				frappe.treeview_settings["Account"].add_node(node);
			},
			btnClass: "hidden-xs",
		},
	],
};
```

<!-- page: framework/framework__user__en__api__utils.md -->
---
title: "Utility Functions"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/utils"
updated: "2026-02-26"
---

Frappe Framework comes with various utility functions to handle common operations for managing site-specific DateTime management, date and currency formatting, PDF generation, and much more.

These utility methods can be imported from the `frappe.utils` module (and its nested modules like `frappe.utils.logger` and `frappe.utils.data`) in any Python file of your Frappe App. This list is not at all exhaustive, you can take a peek at the Framework codebase to see what's available.

## now

`now()`

Returns the current datetime in the format **yyyy-mm-dd hh:mm:ss**

```
from frappe.utils import now

now() # '2021-05-25 06:38:52.242515'
```

## getdate

`getdate(string_date=None)`

Converts `string_date` (yyyy-mm-dd) to `datetime.date` object. If no input is provided, current date is returned. Throws an exception if `string_date` is an invalid date string.

```
from frappe.utils import getdate

getdate() # datetime.date(2021, 5, 25)
getdate('2000-03-18') # datetime.date(2000, 3, 18)
```

## today

`today()`

Returns current date in the format **yyyy-mm-dd**.

```
from frappe.utils import today

today() # '2021-05-25'
```

## add_to_date

`add_to_date(date, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0, as_string=False, as_datetime=False)`

```
`date`: A string representation or `datetime` object, uses the current `datetime` if `None` is passed
`as_string`: Return as string
`as_datetime`: If `as_string` is True and `as_datetime` is also True, returns a `datetime` string otherwise just the `date` string.
```

This function can be quite handy for doing date/datetime deltas, for instance, adding or substracting certain number of days from a particular date/datetime.

```
from datetime import datetime # from python std library
from frappe.utils import add_to_date

today = datetime.now().strftime('%Y-%m-%d')
print(today) # '2021-05-21'

after_10_days = add_to_date(datetime.now(), days=10, as_string=True)
print(after_10_days) # '2021-05-31'

add_to_date(datetime.now(), months=2) # datetime.datetime(2021, 7, 21, 15, 31, 18, 119999)
add_to_date(datetime.now(), days=10, as_string=True, as_datetime=True) # '2021-05-31 15:30:23.757661'
add_to_date(None, years=6) # datetime.datetime(2027, 5, 21, 15, 32, 31, 652089)
```

## date_diff

`date_diff(date_2, date_1)`

Return the difference between the given two dates in days.

```
from frappe.utils import add_to_date, today, date_diff
date_1 = today()
date_2 = add_to_date(date_1, days=10)

print(date_diff(date_2, date_1)) #10
```

## days_diff

`days_diff(date_2, date_1)`

Return the difference between the given two dates in days.

```
from frappe.utils import add_to_date, today, days_diff
date_1 = today()
date_2 = add_to_date(date_1, days=10)

print(days_diff(date_2, date_1)) #10
```

## month_diff

`month_diff(date_2, date_1)`

Return the difference between the given two dates in months.

```
from frappe.utils import add_to_date, month_diff
date_1 = "2024-07-01"
date_2 = add_to_date(date_1, days=60)

print(month_diff(date_2, date_1)) #2
```

## pretty_date

`pretty_date(iso_datetime)`

Takes an ISO time and returns a string representing how long ago the date represents. Very common in communication applications like instant messengers.

```
from frappe.utils import pretty_date, now, add_to_date

pretty_date(now()) # 'just now'

# Some example outputs:

# 1 hour ago
# 20 minutes ago
# 1 week ago
# 5 years ago
```

## format_duration

`format_duration(seconds, hide_days=False)`

Converts the given duration value in seconds (float) to duration format.

```
from frappe.utils import format_duration

format_duration(50) # '50s'
format_duration(10000) # '2h 46m 40s'
format_duration(1000000) # '11d 13h 46m 40s'

# Convert days to hours
format_duration(1000000, hide_days=True) # '277h 46m 40s'
```

## comma_and

`comma_and(some_list, add_quotes=True)`

Given a list or tuple `some_list`, returns a string of the format `1st item, 2nd item, .... and last item`. This function uses `frappe._`, so you don't have to worry about the translations for the word `and`. If `add_quotes` is `False`, returns the items without quotes, with quotes otherwise. If the type of `some_list` passed as an argument is something other than a list or tuple, it (`some_list`) is returned as it is.

```
from frappe.utils import comma_and

comma_and([1, 2, 3]) # "'1', '2' and '3'"
comma_and(['Apple', 'Ball', 'Cat'], add_quotes=False) # 'Apple, Ball and Cat'
comma_and('abcd') # 'abcd'
```

> There is also a `comma_or` function which is similar to `comma_and` except the separator, which is `or` in the case of `comma_or`.

## money_in_words

`money_in_words(number, main_currency=None, fraction_currency=None)`

```
`number`: A floating point money amount
`main_currency`: Uses this as the main currency. If not given, tries to fetch from default settings or uses `INR` if not found there.
```

This function returns string in words with currency and fraction currency.

```
from frappe.utils import money_in_words

money_in_words(900) # 'INR Nine Hundred and Fifty Paisa only.'
money_in_words(900.50) # 'INR Nine Hundred and Fifty Paisa only.'
money_in_words(900.50, 'USD') # 'USD Nine Hundred and Fifty Centavo only.'
money_in_words(900.50, 'USD', 'Cents') # 'USD Nine Hundred and Fifty Cents only.'
```

## validate_json_string

`validate_json_string(string)`

Raises `frappe.ValidationError` if the given `string` is a valid JSON (JavaScript Object Notation) string. You can use a `try-except` block to handle a call to this function as shown the code snippet below.

```
import frappe
from frappe.utils import validate_json_string

# No Exception thrown
validate_json_string('[]')
validate_json_string('[{}]')
validate_json_string('[{"player": "one", "score": 199}]')

try:
    # Throws frappe.ValidationError
    validate_json_string('invalid json')
except frappe.ValidationError:
    print('Not a valid JSON string')
```

## random_string

`random_string(length)`

This function generates a random string containing `length` number of characters. This can be useful for cryptographic or secret generation for some cases.

```
from frappe.utils import random_string

random_string(40) # 'mcrLCrlvkUdkaOe8m5xMI8IwDB8lszwJsWtZFveQ'
random_string(6) # 'htrB4L'
random_string(6) #'HNRirG'
```

## mask_string

`mask_string(input_string, mask_char="*", show_first=4, show_last=3)`

Masks a string for privacy protection by hiding middle chars while showing configurable first and last chars for identification purposes.

```
from frappe.utils import mask_string

mask_string("1234567890")  # "1234***890"
mask_string("12345")       # "******"
mask_string("1234567890", mask_char="#", show_first=2, show_last=2)  # "12####90"
```

## unique

`unique(seq)`

`seq`: An iterable / Sequence

This function returns a list of elements of the given sequence after removing the duplicates. Also, preserves the order, unlike: `list(set(seq))`.

```
from frappe.utils import unique

unique([1, 2, 3, 1, 1, 1]) # [1, 2, 3]
unique('abcda') # ['a', 'b', 'c', 'd']
unique(('Apple', 'Apple', 'Banana', 'Apple')) # ['Apple', 'Banana']
```

## get_pdf

`get_pdf(html, options=None, output=None)`

```
`html`: HTML string to render
`options`: An optional `dict` for configuration
`output`: A optional `PdfFileWriter` object.
```

This function uses `pdfkit` and `pyPDF2` modules to generate PDF files from HTML. If `output` is provided, appends the generated pages to this object and returns it, otherwise returns a `byte` stream of the PDF.

For instance, generating and returning a PDF as response to a web request:

```
import frappe
from frappe.utils.pdf import get_pdf

@frappe.whitelist(allow_guest=True)
def generate_invoice():
    cart = [{
        'Samsung Galaxy S20': 10,
        'iPhone 13': 80
    }]

    html = '<h1>Invoice from Star Electronics e-Store!</h1>'

    # Add items to PDF HTML
    html += '<ol>'
    for item, qty in cart.items():
        html += f'<li>{item} - {qty}</li>'
    html += '</ol>'

    # Attaching PDF to response
    frappe.local.response.filename = 'invoice.pdf'
    frappe.local.response.filecontent = get_pdf(html)
    frappe.local.response.type = 'pdf'
```

## get_abbr

`get_abbr(string, max_len=2)`

Returns an abbrivated (initials only) version of the given `string` with a maximum of `max_len` letters. It is extensively used in Frappe Framework and ERPNext to generate thumbnail or placeholder images.

```
from frappe.utils import get_abbr

get_abbr('Gavin') # 'G'
get_abbr('Coca Cola Company') # 'CC'
get_abbr('Mohammad Hussain Nagaria', max_len=3) # 'MHN'
```

## validate_url

`validate_url(txt, throw=False, valid_schemes=None)`

```
`txt`: A string to check validity
`throw`: Weather to throw an exception if `txt` does not represent a valid URL, `False` by default
`valid_schemes`: A string or an iterable (list, tuple or set). If provided, checks the given URL's scheme against this.
```

This utility function can be used to check if a string represents a valid URL address.

```
from frappe.utils import validate_url

validate_url('google') # False
validate_url('https://google.com') # True
validate_url('https://google.com', throw=True) # throws ValidationError
```

## validate_email_address

`validate_email_address(email_str, throw=False)`

Returns a string containing the email address or comma-separated list of valid email addresses present in the given `email_str`. If `throw` is `True`, `frappe.InvalidEmailAddressError` is thrown in case of no valid email address in present in the given string else an empty string is returned.

```
from frappe.utils import validate_email_address

# Single valid email address
validate_email_address('rushabh@erpnext.com') # 'rushabh@erpnext.com'
validate_email_address('other text, rushabh@erpnext.com, some other text') # 'rushabh@erpnext.com'

# Multiple valid email address
validate_email_address(
    'some text, rushabh@erpnext.com, some other text, faris@erpnext.com, yet another no-emailic phrase.'
) # 'rushabh@erpnext.com, faris@erpnext.com'

# Invalid email address
validate_email_address('some other text') # ''
```

## validate_phone_number

`validate_phone_number(phone_number, throw=False)`

Returns `True` if `phone_number` (string) is a valid phone number. If `phone_number` is invalid and `throw` is `True`, `frappe.InvalidPhoneNumberError` is thrown.

```
from frappe.utils import validate_phone_number

# Valid phone numbers
validate_phone_number('753858375') # True
validate_phone_number('+91-75385837') # True

# Invalid phone numbers
validate_phone_number('invalid') # False
validate_phone_number('87345%%', throw=True) # InvalidPhoneNumberError
```

## frappe.cache()

`cache()`

Returns the redis connection, which is an instance of class `RedisWrapper` which is inherited from the `redis.Redis` class. You can use this connection to use the Redis cache to store/retrieve key-value pairs.

```
import frappe

cache = frappe.cache()

cache.set('name', 'frappe') # True
cache.get('name') # b'frappe'
```

## frappe.sendmail()

`sendmail(recipients=[], sender="", subject="No Subject", message="No Message", as_markdown=False, template=None, args=None, **kwargs)`

```
`recipients`: List of recipients
`sender`: Email sender. Default is current user or default outgoing account
`subject`: Email Subject
`message`: (or `content`) Email Content
`as_markdown`: Convert content markdown to HTML
`template`: Name of html template (jinja) from templates/emails folder
`args`: Arguments for rendering the template
```

For most cases, the above arguments are sufficient but there are many other keyword arguments that can be passed to this function. To see all the keyword arguments, please have a look the implementation of this function (`frappe/__init__.py`).

This function can be used to send email using user's default **Email Account** or global default **Email Account**.

```
import frappe

recipients = [
    'gavin@erpnext.com',
    'hussain@erpnext.com'
]

frappe.sendmail(
    recipients=recipients,
    subject=frappe._('Birthday Reminder'),
    template='birthday_reminder',
    args=dict(
        reminder_text=reminder_text,
        birthday_persons=birthday_persons,
        message=message,
    ),
    header=_('Birthday Reminder 🎂')
)
```

Sample Jinja template file:

```
<!-- templates/emails/birthday_reminder.html -->
<div>
<div class="gray-container text-center">
<div>
 {% for person in birthday_persons %}
 {% if person.image %}
 <img src="{{ person.image }}" title="{{ person.name }}">
 {% endif %}
 {% endfor %}
 </div>
<div style="margin-top: 15px;">
<span>{{ reminder_text }}</span>
<p class="text-muted">{{ message }}</p>
</div>
</div>
```

### Attaching Files

You can easily attach files to your email by passing a list of attachments to the `sendmail` function:

```
frappe.sendmail(
    ["faris@frappe.io", "hussain@frappe.io"],
    message="## hello, *bro*"
    attachments=[{"file_url": "/files/hello.png"}],
    as_markdown=True
)
```

Notice how attachments are a list of dictionaries having a key `file_url`. You can find this `file_url` in a `File` document's `file_url` field.

## filelock

File lock can be used to synchronize processes to avoid race conditions.

Example: Writing to a file can cause race condition if multiple writers are trying to write to a file. So we create a named lock so processes can see the lock and wait until it's avialable for writing.

```
from frappe.utils.synchronization import filelock

def update_important_config(config, file):
    with filelock("config_name"):
        json.dumps(config, file)
```

## get_filtered_list_url

`get_filtered_list_url(doctype, docnames=None)`

Helpful when multiple documents are created and you want to show the user all of them together in List View.

```py
from frappe.utils import get_filtered_list_url

get_filtered_list_url("Work Order", [
    "MFG-WO-2025-00027",
    "MFG-WO-2025-00028",
    "MFG-WO-2025-00029"
])
# → 'http://<site>/app/work-order?name=["in",["MFG-WO-2025-00027","MFG-WO-2025-00028","MFG-WO-2025-00029"]]'
```

## get_filtered_list_link

`get_filtered_list_link(doctype, docnames=None, label=None)`

Helpful when multiple documents are created and instead of showing long msg dialog links, you show one clean link.

```py
from frappe.utils import get_filtered_list_link

get_filtered_list_link("Work Order", [
    "MFG-WO-2025-00027",
    "MFG-WO-2025-00028",
])
# → '<a href="http://<site>/app/work-order?name=[...]">Work Order</a>'
```

<!-- page: framework/framework__user__en__apps-page.md -->
---
title: "Apps Page"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/apps-page"
updated: "2026-02-17"
---

The Apps Page provides a quick navigation interface for accessing all the apps installed on your site. By default, all Frappe apps installed on your site will appear on this page.

![](/files/Apps%20Page.png)

## How can we show our custom apps on apps page?

You can include it by adding the following configuration in your app’s hooks.py. Below is the example of Frappe CRM app.

Here `has_permission` option is used to show/hide app icon based on app based business logic. E.g. Hide icon if user is a Website User.

```Python
# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [{
    "name": "crm",
    "logo": "/assets/crm/logo.png",
    "title": "CRM",
    "route": "/crm",
    "has_permission": "crm.api.check_app_permission"
}]
```

> It is supported in v15 and above

## Setting a default app

You can configure a default app, which means users will be taken directly to that app upon logging into the site. If no default app is set, users will see the Apps Page by default.

### Default app configuration can be done at two levels:
1. User Level: Allows individual users to set their preferred default app.
	![](/files/SetAsDefault.png)
    ![](/files/UserLevel.jpeg)
2.	System Level: Sets a global default app for all users.
    ![](/files/SystemLevel.png)

<!-- page: framework/framework__user__en__audit-trail.md -->
---
title: "Audit Trail"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/audit-trail"
updated: "2026-02-17"
---

#### **Description**

A tool for viewing the changes made to a submittable doctype across multiple amended versions. In a case where a submittable document is cancelled and amended, tracking changes made to the document becomes difficult using the Version doctype since the name of the document changes. Audit Trail can be used to view **atmost 5 previously amended versions** of a submittable doctype.

#### **Steps**

1. Select the type of the document in the **Doctype** field.
2. Select the name of the document in the **Document** field.
3. Optionally, select the start and end dates in order to show the amended documents within the specified date range.
4. Click on the Compare button to view the Audit Trail for the selected document.



---

**Fields Changed**

Values for the fields changed across the different versions.

![Screenshot 2023-12-03 at 5.32.42 PM](/files/Screenshot 2023-12-03 at 5.32.42 PM.png "Screenshot 2023-12-03 at 5.32.42 PM.png")  


**Rows Updated**

Values for the child table fields changed across the different versions.

![Screenshot 2023-12-03 at 5.32.57 PM](/files/Screenshot 2023-12-03 at 5.32.57 PM.png "Screenshot 2023-12-03 at 5.32.57 PM.png")  


**Rows Added / Rows Removed**

Rows added or removed for every child table across the different versions.

![Screenshot 2023-12-03 at 5.33.08 PM](/files/Screenshot 2023-12-03 at 5.33.08 PM.png "Screenshot 2023-12-03 at 5.33.08 PM.png")  

<!-- page: framework/framework__user__en__basics.md -->
---
title: "What is Frappe Framework?"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics"
updated: "2026-02-17"
---

Frappe is a full stack, batteries-included, web framework written in Python and Javascript.

It is the framework which powers [ERPNext](https://erpnext.com). It is pretty generic and can be used to build database driven apps.

Meta-data driven
----------------

Meta-data is a first class citizen in Frappe. It is used to generate database tables, design forms and configure a lot of features. Meta-data is stored in a **Model** which is known as DocType in Frappe.

Let's take an example of a DocType called **ToDo**. It will contain fields like `status`, `date` and `description`.

Here is what the `todo.json` may look like:


```
{
 "name": "ToDo",
 "module": "Desk",
 "field_order": [
  "status",
  "date",
  "description"
 ],
 "fields": [
  {
   "default": "Open",
   "fieldname": "status",
   "fieldtype": "Select",
   "in_global_search": 1,
   "in_list_view": 1,
   "in_standard_filter": 1,
   "label": "Status",
   "options": "Open
Closed"
  },
  {
   "fieldname": "date",
   "fieldtype": "Date",
   "in_standard_filter": 1,
   "label": "Due Date"
  },
  {
   "fieldname": "description",
   "fieldtype": "Text Editor",
   "in_global_search": 1,
   "label": "Description",
   "reqd": 1
  }
 ]
}
  

```
A configuration like this will generate a database table whose schema might look like


```
MariaDB [_baa0f26509a564b6]> desc tabToDo;
+-----------------------+--------------+------+-----+---------+-------+
| Field                 | Type         | Null | Key | Default | Extra |
+-----------------------+--------------+------+-----+---------+-------+
| name                  | varchar(140) | NO   | PRI | NULL    |       |
| creation              | datetime(6)  | YES  |     | NULL    |       |
| modified              | datetime(6)  | YES  | MUL | NULL    |       |
| modified_by           | varchar(140) | YES  |     | NULL    |       |
| owner                 | varchar(140) | YES  |     | NULL    |       |
| docstatus             | int(1)       | NO   |     | 0       |       |
| idx                   | int(8)       | NO   |     | 0       |       |
| status                | varchar(140) | YES  |     | Open    |       |
| description           | longtext     | YES  |     | NULL    |       |
| date                  | date         | YES  |     | NULL    |       |
+-----------------------+--------------+------+-----+---------+-------+
  

```
Rich Admin Interface
--------------------

Frappe does not only manage the backend, it also comes with a feature rich admin interface called the Desk. When you create a DocType in Frappe, a number of views are generated for it. Here are some of them:

The List View supports paging, filtering, sorting and bulk editing records.

![List View](/files/list-view.png) *List View*

The Form View used for editing records also supports file attachments, PDF format, comments, email, etc.

![Form View](/files/form-view.png) *Form View*

The Report Builder supports adding columns, grouping, filtering, sorting and saving it as a configuration.

![Report Builder](/files/report-builder.png) *Report Builder*

Users, Roles and Permissions
----------------------------

Frappe comes with User and Role management out of the box. A **User** is someone who can login to the system and perform authorized actions like creating, updating or deleting records. A **Role** is a mapping of DocTypes and actions allowed to perform on it.

![Role Permission Manager](/files/permission-manager.png)  


Python, JS and MariaDB
----------------------

Frappe Framework uses Python for the backend. It comes with a simple yet powerful ORM as an abstraction over CRUD operations. The default database is MariaDB. Postgres support is in beta.


```
doc = frappe.new_doc('ToDo')
doc.description = 'Buy Eggs'
doc.insert()
  

```
The front-end is an SPA built using Javascript (jQuery).

Realtime
--------

Frappe also supports realtime pub/sub events using NodeJS and socketio.


```
# server
frappe.publish_realtime('update_progress', {
    'progress': 42,
    'total': 100
})

# client
frappe.realtime.on('update_progress', (data) => {
    console.log(data)
});
  

```
Background Jobs
---------------

Frappe also supports background job queuing based on Python RQ.


```
frappe.enqueue('frappe.job.run_job', arg1='Test', arg2='Test2')
  

```
Email
-----

Frappe supports sending and receiving emails, which can also be linked to individual documents.

![Email](/files/email.png)  


Printing
--------

Frappe supports generating PDF print formats based on Jinja Templates. It also comes with a drag-and-drop Print Format Builder.

![Print Preview](/files/print-view.png) *Print Preview*

![Print Format Builder](/files/print-format-builder.png) *Print Format Builder*

Batteries Included
------------------

Frappe has tons of features that are essential to building a modern complex app. Only the basic features are introduced here. The rest of this guide will cover them and other advanced features with much finer detail, so make sure to read it all.

<!-- page: framework/framework__user__en__basics__apps.md -->
---
title: "Apps\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/apps"
updated: "2026-02-17"
---

A Frappe app is a python package that uses the Frappe framework. Frappe apps live
in a directory called `apps` in the `frappe-bench` directory.

The default app `frappe` is a frappe app which acts as the framework for all
apps. A Frappe app should have an entry in `apps.txt`.

## Creating an App

Frappe ships with a boilerplate for a new app. To create a new app, run the
following command from the `frappe-bench` directory.

```sh
$ bench new-app custom_app
INFO:bench.app:creating new app custom_app
App Title (default: Custom App):
App Description: Custom Frappe App
App Publisher: John Doe
App Email: custom@johndoe.com
App Icon (default 'octicon octicon-file-directory'):
App Color (default 'grey'):
App License (default 'MIT'):
'custom_app' created at /Users/johndoe/frappe-bench/apps/custom_app
INFO:bench.app:installing custom_app
INFO:bench.utils:./env/bin/pip install -q -e ./apps/custom_app
```

The `custom_app` directory will now be created in the `apps` directory. It will
also be added to `apps.txt`.

## Directory structure

The directory structure of the app will look something like this:

```sh
apps/custom_app
├── MANIFEST.in
├── README.md
├── custom_app
│ ├── __init__.py
│ ├── config
│ │ ├── __init__.py
│ │ ├── desktop.py
│ │ └── docs.py
│ ├── custom_app
│ │ └── __init__.py
│ ├── hooks.py
│ ├── modules.txt
│ ├── patches.txt
│ ├── public
│ │ ├── css
│ │ └── js
│ ├── templates
│ │ ├── __init__.py
│ │ └── includes
│ └── www
├── license.txt
├── requirements.txt
├── dev-requirements.txt
├── package.json
└── setup.py
```

### requirements.txt

This file stores the list of python dependencies. When this app is installed,
it's dependencies will also get installed.

### dev-requirements.txt [Optional]

This file stores the list of python development dependencies. Syntax of this
file is same as requirements.txt. If developer mode is enabled, then
installing the app will also install its development dependencies.

### package.json

This file is used to keep track of node dependencies. Learn more about it
[here](https://docs.npmjs.com/files/package.json).

### customapp

This is the directory where the source files are stored.

### customapp/customapp

When you create a new app, a module with the same name is also created within
the app. This is the directory which corresponds to that module.

### customapp/hooks.py

This file is used to hook into frappe events and extend or override standard
behaviour by frappe.

Learn more about [hooks](/framework/v14/user/en/python-api/hooks).

### customapp/modules.txt

Every frappe app is organized into different modules. Every DocType is part of a
module. These modules are listed in this file.

Learn more about [modules](/framework/v14/user/en/basics/doctypes/modules).

### customapp/patches.txt

This file is used to store references to patches that run in database migrations.
These patches are run in order, and they are run only once.

Learn more about [Database Migrations](https://docs.frappe.io/framework/user/en/database-migrations#writing-a-patch).

### customapp/public

The public folder is a static folder and can be served by nginx in production.
Files put here can be accessed via the url `/assets/custom_app/**/*`.

For example, the file `public/img/logo.png` is accessible via the url
`/assets/custom_app/img/logo.png`.

This folder is used to store static assets used directly in the client side like
JS, CSS and Images.

### customapp/templates

The templates folder is used to write and manage Jinja Templates. They can be
organized in any way you want. This directory is directly scanned when you use
them in Jinja templates.

For example, when you include a partial `{% include "templates/navbar/navbar.html" %}`,
it will first scan this directory and then fallback to other apps.

### customapp/www

Files in this directory are directly mapped to portal pages and the URLs match the
directory structure.

Learn more about [portal pages](/framework/v14/user/en/portal-pages).

## Installing an app into a site

To use an app, it must be installed on a site. Installing an app on a site means
creating the models that are bundled with the app into the site, which means
creating database tables in the site database.

To install an app onto a site, run the following command:

```sh
$ bench --site site_name install-app custom_app

Installing custom_app...
```

To check whether the app was installed correctly, run the following command:

```
$ bench --site site_name list-apps
frappe
custom_app
```

<!-- page: framework/framework__user__en__basics__architecture.md -->
---
title: "Architecture\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/architecture"
updated: "2026-02-17"
---


Frappe Framework is a full-stack web based framework and it includes all the
tools needed to deploy a site into production. Database, caching, background
jobs, realtime notifications, etc are all configured when you set up a Frappe
site.

Frappe framework is based on Python, so it uses the `virtualenv` to setup
isolated environments for multiple Python versions. You can also use it to
deploy sites with different Frappe versions.

The following diagram closely resembles the `frappe-bench` directory structure
and its interface with different parts of the stack.

![Architecture](/files/architecture.png)
*Architecture*

To setup a Frappe based site, you need to first install Bench. If you haven't
installed it already, check out the [Installation](/framework/v14/user/en/installation)
page.

You can create a new `frappe-bench` setup by running the following command:

```sh
bench init frappe-bench
```

This command will do the following:

1. Create a directory called `frappe-bench` and `frappe-bench/sites`, `frappe-bench/apps` within it.
1. Setup a python virtual environment under `frappe-bench/env`.
1. Create a `frappe-bench/config` folder to store redis configuration files.
1. Download `frappe` app and `pip install` it.
1. Install node packages.
1. Build JS/CSS assets.

Each `frappe-bench` setup spawns it owns web, redis and node processes.

<!-- page: framework/framework__user__en__basics__asset-bundling.md -->
---
title: "Asset Bundling\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/asset-bundling"
updated: "2026-02-17"
---


A guide to understanding how static asset bundling works in Frappe Framework.

Frappe ships with a Rich Admin UI accessible at `/app` which is an SPA written
in modern JavaScript syntax and styling which is written in SASS (`.scss`)
files. These files are not directly understandable by the browser and hence need
to be compiled before they are sent to the browser to parse and execute.

Frappe ships with an asset bundler that can compile client side assets like:

- `.js` (Modern syntax with `import` and `export`)
- `.ts` (TypeScript files)
- `.vue` (Vue single file components)
- `.css` (CSS processed using PostCSS)
- `.scss` (SASS files)
- `.sass` (SASS files with indentation syntax)
- `.styl` (Stylus files)
- `.less` (Less files)

These files are compiled to `.js` or `.css` depending on the type and are sent
to the browser.

## Building assets

To compile assets using the asset bundler, you run the following command from
the `frappe-bench` folder:

```sh
$ bench build
```

You can also run it for specific apps by giving it the `--apps` option.

```sh
# build only frappe assets
$ bench build --apps frappe

# build only frappe and erpnext assets
$ bench build --apps frappe,erpnext
```

## Watch mode

When you are working with bundled files you need the build command to run every
time you make a change to your source files. The asset bundler comes with a
watch mode where it will listen to changes in the file system and rebuild
whenever a file changes.

Running the following command will start a long-running process that watches
your files and rebuilds them as they change. It will log a line with the text
"Compiled changes..." every time it does a rebuild.

```sh
$ bench watch
Watching for changes...
1:17:28 PM: Compiled changes...
```

You can also run it for specific apps by giving it the `--apps` option.

```sh
# watch only erpnext assets
$ bench watch --apps erpnext
```

Starting with Version 14, [Desk](/framework/v14/user/en/desk) will be automatically reloaded if assets get rebuilt in watch mode. This behavior can be toggled by setting the `LIVE_RELOAD` environment variable, or changing the value for `live_reload` in [`common_site_config.json`](/framework/v14/user/en/basics/site_config#common-site-config).


## Bundle files

A bundle file is an entry point of an asset that is picked up by the bundler for
compilation. For e.g., if there is a file named `main.bundle.js` in the public
folder of your app it will be automatically picked up by the bundler and
compiled at `/assets/[app]/dist/js/main.bundle.[hash].js`. A unique hash
computed from the contents of the output is also appended to the file name which
is useful for cache-busting in browsers.

Similarly, if there is a file named `style.bundle.scss` in the public folder, it
will be compiled to `/assets/[app]/dist/css/style.bundle.css`. Notice, the
extension changed from `.scss` to `.css` because browsers can understand CSS
files but not SASS files. Bundle files can exist at any nesting level in the
`public` folder, but they will always be compiled in either `dist/js` or
`dist/css` depending upon their type. This means if there is a file at
`public/main.bundle.js` and another file at `public/src/main.bundle.js` the
compiled output of the latter will override. The bundler will also print a
warning for such collisions.

Some more examples of bundle inputs and their outputs:

| Input | Output |
| ---------------------------------------- | ----------------------------------------------- |
| `[app]/public/main.bundle.js` | `/assets/dist/[app]/js/main.bundle.[hash].js` |
| `[app]/public/src/main.bundle.js` | `/assets/dist/[app]/js/main.bundle.[hash].js` |
| `[app]/public/src/utils/utils.bundle.js` | `/assets/dist/[app]/js/utils.bundle.[hash].js` |
| `[app]/public/main.bundle.ts` | `/assets/dist/[app]/js/main.bundle.[hash].js` |
| `[app]/public/main.bundle.css` | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/styles/main.bundle.css` | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.scss` | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.sass` | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.styl` | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.less` | `/assets/dist/[app]/css/main.bundle.[hash].css` |

## Importing libraries from npm

If you are familiar with modern web development, you might need to install
3rd-party libraries from npm and use it in your project.

Let's say you want to use the `dayjs` library for working with Date and Time in
your app. You first install it using `yarn` by running the following command
from the root of your apps folder.

```sh
$ cd frappe-bench/apps/myapp
$ yarn add dayjs
```

Now, you can import it in your source files like so:

**myapp/public/main.bundle.js**
```js
import * as dayjs from 'dayjs';

console.log(dayjs())
```

## Including bundled assets in HTML

When a bundle file is compiled, the output file contains a unique hash. So, you
cannot hardcode the path of the file because the next time you make a change to
that file the hash will change. Frappe provides a couple of helpers to do this.

### Including assets in custom HTML files

The Jinja methods `include_script` and `include_style` will output the correct
path of the file including the HTML markup for `.js` and `.css` files respectively.

**index.html**

```html



 


My App

 
 {{ include_style('style.bundle.css') }}
 


 

 {{ include_script('main.bundle.js') }}
 


```

**index.html (Rendered)**

```html



 


My App



 <script type="text/javascript" src="/assets/myapp/dist/js/main.bundle.BYJXV4LB.js"></script>


```

### Including assets in app.html

If you want to include bundled assets from your app in `/app` you can use the
`app_include_js` and `app_include_css` to load them into app.html.

**[app]/hooks.py**
```py
app_include_js = ['main.bundle.js']
app_include_css = ['style.bundle.css']
```

### Get bundled asset path

If for some reason you need only the path of the bundled asset, you can use the
`bundled_asset` Jinja method to generate it.

**Jinja**
```
{{ bundled_asset('main.bundle.js') }}
```

**Rendered**
```html
/assets/myapp/dist/js/main.bundle.BYJXV4LB.js
```

### Python API

These APIs are also available in python. You can import them from jinja_globals.py.

```py
from frappe.utils.jinja_globals import bundled_asset, include_script, include_style

bundled_asset('main.bundle.js')
```

## Including bundled assets lazily in `/app`

If you want to lazy load bundled assets inside the Admin UI (`/app`) you can
use the `frappe.require` method.

```js
frappe.require('main.bundle.js').then(() => {
 // main.bundle.js is now loaded
})
```

This approach is useful when you want to load your code based on some condition.
The first page load won't be impacted and is better for performance.

## Production Mode

When deploying your app to production, you can build your assets in production
mode. In this mode, the bundler will minify the final output of your bundle
which results in smaller file sizes.

To build your assets in production mode, run the following command:
```sh
$ bench build --production
```

<!-- page: framework/framework__user__en__basics__directory-structure.md -->
---
title: "Directory structure\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/directory-structure"
updated: "2026-02-17"
---


When you initialize a new **frappe-bench** directory, you will have a directory
structure similar to:

```bash
.
├── apps
 ├── frappe
├── config
 ├── redis_cache.conf
 ├── redis_queue.conf
 └── redis_socketio.conf
├── env
├── logs
├── Procfile
└── sites
 ├── apps.txt
 ├── assets
 ├── common_site_config.json
 └── site1.local
 ├── private
 ├── public
 └── site_config.json
```

### apps

The `frappe` app and other frappe based apps live in this directory. When you
run the command `bench new-app app_name`, the app will be bootstrapped in this
directory. Your custom apps live here and you are supposed to edit/work with
them here.

Learn more about [apps](/framework/v14/user/en/basics/apps).

### sites

Sites are served from this directory. When you run the command `bench new-site
site_name`, the site will be created in this directory. Sites are distinguished
based on their directory name.

Learn more about [sites](/framework/v14/user/en/guides/basics/sites).

### logs

This directory is used to dump log files from various processes. Each log file
is named based on the process it is logged from.

### config

Frappe uses 3 Redis instances to manage caching, job queueing and socketio
communication. All of those configurations live here.

### env

The Python virtual environment live in this directory. Frappe based apps and
Python package dependencies are installed here.

### Procfile

Frappe uses Procfile based process management. The default Procfile looks
something like this:

```
redis_cache: redis-server config/redis_cache.conf
redis_socketio: redis-server config/redis_socketio.conf
redis_queue: redis-server config/redis_queue.conf
web: bench serve --port 8000

socketio: /usr/bin/node apps/frappe/socketio.js

watch: bench watch

schedule: bench schedule
worker_short: bench worker --queue short --quiet
worker_long: bench worker --queue long --quiet
worker_default: bench worker --queue default --quiet
```

Let's see what each process is used for.

#### `redis_cache:`
Redis used for in-memory caching.

#### `redis_socketio:`
Redis used as a pub/sub between `web` and `socketio` processes for realtime communication.

#### `redis_queue:`
Redis used for managing background jobs queuing.

#### `web:`
Python web server based on [Werkzeug](https://palletsprojects.com/p/werkzeug/).

#### `socketio:`
Node server for a socketio connection with the browser for realtime communication.

#### `watch:`
Node server for bundling JS/CSS assets using [Rollup](https://rollupjs.org).
It will also rebuild files as they change.

#### `schedule:`
Job Scheduler using Python RQ.

#### `worker_short:`
Python worker with a (short) timeout of 300s.

#### `worker_long:`
Python worker with a (long) timeout of 1500s.

#### `worker_default:`
Python worker with a timeout of 300s.

<!-- page: framework/framework__user__en__basics__doctypes.md -->
---
title: "Understanding DocTypes"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes"
updated: "2026-02-17"
---

1. [Introduction](#doctype)
2. [Modules](doctypes/modules)
3. [DocField](doctypes/docfield)
4. [Naming](doctypes/naming)
5. [Controllers](doctypes/controllers)


	* [Controller Methods](doctypes/controllers#controller-methods)
	* [Controller Hooks](doctypes/controllers#controller-hooks)
6. [Child DocType](doctypes/child-doctype)
7. [Single DocType](doctypes/single-doctype)
8. [Virtual DocType](doctypes/virtual-doctype)
9. [Actions and Links](doctypes/actions-and-links)
10. [Customizing DocTypes](doctypes/customize)

Introduction
------------

A DocType is the core building block of any application based on the Frappe Framework. It describes the **Model** and the **View** of your data. It contains what fields are stored for your data, and how they behave with respect to each other. It contains information about how your data is named. It also enables rich **Object Relational Mapper (ORM)** pattern which we will discuss later in this guide. When you create a DocType, a JSON object is created which in turn creates a database table.


> ORM is just an easy way to read, write and update data in a database without writing explicit SQL statements.
> 
> 

#### Conventions

To enable rapid application development, Frappe Framework follows some standard conventions.

1. DocType is always singular. If you want to store a list of articles in the database, you should name the doctype **Article**.
2. Table names are prefixed with `tab`. So the table name for **Article** doctype is `tabArticle`.

The standard way to create a DocType is by typing *new doctype* in the search bar in the **Desk**.

![ToDo DocType](/files/todo-doctype.png) *ToDo DocType*

A DocType not only stores fields, but also other information about how your data behaves in the system. We call this **Meta**. Since this meta-data is also stored in a database table, it makes it easy to change meta-data on the fly without writing much code. Learn more about [Meta](#meta).


> A DocType is also a DocType. This means that we store meta-data as the part of the data.
> 
> 

After creating a DocType, Frappe can provide many features out-of-the-box. If you go to `/app/todo` you will be routed to the List View in the desk.

![ToDo List](/files/list-view.png) *ToDo List*

Similarly, you get a Form View at the route `/app/todo/000001`. The Form is used to create new docs and view them.

![ToDo Form](/files/form-view.png) *ToDo Form*

<!-- page: framework/framework__user__en__basics__doctypes__actions-and-links.md -->
---
title: "Actions and Links"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/actions-and-links"
updated: "2026-03-12"
---

> Added in Version 12.1  
>  
> 

Action and Links (also called Connections) are two ways to provide the end user more interaction with the document. The image below shows what they are :

![Action and Link View](/files/action-link.png)



## Actions

A DocType may have some `DocType Action` that will result in a button creation on the DocType View. Supported actions are:

1. **Server Action**: This will trigger a whitelisted server action.
2. **Route**: This will redirect to a given route.

### Configuration of Action

![Action Configuraton](/files/action-config.png)



### Configuration of Action in custom app

To call an Action in you own app, you will need a python function decorated with `frappe.whitelist` :

```
import frappe

@frappe.whitelist()
def execute_function(*args,**kwargs):
    """
 This function will be executed when the Execute Action Button will be clicked
 """
    print('Hello World')
    # The data is transmitted via keyword argument
    print(kwargs)
  

```

This code should go somewhere inside you app, typically in a file like `apps/my_app/my_app/api.py`

And then, configure the correspondant Action path :

![Custom Action Configuraton](/files/custom-app-action-config.png)



## Connections (Linked Documents)

A standard navigation aid to the DocType view is the `Connections` section on the dashboard. This helps the viewer identify at a glance which document types are connected to this DocType and can quickly create new related documents.

These links also support adding internal links (links to DocType in child tables).

### Configuration Connections

![Link Configuration](/files/link-config.png)



![Internal Link](/files/internal-link.png)



### Via script

To configure connections for a doctype in your app, create a `get_data()` function inside `<doctype>_dashboard.py`. Here's an example from the `sales_invoice_dashboard.py` of the Sales Invoice doctype from ERPNext:

```
from frappe import _


def get_data():
	return {
		"fieldname": "sales_invoice",
		"non_standard_fieldnames": {
			"Delivery Note": "against_sales_invoice",
			"Journal Entry": "reference_name",
			"Payment Entry": "reference_name",
			"Payment Request": "reference_name",
			"Sales Invoice": "return_against",
			"Auto Repeat": "reference_document",
			"Purchase Invoice": "inter_company_invoice_reference",
		},
		"internal_links": {
			"Sales Order": ["items", "sales_order"],
			"Timesheet": ["timesheets", "time_sheet"],
		},
		"internal_and_external_links": {
			"Delivery Note": ["items", "delivery_note"],
		},
		"transactions": [
			{
				"label": _("Payment"),
				"items": [
					"Payment Entry",
					"Payment Request",
					"Journal Entry",
					"Invoice Discounting",
					"Dunning",
				],
			},
			{"label": _("Reference"), "items": ["Timesheet", "Delivery Note", "Sales Order"]},
			{"label": _("Returns"), "items": ["Sales Invoice"]},
			{"label": _("Subscription"), "items": ["Auto Repeat"]},
			{"label": _("Internal Transfers"), "items": ["Purchase Invoice"]},
		],
	}
```

- `transactions` define all the connections and the respective groups to put them under.
- `internal_links` define the connections where the doctype has internal links. For example, Sales Invoice has internal links through its Item child table to the Sales Order doctype.
- `internal_and_external_links` define the connections where the doctype has both internal and external links. For example, Sales Invoice has internal links through its Item child table to the Delivery Note doctype and Sales Invoice also has external links to the Delivery Note doctype through its Item child table.
- `fieldname` defines the default fieldname to be searched while finding external links for the doctype.
- `non_standard_fieldnames` define the fieldnames and their respective doctypes to be searched while finding external links for the doctype.

This would result in the following connections:

![](/files/EgU4Cnp.png)



### Customization of Actions and Links

DocType Actions and Links are extensible via [Customize Form](customize)

<!-- page: framework/framework__user__en__basics__doctypes__child-doctype.md -->
---
title: "Child / Table DocType"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype"
updated: "2026-02-17"
---


Up until now we have only seen DocTypes that can have a single value for each field.
However, there might be a need for storing multiple records against one record, also
known as many-to-one relationships. A Child DocType is doctype which can only be linked
to a parent DocType. To make a Child DocType make sure to check **Is Child Table** while
creating the doctype.

![Child DocType](/files/child-doctype.png)

To link a Child Doctype to its parent, add another row in Parent Doctype with field
type **Table** and options as **Child Table**.

![Child Table](/files/child-table-field.png)

Child DocType records are directly attached to the parent doc.

```python
>>> person = frappe.get_doc('Person', '000001')
>>> person.as_dict()
{
 'first_name': 'John',
 'last_name': 'Doe',
 'qualifications': [
 {'title': 'Frontend Architect', 'year': '2017'},
 {'title': 'DevOps Engineer', 'year': '2016'},
 ]
}
```

## Child Properties

Child documents have special properties that define their relationship to their parent :

- `parent`: name of the parent.
- `parenttype`: DocType of the parent.
- `parentfield`: Field in the parent that links this child to it.
- `idx`: Sequence (row).

<!-- page: framework/framework__user__en__basics__doctypes__controllers.md -->
---
title: "Controllers"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/controllers"
updated: "2026-02-17"
---

A Controller is a normal Python class which extends from `frappe.model.Document` base class. This base class is the core logic of a DocType. It handles how values are loaded from the database, how they are parsed and saved back to the database.

When you create a DocType named `Person`, a python file is created by the name `person.py` and the contents look like:


```
import frappe
from frappe.model.document import Document

class Person(Document):
    pass

  

```
All the fields are available to the class as attributes.

### Controller Methods

You can add custom methods to your Controller and it will be callable using the `doc` object. For example,


```
# controller class
class Person(Document):
    def get_full_name(self):
        """Returns the person's full name"""
        return f"{self.first_name} {self.last_name}"

# somewhere in your code
>>> doc = frappe.get_doc("Person", "000001")
>>> doc.get_full_name()
John Doe
  

```
### Controller Hooks

To add custom behaviour during the lifecycle of a document, we have controller hooks.



| Method Name | Description | Insert | Save | Submit | Cancel | Update after submit |
| --- | --- | --- | --- | --- | --- | --- |
| `before_insert` | This is called before a document is prepared for insertion. | X |  |  |  |  |
| `before_naming` | This is called before the `name` property of the document is set. | X |  |  |  |  |
| `autoname` | If defined in the controller, this method is used to set `name` property of the document. | X |  |  |  |  |
| `before_validate` | This hook is called before validation, use this for auto setting missing values. | X | X | X |  |  |
| `validate` | Use this method to throw any validation errors and prevent the document from saving. | X | X | X |  |  |
| `before_save` | This method is called before the document is saved. | X | X |  |  |  |
| `before_submit` | This method is called before the document is submitted. | X |  | X |  |  |
| `before_cancel` | This method is called before the document is cancelled. |  |  |  | X |  |
| `before_update_after_submit` | This method is called when doc fields are updated on submitted document. |  |  |  |  | X |
| `db_insert` | This method inserts document in database, do not override this unless you're working on virtual DocType. | X |  |  |  |  |
| `after_insert` | This is called after the document is inserted into the database. | X |  |  |  |  |
| `db_update` | This method updates document in database, do not override this unless you're working on virtual DocType. |  | X | X | X | X |
| `on_update` | This is called when values of an existing document is updated. | X | X | X |  |  |
| `on_submit` | This is called when a document is submitted. |  |  | X |  |  |
| `on_cancel` | This is called when a submitted document is cancelled. |  |  |  | X |  |
| `on_update_after_submit` | This is called *when* a submitted document values are updated. |  |  |  |  | X |
| `on_change` | This is called when a document's values has been changed. This method is also called when db_set is performed, so operation performed in this method should be idempotent. | X | X | X | X | X |

Apart from doc events for typical actions, you can also hook into other actions.



| Method Name | Description |
| --- | --- |
| `before_rename` | This is called before a document is renamed. |
| `after_rename` | This is called after a document is renamed. |
| `on_trash` | This is called when a document is being deleted. |
| `after_delete` | This is called after a document has been deleted. |

To use a controller hook, just define a class method with that name. For e.g


```
class Person(Document):
    def validate(self):
        if self.age <= 18:
            frappe.throw("Person's age must be at least 18")

    def after_insert(self):
        frappe.sendmail(recipients=[self.email], message="Thank you for registering!")
  

```
You can also override the pre-defined document methods to add your own behaviour if the hooks aren't enough for you. For e.g to override the `save()` method,


```
class Person(Document):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # call the base save method
        do_something() # eg: trigger an API call or a Rotating File Logger that "User X has tried updating this particular record"
  

```
There are a lot of methods provided by default on the `doc` object. You can find the complete [list here](/framework/v14/user/en/api/document#document-methods).

#### 1. Create a document

To create a new document and save it to the database,


```
doc = frappe.get_doc({
    'doctype': 'Person',
    'first_name': 'John',
    'last_name': 'Doe'
})
doc.insert()

doc.name # 000001
  

```
#### 2. Load a document

To get an existing document from the database,


```
doc = frappe.get_doc('Person', '000001')

# doctype fields
doc.first_name # John
doc.last_name # Doe

# standard fields
doc.creation # datetime.datetime(2018, 9, 20, 12, 39, 34, 236801)
doc.owner # john.doe@frappeframework.com
  

```
### Document

A Document is an instance of a DocType. It usually maps to a single row in the database table. We refer to it as `doc` in code.

**Example**

Let's say we have a DocType **ToDo** with the following fields:

* `description`
* `status`
* `priority`

Now, if we want to query a document from the database, we can use the [ORM](#orm).


```
>>> doc = frappe.get_doc("ToDo", "0000001")
<todo: 0000001="">

>>> doc.as_dict()
{'name': '0000001',
 'owner': 'Administrator',
 'creation': datetime.datetime(2022, 3, 28, 18, 20, 23, 275229),
 'modified': datetime.datetime(2022, 3, 28, 18, 20, 23, 275229),
 'modified_by': 'Administrator',
 'docstatus': 0,
 'idx': 0,
 'status': 'Open',
 'priority': 'Medium',
 'color': None,
 'date': None,
 'allocated_to': None,
 'description': 'Test',
 'reference_type': None,
 'reference_name': None,
 'role': None,
 'assigned_by': 'Administrator',
 'assigned_by_full_name': 'Administrator',
 'sender': None,
 'assignment_rule': None,
 'doctype': 'ToDo'}
  

```
You get the values of `description`, `status` and `priority`, but you also get fields like `creation`, `owner` and `modified_by` which are fields added by default by the framework on all `docs`.

### Type Annotations


> Introduced in Version 15.
> 
> 

Frappe support automatically generating Python type annotations in controller files. These annotations can be used for auto-completion, reference and type-checking inside the controller file.


```
class Person(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        first_name: DF.Data
        last_name: DF.Data 
        user: DF.Link
    # end: auto-generated types
    pass
  

```
Note: These annotations are generated when creating or updating doctypes. If you modify the code block, it will get overridden on the next update.

You can configure automatic exporting in your app by adding the following hook.


```
# hooks.py

export_python_type_annotations = True
```
  


Learn more about type annotations:

* <https://docs.python.org/3/library/typing.html>
* VS Code users can install Python extension for better auto-complete - <https://code.visualstudio.com/docs/languages/python>
* Most other editors have an equivalent plugin system using LSP.

<!-- page: framework/framework__user__en__basics__doctypes__customize.md -->
---
title: "Customizing DocTypes\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/customize"
updated: "2026-02-17"
---


If you are using the same application for multiple site (tenants), each site may want specific customization on top of the DocType. For example if you have a "Customer" DocType each user may want addition Custom Fields or naming or other configuration that would be specific to them.

To allow for site-specific customization, Frappe Framework has multiple approaches

1. Custom Field: A DocType that keeps track of site-specific fields.
1. Property Setter: This keeps track of specific properties that are overridden in DocType and its children.
1. Customize Form: A view that helps you easily customize DocTypes
1. [Client Script](/framework/v14/user/en/desk/scripting/client-script): Additional client-side event handlers.
1. [Server Script](/framework/v14/user/en/desk/scripting/server-script): Additional server-side business logic.
1. Custom DocPerm: Additional Permission (handled via Role Permission Manager)

## Customize Form

Customize Form is a view that helps you override properties of a DocType and add Custom Fields via a single view.

![Customize Form](/files/customize-form.png)

When you change any properties of the DocType via Customize Form, it will not change the underlying DocType but add new custom objects to override those properties. This is done in a seamless manner.

#### Adding Custom Links and Actions

> Added in Version 13

You can also add / edit Links and Actions via Customize Form. These changes are saved in the same DocTypes (`DocType Link` and `DocType Action`) but with a `custom` property checked.

These addtional (custom) configurations are automatically applied when metadata is fetched via `frappe.get_meta`.

<!-- page: framework/framework__user__en__basics__doctypes__docfield.md -->
---
title: "DocField\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/docfield"
updated: "2026-02-17"
---


A DocField defines a property (or a field) of a DocType. You can define the column name, label, datatype and more for DocFields. For instance, a ToDo doctype has fields `description`, `status` and `priority`. These ultimately become columns in the database table `tabToDo`.

**Example**

The DocField stores meta-data about the field. Some of them are described below.

```json
[
 {
 "label": "Description", // the value shown to the user (Form, Print, etc)
 "fieldname": "description", // the property name we refer in code, also the column name
 "fieldtype": "Text Editor", // the fieldtype which also decides how to store this value
 "reqd": 1 // whether this field is mandatory
 },
 {
 "label": "Status",
 "fieldname": "status",
 "fieldtype": "Select",
 "options": [
 "Open",
 "Pending",
 "Closed"
 ]
 },
 {
 "label": "Priority",
 "fieldname": "priority",
 "fieldtype": "Select",
 "options": [ // list of options for select
 "Low",
 "Medium",
 "High"
 ],
 "default": "Low" // the default value to be set
 },
 {
 "label": "Completed By",
 "fieldname": "completed_by",
 "fieldtype": "Link",
 "options": "User",
 "depends_on": "eval: doc.status == 'Closed'", // the condition on which this field's display depends
 },
 {
 "collapsible": 1,
 "collapsible_depends_on": "eval:doc.status!='Closed'", // determines if a Section Break field is collapsible
 "fieldname": "sb_details",
 "fieldtype": "Section Break",
 "label": "Details"
 },
 {
 "fieldname": "amount",
 "fieldtype": "Currency", // Currency field
 "label": "Amount",
 "non_negative": 1, // determines whether this field value can be negative
 "options": "INR",
 }
]
```

Similar to the `depends_on` property which determines whether a field will be displayed or not,
in Version 12 we have introduced two new properties:

- `mandatory_depends_on`: If this condition is satisfied, the field will be mandatory.
- `read_only_depends_on`: If this condition is satisfied, the field will be read only.


Frappe comes with more than 30 different fieldtypes out-of-the-box.
These fieldtypes serve a variety of use-cases. You can learn more about fieldtypes in the next page.

<!-- page: framework/framework__user__en__basics__doctypes__fieldtypes.md -->
---
title: "Field Types"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes"
updated: "2026-07-16"
---

There are variety of fieldtypes available in Frappe Framework. Each one has its own use case and can be used to input and store different types of data in a document. Fieldtypes are used to render components in desk as well as web forms.

![Field Types Dropdown Menu](/files/fieldtypes.png)



#### Data

The data field will be a **simple text field**. It allows you to enter a value of up to 140 characters, making this the most generic field type.

You can enable validations for the following types of data:

1. Name
2. Email
3. Phone
4. URL

by setting the options to "Name", "Email", "Phone" or "URL" respectively.

![Data field types](/files/data-field-1.png)



Set the options to "IBAN" to enable formatting in blocks of 4 characters.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](https://docs.frappe.io/erpnext/user/manual/en/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here. You can set the `Default` value to 1 and it will be checked by default.

![Check Field Preview](/files/check-field-2.png)



![Check Field Edit](/files/check-field-1.png)



#### Select

Using the field type "Select", you can create a drop-down field. You can specify all selectable values in the *Options* field, each value separated by a new line.

One of the selectable values can be copied into the *Default* field. This value will then be selected by default in a new form.

If you enable the *Sort Options* checkbox, values will be displayed in alphabetical order (in the user's language).

The following screenshot shows how a "Select" field can be defined in the **DocType** or via **Customize Form**:

![define_select_field](/files/define_select_field.png "define_select_field.png")



And this is how it will be rendered in a new form:

![use_select_field](/files/use_select_field.png "use_select_field.png")



#### Table

With a "Table" field, you can render another DocType as a child table within your form.

First, you'll have to choose or define a DocType that has the Checkbox *Is Child Table* enabled. Then you can add a field of type "Table" and paste the name of your child table DocType into the *Options* field.

For example, ERPNext defines a child DocType called "Purchase Receipt Item" with *Is Child Table* enabled:

![define_child_table_doctype](/files/define_child_table_doctype.png "define_child_table_doctype.png")



Another DocType called "Purchase Receipt" has a field of type "Table", with *Options* set to above child doctype "Purchase Receipt Item":

![define_child_table_field](/files/define_child_table_field.png "define_child_table_field.png")



Finally, the child table will be rendered in the Purchase Receipt form:

![child_table_in_form](/files/child_table_in_form.png "child_table_in_form.png")



#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

![Field Types](/files/attach_fieldtype.png)



#### Attachment Gallery

The Attachment Gallery field displays files attached to the current document in a responsive gallery. Images appear as thumbnails and can be opened in a larger preview. Other file types appear as file cards and open in a new tab.

Users with write permission can upload and delete attachments directly from the gallery. Enabling *Read Only* hides these actions. The document must be saved before files can be uploaded.

By default, the gallery displays all attachments belonging to the document. Use *Filters* to restrict the displayed **File** records. For example, to show only PDF files:

```json
[["File", "file_type", "=", "PDF"]]
```

To show only files uploaded through a particular gallery, filter by `attached_to_field` using the gallery’s field name:

```json
[["File", "attached_to_field", "=", "marketing_assets"]]
```

Enable *Make Attachment Public (by default)* if files uploaded through the gallery should be public by default.

#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

#### Text Editor

Text Editor is a text field and renders a **WYSIWYG** editor for input. It has various text-formatting options.

![Field Types](/files/text_editor_field.png)



#### Date

This field will enable you to enter the Date in this field.

![Field Types](/files/date_fieldtype.png)



#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Once you do that, the Barcode would automatically get generated against the number.

![barcode](/files/barcode.png)



#### Button

This field lets you place a button in a document. This can be used to perform specific actions like publishing a blog post, triggering an action etc.

#### Code

This fieldtype can be used to take `code` as input. A code editor is rendered in the document form. Optionally, you can provide a langauge in the fieldtype options to enable syntax highlighting. For example, below is a `Code` type field with options set to `Python`:

You can enable basic syntax validations for following languages by setting "Option".

1. Python (for scripts)
2. PythonExpression (for simple one-line expressions that must evaluate to a value) E.g. Assignment Rule condition

Example of differences between `Python` and `PythonExpression`:

- `variable = 42` is a valid `Python` code but not a valid `PythonExpression` since the assignment doesn't evaluate to any value.
- `variable == 42` is both valid `Python` code and valid `PythonExpression` as the expresion can evaluate to some value.

![Field Types](/files/code_fieldtype.png)



#### Color

This will let the user input a color via a rendered color picker or directly input a hexadecimal color.

![Field Types](/files/color_fieldtype.png)



#### Column Break

This is a `'meta'` fieldtype that does not store any input data but can be used to indicate a column break in the document view or form.

For example,

![Field Types](/files/column_break_fieldtype_1.png)



will result into:

![Field Types](/files/column_break_fieldtype_2.png)



#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

#### Float

Float field carries numeric value, up to nine decimal places.

#### Geolocation

A Geolocation field will show a map view on which you can draw polygons, lines, and points. The data is stored as a GeoJSON [feature_collection](https://tools.ietf.org/html/rfc7946#section-3.3).

If you add a Geolocation field with the exact field name "location", you will get an additional map view (the equivalent of list view, but on a map). By the way, this also works if you create two separate fields named "latitude" and "longitude".

Note: Frappe uses the "Leaflet" library which stores coordinates as [latitude, longitude] which is the reverse of what GeoJSON usually does.

#### HTML

This will render the content entered in `Options` as HTML in the document form or view page. Here is an example:

![Field Types](/files/html_fieldtype_1.png)



will result into:

![Field Types](/files/html_fieldtype_2.png)



#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

![Field Types](/files/image_fieldtype_1.png)



will result into:

![Field Types](/files/image_fieldtype_2.png)



#### Int (Integer)

The integer field holds numeric value, without decimal place.

#### Small Text

Small Text field carries text content and has more character limit than the Data field.

#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

#### Markdown Editor

This field will allow you to add the text in markdown. This fieldtype also provides a `Preview` view of rendered HTML:

![Field Types](/files/md_fieldtype_1.png)



when preview is clicked:

![Field Types](/files/md_fieldtype_2.png)



#### Password

The password field will have decoded value in it. This type of field can be used to store sensitive data like passwords, pass phrases, secret keys etc.

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

#### Rating

This field can be used to display an interactive star rating input. The default star count shown is 5, however, this can easily be changed by entering a number ranging from 3 - 10 in the options field for that particular rating field.

![Check Field Edit](/files/rating-field.png)



You can also provide half ratings e.g 3.5 out of 5.

![Half Rating](/files/Screenshot 2021-12-20 at 4.52.09 PM.png)



#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

#### Section Break

Section Break is used to divide the form into multiple sections. Any fields that follow (and before any other `Section Break`) a `Section Break` field will be part of this new section.

![Field Types](/files/section_break_fieldtype.png)



### Tab Break

Tab Break is used to divide the form into multiple tabs. Any field that follow till the next `Tab Break` will be the part of this new tab.

![Tabs](/files/form-tabs.png)



**Note:** If the `fields` table of a DocType is not started with a Tab Break, a default Tab Break named `Details` will be used. This happens only if a DocType has atleast one `Tab Break` in the `fields` table.

#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field. Read documentation for [Signature Field](https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/articles/electronic-signature) to know more.

#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

#### Time

This is a Time field where you can define the Time in the field.

#### Duration

You can use the Duration field if you want to define a timespan.

If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form. One day is equivalent to 24 hours.

#### JSON

This creates a JSON type column in your database. Also adds syntax highlighting for Desk controls.

<!-- page: framework/framework__user__en__basics__doctypes__form_-_view_settings.md -->
---
title: "Form & View Settings"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/form_&_view_settings"
updated: "2026-02-17"
---

**View Settings**
-----------------

Title Field
-----------

A field of the DocType which will be displayed as a title in the Form

![](/files/8mYiuB1.png)

 

**Set the title field**

Enter the name of a custom field in 'Title Field'

![](/files/HafbLM1.png)

 

**Show Title in Link Fields**

You can enable **Show Title in Link Fields** to display **Title** instead of **Name** in the **Link Fields** in another doctype.

![](/files/xhk48oU.png)

 

So if a custom field of 'link' type is added in another doctype (or through customize form), then the title of the linked document will be displayed in the field instead of name.

![](/files/8vUNrEr.png)

<!-- page: framework/framework__user__en__basics__doctypes__modules.md -->
---
title: "Module\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/modules"
updated: "2026-02-17"
---


A DocType will always belong to a module, to enable easier grouping of related models.
Frappe comes with a lot of built-in modules. For e.g

1. Core - contains doctypes like DocType, DocField, Report, System Settings, etc
1. Desk - contains doctypes like ToDo, Event, Note, Kanban Board, etc
1. Email - contains doctypes like Email Account, Newsletter, Email Group, etc

Modules also helps in grouping of code files in directories. The controller files
generated by a DocType will live in it's respective Module directory.

```
frappe
├── commands
├── config
├── core
│   ├── doctype
│   │   ├── doctype
│   │   ├── docfield
│   │   ├── report
│   │   ├── system_settings
│   │   ├── ...
│   │   └── ...
│   ├── page
│   ├── report
│   └── web_form
├── desk
│   ├── doctype
│   │   ├── ...
│   │   ├── event
│   │   ├── kanban_board
│   │   ├── note
│   │   └── todo
│   ├── form
│   ├── page
```

<!-- page: framework/framework__user__en__basics__doctypes__naming.md -->
---
title: "Naming\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/naming"
updated: "2026-04-14"
---

All DocTypes in Frappe have a primary key called `name`. This is the unique ID by which you find records and manipulate them using the ORM.

## Naming Methods

You can configure how documents should be named when a new document is created. There are 9 ways of naming provided in the framework:

1. Set by user
2. Autoincrement
3. By fieldname
4. By "Naming Series" field
5. Expression
6. Expression (Old Style)
7. Random
8. UUID
9. By script

### 1. Set by user

The document name is entered manually by the user at the time of creation.

### 2. Autoincrement

The system generates a sequential numeric name by incrementing the last created document.

**Key considerations:**

- Numbering starts from 1.
- **Not gap-safe:** Deleted records are not reused. For example, if you have documents named `1`, `2`, `3`, `4` and you delete `3`, the next document will be named `5`, not `3`.
- You cannot switch to a different naming schema once this is set unless the DocType has zero documents.
- You cannot switch to this naming schema from another unless the DocType has zero documents.

![](/files/autoincrement.gif)
*Autoincrement*

### 3. By fieldname

The document name is fetched directly from the value of a specific field.

> **Note:** The value in the selected field must always be unique.

![](/files/fieldname.gif)
*By Fieldname*

### 4. By "Naming Series" field

The naming pattern is derived from a specific field in the document (usually `naming_series`).

For example, if you have a field `naming_series` in your document and its value is set to `PRE.#####`, that pattern will be used to generate the name (e.g., `PRE00001`). This value can change per document, allowing different documents within the same DocType to follow different patterns.

> **Requirement:** This works only if you have a field called `naming_series` in your DocType.

![](/files/naming-series.gif)
*By "Naming Series"*

### 5. Expression

You can provide a standard naming pattern which will be incremented automatically.

For example, if you set the pattern as `PRE-.#####`:

- The first document created will be named `PRE-00001`
- The second will be `PRE-00002`
- And so on...  
  ![](/files/expression.gif)
  *Expression*

You can use this method to flexibly configure naming schemes using multiple field values and variables. Individual parts are separated by a dot `.` .

**Example Pattern:**

```python
EXAMPLE-.MM.-test-.{fieldname1}.-.{fieldname2}.-.#####
```

This format allows you to combine:

- Static text (`EXAMPLE`, `test`)
- Date variables (`MM`, `YYYY`, `DD`, `WW`, `timestamp`)
- Field values (`{fieldname1}`)
- Auto-incrementing numbers ( `#####`)

### 6. Expression (Old Style)

> **Warning: Deprecated in v16** This method is deprecated and will be removed in version 16.

This is a highly flexible method for configuring naming schemes using multiple field values and variables. You enter this pattern directly into the **Auto Name** field in the DocType settings.

**Example Pattern:**

```
EXAMPLE-{MM}-test-{fieldname1}-{fieldname2}-{#####}
```

This format allows you to combine:

- Static text `EXAMPLE`, `test`)
- Date variables `{MM}`, `{YYYY}`, `{DD}`)
- Field values `{fieldname1}`)
- Auto-incrementing numbers `{#####}`)

### 7. Random

Generates a random alphanumeric string as the document name.  

![](/files/ramdom.gif)
*Random*

### 8. UUID

Uses a randomly generated Universally Unique Identifier (UUID v4) as the document name.

**Example:** `550e8400-e29b-41d4-a716-446655440000`  

![](/files/uuid.gif)
*UUID*

### 9. By script

You can define custom naming logic using the `autoname` controller method in your DocType's Python file. This gives you complete control over the naming process.

```
from frappe.model.naming import getseries

class Project(Document):
    def autoname(self):
    # select a project name based on customer
    prefix = f"P-{self.customer}"
    series = getseries(prefix, 3)
    self.name = f"{prefix}-{series}"
```

## By Document Naming Rule

You can also create rules for naming DocTypes by creating **Document Naming Rule.**

![](/files/imagec0c7f9.png)

You can create multiple Document Naming Rules for a particular doctype that can be applied selectively based on filters.

To define a Document Naming Rule you have to specify

1. Document Type it is being applied on
2. Priority of the rule (rules with higher priority will be applied first)
3. Conditions to apply the rule
4. Naming Rules

### Numbering

You can define various numbering prefixes for the rule based on the conditions defined. This is done by setting a prefix and the number of digits for that rule.

For example if you are creating a separate numbering for high priority todos:

1. Prefix: todo-high-
2. Digits: 3

Will lead to numbering like `todo-high-001`, `todo-high-002` and so on.

## Naming Priority

When multiple naming rules might apply, the framework prioritizes them in this order:

1. **Document Naming Rule:** Defined in the `autoname` property of the DocType.
2. **Controller Method:** Logic defined in the `autoname` method of the controller script (overrides DocType settings if defined) .

## Special Rules

1. Child DocTypes do not follow naming rules
2. Amended documents have a suffix (`-1`, `-2` etc) to the original document

<!-- page: framework/framework__user__en__basics__doctypes__single-doctype.md -->
---
title: "Single DocType\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/single-doctype"
updated: "2026-02-17"
---


A Single DocType is a DocType that has only one instance in the database. It is useful
for persisting things like *System Settings*, which don't make sense to have multiple
records.

![Single DocType](/files/single-doctype.png)

```python
>>> settings = frappe.get_doc('System Settings')
>>> settings.notification_frequency
'Daily'
```

### Schema

Single DocTypes are stored in the `tabSingles` table in the database, with each property having its own record.

Columns:

- `doctype`
- `field`
- `value`

<!-- page: framework/framework__user__en__basics__doctypes__virtual-doctype.md -->
---
title: "Virtual DocTypes"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/doctypes/virtual-doctype"
updated: "2026-02-17"
---

Virtual DocType is a feature-extension for DocType which allows developers to create DocTypes with custom data sources and DocType controller. The purpose is to define custom DocTypes in the system without creating a table in the database, while utilizing the frontend, resource APIs, and roles and permissions from the framework.

These Virtual DocTypes function exactly like normal DocTypes in the frontend and are indistinguishable for the end-user, but gives more control to the developer over the DocType's data source. With this, the data source for a Virtual DocType can be anything: an external API, a secondary database, JSON or CSV files, etc. This enables the developers to plug-in database backends other than MariaDB and Postgres, and makes the Frappe Framework even more powerful!

Note: `frappe.db.*` calls work only with site's database connection. You'll need to implement methods to achieve direct query to data store used by Virtual DocType.

Creating a Virtual DocType
--------------------------

To create a Virtual DocType, just select the Virtual DocType checkbox while creating the DocType:

![Virtual DocType](/files/virtual_doctype.png)  


#### Creating a Custom Controller

As an example, the following controller code uses a JSON file as the DocType datasource:


```
class VirtualDoctype(Document):
    """This is a virtual doctype controller for demo purposes.

 - It uses a single JSON file on disk as "backend".
 - Key is docname and value is the document itself.

 Example:
 {
 "doc1": {"name": "doc1", ...}
 "doc2": {"name": "doc2", ...}
 }
 """

    DATA_FILE = "data_file.json"

 @staticmethod
    def get_current_data() -> dict[str, dict]:
        """Read data from disk"""
        if not os.path.exists(VirtualDoctype.DATA_FILE):
            return {}

        with open(VirtualDoctype.DATA_FILE) as f:
            return json.load(f)

 @staticmethod
    def update_data(data: dict[str, dict]) -> None:
        """Flush updated data to disk"""
        with open(VirtualDoctype.DATA_FILE, "w+") as data_file:
            json.dump(data, data_file)

    def db_insert(self, *args, **kwargs):
        d = self.get_valid_dict(convert_dates_to_str=True)

        data = self.get_current_data()
        data[d.name] = d

        self.update_data(data)

    def load_from_db(self):
        data = self.get_current_data()
        d = data.get(self.name)
        super(Document, self).__init__(d)

    def db_update(self, *args, **kwargs):
        # For this example insert and update are same operation,
        # it might be different for you.
        self.db_insert(*args, **kwargs)

    def delete(self):
        data = self.get_current_data()
        data.pop(self.name, None)
        self.update_data(data)

 @staticmethod
    def get_list(args):
        data = VirtualDoctype.get_current_data()
        return [frappe._dict(doc) for name, doc in data.items()]

 @staticmethod
    def get_count(args):
        data = VirtualDoctype.get_current_data()
        return len(data)

 @staticmethod
    def get_stats(args):
        return {}
  

```
You can read about the interface requriements and explanation in the [interface file](https://github.com/frappe/frappe/blob/develop/frappe/model/virtual_doctype.py). To integrate other datasources with the Virtual DocType, you will need to add controller methods defining the database access.

#### Outcome

The frontend for Virtual DocTypes remain unchanged

![Virtual DocType Form](/files/virtual_doctype_form.png)  


All the /api/resource methods defined by the framework are compatible with Virtual DocTypes.


> Added in Version 13
> 
> 
