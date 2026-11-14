# Interface adapter — Website, shop and content

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
| `https://your-site/builder` | Frappe Builder |
| `https://your-site/drive` | Frappe Drive |
| `https://your-site/wiki` | the Frappe Wiki interface |

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

### Set up the website
- **Path:** open https://your-site/app (the Desk) and find *Website Setup* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__website.md`  (https://docs.frappe.io/erpnext/website)

### Publish a web page
- **Path:** https://your-site/app → **Home > Website > Web Site > Web Page**
- **Record type:** Web Page
- **Documented steps:**
  1. Go to the Web Page list and click on New
  2. Enter a Title and add content in Main Section. The route will auto generated but you can change it
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__web-page.md`  (https://docs.frappe.io/erpnext/web-page)

### Publish a blog post
- **Path:** https://your-site/app → **Home > Website > Blog > Blog Post**
- **Record type:** Blog Post
- **Documented steps:**
  1. Go to the Blog Post list and click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__blog-post.md`  (https://docs.frappe.io/erpnext/blog-post)

### Change the website theme
- **Path:** https://your-site/app → **Home > Website > Setup > Website Theme**
- **Record type:** Website Theme
- **Documented steps:**
  1. Go to the Website Theme list and click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__website-theme.md`  (https://docs.frappe.io/erpnext/website-theme)

### Run the shopping cart
- **Path:** https://your-site/app → **E Commerce Settings > Shopping Cart**
- **Record type:** E Commerce Settings
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__shopping-cart.md`  (https://docs.frappe.io/erpnext/shopping-cart)

### Publish items to the shop
- **Path:** open https://your-site/app (the Desk) and search the awesomebar for **Website Item**
- **Record type:** Website Item
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__website_item.md`  (https://docs.frappe.io/erpnext/website_item)

### Build pages with Frappe Builder
- **Path:** open https://your-site/builder (Frappe Builder) and find *Learning Resources* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/builder/builder__setting-up.md`  (https://docs.frappe.io/builder/setting-up)

### Bind data to a Builder page
- **Path:** open https://your-site/builder (Frappe Builder) and find *Data Script* — the documentation page below shows the screen
- **Documented steps:**
  1. Set up a dynamic route in your web page settings (e.g., /blog/:blog_slug)
  2. In your data script, access the route parameter using frappe.form_dict.<parameter_name >
  3. Use this parameter to fetch the relevant data
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/builder/builder__data-script.md`  (https://docs.frappe.io/builder/data-script)

### Publish a wiki space
- **Path:** open https://your-site/wiki (the Frappe Wiki interface) and find *Wiki Settings* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/wiki/wiki-v2__wiki-settings.md`  (https://docs.frappe.io/wiki-v2/wiki-settings)

### Share files with Frappe Drive
- **Path:** open https://your-site/drive (Frappe Drive) and find *Files* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/drive/drive__files.md`  (https://docs.frappe.io/drive/files)

### Share a Drive team folder
- **Path:** open https://your-site/drive (Frappe Drive) and find *Teams* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/drive/drive__teams.md`  (https://docs.frappe.io/drive/teams)

### Control file access in Drive
- **Path:** open https://your-site/drive (Frappe Drive) and find *Sharing* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/drive/drive__file-access.md`  (https://docs.frappe.io/drive/file-access)

## What cannot be done in the interface

- Set up SEO for the website — an explanation, not an action (guide.md)
