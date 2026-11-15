# Capabilities — Users, roles and permissions

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `perm.users` | Add and manage users | browser | no | reversible | `docs/framework/framework-10.md` lines 3–164 | https://docs.frappe.io/framework/user/en/basics/users-and-permissions |
| `perm.roles` | Set role-based permissions | browser | yes | reversible | `docs/erpnext/erpnext-51.md` lines 552–625 | https://docs.frappe.io/erpnext/role-based-permissions |
| `perm.userperm` | Restrict a user to specific records | browser | yes | reversible | `docs/erpnext/erpnext-67.md` lines 141–246 | https://docs.frappe.io/erpnext/user-permissions |
| `perm.levels` | Hide fields with permission levels | browser | yes | reversible | `docs/erpnext/erpnext-42.md` lines 130–202 | https://docs.frappe.io/erpnext/perm-levels |
| `perm.types` | Understand permission types | guide | no | reversible | `docs/framework/framework-03.md` lines 363–440 | https://docs.frappe.io/framework/permission-types |
| `perm.roleprofile` | Group roles into a role profile | browser | yes | reversible | `docs/erpnext/erpnext-51.md` lines 510–550 | https://docs.frappe.io/erpnext/role-and-role-profile |
| `perm.2fa` | Turn on two-factor authentication | browser | yes | reversible | `docs/erpnext/erpnext-57.md` lines 610–665 | https://docs.frappe.io/erpnext/setup-two-factor-authentication |
| `perm.audit` | Read the audit trail | browser | no | reversible | `docs/framework/framework-07.md` lines 550–591 | https://docs.frappe.io/framework/user/en/audit-trail |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

