# Run order to cash

Owner: **Hazim** · verified: docs (documentation, not a live probe)

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Send a quotation** (`sell.quotation`, api mode) — SNAPSHOT FIRST, reversible
   read: `docs/erpnext/erpnext__quotation.md`   (https://docs.frappe.io/erpnext/quotation)
2. **Confirm a sales order** (`sell.salesorder`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__sales-order.md`   (https://docs.frappe.io/erpnext/sales-order)
3. **Ship goods with a delivery note** (`sell.deliverynote`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__delivery-note.md`   (https://docs.frappe.io/erpnext/delivery-note)
4. **Raise a sales invoice** (`acc.salesinvoice`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__sales-invoice.md`   (https://docs.frappe.io/erpnext/sales-invoice)
5. **Record a payment entry** (`acc.paymententry`, api mode) — SNAPSHOT FIRST, irreversible
   read: `docs/erpnext/erpnext__payment-entry.md`   (https://docs.frappe.io/erpnext/payment-entry)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
