# Capabilities — CRM and the sales pipeline

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `crm.lead` | Capture leads | api | yes | reversible | `docs/crm/crm-01.md` lines 1885–1963 | https://docs.frappe.io/crm/lead |
| `crm.deal` | Move deals through the pipeline | api | yes | reversible | `docs/crm/crm-01.md` lines 1069–1144 | https://docs.frappe.io/crm/deal |
| `crm.task` | Track CRM tasks | api | yes | reversible | `docs/crm/crm-01.md` lines 2466–2506 | https://docs.frappe.io/crm/task |
| `crm.note` | Keep notes on a deal | api | yes | reversible | `docs/crm/crm-01.md` lines 2035–2072 | https://docs.frappe.io/crm/note |
| `crm.organization` | Track organizations | api | yes | reversible | `docs/crm/crm-01.md` lines 2110–2139 | https://docs.frappe.io/crm/organization |
| `crm.emailtemplate` | Reply with email templates | browser | yes | reversible | `docs/crm/crm-01.md` lines 1216–1249 | https://docs.frappe.io/crm/email-template |
| `crm.telephony` | Log calls against a deal | browser | yes | reversible | `docs/crm/crm-01.md` lines 42–90 | https://docs.frappe.io/crm/call-log |
| `crm.sla` | Set a CRM service level agreement | browser | yes | reversible | `docs/crm/crm-01.md` lines 2273–2318 | https://docs.frappe.io/crm/service-level-agreement |
| `crm.status` | Customize deal statuses | browser | yes | reversible | `docs/crm/crm-01.md` lines 878–1049 | https://docs.frappe.io/crm/custom-statuses |
| `crm.webform` | Capture leads from a web form | browser | yes | reversible | `docs/crm/crm-01.md` lines 92–176 | https://docs.frappe.io/crm/capturing-leads/web-form |
| `crm.team` | Invite your sales team | browser | yes | reversible | `docs/crm/crm-01.md` lines 1786–1816 | https://docs.frappe.io/crm/inviting-your-team |
| `crm.whatsapp` | Message a contact on WhatsApp | browser | yes | irreversible | `docs/crm/crm-01.md` lines 2643–2709 | https://docs.frappe.io/crm/whatsapp |
| `crm.opportunity` | Work an opportunity in ERPNext | api | yes | reversible | `docs/erpnext/erpnext-10.md` lines 2809–2898 | https://docs.frappe.io/erpnext/opportunity |
| `crm.campaign` | Run a campaign | browser | yes | reversible | `docs/erpnext/erpnext-04.md` lines 3–79 | https://docs.frappe.io/erpnext/campaign |
| `crm.emailcampaign` | Send an email campaign | browser | yes | irreversible | `docs/erpnext/erpnext-06.md` lines 2952–3045 | https://docs.frappe.io/erpnext/email-campaign |
| `crm.newsletter` | Send a newsletter | browser | yes | irreversible | `docs/erpnext/erpnext-10.md` lines 1890–1947 | https://docs.frappe.io/erpnext/newsletter |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

