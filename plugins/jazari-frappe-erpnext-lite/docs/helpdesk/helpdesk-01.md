<!-- Frappe documentation: helpdesk, part 1 of 1. Index: docs/INDEX.md -->

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

<!-- page: helpdesk/helpdesk__exotel.md -->
---
title: "Exotel"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/exotel"
updated: "2026-05-21"
---

Exotel is a cloud telephony platform that enables businesses to manage voice calls, SMS, and communication workflows without traditional phone hardware. The integration with Frappe Helpdesk combines these communication capabilities with customer relationship management to provide a unified system for handling customer interactions.



Exotel setup
------------

To configure Exotel for use within the Helpdesk, follow these steps:

1. **Exotel Subscription:** Obtain an active Exotel subscription (refer to Exotel's documentation for details).
2. **Exotel Credentials:** From your Exotel account, retrieve your Account SID, Subdomain, API Key, API Token and Exotel Mobile Number (Exophones).
    ![](/files/Screenshot%202025-01-20%20at%206.51.13%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%206.56.49%E2%80%AFPM.png)
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
    ![](/files/Screenshot%202025-08-19%20122908.png)
4. **Telephony Settings:** Navigate to Telephony Settings and enable Exotel. Add your Account SID, Subdomain, API Key, API Token, Webhook verify token (it can be anything it will be used later in Exotel incoming call flow configuration), exotel number and personal number also. You can also enable call recording at this point.
![](/files/exotel-telephony-settings.png)



Exotel incoming call flow configuration
------------------------

> By simply adding or removing this incoming call flow you can enable or disable incoming calls.

For your Helpdesk's API to connect with Exotel, perform the following configurations within Exotel:

1. Login to your Exotel account and go to App Bazar.
2. Create a new "App" for a new flow.
    ![](/files/Screenshot%202025-01-20%20at%207.02.50%E2%80%AFPM0a6a6d.png)
3. Setup the flow as you wish it to be.
    
    * [Dial Whom](https://support.exotel.com/support/solutions/articles/3000088074-working-with-connect-applet-dial-whom-)
    * [Passthru](https://support.exotel.com/support/solutions/articles/48283-working-with-passthru-applet)
    * Check the documentation to learn about all the applets in flow builder - [Link](https://developer.exotel.com/applet)
4. Set "Dial Whom" as user group. In user group there can be multiple agents. Incoming call will be redirected to agents in this group in the order they are added.
    ![](/files/Screenshot%202025-01-20%20at%207.19.44%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.37.38%E2%80%AFPM.png)
5. You can also set how you want to distribute calls.
    ![](/files/Screenshot%202025-01-20%20at%207.44.03%E2%80%AFPM.png)
6. In your connect API under "Create popup...", copy and paste URL (Callback API) mentioned below. Here use webhook verify token which was mentioned in **Exotel Setup (point 4)**.


    ```
    https://<yoursitename>/api/method/telephony.exotel.handler.handle_request?key=<webhook-verify-token>
    ```
    
    ![](/files/Screenshot%202025-01-20%20at%207.08.08%E2%80%AFPM.png)
7. After that add a "Passthru applet" under "After Call Conversation ends" and paste the same URL.
    
    ![](/files/Screenshot%202025-01-20%20at%207.20.05%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.20.46%E2%80%AFPM.png)
    > Note: Make sure to check "Make Passthru Async".

8. Similary, add another "Passthru applet" under "If nobody answers..." section and paste the same URL.
    ![](/files/Screenshot%202025-01-20%20at%207.20.14%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.24.51%E2%80%AFPM.png)
    > Note: Make sure to check "Make Passthru Async".

9. Save the flow.
10. Now assign this newly created "App" to your ExoPhone from which you receive your business calls.
    ![](/files/Screenshot%202025-01-20%20at%207.26.56%E2%80%AFPM.png)


Make call
-----------

* **Ticket page:** A call button is available in the right section above ticket details. Use this button to initiate a call, but ensure the **Mobile No** field in the **Person** section includes the country code.
    ![](/files/ticket-view-call.png)

> Make sure to complete your KYC on Exotel before making calls [docs](https://support.exotel.com/support/solutions/articles/110606-trial-accounts-how-do-i-test-outbound-calling-)

Call pop-up
-----------

Upon making or receiving a call, a pop-up window appears displaying:

* Caller name
* Mobile number
* Call status
* Call duration
* Action buttons (Close or Minimize)


![](/files/Diler.png)


This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

![](/files/diler-minimized.png)

<!-- page: helpdesk/helpdesk__faq.md -->
---
title: "Custom time for pulling emails"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/faq"
updated: "2026-01-06"
---

By default Helpdesk pulls Emails every 10 minutes, if you want to configure that, you can do so by writing a small server script.

Go to desk => Server Script => Add Server Script

Use this configuration

![imageb182fe](/files/imageb182fe.png)

In the script paste this code:
`frappe.call("frappe.email.doctype.email_account.email_account.pull_emails",email_account="Sales")`
Replace "Sales" with the name of your email account.

Time configuration:

`All`: Pulls emails every 4 minutes
`Every n minute`: */n * * * * 
example for pulling emails every 2 minutes `*/2 * * * *`


# Change Helpdesk Email Pull Frequency

By default, Helpdesk pulls emails every **10 minutes**.  
To change this:

### 1. Create a Server Script
**Desk → Server Script → New**


### 2. Add Script
```python
frappe.call(
    "frappe.email.doctype.email_account.email_account.pull_emails",
    email_account="Sales"
)
> Replace "Sales" with your Email Account name.

```

### 3. Config

- Script Type: Scheduler Event
- Event frequency
- All: Pulls every 4 minutes
- CRON: */n * * * * -> To pull emails every n minutes
examples:

| Desired Frequency    | CRON Expression |
| -------------------- | --------------- |
| Every **2 minutes**  | `*/2 * * * *`   |
| Every **5 minutes**  | `*/5 * * * *`   |
| Every **15 minutes** | `*/15 * * * *`  |

<!-- page: helpdesk/helpdesk__faq__setting-up-outlook-for-frappe.md -->
---
title: "Setting up Outlook for Frappe Helpdesk"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/faq/setting-up-outlook-for-frappe"
updated: "2026-06-16"
---

You can connect a Microsoft 365 / Outlook mailbox to Frappe using OAuth instead of a password. OAuth is the recommended method because Microsoft is retiring basic (password) authentication for Exchange Online, and it lets Frappe send and receive mail without ever storing your mailbox password. Setup happens in two places: you register an app in **Microsoft Entra ID** (Azure), then point a **Connected App** and **Email Account** in Frappe at it.

## Before you begin

- Your Frappe site must be served over **HTTPS** (a local `localhost` dev site is fine).
- You need a Microsoft 365 account with **admin access to Azure / Microsoft Entra ID**.
- You need administrator access to your Frappe site to create a Connected App.

## Part 1: Register an app in Microsoft Entra ID

### Step 1: Create the app registration

1. Sign in to the [Azure Portal](https://portal.azure.com) and open **Microsoft Entra ID → App registrations**.
  ![](/files/imageff427d.png)
2. Click **New registration**.
  ![](/files/image56b32e.png)
  *New app registration button*
3. Give it a name (for example, `Frappe Email App`), leave the supported account type as default, and click **Register**. You will add the redirect URI later, once Frappe generates it.
  ![](/files/imagefd693d.png)
4. Once done successfully click on the register button below the form.

### Step 2: Add API permissions

1. Open your new app and go to **API permissions → Add a permission**
  ![](/files/imagea4cec0.png)
  *Guide to API Permissions*
  ![](/files/imaged7d057.png)
  *Add Permission*
2. Add the following Permissions under select Microsoft Graph option and inside go to  **Microsoft Graph → Delegated permissions**.
  ![](/files/image476ca7.png)
3. Click **Grant admin consent for**   and confirm. Each permission should show a green check under **Status**.
  ![](/files/image3483b7.png)
  *Click Grant admin consent*
  ![](/files/image6f40bf.png)
  *Updated status message*

### Step 3: Create a client secret

1. Go to **Certificates & secrets → New client secret** or in **Overview** click **Add a secret**.
  ![](/files/image3454e8.png)
  ![](/files/imagee26167.png)
2. Add a description, choose an expiry, and click **Add**.
  ![](/files/image7b6a71.png)
3. Copy the secret **Value** immediately and store it safely.
  ![](/files/image0ec9c5.png)

> **Note:** Copy the **Value**, not the **Secret ID**. The value is shown only once and cannot be retrieved again after you leave the page.

### Step 4: Collect your IDs and endpoint

From the app's **Overview** page, copy:

- **Application (client) ID**
- **Directory (tenant) ID**
- **OpenID Connect Metatdata Document ID** (Under endpoints)

![](/files/acb494e027c6e635843dee5bd28bff95f89eb228.png)

Your OpenID configuration URL follows this format — keep it for the next part:

```text
https://login.microsoftonline.com/your_tenant_id/v2.0/.well-known/openid-configuration
```

## Part 2: Create a Connected App in Frappe

1. In Frappe, go to **Connected App** and click **New** (`/app/connected-app/new`).
  ![](/files/image150cfa.png)
2. Paste your OpenID configuration URL into the **OpenID Configuration** field, then click **Get OpenID Configuration**. Frappe auto-fills the authorization, token, and revocation endpoints.
  ![](/files/imagee2cc0c.png)
  On clicking **Get OpenID Configuration**, the field values will be filled automatically. Add the Provider name as Outlook.
  ![](/files/imagecde89d.png)
3. Enter the **Client ID** and the **client secret Value** from Part 1 which you have stored from the overview section.
  ![](/files/imagef6c1d2.png)
4. Add the required **Scopes**:
  ![](/files/image227dc0.png)

```
https://outlook.office365.com/.default
```

```
offline_access
```

5. **Save** the Connected App.

> **Note:** The `.default` scope tells Microsoft to grant every permission you consented to in Step 2, so you don't have to list each one again here.

After saving, Frappe generates a **Redirect URI** on the Connected App. It looks like this:

![](/files/image0d15cf.png)

```text
https://your_site.com/api/method/frappe.integrations.doctype.connected_app.connected_app.callback
```

Copy that value, go back to your Azure app, open **Authentication → Add a platform → Web**, paste it as a redirect URI, and **Save**.



![](/files/imageee4504.png)

![](/files/image08eb8c.png)
*add your redirect URI and then configure*

Lastly click on the Connect to Provider button to grant permissions for frappe to access resources from your outlook based on the scope defined.

![](/files/image418979.png)



## Part 3: Connect your Email Account

Log in to Frappe as the **actual mailbox user** (not Administrator) before authorizing — the connection is granted for whoever is signed in.

1. Go to **Email Account** and create a new one (or open an existing account).
2. Enter the **Email Address** for the mailbox.
3. Set the incoming and outgoing servers:
  ```text
    Incoming (IMAP):  outlook.office365.com   port 993, SSL
    Outgoing (SMTP):  smtp.office365.com      port 587, TLS
  ```
4. Enable **Use OAuth**, then link the **Connected App** you created in Part 2.
5. **Save**, then click **Authorize API Access**. Microsoft will ask you to sign in and approve the request. Once approved, you're returned to Frappe and the account is connected.
6. Mark the account as **Default Incoming** and/or **Default Outgoing** as needed, Use OAuth option for authentication and then click **Authorize API Access**.

![](/files/image988c3d.png)

If everything is correctly done you will be taken to the outlook page where you select the account you want to gain access to. On approval you have then successfully connected your email account to Frappe.

## Troubleshooting

- **Outgoing mail fails:** Even with OAuth, **SMTP AUTH must be enabled** for the mailbox in the Exchange admin center. Check it at [aka.ms/smtp_auth_disabled](https://aka.ms/smtp_auth_disabled).
- **Authorization is blocked:** If your organization uses Microsoft **Security Defaults** (which block legacy auth), confirm SMTP AUTH is enabled for the specific account.
- **"Admin consent required" error:** Return to **API permissions** in Azure and make sure **Grant admin consent** was clicked for every permission.
- **Wrong account connected:** Re-authorize while logged in to Frappe as the intended final user, not Administrator.

**Sources:**

- [Tutorial: Connecting Frappe/ERPNext to Microsoft 365 Mail Services (OAuth)](https://discuss.frappe.io/t/tutorial-connecting-frappe-erpnext-to-microsoft-365-mail-services-oauth/106003)
- [Frappe Helpdesk — Installation](https://docs.frappe.io/helpdesk/installation)
- [Frappe Helpdesk — Email Communication](https://docs.frappe.io/helpdesk/email-communication)

---

<!-- page: helpdesk/helpdesk__field-dependency.md -->
---
title: "Field Dependency"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/field-dependency"
updated: "2026-03-02"
---

Dependency fields are those that have a parent-child relationship, such as the Category and Sub-category field values. The relevant Sub-categories will only be listed when the Category is also selected. Similarly, you may only need to list the specific issues when the main category is selected, or list the products based on the Category type. 
Such dependency fields can be created using the Field Dependency feature. 

Only Select or Link fieldtypes are supported.

> Note: This is only applicable while creating tickets.



# Adding a Custom Field
-------------------------


1. Create a new field using customize form. To do so, switch to Desk and navigate to HD Ticket doctype, then use the Customize Form option (for more details, follow this [documentation](https://docs.frappe.io/erpnext/user/manual/en/customize-form))
2. Copy the field name you want the user to fill while creating ticket.
3. Go to HD Ticket Template doctype (in desk) => open document named "default" => Paste the name in the  table shown in "fields" section. You can click on "Hide from customer" to hide fields from the customer portal.
(url: http://your_site_name//app/hd-ticket-template/Default)

e.g. 

![](/files/Screenshot%202025-03-29%20at%209.15.22%20PM.png)


# Implementing Field Dependency
---------------------------------
Now that you have added required custom fields in the **HD Ticket Template**, field dependency (customization) can be implemented in two ways:

1. Creating field dependencies from the portal UI.
2. Using HD Form Script in Desk

### Creating field dependencies from the portal UI.

To create field dependencies from the portal UI, follow these steps:

1. Open **Settings** from the User Dropdown.
2. Click on the **Field Dependencies** tab > Click on **New**.
3. Select the parent field and child field. If fields are previously added from the Field Dependency UI, they wont be available for selection in the child field dropdown while creating new field dependency.

> Note: Ensure that these fields are added in the HD Ticket template (default template).

4. For each parent field value, select the corresponding child field values that should be available when that parent value is chosen. If there are no child values selected for the parent value, the child field will not be editable.

![](/files/New%20FD.png)



#### Handling visibility of child field
Set the condition for the child field to be visible or hidden based on the parent field's value. If disabled, the child field will always be visible. 
If enabled, you can control when the child field appears - either for any parent field value ("Any") or only when specific parent field values are selected. You can click on "Clear" button to reset the value to "Any".


![](/files/Display%20depends%20on.png)

In this example, the child field "Sub Category", will be visible as soon as some value is set in the "Category" field.

#### Handling if the child field is mandatory
Set the condition for the child field to be mandatory or not based on the parent field's value.

If disabled, the child field will not be mandatory. If enabled, you can control when the child field is mandatory - either for any parent field value ("Any") or only when specific parent field values are selected. You can click on "Clear" button to reset the value to "Any".

> Note: If the child field is required, user can't keep that field as empty

![](/files/Display%20depends%20on.png)
In this example, the child field "Sub Category", will be require only if "Category" field's value is one of "Billing / Accounting / Payroll".



### Using HD Form Script in Desk

Open Desk: Switch to Desk and navigate to HD Form Script.
Select Doctype: Choose the Doctype (e.g., HD Ticket) where you want to add the custom action. You'll be presented with a boilerplate code.
Apply To: Choose "Form".
Enabling Script: Check "Apply on new page" & "Enabled" field.
Define Your onChange handler: Here's how to define different types of handlers for different Fields:


Let us say we have created two Select Fields called "App" & "Category" & based on the App selected I want to filter the options on "Category" field.

```
function setupForm({doc, applyFilters}) {
    
    function update_category(value) {
        if(value=="ERPNext"){
            options = ["Manufacturing","Accounting","Selling","Purchase"]
        }
        else if(value =="Frappe Cloud"){
            options = ["Payment","Bench Down","Site Down", "FC Marketplace"]
        }
        else if(value== "HRMS") {
            options = ["Attendance","Shift","Tax"]
            
        }
        applyFilters("custom_category",options)
    }
    
    return {
        onChange:{
//          works only for new ticket page
            "custom_app":(newVal)=>update_category(newVal)
        }
    }
}
```


In the example mentioned above when the ```custom_app``` field changes the ```update_cateogory``` function will be triggered and the new value of the ```custom_app``` field will be passed to the ```update_category``` function, and based on the new value we update the options using
```apply_filters``` function

this function takes 2 values as an argument

1. Field you want to change (can be a Select field or a Link field).

2. The Options you wanna show in the dropdown. (make sure to use the correct spelling). If null is passed then the options will reset to default.

Here is an example of implementation:
![](/files/New%20Option%20Depends.gif)


**Some more customisations**

* To hide or show a field use ```display_depends_on``` functionality using form [customisation](https://docs.frappe.io/erpnext/user/manual/en/customize-form), watch this [video](https://www.youtube.com/watch?v=H_gWt0EPZCE) to know more

e.g for update_category:
```eval:doc.custom_app!==""```



* To make a field mandatory bases on another field use ```mandatory_depends_on``` functionality using form [customisation](https://docs.frappe.io/erpnext/user/manual/en/customize-form). To know more read [this](https://docs.frappe.io/framework/v14/user/en/basics/doctypes/docfield)

e.g for making a application field mandatory use this expression:
```eval:doc.ticket_type==="Bug"```

video showcasing `mandatory_depends_on` & `display_depends_on` 

![](/files/Display%20and%20mandatory%20depends%20on.gif)

<!-- page: helpdesk/helpdesk__helpdesk__customization__outside-working-hours-banner.md -->
---
title: "Outside Working Hours Banner"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/helpdesk/customization/outside-working-hours-banner"
updated: "2026-05-08"
---

When users raise a ticket outside regular working hours, they may be confused about delayed responses. The Outside Working Hours Banner addresses this by notifying users of potential delays and setting clear expectations about response times.

To display the after-hours banner in the customer view, navigate to the **General** tab in the Settings view and enable the "**Outside working hours notice"** toggle, as shown below.

![](/files/Adobe Express - Screen Recording 2026-01-21 at 12.39.30 PM77d642.gif)

When you enable the toggle, a text input appears, allowing you to customize the banner message. Your customized message takes effect once you save the settings.

![](/files/Untitled design6ed650.gif)

Currently, you can use the following variables to personalize your banner message.

**Available variables:**

- `{{ ticket.name}}` — Ticket reference and other fields of the ticket can also be used. *e.g: #TKT-00123*
- `{{ next_working_day }}` — Full date with day name. *e.g: Monday, 23 Jan*
- `{{ next_working_date }}` — Short date format. *e.g: 23 Jan*
- `{{ expected_response }}` — Expected response time. *e.g: 09:00, Monday, 23 Jan*

**How does it work?**

Suppose your business working hours are set from 9 am to 6 pm on a working day. Now, a customer raises a ticket after 6 pm, say at 9 pm, outside of working hours, then what will happen?

Voila! A notice banner is now displayed for the ticket. Why? because according to the configured SLA for the ticket, the time 9pm is *outside working hours.*

![](/files/highlighted-banner.png)

Now, in the same scenario, let's say a day has passed, and now it's 12 pm on a working day according to your SLA.

![](/files/image313c83.png)

As you can see, the banner is no longer there. Why? because the ticket is now being viewed inside working hours. Seems confusing, but it's really simple.

`Inside Working Hours = No Banner`

`Outside Working Hours = Show Banner`

Additionally, if an agent replies to a ticket raised outside working hours, the banner will not be displayed again for that ticket.

> Note: The logic for the banner to be displayed solely depends on the SLA's configured for the tickets, also including the holiday list of that particular SLA, to read more about how SLA's work, click  [here](https://docs.frappe.io/helpdesk/service-level-agreement)

<!-- page: helpdesk/helpdesk__helpdesk__other-features__comment-reactions.md -->
---
title: "Comment Reactions"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/helpdesk/other-features/comment-reactions"
updated: "2026-05-28"
---

Comment reactions allow users to interact with comments using emojis. This feature provides a quick way to acknowledge feedback and keeps the ticket thread concise by reducing the need for short text responses.





**Enabling Comment Reactions:**

1. Navigate to **Settings** from the sidebar.
2. Go to the **General** tab under **App Settings**.
3. Under the **Ticket settings** section, find the toggle labelled '**Enable comment reactions'.**
4. Switch the toggle **on.**
5. Click the **Save** button at the top right of the page.

![](/files/img1.png)



**Adding Reactions:**

1. Whenever you are on ticket page.
2. See comments, under each comment you will see the **Reaction Icon** (plus-face emoji)
3. Select your desired emoji from the reaction picker.

![](/files/image060f45.png)





**Notifications for Comment Reactions**

When someone reacts to your comment, you’ll receive a notification.

Clicking the notification takes you directly to the comment that received the reaction.

![](/files/image50dde7.png)

  
  
  

<!-- page: helpdesk/helpdesk__installation.md -->
---
title: "Installation"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/installation"
updated: "2026-01-06"
---

Frappe Helpdesk can be installed in several ways depending on your requirements. You can choose to install it on Frappe Cloud, the cloud version of Frappe Helpdesk, or on your own server. The following sections describe the installation methods in detail.

## Managed Hosting

Install Frappe Helpdesk with one click on [Frappe Cloud](https://frappecloud.com/helpdesk/signup). Frappe Cloud is a managed hosting platform that makes installation and maintenance easy. Sign up [here](https://frappecloud.com/helpdesk/signup) to get started. Your instance will be ready in minutes. We recommend trying Frappe Cloud before self-hosting.

If you have an existing Frappe Cloud site, you can install Frappe Helpdesk from the [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/helpdesk).

## Self Hosting

### Production Setup

1. First, download the installation script:

    ```bash
    wget https://frappe.io/easy-install.py
    ```

2. Run this command to install Frappe Helpdesk:

    ```bash
    python3 ./easy-install.py deploy \
        --project=helpdesk_prod_setup \
        --email=your_email.example.com \
        --image=ghcr.io/frappe/helpdesk \
        --version=stable \
        --app=helpdesk \
        --sitename subdomain.domain.tld
    ```

You need to change two things in this command:

- Replace `your_email.example.com` with your actual email address
- Replace `subdomain.domain.tld` with your website domain name

The setup will take about 5 minutes. After that, you'll have a ready-to-use Frappe Helpdesk instance.

### Development Setup

If you want to set up Frappe Helpdesk for development, please check our [GitHub repository](https://github.com/frappe/helpdesk/tree/develop#development-setup) for detailed instructions.


## Frequently Asked Questions

### I have an existing self-hosted ERPNext site. How can I install Frappe Helpdesk on it?

You can install Frappe Helpdesk just like any other Frappe app. Following are the commands to get and install the app:

```bash
bench get-app helpdesk --branch main
bench --site your_site_name install-app helpdesk
```

### I am facing issues during installation. What should I do?

If you encounter any issues during installation, please raise a [GitHub issue](https://github.com/frappe/helpdesk/issues) with the error message and the steps you followed.

<!-- page: helpdesk/helpdesk__integration__erpnext.md -->
---
title: "ERPNext"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/integration/erpnext"
updated: "2026-06-11"
---

## ERPNext Integration

Frappe Helpdesk can stay in sync with ERPNext so that your customer records are never out of date. 

## Prerequisites

ERPNext must be installed on the same Frappe bench as Helpdesk. If ERPNext is not installed on your site, the UI will look like this.



![](/files/imagefd7e25.png)

## Enabling the Integration

1. Open Helpdesk and go to **Settings → Integrations → ERPNext**
2. Toggle **Enable ERPNext Integration** on.

Once enabled, you will see this banner at the bottom, and a "Sync Now" button

![](/files/image962c92.png)



The same button will also be visible in ERPNext HD Settings doctype.

![](/files/imagef6e57e.png)



When either of these buttons is clicked, the syncing process begins.



It takes from a few minutes to a few hours depending upon the size of your master data.



**How is the master data synced?**

The bulk sync performs a union merge:  

- ERPNext customers not in Helpdesk are added to Helpdesk.
- Helpdesk customers not in ERPNext are added to ERPNext.
- Customers that already exist by name on both sides are linked without creating duplicates.  After a successful bulk sync, every customer will exist in both systems and will be linked bidirectionally.



Once the syncing is done

1. If a Customer is created in Helpdesk, the same record is created in ERPNext Customer (if installed) automatically.
2. If a Customer is created in ERPNext, the same record is created in Helpdesk's Customer (if installed) automatically.
3. All the User Perms will also be synced.
4. All the documents that were shared will also be synced together.

This is how the UI will look in Settings of the Helpdesk Portal:

![](/files/imageea93eb.png)

## Disabling the Integration

Toggle **Enable ERPNext Integration** off in **Settings → General**.  
Existing records are preserved. No further changes will be mirrored until the integration is re-enabled. 



> [!WARNING]

> To sync the two doctypes, the user needs to have "write" permissions in both Customer & HD Customer DocType

<!-- page: helpdesk/helpdesk__inviting-agents.md -->
---
title: "Inviting agents"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/inviting-agents"
updated: "2026-01-06"
---

> Note: This feature is available only on the `develop` branch

The Invite Agents tab in the settings modal can be used to invite new or existing (haven't been invited yet) users to Helpdesk.

![invite agents tab in the settings modal](/files/Screenshot%202025-08-12%20at%201.11.50%E2%80%AFPM.png)

## Steps to invite

1. List out the emails you wish to invite in a comma-separated format.
    
    
    !['invite by email' field filled example](/files/Screenshot%202025-08-12%20at%201.23.22%E2%80%AFPM.png)

2. Select a suitable role.
    
    > If you are a `Manager`, you will be only shown `Agent` or `Manager` options

    
    !['role' field select expanded example](/files/Screenshot%202025-08-12%20at%201.26.35%E2%80%AFPM.png)

3. Trigger the invitation action using the 'Send Invites' button.
    
    
    ![invites sent example](/files/Screenshot%202025-08-12%20at%205.11.42%E2%80%AFPM.png)

All of the email addresses that were successfully invited will receive an invitation email with a link to accept the invitation. The sent invitations auto-expire in 3 days. Once an invitation expires, an email will be sent to the sender of the invitation.

## Cancel an invitation

To cancel a pending invitation, you can trigger the cancel invitation action using the 'Cancel Invitation' button in the UI.


![cancel a pending invitation](/files/Screenshot%202025-08-12%20at%205.20.45%E2%80%AFPM.png)

Once the invitation is cancelled, an email is sent to let the invitee know that the invitation was cancelled.

## Accept an invitation

To accept an invitation, use the link present in the invitation email. The link will redirect the invitee to a page that can be used to set/update the password **if a new [Framework](https://docs.frappe.io/framework/user/en/introduction) user was created because of accepting the invitation**.

To disable redirecting the invitee to set a password, you can disable username/password login present under the System Settings section of the Desk view.


![system settings](/files/Screenshot%202025-08-12%20at%205.42.02%E2%80%AFPM.png)

<!-- page: helpdesk/helpdesk__knowledge-base.md -->
---
title: "Knowledge Base"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/knowledge-base"
updated: "2026-01-06"
---

The Knowledge Base in Frappe Helpdesk is a centralized repository of information designed to assist both support agents and customers in finding solutions to common issues. It serves as a self-service tool that helps reduce the number of support tickets by enabling users to resolve problems on their own.

![Screenshot 2024-07-19 at 2.20.12 PM](/files/Screenshot 2024-07-19 at 2.20.12 PM.png)  


Key Features of the Knowledge Base
----------------------------------

* **Articles and Documentation**: Contains a variety of informational content, such as FAQs, how-to guides, troubleshooting steps, and detailed documentation addressing common questions and issues.
* **Search Functionality**: Users can quickly find relevant articles by searching for keywords or phrases, enhancing ease of use and efficiency.
* **Categorization**: Articles are organized into categories to facilitate easy navigation and searching.
* **User-Friendly Interface**: Designed with a clean and intuitive interface, allowing users to browse categories or search for specific information effortlessly.

Use Cases for the Knowledge Base
--------------------------------

* **Self-Service for Customers**: Enables customers to find answers to their questions and resolve issues independently, reducing the need to contact support. This decreases the volume of incoming support tickets and allows customers to get help instantly.
* **Support Agent Resource**: Provides support agents with quick access to solutions for common problems, ensuring consistent and accurate responses to customer inquiries. It also serves as a training resource for new agents.
* **Product Documentation**: Houses comprehensive product documentation, including user manuals, feature descriptions, and update notes, helping customers understand and use the product more effectively.
* **Troubleshooting Guides**: Offers detailed troubleshooting guides that assist both customers and agents in diagnosing and resolving technical issues.

Benefits of the Knowledge Base
------------------------------

* **Efficiency**: Reduces the time support agents spend on repetitive issues, allowing them to focus on more complex problems.
* **Consistency**: Ensures customers receive consistent and accurate information across all support interactions.
* **Customer Satisfaction**: Improves customer satisfaction by providing immediate answers and reducing wait times for support.
* **Cost-Effective**: Lowers support costs by enabling self-service and reducing the volume of support tickets.

By leveraging the Knowledge Base, Frappe Helpdesk enhances the efficiency of support operations, provides valuable resources to both customers and agents, and ultimately improves the overall support experience.

<!-- page: helpdesk/helpdesk__lesson-1-your-first-ticket.md -->
---
title: "Creating a ticket"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/lesson-1-your-first-ticket"
updated: "2026-01-06"
---

Once you have [set up](https://docs.frappe.io/helpdesk/settings) your Email account, you are ready to get started with helpdesk.

When you land on Helpdesk for the first time your URL should be "/helpdesk/tickets".

This view shows you the list of all the tickets, in the begining you will see only one ticket:

![](/files/Screenshot%202025-04-21%20at%201.44.27%20AM.png)

## Channels to create tickets
In Frappe Helpdesk you can create tickets by many ways:

1. Email
2. Customer Portal
3. Agent Portal


### Email
When you set up your email account, and enable that account as incoming or default incoming, all the emails you will receive on that email will be converted to tickets in your Helpdesk Portal. The system pulls the emails from your account every 10 minutes.


### Customer Portal


<!--Let us talk about creating tickets from the *Customer Portal* first:-->

Agents/Admins can navigate to Customer Portal and create ticket by:
![](/files/CP%20new.gif)

When you click on "Customer Portal" in the dropdown you will be navigated to the route

`/helpdesk/my-tickets`

Click on username => Customer Portal => New => Add info => Submit


For Customers:
When the customer login they will be directed to Customer Portal directly.

### Agent Portal


On the top right corner (agent portal) you will see a button called "Create", click on it and you will be navigated to "New Ticket Page" with url `/helpdesk/tickets/new`.

![](/files/Screenshot%202025-04-21%20at%201.46.29%20AM.png)

Fill the subject & description using our Rich Text Editor which provides support for headings, list, attachments and much more.

Once you fill the information, click on "Submit" button or use the shortcut "cmnd/ctrl + Enter", to create a new ticket.

When a ticket is created you will be navigated to the created ticket. 

![](/files/Screenshot%202025-04-21%20at%201.48.58%20AM.png)


**Emails**

1. When a ticket is assigned to an agent, the agent receives an email.
2. Whenever a customer replies on a ticket, agent received the email.



You have successfully created your first ticket 🎉

Let's move to the [next section](https://docs.frappe.io/helpdesk/lesson-2understanding-ticket-view), to understand the ticket view in detail!

<!-- page: helpdesk/helpdesk__lesson-2understanding-ticket-view.md -->
---
title: "Understanding ticket view"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/lesson-2understanding-ticket-view"
updated: "2026-01-16"
---

![](/files/Ticket%20Basic%20Info.png)

- SLA information: Here you can see the SLA information, like when is the first response due or when is the resolution due, we will cover how to create & manage SLA's in the upcoming lessons.
- Description: Whatever we added as description (in above img) shows up as the first communication.
- Ticket Additional Info: Some more info regarding the ticket. We will cover how to show more fields here in the upcoming sections.

### Assigning tickets to agent

Let us try to assign this ticket to an agent, click on "Assign" button at the top

![](/files/Assign%20btn.png)

Once you click on the button, a dialog will open

![](/files/Screenshot%202025-04-21%20at%202.25.52%20AM.png)

When you click on "Select an option", you will see "No results found", this is because we now need to add agents to our system, follow this link to add agents, and get back here.

Now when you click on "Assign" button, the new agent will be populated, select the agent and the ticket will be assigned to that agent.

![](/files/Screenshot%202025-04-21%20at%202.48.35%20AM.png)

As you can see the ticket is assigned to the agent.

### Replying to a ticket

You can reply to tickets in two ways:

![](/files/Reply%20buttons.png)

1. Reply Button at bottom corner:

When you click on the reply button, a editor pops up.
As soon as you click on it the "To" field automatically gets filled up by the person who has raised the ticket.

This editor has various functionalities like:

- Autocomplete on adding new emails
- CC & BCC
- Text formatting
- Adding videos & images to the reply
- Adding attachments
- Auto applying canned responsed (email button), read more about it from here.

![](/files/Reply.png)

1. Reply Icon on each email:

Sometimes in a long conversation, agents wants to reply on a particular "email" from the customer.

Agents can click on the "reply icon" on an email, and all the context related to that email will be shown in the text editor. This saves the agent the hastle to manulalyt copying & pasting the replies and formatting them.

![](/files/Screenshot%202025-04-22%20at%2012.45.07%20AM.png)

### Adding a private note (comment)

Sometimes you need to jot down a quick thought or share internal info without the customer seeing it. That’s where private notes come in handy. You can add context, loop in teammates, or leave reminders—all right inside the ticket, just for your team’s eyes.

Comments are for internal team, they will never be displayed to the customer.

![](/files/Commentfdcacc.gif)

When you click on comment, you can mention any agent from your system, whoever you mention will receive an Email saying "you were mentioned in this comment, on this ticket".



You can also **react** to **comments**, read more about it from [here.](https://docs.frappe.io/helpdesk/helpdesk/other-features/comment-reactions)



### Ticket Statuses in Frappe Helpdesk

In Frappe Helpdesk, each support ticket moves through one of the following four statuses, the SLA applied on the ticket is used.

![](/files/Screenshot%202025-04-22%20at%201.28.53%20AM.png)

1. 🔴 **Open**
2. 🔵 **Replied**
3. 🟢 **Resolved**
4. ⚫️ **Closed**

Each status interacts with SLA timers differently. Here's how:

---

#### 🔴 Open

- SLA timers are **active**.
- Both **First Response Time** and **Resolution Time** are tracked based on the SLA applied to the ticket.

---

#### 🔵 Replied

- Can be set by an agent only, usually is markd when an agent replies to the customer.
- The system checks **First Response SLA**:
  - ✅ **Successful** if the first reply was within SLA time.
  - ❌ **Failed** if it was late.
- While in this status:
  - **Resolution SLA** is **paused**.
  - It stays paused until the customer replies again.
- On customer reply:
  - The ticket moves back to **Open**.
  - Assigned agents are notified by email.

---

#### 🟢 Resolved

- Set when the issue is considered solved by the agent.
- SLA evaluation happens:
  - If **First Response** hasn’t been marked yet, it’s evaluated now.
  - Both **First Response** and **Resolution** are marked:
    - ✅ If done within time → **Successful**
    - ❌ If delayed → **Failed**
- Customers can still reply to reopen the ticket.
  - Ticket status changes back to **Open** on reply.

---

#### ⚫️ Closed

- Final stage of the ticket.
- SLA evaluation rules:
  - If **First Response** not already marked, it's evaluated.
  - **Resolution** SLA is always checked:
    - ✅ Within SLA time → **Successful**
    - ❌ Delayed → **Failed**
- If **First Response** was already marked (Success/Fail), only **Resolution SLA** is re-evaluated.
- A ticket can be **Closed** in two ways:
  1. **Customer closes the ticket** – They are prompted to leave feedback (you can make feedback mandatory or optional via the **HD Settings** doctype).
  2. **Agent manually closes the ticket** from their side.
- Once a ticket is closed:
  - The **customer can no longer reply**.
  - Only agents can **reopen**, **reply**, or **add private comments** in a ticket.

---

#### 🕒 What does “First Response marked” mean?

A ticket is marked for **First Response** when an agent replies for the first time, and the system checks if the reply was sent within the **First Response Time** defined in the SLA. This helps measure how quickly the team acknowledges a customer issue.

---

You can read more about SLA's from here. This page will tell you about how SLA is calculated and how you can create one.

Next we’ll explore assigning tickets to teams and managing tickets.

<!-- page: helpdesk/helpdesk__lesson-3-agents-teams.md -->
---
title: "Agents & Teams"
space: "Helpdesk"
url: "https://docs.frappe.io/helpdesk/lesson-3-agents-teams"
updated: "2026-01-06"
---

In Helpdesk, the way tickets are handled depends on three key concepts: Roles, Agents, and Teams. 
### 1. Roles

Roles define what a user can do in the system. There are three main roles:

- **Admin**  
  Has full access across the system — including all tickets, settings, teams, and configurations.

- **Agent Manager**  
  - Work on tickets  
  - Delete tickets  
  - Create custom views and manage [public views](https://docs.frappe.io/helpdesk/custom-views) 
  - Manage Knowledge Base articles
  - Manage Dashboard and get an overview of other agents in your team

- **Agent**  
  - Work on tickets  
  - Create custom views and manage private views
  - Manage Knowledge Base articles
  - Manage Dashboard only for themselves

These roles help control permissions and ensure each user sees and does only what they’re meant to.

---

### 2. Agents

Agents are the users responsible for working on support tickets. They’re assigned to tickets directly or through teams. Read [more](https://docs.frappe.io/helpdesk/agent) about agents.

- They can belong to one or more teams.
- Their workload is managed either manually or automatically through assignment rules.

---

### 3. Teams (Agent Groups)

Teams, also referred to as **Agent Groups** in single ticket view, are used to group agents for ticket distribution and assignment.

- A team consists of one or more agents.
- When a new team is created, an [Assignment Rule](https://docs.frappe.io/helpdesk/assignment-rule) is automatically created in the system.
- This rule ensures that when a ticket is assigned to that team, the system will pick one of the team members and assign the ticket to them — based on round-robin, load balancing, or some other logic.

You can manage the members of a team anytime — adding or removing agents immediately affects who gets assigned tickets.


Helpdesk creates two teams for you by default. Try adding members in each team and then try to assign a ticket to another team. You will notice that on changing the team (Agent Group), the ticket gets re-assigned to the agent of the selected team.


![](/files/Auto%20Assignment.gif)

#### Custom Assignment Logic

You can also define your own assignment logic using [Server Scripts](https://docs.frappe.io/framework/user/en/desk/scripting/server-script).

For example, assign tickets to different teams based on priority:

This server script below ensures that based on priority, the teams & agents are assigned automatically.

Here is an example of auto agent group assignment:


![](/files/Server%20Script%20Assg.gif)


![](/files/Screenshot%202025-04-22%20at%205.08.05%20PM.png)

```
if doc.priority == "Low":
    doc.agent_group = "Team A"
else:
    doc.agent_group = "Team B"
```


Now let us understand how you can reduce your ticket count and provide your customers with resolution faster using Knowledge Base.

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
