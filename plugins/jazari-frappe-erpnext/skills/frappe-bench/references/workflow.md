# Back up and restore a site

Owner: **Urwah** · verified: docs (documentation, not a live probe)

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Back up a site** (`bench.backup`, bench mode)
   read: `docs/framework/framework__user__en__bench__reference__backup.md`   (https://docs.frappe.io/framework/user/en/bench/reference/backup)
2. **Restore a site from a backup** (`bench.restore`, bench mode) — FRESH BACKUP FIRST, irreversible
   read: `docs/framework/framework__user__en__bench__reference__restore.md`   (https://docs.frappe.io/framework/user/en/bench/reference/restore)
3. **Back up a Frappe Cloud site** (`cloud.site.backup`, browser mode)
   read: `docs/cloud/cloud__sites__backups.md`   (https://docs.frappe.io/cloud/sites/backups)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
