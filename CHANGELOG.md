# Changelog

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

### Known gaps

- Not yet run end to end against a live Frappe site, real `frappectl` or a real MCP connection.
- The bundled documentation and capability tables date from 2026-08-31 (Frappe 16.32, ERPNext 16.33).
  Ten later changes are listed in `compat.json` as not covered, including Automation rules and the
  rebuilt BOM Creator.
- The HTML manual still describes the 1.0 connection flow and does not mention the dashboard.

## 1.0.0 — 2026-08-31

Private release. 22 skills built from 1,607 pages of official Frappe documentation.
