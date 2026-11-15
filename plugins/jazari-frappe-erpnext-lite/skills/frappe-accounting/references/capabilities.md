# Capabilities — Accounting, invoicing and tax

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `acc.salesinvoice` | Raise a sales invoice | api | yes | irreversible | `docs/erpnext/erpnext-14.md` lines 306–524 | https://docs.frappe.io/erpnext/sales-invoice |
| `acc.purchaseinvoice` | Record a purchase invoice | api | yes | irreversible | `docs/erpnext/erpnext-12.md` lines 2353–2552 | https://docs.frappe.io/erpnext/purchase-invoice |
| `acc.creditnote` | Issue a credit note | api | yes | irreversible | `docs/erpnext/erpnext-04.md` lines 2876–2975 | https://docs.frappe.io/erpnext/credit-note |
| `acc.debitnote` | Issue a debit note | api | yes | irreversible | `docs/erpnext/erpnext-05.md` lines 1904–2049 | https://docs.frappe.io/erpnext/debit-note |
| `acc.paymententry` | Record a payment entry | api | yes | irreversible | `docs/erpnext/erpnext-11.md` lines 3–201 | https://docs.frappe.io/erpnext/payment-entry |
| `acc.paymentrequest` | Send a payment request | api | yes | irreversible | `docs/erpnext/erpnext-11.md` lines 497–639 | https://docs.frappe.io/erpnext/payment-request |
| `acc.journalentry` | Post a journal entry | api | yes | irreversible | `docs/erpnext/erpnext-09.md` lines 1322–1493 | https://docs.frappe.io/erpnext/journal-entry |
| `acc.paymentterms` | Set payment terms | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 735–809 | https://docs.frappe.io/erpnext/payment-terms |
| `acc.bankreconciliation` | Reconcile the bank | browser | yes | reversible | `docs/erpnext/erpnext-03.md` lines 237–324 | https://docs.frappe.io/erpnext/bank-reconciliation |
| `acc.paymentreconciliation` | Reconcile payments against invoices | browser | yes | reversible | `docs/erpnext/erpnext-11.md` lines 336–495 | https://docs.frappe.io/erpnext/payment-reconciliation |
| `acc.openingbalance` | Enter opening balances | browser | yes | reversible | `docs/erpnext/erpnext-10.md` lines 2437–2540 | https://docs.frappe.io/erpnext/opening-balance |
| `acc.openinginvoices` | Import opening invoices | browser | yes | reversible | `docs/erpnext/erpnext-10.md` lines 2542–2657 | https://docs.frappe.io/erpnext/opening-invoice-creation-tool |
| `acc.costcenter` | Set up cost centers | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 2164–2259 | https://docs.frappe.io/erpnext/cost-center |
| `acc.budget` | Set and track a budget | browser | yes | reversible | `docs/erpnext/erpnext-03.md` lines 2568–2728 | https://docs.frappe.io/erpnext/budget |
| `acc.dimensions` | Use accounting dimensions | browser | yes | reversible | `docs/erpnext/erpnext-01.md` lines 226–369 | https://docs.frappe.io/erpnext/accounting-dimensions |
| `acc.multicurrency` | Handle multi-currency accounting | guide | no | reversible | `docs/erpnext/erpnext-10.md` lines 1337–1512 | https://docs.frappe.io/erpnext/multi-currency-accounting |
| `acc.periodclose` | Close an accounting period | browser | yes | irreversible | `docs/erpnext/erpnext-11.md` lines 1127–1209 | https://docs.frappe.io/erpnext/period-closing-voucher |
| `acc.freeze` | Freeze accounting entries | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 2772–2827 | https://docs.frappe.io/erpnext/freeze-accounting-entries |
| `acc.deferred` | Set up deferred revenue and expense | browser | yes | reversible | `docs/erpnext/erpnext-05.md` lines 2153–2311 | https://docs.frappe.io/erpnext/deferred-accounting |
| `acc.dunning` | Chase overdue invoices with dunning | api | yes | irreversible | `docs/erpnext/erpnext-06.md` lines 2313–2417 | https://docs.frappe.io/erpnext/dunning |
| `acc.soa` | Send a statement of accounts | browser | yes | irreversible | `docs/erpnext/erpnext-12.md` lines 316–420 | https://docs.frappe.io/erpnext/process-statement-of-accounts |
| `acc.subscription` | Bill customers on a subscription | api | yes | irreversible | `docs/erpnext/erpnext-16.md` lines 1721–1824 | https://docs.frappe.io/erpnext/subscription |
| `acc.assets` | Manage fixed assets | api | yes | reversible | `docs/erpnext/erpnext-02.md` lines 2236–2339 | https://docs.frappe.io/erpnext/asset |
| `acc.depreciation` | Run asset depreciation | browser | yes | irreversible | `docs/erpnext/erpnext-02.md` lines 1445–1536 | https://docs.frappe.io/erpnext/asset-depreciation |
| `acc.shareholder` | Track shareholders and share transfers | browser | yes | reversible | `docs/erpnext/erpnext-15.md` lines 1605–1678 | https://docs.frappe.io/erpnext/share-transfer |
| `tax.setup` | Set up taxes | browser | yes | reversible | `docs/erpnext/erpnext-15.md` lines 1252–1330 | https://docs.frappe.io/erpnext/setting-up-taxes |
| `tax.salestemplate` | Create a sales tax template | browser | yes | reversible | `docs/erpnext/erpnext-14.md` lines 1838–2034 | https://docs.frappe.io/erpnext/sales-taxes-and-charges-template |
| `tax.purchasetemplate` | Create a purchase tax template | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 3–215 | https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template |
| `tax.itemtemplate` | Set item-level tax | browser | yes | reversible | `docs/erpnext/erpnext-09.md` lines 231–443 | https://docs.frappe.io/erpnext/item-tax-template |
| `tax.category` | Use tax categories | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 2659–2851 | https://docs.frappe.io/erpnext/tax-category |
| `tax.rule` | Apply tax rules automatically | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 3–202 | https://docs.frappe.io/erpnext/tax-rule |
| `tax.withholding` | Set up withholding tax | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 204–440 | https://docs.frappe.io/erpnext/tax-withholding-category |
| `tax.uaevat` | Set up UAE VAT | browser | yes | reversible | `docs/erpnext/erpnext-17.md` lines 2104–2160 | https://docs.frappe.io/erpnext/uae-vat-setup |
| `tax.ksavat` | Set up KSA VAT reporting | browser | yes | reversible | `docs/erpnext/erpnext-15.md` lines 2256–2289 | https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

