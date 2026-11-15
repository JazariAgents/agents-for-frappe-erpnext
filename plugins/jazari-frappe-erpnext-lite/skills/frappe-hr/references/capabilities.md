# Capabilities — HR and payroll

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `hr.employee` | Create employee records | api | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 2444–2596 | https://docs.frappe.io/hr/employee |
| `hr.onboarding` | Onboard a new employee | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 1810–1906 | https://docs.frappe.io/hr/employee-onboarding |
| `hr.separation` | Run employee separation | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 2129–2218 | https://docs.frappe.io/hr/employee-separation |
| `hr.attendance` | Mark attendance | api | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 537–612 | https://docs.frappe.io/hr/attendance |
| `hr.autoattendance` | Automate attendance from check-ins | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 614–721 | https://docs.frappe.io/hr/auto-attendance |
| `hr.checkin` | Record employee check-ins | api | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 1403–1478 | https://docs.frappe.io/hr/employee-checkin |
| `hr.shift` | Plan shifts | browser | yes | reversible | `docs/frappe-hr/frappe-hr-03.md` lines 1042–1107 | https://docs.frappe.io/hr/shift-type |
| `hr.leavetype` | Define leave types | browser | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 2462–2578 | https://docs.frappe.io/hr/leave-type |
| `hr.leavepolicy` | Set a leave policy | browser | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 2423–2460 | https://docs.frappe.io/hr/leave-policy |
| `hr.leaveallocation` | Allocate leave | api | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 1510–1571 | https://docs.frappe.io/hr/leave-allocation |
| `hr.leaveapplication` | Approve a leave application | api | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 1573–1684 | https://docs.frappe.io/hr/leave-application |
| `hr.holidaylist` | Maintain the holiday list | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 3163–3245 | https://docs.frappe.io/hr/holiday-list |
| `hr.salarystructure` | Build a salary structure | browser | yes | reversible | `docs/frappe-hr/frappe-hr-03.md` lines 476–571 | https://docs.frappe.io/hr/salary-structure |
| `hr.salarycomponent` | Define salary components | browser | yes | reversible | `docs/frappe-hr/frappe-hr-03.md` lines 96–230 | https://docs.frappe.io/hr/salary-component |
| `hr.payrollentry` | Run payroll | api | yes | irreversible | `docs/frappe-hr/frappe-hr-02.md` lines 3169–3277 | https://docs.frappe.io/hr/payroll-entry |
| `hr.salaryslip` | Issue salary slips | api | yes | irreversible | `docs/frappe-hr/frappe-hr-03.md` lines 232–304 | https://docs.frappe.io/hr/salary-slip |
| `hr.expenseclaim` | Process expense claims | api | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 2718–2816 | https://docs.frappe.io/hr/expense-claim |
| `hr.advance` | Give an employee advance | api | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 1172–1287 | https://docs.frappe.io/hr/employee-advance |
| `hr.appraisal` | Run an appraisal cycle | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 119–211 | https://docs.frappe.io/hr/appraisal-cycle |
| `hr.jobopening` | Post a job opening | api | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 1259–1321 | https://docs.frappe.io/hr/job-opening |
| `hr.jobapplicant` | Track job applicants | api | yes | reversible | `docs/frappe-hr/frappe-hr-02.md` lines 1133–1202 | https://docs.frappe.io/hr/job-applicant |
| `hr.taxexemption` | Collect tax exemption declarations | browser | yes | reversible | `docs/frappe-hr/frappe-hr-01.md` lines 2257–2345 | https://docs.frappe.io/hr/employee-tax-exemption-declaration |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

