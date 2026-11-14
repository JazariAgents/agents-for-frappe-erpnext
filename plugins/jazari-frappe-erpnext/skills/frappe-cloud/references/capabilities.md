# Capabilities — Frappe Cloud — sites, benches, servers

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `cloud.site.create` | Create a site on Frappe Cloud | browser | no | reversible | `docs/cloud/cloud__sites__creating-a-new-site.md` | https://docs.frappe.io/cloud/sites/creating-a-new-site |
| `cloud.bench.create` | Create a bench group on Frappe Cloud | browser | no | reversible | `docs/cloud/cloud__benches__create-new.md` | https://docs.frappe.io/cloud/benches/create-new |
| `cloud.bench.concepts` | Understand benches and bench groups | guide | no | reversible | `docs/cloud/cloud__what-are-benches-and-bench-groups.md` | https://docs.frappe.io/cloud/what-are-benches-and-bench-groups |
| `cloud.bench.update` | Update a bench group | browser | yes | reversible | `docs/cloud/cloud__benches__updating_a_bench.md` | https://docs.frappe.io/cloud/benches/updating_a_bench |
| `cloud.app.custom` | Add a custom app to a bench | browser | yes | reversible | `docs/cloud/cloud__benches__custom-app.md` | https://docs.frappe.io/cloud/benches/custom-app |
| `cloud.server.new` | Create a server | browser | no | reversible | `docs/cloud/cloud__servers__new.md` | https://docs.frappe.io/cloud/servers/new |
| `cloud.site.backup` | Back up a Frappe Cloud site | browser | no | reversible | `docs/cloud/cloud__sites__backups.md` | https://docs.frappe.io/cloud/sites/backups |
| `cloud.site.migrate` | Move a site between benches or servers | browser | yes | reversible | `docs/cloud/cloud__site__site-migrations__move-site-to-different-server-or-bench.md` | https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench |
| `cloud.domain` | Add a custom domain to a Frappe Cloud site | browser | yes | reversible | `docs/cloud/cloud__sites__custom-domains.md` | https://docs.frappe.io/cloud/sites/custom-domains |
| `cloud.billing` | Manage billing and payments | browser | yes | irreversible | `docs/cloud/cloud__billing__bill-payments.md` | https://docs.frappe.io/cloud/billing/bill-payments |
| `cloud.ssh` | Connect to a bench over SSH | browser | no | reversible | `docs/cloud/cloud__benches__ssh.md` | https://docs.frappe.io/cloud/benches/ssh |
| `cloud.marketplace` | Install a marketplace app | browser | yes | reversible | `docs/cloud/cloud__installing-an-app.md` | https://docs.frappe.io/cloud/installing-an-app |
| `cloud.publishapp` | Publish an app to the marketplace | browser | yes | reversible | `docs/cloud/cloud__marketplace__publishing-an-app-to-marketplace.md` | https://docs.frappe.io/cloud/marketplace/publishing-an-app-to-marketplace |
| `cloud.siteplan` | Change a site plan | browser | yes | reversible | `docs/cloud/cloud__how-to-change-a-site-plan.md` | https://docs.frappe.io/cloud/how-to-change-a-site-plan |
| `cloud.serverscript` | Enable server scripts on a site | browser | yes | reversible | `docs/cloud/cloud__enable-server-script.md` | https://docs.frappe.io/cloud/enable-server-script |
| `cloud.logs` | Read site and bench logs | browser | no | reversible | `docs/cloud/cloud__logs.md` | https://docs.frappe.io/cloud/logs |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

