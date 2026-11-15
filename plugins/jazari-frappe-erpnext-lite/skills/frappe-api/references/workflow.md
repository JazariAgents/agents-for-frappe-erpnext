# Connect Claude to a Frappe site

Owner: **Urwah** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Test the site connection** (`api.connect`, api mode)
   read: `docs/framework/framework-06.md` lines 660–1163   (https://docs.frappe.io/framework/user/en/api/rest)
2. **Sign in through Frappe's MCP connector or frappectl** (see **frappe-connect**; this edition never handles a key)
   read: `docs/framework/framework-06.md` lines 660–1163   (https://docs.frappe.io/framework/user/en/api/rest)
3. **Read DocType metadata to discover a site's schema** (`api.doctype.meta`, api mode)
   read: `docs/framework/framework-17.md` lines 373–492   (https://docs.frappe.io/framework/user/en/guides/integration/rest_api)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
