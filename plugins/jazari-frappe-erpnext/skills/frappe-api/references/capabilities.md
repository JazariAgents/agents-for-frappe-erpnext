# Capabilities — REST API, webhooks and automation

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page. The first 23 were fetched on 2026-08-31 while this plugin was built; the four `api.automation.*` rows were added on 2026-11-14 from Frappe's newer pages and run on a live v16.56 site. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `api.connect` | Test the site connection | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.token` | Authenticate with API key and secret | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.password` | Log in with username and password | api | no | reversible | `docs/framework/framework__user__en__api__rest.md` | https://docs.frappe.io/framework/user/en/api/rest |
| `api.auth.oauth2` | Authenticate with OAuth 2 | api | no | reversible | `docs/framework/framework__oauth2.md` | https://docs.frappe.io/framework/oauth2 |
| `api.keys.generate` | Generate API key and secret for a user | browser | no | reversible | `docs/framework/framework__user__en__guides__integration__how_to_setup_token_based_auth.md` | https://docs.frappe.io/framework/user/en/guides/integration/how_to_setup_token_based_auth |
| `api.doc.list` | List documents of any DocType | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api__listing_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents |
| `api.doc.filter` | Filter and select fields in a list call | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api__listing_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/listing_documents |
| `api.doc.create` | Create a document through the API | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api__manipulating_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.read` | Read one document through the API | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api__manipulating_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.update` | Update a document through the API | api | yes | reversible | `docs/framework/framework__user__en__guides__integration__rest_api__manipulating_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.delete` | Delete a document through the API | api | yes | recreate | `docs/framework/framework__user__en__guides__integration__rest_api__manipulating_documents.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api/manipulating_documents |
| `api.doc.submit` | Submit a document through the API | api | yes | irreversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doc.cancel` | Cancel a submitted document | api | yes | irreversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.meta` | Read DocType metadata to discover a site's schema | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.doctype.count` | Count records of a DocType | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.method.rpc` | Call a whitelisted method on a document | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.file.upload` | Upload a file through the API | api | no | reversible | `docs/framework/framework__user__en__guides__integration__rest_api.md` | https://docs.frappe.io/framework/user/en/guides/integration/rest_api |
| `api.ratelimit` | Respect the site's rate limits | api | no | reversible | `docs/framework/framework__user__en__rate-limiting.md` | https://docs.frappe.io/framework/user/en/rate-limiting |
| `api.webhook.create` | Create a webhook on document events | browser | no | reversible | `docs/framework/framework__user__en__guides__integration__webhooks.md` | https://docs.frappe.io/framework/user/en/guides/integration/webhooks |
| `api.webhook.secret` | Secure a webhook with a shared secret | browser | no | reversible | `docs/framework/framework__user__en__guides__integration__webhooks.md` | https://docs.frappe.io/framework/user/en/guides/integration/webhooks |
| `api.realtime` | Publish and listen to realtime events | api | no | reversible | `docs/framework/framework__user__en__api__realtime.md` | https://docs.frappe.io/framework/user/en/api/realtime |
| `api.background.jobs` | Queue and monitor background jobs | api | no | reversible | `docs/framework/framework__user__en__api__background_jobs.md` | https://docs.frappe.io/framework/user/en/api/background_jobs |
| `api.scheduler` | Diagnose the scheduler | bench | no | reversible | `docs/framework/framework__user__en__bench__guides__diagnosing-the-scheduler.md` | https://docs.frappe.io/framework/user/en/bench/guides/diagnosing-the-scheduler |
| `api.automation.build` | Build an Automation Flow, switched off | api | no | reversible | `docs/framework/framework__automations.md` | https://docs.frappe.io/framework/automations |
| `api.automation.test` | Test-run an Automation Flow on a real record | api | no | reversible | `docs/framework/framework__automations__steps-and-actions.md` | https://docs.frappe.io/framework/automations/steps-and-actions |
| `api.automation.enable` | Turn an Automation Flow on or off | api | yes | irreversible | `docs/framework/framework__automations__triggers-and-conditions.md` | https://docs.frappe.io/framework/automations/triggers-and-conditions |
| `api.automation.runs` | Read an Automation Flow's run history | api | no | reversible | `docs/framework/framework__automations.md` | https://docs.frappe.io/framework/automations |

## Version notes

- Endpoints under `/api/v2/` require Frappe Framework **v15 or newer**. On v14 and older use `/api/resource/...`.
- Automation Flows require Frappe Framework **v16.36 or newer**. Turning one on is marked irreversible because what it sends or changes while on cannot be recalled; the switch itself can be turned off again.
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

