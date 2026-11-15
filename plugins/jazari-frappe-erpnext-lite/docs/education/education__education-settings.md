---
title: "Education Settings"
space: "Education"
url: "https://docs.frappe.io/education/education-settings"
updated: "2026-02-09"
---

**The Education Settings will allow you to do a basic setup for your Institute wherein you can define the Academic Year, Academic Term, and other defaults for your ERPNext account.**

These configuration settings will have an impact throughout the module.

To access Academic term, go to:


> Home > Education > Settings > Education Settings
> 
> 

1. Steps to configure Education Settings
----------------------------------------

1. Select the current Academic Year. This will become the default Academic Year throughout your account.
2. Select the current Academic Term. This will become the default Academic Term throughout your account.
3. Select the Attendance Freeze date. Any attendance captured after the Attendance Freeze Date would not be valid.
4. Select how you want the Instructor Records to be created, using Full Name, using Naming series or using Employee Number.
5. **Instructor Record to be created by**: You can select how you want the Instructor Records to be created in your ERPNext system, whether it should be by Full Name, by Naming series, or by Employee Code.

  


![edu_settings](/files/edu_settings.png)

### 1.1. Configuring Properties

* **Validate Batch for Students in Student Group**: When adding students to a student group via Batch, the system will verify whether the student belongs to that batch or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Validate Batch for Students in Student Group**: When adding students to a student group via Course, the system will verify whether the student is enrolled to that course or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Make Academic Term Mandatory**: When enabled, this option will ensure that while creating a Program Enrollment via the [Program Enrollment Tool](/education/program-enrollment-tool), the user has to enter the Academic Term.
* **Skip User Creation for New Student**: Whenever a new student is created, by default a User is created against it. If this option is enabled, no new User will be created when a new Student is created. For giving Portal access to the students this needs to be disabled, else the user will not be created and the student can't login to the portal.
* **Submit Sales Invoice from Program Enrollment / Fee Schedule:** When creating a Sales Invoice from either a Program Enrollment or Fee Schedule, if disabled then the Sales Invoice will br created in "Draft" Mode, if enabled it will be"Submitted".
* **Sales Invoice Posting Date should be same as Fee Schedule Posting Date:** By default, the Sales Invoice's Posting Date will be equal to Fee Schedule's Posting Date. If disabled then Sales Invoice's Posting Date will be today's date.

### 1.2. Portal Settings

The Education module is bundled with a Student Portal from v15.2.0 onwards.

![edu_settings1](/files/edu_settings1.png)  


* **Attendance Based on Course Schedule:** From Portal if the student applies for a leave, the attendance is marked based on this setting. If disabled the attendance will be marked for the whole day and if enabled the attendance will be marked for all the course schedule on which the student has applied for leave.
* **Razorpay Key & Razorpay Secret:** To collect Fees from students via portal these 2 settings needs to be there to connect the payment gateway to your account.
* **School / College Name Abbreviation:** Add your Institute's Abbreviation here, which will be displayed on the Student Portal
* **School / College Logo:** Upload your Institute's Logo here, which will be displayed on the Student Portal.
