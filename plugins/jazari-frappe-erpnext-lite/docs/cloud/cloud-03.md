<!-- Frappe documentation: cloud, part 3 of 9. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__database-server-actions.md -->
---
title: "Database Server Actions"
space: "Cloud"
url: "https://docs.frappe.io/cloud/database-server-actions"
updated: "2026-08-13"
---

On **Server Actions** page, you will find several options for database configuration.

[Screenshot on the live page: image9765dc]

## What is Binlog &amp; Why It's required ?

The **Binary Log (Binlog)** in MariaDB is a crucial logging mechanism that records all changes to the database - such as SQL statements that modify data (INSERT, UPDATE, DELETE). It does **not** log SELECT queries.

Binlogs are primarily used for:

- **Replication**: Keeping replicas in sync with the primary database.
- **Point-in-time recovery**: Restoring a database to a specific moment in time.

For example, if a site is accidentally deleted or broken due to a faulty SQL query, in that case binlogs combined with the last available backup—allow you to **roll back to a specific time** and recover your data.

## View &amp; Purge Binlogs

You can view binary log file sizes by date. If you're running low on storage, it's possible to **purge old binlogs** that are no longer needed.

[Screenshot on the live page]

[Screenshot on the live page]

[Screenshot on the live page]

## Manage Binlog Retention

By default, when Frappe Cloud provisions a server, MariaDB has a **binlog retention period of 14 days**.

If your site handles a large volume of transactions and binlogs are filling up your storage quickly, you may choose to **reduce the retention period**.

Alternatively, for compliance or auditing purposes, you can **increase binlog retention** as needed.

You can manage these settings directly from the interface:

[Screenshot on the live page]

## Binlog Auto-Purging Based on Size Limit

Binlog files can occasionally grow rapidly, consuming a significant portion of your disk space. If Auto Add-on Storage is not enabled, this may lead to storage exhaustion and potential downtime for your server or application.

The Binlog Auto-Purging feature helps prevent such issues by allowing you to define a size limit for binlogs. When the total binlog size exceeds this limit, the system automatically purges older binlogs to bring usage back within the specified threshold.

[Screenshot on the live page: image3b13b3]

## Enable / Disable Binlog Indexer

The **Binlog Indexer** converts binary logs into a readable, searchable format, allowing end-users to explore and query binlogs using the **Binlog Browser**.

To **enable** the binlog indexer and browser, click on `Enable Binlog Indexer` under `Database Server Actions`, then confirm the action.

[Screenshot on the live page: image16cc0f]

To **disable** the binlog indexer and browser, click on `Disable Binlog Indexer` under `Database Server Actions`, then confirm the action.

[Screenshot on the live page: image7a1581]

## **Default Configuration for Database Servers:**

- When a server is created with Auto Add-on Storage enabled, binlogs can use up to 75% of the total disk capacity.
- When a server is created with Auto Add-on Storage disabled, binlogs can use up to 20% of the total disk capacity.

These are the default limits, but you can adjust them based on your requirements.

**Note :** This feature is not available for database servers configured with replicas.

## Performance Schema

If you own some dedicated server, you can enable/disable the performance schema as per requirement.

[Screenshot on the live page]

## Manage InnoDB Buffer Pool Size

If you want to change innodb buffer pool size, you can now do that from Frappe Cloud dashboard.

[Screenshot on the live page]

## Manage Max Database Connections

When you create a database server, Frappe Cloud set a default max connections based on the total memory on the server. In case if you need more database connection, you can increase that from dashboard.

[Screenshot on the live page]

## View Database Configurations

If you want to check all the configuration of your dedicated database server, you can use the `View Database Configuration` option.

[Screenshot on the live page]

Currently, it's not allowed to change in variable. If you need some special configuration, please reach out to support.frappe.io

## Database Audit Trail

For compliance purposes, if you need a database audit trail, you can enable it from **Server Actions** in the Frappe Cloud dashboard.



Database audit trail has two capture modes:

1. **Only write queries :** Captures queries that modify the database, such as changes to databases, tables, or rows. Read queries are not logged.
2. **Read and write queries :** Captures all queries running on the database, including `SELECT` queries. Since read queries are also logged, the log size can be **at least 3X larger**.

[Screenshot on the live page]

The cost is **2 INR per GB per month**, based on your log's storage usage. All audit logs are uploaded to S3, so they won't use additional disk space on the server.



We recommend keeping **at least 20 GB of free disk space** for audit logging. Audit logs are rotated and uploaded every **2 hours**, so you should have enough free space to store up to 2 hours of logs locally on the server.

### Accessing Database Audit Logs

From the server actions, you can view all the stored audit logs.

[Screenshot on the live page]

You can download the required ones from dashboard itself.

**Sample audit log format -**

```
20260812 06:31:18,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,54,0,CONNECT,_99d3ba2c63387bd7,,0
20260812 06:31:18,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,54,0,DISCONNECT,_99d3ba2c63387bd7,,0
20260812 06:32:01,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,55,0,CONNECT,_99d3ba2c63387bd7,,0
20260812 06:32:01,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,55,621,QUERY,_99d3ba2c63387bd7,'SELECT module,custom,is_tree FROM tabDocType WHERE name='Scheduled Job Type' ORDER BY creation DESC LIMIT 1',0
20260812 06:32:01,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,55,622,QUERY,_99d3ba2c63387bd7,'SELECT * FROM tabScheduled Job Type WHERE stopped=0 ORDER BY creation ASC LIMIT 1000',0
20260812 06:32:01,ip-10-3-4-101,_99d3ba2c63387bd7,ip-10-3-3-101.eu-west-2.compute.internal,55,623,QUERY,_99d3ba2c63387bd7,'SELECT * FROM tabScheduled Job Type WHERE stopped=0 ORDER BY creation ASC LIMIT 1000 OFFSET 1000',0
```

Check the official MariaDB documentation to know more about audit log structure : 

[https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-log-format#audit-log-format-with-syslog](https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-log-format#audit-log-format-with-syslog)

<!-- page: cloud/cloud__database-users-and-permission-manager.md -->
---
title: "Database Users And Permission Manager"
space: "Cloud"
url: "https://docs.frappe.io/cloud/database-users-and-permission-manager"
updated: "2026-03-19"
---

> **Database Access is available for sites on USD 50 and above plans**

## Available Permissions

There are three types of permissions that can be assigned to database users:

1. **Read Only**: The user can view data but cannot modify it. They have access to all tables and columns in the database for reading purposes only.
2. **Read Write**: The user can both view and modify data. They have full access to all tables and columns in the database for reading and writing.
3. **Granular**: This permission mode allows for fine-grained control over a user's access. You can grant access to specific tables and, if needed, even restrict access to specific columns within those tables.

## Manage Database Users

Go to Site Dashboard > Actions > Manage database users

From here, you can view all the existing users of your site's database and manage their permissions and access settings.

[Screenshot on the live page]



## Create Database User

Click on `Add User` button to open the modal for creating database users.

1. **Read Only Mode :**

[Screenshot on the live page]

2. **Read Write Mode :**

[Screenshot on the live page]

3. **Granular Mode :**

> When you begin configuring `Granular Access`, the system will load your database's table schema. This process may take anywhere from 30 seconds to 5 minutes, depending on the number of tables in your database.

You can set the **Read Only** or **Read Write** mode for each table individually. Additionally, if needed, you can restrict access to specific columns within a table by selecting the columns you want to grant access to.





[Screenshot on the live page]

## Edit Database User

If you want to modify the permissions for a specific database user, you can easily do so by selecting the **Configure User** option in the row menu. This will allow you to adjust the user’s access levels and permissions as needed.

[Screenshot on the live page]



You can make the changes to the user's permissions and save them. Once saved, it may take some time for the updates to take effect.

> Please note that if the database user previously had **Read Only** or **Read Write** global privileges, any changes you make to their permissions will not take effect immediately. These changes will only apply to new connections created after the update.

## View Database Credential

Click on the three dots in the row and select **View Credential** to view the details for that specific user’s credentials.

[Screenshot on the live page: Screenshot 2024-12-03 at 12.18.52 PM]



After selecting **View Credential**, a modal will appear displaying all the necessary information to connect to your site database.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]



## Delete Database User

Click on the three dots in the row and select **Delete User** to remove the database user.

[Screenshot on the live page: Screenshot 2024-12-03 at 12.16.58 PM]



When you click to delete a user, a confirmation modal will appear. Once you confirm the deletion, the selected database user will be deleted.

[Screenshot on the live page]



## Access Logs

If you want to view all the SQL query pass through FC SQL Proxy service, you can click on `View Logs` button.

[Screenshot on the live page]

You can filter search result by some keywords or client IP.

[Screenshot on the live page]

## Connect External Tools to the Database

### Connect Popular Analytics or Business Intelligence tool


| **Tool Name**    | **Documentation**                                                   |
| ---------------- | ------------------------------------------------------------------- |
| Frappe Insights  | [Click Here](https://frappecloud.com/docs/frappe-insights)          |
| Metabase         | [Click Here](https://frappecloud.com/docs/connect-metabase)         |
| Apache Superset  | [Click Here](https://frappecloud.com/docs/connect-apache-superset)  |
| Looker Studio    | [Click Here](https://frappecloud.com/docs/connect-looker-studio)    |
| Power BI Desktop | [Click Here](https://frappecloud.com/docs/connect-power-bi-desktop) |
| Zoho Analytics   | [Click Here](https://frappecloud.com/docs/connect-zoho-analytics)   |




### Other Analytics or Business Intelligence tool

Copy the credentials shown to your analytics tool.

We only allow TLS connections. If you're having issues while connecting then please ensure that the analytics tool is using SSL/TLS and our certificate [chain.pem](https://frappecloud.com/files/chain.pem) for `*.frappe.cloud` (Signed by [Let's Encrypt](https://letsencrypt.org/)).

### MariaDB command line client

[Screenshot on the live page: Database Access CLI]



Copy the command to your console and paste the password when prompted.

You will need to install [mariadb-client or mysql-client](https://mariadb.com/docs/server/connect/clients/mariadb-client/) on your machine.









---

## FAQ

## Error when running mysql query

Sometimes you may get errors such as

```
lost connection to server during query
```

In such cases, the application with which you're connecting to the database may not be showing the exact error mysql server is throwing. If you run into any errors when running queries, it's best to try the same query over [mysql client](https://frappecloud.com/docs/sites/database-access#mariadb-mysql-command-line-client) in the command line.  



With the error thrown there, you'll be able to tell what exactly went wrong, and if anything is needed from our end, you can take a screenshot of the same and raise support ticket with it.

## Timezone doesn't match the timezone of the site

The [system-time-zone](https://mariadb.com/kb/en/time-zones/#system-time-zone) mariadb variable will not be set to the timezone you see under System Settings. This is simply because that is not how timezone is implemented in Frappe. This is not an issue.

<!-- page: cloud/cloud__devtools__log-browser.md -->
---
title: "Log Browser"
space: "Cloud"
url: "https://docs.frappe.io/cloud/devtools/log-browser"
updated: "2026-02-16"
---

Log Browser is a handy tool to debug what has happened in your site or bench.

There are 2 modes in Log Browser - Site and Bench

In Site mode you can view and browse through the logs generated by a site and in Bench mode you can view and browse through the logs generated by a bench (not a bench group).

### Steps to use the Log Browser

* Select the mode from the dropdown.
* Select the site/bench you want to view logs from the dropdown in the top right corner

[Screenshot on the live page]
* Select the log you want to view from the log list

[Screenshot on the live page]
* Filter, sort and search through the log file as you need

[Screenshot on the live page]


> Currently we don't support merged rotated log files yet.
> 
> 

<!-- page: cloud/cloud__dropping-a-bench-group.md -->
---
title: "Dropping a Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/dropping-a-bench-group"
updated: "2026-03-10"
---

> You cannot drop a Bench which has active sites under it

1. From your Bench dashboard go to Actions > Dangerous Actions.
2. Click on the Drop button.

[Screenshot on the live page]

3. You will be asked to confirm the name of the Bench you want to drop.

[Screenshot on the live page]

4. Once you have typed in the name click on the `Drop` button

<!-- page: cloud/cloud__enable-server-script.md -->
---
title: "Enable Server Script"
space: "Cloud"
url: "https://docs.frappe.io/cloud/enable-server-script"
updated: "2026-02-16"
---

Starting from version 15, Server Scripts are disabled by default to improve security on shared bench groups.

You need to [create a private bench](https://frappecloud.com/docs/benches) to enable server scripts. Public shared bench groups **DO NOT** allow the use of server scripts.

You can refer to this [documentation](https://frappeframework.com/docs/user/en/desk/scripting/server-script) for more information regarding server scripts.  
  
Once your v15 site is moved from public/shared to private bench group, server script will be enabled automatically.[Screenshot on the live page]  


  

<!-- page: cloud/cloud__faq__app-installation-issue.md -->
---
title: "App Installation Issue"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/app-installation-issue"
updated: "2026-02-16"
---

If you have been seeing the *Attention Required* status badge next to your apps:

[Screenshot on the live page]  


It means that Frappe Cloud could not fetch the source code of your application.

This can be because of multiple reasons, here are two:

1. The **App Installation ID** of your app is missing or is invalid.
2. An **invalid URL** is being used to fetch your app.

Please see the specific sections to find out and fix the cause.

Invalid URL
-----------

To figure out if your app has an invalid URL, navigate to **Apps** under your Bench Group's page and ensure that the *repository path* of your app is correct:

[Screenshot on the live page]  


The *repository path* could have changed due to a repository rename or other reasons.

If the *repository path* is invalid, you can first remove the App by clicking on the three-dots menu button and selecting **Remove App**:

[Screenshot on the live page]  


Then re-add it back in by clicking on **Add App** and then **Add from GitHub**:

[Screenshot on the live page]  


If your App has been re-added in correctly you should not see the *Attention Required* status badge anymore.

App Installation ID issue
-------------------------

If the *repository path* is valid, you might be seeing the *Attention Required* badge because of a missing or invalid **App Installation ID**.

This could be due to one of these reasons:

1. The repository visibility has been changed.
2. Repository access has not been granted to Frappe Cloud.
3. Frappe Cloud has not been added as an app.

  


To help us fix this issue you will have to re-install Frappe Cloud as a GitHub app. To do so, follow these steps:

1. Visit the Installed GitHub Apps page ([link](https://github.com/settings/installations)), and click on configure next to Frappe Cloud:[Screenshot on the live page]
2. Ensure that your app is present in the list below if you have not checked **All repositories,** if your app is present then move onto step 3.[Screenshot on the live page]
3. Uninstall Frappe Cloud:[Screenshot on the live page]
4. Reinstall it by clicking on **Connect To GitHub** from the apps page on Frappe Cloud:[Screenshot on the live page]
5. Complete the authorization flow:[Screenshot on the live page]
6. Return to the Installed GitHub Apps page ([link](https://github.com/settings/installations)), and click on configure next to Frappe Cloud as shown in step 1. You will find that your address in your browser will be of the form: `https://github.com/settings/installations/INSTALLATION_ID` keep a note of this `INSTALLATION_ID` (this is the **App Installation ID**)

If you have re-installed the App correctly, **your App Installation ID should be reset on Frappe Cloud within 30** **minutes** of having completed the steps above, and you should not be seeing the *Attention Required* badge anymore.

If you are still seeing the Attention Required badge then p**lease raise a support ticket with us with the following information**:

* **Bench Group name** where the app cannot be installed
* **Repository URL** of the app
* `INSTALLATION_ID` from the URL mentioned above

If you have followed through with the above steps, we'll take care of the rest.

<!-- page: cloud/cloud__faq__architecture-and-security.md -->
---
title: "FAQ - Security"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/architecture-and-security"
updated: "2026-07-27"
---

## Network Security &amp; Access Control

### How is network security implemented?

We use a combination of security groups and firewalls to secure networks. VPCs isolate resources and restrict access. Only necessary ports are open to the public internet; all other ports are blocked by default.

### How do you manage server access?

We use SSH with certificates and/or public keys for server access. Passwords are not used. Users can only access benches with SSH certificates.

### Is there a WAF protecting applications?

No, but a server level firewall is available.

### Is there any firewall imposed for outgoing connections?

As of now, we do not have any restrictions for outgoing requests.

### Is there an IPS/IDS solution in place?

No, there is no Intrusion Prevention/Detection System currently implemented.

### What DDoS mitigation measures are in place?

We do not have specific DDoS mitigation measures in place currently.

### Port 3306 is open. Why?

We use [ProxySQL](https://proxysql.com/) for our [database users feature](https://docs.frappe.io/cloud/database-users-and-permission-manager). This requires the port to be open.

## Data Protection &amp; Encryption

### What database is used? (RDS, Aurora, etc.)

We use MariaDB as the database for Frappe Cloud instances. We manage the database directly on the server on an AWS EC2 instance, not using services like RDS or Aurora.

### Is there High Availability for databases?

There is no High Availability setup for databases by default. We allow [dedicated server](https://docs.frappe.io/cloud/servers/servers-introduction) users to set up their own replication on request basis. You can raise a ticket for the same on our [support portal](https://support.frappe.io).

### Is there automated failover for databases?

No, there is no automated failover for databases on Frappe Cloud.

### What is the RPO and RTO for databases?

The RPO (Recovery Point Objective) for databases is up to 24 hours, as backups are taken daily. The RTO (Recovery Time Objective) can vary based on the size of the database and the time taken to restore from backups, typically ranging from a few hours to several hours. It is noted to be under 15 mintues as per our drills.

### Is point-in-time recovery available?

No, point-in-time recovery is not available for databases on Frappe Cloud.

### What encryption is used for communication?

We use HTTPS for all internet communication. SSH connections are also encrypted.

### Are databases encrypted at rest?

No, MariaDB databases are not encrypted at rest.

### Are backups encrypted?

Backups are unencrypted by default. Users can enable encryption by following our [backup encryption documentation](https://docs.frappe.io/framework/user/en/guides/basics/how-to-enable-backup-encryption). This uses fernet encryption (AES + HMAC).

### Is EBS volume/storage encrypted?

No, EBS volumes/storage attached to Frappe Cloud instances are not encrypted.

## Security Monitoring &amp; Management

### What antimalware software is used?

We use ClamAV for antimalware protection on all servers. Virus definitions are updated manually as needed. Regular scans are not implemented to maintain performance.

### Is there an EDR solution monitoring servers?

No, there is no Endpoint Detection and Response solution currently implemented.

### Are containers scanned for vulnerabilities?

No, containers are not scanned for malware or vulnerabilities.

### Do you use multi-factor authentication?

Yes, we have 2FA enabled for all logins to third-party services.

## Patch Management &amp; Updates

### How are OS security patches managed?

We use unattended upgrades to deploy patches automatically on a daily basis across all servers.

### How are Frappe Framework updates handled?

On shared benches, Frappe Framework updates are managed by the Frappe Cloud team, typically occurring weekly or with major updates. Private bench users can manage updates themselves. See [bench documentation](https://docs.frappe.io/cloud/benches) for details.

### How are MariaDB updates managed?

MariaDB security updates are handled via Ubuntu's unattended-upgrades system.

### How are Python and dependency updates managed?

Python and other dependencies are managed via benches. Users can manage them through `Bench` &gt; `Dependencies`.

### Do you have a formal patch management policy?

Yes, we have a comprehensive patch management process that covers implementation and tracking of ongoing patch compliance for all systems within our IT scope.

**Process Triggers:**

- Ongoing patch updating process
- Vulnerability assessment results
- Vulnerability alerts from vendors/OEM/security forums

**Server Patch Deployment Process:**

- Critical security patches applied automatically via Ubuntu's unattended upgrades
- Previous backups or application utilities used for system rollback when needed

### Where can I check for recent security patches?

You can check security advisories on relevant GitHub repositories:

- Frappe Framework: [Security Board](https://github.com/frappe/frappe/security/advisories)
- Frappe Cloud: [Security Board](https://github.com/frappe/press/security/advisories)

## Version Information

### How can I check current Frappe version?

You can check the current Frappe version by going to `Bench` &gt; `Apps`.

### How can I check current MariaDB version?

You can check the current MariaDB version by going to `Server` &gt; `Actions` &gt; `View Database Configuration`.

### How can I check current Python version?

You can check the current Python version by going to `Bench` &gt; `Dependencies`.

## Backup &amp; Disaster Recovery

### What backup policy do you follow?

We take logical site backups as per our [backup policy](https://frappecloud.com/docs/sites/backups). Server-wide snapshots (including data volume) are taken daily, and are retained for 2 days.

### What disaster recovery measures are in place?

We maintain server-wide multi-AZ snapshots taken daily. In case of disaster, we plan to restore from these snapshots.

## Compliance &amp; Certifications

### What certifications do you have?

Yes, we are certified under ISO 9001:2015, ISO 27001:2022, and SOC-2 Type-2 standards. Check [our compliance page](https://frappe.io/quality-and-information-security) for more information.

### Do you conduct penetration testing?

Yes, the Frappe Cloud platform undergone formal third-party penetration testing within the last 12-18 months.

### Do you conduct vulnerability scans?

Yes, we conduct regular internal and external vulnerability scans on our cloud infrastructure as part of our ongoing vulnerability management program.

<!-- page: cloud/cloud__faq__architecture.md -->
---
title: "Architecture"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/architecture"
updated: "2026-05-07"
---

## What's under the hood?

1. **Frappe Framework**: A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
2. **Frappe UI**: A Vue-based UI library to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.
3. **Agent**: A flask app designed to work along with Press. It provides a CLI interface for Press to communicate with the sites and benches.
4. **Docker**: An open-source platform that enables developers to build, package, and deploy applications in lightweight, portable containers.
5. **Ansible**: An open-source IT automation tool that simplifies the management, configuration, and deployment of systems and applications.

---

## Architecture Diagram

Typical Frappe Cloud (FC) cluster has a similar architecture:

[Screenshot on the live page: FC Cluster]

A more complex architecture would explain the redundancy for each server along with the network cluster.

---



Watch this video to know more. 

<iframe src="https://www.youtube.com/embed/KIohic6ML5o?si=TSFcTWhxF-YNe_fd" width="800" height="473.333333333" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



---

<!-- page: cloud/cloud__faq__billing.md -->
---
title: "FAQ - Billing"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/billing"
updated: "2026-02-16"
---

### How is site usage calculated and charged?

Let's say you create a site with the $25/month plan. For every day your site is active, we will charge $25 / 30 = $0.83 per day. That means if you use a site for only 20 days, we will charge only for 20 days.

### Is there a User limit?

Sites created with any of the plans do not have any user limit. However, these sites are limited by CPU hours per day. This means if there are a lot of users using the site, the site may slow down if the CPU usage limit is reached. For a detailed explanation read this [blog post on Pricing](https://frappecloud.com/blog/frappe-cloud/frappe-cloud-pricing).

### How is CPU usage calculated and throttled?

We log every request that you make to your site. For e.g, if you open the General Ledger Report in your site and it takes 2 seconds for the report to generate, we log that time. This is the CPU usage time. This time will add up as you use your site.

Now, based on the plan you chose, we will check if the total CPU usage time is used up, if it is we will drop the request and all the subsequent requests. If this is happening frequently to your site, it is an indication that you should switch to a higher plan.

### How do I stop billing in my account?

You are charged based on the number of sites you have created. If you delete all your sites, you won't be billed anything.

### Is there downtime involved in changing plan?

Changing plan of your **site** is instantaneous without any downtime involved. On the other hand, when you change plan of your **dedicated server**, regardless of upgrade or downgrade, there will be downtime. This is because changing plan means replacing the virtual machine running your sites.

<!-- page: cloud/cloud__faq__custom_apps.md -->
---
title: "Attention required in Custom Apps"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/custom_apps"
updated: "2026-06-18"
---

[Screenshot on the live page: Attention Required badge]

This means that we are **not able to fetch the latest updates from the associated GitHub repository** for the app. This happens most probably because the Frappe Cloud GitHub app does not have the permission to access the repository. 

Please make sure Frappe Cloud app has proper permissions from GitHub settings:  

[Screenshot on the live page]

[Screenshot on the live page]

You can then retry fetching the latest update:  

[Screenshot on the live page: Fetch Latest Updates in dropdown]

### Workaround: Attention required even after trying the above

If you're getting the error even after adding and removing the app on Frappe Cloud, please visit <[https://github.com/settings/installations/](https://github.com/settings/installations/)> and then click the configure button next to the **Frappe Cloud** Github App.  

[Screenshot on the live page: Configure Frappe Cloud Github]

It should take you to another page with a URL like `https://github.com/settings/installations/<unique_number>`. Copy this number (or the URL as a whole).

Now, you can raise a support ticket stating the problem (or linking this doc page) with the number you copied so that we can quickly resolve the issue from our end.

### How to add python dependencies to my custom app? Eg: pandas

If you require to install pandas or any other python package for that matter, you need to add them in your dependency file rather than doing `pip install pandas`.

You can add python dependencies to your app by adding the name of the same in [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)  
file under `dependencies` or [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) file (only one of the files should be present) present in the root folder of your custom app.

```
[project]
name = "insights"
authors = [
    { name = "Powerful Reporting Tool for Frappe Apps", email = "hello@frappe.io"}
]
description = "Open Source Business Intelligence Tool"
requires-python = ">=3.10"
readme = "README.md"
dynamic = ["version"]
dependencies = [
    "pandas~=2.3.3",
    "SQLAlchemy==2.0.41",
    "python-telegram-bot==21.4",
    "duckdb~=1.4.3",
    "sqlglot<28.0.0"
]
```

You can check ERPNext's [pyproject.toml](https://github.com/frappe/erpnext/blob/develop/pyproject.toml) for reference.

<!-- page: cloud/cloud__faq__installing-app-apt-dependencies.md -->
---
title: "Installing App APT Dependencies"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/installing-app-apt-dependencies"
updated: "2026-02-27"
---

While developing your app, you may use certain python dependencies; which you would add to your `requirements.txt` or `pyproject.toml` file. Some of these may require you to additionally install certain system level packages with some command, like:

```
sudo apt install ffmpeg
```

To do the same for Frappe Cloud, i.e, if your app has dependencies installable using Ubuntu's [APT](https://ubuntu.com/server/docs/package-management) package manager, you can list them in your custom app's `pyproject.toml` file like this:

```
[deploy.dependencies.apt]
packages = [
    "ffmpeg",
]
```

Frappe Cloud will check if it is present and install it if it is.

Here is an example from Frappe Drive: [github.com/frappe/drive](https://github.com/frappe/drive/blob/d5a0d33813885e59e49643c4c4b73f0af9f432a4/pyproject.toml#L33C1-L36C2)

<!-- page: cloud/cloud__faq__mariadb-slow-queries-in-your-site.md -->
---
title: "MariaDB slow queries in your site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site"
updated: "2026-07-25"
---

[Slow queries](https://mariadb.com/kb/en/slow-query-log-overview/) take up lots of CPU on your database server. Ideally there should be none.

In the **analytics** tab of your site dashboard, you'll be able to see slow queries (tracked by MariaDB) being run on your site database. These usually mean that the queries can be optimized to improve performance (and reduce CPU usage!)

[Screenshot on the live page]



You can also see queries that aren't necessary slow, but frequent enough to increase cpu usage from the [Database Analyzer](https://docs.frappe.io/cloud/database-analyzer) tab of your site dashboard:

[Screenshot on the live page]





> Prerequisites: You need to be on a [private bench](https://frappecloud.com/docs/benches#private-benches) and on Version 14 or higher for the following

### Adding composite database indexes

> Version 15 users can also follow the doc here for easier experience: [https://frappeframework.com/docs/user/en/profiling#query-optimization-using-recorder](https://frappeframework.com/docs/user/en/profiling#query-optimization-using-recorder)  
> Version 14 users can also try out this [feature](https://frappecloud.com/docs/performance-tuning) out on Frappe Cloud  
>
> Note: The above feature only adds singular indexes and may be suboptimal. Please try out below steps to add **composite** indexes if it doesn't yield good results.

One of the easier ways to speed up queries is to add indexes to the filtered columns. Usually, adding composite indexes rather than single column indexes is a good idea. MariaDB has an [article](https://mariadb.com/kb/en/compound-composite-indexes/) explaining the same.

You can see existing indexes on your site with:

```
SHOW INDEXES FROM `tab<doctype_name>`
```

after going to mariadb console with:

```
bench --site <site_name> mariadb
```

In frappe (since v14), it's easy to index columns with the **bench add-database-index** command. Simply find the columns that need indexing and run

```
bench --site <site_name> add-database-index --doctype "<doctype_name>" --column <column_1> --column <column_2> ...
```

```
#example
bench --site <site_name> add-database-index --doctype "Sales Order" --column order_type --column status ...
```

This index creates a **Property Setter** document as well, so the changes persist across migrations and restores.

> Note: Adding too many indexes will slow down insertion of records into the table. If you run into any problems, you can remove indexes added by deleting them from the Property Setter doctype and running bench migrate on your site

### Side effect of coalesce

Use of [COALESCE](https://mariadb.com/kb/en/coalesce/) on an index column and most other functions in mysql tends to not make use of the index and hence slow down the query. If you're writing the query with frappe ORM, you can set `ignore_ifnull=True` in your `get_list` query to remove the COALESCE from the generated query.

If you're running report from report view, you may want to consider writing a [custom report](https://frappeframework.com/docs/user/en/desk/reports/query-report) in SQL by modifying the SQL query (without the COALESCE functions) you got from the slow query reports.
