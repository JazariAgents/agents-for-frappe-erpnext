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
