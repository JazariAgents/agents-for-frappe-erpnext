<!-- Frappe documentation: education, part 2 of 2. Index: docs/INDEX.md -->

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
