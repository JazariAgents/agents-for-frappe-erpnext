# Set up a company and go live on ERPNext

Owner: **Rukaz** · verified: docs (documentation, not a live probe)

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Set up a company** (`setup.company`, browser mode)
   read: `docs/erpnext/erpnext__company-setup.md`   (https://docs.frappe.io/erpnext/company-setup)
2. **Set the fiscal year** (`setup.fiscalyear`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__fiscal-year.md`   (https://docs.frappe.io/erpnext/fiscal-year)
3. **Set up the chart of accounts** (`setup.coa`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__chart-of-accounts.md`   (https://docs.frappe.io/erpnext/chart-of-accounts)
4. **Add and manage users** (`perm.users`, browser mode)
   read: `docs/framework/framework__user__en__basics__users-and-permissions.md`   (https://docs.frappe.io/framework/user/en/basics/users-and-permissions)
5. **Import records from a spreadsheet** (`imp.dataimport`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__data-import.md`   (https://docs.frappe.io/erpnext/data-import)
6. **Enter opening balances** (`acc.openingbalance`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__opening-balance.md`   (https://docs.frappe.io/erpnext/opening-balance)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
