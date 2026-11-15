<!-- Frappe documentation: cloud, part 3 of 3. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__sites__move-site-to-private-bench.md -->
---
title: "Move site to private bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/move-site-to-private-bench"
updated: "2026-06-17"
---

**Note:** This option is now part of the **Site Migration** feature.

For instructions on moving a site to a different server / bench, see the documentation : [https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench](https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench)

---

> If you want to move to a dedicated server refer [Move site across server](https://frappecloud.com/docs/sites/move-site-across-server)
>
> **Note:** If you need to move to a bench on another server, you need to move the current bench [to the server](https://frappecloud.com/docs/sites/move-site-across-server) first, and after that is done, do **Change bench** by following this doc.

You can directly schedule Site Migration to a private bench from a site's dashboard.

1. To change your site to a private bench, go to your site Dashboard>Actions>Change Bench

![](/files/Ceb7DH0.png)

2. If you don't have an available private bench, click on Clone current Bench to create a compatible private bench for your site to move to.

![](/files/UvskiT2.png)

3. If there's a compatible private bench, click on Change Bench to start moving the site to the chosen bench.

![](/files/5KyGxnV.png)

<!-- page: cloud/cloud__sites__site-config.md -->
---
title: "Site Config"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/site-config"
updated: "2026-02-19"
---

[Site Config](https://frappeframework.com/docs/v13/user/en/basics/sites#site-config) is the Frappe Framework way of specifying environment variables.

Site Config let's you configure options that is specific to a single site.

For e.g.

- Configure an Email account to send emails from.
- Disable Website Cache
- Disable [Global Search](https://docs.erpnext.com/docs/user/manual/en/using-erpnext/Global-search)
- Enable [Server Scripts](https://docs.erpnext.com/docs/user/manual/en/customize-erpnext/server-script)

## Update Site Config

1. Go to the **Site Config** tab.
2. Enter values in the corresponding input field.
3. Click on **Update Configuration**.

![](/files/w9v6T9E.png)

# FAQ

## Why can't I enable developer mode?

Developer Mode lets you create standard documents like DocType, Page, Report, Workspace, etc. These are standard as they are persisted on disk as JSON files. These must be part of an app. You cannot add these files to the standard Frappe and ERPNext apps. Therefore, you will need to [create your own app](https://frappecloud.com/docs/benches/custom-app).



Furthermore, apps on Frappe Cloud are ephemeral. We pull a fresh copy from Github every time a new bench is deployed.Therefore, even if you do manage to enable developer mode, your changes shall not persist.  
 

That is why you cannot enable developer mode on Frappe Cloud. You must create those features as a part of a custom app and then upload it on Frappe Cloud to use it.

<!-- page: cloud/cloud__sites__version-upgrade.md -->
---
title: "Version Upgrade"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/version-upgrade"
updated: "2026-03-12"
---

You can directly schedule version upgrades from a site's dashboard.

### Sites on Private Benches

1. To upgrade the version for your site, go to your Frappe cloud site Dashboard > **Actions** > **Version** **Upgrade**.
  ![](/files/Z2MWPOI.png)
2. If you have any custom frappe apps on your bench, you will be prompted to select the branch.
  ![](/files/Screenshot 2026-02-26 at 1.40.13 PM.png)
3. Click on Upgrade.
4. A new bench will be created and the site will be moved there.

### Sites on Public Bench

1. To upgrade the version for your site, go to your Frappe cloud site Dashboard > **Actions** > **Version** **Upgrade**.
2. Click on Upgrade if your site is not on the latest version.

![](/files/flBiOZD.png)

<!-- page: cloud/cloud__soc-2-report.md -->
---
title: "SOC 2 (Systems and Organization Controls) Report"
space: "Cloud"
url: "https://docs.frappe.io/cloud/soc-2-report"
updated: "2026-02-16"
---

Frappe has successfully attained SOC 2 Type II attestation for the review period of 1st June 2024 to 31st May 2025, in addition to its existing ISO 27001:2022 certification.

The SOC 2 Type II report, issued by an independent audit firm indicating that Frappe’s internal controls related to security, availability, and confidentiality have been effectively designed and operated throughout the review period in a satisfactory manner.

This milestone highlights our commitment and continual improvement related to data security and privacy. With both ISO 27001 and SOC 2 Type II in place, Frappe provides customers and partners with increased assurance that their data is handled securely and responsibly.

Frappe's ISO 9001 and ISO 27001 certifications along with the SOC 2 Type II attestation report are available [here](https://frappe.io/quality-and-information-security).

<!-- page: cloud/cloud__storage-addons.md -->
---
title: "Storage Addons"
space: "Cloud"
url: "https://docs.frappe.io/cloud/storage-addons"
updated: "2026-05-10"
---

## Introduction

In case the base storage included in the Server's plan is not enough, you can always add more storage to your server as required at an additional cost of $0.2/GB per month. Note that [AWS does not allow us](https://repost.aws/questions/QUPe0ekJ79TpaI-TNGoPXIKQ/can-i-reduce-an-over-sized-ebs-volume) to revert the storage added to a volume. So, if it turns out that you don't need the additional storage that's been added to your server, you can create a new server and move your sites over to the same.

## Steps to add storage manually

1. Click on the + button adjacent to the server you want to add storage to

![](/files/lqujBfZ.png)

2. Select the amount of storage you want to add. Note that you can't add storage again for a period of 6 hours.

![](/files/NcZAh9c.png)

3. Select confirm to increase the storage

&gt; Before the addons were introduced, Frappe Cloud itself was handling the additional storage being added on the server. The system automatically adds additional storage as and when required in order to prevent downtimes and other issues (mainly redis) from happening. If you wish to opt-out of this feature, you can disable it following the below steps. Note that if you do choose to do this, the downtimes on the server will be ignored by the system.  
&gt;  
&gt; 

## Steps to disable Auto Increase Storage

1. Click on the spanner icon adjacent to the server you want to disable auto add storage

![](/files/lqujBfZ.png)

2. Uncheck the box

![](/files/Screenshot%202025-07-29%20at%2017-57-51%20Frappe%20Cloud.png)

3. Click on confirm to disable the feature.

## FAQ

### Why does application server storage take so much more than sum of sites' storage

![](/files/gfTicLd.png)



You may notice that the storage consumed in your application server is much larger than sum of storage of all the sites you have on the same. This is because the total storage consumed also includes all the benches (and therefore code and it's dependencies) deployed on your server.

Once you drop a Bench Group, you may notice that the storage doesn't go down immediately. This is because of docker cache. This should get cleared [within 6 hours](https://github.com/frappe/press/blob/873be0859355f2328dd0b265608d38022554acc1/press/hooks.py#L248-L249) when scheduled cleanup for the same happens.

### Why does storage increase during bench/site update

This happens majorly as we take table-wise backup of the site during update. This is done so that in case of any failure during migration (eg: some breaking patch), all the changes done so far to the tables can be quickly rolled back. They're stored in the .migrate folder. This files in this folder should **NOT** be removed/updated manually as this can cause data loss

![.migrate folder](/files/Screenshot_20250724_191323.png)

You may therefore find it useful to update sites one at a time to reduce this increase in storage.

Moreover, deploying new bench also downloads a new image onto the app server. This has the newer code deployed in your updated apps. This will also take some space.

### Why does storage increase more than the limit

The feature automatically increases available storage as it reaches over **90%** of its capacity. The limits apply for each such increase and does not impose an overall limit as of now. This is done to ensure uptime. In the future, we will allow imposing a hard limit on storage increased automatically.

### How to force cleanup unused files

Under server actions, you can find option to **Cleanup Server**. If you have performed too many site updates recently, you can force cleanup of older bench versions from your server.

![](/files/image0d8c65.png)

![](/files/imageca30a8.png)

<!-- page: cloud/cloud__switching_between_teams.md -->
---
title: "Switching between Teams"
space: "Cloud"
url: "https://docs.frappe.io/cloud/switching_between_teams"
updated: "2026-02-16"
---

You can switch easily between teams from the Team section in Settings.

![](/files/cTjeBOU.png)  


If you want to leave a team, first switch to some other team and then click on the Switch button under the Change Team action.![](/files/fCpXfpP.png)  


Rememeber you can't leave your own team(created when you signup) since your the owner of that team.

<!-- page: cloud/cloud__tiny-plan.md -->
---
title: "Tiny Plan ($5 / month)"
space: "Cloud"
url: "https://docs.frappe.io/cloud/tiny-plan"
updated: "2026-02-16"
---

### Why is it so cheap ?

This plan has a couple of constraints on resource usage, deployment location, and the ability to install only selected apps. Custom apps are also not permitted.

This plan provides

* 0.5 compute hour / day
* 250 MB of database storage
* 2.5 GB of disk storage

It has several limitations

* Currently, this plan is available only on Mumbai, KSA & Virginia region.
* Background jobs will be scheduled every 10 minutes, rather than every minute
* Incoming HTTP requests will be timed out in 30 seconds instead of 120 seconds.
* You can only specific apps on site. (scroll below to check the allowed apps list)
* We can add some other limitations on this plan as per requirement.

There are also some restrictions -

* You can't disable auto update of your site
* This plan is unavailable for private bench groups
* You can't downgrade to this plan from other plans

### Why is this plan available only in specific regions ?

Out of all the accessible regions, the Mumbai, KSA & Virginia Regions have servers at affordable rates to provide this 5$ plan.

### Why are there restrictions on the installation of apps ?

Tiny Plan allows only a limited number of apps to be installed. To ensure low-cost deployment, all apps must be optimized so that they do not cause issues for other sites, as the site will be placed on a shared server.

### Why can't I downgrade to this plan ?

Because of the limitations imposed, moving to this plan is not as easy as others, therefore, it is best to take a backup and restore it on a new 5$ plan site if you desire to do so.

### Why can't I upgrade to this plan ?

Same reason as above. Please do a backup/restore.

### **Allowed Apps**

Currently, these apps are allowed to install in $5 plan.

* Frappe
* ERPNext
* HRMS
* Frappe CRM
* Builder
* Insights
* Gameplan
* LMS
* Wiki
* Raven
* Helpdesk
* Print Designer
* India Compliance
* Education
* Drive
* Email Delivery Service
* Payments
* Lending
* Webshop
* KSA Compliance
* Burundi Compliance
* erpnext_germany
* erpnext_france
* Swiss accounting software
* ERPNext Egypt Compliance
* Kenya Compliance via Slade
* ERPNext Indonesia Compliance
* Uganda Compliance
* EU einvoice

  

<!-- page: cloud/cloud__two-factor-authentication-2fa.md -->
---
title: "Two-factor authentication (2FA)"
space: "Cloud"
url: "https://docs.frappe.io/cloud/two-factor-authentication-2fa"
updated: "2026-02-16"
---

Two-Factor Authentication (2FA) is a security measure that requires two different methods of verification to access an account.


> At the moment you can only use an authenticator app to enable 2FA
> 
> 

Authenticator App
-----------------

We use [TOTP](https://en.wikipedia.org/wiki/Time-based_One-Time_Password) method, that generates a unique password that is valid for a limited time, for 2FA.

### Enable 2FA

1. Go to Settings and click on enable beside the enable 2FA option.
2. Download an authenticator app on your phone, such as [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) or [Aegis](https://github.com/beemdevelopment/Aegis) or use a browser extension like [1Password](https://support.1password.com/one-time-passwords/).
3. Scan the QR code using the app or extension.
4. Enter the code that's generated in the app to enable 2FA for your Frappe Cloud account.


> Make sure to backup your vault/keys through the app as losing it means you could potentially get locked out of your Frappe Cloud account
> 
>

### Disable 2FA

1. Go to Settings and click on disable beside the disable 2FA option.
2. Open your authenticator app.
3. Enter the code that's generated in the app to disable 2FA for your Frappe Cloud account.


> Disabling 2FA makes your account less secure
> 
>

### Enforce 2FA for the whole team

1. Go to Settings and navigate to team tab.
2. Click on Settings button.
3. Switch Enforce 2FA button to enable it. Users will now be asked to enable 2FA when they visit the dashboard.

<!-- page: cloud/cloud__unknown-command-.md -->
---
title: "Unknown command -"
space: "Cloud"
url: "https://docs.frappe.io/cloud/unknown-command-"
updated: "2026-02-16"
---

When restoring a backup, you may see a command like so:


```
Restoring Database file...
ERROR at line 7: Unknown command '\-'.
```
This happens when backup from newer MariaDB is attempted to restore on an older version. This has been fixed in [**frappe**](https://github.com/frappe/frappe/) already. To rectify this, you should update your site to latest [supported](https://github.com/frappe/erpnext/wiki/Supported-Versions) version of frappe and try again.

  

<!-- page: cloud/cloud__webhook-attempt-logs.md -->
---
title: "Webhook Attempt Logs"
space: "Cloud"
url: "https://docs.frappe.io/cloud/webhook-attempt-logs"
updated: "2026-02-16"
---

Webhook attempt logs are essential for diagnosing issues on the webhook backend. They allow the end-user to review the request payload, response, and status code, enabling more effective troubleshooting.


> You can only view logs of last 24 hours only.
> 
> 

From the webhook record's actions button, you will be able to open the `Webhook Attempts List`

![Screenshot 2024-09-25 at 4.54.33 PM](/files/Screenshot 2024-09-25 at 4.54.33 PM.png "Screenshot 2024-09-25 at 4.54.33 PM.png")  


![Screenshot 2024-09-25 at 5.00.30 PM](/files/Screenshot 2024-09-25 at 5.00.30 PM.png "Screenshot 2024-09-25 at 5.00.30 PM.png")  


You can click on a row to view the details of a specific webhook attempt.

![Screenshot 2024-09-25 at 5.01.41 PM](/files/Screenshot 2024-09-25 at 5.01.41 PM.png "Screenshot 2024-09-25 at 5.01.41 PM.png")  

<!-- page: cloud/cloud__webhook-events.md -->
---
title: "Webhook Events"
space: "Cloud"
url: "https://docs.frappe.io/cloud/webhook-events"
updated: "2026-02-16"
---

Site Status Update
------------------

This event is triggered whenever the status of a site changes.

Sample Payload -


```json
{
   "doctype":"Site",
   "name":"ytest.tanmoy.fc.frappe.dev",
   "owner":"Administrator",
   "creation":"2024-09-13 10:04:41.244578",
   "modified":"2024-09-26 10:49:34.381793",
   "modified_by":"Administrator",
   "docstatus":0,
   "idx":7,
   "ip":"None",
   "status":"Active",
   "group":"bench-0008",
   "notify_email":"admin@example.com",
   "team":"dnjt4bkes2",
   "plan":"ERPNext Trial",
   "setup_wizard_complete":0,
   "archive_failed":0,
   "cluster":"Default",
   "bench":"bench-0008-000005-f1",
   "is_database_access_enabled":0,
   "trial_end_date":"2024-09-27",
   "tags":[
      
   ],
   "server":"f1.tanmoy.fc.frappe.dev",
   "host_name":"ytest.tanmoy.fc.frappe.dev",
   "skip_auto_updates":0,
   "additional_system_user_created":1
}
```
Site Plan Change
----------------

This event is triggered whenever a site is upgraded or downgraded to a different site plan.

Sample Payload -


```json
{
   "event":"Site Plan Change",
   "data":{
      "doctype":"Site Plan Change",
      "name":"368704046d",
      "owner":"tanmoy@frappe.io",
      "creation":"2024-09-24 11:29:41.596739",
      "modified":"2024-09-24 11:29:41.596739",
      "modified_by":"tanmoy@frappe.io",
      "docstatus":0,
      "idx":0,
      "from_plan":"USD 10",
      "to_plan":"USD 25",
      "type":"Upgrade",
      "site":"test465.frappe.cloud",
      "timestamp":"2024-09-24 11:29:41.596639"
   }
}
```

Bench Deploy Status Update
--------------------------

The event is trigerred whenever a new bench created under a Bench Group. It will notify your backend about all the status update for a new Bench.

Draft -> Scheduled -> Pending -> Preparing -> Running -> Success -> Failure

Sample Payload -

```json
{
    "event": "Bench Deploy Status Update",
    "data": {
        "doctype": "Deploy Candidate",
        "name": "deploy-0019-000059",
        "owner": "Administrator",
        "creation": "2025-04-09 13:24:33.597587",
        "modified": "2025-04-09 13:25:16.659627",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "status": "Success",
        "deployed": "None",
        "build_start": "2025-04-09 13:24:34.864515",
        "build_end": "2025-04-09 13:25:16.659052",
        "build_duration": "0:00:41.794537",
        "build_error": "None",
        "group": "bench-0019",
        "retry_count": 0
    }
}
```

Bench Status Update
-------------------

This event is trigerred whenever some actions are got performed on the bench and status got updated.

Pending -> Installing -> Updating -> Active -> Broken -> Archived

Sample Payload -

```json
{
    "event": "Bench Status Update",
    "data": {
        "doctype": "Bench",
        "name": "bench-0019-000059-f2-london",
        "owner": "Administrator",
        "creation": "2025-04-09 13:25:16.930474",
        "modified": "2025-04-09 13:27:21.992663",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "group": "bench-0019",
        "status": "Pending",
        "cluster": "London",
        "is_ssh_proxy_setup": 1,
        "inplace_update_docker_image": "None"
    }
}
```


If you have a requirement for other events, please [raise a feature request on github](https://github.com/frappe/press/issues/new).

<!-- page: cloud/cloud__webhook-introduction.md -->
---
title: "Introduction"
space: "Cloud"
url: "https://docs.frappe.io/cloud/webhook-introduction"
updated: "2026-02-16"
---

Frappe Cloud Webhooks help deliver events related to various resources directly to your backend service.

![webhook-slide](/files/webhook-slide.png "webhook-slide.png")  


This makes it easier to build tools and custom SaaS workflows on top of Frappe Cloud using the Frappe Cloud API and webhook events.

Notes
-----

1. Webhook configurations are specific to each team.
2. A team can have a maximum of 5 webhook endpoints configured.
3. If 70% of webhook requests to your endpoint fail within the past hour, the webhook will be disabled, and the team will be notified. You can re-enable the webhook from the dashboard after resolving the issue on your end.

<!-- page: cloud/cloud__what-are-benches-and-bench-groups.md -->
---
title: "What are Benches?"
space: "Cloud"
url: "https://docs.frappe.io/cloud/what-are-benches-and-bench-groups"
updated: "2026-02-27"
---

A **Bench** is a collection of apps and sites. All sites on a **Bench** share the same configuration, such as the version of apps, or version of dependencies.

Frappe Cloud creates the benches from templates which can be viewed under the **Benches** menu.

![](/files/Screenshot 2026-02-27 at 3.20.37 PM.png)

> For a more technical explanation of what a **Bench** is, see the [Bench confusion](#bench-confusion) section.

The template holds information such as:

- Which apps to install.![](/files/WtN8r0p.png)
- What common site config flags to be set for benches deployed from the current template.
- The version of dependencies to be used for the benches.

> **Private Bench"**
>
> If you are using a [private bench](https://frappecloud.com/docs/benches) then all of the above information can be set and updated by you.

### **When is a Bench created?**

A bench template by itself does not run your site. For this you have to *deploy* that template. This takes place when you click on *Deploy* or *Update Available* on your **Bench** page.

1. When you do this, a *Deploy* job (visible in the **Deploys** tab) is created. This job builds a [Docker image](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image) from the template and uploads it to the Frappe Cloud [Docker registry](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry).
  ![](/files/Screenshot 2026-02-27 at 2.44.37 PM.png)
2. After the Deploy job succeeds, a *New Bench* job (visible in the **Jobs** tab) is created. This job downloads the template’s image and runs it on the server.
  ![](/files/Screenshot 2026-02-27 at 2.52.20 PM.png)

Once the **Bench** is up and running, a new site can be created on it, or an existing site can be moved to it from another **Bench**.

## **Bench confusion**

If you are familiar with [Frappe Framework](https://frappe.io/framework) development then term "bench" may not be a new one and might cause some confusion. This is a perfectly sane response to our shortcomings when it comes to naming things. To help clear this, I'll try and differentiate between the different benches:




| **Term**       | **Context**      | **Description**                                                                                      |
| -------------- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| *Frappe Bench* | Frappe Framework | Directory that holds a collection of Frappe Framework apps and sites on which they may be installed. |
| `frappe/bench` | Frappe Framework | [CLI tool](https://github.com/frappe/bench) used to manage a *Frappe Bench*.                         |
| **Bench**      | Frappe Cloud     | *Frappe Bench* running inside a container from which your site is served.                            |


In the context of Frappe, all benches are conceptually linked (unless you are talking about a [regular bench](https://en.wikipedia.org/wiki/Bench_(furniture))).

<!-- page: cloud/cloud__whats-new.md -->
---
title: "What's New"
space: "Cloud"
url: "https://docs.frappe.io/cloud/whats-new"
updated: "2026-05-30"
---

## Major updates from 2026

The biggest update from this year is that Frappe Cloud has added 2 new providers - Hetzner and DigitalOcean, and an option to host App and Database on one server - also called Unified Server deployment. 

Watch this video to know more about it. 

<iframe width="800" height="450" src="https://www.youtube.com/embed/mRRfPPeurY8?si=fAcECAVwWtV89Duh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



---

## Recap of 2025

2025 was an year of continuous improvement. You can read about them in [this blog](https://frappe.io/blog/engineering/frappe-cloud-in-2025-a-year-of-magic-under-the-hood) or watch the video below. 

<iframe width="800" height="450" src="https://www.youtube.com/embed/4DMeDg3YYl0?si=Jil2EDOcerSkRAMO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
