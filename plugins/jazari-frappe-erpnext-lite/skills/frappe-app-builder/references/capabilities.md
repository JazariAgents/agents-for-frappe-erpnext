# Capabilities — Build a Frappe app from scratch

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `app.create` | Create a new Frappe app | bench | no | reversible | `docs/framework/framework-06.md` lines 3202–3298 | https://docs.frappe.io/framework/user/en/tutorial/create-an-app |
| `app.site.create` | Create a new site for an app | bench | no | reversible | `docs/framework/framework-06.md` lines 2985–3200 | https://docs.frappe.io/framework/user/en/tutorial/create-a-site |
| `doctype.create` | Create a DocType | browser | no | reversible | `docs/framework/framework-06.md` lines 2809–2983 | https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype |
| `doctype.features` | Turn on DocType features | browser | no | reversible | `docs/framework/framework-06.md` lines 3300–3367 | https://docs.frappe.io/framework/user/en/tutorial/doctype-features |
| `doctype.types` | Choose the right kind of DocType | guide | no | reversible | `docs/framework/framework-06.md` lines 3587–3907 | https://docs.frappe.io/framework/user/en/tutorial/types-of-doctype |
| `doctype.fieldtypes` | Pick the right field type | browser | no | reversible | `docs/framework/framework-02.md` lines 5645–5988 | https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes |
| `doctype.naming` | Set how documents are named | browser | no | reversible | `docs/framework/framework-02.md` lines 6075–6250 | https://docs.frappe.io/framework/user/en/basics/doctypes/naming |
| `doctype.controller` | Write controller methods | guide | no | reversible | `docs/framework/framework-06.md` lines 2754–2807 | https://docs.frappe.io/framework/user/en/tutorial/controller-methods |
| `doctype.formscript` | Add a form script | guide | no | reversible | `docs/framework/framework-06.md` lines 3369–3416 | https://docs.frappe.io/framework/user/en/tutorial/form-scripts |
| `doctype.child` | Use a child table | browser | no | reversible | `docs/framework/framework-02.md` lines 5249–5293 | https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype |
| `doctype.virtual` | Use virtual doc fields | guide | no | reversible | `docs/framework/framework-03.md` lines 741–859 | https://docs.frappe.io/framework/user/en/basics/virtual_docfield |
| `app.hooks` | Wire app behaviour with hooks | guide | no | reversible | `docs/framework/framework-06.md` lines 3–1740 | https://docs.frappe.io/framework/user/en/python-api/hooks |
| `app.database.api` | Query data with the database API | guide | no | reversible | `docs/framework/framework-01.md` lines 4260–4717 | https://docs.frappe.io/framework/user/en/api/database |
| `app.document.api` | Work with documents in Python | guide | no | reversible | `docs/framework/framework-02.md` lines 3–480 | https://docs.frappe.io/framework/user/en/api/document |
| `app.querybuilder` | Build safe queries with the query builder | guide | no | reversible | `docs/framework/framework-02.md` lines 2187–2566 | https://docs.frappe.io/framework/user/en/api/query-builder |
| `app.jinja` | Render templates with the Jinja API | guide | no | reversible | `docs/framework/framework-02.md` lines 1136–1430 | https://docs.frappe.io/framework/user/en/api/jinja |
| `app.portal.pages` | Build portal and web pages | guide | no | reversible | `docs/framework/framework-05.md` lines 3229–3512 | https://docs.frappe.io/framework/user/en/portal-pages |
| `app.webform` | Publish a web form | browser | no | reversible | `docs/framework/framework-06.md` lines 4277–4315 | https://docs.frappe.io/framework/user/en/web-form |
| `app.testing` | Test an app before release | guide | no | reversible | `docs/framework/framework-06.md` lines 2208–2485 | https://docs.frappe.io/framework/user/en/testing |
| `app.architecture` | Understand the framework architecture | guide | no | reversible | `docs/framework/framework-02.md` lines 4643–4686 | https://docs.frappe.io/framework/user/en/basics/architecture |
| `app.directory` | Read an app's directory structure | guide | no | reversible | `docs/framework/framework-02.md` lines 4935–5052 | https://docs.frappe.io/framework/user/en/basics/directory-structure |
| `app.assets` | Bundle app assets | bench | no | reversible | `docs/framework/framework-02.md` lines 4688–4933 | https://docs.frappe.io/framework/user/en/basics/asset-bundling |
| `setup.printformat` | Build a print format | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 2840–2900 | https://docs.frappe.io/erpnext/print-format-builder |
| `setup.customfield` | Add a custom field | browser | yes | reversible | `docs/erpnext/erpnext-05.md` lines 274–360 | https://docs.frappe.io/erpnext/custom-field |
| `setup.customizeform` | Customize a form | browser | yes | reversible | `docs/erpnext/erpnext-05.md` lines 1175–1277 | https://docs.frappe.io/erpnext/customize-form |
| `setup.clientscript` | Add a client script | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 951–984 | https://docs.frappe.io/erpnext/client-scripts |
| `setup.workflow` | Set up an approval workflow | browser | yes | reversible | `docs/erpnext/erpnext-18.md` lines 1906–1921 | https://docs.frappe.io/erpnext/workflow |
| `app.studio` | Design an app screen in Frappe Studio | browser | yes | reversible | `docs/studio/studio-01.md` lines 3–71 | https://docs.frappe.io/studio/editor-interface |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

