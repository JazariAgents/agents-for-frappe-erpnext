# Capabilities — Connect to a Frappe site

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `api.connect` | Test the site connection | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.token` | Authenticate with API key and secret | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.password` | Log in with username and password | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.oauth2` | Authenticate with OAuth 2 | api | no | reversible | `docs/framework/framework__oauth2.md` | https://docs.frappe.io/framework/oauth2 |
| `api.keys.generate` | Generate API key and secret for a user | browser | no | reversible | `docs/framework/framework__user__en__guides__integration__how_to_setup_token_based_auth.md` | https://docs.frappe.io/framework/user/en/guides/integration/how_to_setup_token_based_auth |
| `api.doctype.meta` | Read DocType metadata to discover a site's schema | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.count` | Count records of a DocType | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.ratelimit` | Respect the site's rate limits | api | no | reversible | `docs/framework/framework__user__en__rate-limiting.md` | https://docs.frappe.io/framework/user/en/rate-limiting |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

