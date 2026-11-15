# Capabilities — Run bench — sites, apps, backups, deploys

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `bench.overview` | Understand bench and the bench directory | bench | no | reversible | `docs/framework/framework-10.md` lines 490–525 | https://docs.frappe.io/framework/user/en/bench |
| `bench.commands` | Run bench CLI commands | bench | no | reversible | `docs/framework/framework-10.md` lines 527–875 | https://docs.frappe.io/framework/user/en/bench/bench-commands |
| `bench.frappe.commands` | Run site-scoped framework commands | bench | no | reversible | `docs/framework/framework-11.md` lines 3–409 | https://docs.frappe.io/framework/user/en/bench/frappe-commands |
| `bench.newsite` | Create a site with bench new-site | bench | no | reversible | `docs/framework/framework-12.md` lines 366–463 | https://docs.frappe.io/framework/user/en/bench/reference/new-site |
| `bench.dropsite` | Drop a site | bench | yes | recreate | `docs/framework/framework-11.md` lines 1071–1123 | https://docs.frappe.io/framework/user/en/bench/reference/drop-site |
| `bench.backup` | Back up a site | bench | no | reversible | `docs/framework/framework-11.md` lines 887–984 | https://docs.frappe.io/framework/user/en/bench/reference/backup |
| `bench.restore` | Restore a site from a backup | bench | yes | irreversible | `docs/framework/framework-12.md` lines 564–659 | https://docs.frappe.io/framework/user/en/bench/reference/restore |
| `bench.partialrestore` | Restore selected tables only | bench | yes | irreversible | `docs/framework/framework-12.md` lines 465–506 | https://docs.frappe.io/framework/user/en/bench/reference/partial-restore |
| `bench.migrate` | Run migrations after an update | bench | yes | reversible | `docs/framework/framework-12.md` lines 306–364 | https://docs.frappe.io/framework/user/en/bench/reference/migrate |
| `bench.reinstall` | Reinstall a site from scratch | bench | yes | recreate | `docs/framework/framework-12.md` lines 508–562 | https://docs.frappe.io/framework/user/en/bench/reference/reinstall |
| `bench.listapps` | List the apps installed on a site | bench | no | reversible | `docs/framework/framework-12.md` lines 248–304 | https://docs.frappe.io/framework/user/en/bench/reference/list-apps |
| `bench.uninstallapp` | Uninstall an app from a site | bench | yes | recreate | `docs/framework/framework-12.md` lines 943–997 | https://docs.frappe.io/framework/user/en/bench/reference/uninstall-app |
| `bench.config` | Read and change site configuration | bench | yes | reversible | `docs/framework/framework-12.md` lines 661–724 | https://docs.frappe.io/framework/user/en/bench/reference/set-config |
| `bench.showconfig` | Show the current site configuration | bench | no | reversible | `docs/framework/framework-12.md` lines 726–775 | https://docs.frappe.io/framework/user/en/bench/reference/show-config |
| `bench.execute` | Execute a Python method on a site | bench | yes | irreversible | `docs/framework/framework-12.md` lines 3–246 | https://docs.frappe.io/framework/user/en/bench/reference/execute |
| `bench.trimdatabase` | Trim unused database tables | bench | yes | recreate | `docs/framework/framework-12.md` lines 834–884 | https://docs.frappe.io/framework/user/en/bench/reference/trim-database |
| `bench.production` | Set up a production environment | bench | yes | reversible | `docs/framework/framework-11.md` lines 783–843 | https://docs.frappe.io/framework/user/en/bench/guides/setup-production |
| `bench.multitenancy` | Run several sites on one bench | bench | yes | reversible | `docs/framework/framework-11.md` lines 714–781 | https://docs.frappe.io/framework/user/en/bench/guides/setup-multitenancy |
| `bench.https` | Configure HTTPS for a site | bench | yes | reversible | `docs/framework/framework-11.md` lines 447–512 | https://docs.frappe.io/framework/user/en/bench/guides/configuring-https |
| `bench.domains` | Add a custom domain to a site | bench | yes | reversible | `docs/framework/framework-11.md` lines 411–445 | https://docs.frappe.io/framework/user/en/bench/guides/adding-custom-domains |
| `bench.procfile` | Understand the bench Procfile | bench | no | reversible | `docs/framework/framework-12.md` lines 1234–1274 | https://docs.frappe.io/framework/user/en/bench/resources/bench-procfile |
| `bench.services` | Check background services | bench | no | reversible | `docs/framework/framework-12.md` lines 999–1051 | https://docs.frappe.io/framework/user/en/bench/resources/background-services |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

