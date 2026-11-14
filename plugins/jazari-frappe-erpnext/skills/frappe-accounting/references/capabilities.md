# Capabilities — Accounting, invoicing and tax

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `acc.salesinvoice` | Raise a sales invoice | api | yes | irreversible | `docs/erpnext/erpnext__sales-invoice.md` | https://docs.frappe.io/erpnext/sales-invoice |
| `acc.purchaseinvoice` | Record a purchase invoice | api | yes | irreversible | `docs/erpnext/erpnext__purchase-invoice.md` | https://docs.frappe.io/erpnext/purchase-invoice |
| `acc.creditnote` | Issue a credit note | api | yes | irreversible | `docs/erpnext/erpnext__credit-note.md` | https://docs.frappe.io/erpnext/credit-note |
| `acc.debitnote` | Issue a debit note | api | yes | irreversible | `docs/erpnext/erpnext__debit-note.md` | https://docs.frappe.io/erpnext/debit-note |
| `acc.paymententry` | Record a payment entry | api | yes | irreversible | `docs/erpnext/erpnext__payment-entry.md` | https://docs.frappe.io/erpnext/payment-entry |
| `acc.paymentrequest` | Send a payment request | api | yes | irreversible | `docs/erpnext/erpnext__payment-request.md` | https://docs.frappe.io/erpnext/payment-request |
| `acc.journalentry` | Post a journal entry | api | yes | irreversible | `docs/erpnext/erpnext__journal-entry.md` | https://docs.frappe.io/erpnext/journal-entry |
| `acc.paymentterms` | Set payment terms | browser | yes | reversible | `docs/erpnext/erpnext__payment-terms.md` | https://docs.frappe.io/erpnext/payment-terms |
| `acc.bankreconciliation` | Reconcile the bank | browser | yes | reversible | `docs/erpnext/erpnext__bank-reconciliation.md` | https://docs.frappe.io/erpnext/bank-reconciliation |
| `acc.paymentreconciliation` | Reconcile payments against invoices | browser | yes | reversible | `docs/erpnext/erpnext__payment-reconciliation.md` | https://docs.frappe.io/erpnext/payment-reconciliation |
| `acc.openingbalance` | Enter opening balances | browser | yes | reversible | `docs/erpnext/erpnext__opening-balance.md` | https://docs.frappe.io/erpnext/opening-balance |
| `acc.openinginvoices` | Import opening invoices | browser | yes | reversible | `docs/erpnext/erpnext__opening-invoice-creation-tool.md` | https://docs.frappe.io/erpnext/opening-invoice-creation-tool |
| `acc.costcenter` | Set up cost centers | browser | yes | reversible | `docs/erpnext/erpnext__cost-center.md` | https://docs.frappe.io/erpnext/cost-center |
| `acc.budget` | Set and track a budget | browser | yes | reversible | `docs/erpnext/erpnext__budget.md` | https://docs.frappe.io/erpnext/budget |
| `acc.dimensions` | Use accounting dimensions | browser | yes | reversible | `docs/erpnext/erpnext__accounting-dimensions.md` | https://docs.frappe.io/erpnext/accounting-dimensions |
| `acc.multicurrency` | Handle multi-currency accounting | guide | no | reversible | `docs/erpnext/erpnext__multi-currency-accounting.md` | https://docs.frappe.io/erpnext/multi-currency-accounting |
| `acc.periodclose` | Close an accounting period | browser | yes | irreversible | `docs/erpnext/erpnext__period-closing-voucher.md` | https://docs.frappe.io/erpnext/period-closing-voucher |
| `acc.freeze` | Freeze accounting entries | browser | yes | reversible | `docs/erpnext/erpnext__freeze-accounting-entries.md` | https://docs.frappe.io/erpnext/freeze-accounting-entries |
| `acc.deferred` | Set up deferred revenue and expense | browser | yes | reversible | `docs/erpnext/erpnext__deferred-accounting.md` | https://docs.frappe.io/erpnext/deferred-accounting |
| `acc.dunning` | Chase overdue invoices with dunning | api | yes | irreversible | `docs/erpnext/erpnext__dunning.md` | https://docs.frappe.io/erpnext/dunning |
| `acc.soa` | Send a statement of accounts | browser | yes | irreversible | `docs/erpnext/erpnext__process-statement-of-accounts.md` | https://docs.frappe.io/erpnext/process-statement-of-accounts |
| `acc.subscription` | Bill customers on a subscription | api | yes | irreversible | `docs/erpnext/erpnext__subscription.md` | https://docs.frappe.io/erpnext/subscription |
| `acc.assets` | Manage fixed assets | api | yes | reversible | `docs/erpnext/erpnext__asset.md` | https://docs.frappe.io/erpnext/asset |
| `acc.depreciation` | Run asset depreciation | browser | yes | irreversible | `docs/erpnext/erpnext__asset-depreciation.md` | https://docs.frappe.io/erpnext/asset-depreciation |
| `acc.shareholder` | Track shareholders and share transfers | browser | yes | reversible | `docs/erpnext/erpnext__share-transfer.md` | https://docs.frappe.io/erpnext/share-transfer |
| `tax.setup` | Set up taxes | browser | yes | reversible | `docs/erpnext/erpnext__setting-up-taxes.md` | https://docs.frappe.io/erpnext/setting-up-taxes |
| `tax.salestemplate` | Create a sales tax template | browser | yes | reversible | `docs/erpnext/erpnext__sales-taxes-and-charges-template.md` | https://docs.frappe.io/erpnext/sales-taxes-and-charges-template |
| `tax.purchasetemplate` | Create a purchase tax template | browser | yes | reversible | `docs/erpnext/erpnext__purchase-taxes-and-charges-template.md` | https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template |
| `tax.itemtemplate` | Set item-level tax | browser | yes | reversible | `docs/erpnext/erpnext__item-tax-template.md` | https://docs.frappe.io/erpnext/item-tax-template |
| `tax.category` | Use tax categories | browser | yes | reversible | `docs/erpnext/erpnext__tax-category.md` | https://docs.frappe.io/erpnext/tax-category |
| `tax.rule` | Apply tax rules automatically | browser | yes | reversible | `docs/erpnext/erpnext__tax-rule.md` | https://docs.frappe.io/erpnext/tax-rule |
| `tax.withholding` | Set up withholding tax | browser | yes | reversible | `docs/erpnext/erpnext__tax-withholding-category.md` | https://docs.frappe.io/erpnext/tax-withholding-category |
| `tax.uaevat` | Set up UAE VAT | browser | yes | reversible | `docs/erpnext/erpnext__uae-vat-setup.md` | https://docs.frappe.io/erpnext/uae-vat-setup |
| `tax.ksavat` | Set up KSA VAT reporting | browser | yes | reversible | `docs/erpnext/erpnext__simplified_ksa_vat_management_and_reporting.md` | https://docs.frappe.io/erpnext/simplified_ksa_vat_management_and_reporting |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

