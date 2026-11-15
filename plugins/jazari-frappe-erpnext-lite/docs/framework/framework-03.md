<!-- Frappe documentation: framework, part 3 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__help__event-streaming.md -->
---
title: "Event Streaming"
space: "Framework"
url: "https://docs.frappe.io/framework/help/event-streaming"
updated: "2026-07-04"
---

Event Streaming was a Frappe feature used to publish document changes from one Frappe site and consume them on another site. It was useful when selected DocTypes needed to be synchronized between sites without building a separate integration for every record type.

## How Event Streaming Worked

In a typical setup, one site acted as the **Event Producer** and another site acted as the **Event Consumer**. When selected documents were created or updated on the producer site, events were recorded and then consumed by the other site. This made it possible to replicate masters, transactions, or custom DocTypes across Frappe sites.

## Status In Version 15 And Later

Event Streaming is not supported as a maintained core feature from Frappe/ERPNext version 15 onward. In Frappe version 14, Event Streaming existed inside the framework source under `frappe/event_streaming`. In version 15, Frappe added a removal patch for the Event Streaming module and its DocTypes, including Event Producer, Event Consumer, Event Update Log, and related mapping DocTypes.

## Separate App

The feature was separated into its own app: [frappe/event_streaming](https://github.com/frappe/event_streaming). However, the app is not actively maintained. The GitHub repository was archived by Frappe on December 6, 2024, is now read-only, and has no published releases. Treat it as unsupported for new production implementations unless your team is ready to test and maintain it independently.

## Recommended Alternatives

- **REST API:** Use Frappe's REST API for explicit integrations between ERPNext and other systems.
- **Webhooks:** Use webhooks when another system should be notified after a document is created or updated.
- **Background Jobs:** Use scheduled or queued jobs for sync logic that needs retries, logs, and error handling.
- **Custom Integration Apps:** Build a custom app when data mapping, conflict handling, or business rules need to be controlled carefully.

## When To Be Careful

Avoid planning new implementations around Event Streaming on version 15 or later. For current ERPNext integrations, prefer APIs, webhooks, and integration-specific queues so ownership, retry behavior, and failure handling are clear.

## Related Topics

- [frappe/event_streaming on GitHub](https://github.com/frappe/event_streaming)
- [Frappe version 15 Event Streaming removal patch](https://github.com/frappe/frappe/blob/version-15/frappe/patches/v15_0/remove_event_streaming.py)
- [Frappe REST API](https://docs.frappe.io/framework/user/en/api/rest)
- [Webhooks](https://docs.frappe.io/framework/user/en/guides/integration/webhooks)
- [Background Jobs](https://docs.frappe.io/framework/user/en/api/background_jobs)

<!-- page: framework/framework__keyboard-shortcuts.md -->
---
title: "Keyboard Shortcuts"
space: "Framework"
url: "https://docs.frappe.io/framework/keyboard-shortcuts"
updated: "2026-07-04"
---

# Keyboard Shortcuts

Keyboard shortcuts help you move around Frappe Desk without switching between the keyboard and mouse. Use them to open pages, search for records, save forms, open help, and view the complete shortcuts list from anywhere in Desk.

The shortcuts shown in Desk follow your operating system. On macOS, Desk shows **Command** as **⌘** and **Option** as **⌥**. On Windows and Linux, use the equivalent **Ctrl** and **Alt** keys where applicable.

## View keyboard shortcuts

Press **Shift + /** to open the Keyboard Shortcuts panel. The panel lists the global shortcuts available in Desk.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Global shortcuts


| Shortcut          | Action                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **⌘ + S**         | Trigger the primary action on the current page. On a form, this is usually the save action. |
| **⌘ + K**         | Open the Awesomebar.                                                                        |
| **⌘ + G**         | Open the Awesomebar.                                                                        |
| **⌥ + S**         | Open Settings.                                                                              |
| **Shift + /**     | Show Keyboard Shortcuts.                                                                    |
| **⌥ + H**         | Open Help.                                                                                  |
| **Shift + ⌘ + R** | Clear cache and reload.                                                                     |
| **Shift + T**     | Open the console.                                                                           |
| **Shift + ⌘ + G** | Switch theme.                                                                               |


Press **Alt** to reveal additional shortcuts in the menu and sidebar.

## Open pages with the Awesomebar

Press **⌘ + K** or **⌘ + G** to open the Awesomebar. Start typing the page, report, document type, or record you want to open, then use the arrow keys to move through results and press **Enter** to select one.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Navigate search results

- Use the **Up** and **Down** arrow keys to move through results.
- Press **Enter** to open the selected result.
- Press **Esc** to close the Awesomebar or shortcut panel.

## When shortcuts do not work

Some browser, operating system, or extension shortcuts may take priority over Desk shortcuts. If a shortcut does not work, click inside the Desk page and try again. If the cursor is inside a text field, close the field or move focus back to the page before using a global shortcut.

<!-- page: framework/framework__notifications.md -->
---
title: "Notifications"
space: "Framework"
url: "https://docs.frappe.io/framework/notifications"
updated: "2026-02-17"
---

The **Notification** doctype in Frappe Framework provides a powerful way to automate notifications across different channels when specific events occur in your system. This guide explains how to configure and use notifications effectively.

## General Settings

- **Enabled**: Toggle to activate or deactivate a notification.
- **Channel**: Select the delivery method for your notification:
  - **Email**: Send notifications via email
  - **Slack**: Send notifications to a Slack channel
  - **System Notification**: Display notifications within the Frappe interface
  - **SMS**: Send notifications via SMS (requires SMS Settings configuration)
- **Is Standard**: For developer mode; marks the notification as part of a standard module

## Event Triggers

Notifications can be triggered based on various events:

### Document Events

- **New**: Triggered when a new document is created
- **Save**: Triggered when a document is saved
- **Submit**: Triggered when a document is submitted
- **Cancel**: Triggered when a document is cancelled

### Date-Based Events

- **Days Before**: Triggered a specific number of days before a date field value
- **Days After**: Triggered a specific number of days after a date field value
- When using these events:
  - **Reference Date**: Select the date field to monitor
  - **Days Before or After**: Specify number of days before/after the date to trigger

### Value-Based Events

- **Value Change**: Triggered when a specific field's value changes
  - **Value Changed**: Select the field to monitor for changes

### Method-Based Events

- **Method**: Triggered when a specific document method is called
  - **Trigger Method**: Specify the method name (e.g., "before_insert", "after_update")

### Custom Events

- **Custom**: For programmatically triggered notifications

## Conditional Triggers

You can make notifications more targeted by adding conditions:

- **Condition**: A Python expression that must evaluate to `True` for the notification to be sent
- The condition has access to:
  - `doc`: The document that triggered the notification
  - `nowdate()`: Current date function
  - `frappe.utils`: Utility functions

### Examples

- The _Status_ of the document is "Open"

    ```python
    doc.status=="Open"
    ```

- The document's _Due Date_ matches the current date

    ```python
    doc.due_date==nowdate()
    ```

- The total is bigger than 40,000

    ```python
    doc.total > 40000
    ```

## Recipients Configuration

### Email, System Notification, and SMS Channels

Configure recipients using the Recipients table:

1. **Receiver Type**:

   - **By Document Field**: Select a field containing email addresses/phone numbers
   - **By Role**: Select a role whose users will receive the notification
   - **Custom**: Specify custom recipients

2. **Additional Options**:

   - **CC/BCC**: For email notifications
   - **Condition**: Python expression to conditionally include recipients
   - **Send to All Assignees**: Include all users assigned to the document

### For Slack Channel

- Select a predefined Slack Webhook URL from the dropdown

## Message Configuration

### Subject (for Email, Slack, and System Notifications)

- Enter the subject line text
- Support for Jinja templates: `{{ doc.name }} Delivered`

### Message Body

- **Message Type**: Select between HTML, Markdown, or Plain Text (available in developer mode only)
- **Message**: Enter the notification content
- Uses Jinja templating for dynamic content

### Templating Variables

- `{{ doc }}`: Access any field from the triggering document (e.g., `{{ doc.customer }}`)
- `{{ comments }}`: Access document comments (e.g., `{{ comments[-1].comment }}`)
- `{% if %}...{% endif %}`: Conditional logic
- `{{ nowdate() }}`: Current date

### Template Example

```html
<h3>Order Overdue</h3>

<p>Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.</p>

<!-- show last comment -->
{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

<h4>Details</h4>

<ul>
<li>Customer: {{ doc.customer }}
</li><li>Amount: {{ doc.grand_total }}
</li></ul>
```

## Advanced Options

### Attachment Settings

- **Attach Print**: Attach a PDF printout of the document
    - **Print Format**: Select a specific print format for the attached PDF
- **Attach Files**:
    - "All": sends all files that are attached to the record that triggered the notification
    - "From Field": sends a file from a specific attachment field
        - **From Attach Field**: Select the field that holds the attachment you want to send

### Post-Notification Actions

- **Set Property After Alert**: Update a field after sending the notification
- **Value To Be Set**: The value to set in the specified field

## Best Practices

1. **Test your notifications**: Use the "Get Alerts for Today" button to test date-based notifications.
2. **Keep conditions specific**: Make sure your conditions are targeted to avoid notification fatigue.
3. **Use templating wisely**: Make messages clear and include only relevant information.
4. **Verify recipient fields**: Ensure fields contain valid email addresses or phone numbers.
5. **Consider permission levels**: Recipients must have permission to access documents referenced in notifications.

## Troubleshooting

- If notifications aren't sending, check that the document meets all conditions.
- For email notifications, verify email settings are properly configured.
- For SMS notifications, ensure SMS settings are configured.
- For Slack notifications, verify webhook URL is valid and active.
- Check server logs for any errors related to notification delivery.

## Technical Notes

- Notifications are processed asynchronously to avoid impact on system performance.
- Date-based events are checked daily via a scheduled job.
- Document-event notifications are triggered in real-time when the associated action occurs.
- Conditions and templates are evaluated in a restricted environment for security.

By effectively configuring the Notification doctype, you can keep users informed about important events and automate communication across your Frappe application.

<!-- page: framework/framework__oauth2.md -->
---
title: "OAuth2"
space: "Framework"
url: "https://docs.frappe.io/framework/oauth2"
updated: "2026-02-17"
---

Frappe Framwork uses [`oauthlib`](https://github.com/oauthlib/oauthlib) to manage OAuth2 requirements. A Frappe instance can function as all of these:

1. **Resource Server**: contains resources, for example the data in your DocTypes.
2. **Authorization Server**: server that issues tokens to access some resource.
3. **Client**: app that requires access to some resource on a resource server.

DocTypes pertaining to the above roles:

1. **Common**
   - **OAuth Settings**: allows configuring certain OAuth features pertaining to the three roles.
2. **Authorization Server**
   - **OAuth Client**: keeps records of _clients_ registered with the frappe instance.
   - **OAuth Bearer Token**: tokens given out to registered _clients_ are maintained here.
   - **OAuth Authorization Code**: keeps track of OAuth codes a client responds with in exchange for a token.
   - **OAuth Provider Settings**: allows skipping authorization. `[DEPRECATED]` use **OAuth Settings** instead.
3. **Client**
   - **Connected App**: keeps records of _authorization servers_ against whom this frappe instance is registered as a _client_ so some resource can be accessed. Eg. a users Google Drive account.
   - **Social Key Login**: similar to **Connected App**, but for the purpose of logging into the frappe instance. Eg. a users Google account to enable "Login with Google".
   - **Token Cache**: tokens received by the Frappe instance when accessing a **Connected App**.

### Features

Additional features over `oauthlib` that have implemented in the Framework:

- **Dynamic Client Registration**: allows a client to register itself without manual configuration by the resource owner. [RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)
- **Authorization Server Metadata Discovery**: allows a client to view the instance's auth server (itself) metadata such as auth end points. [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)
- **Resource Server Metadata Discovery**: allows a client to view the instance's resource server metadata such as documentation, auth servers, etc. [RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)

### Additional Docs

Documentation of various OAuth2 features:

1. [How to setup OAuth 2?](https://docs.frappe.io/framework/user/en/guides/integration/how_to_set_up_oauth)
2. [OAuth 2](https://docs.frappe.io/framework/user/en/guides/integration/rest_api/oauth-2)
3. [Token Based Authentication](https://docs.frappe.io/framework/user/en/guides/integration/rest_api/token_based_authentication)
4. [Using Frappe as OAuth Service](https://docs.frappe.io/framework/user/en/using_frappe_as_oauth_service)
5. [Social Login Key](https://docs.frappe.io/framework/user/en/guides/integration/social_login_key)
6. [Connected App](https://docs.frappe.io/framework/user/en/guides/app-development/connected-app)

> **Warning**
>
> Some of these pages might be outdated, it is always recommended to check the
> code when in doubt.

### OAuth Settings

A Single doctype that allows configuring OAuth2 related features. It is
recommended to open the DocType page itself as each field has a
sufficiently descriptive help text.

The settings allow toggling the following features:

- Authorization check when active token is present using the _Skip Authorization_ field. _**Note**: Keep this unchecked in production._
- **Authorization Server Metadata Discovery**: by toggling the _Show Auth Server Metadata_ field.
- **Dynamic Client Registration**: by toggling the _Enable Dynamic Client Registration_ field.
- **Resource Server Metadata Discovery**: by toggling the _Show Protected Resource Metadata_.

The remaining fields (in the **Resource** section) are used only when responding to requests on `/.well-known/oauth-protected-resource`

> **Regarding Public Clients**
>
> Public clients, for example an SPA, have restricted access by default. This
> restriction is applied by use of CORS.
>
> To side-step this restriction for certain trusted clients, you may add their
> hostnames to the **Allowed Public Client Origins** field.

<!-- page: framework/framework__permission-types.md -->
---
title: "Permission Types"
space: "Framework"
url: "https://docs.frappe.io/framework/permission-types"
updated: "2026-02-17"
---

> Note: This feature is available v16 onwards.

Custom Permission Types let you create permission flags beyond the built-in ones `read`, `write`, `create`, `delete`, `submit`). Use them for action-specific permissions like "approve record", "download file", or "impersonate user".

## How it works

There are three steps:

1. **Developer creates the permission type** in dev mode for a DocType
2. **Developer adds permission checks** in code where the action happens
3. **System Manager assigns the permission to roles** in the Desk UI

The permission type is saved as a fixture and shipped with your app.

## Example: Creating an "approve" permission on Invoice

### Step 1: Create the permission type (Developer)

1. Enable developer mode and log in as Administrator
2. Create a new **Permission Type** record
3. Set **Perm Type** as `approve` and **DocType** as `Invoice`
4. Save

The permission type is now created and will be exported with your app.

### Step 2: Add permission checks in your code (Developer)

In your Invoice controller or in functions that handle approvals, check for the permission:

```python
@frappe.whitelist()
def approve_invoice(invoice_name):
    invoice = frappe.get_doc("Invoice", invoice_name)
    if not frappe.has_permission(invoice, "approve"):
        frappe.throw("Not permitted to approve", frappe.PermissionError)
    invoice.approval_status = "Approved"
    invoice.save()
```

You can also check without throwing an error:

```python
if frappe.has_permission(invoice, "approve"):
    # show approve button on frontend
```

### Step 3: Assign to roles (System Manager)

After your app is installed, system managers assign the permission to roles:

1. Open **Role Permission Manager**
2. Select the Invoice DocType
3. For each role, check or uncheck the "Approve" column, just like other permissions
4. The permission is now applied to all users with that role

That's it. Users with the "approve" permission can now perform the action. Users without it will see an error.

## How to check the permission

Use `frappe.has_permission()` in your Python code:

```python
# Check document-level permission
if frappe.has_permission(invoice_doc, "approve"):
    # User can approve this invoice

# Check DocType-level permission
if frappe.has_permission("Invoice", "approve"):
    # User can approve any invoice
```

<!-- page: framework/framework__portal-web-form__web-form-request.md -->
---
title: "Web Form Request"
space: "Framework"
url: "https://docs.frappe.io/framework/portal-web-form/web-form-request"
updated: "2026-06-26"
---

## Web Form Request

A **Web Form Request** creates a private request link for a **Web Form**.

Use it when a form should not be fully public, but the respondent should still be able to submit it without having a user account. For example, you can send a customer satisfaction survey link to a customer, pre-fill customer-specific values, and keep internal fields hidden from the browser.

## When to Use

Use a **Web Form Request** when:

1. The respondent should open the form through a private link.
2. The respondent may not have a user account.
3. The form should include respondent-specific values.
4. The target document needs hidden values that should not be exposed in the web page.

## Creating a Request

Create a **Web Form Request** and select the *Web Form* it belongs to. A URL-safe key is generated automatically.

The request can define:

- *Expires On*: expiry date and time for the request key.
- *Web Form Values*: JSON values shown in the web form and editable by the respondent.
- *Doc Values*: JSON values applied to the target document on submission, but not sent to the browser.

The request key is used in the web form URL:

```text
/your-web-form-route/new?web_form_request_key=<key>
```

You can copy this URL from the **Web Form Request** form.

## Requiring a Key

Enable *Key required* on the **Web Form** to require a valid **Web Form Request** key.

If *Key required* is enabled and no valid key is provided, the web form cannot be opened or submitted.

If *Login required* is also enabled, both conditions apply: the user must be logged in and must provide a valid request key.

## Pre-filled and Hidden Values

Use *Web Form Values* for fields that should be visible to the respondent. These fields must be included in the **Web Form** fields table.

Use *Doc Values* for fields that should be set on the created document but should not be visible to the respondent. These fields must exist on the target DocType.

The JSON keys must use the underlying field names, for example `customer` or `survey_source`.

Example:

```json
{
 "customer": "CUST-0001",
 "survey_source": "Partner CSAT"
}
```

## Expiry and Usage

If *Expires On* is set, the request key cannot be used after that date and time.

For a single-response web form, the request is marked as used after successful submission and links to the created target document. This allows the same key to be used later for editing or deleting that response if the **Web Form** settings allow it.

For a **Web Form** with *Allow multiple responses* enabled, the request key can be reused for multiple submissions and does not link to a single target document.

## Related Web Form Settings

- *Allow Multiple Responses:*  
If enabled, the same request key can submit multiple responses. In this mode, the **Web Form Request** cannot have a *Reference Docname*, because one request may create many documents.
- *Allow Editing After Submit:*  
If enabled, a request key linked to a response can open and edit that response.
- *Allow Delete:*  
If enabled, a request key linked to a response can delete that response.

<!-- page: framework/framework__sqlite-search.md -->
---
title: "SQLite Search"
space: "Framework"
url: "https://docs.frappe.io/framework/sqlite-search"
updated: "2026-02-17"
---

SQLite Search is a full-text search framework for Frappe applications that provides advanced search capabilities using SQLite's FTS5 (Full-Text Search) engine. It offers features like spelling correction, time-based recency scoring, custom ranking, permission-aware filtering, and extensible scoring pipelines.

## Table of Contents

- [Quick Start](#quick-start)

- [How It Works](#how-it-works)

- [Configuration](#configuration)

- [Features &amp; Customization](#features--customization)

- [API Reference](#api-reference)

## Quick Start

### 1. Create a Search Class

Create a search implementation by extending `SQLiteSearch`:

```python

# my_app/search.py

from frappe.search.sqlite_search import SQLiteSearch

class MyAppSearch(SQLiteSearch):

    # Database file name

    INDEX_NAME = "my_app_search.db"

    # Define the search schema

    INDEX_SCHEMA = {

        "metadata_fields": ["project", "owner", "status"],

        "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_'",

    }

    # Define which doctypes to index and their field mappings

    INDEXABLE_DOCTYPES = {

        "Task": {

            "fields": ["name", {"title": "subject"}, {"content": "description"}, "modified", "project", "owner", "status"],

        },

        "Issue": {

            "fields": ["name", "title", "description", {"modified": "last_updated"}, "project", "owner"],

            "filters": {"status": ("!=", "Closed")},  # Only index non-closed issues

        },

    }

    def get_search_filters(self):

        """Return permission filters for current user"""

        # Get projects accessible to current user

        accessible_projects = frappe.get_all(

            "Project",

            filters={"owner": frappe.session.user},

            pluck="name"

        )

        if not accessible_projects:

            return {"project": []}  # No access

        return {"project": accessible_projects}

```

### 2. Register the Search Class

Add your search class to hooks.py:

```python

# my_app/hooks.py

sqlite_search = ['my_app.search.MyAppSearch']

```

### 3. Create API Endpoint

Create a whitelisted method to expose search functionality:

```python

# my_app/api.py

import frappe

from my_app.search import MyAppSearch

@frappe.whitelist()

def search(query, filters=None):

    search = MyAppSearch()

    result = search.search(query, filters=filters)

    return result

```

### 4. Build the Index

Build the search index programmatically or via console:

```python

from my_app.search import MyAppSearch

search = MyAppSearch()

search.build_index()

```

## How It Works

### 1. Indexing Process

#### Full Index Building

When you call `build_index()`, the framework performs a complete index rebuild:

1. **Database Preparation**: Creates a temporary SQLite database with FTS5 tables configured according to your schema

2. **Document Collection**: Queries all specified doctypes using the configured field mappings and filters

3. **Document Processing**: For each document:

   - Extracts and maps fields according to `INDEXABLE_DOCTYPES` configuration

   - Cleans HTML content using BeautifulSoup to extract plain text

   - Applies custom document preparation logic if `prepare_document()` is overridden

   - Validates required fields (title, content) are present

4. **Batch Insertion**: Inserts processed documents into the FTS5 index in batches for performance

5. **Vocabulary Building**: Constructs a spelling correction dictionary from all indexed text

6. **Atomic Replacement**: Replaces the existing index database with the new one atomically

#### Individual Document Indexing

For real-time updates using `index_doc()` or `remove_doc()`:

1. **Single Document Processing**: Retrieves and processes one document using the same field mapping logic

2. **Incremental Update**: Updates the existing FTS5 index by inserting, updating, or deleting the specific document

3. **Vocabulary Update**: Updates the spelling dictionary with new terms from the document

### 2. Search Process

When a user performs a search using `search()`, the framework executes these steps:

1. **Permission Filtering**: Calls `get_search_filters()` to determine what documents the current user can access

2. **Query Preprocessing**:

   - Validates the search query is not empty

   - Combines user-provided filters with permission filters

3. **Spelling Correction**:

   - Analyzes query terms against the vocabulary dictionary

   - Uses trigram similarity to suggest corrections for misspelled words

   - Expands the original query with corrected terms

4. **FTS5 Query Execution**:

   - Constructs an FTS5-compatible query string

   - Executes the full-text search against the SQLite database

   - Applies metadata filters (status, owner, project, etc.)

   - Retrieves raw results with BM25 scores

5. **Results Processing**:

   - **Custom Scoring**: Applies the scoring pipeline to calculate final relevance scores

     - Base BM25 score processing

     - Title matching boosts (exact and partial matches)

     - Recency boosting based on document age

     - Custom scoring functions (doctype-specific, priority-based, etc.)

   - **Ranking**: Sorts results by final scores and assigns rank positions

   - **Content Formatting**: Generates content snippets and highlights matching terms

## Configuration

### INDEX_SCHEMA

Defines the structure of your search index:

```python

INDEX_SCHEMA = {

    # Text fields that will be searchable (defaults to ["title", "content"])

    "text_fields": ["title", "content"],

    # Metadata fields stored alongside text content for filtering

    "metadata_fields": ["project", "owner", "status", "priority"],

    # FTS5 tokenizer configuration

    "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_@.'"

}

```

### INDEXABLE_DOCTYPES

Specifies which doctypes to index and how to map their fields:

```python

INDEXABLE_DOCTYPES = {

    "Task": {

        # Field mapping

        "fields": [

            "name",

            {"title": "subject"},        # Maps subject field to title

            {"content": "description"},  # Maps description field to content

            {"modified": "creation"},    # Use creation instead of modified for recency boost

            "project",

            "owner"

        ],

        # Optional filters to limit which records are indexed

        "filters": {

            "status": ("!=", "Cancelled"),

            "docstatus": ("!=", 2)

        }

    }

}

```

### Field Mapping Rules

- **String fields**: Direct mapping `"field_name"`

- **Aliased fields**: Dictionary mapping `{"schema_field": "doctype_field"}`

- **Required fields**: `title` and `content` fields must be present or explicitly mapped (e.g., `{"title": "subject"}`)

- **Auto-added fields**: `doctype` and `name` are automatically included

- **Modified field**: Added automatically if used in any doctype configuration. Used for recency boosting - if you want to use a different timestamp field (like `creation` or `last_updated`), map it to `modified` using `{"modified": "creation"}`

## Features &amp; Customization

### Permission Filtering

Implement `get_search_filters()` to control access:

```python

def get_search_filters(self):

    """Return filters based on user permissions"""

    user = frappe.session.user

    if user == "Administrator":

        return {}  # No restrictions

    # Example: User can only see their own and public documents

    return {

        "owner": user,

        "status": ["Active", "Published"]

    }

```

### Custom Scoring

Create custom scoring functions to influence search relevance:

```python

class MyAppSearch(SQLiteSearch):

    ...

    @SQLiteSearch.scoring_function

    def *get*priority_boost(self, row, query, query_words):

        """Boost high-priority items"""

        priority = row.get("priority", "Medium")

        if priority == "High":

            return 1.5

        if priority == "Medium":

            return 1.1

        return 1.0

```

### Recency Boosting

The framework automatically provides time-based recency boosting using the `modified` field:

```python

# The modified field is used for calculating document age

# Recent documents get higher scores:

# - Last 24 hours: 1.8x boost

# - Last 7 days: 1.5x boost

# - Last 30 days: 1.2x boost

# - Last 90 days: 1.1x boost

# - Older documents: gradually decreasing boost

# If your doctype uses a different timestamp field, map it to modified:

INDEXABLE_DOCTYPES = {

    "GP Discussion": {

        "fields": ["name", "title", "content", {"modified": "last_post_at"}, "project"],

    },

    "Article": {

        "fields": ["name", "title", "content", {"modified": "published_date"}, "category"],

    }

}

```

### Document Preparation

Override `prepare_document()` for custom document processing:

```python

def prepare_document(self, doc):

    """Custom document preparation"""

    document = super().prepare_document(doc)

    if not document:

        return None

    # Add computed fields

    if doc.doctype == "Task":

        # Combine multiple fields into content

        content_parts = [

            doc.description or "",

            doc.notes or "",

            "\n".join([comment.content for comment in doc.get("comments", [])])

        ]

        document["content"] = "\n".join(filter(None, content_parts))

        # set fields that might be stored in another table

        document["category"] = get_category_for_task(doc)

    return document

```

### Spelling Correction

The framework includes built-in spelling correction using trigram similarity:

```python

# Spelling correction happens automatically

search_result = search.search("projetc managment")  # Will find "project management"

# Access correction information

print(search_result["summary"]["corrected_words"])

# Output: {"projetc": "project", "managment": "management"}

```

### Content Processing

HTML content is automatically cleaned and processed using BeautifulSoup:

```python

# Complex HTML content like this:

html_content = """

<div class="article">

    <h1>API Documentation</h1>

    <p>Learn how to integrate with our <a href="/api">REST API</a>.</p>

    [Screenshot on the live page]

    <ul>

        <li><strong>Authentication:</strong> Use <code>Bearer tokens</code></li>

        <li>Rate limiting: <em>1000 requests/hour</em></li>

    </ul>

    <blockquote>See our <a href="/examples">code examples</a> for details.</blockquote>

    <table><tbody><tr><td>Method</td><td>POST</td></tr></tbody></table>

    <script>analytics.track('page_view');</script>

    <style>.hidden { display: none; }</style>

</div>

"""

# Is automatically converted to clean, searchable plain text:

"""

API Documentation

Learn how to integrate with our REST API.

Authentication: Use Bearer tokens

Rate limiting: 1000 requests/hour

See our code examples for details.

Method POST

"""

# The cleaning process:

# 1. Removes all HTML tags (<div>, <h1>, <strong>, <code>, etc.)

# 2. Strips out scripts, styles, and non-content elements

# 3. Extracts link text while removing href URLs

# 4. Normalizes whitespace and line breaks

```

### Title-Only Search

```python

results = search.search("project update", title_only=True)

```

### Advanced Filtering

```python

accessible_projects = ['PROJ001', 'PROJ002', ...]

filters = {

    "project": accessible_projects,     # Multiple values (IN clause)

    "owner": current_user,              # Single value (= clause)

}

results = search.search("bug fix", filters=filters)

```

### Automatic Index Handling

The framework handles index building and maintenance automatically when you register your search class:

```python

# hooks.py

sqlite_search = ['my_app.search.MyAppSearch']

```

**What the framework does automatically:**

1. **Post-Migration Index Building**: Builds the search index automatically after running `bench migrate`

2. **Periodic Index Verification**: Checks every 15 minutes that the index exists and rebuilds if missing

3. **Real-time Document Updates**: Automatically calls `index_doc()` and `remove_doc()` on document lifecycle events (insert, update, delete) for all doctypes defined in your `INDEXABLE_DOCTYPES`

### Manual Index Handling

If you prefer to have manual control over the lifecycle of indexing, then you can simply opt out of automatic index handling by not registering the search class in `sqlite_search` hook.

```python

from my_app.search import MyAppSearch

def build_index_in_background():

    """Manually trigger background index building"""

    search = MyAppSearch()

    if search.is_search_enabled() and not search.index_exists():

        frappe.enqueue("my_app.search.build_index", queue="long")

# hooks.py

scheduler_events = {

    # Custom scheduler (if you want different timing)

    "daily": ["my_app.search.build_index_if_not_exists"],

}

```

## API Reference

#### `search(query, title_only=False, filters=None)`

Main search method that returns formatted results.

**Parameters:**

- `query` (str): Search query text

- `title_only` (bool): Search only in title fields

- `filters` (dict): Additional filters to apply

**Returns:**

```python

{

    "results": [

        {

            "doctype": "Task",

            "name": "TASK-001",

            "title": "Fix login bug",

            "content": "User cannot login after password reset...",

            "score": 0.85,

            "original_rank": 3, # original bm25 rank

            "rank": 1, # modified rank after custom scoring pipeline

            # ... other metadata fields

        }

    ],

    "summary": {

        "duration": 0.023,

        "total_matches": 15,

        "returned_matches": 15,

        "corrected_words": {"loggin": "login"},

        "corrected_query": "Fix login bug",

        "title_only": False,

        "filtered_matches": 15,

        "applied_filters": {"status": ["Open"]}

    }

}

```

#### `build_index()`

Build the complete search index from scratch.

#### `index_doc(doctype, docname)`

Index a single document.

#### `remove_doc(doctype, docname)`

Remove a single document from the index.

#### `is_search_enabled()`

Check if search is enabled (override to add disable logic).

#### `index_exists()`

Check if the search index exists.

#### `get_search_filters()`

**Must be implemented by subclasses.** Return filters for the current user.

**Returns:**

```python

{

    "field_name": "value",           # Single value

    "field_name": ["val1", "val2"],  # Multiple values

}

```

#### `scoring_function()`

Use the `@SQLiteSearch.scoring_function` decorator to mark a function as a scoring function.

<!-- page: framework/framework__user__en__api.md -->
---
title: "Developer API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api"
updated: "2026-02-17"
---

## Python

Frappe aims to achieve minimum cognitive load for its users. Hence, you can find
the most used methods and utilities in the `frappe` namespace itself. It's the
only import you need (most of the time) in a Python file.

1. [Document](/framework/user/en/api/document)
2. [Database](/framework/user/en/api/database)
3. [Jinja](/framework/user/en/api/jinja)
4. [Common Utilities](/framework/user/en/api/utils)
5. [Router](/framework/user/en/python-api/routing-and-rendering)
6. [Response](/framework/user/en/python-api/response)
7. [Language Resolution](/framework/v14/user/en/python-api/language)
8. [Search](/framework/user/en/python-api/search)
9. [Hooks](/framework/user/en/python-api/hooks)
10. [REST API](/framework/user/en/api/rest)
11. [Full Text Search](/framework/user/en/api/full-text-search)
12. [Dialog API](/framework/user/en/api/py-dialog)
13. [Query Builder](/framework/user/en/api/query-builder)

## Javascript

Frappe attaches itself to the `window` object under the `frappe` namespace. You
will find most of the Client API under the `frappe` object. All of these methods
are only available inside the Desk. A good way to explore these APIs is from the
browser console.

1. [Form](/framework/user/en/api/form)
2. [Controls](/framework/user/en/api/controls)
3. [Page](/framework/user/en/api/page)
4. [Tree](/framework/user/en/api/tree)
5. [Server Calls (AJAX)](/framework/user/en/api/server-calls)
6. [Common Utilities](/framework/user/en/api/js-utils)
7. [Dialog API](/framework/user/en/api/dialog)
8. [Chart API](/framework/user/en/api/chart)
9. [Scanner API](/framework/user/en/api/scanner)

## Other

1. [REST API](/framework/user/en/api/rest)
2. [Jinja API](/framework/user/en/api/jinja)

<!-- page: framework/framework__user__en__api__background_jobs.md -->
---
title: "Background Jobs"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/background_jobs"
updated: "2026-02-17"
---

Frappe ships with a system for running jobs in the background. It is implemented by using the [schedule package](https://pypi.org/project/schedule/) and a simple long-running infinite [while loop](https://github.com/frappe/frappe/blob/d0efa8e3ff734268a30b4804427641d2a5ed643e/frappe/utils/scheduler.py#L36-L46).

You can enqueue a python method to run in the background by using the `frappe.enqueue` method:


```
def long_running_job(param1, param2):
    # expensive tasks
    pass

# directly pass the function
frappe.enqueue(long_running_job, queue='short', param1='A', param2='B')

# or pass the full module path as string
frappe.enqueue('app.module.folder.long_running_job', queue='short', param1='A', param2='B')
```
Here are all the possible arguments you can pass to the `enqueue`:


```
frappe.enqueue(
    method, # python function or a module path as string
    queue="default", # one of short, default, long
    timeout=None, # pass timeout manually
    is_async=True, # if this is True, method is run in worker
    now=False, # if this is True, method is run directly (not in a worker) 
    job_name=None, # specify a job name
    enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
    at_front=False, # put the job at the front of the queue
    **kwargs, # kwargs are passed to the method as arguments
)
```
You can also enqueue a [Document](https://frappeframework.com/docs/v14/user/en/api/document) method by using `frappe.enqueue_doc`:


```
frappe.enqueue_doc(
    doctype,
    name,
    "do_something", # name of the controller method
    queue="long",
    timeout=4000,
    param="value"
)
```
Queue
-----

There are 3 default queues that are configured with the framework: `short`, `default`, and `long`. Each queue has a default timeout as follows:

* short: 300 seconds
* default: 300 seconds
* long: 1500 seconds

You can also pass a custom timeout to the `enqueue` method.

### Custom Queues

You can add custom queues by configuring them in `[common_site_config.json](https://frappeframework.com/docs/v14/user/en/basics/site_config#common-site-config)`:


```
{
    ...
    "workers": {
        "myqueue": {
            "timeout": 5000, # queue timeout
            "background_workers": 4, # number of workers for this queue
        }   
    }
}
```
Workers
-------

By default Frappe sets up 3 worker types for consuming from each queue. The default configuration looks like this:


```
bench worker --queue short
bench worker --queue default
bench worker --queue long
```
In production these 3 worker processes are replicated to configured number of background workers to handle higher workloads.

NOTE: This way of mapping workers to single queue is just a convention and it's not necessary to follow it.

### Multi-queue consumption

You can specify more than one queue for workers to consume from by specifying a comma separate string of queue names.

Example: If you wanted to combine short and default workers and only use two types of workers instead of default configuration then you can modify your worker configuration like this:


```
bench worker --queue short,default
bench worker --queue long
```
NOTE: The examples shown here are for Procfile format but they can be applied to supervisor or systemd configurations easily too.

### Burst Mode using `--burst`


```
bench worker --queue short --burst
```
This command will spawn a tempoary worker that will start consuming short queue and quit once queue is empty. If you periodically need higher amount of workers then you can use your OS's crontab to setup burst workers at specific times.

Scheduler Events
----------------

You can use Scheduler Events for running tasks periodically in the background using the `scheduler_events` hook.

**app/hooks.py**


```
scheduler_events = {
    "hourly": [
        # will run hourly
        "app.scheduled_tasks.update_database_usage"
    ],
}
```
**app/scheduled_tasks.py**


```
def update_database_usage():
    pass
```

> After changing any scheduled events in hooks.py, you need to run bench migrate for changes to take effect.
> 
> 

### Available Events

* `hourly`, `daily`, `weekly`, and `monthly`

These events will trigger every hour, day, week, and month respectively.
* `hourly_long`, `daily_long`, `weekly_long`, `monthly_long`

Same as above but these jobs are run in the [long worker](https://frappeframework.com/docs/v14/user/en/basics/directory-structure#worker_long) suitable for long-running jobs.
* `all`

The `all` event is triggered every 4 minutes. This can be configured via the `scheduler_interval` key in [common_site_config.json](https://frappeframework.com/docs/v14/user/en/basics/sites#scheduler_tick_interval)
* `cron`

A valid cron string that can be parsed by [croniter](https://pypi.org/project/croniter/).

Usage Examples:


```
scheduler_events = {
    "daily": [
        "app.scheduled_tasks.manage_recurring_invoices"
    ],
    "daily_long": [
        "app.scheduled_tasks.take_backups_daily"
    ],
    "cron": {
        "15 18 * * *": [
            "app.scheduled_tasks.delete_all_barcodes_for_users"
        ],
        "*/6 * * * *": [
            "app.scheduled_tasks.collect_error_snapshots"
        ],
        "annual": [
            "app.scheduled_tasks.collect_error_snapshots"
        ]
    }
}
```


Configurable Scheduler Events
----------------

On scenarios that require a user configurable trigger interval, Create a `Scheduler Event` record and create a `Scheduled Job Type` entry against that record. This doesn't require `scheduler_event` hook.

Example:
```
# Create `Scheduler Event` record
sch_eve = frappe.new_doc("Scheduler Event")
sch_eve.scheduled_against = "Process Payment Reconciliation"
sch_eve.save()

# Create `Scheduled Job Type`
job = frappe.new_doc("Scheduled Job Type")
job.frequency = "Cron"
job.scheduler_event = sch_eve.name
job.cron_format = "0/5 * * * *"     # runs every five minutes
job.save()
```

The `Scheduled Job Type`s trigger interval can be modified later, which persits across bench migration.

> The jobs triggered by scheduler are run by **Administrator** user. This also means any docs you create via scheduled job will be owned by the **Administrator** user unless specified otherwise.
> 
> 
