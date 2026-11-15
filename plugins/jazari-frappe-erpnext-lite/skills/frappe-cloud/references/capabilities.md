# Capabilities — Frappe Cloud — sites, benches, servers

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `cloud.site.create` | Create a site on Frappe Cloud | browser | no | reversible | `docs/cloud/cloud-02.md` lines 2983–3009 | https://docs.frappe.io/cloud/sites/creating-a-new-site |
| `cloud.bench.create` | Create a bench group on Frappe Cloud | browser | no | reversible | `docs/cloud/cloud-01.md` lines 234–270 | https://docs.frappe.io/cloud/benches/create-new |
| `cloud.bench.concepts` | Understand benches and bench groups | guide | no | reversible | `docs/cloud/cloud-03.md` lines 552–603 | https://docs.frappe.io/cloud/what-are-benches-and-bench-groups |
| `cloud.bench.update` | Update a bench group | browser | yes | reversible | `docs/cloud/cloud-01.md` lines 709–834 | https://docs.frappe.io/cloud/benches/updating_a_bench |
| `cloud.app.custom` | Add a custom app to a bench | browser | yes | reversible | `docs/cloud/cloud-01.md` lines 272–301 | https://docs.frappe.io/cloud/benches/custom-app |
| `cloud.server.new` | Create a server | browser | no | reversible | `docs/cloud/cloud-02.md` lines 1833–1921 | https://docs.frappe.io/cloud/servers/new |
| `cloud.site.backup` | Back up a Frappe Cloud site | browser | no | reversible | `docs/cloud/cloud-02.md` lines 2833–2952 | https://docs.frappe.io/cloud/sites/backups |
| `cloud.site.migrate` | Move a site between benches or servers | browser | yes | reversible | `docs/cloud/cloud-02.md` lines 2769–2814 | https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench |
| `cloud.domain` | Add a custom domain to a Frappe Cloud site | browser | yes | reversible | `docs/cloud/cloud-02.md` lines 3011–3224 | https://docs.frappe.io/cloud/sites/custom-domains |
| `cloud.billing` | Manage billing and payments | browser | yes | irreversible | `docs/cloud/cloud-01.md` lines 873–934 | https://docs.frappe.io/cloud/billing/bill-payments |
| `cloud.ssh` | Connect to a bench over SSH | browser | no | reversible | `docs/cloud/cloud-01.md` lines 467–707 | https://docs.frappe.io/cloud/benches/ssh |
| `cloud.marketplace` | Install a marketplace app | browser | yes | reversible | `docs/cloud/cloud-01.md` lines 4240–4298 | https://docs.frappe.io/cloud/installing-an-app |
| `cloud.publishapp` | Publish an app to the marketplace | browser | yes | reversible | `docs/cloud/cloud-02.md` lines 649–711 | https://docs.frappe.io/cloud/marketplace/publishing-an-app-to-marketplace |
| `cloud.siteplan` | Change a site plan | browser | yes | reversible | `docs/cloud/cloud-01.md` lines 4069–4080 | https://docs.frappe.io/cloud/how-to-change-a-site-plan |
| `cloud.serverscript` | Enable server scripts on a site | browser | yes | reversible | `docs/cloud/cloud-01.md` lines 2807–2824 | https://docs.frappe.io/cloud/enable-server-script |
| `cloud.logs` | Read site and bench logs | browser | no | reversible | `docs/cloud/cloud-02.md` lines 415–445 | https://docs.frappe.io/cloud/logs |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

