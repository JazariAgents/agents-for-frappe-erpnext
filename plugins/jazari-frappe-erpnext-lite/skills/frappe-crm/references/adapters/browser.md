# Interface adapter — CRM and the sales pipeline

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
| `https://your-site/crm` | the Frappe CRM interface |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Capture leads
- **Path:** open https://your-site/crm → **Leads** in the sidebar
- **Record type:** CRM Lead
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 1885–1963  (https://docs.frappe.io/crm/lead)

### Move deals through the pipeline
- **Path (checked on v16.55 with the app installed):** https://your-site/crm → **Deals** in the sidebar
- **On this screen:** On a first visit Frappe CRM opens an email setup screen; connect email or choose **Skip setup**.
- **Record type:** CRM Deal
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 1069–1144  (https://docs.frappe.io/crm/deal)

### Track CRM tasks
- **Path:** open https://your-site/crm (the Frappe CRM interface) and find *Task* — the documentation page below shows the screen
- **Record type:** CRM Task
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 2466–2506  (https://docs.frappe.io/crm/task)

### Keep notes on a deal
- **Path:** open https://your-site/crm → **Notes** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 2035–2072  (https://docs.frappe.io/crm/note)

### Track organizations
- **Path (checked on v16.55 with the app installed):** https://your-site/crm → **Organizations** in the sidebar
- **Record type:** CRM Organization
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 2110–2139  (https://docs.frappe.io/crm/organization)

### Reply with email templates
- **Path:** open https://your-site/crm (the Frappe CRM interface) and find *Email Template* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 1216–1249  (https://docs.frappe.io/crm/email-template)

### Log calls against a deal
- **Path:** open https://your-site/crm (the Frappe CRM interface) and find *Call Log* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 42–90  (https://docs.frappe.io/crm/call-log)

### Set a CRM service level agreement
- **Path (checked on v16.55 with the app installed):** https://your-site/crm → your name at the top left → **Settings** → **SLA Policies**
- **Documented steps:**
  1. Go to Settings > SLA Policies and click on +New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 2273–2318  (https://docs.frappe.io/crm/service-level-agreement)

### Customize deal statuses
- **Path (checked on v16.55 with the app installed):** https://your-site/desk → type *CRM Lead Status* or *CRM Deal Status* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 878–1049  (https://docs.frappe.io/crm/custom-statuses)

### Capture leads from a web form
- **Path (checked on v16.55 with the app installed):** https://your-site/crm → your name at the top left → **Settings** → **Forms**
- **Documented steps:**
  1. Open Settings → Forms. (You'll need the Sales Manager or System Manager role to see this.)
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 92–176  (https://docs.frappe.io/crm/capturing-leads/web-form)

### Invite your sales team
- **Path (checked on v16.55 with the app installed):** https://your-site/crm → your name at the top left → **Settings** → **Users**, then **Invite User**
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 1786–1816  (https://docs.frappe.io/crm/inviting-your-team)

### Message a contact on WhatsApp
- **Path (checked on v16.55):** **Needs Frappe's WhatsApp integration app**, which is not part of Frappe CRM and was not on the test site. Check `installed_apps` first; if it is missing, say so instead of looking for the screen
- **Documented steps:**
  1. Navigate to the WhatsApp Templates DocType
  2. Click on Add WhatsApp Template
  3. Fill in the required details for your template message
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/crm/crm-01.md` lines 2643–2709  (https://docs.frappe.io/crm/whatsapp)

### Work an opportunity in ERPNext
- **Path:** https://your-site/app → **Home > CRM > Sales Pipeline > Opportunity**
- **Record type:** Opportunity
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-10.md` lines 2809–2898  (https://docs.frappe.io/erpnext/opportunity)

### Run a campaign
- **Path:** https://your-site/app → **Home > CRM > Campaign > Campaign**
- **Record type:** Campaign
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-04.md` lines 3–79  (https://docs.frappe.io/erpnext/campaign)

### Send an email campaign
- **Path:** https://your-site/app → **Home > CRM > Campaign > Email Campaign**
- **Record type:** Email Campaign
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-06.md` lines 2952–3045  (https://docs.frappe.io/erpnext/email-campaign)

### Send a newsletter
- **Path (checked on v16.55):** **Not part of Frappe v16 itself**: Newsletter moved out of the framework into a separate app. Check `installed_apps` first; if it is missing, say so instead of looking for the screen
- **Record type:** Newsletter
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-10.md` lines 1890–1947  (https://docs.frappe.io/erpnext/newsletter)

