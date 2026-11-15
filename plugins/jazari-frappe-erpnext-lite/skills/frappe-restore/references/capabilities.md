# Capabilities — Undo and restore

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `bench.backup` | Back up a site | bench | no | reversible | `docs/framework/framework__user__en__bench__reference__backup.md` | https://docs.frappe.io/framework/user/en/bench/reference/backup |
| `bench.restore` | Restore a site from a backup | bench | yes | irreversible | `docs/framework/framework__user__en__bench__reference__restore.md` | https://docs.frappe.io/framework/user/en/bench/reference/restore |
| `bench.partialrestore` | Restore selected tables only | bench | yes | irreversible | `docs/framework/framework__user__en__bench__reference__partial-restore.md` | https://docs.frappe.io/framework/user/en/bench/reference/partial-restore |
| `cloud.site.backup` | Back up a Frappe Cloud site | browser | no | reversible | `docs/cloud/cloud__sites__backups.md` | https://docs.frappe.io/cloud/sites/backups |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

