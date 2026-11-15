# Capabilities — HR and payroll

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `hr.employee` | Create employee records | api | yes | reversible | `docs/frappe-hr/hr__employee.md` | https://docs.frappe.io/hr/employee |
| `hr.onboarding` | Onboard a new employee | browser | yes | reversible | `docs/frappe-hr/hr__employee-onboarding.md` | https://docs.frappe.io/hr/employee-onboarding |
| `hr.separation` | Run employee separation | browser | yes | reversible | `docs/frappe-hr/hr__employee-separation.md` | https://docs.frappe.io/hr/employee-separation |
| `hr.attendance` | Mark attendance | api | yes | reversible | `docs/frappe-hr/hr__attendance.md` | https://docs.frappe.io/hr/attendance |
| `hr.autoattendance` | Automate attendance from check-ins | browser | yes | reversible | `docs/frappe-hr/hr__auto-attendance.md` | https://docs.frappe.io/hr/auto-attendance |
| `hr.checkin` | Record employee check-ins | api | yes | reversible | `docs/frappe-hr/hr__employee-checkin.md` | https://docs.frappe.io/hr/employee-checkin |
| `hr.shift` | Plan shifts | browser | yes | reversible | `docs/frappe-hr/hr__shift-type.md` | https://docs.frappe.io/hr/shift-type |
| `hr.leavetype` | Define leave types | browser | yes | reversible | `docs/frappe-hr/hr__leave-type.md` | https://docs.frappe.io/hr/leave-type |
| `hr.leavepolicy` | Set a leave policy | browser | yes | reversible | `docs/frappe-hr/hr__leave-policy.md` | https://docs.frappe.io/hr/leave-policy |
| `hr.leaveallocation` | Allocate leave | api | yes | reversible | `docs/frappe-hr/hr__leave-allocation.md` | https://docs.frappe.io/hr/leave-allocation |
| `hr.leaveapplication` | Approve a leave application | api | yes | reversible | `docs/frappe-hr/hr__leave-application.md` | https://docs.frappe.io/hr/leave-application |
| `hr.holidaylist` | Maintain the holiday list | browser | yes | reversible | `docs/frappe-hr/hr__holiday-list.md` | https://docs.frappe.io/hr/holiday-list |
| `hr.salarystructure` | Build a salary structure | browser | yes | reversible | `docs/frappe-hr/hr__salary-structure.md` | https://docs.frappe.io/hr/salary-structure |
| `hr.salarycomponent` | Define salary components | browser | yes | reversible | `docs/frappe-hr/hr__salary-component.md` | https://docs.frappe.io/hr/salary-component |
| `hr.payrollentry` | Run payroll | api | yes | irreversible | `docs/frappe-hr/hr__payroll-entry.md` | https://docs.frappe.io/hr/payroll-entry |
| `hr.salaryslip` | Issue salary slips | api | yes | irreversible | `docs/frappe-hr/hr__salary-slip.md` | https://docs.frappe.io/hr/salary-slip |
| `hr.expenseclaim` | Process expense claims | api | yes | reversible | `docs/frappe-hr/hr__expense-claim.md` | https://docs.frappe.io/hr/expense-claim |
| `hr.advance` | Give an employee advance | api | yes | reversible | `docs/frappe-hr/hr__employee-advance.md` | https://docs.frappe.io/hr/employee-advance |
| `hr.appraisal` | Run an appraisal cycle | browser | yes | reversible | `docs/frappe-hr/hr__appraisal-cycle.md` | https://docs.frappe.io/hr/appraisal-cycle |
| `hr.jobopening` | Post a job opening | api | yes | reversible | `docs/frappe-hr/hr__job-opening.md` | https://docs.frappe.io/hr/job-opening |
| `hr.jobapplicant` | Track job applicants | api | yes | reversible | `docs/frappe-hr/hr__job-applicant.md` | https://docs.frappe.io/hr/job-applicant |
| `hr.taxexemption` | Collect tax exemption declarations | browser | yes | reversible | `docs/frappe-hr/hr__employee-tax-exemption-declaration.md` | https://docs.frappe.io/hr/employee-tax-exemption-declaration |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

