# Capabilities — Users, roles and permissions

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `perm.users` | Add and manage users | browser | no | reversible | `docs/framework/framework-03.md` lines 578–739 | https://docs.frappe.io/framework/user/en/basics/users-and-permissions |
| `perm.roles` | Set role-based permissions | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 3285–3358 | https://docs.frappe.io/erpnext/role-based-permissions |
| `perm.userperm` | Restrict a user to specific records | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 2928–3033 | https://docs.frappe.io/erpnext/user-permissions |
| `perm.levels` | Hide fields with permission levels | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 1254–1326 | https://docs.frappe.io/erpnext/perm-levels |
| `perm.types` | Understand permission types | guide | no | reversible | `docs/framework/framework-01.md` lines 2738–2815 | https://docs.frappe.io/framework/permission-types |
| `perm.roleprofile` | Group roles into a role profile | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 3243–3283 | https://docs.frappe.io/erpnext/role-and-role-profile |
| `perm.2fa` | Turn on two-factor authentication | browser | yes | reversible | `docs/erpnext/erpnext-15.md` lines 1484–1539 | https://docs.frappe.io/erpnext/setup-two-factor-authentication |
| `perm.audit` | Read the audit trail | browser | no | reversible | `docs/framework/framework-02.md` lines 4259–4300 | https://docs.frappe.io/framework/user/en/audit-trail |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

