<!-- Frappe documentation: framework, part 7 of 24. Index: docs/INDEX.md -->

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
