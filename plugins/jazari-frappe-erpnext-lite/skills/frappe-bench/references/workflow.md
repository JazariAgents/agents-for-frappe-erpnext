# Back up and restore a site

Owner: **Urwah** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Back up a site** (`bench.backup`, bench mode)
   read: `docs/framework/framework__user__en__bench__reference__backup.md`   (https://docs.frappe.io/framework/user/en/bench/reference/backup)
2. **Restore a site from a backup** (`bench.restore`, bench mode) — FRESH BACKUP FIRST, irreversible
   read: `docs/framework/framework__user__en__bench__reference__restore.md`   (https://docs.frappe.io/framework/user/en/bench/reference/restore)
3. **Back up a Frappe Cloud site** (`cloud.site.backup`, browser mode)
   read: `docs/cloud/cloud__sites__backups.md`   (https://docs.frappe.io/cloud/sites/backups)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
