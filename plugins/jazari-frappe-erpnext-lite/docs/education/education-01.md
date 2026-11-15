<!-- Frappe documentation: education, part 1 of 1. Index: docs/INDEX.md -->

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

![KzzYqR0](/files/KzzYqR0.png)  


  


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

![Academic Year](/files/education-academic-year-1.png)  


An academic year can be further linked to a [Student group](/education/student-group), which can be created from an Academic Year.

![Academic Year](/files/education-academic-year-2.png)  


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

![Assessment Criteria](/files/education-assessment-criteria.png)

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

![Assessment Group](/files/education-assessment-group.png)

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

![Assessment Plan](/files/assessment-plan-4.png)

## 3. Features

### 3.1. Schedule

1. **Schedule Date**: Enter the date on which the assessment is to be conducted.
1. **From Time**: Enter the start date for the assessment.
1. **To Time**: Enter the end time for the assessment.
1. **Room**: Select the room in which the assessment would be conducted.
1. **Examiner**: Add the name of the Examining Instructor for this assessment.
1. **Supervisor**: Add the name of the Supervising Instructor for this assessment.

![Assessment Plan](/files/education-assessment-plan-2.png)

### 3.2. Evaluate

Once you select the Course and the Grading Scale gets updated, you will be required to enter the Maximum Assessment Score and the Assessment Criteria would get automatically updated in the system.

![Assessment Plan](/files/education-assessment-plan-3.png)

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

![Assessment Result]({{docs_base_url}}/img/education/assessment/assessment-result.png)

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

![Assessment Result Tool](/files/education-assessment-result-tool.png)

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

![Course Schedule](/files/education-course-schedule-1.png)

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

![Course Schedule](/files/education-course-schedule-1.gif)

## 3. Marking Attendance

You can mark attendance for a Student Group against a Course Schedule.

![Course Schedule](/files/education-course schedule-3.png)

To mark attendance for a course, click on **Attendance** in the Course Schedule. You will be redirected to a page, wherein the name of all the students will be listed along with check-boxes for marking attendance. You can check the Present students and **Mark Attendance**. You can also **Check All** or **Uncheck All** and mark attendance.

![Course Schedule](/files/education-course-schedule-4.gif)

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

![Course Scheduling Tool](/files/education-course-schedule-1.png)  


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

![Course Scheduling Tool](/files/education-course-scheduling-tool.gif)  


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

![Course](/files/education-program-workflow.png)

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

 ![Course](/files/education-course-1.png)

## 3. Features

### 3.1. Assessment

For every new Course a User can have a New Assessment setting where in they can define the criteria based on which the students will be assessed for the course.

1. **Default Grading Scale**: A default [Grading Scale](/education/grading_scale) can be set up for the course, wherein you can define what would be the achievement level of the student based on the scores they earn for a course.
2. **Assessment Criteria**: You can define the [Assessment Criteria](/education/assessment_criteria) for this course wherein based on the different parameters of assessment, the student's understanding of the subject would be assessed.

 ![Course](/files/education-course-2.png)

## 4. More Actions

Once the course has been created, the following documents can be created from the course, which will later be linked to the course.

1. [Program](/education/program)
2. [Student Group](/education/student-group)
3. [Course Schedule](/education/course-schedule)
4. [Assessment Plan](/education/assessment_plan)

 ![Course](/files/education-course-3.png)

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

<!-- page: education/education__fee-category.md -->
---
title: "Fee Category"
space: "Education"
url: "https://docs.frappe.io/education/fee-category"
updated: "2026-02-09"
---

**Fee Category would form all the components for calculation of Fees or creation of Fee Structure.**

For example, Tuition Fees and Hostel fees would make the different categories of fees.

![Fee Category](/files/education-fee-category-1 (1).png)  


To access Fee Category, go to:


> Home > Education > Fees > Fee Category
> 
> 

To create a new Fee Category, go to the Fee Category list, and click on new. Add the **Name** and **Description** of the Fee Category.

![Fee Category](/files/education-fee-category-2.gif)  


For example, Tuition Fees and Hostel fees would make the different categories of fees.

![Fee Category](/files/education-fee-category-1 (1).png)  


To access Fee Category, go to:


> Home > Education > Fees > Fee Category
> 
> 

To create a new Fee Category, go to the Fee Category list, and click on new. Add the **Name** and **Description** of the Fee Category.

![Fee Category](/files/education-fee-category-2.gif)  


Version 15.1
------------

  


From Version 15.1.0 onwards, when a Fee Category is created an Item Master for the same Fee Category and is linked to the Fee Category.

  


![Screenshot 2024-02-23 at 8.18.15 PM](/files/Screenshot 2024-02-23 at 8.18.15 PM.png)  


Version 15.4
------------

From 15.4.0 onwards, a child table named "Accounting Defaults" will be present inside the Fee Category DocType.

![Screenshot 2024-06-30 at 2.32.20 AM](/files/Screenshot 2024-06-30 at 2.32.20 AM.png)  


  


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

![Fee Schedule](/files/education-fee-schedule-1.gif)  


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

![Screenshot 2024-04-01 at 12.41.38 PM](/files/Screenshot 2024-04-01 at 12.41.38 PM.png)  


As soon as you submit the document, the status changes from "Draft" to "Invoice Pending".

On clicking the "Create Sales Invoice" button, sales invoices will be created for all the students for all the student groups present in the document, and the status will change from "Invoice Pending" to "Invoice Created".

![Screenshot 2024-04-01 at 12.43.23 PM](/files/Screenshot 2024-04-01 at 12.43.23 PM.png)  


Sales Invoice is created with the customer field filled as Student's Name, the Fee Schedule Name is also stored in the Sales Invoice Document, and all the Fee Categories are linked to Sales Invoice Item Table.

By default the Sales Invoice will be created in the Draft mode, you can change this using enabling "Submit Sales Invoice from Program Enrollment / Fee Schedule" in Education Settings.

If this is enabled then clicking on "Create Sales Invoice" button in the Fee Schedule DocType, all the Sales Invoice will be automatically submitted.

![Screenshot 2024-04-01 at 12.45.18 PM](/files/Screenshot 2024-04-01 at 12.45.18 PM.png)  


### 2.5. Version 15.3.0

From version 15.3.0 onwards, users will have an option to create Sales Order instead of Sales Invoice.

This feature can be helpful in the situations where you want to show accounting ledgers only when a student is joining the school. In such scenario you can create a "Sales Order" then when you want to create ledgers, you can create Sales Invoice against the Sales Order.

To enable this feature, go to:

Education Settings > Create Sales Order instead of Sales Invoice.

![Screenshot 2024-04-01 at 12.39.28 PM](/files/Screenshot 2024-04-01 at 12.39.28 PM.png)  


After enabling, whenever a Fee Schedule is submitted. The status of the document will be "Order Pending" and "Create Sales Order" button will be shown instead of "Create Sales Invoice" button.

![Screenshot 2024-04-01 at 12.53.36 PM](/files/Screenshot 2024-04-01 at 12.53.36 PM.png)  


On clicking the "Create Sales Order" button, sales order will be created for all the students for all the student groups present in the document, and the status will change from "Order Pending" to "Order Created".

![Screenshot 2024-04-01 at 12.55.22 PM](/files/Screenshot 2024-04-01 at 12.55.22 PM.png)  


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

![Fee Structure](/files/education-fee-structure-2.png)  


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

![Fee Structure](/files/education-fee-structure-1.gif)

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

![Fee Structure](/files/education-fee-structure-3.png)  


3. After submitting the Fee Structure
-------------------------------------

Once you have submitted the Fee Structure, you will be able to create the [Fee Schedule](/education/fee-schedule) from within Fee Structure.

![Fee Structure](/files/education-fee-structure-4.png)  


##### **Old flow**

![fee_sch_old](/files/fee_sch_old.gif)  


4. Version 15.1.0
-----------------

From Version 15.1.0 onwards user can create multiple Fee Schedules from Fee Structure DocType by clicking on "Create Fee Schedule".

The Fee Component table now has the discount option, which can be used by various Institutes to give discount to a particular Student Category.

The total amount which the user will put shall be the amount for the total year, and if the user wants they can be further bifurcated using the "Create Fee Schedule". After clicking on the button a modal will be opened, user will be prompted to select a fee plan, adjust the fees and select student group.

While creating the Fee structure, Company can be set, against which all the ledger entries will be created.

If you want to create a fee schedule just for a particular Academic Term, then you may fill the Academic Term Field.

  
Here is the demo:

![fee_sch_demo_new](/files/fee_sch_demo_new.gif)  


  

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

![Fees](/files/education-fee-1.gif)

### 2.1. Additional Options while Creating Fees

* The **Date** and **Posting Time** will be added by default as per the time and date on which the record is being made. However, if required, the same can be manually entered by checking the box **Edit Posting Date and Time**.
* The Student can be notified of their Fee Payment Due Date by checking on the box **Send Payment Request**.

3. Features
-----------

### 3.1. Student Details

Add all the relevant details of the student which includes **Program Enrollment**, **Program**, **Academic Term** and **Academic Year.** The **Student Email ID** gets fetched from the Student details given earlier.

![Fees](/files/education-fees-2.png)  


### 3.2. Fee Structure

You can select a **Fee Structure** for the given Fees Record. The moment you do so, all the **Fee Components** will be auto-populated from the Fee Structure.

![Fees](/files/education-fee-4.gif)  


### 3.3. Fee Components

You can also add the **Fee Components** by selecting and adding the **Fee Category**, **Description** and **Fee Amount**.

![Fees](/files/education-fees-5.png)  


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

![Fees](/files/education-fees-3.png)

### Payment

Directly make a payment from fee, select Mode of Payment in payment entry and submit the payment.

![Fee Payment]({{docs_base_url}}/v13/assets/img/education/fees/fee-payment.png)  


### v15.1.0

Version 15.1.0 onwards, Sales Invoice will be created against a student and a Fee Schedule.

All the Fee Categories will be shown in the "Sales Invoice Item" Table.

P.S: When a new Fee Category is created, an Item is also created against it.

### v15.3.0

User will have an option to create Sales Order instead of Sales Invoice.

To enable Sales Order functionality.

Open Education Settings > Create Sales Order instead of Sales Invoice.

![Screenshot 2024-04-01 at 12.39.28 PM](/files/Screenshot 2024-04-01 at 12.39.28 PM.png)  


  

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

![Grading Scale](/files/education-grading-scale-1.png)

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

![Guardian](/files/education-guardian-1.png)

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

 ![Guardian](/files/education-guardian-1.png)

## 3. Features

### 3.1. Guardian Of

While creating a Student, if you have selected a Particular Guardian for them, the name of that Student will automatically be fetched here. Multiple students can have the same person as their guardian. In that case, multiple entries will be made in this section. However, on the front end, one will not be able to add more students to this section.

![Guardian](/files/education-guardian-2.png)

### 3.2. Guardian Interests

Interests could be a list of activities that the Guardian would be willing to do for the institute or would like their Dependent or Ward to do as a part of extra-curricular activities.

![Guardian](/files/education-guardian-3.png)

## 4. Making the Guardian A User

Once Guardian has been saved, you can find a button **Invite As User** on the top right corner of the form. This button would allow you to invite the guardian as a User of ERPNext by sending them an invitation email on the recorded email ID.

![Guardian](/files/education-guardian-4.png)

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

![](/files/vDpjU6T.png)  


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

![](/files/LyThgam.png)

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

![](/files/H0lCkO4.png)

### 3.2. After Submitting

Once the Instructor and Instructor Log is saved, you can create the following from there:

1. [Student Group](/docs/v13/user/manual/en/education/student-group)
2. [Course Schedule](/docs/v13/user/manual/en/education/course-schedule)
3. [Assessment Plan](/docs/v13/user/manual/en/education/assessment_plan)

![](/files/JA8Cueq.png)

> Note: While creating an Assessment Plan from the Instructor, the user can select whether the Instructor has to be kept as a Supervisor or as an Examiner for the Assessment plan.

![](/files/ZQeVNRf.png)  


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

![](/files/399563531-46af048c-749f-41f7-8d10-47e4fa643592.png)

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

 ![Student Enrollment Tool](/files/education-student-tool-5.png)

* If the student list is fetched from the existing Program Enrollment, you will be asked to enter the details of the new Program like Program Name, Academic Year, Academic Term and New Student Batch.

 ![Student Enrollment Tool](/files/education-student-tool-6.png)

* Once all the details have been entered, click on **Enroll Students** to create Program Enrollment in bulk.

 ![Student Enrollment Tool](/files/education-student-tool-7.png)

## 2. Video Tutorial for Program Enrollment Tool




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//5nxWYBRHY_o?start=82">
</iframe>

<!-- page: education/education__program-enrollment.md -->
---
title: "Program Enrollment\n"
space: "Education"
url: "https://docs.frappe.io/education/program-enrollment"
updated: "2026-02-09"
---


**Program Enrollment is the record of enrollment of a student in a given program and chosen courses for a particular Academic Term.**

To ensure that students are associated with a particular program in the system, their Program Enrollment must be created. The mandatory course in that program is automatically filled in the Enrolled Courses table while the elective or optional courses can be selected manually.

If the student has applied online for the admission in a particular **Program** and the application is approved, then the Program Enrollment can be created from within the Student Applicant record via clicking on the **Enroll** button. Checkout [Student Applicant](/education/student-applicant) for more information on this.

To access Program Enrollment, go to:

> Home > Education > Admission > Program Enrollment

## 1. Prerequisites

Before creating a Program Enrollment, it is advisable that you create the following first:

1. [Student](/education/student)
1. [Program](/education/program)
1. [Student Category](/education/student-category)
1. [Student Batch](/education/student-batch-name)
1. [Academic Year](/education/academic-year)
1. [Academic Term](/education/academic-term)
1. [Course](/education/course)
1. [Fee Structure](/education/fee-structure)

## 2. How to create a Program Enrollment

1. Go to Program Enrollment List and click on new.
1. Select the Student whom you are getting enrolled in the program.
1. Select the Program under which you are getting the student enrolled.
1. Enter the Academic Year for which the student is getting enrolled.
1. The Enrollment Date for the form would by default be set on the current date, the same, however, can be changed if needed.
1. Save and submit.

 ![Program Enrollment](/files/education-program-enrollment-1.gif)

### 2.1. Additional Options while creating a Program Enrollment

1. **Student Category**: Select the category if the student belongs to a particular student category.
1. **Academic Term**: Select the Academic Term.
1. **Student Batch**: Select the batch if the student belongs to a particular student batch.
1. **Student House**: Select the House if the student belongs to a particular student house.
1. **Boarding Student**: Check this if the Student is residing at the Institute hostel. In this case, the fee structure would accordingly be updated.

 ![Program Enrollment](/files/education-program-enrollment-2.gif)

## 3. Features

### 3.1. Transportation

Select the mode of transportation for the student to and from the Institute and the Vehicle Number.

### 3.2. Enrolled Courses

Select and add the courses which the student has opted to study during the course of the program.

![Program Enrollment](/files/education-program-enrollment-3.png)

### 3.3. Fees

Select and add the Academic Term, Fee Structure, Student Category, Fees Due Date and Fees Amount to be paid by the student for the enrollment to the course.

![Program Enrollment](/files/education-program-enrollment-4.gif)

## 4. Video




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//5nxWYBRHY_o?start=0&amp;end=88">
</iframe>

<!-- page: education/education__program.md -->
---
title: "Program\n"
space: "Education"
url: "https://docs.frappe.io/education/program"
updated: "2026-02-09"
---


**A Program will have an educational curriculum defined by your institute to streamline the learning process and goals in each subject or course.**

For example, Economics Major would be a Program taught at an institution that will have various courses within.

![Program](/files/education-program-workflow.png)

An Economics major would look something like this:
![Program](/files/education-program-2.png)

To access the Program list go to:

> Home > Education > Masters > Program

## 1. Prerequisites

To create a New Program, it is advised to create the following first:

1. Department
2. Course

## 2. Creating a New Program

1. Go to the Program list and click on New.
2. Enter the Program Name and the Program Abbreviation.
3. Select the Department for the Program.
4. Select and add the courses within the Program.
5. Save.

 ![Program](/files/education-program-1.gif)

### 2.1 Alternate ways of creating a new Program

A new program can also be created from a course, in the following way:

![Program](/files/education-program-3.gif)

### 2.2 Additional Options while creating a new Program

* **Portal Settings**

 * **Is Published**: For every program created in ERPNext, there is a check-box in the Portal settings, that allows the Program to be published on the portal. This can facilitate Self Enrollment and other settings for the program. Once this box is checked, the following options will be available for the user.
 * **Allow Self Enroll**: Once this box is checked, the students/applicants would be able to enroll themselves for the program on the portal.
 * **Is Featured**: Enabling this option would allow the program to be featured on the portal.
 * **Intro Video**: Enter the link for the video that you wish to add an Introductory Video for the Program.
 * **Description**: Add the description of the Program which you want to be visible on the portal.

 ![Program](/files/education-program-4.png)

## 3. Video Tutorial on Program and Courses



<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//1ueE4seFTp8?end=70">
</iframe>

<!-- page: education/education__room.md -->
---
title: "Room\n"
space: "Education"
url: "https://docs.frappe.io/education/room"
updated: "2026-02-09"
---


**Room refers to a tutoring space which can be set as the venue for courses or examinations.**

Examples of a room are Examination Halls, Classrooms, or Labs. The Room will have details like Room number and Room Capacity.

To access Room, go to:

> Home > Education > Masters > Room

## 1. How to create a Room

1. Go to the Room list and click on New.
1. Add the name of the room.
2. Add the Room Number for the selected room.
3. Enter the Seating capacity for the room.

 ![Room](/files/education-room-1.gif)

## 2. Other Actions

A Room can be further linked to a [Course Schedule](/education/course-schedule).

![Room](/files/education-room-2.png)

<!-- page: education/education__student-applicant.md -->
---
title: "Student Applicant\n"
space: "Education"
url: "https://docs.frappe.io/education/student-applicant"
updated: "2026-02-09"
---


**A Student Applicant record gets created when a student applies to your institute for admission.**

You can Approve or Reject a student applicant. By accepting a student applicant you can add them to the student master.

To access student Applicant, go to:

> Home > Education > Admission > Student Applicant

## 1. Prerequisites

Before creating a Student Applicant, it is advisable to first create the following:

1. [Academic Term](/education/academic-term)
1. [Academic Year](/education/academic-year)
1. [Program](/education/program)

## 2. How to create a Student Applicant

1. Go to the student Applicant and click on New.
2. Enter the **First Name** of the student Applicant.
3. Enter the **Program** for which the student has applied.
4. Enter the **Student Email Address**.
5. Save.

 ![Student Applicant](/files/education-student-applcant-1.gif)

## 3. Features

### 3.1 Online Application via a Web Form

A Student Applicant gets automatically created when a student applies online. This can be made possible through the Student Applicant Web Form which is created by default in the system. Search for "[Web Form List](/website/web-form)" in the awesome bar to access the list of all the web forms in the system.

Once the student applies, the status of the application by default is "Applied". You can either "Approve" or "Reject" the form.

![Student Applicant](/files/education-student-applicant-5.png)

Once the application is approved, you can "Enroll" the student to a program. When you click the **Enroll** button, the system shall create a student against that applicant and redirect you to the [Program Enrollment form](/education/program-enrollment).

![Student Applicant](/files/education-student-applcant-6.gif)

> Note: Once a student is created against the student applicant, the system will set the application status to 'Admitted' and will not allow you to change the application status unless the student record is deleted.

## 4. Video Tutorial for Student Application



<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/l8PUACusN3E">
</iframe>

<!-- page: education/education__student-attendance-tool.md -->
---
title: "Student Attendance Tool"
space: "Education"
url: "https://docs.frappe.io/education/student-attendance-tool"
updated: "2026-02-09"
---

**The Student Attendance tool allows you to bulk update the attendance for students based on Student Group and Course Schedule**.

To access the Student Assessment Tool, go to:

> Home > Education > Attendance > Student Attendance Tool

To mark the Attendance based on Student Group select the group based on:

1. Batch
2. Course
3. Activity

Student details will be auto-fetched and you can mark the attendance of the given date.

![student-attendance-tool](/files/student-attendance-tool.gif)  


Video for Student Attendance Tool
---------------------------------




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//j9pgkPuyiaI?start=63">
</iframe>

<!-- page: education/education__student-attendance.md -->
---
title: "Student Attendance"
space: "Education"
url: "https://docs.frappe.io/education/student-attendance"
updated: "2026-02-09"
---

**Student Attendance allows you to track and manage the attendance of a student for a day. The Attendance module is designed to help teachers easily mark student attendance during class.**

Attendance Records can be created against Students on a daily basis.

To access Student Attendance, go to:

> Home > Education > Attendance > Student Attendance

1. How to create Student Attendance
-----------------------------------

Select the **Student, Course Schedule, and Student Group** for which attendance is to be marked for the given date. Set the Status to Present/Absent and save.

![education-student-attendance-1](/files/education-student-attendance-1.gif)  


[**Student Attendance tool**](/education/student-attendance-tool) can be used for bulk updation of the attendance based on **Batch, Course, or Activity**.

  



> From version 15.3.1 onwards: Attendance DocType have 3 States:
> 
> 1. Present
> 2. Leave
> 3. Absent
> 
> The status of the attendance can be changed even after submitting the doctype 
> 
> 

2. Video on Student Attendance
------------------------------




<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//j9pgkPuyiaI">
</iframe>

<!-- page: education/education__student-batch-name.md -->
---
title: "Student Batch"
space: "Education"
url: "https://docs.frappe.io/education/student-batch-name"
updated: "2026-02-09"
---

**A Student batch is a collection of students from within Student Groups.**

For example, A group of students studying the same Program together will be called a Student Batch.

![education-student-workflow](/files/education-student-workflow.png)  


To access the Student Batch, go to:


> Home > Education > Settings > Student Batch Name
> 
> 

When a student is enrolled for a [Program](/education/program), the batch can be selected for the student, and they shall be a part of that batch.

You can also get a Student Batch-Wise Attendance report to view the number of students present from the Batch.

<!-- page: education/education__student-category.md -->
---
title: "Student Category"
space: "Education"
url: "https://docs.frappe.io/education/student-category"
updated: "2026-02-09"
---

**Student Category allows you to classify the students based on various categories.**

In Institutions, there may be fee concession for some categories such as Handicapped Students, Foreign Nationals, Reserved Categories by the government, etc.

When a Student is enrolled for a [Program](/education/program), you can select the select the Category for the Student.

To access Student category, go to:


> Home > Education > Settings > Student Category
> 
> 

![education-student-category-1](/files/education-student-category-1.png)  


1. How to create a Student Category
-----------------------------------

To create a new student category, click on New Student Category and add the name of the Student Category.

![education-student-category-2](/files/education-student-category-2.gif)  


You can select the Student Category while making the Fee Structure and accordingly the student from the selected groups can be filtered out while making the Fee Schedule.

<!-- page: education/education__student-group-creation-tool.md -->
---
title: "Student Group Creation Tool\n"
space: "Education"
url: "https://docs.frappe.io/education/student-group-creation-tool"
updated: "2026-02-09"
---


**The Student group creation tool allows you to create student groups in bulk.**

To access the Student Group Creation Tool, go to:

> Home > Education > Tools > Student Group Creation Tool

## 1. How to use the Student Group Creation Tool

1. Select the **Academic Term** and the **Program** for which a student group is to be created.
1. Select the **Program** under which you are creating the student group.
1. By default, the student group is created based on the courses only. The check-box for **Separate course based Group for every Batch** allows you to create different batch-wise Student groups for each course.
1. Click on get **Get Courses**: All the courses within the selected Program will be enlisted here. You can choose and delete courses from the list already added in the list. You can also select and add courses from other programs on this list.
1. Click on **Create Students Groups**. Multiple Student groups for each course and batch will be created.

![Student Group Creation Tool](/files/education-student-group-creation-tool.gif)

## 2. Tutorial Video on Student Group Creation Tool


.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
 

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/5K_smeeE1Q4?start=108">
</iframe>

<!-- page: education/education__student-group.md -->
---
title: "Student Group\n"
space: "Education"
url: "https://docs.frappe.io/education/student-group"
updated: "2026-02-09"
---


**A student group is a collection of students from the same batch or taking the same course.**

For example, if a group of students studying the same program together will be called a student batch, then from within this group, the cluster of students who have taken up the same elective course will be called a Student Group.

![Student Group](/files/education-student-workflow.png)

To access Student Group, go to:

> Home > Education > Student > Student group

## 1. Prerequisites

Before creating a Student group, it is advisable that you first create the following:

1. [Student](/education/student)
1. [Program Enrollment](/education/program-enrollment)
1. [Student Batch name](/education/student-batch-name)
1. [Student Category](/education/student-category)
1. [Instructor](/education/instructor)

## 2. Creating a Student Group

1. Go to Student Group List and click on New.
1. **Group Based On**: Select the basis on which you would like to create the student group. The three options available are:
 * Batch: List of all the students from within a specific batch will be fetched in this case.
 * Course: Lst of all the students who have enrolled for a specific course will be fetched in this case.
 * Activity: You can select this option when you want to create a group of students for certain activities happening in the school.
1. **Student Group Name**: Enter the name of the student group.
1. Save.

![Student Group](/docs/v13/assets/img/education/education-student-group-1)

### 2.1. Additional Options while creating a Student Group

Apart from the above mandatory options, the following fields should also be filled in the form to create a Student Group:

1. Select the **Academic Year** and **Academic Term** for which the Student Group is being made.
1. **Program**: Select the Program for which the Student Group is being made.
1. **Batch**: Select the Batch based on which you would want to fetch the list of students for the student group.
1. **Max Strength**: Enter the Maximum number of students that can be a part of this Student Group. If the number of selected students in the group is more than the Max Strength, the system will not allow you to save this group and an error will be shown.

 ![Student Group](/files/education-student-group-max-student-limit-error.png)

1. **Student Category**: If you want the students of a specific category to be a part of this group, you can select that.
1. **Course**: This option only appears when then Group is Based on a Course. You can select a particular course here, and a list of only those students who have been enrolled in this course would be fetched to create this student group.

### 2.2. Features:

* **Students**: Enter the names of the students that you wish to add to this Student Group. The student list will be fetched according to the parameters selected above, like Academic Year, Academic Term, Batch, Program, Course, etc.

* **Get Students**: Based on the parameters selected above, the system will automatically fetch the list of students, and all the students who have the criteria matching with the Student Group, will be enlisted in the Students list once you click on 'Get students'.

 > Note: You have to select the students Manually for an Activity-Based group as this group may not have any defined criteria and any student can be selected to be added in this group. **Get Students** will not be functional in this condition.

* **Instructors**: Select the Instructors who will be teaching or mentoring this particular group of students.

![Student Group](/files/education-student-group-4.png)

## 3. After creating a Student Group

Once the student group has been created and saved, the following can be created from the Student group:

1. **Attendance**: You will be redirected to [Student Attendance Tool](/education/student-attendance-tool) through which you can mark the attendance of all the students for a particular date.
1. **Course Schedule**: You will be redirected to [Course Schedule](/education/course-schedule), wherein you will be able to see the schedule for this student group and further you can also create a New Course Schedule for the students in this group.
1. **Assessment Plan**: You will be redirected to [Assessment Plan](/education/assessment_plan) list, where all the assessment plan for your student group will be listed and you will also be allowed to create a New Assessment Plan for the group.
1. **Update Email Group**: Once you select this option if the Email Ids of the Students in this group will be added to the Email Group and you will be able to send newsletters to all the subscribers in this Student Group.

 ![Student Group](/files/education-student-group-update-email.png)

1. **Newsletters**: You will be able to send [Newsletters](/CRM/newsletter) to all the subscribers from within the student group with this option.

![Student Group](/files/education-student-group-4.png)



## 4. Video


.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
 

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/5K_smeeE1Q4">
</iframe>

<!-- page: education/education__student-leave-application.md -->
---
title: "Student Leave Application"
space: "Education"
url: "https://docs.frappe.io/education/student-leave-application"
updated: "2026-03-20"
---

**Student Leave Application is a formal document to keep a track of leaves for a student.**

To access Student Leave Application list, go to:

> Home > Education > Attendance > Student Leave Application

## 1 How to create a Student Leave Application

1. Go to the Student Leave Application list, and click on New.
2. Select the Student.
3. Set the 'From Date' and 'To Date' fields for specifying the period.
4. Marking Attendance for the Leave Application is governed by the 'Attendance Based On' field. In ERPNext, Student Attendance can be marked in two ways:
  **Course Schedule**: If attendance is taken for every lecture (in colleges/universities), then the leave application can be created for that particular course schedule slot.  
   **Student Group**: If attendance is taken for the entire day then student group (class/division) is used to mark attendance so that leave is calculated for the entire day
5. Based on the Attendance field, select the Student Group or Course Schedule. Optionally enter the reason.
6. In case the student is not attending the institute to participate or represent the institute in any event, he/she can be marked as "Present" from the Leave Application itself by checking *Mark as Present*.
7. Save. The 'Total Leave Days' will be calculated and set in the document after excluding the holidays which are part of your default [Holiday List](/human-resources/holiday-list).

![Screenshot 2024-05-23 at 6.23.14 PM](/files/Screenshot 2024-05-23 at 6.23.14 PM.png)

### 1.2 On Submission of Student Leave Application

Once the Student Leave Application is submitted, a Student Attendance record is automatically created with status as 'Leave'. If *Mark as Present* is checked, then the status of the Attendance Record is set as 'Present'. The Leave Application is linked to this Student Attendance document for reference.

![Screenshot 2024-05-23 at 6.23.27 PM](/files/Screenshot 2024-05-23 at 6.23.27 PM.png)



If any of the dates within the leave period is a holiday, then, Student Attendance record creation is skipped for that date.

### 1.3 On Cancellation of Student Leave Application

On cancellation of the Student Leave Application, the linked Student Attendance record is also cancelled automatically.

2. Tutorial Video for Student Leave Application

---





3. Related Topics

1. [Student Attendance](/education/student-attendance).

<!-- page: education/education__student-log.md -->
---
title: "Student Log\n"
space: "Education"
url: "https://docs.frappe.io/education/student-log"
updated: "2026-02-09"
---


**The student Log will act as a Student Diary, wherein, all their logs and other notes can be recorded.**

A student log can be used to record the student's performance in General, Academic, Medical or Achievement terms.

To access Student Log, go to

> Home > Education > Student > Student Log

## 1. Prerequisites

* Student
* Academic Year
* Academic Term
* Program
* Student Batch

## 2. How to create a Student Log

1. Go to Student Log List and click on New.
1. Enter the Student ID. The moment you do this, the name of the student will automatically be fetched.
1. Save.

 ![Student Log](/files/education-student-log-1.png)

### 3.1. Additional Options while creating a Student Log

* **Type**: You can enter the type of the Log that is being created for the student. A student log can be a General, Academic, Medical or Achievement log. Following are some examples wherein you can make a log for the student:

 - General: If the student was extremely well behaved during the entire day or if they were sleeping during the class.
 - Academic: If a student gets a full score in a surprise test, or if they get a very bad score.
 - Medical: If the student was found not having their lunch, or if they complained of some other medical issue.
 - Achievement: If the student scored a goal for the team in a football match.

 ![Student Log](/files/education-student-log-2.png)

* **Date**: You can select the date on which the log was entered.
* **Academic Year**: You can select the academic session for which this log is being made.
* **Academic Term**: You can select the term in which this log is being recorded.
* **Program**: Select the Program under which the student is enrolled.
* **Student Batch**: Select the batch of which this student is a part of.
* **Log**: This field will have your note of log for the student.

 ![Student Log](/files/education-student-log-3.png)

<!-- page: education/education__student-portal.md -->
---
title: "Student Portal"
space: "Education"
url: "https://docs.frappe.io/education/student-portal"
updated: "2026-02-09"
---

  


From Version 15.2.0 onwards the Student Portal is available with the Education Module.


> Note: As of now only a Student can login to the portal, which is only possible if a user is created against that student who is trying to login. The portal is accessible at the url "/student-portal".
> 
> "Current Academic Year" in "Education Settings" should be set for the portal to work.
> 
> 

  


  


Features with the portal:

1. School/College Timetable
2. Current and Previous Grades
3. Fee History and Fee Payment
4. Student Attendance
5. Student Profile Data

Timetable
---------

![Screenshot 2024-02-21 at 6.03.02 PM](/files/Screenshot 2024-02-21 at 6.03.02 PM.png)  


All the courses which are scheduled for the particular program for that particular student will be displayed on the "/education/schedule" page. The data of the same is taken from the "Course Schedule" DocType

Whatever color the user will decide in the Course Schedule DocType, will be displayed in the Calendar.

On clicking each class, student will be able to see data related to the class.

Grades
------

![Screenshot 2024-02-21 at 6.03.09 PM](/files/Screenshot 2024-02-21 at 6.03.09 PM.png)  


On this page the Student can check the results of the examination conducted in the current Program, or from the Drop down list student can select previous programs and see the grades for the each exam conducted in that program.

  


The data in this page is taken from "Assessment Result" DocType. Then the data is grouped together to show the results in the format shown in the image.

Fees
----

![Screenshot 2024-02-21 at 6.03.20 PM](/files/Screenshot 2024-02-21 at 6.03.20 PM.png)  


On this page student can either check the previous payments or they can pay any fees if there is any.

For already "Paid" Fees, the student can download the Invoice and whatever is the "Standard Print Format" is in "Sales Invoice" doctype, will be shown to the student. The data on this Page is taken from the Sales Invoice DocType  
  
If the student wants to pay the Fees, then on Clicking "Pay Now", a razorpay payment gateway is opened.![Screenshot 2024-02-21 at 6.03.54 PM](/files/Screenshot 2024-02-21 at 6.03.54 PM.png)  


To setup Razorpay, go to Education Settings -> Portal Settings, and enter your "Razorpay Key" & "Razorpay Secret".

On successful payment, a Payment Entry is created against that Fees (which basically is a Sales Invoice), and the status of the payment is then updated to "Paid" in that particular "Sales Invoice", which is then reflected in the frontend.

Attendance
----------

![stud_portal_attendance](/files/stud_portal_attendance.png)  


Attendance data for current Program and any Student Groups is displayed over here, as a student can be enrolled in various Student Groups so all the Student Groups are visible in the dropdown.

On clicking of any Student Group the Present and Absent Data is shown in the calendar. The data for this page is taken from "[Student Attendance"](http://education-module:8000/app/student-attendance) DocType.

A student can also apply for leave here from the attendance page by clicking on "Apply for Leave" button. A dialog is popped up.

![stud_portal_attendance_1](/files/stud_portal_attendance_1.png)  


When the save button is clicked, attendance is marked for the student with the status of "Leave".

Based on Education Settings (Portal Tab), the attendance is marked for the student.

If "Attendance Based on Course Schedule" is enabled, the attendance will be marked on Course Schedule basis and will be mandatory. If disabled, the attendance will be marked on Student Group Basis for that particular date.

The use case for the above is:

Some schools like to take attendance at the starting of the day and some schools take attendance for each class, so depending upon your use case you can change the education settings.

Student Profile Data
--------------------

![stud_portal_profile](/files/stud_portal_profile.png)  


After clicking on the School Logo, the student can see their profile data. The profile data is taken from the Student Master.  
  

<!-- page: education/education__student.md -->
---
title: "Student\n"
space: "Education"
url: "https://docs.frappe.io/education/student"
updated: "2026-02-09"
---


**The Student document will hold all the data of any Student in your Academy like their Personal Information, Photo, Date of Birth, Address, etc.**

This form will also contain any additional details like the Student's Guardian and Sibling details.

![Student](/files/education-student-1.png)

The student is enrolled in a [Program](/education/program) when the application is approved. Once the enrollment is done the [Student Applicant](/education/student-applicant) status is update to Admitted.

To access Student, go to:

> Home > Education > Student > Student

## 1. Prerequisites

Before creating a student, it is advised to create the following first:

* User(If Applicable)

## 2. How to create a New Student

1. Go to the student list and click on New.
2. Enter the First Name, Middle Name and Last Name of the student.
3. Enter other details like Student Email Address, User ID(If Applicable) and Joining Date.
4. Save.

 ![Student](/files/education-student-4.png)

## 3. Features

Apart from the aforementioned details, some additional details of the student that can be captured are as follows:

### 3.1. Personal Details

Personal details of the Student like their Date of Birth, Gender, Blood Group, and Nationality can be added here.

![Student](/files/education-student-personal.png)

### 3.2. Home Address

The address of the student, along with the City, State, and Pincode can be captured here. Two address lines can be captured for each student.

![Student](/files/education-student-address.png)

### 3.3. Guardian Details

The details of the student's guardian and their relationship with the student can be captured here. You can create a [Guardian](/education/guardian) from here itself, or create a guardian first and then create the Student.

![Student](/files/education-student-guardian.png)

### 3.4. Sibling Details

This section will have all the details of the Student's Siblings. You can select if the sibling is studying in the Same Institute or no. If the Sibling is also a student of your institute, you will be required to enter their Student ID, if not, you can enter the name of the Institution they are associated with. Their academic details like Program and personal details like Gender and Date of Birth can also be captured.

![Student](/files/education-student-sibling.png)

### 3.5. Exit Details

The Student's exit details can be captured here, like their Date of Leaving, and Leaving Certificate Number as captured in your institute's records can be captured. Further, you can also enter the Reason For Leaving in here.

![Student](/files/education-student-7.png)

> Note: On top of the student form, there is an **'Enabled'** checkbox using which the student by default would always be enabled. Once you have recorded the Student's Exit Details, you must uncheck this box to disable the student.

![Student](/files/education-student-3.png)

### 3.6. After Saving

Once you save the Student Form, the student gets created in the system and you will be able to link this document to other documents related to Admission, Assessment, Attendance, Student Activity, Student LMS Activity, and Fees. Further, you will also be able to see a dashboard that will indicate their activities throughout the year.

## 4. Other actions

Once a student is created in the system, you can also view the Accounting Ledger, which will show a report of all the payments made by the student.

![Student](/files/education-student-2.png)

## 5. Related Topics

1. [Guardian](/education/guardian)
2. [Student Group](/education/student-group)
3. [Student Attendance](/education/student-attendance)
4. [Program](/education/program)
5. [Course](/education/course)

## 6. Video Tutorial on Student Management



.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
 

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed//nIUsbl0rEE0">
</iframe>

<!-- page: education/education__student_admission.md -->
---
title: "Student Admission\n"
space: "Education"
url: "https://docs.frappe.io/education/student_admission"
updated: "2026-02-09"
---


**Student Admission is a document which can be configured to initiate an Admission Process for your institution by publishing it on the ERPNext generated website.**

To access student Admission, go to:

> Home > Education > Admission > Student Admission

## 1. Prerequisites

Before creating a Student Admission, it is advisable that you first create the following:

1. [Academic Year](/education/academic-year)
1. [Program](/education/program)

## 2. How to create a Student Admission

1. Go to Student Admission list and click on New.
1. Select the **Academic Year** for the Student Admission.
1. Enter the **Application Form Route**. This is the navigation URL for the Online Admission portal.
1. Save.

Once the Student Admission has been saved, you will be bale to see a link on the left sidebar, saying **See on Website**. This link will allow you to see the Student Admission Portal on ERPNext generated website.

![Student Admission](/files/education-student-admission-4.png)

This is what the Student Admission will look like in the website view:
![Student Admission](/files/education-student-admission-5.png)

### 2.1. Additional Details while creating a Student Admission

1. **Title**: Enter the title for the Student Admission Portal.
1. **Route**: Enter a desirable path which will become the url extension for the admission portal.
1. **Admission Start Date**: Select the date for the start of online Admission Process.
1. **Admission End Date**: Select the last date for applying to online Admission Process.
1. **Publish on Website**: Check this box when the content of the portal is ready and the Admission Process can be kickstarted on the website.

 ![Student Admission](/files/education-student-admission-2.png)

### 2.2. Eligibility And Details

* **Program**: Here you can select which program are the admissions being called for.
* **Minimum Age**: Enter the probable birth-date of the youngest person that can seek admission in the program.
* **Maximum Age**: Enter the probable birth-date of the oldest person that can seek admission to the program.
* **Application Fee**: You can choose to declare the application fee for the selected program.
* **Naming Series**: Here you can define the Naming series based which the forms of the Admission Seekers will be named ond ordered.
* **Introduction**: You can add a brief introductory information about the admission process so that it is better understood to the admission seekers.

 ![Student Admission](/files/education-student-admission-3.png)

<!-- page: education/education__topic.md -->
---
title: "Topic"
space: "Education"
url: "https://docs.frappe.io/education/topic"
updated: "2026-02-09"
---

**A Topic is a subunit of a Course and will contain all the contents related to the topic.**

For example, under the program Economics Major, the course Mathematical Methods in Economics would be course whereas, within the course 'Linear Algebra' would be a topic.

![Topic](/files/education-program-workflow.png)  


The content of the topic could be in the form of an article, a video or a quiz.

![Topic](/files/education-topic-1.png)  


To access the Topic list, go to:


> Home > Education > Masters > Topic
> 
> 

1. Prerequisites
----------------

Before creating a New Topic, it is advisable that you create the following first:

1. Article
2. Video
3. Quiz

2. How to create a Topic
------------------------

1. Click on New Topic and add the title of the Topic.
2. Add the related course (optionally).
3. Select the Content Type for the topic. It could be an Article, a Video or a Quiz.
4. Select the Content for the Topic. You can create a New Article, Video or a Quiz from here itself.
5. Optionally add a description and Save.

![education-topic-3](/files/education-topic-3.gif)
