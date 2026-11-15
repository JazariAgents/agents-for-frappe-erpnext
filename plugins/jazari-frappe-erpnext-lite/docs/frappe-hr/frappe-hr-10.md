<!-- Frappe documentation: frappe-hr, part 10 of 10. Index: docs/INDEX.md -->

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

  
