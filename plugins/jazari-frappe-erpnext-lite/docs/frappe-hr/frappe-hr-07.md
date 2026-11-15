<!-- Frappe documentation: frappe-hr, part 7 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__leave-encashment.md -->
---
title: "Leave Encashment                                          "
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-encashment"
updated: "2026-02-04"
---

**Leave Encashment refers to an amount of money received in exchange for Leaves not availed by an Employee. You can submit Leave Encashment for Leave Types which are encashable.**

To access Leave Encashment, go to:

> Home > Human Resources > Leaves > Leave Encashment

**1. Prerequisites**
--------------------

Before creating Leave Encashment, it is advisable you create the following documents:

1. [Employee](https://docs.frappe.io/hr/leave-allocation)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Period](https://docs.frappe.io/hr/leave-period)
5. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
6. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)

**2. How to create a Leave Encashment**
---------------------------------------

1. Go to Leave Encashment list, click on New.
2. Select Leave Period.
3. Select the Employee. Once the Employee is selected, the Employee's Department is automatically fetched.
4. Select Leave Type for which the Leave is encashed. Make sure the Leave Type is encashable (the 'Allow Encashment' checkbox in the Leave Type is checked).
5. Select Encashment Date, if you want payment via Salary Slip. Based on the date selected, the amount will be encashed in that particular Payroll Entry.
6. Save and Submit.

![Leave Encashment](https://frappehr.com/files/leave-encashment-new.png)

> **Note:** As you select Employee and Leave Type, Leave Balance and Encashable Days (which is total leave balance minus the threshold days set in Leave Type) will be shown along with the Encashment Amount based on the Leave Encashment per day as configured in the Employee's assigned Salary Structure.

**3. Leave Encashment Payment Methods**
---------------------------------------

In Frappe HR, we allow you to pay the encashment amount via Salary Slip or Payment Entry.

### **3.1 Payment via Payment Entry**

1. To pay the Leave Encashment amount via Payment Entry you need to check Pay via Payment Entry checkbox. 
2. After that, it will allow you to select Payable Account and Expense Account. 
3. After Submitting the record click on the button "Create Payment Entry" which will redirect you to the Payment Entry Form fill in the details, save, and submit.

### **3.2 Payment via Salary Slip**

1. To pay the Leave Encashment amount via Salary Slip you need to make sure that checkbox Pay via Payment Entry is unchecked.
2. Select the Encashment Date. Based on the date selected, the amount will be encashed in that particular Payroll Entry. Save and Submit. 
On submitting a Leave Encashment for an Employee, Frappe HR automatically creates an [Additional Salary](https://docs.frappe.io/hr/additional-salary) which will get added to the Salary Slip of the Employee when processing the payroll.


**3. Related Topics**
---------------------

1. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
2. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
3. [Additional Salary](https://docs.frappe.io/hr/additional-salary)

  

<!-- page: frappe-hr/hr__leave-ledger-entry.md -->
---
title: "Leave Ledger Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-entry"
updated: "2026-02-26"
---

A unified ledger for all leave related transactions for an employee. This maintains all the leaves related transactions, this includes the leave allocations, leave applications and leave encashments of your employees.

![Leave Ledger Entry](https://frappehr.com/files/leave-ledger-entry.png)  


  

<!-- page: frappe-hr/hr__leave-ledger-report.md -->
---
title: "Leave Ledger Report"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-report"
updated: "2026-02-26"
---

This report allows you to view the ledger impact for all your leave-related transactions:

1. Leave Allocation
2. Leave Application
3. Leave Encashment

![ledger-report](https://frappehr.com/files/ledger-report.png "ledger-report.png")  


This report gives you an overview of:

1. Ledger entry creation date
2. Ledger transaction dates (From Date - To Date)
3. Leaves (added/consumed/deducted)
4. Leave Type
5. Linked transaction details (Type & Name)
6. Any special flags: Is Carry Forward, Is Expired, Is Leave Without Pay
7. Company & Holiday List linked to it

You can use the **View Ledger** button in transactions to view the linked ledger entries in the report view

![leave-ledger](https://frappehr.com/files/leave-ledger.gif "leave-ledger.gif")  


  

<!-- page: frappe-hr/hr__leave-management__help-articles__how-to-sanction-leave-encashment-amount-in-salary-slip.md -->
---
title: "How to Sanction Leave Encashment Amount in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/how-to-sanction-leave-encashment-amount-in-salary-slip"
updated: "2026-07-05"
---

Leave Encashment is used to pay an employee for unused leaves. In Frappe HR, this amount can be paid through a **Salary Slip** or through a separate **Payment Entry**.

This article explains how to sanction the leave encashment amount through Salary Slip.

## When To Use This

Use this method when the encashment amount should be paid along with the employee's regular payroll.

For example, if an employee has unused earned leaves at the end of the year, you can create a Leave Encashment record and include the encashment amount in the employee's Salary Slip for that payroll period.

## Prerequisites

Before creating Leave Encashment, make sure the following are configured:

- The employee has an active **Salary Structure Assignment**.
- The **Leave Type** is marked as encashable.
- The Leave Type has an **Earning Component** set for encashment.
- The employee has a submitted **Leave Allocation** for that Leave Type.
- The employee has unused leave balance available for encashment.
- The per-day encashment amount is set in the Salary Structure or Salary Structure Assignment.

## Step 1: Enable Encashment In Leave Type

Open the relevant **Leave Type** and enable **Allow Encashment**.

You can also configure limits such as:

- Non-encashable leaves
- Maximum encashable leaves
- Earning Component

The Earning Component is important because it decides which salary component will be used when the encashment amount is added to payroll.

## Step 2: Set Leave Encashment Amount Per Day

Open the employee's **Salary Structure** or **Salary Structure Assignment** and set the leave encashment amount per day.

Frappe HR uses this amount to calculate:

```text
Encashment Amount = Encashment Days x Leave Encashment Amount Per Day
```

If the per-day amount is not set, the encashment amount may be calculated as zero.

## Step 3: Create Leave Encashment

Go to:

```text
Home > Human Resources > Leaves > Leave Encashment
```

Create a new Leave Encashment record and select:

- Leave Period
- Employee
- Leave Type
- Encashment Date

The system fetches the employee's leave balance and calculates the encashable days and encashment amount.

## Step 4: Pay Through Salary Slip

To pay the amount through Salary Slip, keep **Pay Via Payment Entry** unchecked.

When the Leave Encashment is submitted, Frappe HR creates an **Additional Salary** record for the employee. This Additional Salary record is linked to the Leave Encashment and uses the earning component selected in the Leave Type.

## Step 5: Process Payroll

Create the **Payroll Entry** or **Salary Slip** for the payroll period that includes the encashment date.

When the Salary Slip is created, the Additional Salary from the Leave Encashment is included in the employee's earnings.

Review the Salary Slip and check that:

- The encashment earning component is visible.
- The amount is correct.
- The total earnings include the encashment amount.

Submit the Salary Slip to sanction and pay the amount through payroll.

## Example

An employee has 5 earned leaves available for encashment.

The leave encashment amount per day is set to 1,000.

```text
5 x 1,000 = 5,000
```

When the Leave Encashment is submitted, Frappe HR creates an Additional Salary for 5,000. The amount is then added to the Salary Slip for the payroll period that includes the encashment date.

## Common Checks

If the encashment amount is not appearing in the Salary Slip, check the following:

- The Leave Encashment is submitted.
- **Pay Via Payment Entry** is not checked.
- The encashment date falls within the Salary Slip or Payroll Entry period.
- The Additional Salary record was created.
- The Additional Salary payroll date is within the payroll period.
- The Leave Type has an earning component.
- The employee has an active Salary Structure Assignment.
- The leave encashment amount per day is configured.

## Salary Slip Or Payment Entry?

Use **Salary Slip** when the encashment should be part of payroll and paid along with salary.

Use **Payment Entry** when the encashment should be paid separately and accounted for directly through accounts.

## Related Topics

- [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)
- [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
- [Additional Salary](https://docs.frappe.io/hr/additional-salary)

<!-- page: frappe-hr/hr__leave-management__help-articles__leave-calculation-in-salary-slip.md -->
---
title: "Leave Calculation in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/leave-calculation-in-salary-slip"
updated: "2026-07-05"
---

Frappe HR calculates leave impact in the Salary Slip by reducing the employee's payable days for the payroll period. This is mainly controlled by Leave Without Pay, Partially Paid Leave, attendance records, holidays, and the employee's joining or relieving date.

The calculation decides two important values in the Salary Slip:

- **Total Working Days**
- **Payment Days**

The salary components that depend on payment days are calculated based on the final Payment Days.

## How Leave Affects Salary Slip

When a Salary Slip is created, Frappe HR checks the payroll period and calculates how many days the employee should be paid for.

In simple terms:

```text
Payment Days = Eligible Working Days - Leave Without Pay - Absent Days
```

The exact calculation can change depending on payroll settings, holiday settings, attendance records, and leave type settings.

## Leave Without Pay

If an employee has an approved Leave Application for a Leave Type marked as **Leave Without Pay**, those days reduce the Payment Days in the Salary Slip.

For example, if the payroll period has 30 working days and the employee has 2 days of Leave Without Pay:

```text
Payment Days = 30 - 2 = 28
```

Salary components that depend on payment days are then calculated for 28 days instead of 30.

## Partially Paid Leave

Frappe HR also supports **Partially Paid Leave**. In this case, the leave does not reduce the full day's salary. It reduces salary based on the fraction configured in the Leave Type.

For example, if a leave type pays 50% of daily salary for one day, the Salary Slip treats it as a partial reduction instead of a full Leave Without Pay day.

Use Partially Paid Leave when employees should receive part of their salary during a leave period.

## Calculation Based On Leave Application Or Attendance

Payroll can be calculated based on either leave applications or attendance records, depending on the payroll configuration.

### Based On Leave Application

When payroll is based on leave applications, Frappe HR checks approved leave records during the Salary Slip period.

It considers:

- Leave Without Pay
- Partially Paid Leave
- Half-day leave
- Whether the Leave Type includes holidays

### Based On Attendance

When payroll is based on attendance, Frappe HR checks submitted Attendance records for the Salary Slip period.

It considers:

- Absent days
- Half-day attendance
- Attendance marked on holidays, depending on settings
- Leave Type used in attendance records
- Unmarked attendance, depending on payroll settings

If unmarked attendance is configured to be treated as absent, those unmarked days can also reduce Payment Days.

## Half-Day Leave And Half-Day Attendance

Half-day leave or half-day attendance reduces salary based on the half-day fraction configured in payroll settings.

For example, if the daily wages fraction for half day is 0.5, then one half-day Leave Without Pay reduces Payment Days by 0.5.

## Holidays In Salary Slip Calculation

Holiday handling depends on payroll settings and the employee's holiday list.

If holidays are included in total working days, holidays are part of the working day count.

If holidays are not included, holidays are removed from Total Working Days before Payment Days are calculated.

Some Leave Types can also be configured to include holidays. If holidays are included for that Leave Type, leave falling on holidays may be considered in the leave calculation.

## Joining Date And Relieving Date

Salary Slip calculation also considers the employee's joining and relieving dates.

If an employee joins in the middle of the payroll period, Payment Days are calculated from the joining date.

If an employee leaves in the middle of the payroll period, Payment Days are calculated only up to the relieving date.

This prevents salary from being calculated for dates before joining or after relieving.

## Example

Suppose the payroll period is from 1 April to 30 April.

- Total days in period: 30
- Holidays excluded from working days: 4
- Total Working Days: 26
- Leave Without Pay: 2
- Half-day Leave Without Pay: 0.5

The Payment Days will be:

```text
26 - 2 - 0.5 = 23.5
```

Salary components that depend on payment days are calculated for 23.5 payment days.

## Why The Salary Amount May Look Different

If the salary amount in the Salary Slip is not what you expected, check:

- Whether payroll is based on Attendance or Leave Application.
- Whether the Leave Application is submitted and approved.
- Whether the Leave Type is marked as Leave Without Pay or Partially Paid Leave.
- Whether holidays are included in Total Working Days.
- Whether the Leave Type includes holidays.
- Whether attendance is marked for the full period.
- Whether unmarked attendance is treated as absent.
- Whether the employee joined or left during the payroll period.
- Whether the salary component depends on payment days.

## Components That Depend On Payment Days

Only salary components configured to depend on payment days are reduced based on leave calculation.

If a component does not depend on payment days, it may remain the same even when Payment Days are reduced.

Check the Salary Component and Salary Structure configuration if a particular earning or deduction is not changing as expected.

## Related Topics

- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Settings](https://docs.frappe.io/hr/payroll-settings)
- [Leave Application](https://docs.frappe.io/hr/leave-application)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Attendance](https://docs.frappe.io/hr/attendance)
- [Holiday List](https://docs.frappe.io/hr/holiday-list)
- [Salary Component](https://docs.frappe.io/hr/salary-component)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)

<!-- page: frappe-hr/hr__leave-management__help-articles__setting-employee-wise-leave-approver.md -->
---
title: "Setting Employee Wise Leave Approver"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/setting-employee-wise-leave-approver"
updated: "2026-07-05"
---

Frappe HR supports more than one way to decide who should approve an employee's leave application. The right method depends on whether the approver is specific to one employee, shared by a department, or selected while creating the leave application.

## 1. Set Leave Approver In Employee Master

Use this when an employee should always have a specific default leave approver.

Steps:

1. Open the employee record from **Employee**.
2. Go to the **Attendance and Leave Details** section.
3. Select the **Leave Approver** for that employee.
4. Save the employee record.

When the employee creates a **Leave Application**, Frappe HR automatically fetches this approver as the default **Leave Approver**.

This is the best option when approvals are handled by each employee's reporting manager or by a specific HR person.

## 2. Set Leave Approvers In Department

Use this when all employees in a department should be approved by one or more department-level approvers.

Steps:

1. Open the relevant **Department**.
2. Add one or more users in the **Leave Approvers** table.
3. Save the department.

When an employee from that department applies for leave, the department leave approvers are available on the Leave Application.

If both employee-wise and department-wise approvers are configured, the approver set in the employee master is used as the default approver, while department approvers can also be available for selection.

## 3. Select The Leave Approver On Leave Application

The **Leave Approver** field is also available on the **Leave Application** itself.

When creating a leave application:

1. Select the employee.
2. Select the leave type and dates.
3. Check the **Leave Approver** field.
4. Change the approver if another eligible approver should approve this specific request.

This is useful for exceptions, temporary reporting changes, or cases where a leave request should go to a different approver than usual.

## 4. Use User Permissions For Department-Level Access

Setting the approver decides who can be selected as the approver. Access can be controlled separately using **User Permissions**.

For example, if a department manager should only see and approve leave applications from their own department, configure User Permissions for that approver based on:

- Company
- Department
- Employee

This keeps the approval process clean and prevents approvers from seeing leave applications outside their permitted scope.

## Which Method Should You Use?

Use employee-wise approver when each employee has a fixed manager or approver.

Use department-wise approver when the same approver or approver group handles leaves for an entire department.

Use the Leave Application approver field when the approver needs to be changed for a specific request.

Use User Permissions when you also need to restrict what leave records an approver can access.

## Important Notes

- The approver must be a valid Frappe user.
- The approver should have the **Leave Approver** role.
- Employee-wise approver is treated as the default when both employee and department approvers are configured.
- Department approvers are useful for shared approval responsibility.
- User Permissions control access; they do not replace setting the approver.

## Related Topics

- [Setting Employee-wise Leave Approver](https://docs.frappe.io/hr/setting-employee-wise-leave-approver)
- [Department-wise Leave Approval in ERPNext](https://docs.frappe.io/hr/department-wise-leave-approval-in-erpnext)
- [Leave Application](https://docs.frappe.io/hr/leave-application)
- [Employee](https://docs.frappe.io/hr/employee)
- [Department](https://docs.frappe.io/hr/department)
- [HR Settings](https://docs.frappe.io/hr/hr-settings)

<!-- page: frappe-hr/hr__leave-period.md -->
---
title: "Leave Period"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-period"
updated: "2026-02-04"
---

**A Leave Period is a duration of time for which leaves are allocated.**

Most companies manage leaves based on a Leave Period, corresponding to a calendar year or the fiscal year. To access Leave Period, go to:

> Home > Human Resources > Leaves > Leave Period

**1. Prerequisites**
--------------------

Before creating a Leave Period, it is advisable to create the following:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)

**2. How to create a Leave Period**
-----------------------------------

1. Go to Leave Period list, click on New.
2. Enter the From Date and To Date of the Leave Period.
3. Select the Company name for which the Leave Period is applicable.
4. Save.

The Leave Period also allows you to select a [Holiday List for Optional Leaves](https://docs.frappe.io/hr/holiday-list) (optional) which will be considered for allocating Optional Leaves for the period.

> **Note:** The 'Holiday List for Optional Leaves' is not the same as the usual 'Holiday List'. This list will contain a list of optional holidays only. 'Holiday List for Optional Leaves' can be created from the [Holiday List](https://docs.frappe.io/hr/holiday-list) document. You can create two Holiday Lists for a Leave Period; one containing the usual set of holidays and the other for optional holidays.

Additionally, you can check the 'Is Active' checkbox if you want to enable this particular Leave Period.

![Leave Period](https://frappehr.com/files/leave-period.png)  


**3. Granting leaves based on Leave Period**
--------------------------------------------

To grant leaves based on Leave Period, use the [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment).

**4. Related Topics**
---------------------

1. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
2. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
3. [Leave Type](https://docs.frappe.io/hr/leave-type)


  

<!-- page: frappe-hr/hr__leave-policy-assignment.md -->
---
title: "Leave Policy Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-policy-assignment"
updated: "2026-02-04"
---


> **Introduced in Version 13**
> 
> 

Leave Policy Assignment in Frappe HR is used to assign leaves to employees based on created policies. To access Leave policy assignment, go to:


> **Home > Human Resources > Leaves > Leave Policy Assignment**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)

**2. How to create a Leave Policy Assignment**
----------------------------------------------

1. Go to Leave Policy Assignment, click on New.
2. Select Employee and Leave Policy.
3. Select Assignment based on the following as needed:


	* If "Assignment based on" is set to Leave Period, you need to select the applicable Leave Period. The Effective From and Effective To dates will be set automatically based on the Leave Period selected.
	* If "Assignment based on" is set to Joining Date, the Effective From date will be set to the employee's Date of Joining.
	* If "Assignment based on" is left blank, then you will have to set the Effective From and Effective To date manually.
4. Save and Submit.

![Leave Policy Assignment](https://frappehr.com/files/leave-policy-assignment.png)  


On submission, Leave Allocation documents would be created automatically based on the [Leave Policy](https://docs.frappe.io/hr/leave-policy) as shown below.

![Leave Allocations](https://frappehr.com/files/granted-leaves.png)  


**3. Features**
---------------

### **3.1 Bulk Leave Policy Assignment**

Frappe HR also allows creating Leave Policy Assignments for multiple employees at once.

1. Go to the Leave Policy Assignment list.
2. Click on Bulk Leave Policy Assignment.
3. This will take you to the [Leave Control Panel](https://docs.frappe.io/hr/leave-control-panel), where you can assign Leave Policies in bulk.

![](https://frappehr.com/files/NUL3M8C.png)  


### **3.2 Allocating Earned Leaves**

Leave Policy Assignments can also be used to allocate [Earned Leaves](https://docs.frappe.io/hr/configuring-earned-leave).

  

<!-- page: frappe-hr/hr__leave-policy.md -->
---
title: "Leave Policy"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-policy"
updated: "2026-02-04"
---

**The amount of entitled leaves in a Company for an Employee in a Leave Period is known as Leave Policy.**

It is a practice for many enterprises to enforce a general Leave Policy to effectively track and manage Employee leaves. Frappe HR allows you to create and manage multiple Leave Policies and allocate leaves to Employees as defined by the policy.

To access Leave Policy, go to:


> **Home > Human Resources > Leaves > Leave Policy**
> 
> 

**1. How to create a Leave Policy**
-----------------------------------

1. Go to Leave Policy list, click on New.
2. Select the Leave Type and enter its Annual Allocation.
3. Save and Submit.

![Leave Policy](https://frappehr.com/files/leave-policy.png)

Once submitted, you can create [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment) to assign this policy to multiple employees.

**2. Related Topics**
---------------------

1. [Leave Period](https://docs.frappe.io/hr/leave-period)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment)

  

<!-- page: frappe-hr/hr__leave-type.md -->
---
title: "Leave Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-type"
updated: "2026-07-15"
---

**Leave Type refers to the types of leaves allocated to an Employee which they can use while making Leave Applications.**

You can create any number of Leave Types based on your company’s requirements.

To access Leave Type, go to:


> **Home > Human Resources > Leaves > Leave Type**
> 
> 

**1. How to create a Leave Type**
---------------------------------

1. Go to Leave Type list, click on New.
2. Enter Leave Type Name.
3. Enter Maximum Leave Allocation Allowed, Applicable After (Working Days), Maximum Consecutive Leaves Allowed (optional).
4. Save.

![](/files/leave-type-settings.png)

Below is a detailed explanation of all the fields and checkboxes in Leave Type.

* **Maximum Leave Allocation Allowed per Leave Period:** This field allows you to set the maximum number of the allocation allowed per Leave Period of this Leave Type while creating the Leave Policy.
* **Allow Leave Application After (Working Days):** Enter the minimum number of working days here. Only the employees who have worked for this number of days or more since their Date of Joining will be allowed to apply for this particular leave type. Any other leaves (such as Casual Leave, Sick Leave.etc.) availed by the Employees after their joining date will also be considered while calculating working days of the Employee.
* **Maximum Consecutive Leaves Allowed:** It refers to the maximum number of days this particular Leave Type can be availed at a stretch. If an employee exceeds the maximum number of days, their extended leave will be considered as ‘Leave Without Pay'.
* **Is Carry Forward:** If checked, the balance leaves of this Leave Type will be carried forward to the next allocation period.
* **Is Leave Without Pay:** This ensures that the Leave Type will be treated as leaves without pay and salary will get deducted for this Leave Type.
* **Is Optional Leave:** Optional Leaves are holidays that Employees can choose to avail from a list of holidays published by the company. The Holiday List for Optional Leaves can have any number of holidays, but you can restrict the number of such leaves by setting the Max Days Leave Allowed field.
* **Allow Negative Balance:** If checked, the system will always allow to apply and approve [Leave Applications](https://docs.frappe.io/hr/leave-application) for the Leave Type, even if there is no leave balance.
* **Allow Over Allocation:** If checked, the system will allow allocating more leaves than the number of days in the allocation period. Enabling this option does not bypass or override the limit configured in the **Maximum Leave Allocation Allowed per Leave Period** field.
* **Include holidays within leaves as leaves:** Check this option if you wish to count holidays within leaves as a ‘leave’. For example, if an Employee has applied for leave on Friday and Monday, and Saturday and Sunday are weekly offs, if the 'Include holidays within leaves as leaves' checkbox for the Leave Type is checked, the system will consider Saturday as Sunday as leaves too. Such holidays will be deducted from the total number of leaves.
* **Is Compensatory:** Compensatory leaves are leaves granted for working overtime or on holidays, normally compensated as an encashable leave. You can check this option to mark the Leave Type as compensatory. An Employee can request for compensatory leaves using [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request).


> **Introduced in version 13**
> 
> 

* **Is Partially Paid Leaves:** This checkbox ensures that Leave Type will be treated as partially paid and some part of daily earnings will be paid through salary slip. If this checkbox is enabled then a field "Fraction of Daily Salary Per Leave" appears where you can define the fraction of daily salary paid on the partial leave day.

![](https://frappehr.com/files/8IeXPo5.png)


> **Note: The Leave Type can be either Leave Without pay or Partially Paid.**
> 
> 

**2. Features**
---------------

### **2.1 Leave Encashment**

It is possible that Employees can receive cash from their Employer for unused leaves granted to them in a Leave Period. Not all Leave Types need to be encashable, so, you should set "Allow Encashment" for only those Leave Types which are encashable.


> **Note: Leave encashment is allowed only in the last month of the Leave Period.**
> 
> 

![](https://frappehr.com/files/N7AiiYE.png)  


**Non-Encashable Leaves:** This field indicates the number of leave days the Employees won't be able to encash. Above the mentioned days, the Employee is eligible to encash leaves.

For example, if there are 10 leaves of a particular Leave Type which is encashable, and the Employee has 8 leaves left. If Non-Encashable Leaves = 5, the Employee is given encashment of only 8 - 5 = 3 leaves.

**Earning Component:** This field allows you to specify the Salary Component that will be encashed to Employees as a part of their Salary in the Salary Slip.


> **Note: On submitting a** [**Leave Encashment**](https://docs.frappe.io/hr/leave-encashment) **for an Employee, Frappe HR automatically creates an** [**Additional Salary**](https://docs.frappe.io/hr/additional-salary) **which will get added to the Salary Slip of the Employee when processing the next payroll.**
> 
> 

### **2.2 Earned Leave**

Earned Leaves are leaves earned by an Employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro-rata basis by automatically updating Leave Allocation for leaves of this type at intervals set by 'Earned Leave Frequency'.

For example, an Employee is allotted 24 Privilege Leaves in a year, wherein the Privilege Leave is set as Earned Leave with Monthly allotment. In this case, the Employee will earn 2 (24 leaves/12 months) Privilege Leaves at the end of every month. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type and will round to 'Rounding' for fractions.

![](https://frappehr.com/files/1SrI5mm.png)  



> **Note: The initial allocation of this Leave Type will be 0. Leaves will be updated at the end of the Month (or as per the 'Earned Leave Frequency' set).**
> 
> 

### **2.3 Default Leave Types**

There are some pre-loaded Leave Types in the system, as below:

* **Leave Without Pay:** You can avail these leaves for different purposes, such as extended medical issues, educational purposes, or unavoidable personal reasons. The 'Leave Without Pay' checkbox for this Leave Type is checked by default. The employee does not get paid for such leaves.
* **Privilege leave:** These are like earned leaves that can be availed for travel, family vacation, and so on.
* **Sick leave:** You can avail of these leaves if you are unwell.
* **Compensatory off:** These are compensatory leaves allotted to employees for overtime work. The 'Is Compensatory' checkbox for this Leave Type is checked by default.
* **Casual leave:** You can avail of this leave to take care of urgent and unseen matters.

**3. Related Topics**
---------------------

1. [Leave Period](https://docs.frappe.io/hr/leave-period)
2. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
3. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
4. [Leave Application](https://docs.frappe.io/hr/leave-application)
5. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
6. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)

  

<!-- page: frappe-hr/hr__leaves.md -->
---
title: "Leaves"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leaves"
updated: "2026-02-04"
---

This section will help you understand how Frappe HR enables you to efficiently manage the leave schedule of your organization. It also explains how employees can apply for leaves.

The number and type of leaves an Employee can apply is controlled by Leave Allocation. You can create Leave Allocation for a Leave Period based on the Company's Leave Policy. You can also allocate Additional Leaves to your employees and generate reports to track leaves taken by Employees.

Employees can also create leave requests, which their respective managers (leave approvers) can approve or reject. An Employee can select leaves from a number of leave types such as Sick Leave, Casual Leave, Privilege Leave and so on.

**Related Topics**
------------------

1. [Holiday List](https://docs.frappe.io/hr/holiday-list)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Period](https://docs.frappe.io/hr/leave-period)
4. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
5. [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment)
6. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
7. [Leave Control Panel](https://docs.frappe.io/hr/leave-control-panel)
8. [Leave Application](https://docs.frappe.io/hr/leave-application)
9. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
10. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
11. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)
12. [Leave Ledger Entry](https://docs.frappe.io/hr/leave-ledger-entry)

  

<!-- page: frappe-hr/hr__loan-application.md -->
---
title: "Loan Application"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan-application"
updated: "2026-02-04"
---

**Loan Application is a document which contains the information regarding the Loan Applicant, Loan Type, Repayment Method, Loan Amount and Rate of Interest.**

Employee can apply for loan by going to:

> Human Resources > Loan > Loan Application

**1. Prerequisites**
--------------------

Before creating a Loan Application, it is advisable to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Loan Type](https://docs.frappe.io/hr/loan-type)

**2. How to create a Loan Application**
---------------------------------------

1. Go to: Loan Application > New.
2. Enter the Applicant name.
3. Enter loan information such as a Loan Type, Loan Amount and Required by Date.
4. Select the [Repayment Method](https://docs.frappe.io/hr/loan-application#3-1-repayment-method) and based on loan information, information such as Total Payable Amount and Interest will be calculated.
5. Save and Submit.

![Loan Application](https://frappehr.com/files/loan-application99399a.png)

**3. Features**
---------------

### **3.1 Repayment Method**

There are two types of Repayment Methods in Loan Application:

#### **1. Repay Fixed Amount Per Period**

* Enter the Monthly Payment Amount.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Period in Months.
* Submit.

![Repayment Fixed Amount Per Period](https://frappehr.com/files/repayment-period-in-months.png)

#### **2. Repay Over Number Of Periods**

* Enter the Repayment Period in Months.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Monthly Repayment Amount.
* Submit.

![Repayment Fixed Amount Per Period](https://frappehr.com/files/repayment2.png)

**4. Related Topics**
---------------------

1. [Loan Type](https://docs.frappe.io/hr/loan-type)
2. [Loan](https://docs.frappe.io/hr/loan)

  

<!-- page: frappe-hr/hr__loan-type.md -->
---
title: "Loan Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan-type"
updated: "2026-02-04"
---

**Loans can be categorized into different types based on their specific characteristics.**

In Frappe HR, you can define different Loan Types, their Rate of Interest and other related information in the Loan Type doctype.

To access Loan Type go to:

> Human Resources > Loans > Loan Type

**1. How to create a Loan Type**
--------------------------------

1. Go to: Loan Type.
2. Enter the Loan Name.
3. Enter the Rate of Interest (%) Yearly.
4. Optionally, you can also enter the Maximum Loan Amount and Description of the Loan Type.
5. Save.

![Loan Type](https://frappehr.com/files/loan-type.png)

**2. Related Topics**
---------------------

1. [Loan Application](https://docs.frappe.io/hr/loan-application)
2. [Loan](https://docs.frappe.io/hr/loan)

  

<!-- page: frappe-hr/hr__loan.md -->
---
title: "Loan"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan"
updated: "2026-02-04"
---

**Once the Loan Application is approved by the manager, a Loan record and repayment schedule can be created for the Applicant using the Loan.**

To access Loan, go to:

> Human Resources > Loans > Loan

**1. Prerequisites**
--------------------

Before creating a Loan record, it is necessary that you create the following documents:

* [Loan Type](https://docs.frappe.io/hr/loan-type)
* [Loan Application](https://docs.frappe.io/hr/loan-application)
* [Chart of Accounts](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/chart-of-accounts)

**2. How to create a Loan record**
----------------------------------

1. Go to: Loan > New.
2. Select the Applicant name.
3. Select the Loan Application. Once selected, loan information such as Loan Type, Loan Amount, Rate of Interest, Repayment Method, Repayment Period in Months and Monthly Repayment Amount will be fetched.
4. Enter Repayment Start Date.

![Loan](https://frappehr.com/files/loan1.png)
5. Enter Account Information such as Mode of Payment, Payment Account, Loan Account and Interest Income Account.
6. Save. Once saved, a Repayment Schedule is automatically generated. The first repayment payment date would be set as per the "Repayment Start Date". The

![Repayment Schedule](https://frappehr.com/files/loan2.png)

> Note: Check "Repay from Salary" if the loan repayment will be deducted from the salary

You can alternatively create a Loan record directly from [Loan Application](https://docs.frappe.io/hr/loan-application)

**3. Features**
---------------

### **3.1 Creation of Disbursement Entry**

After submitting the Loan document, if the status is "Sanctioned", you can click on "Create Disbursement Entry" to create a Journal Entry of the Loan.

![Disbursement Entry](https://frappehr.com/files/disbursement-entry.png)  


### **3.2 Loan repayment deduction from Salary**

To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip.

![Salary Slip](https://frappehr.com/files/salary-slip-loan.png)  


### **3.3 Extending the Loan**

Loan amount is deducted from the salary. If the employee is on leave without pay for some period, the existing loan can be extended without the need for creating a new loan. This can be done be editing the Repayment Schedule table even after submitting the loan.

![Extending Loan](https://frappehr.com/files/change-loan-amount.gif)  


**4. Related Topics**
---------------------

1. [Journal Entry](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/journal-entry)
2. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__mobile-app-installation.md -->
---
title: "Mobile App Installation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/mobile-app-installation"
updated: "2026-02-04"
---

Frappe HR ships with a mobile frontend (progressive web app) v15 onwards. To install the app on your phones, go to https://<sitename>/hrms eg: if my site name is <https://frappeio.frappe.cloud>, the mobile app can be installed from <https://frappeio.frappe.cloud/hrms> 
Go to this URL on your mobile browser (Chrome/Safari) and install the app.
> Note: Firefox does not support PWA installation unless you have a plugin. 

## Android

1. On Android, you will get a prompt to install the app on this URL. 
2. If you do not see the prompt, tap on the hamburger menu (three dots), and tap on Install app from the list of options.
3. Tap on Install, and wait for a few seconds.
4. You will then be able to find the Frappe HR app in your applications. You can login to this app with your site credentials. 

![](https://gameplan.frappe.cloud/files/wqkysO0.jpg) 

### Installation GIF

<img src="/files/frappehr-android-pwa.gif" alt="frappehr-android-pwa-install" width="350"> 

## iOS

1. On iOS, if you're using Safari, tap on the share button shown in the image below. 
2. Scroll down the list of options, then tap Add to Home Screen. 
3. If you do not see "Add to Home Screen", click on "Edit Actions" and you should find the option. 
4. The icon will then appear on your home screen. You can login to this app with your site credentials. 

![](https://gameplan.frappe.cloud/files/bG9exfR.jpg) 

### Installation GIF

<img src="/files/frappehr-ios-pwa.gif" alt="frappehr-ios-pwa-install" width="350">

<!-- page: frappe-hr/hr__multicurrency-employee-advance-expense-claim.md -->
---
title: "Multi Currency Advance & Claim"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/multicurrency-employee-advance-expense-claim"
updated: "2026-04-03"
---

**Employees working internationally or handling expenses in foreign currencies may receive advances in currencies different from the company’s base currency. Frappe HR now supports Multi-Currency handling for both Employee Advance and Expense Claim to be recorded, paid, adjusted, and managed in any currency while maintaining accurate accounting and exchange rate impact.**

With this feature in v16, it now supports:

- Multi Currency Employee Advances
- Multi Currency Expense Claims
- Accurate exchange rate conversions
- Automatic exchange gain/loss entries
- Multiple Payment Entry against the same advance

## **1. Prerequisites**

1. Employee
2. Department
3. Chart of Accounts
4. Multi Currency Setup
5. Employee Advance
6. Expense Claim

**1.1 Create Expense Claim Type & Mode of Payment**

Before creating multicurrency records, make sure your **Expense Claim Types** and **Modes of Payment** are configured with accounts that use the correct currency.

For example, the standard **Expense Claim Type** (such as *Travel*) may be linked to an account in the company’s base currency. So such a type won’t accept a claim in a different currency. In these cases, create a separate expense type (e.g., *Travel — USD*) and link it to an account that uses the same transaction currency

![](/files/Expense Claim Type.png)
*Expense Claim Type*



Similarly, if you are paying via Bank or Cash in a foreign currency, the Mode of Payment must link to a corresponding currency account. This ensures that expense claims and advances in currencies other than the company’s base currency are captured and processed correctly.

![](/files/Mode of Payment.png)
*Mode of Payment*

## **2. Multi-Currency in Employee Advance**

Before creating an Employee Advance, ensure that the **Employee Salary Currency** is correctly set in the Employee master.  

A new field **Employee Advance Account** is added in the Employee master. This account should match the employee’s salary currency.  

> **Note:** If these fields are not set, Employee Advance allows manual selection. Make sure the advance account exists with the correct currency before creating an advance.

**2.1 How to Create a Multi-Currency Employee Advance**

1. Go to: **Employee Advance > New**
2. Select the **Employee**
3. Choose the **Currency** if not fetched automatically and enter the **Advance Amount**
4. Under the Accounting section:
  - **Advance Account** is fetched from **Employee Advance Account** in the Employee master; if not fetched, select manually  
  - Select **Mode of Payment** if applicable
5. Save the document

![emp-advance](/files/MultiCurrencyEmployeeAdvance.png)

## **3. Payment of Multi-Currency Advances**

Payment for a submitted Employee Advance can be made via **Payment Entry**.  

> **Note**

- At the time of payment, the current exchange rate will be fetched. This rate is used to calculate the base currency amounts and determine exchange gain/loss during Expense Claim.  
- The original exchange rate on the Employee Advance is no longer used; the payment exchange rate is used for all further calculations.

**3.1 Multiple Payment Entries**

If the same advance has multiple payments:  

- Each payment is tracked separately  
- Multi-currency payments with different exchange rates are supported  
- Correct amounts are reflected in Expense Claim

## **4.Multi Currency Expense Claim**

1. From **Employee Advance → Make Expense Claim**

- The advance currency will be fetched in the Expense Claim.  
- All linked advances will appear in the **Advances Table**.  
- Exchange rate at the time of payment will also be fetched in Advances Table. 
- Base currency values are auto-calculated based on the exchange rate at the time of claim.  
- If the same advance has multiple payments, each payment will appear as a separate row in Advances Table with the corresponding **Payment Entry** reference. This helps in reconciling partially claimed advances.

![multi-payments](/files/multi-payments.jpeg)

Once the Expense Claim is Submitted, the claim amount is allocated from the Advance table

![advance-claimed](/files/advance-claimed.jpeg)

## **5. Exchange Gain/Loss Handling**

- If the exchange rate at the time of Expense Claim differs from the exchange rate at the time of advance payment:  
  - Exchange gain/loss is calculated for each advance row  
  - Total gain/loss is posted via **Journal Entry**, ensuring accurate accounting

![gain_loss](/files/gain_loss.jpeg)

![gain_loss-booked](/files/gain_loss-booked.jpeg)

**References:**  

- Employee Advance
- Expense Claim
