<!-- Frappe documentation: frappe-hr, part 1 of 10. Index: docs/INDEX.md -->

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
