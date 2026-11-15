# Capabilities — Run bench — sites, apps, backups, deploys

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `bench.overview` | Understand bench and the bench directory | bench | no | reversible | `docs/framework/framework__user__en__bench.md` | https://docs.frappe.io/framework/user/en/bench |
| `bench.commands` | Run bench CLI commands | bench | no | reversible | `docs/framework/framework__user__en__bench__bench-commands.md` | https://docs.frappe.io/framework/user/en/bench/bench-commands |
| `bench.frappe.commands` | Run site-scoped framework commands | bench | no | reversible | `docs/framework/framework__user__en__bench__frappe-commands.md` | https://docs.frappe.io/framework/user/en/bench/frappe-commands |
| `bench.newsite` | Create a site with bench new-site | bench | no | reversible | `docs/framework/framework__user__en__bench__reference__new-site.md` | https://docs.frappe.io/framework/user/en/bench/reference/new-site |
| `bench.dropsite` | Drop a site | bench | yes | recreate | `docs/framework/framework__user__en__bench__reference__drop-site.md` | https://docs.frappe.io/framework/user/en/bench/reference/drop-site |
| `bench.backup` | Back up a site | bench | no | reversible | `docs/framework/framework__user__en__bench__reference__backup.md` | https://docs.frappe.io/framework/user/en/bench/reference/backup |
| `bench.restore` | Restore a site from a backup | bench | yes | irreversible | `docs/framework/framework__user__en__bench__reference__restore.md` | https://docs.frappe.io/framework/user/en/bench/reference/restore |
| `bench.partialrestore` | Restore selected tables only | bench | yes | irreversible | `docs/framework/framework__user__en__bench__reference__partial-restore.md` | https://docs.frappe.io/framework/user/en/bench/reference/partial-restore |
| `bench.migrate` | Run migrations after an update | bench | yes | reversible | `docs/framework/framework__user__en__bench__reference__migrate.md` | https://docs.frappe.io/framework/user/en/bench/reference/migrate |
| `bench.reinstall` | Reinstall a site from scratch | bench | yes | recreate | `docs/framework/framework__user__en__bench__reference__reinstall.md` | https://docs.frappe.io/framework/user/en/bench/reference/reinstall |
| `bench.listapps` | List the apps installed on a site | bench | no | reversible | `docs/framework/framework__user__en__bench__reference__list-apps.md` | https://docs.frappe.io/framework/user/en/bench/reference/list-apps |
| `bench.uninstallapp` | Uninstall an app from a site | bench | yes | recreate | `docs/framework/framework__user__en__bench__reference__uninstall-app.md` | https://docs.frappe.io/framework/user/en/bench/reference/uninstall-app |
| `bench.config` | Read and change site configuration | bench | yes | reversible | `docs/framework/framework__user__en__bench__reference__set-config.md` | https://docs.frappe.io/framework/user/en/bench/reference/set-config |
| `bench.showconfig` | Show the current site configuration | bench | no | reversible | `docs/framework/framework__user__en__bench__reference__show-config.md` | https://docs.frappe.io/framework/user/en/bench/reference/show-config |
| `bench.execute` | Execute a Python method on a site | bench | yes | irreversible | `docs/framework/framework__user__en__bench__reference__execute.md` | https://docs.frappe.io/framework/user/en/bench/reference/execute |
| `bench.trimdatabase` | Trim unused database tables | bench | yes | recreate | `docs/framework/framework__user__en__bench__reference__trim-database.md` | https://docs.frappe.io/framework/user/en/bench/reference/trim-database |
| `bench.production` | Set up a production environment | bench | yes | reversible | `docs/framework/framework__user__en__bench__guides__setup-production.md` | https://docs.frappe.io/framework/user/en/bench/guides/setup-production |
| `bench.multitenancy` | Run several sites on one bench | bench | yes | reversible | `docs/framework/framework__user__en__bench__guides__setup-multitenancy.md` | https://docs.frappe.io/framework/user/en/bench/guides/setup-multitenancy |
| `bench.https` | Configure HTTPS for a site | bench | yes | reversible | `docs/framework/framework__user__en__bench__guides__configuring-https.md` | https://docs.frappe.io/framework/user/en/bench/guides/configuring-https |
| `bench.domains` | Add a custom domain to a site | bench | yes | reversible | `docs/framework/framework__user__en__bench__guides__adding-custom-domains.md` | https://docs.frappe.io/framework/user/en/bench/guides/adding-custom-domains |
| `bench.procfile` | Understand the bench Procfile | bench | no | reversible | `docs/framework/framework__user__en__bench__resources__bench-procfile.md` | https://docs.frappe.io/framework/user/en/bench/resources/bench-procfile |
| `bench.services` | Check background services | bench | no | reversible | `docs/framework/framework__user__en__bench__resources__background-services.md` | https://docs.frappe.io/framework/user/en/bench/resources/background-services |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

