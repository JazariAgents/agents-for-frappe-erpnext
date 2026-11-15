<!-- Frappe documentation: framework, part 4 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__api__chart.md -->
---
title: "Chart API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/chart"
updated: "2026-02-17"
---


Frappe provides easy-to-use and fully configurable SVG charts. You can learn about them in the Frappe Chart's [documentation](https://frappe.io/charts).

## frappe.ui.RealtimeChart

`new frappe.ui.RealtimeChart(dom_element, event_name, max_label_count, data)`

Creates a new RealtimeChart instance that adds real-time data update functionality on top of the Frappe Chart API.

`dom_element`: HTML Element to be used to render the Chart.
`event_name`: Socket event which will provide the data stream.
`max_label_count`: Maximum number of labels allowed on the x-axis.
`data`: Data for the chart to be initialized with.

```js
// Empty data array
const data = {
 datasets: [
 {
 name: "Some Data",
 values: [],
 },
 ],
};

// Realtime Chart initialization
let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8, {
 title: "My Realtime Chart",
 data: data,
 type: "line",
 height: 250,
 colors: ["#7cd6fd", "#743ee2"]
});
```

Here is the sample client code to render a chart over the specified socket event.

The following python code can be executed as a cron job using [Hook](https://frappeframework.com/docs/v14/user/en/python-api/hooks) functionality.

```py
data = {
 'label': 1,
 'points': [10]
}
frappe.publish_realtime('test_event', data)
```

The `label` key specifies the label to be appended in the Chart. The `points` key specifies the array of points to be plotted. The number of values in the `points` array depends on the number of datasets.

This would produce a Chart like

[Screenshot on the live page: RealtimeChart]

### frappe.ui.RealtimeChart.start_updating

`frappe.ui.RealtimeChart.start_updating()`

Start listening to the specified socket event and update the RealtimeChart accordingly.

```js
frappe.ui.RealtimeChart.start_updating();
```

[Screenshot on the live page: RealtimeChart]
_frappe.ui.RealtimeChart.start_updating_

### frappe.ui.RealtimeChart.stop_updating

`frappe.ui.RealtimeChart.stop_updating()`

Stop listening to the socket event that RealtimeChart was initialized with.

```js
frappe.ui.RealtimeChart.stop_updating();
```

### frappe.ui.RealtimeChart.update_chart

`frappe.ui.update_chart(label, data)`

Manually updates RealtimeChart by appending the label and associated data to the end of the chart.

```js
frappe.ui.update_chart(2, [30]);
```

<!-- page: framework/framework__user__en__api__controls.md -->
---
title: "Controls\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/controls"
updated: "2026-02-17"
---


## frappe.ui.form.make_control
`frappe.ui.form.make_control({ parent, df })`

Makes a frappe control based on `df` properties and appends into `parent`
container.

```js
frappe.ui.form.make_control({
 parent: $wrapper.find('.my-control'),
 df: {
 label: 'Due Date',
 fieldname: 'due_date',
 fieldtype: 'Date'
 },
 render_input: true
})
```

Here are the `df` properties for most of frappe control types.

```js
// Attach
{
 label: 'Attachment',
 fieldname: 'attachment',
 fieldtype: 'Attach'
}

// Attach Image
{
 label: 'User Image',
 fieldname: 'user_image',
 fieldtype: 'Attach Image'
}

// Autocomplete
{
 label: 'Select User',
 label: 'user',
 fieldtype: 'Autocomplete',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com'
 ]
}

// Barcode
{
 label: 'Item Barcode',
 fieldname: 'item_barcode',
 fieldtype: 'Barcode'
}

// Check
{
 label: 'Enable feature',
 fieldname: 'enable_feature',
 fieldtype: 'Check'
}

// Code
{
 label: 'JS Script',
 fieldname: 'script',
 fieldtype: 'Code',
 // for syntax highlighting
 options: 'Javascript' // JS, HTML, CSS, Markdown, SCSS, JSON,
 // wrap code
 wrap: true,
 // changing `max_lines` will set the max-height of the editor
 max_lines: 10,
 // changing `min_lines` will set the min-height of the editor
 min_lines: 5
}

// Color
{
 label: 'Your favorite color',
 fieldname: 'user_color',
 fieldtype: 'Color'
}

// Currency
{
 label: 'Amount',
 fieldname: 'amount',
 fieldtype: 'Currency',
 options: 'INR' // or name of field which holds currency
}

// Data
{
 label: 'First Name',
 fieldname: 'first_name',
 fieldtype: 'Data',
 options: 'Email' // 'Name', 'Phone', 'URL', 'Barcode'
}

// Date Range
{
 label: 'Select Date Range',
 fieldname: 'date_range',
 fieldtype: 'Date Range'
}

// Date
{
 label: 'Birth Date',
 fieldname: 'birth_date',
 fieldtype: 'Date'
}

// Datetime
{
 label: 'Submission Date and Time',
 fieldname: 'submission',
 fieldtype: 'Datetime'
}

// Dynamic Link
{
 label: 'Party',
 fieldname: 'party',
 fieldtype: 'Dynamic Link',
 options: 'party_type' // fieldname which holds the Link type
}

// Float
{
 label: 'Threshold',
 fieldname: 'threshold',
 fieldtype: 'Float'
}

// Geolocation
{
 label: 'Meeting Place',
 fieldname: 'meeting_place',
 fieldtype: 'Geolocation'
}

// HTML Editor
{
 label: 'Custom HTML',
 fieldname: 'custom_html',
 fieldtype: 'HTML Editor'
}

// Int
{
 label: 'No of days',
 fieldname: 'no_of_days',
 fieldtype: 'Int'
}

// Link
{
 label: 'Select User',
 fieldname: 'user',
 fieldtype: 'Link',
 options: 'User' // name of doctype
}

// Markdown Editor
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'Markdown Editor'
}

// MultiCheck
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'MultiCheck',
 options: [
 'Option 1',
 'Option 2',
 'Option 3',
 'Option 4',
 ],
 columns: 2 // break into 2 columns
}

// MultiSelect
{
 label: 'Select Users',
 fieldname: 'users',
 fieldtype: 'MultiSelect',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com',
 'shivam@erpnext.com'
 ]
}

// Password
{
 label: 'New Password',
 fieldname: 'password',
 fieldtype: 'Password'
}

// Rating
{
 label: 'Rate your experience',
 fieldname: 'rating',
 fieldtype: 'Rating'
}

// Select
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Select',
 options: [
 'Open',
 'Closed',
 'Cancelled'
 ]
}

// Signature
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Signature'
}

// Text Editor
{
 label: 'Description',
 fieldname: 'description',
 fieldtype: 'Text Editor'
}

// Time
{
 label: 'In Time',
 fieldname: 'in_time',
 fieldtype: 'Time'
}

// Button
{
 label: 'Fetch',
 fieldname: 'fetch',
 fieldtype: 'Button',
 btn_size: 'xs' // xs, sm, lg
}

//Icon
{
 label: 'Page Icon',
 fieldname: 'page_icon',
 fieldtype: 'Icon'
}
```

## Adding Custom Formatters

You can add custom formatters for text type objects (Data, Select, Text etc) by adding them to the `docfield` object in `frappe.meta.docfield_map`

Example:

```
frappe.meta.docfield_map['DocField'].fieldtype.formatter = (value) => {
 if (value==='Section Break') return '🔵 Section Break';
 else return value;
}
```

<!-- page: framework/framework__user__en__api__database.md -->
---
title: "Database API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/database"
updated: "2026-02-17"
---

*Version 16* onwards has some [breaking changes](https://github.com/frappe/frappe/wiki/query-builder-migration) in `get_list` and `get_all`

## frappe.db.get_list

`frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length, run)`

- Also aliased to `frappe.get_list`

Returns a list of records from a `doctype` table. ORM Wrapper for a `SELECT` query. Will also apply user permissions for the records for the session user. Only returns the document names if the `fields` keyword argument is not given. By default this method returns a list of `dict`s, but, you can pluck a particular field by giving the `pluck` keyword argument:

```
frappe.db.get_list('Employee')

# output
[{'name': 'HR-EMP-00008'},
 {'name': 'HR-EMP-00006'},
 {'name': 'HR-EMP-00010'},
 {'name': 'HR-EMP-00005'}
]

# with pluck
frappe.db.get_list('Employee', pluck='name')

# output
['HR-EMP-00008',
 'HR-EMP-00006',
 'HR-EMP-00010',
 'HR-EMP-00005'
]
  

```

Combining filters and other arguments:

```
frappe.db.get_list('Task',
    filters={
        'status': 'Open'
    },
    fields=['subject', 'date'],
    order_by='date desc',
    start=10,
    page_length=20,
    as_list=True
)

# output
(('Update Branding and Design', '2019-09-04'),
('Missing Documentation', '2019-09-02'),
('Fundraiser for Foundation', '2019-09-03'))

# Tasks with date after 2019-09-08
frappe.db.get_list('Task', filters={
    'date': ['>', '2019-09-08']
})

# Tasks with date between 2020-04-01 and 2021-03-31 (both inclusive)
frappe.db.get_list('Task', filters=[[
    'date', 'between', ['2020-04-01', '2021-03-31']
]])

# Tasks with subject that contains "test"
frappe.db.get_list('Task', filters={
    'subject': ['like', '%test%']
})

# Count number of tasks grouped by status
frappe.db.get_list('Task',
    fields=['count(name) as count', 'status'],
    group_by='status'
)

# For version 16 +
frappe.db.get_list('Task',
    fields=[{'COUNT': 'name', 'as': 'count'}, 'status'],
    group_by='status'
)

# output
[{'count': 1, 'status': 'Working'},
 {'count': 2, 'status': 'Overdue'},
 {'count': 2, 'status': 'Open'},
 {'count': 1, 'status': 'Filed'},
 {'count': 20, 'status': 'Completed'},
 {'count': 1, 'status': 'Cancelled'}]
  
```

Prior to version 16, setting `run=False` would return the SQL query instead of running it. From version 16 onwards, you'd get a query builder object instead. You can call `.get_sql()` to get the SQL query like earlier, otherwise you can mutate the query as desired before running it (`query.run()`)

## frappe.db.get_all

`frappe.db.get_all(doctype, filters, or_filters, fields, order_by, group_by, start, page_length, run)`

- Also aliased to `frappe.get_all`

Same as `frappe.db.get_list` but will fetch all records without applying permissions.

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)` or `frappe.db.get_value(doctype, filters, fieldname)`

- Also aliased to `frappe.get_value` and `frappe.db.get_values`

Returns a document's field value or a list of values.

```
# single value
subject = frappe.db.get_value('Task', 'TASK00002', 'subject')

# multiple values
subject, description = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'])

# as dict
task_dict = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'], as_dict=1)
task_dict.subject
task_dict.description

# with filters, will return the first record that matches filters
subject, description = frappe.db.get_value('Task', {'status': 'Open'}, ['subject', 'description'])
  

```

## frappe.db.getsinglevalue

`frappe.db.get_single_value(doctype, fieldname)`

Returns a field value from a Single DocType.

```
timezone = frappe.db.get_single_value('System Settings', 'timezone')
  

```

## frappe.db.set_value

`frappe.db.set_value(doctype, name, fieldname, value)`

- Also aliased to `frappe.db.update`

Sets a field's value in the database, does not call the ORM triggers but updates the modified timestamp (unless specified not to).

```
# update a field value
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject')

# update multiple values
frappe.db.set_value('Task', 'TASK00002', {
    'subject': 'New Subject',
    'description': 'New Description'
})

# update without updating the `modified` timestamp
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject', update_modified=False)
  

```

> This method won't call ORM triggers like `validate` and `on_update`. Use this method to update hidden fields or if you know what you are doing.

## frappe.db.exists

`frappe.db.exists(doctype, name)`

Returns true if a document record exists.

Pass doctype and docname:

```
frappe.db.exists("User", "jane@example.org", cache=True)
  

```

Pass a dict of filters including the `"doctype"` key:

```
frappe.db.exists({"doctype": "User", "full_name": "Jane Doe"})
  

```

Pass the doctype and a dict of filters:

```
frappe.db.exists("User", {"full_name": "Jane Doe"})
  

```

## frappe.db.count

`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.

```
# total number of Task records
frappe.db.count('Task')

# total number of Open tasks
frappe.db.count('Task', {'status': 'Open'})
  

```

## frappe.db.delete

`frappe.db.delete(doctype, filters)`

Delete `doctype` records that match `filters`. This runs a DML command, which means it can be rolled back. If no filters specified, all the records of the doctype are deleted.

```
frappe.db.delete("Route History", {
    "modified": ("<=", last_record_to_keep[0].modified),
    "user": user
})

frappe.db.delete("Error Log")
frappe.db.delete("__Test Table")
  

```

You may pass the doctype name or an internal table name. Conventionally, internal tables in Frappe are prefixed with `__`. The API follows this. The above commands run an unconditional `DELETE` query over tables **tabError Log** and **__Test Table**.

## frappe.db.truncate

`frappe.db.truncate(doctype)`

Truncate a table in the database. This runs a DDL command `TRUNCATE TABLE`, a commit is triggered before the statement is executed. This action cannot be rolled back. You may want to use this for clearing out log tables periodically.

```
frappe.db.truncate("Error Log")
frappe.db.truncate("__Test Table")
  

```

The above commands run a `TRUNCATE` query over tables **tabError Log** and **__Test Table**.

## frappe.db.commit

`frappe.db.commit()`

Commits current transaction. Calls SQL `COMMIT`.

> In most cases you don't need to commit manually. Refer Frappe's [Database transaction model](#database-transaction-model) below.

## frappe.db.savepoint

`frappe.db.savepoint(save_point)`

Create a named savepoint to which you can later roll back to.

## frappe.db.rollback

`frappe.db.rollback()`

Rollbacks current transaction. Calls SQL `ROLLBACK`.

> Frappe will automatically run `frappe.db.rollback()` if an exception is thrown during a Web Request of type `POST` or `PUT`. Use this if you have to rollback early in a transaction.

`frappe.db.rollback(save_point="save_point_name")`

Rollback to a specific savepoint instead rolling back full transactions. This rollback won't undo changes done to filesytem and any other rollback watchers.

## frappe.db.sql

`frappe.db.sql(query, values, as_dict)`

Execute an arbitrary SQL query. This may be useful for complex server side reports with join statements, adjusting the database to new features, etc.

Example:

```
values = {'company': 'Frappe Technologies Inc'}
data = frappe.db.sql("""
 SELECT
 acc.account_number
 gl.debit
 gl.credit
 FROM `tabGL Entry` gl
 LEFT JOIN `tabAccount` acc
 ON gl.account = acc.name
 WHERE gl.company = %(company)s
""", values=values, as_dict=0)

```

> Avoid using this method as it will bypass validations and integrity checks. It's always better to use [frappe.get_doc](https://frappeframework.com/docs/v14/user/en/api/document#frappeget_doc), [frappe.db.get_list](#frappedbget_list), etc., if possible.

## frappe.db.multisql

`frappe.db.multisql({'mariadb': mariadb_query, 'postgres': postgres_query})`

Execute the suitable SQL statement for any supported database engine.

## frappe.db.rename_table

`frappe.db.rename_table(old_name, new_name)`

Executes a query to change table name. Specify the DocType or internal table's name directly to rename the table.

Example:

```
frappe.db.rename_table("__internal_cache", "__temporary_cache")
frappe.db.rename_table("todo", "ToDo")
  

```

The second example should be used only if you understand the ramifications of it.

> Don't use this to rename DocType tables. Use `frappe.rename_doc` for that instead

## frappe.db.describe

`frappe.db.describe(doctype)`

Returns a tuple of the table description for given DocType.

## frappe.db.changecolumntype

`frappe.db.change_column_type(doctype, column, new_type)`

Changes the type of column for specified DocType.

## frappe.db.add_index

`frappe.db.add_index(doctype, fields, index_name)`

Creates indexes for doctypes for the specified fields.

> Note: if you want an index on a TEXT or a BLOB field, you must specify a fixed length to do that.

Example:

```
frappe.db.add_index("Notes", ["id(10)", "content(500)"], index_name)
```

## frappe.db.add_unique

`frappe.db.add_unique(doctype, fields, constraint_name=None)`

Creates unique constraint for doctypes for the specified fields.

Example:

```
frappe.db.add_unique("DoctypeName",["field1","field2"])
```

## frappe.db.bulk_update

`frappe.db.bulk_update(doctype, doc_updates, *, chunk_size=100, modified=None, modified_by=None, update_modified=True, debug=False)`

Bulk update multiple documents in batches using a single SQL UPDATE with CASE expressions.

Example:

```
frappe.db.bulk_update(
    "Task",
    {
        "TASK-0001": {"status": "Closed", "description": "Completed by QA"},
        "TASK-0002": {"status": "Open", "description": "Pending assignment"},
    },
    chunk_size=200,
    modified_by="admin@example.com",
    update_modified=True,
    debug=True,
)
```

doc_updates format:

```
{
    "DOC-0001": {"field1": "value1", "field2": "value2"},
    "DOC-0002": {"field1": "valueA", "field2": "valueB"},
}
```

**Notes:**

- Direct DB update; Document events/validations are not triggered.
- Unspecified fields remain unchanged.

## Database transaction hooks

> Note: This API is introduced in v15.

Frappe provides hooks for running callbacks before/after transaction commands like commit/rollback are issued. These hooks are useful for:

- Rolling back changes that are done outside of the database if the transaction is rolled back
- Flushing changes outside of the database only if the transaction is committed.

These hooks are :

- `frappe.db.before_commit.add(func: Callable)`
- `frappe.db.after_commit.add(func: Callable)`
- `frappe.db.before_rollback.add(func: Callable)`
- `frappe.db.after_rollback.add(func: Callable)`

Example usage:

```
def create_file(self):
    self.write_file()
    # This ensures rollback if DB transaction is rolledback
    frappe.db.after_rollback.add(self.rollback_file)

def rollback_file(self):
    self.delete_file()
```

## Database transaction model

Frappe's database abstractions implement a sane transaction model by default. So in most cases, you won't have to deal with SQL transactions manually. A broad description of this model is described below:

### Web requests

- While performing `POST` or `PUT`, if any writes were made to the database, they are committed at end of the successful request.
- AJAX calls made using `frappe.call` are `POST` by default unless changed.
- `GET` requests do not cause an implicit commit.
- Any **uncaught** exception during handling of request will rollback the transaction.

### Background/scheduled Jobs

- Calling a function as background or scheduled job will commit the transaction after successful completion.
- Any **uncaught** exception will cause rollback of the transaction.

### Patches

- Successful completion of the patch's `execute` function will commit the transaction automatically.
- Any **uncaught** exception will cause rollback of the transaction.

### Unit tests

- Transaction is committed after running one test module. Test module means any python test file like `test_core.py`.
- Transaction is also committed after finishing all tests.
- Any **uncaught** exception will exit the test runner, hence won't commit.

> Note: If you're catching exceptions anywhere, then database abstraction does not know that something has gone wrong hence you're responsible for the correct rollback of the transaction.

<!-- page: framework/framework__user__en__api__dialog.md -->
---
title: "Dialog API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/dialog"
updated: "2026-02-17"
---

Frappe provides a group of standard, interactive and flexible dialogs that are easy to configure and use. There's also an API for [Python](/framework/v14/user/en/api/py-dialog).

### frappe.ui.Dialog

`new frappe.ui.Dialog({ title, fields, primary_action })`

Creates a new Dialog instance.

```
let d = new frappe.ui.Dialog({
    title: 'Enter details',
    fields: [
        {
            label: 'First Name',
            fieldname: 'first_name',
            fieldtype: 'Data'
        },
        {
            label: 'Last Name',
            fieldname: 'last_name',
            fieldtype: 'Data'
        },
        {
            label: 'Age',
            fieldname: 'age',
            fieldtype: 'Int'
        }
    ],
    size: 'small', // small, large, extra-large 
    primary_action_label: 'Submit',
    primary_action(values) {
        console.log(values);
        d.hide();
    }
});

d.show();
  

```

[Screenshot on the live page: Dialog]

 *frappe.ui.Dialog*

### frappe.msgprint

`frappe.msgprint(message)` or `frappe.msgprint({ title, message, indicator })`

Show `message` in a modal.

```
// only message
frappe.msgprint(__('Document updated successfully'));

// with options
frappe.msgprint({
    title: __('Notification'),
    indicator: 'green',
    message: __('Document updated successfully')
});
  

```

[Screenshot on the live page: Msgprint]

 *frappe.msgprint*

You can also bind a primary action to this dialog by passing `action`(as a method) within `primary_action`. Alternatively, `primary_action` can contain `server_action` **or** `client_action`.

The `server_action` and `client_action` are dotted paths to the respective methods which will execute on clicking the primary button.

```
// with primary action
 frappe.msgprint({
    title: __('Notification'),
    message: __('Are you sure you want to proceed?'),
    primary_action:{
        action(values) {
            console.log(values);
        }
    }
});

// with server and client action
frappe.msgprint({
    title: __('Notification'),
    message: __('Are you sure you want to proceed?'),
    primary_action: {
    'label': 'Proceed',
    // either one of the actions can be passed
    'server_action': 'dotted.path.to.method',
    'client_action': 'dotted_path.to_method',
    'args': args
    }
});
  

```

[Screenshot on the live page: Msgprint with Primary Action]

 *frappe.msgprint with primary action bound*

### frappe.throw

`frappe.throw(error_message)`

Show `error_message` in a modal and `throw` exception.

```
frappe.throw(__('This is an Error Message'))
  

```

[Screenshot on the live page: Throw]

 *frappe.throw*

### frappe.prompt

`frappe.prompt(label)` or `frappe.prompt(df)` or `frappe.prompt(fields)`

Prompt user for a value or list of values.

```
// prompt for single value of type Data
frappe.prompt('First Name', ({ value }) => console.log(value))

// Set title and button label
frappe.prompt('First Name', console.log, 'Enter First Name', 'Submit');

// prompt for single value of any type
frappe.prompt({
    label: 'Birth Date',
    fieldname: 'date',
    fieldtype: 'Date'
}, (values) => {
    console.log(values.date);
})

// prompt for multiple values
frappe.prompt([
    {
        label: 'First Name',
        fieldname: 'first_name',
        fieldtype: 'Data'
    },
    {
        label: 'Last Name',
        fieldname: 'last_name',
        fieldtype: 'Data'
    },
], (values) => {
    console.log(values.first_name, values.last_name);
})
  

```

[Screenshot on the live page: Prompt]

 *frappe.prompt*

### frappe.confirm

`frappe.confirm(message, if_yes, if_no)`

Show a confirmation modal, executes `if_yes` if confirmation is given else executes `if_no`.

```
frappe.confirm('Are you sure you want to proceed?',
    () => {
        // action to perform if Yes is selected
    }, () => {
        // action to perform if No is selected
    })
  

```

[Screenshot on the live page: Prompt]

 *frappe.confirm*

### frappe.warn

`frappe.warn(title, message_html, proceed_action, primary_label, is_minimizable)`

Show a warning modal, executes `proceed_actiion` if confirmation is given. It can be set as `minimizable` which allows the dialog to be minimized.

```
frappe.warn('Are you sure you want to proceed?',
    'There are unsaved changes on this page',
    () => {
        // action to perform if Continue is selected
    },
    'Continue',
    true // Sets dialog as minimizable
)
  

```

[Screenshot on the live page: Prompt]

 *frappe.confirm*

### frappe.showalert

`frappe.show_alert(message, seconds)` or `frappe.show_alert({message, indicator}, seconds)`

Alert Dialog is used for showing non-obstructive messages.

Its parameters include `message`, which can contain the indicator color as well, and its display duration. The default is **7 seconds**.

```
frappe.show_alert('Hi, you have a new message', 5);

//show_alert with indicator
frappe.show_alert({
    message:__('Hi, you have a new message'),
    indicator:'green'
}, 5);
  

```

[Screenshot on the live page: Show Alert]

 *frappe.showalert*

### frappe.showprogress

`frappe.show_progress(title, count, total, description)`

Displays a progress bar with `count` (as current progress) and `total` (as maximum progress value).

```
frappe.show_progress('Loading..', 70, 100, 'Please wait');
  

```

[Screenshot on the live page: Show Progress]

 *frappe.showprogress*

### frappe.newdoc

`frappe.new_doc(doctype, route_options, init_callback)`

Opens a new form of the specified DocType that allows to edit and save it. If "Quick Entry" is enabled for the DocType (that allows to enter the most important fields) the "Quick Entry" pop-up window will be shown. Otherwise you will be redirected to the usual document entry form.

For example, let's create a new **Task**:

```
frappe.new_doc("Task");
  

```

Often when you are creating a new document in the user interface you want to initialize some of its fields based on the user interaction that triggered the creation. The other two arguments can be used for such initialization.

Specifically, the `route_options` argument is a quick and convenient way to set any field of type Link, Select, Data, or Dynamic Link in the new document. Its value should be an object whose keys are the desired field names and whose values are the initial values.

```
frappe.new_doc("Task", {subject: "New Task"});
  

```

If you need to do any other initialization of the new document that is not possible with `route_options`, `init_callback` gives you full control. It should be a function of one argument. If the doctype is initialized with a "Quick Entry" form, the callback is called with the "Quick Entry" dialog object just before control is released back to the user. Otherwise, the callback is called with the new document just before the user is allowed to edit it in the standard form.

```
frappe.new_doc("Task", {subject: "New Task"},
                doc => {doc.description = "Do what's necessary";});
  

```

Note that `subject` is a field of type "Data", so we are able to take advantage of the `route_options` argument to set it. `description` is a field of type "Text Editor", so if we want to initialize it, that must be done in the callback.

For a slightly more complex example, here's a call that creates a new **Journal Entry** of type "Bank Entry" and populates one side of the transaction:

```
frappe.new_doc("Journal Entry", {"voucher_type": "Bank Entry"}, doc => {
    doc.posting_date = frappe.datetime.get_today();
    let row = frappe.model.add_child(doc, "accounts");
    row.account = 'Bank - A';
    row.account_currency = 'USD';
    row.debit_in_account_currency = 100.0;
    row.credit_in_account_currency = 0.0;
});
  

```

### frappe.ui.form.MultiSelectDialog

`new frappe.ui.form.MultiSelectDialog({ doctype, target, setters, date_field, get_query, action })`

A MultiSelectDialog consists of filter fields followed by a multiple selection list. The primary button will perform the passed `action` on the selected options.

By default, the **Search Term** field and **Date Range** field will compose the filter fields.

The argument list includes:

- `doctype`: The source to fetch and display selection entries from.
- `target`: The target where the modal is to be displayed.
- `setters`: These will compose the filter fields and values to populate them with. These also translate to custom columns for the selection list.
- `read_only_setters`: If you want to make setters (filters) read only so that users can't change the value of the filters then add those fields in the "read_only_setters".
- `add_filters_group`: A boolean value to add/remove the filter group in the dialog below `setters`. The filter group is same as the list view filters.
- `date_field`: It is necessary to pass the `date_field` of the DocType in consideration.
- `get_query`: A function that returns `query` and `filters` to query the selection list. A custom server side method can be passed via `query`, and `filters` will be passed to that method.
- `action`: Contains the primary action to be performed on the selected options. It takes `selections` as a parameter, which comprises of the selected options.
- `columns`: An array of fields returned by custom query which will become columns in result datatable. Only works with the custom query (`get_query` argument returning a `query`).

Let us assume we want to fetch Material Requests into our dialog. We can then go on to invoke the MultiSelectDialog in the following manner:

```
new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: 'Pending'
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    get_query() {
        return {
            filters: { docstatus: ['!=', 2] }
        }
    },
    action(selections) {
        console.log(selections);
    }
});

// MultiSelectDialog with custom query method
let query_args = {
    query:"dotted.path.to.method",
    filters: { docstatus: ["!=", 2], supplier: "John Doe" }
}

new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: 'Pending'
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    columns: ["name", "transaction_date", "status"],
    get_query() {
        return query_args;
    },
    action(selections) {
        console.log(selections);
    }
});
  

```

[Screenshot on the live page: MultiSelectDialog]

 *frappe.ui.form.MultiSelectDialog*

Here all the Material Requests that fulfill the filter criteria will be fetched into the selection area. The setter `company` is added to the filter fields along with its passed value. The `date_field` will be used to fetch and query dates from the DocType mentioned.

The **Make Material Request** (or `Make {DocType}`) secondary action button will redirect you to a new form in order to make a new entry into the DocType passed.

Now, if we want to only select particular item from a Material Request, then we can use optional `child_selection_mode` to enable child selection

```

// MultiSelectDialog for individual child selection
new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: null
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    allow_child_item_selection: 1,
    child_fieldname: "items", // child table fieldname, whose records will be shown &amp; can be filtered
    child_columns: ["item_code", "qty"], // child item columns to be displayed
    get_query() {
        return {
            filters: { docstatus: ['!=', 2] }
        }
    },
    action(selections, args) {
        console.log(args.filtered_children); // list of selected item names
    }
});
  

```

[Screenshot on the live page: MultiSelectDialog]

 *frappe.ui.form.MultiSelectDialog*

Here you will see a checkbox **Select Individual Items** to toggle between child item selection & parent selection. Once you toggle it, all the individual Material Requests Items are listed from the all the queried Material Request, you can now filter these items for selection.

To access the selected children, you can use `args.filtered_children` list which contains selected child item names.

### Table / Grid in a Dialog

A table can be added to a dialog, just like any other field as follows:

```
const dialog = new frappe.ui.Dialog({
  title: __("Create Logs"),
  fields: [
      {
          fieldname: "logs",
          fieldtype: "Table",
          label: __("Logs"),
          in_place_edit: true,
          reqd: 1,
          fields: [
              {
                  fieldname: "log_type",
                  label: __("Log Type"),
                  fieldtype: "Select",
                  options: "
IN
OUT",
                  in_list_view: 1,
                  reqd: 1,
              },
              {
                  fieldname: "time",
                  label: __("Time"),
                  fieldtype: "Time",
                  in_list_view: 1,
                  reqd: 1,
              }
          ],
          on_add_row: (idx) => {
            // idx = visible idx of the row starting from 1
            // eg. set `log_type` as alternating IN/OUT in the table on row addition
              let data_id = idx - 1;
              let logs = dialog.fields_dict.logs;
              let log_type = (data_id % 2) == 0 ? "IN" : "OUT";

              logs.df.data[data_id].log_type = log_type;
              logs.grid.refresh();
          },
      },
  ],
  primary_action: (values) => { ... },
  primary_action_label: __("Create"),
});
```

`on_add_row`: An event that gets triggered on adding a row to the table. You can perform an action like data manipulation or some other sort of calculation by adding your functionality to this event hook.

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
