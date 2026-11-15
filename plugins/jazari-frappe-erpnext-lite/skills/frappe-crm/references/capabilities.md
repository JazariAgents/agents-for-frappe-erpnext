# Capabilities — CRM and the sales pipeline

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `crm.lead` | Capture leads | api | yes | reversible | `docs/crm/crm__lead.md` | https://docs.frappe.io/crm/lead |
| `crm.deal` | Move deals through the pipeline | api | yes | reversible | `docs/crm/crm__deal.md` | https://docs.frappe.io/crm/deal |
| `crm.task` | Track CRM tasks | api | yes | reversible | `docs/crm/crm__task.md` | https://docs.frappe.io/crm/task |
| `crm.note` | Keep notes on a deal | api | yes | reversible | `docs/crm/crm__note.md` | https://docs.frappe.io/crm/note |
| `crm.organization` | Track organizations | api | yes | reversible | `docs/crm/crm__organization.md` | https://docs.frappe.io/crm/organization |
| `crm.emailtemplate` | Reply with email templates | browser | yes | reversible | `docs/crm/crm__email-template.md` | https://docs.frappe.io/crm/email-template |
| `crm.telephony` | Log calls against a deal | browser | yes | reversible | `docs/crm/crm__call-log.md` | https://docs.frappe.io/crm/call-log |
| `crm.sla` | Set a CRM service level agreement | browser | yes | reversible | `docs/crm/crm__service-level-agreement.md` | https://docs.frappe.io/crm/service-level-agreement |
| `crm.status` | Customize deal statuses | browser | yes | reversible | `docs/crm/crm__custom-statuses.md` | https://docs.frappe.io/crm/custom-statuses |
| `crm.webform` | Capture leads from a web form | browser | yes | reversible | `docs/crm/crm__capturing-leads__web-form.md` | https://docs.frappe.io/crm/capturing-leads/web-form |
| `crm.team` | Invite your sales team | browser | yes | reversible | `docs/crm/crm__inviting-your-team.md` | https://docs.frappe.io/crm/inviting-your-team |
| `crm.whatsapp` | Message a contact on WhatsApp | browser | yes | irreversible | `docs/crm/crm__whatsapp.md` | https://docs.frappe.io/crm/whatsapp |
| `crm.opportunity` | Work an opportunity in ERPNext | api | yes | reversible | `docs/erpnext/erpnext__opportunity.md` | https://docs.frappe.io/erpnext/opportunity |
| `crm.campaign` | Run a campaign | browser | yes | reversible | `docs/erpnext/erpnext__campaign.md` | https://docs.frappe.io/erpnext/campaign |
| `crm.emailcampaign` | Send an email campaign | browser | yes | irreversible | `docs/erpnext/erpnext__email-campaign.md` | https://docs.frappe.io/erpnext/email-campaign |
| `crm.newsletter` | Send a newsletter | browser | yes | irreversible | `docs/erpnext/erpnext__newsletter.md` | https://docs.frappe.io/erpnext/newsletter |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

