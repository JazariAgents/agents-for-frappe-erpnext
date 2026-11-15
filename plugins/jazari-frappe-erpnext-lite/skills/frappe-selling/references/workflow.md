# Run order to cash

Owner: **Hazim** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Send a quotation** (`sell.quotation`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext-49.md` lines 335–466   (https://docs.frappe.io/erpnext/quotation)
2. **Confirm a sales order** (`sell.salesorder`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-53.md` lines 3–244   (https://docs.frappe.io/erpnext/sales-order)
3. **Ship goods with a delivery note** (`sell.deliverynote`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-20.md` lines 476–739   (https://docs.frappe.io/erpnext/delivery-note)
4. **Raise a sales invoice** (`acc.salesinvoice`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-52.md` lines 306–524   (https://docs.frappe.io/erpnext/sales-invoice)
5. **Record a payment entry** (`acc.paymententry`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext-40.md` lines 353–551   (https://docs.frappe.io/erpnext/payment-entry)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
