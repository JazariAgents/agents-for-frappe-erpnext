<!-- Frappe documentation: frappe-hr, part 4 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__hr-settings.md -->
---
title: "HR Settings"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/hr-settings"
updated: "2026-02-04"
---

**HR Settings allow global settings for HR-related documents.**

To access HR Settings, go to: > Home > Human Resources > Settings > HR Settings

There are various settings available in the HR Settings.

**1. Employee Settings**
------------------------

[Screenshot on the live page: Previous Work Experience]  


### **1.1. Retirement Age:**

You can enter the retirement age (in years) for your employees.

### **1.2 Employee Records to be created by**

The naming for employee documents is based on the value selected in this field.

* **Naming Series**: The employee documents created will be named using the naming series selected in the 'Series' field.
* **Employee Number**: The Employee Number field becomes visible in selecting this field, and the naming of the employee document happens based on this field.
* **Full Name**: The employee document is named using the full name of the employee.

### **1.3 Stop Birthday Reminders**

An email is sent to all the employees of the company when an employee has a birthday. To stop this email from being sent you can check this option.

### **1.4 Expense Approver Mandatory In Expense Claim**

In Expense Claim Document the 'Expense Approver' field is set to mandatory on checking this option.

> Payroll Settings will be part of HR Settings till version 12. In version 13, Payroll Settings will be part of the new module, Payroll.

**2. Payroll Settings**
-----------------------

[Screenshot on the live page: Previous Work Experience]  


### **2.1 Calculate Payroll Working Days Based On**

Working Days in Salary Slip can be calculated based on Leave Application or Attendance records. You can select the option based on what you want to calculate working days.

### **2.2 Max working hours against Timesheet**

For salary slips based on the timesheet, you can set the maximum allowed hours against a single timesheet. Set this value to zero to disable this validation.

### **2.3 Include holidays in Total no. of Working Days**

If checked, the total number of working days will include holidays, and this will reduce the value of salary per day.

### **2.4 Disable Rounded Total**

You can enable this to disable rounding off the total amount in salary slips.

### **2.5 Daily Wages Fraction for Half Day**

Based on this fraction, the salary for Half Day will be calculated. For example, if the value is set as 0.75, the three-fourth salary will be given for half-day attendance.

### **2.6 Email Salary Slip to Employee**

An email with the salary slip is sent to the respective employee's preferred email address on submission of the salary slip.

### **2.7 Encrypt Salary Slips in Emails**

The salary slip PDF sent to the employee is encrypted using the mentioned Password Policy.

### **2.8 Password Policy**

This field becomes visible and mandatory on checking the above option for encrypting the salary slip in email.

Here is an example of how to set a Password Policy for the salary slip PDF.

**Example:**


```
SAL-{first_name}-{date_of_birth.year}

  

```
This will generate a password like SAL-Jane-1972

**3. Shift Settings**
---------------------

**[Screenshot on the live page]**  


### **3.1 Allow Multiple Shift Assignments for Same Date**

Enabling this allows the user to create Shift Assignments for an employee with pre-existing Assignments on any of the dates within the selected range, and vice versa.

**4. Leave Settings**
---------------------

[Screenshot on the live page: Previous Work Experience]  


### **4.1 Leave Approval Notification Template**

On creating or updating a leave application with a leave approver, an email is sent to this leave approver notifying about the new leave application. The email template used for this purpose can be selected here.

### **4.2 Leave Status Notification Template**

On Submission/Cancellation of a leave application, the employee receives an email with the updated status of their leave application. The email template used for this purpose can be selected here.

### **4.3 Leave Approver Mandatory In Leave Application**

In Leave Application document the 'Leave Approver' field is set to mandatory on checking this option.

### **4.4 Show Leaves Of All Department Members In Calendar**

The approved leaves of all employees in the same department are shown in the calendar view on checking this option.

### **4.5 Auto Leave Encashment**

If checked, the system generates a draft Leave Encashment record on the expiry of the leave allocation for all encashable Leave Types.

### **4.6 Restrict Backdated Leave Application**

If checked, the system will not allow making a backdated leave application.

> Introduced in version 13

### **4.7 Automatic Allocate Leaves Based On Leave Policy**

If checked, leaves will be granted to the employees automatically based on the Effective From date as per the present Leave Policy Assignment.

**5. Hiring Settings**
----------------------

[Screenshot on the live page: image]  


### **5.1 Check Vacancies On Job Offer Creation**

On the creation of a job offer for a particular position, vacancies present in the staffing plan for that position are checked to warn the user from over hiring for a particular position.

### **5.2 Send Interview Reminder**

Enabling this will send a reminder email to all the Interviewers associated with the Interview Round of an upcoming Interview. This mail will be scheduled according to the Remind Before field set by the user.

### **5.2 Send Interview Feedback Reminder**

Enabling this option will trigger reminder emails to be sent to Interviewers who are associated with a conducted Interview Round but haven't yet submitted their Feedback for it.

**6. Mobile Settings**
----------------------

[Screenshot on the live page: Screenshot 2024-04-08 at 2 49 50 PM]  


### **6.1 Allow Employee Checkin from Mobile App**

Enabling this will allow Employees to check-in from the mobile app. It is enabled by default.

<!-- page: frappe-hr/hr__hr__leave-management__holiday-list-assignment.md -->
---
title: "Holiday List Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/hr/leave-management/holiday-list-assignment"
updated: "2026-02-04"
---

Previously, holiday list for employees and company was set in their respective master records. When new holiday list needs to be assigned to employees or company this fields is edited to set the new holiday list, this loses the historic holiday list assignment record. Additionally since only one list could be assigned at any given time, leave applications spanning two different holiday lists would not count holidays from the unassigned list.

To solve this problem, Holiday List Assignment feature is introduced. This will allows multiple holiday list assignments to employee and companies and preserves the historic assignment records.

##### Note

> Creating Holiday List Assignment for company or employee is mandatory if Frappe HR is installed on your site. ERPNext only users, can continue setting the list in the employee and company masters.

### 1. Create Holiday List Assignment

1. Set **Applicable For,** this could be either Company or Employee
2. Select the employee or company to assign the holiday list to
3. Select the holiday list to be assigned. You can edit the **Assignment Starts From** date, this is the date from which the selected holiday list is applicable for the employee or company and remains applicable till the end of the holiday list, unless another assignment is created.
  [Screenshot on the live page]

### 2. Switch List Assignment

1. In case the employee changes branches or department and new holiday list needs to be assigned, just create another holiday list assignment with appropriate **Assignment Starts From** date.
2. The most recent assignment as sorted by **Assignment Starts From** will be applicable

##### Note

> The holiday list assignment created for company will be the default list for all employees belonging to the company.

##### Note

> Employee level assignment is preferred over the default company level assignment.

<!-- page: frappe-hr/hr__hr__leave-management__leave-adjustment.md -->
---
title: "Leave Adjustment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/hr/leave-management/leave-adjustment"
updated: "2026-02-04"
---

Leave adjustment allows you to adjust leaves from existing leave allocations. This is useful in cases when the initially allocated leaves were incorrect and allocated leaves need to be either increased or decreased.

1. Go to any leave allocation document
2. Select **Adjust Allocation** from Actions menu
  [Screenshot on the live page]
3. Set adjustment type either allocate new leaves or reduce from the allocation, number of leaves to adjust and click on **Adjust Leaves.**
  [Screenshot on the live page]
4. A new leave adjustment document will be created to correct the existing leave allocation.
  [Screenshot on the live page]

<!-- page: frappe-hr/hr__human-resource-setup.md -->
---
title: "Human Resource Setup"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/human-resource-setup"
updated: "2026-02-04"
---

The HR module has a setup process where you create the masters for all the major activities.

### **Organization Setup**

To setup your Employee master you must first create:

* Employment Type (like Permanent, Temp, Contractor, Intern etc).
* Branch (if there are multiple offices).
* Department (if any, like Accounting, Sales etc).
* Designation (CEO, Sales Manager etc).
* Grade (A, B, C etc, usually based on seniority).

Check [Setup](https://frappehr.com/docs/v14/user/manual/en/setting-up) for more details on each of masters, global *HR Settings* and other configurations.

### **Leave Setup**

To setup Leaves, create:

* Leave Type (like Sick Leave, Travel Leave etc)
* Holiday List (list of annual holidays for the year - these days will not be considered in Leave Applications)
* Leave Policy to effectively track and manage Employee leaves across the company

You can read [Leaves](https://docs.frappe.io/hr/leaves/) for a detailed description about how you can configure and manage Leaves.

### **Payroll (Salary) Setup**

In Frappe HR, salaries have two types of components, earnings (basic salary, expenses paid by the company, like telephone bill, travel allowance etc) and deductions (amounts deducted for taxes, social security etc). You can create and assign salary structures to employees and Frappe HR simplifies most of the payroll processing for you.

Read more about setting up your payroll and how Frappe HR simplifies payroll processing in [Salary and Payroll](https://docs.frappe.io/hr/payroll-setup).

If you intend to configure Frappe HR to calculate Income Tax deductions automatically based on multiple Salary Slabs, [Setting Up Income Tax Deduction](https://docs.frappe.io/hr/setting-up-income-tax-deduction) will help you understand how you can set this up properly.

### **Recruitment**

It is important for enterprises to plan their manpower recruitment for future periods. Frappe HR allows you to define recruitment plans at group company level. Subsidiary companies can create and publish job openings based on the group company plans, making it easy to manage your hiring process. To understand how you can set this up, check [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

If you have an active Staffing Plan, every time you create a new *Job Opening* Frappe HR will validate the open positions and current employment count with the Staffing Plan.

  

<!-- page: frappe-hr/hr__human-resources-reports.md -->
---
title: "Human Resources Reports"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/human-resources-reports"
updated: "2026-02-04"
---

**1. Employee Leave Balance**
-----------------------------

[Screenshot on the live page: Employee Leave Balance]  


**2. Salary Register**
----------------------

Salary Register shows net pay and its components of employee(s) at a glance.

[Screenshot on the live page: Monthly Salary Register]  


**3. Monthly Attendance Sheet**
-------------------------------

Monthly Attendance Sheet shows you the employee-wise attendance status. If you assign shifts to employees, this sheet will also show you shift-wise attendance for each employee.

[Screenshot on the live page: Monthly Attendance Sheet]  


If you do not want to see day-wise attendance, and get a summarized view of total absent, present, leave days, etc. you can switch to the summarized view:

[Screenshot on the live page: Monthly Attendance Sheet]  


This will show you:

* Total Present Days
* Total Absent Days
* Total Leave Days
* Total Holidays
* Total Unmarked Days
* Number of leaves taken per leave type
* Total Late Entries
* Total Early Exits

You can also view the report grouped by Department, Branch, Designation, or Employee Grade.

**4. Shift Attendance**
-----------------------

> Introduced in Version 15

Shift Attendance presents and summarizes attendance details for marked shifts:

* Attendance Details: Employee, Date, Status, In/Out Time, Total Working Hours, Time by which Entry is Late or Exit is Early
* Shift Details: Shift Name, Shift Start/End Time, Shift Actual Start/End Time

Entries can be further filtered on the basis of:

* Shift Type
* Late Entry
* Early Exit

[Screenshot on the live page]  


**5. Vehicle Expenses Report**
------------------------------

To track and monitor Vehicle Expenses you can use the Vehicle Expenses report. This report gives a one-stop view of all your Vehicle Expenses month-wise.

[Screenshot on the live page: Vehicle Log]  


**6. Employee Exits**
---------------------

> Introduced in Version 14

This report gives a summary of Employee Exits:

* Employee Details: Employee, Reports to, Date of Joining, Relieving Date, Department, Designation
* Exit Interview
* Interview Status (Pending/Scheduled/Completed)
* Final Decision (Employee Retained/Exit Confirmed)
* Full and Final Statement

This report also provides extra filters for:

* Interview Pending
* Questionnaire Pending
* FnF Pending

Users can set up auto email reports on the above filters to make pending exit tracking easier.

[Screenshot on the live page: Monthly Salary Register]  


**7. Employee Birthday**
------------------------

Employee Birthday Report shows month-wise birthdays of your Employees.

[Screenshot on the live page: Employee Birthday]  


**8. Employee working on a holiday**
------------------------------------

Employee Holiday Attendance shows the list of Employees who attended on Holidays.

[Screenshot on the live page: Employee Working on a Holiday]  


**9. Bank Remittance Report**
-----------------------------

This report helps you to track bank transactions of payroll entries between companie(s) and employees. It shows the transaction between the bank accounts of the Company and the Employee with the Payment Date.

[Screenshot on the live page: Monthly Salary Register]  


**10. Loan Repayment Report**
-----------------------------

Loan Repayment Report allows you to keep a track of loans by showing the loan amount, interest, payable amount, and EMI. It also shows the paid and outstanding amount.

  

<!-- page: frappe-hr/hr__income-tax-calculation-in-frappehr.md -->
---
title: "Income Tax Calculation in Frappe HR"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/income-tax-calculation-in-frappehr"
updated: "2026-02-09"
---

* In payroll period, define the income tax slabs as per the government rule. If there are any standard deductions provided by the government, that amount can also be added here.

  


* If an employee has any kind of investments or tax declarations such as PPF, insurance, mutual funds, HRA, etc., add these in "Employee Tax Exemption Declaration". Screenshot attached:

  
[Screenshot on the live page]  


* While creating salary component of Income Tax, check the box "Variable Based On Taxable Salary". Ticking this checkbox means, income tax will be calculated automatically taking the payroll period and tax declarations into consideration.

  


* Create a salary structure and add Income Tax in the deduction section leaving the amount section blank. Along with that kindly add Education cess which will be based on a formula. Screenshot attached:

[Screenshot on the live page]  


* Create a payroll entry and generate salary slips. Income tax will be calculated automatically along with the education cess. Screenshot attached:

[Screenshot on the live page]  


  

<!-- page: frappe-hr/hr__income-tax-slab.md -->
---
title: "Income Tax Slab"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/income-tax-slab"
updated: "2026-02-04"
---

**Income Tax Slab is a document to define income tax rates based on different taxable income slab.**

In many countries, income tax is levied on individual taxpayers based on a slab system where different tax rates have been prescribed for different slabs and such tax rates keep increasing with an increase in the income slab. In Frappe HR, you can define multiple Income Tax Slabs and link them to individual employee's salary structure via Salary Structure Assignment.

To access Income Tax Slab, go to: > Home > Human Resources > Payroll > Income Tax Slab

**1. How to create an Income Tax Slab**
---------------------------------------

To create a new Income Tax Slab:

1. Enter a Name for the IT Slab, Company and the date from which it will be Effective From.
2. Enable the checkbox 'Allow Tax Exemption' if applicable.
3. Save and Submit.

**2. Features**
---------------

### **2.1 Tax Slabs**

In the Tax Slab table, you can define the rate for different income slabs. To define slab, From Amount and To Amount should be entered. For the first slab, From Amount is optional and for the last slab, To Amount is optional. Both the amount is inclusive while evaluating tax based on taxable income.

[Screenshot on the live page: Income Tax Slab]  


The tax slab can be applicable based on specific conditions. Conditions can be written using all field names of Employee, Salary Structure, Salary Structure Assignment, and Salary Slip documents.

Examples:


```
// Apply tax if employee born between 31-12-1937 and 01-01-1958 (Employees aged 60 to 80)
date_of_birth > date(1937, 12, 31) and date_of_birth < date(1958, 01, 01)

// Apply tax by employee gender
gender == "Male"

// Apply tax by Salary Component
base > 10000

// Annual Taxable income is greater than 5 lakhs
annual_taxable_earning > 500000
  

```
### **2.2 Other Taxes and Charges on Income Tax**

If other taxes are applicable on calculated income tax, you can enter those using this table. You can also define the min and max taxable amount for which this tax will be applicable. For example, Health and Education Cess is applied additionally on income tax to everyone in India.

[Screenshot on the live page: Other Charged on Income Tax]  


### **2.3 Other Properties**

* **Allow Tax Exemptions:** Tax exemptions can be allowed for a specific Income Tax Slab. If enabled, while calculating taxes based on this tax slab, Employee Tax Exemption Declaration and Proof Submission are considered for calculating taxable income.
* **Standard Tax Exemption Amount:** If exemption is allowed, the Standard Tax Exemption Amount defined by the government can be added here. This exemption generally does not need any kind of document proof and applicable to all employees linked to this income tax slab.

**3. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
4. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
5. [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration)
6. [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)

  

<!-- page: frappe-hr/hr__india-payroll__employee-provident-fund.md -->
---
title: "Employee Provident Fund (EPF)"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/employee-provident-fund"
updated: "2026-07-09"
---

The Employees' Provident Fund is a mandatory retirement-savings scheme governed by the **Employees' Provident Funds & Miscellaneous Provisions Act, 1952**, administered by the EPFO. Every covered employee and their employer contribute a share of the employee's monthly wages towards the fund.

India Payroll computes the employee's EPF and Voluntary Provident Fund (VPF) deductions automatically on each salary slip, tracks the employer's statutory split (EPF, EPS, EDLI and admin charges), and produces the **Employee Provident Fund Register** along with a ready-to-upload **ECR** (Electronic Challan-cum-Return) file for the EPFO portal.

## **How contributions are split**

Both the employee and the employer contribute **12% of PF wages**. The employer's 12% is not a single deposit — statute splits it across four accounts:


| Contribution                               | Account | Rate                                        | Paid by  | Appears on slip? |
| ------------------------------------------ | ------- | ------------------------------------------- | -------- | ---------------- |
| Provident Fund (EPF)                       | A/c 1   | 12% of PF wages                             | Employee | Yes — deduction  |
| Voluntary Provident Fund (VPF)             | A/c 1   | Optional, over and above 12%                | Employee | Yes — deduction  |
| Employer Provident Fund                    | A/c 1   | 12% of PF wages **minus** the EPS diversion | Employer | No — part of CTC |
| Employer Pension Scheme (EPS)              | A/c 10  | 8.33% of capped PF wages                    | Employer | No — part of CTC |
| Employees' Deposit Linked Insurance (EDLI) | A/c 21  | 0.5% of capped PF wages                     | Employer | No — part of CTC |
| EPF Admin Charges                          | A/c 2   | 0.5% of PF wages                            | Employer | No — part of CTC |


Only the **employee-side** components (Provident Fund and VPF) are posted to the salary slip as deductions and reduce net pay. The **employer-side** contributions are configured as *Employer Contribution* components on the Salary Structure, rolled into CTC by the Salary Structure Assignment, and reconstructed for statutory reporting — they never touch gross or net pay.

## **Setup**

### **1. Enable EPF in Payroll Settings**

1. Go to **Payroll Settings → India Payroll** tab.
2. Expand the **Employee Provident Fund** section.
3. Tick **Enable EPF Deduction**.
4. Optionally enter your **EPF Establishment Code** — the EPFO code for your establishment, used when filing the ECR.
5. **Save**.

When EPF is disabled, any Provident Fund and VPF rows previously injected onto salary slips are removed on the next save.

### **2. Set the employee's UAN**

On each **Employee** record, open the **India Payroll** section and fill in:

- **UAN** — the 12-digit Universal Account Number issued by EPFO.
- **Name as per UAN** — the employee's name as registered with EPFO. This can differ from the HR name and is the name written to the ECR file.

The UAN is mandatory for the ECR export. Generating the file will fail with a list of the affected employees if any in-scope employee is missing a UAN.

### **3. Opt the employee into EPF on the Salary Structure Assignment**

EPF configuration lives on the **Salary Structure Assignment (SSA)** so it can be set per employee and revised mid-year. Open the assignment, switch to the **India Payroll** tab, and use the **Employee Provident Fund** section:

- **EPF Applicable** — opts this employee into EPF for this assignment. The system defers entirely to this flag rather than applying a wage-based eligibility test, so you stay in control of who is covered.
- **Contribute on Actual PF Wage** — see [Wage ceiling](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/epf/employee-provident-fund.md#wage-ceiling-and-the-actual-wage-option) below.
- **VPF Mode / VPF Percentage / VPF Amount** — see [Voluntary Provident Fund](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/epf/employee-provident-fund.md#voluntary-provident-fund-vpf) below.

If **EPF Applicable** is unticked, no EPF or VPF rows are added and the employee is excluded from the EPF Register.

## **How the deduction is calculated**

When a salary slip is saved, India Payroll applies EPF as follows:

1. **PF wage** is the sum of every earning component on the slip. Because slip amounts are already prorated for Loss of Pay (LOP) and payment days, the PF wage automatically reflects non-contributing period (NCP) days.
2. The **EPF base** is derived from the PF wage using the wage-ceiling rule below.
3. **Employee EPF** = 12% of the EPF base, rounded to the nearest rupee.
4. **VPF** (if elected) is added as a second deduction.

All amounts are rounded to the nearest whole rupee using EPFO's half-up convention (for example, 8.33% × ₹15,000 = ₹1,249.50 becomes ₹1,250).

### **Wage ceiling and the actual-wage option**

The statutory PF wage ceiling is **₹15,000 per month**. By default, contributions are computed on the PF wage **capped at ₹15,000**.

Tick **Contribute on Actual PF Wage** on the assignment to compute the employee and employer EPF shares on the *actual* PF wage when it exceeds ₹15,000. Note that **EPS and EDLI always remain capped at ₹15,000 by law**, regardless of this setting.


| Scenario                               | EPF base       | EPS / EDLI base |
| -------------------------------------- | -------------- | --------------- |
| PF wage ≤ ₹15,000                      | Actual PF wage | Actual PF wage  |
| PF wage > ₹15,000, actual-wage **off** | ₹15,000        | ₹15,000         |
| PF wage > ₹15,000, actual-wage **on**  | Actual PF wage | ₹15,000         |


### **Pension Scheme (EPS) eligibility**

India Payroll assumes all employees are EPF members who joined on or after **1 September 2014**. Under that rule, a member whose PF wage exceeds ₹15,000 receives **no EPS diversion** — the employer's entire 12% goes to the Provident Fund account (A/c 1) instead of being split with the pension account (A/c 10).

## **Voluntary Provident Fund (VPF)**

VPF is an optional employee contribution *over and above* the mandatory 12%. The employer does not match it. Configure it per assignment with **VPF Mode**:

- **Amount** (default) — a fixed monthly rupee amount (**VPF Amount**). It is prorated by payment days ÷ total working days so LOP months don't over-deduct.
- **Percentage** — a percentage (**VPF Percentage**) of the EPF base, which already follows the capping / actual-wage rule and slip proration.

When VPF Mode is left unset on older assignments, it falls back to **Amount** mode with an amount of 0, so no VPF is ever deducted for employees who never opted in.

## **Reporting**

### **Employee Provident Fund Register**

Go to **Employee Provident Fund Register** (query report). Only employees with **EPF Applicable** ticked on their effective assignment appear.

**Filters**

- **Company** (required)
- **Year** (required)
- **Month** — a single month
- **Contribution Period** — `Apr-Sep` or `Oct-Mar`; overrides the Month filter when set

**Columns** include the UAN and name-as-per-UAN, gross wages, PF / EPS / EDLI wage bases, the employee EPF and VPF contributions, the employer EPS and EPF shares, and non-contributing period (NCP) days.

### **ECR file export**

From the report toolbar, click **Download ECR Text File** to generate the EPFO Electronic Challan-cum-Return payload for the selected period. The file is plain text — one line per member, no header — with eleven `#~#`-separated fields per member in EPFO's prescribed order:

> UAN, Member Name, Gross Wages, EPF Wages, EPS Wages, EDLI Wages, Employee EPF, EPS Contribution, Employer EPF–EPS difference, NCP Days, Refund of Advances

All amounts are reported as whole rupees. If any in-scope employee is missing a UAN, the export stops and lists those employees so you can update their master records and retry — an incomplete ECR file would be rejected by the portal anyway.

## **Salary components installed**

Installing India Payroll creates these EPF-scheme salary components automatically:

- **Provident Fund** (PF) — employee deduction, 12% of PF wages.
- **Voluntary Provident Fund** (VPF) — optional employee deduction over 12%.
- **Employer Provident Fund** (EREPF) — employer contribution, part of CTC.
- **Employer Pension Scheme** (EREPS) — employer contribution, part of CTC.
- **Employees Deposit Linked Insurance** (EDLI) — employer contribution, part of CTC.
- **EPF Admin Charges** (EPFADM) — employer contribution, part of CTC.

If any employee-side component is missing when a slip is saved, India Payroll alerts you to reinstall the app or create the components manually.

<!-- page: frappe-hr/hr__india-payroll__employee-state-insurance.md -->
---
title: "Employee State Insurance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/employee-state-insurance"
updated: "2026-07-03"
---

# Employee State Insurance (ESIC)

The Employees' State Insurance scheme (ESI) is a mandatory social security scheme under the **ESI Act, 1948**. India Payroll automates ESI contribution calculation and injection into Salary Slips.

---

## 1. How to Enable

1. Go to **Payroll Settings → India Payroll** tab.
2. Check **Enable ESIC Deduction**.
3. Optionally enter your **ESIC Registration Number** (appears on the ESIC Register report).
4. Save.

[Screenshot on the live page]
*Enabling ESI deduction*

---

## 2. How It Works

The single contribution row covers **both** shares:


| Share                  | Rate                     |
| ---------------------- | ------------------------ |
| Employee contribution  | 0.75% of gross wages     |
| Employer contribution  | 3.25% of gross wages     |
| **Combined (on slip)** | **4.00% of gross wages** |


:::note
The employer's 3.25% is shown as a single line on the slip for transparency. It is part of the CTC and not a separate payable deduction from the employee's perspective.
:::



## 3. Wage Ceiling


| Category                      | Monthly Gross Wage Ceiling |
| ----------------------------- | -------------------------- |
| General employees             | ₹21,000                    |
| Persons with Disability (PwD) | ₹25,000                    |


The PwD status is read from the `is_person_with_disability` checkbox on the Employee master.

- Employees **at or below** the ceiling are covered (ESI row injected).
- Employees **above** the ceiling are not covered (ESI row removed if previously present).

---

## 4. Persons with Disability

To apply the higher ₹25,000 ceiling for a PwD employee:

1. Open the **appropriate Salary Structure Assignment** document.
2. Check **Is Person with Disability**.

[Screenshot on the live page]

The hook reads this field on every slip save, so changing the flag mid-year takes effect on the next payroll run.

## 5. ESIC Card Number

The **ESIC Card No** (IP Number) field is a standard Frappe HR field on the Employee master. It is displayed in the **ESIC Register** report and should be filled for all covered employees for the report to be complete.

---

<!-- page: frappe-hr/hr__india-payroll__introduction.md -->
---
title: "Introduction"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/introduction"
updated: "2026-06-24"
---

# Introduction

India Payroll is an open-source Frappe HR extension app that automates statutory payroll deductions and compliance reporting for Indian businesses.

## Why India Payroll?

Running payroll in India means complying with multiple overlapping statutory obligations. Doing this manually inside salary structure formulas is fragile and hard to maintain.

India Payroll takes a different approach:

- **Zero formula changes** - All deductions are injected via `before_save` hooks on the Salary Slip. Your salary structures stay clean.
- **Single toggle to activate** - Enable each deduction type from **Payroll Settings → India Payroll** tab.
- **State-aware** - Rules are driven by the `employment_state` field on Salary Structure Assignment, not hard-coded in structures.
- **Auditable** - Each deduction appears as a named salary component on the slip, visible to HR and employees alike.

<!-- page: frappe-hr/hr__india-payroll__labour-welfare-fund.md -->
---
title: "Labour Welfare Fund (LWF)"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/labour-welfare-fund"
updated: "2026-07-09"
---

The Labour Welfare Fund (LWF) is a statutory contribution collected by state governments under their respective Labour Welfare Fund Acts. India Payroll automates LWF deduction on Salary Slips based on the employee's work state and the payroll month.

> LWF amounts are **flat fixed amounts per employee**, not percentages of salary.

---

## 1. How to Enable

1. Go to **Payroll Settings → India Payroll** tab.
2. Check **Enable LWF Deduction**.
3. Save.

[Screenshot on the live page]
*Enable Labour Welfare Fund*

---

## 2. Deduction Frequency


| Frequency       | Deduction Months | States                                                                              |
| --------------- | ---------------- | ----------------------------------------------------------------------------------- |
| **Monthly**     | Every month      | Haryana, Kerala, Punjab, Chandigarh                                                 |
| **Half-yearly** | June + December  | Chhattisgarh, Delhi, Goa, Gujarat, Madhya Pradesh, Maharashtra, Odisha, West Bengal |
| **Annual**      | December only    | Andhra Pradesh, Karnataka, Tamil Nadu, Telangana                                    |


---

## 3. State-wise Rate Table

All amounts are flat fixed contributions per employee per deduction period.

### Monthly States


| State      | Employee (₹) | Employer (₹) |
| ---------- | ------------ | ------------ |
| Haryana    | 34           | 68           |
| Kerala     | 50           | 50           |
| Punjab     | 5            | 20           |
| Chandigarh | 5            | 20           |


### Half-Yearly States (June + December)


| State          | Employee (₹) | Employer (₹) |
| -------------- | ------------ | ------------ |
| Chhattisgarh   | 15           | 45           |
| Delhi          | 0.75         | 2.25         |
| Goa            | 60           | 180          |
| Gujarat        | 6            | 12           |
| Madhya Pradesh | 10           | 30           |
| Maharashtra    | 25           | 75           |
| Odisha         | 20           | 40           |
| West Bengal    | 3            | 30           |


### Annual States (December only)


| State          | Employee (₹) | Employer (₹) |
| -------------- | ------------ | ------------ |
| Andhra Pradesh | 30           | 70           |
| Karnataka      | 50           | 100          |
| Tamil Nadu     | 20           | 40           |
| Telangana      | 2            | 5            |


> **Only the employee share is deducted on the salary slip.** The employer share is visible in the LWF Register report for remittance purposes.

---

## 4. Employment State

LWF is determined by the **Employment State** set on the **Salary Structure Assignment**. The same field is used by Professional Tax, so it only needs to be set once per assignment.

---

## 5. Per-Employee Exemptions

Some employees may be exempt from LWF by local law (e.g., contract workers, employees above a certain grade in specific states, or directors). India Payroll provides a per-employee exemption flag.

### How to Exempt an Employee

1. Open the **Salary Structure Assignment** document.
2. Go to the **Labour Welfare Fund** section.
3. Check **LWF Exempted**.
4. Fill in **LWF Exemption Reason** (optional, for audit trail).

[Screenshot on the live page]

> **Key behaviour:** The `lwf_exempted` flag is **never auto-overridden** by the hook. Only an HR user with write access to the Employee document can change it. This ensures manual exemptions are preserved across all payroll runs.

---

<!-- page: frappe-hr/hr__india-payroll__multi-company-settings.md -->
---
title: "Multi-Company Settings"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/multi-company-settings"
updated: "2026-08-31"
---

Payroll Settings is a single, site-wide document, so by default, one India Payroll configuration applies to every company on the site. That works for a single legal entity, but a group running two or more entities has only one place to record an ESIC employer code or an EPF establishment code, and each registered entity has its own.

Multi-company payroll lifts that limit. It adds a table where you record statutory registration details per company, and it scopes statutory deductions to the companies you list.

It is **off by default**. Existing sites are unaffected until you turn it on.

[Screenshot on the live page]
*Multi-Company Settinga*

## **When you need it**

Turn it on when either is true:

- You run payroll for more than one company on this site, and they have **different** statutory registration numbers.
- Some companies on this site are registered under a scheme (EPF, ESIC, LWF, Professional Tax), and others are not. For example, a newly incorporated entity still below the headcount threshold.

You do **not** need it when every company on the site shares one registration, or when only one company runs payroll.

## **Enabling it**

1. Go to **Payroll Settings &gt; India Payroll**.
2. Under **Multi-Company Payroll**, tick **Enable Multi-Company Payroll**.
3. In the **Company Payroll Settings** table that appears, add a row for each company that participates in statutory payroll.
4. Save.

Each row holds:


| Field                                    | Description                                                                       |
| :---------------------------------------- | :--------------------------------------------------------------------------------- |
| **Company**                              | The company this row configures. Required, and each company may appear only once. |
| **ESIC Registration Number**             | 17-digit ESIC employer code for this company.                                     |
| **EPF Establishment Code**               | EPFO Establishment Code used in this company's ECR file header.                   |
| **Professional Tax Registration Number** | State Professional Tax enrolment / registration number.                           |
| **LWF Registration Number**              | State Labour Welfare Fund establishment registration number.                      |


Only **Company** is mandatory. Leave a registration number blank if the company is not registered under that scheme, or if you have not received the number yet.

While multi-company payroll is on, the site-wide **ESIC Registration Number** and **EPF Establishment Code** fields are hidden, so there is never any question about which value applies to a given company.

## **How it changes payroll**

The per-scheme checkboxes (**Enable Professional Tax Deduction**, **Enable ESIC Deduction**, **Enable LWF Deduction**, **Enable EPF Deduction**) remain the master switches. Multi-company payroll narrows their reach; it does not override them.

A statutory deduction is applied to a salary slip only when **both** are true:

1. The scheme is enabled in Payroll Settings, **and**
2. The slip's company appears in the Company Payroll Settings table.

A company with no row is treated as **not configured** and gets no statutory deduction:


| Multi-company | Scheme enabled | Company listed | Deduction applied |
| :------------- | :-------------- | :-------------- | :----------------- |
| Off           | No             | n/a            | No                |
| Off           | Yes            | n/a            | Yes               |
| On            | No             | Any            | No                |
| On            | Yes            | Yes            | Yes               |
| On            | Yes            | No             | **No**            |


This applies to all four schemes and takes effect the next time a salary slip is created or saved. Salary slips already submitted are not altered. See [Removing a company](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/setup/multi-company-payroll.md#removing-a-company) below.

One related behaviour: the Salary Structure Assignment warning about a missing **Employment State** is also scoped this way. Assignments for a company outside Professional Tax scope will not raise it.

## **How it changes reports**

The statutory registers (**Employee Provident Fund Register**, **ESIC Register** and **LWF Register**) follow the same scope, with one deliberate exception that protects filed records.

A salary slip appears in a register when **either**:

- its company is currently in scope for that scheme, **or**
- the slip **actually recorded** that deduction.

The second rule matters. A register is a record of liabilities that were incurred, not a projection of current configuration. If a company deducted ESI in June and you remove it from the table in September, the June contributions were still deducted from employees and remitted to ESIC, so they must remain reportable, and the June ECR file must still regenerate identically. The registers therefore never erase history when scope changes.

The practical effect of the two rules together:

- Slips from **before** a company was removed keep their deductions and stay reported.
- Slips created **after** removal carry no statutory deductions, so they drop out.

The **Bank Mandate Report** is not scoped, by design: it lists salary payment instructions, not statutory liabilities.

### **ECR export**

An ECR file is filed against a **single** EPF establishment code. Once codes are recorded per company, a file spanning several companies cannot be filed.

So while multi-company payroll is on, **Generate ECR File** requires a Company filter, and will show *"Select a Company before generating the ECR file"* if one is not set. In single-company mode, the filter stays optional, as before.

## **Validation**

Saving Payroll Settings enforces three rules:

- **A company may appear only once.** A duplicate is rejected, naming both row numbers.
- **Registration numbers are trimmed** of leading and trailing whitespace.
- **The table cannot be empty while multi-company payroll is on.** Without this, ticking the box would silently switch off every statutory deduction across the site.

## **Removing a company**

Removing a company's row stops it accruing new statutory deductions from the next salary slip onward. Its history is preserved: past slips keep the deductions they recorded, and those amounts continue to appear in the registers and the ECR export.

To also strip deductions from slips that are already **draft**, re-save them after removing the row. **Submitted** slips are unchanged. Amending a submitted slip to remove a statutory deduction is a payroll correction and should be done deliberately, not as a side effect of a settings change.

## **Turning it off**

Unticking **Enable Multi-Company Payroll** returns the site to a single shared configuration:

- The site-wide ESIC and EPF registration fields reappear, holding whatever they held before.
- Every company is back in scope for whichever schemes are enabled.
- The Company Payroll Settings rows are retained, so re-enabling restores your per-company details.

Check the site-wide registration numbers after switching back, since they are not populated from the table.

## **Developer reference**

`india_payroll/india_payroll/company_settings.py` is the single place that resolves statutory configuration. Use it rather than reading Payroll Settings fields directly, so behaviour stays consistent across schemes.

```python
from india_payroll.india_payroll.company_settings import (
    is_statutory_enabled,
    get_applicable_companies,
    get_registration_number,
)

```

`is_statutory_enabled(statute, company)` **→** `bool`

Whether a scheme applies to a company right now. This is the salary-slip gate. `statute` is one of `"professional_tax"`, `"esic"`, `"lwf"`, `"epf"`.

`get_applicable_companies(statute)` **→** `list[str] | None`

The company scope for a register. Three-valued, and the distinction matters:


| Return    | Meaning                                                                                                         |
| :--------- | :--------------------------------------------------------------------------------------------------------------- |
| `None`    | No restriction. Multi-company payroll is off, so reports behave exactly as they did before the feature existed. |
| `[]`      | Multi-company payroll is on but the scheme is globally disabled, so no company is currently in scope.           |
| `[names]` | Only these companies are currently in scope.                                                                    |


`None` is not the same as an empty list, and a caller that treats them alike will silently change single-company behaviour.

Because this returns *current* scope, never apply it as a bare filter to historical records. Combine it with evidence from the slip, as the registers do:

```python
applicable = get_applicable_companies("esic")
if applicable is not None:
    with_esi = get_slips_with_deduction([r.slip for r in rows], [ESI_EMPLOYEE_COMPONENT])
    rows = [r for r in rows if r.company in applicable or r.slip in with_esi]

```

`get_slips_with_deduction` lives in `india_payroll/india_payroll/utils.py`. It returns the subset of slips carrying a given deduction with a positive amount. Statutory deduction rows are only ever written when the amount is above zero, so a row's presence is the slip's own record that the liability was incurred, independent of how Payroll Settings is configured today.

`get_registration_number(statute, company)` **→** `str | None`

The registration identifier for a scheme. Reads the company's row when multi-company payroll is on, and falls back to the site-wide field otherwise.

## **Current limitations**

- **Registration numbers are stored but not yet consumed.** No report or export currently prints them: the ECR file format carries no header, and the ESIC Register has no registration column. The fields are in place so entities can be recorded correctly now, and so the values are available when those outputs are added.
- **No site-wide fallback for Professional Tax and LWF.** Those two registration numbers exist only on the per-company table. In single-company mode `get_registration_number` returns `None` for them.
- **Registers ignore the master switches in single-company mode.** With multi-company payroll off, the registers report computed liabilities regardless of whether the scheme's checkbox is ticked. This predates multi-company payroll and is unchanged by it.
- **TDS is configured separately.** Deductor details for Form 24Q (TAN, deductor type, responsible person) live on the Company record itself and were already per-company. They are not affected by this setting.
