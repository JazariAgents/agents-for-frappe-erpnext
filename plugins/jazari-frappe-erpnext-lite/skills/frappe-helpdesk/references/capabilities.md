# Capabilities — Support tickets and service levels

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `hd.ticket` | Handle support tickets | api | yes | reversible | `docs/helpdesk/helpdesk-04.md` lines 500–534 | https://docs.frappe.io/helpdesk/ticket |
| `hd.sla` | Set service level agreements | browser | yes | reversible | `docs/helpdesk/helpdesk-03.md` lines 684–944 | https://docs.frappe.io/helpdesk/service-level-agreement |
| `hd.team` | Route tickets to teams | browser | yes | reversible | `docs/helpdesk/helpdesk-04.md` lines 222–251 | https://docs.frappe.io/helpdesk/team |
| `hd.routing` | Route tickets automatically | browser | yes | reversible | `docs/helpdesk/helpdesk-04.md` lines 314–379 | https://docs.frappe.io/helpdesk/ticket-routing |
| `hd.priority` | Set ticket priorities | browser | yes | reversible | `docs/helpdesk/helpdesk-04.md` lines 253–312 | https://docs.frappe.io/helpdesk/ticket-priority |
| `hd.tickettype` | Define ticket types | browser | yes | reversible | `docs/helpdesk/helpdesk-04.md` lines 467–498 | https://docs.frappe.io/helpdesk/ticket-type |
| `hd.agent` | Invite and manage agents | browser | yes | reversible | `docs/helpdesk/helpdesk-01.md` lines 3–51 | https://docs.frappe.io/helpdesk/agent |
| `hd.savedreplies` | Answer faster with saved replies | browser | yes | reversible | `docs/helpdesk/helpdesk-03.md` lines 487–682 | https://docs.frappe.io/helpdesk/saved-replies |
| `hd.kb` | Publish knowledge base articles | browser | yes | reversible | `docs/helpdesk/helpdesk-02.md` lines 754–791 | https://docs.frappe.io/helpdesk/knowledge-base |
| `hd.email` | Connect a support email account | browser | yes | reversible | `docs/helpdesk/helpdesk-01.md` lines 890–961 | https://docs.frappe.io/helpdesk/email-communication |
| `hd.issue` | Track an issue in ERPNext | api | yes | reversible | `docs/erpnext/erpnext-32.md` lines 359–494 | https://docs.frappe.io/erpnext/issue |
| `hd.warranty` | Handle a warranty claim | api | yes | reversible | `docs/erpnext/erpnext-67.md` lines 747–848 | https://docs.frappe.io/erpnext/warranty-claim |
| `hd.maintenance` | Schedule maintenance visits | api | yes | reversible | `docs/erpnext/erpnext-35.md` lines 742–791 | https://docs.frappe.io/erpnext/maintenance-schedule |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

