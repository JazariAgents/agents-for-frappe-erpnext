<!-- Frappe documentation: frappe-hr, part 3 of 3. Index: docs/INDEX.md -->

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

<!-- page: frappe-hr/hr__shift-schedule.md -->
---
title: "Shift Schedule"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-schedule"
updated: "2026-02-04"
---

Shift Schedule can be used to create definitions for recurring shift assignments based on selected days and frequency.

**1. Prerequisites**
--------------------

To create a Shift Schedule, this needs to be created first:

* [Shift Type](https://docs.frappe.io/hr/shift-type)

**2. How to create a Shift Schedule**
------------------------------------------------

To directly create a Shift Schedule, go to:


> **Frappe HR > HR > Shift & Attendance > Shift Schedule**
> 
> 

* Click on Add Shift Schedule.
* Enter the Name.
* Select the Shift Type.
* Select the Frequency.
* Select the Repeat On Days.
* Click on Save, and then Submit.

![](/files/Screenshot%202024-12-19%20at%2011.37.49%E2%80%AFAM.png)

**3. Assigning Shift Schedule**
--------------------------------------------

To assign a shift schedule to an employee, and to create shift assignments based on it, use [Shift Schedule Assignment](https://docs.frappe.io/hr/shift-schedule-assignment). You can also assign shift schedules in bulk using the [Shift Assignment Tool](https://docs.frappe.io/hr/shift-assignment-tool).

**4. Related Topics**
---------------------

1. [Shift Type](https://docs.frappe.io/hr/shift-type)
2. [Shift Assignment](https://docs.frappe.io/hr/shift-assignment)
3. [Roster](https://docs.frappe.io/hr/roster)

<!-- page: frappe-hr/hr__shift-type.md -->
---
title: "Shift Type                                          "
space: "Frappe HR"
url: "https://docs.frappe.io/hr/shift-type"
updated: "2026-02-04"
---

The Shift Type document allows you to define the different types of Shifts in your Organization and set up auto attendance for the shift. Auto attendance marks attendance based on [Employee Checkin](https://docs.frappe.io/hr/employee-checkin) records for employees assigned to a shift.

To access Shift Type, go to:

> **Home > Human Resources > Shift Management > Shift Type**

1. Click on New.
2. Enter the Shift Name, Start Time and End Time
3. Save

![Shift Type](https://frappehr.com/files/new-shift-type.png)

In addition to defining the different shifts in your organization, the Shift Type document also has settings for auto attendance. Auto attendance marks the attendance for the employees assigned to this shift based on records in the 'Employee Checkin' Document. Auto Attendance for all shift type records is attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Attendance' button in the shift type document.

![auto attendance settings](https://frappehr.com/files/auto-attendance-settings.png)

### **1. Basic Set Up**

1. **Start Time**: The time of the day when this shift starts. The time is to be entered in a 24Hrs format.
2. **End Time**: The time of the day when this shift ends. The time is to be entered in a 24Hrs format.
3. **Holiday List**: The applicable holidays for this shift can be selected here. If left blank, the default holiday list from the employee master or the company document is taken into account. Attendance is not marked via the scheduler if it's a holiday.
4. **Enable Auto Attendance**: You can use this option to enable marking attendance for the employees assigned to this shift based on their [Employee Checkin](https://docs.frappe.io/hr/employee_checkin) records.

> **Note: For cases where the 'End Time' is less than 'Start Time', the shift is assumed to be a night shift that starts on one calendar date and ends on the next calendar date.**

### **2. Auto Attendance Settings**

You can use the following settings to configure the Auto Attendance as per your requirements:

- **Determine Check-in and Check-out**: This setting determines how your check-in logs should be interpreted by the auto attendance system.
  1. **Alternating entries as IN and OUT during the same shift**: The first entry is taken as IN followed by the next entry as OUT and the following entry as IN and so on. Employee Check-in may not always have an IN/OUT log type. Not all biometric devices return Log Type for every log. For such scenarios you can use this option.
  2. **Strictly based on Log Type in Employee Checkin**: The check-in is determined as IN or OUT strictly based on the 'Log Type' in the Employee Checkin record. This should be used when the logs that are being recorded in Frappe HR have the exact log type.
- **Working Hours Calculation Based On**: Working hours can be calculated either by including the breaks in between the shift or by excluding the breaks. This can be configured using the following options:
  1. **First Check-in and Last Check-out**:
    - Use this option when you want to include breaks or all out/in entries in your working hours.
    - Selecting this option calculates the working hours by considering the first IN and last OUT Employee Checkin during the shift. The time difference between the two is considered as the actual working hours.
    - In case the IN/OUT is determined by alternating entries then the first Employee Checkin is considered as IN and the last Employee Checkin is considered as OUT for the purpose of calculating working hours.
  2. **Every Valid Check-in and Check-out**:
    - Selecting this option excludes the time during which the Employee is checked out.
    - i.e. Only the time during which the employee is checked in is calculated as working hours.
- **Begin check-in before shift start time (in minutes)**: Often employees would check-in a few minutes before the shift start time. To consider these check-ins as part of the shift during the calculation of working hours and marking attendance, you can set up this value accordingly.
- **Allow check-out after shift end time (in minutes)**: Often employees would check-out after the shift end time. To consider these check-outs as part of the shift during the calculation of attendance, you can set up this value accordingly.
- **Mark Auto Attendance on Holidays**: If enabled, auto attendance will be marked on holidays if Employee Checkins exist on that date. By default, auto attendance is skipped on holidays.
- **Working Hours Threshold for Half Day**: If the actual number of working hours is less than the given value in this field then the employee attendance is marked as 'Half Day'. If you never want to mark Half Day based on working hours, you should set this value to zero.
- **Working Hours Threshold for Absent**: If the actual number of working hours is less than the given value in this field then the employee attendance is marked as 'Absent'. If you never want to mark Absent based on working hours, you should set this value to zero.

> Note: This only applies for cases when at least one checkin is present to process attendance. In case of absense of any checkin log, attendance will still be marked as Absent.

- **Process Attendance After**: The date from which 'Auto Attendance' should start marking attendance. You should set it to a date after which you have Employee Checkin records for this shift.
- **Last Sync of Checkin**: This is the timestamp up to which Employee Checkin records have been synced. This field has to be updated by the script/person(in case of manual entry) making the Employee Checkin Records. If your logs are automatically pushed to Frappe HR using the sync tool, this timestamp will automatically be updated for you. You should set this to a date and time up to which the Employee Checkin has been synced.
- **Automatically update Last Sync of Checkin**: In case of a single biometric device, or check-ins through the mobile app, you can enable this to let the system take care of auto updating your last sync of checkin so that no scripting or manually updating this timestamp is required.

### **3. Late Entry & Early Exit Settings for Auto Attendance**

- **Enable Late Entry Marking**: Selecting this option marks those Attendance records with Late Entry wherein the employee's In Time exceeds the permissible In Time.
- **Late Entry Grace Period**: Adds additional grace period in minutes to the Shift Start Time after which entries are marked as late.
- **Enable Early Exit Marking**: Selecting this option marks those Attendance records with Early Exit wherein the employee's Out Time falls short of the permissible Out Time.
- **Early Exit Grace Period**: Adds additional grace period in minutes to the Shift End Time before which exits are marked as early.

<!-- page: frappe-hr/hr__staffing-plan.md -->
---
title: "Staffing Plan"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/staffing-plan"
updated: "2026-02-04"
---

**Staffing Plan helps you to plan manpower requirements for your Company.**

Frappe HR allows you to do this at a company level helping you efficiently plan and budget new hirings for a period. Job Openings can only be created as per the number of vacancies and budget as per the active Staffing Plan.

To access Staffing, go to:

> Home > Human Resources > Recruitment > Staffing Plan

**1. Prerequisites**
--------------------

Before creating a Staffing Plan, it is necessary you create the following:

* [Department](https://docs.frappe.io/hr/department)
* [Designation](https://docs.frappe.io/hr/designation)

**2. How to create a Staffing Plan**
------------------------------------

1. Go to Staffing Plan list, click on New.
2. Enter the Name, From and To Date and select the Department for which you want to create the Staffing Plan.
3. Enter the Staffing Plan Details such as Designation, Vacancies, Estimated Cost Per Position, Total Estimated Cost and Number of Positions.
4. Save and Submit.

![Staffing Plan](https://frappehr.com/files/staffing-plan.png)

**3. Features**
---------------

Some of the additional features in the Staffing Plan doctype are explained below:

* **Designation:** The designations for which the Staffing Plan is created.
* **Number of Positions:** The number of positions you plan to recruit for between the From and To Dates of the Staffing Plan.
* **Current Count:** This is the number of Employees already hired against the particular Designation.
* **Vacancies:** The number of vacancies based on the Number of Positions you wish to recruit and the current Employee count.
* **Estimated Cost Per Position:** You can specify the cost to company per position so that hiring officials can stick to the budget.

![Staffing Plan Detail](https://frappehr.com/files/staffing-plan-detail.png)
* **Total Estimated Budget:** Once you enter the recruitment plan for all the designations, Staffing Plan will draw up the total estimated budget as per the plan.

**4. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Job Applicant](https://docs.frappe.io/hr/job-applicant)
3. [Job Offer](https://docs.frappe.io/hr/job-offer)

  

<!-- page: frappe-hr/hr__training-event.md -->
---
title: "Training Event"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/training-event"
updated: "2026-02-04"
---

**Training Event allows you to schedule seminars, workshops, conferences, etc. under a Training Program.**

You can also invite your employees to attend the event using this feature.

To access Training Event, go to:

> Home > Human Resources > Training > Training Event

**1. Prerequisites**
--------------------

Before creating a Training Event, it is advisable you create the following documents:

* [Training Program](https://docs.frappe.io/hr/training-program)
* [Employee](https://docs.frappe.io/hr/employee)

**2. How to create a Training Event**
-------------------------------------

1. Go to the Training Event list, click on New.
2. Enter the Event Name.
3. Select the Event Type.
4. Select Event Level (Beginner, Intermediate, Expert).
5. Enter the Trainer Name, Email and Contact Number.
6. Select the Event [Course](https://docs.erpnext.com/docs/v143/user/manual/en/education/course). Enter the Start Time, End Time and Location of the Training Event.
7. Additionally, you can also write a short description of the Event in the Description box.
8. Save and Submit.

![Employee](https://frappehr.com/files/training-event.png)

> **Note:** Check the 'Has Certificate' checkbox if the Training Event is a certified course.

**3. Features**
---------------

### **3.1 Inviting Employees for the Event**

You can invite your employees to attend the Training Event. You can do so by selecting the employees to be invited in the Employees table.

By default the status of the employee will be 'Open'.

![Employee](https://frappehr.com/files/training-event-employee.png)  


When you submit the Training Event, a notification will be sent to the employee notifying that the Training has been scheduled. This is sent via Email Alert "Training Scheduled". You can modify this Email Alert to customize the message.

**4. Related Topics**
---------------------

1. [Training Result](https://docs.frappe.io/hr/training-result)
2. [Training Feedback](https://docs.frappe.io/hr/training-feedback)
3. [Course](https://docs.erpnext.com/docs/v143/user/manual/en/education/course)

  

<!-- page: frappe-hr/hr__training-feedback.md -->
---
title: "Training Feedback"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/training-feedback"
updated: "2026-02-04"
---

**Once the Training is complete, employees can share their feedback via Training Feedback.**

To access Training Feedback, go to: > Human Resources > Training > Training Feedback

**1. Prerequisites**
--------------------

Before creating a Training Event, it is advisable you create the following documents:

* [Training Program](https://docs.frappe.io/hr/training-program)
* [Training Event](https://docs.frappe.io/hr/training-event)
* [Employee](https://docs.frappe.io/hr/employee)

**2. How to create a Training Feedback**
----------------------------------------

1. Go to the Training Feedback list, click on New.
2. Select the Employee.
3. Select the Training Event. Based on that, the corresponding Event Name, Course and Trainer Name will get fetched.
4. Enter the feedback in the Feedback box.
5. Save and Submit.

![Employee](https://frappehr.com/files/training-feedback.png)

> Note: You can also access Training Feedback directly through the Training Event dashboard.

**3. Related Topics**
---------------------

1. [Training Result](https://docs.frappe.io/hr/training-result)

last

  

<!-- page: frappe-hr/hr__training-program.md -->
---
title: "Training Program"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/training-program"
updated: "2026-02-04"
---

**Training Program defines programs designed for training employees or other individuals in specific skills.**

In Frappe HR, you can create a Training Program and schedule [Training Events](https://docs.frappe.io/hr/training-event) under it.

To access Training Program, go to:

> Home > Human Resources > Training > Training Program

**1. How to create a Training Program**
---------------------------------------

1. Go to Training Program list, click on New.
2. Enter the Training Program name.
3. Enter the Trainer Name, Trainer Email and Contact Number.
4. Select the Supplier n(optional) in case an outside vendor/expert was called to conduct the training.
5. Additionally, you can also write a short description of the Training Program in the Description box (optional).

![Training Program](https://frappehr.com/files/training-program.png)

> **Note:** By default, the Status of the Training Program is 'Scheduled'. However, you can change the status to 'Completed' or 'Cancelled' as per the requirement.

Once the Training Program is saved, you can create Training Events under the same.

**2. Related Topics**
---------------------

1. [Training Event](https://docs.frappe.io/hr/training-event)
2. [Training Result](https://docs.frappe.io/hr/training-result)
3. [Training Feedback](https://docs.frappe.io/hr/training-feedback)

  

<!-- page: frappe-hr/hr__training-result.md -->
---
title: "Training Result"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/training-result"
updated: "2026-02-04"
---

**After completion of the training event, employee-wise training results can be stored based on the evaluation done by the trainer.**

Frappe HR allows you to create training results and share it with the employees with the Training Result doctype.

To access Training Result, go to:

> Home > Human Resources > Training > Training Result

**1. Prerequisites**
--------------------

Before creating a Training Result, it is advisable you create the following documents:

* [Training Program](https://docs.frappe.io/hr/training-program)
* [Training Event](https://docs.frappe.io/hr/training-event)
* [Employee](https://docs.frappe.io/hr/employee)

**2. How to create a Training Result**
--------------------------------------

1. Go to the Training Result list, click on New.
2. Select Training Event.
3. Enter the Hours, Grade and Comments against the Employee Name.
4. Save and Submit

![Employee](https://frappehr.com/files/training-result.png)

When the Training Result is submitted, all the employees will receive an email notifying them that they must share their feedback via [Training Feedback](https://docs.frappe.io/hr/training-feedback). This is also managed via an Email Alert, so you can customize this alert too.

> **Note:** You can also access Training Result directly from the Training Event dashboard.

**3. Related Topics**
---------------------

1. [Training Feedback](https://docs.frappe.io/hr/training-feedback)

  

<!-- page: frappe-hr/hr__travel-request.md -->
---
title: "Travel Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/travel-request"
updated: "2026-02-04"
---

Employees can request funds for official travel using Travel Request. To create a new Travel Request, go to


> **Human Resource > Travel and Expense Claim > Travel Request > New Travel Request**
> 
> 

![](https://frappehr.com/files/VW8kpGD.png)  


You can also mention the Travel Itinerary as well as the costs involved for the trip. Employees can also check `Travel Advance Required` if they wish to receive any upfront payment form the company.

![Travel Request Itinerary](https://frappehr.com/files/travel-request-itinerary.png)  


  

<!-- page: frappe-hr/hr__upload-attendance.md -->
---
title: "Upload Attendance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/upload-attendance"
updated: "2026-02-28"
---


**This tool helps you to upload bulk attendance from a csv file.**

To upload the attendance go to:

> Home > Human Resources > Attendance > Upload Attendance


## 1. Prerequisites

Before uploading bulk Attendance record, it is advised that you create the following first:

* [Employee](/hr/employee)


## 2. How to upload attendance in bulk

1. Enter Attendance From Date and Attendance To Date.
1. Click on 'Get Template' button. It will download a csv file with the Employee Details as shown.

 ![Attendance Template](/files/upload-attendance1.png)

1. Enter the Status (Present / Absent) of the Employee for the selected dates.
1. Save the file.
1. Upload the saved file.


 ![Attendance upload](/files/upload-attendance.png)


Once the bulk attendance is uploaded, respective attendance records will be created.


## 3. Related Topics


1. [Employee Attendance Tool](/hr/employee-attendance-tool)
1. [Shift Management](/hr/shift-management)
1. [Auto Attendance](/hr/auto-attendance)
1. [Attendance Request](/hr/attendance-request)
1. [Attendance](/hr/attendance)

<!-- page: frappe-hr/hr__user-permission-based-on-hierarchy.md -->
---
title: "User Permission based on Hierarchy"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/user-permission-based-on-hierarchy"
updated: "2026-02-04"
---

**Question:**

How to configure User Permissions, so that an Employee can view his Expense Claims, and also of ones who report to him/her?

**Answer:**

In the Employee master, for each Employee, you can define who does he/she reports to. Based on the Reports To defined, the Employee hierarchy is built as well.

![](https://docs.erpnext.com/files/14Khhti.png)  


**Employee Hierarchy**

Also, one a User is linked with the Employee, it creates a User Permission as follows. As per this User Permission, Employee will be allowed to review his/her own document created in the HR module + the document which are created for Employees reporting to hm/her.

![](https://docs.erpnext.com/files/wRl6sKW.png)  


As per this configuration, when an Expense Claim is being created by the User reporting to Kenneth, it will also be accessible to Kenneth as well.

![](https://docs.erpnext.com/files/4L4Co0O.png)  


Can you please ensure that seniors Employee ID is updated as Reports To in the Employee's who report to him/er? After that, manager should be able to view the Expense Claims and other documents (like Leave Application, Appraisal etc.) made for his/her sub-ordinates.

<!-- page: frappe-hr/hr__using-auto-attendance.md -->
---
title: "Using Auto Attendance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/using-auto-attendance"
updated: "2026-02-04"
---

Frappe HR allows us to Mark Attendance automatically depending upon the Employee Checkin records.

A. Create or import Employee Checkin:

![](https://docs.erpnext.com/files/zTTsnRA.png) 


1. Set the time carefully for log type **IN** and **OUT.**
2. For Log Type **IN** time should be greater than **Shift Type Start Time - Begin check-in before shift time**
3. For Log Type **OUT** time should be less Than **Shift Type End Time + Allow check-out after shift end time.**
4. Then only Shift would be mapped properly and your Checkin is valid.

B. Check your shift type:

![](https://docs.erpnext.com/files/ant5ZYn.png)  


1. Set **Process Attendance After** (Attendance will be marked Only after this date)
2. Set **Last Sync of Checkins** (It is the time before which all the checkin records will be considered. Note: If it is less than shift end Time then it will not consider that day's checkin because it means that shift is not over yet)

C. Click on Mark Auto Attendance to check whether it is working

Note: The scheduler will run the process to mark attendance automatically every hour. But after uploading or creating check-ins you need to check your **Process Attendance After and Last Sync of Checkin** in **Shift Type**.

<!-- page: frappe-hr/hr__vehicle-log.md -->
---
title: "Vehicle Log"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/vehicle-log"
updated: "2026-05-29"
---

**Vehicle Log is used to enter Odometer readings, Fuel Expenses and Service Expense details.**

To access Vehicle Log, go to:

> Human Resources > Fleet Management > Vehicle Log

## **1. Prerequisites**

Before creating a Vehicle Log, it is necessary that you create the following documents:

- [Vehicle](https://docs.frappe.io/hr/vehicle)

## **2. How to create a Vehicle Log**

1. Go to Vehicle Log list, click on New.
2. Select License Plate and Employee.
3. Enter Odometer Reading information such as Date and Odometer (reading).
4. Enter Refueling Details [optional] such as Fuel Qty, Fuel Price, Supplier and Invoice Ref.

![](/files/vehicle-log1ddd1a8.png)

5. Additionally, Vehicle Service Details can also be added as shown (optional).

![](/files/image18b180.png)

6. Save. Once the information is saved, the Model and Make values will be automatically fetched.

## **3. Features**

Fleet Management in Frappe HR allows you to automatically create an [Expense Claim](https://docs.frappe.io/hr/expense-claim) against your Vehicle Expenses.

### **3.1 Make Expense Claim against Vehicle Expenses**

Click on Create Expense Claim button. This button appears only in case of Submitted Vehicle Logs.

![](/files/vehicle-log-expense-claim-buttonca7bfe.png)



When you click on 'Make Expense Claim',

1. The Date, Employee, Expense total are fetched over to the created Expense Claim.
2. The sum of Fuel Expenses and Service Expenses is calculated and fetched over to Expense Claim Amount.
3. Employee can submit the Expense Claim for further processing.

![](/files/vehicle-log-expense-claim47633b.png)

## **4. Related Topics**

1. [Expense Claim](https://docs.frappe.io/hr/expense-claim)

<!-- page: frappe-hr/hr__vehicle.md -->
---
title: "Vehicle"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/vehicle"
updated: "2026-02-04"
---

**The Vehicle document allows you to define the different types of Vehicles in your Organization. It acts as the Vehicle Master for Fleet Management.**

To access the Vehicle master, go to:

> Human Resources > Fleet Management > Vehicle

**1. How to create a Vehicle document**
---------------------------------------

1. Go to Vehicle list, click on New.
2. Enter information such as License Plate, Make (Brand) and Model.
3. Enter Odometer value (Last).
4. Enter other additional details such as Fuel Type ad Fuel UOM.
5. Save.

![Vehicle](https://frappehr.com/files/vehicle-mandatory.png)

**2. Features**
---------------

Apart from the aforementioned mandatory features, some additional features that can be captured in the Vehicle master are as follows:

### **2.1 Additional Vehicle Details**

Additional Vehicle details such as Chassis No., Acquisition Date, Vehicle Value (Amount), Location, Employee managing the Vehicle and Insurance details can be captured in the Vehicle master.

![Vehicle](https://frappehr.com/files/vehicle1.png)  


### **2.2 Vehicle Attributes**

Additionally, Vehicle attributes like Color, Wheels, Door, Last Carbon Check, Fuel Type and UOM can be saved in the Vehicle master.

![Vehicle](https://frappehr.com/files/vehicle2.png)  


**3. Related Topics**
---------------------

1. [Vehicle Log](https://docs.frappe.io/hr/vehicle-log)

  

<!-- page: frappe-hr/hr__videos.md -->
---
title: "Videos"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/videos"
updated: "2026-02-04"
---

The Human Resources (HR) module covers the processes related to the HR department of a company. It maintains a complete employee database including contact information,
salary details, attendance, performance evaluation, leaves, and appraisal records.

## Talks &amp; Webinars

### Introducing Frappe HR



<iframe allowfullscreen="" frameborder="0" height="371" src="https://www.youtube.com/embed/WNvqA9QsVmY?start=231" width="660">
</iframe>




**Duration: 14:24**


Introducing Frappe HR at the ERPNext conference 2022




### Simplify your HR and Payroll operations with Frappe HR



<iframe allowfullscreen="" frameborder="0" height="371" src="https://www.youtube.com/embed/-7PhoqDaHjQ" width="660">
</iframe>




**Duration: 43:27**


Discover the latest updates on Frappe HR - the ultimate open-source solution for seamless HR and payroll management




## Video Tutorial
1. [Employees](https://docs.erpnext.com/docs/v13/user/videos/learn/employee)
1. [Leave Management](https://docs.erpnext.com/docs/v13/user/videos/learn/leave-management)
1. [Expense Claims](https://docs.erpnext.com/docs/v13/user/videos/learn/expense-claim)
1. [Employee Advance](https://docs.erpnext.com/docs/v13/user/videos/learn/employee-advance)

<!-- page: frappe-hr/hr__working-days-calculation-in-the-salary-slip.md -->
---
title: "Working Days Calculation in the Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/working-days-calculation-in-the-salary-slip"
updated: "2026-02-04"
---

Working Days are shown in the Salary Slip. Based on your preference, it may include holidays of the month, or it may not. You can define your preference for the Working Days calculation in HR Settings.

`HR > Setup > HR Settings`

If you want to include holidays in the count of Total Working days, then ensure that in the HR Settings, field **Include holidays in Total no. of Working Days** is checked and vice versa.

![Role Desk Permission](https://frappehr.com/files/hr-working-days.png)  


To learn how to define holidays for your company, check [Holiday List](https://docs.frappe.io/hr/holiday-list) feature in the HR module.

  
