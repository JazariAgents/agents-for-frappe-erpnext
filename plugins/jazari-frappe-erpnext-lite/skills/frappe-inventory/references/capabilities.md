# Capabilities — Inventory and stock

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `stock.item` | Create and manage items | api | yes | reversible | `docs/erpnext/erpnext-33.md` lines 3–307 | https://docs.frappe.io/erpnext/item |
| `stock.itemgroup` | Group items | browser | yes | reversible | `docs/erpnext/erpnext-32.md` lines 175–245 | https://docs.frappe.io/erpnext/item-group |
| `stock.variants` | Create item variants | browser | yes | reversible | `docs/erpnext/erpnext-32.md` lines 575–636 | https://docs.frappe.io/erpnext/item-variants |
| `stock.attribute` | Define item attributes | browser | yes | reversible | `docs/erpnext/erpnext-31.md` lines 884–923 | https://docs.frappe.io/erpnext/item-attribute |
| `stock.bundle` | Sell a product bundle | browser | yes | reversible | `docs/erpnext/erpnext-44.md` lines 669–746 | https://docs.frappe.io/erpnext/product-bundle |
| `stock.uom` | Manage units of measure | browser | yes | reversible | `docs/erpnext/erpnext-66.md` lines 918–935 | https://docs.frappe.io/erpnext/uom |
| `stock.warehouse` | Set up warehouses | api | yes | reversible | `docs/erpnext/erpnext-67.md` lines 667–745 | https://docs.frappe.io/erpnext/warehouse |
| `stock.entry` | Make a stock entry | api | yes | irreversible | `docs/erpnext/erpnext-59.md` lines 487–671 | https://docs.frappe.io/erpnext/stock-entry |
| `stock.reconciliation` | Reconcile physical stock | api | yes | irreversible | `docs/erpnext/erpnext-60.md` lines 3–128 | https://docs.frappe.io/erpnext/stock-reconciliation |
| `stock.openingstock` | Load opening stock | browser | yes | irreversible | `docs/erpnext/erpnext-39.md` lines 455–495 | https://docs.frappe.io/erpnext/opening-stock |
| `stock.batch` | Track batches | api | yes | reversible | `docs/erpnext/erpnext-09.md` lines 522–608 | https://docs.frappe.io/erpnext/batch |
| `stock.serial` | Track serial numbers | api | yes | reversible | `docs/erpnext/erpnext-56.md` lines 545–641 | https://docs.frappe.io/erpnext/serial-no |
| `stock.bundleserial` | Use the serial and batch bundle | api | yes | reversible | `docs/erpnext/erpnext-56.md` lines 304–435 | https://docs.frappe.io/erpnext/serial-and-batch-bundle |
| `stock.valuation` | Choose a valuation method | guide | no | reversible | `docs/erpnext/erpnext-26.md` lines 3–188 | https://docs.frappe.io/erpnext/fifo-and-moving-average |
| `stock.perpetual` | Run perpetual inventory | guide | no | reversible | `docs/erpnext/erpnext-42.md` lines 355–626 | https://docs.frappe.io/erpnext/perpetual-inventory |
| `stock.reservation` | Reserve stock for an order | browser | yes | reversible | `docs/erpnext/erpnext-60.md` lines 344–401 | https://docs.frappe.io/erpnext/stock-reservation |
| `stock.putaway` | Set putaway rules | browser | yes | reversible | `docs/erpnext/erpnext-48.md` lines 418–520 | https://docs.frappe.io/erpnext/putaway-rule |
| `stock.quality` | Inspect incoming quality | api | yes | reversible | `docs/erpnext/erpnext-48.md` lines 566–701 | https://docs.frappe.io/erpnext/quality-inspection |
| `stock.settings` | Configure stock settings | browser | yes | reversible | `docs/erpnext/erpnext-60.md` lines 403–607 | https://docs.frappe.io/erpnext/stock-settings |
| `stock.ledger` | Read the stock ledger | browser | no | reversible | `docs/erpnext/erpnext-59.md` lines 692–734 | https://docs.frappe.io/erpnext/stock-ledger |
| `stock.levelreport` | Check stock levels | browser | no | reversible | `docs/erpnext/erpnext-59.md` lines 736–763 | https://docs.frappe.io/erpnext/stock-level-report |
| `stock.closing` | Close a stock period | browser | yes | irreversible | `docs/erpnext/erpnext-59.md` lines 409–431 | https://docs.frappe.io/erpnext/stock-closing-entry |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

