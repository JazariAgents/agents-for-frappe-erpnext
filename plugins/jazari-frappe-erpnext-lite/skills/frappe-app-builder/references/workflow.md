# Build a Frappe app from scratch

Owner: **Imran** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the signed-in user has the roles for every step below

## Steps
1. **Create a new Frappe app** (`app.create`, bench mode)
   read: `docs/framework/framework-23.md` lines 396–492   (https://docs.frappe.io/framework/user/en/tutorial/create-an-app)
2. **Create a new site for an app** (`app.site.create`, bench mode)
   read: `docs/framework/framework-23.md` lines 179–394   (https://docs.frappe.io/framework/user/en/tutorial/create-a-site)
3. **Create a DocType** (`doctype.create`, browser mode)
   read: `docs/framework/framework-23.md` lines 3–177   (https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype)
4. **Pick the right field type** (`doctype.fieldtypes`, browser mode)
   read: `docs/framework/framework-08.md` lines 399–742   (https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes)
5. **Write controller methods** (`doctype.controller`, guide mode)
   read: `docs/framework/framework-22.md` lines 1015–1068   (https://docs.frappe.io/framework/user/en/tutorial/controller-methods)
6. **Run migrations after an update** (`bench.migrate`, bench mode) — SNAPSHOT FIRST, reversible
   read: `docs/framework/framework-12.md` lines 306–364   (https://docs.frappe.io/framework/user/en/bench/reference/migrate)

## Failure modes
- HTTP 403: the signed-in user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: this edition cannot reach it through MCP or frappectl; work through the Desk (`browser.md`)
