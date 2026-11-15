<!-- Frappe documentation: frappe-hr, part 1 of 3. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__additional-salary.md -->
---
title: "Additional Salary"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/additional-salary"
updated: "2026-02-04"
---

**Additional Salary is something that an Employee receives from the company they work for, other than their usual pay.**

Frappe HR offers you a feature called Additional Salary to add or deduct ad hoc salary for a particular Employee while processing the Payroll. Some examples of Additional Salary could be Performance Bonus, Deputation Allowance, Arrears, Incentives, or other adjustments.

To access Additional Salary, go to:

> Home > Human Resources > Payroll > Additional Salary

**1. Prerequisites**
--------------------

Before creating an Additional Salary, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create an Additional Salary**
-----------------------------------------

1. Go to the Additional Salary list, click on New.
2. Select Employee.
3. Select Salary Component.
4. Enter the Amount.
5. Enter the Payroll Date. If Payroll Date for Additional Salary is in the interval when the salary is processed, it will be added to the earnings/deduction.
6. Save and Submit.

Select the 'Overwrite Salary Structure Amount' checkbox to overwrite the Additional Salary component on the Salary Structure amount. Additionally, the 'Deduct Full Tax on Selected Payroll Date' checkbox can be selected if full tax needs to be deducted on the Additional Salary component for that particular payroll date.

![Additional Salary](https://frappehr.com/files/additional-salary.png)  


**3.Features**
--------------

### **3.1 Recurring Additional Salary**

This feature allows users to create an Additional Salary for a fixed interval. When 'Is Recurring' is checked you need to fill 'To Date' and 'From Date'. This will add or deduct the additional salary amount for this employee within the selected date range and it will be reflected in the Salary Slip for the employee. The Additional Salary will be repeated every month between 'From Date' and 'To Date' interval.

**4. Related Topics**
---------------------

1. [Retention Bonus](https://docs.frappe.io/hr/retention-bonus)
2. [Employee Incentive](https://docs.frappe.io/hr/employee-incentive)
3. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
4. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
6. [Payroll Period](https://docs.frappe.io/hr/payroll-period)

  

<!-- page: frappe-hr/hr__appointment-letter.md -->
---
title: "Appointment Letter"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/appointment-letter"
updated: "2026-02-04"
---

> Introduced in Version 13

**The letter written by the employer requesting the selected candidates to join in a specific position.**

In Frappe HR you can create an Appointment Letter that you can give to candidates. To access Appointment Letter, go to:

> Home > Human Resource > Recruitment > Appointment Letter

**1. Prerequisites**
--------------------

Before creating an Appointment Letter, it is advisable to create the following:

* [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**2. How to Create an Appointment Letter**
------------------------------------------

1. Go to an Appointment Letter list, click on New.
2. Select the Job Applicant and Appointment Date.
3. You can manually fill Introduction, Terms and, Closing Statement or select an Appointment Letter Template to autofill the content. You can create new Appointment Letter Templates to select them easily.
4. Click on Save.
5. After saving, go to the Print View to view and save the PDF of the Appointment letter.

![Appointment Letter](https://frappehr.com/files/appointment-letter.png)

> **Note:** Appointment Letter can be made only against a [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**3. Features**
---------------

### **3.1 Appointment Letter Template**

1. Go to Appointment Letter Template list, click to New.
2. Fill Introduction, Terms and, Closing Statement.
3. Click on Save.

![Appointment Letter](https://frappehr.com/files/appointment-letter-template.png)

> **Note** On selecting Appointment Letter Template in Appointment Letter, it autofills the content.

### **3.2 Print Format**

You can create new or use existing standard print formats.

![Appointment Letter](https://frappehr.com/files/standard-appointment-letter.png)  


  

<!-- page: frappe-hr/hr__appraisal-cycle.md -->
---
title: "Appraisal Cycle"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/appraisal-cycle"
updated: "2026-02-04"
---

An Appraisal Cycle is a defined period of time during which the overall performance of an employee is assessed.

To create an Appraisal Cycle, go to:


> **Home > Human Resources > Performance > Appraisal Cycle**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Appraisal Cycle, you should create [Appraisal Templates](https://docs.frappe.io/hr/appraisal-template) for different designations.

You can link them in the Designation master for fetching them automatically in the cycle or manually select relevant templates in the Appraisees child table.

**2. How to create an Appraisal Cycle**
---------------------------------------

1. Go to the Appraisal Cycle list, and click on New.
2. Enter the Cycle Name.
3. Select the Company and set the Start and End dates.
4. Select the KRA Evaluation Method:


	* **Automated Based on Goal Progress** (Default): Your KRA/Goal score will be automatically calculated based on your goal completion linked to that KRA. You can read more about [here](https://docs.frappe.io/hr/goal).
	* **Manual Rating**: You can choose to rate Goals/KRAs manually. This is the original evaluation method used until v13.
5. By default, the Final Score is calculated as the average of Goal Score, Feedback Score, and Self Appraisal Score. To calculate final score using your own formula, enable ***Calculate Final Score based on Formala*** and enter the formula expression.

  


![](https://frappehr.com/files/0UPkmBl.png)

**3. Actions**
--------------

### **3.1 Create Appraisals**

You can create appraisals in bulk from the Appraisal Cycle.

1. In the "Applicable For" tab, set relevant filters to fetch the employees included in this cycle. You can choose to create separate cycles for a particular Branch, Department, or Designation. Ex: Engineering could have an yearly cycle but Sales might need a half-yearly cycle.
2. After setting the filters, click on the **Get Employees** button and save. This will fetch the employees based on the set filters.
3. You can check the Employees table to find the fetched employees. You can add more employees to be included in the cycle manually by clicking on the **Add Row** button.
4. Click on the **Create Appraisals** button. This will create all the Appraisal documents for the selected employees.
5. Click on **Start** button to start the cycle.

![create appraisalsaa9d04](https://frappehr.com/files/create-appraisalsaa9d04.gif)  


If an employee joins after the cycle has already started, you can:

* Create an Appraisal document for them separately and select the cycle.
* Or, add rows for new employees in the cycle's Employees child table, save and click on Create Appraisals again. This will create appraisals for the newly added employees.

### **3.2 View Goals**

With this button, you can view the goals linked to the cycle. This button will navigate you to the Goal Tree filtered by the Appraisal Cycle.

![filtered goal tree](https://frappehr.com/files/filtered-goal-tree.png)  


**4. Features**
---------------

### **4.1 Appraisal Stats**

The Stats section in the cycle will give you an overview of:

* Appraisees: The number of appraisees included in the cycle
* Self Appraisal Pending
* Employees without Feedback
* Employees without Goals

![appraisal stats](https://frappehr.com/files/appraisal-stats.png)  


**5. Related Topics**
---------------------

1. [Appraisal](https://docs.frappe.io/hr/appraisal)
2. [Goal](https://docs.frappe.io/hr/goal)
3. [Employee Performance Feedback](https://docs.frappe.io/hr/employee-performance-feedback)

  

<!-- page: frappe-hr/hr__appraisal-overview-report.md -->
---
title: "Appraisal Overview Report"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/appraisal-overview-report"
updated: "2026-02-04"
---

This report gives an overview of the Appraisals:

* **Appraisal Cycle & Appraisal**
* **Feedback Count**: Number of feedback documents created against the appraisal
* **Goal Score**: Goal completion score against KRA
* **Avg Feedback Score**: Avg of all the feedback scores received
* **Self Score**: Self Appraisal Score
* **Final Score**: Avg of Goal Score, Feedback Score, and Self Score

![appraisal overview](https://frappehr.com/files/appraisal-overview.png)  


  

<!-- page: frappe-hr/hr__appraisal-template.md -->
---
title: "Appraisal Template"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/appraisal-template"
updated: "2026-02-04"
---

You can define the KRAs and Feedback Criteria based on which employees would be rated in the Appraisal Template.

To access Appraisal Template, go to:


> Home > Human Resources > Performance > Appraisal Template
> 
> 

1. Prerequisites
----------------

Before creating an Appraisal Template, you should create the following:

* KRA: Key Result Areas master to align your goals against
* Employee Feedback Criteria: Criteria based on which employees should be rated in Performance Feedback and Self Appraisal

2. How to create an Appraisal Template
--------------------------------------

1. Go to the Appraisal Template list, and click on New.
2. Enter a title for the Template. You can keep the title same as the Department or Designation you are creating the template for.
3. You can optionally set some description.
4. Add the KRAs (Key Result Areas) along with their weightages.
5. Add the Criteria based on which employees should be rated in Performance Feedback and Self Appraisal.

![](https://frappehr.com/files/appraisal-template9d1d22.png)

Once you create the templates, you can link them to the respective Designations.

![template link](https://frappehr.com/files/template-link.png)  


You can link a template to multiple designations

![](https://frappehr.com/files/template-link-2.png)  


3. Related Topics
-----------------

1. [Appraisal](/hr/appraisal)
2. [Employee Performance Feedback](/hr/employee-performance-feedback)

<!-- page: frappe-hr/hr__appraisal.md -->
---
title: "Appraisal"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/appraisal"
updated: "2026-02-04"
---

**An appraisal is a process in which an employee's performance is documented and evaluated.**

To create an Appraisal Cycle, go to:


> **Home > Human Resources > Performance > Appraisal**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Appraisal, you should create the following:

* [Appraisal Template](https://docs.frappe.io/hr/appraisal-template)
* [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle)

**2. How to create an Appraisal**
---------------------------------

Appraisals can be created in bulk from the [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle).

However, if you want to create an appraisal manually, here are the steps:

1. Go to the Appraisal list, and click on New.
2. Select the Employee
3. Select the Appraisal Cycle.
4. If the Appraisal Template for the employee is already set in the cycle's Employees child table, it will be auto-fetched. Else you can select a template for the employee. Save.

**3. Features**
---------------

### **3.1 KRA Evaluation**

Based on the KRA Evaluation Method selected in the [Appraisal Cycle](https://docs.frappe.io/hr/appraisal-cycle) one of the following processes would be applicable:

#### **3.1.1 Automated Based on Goal Progress**

This is the default KRA Evaluation method.

In this method you can create goals and sub-goals aligned to your KRAs.

A KRA vs Goals table will be visible in your appraisal document.

* **KRA and weightage**: Fetched from the appraisal template
* **Goal Completion (%)**: Your goal completion percentage will be auto-calculated based on the **progress** of the goals linked to your KRAs.
* **Goal Score (weighted)**: Based on the weightage assigned to each KRA, the Goal Score will be computed from the completion percentage. For ex: In the screenshot below, the Development KRA has 30% weightage and the employee has completed 75% of the goals. So the goal score is 22.5 out of 30, and so on.

You will finally get a **Total Goal Score** (out of 5) based on the **Goal Score (%)**.

![kra vs goals](https://frappehr.com/files/kra-vs-goals.png)  


#### **3.1.2 Manual Rating**

You can choose to rate Goals/KRAs manually. This is the original evaluation method used until v13.

1. Based on the template selected, the KRAs will be fetched in the Goals section.
2. Enter the score (0-5) for each KRA.
3. Based on the weightage mentioned, the **Score Earned** will be calculated for each KRA.
4. Save.

Based on the Score Earned for each KRA, the system will calculate the Total Score (out of 5) for the Employee.

![manual rating](https://frappehr.com/files/manual-rating.png)  


### **3.2 Feedback**

Employee Performance Feedback is captured in the [Employee Performance Feedback](https://docs.frappe.io/hr/employee-performance-feedback) DocType.

But to get an overview of the employee's performance, you can see the history of all the feedback employee has received in the cycle under the Feedback tab.

You can see the rating summary with the average feedback score, no of reviews, and the percentage distribution of the stars the employee has received.

![feedback history](https://frappehr.com/files/feedback-history.png)  



> **Note: Only submitted feedback documents are visible in this history and the view is permission sensitive.**
> 
> 

In every review, you can see the reviewer, their designation, avg rating given to the employee, the feedback and the time when the feedback was given. You can also click on the link icon to see the entire Employee Performance Feedback document.

![feedback link](https://frappehr.com/files/feedback-link.png)  


If you have the required permissions, you can submit the performance feedback right from this view by clicking on the **New Feedback** button.

![add feedback](https://frappehr.com/files/add-feedback.png)  


### **3.3 Self Appraisal**

Under the Self Appraisal tab, employees can rate themselves and add reflections on their performance. The Total Self Score is calculated based on the rating and the weightage against each Feedback Criteria.

![self appraisal](https://frappehr.com/files/self-appraisal.png)  


### **3.4 Final Score Calculation**

The Final Score is calculated as an average of your Goal Score, Avg Feedback Score, and Self Appraisal Score.

![final score](https://frappehr.com/files/final-score.png)  


### **3.5 View Goals**

You can view the Employee's goals linked to that Appraisal Cycle by clicking on the View Goals button:

![goals appraisal](https://frappehr.com/files/goals-appraisal.png)  


### **3.6 Approvals for Appraisals**

Finally, once you have captured all the feedback and updated goals and self appraisal in the Appraisal document, you can submit it.

You can also set up a [Workflow](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/workflows) for approvals before Appraisal submission.

**4. Related Topics**
---------------------

1. [Goal](https://docs.frappe.io/hr/goal)
2. [Employee Performance Feedback](https://docs.frappe.io/hr/employee-performance-feedback)

  

<!-- page: frappe-hr/hr__arrears.md -->
---
title: "Arrears"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/arrears"
updated: "2026-02-04"
---

Review and approval of new salary structures often takes time and is assigned to employee much later than the applicable date.

When a new Salary Structure Assignment is approved and applied (e.g., June 2025 onward, but effective from April 2025), and salary for past months (April, May) has already been processed, this feature calculates and compensates the employee for the arrears, ensuring their paid salary matches the new structure.



Step 1: Navigate to Arrears doctype
1.	Go to HR > Payroll > Arrears

Step 2: Select Employee, Salary Structure, and the date from which arrears needs to paid for.

Step 3: Save and Submit

- Upon save system will populate earning, deduction and accrual arrears in respective child tables.
- Based on Payroll Date, additional salary will be created for earnings and deductions after submission. Accruals are tracked in Employee Benefit Ledger

![](/files/Screenshot%202025-09-23%20at%201.20.20%E2%80%AFPM.png)
![](/files/Screenshot%202025-09-23%20at%201.21.03%E2%80%AFPM.png)

<!-- page: frappe-hr/hr__attendance-request.md -->
---
title: "Attendance Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/attendance-request"
updated: "2026-02-04"
---

**Using the Attendance Request, employees can submit their attendance request for the days when their attendance wasn't marked due to various reasons such as on-site duty or work from home. Attendance Request can also be used for Attendance Regularization to overwrite existing attendance records.**

To access Attendance Request, go to:

> Home > Human Resources > Attendance > Attendance Request

**1. Prerequisites**
--------------------

Before creating an Attendance Request, it is advised that you create the following first:

* [Employee](https://docs.frappe.io/hr/employee)

**2. How to create an Attendance Request**
------------------------------------------

1. Go to Attendance Request list, click on New.
2. Select Employee who wants to submit the Attendance Request.
3. Select From Date and To Date of Attendance Request.
4. You can enable **"Include Holidays"** if you want to mark attendance for holidays in between these dates too. This feature was introduced v15 onwards.
5. Select Reason and enter Explanation (optional).
6. Save and Submit.

![Attendance Request](https://frappehr.com/files/attendance-request.png)

> **Note 1:** You can check the 'Half Day' checkbox and enter the Date in case the attendance is for Half Day.

> **Note 2:** On submission of the same, Attendance documents will be created for the days you mentioned as shown.

![Attendance Request Submit](https://frappehr.com/files/attendance-request-submission.png)  


As seen below, respective Attendance records are linked with the submitted Attendance Request.

![Attendance Request Linked](https://frappehr.com/files/attendance-request-link.png)  


If you cancel the Attendance Request, the linked Attendance documents created will be cancelled as well.

![Attendance Request Cancelled](https://frappehr.com/files/attendance-request-cancelled.png)  


**3. Features**
---------------

### **3.1 Overwrite an existing Attendance record**

Consider a scenario where the auto-attendance tool marked an employee as Absent. If the employee wants to rectify their attendance, they can raise a request. On submission, the Attendance record will be updated:

![changed status](https://frappehr.com/files/changed%20status.png)  


The submission can be controlled via [workflows](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/workflows) to undergo approvals.

### **3.2 Request for Attendance in Bulk**

Employees can also request for attendance for an entire month or week. On submission, attendance marking is skipped for holidays or leave days.

You can enable "Include Holidays" if you want to mark attendance for holidays too.

![](https://frappehr.com/files/FYdSpw9.png)  


Attendance warnings are shown on the request dashboard for the same:

![attendance warnings](https://frappehr.com/files/attendance-warnings.png)  


**4. Related Topics**
---------------------

1. [Employee Attendance Tool](https://docs.frappe.io/hr/employee-attendance-tool)
2. [Shift Management](https://docs.frappe.io/hr/shift-management)
3. [Auto Attendance](https://docs.frappe.io/hr/auto-attendance)
4. [Upload Attendance](https://docs.frappe.io/hr/upload-attendance)
5. [Attendance](https://docs.frappe.io/hr/attendance)

  

<!-- page: frappe-hr/hr__attendance.md -->
---
title: "Attendance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/attendance"
updated: "2026-02-04"
---

**Attendance is a record stating whether an Employee has been present on a particular day or not.**

In Frappe HR, you can mark and record attendance of an Employee on a daily basis using the Attendance doctype.

To access Attendance, go to:

> Home > Human Resources > Attendance

**1. Prerequisites**
--------------------

Before creating an Attendance record, it is advised that you create the following first:

* [Employee](https://docs.frappe.io/hr/employee)
* [Shift Type](https://docs.frappe.io/hr/shift-management)

**2. How to create an Attendance**
----------------------------------

1. Go to the Attendance list, click on New.
2. Select the Employee.
3. Select the Attendance Date.
4. Select the Shift (optional).
5. Select the Status (Present, Absent, On Leave, Half Day).
6. Save and Submit.

![Attendance](https://frappehr.com/files/attendance.png)

> **Note:** Attendance cannot be marked for future dates.

You can get a monthly report of your Attendance data by going to the **Monthly Attendance Details** report.

You can easily set attendance for Employees using the [Employee Attendance Tool](https://docs.frappe.io/hr/employee-attendance-tool).

You can also bulk upload attendance using the [Upload Attendance](https://docs.frappe.io/hr/upload-attendance).

**3. Features**
---------------

### **3.1 Marking Unmarked Attendance**

In case the attendance for some employees is not marked, you can mark them as present, absent, or half-day.

#### **How to Mark Attendance**

1. Go to the Attendance list.
2. Click on the **Mark Attendance** button.
3. A dialog will appear.
4. Select the Employee and Month.
5. Select the Status whether Present, Absent, or Half Day.
6. If you want to exclude holidays while doing so, check *Exclude Holidays*.
7. Select the dates on which you want to mark attendance for a selected Employee.
8. Click on the **Mark Attendance** button and click on **Yes**.

![Attendance](https://frappehr.com/files/mark-attendance.gif)

**4. Related Topics**
---------------------

1. [Employee Attendance Tool](https://docs.frappe.io/hr/employee-attendance-tool)
2. [Shift Management](https://docs.frappe.io/hr/shift-management)
3. [Auto Attendance](https://docs.frappe.io/hr/auto-attendance)
4. [Upload Attendance](https://docs.frappe.io/hr/upload-attendance)
5. [Attendance Request](https://docs.frappe.io/hr/attendance-request)

It is also, possible to set up marking of attendance automatically based on check-in/check-out logs from Biometric/RFID Devices (or any other similar mechanisms that produce IN/OUT logs of the employee). Please refer to [Auto Attendance](https://docs.frappe.io/hr/auto-attendance) feature for more information.

  

<!-- page: frappe-hr/hr__auto-attendance.md -->
---
title: "Auto Attendance"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/auto-attendance"
updated: "2026-02-04"
---

Auto attendance marks the attendance for employees assigned to a shift based on the records in the [Employee Checkin](https://docs.frappe.io/hr/employee-checkin) document and the [Auto Attendance Settings](https://docs.frappe.io/hr/shift-type#2-auto-attendance-settings) of that shift.


> **Note:** [**Shift Type**](/hr/shift-type) **needs to be set up and assigned to employees before creating 'Employee Checkin' records. Attendance will be marked by Auto Attendance only for check-in records that are created after setting up and assigning an employee to their shift type.**
> 
> 

**Steps to Set Up Auto Attendance**
-----------------------------------

You can set up Auto Attendance by following the steps mentioned below:

### **1. Define Shift Type with Auto Attendance Enabled**

You will have to define a Shift Type with Auto Attendance enabled. Details can be found [here](https://docs.frappe.io/hr/shift-type).

### **2. Assign these shifts to employees**

Once you have set up a shift, you will have to assign this shift to the employees. You can assign this to an employee using one of the two methods given below:

* **Using the Shift Assignment**: You can use the [Shift Assignment](https://docs.frappe.io/hr/shift-assignment) document to assign shifts to employees on a date to date basis.
* **Using the Default Shift field in the employee master**: Sometimes you would want to assign a shift for an employee for all the days. You can do this by setting the following field in the Employee: `> Employee > Attendance and Leave Details > Default Shift`


> **Note: Setting Shift Assignment takes precedence over the Default Shift. i.e. if you have set up a shift assignment as well as a default shift for an employee, the system will consider the assigned shift over a default shift.**
> 
> 

### **3. Setup Attendance Device ID field in Employee**

Biometric systems usually have their own IDs for employees. But, the Employee Checkin in Frappe HR needs to be mapped to an employee.

To map the employee to their IDs in the Biometric system you need to set the following field with the appropriate value: `Employee > Attendance and Leave Details > Attendance Device ID (Biometric/RF tag ID)`

### **4. Import or sync Employee Checkins**

Once you are done with the above steps you can import/sync the [Employee Checkin](https://docs.frappe.io/hr/employee-checkin) and start generating attendance automatically.

Please refer to this article to know more about populating Employee Checkins from an external system: [Integrating Frappe HR With Biometric Attendance Devices](https://docs.frappe.io/hr/integrating-frappe-hr-with-biometric-attendance-devices)

**Frequently Asked Questions**
------------------------------

### **1. How are a shift's actual start and end timings determined?**

Consider a Morning Shift:

* Start Time: 08:00:00
* End Time: 11:30:00
* Begin check-in before shift start time (in minutes): 60
* Allow check-out after shift end time (in minutes): 60

So the "Actual Start Time" of the shift = *Start Time - Begin check-in before shift start time* = 07:00:00

The "Actual End Time" of the shift = *End Time + Allow check-out after shift end time* = 12:30:00.

### **2. When is the attendance marked automatically for a particular shift?**

Auto Attendance for every 'Shift Type' record is attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Auto Attendance' button in the Shift Type document.

Once the "**Last Sync of Checkin**" passes the shift's actual end time, all the employee checkins for that shift are processed for marking attendance.

For eg: Consider a Morning Shift:

* Start Time: 08:00:00
* End Time: 11:30:00
* Begin check-in before shift start time (in minutes): 60
* Allow check-out after shift end time (in minutes): 60

So the "Actual Start Time" of the shift is 07:00:00 and the actual end time of the shift is 12:30:00.

Once the "Last Sync of Checkin" timestamp passes 12:30:00, it indicates that all possible checkin records for that particular shift have been synced/captured and this is when attendance marking is attempted.

### **3. How does Auto Attendance determine shift for an Employee?**

The shift of an Employee on a particular date is determined by the following steps:

* Shift assigned to an Employee on the given date in the 'Shift Assignment' document.
* If the above is not found, the shift is picked up from the 'Default Shift' field of the 'Employee' document.
* Finally, if a shift is not found in 'Employee' document also, then it is assumed that the Employee does not belong to any shift on the given date and no attendance is attempted to be marked by the Auto Attendance job.

### **4. How does Auto Attendance determine Holiday List for an Employee?**

Holiday List for an employee is determined as follows:

* If the employee's determined 'Shift Type' has a holiday list, then this is considered.
* Otherwise, the holiday list is fetched from either the 'Holiday List' field in the Employee document or from the 'Default Holiday List' field in the Company document, in that order.

Note: The Holiday List is important to be determined correctly by the Auto Attendance to not mark the employee as 'Absent' on holidays.

### **5. Most Biometric devices don't return the exact Log Type. In such cases how will the auto attendance determine which log is IN/OUT and how does it calculate working hours?**

This is determined by 2 fields in the Shift Type set up:

* Determine Check-in and Check-out
* Working Hours Calculation Based On

It has been explained in detail over [here](https://docs.frappe.io/hr/shift-type#2-auto-attendance-settings).

  

<!-- page: frappe-hr/hr__branch.md -->
---
title: "Branch"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/branch"
updated: "2026-02-04"
---

**A Branch office is an outlet of a company located at a different location, other than the main office.**

Frappe HR allows you to create and keep a record of the different branches of your organization.

To access Branch, go to:


> **Home > Human Resources > Employee > Branch**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Branch, it is mandatory you create the following documents:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)

**2. How to create a Branch**
-----------------------------

1. Go to the Branch list, click on New.
2. Enter the name of the Branch.
3. Save.

![Branch](https://frappehr.com/files/branch.png)  


You can link the Branch to the [Employee](https://docs.frappe.io/hr/employee) master.

**3. Related Topics**
---------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Employment Type](https://docs.frappe.io/hr/employment-type)
3. [Department](https://docs.frappe.io/hr/department)
4. [Designation](https://docs.frappe.io/hr/designation)
5. [Employee Grade](https://docs.frappe.io/hr/employee-grade)
6. [Employee Group](https://docs.frappe.io/hr/employee-group)

<!-- page: frappe-hr/hr__compensatory-leave-request.md -->
---
title: "Compensatory Leave Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/compensatory-leave-request"
updated: "2026-02-04"
---

**Compensatory Leave is a leave that is granted to an Employee as compensation for working overtime or on holidays.**

Frappe HR allows Employees to request for Compensatory Leaves through the Compensatory Leave Request document. It is necessary that the dates mentioned in the Compensatory Leave Request should be in default Holiday List and also that the Employee should have their attendance marked Present.

> **Note:** Only Leave Types which are marked as 'Is Compensatory' can be selected in the Compensatory Leave Request.

To access Compensatory Leave Request, go to:

> Home > Human Resources > Leaves > Compensatory Leave Request

**1. Prerequisites**
--------------------

Before creating a Compensatory Leave Request, it is necessary to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Leave Type](https://docs.frappe.io/hr/leave-type)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)
* [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)
* [Attendance](https://docs.frappe.io/hr/attendance)

**2. How to create a Compensatory Leave Request**
-------------------------------------------------

1. Go to Compensatory Leave Request list, click on New.
2. Select the Employee ID. Once selected, The Employee Name and Department will get automatically fetched.
3. Select Leave Type.
4. Select Work From Date and Work End Date. This is the date of the day(s) the Employee has worked on, during a Holiday.
5. Enter the Reason.
6. Save and Submit.

![Compensatory Leave Request](https://frappehr.com/files/compensatory-leave.png)

On submitting the Compensatory Leave Request, Frappe HR updates the Leave Allocation record for the Compensatory leave type, allowing the Employee to apply for leaves of this type later on depending upon the number of leaves left.

**3. Related Topics**
---------------------

1. [Leave Application](https://docs.frappe.io/hr/leave-application)
2. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
3. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)

  

<!-- page: frappe-hr/hr__configuring-earned-leave.md -->
---
title: "Configuring Earned Leave"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/configuring-earned-leave"
updated: "2026-02-04"
---

## **1. Prerequisites**

Before configuring Earned Leaves, it is required that you create the following first:

- Leave Type

![](https://frappehr.com/files/4KilVPP.png)

- Leave Period

![](https://frappehr.com/files/MI9ZPNM.png)

- Leave Policy

![](https://frappehr.com/files/CX0uqps.png)

- Leave Policy Assignment

![](https://frappehr.com/files/ZxOw5L4.png)

## **2. How to Configure Earned Leaves**

1. Creating a Leave Policy Assignment will result in the creation of associated Leave Allocations. These allocations will be automatically updated with leaves at intervals set by 'Earned Leave Frequency'.

![](/files/earned_leave_allocation.png)

<!-- page: frappe-hr/hr__create-payroll-entry-with-timesheets.md -->
---
title: "Create Payroll Entry with Timesheets"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/create-payroll-entry-with-timesheets"
updated: "2026-02-04"
---

**Use Case:** An employee's overtime is recorded using timesheets, and the employee needs to be compensated for the same during payroll apart from his usual salary.

**Steps:**

1) Create an Employee.

2) Create a Salary Component called "Overtime" of type Earning.

![](https://docs.erpnext.com/files/IKY5KnC.png)  


3) Create a Salary Structure and include "Overtime" with amount set to 0.

4) In the Salary Structure itself, select the "Salary Slip Based on Timesheet" checkbox, select Salary Component as "Overtime" and enter the Hour Rate.

![](https://docs.erpnext.com/files/RSBGOUP.png)  


5) Submit the Salary Structure and assign this Salary Structure to an Employee via Salary Structure Assignment.

![](https://docs.erpnext.com/files/qj9KVAu.png)  


6) Create Timesheets for this Employee through the Timesheet DocType.

![](https://docs.erpnext.com/files/xtdKq6i.png)  


![](https://docs.erpnext.com/files/W7vYYWt.png)  


In the above example shown, the Employee has worked overtime for a total of 8 hours in the month of January.

  


7) Create a new Payroll Entry for the month of January and select the "Salary Slip Based on Timesheet" checkbox. Save. Click on the "Get Employees" button. Next, click on "Create Salary Slips".

  


The Salary Slip of the employee will fetch all the timesheets (if any) of that employee created for that particular month and calculate the Overtime Component in the Salary Slip accordingly.

![](https://docs.erpnext.com/files/oZ1rr5x.png)  


![](https://docs.erpnext.com/files/1QoJVGc.png)  


  


  

<!-- page: frappe-hr/hr__daily-work-summary-group.md -->
---
title: "Daily Work Summary Group"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/daily-work-summary-group"
updated: "2026-02-04"
---

**In order to facilitate daily reporting of employees, you can configure Frappe HR to request employees to send their work summaries through email. Daily Work Summary is an automated way of getting the daily work reporting of employees in an organization.**

To configure a new Daily Work Summary Group, go to:

> Human Resources > Settings > Daily Work Summary Group

You can set multiple groups with different set of 'Users' from your user list with different 'Send Emails At' time and with separate 'Holiday List' for each.

You can also choose to customize the 'Message' you send to users.

**1. Prerequisites**
--------------------

Before creating a Daily Work Summary Group, it is necessary you create the following:

* [Email Account](https://docs.erpnext.com/docs/user/manual/en/email-account)

**2. How to create a Daily Work Summary Group**
-----------------------------------------------

1. Go to: Daily Work Summary Group > New.
2. Enter the name of the Daily Work Summary Group.
3. Enter the User's names in the 'Users' table.
4. Set the 'Send Emails At' time. This is the time the Daily Work Summary email will be sent.
5. Select Holiday List (optional). On these days, the Daily Work Summary email won't be sent.
6. In the Reminder section, enter the mail Subject and type in the Message.
7. Save.

>**Note:**

>1. If no Holiday List is selected, then the email will be sent every day. >2. Name of the "Daily Work Summary Group" will be sent as the title for daily summary email. >3. Mail will not be sent to the users of a disabled Daily Work Summary Group.

![Daily Work Summary Group](/files/Screenshot%202024-11-12%20at%2011.54.59%E2%80%AFAM.png) 


  

<!-- page: frappe-hr/hr__department-wise-leave-approval-in-erpnext.md -->
---
title: "Department-wise Leave Approval in ERPNext"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/department-wise-leave-approval-in-erpnext"
updated: "2026-02-04"
---

Any user with role, "Leave Approver" should be only able to access leave applications of those employees that belong in their department. This is a common use-case in most companies, and with some quick configurations, we can achieve it in Frappe HR.

**In company "SX4", let's consider Chris as the Leave Approver for department, "Research And Development". With this configuration, Chris will only be able to view Leave Applications raised by his department.**

1. Under Role Permissions Manager, provide this role with access of Department DocType

[![18](https://discuss.erpnext.com/uploads/default/original/3X/a/8/a8242a2ee2e82cd47b76d264eed601f474bd5142.png)](https://discuss.erpnext.com/uploads/default/original/3X/a/8/a8242a2ee2e82cd47b76d264eed601f474bd5142.png)  


2. Create the user in Frappe HR with Role as “Leave Approver”, and Employee In our example, this is Chris.

[![image](https://discuss.erpnext.com/uploads/default/original/3X/a/8/a8242a2ee2e82cd47b76d264eed601f474bd5142.png)](https://discuss.erpnext.com/uploads/default/original/3X/4/c/4c9dd72505cccbb8d35bb323d1e63fd960f6cfb1.png)  


![](https://docs.erpnext.com/files/L2uZrLq.png)  


3. Now, create the necessary user permissions as per Company, Department, and Employee.

[![image](https://discuss.erpnext.com/uploads/default/original/3X/4/a/4a100efbc5a42bdee7817fdc89e9d4f5f2f60227.png)](https://discuss.erpnext.com/uploads/default/original/3X/4/a/4a100efbc5a42bdee7817fdc89e9d4f5f2f60227.png)  


While adding the "Employee" permission for Chris, just keep Leave Application unchecked, so that Chris has access to only view other employees

![](https://docs.erpnext.com/files/4CoBHlZ.gif)  


4. Department: Set a “Leave Approver” in the Department master

[![image](https://discuss.erpnext.com/uploads/default/original/3X/5/c/5cabba46854752f07d9ed269ab7a3b0cf53baf26.png)](https://discuss.erpnext.com/uploads/default/original/3X/5/c/5cabba46854752f07d9ed269ab7a3b0cf53baf26.png)  


-------------------------------------------------------------------------------------------------------------------

Now, let’s say, we have an employee called Pepper who works in the “Research and Development” Department.

[![image](https://discuss.erpnext.com/uploads/default/original/3X/8/a/8a3ebb9644069224c31180fbbd816775f54aea2e.png)](https://discuss.erpnext.com/uploads/default/original/3X/8/a/8a3ebb9644069224c31180fbbd816775f54aea2e.png)  


6. Pepper fills in a leave application.

[![image](https://discuss.erpnext.com/uploads/default/original/3X/c/f/cf8418b1278c5bd6c89ff5a86a1412049e7bd109.png)](https://discuss.erpnext.com/uploads/default/original/3X/c/f/cf8418b1278c5bd6c89ff5a86a1412049e7bd109.png)  


7. When the Leave Approver, Chris, logins, he can only access the leaves raised by employees of his department.

[![](https://dl.dropboxusercontent.com/s/lfqeaivl50ixt5l/la-dept-1.gif?dl=0)](https://dl.dropboxusercontent.com/s/lfqeaivl50ixt5l/la-dept-1.gif?dl=0)  


8. Meanwhile, when we login via System Manager, there are few other Leave Applications in the list, too.

![](https://docs.erpnext.com/files/JTXLFmW.png)  


PS. We have assumed that the reader knows how to manage different leaves and allocations in Frappe HR. To explore that again, click [here](https://erpnext.com/docs/user/manual/en/human-resources)

Thanks for your time! ;-)

<!-- page: frappe-hr/hr__department.md -->
---
title: "Department"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/department"
updated: "2026-02-04"
---

**A Department is a specialized functional area or a division within an organization.**

You can configure the Departments in your organization, set Leave Block List, and also Leave and Expense Approvers for the same.

To access Department, go to:

> Home > Human Resources > Employee > Department

Department is a tree-structured master, which means you can create parent departments and sub-departments as shown below:

![Department Tree](https://frappehr.com/files/department-tree.png)  


> **Note:** The 'Is Group' checkbox needs to be checked if the Department is a parent department.

**1. Prerequisites**
--------------------

Before creating a Department, it is advisable you create the following documents:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)

**2. How to create a Department**
---------------------------------

1. Go to the Department list, click on New.
2. Enter Department name.
3. Select Company name.
4. Select Leave Block List (optional) applicable for this department.
5. Save.

![Department](https://frappehr.com/files/department.png)

**3. Features**
---------------

### **3.1 Leave and Expense Approvers**

You can set Leave and Expense Approvers for a particular Department in the 'Leave Approver' and 'Expense Approver' table respectively.

![Leave and Expense Approver](https://frappehr.com/files/leave-and-expense.png)  


> **Note:** Multiple Leave and Expense Approvers can be set for a particular Department. However, the first Approver in the list will be set as the default Approver.

**4. Related Topics**
---------------------

1. [Employment Type](https://docs.frappe.io/hr/employment-type)
2. [Employee Grade](https://docs.frappe.io/hr/employee-grade)
3. [Employee Branch](https://docs.frappe.io/hr/branch)
4. [Employee Designation](https://docs.frappe.io/hr/designation)

<!-- page: frappe-hr/hr__designation.md -->
---
title: "Designation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/designation"
updated: "2026-02-04"
---

**Designations are the official job titles given to employees.**

With reference to company management, there are various stakeholders like directors, officers, managers and shareholders who guide a company towards the fulfillment of its business objectives.

Frappe HR allows you to create various designations and also mention the skills required for the same.

To access Designation, go to:


> **Home > Human Resources > Employee > Designation**
> 
> 

**1. How to create a Designation**
----------------------------------

1. Go to Designation list, click on New.
2. Enter the Designation name.
3. Enter Description and Required Skills (optional).
4. Save.

![Designation](https://frappehr.com/files/designation.png)


> **Note: The skills required for an Employee of a particular Designation that are specified in the "Required Skills" section of the Designation doctype can be directly fetched in the** [**Employee Skill Map**](https://docs.frappe.io/hr/employee-skill-map) **to evaluate an employee's performance based on his skills.**
> 
> 

**3. Related Topics**
---------------------

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Employment Type](https://docs.frappe.io/hr/employment-type)
3. [Branch](https://docs.frappe.io/hr/branch)
4. [Department](https://docs.frappe.io/hr/department)
5. [Employee Grade](https://docs.frappe.io/hr/employee-grade)
6. [Employee Skill Map](https://docs.frappe.io/hr/employee-skill-map)

  

<!-- page: frappe-hr/hr__earned-leaves.md -->
---
title: "Earned Leaves"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/earned-leaves"
updated: "2026-02-26"
---

Earned leaves are special type of leaves that are credited or earned regularly after certain intervals. You can configure earned leaves from leave type. Once the leave type is configured as earned leave, you'll need to create the following.

- Leave Period

![](https://frappehr.com/files/MI9ZPNM.png)

- Leave Policy

![](https://frappehr.com/files/CX0uqps.png)

- Leave Policy Assignment

![](https://frappehr.com/files/ZxOw5L4.png)

## **2. Earned Leave Schedule**

1. Creating a Leave Policy Assignment will result in the creation of associated Leave Allocations. The allocation for earned leave will display the schedule upfront for the days the leaves will be credited.
2. Successfully credited leaves will be indicated in green.
  ![](https://docs.frappe.io/files/Screenshot 2026-01-08 at 12.06.41.png)
3. If for any reason the background job fails to credit the leaves, an email will be sent to the HR managers with a list of allocations that failed. The HR managers will see an option to retry failed allocations right from the leave allocation.

![](/files/Arc 2025-06-01 21:43:37 - Frame 215.png)

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

![](https://frappehr.com/files/tHvOj5m.png)

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

![](https://frappehr.com/files/BJIr6RK.png)  


#### **Employee Advance Payment via Journal Entry**

Alternatively, a [Journal Entry](https://docs.erpnext.com/docs/user/manual/en/journal-entry) can also be created against the Employee Advance.

![Employee Advance Payment via Journal Entry](https://frappehr.com/files/employee-advance-journal-entry1.png)  


> Note: Make sure the Party Type is selected as Employee and the Reference Type is selected as Employee Advance.

![Employee Advance Payment via Journal Entry](https://frappehr.com/files/employee-advance-journal-entry2.png)  


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

* If amount is unused, click on the **Return** button to return the paid Advance amount ![Return Button](https://frappehr.com/files/advance-return-button.png)
* If all of the advance is used, it will reflect in the Claimed Amount field
* If only some amount is claimed and rest is returned, the returned amount will be shown in the 'Returned Amount' field. ![Return advance Amount](https://frappehr.com/files/advance-returned-amount.png)

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

![](https://frappehr.com/files/pOo6Zsf.gif)  



> **Note: Attendance cannot be marked for future dates.**
> 
> 

Once the attendance is marked using the Employee Attendance Tool, the employee attendance is saved in the [Attendance](https://docs.frappe.io/hr/attendance) record as shown:

![](https://frappehr.com/files/dxhxNaV.png)  


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

![Employee Benefit Application](https://frappehr.com/files/employee-benefit-application.png)  


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

![Employee Benefit Claim](https://frappehr.com/files/employee-benefit-claim.png)  


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

![](/files/qkGD7oD.png)  


If auto attendance is enabled, the attendance record marked for a set of check-ins will be linked to the document later.

#### **2.2 Integrating Frappe HR with Biometric Devices**

If you are using a Biometric Device to log employee check-ins and check-outs you can use it to create records in Frappe HR. You can read more about this [here](https://docs.frappe.io/hr/integrating-frappe-hr-with-biometric-attendance-devices).

**3. Features**
---------------

### **3.1 Geolocation Tracking**

You can also track geolocation in employee checkins. To enable this, go to HR Settings and enable "**Allow Geolocation Tracking**"

![](https://frappehr.com/files/UqR7S9c.png)  


You can then click on the "**Fetch Geolocation**" button in the check-in form to fetch your current location

![geolocation-desk](https://frappehr.com/files/geolocation-desk.gif "geolocation-desk.gif")  


It geolocation tracking has been enabled, it will be automatically captured while checking in from the mobile app too

![geolocation-mobile](https://frappehr.com/files/geolocation-mobile.gif "geolocation-mobile.gif")  
### **3.2 Checkin log indicator**

Employee checkins fetch appropriate shift while saving based on the time of checkin or checkout log. If there is no active shift asssociated for the time of log, the employee checkin log is marked as **Off-Shift** indicating the lack of associated shift. Since auto-attendance works based on shift, these checkin logs are excluded while marking auto-attendance.


![](/private/files/Screenshot%202025-07-11%20at%2011-06-45%20Jane%20Doe%20-%20EMP-CKIN-07-2025-000001.png)

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

![](/files/Screenshot%202025-09-18%20at%208.42.25%E2%80%AFPM.png)
---

## Employee Benefit Application

* Employees can opt for the benefits they want from those assigned in their Salary Structure Assignment.
* If no Benefit Application exists, the system falls back to the Salary Structure Assignment.
* To make a Benefit Application mandatory, enable **Mandatory Benefit Application** in Payroll Settings.

<img width="956" height="358" alt="Screenshot 2025-09-18 at 3 43 12 PM" src="https://github.com/user-attachments/assets/a3938f4f-2ac5-4f75-889b-4672f0d73dbe">

---

## Employee Benefit Ledger

* In the Salary Slip:

  * **Accrued Benefits** appear in the *Accrued Benefits* table.
  * **Payouts** appear as *Earnings*.
  * 
![](/files/Screenshot%202025-09-18%20at%208.44.32%E2%80%AFPM.png)

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

![](/files/Screenshot%202025-09-18%20at%208.48.27%E2%80%AFPM.png)

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

![Employee Grade](https://frappehr.com/files/employee-grade.png)

Shown below are the different Employee Grades created.

![New Employee Grade](https://frappehr.com/files/employee-grade1.png)  


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

![Employee Group](https://frappehr.com/files/employee-group.png)

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

![Employee](https://frappehr.com/files/health-insurance.png)

Additionally, in the Employee master, you can attach the Health Insurance Provider Name and fill in the Health Insurance No.

![Employee](https://frappehr.com/files/employee-health-insurance.png)  


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

![Employee Incentive](https://frappehr.com/files/employee-incentive.png)

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

![Onboarding Template](https://frappehr.com/files/employee-onboarding1.png)

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

![Onboarding Template](https://docs.erpnext.com/files/onboarding-template972e99.png)

### **3.2 Tasks and Assignments**

On submission of the Employee Onboarding, a [Project](https://docs.erpnext.com/docs/v143/user/manual/en/projects/project) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v143/user/manual/en/projects/tasks) will also be created for each Activity. If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.

You can view the created Projects and Tasks as shown below:

![Onboarding Template](https://frappehr.com/files/project-task.png)  


Additionally, each Activity can be assigned weights based on its importance.

![Tasks and Assignments](https://frappehr.com/files/employee-onboarding3.png)  


Based on the progress on the Tasks, progress can be updated in the Employee Onboarding process.

### **3.3 Employee Creation**

You can directly create an Employee through the Employee Onboarding doctype (if not already created) once all the mandatory onboarding tasks are complete.

![Onboarding Template](https://frappehr.com/files/onboarding-employee.png)  


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

![Employee Other Income](https://frappehr.com/files/employee-other-income.png)  


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

![add feedback](https://frappehr.com/files/add-feedback.png)  


For more details about the feedback timeline check [Appraisal](https://docs.frappe.io/hr/appraisal#32-feedback)

### **2.2 Direct creation**

1. Go to the Employee Performance Feedback list, and click on New.
2. Select the Employee.
3. If your session user is linked to some employee, that employee will be auto-selected as the reviewer. Else you can select the reviewer.
4. Select the Appraisal document against which you want to give the feedback.
5. The feedback criteria set in the Appraisal Template in the Appraisal document will be pulled into the Feedback Ratings child table.
6. You can rate the employee for each criteria and add your feedback under the feedback.
7. Save and Submit.

![perf feedback](https://frappehr.com/files/perf-feedback.png)  


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

![Employee Promotion](https://frappehr.com/files/employee-promotion.png)

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

![employee referral doc](https://frappehr.com/files/employee-referral-doc.png)  


**3. Features**
---------------

### **3.1 Creating Job Applicant and auto-syncing status from Job Applicant**

When you submit an employee referral document the initial status will be "Pending". After submitting the document, the "Create Job Applicant" button will appear at the top right corner.

Clicking this button will create a new **Job Applicant** with the status "Open". The status of the **Employee Referral** document will change to "In Process"

![Create Job Applicant](https://frappehr.com/files/create-job-applicant.png)  


When someone changes the status of the **Job Applicant** to "Hold" or "Replied", the status of the Employee Referral will remain "In Process". If the status of the Job Applicant changes to "Accepted" or "Rejected", the status of the **Employee Referral** document will also change to "Accepted" or "Rejected" respectively.

### **3.2 Managing referral bonus**

Many companies provide bonuses to their employees for such referrals. Frappe HR allows you to track the payment of the bonus to the employee for their referral.

For the Referral bonus, you need to check the "Is applicable for referral bonus" checkbox before submitting the document. After submitting the document, the "Create Additional Salary" button will appear at the top right corner, if the status is "Accepted".

![Referral Bonus](https://frappehr.com/files/referral-bonus.png)  


On Click, It will redirect you to the Additional salary form where you need to select Salary component and Payroll date and after that, you need to save and submit the document.

![Create Referral Bonus](https://frappehr.com/files/create-referral-bonus.png)  


  

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

![Separation Template](https://frappehr.com/files/employee-separation.png)

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

![Separation Template](https://docs.erpnext.com/files/separation-template.png)

### **3.2 Tasks and Assignments**

On submission of the Employee Separation, a [Project](https://docs.erpnext.com/docs/v13/user/videos/learn/project-and-task) will be created. Within the Project, [Tasks](https://docs.erpnext.com/docs/v13/user/videos/learn/project-and-task) will also be created for each Activity. If you have set the date and duration against activities, tasks will be created with appropriate Start and End Date excluding holidays.

You can view the created Projects and Tasks through View > Project/ Tasks.

Additionally, each Activity can be assigned weights based on its importance.

![Tasks and Assignments](https://frappehr.com/files/employee-sep1.png)  


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

Example of Skills for a Designation: ![Designation Skills](https://frappehr.com/files/designation-skills.png)  


**1. How to create an Employee Skill Map**
------------------------------------------

1. Go to the Employee Skill Map list, click on New.
2. Select the Employee.
3. Based on the designation of the Employee system will pull the Skills. Set the Proficiency level out of 5, and the Evaluation Date.
4. If the Employee is lacking in any skill, you can schedule trainings for the Employee.
5. Under the Trainings table, select the Training Event and the Training Date.
6. Save.

![Employee Skill Map](https://frappehr.com/files/employee-skill-map.png)  


  

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

<!-- page: frappe-hr/hr__how-to-process-payroll-in-frappehr.md -->
---
title: "How to process Payroll in Frappe HR"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/how-to-process-payroll-in-frappehr"
updated: "2026-02-09"
---

Most of the users find it difficult to process payroll in Frappe HR, but rather than it being difficult, it is a bit tedious in the initial setup. Once, the setup is done it, the process for the following months becomes easy. Kindly go through the below steps for a quick guide:

**1) Create Payroll Period**

In this, you define a period for which you want to process the payroll for. It could be January to December or April to March as per the year followed by your company.

**2) Create Income Tax Slabs**

Over here, you can create multiple Income Tax slabs if you are following the Indian Income Tax system. Define the slabs as per the government rule. You can also add additional tax in the section below and conditions in the table if required and also check 'Allow Tax Exemption' in case there is a standard deduction applicable.

![](https://docs.erpnext.com/files/J2NBGym.png)  


**3) Submit Employee Tax Exemption Declaration**

An employee who has some investments can submit tax declarations to avail tax benefits and thus can reduce their Income Tax amount. They can invest in various sub categories under 80C, 80D, etc. (Applicable for Indian Taxation).

**4) Define Salary Components**

You can create salary components and define whether the component is an Earning or a Deduction component. There are certain checkboxes that you can check depending on the component type. Select the company and a default ledger account. Now, these salary components can be based on a particular formula or it can be a fixed amount. Only for Income Tax component you need to check a particular checkbox called "Variable based on Taxable Salary". This will ensure that the Income Tax is calculated automatically in the backend.

**5)Create a Salary Structure**

Once you have created all the salary components, you can define a salary structure. You can also define whether the salary is based on timesheets. You can add the earnings and deductions as per your choice and the mode of payment.

![](https://docs.erpnext.com/files/AnuaBH8.png)  


**6) Assign the Salary Structure**

Once the salary structures have been created, you need to assign it to employees. If you miss this step, then you will not be able to proceed further. During assignment, you have to select the Income Tax Slab (if you have multiple slabs), since the percentage deduction of Income Tax will be calculated based on the same. You can also define a base amount if your salary structures are based on formulas.

![](https://docs.erpnext.com/files/Zg8nsfS.png)  


**7) Create a Payroll Entry & Salary Slips**

Once all of the above steps are done, you need to create a payroll entry. Once you have selected the payroll date, frequency and added the payment account, you can filter employees on the basis on department, designation and branch. If you do not wish to do so then you can directly click on 'Get employees'. On doing so, a list of all the employees will populate in the Employee Details section. You can then proceed by clicking on "Create Salary Slips" and all the salary slips will be generated in draft.

![](https://docs.erpnext.com/files/HQAMnYm.png)  


You can verify the draft salary slips and then submit them via the payroll entry. On submitting the salary slips, an accrual journal entry will be created. This means we are booking the salary expenses in the system and not paying them. 


![](https://docs.erpnext.com/files/z7DIBpo.png)  


**8) Bank Entry**

Once you have booked the accrued salary slips, as a last step you need to make a Bank Entry. With this last step, your payroll process is completed, but this does not mean the salaries are transferred in the bank. That minor step has to be done manually.

![](https://docs.erpnext.com/files/iOrcSFs.png)  

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

![Previous Work Experience](https://frappehr.com/files/hr-settings1.png)  


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

![Previous Work Experience](https://frappehr.com/files/hr-settings2.png)  


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

**![](https://lh7-us.googleusercontent.com/A9IyXp8Eyjcnl4aVb164XrJ-bE-senEbgybURCe9zXcvMAKbzj-wXdCNPNgBc8xyWvpCBDQrXnHfMv5827Q6nFb2tEj-zwLnYtsuSpuaTbyKdqFOhenGoOsqQRydhWMbIalDoshnR1Lh)**  


### **3.1 Allow Multiple Shift Assignments for Same Date**

Enabling this allows the user to create Shift Assignments for an employee with pre-existing Assignments on any of the dates within the selected range, and vice versa.

**4. Leave Settings**
---------------------

![Previous Work Experience](https://frappehr.com/files/hr-settings3.png)  


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

![image](https://user-images.githubusercontent.com/24353136/135511758-4300b29e-78c2-4492-a6a7-d75d0632fd5a.png)  


### **5.1 Check Vacancies On Job Offer Creation**

On the creation of a job offer for a particular position, vacancies present in the staffing plan for that position are checked to warn the user from over hiring for a particular position.

### **5.2 Send Interview Reminder**

Enabling this will send a reminder email to all the Interviewers associated with the Interview Round of an upcoming Interview. This mail will be scheduled according to the Remind Before field set by the user.

### **5.2 Send Interview Feedback Reminder**

Enabling this option will trigger reminder emails to be sent to Interviewers who are associated with a conducted Interview Round but haven't yet submitted their Feedback for it.

**6. Mobile Settings**
----------------------

![Screenshot 2024-04-08 at 2 49 50 PM](https://private-user-images.githubusercontent.com/52369157/320425819-5d05a9e1-7df9-4cc8-ad02-b90f2e383159.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTI4MzEyNjksIm5iZiI6MTcxMjgzMDk2OSwicGF0aCI6Ii81MjM2OTE1Ny8zMjA0MjU4MTktNWQwNWE5ZTEtN2RmOS00Y2M4LWFkMDItYjkwZjJlMzgzMTU5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA0MTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNDExVDEwMjI0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIxNzBmYTA4MjI1NWY2ZjZiY2FmMDkwOTFjMDFiNjA3ZGVhNGQ3ODczOTFhNDg5YTM1ZTZlYjhjMDU4MDdiYjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.MARRAtci4sfl2GJEgPWhvmwmu2O0oLu952O19A8jw_8)  


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
  ![](/files/Screenshot From 2026-01-08 13-07-48.png)

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
  ![](/files/Screenshot 2026-01-08 at 12.37.40.png)
3. Set adjustment type either allocate new leaves or reduce from the allocation, number of leaves to adjust and click on **Adjust Leaves.**
  ![](/files/Screenshot 2026-01-08 at 12.42.20.png)
4. A new leave adjustment document will be created to correct the existing leave allocation.
  ![](/files/Screenshot 2026-01-08 at 12.43.28.png)

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

![Employee Leave Balance](https://frappehr.com/files/employee-leave-balance.png)  


**2. Salary Register**
----------------------

Salary Register shows net pay and its components of employee(s) at a glance.

![Monthly Salary Register](https://frappehr.com/files/monthly-salary-register.png)  


**3. Monthly Attendance Sheet**
-------------------------------

Monthly Attendance Sheet shows you the employee-wise attendance status. If you assign shifts to employees, this sheet will also show you shift-wise attendance for each employee.

![Monthly Attendance Sheet](https://frappehr.com/files/monthly-attendance-sheet.png)  


If you do not want to see day-wise attendance, and get a summarized view of total absent, present, leave days, etc. you can switch to the summarized view:

![Monthly Attendance Sheet](https://frappehr.com/files/monthly-attendance-summarized.png)  


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

![](https://frappehr.com/files/KBfhUlt.png)  


**5. Vehicle Expenses Report**
------------------------------

To track and monitor Vehicle Expenses you can use the Vehicle Expenses report. This report gives a one-stop view of all your Vehicle Expenses month-wise.

![Vehicle Log](https://frappehr.com/files/vehicle-expenses-report.png)  


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

![Monthly Salary Register](https://frappehr.com/files/employee-exits.png)  


**7. Employee Birthday**
------------------------

Employee Birthday Report shows month-wise birthdays of your Employees.

![Employee Birthday](https://frappehr.com/files/employee-birthday.png)  


**8. Employee working on a holiday**
------------------------------------

Employee Holiday Attendance shows the list of Employees who attended on Holidays.

![Employee Working on a Holiday](https://frappehr.com/files/employees-working-on-a-holiday.png)  


**9. Bank Remittance Report**
-----------------------------

This report helps you to track bank transactions of payroll entries between companie(s) and employees. It shows the transaction between the bank accounts of the Company and the Employee with the Payment Date.

![Monthly Salary Register](https://frappehr.com/files/bank_remittance_report.png)  


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

  
![](https://docs.erpnext.com/files/K0DGKxb.png)  


* While creating salary component of Income Tax, check the box "Variable Based On Taxable Salary". Ticking this checkbox means, income tax will be calculated automatically taking the payroll period and tax declarations into consideration.

  


* Create a salary structure and add Income Tax in the deduction section leaving the amount section blank. Along with that kindly add Education cess which will be based on a formula. Screenshot attached:

![](https://docs.erpnext.com/files/paJO8Kk.png)  


* Create a payroll entry and generate salary slips. Income tax will be calculated automatically along with the education cess. Screenshot attached:

![](https://docs.erpnext.com/files/svhgWSq.png)  


  

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

![Income Tax Slab](https://frappehr.com/files/income-tax-slab.png)  


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

![Other Charged on Income Tax](https://frappehr.com/files/other-taxes-on-income-tax.png)  


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

![](/files/image363911.webp)
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

![](/files/imagec6a7e8.webp)

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

![](/files/image691bee.webp)
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

![](/files/image6540b3.webp)

> **Key behaviour:** The `lwf_exempted` flag is **never auto-overridden** by the hook. Only an HR user with write access to the Employee document can change it. This ensures manual exemptions are preserved across all payroll runs.

---
