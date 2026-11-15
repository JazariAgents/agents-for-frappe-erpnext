<!-- Frappe documentation: frappe-hr, part 7 of 10. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Leave Period]  


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

[Screenshot on the live page: Leave Policy Assignment]  


On submission, Leave Allocation documents would be created automatically based on the [Leave Policy](https://docs.frappe.io/hr/leave-policy) as shown below.

[Screenshot on the live page: Leave Allocations]  


**3. Features**
---------------

### **3.1 Bulk Leave Policy Assignment**

Frappe HR also allows creating Leave Policy Assignments for multiple employees at once.

1. Go to the Leave Policy Assignment list.
2. Click on Bulk Leave Policy Assignment.
3. This will take you to the [Leave Control Panel](https://docs.frappe.io/hr/leave-control-panel), where you can assign Leave Policies in bulk.

[Screenshot on the live page]  


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

[Screenshot on the live page: Leave Policy]

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

[Screenshot on the live page]

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

[Screenshot on the live page]


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

[Screenshot on the live page]  


**Non-Encashable Leaves:** This field indicates the number of leave days the Employees won't be able to encash. Above the mentioned days, the Employee is eligible to encash leaves.

For example, if there are 10 leaves of a particular Leave Type which is encashable, and the Employee has 8 leaves left. If Non-Encashable Leaves = 5, the Employee is given encashment of only 8 - 5 = 3 leaves.

**Earning Component:** This field allows you to specify the Salary Component that will be encashed to Employees as a part of their Salary in the Salary Slip.


> **Note: On submitting a** [**Leave Encashment**](https://docs.frappe.io/hr/leave-encashment) **for an Employee, Frappe HR automatically creates an** [**Additional Salary**](https://docs.frappe.io/hr/additional-salary) **which will get added to the Salary Slip of the Employee when processing the next payroll.**
> 
> 

### **2.2 Earned Leave**

Earned Leaves are leaves earned by an Employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro-rata basis by automatically updating Leave Allocation for leaves of this type at intervals set by 'Earned Leave Frequency'.

For example, an Employee is allotted 24 Privilege Leaves in a year, wherein the Privilege Leave is set as Earned Leave with Monthly allotment. In this case, the Employee will earn 2 (24 leaves/12 months) Privilege Leaves at the end of every month. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type and will round to 'Rounding' for fractions.

[Screenshot on the live page]  



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

[Screenshot on the live page: Loan Application]

**3. Features**
---------------

### **3.1 Repayment Method**

There are two types of Repayment Methods in Loan Application:

#### **1. Repay Fixed Amount Per Period**

* Enter the Monthly Payment Amount.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Period in Months.
* Submit.

[Screenshot on the live page: Repayment Fixed Amount Per Period]

#### **2. Repay Over Number Of Periods**

* Enter the Repayment Period in Months.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Monthly Repayment Amount.
* Submit.

[Screenshot on the live page: Repayment Fixed Amount Per Period]

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

[Screenshot on the live page: Loan Type]

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

[Screenshot on the live page: Loan]
5. Enter Account Information such as Mode of Payment, Payment Account, Loan Account and Interest Income Account.
6. Save. Once saved, a Repayment Schedule is automatically generated. The first repayment payment date would be set as per the "Repayment Start Date". The

[Screenshot on the live page: Repayment Schedule]

> Note: Check "Repay from Salary" if the loan repayment will be deducted from the salary

You can alternatively create a Loan record directly from [Loan Application](https://docs.frappe.io/hr/loan-application)

**3. Features**
---------------

### **3.1 Creation of Disbursement Entry**

After submitting the Loan document, if the status is "Sanctioned", you can click on "Create Disbursement Entry" to create a Journal Entry of the Loan.

[Screenshot on the live page: Disbursement Entry]  


### **3.2 Loan repayment deduction from Salary**

To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip.

[Screenshot on the live page: Salary Slip]  


### **3.3 Extending the Loan**

Loan amount is deducted from the salary. If the employee is on leave without pay for some period, the existing loan can be extended without the need for creating a new loan. This can be done be editing the Repayment Schedule table even after submitting the loan.

[Screenshot on the live page: Extending Loan]  


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

[Screenshot on the live page] 

### Installation GIF

[Screenshot on the live page] 

## iOS

1. On iOS, if you're using Safari, tap on the share button shown in the image below. 
2. Scroll down the list of options, then tap Add to Home Screen. 
3. If you do not see "Add to Home Screen", click on "Edit Actions" and you should find the option. 
4. The icon will then appear on your home screen. You can login to this app with your site credentials. 

[Screenshot on the live page] 

### Installation GIF

[Screenshot on the live page]

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

[Screenshot on the live page]
*Expense Claim Type*



Similarly, if you are paying via Bank or Cash in a foreign currency, the Mode of Payment must link to a corresponding currency account. This ensures that expense claims and advances in currencies other than the company’s base currency are captured and processed correctly.

[Screenshot on the live page]
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

[Screenshot on the live page: emp-advance]

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

[Screenshot on the live page: multi-payments]

Once the Expense Claim is Submitted, the claim amount is allocated from the Advance table

[Screenshot on the live page: advance-claimed]

## **5. Exchange Gain/Loss Handling**

- If the exchange rate at the time of Expense Claim differs from the exchange rate at the time of advance payment:  
  - Exchange gain/loss is calculated for each advance row  
  - Total gain/loss is posted via **Journal Entry**, ensuring accurate accounting

[Screenshot on the live page: gain_loss]

[Screenshot on the live page: gain_loss-booked]

**References:**  

- Employee Advance
- Expense Claim

<!-- page: frappe-hr/hr__organizational-chart.md -->
---
title: "Organizational Chart"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/organizational-chart"
updated: "2026-02-04"
---

**An organizational chart shows the organizational structure by depicting connections between different employees with their designation, image, and name. In large organizations where it's difficult to remember names, people can interact with the org chart and know the hierarchy through faces and other info.**

To access Employee Grade, go to:

> Home > Human Resources > Employee > Organizational Chart

* The org chart is created based on the "Reports To" field in Employee master.
* The employees that don't report to anyone are shown in the first level.
* The chart expands horizontally on the desktop view and vertically on mobile.
* Each node has details like the Employee Name, Image, Designation, and the total number of connections.
* The connections are the total number of descendants a particular node has till the end of the hierarchy.
* The edit button in every node navigates to the Employee Master.
* As you navigate through the chart, the active hierarchy is highlighted.
* You can use the Company filter to check the org chart for individual companies.

[Screenshot on the live page: Org Chart]  


[Screenshot on the live page: Org Chart Mobile]  


  

<!-- page: frappe-hr/hr__overtime.md -->
---
title: "Overtime"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/overtime"
updated: "2026-02-04"
---

Overtime allows employees to be compensated or granted compensatory leave for working beyond their standard working hours. Overtime is calculated based on employee check-in and check-out times and processed through Attendance and Overtime Slip records

### Create an Overtime Type

Navigate to the **Overtime Type** doctype to configure how overtime is handled:

- **Maximum Overtime Hours Allowed Per Day**: If set, overtime exceeding this limit won’t be considered for payment.
- **Overtime Salary Component**: The salary component through which overtime earnings are paid.
- **Overtime Amount Calculation**:
  - **Fixed Hourly Rate**: A predefined per-hour rate multiplied by total overtime hours.
  - **Salary Component-Based**: Select applicable salary components. The total amount is divided by the salary cycle's payment days and standard working hours to determine the hourly rate.
- **Pay Rate Multipliers**:
  - **Standard Multiplier**: The hourly rate is multiplied by this value.
  - **Holiday/Weekend Multipliers**: If enabled, separate multipliers can be set for public holidays and weekends; otherwise, the standard multiplier applies.
 
[Screenshot on the live page]


### To allow overtime for a specific **Shift Type**:

1. Navigate to the **Shift Type** doctype.
2. Enable **Allow Overtime**.
3. Set the applicable **Overtime Type**.
4. Assign the shift to employee(s).

[Screenshot on the live page]

### Record Employee Check-ins & Mark Attendance

- Employees' **check-in and check-out times** must be recorded.
- **Attendance must be processed** for the shift type as overtime details are fetched based on this.


### Generate & Approve Overtime Slip

1. Create an **Overtime Slip** and select the **employee** and **date range**.
2. Click **Fetch Overtime Details** to populate the **Overtime Details** table based on attendance records.
3. **HR can approve or reject** the overtime slip.
4. Upon approval, an **Additional Salary** record is created, ensuring payment is included in the salary cycle corresponding to the slip’s **from date**.

[Screenshot on the live page]

<!-- page: frappe-hr/hr__payroll-articles__make-bank-entry-from-payroll-entry.md -->
---
title: "Make Bank Entry from Payroll Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-articles/make-bank-entry-from-payroll-entry"
updated: "2026-07-02"
---

After payroll is processed, companies usually need to record the actual salary payment made from the bank account. In Frappe HR, this can be done from the Payroll Entry by creating a Bank Entry.

A Bank Entry records the movement of money from the company's bank account to settle the payroll liability created during payroll processing.

## When to use this

Use Make Bank Entry when:

- Payroll Entry has been created for a payroll period.
- Salary Slips have been created and submitted.
- Payroll accounting entries have been posted.
- The company is ready to record payment of salaries through a bank account.

## Before you begin

Make sure the following setup is complete:

- Employees have valid salary structures and salary slips.
- Payroll Entry has been processed for the correct payroll period.
- Salary Slips are submitted.
- Payroll accounting has been posted.
- The company has a bank account configured in ERPNext.
- The payable account and bank account used for payroll are correct.

## How it works

When payroll is processed, ERPNext/Frappe HR records the salary expense and the amount payable to employees. The Bank Entry is then used to record the payment of that payable amount from the bank.

Simple flow:

```
Create Payroll Entry
        |
        v
Create Salary Slips
        |
        v
Submit Salary Slips
        |
        v
Post Payroll Accounting Entry
        |
        v
Make Bank Entry
        |
        v
Submit Bank Entry
        |
        v
Salary Payable is settled
```

## Steps to make a Bank Entry

1. Open the submitted Payroll Entry.
2. Check that the Salary Slips are created and submitted.
3. Check that the payroll accounting entry has been created.
4. Click Make Bank Entry from the Payroll Entry actions.
5. Review the generated Bank Entry.
6. Confirm the bank account, payable account, posting date, and amount.
7. Save and submit the Bank Entry.

Once submitted, the Bank Entry records the salary payment and reduces the outstanding payroll payable balance.

## What the Bank Entry represents

The Bank Entry usually records two sides of the transaction:

- Debit: Payroll payable or salary payable account
- Credit: Bank account from which salaries are paid

This means the liability created during payroll processing is reduced, and the bank balance is reduced by the salary payment amount.

## Things to check before submitting

Before submitting the Bank Entry, verify:

- The posting date matches the salary payment date.
- The bank account is correct.
- The payable account is correct.
- The amount matches the salary amount to be paid.
- The company and cost center details are correct, if applicable.

## Common mistakes

### Salary Slips are not submitted

The Bank Entry should be made only after salary slips are submitted and payroll accounting is posted.

### Wrong bank account selected

If the wrong bank account is selected, the accounting impact will be incorrect. Always review the bank account before submission.

### Payroll accounting not posted

If the salary payable entry has not been created, the Bank Entry may not correctly settle the payroll liability.

## Summary

Make Bank Entry from Payroll Entry is used to record salary payment after payroll has been processed. It connects payroll processing with accounting by settling the salary payable amount against the company's bank account.

<!-- page: frappe-hr/hr__payroll-correction.md -->
---
title: "Payroll Correction"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-correction"
updated: "2026-02-04"
---

The feature ensures accurate payroll calculations by allowing users to reverse a portion of LWP days, automatically recalculating earnings and deductions based on the reversal.

How to Use

Step 1: Navigate to Payroll Correction
1.	Go to HR > Payroll > Payroll Correction.
2.	Click New to create a new Payroll Correction entry.
Step 2: Select Employee and Payroll Period

- Choose the Employee whose LWP needs correction.
- Select the Payroll Period.
- The system will fetch available Salary Slips with LWP and absent days applied.

Step 3: Select the Month for LWP Reversal

- In the "Select Month for LWP Reversal" field, choose the month from the dropdown.
- Once that is done system fetches:
  - Salary Slip Reference
  - Absent Days
  - LWP Days
  - Total Working Days
  - Total LWP Applied

Step 4: Enter the number of days to reverse in the Days to Reverse field.

Step 5: Save

- Upon save arrear details will be populated for Earnings, Deductions and Accrued Benefits

Step 5: Submit the Payroll Correction

- •	Once validated, submit the document.
- •	The system will:
  - Create Additional Salary Entries against earnings and deductions for the reversed amount.
  - Record accruals in Employee Benefit Ledger

<!-- page: frappe-hr/hr__payroll-entry.md -->
---
title: "Payroll Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-entry"
updated: "2026-02-04"
---

**Payroll is the sum total of all compensation a business must pay to its employees for a set period of time or on a given date.**

In Frappe HR, Payroll Entry enables bulk processing of payroll for employees. In other words, processing salary slips of all employees in one go. The bulk processing can be Company-wide or based on these categories: Branch, Department, or Designation.

To access Payroll Entry, go to:


> **Home > Human Resources > Payroll > Payroll Entry**
> 
> 

**1. How to create a Payroll Entry**
------------------------------------

1. Go to to Payroll Entry list, click on New.
2. Select the Payroll Frequency.
3. Select Branch, Designation and Department to filter out employees (optional).
4. Select Project (optional) if you want to run the payroll against a project.
5. Select 'Validate Attendance' and 'Salary Slip Based on Timesheet' checkboxes in case you want to deduct the salary based on attendance and if you want to also consider the timesheets of the employees respectively.
6. Select the Payment Account to make the Bank Entry.
7. Save.

Once the information is saved, click on the **Get Employees** button to get a list of Employees for which the Salary Slips will be created based on the selected criteria.

Once the list of Employees is fetched, click on the **Create Salary Slips** button to generate Salary Slips.

[Screenshot on the live page: Payroll Entry]  



> **Note: If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.**
> 
> 

**2. Features**
---------------

### **2.1 Salary Accrual**

After verifying the Salary Slips, you can Submit them all together by clicking on the **Submit Salary Slip** button.

[Screenshot on the live page: Payroll Entry]  


This will also book the default Payroll Payable account against respective Expense Heads (as configured in Salary Components) to record the accrual of salary to employees.

**Cost Center:**

You can select Cost Center in the Payroll Entry against which the expenses will be posted.

If you want to book expenses against multiple cost centers based on Employee/Department, you can do so by setting Payroll Cost Center in the Employee/Department master.

[Screenshot on the live page]  


Even multiple cost centers can be assigned against a single Employee. You can do so via the Salary Structure Assignment document.

[Screenshot on the live page]  


Cost Center assigned in Salary Structure Assignment gets the highest priority and then Employee and Department master respectively. The least priority is given to the Cost Center selected in Payroll Entry.

[Screenshot on the live page: Payroll Entry]  



> **Note: Submitting Salary Slips one by one manually will not create the Journal Entry to record salary accrual.**
> 
> 

### **2.2 Salary Payment**

The final step is to book the Salary Payment.

Salaries in businesses are usually dealt with extreme privacy. In most cases, companies issue a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account.

This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the Earnings type salary component and credits the total of Deductions type salary component of all Employees to the default account set at the Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on the **Make Bank Entry** button.

Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You will have to set the reference number and date for the transactions and Submit the Journal Entry.

[Screenshot on the live page: Payroll Entry]  



> **Note: For Salary Components which are Flexible Benefits and has *Create Separate Payment Entry Against Benefit Claim* checked, Frappe HR will book separate draft Journal Entries.**
> 
> 

**3. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
4. [Journal Entry](https://docs.erpnext.com/docs/user/manual/en/journal-entry)

  

<!-- page: frappe-hr/hr__payroll-management.md -->
---
title: "Payroll Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-management"
updated: "2026-02-04"
---

Payroll processing is an important function of every enterprise HR. Frappe HR greatly simplifies this process by offering an array of features that you can utilize from Salary Structure management to bulk processing Payroll of employees. Read the following documentation to understand how to configure and use Frappe HR Human Resources to super power your Payroll processing.

**Related Topics**
------------------

1. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
2. [Salary Component](https://docs.frappe.io/hr/salary-component)
3. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
4. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
6. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
7. [Retention Bonus](https://docs.frappe.io/hr/retention-bonus)
8. [Employee Incentive](https://docs.frappe.io/hr/employee-incentive)

  

<!-- page: frappe-hr/hr__payroll-period.md -->
---
title: "Payroll Period"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-period"
updated: "2026-02-04"
---

**A Payroll Period is a period for which Employees get paid for their occupation with the Company.**

Payroll Period helps you define Salary Structures and to calculate tax for a specific period based on applicable Income Tax Slab.

To access Payroll Period, go to:


> **Home > Human Resources > Payroll > Payroll Period**
> 
> 

**1. How to create a Payroll Period**
-------------------------------------

1. Go to Payroll Period list, click on New.
2. Enter Name.
3. Select Start Date and End Date of Payroll Period.
4. Save.

**2. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab)
4. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
5. [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)
6. [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration)

  
