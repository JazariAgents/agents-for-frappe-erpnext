# Capabilities — Selling, delivery and point of sale

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `sell.quotation` | Send a quotation | api | yes | reversible | `docs/erpnext/erpnext__quotation.md` | https://docs.frappe.io/erpnext/quotation |
| `sell.salesorder` | Confirm a sales order | api | yes | irreversible | `docs/erpnext/erpnext__sales-order.md` | https://docs.frappe.io/erpnext/sales-order |
| `sell.deliverynote` | Ship goods with a delivery note | api | yes | irreversible | `docs/erpnext/erpnext__delivery-note.md` | https://docs.frappe.io/erpnext/delivery-note |
| `sell.picklist` | Pick stock for an order | api | yes | reversible | `docs/erpnext/erpnext__pick-list.md` | https://docs.frappe.io/erpnext/pick-list |
| `sell.packingslip` | Pack an order | api | yes | reversible | `docs/erpnext/erpnext__packing-slip.md` | https://docs.frappe.io/erpnext/packing-slip |
| `sell.shipment` | Book a shipment | api | yes | irreversible | `docs/erpnext/erpnext__shipment.md` | https://docs.frappe.io/erpnext/shipment |
| `sell.deliverytrip` | Plan a delivery trip | api | yes | reversible | `docs/erpnext/erpnext__delivery-trip.md` | https://docs.frappe.io/erpnext/delivery-trip |
| `sell.return` | Process a sales return | api | yes | irreversible | `docs/erpnext/erpnext__sales-return.md` | https://docs.frappe.io/erpnext/sales-return |
| `sell.customer` | Create and manage customers | api | yes | reversible | `docs/erpnext/erpnext__customer.md` | https://docs.frappe.io/erpnext/customer |
| `sell.customergroup` | Group customers | browser | yes | reversible | `docs/erpnext/erpnext__customer-group.md` | https://docs.frappe.io/erpnext/customer-group |
| `sell.territory` | Organise territories | browser | yes | reversible | `docs/erpnext/erpnext__territory.md` | https://docs.frappe.io/erpnext/territory |
| `sell.pricelist` | Maintain price lists | api | yes | reversible | `docs/erpnext/erpnext__price-lists.md` | https://docs.frappe.io/erpnext/price-lists |
| `sell.itemprice` | Set item prices | api | yes | reversible | `docs/erpnext/erpnext__item-price.md` | https://docs.frappe.io/erpnext/item-price |
| `sell.pricingrule` | Apply a pricing rule | browser | yes | reversible | `docs/erpnext/erpnext__pricing-rule.md` | https://docs.frappe.io/erpnext/pricing-rule |
| `sell.promotional` | Run a promotional scheme | browser | yes | reversible | `docs/erpnext/erpnext__promotional-scheme.md` | https://docs.frappe.io/erpnext/promotional-scheme |
| `sell.coupon` | Issue coupon codes | browser | yes | reversible | `docs/erpnext/erpnext__coupon-code.md` | https://docs.frappe.io/erpnext/coupon-code |
| `sell.loyalty` | Run a loyalty program | browser | yes | reversible | `docs/erpnext/erpnext__loyalty-program.md` | https://docs.frappe.io/erpnext/loyalty-program |
| `sell.salesperson` | Track sales people and commission | browser | yes | reversible | `docs/erpnext/erpnext__sales-person.md` | https://docs.frappe.io/erpnext/sales-person |
| `sell.creditlimit` | Enforce a customer credit limit | browser | yes | reversible | `docs/erpnext/erpnext__credit-limit.md` | https://docs.frappe.io/erpnext/credit-limit |
| `sell.pos` | Sell at the point of sale | browser | yes | irreversible | `docs/erpnext/erpnext__point-of-sale.md` | https://docs.frappe.io/erpnext/point-of-sale |
| `sell.posprofile` | Configure a POS profile | browser | yes | reversible | `docs/erpnext/erpnext__pos-profile.md` | https://docs.frappe.io/erpnext/pos-profile |
| `sell.posconsolidate` | Consolidate POS invoices | browser | yes | irreversible | `docs/erpnext/erpnext__pos-invoice-consolidation.md` | https://docs.frappe.io/erpnext/pos-invoice-consolidation |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

