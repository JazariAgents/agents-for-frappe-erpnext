<!-- Frappe documentation: erpnext, part 23 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__e_commerce_settings.md -->
---
title: "E Commerce Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/e_commerce_settings"
updated: "2026-03-02"
---

The legacy **Shopping Cart Settings** and **Products Settings** are combined into a single **E -Commerce Settings** page. 

The e-commerce settings in ERPNext can be leveraged by users to manage and streamline the online sales processes. These settings can enable users to efficiently manage product listing, customer management and integration with other ERPNext modules seamlessly.


> **E Commerce Settings / Webshop Settings** in the awesomebar (search bar)
> 
> 

[Screenshot on the live page: E Commerce Settings] *E Commerce Settings*

### Products Per Page

Define how many products to show per page on the Product Listing in the **All Products** page (`/all-products`).

### Filters and Categories

[Screenshot on the live page: Filters and Categories] *Filters and Categories*

You can also add filters to your listing. There are two types of filters:

1. **Field Filters**: Enable the **Field Filters** checkbox and add the fields based on which you want to have filters. These fields will also be used as categories for the **Shop by Category** page.
2. **Attribute Filters**: Enable the **Attribute Filters** checkbox and add the attributes based on which you want to have filters.

### Display Settings

1. **Hide Variants**: Only show Website Item Templates on the Product Listing.
2. **Enable Variant Selection**: Show a configure button if the Item has variants. It can be used to narrow down the specific item based on Attributes.
3. **Show Price**: Show Item Price on the product page.
4. **Show Stock Availability**: Show whether the Item is in stock.
5. **Show Stock Quantity**: Show available stock on the product page.
6. **Allow items not in stock to be added to cart**: Allow items not in stock to be added to Cart.
7. **Show Apply Coupon Code**: Additional provision to apply coupon code at checkout.
8. **Show Contact Us Button**: Show a contact us button which customers can use to enquire about the Item. It will create a Lead in the system.
9. **Show Public Attachments**: Show public attachments in the Sales Order generated, after checkout, for Customers.


> You can **Hide Variants** only when Attribute Filters are disabled.
> 
> 

### Shopping Cart

1. **Company**: Specify the company that the web shop is set up for.
2. **Price List**: Mention Price List to consider while fetching Item Prices.
3. **Enable Shopping Cart**: Add the provision to add items to Cart.
4. **Default Customer Group**: Add the Default Customer Group to be set while auto creating customers on adding to Cart.

### Checkout Settings

1. **Enable Checkout**: If checkout is disabled, when your customers add an item to Cart, they can click on the **Request for Quotation** button to get a quote for it. A [Quotation](/erpnext/quotation) is generated in the system. If enabled, a [Sales Order](/erpnext/sales-order) is generated on clicking on the **Place Order** button in the Cart.
2. **Payment Gateway Account**: If checkout is enabled, you must have [PayPal Integration](/erpnext/paypal-integration) or [Razorpay Integration](/erpnext/razorpay-integration).
3. **Payment Success Url**: After payment completion redirect users to the selected option.
4. **Show Price in Quotation**: If checkout is disabled, you can choose whether or not to show prices against Website Items in the Quotation.
5. **Save Quotations as Draft**: If checkout is disabled, on clicking on the **Request for Quotation** button, you can choose whether the auto-generated Quotation must be auto-submitted or kept in the Draft state.

### Add-ons

1. **Enable Wishlist**: Add the provision to add items to a Wishlist
2. **Enable Reviews and Ratings**: Add the privision for **customers** to leave reviews and ratings against Website Items.
3. **Enable Recommendations**: Add the provision to show manually selected **recommended items** against a Website Item.

### Shop By Category

The **Shop By Category** page is an out-of-the-box page that lists categories linked to Website Items. These categories can be configured in the **Filters and Categories** section's **Field Filters** table.

You can also select a slideshow as the banner of the page.

### Guest Display Settings

1. **Hide Price for Guest**: You can show or hide prices against Website Items for guest users (users who are not logged in).
2. **Redirect on Action**: If a guest user tries to add a Website Item to Cart or to the Wishlist, you can select a URL to redirect them to. By default, guest users are redirected to the `/login` page. You can instead redirect them to a custom Web Form of choice by adding a URL here e.g. `/contact-us`

<!-- page: erpnext/erpnext__easy-steps-to-setup-workflow.md -->
---
title: "Easy steps to setup Workflow"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/easy-steps-to-setup-workflow"
updated: "2026-03-04"
---

When a company has multiple levels of approval for a document, a Workflow can be set.   
In ERPNext, you can go to Workflow list --> Create New --> Name the workflow and define :1. States
2. Transition rules.

  
1. States :

When a document is passed on for different levels of approval, there are states defined at each level for the role of the user.   
[Screenshot on the live page]  
  
1. Transition Rules :

For instance: A **Sales user** is only allowed to create a **Quotation** and it can be saved in the **Draft** state. Further, it can be sent to the **Sales Manager** for approval and the User with this role can have the permission to either **Approve** or **Reject** the Quotation after which it can either be sent to the **Draft** State if **Rejected** or final **Approved** State.   
[Screenshot on the live page]  
Error Messages: **A document cannot be Cancelled before it is Submitted.**   
[This is a typical error faced by users who define the state of the Document cancelled before Submitting it. Doc Status 1 defines that the Document will be Submitted at that State, thus the State with Doc status 2 should only be defined in the Transition after the State with Doc status 1. ]  
Setup a Simple Workflow to begin with and let us know what you think more on Workflows! We love to see our Users Happy!! ;)   
  

<!-- page: erpnext/erpnext__edit-submitted-document.md -->
---
title: "Edit Submitted Document\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/edit-submitted-document"
updated: "2026-03-04"
---


To edit a submitted document, you need to cancel it first. Following are steps to edit submitted document. These steps assume you have the appropriate permissions for cancelling and editing a document.

#### Step 1: Cancel Submitted Document

You will find Cancel button on upper right corner of submitted document.

[Screenshot on the live page: Cancel Doc]

#### Step 2: Amend the document

On cancellation of submitted document, Amend button will be became visible.

[Screenshot on the live page: Amend Doc]

#### Step 3: Save and Submit the document

On clicking Amend button, same document will become editable again. After Making required changes, save and submit the document.

[Screenshot on the live page: Resave and Submit Doc]
Note: If your document is linked with other documents, then you will need to cancel the dependant document before cancelling the parrent document.

Example: If you have created Delivery Note and Sales Invoice against Sales Order, which you need to amend, then you should first Cancel Delivery Note and Sales Invoice made for that Sales Order. Then amend Sales Order, re-save and re-submit it.

<!-- page: erpnext/erpnext__editing-a-field-after-submission.md -->
---
title: "Edit a Field after Submission "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/editing-a-field-after-submission"
updated: "2026-03-04"
---

In ERPNext, once a document is submitted, you can only edit it through Cancel > Amend. However, you can still make certain fields (custom fields) editable after submission using the **Allow on Submit** feature. For example, we have created a custom field called "Supplier ID" in Supplier Quotation. To allow editing of this field after submission, follow the following steps:  
1) Go to Settings > Customize Form and select the Form Type (Supplier Quotation in this case).  
2) Expand the field row and check the "Allow on Submit" checkbox.  
[Screenshot on the live page]  
[Screenshot on the live page]  
  
3) Click on Update.  
This setting will allow you to edit this field even after submitting the document without amending it.  
**Note:** The Allow on Submit feature works only for non-standard fields (custom fields).

<!-- page: erpnext/erpnext__education-module-in-erpnext.md -->
---
title: "Education Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/education-module-in-erpnext"
updated: "2026-07-04"
---

## Overview

Frappe Education is an open-source education management app for the Frappe and ERPNext ecosystem. It helps schools, colleges, coaching institutes, and other academic institutions manage academic administration, student information, courses, admissions, fees, scheduling, and student self-service in one system.

The app is built on Frappe Framework and works alongside ERPNext, so institutions can manage academic operations while still using ERPNext for accounting and other business processes.

## GitHub Repository

Source code: [github.com/frappe/education](https://github.com/frappe/education)

The repository describes Frappe Education as an open-source Education Management System for streamlining administrative and academic processes in educational institutions.

## When To Use Frappe Education

Use Frappe Education when an institution needs an ERPNext-backed system for academic operations, not just a learning management system. It is useful when student records, instructors, courses, admissions, fee collection, and academic schedules need to be managed in a structured way.

## Key Features

- **Student and teacher management:** Maintain profiles and academic records for students, guardians, and instructors.
- **Admissions:** Manage student applications and admission workflows from enquiry to enrollment.
- **Programs and courses:** Define academic programs, courses, batches, terms, and course schedules.
- **Attendance:** Track student attendance and use it for academic administration and reporting.
- **Fee management:** Create fee structures, schedule fee collection, and track payment status.
- **Student portal:** Let students access information such as timetables, attendance, fees, and grades.

## How It Fits With ERPNext

Frappe Education extends ERPNext for education-specific workflows. ERPNext provides the broader ERP foundation, while Frappe Education adds the academic objects and flows needed by educational institutions. This makes it suitable for organizations that want both education management and ERP-style accounting or operations in the same ecosystem.

## Related Links

- [Frappe Education on GitHub](https://github.com/frappe/education)
- [Frappe Education website](https://frappe.io/education)
- [Frappe Education documentation](https://docs.frappe.io/education)

<!-- page: erpnext/erpnext__electronic-signature.md -->
---
title: "Signature Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/electronic-signature"
updated: "2026-03-04"
---

  


Electronic signature can be created in ERPNext using the Signature field type. This field allows you to write a signature in a block, just like the signature on a paper.

To create an electronic signature, follow the following steps:

1. Open the DocType and go to Customise Form.
2. In the Form view or Fields table, create a new field called Signature and select the Field Type as **Signature.**

[Screenshot on the live page: Screenshot 2024-06-21 at 5.32.17 PM]  


[Screenshot on the live page: Screenshot 2024-06-21 at 5.29.51 PM]  


3. Click on Update.
4. Refresh the page and put your signature.

[Screenshot on the live page: Screenshot 2024-06-21 at 5.27.47 PM]  


  

<!-- page: erpnext/erpnext__email-account.md -->
---
title: "Email Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-account"
updated: "2026-03-02"
---

**You can sync your email account with ERPNext to send and receive emails from ERPNext.**

You can manage multiple incoming and outgoing Email Accounts in ERPNext. There has to be at least one default outgoing account and one default incoming account. If you are on the ERPNext cloud, the default outgoing email is set by us.

To access Email Accounts, go to:

> Home > Settings > Email Account

1. Prerequisites
----------------

Before creating an Email Account, you need an [Email Domain](/erpnext/email-domain). However, you can skip creating an Email Domain if you're using one of the services listed below, then create [here](/erpnext/email-inbox#2-create-an-email-domain) for set up

* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* [**Outlook.com**](http://Outlook.com)
* **Yandex.mail**

2. How to create an Email Account
---------------------------------

1. Go to the Email Account list, click on New.
2. Enter the email address with the domain. [Domains](/erpnext/email-domain) need to be created in order to create an email account. You don't need to create a domain if you're syncing an email from certain providers as listed [here](/erpnext/email-inbox#2-create-an-email-domain).
3. Enter the email account password.
4. Save. If the credentials are correct, the email account will be synced.


> For some services like Gmail, you may need to enable 2FA and use [App Passwords](https://myaccount.google.com/u/0/apppasswords).
> 
> 

### 2.1 Additional options when creating an Email Account

1. **Use Different Email Login ID**: To use an alternative email login and password to access this account. For example, if you have [notifications@example.com](mailto:notifications@example.com) and you want users to access this email with an alternate email ID, they should tick this checkbox. The recipients will see [notifications@example.com](mailto:notifications@example.com) as the sender.
2. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox. When the other user logs in, they'll be prompted to enter the password.
3. **Use ASCII encoding for password**: Ticking this will use ASCII encoding for the password.

3. Configuration of the Email Account
-------------------------------------

### 3.1 Default Email Accounts

ERPNext will create templates for a bunch of email accounts by default. Not all of them are enabled. To enable them, you must set valid email account details.

There are two types of email accounts, outgoing and incoming. Outgoing email accounts use an SMTP service to send emails and emails are retrieved from your inbox using an IMAP or POP. Most email providers such as Gmail, Outlook, or Yahoo provide these services.

[Screenshot on the live page: Defining Criteria]  


### 3.2 Incoming Email Accounts

To set up an incoming Email Account, check on **Enable Incoming** and set your POP3 settings, if you are using a popular email service, these will be preset for you.

[Screenshot on the live page: Incoming EMail]  


The following options are available for incoming emails:

1. **Use IMAP**
2. **Use SSL**
3. **Attachment Limit**
4. **Default Incoming**: If ticked, all replies to your company (eg: [replies@yourcomany.com](mailto:replies@yourcomany.com)) will come to this account.
5. **Email Sync Option**: Whether to sync all or only unseen emails.
6. **Initial Sync Count**: Number of emails to sync the first time.

#### Automatic Document Creation Through Linked Emails

This feature creates documents when an email is sent to a particular pre-configured email.

For example, you can link [support@example.com](mailto:support@example.com) to the Issue DocType. After doing this, whenever an email is sent to [support@example.com](mailto:support@example.com), the system will automatically create an Issue is the system.

Similarly, if you link [jobs@example.com](mailto:jobs@example.com), when emails are sent to [jobs@example.com](mailto:jobs@example.com), a Job Applicant document is automatically created.

Enable Automatic Linking in Documents will link emails to documents, to know more [click here](/erpnext/linking-emails-to-document).

### 3.4 Outgoing Email Accounts

All emails sent from the system, either by the user to contact or via notifications or via transaction emails, will be sent from an Outgoing Email Account.

To set up an outgoing Email Account, check on **Enable Outgoing** and set your SMTP server settings, if you are using a popular email service, these will be preset for you.

[Screenshot on the live page: Outgoing EMail]  


The following options are available for outgoing emails:

1. **Use TLS**
2. **Port**
3. **Disable SMTP server authentication**
4. **Add Signature**: The default signature is appended to the end of each email.
5. **Default Outgoing**: Notifications and bulk emails will be sent from this outgoing server.
6. **Always use Account's Email Address as Sender**: The email address of this account will be mentioned as the sender for outgoing emails.
7. **Send unsubscribe message in an email**: Send a link to unsubscribe from emails sent from this account.
8. **Track Email Status**: Track if your email has been opened by the recipient. Note that, if you're sending to multiple recipients, even if one recipient reads the email, it'll be considered "Opened".
9. **Enable Auto Reply**: If enabled, enter an auto-reply message.
10. **Append Outgoing Email to Sent Folder**: If using custom email servers like Zimbra or CPanel, SMTP will not automatically append emails to the Sent folder. Enabling this option will ensure all emails are explicitly appended to the email account's Sent folder.
11. **Use SSL for Outgoing Emails**: Use SSL as a standard for outgoing emails. Defaults to port 465.

4. How ERPNext handles replies
------------------------------

In ERPNext when you send an email to contact like a customer, the sender will be the user who sent the email. In the **Reply-To** property, the Email Address will be of the default incoming account (like `[replies@yourcompany.com](mailto:replies@yourcompany.com)`). ERPNext will automatically extract these emails from the incoming account and tag them to the relevant communication.

> **Note for self implementers:** For outgoing emails, you should set up your own SMTP server or sign up with an SMTP relay service like mandrill.com or sendgrid.com that allows a larger number of transactional emails to be sent. Regular email services like Gmail will restrict you to a limited number of emails per day.

If you encounter errors when configuring an email account, refer to [this page](/erpnext/email-error).

5. Video
--------

### 6. Related Topics

1. [Email Inbox](/erpnext/email-inbox)
2. [Email Digest](/erpnext/email-digest)
3. [Auto Email Reports](/erpnext/auto-email-reports)
4. [Sending Email](/erpnext/sending-email)
5. [Email Domain](/erpnext/email-domain)

<!-- page: erpnext/erpnext__email-campaign.md -->
---
title: "Email Campaign | ERPNext Documentation"
description: "Learn how to create an Email Campaign in ERPNext using email templates, schedules, and recipient records."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-campaign"
updated: "2026-07-23"
---

**An Email Campaign is a coordinated set of emails sent to leads or contacts according to a particular schedule.**

Email Campaigns are still one of the most effective ways to reach your Customers, Contacts or Leads and keep them engaged. For example, you could set up Email Campaigns for introducing your product to the customers, with every email revealing an interesting feature of your product.

To create an Email Campaign, go to:

> Home > CRM > Campaign > Email Campaign

## Prerequisites

Before creating and using Email Campaign, these need to be created first:

- [Campaign](/erpnext/campaign)
- [Lead](/erpnext/lead) or [Contact](/erpnext/contact) or [Email Group](/erpnext/email_group)

## How to Create an Email Campaign

- Go to the Email Campaign list, select New.
- Select the [Campaign](/erpnext/campaign) for which you want to set up an Email Campaign.
- Set the 'Start Date' for the Email Campaign.
- In 'Email Campaign For', select whether you want to set up Email Campaign for a Lead or a Contact or for an Email Group to send to multiple email contacts.
- In 'Recipient', select the respective Lead or Contact or Email Group for whom you want to start the Email Campaign.
- In 'Sender', select the user of the system who should be the sender of the emails.
- SaveEmail Campaign (picture on the live page)

he above Email Campaign is for the following Campaign:

Campaign Schedule (picture on the live page)

*Note**: The **Send After (days)** field in Campaign specifies the day on which email is to be sent relative to the **Start Date** of **Email Campaign**. Notice the 'End Date' in the above Email Campaign. It is '26-07-2019', which is 4 days after the 'Start Date', '22-07-2029', as the Campaign Schedule ends on day 4.

### Create multiple Email Campaigns for a Campaign

You can also create new Email Campaigns for different Leads or Contacts for the same Campaign though the Campaign Dashboard.

- Go to the Campaign for which you want to create Email Campaigns.
- select + in front of Email Campaigns to create a new Email Campaign for the Campaign.Email Campaigns from Dashboard (picture on the live page)

## Features

### Linked Communication

When emails are sent to the respective leads or contacts, Communication is linked to the Email Campaign document. You can view all the emails sent in your document.

[Screenshot on the live page: Linked Communication]

### Unsubscribe from Email Campaign

If a lead or contact does not want to continue getting emails regarding the campaign, he or she can unsubscribe from the Email Campaign via the unsubscribe link sent with the email.

[Screenshot on the live page: Unsubscribe Link]

When the lead or contact unsubscribes, the status of the Email Campaign document changes to 'Unsubscribed'.

[Screenshot on the live page: Unsubscribed]

### Use Lead or Contact fields in Email Template

 The Email Template has the context of the document you have specified in the 'Email Campaign For' field. If you want to display the fields from your Lead or Contact document in your Email Template you will have to use doc.fieldname for the same.  
 For example, if 'Email Campaign For' is 'Contact', you can mention the 'first name' of your Contact as doc.first_name in the Email Template as shown below:

[Screenshot on the live page: Email Template Document]

Then the emails sent would look like this:

[Screenshot on the live page: Email Campaign Doc Data]

### Status indication

Status indicates the state of the Email Campaign, the various Statuses are:

- **Scheduled**: When the Email Campaign has not yet started but scheduled on a future 'Start Date'.
- **In Progress**: The campaign would be marked as 'In Progress' between 'Start Date' and 'End Date' of the campaign.
- **Completed**: After the 'End Date' of the campaign, the status will be changed to 'Completed'.
- **Unsubscribed**: When the Lead or Contact unsubscribes from the Campaign.

[Screenshot on the live page: Email Campaign Status]

## Related Topics

- [Campaign](/erpnext/campaign)
- [Lead](/erpnext/lead)
- [Contact](/erpnext/contact)

Next: [Newsletter](/erpnext/newsletter)

<!-- page: erpnext/erpnext__email-digest.md -->
---
title: "Email Digest\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-digest"
updated: "2026-03-02"
---


**Email Digests allow you to get regular updates about your sales, expenses and other critical numbers directly in your Email Inbox.**

Email Digests are a great way for top managers to keep track of the big numbers like “Sales Booked” or “Amount Collected” or “Invoices Raised” etc.

To set up Email Digest, go to:

> Home > Settings > Email Digest

1. Enter a name for the Email digest.
1. Set the frequency of mails to be sent.
1. Add or remove recipients.
1. Select the items to be included in the digest.
1. Save.

Example:

[Screenshot on the live page: Email Digest]

### Related Topics
1. [Auto Email Reports](/erpnext/auto-email-reports)
1. [Sending Email](/erpnext/sending-email)

<!-- page: erpnext/erpnext__email-domain.md -->
---
title: "Email Domain"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-domain"
updated: "2026-03-02"
---


**The ``Email Domain`` is the display name of an email network/service account you're setting up for your email services in ERPNex and other Frappe apps.**

You can skip to [Email Account](/erpnext/email-account) creation if you are using one of the services listed [here](/erpnext/email-inbox#2-create-an-email-domain).

You can configure Email Domains in ERPNext for easy setup of all Email Accounts. To find Email Domain settings go to:

> Home > Settings > Email Domain

**What is my Email Domain?:** You might have purchased an Email service from your internet service provider or your IT services provider. For example, if you access your business mailbox with URL like http://mail.yourcompany.com, then yourcompany.com is expected to be used as your email domain. ERPnext tries to guess the ``Email Domain`` from your initially entered example ``Email Address`` if you started from there.

If you want to send and receive emails on your ERPNext account, you need to correctly setup an ``Email Domain``. You may be using free mail services like GMail or Yahoo. In this case, you don't need to create a domain, instead select a service provider from the list. However, you might have to allow access to ERPNext for your GMail account.

ERPNext creates a template ``Email Domain`` using example.com for your reference. You should add your new domain if you want to use it in your ERPNext account.

> **IMPORTANT:** If your actual mail account id differs from the work email address you use in the ``Email Account``setup later, you need to use the option ``Use different Email ID`` when creating the different work mail accounts to communicate with your service and use the related password!

[Screenshot on the live page: Email Domain]

## 1. How to create an Email Domain
1. Go to the Email Domain list, click on New.
1. Enter the Example Email Address. This is where you enter your business email address. For example, if your email ID is yourname@yourcompanyname.com you should enter this.
1. Email Server. This is the URL of your mail server or the email service that you have purchased. For example, it may be mail.yourcompany.com or imap.yourcompany.com.
1. Use IMAP. IMAP and POP are two services used by most mail servers for incoming emails. If your Email server allows IMAP service for the incoming emails keep this checked. Otherwise, leave this unchecked.

1. Use SSL. If your mail server uses SSL (Secure Socket Layer) communication keep this checked.

 **Do I have SSL?:** You may have purchased SSL certificate from your IT service provider for SSL and they may have set up SSL for your mail server. If you're using 'https' while accessing mail server over browser then you might have SSL setup.

1. Use SSL for Outgoing. If your mailserver uses SSL for outgoing, enable this to explicitly use SSL for outgoing emails. Defaults to port 465.

1. Append Outgoing Email to Sent Folder. If you are not using standard mailservers provided by GMail and similar services, you might need to enable this option to append all outgoing emails to the email account's inbox. (Recommended for email servers like Zimbra and CPanel).

1. Attachment Limit (MB). You can limit the size of file attachments in emails sent from ERPNext.

1. SMTP Server is the outgoing email service address of your email server.

1. Tick Use TLS if your SMTP service supports TLS for security.

1. Default port. SMTP service is usually set on port 25. If your email server is set up on a separate port number you can set that up here.

### 1.1 After saving the domain

Once you click on save, these settings are validated by ERPNext and the Email Domain gets saved. Sometimes this could take a few seconds and you might have to wait. This email domain is then available in a dropdown called Domain in the Email Accounts screen.

[Screenshot on the live page: Email domain in email account]

#### Entered everything but still unable to setup Email Domain?

If you've entered and verified the above settings and are still unable to setup Email Domain, you can contact ERPNext support within your account for help.

### 2. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email-dropbox.md -->
---
title: "Email Dropbox\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-dropbox"
updated: "2026-03-02"
---


When you receive emails from Leads, Customers, Suppliers, or other business partners, you might wish to attach those to their relevant records in ERPNext. One way to do so is to save the email and upload it as an attachment. However, this could turn into a cumbersome process. ERPNext offers a better way to handle this through its "Email Dropbox" feature.

When enabled, each record in ERPNext will have it's own unique email address to which you can forward emails. You can click on the email address to copy it to your clipboard, which can then be added to the "To", "Cc", or "Bcc" field of the email that you wish to send.

## 1. Enable Email Dropbox Feature

In [Email Account](/erpnext/email-account), check 'Enable Email Dropbox'.

[Screenshot on the live page: Enable Email Dropbox]

## 2. Copy Unique Email Address in Any Record

Once the Email Dropbox feature is enabled, the unique email address becomes visible in all the records. You can click on the same and the address is copied to your clipboard. You can directly paste it in 'To', 'Cc' or 'Bcc' and send the email.

[Screenshot on the live page: Unique Email Address]

## 3. Email in Timeline

Once the email is received, ERPNext attaches it to the appropriate record and it will be visible in that record's timeline.

[Screenshot on the live page: Email in Timeline]

### Related Topics
1. [Email Domain](/erpnext/email-domain)
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email-error.md -->
---
title: "Email Error in Sending or Receiving\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-error"
updated: "2026-03-04"
---


In ERPNext, you can customize the Incoming and Outgoing Email Gateway. On saving an Email Account, ERPNext tries establishing a connection with your email gateway. If your ERPNext account is able to connect fine, then Email Account is saved successfully. If not, then you might receive an error as below.

[Screenshot on the live page: Email Error]

This indicates that using login credentials and other email gateway details provided in the Email Account, ERPNext is not able to connect to your email server. Please ensure that you have entered valid email credentials for your Email Gateway. Once you have configured Email Account successfully, you should be able to send and receive emails from your ERPNext account fine.

Note: Your ERPNext account is connected with an ERPNext email server by default. If you don't want to use your own email server, you can continue sending emails using ERPNext email server, without any configuration required in the Email Account.

<!-- page: erpnext/erpnext__email-inbox.md -->
---
title: "Email Inbox\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-inbox"
updated: "2026-03-02"
---


**Once an email account is added, the email inbox will be accessible.**

Running a business involves many transactional email exchanges with parties like Customers and Suppliers and other members within the company. Email Inbox feature allows you to pull all your business emails into your ERPNext account. Enabling access to business emails with other transactional details makes ERPNext a single platform for accessing all business information in one place.

In ERPNext, you can configure Email Inbox for each System User. Following are the detailed steps to configure Email Inbox for a User.

## 1. Create a User

You can configure an Email Inbox for a System User only. Hence ensure that you have added yourself and your colleagues as a User and assigned them required permissions.

To know how to add a new User, go to the [User page](/erpnext/adding-users).

## 2. Create an Email Domain

Email Domain for the following Services is available out-of-the-box and you can directly proceed to create an [Email Account](/erpnext/email-account). Know more about creating an Email Domain [here](/erpnext/email-domain).

* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* **Outlook.com**
* **Yandex.mail**

[Screenshot on the live page: Email Service]

To be able to send and receive emails into your ERPNext account from other email services (like WebMail or Gmail), you should set up an Email Domain master. In this master, email gateway details like SMTP Address, Port No., IMAP/POP3 address details are captured. If you have ever configured a local email client (like Outlook), Email Domain master requires details to be fed similarly.

To add new Email Domain, go to:

> Home > Settings > Emails > Email Domain > New

[Screenshot on the live page: Email Domain]

Know more about Email Domains [here](/erpnext/email-domain). Once you have configured an Email Domain for your Email Service, it will be used for creating Email Accounts for all the Users in your ERPNext account.

## 3. Email Account

Create an Email Account based on the Email ID of the User. For each User whose email account is to be integrated with ERPNext, an Email Account master should be created for it.

If you are creating an Email Account for your colleague who's Email Password is unknown to you, then check field "Awaiting Password". As per this setting, a User (for whom Email Account is created) will get a prompt to enter email password when accessing his/her ERPNext Account.

[Screenshot on the live page: Email Password]

> If you are creating an Email Account for Email Inbox of a User, then leave Append To field as blank.

Read [Email Account documentation](/erpnext/email-account) for more details on how to setup.

## 4. Linking Email Account in the User master

Once an Email Account is created for a User, select that Email Account in the User. This will ensure that emails pulled from the said Email ID will accessible only to this User in your ERPNext account.

[Screenshot on the live page: Email User Link]

You can link multiple emails with one user.

## 5. Using Email Inbox

If you have correctly configured Email Inbox as instructed above, then on the login of a User, Email Inbox icon will be visible. This will navigate the user to Email Inbox view within the ERPNext account. All the Emails received on that email will be fetched and listed in the Email Inbox view. User will be able to open emails and perform various actions on them.

### 5.1 Folders

In ERPNext, you can link multiple Email Accounts with the single User. To switch to Inbox of a different email account and access other folders like Sent Emails, Spam, Trash, click on Email Inbox option in the left bar.

[Screenshot on the live page: Email Folders]

### 5.2 Actions

On the emails in your inbox, you can take various actions like Reply, Forward, Mark as Spam or Trash.

[Screenshot on the live page: Email Actions]

### 5.3 Relink

You can relink an email to a document like Issue, Lead, Opportunity, etc. based on the context of the email. Select the document type and the document to link the email to.

[Screenshot on the live page: Make from Email]

### 6. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Sending Email](/erpnext/sending-email)
1. [Email Domain](/erpnext/email-domain)

<!-- page: erpnext/erpnext__email-template.md -->
---
title: "Email Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email-template"
updated: "2026-03-02"
---


Every email sent is different but certain emails can be standardized, usually known as Email Template or Standard Reply.

To access the Email Template list, go to:
> Home > Settings > Email > Email Template

## 1. How to create an Email Template
1. Go to the Email Template list, click on New.
1. Enter a name for this Email Template.
1. Enter a Subject for this Email Template.
1. Response is the standard content of the email that will be a part of this template.
1. Save.

[Screenshot on the live page: Email Template]

**DocType Associated:** (optional) The DocType associated with this template.

### 1.1 How to use Email Template
You can use this Email Template in the Emails that are sent from ERPNext in the "CC, BCC & Email Template" field of the email section of the document. ERPNext will fetch the subject and response as per the template selected.

You can set a Default Email Template for each document type via [Customize Form](/erpnext/customize-form).

### 1.2 How to get fieldnames
The fieldnames you can use in your email template are the fields in the document from which you are sending the email. You can find out the fields of any documents via [Customize Form](/erpnext/customize-form) and selecting the document type (e.g. Sales Order)

### 1.3 Using HTML to build the template

There's a `Use HTML` check that you can toggle to switch from the text editor to a code editor. This allows finer control over the body of the email and makes it easier to use for features like loops in Jinja.

### 1.4 Templating
Templates are compiled using the Jinja. To learn more about Jinja, [visit this page](https://jinja.palletsprojects.com/en/2.10.x/).

## 2. Related Topics
1. [Email Account](/erpnext/email-account)
1. [Email Inbox](/erpnext/email-inbox)

<!-- page: erpnext/erpnext__email.md -->
---
title: "Email Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email"
updated: "2026-03-02"
---

There is a process for configuring email in ERPNext that can greatly enhance communication and productivity within the system. By configuring your email settings, you can seamlessly send and receive emails directly from ERPNext which allows efficient correspondence with clients, suppliers, and team members in order to maintain transparency.

Additionally, the users can personalise email templates, set up auto-replies, and schedule email notifications, enhancing productivity and streamlining communication workflows within the ERP system.

- [Email Domain](/erpnext/user/manual/en/email-domain)
- [Email Account](/erpnext/user/manual/en/email-account)
- [Email Template](/erpnext/user/manual/en/email-template)
- [Email Digest](/erpnext/user/manual/en/email-digest)
- [Newsletter](/erpnext/user/manual/en/newsletter)
- [Notification](/erpnext/user/manual/en/notifications)
- [Auto Email Report](/erpnext/user/manual/en/auto-email-reports)
- [Sending email from documents](/erpnext/user/manual/en/sending-email)
- [Linking email to documents](/erpnext/user/manual/en/linking-emails-to-document)

<!-- page: erpnext/erpnext__email_group.md -->
---
title: "Email Group | ERPNext Documentation"
description: "Learn how to create and manage Email Groups and subscribers for ERPNext newsletters and campaigns."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/email_group"
updated: "2026-07-23"
---

**An Email Group is a list of subscriber email IDs to which you send newsletters.**

You can manage subscribers by grouping them into different groups.

You can group existing and potential customers into different groups based on their territory or products they are interested in. You can group the email ID of all employees so that you can share information with them.

To access the Email Group list, go to:

> Home > Settings > Email > Email Group

## How to Create an Email Group

- Go to the Email Group list and select New.
- Enter 'Title'.
- select 'Save'
- select Action > Add Subscribers.
- Enter Email Addresses.
- select 'Add'

## Features

### Import Email IDs from Transactions

You can import email IDs from existing transactions.

select Action > Import Subscribers and select a transaction like Lead. select Import and all the email IDs mentioned in the email IDs will be imported.

### Email Templates

You can specify the confirmation email and welcome email template for the email group. A confirmation email will be sent to confirm a person's subscription to your newsletter. The welcome email is sent when the person confirms their subscription to your email newsletter.

**Confirmation Email Template:** This email template is used to replace the default template sent for newsletter subscription. The confirmation email generated via this template is sent when someone subscribes to the Email Group Website.  
**Welcome Email Template:** Whenever a subscriber is added to an email group after confirmation, the email template set here will be sent to them.

[Screenshot on the live page: Email Group Templates]

<!-- page: erpnext/erpnext__energy-point-system.md -->
---
title: "Energy Point System"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/energy-point-system"
updated: "2026-05-28"
---

**Energy Points System is a gamification of user engagement to recognize and incentivize users for their contributions and activities within ERPNext.**

 

This system can be used to track the performance of each user.

 

> To enable Energy Point System go to
>
> **Energy Point Settings** > **Enabled**

 

## How to use the Energy Point System?

---

 To start using this system you need to create some Energy Point Rules (see section 3. How to create Energy Point Rules?) so that users can get energy points based on their activities.

## What are Energy Point Rules?

---

Energy Point Rules store the information about the activity and the value of points to be allocated.

 

Energy Point Rule has the following fields: 


| Field                          | Description                                                                                                                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reference DocType              | Document Type you want to apply the rule on eg. Task, ToDo, Issue, etc.                                                                                                                                                       |
| For Document Event             | Options: Save, Submit, Cancel, and Custom.**Note:** If "Custom" option is selected then the "Conditions" field becomes mandatory                                                                                              |
| Points                         | Points to be allocated.                                                                                                                                                                                                       |
| Allot Points To Assigned Users | If checked, users assigned to the reference document will get respective points. eg. If users Santosh and Albert are assigned to a particular task then both of them will get points when the document fulfills the condition |
| User Field                     | Field from which user will be selected eg. `Resolved By`, `Modified By`, `Owner`, etc. can be used. If `Modified By` is selected, the last person to satisfy the doc condition will get the points.                           |
| Multiplier Field               | Field which stores value for the multiplier. This field can take numeric and decimal values which will be multiplied with points defined in the rule. For example: 2 (multiplier) * 10 (points set in the rule) = 20 points   |
| Condition                      | Condition for the point allocation. eg. `doc.status == 'Closed'`The above condition will check whether the `status` field in the document is 'Closed' and if yes then the points will be allocated to the user.               |
| Apply Only Once                | The rule will be applied only once per document.                                                                                                                                                                              |
|                                |                                                                                                                                                                                                                               |


 

## How to create Energy Point Rules? 

---

 Search for **Energy Point Rule** > create new Energy Point Rule

 

Take a look at the following example rule:  

[Screenshot on the live page]

The screenshot above is the rule for **Issue Closing**. So when any user closes the issue he/she will be rewarded with **10** points.

 

Other cases can be covered similarly.

 

Suppose, you want to create a rule where a user gets points on completing a task, you can do so by creating following rule   

[Screenshot on the live page]

## Features 

---

### 4.1 Auto Point allocation

Based on energy point rules created, users will automatically get points when they complete activities which are tracked using the Energy Point System. 

### 4.2 Review System

Review system can be used to "Appreciate" or "Criticize" someone's work, check out the following GIF for the review process.

[Screenshot on the live page]

   

For reviewing, the user needs to have review points which can be assigned by System Manager through **Energy Point Settings**.

 

You can also setup auto review point allocation from 'Energy Point Settings':   

[Screenshot on the live page]

### 4.3 Leaderboard

> Go to Social Home > Leaderboard (side navigation bar)

The leaderboard shows the user's standing in the organization.

[Screenshot on the live page]

### 5. Related Topics

1. [Milestone Tracking](/erpnext/milestone-tracker)
