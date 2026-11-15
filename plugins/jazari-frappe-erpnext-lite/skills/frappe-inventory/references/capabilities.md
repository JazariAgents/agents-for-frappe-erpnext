# Capabilities — Inventory and stock

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `stock.item` | Create and manage items | api | yes | reversible | `docs/erpnext/erpnext-09.md` lines 624–928 | https://docs.frappe.io/erpnext/item |
| `stock.itemgroup` | Group items | browser | yes | reversible | `docs/erpnext/erpnext-09.md` lines 83–153 | https://docs.frappe.io/erpnext/item-group |
| `stock.variants` | Create item variants | browser | yes | reversible | `docs/erpnext/erpnext-09.md` lines 483–544 | https://docs.frappe.io/erpnext/item-variants |
| `stock.attribute` | Define item attributes | browser | yes | reversible | `docs/erpnext/erpnext-08.md` lines 3405–3444 | https://docs.frappe.io/erpnext/item-attribute |
| `stock.bundle` | Sell a product bundle | browser | yes | reversible | `docs/erpnext/erpnext-12.md` lines 465–542 | https://docs.frappe.io/erpnext/product-bundle |
| `stock.uom` | Manage units of measure | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 2735–2752 | https://docs.frappe.io/erpnext/uom |
| `stock.warehouse` | Set up warehouses | api | yes | reversible | `docs/erpnext/erpnext-18.md` lines 30–108 | https://docs.frappe.io/erpnext/warehouse |
| `stock.entry` | Make a stock entry | api | yes | irreversible | `docs/erpnext/erpnext-15.md` lines 3057–3241 | https://docs.frappe.io/erpnext/stock-entry |
| `stock.reconciliation` | Reconcile physical stock | api | yes | irreversible | `docs/erpnext/erpnext-16.md` lines 3–128 | https://docs.frappe.io/erpnext/stock-reconciliation |
| `stock.openingstock` | Load opening stock | browser | yes | irreversible | `docs/erpnext/erpnext-10.md` lines 2730–2770 | https://docs.frappe.io/erpnext/opening-stock |
| `stock.batch` | Track batches | api | yes | reversible | `docs/erpnext/erpnext-03.md` lines 845–931 | https://docs.frappe.io/erpnext/batch |
| `stock.serial` | Track serial numbers | api | yes | reversible | `docs/erpnext/erpnext-15.md` lines 545–641 | https://docs.frappe.io/erpnext/serial-no |
| `stock.bundleserial` | Use the serial and batch bundle | api | yes | reversible | `docs/erpnext/erpnext-15.md` lines 304–435 | https://docs.frappe.io/erpnext/serial-and-batch-bundle |
| `stock.valuation` | Choose a valuation method | guide | no | reversible | `docs/erpnext/erpnext-07.md` lines 1888–2073 | https://docs.frappe.io/erpnext/fifo-and-moving-average |
| `stock.perpetual` | Run perpetual inventory | guide | no | reversible | `docs/erpnext/erpnext-11.md` lines 1479–1750 | https://docs.frappe.io/erpnext/perpetual-inventory |
| `stock.reservation` | Reserve stock for an order | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 344–401 | https://docs.frappe.io/erpnext/stock-reservation |
| `stock.putaway` | Set putaway rules | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 418–520 | https://docs.frappe.io/erpnext/putaway-rule |
| `stock.quality` | Inspect incoming quality | api | yes | reversible | `docs/erpnext/erpnext-13.md` lines 566–701 | https://docs.frappe.io/erpnext/quality-inspection |
| `stock.settings` | Configure stock settings | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 403–607 | https://docs.frappe.io/erpnext/stock-settings |
| `stock.ledger` | Read the stock ledger | browser | no | reversible | `docs/erpnext/erpnext-15.md` lines 3262–3304 | https://docs.frappe.io/erpnext/stock-ledger |
| `stock.levelreport` | Check stock levels | browser | no | reversible | `docs/erpnext/erpnext-15.md` lines 3306–3333 | https://docs.frappe.io/erpnext/stock-level-report |
| `stock.closing` | Close a stock period | browser | yes | irreversible | `docs/erpnext/erpnext-15.md` lines 2979–3001 | https://docs.frappe.io/erpnext/stock-closing-entry |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

