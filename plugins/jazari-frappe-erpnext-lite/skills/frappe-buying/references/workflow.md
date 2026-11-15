# Run procure to pay

Owner: **Mizan** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Raise a material request** (`buy.materialrequest`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-37.md` lines 3–128   (https://docs.frappe.io/erpnext/material-request)
2. **Place a purchase order** (`buy.purchaseorder`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-47.md` lines 204–398   (https://docs.frappe.io/erpnext/purchase-order)
3. **Receive goods** (`buy.purchasereceipt`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-47.md` lines 400–661   (https://docs.frappe.io/erpnext/purchase-receipt)
4. **Record a purchase invoice** (`acc.purchaseinvoice`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-47.md` lines 3–202   (https://docs.frappe.io/erpnext/purchase-invoice)
5. **Record a payment entry** (`acc.paymententry`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-40.md` lines 353–551   (https://docs.frappe.io/erpnext/payment-entry)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
