# Interface adapter — Frappe Cloud — sites, benches, servers

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
| `https://frappecloud.com/dashboard` | the Frappe Cloud dashboard |

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

### Create a site on Frappe Cloud
- **Path:** open https://frappecloud.com/dashboard → **Sites** in the sidebar
- **Documented steps:**
  1. From the Sites tab on the dashboard, click on New Site
  2. Select the apps you want to install on your site
  3. Select the site version you want, and the site region you want
  4. Select the appropriate plan you want for your site. For more details visit our pricing page
  5. Choose a unique hostname for your site. Subdomain could be 5 to 32 characters long and contain lowercase alphabets, numbers, and hyphens. A subdomain can not start or end with hyphens
  6. It will take a few seconds for site creation depending on the apps you have chosen
  7. Click on Visit Site at the top of the page to access your site
  8. After site creation you will see a message, you can proceed to complete the setup wizard by clicking on login. You must log in and complete the setup wizard on your site. Analytics will be collected only after the setup is complete
- **Full page, bundled offline:** `docs/cloud/cloud-08.md` lines 153–179  (https://docs.frappe.io/cloud/sites/creating-a-new-site)

### Create a bench group on Frappe Cloud
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Creating a new bench* — the documentation page below shows the screen
- **Full page, bundled offline:** `docs/cloud/cloud-01.md` lines 234–270  (https://docs.frappe.io/cloud/benches/create-new)

### Update a bench group
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Updating a Bench* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-01.md` lines 709–834  (https://docs.frappe.io/cloud/benches/updating_a_bench)

### Add a custom app to a bench
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *How to install a custom app* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-01.md` lines 272–301  (https://docs.frappe.io/cloud/benches/custom-app)

### Create a server
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Creating new server* — the documentation page below shows the screen
- **Full page, bundled offline:** `docs/cloud/cloud-07.md` lines 54–142  (https://docs.frappe.io/cloud/servers/new)

### Back up a Frappe Cloud site
- **Path:** open https://frappecloud.com/dashboard → **Backups** in the sidebar
- **Full page, bundled offline:** `docs/cloud/cloud-08.md` lines 3–122  (https://docs.frappe.io/cloud/sites/backups)

### Move a site between benches or servers
- **Path:** open https://frappecloud.com/dashboard → **Migrations** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-07.md` lines 990–1035  (https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench)

### Add a custom domain to a Frappe Cloud site
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Custom Domains* — the documentation page below shows the screen
- **Documented steps:**
  1. Create DNS records from the dashboard of your domain provider. Follow one of the steps below
  2. After adding the DNS record, open your site dashboard
  3. From the site overview page, go to Domains card
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-08.md` lines 181–394  (https://docs.frappe.io/cloud/sites/custom-domains)

### Manage billing and payments
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Bill Payments* — the documentation page below shows the screen
- **Documented steps:**
  1. Go to Billing → Mode of payment and select UPI Autopay
  2. You will be redirected to the mandate setup page. Click "Setup Autopay" and complete the authorization via your UPI app
  3. A one-time ₹1 authorization charge is made to confirm mandate creation
  4. Once authorized, your UPI account will be auto-debited every month end
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/cloud/cloud-01.md` lines 873–934  (https://docs.frappe.io/cloud/billing/bill-payments)

### Connect to a bench over SSH
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *SSH Access* — the documentation page below shows the screen
- **Documented steps:**
  1. Output of your ssh command with the -vvvv option. Eg
- **Full page, bundled offline:** `docs/cloud/cloud-01.md` lines 467–707  (https://docs.frappe.io/cloud/benches/ssh)

### Install a marketplace app
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Installing an app* — the documentation page below shows the screen
- **Documented steps:**
  1. Click on Apps tab of your Site's dashboard
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-04.md` lines 945–1003  (https://docs.frappe.io/cloud/installing-an-app)

### Publish an app to the marketplace
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Publishing an App to Marketplace* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-05.md` lines 718–780  (https://docs.frappe.io/cloud/marketplace/publishing-an-app-to-marketplace)

### Change a site plan
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Change a site plan* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-04.md` lines 774–785  (https://docs.frappe.io/cloud/how-to-change-a-site-plan)

### Enable server scripts on a site
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Enable Server Script* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/cloud/cloud-03.md` lines 363–380  (https://docs.frappe.io/cloud/enable-server-script)

### Read site and bench logs
- **Path:** open https://frappecloud.com/dashboard (the Frappe Cloud dashboard) and find *Logs* — the documentation page below shows the screen
- **Documented steps:**
  1. web.log and web.err.log. These correspond to the STDOUT and STDERR streams of the web process. These handle the individual web requests to your site
  2. worker.log and worker.err.log. These correspond to the STDOUT and STDERR streams of the background workers. These run the background jobs
- **Full page, bundled offline:** `docs/cloud/cloud-05.md` lines 484–514  (https://docs.frappe.io/cloud/logs)

## What cannot be done in the interface

- Understand benches and bench groups — an explanation, not an action (guide.md)
