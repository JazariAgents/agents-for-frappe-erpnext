# Capabilities — Selling, delivery and point of sale

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `sell.quotation` | Send a quotation | api | yes | reversible | `docs/erpnext/erpnext-13.md` lines 1206–1337 | https://docs.frappe.io/erpnext/quotation |
| `sell.salesorder` | Confirm a sales order | api | yes | irreversible | `docs/erpnext/erpnext-14.md` lines 674–915 | https://docs.frappe.io/erpnext/sales-order |
| `sell.deliverynote` | Ship goods with a delivery note | api | yes | irreversible | `docs/erpnext/erpnext-06.md` lines 3–266 | https://docs.frappe.io/erpnext/delivery-note |
| `sell.picklist` | Pick stock for an order | api | yes | reversible | `docs/erpnext/erpnext-11.md` lines 1916–2030 | https://docs.frappe.io/erpnext/pick-list |
| `sell.packingslip` | Pack an order | api | yes | reversible | `docs/erpnext/erpnext-10.md` lines 3023–3088 | https://docs.frappe.io/erpnext/packing-slip |
| `sell.shipment` | Book a shipment | api | yes | irreversible | `docs/erpnext/erpnext-15.md` lines 1812–1893 | https://docs.frappe.io/erpnext/shipment |
| `sell.deliverytrip` | Plan a delivery trip | api | yes | reversible | `docs/erpnext/erpnext-06.md` lines 268–305 | https://docs.frappe.io/erpnext/delivery-trip |
| `sell.return` | Process a sales return | api | yes | irreversible | `docs/erpnext/erpnext-14.md` lines 1643–1836 | https://docs.frappe.io/erpnext/sales-return |
| `sell.customer` | Create and manage customers | api | yes | reversible | `docs/erpnext/erpnext-05.md` lines 820–992 | https://docs.frappe.io/erpnext/customer |
| `sell.customergroup` | Group customers | browser | yes | reversible | `docs/erpnext/erpnext-05.md` lines 544–698 | https://docs.frappe.io/erpnext/customer-group |
| `sell.territory` | Organise territories | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 974–1144 | https://docs.frappe.io/erpnext/territory |
| `sell.pricelist` | Maintain price lists | api | yes | reversible | `docs/erpnext/erpnext-11.md` lines 2650–2689 | https://docs.frappe.io/erpnext/price-lists |
| `sell.itemprice` | Set item prices | api | yes | reversible | `docs/erpnext/erpnext-09.md` lines 155–229 | https://docs.frappe.io/erpnext/item-price |
| `sell.pricingrule` | Apply a pricing rule | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 2691–2838 | https://docs.frappe.io/erpnext/pricing-rule |
| `sell.promotional` | Run a promotional scheme | browser | yes | reversible | `docs/erpnext/erpnext-12.md` lines 2015–2128 | https://docs.frappe.io/erpnext/promotional-scheme |
| `sell.coupon` | Issue coupon codes | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 2467–2590 | https://docs.frappe.io/erpnext/coupon-code |
| `sell.loyalty` | Run a loyalty program | browser | yes | reversible | `docs/erpnext/erpnext-09.md` lines 2122–2250 | https://docs.frappe.io/erpnext/loyalty-program |
| `sell.salesperson` | Track sales people and commission | browser | yes | reversible | `docs/erpnext/erpnext-14.md` lines 1331–1480 | https://docs.frappe.io/erpnext/sales-person |
| `sell.creditlimit` | Enforce a customer credit limit | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 2690–2874 | https://docs.frappe.io/erpnext/credit-limit |
| `sell.pos` | Sell at the point of sale | browser | yes | irreversible | `docs/erpnext/erpnext-11.md` lines 2122–2143 | https://docs.frappe.io/erpnext/point-of-sale |
| `sell.posprofile` | Configure a POS profile | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 2205–2340 | https://docs.frappe.io/erpnext/pos-profile |
| `sell.posconsolidate` | Consolidate POS invoices | browser | yes | irreversible | `docs/erpnext/erpnext-11.md` lines 2174–2203 | https://docs.frappe.io/erpnext/pos-invoice-consolidation |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

