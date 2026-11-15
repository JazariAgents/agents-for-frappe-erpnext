# Guide adapter — Build a Frappe app from scratch

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Choose the right kind of DocType
- **What the page says:** Let's learn about the different types of doctype in the framework by creating more doctypes.
- **It covers:** Library Membership, Linked DocTypes, Submittable DocTypes, Controller Validation for Membership, Library Transaction, Validation for Transaction, Library Settings, Single DocTypes
- **Documented detail:**
  1. Article - Link to Article
  2. Library Member - Link to Library Member
  3. Type - Select with 2 options: Issue and Return
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-06.md` lines 3587–3907  (https://docs.frappe.io/framework/user/en/tutorial/types-of-doctype)

### Write controller methods
- **What the page says:** Controller methods allow you to write business logic during the lifecycle of a document.
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-06.md` lines 2754–2807  (https://docs.frappe.io/framework/user/en/tutorial/controller-methods)

### Add a form script
- **What the page says:** Form Scripts are client-side javascript code that enhances the UX of your Forms.
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-06.md` lines 3369–3416  (https://docs.frappe.io/framework/user/en/tutorial/form-scripts)

### Use virtual doc fields
- **What the page says:** A Virtual DocField is a dynamic attribute of a given Document (or Record). It's a calculated attribute that isn't stored in the site database. This could be used for representing values that may be functions of other static Document attributes.
- **It covers:** How to use Virtual DocFields, 1. Define a Virtual DocField, 2. Define a source for the field, Impact on internals, Backend API, REST API, Database, Virtual Tables on Non-virtual DocTypes
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-03.md` lines 741–859  (https://docs.frappe.io/framework/user/en/basics/virtual_docfield)

### Wire app behaviour with hooks
- **What the page says:** Hooks allow you to "hook" into functionality and events of core parts of the Frappe Framework. This page documents all of the hooks provided by the framework.
- **It covers:** How does hooks work?, How are conflicting hooks resolved?, App Meta Data, Javascript / CSS Assets, Desk, Portal, Web Form, Page
- **Documented detail:**
  1. app_name - slugified name of the app
  2. app_title - presentable app name
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-06.md` lines 3–1740  (https://docs.frappe.io/framework/user/en/python-api/hooks)

### Query data with the database API
- **What the page says:** `frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length, run)`
- **It covers:** frappe.db.get_list, frappe.db.get_all, frappe.db.get_value, frappe.db.getsinglevalue, frappe.db.set_value, frappe.db.exists, frappe.db.count, frappe.db.delete
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-01.md` lines 4260–4717  (https://docs.frappe.io/framework/user/en/api/database)

### Work with documents in Python
- **What the page says:** A Document is an instance of a DocType. It is derived from the `frappe.model.Document` class and represents a single record in the database table.
- **It covers:** frappe.get_doc, frappe.get_last_doc, frappe.get_cached_doc, frappe.new_doc, frappe.delete_doc, frappe.rename_doc, frappe.get_meta, frappe.only_for
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-02.md` lines 3–480  (https://docs.frappe.io/framework/user/en/api/document)

### Build safe queries with the query builder
- **What the page says:** `frappe.qb` is a query builder written around PyPika to build a single interface for cross-db queries
- **It covers:** frappe.qb, frappe.qb.from_(doctype), frappe.qb.Doctype(name_of_table), frappe.qb.Table(name_of_table), frappe.qb.Field(name_of_coloum), Executing queries, Walk method, Run method
- **Documented detail:**
  1. Read JSON object values by path
  2. Read scalar/text values for filtering
  3. Check whether JSON object/array contains a value
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-02.md` lines 2187–2566  (https://docs.frappe.io/framework/user/en/api/query-builder)

### Render templates with the Jinja API
- **What the page says:** These are the whitelisted methods that frappe provides to use them in Jinja Templates.
- **It covers:** frappe.format, frappe.format_date, frappe.get_url, frappe.get_doc, frappe.get_all, {{ task.title }}, Redesign Website, Add meta tags on websites
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-02.md` lines 1136–1430  (https://docs.frappe.io/framework/user/en/api/jinja)

### Build portal and web pages
- **What the page says:** Frappe Framework not only provides a rich admin interface via the [Desk](/framework/v14/user/en/desk) which is an SPA but also static server rendered web pages. These pages are generally built for your website visitors. They can be public or can require login.
- **It covers:** Adding pages, Overriding standard pages, Templating, Context, Custom CSS and JS, Home Page, {{ _("About Us") }}, {{ _("About Us") }}
- **Documented detail:**
  1. Portal Settings (this will be for logged in users)
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-05.md` lines 3229–3512  (https://docs.frappe.io/framework/user/en/portal-pages)

### Test an app before release
- **What the page says:** Frappe provides some basic tooling to write automated tests. There are some basic rules:
- **It covers:** Writing Tests, Writing Tests for Commands, Running Tests, Checking if Tests are Running, Running Tests Parallelly, Parallel Tests, Parallel tests with orchestrator, Comparison
- **Documented detail:**
  1. The test runner will automatically build test records for dependent DocTypes
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-06.md` lines 2208–2485  (https://docs.frappe.io/framework/user/en/testing)

### Understand the framework architecture
- **What the page says:** Frappe Framework is a full-stack web based framework and it includes all the tools needed to deploy a site into production. Database, caching, background jobs, realtime notifications, etc are all configured when you set up a Frappe site.
- **Documented detail:**
  1. Create a directory called frappe-bench and frappe-bench/sites, frappe-bench/apps within it
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-02.md` lines 4643–4686  (https://docs.frappe.io/framework/user/en/basics/architecture)

### Read an app's directory structure
- **What the page says:** When you initialize a new **frappe-bench** directory, you will have a directory structure similar to:
- **It covers:** apps, sites, logs, config, env, Procfile
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-02.md` lines 4935–5052  (https://docs.frappe.io/framework/user/en/basics/directory-structure)

