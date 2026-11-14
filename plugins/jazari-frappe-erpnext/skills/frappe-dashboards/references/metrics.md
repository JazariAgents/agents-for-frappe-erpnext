# What each figure on ERPNext Pulse is

Every request is a GET on the v1 REST paths (`/api/resource/<DocType>`, `/api/method/<name>`), which
all Frappe versions serve. Lists are read 500 rows at a time up to 10,000 rows; past that the figure
is marked partial on the page. All money is in the company's default currency.

"Period" means the last 12 calendar months including the current, unfinished one (`--months` changes it).

## Finance

| Figure | Read from | Filters | Notes |
|---|---|---|---|
| Sales invoiced, per month | Sales Invoice `base_net_total` by `posting_date` | submitted, company, in period | Net of tax. Credit notes are negative invoices, so they reduce the month they are posted in. |
| Purchases invoiced, per month | Purchase Invoice `base_net_total` by `posting_date` | submitted, company, in period | Not total expenses: payroll, journal entries and depreciation are not here. |
| Cash received / paid, per month | Payment Entry `base_paid_amount` by `posting_date` | submitted, company, in period, type Receive / Pay | Internal transfers are left out. |
| Receivables outstanding | Sales Invoice `outstanding_amount` × `conversion_rate` | submitted, company, outstanding above zero, any date | The multiplication is an approximation for foreign-currency invoices: it uses the invoice's rate, not today's. |
| Receivables by age | same rows, days between today and `due_date` | | Buckets: not yet due, 1–30, 31–60, 61–90, over 90 days. |
| Largest overdue invoices | same rows, past due | top 8 by amount | |
| Payables outstanding / overdue | Purchase Invoice `outstanding_amount` × `conversion_rate` | submitted, company, outstanding above zero | Same approximation. |

## Sales

| Figure | Read from | Filters | Notes |
|---|---|---|---|
| Top customers | the Sales Invoice rows above, summed by `customer_name` | | Two customers with the same display name are merged. |
| Sales orders by status | Sales Order `status`, `base_net_total` | submitted, company, `transaction_date` in period | An order older than the period that is still open is not counted. |
| Open sales orders | the statuses To Deliver and Bill, To Bill, To Deliver, On Hold from the rows above | | |
| Open quotations | Quotation `base_net_total` | submitted, company, status Open | |
| Customers / new per month | Customer count; Customer `creation` | enabled; created in period | Not filtered by company: customers are shared across companies. |

## People

Employee is part of ERPNext. Attendance, Leave Application, Expense Claim and Salary Slip come from
Frappe HR; without it those cards say so.

| Figure | Read from | Filters | Notes |
|---|---|---|---|
| Headcount, by department | Employee `status`, `department` | company; status Active | The company suffix on a department name ("Sales - ABC") is removed. |
| Joined / left, 12 months | Employee `date_of_joining`, `relieving_date` | in period; left = status Left | |
| On leave today | Leave Application count | approved, submitted, today inside from/to dates | |
| Leave requests awaiting approval | Leave Application count | status Open, draft | |
| Attendance today | Attendance `status` | submitted, `attendance_date` today | Empty until attendance is marked. |
| Expense claims awaiting approval | Expense Claim `total_claimed_amount` | company, draft | |
| Last payroll run | Salary Slip `gross_pay`, `net_pay` | submitted, company, latest `start_date` in the last 92 days | Totals only; no individual pay is read into the page. |

"Today" is the date on the machine that runs the script, which can differ from the site's time zone
around midnight.

## System

These need the System Manager role.

| Figure | Read from | Notes |
|---|---|---|
| Installed apps | `frappe.utils.change_log.get_versions` | |
| Scheduler | `frappe.utils.scheduler.get_scheduler_status` | "Stopped" means scheduled jobs (emails, backups, recurring documents) are not running. |
| Errors per day, last 24 hours | Error Log `creation`, last 14 days | |
| Failed scheduled jobs | Scheduled Job Log, status Failed, last 24 hours | |
| Email queue | Email Queue count, status Not Sent and Error | |
| Enabled users | User count, enabled; and those of type System User | |
| Backups | not read | The REST API does not expose backup status. Always shown as Unknown. |

## Agents

Built from the workspace file `.frappe/activity.jsonl`, not from the site. One line per finished
request, written by the skill that handled it. The window is the last 30 days; the per-day chart shows
the last 14.

| Figure | How it is worked out | Notes |
|---|---|---|
| Requests | lines in the window | Lines that are not valid JSON, have no readable `ts`, or an `outcome` other than done / partial / failed / refused are left out and counted in a note. |
| Completed % | `done` ÷ requests | |
| Records changed | sum of `changed` | As reported by the agent. |
| Changes with a snapshot first | requests with `changed` above 0 and `snapshot` true ÷ requests with `changed` above 0 | Should be 100%. |
| Stopped before acting | `outcome` = refused | A guardrail stopped it, or the user declined at the confirmation. Not a failure. |
| Typical time per request | median of `seconds` where given | |
| Work by agent | grouped by `agent`; "Failed" counts failed and partial | All nine agents are listed, including those with no requests. |
| Connection used | grouped by `adapter` | |

Everything on this screen is self-reported. Nothing here is checked against the site's own records.

## How the page decides a status

| Check | OK | Check | Problem | Critical |
|---|---|---|---|---|
| Scheduler | active | | | anything else |
| Errors, 24 hours | 0 | 1–20 | over 20 | |
| Failed scheduled jobs | 0 | | 1 or more | |
| Email queue | 0 failed | 1 or more failed | | |
| Overdue receivables | none | | any | |
| Overdue payables | none | any | | |

These thresholds are this plugin's own judgement, not Frappe's. They live in the `attention()` and
`VIEWS.system` functions of `assets/pulse.template.html`.
