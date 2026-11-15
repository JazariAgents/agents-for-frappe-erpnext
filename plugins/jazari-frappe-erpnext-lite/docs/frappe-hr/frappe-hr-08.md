<!-- Frappe documentation: frappe-hr, part 8 of 10. Index: docs/INDEX.md -->

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

![Org Chart](https://frappehr.com/files/org-chart.png)  


![Org Chart Mobile](https://frappehr.com/files/org-chart-mobile-2.png)  


  

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
 
![](/files/Screenshot%202025-03-25%20at%204.27.08%E2%80%AFPM.png)


### To allow overtime for a specific **Shift Type**:

1. Navigate to the **Shift Type** doctype.
2. Enable **Allow Overtime**.
3. Set the applicable **Overtime Type**.
4. Assign the shift to employee(s).

![](/files/Screenshot%202025-03-25%20at%204.38.16%E2%80%AFPM.png)

### Record Employee Check-ins & Mark Attendance

- Employees' **check-in and check-out times** must be recorded.
- **Attendance must be processed** for the shift type as overtime details are fetched based on this.


### Generate & Approve Overtime Slip

1. Create an **Overtime Slip** and select the **employee** and **date range**.
2. Click **Fetch Overtime Details** to populate the **Overtime Details** table based on attendance records.
3. **HR can approve or reject** the overtime slip.
4. Upon approval, an **Additional Salary** record is created, ensuring payment is included in the salary cycle corresponding to the slip’s **from date**.

![](/files/Screenshot%202025-03-25%20at%204.40.52%E2%80%AFPM.png)

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

![Payroll Entry](https://frappehr.com/files/payroll-entry-get-employees.png)  



> **Note: If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.**
> 
> 

**2. Features**
---------------

### **2.1 Salary Accrual**

After verifying the Salary Slips, you can Submit them all together by clicking on the **Submit Salary Slip** button.

![Payroll Entry](https://frappehr.com/files/payroll-entry.png)  


This will also book the default Payroll Payable account against respective Expense Heads (as configured in Salary Components) to record the accrual of salary to employees.

**Cost Center:**

You can select Cost Center in the Payroll Entry against which the expenses will be posted.

If you want to book expenses against multiple cost centers based on Employee/Department, you can do so by setting Payroll Cost Center in the Employee/Department master.

![](https://frappehr.com/files/ViFAtRT.png)  


Even multiple cost centers can be assigned against a single Employee. You can do so via the Salary Structure Assignment document.

![](https://frappehr.com/files/hUnTWPJ.png)  


Cost Center assigned in Salary Structure Assignment gets the highest priority and then Employee and Department master respectively. The least priority is given to the Cost Center selected in Payroll Entry.

![Payroll Entry](https://frappehr.com/files/payroll-make-accrual-entry.png)  



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

![Payroll Entry](https://frappehr.com/files/payroll-make-bank-entry.png)  



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

  

<!-- page: frappe-hr/hr__payroll-settings.md -->
---
title: "Payroll Settings"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-settings"
updated: "2026-02-04"
---

**Payroll Settings allow you to configure global settings for the Payroll module.**

To access Payroll Settings, go to: > Home > Payroll > Settings > Payroll Settings

**1. Working Days & Hours**
---------------------------

![](https://frappehr.com/files/0jpZNkE.png)  


#### **1.1 Calculate Payroll Working Days Based On**

Working Days in Salary Slip can be calculated based on Leave Application or Attendance records.

#### **1.2 Consider Unmarked Attendance As**

If you set payroll based on Attendance, this option will be shown. It allows you to control the status of unmarked attendance. Eg: If you set it as Present, you don't need to explicitly mark attendance for every employee throughout the month. Just mark the absent days and the rest would be considered as Present by default.

#### **1.3 Include holidays in Total no. of Working Days**

If checked, the total number of working days will include holidays, and this will reduce the value of salary per day. Eg: If there are 10 holidays in a 30-day month, the Total Working Days will be considered as 30 if this checkbox is enabled and 20 if disabled. Then attendance will be checked for these 30/20 days to find out the payment days.

#### **1.4 Consider Marked Attendance on Holidays**

By default, holidays are considered as paid days. If this is enabled and you mark attendance on a holiday, the marked attendance will override holiday status on that day. Eg: if you mark an employee as Absent on a holiday, it will be counted as an absent day and not a paid one.

#### **1.5 Max working hours against Timesheet**

For salary slips based on the timesheet, you can set the maximum allowed hours against a single timesheet. Set this value to zero to disable this validation.

#### **1.6 Fraction of Daily Salary for Half Day**

Based on this fraction, the salary for Half Day will be calculated. For example, if the value is set as 0.75, then the three-fourth salary will be given for half-day attendance.

**2. Salary Slip**
------------------

![](https://frappehr.com/files/8i1mB1S.png)  


#### **2.1 Disable Rounded Total**

If enabled, hides and disables Rounded Total field in Salary Slips

#### **2.2 Show Leave Balances in Salary Slip**

**3. Email**
------------

![](https://frappehr.com/files/g2R6b5Z.png)  


#### **3.1 Email Salary Slip to Employee**

An email with the salary slip is sent to the respective employee's preferred email address on submission of the salary slip.

#### **3.2 Encrypt Salary Slips in Emails**

The salary slip PDF sent to the employee is encrypted using the mentioned Password Policy.

#### **3.3 Password Policy**

This field becomes visible and mandatory on checking the above option for encrypting the salary slip in email.

Here is an example of how to set a Password Policy for the salary slip PDF.

**Example:**


```
SAL-{first_name}-{date_of_birth.year}
```
This will generate a password like SAL-Jane-1972

**4. Other Settings**
---------------------

![](https://frappehr.com/files/gMl5WRl.png)  


#### **4.1 Define Opening Balance for Earning and Deduction**

If enabled, it will allow you to set up opening entries for **Taxable Earnings till Date** and **Tax Deducted till Date** in the Salary Structure Assignment if there are no existing salary slips for the employee.**![](https://frappehr.com/files/bYBjuyW.png)**  


#### **4.2 Process Payroll Accounting Entry based on Employee**

By default, a consolidated Journal Entry is created against the Payroll Entry for all the employees. If you want a better breakup of payroll amounts per employee, enable this to process employee-wise accounting entries.

![](https://frappehr.com/files/B9OY6ym.png)  


  

<!-- page: frappe-hr/hr__payroll-setup.md -->
---
title: "Payroll Setup"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-setup"
updated: "2026-02-04"
---

Salary is a fixed amount of money or compensation paid to an employee by an employer in return for the work performed.

Payroll is the administration of financial records of employees' salaries, wages, bonuses, net pay, and deductions.

To process Payroll in Frappe HR,

1. Define [Payroll Period](https://docs.frappe.io/hr/payroll-period.html) (optional)
2. Define [Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab.html) (optional)
3. Create Salary Structure with Salary Components (Earnings and Deductions)
4. Assign Salary Structures to each Employee via Salary Structure Assignment
5. Generate Salary Slips via [Payroll Entry](https://docs.frappe.io/hr/payroll-entry.html).
6. Book the Salary in your Accounts.

**Payroll Period**
------------------

[Payroll Period](https://docs.frappe.io/hr/payroll-period.html), in Frappe HR, is a period for which Employees get paid for their occupation with the Company. Payroll period helps you define Tax slabs applicable for the period, making it easier to manage changing laws.

> Note: Configuring Payroll Period is optional if you do not intend to use Flexible Benefits or Tax Slabs

**Salary Component**
--------------------

This document allows you to define each Earning and Deduction component which can be used to create a Salary Structure and subsequently create Salary Slip or Additional Salary. You can also configure the type, condition and formula as well as other settings which are discussed below. You should be able to enable various combinations of the following options to configure each component as it fits your Company / Regional policies.

* Depends on Leave Without Pay: Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves or takes a leave without an approval (via Leave Application). If enabled, Frappe HR will automatically deduct the pay in proportion of LWP days divided by the total working days for the month (based on the Holiday List).

> Note: If you don’t want Frappe HR to manage LWP, don’t turn on this flag in any of the Salary Components
* Do not include in total: If this option is enabled, the component wont be added to the total of the Earnings or Deductions of the Salary Slip

#### **Earning**

![Salary Component Earnings](https://frappehr.com/files/salary-component.png)  


* Is Additional Component: This option specify that the component can only be paid as Additional Salary. Examples of this component could be Performance Bonus or pay received for on-site deputation etc. Such components are not considered to be part of normal Salary Structure. Instead, Additional Salary with these components can be submitted as required which will be added to the Salary Slip automatically.
* Is Tax Applicable: If a component needs to be considered for Tax calculations specified as per the Payroll Period you may want to enable this option. It would be required that you have a Payroll Period and Income Tax Slab configured with valid Tax Slabs for payroll processing.
* Is Payable: Such components can be booked against separate payable accounts and the Accounts shall be configured in the Accounts table
* Flexible Benefits: Flexible Benefits are earning components which Employees can choose to receive on a pro-rata basis or annually when they claim for. These are mostly tax exempted, unless the Employee fail to file the claim with adequate bills / documents. If turned on, you can specify the maximum benefit allowed for an employee in a year. Employees can create [Employee Benefit Application](https://docs.frappe.io/hr/employee-benefit-application) with the ones they opt for.

>Note: Employee Benefit Application will only allow Employees to only choose from the flexible components which are present in the Salary Structure assigned to the Employee


	+ Pay Against Benefit Claim: Employees can opt to receive flexible benefits annually via Employee Benefit Claim or along with their salary every month. If you enable this, the amount allocated for the component will be paid as the Employee submits an [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim.html). Else the amount will be dispersed as part of the Employee's salary on a pro-rata basis.
	
	
		- Only Tax Impact (Cannot Claim But Part of Taxable Income): Such components are those which the company has already paid to the Employee in cash or by some other means, for example a car purchased for the Employee's use. The Employee cannot claim but is liable to pay tax. The amount allocated for this component will be considered while calculating the taxable income of the Employee.
		- Create Separate Payment Entry Against Benefit Claim: Some of the flexible benefits may be legally required to be paid via separate vouchers. If you enable this, while posting the bank entry the amount paid for such components will be posted as a separate entry for each Employee.![Flexible Salary Component](https://frappehr.com/files/salary-component-1.png)  
	
	
	> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before that last payroll, use "Deduct Tax For Unclaimed Employee Benefits" in Payroll Entry / Salary Slip while processing the Salary.

#### **Deduction**

![Salary Component Deduction](https://frappehr.com/files/salary-component-2.png)  


* Variable Based On Taxable Salary: If you enable this, the component will be considered as the standard Tax deduction component. Tax will be calculated based on the Income Tax Slab linked to the employee.

**Salary Structure**
--------------------

Salary Structure represents how Salaries are structured and calculated based on Earnings and Deductions. Salary structures are used to help organizations:

1. Maintain pay levels that are competitive with the external labor market,
2. Maintain internal pay relationships among jobs,
3. Recognize and reward differences in the level of responsibility, skill, and performance, and manage pay expenditures.

Usual components of a salary structure (in India) include:

* Basic Salary: It is the taxable base income and generally not more than 40% of CTC.
* House Rent Allowance: The HRA constitutes 40 to 50% of the basic salary.
* Special Allowances: Makes up for the remainder part of the salary, mostly smaller than the basic salary which is completely taxable.
* Leave Travel Allowance: The non-taxable amount paid by the employer to the employee for vacation/trips with family within India.
* Gratuity: It is basically a lump sum amount paid by the employer when the employee resigns from the organization or retires.
* PF: Fund collected during emergency or old age. 12% of the basic salary is automatically deducted and goes to the employee provident fund.
* Medical Allowance: The employer pays the employee for the medical expenditures incurred. It is tax-free up to Rs.15,000.
* Bonus: Taxable part of the CTC, usually a once a year lump sum amount, given to the employee based on the individual’s as well as the organizational performance for the year.
* Employee Stock Options: ESOPS are Free/discounted shares given by the company to the employees. This is done to primarily increase employee retention.

![Submitted Salary Structure](https://frappehr.com/files/salary-structure.png) A submitted Salary Structure

### **Creating a New Salary Structure**

To create a new Salary Structure go to:

> Human Resources > Payroll Setup > Salary Structure > New Salary Structure

In the new Salary Structure,

1. Name the salary Structure and set the company, letterhead for Salary Slip printing and frequency of payroll etc.
2. Set the starting date from which this is valid (Note: There can only be one Salary Structure that can be “Active” for an Employee during any period).
3. Configure Leave Encashment Amount per Day which will be the amount payable to Employees on Leave Encashment requests.
4. Max Benefits amount is the maximum amount eligible as Flexible Components to employees.

#### **Salary Slip Based on Timesheet**

Salary Slip based on Timesheet is applicable if you have timesheet based payroll system

1. Check "Salary Slip Based on Timesheet"
2. Select the salary component and enter Hour Rate (Note: This salary component gets added to earnings in Salary Slip)

![Salary Slip based on Timesheet](https://frappehr.com/files/salary-timesheet.png)  


#### **Earnings and Deductions in Salary Structure**

In the “Earnings” and “Deductions” tables, you can select the earnings and deductions components The condition and formula configured in Salary Component will be copied by default, but you may change this if required. You may also want to select the Base component in the Earnings table. Note that the amount eligible for each employee should be configured in Salary Structure Assignment.

If the condition and formula for any of the earnings or deductions are not configured in Salary Component, you can calculate the values of Salary Components based on,

#### **Condition and Formula**

![Condition and Formula](https://frappehr.com/files/condition-formula.png)  


#### **Condition and Amount**

![Condition and Amount](https://frappehr.com/files/condition-amount.png)  


In conditions and formulas,

* Use field "base" for using base salary of the Employee
* Use Salary Component abbreviations. For example: BS for Basic Salary
* Use field name for employee details. For example: Employment Type for employment_type

#### **Account Details**

![Salary Structure Account](https://frappehr.com/files/salary-structure-account.png)  


* Select Mode of Payment and Payment Account for the Salary Slips which will be generated using this Salary Structure

Finally, *Save* the Salary Structure.

### **Leave Without Pay (LWP)**

Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves or takes a leave without an approval (via Leave Application). If you want Frappe HR to automatically deduct salary in case of LWP, then you must check on the “Apply LWP” column in the Earning Type and Deduction Type masters. The amount of pay cut is the proportion of LWP days divided by the total working days for the month (based on the Holiday List).

If you don’t want Frappe HR to manage LWP, leave the LWP unchecked in all of the Earning Types and Deduction Types.

**Salary Structure Assignment**
-------------------------------

Salary Structure Assignment allows you to assign salary structure and specify the base pay eligible for each employee. It is important that you set the base salary for each assignment as this will be the base salary used for calculations as per the Salary Structure.

To create a new Salary Structure Assignment go to:

> Human Resources > Payroll > Salary Structure Assignment > New Salary Structure Assignment

![Salary Structure Assignment](https://frappehr.com/files/salary-structure-assignment.png)  




---

**Processing Payroll**
======================

You can either bulk process payroll for Employees under a department, branch or designation or process payroll individually by creating Salary Slips for each employee.

**Payroll Processing Using Payroll Entry**
------------------------------------------

You can also create salary slip for multiple employees using Payroll Entry:

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

#### **Payroll Entry**

![Payroll Entry](https://frappehr.com/files/payroll-entry.png)  


In Payroll Entry,

1. Select the Company for which you want to create the Salary Slips. You can also select the other fields like Branch, Department, Designation or Project to be more specific.
2. Check *Salary Slip based on Timesheet* if you want to process timesheet based Salary Slips.
3. Select the Posting Date and the frequency of payroll which you want to create the Salary Slips.
4. Click on "Get Employee Details" to get a list of Employees for which the Salary Slips will be created based on the selected criteria.
5. Enter the Start and End dates for the payroll period.
6. You can check *Deduct Tax For Unclaimed Employee Benefits* if you want to deduct taxes for all benefits (Salary Components which are *Is Flexible Benefit*) paid to employees till the current payroll
7. Similarly, *Deduct Tax For Unsubmitted Tax Exemption Proof* allows you to deduct taxes for the earnings which were exempted in the previous payrolls as declared in [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration) but the Employee has not submitted sufficient proof [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)
8. Select the Cost Center and Payment Account.
9. Save the form and Submit it to create Salary Slip records for each active Employee for the time period selected. If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.

![Submitted Payroll Entry](https://frappehr.com/files/created-payroll.png)  


Once all Salary Slips are created, you can use *View Salary Slips* to verify if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).

After checking, you can "Submit" them all together by clicking on "Submit Salary Slip".

>Note: Submitting Salary Slips will also book the default Payroll Payable account to record the accrual of salary.

#### **Booking Salaries in Accounts**

The final step is to book the Salaries in your Accounts.

Salaries in businesses are usually dealt with extreme privacy. In most cases, the companies issues a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account. This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the earning type salary component and credits the total of deduction type salary component of all Employees to the default account set at Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on - > Make > Bank Entry

![Payroll Make Entry](https://frappehr.com/files/payroll-make-bank-entry.png)  


Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You shall set reference number and date for the transactions and Submit the Journal Entries.

>Note: For Salary Components which are Flexible Benefits and has *Create Separate Payment Entry Against Benefit Claim* checked, Frappe HR will book separate draft Journal Entries.

![Payroll Entry](https://frappehr.com/files/payroll-journal-entry.png)  


**Creating Salary Slips Manually**
----------------------------------

Once the Salary Structure is created and assigned to employees via Salary Structure Assignment, you can make a Salary Slip individually. Go to:

> Human Resources > Payroll > Salary Slip > New Salary Slip

#### **Salary Slip**

![Salary Slip](https://frappehr.com/files/salary-slip.png)  


  

<!-- page: frappe-hr/hr__project-profitability-report.md -->
---
title: "Project Profitability Report\n"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/project-profitability-report"
updated: "2026-02-16"
---


The Project Profitability Report shows the Profitability and Utilization of each employee based on the Timesheets generated.

To view this report, you can go to:

> Home > Projects > Reports > Project Profitability

This report shows the Project Profitability with the following data:

- Timesheet
- Salary Slip generated using the Timesheet
- Sales Invoice generated using the Timesheet

![](/files/profitability-report.gif)

### Calculation of Utilization

The Utilization of the Employee is calculated using the Total Billed Hours from the Timesheet, Working Days from the Salary Slip, and the Standard Working Hours from HR Settings.

The formula for Utilization is as follows,
```
Utilization = Total Billed Hours / (Working Days * Standard Working Hours)
```

### Calculation of Profit
The Profit is calculated using the Gross Pay from the Salary Slip, Grand Total from the Sales Invoice, and Utilization.

The formula for Profit is as follows,
```
Profit = Grand Total - Gross Pay * Utilization
```

### Calculation of Fractional Cost
The Fractional Cost is calculated using Gross Pay from Salary Slip and Utilization.

The formula for Fractional Cost is as follows,
```
Fractional Cost = Gross Pay * Utilization
```

<!-- page: frappe-hr/hr__push-notification.md -->
---
title: "Push Notification"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/push-notification"
updated: "2026-02-04"
---

v15 onwards, all sites hosted on Frappe Cloud can enable Push Notifications for the mobile app.

Go to


> **Integrations > Push Notification Settings**
> 
> 

Check the **Enable Push Notification Relay** checkbox

![](https://frappehr.com/files/LoM5jEH.png)  


In your mobile app:

Go to **Profile > Settings** or **Notification Icon > Settings** and click on "**Enable Push Notifications"**

![push](https://frappehr.com/files/push.png "push.png")  


This will register your site on the Frappe Cloud relay server and you will receive push notifications.

![push-notifications](https://frappehr.com/files/push-notifications.png "push-notifications.png")  


  

<!-- page: frappe-hr/hr__recruitment.md -->
---
title: "Recruitment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/recruitment"
updated: "2026-02-04"
---

It is important for enterprises to create and manage vacant positions, job applicants and also create and manage recruitment plans. Frappe HR helps you create recruitment plans and create and publish job openings accordingly, making it easy to manage your hiring process. To understand how you can do configure this, check [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

  

<!-- page: frappe-hr/hr__reports__employee-ctc-break-up.md -->
---
title: "Employee CTC Break-Up"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/reports/employee-ctc-break-up"
updated: "2026-06-24"
---

**The Employee CTC Break-up report presents an employee's Cost to Company broken down by salary component. For each component it shows the per-cycle amount, the annual amount, and the share of CTC that the component represents.**

The report is generated for a single [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment), so it always reflects the structure and CTC assigned to that employee.

To access the Employee CTC Break-up report, go to:

> Home > Payroll > Employee CTC Break-up

**1. Prerequisites**
--------------------

Before viewing the report, the following must exist:

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment) with a CTC set

**2. How to view the report**
-----------------------------

There are two ways to open the report:

1. From a Salary Structure Assignment, click Actions > See CTC Break-up. The Employee and Salary Structure Assignment are selected automatically.
2. Go to Employee CTC Break-up and select the Company, Employee, and Salary Structure Assignment.

![Employee CTC Break-up report](/files/Screenshot From 2026-06-24 11-50-31.webp)

**3. Report columns**
---------------------

| Column | Description |
| --- | --- |
| Component | The salary component, shown with its abbreviation. |
| Type | Fixed for a flat amount, or Formula for a derived one. |
| Formula/Amount | The formula text, or the fixed amount. |
| Monthly / Fortnightly / ... | The per-cycle amount. The column title follows the payroll frequency. |
| Annual | The per-cycle amount multiplied by the number of cycles per year. |
| Percent of CTC (%) | The component's share of total CTC. |

**4. Sections**
---------------

The components are grouped into sections. Each section opens with a bold totals row that sums the components below it. The sections appear in this order:

1. Earnings
2. Deductions
3. Tax Deductions
4. Employer Contributions
5. Total Net Earnings
6. Total Gross Earnings

Employer contributions appear after the Tax Deductions section and before the net and gross totals. A section with no components still shows its totals row at zero, so the layout is consistent across employees.

**5. Understanding the totals**
-------------------------------

- Gross is the sum of payable earnings.
- Net is gross minus deductions and tax.
- CTC is gross plus employer contributions and any non-payout earnings, annualised.

Because employer contributions are part of CTC but not of net pay, two assignments with the same CTC can result in different take-home pay, depending on how much of the CTC is made up of employer contributions. The report makes this split visible.

For how employer-contribution components are configured, see [Salary Component](https://docs.frappe.io/hr/salary-component).

<!-- page: frappe-hr/hr__retention-bonus.md -->
---
title: "Retention Bonus"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/retention-bonus"
updated: "2026-02-04"
---

**Retention bonus is a payment or reward outside of an employee's regular salary that is offered as an incentive to keep a key employee on the job.**

Frappe HR allows you to configure Retention Bonus for an Employee for a particular period.

To access Retention Bonus, go to: > Home > Human Resources > Payroll > Retention Bonus

**1. Prerequisites**
--------------------

Before creating a Retention Bonus, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create a Retention Bonus**
--------------------------------------

1. Go to Retention Bonus list, click on New.
2. Select Employee and Bonus Payment Date.
3. Enter the Bonus Amount.
4. Select the [Salary Component](https://docs.frappe.io/hr/salary-component) under which you want to give the bonus.
5. Save and Submit.
6. On submit, 'Additional Salary' document of the specified 'Salary Component' is created. This will be fetched while running Payroll Entry.

![Retention Bonus](https://frappehr.com/files/retention-bonus.png)

**3. Related Topics**
---------------------

1. [Employee Incentive](https://docs.frappe.io/hr/employee-incentive)
2. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
3. [Salary Component](https://docs.frappe.io/hr/salary-component)
4. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__roster.md -->
---
title: "Roster"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/roster"
updated: "2026-02-04"
---

**1. Prerequisites**
--------------------

Before using the Roster, it is advisable you create the following:

* [Shift Type](https://docs.frappe.io/hr/shift-type)
* [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)

**2. How to Access the Roster**
----------------------------

To access the roster, go to:


> **Home > Human Resources > Shift &amp; Attendance > Roster**
> 
> 

You can also access it directly from https://<sitename>/hr/roster. For example, if your site url is https://frappeio.frappe.cloud, go to https://frappeio.frappe.cloud/hr/roster. 


**3. Features**
-----------

### **3.1 Calendar View**

The Roster features the visualization of Employee - Shift, Leave, and Holiday mapping in an Employee vs Day of the Month representation. 

![355695579-9695b9dc-7b07-4541-93b0-d55521e01362](/files/355695579-9695b9dc-7b07-4541-93b0-d55521e01362.png)

### **3.2 Searching and Filtering**

You can use the search bar to search for employees. You can also filter shifts by company, department, branch, designation, and shift type.

![](/files/355696715-ced58ea2-f2da-4560-be88-c917859d572b.png)

### **3.3 Creating Shifts**

Click on the plus button in a cell to create a shift corresponding to that date and employee. The roster allows for two types of shifts to be created.

**Regular Shifts**

Creating a regular shift results in the creation of a single Shift Assignment. Shifts spanning a week or less are automatically created as regular. For shifts spanning over a week, the user will have to select all days from the Repeat On Days field, under Schedule Settings, to ensure that a regular shift is created.

![355756505-0ec2ecee-e311-40fc-95e4-99562a3ca2ef](/files/355756505-0ec2ecee-e311-40fc-95e4-99562a3ca2ef.png)  

**Repeating/Scheduled Shifts**

The user has the option to turn shifts spanning over a week into repeating shifts. This can be done by selecting specific days from the Repeat On Days field and setting the Frequency field—which represents the frequency of repetition. Doing so will fetch a Shift Schedule with these specifications, or create a new one if it does not exist. This Shift Schedule will then be assigned to the employee with the rest of the shift details via a Shift Schedule Assignment.

![355697616-f0731f69-3897-40b2-afa2-b0b4b8e77404](/files/355697616-f0731f69-3897-40b2-afa2-b0b4b8e77404.png)

### **3.4 Viewing and Updating Shifts**

Click on a shift to view it in detail. Edit its values and click on 'Update' to update it. 

![](/files/355740198-14aeb033-375d-4a55-81d4-d1a9354a2d3e%2010.56.45%E2%80%AFAM.png)

### **3.5 Deleting Shifts**

Click on the Delete button to delete a shift. This presents the user with three options:-

**Shift for [Date]**: Delete the shift only on that date. This is done by updating the Shift Assignment and creating another one if needed.

**All Consecutive Shifts**: Delete the Shift Assignment altogether.

**Shift Schedule Assignment**: Delete the Shift Schedule Assignment and all the Shift Assignments associated with it.

![](/files/Screenshot%202024-12-19%20at%2012.50.09%E2%80%AFPM.png)


### **3.5 Moving and Swapping Shifts**

Shifts can be dragged and dropped to move them. Dropping a shift on another will swap it with that one.

![355751174-509bb203-8e39-42aa-8cd9-aebf0e6beeb3](/files/355751174-509bb203-8e39-42aa-8cd9-aebf0e6beeb3.gif)

**4. Related Topics**
---------------------

1. [Shift Type](https://docs.frappe.io/hr/shift-type)
2. [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)
3. [Shift Schedule](https://docs.frappe.io/hr/shift-schedule)
4. [Shift Schedule Assignment](https://docs.frappe.io/hr/shift-schedule-assignment)
