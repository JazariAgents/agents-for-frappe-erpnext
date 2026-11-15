# Set up a company and go live on ERPNext

Owner: **Rukaz** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Set up a company** (`setup.company`, browser mode)
   read: `docs/erpnext/erpnext-04.md` lines 1546–1628   (https://docs.frappe.io/erpnext/company-setup)
2. **Set the fiscal year** (`setup.fiscalyear`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-07.md` lines 2480–2549   (https://docs.frappe.io/erpnext/fiscal-year)
3. **Set up the chart of accounts** (`setup.coa`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-04.md` lines 775–860   (https://docs.frappe.io/erpnext/chart-of-accounts)
4. **Add and manage users** (`perm.users`, browser mode)
   read: `docs/framework/framework-03.md` lines 578–739   (https://docs.frappe.io/framework/user/en/basics/users-and-permissions)
5. **Import records from a spreadsheet** (`imp.dataimport`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-05.md` lines 1481–1721   (https://docs.frappe.io/erpnext/data-import)
6. **Enter opening balances** (`acc.openingbalance`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-10.md` lines 2437–2540   (https://docs.frappe.io/erpnext/opening-balance)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
