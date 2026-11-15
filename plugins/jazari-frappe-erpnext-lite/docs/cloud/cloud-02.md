<!-- Frappe documentation: cloud, part 2 of 9. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__common-issues__debugging-app-installs-locally.md -->
---
title: "Debugging app installs locally"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/debugging-app-installs-locally"
updated: "2026-02-16"
---

If your deploy has failed at an **Install Apps** step or at the **Run Validations - Pre-build** step, chances are that there is some kind of error in one (or several) of the apps on your bench group.

[Screenshot on the live page]  


In such a case, retrying the deploy on Frappe Cloud without making any changes will lead to it failing in the same way.


> 💡 First step to prevent repeated failures is to view the error in the failed step's output. If you do not understand the error, you can ask in the [Frappe Cloud Telegram group](https://t.me/frappecloud).
> 
> 

One way to figure out is to try and run the app install locally.


> 🛎️ You can view common issues we come across in the **Common issues in app related build failures** section.
> 
> 

Running app installs locally
----------------------------

To install an app locally:

1. Setup a new bench on your computer.
2. Clone the repository of the app you want to install.
3. Install app using `bench get-app` with the file path.

### Setup a new bench

If you are not familiar with how to setup a bench using `bench init`, you can follow this documentation: [Install and Setup Bench](https://frappeframework.com/docs/user/en/tutorial/install-and-setup-bench). Example:


```
bench init test-install # At /some/path/test-install
```
There are several reasons to setup a new bench, here are a few:

1. Each bench maintains it's own set of Python dependencies.
2. Your main bench might have manually installed dependencies.
3. Your main bench might have manually updated apps.

### Clone the apps repository

Clone the the **specific version** of the app you want to install at a **path outside the new bench** you just setup. Example:


```
git clone https://github.com/org/app --depth 1 /some/path/app
```

> 💡 To try the exact command Frappe Cloud uses to fetch a repository, you can follow [this function](https://github.com/frappe/press/blob/2da6e1b29b9462f653d4890e35ecbb8ec2b41544/press/press/doctype/app_release/app_release.py#L147).
> 
> 

### Install app

Install the app using the path to where you cloned it.


```
bench get-app file:///some/path/app # In /some/path/test-install
```
On doing this `bench` will install your into the **test-install** bench from repository you cloned locally.

### Debug and fix

Now if there are any issues in the apps code, the `get-app` command will fail to complete.

If that does happen you can fix the code in the repository you just cloned (for example, at `/some/path/app`) and try running `bench get-app` in the same bench or a new one.

Common issues in app related build failures
-------------------------------------------


> 💡 To figure out the issue you are facing, be sure to first view the failed step's output.
> 
> 

### Module Not Found Error

The app is trying to import from a module that is not present. The module here can be another Frappe app or a Python dependency. [Reference](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError).

**To Fix**: If the module is a Python dependency, ensure that it is mentioned in your `requirements.txt` or `pyproject.toml` file. If the module is a Frappe app, ensure that it is installed on your Bench before the failing app.

### Import Error

The app is trying to import a value that is not present in that module. [Reference](https://docs.python.org/3/library/exceptions.html#ImportError).

**To Fix**: Ensure that you are using the correct version of the dependency from which the value is being imported. Ensure that the value is actually present in the module from which you are importing it.

### Syntax Error

The app has syntax errors. This can occur if your Python version is not new enough, for example using unsupported type annotations. [Reference](https://docs.python.org/3/library/exceptions.html#SyntaxError).

**To Fix**: Ensure that the syntax you are using is supported by the Python version on your Frappe Cloud Bench.

### Could not find a version that satisfies the requirement

The app has specified a dependency version that does not actually exist. [Example](https://stackoverflow.com/questions/44674838/no-matching-distribution-found-for-django).

**To Fix**: Ensure that the version of the dependency mentioned in your `requirements.txt` or `pyproject.toml` file exists and is installable by `pip`.

  


  


  


  


  

<!-- page: cloud/cloud__common-issues__forgot-password-of-frappe-cloud.md -->
---
title: "Forgot Password"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/forgot-password-of-frappe-cloud"
updated: "2026-02-16"
---

If you've forgotten your Frappe Cloud password, you can use the **forgot password** link in the login page to obtain instructions to recover your account

[Screenshot on the live page]

<!-- page: cloud/cloud__common-issues__incompatible-app-version.md -->
---
title: "Incompatible app version"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/incompatible-app-version"
updated: "2026-02-16"
---

If you have been seeing a message such as this it means that an app on your bench group is not compatible with some other apps.

[Screenshot on the live page]  


Going forward, I'll use the example of *HRMS*.

*HRMS* depends on *Frappe.* Not just any version of *Frappe,* but a version that satisfies the version (or version range) specified by it. For example: **>=16.0.0-dev,<17.0.0**.

This requirement is mentioned in an apps `pyproject.toml` file. For [example](https://github.com/frappe/hrms/blob/c1704c9767b9c78b23d67cb6b0514afc084cc0dd/pyproject.toml#L69):

[Screenshot on the live page]  


To fix this, you will have to change to the correct branch**:**

* Navigate to the **Apps** tab on your **Bench Group**
* Locate the app to be updated
* Click on **Change Branch** under the `···` menu button:

[Screenshot on the live page]  


If you are unsure which branch to change to, you can check the app's version by checking it's `__init__.py` file, [example](https://github.com/frappe/frappe/blob/6fb6c4035cb4bd17e22143f7c483af34a296ca0c/frappe/__init__.py#L52):[Screenshot on the live page]  



> We change the branch because branches are used to maintain specific versions of an app. In this cause you would change *Frappe* to the `develop` branch, which at the time of writing is on version **16.0.0-dev**
> 
> 

  

<!-- page: cloud/cloud__common-issues__incompatible-dependency-version.md -->
---
title: "Incompatible dependency version"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/incompatible-dependency-version"
updated: "2026-02-16"
---

If your Frappe Cloud build is failing with an "Incompatible `dependency` version" message, it means that one of your `bench` dependencies is incompatible one or more of the apps you want to add to your `bench`.

### **How to fix?**


> The example below shows you how to correct Node's version.
> 
> You can use the same steps to correct the version of **any dependency**.
> 
> 

To fix this issue:

* Navigate to the **Dependencies** tab on your **Bench Group**
* Locate the **Node Version** entry. Or the entry to which ever dependency you need to correct.
* Click on **Edit** under the `···` menu button:

[Screenshot on the live page]  



> ℹ️ **Tip**
> 
> To set a custom dependency version view [this documentation page](https://frappecloud.com/docs/benches/editing-bench-dependency-version#setting-a-custom-version).
> 
> 

You should see an **Edit Dependency** dialog pop up:

[Screenshot on the live page]  


Select the correct **Node Version,** click on **Edit** to save the setting. Then try updating your Bench Group.


> If your build still does not succeed, raise a support ticket and we'll help you out.
> 
> 

<!-- page: cloud/cloud__common-issues__incompatible-node-version.md -->
---
title: "Incompatible Node version"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/incompatible-node-version"
updated: "2026-02-16"
---

If your Frappe Cloud build is failing with an `***engine "node" is incompatible***` message such as this:


```
$ yarn install
yarn install v1.22.22
[1/5] Validating package.json...
error customization_forms@1.0.0: The engine "node" is incompatible with this module. Expected version ">=18.0.0". Got "16.16.0"
error Found incompatible module.
```
It means that Node version on your bench group is different from what is required by the app.

To fix this issue:

* Navigate to the **Dependencies** tab on your **Bench Group**
* Locate the **Node Version** entry
* Click on **Edit** under the `···` menu button:

[Screenshot on the live page]  



> ℹ️ **Tip**
> 
> To set a custom dependency version view [this documentation page](https://frappecloud.com/docs/benches/editing-bench-dependency-version#setting-a-custom-version).
> 
> 

You should see an **Edit Dependency** dialog pop up:

[Screenshot on the live page]  


Select the correct **Node Version,** click on **Edit** to save the setting. Then try updating your Bench Group.


> If your build still does not succeed, raise a support ticket and we'll help you out.
> 
> 

<!-- page: cloud/cloud__common-issues__internal-server-error-on-frappe-site.md -->
---
title: "Internal Server Error On Frappe Site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/internal-server-error-on-frappe-site"
updated: "2026-02-16"
---

More often than not, this error represents some application related issue. If your site is on custom bench group, then you can investigate the same with [logs](https://frappecloud.com/docs/logs) or [ssh access](https://frappecloud.com/docs/benches/ssh). It is a possibility that your custom app is throwing an error. You can view the same in **web.error.log**. Refer our [docs](https://frappecloud.com/docs/benches/debugging) for the same.

If you occassionally get a pop-up with the same message, it is likely that a background job is failing. In such cases, checking your **Scheduled Job Log, Error Log** and **worker.err.log** file should help.

<!-- page: cloud/cloud__common-issues__invalid-pyprojecttoml-file.md -->
---
title: "Invalid pyproject.toml file"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/invalid-pyprojecttoml-file"
updated: "2026-02-16"
---

If your build has failed due to this error then it means that the TOML syntax in your `pyproject.toml` file ([example](https://github.com/frappe/frappe/blob/0a814073043619e4621296b5fa6cf6a7c6406498/pyproject.toml)) is invalid.

For instance, you may have mentioned your the dependencies in the app's `pyproject.toml` like so:


```
dependencies = [
    Babel
    Click
    filelock
]
```
but the actual format is this:


```
dependencies = [
    "Babel~=2.13.1",
    "Click~=8.1.7",
    "filelock~=3.13.1",
]
```
To fix this issue:

1. If the repository is not yours, contact the developer and ask them to fix the file.
2. If the repository is yours, fix the file and push the changes to the repository.

Once the format has been fixed, you can retry the deploy.

<!-- page: cloud/cloud__common-issues__oom-issues.md -->
---
title: "Out-of-Memory Issues"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/oom-issues"
updated: "2026-02-16"
---

If an agent job fails due to the error


```
Traceback (most recent call last):
  File "/home/frappe/agent/repo/agent/base.py", line 50, in execute
    output, returncode = self.run_subprocess(
  File "/home/frappe/agent/repo/agent/base.py", line 103, in run_subprocess
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command 'docker exec -w /home/frappe/frappe-bench bench-xxxxx-000xxxx-fxx-reg bench --site site.frappe.cloud migrate --skip-search-index --skip-failing' returned non-zero exit status 137.
```
it means that your server ran out of memory and should ideally be upgraded to ease the load on the server. To upgrade your dedicated server refer [this guide](https://frappecloud.com/docs/servers/plan)

<!-- page: cloud/cloud__common-issues__required-app-not-found.md -->
---
title: "Required app not found"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/required-app-not-found"
updated: "2026-02-16"
---

If you have been seeing a message such as this, it means that your bench group is missing a required Frappe app that is a dependency of another app on your bench group.

[Screenshot on the live page]  


What does this mean?
--------------------

This can mean one of two things:

* The required app is not present on your bench group.
* The app present on your bench group is not from the correct org.

The message that you see might mention the **app** and the **org**. For example, **frappe/erpnext** i.e. `frappe` is the **org** and `erpnext` is the **app**. This means that your bench group should be having ERPNext from [this repository](https://github.com/frappe/erpnext) (frappe/erpnext).

If the message just mentions the **app**, for example **erpnext**, then ERPNext from any repository should do.

How to fix this?
----------------

### App org is incorrect

To fix this, you will have to remove the existing app (with the incorrect org) from your bench group.

To do so, navigate to the **Apps** tab on your bench group, scroll to your app, then click on the `···` menu button and click on **Remove App**:

[Screenshot on the live page]  


After this is done, you will have to add the correct app. Check the next section (**App is not present**) for this.

### App is not present

To fix this navigate to the **Apps** tab on your bench group and then click on **Add App**:[Screenshot on the live page]  


after that navigate through the Add App dialog to add the missing app.


> ⚠️ If the org is mentioned in the message above, ensure that the added app's org matches the mentioned one.
> 
> 

Why does this happen?
---------------------

Frappe Framework apps can have dependencies on other Frappe Framework apps, without which they cannot function. For example: HRMS requires ERPNext to be installed to function.

This requirement is mentioned in one of two places:

* An app's `hooks.py` file ([example](https://github.com/frappe/hrms/blob/539cbe9c8a04c11940a0d8b2f9b8710f16182565/hrms/hooks.py#L7))
* An app's `pyproject.toml` file ([example](https://github.com/frappe/hrms/blob/539cbe9c8a04c11940a0d8b2f9b8710f16182565/pyproject.toml#L70))

Using your own version of the dependency
----------------------------------------

If you need to use your own version of the dependency (example `your_org/erpnext` instead of `frappe/erpnext`), you will have to:

1. Fork the dependent app (example fork `your_org/hrms` from `frappe/hrms`)
2. Edit the `hooks.py` and `pyproject.toml` files of the fork
3. Remove dependent app (example `frappe/hrms`) from your bench group
4. Add the forked version (example `your_org/hrms`) to your bench group

<!-- page: cloud/cloud__common-issues__ssl-certificate-verification-error.md -->
---
title: "SSL Certificate Verification Error"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/ssl-certificate-verification-error"
updated: "2026-03-11"
---

You may run into SSL: CERTIFICATE_VERIFY_FAILED in your custom app when attempting to connect to an endpoint outside of Frappe Cloud. This tends to happen due to 2 reasons mainly:

1. **SSL is not configured correctly on the server you are trying to connect to.**
  It may be not serving the full chain of certificates and hence python's SSL module [cannot validate](https://github.com/python/cpython/issues/62817) the TLS connection. Browsers can however connect to such servers as they implement [AIA](http://www.pkiglobe.org/auth_info_access.html). You can verify this by using online tools like [https://www.ssllabs.com/](https://www.ssllabs.com/). In this case, the server should be correctly configured to serve the full chain of certificates.
2. **Python can't use OS certificate store.**
  To resolve this, you can [install](https://frappecloud.com/docs/faq/custom_apps#how-to-add-python-dependencies-to-my-custom-app-eg-pandas) [pip-system-certs](https://pypi.org/project/pip-system-certs/) package in your custom app as suggested in this stackoverflow [thread](https://stackoverflow.com/questions/77442172/ssl-certificate-verify-failed-certificate-verify-failed-unable-to-get-local-is).

<!-- page: cloud/cloud__common-issues__vite-not-found.md -->
---
title: "Vite not found"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/vite-not-found"
updated: "2026-02-16"
---

If you build has been failing at the **Install Apps** stage with `vite: not found` in the build output, such as this:

[Screenshot on the live page]  


Then it means that the `vite` build dependency wasn't installed when your app was being installed.

Why does this happen?
---------------------

This can happen if your project has two `package.json` files such as this ([repository](https://github.com/frappe/gameplan)):

[Screenshot on the live page]  


And if the **outer** `package.json` does not have a `postinstall` script that installs packages mentioned in the **inner** `package.json`.

How to fix this?
----------------

Ensure that your **outer** `package.json` has a `postinstall` script with a line similar to this:


```
cd frontend && yarn install
```
Here `frontend` is the folder with the **inner** `package.json`.

You can use [frappe/gameplan](https://github.com/frappe/gameplan/blob/89315d218ba91b8ccbc477930128e57595c8c07a/package.json#L5) as a reference point.

<!-- page: cloud/cloud__connect-apache-superset.md -->
---
title: "Apache Superset"
space: "Cloud"
url: "https://docs.frappe.io/cloud/connect-apache-superset"
updated: "2026-02-16"
---


> **Apache Superset** is an open-source modern data exploration and visualization platform.


1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]
2. Open your Superset dashboard and go ahead with connecting a new database.

[Screenshot on the live page: Screenshot 2025-01-31 at 2.53.56 PM]
3. Choose **MySQL** as database type.

[Screenshot on the live page: Screenshot 2025-01-31 at 2.54.49 PM]
4. Fill in all the required details and ensure the **SSL** checkbox is checked. Then, proceed.

[Screenshot on the live page: Screenshot 2025-01-31 at 2.56.20 PM]
5. You will see this message upon a successful connection.

[Screenshot on the live page: Screenshot 2025-01-31 at 3.19.46 PM]
6. Now, you can refer to the [official documentation](https://superset.apache.org/) to create a dashboard in Superset.

<!-- page: cloud/cloud__connect-looker-studio.md -->
---
title: "Looker Studio"
space: "Cloud"
url: "https://docs.frappe.io/cloud/connect-looker-studio"
updated: "2026-02-16"
---


> [Looker Studio](https://lookerstudio.google.com/navigation/reporting) is a free, online tool that helps users create and share interactive dashboards and reports from data. It was formerly known as Google Data Studio. 
> 
> 

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.

  


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]
2. Go to Looker Studio and click on **Create New Data Source** !

[Screenshot on the live page: Screenshot 2025-01-31 at 1.39.14 PM]
3. Search for **mysql** in connector list and choose the connector from Google.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.40.34 PM]
4. Fill up the database user's info and click on **Authenticate**. 

  


**Note :** You need to check **Enable SSL** and must provide the SSL certificate. Check the representation image of **Step 1** of this documentation to get the idea from where to download the certificate.

  


[Screenshot on the live page: Screenshot 2025-01-31 at 1.45.07 PM]
5. Choose the required table and click on **Connect**.
6. After that, you can see the details of the table and create required reports. 

[Screenshot on the live page: Screenshot 2025-01-31 at 1.59.10 PM]
7. Check Looker Studio [office documentation](https://cloud.google.com/looker/docs/intro) to get guidance on creating dashboards and reports.

  

<!-- page: cloud/cloud__connect-metabase.md -->
---
title: "Metabase"
space: "Cloud"
url: "https://docs.frappe.io/cloud/connect-metabase"
updated: "2026-02-16"
---


> [Metabase](https://www.metabase.com/) is an open-source business intelligence (BI) tool that allows users to explore data, create dashboards, and visualize data
> 
> 

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.

  


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**

  


[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]
2. Open your Metabase dashboard and click on **Add database**.
3. Choose **MySQL** as Database Type and fill all the database user related information.  
  


**Note :** Ensure that `Use a secure Connection (SSL)` is checked.

  


For **Server SSL certificate Chain**, check the **Step 1** and download the certificate first. Next, open your operating system's default text editor and copy- paste to metabase. 

[Screenshot on the live page: Screenshot 2025-01-31 at 2.14.10 PM]
4. Once all the details filled, click on **Save**.
5. If everything works fine, you will see your database in the list.

[Screenshot on the live page: Screenshot 2025-01-31 at 2.19.23 PM]
6. Wait a few minutes for the table schema to sync, then you can view the metadata.

[Screenshot on the live page: Screenshot 2025-01-31 at 2.26.22 PM]
7. Once this step is complete, you can follow the [official documentation](https://www.metabase.com/docs/latest/) to create the dashboard and reports.

<!-- page: cloud/cloud__connect-power-bi-desktop.md -->
---
title: "Power BI Desktop"
space: "Cloud"
url: "https://docs.frappe.io/cloud/connect-power-bi-desktop"
updated: "2026-02-16"
---


> [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) is an interactive data visualization software product developed by Microsoft with a primary focus on business intelligence (BI).
> 
> 

Step 1: Create Site Database User
---------------------------------

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.
2. Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]

Step 2: Install MariaDB ODBC connector
--------------------------------------

1. Download MariaDB ODBC Connector v3.1.x ([Download link](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector)). 


> **Note**: Please avoid installing v3.2.x as it has a [bug](https://community.fabric.microsoft.com/t5/Power-Query/Excel-Power-Query-issue-with-MariaDB-ODBC-driver/m-p/4320893) that causes it to not work with Power BI.
> 
> 

[Screenshot on the live page: 256]
2. Install ODBC Connector.

[Screenshot on the live page: ss2 1]  


[Screenshot on the live page: ss3]  


[Screenshot on the live page: ss5]

Step 3: Setup Credentials in ODBC
---------------------------------

1. Open **ODBC Data Sources** with **Run as administrator.**


> **Note :** If you have installed ODBC connector of x64 version, then you should open `ODBC Data Sources (64-bit)` and if you have downloaded and installed x32 version, then open `ODBC Data Sources (32-bit)`
> 
> 

[Screenshot on the live page: ss12]
2. Click on **Add** button in **User DSN** tab.

[Screenshot on the live page: ss19]
3. Choose **MariaDB ODBC 3.1 Driver**.

[Screenshot on the live page: 27]
4. Put the **Server Name** , **Port**, **Use Name** , **Password**, **Database** in the required fields and go to next page.


> **Note:** Currently If you try to click on **Test DSN**, it will fail. We need to do few more configurations to make it working.
> 
> 

[Screenshot on the live page: ss14]
5. No information is needed on the current page. Proceed to the next page.

[Screenshot on the live page: 17]
6. No information is needed on the current page. Proceed to the next page.

[Screenshot on the live page: 18]
7. In current page, make sure to check **Verify Certificate** & **Force TLS Use** checkbox.

[Screenshot on the live page: ss17]
8. No information is needed on the current page. Click on **Finish** to save it.

[Screenshot on the live page: ss18]

Step 4: Configure MariaDB ODBC In Power BI Desktop
--------------------------------------------------

1. Open Power BI and click on **Get Data From Other Sources**.

[Screenshot on the live page: ss6]
2. Search for **ODBC** and click on **Connect**.

[Screenshot on the live page: ss20]
3. Choose the ODBC connection from the list. It should be the same you have created in **ODBC Data Sources Administrator** in **Step 3**.

[Screenshot on the live page: 21]
4. Now, it might ask you for username and password. Choose **Windows** from the sidebar and click on **Connect**.

[Screenshot on the live page: 25]
5. Once connected, you will be able to view all the tables and their previews.

[Screenshot on the live page: 257]
6. Now, follow the [official documentation](https://learn.microsoft.com/en-us/power-bi/) to create dashboards and reports in Power BI.

<!-- page: cloud/cloud__connect-zoho-analytics.md -->
---
title: "Zoho Analytics"
space: "Cloud"
url: "https://docs.frappe.io/cloud/connect-zoho-analytics"
updated: "2026-02-16"
---


> [Zoho Analytics](https://www.zoho.com/analytics/) is a business intelligence (BI) and analytics platform that helps users analyze data, create reports, and gain insights.
> 
> 

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.

  


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**.

[Screenshot on the live page: Screenshot 2025-01-31 at 1.15.44 PM]
2. Open your Zoho Analytics dashboard and go to **Import Data** page.

Search & Select **MariaDB** from the list**.**  
[Screenshot on the live page: Screenshot 2025-01-31 at 3.28.14 PM]
3. Change **Cloud Service Provider** to **Other Cloud Services** and fill all the required details.   
Make sure to check **SSL** checkbox.

[Screenshot on the live page: Screenshot 2025-01-31 at 3.37.43 PM]
4. Choose the tables to import and Schedule it.

[Screenshot on the live page: Screenshot 2025-01-31 at 3.39.33 PM][Screenshot on the live page: Screenshot 2025-01-31 at 3.41.40 PM]
5. You will be able to see the data sources in your dashboard.

[Screenshot on the live page: Screenshot 2025-01-31 at 3.48.50 PM]
6. Now, you can refer to the [Zoho Analytics official documentation](https://www.zoho.com/analytics/help/) to create reports and dashboards.

<!-- page: cloud/cloud__control-resources-allocated-for-site.md -->
---
title: "Control resources allocated for site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/control-resources-allocated-for-site"
updated: "2026-06-05"
---

## Performance mode toggle

From the site detail page, under **Dangerous Actions**, you can toggle performance mode for a site on a dedicated server.





[Screenshot on the live page: Configure compute allocation in Dangerous Actions]



### How worker allocation works

## 

Changing the performance mode directly affects the number of workers on your bench. Every active bench on a server gets a proportional share of the server's total worker capacity. This runs automatically via `auto_scale_workers`, which calls `allocate_workers` on each bench.

### Workload score

## 

Each bench gets a [workload score](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L662): the sum of `cpu_time_per_day` from the plan of every active, pending, or updating site on that bench. The server's [total workload](https://github.com/frappe/press/blob/develop/press/press/doctype/server/server.py#L3712) is the sum across all its [benches](https://github.com/frappe/press/blob/develop/press/press/doctype/server/server.py#L3695).

The performance mode controls which plan a site is on, and therefore its `cpu_time_per_day` contribution to the workload score:

- **High performance** → `cpu_time_per_day: 86000`
- **Not high performance** → `cpu_time_per_day: 8000`

### Server RAM budget

## 

Usable RAM is [calculated first](https://github.com/frappe/press/blob/develop/press/press/doctype/server/server.py#L3716), then split between the two worker pools:

```
usable_ram      = max(total_ram - 3000 MB, total_ram × 0.75)
gunicorn pool   = 60% of usable_ram   →  max_gunicorn_workers = pool / 150 MB
background pool = 40% of usable_ram   →  max_bg_workers       = pool / 240 MB
```

150 MB = avg per gunicorn worker (`GUNICORN_MEMORY`). 240 MB = avg per set of 3 background workers (`BACKGROUND_JOB_MEMORY`).

#### Per-bench allocation formula

## 

Each bench gets a share proportional to its workload, [clamped to the release group's configured bounds](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L793):

```
gunicorn_workers   = clamp(min_gn..max_gn,  round(bench_workload / server_workload × max_gunicorn_workers))
background_workers = clamp(min_bg..max_bg,  round(bench_workload / server_workload × max_bg_workers))
```


| Worker type | Default min | Default max |
| ----------- | ----------- | ----------- |
| Gunicorn    | 2           | 36          |
| Background  | 1           | 8           |


These are overridden if the release group has explicit `min/max_gunicorn_workers` or `min/max_background_workers` set. If total server workload is zero, [every bench falls back to the minimums](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L828).

#### Threaded workers

## 

If `gunicorn_threads_per_worker` is set on the bench, the gunicorn count is [reduced after the proportional step](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L809) to keep total concurrency the same while using fewer processes:

```
gunicorn_workers = clamp(1..max_gn, ceil(gunicorn_workers / gunicorn_threads_per_worker))
```

#### Memory limits

## 

When `set_bench_memory_limits` is on, [cgroup limits are set per bench](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L832):

```
memory_high = 512 MB + (gunicorn_workers × 150 MB) + (background_workers × 240 MB)
memory_max  = memory_high + 150 MB + 240 MB
memory_swap = memory_max × 2
```

If `skip_memory_limits` is set on the bench, it gets the server's [maximum possible limits](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L386) instead. When memory limits are off, [all three are set to 0](https://github.com/frappe/press/blob/develop/press/press/doctype/bench/bench.py#L842).

<!-- page: cloud/cloud__custom-apps__app-versioning__versioning.md -->
---
title: "Versioning"
space: "Cloud"
url: "https://docs.frappe.io/cloud/custom-apps/app-versioning/versioning"
updated: "2026-08-05"
---

## Overview

Adding a `pyproject.toml` file to your Frappe app is now **mandatory**.  
This file must declare the app’s supported Frappe versions using the following section:

```toml
[tool.bench.frappe-dependencies]

```

This allows **Frappe Cloud** to validate application compatibility during operations like:

- `bench update`
- App installation
- App addition to a bench group

---

## Required Configuration

Add a `pyproject.toml` file to the **root directory of your app repository** with content similar to:

```toml
[tool.bench.frappe-dependencies]
frappe = ">=16.0.0-dev,<=17.0.0"

```

### Explanation

- `tool.bench.frappe-dependencies`  
Declares compatibility requirements for Frappe.
- `frappe`  
Specifies the supported version range using standard version specifiers.

This ensures the platform can validate whether the app is compatible with the target bench version.

---

## Common Errors

### 1️⃣ Missing `pyproject.toml`

**Error Meaning**

Indicates that no `pyproject.toml` file exists in the root of the application repository.

[Screenshot on the live page]

**Resolution**

Create the file and add the required dependency section.

---

### 2️⃣ Missing `[tool.bench.frappe-dependencies]` Section

**Error Meaning**

The `pyproject.toml` exists, but the required dependency section is not defined or not in the exact format as mentioned above.

[Screenshot on the live page]

**Resolution**

Add:

```toml
[tool.bench.frappe-dependencies]
frappe = "<version-range>"

```

---

### 3️⃣ Version Mismatch With Bench

**Error Meaning**

The app branch declares compatibility with a Frappe version different from the bench version.

Example scenario:

- Bench group version → **15**
- App branch → declares **develop (v16+)**

This branch will be rejected.

[Screenshot on the live page]

**Resolution**

Ensure:

- The declared version range matches the target bench version
- Or switch to a compatible app branch

---

## Best Practices

- Always keep the version range updated when releasing new branches
- Align branch naming with supported Frappe versions
- Validate compatibility locally before pushing changes
- Use semantic version ranges rather than hard pinning

---

## Summary

The `pyproject.toml` dependency declaration enables automated compatibility checks across Frappe Cloud infrastructure.  
Ensuring correct configuration prevents installation failures and version conflicts during bench operations.

<!-- page: cloud/cloud__custom-apps__common-issues__github-ip-allow-list.md -->
---
title: "GitHub IP Allow List"
space: "Cloud"
url: "https://docs.frappe.io/cloud/custom-apps/common-issues/github-ip-allow-list"
updated: "2026-06-05"
---

If your GitHub organisation has the **IP Allow List** feature enabled, Frappe Cloud's servers may be blocked from making authenticated API calls and cloning repositories during deployments, even when valid credentials are provided. 

When Frappe Cloud attempts to list repositories accessible to the connected GitHub user, the following error is returned:

```json
{
  "message": "Although you appear to have the correct authorization credentials, the organisation has an IP allow list enabled, and your IP address is not permitted to access this resource.",
  "documentation_url": "https://docs.github.com/rest/apps/installations#list-repositories-accessible-to-the-user-access-token",
  "status": "403"
}

```



This affects:



- The **repository dropdown** in the Frappe Cloud dashboard (shows "No results found")
- **Deployments**: build servers cannot clone private repositories
- Any **background jobs** that pull releases from GitHub

## What Is GitHub's IP Allow List?

GitHub's IP Allow List is a security feature that restricts access to organisation resources (repositories, API, etc.) to only a defined set of trusted IP addresses.



### Availability




| Plan                                  | IP Allow List Available |
| ------------------------------------- | ----------------------- |
| GitHub Free (personal)                | ❌ No                    |
| GitHub Team                           | ❌ No                    |
| **GitHub Enterprise Cloud**           | ✅ Yes                   |
| **GitHub Enterprise Server**          | ✅ Yes                   |
| GitHub Advanced Security (standalone) | ❌ No                    |


> This is a **GitHub Enterprise Cloud / Enterprise Server exclusive feature**.
>
> Source: [GitHub Docs — Managing allowed IP addresses for your organisation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)



### Where Is It Configured?

```
https://github.com/organizations/{your-org}/settings/security

```



Under: **Organisation Settings → Security → IP allow list**



---



## Root Cause

Frappe Cloud's production and build servers operate from fixed public IPs. If these IPs are not on the organisation's IP allow list, all GitHub API requests and git clone operations originating from Frappe Cloud will be rejected with a `403`.



---



## IPs to Whitelist

The following Frappe Cloud IPs must be added to the GitHub organisation's IP allow list:



### Frappe Cloud Production Server

*(Handles GitHub API calls — repo listing, branch fetching, webhook processing)*






| IP Address      | Purpose                  |
| --------------- | ------------------------ |
| `139.59.79.221` | Frappe Cloud prod server |


### Build Servers

*(Clone repositories during app deployments)*






| IP Address       | Purpose      |
| ---------------- | ------------ |
| `13.205.88.211`  | Build server |
| `43.205.115.209` | Build server |
| `13.127.110.154` | Build server |
| `64.227.148.209` | Build server |
| `139.59.9.202`   | Build server |
| `64.227.183.30`  | Build server |




## Steps to Whitelist

1. Go to `https://github.com/organizations/{your-org}/settings/security`
2. Scroll to **IP allow list**
3. Click **Add**
4. Enter each IP above with a descriptive label
5. Save
6. Repeat for all 7 IPs

Once all IPs are added, return to the Frappe Cloud dashboard and retry adding the GitHub app. The repository dropdown should now populate correctly. If this still doesn't work, please reach out to Frappe Cloud support.



## Notes

- These IPs are Frappe Cloud's **shared infrastructure IPs** and are the same for all customers on the platform
- If your site is on a **dedicated/private Frappe Cloud cluster**, the IPs may differ — contact [Frappe Cloud support](https://frappecloud.com/support) to confirm the correct egress IPs.

<!-- page: cloud/cloud__custom-frappe-framework-fork.md -->
---
title: "Custom Frappe Framework Fork"
space: "Cloud"
url: "https://docs.frappe.io/cloud/custom-frappe-framework-fork"
updated: "2026-02-16"
---

You can use your custom version/fork of the vanilla Frappe Framework.

:::caution
We do not provide support for modified versions of the framework.
:::



You can do so by simply following the add app flow inside your Bench Groups.

[Screenshot on the live page: Screenshot 2024-11-20 112324]

This will replace the Vanilla Frappe Framework with your custom fork / version.

<!-- page: cloud/cloud__daily-usage-limit-reached.md -->
---
title: "Daily Usage limit reached"
space: "Cloud"
url: "https://docs.frappe.io/cloud/daily-usage-limit-reached"
updated: "2026-05-25"
---

[Screenshot on the live page]

This happens when you exceed CPU hours allotted for your site. If you're confused as to how you reached your CPU hours limit, you can check the **Insights** tab of your site.

[Screenshot on the live page]

Here, you can scroll down to **Advanced analytics** to see:the **Slowest Requests** and **Slowest Background Jobs** graphs. This will give you an idea of which endpoints in your site take most time/requests. We can take a look at the following graphs as an example

[Screenshot on the live page]

Here, the red bars are seem to take relatively long and should be looked into.

[Screenshot on the live page]

It is sorted in descending order, so the first endpoints in the list are usually slowest.

<!-- page: cloud/cloud__database-analyzer.md -->
---
title: "Database Analyzer"
space: "Cloud"
url: "https://docs.frappe.io/cloud/database-analyzer"
updated: "2026-04-26"
---

This tool can help you analyze storage usage of your database and find performance issues in the database as well.

## How to access the tool ?

Visit frappecloud.com/dashboard and check the sidebar. From Sidebar > Dev Tools > DB Analyzer, you can acccess the tool.

Or, you can simply visit - [https://frappecloud.com/dashboard/database-analyzer](https://frappecloud.com/dashboard/database-analyzer)

[Screenshot on the live page]

## Storage Breakdown

If you want to check disk usage by every table in your database, you can click on the `Storage Bar`

You can then view usage by each table

[Screenshot on the live page]

## Database Processes

If you want to view all the active database queries, you can view them from the same page and even kill the query if it's stuck.

[Screenshot on the live page]



## Database Locks

MairaDB lock report helps to find active locks on the specific database. This helps with investigating `lock timeout error` issues.

[Screenshot on the live page]

## Slow Queries

Slow queries usually affect the performance of your site. You can find all the information about slow queries.

[Screenshot on the live page]

## Time Consuming Queries

Sometimes there are queries that execute very fast but run very frequently and, in total, consume a lot of your database's CPU time.

These queries don't always affect database performance, but the results can help you further optimize your code.

[Screenshot on the live page]

## Full Table Scan Queries

If queries lack indexing or have issues, they can cause full table scans, which hurt your database performance the most.

You can find these kinds of queries and optimize them for better performance.

[Screenshot on the live page]

## Index Analysis

Other than that, you can click on `Suggest Indexes`, and the system will try to analyze slow queries and provide suggestions based on that.

[Screenshot on the live page]
