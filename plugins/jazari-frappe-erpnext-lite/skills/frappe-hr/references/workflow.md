# Run monthly payroll

Owner: **Anees** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Mark attendance** (`hr.attendance`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/frappe-hr/frappe-hr-01.md` lines 537–612   (https://docs.frappe.io/hr/attendance)
2. **Build a salary structure** (`hr.salarystructure`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/frappe-hr/frappe-hr-03.md` lines 476–571   (https://docs.frappe.io/hr/salary-structure)
3. **Run payroll** (`hr.payrollentry`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/frappe-hr/frappe-hr-02.md` lines 3169–3277   (https://docs.frappe.io/hr/payroll-entry)
4. **Issue salary slips** (`hr.salaryslip`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/frappe-hr/frappe-hr-03.md` lines 232–304   (https://docs.frappe.io/hr/salary-slip)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
