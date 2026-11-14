# Interface adapter — Support tickets and service levels

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |
| `https://your-site/helpdesk` | the Frappe Helpdesk interface |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Handle support tickets
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Ticket* — the documentation page below shows the screen
- **Record type:** HD Ticket
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__ticket.md`  (https://docs.frappe.io/helpdesk/ticket)

### Set service level agreements
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Service Level Agreement* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__service-level-agreement.md`  (https://docs.frappe.io/helpdesk/service-level-agreement)

### Route tickets to teams
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Team* — the documentation page below shows the screen
- **Record type:** HD Team
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__team.md`  (https://docs.frappe.io/helpdesk/team)

### Route tickets automatically
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Ticket Routing* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__ticket-routing.md`  (https://docs.frappe.io/helpdesk/ticket-routing)

### Set ticket priorities
- **Path:** open https://your-site/helpdesk → **HD Ticket Priority** in the sidebar
- **Record type:** HD Ticket Priority
- **Documented steps:**
  1. Navigate to Desk and open HD Ticket Priority (see above)
  2. Click + Add HD Ticket Priority
  3. Enter a name, choose a level, and optionally add a description
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__ticket-priority.md`  (https://docs.frappe.io/helpdesk/ticket-priority)

### Define ticket types
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Ticket Type* — the documentation page below shows the screen
- **Record type:** HD Ticket Type
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__ticket-type.md`  (https://docs.frappe.io/helpdesk/ticket-type)

### Invite and manage agents
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Agent* — the documentation page below shows the screen
- **Documented steps:**
  1. Click on "Create" button in the center
  2. A dialog will open, enter agent's email ID
  3. Click on "Send Invites", if you get an error like "Outgoing Email Error", this means you have not setup your email account, add it and try again
  4. They will be sent an email link to add there password, once they setup there password, they can login into your Helpdesk system
  5. Agent is added to your helpdesk system
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__agent.md`  (https://docs.frappe.io/helpdesk/agent)

### Answer faster with saved replies
- **Path:** open https://your-site/helpdesk → **Saved Replies** in the sidebar
- **Documented steps:**
  1. Go to the Saved Replies section in the settings modal and open a saved reply, or create a new one
  2. Scroll to the Actions table below the message
  3. Click Add action, pick an action from the dropdown, then pick its value
  4. Use the row menu on the right to delete a row
  5. Save the saved reply
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__saved-replies.md`  (https://docs.frappe.io/helpdesk/saved-replies)

### Publish knowledge base articles
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Knowledge Base* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__knowledge-base.md`  (https://docs.frappe.io/helpdesk/knowledge-base)

### Connect a support email account
- **Path:** open https://your-site/helpdesk (the Frappe Helpdesk interface) and find *Email Communication* — the documentation page below shows the screen
- **Documented steps:**
  1. Locate the Reply Button: On the Ticket page, find the "Reply" button, typically situated at the bottom of the page
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/helpdesk/helpdesk__email-communication.md`  (https://docs.frappe.io/helpdesk/email-communication)

### Track an issue in ERPNext
- **Path:** https://your-site/app → **Home > Support > Issues > Issue**
- **Record type:** Issue
- **Documented steps:**
  1. Go to the Issue list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__issue.md`  (https://docs.frappe.io/erpnext/issue)

### Handle a warranty claim
- **Path:** https://your-site/app → **Home > Support > Warranty > Warranty Claim**
- **Record type:** Warranty Claim
- **Documented steps:**
  1. Go to the Warranty Claim list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__warranty-claim.md`  (https://docs.frappe.io/erpnext/warranty-claim)

### Schedule maintenance visits
- **Path:** https://your-site/app → **Home > Support > Maintenance > Maintenance Schedule**
- **Record type:** Maintenance Schedule
- **Documented steps:**
  1. Go to the Maintenance Schedule, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__maintenance-schedule.md`  (https://docs.frappe.io/erpnext/maintenance-schedule)

