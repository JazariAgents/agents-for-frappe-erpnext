# Capabilities — Set up a company and go live

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `setup.company` | Set up a company | browser | no | reversible | `docs/erpnext/erpnext-04.md` lines 1546–1628 | https://docs.frappe.io/erpnext/company-setup |
| `setup.getting.started` | Run the ERPNext getting-started checklist | guide | no | reversible | `docs/erpnext/erpnext-07.md` lines 3032–3076 | https://docs.frappe.io/erpnext/getting-started-with-erpnext |
| `setup.fiscalyear` | Set the fiscal year | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 2480–2549 | https://docs.frappe.io/erpnext/fiscal-year |
| `setup.coa` | Set up the chart of accounts | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 775–860 | https://docs.frappe.io/erpnext/chart-of-accounts |
| `setup.currency` | Configure currencies and exchange rates | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 3249–3398 | https://docs.frappe.io/erpnext/currency-exchange-settings |
| `setup.naming` | Configure naming series | browser | yes | reversible | `docs/erpnext/erpnext-10.md` lines 1806–1888 | https://docs.frappe.io/erpnext/naming-series |
| `setup.letterhead` | Add a letter head | browser | yes | reversible | `docs/erpnext/erpnext-09.md` lines 1845–1899 | https://docs.frappe.io/erpnext/letter-head |
| `setup.email` | Connect an email account | browser | yes | reversible | `docs/erpnext/erpnext-06.md` lines 2824–2950 | https://docs.frappe.io/erpnext/email-account |
| `setup.emailtemplate` | Create an email template | browser | yes | reversible | `docs/erpnext/erpnext-06.md` lines 3285–3327 | https://docs.frappe.io/erpnext/email-template |
| `setup.systemsettings` | Change system settings | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 2363–2521 | https://docs.frappe.io/erpnext/system-settings |
| `setup.globaldefaults` | Set global defaults | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 3078–3170 | https://docs.frappe.io/erpnext/global-defaults |
| `setup.assignmentrule` | Assign documents automatically | browser | yes | reversible | `docs/erpnext/erpnext-02.md` lines 2416–2499 | https://docs.frappe.io/erpnext/assignment-rule |
| `setup.autorepeat` | Repeat a document on a schedule | browser | yes | reversible | `docs/erpnext/erpnext-02.md` lines 2849–2946 | https://docs.frappe.io/erpnext/auto-repeat |
| `setup.notifications` | Send notifications on events | browser | yes | reversible | `docs/erpnext/erpnext-10.md` lines 2050–2276 | https://docs.frappe.io/erpnext/notifications |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

