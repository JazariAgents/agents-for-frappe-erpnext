# Capabilities — Buying and procurement

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `buy.supplier` | Create and manage suppliers | api | yes | reversible | `docs/erpnext/erpnext-62.md` lines 192–352 | https://docs.frappe.io/erpnext/supplier |
| `buy.materialrequest` | Raise a material request | api | yes | reversible | `docs/erpnext/erpnext-36.md` lines 615–740 | https://docs.frappe.io/erpnext/material-request |
| `buy.rfq` | Send a request for quotation | api | yes | irreversible | `docs/erpnext/erpnext-51.md` lines 3–168 | https://docs.frappe.io/erpnext/request-for-quotation |
| `buy.supplierquotation` | Record a supplier quotation | api | yes | reversible | `docs/erpnext/erpnext-62.md` lines 3–87 | https://docs.frappe.io/erpnext/supplier-quotation |
| `buy.purchaseorder` | Place a purchase order | api | yes | irreversible | `docs/erpnext/erpnext-47.md` lines 204–398 | https://docs.frappe.io/erpnext/purchase-order |
| `buy.purchasereceipt` | Receive goods | api | yes | irreversible | `docs/erpnext/erpnext-47.md` lines 400–661 | https://docs.frappe.io/erpnext/purchase-receipt |
| `buy.purchasereturn` | Return goods to a supplier | api | yes | irreversible | `docs/erpnext/erpnext-47.md` lines 663–718 | https://docs.frappe.io/erpnext/purchase-return |
| `buy.landedcost` | Add landed costs | api | yes | reversible | `docs/erpnext/erpnext-34.md` lines 176–197 | https://docs.frappe.io/erpnext/landed-cost-voucher |
| `buy.subcontracting` | Run subcontracting | browser | yes | reversible | `docs/erpnext/erpnext-61.md` lines 109–326 | https://docs.frappe.io/erpnext/subcontracting |
| `buy.scorecard` | Score suppliers | browser | yes | reversible | `docs/erpnext/erpnext-62.md` lines 89–190 | https://docs.frappe.io/erpnext/supplier-scorecard |
| `buy.blanketorder` | Agree a blanket order | api | yes | reversible | `docs/erpnext/erpnext-10.md` lines 3–114 | https://docs.frappe.io/erpnext/blanket-order |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

