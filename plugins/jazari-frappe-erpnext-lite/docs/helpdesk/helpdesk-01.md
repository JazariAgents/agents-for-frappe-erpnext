<!-- Frappe documentation: helpdesk, part 1 of 4. Index: docs/INDEX.md -->

<!-- page: helpdesk/helpdesk__agent.md -->
---
title: "Agent"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/agent"
updated: "2026-01-06"
---

In Frappe Helpdesk, an agent is a user who is responsible for handling customer support tickets. Agents are the frontline personnel who interact directly with customers, diagnose issues, provide solutions, and ensure customer satisfaction. They play a vital role in the helpdesk system, contributing to the overall efficiency and effectiveness of the support process.



#### Key Features and Responsibilities of Agents

1. **Ticket Management**: Agents manage the lifecycle of support tickets from creation to resolution. This includes responding to customer inquiries, updating ticket status, and documenting the resolution process.
2. **Communication**: Agents communicate with customers through various channels such as email, chat. They provide timely updates, request additional information if needed, and keep the customer informed throughout the resolution process.
3. **Collaboration**: Agents work collaboratively with other team members and departments to resolve complex issues. They can share notes, escalate tickets, and seek assistance from specialists or higher-tier support teams.
4. **Knowledge Base Utilization**: Agents utilize the knowledge base to find solutions to common issues, ensuring quick and accurate responses. They can also contribute to the knowledge base by documenting new solutions and best practices.
5. **Performance Metrics**: Agents are often evaluated based on key performance indicators (KPIs) such as ticket response time, resolution time, customer satisfaction scores, and the number of tickets handled. These metrics help in assessing the effectiveness of agents and identifying areas for improvement.
6. **Customer Satisfaction**: Ensuring customer satisfaction is a primary goal for agents. This involves not only resolving issues but also providing a positive and empathetic customer experience.

#### Use Cases for Agents in Frappe Helpdesk

* **Technical Support**: Agents with technical expertise handle tickets related to software issues, hardware problems, and other technical queries.
* **Billing and Account Support**: Agents manage tickets related to billing inquiries, account issues, and payment problems, ensuring that customers' financial concerns are addressed promptly.
* **Product Support**: Agents provide assistance with product-related questions, feature usage, and troubleshooting.
* **General Inquiries**: Agents handle general customer inquiries, guiding customers to the appropriate resources or departments.

By effectively managing tickets and providing excellent customer service, agents in Frappe Helpdesk play a crucial role in maintaining customer satisfaction and loyalty. Their ability to resolve issues efficiently and communicate effectively directly impacts the overall success of the helpdesk system.


#### Adding Agents 
Pre-requisite: Email account must be setup, if it is not setup follow this [https://docs.frappe.io/helpdesk/settings](url)


Click on "Agents" on the sidebar and you will be navigated to this page.

![](/files/Screenshot%202025-04-21%20at%202.33.41%20AM.png)


1. Click on "Create" button in the center
   
![](/files/Screenshot%202025-04-21%20at%202.34.53%20AM.png)

2. A dialog will open, enter agent's email ID
3. Click on "Send Invites", if you get an error like "Outgoing Email Error", this means you have not setup your email account, add it and try again.

4. They will be sent an email link to add there password, once they setup there password, they can login into your Helpdesk system.
5. Agent is added to your helpdesk system.

<!-- page: helpdesk/helpdesk__assignment-rule.md -->
---
title: "Assignment Rule"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/assignment-rule"
updated: "2026-05-28"
---

Assignment Rules automate the process of assigning tickets to specific agents based on predefined conditions. This streamlines your workflow and ensures tickets are directed to the most qualified agents for faster resolution and improved customer experience.

**Creating an Assignment Rule**
-------------------------------

1. **Open settings modal:** Click on top left dropdown and click "Settings"


![settings dropdown](/files/Screenshot%202025-08-19%20122908.png)

2. **Open Assignment Rules tab:** Click on "Assignment Rules" in the sidebar and click on "Create new"


![](/files/Screenshot%202025-08-19%20123014.png)

3. **Define the Rule:** Fill in the following mandatory fields:



- **Name:** Give your rule a descriptive name for easy identification.
- **Description:** Describe in short what does the rule do
- **Assignment condition:** Define condition using the conditions builder for the assignment rule, complex nested conditions are also supported 
![](/files/Screenshot%202025-08-19%20125226.png)

- **Users:** Choose the user(s) to whom tickets meeting the condition will be assigned.

**Ticket Routing**
---------

Assignment Rules offer two rules for assigning tickets:

1. **Auto-rotate:** This method distributes tickets evenly among the selected users. Each user receives one assignment at a time, and the cycle repeats once all users have been assigned.
2. **Assign by workload:** This method assigns tickets to the user with the least workload, ensuring a fair distribution and preventing any single user from being overloaded.


**Additional Fields**
---------------------

**Unassignment condition:** Define condition using the conditions builder for the unassignment rule, complex nested conditions are also supported. This will be used to unassign a ticket based on the condition specified

**Assignment Schedule:** Select the days you want the assignment rule to be active

---

By effectively utilizing Assignment Rules, you can significantly improve the efficiency and organization of your ticket management process.

<!-- page: helpdesk/helpdesk__comment.md -->
---
title: "Comment"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/comment"
updated: "2026-05-28"
---

The comment feature allows internal communication and information sharing related to tickets. It facilitates collaboration among agents by providing a dedicated space to discuss, track progress, and share details.

![Screenshot 2024-07-15 at 12.46.14 PM](/files/Screenshot 2024-07-15 at 12.46.14 PM.png)  


**Key Features**
----------------

* **Internal Communication:** Engage in discussions with other agents regarding tickets.
* **Mentions:** Use the "@" symbol followed by a username to notify specific agents about important updates or require their input within a comment.
* **Information Storage:** Store relevant details about the ticket within the comments section for easy reference. This can include notes from conversations, action items, or crucial milestones.

**Add a Comment**
-----------------

1. Locate the "Comment" button at the bottom on the Ticket page.
2. Enter your comment in the designated text box.
3. To mention a user, type "@" followed by their username. A dropdown menu will appear with matching usernames for ease of selection.
4. Once you've crafted your comment and included any necessary mentions, click "Submit".

<!-- page: helpdesk/helpdesk__custom-actions.md -->
---
title: "Custom Actions"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/custom-actions"
updated: "2026-03-02"
---

Custom actions allow you to perform specific tasks directly from the Ticket page. These actions can be anything from integrating with external apps to updating ticket data or creating related documents...

## Creating Custom Actions

Custom actions are implemented using Form Scripts in Desk:

1. **Navigate to Desk:** Switch to Desk and navigate to HD Form Script.
2. **Select Doctype:** Choose the Doctype (e.g., HD Ticket) where you want to add the custom action. You'll be presented with a boilerplate code.
3. **Apply To:** Choose "Form".
4. **Define Your Action:** Here's how to define different types of actions:
  **Single Button:** This code creates a single button labelled "Open in Desk" that opens the current Ticket in a new browser tab.
     
  ![](/files/Normal%20Button%20Script.png)
  ```
  	```
  	const actions = [{
  	    "label": "Open in Desk",
  	    "onClick": () => {
  	        let URL = `https://frappehelpdesk.frappe.cloud/app/hd-ticket/${doc.name}`
  	        window.open(URL, '_blank')
  	    },
  	    "variant": 'solid' | 'subtle' | 'outline' | 'ghost',
  	    "theme" : 'gray' | 'blue' | 'green' | 'red'
  	}]
  	```
  	You can add variant and theme to your buttons.
  	Default variant is "solid".
  	Default color is "gray".
  	Both of these properties are optional.
  	You can also add your own tailwind classes here using the "class" key
  	`e.g: class: 'rounded-lg bg-surface-pink-1' `
  ```
     
  ![](/files/Normal%20Button.png)
   **Grouped Actions:** This code creates a group of buttons hidden under a three-dot menu labelled "Add." Clicking on either "Open Weekly Analysis or "Open Article Analysis" will trigger their respective onClick functions (defined elsewhere).
     
  ![](/files/Three%20dots%20script.png)
  ```
  	```
      const actions = [
        {
          group: 'Reports',
          hideLabel: true,
          items: [
            {
              label: 'Open Weekly Analysis',
              onClick: () => {},
            },
            {
              label: 'Open Articles Analytics',
              onClick: () => {},
            },
          ],
        },
        {
          group: 'Ticket',
          items: [
            {
              label: 'Create a new ticket',
              onClick: () => {},
            },
            // suggest some action other than open in fc
            {
              label: 'Open Customer Details',
              onClick: () => {},
            },
          ],
        },
      ]
  	```
  ```
     
  ![](/files/Drop%20down%20three%20dots.png)
   **Grouped Actions with label:** This code creates a group of buttons hidden under a dropdown button labelled "Reports". Clicking on either "Open Weekly Analysis or "Open Article Analysis" will trigger their respective onClick functions (defined elsewhere)
     
  ![](/files/Button%20Dropdown%20script.png)
  ```
  	```
      const actions = [{
            "buttonLabel": "Reports",
            "group": "Add",
            "hideLabel": true,
            "items": [
                {
                  label: 'Open Weekly Analysis',
                  onClick: () => {},
                },
                {
                  label: 'Open Articles Analytics',
                  onClick: () => {},
                },
            ]
        }]
  	```
  ```
     
  ![](/files/Dropdown%20button.png)
   **Combined Actions:** You can combine both single buttons and group actions into a single list and pass them as the "actions" property.
     
  ![](/files/Combined%20Script.png)
     
  ![](/files/Combined%20Script%20UI.png)

## Using Context and Actions

The `doc` parameter provides context about the current Ticket page. You can utilize this context along with various functionalities to create your custom actions:

- `doc`: Access Ticket field values (e.g., `doc.raised_by`, `doc.customer`).
- `$dialog`: Opens a confirmation dialog with actions. (you can pass title,message,html & actions as key while creating dialog)
- `updateField`: Updates a specific field value (e.g., `updateField('status', 'closed', callback)`).
- `router`: Navigate to a different page using Vue Router.
- `call`: Calls an API from the client side. You can add the server side end point in server script.
- `createToast`: Displays success or error messages.

Field Values in HD Form script doct

- `Enabled`: Enable script, if no other options are ticket, the script will be applied to the Agent's Ticket View
- `Apply to customer portal`: Script will be applied to Ticket View of Customer
- `Apply on new page`: Script will be applied on creation of New Ticket
  ![](/files/Screenshot%202025-03-29%20at%209.02.54%20PM.png)

Function Support on various pages:


| Functions    | Ticket Agent | Ticket Customer | New Ticket |
| ------------ | ------------ | --------------- | ---------- |
| call         | ✓            | ✓               | ✓          |
| updateField  | ✓            | ✓               | ✗          |
| router       | ✓            | ✓               | ✓          |
| $dialog      | ✓            | ✓               | ✓          |
| createToast  | ✓            | ✓               | ✓          |
| applyFilters | ✗            | ✗               | ✓          |


## Example: Custom Actions for Ticket Management

Here's an example showcasing various custom actions you can create to manage Deals:  

![](/files/Dialogs.gif)



```
function setupForm({
  doc,
  updateField,
  call,
  router,
  $dialog,
  createToast,
}) {
  const actions = [
    {
      group: "Actions",
      hideLabel: true,
      items: [
        {
          label: "Open FC Info",
          onClick: () => {
            // Call API to get custom information
            call("show_custom_info", {
              ticket: doc.name,
              // Include relevant fields for fetching data
            }).then((data) => {
              if (data.name) {
                $dialog({
                  title: data?.title,
                  message: data?.message,
                  html: data?.html, // this field can be in HTML format
                  actions: [
                    {
                      label: "Open in FC",
                      variant: "solid",
                      onClick(close) {
                        let URL = `http://helpdesk:8010/app/hd-ticket/${doc?.name}`;
                        window.open(URL, "_blank");
                      },
                    },
                    //   add more actions
                  ],
                });
              }
            });
          },
        },
        {
          label: "Close this ticket",
          onClick: () => {
            $dialog({
              title: "Close this ticket?",
              message: "Are you sure you want to mark this close this ticket?",
              actions: [
                {
                  label: "Close",
                  theme: "red",
                  variant: "solid",
                  onClick(close) {
                    updateField("status", "Closed", () => {
                      createToast({
                        title: "Ticket has been closed",
                        icon: "alert-circle",
                      });
                      close();
                    });
                  },
                },
                {
                  label: "Cancel",
                  variant: "outline",
                  onClick(close) {
                    close();
                  },
                },
              ],
            });
          },
        },
      ],
    },
  ];
  if (doc.status !== "Closed") {
    actions.push({
      label: "Close the ticket",
      onClick: () => {
        $dialog({
          title: `Close ticket: ${doc.name}`,
          message: "Are you sure you want to close this ticket?",
          actions: [
            {
              label: "Close",
              theme: "red",
              variant: "solid",
              onClick(close) {
                updateField("status", "Closed", () => {});
                close();
              },
            },
            {
              label: "Cancel",
              variant: "outline",
              onClick(close) {
                close();
              },
            },
          ],
        });
      },
    });
  }

  return {
    actions,
  };
}
```

<!-- page: helpdesk/helpdesk__custom-views.md -->
---
title: "Managing Tickets with ease (Views)"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/custom-views"
updated: "2026-03-19"
---

By default helpdesk provides you with 4 Standard Views. These views are visible in the dropdown selection at the top of the tickets list view. 

1. SLA Due

Tickets where the SLA is either failed or close to being failed, requiring immediate attention.  
2. My Feedback  
Feedback received on tickets handled by the logged in agent.  
3. Recently Assigned Tickets  
Tickets that have been recently assigned to the logged in agent and may need initial action.  
4. Pending Tickets  
Tickets which are awaiting the response of the logged in agent.

![](/files/imagecebdba.png)
*Standard views*







By default these are visible on the sidebar, if you want to hide these views from the sidebar, go to the dropdown in the ticket list view, click on triple dots and then "Hide from sidebar". 

> Note: Standard views can't be deleted. 



### Custom Views

It becomes difficult for agents and customers to create different filters and constantly change them depending on their requirements. Custom views makes it easier for both types of users to segregate and maintain combinations of sort, filters, and columns. 

#### Creating a view

![](/files/Creating%20a%20view.gif)

There are 4 types of views:

- **Default view**: The default view set by the user.
- **Public view**: visible to all the agents. (Only Agent managers are allowed to make actions on public views) such as users with the role of "Agent Manager" can create/edit/delete public views or even make it private.
- **Saved views**: Personal Views for easy filters, sort & column settings.
- **Private views**: These are shown on the sidebar for easy access.

![](/files/Types%20of%20views.png)

#### Actions available on each view

![](/files/h8PJhxI.png)

Making views is also available on the customer portal side, all actions are possible except making public views.

#### Example of "My Open Tickets" View for Agents

Agents often need quick access to their open tickets. **Public Views** are perfect for this use case.

To create a view for "My Open Tickets", apply the following filters:

![My Open Tickets Filter](/files/Screenshot%202025-04-23%20at%206.01.36%20PM.png)

- Use the `@me` filter in the **assign_to** field.  
- This automatically resolves to the current logged-in user.

Once the view is created, mark it as **Public**. Now, every agent will be able to use this shared view to easily access their own open tickets, without having to set up private views individually.

Similarly you can build different views like "My Replied Tickets" & make them public.

### Bulk Actions

- **Exporting Tickets**
  1. Use the checkboxes beside each ticket to select one or multiple rows.
  2. Once you selected the rows, a popover appears at the bottom.
  3. Click the **three dots** (•••) to:
    - Export the selected tickets
    - Or export **all tickets** in the list
- **Delete Tickets**
  1. Agents with the role of "Agent Manager" can delete tickets.
  2. Use the checkboxes beside each ticket to select one or multiple rows.
  3. Once you selected the rows, a popover appears at the bottom.
  4. Click the **three dots** (•••) => Delete => a confirmation dialog appears => Click Confirm to delete your tickets

<!-- page: helpdesk/helpdesk__customer-portal.md -->
---
title: "Customer Portal"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/customer-portal"
updated: "2026-01-06"
---

The **Customer Portal** allows your users to sign in to the Helpdesk and manage their support interactions.

When a [contact](https://docs.frappe.io/helpdesk/customers-contacts) logs in, they are automatically redirected to the Customer Portal.

Once you’ve [invited](https://docs.frappe.io/helpdesk/customers-contacts#inviting-as-user) a contact, they can access the portal to:

- Submit new tickets
- Track the status of existing tickets
- Access the Knowledge Base with relevant search functionality

> 🔍 The portal provides a self-service experience for your customers, reducing support load and improving user satisfaction.


### 📝 Submitting New Tickets

To create a new ticket:

1. Click on the **Tickets** page from the sidebar.
2. Click the **Create** button.
3. Fill in the **Subject** and other necessary details.

![](/files/CP%20Suggestion%20&%20Ticket%20Creation.gif)

> 💡 As you type the subject, relevant articles will appear based on your query.  
> This helps customers resolve issues on their own before submitting a ticket.

To add more fields in the ticket form on the Customer Portal, check out [this guide](https://docs.frappe.io/helpdesk/field-dependency).

---

### 📊 Tracking Ticket Status

On the **Tickets** list view, users can manage and track the status of their submitted tickets.

#### Custom Views

- You can create personalized views to filter tickets based on status, priority, or other fields.
- Learn [how](https://docs.frappe.io/helpdesk/custom-views) to create & configure custom views.

#### Exporting Tickets

1. Use the checkboxes beside each ticket to select one or multiple rows.
2. Once you selected the roww, a popover appears at the bottom.
3. Click the **three dots** (•••) to:
   - Export the selected tickets
   - Or export **all tickets** in the list
![](/files/Export%20Customer%20Portal.gif)
---


### 📚 Knowledge Base

The Customer Portal includes a built-in **Knowledge Base** to help users find answers faster.

- As users type their questions, relevant articles automatically appear.
![](/files/Screenshot%202025-04-23%20at%203.32.27%20PM.png)

- Users can browse through the Knowledge Base to find the information they need without having to raise a ticket.
![](/files/KB%20Customer.gif)

> 🧠 A well-maintained Knowledge Base can significantly reduce support load by enabling users to self-serve.


> You can setup Knowledge Base as the landing page for your customers/contacts, to do so
    go to [HD Settings](https://docs.frappe.io/helpdesk/settings) => Find "Prefer Knowledge Base" => click & save.

### 🚀 You’re Ready to Get Started!

You’ve now learned the basics to start using **Frappe Helpdesk** — from managing customers and contacts to submitting and tracking tickets via the Customer Portal.

To explore more advanced features, visit our [full documentation](https://docs.frappe.io/helpdesk).

We recommend checking out the **Customisations** section to tailor Frappe Helpdesk according to your specific needs and workflows.

Happy supporting! 💬

<!-- page: helpdesk/helpdesk__customer.md -->
---
title: "Customer"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/customer"
updated: "2026-06-25"
---

A **Customer** refers to an organization or a company. It is used to group [Contacts](https://docs.frappe.io/helpdesk/contact) under a common entity, so a team from the same company can be managed and reported on together.

### Creating a Customer

1. Navigate to the **Customer** page using the sidebar.
2. Click on "Create", present in the top right corner, and fill in the details. Optionally, you can add details of the primary contact for the customer. If added, the contact will be created automatically and will be invited to the system.
  ![](/files/image421694.webp)
3. Click **Create** to save the customer.

## Customer View

![](/files/imagebfefed.webp)

Open a customer from the list to see its full details. The top of the page shows:

### Top Section

- **Logo and name** of the customer.
- **Domain**, **Email**, **Phone**, and **Country** — each shown when set. The email and phone are taken from the customer's primary contact.



### Actions

Use the **Edit** button and the **⋯ (more)** menu at the top right to manage the customer.

- **Edit details** — Opens the Edit Customer dialog where you can change the logo, name, customer type (Company, Individual, Partnership), country, and domain. An **Unsaved** badge appears while you have pending changes; click **Save** to apply them.
- **Delete** — Removes the customer. A confirmation dialog appears; the reference to this customer is removed from all related tickets. If the customer has linked tickets, you can also choose to **delete those tickets**.



### Analytics

On desktop, a row of summary cards is shown above the tabs, giving a quick health check for this customer:

- **Avg. Feedback Received** — Average star rating across the customer's tickets, with the total number of reviews.
- **Failed SLAs** — Number of tickets that breached their SLA.
- **Avg. First Response Time** — Trend of how quickly the first response went out.
- **Avg. Resolution Time** — Trend of how long tickets took to resolve.



### Tickets

The **Tickets** tab lists all tickets raised under this customer.

- **Search** by ticket ID or subject.
- **Filter** by Status, Priority, and Contact.
- The table shows ID, Subject, Status, Priority, First Response, Resolution, and Assigned To. Click any row to open the ticket in a new tab.



### Managing Contacts under a Customer

![](/files/image2ede6e.webp)



The **Contacts** tab lists everyone grouped under the customer as cards, and is where you manage membership.

- **Invite a contact** — Click **Invite** to add people by email. You can add existing contacts or brand-new ones. For each, choose a **Role**:
  - **HD Customer** — Can raise tickets on behalf of the organization and manage the tickets they raised.
  - **HD Customer Manager** — Can view all tickets raised by the organization and assign other members as managers.  
  If a contact with that email already exists, it is linked to the customer; otherwise a new contact is created and invited as a user. Pending invitations are listed and can be revoked.
- **Set as Primary** — From a contact card's menu, mark a contact as the **primary** point of contact (shown with a star). The primary contact is always a manager.
- **Assign / change role** — Promote a contact to **Manager** or revoke manager access from the card menu. Managers can see all of the organization's tickets; regular contacts only see their own. A customer can have multiple managers.
- **Remove a contact** — Removes the contact from this customer only. The contact itself is not deleted and stays available for other customers.
- To view the invited contacts, click the Invite button to see the pending Invites.  
  ![](/files/image1fef71.webp)



**Deleting a Customer** - When you delete a customer, you can also choose to delete all tickets linked to that customer. If you do not delete the tickets, they will remain in the system but will no longer be associated with any customer; i.e., there will be no reference to the customer in those tickets.

## Notes

- Linking a Contact to a Customer is optional.
- A Contact can be part of **multiple Customers** at the same time.
- Contacts under the same Customer can collaborate and see each other's support tickets (managers see all, regular contacts see their own).
- While raising a ticket, if the person  raising the ticket via the portal is part of multiple customers, then adding a "Customer" becomes mandatory.

<!-- page: helpdesk/helpdesk__customers-contacts.md -->
---
title: "Customers & Contacts"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/customers-contacts"
updated: "2026-07-23"
---

## Contact

A **Contact** is an individual user who may be linked to a Customer (organization), we will talk about Customers in the next section. Contacts are the primary point of communication for support tickets, and they can also be invited as users to access the system.

### Creating a New Contact

1. Navigate to the **Contact** page using the sidebar.
2. Click on **"Create New Contact"**, present in the top right corner.
3. Fill in the following fields:
  - **Email ID** (required)
  - **First Name** (required)
  - **Last Name**
  - **Phone**
  - **Customer** *(Optional)* — Select a customer this contact belongs to.
  - **Invite as User** *(Optional)* — If checked, the contact will be invited to the system as a user.

![](/files/image5d3361.webp)

4. Click **Create** to save the contact. On saving the contact, if the **Invite as User** option was checked, an email will be sent to the contact's email address with a link to set their password and access the system.

To know more about Contact, click [here.](https://docs.frappe.io/helpdesk/contact)



---

## Customer

A **Customer** refers to an organization or a company. It is used to group contacts under a common entity.

### Adding a New Customer

1. Navigate to the **Customer** page using the sidebar.
2. Click on "Create", present in the top right corner, and fill in the details. Optionally, you can add details of the primary contact for the customer. If added, the contact will be created automatically and will be invited to the system.
  ![](/files/image421694.webp)
3. Click **Create** to save the customer.

### Managing Contacts under a Customer

![](/files/image2ede6e.webp)



The **Contacts** tab lists everyone grouped under the customer as cards, and is where you manage membership.

- **Invite a contact** — Click **Invite** to add people by email. You can add existing contacts or brand-new ones. For each, choose a **Role**:
  - **HD Customer** — Can raise tickets on behalf of the organization and manage the tickets they raised.
  - **HD Customer Manager** — Can view all tickets raised by the organization and assign other members as managers.  
  If a contact with that email already exists, it is linked to the customer; otherwise a new contact is created and invited as a user. Pending invitations are listed and can be revoked.
- **Set as Primary** — From a contact card's menu, mark a contact as the **primary** point of contact (shown with a star). The primary contact is always a manager.
- **Assign / change role** — Promote a contact to **Manager** or revoke manager access from the card menu. Managers can see all of the organization's tickets; regular contacts only see their own. A customer can have multiple managers.
- **Remove a contact** — Removes the contact from this customer only. The contact itself is not deleted and stays available for other customers.
- To view the invited contacts, click the Invite button to see the pending Invites.  
  ![](/files/image1fef71.webp)

## Notes

- Linking a Contact to a Customer is optional.
- A Contact can be part of **multiple Customers** at the same time.
- Contacts under the same Customer can collaborate and see each other's support tickets (managers see all, regular contacts see their own).



---



# Update on Permissions⚠️

> ## Breaking change: customer ticket permissions (v1.28.0)
>
> Starting with v1.28.0, ticket visibility for customer portal users is controlled explicitly from the Customer page. It is no longer granted implicitly.  
>
>
>
> ### What changed
>
> **Before v1.28.0**, any user who raised a ticket implicitly got portal access, and contacts linked to a customer could see all tickets of that customer. There was no per-contact control.
>
> **From v1.28.0 onwards**, by default a contact can only see the tickets they raised themselves. To let a contact see all tickets of their customer (organization), mark that contact as a **customer manager** on the Customer page. Portal access itself is now gated on two new roles, **HD Customer** and **HD Customer Manager**, which Helpdesk manages for you as you add contacts and mark managers.
>
>
>
> ### Who is affected
>
> - **Existing sites upgrading to v1.28.0**: yes. Read the sections below.
> - **New sites**: nothing to do. This is the default behavior.
> - **Agents**: not affected. This change only concerns customer portal users.
>
>
>
>
>
> ### After upgrading
>
> Sites hosted on Frappe Cloud are migrated automatically. On self-hosted sites, run `bench migrate` after upgrading.
>
> The migration does the following:
>
> - Grants the **HD Customer** role to every non-agent user who has raised a ticket, so they keep their portal access.
> - Moves all existing contact-to-customer links onto the Customer page. You will see each customer's contacts listed there.
> - Existing contacts are added as regular members, **not** as customer managers. This means that after the upgrade, contacts only see their own tickets until you decide otherwise (see "Restoring the old behavior" below).
>
> **Note:** a contact who never raised a ticket does not receive the HD Customer role from the migration. Such users will regain portal access when you add them as a contact on the Customer page or give them HD Customer role from the backend.
>
>
>
> ### Managing ticket visibility
>
> All of this is done from the **Customer page** in the agent portal:
>
> - **Add or remove contacts** on a customer to control who belongs to that organization. New contacts see only their own tickets by default.
> - **Mark a contact as a customer manager** to let them see every ticket of that customer. Helpdesk assigns the HD Customer Manager role automatically.
>
>
>
> ### Restoring the old behavior
>
> If you want all contacts to see each other's tickets again, like before the upgrade, use the **Customer portal update** banner:
>
> - The banner appears in the **sidebar of the agent portal** and is visible only to **Agent Managers** and **System Managers**. Customer portal users never see it.  
>   ![](/files/image75c4eb.webp)
> - Clicking **Learn more** opens a dialog explaining the change. To restore the old behavior, check **Make all existing contacts customer managers** and click **Confirm**. Every existing contact is marked as a customer manager, so all contacts of a customer can see that customer's tickets again. This runs in the background and may take a few minutes on large sites.
> - To keep the new restricted behavior, leave the checkbox unchecked and click **Confirm**.  
>   ![](/files/image43ff5f.webp)
>
>
>
> Two things to keep in mind:
>
> - Restoring access is a **one-time action, not a setting**. It promotes the contacts that exist at that moment. Contacts added later will still start with access to only their own tickets, and you will need to mark them as customer managers individually.
> - Confirming either way dismisses the notice permanently for all managers. It does not come back.
>
>
>
> ### Default Role
>
> Helpdesk sets the portal's **Default Role** to **HD Customer** automatically — this is the role new self-signup contacts receive, and it's what grants them access to the customer portal at `/helpdesk`. On new sites this is already done for you.
>
> If you're on an existing site and had a different default role configured, the upgrade leaves your value untouched. Check **Portal Settings** → **Default Role**; if it isn't **HD Customer**, update it so newly signed-up contacts get portal access and the right permissions.
>
>
>
> ### Ticket Template (Customer field)
>
> "Customer" field will be rendered in Customer Portal only if the contact raising the ticket is part of multiple customers. If it is present in HD Ticket Template => Default, then the field will be only visible if an agent is raising a ticket.  
>
> ### Domain Linking
>
> Domain based auto contact linking has been removed.
>
>
>
> ### Coming soon
>
> Customer managers will be able to invite other people into their organization (customer) themselves, without needing an agent to add them.

<!-- page: helpdesk/helpdesk__customization__email-preferences.md -->
---
title: "Email Preferences"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/customization/email-preferences"
updated: "2026-05-08"
---

The **Email and Signatures** section in your profile settings allows you to control how your outgoing emails are sent and displayed. Any changes you make here will automatically apply when you reply to tickets via email in Frappe Helpdesk.

To access and update these settings:

1. Click on the dropdown located in the top-left corner of the sidebar and select the **Settings** option.
2. Once the Settings modal is opened, inside in the Profile section find **Emails & Signature** option.
3. Click the **Configure** button next to it.

From this section, you can manage all email-related preferences in one place.

![](/files/imageada66c.png)

## Email Signature

The Email Signature feature lets agents add a personalised signature to their outgoing email replies. Once configured in their profile, the signature is automatically appended to every new email reply.

## Setting Up Your Signature

Each agent can configure their own signature from their Profile settings.

Once you're inside the **Email & Signature** section, you can use the rich text editor to create your signature. This editor allows you to include formatted text, links, and images, helping you design a more professional and visually appealing signature.

After making your changes, click **Save** to apply them.

> Your signature is personal to your account. Each agent manages their own signature independently.

In the below demonstration you can see how Email Signature works in Frappe Helpdesk.

![](/files/Screen Recording 2026-05-03 at 8.18.05 PM.mov)









You can clear your signature at any time by simply deleting the content from the signature editor and saving the changes.

Once set up, your signature is automatically added to every outgoing reply, keeping your communication professional and consistent without any extra effort on your part.

## From Emails

If your account has multiple [outgoing emails](https://docs.frappe.io/erpnext/email-account#34-outgoing-email-accounts) configured, you can now select which one to use when replying to tickets directly from the email editor in Frappe Helpdesk.    

A "From" dropdown menu appears in the email editor toolbar. Click it to switch between your available sender addresses. The chosen email address will be remembered for your session, so you won't need to change it for every reply.

In the below demonstration you can see how you can switch between your outgoing emails while reply to a ticket

![](/files/Screen Recording 2026-05-03 at 8.32.08 PM.mov)





This feature can be useful for agents who manage multiple inboxes or support different products from a single Helpdesk account.

<!-- page: helpdesk/helpdesk__email-communication.md -->
---
title: "Email Communication"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/email-communication"
updated: "2026-05-28"
---

This feature allows you to seamlessly exchange emails with your customers directly from the Ticket page within the system. All email interactions are conveniently stored and accessible, promoting efficient communication and record-keeping.

**Sending Emails**
------------------

1. **Locate the Reply Button:** On the Ticket page, find the "Reply" button, typically situated at the bottom of the page.
2. **Compose Your Email:** A new email composition window will appear. Here, you can:

![Screenshot 2024-07-05 at 11.04.39 AM](/files/Screenshot 2024-07-05 at 11.04.39 AM.png)  



	* **Subject:** Craft a clear and concise subject line that summarizes the email's purpose.
	* **To:** Enter the recipient's email address in the "To" field.
	* **Cc & Bcc (Optional):** Utilize the "Cc" (Carbon Copy) field to include additional recipients who should be informed but not required to respond. The "Bcc" (Blind Carbon Copy) field allows you to send a copy to recipients without revealing their addresses to other recipients.
	* **Message Body:** Compose the main content of your email. You can leverage formatting options for better readability and include attachments if necessary.
3. **Leverage Canned Responses (Optional):** Streamline communication by incorporating pre-defined Canned Responses. Click on the "Canned Responses" icon and select the desired message from the available list. This pre-populates the message body, saving you time and ensuring consistency.

![Screenshot 2024-07-05 at 11.06.47 AM](/files/Screenshot 2024-07-05 at 11.06.47 AM.png)
4. **Hit Submit:** Once you've crafted your email, click the "Submit" button to send it to the recipient(s).

**Viewing Email Communication**
-------------------------------

All email interactions related to a specific Ticket are consolidated within the system.

![Screenshot 2024-07-05 at 10.58.40 AM](/files/Screenshot 2024-07-05 at 10.58.40 AM.png)  


**Email Account Setup**
-----------------------

You can sync your email account with Frappe Helpdesk to send and receive emails from Frappe Helpdesk.

You can manage multiple incoming and outgoing Email Accounts in Frappe Helpdesk. There has to be at least one default outgoing account and one default incoming account. If you are on the Frappe Helpdesk cloud, the default outgoing email is set by us.

To access Email Accounts, go to Email Account Master from the desk.

### **1. Prerequisites**

Before creating an Email Account, you need an Email Domain. However, you can skip creating an Email Domain if you're using one of the services listed [here](https://docs.erpnext.com/docs/user/manual/en/email-inbox#2-create-an-email-domain).


> **For detailed Email Account setup you can check ERPNext documentation** [**here**](https://docs.erpnext.com/docs/user/manual/en/email-account)
> 
> 

### **2. How to create an Email Account**

1. Go to the Email Account list, and click on New.
2. Enter the email address with the domain. Domains need to be created to create an email account. You don't need to create a domain if you're syncing an email from certain providers as listed [here](https://docs.erpnext.com/docs/user/manual/en/email-inbox#2-create-an-email-domain).
3. Enter the email account password.
4. Save. If the credentials are correct, the email account will be synced.


> **For some services like Gmail, you may need to enable 2FA and use** [**App Passwords**](https://myaccount.google.com/u/0/apppasswords)**.**
> 
> 

### **3. Additional options when creating an Email Account**

1. **Use Different Email Login ID**: To use an alternative email login and password to access this account. For example, if you have [notifications@example.com](mailto:notifications@example.com) and you want users to access this email with an alternate email ID, they should tick this checkbox. The recipients will see [notifications@example.com](mailto:notifications@example.com) as the sender.
2. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox. When the other user logs in, they'll be prompted to enter the password.
3. **Use ASCII encoding for the password**: Ticking this will use ASCII encoding for the password.

<!-- page: helpdesk/helpdesk__email-notifications.md -->
---
title: "Email Notifications"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/email-notifications"
updated: "2026-05-08"
---

Some emails are sent by Helpdesk based on the activities carried out by the users. Currently, there are 4 kinds of emails:

- Share Feedback
- Acknowledgement
- Reply From Contact
- Reply From Agent

To customize the content and the related options associated with each kind of email, you can use the 'Email Notifications' tab of the settings view.

![email notification list](/files/email-notification-listb47594.png)

## Share Feedback

This email is sent to the user who has raised the ticket after the ticket is closed or resolved. The purpose of the email is to get feedback on the support experience. 

This **only works** for **tickets** raised via **Email**, as we already have provision to get feedback for the tickets raised via customer portal.

If **feedback** already **exists** for the ticket, the **email** will **not** be **sent**.

The available customizations are highlighted in the image below.

![share feedback customizations](/files/share-feedbackc4e5ff.png)

### Available variables (share feedback)

The content field supports Jinja templates. The dynamic variables that can be used with the template are listed below:

- `url`: `str`  
The url of the feedback form
- `doc`: `HDTicket`  
The support ticket document. All fields associated with the `HDTicket` [doctype](https://docs.frappe.io/framework/user/en/basics/doctypes) are available.

## Acknowledgement

This email is sent to the user right after creating an email ticket. The purpose of the email is to let the user know that a support ticket was created because of the sent email.

The available customizations are highlighted in the image below.

![acknowledgement customizations](/files/acknowledgement.png)

### Available variables (acknowledgement)

The content field supports Jinja templates. The dynamic variables that can be used with the template are listed below:

- `doc`: `HDTicket`  
The support ticket document. All fields associated with the `HDTicket` [doctype](https://docs.frappe.io/framework/user/en/basics/doctypes) are available.

## Reply From Contact

This email is sent to all of the assigned agents after a reply from one of the contacts. The purpose of this email is to let all of the assigned agents know that a contact has replied.

The available customizations are highlighted in the image below.

![reply from contact customizations](/files/reply-from-contact.png)

> The email content is used only for tickets raised via Portal.

### Available variables (reply from contact)

The content field supports Jinja templates. The dynamic variables that can be used with the template are listed below:

- `message`: `str`  
The content of the email reply.
- `ticket_url`: `str`  
The url of the support ticket.
- `doc`: `HDTicket`  
The support ticket document. All fields associated with the `HDTicket` [doctype](https://docs.frappe.io/framework/user/en/basics/doctypes) are available.

## Reply From Agent

This email is sent to all of the recipients associated with an agent reply. The purpose of this email is to let the recipients know that an agent has sent a message.

The available customizations are highlighted in the image below.

![reply from agent customizations](/files/reply-from-agent.png)

> The email content is used only for tickets raised via Portal.

### Available variables (reply from agent)

The content field supports Jinja templates. The dynamic variables that can be used with the template are listed below:

- `message`: `str`  
The content of the reply.
- `ticket_url`: `str`  
The url of the ticket on Customer portal.
- `doc`: `HDTicket`  
The support ticket document. All fields associated with the `HDTicket` [doctype](https://docs.frappe.io/framework/user/en/basics/doctypes) are available.
