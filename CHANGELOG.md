# Changelog

## Lite 1.1.12 — the documentation in fewer files (2026-11-15)

The Lite edition only; the full edition stays at 1.1.11.

- Claude's plugin directory holds a plugin with more than 512 files for review. The Lite edition had 1,752,
  almost all of them the 1,612 bundled documentation pages. The pages are now packed into 146 files of about
  48 KB, each page whole and marked with its original name. Every reference in the skills, and
  `docs/INDEX.md`, says which file and which lines hold a page, so Claude still reads just that page. The
  plugin is now 284 files.
- Two Frappe Cloud pages showed SSH key file paths (`~/.ssh/id_rsa`), which the directory reads as a plugin
  reaching for a credential. In the Lite edition those paths are replaced with a description; `NOTICE.md`
  says so.

## 1.1.11 — a Lite edition for Claude's plugin directory, and fixes from its review (2026-11-15)

**New: Jazari Agents for Frappe & ERPNext Lite** (`jazari-frappe-erpnext-lite`), in `plugins/jazari-frappe-erpnext-lite`.
Anthropic's plugin directory accepts plugins that carry code only from organizations it has verified, so the
Lite edition carries none: no hooks, no scripts, no HTML. It has the same 23 skills, nine agents and 1,612
bundled pages, plus `frappe-safe-change`, which holds the safety steps. It never handles an API key: it
connects through Frappe's MCP server, frappectl or the Desk. Its rules are instructions Claude follows, not
locks in code. When you connect, it asks to add a short note to `CLAUDE.md` in your folder: in real sessions,
without that note quick changes went straight to the site, and with it every change waited for a snapshot and
your reply. It is generated from the full edition by a build script, so the two stay in step. Install one
edition, not both.

**Fixed in both editions** (found by an independent review of the Lite edition; the full edition had the same
text):

- Generating a user's API key, and creating an OAuth client, are now the user's job only. The pages had listed
  both as reachable over the API, which would have put a secret in front of Claude.
- A restore now reads the record first and stops if someone changed it after the snapshot, saves a snapshot of
  the current state before asking, checks again just before writing, keeps the IDs of child-table rows (so
  links to them hold), and says exactly which fields are written back. A deleted record is brought back with
  Frappe's own Deleted Document restore where one exists (on an auto-named DocType it gets a new ID; tested).
- Every change re-reads the record just before it is made; if it changed while you were being asked, the
  snapshot and the question are repeated. The audit log records each record's new `modified` time.
- `bench --site <site> show-config` prints the database password and the encryption key, so the agent no longer
  runs it: you do, and tell it the one setting it needs. `bench new-site` is given to you to run, so its
  passwords never pass through the chat.
- Changes through frappectl now follow the same steps as changes through the MCP server: snapshot (attachments
  included, with `frappectl file download`), ask, and act only after your reply. In the full edition the code
  locks cover the MCP tools and the API helper; frappectl relies on these steps in both editions.
- Switching on an Automation Flow is a change to an existing record: snapshot first, then your reply.
- A data import sample is followed by a file with the remaining rows, not the full file again, which would have
  imported the first rows twice.
- Three safety classes corrected: calling a whitelisted method on a document, loading opening stock and
  importing advances and balances are now marked as changes that cannot simply be undone.
- One page said frappectl-free MCP users cannot run reports; `call_method` with `frappe.desk.query_report.run`
  does (checked on a live site).

## 1.1.10 — the no-Python fallback asks everywhere (2026-11-14)

- In 1.1.9 the fallback that asks you when Python is missing could only see the current folder, so from a
  subfolder of the workspace it stayed silent. It no longer looks at folders at all: without Python, any
  call shaped like a change to a Frappe site (it names a doctype, or it is Frappe's `call_method`) is put
  to you first, wherever the session is. A tool of the same name from another server is left alone.

## 1.1.9 — what the plugin directory's own check asked for (2026-11-14)

Anthropic's submission portal runs a stricter check than its published checklist. It found four blocking
issues, all in one file added in 1.1.7. They are fixed.

- The fallback that asks you when Python is missing looked in the folders above the current one. The
  directory does not allow a hook script to name a path outside the plugin, so it now looks in the current
  folder only. With Python installed, nothing changes: the hook still finds the workspace from a subfolder.
- The safety hook's code now shows plainly that it can only refuse a call or ask you. It never approves a
  call and never changes one.
- The plugin has a listing icon.

## 1.1.8 — an install command that works on every machine (2026-11-14)

- The install command now uses the repository's full web address. The short form
  (`JazariAgents/agents-for-frappe-erpnext`) made Claude Code try SSH on machines that have an SSH key but
  have never connected to GitHub with it, and the install failed there with "Host key verification
  failed". Found on a fresh install test; the full address installed cleanly on the same machine.
- Nothing else changed from 1.1.7. If you already added the marketplace, you do not need to add it again.

## 1.1.7 — an independent review of the safety rules, and the yes held in code (2026-11-14)

A separate reviewer was asked to break the snapshot check, four times over. It found 15 ways through in the
first round and smaller ones after that. All are closed. A real test session also showed that "wait for a yes"
could be skipped, so that is now held in code too.

### The yes is now held in code

- In one test session an agent saved the backup and then made the change in the same turn, without waiting.
  A change to an existing record now waits until you have replied after its snapshot was saved. Through
  Frappe's MCP tools you get Claude Code's own permission prompt; the API helper refuses the call.
- Every skill now says it plainly: the request itself is never the yes, and the snapshot comes before the
  question. Told to "do it now without asking", the test agent still saved the backup, stopped and asked.

### The snapshot check

- **A call the helper does not recognise is refused.** Before, only calls of a familiar shape were checked:
  other verbs, the older address forms, record names containing "/", bulk routes and unknown methods went
  through. `--unlisted-method` lets one through only after that refusal and your reply.
- **It reads a request the way Frappe does**, checked in Frappe 16.56's own code: a JSON body replaces the
  query string, a `cmd` argument runs whatever the address says, the v1 method address runs its first part,
  and `upload_file` runs the method named in it.
- **Update imports are checked row by row.** The dry run shows only the first 10 rows, so for a longer file
  every ID is read from the CSV itself. Record types named by a field (an Item by its code) work too.
- **A name is not proof.** `make_...` counts as a harmless draft only when called as a mapper, and 12
  methods named `get_...` that write to the database (found by reading every one in Frappe and its apps)
  are no longer treated as reads.
- **Creating a settings record, or a row inside an existing record, counts as a change.**
- **A snapshot must hold the record in full.** A list of names restores nothing, so it covers nothing.
- **Where two arguments could name the record and they disagree, the call is refused**, so the check can
  never look at one record while Frappe changes another.
- **Arabic and other non-English record names now work on Windows.** The hook misread them, and the helper
  could fail after the change had already been made.
- **The hook holds in more places**: from a folder below the workspace, from one above it, and it asks you
  when it cannot read a call, when Python is missing, and when it sits above several client folders (a
  backup in one client's folder never covers a change on another's site).
  Another MCP server's tool that happens to share a name is left alone.

### The dashboard and the logs

- Test agents wrote the activity line in their own made-up shape, so the dashboard's Agents screen skipped
  it. Every skill now carries the exact format, and the dashboard reads the near-misses.
- The dashboard script takes the API key only from the credentials file, never from environment variables.

### Ready for Anthropic's plugin directory

- The plugin folder now has its own README (saying what it runs, sends and stores), licence and notice.
- A git setting the directory may refuse is removed. Strict validation passes.

### Repository

- A demo at the top of the README, made from real test sessions and quoted word for word; a preview image
  for shared links; a contributing guide, a code of conduct, and an issue form that asks for versions.

### Tested

- 152 rule checks, 91 hook checks and 16 hook command-line checks (with and without Python).
- 61 live checks on the ERPNext 16.55 site, including a 12-row update import refused until all 12 records
  had snapshots, and an Item import.
- Real sessions with the finished plugin: a forced delete was blocked; a plain delete and an MCP change each
  saved a backup, asked, and finished after "yes"; a 30-record change saved 30 backups, asked, and closed
  all 30 after "yes".

### Limits that remain

- Hooks do not run in claude.ai chat, so there both rules are instructions Claude follows.
- The lock shows that you replied, not what you said. One snapshot covers its record for an hour.
- What was not tested is unchanged: Frappe Cloud, the Education, Drive, Studio, WhatsApp and Newsletter
  apps, bench production setup, and version 15.

## 1.1.6 — each change is checked against the record it really touches (2026-11-14)

A third security review found three more gaps in the snapshot check. All three are closed.

- **Adding a row to an existing record was treated as creating something new.** An insert that adds a child
  row (it carries `parent` and `parenttype`) changes that parent, so the parent now needs a snapshot. So
  does an upload that sets a field on a record. The create-only list matches full method names only.
- **Some writes were checked against the wrong argument.** A rename was checked against `name`, but it
  renames `old_name`. Each known write now has its own rule for which argument names its record: rename
  checks `old_name`, plus `new_name` when merging. A call whose arguments name two different records is
  refused.
- **An update import needed a snapshot of the import record alone.** The API helper now reads the import's
  type from the site, and for an update import reads every record ID from its dry run (which saves
  nothing). Each of those records needs a snapshot; if any row has no ID, the import is refused. Through
  Frappe's MCP server the guard cannot read the site, so it allows insert-only imports and refuses update
  imports; the guide says to start those with the helper or from the Data Import screen.

Tested: 46 of 46 guard checks and 30 of 30 helper checks pass, including a real update import on the live
site that was refused until the import and both customers in its file had snapshots.

## 1.1.5 — one set of safety rules (2026-11-14)

A second security review found that 1.1.4's stricter matching opened two gaps and left a third. All three are
closed.

- **Starting a data import was no longer refused.** The import call was listed by its short name, which exact
  matching no longer found. It now needs a snapshot of the import, and of every record an update import changes.
- **A method run on a record was let through when its name began with `get_` or `make_`.** Only the import
  dry run is now treated as read-only; every other method on a record needs that record's snapshot. A
  method such as `make_payment_request` changes things.
- **The API helper and the MCP guard kept separate lists** of calls that change data, and the helper's
  missed bulk update, bulk delete and import. Both now use one shared file,
  `skills/frappe-connect/scripts/frappe_safety.py`. A bulk delete or update needs a snapshot of every record
  it touches, and a known write under any module path counts as a write.
- The import and payroll recipes now name their snapshot step.

Tested: 35 of 35 guard checks and 28 of 28 helper checks pass, including each case above and a guard that
cannot load its rules (it asks you instead of letting the call through).

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
