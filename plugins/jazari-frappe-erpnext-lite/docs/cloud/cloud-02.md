<!-- Frappe documentation: cloud, part 2 of 3. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__local-fc-setup.md -->
---
title: "Local Development Environment Setup"
space: "Cloud"
url: "https://docs.frappe.io/cloud/local-fc-setup"
updated: "2026-02-16"
---

This guide shows you how to setup your development machine for Frappe Cloud development. By the end of this guide, you will have a replica of the FC production environment.

> "Patience is bitter, but its fruit is sweet." – Aristotle

## Introduction

- `**f` servers**: These host your bench (`f` is for Frappe Apps)
- `**m` servers**: These host the database (`m` is for MariaDB)
- `**n` servers**: These are proxy servers (`n` is Nginx, which does the proxying)

## Prerequisites

### Softwares

You should have the following software packages installed on your computer before proceeding:

1. Docker: Latest, don't forget to give `docker` sudo access!
2. Certbot: Latest
3. dns-route53 plugin for certbot: `pip3 install certbot-dns-route53`

### Credentials from Frappe Assets

You will need access to the following IAM accounts. If you're working at Frappe, you can request them from `Frappe Assets` at frappe.io:

1. Hetzner
2. Digital Ocean
3. AWS

## Creating Servers on Hetzner

Hetzner is a cloud hosting provider that we will use to create our servers (`n`, `f` and `m`). In production, we use Digital Ocean but for development purposes, Hetzner is a better value for money.

The naming convention used can be seen in the servers list:

`<server-type><server-number>.<name-initial>.fc.frappe.dev`

For example, `f1.g.fc.frappe.dev` is the first `f` server and `g` is for Gavin.

> Don't forget to add your default public SSH keys during server creation as Ansible plays rely on default SSH keys.

Now, create **3 servers** in the `Helsinki` region, using either `Ubuntu 20.04` or `Ubuntu 22.04` as the operating system. Other Ubuntu versions will introduce incompatible package dependencies (last verified on Sept 17, 2025).

1. `n1.<unique-name-initial>.fc.frappe.dev`: CPX11 type
2. `f1.<unique-name-initial>.fc.frappe.dev`: CX22 type
3. `m1.<unique-name-initial>.fc.frappe.dev`: CX22 type

After the creation of the above mentioned servers, create a network resource and attach all the servers created above to that network resource.

Note down the Public and Private IP Addresses of all the three servers.

## Creating DNS records in AWS Route53

Go to the AWS Console (again, credentials are in Frappe Assets), navigate to `Route 53 > Hosted Zones`. Click on `fc.frappe.dev` domain name. You have to create 4 DNS `A` records here. One record will be a wild-card sub-domain:

`*.<name-initial>.fc.frappe.dev` pointing to the IP address of the `n` server created in the previous section.

The other 3 records will be for `f1`, `n1` and `m1` respectively. Use the IP address from the previous step. You can have a look at other such records if you get confused at any point.

Now, make sure you can `ssh` (as `root`) into all the three servers using their domain names. For example:

```bash
ssh root@f1.h.fc.frappe.dev
```

## Create your `press` site

On your computer, run `bench get-app https://github.com/frappe/press`.

> If you are on an M series Mac computer and you get an error related to "go" when installing press, here's what you can try:
> 1. Install go binary: `brew install go`
> 2. Run: `go env -w GO111MODULE=off`
>
> After this, try running the get-app command again.

Now, create a new site and install `press` on this site.

Open the site and login as Administrator.

## Press Settings

### Create a `Root Domain`

Navigate to `Root Domain List` (AwesomeBar to rescue!) and create a new document. Fill up the details as below:

- **Name**: `<your-domain-name>`, e.g. `h.fc.frappe.dev`
- **Default Cluster**: `Default`
- **AWS Access Key ID**: Get from `AWS Console`
- **AWS Secret Access Key**: Get from `AWS Console`

Save it.

> You can get your Access Keys by going to AWS Console > IAM > User > John Doe (create one if required) > Security credentials > Access Keys

Open `Press Settings` now. Set the `Domain` to the root domain you created in the previous step and cluster to `Default`.

Now, there is going to be a lot of back and forth between your terminal and `Press Settings`, so sit tight.

### Let's Encrypt

Scroll down and expand the `Let's Encrypt` section. Before entering the details here, you have to create two directories on your local computer (it is better to place this at user level, e.g. `/home/<user>/`):

1. `.certbot` → directory
2. `webroot` → directory, inside the .certbot directory

Now, fill the `Certbot Directory` and `Webroot Directory` with the absolute path of the above two newly created directories respectively. Leave out other fields as it is. You can enter your email if you want.

Save the settings.

### Docker

Now, scroll down to `Docker Registry` section.

Fill in the fields as given below:

- **Docker Registry URL**: `registry.digitalocean.com/staging-frappe-cloud`
- **Docker Registry Namespace**: Any name you like, e.g. `hussain-staging`

Download Docker Credentials from [https://cloud.digitalocean.com/registry/settings?i=abbd47](https://cloud.digitalocean.com/registry/settings?i=abbd47) and then decode the auth string and use it for both `Docker Registry Username` and `Docker Registry Password`.

> The decoded string should be in the following format:
>
> `dop_v1_daaaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:dop_v1_daaaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
>
> Use the string before colon (`:`) as `Docker Registry Username` and `Docker Registry Password`

Again, save the settings and scroll down to `Docker Build` section.

Go to your terminal and `cd` into your `bench` directory. Create two directories here:

1. `.clones`
2. `.docker-builds`

Go back to the `Press Settings` and paste the absolute paths of the above two directories to the `Clone Directory` and `Build Directory` respectively. Leave the other field empty and save the settings.

Sometimes, there is an issue while uploading a docker image in the background and you have to manually `push` it to registry. For that case, you have to login to Digital Ocean registry through docker before pushing. You can do this by running this command:

```bash
docker login -u <username> -p <password> registry.digitalocean.com
```

### Stripe Settings (optional)

This step is optional and is required only if you are planning to work on billing. In the Stripe Settings section, create a new Stripe Account from the link field.

You can signup for a new Stripe account from [https://dashboard.stripe.com/](https://dashboard.stripe.com/). By default, Stripe gives you a test account which is enough for our development purposes.

Get the Publishable Key and Secret Key from Stripe dashboard and create your Stripe Account and set it in Press Settings. Set values for Credits on Signup fields. For e.g., INR 1800 and USD 25.

Now click on Create Stripe Webhook. It should create webhook endpoints on Stripe and set the field Stripe Webhook Endpoint ID.

That's it for Stripe Settings.

## Setting up SSH Agent

Before proceeding to the following steps, we need to make sure you are able to SSH to the aforementioned servers without being prompted for a password. This is done using SSH keys.

If your private key is encrypted with a passphrase, this passphrase must be entered every time you attempt to connect to an SSH server using public-key authentication. Each individual invocation of ssh or scp will need the passphrase in order to decrypt your private key before authentication can proceed. This prompt will block Ansible Plays from running through press.

An SSH agent is a program which caches your decrypted private keys and provides them to SSH client programs on your behalf. In this arrangement, you must only provide your passphrase once, when adding your private key to the agent's cache.

Make sure your private key file has correct permissions:

```bash
chmod 600 <your SSH folder>/id_rsa
```

### Linux instructions (MacOS users must read)

Update your `.zprofile` (or `.bash_profile`) because that's where environment variables are set:

```bash
eval "$(ssh-agent -s)"  # To start the agent
ssh-add <your SSH folder>/id_rsa
```

You can logout and log back in, then run `ssh-add -l` to check if your key is added. If it's not added, you'll get an error like `The agent has no identities.`. If it's added, you'll see the key's fingerprint.

If your key is protected with a passphrase, you should add it to a keyring. You can check this for a guide on how to set it up.

> Note that the above step is NOT OPTIONAL if your private key is protected with a passphrase.

### MacOS instructions

MacOS includes a special variant of ssh-add that allows it to use the keyring easily. Following link won't work if you're using some brew package. Please read this guide on setting up ssh-agent on MacOS.

To confirm if you've done everything correctly, you can restart your computer and run:

```bash
ssh-add -l
```

The output should show your key's fingerprint if everything is set up correctly.

## Setting up Proxy server (`n` server)

Go to the `Proxy Server` list and click `+ Add Proxy Server`. Fill in the details as given below:

- **Hostname**: `n1` (`n2`, `n3`, if you want to create more Proxy servers)
- **IP**: IP Address of the `n` server
- **Private IP**: Private (internal) IP Address of the `n` server. Can be found in `Hetzner` console.

Click on save.

> Note: The agent password will be set automatically for you.

Now, click on the `Actions` dropdown button, which is located next to the `Save` button and click on `Setup Server`. The server doc status should change to `Installing`.

This will setup the server. We use `Ansible` to automate the infrastructure, so, once you click on the `Setup Server` button, `Ansible Play`s will be created and run in the background to setup the server (install necessary software, perform essential configuration changes and more). Each `Ansible Play` document creates a number of `Ansible Task`, which is an individual task that will be carried out to setup the server.

Navigate to `Ansible Task List` and you should see some tasks which will have a particular status. For example, `success` means the task completed successfully and `running` means the task is currently running. You should confirm that all the tasks are eventually `success`ful.

After some time, when the tasks have completed to run, the `Proxy Server` will go to `Active` state.

If there is any error (for example, if the `Proxy Server` goes into `Broken` state) or a task keeps running forever, go to the `Error Log List` and you will most probably find a log that corresponds to the task and more information on why it failed.

> If the Ansible Task "Clone Agent Repository" fails, you might want to generate a personal access token and edit the git clone URL in `press/playbooks/roles/agent/tasks/main.yml` at the agent github URL line. It should be in the format: `"https://<github-username>:<personal-access-token>@github.com:/frappe/agent"`

## Setting up DB server (`m` server)

In this section, we will move on to create a `Database Server`. Go to the `Database Server List` and create a new document. Fill in the fields as given below:

- **Hostname**: `m1`
- **IP**: External IP address of the `m` server
- **Private IP**: Internal IP address of the `m` server

Now, you have to follow the same steps as for the proxy server. Save the document and do setup server. While this server is setting up, you can move on to setting up the `f` server as this takes a long time to finish.

## Setting up App server (`f` server)

In the proxy server section, we created and set up the `Proxy Server` which sits in the front and forwards traffic to various `f` servers. Now, `f` servers are where the benches (along with the sites) are present. The databases are on different `m` servers and the sites hosted in the `f` servers use those databases.

Go to the `Server List` and add a new server document. Fill in the details as given below:

- **Hostname**: `f1`
- **Cluster**: `Default`
- **IP**: External IP address of `f` server
- **Private IP**: Internal IP address of `f` server
- **Proxy Server**: Select the `Proxy Server` which we created in a previous section
- **Database Server**: Select the `Database Server` which we created in the previous section

Look for the `Use for Build` checkbox and enable it.

Leave other fields as they are. Save the document.

Now, click on Actions > Setup Server and wait for it to complete. After that, click on Actions > Add to Proxy.

That's it for the `f` server.

## Setting up Builds

Under **Press Settings** > **Docker** > **Docker Build** set **Build Server** to the app server you have created in the previous step.

Now, when you run a *Build and Deploy*, the image that is created for the deployment will be built on the Build Server.

> **Note**: You need to add **sync** queue in your `common_site_config.json`:
>
> `json > "workers": { >   "sync": { >     "timeout": 300 >   } > } >` 

## Creating a Free Plan

You should create at least one site plan for the tenants to be able to start using the dashboard and creating sites. Without this, the *Create Site* wizard will not work as intended. This can be done using the `Site Plan` doctype. Go ahead and create a Free site plan.

![Site Plan 1](/files/site-plan-16c3ee4.png)

Now under Roles, add `Press Admin` and `Press Member`.

![Site Plan 2](/files/site-plan-2.png)

## Creating an App

The next step is to create an App that will ultimately be installed on our site. The first app in any release group must be `frappe` (Frappe Framework), the name is case sensitive. Navigate to `App List` page and click on `'+ Add new App'` button on the top-right corner. Fill in the details as below:

![New App Frappe](/files/new-app-frappe.png)

## Creating an App Source

Now, we need to create an App source for this app. Navigate to `App Source` list page, create a new document and fill in the details as below:

![App Source](/files/aBnJbGp.png)

## Approving the App Release

Now, go to the `App Release` list page by clicking on the App Release chip. You should see an app release created for the `frappe` app that we created in the previous step. Open that document and change its status from Draft to Approved.

![App Release](/files/Screenshot%202025-09-30%20at%2011.12.24%E2%80%AFAM.png)

## Creating a Release Group

> If you are on a Mac add `export NO_PROXY=* OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` to your shell configuration file (like .zshrc) to avoid having `Agent Jobs` stuck at `Undelivered` status.

Navigate to the `Release Group` list and create a new release group. The details to be filled are shown below.

![New Release Group](/files/new_release_groupa3cb60.png)

Make sure at least one `f` server is added to your chosen *Release Group*. New sites cannot be created if no server is added. Ensure the Release Group is marked **Public**; otherwise, it will remain private and act as an isolated bench.

Go to the `Apps` tab of the release group and select the app source that you created in the previous step, like in the screenshot below.

![New Release Group: Apps tab](/files/new_release_group_2.png)

Now click save.

Once you save the release group document, a `Deploy Candidate` is automatically created for this release group. In fact, a deploy candidate is created any time you make changes to the `Release Group`.

![Created Release Group](/files/created_release_group.png)

Click on the `Deploy Candidate` chip and this will take you to the `Deploy Candidate` page which is filtered for the current `Release Group`. Select the `Deploy Candidate` (are named like `bench-xxx`) that was created latest. You should only have one if you never created a release group before. Now, click on `Actions` and then `Schedule Build and Deploy`.

This will build the docker image for this bench group, upload it to the Digital Ocean image registry and also deploy it to your `f` server.

You can click on `Visit Dashboard` link on the top-left corner to view the progress of the build and deploy step.

> If you see an error like `permission denied while trying to connect to the Docker daemon socket`, it usually means that the updated group permissions have not yet taken effect for the frappe user in the target server. Restarting the virtual machine should start a fresh user session and apply the new group membership, resolving the permission issue.

![Deploy Release Group](/files/deploy_release_group.png)

Once the image is deployed, you can go the bench list and you will find a new bench there. This was created using the `Deploy Candidate`.

## Deploying a New Tenant Site

It's time to create your first tenant site!

1. Open the dashboard by changing the browser address path to `/dashboard`.
2. From the sidebar, click on **Sites**, then select the **+ Add Site** button to start setup. Configure as shown below in the screenshot.

![New tenant site](/files/new-site.png)

Choose a subdomain: this will be the site's primary address. You can link a custom domain later if needed.

1. Click `Create site`. You'll be redirected to the **Insights** tab, where you can track the deployment progress in real time.

![Tenant site deployment in progress](/files/tenant-site-page.png)

Wait until the status updates from `Running` to `Success`.

1. Go back to the **Sites** page. Your new site will now appear in the list, as shown below.

![Tenant sites list with entries](/files/tenant-sites-list.png)

![Tenant site deployment completed](/files/tenant-site-deployment-done.png)

## Resolving issues

One of the issues that you may get into is not being able to obtain a TLS Certificate for the root domain. If that is the case, you have to manually call (via `console`) the `_obtain_certificate` method on the `TLS Certificate` document that was created for the `Root Domain` document that we created in the initial part of this guide.

Start the press site's IPython console:

```bash
bench --site frappe-cloud.local console
```

Call `_obtain_certificate` method on the TLS Certificate document:

```python
p = frappe.get_doc("TLS Certificate", "*.jay.fc.frappe.dev")
p._obtain_certificate()
```

## Testing

When you run `bench init` or `bench setup requirements`, Frappe installs only the runtime dependencies listed in `requirements.txt`. Development dependencies are not installed automatically, since production environments do not require them.

To set up a development or test environment, install the python dependencies using bench. This [internally calls pip](https://github.com/frappe/bench/blob/4fdaaf6a21b7245e039fd8c3d9509b0de1f44b2e/bench/utils/bench.py#L97) to install the dependencies from the dev-requirements file:

```bash
bench setup requirements --dev
```

This will install additional tools commonly needed in development:

- **moto** — emulates AWS services locally. Required for tests that depend on AWS APIs.
- **Faker** — generates fake data for test fixtures.
- **pre-commit** — provides linting and formatting hooks that run before each commit.

If you encounter test failures related to missing AWS services or other dev tools, ensure you have installed the development requirements.

Before running your tests, make sure to [set up pre-commit](https://github.com/frappe/press/blob/develop/setup-pre-commit.sh), follow the [testing guide](https://github.com/frappe/press/blob/develop/guide-to-testing.md), and refer to [the instructions for running tests](https://docs.frappe.io/framework/user/en/testing#running-tests) once all development dependencies are in place.

## Tips

- Set `scheduler_tick_interval` to a smaller value (like 5) for faster Agent Job updates, since most of them don't take much time.

## Conclusion

If you made it till here, well done and be proud of yourself. Now, it's time to build awesome things. Good luck with your journey on Frappe Cloud.

<!-- page: cloud/cloud__lock-wait-timeout-exceeded-error.md -->
---
title: "Lock wait timeout exceeded error"
space: "Cloud"
url: "https://docs.frappe.io/cloud/lock-wait-timeout-exceeded-error"
updated: "2026-06-10"
---

Sometimes you may run into this particular error 

`frappe.exceptions.QueryTimeoutError: (1205, 'Lock wait timeout exceeded; try restarting transaction')` 

This usually indicates a bug in your application. In such cases, you should review your application for locks it holds.  
To understand locks, you should also understand [Frappe's transaction model](https://docs.frappe.io/framework/user/en/api/database#database-transaction-model) first.  
Any writes or read with for_update performed locks the document. If job is running and other transaction (web or background job) tries to access the same doc, it will get a timeout unless the current job updating the rows commits or rolls back the transactions

You should review the process list while the error happens to see what the running queries are [https://docs.frappe.io/cloud/site-process-list](https://docs.frappe.io/cloud/site-process-list)

<!-- page: cloud/cloud__logs.md -->
---
title: "Logs"
space: "Cloud"
url: "https://docs.frappe.io/cloud/logs"
updated: "2026-04-29"
---

Frappe Cloud allows you to see the logs of your processes right from your dashboard.

From your bench group dashboard, you can view logs for a particular **bench**

![](/files/6AYIwgn.png)![](/files/MC50whq.png)  


Reading the logs
----------------

After ssh-ing into the bench, you will see certain files in the `logs` directory that are of interest

1. `web.log` and `web.err.log`. These correspond to the STDOUT and STDERR streams of the web process. These handle the individual web requests to your site.
2. `worker.log` and `worker.err.log`. These correspond to the STDOUT and STDERR streams of the background workers. These run the background jobs.

The above files are usually the areas of interest when you're debugging. But similarly, all the files in the `logs` directory correspond to the processes listed when you do `supervisorctl status` in your bench. Different issues will have you looking at different logs in your bench.

Site specific logs
------------------

For site specific logs check out: &lt;https://frappeframework.com/docs/user/en/logging&gt;

  

<!-- page: cloud/cloud__managing_team_members.md -->
---
title: "Managing Team Members"
space: "Cloud"
url: "https://docs.frappe.io/cloud/managing_team_members"
updated: "2026-02-16"
---

When you signup with Frappe Cloud we create a team for you by default. 
You can add or remove members from this team.

> Note: Team members can access your account on your behalf

To add members to your team go to Settings > Profile & Team. Then click on Manage Members under Team Members section. A dialog like below will open up. Now click on and Add Member button.  

Enter the email of the member you want to add and Send Invitation.  
  

An email will be sent with an invitation to join the team.

![](/files/manage_members.png)

Similarly removing members is very straight forward with just a click of a Remove button!

<!-- page: cloud/cloud__marketplace.md -->
---
title: "Frappe Cloud Marketplace Overview"
space: "Cloud"
url: "https://docs.frappe.io/cloud/marketplace"
updated: "2026-02-16"
---

> All apps on the Marketplace must be **Open Source**. They must be MIT or compatible with the GNU General Public License. For a specific list of compatible licenses, please read the [GPL-Compatible license list](https://www.gnu.org/philosophy/license-list.html#GPLCompatibleLicenses) on gnu.org. 
>
> We do not accept apps from publishers who do not meet this requirement.

## About

Frappe Cloud Marketplace is a platform to share your Frappe apps publicly with the community. It connects you to users using Frappe based sites. You can list free or paid apps for users to use it on their site.

## Apps

Apps on the Marketplace are built on the [Frappe Framework](https://frappeframework.com). These apps can be extensions to existing apps like [ERPNext](https://frappecloud.com/marketplace/apps/erpnext) or can have fully-featured functionality like [Wiki](https://frappecloud.com/marketplace/apps/wiki).

To publish an app on the marketplace, you must be the owner and the app should be hosted on GitHub. After you submit your app for listing, it will be reviewed and published after an approval process.

If you are new to Frappe Framework and app development, you can go through the [Tutorial](https://frappeframework.com/docs/user/en/tutorial).

## Links

- [Publishing an app to Marketplace](/cloud/marketplace/publishing-an-app-to-marketplace)
- [Guidelines for authoring an app](/cloud/marketplace/app-authoring-guidelines)
- [Guidelines for publishing an app](/cloud/marketplace/marketplace-guidelines)
- [Managing your Marketplace App](/cloud/marketplace/manage-marketplace-app)

<!-- page: cloud/cloud__marketplace__app-authoring-guidelines.md -->
---
title: "App authoring guidelines"
space: "Cloud"
url: "https://docs.frappe.io/cloud/marketplace/app-authoring-guidelines"
updated: "2026-02-16"
---

This page contains guidelines for publishers who are writing Frappe apps to publish on the Frappe Cloud Marketplace

If you are new to Frappe apps, learn more about it on [frappeframework.com](https://frappeframework.com). You can also get started by following the [Tutorial](https://frappeframework.com/docs/user/en/tutorial).

1. We recommend having a settings doctype in your app to configure global behaviour of your app's functionality.
2. Make sure your app supports the current stable version of Frappe and ERPNext (if applicable).
  You can also write version specific code by checking the version of these apps in your python code:

```
from frappe import __version__ as frappe_version
from semantic_version import Version

if Version(frappe_version).major >= 13:
    # version 13 or above
    pass
else:
    # version 12 or below
    pass
```

1. Don't override base functionalities provided by Frappe. For e.g., Frappe ships with authentication pages like /login for Login & Sign Up, /update for resetting passwords. If you override these, you will have to implement their functionality again.
2. Extend base functionalities by using [hooks](https://frappeframework.com/docs/v13/user/en/python-api/hooks) provided by the framework.

### Linters and Server Tests CI

For approval, it is mandatory to have a passing GitHub Actions (or similar) CI in your app's GitHub repository. Usually, new apps have the boilerplate, but you can use [this two workflows](https://github.com/Arus-Info/ERPNext-Australian-Localisation/tree/d178b87331381c8bb43322067e713deb04e8165e/.github/workflows) as reference (`ci.yml` and `linters.yml`) and make necessary changes based on your apps's requirements. 

## Run Semgrep Locally

We suggest you to run Semgrep locally in your app. To do that follow these steps:  

```
$ pip install semgrep
$ git clone --depth 1 https://github.com/frappe/semgrep-rules.git frappe-semgrep-rules
$ semgrep --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness .
```

<!-- page: cloud/cloud__marketplace__marketplace-guidelines.md -->
---
title: "Guidelines for publishing an app"
space: "Cloud"
url: "https://docs.frappe.io/cloud/marketplace/marketplace-guidelines"
updated: "2026-02-16"
---

Requirements for submitting an app
----------------------------------

Apps on Frappe Cloud Marketplace must meet the requirements listed on this page before they can be published.

* Apps should provide value to the users
* Apps should not persuade the user away from Frappe Cloud
* Publisher should provide valid contact information
* Apps should support the current stable version of Frappe/ERPNext
* Apps must have a logo, description and screenshots images that meet the recommendations provided in the following section

Submitting Marketplace apps
---------------------------

To publish your app in the Frappe Cloud Marketplace, you'll need to write descriptions of your app and provide images that follow our guidelines.

### App Name

The App Name must be unique across the Frappe Cloud Marketplace. For example, if an app exists with the name "todo", you cannot publish an app with same name even if it does not fork from the published app. Make sure you choose a name that is unique.

### App Title

The App Title will appear on the Marketplace homepage. The name is limited to 255 characters and can be different from your app's name.

### Short Description/Summary

* We recommend keeping the length of the description to 40-80 characters.
* Describe the app's functionality in a single sentence. Don't write multiple sentences.
* Don't repeat your app name or title in the description.
* Only capitalize proper nouns.

#### Long Description

* Describe the usage, features and more about your app here.
* Don't repeat the short description in the long description.
* Don't add installation instruction since Frappe Cloud automatically handles those.
* Move screenshots to the screenshot section.

### Logo

Frappe Cloud Marketplace displays all apps with a logo image inside a circular frame to visually distinguish them. You must upload a custom image for the logo.

* Upload a logo image that is at least 200 pixels x 200 pixels so your logo won't have to be upscaled when your listing is published.
* Logos will be cropped to a square. We recommend uploading a square image file with your logo in the center.
* Avoid using logo images with words or text in them. Logos with text do not scale well on small screens.

### Category

Apps in Frappe Cloud Marketplace can be displayed by category. Select the category that best describes the main functionality of your app.

### Required URLs

* Support URL: The URL of a web page that your customers will go to when they have technical support, product, or account inquiries.
* Privacy Policy URL: The web page that displays your app's privacy policy.


> Please prepare a short demo video of the app describing the usage of the app so we can review if the app would be a good addition to the FC Marketplace.
> 
> 

<!-- page: cloud/cloud__marketplace__payouts.md -->
---
title: "Payouts"
space: "Cloud"
url: "https://docs.frappe.io/cloud/marketplace/payouts"
updated: "2026-02-16"
---

For Marketplace apps that are non-free, we do a payout to the publisher at the **end of every month**. The payout contains all the payments we have collected from the customers over that month.

## Setup Payout Preferences

If you want to publish a paid app, please visit the **Publisher Profile** page and edit your payout preferences:

![Payout Preferences](/files/CleanShot 2022-11-02 at 12.56.57@2x.png)

You can select from one of the following payout methods:

![Payout Methods](/files/CleanShot 2022-11-02 at 12.58.32@2x.png)

> If you are based from outside India, the only option available as of now is Paypal. You need to raise an PayPal invoice at the end of the month.

## Payout Orders

You can visit the **Payouts** page from your Developer dashboard to see the history of payouts with an option to view more details. A payout is in draft mode until the payment is processed from our side:

![Developer Payouts Page](/files/CleanShot 2022-11-02 at 13.03.56@2x.png)

## Payout Terms

Frappe Cloud takes the first $500 of the revenue the app makes. After that the payment will be split 80-20, where 80% will go to you and 20% to Frappe Cloud.

> Payout Terms are effective from 1st April 2023.

<!-- page: cloud/cloud__marketplace__publishing-an-app-to-marketplace.md -->
---
title: "Publishing an App to Marketplace"
space: "Cloud"
url: "https://docs.frappe.io/cloud/marketplace/publishing-an-app-to-marketplace"
updated: "2026-02-16"
---

## Marketplace Developer Account

To be able to publish and manage apps on Frappe Cloud Marketplace, you will need to get a marketplace developer account. You can do this by going to the **settings page of your Frappe Cloud dashboard**. Open the `Profile` tab and click on the `Become a Publisher` button:

![Become Publisher Button location](/files/become-publisher.png)

Once the Developer account is enabled (not to be confused with Developer Mode on Frappe Sites), you will be able to see a new **Marketplace** 
tab on dashboard, as shown below:

![Marketplace Tab](/files/marketplace_tab_no_apps.png)

## Adding your Frappe App

Just click on the `+ Add App` button and you will see a dialog open with a list of apps that you 
own (you might have added it to your bench group before):

![Add App Dialog](/files/add_app_dialog.png)

Select the app you want to add to the marketplace or if you want to add an app from GitHub, click on the **Add from GitHub** link.

Clicking on the **Add from GitHub** link will open a new page, where you can authorize and add any of your Frappe Apps from your 
GitHub account. Once your app is validated, you can select the version of Frappe with which your app is compatible and click on 
the `Add to Marketplace` button:

![Add to Marketplace from GitHub](/files/add_from_github.png)

A marketplace app will be created with the selected app and a new page will open where you will be able to manage your 
marketplace app:

![Manage Marketplace App](/files/marketplace_app.png)

> Notice that your app is in `Draft` state. It will be published to marketplace once we approve it from our side.

You should also be able to see your app on the list of apps in **Marketplace** tab:

![List of Marketplace Apps](/files/marketplace_tab_with_app.png)

## Managing the profile of your App

The first tab on the Marketplace App page is the **Overview** tab. Here, you can edit all the details related to your app like App image, descriptions, links etc. which will
be displayed on the marketplace website:

![Edit Description](/files/darkify_md.gif)

### Details Required for Publishing

Before our team publishes your app on marketplace, the details mentioned on [this](/docs/marketplace/marketpace-guidelines) page must be filled via your app overview page.

## Next Steps

After you have added the marketplace app along with the required details, you need to publish a particular release of your app, which is discussed in detail [here](/docs/marketplace/manage-marketplace-app).

We will approve the release (and the app, if its the first release) and your marketplace app will be live!

> SLA: Apps will be reviewed or published in 10 days time. If your app is still in Draft state after 10 days of adding it to marketplace. Please raise a ticket on [Support Portal](https://support.frappe.io/)

<!-- page: cloud/cloud__notice.md -->
---
title: "Notices"
space: "Cloud"
url: "https://docs.frappe.io/cloud/notice"
updated: "2026-05-14"
---

## Site Suspension for Exceeding Plan Usage

Effective from **16th June, 2025**

If your site exceeds the limits of your plan (either disk space or database usage), you will receive a notification. We will continue to monitor your site's usage for the next **14 days**, sending you daily alerts.

- If your usage returns to within plan limits during this period, the alerts will stop.
- If the usage remains above the limit and no plan upgrade is made, the site will be **automatically suspended** after 14 days.

To avoid suspension, you can either:

- Reduce your site’s storage to fit within your current plan, or
- Upgrade to a higher plan.

In either case, your site will be reactivated once it complies with the plan limits.



## Site Suspension for Unpaid Invoice

Please ensure that all outstanding invoices are settled before the 15th of the month. Failing to do so may result in your sites being suspended on the 16th.

<!-- page: cloud/cloud__notification-configuration.md -->
---
title: "Notification Configuration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/notification-configuration"
updated: "2026-02-16"
---

You can configure multiple notifications at the Team level to ensure that alerts are delivered through the right channels.

### Accessing Notification Settings

- Go to Settings → Profile.
- Under Notification Settings, click `Manage` to open the configuration screen.

![](/files/Screenshot%202025-10-06%20at%2015-30-21%20Settings%20-%20Profile.png)

### Configuring Notifications

The Notification Configuration screen allows you to set up how and where notifications are sent.


![](/files/Screenshot%202025-10-06%20at%2015-32-03%20Settings%20-%20Profile.png)

### Notification Flow Logic

The notification delivery follows a top-down hierarchy:

- Check if a specific notification type (e.g., Billing, Incident) is configured.
- If not found, use the General notification configuration.
- If General is also not configured, fallback to the Team-level configuration.


![](/files/shapes%20at%2025-10-06%2015.57.22.png)

<!-- page: cloud/cloud__performance-tuning.md -->
---
title: "DB Performance Tuning"
space: "Cloud"
url: "https://docs.frappe.io/cloud/performance-tuning"
updated: "2026-04-29"
---

This page consists of all the performance tuning options available to your site.  
  
For more context refer:  
&lt;https://frappecloud.com/docs/faq/mariadb-slow-queries-in-your-site&gt;  
&lt;https://mariadb.com/kb/en/compound-composite-indexes/&gt;  
  


### Add Database Index

1. Click on the row containing the query you would like to analyze and the Normalized Slow Query dialog should open.![Screenshot 2024-07-31 at 2.27.35 PM](/files/Screenshot 2024-07-31 at 2.27.35 PM.png "Screenshot 2024-07-31 at 2.27.35 PM.png")
2. Click on the Analyze Query button and a toast should appear stating that the Analyze query has started in the background.![](/files/9NWWN9T.png)
3. The above process might take time, anywhere between (10s to 5m) depending on how big the query is and how big the actual tables in the database are.


&gt; You wont be able to analyze multiple queries at once, because this process is rather CPU intensive.  
&gt; If you do so, you will be presented with the below warning.
&gt; 
&gt; ![](/files/QoNsjSd.png)  
&gt; 
&gt; 
&gt;
4. Once the analyze query operation is completed, you will be able to see the suggested index.  
![](/files/jZ2WOcl.png)  



&gt; If there is no suggested index, you will be shown the below message. There is nothing much you can do at this point apart from adding database indexes manually.![](/files/GyVpG9L.png)  
&gt; 
&gt; 
&gt;
5. Click on Apply Suggestion to add the suggested index. This will create an "Add Database Index" job, whose status you can track from the jobs tab.  
![](/files/6QNYkJy.png)  



&gt; Note : You will be able to add only one index at a time for any given site.
&gt; 
&gt;

<!-- page: cloud/cloud__private-benches__common-issues__frappe-listed-as-a-python-dependency.md -->
---
title: "Frappe listed as a Python dependency"
space: "Cloud"
url: "https://docs.frappe.io/cloud/private-benches/common-issues/frappe-listed-as-a-python-dependency"
updated: "2026-08-03"
---

Your deploy was blocked with an error like this:

> ERPNext lists `frappe` under `[project]` `dependencies` in its pyproject.toml.  
> Remove `frappe` from `dependencies` and deploy again.

This means one of the apps in your bench group declares `frappe` as a Python package dependency in its `pyproject.toml`.

## Why this breaks the build

Bench installs Frappe and every Frappe app from their **git repositories**, not from PyPI. When an app lists `frappe` under `[project] dependencies`, pip goes looking for a package called `frappe` on PyPI instead. The only thing published there is an empty `0.0.1` placeholder, so the install either fails to resolve a version or replaces the real Frappe with a stub.

The same applies to any other Frappe app — `erpnext`, `hrms`, `payments` and so on. None of them are Python packages on PyPI.

## How to fix it

Remove `frappe` from the `dependencies` list in the app's `pyproject.toml`. Only third-party Python packages your app imports belong in that list.

```toml
[project]
name = "your_app"
dependencies = [
    "frappe>=15.0.0",   # remove this line
    "requests",
]
```

If you listed it to declare which Frappe versions your app supports, use the bench section instead — Frappe Cloud reads it when resolving app compatibility.

```toml
[tool.bench.frappe-dependencies]
frappe = ">=15.0.0,<17.0.0"
```

Commit the change, push it, then deploy again.

## If the app is not yours

Contact the app's developer and ask them to remove `frappe` from their `[project] dependencies`. Until they do, that app cannot be deployed.

<!-- page: cloud/cloud__private-benches__common-issues__pkg-resources-error-when-updating-site.md -->
---
title: "pkg_resources error when updating site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/private-benches/common-issues/pkg-resources-error-when-updating-site"
updated: "2026-08-04"
---

# Update fails with "No module named 'pkg\_resources'"

Your site update failed and the traceback ends with:

```
ModuleNotFoundError: No module named 'pkg_resources'
```

The update is rolled back, so your site is still running on the old bench. Nothing is lost — but the update will keep failing until you do one of the things below.

## Why it happens

`pkg_resources` used to ship with **setuptools**. setuptools removed it in version 82.

Every deploy builds a fresh bench with a fresh Python environment, and that environment now gets a setuptools that no longer has `pkg_resources`. Any app that still imports it — older **Frappe** versions, and **Payments** and **LMS** (both pull it in through `razorpay`) — breaks the moment the site is migrated.

## Fix: update the app

All three apps have newer releases that don't import `pkg_resources` any more. This is the fix — the rest of this page is for when you can't take it.

Open your bench group and go to the **Apps** tab. If an update is available you will see the **Update Available** button.

![](/files/image3b6df7.webp)

Click it, tick **Frappe Framework**, **Payments** and **LMS** — whichever are listed as having an update — and go through **Next** until you can deploy.

![](/files/imaged87cec.webp)

Once the deploy finishes, retry the site update.

## If you don't want to update those apps

Some teams pin app versions deliberately. In that case you have two options.

### Option 1: install the older setuptools yourself

The deploy creates a **new bench**. You can SSH into it and put the older setuptools back before the site is migrated.

1. Open the bench group, go to the **Sites** tab, click the `...` next to the new bench and choose **SSH Access**.  
![](/files/imaged7cf64.webp)
2. Run the two commands the dialog gives you — the first stores a certificate that is valid for 6 hours, the second opens the SSH session.  
![](/files/imagef339b1.webp)

  If the dialog says your SSH public key is missing, add it under **Settings → Developer** first.
3. Once you are in, run:
  ```bash
   cd /home/frappe/frappe-bench
   env/bin/pip install setuptools==80.9.0
  ```
4. Retry the site update from the dashboard.

> **This is not a one-time fix.** Every deploy creates a brand new bench with a brand new environment, so you have to do this again after *every* update. If that isn't practical, use Option 2.

### Option 2: change the Bench version

The bench CLI used to pull in the newest setuptools when it built the environment, without telling anyone. Newer bench releases pin it back below 82, but the versions in between will keep picking up the broken one.

You can move your bench group to a Bench version that isn't affected. Go to the **Dependencies** tab of your bench group.

![](/files/image5d5471.webp)

Click the `...` next to **Bench Version**, choose **Edit**, pick **5.26.0** from the list and click **Update**. Deploy afterwards for it to take effect.

![](/files/image467bde.webp)

If 5.26.0 is not in the list for your Frappe version, pick the highest version below it that is.

This survives future deploys, so you won't have to repeat Option 1 every time. Updating the app is still the better long-term answer.

<!-- page: cloud/cloud__private-benches__common-issues__request-timed-out.md -->
---
title: "Request Timed Out"
space: "Cloud"
url: "https://docs.frappe.io/cloud/private-benches/common-issues/request-timed-out"
updated: "2026-08-24"
---

# Request Timed Out

*(screenshot — not bundled; see the live page URL in this file's front matter)*

One action took longer than the HTTP timeout of the bench. The default timeout is 120 seconds. The proxy stopped the request and returned 504. The dialog has the title **Message** and the text **Request Timed Out**.

The server is not at fault. The code behind that one action is too slow.

If the site shows **Request Timeout: Server was too busy**, read [that page](https://docs.frappe.io/cloud/site/common-issues/request-timeout-server-was-too-busy-to-process-this-request) instead. That error is a database lock.

## Find the cause

1. Read the [slow queries](https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site) of your site. A slow query is the usual cause.
2. If the queries are fast, the Python code is slow. Do the same action from `bench console` after you [connect with SSH](https://docs.frappe.io/cloud/benches/ssh).
3. Time each step of the action there. The step that takes the most time is the one to correct.

## Correct it

- Make the slow code faster. Add an index, or remove work from the loop.
- Move work that is always slow to a [background job](https://docs.frappe.io/framework/user/en/api/background_jobs). The user then does not wait for it.
- If you cannot change the code now, increase `http_timeout` in the [bench config](https://docs.frappe.io/cloud/benches/bench-config). This hides the error. It does not correct it.

<!-- page: cloud/cloud__public-bench-update-schedule.md -->
---
title: "Public Bench Update Schedule"
space: "Cloud"
url: "https://docs.frappe.io/cloud/public-bench-update-schedule"
updated: "2026-02-16"
---

Public/Shared benches update every Wednesday. Sites get auto updated soon after. Your site on public bench should get auto updated by the end of thursday.

<!-- page: cloud/cloud__recent-issues.md -->
---
title: "Recent Issues"
space: "Cloud"
url: "https://docs.frappe.io/cloud/recent-issues"
updated: "2026-08-31"
---

## Intermittent downtime in KSA and Johannesburg regions (2026-08-29)

Due to an apparent network issue at DigitalOcean, sites started facing 504 and 502 errors in their sites intermittently. This started from 11 AM and went on till 5 PM. Upon investigation, we observed packet loss between the servers. We have applied a configuration change on all servers along with our NAT gateways to resolve the issue. Sites should be up now.



KSA region was proxying it's registry requests through another OCI instance in Johannesburg. This was added as a fix to an earlier incident. We removed the proxy and traffic is back to normal now.

## India Compliance API / E-invoicing failures (2026-07-26)

One 2026-07-26 we had updated our servers in Hetzner (Falkenstein and Nuremberg) as a part of scheduled maintenance. As a side effect of the same MTU on the network had reduced. This led to outbound requests from benches on the servers failing -- notably, requests to India Compliance API.  

Our engineers fixed investigated and identified the issue on **2026-07-27** and fixed the issue by **2:35 PM IST** on all affected servers. 

## Deploy failures across multiple regions (2026-07-20)

On 2026-07-20, 14:00 IST we noticed, docker pushes failing for our global docker registry which directly or indirectly caters to all our regions.

After investigation we noticed the issue was with DigitalOcean our upstream storage provider for our Docker registry.



DigitalOcean object storage enforces a silent cap on the allowed bucket size — which is not documented anywhere.



We performed the following actions for restoring normalcy

1. Immediately paused all deploys to ensure that no more failed deploys go through.
2. Raised a formal complaint with the upstream provider.
3. Started manual garbage collection to freaup space if possible

While the GC failed due to the volume of data and synchronous nature of docker registry's garbage collection, we managed to get the upstream providers to increase our storage quota.



Normalcy was restored on 2026-07-21 02:30 IST.



## TLS incident across multiple regions (2026-07-13)

There was a TLS issue affecting multiple proxies from **11:56 AM IST** to **1:43 PM IST**

The issue had transpired due to an update that went to our older proxies. These proxies were still in use for certain regions including Singapore, Frankfurt, Virginia, Jakarta, London and Johannesburg. Custom domains pointing to older proxies' IP were also affected.

Additionally, TLS certificates for some subdomains (l.frappe.cloud, z.frappe.cloud, v.frappe.cloud, s.frappe.cloud) were not renewed. This was happening due to another bug.

New TLS certificates were obtained for the affected domains and the faulty update was rolled back on all proxies to resolve the issue. All wildcard domains have also been pointed to the newer proxies so that such incident may not recur.  
We are taking measures to

- Prevent updates on older proxies
- Ensure TLS renewal success for all wildcard domains
- Ensure new proxy IP used everywhere

## Downtime in Nuremberg (2026-06-05)

Recently our proxy in the Nuremberg faced a networking drop, due to an upstream issue therefore, some sites might have been down intermittently

## Downtime in Virginia (2026-06-05)

Our proxy in Virginia lost communication with our central monitoring system, which might have caused intermittent false incidents on some of the Virginia servers however, systems are stable now.

## Downtime in Mumbai (2026-05-21)

One of our servers in the Mumbai region went down completely on 2025-05-21 from 01:02 PM IST to 02:58 PM IST . The issue was with respect to nginx unable to server any requests completely as all requests to the server would get stuck at nginx without any logging. After investigation from our engineers the culprit was observed to be an nginx plugin we use to tracking metrics of nginx. After disabling the same, we were able to restart the server and bring it back up.

## Downtime on f1-falkenstein2 (2026-05-15)

On 15 May 2026, services on `f1-falkenstein2` went down because the server disk became full. This caused Redis and Docker services to stop working properly. The main reason was unused Docker images taking up too much space over time.

To fix the issue, we attached extra storage and moved bench data to it. We also removed unused Docker images and restarted the services. Sites started coming back online gradually after recovery.

All the sites on the server has faced around \~2hr of downtime.

To avoid this in the future, we are improving [Docker image cleanup](https://github.com/frappe/agent/pull/508), and will move storage to Hetzner Volumes for easier maintenance

## Downtime in Nuremberg and Ashburn (2026-05-13)

The sites are back up and running.

RCA - Proxies going down  
(All timings are in IST)  



2:25am - A new root subdomain \*.nvi.frappe.cloud is created by an engineer.  
2:25am - A race condition sends empty TLS certificates to all proxies.  
6:00am - A Setup TLS certificate job triggers the restart of nginx `systemctl restart nginx` in a few proxy servers.  
6:00am - The regions of Ashburn, Nuremberg and Navi Mumbai start going down as Nginx fails to start due to missing certificates for the root subdomain.  
9:38am - The root cause is identified.  
11:41am - A [code fix](https://github.com/frappe/press/pull/6420) is merged which ensures the old configuration keeps running if the new Nginx configuration is invalid.  
11:43am - The TLS certificates are propagated to the servers.  
12:14pm - TLS setup is triggered on all proxy servers and they are operational.



## Deploys Affected in KSA and Europe (2026-05-12)

On May 12th, we experienced a network disruption affecting incoming international traffic from Europe and the KSA region to our Bangalore server, which **hosts** our central Docker registry. This issue was caused by upstream providers experiencing extreme packet loss at the international-to-domestic handoff.

Once detected, we raised support tickets with **our** upstream providers and **provisioned** HTTP proxies to relay the traffic. This proxy setup allowed us to resume deployments with minimal further disruption.

## Data Rollback Temporary Issue On m4-virginia (2026-04-21)

At 10:17 AM IST, the m4-virginia server experienced high resource usage, which triggered an automated recovery process and caused the server to reboot.

During the reboot, a leftover backup disk (intended for restoration purposes) was mistakenly mounted with higher priority than the live disk. As a result, the system temporarily started serving outdated data.

At 12:13 PM IST, our engineers identified and resolved the issue. Since then, the system has been serving the correct and up-to-date data.

If you are still experiencing any issues or have concerns, please reach out to support at support.frappe.io.

## Downtime in Frankfurt (2026-04-20)

###### One of our Frankfurt servers had unexpected downtime due to a network issue. We are investigating the same. We shall keep you posted once fixed.

**Edit**:- The issue has been fixed, will share the RCA soon, and we will continue to investigate the source of the issue.

## Outbound IP Change for AWS regions (2026-04-01)

We are in the process of updating the outbound IP addresses for most of our AWS-hosted servers.

**Regions affected:**

- Singapore
- Frankfurt
- Cape Town
- Virginia
- London
- Mumbai
- Sydney
- Zurich
- Jakarta

**Status &amp; Timeline:**

- Zurich, Jakarta, and Sydney: **Completed**
- All remaining regions (except Mumbai): ~~Scheduled for completion by 2026-04-01, 11:59 PM IST~~ **Completed**
- Mumbai: ~~**Will begin on 2026-04-02, 10:00 AM IST**  and may take **1–2 days** to fully complete~~ **Completed**

**Unaffected Servers:**

- Self-hosted servers
- Servers with static IP addresses

If you have any IP-based allowlists or firewall rules, please ensure they are updated accordingly.

Example: IF you have whitelisted your server's IP on a bank portal such as ICICI bank, you will have to reach out to the same to get this new IP added to the whitelist

The new outbound IP (post updation) can be checked in the Site Overview page. Please Refer: [https://docs.frappe.io/cloud/faq/site#inbound-and-outbound-ips](https://docs.frappe.io/cloud/faq/site#inbound-and-outbound-ips) 

## Disruptions in AWS Bahrain (2026-03-24)

Multiple servers in Bahrain region (me-south-1a) are down due to an issue in AWS datacenter.

You can track the health status here : [https://health.aws.amazon.com/health/status](https://health.aws.amazon.com/health/status)

For existing customers on Bahrain region, as per recent [advisory from AWS](https://health.aws.amazon.com/health/status) , if you have not already moved your site, we suggest you to move your sites to other regions on Frappe Cloud (Eg: **Mumbai, Frankfurt, Virginia**) to continue services without disruption. Since the servers are already down,  [direct site migration](https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-region) will not work. You will have to move using your **last backup available**. This implies some data loss.

### Steps to move

1. [Create a new site](https://docs.frappe.io/cloud/sites/creating-a-new-site) in one of the regions that are active
2. Go to backups dashboard of your existing site in Bahrain region and follow [these instructions](https://docs.frappe.io/cloud/sites/migrate-an-existing-site#restore-backup-on-another-site) to restore backup onto the newly created site.
3. Following these steps will create a copy of your site using your last backup.
4. If you have [custom domains](https://frappecloud.com/docs/sites/custom-domains), you can now point the same to the new site you created.

Please reach out to us at [support.frappe.io/helpdesk](https://cloud.frappe.io/support.frappe.io/helpdesk) if you have any questions or concerns regarding the same.

## Disruptions in AWS Middle East (2026-03-04)

Our UAE and Bahrain region is backed by AWS, and as per recent [advisory from AWS](https://health.aws.amazon.com/health/status) , we **strongly** suggest you to move your sites to other regions on Frappe Cloud (Eg: **Mumbai, Frankfurt, Virginia**) to continue services without disruption.

You can check [this doc](https://docs.frappe.io/cloud/sites/move-site-across-region) on how you can move your site to other regions at the click of a button.

NOTE: There will be DOWNTIME when moving your site across region, but a planned downtime is much better than unplanned downtime and data loss.

Please reach out to us at [support.frappe.io/helpdesk](https://cloud.frappe.io/support.frappe.io/helpdesk) if you have any questions or concerns regarding the same.

## Downtime in Mumbai region (2026-02-09)

There was a downtime from **12:14 PM IST** to **12:22 PM IST** in the Mumbai region. This had happened due to a DoS attack on the same. We have identified the source and blocked their IP.  



The attack vector was through one of our old used Github pages that we used for serving documentation. It seems an attacker abused a type of vulnerability here to DoS our proxy server. We have dropped these unused domains to prevent this from happening again.

## Downtime in Singapore region (2026-02-09)

We recently faced another downtime in Singapore region as nginx was consuming too much memory on the proxy server. We will be upgrading this server soon to prevent this from happening again. For the time being, we have applied some limits for the process so itself doesn't halt the server.

## Delay in agent jobs and site updates (2026-02-03 - 2026-02-04)

Users may have observed agent jobs remaining in pending state, or site update not happening after new bench is deployed (after bench update). We have found the source of the issue to be a memory contention on our app server. We have found one of the possible sources of the problem and disabled the same. We continue to investigate further sources and solutions of the issue. 

## MariaDB down on few database servers (2026-02-02)

There was a recent outage affecting multiple database servers. This happened due to a change meant for all database servers, but failed for some of them.  

The change was intended to use the data volume present in the servers for [tmpdir](https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#tmpdir) . This is required as some database servers don't have enough memory and need to use the disk for storing temporary tables during large query computations.

The failure happened as the [tmp](https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#tmpdir) directory itself for MariaDB was not present in some servers. This seems to have happened as a side effect of a previous change.

We have reverted the change on affected servers to resolve the issue. We will be rolling out a fix to make the change persist on the affected servers.

## Downtime in Singapore region (2026-02-02)

There was a 15-minute downtime affecting all sites in Singapore region. This had happened due to a memory outage in the reverse proxy server of the same region. We have narrowed the source of the issue down to an auxiliary service on the server. We've memory limited the same to resolve the issue for future. 

## India Compliance App `branch:version` Mismatch (2025-12-05)

We have had a recent issue on Frappe Cloud Marketplace with India Compliance Apps version and branch mismatch. If you triggered a Migrate / Site Update, your site must've been broken due to this issue.

Please fetch the latest branch of India Compliance (for version 15 of the app) on your bench and [update your site](https://docs.frappe.io/cloud/sites/how-to-update-an-app-site-on-a-private-bench). 

## Deploys slow/not happening due to Digital Ocean (2025-10-30)

There appears to be some packet loss between servers from other regions and DigitalOceans servers where our Docker Registry resides. Due to this, builds have started to fail at the last step. We are checking with the provider for an RCA and resolution

## KSA region inaccessible from other regions (2025-10-30)

It seems OCI has faced an incident around **1:02 PM IST** and as a result the servers in the region are inaccessible. For more information regarding the OCI incident you can refer [here](https://ocistatus.oraclecloud.com/#/incidents/ocid1.oraclecloudincident.oc1.phx.amaaaaaanfxwrmaa2pox7nkmzwxleeibdwzsw2u2cj33qajyiap44re4jf6q).

#### Update (October 30, 2025) - 1:55 PM IST

All the sites down on Frappe Cloud under KSA Regions are back up and functional. The down time happened due to Oracle Cloud Infrastructure's KSA Region being down for 35-40 Minutes.

[Incident acknowledgement report](https://ocistatus.oraclecloud.com/#/incidents/ocid1.oraclecloudincident.oc1.phx.amaaaaaanfxwrmaa2pox7nkmzwxleeibdwzsw2u2cj33qajyiap44re4jf6q) from OCI.

## Sites down with redis Auth error (2025-10-29)

Due to a recent change on Frappe Cloud, few benches (89) got affected with a faulty redis config. We have pushed a fix for the same and it should take effect in a few minutes.

Recurrence: The issue reoccured an hour later due to a worker which didn't receive the fix and affected approximately 30 more benches. We have retroactively fixed those as well. We are working on taking better measures for such deployments.

## Bench deploy failures on custom apps (2025-10-28)

If you have imported frappe or other apps within `__init__.py` , deploys will have started to fail with message 'No module named frappe' since 25th October due to recent [pip update](https://pip.pypa.io/en/stable/news/#deprecations-and-removals). Please update your bench to use older version of pip (25.2) to resolve the issue.

## New Bench Failures (2025-10-20)

There was an incident on Frappe Cloud due to which all New Bench jobs started to fail from **2:00 PM IST** to **3:00PM IST**. The incident seemingly resolved itself afterwards. We have taken some measures to prevent the possible cause of the same. We continue to monitor for further occurence.  
Affected users can redeploy the bench to resolve the issue.

> edit: This seems to have been a [side-effect](https://status.digitalocean.com/incidents/sxlrj088l11b) of aforementioned AWS incident also

## AWS N.Virginia Incident (2025-10-20)

There appears to be an [incident](https://health.aws.amazon.com/health/status) started **Oct 20 12:11 AM PDT** in the Virginia region. This will affect:

- Site updates that use physical backups, which are mostly large sites.
- Server actions such as Reboot, Creation of server, Drop server, Snapshots, etc.

> edit: Physical backups have been disabled everywhere on Frappe Cloud for the time being so updates for already deployed benches can proceed

Please refrain from performing these operations till the issue is resolved at AWS side.

## Frankfurt sites down issue (2025-07-22)

Sites were reported being down and agent jobs failing on the sites with a 404 error.  
The issue had happened due to an nginx config limit being reached. We've updated the same on all proxies to prevent same issues going forward.

## .frappe.cloud redirect issue (2025-07-15)

Around midnight 2025-07-15 IST time, frappe.cloud sites started to not resolve correctly and redirect to the Frappe Cloud dashboard instead. We identified the source as a bug in a DNS cleanup job.

Only **x.frappe.cloud** sites that are not in Mumbai region were affected. **erpnext.com** and **frappe.cloud** subdomain sites (**abc.m.frappe.cloud**, **abc.k.frappe.cloud**,etc.) were unaffected. Sites with custom domains that had A records were also unaffected.

The same has been resolved as of 1:34 am IST time. Missing DNS records were re-added for the sites affected to resolve the issue.

---

# New deployment issue in KSA region (2025-04-30)

KSA region has some issues with the networking in orcale cloud and impacting new deployments. [Refernece](https://ocistatus.oraclecloud.com/#/incidents/ocid1.oraclecloudincident.oc1.phx.amaaaaaavwew44aag4f4xhfscggbw74x3sff6jadk73e2rwjbpwykpyipa) 

Our technical team is actively investigating the same and will keep you posted once fixed.

---

# Frappe Cloud dashboard slow (2025-03-12)

We have noticed Frappe Cloud dashboard being slow due to some resource constraints from our end. We're performing an upgrade of the same. The analytics page may not load for some time

## Slow deploys (2025-03-10)

There is an i/o block on our build server causing the deploys slow/stuck, our technical team is investigating this further, The ongoing deploys will take some time to complete. Once the load get reduced on the build server, it will be completed automatically.

## Builds with Marley (healthcare) app broken (2025-02-19)

Due to new release of [flit](https://flit.pypa.io/en/stable/history.html#version-3-11), deploys of benches with Marley app is now broken. Please wait until Marley team fixes the issue.  
Edit:- The issue has been [resolved](https://github.com/earthians/marley/commit/924d48185a216ba559b96d10e199c1bb0621414c) by the Marley team, redeploying the update on your bench group should work.

## Issue with pending jobs on 1 server in Mumbai region (2025-10-02)

A server had an incident where all jobs were stuck. This had gone on for 4 days until it came to our attention on 2025-10-02. We're unsure of the cause of this. We have fixed it and jobs have continued for time being. Further investigation is pending.

## Issue with pending jobs on some servers (2024-12-15)

A few of our shared servers are having issues processing Jobs. If you're affected, you'll see the jobs going to **Pending**.

This is because of some traffic restrictions imposed by our cloud provider due to an abuse report. We're working with them to resolve this as soon as possible.  

Edit: Due to the lack of response from the provider. We fixed the issue ourselves by performing an emergency replacement of the virtual machines. This caused **downtime** between 10:00 AM GMT to 10:41 AM GMT across the 5 servers that were affected.

## Downtime in Frankfurt region (2024-12-09)

There was an issue affecting one of our proxy servers, in the Frankfurt region due to which sites in the region were affected from 16:20 GMT to 16:44 GMT during which we resolved the same. We are taking preventive measures.

## Sites unreachable in KSA region (2024-11-24)

Between 10:48 GMT and 11:08 GMT. One of our proxy servers in the KSA region was down which resulted in downtime for all the sites in the region. We suspect the cause to be a memory spike of an internal service and applied controls to mitigate the same. We continue to monitor the server

## Sites down with internal server error (2024-10-29)

Between Tue, 29 Oct 2024 10:29:06 GMT and Tue, 29 Oct 2024 10:58:00 GMT, a subset of EC2 instances were unavailable in the **Mumbai** Region. The issue has been resolved by AWS and the service is operating normally.  

## Reduced uptime for sites hosted in Virginia Region (2024-10-18)

We've observed a network connectivity issue due to which uptime monitoring of sites in the Virginia region is affected and may show as **red** in the dashboard even when the site is still up. We expect the network providers to fix this soon.  
edit: The issue has been resolved

<!-- page: cloud/cloud__reliability.md -->
---
title: "Reliability"
space: "Cloud"
url: "https://docs.frappe.io/cloud/reliability"
updated: "2026-05-30"
---

Frappe Cloud undertakes multiple measures to ensure reliability: 

## Infrastructure & Operations

- Runs on established cloud providers such as AWS and OCI. Uptime commitments for all providers on Frappe Cloud can be seen [here](https://docs.frappe.io/cloud/getting-started/uptime). 
- Continuous monitoring of infrastructure and platform services by Frappe engineers. 
- Incident tracking, root-cause analysis, and preventive fixes to reduce repeat failures. 
- 24×7 incident response support for critical infrastructure issues.

## High Availability

- Proactive detection and resolution of infrastructure issues before they impact users. 
- Resource monitoring and operational alerts help identify issues early.

Overall, Frappe Cloud maintains a **best-effort uptime of 99.9%**. 

## Reliable Deployments & Upgrades

- Automated and repeatable deployment workflows reduce human error. 
- Most deployments are designed for zero or near-zero downtime. 
- Large upgrades can be scheduled during non-working hours. 
- Automated backups are created before upgrades and migrations. 
- Rollback mechanisms allow recovery to a known working state if a deployment fails.

## Backup & Disaster Recovery

- Automatic daily site backups. 
- Automatic server snapshots. 
- Configurable backup schedules and retention policies. 
- Off-site backup support on eligible plans. 
- Backup files can be downloaded for additional protection. 
- Server snapshots stored separately help support disaster recovery scenarios.

## Recovery & Failover

- Automated recovery workflows help restore services quickly after failures. 
- Systems can be restored from recent backups when required. 
- Automated fallback mechanisms reduce recovery effort and downtime. 
- Disaster recovery procedures are designed to minimise both recovery time and data loss.

## Observability & Monitoring

- Real-time visibility into resource utilisation and infrastructure health. 
- Monitoring of storage consumption trends and performance metrics. 
- Built-in alerts notify users when resource thresholds are approaching limits. 
- Developer tools provide deeper diagnostics when troubleshooting is required.

## Capacity Planning

- Resource utilisation analytics help identify growth trends before they become bottlenecks. 
- Threshold-based alerts allow teams to scale infrastructure proactively. 
- Visibility into usage patterns helps prevent outages caused by resource exhaustion.

---

Watch this video to know more: 

<iframe src="https://www.youtube.com/embed/rxsdcRYS0T0?si=CE07A92eA5L0lMfN" width="800" height="450" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>

<!-- page: cloud/cloud__role-permissions.md -->
---
title: "Role and Permissions"
space: "Cloud"
url: "https://docs.frappe.io/cloud/role-permissions"
updated: "2026-08-10"
---

### Introduction

Why? Because there might be too many people in your organisation that it becomes hard to manage. The team owner must be a person with utmost authority. This person (or organisation) must be the sole authority to do anything on team level. That includes actions like deleting, renaming or transferring a team. But there will be others who want to work on other areas of activities. This may be actions like updating a site, a bench or a server. This person must not be able to do team level actions but they still should be able to what they are supposed to do. There will be also times when a person should see only one resource (a site, for example) and nothing else.



All this means roles and permissions are a way to restrict people, not a way to make it convenient for them. Your authority as the owner gives you the power to set rules that will act as barriers. These barriers are our promise of safety and security.

### Understanding Roles

Two questions arise when talking about roles.



- What if I don’t want to use roles at all?
- What happens when I create a role and add nothing in it.



The first question is relatively simple and that is what we mostly face. Let’s say your team has ten members. You trust all of them and you believe none of them could do anything wrong. You are okay with all ten members having unrestricted access to everything under the team. Good for you, because you don’t have to do anything. Because of absence of any role results in deactivation of the barrier. This is a basic scenario where people don’t care about roles at all, mostly in small teams.



The second question is tricky. Because the moment you create a role, you are opting in to use them. That means from that moment on, the barrier will be active and it will prevent team members from accessing resources they were not cleared for. There is one thing to keep in mind though. All permissions has to be explicit. That means if a member want to access a resource (for example, `foobar.frappe.cloud`), they must be a member of a role that includes said resource (`foobar.frappe.cloud`). That means the barrier denies access by default and permits a member only if there is explicit rules.

### Listing and creating roles

You can access roles from the team settings page.

![image92687f](/files/image92687f.png)

You can also create a new role with users and resources.

![image8a260f](/files/image8a260f.png)

### Gettting members and resources

Click on individual roles to get a detailed view of members and resources.

![imagee94032](/files/imagee94032.png)

![imagef5473f](/files/imagef5473f.png)

### Permissions

Each role can be tweaked to allow or deny certain permissions. These can be seen along with members and resources.

![imageb6db2e](/files/imageb6db2e.png)

### Notes

Roles and permissions are currently in beta. Please expect some rough edges. If you find any issues, please report them. We will fix them as soon as possible.

<!-- page: cloud/cloud__server-notification-configuration.md -->
---
title: "Notification Configuration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/server-notification-configuration"
updated: "2026-02-16"
---

You can configure multiple notifications at the server level to ensure that alerts are delivered through the right channels.

### Accessing Notification Settings

- Go to Server Overview → Application Server Actions.
- Under Notification Settings, click `Manage` to open the configuration screen.


![](/files/Screenshot%202025-10-06%20at%2015-51-41%20Settings%20-%20Profile.png)

### Configuring Notifications

The Notification Configuration screen allows you to set up how and where notifications are sent.


![](/files/Screenshot%202025-10-06%20at%2015-52-53%20Settings%20-%20Profile.png)

### Notification Flow Logic

The notification delivery follows a top-down hierarchy:

- Check if a specific notification type (e.g., Billing, Incident) is configured.
- If not found, use the General notification configuration.
- If General is also not configured, fallback to the Team-level configuration.


![](/files/shapes%20at%2025-10-06%2015.57.22.png)

<!-- page: cloud/cloud__server-snapshot.md -->
---
title: "Server Snapshot"
space: "Cloud"
url: "https://docs.frappe.io/cloud/server-snapshot"
updated: "2026-02-25"
---

A **Server Snapshot** is a time-based copy of server's disks. It can be used to create a new server or recover your data in the future. 

Snapshots are useful for **disaster recovery** and can be kept for as long as you want, even after the server is archived.

### Charges

Snapshots are charged at **6.5 INR / GB / Month** or **0.08 USD / GB / Month**.

### FC Server Snapshot Policy

Frappe Cloud automatically takes snapshots of all servers every **24 hours** and **48 hours**. These automated snapshots are free of cost and are automatically deleted after **48 hours**.

### View Snapshots

You can go to the **Server Overview** page and open the **Snapshots** tab.  
Here you can view all your snapshots along with their details (for AWS servers).

![](/files/view-snapshots.png)

### Create Snapshot

You can create a snapshot with just one click. There are two types of snapshots

- **Consistent Snapshot**: In this mode, Docker and MariaDB on the server are stopped, and the disk is flushed before taking the snapshot. This ensures reliable data recovery but causes **2–5 minutes of downtime** for your deployed sites.  
- **Inconsistent Snapshot**: In this mode, the snapshot is taken without stopping services. This avoids downtime, but in rare cases, recovery may be more complex and require manual help.



To create a snapshot, click on the **New Snapshot** icon, choose the snapshot type, and submit.

![](/files/create-snapshot.png)

### View Snapshot Details

Each snapshot shows important information such as the size, exact timestamp, status, and the list of sites that can be recovered from it.

![](/files/view-snapshot-details-in-list.png)

![](/files/view-snapshot-details.png)

### Recover Sites

You can recover sites by clicking on the **Recover Sites** button and selecting the sites you want. This process does not directly restore data to your deployed site. Instead, you will receive database and file backups.

![](/files/recover-site-0.png)

![](/files/recover-site-1.png)

![](/files/recover-site-2.png)

![](/files/recover-site-3.png)

Once the recovery is completed, you will get an email notification, and the backups will be available to download for **24 hours**.

![](/files/recover-site-4.png)

You can visit the snapshot list and open the `Recover Sites` tab. You will be able to view the status and options to download the backups and view the encryption keys (in case that's available). 

![](/files/recover-site-5.png)

![](/files/recover-site-6.png)

### Lock / Unlock Snapshot

To avoid accidental deletion, you can lock snapshots. Once locked, they cannot be deleted unless unlocked first. 

However, only snapshots created manually by you can be locked. Automated 24h/48h snapshots from Frappe Cloud cannot be locked.

##### Steps For Locking Snapshot

![](/files/lock-snapshot-0.png)

![](/files/lock-snapshot-1.png)

##### Steps For Unlocking Snapshot

![](/files/unlock-snapshot-0.png)

![](/files/unlock-snapshot-1.png)

### Delete Snapshot

If you no longer need a snapshot, you can delete it. Any charges linked to the snapshot will stop once it is deleted.

![](/files/delete-snapshot-0.png)

![](/files/delete-snapshot-1.png)

### Accessing Snapshots of Archived Servers

Even if a server is archived, you can still access its snapshots from the **sidebar**, where all server snapshots are listed, including those from archived servers.

![](/private/files/snapshot-list.png)

### Supported Cloud Providers

Currently, Frappe Cloud supports snapshots on **AWS**, **OCI** and **Hetzner**, but this feature is available only for **AWS-hosted servers**.

 For **OCI-hosted servers**, disk snapshots are also created every **24/48 hours**, but they are **not visible in the dashboard** at the moment.

<!-- page: cloud/cloud__server-storage-breakdown.md -->
---
title: "Server Storage Breakdown"
space: "Cloud"
url: "https://docs.frappe.io/cloud/server-storage-breakdown"
updated: "2026-03-02"
---

# Database Server

If you want to know, what is consuming storage on your dedicated database server, you can use this option.

1. Click on the `pie` icon in your server overview page.

![](/files/Screenshot 2026-03-02 at 14.30.58.png)

2. You will get storage breakdown in this way.

![](/files/Screenshot%20from%202025-05-28%2018-56-28.png)

3. You can click on the `Site Name` to view tablewise usage in the database.



#### Some Terminology -

- **Operating System :** On each dedicated database server, we have Ubuntu operating system installed. The operating system, it's generated logs and installed software take some amount of storage.
- **Binary Log :** Binlogs are important part of database. It helps in database replication. But if you are not using binary log, this can help in point in time recovery and disaster recovery.
- **MariaDB Core :** It includes various kind of files that database required for it's internal operation like ibdata1, ibtmp1, aria_log etc.
- **MariaDB Slow Log :** This log holds slow query of your servers. Frappe Cloud periodically send slow logs to centralized elasticsearch server and purge the file.
- **MariaDB Slow Log :** Holds errors and deadlock of database. Like as slow log, this is also synced to elasticsearch and purged from server daily.
- **MariaDB Owned System Files :** Except this, MariaDB generate some other files as per requirement of operation (like ddl_recover_log, coredump etc.)

# Application Server

Similar to the database server, if you want to know, what is consuming storage on your dedicated application server, you can use this option.

The way to display the storage breakdown is same as for the database server

1. Click on the `pie` icon on your application server's storage section
2. You will get the storage breakdown as such
  ![](/files/Screenshot%202025-08-01%20at%2012.08.10%E2%80%AFPM.png)
3. This can be further expanded to represent the storage of each bench in a hierarchical tree structure.
  ![](/files/Screenshot%202025-08-01%20at%2012.10.14%E2%80%AFPM.png)

#### Additional Usage disclaimer -

As detailed in the Storage Breakdown dialog, the storage calculation is split into two parts:

**Bench Size :** This includes core files and folders necessary for your application including logs, private and public files etc.

**Additional Disk Usage :** This includes disk space consumed by directories that are excluded from the main bench size calculation, such as:

- env – Python virtual environment files
- node_modules – Node.js dependencies
- assets – Static files such as images, stylesheets, or compiled assets

These directories are excluded from the main calculation primarily for performance reasons. Folders like `node_modules` and `assets` can contain tens of thousands of files, and scanning them in real-time significantly slows down storage analysis.

Additionally, for Docker, only active containers and images are considered in the storage breakdown. Docker metadata and unused layers are ignored to focus on what's actively used.

<!-- page: cloud/cloud__servers__create-a-new-site-on-a-dedicated-server.md -->
---
title: "Creating a new site on a dedicated server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/create-a-new-site-on-a-dedicated-server"
updated: "2026-02-16"
---

If you want to create a new site under your dedicated server, you need to follow the steps given below.

1. Click on the server dashboard and select the server under which you want your site to be.
  ![](/files/imageb4e79d.png)
2. Click on the bench group on the selected server under which you want your site.
  ![](/files/imagef9bcca.png)
3. Click on create a new site under the selected bench group.
  ![](/files/image911390.png)
4. Select the apps you want and the region, and then select the plan.
  ![](/files/image8d59c9.png)

> Note:- Only 5 sites can be **Unlimited - Supported**, those site will be supported by the apps team for app related support.

<!-- page: cloud/cloud__servers__delete.md -->
---
title: "Delete Servers"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/delete"
updated: "2026-02-16"
---

Deleting a server will delete both the application and the database server immediately. Be careful when deleting servers since you can **NOT** recover a server after deleting it.

> Note: You must delete all sites and bench groups before deleting the server.

Go to the Server Dashboard>**Actions**>Dangerous Actions>Drop Server

![](/files/image709561.png)

![](/private/files/Screenshot%202025-06-18%20at%201.40.00%E2%80%AFPMf5f2e6.png)

Type in the entire server's name or title to confirm, and click on **Drop Server**

![](/files/image0225e7.png)

<!-- page: cloud/cloud__servers__guidelines-for-choosing-a-server-plan.md -->
---
title: "Guidelines for choosing a server plan"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/guidelines-for-choosing-a-server-plan"
updated: "2026-03-10"
---

We offer a number of plans for both your application and your database server, and you may be confused as to which plan to choose for both. This document will help you rectify that confusion.

90% of the time, you won't be picking the correct plan for your server from the get go, which is why we have the provision to change plan whenever you desire. This is because you can only see the workload on the servers once you start using your sites.

The best tool to help you analyse the workload on the server is the **Analytics** tab on your Frappe Cloud Servers dashboard. You'll see many charts. I'll try to go over some of the important ones that you have quick control over with plans.

## Server Analytics

## **CPU**

This is a graph of the CPU Time consumed by the processes on your server.

**Idle** means there are no processes consuming CPU on the machine. This will go down as CPU is being used i.e there are requests hitting your sites or when background jobs run in your site.

![](https://frappecloud.com/files/9jQqyMm.png)

**iowait** means there are processes waiting for disk operations to finish on your server. This may be reading/writing a big file or loading a table from the database into memory.

**nice** means there are processes which don't take priority but will run when there aren't other processes that are to run. This usually attributes to background jobs as background jobs in Frappe are [niced](https://en.wikipedia.org/wiki/Nice_(Unix)).

> **For database server, servers spike in iowait is generally a sign to upgrade for more memory . This is because it's best practice to give Mariadb as much memory as possible so the database can mostly reside in RAM. This'll make all the database operations fast as memory is faster than disk.**

## **Load Average**

If you're not familiar with load average concept in Linux, refer [https://www.digitalocean.com/community/tutorials/load-average-in-linux](https://www.digitalocean.com/community/tutorials/load-average-in-linux) to learn a bit about it.  

![](https://frappecloud.com/files/IpCh0a4.png)

In the above chart `Load Average 1` is the load average in a time frame of 1 minute, `Load Average 5` is the load average in a time frame of 5 minutes and so on.

> Spike in `Load Average 1` may be harmless and normal but a spike in `Load Average 15` might be an issue  
>  
> 

If load average comes to more than no. of cpu cores, it may be an indication to optimise your code or upgrade server for more cpu.

### Bench Memory Usage

Benches you create on the server will use around **400 MB** (appx.) of memory at minimum number of sites (2 [gunicorn workers](#gunicorn-workers) and 1 set of [background workers](https://frappecloud.com/docs/servers/guidelines-for-choosing-a-server-plan#background-workers)). The system will try to allocate as much free memory that is available to existing bench on the basis of sites on the bench. This means that you should be careful adding too many bench to a server that has only 4 GB total RAM available. You can watch free memory available on the server from the **Analytics** tab on the server dashboard.

#### Gunicorn workers (or web workers)

These are [processes](https://en.wikipedia.org/wiki/Process_(computing)) that serve the web requests to your site. Only 2 workers is enough for a bench with small sites who don't get a lot of concurrent requests. This is because most web requests happen within a span of milliseconds. If you run into a [gateway timeout](https://frappecloud.com/docs/faq/site#site-slow-gateway-timeout) , it is because the web workers are busy executing some long request.

The number within a bench is decided by the system. There is no provision for users to decide this as of now. The system allocates workers based on the plan of site and number of sites in the bench.

#### Background workers

These are [processes](https://en.wikipedia.org/wiki/Process_(computing)) that execute the background jobs in your site. These can be scheduled jobs or jobs created with `frappe.enqueue`. Long-running jobs/queries/reports should be run here so that you can use your site freely. Even 1 of this worker is enough, as these jobs aren't expected to run instantaneously and go in a queue if the worker is busy.

## FAQ

### Very High Database Server Memory Usage

MariaDB on all servers is configured to use as much memory as possible. This ensures that almost all db operations are done in memory and hence fast. So it's normal to see 90% or higher memory usage on your database server. [read more](https://mariadb.com/kb/en/innodb-buffer-pool/)

We also try to limit the maximum memory mariadb uses in order to avoid a [OOM](https://en.wikipedia.org/wiki/Out_of_memory) situation and hence downtime.

One rule of thumb is to have as much RAM on the database server as the total database size. Eg: Here: 16 GB would be good as total database size is 17GB

![imagee20b17](/files/imagee20b17.png)

If all the data within the server is accessed all the time, it can cause memory contention.

Backups could also contribute to high memory consumption and there, you can schedule backups sporadically across the sites on your site. Please raise a ticket on support.frappe.io if you'd like for us to do that

### Work-horse terminated unexpectedly

If your background jobs fail with this particular error, it indicates not enough memory on your application server. You should upgrade the same in such cases.

### Why separate Database and Application servers

This is because both database and application servers run different kind of software. And as they do, it is better to keep them on separate VMs as we can configure the VM to be better suited for running the software. For example, database servers tend to be machines with more memory and less cpu as keeping data in memory makes the site run faster. And we can scale the same as the database size increases.

### How do I decide on a dedicated server plan for a year

You may find [this spreadsheet](https://docs.google.com/spreadsheets/d/1_RW1sMqAUSkoTV7vSlqiUn5O3oq1WPE9yW3sKcWq2zQ/edit#gid=1671562397) useful. Note that this is a guess and not a guarantee. You may well need to upgrade/downgrade your plan depending on your usage.

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

![](/files/image0d442a.png)
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

![](/files/Screenshot 2026-02-24 at 18.03.40.png)





Enter the **Server Name.** 

![](/files/Screenshot 2026-02-24 at 18.06.16.png)





Select the **Cloud Provider**. (Note - [Click here](https://docs.frappe.io/cloud/servers/provider-comparision) to know how providers differ from each other)

![](/files/Screenshot 2026-02-24 at 18.08.31.png)



Select the **Region**. 

![](/files/image74ae1d.png)



Select the **Deployment Mode**. 

- Unified Server - Appropriate for most small and medium business workloads. 
- Separate Server - Recommended for enterprise workloads that may need separate scaling for Application and Database in future.

![](/files/imagea0326d.png)



Select the **Service Type**. 

- Standard - Regular SLA
- Premium - Priority SLA and Performance Consulting (Recommended for Large Enterprises)

![](/files/Screenshot 2026-02-24 at 18.16.10.png)



Select the desired **Application Server configuration**. 

![](/files/Screenshot 2026-02-24 at 18.19.17.png)



Select the desired **Database Server configuration**. (Note - This step is applicable only if you have chosen "Separate Server" as the Deployment Mode).

![](/files/image4ddab5.png)



Click the checkbox to **Enable Auto Add-on Storage** if you wish to allow automatic scaling of Application and Database Servers based on usage. (Note - This option is available only on select cloud providers.)

![](/files/Screenshot 2026-02-24 at 18.22.38.png)

Review the Server Configuration and click the checkbox to provide **Consent for Local Compliances** and click on **Create Server**.

![](/files/Screenshot 2026-02-24 at 18.26.58.png)



A new server will be created based on the selected configuration. It takes 5-10 mins to complete the creation. 



You can check the **Plays** tab to track the progress. (Note - Notice the "Installing" status on the top bar.)

![](/files/Screenshot 2026-02-24 at 18.29.27.png)



Once the server is created, the status will turn to "Active". You can start working with the server now. 

![](/files/image4ea013.png)

<!-- page: cloud/cloud__servers__new_bench.md -->
---
title: "Creating new Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/servers/new_bench"
updated: "2026-02-16"
---

From the server dashboard go to Bench Groups and click on New Bench Group ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdzAhq0dHMhG40H2jh4gj0r7R9Avq7QX7EQadMCIXkHDdqOrfS6R8oOeitF_p5pBUoMmWQ0XUPcb7a8lugmgw6yK7TNnGZiVcMLeSF39NMhpIWeew-MH0tKYWZStk4BzP13PAPPiQ?key=B8rSwy69a11PMxQbCQftVilN)  
Choose the version for which you want to create a new bench group, enter the title for the new bench group, check the "I agree" box, and then click on "Create Bench Group."  
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfb9RcgjZOkU0245q47VsyfbiVGRIzPUbVw07Bg_62MVX1tpooNbhomVD0FzIxNtO9xuasb7kG4EugTdcbEsOboH5RGyuAngBg_b4Y5UNo3wplK8PhzHucD0v4Soy0_CRRnJfLwkA?key=B8rSwy69a11PMxQbCQftVilN)  
  
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

![](/files/imagecfc51a.png)

Frappe Cloud sets up a dedicated WireGuard P2P mesh between:

- Frappe Cloud app server
- Database server
- Your on-premise server

Afterwards, Frappe Cloud will setup a database replica to your on-prem server and sync all docker images and bench data to your on-premise server. 

### Setup Guide

Once support enables the feature, you will see **“Manage On-Prem Replication”** under server actions.

![](/files/image0a7d33.png)

Click **Manage** to view the setup guide for connecting your on-prem server to Frappe Cloud.

![](/files/image6864ea.png)

Complete the on-prem setup and initiate the replication setup from the UI.

![](/files/image1022e2.png)

You can track progress on the same page.

![](/files/image5a1f62.png)

Once successful :

- All existing data will be synced to your on-prem server
- New data will continue to sync automatically

If the setup fails, reach out to **support.frappe.io**.

### Performing Failover

After setup, a small daemon runs on your on-prem server to assist with failover.

**Access the dashboard at :**  `http://<your_on_prem_server_ip_address>:5000`

![](/files/image63629e.png)

From the dashboard, you can :

- Monitor benches and sites
- Click **Configure Sites And Start Benches**  to
  - Stop replication
  - Start serving sites from the on-prem server

Once completed, each site will be accessible on a specific port.

![](/files/image9a3479.png)

**Example:** To access `test-failover-1.nbg.frappe.cloud`, you have to visit `http://<your_on_prem_server_ip>:8394`

### Stop Replication

If you want to stop syncing changes from Frappe Cloud to your on-prem server, use the **Stop Replication** option.

![](/files/image0373c9.png)

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

![](/files/oo6tvfK.png)  


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

1. Go to the Server Overview and click on the + button beside storage![](/files/WNI1Uun.png)
2. Select the amount of storage you want to buy and click on confirm

![](/files/flJZVgK.png)


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



![](/files/Screenshot%20from%202025-04-09%2013-51-37.png)

4. Next, click on the `Activate` button of webhook record.

![Screenshot 2024-09-25 at 4.29.43 PM](/files/Screenshot 2024-09-25 at 4.29.43 PM.png "Screenshot 2024-09-25 at 4.29.43 PM.png")
5. Click on `Validate Webhook`
6. If everything looks good, you can activate the webhook from there

  


![Screenshot 2024-09-25 at 4.32.06 PM](/files/Screenshot 2024-09-25 at 4.32.06 PM.png "Screenshot 2024-09-25 at 4.32.06 PM.png")  


  


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

![Screenshot 2024-10-28 at 5.50.14 PM](/files/Screenshot 2024-10-28 at 5.50.14 PM.png "Screenshot 2024-10-28 at 5.50.14 PM.png")
3. It will take few seconds to initiate the login request, after that you will be presented a modal like this

![Screenshot 2024-10-28 at 5.51.08 PM](/files/Screenshot 2024-10-28 at 5.51.08 PM.png "Screenshot 2024-10-28 at 5.51.08 PM.png")
4. Check your mailbox. You will recieve an e-mail with a verification code.

![Screenshot 2024-10-28 at 5.51.51 PMb](/files/Screenshot 2024-10-28 at 5.51.51 PMdb8d68.png "Screenshot 2024-10-28 at 5.51.51 PMb.png")
5. Put the verification code in input box and click on `Verify`  
![Screenshot 2024-10-28 at 5.52.15 PM](/files/Screenshot 2024-10-28 at 5.52.15 PM.png "Screenshot 2024-10-28 at 5.52.15 PM.png")
6. You should be now logged-in and redirected to Frappe Cloud dashboard

![Screenshot 2024-10-28 at 5.52.58 PM](/files/Screenshot 2024-10-28 at 5.52.58 PM.png "Screenshot 2024-10-28 at 5.52.58 PM.png")
7. You will also get a `Login Successful` banner

![Screenshot 2024-10-28 at 5.52.51 PM](/files/Screenshot 2024-10-28 at 5.52.51 PM.png "Screenshot 2024-10-28 at 5.52.51 PM.png")  


  



> Sometimes many browser block url redirection. In that case, there are two solutions -
> 
> 
> 	1. Tap on `Click Here to login` link inside the modal.
> 	
> 	![Screenshot 2024-10-28 at 5.52.51 PM](/files/Screenshot 2024-10-28 at 5.52.51 PM77e6e1.png "Screenshot 2024-10-28 at 5.52.51 PM.png")
> 	2. Your browser will show a message that popup has been blocked. This message can be vary based on the browser.
> 	
> 	![Screenshot 2024-10-28 at 5.52.36 PM](/files/Screenshot 2024-10-28 at 5.52.36 PM.png "Screenshot 2024-10-28 at 5.52.36 PM.png")  
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


![](/files/Screenshot%202025-10-06%20at%2015-56-26%20Settings%20-%20Profile.png)

### Configuring Notifications

The Notification Configuration screen allows you to set up how and where notifications are sent.

![](/files/Screenshot%202025-10-06%20at%2015-55-33%20Settings%20-%20Profile.png)


### Notification Flow Logic

The notification delivery follows a top-down hierarchy:

- Check if a specific notification type (e.g., Billing, Incident) is configured.
- If not found, use the General notification configuration.
- If General is also not configured, fallback to the Team-level configuration.



![](/files/shapes%20at%2025-10-06%2015.58.51.png)

<!-- page: cloud/cloud__site-process-list.md -->
---
title: "Site Process List"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site-process-list"
updated: "2026-02-16"
---

You can view running mariadb queries in your site by opening **Insights** tab, and then **Reports ->**  **Process List Report**

![](/files/XnwpZ4e.png)  


![](/files/jsXP8Fw.png)  


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

![](/files/image84f365.png)

1. Click on **View Logs**

![](/files/image471f35.png)

1. Open **web.error.log** and scroll to bottom. You should be able to see the traceback:

![](/files/image89f8fe.png)
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

![](/files/prepared-report.jpg)

## What does "Other" mean in chart

The **Other** bucket holds all requests that are not in the top slowest paths.

When **Other** is the largest bar, one pattern of endpoint is usually slow. In this example, the `/custom_app/view/` endpoint is slow, and the developer of that app must examine it.

![](/files/slow-other-bucket.png)

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

![](/files/image525c9e.png)

<!-- page: cloud/cloud__site__site-migrations__introduction-to-site-migration.md -->
---
title: "Introduction to Site Migration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/introduction-to-site-migration"
updated: "2026-03-06"
---

The **Site Migration** feature allows you to seamlessly move your site across benches and servers with minimal effort.

![](/files/image2a0150.png)

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

<!-- page: cloud/cloud__sites__move-site-across-server.md -->
---
title: "Move site across server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/move-site-across-server"
updated: "2026-03-09"
---

> **Note:** This option is now part of the **Site Migration** feature.
>
> For instructions on moving a site to a different server / bench, see the documentation : [https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench](https://docs.frappe.io/cloud/site/site-migrations/move-site-to-different-server-or-bench)

---

You can directly schedule Site Migration across server from a site's dashboard.

> For moving your site to a dedicated server from a public bench group
>
> 1. Use [Change Bench Group](https://frappecloud.com/docs/sites/move-site-to-private-bench) option to move the site to a private bench group
> 2. Follow the below steps to move the site to your dedicated server

1. To change the server for the site go to your site Dashboard>Actions>Change Server.

![](/files/2ZNP8AO.png)

2. Select the server you want to move to (Your team should own the server).

![image](https://user-images.githubusercontent.com/63963181/285370002-4558082a-6271-4271-a6a7-c0bd10dcea7e.png)

3. If the selected server isn't added to the bench group add it by clicking on Add Server to Bench Group.

![image](https://user-images.githubusercontent.com/63963181/285370190-e81da89e-a8dd-4226-9d1d-e0eb0188f87d.png)

4. Click Migrate Site to Server if the target server is added to the bench group and the Site Migration will be done in the scheduled time (or leave it untouched if you want it to start immediately).

![image](https://user-images.githubusercontent.com/63963181/285369952-7d262852-3340-41e4-95fc-b7a3a695aced.png)





### Why is so much additional storage required when moving site to dedicated server?

The reason for storage that is much larger than backup size is because during site/backup restore, the backup files are uncompressed, due to which the disk storage spikes much higher than your database size. To avoid any failure during the restore, it is recommended you have enough storage on the server.   



In such cases, you can [add the required add-on storage](https://docs.frappe.io/cloud/storage-addons) on the server to continue with restoration.
