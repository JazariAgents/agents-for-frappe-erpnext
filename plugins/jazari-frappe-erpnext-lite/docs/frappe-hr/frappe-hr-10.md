<!-- Frappe documentation: frappe-hr, part 10 of 10. Index: docs/INDEX.md -->

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

[Screenshot on the live page]  


You can also mention the Travel Itinerary as well as the costs involved for the trip. Employees can also check `Travel Advance Required` if they wish to receive any upfront payment form the company.

[Screenshot on the live page: Travel Request Itinerary]  


  

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

 [Screenshot on the live page: Attendance Template]

1. Enter the Status (Present / Absent) of the Employee for the selected dates.
1. Save the file.
1. Upload the saved file.


 [Screenshot on the live page: Attendance upload]


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

[Screenshot on the live page]  


**Employee Hierarchy**

Also, one a User is linked with the Employee, it creates a User Permission as follows. As per this User Permission, Employee will be allowed to review his/her own document created in the HR module + the document which are created for Employees reporting to hm/her.

[Screenshot on the live page]  


As per this configuration, when an Expense Claim is being created by the User reporting to Kenneth, it will also be accessible to Kenneth as well.

[Screenshot on the live page]  


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

[Screenshot on the live page] 


1. Set the time carefully for log type **IN** and **OUT.**
2. For Log Type **IN** time should be greater than **Shift Type Start Time - Begin check-in before shift time**
3. For Log Type **OUT** time should be less Than **Shift Type End Time + Allow check-out after shift end time.**
4. Then only Shift would be mapped properly and your Checkin is valid.

B. Check your shift type:

[Screenshot on the live page]  


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

[Screenshot on the live page]

5. Additionally, Vehicle Service Details can also be added as shown (optional).

[Screenshot on the live page]

6. Save. Once the information is saved, the Model and Make values will be automatically fetched.

## **3. Features**

Fleet Management in Frappe HR allows you to automatically create an [Expense Claim](https://docs.frappe.io/hr/expense-claim) against your Vehicle Expenses.

### **3.1 Make Expense Claim against Vehicle Expenses**

Click on Create Expense Claim button. This button appears only in case of Submitted Vehicle Logs.

[Screenshot on the live page]



When you click on 'Make Expense Claim',

1. The Date, Employee, Expense total are fetched over to the created Expense Claim.
2. The sum of Fuel Expenses and Service Expenses is calculated and fetched over to Expense Claim Amount.
3. Employee can submit the Expense Claim for further processing.

[Screenshot on the live page]

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

[Screenshot on the live page: Vehicle]

**2. Features**
---------------

Apart from the aforementioned mandatory features, some additional features that can be captured in the Vehicle master are as follows:

### **2.1 Additional Vehicle Details**

Additional Vehicle details such as Chassis No., Acquisition Date, Vehicle Value (Amount), Location, Employee managing the Vehicle and Insurance details can be captured in the Vehicle master.

[Screenshot on the live page: Vehicle]  


### **2.2 Vehicle Attributes**

Additionally, Vehicle attributes like Color, Wheels, Door, Last Carbon Check, Fuel Type and UOM can be saved in the Vehicle master.

[Screenshot on the live page: Vehicle]  


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

[Screenshot on the live page: Role Desk Permission]  


To learn how to define holidays for your company, check [Holiday List](https://docs.frappe.io/hr/holiday-list) feature in the HR module.

  
