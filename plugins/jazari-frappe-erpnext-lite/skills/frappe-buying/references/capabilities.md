# Capabilities — Buying and procurement

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `buy.supplier` | Create and manage suppliers | api | yes | reversible | `docs/erpnext/erpnext-16.md` lines 2091–2251 | https://docs.frappe.io/erpnext/supplier |
| `buy.materialrequest` | Raise a material request | api | yes | reversible | `docs/erpnext/erpnext-10.md` lines 316–441 | https://docs.frappe.io/erpnext/material-request |
| `buy.rfq` | Send a request for quotation | api | yes | irreversible | `docs/erpnext/erpnext-13.md` lines 2736–2901 | https://docs.frappe.io/erpnext/request-for-quotation |
| `buy.supplierquotation` | Record a supplier quotation | api | yes | reversible | `docs/erpnext/erpnext-16.md` lines 1902–1986 | https://docs.frappe.io/erpnext/supplier-quotation |
| `buy.purchaseorder` | Place a purchase order | api | yes | irreversible | `docs/erpnext/erpnext-12.md` lines 2554–2748 | https://docs.frappe.io/erpnext/purchase-order |
| `buy.purchasereceipt` | Receive goods | api | yes | irreversible | `docs/erpnext/erpnext-12.md` lines 2750–3011 | https://docs.frappe.io/erpnext/purchase-receipt |
| `buy.purchasereturn` | Return goods to a supplier | api | yes | irreversible | `docs/erpnext/erpnext-12.md` lines 3013–3068 | https://docs.frappe.io/erpnext/purchase-return |
| `buy.landedcost` | Add landed costs | api | yes | reversible | `docs/erpnext/erpnext-09.md` lines 1495–1516 | https://docs.frappe.io/erpnext/landed-cost-voucher |
| `buy.subcontracting` | Run subcontracting | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 1282–1499 | https://docs.frappe.io/erpnext/subcontracting |
| `buy.scorecard` | Score suppliers | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 1988–2089 | https://docs.frappe.io/erpnext/supplier-scorecard |
| `buy.blanketorder` | Agree a blanket order | api | yes | reversible | `docs/erpnext/erpnext-03.md` lines 1127–1238 | https://docs.frappe.io/erpnext/blanket-order |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

