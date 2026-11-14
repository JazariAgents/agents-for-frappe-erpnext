# Connect Claude to a Frappe site

Owner: **Urwah** · verified: docs (documentation, not a live probe)

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Test the site connection** (`api.connect`, api mode)
   read: `docs/framework/framework__user__en__api__rest.md`   (https://docs.frappe.io/framework/user/en/api/rest)
2. **Authenticate with API key and secret** (`api.auth.token`, api mode)
   read: `docs/framework/framework__user__en__api__rest.md`   (https://docs.frappe.io/framework/user/en/api/rest)
3. **Read DocType metadata to discover a site's schema** (`api.doctype.meta`, api mode)
   read: `docs/framework/framework__user__en__guides__integration__rest_api.md`   (https://docs.frappe.io/framework/user/en/guides/integration/rest_api)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
