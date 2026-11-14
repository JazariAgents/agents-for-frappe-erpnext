# Capabilities — Users, roles and permissions

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `perm.users` | Add and manage users | browser | no | reversible | `docs/framework/framework__user__en__basics__users-and-permissions.md` | https://docs.frappe.io/framework/user/en/basics/users-and-permissions |
| `perm.roles` | Set role-based permissions | browser | yes | reversible | `docs/erpnext/erpnext__role-based-permissions.md` | https://docs.frappe.io/erpnext/role-based-permissions |
| `perm.userperm` | Restrict a user to specific records | browser | yes | reversible | `docs/erpnext/erpnext__user-permissions.md` | https://docs.frappe.io/erpnext/user-permissions |
| `perm.levels` | Hide fields with permission levels | browser | yes | reversible | `docs/erpnext/erpnext__perm-levels.md` | https://docs.frappe.io/erpnext/perm-levels |
| `perm.types` | Understand permission types | guide | no | reversible | `docs/framework/framework__permission-types.md` | https://docs.frappe.io/framework/permission-types |
| `perm.roleprofile` | Group roles into a role profile | browser | yes | reversible | `docs/erpnext/erpnext__role-and-role-profile.md` | https://docs.frappe.io/erpnext/role-and-role-profile |
| `perm.2fa` | Turn on two-factor authentication | browser | yes | reversible | `docs/erpnext/erpnext__setup-two-factor-authentication.md` | https://docs.frappe.io/erpnext/setup-two-factor-authentication |
| `perm.audit` | Read the audit trail | browser | no | reversible | `docs/framework/framework__user__en__audit-trail.md` | https://docs.frappe.io/framework/user/en/audit-trail |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

