# Capabilities — Set up a company and go live

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `setup.company` | Set up a company | browser | no | reversible | `docs/erpnext/erpnext-14.md` lines 370–452 | https://docs.frappe.io/erpnext/company-setup |
| `setup.getting.started` | Run the ERPNext getting-started checklist | guide | no | reversible | `docs/erpnext/erpnext-27.md` lines 388–432 | https://docs.frappe.io/erpnext/getting-started-with-erpnext |
| `setup.fiscalyear` | Set the fiscal year | browser | yes | reversible | `docs/erpnext/erpnext-26.md` lines 595–664 | https://docs.frappe.io/erpnext/fiscal-year |
| `setup.coa` | Set up the chart of accounts | browser | yes | reversible | `docs/erpnext/erpnext-13.md` lines 280–365 | https://docs.frappe.io/erpnext/chart-of-accounts |
| `setup.currency` | Configure currencies and exchange rates | browser | yes | reversible | `docs/erpnext/erpnext-16.md` lines 275–424 | https://docs.frappe.io/erpnext/currency-exchange-settings |
| `setup.naming` | Configure naming series | browser | yes | reversible | `docs/erpnext/erpnext-38.md` lines 472–554 | https://docs.frappe.io/erpnext/naming-series |
| `setup.letterhead` | Add a letter head | browser | yes | reversible | `docs/erpnext/erpnext-34.md` lines 526–580 | https://docs.frappe.io/erpnext/letter-head |
| `setup.email` | Connect an email account | browser | yes | reversible | `docs/erpnext/erpnext-23.md` lines 236–362 | https://docs.frappe.io/erpnext/email-account |
| `setup.emailtemplate` | Create an email template | browser | yes | reversible | `docs/erpnext/erpnext-23.md` lines 697–739 | https://docs.frappe.io/erpnext/email-template |
| `setup.systemsettings` | Change system settings | browser | yes | reversible | `docs/erpnext/erpnext-62.md` lines 464–622 | https://docs.frappe.io/erpnext/system-settings |
| `setup.globaldefaults` | Set global defaults | browser | yes | reversible | `docs/erpnext/erpnext-27.md` lines 434–526 | https://docs.frappe.io/erpnext/global-defaults |
| `setup.assignmentrule` | Assign documents automatically | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 434–517 | https://docs.frappe.io/erpnext/assignment-rule |
| `setup.autorepeat` | Repeat a document on a schedule | browser | yes | reversible | `docs/erpnext/erpnext-07.md` lines 867–964 | https://docs.frappe.io/erpnext/auto-repeat |
| `setup.notifications` | Send notifications on events | browser | yes | reversible | `docs/erpnext/erpnext-38.md` lines 716–942 | https://docs.frappe.io/erpnext/notifications |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

