<!-- Frappe documentation: framework, part 8 of 24. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Child DocType]

To link a Child Doctype to its parent, add another row in Parent Doctype with field
type **Table** and options as **Child Table**.

[Screenshot on the live page: Child Table]

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

[Screenshot on the live page: Customize Form]

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

[Screenshot on the live page: Field Types Dropdown Menu]



#### Data

The data field will be a **simple text field**. It allows you to enter a value of up to 140 characters, making this the most generic field type.

You can enable validations for the following types of data:

1. Name
2. Email
3. Phone
4. URL

by setting the options to "Name", "Email", "Phone" or "URL" respectively.

[Screenshot on the live page: Data field types]



Set the options to "IBAN" to enable formatting in blocks of 4 characters.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](https://erpnext.com/docs/user/manual/en/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](https://docs.frappe.io/erpnext/user/manual/en/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here. You can set the `Default` value to 1 and it will be checked by default.

[Screenshot on the live page: Check Field Preview]



[Screenshot on the live page: Check Field Edit]



#### Select

Using the field type "Select", you can create a drop-down field. You can specify all selectable values in the *Options* field, each value separated by a new line.

One of the selectable values can be copied into the *Default* field. This value will then be selected by default in a new form.

If you enable the *Sort Options* checkbox, values will be displayed in alphabetical order (in the user's language).

The following screenshot shows how a "Select" field can be defined in the **DocType** or via **Customize Form**:

[Screenshot on the live page: define_select_field]



And this is how it will be rendered in a new form:

[Screenshot on the live page: use_select_field]



#### Table

With a "Table" field, you can render another DocType as a child table within your form.

First, you'll have to choose or define a DocType that has the Checkbox *Is Child Table* enabled. Then you can add a field of type "Table" and paste the name of your child table DocType into the *Options* field.

For example, ERPNext defines a child DocType called "Purchase Receipt Item" with *Is Child Table* enabled:

[Screenshot on the live page: define_child_table_doctype]



Another DocType called "Purchase Receipt" has a field of type "Table", with *Options* set to above child doctype "Purchase Receipt Item":

[Screenshot on the live page: define_child_table_field]



Finally, the child table will be rendered in the Purchase Receipt form:

[Screenshot on the live page: child_table_in_form]



#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

[Screenshot on the live page: Field Types]



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

[Screenshot on the live page: Field Types]



#### Date

This field will enable you to enter the Date in this field.

[Screenshot on the live page: Field Types]



#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Once you do that, the Barcode would automatically get generated against the number.

[Screenshot on the live page: barcode]



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

[Screenshot on the live page: Field Types]



#### Color

This will let the user input a color via a rendered color picker or directly input a hexadecimal color.

[Screenshot on the live page: Field Types]



#### Column Break

This is a `'meta'` fieldtype that does not store any input data but can be used to indicate a column break in the document view or form.

For example,

[Screenshot on the live page: Field Types]



will result into:

[Screenshot on the live page: Field Types]



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

[Screenshot on the live page: Field Types]



will result into:

[Screenshot on the live page: Field Types]



#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

[Screenshot on the live page: Field Types]



will result into:

[Screenshot on the live page: Field Types]



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

[Screenshot on the live page: Field Types]



when preview is clicked:

[Screenshot on the live page: Field Types]



#### Password

The password field will have decoded value in it. This type of field can be used to store sensitive data like passwords, pass phrases, secret keys etc.

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

#### Rating

This field can be used to display an interactive star rating input. The default star count shown is 5, however, this can easily be changed by entering a number ranging from 3 - 10 in the options field for that particular rating field.

[Screenshot on the live page: Check Field Edit]



You can also provide half ratings e.g 3.5 out of 5.

[Screenshot on the live page: Half Rating]



#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

#### Section Break

Section Break is used to divide the form into multiple sections. Any fields that follow (and before any other `Section Break`) a `Section Break` field will be part of this new section.

[Screenshot on the live page: Field Types]



### Tab Break

Tab Break is used to divide the form into multiple tabs. Any field that follow till the next `Tab Break` will be the part of this new tab.

[Screenshot on the live page: Tabs]



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

[Screenshot on the live page]

 

**Set the title field**

Enter the name of a custom field in 'Title Field'

[Screenshot on the live page]

 

**Show Title in Link Fields**

You can enable **Show Title in Link Fields** to display **Title** instead of **Name** in the **Link Fields** in another doctype.

[Screenshot on the live page]

 

So if a custom field of 'link' type is added in another doctype (or through customize form), then the title of the linked document will be displayed in the field instead of name.

[Screenshot on the live page]

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

[Screenshot on the live page]
*Autoincrement*

### 3. By fieldname

The document name is fetched directly from the value of a specific field.

> **Note:** The value in the selected field must always be unique.

[Screenshot on the live page]
*By Fieldname*

### 4. By "Naming Series" field

The naming pattern is derived from a specific field in the document (usually `naming_series`).

For example, if you have a field `naming_series` in your document and its value is set to `PRE.#####`, that pattern will be used to generate the name (e.g., `PRE00001`). This value can change per document, allowing different documents within the same DocType to follow different patterns.

> **Requirement:** This works only if you have a field called `naming_series` in your DocType.

[Screenshot on the live page]
*By "Naming Series"*

### 5. Expression

You can provide a standard naming pattern which will be incremented automatically.

For example, if you set the pattern as `PRE-.#####`:

- The first document created will be named `PRE-00001`
- The second will be `PRE-00002`
- And so on...  
  [Screenshot on the live page]
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

[Screenshot on the live page]
*Random*

### 8. UUID

Uses a randomly generated Universally Unique Identifier (UUID v4) as the document name.

**Example:** `550e8400-e29b-41d4-a716-446655440000`  

[Screenshot on the live page]
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

[Screenshot on the live page]

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

[Screenshot on the live page: Single DocType]

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

[Screenshot on the live page: Virtual DocType]  


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

[Screenshot on the live page: Virtual DocType Form]  


All the /api/resource methods defined by the framework are compatible with Virtual DocTypes.


> Added in Version 13
> 
> 
