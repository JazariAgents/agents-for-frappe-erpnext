# Capabilities — Set up a company and go live

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `setup.company` | Set up a company | browser | no | reversible | `docs/erpnext/erpnext__company-setup.md` | https://docs.frappe.io/erpnext/company-setup |
| `setup.getting.started` | Run the ERPNext getting-started checklist | guide | no | reversible | `docs/erpnext/erpnext__getting-started-with-erpnext.md` | https://docs.frappe.io/erpnext/getting-started-with-erpnext |
| `setup.fiscalyear` | Set the fiscal year | browser | yes | reversible | `docs/erpnext/erpnext__fiscal-year.md` | https://docs.frappe.io/erpnext/fiscal-year |
| `setup.coa` | Set up the chart of accounts | browser | yes | reversible | `docs/erpnext/erpnext__chart-of-accounts.md` | https://docs.frappe.io/erpnext/chart-of-accounts |
| `setup.currency` | Configure currencies and exchange rates | browser | yes | reversible | `docs/erpnext/erpnext__currency-exchange-settings.md` | https://docs.frappe.io/erpnext/currency-exchange-settings |
| `setup.naming` | Configure naming series | browser | yes | reversible | `docs/erpnext/erpnext__naming-series.md` | https://docs.frappe.io/erpnext/naming-series |
| `setup.letterhead` | Add a letter head | browser | yes | reversible | `docs/erpnext/erpnext__letter-head.md` | https://docs.frappe.io/erpnext/letter-head |
| `setup.email` | Connect an email account | browser | yes | reversible | `docs/erpnext/erpnext__email-account.md` | https://docs.frappe.io/erpnext/email-account |
| `setup.emailtemplate` | Create an email template | browser | yes | reversible | `docs/erpnext/erpnext__email-template.md` | https://docs.frappe.io/erpnext/email-template |
| `setup.systemsettings` | Change system settings | browser | yes | reversible | `docs/erpnext/erpnext__system-settings.md` | https://docs.frappe.io/erpnext/system-settings |
| `setup.globaldefaults` | Set global defaults | browser | yes | reversible | `docs/erpnext/erpnext__global-defaults.md` | https://docs.frappe.io/erpnext/global-defaults |
| `setup.assignmentrule` | Assign documents automatically | browser | yes | reversible | `docs/erpnext/erpnext__assignment-rule.md` | https://docs.frappe.io/erpnext/assignment-rule |
| `setup.autorepeat` | Repeat a document on a schedule | browser | yes | reversible | `docs/erpnext/erpnext__auto-repeat.md` | https://docs.frappe.io/erpnext/auto-repeat |
| `setup.notifications` | Send notifications on events | browser | yes | reversible | `docs/erpnext/erpnext__notifications.md` | https://docs.frappe.io/erpnext/notifications |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

