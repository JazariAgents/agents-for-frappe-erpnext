<!-- Frappe documentation: framework, part 19 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__integration__ldap-integration.md -->
---
title: "Setting up LDAP"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/integration/ldap-integration"
updated: "2026-02-17"
---

Lightweight Directory Access Protocol (LDAP) is an object directory that is commonly used for centralized authentication, commonly known as Single Sign on (SSO). Many small through to large-scale organizations have an LDAP implementation.

By setting up the LDAP Integration within Frappe, you will able to login to your frappe app by using your LDAP credentials.

1. Configuring
--------------

Many of the fields that are on the LDAP Settings page are mandatory. These fields will be easily distinguished below by being in **bold** font.

When configuring LDAP Settings, and the 'enabled' check box is checked. Frappe will validate the data you have entered into the fields. If any appear to be invalid, the settings won't save and you will be presented with an error message. Once you have corrected any errors, you will be able to successfully enable LDAP authentication.

The LDAP Settings configuration page has been broken down into smaller sections. Please see the headings below, on how to configure each section.

To setup LDAP, Navigate to:


> Home > Integrations > LDAP Settings
> 
> 



| :memo: *Reminder* |
| --- |
| *Don't forget to 'check' the enable box at the top of the page once you have entered your settings into the configuration page.* |

### 1.1 LDAP Server

Frappe has been tested with both OpenLDAP and Active Directory. However any standards compliant LDAP Directory could be used as the LDAP authentication source.

* **LDAP Directory Server**: *(drop-down)* Select the option that matches your LDAP Directory. Available options are:

*Active Directory* for Microsoft Active Directory

*OpenLDAP* for OpenLDAP

*Custom* Select this option if you need to adjust the LDAP Group attributes. i.e. your setup for LDAP groups are `groupofnames` or `uniquegroupofnames` etc
* **LDAP Server URL**: This is the URL to your LDAP Server. Must be in the form of `ldap://yourserver:port` or `ldaps://yourserver:port`

### 1.2 LDAP Authentication

This section contains the details of the user that will bind to the directory server.

* **Base Distinguished Name (DN)**: This is the user that will bind to LDAP. This user requires permission to view the search paths that you enter below.
* **Password for Base DN**: This is the password for the user above, that is used to look up user details on your LDAP server.

### 1.3 LDAP Search Paths

This section is the searh paths for each of the LDAP Directory objects. Any LDAP container object path can be used as long as it is in LDAP FDN (Full Distinguished Name) format. *i.e. ou=my frappe objects,dc=example,dc=com*. Any paths provided here require that the bind user has access to read and write to.


> Write access is required for the bind user so that end users can reset their passwords.
> 
> 

* **LDAP search path for Users**: This is the search path that all users in your LDAP server must be part of to be able to log into a frappe app.
* **LDAP search path for Group**: This is the search path that all groups in your LDAP server must be part of to be able to log into a frappe app.
* **LDAP Search String**: This field allows frappe to match the user/email entered in the frappe login screen, with the LDAP Server. For example, you could use email address, or username depending on your preference.

You can use complex LDAP search filters here as long as they contain the login name placeholder `{0}` and are enclosed in braces `()`. This is placed inside the search filter where you would like to match the login name. Any filter the [ldap3 python module](https://ldap3.readthedocs.io/en/latest/searches.html#the-ldap-filter) and that your LDAP directory supports should work. examples include:

`(uid={0})`

`(SamAccountName={0})` - *(Active Directory)*

`(&amp;(description=*ACCESS:Frappe*)(uid={0})` - *using a filter description in OpenLDAP allows filtering similar to Active Directories* `memberOf` as it will only select users who have `ACCESS:Frappe` in the description field.

`(&amp;(SamAccountName={0})(memberof=cn=Domain Users,ou=Groups,DC=example,dc=com))` - *(Active Directory)*

### 1.4 LDAP User Creation and Mapping

This section contains the LDAP attributes that will be read from the directory server to map against the frappe user.

* **LDAP Email Field**: Specifies the LDAP attribute that contains the email address of the user. `mail` is the common LDAP attribute to use.
* **LDAP Username Field**: Specifies the LDAP attribute that contains the username of the user. `sAMAccountName` for Active Directory and `uid` for OpenLDAP.
* **LDAP First Name Field**: Specifies the LDAP field that contains the first name of the user. `givenName` or `sn` is commonly used.

There are many other non-mandatory LDAP attributes that you can use to map to the frappe user. They are:

* Middle Name
* Phone
* Mobile


> **SECURITY WARNING** Understand that if you use the LDAP attribute `mail` for the username field, that this may cause security implications. `mail` is not a unique value within LDAP. Enabling `mail` attribute to be used for login purposes is outside of the scope of this documentation. Please consult your directory server documentation on how to do this.
> 
> 

### 1.5 LDAP Security

This section is optional. However if you would like to configure a secure connection to your directory server, this where you enter the TLS connection details.

* In the LDAP Settings area, there are two dropdowns.


	1. SSL/TLS Mode - set this to **StartTLS** to connect to your LDAP server using StartTLS. If your LDAP server does not support StartTLS, setting this to StartTLS will result in an error `StartTLS is not supported`. Check the configuration on your LDAP server if you receive this error.
	2. Require Trusted Certificate - if you change this to
	
	`Yes` then the certificate provided by the LDAP server must be trusted by the Frappe server.
	
	`No` it is not recommended to use this setting as it bypasses ensuring the certificate is signed by a trusted certificate authority.

If you would rather use StartTLS with a self-signed (untrusted) certificate, set this to **No**. If you do not use StartTLS, this setting is ignored.

* SSL/TLS Mode   
Specifies whether you want to start a TLS session on initial connection to the LDAP server.
* Require Trusted Certificate   
Specifies if you require a trusted certificate to connect to the LDAP server

If you are specifying a trusted certificate, you will need to specify the paths to your certificate files. These files are to be placed on your frappe server, and the following fields should be an absolute path to the files on your server. The certificate fields are:
* Path to private Key File
* Path to Server Certificate
* Path to CA Certs File


> To configure your Frappe Instance to accept certificates signed by your own 'Certificate Authority' or a 'self-signed certificate', please consult your Operating Systems documentation on how to add a 'Certificate Authority' / 'self-signed' certificate to your 'Trusted Certificates store.'
> 
> 

### 1.6 LDAP Custom Directory

This section is **mandatory if you select custom** directory server. There are only two options available here and they pertain to the groups that your directory server uses. They are:

* ***Group Object Class*** This is the object class of the groups within your directory server.
* ***Group Member Attribute*** This is the LDAP Attribute within the group that contains the common name (CN) of the user.
* ***Custom Group Search*** This can be used to specify a custom LDAP Custom Group Search which is necessary for some LDAP providers.

### 1.7 LDAP Group Mapping

This section contains the details for mapping the LDAP Groups. Any group the user is a member of will be mapped to the specified frappe role(s).


> Frappe Feature: if you have configured group mapping. Each time a user logs on, their roles are checked and added/removed as required.
> 
> 

* **Default Role on Creation**: When the user is created in your frappe app, they will be assigned with this default role.
* **LDAP Group Mappings Table** You can map mutiple LDAP groups to Frappe roles. Entry of the LDAP group must match the LDAP `cn` attribute. *i.e. 'Domain Users'* not *'cn=Domain Users,ou=Groups,dc=example,dc=com'* which is a LDAP FDN entry.

*Example*



| No | LDAP Group | Role |
| --- | --- | --- |
| 1 | Domain Users | Guest |
| 2 | Domain Administrators | Administrator |
* LDAP Group Field *(depreciation WARNING)* This is the LDAP Attribute within the user LDAP object that contains the list of groups the user is a member of. If you have configured all of the settings as per above, this setting will have no effect. This field exists purely for those who configured LDAP prior to the current layout. This field will be removed in a future version of Frappe.

2. Log in to frappe with LDAP
-----------------------------

After setting up and enabling LDAP, on the login screen, the system enables **Login Via LDAP** option.

[Screenshot on the live page: Log into frappe] *Figure 1. Frappe app login screen when LDAP has been configured and enabled.*

<!-- page: framework/framework__user__en__integration__razorpay.md -->
---
title: "RazorPay\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/integration/razorpay"
updated: "2026-02-17"
---

Razorpay is a popular payments solution in India which allows businesses to accept, process and disburse payments with its product suite. It gives you access to payment methods like Credit Cards, Debit Cards and Netbanking.

## Integrating Razorpay Client Checkout
Razorpay Payment

### Steps for integration
#### Include checkout script in your code

Insert the following script on your page `<script type="text/javascript" src="/assets/js/checkout.min.js"></script>`
The checkout script automatically fetches the razorpay checkout script and wraps their API for some syntactic sugar.

#### Create the Order controller in your backend

```python
def get_razorpay_order(self):
 controller = get_payment_gateway_controller("Razorpay")

 payment_details = {
 "amount": 30000,
 ...
 "reference_doctype": "Conference Participant",
 "reference_docname": self.name,
 ...
 "receipt": self.name
 }

 return controller.create_order(**payment_details)
```

#### Inititate the payment in client using checkout API

```javascript
function make_payment(ticket) {
 var options = {
 "name": "<CHECKOUT MODAL TITLE>",
 "description": "<CHECKOUT MODAL DESCRIPTION>",
 "image": "<CHECKOUT MODAL LOGO>",
 "prefill": {
 "name": "<CUSTOMER NAME>",
 "email": "<CUSTOMER EMAIL>",
 "contact": "<CUSTOMER PHONE>"
 },
 "theme": {
 "color": "<MODAL COLOR>"
 },
 "doctype": "<REFERENCE DOCTYPE>", // Mandatory
 "docname": "<REFERENCE DOCNAME" // Mandatory
 };

 razorpay = new frappe.checkout.razorpay(options)
 razorpay.on_open = () => {
 // SCRIPT TO RUN WHEN MODAL OPENS
 }
 razorpay.on_success = () => {
 // SCRIPT TO RUN ON PAYMENT SUCCESS
 }
 razorpay.on_fail = () => {
 // SCRIPT TO RUN ON PAYMENT FAILURE
 }
 razorpay.init() // Creates the order and opens the modal
}
```

### Lifecycle
1. **Create an Order in your backend**

 An order is first created at the server triggered by `razorpay.init()`, for this a controller `get_razorpay_order` must be created for the doctype. The server method sets the amount to be charged and a unique receipt id for razorpay APIs to consume.

 The `get_razorpay_order` internally calls the create_order controller of razorpay settings doctype. which then creates an integration request and sends POST request to `https://api.razorpay.com/v1/orders`

1. **Process Checkout at Client**

 A successful creation of the Order returns the `order_id` that is stored against the Order in integration request. This `order_id` is passed to the client which triggers the razorpay modal. After the payment, depending on the status the success or fail API method is called and the payment ID is passed to it.

1. **Verify the payment**

 Once the API method is called, The transaction details are saved in integration request. If successful the `authorize_payment` controller is called, which checks the payment status from razorpay API using the Payment ID. Once authorized, the integration request is marked as Completed, following this the payment success hook of the reference_doctype is called.

You can read more about Razorpay custom checkout in their [documentation](https://razorpay.com/docs/payment-gateway/web-integration/custom/)

<!-- page: framework/framework__user__en__introduction.md -->
---
title: "Introduction"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/introduction"
updated: "2026-04-21"
---

## What is Frappe Framework?

Frappe, pronounced *fra-pay*, is a full stack, batteries-included, web framework written in Python and Javascript with MariaDB as the database. It is the framework which powers ERPNext, is pretty generic and can be used to build database driven apps.

[Screenshot on the live page]

## Why Frappe?

The key difference in Frappe compared to other frameworks is that **meta-data** is also treated as data. This enables you to build front-ends very easily. We believe in a monolithic architecture, so Frappe comes with almost everything you need to build a modern web application. It has a full featured Admin UI called the Desk that handles forms, navigation, lists, menus, permissions, file attachment and much more out of the box. Read more here.

## Key Features

1. Full-Stack Framework: Frappe covers both front-end and back-end development, allowing developers to build complete applications using a single framework.
2. Built-in Admin Interface: Provides a pre-built, customizable admin dashboard for managing application data, reducing development time and effort.
3. Role-Based Permissions: Comprehensive user and role management system to control access and permissions within the application.
4. REST API: Automatically generated RESTful API for all models, enabling easy integration with other systems and services.
5. Customizable Forms and Views: Flexible form and view customization using server-side scripting and client-side JavaScript.
6. Report Builder: Powerful reporting tool that allows users to create custom reports without writing any code.

## Installation

Before you can use Frappe, you need to install it. We have a complete installation guide which covers all possibilities, this guide will also help you understand the backend stack.

## Learning and community

1. [Frappe School](https://school.frappe.io) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [GitHub](https://github.com/frappe/frappe) - Explore the source code, contribute, and collaborate with the Frappe community.
3. [Discussion Forum](https://discuss.frappe.io) - Hang out with our growing community on our forum, ask questions, help others and be a part of the community.
4. [buildwithhussain.com](https://buildwithhussain.com) - Watch Frappe Framework being used in the wild to build world-class web apps.

<!-- page: framework/framework__user__en__logging.md -->
---
title: "Logging"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/logging"
updated: "2026-05-10"
---

Logging events can significantly improve the debugging experience. Frappe's development and production environments come with logging capabilities out of the box.

There's two main categories of logs based on accessibility. Desk Logs, which are stored in your site database and can be accessed and queried as Documents and the Server Logs, that are stored in files managed by a Log Rotation system.

Desk Logs
---------

Logs that can be accessed via the Desk UI *(generally searched for, from the* [*Awesomebar*](/framework/v14/user/en/desk#awesomebar)*)*. These track the operational events generally; but you can utilize their APIs to track about anything from your Frappe apps.

Some of the logs in the `Core` module are:

* [Access Log](https://docs.erpnext.com/docs/user/manual/en/using-erpnext/access-log)
* Activity Log
* [Error Log](https://frappe.io/blog/development/better-error-logging-with-frappe)
* Scheduled Job Log

You can find more information about them from the embedded links. The best way to find out more about each of them is checking them out directly on your site.

Server Logs
-----------

Server Logs generally consist of lower level, transactional data as compared to those accessible from Desk. From Version 13, logs are available at site level too. These site logs are created by the Frappe Application, while many of the bench level log files are generated by the processes that support your Frappe environment. From your bench folder, you may find logs under:

* `./logs`
* `./sites/{site}/logs`

At the time of writing this, only `frappe.web.log` and `scheduler.log` are logged at site and bench-level. At bench level, some of the most useful files could be:

* `bench.log`
* `scheduler.log`
* `worker.log`

Tracking the bench commands executed, status of the jobs run by your Scheduler or [Background Jobs](/framework/v14/user/en/guides/app-development/running-background-jobs) can be found in these logs.

&gt; To enable Frappe Web Logging on your site, update the site config with &gt; `enable_frappe_logger`: `true`

### Error Snapshots

Along with these, Frappe maintains error snapshots for your sites for HTTP response codes from 500 and above. This is done in order to provide more context for failures in case of server errors. Consider, a desk action failing with HTTP status code 500, this would add a corresponding log in the `./sites/{site}/frappe.log` file as follows:


```
2021-05-06 14:08:12,177 ERROR frappe New Exception collected with snapshot id: 2021-05-06 14:08:11.940809-127.0.0.1-bde
Site: frappeframework.com
Form Dict: {'docs': '{"name":"assets.frappeframework.com","owner":"Administrator","creation":"2020-04-04 14:58:18.771247","modified":"2021-02-08 09:40:56.820300","modified_by":"gavin@frappe.io","idx":0,"docstatus":0,"status":"Active","hostname":"assets","domain":"frappeframework.com","cluster":"Default","provider":"Generic","is_server_setup":1,"ip":"192.168.29.100","private_ip":"10.120.120.120","agent_password":"*****","is_primary":1,"doctype":"Server","__last_sync_on":"2021-05-06T08:38:08.931Z"}', 'method': 'ping_agent', 'cmd': 'run_doc_method'}
  

```
The first line of the log mentions the snapshot ID of the error, which in this case was `2021-05-06 14:08:11.940809-127.0.0.1-bde`. A corresponding file identified with the snapshot ID should be under `./sites/frappeframework.com/error-snapshots`, with the name `2021-05-06 14:08:11.940809-127.0.0.1-bde.json`. Contents of the file may be:


```
    {
    "etype": "UnboundLocalError",
    "evalue": "UnboundLocalError("local variable 'headers' referenced before assignment")",
    "exception": {
      "args": [...],
      "with_traceback": [...]
    },
    "frames": [
      {
      "call": "(request=&lt;request 'https:="" frappeframework.com="" api="" method="" run_doc_method'="" [post]=""&gt;)",
      "dump": {
        "frappe. api": "&lt;module 'frappe.api'="" from="" '="" home="" frappe="" frappe-bench="" apps="" api.py'=""&gt;",
        "frappe.api. handle": "&lt;function handle=""&gt;",
        "global frappe": "&lt;module 'frappe'="" from="" '="" home="" frappe="" frappe-bench="" apps="" __init__.py'=""&gt;",
        "response": "None"
      },
      "file": "/home/frappe/frappe-bench/apps/frappe/frappe/app.py",
      "func": "application",
      "lines": {
        "66": "",
        "67": "elif request.path.startswith("/api/"):",
        "68": "response = frappe.api.handle()",
        "69": "",
        "70": "elif request.path.startswith('/backups'):"
      },
      "lnum": 68
      },
    ...
    ],
    "locals": {
      "data": "None",
      "files": "None",
      "method": "GET",
      "path": "ping",
      "self": "&lt;orchestrator.agent.agent object=""&gt;",
      "url": "https://assets.frappeframework.com:443/agent/ping"
    },
    "pyver": "Python 3.8.2: /home/frappe/frappe-bench/env/bin/python (prefix: /home/frappe/frappe-bench/env)",
    "timestamp": "2021-05-06 14:08:11.940971",
    "traceback": "Traceback (most recent call last):
 File "/home/frappe/frappe-bench/env/lib/python3.8/site-packages/cryptography/fernet.py", line 119, in _verify_signature
 h.verify(data[-32:])
 File "/home/frappe/frappe-bench/env/lib/python3.8/site-packages/cryptography/hazmat/primitives/hmac.py", line 74, in verify
 ctx.verify(signature)
 File "/home/frappe/frappe-bench/env/lib/python3.8/site-packages/cryptography/hazmat/backends/openssl/hmac.py", line 75, in verify
 raise InvalidSignature("Signature did not match digest.")
cryptography.exceptions.InvalidSignature: Signature did not match digest.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "/home/frappe/frappe-bench/apps/frappe/frappe/app.py", line 68, in application
 response = frappe.api.handle()
 File "/home/frappe/frappe-bench/apps/frappe/frappe/api.py", line 54, in handle
 return frappe.handler.handle()
 File "/home/frappe/frappe-bench/apps/orchestrator/orchestrator/agent.py", line 474, in request
 headers=headers,
UnboundLocalError: local variable 'headers' referenced before assignment
"
    }
  

```
These snapshots are synced periodically with the site's database and are available via the desk with records added under the DocType **Error Snapshot**. They are maintained for a month from creation before each record is deleted.

&gt; Error snapshots are tracked by default. To disable this for your site, update &gt; the site config with `disable_error_snapshot`: `true`

Processes
---------

Server Logs may be generated by the [bench CLI](/framework/v14/user/en/bench), your process manager or the Frappe application directly. Your process managers take care of getting all the moving parts up and running for your Frappe environment as well as directing output and error streams to your log files.

Apart from the *"always running"* default logging, you can also use [Monitor](/framework/v14/user/en/debugging#monitoring) to log more information about all the requests to your site.

Maintainence
------------

The log files generated by your process manager may get pretty large over time if you aren't paying attention. To know which files you have to track for this, checkout the `supervisor.conf` or `Procfile` on your bench, depending on whether you're running a production or development instance respectively.

Auto cleanup of old logs
------------------------

Most logging doctypes in Frappe support configurable retention period with sane defaults.

"Log Settings" doctype lets you configure retention period for default logging doctypes.

[Screenshot on the live page: Log Settings]  


You can also register your custom logging doctype with log settings by adding a single static method to your doctype controller like this. Custom logging doctypes which implement this method will automatically show up in Log Settings.


```
class CustomLoggingDoctype(Document):
 @staticmethod
    def clear_old_logs(days=180):
        from frappe.query_builder import Interval
        from frappe.query_builder.functions import Now

        table = frappe.qb.DocType("Custom Logging Doctype")
        frappe.db.delete(table, filters=(table.modified &lt; (Now() - Interval(days=days))))
  

```
More
----

In a production environment, you'd likely want to log more information for your Frappe Applications or the processes that make up your Frappe Environment. Here's some resources you could go over to find out more.

Frappe Application

* [Frappe Logging API](/framework/v14/user/en/api/logging)

Server Monitoring

* [MySQL](https://dev.mysql.com/doc/refman/5.7/en/server-logs.html)
* [PostgreSQL](https://www.postgresql.org/docs/current/runtime-config-logging.html)
* [NGINX](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

<!-- page: framework/framework__user__en__microsoft-email-oauth.md -->
---
title: "Microsoft Office365 Email OAuth"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/microsoft-email-oauth"
updated: "2026-02-17"
---



---

This guide helps in authenticating an outlook email account in frappe.

> Note: The user should log in as the Email Account User in their Frappe account. For example, if the email account is test@example.com, then they should log in using the user test@example.com on the site.

  
1. Go to your Frappe instance and create a **New Connected App** and save it (just enter the name and save) and copy the Redirect URI for later.

[Screenshot on the live page]
[Screenshot on the live page]

2. Login to [Microsoft Azure](https://portal.azure.com/#home), search for and select **Microsoft Entra ID** (formerly called **Azure Active Directory**).


[Screenshot on the live page]

3. Click **Add** -> **App registration**

[Screenshot on the live page]


4. Enter the respective details (app name, account type), paste the previously copied redirect URI from Frappe instance and select the platform as “Web”.


[Screenshot on the live page]


To know more about the account types, click [here](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application)

5. Click on Register and you’ll be redirected to your created app. Copy your **Application ID** - it’s the Client ID you'll need to paste into your Connected App on your Frappe instance.

[Screenshot on the live page]


6. Head over to **API Permission** section in your app and add Microsoft Graph permissions.


[Screenshot on the live page]


7. Select **Delegated Permissions** for `IMAP.AccessAsUserAll`, `SMTP.Send` and `offline_access`, then click "Add permissions"

[Screenshot on the live page]
[Screenshot on the live page]
[Screenshot on the live page]
[Screenshot on the live page]


8. Head over to **Certificates &amp; Secrets** to create a Client Secret

[Screenshot on the live page]


Add description and click on add to see a newly generated client secret.

[Screenshot on the live page]

Copy over the **Value** - paste this in the `Client Secret` field in the new Connected App on your Frappe instance.


[Screenshot on the live page]

9. Click on "Endpoints" and copy "OpenID Connect metadata document". This should be pasted into the "OpenID Configuration" field of your Frappe Connected App. After that, click "Get OpenID Configuration" on the Connected App, that will populate the endpoints.

[Screenshot on the live page]
[Screenshot on the live page]
[Screenshot on the live page]

Then, add these scopes, and save the document.

- `https://outlook.office.com/IMAP.AccessAsUser.All`
- `https://outlook.office.com/SMTP.Send`
- `offline_access`


10. Click on the “**Connect to {your connected app name}**” button on top right which should start the Oauth flow for Microsoft.

**Make sure the email account you’re authorizing is going to be the same as the one you’re going to add in frappe.**

11. If everything goes as planned, you’ll be redirected back to your Connected App page and should be able to see Token Cache connected to your connected app, head over to your created token cache to check if you have both refresh and access token.

[Screenshot on the live page]


[Screenshot on the live page]  


  
12. Head over to Email Account doctype and create a new Email Account. And select the method as Oauth and add your connected app and user which has created the token cache and set up your email account as usual.

[Screenshot on the live page]  


Please ensure IMAP/POP connections are allowed on your Microsoft account. You can find information regarding that, as well as the settings for outlook servers over here: <https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353>

NOTE: Microsoft restricts sending from any other email address other than the one which authenticated it. For that you can check these 2 options in the email account document itself

[Screenshot on the live page]  


  





---

Please visit Microsoft’s official documentation for any Additional Info: <https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth>



---

### Service Principal Authentication

Email Accounts require access as a User. This disallowed the use of Shared Mailboxes dedicated to Frappe, as Full Access permissions would need to be granted to the user signing into Frappe.

This feature lets Frappe authenticate itself to e.g. Exchange Online, so it can send and receive emails from the Shared Mailbox, without having to delegate Full Access permissions to each user that accesses Frappe.

If you wish to authenticate using this method, there's a checkbox available in `Email Account`

[Screenshot on the live page]  

<!-- page: framework/framework__user__en__portal-pages.md -->
---
title: "Portal Pages\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/portal-pages"
updated: "2026-02-17"
---


Frappe Framework not only provides a rich admin interface via the
[Desk](/framework/v14/user/en/desk) which is an SPA but also static server rendered web
pages. These pages are generally built for your website visitors. They can be
public or can require login.

## Adding pages

Every frappe app including frappe comes with a `www` folder which directly maps
to website urls. Here is what the directory structure looks like:

```bash
frappe/www
├── about.html
├── about.py
├── contact.html
├── contact.py
├── desk.html
├── desk.py
├── login.html
├── login.py
├── me.html
└── me.py
```

This structure enables the routes `/about`, `/contact`, `/desk`, `/login` and
`/me`.

To add your own page, just add an HTML file in the `www` folder of your app.
There are multiple ways to organize these portal pages. For example,

```bash
custom_app/www
├── custom_page.html
└── custom_page.py
```
Will be rendered on the route `/custom_page`.

To add subpages you can convert your main page into a folder and add its content
in an index file. For example,

```bash
custom_app/www
└── custom_page
 ├── index.html
 ├── index.py
 ├── subpage.html
 └── subpage.py

```
Will still be rendered on the route `/custom_page` and `/custom_page/subpage`
will also be available.

> You can write `.md` files instead of `.html` for simple static pages like
> documentation. This documentation you are reading is written as a markdown file.

### Overriding standard pages

Frappe also allows you to override standard pages through your custom app. For
example, to override the standard `/about` provided by frappe, just add a file
named `about.html` in the `www` folder of your app and it will take precedence.

### Templating

You can add dynamic content to Portal Pages using Jinja templates. All of the
portal pages extend from the base template `frappe/templates/web.html` which
itself extends from `frappe/templates/base.html`.

Here is what a sample page might look like:

```html

{% extends "templates/web.html" %}

{% block title %}{{ _("About Us") }}{% endblock %}

{% block page_content %}
{{ _("About Us") }}
====================




 We believe that great companies are driven by excellence,
 and add value to both its customers and society.
 You will find our team embibes these values.
 

{% endblock %}
```

You can also omit the `extend` and `block` if you want to the use the default
base template.

```html

{{ _("About Us") }}
====================




 We believe that great companies are driven by excellence,
 and add value to both its customers and society.
 You will find our team embibes these values.
 

```

### Context

Every portal page can have a python controller which will build `context` for
the page. The controller should have the same name as the `.html` or `.md` file
with a `.py` extension.

```bash
custom_app/www
├── custom_page.html
└── custom_page.py
```

The controller should have a `get_context` method which takes a `context` dict,
adds any data to it and then returns it. Here is what a sample page controller
might look like:

```py
# about.py
import frappe

def get_context(context):
 context.about_us_settings = frappe.get_doc('About Us Settings')
 return context
```

Usage in template


```html

{{ _("About Us") }}
====================




 We believe that great companies are driven by excellence,
 and add value to both its customers and society.
 You will find our team embibes these values.
 

 {% if about_us_settings.show_contact_us %}
 [Contact Us](/contact)
 {% endif %}

```


> Since Portal Pages are built using Jinja, frappe provides a standard
> [API](/framework/v14/user/en/api/jinja) to use in jinja templates.

#### List of standard context keys

Here is a list of all the standard keys that can be set in `context` and their
functionalities.

| Context Key | Functionality |
| --------------------- | ---------------------------------------- |
| `add_breadcrumbs` | Add breadcrumbs to page |
| `no_breadcrumbs` | Remove breadcrumbs from page |
| `show_sidebar` | Show web sidebar |
| `safe_render` | Toggle [safe_render](#safe_render) |
| `no_header` | Hide header |
| `no_cache` | Disable caching for this page |
| `sitemap` | Include/exclude page in sitemap |
| `add_next_prev_links` | Add Next and Previous navigation buttons |
| `title` | Set the page title |

##### safe_render

`frappe.render_template` does not render a template which contains the string
`.__` to prevent running any illegal python expressions. You may want to disable
this behaviour if you are sure that the content is safe. To do this, you need to
turn off safe render by setting the value of `safe_render` key to `False` in
context.

#### Set context via frontmatter

You can also set values in context using a frontmatter block. Frontmatter blocks
can be used to set static values specific to a page like meta tags.

Take a look at the following example:
```bash
---
title: Introduction
metatags:
 description: This is description for the introduction page
---

# Introduction
This is an introduction page
```

The above frontmatter block will update the `context` dict with the following values:
```py
{
 'title': 'Introduction',
 'metatags': {
 'description': 'This is description for the introduction page'
 }
}
```

#### Set context via comments

You can also set some values in context by adding html comments in your pages.

For example by adding `` to your `.html` or `.md` file,
`context.add_breadcrumbs` will be set to `True` and it will automatically generate
breadcrumbs based on folder structure.


```html

{{ _("About Us") }}
====================




 We believe that great companies are driven by excellence,
 and add value to both its customers and society.
 You will find our team embibes these values.
 

 {% if about_us_settings.show_contact_us %}
 [Contact Us](/contact)
 {% endif %}

```

Here is a list of keys that you can set and their context values:

| Comment | Context Value |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| `` | `add_breadcrumbs = 1` |
| `` | `no_breadcrumbs = 1` |
| `` | `show_sidebar = 1` |
| `` | `no_header = 1` |
| `` | `no_cache = 1` |
| `` | `sitemap = 0` |
| `` | `sitemap = 1` |
| `` | `add_next_prev_links = 1` |
| `` | `title = 'Custom Title'` |
| `` | `base_template = 'custom_app/path/to/custom_base.html'` |

### Custom CSS and JS

You can add custom CSS and JS for your pages by dropping a `.css` or `.js` file
of the same name.

```bash
custom_app/www
├── custom_page.html
├── custom_page.css
├── custom_page.js
└── custom_page.py
```

### Home Page

The home page for your portal can be defined in

1. Role
1. Portal Settings (this will be for logged in users)
1. Via Hook `get_website_user_home_page`
1. Website Settings (this will be for non logged in users as well - i.e. Guest)

<!-- page: framework/framework__user__en__prerequisites.md -->
---
title: "Prerequisites"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/prerequisites"
updated: "2026-02-17"
---


A list of resources to help you get started with building apps using Frappe.

## 1. Python

Frappe uses Python 3 for server-side programming. It is highly recommended to
learn Python before you start building apps with Frappe Framework.

Resources:

1. [Codecademy Tutorial for Python](https://www.codecademy.com/learn/learn-python-3)
2. [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)

## 2. MariaDB / Postgres

To create database-driven apps with Frappe, you must understand the basics of
database management and common SQL queries.

Resources:

1. [Codecademy Tutorial for SQL](https://www.codecademy.com/learn/learn-sql)
2. [A basic MySQL tutorial by DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-perform-basic-queries-in-mysql-and-mariadb-on-a-cloud-server)
3. [Getting started with MariaDB](https://mariadb.com/kb/en/mariadb/documentation/getting-started/)

## 3. HTML / CSS

If you want to build user interfaces using Frappe Framework, you will need to
learn basic HTML / CSS and the Bootstrap CSS Framework.

Resources:

1. [Codecademy Tutorial for HTML/CSS](https://www.codecademy.com/learn/learn-html-css)
2. [Getting started with Bootstrap](https://getbootstrap.com/getting-started/)

## 4. JavaScript / jQuery

To customize forms and create interactive user interfaces, you will have to
learn JavaScript and the library jQuery.

Resources:

1. [The Modern JavaScript Tutorial](https://javascript.info/)
2. [Codecademy Tutorial for JavaScript](https://www.codecademy.com/learn/learn-javascript)
3. [Codecademy Tutorial for jQuery](https://www.codecademy.com/learn/jquery)

## 5. Jinja Templating

For building Web Views and Print Templates, you will have to learn the Jinja
Templating language.

Resources:

1. [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/)

## 6. Git / GitHub

Learn how to contribute to an open source project using Git and GitHub, two
great tools to help you manage your code and share it with others.

Resources:

1. [Basic Git Tutorial](https://try.github.io/)
2. [How to contribute to Open Source](https://opensource.guide/how-to-contribute/)

If you are comfortable with the basics of these tools, you are ready to build an
app with Frappe Framework.

Next: [Create a Bench](/framework/v14/user/en/tutorial/install-and-setup-bench)

<!-- page: framework/framework__user__en__production-setup.md -->
---
title: "Production Setup\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/production-setup"
updated: "2026-02-17"
---


[Bench](https://github.com/frappe/bench) is the CLI tool to manage deployments
for sites based on Frappe Framework. Here are steps to deploy your frappe based
sites on production.

## Install Bench

Deploying frappe sites is not too different from setting it up on your local
system. Install bench using the [Easy
Install](https://github.com/frappe/bench#easy-install-script) script if your server is
one of the supported linux distributions (Debian, Ubuntu, CentOS). Make sure you
pass the `--production` flag to the script.

```bash
sudo python install.py --production --user [frappe-user]
```

## Setup sites and apps

```bash
# change directory to frappe-bench
cd frappe-bench

# create a new site
bench new-site example.com

# download frappe apps or your custom-apps
bench get-app erpnext
bench get-app https://github.com/yourremote/yourapp.git

# install apps onto your site
bench --site example.com install-app erpnext yourapp
```

## Check supervisor

If everything is setup properly, you should see frappe processes as the
supervisor status output.

```
$ sudo supervisorctl status
frappe-bench-redis:frappe-bench-redis-cache RUNNING pid 6467, uptime 10 days, 8:12:09
frappe-bench-redis:frappe-bench-redis-queue RUNNING pid 6466, uptime 10 days, 8:12:09
frappe-bench-redis:frappe-bench-redis-socketio RUNNING pid 6468, uptime 10 days, 8:12:09
frappe-bench-web:frappe-bench-frappe-web RUNNING pid 8856, uptime 10 days, 4:32:18
frappe-bench-web:frappe-bench-node-socketio RUNNING pid 8858, uptime 10 days, 4:32:18
frappe-bench-workers:frappe-bench-frappe-default-worker-0 RUNNING pid 8823, uptime 10 days, 4:32:19
frappe-bench-workers:frappe-bench-frappe-long-worker-0 RUNNING pid 8824, uptime 10 days, 4:32:19
frappe-bench-workers:frappe-bench-frappe-schedule RUNNING pid 8822, uptime 10 days, 4:32:19
frappe-bench-workers:frappe-bench-frappe-short-worker-0 RUNNING pid 8825, uptime 10 days, 4:32:19
```

If you own `example.com` and it is mapped to the IP Address of your server, your
site should be live on `example.com`.

## Updating

To update your sites, just run the following command. It will update all of your
apps (`git pull`), run patches on all sites, build JS and CSS assets and restart
supervisor.

```bash
# update everything
bench update

# update apps
bench update --pull

# run patches only
bench update --patch

# build assets only
bench update --build

# update bench (the cli)
bench update --bench

# update python packages and node_modules
bench update --requirements
```

## Redis Namespaces

Namespaces help to secure user's data. Multiple benches can use the same Redis instance without worrying about namespace conflicts. You can enable Redis namespaces in Frappe by following the given setup (for now Frappe supports namespaces for Redis Queue at bench level).

You can create Redis users and configure Frappe with credentials using bench create-rq-users CLI.

```bash
bench create-rq-users

# Optional flags
# --use-rq-auth Enable Redis authentication for all bench sites
# --set-admin-password sets default user admin password
```

Above command generates an ACL file in the bench configs directory. Make sure that Redis_queue.conf file is configured to use an acl file if not already (Alternatively, run `bench setup redis` with the latest version of the Bench CLI).

```bash
aclfile [frappe-bench-absolute-path]/config/redis_queue.acl
```
