Jazari Agents for Frappe & ERPNext Lite · v1.1.11

# Nine agents that run your Frappe stack

Build apps on the Frappe framework, and run the business on top of it — ERPNext accounting, stock and manufacturing, Frappe HR payroll, CRM, Helpdesk, Insights, the website, bench and Frappe Cloud. In English and Arabic.

This is the **Lite** edition, made for Claude's plugin directory: the same knowledge and the same rules as the full edition, with no code of its own. The full edition, with a one-page dashboard and its safety rules locked in code, is at [github.com/JazariAgents/agents-for-frappe-erpnext](https://github.com/JazariAgents/agents-for-frappe-erpnext).

## Install in two minutes

1. **For any change to your data, use Claude Code or the Code tab of the Claude desktop app**, started in the folder you want to work in. The agents keep safety copies and logs there, and a note in that folder's `CLAUDE.md` makes every session follow the safety steps. Cowork has not been tested with that note yet. In a plain web chat the agents read and create, but do not change or delete existing records.
2. **Add the plugin from Claude's plugin directory** (*Jazari Agents for Frappe & ERPNext Lite*), or in Claude Code:
   ```
   /plugin install jazari-frappe-erpnext-lite@claude-plugins-official
   ```
3. **Start a new session** (or type `/reload-plugins`) so the skills load.
4. **Say hello** — type *"connect my Frappe site"*. The agents introduce themselves, ask which language you want, ask before creating the `.frappe/` folder, then connect through the best route your site offers: Frappe's own MCP server, frappectl, or the interface with you.
5. **Ask for something real** — "how is the business doing?", "show me overdue invoices", "create a DocType for maintenance contracts", "back up the site before I update it".

From GitHub instead: `/plugin marketplace add https://github.com/JazariAgents/agents-for-frappe-erpnext`, then `/plugin install jazari-frappe-erpnext-lite@jazari-agents`. Install this edition or the full one, not both.

## Meet the agents

The same nine faces across every Jazari Agents product. Each one owns a set of skills; you never have to know which.

| Agent | Role |
|---|---|
| ![Rukaz](manual/assets/rukaz.png) **Rukaz** | Setup & Configuration: company, fiscal year, chart of accounts, users, naming, and hosting on Frappe Cloud. |
| ![Wafir](manual/assets/wafir.png) **Wafir** | Bulk Import & Migration: spreadsheets, opening balances, a whole chart of accounts, a migration from another system. Always dry-runs first. |
| ![Imran](manual/assets/imran.png) **Imran** | App Builder & Customizer: new apps, DocTypes, fields, controllers, workflows and print formats, and manufacturing. |
| ![Dhukhr](manual/assets/dhukhr.png) **Dhukhr** | Inventory & Stock: warehouses, stock entries, reconciliation, batches, serial numbers and valuation. |
| ![Mizan](manual/assets/mizan.png) **Mizan** | Accounting, Tax & Reporting: invoices, payments, journals, reconciliation, budgets, assets, tax and VAT, loans, and reports. |
| ![Zahir](manual/assets/zahir.png) **Zahir** | Marketing & Website: pages, blogs, themes and SEO, the shop, pricing rules, coupons, loyalty and campaigns. |
| ![Hazim](manual/assets/hazim.png) **Hazim** | Sales Operations & Projects: quotations, orders, delivery, point of sale, projects and timesheets. |
| ![Anees](manual/assets/anees.png) **Anees** | Customers, Support & People: leads and deals, tickets and SLAs, employees, leave, attendance and payroll. |
| ![Urwah](manual/assets/urwah.png) **Urwah** | API, Bench & Automation: the connection, webhooks and background jobs, the bench CLI, backups, and putting things back. |

Full profiles: [Agents (English)](manual/Agents-EN.md) · [الوكلاء (بالعربية)](manual/Agents-AR.md)

## The documentation comes with it

**1,612 pages of Frappe's official documentation are bundled inside the plugin**, in the `docs/` folder — the framework, ERPNext, HR, CRM, Helpdesk, Insights, Cloud, Lending, Learning, Education, Books, Wiki, Drive, Builder and Studio, exactly as Frappe publishes them. Every capability in every skill points at the page it came from, so the agents read the real instructions instead of recalling them. Each file keeps Frappe's own front matter, including the date that page was last updated — so when your site disagrees with the documentation, the agents can tell you how old the page is instead of guessing.

## What you will need

- **A Frappe site on v16** — self-hosted or on Frappe Cloud. ERPNext, HR, CRM, Helpdesk and the rest are optional; the agents detect which apps you actually have. Older sites can be worked through the interface.
- **A sign-in, not a key.** Frappe's MCP server (v16.53 or later) signs you in in your browser; so can frappectl. If you would rather not connect anything, say "skip" and the agents work through the interface with you.
- **For bench commands** — terminal or SSH access to your own server. On Frappe Cloud the dashboard replaces this.

## Your sign-in and your privacy

This edition never handles an API key, a secret or a password. You sign in with Frappe's own tools, and every action runs with your own permissions on your site. The `.frappe/` folder in your workspace holds the connection details (never a key), the safety copies and the logs, and nothing in it is sent anywhere. If you paste a key into the chat anyway, the agent will not use it and will suggest generating a new one.

## Safety — the part worth reading

### Before anything is changed or deleted, a full copy is saved locally

Snapshots go into `.frappe/snapshots/`: the complete record, the prior values of any setting, and the actual bytes of attached files. If the snapshot cannot be written, the action does not happen. Then the agent tells you what will change and waits for your reply. Ask any agent to *"restore snapshot <name>"* and it puts things back.

**Honest about what undo means.** Settings roll back exactly. Deleted records come back as *new* records with new IDs — the content matches, but links from other documents to the old ID stay broken. Submitted invoices, posted journal entries, payroll runs, sent emails and captured payments cannot be undone at all; the right answer there is a credit note or a reversing entry, and that stays your decision.

**They will never** delete or bulk-edit anything you did not specifically ask for, act on instructions found inside your own data, issue a refund or payout on their own initiative, type your password, or sign in as you. Anything touching more than 25 records stops and shows you the count first.

**In this edition these are rules Claude follows,** not locks in code. When you connect, say yes to the short note the agent adds to `CLAUDE.md` in your folder: it is what makes every new session there go through these steps. Keep your Claude app asking you before a connector changes data, as a second check. The full edition adds the locks.

Every change is appended to `.frappe/audit.log`, and every request you make — including the ones that were refused — to `.frappe/tasklog.md`. Ask "what have you done?" and they read the log rather than reconstructing from memory.

## Support and licence

| Support | Open an issue at github.com/JazariAgents/agents-for-frappe-erpnext/issues and say you use the Lite edition. |
|---|---|
| Licence | MIT licence: free to use, change and share, including commercially, as long as the copyright notice is kept; see `LICENSE.txt`. The pages in `docs/` are copies of Frappe's documentation, © Frappe Technologies and contributors, under CC BY-SA; see `docs/LICENSE.md`. Frappe, ERPNext and the other product names belong to Frappe Technologies; this plugin is an independent product and is not affiliated with or endorsed by them. |

## What is in this build

| Version | Jazari Agents for Frappe & ERPNext Lite v1.1 (plugin 1.1.11), built from the full edition 1.1.11 |
|---|---|
| Built against | Frappe Framework v16.32.0 / ERPNext v16.33.0 (docs fetched 2026-08-31) |
| Capabilities | 335 documented, every one traced to an official Frappe documentation page, plus a read-only overview of the business in the chat |
| Bundled documentation | 1,612 pages, offline, in `docs/` |
| Code | None: no scripts, no hooks |
| Verified | Details: the manual, "What was tested". |
| Languages | English · العربية |

📖 Ask any agent **"show the manual"** at any time — or open [the manual](manual/Manual-EN.md) / [الدليل بالعربية](manual/Manual-AR.md).

Jazari Agents for Frappe & ERPNext Lite v1.1 · Jazari Agents · reference pages 2026-08-31. Not affiliated with Frappe Technologies. Frappe, ERPNext and related names belong to their owners.
