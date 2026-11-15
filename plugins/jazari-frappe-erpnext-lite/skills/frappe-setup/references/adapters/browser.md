# Interface adapter — Set up a company and go live

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

### Set up a company
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Setup > Company**, or type *Company* in the search bar at the top
- **Documented steps:**
  1. Open the Company tree view. Select New to create an independent Company, or select a group and use Add Child to create a subsidiary under it
  2. Enter the Company name, abbreviation, default currency, and Country
  3. Enable Is Group only for a parent used to organize child companies. A group does not post normal business transactions
  4. Select a Parent Company when the entity belongs to a group structure
  5. Save the Company and review the accounts, buying, selling, stock, manufacturing, and payroll defaults created for it
- **Full page, bundled offline:** `docs/erpnext/erpnext-14.md` lines 370–452  (https://docs.frappe.io/erpnext/company-setup)

### Set the fiscal year
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Setup > Fiscal Year**, or type *Fiscal Year* in the search bar at the top
- **Record type:** Fiscal Year
- **Documented steps:**
  1. Go to Home > Accounting > Accounting Masters > Fiscal Year
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-27.md` lines 341–410  (https://docs.frappe.io/erpnext/fiscal-year)

### Set up the chart of accounts
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Accounts > Chart of Accounts**, or type *Chart of Accounts* in the search bar at the top
- **Documented steps:**
  1. Select the parent group
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-13.md` lines 280–365  (https://docs.frappe.io/erpnext/chart-of-accounts)

### Configure currencies and exchange rates
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > Currency Exchange**, or type *Currency Exchange Settings* in the search bar at the top
- **Documented steps:**
  1. Open Currency Exchange Settings
  2. Confirm that Disabled is clear when provider fallback is required
  3. Select the Service Provider
  4. Review the API Endpoint and protocol
  5. Enter an Access Key only for a provider that requires one
  6. Review request Parameters and Result Key mappings
  7. Save, then test from a draft foreign-currency transaction
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-16.md` lines 275–424  (https://docs.frappe.io/erpnext/currency-exchange-settings)

### Configure naming series
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Data > Naming > Document Naming Settings**, or type *Document Naming Settings* in the search bar at the top
- **On this screen:** Choose the transaction in **Select Transaction**, edit **Series List for this Transaction**, then press **Update**.
- **Record type:** Document Naming Settings (called Naming Series before v14)
- **Documented steps:**
  1. Select the transaction for which you want to make the series. The system will update the current series in the text box
  2. Edit the series as required with unique prefixes for each series
  3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-38.md` lines 616–698  (https://docs.frappe.io/erpnext/naming-series)

### Add a letter head
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Printing > Letter Head**, or type *Letter Head* in the search bar at the top
- **Record type:** Letter Head
- **Documented steps:**
  1. Go to the Letter Head list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-35.md` lines 216–270  (https://docs.frappe.io/erpnext/letter-head)

### Connect an email account
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Email > Email Account**, or type *Email Account* in the search bar at the top
- **Record type:** Email Account
- **Documented steps:**
  1. Go to the Email Account list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-24.md` lines 3–129  (https://docs.frappe.io/erpnext/email-account)

### Create an email template
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Email > Email Template**, or type *Email Template* in the search bar at the top
- **Record type:** Email Template
- **Documented steps:**
  1. Go to the Email Template list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-24.md` lines 464–506  (https://docs.frappe.io/erpnext/email-template)

### Change system settings
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > System**, or type *System Settings* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-62.md` lines 540–698  (https://docs.frappe.io/erpnext/system-settings)

### Set global defaults
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > Global Defaults**, or type *Global Defaults* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-28.md` lines 252–344  (https://docs.frappe.io/erpnext/global-defaults)

### Assign documents automatically
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Automation > Assignment Rule**, or type *Assignment Rule* in the search bar at the top
- **Record type:** Assignment Rule
- **Documented steps:**
  1. Go to the Assignment Rule list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-07.md` lines 434–517  (https://docs.frappe.io/erpnext/assignment-rule)

### Repeat a document on a schedule
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Automation > Auto Repeat**, or type *Auto Repeat* in the search bar at the top
- **Record type:** Auto Repeat
- **Documented steps:**
  1. Go to Home > Settings > Automation > Auto Repeat > New
  2. Select the Reference Document Type, like Journal Entry or Sales Invoice, etc
  3. Select the Reference Document. This is the individual document that you want to repeat
  4. Set the Start Date and End Date (optional)
  5. Set the Frequency for creating repeatable documents
  6. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-07.md` lines 867–964  (https://docs.frappe.io/erpnext/auto-repeat)

### Send notifications on events
- **Path (checked on v16.55):** https://your-site/desk → type *Notification* in the search bar at the top and open the doctype
- **Record type:** Notification
- **Documented steps:**
  1. The completion date of a Task
  2. Expected Delivery Date of a Sales Order
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-39.md` lines 3–229  (https://docs.frappe.io/erpnext/notifications)

## What cannot be done in the interface

- Run the ERPNext getting-started checklist — an explanation, not an action (guide.md)
