# Changelog

## 1.1.4 — the safety check matches records exactly (2026-11-14)

A security review of 1.1.3 found that the snapshot check could be too generous. It is now strict.

- **A snapshot covers only the records it holds.** Before, the check looked for the record's type and name
  anywhere in the snapshot's text, so a snapshot of `TODO-0012` also let through a change to `TODO-001`.
  It now reads the snapshot and matches each record's type and name exactly, in both the MCP guard and the
  API helper.
- **A change that does not name its record is refused.** Before, a submit or cancel that left out the
  record's name passed whenever any recent snapshot existed.
- **A method the plugin cannot recognise as read-only now asks you first** when it names no record. Before,
  a method was treated as read-only if `get_` appeared anywhere in its name.
- **If the guard itself fails, it asks you** instead of letting the call through.
- The snapshot rules now say each saved record must carry its type and name.

Tested: 23 of 23 guard checks and 25 of 25 helper checks pass, including each case above.

## 1.1.3 — everything checked against a live site (2026-11-14)

Every capability the plugin lists was checked against a live site, the main business workflows were run for real,
and the agents themselves were run on real requests to test the safety promises. This found real problems; they
are fixed here.

### Safety

- **Snapshots are now enforced, not just asked for.** With Frappe's MCP server connected, a test agent deleted a
  record straight through the MCP tool: no snapshot, no question. The plugin now ships hooks: in a folder connected to
  a Frappe site, every request is routed through the plugin's rules, and a change or delete through Frappe's MCP tools
  is refused unless that record was snapshotted in the last hour.
- **The API key can no longer leak.** In testing, an agent's own script put the whole key file into a request header
  and the error printed the key. The plugin now ships `frappe_call.py`, which reads the key itself, removes it from
  every output and error, refuses any change without `--write`, and refuses to change or delete a record that has no
  fresh snapshot. Every skill now uses it.
- Requests about records no module names (ToDos, notes, custom record types) now open the plugin's rules; before,
  they were handled without them.

### Wrong or missing instructions, fixed

- **167 screen paths** rewritten to where things really are on the v16 Desk (`/desk`). About 70 told the agent to
  "find" a documentation page title, such as "Introduction", that is not on any screen.
- **Linked documents.** Creating each document of a sale on its own leaves them unlinked: on the live site the order
  stayed 0% delivered. The guides now give ERPNext's 14 "create from the previous document" calls, each tested.
- **Journal Entry and Stock Reconciliation** cannot be submitted or cancelled with the standard call on v16; the
  guides now give the call that works, through the API, the MCP server and frappectl.
- **Credit notes** keep their own balance by default on v16, so the invoice still shows as unpaid. The guides say so.
- **Spreadsheet imports**: a tested recipe with a real dry run. An import whose preview shows a warning is accepted
  and then silently never runs; the guide now says to fix every warning first.
- **Naming series** is "Document Naming Settings" on v16, with a tested API recipe.
- **Partial restore** needs a partial backup and the file's full path; both now stated.
- **Not in ERPNext v16**: the QuickBooks migrator and the Saudi (KSA) VAT setup. The guides now say so instead of
  sending the agent to look for them.
- Records named by the user (POS Profile, Email Template and others) need the name in the request; now stated.
- The helper works from Git Bash on Windows, which rewrites `/api/...` arguments into Windows paths.

### Tested for the first time

- **Frappe HR, CRM, Helpdesk, Learning, Lending, Insights, Webshop, Builder and Wiki**, on a second site
  with thirteen Frappe apps. Every screen path in their guides now points to the real v16 screen.
- **Payroll**, start to finish: four salary slips submitted and their accounting entry made. HR 16 needs
  four things set up first (a submitted Holiday List Assignment, a Payable payroll account, an account on
  each salary component, and the employee list saved back after filling it); the guide now gives them, and
  says to re-read the run's status, because a run can fail behind a success reply.
- **Lending**, from loan product to repayment: 24 of 24 checks. Lending 16 needs a Loan Demand Offset
  Order and the company's collection sequences before the first product; the guide now gives the setup
  and the calls that make the loan, the disbursement and the repayment from the record before.
- **Attendance, leave and expense claims**, and the dashboard's People screen against the database.

### Said plainly where an app is needed

- WhatsApp, Newsletter and Blog are separate apps on v16, and the shop is the Webshop app (its settings
  are now Webshop Settings). The guides say to check that the app is installed first.
- Education, Drive and Studio were not on the test site; their paths are marked as the documentation's.

### Not tested

- Frappe Cloud (14 capabilities): it needs a Frappe Cloud account.
- bench production setup (nginx, HTTPS, domains) on a real server, and version 15 sites.


## 1.1.2 — the real frappectl (2026-11-14)

`frappectl`, Frappe's official command-line client, was the last connection route not yet run for real.
It now has been: v0.24.0 against the same live ERPNext 16.55 site.

### Tested

- The dashboard through `frappectl`, twice: a read-only profile made by its browser sign-in, and its
  environment-variable sign-in. Both gave exactly the figures of the API-key run, card for card.
- Every command in the plugin's `frappectl` guide: reading, listing every page, filters, reports, method
  calls, and create, update and delete on a harmless record.
- The read-only profile refused create and delete on the user's machine, before anything reached the site.

### Changed

- The sign-in command the plugin gives now includes `--read-only`. Without it the tool stops and asks.
- The guide now warns that the environment-variable sign-in is **not** read-only, and tells the agent to
  check `frappectl auth whoami` first.
- The guide's error table uses the tool's real messages, including a failed browser sign-in when a site
  announces the wrong address for itself.
- A clearer message from the dashboard when `frappectl`'s key is refused.

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

- `frappectl` has only been run against a stand-in, not the real tool. (Done in 1.1.2.)
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
