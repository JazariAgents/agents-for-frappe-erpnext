<!-- Frappe documentation: frappe-hr, part 6 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__integrating-frappe-hr-with-biometric-attendance-devices.md -->
---
title: "Integrating Frappe HR With Biometric Attendance Devices"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/integrating-frappe-hr-with-biometric-attendance-devices"
updated: "2026-02-04"
---

**Background**
--------------

The Attendance punch logs from the biometric device are check-in and check-out logs of an employee. Frappe HR has a provision to store these logs in a document called Employee Checkin.

Attendance can then be marked based on the [Employee Checkin](https://docs.frappe.io/hr/employee-checkin) records and the [Shift Type](https://docs.frappe.io/hr/shift-type) of the employee by using [Auto Attendance](https://docs.frappe.io/hr/auto-attendance)

Hence, integrating your Biometric Device (*or any access control system that collects IN/OUT logs*), can be done using the following steps:

### **1. Setting up Auto Attendance to mark attendance from the Employee Checkin**

Before you import/sync employees' Check-in and Check-out logs into your Frappe HR system, you will have to set up the employees and their shifts to be able to generate attendance using the Auto Attendance feature in Frappe HR.

Please refer to the following link to set up Auto Attendance: [Set up Auto Attendance](https://docs.frappe.io/hr/auto-attendance)

Once you have set up the employee master and assigned shifts to the employees, you are now ready to proceed to the next step.

### **2. Populating the Biometric Punch Logs into Frappe HR's Employee Checkin**

Depending on your biometric system and its features, there can be a lot of ways you can populate the Punch logs into Frappe HR:

1. **Use the Data Import Tool**:


	* The simplest possible solution (in terms of implementation complexity) would be to generate an Excel/CSV of the Check-in/Check-out and use the built-in data import tool in Frappe HR to periodically import the logs to your Employee Checkin Document
	* Please refer to [Documentation on Data Import Tool](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/data/data-import) for more on how to do this.
2. **API Integration**:


	* You can automate the process of syncing the Biometric Punch Logs by integrating it with the available API in Frappe HR.
	* This method requires some technical knowledge and you should probably get in touch with your Frappe HR implementor or Biometric system vendor.
	* Steps:
	
	
		1. You will first need to create a [user](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users) in your Frappe HR instance that would be used for creating logs since this API method requires login. Make sure this user has all the required permissions to create Employee Checkin.
		2. [Generate API Key and API Secret](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users#210-api-access) for the user which will be used for authentication.
		3. Make sure you have set the [Attendance Device ID (Biometric/RF tag ID)](https://docs.frappe.io/hr/auto-attendance#3-setup-attendance-device-id-field-in-employee) for the employees based on your Biometric Device.
		4. The API implementation details can be found [here](https://github.com/frappe/hrms/blob/d2529e03f92bf50efb65d3163bfcfdacbcf0b8f5/hrms/hr/doctype/employee_checkin/employee_checkin.py#L63-L109) and the API can be accessed at: `/api/method/hrms.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
		5. You can write a script to send a POST request to the API. This endpoint finds the relevant Employee using the employee field value and creates an Employee Checkin. Details of the API endpoint:
		
		
			+ URL: `/api/method/hrms.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
			+ Method: `POST`
			+ Params:
			
			
				- `employee_field_value`: The value to look for in the employee field. This will be the Attendance Device ID found in your biometric logs and also set in the employee record.
				- `timestamp`: The timestamp of the Log. Currently expected in the following format as a string: '2022-04-08 10:48:08.000000'
				- `device_id`: (optional) Location / Device ID. A short string is expected.
				- `log_type`: (optional) Direction of the punch if available (IN/OUT).
				- `skip_auto_attendance`: (optional) Skip auto attendance field will be set for this log (0/1)
				- `employee_fieldname`: (Default: `attendance_device_id`) Name of the field in Employee DocType based on which employee lookup will happen.
				- `latitude`: (optional) Latitude of the shift location if shift location is assigned.
				- `longitude`: (optional) Longitude of the shift location if shift location is assigned.
			+ Response: Returns an Employee Checkin document object which was inserted.
3. **Set up a python script on your computer to integrate ZKTeco or similar devices**:


	* This method works only for ZKTeco or similar devices that use the ZKProtocol to communicate over TCP/IP.
	* This script is available at: [github:frappe/biometric-attendance-sync-tool](https://github.com/frappe/biometric-attendance-sync-tool).
	* Please follow the instructions given on the script page to set it up on your computer.
	* This Script pulls biometric logs from a supported device and uses the API mentioned in the above step to push the data into Frappe HR.

**Frequently Asked Questions**
------------------------------

### **1. How do I select a Biometric Device which is compatible with Frappe HR?**

If you are using method 1 or 2, you don't need to worry about compatibility.

However, for the third method, the push biometric app internally uses a script that is compatible with the devices listed over [here](https://github.com/fananimi/pyzk#compatible-devices). Typically, any ZKTeco or similar device that uses the ZKProtocol to communicate over TCP/IP should work. As far as buying the device is concerned, we suggest you opt for a device trial with the vendor if possible, where the device can be tested with the sync tool, as it's dependent on multiple factors when it comes to compatibility.

### **2. How do I know which method to use for integrating my biometric device with Frappe HR?**

Method 1 is feasible in any situation but requires you to manually import logs periodically. Methods 2 and 3 need some monitoring and work for a one-time setup for the log syncing to be automated.

**For a single location set up:**

In the Push Biometric Device approach, the tool needs to be able to communicate with your biometric device via TCP/IP. So, it is usually the case that it needs to run on the same LAN Network as the biometric device. To sync these fetched logs to your Frappe HR instance it uses API access. This works best when you have a single location set up.

**For a multi-location set up:**

In this case, we usually recommend method 2 where most biometric vendors provide services to sync the biometric device logs from multiple locations to Frappe HR via API access. Method 3 (push biometric attendance tool) can also work in this case if you have some networking knowledge.

  

<!-- page: frappe-hr/hr__interview-feedback.md -->
---
title: "Interview Feedback"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-feedback"
updated: "2026-02-04"
---

**Interview feedback refers to the information and comments provided about a job applicant after an interview.**

The Interview Feedback doctype allows you to assess a Job Applicant's Skills and comment on the Interview in general.

To access Interview Feedback, go to:


> **Home > Human Resources > Recruitment > Interview Feedback**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Interview Feedback, it is advisable you create the following:

* [Interview Round](https://docs.frappe.io/hr/interview-round)
* [Interview](https://docs.frappe.io/hr/interview)

**2. How to Create an Interview Feedback**
------------------------------------------

1. Go to the Interview Feedback list and click on Add Interview Feedback.
2. Select the Interview, Interviewer and Result.
3. Selecting the Interview should automatically populate the Skill Assessment table with the Skills defined in the Interview Round corresponding to the selected Interview. You can then fill out stars for each Skill based on the Job Applicant's performance.
4. Fill in the Feedback section with general feedback regarding the Interview (optional).
5. Click on Save, and then Submit.

![](https://frappehr.com/files/Qg0MQwo.png)  


**3. Features**
---------------

### **3.1 Feedback Summary**

After submitting the Interview Feedback, you can view a summary of all the feedback associated with the Interview under its [Feedback Tab](https://docs.frappe.io/hr/interview#3-2-interview-feedback).

### **3.2 Interview Feedback Reminder**

You can [configure](https://docs.frappe.io/hr/hr-settings#4-2-send-interview-feedback-reminder) Frappe HR to send reminder emails to Interviewers for their Feedback.

**4. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Job Applicant](https://docs.frappe.io/hr/job-applicant)

  


  

<!-- page: frappe-hr/hr__interview-management.md -->
---
title: "Interview Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-management"
updated: "2026-02-04"
---

Frappe HR makes it easy to manage and track multiple interview rounds for job applicants interested in joining your company.

Using this sub-module, you can:

1. [Define Interview Types](https://docs.frappe.io/hr/interview-type) (optional)
2. [Set up Interview Rounds](https://docs.frappe.io/hr/interview-round)
3. [Create Interviews](https://docs.frappe.io/hr/interview)
4. [Fill out Interview Feedbacks](https://docs.frappe.io/hr/interview-feedback)

  

<!-- page: frappe-hr/hr__interview-round.md -->
---
title: "Interview Round"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-round"
updated: "2026-02-04"
---

**Interview rounds are a series of interviews that a candidate goes through during the recruitment process. For example, technical interviews, HR interviews, etc.**

The Interview Round doctype enables you to define and set up these rounds for future [Interviews](https://docs.frappe.io/hr/interview).

To access Interview Round, go to:


> **Home > Human Resources > Recruitment > Interview Round**
> 
> 

**1. How to create an Interview Round**
---------------------------------------

1. From the Interview Round list, click on Add Interview Round.
2. Enter the Round Name.
3. Enter the Interview Type and the Expected Average Rating (optional).
4. You can assign Interviewers, authorizing them to provide feedback for upcoming Interviews of this round.
5. You can also enter Designation to filter Job Applicants during Interview creation.
6. Fill in the Expected Skillset table by clicking on Skill and creating Skills as shown below.

![](https://frappehr.com/files/RgZapW8.png)
7. Save

![135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1](https://frappehr.com/files/135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1.png "135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1.png")  


After saving the Interview Round, you can [Create Interviews](https://docs.frappe.io/hr/interview) directly from the dashboard. The assigned Interviewers can then provide [Feedback](https://docs.frappe.io/hr/interview-feedback) for the created Interviews.

**2. Related Topics**
---------------------

1. [Interview Type](https://docs.frappe.io/hr/interview-type)
2. [Interview](https://docs.frappe.io/hr/interview)
3. [Job Opening](https://docs.frappe.io/hr/job-opening)
4. [Designation](https://docs.frappe.io/hr/designation)

  

<!-- page: frappe-hr/hr__interview-type.md -->
---
title: "Interview Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-type"
updated: "2026-02-04"
---

**Interview type refers to the various types of interviews conducted by an organization, such as panel interviews, walk-in interviews, etc.**

Interview Types can be used to specify the type of interview for a particular [Interview Round](https://docs.frappe.io/hr/interview-round).

To access Interview Type, go to:


> **Home > Human Resources > Recruitment > Interview Type**
> 
> 

**1. How to Create an Interview Type**
--------------------------------------

1. Click on Add Interview Type.
2. Enter the Name and Description
3. Save

![image](https://user-images.githubusercontent.com/24353136/135508652-94fbd439-f953-423c-ba10-990067f308c4.png)  


**2. Related Topics**
---------------------

1. [Interview Round](https://docs.frappe.io/hr/interview-round)
2. [Interview](https://docs.frappe.io/hr/interview)
3. [Interview Feedback](https://docs.frappe.io/hr/interview-feedback)

  

<!-- page: frappe-hr/hr__interview.md -->
---
title: "Interview"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview"
updated: "2026-02-04"
---

**Interviews are formal meetings between Job Applicants and Interviewers to assess whether the former is suitable for the Job Opening they're applying for.**

Frappe HR allows you to maintain a record of all Interviews conducted with Job Applicants.

To access Interview, go to:


> **Home > Human Resources > Recruitment > Interview**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Interview, it is advisable you create the following:

* [Interview Round](https://docs.frappe.io/hr/interview-round)
* [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**2. How to Create an Interview**
---------------------------------

1. Go to Interview list, click on Add Interview.
2. First select the Interview Round and then Job Applicant. Order is important.
3. Enter the date (Scheduled On) and time (From Time & To Time).
4. Enter the Resume Link (optional).
5. Click on Save.

![](https://frappehr.com/files/wNX9smG.png)  


After saving the Interview, you can reschedule the interview using the Reschedule Interview button. You can also directly [Submit Feedback](https://docs.frappe.io/hr/interview-feedback) from the dashboard.

> **Note:** Only Interviewers associated with the selected [Interview Round](https://docs.frappe.io/hr/interview-round) can submit Feedback.

**3. Features**
---------------

### **3.1 Calendar View**

Scheduled interviews can be viewed in a color-coded calendar format by going to the Interview list, clicking on List View, and selecting Calendar.

![image](https://user-images.githubusercontent.com/24353136/135509119-e9584525-7c4e-4384-ab1f-d32e605fcde5.png)  


### **3.2 Interview Feedback**

After an interview has received [Feedback](https://docs.frappe.io/hr/interview-feedback), you can click on the Feedback tab to access a summary of the feedback. This summary includes the overall average rating, the distribution of ratings for each Feedback, the average rating for each Skill, and the individual Feedback comments.

![](https://frappehr.com/files/T7SxrmG.png)  


### **3.3 Tracking Interviews**

Interviews related to a Job Applicant can be easily [tracked](https://docs.frappe.io/hr/job-applicant#3-2-tracking-interviews) from its dashboard.

### **3.4 Interview Reminder**

You can [configure](https://docs.frappe.io/hr/hr-settings#4-2-send-interview-reminder) Frappe HR to send reminder emails to Interviewers for upcoming Interviews.

**4. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Interview Type](https://docs.frappe.io/hr/interview-type)
3. [Interview Feedback](https://docs.frappe.io/hr/interview-feedback)
4. [Job Offer](https://docs.frappe.io/hr/job-offer)

  

<!-- page: frappe-hr/hr__introduction.md -->
---
title: "Frappe HR"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/introduction"
updated: "2026-02-04"
---

Frappe HR is an open Source, modern, and easy-to-use HR and Payroll Software for all organizations. It has everything you need to drive excellence within the company. It is a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

![](/files/imagee5004c.png)

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

![Job Applicant](https://frappehr.com/files/job-applicant.png)  


**3. Features**
---------------

### **3.1 Linking with an Email Account**

You can link Job Application with an Email account. Suppose you link Job Application with an email [job@example.com](mailto:job@example.com), the system will create a New Job Applicant against each email received on the mailbox.

* To link Email Account with Job Applicant, go to:

> Settings > Email Account > New Email Account

* Enter the Email Address and the password, and select 'Enable Incoming'
* In 'Append To' select 'Job Applicant'

![Email Account](https://frappehr.com/files/email-account.png)  


### **3.2 Tracking Interviews**

After creating [Interviews](https://docs.frappe.io/hr/interview), you can easily track them within the Job Applicant dashboard. This enables you to compare all the interviews conducted with the applicant and evaluate their overall performance to make an acceptance decision.

![image](https://user-images.githubusercontent.com/24353136/135509483-97c4f78b-66a4-4a7a-b86f-37f20cf86956.png)  


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

![Job Offer](https://frappehr.com/files/job-offer.png)

> **Note:** A Job Offer can be made only against a [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**3. Features**
---------------

### **3.1 Job Offer Terms**

In this section, you can enter the Job Offer Term such as job description, notice period, incentives, leaves per year, etc. and specify its Value/ Description.

### **3.2 Select Terms and Conditions**

All the Terms and Conditions related to the Job Offer can be specified in this section. To do this, create a new Terms and Conditions template and link it to the Job Offer.

### **3.3 Printing Details**

You can create a pre-designed print format to print you Job Offer. To do so, select the Letter Head and Print Heading in the Printing Details section.

![Job Offer](https://frappehr.com/files/job-offer-print.png)  


  

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

![](/files/Screenshot From 2026-08-10 14-16-21.webp)
*You can also use Job Opening Template to populate the common fields*

Once the Job Opening is saved, you can directly create a new [Job Applicant](https://docs.frappe.io/hr/job-opening) from the dashboard.

:::note
You can close/reopen a Job Opening as and when required. Once a Job Opening is Closed, you cannot create a Job Applicant against it.
:::



## **3. Features**

### **3.1 Job Portal**

You can enable 'Publish on website' to publish a Job Opening to the [Job Portal](https://docs.frappe.io/hr/job-portal). This will make it possible for users to view and apply to these openings from your site.

![](/files/Screenshot From 2026-08-10 14-24-20.webp)

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

  


![273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc](https://frappehr.com/files/273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc.png "273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc.png")
2. You can use the search bar to search for jobs by title or description. You can also filter jobs by company, department, location, or employment type, and sort them by the latest or oldest posting date.
3. Click on a job card to view it in detail.

  


![](https://frappehr.com/files/0CTCsNp.png)
4. Click on the 'Apply Now' button at the top-right corner. This will open a web form where applicants can enter their details.

  


![](https://frappehr.com/files/tyfAC5s.png)
5. Fill in the appropriate details and click on Submit. This will result in the creation of the corresponding Job Applicant document.

  


![](https://frappehr.com/files/xj3PDmO.png)

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

![Job Requisition](https://frappehr.com/files/job_req.png)  


![Job Requisition List](https://frappehr.com/files/job_req_list.png)

**3. Actions**
--------------

### **3.1 Create Job Opening**

Once the Job Requisition is **Open & Approved**, you can create a new Job Opening against the Job Requisition or associate an existing one.

![create job opening](https://frappehr.com/files/create-job-openingafcb2d.gif)  


### **3.2 Associate Job Opening**

If you already have an existing Open Job Opening for that designation, you can associate it with the requisition.

![Associate Job Opening](https://frappehr.com/files/associate-job-opening.gif)  


Once the Job Opening is closed, the Job Requisition's status is updated to **Filled**

**4. Features**
---------------

### **4.1 Check existing Employee Referrals**

If there is an existing Employee Referral for that designation, you might want to consider referrals instead of creating new openings. A banner is visible on the Job Requisition form with the links to these employee referrals in these cases.

![employee referral](https://frappehr.com/files/employee-referral.png)  


### **4.2 Get Job Requisitions in Staffing Plan**

While creating a budget with the Staffing Plan, you can fetch the existing **Pending** or **Open & Approved** Job Requisitions.

![Get Job Requisition](https://frappehr.com/files/get-job-req8e955b.gif)  


### **4.3 Time to Fill Metric**

Time to Fill measures the number of days it takes to fill an open position, from the date a job requisition is posted to the date when it is marked as Filled. This metric is auto-calculated and set in Job Requisition.

The Average Time to Fill is also displayed on the Hiring Dashboard:

![time to fill](https://frappehr.com/files/time-to-fill.png)  


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

![](https://docs.erpnext.com/files/9NHbSR1.png)  


3) Create a **Leave allocation** for the **Employee**.

4) In the **Leave Type list**, for all the types that allow Compensatory off, tick the checkbox.

![](https://docs.erpnext.com/files/zO860kS.png)  


5) Now, create a **Compensatory Leave Request** for the employee.

![](https://docs.erpnext.com/files/QuIeV7V.png)  


6) Go back and check the **Leave allocation** for the leave added for the Employee.

![](https://docs.erpnext.com/files/PstYtuX.png)

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

![Leave Allocation](https://frappehr.com/files/leave-allocation.png)

> **Note:** Enable the 'Add unused leaves from previous allocations' option in case you want to carry forward unused leaves from the previous allocation period for this particular Leave Type.


**3. Features**
---------------------------------------

### 1. Manually adding leaves to the current allocation

If your earned leave allocation failed due to some reasons like background jobs weren’t running, you can manually allocate leaves for an allocation

Click on **Actions > Allocate Leaves**

![Allocate Leaves Button](/files/allocate.png)

And set the number of leaves you want to allocate. You can also set the **From Date** from when these leaves will be applicable. By default, it will consider today’s date.

![Manual Leave Allocation](/files/manual-allocation.png)

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

![Leave Application](https://frappehr.com/files/leave-app.png)
3. Select the Employee Name and Leave Type.
4. Set the Leave duration using From Date and To Date. Based on the dates selected, the 'Total Leave Days' and the 'Leave Balance Before Application' fields will be displayed.
5. If the Leave applied is for a half-day, select the 'Half Day' checkbox.
6. Enter the Reason for Leave.

![Leave Application](https://frappehr.com/files/leave-app1.png)
7. Select Leave Approver.
8. Select the Posting Date of the Leave Application.
9. Check the 'Follow via Email' checkbox to send notification of the Leave Application to the Leave Approver.
10. You can also link the Salary Slip of the Employee in the Leave Application for the record.

![Leave Application](https://frappehr.com/files/leave-app3.png)
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

![Leave Application - Leave Approvers](https://frappehr.com/files/leave-app4.png)  


When an Employee belonging to a particular department applies for leave, the Leave Approvers set in that Employee's department master will be considered as his Leave Approvers.
* **Employee Level:** Leave Approvers can also be set Employee-wise in the employee master.

![Leave Application - Leave Approvers](https://frappehr.com/files/employee-level-approvers.png)

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

![Leave Block List](https://frappehr.com/files/leave-block-list.png)

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

![](https://frappehr.com/files/dZbeNka.png)  



> **Note: Leave cannot be allocated for past dates.**
> 
> 

[Leave Policy Assignments](https://docs.frappe.io/hr/leave-policy-assignment) and [Leave Allocations](https://docs.frappe.io/hr/leave-allocation) made using the Leave Control Panel are reflected in their respective DocTypes as shown below:

* Leave Policy Assignment

![](https://frappehr.com/files/91LxRtw.png)  


* Leave Allocation

![](https://frappehr.com/files/2fi9z2Z.png)  
