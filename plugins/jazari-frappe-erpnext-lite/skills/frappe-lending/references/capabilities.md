# Capabilities — Loans and lending

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `loan.product` | Set up a loan product | browser | yes | reversible | `docs/lending/lending__loan-product.md` | https://docs.frappe.io/lending/loan-product |
| `loan.application` | Process a loan application | browser | yes | reversible | `docs/lending/lending__loan-application.md` | https://docs.frappe.io/lending/loan-application |
| `loan.disbursement` | Disburse a loan | browser | yes | irreversible | `docs/lending/lending__loan-disbursement.md` | https://docs.frappe.io/lending/loan-disbursement |
| `loan.repayment` | Record a loan repayment | browser | yes | irreversible | `docs/lending/lending__loan-repayment.md` | https://docs.frappe.io/lending/loan-repayment |
| `loan.interest` | Accrue interest | browser | yes | irreversible | `docs/lending/lending__loan-interest-accrual.md` | https://docs.frappe.io/lending/loan-interest-accrual |
| `loan.security` | Manage loan security | browser | yes | reversible | `docs/lending/lending__loan-security.md` | https://docs.frappe.io/lending/loan-security |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

