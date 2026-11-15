# Capabilities — Connect to a Frappe site

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `api.connect` | Test the site connection | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.token` | Authenticate with API key and secret | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.password` | Log in with username and password | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.oauth2` | Authenticate with OAuth 2 | api | no | reversible | `docs/framework/framework-03.md` lines 288–361 | https://docs.frappe.io/framework/oauth2 |
| `api.keys.generate` | Generate API key and secret for a user | browser | no | reversible | `docs/framework/framework-17.md` lines 246–291 | https://docs.frappe.io/framework/user/en/guides/integration/how_to_setup_token_based_auth |
| `api.doctype.meta` | Read DocType metadata to discover a site's schema | api | no | reversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.count` | Count records of a DocType | api | no | reversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.ratelimit` | Respect the site's rate limits | api | no | reversible | `docs/framework/framework-22.md` lines 333–393 | https://docs.frappe.io/framework/user/en/rate-limiting |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

