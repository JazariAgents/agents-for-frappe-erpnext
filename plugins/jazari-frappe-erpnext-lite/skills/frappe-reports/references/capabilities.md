# Capabilities — Reports, dashboards and Insights

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `rep.generalledger` | Read the general ledger | browser | no | reversible | `docs/erpnext/erpnext__general-ledger.md` | https://docs.frappe.io/erpnext/general-ledger |
| `rep.balancesheet` | Produce a balance sheet | browser | no | reversible | `docs/erpnext/erpnext__balance-sheet.md` | https://docs.frappe.io/erpnext/balance-sheet |
| `rep.pandl` | Produce a profit and loss report | browser | no | reversible | `docs/erpnext/erpnext__profit-and-loss-report.md` | https://docs.frappe.io/erpnext/profit-and-loss-report |
| `rep.cashflow` | Produce a cash flow report | browser | no | reversible | `docs/erpnext/erpnext__cash-flow-report.md` | https://docs.frappe.io/erpnext/cash-flow-report |
| `rep.receivables` | Age receivables and payables | browser | no | reversible | `docs/erpnext/erpnext__accounts-receivable-and-payable.md` | https://docs.frappe.io/erpnext/accounts-receivable-and-payable |
| `rep.accountingreports` | Use the standard accounting reports | browser | no | reversible | `docs/erpnext/erpnext__accounting-reports.md` | https://docs.frappe.io/erpnext/accounting-reports |
| `rep.salesanalytics` | Analyse sales | browser | no | reversible | `docs/erpnext/erpnext__sales-analytics.md` | https://docs.frappe.io/erpnext/sales-analytics |
| `rep.custom` | Build a custom report | browser | yes | reversible | `docs/erpnext/erpnext__making-custom-reports.md` | https://docs.frappe.io/erpnext/making-custom-reports |
| `rep.autoemail` | Email a report on a schedule | browser | yes | reversible | `docs/erpnext/erpnext__auto-email-reports.md` | https://docs.frappe.io/erpnext/auto-email-reports |
| `rep.dashboards` | Build ERPNext dashboards | browser | yes | reversible | `docs/erpnext/erpnext__erpnext-dashboards.md` | https://docs.frappe.io/erpnext/erpnext-dashboards |
| `ins.datasource` | Connect a data source in Insights | browser | yes | reversible | `docs/insights/insights__connect-data__add-data-source.md` | https://docs.frappe.io/insights/connect-data/add-data-source |
| `ins.query` | Write a query in Insights | browser | yes | reversible | `docs/insights/insights__querying__overview.md` | https://docs.frappe.io/insights/querying/overview |
| `ins.expressions` | Use expressions in a query | browser | yes | reversible | `docs/insights/insights__querying__expressions.md` | https://docs.frappe.io/insights/querying/expressions |
| `ins.chart` | Chart a result in Insights | browser | yes | reversible | `docs/insights/insights__charts__overview.md` | https://docs.frappe.io/insights/charts/overview |
| `ins.dashboard` | Publish an Insights dashboard | browser | yes | reversible | `docs/insights/insights__dashboards__overview.md` | https://docs.frappe.io/insights/dashboards/overview |
| `ins.sharing` | Share a dashboard and control access | browser | yes | reversible | `docs/insights/insights__dashboards__sharing-and-access-control.md` | https://docs.frappe.io/insights/dashboards/sharing-and-access-control |
| `ins.permissions` | Set Insights permissions | browser | yes | reversible | `docs/insights/insights__permissions-access-control__overview.md` | https://docs.frappe.io/insights/permissions-access-control/overview |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

