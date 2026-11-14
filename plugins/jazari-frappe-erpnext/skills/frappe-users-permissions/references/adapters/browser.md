# Interface adapter — Users, roles and permissions

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

### Add and manage users
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Users**, or type *User* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__user__en__basics__users-and-permissions.md`  (https://docs.frappe.io/framework/user/en/basics/users-and-permissions)

### Set role-based permissions
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Users > Permissions > Role Permissions Manager**, or type *Role Permissions Manager* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__role-based-permissions.md`  (https://docs.frappe.io/erpnext/role-based-permissions)

### Restrict a user to specific records
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Access > User Permissions**, or type *User Permissions* in the search bar at the top
- **Record type:** User Permission
- **Documented steps:**
  1. Allowing user to access data belonging to one Company
  2. Allowing user to access data related to a specific Customer or Territory
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__user-permissions.md`  (https://docs.frappe.io/erpnext/user-permissions)

### Hide fields with permission levels
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Build > Customization > Customize Form**, or type *Customize Form* in the search bar at the top
- **Documented steps:**
  1. A field is assigned a perm level in the DocType or Customize Form
  2. Role Permission Manager is used to define what each role can do at each perm level
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__perm-levels.md`  (https://docs.frappe.io/erpnext/perm-levels)

### Group roles into a role profile
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Access > Role**, or type *Role* in the search bar at the top
- **Documented steps:**
  1. Go to the Role list, click on New
  2. Enter a name for the Role
  3. Choose whether the Role has desk access. A role that has desk access can access ERPNext modules and the company's documents. The level of access depends on the roles assigned to the user
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__role-and-role-profile.md`  (https://docs.frappe.io/erpnext/role-and-role-profile)

### Turn on two-factor authentication
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > System**, or type *System Settings* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__setup-two-factor-authentication.md`  (https://docs.frappe.io/erpnext/setup-two-factor-authentication)

### Read the audit trail
- **Path (checked on v16.55):** https://your-site/desk → type *Audit Trail* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Select the type of the document in the Doctype field
  2. Select the name of the document in the Document field
  3. Optionally, select the start and end dates in order to show the amended documents within the specified date range
  4. Click on the Compare button to view the Audit Trail for the selected document
- **Full page, bundled offline:** `docs/framework/framework__user__en__audit-trail.md`  (https://docs.frappe.io/framework/user/en/audit-trail)

## What cannot be done in the interface

- Understand permission types — an explanation, not an action (guide.md)
