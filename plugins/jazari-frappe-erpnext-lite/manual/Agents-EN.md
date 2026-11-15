Jazari Agents for Frappe & ERPNext Lite · v1.1.12

# The cast

Nine agents, the same faces across every Jazari Agents product. What changes per system is what each one knows.

![Rukaz](assets/rukaz.png)

### Rukaz

Setup & Configuration · 32 capabilities

Gets a new site into a state where real work can happen: company, fiscal year, chart of accounts, users, naming, and hosting on Frappe Cloud.

Skills: `frappe-cloud`, `frappe-restore`, `frappe-setup`, `frappe-users-permissions`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Turn on two-factor authentication | In the interface | restores exactly | `frappe-users-permissions` |
| Read the audit trail | In the interface | safe — reads or creates | `frappe-users-permissions` |
| Hide fields with permission levels | In the interface | restores exactly | `frappe-users-permissions` |
| Group roles into a role profile | In the interface | restores exactly | `frappe-users-permissions` |
| Set role-based permissions | In the interface | restores exactly | `frappe-users-permissions` |
| Understand permission types | Guided | safe — reads or creates | `frappe-users-permissions` |
| Restrict a user to specific records | In the interface | restores exactly | `frappe-users-permissions` |
| Add and manage users | In the interface | safe — reads or creates | `frappe-users-permissions` |

… and 24 more — see the manual.

![Wafir](assets/wafir.png)

### Wafir

Bulk Import & Migration · 13 capabilities

Moves data in by the thousand — spreadsheets, opening balances, a whole chart of accounts, or a migration from another system. Always dry-runs first.

Skills: `frappe-accounting`, `frappe-data-import`, `frappe-inventory`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Enter opening balances | In the interface | restores exactly | `frappe-accounting` |
| Import opening invoices | In the interface | restores exactly | `frappe-accounting` |
| Rename records in bulk | In the interface | restores exactly | `frappe-data-import` |
| Update many records at once | In the interface | restores exactly | `frappe-data-import` |
| Import a chart of accounts | In the interface | restores exactly | `frappe-data-import` |
| Export records to a spreadsheet | In the interface | safe — reads or creates | `frappe-data-import` |
| Import records from a spreadsheet | In the interface | restores exactly | `frappe-data-import` |
| Load opening stock | In the interface | cannot be undone | `frappe-inventory` |

… and 5 more — see the manual.

![Imran](assets/imran.png)

### Imran

App Builder & Customizer · 47 capabilities

Builds on the framework itself: new apps, DocTypes, fields, controllers, workflows and print formats — and the manufacturing side, where a bill of materials is its own kind of blueprint.

Skills: `frappe-app-builder`, `frappe-buying`, `frappe-inventory`, `frappe-manufacturing`, `frappe-website`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Create a new Frappe app | bench CLI | safe — reads or creates | `frappe-app-builder` |
| Create a new site for an app | bench CLI | safe — reads or creates | `frappe-app-builder` |
| Write controller methods | Guided | safe — reads or creates | `frappe-app-builder` |
| Create a DocType | In the interface | safe — reads or creates | `frappe-app-builder` |
| Turn on DocType features | In the interface | safe — reads or creates | `frappe-app-builder` |
| Pick the right field type | In the interface | safe — reads or creates | `frappe-app-builder` |
| Set how documents are named | In the interface | safe — reads or creates | `frappe-app-builder` |
| Choose the right kind of DocType | Guided | safe — reads or creates | `frappe-app-builder` |

… and 39 more — see the manual.

![Dhukhr](assets/dhukhr.png)

### Dhukhr

Inventory & Stock · 19 capabilities

Knows where every item is and what it is worth: warehouses, stock entries, reconciliation, batches, serial numbers and valuation.

Skills: `frappe-buying`, `frappe-inventory`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Receive goods | API | cannot be undone | `frappe-buying` |
| Return goods to a supplier | API | cannot be undone | `frappe-buying` |
| Make a stock entry | API | cannot be undone | `frappe-inventory` |
| Create and manage items | API | restores exactly | `frappe-inventory` |
| Group items | In the interface | restores exactly | `frappe-inventory` |
| Reconcile physical stock | API | cannot be undone | `frappe-inventory` |
| Manage units of measure | In the interface | restores exactly | `frappe-inventory` |
| Set up warehouses | API | restores exactly | `frappe-inventory` |

… and 11 more — see the manual.

![Mizan](assets/mizan.png)

### Mizan

Accounting, Tax & Reporting · 70 capabilities

The money: invoices, payments, journals, reconciliation, budgets, assets, tax and VAT, loans, and every report the business is judged by.

Skills: `frappe-accounting`, `frappe-buying`, `frappe-inventory`, `frappe-learning`, `frappe-lending`, `frappe-projects`, `frappe-reports`, `frappe-selling`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Issue a credit note | API | cannot be undone | `frappe-accounting` |
| Issue a debit note | API | cannot be undone | `frappe-accounting` |
| Post a journal entry | API | cannot be undone | `frappe-accounting` |
| Record a payment entry | API | cannot be undone | `frappe-accounting` |
| Send a payment request | API | cannot be undone | `frappe-accounting` |
| Set payment terms | In the interface | restores exactly | `frappe-accounting` |
| Record a purchase invoice | API | cannot be undone | `frappe-accounting` |
| Raise a sales invoice | API | cannot be undone | `frappe-accounting` |

… and 62 more — see the manual.

![Zahir](assets/zahir.png)

### Zahir

Marketing & Website · 22 capabilities

The public face: website pages, blogs, themes and SEO, the shop, pricing rules, coupons, loyalty, campaigns and newsletters.

Skills: `frappe-crm`, `frappe-selling`, `frappe-setup`, `frappe-website`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Capture leads from a web form | In the interface | restores exactly | `frappe-crm` |
| Issue coupon codes | In the interface | restores exactly | `frappe-selling` |
| Set item prices | API | restores exactly | `frappe-selling` |
| Run a loyalty program | In the interface | restores exactly | `frappe-selling` |
| Maintain price lists | API | restores exactly | `frappe-selling` |
| Apply a pricing rule | In the interface | restores exactly | `frappe-selling` |
| Run a promotional scheme | In the interface | restores exactly | `frappe-selling` |
| Create an email template | In the interface | restores exactly | `frappe-setup` |

… and 14 more — see the manual.

![Hazim](assets/hazim.png)

### Hazim

Sales Operations & Projects · 17 capabilities

Keeps orders moving: quotations, sales orders, picking, packing, delivery, point of sale, and the projects and timesheets behind service work.

Skills: `frappe-helpdesk`, `frappe-projects`, `frappe-reports`, `frappe-selling`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Ship goods with a delivery note | API | cannot be undone | `frappe-selling` |
| Plan a delivery trip | API | restores exactly | `frappe-selling` |
| Pack an order | API | restores exactly | `frappe-selling` |
| Pick stock for an order | API | restores exactly | `frappe-selling` |
| Send a quotation | API | restores exactly | `frappe-selling` |
| Process a sales return | API | cannot be undone | `frappe-selling` |
| Confirm a sales order | API | cannot be undone | `frappe-selling` |
| Book a shipment | API | cannot be undone | `frappe-selling` |

… and 9 more — see the manual.

![Anees](assets/anees.png)

### Anees

Customers, Support & People · 60 capabilities

Everyone the business deals with: leads and deals, support tickets and SLAs, employees, leave, attendance and payroll, students and learners.

Skills: `frappe-crm`, `frappe-helpdesk`, `frappe-hr`, `frappe-learning`, `frappe-selling`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Mark attendance | API | restores exactly | `frappe-hr` |
| Automate attendance from check-ins | In the interface | restores exactly | `frappe-hr` |
| Create employee records | API | restores exactly | `frappe-hr` |
| Onboard a new employee | In the interface | restores exactly | `frappe-hr` |
| Run employee separation | In the interface | restores exactly | `frappe-hr` |
| Create and manage customers | API | restores exactly | `frappe-selling` |
| Group customers | In the interface | restores exactly | `frappe-selling` |
| Organise territories | In the interface | restores exactly | `frappe-selling` |

… and 52 more — see the manual.

![Urwah](assets/urwah.png)

### Urwah

API, Bench & Automation · 55 capabilities

The plumbing: connecting Claude to the site, the REST API, webhooks and background jobs, the bench CLI, backups — and putting things back when something goes wrong.

Skills: `frappe-api`, `frappe-bench`, `frappe-cloud`, `frappe-connect`, `frappe-reports`, `frappe-restore`, `frappe-setup`

| What it can do | How | Undo | Skill |
|---|---|---|---|
| Authenticate with OAuth 2 | API | safe — reads or creates | `frappe-connect` |
| Log in with username and password | API | safe — reads or creates | `frappe-connect` |
| Authenticate with API key and secret | API | safe — reads or creates | `frappe-connect` |
| Test the site connection | API | safe — reads or creates | `frappe-connect` |
| Create a document through the API | API | safe — reads or creates | `frappe-api` |
| Filter and select fields in a list call | API | safe — reads or creates | `frappe-api` |
| List documents of any DocType | API | safe — reads or creates | `frappe-api` |
| Generate API key and secret for a user | In the interface | safe — reads or creates | `frappe-connect` |

… and 43 more — see the manual.

Jazari Agents for Frappe & ERPNext Lite v1.1.12 · Jazari Agents · 2026-11-14
