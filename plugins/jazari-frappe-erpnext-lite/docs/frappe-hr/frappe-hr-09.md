<!-- Frappe documentation: frappe-hr, part 9 of 10. Index: docs/INDEX.md -->

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

![](https://frappehr.com/files/of1TI53.png)

## **2. Features**

Apart from the above mentioned mandatory fields, some of the additional features of the Salary Component are given below:

### **2.1 Condition and Formula**

In this section, the Condition and Formula required for the calculation of the Salary Component can be specified. To specify the formula, enable the 'Amount based on formula' checkbox.

![](https://frappehr.com/files/QoxdTZF.png)



You can sync updated Condition and Formula values of a Salary Component with existing Salary Structures, where the Component is being used, with the Update Salary Structures button.

![](https://frappehr.com/files/sgRLa11.png)



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

![](https://frappehr.com/files/3lypNxJ.png)



Enter the maximum yearly amount for this flexible benefit in the 'Max Benefit Amount (Yearly)' field. Some of the additional attributes of the Flexible Benefits that can be enabled using checkboxes are as follows:

- **Pay Against Benefit Claim:** Enable this checkbox if you want to pay this benefit via the [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim).
- **Only Tax Impact (Cannot Claim But Part of Taxable Income):** If set, the flexible benefit will be part of taxable income.
- **Create Separate Payment Entry Against Benefit Claim:** If this checkbox is checked, it will let you create a separate payment entry against the Benefit Claim.

### **2.4 Employer Contribution**

Apart from Earning and Deduction, a Salary Component can be of the type Employer Contribution. This represents a cost the employer bears on the employee's behalf, such as the employer's share of provident fund or an employer NPS contribution. It is part of the Cost to Company (CTC), but it is not paid to the employee and does not appear on the Salary Slip.

To set a Salary Component as an employer contribution, set Type to Employer Contribution while creating the component.

![](/files/Screenshot From 2026-06-24 11-37-24.png)

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

![Create Salary Slip based on Timesheets](https://frappehr.com/files/create-salary-slip-based-on-timesheets.png)



The Payment Amount is calculated based on Hour Rate defined in Salary Structure and is reflected in the Earnings table.

### **3.3 Year to Date and Month to Date**

For every salary slip, 'Year to Date' and 'Month to Date' are computed.

![Year to Date and Month to Date](https://frappehr.com/files/ytd-and-mtd.png)



- **Year to Date**: Total salary booked for that particular employee from the beginning of the year (payroll period or fiscal year) up to the current salary slip's end date.
- **Month to Date**: Total salary booked for a particular employee from the beginning of the month (for which the payroll entry is created) up to the current salary slip's end date.

Year to Date is also computed for every component in the earnings and deduction tables. The "Salary Slip with Year to Date" print format is available with Year to Date and Month to Date computations.

![Year to Date for Salary Slip Components](https://frappehr.com/files/ytd-component.png)



### **3.4 Bulk Email Salary Slips**

By default, the Payroll Entry sends salary slip emails to all the employees on salary slip submission if **Email Salary Slip to Employee** is enabled in Payroll Settings. Optionally, you can also set up the sender email account and email template for this.

![](https://frappehr.com/files/X8WK2C7.png)



But if there are a few employees who don't have an email ID set or the setup is incorrect during this action, you can use the bulk action in the Salary Slip list view to trigger sending emails to selected employees later.

![bulk](https://frappehr.com/files/bulk.png "bulk.png")

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

![](https://docs.erpnext.com/files/kNXzqwY.png)  


This way, salary will be calculated individually for each employee depending on their monthly income.

**Use case 2:** What if while generating a payroll, all the employees are not supposed to be fetched, payroll has to be created for selected employees?

Generally, while a payroll is being processed, there is an option --> **Get Employees,** once it is clicked, all the employees are fetched.

In case, there is only a selected list of employees payroll to be generated, it is preferable to select the employees by filtering on the basis of department, branch, or designation, this way only the selected list of employees belonging to the particular filter will be selected for payroll.

![](https://docs.erpnext.com/files/BwEvgFb.png)  


  

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
    

![](https://frappehr.com/files/pnlAEli.png)  

[Salary Structure Assignments](https://docs.frappe.io/hr/salary-structure-assignment) made using this tool will now be found in their list:

![](https://frappehr.com/files/ZZ01jWY.png)  

**3\. Related Topics**
----------------------

1.  [Payroll Period](/hr/payroll-period)
    
2.  [Income Tax Slab](/hr/income-tax-slab)
    
3.  [Salary Component](/hr/salary-component)
    
4.  [Salary Slip](/hr/salary-slip)
    
5.  [Payroll Entry](/hr/payroll-entry)

<!-- page: frappe-hr/hr__salary-structure-assignment.md -->
---
title: "Salary Structure Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-structure-assignment"
updated: "2026-02-04"
---

**Salary Structure Assignment form allows you to assign a particular Salary Structure to the employee.**

In Frappe HR, you can create multiple Salary Structure Assignments for the same Employee for different periods.

To access Salary Structure Assignment, go to: > Home > Human Resources > Payroll > Salary Structure Assignment

**1. Prerequisites**
--------------------

Before you create a Salary Structure Assignment, it is advisable you have the following documents:

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Salary Component](https://docs.frappe.io/hr/salary-component)
3. [Salary Structure](https://docs.frappe.io/hr/salary-structure)

**2. How to create a Salary Structure Assignment:**
---------------------------------------------------

1. Go to Salary Structure Assignment list and click on New.
2. Select the Employee and Salary Structure.
3. Select the From Date from which this particular Salary Structure will be applicable.
4. Select preferred Income Tax Slab for the employee.
5. Enter Base and Variable amount as per requirement. Base amount refers to the Base Salary of the Employee, which is fixed and paid out, regardless of employees meeting their goals. Variable pay, on the other hand, is the portion of sales compensation determined by employee performance. When employees hit their goals (aka quota), variable pay is provided as a type of bonus, incentive pay, or commission.

![Salary Structure Assignment](https://frappehr.com/files/salary-structure-assignment.png)

### **3.1 Bulk Salary Structure Assignment**

Frappe HR also allows creating Salary Structure Assignments for multiple employees at once.

1. Go to the Salary Structure list.
2. Click on Bulk Salary Structure Assignment.
3. This will take you to the [Salary Structure Assignment Tool](https://docs.frappe.io/hr/salary-structure-assignment-tool), where you can assign Salary Structures in bulk.

![](https://frappehr.com/files/STjQmpp.png)  



> **For version 14, follow the steps below.**
> 
> 

You can assign a Salary Structure to Employee(s) directly through the Salary Structure document. To assign the Salary Structure to a single employee, click on the 'Assign Salary Structure' button in the Salary Structure document.

![Salary Structure Assignment](https://frappehr.com/files/assign-sal1.png)  


If you want to bulk assign the Salary Structure to multiple employees, you can do so via the 'Assign to Employees' button.

![Salary Structure Assignment](https://frappehr.com/files/assign-sal2.png)  


You can optionally filter out employees based on Employee Grade, Department, Designation, and Employee itself.

![Salary Structure Assignment](https://frappehr.com/files/assign-sal3.png)  


Once this is done, click on the 'Assign' button to assign the Salary Structure accordingly.

**4. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Employee Grade](https://docs.frappe.io/hr/employee-grade)
4. [Department](https://docs.frappe.io/hr/department)
5. [Designation](https://docs.frappe.io/hr/designation)
6. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__salary-structure.md -->
---
title: "Salary Structure"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/salary-structure"
updated: "2026-02-04"
---

**Salary Structure is the details of the salary being offered to an Employee, in terms of the breakup of the different components constituting the compensation.**

Any changes to the Salary Structure i.e. among the components can have a major impact on what the Employee does, such as the kind of tax exemptions claimed.

Frappe HR allows you to define the Earnings and Deductions of a Salary Structure, Payroll frequency, and Payment Mode among other features.

To access Salary Structure, go to:


> **Home > Human Resources > Payroll > Salary Structure**
> 
> 

**1. Prerequisites**
--------------------

Before you create a Salary Structure, it is advisable you have the following:

* [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create a Salary Structure**
---------------------------------------

1. Go to the Salary Structure list, click on New.
2. Enter the Salary Structure Name.
3. Select the Company Name and Payroll Frequency.
4. Save and Submit.

**2. Features**
---------------

### **2.1 Earnings and Deductions**

Earnings specify the Salary Components that are earned by an Employee. These components typically include basic, allowances, bonuses, and incentives that are added to the employee's Total Salary. On the other hand, Deductions specify the Salary Components that are deducted from the employee's Total Salary. These typically include the taxes.


> **Note: Only Salary Components set as 'Earnings' will be shown in the Earnings table and components set as 'Deductions' will be shown in the Deductions table.**
> 
> 

To create Earnings and Deductions, select the Salary Component in the Component column. Enter the Formula/Condition if not previously specified while creating the [Salary Component](https://docs.frappe.io/hr/salary-component). Additionally, you can also enter a pre-defined amount in the Amount column.

![Salary Structure](https://frappehr.com/files/salary-structure.png)  



> **Note: Make sure to click on the downward arrow and enable the 'Amount based on formula' checkbox in case the Salary Component is calculated using a formula.**
> 
> 

### **2.2 Account**

In this section, the [Mode of Payment](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/articles/mode-of-payment) and the [Payment Account](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/chart-of-accounts) that is used to pay the salary can be specified.

### **2.3 Salary Structure for Salary based on Timesheets**

In Frappe HR you can also define the Salary Structure for Salary Slip based on Timesheet, which allows the Company to pay there Employee as per working hours.

Steps for creating Salary Structure based on Timesheets:

1. Go to Salary Structure List, click on New.
2. Select checkbox **Salary Slip Based on Timesheet**.
3. Select the Salary Component.
4. Enter the Hour Rate. Based on the Rate entered, the amount for Working hours for the selected Salary Component will be calculated accordingly.
5. Save and Submit.

![Create Salary Slip based on Timesheets](https://frappehr.com/files/salary-structure-for-salary-based-on-timesheets.png)

### **2.4 Leave Encashment Amount Per Day**

In case there are encashable leaves for an Employee, you can define the leave encashment amount per day in this field for this particular Salary Structure. Based on the 'Earning Component' set in the encashed [Leave Type](https://docs.frappe.io/hr/leave-type) and the amount per day, the value for the Salary component will be calculated accordingly in the Salary Slip.

### **2.5 Max Benefits (Amount)**

In this field, the Max Benefits Amount for the Salary Structure can be specified. If this field is filled, make sure the Salary Structure has a [Salary Component](https://docs.frappe.io/hr/salary-component) with the "Is Flexible Benefits" checked, against which this amount will be paid.

Once all the information is saved and submitted, you can assign the Salary Structure by clicking on the Create button and selecting 'Single Assignment' to assign a single employee or 'Bulk Assignments' to assign multiple employees via the [Salary Structure Assignment Tool](https://docs.frappe.io/hr/salary-structure-assignment-tool).

You can also preview the associated Salary Slip by clicking on the Actions button and selecting 'Preview Salary Slip'.

**3. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
3. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__setting-employee-wise-leave-approver.md -->
---
title: "Setting Employee-wise Leave Approver"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/setting-employee-wise-leave-approver"
updated: "2026-02-04"
---

**Use Case:** Need to set up one Leave Approver per Employee.

**Steps:**

1) Go to the Employee's master.

2) In "Attendance and Leave Details" section, select the Leave Approver for that particular Employee.

![](https://docs.erpnext.com/files/rVabhxn.png)


3) Assign a Leave Policy to the Employee through the Employee master and Grant leaves through Leave Period.

4) Create a new Leave Application for the Employee. The system automatically fetches the Leave Approver set for that particular Employee.

![](https://docs.erpnext.com/files/hVuDojL.png)  


**Note:** In case you have set a Department for that Employee, and Leave Approvers are also set in that particular Department, then those Leave Approvers will also be fetched in the Leave Application. However, the default Leave Approver will always be the one set in the Employee master.

For example, a Leave Approver is set in the Department.

![](https://docs.erpnext.com/files/wKT4Zcb.png)  


Now, if an Employee belonging to this Department creates a Leave Application, all the Leave Approvers set for this Department will also be fetched in his Leave Application.

![](https://docs.erpnext.com/files/3nyXGpt.png)  

<!-- page: frappe-hr/hr__setting-flexible-benefits-against-a-benefit-claim.md -->
---
title: "Setting Flexible Benefits against a Benefit Claim"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/setting-flexible-benefits-against-a-benefit-claim"
updated: "2026-02-04"
---

**Flexible benefit** plans allow employees to avail the **benefits** they want or need from a package of programs offered by an employer. They may include health insurance, pension plans, telephone expenses, etc.

  


To set Flexible Benefits in Frappe HR, follow the following steps:

  


1) Go to Salary Component for which you want to set flexible benefits for and select the **"Is Flexible Benefit"** checkbox. Enter the Yearly **Max. Benefit Amount**. Select the **"Pay Against Benefit Claim**" checkbox to avail the flexible benefits via a Benefit Claim.

![](https://docs.erpnext.com/files/gpYJN0U.png)  


2) Set up a Salary Structure for the Employee with this Salary Component. Set the Amount to 0. Also, enter the Max Benefits Amount for this Salary Structure.

![](https://docs.erpnext.com/files/CoNsmqr.png)3) Assign the Salary Structure to the employee via Salary Structure Assignment.

4) Create an Employee Benefit Claim for this employee. Select the Claim Date, Component and enter the Claimed Amount.

![](https://docs.erpnext.com/files/Qvfr4xl.png)  


5) Run the Payroll Entry. The amount will be fetched against the component in the Salary Slip as seen below.

![](https://docs.erpnext.com/files/Iyh0LJa.png)  

<!-- page: frappe-hr/hr__setting-up-income-tax-deduction.md -->
---
title: "Setting Up Income Tax Deduction"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/setting-up-income-tax-deduction"
updated: "2026-02-04"
---

Calculating Tax deductions for employees every month is a time-consuming activity for most businesses, especially for large enterprises. If set up properly, Frappe HR simplifies most of the tax-related calculations by automatically calculating tax deductions while generating Salary Slips. Here's how you can configure Frappe HR to ease your payroll processing -

**Income Tax Exemption**
========================

In many countries, especially in India, regulations allow exempting a part (or all) of some type of spendings by individuals from being added to their annual taxable income. Examples of such spendings could be contributions to charitable institutions, the amount spent on the education of children, specific investments, etc. To avail the exemption from their taxable income, individuals are required to submit proof of such spendings.

Frappe HR allows you to configure Income Tax Slabs and the tax is calculated based on the projected annual earnings of the employee. For this, employees are required to declare the exemption amount they plan to claim at the start of the financial year so that the payroll deductions for tax will be calculated based on the projected annual earnings minus the exemption. Employees can declare this through [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration).

If no declaration is submitted by the employee, the monthly deductions will be calculated without any exemption from the employee's annual earnings. However, if the employee submits a declaration in between the payroll period, the tax exemption will be applied from the next payroll onwards. Any additional tax collected in earlier payrolls will be adjusted in the last payroll or when using *Deduct Tax For Unsubmitted Tax Exemption Proof* in Payroll Entry or Salary Slip.

Also, at the end of the year employees submit the actual proof of the spendings for filing via [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission). In the last payroll of the Payroll Period, Frappe HR checks for proof submissions of employees, and if not found, tax for the exempted income will be added to the standard deduction component.

### **Employee Tax Exemption Category**

Exemptions from taxable salary are usually restricted to spendings on particular categories decided by government or regulatory agencies. Frappe HR allows you to configure various categories which are allowed to be exempted. Examples of this could be, for India, 80G, 80C, B0CC, etc.

You can configure Employee Tax Exemption Category by going to, > Human resources > Payroll Setup > Employee Tax Exemption Category > New Employee Tax Exemption Category

![Employee Tax Exemption Category](https://frappehr.com/files/employee-tax-exemption-category.png)  


### **Employee Tax Exemption Sub Category**

Under each category, there could be many heads for which the exemptions are allowed. For example, in India, subcategories under 80C could be Life Insurance Premium

You can configure Employee Tax Exemption Sub Category by going to, > Human resources > Payroll Setup > Employee Tax Exemption Sub Category > New Employee Tax Sub Exemption Category

![Employee Tax Exemption Sub Category](https://frappehr.com/files/employee-tax-exemption-subcategory.png)  


### **HRA Exemption - Regional, India**

For the fiscal year 2018-19, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:  *The actual amount allotted by the employer as the HRA.*  Actual rent paid less 10% of the basic salary. * 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

As part of the Employee Tax Exemption Declaration, employees shall also fill out the HRA Exemption. Frappe HR will calculate the exemption eligible for HRA and exempt it while calculating the taxable earnings.

> Note: Basic and HRA salary component shall be configured in Company for HRA exemption to work

### **Options in Payroll Entry and Salary Slip**

Frappe HR simplifies payroll processing by automatically processing payroll in bulk via [Payroll Entry](https://docs.frappe.io/hr/payroll-entry).

* Deduct Tax For Unclaimed Employee Benefits: Flexible benefits (Salary Components which are *Is Flexible Benefit*) are not included in the taxable income of the employee. However, the amount received for these components will be included in the taxable earnings of the employee if she fails to submit [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim) while calculating tax in the last payroll of the Payroll Period.

If you wish to collect tax for benefits before the last payroll, check this option and Frappe HR will recalculate the tax and add the tax for all untaxed benefits while generating the Salary Slip.

* Deduct Tax For Unsubmitted Tax Exemption Proof: This option allows you to deduct taxes for the earnings which were exempted in previous payrolls as declared in [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration) but the Employee has not submitted sufficient proof via [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission). It is to be noted that if this option is checked Frappe HR does not consider the Employee Tax Exemption Declaration by employees and will only take into account *Employee Tax Exemption Proof Submission* instead while calculating exemption from employees' annual earnings.

> Note: If required, you can still process payroll for employees individually, by manually creating a new Salary Slip and both these options are made available in the Salary Slip

**Income Tax Slab**
===================

[Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab) helps you define Tax slabs applicable for the period, making it easier to manage changing laws. You can add multiple tax slabs for the payroll period depending on the tax regulations. Note that you can use fields in Employee document in the *Condition* field to apply tax slabs based on attributes of employees.

**Salary Component**
====================

To enable automatic tax deduction based on Tax slabs configured in Income Tax Slab, you have to configure a Salary Component of type *Deduction* with *Variable Based On Taxable Salary* option enabled. This checkbox enables auto calculation of Income Tax considering the tax slabs and declaration submitted by an employee. The tax will be calculated annually on the remaining taxable salary and equally divide it in 12 months.

>**Important Note:** If you configure condition and formula for this Deduction component, the condition and formula will be considered for calculating the Salary Component and the Tax Slabs configured in Income Tax Slab will be ignored. However, you can still use *Deduct Tax For Unsubmitted Tax Exemption Proof* option in Payroll Entry / Salary Slip to deduct taxes based on the Tax Slabs configured in Income Tax Slab, exempting [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission) which will give precedence to the Tax Slab based tax deduction. This is particularly helpful if you need to deduct a fixed amount as a deduction in each payroll rather than Frappe HR automatically calculating the deductions based on the projected annual salary of the employee after exemption as declared by the employee via [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration). At the end of the fiscal year, you can still use *Deduct Tax For Unsubmitted Tax Exemption Proof* to deduct the remaining tax liability of the employee for the whole period.

  

<!-- page: frappe-hr/hr__shift-assignment-tool.md -->
---
title: "Shift Assignment Tool"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-assignment-tool"
updated: "2026-02-04"
---

The Shift Assignment Tool allows you to assign shifts or process shift requests in bulk.


> **Home > Human Resources > Shift Management > Shift Assignment Tool**
> 
> 

**1. Prerequisites**
--------------------

Before using the Shift Assignment Tool, it is advisable to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Shift Type](https://docs.frappe.io/hr/shift-type)
* [Shift Request](https://docs.frappe.io/hr/shift-request)

**2. How to use the Shift Assignment Tool**
-------------------------------------------

### **2.1 Assigning Shifts**

1. Set Action as 'Assign Shift' and select a Company if it hasn't been appropriately selected already.
2. Select the Shift Type that you wish to assign, along with the dates on which you wish to assign it. This will cause all employees without overlapping active Shift Assignments to be loaded in the Select Employees table below.
3. You can also assign inactive shifts by setting Status as 'Inactive'. Pre-existing overlapping shifts will be ignored in this case.
4. Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
5. Select suitable employees from the Select Employees table.
6. If everything looks good, click on the Assign Shift button at the top.

![](https://frappehr.com/files/dCNR1ua.png)  

As a result, Shift Assignments will be created for the selected employees.

### **2.2 Assigning Shift Schedules**

1. Set Action as 'Assign Shift Schedule' and select a Company if it hasn't been appropriately selected already.
2. Select the Shift Schedule that you wish to assign, along with the dates between which you want to create shift assignments. This will cause all employees without overlapping enabled Shift Schedule Assignments to be loaded in the Select Employees table below. If you set the End Date, the shift schedule assignments created will be disabled. If not, the shift schedule assignment will be 'Enabled'. This means that shift assignments will continue to be created automatically via the scheduler.
4. Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
5. Select suitable employees from the Select Employees table.
6. If everything looks good, click on the Assign Shift Schedule button at the top.

![](/files/Screenshot%202024-12-19%20at%2012.26.21%E2%80%AFPM.png)

As a result, Shift Schedule Assignments and their corresponding Shift Assignments will be created for the selected employees.

### **2.3 Processing Shift Requests**

1. Set Action as 'Process Shift Requests' and select a Company if it hasn't been appropriately selected already.
2. You can filter based on Shift Type or Approver. You can also set From Date and To Date to only include shift requests falling between these dates.
3. Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
4. Select suitable shift requests from the Select Shift Requests table.
5. If everything looks good, click on the Process Requests button at the top and select Approve or Reject.

![](https://frappehr.com/files/L4mUQdk.png)  

The selected Shift Requests will then be approved or rejected, and submitted accordingly.

**3. Related Topics**
---------------------

1. [Shift Type](https://docs.frappe.io/hr/shift-type)
2. [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)
3. [Shift Request](https://docs.frappe.io/hr/shift-request)
4. [Shift Schedule](https://docs.frappe.io/hr/shift-schedule)
5. [Roster](https://docs.frappe.io/hr/roster)

  

<!-- page: frappe-hr/hr__shift-assignment.md -->
---
title: "Shift Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-assignment"
updated: "2026-02-04"
---

**1. Prerequisites**
--------------------

To create a Shift Assignment, these need to be created first:

* [Employee](https://docs.frappe.io/hr/employee)
* [Shift Type](https://docs.frappe.io/hr/shift-type)

**2. How to create a Shift Assignment**
---------------------------------------

In some organizations, shifts are assigned to employees, and in some, employees request for a shift. In the latter case, employees can create a [Shift Request](https://docs.frappe.io/hr/shift-request). Once the Shift Request is Approved and submitted it automatically creates a Shift Assignments for an Employee.

To directly create a Shift Assignment, go to:


> **Home > Human Resources > Shift Management > Shift Assignment**
> 
> 

* Click on New
* Select the Employee
* Select the Shift Type
* Set the Start Date. If you want to assign this shift for a specific period, set an End Date.
* Save and Submit.
* You can set the Assignment as Inactive after submission too.

![Shift Assignment](https://frappehr.com/files/shift-assignment0b8bdd.png)  


You can also switch to a calendar view to see shift schedules of multiple employees

![Shift Assignment Calendar](https://frappehr.com/files/shift-assignment374dda.png)  



> **Note: The Assignment for active shift-type will be for a fixed period if there is an End Date otherwise, it will be treated as an ongoing shift with no End Date. Users can update the End Date and status even after submitting the document.**
> 
> 

**3. Features**
---------------

### **3.1 Allow Multiple Shift Assignments for Same Date**

Multiple Shift Assignments on the same date for an employee can be enabled or disabled under the [HR Settings](https://docs.frappe.io/hr/hr-settings#3-1-allow-multiple-shift-assignments-for-same-date).

<!-- page: frappe-hr/hr__shift-location.md -->
---
title: "Shift Location"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-location"
updated: "2026-02-04"
---

Shift Location is used to map locations to Shift Assignments. It can also be used to implement geofencing by ensuring that the employee can only checkin within a certain radius of the location.

### **1. How to create a Shift Location**

To create a new Shift Location, go to: Human Resources > Shift & Attendance > Shift Location

1. Go to the Shift Location list and click on Add Shift Location.
2. Set the Location Name.
3. If you wish to implement geofencing, you will first have to enable **Allow Geolocation Tracking** under HR Settings.
4. You can now set the Checkin Radius, along with the Latitude and Logitude, or click on the Fetch Geolocation button to do so automatically.
5. Save.

![](/files/348245952-f1ca828c-0007-400a-9ad9-58234ffddbad.png)

### **2. Geofencing**

To implement geofencing, you will first have to assign a shift to an employee with the desired Shift Location. While checking in, if the employee is not within the Checkin Radius of the Shift Location, they will be faced with an error that will disallow them from doing so.


![](/files/348247335-226408a2-7a21-45ae-a168-4337d20c59cc.png)

<!-- page: frappe-hr/hr__shift-management.md -->
---
title: "Shift Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-management"
updated: "2026-02-04"
---

The Shift Management module in Frappe HR helps you efficiently manage shifts for your employees.

Using this module you can:

1. [Set up a Shift Type](https://docs.frappe.io/hr/shift-type).
2. [Create Shift Requests](https://docs.frappe.io/hr/shift-request).
3. [View and Manage Shift Assignments](https://docs.frappe.io/hr/shift-assignment).
4. [Setup Attendance Device ID field in Employee master](https://docs.frappe.io/hr/auto-attendance#3-setup-attendance-device-id-field-in-employee).
5. [Create Employee Checkins](https://docs.frappe.io/hr/employee-checkin).
6. [The system then processes auto attendance if it is enabled](https://docs.frappe.io/hr/auto-attendance).

  

<!-- page: frappe-hr/hr__shift-request.md -->
---
title: "Shift Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-request"
updated: "2026-02-04"
---

Shift Request is used by an employee to request for a particular Shift Type.

### **1. Prerequisites**

To create a Shift Request, these need to be created first:

* [Employee](https://docs.frappe.io/hr/employee)
* [Shift Type](https://docs.frappe.io/hr/shift-type)

### **2. How to create a Shift Request**

To create a new Shift Request go to: > Human Resources > Shift Management > Shift Request

1. Go to Shift Request List, Click on New.
2. Select Employee and Shift Type.
3. Set the Shift duration using From Date and To Date.
4. Select the Approver. If the selected approver does not have access to the Shift Request document, it is shared with the approver with "submit" permission.
5. Save.
6. Once the Shift Request is Approved and submitted, it creates a [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)

![Shift Request](https://frappehr.com/files/shift-requestae7f8e.png)

### **3. Setting Shift Request Approver**

A Shift Request Approver is a user who can approve a Shift Request of an Employee. Shift Request Approver can be set at two levels:

* **Department Level:** Shift Request Approvers for each department can be configured in the [Department](https://docs.frappe.io/hr/department) master. Multiple Shift Request Approver can be set in a Department.

![Shift Request Approvers](https://frappehr.com/files/department-shift-request-approvers.png)  


When an Employee belonging to a particular department request for Shift Type, the Shift Request Approver set in that Employee's department master will be considered as his Shift Type Approvers.
* **Employee Level:** Shift Request Approver can also be set in the employee master.

![Shift Request Approvers](https://frappehr.com/files/employee-shift-request-approver.png)

If Shift Request Approver are set at both employee and department level, the employee level Shift Request Approver will be considered as the default Leave Approver in this case.

  

<!-- page: frappe-hr/hr__shift-schedule-assignment.md -->
---
title: "Shift Schedule Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-schedule-assignment"
updated: "2026-02-04"
---

Shift Schedule Assignment can be used to assign shift schedules to employees and create repeating shift assignments based on it.

**1. Prerequisites**
--------------------

To create a Shift Schedule Assingnment, these need to be created first:

* [Employee](https://docs.frappe.io/hr/employee)
* [Shift Schedule](https://docs.frappe.io/hr/shift-schedule)
* [Shift Location](https://docs.frappe.io/hr/shift-location) (Optional)

**2. How to create a Shift Schedule Assignment**
------------------------------------------------

To directly create a Shift Schedule Assignment, go to:


> **Frappe HR > HR > Shift & Attendance > Shift Schedule Assignment**
> 
> 

* Click on Add Shift Schedule Assignment.
* Select the Employee, Shift Schedule, and Shift Location, if any.
* Set the Shift Status. Shift Assignments will be created of this status.
* Select Enabled if you wish for shifts to continue being created automatically via the scheduler. Deselect this if you wish to stop the same.
* Set Create Shifts After. As the name suggests, shifts will be created after this date. This field will be automatically updated after shift assignments are created via the scheduler.
* Click on Save.

![](/files/Screenshot%202024-12-19%20at%2012.10.45%E2%80%AFPM.png)


**4. Related Topics**
---------------------

1. [Shift Type](https://docs.frappe.io/hr/shift-type)
2. [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)
3. [Shift Assignment Tool](https://docs.frappe.io/hr/shift-assignment-tool)
3. [Roster](https://docs.frappe.io/hr/roster)
