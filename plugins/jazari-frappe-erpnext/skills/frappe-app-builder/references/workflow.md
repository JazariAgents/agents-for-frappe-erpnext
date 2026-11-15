# Build a Frappe app from scratch

Owner: **Imran** · verified: documentation; the screens, record types and API calls were checked on live sites on 2026-11-14

## Preconditions
- `.frappe/state.json` exists (run frappe-connect first)
- the site is reachable and the API user has the roles for every step below

## Steps
1. **Create a new Frappe app** (`app.create`, bench mode)
   read: `docs/framework/framework__user__en__tutorial__create-an-app.md`   (https://docs.frappe.io/framework/user/en/tutorial/create-an-app)
2. **Create a new site for an app** (`app.site.create`, bench mode)
   read: `docs/framework/framework__user__en__tutorial__create-a-site.md`   (https://docs.frappe.io/framework/user/en/tutorial/create-a-site)
3. **Create a DocType** (`doctype.create`, browser mode)
   read: `docs/framework/framework__user__en__tutorial__create-a-doctype.md`   (https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype)
4. **Pick the right field type** (`doctype.fieldtypes`, browser mode)
   read: `docs/framework/framework__user__en__basics__doctypes__fieldtypes.md`   (https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes)
5. **Write controller methods** (`doctype.controller`, guide mode)
   read: `docs/framework/framework__user__en__tutorial__controller-methods.md`   (https://docs.frappe.io/framework/user/en/tutorial/controller-methods)
6. **Run migrations after an update** (`bench.migrate`, bench mode) — SNAPSHOT FIRST, reversible
   read: `docs/framework/framework__user__en__bench__reference__migrate.md`   (https://docs.frappe.io/framework/user/en/bench/reference/migrate)

## Failure modes
- HTTP 403: the API user lacks the role for that DocType — say which role is missing, do not retry blindly
- HTTP 429: the site's rate limit was hit; back off and tell the user (see `api.ratelimit`)
- a submitted document cannot be edited: amend or cancel it instead, and say so before acting
- the site runs v14 or older: API v2 paths are unavailable (`/api/v2/` returns 404), fall back to `/api/resource/...` (v1)
