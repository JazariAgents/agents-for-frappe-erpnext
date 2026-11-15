<!-- Frappe documentation: cloud, part 4 of 9. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__faq__site.md -->
---
title: "FAQ - Site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/site"
updated: "2026-06-01"
---

### My site is in **Inactive** state, why is it getting billed?

Both "Active" and "Inactive" sites are billed, you have to drop the site in order to suspend billing.

### My site is suspended, what do I do?

Your site may be suspended for one of the following reasons. Please check your dashboard — a banner will display the reason for suspension :

[Screenshot on the live page]

1. **Unpaid Invoices** : If you have pending invoices, your site will be suspended.
  You can pay them through the **Billing** section in your FC dashboard to restore access.
2. **Trial Ended** : Once your trial period ends, you’ll need to upgrade to a **paid plan** to keep your site active.
3. **Site Usage Exceeds Plan Limits** : Each plan has limits on disk and database usage.
  If your site exceeds these limits continuously for **7 days**, it will be suspended automatically.

To resolve this, you can:

- **Upgrade** to a higher plan that matches your usage.
- **Reduce disk usage** by:
  - Deleting unnecessary files or media.
  - Clearing backups or unused static assets.
- **Reduce database usage** by:
  - Archiving or removing old records.
  - Optimizing queries and database structure.

If your site has been suspended already, you might not access the site to reduce the usage. In that case, you can **upgrade** the site plan and then reduce usage. After reducing usage, you may **downgrade** your plan.

### What is using up all my database size?

You can see which tables/doctypes are using most space within your site itself. Search for **Database storage report** in the search bar and you will find report like follows 

[Screenshot on the live page: Database Storage report]

#### Clearing logs

More often than not, log tables can take up a lot of space. You can control size of log tables with: **Log Settings**

[Screenshot on the live page]

You can safely add additional doctypes such as **Deleted Document** to this list. The system will only let you add supported doctypes to this table. If you attempt to add unsupported doctypes, it will throw an error like so:

[Screenshot on the live page]

To allow deletion for your doctypes within your app, implement the staticmethod within your doctype controller like so 

[Screenshot on the live page]

> Log cleanup happens on daily basis. Please wait for a day for the size change to reflect in your Frappe Cloud dashboard

#### Clearing Comment and Version

It's **NOT RECOMMENDED** to clear these doctypes as they may be used for auditing purposes, but in the case of test sites, you may wish to do so. In such cases, deleting them with `frappe.delete_doc` will be counterintuitive as deleting comment will create another comment saying the comment was deleted (lol). In such cases, deleting them using SQL is probably the easiest way.

> Use your own discretion for the above as the application may misbehave

### What is the difference between Database and Disk space?

When you create data in your site, for e.g., Sales Invoices it will consume database space. When you upload files and images, it will consume disk space.

> You might find database space used on dashboard is higher than your actual database size when you download it on your machine. This is because on Frappecloud it is sum of space consumed by each table and index of each table. Click here to know more about database indexes.


| Space    | Files                  |
| -------- | ---------------------- |
| Database | Database + Indexes     |
| Disk     | Public + Private Files |


### Destination bench group does not have some of the apps installed

If you're updating site on public bench group and you face this error with respect to a marketplace app, it's because we've removed certain Marketplace apps from Public Bench Groups. They are still valid Marketplace apps, but due to technical difficulties and low usage, they were taken off of public bench groups. Please remove the marketplace app if you are not using it or create a Private Bench Group with the required apps and migrate your site to that Private Bench Group using this tool

### Database Size increased after moving site to dedicated server

You may notice that after moving your site to dedicated server, the database usage of the server will seem higher than what used to be the database usage of your site. This is because when we consider database usage for dedicated servers, we consider the storage used by the entire server not just the database. The difference in size is largely due to the binary logs that we collect.

### Row size too large error on migrate

At times, you may see this error upon updating/restoring a site:

```
pymysql.err.OperationalError: (1118, 'Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs')
```

> TL;DR Convert your custom **Data** fields to **Text**

This most often happens in core ERPNext doctypes such as Sales Invoice, Stock Entry, etc. and this happens because of **custom fields**. There's nothing wrong with adding custom fields for your use case, but due to limits placed by **MariaDB,** often times, you'll have to make some changes to the same.

As the error message points out, the way to circumvent this error is to change the datatype to TEXT or BLOB. Now, these are datatypes available in **MariaDB**. In Frappé, these correspond to the following field types:

- Small Text
- Text
- Password
- Attach
- Attach Image

You will want to convert your **varchar** fields into one of the above so that they can be stored in overflow pages in **MariaDB** as we use the DYNAMIC row format.

### Data truncated for column

Sometimes, during migrate you may stumble upon this error:

```
pymysql.err.DataError: (1265, "Data truncated for column 'custom_column_name' at row 1")
```

This happens when you change the datatype of a field in a doctype. Here, the datatype of column was changed to a "smaller" field. Eg: from `Text` to `Data` . Since `Text` can hold more characters than `Data` there can be the case that there is existing data in the Doctype that cannot fit into `Data` field.

In such case, you should write a patch that retains the necessary data from this field or revert the field datatype change altogether.

Alternatively, you can also manually go find and update such data in your site. Though, you'll have to do this for all such sites. It is better to simply write a patch.

### Administrator password not working after restoring site

You can login as administrator to your site directly from your Frappe Cloud dashboard.

[Screenshot on the live page]

If you still wish to obtain the new administrator password set on your site, you may request for the same through our support portal.

### Apps missing after restoring site from backup

You may notice the apps installed in your sites disappear or change after restoring a backup onto the site. This is because restore is a **destructive** operation. Restoring a backup will completely overwrite the database with the contents of the backup. This includes the apps, and the same gets reflected in your Frappe Cloud dashboard.

### Cannot embed site in iframe (blocked by X-Frame-Options)

This should ideally be a feature in the framework itself, but until then you may use the following workaround with a private bench group. You can use the `after_request` hook in `hooks.py` to add a Content-Security-Policy header.

Here’s an example.

```
def after_request(response):
   response.headers.extend({"Content-Security-Policy": "frame-ancestors https://example.com"}) # Replace example.com with the site where you want to embed your frappe.cloud site in
```

As with any other hook, you’ll need to define it in hooks.py of your custom app. E.g:

```
after_request = ["custom_app..after_request"]
```

### CORS error when making API requests

If you try to access endpoints of your FC site from another site (or localhost) you will run into this error. To allow cross-origin requests to your site, you need to set `allow_cors` in your site config to all the sites from which you need to perform the requests.

[Screenshot on the live page]

ref: [https://frappeframework.com/docs/user/en/basics/site_config](https://frappeframework.com/docs/user/en/basics/site_config)

#### Add allow_cors from Site Config tab of your site dashboard

[Screenshot on the live page]

### Scheduler not running in my site

At times, it may seem that the scheduled jobs in your site aren't running at the specified time. This could be due to a lot of things. You can check the status of scheduler within your site by going to **RQ Job** doctype.

> For v13 and lower, you can view **Open** **Background Jobs** page for the same.

If scheduler is running, you'll see status like so

[Screenshot on the live page]

#### Dormant days setting

You should also check **Run Jobs only Daily if Inactive For (Days)** setting within **System Settings** as well. All your scheduled jobs will run once daily regardless of their specified frequency when no user **logs in** to the site in specified number of days.

[Screenshot on the live page]

### Need 4096 bit https certificate

You may need a 4096 bit tls certificate for some custom app integration. For this, you need to, first, get a custom domain. This is because the certificate for the frappe.cloud or erpnext.com domains are 2048 bit and is shared by all the sites.

Once you add a custom domain, you can raise a ticket asking to make the same 4096 bit. You can download the public certificate for sharing purposes as seen in this SO answer.

### Inbound and Outbound IPs

Often, you may need the IP addresses used by your site for whitelisting or blacklisting reasons.

You can get the same from within your site dashboard under the **Overview** tab.

[Screenshot on the live page]

When your site makes a request to an external endpoint, the endpoint sees the **Outbound IP.** This should be used for whitelisting your site's access to some 3rd party service.

**Inbound IP** is what should be used when adding **A** records to some DNS service. As the requests *to* your site go here first.  

Also, We can offer a standalone setup where the connection is direct bypassing the proxy. You can request this to us via the support portal.

### Page Unresponsive

You may obtain an error with a popup with the above title. In this case, it's not an issue with the server, but rather with the client. This most often results due to a memory shortage on the client side; mostly due to some javascript memory leak. To resolve this, you should review your client scripts or the client side code in your custom app.

### How do you get MySQL / MariaDB root password

You don't. You don't need it. If you think you need it to create/delete sites on Frappe Cloud, then you're doing it wrong. You're not supposed to use bench commands to do this. You can use the dashboard to perform these actions.

### Restore dropped site / Site no longer visible

It may be the case that you dropped a site by accident or want to restore an old site. You can do this on your own from your site dashboard by setting the **status** filter to **Archived** to see a list of sites that you've dropped in the past.

> When 2 sites of same name are dropped a numeric suffix is added at the end. So between abc.frappe.cloud and abc.frappe.cloud.1 , the latter will be the recently dropped site.

> If your trial site got dropped, then there is nothing we can do. We don't take backups of trial sites. You will have to start over from a new site.

[Screenshot on the live page]

Clicking on these will essentially allow you to access the **Backups** tab of your site, from where you can **Restore Backup on another Site** easily

[Screenshot on the live page]

### Outgoing requests blocked

Frappe Cloud imposes no restrictions on outgoing requests. You are free to place requests on whichever ports to whatever endpoints you like. If you do face any issues, please check your endpoint server's request logs and see what's the issue there. Perhaps you need to whitelist your Frappe Cloud site's ip

### An error occurred while installing erpnext

ERPNext can only be installed on a fresh site where the setup wizard is not completed. You can reinstall this site (after saving your data) using: bench --site [sitename] reinstall

You can also reset your site's database to **a** clean state and retry installing the ERPNext app.  
To perform this action you can go to your Frappe Cloud site dashboard>Actions>Dangerous Actions>Reset site.

**Note**:- This action will reset your database to a clean state.

### Job taking too long

Sometimes it may seem that a job (most often update site migrate) is taking too long to finish. At this point, it may seem that the job is stuck. In times like this you can have a look at your site's processlist to see what's going on. Often, it is some ALTER query related to some new feature in one of your apps that's taking it's time. Just give it time to finish and you will be fine.

### Change notification email per site

You can change notification email per site from under your **Activity** tab:

[Screenshot on the live page]

### India Compliance credits not correct after restore from backup

After restoring a site from backup, you may notice from your India Compliance account page that the credits shown are not the same as it was on your previous instance. This happens due to a bug. In such case, you can logout and log back in to fix it.

[Screenshot on the live page]

[Screenshot on the live page]

### Allow Changing System Timezone within site

You cannot change timezone under system settings once it's set. However, you may change user timezone under user settings. This will convert time in user's timezone when showing it to the user.

### Increasing the database size availability for shared hosting

Currently, Frappe Cloud does not offer à la carte options. To increase your database capacity, you’ll need to upgrade your site to the next available plan. You can view the pricing here.  
Also you can use the Database Analyzer tool to see which tables/doctypes are using the most space within your site itself. More often than not, log tables can take up a lot of space. You can control the size of log tables with: Log Settings.

[Screenshot on the live page]

### How do I Deactivate my site ?

The deactivate site feature makes the site inactive and inaccessible on the internet. When deactivated the site enters into maintenance mode and the user will still be billed for the site. Please refer to the below screenshot to deactivate your site.

[Screenshot on the live page]

This action is not very dangerous and can be reverted, but please make sure to verify yourself before Deactivating any site on your account.

[Screenshot on the live page]

### I am not able to upload large attachments

By default, the file upload limit is 10Mb which can be overridden by setting the `max_file_size` parameter in the Site Config.

Setting `max_file_size` will still not work if you are using Cloudflare Proxy (Orange Cloud) for your Site's domain because Cloudflare blocks large file uploads for free customers. This can be fixed by turning the proxy / orange cloud off in the Domain Records checkbox.

Please check this reference for more details on cloudflare's rate-limiting.

### Rest site to clean state

From your site dashboard > go to Actions > Dangerous Actions > Reset site.

`Note:- This will reset your site's database to clean state`

[Screenshot on the live page]

<!-- page: cloud/cloud__features.md -->
---
title: "Features"
space: "Cloud"
url: "https://docs.frappe.io/cloud/features"
updated: "2026-05-07"
---

## What can Frappe Cloud do?

- **Multitenancy Made Easy**: Press simplifies multi-tenancy by enabling multiple sites on a single platform, each with its app version, allowing independent updates and minimal downtime, even for large sites.
- **Dashboard**: The dashboard provides a centralized interface to manage apps, servers, sites, billing, backups, and updates, offering real-time insights and streamlined control of complex operations.
- **Permissions**: Granular access controls let team owners manage roles and resources efficiently, ensuring users have access only to relevant information and actions for their roles.
- **Simplified Management**: Press streamlines site management with automated backups, real-time monitoring, role-based access, and easy scaling, making it ideal for growing Frappe environments.
- **Billing**: Automated billing supports daily or monthly subscriptions, flexible payment methods, wallet credits, and ERP integration, simplifying customer invoicing and payments.
- **Marketplace**: The marketplace allows developers to list apps with flexible pricing models, ensures compatibility checks, and provides a streamlined system for sales and payouts.

And a ton more.

---

Watch this video to know more. 

<iframe src="https://www.youtube.com/embed/enrUIePjYP0?si=ThLFWUXJ1CbZy0jv" width="800" height="450" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



---

<!-- page: cloud/cloud__frappe-compute__what-is-this-new-frappe-provider.md -->
---
title: "What is this new 'Frappe' provider?"
space: "Cloud"
url: "https://docs.frappe.io/cloud/frappe-compute/what-is-this-new-frappe-provider"
updated: "2026-05-07"
---

## About
The new Frappe provider is our attempt at decentralisation and ownership over our own infra. Instead of using compute from public cloud companies like AWS, Oracle and Hetzner, we are using our own infrastructure.

## What do you mean by compute?
Frappe Cloud uses virtual machines to create server. A 'server' on Frappe Cloud is anologous with a virtual machine.

## How are you doing this?
We are building our own cloud infrastructure stack in Frappe that runs on rented hardware.

## Can I host my production sites on this?
Not a good idea. While we are in the process of building features like data replication and backups, we do not give any guarantees with respect to uptime and data safety.

<!-- page: cloud/cloud__frappe-insights.md -->
---
title: "Frappe Insights"
space: "Cloud"
url: "https://docs.frappe.io/cloud/frappe-insights"
updated: "2026-04-29"
---


&gt; [Frappe Insights](https://frappe.io/insights) is an easy-to-use, open-source business intelligence tool designed to help businesses make the most of their data.
&gt; 
&gt; 


&gt; For simplicity, we have used **test.com** as the site name in the documentation. Please replace it with your actual site name.
&gt; 
&gt; 

First Scenario
--------------

Insights is installed in same site and you haven't configured anything.

1. Go to insights setup page &gt; &lt;https://test.com/insights/setup&gt;

[Screenshot on the live page: Screenshot 2025-01-31 at 1.08.30 PM]
2. Click on the first option **Connect to your ERPNext Site**.
3. Choose a title for your data source. It can be anything you prefer, then continue.

[Screenshot on the live page: Screenshot 2025-01-31 at 12.55.02 PM]
4. This may take a few minutes. Once it's complete, you will be redirected to insight's dashboard.
5. Open Data Sources and you will be able to see you database's tables.

[Screenshot on the live page: Screenshot 2025-01-31 at 12.57.00 PM]
6. Now you can write query, reports. For more details, check the documentation &lt;https://docs.frappe.io/insights/introduction&gt; .

Second Scenario
---------------

Insights is installed in different site and you need to connect with that.

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.

  


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]
2. Go to insights setup page &gt; &lt;https://test.com/insights/setup&gt;

[Screenshot on the live page: Screenshot 2025-01-31 at 1.08.45 PM]  


**Note :** If you have already completed setup and this page is not appearing to you, go to &lt;https://test.com/insights&gt; and click on **Connect Data Source**.
3. Click on **MariaDB** and continue.
4. Fill in the required information and make sure to check the **Use SSL** checkbox.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.26.50 PM]
5. Click on **Connect**
6. Once connection verified, click on **Continue** button.
7. This may take a few minutes. Once it's complete, you will be redirected to insights dashboard.
8. Open Data Sources and you will be able to see you database's tables.

[Screenshot on the live page: Screenshot 2025-01-31 at 12.57.00 PM]
9. Now you can write query, reports. For more details, check the documentation &lt;https://docs.frappe.io/insights/introduction&gt; .

  

<!-- page: cloud/cloud__getting-started__connect-learn.md -->
---
title: "Connect & Learn"
space: "Cloud"
url: "https://docs.frappe.io/cloud/getting-started/connect-learn"
updated: "2026-05-30"
---

## Important Links

- [Telegram Chat](https://t.me/frappecloud)

- [Discuss Forum](https://discuss.frappe.io/c/frappe-cloud/77)
- [GitHub (Press)](https://github.com/frappe/press)

<!-- page: cloud/cloud__getting-started__faqs.md -->
---
title: "FAQs - General"
space: "Cloud"
url: "https://docs.frappe.io/cloud/getting-started/faqs"
updated: "2026-05-30"
---

### Do you have maintenance windows?

No specific maintenance window policy is in place due to varying activity types. We inform users beforehand via email about potential downtime during maintenance activities.

<!-- page: cloud/cloud__getting-started__plans-pricing__change-product-warranty-for-dedicated-sites.md -->
---
title: "Change product warranty for dedicated sites"
space: "Cloud"
url: "https://docs.frappe.io/cloud/getting-started/plans-pricing/change-product-warranty-for-dedicated-sites"
updated: "2026-06-15"
---

## Overview

Product warranty determines whether your site on a dedicated server is covered by Frappe Cloud's support SLA. You can manage this setting directly from your site's actions panel.



**Note:** We do not provide product warranty for sites on <$100 Hetzner app server plans.



## Managing Warranty on Your Site

1. Navigate to your site's detail page
2. Go to **Site Actions**
3. Click **Manage Product Warranty**
4. Toggle the warranty setting and save

### Cooldown Period

To prevent frequent changes, each dedicated server has a **warranty cooldown period**. You can only change a site's warranty status once per cooldown window.



- If the cooldown hasn't elapsed, the action will show you when the next change is available
- The warranty setting applied when you first create a site doesn't count toward the cooldown — only subsequent changes do
- You are free to disable product warranty on one site and enable it for others. However, only a fixed number of sites can have product warranty enabled at the same time.



---



## When You Create a New Site

When creating a site on a dedicated server, Frappe Cloud automatically picks the best plan based on your server's warranty configuration:



- If your server's plan qualifies for product support, the site is created with both **Product Warranty** and **High Performance** enabled
- If it doesn't qualify, the site is created with **High Performance** enabled but **Product Warranty** disabled



---



## Default Configuration

Warranty settings (cooldown period and quota) are configured at the server level. The platform-wide defaults are:



- **Warranty cooldown:** 30 days
- **Site warranty quota:** 5



These defaults apply to new dedicated servers. Settings on existing servers are not affected when defaults change.



If you'd like your cooldown period or warranty quota adjusted, please [contact support](https://frappecloud.com/support).



---



## Notes

The **Manage Product Warranty** action may not be visible for servers where product support is not applicable



---



*For implementation details, see [PR #6166](https://github.com/frappe/press/pull/6166).*

<!-- page: cloud/cloud__getting-started__uptime.md -->
---
title: "Uptime"
space: "Cloud"
url: "https://docs.frappe.io/cloud/getting-started/uptime"
updated: "2026-05-30"
---

We provide hosting via multiple cloud providers with the following uptime guarantees:


| Provider      | Uptime Guarantee                                                                                                                                                                                                           |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS           | [99.0 - 99.5%](https://aws.amazon.com/compute/sla/?did=sla_card&trk=sla_card)                                                                                                                                              |
| Digital Ocean | [99.99%](https://www.digitalocean.com/sla/cpu-droplets)                                                                                                                                                                    |
| OCI           | [99.9%](https://www.oracle.com/content/published/api/v1.1/assets/CONT95B931480DF242229DF530A64F0D0245/native/Oracle+PaaS+and+IaaS+Public+Cloud+Services+Pillar+Document.pdf?channelToken=117bec9b3b4e4e90a1c4c9069d210baf) |


We monitor uptime of each server and notify users via email if their server is consistently down. Engineers are notified via call for extended downtime.

<!-- page: cloud/cloud__guidelines-for-contributing-regional-compliance-app.md -->
---
title: "Guidelines for Contributing Regional Compliance App"
space: "Cloud"
url: "https://docs.frappe.io/cloud/guidelines-for-contributing-regional-compliance-app"
updated: "2026-06-05"
---

Every country has specific tax compliance laws that businesses must follow. ERPNext includes an accounting module with core features like maintaining a Chart of Accounts, creating tax invoices, and recording payments.

To handle regional tax rules, additional features can be developed and maintained in a separate Frappe application. For example, the [India Compliance App](https://frappecloud.com/marketplace/apps/india_compliance) lets users generate e-invoices, e-way bills, and GST reports required by the Indian government.

## Chart of Accounts

ERPNext comes with a pre-configured Chart of Accounts. If your country uses a different standard, you should first apply your country's specific Chart of Accounts over the standard one. This ensures all the necessary tax accounts are available for setting up taxes, which you will later select in accounting transactions.

You can contribute your regional Chart of Accounts to the core ERPNext repository in the specified folder. Alternatively, you can set up the Chart of Accounts through a custom app, which can also include the required tax ledgers.

Contribute the regional Chart of Accounts in the core repo of ERPNext, in [this particular folder](https://github.com/frappe/erpnext/tree/develop/erpnext/accounts/doctype/account/chart_of_accounts/verified)

[Screenshot on the live page]

Also, you can have Chart of Accounts setup via your custom application, which will include tax ledgers.

## Sales, Purchase and Item Tax Templates

To make applying taxes easier in transactions, ERPNext allows you to set up Tax Templates for sales and purchases. This helps new users correctly apply taxes to invoices to ensure they are compliant.

[Screenshot on the live page]

In cases where an invoice contains multiple items with different tax rates, an Item Tax Template should be auto-created. For instance, in India, there are GST slabs of 5%, 12%, 18%, and 28%. Since a single sales invoice can have items from different slabs, the tax must be defined at the item level.

## Regional Tax Setting

The final goal for tax ledgers is to provide reports as specified by the tax authorities. While tax ledgers are created in the Chart of Accounts, the system needs a setting to identify which ledger corresponds to which tax type. The India Compliance app, for example, has a GST Setting page for this.

[Screenshot on the live page]

This settings page can also store other country-specific configurations, such as API details for e-invoicing integrations.

[Screenshot on the live page]

## Workspace for Regional Taxation

Your regional compliance app will include several DocTypes, such as:

- Setting page (for tax ledgers and integration details with the system of tax authorities)
- Additional masters and transactions are required for creating compliant invoices
- Link of Reports
- Link of User manual and help videos

[Screenshot on the live page]

Do create a Workspace or sub-workspace that lists all these DocTypes, pages, and reports, grouped logically. This makes it easy for new users to find compliance features and helpful resources.

## Onboarding Help

You can create a step-by-step onboarding guide to help users set up the app. For reference, you can look at the onboarding flow in the Thai Taxation app.

[Screenshot on the live page]

## Reports

The success of a regional compliance app depends on providing accurate reports in the exact format and with the names specified by the tax authorities. It is extremely important to build these reports correctly. They should be grouped within the app's workspace based on their importance.

[Screenshot on the live page]

## Review Process

Your regional app will be reviewed from two main aspects:

**Technical Review:** This ensures the app follows Frappe's best practices and does not introduce security vulnerabilities. Frappe uses [Semgrep](https://github.com/frappe/semgrep-rules) as a CI/CD tool for security scanning of Frappe apps. App builders must run a Semgrep scan on their app’s repository and fix any vulnerabilities identified. A successful Semgrep scan (green check) will be a significant advantage in the review process.



Check Nikhil's talk for a comprehensive understanding of technical guidelines for building a compliance app. Start talk from 00:55 hrs.

<iframe src="https://www.youtube.com/embed/yyRW6wz6WVA?si=BlmOXWHsbV32XMVW" width="560" height="315" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



**Functional Review:** This ensures the app's features work as expected. It includes a session with the app builders to understand the country's tax system and verify that the features and reports meet those requirements. Accreditation from a tax authority is helpful. If not available, we may ask community members in your country to test and review the app's coverage.

#### Functional Review Criterias

- Does the app set up a country-specific Chart of Accounts with tax ledgers? At a minimum, does it auto-create the necessary tax ledgers?
- Does the app pre-configure Sales, Purchase, and Item Tax Templates?
- Is there a settings page where each tax account can be mapped to its official tax name?
- For countries with e-invoicing, does the setup capture company-wise tax and API details?
- Does the app add necessary Custom Fields to masters and transactions? For API integrations, can it fetch party details based on their tax ID?
- Does it add validations for custom fields, especially those mandatory for compliant invoicing?
- For e-invoicing, does the Sales Invoice fetch tax details? If the government provides a unique acknowledgement ID, is it stored in a read-only field? (This ID is often used for QR code generation on printed invoices).
- Ensure application has documentation sufficient to guide new user to complete taxation setup.
- Reports:
  - Are all required statutory tax reports available?
  - Are the reports named exactly as referred to by the tax authorities?

<!-- page: cloud/cloud__guides-and-manuals__what-is-product-warranty.md -->
---
title: "What is Product Warranty"
space: "Cloud"
url: "https://docs.frappe.io/cloud/guides-and-manuals/what-is-product-warranty"
updated: "2026-06-03"
---

# Product Warranty

## Overview

For Frappe applications such as **ERPNext** and **Frappe Framework**, Product Warranty is a developer support service that helps customers resolve verified product issues.

The warranty covers:

- Replicable product bugs in officially supported Frappe applications
- Security vulnerabilities affecting supported versions of Frappe products
- Defects that can be reproduced on a standard, unmodified installation

The warranty does **not** cover:

- Customisations or custom code
- Third-party applications and integrations
- Functional consulting, implementation assistance, or user training
- Data corrections, migrations, or configuration changes
- Issues caused by unsupported modifications to the product

## Eligibility

Product Warranty is available as part of an official Frappe support subscription.

### Included

Sites hosted on **Frappe Cloud** with plans starting at **$50/month (₹4,100/month)** or higher are eligible for Product Warranty coverage.

Product Warranty is also included for up to 5 sites hosted on any server priced at **$100/month (₹8,100/month)**  or higher.

### Not Included

Product Warranty is not available for:

- Self-hosted installations
- Frappe Cloud sites on plans below $50/month
- Customers without an active support subscription

Customers on ineligible plans can purchase an additional support subscription to access Product Warranty.

## How to Request Support

If you believe you have encountered a product-related bug or security issue:

1. Create a support ticket through Frappe Support Portal ([support.frappe.io)](https://support.frappe.io).
2. Provide clear reproduction steps, screenshots, logs, and any relevant details.
3. The support team will verify whether the issue is a product defect covered under Product Warranty.
4. Confirmed product issues will be prioritized and addressed according to the applicable support agreement.

<!-- page: cloud/cloud__guides__access-request.md -->
---
title: "Access Request"
space: "Cloud"
url: "https://docs.frappe.io/cloud/guides/access-request"
updated: "2026-02-16"
---

Access to Frappe Cloud resources are granted upon permission and on a time bound manner. This document explain how to manage this from both customer and agent perspectives.

> Implementation of access controls is not complete. There maybe hiccups here and there.

### Why is this needed?
Customer data security is of extreme importance to us. We want to treat that data with utmost respect and care. Hence, we deny access by default to everyone including Frappe employees. When in need of help and support, agents can ask for explicit permission for a limited time period. Customer can then accept or reject the request depending on the context. This ensures optimum conditions for data security and customer satisfaction.

### What should I as a customer do?
You can manage incoming access requests from Frappe Cloud dashboard itself. You can go to this dedicated page from the sidebar. It will look like this.

[Screenshot on the live page: image6357ec]

This list should tell you about the target resource or resources, reason for the request, time for expiry and when was it requested. The list is sorted by last updated. So most relevant requests will be kept on top.

Clicking any row will open a dialog with more details. It can show a list of resources and any additional permissions if requested.

[Screenshot on the live page: image17afbf]

Pending requests can be accepted or rejected. Once accepted, access will be granted for a limited amount of time. This includes any additional permissions mentioned in the request.

Already accepted requests can be revoked. This will instantly remove the agent’s access to mentioned resource. Please note that when there are multiple accepted requests against a common resource, all of them will have to be revoked for complete denial of access.

You will get a email and in-app notification when an agent requests access for one of your resources. You will also be notified when there are any updates on said request.

That’s it! There is nothing else you have to do. Your data will remain secure and untouched by anyone other than you!

### What should I as an agent do?
You are on the other side of this see-saw. Your role as an agent is to request access to a particular resource. There is no special page to do this. Instead, you can go a resource’s page and click on Request Access button. This will open a dialog asking for necessary information.

[Screenshot on the live page: image4c3a4a]

Ideally, you should ask for minimum required permissions depending on the need. More permissions can be asked later.

You will get email and in-app notifications whenever there is an update on the request. If the customer accepted your request, you can access the resource. All requests sent from your team can be tracked anytime in Access Requests page. This is the same page as customer, except you can see outgoing requests as well.

Clicking any of the rows will open up a dialog with it’s details. Like customer’s ability to revoke an accepted request, you can forfeit an accepted request. This will ensure you don’t keep access to a certain resource even after the issue is solved. Customer will get a notification regarding the same.

In addition to Access Requests page, you can see individual resource statuses in their own page. If you have access via request for a resource, a button with unlock icon will be shown on the top bar. This button opens a dialog with relevant permissions and dates. There is also an additional button to re-request access with or without permissions.

[Screenshot on the live page: image277c18]

That is all for an agent’s part. You can be headache free when it comes to consent, access and timelines. All of them are handled here!

<!-- page: cloud/cloud__handbook__fc-onboarding.md -->
---
title: "Most frequently used DocTypes"
space: "Cloud"
url: "https://docs.frappe.io/cloud/handbook/fc-onboarding"
updated: "2026-05-22"
---




| Doctype       | Used For                                                                                        |
| ------------- | ----------------------------------------------------------------------------------------------- |
| Site          | Details of a particular site including their team, bench, server, trial period etc              |
| Bench         | Details about a particular site's bench including status, docker build, deploy candidate etc    |
| Release Group | It can be referred to as umbrella term for bench.                                               |
| Agent Job     | Each activity on FC is performed via agent jobs. It stores information such as status, job, etc |
| Team          | Details about team along with team members and subscription details.                            |
| Invoice       | Every Site is monthly billed by FC and invoice is created for each site every month.            |
| Subscription  | This records what plans and marketplace apps a team has subscribed to.                          |
| Site Backup   | These are backup agent jobs of particular site.                                                 |

<!-- page: cloud/cloud__how-to-change-a-site-plan.md -->
---
title: "Change a site plan"
space: "Cloud"
url: "https://docs.frappe.io/cloud/how-to-change-a-site-plan"
updated: "2026-02-18"
---

To change a site plan, click on the change button from your Frappe Cloud site's dashboard on the overview tab.  
**[Screenshot on the live page]**  
  
Select the appropriate plan you want to change your site to and click on the change plan button to change your site plan to the newly selected one.**[Screenshot on the live page]**  

<!-- page: cloud/cloud__how-to-disable-auto-update-for-your-site.md -->
---
title: "Disable auto-update for your site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/how-to-disable-auto-update-for-your-site"
updated: "2026-02-16"
---


> Please note your site should be on a private bench group.
> 
> 

**1.** From your site’s dashboard click on the Update button.[Screenshot on the live page]  
  
**2.** Click on the “**Configure**” button.[Screenshot on the live page]  
  
**3.** Once you click on the Configure button you will see a pop-up, you can toggle On/Off the “Enable Auto Update” option.  
  
[Screenshot on the live page]  


  

<!-- page: cloud/cloud__how-to-get-static-ip.md -->
---
title: "Obtain a Static IP"
space: "Cloud"
url: "https://docs.frappe.io/cloud/how-to-get-static-ip"
updated: "2026-02-16"
---

To obtain a static IP, you will need to migrate your site to a dedicated server and request a static IP to be assigned to your site in advance. (You can request us via support portal)  
  
**Note**:- The IP that you will get by default will not be static

  

<!-- page: cloud/cloud__how-to-uninstall-an-app-from-the-site.md -->
---
title: "Uninstall an app from the site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/how-to-uninstall-an-app-from-the-site"
updated: "2026-02-16"
---

Go to the Apps tab from your Frappe Cloud dashboard.[Screenshot on the live page]  
  


Click on the three dots of the app you want to uninstall from your site.[Screenshot on the live page]  
  


From the drop-down select uninstall.[Screenshot on the live page]  

<!-- page: cloud/cloud__in-place-updates.md -->
---
title: "In Place Updates"
space: "Cloud"
url: "https://docs.frappe.io/cloud/in-place-updates"
updated: "2026-02-16"
---

In place updates is an experimental feature that allows you to update your bench without having to wait for a regular update to take place.

The targeted use case for in place updates are:

1. Shipping small changes (that will not break a site) quickly to production.
2. Shipping changes to few number of targets (few sites and a single bench).


> ℹ️ **Info**
> 
> A regular update does the following:
> 
> 1. Build new image with updated apps
> 2. Create new Bench from the newly built image
> 3. Move site from old Bench to the new Bench
> 
> An in place update instead updates the old Bench without building an image which is a time consuming step.
> 
> 

Enabling in place updates
-------------------------

You will have to contact the Frappe Team to enable In Place Updates. Due to the caveats we do not enable for all users.


> ℹ️ **Info**
> 
> This does not mean all updates will be run in place. Certain conditions need to be met for an update to occur in place.
> 
> 

Required conditions for an in place update
------------------------------------------

After you have enabled in place updates, a few conditions need to be met:

1. All Sites under a bench have to be updated.
2. Only sites under a single site group can be updated.
3. Apps cannot be removed from a bench.
4. Selected bench should have been successfully updated in place (or should not have been in place updated).

To understand points 1. and 2. please see the image below:

[Screenshot on the live page]  


Here 7 **sites** under 3 **site groups** under the **FrappeDesk** Bench Group have been highlighted by red squares. When running an in place update only sites under one of these groups can be updated.

For instance sites *demosite.frappe.cloud* and *test-company123.frappedesk.com* cannot be updated with an in place update. For this a regular update will have to be used.

Caveats of an in place update
-----------------------------

There are a few reasons for why you would not want to use a regular update:

1. In place update is **less safe than a regular** update because if the update fails, your site can go down. This does not happen in a regular update because we create a separate container for each update.
2. **Failing patches are skipped by default**. This is to prevent failing patches from interrupting the migration procedure.
3. **Backups are not taken** before an in place update.


> ⚠️ **Warning**
> 
> Due to the mentioned caveats, it would behoove you to ensure that there are no breaking changes before running an in place update.
> 
> 

Using an in place update
------------------------

To use an in place update for deployment, follow this [document](https://frappecloud.com/docs/sites/how-to-update-an-app-site-on-a-private-bench) until step 2. If all the above mentioned conditions have been met, the dialog box you see will be a bit different:

[Screenshot on the live page]  


Enable the **Use in place update** checkbox. The action button will now say **Update site in place** instead of **Deploy and update site**.

Once you click the **Update site in place** button, you will be redirected to the update job:

[Screenshot on the live page]  



> ℹ️ **Info**
> 
> If the Update Bench In Place job fails, Frappe Cloud will try to recover your bench by running the Recover Update In Place job:
> 
> [Screenshot on the live page]  
> 
> 
> If this occurs, you cannot use in place update to update this bench.
> 
> 

<!-- page: cloud/cloud__installing-an-app.md -->
---
title: "Installing an app"
space: "Cloud"
url: "https://docs.frappe.io/cloud/installing-an-app"
updated: "2026-02-18"
---

## Public sites

You will be able to install featured apps from the [marketplace](https://frappecloud.com/marketplace) only for your site. To install an app

1. Click on Apps tab of your Site's dashboard

[Screenshot on the live page]

2. Click on Install App
3. Select the app you need to install
  [Screenshot on the live page]

## Sites on Private bench groups

You can add custom apps or any app from the [marketplace](https://frappecloud.com/marketplace) to your bench group and then install to your site. To install an app on a site on private bench group you have to add app in 2 places.

### Bench Group

1. Click on Apps tab of your Bench Group's dashboard

[Screenshot on the live page]

2. Click on Add App

[Screenshot on the live page]

3. Select any marketplace app or follow [this guide](https://frappecloud.com/docs/benches/custom-app) to install a custom app.

[Screenshot on the live page]

4. Click on the Update Available button to create a new deploy so that your site can install the app

[Screenshot on the live page]

5. Select your site while doing the update and click on deploy and update

[Screenshot on the live page]

### Site

1. Once the update is done click on Apps tab of your Site's dashboard

[Screenshot on the live page]

2. Click on Install App

[Screenshot on the live page]

3. Select the app added earlier to install

[Screenshot on the live page]
