# Interface adapter — Connect to a Frappe site

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

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Authenticate with OAuth 2
- **A client secret is the user's to copy.** If an OAuth Client is set up, the user reads its secret themselves; never read, copy or repeat it.
- **Path (checked on v16.55):** https://your-site/desk → **Framework > Integrations > Authentication > OAuth Client**, or type *OAuth Client* in the search bar at the top
- **Full page, bundled offline:** `docs/framework/framework__oauth2.md`  (https://docs.frappe.io/framework/oauth2)

### Generate API key and secret for a user
- **The user does this, never Claude.** Do not click Generate Keys or call `generate_keys` yourself, even with browser control, and never read, copy or repeat the secret.
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Users**, or type *User* in the search bar at the top
- **Documented steps:**
  1. Open the User list and click the user the API key should belong to
  2. Open the Settings tab on that user (skip if the form shows no tabs)
  3. Expand the API Access section and click Generate Keys
  4. The user copies the API Secret from the popup — it is shown once — and keeps it out of the chat; the API Key is in the same section
- **Full page, bundled offline:** `docs/framework/framework__user__en__guides__integration__how_to_setup_token_based_auth.md`  (https://docs.frappe.io/framework/user/en/guides/integration/how_to_setup_token_based_auth)

### Respect the site's rate limits
- **Path (checked on v16.55):** No screen: rate limits are set by the server administrator in `site_config.json` (see the page), and the agent only reads the limit headers.
- **Full page, bundled offline:** `docs/framework/framework__user__en__rate-limiting.md`  (https://docs.frappe.io/framework/user/en/rate-limiting)

## What cannot be done in the interface

- Test the site connection — an API call (api.md)
- Authenticate with API key and secret — an API call (api.md)
- Log in with username and password — an API call (api.md)
- Read DocType metadata to discover a site's schema — an API call (api.md)
- Count records of a DocType — an API call (api.md)
