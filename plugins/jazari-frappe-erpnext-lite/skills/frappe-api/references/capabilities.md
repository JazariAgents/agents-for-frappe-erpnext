# Capabilities — REST API, webhooks and automation

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page. The first 23 were fetched on 2026-08-31 while this plugin was built; the four `api.automation.*` rows were added on 2026-11-14 from Frappe's newer pages and run on a live v16.56 site. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `api.connect` | Test the site connection | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.token` | Authenticate with API key and secret | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.password` | Log in with username and password | api | no | reversible | `docs/framework/framework-06.md` lines 660–1163 | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.oauth2` | Authenticate with OAuth 2 | api | no | reversible | `docs/framework/framework-03.md` lines 288–361 | https://docs.frappe.io/framework/oauth2 |
| `api.keys.generate` | Generate API key and secret for a user | browser | no | reversible | `docs/framework/framework-17.md` lines 246–291 | https://docs.frappe.io/framework/user/en/guides/integration/how_to_setup_token_based_auth |
| `api.doc.list` | List documents of any DocType | api | no | reversible | `docs/framework/framework-17.md` lines 494–559 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents |
| `api.doc.filter` | Filter and select fields in a list call | api | no | reversible | `docs/framework/framework-17.md` lines 494–559 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents |
| `api.doc.create` | Create a document through the API | api | no | reversible | `docs/framework/framework-17.md` lines 561–734 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.read` | Read one document through the API | api | no | reversible | `docs/framework/framework-17.md` lines 561–734 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.update` | Update a document through the API | api | yes | reversible | `docs/framework/framework-17.md` lines 561–734 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.delete` | Delete a document through the API | api | yes | recreate | `docs/framework/framework-17.md` lines 561–734 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.submit` | Submit a document through the API | api | yes | irreversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doc.cancel` | Cancel a submitted document | api | yes | irreversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.meta` | Read DocType metadata to discover a site's schema | api | no | reversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.count` | Count records of a DocType | api | no | reversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.method.rpc` | Call a whitelisted method on a document | api | yes | irreversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.file.upload` | Upload a file through the API | api | no | reversible | `docs/framework/framework-17.md` lines 373–492 | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.ratelimit` | Respect the site's rate limits | api | no | reversible | `docs/framework/framework-22.md` lines 333–393 | https://docs.frappe.io/framework/user/en/rate-limiting |
| `api.webhook.create` | Create a webhook on document events | browser | no | reversible | `docs/framework/framework-18.md` lines 3–148 | https://docs.frappe.io/framework/user/en/guides/integration/webhooks |
| `api.webhook.secret` | Secure a webhook with a shared secret | browser | no | reversible | `docs/framework/framework-18.md` lines 3–148 | https://docs.frappe.io/framework/user/en/guides/integration/webhooks |
| `api.realtime` | Publish and listen to realtime events | api | no | reversible | `docs/framework/framework-06.md` lines 384–658 | https://docs.frappe.io/framework/user/en/api/realtime |
| `api.background.jobs` | Queue and monitor background jobs | api | no | reversible | `docs/framework/framework-03.md` lines 1299–1508 | https://docs.frappe.io/framework/user/en/api/background_jobs |
| `api.scheduler` | Diagnose the scheduler | bench | no | reversible | `docs/framework/framework-11.md` lines 514–550 | https://docs.frappe.io/framework/user/en/bench/guides/diagnosing-the-scheduler |
| `api.automation.build` | Build an Automation Flow, switched off | api | no | reversible | `docs/framework/framework-01.md` lines 125–221 | https://docs.frappe.io/framework/automations |
| `api.automation.test` | Test-run an Automation Flow on a real record | api | no | reversible | `docs/framework/framework-01.md` lines 395–545 | https://docs.frappe.io/framework/automations/steps-and-actions |
| `api.automation.enable` | Turn an Automation Flow on or off | api | yes | irreversible | `docs/framework/framework-01.md` lines 547–667 | https://docs.frappe.io/framework/automations/triggers-and-conditions |
| `api.automation.runs` | Read an Automation Flow's run history | api | no | reversible | `docs/framework/framework-01.md` lines 125–221 | https://docs.frappe.io/framework/automations |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- Automation Flows require Frappe Framework **v16.36 or newer**. Turning one on is marked irreversible because what it sends or changes while on cannot be recalled; the switch itself can be turned off again.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

