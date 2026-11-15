<!-- Frappe documentation: frappe-hr, part 3 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__employee-tax-exemption-declaration.md -->
---
title: "Employee Tax Exemption Declaration"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-tax-exemption-declaration"
updated: "2026-02-04"
---

**Tax exemption is the monetary exemption of income, property or transactions from taxes that would otherwise be levied on an Employee.**

At the beginning of a Payroll Period, employees can declare the amount of exemption they will be claiming from their taxable salary. Frappe HR allows you to specify tax exemption category/sub-category, tax exemption amount and other related information in the Employee Tax Exemption Declaration form.

To access Employee Tax Exemption Declaration, go to:

> Home > Human resources > Employee Tax and Benefits > Employee Tax Exemption Declaration

**1. Prerequisites**
--------------------

Before creating an Employee Tax Exemption Declaration, it is advisable you create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Employee Tax Exemption Category](https://docs.frappe.io/hr/employee-tax-exemption-declaration#31-employee-tax-exemption-category)
* [Employee Tax Exemption Sub Category](https://docs.frappe.io/hr/employee-tax-exemption-declaration#32-employee-tax-exemption-category)

**2. How to create Employee Tax Exemption Declaration**
-------------------------------------------------------

To create a new Employee Tax Exemption Declaration:

1. Go to: Employee Tax Exemption Declaration > New.
2. Select the Exemption Sub Category and Exemption Category.
3. Enter the Maximum Exemption Amount and Declared Amount.
4. Save and Submit.

![Employee Tax Exemption Declaration](https://frappehr.com/files/employee-tax-exemption-declaration.png)

The Total Exemption Amount will be exempted from annual taxable earnings of the employee while calculating the tax deductions in Payroll.

> **Note:** Employees can only submit one Employee Tax Exemption Declaration for a Payroll Period.

**3. Features**
---------------

### **3.1 Employee Tax Exemption Category**

Exemptions from taxable salary are usually restricted to spendings on particular categories decided by the Government or regulatory agencies. Frappe HR allows you to configure various categories which are allowed to be exempted. Examples of these (for India) could be, 80G, 80C, B0CC etc.

You can configure Employee Tax Exemption Category by going to, **Employee Tax and Benefits > Employee Tax Exemption Category**

![Employee Tax Exemption Category](https://frappehr.com/files/employee-tax-exemption-sub-category1.png)  


### **3.2 Employee Tax Exemption Sub-Category**

Under each category, there could be many heads for which the exemptions are allowed. For example, in India, sub categories under 80C could be Life Insurance Premium

You can configure Employee Tax Exemption Category by going to, **Employee Tax and Benefits > Employee Tax Exemption Sub-Category**

![Employee Tax Exemption Category](https://frappehr.com/files/employee-tax-exemption-category1.png)  


### **3.3 HRA Exemption (Regional - India)**

For the current fiscal year, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:

* The actual amount allotted by the employer as the HRA.
* Actual rent paid less 10% of the basic salary.
* 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

As part of the Employee Tax Exemption Declaration, employees can also fill out the HRA Exemption. Frappe HR calculates the exemption eligible for HRA and exempts it while calculating the taxable earnings.

Enter the Monthly House Rent and check the 'Rented in Metro City' checkbox if applicable and submit the form. The Annual and Monthly HRA Exemption will be automatically calculated.

Once the declaration is submitted, you can submit the proof of your tax exemption by clicking on the *Submit Proof* button.

![Employee Tax Exemption Declaration](https://frappehr.com/files/hra-exemption.png)  


> Note: HRA component needs to be configured in Company master under HRA Settings sections for the HRA exemption to work.

**4. Related Topics**
---------------------

1. [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)
2. [Employee Benefit Application](https://docs.frappe.io/hr/employee-benefit-application)
3. [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim)

  

<!-- page: frappe-hr/hr__employee-tax-exemption-proof-submission.md -->
---
title: "Employee Tax Exemption Proof Submission"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-tax-exemption-proof-submission"
updated: "2026-02-04"
---

**Employees are required to submit proofs for all the spendings they claim tax exemption for. This can be done through the Employee Tax Exemption Proof Submission document**

This is usually done at the end of a Payroll Period, but employees can submit any number of proofs unlike Employee Tax Exemption Declaration.

> **Note:** Create an Employee Tax Exemption Declaration before creating an Employee Tax Exemption Proof Submission

To access Employee Tax Exemption Proof Submission, go to:

> Home > Human resources > Employee Tax Exemption Proof Submission

**1. How to create an Employee Tax Exemption Proof Submission**
---------------------------------------------------------------

The details are already fetched if you click on 'Submit Proof' from [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration). However, if you want to create an 'Employee Tax Exemption Proof Submission' manually, follow these steps.

1. Go to the Employee Tax Exemption Proof Submission list, click on New.
2. Enter the details as needed.
3. Additionally, enter the 'Type of Proof' (documents, receipts, etc.).
4. Attach the proofs in by clicking on the **Attach** button at the bottom.
5. Enter House Rent Payment Amount, Rented From Date and Rented To Date.
6. Save and Submit.

![Employee Tax Exemption Proof Submission](https://frappehr.com/files/employee-tax-exemption-proof-submission.png)

The *Total Exemption Amount* will be exempted from annual taxable earnings of the employee while calculating the tax deductions in the last payroll.

> Note: Even if employees submit exemption proofs anytime during the payroll period, Frappe HR will only consider this in the last payroll of the Payroll Period for adjusting the final taxes based on the proof submitted. If you need to adjust any additional tax collected or consider proof submission of employees anytime before the last payroll, while processing Payroll Entry (or in the Salary Slip of the employee) check the *Deduct Tax For Unsubmitted Tax Exemption Proof* option.

### **Regional - India**

For the current fiscal year, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:

* The actual amount allotted by the employer as the HRA.
* Actual rent paid less 10% of the basic salary.
* 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

As part of the Employee Tax Exemption Proof Submission, employees shall also submit proof for HRA Exemption. Frappe HR will calculate the exemption eligible for HRA and exempt it while calculating the taxable earnings in the last payroll of the Payroll Period.

> Note: HRA component shall be configured in Company for HRA exemption to work

  

<!-- page: frappe-hr/hr__employee-transfer.md -->
---
title: "Employee Transfer"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee-transfer"
updated: "2026-02-04"
---

**Employee Transfer is a form of internal mobility, in which the Employee is shifted from one job to another usually at a different location, department, or unit.**

In Frappe HR, you can record Employee transfers to different Company or Department by using the Employee Transfer document.

To access Employee Transfer go to:

> Human Resource > Employee Lifecycle > Employee Transfer

**1. Prerequisites**
--------------------

* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)

**2. How to create a Employee Transfer**
----------------------------------------

1. Select the Employee.
2. Select the Transfer Date.
3. Select the New Company in case the Employee is transferred to a different company (optional).
4. In the Employee Transfer Details table, select the Property and set the Current and New value.
5. Additionally, 'Create New Employee' checkbox can be checked to create a new Employee ID for the transferred Employee.

> Note: If Create New Employee ID is checked, a new Employee will be created with property changes in Transfer Details table and old Employee will be marked as relieved. Leave allocations for the new Employee has to be manually created from Leave Period.

![Employee Transfer](https://frappehr.com/files/employee-transfer.png)  


> Note: Transfer document can be submitted on or after Transfer Date. Once submitted all the changes added to Transfer Details table will applied to Employee.

**3. Related Topics**
---------------------

1. [Employee Onboarding](https://docs.frappe.io/hr/employee-onboarding)
2. [Employee Separation](https://docs.frappe.io/hr/employee-separation)
3. [Employee Promotion](https://docs.frappe.io/hr/employee-promotion)

  

<!-- page: frappe-hr/hr__employee.md -->
---
title: "Employee"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employee"
updated: "2026-03-31"
---

**An individual who works part-time or full-time under a contract of employment, and has recognized rights and duties of your company is your Employee.**

In Frappe HR, you can manage the Employee master. It captures the demographic, personal, and professional details, joining and leave details, etc. of the Employee.

To access the Employee master, go to:

> **Home > Human Resources > Employee**

![](https://frappehr.com/files/RtArfPD.gif)



## **1. Prerequisites**

Before creating an Employee, it is advised to create the following:

- [Company](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/company-setup#1-how-to-create-a-new-company)

## **2. How to create an Employee**

1. Go to the Employee list, and click on New.
2. Enter the Employee's personal details such as Name, Gender, Date of Birth, and Date of Joining.
3. Save.

As shown below, all the mandatory fields are marked with red asterisks.

![](https://frappehr.com/files/rqUdH4m.png)

### **2.1 Bulk Creation via Data Import**

Multiple Employees can be created at once using the Data Import tool.

1. Go to Data Import or click on Import from the top menu, then select Employee as the DocType.
2. Download the template and fill in the required fields such as Employee Name, Company, and Date of Joining.
3. Ensure that either the **Company Email** or **Preferred Contact Email** field is populated for each Employee if User creation is required.
4. Upload the filled template and start the import.

Upon successful import, Employee records will be created for all valid rows.

Refer to the [Data Import](https://docs.frappe.io/erpnext/data-import) guide to learn more.

## **3. Features**

Apart from the aforementioned mandatory details, some additional details that can be captured in the Employee master are as follows:

### **3.1 Employment Type**

You can set an [Employment Type](https://docs.frappe.io/hr/employment-type) such as Intern, Contract, Full-time, Part-time, Probation, etc. for an Employee.

### **3.2 Create User**

The User ID can be linked to the Employee. User accounts can be created and associated with an Employee in different ways depending on your workflow.

#### **Option 1: During Employee Creation (Automatic)**

While creating a new Employee:

- Enable the **Create User Automatically** checkbox to create a User when saving the Employee.
- The **Create User Permission** checkbox is enabled by default. This ensures that the newly created User has access only to their own Employee record and associated Company.
- Ensure that either the **Company Email** or **Preferred Contact Email** field is populated.

#### **Option 2: For Existing Employees (Via Button)**

If an Employee is created without linking a User ID, a User can be created later from the Employee record:

- Click on the **Create User** button from the top actions menu.
- A dialog will appear with the **Create User Permission** option enabled by default. You can set or update the email in the dialog before creating the User.
- On confirmation, the system will create the User, assign the necessary permissions, and link it to the Employee.

#### **Option 3: Via Data Import**

User accounts can also be created during Employee import by including the required fields in the import template:

- Ensure that either the **Company Email** or **Preferred Contact Email** field is populated.
- Include the **Create User Automatically** column and set the value to `1` for the required rows.
- Include the **Create User Permission** column and set it to `1` to apply default access restrictions.
- Upon successful import, the system will automatically create and link the Users for all applicable Employee records.

Check [Adding Users](https://docs.frappe.io/erpnext/adding-users) to learn how to create users and add permissions.

### **3.3 Joining Details**

The Joining Details of the Employee such as the Offer Date, Confirmation Date, Contract End Date, Notice (Days), and Date of Retirement can be captured.

### **3.4 Department and Grade**

In a company, the Employees are usually grouped on the basis of [Department](https://docs.frappe.io/hr/department), [Grade](https://docs.frappe.io/hr/employee-grade), [Designation](https://docs.frappe.io/hr/designation), and [Branch](https://docs.frappe.io/hr/branch).

In the Department and Grade section, these details of the Employee can be saved. In the 'Reports to' field, the person to whom the Employee has to report his duties to can be captured.

### **3.5 Leave Details**

In Leave Details, you can save the [Leave Policy](https://docs.frappe.io/hr/leave-policy) and [Holiday List](https://docs.frappe.io/hr/holiday-list) details. Leave Policy specifies the type and number of leaves an Employee is entitled to, and Holiday List is a list which contains the dates of holidays and weekly offs.

### **3.6 Salary Details**

Here, the mode of salary payment, i.e. through Bank, Cheque or Cash can be selected.

### **3.7 Contact Details**

Employee's Contact information such as Mobile Number, Current and Permanent Address, Personal and Company Email ID can be captured here. In the Preferred Email ID field, either the the Company Email, Personal Email or User ID of the Employee can be selected depending on the user's preference.

### **3.8 Personal Details**

Personal Details of the Employee such as Family Background details like name and occupation of parent, spouse and children, Passport Details including date and place of issue, Health Details like height, weight, allergies, medical concerns, etc. can be saved.

### **3.9 Educational Qualification**

Here, the Educational Details such as School/University, Qualification, Level and Year of Passing of the Employee can be saved as shown below:

![](https://frappehr.com/files/educational-qualification.png)



Additionally, details such as Class/Percentage and Subjects can also be saved by clicking on the downward arrow in the Education table.

### **3.10 Previous Work Experience**

Just like Educational Qualification, an Employee's Previous Work Experience can also be captured in the External Work History table as shown below:

![Previous Work Experience](https://frappehr.com/files/previous-work-experience.png)



Additionally, details such as Contact of the previous company and Total Experience in years can also be saved in the External Work History table.

### **3.11 Exit**

Exit details of the employee (if any) such as Resignation, Exit Interview and [Leave Encashment](https://docs.frappe.io/hr/leave-encashment) details can be saved. When the status of the Employee is set to 'Left', it is mandatory to fill the Relieving Date.

> **Note: Once the Employee status is set to 'Left', that particular Employee master won't be accessible in further transactions.**

### **3.12 Additional Features**

Some additional features included in the Employee master are as follows:

- Emergency Contact
- Health Insurance
- Personal Bio
- History in the Company

## **3. Related Topics**

1. [Leave Management](https://docs.frappe.io/hr/leaves)
2. [Payroll Management](https://docs.frappe.io/hr/payroll-setup)

<!-- page: frappe-hr/hr__employment-type.md -->
---
title: "Employment Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/employment-type"
updated: "2026-02-04"
---

**You can employ people under a number of categories each having their own wage and leave entitlements. This is called an Employment Type.**

Frappe HR allows you to select an Employment Type from a pre-defined list or even create a new Employment Type based on your requirements.

To access the Employment Type, go to:


> **Home > Human Resources > Employee > Employment Type**
> 
> 

**1. How to create an Employment Type**
---------------------------------------

1. Go to the Employment Type list, click on New.
2. Enter the Name of the Employment Type.
3. Save.

![Employment Type](https://frappehr.com/files/employment-type.png)

The Employment Type can be linked to the [Employee](https://docs.frappe.io/hr/employee) master.

**2. Related Topics**
---------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Employment Type](https://docs.frappe.io/hr/employment-type)
3. [Branch](https://docs.frappe.io/hr/branch)
4. [Department](https://docs.frappe.io/hr/department)
5. [Designation](https://docs.frappe.io/hr/designation)
6. [Employee Grade](https://docs.frappe.io/hr/employee-grade)

<!-- page: frappe-hr/hr__exit-interview.md -->
---
title: "Exit Interview"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/exit-interview"
updated: "2026-02-04"
---

> Introduced in Version 14

**An Exit Interview is a survey interview conducted for an Employee who is leaving the organization.**

In Frappe HR, to access the Exit Interview, go to:

> Human Resources > Employee Exit > Exit Interview

**1. Prerequisites**
--------------------

Before creating an Exit Interview, it is advisable that you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Department](https://docs.frappe.io/hr/department)
* [Designation](https://docs.frappe.io/hr/designation)

Exit Interview is created for an Employee who has resigned or is being terminated. Hence it is mandatory to set the **Relieving Date** for the Employee in the Employee master.

**2. How to create an Exit Interview**
--------------------------------------

1. Go to: Exit Interview > New.
2. Select the Employee. Once the Employee is selected, the corresponding Employee information such as Department, Designation, Reports To, Date of Joining, Relieving Date, etc. will automatically get fetched.
3. The status will be Pending by default.
4. When the Interview is scheduled, set the Date, select the Interviewers, and change status to Scheduled.
5. You can record the Interview Summary during the Interview.
6. Once the Exit Interview is completed, you can change the status to Completed. Final Decision can be recorded on completion (Employee Retained / Exit Confirmed).
7. Submit. On submission, the Exit Interview Date will be updated in the Employee master.

![](https://frappehr.com/files/7RqwdBu.png)  


**3. Features**
---------------

### **3.1 Sending Exit Questionnaire**

During Employee Exits, companies conduct surveys by sending a questionnaire to the Employee to get feedbacks for improvement and reviews. Here is how you can conduct exit surveys:

1. Since exit questionnaires will differ from company to company, you can create your own Questionnaire as a Custom [DocType](https://frappehr.com/docs/v14/user/manual/en/customize-erpnext/doctype). For eg, we have created a sample custom doctype for the same:

  


![](https://frappehr.com/files/VWYkMrj.png)
2. After creating the questionnaire, you can create a [Web Form](https://frappehr.com/docs/v14/user/manual/en/website/web-form) for the same so that these forms can be sent to employees.
3. Link the Web Form in HR Settings. A default notification email template is already provided by Frappe HR which is linked in HR Settings.

  


![](https://frappehr.com/files/HX2hImw.png)
4. In the Exit Interview document, you can see a button **Send Exit Questionnaire**. This will send an email to the Employee with a link to the web form as per the email template set in HR Settings.

![](https://frappehr.com/files/QZLEPfA.png)
5. Once your employee fills up this questionnaire, you can link it to the Exit Interview document.

![](https://frappehr.com/files/DvRVjac.png)
6. If you want to send Exit Questionnaires in bulk to multiple employees, you can select the employees from the Exit Interview list view and click on **Actions > Send Exit Questionnaire**. This will send the exit questionnaire emails and provide you with a summary of the emails sent.

![](https://frappehr.com/files/svg7XbQ.png)

**4. Related Topics**
---------------------

1. [Employee](https://docs.frappe.io/hr/employee-separation)
2. [Employee Separation](https://docs.frappe.io/hr/employee-separation)
3. [Employee Exits Report](https://docs.frappe.io/hr/human-resources-reports#5-employee-exits)

  

<!-- page: frappe-hr/hr__expense-claim.md -->
---
title: "Expense Claim"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/expense-claim"
updated: "2026-02-04"
---

**Expense Claim is made when employees make expenses out of their pocket on behalf of the company.**

For example, if they take a customer out for lunch, they can make a request for reimbursement via the Expense Claim form.

To access an Expense Claim, go to:

> Human Resources > Expense Claims > Expense Claim

**1. Prerequisites**
--------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Department](https://docs.frappe.io/hr/department)
3. [Chart of Accounts](https://docs.erpnext.com/docs/user/manual/en/chart-of-accounts)

**2. How to create a Expense Claim**
------------------------------------

1. Go to: Expense Claim > New.
2. Select the Employee Name in the 'From Employee' field.
3. Select the Expense Approver.
4. Enter the Expense Date, Expense Claim Type and the Amount.
5. Additionally, you can also enter the Expense Taxes and Charges.
6. In Accounting Details, select the Company's Default Payable Account.
7. Save and Submit.

![Expense Claim](https://frappehr.com/files/expense_claim.png)  


Set the Employee ID, date, the list of expenses, and corresponding taxes that are to be claimed and “Submit” the record.

![Expense Claim](https://frappehr.com/files/expense-claim-expenses.png)  


Expense claim workflow

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/5SZHJF--ZFY?rel=0"> </iframe>

### **Approving Expenses**

Approver for the Expense Claim is selected by an Employee himself. Employee can choose from the list of users who are configured as *Expense Approvers* for their [Department](https://docs.frappe.io/hr/department).

When a new Expense Claim is created, if the selected expense approver does not have access to it, the document is shared with the approver with "submit" permission.

After saving Expense Claim, Employee should [Assign document to Approver](https://docs.erpnext.com/docs/v14/user/manual/en/using-erpnext/assignment). On assignment, approving user will also receive email notification. To automate email notification, you can also setup Email Alert

Expense Claim Approver can update the “Sanctioned Amounts” against Claimed Amount of an Employee. If submitting, Approval Status should be submitted to Approved or Rejected. If Approved, then Expense Claim gets submitted. If rejected, then Expense Approver's comments can be added in the Comments section explaining why the claim was approved or rejected.

### **Booking the Expense**

On submission of Expense Claim, system books an expense against the expense account and the employee account ![Expense Claim](https://frappehr.com/files/expense_claim_book.png)  


User can view unpaid expense claim using report "Unclaimed Expense Claims" ![Expense Claim](https://frappehr.com/files/unclaimed_expense_claims.png)  


### **Payment for Expense Claim**

To make payment against the expense claim, user has to click on Create > Payment.

#### **Expense Claim**

![Create Payment](https://frappehr.com/files/expense_claim_create_payment.png)  


#### **Payment Entry**

> Note: This amount should not be clubbed with Salary because the amount will then be taxable to the Employee.

![Expense Claim](https://frappehr.com/files/expense_claim_payment_entry.png)  


Alternatively, a Payment Entry can be made for an employee and all outstanding Expense Claims will be pulled in.

> Accounting > Payment Entry > New Payment Entry

Set the Payment Type to "Pay", the Party Type to Employee, the Party to the employee being paid and the account being paid from. All outstanding expense claims will be pulled in and payments amounts can be allocated to each expense.

### **Linking with Task &amp; Project**

* To Link Expense Claim with Task or Project specify the Task or the Project while making an Expense Claim

![Expense Claim - Project Link](https://frappehr.com/files/project-expense-claim-1.png)  


This will update the Project cost with the Expense claim amounts

![Expense Claim - Project Link](https://frappehr.com/files/project-expense-claim-2.png)  


  

<!-- page: frappe-hr/hr__fleet-management.md -->
---
title: "Fleet Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/fleet-management"
updated: "2026-02-04"
---

Fleet Management section of Human Resources helps your Organization manage their fleet of vehicles and track their expenses.

To use Fleet Management in Frappe HR, you can do the following:

1. Set Up a Vehicle.
2. Enter Vehicle Logs regularly.
3. Make Expense Claims for Vehicle Expenses.
4. View Reports for Vehicle Expenses.

**Related Topics**
------------------

1. [Vehicle](https://docs.frappe.io/hr/vehicle)
2. [Vehicle Log](https://docs.frappe.io/hr/vehicle-log)

  

<!-- page: frappe-hr/hr__full-and-final-statement.md -->
---
title: "Full and Final Statement"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/full-and-final-statement"
updated: "2026-02-04"
---

When the employee is relieved from the company, all the payables, receivables, and assets allocated to the employee are settled using the Full and Final Statement or Settlement. This statement serves as a checklist to ensure smooth exit procedures with an accounting impact.

**1. Prerequisites**
--------------------

Before creating a Full and Final Statement, you need to have an [Employee](https://docs.frappe.io/hr/employee) in the system.

This document is created for an Employee who has resigned or is being terminated. Hence it is mandatory to set the **Relieving Date** for the Employee too.

**2. How to create a Full and Final Statement**
-----------------------------------------------

Go to


> **Employee Lifecycle > Exit > Full and Final Statement > New.**
> 
> 

1. Select the Employee.
2. The system will pull in some components and existing documents in payables/receivables:


	* **Payables**: Salary Slip, Gratuity, Expense Claim, Bonus, Leave Encashment
	* **Receivables**: Loan, Employee Advance
3. The default status for all these will be **Unsettled**. Users can then select the respective document against each (like expense claims yet to be settled, bonus(additional salary), etc.) and remove the components that do not require settling.
4. Users can also add their own components or custom doctypes to this checklist.
5. The amount and payable account will be fetched if applicable otherwise, it needs to be entered manually.


	* For eg:
	
	
		1. If a loan document is selected, then the payment account is fetched and the amount is set as `Total Payment - Total Amount Paid`
		2. If an Employee Advance is selected, then the payment account is set as the advance's payment account, and the amount is set as `paid_amount - (claimed_amount + return_amount)`
		3. If an Expense Claim is selected, then the payment account is set as the claim's payable account, and the amount is set as `grand_total - (total_amount_reimbursed + total_advance_amount)`
		4. For gratuity, payable account and amount are fetched as is.
		5. For Salary Slip, the account is set as Payroll Payable Account and the amount is fetched from the salary slip's `net_pay`
6. Based on that the total receivable/payable will be calculated
7. The system will automatically fetch assets allocated to the employee by the company (eg: laptops, phones, etc). These records are fetched from existing Asset Movement records.
8. These assets need to be returned to the company or you can also choose to recover the asset cost instead.
9. The status will be Pending by default. After reviewing all the amounts and accounts, HR can mark all the components in Payables, Receivables, and Assets as Settled.

![](https://frappehr.com/files/kICaqMO.png)  


**3. Features**
---------------

### **3.1 Asset Cost Recovery**

Consider a scenario where you allocate some assets to the employee like laptops/uniforms. In some cases, you might not want to return the asset to the company but instead, recover the asset cost and let the employee own the asset.

You can set "Action" as "Recover Cost" in such cases against such assets. This will add the Total Asset Cost for that asset to the **Total Receivable Amount**.

### **3.2 Settle with Journal Entry**

On submission, a button to create a Journal Entry will be shown. Click on **Create Journal Entry**. This entry is made to record payment from the employee + payment done to the employee hence settling the account.

This will map all your accounts and amounts to your journal entry. Select the final account from where the amount should get created if not already mapped. Save and Submit. The FnF status should then change to Paid.

![](https://frappehr.com/files/RxYZp3s.png)  


  

<!-- page: frappe-hr/hr__goal.md -->
---
title: "Goal"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/goal"
updated: "2026-02-04"
---

**Goal setting is the process of planning specific, measurable and role-oriented goals that employees work towards in your company.**

To check the goal list, go to:


> **Home > Human Resources > Performance > Goal**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Goal, you should create the following:

* [Employee](https://docs.frappe.io/hr/employee)

If you want the goal's progress to impact your appraisals, you will also need to create:

* [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle)
* [Appraisal](https://docs.frappe.io/hr/appraisal)

**2. Goal Setting**
-------------------

### **2.1 From the tree view**

Since goals have a hierarchical structure, its easier to add new goals from the tree view. You can also update the progress for your child goals from the tree view. Parent goal's progress is auto-calculated based on child goals.

![goal tree](https://frappehr.com/files/goal-tree.png)  


You can apply a filter for the Appraisal cycle and your Employee record. These fields will be picked up in the New Goal dialog.

![goal update](https://frappehr.com/files/goal-update.gif)  


### **2.2 From the list view**

1. Go to the Goal list, and click on New.
2. Enter your goal. You can optionally add a detailed description of your goal.
3. You can break down your goals into sub-goals for better tracking. To do so, select the goal in the Parent Goal field. Ex: I have a goal called Quality Improvement aligned to the Quality KRA. I can add multiple goals under Quality Improvement like:


	* Bring down GitHub issues by 20%
	* Increase test converage by 30%
4. Mark the goal as **Is Group** if this goal is going to have sub-goals
5. Select the Employee.
6. Set the Start and End Dates for your goal.
7. If you want the goal's progress to impact your appraisal, select the Appraisal Cycle and tag the KRA for your goal. Now on updating the goal's progress the goal score linked to your KRA will be updated.
8. Save. The status of your goal is auto-updated based on the progress.

![goal](https://frappehr.com/files/goal.png)  


![goal list](https://frappehr.com/files/goal-list.png)  


**3. Features**
---------------

### **3.1 Goal Progress Update**

Whenever a child goal is updated, the parent's goal progress is also updated.

How does a goal's progress affect its parent?

Ex: progress for the goal `child2` is 25%: the average of its children (`child3` and `child4`) progress for the goal `parent` is 12.5%: the average of its children (`child1` and `child2`)


```
parent (12.5%)
|_ child1 (0%)
|_ child2 (25%)
        |_ child3 (50%)
        |_ child4 (0%)
  

```
Whenever a goal is updated, the average goal completion against the KRA linked to that goal is also updated. Ex: In the screenshot below, the Development KRA has 30% weightage and the employee has completed 75% of the goals. So the goal score is 22.5 out of 30, and so on.

![kra vs goals](https://frappehr.com/files/kra-vs-goals.png)  


### **3.2 Archive Goal**

Sometimes you add a goal while planning but later on, you don't want to work on that goal anymore. In that case, you can archive the goal. Archived goal's progress won't contribute to the KRA/Goal score.

![archive](https://frappehr.com/files/archive.png)  


### **3.2 Close Goal**

Closing goals will stop employees from making further progress updates but would still contribute to the KRA/Goal score, unlike Archived goals. You can close a goal by clicking the **Status > Goal** button on the Goal form

**4. Related Topics**
---------------------

1. [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle)
2. [Appraisal](https://docs.frappe.io/hr/appraisal)

  

<!-- page: frappe-hr/hr__gratuity-rule.md -->
---
title: "Gratuity Rule"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/gratuity-rule"
updated: "2026-02-04"
---

> This Feature is introduced in Version 13, which will be part of separate Payroll Module.

**Gratuity Rule are set of rule defined by Central or State used during calculation of Gratuity Amount**

In Frappe HR, you can define different Gratuity Rules based on different Region.

To access the Gratuity Rule, go to:

> Home > Payroll > Gratuity Rule

**1. Prerequisites**
--------------------

Before creating a Gratuity Rule, it is advised to create the following:

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create Gratuity Rule**
----------------------------------

1. Got to Gratuity Rule > New
2. Select Applicable Components. These Salary Components contribute during Gratuity Calculation.
3. Select "Calculate Gratuity Amount based on"
4. Define Gratuity Rule
5. Save

![Gratuity Rule](https://frappehr.com/files/gratuity-rule.png)  


**3. Additional Properties**
----------------------------

Some of the additional attributes used while gratuity Calculation are define below.

### **3.1 Work Experience Calculation method:**

Frappe HR provide two different method for calculation of Work experience.

1. Round off Work Experience method Round off yor current experience. For example, if employee have total experience of 3 year and 6 month will be treated as 4 year experience.
2. Take Exact Completed Year.

### **3.2 Calculate Gratuity Amount Based On:**

Let's consider the following example to understand the calculation.

![gratuity-rule-example](https://frappehr.com/files/gratuity-rule-example.png)  


1. **Current slab:** If Gratuity Amount calculation is based on Current Slab, then amount will be the product of Work Experience (in years), Fraction of Applicable Earnings and summation of the Applicable Earnings Components. Based on above Gratuity Rules/slab, if an employee has an experience of 5 years, then it falls in third slab. The calculation of Gratuity Amount will be as follows:

> Gratuity amount = 5  *0.467*  (Arrear + Basic)

2. **Sum of all previous slabs:** If Gratuity Amount calculation is based on Sum of all previous slabs, then amount will be the summation of product of individual slabs up to the year of experience and summation of Applicable Earnings Component. Based on above Gratuity Rules/slab, if an employee has an experience of 5 years, then the calculation of Gratuity Amount will be as follows:

> Gratuity amount = [(1  *0) + (2*  0.233) + (2  *0.467)]*(Arrear + Basic)

  

<!-- page: frappe-hr/hr__gratuity.md -->
---
title: "Gratuity"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/gratuity"
updated: "2026-02-04"
---

> This Feature is introduced in Version 13, which will be part of a separate Payroll Module.

**Gratuity is given by the employer to his/her employee for the services rendered by him/her during the period of employment. It is usually paid at the time of retirement but can be paid earlier, provided certain conditions are met.**

In Frappe HR you can manage Gratuity Payments of employee, based on different [Gratuity Rule](https://docs.frappe.io/hr/gratuity-rule) which vary from region to region.

To access the Gratuity go to:

> Home > Payroll > Gratuity

**1. Prerequisites**
--------------------

Before creating an Gratuity, it is advised to create the following:

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Gratuity Rule](https://docs.frappe.io/hr/gratuity-rule)
3. [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create Gratuity**
-----------------------------

1. Got to Gratuity > New
2. Select Employee and Gratuity Rule. On selecting it will calculate Current Work Experience and Total Gratuity Amount based on Gratuity rule and relieving date.
3. Check checkbox Pay via Salary Slip. if you want gratuity payment through Salary Slip.
4. Save and Submit

![Gratuity](https://frappehr.com/files/gratuity.png)  


**3. Gratuity Payments Methods**
--------------------------------

In Frappe HR, we allow you to pay the amount via Salary Slip or Payment Entry.

### **3.1 Payment via Salary Slip**

To pay the Gratuity amount via Salary Slip you need to check the checkbox **Pay via Salary Slip**. Select Payroll Date and **Salary Component**, which will appear on Check.

![payment conf via salary slip](https://frappehr.com/files/payment-conf-via-salary-slip.png)  


On Submit, it will automatically create Additional Salary with respective Payroll Date and Salary Component.

![gratuity payment via salary slip](https://frappehr.com/files/gratuity-payment-via-salary-slip.png)  


### **Payment via Payment Entry**

To pay the Gratuity amount via Payment Entry you need to make sure that checkbox **Pay via Salary Slip** is unchecked. After that, it will allow you to select Payable Account, Expense Account, and **Mode of Payment**.

![payment conf via payment entry](https://frappehr.com/files/payment-conf-via-payment-entry.png)  


After Submitting the record click on the button "Create Payment Entry" which will redirect you to the Payment Entry Form fill in the details, save, and submit.

![gratuity payment via payment entry](https://frappehr.com/files/gratuity-payment-via-payment-entry.png)  


  

<!-- page: frappe-hr/hr__holiday-list.md -->
---
title: "Holiday List"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/holiday-list"
updated: "2026-02-04"
---

**Holiday List is a list which contains the dates of holidays.**

Most organizations have a standard Holiday List for their employees. However, some of them may have different holiday lists based on different Locations or Departments. In ERPNext, you can configure multiple Holiday Lists and assign them to your employees based on your requirements.

To access Holiday List, go to:

> **Home > Human Resources > Leaves > Holiday List**

## **1. How to create a Holiday List**

1. Go to Holiday List, click on New.
2. Enter Holiday List Name. It can be based on the Fiscal Year or Location or Department as per the requirement.
3. Select From Date and To Date for the Holiday List.

![Holiday List](https://frappehr.com/files/holiday-list-1.png)

## **2. Features**

Some of the additional features in the Holiday List are as follows:

### **2.1 Adding Weekly Holidays**

You can quickly add Weekly Offs in the Holiday List as follows:

1. In the 'Add Weekly Holidays' section, select the day in the Weekly Off field.
2. Click on the 'Add to Holidays' button.

![Holiday List](https://frappehr.com/files/holiday-list-2.gif)

### **2.2 Adding Local Holidays**

You can quickly add local holidays to the Holiday List as follows:

1. In the 'Add Local Holidays' section, select the country.
2. Some countries have subdivisions with different or additional holidays. If you like, you can optionally select a specific subdivision.
3. Click on the 'Add to Holidays' button.

#### Can't find your country for fetching local holidays in Holiday List?

Frappe HR uses an external package Holidays to get predictable holiday dates for countries. These are the list of countries supported:

https://holidays.readthedocs.io/en/latest/#available-countries 

If your country is not listed here, you will have to manually add local holidays. If you are a developer, you can also consider contributing your country’s holidays to the original repository.

### **2.3 Adding Holidays manually**

You can also add specific days manually by clicking on the 'Add row' option in the Holidays table.

![Holiday List](https://frappehr.com/files/holiday-list-3.png)

## **3. Holiday List in Company**

You can set a default Holiday List at the company-level in the Company master in the 'Default Holiday List' field.

![Holiday List](https://frappehr.com/files/default-holiday-list-company.png)

## **4. Holiday List in Employee**

See Holiday List Assignment

## **5. Holiday List in Workstation**

You can also set a Holiday List at workstation-level as shown in the screenshot below.

![Holiday List](https://frappehr.com/files/holiday-list-workstation.png)

The dates in the Holiday List tagged in the Workstation master will be considered as the days the Workstation will remain closed.

## **6. Related Topics**

1. Leave Allocation
2. Leave Period
3. Leave Policy
4. HR Settings

<!-- page: frappe-hr/hr__how-to-encash-unused-leaves-using-salary-slips.md -->
---
title: "How to encash unused leaves using Salary Slips"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/how-to-encash-unused-leaves-using-salary-slips"
updated: "2026-02-04"
---

Encashment of unused leaves into an Employee's Salary Slip can be done easily by following the steps given below

1. Enable 'Allow Encashment' for the Leave Type which will be of Encashment type.

![](https://docs.erpnext.com/files/2N9pIsu.png)  


2. Add it in the Leave Policy and assign it to the Employee you want to create this Leave Policy for by going to the Leave Policy Assignment. Leaves will automatically be allocated once the Leave Policy Assignment is 'Submitted'.

![](https://docs.erpnext.com/files/CRA2R4X.png)


3. Before creating a **Leave Encashment** with the Encashable Leave Type that was previously created, make sure that a Salary Structure is assigned to the Employee and that you have added the 'Leave Encashment Amount Per Day (INR)' for the same Salary Structure.

![](https://docs.erpnext.com/files/d1KlS2Q.png)  


4. Assign the Salary Structure to the same Employee.

![](https://docs.erpnext.com/files/5j8DhiT.png)  


5. Create a Leave Encashment and make sure that the date you create the Leave Encashment falls between the 'From Date' and 'To Date' in the Leave Allocation.

![](https://docs.erpnext.com/files/InFO2wh.png)  


The '**Encashment Amount**' will be automatically pulled in when you save the Leave Encashment DocType.

An Additional Salary will be automatically created once the 'Encashment Leave' is **Submitted**.

![](https://docs.erpnext.com/files/d1KlS2Q.png)  


6. On creation of the Salary Slip the Leave Encashment amount will be added along with other Earnings into the Salary Slip as shown below.

![](https://docs.erpnext.com/files/VSbXubU.png)  


You can use the ‘Preview Salary Slip’ button to make sure that the Encashed leaves are also included in the Employee’s Salary Slip before submitting the same.
