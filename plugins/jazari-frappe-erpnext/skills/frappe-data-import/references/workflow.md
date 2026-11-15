# Load data in bulk from spreadsheets

Owner: **Wafir** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Import records from a spreadsheet** (`imp.dataimport`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__data-import.md`   (https://docs.frappe.io/erpnext/data-import)
2. **Update many records at once** (`imp.bulkupdate`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__bulk-update.md`   (https://docs.frappe.io/erpnext/bulk-update)
3. **Import a chart of accounts** (`imp.coaimport`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__chart-of-accounts-importer.md`   (https://docs.frappe.io/erpnext/chart-of-accounts-importer)
4. **Load opening stock** (`stock.openingstock`, browser mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__opening-stock.md`   (https://docs.frappe.io/erpnext/opening-stock)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
