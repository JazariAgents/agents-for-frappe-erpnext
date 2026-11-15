<!-- Frappe documentation: erpnext, part 24 of 69. Index: docs/INDEX.md -->

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

![Defining Criteria](/files/email-account-list.png)  


### 3.2 Incoming Email Accounts

To set up an incoming Email Account, check on **Enable Incoming** and set your POP3 settings, if you are using a popular email service, these will be preset for you.

![Incoming EMail](/files/email-account-incoming.png)  


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

![Outgoing EMail](/files/email-account-sending.png)  


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
- Save[Email Campaign](/files/email-campaign.png)

he above Email Campaign is for the following Campaign:

[Campaign Schedule](/files/campaign-email-schedule.png)

*Note**: The **Send After (days)** field in Campaign specifies the day on which email is to be sent relative to the **Start Date** of **Email Campaign**. Notice the 'End Date' in the above Email Campaign. It is '26-07-2019', which is 4 days after the 'Start Date', '22-07-2029', as the Campaign Schedule ends on day 4.

### Create multiple Email Campaigns for a Campaign

You can also create new Email Campaigns for different Leads or Contacts for the same Campaign though the Campaign Dashboard.

- Go to the Campaign for which you want to create Email Campaigns.
- select + in front of Email Campaigns to create a new Email Campaign for the Campaign.[Email Campaigns from Dashboard](/files/campaign-dashboard.png)

## Features

### Linked Communication

When emails are sent to the respective leads or contacts, Communication is linked to the Email Campaign document. You can view all the emails sent in your document.

![Linked Communication](/files/email-campaign-linked-comm.png)

### Unsubscribe from Email Campaign

If a lead or contact does not want to continue getting emails regarding the campaign, he or she can unsubscribe from the Email Campaign via the unsubscribe link sent with the email.

![Unsubscribe Link](/files/unsubscribe-link.png)

When the lead or contact unsubscribes, the status of the Email Campaign document changes to 'Unsubscribed'.

![Unsubscribed](/files/email-campaign-unsubscribed.png)

### Use Lead or Contact fields in Email Template

 The Email Template has the context of the document you have specified in the 'Email Campaign For' field. If you want to display the fields from your Lead or Contact document in your Email Template you will have to use doc.fieldname for the same.  
 For example, if 'Email Campaign For' is 'Contact', you can mention the 'first name' of your Contact as doc.first_name in the Email Template as shown below:

![Email Template Document](/files/email-template-doc.png)

Then the emails sent would look like this:

![Email Campaign Doc Data](/files/email-campaign-doc-data.png)

### Status indication

Status indicates the state of the Email Campaign, the various Statuses are:

- **Scheduled**: When the Email Campaign has not yet started but scheduled on a future 'Start Date'.
- **In Progress**: The campaign would be marked as 'In Progress' between 'Start Date' and 'End Date' of the campaign.
- **Completed**: After the 'End Date' of the campaign, the status will be changed to 'Completed'.
- **Unsubscribed**: When the Lead or Contact unsubscribes from the Campaign.

![Email Campaign Status](/files/email-campaign-status.png)

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

![Email Digest](/files/email-digest.png)

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

![Email Domain](/files/email-domain.png)

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

![Email domain in email account](/files/email-domain1.png)

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

![Enable Email Dropbox](/files/enable_email_dropbox.png)

## 2. Copy Unique Email Address in Any Record

Once the Email Dropbox feature is enabled, the unique email address becomes visible in all the records. You can click on the same and the address is copied to your clipboard. You can directly paste it in 'To', 'Cc' or 'Bcc' and send the email.

![Unique Email Address](/files/unique_email_address_dropbox.png)

## 3. Email in Timeline

Once the email is received, ERPNext attaches it to the appropriate record and it will be visible in that record's timeline.

![Email in Timeline](/files/email_in_timeline.png)

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

![Email Error](/files/email-error.png)

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

![Email Service](/files/email-service.png)

To be able to send and receive emails into your ERPNext account from other email services (like WebMail or Gmail), you should set up an Email Domain master. In this master, email gateway details like SMTP Address, Port No., IMAP/POP3 address details are captured. If you have ever configured a local email client (like Outlook), Email Domain master requires details to be fed similarly.

To add new Email Domain, go to:

> Home > Settings > Emails > Email Domain > New

![Email Domain](/files/email-domain.png)

Know more about Email Domains [here](/erpnext/email-domain). Once you have configured an Email Domain for your Email Service, it will be used for creating Email Accounts for all the Users in your ERPNext account.

## 3. Email Account

Create an Email Account based on the Email ID of the User. For each User whose email account is to be integrated with ERPNext, an Email Account master should be created for it.

If you are creating an Email Account for your colleague who's Email Password is unknown to you, then check field "Awaiting Password". As per this setting, a User (for whom Email Account is created) will get a prompt to enter email password when accessing his/her ERPNext Account.

![Email Password](/files/email-password.png)

> If you are creating an Email Account for Email Inbox of a User, then leave Append To field as blank.

Read [Email Account documentation](/erpnext/email-account) for more details on how to setup.

## 4. Linking Email Account in the User master

Once an Email Account is created for a User, select that Email Account in the User. This will ensure that emails pulled from the said Email ID will accessible only to this User in your ERPNext account.

![Email User Link](/files/email-user-link.png)

You can link multiple emails with one user.

## 5. Using Email Inbox

If you have correctly configured Email Inbox as instructed above, then on the login of a User, Email Inbox icon will be visible. This will navigate the user to Email Inbox view within the ERPNext account. All the Emails received on that email will be fetched and listed in the Email Inbox view. User will be able to open emails and perform various actions on them.

### 5.1 Folders

In ERPNext, you can link multiple Email Accounts with the single User. To switch to Inbox of a different email account and access other folders like Sent Emails, Spam, Trash, click on Email Inbox option in the left bar.

![Email Folders](/files/email-folders.png)

### 5.2 Actions

On the emails in your inbox, you can take various actions like Reply, Forward, Mark as Spam or Trash.

![Email Actions](/files/email-actions.png)

### 5.3 Relink

You can relink an email to a document like Issue, Lead, Opportunity, etc. based on the context of the email. Select the document type and the document to link the email to.

![Make from Email](/files/make-from-email.png)

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

![Email Template](/files/email-template-example.png)

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

![Email Group Templates](/files/email-group.png)

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

![](/files/image13b0d0.png)

The screenshot above is the rule for **Issue Closing**. So when any user closes the issue he/she will be rewarded with **10** points.

 

Other cases can be covered similarly.

 

Suppose, you want to create a rule where a user gets points on completing a task, you can do so by creating following rule   

![](/files/image1d19dd.png)

## Features 

---

### 4.1 Auto Point allocation

Based on energy point rules created, users will automatically get points when they complete activities which are tracked using the Energy Point System. 

### 4.2 Review System

Review system can be used to "Appreciate" or "Criticize" someone's work, check out the following GIF for the review process.

![](/files/review-system.gif)

   

For reviewing, the user needs to have review points which can be assigned by System Manager through **Energy Point Settings**.

 

You can also setup auto review point allocation from 'Energy Point Settings':   

![](/files/imaged9995e.png)

### 4.3 Leaderboard

> Go to Social Home > Leaderboard (side navigation bar)

The leaderboard shows the user's standing in the organization.

![](/files/leaderboard.png)

### 5. Related Topics

1. [Milestone Tracking](/erpnext/milestone-tracker)

<!-- page: erpnext/erpnext__erpnext-chat-with-raven.md -->
---
title: "ERPNext Chat with Raven"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext-chat-with-raven"
updated: "2026-07-05"
---

ERPNext Chat is deprecated and should not be used for new implementations. If your organization needs instant messaging, team channels, document sharing, and collaboration inside the Frappe ecosystem, use **Raven** instead.

Raven is a Frappe app for team messaging. It works as an open-source Slack alternative and can be installed on the same site as ERPNext and other Frappe apps. This makes it a good option for organizations that want internal communication to stay close to their business data and workflows.

## Why Use Raven

Raven helps teams communicate in real time without leaving the Frappe ecosystem. Teams can create channels, send direct messages, share files, mention users, react to messages, and search conversations.

It is especially useful for organizations using ERPNext because discussion can happen around actual work: customers, sales orders, invoices, issues, projects, tasks, and other business documents.

## Key Features

- **Channels and direct messages:** Create public or private channels for teams, departments, projects, or topics.
- **Rich messaging:** Send formatted messages, links, code blocks, emojis, mentions, replies, and reactions.
- **File sharing:** Share images, documents, PDFs, and other files directly in conversations.
- **Search:** Search messages, channels, files, and users.
- **Mobile-friendly:** Raven is designed for collaboration on desktop and mobile.
- **Dark mode:** Users can choose a comfortable interface for daily communication.

## ERPNext And Frappe Native Features

Raven is more than a standalone chat tool. Since it is built on Frappe, it can work closely with ERPNext and other Frappe apps.

Useful ERPNext-native capabilities include:

- Share ERPNext documents in Raven conversations.
- Send messages to channels from the Desk interface.
- Link messages to documents so the discussion context is available from the document timeline.
- Trigger notifications based on document events.
- Use document previews when sharing ERPNext records.
- Perform workflow-related actions from conversations where supported.
- Keep collaboration connected to business records instead of scattered across external chat tools.

This makes Raven useful for teams that want conversations to remain connected to actual ERPNext work instead of living separately in another system.

## When To Use Raven

Use Raven when your organization needs:

- Internal team messaging.
- Department or project channels.
- ERPNext-related discussions around documents and transactions.
- A Frappe-native alternative to Slack.
- A self-hostable or Frappe Cloud-hosted communication tool.
- Better context between chat, documents, and workflows.

## Installation And Source Code

You can install Raven from the Frappe Cloud Marketplace:

- [Raven on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/raven)

The source code is available on GitHub:

- [Raven GitHub Repository](https://github.com/The-Commit-Company/raven)

## Related Topics

- [ERPNext](https://docs.frappe.io/erpnext)
- [Frappe Framework](https://docs.frappe.io/framework)
- [Raven on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/raven)
- [Raven GitHub Repository](https://github.com/The-Commit-Company/raven)
