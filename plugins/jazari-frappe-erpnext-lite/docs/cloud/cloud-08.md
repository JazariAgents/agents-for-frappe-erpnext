<!-- Frappe documentation: cloud, part 8 of 9. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__site__site-migrations__move-site-from-shared-to-private-bench.md -->
---
title: "Move Site From Shared To Private Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/move-site-from-shared-to-private-bench"
updated: "2026-03-06"
---

If your site is currently running on a **shared bench**, you can move it to a **private bench** to gain access to **Server Scripts**, install **custom apps**, and have better control over your bench environment.



1. **Verify Plan Eligibility :** First, confirm that your **site plan supports private benches**. If your current plan does not support this feature, a **banner will appear on the site page** indicating that an upgrade is required. Click the **Upgrade Plan** button to proceed.
  ![](https://docs.frappe.io/files/image7fab00.png)
2. **Upgrade Your Plan :**  To enable private bench support, upgrade your site to **any plan priced at $25/month or higher**.
  ![](https://docs.frappe.io/files/image38f232.png)
  After upgrading, a new banner will appear on the site page prompting you to move the site. Click **Move to Private Bench**.
  ![](https://docs.frappe.io/files/imageeefb3c.png)
3. **Confirm the Migration Configuration :** A dialog will appear with **pre-filled configuration details** for the migration.  
In most cases, you can keep the default values and click **Move to Private Bench** to proceed.  
  ![](https://docs.frappe.io/files/imagef260b3.png)
  Additional options are also available in the dialog, such as - Moving the site to a dedicated server or to an existing bench. You can explore these options if your setup requires a different configuration.  

4. **Track the Migration Progress :** After triggering the migration, you will be redirected to a **progress page** where you can monitor the status of the operation.
  ![](https://docs.frappe.io/files/imageda50be.png)
5. **Migration Completion :** Once the migration process finishes, your site will be running on a **private bench** according to the selected configuration.
  ![](https://docs.frappe.io/files/imageb09efa.png)
  You can now start using features such as **server scripts and custom app** for your site.

<!-- page: cloud/cloud__site__site-migrations__move-site-to-different-region.md -->
---
title: "Move Site To Different Region"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-region"
updated: "2026-03-06"
---

To move your site to a **different region**, follow the steps below.

> If your site is currently running on a **Shared Bench**, you can skip the region setup steps described below.

### 1. Add the Target Region

Go to your **Private Bench** and open the **Regions** tab.

Click **Add Region** and select the region where you want to deploy your site.

![](/files/image41a717.png)

### 2. Wait for Bench Provisioning

After adding the region, return to the **Sites** tab.

A **new bench** will appear with the status **Installing**. Wait until the bench becomes **Active** before proceeding.

![](/files/image485bb7.png)

### 3. Trigger the Migration

Once the bench becomes active, open your **Site** and go to the **Migrations** tab.

Click **Trigger Migration**. From the migration type options, select **Move Site to Different Region**, then choose the **target region** where you want the site to be moved.

![](/files/image939156.png)

### 4. Migration Completion

Once the migration process completes, your site will be **successfully moved to the selected region**.

<!-- page: cloud/cloud__site__site-migrations__move-site-to-different-server-or-bench.md -->
---
title: "Move Site To Different Server or Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench"
updated: "2026-03-08"
---

If you want to move your site to another **server** or **bench**, you can do so from the **Migrations** tab.

Go to the **Migrations** tab and click **Trigger Migration**.

![](/files/imageb2de81.png)



## **Choose a Migration Option**

You will see two available options :

### 1. Use New Bench

Select this option if you want to **create a new bench** and move your site there.  
When choosing this option, you can deploy the new bench in one of two ways :

- **Shared Server** – Create the new bench on a shared server (managed by Frappe).
- **Dedicated Server** – Deploy the new bench on a dedicated server.

After selecting your preferred configuration, click the button to **proceed with the migration setup**.

![](https://docs.frappe.io/files/image0283c6.png)

**Note:** If you are moving your site **from dedicated server to shared server**, the system will set **100 USD** as **default plan** after migration. Thereafter, you can upgrade / downgrade site plan according to your requirement.

### **2. Use an Existing Bench :**

Select this option if you already have a **bench with the required apps installed**.

You will need to :

- Select the **bench**
- Select the **server where the bench should be deployed**

After selecting the appropriate options, click the button to **proceed with the migration configuration**.

![](/files/imagead7e63.png)

<!-- page: cloud/cloud__sites__activity.md -->
---
title: "Activity"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/activity"
updated: "2026-02-16"
---

Frappe Cloud maintains a log of all actions taken on your sites.




![](/files/Screenshot%202025-06-20%20at%2012.34.43%E2%80%AFPM.png)

All actions taken on the sites from the dashboard or triggered directly by the system are logged in Frappe Cloud. This log may be viewed from your site's Activity tab.

<!-- page: cloud/cloud__sites__backups.md -->
---
title: "Site Backups"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/backups"
updated: "2026-02-27"
---

# Introduction

On Frappe Cloud, we take automated backups for site's with $25 plan and further. Frappe Cloud has automated mechanism in the backend which makes sure to take backup for your site every day.

Frappe Cloud offers two types of backups: on-site (physical) and offsite (logical) backups. Let's have a look at what each of that means.

1. **Onsite**: These backups stay on the server machine and never leave the server. They are stored in compressed format. Onsite backups are usually faster.
2. **Offsite**: In offsite, we take a backup of the site, compress it with `gzip` and then the compressed file is uploaded to an AWS S3 Bucket in `ap-south-1` (Mumbai) region by default. Read more about [offsite backups.](https://docs.frappe.io/cloud/sites/backups#offsite-backups)

## Onsite Backup Frequency

Frappe Cloud takes automated backups of your sites every **24** hours. There is no setting to increase this setting as of now. 

The setting inside **System Settings** is for how many onsite backup files to keep within the sites directory, provided multiple backups have been taken. This will **NOT** change the number of automated backups taken by Frappe Cloud.

![](/files/87rYe4n.png)
*configuring number of onsite backups*

As of now, there is no limit on how many onsite backups you can take in a day. You can mention any number which make sense and also take on-demand backups.

## Offsite Backups

> Offsite backups are available for sites on USD 25 and above plans.  
>
> Only the backup marked as "offsite" can be downloaded directly from Frappe Cloud dashboard  
>
> The onsite backups can only be downloaded from within the site

Automated backups are stored offsite, which means the files are stored on a different server than the site. This ensures that you can access your backups even in the unfortunate event of server downtime.

In the process of taking an offsite backup, we take the backup, compress it and it is kept on your server machine until the upload to S3 Server is completed. Please make a note that, this increases your site's storage consumption metric by a few GB temporarily. Once the upload to the S3 server is completed the compressed files are automatically deleted from local.

Offsite backups are marked as such in the Backups tab.

![](/files/imaged559c8.png)
*Offsite backup reprensetation in the list of backups*

### Offsite Backup Rotation

For each site, a certain number of offsite backups are kept at all times. The frequency of backups is as shown below:

- 7 daily
- 4 weekly
- 12 monthly
- 10 yearly

This is done to store backups efficiently. For example, if the current day is Jan 13, then the backups available will be like so:

![Backups Example - December](https://cloud.frappe.io/assets/press/images/docs/brs-december.png)



![Backups Example - January](https://cloud.frappe.io/assets/press/images/docs/brs-january.png)
*Backup rotation policy representation a Calendar*

(Monthly and yearly backups before December 2020 not shown in picture)

- Weekly backups are taken every Sunday
- Monthly backups taken every 1st day of the month
- Yearly backups taken every 1st day of the year

# Actions

## Downloading backups

From the Frappe Cloud site dashboard, go to the **Backups** tab. Here you will see the list of backups that were taken of your site. Every backup consists of a database backup, public files backup, private files backup and a backup of your site's config.

![](/files/zuEcx4r.png)

## Trigger on-demand backup

You can also trigger a manual backup operation for your site anytime from the **Backups** tab by clicking on the **Schedule Backup** button.

The job will be queued and it will take a few minutes to complete.

![](/files/OMMoOUJ.png)

## FAQ

### Why is my backup size so much smaller than database usage I see in dashboard?

This is because we store backups in compressed form as it is static and no operations are being done on it. We use standard unix tool called gzip for compressing the backups. The difference is in size is thanks to the same.

You can download the backup and decompress it with gzip to compare the size for yourself. It should be almost same as the size you see in your dashboard.

### Forbidden: You need System Manager Role to access backup

This happens when you try to download onsite backup, and you are not logged in to your site with a user of role System Manager or higher. You can simply login as adminstrator from your FC dashboard and then try to download again.

### What are the scheduled times for these backups?

There's no scheduled time. We do backups for all sites on a round-robin basis. But if they want a scheduled time for backup to run, we can set it.

### How can I access and download the backed-up data?

You can access your backups from the Frappe Cloud dashboard>Backups tab.

### What is the storage capacity for backups?

We don't charge for these. They're uploaded to AWS s3 storage. So the limit is as high as they allow, which is 5 TB

### What is the policy for archiving or deleting old backups?

You can refer to our Frappe Cloud Policy page [here](https://frappecloud.com/privacy)

### How is backup data secured?

HTTPS is used for all communications. Encryption is opt-in. You can add a backup encryption key in the site config for this. [Here](https://frappeframework.com/docs/user/en/guides/basics/how-to-enable-backup-encryption) is how you can enable backup encryption.

### Where to find backup of particular date? The backup for the date I want is missing

We only keep backups as per our backup policy. You can take a look at our [rotation policy above](#offsite-backup-rotation) to get an idea of why certain dates' backups are available. Offsite backups are only available for $25 plan and above. No, you cannot request for a specific date's backup as we don't have them.

<!-- page: cloud/cloud__sites__change-team-of-site.md -->
---
title: "Change Team of Site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/change-team-of-site"
updated: "2026-02-16"
---

You can change the team of the site by using the **Transfer Site** feature.

1.  Select Transfer site option from the Actions tab in your site's dashboard.



![](/files/Screenshot%202025-08-20%20at%204.24.39%E2%80%AFPM.png)

2. Fill in the fields and click on Submit



![](/files/Screenshot%202025-08-20%20at%204.25.53%E2%80%AFPM.png)

3. The team that is supposed to receive the ownership will now receive a mail to accept the ownership. Click on **Accept Site Transfer** to accept the ownership of the site.




![](/files/image558c81.png)

<!-- page: cloud/cloud__sites__creating-a-new-site.md -->
---
title: "Creating a new site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/creating-a-new-site"
updated: "2026-05-22"
---

Simplest guide to creating a new site on Frappe Cloud

1. From the Sites tab on the dashboard, click on **New Site**.
2. Select the apps you want to install on your site 

![](/files/adOvj8s.png)
3. Select the site version you want, and the site region you want.![](/files/YrCJl0a.png)
4. Select the appropriate plan you want for your site. For more details visit our [pricing page](/pricing).

![](/files/jGRWR5c.png)
5. Choose a unique hostname for your site. Subdomain could be 5 to 32 characters long and contain lowercase alphabets, numbers, and hyphens. A subdomain can not start or end with hyphens.![](/files/XByVq6n.png)
6. It will take a few seconds for site creation depending on the apps you have chosen.
7. Click on Visit Site at the top of the page to access your site.
8. After site creation you will see a message, you can proceed to complete the setup wizard by clicking on login. You must log in and complete the setup wizard on your site. Analytics will be collected only after the setup is complete.


> Note: All sites are only available on HTTPS.
> 
> 

<!-- page: cloud/cloud__sites__custom-domains.md -->
---
title: "Custom Domains"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/custom-domains"
updated: "2026-08-14"
---

## Adding a custom domain

Frappe Cloud allows you to map custom domains that you own in a few simple steps.

1. Create DNS records from the dashboard of your domain provider. Follow **one** of the steps below:  
**Subdomain**: To point a subdomain to your site, add a **CNAME record** pointing your subdomain to your site. For example, if you want to use `www.example.com` for your site `example.frappe.cloud` then add CNAME record for `www.example.com` pointing to `example.frappe.cloud`. For the instructions to add such a record, please contact your domain provider.  
**Naked domain**: To point a naked domain like `example.com` to your site, simply add an **A** **record** pointing to the IP address of your site. You can get this IP from **Inbound IP** of your dashboard  
![](/files/3MWe7ri.png)  
One caveat to adding naked domains is that you will have to update the DNS record if the IP of your site changes.
  > **NOTE:** Only add 1 record. If you're adding multple **A** records for the same domain, you're doing it wrong.  
  > There are some DNS providers such as Cloudflare that allow adding CNAME records for naked domains. If so, you won't need an A record. Simply follow the same steps as in the Subdomain section above, replacing `www.example.com` with `example.com`.
2. After adding the DNS record, open your site dashboard.
3. From the site overview page, go to **Domains** card.
4. Click on Add Domain.
5. Enter the custom domain.
6. Click on Verify DNS.
7. If the verification succeeds, you have correctly added the CNAME record, and you will see Add Domain button. Click on Add Domain.  
![Custom Domains](https://cloud.frappe.io/assets/press/images/docs/site-domain.png)

> Note: We obtain an SSL certificate for the custom domain. So you will be able to use HTTPS with your domain.

> You are able to add both naked and subdomains to your site

![](/files/image43789c.png)

## Redirecting domains

In some cases, you may not want the user to see certain domains that direct you to your site. You may even want to hide your fancy **.frappe.cloud** domain that we provide. This is also possible.

1. You need to set one domain as primary domain. This is the domain where the "redirected domains" will redirect to

![Set Primary Image](/files/domain-redirect.png)

1. Next, you need to enable redirection for domains that you wish to hide

![Enable Redirect Image](/files/domain-redirect-2.png)

That's it. Your users will be able to access your site from the redirected domains, but they will be redirected to the **primary domain** which will show up in their address bar

> This redirection will also prevent the redirected domains from appearing in search engine results. Eg: Google Search

## Search Engine Optimization (SEO)

### Prevent my site from showing up in search engine/google search results

Please follow the steps in [this documentation](https://developers.google.com/search/docs/crawling-indexing/block-indexing) and update your **Website Settings** accordingly\*\*.\*\*

### Site Name/Title in search result shows as "Frappe Cloud"

This seems to happen when google crawls your site when it was deactivated/suspended. You can [ask google to recrawl your site](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) in such cases. If you continue to face issues, you may try the instructions [here](https://developers.google.com/search/docs/appearance/site-names#how-to-add-structured-data)

## FAQ

#### DNS verification failed even after adding DNS record on Cloudflare

Currently, the custom domains you add on FC don't work when Cloudflare proxy is enabled. Please use the **DNS only** option for your DNS record.

![Cloudflare DNS only](/files/dns_only.png)

Note that proxying can be re-enabled once the domain is successfully added in Frappe Cloud. However, there is an existing issue with websocket communication due to which real-time updates may not happen in site correctly. 

Note that if you have multiple A records and one of them is **proxied** [all records will be proxied](https://developers.cloudflare.com/dns/manage-dns-records/reference/proxied-dns-records/#dns-only-records).

### Add custom https certificate / CSR File Request

We don’t support adding arbitrary SSL certificates. You may add a custom domain, and we can generate a 4096-bit certificate for the same if that is the requirement. We’ve done so similarly for other customers.

### I want to whitelist my site's IP on a 3rd party service

You can use the **outbound IP t**o whitelist on any 3rd party services.

![](/files/mVhiq4U.png)

### Certificate information for Bank Integration

We cannot provide this for [Frappe.Cloud](http://Frappe.Cloud) or [ERPNext.com](http://ERPNext.com) domains due to security concerns. You will need to add a custom domain for the same. After adding custom domain, you may request for private key of the certificate over our [support portal](https://support.frappe.io)

### I want to change url or name displayed in outgoing emails and pdfs

Only the **primary** domain is sent within outgoing emails and PDFs. In order to change this to your custom domain, you can set the domain as **primary**

![Set Primary Image](https://frappecloud.com/files/domain-redirect.png)

### Can I move a domain that I use elsewhere to Frappe Cloud?

Yes, if you have bought the domain from a domain provider (E.g: Namecheap) , you can use it on Frappe Cloud by updating the DNS record as shown at the top of this documentation

### How to get full chain of SSL certificate?

Some browsers (eg: Firefox) allow you to download full chain of certificates easily. Otherwise, you may use this site to download the same easily: [https://whatsmychaincert.com](https://whatsmychaincert.com)

![](/files/0W9iQ07.png)

---

Frappe Cloud allows you to map custom domains that you own in a few simple steps.

1. Create DNS records from the dashboard of your domain provider. Follow one of the steps below:

**Subdomain**: To point a subdomain to your site, add a **CNAME record** pointing your subdomain to your site. For example, if you want to use `www.example.com` for your site `example.frappe.cloud` then add CNAME record for `www.example.com` pointing to `example.frappe.cloud`. For the instructions to add such a record, please contact your domain provider.  

**Naked domain**: To point a naked domain like `example.com` to your site, simply add an **A** **record** pointing to the IP address of your site. You can get this IP from **Inbound IP** of your dashboard

![](/files/3MWe7ri.png)

One caveat to adding naked domains is that you will have to update the DNS record if the IP of your site changes.

> **NOTE:** Only add 1 record. If you're adding multple **A** records for the same domain, you're doing it wrong.  

There are some DNS providers such as Cloudflare that allow adding CNAME records for naked domains. If so, you won't need an A record. Simply follow the same steps as in the Subdomain section above, replacing `www.example.com` with `example.com`.  
2. After adding the DNS record, open your site dashboard.  
3. From the site overview page, go to **Domains** card.  
4. Click on Add Domain.  
5. Enter the custom domain.  
6. Click on Verify DNS.  
7. If the verification succeeds, you have correctly added the CNAME record, and you will see Add Domain button. Click on Add Domain.

![](/files/image124f0c.png)



> Note: We obtain an SSL certificate for the custom domain. So you will be able to use HTTPS with your domain.

You are able to add both naked and subdomains to your site

![](/files/image853893.png)





## Redirecting domains

In some cases, you may not want the user to see certain domains that direct you to your site. You may even want to hide your fancy **.frappe.cloud** domain that we provide. This is also possible.

1. You need to set one domain as primary domain. This is the domain where the "redirected domains" will redirect to

![Set Primary Image](/files/domain-redirect.png)

1. Next, you need to enable redirection for domains that you wish to hide

![Enable Redirect Image](/files/domain-redirect-2.png)

That's it. Your users will be able to access your site from the redirected domains, but they will be redirected to the **primary domain** which will show up in their address bar

> This redirection will also prevent the redirected domains from appearing in search engine results. Eg: Google Search

## Web Application Firewall (WAF) Eg: Cloudflare

You may add WAF such as Cloudflare for your custom domain for the features they provide such as IP whitelist/blacklist, spam filter, etc. You can ensure that all request to your site receive the same by enabling redirects to the domain that you've added on WAF.

> Please note that there is a known issue where websockets fail to work with cloudflare. We don't have a solution for this as of now. So real-time updates will fail as of now

## Search Engine Optimization (SEO)

### Prevent my site from showing up in search engine/google search results

Please follow the steps in [this documentation](https://developers.google.com/search/docs/crawling-indexing/block-indexing) and update your **Website Settings** accordingly\*\*.\*\*

### Site Name/Title in search result shows as "Frappe Cloud"

This seems to happen when google crawls your site when it was deactivated/suspended. You can [ask google to recrawl your site](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) in such cases. If you continue to face issues, you may try the instructions [here](https://developers.google.com/search/docs/appearance/site-names#how-to-add-structured-data)

## FAQ

#### DNS verification failed even after adding DNS record on Cloudflare

Currently, the custom domains you add on FC don't work when Cloudflare proxy is enabled. Please use the **DNS only** option for your DNS record. 

![Cloudflare DNS only](/files/dns_only.png)

Note that if you have multiple A records and one of them is **proxied** [all records will be proxied](https://developers.cloudflare.com/dns/manage-dns-records/reference/proxied-dns-records/#dns-only-records).

### Add custom https certificate / CSR File Request

We don’t support adding arbitrary SSL certificates. You may add a custom domain, and we can generate a 4096-bit certificate for the same if that is the requirement. We’ve done so similarly for other customers.

### I want to whitelist my site's IP on a 3rd party service

You can use the **outbound IP t**o whitelist on any 3rd party services.

![](/files/mVhiq4U.png)

### Certificate information for ICICI Bank Integration

We cannot provide this for [Frappe.Cloud](http://Frappe.Cloud) or [ERPNext.com](http://ERPNext.com) domains due to security concerns. You will need to add a custom domain for the same

### I want to change url or name displayed in outgoing emails and pdfs

Only the **primary** domain is sent within outgoing emails and PDFs. In order to change this to your custom domain, you can set the domain as **primary**

![Set Primary Image](https://frappecloud.com/files/domain-redirect.png)

### Can I move a domain that I use elsewhere to Frappe Cloud?

Yes, if you have bought the domain from a domain provider (E.g: Namecheap) , you can use it on Frappe Cloud by updating the DNS record as shown at the top of this documentation

### How to get full chain of SSL certificate?

Some browsers (eg: Firefox) allow you to download full chain of certificates easily. Otherwise, you may use this site to download the same easily: &lt;[https://whatsmychaincert.com](https://whatsmychaincert.com)&gt;

![](/files/0W9iQ07.png)

### How to to verify DNS changes

You can use [this site](https://toolbox.googleapps.com/apps/dig/) to check if the DNS change you made have reflected on the internet.

<!-- page: cloud/cloud__sites__drop-delete-your-site.md -->
---
title: "Drop/Delete your site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/drop-delete-your-site"
updated: "2026-02-16"
---


> Note: You will lose all the data in your site as you proceed with these steps
> 
> 

If you don't want need your site anymore (including all the data in the site) and don't want to be billed for the same, you can drop your site from your Frappe Cloud dashboard.

1. From your Frappe Cloud site dashboard click on the **Actions** button![](/files/GcbJ7j4.png)
2. Scroll down and click on the Drop button beside the Drop site option 

![](/files/U01WObK.png)  
  
3. Type in the name of your site for confirmation and proceed to **permanently** delete your site ![](/files/eFN3GyI.png)

<!-- page: cloud/cloud__sites__how-to-update-an-app-site-on-a-private-bench.md -->
---
title: "Update an app/site on a private bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/how-to-update-an-app-site-on-a-private-bench"
updated: "2026-02-16"
---

  
1. Go to your bench group and click on the Update Available button, this will show the updates available for the **apps** you have added to your bench group.  
![](https://lh7-us.googleusercontent.com/AGGGfz0407BS6hoKD6634CobRibEZY3w8Au6RUzOruLQbbokzdpusss5l2b9fAncaioHjTr5FjOh4Ycags0U7eSdLhfKQiOqg6JFkwmsir3VfFlPvF8ZyenjtiXGHyyU0uAPY_IOIahMOnIHPXqxM9c)  
![](https://lh7-us.googleusercontent.com/12w5aOVpuWwpTxrNzG5wMiqEmgvY6fc9qxNXW7vfvsqCKOUBWB1pjTBPurrPZXPupd459SimuHTLKfvm_Van4mBP0FiMI6zkyLo8fVmd3G_ot36BMoi4D8-VRcobRA7DZLqLR9n6exTLardXCZBh84k)  
  
  
2. Select the apps you want to update and click on **Next**. You will be asked to select the site on which you want to update the apps, you can select the sites and click on **Deploy and Update**.  
  
  
![](https://lh7-us.googleusercontent.com/Nmhd965LRI18PWz7iTUMPHbH46dE6-TWOW447e1x_I_X2uoiwPNj6I-kzUvEXvm98Q8oQi1AfLUdpn7Fx-oaqPODTA3wvBrgJgiIKePBVzQbV--cke1ZoP66Zrf-PUnOS8RaT1KmikBCQ6kLb0C_KUU)  
  
  
**3.** Once done, you will see a new deploy in progress. Let the deploy complete. This usually takes around 20 mins.![](https://lh7-us.googleusercontent.com/4yNOST6CnIhy6om0W8QY41E-z4tV9jSK54SEpxjuokzMdj-6-QB31jGrFd7U5PmHFM-0_tkZIjCl6i4PsLBkUUjqhIEP1GlHLn7az_GG3_GJd3viQUuqOPPliav-NWm6niS2duLwnlwJlJZ-dWsitAE)  
  
4. Once the deploy has been completed, you will see your site updating as well to the latest version of the selected apps deployed on your bench group.![](https://lh7-us.googleusercontent.com/7quze_p82gZYYemUHjIxpoN2LUkS2SHZR639tzwkZ_F9fifYrRQz02amf5J9PjmlqsC59KvULobCK7DQFbhIWXNcPg9oLgz6hwchOwSXJBvDIFjUMTQhNWD568TjyqeHVL5rRTsyYDl0FyK6Dwqiz2Y)  



> **NOTE:- There will be some downtime while your site is updating**
> 
> 

<!-- page: cloud/cloud__sites__migrate-an-existing-site.md -->
---
title: "Restore & Migrate Site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/migrate-an-existing-site"
updated: "2026-07-17"
---

Restore an existing site by uploading backup files or by using a bench from your local setup or from your cloud provider.

> While migrating existing sites using the Frappe Cloud dashboard, some users miss the step to restore the site config details. If you're using the bench command, you won't have to worry about this.

## Restore from Backup Files

The easiest way to migrate an existing site on Frappe Cloud is to restore it from backup files.

1. Backup your site using the [bench backup](https://frappeframework.com/docs/user/en/bench/reference/backup) command.
2. You must have 4 files that should be named like the following:
  1. `20210817_125915-sitename-database.sql.gz`
  2. `20210817_125915-sitename-files.tar` (Public Files)
  3. `20210817_125915-sitename-private-files.tar` (Private Files)
  4. `20210817_125915-sitename-site_config_backup.json` (Site Config)
3. Create a **New Site** from the Sites tab in the Frappe Cloud Dashboard.
4. Fill out the subdomain and select the version.
5. Once the site is created and active, go to the Actions tab.
6. Click on the **Restore with files** option in the Dangerous Actions group.
7. Now, upload each file you got in Step 2 in their corresponding upload boxes.
8. Click on **Restore**.
9. When the site reaches Active state, you should be able to access the restored site.

> This method is ideal if your backup file's size is less 200MB. If you have larger backup files, you should use the `bench` command to migrate your site.

### Encryption Key

This key is used to encrypt passwords. This key is created automatically on a fresh site. Upon restoring a site from backup, this key will have to be copied into the site config as well to be able to use existing passwords.

In cases where you have lost your previous encryption key, and system has already generated a new key for you (you can verify this in your Frappe Cloud dashboard), you may stumble upon an "Encryption Key error". This is because certain password fields were encrypted using the old key. Now when then system tries to use those passwords, it fails as it tries to decrypt those passwords with the new key. In such cases, re-entering the value in those password fields will fix the problem (same password as before is fine). This works as re-entering the password will again encrypt the password using the new key.

> TLDR; Re-enter all password fields to encrypt them with new encryption key.

Eg: **Email Account** is a common doctype who's document has a password field. You will want to re-enter the annotated password field if you face errors while sending email.

![](/files/email-account-password163dd0.png)



### Restoring an encrypted backup

If you are experiencing this error while restoring your existing backup to Frappe Cloud.

```
Encrypted backup file detected. Decrypting using site config. Decryption failed. Please provide a valid key and try again.
```

To fix this `backup_encryption_key` should be added in [site config](https://frappecloud.com/docs/sites/site-config) before restoring.

## Migrate using FC Restore CLI

### Setup FC Restore CLI

**Setup on Windows**

1. Open a powershell window.
2. Run this command to download the CLI
  ```
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/frappe/fc-scripts/refs/heads/develop/fcrestore/cli.ps1" -OutFile cli.ps1
    .\cli.ps1
  ```

> In some cases, Windows Defender can flag the CLI with `trojan:Win32/Sabsik.FL.A!ml` virus. It's a false positive. You can safely whitelist the binary or disable windows defender tmeporarily.

**Setup on Linux / MacOS**

1. Open a new terminal
2. Run this command to setup the CLI
  ```bash
    curl -fsSL https://raw.githubusercontent.com/frappe/fc-scripts/refs/heads/develop/fcrestore/cli.sh | bash -
  ```

### User Guide

#### Login to CLI

You need to login to CLI using your Frappe Cloud account.

![](/files/user-auth.gif)

#### Restore Site

The CLI will guide you through the restoration process. You’ll need to choose what you want to restore — database, public files, or private files and upload the corresponding files.

Watch the video below for a step-by-step overview:

![](/files/restore.gif)

> If you have restored the database, please make sure to collect the encryption key from backup's site_config.json and set it on the new site. Please check above for the guide,

#### Cleanup

1. If you want to logout, you can just open up the CLI and it will ask you whether you want to logout. You can use that option.
2. Also there will be a `sessio.json` file in the same folder. You can just remove it for cleanup.

## Migrate using Bench

If you are running Frappe sites, most likely you have `bench` installed. You can run the following command to restore a site from your bench to Frappe Cloud.

```
bench migrate-to
```

You can run this command even from your local setup. If your site is hosted on a cloud provider like Digital Ocean or Amazon AWS, you must SSH into your server, and run this command.

The bench command provides a form similar to the dashboard UI. It's probably the easiest way to migrate your site to Frappe Cloud.  



It is prompt-based and even allows you to pass external backup files, this way there is no need to restore a site from backup, just to migrate it again somewhere else.  

![Screenshot 2024-07-29 at 2.19.03 PM](/files/Screenshot 2024-07-29 at 2.19.03 PM.png "Screenshot 2024-07-29 at 2.19.03 PM.png")





> If you are migrating a site from external backup files, pass the absolute path to said files.

> This method will work only if your sites are on Version **[v14.78.2](https://github.com/frappe/frappe/releases/tag/v14.78.2)** (for v14) or **[v15.36.1](https://github.com/frappe/frappe/releases/tag/v15.36.1)** (for v15) or [greater](https://github.com/frappe/frappe/pull/27115). If you are on an older version or this command didn't work for you, you can try the Python Script method explained later.

## Migrate using Python Script

If you are on an older version of Frappe (older than version 11) or the Bench command didn't work for you, you can try this method.

Make sure you have `wget` installed. Run the following commands from your bench directory:

```
wget https://frappecloud.com/assets/press/migrate
chmod +x migrate
./migrate
  
```

## Restore Backup on another site

You can restore backup on another site by following the given steps:-  



1. Click on the Backups tab from your site dashboard on which you have the offsite backup stored.

![](/files/Screenshot%202025-08-20%20at%204.48.45%E2%80%AFPM.png)



2. Click on the three dots of the offsite backup you wish to restore it on another site.

![](/files/Screenshot%202025-08-20%20at%204.49.47%E2%80%AFPM.png)

3. Once you click on the option you will be asked to select the site you want to restore it on, you can click the site and click on restore to continue.

![](/files/Screenshot%202025-08-20%20at%204.50.32%E2%80%AFPM.png)

![](/files/Screenshot%202025-08-20%20at%204.52.18%E2%80%AFPM.png)

4. Once done, it will automatically redirect to the restore job that will trigger.

## Migrate using site URL

While creating a new site using the new site creation wizard, you can go the **Migrate from Site URL** tab while in the **Restore from Existing Site** step and follow the given steps:

![Migrate from Site URL](https://frappecloud.com/files/migrate_from_site_url.png)



- Enter your existing site URL
- Enter your old site user credentials
- Click on Get Backups

Get Backups will fetch backup files from your old site to restore on Frappe Cloud.

## FAQ

### tar/gzip command fails with unexpected EOF

This is a common error faced by many users. We believe this happens due to a corrupt file in the tarball. If this happens to you during site restore, please try again with a fresh backup of the site.

> If you continue to face the error with fresh backup. Try taking a backup **after** putting your site on maintenance mode.





### Uploading a files backup that's too large

> **Try the [FC Restore CLI](https://3fa1496a-d896-450b-98e8-d2029aa5499e.frame.claudeusercontent.com/_f/1784265986-d887/#migrate-using-fc-restore-cli) first.** It's the supported way to restore backups larger than the 5 GiB upload limit, and it handles the database and files together. Only use the steps below if the CLI tool also fails for you, and you're on a [private bench group](https://docs.frappe.io/cloud/benches/create-new).

If your files are too large to upload from the UI, the site is no longer hosted anywhere (so **Migrate using site URL** and **Migrate using Bench** are out), and the FC Restore CLI hasn't worked either, you can restore the database from the UI and upload the files separately over SSH.

1. Restore the database first. In the restore dialog, upload only the database backup and leave the public and private files empty. The database is small enough to go through the UI, and restoring it creates the site so there's somewhere for the files to land.
2. Upload the files backup to Google Drive, then **Copy link** and set access to "Anyone with the link".
  ![](/files/image1879e9.webp)
  ![](/files/image4dfaf1.webp)
3. [Set up SSH access](https://docs.frappe.io/cloud/benches/ssh) to your bench group and generate an SSH certificate. Connect using the command shown in the SSH Access dialog — it's specific to your bench group and region:
  ```bash
  # Example only — replace with the command from your SSH Access dialog
  ssh bench-0001-000001-f1-mumbai@n1-mumbai.frappe.cloud -p 2222
  ```
4. Go to your site's directory and download the files backup:
  ```bash
  cd sites/<your-site>

  # Replace this link with your link
  LINK='https://drive.google.com/file/d/1A2b3C4d5E6f7G8h9I0jK1L2m3N4o5P6q/view?usp=sharing'

  wget --no-check-certificate -O files.tar \
    "https://drive.usercontent.google.com/download?id=$(echo "$LINK" | grep -oE '[-_A-Za-z0-9]{25,}')&export=download&confirm=t"

  ```
5. Look inside the archive before extracting. The paths tell you how many leading directories to strip:
  ```bash
  tar -tf files.tar | head
  ```
  A files backup is laid out with the site name above `public/files`, so you'll see something like:
  ```
  ./your-site.frappe.cloud/public/files/
  ./your-site.frappe.cloud/public/files/some-image.png

  ```
  Everything before `public` gets stripped — here that's `./` and the site name, so two components.
6. Extract the files into place:
  ```bash
  tar -xvf files.tar --strip-components=2

  ```
  For a `.tar.gz` backup, use `tar -xzvf` instead. Repeat steps 4 to 6 for the private files backup.
7. Check it landed, then clean up:
  ```bash
  ls public/files private/files
  rm files.tar
  ```
  You should see your files directly under `public/files`. If you see your site name nested in there instead, the strip count was off by one — delete the stray directory and re-extract with a different `--strip-components` value.

<!-- page: cloud/cloud__sites__monitoring.md -->
---
title: "Monitoring"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/monitoring"
updated: "2026-08-25"
---

Frappe Cloud collects metrics while your site runs: request counts, request duration, background jobs, CPU time, and uptime. You read them on the **Analytics** tab of your site.

## Site Analytics

To open the charts, go to your site in the dashboard and click the **Analytics** tab.

The tab opens with six charts:

| Chart | What it shows |
| --- | --- |
| **Daily Usage** | Cumulative CPU time of the requests today. The line marks your daily CPU limit. Watch this chart to know when to upgrade the plan. |
| **Uptime** | Uptime of the web worker and the scheduler. The monitor server probes the site every minute. |
| **Requests** | Number of requests per minute. |
| **Requests CPU Usage** | CPU time that the requests used. |
| **Background Jobs** | Number of background jobs. |
| **Background Jobs CPU Usage** | CPU time that the background jobs used. |

![](/files/image3c0c87.png)

Two controls at the top of the tab change what all charts show:

- **Absolute from ... to ...** sets a start date and an end date.
- **Relative** sets a period that ends now, for example the last 24 hours.

You can also drag across a chart to zoom into a shorter period.

Note: Analytics start only after you complete the Setup Wizard on the site.

## Investigating high usage

The charts that name your slow endpoints are under **Advanced Analytics**. This section is closed by default.

1. Open the **Analytics** tab.
2. Scroll below the first charts, to the heading **Advanced Analytics**.
3. Click the heading. The section opens and loads the charts.

The section holds these charts:

- **Frequent Requests** and **Slowest Requests**, by path.
- **Frequent Background Jobs** and **Slowest Background Jobs**, by method.
- **Requests by IP**.
- **Frequent Slow Queries** and **Top Slow Queries**.
- Duration charts for the paths that are slow most often. They appear only when that path is slow on your site. One chart names the reports, one names the document methods, and two name the doctypes and the actions of the saved documents.

![](https://cloud.frappe.io/files/gszsZA1.png)

The list is sorted, so the first entry is the slowest. The long red bars are the paths to examine.

![](https://cloud.frappe.io/files/xKtypi1.png)

To read these charts and to act on them, see [Site Slow: 504 Gateway timeout](/cloud/site/common-issues/site-slow-504-gateway-timeout).

## Database Storage Usage

Frappe Cloud syncs the database usage of your site every 6 hours.

### How to refresh the database usage on demand

If you changed data and want the current number, start a refresh yourself. You can do this from the **Site Overview** page or from the **DB Analyzer**.

The refresh also purges the Information Schema cache. After the refresh, the usage from Frappe Cloud and from the DB Storage Report of the framework agree.

Note: You can refresh once every 15 minutes.

![](/files/imagecdfe78.png)

![](/files/image4e6986.png)

### Why Frappe Cloud and the storage reports disagree

The number from Frappe Cloud can differ from the DB Storage Report of the framework, and from the DB Analyzer.

Frappe Cloud reads the table sizes with its own parser. The parser does not use cached data, and it does not slow the database down.

The DB Storage Report and the DB Analyzer read the Information Schema tables of MariaDB. MariaDB caches that data and refreshes it only in some conditions. The reports can therefore show old numbers.

To make the numbers agree, refresh the database usage from the **Site Overview** page or from the **DB Analyzer**.

## Monitoring Disabled

A monitoring server tests every minute if your site is online. It sends a request to the primary domain of the site:

```
https://example.com/api/method/ping
```

The site must answer with an HTTP 200 status code and this body:

```json
{"message": "pong"}
```

### Why monitoring becomes disabled

Frappe Cloud turns monitoring off when the ping does not arrive, and sends you a mail. These are the common causes:

- The primary domain expired.
- The DNS records are incorrect.
- Cloudflare, or another CDN in front of the site, blocks the request.
- A custom app makes the ping endpoint fail.

### How to enable monitoring again

1. Open the **Site Overview** page of your site.
2. Click **Enable Monitoring** at the top of the page. The dialog shows why monitoring stopped.
   ![shapes at 25 10 08 15.06.33](/files/shapes%20at%2025-10-08%2015.06.33.png)
   ![Screenshot 2025 10 08 at 15 07 33 Frappe Cloud](/files/Screenshot%202025-10-08%20at%2015-07-33%20Frappe%20Cloud.png)
3. Click **Check & Enable Monitoring**.
   ![Screenshot 2025 10 08 at 15 12 42 Frappe Cloud](/files/Screenshot%202025-10-08%20at%2015-12-42%20Frappe%20Cloud.png)

If the test fails, the dialog shows the cause and the correction.

<!-- page: cloud/cloud__sites__move-site-across-region.md -->
---
title: "Move site across region"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/move-site-across-region"
updated: "2026-03-07"
---

**Note:** This option is now part of the **Site Migration** feature.

For instructions on moving a site to a different region, see the documentation : [https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-region](https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-region)



---

You can directly schedule Site Migration across region from a site's dashboard.

> Sites on public bench groups won't be able to add region to the bench group. Contact us [support.frappe.io](http://support.frappe.io) to add them.

1. Go to your site Dashboard → Actions → Change Region.

![](/files/KcGOWHr.png)

2. Select the region you want to migrate your site.

![](/files/J5U1RO6.png)





> If the region is not available, you can add a region to your bench group from your Bench group dashboard → Regions → Add Region. 
>
> ![](/files/xLETGai.png)
>
>

3. If the region is available in the current bench group, input an appropriate date and time (leave it untouched if you want the migration to happen immediately) and then click on Change Region and the Site Migration will be done in the scheduled time.

![](/files/Ru01b7n.png)
