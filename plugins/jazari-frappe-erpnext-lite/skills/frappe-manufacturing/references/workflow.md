# Manufacture to order

Owner: **Imran** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Build a bill of materials** (`mfg.bom`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__bill-of-materials.md`   (https://docs.frappe.io/erpnext/bill-of-materials)
2. **Plan production** (`mfg.productionplan`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__production-plan.md`   (https://docs.frappe.io/erpnext/production-plan)
3. **Run a work order** (`mfg.workorder`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__work-order.md`   (https://docs.frappe.io/erpnext/work-order)
4. **Record work on a job card** (`mfg.jobcard`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__job-card.md`   (https://docs.frappe.io/erpnext/job-card)
5. **Make a stock entry** (`stock.entry`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__stock-entry.md`   (https://docs.frappe.io/erpnext/stock-entry)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
