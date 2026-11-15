# Close the month

Owner: **Mizan** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Reconcile the bank** (`acc.bankreconciliation`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__bank-reconciliation.md`   (https://docs.frappe.io/erpnext/bank-reconciliation)
2. **Reconcile payments against invoices** (`acc.paymentreconciliation`, browser mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__payment-reconciliation.md`   (https://docs.frappe.io/erpnext/payment-reconciliation)
3. **Produce a balance sheet** (`rep.balancesheet`, browser mode)
   read: `docs/erpnext/erpnext__balance-sheet.md`   (https://docs.frappe.io/erpnext/balance-sheet)
4. **Produce a profit and loss report** (`rep.pandl`, browser mode)
   read: `docs/erpnext/erpnext__profit-and-loss-report.md`   (https://docs.frappe.io/erpnext/profit-and-loss-report)
5. **Close an accounting period** (`acc.periodclose`, browser mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__period-closing-voucher.md`   (https://docs.frappe.io/erpnext/period-closing-voucher)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
