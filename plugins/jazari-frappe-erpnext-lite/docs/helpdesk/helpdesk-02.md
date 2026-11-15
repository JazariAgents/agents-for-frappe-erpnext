<!-- Frappe documentation: helpdesk, part 2 of 4. Index: docs/INDEX.md -->

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
