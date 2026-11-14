# Changelog

## 1.1.1 — tested on a live site (2026-11-14)

The three gaps listed under 1.1.0 are closed: the plugin was run on a real ERPNext site, the ten newer
Frappe changes are covered, and the manual is rewritten.

### Tested

- Run against ERPNext 16.55 on Frappe 16.56 (Frappe's official Docker image, a throwaway company with six
  months of trading). Every dashboard figure was compared with the database and matched.
- The 27 API call shapes the skills share, Frappe's built-in MCP server (13 tools), eight standard reports
  and one Automation Flow were all run for real.

### Fixed, found by that test

- **Paging on API v2.** The skills told the agent to page with `limit_page_length` and `limit_start`. On
  `/api/v2/` those words are ignored without an error, so a long list would have come back as its first 20
  rows only. The guidance now gives `limit` and `start` for v2 and the older words for v1.
- **Validation errors on API v2** are in `errors[].message`, not `_server_messages`.
- **Reports.** The reports skill said reports could only be run by clicking. They can be run through the
  API; the skill now has the call and the filters that were tested.
- **Dashboard:** two "not available" notes named the wrong record type; Guest was counted as a user; a
  smoothed line could dip below zero; count charts showed gridlines at 0.3 and 0.8; a key refused by a
  Restrict IP list was reported as a bad key; and a site without Frappe HR now says so in one clear line.
- **BOM Creator** was labelled reversible. Its Create BOMs button submits a BOM for every assembly, so it
  is now labelled irreversible.

### New

- **Automation Flows** (Frappe 16.36 and later): build one switched off, test-run it on a real record,
  turn it on only after a yes. Includes the exact action names the site accepts, which differ from the
  labels on screen.
- **The rebuilt BOM Creator** (ERPNext 16.53), and how to tell it from the older screen.
- **Group by Dimension** for Profit and Loss and Balance Sheet (ERPNext 16.51).
- Guidance for the wider permission checks (ERPNext 16.36 and 16.50), Restrict IP on API keys
  (Frappe 16.33), per-method rate limits (Frappe 16.53), the renamed manufacturing option (ERPNext 16.52),
  the removed IRS 1099 print button (ERPNext 16.35) and Chrome as the default PDF engine (Frappe 16.55).
- Five newer official pages added to the bundled documentation: 1,612 pages in total.

### Changed

- The HTML manual is rewritten in English and Arabic for the new install commands, the four ways to
  connect, the dashboard, the Agents page, automations, updating, and what was and was not tested.

### Still open

- `frappectl` has only been run against a stand-in, not the real tool.
- Frappe HR, CRM, Helpdesk, Insights, Lending and Learning were not on the test site.
- The individual walkthroughs trace to documentation and were not each run.

## 1.1.0 — first public release (prepared 2026-11-14)

The first version published on GitHub, under the MIT licence.

### New

- **Connects through Frappe's own tools.** The built-in MCP server (Frappe v16.53 and later) and the
  `frappectl` command-line client are tried first; an API key is the fallback. Two new guides map every
  call the skills describe onto those tools.
- **Dashboard.** A new skill builds a one-page, read-only dashboard from a live site: Overview, Finance,
  Sales, People, System and Agents. English and Arabic. Works through an API key or a `frappectl` profile.
- **Agents page.** Every skill now writes one line per finished request to a local activity log, and the
  dashboard summarises it: requests handled, records changed, snapshot coverage, refusals.
- **Version check.** On connecting, the plugin compares itself with the site's Frappe and ERPNext versions
  and says what has changed since it was built.

### Changed

- The agents now carry the Jazari Agents cast names: Rukaz, Wafir, Imran, Dhukhr, Mizan, Zahir, Hazim,
  Anees and Urwah.
- Renamed from "Frappe Agents" to "Jazari Agents for Frappe & ERPNext"; plugin id `jazari-frappe-erpnext`.
- Licence changed from commercial to MIT.

### Fixed

- API v2 was described as needing Frappe v16; it is available from v15. Corrected in 109 places.
- Restoring a site from a backup was labelled reversible; it replaces the whole database and is now
  labelled irreversible, with a fresh backup required first.
- Password login is now marked as reference only: the plugin never handles a password.
- 61 step-by-step walkthroughs stopped after four steps; they now carry the full procedure from their
  documentation page.
- A wrong "see above" reference in the restore skill.

### Known gaps (closed in 1.1.1, except the real `frappectl`)

- Not yet run end to end against a live Frappe site, real `frappectl` or a real MCP connection.
- The bundled documentation and capability tables date from 2026-08-31 (Frappe 16.32, ERPNext 16.33).
  Ten later changes are listed in `compat.json` as not covered, including Automation rules and the
  rebuilt BOM Creator.
- The HTML manual still describes the 1.0 connection flow and does not mention the dashboard.

## 1.0.0 — 2026-08-31

Private release. 22 skills built from 1,607 pages of official Frappe documentation.
