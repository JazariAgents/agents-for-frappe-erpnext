# Capabilities — Build a Frappe app from scratch

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `app.create` | Create a new Frappe app | bench | no | reversible | `docs/framework/framework-23.md` lines 396–492 | https://docs.frappe.io/framework/user/en/tutorial/create-an-app |
| `app.site.create` | Create a new site for an app | bench | no | reversible | `docs/framework/framework-23.md` lines 179–394 | https://docs.frappe.io/framework/user/en/tutorial/create-a-site |
| `doctype.create` | Create a DocType | browser | no | reversible | `docs/framework/framework-23.md` lines 3–177 | https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype |
| `doctype.features` | Turn on DocType features | browser | no | reversible | `docs/framework/framework-23.md` lines 494–561 | https://docs.frappe.io/framework/user/en/tutorial/doctype-features |
| `doctype.types` | Choose the right kind of DocType | guide | no | reversible | `docs/framework/framework-23.md` lines 781–1101 | https://docs.frappe.io/framework/user/en/tutorial/types-of-doctype |
| `doctype.fieldtypes` | Pick the right field type | browser | no | reversible | `docs/framework/framework-08.md` lines 399–742 | https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes |
| `doctype.naming` | Set how documents are named | browser | no | reversible | `docs/framework/framework-08.md` lines 829–1004 | https://docs.frappe.io/framework/user/en/basics/doctypes/naming |
| `doctype.controller` | Write controller methods | guide | no | reversible | `docs/framework/framework-22.md` lines 1015–1068 | https://docs.frappe.io/framework/user/en/tutorial/controller-methods |
| `doctype.formscript` | Add a form script | guide | no | reversible | `docs/framework/framework-23.md` lines 563–610 | https://docs.frappe.io/framework/user/en/tutorial/form-scripts |
| `doctype.child` | Use a child table | browser | no | reversible | `docs/framework/framework-08.md` lines 3–47 | https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype |
| `doctype.virtual` | Use virtual doc fields | guide | no | reversible | `docs/framework/framework-10.md` lines 166–284 | https://docs.frappe.io/framework/user/en/basics/virtual_docfield |
| `app.hooks` | Wire app behaviour with hooks | guide | no | reversible | `docs/framework/framework-21.md` lines 3–1740 | https://docs.frappe.io/framework/user/en/python-api/hooks |
| `app.database.api` | Query data with the database API | guide | no | reversible | `docs/framework/framework-04.md` lines 378–835 | https://docs.frappe.io/framework/user/en/api/database |
| `app.document.api` | Work with documents in Python | guide | no | reversible | `docs/framework/framework-04.md` lines 1312–1789 | https://docs.frappe.io/framework/user/en/api/document |
| `app.querybuilder` | Build safe queries with the query builder | guide | no | reversible | `docs/framework/framework-06.md` lines 3–382 | https://docs.frappe.io/framework/user/en/api/query-builder |
| `app.jinja` | Render templates with the Jinja API | guide | no | reversible | `docs/framework/framework-05.md` lines 657–951 | https://docs.frappe.io/framework/user/en/api/jinja |
| `app.portal.pages` | Build portal and web pages | guide | no | reversible | `docs/framework/framework-19.md` lines 607–890 | https://docs.frappe.io/framework/user/en/portal-pages |
| `app.webform` | Publish a web form | browser | no | reversible | `docs/framework/framework-24.md` lines 344–382 | https://docs.frappe.io/framework/user/en/web-form |
| `app.testing` | Test an app before release | guide | no | reversible | `docs/framework/framework-22.md` lines 469–746 | https://docs.frappe.io/framework/user/en/testing |
| `app.architecture` | Understand the framework architecture | guide | no | reversible | `docs/framework/framework-07.md` lines 934–977 | https://docs.frappe.io/framework/user/en/basics/architecture |
| `app.directory` | Read an app's directory structure | guide | no | reversible | `docs/framework/framework-07.md` lines 1226–1343 | https://docs.frappe.io/framework/user/en/basics/directory-structure |
| `app.assets` | Bundle app assets | bench | no | reversible | `docs/framework/framework-07.md` lines 979–1224 | https://docs.frappe.io/framework/user/en/basics/asset-bundling |
| `setup.printformat` | Build a print format | browser | yes | reversible | `docs/erpnext/erpnext-43.md` lines 811–871 | https://docs.frappe.io/erpnext/print-format-builder |
| `setup.customfield` | Add a custom field | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 3–89 | https://docs.frappe.io/erpnext/custom-field |
| `setup.customizeform` | Customize a form | browser | yes | reversible | `docs/erpnext/erpnext-18.md` lines 184–286 | https://docs.frappe.io/erpnext/customize-form |
| `setup.clientscript` | Add a client script | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 456–489 | https://docs.frappe.io/erpnext/client-scripts |
| `setup.workflow` | Set up an approval workflow | browser | yes | reversible | `docs/erpnext/erpnext-69.md` lines 536–551 | https://docs.frappe.io/erpnext/workflow |
| `app.studio` | Design an app screen in Frappe Studio | browser | yes | reversible | `docs/studio/studio-01.md` lines 3–71 | https://docs.frappe.io/studio/editor-interface |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

