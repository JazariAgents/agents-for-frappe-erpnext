# Capabilities — Build a Frappe app from scratch

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `app.create` | Create a new Frappe app | bench | no | reversible | `docs/framework/framework__user__en__tutorial__create-an-app.md` | https://docs.frappe.io/framework/user/en/tutorial/create-an-app |
| `app.site.create` | Create a new site for an app | bench | no | reversible | `docs/framework/framework__user__en__tutorial__create-a-site.md` | https://docs.frappe.io/framework/user/en/tutorial/create-a-site |
| `doctype.create` | Create a DocType | browser | no | reversible | `docs/framework/framework__user__en__tutorial__create-a-doctype.md` | https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype |
| `doctype.features` | Turn on DocType features | browser | no | reversible | `docs/framework/framework__user__en__tutorial__doctype-features.md` | https://docs.frappe.io/framework/user/en/tutorial/doctype-features |
| `doctype.types` | Choose the right kind of DocType | guide | no | reversible | `docs/framework/framework__user__en__tutorial__types-of-doctype.md` | https://docs.frappe.io/framework/user/en/tutorial/types-of-doctype |
| `doctype.fieldtypes` | Pick the right field type | browser | no | reversible | `docs/framework/framework__user__en__basics__doctypes__fieldtypes.md` | https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes |
| `doctype.naming` | Set how documents are named | browser | no | reversible | `docs/framework/framework__user__en__basics__doctypes__naming.md` | https://docs.frappe.io/framework/user/en/basics/doctypes/naming |
| `doctype.controller` | Write controller methods | guide | no | reversible | `docs/framework/framework__user__en__tutorial__controller-methods.md` | https://docs.frappe.io/framework/user/en/tutorial/controller-methods |
| `doctype.formscript` | Add a form script | guide | no | reversible | `docs/framework/framework__user__en__tutorial__form-scripts.md` | https://docs.frappe.io/framework/user/en/tutorial/form-scripts |
| `doctype.child` | Use a child table | browser | no | reversible | `docs/framework/framework__user__en__basics__doctypes__child-doctype.md` | https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype |
| `doctype.virtual` | Use virtual doc fields | guide | no | reversible | `docs/framework/framework__user__en__basics__virtual_docfield.md` | https://docs.frappe.io/framework/user/en/basics/virtual_docfield |
| `app.hooks` | Wire app behaviour with hooks | guide | no | reversible | `docs/framework/framework__user__en__python-api__hooks.md` | https://docs.frappe.io/framework/user/en/python-api/hooks |
| `app.database.api` | Query data with the database API | guide | no | reversible | `docs/framework/framework__user__en__api__database.md` | https://docs.frappe.io/framework/user/en/api/database |
| `app.document.api` | Work with documents in Python | guide | no | reversible | `docs/framework/framework__user__en__api__document.md` | https://docs.frappe.io/framework/user/en/api/document |
| `app.querybuilder` | Build safe queries with the query builder | guide | no | reversible | `docs/framework/framework__user__en__api__query-builder.md` | https://docs.frappe.io/framework/user/en/api/query-builder |
| `app.jinja` | Render templates with the Jinja API | guide | no | reversible | `docs/framework/framework__user__en__api__jinja.md` | https://docs.frappe.io/framework/user/en/api/jinja |
| `app.portal.pages` | Build portal and web pages | guide | no | reversible | `docs/framework/framework__user__en__portal-pages.md` | https://docs.frappe.io/framework/user/en/portal-pages |
| `app.webform` | Publish a web form | browser | no | reversible | `docs/framework/framework__user__en__web-form.md` | https://docs.frappe.io/framework/user/en/web-form |
| `app.testing` | Test an app before release | guide | no | reversible | `docs/framework/framework__user__en__testing.md` | https://docs.frappe.io/framework/user/en/testing |
| `app.architecture` | Understand the framework architecture | guide | no | reversible | `docs/framework/framework__user__en__basics__architecture.md` | https://docs.frappe.io/framework/user/en/basics/architecture |
| `app.directory` | Read an app's directory structure | guide | no | reversible | `docs/framework/framework__user__en__basics__directory-structure.md` | https://docs.frappe.io/framework/user/en/basics/directory-structure |
| `app.assets` | Bundle app assets | bench | no | reversible | `docs/framework/framework__user__en__basics__asset-bundling.md` | https://docs.frappe.io/framework/user/en/basics/asset-bundling |
| `setup.printformat` | Build a print format | browser | yes | reversible | `docs/erpnext/erpnext__print-format-builder.md` | https://docs.frappe.io/erpnext/print-format-builder |
| `setup.customfield` | Add a custom field | browser | yes | reversible | `docs/erpnext/erpnext__custom-field.md` | https://docs.frappe.io/erpnext/custom-field |
| `setup.customizeform` | Customize a form | browser | yes | reversible | `docs/erpnext/erpnext__customize-form.md` | https://docs.frappe.io/erpnext/customize-form |
| `setup.clientscript` | Add a client script | browser | yes | reversible | `docs/erpnext/erpnext__client-scripts.md` | https://docs.frappe.io/erpnext/client-scripts |
| `setup.workflow` | Set up an approval workflow | browser | yes | reversible | `docs/erpnext/erpnext__workflow.md` | https://docs.frappe.io/erpnext/workflow |
| `app.studio` | Design an app screen in Frappe Studio | browser | yes | reversible | `docs/studio/studio__editor-interface.md` | https://docs.frappe.io/studio/editor-interface |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

