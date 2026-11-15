<!-- Frappe documentation: helpdesk, part 3 of 4. Index: docs/INDEX.md -->

<!-- page: helpdesk/helpdesk__lesson-4-knowledge-base.md -->
---
title: "Knowledge Base"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/lesson-4-knowledge-base"
updated: "2026-01-06"
---

The Knowledge Base is a powerful tool for agents to create, organize, and reuse helpful articles when responding to tickets. It helps ensure accurate and consistent replies while reducing time spent typing the same responses.

In addition, these articles are shown on the Customer Portal, allowing customers to find answers and solve issues on their own — which can lead to a **reduction in ticket volume** and faster resolution times. (We will talk about the Customer Portal in the next lesson)

On the sidebar click on "Knowledge Base" or the "book icon" to navigate to Knowledge Base.


---

### Creating a new article

To create a new article:

1. Click the **“+ Add New”** button on the top-right corner
2. A dropdown will appear with two options:
   - **Article**
   - **Category**

Click **“Article”** to get started.


![](/files/Article.png)

> The article will be created under the **General** category by default. You can change the category later inside the article editor.

Edit the title and add some description of the article and click on "Create"

![](/files/New%20Article.png)

You have successfully created your first article🎉

#### Publishing

- New articles are saved in **Draft Mode** (internal only)
- Click **“Publish”** to make it **Public**
  - **Draft Mode**: Visible only to the internal team
  - **Public Mode**: Visible to customers on the Customer Portal

#### Article Actions:

- **Edit** – Modify title, content, or category
- **Move** – Change category of the article.
- **Share Link** – Copy article URL (for customers, if public)
- **Delete** – Remove the article

---

### Creating a new category

Creating categories is optional but important as it helps your organisation to maintain the articles and find them easily.

To create a new category:

1. Click the **“+ Add New”** button on the top-right corner
2. A dropdown will appear with two options:
   - **Article**
   - **Category**

Click on **“Category”**

![](/files/New%20Cate.png)

When you create a new category, a dialog box popus up, add the category name and click on "Create". When a category is created, an article named "New Article" is also created under the newly created category, you can edit the article and click on "Save".

Here is a small video to understand the flow:

![](/files/KB%20New%20Category%20Flow.gif)

---


### Knowledge Base List View

After creating articles and categories, your Knowledge Base would look something like this
In the list view, articles are grouped by categories. You can filter and manage everything from here.

![](/files/Screenshot%202025-04-23%20at%201.06.59%20AM.png)


#### Features in the List View

Each category has "three dots" icon on the right side of it. Clicking on it opens various options:

![](/files/Screenshot%202025-04-23%20at%2012.35.07%20AM.png)

- **Add New Article**
- **Edit Category Title**
- **Merge** this category into another
- **Share** category link
- **Delete** the category  


#### Bulk Actions

- Select multiple articles using checkboxes present on the left side of each row.
- A popover menu appears click on three dots icon, you will see 2 buttons:
  - **Delete** – Removes all selected articles
  - **Move To** – Move selected articles to a different category


> ⚠️ If a category is deleted, all its articles are automatically moved to the **General** category.

> ℹ️ A category must contain at least one article. To move its only article, delete the category instead.


Now that you've understood how the Knowledge Base works from the agent's side — from creating articles to managing categories — let's move on to explore the **Customer Portal** and how customers interact with your support system.

<!-- page: helpdesk/helpdesk__notification.md -->
---
title: "Notification"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/notification"
updated: "2026-05-28"
---

Stay informed about important activities within your Helpdesk system using the Notifications feature. This page serves as a central hub for all your Helpdesk-related alerts and updates.

![Screenshot 2024-07-15 at 12.55.29 PM](/files/Screenshot 2024-07-15 at 12.55.29 PM.png)  


**Accessing Notifications**
---------------------------

1. Locate the **Notifications** option in the sidebar.
2. Click to open the **Notifications Panel**.

**Understanding Notifications**
-------------------------------

The Notifications Panel displays a list of alerts related to your Helpdesk activities. These alerts can currently include mentions in comments, Ticket Assignment, and Ticket re-open.

**Managing Notifications**
--------------------------

Within the Notifications Panel, you can perform the following actions:

* **Open a Notification:** Click on an individual notification to view the specific comment or activity it refers to. This action will also mark the notification as read.
* **Mark All as Read:** Click the dedicated button at the top of the panel to mark all your current notifications as read.


> **Please Note: Future updates will introduce notifications for a wider range of activities.**
> 
> 

<!-- page: helpdesk/helpdesk__other-features__agent-availability.md -->
---
title: "Agent Availability Status"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/other-features/agent-availability"
updated: "2026-06-08"
---

The **Agent Availability Status** feature lets agents communicate their current status throughout their shift, giving team leads and the system a real-time view of who can take on new tickets.

When an agent updates their status, it is immediately reflected across the team, giving other agents and team leads a clear picture of who is currently available. This helps route tickets efficiently so that no work lands with an agent who is unable to respond.

Here is a short walkthrough of the feature in action:

![](/files/Clipboard-20260606-172415-986.gif)

Each agent carries a live availability status  **Active**, **Away**, or **Unavailable** that is shown across the agent portal as a coloured presence dot.

## Setting your Availability

Agents can change their own status from within the agent portal by following the steps below:

1. Click on the dropdown located in the top-left corner of the sidebar and select the **Settings** option.
2. Once the Settings modal is opened, inside in the Profile section find the **Agent Availability Dropdown**
3. Click the **Dropdown** and switch your current status.

![](/files/image134e4c.png)

Selecting a status:

1. On selecting a status the activity indicator in the avatar is updated and a "*Status updated successfully*" toast pops up.
2. Changing the activity status saves it to the agent's **HD Agent** Doctype's**** `availability` field which holds the agents current status and it also sets the `availability_changed_on` field which is very useful in calculation of time since the status was  last changed.

These statuses influence both manual & automatic ticket assignment which can be done via [assignment rules.](https://docs.frappe.io/erpnext/assignment-rule)

For automatic assignment, if a specific agent is away, this feature elegantly handles the situation  by routing the ticket to the next available active agent instead leaving no ticket unassigned.

While manually assigning a ticket through the assignment modal, the team's current statuses are visible at a glance making it easy to have tickets routed to the right person.

## HD Agent Status

The feature is built upon the HD Agent Status Doctype, which defines a set of statuses that can be customised according to the organisation's needs.

An agent can select from the available statuses enabled by the organisation, each belonging to a category that influences the ticket assignment behaviour.  

The three basic categories available currently are as follows:


| Category        | Meaning                               | Automatic Assignment behaviour                                                      |
| --------------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| **Active**      | The agent is available and working.   | Preferred for automatic assignment.                                                 |
| **Away**        | The agent is temporarily unreachable. | Skipped while any Active agent is available; used as a fallback before Unavailable. |
| **Unavailable** | The agent is off.                     | Used only as a last resort, so a ticket is never left unassigned.                   |


Every status belongs to exactly one of three categories. The category — not the status name — is what the routing logic reads, so you can add as many custom statuses as you like (e.g. "On Lunch", "In a Meeting", "Focusing") and slot each into the category that matches how reachable that state really is.

You can create a custom statuses by doing the following steps in the demonstration below:

![](/files/Clipboard-20260606-171744-343.gif)

## How to Navigate to HD Agent Status

- Go to **Desk**.
- Click on **Search in the awesome bar**, type **HD Agent Status**, and open the first result.
- If you can't find it, open this URL directly in your browser:  
`<site_name>/desk/hd-agent-status`

### Key Properties


| Field          | Type                                 | Description                                                                                                       |
| -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `agent_status` | Data (Unique)                        | The status name. This is also the record name (autonamed from this field), e.g. `Active`, `Away`, `In a Meeting`. |
| `enable`       | Check                                | Whether the status is active and offered to agents. Only enabled statuses appear in the agent's status picker.    |
| `status_order` | Int                                  | Sequence in which statuses appear in the picker.                                                                  |
| `category`     | Select (Active / Away / Unavailable) | Drives automatic-assignment behaviour.                                                                            |
| `color`        | Select                               | Colour tag used for the presence dot shown next to the agent's avatar.                                            |


## How automatic assignment picks an agent

Helpdesk overrides Frappe's **[Assignment Rule](https://docs.frappe.io/erpnext/assignment-rule)** (`HelpdeskAssignmentRule`) for **Round Robin**, **Load Balancing**, and **Weighted Distribution** rules. When a ticket needs an assignee, the assignment rule creates a pool of all the available agents which are currently accepting tickets. 

To better understand this, consider the following example.  

There are three agents: Bob, Sam, and Alice. Depending on various scenarios, the ticket assignment will occur as follows: 

1. If Bob is active while Sam and Alice are away, the ticket will be assigned to Bob.
2. If both Bob and Sam are away and Alice is unavailable, the user pool for ticket assignment will be limited to Bob and Sam, and the assignment will follow the configured rules.
3. If Bob, Sam, and Alice are all unavailable, the ticket assignment rule will proceed as usual.

This guarantees a ticket is always assigned to *someone* while still favouring people who are actually around. 

> Rules of type **"Based on Field"** assign through a document field and are unaffected by availability.

### Manual assignment for away agents

Manual assignment is never blocked. From a ticket's **Assignee** picker an agent can be assigned regardless of their status but if the chosen agent is **Away** or **Unavailable**, a warning toast is shown ("*{agent} is currently away.*" / "*{agent} is currently unavailable.*") so the assigner knows the work may not be picked up promptly. 

![](/files/Screenshot 2026-06-05 at 3.34.52 PM.png)

Each agent in the picker shows a coloured presence dot and a tooltip describing their status and how long they've been in it (e.g. "*Away since 5m ago*").

![](/files/image29142b.png)

## Behavioural Rules for HD Agent Status

- `category` is mandatory and must be one of `Active`, `Away`, or `Unavailable`.
- The should be at least **one status** of the `Active` category enabled at all times.
- `agent_status` is unique and autonames the record, so two statuses cannot share the same name.
- **Only enabled statuses are offered** to agents in the availability picker.

<!-- page: helpdesk/helpdesk__other-features__agent-home-page.md -->
---
title: "Agent Home Page"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/other-features/agent-home-page"
updated: "2026-05-28"
---

The Agent Home Page is a dynamic, customizable dashboard designed to give support agents a comprehensive overview of their daily tasks, performance metrics, and customer satisfaction levels. It acts as the central hub for agents to track their productivity and prioritize their workflow.



![](/files/image0d0533.png)
*Agent Home Page*

### Key Features

- **Customizable Layout:** Drag, drop, resize, and reorder widgets to suit individual preferences.
- **Real-time Metrics:** Data is fetched directly from the Helpdesk backend to ensure agents are always looking at the most up-to-date information.
- **Period Filtering:** Most widgets support quick time-duration toggles (e.g., Last week, Last month, Last 3 months) to analyze trends over different periods.
- **Quick Actions:** Clickable links within widgets allow agents to jump directly to specific tickets or filtered ticket lists.

---

### Available Dashboard Widgets

#### 1. My Tickets

A metric card that displays the total number of tickets assigned to the agent for a selected period.

- **Visuals:** Includes a line chart tracking ticket volume over time.
- **Insights:** Shows a percentage change (increase or decrease) compared to the previous duration (e.g., vs last month), highlighting volume trends.

#### 2. Average First Response Time

A dedicated card tracks how quickly an agent sends the first reply to a customer.

- **Visuals:** Rendered with a red-themed line chart and gradient.
- **Insights:** Displays the average time formatted in days, hours, and minutes, along with the percentage change to monitor responsiveness improvements.

#### 3. Average Resolution Time

A dedicated card tracking the average time taken to fully resolve and close tickets.

- **Visuals:** Rendered with a purple-themed line chart and gradient.
- **Insights:** Similar to the First Response card, it shows the formatted average time and percentage change, helping agents gauge their problem-solving efficiency.

#### 4. Average Time Metrics

A comprehensive bar chart widget that compares the "Average First Response Time" and "Average Resolution Time" side-by-side.

- **Visuals:** Dual-bar chart visualization.
- **Filters:** Supports longer historical filters: 3 Months (3M), 6 Months (6M), and 1 Year (1Y).
- **Usage:** Ideal for recognizing long-term performance trends and identifying operational bottlenecks.

#### 5. Pending Tickets

An actionable list view of tickets requiring the agent's attention. This widget is categorized into three distinct tabs:

- **SLA Alerts:** Tickets that are approaching or have already breached their Service Level Agreement (SLA). Flags overdue items in red.
- **Pending:** Tickets currently awaiting an agent response.
- **Recent:** New tickets assigned to the agent within the last 24 hours.
- **Details Displayed:** Ticket ID, Subject, Status, Priority (color-coded badges), Team/Group, and Reason (e.g., upcoming SLA, pending status).

#### 6. Reviews (Recent Feedback)

A two-panel widget summarizing customer satisfaction and recent feedback.

- **Left Panel (Summary):** Displays the overall average star rating (1 to 5), total number of reviews, a performance assessment label (e.g., "excellent", "good"), and a bar chart showing the distribution of ratings.
- **Right Panel (Detailed Feedback):** A carousel of individual customer reviews. Agents can navigate through reviews using the previous/next buttons. 
- **Filters:** Agents can filter reviews by period (All Time, Last Week, Last Month, Last 3 Months) and sort them (Positive first, Negative first).

---

### Managing the Dashboard

Agents can tailor the Home Page to display only the metrics that matter most to them.

#### Editing the Layout

1. Click the **Edit** button in the top right corner of the header.
2. **Move:** Click and drag any widget to a new position on the grid.
3. **Resize:** Drag the bottom-right corner of a widget to expand or shrink its size (widgets have predefined minimum and maximum dimensions to preserve UI integrity).
4. **Remove:** Hover over a widget while in edit mode and click the **Trash** icon in the top right corner to remove it from the dashboard.

#### Adding New Widgets

1. While in Edit mode (or via the **New** dropdown if the dashboard is empty), click the **New** button in the header.
2. Select a widget from the dropdown list (e.g., "Pending Tickets", "Reviews").
3. The new widget will automatically appear at the top of the dashboard, ready to be placed.

#### Saving or Resetting

- **Save:** Once the layout is arranged as desired, click **Save** to apply the changes to your user profile.
- **Cancel:** Click **Cancel** to discard any unsaved layout changes and revert to the previous state.
- **Reset:** If the layout has been customized but you want to return to the system default, enter Edit mode and click the **Reset** button.

<!-- page: helpdesk/helpdesk__other-features__bulk-reply.md -->
---
title: "Bulk Reply"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/other-features/bulk-reply"
updated: "2026-05-29"
---

# Bulk Reply

Bulk Reply lets an agent send the **same response to several tickets at once**, instead of opening each ticket and replying one by one. Each customer still receives a private, individual reply on their own ticket; they never see that the message went to anyone else.    





## How to use it

1. Go to the **Tickets** list.
2. **Select the tickets** you want to reply to using the checkboxes on the left of each row. A selection bar appears at the bottom.
3. Click **Bulk Reply** in the selection bar.
4. In the **Bulk Reply** window, type your message in the editor.
5. (Optional) Add attachments — see [Attachments](#attachments) below.
6. Click the send button:
  - **Send Reply** when one ticket is selected.    
  - **Send to N tickets** when several are selected (N shows the exact count).

> 💡 **Shortcut:** Press **⌘ + Enter** (Mac) or **Ctrl + Enter** (Windows/Linux) to send without reaching for the mouse.



For each ticket, the reply is sent to **the person who raised that ticket** (the ticket's requester).  
When the reply is sent, you'll see a confirmation like *"Bulk reply sent successfully to 5 tickets."*  
The message is recorded in each ticket's conversation, exactly as if you had replied to each one individually. 



## Signature is added automatically

Your **email signature is inserted into the reply for you** — you don't need to type or paste it. The editor opens with your signature already in place, and the cursor positioned above it so you can start writing straight away.

The signature comes from your personal email signature in Helpdesk. If you'd like to change what appears, update your signature in your settings, and it will be used the next time you reply. 



## Attachments

You can attach files (screenshots, PDFs, documents) to a bulk reply:  

1. Click the **attachment (paperclip) icon** in the editor toolbar.
2. Choose the file(s) to upload. Each file appears as a chip below the editor once uploaded.
3. To remove a file before sending, click the **✕** on its chip.  Every attachment you add is included with the reply sent to **each** selected ticket, and is also saved on each ticket so it's available later in the ticket's attachments.

>  ⏳ Wait for files to finish uploading — the send button stays disabled until uploads complete.



## Good to know

- **Drafts are remembered.** If you close the window before sending, your typed message and attachments are kept. They're cleared only when you **Send** or click **Discard**.
- **Each reply is private.** Customers receive only the reply on their own ticket — recipients are never exposed to each other.
- **Discard** closes the window and clears the draft without sending anything.



## Frequently asked

Q) Does the customer know this was a bulk reply?

A) No. Each customer sees a normal, individual reply on their ticket.



Q) Can I reply to just one ticket with this?

A) Yes — select a single ticket and the button reads **Send Reply**. It works the same as a regular reply, with your signature added automatically.



Q) Who receives the reply?

A) For each ticket, the reply goes to the person who raised that ticket. It's emailed to them according to your Helpdesk's email settings, and is also stored in the ticket's conversation.

<!-- page: helpdesk/helpdesk__pwa-installation.md -->
---
title: "PWA Installation"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/pwa-installation"
updated: "2026-01-06"
---

###Safari Browser

1. Click on the share button (middle one in the bottom navbar)

    <img width="199" alt="Screenshot 2024-09-26 at 10 22 41 AM" src="https://github.com/user-attachments/assets/d7505f08-96ce-4b58-a920-eea223e568b6">

2. Click on Add to Home screen button

    <img width="199" alt="Screenshot 2024-09-26 at 10 22 42 AM" src="https://github.com/user-attachments/assets/acf4d19e-63e3-444c-9f9d-1289463300e9"> 

3. Click on Add

    <img width="199" alt="Screenshot 2024-09-26 at 10 22 41 AM" src="https://github.com/user-attachments/assets/3f95257a-6fce-4b98-b90b-0f89233b5c8b">


4. Login Once, and you are done ✅

###Chrome Browser

1. Click on Share Icon (position might differ for android phones)

    <img width="199" alt="Screenshot 2024-09-26 at 10 22 41 AM" src="https://github.com/user-attachments/assets/174a1ad4-2c9b-44a9-af3a-a3ad94155166">

2. Click on Add to Home Screen

    <img width="199" alt="Screenshot 2024-09-26 at 10 22 41 AM" src="https://github.com/user-attachments/assets/664087cb-4c2f-4e71-9cf6-eaaa5b6b8f57">

3. Click on Add

4. Login Once, and you are done ✅

<!-- page: helpdesk/helpdesk__saved-replies.md -->
---
title: "Saved Replies"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/saved-replies"
updated: "2026-08-12"
---

Saved replies in Frappe Helpdesk are pre-written replies that support agents can use to respond to common customer inquiries quickly and consistently. These templates help streamline communication, ensuring that customers receive prompt and accurate information.

![saved reply](/files/saved-reply.png)

Key Features of Saved Replies
--------------------------------

1. **Pre-Written Templates**: Saved replies are ready-made templates for common questions and issues, saving agents time when replying to frequently asked questions.
2. **Dynamic fields**: Saved replies supports dynamic field using jinja templates. For dynamic fields here are all the fields available

    **Ticket** - All ticket fields including any custom field that you may have added
    
    **User** - email, first_name, middle_name, last_name, full_name, username, user_image, phone, location, bio, mobile_no
    
    Here are some examples:
    
    **1. First Response**
    ```
    Hello {{ contact }},
    
    We are sorry for the inconvenience, we will get back to you soon. 
    
    Regards, 
    {{ full_name }}
    ```
    
    **2.Refund Confirmation**
    
    Example for custom field in HD Ticket doctype e.g `order_number`
    
    ```
    Hi {{ contact }},
    
    Your refund for order {{ order_number }} has been processed. It may take 3–5 business days to appear in your account, depending on your bank.
    
    Let us know if you need anything else!
    
    Warm regards,
    {{full_name}}
    ```

3. **Customization**: While saved replies are pre-written, they can be customized to suit the specific context of a customer inquiry, allowing for a personal touch.
4. **Easy Access**: Agents can easily access and insert saved replies into their replies from within the helpdesk interface, improving efficiency.
5. **Consistency**: Ensures that all customers receive consistent and accurate information, maintaining a high standard of support.
6. **Bulk Actions**: Useful for sending similar information to multiple customers simultaneously, particularly during incidents affecting multiple users.
7. **Actions**: A saved reply can also update the ticket for you, for example set the status, assign an agent or add a tag, when the reply is sent.

## Scope Feature

The Scope feature allows you to control the visibility and accessibility of saved replies across your support team. Each saved reply can be configured with one of three scope levels, providing granular control over who can access and use specific templates.

### Scope Types

1. **Global**

   - Visible to **all agents**
   - Ideal for company-wide templates that every support agent should have access to
   - Examples: Standard greetings, company policies, general troubleshooting steps
   - Can be disabled system-wide using the HD Settings option (see Settings below)

2. **Team**

   - Visible to **members of specific teams** only
   - You can assign a saved reply to one or more teams
   - Perfect for department-specific or team-specific responses
   - Examples: Technical support templates for the Tech Team, billing templates for the Finance Team
   - Behavior changes based on the "Restrict Tickets by Agent Group" setting

3. **Personal**
   - Visible **only to the owner** (creator) of the saved reply
   - Ideal for individual agent preferences and frequently used custom responses
   - Other agents cannot view or use personal saved replies

### Visibility Rules Summary

| Scope    | Owner | Same Team Members    | Other Agents         | Admins |
| -------- | ----- | -------------------- | -------------------- | ------ |
| Global   | ✅    | ✅                   | ✅                   | ✅     |
| Team     | ✅    | ✅ (when restricted) | ❌ (when restricted) | ✅     |
| Personal | ✅    | ❌                   | ❌                   | ✅     |

> [!NOTE]
> System Managers and Agent Managers always have full access to all saved replies regardless of scope settings.

### Disable Saved Replies Global Scope

To disable global scope for saved replies, go to settings modal from top left corner and click on settings or from desk go to **HD Settings**. Enable **Restrict tickets by team**, **Disable global scope for saved replies** will appear below it, enable it and save.


## Actions

Most replies come with follow-up work. An escalation reply usually also moves the ticket to another team, a resolution reply closes it, a first response bumps the priority. Actions let you attach that work to the saved reply itself, so the agent writes the reply once and the ticket is updated for them.

Actions run **after the reply email is sent**, on the ticket the reply was sent from.

![saved reply actions](/files/docs-actions-editor.png)

### Available Actions

| Action | What it does | Value |
| ------ | ------------ | ----- |
| **Set status** | Sets the ticket status | An enabled ticket status |
| **Set priority** | Sets the ticket priority | An enabled priority |
| **Set team** | Moves the ticket to another team | An enabled team |
| **Set ticket type** | Sets the ticket type | An enabled ticket type |
| **Assign agent** | Assigns the ticket to a specific agent | An active agent |
| **Assign to me** | Assigns the ticket to whoever sends the reply | No value needed |
| **Add tags** | Adds one or more tags to the ticket | Tags, new ones are created if they do not exist |
| **Remove tags** | Removes one or more tags from the ticket | Tags |
| **Add comment** | Adds an internal comment to the ticket | Rich text, visible to agents only |

### Rules

- A saved reply can use **only one assignment action**, either Assign agent or Assign to me.
- The same action with the same value cannot be added twice.
- The same tag cannot be added and removed in one reply.

### Adding Actions to a Saved Reply

1. Go to the Saved Replies section in the settings modal and open a saved reply, or create a new one.
2. Scroll to the **Actions** table below the message.
3. Click **Add action**, pick an action from the dropdown, then pick its value.
4. Use the row menu on the right to delete a row.
5. Save the saved reply.

### Using Actions While Replying

1. Insert the saved reply in the reply editor as usual.
2. Its actions appear in a strip above the editor, showing the reply name and how many actions are staged.
3. Expand the strip to review the actions. You can change a value, remove a single action, or clear all of them before sending. A comment action can be edited inline, and whatever is in the editor at send time is what gets added.
4. Send the reply. The actions are applied to the ticket right after the email goes out, and the ticket refreshes with the changes.

![saved reply actions in the reply editor](/files/docs-actions-composer.png)

> [!NOTE]
> Actions are applied with the permissions of the agent sending the reply. An agent who cannot edit the ticket cannot apply actions to it either.

### When an Action Cannot Be Applied

Targets change over time, a team gets disabled, an agent is deactivated, a ticket type is removed. Helpdesk handles this quietly instead of blocking the reply:

- Actions whose target no longer exists are **dropped when the saved reply is inserted**, so an agent never stages one that is bound to fail.
- Anything that turns invalid between insert and send is **skipped at apply time** and reported in a notification, the rest still apply.
- If applying the batch fails altogether, an error notification offers a **Retry**. The email itself is already sent and is never affected.


Use Cases for Saved Replies
------------------------------

* **Common Queries**: Quickly respond to frequently asked questions about products, services, policies, or procedures.
* **Troubleshooting Steps**: Provide step-by-step instructions for resolving common technical issues.
* **Acknowledgments**: Send quick acknowledgments of receipt for new support tickets or inquiries.
* **Follow-Up**: Send follow-up messages to customers, ensuring they have all the information they need and checking on the status of their issue.
* **General Information**: Share general information, such as office hours, contact details, or links to the Knowledge Base.
* **Escalations**: Move a ticket to the right team, raise its priority and drop an internal note, all from one reply.

Benefits of Saved Replies
----------------------------

* **Efficiency**: Significantly reduces the time agents spend composing responses, allowing them to handle more tickets in less time.
* **Consistency**: Maintains uniformity in responses, ensuring that all customers receive the same high-quality information.
* **Accuracy**: Minimizes the risk of errors or omissions in replies, as the responses are pre-approved and standardized.
* **Speed**: Enhances response times, leading to quicker resolutions and improved customer satisfaction.
* **Training**: Serves as a training tool for new agents, providing them with examples of appropriate responses.
* **Fewer missed steps**: Actions make sure the ticket is updated the same way every time a given reply is sent.

How to Use Saved Replies in Frappe Helpdesk
----------------------------------------------

1. **Creating Saved Replies**:


	* Navigate to the Saved Replies section in the settings modal.
	* Click on "New Saved Reply" and enter a descriptive title.
	* Write the pre-written message in the content section, including any placeholders for customization.
	* Optionally, add actions that should update the ticket when this reply is sent.
2. **Using Saved Replies**:


	* When replying to a ticket, click on the saved reply icon in the reply editor.
	* Select the appropriate saved reply from the list.
	* Customize the message if needed to address the specific context of the inquiry.
	* Review the staged actions, if the reply has any.
	* Send the response to the customer. 
	
![saved reply insert](/files/saved-reply%20insert.gif)

By utilizing saved replies, Frappe Helpdesk can enhance the efficiency and effectiveness of support operations, ensuring that customers receive prompt, accurate, and consistent information.

<!-- page: helpdesk/helpdesk__service-level-agreement.md -->
---
title: "Service Level Agreement"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/service-level-agreement"
updated: "2026-08-03"
---

A **Service Level Agreement (SLA)** is a formal agreement between a service provider and a customer that defines the level of service expected. It sets clear expectations by outlining key metrics such as response times, resolution times, service availability, and responsibilities. SLAs help ensure accountability by establishing measurable standards and consequences if those standards are not met. 
In helpdesk systems, SLAs are critical for tracking how quickly and efficiently support teams handle customer issues, maintaining service quality, and improving customer satisfaction.

Creating an SLA
---------------

1. **Go to settings:** Click on logo at top left corner and click settings option
![](/files/Screenshot%202025-07-03%20110517.png)

2. **SLA Policies:** Click on "SLA Policies" in the left sidebar and click "New" at top right corner
![](/files/Screenshot%202025-07-03%20110645.png)

3. **Define SLA Details:** Fill the form with all required details
![](/files/Screenshot%202025-07-03%20111322.png)

Each SLA is linked to the `HD Ticket` doctype and includes:

- **Default Priority**: Used when a ticket doesn’t have a priority set.
- **Enabled**: Ensures the SLA is active.
- **Valid From / To**: Optional start and end date for this SLA.

---

### Response and Resolution

You can define different **First Response Time** and **Resolution Time** for each [priority](https://docs.frappe.io/helpdesk/ticket-priority):

| Priority | First Response Time | Resolution Time |
|----------|---------------------|-----------------|
| Low      | 24h                 | 72h             |
| Medium   | 8h                  | 24h             |
| High     | 1h                  | 4h              |
| Urgent   | 30m                 | 2h              |


### Status-based Triggers

#### SLA Fulfilled On:
These statuses indicate the SLA has been fulfilled:

- **Resolved**
- **Closed**

#### SLA Paused On:
These statuses pause the SLA timer:

- **Replied**

When a ticket is in "Replied" state, the resolution timer is paused until the customer responds.

---

### Working Hours

SLAs respect your business hours, which you can define in the **Working Hours** section:

| Workday    | Start Time | End Time   |
|------------|------------|------------|
| Monday     | 10:00 AM   | 6:00 PM    |
| Tuesday    | 10:00 AM   | 6:00 PM    |
| Wednesday  | 10:00 AM   | 6:00 PM    |
| Thursday   | 10:00 AM   | 6:00 PM    |
| Friday     | 10:00 AM   | 6:00 PM    |

Tickets created or due outside of these hours will have their SLA timers paused until working hours resume.

---

---

### Holiday List

You can link a **Holiday List** to exclude specific dates from SLA time tracking (e.g., public holidays). SLA timers will automatically pause on the dates included in the selected Holiday List. 

#### Creating an Holiday list

1. **Go to settings:** Click on logo at top left corner and click settings option
![](/files/Screenshot%202025-07-03%20110517.png)
2. **Business holidays:** Click on "Business holidays" in the left sidebar and click "New" at top right corner
![](/files/Screenshot%202025-07-03%20121953.png)
3. **Define Business holidays Details:** Fill the form with all required details
![](/files/Screenshot%202025-07-03%20122153.png)

##### Recurring holidays
![](/files/Screenshot%202025-07-03%20133310.png)
Recurring holidays such as weekends can be added from Recurring holidays section, these holidays will be auto generate for duration of "From date" and "To date" set for the respective holiday list

##### Calendar view for holidays
![](/files/Screenshot%202025-07-03%20133620.png)
Holidays and recurring holiday can be viewed from calendar view, where holiday dates are represented by light yellow and orange background, recurring holidays are represented by grey background.
You can click on any date on the calendar to add holiday directly or by clicking on "Add Holiday" button at the bottom of the page

##### List view for holidays
![](/files/Screenshot%202025-07-03%20134234.png)
By clicking on list icon above calendar view you can toggle between calendar and list view

Example:  
If a holiday falls on a Tuesday, and a ticket is created on Monday evening with an 8h SLA, the SLA timer will resume on Wednesday morning (assuming Tuesday is a holiday).

---


### SLA Assignment Conditions

Frappe Helpdesk lets you assign SLAs to tickets dynamically using **conditions**.

An SLA applies to a ticket only when **both** are true:

1. its **condition** matches the ticket, and
2. its priority table **includes the ticket's priority**.

A policy whose condition matches but which does not list the ticket's priority is skipped, and the next one is tried.

#### Condition-based SLA

Each SLA can define a condition using the UI in Assignment conditions section. These conditions are evaluated against ticket fields using the `doc` object.

**Example Condition:**

In the image below, conditions defined in the UI will be automatically converted into the condition string and store it in the backend
![](/files/Screenshot%202025-07-03%20112s024.png)
Converted condition string:
```python
doc.agent_group == 'Billing' and doc.ticket_type == 'Bug' and (doc.custom_app == 'FC' or doc.resolution_date == '2025-07-22 11:41:31' or doc.priority == 'Low')
```
Also as you can see in the above image, at any level at a time, same type of conjunction (and,or) can be used, one level cannot have both the conjunctions at the same time.

#### Rank

When more than one SLA matches, **Rank** decides which is tried first. A lower rank wins. `0` means unranked and is applied last, so an unranked policy never overtakes one you have deliberately ranked. Policies on the same rank are tried oldest first, so adding a new SLA never silently takes over tickets an existing one already handles.

The SLA Policies list in Settings is sorted the same way, so what you see top to bottom is the order Helpdesk tries them in.

#### Default SLA

An SLA marked **Default** needs no condition and is always considered **last**, after every conditional policy. It still only applies if it includes the ticket's priority.

Marking an SLA as Default is optional — you can untick it, disable it, or delete it.

#### Tickets without an SLA

If no policy matches, the ticket has no SLA: no first response or resolution target is set. This is a normal state, not an error.

A ticket can also lose its SLA later — its priority changes to one the policy does not cover, its condition stops matching, or the policy is disabled. The targets are cleared on the ticket's next update, but a breach that already happened is kept, so a ticket that failed still shows **Failed**.

If it matches a policy again later, targets are recalculated from when the SLA first attached — the clock does not restart.

### How is SLA calclulated?



Some definitions:

1. First Response Due: The time at which the first response should be made, considering working hours and holidays.
2. Resolution Due: The time by which the ticket should be resolved, also considering working hours and holidays.

While calculating these 2, the factors which are considers are:
1. Working Hours
2. Holiday list
3. Total hold time of the ticket (for how long the ticket was in "Replied" state)

Some points we are assuming before doing calculations

1. Working Hours: The company operates between 10:00 AM and 6:00 PM from Monday to Friday.
2. Holiday List: Every Saturday & Sunday is a holiday, and SLA timers pause during holidays.


### Scenario 1: Ticket Created with High priority on a Tuesday (working day)
#### Ticket Created: Tuesday, 5:00 PM  
- **SLA for First Response**: 4 hours (High priority)  
- **SLA for Resolution**: 8 hours (High priority)  
- **Holiday List**: All Saturdas & Sundays are holidays.  
- **Working Hours**: 10:00 AM to 6:00 PM (Monday to Friday)  
- **Status**: `Resolved` (SLA fulfilled once status changes)

#### First Response Calculation:
- **First Response Time** is 4 hours.
- Created at 5:00 PM on Tuesday.
- The timer will run for 1 hour on Tuesday (5:00 PM to 6:00 PM).
- The remaining 3 hours will be counted from Wednesday, starting at 10:00 AM.
- **First Response Due**: Wednesday, 1:00 PM.

#### Resolution Calculation:
- **Resolution Time** is 8 hours.
- 1 hour used from 5:00 PM to 6:00 PM on Tuesday.
- The remaining 7 hours will be counted from Wednesday, starting at 10:00 AM.
- **Resolution Due**: Wednesday, 5:00 PM.

---



### Scenario 2: Ticket Created Before a Holiday (On Friday)

#### Ticket Created: Friday, 4:00 PM  

- **SLA for First Response**: 8 hours (Medium priority)  
- **SLA for Resolution**: 24 hours (Medium priority)  
- **Holiday List**: All Saturdas & Sundays are holidays.  
- **Working Hours**: 10:00 AM to 6:00 PM (Monday to Friday)  
- **Status**: `Replied` (Resolution timer paused until customer response)

#### First Response Calculation:
- **First Response Time** is 8 hours.
- Created at 4:00 PM on Friday.
- The timer will run for 2 hours on Friday (4:00 PM to 6:00 PM).
- The remaining 6 hours will be counted from Monday, starting at 10:00 AM.
- **First Response Due**: Monday, 4:00 PM.

#### Resolution Calculation:
- **Resolution Time** is 24 hours.
- 2 hours used from 4:00 PM to 6:00 PM on Friday.
- The remaining 22 hours will be counted from Monday, starting at 10:00 AM.
- **Resolution Due**: Wednesday, 4:00 PM.

---

### Scenario 3: Ticket Created on Saturday(Holiday) with Low Priority.
#### Ticket Created: Saturday, 3:00 PM  
- **SLA for First Response**: 8 hours (Low priority)  
- **SLA for Resolution**: 24 hours (Low priority)  
- **Holiday List**: All Saturdas & Sundays are holidays.  
- **Working Hours**: 10:00 AM to 6:00 PM (Monday to Friday)  
- **Status**: `Replied` (Resolution timer paused until customer response)

#### First Response Calculation:
- **First Response Time** is 8 hours.
- Created at 3:00 PM on Saturday.
- Saturday is a holiday, so no hours are counted on that day.
- The first 8 hours will count from **Monday**, starting at **10:00 AM**.
- The full 8 hours will be completed by **Monday at 6:00 PM**.
- **First Response Due**: Monday, 6:00 PM.

#### Resolution Calculation:
- **Resolution Time** is 24 hours.
- Since the first response is completed by **Monday at 6:00 PM**, the resolution timer will begin immediately after that.
- The full 24 hours will be counted from **Tuesday at 10:00 AM**, considering the holiday on Sunday.
- The full 24 hours will complete by **Wednesday at 6:00 PM**.
- **Resolution Due**: Wednesday, 6:00 PM.

---



### All Scenarios in tabular form:

| **Scenario** | **Ticket Created**    | **First Response Due** | **Resolution Due**   |
|--------------|-----------------------|------------------------|----------------------|
| **1**        | Tuesday, 5:00 PM      | Wednesday, 1:00 PM     | Wednesday, 5:00 PM   |
| **2**        | Friday, 4:00 PM       | Monday, 4:00 PM        | Wednesday, 4:00 PM   |
| **3**        | Saturday, 3:00 PM     | Monday, 6:00 PM        | Wednesday, 6:00 PM   |

---

<!-- page: helpdesk/helpdesk__setting-up.md -->
---
title: "Setting Up"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/setting-up"
updated: "2026-01-06"
---

If you have installed Helpdesk on a brand new site, you will need to set up your account. Visit your site that has Helpdesk installed, and you should see a setup wizard.

![Setup Wizard](/files/insights-setup-wizard.png)
*Setup Wizard*

To complete the setup you will need to enter basic information like your country, name, email, and password. Make sure to remember your email and password as this is going to be your [admin account](/miscellaneous/faq#admin-account).

Once you have gone through the setup wizard, you will be redirected to the Ticket List Page where you can see a List of pre-created ticket. You can click on the ticket to view the sample ticket. 

![](/files/Screenshot%202025-04-28%20at%202.01.41%20PM.png)
*Ticket List View*
