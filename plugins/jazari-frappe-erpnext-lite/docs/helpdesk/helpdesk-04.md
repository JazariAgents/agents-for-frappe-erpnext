<!-- Frappe documentation: helpdesk, part 4 of 4. Index: docs/INDEX.md -->

<!-- page: helpdesk/helpdesk__settings.md -->
---
title: "Settings"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/settings"
updated: "2026-05-15"
---

To go to the settings tab click on the dropdown present in the sidebar, then click on settings to open the settings modal. Settings tab will only be shown to the users who are either "System Manager" or "Administrator".

![open setting](/files/open-setting.gif)





Inside the modal, 2 settings are present, let's go through them one by one,

1. Email Accounts.

Inside this settings, user can create a new email account or edit an existing one

![](/files/9XZop8H.png)





To create a new email account click on the "Add Account Button"
	

![](/files/XxFZ65F.png)







Select the email account provider from the list , then fill the fields mentioned in the image above, the form accepts 7 fields

- **Account Name:** The name of your account, it can be support/sales or any other email account for which you are configuring it.
- **Email ID:** The email address of your email account.
- **Password:** App password for your email account which can be found from the link provided in the banner.
- **Enable Incoming:** If enabled, all the emails which you will receive in this account will be created as a ticket in your Helpdesk System.
- **Enable Outgoing:** If enabled, all the replies to the tickets will be sent from this email address.
- **Default Incoming:** If enabled, all replies to your company (eg: [replies@yourcomany.com](mailto:replies@yourcomany.com)) will come to this account. Note: Only one account can be default incoming.
- **Default Outgoing:** If enabled, all outgoing emails will be sent from this account. Note: Only one account can be default outgoing.
- To edit an email account, simply click on the account and you will be able to edit your email account.



![](/files/Screenshot%202025-05-18%20at%2010.16.29%20PM.png)

**Pull Emails:** All emails are pulled every 10 minutes, if you manually want to trigger that, you can click on the "Pull Emails" button to get the latest tickets. This button is only visible when the "Enable Incoming" is checked.

**Note:** Emails will be pulled automatically only if the set email account has not set awaiting password field as 1.

2. Branding

Inside the settings, user can change the logo and favicon of their Helpdesk.

![](/files/DSKMXAD.png)



There are many other settings in Helpdesk to customise the software according to your organisation. These settings can be found in `HD Settings DocType`. 

To go to HD Settings DocType:

1. Switch to [desk](https://docs.frappe.io/helpdesk/service-level-agreement)
2. Type HD Settings in the search bar at the top & press enter. URL path `app/hd-settings/HD%20Settings`

### Details Tab

**Default Priority**  
When enabled, agents will only be able to view tickets that are assigned to [teams](https://docs.frappe.io/helpdesk/lesson-3-agents-teams) they are a part of.

**Team Restrictions**

- Restrict tickets by Team: When enabled, tickets are only visible to members of the team they are assigned to.
- Do not restrict tickets without a Team: This setting is only visible if the above setting is enabled, it allows unassigned tickets to be visible to everyone, that means tickets without any teams or agent_group will be visible to all the teams till some team is assigned to those tickets.
- 

**Restrict agent assignment to selected Team**   



If team restrictions are enabled, tickets can still be assigned to agents outside the assigned team. This feature ensures that tickets can only be assigned to agents within the team specified on the ticket.

To enable it, go to HD Settings and click on "Restrict agent assignment to selected Team"

![](/files/Screenshot%202025-07-30%20at%2010.13.00%E2%80%AFPM.png)

> Note: We need to enable "Restrict tickets by Team" for this setting to work. 

**Prefer knowledge base**  
When enabled, the Knowledge Base becomes the default landing page for users accessing the Customer Portal.

### Ticket Tab

**Default ticket type**  
Set a default type that will be pre-selected when a new ticket is created.

**Ticket type is mandatory**  
If enabled, agents must select a ticket type before creating or updating a ticket.

**Allow anyone to create tickets**  
Allows users to create tickets without needing any specific permission.

**Enable feedback for Customer Portal**  
Users will be required to give feedback before a ticket can be closed.

**Auto update status**  
Automatically changes the ticket status to "Replied" when an agent sends a response.

**Automatically Close Tickets when**  
Enables the system to automatically close tickets if the customer doesn't respond after a reply.

**Auto-close status**  
This field is visible if the "Automatically Close Tickets when" field is enabled. Here you can set the status on which to trigger this functionality.

**Auto-close after (Days)**  
This field is visible if the "Automatically Close Tickets when" field is enabled. Here you can set after how many days the tickets in the status mentioned above closes automatically (e.g: after the ticket has been in resolved status for 3 days the ticket will be closed automatically)

![](/files/Auto%20update.png)

**Enable feedback for Email Tickets**   



Click on "Ticket" tab, and click on "Enable feedback for Email Tickets".

![](/files/1st.png)

Once you enable it, the feedback email will be sent to the customer either when the status of the ticket is "Resolved" or "Closed". You can configure the status on which email is sent by using the field "Send feedback when"

![](/files/2nd.png)

Now once the ticket status is changed to "Resolved" or "Closed", the email is shared with the customer on the same thread. When they click on the button in the email, they are redirected to a "WebForm" on which they can fill the feedback. Once they click on submit, the feedback is attached to the relevant ticket.

When the email is shared, the agent is also notified about it on the frontend via toast:

![](/files/3rd.png)

**Internal working**

Whenever a Ticket is generated, a unique UUID4 key is generated for the document.  
When we set the status of the ticket to either "Resolved/Closed" (depending on your settings), an email is shared to the customer on the same "email thread", when they click on the button, they are navigated to the feedback form (the URL contains the UUID of the ticket which is removed from the URL after a few milliseconds) where they fill in the details.

Once they click on submit, a record is generated in the doctype "HD Email Feedback".

In before_save of this doctype, we check whether the key exists or not in the HD Ticket doctype, if it exists, then the feedback is added to that particular ticket.

> **Note**  
>
> 1. Works for only new tickets.
> 2. Feedback once added the the ticket, cant be changed by the customer.
> 3. Only works for Tickets received via email.



### Search Tab

On the top of settings there is a button called **Regenerate Search Index**. Clicking on it will regenerate the search results which will include the latest articles, also if some error is thrown regarding search you can click on this button to solve the search issue.

This section lets you define how important each field is when someone searches for a ticket or an article.

- **Name Weight**: 1  
- **Subject Weight**: 6  
- **Description Weight**: 5  
- **Headings Weight**: 8

Higher values mean that field will have more weight in the search ranking. You can adjust these weights according to your needs.



### Dark Mode

Helpdesk also supports dark mode.  
To toggle the theme:

1. Click on User Dropdown at the top left corner.
2. Click on Toggle Theme

![](/files/imagea753bb.png)



### Naming Series of Ticket

(Changing the naming of your ticket).



By default the naming series in Helpdesk is "0001" -> "0002" and so on.  



If you wish to alter it to something like "INCD-0001" or "ISS-01" or something else, it is totally possible. Here is a step by step procedure  

1. Go to the URL /desk/hd-ticket
2. Click on overflow menu on the right (triple dots)
  ![](/files/image21eb48.png)
3. Customize
4. Click on "Details" Tab at the top
5. Click on Naming
6. Change Naming Rule to "Expression".

![](/files/image2476eb.png)

Update Auto Name field to "INCD-.#####". Where ##### represent the digits to be followed after the INCD key word. So for e.g. if the naming series is "INCD-.###" then the ticket name would be "INCD-001" and so on.





There are multiple ways to name your Ticket. You can read about it from [here.](https://docs.frappe.io/framework/user/en/basics/doctypes/naming#5-expression)  

<!-- page: helpdesk/helpdesk__team.md -->
---
title: "Team"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/team"
updated: "2026-01-06"
---

In Frappe Helpdesk, a team is a group of support agents or users who collaborate to manage and resolve customer support tickets. Teams are crucial for organizing and distributing workloads, ensuring that customer inquiries are handled efficiently and effectively.

Key Features of Teams in Frappe Helpdesk
----------------------------------------

* **Role Assignment:** Assign specific roles to team members, such as support agents, supervisors, and administrators. This helps define responsibilities and access levels within the helpdesk system.
* **Ticket Assignment:** Automatically or manually assign tickets to specific teams based on criteria such as issue type, priority, or customer. This ensures that tickets are directed to the appropriate group of agents.
* **Collaboration:** Facilitate communication and collaboration among team members to work on resolving tickets. Team members can share notes, updates, and solutions within the ticket interface.
* **Performance Tracking:** Monitor team performance through metrics such as ticket response time, resolution time, and customer satisfaction. This data helps in identifying areas for improvement and recognizing high-performing team members.
* **Workload Distribution:** Balance the workload by distributing tickets evenly among team members. This helps in preventing burnout and ensuring that no single agent is overwhelmed with too many tickets.

Use Cases for Teams in Frappe Helpdesk
--------------------------------------

* **Specialization:** Create specialized teams for different types of issues, such as technical support, billing inquiries, or product-related questions. This ensures that tickets are handled by agents with the appropriate expertise.
* **Regional Support:** Establish teams based on geographic regions to provide localized support and accommodate different time zones and languages.
* **Tiered Support:** Implement tiered support levels (e.g., Level 1, Level 2, and Level 3) where each team handles different levels of complexity. Tickets can be escalated to higher tiers if they require more advanced knowledge or skills.
* **High-Priority Handling:** Form dedicated teams to handle high-priority or urgent tickets, ensuring that critical issues are addressed promptly.

By organizing support agents into teams, Frappe Helpdesk enhances the efficiency and effectiveness of customer support operations, leading to improved customer satisfaction and streamlined support processes.

  

<!-- page: helpdesk/helpdesk__ticket-priority.md -->
---
title: "Ticket Priority"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/ticket-priority"
updated: "2026-08-03"
---

## Overview

The `HD Ticket Priority` DocType defines the urgency levels used to classify helpdesk tickets. Priority determines which tickets need faster attention and, together with the [SLA](https://docs.frappe.io/helpdesk/service-level-agreement), drives the **first response** and **resolution time** targets for every ticket.

## How to Navigate to **HD Ticket Priority**

1. Go to **Desk**.
2. Click on **Search**, type **HD Ticket Priority**, and open the first result.
3. If you can’t find it, open this URL directly in your browser:
  `<site_name>/app/hd-ticket-priority`

## Default Priorities

Helpdesk ships with four priorities out of the box, ordered from most to least urgent:

- Urgent
- High
- Medium
- Low

## Key Properties


| Field           | Type                                                    | Description                                                                      |
| --------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **name**        | Data (set on creation)                                  | The priority’s name shown to agents (e.g. `Urgent`, `High`).                     |
| **level**       | Select — Urgent / High / Medium / Low (Default: Medium) | Severity level used to rank the priority and render its icon in the ticket list. |
| **description** | Small Text                                              | Optional note describing when this priority should be used.                      |
| **disabled**    | Check (Default: 0)                                      | If enabled, the priority is hidden and can no longer be assigned to tickets.     |


## Adding a Ticket Priority

1. Navigate to **Desk** and open **HD Ticket Priority** (see above).
2. Click **+ Add HD Ticket Priority**.
3. Enter a **name**, choose a **level**, and optionally add a **description**.
4. Save.

## Why it's important

Ticket Priority is closely tied to [SLA](https://docs.frappe.io/helpdesk/service-level-agreement) (Service Level Agreement) behavior. When a ticket is created, an SLA is applied to it if one matches, and each SLA defines a different **first response** and **resolution time** for every priority.

If the ticket priority is updated later, the SLA is recalculated based on the new priority, and the **first response** and **resolution time** are updated accordingly. If no SLA covers the new priority, the ticket is left without an SLA and its targets are cleared.

> **A priority only gets targets from the SLAs that list it.**  
> An SLA sets response and resolution targets *per priority*, and applies to a ticket only if it includes that ticket's priority. A priority that no SLA lists is still usable — tickets on it simply have no SLA and no targets. When you add a new priority, add it to whichever SLAs should cover it.

## Use Cases

- Automatically escalate critical issues by assigning higher priorities.
- Control response deadlines with different SLAs for each priority level.
- Trigger custom workflows or automations using server scripts based on priority.

<!-- page: helpdesk/helpdesk__ticket-routing.md -->
---
title: "Ticket Routing"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/ticket-routing"
updated: "2026-03-02"
---

In Frappe Helpdesk, you can automate ticket routing using the Server Script feature. The `Server Script` DocType allows you to write server-side Python code without creating a custom app or deploying anything. Read more about server scripts from [here](https://docs.frappe.io/framework/user/en/desk/scripting/server-script).


## 1.Route tickets based on the type of ticket

![](/files/Screenshot%202025-08-19%20at%2011.16.11%E2%80%AFPM.png)


`agent_group` is the name of the field that translates to "Team".

```python
if (doc.ticket_type == "Bug"):
    doc.agent_group = "Frappe Cloud"
    
elif (doc.ticket_type == "Customization"):
    doc.agent_group = "Billing"

else:
    doc.agent_group = "Product Experts"
```


## 2.Route tickets based on the type of email_account


![](/files/Screenshot%202025-08-19%20at%2011.18.41%E2%80%AFPM.png)

```python 
if (doc.email_account == "Accounting"):
    doc.agent_group = "L1 Accounting"
    
elif (doc.email_account == "Warehouse"):
    doc.agent_group = "L2 Warehouse"

else:
    doc.agent_group = "L1"
```



## 3.Route tickets based on custom fields

To add custom fields follow [this](https://docs.frappe.io/helpdesk/field-dependency#-adding-a-custom-field).
After adding custom fields you can write your script like this to route the tickets based on custom fields


![](/files/Screenshot%202025-08-19%20at%2011.20.27%E2%80%AFPM.png)

```python
if (doc.custom_category == "Frappe Cloud"):
    doc.agent_group = "Frappe Cloud"
    
elif (doc.custom_category == "Accounting"):
    doc.agent_group = "Billing"

else:
    doc.agent_group = "Product Experts"
```

<!-- page: helpdesk/helpdesk__ticket-status.md -->
---
title: "Ticket Status"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/ticket-status"
updated: "2026-01-06"
---

## Overview
The `HD Ticket Status` DocType defines the lifecycle states of helpdesk tickets in the system. It lets administrators control how statuses appear to agents and end-users, how SLAs behave depending on the status, and how statuses are visually represented (e.g., with colors). This DocType helps keep ticket handling, SLA tracking, and reporting consistent.


## How to Navigate to **HD Ticket Status**
1. Go to **Desk**.
2. Click on **Search**, type **HD Ticket Status**, and open the first result.
3. If you can’t find it, open this URL directly in your browser:  
   `<site_name>/app/hd-ticket-status`


## Key Properties

| Field | Type | Description |
|---|---|---|
| **enabled** | Check (Default: 1) | Whether the status is active and available for use. |
| **label_agent** | Data (Required, Unique) | Internal name of the status shown to helpdesk agents. |
| **order** | Int | Sequence in which statuses appear in lists. |
| **different_view** | Check | If enabled, end users will see a different label than agents. |
| **label_customer** | Data | Label shown to end users (mandatory when `different_view` is enabled). |
| **category** | Select (Open / Paused / Resolved) | Controls SLA timer behavior: Open = continues, Paused = paused, Resolved = stops. |
| **color** | Select | Optional color tag for visually distinguishing statuses. |



Setting up a ticket status:
![](/files/Screenshot%202025-08-25%20at%2012.42.11%E2%80%AFPM.png)


---


## Helpdesk Settings (HD Settings)
Global settings define status behavior when tickets are created or reopened:

- **Default Ticket Status** — Status assigned when a ticket is first created.  
- **Reopen Ticket Status** — Status assigned when a ticket is reopened.

These apply system-wide unless an SLA overrides them.


![](/files/HD%20Settings.png)



## Per-SLA Level Configuration
You can set **Default** and **Reopen** statuses per SLA. Preference order:

1. **SLA-level configuration** (highest priority)  
2. **HD Settings** (fallback)

This allows different SLAs (e.g., team A vs team B) to have distinct creation/reopen workflows while maintaining a global default.


![](/files/HD%20SLA.png)

---

## Permissions
Only users with the **System Manager** / **Agent Manager** role can create, modify, or delete ticket statuses.

Available permissions: Create, Read, Write, Delete.

---


## Behavioural Rules
- **Closed** is read-only: only **color** and **order** can be changed.  Closed status is also of the category "Resolved". It can't be deleted.
- If **different_view** is enabled, `label_customer` is mandatory.  
- **category** directly affects SLA timers (Open = continues, Paused = paused, Resolved = stops).
- The system must always have at least one enabled status in each category (Open, Paused, and Resolved). 


This is how status looks like on the Agent Side:


![](/files/TV.png)

<!-- page: helpdesk/helpdesk__ticket-type.md -->
---
title: "Ticket Type"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/ticket-type"
updated: "2026-01-06"
---

Ticket Types help you categorize incoming tickets based on the nature of the issue — such as "Bug", "Feature Request", or "Billing". Adding meaningful ticket types can help teams streamline operations and reporting.

Helpdesk creates for 4 default ticket types for you out of the box.

- Bug
- Incident
- Question
- Unspecified (system generated, can't be deleted)

### Adding a ticket type
1. Navigate to desk.
2. In the search bar on top right corner search for "HD Ticket Type".
3. Click on the first search result.

### Why use Ticket Types?

- **Segregation of tickets**  
  Easily filter and organize tickets by their type for better visibility and workload management.

- **Custom logic with Server Scripts**  
  You can apply different workflows, auto-assignments, or triggers using Server Scripts based on the selected ticket type.

- **SLA Configuration**  
  Define different SLA policies for different ticket types (using the condition field). For example, urgent issues like "Outage" may have a some different SLA applied to the ticket as compared to "General Inquiry". 

<!-- page: helpdesk/helpdesk__ticket.md -->
---
title: "Ticket"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/ticket"
updated: "2026-08-03"
---

In Frappe Helpdesk, a Ticket represents a digital record used to manage and track customer support and service requests. These tickets can be created by customers using Portal or by sending an email to the email address specified by admin.  
  
A Ticket can have an [SLA](https://docs.frappe.io/helpdesk/service-level-agreement) attached to it, which gets updated based on interaction with the customer. Where a ticket has one, both the agent and customer are aware of the expectations of ticket resolution. A ticket that [matches](https://docs.frappe.io/helpdesk/service-level-agreement#sla-assignment-conditions) no SLA policy has none, and shows no response or resolution target![Screenshot 2024-07-17 at 11.52.05 PM](/files/Screenshot 2024-07-17 at 11.52.05 PM.png)  
  


Investigating Ticket
--------------------

A ticket takes the subject and description of the issue from the user and assigns default Status, Priority, SLA, and Type to the Ticket.  
  
A ticket page has everything an agent needs for investigation such as detailed description, customer information, ETA for First Response to the Customer, and Ticket Resolution.  
An agent after investigating the ticket, updates these fields accordingly and based on Type and Priority, an appropriate SLA is set

Screenshot 2024-07-18 at 12.21.32 AM
------------------------------------

Solving Issue
-------------

An agent can solve issues and respond to customers using the [Email](https://docs.frappe.io/helpdesk/email-communication) feature and mark the ticket as resolved. If the customer is satisfied with the solution, he can mark the ticket as closed and give feedback to his liking.  
  
If the customer is not satisfied with the solution, he can reopen the ticket by responding to the agent. If the agent has any queries related to the ticket, he can interact with the customer to gather more information. If the need arises agent can assign the ticket to another agent or escalate it to another team and the next eligible agent will be assigned and can take things forward.

An agent can use the [Comment](https://docs.frappe.io/helpdesk/comment) feature to document his findings which might be helpful for other agents who might work on this ticket or other similar tickets  
  
  

<!-- page: helpdesk/helpdesk__tickets-not-being-created.md -->
---
title: "Tickets not being created?"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/tickets-not-being-created"
updated: "2026-01-06"
---

You may face some issues like, email is being sent to your email account but the tickets are not being created.

If you are facing something similar. Follow this:


1. Go to Desk
2. Go to Email Account => Open your Email Account
3. Click on Incoming Tab

![Screenshot 2025 12 11 at 2.45.59 PM](/files/Screenshot%202025-12-11%20at%202.45.59%E2%80%AFPM.png)


4. Scroll down to the section called IMAP Details 
5. Here configure the the "IMAP Folder" like this

![IMAP](/files/IMAP.png)

Add "INBOX" in "Folder Name"
Add "HD Ticket" in "Append To"

6. Save the document
7. Click on Pull Emails

<!-- page: helpdesk/helpdesk__twilio.md -->
---
title: "Twilio"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/twilio"
updated: "2026-05-21"
---

Twilio is a cloud communications platform that allows businesses to integrate voice, video, messaging, and authentication functionalities into their applications. This integration enables you to make calls directly from various pages within the Helpdesk.

## Twilio setup

To configure Twilio for use within the Helpdesk, follow these steps:

1. **Twilio Subscription:** Obtain an active Twilio subscription (refer to Twilio's documentation for details).
2. **Twilio Credentials:** From your Twilio account, retrieve your Account SID, Auth Token, and Twilio Mobile Number.
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
  ![](/files/Screenshot%202025-08-19%20122908.png)
4. **Telephony Settings:** Navigate to Telephony Settings, enable Twilio and add your Account SID, Auth Token and twilio number. You can also enable call recording at this point.

![](/files/telephony-settings.png)

## Twilio API configuration

For your Helpdesk's API to connect with Twilio, perform the following configurations within Twilio:

1. **Incoming Call API URL:** Under **Phone Numbers** -> **Manage** -> **Active Numbers**, select your mobile number. Locate the **Voice Configuration** form and within the "**A call comes in**" section, add the following **URL** to the URL field:
  ```
    "https://<yoursitename>/api/method/telephony.twilio.api.twilio_incoming_call_handler"
  ```

![](/files/twilio-voice-config.png)

```
This URL is responsible for handling incoming calls. 
```

> By simply adding or removing this incoming call handler you can enable or disable incoming calls.

2. **Outgoing Call API URL:** Navigate to **Phone Numbers** -> **Manage** -> **TwiML apps** and select your app. In the **Voice Configuration** -> **Request URL** field, enter the following URL:
  ```
    "https://<yoursitename>/api/method/telephony.twilio.api.voice"
  ```

![](/files/twilio-app-voice-config.png)

```
This URL is used for making outbound calls.
```

> Please refer to Twilio's official guide for any additional Twilio configuration requirements.



## Make call

- **Ticket page:** A call button is available in the right section above ticket details, use this button to initiate a call.
  ![](/files/ticket-view-call.png)

## Call pop-up

Upon making or receiving a call, a pop-up window appears displaying:

- Caller name
- Mobile number
- Call status
- Call duration
- Mute button
- Action buttons (Accept, Reject, Cancel Call)

![](/files/Diler.png)

This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

![](/files/diler-minimized.png)

<!-- page: helpdesk/helpdesk__your-first-steps-with-frappe-helpdesk.md -->
---
title: "Your First Steps with Frappe Helpdesk"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/your-first-steps-with-frappe-helpdesk"
updated: "2026-05-27"
---

Welcome to Frappe Helpdesk! We’re so glad you’re here. 

We built Frappe Helpdesk because we were tired of tools that were too complicated or too expensive.

This one's different—simple, open-source, and easy for both agents and customers.

In this guide, we’ll help you set up your inbox, invite your team, manage tickets, track SLAs, and chat internally. Just the basics to get you going.

Before you begin, it helps to know how Helpdesk is structured.

### The frontend

The frontend of Helpdesk has two portals:

1. **Agent portal:** This is the first screen you will see. If not accessible, type add **/helpdesk** in the URL. This is where your team manages tickets and replies to customers.

  ![](/files/image%20(14).png)

2. **Customer portal:** Where customers can raise tickets and track updates. To access this, go to **Settings → Customer Portal.**
  ![](/files/image%20(15).png)

### The backend (Desk)

This view only the Admins (System Managers) can access to:

- Set up SLA policies and assignment rules
- Customize ticket forms and workflows
- Manage teams, roles, and permissions

This gives you full control over how your support team operates.

Now that you’ve understood the basic structure of Frappe Helpdesk, let’s dive in and start the setup!

---

### 1. Basic Setup

All your basic setup can be done through the **Settings** in the Agent view.

![](/files/image%20(16).png)

#### a. Upload your logo

To make the support portal your own. Go to Settings → Branding, and update the logo and favicon. This will show up both in your Agent and Customer portal.

![](/files/image%20(17).png)

#### b. Connect your support email account

To set up your email account to send/receive suppot tickets via emails, go to **Settings → Email Accounts**.

Select the email service provider, and for the rest, follow the steps as mentioned [here](https://docs.frappe.io/helpdesk/email-communication#2-how-to-create-an-email-account).

![](/files/image%20(18).png)

#### c. Invite agents

Now that you have your email account set up, add your team so they can start replying to tickets. Go to Settings → Agents → Add Agent. An invitation email will be sent to them. You can then set the their role as Agent or Manager (full access).

![](/files/image%20(19).png)

#### d. Add agents to teams

Create teams from the **Settings → Teams** section in the Agent portal.

Tickets can be assigned directly to agents or routed to a team, where Helpdesk will auto-assign them to a member.

![](/files/image%20(20).png)

Once this is done, you’re ready to define how tickets get handled.

---

### 2. Set SLA

Before tickets start coming in, we need to define how the SLA should be handled. To configure SLAs, switch to the backend (Desk view):

1. Go to **Apps → Desk**

![](/files/image%20(21).png)

1. Search for **“HD Service Level Agreement”** in the search bar. You’ll see the Default SLA already created
2. You can define multiple SLAs for different scenarios — for example, separate rules for Enterprise customers or Indian customers. If no match is found, the **Default SLA** will be applied to all tickets.

![](/files/image%20(22).png)

Here’s what you can configure:

- Set **First Response** and **Resolution** times by priority (High, Medium, Low)
- Choose which statuses pause or complete the SLA
- Define **working hours** so timers only count during business time
- Link a **holiday list** to exclude public holidays from SLA calculations
- Add **conditions** to apply SLAs based on ticket fields (like priority or region)

To see detailed steps and examples, [read the full SLA documentation](https://docs.frappe.io/helpdesk/service-level-agreement).

---

### 3. Set Assignment Rule

Once your SLA is set, you can use **Assignment Rules** to automatically route tickets to the right agents based on conditions.

1. Switch to the **Desk view** (Go to **Apps → Desk**).
2. Search for **HD Assignment Rule** and click **New**.
3. Define a assign, unassign and close condition (e.g., `doc.priority == "High"`) to trigger the rule.
4. Select the Assignment Days on which you want the Assignment Rule to be active
5. Choose how to assign — Round Robin, Load Balancing, or Based on Field.
6. Add users or teams to whom tickets should be assigned.

For examples and advanced conditions using Python expressions, read the full [Assignment Rule documentation](https://docs.frappe.io/helpdesk/assignment-rule).

---

### 4. Creating Tickets

Now that you have everything configured, let's start creating tickets! There are three main ways tickets can be created:

#### a. Customer Portal

Share your Customer Portal URL with your customers so they can directly log in, raise new tickets, and track updates.

If you have [help articles created](https://docs.frappe.io/helpdesk/lesson-4-knowledge-base), your customer should be able to see recommended articles based on subject they’ve typed. Once they’ve created the ticket, agents should be able to see the ticket in the Agent view as well where they work on resolving it. Customers can track SLA and see replies inside the ticket (as and when the Agent responds).

![](/files/image%20(23).png)

#### b. Email

If you want your customers to raise tickets via email (e.g., [support@company.com](mailto:support@company.com)), set one of your email accounts as "Incoming" or "Default Incoming." All emails sent to this address will automatically become tickets every 10 minutes.

#### c. Agent Portal

If your agent receives a customer query through a call or chat, they can manually create tickets in the agent portal. After submitting, you'll immediately see the new ticket.

In the ticket view, you can see ticket details, SLA timers, customer replies, agent assignments, priority settings, team changes, internal comments, and tagging—all in one place.

![](/files/image%20(24).png)

---

### 5. What Next?

Now that you have everything set up, you're good to go. But if you're curious, there's more!

- [Customize ticket forms and add custom fields](https://docs.frappe.io/helpdesk/field-dependency) to suit your team's workflow.
- Save time with [canned responses](https://docs.frappe.io/helpdesk/canned-response).
- Set up a [knowledge base](https://docs.frappe.io/helpdesk/knowledge-base) for self-serve support.
- Configure [notifications](https://docs.frappe.io/erpnext/user/manual/en/notifications) to stay informed.

---

### Need help along the way?

Here are a few links you might find useful:

- 📖 [Documentation](https://docs.frappe.io/helpdesk/introduction?utm_source=setup_guide) – Learn how everything works
- 🌐 [Website](https://frappe.io/helpdesk?utm_source=setup_guide) – Explore features, pricing, and more
- 💬 [Support](https://support.frappe.io/) – Reach out if you get stuck
- 🧩 [Discover other Frappe products](https://frappe.io/products?utm_source=setup_guide) – Check out our open-source tools to make your business more efficient
