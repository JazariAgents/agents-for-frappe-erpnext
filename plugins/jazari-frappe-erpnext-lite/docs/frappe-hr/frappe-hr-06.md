<!-- Frappe documentation: frappe-hr, part 6 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__introduction.md -->
---
title: "Frappe HR"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/introduction"
updated: "2026-02-04"
---

Frappe HR is an open Source, modern, and easy-to-use HR and Payroll Software for all organizations. It has everything you need to drive excellence within the company. It is a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

[Screenshot on the live page]

## Why Frappe HR

Businesses often struggle with scattered HR processes, manual payroll calculations, disconnected employee records, and time-consuming approvals.

- Frappe HR brings everything under one roof so HR teams can focus on people, not paperwork.
- Built for organizations that need a flexible and cost-effective solution, Frappe HR eliminates inefficiencies, ensures compliance, and gives employees a seamless experience. 
- Whether you are managing a handful of employees or scaling to thousands, it helps you stay organized without getting bogged down in administrative overhead.

## Key Features

- **Employee Lifecycle**: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.
- **Leave and Attendance**: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.
- **Expense Claims and Advances**: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with ERPNext accounting.
- **Performance Management**: Track goals, align goals with key result areas (KRAs), enable employees to evaluate themselves, make managing appraisal cycles easy.
- **Payroll & Taxation**: Create salary structures, configure income tax slabs, run standard payroll, accomodate additional salaries and off cycle payments, view income breakup on salary slips and so much more.
- **Frappe HR Mobile App**: Apply for and approve leaves on the go, check-in and check-out, access employee profile right from the mobile app.

And more.

## Under the Hood

- **[Frappe Framework](https://github.com/frappe/frappe)**: A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
- **[Frappe UI](https://github.com/frappe/frappe-ui)**: A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/hrms/?tab=readme-ov-file#production-setup).

### Learning and Community

1. [Frappe School](https://frappe.school) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [Documentation](https://docs.frappe.io/hr) - Extensive documentation for Frappe HR.
3. [User Forum](https://discuss.erpnext.com/) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/frappehr) - Get instant help from the community of users.

<!-- page: frappe-hr/hr__job-applicant.md -->
---
title: "Job Applicant"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-applicant"
updated: "2026-02-04"
---

**A Job Applicant is a person who applies for a job in your Company against a particular Job Opening.**

In Frappe HR, you can maintain a list of people who have applied against a particular [Job Opening](https://docs.frappe.io/hr/job-opening).

To create a Job Applicant, go to:

> Home > Human Resource > Recruitment > Job Applicant

**1. Prerequisites**
--------------------

Before creating a Job Applicant, it is advisable you create the following:

* [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
* [Department](https://docs.frappe.io/hr/department)
* [Job Opening](https://docs.frappe.io/hr/job-opening)

**2. How to Create a Job Applicant**
------------------------------------

1. Go to Job Applicant list, click on New.
2. Enter Applicant Name and Email Address.
3. Select Job Opening.
4. Select Source (Campaign, Employee Referral, Walk In, Website Listing).

> **Note:** If you select the Source as Employee Referral, you will have to select the Employee name in the Source Name Field.

[Screenshot on the live page: Job Applicant]  


**3. Features**
---------------

### **3.1 Linking with an Email Account**

You can link Job Application with an Email account. Suppose you link Job Application with an email [job@example.com](mailto:job@example.com), the system will create a New Job Applicant against each email received on the mailbox.

* To link Email Account with Job Applicant, go to:

> Settings > Email Account > New Email Account

* Enter the Email Address and the password, and select 'Enable Incoming'
* In 'Append To' select 'Job Applicant'

[Screenshot on the live page: Email Account]  


### **3.2 Tracking Interviews**

After creating [Interviews](https://docs.frappe.io/hr/interview), you can easily track them within the Job Applicant dashboard. This enables you to compare all the interviews conducted with the applicant and evaluate their overall performance to make an acceptance decision.

[Screenshot on the live page: image]  


**4. Related Topics**
---------------------

1. [Interview](https://docs.frappe.io/hr/interview)
2. [Job Offer](https://docs.frappe.io/hr/job-offer)
3. [Employee](https://docs.frappe.io/hr/employee)

  

<!-- page: frappe-hr/hr__job-offer.md -->
---
title: "Job Offer"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-offer"
updated: "2026-02-04"
---

**Job Offer is given to selected candidates after interview and selection which states the offered salary package, designation, grade, department, number of days entitled for leave among other information.**

In Frappe HR you can make a record of the Job Offers that you can give to candidates. To access Job Offer, go to:

> Home > Human Resource > Recruitment > Job Offer

**1. Prerequisites**
--------------------

Before creating a Job Offer, it is advisable to create the following:

* [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
* [Job Applicant](https://docs.frappe.io/hr/job-applicant)
* [Job Opening](https://docs.frappe.io/hr/job-opening)

**2. How to Create a Job Offer**
--------------------------------

1. Go to Job Offer list, click on New.
2. Select the Job Applicant, Offer Date and Designation.
3. Set the Status of the Job Offer (Awaiting Response, Accepted, Rejected).
4. Save and Submit.

[Screenshot on the live page: Job Offer]

> **Note:** A Job Offer can be made only against a [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**3. Features**
---------------

### **3.1 Job Offer Terms**

In this section, you can enter the Job Offer Term such as job description, notice period, incentives, leaves per year, etc. and specify its Value/ Description.

### **3.2 Select Terms and Conditions**

All the Terms and Conditions related to the Job Offer can be specified in this section. To do this, create a new Terms and Conditions template and link it to the Job Offer.

### **3.3 Printing Details**

You can create a pre-designed print format to print you Job Offer. To do so, select the Letter Head and Print Heading in the Printing Details section.

[Screenshot on the live page: Job Offer]  


  

<!-- page: frappe-hr/hr__job-opening.md -->
---
title: "Job Opening"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-opening"
updated: "2026-08-10"
---

**A Job Opening is a job vacancy in your Company. You can make a record of the open vacancies in your company using Job Opening.**



Frappe HR allows to plan recruitment for your company. The number of Job Openings you can create for a Designation is restricted according to the vacancies planned by the Staffing Plan defined for the company or one of its parent group companies in the hierarchy.

:::note
Make sure the "Check Vacancies On Job Offer Creation" checkbox is checked in the Hiring Settings section of the HR Settings.
:::



To access Job Opening, go to:

> Home &gt; Human Resource &gt; Recruitment &gt; Job Opening

## **1. Prerequisites**

Before creating a Job Opening, it is advisable you create the following:

- [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
- [Department](https://docs.frappe.io/hr/department)

## **2. How to create a Job Opening**

1. Go to Job Opening list, click on New.
2. Enter the Job Title.
3. Select the Designation and Department. Based on Designation selected, appropriate Staffing Plan and Planned Number of Positions will be fetched.
4. Save.

[Screenshot on the live page]
*You can also use Job Opening Template to populate the common fields*

Once the Job Opening is saved, you can directly create a new [Job Applicant](https://docs.frappe.io/hr/job-opening) from the dashboard.

:::note
You can close/reopen a Job Opening as and when required. Once a Job Opening is Closed, you cannot create a Job Applicant against it.
:::



## **3. Features**

### **3.1 Job Portal**

You can enable 'Publish on website' to publish a Job Opening to the [Job Portal](https://docs.frappe.io/hr/job-portal). This will make it possible for users to view and apply to these openings from your site.

[Screenshot on the live page]

## **4. Related Topics**

1. [Job Applicant](https://docs.frappe.io/hr/job-applicant)
2. [Job Offer](https://docs.frappe.io/hr/job-offer)

Frappe HR allows to plan your recruitment at a group company level. The number of Job Openings you can create for a Designation is restricted according to the Vacancies planned by the Staffing Plan defined for the company or one of it's parent group companies in the hierarchy. To understand how you can do configure this, check [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

<!-- page: frappe-hr/hr__job-portal.md -->
---
title: "Job Portal"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-portal"
updated: "2026-02-04"
---

**The Job Portal provides an interface for applicants to browse and apply to published Job Openings.**

**1. Prerequisites**
--------------------

Before using the Job Portal, it is advisable you create the following:

* [Job Opening](https://docs.frappe.io/hr/job-opening)


> **Note: For an opening to be visible on the Job Portal, you must enable the 'Publish on website' field for that specific Job Opening.**
> 
> 

**2. How to Apply Using the Job Portal**
----------------------------------------

1. To visit the Job Portal, go to https://<sitename>/jobs. For example, if my site name is <https://frappeio.frappe.cloud>, the Job Portal can be accessed from <https://frappeio.frappe.cloud/jobs>

  


[Screenshot on the live page: 273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc]
2. You can use the search bar to search for jobs by title or description. You can also filter jobs by company, department, location, or employment type, and sort them by the latest or oldest posting date.
3. Click on a job card to view it in detail.

  


[Screenshot on the live page]
4. Click on the 'Apply Now' button at the top-right corner. This will open a web form where applicants can enter their details.

  


[Screenshot on the live page]
5. Fill in the appropriate details and click on Submit. This will result in the creation of the corresponding Job Applicant document.

  


[Screenshot on the live page]

**3. Related Topics**
---------------------

1. [Job Applicant](https://docs.frappe.io/hr/job-applicant)
2. [Interview Management](https://docs.frappe.io/hr/interview-management)

  

<!-- page: frappe-hr/hr__job-requisition.md -->
---
title: "Job Requisition"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-requisition"
updated: "2026-02-04"
---

Job Requisition is an internal document raised to request a new hire. These requisitions are then converted to Job Openings or considered for budgeting while making the Staffing Plan.

To access Job Requisition, go to:


> **Home > Human Resources > Recruitment > Job Requisition**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Job Requisition, you should create the following:

* [Designation](https://docs.frappe.io/hr/designation)
* [Department](https://docs.frappe.io/hr/department) (Optional)

**2. How to create a Job Requisition**
--------------------------------------

1. Go to the Job Requisition list, and click on New.
2. Enter the Designation you want to place the request for.
3. Enter the No of Positions, Expected Compensation, Company, and Department (optional).
4. Select the employee who is applying for the requisition in the Requested By field.
5. Optionally, you can set the **Expected By** date.
6. The Job Description will be fetched from the Designation. If you want to add additional information for the opening, you can do so here.
7. Save.
8. By default, the status will be Pending. You can set up [workflows](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/workflows) to change the status to Open & Approved.

[Screenshot on the live page: Job Requisition]  


[Screenshot on the live page: Job Requisition List]

**3. Actions**
--------------

### **3.1 Create Job Opening**

Once the Job Requisition is **Open & Approved**, you can create a new Job Opening against the Job Requisition or associate an existing one.

[Screenshot on the live page: create job opening]  


### **3.2 Associate Job Opening**

If you already have an existing Open Job Opening for that designation, you can associate it with the requisition.

[Screenshot on the live page: Associate Job Opening]  


Once the Job Opening is closed, the Job Requisition's status is updated to **Filled**

**4. Features**
---------------

### **4.1 Check existing Employee Referrals**

If there is an existing Employee Referral for that designation, you might want to consider referrals instead of creating new openings. A banner is visible on the Job Requisition form with the links to these employee referrals in these cases.

[Screenshot on the live page: employee referral]  


### **4.2 Get Job Requisitions in Staffing Plan**

While creating a budget with the Staffing Plan, you can fetch the existing **Pending** or **Open & Approved** Job Requisitions.

[Screenshot on the live page: Get Job Requisition]  


### **4.3 Time to Fill Metric**

Time to Fill measures the number of days it takes to fill an open position, from the date a job requisition is posted to the date when it is marked as Filled. This metric is auto-calculated and set in Job Requisition.

The Average Time to Fill is also displayed on the Hiring Dashboard:

[Screenshot on the live page: time to fill]  


**5. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

  

<!-- page: frappe-hr/hr__leave-allocation-after-compensatory-leave-request.md -->
---
title: "Leave allocation after Compensatory Leave Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-allocation-after-compensatory-leave-request"
updated: "2026-02-04"
---

**Use case:** If an employee works on a Holiday and wants to apply for a compensatory off, the following process is important in Frappe HR:

1) Create an **Employee** with the mandatory details and assign a **Holiday List** and a **Leave Policy** to it.

2) Attendance should be marked for the Employee, it is mandatory for the employee to be marked as present on the Holiday [this Holiday should be in the Holiday List.]

[Screenshot on the live page]  


3) Create a **Leave allocation** for the **Employee**.

4) In the **Leave Type list**, for all the types that allow Compensatory off, tick the checkbox.

[Screenshot on the live page]  


5) Now, create a **Compensatory Leave Request** for the employee.

[Screenshot on the live page]  


6) Go back and check the **Leave allocation** for the leave added for the Employee.

[Screenshot on the live page]

<!-- page: frappe-hr/hr__leave-allocation.md -->
---
title: "Leave Allocation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-allocation"
updated: "2026-02-26"
---

**Leave Allocation enables you to allocate a specific number of leaves of a particular type to an Employee.**

To access Leave Allocation, go to:

> Home > Human Resources > Leaves > Leave Allocation

**1. Prerequisites**
--------------------

Before creating a Leave Allocation, it is advisable you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Type](https://docs.frappe.io/hr/leave-type)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)

**2. How to create a Leave Allocation**
---------------------------------------

1. Go to Leave Allocation list, click on New.
2. Select the Employee, Leave Type, From Date and To Date.
3. Enter the number of New Leaves Allocated for that particular Leave Type.
4. Save and Submit.

[Screenshot on the live page: Leave Allocation]

> **Note:** Enable the 'Add unused leaves from previous allocations' option in case you want to carry forward unused leaves from the previous allocation period for this particular Leave Type.


**3. Features**
---------------------------------------

### 1. Manually adding leaves to the current allocation

If your earned leave allocation failed due to some reasons like background jobs weren’t running, you can manually allocate leaves for an allocation

Click on **Actions > Allocate Leaves**

[Screenshot on the live page: Allocate Leaves Button]

And set the number of leaves you want to allocate. You can also set the **From Date** from when these leaves will be applicable. By default, it will consider today’s date.

[Screenshot on the live page: Manual Leave Allocation]

Click on allocate to add leaves to the balance

**4. Related Topics**
---------------------

1. [Leave Application](https://docs.frappe.io/hr/leave-application)
2. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
3. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
4. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)
5. [Holiday List](https://docs.frappe.io/hr/holiday-list)

<!-- page: frappe-hr/hr__leave-application.md -->
---
title: "Leave Application"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-application"
updated: "2026-02-04"
---

**Leave Application is a formal document created by an Employee to apply for Leaves for a particular time period.**

Frappe HR allows your employees to apply for leaves via Leave Applications and get them approved by the Leave Approvers.

To access Leave Application, go to:


> **Home > Human Resources > Leaves > Leave Application**
> 
> 

**1. Prerequisites**
--------------------

Before you create a Leave Application, it is advisable you have the following documents:

* [Department](https://docs.frappe.io/hr/department)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)
* [Leave Type](https://docs.frappe.io/hr/leave-type)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)
* [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)

**2. How to create a Leave Application**
----------------------------------------

1. Go to Leave Application list, click on New.
2. A table of Allocated Leaves will be shown. Based on the Leaves taken, the available leaves are displayed for each Leave Type.

[Screenshot on the live page: Leave Application]
3. Select the Employee Name and Leave Type.
4. Set the Leave duration using From Date and To Date. Based on the dates selected, the 'Total Leave Days' and the 'Leave Balance Before Application' fields will be displayed.
5. If the Leave applied is for a half-day, select the 'Half Day' checkbox.
6. Enter the Reason for Leave.

[Screenshot on the live page: Leave Application]
7. Select Leave Approver.
8. Select the Posting Date of the Leave Application.
9. Check the 'Follow via Email' checkbox to send notification of the Leave Application to the Leave Approver.
10. You can also link the Salary Slip of the Employee in the Leave Application for the record.

[Screenshot on the live page: Leave Application]
11. Click on Save. Once the Employee saves the Leave Application, the status of the Leave Application changes to 'Open', and an email is sent to the Leave Approver for approval. The Leave Approval Notification Template can be configured in [HR Settings](https://docs.frappe.io/hr/hr-settings) under the Leave Settings section.
12. Once the Leave Approver receives the email, they can Approve, Reject, or Cancel the Leave Application. Once this is done, the Leave Approver can submit the Leave Application. On submission, the status of the document changes accordingly, and an email is sent to the Employee notifying them the same.


> **Note: Leave Application cannot be submitted if the Salary is already processed for the leave period.**
> 
> 

The Leave Application process flow is summarized below:

* The employee applies for leave through Leave Application.
* Approver gets notification via email. For this, the "Follow via Email" checkbox should be checked.
* Approver reviews Leave Application.
* Approver approves/rejects/cancels Leave Application
* The employee gets the notification on the status of his/her Leave Application

**3. Features**
---------------

### **3.1 Setting Leave Approver**

A leave approver is a user who can approve a Leave Application of an Employee. In Frappe HR version 12, Leave Approvers can be set at two levels:

* **Department Level:** Leave Approvers for each department can be configured in the [Department](https://docs.frappe.io/hr/department) master. Multiple Leave Approvers can be set in a Department. The first Leave Approver in the list will be considered as the default Leave Approver.

[Screenshot on the live page: Leave Application - Leave Approvers]  


When an Employee belonging to a particular department applies for leave, the Leave Approvers set in that Employee's department master will be considered as his Leave Approvers.
* **Employee Level:** Leave Approvers can also be set Employee-wise in the employee master.

[Screenshot on the live page: Leave Application - Leave Approvers]

If Leave Approvers are set at both Employee-level and Department-level, the Employee-level Leave Approver will be considered as the default Leave Approver in this case.

When a new Leave Application is created, if the selected leave approver does not have access to it, the document is shared with the approver with "submit" permission.

**Tip:** If you want all users to create their own Leave Applications, you can set their “Employee ID” as a match rule in the Leave Application Permission settings. Check [Setting Up Permissions](https://docs.erpnext.com/docs/v144/user/manual/en/setting-up/users-and-permissions/user-permissions) for more information.


> **Additional Notes:**
> 
> 


> * **Leave Application period must be within a single Leave Allocation period. In case, you are applying for leave across the leave allocation period, you have to create two Leave Application records.**
> * **Leave Application period must be in the latest Leave Allocation period.**
> * **Employee cannot apply for leave on the dates which are added in the** [**Leave Block List**](https://docs.frappe.io/hr/leave-block-list)**.**
> 

To understand how Frappe HR allows you configure leaves for employees, check [Leaves](https://docs.frappe.io/hr/leave-management-intro/).

**3. Related Topics**
---------------------

1. [Leave Type](https://docs.frappe.io/hr/leave-type)
2. [Leave Period](https://docs.frappe.io/hr/leave-period)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
5. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)

  

<!-- page: frappe-hr/hr__leave-block-list.md -->
---
title: "Leave Block List"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-block-list"
updated: "2026-02-04"
---

**Leave Block List is a list of dates in a year, on which employees cannot apply for leave.**

To access Leave Block List, go to:

> Home > Human Resources > Leaves > Leave Block List

Frappe HR allows you to define a list of Leave Approvers who can approve Leave Applications on blocked days, in case of urgency. You can also define whether the list will be applied to the entire company or on any specific departments.

**1. Prerequisites**
--------------------

Before you create a Leave Block List, it is advisable you have the following documents:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)
* [Department](https://docs.frappe.io/hr/department)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)

**2. How to create a Leave Block List**
---------------------------------------

1. Go to Leave Block list, and click on New.
2. Enter Leave Block List Name.
3. Enter Block Date and Reason in the 'Leave Block List Dates' table.
4. Enter Users to approve Leave Applications for Blocked Days in the 'Leave BLock List Allowed' table.
5. Save.

[Screenshot on the live page: Leave Block List]

> **Note:** Enable the 'Applies to Company' option if you want the Leave Block List to be applicable for the entire Company. If not checked, the list will have to be added to each [Department](https://docs.frappe.io/hr/department) where it has to be applied.

**3. Related Topics**
---------------------

1. [Leave Type](https://docs.frappe.io/hr/leave-type)
2. [Leave Period](https://docs.frappe.io/hr/leave-period)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
5. [Leave Application](https://docs.frappe.io/hr/leave-application)

  

<!-- page: frappe-hr/hr__leave-calculation-in-salary-slip.md -->
---
title: "Leave Calculation In Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-calculation-in-salary-slip"
updated: "2026-02-04"
---

There are two types of leave which user can apply for.

* Paid Leave (Sick Leave, Privilege Leave, Casual Leave etc.)
* Unpaid Leave

Paid Leave are firstly allocated by HR manager. As and when Employee creates Leave Application, leaves allocated to him/her are deducted. These leaves doesn't have impact on the employee's Salary Slip.

When Employee is out of paid leave, he create Leave Application for unpaid leave. The term used for unpaid leave in Frappe HR is Leave Without Pay (LWP). These leaves does have impact on the Employee's Salary Slip.

Just marking Absent in the Attendance record do not have impact on salary calculation of an Employee, as that absenteeism could be because of paid leave. Hence creating Leave Application should be created incase of absenteeism. Let's consider a scenario to understand how leaves impact employees Salary Slip. 1. Setup Employee 1. Allocate him paid leaves 1. Create Salary Structure for that Employee. In the Earning and Deduction table, select which component of salary should be affected if Employee takes LWP. 1. Create Holiday List (if any), and link it with Employee master. **Working Days:** Working Days in Salary Slip are calculated based on number of days selected above. If you don't wish to consider holiday in Working Days, then you should do following setting. > Human Resource > Setup > HR Setting Uncheck field "Include Holidays in Total No. of Working Days" Holidays are counted based on Holiday List attached to the Employee's master. **Leave Without Pay:** Leave Without Pay is updated based on Leave Application made for this Employee, in the month for which Salary Slip is created, and which has Leave Type as "Leave Without Pay". Payment Days: Following is how Payment Days are calculated: Payment Days = Working Days - Leave Without Pay If you have LWP checked for the Salary Component, there will be reduction in Amount based on no. of LWP of an Employee for that month.

<!-- page: frappe-hr/hr__leave-control-panel.md -->
---
title: "Leave Control Panel"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-control-panel"
updated: "2026-02-04"
---

The Leave Control Panel allows you to allocate leaves in bulk based on a specific Leave Policy or Leave Type.


> **Home > Human Resources > Leaves > Leave Control Panel**
> 
> 

**1. Prerequisites**
--------------------

Before using the Leave Control Panel, it is advisable to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Period](https://docs.frappe.io/hr/leave-period) (optional)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy) / [Leave Type](https://docs.frappe.io/hr/leave-type)

**2. How to allocate leave using the Leave Control Panel**
----------------------------------------------------------

1. Choose the appropriate option from Dates Based On and fill in the corresponding data. This would include Leave Period or From Date and/or To Date.
2. If you wish to assign a Leave Policy, select the intended one. Alternatively, you can allocate leave directly by disabling Allocate Based On Leave Policy, selecting the desired Leave Type, and filling in the corresponding number of New Leaves Allocated.
3. Select Carry Forward if you wish to add unused leaves from the previous allocation into this one.
4. Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
5. Select suitable employees from the Select Employees table below and click on the Allocate Leave button at the top right corner.

[Screenshot on the live page]  



> **Note: Leave cannot be allocated for past dates.**
> 
> 

[Leave Policy Assignments](https://docs.frappe.io/hr/leave-policy-assignment) and [Leave Allocations](https://docs.frappe.io/hr/leave-allocation) made using the Leave Control Panel are reflected in their respective DocTypes as shown below:

* Leave Policy Assignment

[Screenshot on the live page]  


* Leave Allocation

[Screenshot on the live page]  

<!-- page: frappe-hr/hr__leave-encashment.md -->
---
title: "Leave Encashment                                          "
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-encashment"
updated: "2026-02-04"
---

**Leave Encashment refers to an amount of money received in exchange for Leaves not availed by an Employee. You can submit Leave Encashment for Leave Types which are encashable.**

To access Leave Encashment, go to:

> Home > Human Resources > Leaves > Leave Encashment

**1. Prerequisites**
--------------------

Before creating Leave Encashment, it is advisable you create the following documents:

1. [Employee](https://docs.frappe.io/hr/leave-allocation)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Period](https://docs.frappe.io/hr/leave-period)
5. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
6. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)

**2. How to create a Leave Encashment**
---------------------------------------

1. Go to Leave Encashment list, click on New.
2. Select Leave Period.
3. Select the Employee. Once the Employee is selected, the Employee's Department is automatically fetched.
4. Select Leave Type for which the Leave is encashed. Make sure the Leave Type is encashable (the 'Allow Encashment' checkbox in the Leave Type is checked).
5. Select Encashment Date, if you want payment via Salary Slip. Based on the date selected, the amount will be encashed in that particular Payroll Entry.
6. Save and Submit.

[Screenshot on the live page: Leave Encashment]

> **Note:** As you select Employee and Leave Type, Leave Balance and Encashable Days (which is total leave balance minus the threshold days set in Leave Type) will be shown along with the Encashment Amount based on the Leave Encashment per day as configured in the Employee's assigned Salary Structure.

**3. Leave Encashment Payment Methods**
---------------------------------------

In Frappe HR, we allow you to pay the encashment amount via Salary Slip or Payment Entry.

### **3.1 Payment via Payment Entry**

1. To pay the Leave Encashment amount via Payment Entry you need to check Pay via Payment Entry checkbox. 
2. After that, it will allow you to select Payable Account and Expense Account. 
3. After Submitting the record click on the button "Create Payment Entry" which will redirect you to the Payment Entry Form fill in the details, save, and submit.

### **3.2 Payment via Salary Slip**

1. To pay the Leave Encashment amount via Salary Slip you need to make sure that checkbox Pay via Payment Entry is unchecked.
2. Select the Encashment Date. Based on the date selected, the amount will be encashed in that particular Payroll Entry. Save and Submit. 
On submitting a Leave Encashment for an Employee, Frappe HR automatically creates an [Additional Salary](https://docs.frappe.io/hr/additional-salary) which will get added to the Salary Slip of the Employee when processing the payroll.


**3. Related Topics**
---------------------

1. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
2. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
3. [Additional Salary](https://docs.frappe.io/hr/additional-salary)

  

<!-- page: frappe-hr/hr__leave-ledger-entry.md -->
---
title: "Leave Ledger Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-entry"
updated: "2026-02-26"
---

A unified ledger for all leave related transactions for an employee. This maintains all the leaves related transactions, this includes the leave allocations, leave applications and leave encashments of your employees.

[Screenshot on the live page: Leave Ledger Entry]  


  

<!-- page: frappe-hr/hr__leave-ledger-report.md -->
---
title: "Leave Ledger Report"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-report"
updated: "2026-02-26"
---

This report allows you to view the ledger impact for all your leave-related transactions:

1. Leave Allocation
2. Leave Application
3. Leave Encashment

[Screenshot on the live page: ledger-report]  


This report gives you an overview of:

1. Ledger entry creation date
2. Ledger transaction dates (From Date - To Date)
3. Leaves (added/consumed/deducted)
4. Leave Type
5. Linked transaction details (Type & Name)
6. Any special flags: Is Carry Forward, Is Expired, Is Leave Without Pay
7. Company & Holiday List linked to it

You can use the **View Ledger** button in transactions to view the linked ledger entries in the report view

[Screenshot on the live page: leave-ledger]  


  

<!-- page: frappe-hr/hr__leave-management__help-articles__how-to-sanction-leave-encashment-amount-in-salary-slip.md -->
---
title: "How to Sanction Leave Encashment Amount in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/how-to-sanction-leave-encashment-amount-in-salary-slip"
updated: "2026-07-05"
---

Leave Encashment is used to pay an employee for unused leaves. In Frappe HR, this amount can be paid through a **Salary Slip** or through a separate **Payment Entry**.

This article explains how to sanction the leave encashment amount through Salary Slip.

## When To Use This

Use this method when the encashment amount should be paid along with the employee's regular payroll.

For example, if an employee has unused earned leaves at the end of the year, you can create a Leave Encashment record and include the encashment amount in the employee's Salary Slip for that payroll period.

## Prerequisites

Before creating Leave Encashment, make sure the following are configured:

- The employee has an active **Salary Structure Assignment**.
- The **Leave Type** is marked as encashable.
- The Leave Type has an **Earning Component** set for encashment.
- The employee has a submitted **Leave Allocation** for that Leave Type.
- The employee has unused leave balance available for encashment.
- The per-day encashment amount is set in the Salary Structure or Salary Structure Assignment.

## Step 1: Enable Encashment In Leave Type

Open the relevant **Leave Type** and enable **Allow Encashment**.

You can also configure limits such as:

- Non-encashable leaves
- Maximum encashable leaves
- Earning Component

The Earning Component is important because it decides which salary component will be used when the encashment amount is added to payroll.

## Step 2: Set Leave Encashment Amount Per Day

Open the employee's **Salary Structure** or **Salary Structure Assignment** and set the leave encashment amount per day.

Frappe HR uses this amount to calculate:

```text
Encashment Amount = Encashment Days x Leave Encashment Amount Per Day
```

If the per-day amount is not set, the encashment amount may be calculated as zero.

## Step 3: Create Leave Encashment

Go to:

```text
Home > Human Resources > Leaves > Leave Encashment
```

Create a new Leave Encashment record and select:

- Leave Period
- Employee
- Leave Type
- Encashment Date

The system fetches the employee's leave balance and calculates the encashable days and encashment amount.

## Step 4: Pay Through Salary Slip

To pay the amount through Salary Slip, keep **Pay Via Payment Entry** unchecked.

When the Leave Encashment is submitted, Frappe HR creates an **Additional Salary** record for the employee. This Additional Salary record is linked to the Leave Encashment and uses the earning component selected in the Leave Type.

## Step 5: Process Payroll

Create the **Payroll Entry** or **Salary Slip** for the payroll period that includes the encashment date.

When the Salary Slip is created, the Additional Salary from the Leave Encashment is included in the employee's earnings.

Review the Salary Slip and check that:

- The encashment earning component is visible.
- The amount is correct.
- The total earnings include the encashment amount.

Submit the Salary Slip to sanction and pay the amount through payroll.

## Example

An employee has 5 earned leaves available for encashment.

The leave encashment amount per day is set to 1,000.

```text
5 x 1,000 = 5,000
```

When the Leave Encashment is submitted, Frappe HR creates an Additional Salary for 5,000. The amount is then added to the Salary Slip for the payroll period that includes the encashment date.

## Common Checks

If the encashment amount is not appearing in the Salary Slip, check the following:

- The Leave Encashment is submitted.
- **Pay Via Payment Entry** is not checked.
- The encashment date falls within the Salary Slip or Payroll Entry period.
- The Additional Salary record was created.
- The Additional Salary payroll date is within the payroll period.
- The Leave Type has an earning component.
- The employee has an active Salary Structure Assignment.
- The leave encashment amount per day is configured.

## Salary Slip Or Payment Entry?

Use **Salary Slip** when the encashment should be part of payroll and paid along with salary.

Use **Payment Entry** when the encashment should be paid separately and accounted for directly through accounts.

## Related Topics

- [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)
- [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
- [Additional Salary](https://docs.frappe.io/hr/additional-salary)

<!-- page: frappe-hr/hr__leave-management__help-articles__leave-calculation-in-salary-slip.md -->
---
title: "Leave Calculation in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/leave-calculation-in-salary-slip"
updated: "2026-07-05"
---

Frappe HR calculates leave impact in the Salary Slip by reducing the employee's payable days for the payroll period. This is mainly controlled by Leave Without Pay, Partially Paid Leave, attendance records, holidays, and the employee's joining or relieving date.

The calculation decides two important values in the Salary Slip:

- **Total Working Days**
- **Payment Days**

The salary components that depend on payment days are calculated based on the final Payment Days.

## How Leave Affects Salary Slip

When a Salary Slip is created, Frappe HR checks the payroll period and calculates how many days the employee should be paid for.

In simple terms:

```text
Payment Days = Eligible Working Days - Leave Without Pay - Absent Days
```

The exact calculation can change depending on payroll settings, holiday settings, attendance records, and leave type settings.

## Leave Without Pay

If an employee has an approved Leave Application for a Leave Type marked as **Leave Without Pay**, those days reduce the Payment Days in the Salary Slip.

For example, if the payroll period has 30 working days and the employee has 2 days of Leave Without Pay:

```text
Payment Days = 30 - 2 = 28
```

Salary components that depend on payment days are then calculated for 28 days instead of 30.

## Partially Paid Leave

Frappe HR also supports **Partially Paid Leave**. In this case, the leave does not reduce the full day's salary. It reduces salary based on the fraction configured in the Leave Type.

For example, if a leave type pays 50% of daily salary for one day, the Salary Slip treats it as a partial reduction instead of a full Leave Without Pay day.

Use Partially Paid Leave when employees should receive part of their salary during a leave period.

## Calculation Based On Leave Application Or Attendance

Payroll can be calculated based on either leave applications or attendance records, depending on the payroll configuration.

### Based On Leave Application

When payroll is based on leave applications, Frappe HR checks approved leave records during the Salary Slip period.

It considers:

- Leave Without Pay
- Partially Paid Leave
- Half-day leave
- Whether the Leave Type includes holidays

### Based On Attendance

When payroll is based on attendance, Frappe HR checks submitted Attendance records for the Salary Slip period.

It considers:

- Absent days
- Half-day attendance
- Attendance marked on holidays, depending on settings
- Leave Type used in attendance records
- Unmarked attendance, depending on payroll settings

If unmarked attendance is configured to be treated as absent, those unmarked days can also reduce Payment Days.

## Half-Day Leave And Half-Day Attendance

Half-day leave or half-day attendance reduces salary based on the half-day fraction configured in payroll settings.

For example, if the daily wages fraction for half day is 0.5, then one half-day Leave Without Pay reduces Payment Days by 0.5.

## Holidays In Salary Slip Calculation

Holiday handling depends on payroll settings and the employee's holiday list.

If holidays are included in total working days, holidays are part of the working day count.

If holidays are not included, holidays are removed from Total Working Days before Payment Days are calculated.

Some Leave Types can also be configured to include holidays. If holidays are included for that Leave Type, leave falling on holidays may be considered in the leave calculation.

## Joining Date And Relieving Date

Salary Slip calculation also considers the employee's joining and relieving dates.

If an employee joins in the middle of the payroll period, Payment Days are calculated from the joining date.

If an employee leaves in the middle of the payroll period, Payment Days are calculated only up to the relieving date.

This prevents salary from being calculated for dates before joining or after relieving.

## Example

Suppose the payroll period is from 1 April to 30 April.

- Total days in period: 30
- Holidays excluded from working days: 4
- Total Working Days: 26
- Leave Without Pay: 2
- Half-day Leave Without Pay: 0.5

The Payment Days will be:

```text
26 - 2 - 0.5 = 23.5
```

Salary components that depend on payment days are calculated for 23.5 payment days.

## Why The Salary Amount May Look Different

If the salary amount in the Salary Slip is not what you expected, check:

- Whether payroll is based on Attendance or Leave Application.
- Whether the Leave Application is submitted and approved.
- Whether the Leave Type is marked as Leave Without Pay or Partially Paid Leave.
- Whether holidays are included in Total Working Days.
- Whether the Leave Type includes holidays.
- Whether attendance is marked for the full period.
- Whether unmarked attendance is treated as absent.
- Whether the employee joined or left during the payroll period.
- Whether the salary component depends on payment days.

## Components That Depend On Payment Days

Only salary components configured to depend on payment days are reduced based on leave calculation.

If a component does not depend on payment days, it may remain the same even when Payment Days are reduced.

Check the Salary Component and Salary Structure configuration if a particular earning or deduction is not changing as expected.

## Related Topics

- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Settings](https://docs.frappe.io/hr/payroll-settings)
- [Leave Application](https://docs.frappe.io/hr/leave-application)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Attendance](https://docs.frappe.io/hr/attendance)
- [Holiday List](https://docs.frappe.io/hr/holiday-list)
- [Salary Component](https://docs.frappe.io/hr/salary-component)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)
