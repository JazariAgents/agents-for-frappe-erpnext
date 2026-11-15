# Capabilities — Reports, dashboards and Insights

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `rep.generalledger` | Read the general ledger | browser | no | reversible | `docs/erpnext/erpnext-28.md` lines 3–138 | https://docs.frappe.io/erpnext/general-ledger |
| `rep.balancesheet` | Produce a balance sheet | browser | no | reversible | `docs/erpnext/erpnext-08.md` lines 264–367 | https://docs.frappe.io/erpnext/balance-sheet |
| `rep.pandl` | Produce a profit and loss report | browser | no | reversible | `docs/erpnext/erpnext-45.md` lines 425–537 | https://docs.frappe.io/erpnext/profit-and-loss-report |
| `rep.cashflow` | Produce a cash flow report | browser | no | reversible | `docs/erpnext/erpnext-12.md` lines 695–787 | https://docs.frappe.io/erpnext/cash-flow-report |
| `rep.receivables` | Age receivables and payables | browser | no | reversible | `docs/erpnext/erpnext-03.md` lines 358–449 | https://docs.frappe.io/erpnext/accounts-receivable-and-payable |
| `rep.accountingreports` | Use the standard accounting reports | browser | no | reversible | `docs/erpnext/erpnext-02.md` lines 485–647 | https://docs.frappe.io/erpnext/accounting-reports |
| `rep.salesanalytics` | Analyse sales | browser | no | reversible | `docs/erpnext/erpnext-52.md` lines 3–131 | https://docs.frappe.io/erpnext/sales-analytics |
| `rep.custom` | Build a custom report | browser | yes | reversible | `docs/erpnext/erpnext-35.md` lines 897–930 | https://docs.frappe.io/erpnext/making-custom-reports |
| `rep.autoemail` | Email a report on a schedule | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 735–794 | https://docs.frappe.io/erpnext/auto-email-reports |
| `rep.dashboards` | Build ERPNext dashboards | browser | yes | reversible | `docs/erpnext/erpnext-25.md` lines 3–162 | https://docs.frappe.io/erpnext/erpnext-dashboards |
| `ins.datasource` | Connect a data source in Insights | browser | yes | reversible | `docs/insights/insights-01.md` lines 412–520 | https://docs.frappe.io/insights/connect-data/add-data-source |
| `ins.query` | Write a query in Insights | browser | yes | reversible | `docs/insights/insights-02.md` lines 694–745 | https://docs.frappe.io/insights/querying/overview |
| `ins.expressions` | Use expressions in a query | browser | yes | reversible | `docs/insights/insights-02.md` lines 3–369 | https://docs.frappe.io/insights/querying/expressions |
| `ins.chart` | Chart a result in Insights | browser | yes | reversible | `docs/insights/insights-01.md` lines 382–410 | https://docs.frappe.io/insights/charts/overview |
| `ins.dashboard` | Publish an Insights dashboard | browser | yes | reversible | `docs/insights/insights-01.md` lines 898–920 | https://docs.frappe.io/insights/dashboards/overview |
| `ins.sharing` | Share a dashboard and control access | browser | yes | reversible | `docs/insights/insights-01.md` lines 922–1005 | https://docs.frappe.io/insights/dashboards/sharing-and-access-control |
| `ins.permissions` | Set Insights permissions | browser | yes | reversible | `docs/insights/insights-01.md` lines 1302–1330 | https://docs.frappe.io/insights/permissions-access-control/overview |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

