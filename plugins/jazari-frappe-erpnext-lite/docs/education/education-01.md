<!-- Frappe documentation: education, part 1 of 2. Index: docs/INDEX.md -->

<!-- page: education/education__academic-term.md -->
---
title: "Academic Term"
space: "Education"
url: "https://docs.frappe.io/education/academic-term"
updated: "2026-02-09"
---

**An Academic Term would become a part of the Academic Year, during which the Institute will assess its Students on the curriculum defined for that term. It could be a Quarter, Trimester or a Semester.**

To access Academic term, go to:


> Home > Education > Settings > Academic Term
> 
> 

The **Academic term** form in ERPNext enables you to create academic terms within in an Academic Year. Based on the term schedule enter the start and end date for the schedule and generate the Academic Term.

[Screenshot on the live page: KzzYqR0]  


  


If the Academic Term has been specified in the [Education Settings](/education/education-settings) then it will become the default Academic Term in all the forms and will be editable if required.

The following are the various forms where Academic Term is a relevant field:

1. Student Log
2. Student Group
3. Student Applicant
4. Student Admission
5. Program Enrollment
6. Assessment Plan
7. Assessment Result
8. Assessment Criteria
9. Fees
10. Fee Schedule
11. Fee Structure
12. Fee Category
13. Course Schedule

<!-- page: education/education__academic-year.md -->
---
title: "Academic Year"
space: "Education"
url: "https://docs.frappe.io/education/academic-year"
updated: "2026-02-09"
---

**An academic year is a period which the Educational Institutes, Schools and Universities use to measure a quantity of study.**

The **Academic year** form have the Start and End date for the Academic year.

Within an Academic Year, you can have multiple **Academic Terms**.

[Screenshot on the live page: Academic Year]  


An academic year can be further linked to a [Student group](/education/student-group), which can be created from an Academic Year.

[Screenshot on the live page: Academic Year]  


If the Academic Year has been specified in the [Education Settings](/education/education-settings) then it will become the default Academic Term in all the forms and will be editable if required.

The following are the various forms where Academic Year is a relevant field:

1. Student Log
2. Student Group
3. Student Applicant
4. Student Admission
5. Program Enrollment
6. Assessment Plan
7. Assessment Result
8. Assessment Criteria
9. Fees
10. Fee Schedule
11. Fee Structure
12. Fee Category
13. Course Schedule

<!-- page: education/education__assessment-introduction.md -->
---
title: "Assessment\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment-introduction"
updated: "2026-02-09"
---


Every education institute needs to have a well-defined assessment procedure to evaluate the students' curricular performance in a period. The complete assessment processing for your institute can be very easily mapped into and managed via ERPNext.

Following is the order in which you should set up the masters in the Assessment module.

1. Assessment Criteria
1. Assessment Group
1. Grading Scale

Once you have also defined the Student Group and Courses, you can schedule an assessment/examination by creating Assessment Plan.

Based on the performance of the Student in the assessment, you can create Assessment Result for a Student. You can create Assessment Results in bulk using the Assessment Result Tool. In this tool, on the selection of Assessment Plan, all the students (for Student Group) will be fetched. You can quickly enter marks earned by each Student for each Assessment Criteria in a single row.

<!-- page: education/education__assessment_criteria.md -->
---
title: "Assessment Criteria\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment_criteria"
updated: "2026-02-09"
---


**Assessment Criteria is the parameter based on which you assess the Student.**

[Screenshot on the live page: Assessment Criteria]

After an assessment is conducted for a Course, marks earned are entered based on the Assessment Criteria. For example, if the assessment was conducted for science subjects, then you can evaluate Student in Science on various criteria like Writing, Practicals, Presentation, etc.

Assessment Criteria can be used while scheduling Assessment Plan for Student Group and Course.

#### Video Tutorial on Assessment Criteria





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/t8ZDDq4qtIk?end=52">
</iframe>

<!-- page: education/education__assessment_group.md -->
---
title: "Assessment Group\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment_group"
updated: "2026-02-09"
---


**Assessment Group tree is a master where you can define the hierarchy for examination conducted in your education institute.**

For example, if you wish to conduct an assessment for each Academic Term within an Academic Year, then setup Assessment Group as follows.

[Screenshot on the live page: Assessment Group]

To access the Assessment Group, go to

> Home > Education > Assessment > Assessment Group

#### Video Tutorial on Assessment Group





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/I1T7Z2JbcP4">
</iframe>

<!-- page: education/education__assessment_plan.md -->
---
title: "Assessment Plan\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment_plan"
updated: "2026-02-09"
---


**An Assessment Plan is a schedule to conduct the examination/assessment of a particular course for a group of students studying that course in an on-going academic term.**

To access the Assessment Plan, go to

> Home > Education > Assessment > Assessment Plan

## 1. Prerequisites

Before creating an Assessment Plan, it is advisable that you create the following first:

1. [Student Group](/education/student-group)
1. [Course](/education/course)
1. [Program](/education/program)
1. [Assessment Group](/education/assessment_group)
1. [Grading Scale](/education/grading_scale)

## 2. How to create an Assessment Plan

1. Go to the Assessment Plan list and click on New.
1. Select the **Student Group** for which you want to conduct the assessment.
1. Select the **Course** for which you are conducting the assessment.
1. Select the **Assessment Group** under which the assessment is being conducted.
1. Once you select the course, the **Grading Scale** would automatically be updated for the assessment.
1. Save.

### 2.1. Additional Options while creating an Assessment Plan

Apart from the mandatory fields, you may also add the following details to the assessment plan:

1. **Assessment Name**: Enter the name for the assessment which is to be conducted. E.g., Assessment for Economics Core Course IV, Term I.
1. **Program**: Select the Program under which the assessment has been conducted.
1. **Academic Year and Academic Term**: Select and enter the Academic Year and the Academic Year for which the Assessment is being done.

[Screenshot on the live page: Assessment Plan]

## 3. Features

### 3.1. Schedule

1. **Schedule Date**: Enter the date on which the assessment is to be conducted.
1. **From Time**: Enter the start date for the assessment.
1. **To Time**: Enter the end time for the assessment.
1. **Room**: Select the room in which the assessment would be conducted.
1. **Examiner**: Add the name of the Examining Instructor for this assessment.
1. **Supervisor**: Add the name of the Supervising Instructor for this assessment.

[Screenshot on the live page: Assessment Plan]

### 3.2. Evaluate

Once you select the Course and the Grading Scale gets updated, you will be required to enter the Maximum Assessment Score and the Assessment Criteria would get automatically updated in the system.

[Screenshot on the live page: Assessment Plan]

#### Video Tutorial on Assessment Plan





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/Q9CzzoYb_Js">
</iframe>

<!-- page: education/education__assessment_result.md -->
---
title: "Assessment Result\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment_result"
updated: "2026-02-09"
---


**Assessment Result is a log of marks/grades earned by the student for specific Assessment.**

An Assessment Result is created in the backend based on the marks entered in the [Assessment Result Tool](/education/assessment_result_tool).

[Screenshot on the live page: Assessment Result]

#### Video Tutorial on Assessment Result




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/U8ZRB8CM-UM?end=89">
</iframe>

<!-- page: education/education__assessment_result_tool.md -->
---
title: "Assessment Result Tool\n"
space: "Education"
url: "https://docs.frappe.io/education/assessment_result_tool"
updated: "2026-02-09"
---


**Assessment Result Tool helps you entering marks earned by the Students for a specific course. In this tool, based on the Assessment Plan, all the Student will be fetched into the Assessment Result Tool.**

Also, Columns for Assessment Criteria will be where marks earned can be entered for each Student.

[Screenshot on the live page: Assessment Result Tool]

As you go on entering marks for a Student, and switch to the next student, in the backend, Student Result record will be auto-created for that Student.

#### Video Tutorial on Assessment Result Tool





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/U8ZRB8CM-UM?start=80">
</iframe>

<!-- page: education/education__course-schedule.md -->
---
title: "Course Schedule\n"
space: "Education"
url: "https://docs.frappe.io/education/course-schedule"
updated: "2026-02-09"
---


**Course Schedule can be used for scheduling a particular course by an Instructor.**

Using this feature, a time table or an itinerary can be created in the Institute, wherein each slot will be scheduled via Course schedule.

[Screenshot on the live page: Course Schedule]

To access Course schedule, go to:

> Home > Education > Schedule > Course Schedule

## 1. Prerequisites

Before creating a Course Schedule, it is advised that you create the following first:

1. [Student Group](/education/student-group)
1. [Instructor](/education/instructor)
1. [Course](/education/course)
1. [Program](/education/program)
1. [Room](/education/room)

## 2. How to create a Course Schedule

1. Create a new Course Schedule from the Schedule Calendar.
1. Select the **Student Group** for which you want to create the Course Schedule.
1. Select the **Instructor** who will be tutoring the students for the course.
1. Select the **Course** for which the schedule is being prepared.
1. Add the **From Time** and **To Time** for the Course Schedule.
1. Select and add the **Room** wherein the Lecture would be conducted.

[Screenshot on the live page: Course Schedule]

## 3. Marking Attendance

You can mark attendance for a Student Group against a Course Schedule.

[Screenshot on the live page: Course Schedule]

To mark attendance for a course, click on **Attendance** in the Course Schedule. You will be redirected to a page, wherein the name of all the students will be listed along with check-boxes for marking attendance. You can check the Present students and **Mark Attendance**. You can also **Check All** or **Uncheck All** and mark attendance.

[Screenshot on the live page: Course Schedule]

## 4. Video Tutorial on Course Scheduling



<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/iy-DBV9jI-A?start=0&amp;end=114">
</iframe>

<!-- page: education/education__course-scheduling-tool.md -->
---
title: "Course Scheduling Tool"
space: "Education"
url: "https://docs.frappe.io/education/course-scheduling-tool"
updated: "2026-02-09"
---

**A Course Scheduling Tool will allow you to create Course Schedules in bulk for a particular Student Group and an Instructor.**

[Screenshot on the live page: Course Scheduling Tool]  


To access the Course Scheduling Tool, go to:


> Home > Education > Schedule > Course Scheduling Tool
> 
> 

1. Prerequisites
----------------

Before creating a Course Schedule, it is advised that you create the following first:

1. [Student Group](/education/student-group)
2. [Instructor](/education/instructor)
3. [Course](/education/course)
4. [Room](/education/room)

2. How to create a Course Schedule using the Course Scheduling Tool
-------------------------------------------------------------------

1. Select and add the **Student Group**. Once you do this, the Academic Term, Academic Year the Program will be auto-populated.
2. Select and add the **Course**.
3. Select and add the **Instructor** whose lectures are being scheduled using the tool.
4. Select and add the **Room** wherein the lectures will take place.
5. Change the **From Time** and **To Time** to your desirable schedule.
6. Select the **Course Start Date** and the **Course End Date** for the Course Schedule.
7. Select the **Day** of the week on which the Course Lecture has to be scheduled.
8. Click on **Schedule Course** button, based on the dates selected and days for the course selected, the Tool will schedule the required course lectures.

[Screenshot on the live page: Course Scheduling Tool]  


3.**Rescheduling**
------------------

* If you wish to reschedule Course Schedules created against a Course, follow the instructions for creating course schedules
* Check the 'Reschedule' checkbox and then click 'Schedule Course' button.
* System will delete existing Course Schedules for specified Course within the mentioned Course Start Date and Course End Date and crate new Course Schedules.

4.**Video Tutorial on Scheduling Tool**
---------------------------------------

  





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/iy-DBV9jI-A?start=114">
</iframe>

<!-- page: education/education__course.md -->
---
title: "Course\n"
space: "Education"
url: "https://docs.frappe.io/education/course"
updated: "2026-02-09"
---


**A course can be considered as a subject or a part of an educational program which is to be taught for a term.**

For example, if for a particular term, Economics Major is a program taught in the institute, then Mathematical Methods for Economics would be a Course covered under the program.

[Screenshot on the live page: Course]

A course will have a set of [topics](/education/topic) that are to be covered under it's scope.

To access the course list, go to:

> Home > Education > Masters > Course

## 1. Prerequisites

Before creating a course, it is advised to create:

1. Department
2. Topics

## 2. How to create a course

1. Go to Course List and click on New.
2. Enter the Course Name.
3. Select the Department under which this course is being made.
4. Add the Topics. You can also create the topics from here itself.
5. Add the Description for the course.
6. Save.

 [Screenshot on the live page: Course]

## 3. Features

### 3.1. Assessment

For every new Course a User can have a New Assessment setting where in they can define the criteria based on which the students will be assessed for the course.

1. **Default Grading Scale**: A default [Grading Scale](/education/grading_scale) can be set up for the course, wherein you can define what would be the achievement level of the student based on the scores they earn for a course.
2. **Assessment Criteria**: You can define the [Assessment Criteria](/education/assessment_criteria) for this course wherein based on the different parameters of assessment, the student's understanding of the subject would be assessed.

 [Screenshot on the live page: Course]

## 4. More Actions

Once the course has been created, the following documents can be created from the course, which will later be linked to the course.

1. [Program](/education/program)
2. [Student Group](/education/student-group)
3. [Course Schedule](/education/course-schedule)
4. [Assessment Plan](/education/assessment_plan)

 [Screenshot on the live page: Course]

## 5. Video Tutorial for Course



<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//1ueE4seFTp8?start=66">
</iframe>

<!-- page: education/education__education-settings.md -->
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

  


[Screenshot on the live page: edu_settings]

### 1.1. Configuring Properties

* **Validate Batch for Students in Student Group**: When adding students to a student group via Batch, the system will verify whether the student belongs to that batch or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Validate Batch for Students in Student Group**: When adding students to a student group via Course, the system will verify whether the student is enrolled to that course or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Make Academic Term Mandatory**: When enabled, this option will ensure that while creating a Program Enrollment via the [Program Enrollment Tool](/education/program-enrollment-tool), the user has to enter the Academic Term.
* **Skip User Creation for New Student**: Whenever a new student is created, by default a User is created against it. If this option is enabled, no new User will be created when a new Student is created. For giving Portal access to the students this needs to be disabled, else the user will not be created and the student can't login to the portal.
* **Submit Sales Invoice from Program Enrollment / Fee Schedule:** When creating a Sales Invoice from either a Program Enrollment or Fee Schedule, if disabled then the Sales Invoice will br created in "Draft" Mode, if enabled it will be"Submitted".
* **Sales Invoice Posting Date should be same as Fee Schedule Posting Date:** By default, the Sales Invoice's Posting Date will be equal to Fee Schedule's Posting Date. If disabled then Sales Invoice's Posting Date will be today's date.

### 1.2. Portal Settings

The Education module is bundled with a Student Portal from v15.2.0 onwards.

[Screenshot on the live page: edu_settings1]  


* **Attendance Based on Course Schedule:** From Portal if the student applies for a leave, the attendance is marked based on this setting. If disabled the attendance will be marked for the whole day and if enabled the attendance will be marked for all the course schedule on which the student has applied for leave.
* **Razorpay Key & Razorpay Secret:** To collect Fees from students via portal these 2 settings needs to be there to connect the payment gateway to your account.
* **School / College Name Abbreviation:** Add your Institute's Abbreviation here, which will be displayed on the Student Portal
* **School / College Logo:** Upload your Institute's Logo here, which will be displayed on the Student Portal.

<!-- page: education/education__fee-category.md -->
---
title: "Fee Category"
space: "Education"
url: "https://docs.frappe.io/education/fee-category"
updated: "2026-02-09"
---

**Fee Category would form all the components for calculation of Fees or creation of Fee Structure.**

For example, Tuition Fees and Hostel fees would make the different categories of fees.

[Screenshot on the live page: Fee Category].png)  


To access Fee Category, go to:


> Home > Education > Fees > Fee Category
> 
> 

To create a new Fee Category, go to the Fee Category list, and click on new. Add the **Name** and **Description** of the Fee Category.

[Screenshot on the live page: Fee Category]  


For example, Tuition Fees and Hostel fees would make the different categories of fees.

[Screenshot on the live page: Fee Category].png)  


To access Fee Category, go to:


> Home > Education > Fees > Fee Category
> 
> 

To create a new Fee Category, go to the Fee Category list, and click on new. Add the **Name** and **Description** of the Fee Category.

[Screenshot on the live page: Fee Category]  


Version 15.1
------------

  


From Version 15.1.0 onwards, when a Fee Category is created an Item Master for the same Fee Category and is linked to the Fee Category.

  


[Screenshot on the live page: Screenshot 2024-02-23 at 8.18.15 PM]  


Version 15.4
------------

From 15.4.0 onwards, a child table named "Accounting Defaults" will be present inside the Fee Category DocType.

[Screenshot on the live page: Screenshot 2024-06-30 at 2.32.20 AM]  


  


**Usecase:**

1. If the user wants to book income in different accounts within the same company. Basically allows user to book different fee category in different income accounts.
2. If Institutes wants to take fees of class 1-4 in company X, and 4-8 in company Y and rest in company Z.
3. If institutes wants to segregate the incomes and ledgers booked based on a particular branch of the institute.

**Company:** In which company the user wants accounting ledgers to be shown.

  
**Default Income Account:** In the company set above, in which account the user would want to book the income against for that particular Fee Category.  
  


**Default Cost Center:** In the company set above, in which cost center you want the ledgers to be shown. This helps the use case where an educational institute has various branches and wants to segregate the incomes booked based on branch.

  


**Default Income Account & Cost center Scenarios are as follows:**

1. If no defaults are set for the Fee Component. Then the default income account and the default cost center will be taken from the defaults set in the Company mentioned in the [Fee Structure](https://docs.frappe.io/education/fee-structure).
2. If the defaults are set in the Item Group called "Fee Component", then the defaults will be used from the Item Group, for the Company selected in the Fee Structure.
3. If the defaults are set in the Fee Category, then those defaults will be used against the Company selected in the Fee Structure.

  


**What happens behind the scenes?**

When a Fee Category is created, an Item is created in the Item DocType.  
When the user set the defaults in the Fee Category DocType, those defaults are also set in the Item which is created against the Fee Category. And when the Sales Invoice is created, those defaults are used and the ledger entries are created.

<!-- page: education/education__fee-schedule.md -->
---
title: "Fee Schedule"
space: "Education"
url: "https://docs.frappe.io/education/fee-schedule"
updated: "2026-02-09"
---

**Fee Schedule would help you in defining a time-line for the Fee payment of the students, based on the Student Group.**

To access Fee Schedule, go to:


> Home > Education > Fees > Fee Schedule
> 
> 

1. Prerequisites
----------------

1. [Fee Structure](/docs/v13/user/manual/en/education/fee-structure)
2. [Student group](/docs/v13/user/manual/en/education/student-group)

1. How to create a new Fee Schedule
-----------------------------------

1. Go to the Fee Schedule list and click on New.
2. Select and add the **Fee Structure**. The moment you add the Fee Structure, the **Fee Break Up for Each Student** will be auto-populated.
3. Select and add the **Academic Year** and the **Academic Term**.
4. Add the **Due Date** for the fees.
5. Select and add the **Student Group**.
6. Save and Submit.

[Screenshot on the live page: Fee Schedule]  


2. Features
-----------

The **Accounting** features and **Accounting Dimensions** will be fetched as-is from the Fee structure.

### 2.1. Printing Settings

* Select and add the **Letter Head** to be used for printing the Fee Receipt.
* Select and add the **Print Heading** for the Fee Receipt.

### 2.2. Accounting

Working with ERPNext allows you to update your account entries with extreme ease. Whenever a student submits their fees and it gets recorded in the system, your Accounts will get updated simultaneously.

To facilitate that smoothly, you can add your Accounts details in the fee structure.

* **Receivable Account**: Enter the name of the Receivable Account for your Institution.
* **Income Account**: Select and add the Income Account for your Institution.
* **Company**: Select and add the Company under which all the payments are made. If there are multiple institutions in your ERPNext account, or if the Accounts are handled by a Sister Company.

### 2.3. Accounting Dimensions

* **Cost Center**: Select and add the name of the Cost Center of your Institute for Accounting Dimensions.

### 2.4. Version 15.1.0

When the document is submitted, you get an option to Create Sales Invoice.

[Screenshot on the live page: Screenshot 2024-04-01 at 12.41.38 PM]  


As soon as you submit the document, the status changes from "Draft" to "Invoice Pending".

On clicking the "Create Sales Invoice" button, sales invoices will be created for all the students for all the student groups present in the document, and the status will change from "Invoice Pending" to "Invoice Created".

[Screenshot on the live page: Screenshot 2024-04-01 at 12.43.23 PM]  


Sales Invoice is created with the customer field filled as Student's Name, the Fee Schedule Name is also stored in the Sales Invoice Document, and all the Fee Categories are linked to Sales Invoice Item Table.

By default the Sales Invoice will be created in the Draft mode, you can change this using enabling "Submit Sales Invoice from Program Enrollment / Fee Schedule" in Education Settings.

If this is enabled then clicking on "Create Sales Invoice" button in the Fee Schedule DocType, all the Sales Invoice will be automatically submitted.

[Screenshot on the live page: Screenshot 2024-04-01 at 12.45.18 PM]  


### 2.5. Version 15.3.0

From version 15.3.0 onwards, users will have an option to create Sales Order instead of Sales Invoice.

This feature can be helpful in the situations where you want to show accounting ledgers only when a student is joining the school. In such scenario you can create a "Sales Order" then when you want to create ledgers, you can create Sales Invoice against the Sales Order.

To enable this feature, go to:

Education Settings > Create Sales Order instead of Sales Invoice.

[Screenshot on the live page: Screenshot 2024-04-01 at 12.39.28 PM]  


After enabling, whenever a Fee Schedule is submitted. The status of the document will be "Order Pending" and "Create Sales Order" button will be shown instead of "Create Sales Invoice" button.

[Screenshot on the live page: Screenshot 2024-04-01 at 12.53.36 PM]  


On clicking the "Create Sales Order" button, sales order will be created for all the students for all the student groups present in the document, and the status will change from "Order Pending" to "Order Created".

[Screenshot on the live page: Screenshot 2024-04-01 at 12.55.22 PM]  


All the Sales Order by default will be created in Draft Mode. If you want to submit the Sales Order directly when created, you can enable "Submit Sales Order from Program Enrollment / Fee Schedule" in the Education Settings(as shown above).

  


### 2.6. Version 15.5.0

Fee Component table in Fee Schedule is editable. This allows user to add or delete Components for just one Fee Schedule.

**Usecase:**

Alot of times, institutes wants to collect one fee component in only one Fee Schedule and not in other Fee Schedules.


> Note: If a component which is added in Fee Schedule which is not their in the Fee Structure an alert message will be shown to the user.
> 
> 

<!-- page: education/education__fee-structure.md -->
---
title: "Fee Structure"
space: "Education"
url: "https://docs.frappe.io/education/fee-structure"
updated: "2026-02-09"
---

**A Fee Structure is a template that can be used while making Fees records or generating them via the Fee Schedule.**

The Fee structure can be fetched while creating the [Fees](/education/fees) for each student.

[Screenshot on the live page: Fee Structure]  


To access fee Structure, go to:

> Home > Education > Fees > Fee Structure

1. Prerequisites
----------------

Before creating a Fee Structure, it is advisable to create the following first:

1. [Academic Term](/education/academic-term)
2. [Academic Year](/education/academic-year)
3. [Program](/education/program)
4. [Student Category](/education/student-category)

2. How to create a Fee Structure
--------------------------------

1. Go to the fee structure list and click on New.
2. Select and add the **Program** and other details for the fee structure.
3. In the Components Table, enter the **Fees Category** and **Amount**.
4. Save and Submit.

[Screenshot on the live page: Fee Structure]

### 2.1. Additional Options while creating a Fee Structure.

* Enter the basic details like **Student Category**, **Academic Term** and **Academic Year**.
* In the components table, add the **Description** for the Fees Category.

2. Features
-----------

### 2.1. Accounts

Working with ERPNext allows you to update your account entries with extreme ease. Whenever a student submits their fees and it gets recorded in the system, your Accounts will get updated simultaneously.

To facilitate that smoothly, you can add your Accounts details in the fee structure.

* **Receivable Account**: Enter the name of the Receivable Account for your Institution.
* **Income Account**: Select and add the Income Account for your Institution.
* **Company**: Select and add the Company under which all the payments are made. If there are multiple institutions in your ERPNext account, or if the Accounts are handled by a Sister Company. Sales Invoice will be created against the company added in Fee Structure.

### 2.2. Accounting Dimensions

* **Cost Center**: Select and add the name of the Cost Center of your Institute for Accounting Dimensions.

[Screenshot on the live page: Fee Structure]  


3. After submitting the Fee Structure
-------------------------------------

Once you have submitted the Fee Structure, you will be able to create the [Fee Schedule](/education/fee-schedule) from within Fee Structure.

[Screenshot on the live page: Fee Structure]  


##### **Old flow**

[Screenshot on the live page: fee_sch_old]  


4. Version 15.1.0
-----------------

From Version 15.1.0 onwards user can create multiple Fee Schedules from Fee Structure DocType by clicking on "Create Fee Schedule".

The Fee Component table now has the discount option, which can be used by various Institutes to give discount to a particular Student Category.

The total amount which the user will put shall be the amount for the total year, and if the user wants they can be further bifurcated using the "Create Fee Schedule". After clicking on the button a modal will be opened, user will be prompted to select a fee plan, adjust the fees and select student group.

While creating the Fee structure, Company can be set, against which all the ledger entries will be created.

If you want to create a fee schedule just for a particular Academic Term, then you may fill the Academic Term Field.

  
Here is the demo:

[Screenshot on the live page: fee_sch_demo_new]  


  

<!-- page: education/education__fees.md -->
---
title: "Fees"
space: "Education"
url: "https://docs.frappe.io/education/fees"
updated: "2026-02-09"
---

**In this document we can maintain the Fee Records of the students.**

At the time of submission of Fees by each student, a new Fees Record will be created wherein all the details of the student, Program they are enrolled in, Accounting information, etc. would be maintained.

To access Fees, go to:

> Home > Education > Fees > Fees

1. Prerequisites
----------------

Before you create Fees record, it is advisable that you create the following first:

1. [Student](/education/student)
2. [Fee Category](/education/fee-category)
3. [Fee Structure](/education/fee-structure)

2. How to Create Fees
---------------------

1. Go to the Fees list and click on New.
2. The **Institution** will be selected by default, which is editable, if required.
3. Select and add the **Student** for whom the Fees record is being made. The name of the student will be fetched simultaneously.
4. Add the **Due Date** of the payment of the Fees.
5. Save.

[Screenshot on the live page: Fees]

### 2.1. Additional Options while Creating Fees

* The **Date** and **Posting Time** will be added by default as per the time and date on which the record is being made. However, if required, the same can be manually entered by checking the box **Edit Posting Date and Time**.
* The Student can be notified of their Fee Payment Due Date by checking on the box **Send Payment Request**.

3. Features
-----------

### 3.1. Student Details

Add all the relevant details of the student which includes **Program Enrollment**, **Program**, **Academic Term** and **Academic Year.** The **Student Email ID** gets fetched from the Student details given earlier.

[Screenshot on the live page: Fees]  


### 3.2. Fee Structure

You can select a **Fee Structure** for the given Fees Record. The moment you do so, all the **Fee Components** will be auto-populated from the Fee Structure.

[Screenshot on the live page: Fees]  


### 3.3. Fee Components

You can also add the **Fee Components** by selecting and adding the **Fee Category**, **Description** and **Fee Amount**.

[Screenshot on the live page: Fees]  


### 3.4. Printing Settings

* Select and add the **Letter Head** to be used for printing the Fee Receipt.
* Select and add the **Print Heading** for the Fee Receipt.

### 3.5. Accounts

Working with ERPNext allows you to update your account entries with extreme ease. Whenever a student submits their fees and it gets recorded in the system, your Accounts will get updated simultaneously.

To facilitate that smoothly, you can add your Accounts details in the fee structure.

* **Receivable Account**: Enter the name of the Receivable Account for your Institution.
* **Income Account**: Select and add the Income Account for your Institution.
* **Company**: Select and add the Company under which all the payments are made. If there are multiple institutions in your ERPNext account, or if the Accounts are handled by a Sister Company.

### 3.6. Accounting Dimensions

* **Cost Center**: Select and add the name of the Cost Center of your Institute for Accounting Dimensions.

[Screenshot on the live page: Fees]

### Payment

Directly make a payment from fee, select Mode of Payment in payment entry and submit the payment.

[Screenshot on the live page: Fee Payment]  


### v15.1.0

Version 15.1.0 onwards, Sales Invoice will be created against a student and a Fee Schedule.

All the Fee Categories will be shown in the "Sales Invoice Item" Table.

P.S: When a new Fee Category is created, an Item is also created against it.

### v15.3.0

User will have an option to create Sales Order instead of Sales Invoice.

To enable Sales Order functionality.

Open Education Settings > Create Sales Order instead of Sales Invoice.

[Screenshot on the live page: Screenshot 2024-04-01 at 12.39.28 PM]  


  

<!-- page: education/education__final-assessment-grades.md -->
---
title: "Final Assessment Grades"
space: "Education"
url: "https://docs.frappe.io/education/final-assessment-grades"
updated: "2026-02-09"
---

</education>

<!-- page: education/education__grading_scale.md -->
---
title: "Grading Scale\n"
space: "Education"
url: "https://docs.frappe.io/education/grading_scale"
updated: "2026-02-09"
---


**Under Grading Scale, you can define the threshold for the different grades obtained by the students, based on their scores in the assessment.**

For example, Students obtaining a score of 90% and above would be graded as A+, students obtaining a score of 80% and above would be graded A- and so on.

[Screenshot on the live page: Grading Scale]

#### Video Tutorial on Grading Scale





<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/t8ZDDq4qtIk?start=52">
</iframe>

<!-- page: education/education__guardian.md -->
---
title: "Guardian\n"
space: "Education"
url: "https://docs.frappe.io/education/guardian"
updated: "2026-02-09"
---


**Guardian allows you to record the details of the Guardians of a Student.**

[Screenshot on the live page: Guardian]

Every student can have multiple guardians like Father, Mother, Brother, or Sister.

To access Guardian, go to:

> Home > Education > Student > Guardian

## 1. Prerequisites

Before creating a Guardian, it is advised to create the following first:

* Student
* User

## 2. How to create a Guardian

1. Click on New Guardian in the Guardian List.
1. Add the name of the Guardian and click on Save.

### 2.1. Additional Options while creating a Guardian

Apart from the mandatory details of the Guardian, you can also add the following details:

1. **Email Address**: Enter the email address of the Guardian. The email address can be linked to an email group for sending Newsletters or Announcements.
2. **Mobile Number**: The mobile number of the Guardian can be recorded here.
3. **Alternate Mobile Number**: You can add the Alternate Mobile Number of the Guardian over here for emergency purposes.
4. **Date of Birth**: The date of birth of the Guardian can be recorded here.
5. **User ID**: If the Guardian is a User of the system, their User Id can be mentioned here.
6. **Education**: The Academic and Educational details of the Guardian can be recorded here.
7. **Occupation**: The occupation of the Guardian can be captured here.
8. **Designation**: You can enter the designation of the Guardian here.
9. **Work Address**: The Work Address of the Guardian can be recorded here for emergency purposes.

 [Screenshot on the live page: Guardian]

## 3. Features

### 3.1. Guardian Of

While creating a Student, if you have selected a Particular Guardian for them, the name of that Student will automatically be fetched here. Multiple students can have the same person as their guardian. In that case, multiple entries will be made in this section. However, on the front end, one will not be able to add more students to this section.

[Screenshot on the live page: Guardian]

### 3.2. Guardian Interests

Interests could be a list of activities that the Guardian would be willing to do for the institute or would like their Dependent or Ward to do as a part of extra-curricular activities.

[Screenshot on the live page: Guardian]

## 4. Making the Guardian A User

Once Guardian has been saved, you can find a button **Invite As User** on the top right corner of the form. This button would allow you to invite the guardian as a User of ERPNext by sending them an invitation email on the recorded email ID.

[Screenshot on the live page: Guardian]

## 5. Related Topics

1. [Student](/education/student)

<!-- page: education/education__instructor.md -->
---
title: "Instructor\n"
space: "Education"
url: "https://docs.frappe.io/education/instructor"
updated: "2026-02-09"
---

**An instructor is a teacher, tutor, or a professor that will be responsible for teaching a particular topic or course to the students.**

This document can be used to maintain the Instructor Log in the form of a list of topics/courses covered by the Instructor. This log will have the entire history of the courses taught by the Instructor.

[Screenshot on the live page]  


To access the instructor list, go to:

> Home > Education > Masters > Instructor

1. Prerequisites
----------------

Before creating an instructor, it is advisable to first create the following:

1. Employee
2. Department
3. Academic Year
4. Academic Term
5. Program
6. Course
7. Student Group

2. How to create an Instructor
------------------------------

1. Click on New Instructor.
2. Select the Employee ID/Employee Name for the Instructor.
3. Select the Department for which you are creating an Instructor.
4. Save.

[Screenshot on the live page]

3. Features
-----------

### 3.1. Instructor Log

* **Academic Year**: The Academic Year for which the Instructor is created.
* **Academic Term**: The Academic Term for which the Instructor is created.
* **Department**: The department to which the Instructor belongs to.
* **Program**: The Program for which the Instructor Log is being made.
* **Course**: The course for which the Instructor Log is being made.
* **Student Group**: The Student Group for which the user is making the Instructor Log.
* **Other Details**: Any other details regarding the Instructor Log can be recorded here.

[Screenshot on the live page]

### 3.2. After Submitting

Once the Instructor and Instructor Log is saved, you can create the following from there:

1. [Student Group](/docs/v13/user/manual/en/education/student-group)
2. [Course Schedule](/docs/v13/user/manual/en/education/course-schedule)
3. [Assessment Plan](/docs/v13/user/manual/en/education/assessment_plan)

[Screenshot on the live page]

> Note: While creating an Assessment Plan from the Instructor, the user can select whether the Instructor has to be kept as a Supervisor or as an Examiner for the Assessment plan.

[Screenshot on the live page]  


4. Video Tutorial for Instructor
--------------------------------




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//rVqQYS1_02k">
</iframe>

<!-- page: education/education__introduction.md -->
---
title: "Introduction"
space: "Education"
url: "https://docs.frappe.io/education/introduction"
updated: "2026-02-09"
---

## What is Frappe Education?

Frappe Education is an open-source and user-friendly Education Management System designed to streamline the administrative and academic processes of educational institutions. It is a powerful module based on the ERPNext software.

Whether you are running a B-School, an Academy or even a Primary School, Frappe Education helps you in organizing your entire set-up. You can have your entire Student Database, Fee Structure, Staffing Information, Courses, Curriculum, all defined in this app.

[Screenshot on the live page]

## Why Frappe Education

All the tools to manage which are available in the market were just not good enough. They were way too scatered, or too expensive or too complex to use. We wanted to create a tool that is easy to use, affordable and can be customized as per the needs of the institution. Frappe Education is dedicated to making education management more efficient and less time-consuming.

## Key Features

1. Student & Teacher Management - Manage student and teacher profiles, attendance.
2. Admission Management - Streamline the admission process for new students.
3. Fee Management - Organize and manage the fee structure and schedule payments.
4. Course Scheduling & Exam Planning - Efficiently schedule courses and manage course calendars.
5. Student Portal - Students can visit the portal to check their timetable, attendance, pay fees online, and see current and previous grades.

## Under The Hood

1. [Frappe Framework](https://frappe.io/framework) - A full-stack web application framework written in Python and Javascript.
2. [ERPNext](https://frappe.io/erpnext) - An open-source, modern ERP system that includes modules for accounting, inventory, manufacturing, and more.
3. [Frappe UI](https://github.com/frappe/frappe-ui) - A Vue-based UI library, to provide a modern user interface.

## Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/education?tab=readme-ov-file#production-setup).

## Learning and community

For an online demonstration of each functionality of the Education module, [click here.](https://www.youtube.com/watch?v=f6foQOyGzdA&list=PL3lFfCEoMxvxyjnARY_C1zLoOE55LcMKB)

1. [Telegram Group](https://t.me/frappe_education)
2. [Discuss Forum](https://discuss.frappe.io/c/erpnext/schools-college-education/40)
3. [GitHub](https://github.com/frappe/education)

<!-- page: education/education__program-enrollment-tool.md -->
---
title: "Program Enrollment Tool\n"
space: "Education"
url: "https://docs.frappe.io/education/program-enrollment-tool"
updated: "2026-02-09"
---


**The Program Enrollment Tool can be used in cases when you want to bulk Enroll new students to a Program, or when old or existing students, who are already enrolled to a program are needed to be enrolled to a new program.**

To access the Program Enrollment Tool, go to:

> Home > Education > Tools > Program Enrollment Tool

## 1. How to create Student Enrollment using the Student Enrollment Tool

1. **Get Students From**: If you are enrolling a new student, you can fetch the students from the **Student Applicant** or if you are promoting the older students you can fetch them from the **Program Enrollment** itself.
2. **Academic Year**: Enter the Academic Year for which the new students had applied or under which the existing students were enrolled.
3. **Academic Term**: Enter the Academic Term for which the new students had applied or under which the existing students were enrolled.
4. **Program**: Enter the Program for which the new students had applied or under which the existing students were enrolled.

### 1.1. Fetching Students

Once you click on the **Get Students** button, the system will fetch the list of all the students matching with the above-specified criteria. You can then delete a record if you wish to.

### 1.2. Enrollment Details

* If the student list is fetched from the Student Applicant list, you can enter a New Student BAtch Name under which all the New Students will be enrolled.

 [Screenshot on the live page: Student Enrollment Tool]

* If the student list is fetched from the existing Program Enrollment, you will be asked to enter the details of the new Program like Program Name, Academic Year, Academic Term and New Student Batch.

 [Screenshot on the live page: Student Enrollment Tool]

* Once all the details have been entered, click on **Enroll Students** to create Program Enrollment in bulk.

 [Screenshot on the live page: Student Enrollment Tool]

## 2. Video Tutorial for Program Enrollment Tool




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//5nxWYBRHY_o?start=82">
</iframe>
