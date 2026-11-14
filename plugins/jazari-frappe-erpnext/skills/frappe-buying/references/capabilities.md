# Capabilities — Buying and procurement

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `buy.supplier` | Create and manage suppliers | api | yes | reversible | `docs/erpnext/erpnext__supplier.md` | https://docs.frappe.io/erpnext/supplier |
| `buy.materialrequest` | Raise a material request | api | yes | reversible | `docs/erpnext/erpnext__material-request.md` | https://docs.frappe.io/erpnext/material-request |
| `buy.rfq` | Send a request for quotation | api | yes | irreversible | `docs/erpnext/erpnext__request-for-quotation.md` | https://docs.frappe.io/erpnext/request-for-quotation |
| `buy.supplierquotation` | Record a supplier quotation | api | yes | reversible | `docs/erpnext/erpnext__supplier-quotation.md` | https://docs.frappe.io/erpnext/supplier-quotation |
| `buy.purchaseorder` | Place a purchase order | api | yes | irreversible | `docs/erpnext/erpnext__purchase-order.md` | https://docs.frappe.io/erpnext/purchase-order |
| `buy.purchasereceipt` | Receive goods | api | yes | irreversible | `docs/erpnext/erpnext__purchase-receipt.md` | https://docs.frappe.io/erpnext/purchase-receipt |
| `buy.purchasereturn` | Return goods to a supplier | api | yes | irreversible | `docs/erpnext/erpnext__purchase-return.md` | https://docs.frappe.io/erpnext/purchase-return |
| `buy.landedcost` | Add landed costs | api | yes | reversible | `docs/erpnext/erpnext__landed-cost-voucher.md` | https://docs.frappe.io/erpnext/landed-cost-voucher |
| `buy.subcontracting` | Run subcontracting | browser | yes | reversible | `docs/erpnext/erpnext__subcontracting.md` | https://docs.frappe.io/erpnext/subcontracting |
| `buy.scorecard` | Score suppliers | browser | yes | reversible | `docs/erpnext/erpnext__supplier-scorecard.md` | https://docs.frappe.io/erpnext/supplier-scorecard |
| `buy.blanketorder` | Agree a blanket order | api | yes | reversible | `docs/erpnext/erpnext__blanket-order.md` | https://docs.frappe.io/erpnext/blanket-order |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

