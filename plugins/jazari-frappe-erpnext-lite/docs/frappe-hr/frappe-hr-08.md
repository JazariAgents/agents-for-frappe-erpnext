<!-- Frappe documentation: frappe-hr, part 8 of 10. Index: docs/INDEX.md -->

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

[Screenshot on the live page]  


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

[Screenshot on the live page]  


#### **2.1 Disable Rounded Total**

If enabled, hides and disables Rounded Total field in Salary Slips

#### **2.2 Show Leave Balances in Salary Slip**

**3. Email**
------------

[Screenshot on the live page]  


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

[Screenshot on the live page]  


#### **4.1 Define Opening Balance for Earning and Deduction**

If enabled, it will allow you to set up opening entries for **Taxable Earnings till Date** and **Tax Deducted till Date** in the Salary Structure Assignment if there are no existing salary slips for the employee.**[Screenshot on the live page]**  


#### **4.2 Process Payroll Accounting Entry based on Employee**

By default, a consolidated Journal Entry is created against the Payroll Entry for all the employees. If you want a better breakup of payroll amounts per employee, enable this to process employee-wise accounting entries.

[Screenshot on the live page]  


  

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

[Screenshot on the live page: Salary Component Earnings]  


* Is Additional Component: This option specify that the component can only be paid as Additional Salary. Examples of this component could be Performance Bonus or pay received for on-site deputation etc. Such components are not considered to be part of normal Salary Structure. Instead, Additional Salary with these components can be submitted as required which will be added to the Salary Slip automatically.
* Is Tax Applicable: If a component needs to be considered for Tax calculations specified as per the Payroll Period you may want to enable this option. It would be required that you have a Payroll Period and Income Tax Slab configured with valid Tax Slabs for payroll processing.
* Is Payable: Such components can be booked against separate payable accounts and the Accounts shall be configured in the Accounts table
* Flexible Benefits: Flexible Benefits are earning components which Employees can choose to receive on a pro-rata basis or annually when they claim for. These are mostly tax exempted, unless the Employee fail to file the claim with adequate bills / documents. If turned on, you can specify the maximum benefit allowed for an employee in a year. Employees can create [Employee Benefit Application](https://docs.frappe.io/hr/employee-benefit-application) with the ones they opt for.

>Note: Employee Benefit Application will only allow Employees to only choose from the flexible components which are present in the Salary Structure assigned to the Employee


	+ Pay Against Benefit Claim: Employees can opt to receive flexible benefits annually via Employee Benefit Claim or along with their salary every month. If you enable this, the amount allocated for the component will be paid as the Employee submits an [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim.html). Else the amount will be dispersed as part of the Employee's salary on a pro-rata basis.
	
	
		- Only Tax Impact (Cannot Claim But Part of Taxable Income): Such components are those which the company has already paid to the Employee in cash or by some other means, for example a car purchased for the Employee's use. The Employee cannot claim but is liable to pay tax. The amount allocated for this component will be considered while calculating the taxable income of the Employee.
		- Create Separate Payment Entry Against Benefit Claim: Some of the flexible benefits may be legally required to be paid via separate vouchers. If you enable this, while posting the bank entry the amount paid for such components will be posted as a separate entry for each Employee.[Screenshot on the live page: Flexible Salary Component]  
	
	
	> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before that last payroll, use "Deduct Tax For Unclaimed Employee Benefits" in Payroll Entry / Salary Slip while processing the Salary.

#### **Deduction**

[Screenshot on the live page: Salary Component Deduction]  


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

[Screenshot on the live page: Submitted Salary Structure] A submitted Salary Structure

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

[Screenshot on the live page: Salary Slip based on Timesheet]  


#### **Earnings and Deductions in Salary Structure**

In the “Earnings” and “Deductions” tables, you can select the earnings and deductions components The condition and formula configured in Salary Component will be copied by default, but you may change this if required. You may also want to select the Base component in the Earnings table. Note that the amount eligible for each employee should be configured in Salary Structure Assignment.

If the condition and formula for any of the earnings or deductions are not configured in Salary Component, you can calculate the values of Salary Components based on,

#### **Condition and Formula**

[Screenshot on the live page: Condition and Formula]  


#### **Condition and Amount**

[Screenshot on the live page: Condition and Amount]  


In conditions and formulas,

* Use field "base" for using base salary of the Employee
* Use Salary Component abbreviations. For example: BS for Basic Salary
* Use field name for employee details. For example: Employment Type for employment_type

#### **Account Details**

[Screenshot on the live page: Salary Structure Account]  


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

[Screenshot on the live page: Salary Structure Assignment]  




---

**Processing Payroll**
======================

You can either bulk process payroll for Employees under a department, branch or designation or process payroll individually by creating Salary Slips for each employee.

**Payroll Processing Using Payroll Entry**
------------------------------------------

You can also create salary slip for multiple employees using Payroll Entry:

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

#### **Payroll Entry**

[Screenshot on the live page: Payroll Entry]  


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

[Screenshot on the live page: Submitted Payroll Entry]  


Once all Salary Slips are created, you can use *View Salary Slips* to verify if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).

After checking, you can "Submit" them all together by clicking on "Submit Salary Slip".

>Note: Submitting Salary Slips will also book the default Payroll Payable account to record the accrual of salary.

#### **Booking Salaries in Accounts**

The final step is to book the Salaries in your Accounts.

Salaries in businesses are usually dealt with extreme privacy. In most cases, the companies issues a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account. This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the earning type salary component and credits the total of deduction type salary component of all Employees to the default account set at Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on - > Make > Bank Entry

[Screenshot on the live page: Payroll Make Entry]  


Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You shall set reference number and date for the transactions and Submit the Journal Entries.

>Note: For Salary Components which are Flexible Benefits and has *Create Separate Payment Entry Against Benefit Claim* checked, Frappe HR will book separate draft Journal Entries.

[Screenshot on the live page: Payroll Entry]  


**Creating Salary Slips Manually**
----------------------------------

Once the Salary Structure is created and assigned to employees via Salary Structure Assignment, you can make a Salary Slip individually. Go to:

> Human Resources > Payroll > Salary Slip > New Salary Slip

#### **Salary Slip**

[Screenshot on the live page: Salary Slip]  


  

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

[Screenshot on the live page]

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

[Screenshot on the live page]  


In your mobile app:

Go to **Profile > Settings** or **Notification Icon > Settings** and click on "**Enable Push Notifications"**

[Screenshot on the live page: push]  


This will register your site on the Frappe Cloud relay server and you will receive push notifications.

[Screenshot on the live page: push-notifications]  


  

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

[Screenshot on the live page: Employee CTC Break-up report]

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

[Screenshot on the live page: Retention Bonus]

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

[Screenshot on the live page: 355695579-9695b9dc-7b07-4541-93b0-d55521e01362]

### **3.2 Searching and Filtering**

You can use the search bar to search for employees. You can also filter shifts by company, department, branch, designation, and shift type.

[Screenshot on the live page]

### **3.3 Creating Shifts**

Click on the plus button in a cell to create a shift corresponding to that date and employee. The roster allows for two types of shifts to be created.

**Regular Shifts**

Creating a regular shift results in the creation of a single Shift Assignment. Shifts spanning a week or less are automatically created as regular. For shifts spanning over a week, the user will have to select all days from the Repeat On Days field, under Schedule Settings, to ensure that a regular shift is created.

[Screenshot on the live page: 355756505-0ec2ecee-e311-40fc-95e4-99562a3ca2ef]  

**Repeating/Scheduled Shifts**

The user has the option to turn shifts spanning over a week into repeating shifts. This can be done by selecting specific days from the Repeat On Days field and setting the Frequency field—which represents the frequency of repetition. Doing so will fetch a Shift Schedule with these specifications, or create a new one if it does not exist. This Shift Schedule will then be assigned to the employee with the rest of the shift details via a Shift Schedule Assignment.

[Screenshot on the live page: 355697616-f0731f69-3897-40b2-afa2-b0b4b8e77404]

### **3.4 Viewing and Updating Shifts**

Click on a shift to view it in detail. Edit its values and click on 'Update' to update it. 

[Screenshot on the live page]

### **3.5 Deleting Shifts**

Click on the Delete button to delete a shift. This presents the user with three options:-

**Shift for [Date]**: Delete the shift only on that date. This is done by updating the Shift Assignment and creating another one if needed.

**All Consecutive Shifts**: Delete the Shift Assignment altogether.

**Shift Schedule Assignment**: Delete the Shift Schedule Assignment and all the Shift Assignments associated with it.

[Screenshot on the live page]


### **3.5 Moving and Swapping Shifts**

Shifts can be dragged and dropped to move them. Dropping a shift on another will swap it with that one.

[Screenshot on the live page: 355751174-509bb203-8e39-42aa-8cd9-aebf0e6beeb3]

**4. Related Topics**
---------------------

1. [Shift Type](https://docs.frappe.io/hr/shift-type)
2. [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)
3. [Shift Schedule](https://docs.frappe.io/hr/shift-schedule)
4. [Shift Schedule Assignment](https://docs.frappe.io/hr/shift-schedule-assignment)

<!-- page: frappe-hr/hr__salary-component.md -->
---
title: "Salary Component"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-component"
updated: "2026-06-24"
---

**Salaries are paid by organizations to their employees in exchange for the services rendered by them. The different components that make up the Salary Structure are called as Salary Components.**

Salary paid to the employees comprises of several different components, such as basic salary, allowances, arrears, etc. Frappe HR allows you to define these Salary Components and also specify its various attributes.

To access Salary Component, go to: > Home > Human Resources > Payroll > Salary Component

## **1. How to create a Salary Component**

To create a new Salary Component:

1. Go to Salary Component list, click on New.
2. Enter its Name and Abbreviation.
3. Enter Description of the Salary Component (optional).
4. Enter the Company name and the Default Account of the Salary Component in the Accounts table.
5. Save.

[Screenshot on the live page]

## **2. Features**

Apart from the above mentioned mandatory fields, some of the additional features of the Salary Component are given below:

### **2.1 Condition and Formula**

In this section, the Condition and Formula required for the calculation of the Salary Component can be specified. To specify the formula, enable the 'Amount based on formula' checkbox.

[Screenshot on the live page]



You can sync updated Condition and Formula values of a Salary Component with existing Salary Structures, where the Component is being used, with the Update Salary Structures button.

[Screenshot on the live page]



In case the Salary Component is based on a pre-defined amount, Frappe HR allows you to directly enter the amount in the Amount field (disable the 'Amount based on formula' checkbox).

You can also use some mathematical/date functions while writing formulae.

```
# Consider a component `basic` with amount as 1220.32 as an example:

# int - cast the amount as int
int(basic) # evaluates to 1220

# flt - cast the amount as flt
flt(basic, 1) # evaluates to 1220.3

# round - rounds the amount (Banker's Rounding)
round(basic) # evaluates to 1220

# rounded - rounds the amount based on System Settings or passed method (Banker's Rounding or Commercial Rounding)
# If basic is 1220.5
round(1220.5) # evaluates to 1220
rounded(1220.5, rounding_method="Banker's Rounding") # evaluates to 1220
rounded(1220.5, rounding_method="Commercial Rounding") # evaluates to 1221

# ceil - rounds the number up to the nearest integer
ceil(basic) # evaluates to 1221

# floor - rounds the number down to the nearest integer
floor(basic) # evaluates to 1220

# getdate/date - casts the value `start_date` to a `datetime.date` object
# eg: Professional Tax is 300 in February and 200 in every other month. `start_date` takes up the value of salary slip's `start_date`
# In that case the condition can be written as given below:

300 if getdate(start_date).month == 2 else 200

  

```

> **Note:** This above setup is optional. You can define Amount and Formula/Condition for a Salary Component directly in the Salary Structure also. If they are specified in the Salary Component document itself, the information will be directly fetched in the Salary Structure when the Component is selected.

### **2.2 Additional Properties**

Some of the additional attributes of the Salary Component that can be enabled using checkboxes are as follows:

- **Is Payable:** Select this if the Salary Component is payable.
- **Depends on Payment Days:** If this checkbox is enabled then the Salary Component will be calculated based on the number of working days.
- **Is Tax Applicable:** This checkbox is applicable for Earning Components. Selecting this checkbox allows tax to be applied on this Salary Component.
- **Deduct Full Tax on Selected Payroll Date:** If checked and the component is used in Additional Salary, the tax amount applicable on the additional amount will be deducted on the specific payroll month. If not checked, the tax will be distributed over the remaining months of the payroll period. For example, if a bonus is given in a particular month using Additional Salary, then you can deduct full tax amount in the same month only.
- **Round to the Nearest Integer:** Selecting this checkbox allows you to round the amount of this Salary Component to the nearest integer.
- **Statistical Component:** If selected, the value specified or calculated in this component will not contribute to the earnings or deductions. However, it's value can be referenced by other components that can be added or deducted. If you set a Salary Component as a Statistical component, then you do not have to set the Default Account for the same. Also, you would not be able to set this component as a Flexible Benefit.
- **Do Not Include in Total:** Selecting this checkbox ensures that the Salary Component is not included in the Total Salary. It is used to define the component which is part of the CTC, not payable but should apprear on employee's salary slip (e.g. Usage of Company Cars).
- **Variable Based On Taxable Salary:** The component is calculated automatically on taxable income based on applicable Income Tax Slab (e.g. TDS or Income Tax).
- **Exempted from Income Tax:** If checked, the full amount will be deducted from taxable income before calculating income tax without any [declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration) or [proof submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission). For example, Professional Tax in India is deducted from taxable income before calculating income tax.
- **Disabled:** This checkbox can be selected to disable this Salary Component. A disabled Salary Component cannot be used in the Salary Structure.

### **2.3 Flexible Benefits**

This section is shown if the Salary Component is an Earning Component. Flexible Benefit plans allow employees to avail the benefits they want or need from a package of programs offered by an employer. They may include health insurance, pension plans, telephone expenses, etc. To set a Salary Component as a Flexible Benefit, check the 'Is Flexible Benefit' checkbox.

[Screenshot on the live page]



Enter the maximum yearly amount for this flexible benefit in the 'Max Benefit Amount (Yearly)' field. Some of the additional attributes of the Flexible Benefits that can be enabled using checkboxes are as follows:

- **Pay Against Benefit Claim:** Enable this checkbox if you want to pay this benefit via the [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim).
- **Only Tax Impact (Cannot Claim But Part of Taxable Income):** If set, the flexible benefit will be part of taxable income.
- **Create Separate Payment Entry Against Benefit Claim:** If this checkbox is checked, it will let you create a separate payment entry against the Benefit Claim.

### **2.4 Employer Contribution**

Apart from Earning and Deduction, a Salary Component can be of the type Employer Contribution. This represents a cost the employer bears on the employee's behalf, such as the employer's share of provident fund or an employer NPS contribution. It is part of the Cost to Company (CTC), but it is not paid to the employee and does not appear on the Salary Slip.

To set a Salary Component as an employer contribution, set Type to Employer Contribution while creating the component.

[Screenshot on the live page]

Employer contributions are added to the Salary Structure through a dedicated Employer Contributions table, separate from the Earnings and Deductions tables. The amount can be fixed or based on a formula, and the formula can reference earning abbreviations and `gross_pay` (for example, `BS * 0.12` for 12% of basic salary).

When a Salary Structure Assignment is saved, employer contributions are included in the CTC but not in gross or net pay:

> CTC = (per-cycle gross + employer contributions + non-payout earnings) x cycles per year

You can view employer contributions against the employee's CTC in the [Employee CTC Break-up](https://docs.frappe.io/hr/reports/employee-ctc-break-up) report.

## **3. Related Topics**

1. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
2. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
3. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
4. [Payroll Period](https://docs.frappe.io/hr/payroll-period)

<!-- page: frappe-hr/hr__salary-slip.md -->
---
title: "Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-slip"
updated: "2026-07-05"
---

**A salary slip is a document issued to an employee. It contains a detailed description of the employee’s salary components and amounts.**

To access Salary Slip, go to: > Home > Human Resources > Payroll > Salary Slip

## **1. Prerequisites**

Before creating Salary Slip, it is advised that you create the following first:

- [Employee](https://docs.frappe.io/hr/employee)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)
- [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)

## **2. How to create a Salary Slip**

1. Go to Salary Slip, Click on New.
2. Select Employee. On selecting Employee all details of the Employee will be fetched from Salary Structure which is assigned to that Employee. This includes details such as Payroll Frequency, Earnings, Deductions, etc.
3. Select Start Date and End Date.
4. Save.

## **3. Feature**

### **3.1. Salary Slip based on Attendance/Leave**

HR users can create Salary Slip based on Attendance or leave. The Working days will calculated on basis of leave/Attendance, depending on the field **Calculate Payroll Working Days Based On** in [HR Settings](https://docs.frappe.io/hr/hr-settings). If Payroll is based on Attendance then, the **Leave without pay** will be considered as absent and **half-day** will be considered as half-day absent.

### **3.2. Salary Slip based on Timesheet**

For creating Salary Slip based on timesheet you need to create Salary Structure for Timesheets.

Frappe HR also provides an option to create Salary slip based on working hours based on [Timesheet](https://docs.erpnext.com/docs/user/manual/en/timesheets). You can create Salary Slip after submitting the Timesheet by clicking directly on **Create Salary Slip** button on the top right.

[Screenshot on the live page: Create Salary Slip based on Timesheets]



The Payment Amount is calculated based on Hour Rate defined in Salary Structure and is reflected in the Earnings table.

### **3.3 Year to Date and Month to Date**

For every salary slip, 'Year to Date' and 'Month to Date' are computed.

[Screenshot on the live page: Year to Date and Month to Date]



- **Year to Date**: Total salary booked for that particular employee from the beginning of the year (payroll period or fiscal year) up to the current salary slip's end date.
- **Month to Date**: Total salary booked for a particular employee from the beginning of the month (for which the payroll entry is created) up to the current salary slip's end date.

Year to Date is also computed for every component in the earnings and deduction tables. The "Salary Slip with Year to Date" print format is available with Year to Date and Month to Date computations.

[Screenshot on the live page: Year to Date for Salary Slip Components]



### **3.4 Bulk Email Salary Slips**

By default, the Payroll Entry sends salary slip emails to all the employees on salary slip submission if **Email Salary Slip to Employee** is enabled in Payroll Settings. Optionally, you can also set up the sender email account and email template for this.

[Screenshot on the live page]



But if there are a few employees who don't have an email ID set or the setup is incorrect during this action, you can use the bulk action in the Salary Slip list view to trigger sending emails to selected employees later.

[Screenshot on the live page: bulk]

<!-- page: frappe-hr/hr__salary-structure-and-payroll.md -->
---
title: "Salary Structure and Payroll"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-structure-and-payroll"
updated: "2026-02-04"
---

**Use case 1:**What if one Salary structure has to be assigned to all the Employees ?

If a single Salary structure has to be assigned, it is preferable to create a structure for all the Employees, irrespective of their Salaries, but we can set formula based on which actual salary structures can be allocated to each employee in an organisation.

Go to Salary Structure --> select the Earning or deduction component --> Add formula

[Screenshot on the live page]  


This way, salary will be calculated individually for each employee depending on their monthly income.

**Use case 2:** What if while generating a payroll, all the employees are not supposed to be fetched, payroll has to be created for selected employees?

Generally, while a payroll is being processed, there is an option --> **Get Employees,** once it is clicked, all the employees are fetched.

In case, there is only a selected list of employees payroll to be generated, it is preferable to select the employees by filtering on the basis of department, branch, or designation, this way only the selected list of employees belonging to the particular filter will be selected for payroll.

[Screenshot on the live page]  


  

<!-- page: frappe-hr/hr__salary-structure-assignment-tool.md -->
---
title: "Salary Structure Assignment Tool"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-structure-assignment-tool"
updated: "2026-02-04"
---

The Salary Structure Assignment Tool allows you to assign Salary Structures to employees in bulk.

> Home > Human Resources > Payroll > Salary Structure Assignment Tool

**1\. Prerequisites**
---------------------

Before using the Salary Structure Assignment Tool, it is advisable to create the following documents:

*   [Employee](/hr/employee)
    
*   [Salary Structure](/hr/salary-structure)
    

**2\. How to assign Salary Structures using the Salary Structure Assignment Tool**
----------------------------------------------------------------------------------

1.  Select a Company if it hasn't already been selected. This should also fetch its default Payroll Payable Account.
    
2.  Select the Salary Structure that you wish to assign. This will fetch the Currency associated with it.
    
3.  Select From Date which is the date from which you wish to assign the Salary Structure. This will cause all employees, that do not already have a Salary Structure Assignment on that date, to be loaded in the Select Employees table below.
    
4.  Select an Income Tax Slab if applicable.
    
5.  Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
    
6.  Select suitable employees from the Select Employees table below.
    
7.  You can update the Base and Variable amounts for an employee by double clicking and editing the required cell. If you wish to update these values in bulk, click on the Update button, select the appropriate field, and enter the desired amount. Click on Update.
    
8.  If everything looks right, click on the Assign Structure button.
    

[Screenshot on the live page]  

[Salary Structure Assignments](https://docs.frappe.io/hr/salary-structure-assignment) made using this tool will now be found in their list:

[Screenshot on the live page]  

**3\. Related Topics**
----------------------

1.  [Payroll Period](/hr/payroll-period)
    
2.  [Income Tax Slab](/hr/income-tax-slab)
    
3.  [Salary Component](/hr/salary-component)
    
4.  [Salary Slip](/hr/salary-slip)
    
5.  [Payroll Entry](/hr/payroll-entry)
