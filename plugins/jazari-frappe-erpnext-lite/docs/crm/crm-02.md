<!-- Frappe documentation: crm, part 2 of 3. Index: docs/INDEX.md -->

<!-- page: crm/crm__email-template.md -->
---
title: "Email Template"
space: "CRM"
url: "https://docs.frappe.io/crm/email-template"
updated: "2026-04-23"
---

Email Templates is a time-saving tool that lets you create reusable email drafts (such as introductions, follow-ups, or proposals) you frequently send to your leads and deals. With the ability to utilize Jinja templates, you can personalize emails to cater to specific recipients or contexts. 

## Create a new Email Template

To create a new email template, go to **Settings > Templates.** Click on Create, and add the:

- **Name:** A label to identify the template in your list
- **Subject:** The email subject line (Jinja variables supported)
- **For:** Whether it is for a lead or a deal
- **Content Type:** You can select how you want to format the template. There are two options: Rich Text and HTML

![](/files/image8cee4e.png)

Only "Enabled" Email Templates will be visible for further use. There is a toggle option against every template.

## Using the Email Template

You can use the Email Templates you have created in Lead and/or Deal while composing your emails by clicking on the Email Template button. When you click on Reply to compose an email, the email template button appears.

For example, as seen in the screenshot, the email template "First response to deals" is selected.

![](/files/image6ca4dd.png)

The email content is then copied, and you are free to edit the content as well to personalize it further.

![](/files/image422097.png)

<!-- page: crm/crm__erpnext.md -->
---
title: "ERPNext"
space: "CRM"
url: "https://docs.frappe.io/crm/erpnext"
updated: "2026-06-25"
---

Frappe CRM, while a standalone application, offers seamless integration with ERPNext to streamline your business processes. This integration allows you to create quotations and customers directly from deals within Frappe CRM, enhancing efficiency and reducing manual data entry.

## ERPNext Setup

Both Frappe CRM and ERPNext are installed on the same site  

![](/files/image0391fb.webp)

1. Navigate to **Settings** -> **ERPNext** -> **Enable** -> Set **Company**.
2. Create **Customer** when status change -> Set **Deal Status (Optional)**

## What gets synced

Once the integration is enabled, data flows between Frappe CRM and ERPNext as described below. Most syncing runs only when both apps are on the same site; differences for separate-site setups are called out where they apply.

### Customers

- The Customer is named after the Deal's organization (Customer Type **Company**) or after the primary contact / lead name when there is no organization (Customer Type **Individual**).
- The Deal's contacts and organization address are carried over to the new Customer.
- Territory, currency, industry and website are copied from the Deal. Territory and industry are dropped automatically if they don't exist in ERPNext.

**Two Ways:**

1. Upon marking a Deal as "Won" (or a specified status, configurable in ERPNext settings), a new customer will be created in your ERPNext instance. The Deal's contacts and organization address will be automatically linked to this newly created customer.
  ![Screenshot 2024-09-18 at 8.45.09 PM](https://docs.frappe.io/files/Screenshot%202024-09-18%20at%208.45.09%E2%80%AFPM.png)
  ![Screenshot 2024-09-18 at 9.07.32 PM](https://docs.frappe.io/files/Screenshot%202024-09-18%20at%209.07.32%E2%80%AFPM.png)
2. When a Sales Order is create in ERPNext from a Deal's Quotation.
  he Create Quotation button on a Deal opens a new Quotation in ERPNext with the Deal's data pre-filled:

- The quotation is raised against the Customer if one already exists otherwise against the CRM Deal itself. (ERPNext's Quotation To field is extended to allow Customer, Lead, Prospect and CRM Deal.)
- The Deal's primary contact and organization address are attached.
- Quotation line items are pre-filled from the Deal's products ie item code, quantity, rate and discount for every Deal product that is linked to an ERPNext Item.

The typical Deal to Sales Order flow looks like: 

![](/files/create quotation.webp)
*Create Quotation*

Quotation line items are pre-filled from the deal's products

![](/files/image9b795a.webp)
*New Quotation*

![](/files/Sales Order1eb7d4.webp)

Once the customer is created, you'll find a "View Customer" button on the deal header, allowing you to easily access the customer from deal page.

![Screenshot 2024-09-18 at 8.43.34 PM](/files/Screenshot 2024-09-18 at 8.43.34 PM.png)

### CRM Product and ERPNext Item

ERPNext Items and CRM Products are kept in sync with ERPNext as the source of truth. This sync runs on the same site only.

![](/files/sync.webp)

- Creating an Item in ERPNext automatically creates a matching CRM Product and links the two records.
- Updating an Item auto updates its CRM Product. The synced fields are: item name, rate, image, disabled status and description.
- Renaming an Item renames its CRM Product (and vice-versa) keeping both sides aligned.
- Deleting an Item deletes its linked CRM Product and deleting a CRM Product deletes its linked Item.

### Pricing

  Product rates shown in the CRM follow ERPNext's pricing rather than a static value:

- A CRM Product's rate is taken from its ERPNext Item Price in the selling price list falling back to the Item's standard rate when no Item Price exists.
- On a Deal, each product line is priced the way ERPNext prices a quotation line: the price list is derived from the Deal's customer (or the default selling price list when there is none), and the rate is looked up for the item's UOM. If no Item Price is found, the CRM Product's standard rate is used as a fallback.  
This means a customer specific price list configured in ERPNext surfaces its negotiated rates directly on the Deal.

## Customizations

The **Create Quotation** and **View Custome**r buttons on the Deal page are rendered by a standard CRM Form Script named Create Quotation from CRM Deal. It is created automatically when you enable the integration and is bound to the CRM Deal form view.

### How the script works

  On load, the script checks whether the integration is enabled and if so, it adds the actions to the Deal header:

- **Create Quotation** calls the backend to build the pre-filled quotation URL and opens it n a new tab.
- **View Customer** shown only when the Deal already has a linked ERPNext Customer. opens the Customer record in a new tab.

![](/files/imageec1372.webp)
*Form Script*

### Editing the script

Because it is a standard script, Create Quotation from CRM Deal is read-only and cannot be edited in place. This protects it from being overwritten. 

To customize the behavior:

1. Go to Desk → CRM Form Script.
2. Disable the Create Quotation from CRM Deal script.
3. Duplicate it (or create a new script on the CRM Deal form view) and make your changes there. for example: changing the conditions under which the buttons appear. Add new actions or adjust labels.
4. Enable your copy.

Your custom script then renders the buttons in place of the standard one.

**Example Script:**

```
class CRMDeal {
        onLoad() {
                if (this.doc.__newDocument) return
                call(
                        "frappe.client.get_single_value",
                        {
                                doctype: "ERPNext CRM Settings",
                                field: "enabled"
                        }
                ).then((enabled) => {
                        if (enabled) this.doc.trigger('setActions')
                })
        }
        setActions() {
                // Only offer quotation creation for qualified-or-later deals
                const allowed = ["Qualification", "Proposal/Quotation", "Negotiation"]
                if (allowed.includes(this.doc.status)) {
                        this.actions.push({
                                label: __("Create Quotation"),
                                onClick: () => {
                                        call(
                                                "crm.fcrm.doctype.erpnext_crm_settings.erpnext"
                                                {
                                                        crm_deal: this.doc.name,
                                                        organization: this.doc.organization
                                                }
                                        ).then((quotation_url) => {
                                                if (quotation_url) {
                                                        window.open(quotation_url, '_blank')
                                                } else {
                                                        toast.error("Error while creating quotation")
                                                }
                                        }).catch((e) => {
                                                toast.error(e.messages[0] || "Error while creating")
                                        });
                                }
                        })
                }
     // A custom action unrelated to the integration
            this.actions.push({
                    label: __("Copy Deal Link"),
                    onClick: () => {
                            navigator.clipboard.writeText(window.location.href);
                            toast.success(__("Deal link copied"));
                    }
            })
    }
}
```

<!-- page: crm/crm__exotel.md -->
---
title: "Exotel\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "CRM"
url: "https://docs.frappe.io/crm/exotel"
updated: "2026-02-05"
---

Exotel is a cloud telephony platform that enables businesses to manage voice calls, SMS, and communication workflows without traditional phone hardware. The integration with Frappe CRM combines these communication capabilities with customer relationship management to provide a unified system for handling customer interactions.

Make call
-----------

* **Lead page:** A call button is available in the right section above lead details. Use this button to initiate a call, but ensure the **Mobile No** field in the **Person** section includes the country code.
    ![](/files/PBAkpiy.png)
* **Deal page:** In the **Contacts** section on the right side. You can add multiple contacts and designate a primary contact. The call button will utilize the primary contact's number.  
    ![](/files/LKceTy6066660.png)
* **Contact page:** Directly initiate a call by clicking the **Mobile No** displayed below the contact's name.  
    ![](/files/9YnXfPgc03eb0.png)

> Make sure to complete your KYC on Exotel before making calls [docs](https://support.exotel.com/support/solutions/articles/110606-trial-accounts-how-do-i-test-outbound-calling-)

Call pop-up
-----------

Upon making or receiving a call, a pop-up window appears displaying:

* Caller name
* Mobile number
* Call status
* Call duration
* Note button
* Task button
* Lead/Deal button
* Action buttons (Close or Minimize)


![](/files/Screenshot%202025-01-20%20at%206.39.27%E2%80%AFPM607878.png)


This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

![](/files/Screenshot%202025-01-20%20at%206.38.34%E2%80%AFPM.png)


Take notes &amp; task during a call
------------------------

While on a call, you can take notes/task using the note/task button. These notes/task are saved in the Call Log for later viewing and editing.  

<div style="display: flex;">
    <img style="height: 300px;" src="/files/Screenshot%202025-01-20%20at%206.32.05%E2%80%AFPM38cf45.png">
    <img style="height: 300px;" src="/files/Screenshot%202025-01-20%20at%206.30.54%E2%80%AFPM2432c4.png">
</div>

Exotel setup
------------

To configure Exotel for use within the CRM, follow these steps:

1. **Exotel Subscription:** Obtain an active Exotel subscription (refer to Exotel's documentation for details).
2. **Exotel Credentials:** From your Exotel account, retrieve your Account SID, Subdomain, API Key, API Token and Exotel Mobile Number (Exophones).
    ![](/files/Screenshot%202025-01-20%20at%206.51.13%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%206.56.49%E2%80%AFPM.png)
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
    ![](/files/LHGhoZR.png)
4. **Telephony Settings:** Navigate to Telephony Settings and enable Exotel. Add your Account SID, Subdomain, API Key, API Token and set Webhook verify token (it can be anything it will be used later in Exotel incoming call flow configuration). You can also enable call recording at this point.  
    ![](/files/Screenshot%202025-01-20%20at%206.27.24%E2%80%AFPM.png)
5. **Telephony Agent:** Go to Telephony Agent (In Desk) and add users (agents) with Exotel mobile number designated for making calls and also personal number(do not forget to mark one number as primary).

    >  Make sure the email is same in both Telephony Agent and Exotel.

    ![](/files/Screenshot%202025-01-20%20at%206.41.03%E2%80%AFPM.png)


Exotel incoming call flow configuration
------------------------

For your CRM's API to connect with Exotel, perform the following configurations within Exotel:

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
    https://<yoursitename>/api/method/crm.integrations.exotel.handler.handle_request?key=<webhook-verify-token>
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

Once this is done, you should see all new incoming calls on your exotel phone number in the "Call Log" list in your CRM instance.

![](/files/Screenshot%202025-01-20%20at%207.30.13%E2%80%AFPM.png)

<!-- page: crm/crm__general-and-defaults.md -->
---
title: "General and Defaults"
space: "CRM"
url: "https://docs.frappe.io/crm/general-and-defaults"
updated: "2026-04-20"
---

These are system-wide settings that apply across your entire CRM. You'll probably set these once and rarely touch them again. To get here, go to **Settings > General** and **Settings > Defaults**.

## General

These settings control how your CRM behaves when emails and comments come in.

![](/files/Screenshot 2026-04-20 at 5.44.28 PM.png)

- **Update timestamp on new communication** – When someone sends an email or leaves a comment on a lead or deal, this updates the "Last Modified" timestamp on that record. Useful for tracking recent activity across your pipeline. If you don't enable this, then new email activity won't affect the last modified timestamp
- **Mark lead/deal as replied on response** – When a customer replies to your email, the lead or deal is automatically marked as "Replied". Only works if SLA is enabled
- **Reopen lead/deal on new communication** – If a new email comes in on a lead or deal, it automatically sets the status back to "Open". Only works if SLA is enabled

## Defaults

These settings control how numbers, currencies, and dates are displayed across the CRM. Set these to match how your team works.

![](/files/Screenshot 2026-04-20 at 5.45.52 PM.png)

- **Currency** – The default currency for all records. Can be changed on individual records if needed
- **Currency Precision** – How many decimal places to show for currency values
- **Number Format** – How numbers are displayed, for example, with commas and decimal separators
- **Float Precision** – Decimal places for non-currency number fields
- **Date Format** – How dates appear across the CRM, for example, dd-mm-yyyy
- **Time Format** – Whether to show time with or without seconds

<!-- page: crm/crm__home-actions.md -->
---
title: "Home Actions"
space: "CRM"
url: "https://docs.frappe.io/crm/home-actions"
updated: "2026-04-20"
---

When you click on the CRM logo at the top left, a small dropdown appears. By default, it shows things like Apps, Settings, and Log out.

**Home Actions** lets you customize what shows up there. Add links to tools your team uses every day, hide things they don't need, or add separators to keep things organized.

It's a small thing, but it makes a big difference if your team is jumping between tools often.

To get here, go to **Settings > Home Actions**.

![](/files/Screenshot 2026-04-20 at 5.36.42 PM.png)

Each row in the list is one item in the dropdown. You can edit any row to configure:

- **Label** – The name that shows up in the dropdown
- **Type** – Either a Route (a link) or a Separator (a divider line to group things)
- **Route** – The URL or internal path the link points to
- **Icon** – Use a Feather icon name like `settings` or `book-open`, or paste in custom SVG code
- **Open in new window** – Opens the link in a new tab
- **Hidden** – Hides the item from the dropdown without deleting it

Click **Add Row** to add a new link. Hit **Update** when you're done.

<!-- page: crm/crm__introduction.md -->
---
title: "Introduction"
space: "CRM"
url: "https://docs.frappe.io/crm/introduction"
updated: "2026-04-20"
---

## What is Frappe CRM

If you're here, you're probably outgrowing a spreadsheet, paying too much for a CRM that charges per seat, or just overwhelmed by features you never use. We've heard this a lot.

When we built Frappe CRM, we had two things in mind. Keep it simple enough that your sales team actually enjoys using it. And keep it open source, so it's always yours to own and adapt.

Most CRMs are built for enterprise teams with dedicated admins and big budgets. Frappe CRM is built for everyone else – founders tracking their first pipeline, sales managers who want their team focused on selling, and growing businesses that don't want to rethink their tooling every time they hire someone new.

## What it does

Frappe CRM gives you everything a sales team needs to manage their pipeline without the clutter.

- **Leads and Deals** – Track every prospect and opportunity in one place. Add notes, log calls, set tasks, and keep the full context of every relationship right where you need it.
- **Communication** – Send and receive emails directly from a lead or deal. Use templates to move faster. Your team can leave comments and tag each other so nothing falls through the cracks.
- **Views and Reports –** Work on a simple list or a Kanban board, whatever fits how your team thinks. Filter, sort, and save your view. Pin the ones you use every day.
- **Automation** – Set up assignment rules to route leads automatically. Define SLAs so every lead gets followed up on time.
- **Customization** – Add custom fields, statuses, and actions to adapt it as per your workflow.
- **Integrations** – Connect with Twilio, Exotel, Meta, WhatsApp, and ERPNext to extend your CRM. You can also integrate with any third-party app via APIs.

## Is it for me?

Frappe CRM works well if you are:

- A small or mid-sized sales team that wants things simple and easy
- A business that likes to stay in control of its own data
- A team that’s outgrowing spreadsheets (finally 😄)
- Someone tired of per-seat pricing on other CRMs

If you need a highly complex enterprise CRM with deep out-of-the-box integrations, Frappe CRM might feel lightweight. But if you want something your team will actually use, it's worth a try.

## Ready to get started?

Head over to the [Installation page](https://docs.frappe.io/crm/introduction/installation) to get Frappe CRM up and running.

## Learning and Community

Got stuck or want to connect with others using Frappe CRM?

- [Telegram Public Group](https://t.me/frappecrm)
- [Discuss Forum](https://discuss.frappe.io/c/frappe-crm)
- [Website](https://frappe.io/crm)
- [YouTube](https://www.youtube.com/channel/UCn3bV5kx77HsVwtnlCeEi_A)

<!-- page: crm/crm__introduction__installation.md -->
---
title: "Installation"
space: "CRM"
url: "https://docs.frappe.io/crm/introduction/installation"
updated: "2026-04-21"
---

Frappe CRM can be installed in multiple ways, depending on your requirements. You can either use **Frappe Cloud** for a fully managed experience or install CRM on your own server.

The following sections explain each installation method in detail.

---

## Managed Hosting (Frappe Cloud)

You can install Frappe CRM with a single click using **[Frappe Cloud](https://frappecloud.com/crm/signup)**, the managed hosting platform for Frappe applications.

- Sign up [here](https://frappecloud.com/crm/signup) to get started
- Your CRM instance will be ready in a few minutes

If you already have a Frappe Cloud site, you can install Frappe CRM directly from the **[Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/crm)**.

:::tip
Recommendation: We strongly recommend trying Frappe Cloud before opting for self-hosting.
:::





---

## Self Hosting

### Production Setup

Follow these steps to set up Frappe CRM in production:

**Step 1**: Download the easy install script

```
wget https://frappe.io/easy-install.py
```

**Step 2**: Run the deployment command

```
python3 ./easy-install.py deploy \
    --project=crm_prod_setup \
    --email=email.example.com \
    --image=ghcr.io/frappe/crm \
    --version=stable \
    --app=crm \
    --sitename subdomain.domain.tld
```

Replace the following parameters with your values:

- `your_email.example.com`: Your email address
- `subdomain.domain.tld`: Your domain name where CRM will be hosted

The script will set up a production-ready instance of Frappe CRM with all the necessary configurations in about 5 minutes.

:::note
If hosting on a public server, make sure your DNS A record points to your server's IP and if hosting locally, map your domain to 127.0.0.1 in your /etc/hosts file to avoid 404 Page Not Found error.
:::





---

### Development Setup

#### Docker Setup

To run CRM using Docker, ensure the following are installed:

- Docker
- Docker Compose
- Git

Refer to [Docker documentation](https://docs.docker.com/). After that, follow the steps below:

**Step 1**: Create a directory and download the required files

```bash
mkdir frappe-crm
cd frappe-crm

# Download the docker-compose file
wget -O docker-compose.yml https://raw.githubusercontent.com/frappe/crm/develop/docker/docker-compose.yml

# Download the setup script
wget -O init.sh https://raw.githubusercontent.com/frappe/crm/develop/docker/init.sh
```

**Step 2**: Start the containers

```
docker compose up -d
```

**Step 3**: Access the application.

The site [http://crm.localhost:8000/crm](http://crm.localhost:8000/crm) should now be available. The default credentials are:

```
Username: Administrator
Password: admin
```

:::tip
Security note: Recommend changing the default password after login.
:::





#### Local Setup (Bench)

1. [Setup Bench](https://docs.frappe.io/framework/user/en/installation).
2. In the frappe-bench directory, run `bench start` and keep it running.
3. Open a new terminal session and cd into `frappe-bench` directory and run following commands:
  ```
  $ bench get-app crm
  $ bench new-site sitename.localhost --install-app crm
  $ bench browse sitename.localhost --user Administrator
  ```
4. Access the crm page at `sitename.localhost:8000/crm` in your web browser.

**For Frontend Development**

1. Open a new terminal session and cd into `frappe-bench/apps/crm`, and run the following commands:
  ```
  yarn install
  yarn dev

  ```
2. Now, you can access the site on the Vite dev server at `http://sitename.localhost:8080`

**Note:** You'll find all the code related to Frappe CRM's frontend inside `frappe-bench/apps/crm/frontend`

<!-- page: crm/crm__inviting-your-team.md -->
---
title: "Inviting Your Team"
space: "CRM"
url: "https://docs.frappe.io/crm/inviting-your-team"
updated: "2026-04-20"
---

Frappe CRM works best when your whole team is in. Once everyone's set up, you can assign leads, track deals together, and collaborate without things falling through the cracks.

To invite someone, go to **Settings > Invite User**.

![](/files/Screenshot 2026-04-20 at 5.04.48 PM.png)

There are two situations here:

**New users** – People who don't have a Frappe account yet. Add their email, pick a role, and hit **Send Invites**. They'll get an email asking them to set up their account and log in. If you're inviting multiple people at once, just separate their emails with commas.



**Existing site users** – If someone already has an account on your Frappe site (maybe they use another Frappe app like HRMS or Helpdesk), they're not automatically part of the CRM. You can add them directly from **Settings > Users** without sending a new invite. Just add them and assign a role.

![](/files/Screenshot 2026-04-20 at 5.14.42 PM.png)

There are three roles to choose from:

- **Sales User** – Your day-to-day sales reps. They can work on leads and deals assigned to them
- **Manager** – Can see and manage the whole team's leads and deals, not just their own
- **Admin** – Full access. Can configure the CRM, manage users, and change settings

Once someone is in, they'll show up under **Settings > Users**. You can change anyone's role anytime from there.

<!-- page: crm/crm__lead-syncing__meta.md -->
---
title: "Facebook / Instagram"
space: "CRM"
url: "https://docs.frappe.io/crm/lead-syncing/meta"
updated: "2026-03-09"
---

### Prerequisites

Before you begin, you must have atleast one Facebook page and a lead generation form. You can follow [this guide](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/) to obtain an access token for your account.

> Note: This feature is in beta, if you find any bugs, please report [here](https://github.com/frappe/crm).

### Adding a new Lead Sync Source

Open **Settings** from the dropdown menu on top-left corner of the CRM dashboard:

![Settings from Sidebar](/files/CleanShot%202025-11-11%20at%2017.09.58@2x.png)

Click on the **Lead Syncing** tab and then click on the `+ New` button to add a new Source:

![Lead Syncing Settings](/files/CleanShot%202025-11-11%20at%2017.15.57@2x4d3c60.png)

### Configuring Lead Sync Source

Now follow these steps:

1. Select **Facebook** as the source type
2. Give your source a relevant name
3. Select a frequency for scheduled syncing: how frequently the leads should be automatically synced
4. Paste the Access token obtained from Meta

![New Lead Sync Source](/files/CleanShot%202025-11-11%20at%2017.18.55@2x047f4a.png)

Now click **Create**. It will take a few seconds since we are pulling the pages and forms from Facebook. But once it is done, you can select the page and the form from where the leads will be pulled in from:

![Select Page and corresponding form](/files/CleanShot%202025-11-11%20at%2018.00.30@2x.png)

As soon as you select the form, you will see a mapping table:

![CRM Mapping Table](/files/CleanShot%202025-11-11%20at%2018.00.49@2x.png)

This table let's you easily map fields of your Facebook form to fields in Frappe CRM. Apart from this, we also store the Lead ID and Form ID in CRM Lead document. Once you are done configuring the field mapping, click on **Update**, and that is it! Your leads will start syncing in the background in some time.

:::tip
You can use Meta's [Graph API Explorer](https://developers.facebook.com/tools/explorer/) to test your token.
:::





### Sync Now

You can also manually trigger a lead sync by clicking on the **Sync Now** button.

### Failure Logs & Retry

If your leads don't appear in your CRM, go to the **Failure Logs** tab, and check the logs. The failure log contains the reason for failure (e.g. Duplicate), the lead data we received from Facebook, and also error traceback if available:

![Sync Failure Log](/files/CleanShot%202025-11-11%20at%2018.16.07@2xc169ec.png)

You can click on the **Retry Sync** button to retry syncing of this particular lead. 

> Note: A new failure log will get created if a resync fails too.

<!-- page: crm/crm__lead.md -->
---
title: "Lead"
space: "CRM"
url: "https://docs.frappe.io/crm/lead"
updated: "2026-04-20"
---

A lead is someone who has shown interest in your product or service but hasn't become a customer yet. It could be someone who filled out a form on your website, someone you met at an event, or a referral from an existing customer. The lead stage is where you figure out if they're worth pursuing further.

## The Leads List

When you click on Leads in the sidebar, you see all your leads in one place. Each row shows you the key details at a glance – name, organization, status, email, phone, who it's assigned to, and when it was last updated.

You can filter, sort, and search across your leads from here. 

![](/files/image7ce865.png)
*List View*

You can also switch between List and Kanban view depending on how you like to work.

![](/files/imageef81e1.png)
*Kanban View*



To create a new lead, hit **+ Create** in the top right. This is the manual way to create a lead. 

## Capturing Leads

There are a few ways to get leads into Frappe CRM without adding them manually one by one. You can embed a web form on your website, sync leads from Facebook and Instagram ads, bulk import them from Excel/spreadsheets, or write custom scripts to pull leads from other sources.

These are covered in detail in the [Capturing Leads](https://docs.frappe.io/crm/web-form) section.

## Inside a Lead

When you open a lead, everything about that person lives in one place.

![](/files/imagef3ab15.png)

On the right side are the lead's details – their name, email, phone, organization, job title, source, industry, and who owns the lead. You can edit any of these inline. 

On the left is the activity panel, with tabs across the top:

- **Activity** – A full timeline of everything that's happened. Emails, comments, calls, field changes — all in one feed
- **Emails** – Send and receive emails directly from here. No switching tabs
- **Comments** – Leave notes for your team, tag teammates, keep the conversation in context
- **Data** – Additional fields and information about the lead
- **Calls** – Log and view call history
- **Tasks** – Create and track tasks related to this lead
- **Notes** – Freeform notes that don't need to be part of the activity feed
- **Attachments** – Files, documents, anything relevant

## Adding a new Lead Status

At the top, you'll also see the Lead status. Some of these statuses are available out of the box. If you want to add custom statuses, you can add them by going to the Desk view (more details [read here](https://docs.frappe.io/crm/setting-up#frontend-and-backend)) and searching for CRM Lead Status. Add the status of your choice, choose the type, and click on save.

![](/files/imaged07f73.png)
*Adding new CRM Lead Status*

It should then appear as a newly added status in the frontend view too.

![](/files/image9ac94b.png)



You can see who the lead is assigned to, what status it's in, and a **Convert to Deal** button for when you're ready to move them forward.

## Converting a Lead to a Deal

When a lead is qualified and ready to move forward, hit **Convert to Deal**. You'll get the option to create a new Contact and Organization from the lead's details, or link to existing ones if they're already in your CRM. Also, choose the status you want your Deal to be in. 

![](/files/17e1-b1cb-4f43-b6b2-bd435b2f7a64.mp4)





Once converted, the lead becomes a Deal and moves into your sales pipeline.

<!-- page: crm/crm__mobile-app-installation.md -->
---
title: "Mobile App Installation"
space: "CRM"
url: "https://docs.frappe.io/crm/mobile-app-installation"
updated: "2026-02-05"
---

Frappe CRM offers a mobile-friendly interface through a Progressive Web App (PWA). This means you can access all the CRM functionalities directly on your phone.

Supported Devices and Browsers
------------------------------

The Frappe CRM PWA works on most modern smartphones and tablets. Here's a quick note about browser compatibility:

* **Android:** Chrome is recommended for the best experience.
* **iOS:** Safari is recommended.

> NOTE: Firefox currently doesn't support PWA installation without additional plugins.
 

How to Install
--------------

Here's how to install the Frappe CRM mobile app on your phone:

**Open the App URL:**

In your mobile browser (Chrome or Safari), navigate to the following URL, replacing `<sitename>` with your actual Frappe CRM website address:


```
https://<sitename>/crm
```

**Example:**

If your Frappe CRM site address is <https://frappecrm.frappe.cloud>, the mobile app URL would be:


```
https://frappecrm.frappe.cloud/crm
```
Devices
-------

### Android (Chrome)

1. On Android, you will get a prompt to install the app on this URL.
2. If you do not see the prompt, tap on the hamburger menu (three dots), and tap on Install app from the list of options.
3. Tap on Install, and wait for a few seconds.
4. You will then be able to find the Frappe CRM app in your applications. You can login to this app with your site credentials.

    <video controls data-setup="{}" height="auto" preload="auto" style="border-radius: 10px;
 border: 2px solid;" width="300">
<source src="https://docs.frappe.io/files/AndroidPWAInstall.mp4" type="video/mp4">
</video>

1. On iOS, if you're using Safari, tap on the share button shown in the video below.
2. Scroll down the list of options, then tap Add to Home Screen.
3. If you do not see "Add to Home Screen", click on "Edit Actions" and you should find the option.
4. The icon will then appear on your home screen. You can login to this app with your site credentials.

    <video controls data-setup="{}" height="auto" preload="auto" style="border-radius: 10px;
 border: 2px solid;" width="300">
<source src="https://docs.frappe.io/files/IOSPWAInstall.mp4" type="video/mp4">
</video>

**Congratulations! You've successfully installed the Frappe CRM PWA on your mobile device.**

<!-- page: crm/crm__note.md -->
---
title: "Note"
space: "CRM"
url: "https://docs.frappe.io/crm/note"
updated: "2026-04-21"
---

Notes are for capturing anything important about a lead or deal that doesn't fit neatly into a form field. A key thing a prospect mentioned on a call, something to remember before the next meeting, internal context for your team, or anything worth writing down.

## The Notes View

Click on Notes in the sidebar to see all notes across your CRM in one place, shown as cards. Each card shows the title, content, who wrote it, and when. You can filter and search to find what you need.

![](/files/image3d95de.png)
*The Notes View*

Every note is also linked back to the lead or deal it belongs to, so you can jump straight to the record from here.

![](/files/image348688.png)
*Inside a Note - linked to a Lead / Deal*

## Notes inside a Lead or Deal

Each lead and deal has its own Notes tab. Notes created here are tied to that specific record. They won't show up on other leads or deals. To add one, go to the Notes tab and hit **+ New Note**. Give it a title and write whatever you need.



![](/files/imaged9af76.png)
*Notes tab inside a Lead / Deal*

You can edit a note anytime by clicking on it.

## Creating a Note from the Activity tab

You can also create a note directly from the Activity tab inside a lead or deal using the **+ New** button. It'll show up in the Notes tab and in the activity feed.

![](/files/Screen Recording 2026-04-21 at 7.59.36 AM.mov)

<!-- page: crm/crm__notification.md -->
---
title: "Notification"
space: "CRM"
url: "https://docs.frappe.io/crm/notification"
updated: "2026-02-05"
---

Stay informed about important activities within your CRM system using the Notifications feature. This page serves as a central hub for all your CRM-related alerts and updates.

![](/files/4pVP4rV.png)  


Accessing Notifications
-----------------------

1. Locate the **Notifications** option in the sidebar.
2. Click to open the **Notifications Panel**.

Understanding Notifications
---------------------------

The Notifications Panel displays a list of alerts related to your CRM activities. These alerts currently includes:

* Mentions in comment
* Task assignments/unassignment (changing assigned user)
* Lead/Deal assignments/unassignment

Managing Notifications
----------------------

Within the Notifications Panel, you can perform the following actions:

* **Open a Notification:** Click on an individual notification to view the specific comment or activity it refers to. This action will also mark the notification as read.
* **Mark All as Read:** Click the dedicated button at the top of the panel to mark all your current notifications as read.

<!-- page: crm/crm__organization.md -->
---
title: "Organization"
space: "CRM"
url: "https://docs.frappe.io/crm/organization"
updated: "2026-04-21"
---

If you're in B2B sales, you're rarely dealing with just one person at a company. There might be multiple deals happening with the same organization at the same time – a new product, an upsell, a renewal, a cross-sell. Organizations give you a place to track all of it in one view.

## Inside an Organization

When you open an organization, you'll see its details on the left – name, website, territory, industry, number of employees, and address.

On the right, you get two tabs:

- **Deals** – Every deal linked to this organization, with the amount and current status. At a glance, you can see where each opportunity stands
  ![](/files/image02ff87.png)
  *Linked Deals to an Organization - could be a new Deal, Upsell/Cross-sell, Renewal*
- **Contacts** – Everyone at this organization who's in your CRM, with their email and phone
  ![](/files/image36fbcf.png)
  *Multiple stakehoders of an Organization shown as Contacts*



This makes it easy for a sales rep to walk into a conversation fully prepared. They know what's been discussed, what's open, and who else on their team has been talking to this account.

## How Organizations get created

Just like contacts, organizations are created automatically when a lead is created or converted to a deal. You can also create them manually or link an existing organization to a deal during the conversion process. Read about it more [here](https://docs.frappe.io/crm/lead#converting-a-lead-to-a-deal).

<!-- page: crm/crm__pinned-view.md -->
---
title: "Pinned View"
space: "CRM"
url: "https://docs.frappe.io/crm/pinned-view"
updated: "2026-05-21"
---

Pinned Views let you quickly access frequently used saved views directly from the sidebar. You can create custom filters, sorting, and column configurations, save them as views, and pin them for instant access whenever needed.

## How to pin a view

1. Prerequisite: Create a [saved view](https://docs.frappe.io/crm/view). If you already have an existing saved view, go to the next step.
2. Go to the **List** dropdown and navigate to the view you want to pin.
3. Hover over the desired view and click on the three-dot (...) menu.
4. From the menu that appears, select **Pin View**.

![](/files/Screenshot 2026-05-21 at 6.40.20 PM.png)

## Managing pinned views

Once you've pinned a view, it will be displayed in a dedicated "Pinned Views" section within the sidebar. You can access this view with a single click whenever needed.

![](/files/image53f4b2.png)

## Unpinning views

To remove a view from the pinned section and revert it to a regular saved view, follow the same steps mentioned above. Access the three-dot menu for the pinned view and select **Unpin View.**

<!-- page: crm/crm__profile-and-preferences.md -->
---
title: "Profile and Preferences"
space: "CRM"
url: "https://docs.frappe.io/crm/profile-and-preferences"
updated: "2026-04-20"
---

Every user in Frappe CRM has their own profile and preferences. These are personal to you. Changing them won't affect anyone else on your team.

To get here, click your name at the top left of the sidebar and go to **Settings**.

## Profile

This is your personal account page. Keep it up to date, especially if you're communicating with leads and deals directly from the CRM.

![](/files/Screenshot 2026-04-20 at 4.55.23 PM.png)

- **Name** – How you appear to your teammates inside the CRM
- **Email & Signature** – Click Configure to open your Email Settings. Here you can set up two things: 
  - **Signature** – Write your email signature once, and it'll automatically appear at the bottom of every email you send from the CRM
  - **Emails** – If your team has multiple email accounts set up, you can choose which one to send from when composing an email. Useful if you handle both a personal inbox and a shared team inbox like [sales@yourcompany.com](mailto:sales@yourcompany.com)
    ![](/files/Screenshot 2026-04-20 at 4.57.12 PM.png)
- **Password** – Change your password anytime from here.

## Preferences

This is where you make the CRM feel like yours.

- **Theme** – Light, Dark, or System. System follows whatever your OS is set to, so it switches automatically if you use dark mode at night
- **Language** – Change the language of the application. This will be only applicable to your user account, so your sales team is free to pick theirs
- **Timezone** – Set this to your local timezone so dates and times always show up correctly for you

Once you've set this up, you are now set to invite more of your team members to Frappe CRM. Check the next page to learn how to do this.

<!-- page: crm/crm__public-view.md -->
---
title: "Public View"
space: "CRM"
url: "https://docs.frappe.io/crm/public-view"
updated: "2026-05-21"
---

Public Views are [saved views](https://docs.frappe.io/crm/view) that are accessible to every sales user in the system. They function similarly to your personal saved views, but instead of being confined to your workspace, they become a shared resource accessible to everyone.

## When to use public views

Public Views are ideal for situations where a specific filter or layout needs to be consistently used by your entire team. Here are some examples:

- A view that filters leads/deals by a particular source or industry.
- A view that prioritizes high-value deals that require immediate attention.
- A view that displays specific customer information relevant to the sales team.

By creating Public Views for these commonly used scenarios, you can ensure everyone has access to the same information and is working from the same perspective.

## Who can create a public view

Only users with the **Sales Manager and Admin** roles can create Public Views. This helps maintain control over what information is shared publicly within the CRM system.

## Creating a public view

1. Prerequisite: Create a [saved view](https://docs.frappe.io/crm/view). If you already have an existing saved view, go to the next step.
2. Go to the **List** dropdown and navigate to the saved view you want to make public.
3. Hover over the desired view and click on the three-dot (...) menu.
4. From the menu that appears, select **Make Public**.
  ![](/files/image7615eb.png)

This will convert your saved view into a Public View, making it accessible to all users in the sidebar under the **Public Views** section.

## Making a public view private

Public Views can be reverted to private views at any time. Simply follow the same steps mentioned above and select **Make Private** from the three-dot menu.

<!-- page: crm/crm__quick-entry-layout.md -->
---
title: "Quick Entry Layout"
space: "CRM"
url: "https://docs.frappe.io/crm/quick-entry-layout"
updated: "2026-02-05"
---

The Quick Entry Layout Builder allows you to customize the layout of quick entry forms in Frappe CRM, similar to how you can add custom sections and fields to Lead and Deal pages. This gives you more control over the data capture process for different document types.
![](/files/Screenshot%202024-09-28%20at%203.15.58%E2%80%AFPM.png)


Steps
-----

1. **Navigate to Lead/Deal ListView:** Go to Lead/Deal ListView and click on the "Create" to open quick entry modal. Click on the edit button.
    ![](/files/Screenshot%202024-09-28%20at%203.14.48%E2%80%AFPM.png)
2. **Select the Doctype:** A modal will open and doctype will be selected automatically but can still choose the doctype for which you want to add or edit fields in the quick entry form.
3. **Utilize the Quick Entry Layout Builder:** Once you've selected the doctype, the Quick Entry Layout Builder interface for that doctype will appear. This interface provides functionalities for:
	* Adding new sections to the quick entry form.
	* Adding fields within these sections.
	* Dragging and dropping fields to reposition them within sections or between sections.
	* Rearranging sections by dragging and dropping.
	* Editing section labels to provide clear descriptions.
	* and more
4. **Preview Your Work (Optional):** The Quick Entry Layout Builder offers a **Show Preview** button. Clicking this button will display a preview of how the customized quick entry form will look for the chosen doctype. This allows you to visualize your layout changes before saving them.
    ![](/files/Screenshot%202024-09-28%20at%203.15.34%E2%80%AFPM.png)

By following these steps, you can effectively customize quick entry forms in Frappe CRM to better suit your specific data collection requirements for different document types.
