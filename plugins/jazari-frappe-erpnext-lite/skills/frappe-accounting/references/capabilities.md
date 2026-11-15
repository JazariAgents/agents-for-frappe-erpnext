# Capabilities — Accounting, invoicing and tax

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `acc.salesinvoice` | Raise a sales invoice | api | yes | irreversible | `docs/erpnext/erpnext-52.md` lines 306–524 | https://docs.frappe.io/erpnext/sales-invoice |
| `acc.purchaseinvoice` | Record a purchase invoice | api | yes | irreversible | `docs/erpnext/erpnext-47.md` lines 3–202 | https://docs.frappe.io/erpnext/purchase-invoice |
| `acc.creditnote` | Issue a credit note | api | yes | irreversible | `docs/erpnext/erpnext-15.md` lines 715–814 | https://docs.frappe.io/erpnext/credit-note |
| `acc.debitnote` | Issue a debit note | api | yes | irreversible | `docs/erpnext/erpnext-19.md` lines 3–148 | https://docs.frappe.io/erpnext/debit-note |
| `acc.paymententry` | Record a payment entry | api | yes | irreversible | `docs/erpnext/erpnext-40.md` lines 353–551 | https://docs.frappe.io/erpnext/payment-entry |
| `acc.paymentrequest` | Send a payment request | api | yes | irreversible | `docs/erpnext/erpnext-41.md` lines 164–306 | https://docs.frappe.io/erpnext/payment-request |
| `acc.journalentry` | Post a journal entry | api | yes | irreversible | `docs/erpnext/erpnext-34.md` lines 395–566 | https://docs.frappe.io/erpnext/journal-entry |
| `acc.paymentterms` | Set payment terms | browser | yes | reversible | `docs/erpnext/erpnext-41.md` lines 402–476 | https://docs.frappe.io/erpnext/payment-terms |
| `acc.bankreconciliation` | Reconcile the bank | browser | yes | reversible | `docs/erpnext/erpnext-08.md` lines 735–822 | https://docs.frappe.io/erpnext/bank-reconciliation |
| `acc.paymentreconciliation` | Reconcile payments against invoices | browser | yes | reversible | `docs/erpnext/erpnext-41.md` lines 3–162 | https://docs.frappe.io/erpnext/payment-reconciliation |
| `acc.openingbalance` | Enter opening balances | browser | yes | reversible | `docs/erpnext/erpnext-39.md` lines 390–493 | https://docs.frappe.io/erpnext/opening-balance |
| `acc.openinginvoices` | Import opening invoices | browser | yes | reversible | `docs/erpnext/erpnext-39.md` lines 495–610 | https://docs.frappe.io/erpnext/opening-invoice-creation-tool |
| `acc.costcenter` | Set up cost centers | browser | yes | reversible | `docs/erpnext/erpnext-15.md` lines 3–98 | https://docs.frappe.io/erpnext/cost-center |
| `acc.budget` | Set and track a budget | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 541–701 | https://docs.frappe.io/erpnext/budget |
| `acc.dimensions` | Use accounting dimensions | browser | yes | reversible | `docs/erpnext/erpnext-01.md` lines 226–369 | https://docs.frappe.io/erpnext/accounting-dimensions |
| `acc.multicurrency` | Handle multi-currency accounting | guide | no | reversible | `docs/erpnext/erpnext-38.md` lines 147–322 | https://docs.frappe.io/erpnext/multi-currency-accounting |
| `acc.periodclose` | Close an accounting period | browser | yes | irreversible | `docs/erpnext/erpnext-42.md` lines 3–85 | https://docs.frappe.io/erpnext/period-closing-voucher |
| `acc.freeze` | Freeze accounting entries | browser | yes | reversible | `docs/erpnext/erpnext-27.md` lines 633–688 | https://docs.frappe.io/erpnext/freeze-accounting-entries |
| `acc.deferred` | Set up deferred revenue and expense | browser | yes | reversible | `docs/erpnext/erpnext-19.md` lines 252–410 | https://docs.frappe.io/erpnext/deferred-accounting |
| `acc.dunning` | Chase overdue invoices with dunning | api | yes | irreversible | `docs/erpnext/erpnext-23.md` lines 386–490 | https://docs.frappe.io/erpnext/dunning |
| `acc.soa` | Send a statement of accounts | browser | yes | irreversible | `docs/erpnext/erpnext-44.md` lines 568–672 | https://docs.frappe.io/erpnext/process-statement-of-accounts |
| `acc.subscription` | Bill customers on a subscription | api | yes | irreversible | `docs/erpnext/erpnext-61.md` lines 735–838 | https://docs.frappe.io/erpnext/subscription |
| `acc.assets` | Manage fixed assets | api | yes | reversible | `docs/erpnext/erpnext-07.md` lines 254–357 | https://docs.frappe.io/erpnext/asset |
| `acc.depreciation` | Run asset depreciation | browser | yes | irreversible | `docs/erpnext/erpnext-06.md` lines 407–498 | https://docs.frappe.io/erpnext/asset-depreciation |
| `acc.shareholder` | Track shareholders and share transfers | browser | yes | reversible | `docs/erpnext/erpnext-58.md` lines 67–140 | https://docs.frappe.io/erpnext/share-transfer |
| `tax.setup` | Set up taxes | browser | yes | reversible | `docs/erpnext/erpnext-57.md` lines 755–833 | https://docs.frappe.io/erpnext/setting-up-taxes |
| `tax.salestemplate` | Create a sales tax template | browser | yes | reversible | `docs/erpnext/erpnext-54.md` lines 510–706 | https://docs.frappe.io/erpnext/sales-taxes-and-charges-template |
| `tax.purchasetemplate` | Create a purchase tax template | browser | yes | reversible | `docs/erpnext/erpnext-48.md` lines 3–215 | https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template |
| `tax.itemtemplate` | Set item-level tax | browser | yes | reversible | `docs/erpnext/erpnext-33.md` lines 3–215 | https://docs.frappe.io/erpnext/item-tax-template |
| `tax.category` | Use tax categories | browser | yes | reversible | `docs/erpnext/erpnext-63.md` lines 3–195 | https://docs.frappe.io/erpnext/tax-category |
| `tax.rule` | Apply tax rules automatically | browser | yes | reversible | `docs/erpnext/erpnext-63.md` lines 566–765 | https://docs.frappe.io/erpnext/tax-rule |
| `tax.withholding` | Set up withholding tax | browser | yes | reversible | `docs/erpnext/erpnext-64.md` lines 3–239 | https://docs.frappe.io/erpnext/tax-withholding-category |
| `tax.uaevat` | Set up UAE VAT | browser | yes | reversible | `docs/erpnext/erpnext-66.md` lines 287–343 | https://docs.frappe.io/erpnext/uae-vat-setup |
| `tax.ksavat` | Set up KSA VAT reporting | browser | yes | reversible | `docs/erpnext/erpnext-58.md` lines 718–751 | https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

