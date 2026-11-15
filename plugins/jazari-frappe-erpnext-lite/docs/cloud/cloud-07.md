<!-- Frappe documentation: cloud, part 7 of 9. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__servers__instance-types.md -->
---
title: "Server Instance Types"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/instance-types"
updated: "2026-02-16"
---

## Dedicated Instance

With **dedicated instances**, the underlying virtual machine provider allocates a fixed set of resources exclusively for your workload. These resources are reserved for you alone, and even if your server is not fully utilizing them, they remain available at all times.

Because of this, dedicated instances are well suited for workloads that require consistently high CPU and memory usage or need to handle sudden traffic spikes. The guaranteed resources ensure stable and predictable performance without interference from other tenants.

## Shared Instance

With **shared instances**, the virtual machine runs on infrastructure where resources are shared among multiple tenants. For example, your instance may be allocated 2 vCPUs, but if other virtual machines on the same physical host require more resources, your instance’s performance may be affected.

Shared instances typically support **CPU bursting**, which allows you to fully utilize the allocated vCPUs for short periods of time. However, sustained high usage (e.g., running at full CPU 24/7) is not guaranteed. Once usage exceeds a certain threshold, the cloud provider may throttle CPU performance.

#### Provider-Specific Details :

For a deeper understanding, refer to the official documentation from cloud providers:

- Hetzner : [https://docs.hetzner.com/cloud/servers/faq/](https://docs.hetzner.com/cloud/servers/faq/)
- Amazon : [https://www.amazonaws.cn/en/ec2/spot-instances/faqs/](https://www.amazonaws.cn/en/ec2/spot-instances/faqs/)

#### **Limited Support:**

Shared instances can have variable performance. If your server hits certain thresholds, the machine may throttle, and there is no reliable way to determine whether site slowness is due to an application-level issue or a server-level issue.

Therefore, if your site on a shared instance faces performance issues, we will not be able to provide support for those cases.

We recommend using **Shared Instances** for **development** and **UAT** environments. For **production workloads**, it is strongly advised to use **Dedicated Instances** to ensure consistent performance and reliable support.

## Unified Server

Previously, Frappe Cloud dedicated setups required **two separate servers**:

- One server for the application (benches)
- One server for the database

You can now choose a **Unified Server** setup, where both the application (benches) and the database run on the **same server**.

This simplifies the architecture and enables you to run a dedicated setup at a **lower cost**.

[Screenshot on the live page]
*Architecture for Unified Server*

Unified servers are now available for all cloud providers on Frappe Cloud.

<!-- page: cloud/cloud__servers__new.md -->
---
title: "Creating new server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/new"
updated: "2026-05-22"
---

From the [Servers](https://frappecloud.com/dashboard/servers) tab on the dashboard, click on **New** **Server.** 

[Screenshot on the live page]





Enter the **Server Name.** 

[Screenshot on the live page]





Select the **Cloud Provider**. (Note - [Click here](https://docs.frappe.io/cloud/servers/provider-comparision) to know how providers differ from each other)

[Screenshot on the live page]



Select the **Region**. 

[Screenshot on the live page]



Select the **Deployment Mode**. 

- Unified Server - Appropriate for most small and medium business workloads. 
- Separate Server - Recommended for enterprise workloads that may need separate scaling for Application and Database in future.

[Screenshot on the live page]



Select the **Service Type**. 

- Standard - Regular SLA
- Premium - Priority SLA and Performance Consulting (Recommended for Large Enterprises)

[Screenshot on the live page]



Select the desired **Application Server configuration**. 

[Screenshot on the live page]



Select the desired **Database Server configuration**. (Note - This step is applicable only if you have chosen "Separate Server" as the Deployment Mode).

[Screenshot on the live page]



Click the checkbox to **Enable Auto Add-on Storage** if you wish to allow automatic scaling of Application and Database Servers based on usage. (Note - This option is available only on select cloud providers.)

[Screenshot on the live page]

Review the Server Configuration and click the checkbox to provide **Consent for Local Compliances** and click on **Create Server**.

[Screenshot on the live page]



A new server will be created based on the selected configuration. It takes 5-10 mins to complete the creation. 



You can check the **Plays** tab to track the progress. (Note - Notice the "Installing" status on the top bar.)

[Screenshot on the live page]



Once the server is created, the status will turn to "Active". You can start working with the server now. 

[Screenshot on the live page]

<!-- page: cloud/cloud__servers__new_bench.md -->
---
title: "Creating new Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/new_bench"
updated: "2026-02-16"
---

From the server dashboard go to Bench Groups and click on New Bench Group [Screenshot on the live page]  
Choose the version for which you want to create a new bench group, enter the title for the new bench group, check the "I agree" box, and then click on "Create Bench Group."  
[Screenshot on the live page]  
  
Follow steps mentioned in [Private Bench Groups > Creating a new bench group](https://frappecloud.com/docs/benches/create-new).

<!-- page: cloud/cloud__servers__other-information__faqs-server.md -->
---
title: "FAQs - Server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/other-information/faqs-server"
updated: "2026-02-16"
---

### How many servers do I buy? Do I need to buy 2?

Yes, you always need to buy pair of servers:

- Application: This is where your code and your "site" directory will sit. All your attachments (photos, videos) will go here unless configured otherwise. Eg: [s3-attachements](https://github.com/shridarpatil/Frappe-attachments-s3)
- Database: This is where your database (MariaDB) and all "doctype" data will sit.

### How many bench groups can I create? Can I create testing and production bench group on same server?

You can create as many bench groups as you want on your server. Though the performance will get affected as you create many. [Here](https://frappecloud.com/docs/servers/guidelines-for-choosing-a-server-plan) is a guide for the same

<!-- page: cloud/cloud__servers__other-information__on-prem-failover-setup.md -->
---
title: "On-Prem Failover Setup"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/other-information/on-prem-failover-setup"
updated: "2026-04-08"
---

This feature enables you to replicate data from your Frappe Cloud–hosted dedicated servers to servers hosted by you (on-premises or external infrastructure).

In the event of a disaster - such as physical hardware failure in cloud infrastructure or international network disruptions, you can initiate a failover without requiring internet access.

### **Important Points**

- **Supported Architecture Only :** This feature works **only with a separate app server and database server setup**. If you are currently using a unified server, you must first migrate to a separated architecture.
- **Pricing :** This feature is in beta and currently **free of charge** due to recent geopolitical issues. However, it will become **chargeable in the future**, and customers will be notified in advance via email.
- **Access To Feature :** The feature is **disabled by default** for all servers. To enable it, you must create a support ticket at : **support.frappe.io**, including the list of servers where you want this feature activated. 
- **What is On-Prem Server :** An on-prem server refers to any server that you manage outside of Frappe Cloud. This can be : A physical server with internet connectivity or A virtual server hosted on another cloud provider (e.g., AWS, GCP, etc.).  
Frappe Cloud does not provision or manage these servers - you are responsible for setting them up and maintaining them.
- Frappe Cloud does **not monitor or manage** the health or state of your on-premises or external servers as of now. You are responsible for ensuring that those systems remain operational and properly maintained.

### Architecture

[Screenshot on the live page]

Frappe Cloud sets up a dedicated WireGuard P2P mesh between:

- Frappe Cloud app server
- Database server
- Your on-premise server

Afterwards, Frappe Cloud will setup a database replica to your on-prem server and sync all docker images and bench data to your on-premise server. 

### Setup Guide

Once support enables the feature, you will see **“Manage On-Prem Replication”** under server actions.

[Screenshot on the live page]

Click **Manage** to view the setup guide for connecting your on-prem server to Frappe Cloud.

[Screenshot on the live page]

Complete the on-prem setup and initiate the replication setup from the UI.

[Screenshot on the live page]

You can track progress on the same page.

[Screenshot on the live page]

Once successful :

- All existing data will be synced to your on-prem server
- New data will continue to sync automatically

If the setup fails, reach out to **support.frappe.io**.

### Performing Failover

After setup, a small daemon runs on your on-prem server to assist with failover.

**Access the dashboard at :**  `http://<your_on_prem_server_ip_address>:5000`

[Screenshot on the live page]

From the dashboard, you can :

- Monitor benches and sites
- Click **Configure Sites And Start Benches**  to
  - Stop replication
  - Start serving sites from the on-prem server

Once completed, each site will be accessible on a specific port.

[Screenshot on the live page]

**Example:** To access `test-failover-1.nbg.frappe.cloud`, you have to visit `http://<your_on_prem_server_ip>:8394`

### Stop Replication

If you want to stop syncing changes from Frappe Cloud to your on-prem server, use the **Stop Replication** option.

[Screenshot on the live page]

<!-- page: cloud/cloud__servers__plan.md -->
---
title: "Change plan"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/plan"
updated: "2026-02-16"
---

Server Plan
-----------

You can change your server plan to resize the server. Application and Database server plans can be changed independently.


> Note: Changing plan will result in a minor (~5 minutes) downtime on the server.
> 
> 

Go to the Server Overview tab and find the Plan card. Click on **Change** button.

[Screenshot on the live page]  


Choose new plan. Click on Change plan.

### AWS Instance types

For all regions other than KSA, we currently use AWS VMs for dedicated servers. The instances seen in the above plan correspond to `c6i`, `m6i` and `r6i` machines as seen [here](https://aws.amazon.com/ec2/instance-types/)

In general, the CPU:Memory ratio vary across these instances:

  
c6i: These are Compute optimized instances where CPU:Memory ratio is 1:2

m6i: These machines have CPU:Memory ratio of 1:4 (General Purpose)

r6i: These have CPU:Memory ratio of 1:8 (Memory optimized)

Storage Add-on Plan
-------------------

You can increase the storage of your server without upgrading your server's plan through Storage Add-ons. To buy Storage Add-on

1. Go to the Server Overview and click on the + button beside storage[Screenshot on the live page]
2. Select the amount of storage you want to buy and click on confirm

[Screenshot on the live page]


> Note: You can't reduce/revert the storage you've bought for your server
> 
> 

<!-- page: cloud/cloud__servers__provider-comparision.md -->
---
title: "Cloud Provider Comparison"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/provider-comparision"
updated: "2026-04-14"
---

Although all cloud providers allow you to deploy any kind of bench and sites, some advanced features may not be available on all providers. Please refer to the comparison matrix below for a better understanding.



## Comparison Matrix


| Feature                                                            | AWS                      | OCI                   | Hetzner                                                       | Frappe Compute                      |
| ------------------------------------------------------------------ | ------------------------ | --------------------- | ------------------------------------------------------------- | ----------------------------------- |
| Basic Functionalities (Analytics, Monitoring, Server Management)   | Yes                      | Yes                   | Yes                                                           | Yes                                 |
| Add-on Storage (Add more disk space without upgrading server plan) | Yes                      | Yes (Requires Reboot) | No (Support planned for the future)                           | No (Support planned for the future) |
| Disk Size Reduction                                                | Yes (Mumbai Region Only) | No                    | No                                                            | No                                  |
| Restriction on Plan Downgrade                                      | No                       | No                    | Partially (Cannot downgrade to a plan with smaller disk size) | No                                  |
| Automated Disk Snapshot (Retention Window – 2 days)                | Yes                      | Yes                   | Yes                                                           | No                                  |
| Server Snapshot (Allows automated recovery)                        | Yes                      | No                    | No                                                            | No                                  |
| App Server Auto Scaling [Beta]                                     | Yes                      | Yes                   | No (Support planned for the future)                           | No (Support planned for the future) |
| Physical Backup for Large Sites during Site Update / Migration     | Yes                      | No                    | No                                                            | No                                  |
| Support                                                            | L1 & L2 (FC + Apps)      | L1 & L2 (FC + Apps)   | L1 & Limited L2 FC*                                           | L1 & Limited L2 FC*                 |


**covers only incidents on Frappe Cloud (no bug fixes or support for apps or Frappe Framework)* 



## Support

For the **Shared Instance** plan, we provide **limited L2 Frappe Cloud (FC) support**.

Shared instances can experience variable performance. If the server reaches certain thresholds, it may be throttled, and there is no reliable way to distinguish whether performance degradation is caused by application-level issues or underlying server-level constraints.

As a result, if your site encounters performance-related issues while running on a shared instance, we will not be able to provide support for those cases.

We recommend using **Shared Instances** primarily for **development** and **UAT** environments. For **production workloads**, it is strongly recommended to use **Dedicated Instances** to ensure consistent performance and full support coverage.



## FAQ

1. **Why is there no Add-on Storage support on Hetzner ?**
  Hetzner machines usually come with a single root disk by default. Increasing disk size requires upgrading the server plan. We plan to add support for this in the future.
2. **Why does only AWS Mumbai support disk size reduction ?**
  No upstream cloud provider natively supports disk size reduction. Frappe Cloud implements this feature, but it relies heavily on multiple EBS disks. During the ARM migration on the Mumbai cluster, all servers were migrated to a dual-disk setup, which enables disk size reduction only on AWS Mumbai servers.
3. **Why is there a restriction on plan downgrade on Hetzner ?**
  This is an upstream limitation. On Hetzner, the root disk size increases with the plan size. If you upgrade the disk during a plan change, you cannot downgrade to a plan with a smaller disk. As an alternative, choose **CPU and Memory Only Upgrade** during a site plan upgrade.
4. **Why are Server Snapshots not available on OCI and Hetzner ?**
  Server Snapshots are different from Disk Snapshots. This feature allows users to take on-demand snapshots and restore servers directly from them, and it relies heavily on AWS APIs. Due to technical limitations, it is not yet available on OCI and Hetzner.  
   **Note:** We always keep snapshots of the entire machine for the last 2 days. In case of any issue, we can restore your server from these snapshots, although they are not visible on the dashboard.
5. **Why doesn’t Hetzner have the Auto Scaling feature ?**
  Auto Scaling is a relatively new feature and is still in beta. It has currently been rolled out only for AWS and OCI servers. Support for Hetzner will be added once Auto Scaling becomes stable across providers.
6. **Why is Physical Backup available only in AWS regions ?**
  Database Physical Backup heavily depends on AWS EC2 and EBS snapshot features, which is why it is not yet available on other providers. Where Physical Backup is unavailable, we use Logical Backup instead. The main drawback is that backups during updates or migrations of large sites can take longer.
7. **What is the "Frappe" Cloud Provider?**
  Frappe is coming up with its own hosting provider. This is currently in the early stage and gives very few guarantees.

<!-- page: cloud/cloud__servers__servers-introduction.md -->
---
title: "Introduction"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/servers-introduction"
updated: "2026-02-16"
---

Unlike with Public or Private benches, with Servers on Frappe Cloud you now get dedicated compute resources for your sites. Even on private benches, your bench is still on a shared server consuming shared resources along with other benches. This is not the case here.

Servers on Frappe Cloud come in pairs (Application + Database), both the servers can have different plan/size, however both are created within the same region.

Since you're paying for the servers, sites on these servers don't cost you anything extra. That means you can run as many sites and bench groups as you want on these servers.

All other features like [Private Bench Groups](https://frappecloud.com/docs/benches), [SSH Access](https://frappecloud.com/docs/ssh), Database Access work as is with servers. All Frappe Cloud servers are powered by AWS (Amazon Web Services) EC2 instances.

<!-- page: cloud/cloud__setup-webhook.md -->
---
title: "Webhook Implementation"
space: "Cloud"
url: "https://docs.frappe.io/cloud/setup-webhook"
updated: "2026-04-29"
---

Webhook Payload Format
----------------------

Webhook requests are sent as POST requests, and the body contains the following information:


```
{
  "event": "Site Plan Change",
  "data": {
     // details of the resource
  }
}
```
Prerequisites
-------------

1. Your backend service should be up and running to accept incoming webhook requests.

  


At minimum, You need to handle `Webhook Validate` event to be able to validate and activate the webhook.

  


Here, it's a tiny flask app to get started with webhook -


```
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_json()
    event = payload['event']
    data = payload['data']

    print(f"Event: {event}")
    print(f"Data: {data}

")

    # This event is sent by FC at the time of webhook validation
    if event == "Webhook Validate":
        return 'OK'

    # Its just for demo purpose, you can write your business logic here
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
```
2. Your backend should be publicly accessible.

Setup Guide
-----------

1. Visit `Developer Settings` inside Frappe Cloud dashboard (&lt;https://frappecloud.com/dashboard/settings/developer&gt;)
2. Click on `Add Webhook` button
3. Put your backend endpoint and select at-least one webhook event and submit.


&gt; The `Secret` will be used for webhook authentication. This is an optional field.
&gt; 
&gt; Check the [Authentication](#authentication) section to learn more about this.
&gt; 



[Screenshot on the live page]

4. Next, click on the `Activate` button of webhook record.

[Screenshot on the live page: Screenshot 2024-09-25 at 4.29.43 PM]
5. Click on `Validate Webhook`
6. If everything looks good, you can activate the webhook from there

  


[Screenshot on the live page: Screenshot 2024-09-25 at 4.32.06 PM]  


  


Similarly, you will see one event on your backend -


```
Event: Webhook Validate
Data: {}
127.0.0.1 - - [24/Sep/2024 13:25:33] "POST /webhook HTTP/1.1" 200 -
```
7. Click on `Activate Webhook` to make it active.
8. That's all !

Authentication
--------------

You can configure a secret key for authentication at the time of webhook creation or use the `edit` option to update that

If you have provided secret key, Frappe Cloud will set that secret key in `X-Webhook-Secret` header of all webhook requests.

We can modify the tiny flask app to handle webhook authentication -


```
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # authorise webhook requests
    secret = request.headers.get('X-Webhook-Secret', "")
    if secret != "super-secret-key":
        return 'Unauthorized', 401

    payload = request.get_json()
    event = payload['event']
    data = payload['data']

    print(f"Event: {event}")
    print(f"Data: {data}")

    # This event is sent by FC at the time of webhook validation
    if event == "Webhook Validate":
        return 'OK'

    # Its just for demo purpose, you can write your business logic here
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
```

<!-- page: cloud/cloud__signup-login__notifications.md -->
---
title: "Notifications"
space: "Cloud"
url: "https://docs.frappe.io/cloud/signup-login/notifications"
updated: "2026-02-16"
---

You can customize the email addresses used for different types of notifications.  

Depending on where you want to apply the configuration, refer to the appropriate documentation below:

- **Team level:** [Notification Configuration for Teams](https://docs.frappe.io/cloud/notification-configuration)  
- **Site level:** [Site Notification Configuration](https://docs.frappe.io/cloud/site-notification-configuration)  
- **Server level:** [Server Notification Configuration](https://docs.frappe.io/cloud/server-notification-configuration)

<!-- page: cloud/cloud__simplified-login-to-frappe-cloud-dashboard.md -->
---
title: "Login from Frappe apps"
space: "Cloud"
url: "https://docs.frappe.io/cloud/simplified-login-to-frappe-cloud-dashboard"
updated: "2026-05-22"
---


> This feature is only available for sites created through SaaS flow (i.e. [frappecloud.com/erpnext/signup](http://frappecloud.com/erpnext/signup)).
> 
> 

1. Go to desk of your site.
2. Click on `Login to Frappe Cloud` button inside the menu.

[Screenshot on the live page: Screenshot 2024-10-28 at 5.50.14 PM]
3. It will take few seconds to initiate the login request, after that you will be presented a modal like this

[Screenshot on the live page: Screenshot 2024-10-28 at 5.51.08 PM]
4. Check your mailbox. You will recieve an e-mail with a verification code.

[Screenshot on the live page: Screenshot 2024-10-28 at 5.51.51 PMb]
5. Put the verification code in input box and click on `Verify`  
[Screenshot on the live page: Screenshot 2024-10-28 at 5.52.15 PM]
6. You should be now logged-in and redirected to Frappe Cloud dashboard

[Screenshot on the live page: Screenshot 2024-10-28 at 5.52.58 PM]
7. You will also get a `Login Successful` banner

[Screenshot on the live page: Screenshot 2024-10-28 at 5.52.51 PM]  


  



> Sometimes many browser block url redirection. In that case, there are two solutions -
> 
> 
> 	1. Tap on `Click Here to login` link inside the modal.
> 	
> 	[Screenshot on the live page: Screenshot 2024-10-28 at 5.52.51 PM]
> 	2. Your browser will show a message that popup has been blocked. This message can be vary based on the browser.
> 	
> 	[Screenshot on the live page: Screenshot 2024-10-28 at 5.52.36 PM]  
> 	
> 	
> 	In case of firefox, you can choose `Show https://....` option.

<!-- page: cloud/cloud__site-notification-configuration.md -->
---
title: "Notification Configuration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site-notification-configuration"
updated: "2026-02-16"
---

You can configure multiple notifications at the site level to ensure that mails are delivered through the right channels.

### Accessing Notification Settings

- Go to Site Overview → General Actions.
- Under Notification Settings, click `Manage` to open the configuration screen.


[Screenshot on the live page]

### Configuring Notifications

The Notification Configuration screen allows you to set up how and where notifications are sent.

[Screenshot on the live page]


### Notification Flow Logic

The notification delivery follows a top-down hierarchy:

- Check if a specific notification type (e.g., Billing, Incident) is configured.
- If not found, use the General notification configuration.
- If General is also not configured, fallback to the Team-level configuration.



[Screenshot on the live page]

<!-- page: cloud/cloud__site-process-list.md -->
---
title: "Site Process List"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site-process-list"
updated: "2026-02-16"
---

You can view running mariadb queries in your site by opening **Insights** tab, and then **Reports ->**  **Process List Report**

[Screenshot on the live page]  


[Screenshot on the live page]  


You'll see running queries in the above page when using your site

<!-- page: cloud/cloud__site__common-issues__500-internal-server-error.md -->
---
title: "500 Internal Server Error"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/500-internal-server-error"
updated: "2026-02-16"
---

This usually indicates an application related issue. If your site is on custom [bench group](https://docs.frappe.io/cloud/benches), then you can investigate the same with:

#### Checking bench logs (Option 1)

1. Go to your site's **Bench Group** dashboard and check **Sites** tab

[Screenshot on the live page]

1. Click on **View Logs**

[Screenshot on the live page]

1. Open **web.error.log** and scroll to bottom. You should be able to see the traceback:

[Screenshot on the live page]
*In this example, the site can't connect to the database server. Restarting the database server might a solution here.*

#### Using SSH Access (Option 2)

Alternatively, you can locate **web.error.log** after SSH Access. Please check the docs [here](https://docs.frappe.io/cloud/benches/debugging)

If you occasionally get a pop-up with the **Internal Server Error** message, it is likely that a background job is failing. In such cases, checking your **Scheduled Job Log, Error Log** and **worker.err.log** file should help.

<!-- page: cloud/cloud__site__common-issues__502-bad-gateway.md -->
---
title: "502 Bad Gateway"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/502-bad-gateway"
updated: "2026-08-12"
---

A 502 error means that the [web workers](https://docs.frappe.io/cloud/servers/guidelines-for-choosing-a-server-plan#gunicorn-workers) of your site are dead, or the app server is dead. The proxy in front of your site got no connection.

**Note:** A slow site gives a 504 error, not a 502. See [Site Slow: 504 Gateway timeout](https://docs.frappe.io/cloud/site/common-issues/site-slow-504-gateway-timeout).

## Step 1: Wait one minute and reload the page

A deploy or a bench restart gives a short 502. If the site opens again, no other action is necessary.

## Step 2: Restart the bench

1. Open your [bench group](https://docs.frappe.io/cloud/benches) dashboard.
2. Go to the **Sites** tab.
3. Click the **⋯** menu of the bench that hosts your site.
4. Click **Restart Bench**.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

If your site is on a shared server, you have no bench group dashboard. Then open a ticket at [support.frappe.io](https://support.frappe.io).

You can also restart the bench over [SSH](https://docs.frappe.io/cloud/benches/ssh):

```
bench restart

```

## Step 3: Read the logs

If the 502 continues after a restart, read the logs of the bench.

1. Go to the **Sites** tab of your bench group.
2. Click the **⋯** menu of the bench.
3. Click **View Logs**.
4. Open `web.error.log`.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

5. Go to the bottom of the file. The last lines show why the workers stopped.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

*In this example, Gunicorn stopped a worker with a* `WORKER TIMEOUT` *error. Then it started a new worker.*

The steps are the same as for a [500 Internal Server Error](https://docs.frappe.io/cloud/site/common-issues/500-internal-server-error). You can also read the logs over SSH. See [Debugging](https://docs.frappe.io/cloud/benches/debugging).

## Step 4: Examine the memory of the server

If the log shows no error, the system stopped the workers before they wrote one. This usually means that the server had no free memory.

1. Open your server dashboard.
2. Go to the **Analytics** tab.
3. Examine the memory graph at the time of the error.

*(screenshot — not bundled; see the live page URL in this file's front matter)*

4. If the memory was full, [change the server plan](https://docs.frappe.io/cloud/servers/plan), or decrease the load on the server.

**Note:** You cannot change the number of workers from the dashboard. The server plan gives the number of workers. If you think that your bench needs more workers, open a ticket at [support.frappe.io](https://support.frappe.io). More workers also need more memory.

<!-- page: cloud/cloud__site__common-issues__lost-connection-to-mysql-server.md -->
---
title: "Lost connection to mysql server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/lost-connection-to-mysql-server"
updated: "2026-02-16"
---

```
MySQLdb.OperationalError: (2013, 'Lost connection to server during query')
```

You may see this error when **restoring** a site or during an **update site migrate** job. This likely happened as the mysql server restarted as it didn't have sufficient memory for the operation. Changing the **database server** plan for more memory should fix this. To change plan of your dedicated database server, refer [this guide](https://frappecloud.com/docs/servers/plan)

<!-- page: cloud/cloud__site__common-issues__request-timeout-server-was-too-busy-to-process-this-request.md -->
---
title: "Request Timeout: Server was too busy to process this request"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/request-timeout-server-was-too-busy-to-process-this-request"
updated: "2026-08-24"
---

# Request Timeout: Server was too busy to process this request

*(screenshot — not bundled; see the live page URL in this file's front matter)*

The server was not busy. A query waited for a row lock, and MariaDB stopped it after 50 seconds with error 1205, `Lock wait timeout exceeded`. Another transaction held that lock. This is a bug in the application, not a limit of the plan.

## Find the cause

1. Do the action a second time. While it runs, open the [process list](https://docs.frappe.io/cloud/site-process-list) of your site. The list shows the query that waits and the query that blocks it.
2. If the process list is empty, read the [slow queries](https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site) of your site.
3. Search the Error Log for `QueryTimeoutError`. The traceback names the code that failed.

A new [controller hook](https://docs.frappe.io/framework/user/en/basics/doctypes/controllers#controller-hooks) or [scheduled job](https://docs.frappe.io/framework/user/en/api/background_jobs) is the usual cause.

## Correct it

- Keep transactions short. Do the slow work first, then write to the database.
- Update rows in batches. Commit after each batch.
- If two jobs write to the same document, run them one after the other.

<!-- page: cloud/cloud__site__common-issues__site-slow-504-gateway-timeout.md -->
---
title: "Site Slow: 504 Gateway timeout"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/site-slow-504-gateway-timeout"
updated: "2026-08-25"
---

A 504 error means that the proxy waited too long for an answer from your site. All [web workers](https://docs.frappe.io/cloud/servers/guidelines-for-choosing-a-server-plan#gunicorn-workers-or-web-workers) were busy with earlier requests. A slow API causes this, most often a report that takes too long to run.

When the workers stay busy, the bench can go down and the site stops.

Note: A dead web worker gives a 502 error, not a 504. See [502 Bad Gateway](/cloud/site/common-issues/502-bad-gateway).

## Find the slow endpoint

1. Open the **Analytics** tab of your site.
2. Click the heading **Advanced Analytics**. The section is closed by default.
3. Read the **Slowest Requests** chart. It groups the request time by path.
4. Read the duration charts below it. They name the report, the method, or the doctype behind a slow path.

The list is sorted, so the first path is the slowest.

## Common endpoints

| Endpoint | Meaning |
| --- | --- |
| `/api/method/frappe.desk.query_report.run` | A report from the **Report** doctype runs. |
| `/api/method/frappe.desk.reportview.get` | A list view or a report view loads. Many columns and many filters make this slow. Add [indexes](https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site#adding-composite-database-indexes) for the fields in the filters. |
| `/api/method/run_doc_method` | A whitelisted method of a document controller runs. |
| `/api/method/frappe.desk.form.save.savedocs` | A document is saved or submitted. A slow hook or a large child table makes this slow. |

## Slow reports

If `/api/method/frappe.desk.query_report.run` is at the top of the list, your reports are slow. Convert them into [Prepared Reports](https://docs.frappe.io/erpnext/prepared-report). A Prepared Report runs in the background, and the site stays free for other requests.

The **Query Report Durations** chart names the reports that take the most time.

[Screenshot on the live page]

## What does "Other" mean in chart

The **Other** bucket holds all requests that are not in the top slowest paths.

When **Other** is the largest bar, one pattern of endpoint is usually slow. In this example, the `/custom_app/view/` endpoint is slow, and the developer of that app must examine it.

[Screenshot on the live page]

If you see no pattern and **Other** is still the largest bar, the server itself is slow.

## Correct the cause

- Profile the slow endpoint with the [Recorder](https://docs.frappe.io/framework/user/en/profiling) of the framework. Turn the Recorder off when you finish, because it makes the site slower.
- If a slow query causes the delay, add an index. See [MariaDB slow queries in your site](/cloud/faq/mariadb-slow-queries-in-your-site).
- If you cannot make the endpoint faster, move the work into a [background job](https://docs.frappe.io/framework/user/en/guides/app-development/running-background-jobs).
- If you own a dedicated server, open the **Analytics** tab of the server. Read the CPU and Load Average charts of the application server and of the database server. See [Guidelines for choosing a server plan](/cloud/servers/guidelines-for-choosing-a-server-plan).

<!-- page: cloud/cloud__site__common-issues__work-horse-terminated-unexpectedly.md -->
---
title: "Work-horse terminated unexpectedly; Waitpid returned 9/15 (signal 9/15)"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/work-horse-terminated-unexpectedly"
updated: "2026-02-16"
---

You may see this as the output of **RQ Job** . This happens when a background worker gets killed. Usually by the [OOM Killer](https://linux-mm.org/OOM_Killer) as the result of consuming too much memory. In such cases, you may consider optimizing your code to use less memory. If that is not possible, you'll have to upgrade your **application** server for more memory.

<!-- page: cloud/cloud__site__site-migrations__in-place-site-migration.md -->
---
title: "In-Place Site Migration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/in-place-site-migration"
updated: "2026-03-06"
---

In certain situations, you may need to manually run the `bench migrate` command for your site.

> **[Note]** This operation **does not create a backup** before running the migration. Proceed with caution and ensure you have a backup if required.

To run the migration:

1. Open your **Site** page.
2. Go to the **Migrations** tab.
3. Click **Trigger Migration**.
4. Select **In-Place Migrate Site** as the migration type.

Once triggered, that will run the equivalent of the `bench migrate` command on your site.

[Screenshot on the live page]

<!-- page: cloud/cloud__site__site-migrations__introduction-to-site-migration.md -->
---
title: "Introduction to Site Migration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/introduction-to-site-migration"
updated: "2026-03-06"
---

The **Site Migration** feature allows you to seamlessly move your site across benches and servers with minimal effort.

[Screenshot on the live page]

This supports the following migration types :

1. **In-Place Migration** : Run `bench migrate` on your site. *This operation does not take a backup, so use with caution.*
2. **Move Site from Shared to Private Bench**  : Transfer your site from a shared bench to a shared / dedicated private bench.
3. **Move Site to Different Server / Bench** : Relocate your site to another server (both shared and dedicated) on an existing or new bench.
4. **Move Site to Different Region** : Migrate your site to a server located in a different geographic region.

#### Bench Selection During Migration :

For most migration types, you can choose one of the following options : 

1. **Select an Existing Bench** : Move your site to an already available bench.
2. **Clone and Create a New Bench Automatically** : Automatically creates a new bench with the same configuration and apps as the current one.

In the next pages, we will cover the details of each migration type.

<!-- page: cloud/cloud__site__site-migrations__move-site-from-shared-to-private-bench.md -->
---
title: "Move Site From Shared To Private Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/move-site-from-shared-to-private-bench"
updated: "2026-03-06"
---

If your site is currently running on a **shared bench**, you can move it to a **private bench** to gain access to **Server Scripts**, install **custom apps**, and have better control over your bench environment.



1. **Verify Plan Eligibility :** First, confirm that your **site plan supports private benches**. If your current plan does not support this feature, a **banner will appear on the site page** indicating that an upgrade is required. Click the **Upgrade Plan** button to proceed.
  [Screenshot on the live page]
2. **Upgrade Your Plan :**  To enable private bench support, upgrade your site to **any plan priced at $25/month or higher**.
  [Screenshot on the live page]
  After upgrading, a new banner will appear on the site page prompting you to move the site. Click **Move to Private Bench**.
  [Screenshot on the live page]
3. **Confirm the Migration Configuration :** A dialog will appear with **pre-filled configuration details** for the migration.  
In most cases, you can keep the default values and click **Move to Private Bench** to proceed.  
  [Screenshot on the live page]
  Additional options are also available in the dialog, such as - Moving the site to a dedicated server or to an existing bench. You can explore these options if your setup requires a different configuration.  

4. **Track the Migration Progress :** After triggering the migration, you will be redirected to a **progress page** where you can monitor the status of the operation.
  [Screenshot on the live page]
5. **Migration Completion :** Once the migration process finishes, your site will be running on a **private bench** according to the selected configuration.
  [Screenshot on the live page]
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

[Screenshot on the live page]

### 2. Wait for Bench Provisioning

After adding the region, return to the **Sites** tab.

A **new bench** will appear with the status **Installing**. Wait until the bench becomes **Active** before proceeding.

[Screenshot on the live page]

### 3. Trigger the Migration

Once the bench becomes active, open your **Site** and go to the **Migrations** tab.

Click **Trigger Migration**. From the migration type options, select **Move Site to Different Region**, then choose the **target region** where you want the site to be moved.

[Screenshot on the live page]

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

[Screenshot on the live page]



## **Choose a Migration Option**

You will see two available options :

### 1. Use New Bench

Select this option if you want to **create a new bench** and move your site there.  
When choosing this option, you can deploy the new bench in one of two ways :

- **Shared Server** – Create the new bench on a shared server (managed by Frappe).
- **Dedicated Server** – Deploy the new bench on a dedicated server.

After selecting your preferred configuration, click the button to **proceed with the migration setup**.

[Screenshot on the live page]

**Note:** If you are moving your site **from dedicated server to shared server**, the system will set **100 USD** as **default plan** after migration. Thereafter, you can upgrade / downgrade site plan according to your requirement.

### **2. Use an Existing Bench :**

Select this option if you already have a **bench with the required apps installed**.

You will need to :

- Select the **bench**
- Select the **server where the bench should be deployed**

After selecting the appropriate options, click the button to **proceed with the migration configuration**.

[Screenshot on the live page]

<!-- page: cloud/cloud__sites__activity.md -->
---
title: "Activity"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/activity"
updated: "2026-02-16"
---

Frappe Cloud maintains a log of all actions taken on your sites.




[Screenshot on the live page]

All actions taken on the sites from the dashboard or triggered directly by the system are logged in Frappe Cloud. This log may be viewed from your site's Activity tab.
