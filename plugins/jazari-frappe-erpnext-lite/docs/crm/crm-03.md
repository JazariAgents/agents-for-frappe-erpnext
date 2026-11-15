<!-- Frappe documentation: crm, part 3 of 3. Index: docs/INDEX.md -->

<!-- page: crm/crm__setting-up.md -->
---
title: "Setting Up Your Workspace"
space: "CRM"
url: "https://docs.frappe.io/crm/setting-up"
updated: "2026-04-20"
---

Once you've installed Frappe CRM, you'll be walked through a quick setup before you land in your workspace. It takes about two minutes.

### Step 1: Set your preferences

You'll start with a Welcome screen. Pick your language, confirm your country, set your timezone, and choose your currency. These make sure dates, times, and deal values show up correctly across your CRM.

Hit Next when you're done.

[Screenshot on the live page]
*Setting up your preferences*



### Step 2: Set up your account

Enter your full name and email address. Your email will be your login ID going forward, so use one you actively check.

Hit Complete Setup, and you're in.

[Screenshot on the live page]
*Setting up your first user (you)*

## Frontend and backend

What you're looking at is the CRM frontend. This is what your sales team will use every day. It's clean, focused, and built for speed. When you first land inside the frontend, you'll see some demo data already in place – a few sample leads with names, organizations, and statuses. 

[Screenshot on the live page]

But as the admin, you also have access to a more powerful backend view called **Desk**. 

To get there, click on the **CRM logo** at the top left, then go to **Apps > Desk**.

[Screenshot on the live page]
*To navigate to desk view, click on Apps → Desk*

[Screenshot on the live page]
*The backend view which shows all the apps installed installed on your site*

You'll need it for things like writing scripts, adding custom fields, and some advanced configuration. To navigate around Desk, use the search bar (Command + Shift + K) to quickly find what you're looking for.

We're working on bringing more of this into the frontend, but for now, it's good to know it's there.

## What's next?

Once you're comfortable with the basics, the next step is inviting your team and configuring your CRM to match your sales process. The next few pages cover that.

<!-- page: crm/crm__settings__sales-hierarchy.md -->
---
title: "Sales Hierarchy"
space: "CRM"
url: "https://docs.frappe.io/crm/settings/sales-hierarchy"
updated: "2026-06-02"
---

Arrange your sales team into a reporting tree so managers see the leads and deals owned by their team while everyone else sees only their own.

> Only Admins Can edit the Sales Hierarchy. For others, they can only view it in read-only mode

### Enable Sales Hierarchy

Go to Settings > User Management >  Click on "Enable" button to enable sales hierarchy for your site.

[Screenshot on the live page]
*Enable Sales Hierarchy*

Once enabled:

- Sales Managers see leads and deals owned by themselves and anyone below them in the tree
- Sales Users see only what they own

Note:

- A user with Sales Manager Role cannot directly report to a Sales User
- A Sales Manager who has reportees cannot be demoted to Sales User from the frontend

---

### Adding Users

Click on the "Add User" button from the top right corner to select the users which you want to add to the hierarchy. These users will be added at the top level of the tree. 

[Screenshot on the live page]
*Add users*

**Add direct reports**

Reportees can be added to a manager by clicking the `+` icon. Using this you can bulk assign reportees to a manager to create a hierarchy. 

[Screenshot on the live page]



---

### Removing Users from hierarchy

The are three ways to remove users from the hierarchy. The options depend based on whether the user has someone reporting to them or not. 

#### **Delete**

A user who does not have any reportee can be removed without unlinking by clicking on the delete button

[Screenshot on the live page]



#### **Reassign And remove**

Moves their direct reports up to their own manager and then removes them from the hierarchy

[Screenshot on the live page]



#### **Remove with reports**

Removes the user and everyone reporting to them from the hierarchy. 

[Screenshot on the live page]



---

### **Managing users**

Quickly drag and drop users you want to change reporting for.

[Screenshot on the live page]



#### **Move a user to top level**

A Manger who reports to another manager can be moved to top level along with their reportees. 

[Screenshot on the live page]

<!-- page: crm/crm__task.md -->
---
title: "Task"
space: "CRM"
url: "https://docs.frappe.io/crm/task"
updated: "2026-04-21"
---

If you or your team are still tracking follow-ups on a spreadsheet or a sticky note, you have a better place to do so now.

Tasks are how you make sure things actually get done. Send a proposal, schedule a demo, follow up on a trial, anything with a clear action and a deadline can be a task. They're linked to leads and deals, so everything stays in context.

## The Tasks List

Click on Tasks in the sidebar to see all tasks across your CRM. Each row shows the title, status, priority, due date, and who it's assigned to. You can filter by assignee, priority, status, or due date to focus on what matters right now.

[Screenshot on the live page]
*Inside a Task*

## Tasks inside a Lead or Deal

Each lead and deal has its own Tasks tab. Tasks created here are tied to that specific record. Hit **+ New Task** to create one.

[Screenshot on the live page]
*Task tab inside a Lead / Deal*

Each task has:

- **Title** – What needs to be done
- **Description** – Any additional context or details
- **Status** – Backlog, Todo, In Progress, Done, or Cancelled
- **Assignee** – Who's responsible for it
- **Due Date** – When it needs to be done by
- **Priority** – High, Medium, or Low

## Task Reminders

Frappe CRM will automatically send you a reminder once a day, starting a day before the due date, and again an hour before. Reminders come in as both an in-app notification and an email, so nothing slips through.

[Screenshot on the live page]
*Task reminder send via Email*

<!-- page: crm/crm__twilio.md -->
---
title: "Twilio"
space: "CRM"
url: "https://docs.frappe.io/crm/twilio"
updated: "2026-02-05"
---

Twilio is a cloud communications platform that allows businesses to integrate voice, video, messaging, and authentication functionalities into their applications. This integration enables you to make calls directly from various pages within the CRM.

## Make call

- **Lead page:** A call button is available in the right section above lead details. Use this button to initiate a call, but ensure the **Mobile No** field in the **Person** section includes the country code.
  [Screenshot on the live page]
- **Deal page:** In the **Contacts** section on the right side. You can add multiple contacts and designate a primary contact. The call button will utilize the primary contact's number.  
  [Screenshot on the live page]
- **Contact page:** Directly initiate a call by clicking the **Mobile No** displayed below the contact's name.  
  [Screenshot on the live page]

## Call pop-up

Upon making or receiving a call, a pop-up window appears displaying:

- Caller name
- Mobile number
- Call status
- Call duration
- Mute button
- Note button
- Action buttons (Accept, Reject, Cancel Call)

[Screenshot on the live page]

This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

[Screenshot on the live page]

## Take notes during a call

While on a call, you can take notes using the note button. These notes are saved in the Call Log for later viewing and editing.  

[Screenshot on the live page]

## Twilio setup

To configure Twilio for use within the CRM, follow these steps:

1. **Twilio Subscription:** Obtain an active Twilio subscription (refer to Twilio's documentation for details).
2. **Twilio Credentials:** From your Twilio account, retrieve your Account SID, Auth Token, and Twilio Mobile Number.
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
  [Screenshot on the live page]
4. **Telephony Settings:** Navigate to Telephony Settings, enable Twilio and add your Account SID and Auth Token. You can also enable call recording at this point.
  [Screenshot on the live page]
5. **Telephony Agent:** Go to Telephony Agent (In Desk) and add users (agents) with Twilio mobile numbers designated for making calls.
  Make sure the Twilio number added does not contain spaces and special characters (it can still have + at the start)  
  [Screenshot on the live page]

## Twilio API configuration

For your CRM's API to connect with Twilio, perform the following configurations within Twilio:

1. **Incoming Call API URL:** Under **Phone Numbers** > **Manage** > **Active Numbers**, select your mobile number. Locate the **Voice Configuration** form and within the "**A call comes in**" section, add the following **URL** to the URL field:
  ```
    "https://<yoursitename>/api/method/crm.integrations.twilio.api.twilio_incoming_call_handler"
  ```
  [Screenshot on the live page]
    This URL is responsible for handling incoming calls.
2. **Outgoing Call API URL:** Navigate to **Phone Numbers** > **Manage** > **TwiML apps** and select your app. In the **Voice Configuration** > **Request URL** field, enter the following URL:
  ```
    "https://<yoursitename>/api/method/crm.integrations.twilio.api.voice"
  ```
  [Screenshot on the live page]
    This URL is used for making outbound calls.

:::note
Please refer to Twilio's official guide for any additional Twilio configuration requirements.
:::

<!-- page: crm/crm__view.md -->
---
title: "Saved View"
space: "CRM"
url: "https://docs.frappe.io/crm/view"
updated: "2026-05-21"
---

Saved Views help you personalize list views by saving your preferred filters, sorting, and columns. This allows you to quickly access frequently used lists and data configurations without setting them up each time. You can also consider them as reports.

## What are Views?

A View is a combination of:

- **Filters:** Show records that match specific conditions.
- **Sorting:** Arrange the data in a particular order (ascending, descending, etc.) 
- **Columns:** Choose which fields are visible in the list view.

> **Important Note:** Saved Views are personal by default and only visible to the user who created them. We'll discuss making views public in the next page.

## How to create a View

There are two ways to create a view:

**1. Default View:** You can add filters, sorting, and columns by clicking on **+Add** (as shown in the video below).

[Screenshot on the live page]







- Any changes you make to the default list view, such as applying filters, sorting, or adding/removing columns, are automatically saved.
- When you return to the list view, your personalized configuration will be retained.

**2. Creating a Named View:** 

[Screenshot on the live page]

1. Apply your desired filters, sorting, and column selections.
2. Click the **List** view in the header, then click **+Create View.**
3. Give your Saved View a descriptive name, then click **Create.**

Your newly created Saved View will be accessible from the list view dropdown menu.

## Saved View Actions

The three-dot menu (...) on a Saved View provides additional actions:

- **Duplicate**: Make a copy of the saved view.
- **Edit:** Modify the name and set a custom icon for your saved view.
- **Pin View** (covered on next page): Pin the saved view in the sidebar.
- **Make Public** (covered on next page): Share your saved view with other users. It will be accessible to all users.
- **Delete:** Remove the Saved View from the list.

<!-- page: crm/crm__whatsapp.md -->
---
title: "WhatsApp"
space: "CRM"
url: "https://docs.frappe.io/crm/whatsapp"
updated: "2026-03-09"
---

WhatsApp integration allows you to send and receive WhatsApp messages from within the lead and deal pages in Frappe CRM. This streamlines communication and keeps all interaction history centralised for better customer relationship management.

[Screenshot on the live page: wiki-hero2]



A dedicated WhatsApp tab is available on both Lead and Deal pages, providing a real-time chat window for efficient communication.

- **Lead:** The mobile number field of a Lead is used to initiate and receive WhatsApp messages.
- **Deal:** The primary contact number associated with a Deal is used for WhatsApp communication.

## Installation

WhatsApp integration requires a separate app called "Frappe WhatsApp" developed by [Shridhar](https://github.com/shridarpatil/frappe_whatsapp/commits?author=shridarpatil).

- **Frappe Cloud Marketplace:** The app is available on the Frappe Cloud marketplace for easy installation.  
  [Screenshot on the live page]
- **Manual Installation:** Clone the app's repository from Github: [[https://github.com/shridarpatil/frappe_whatsapp](https://github.com/shridarpatil/frappe_whatsapp)]

## Configuration Steps

To enable WhatsApp integration in Frappe CRM, follow these steps:

1. **Obtain WhatsApp Business Credentials:** Refer to the official WhatsApp guide for creating a WhatsApp Business account and acquiring the necessary credentials [WhatsApp Business Account Creation Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started).
  [Screenshot on the live page]
2. **Configure WhatsApp Settings:**
  [Screenshot on the live page]
   Click the dropdown menu on the top left logo and select "Settings."  
   Locate the **WhatsApp Settings**.  
   Enter the credentials obtained in step 1.  
   Enable the WhatsApp integration.
3. **Set up the Webhook:**
  [Screenshot on the live page]
    A webhook URL is required to establish communication between Frappe CRM and WhatsApp Business. Use the following URL format, replacing `<yoursitename>` with your actual Frappe CRM site name and including the **Webhook Verify Token** you created in the **WhatsApp Settings** in **Verify token** field
    
  [Screenshot on the live page]
4. **Subscribe to webhook fields**:
  Subscribe all webhook fields (recommended - whatsapp docs) but atleast subscribe to `messages` &amp; `message_template_status_update`
    
  [Screenshot on the live page]

## Creating WhatsApp Templates

To ensure compliance and streamline communication, Frappe CRM utilizes WhatsApp templates. These pre-approved messages can be created and managed within the system.

[Screenshot on the live page]

[Screenshot on the live page]



1. Navigate to the **WhatsApp Templates** DocType.
2. Click on **Add WhatsApp Template**.
3. Fill in the required details for your template message.
4. Save the template.

With these configurations in place, you're ready to leverage WhatsApp Business for efficient communication with your leads and deal contacts directly within Frappe CRM.

> **Important Note:** Due to WhatsApp Business limitations, you can only initiate communication by sending a pre-approved WhatsApp template. You can only send regular messages after receiving a reply from the customer.
