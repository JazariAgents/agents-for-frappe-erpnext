# Capabilities — Website, shop and content

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `web.website` | Set up the website | browser | yes | reversible | `docs/erpnext/erpnext-68.md` lines 496–509 | https://docs.frappe.io/erpnext/website |
| `web.webpage` | Publish a web page | browser | yes | reversible | `docs/erpnext/erpnext-68.md` lines 3–128 | https://docs.frappe.io/erpnext/web-page |
| `web.blog` | Publish a blog post | browser | yes | reversible | `docs/erpnext/erpnext-10.md` lines 116–229 | https://docs.frappe.io/erpnext/blog-post |
| `web.theme` | Change the website theme | browser | yes | reversible | `docs/erpnext/erpnext-68.md` lines 421–494 | https://docs.frappe.io/erpnext/website-theme |
| `web.seo` | Set up SEO for the website | guide | no | reversible | `docs/erpnext/erpnext-30.md` lines 27–49 | https://docs.frappe.io/erpnext/how-to-setup-seo-for-your-website-on-erpnext |
| `web.shoppingcart` | Run the shopping cart | browser | yes | reversible | `docs/erpnext/erpnext-58.md` lines 590–638 | https://docs.frappe.io/erpnext/shopping-cart |
| `web.websiteitem` | Publish items to the shop | browser | yes | reversible | `docs/erpnext/erpnext-68.md` lines 511–615 | https://docs.frappe.io/erpnext/website_item |
| `web.builder` | Build pages with Frappe Builder | browser | yes | reversible | `docs/builder/builder-01.md` lines 242–270 | https://docs.frappe.io/builder/setting-up |
| `web.builderdata` | Bind data to a Builder page | browser | yes | reversible | `docs/builder/builder-01.md` lines 3–150 | https://docs.frappe.io/builder/data-script |
| `web.wiki` | Publish a wiki space | browser | yes | reversible | `docs/wiki/wiki-01.md` lines 198–240 | https://docs.frappe.io/wiki-v2/wiki-settings |
| `web.drive` | Share files with Frappe Drive | browser | yes | reversible | `docs/drive/drive-01.md` lines 49–71 | https://docs.frappe.io/drive/files |
| `web.driveteams` | Share a Drive team folder | browser | yes | reversible | `docs/drive/drive-01.md` lines 323–340 | https://docs.frappe.io/drive/teams |
| `web.driveaccess` | Control file access in Drive | browser | yes | reversible | `docs/drive/drive-01.md` lines 3–47 | https://docs.frappe.io/drive/file-access |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

