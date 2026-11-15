<!-- Frappe documentation: frappe-hr, part 2 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__employee-advance.md -->
---
title: "Employee Advance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-advance"
updated: "2026-02-04"
---

**Sometimes employees go outside for company's work and company pays some amount for their expenses in advance. This is when the employee can create an Employee Advance form where details such as the Purpose of Expense and Expense Amount can be recorded.**

Once the Employee Advance is created by the Employee, the Expense Approver can submit the advance record after verification. After Employee Advance gets submitted, the accountant releases the payment and makes the Payment Entry.

To access Employee Advance, go to:

> Human Resources > Expense Claims > Employee Advance

**1. Prerequisites**
--------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Department](https://docs.frappe.io/hr/department)
3. [Chart of Accounts](https://docs.erpnext.com/docs/user/manual/en/chart-of-accounts)

**2. How to create an Employee Advance**
----------------------------------------

1. Go to: Employee Advance > New.
2. Select Employee to whom you need to give the advance.
3. Enter the Purpose and Advance Amount.
4. Under the Accounting section, select Mode of Payment. Advance Account will be fetched from the Default Employee Advance Account of your Company.
5. Save.

[Screenshot on the live page]

> Note: The Employee can only Save the Employee Advance but cannot Submit it. It can be only submitted by the Expense Approver.

### **2.1 Statuses**

These are the statuses that are automatically set for Employee Advance.

* **Draft**: A draft is saved but yet to be submitted.
* **Paid**: Advance has been Paid to the employee and a [Payment Entry](https://docs.erpnext.com/docs/user/manual/en/payment-entry) has been submitted.
* **Unpaid**: Advance is not paid out to the employee yet. A Payment Entry is not created against the advance.
* **Claimed**: After the advance is paid, the employee has claimed the entire *Paid Amount* via [Expense Claim](https://docs.frappe.io/hr/expense-claim).
* **Returned**: After the advance is paid, the employee has returned the entire *Paid Amount* and a return entry is submitted via Payment Entry/Journal Entry.
* **Partly Claimed and Returned**: After the advance is paid, the employee has partially claimed the *Paid Amount* via Expense Claim and returned the remaining amount via a submitted Payment Entry/Journal Entry.
* **Cancelled**: The Advance is cancelled due to any reason.

**3. Features**
---------------

### **3.1 Employee Advance Submission**

Employee Advance record can be created by any Employee but they cannot submit the record.

After saving Employee Advance, Employee should [Assign document to Approver](https://docs.erpnext.com/docs/v14/user/manual/en/using-erpnext/assignment). On assignment, approving user will also receive email notification. To automate email notification, you can also setup [Email Alert](https://docs.erpnext.com/docs/user/manual/en/notifications).

After verification, the Expense Approver can Submit (Accept) the Employee Advance form or Reject the request.

### **3.2 Make Payment Entry**

##### **Employee Advance via Payment Entry**

After submission of Employee Advance record, accounts user will be able to create a [Payment Entry](https://docs.erpnext.com/docs/user/manual/en/payment-entry) using the 'Create' button.

The Payment Entry will look like following:

[Screenshot on the live page]  


#### **Employee Advance Payment via Journal Entry**

Alternatively, a [Journal Entry](https://docs.erpnext.com/docs/user/manual/en/journal-entry) can also be created against the Employee Advance.

[Screenshot on the live page: Employee Advance Payment via Journal Entry]  


> Note: Make sure the Party Type is selected as Employee and the Reference Type is selected as Employee Advance.

[Screenshot on the live page: Employee Advance Payment via Journal Entry]  


#### **Employee Advance is Paid**

On submission of the Payment Entry/Journal Entry, the paid amount and status will be updated in Employee Advance record.

### **3.3 Adjust Advances on Expense Claim**

Later when the employee claims the expense, an advance record can be fetched in the [Expense Claim](https://docs.frappe.io/hr/expense-claim) and linked to the claim record.

### **3.4 Return Amount**

When advance is paid to an Employee, there are three situations:

* The amount may be unused
* All of it may be used
* Some part may be used

Create the Employee Advance, create a payment entry to indicate that the amount is paid.

* If amount is unused, click on the **Return** button to return the paid Advance amount [Screenshot on the live page: Return Button]
* If all of the advance is used, it will reflect in the Claimed Amount field
* If only some amount is claimed and rest is returned, the returned amount will be shown in the 'Returned Amount' field. [Screenshot on the live page: Return advance Amount]

> Note: (On Ledger Behaviour in v16 only):  
* Creating an **Employee Advance** does **not** create any GL (General Ledger) entry. The advance voucher is only a request/reservation.  
* The GL entry is created only when the **Payment Entry** (or Journal Entry) is submitted against the advance.  
* When an **Expense Claim** is made against the advance, the claim fetches the linked Payment Entry(s) along with the advance and uses those to adjust claim amounts, clear the advance, and record any exchange gain/loss (in case of multicurrency transaction).  
* In case of multiple payments against the same advance or partial claims/returns, each Payment Entry is separately referenced, ensuring full traceability and correct accounting.  

**4. Related Topics**
---------------------

1. [Expense Claim](https://docs.frappe.io/hr/expense-claim)

  

<!-- page: frappe-hr/hr__employee-attendance-tool.md -->
---
title: "Employee Attendance Tool"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-attendance-tool"
updated: "2026-02-04"
---

**Employee Attendance Tool allows you to mark the attendance of multiple employees for a particular date.**

To access the Employee Attendance Tool, go to:


> **Home > Human Resources > Attendance > Employee Attendance Tool**
> 
> 

This tool allows you to add attendance records for multiple employees based on their Department and Branch for a given day quickly.

**1. Prerequisites**
--------------------

Before creating an Employee Attendance, it is advised that you create the following first:

* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)
* [Branch](https://docs.frappe.io/hr/branch)

**2. How to mark attendance using Employee Attendance Tool**
------------------------------------------------------------

1. Enter the Date.
2. Select the Department and Branch (optional).
3. Select the Employees.
4. Mark Present, Absent, or Half Day as required.
5. You can also select the shift and mark employees with Late Entry and Early Exit from this view.
6. The Marked Attendance table below the tool will show you all the employees you have marked attendance for along with their attendance status. You can use column filters to search for a particular employee or employees with a particular status form this table.

[Screenshot on the live page]  



> **Note: Attendance cannot be marked for future dates.**
> 
> 

Once the attendance is marked using the Employee Attendance Tool, the employee attendance is saved in the [Attendance](https://docs.frappe.io/hr/attendance) record as shown:

[Screenshot on the live page]  


**3. Related Topics**
---------------------

1. [Attendance](https://docs.frappe.io/hr/attendance)
2. [Attendance Request](https://docs.frappe.io/hr/attendance-request)
3. [Upload Attendance](https://docs.frappe.io/hr/upload-attendance)
4. [Shift Management](https://docs.frappe.io/hr/shift-management)
5. [Auto Attendance](https://docs.frappe.io/hr/auto-attendance)

  

<!-- page: frappe-hr/hr__employee-benefit-application.md -->
---
title: "Employee Benefit Application"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-benefit-application"
updated: "2026-02-04"
---

Employees are entitled to flexible benefits which they can either receive pro-rata (as part of their Salary) or as a lump-sum amount when they claim the benefit. In order to choose from various flexible benefits which an Employee shall receive on a pro-rata basis, the employee should create a new Employee Benefit Application.

To create a new Employee Benefit Application,

> Human Resources > Payroll > Employee Benefit Application > New Employee Benefit Application

[Screenshot on the live page: Employee Benefit Application]  


Here, Employee can view the Max Benefits as per the Salary Structure Assignment and then chose from the Earning Components which are part of the employee's assigned Salary Structure. They can also enter the amount which they wish to receive as part of their Salary Slip.

It is based on the Employee Benefit Application that the Max Benefit Amount will be distributed among the flexible earning components while generating the Salary Slip. If an Employee fails to submit the Employee Benefit Application before processing the payroll, the Max Benefit Amount eligible to the employee will be distributed proportionately to each of the flexible component present in the Employee's salary structure.

> Note: Employees can only submit one Employee Benefit Application for a Payroll Period.

Employee Benefit Application should cover the full amount which the employee has to receive as per the Max Benefit amount on a pro-rata basis. However, if the Salary Structure of the employee consists of Salary Components which are to be paid on Employee Benefit Claim (Salary Component with *Pay Against Benefit Claim*), they are allowed to submit Employee Benefit Application excluding the amount allocated for such components.

Also, note that those components which are to be received based on Employee Benefit Claims can also be part of the application, but will only be disbursed lump-sum, as part of their salary when the Employee submits a claim for it.

> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before the last payroll, use *Deduct Tax For Unclaimed Employee Benefits* in Payroll Entry / Salary Slip while processing the Salary.

  

<!-- page: frappe-hr/hr__employee-benefit-claim.md -->
---
title: "Employee Benefit Claim"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-benefit-claim"
updated: "2026-02-04"
---

Employee Benefit Claim allows Employees to - 1. Claim flexible benefits which are to be received lump-sum (if Salary Component is *Pay Against Benefit Claim*) 2. Claim tax exemption for flexible benefits received pro-rata, as part of salary when *Deduct Tax For Unclaimed Employee Benefits* is checked in Payroll Entry / Salary Slip

You can create a new Employee Benefit Claim by going to, > Human Resources > Payroll > Employee Benefit Claim > New Employee Benefit Claim

[Screenshot on the live page: Employee Benefit Claim]  


Here, Employee can view the eligible amount as per their Salary Structure Assignment and claim for the amount which they wish to receive as part of their next Salary. Any remaining amount which the employee did not claim for, in a Payroll Period, will be disbursed as part of the last payroll Salary.

> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before the last payroll, use *Deduct Tax For Unclaimed Employee Benefits* in Payroll Entry / Salary Slip while processing the Salary.

  

<!-- page: frappe-hr/hr__employee-checkin.md -->
---
title: "Employee Checkin"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-checkin"
updated: "2026-02-04"
---

Employee Checkin is used to keep a log of all the check-ins and check-outs of an employee in the organization. Most organizations use this for attendance, shift management, and working hours calculations.

**1. Prerequisites**
--------------------

To create an Employee Checkin, you need to first create:

* [Employee](https://docs.frappe.io/hr/employee)

If you want shifts to be determined in employee checkins and want to process auto-attendance, then you need to create the following documents too:

* [Shift Type](https://docs.frappe.io/hr/shift-type)
* [Shift Assignment](https://docs.frappe.io/hr/shift-assignment) or set a default shift in Employee master.

**2. How to create an Employee Checkin**
----------------------------------------

#### **2.1 Creating logs manually**

To create a new Employee Checkin go to:


> **Human Resources > Attendance > Employee Checkin**
> 
> 

1. Click on New.
2. Select the Employee.
3. Set the date and time for the log.
4. Set Log Type as IN/OUT.
5. Save.
6. If you have set up shifts and shift assignments, the Employee Checkin will set the appropriate shift in which the timestamp falls after saving. If you have forgotten to assign a shift, causing the system to pick up the wrong one, you can re-fetch it by clicking on the 'Fetch Shift' button, as long as attendance has not already been marked for the same.
7. You can enable *Skip Auto Attendance* to skip that record while marking attendance.
8. You can also capture the location from where the employee has checked in or the Biometric Device ID.

[Screenshot on the live page]  


If auto attendance is enabled, the attendance record marked for a set of check-ins will be linked to the document later.

#### **2.2 Integrating Frappe HR with Biometric Devices**

If you are using a Biometric Device to log employee check-ins and check-outs you can use it to create records in Frappe HR. You can read more about this [here](https://docs.frappe.io/hr/integrating-frappe-hr-with-biometric-attendance-devices).

**3. Features**
---------------

### **3.1 Geolocation Tracking**

You can also track geolocation in employee checkins. To enable this, go to HR Settings and enable "**Allow Geolocation Tracking**"

[Screenshot on the live page]  


You can then click on the "**Fetch Geolocation**" button in the check-in form to fetch your current location

[Screenshot on the live page: geolocation-desk]  


It geolocation tracking has been enabled, it will be automatically captured while checking in from the mobile app too

[Screenshot on the live page: geolocation-mobile]  
### **3.2 Checkin log indicator**

Employee checkins fetch appropriate shift while saving based on the time of checkin or checkout log. If there is no active shift asssociated for the time of log, the employee checkin log is marked as **Off-Shift** indicating the lack of associated shift. Since auto-attendance works based on shift, these checkin logs are excluded while marking auto-attendance.


[Screenshot on the live page]

<!-- page: frappe-hr/hr__employee-flexible-benefits.md -->
---
title: "Flexible Benefits"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-flexible-benefits"
updated: "2026-02-04"
---

# Employee Benefits in HRMS

**Flexible benefit** plans allow employees to avail the **benefits** they want or need from a package of programs offered by an employer. They may include health insurance, pension plans, telephone expenses, etc.

 
To set Flexible Benefits in Frappe HR, follow the following steps:

---

## Types of Benefits
Once **Is Flexible Benefit** is enabled for a salary component, user can choose how to pay it out based on following scenarios:

1. **Accrue and payout at end of payroll period**

   * The benefit amount accrues each payroll cycle and is fully paid out in the final cycle.

2. **Accrue per cycle, pay only on claim**

   * The benefit accrues each cycle but is paid only when the employee submits an **Employee Benefit Claim**.
   * Payout is processed via Additional Salary.
   * *Optional:* Any unclaimed accrued balance can be auto-paid in the final cycle by enabling **Payout Unclaimed Amount in Final Payroll Cycle**.


3. **Allow claim up to the full period limit**

   * The employee can claim the entire annual benefit in one go. No accruals are created.

> **Note:** If *Depends on Payment Days* is enabled for a component, the monthly entitlement will be adjusted accordingly.

---

---

## Assigning Employee Benefits to Employees

* Configure employee benefits and their yearly amount in the **Salary Structure**. This acts as the template for employee benefits.
* When a Salary Structure is assigned to an employee, these details are copied into the **Salary Structure Assignment** and can be edited further if required.
* The final list and amounts in the Salary Structure Assignment are what the system considers.

[Screenshot on the live page]
---

## Employee Benefit Application

* Employees can opt for the benefits they want from those assigned in their Salary Structure Assignment.
* If no Benefit Application exists, the system falls back to the Salary Structure Assignment.
* To make a Benefit Application mandatory, enable **Mandatory Benefit Application** in Payroll Settings.

[Screenshot on the live page]

---

## Employee Benefit Ledger

* In the Salary Slip:

  * **Accrued Benefits** appear in the *Accrued Benefits* table.
  * **Payouts** appear as *Earnings*.
  * 
[Screenshot on the live page]

* After salary is processed, a **Benefit Ledger Entry** is created for every accrual and payout to keep track of balances.

---

## Employee Benefit Claim

Claims can be submitted only for these payout types:

* **Accrue per cycle, pay only on claim**

  * Claim limit = Total accrued so far + Current month’s entitlement
* **Allow claim up to the full period limit**

  * Claim limit = Total assigned amount

---

## Accrual Component in Salary Component

A new checkbox **Accrual Component** is available in the *Salary Component* doctype.

**Example use case:**

* HR wants to record a **Loyalty Bonus** equal to 5% of basic salary every month and pay it out after 10 months.
* Create a Salary Component *Loyalty Bonus*, enable **Accrual Component**, and add it to the Salary Structure with a formula.
* This accrual will:

  * Show in the salary slip as *Accrued Earnings*.
  * Not be included in gross pay or accounting entries.
  * Create an **Employee Benefit Ledger** entry for tracking.
* At the end of 10 months, the employer can create an *Additional Salary* for the accrued amount, which will then flow into gross pay, accounting, and tax calculations.

---

## Accrued Earnings Report

A report to track total accruals and payouts.

* For standard accruals, users can create an Additional Salary for pending payouts directly.
* For flexible benefits, payouts must be done via an **Employee Benefit Claim**.

[Screenshot on the live page]

<!-- page: frappe-hr/hr__employee-grade.md -->
---
title: "Employee Grade"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-grade"
updated: "2026-02-04"
---

**An Employee Grade is a grouping of employees with similar positions or values in order to assign compensation rates and salary structures.**

Frappe HR allows you to configure Employee Grades, helping you to easily categorize employees based on seniority or any other criteria.

Employee Grade also helps you fetch Employee records in bulk based on their grades while processing payroll, allocating leaves, etc.

To access Employee Grade, go to:


> **Home > Human Resources > Employee > Employee Grade**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Employee Grade, it is advisable you create the following documents:

* [Leave Policy](https://docs.frappe.io/hr/leave-policy)
* [Salary Structure](https://docs.frappe.io/hr/salary-structure)

**2. How to create an Employee Grade**
--------------------------------------

1. Go to Employee Grade list, click on New.
2. Enter the Name of the Employee Grade.
3. Enter the Default [Leave Policy](https://docs.frappe.io/hr/leave-policy) and Default [Salary Structure](https://docs.frappe.io/hr/salary-structure) for that Grade.
4. Save.

[Screenshot on the live page: Employee Grade]

Shown below are the different Employee Grades created.

[Screenshot on the live page: New Employee Grade]  


You also can access [Employee](https://docs.frappe.io/hr/employee), [Leave Period](https://docs.frappe.io/hr/leave-type), [Employee Onboarding Template](https://docs.frappe.io/hr/employee-onboarding) and [Employee Separation Template](https://docs.frappe.io/hr/employee-separation).

**3. Related Topics**
---------------------

1. [Leave Type](https://docs.frappe.io/hr/leave-type)

last

  

<!-- page: frappe-hr/hr__employee-group.md -->
---
title: "Employee Group"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-group"
updated: "2026-02-04"
---

**Employee Group is grouping of Employees based on some attributes such as Designation, Grade, Branch, etc.**

To access Employee Group, go to:


> **Home > Human Resources > Employee > Employee Group**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Employee Group, it is advisable you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)

**2. How to create an Employee Group**
--------------------------------------

1. Go to Employee Group list, click on New.
2. Enter the Name.
3. Select and add Employee ID to the group. The Employee Name will get automatically fetched.
4. Save.

[Screenshot on the live page: Employee Group]

**3. Features**
---------------

### **3.1 Service Level Agreement**

An Employee Group can be added to the [Service Level Agreement](https://docs.erpnext.com/docs/v14/user/manual/en/support/service-level-agreement) doctype, where the Service Level can be specified for a particular Employee Group.

**4. Related Topics**
---------------------

1. [Employment Type](https://docs.frappe.io/hr/employment-type)
2. [Branch](https://docs.frappe.io/hr/branch)
3. [Department](https://docs.frappe.io/hr/department)
4. [Designation](https://docs.frappe.io/hr/designation)
5. [Employee Grade](https://docs.frappe.io/hr/employee-grade)

last

  

<!-- page: frappe-hr/hr__employee-health-insurance.md -->
---
title: "Employee Health Insurance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-health-insurance"
updated: "2026-02-04"
---

**Employee Health Insurance is a benefit extended by the company to their employees. When a company provides health insurance assistance, they pay full or part premiums for the health insurance policy.**

Frappe HR allows you to save the Employee Health Insurance detail and link it to that particular Employee's master.

To access Health Insurance Provider document, go to:


> **Home > Human Resources > Employee > Employee Health Insurance**
> 
> 

**1. How to create an Employee Health Insurance**
-------------------------------------------------

1. Go to Employee Health Insurance list, click on New.
2. Enter the Health Insurance Name.
3. Save.

[Screenshot on the live page: Employee]

Additionally, in the Employee master, you can attach the Health Insurance Provider Name and fill in the Health Insurance No.

[Screenshot on the live page: Employee]  


**2. Related Topics**
---------------------

1. [Employee](https://docs.frappe.io/hr/employee)

last

  

<!-- page: frappe-hr/hr__employee-incentive.md -->
---
title: "Employee Incentive"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-incentive"
updated: "2026-02-04"
---

**Employee Incentives are a way of compensating and motivating employee performance apart from the usual salary.**

When an organization wants to encourage productivity among its employees, one of the options available is rewarding the Employee with an incentive. Frappe HR allows you to create Employee Incentives as and when required for a particular payroll entry.

To access Employee Incentive, go to: > Home > Human Resources > Payroll > Employee Incentive

**1. Prerequisites**
--------------------

Before creating an Employee Incentive, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Salary Component](https://docs.frappe.io/hr/salary-component)

**1. How to create an Employee Incentive**
------------------------------------------

1. Go to Employee Incentive list, click on New.
2. Select the Employee.
3. Enter the Incentive Amount.
4. Select the Payroll Date.
5. Select the [Salary Component](https://docs.frappe.io/hr/salary-component) under which you want to give the incentive.
6. Save and Submit.
7. On submit, the 'Additional Salary' document of the specified 'Salary Component' is created. This will be fetched while running the Payroll Entry.

[Screenshot on the live page: Employee Incentive]

**2. Related Topics**
---------------------

1. [Retention Bonus](https://docs.frappe.io/hr/retention-bonus)
2. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
3. [Salary Component](https://docs.frappe.io/hr/salary-component)
4. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__employee-lifecycle-management.md -->
---
title: "Employee Lifecycle Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-lifecycle-management"
updated: "2026-02-04"
---

Employee Lifecycle Management relates to the various stages an Employee goes through during the employment with an organization. It is important for most enterprises' HR departments to keep records of these changes that the employees go through across the company. Frappe HR simplifies these HR activities, read the following sections to understand how.

**1. Topics**
-------------

1. [Employee Onboarding](https://docs.frappe.io/hr/employee-onboarding)
2. [Employee Promotion](https://docs.frappe.io/hr/employee-promotion)
3. [Employee Separation](https://docs.frappe.io/hr/employee-separation)
4. [Employee Transfer](https://docs.frappe.io/hr/employee-transfer)
5. [Employee Skill Map](https://docs.frappe.io/hr/employee-skill-map)

  

<!-- page: frappe-hr/hr__employee-onboarding.md -->
---
title: "Employee Onboarding"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-onboarding"
updated: "2026-02-04"
---

**In the process of hiring an Employee, there are set of standard activities which need to be executed. This feature helps you to maintain the masters of these activities, and create a set of tasks at the time of each Employee hiring.**

Employee Onboarding is created for a Job Application, who is approved for the hiring.

**Use Case:** Let's assume that following are the activities which need to be performed as soon as a job applicant is approved to be hired.

* Perform a legal and professional background check
* Create an Employee master
* Create an Email Account
* Create an identity card
* Allocate leaves

In Frappe HR, these standard activities can be tracked in the Employee Onboarding Template. To access Employee Onboarding, go to:

> Human Resources > Employee Lifecycle > Employee Onboarding

**1. Prerequisites**
--------------------

Before creating an Employee Onboarding, it is advisable that you create the following documents:

* [Job Applicant](https://docs.frappe.io/hr/job-applicant)
* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)
* [Designation](https://docs.frappe.io/hr/designation)
* [Employee Grade](https://docs.frappe.io/hr/employee-grade)

**2. How to create an Employee Onboarding**
-------------------------------------------

1. Go to: Employee Onboarding > New.
2. Select the Job Applicant. once the Job Applicant is selected, the corresponding Employee will automatically get fetched.
3. Select the [Employee Onboarding Template](https://docs.frappe.io/hr/employee-onboarding#31-employee-onboarding-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Onboarding Template).
4. Enter Date of Joining.
5. Save and Submit.

[Screenshot on the live page: Onboarding Template]

> Note 1: If an Employee Onboarding Template isn't created, you can directly fill the onboarding information in the Employee Onboarding doctype itself.

> Note 2: The 'Status' of the Employee Onboarding will change to Completed once all the associated Activities are complete.

**3. Features**
---------------

### **3.1 Employee Onboarding Template**

The Employee Onboarding Template is a blueprint which contains a predefined list of Activities for Employee Onboarding. An Employee Onboarding Template can be created for a particular Department, Designation and Employee Grade.

To create a new Employee Onboarding Template:

1. Go to: Human Resources > Employee Lifecycle > Employee Onboarding Template > New.
2. Enter the Department, Designation and Employee Grade (optional).
3. Mention the Activities for onboarding. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
4. You can also schedule the Onboarding Activities by specifying the **Begin On (Days)** i.e. when the activity has to start and the **Duration (in Days)** for the same.

[Screenshot on the live page: Onboarding Template]

### **3.2 Tasks and Assignments**

On submission of the Employee Onboarding, a [Project](https://docs.erpnext.com/docs/v143/user/manual/en/projects/project) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v143/user/manual/en/projects/tasks) will also be created for each Activity. If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.

You can view the created Projects and Tasks as shown below:

[Screenshot on the live page: Onboarding Template]  


Additionally, each Activity can be assigned weights based on its importance.

[Screenshot on the live page: Tasks and Assignments]  


Based on the progress on the Tasks, progress can be updated in the Employee Onboarding process.

### **3.3 Employee Creation**

You can directly create an Employee through the Employee Onboarding doctype (if not already created) once all the mandatory onboarding tasks are complete.

[Screenshot on the live page: Onboarding Template]  


**4. Related Topics**
---------------------

1. [Employee Promotion](https://docs.frappe.io/hr/employee-promotion)
2. [Employee Separation](https://docs.frappe.io/hr/employee-separation)
3. [Employee Transfer](https://docs.frappe.io/hr/employee-transfer)

  

<!-- page: frappe-hr/hr__employee-other-income.md -->
---
title: "Employee Other Income"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-other-income"
updated: "2026-02-04"
---

**Employee Other Income is a document to declare other income of an employee from different sources.**

Other income of an employee is also important to calculate the income tax liability of an employee. In Frappe HR, an employee can declare their other income using this document.

To access Employee Other Income, go to: > Home > Human Resources > Employee Tax and Benefits > Employee Other Income

**1. How to create an Employee Other Income**
---------------------------------------------

1. Go to: Employee Other Income > New.
2. Select the Employee and Company.
3. Select the Payroll Period.
4. Enter the Amount and its Source.
5. Save and Submit.

[Screenshot on the live page: Employee Other Income]  


**2. Related Topics**
---------------------

1. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
2. [Salary Structure](https://docs.frappe.io/hr/salary-slip)
3. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__employee-performance-feedback.md -->
---
title: "Employee Performance Feedback"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-performance-feedback"
updated: "2026-02-04"
---

**The Employee Performance Feedback document allows you to capture 360° feedback on the employee's performance. Reviewers can rate the employee based on some criteria set up in the Appraisal Template and add a written feedback assessing the employee's performance throughout the cycle.**

To create an Employee Performance Feedback, go to:


> **Home > Human Resources > Performance > Employee Performance Feedback**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Performance Feedback, you should create the following:

* [Appraisal Template](https://docs.frappe.io/hr/appraisal-template)
* [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle)
* [Appraisal](https://docs.frappe.io/hr/appraisal)

**2. How to create an Employee Performance Feedback**
-----------------------------------------------------

### **2.1 From the Appraisal**

You can directly give feedback to an employee from their Appraisal document. If you have the required permissions, you can submit the performance feedback right from this view by clicking on the **New Feedback** button.

[Screenshot on the live page: add feedback]  


For more details about the feedback timeline check [Appraisal](https://docs.frappe.io/hr/appraisal#32-feedback)

### **2.2 Direct creation**

1. Go to the Employee Performance Feedback list, and click on New.
2. Select the Employee.
3. If your session user is linked to some employee, that employee will be auto-selected as the reviewer. Else you can select the reviewer.
4. Select the Appraisal document against which you want to give the feedback.
5. The feedback criteria set in the Appraisal Template in the Appraisal document will be pulled into the Feedback Ratings child table.
6. You can rate the employee for each criteria and add your feedback under the feedback.
7. Save and Submit.

[Screenshot on the live page: perf feedback]  


**3. Features**
---------------

### **3.1 Average Feedback Score**

On submitting a feedback, the average feedback score will be updated in the linked appraisal. Cancelling the feedback will update the score again.

### **3.2 Approvals for Appraisals**

If you don't want employees to submit feedback directly, You can also set up a [Workflow](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/workflows) for approvals before submission.

**3. Related Topics**
---------------------

1. [Appraisal](https://docs.frappe.io/hr/appraisal)

  

<!-- page: frappe-hr/hr__employee-promotion.md -->
---
title: "Employee Promotion"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-promotion"
updated: "2026-02-04"
---

**Promotion or career advancement is a process through which an Employee of a company is given a higher share of duties, a higher pay-scale or both.**

In Frappe HR, you can manage Employee Promotion and its various associated activities using this document.

To access Employee Promotion, go to:

> Human Resources > Employee Lifecycle > Employee Promotion

**1. Prerequisites**
--------------------

Before creating an Employee Promotion, it is advisable that you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)

**2. How to create an Employee Promotion**
------------------------------------------

1. Go to: Employee Promotion > New.
2. Select the Employee.
3. Enter the Promotion Date.
4. In the Employee Promotion Detail table, select the Property and set the Current and New value.

[Screenshot on the live page: Employee Promotion]

> Note: Promotion document can be submitted on or after Promotion Date. Once submitted all the changes added to Promotion Details table will be applied to the Employee. Frappe HR also keeps a record of all promotions of the Employee in the Employment History table in Employee document.

**3. Related Topics**
---------------------

1. [Employee Onboarding](https://docs.frappe.io/hr/employee-onboarding)
2. [Employee Separation](https://docs.frappe.io/hr/employee-separation)
3. [Employee Transfer](https://docs.frappe.io/hr/employee-transfer)

  

<!-- page: frappe-hr/hr__employee-referral.md -->
---
title: "Employee Referral"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-referral"
updated: "2026-02-04"
---


> **Introduced In Version 13**
> 
> 

Internal Recruitment is one of the best processes for recruitment, and it also saves effort and capital. The Employee Referral is a process where existing employees refer a suitable candidate from their network for a vacant designation/position.

In Frappe HR, you can manage Employee Referrals.

To access Employee Referral, go to:


> **Human Resources > Recruitment > Employee Referral**
> 
> 

**1. Prerequisites**
--------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
3. [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**2. How to create Employee Referral**
--------------------------------------

1. Go to Employee Referral > Add Employee Referral.
2. Fill in basic details of the person you want to refer like First Name, Last Name, Email, etc.
3. Select Employee under Referrer.
4. Save and Submit.

[Screenshot on the live page: employee referral doc]  


**3. Features**
---------------

### **3.1 Creating Job Applicant and auto-syncing status from Job Applicant**

When you submit an employee referral document the initial status will be "Pending". After submitting the document, the "Create Job Applicant" button will appear at the top right corner.

Clicking this button will create a new **Job Applicant** with the status "Open". The status of the **Employee Referral** document will change to "In Process"

[Screenshot on the live page: Create Job Applicant]  


When someone changes the status of the **Job Applicant** to "Hold" or "Replied", the status of the Employee Referral will remain "In Process". If the status of the Job Applicant changes to "Accepted" or "Rejected", the status of the **Employee Referral** document will also change to "Accepted" or "Rejected" respectively.

### **3.2 Managing referral bonus**

Many companies provide bonuses to their employees for such referrals. Frappe HR allows you to track the payment of the bonus to the employee for their referral.

For the Referral bonus, you need to check the "Is applicable for referral bonus" checkbox before submitting the document. After submitting the document, the "Create Additional Salary" button will appear at the top right corner, if the status is "Accepted".

[Screenshot on the live page: Referral Bonus]  


On Click, It will redirect you to the Additional salary form where you need to select Salary component and Payroll date and after that, you need to save and submit the document.

[Screenshot on the live page: Create Referral Bonus]  


  

<!-- page: frappe-hr/hr__employee-separation.md -->
---
title: "Employee Separation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-separation"
updated: "2026-02-04"
---

**Employee Separation is a situation when the service agreement of an Employee with his/her organization comes to an end and the Employee leaves the organization.**

Employee Separation is created for an Employee who has resigned or terminated from the organization.

**Use Case:** Let's assume that following are the activities which need to be performed as soon as an Employee needs to be separated from the organization.

* Collect laptop
* Clear dues
* Delete Employee Email Account
* Collect identity card

In Frappe HR, these standard activities can be tracked in the Employee Separation Template. To access Employee Separation, go to:

> Human Resources > Employee Lifecycle > Employee Separation

**1. Prerequisites**
--------------------

Before creating an Employee Separation, it is advisable that you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)
* [Designation](https://docs.frappe.io/hr/designation)
* [Employee Grade](https://docs.frappe.io/hr/employee-grade)

**2. How to create an Employee Separation**
-------------------------------------------

1. Go to: Employee Separation > New.
2. Select the Employee. Once the Employee is selected, the corresponding Employee information such as Department, Designation and Employee Grade will automatically get fetched.
3. Select the [Employee Separation Template](https://docs.frappe.io/hr/employee-separation#31-employee-separation-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Separation Template).
4. Enter the Resignation Letter Date.
5. Additionally, you can also enter the Exit Interview Summary.
6. Save and Submit.

[Screenshot on the live page: Separation Template]

> Note 1: If an Employee Separation Template isn't created, you can directly fill the separation information in the Employee Separation doctype itself.

> Note 2: The 'Status' of the Employee Separation will change to Completed once all the associated Activities are complete.

**3. Features**
---------------

### **3.1 Employee Separation Template**

The Employee Separation Template is a blueprint which contains a predefined list of Activities for Employee Separation. An Employee Separation Template can be created for a particular Department, Designation and Employee Grade.

To create a new Employee Separation Template:

1. Go to: Human Resources > Employee Lifecycle > Employee Separation Template > New.
2. Enter the Department, Designation and Employee Grade (optional).
3. Mention the Activities for separation. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
4. You can also schedule the Separation Activities by specifying the **Begin On (Days)** i.e. when the activity has to start and the **Duration (Days)** for the same.

[Screenshot on the live page: Separation Template]

### **3.2 Tasks and Assignments**

On submission of the Employee Separation, a [Project](https://docs.erpnext.com/docs/v13/user/videos/learn/project-and-task) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v13/user/videos/learn/project-and-task) will also be created for each Activity. If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.

You can view the created Projects and Tasks through View > Project/ Tasks.

Additionally, each Activity can be assigned weights based on its importance.

[Screenshot on the live page: Tasks and Assignments]  


Based on the progress on the Tasks, progress can be updated in the Employee Separation process.

### **3.3 Employee Status**

You can directly view the separated Employee through the Employee Separation doctype through View > Employee once the form is submitted.

**4. Related Topics**
---------------------

1. [Employee Onboarding](https://docs.frappe.io/hr/employee-onboarding)
2. [Employee Promotion](https://docs.frappe.io/hr/employee-promotion)
3. [Employee Separation](https://docs.frappe.io/hr/employee-separation)

  

<!-- page: frappe-hr/hr__employee-skill-map.md -->
---
title: "Employee Skill Map"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-skill-map"
updated: "2026-02-04"
---

Employee Skill Map is a record which helps your organization track your Employee's skill sets and trainings. It can be used to rate each skill of the Employee and track their growth after each internal training. This data can be used at the time of appraisals.

To record an Employee Skill Map go to:


> **Home > Human Resource > Employee Lifecycle > Employee Skill Map**
> 
> 

Make sure you have set the required Skills for designations from the Skill doctype.

Example of Skills for a Designation: [Screenshot on the live page: Designation Skills]  


**1. How to create an Employee Skill Map**
------------------------------------------

1. Go to the Employee Skill Map list, click on New.
2. Select the Employee.
3. Based on the designation of the Employee system will pull the Skills. Set the Proficiency level out of 5, and the Evaluation Date.
4. If the Employee is lacking in any skill, you can schedule trainings for the Employee.
5. Under the Trainings table, select the Training Event and the Training Date.
6. Save.

[Screenshot on the live page: Employee Skill Map]  


  
