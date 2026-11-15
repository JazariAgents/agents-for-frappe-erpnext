<!-- Frappe documentation: framework, part 2 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__doctypes__doctype-layout.md -->
---
title: "DocType Layout"
space: "Framework"
url: "https://docs.frappe.io/framework/doctypes/doctype-layout"
updated: "2026-06-03"
---

# DocType Layout



DocType Layout lets you create multiple form views for the same DocType — each with different field labels, visibility rules, and defaults — **without modifying the DocType itself**. Layouts activate automatically based on document state, so the right view appears with no manual action.

**Common use cases**

- A simplified data-entry view that hides advanced fields
- A read-heavy review view that relabels fields for clarity
- Auto-switching to a "Return" layout when `doc.is_return == 1`
- State- or context-specific layouts driven by conditions or workspace links

## Creating a Layout



Go to the **DocType Layout** list and click **New**.


| Field                      | Description                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Title**                  | Display name shown in the layout indicator and breadcrumb (e.g. *Compact View*).                                          |
| **Document Type**          | The DocType this layout applies to. Set once and cannot change.                                                           |
| **Condition**              | Optional JS expression. When truthy, this layout activates automatically on form refresh.                                 |
| **Based On**               | Inherit field configuration from another layout of the same DocType.                                                      |
| **Is Child Table**         | Mark this layout as a child-table layout. When checked, it appears in the Child Layout selector of other DocType Layouts. |
| **Default Print Format**   | Pre-selects this print format when the layout is active.                                                                  |
| **Default Email Template** | Pre-selects this email template when the layout is active.                                                                |


After selecting a **Document Type**, click **Sync Fields** to pull in all fields from the DocType. A visual form builder opens in the **Parent Layout** tab where you can reorder and configure fields.

## Overriding Field Properties



In the form builder, select any field to override its properties. The following properties can be set **per layout** without affecting the base DocType:


| Property               | Effect                                        |
| ---------------------- | --------------------------------------------- |
| `label`                | Rename the field for this layout              |
| `hidden`               | Hide the field                                |
| `reqd`                 | Make the field mandatory                      |
| `read_only`            | Make the field read-only                      |
| `bold`                 | Emphasize the label                           |
| `allow_in_quick_entry` | Include the field in the Quick Entry dialog   |
| `in_list_view`         | Show the field as a column in the List View   |
| `in_standard_filter`   | Include the field in the Standard Filters bar |
| `default`              | Set a default value for new documents         |
| `description`          | Override the help text                        |
| `depends_on`           | Conditional visibility expression             |
| `mandatory_depends_on` | Conditional required expression               |
| `read_only_depends_on` | Conditional read-only expression              |


Properties not set in the layout fall back to the base DocType definition.

## Automatic Layout Switching



Layout selection is **entirely condition-driven** — there is no manual switcher. Set a **Condition** to make a layout activate automatically when the expression evaluates to truthy after a form refresh:

```
// Activates for return transactions
doc.is_return == 1

// Activates for high-value orders
doc.grand_total > 100000

// Activates for a specific status
doc.status === "Closed"
```

When a condition matches, the layout is applied and the URL is updated with `?layout=<name>`. The first matching layout wins; layouts are evaluated in the order they appear in the list. A layout indicator badge appears next to the document title whenever a non-default layout is active.

## Breadcrumb Navigation



When a layout is active, the breadcrumb bar reflects it:

- On the **form view**, the layout title appears as a clickable crumb between the DocType and the document name. Clicking it opens the list **filtered by the layout's condition** (parsed from `doc.field OP value` expressions).
- On that **filtered list**, the layout title appears as a non-clickable crumb so the active context stays visible.
- Clicking the **DocType crumb** while a layout is active clears all filters and removes the layout crumb, returning to the unfiltered list.

## Child Table Layouts



A layout can specify different layouts for its child tables. In the **Child Layouts** tab, add a row for each child table you want to customize:


| Field               | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| **Table Fieldname** | The fieldname of the child table in the parent DocType                 |
| **Child Layout**    | A DocType Layout whose Document Type matches the child table's DocType |


When the parent layout is active, each child table grid automatically renders using its assigned child layout — applying the same field-level overrides as a parent layout would.

**Important.** The child layout's **Document Type** must match the child table's DocType (e.g. `Sales Invoice Item`), not the parent DocType. Create a separate layout for the child table first, then reference it here.

The same field properties available on a parent layout — `label`, `hidden`, `reqd`, `read_only`, `depends_on`, column order, and so on — apply inside the grid when the child layout is active.

**Example.** A *Finance View* parent layout maps the items table to a *Compact Items* child layout that hides `description`, `uom`, and other detail columns, leaving only `item_code`, `qty`, and `amount` visible. Switching to the parent layout automatically compacts the grid — no extra action required from the user.

## Layout Inheritance



Use **Based On** to inherit the field configuration of another layout for the same DocType. The child layout starts with the parent's field order and overrides, and can further customize individual fields or add new ones.

This is useful for creating a family of related layouts: define a *Base Layout* with common field order, then create specialized layouts (e.g. *Sales View*, *Finance View*) that inherit and tweak it.

## Keeping Fields in Sync



The **Sync Fields** button compares the layout's field list against the current DocType definition and reports:

- **Added** — fields present in the DocType but missing from the layout (added to the end)
- **Removed** — fields in the layout that no longer exist in the DocType (removed)

Run this after modifying the underlying DocType to keep the layout consistent.

## Workspace Integration



Any DocType link in the sidebar workspace can be tied to a specific layout. Open the workspace in edit mode, select a DocType link, and set the **DocType Layout** field to the layout you want. Clicking that link opens the list pre-scoped to that layout (the URL carries `?layout=<name>`), and new documents created from the list open under that layout.

## For Developers: Standard Layouts



Layouts can be shipped as part of an app by setting **Is Standard** and selecting a **Module**. In developer mode, saving a standard layout automatically exports it as a JSON file to:

{app}/{module}/doctype/{doctype}/doctype_layout/{layout_name}.json

This file is included in migrations and deployed automatically via `bench migrate`. Standard layouts are **read-only** on production instances (outside developer mode).

<!-- page: framework/framework__document-queue.md -->
---
title: "Document Queue"
space: "Framework"
url: "https://docs.frappe.io/framework/document-queue"
updated: "2026-07-02"
---

Document Queue is a framework-level document intake workflow for files that need to be reviewed before creating a Frappe document. It stores one uploaded source file, extracts text from it, and lets the user open a target DocType with the source preview beside the native form.

Document Queue is generic. It does not map fields by itself and does not contain ERPNext-specific logic. Apps such as ERPNext can build document-specific mapping, validation, or automation on top of completed Document Queue records.

## When To Use It

Use Document Queue when users receive documents first and decide or create the target record afterwards.

Examples:

- Uploading a vendor invoice PDF before creating a Purchase Invoice in another app.
- Uploading an expense receipt before creating an Expense Claim.
- Uploading a signed form, identity document, or application PDF before creating a custom DocType record.
- Collecting files from an email inbox or bulk upload flow for later review.

Document Queue is useful when the framework should handle file intake, extraction, and review, while the app or user decides what the extracted content means.

## How It Works

A Document Queue record represents one source file. The record stores extraction status, extracted text, raw extraction output, error details, and the target document created during review.

The usual flow is:

1. A user uploads a PDF or image into Document Queue.
2. The user clicks **Extract**, or the file is extracted as part of an upload-first flow.
3. Frappe extracts readable text and stores it on the queue record.
4. The record becomes **Ready for Review**.
5. The user clicks **Start Review** and chooses a target DocType if one is not already set.
6. Frappe opens a new target document with a left-side review panel.
7. The user manually enters values into the native form using the preview and extracted text.
8. When the target document is saved, Frappe links the queue record to that document, marks the queue record **Completed**, and moves the source attachment to the target document.

## Statuses

Document Queue records use these statuses:


| Status           | Meaning                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Draft            | The record exists but extraction has not started.                                          |
| Queued           | Extraction has been queued as a background task.                                           |
| Processing       | Extraction is currently running.                                                           |
| Ready for Review | Extraction completed and the record can be reviewed into a target document.                |
| Completed        | A target document was saved and linked to the queue record.                                |
| Failed           | Extraction failed or the file type is unsupported. Error details are stored on the record. |


Completed records cannot be started for review again. This keeps one Document Queue record tied to one completed target document.

## Extraction

Document Queue supports PDF and image extraction.

For PDFs, Frappe uses `pdfplumber` as the primary extractor. The extracted text is stored in **Extracted Text** and the detailed extraction result is stored in **Raw Extraction JSON**.

For each PDF page, the raw JSON can include:

- page number
- page width and height
- plain text
- layout text
- words with coordinates
- tables detected by `pdfplumber`

If the embedded PDF text is not useful, Frappe attempts OCR fallback with Tesseract, when the required system tools are available.

For images, Frappe uses Tesseract OCR when available. OCR words and coordinates are stored in the raw JSON.

Unsupported files are marked **Failed** and the error is stored in **Error Message**. Debug details, such as skipped OCR because `tesseract` is not available, are stored in **Debug Output**.



## Manual Document Queue Flow

To create a queue record manually:

1. Open **Document Queue**.
2. Create a new record.
3. Attach a PDF or image in **Source File**.
4. Save the record.
5. Click **Extract**.

If extraction succeeds, the record moves to **Ready for Review**.

To create a target document from the queue:

1. Open a **Ready for Review** Document Queue record.
2. Click **Start Review**.
3. If **Document Type** is not set, choose a target DocType.
4. Frappe opens a new target document.
5. Use the left review panel while filling the native form on the right.
6. Save the target document.

After save, the Document Queue record is marked **Completed**, linked to the target document, and the source file is attached to the target document.



## Review Panel

The review panel appears on the left side of the target document form.

It has two tabs:

- **Preview**: Shows the uploaded PDF or image.
- **Extraction**: Shows the extracted text.

The right side remains the native Frappe form. Users enter data manually, using the preview and extracted text as reference.

The preview pane can be resized. Frappe remembers the preferred width in the browser.

If the user leaves the new target document without saving, no target document is linked and the Document Queue record remains resumable.



## Upload Document Flow For Target DocTypes

Administrators can enable an upload-first workflow for any non-child DocType.

When enabled, new records for that DocType show an **Upload Document** banner. Users can upload a PDF or image before filling the form. Frappe creates a Document Queue record, extracts the file, and opens the same review experience for the new target document.

To enable it:

1. Open the DocType record.
2. Enable **Upload First Workflow**.
3. Save the DocType.

Only DocTypes with **Upload First Workflow** enabled are shown in the Document Queue target DocType selector.



## Ready For Review Banner

When a DocType has **Upload First Workflow** enabled, its list view can show a thin banner such as:

> 3 Documents ready for review

The banner includes a **View** action that opens Document Queue filtered to records for that target DocType in **Ready for Review** status.



## Permissions

By default:

- **System Manager** can create, read, write, delete, export, print, email, report, and share Document Queue records.
- **Desk User** can create records and can read, export, print, email, report, and share records they own.

Users also need permission to create and save the target DocType used during review.

## Developer API

### Queue Extraction

Use `enqueue_document_extraction` to run extraction as a background task.

```python
from frappe.core.doctype.document_queue.document_queue import enqueue_document_extraction

task = enqueue_document_extraction(document_queue_name)
```

This marks the record **Queued** and creates a Background Task that extracts that one Document Queue record.

### Extract Immediately

Use `extract_document_queue_record` when extraction should run immediately in the current request or test.

```python
from frappe.core.doctype.document_queue.document_queue import extract_document_queue_record

result = extract_document_queue_record(document_queue_name)
```

The result includes:

```python
{
    "extraction_method": "pdfplumber",
    "extracted_text": "...",
    "raw_extraction_json": {
        "file": "invoice.pdf",
        "extraction_method": "pdfplumber",
        "pages": [],
    },
    "debug_output": [],
}
```

### Get Review Context

Use `get_document_review_context` to fetch the data needed by a review UI.

```python
from frappe.core.doctype.document_queue.document_queue import get_document_review_context

context = get_document_review_context(document_queue_name)
```

Example response:

```python
{
    "queue_name": "abc123",
    "status": "Ready for Review",
    "document_type": "Address",
    "created_document": None,
    "source_file": "/private/files/source.pdf",
    "source_file_url": "/private/files/source.pdf?fid=...",
    "extracted_text": "Extracted text...",
    "raw_extraction_json": {},
    "debug_output": "",
}
```

### Link A Queue Record To A Target Document

Use `link_to_document` after the target document is saved.

```python
from frappe.core.doctype.document_queue.document_queue import link_to_document

link_to_document(
    document_queue=document_queue_name,
    document_type="Address",
    document_name=address_name,
)
```

This marks the Document Queue record **Completed**, stores the target document link, and attaches the source file to the target document.

### Count Records Ready For Review

Use `get_ready_for_review_count` to show a badge or banner for enabled target DocTypes.

```python
from frappe.core.doctype.document_queue.document_queue import get_ready_for_review_count

count = get_ready_for_review_count("Address")
```

The count is returned only for DocTypes that have **Upload First Workflow** enabled.

## Building On Document Queue

Document Queue intentionally stops at extraction and review. It does not infer field mappings or create accounting, buying, selling, HR, or domain-specific documents by itself.

Downstream apps can build on top of it by:

- consuming **Completed** Document Queue records
- reading `extracted_text` for simple search or manual copy flows
- reading `raw_extraction_json` for word coordinates, page data, and tables
- adding app-specific field suggestions
- adding app-specific validation before or after the target document is saved
- adding email or bulk-upload intake that creates queue records

For example, an ERP app can filter completed queue records where `document_type` is `Purchase Invoice`, read the raw extraction JSON, and apply invoice-specific mapping in that app. The mapping logic stays outside Frappe Framework.

## Limitations

- Document Queue does not perform AI or LLM-based field extraction.
- Document Queue does not map extracted text into target DocType fields.
- CSV and spreadsheet extraction are not supported by the built-in extractor.
- OCR requires system tools such as `tesseract`; PDF OCR fallback also requires `pdftoppm`.
- Extraction quality depends on the source document. Digital PDFs usually extract better than scanned or low-resolution images.

<!-- page: framework/framework__get_query.md -->
---
title: "frappe.qb.get_query"
space: "Framework"
url: "https://docs.frappe.io/framework/get_query"
updated: "2026-02-17"
---

The `frappe.qb.get_query` function provides a modern, safe, and expressive way to build database queries in Frappe. It leverages the power of the [Pypika](https://pypika.readthedocs.io/en/latest/) library while integrating seamlessly with Frappe's DocType metadata, permissions, and conventions. This guide will walk you through using `frappe.qb.get_query` from basic usage to more advanced scenarios.

## Introduction

While `frappe.db.get_list` and `frappe.db.get_all` have served Frappe well for many years and are capable of handling complex queries, their underlying code has grown complex over time, making them harder to maintain and extend. `frappe.qb.get_query` represents a modern approach to achieve similar results, built with better extensibility and maintainability in mind.

## Getting Started

### Basic Query Structure

To get started, you need to understand the basic structure of a query:

```python
# Get a query builder instance for the 'User' DocType
query = frappe.qb.get_query("User")

# Execute the query and fetch results
users = query.run(as_dict=True)
```

By default, if no `fields` are specified, it selects **only the `name` field**.

### Simple Example

```python
# Get all user names and emails
query = frappe.qb.get_query("User", fields=["name", "email"])
users = query.run(as_dict=True)
# users will be like: [{'name': 'Administrator', 'email': 'admin@example.com'}, ...]
```

## Field Selection

### Basic Field Selection

Use the `fields` argument to specify which columns you want.

```python
# Select specific fields
query = frappe.qb.get_query("User", fields=["name", "email"])

# You can also pass fields as a comma-separated string
query = frappe.qb.get_query("User", fields="name, email")

# Or select all fields using '*'
query = frappe.qb.get_query("User", fields="*")
```

### Using Aliases

Use `as` within the field string to give fields aliases in the output.

```python
query = frappe.qb.get_query(
    "User",
    fields=["name as user_name", "email as user_email"]
)
users = query.run(as_dict=True)
# users will be like: [{'user_name': 'Administrator', 'user_email': 'admin@example.com'}, ...]
```

### Linked Document Fields

If you have a Link field, you can fetch fields from the linked document using dot notation: `link_fieldname.target_fieldname`. The query builder automatically adds the necessary `LEFT JOIN`.

```python
# Get Sales Order customer name (assuming 'customer' is a Link field to Customer DocType)
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer.customer_name as customer_name"],
    filters={"name": "SO-00001"}
)
so_data = query.run(as_dict=True)
# so_data might be: [{'name': 'SO-00001', 'customer_name': 'Test Customer'}]
```

### Child Table Fields

You can access fields within a Child Table using dot notation: `child_table_fieldname.child_doc_fieldname`.

```python
# Get item code from Sales Order Item (assuming 'items' is the child table fieldname)
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "items.item_code"],
    filters={"name": "SO-00001"}
)
# This will likely return multiple rows if SO-00001 has multiple items
so_items = query.run(as_dict=True)
# so_items might be: [{'name': 'SO-00001', 'item_code': 'ItemA'}, {'name': 'SO-00001', 'item_code': 'ItemB'}]
```

**Important:** When selecting fields from child tables this way, the query performs a `LEFT JOIN`, potentially resulting in multiple rows for each parent document if the child table has multiple entries.

### Fetching Child Table Records

A more structured way to fetch child table data:

```python
# Get Sales Orders and their associated items
query = frappe.qb.get_query(
    "Sales Order",
    fields=[
        "name",
        "customer",
        {"items": ["item_code", "qty", "rate"]} # Fetch from 'items' child table
    ],
    filters={"docstatus": 1},
    limit=5
)

results = query.run(as_dict=True)

# Example result structure:
# [
#   {
#     'name': 'SO-00001',
#     'customer': 'Customer A',
#     'items': [
#       {'item_code': 'ItemA', 'qty': 2.0, 'rate': 100.0},
#       {'item_code': 'ItemB', 'qty': 1.0, 'rate': 50.0}
#     ]
#   },
#   {
#     'name': 'SO-00002',
#     'customer': 'Customer B',
#     'items': [
#       {'item_code': 'ItemC', 'qty': 5.0, 'rate': 20.0}
#     ]
#   }
# ]
```

This approach performs a separate query for the child records after fetching the parent records, efficiently grouping them by parent.


### SQL Functions in Fields

To use SQL functions in your select clauses, you can use dictionary-based syntax within the `fields` argument.

#### Aggregation Functions

```python
# COUNT - Count rows or non-null values
query = frappe.qb.get_query(
    "User",
    fields=["user_type", {"COUNT": "name", "as": "total_users"}],
    group_by="user_type"
)

# COUNT(*) - Count all rows including nulls
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"COUNT": "'*'", "as": "total_invoices"}]
)

# SUM - Calculate sum of numeric values
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"SUM": "grand_total", "as": "total_sales"}],
    filters={"docstatus": 1}
)

# AVG - Calculate average of numeric values
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"AVG": "grand_total", "as": "avg_invoice_amount"}],
    group_by="customer"
)

# MAX - Find maximum value
query = frappe.qb.get_query(
    "User",
    fields=[{"MAX": "creation", "as": "latest_user_date"}]
)

# MIN - Find minimum value
query = frappe.qb.get_query(
    "User",
    fields=[{"MIN": "creation", "as": "earliest_user_date"}]
)
```

#### Scalar Functions

```python
# ABS - Absolute value
query = frappe.qb.get_query(
    "Journal Entry Account",
    fields=[{"ABS": "debit_in_account_currency", "as": "abs_amount"}]
)

# IFNULL - Handle null values (takes two arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"IFNULL": ["first_name", "'Unknown'"], "as": "display_name"}]
)

# CONCAT - Concatenate strings (takes multiple arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"CONCAT": ["first_name", "' '", "last_name"], "as": "full_name"}]
)

# EXTRACT - Extract part of date/time (takes two arguments: unit and date)
query = frappe.qb.get_query(
    "User",
    fields=[{"EXTRACT": ["'YEAR'", "creation"], "as": "creation_year"}]
)

# NOW - Current timestamp (no arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"NOW": None, "as": "current_time"}]
)
```


## Filtering

### Basic Filters

The `filters` argument allows you to add `WHERE` clauses.

#### Dictionary Filters (Equality)

This is the simplest and often preferred way for equality checks.

```python
# Get users with first_name 'Admin'
query = frappe.qb.get_query(
    "User",
    fields=["name", "email"],
    filters={"first_name": "Admin"} # Simple key-value implies '='
)
```

#### Dictionary Filters (Other Operators)

For operators other than `=`, use a dictionary where the value is a list `[operator, value]`.

```python
# Get users created after a certain date
query = frappe.qb.get_query(
    "User",
    fields=["name", "creation"],
    filters={"creation": [">", "2023-01-01 00:00:00"]}
)

# Get users whose name is like 'test%'
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["like", "test%"]}
)

# Get users whose name is in a list
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["in", ["test1@example.com", "test2@example.com"]]}
)

# Get users whose name is NOT in a list
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["not in", ["Administrator", "Guest"]]}
)
```

#### List Filters (Alternative Format)

You can also provide a list containing filter lists `[[fieldname, operator, value]]`.

```python
# Get users created after a certain date (using list format)
query = frappe.qb.get_query(
    "User",
    fields=["name", "creation"],
    filters=[["creation", ">", "2023-01-01 00:00:00"]]
)

# Multiple filters (combined with AND)
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters=[
        ["enabled", "=", 1],
        ["user_type", "=", "System User"]
    ]
)
```

### Filter Operators

`frappe.qb.get_query` supports various operators:

| Operator String    | SQL Equivalent | Example Usage (Dictionary Format)                    | Example Usage (List Format)                               |
| :----------------- | :------------- | :--------------------------------------------------- | :-------------------------------------------------------- |
| `=`                | `=`            | `{"name": "Test"}`                                   | `[["name", "=", "Test"]]`                                 |
| `!=`               | `!=`           | `{"name": ["!=", "Test"]}`                           | `[["name", "!=", "Test"]]`                                |
| `>`                | `>`            | `{"creation": [">", "2023-01-01"]}`                 | `[["creation", ">", "2023-01-01"]]`                       |
| `<`                | `<`            | `{"creation": ["<", "2023-01-01"]}`                 | `[["creation", "<", "2023-01-01"]]`                       |
| `>=`               | `>=`           | `{"age": [">=", 18]}`                               | `[["age", ">=", 18]]`                                     |
| `<=`               | `<=`           | `{"age": ["<=", 65]}`                               | `[["age", "<=", 65]]`                                     |
| `like`             | `LIKE`         | `{"subject": ["like", "%urgent%"]}`                 | `[["subject", "like", "%urgent%"]]`                       |
| `not like`         | `NOT LIKE`     | `{"subject": ["not like", "spam%"]}`                | `[["subject", "not like", "spam%"]]`                      |
| `in`               | `IN`           | `{"status": ["in", ["Open", "Pending"]]}`           | `[["status", "in", ["Open", "Pending"]]]`                 |
| `not in`           | `NOT IN`       | `{"role": ["not in", ["Guest"]]}`                   | `[["role", "not in", ["Guest"]]]`                         |
| `is`               | `IS NULL` or `IS NOT NULL` | `{"customer": ["is", "set"]}` or `{"email": ["is", "not set"]}` | `[["customer", "is", "set"]]` or `[["email", "is", "not set"]]` |
| `descendants of`   | (Nested Set)   | `{"parent_account": ["descendants of", "Assets"]}`  | `[["parent_account", "descendants of", "Assets"]]`        |
| `ancestors of`     | (Nested Set)   | `{"location": ["ancestors of", "Room 101"]}`        | `[["location", "ancestors of", "Room 101"]]`              |
| `not descendants of` | (Nested Set)   | `{"category": ["not descendants of", "Internal"]}` | `[["category", "not descendants of", "Internal"]]`         |
| `not ancestors of` | (Nested Set)   | `{"territory": ["not ancestors of", "West Coast"]}` | `[["territory", "not ancestors of", "West Coast"]]`       |

**Note on `is set` / `is not set`:** These check if a field has a value (`IS NOT NULL` and `IS NULL` respectively).

### Filtering on Linked Document Fields

You can filter based on fields in linked documents using dot notation: `link_fieldname.target_fieldname`.

```python
# Get Sales Orders where the linked Customer's territory is 'North America'
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer"],
    filters={"customer.territory": "North America"} # Filter on linked field
)
north_america_orders = query.run(as_dict=True)
```

### Filtering by Child Table Fields

You can filter parent records based on values in their child table records using dot notation: `child_table_fieldname.target_fieldname`.

```python
# Get Sales Orders that contain 'Item A' in their items table
# Use distinct=True to ensure each Sales Order appears only once
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer"],
    filters={"items.item_code": "Item A"}, # Filter based on child table field
    distinct=True
)
orders_with_item_a = query.run(as_dict=True)
```

**Important:** When filtering based on child table fields, use `distinct=True` if you only want unique parent records.

### Nested Set Filters

For DocTypes that are trees (using `lft` and `rgt` columns, like Account, Territory, Warehouse, etc.), you can use special filters:

```python
# Get all accounts under 'Assets'
query = frappe.qb.get_query(
    "Account",
    fields=["name"],
    filters={"parent_account": ["descendants of", "Assets"]}
)

# Get the parent territories of 'West Coast'
query = frappe.qb.get_query(
    "Territory",
    fields=["name"],
    filters={"parent_territory": ["ancestors of", "West Coast"]}
)
```

### Logical Operators (AND/OR)

For complex conditions, structure your `filters` as a list combining conditions with `'and'` or `'or'`.

```python
# Find users who are enabled AND have first name 'Admin'
filters_and = [
    ["enabled", "=", 1],
    "and",
    ["first_name", "=", "Admin"],
]
query = frappe.qb.get_query("User", filters=filters_and)

# Find users who have first name 'Admin' OR 'Guest'
filters_or = [
    ["first_name", "=", "Admin"],
    "or",
    ["first_name", "=", "Guest"],
]
query = frappe.qb.get_query("User", filters=filters_or)

# Combine AND and OR (use nested lists for grouping)
# Find users who are enabled AND (have first name 'Admin' OR 'Guest')
filters_nested = [
    ["enabled", "=", 1],
    "and",
    [
        ["first_name", "=", "Admin"],
        "or",
        ["first_name", "=", "Guest"],
    ]
]
query = frappe.qb.get_query("User", filters=filters_nested)
```

## Query Execution

### Basic Execution

Once you have the `query` object, execute it using `.run()`:

```python
# Returns a list of tuples by default
results = query.run()

# Returns a list of dictionaries
results = query.run(as_dict=True)

# Returns a list of lists
results = query.run(as_list=True)

# If selecting a single field, returns a flat list of values
results = query.run(pluck=True)

# Print the generated SQL query and execution time
results = query.run(debug=True)
```

### Getting the SQL String

You can get the generated SQL string without executing:

```python
# Get the SQL string with values directly substituted (for debugging)
sql_string = query.get_sql()
print(sql_string)
# Example Output: SELECT `name`, `email` FROM `tabUser` WHERE `first_name`='Admin'
```

### Using Iterators for Large Datasets

When dealing with large datasets, use `as_iterator=True` to process results row by row without loading everything into memory:

```python
# Process a large number of tasks without loading all into memory
query = frappe.qb.get_query(
    "Task",
    fields=["name", "subject", "status"],
    filters={"status": "Open"}
)

# Use unbuffered_cursor for optimal memory usage with the iterator
with frappe.db.unbuffered_cursor():
    task_iterator = query.run(as_iterator=True, as_dict=True)

    processed_count = 0
    for task in task_iterator:
        # Process each task dictionary one by one
        print(f"Processing Task: {task['name']} - {task['subject']}")
        processed_count += 1
        if processed_count % 1000 == 0:
            print(f"Processed {processed_count} tasks...")
```

**Requirements:**

- You must use `as_iterator=True` with either `as_dict=True` or `as_list=True`
- For optimal memory efficiency, use within `frappe.db.unbuffered_cursor()` context manager

## Ordering, Grouping, and Pagination

### Ordering Results

Use the `order_by` argument to sort results:

```python
# Order users by creation date, ascending
query = frappe.qb.get_query("User", fields=["name", "creation"], order_by="creation asc")

# Order by multiple fields
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["name", "customer", "grand_total"],
    order_by="customer asc, grand_total desc"
)
```

### Grouping Results

Use `group_by` for aggregation:

```python
# Count invoices per customer
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["customer", {"COUNT": "'*'", "as": "invoice_count"}],
    filters={"docstatus": 1},
    group_by="customer"
)
results = query.run(as_dict=True)
# results: [{'customer': 'Cust A', 'invoice_count': 5}, {'customer': 'Cust B', 'invoice_count': 3}, ...]
```

### Pagination

Use `limit` and `offset` for pagination:

```python
# Get the first 10 users
query = frappe.qb.get_query("User", limit=10)

# Get the next 10 users (page 2)
query = frappe.qb.get_query("User", limit=10, offset=10)
```

### Distinct Results

Use `distinct=True` to get unique rows:

```python
# Get distinct customers from submitted Sales Invoices
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["customer"],
    filters={"docstatus": 1},
    distinct=True
)
```

## Permissions

### The `ignore_permissions` Flag

By default, `frappe.qb.get_query` **ignores** permissions (`ignore_permissions=True`). To enforce permissions, set `ignore_permissions=False`:

```python
# This query bypasses all permission checks (default behavior)
query_ignore = frappe.qb.get_query("DocType", fields=["name"], filters={"istable": 1})

# This query enforces standard Frappe permissions for the current user
query_enforce = frappe.qb.get_query(
    "DocType",
    fields=["name"],
    filters={"istable": 1},
    ignore_permissions=False # Explicitly enable permission checks
)

try:
    results = query_enforce.run()
except frappe.PermissionError:
    print("User does not have permission to read DocType!")
```

### How Permissions are Applied

When `ignore_permissions=False`:

1. **Role Permissions:** Checks if the user has 'read' or 'select' permission based on their roles.
2. **User Permissions:** Applies User Permissions (Allow/Restrict) defined for the DocType and linked DocTypes.
3. **Sharing:** Includes documents explicitly shared with the user.
4. **Owner Constraint:** If the role permissions only grant access `if_owner`, the query restricts results to documents owned by the user.
5. **Permission Query Conditions:** Applies conditions defined via Hooks or Server Scripts.
6. **Field Level Security:** Filters the selected `fields`, and does not allow fields used in `filters`, `group_by`, `order_by` if user does not have permlevel access. Also checks fields in `link_field.target_field` and `child_field.target_field` notations.

### Field-Level Security

When `ignore_permissions=False`:

- **`fields`:** Only fields accessible at the user's maximum permitted permlevel are included. Requesting inaccessible fields will **silently remove** the field from the selection.
- **`filters`:** Filtering is **only allowed** on fields the user has permission to access. Attempting to filter on an inaccessible field **will raise** a `frappe.PermissionError`.
- **`group_by`:** Grouping is **only allowed** on fields the user has permission to access. Attempting to group by an inaccessible field **will raise** a `frappe.PermissionError`.
- **`order_by`:** Ordering is **only allowed** on fields the user has permission to access. Attempting to order by an inaccessible field **will raise** a `frappe.PermissionError`.
- **Linked and Child Table Fields:** When using `link_field.target_field` or `child_field.target_field` notation in any of the above clauses, the system checks permissions for both the link/child field itself and the target field in the linked/child DocType.

```python
# Assume 'published' field in Blog Post has permlevel 1
# User 'test@example.com' only has permlevel 0 access

# This works, but 'published' field is silently removed from results
query = frappe.qb.get_query(
    "Blog Post",
    fields=["name", "title", "published"], # 'published' requested but inaccessible
    ignore_permissions=False,
    user="test@example.com"
)
# result will contain 'name' and 'title', but NOT 'published'

# This FAILS because filtering on 'published' is not allowed for this user
try:
    query = frappe.qb.get_query(
        "Blog Post",
        fields=["name"],
        filters={"published": 1}, # Filtering on restricted field
        ignore_permissions=False,
        user="test@example.com"
    )
    query.run()
except frappe.PermissionError as e:
    print(f"Permission error: {e}")
```

### Specifying User and Parent Context

```python
# Check permissions for a specific user
query = frappe.qb.get_query(
    "Task",
    ignore_permissions=False,
    user="test@example.com" # Check permissions for this user
)

# Provide parent context for child DocTypes
query = frappe.qb.get_query(
    "Sales Order Item",
    fields=["item_code", "qty"],
    filters={"parent": "SO-00001"},
    ignore_permissions=False,
    parent_doctype="Sales Order" # Specify parent context for permission checks
)
```

## Advanced Features

### Using Pypika Objects

For complex scenarios involving subqueries, advanced conditions, or functions not available in the dictionary syntax, you can use Pypika objects directly.

#### Pypika Objects in Fields

```python
from frappe.query_builder import Field, functions, Query

# Define Pypika objects
user_table = frappe.qb.DocType("User")
todo_table = frappe.qb.DocType("ToDo")

# Build a subquery to count open ToDos for each user
open_todo_subquery = (
    Query.from_(todo_table)
    .select(functions.Count("*"))
    .where(todo_table.owner == user_table.name) # Correlated subquery
    .where(todo_table.status == "Open")
).as_("open_todos_count")

# Use Pypika objects in fields
query = frappe.qb.get_query(
    "User",
    fields=[
        user_table.name,
        user_table.email,
        open_todo_subquery # Using the subquery object
    ],
    filters={"user_type": "System User"}
)
users_with_counts = query.run(as_dict=True)
```

#### Pypika Objects in Filters

```python
from frappe.query_builder import Field, functions

# Define Pypika objects
task_table = frappe.qb.DocType("Task")
modified_field = task_table.modified
creation_field = task_table.creation
subject_field = task_table.subject
status_field = task_table.status

# Build complex criterion
complex_filter = (
    (modified_field > creation_field) & (functions.Length(subject_field) > 10)
) | (status_field == "Cancelled")

# Use the Criterion object in filters
query = frappe.qb.get_query(
    "Task",
    fields=["name", "subject", "status", "creation", "modified"],
    filters=complex_filter
)
results = query.run(as_dict=True)
```

### Record Locking

For use within database transactions where you need to prevent other transactions from modifying specific rows:

#### Basic Locking

```python
# Lock specific Stock Ledger Entries
query = frappe.qb.get_query(
    "Stock Ledger Entry",
    fields=["name", "qty_after_transaction"],
    filters={"item_code": "ITEM001", "warehouse": "WH001"},
    for_update=True # Adds FOR UPDATE clause, will wait if rows are locked
)
entries = query.run(as_dict=True)
```

#### Skip Locked Rows

```python
# Skip rows that are already locked by another transaction
query = frappe.qb.get_query(
    "ToDo",
    fields=["name", "description"],
    filters={"status": "Pending"},
    limit=5,
    order_by="creation asc",
    for_update=True,
    skip_locked=True # Skip locked rows
)
available_tasks = query.run(as_dict=True)
```

#### Non-Blocking Lock Attempt

```python
# Fail immediately if rows are already locked
try:
    query = frappe.qb.get_query(
        "System Settings",
        fields=["name"],
        filters={"name": "System Settings"},
        for_update=True,
        wait=False # Don't wait for locks
    )
    settings = query.run(as_dict=True)
except Exception as e:
    print(f"Could not acquire lock immediately: {e}")
```

## Security Considerations

`frappe.qb.get_query` is designed with security in mind:

- **Field Validation:** Field names are validated against strict patterns to prevent SQL injection.
- **Parameterization:** Filter values are parameterized by the database driver.
- **Permission Enforcement:** Using `ignore_permissions=False` leverages Frappe's robust permission system.

Always ensure that any dynamic values used to construct filter keys or field names are properly sanitized if they originate from untrusted sources. **Always rely on passing user input as filter values.**


Written by Claude Sonnet 4. Reviewed by human.

<!-- page: framework/framework__guides-app-development__updating-a-field-from-a-linked-doctype.md -->
---
title: "Updating a Field from a Linked Doctype"
space: "Framework"
url: "https://docs.frappe.io/framework/guides-app-development/updating-a-field-from-a-linked-doctype"
updated: "2026-07-05"
---

ERPNext lets you fetch a value from a linked document into another field by using the **Fetch From** property. This is useful when one field should automatically show information from a selected linked record.

For example, when a user selects a **Customer**, you may want to automatically show the customer's territory, tax ID, customer group, or another field from the Customer master. Instead of writing a Client Script, you can configure this using **Fetch From** in the field settings.



[https://www.youtube.com/watch?v=78Yp_OdXnBI](https://www.youtube.com/watch?v=78Yp_OdXnBI)

## How Fetch From Works

Fetch From works with a **Link** field.

The format is:

```text
link_fieldname.field_to_fetch
```

Where:

- `link_fieldname` is the fieldname of the Link field in the current DocType.
- `field_to_fetch` is the fieldname from the linked DocType.

When the user selects a value in the Link field, ERPNext reads the selected linked document and copies the specified field value into the current field.

## Example

Suppose you have a custom field on **Sales Order** called **Customer Territory**, and you want it to automatically fetch the territory from the selected Customer.

In this case:

- The Link field on Sales Order is `customer`.
- The field to fetch from Customer is `territory`.
- The Fetch From value should be:

```text
customer.territory
```

When a user selects a Customer in the Sales Order, ERPNext fetches the Customer's Territory and fills it in the Customer Territory field.

## Steps To Configure Fetch From

1. Go to **Customize Form**.
2. Select the DocType where you want to show the fetched value.
3. Add or select the target field where the fetched value should appear.
4. In the field settings, enter the **Fetch From** value using this format:

```text
link_fieldname.field_to_fetch
```

5. Save the customization.
6. Reload the form and test by selecting a linked document.

## Another Example

If you want to fetch the **Supplier Group** from the selected Supplier into a custom field on Purchase Order:

- Link field: `supplier`
- Field to fetch: `supplier_group`
- Fetch From value:

```text
supplier.supplier_group
```

When the Supplier is selected, ERPNext fetches the Supplier Group into the target field.

## Important Notes

- Fetch From works only when the source field is available on the linked DocType.
- Use the **fieldname**, not the field label. For example, use `customer_group`, not `Customer Group`.
- The target field should have a compatible field type. For example, fetch text into a Data field, dates into a Date field, and linked records into a Link field where appropriate.
- Fetch From is best for simple one-way fetching. If the value needs complex conditions, calculations, or multiple dependent updates, use a Client Script instead.
- If the value in the linked document changes later, existing documents may not update automatically unless the link field is changed or the document is refreshed and saved according to the form behavior.

## Common Mistakes

- **Using the label instead of fieldname:** `customer.Customer Group` will not work. Use `customer.customer_group`.
- **Using the wrong link field:** The first part must be the fieldname of the Link field on the current form.
- **Fetching from a field that does not exist:** Check the linked DocType to confirm the exact fieldname.
- **Expecting complex logic:** Fetch From copies a value. It is not a replacement for business logic or validation.

## When To Use Fetch From

Use Fetch From when:

- A field should show a value from a selected Customer, Supplier, Item, Employee, Project, or another linked record.
- The value is informational and follows the selected linked document.
- You want a no-code configuration instead of a Client Script.
- The fetching rule is simple and does not require conditions or calculations.

## Related Topics

- [Customize Form](https://docs.frappe.io/erpnext/customize-form)
- [Custom Field](https://docs.frappe.io/erpnext/custom-field)
- [Client Script](https://docs.frappe.io/erpnext/customization/custom-scripts)
- [DocType](https://docs.frappe.io/framework/user/en/basics/doctypes)
- [Link Field](https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes)
