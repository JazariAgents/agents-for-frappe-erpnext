# Interface adapter — HR and payroll

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
| `https://your-site/app` | the Desk (Frappe HR also serves a portal at /hr) |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Create employee records
- **Path:** https://your-site/app → **Home > Human Resources > Employee**
- **Record type:** Employee
- **Documented steps:**
  1. Go to the Employee list, and click on New
  2. Enter the Employee's personal details such as Name, Gender, Date of Birth, and Date of Joining
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee.md`  (https://docs.frappe.io/hr/employee)

### Onboard a new employee
- **Path:** https://your-site/app → **Human Resources > Employee Lifecycle > Employee Onboarding**
- **Record type:** Employee Onboarding
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee-onboarding.md`  (https://docs.frappe.io/hr/employee-onboarding)

### Run employee separation
- **Path:** https://your-site/app → **Human Resources > Employee Lifecycle > Employee Separation**
- **Record type:** Employee Separation
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee-separation.md`  (https://docs.frappe.io/hr/employee-separation)

### Mark attendance
- **Path:** https://your-site/app → **Home > Human Resources > Attendance**
- **Record type:** Attendance
- **Documented steps:**
  1. Go to the Attendance list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__attendance.md`  (https://docs.frappe.io/hr/attendance)

### Automate attendance from check-ins
- **Path:** open https://your-site/app (the Desk (Frappe HR also serves a portal at /hr)) and find *Auto Attendance* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__auto-attendance.md`  (https://docs.frappe.io/hr/auto-attendance)

### Record employee check-ins
- **Path:** https://your-site/app → **Human Resources > Attendance > Employee Checkin**
- **Record type:** Employee Checkin
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee-checkin.md`  (https://docs.frappe.io/hr/employee-checkin)

### Plan shifts
- **Path:** https://your-site/app → **Home > Human Resources > Shift Management > Shift Type**
- **Record type:** Shift Type
- **Documented steps:**
  1. First Check-in and Last Check-out
  2. Every Valid Check-in and Check-out
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__shift-type.md`  (https://docs.frappe.io/hr/shift-type)

### Define leave types
- **Path:** https://your-site/app → **Home > Human Resources > Leaves > Leave Type**
- **Record type:** Leave Type
- **Documented steps:**
  1. Go to Leave Type list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__leave-type.md`  (https://docs.frappe.io/hr/leave-type)

### Set a leave policy
- **Path:** https://your-site/app → **Home > Human Resources > Leaves > Leave Policy**
- **Record type:** Leave Policy
- **Documented steps:**
  1. Go to Leave Policy list, click on New
  2. Select the Leave Type and enter its Annual Allocation
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__leave-policy.md`  (https://docs.frappe.io/hr/leave-policy)

### Allocate leave
- **Path:** https://your-site/app → **Home > Human Resources > Leaves > Leave Allocation**
- **Record type:** Leave Allocation
- **Documented steps:**
  1. Go to Leave Allocation list, click on New
  2. Select the Employee, Leave Type, From Date and To Date
  3. Enter the number of New Leaves Allocated for that particular Leave Type
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__leave-allocation.md`  (https://docs.frappe.io/hr/leave-allocation)

### Approve a leave application
- **Path:** https://your-site/app → **Home > Human Resources > Leaves > Leave Application**
- **Record type:** Leave Application
- **Documented steps:**
  1. Go to Leave Application list, click on New
  2. A table of Allocated Leaves will be shown. Based on the Leaves taken, the available leaves are displayed for each Leave Type
  3. Select the Employee Name and Leave Type
  4. Set the Leave duration using From Date and To Date. Based on the dates selected, the 'Total Leave Days' and the 'Leave Balance Before Application' fields will be displayed
  5. If the Leave applied is for a half-day, select the 'Half Day' checkbox
  6. Enter the Reason for Leave
  7. Select Leave Approver
  8. Select the Posting Date of the Leave Application
  9. Check the 'Follow via Email' checkbox to send notification of the Leave Application to the Leave Approver
  10. You can also link the Salary Slip of the Employee in the Leave Application for the record
  11. Click on Save. Once the Employee saves the Leave Application, the status of the Leave Application changes to 'Open', and an email is sent to the Leave Approver for approval. The Leave Approval Notification Template can be configured in HR Settings under the Leave Settings section
  12. Once the Leave Approver receives the email, they can Approve, Reject, or Cancel the Leave Application. Once this is done, the Leave Approver can submit the Leave Application. On submission, the status of the document changes accordingly, and an email is sent to the Employee notifying them the same
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__leave-application.md`  (https://docs.frappe.io/hr/leave-application)

### Maintain the holiday list
- **Path:** https://your-site/app → **Home > Human Resources > Leaves > Holiday List**
- **Record type:** Holiday List
- **Documented steps:**
  1. Go to Holiday List, click on New
  2. Enter Holiday List Name. It can be based on the Fiscal Year or Location or Department as per the requirement
  3. Select From Date and To Date for the Holiday List
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__holiday-list.md`  (https://docs.frappe.io/hr/holiday-list)

### Build a salary structure
- **Path:** https://your-site/app → **Home > Human Resources > Payroll > Salary Structure**
- **Record type:** Salary Structure
- **Documented steps:**
  1. Go to the Salary Structure list, click on New
  2. Enter the Salary Structure Name
  3. Select the Company Name and Payroll Frequency
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__salary-structure.md`  (https://docs.frappe.io/hr/salary-structure)

### Define salary components
- **Path:** https://your-site/app → **Home > Human Resources > Payroll > Salary Component**
- **Record type:** Salary Component
- **Documented steps:**
  1. Go to Salary Component list, click on New
  2. Enter its Name and Abbreviation
  3. Enter Description of the Salary Component (optional)
  4. Enter the Company name and the Default Account of the Salary Component in the Accounts table
  5. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__salary-component.md`  (https://docs.frappe.io/hr/salary-component)

### Run payroll
- **Path:** https://your-site/app → **Home > Human Resources > Payroll > Payroll Entry**
- **Record type:** Payroll Entry
- **Documented steps:**
  1. Go to to Payroll Entry list, click on New
  2. Select the Payroll Frequency
  3. Select Branch, Designation and Department to filter out employees (optional)
  4. Select Project (optional) if you want to run the payroll against a project
  5. Select 'Validate Attendance' and 'Salary Slip Based on Timesheet' checkboxes in case you want to deduct the salary based on attendance and if you want to also consider the timesheets of the employees respectively
  6. Select the Payment Account to make the Bank Entry
  7. Save
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__payroll-entry.md`  (https://docs.frappe.io/hr/payroll-entry)
- **Also read:** `docs/frappe-hr/hr__salary-structure.md` — the step-by-step page for this
- **Also read:** `docs/frappe-hr/hr__salary-slip.md` — the step-by-step page for this

### Issue salary slips
- **Path:** https://your-site/app → **Home > Human Resources > Payroll > Salary Slip**
- **Record type:** Salary Slip
- **Documented steps:**
  1. Go to Salary Slip, Click on New
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__salary-slip.md`  (https://docs.frappe.io/hr/salary-slip)

### Process expense claims
- **Path:** https://your-site/app → **Human Resources > Expense Claims > Expense Claim**
- **Record type:** Expense Claim
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__expense-claim.md`  (https://docs.frappe.io/hr/expense-claim)

### Give an employee advance
- **Path:** https://your-site/app → **Human Resources > Expense Claims > Employee Advance**
- **Record type:** Employee Advance
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee-advance.md`  (https://docs.frappe.io/hr/employee-advance)

### Run an appraisal cycle
- **Path:** https://your-site/app → **Home > Human Resources > Performance > Appraisal Cycle**
- **Record type:** Appraisal Cycle
- **Documented steps:**
  1. Go to the Appraisal Cycle list, and click on New
  2. After setting the filters, click on the Get Employees button and save. This will fetch the employees based on the set filters
  3. You can check the Employees table to find the fetched employees. You can add more employees to be included in the cycle manually by clicking on the Add Row button
  4. Click on the Create Appraisals button. This will create all the Appraisal documents for the selected employees
  5. Click on Start button to start the cycle
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__appraisal-cycle.md`  (https://docs.frappe.io/hr/appraisal-cycle)

### Post a job opening
- **Path:** https://your-site/app → **Home > Human Resource > Recruitment > Job Opening**
- **Record type:** Job Opening
- **Documented steps:**
  1. Go to Job Opening list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__job-opening.md`  (https://docs.frappe.io/hr/job-opening)

### Track job applicants
- **Path:** https://your-site/app → **Home > Human Resource > Recruitment > Job Applicant**
- **Record type:** Job Applicant
- **Documented steps:**
  1. Go to Job Applicant list, click on New
  2. Enter Applicant Name and Email Address
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__job-applicant.md`  (https://docs.frappe.io/hr/job-applicant)

### Collect tax exemption declarations
- **Path:** https://your-site/app → **Home > Human resources > Employee Tax and Benefits > Employee Tax Exemption Declaration**
- **Documented steps:**
  1. Employee Tax Exemption Proof Submission
  2. Employee Benefit Application
  3. Employee Benefit Claim
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/frappe-hr/hr__employee-tax-exemption-declaration.md`  (https://docs.frappe.io/hr/employee-tax-exemption-declaration)

