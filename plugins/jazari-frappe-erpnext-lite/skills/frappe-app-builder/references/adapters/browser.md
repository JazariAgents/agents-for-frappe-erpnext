# Interface adapter — Build a Frappe app from scratch

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |
| `https://your-site/studio` | Frappe Studio |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Create a DocType
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > DocType**, or type *DocType* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__tutorial__create-a-doctype.md`  (https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype)
- **Also read:** `docs/framework/framework__user__en__basics__doctypes.md` — the step-by-step page for this

### Turn on DocType features
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > DocType**, or type *DocType* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__tutorial__doctype-features.md`  (https://docs.frappe.io/framework/user/en/tutorial/doctype-features)

### Pick the right field type
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > DocType**, or type *DocType* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__basics__doctypes__fieldtypes.md`  (https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes)

### Set how documents are named
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > DocType**, or type *DocType* in the search bar at the top
- **On this screen:** Naming is set on the DocType form; rules that apply to existing DocTypes are **Document Naming Rule** records.
- **Documented steps:**
  1. Document Type it is being applied on
  2. Priority of the rule (rules with higher priority will be applied first)
  3. Conditions to apply the rule
- **Full page, bundled offline:** `docs/framework/framework__user__en__basics__doctypes__naming.md`  (https://docs.frappe.io/framework/user/en/basics/doctypes/naming)

### Use a child table
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > DocType**, or type *DocType* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__basics__doctypes__child-doctype.md`  (https://docs.frappe.io/framework/user/en/basics/doctypes/child-doctype)

### Publish a web form
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Website > Web Form**, or type *Web Form* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__web-form.md`  (https://docs.frappe.io/framework/user/en/web-form)

### Build a print format
- **Path (checked on v16.55):** https://your-site/desk → type *Print Format Builder* in the search bar at the top and open the page
- **Documented steps:**
  1. Go to the Print Format Builder
- **PDF engine:** how the format comes out as a PDF depends on **Print Settings → PDF Generator** (`wkhtmltopdf`, `chrome` or `PlutoPrint`). Sites created on Frappe 16.55 or later start on `chrome`. Check a real PDF, not only the screen preview, before calling a format finished.
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__print-format-builder.md`  (https://docs.frappe.io/erpnext/print-format-builder)

### Add a custom field
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > Customization > Custom Field**, or type *Custom Field* in the search bar at the top
- **Record type:** Custom Field
- **Documented steps:**
  1. Go to the Custom Field list and click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__custom-field.md`  (https://docs.frappe.io/erpnext/custom-field)

### Customize a form
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > Customization > Customize Form**, or type *Customize Form* in the search bar at the top
- **Documented steps:**
  1. Click on Customize Form
  2. You will be redirected to a page wherein you will be asked to Enter Form Type
  3. Once you enter the Form Type in this field, the page further expands and you will be able to see multiple features
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__customize-form.md`  (https://docs.frappe.io/erpnext/customize-form)

### Add a client script
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > Scripting > Client Script**, or type *Client Script* in the search bar at the top
- **Documented steps:**
  1. Go to Custom Script List and click on New
  2. You will be redirected to a page wherein you will be asked to enter the DocType for which you wish to create a Custom Script
  3. Type your Custom Script and make sure it is enabled
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__client-scripts.md`  (https://docs.frappe.io/erpnext/client-scripts)

### Set up an approval workflow
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Workflow > Workflow**, or type *Workflow* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__workflow.md`  (https://docs.frappe.io/erpnext/workflow)
- **Also read:** `docs/erpnext/erpnext__easy-steps-to-setup-workflow.md` — the step-by-step page for this
- **Also read:** `docs/erpnext/erpnext__workflows.md` — the step-by-step page for this

### Design an app screen in Frappe Studio
- **Path:** open https://your-site/studio (Frappe Studio) and find *Editor Interface* — the documentation page below shows the screen
- **Not checked on a live site:** the Studio app was not on the test site; this path is the documentation's.
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/studio/studio__editor-interface.md`  (https://docs.frappe.io/studio/editor-interface)

## What cannot be done in the interface

- Create a new Frappe app — runs on the server (bench.md)
- Create a new site for an app — runs on the server (bench.md)
- Choose the right kind of DocType — an explanation, not an action (guide.md)
- Write controller methods — an explanation, not an action (guide.md)
- Add a form script — an explanation, not an action (guide.md)
- Use virtual doc fields — an explanation, not an action (guide.md)
- Wire app behaviour with hooks — an explanation, not an action (guide.md)
- Query data with the database API — an explanation, not an action (guide.md)
- Work with documents in Python — an explanation, not an action (guide.md)
- Build safe queries with the query builder — an explanation, not an action (guide.md)
- Render templates with the Jinja API — an explanation, not an action (guide.md)
- Build portal and web pages — an explanation, not an action (guide.md)
- Test an app before release — an explanation, not an action (guide.md)
- Understand the framework architecture — an explanation, not an action (guide.md)
- Read an app's directory structure — an explanation, not an action (guide.md)
- Bundle app assets — runs on the server (bench.md)
