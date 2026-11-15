<!-- Frappe documentation: cloud, part 5 of 9. Index: docs/INDEX.md -->

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

![](/files/sUR2zsI.png)

2. Click on Install App
3. Select the app you need to install
  ![](/files/image2769a6.png)

## Sites on Private bench groups

You can add custom apps or any app from the [marketplace](https://frappecloud.com/marketplace) to your bench group and then install to your site. To install an app on a site on private bench group you have to add app in 2 places.

### Bench Group

1. Click on Apps tab of your Bench Group's dashboard

![](/files/Jl7MSK0.png)

2. Click on Add App

![](/files/xeR5clV.png)

3. Select any marketplace app or follow [this guide](https://frappecloud.com/docs/benches/custom-app) to install a custom app.

![](/files/HzkmdMl.png)

4. Click on the Update Available button to create a new deploy so that your site can install the app

![](/files/svW5FMt.png)

5. Select your site while doing the update and click on deploy and update

![](/files/ARYkCG7.png)

### Site

1. Once the update is done click on Apps tab of your Site's dashboard

![](/files/sUR2zsI.png)

2. Click on Install App

![](/files/z2nse6u.png)

3. Select the app added earlier to install

![](/files/Behu0t3.png)

<!-- page: cloud/cloud__instructions-to-upgrade-the-email-delivery-service-plan.md -->
---
title: "Upgrade the Email Delivery Service plan for more emails"
space: "Cloud"
url: "https://docs.frappe.io/cloud/instructions-to-upgrade-the-email-delivery-service-plan"
updated: "2026-02-18"
---

From your Frappe Cloud site dashboard navigate to the Apps tab and click on three dots from the Email Delivery Service app.

![](/files/V1lcDrp.png)

Choose the plan you would like as per your requirements and click on select plan to confirm the change.

![](/files/9h10e34.png)





> Once logged into your site, you can monitor the emails sent by searching for "**Email Delivery Analytics**" in the Awesome Bar.

![](/files/BpKfYU8.png)

## FAQ

### How to use my own smtp server/service for sending emails?

Simply uninstall the email delivery service app from your site and you should be able to resume sending emails from your own configured email account.

<!-- page: cloud/cloud__introduction.md -->
---
title: "Introduction"
space: "Cloud"
url: "https://docs.frappe.io/cloud/introduction"
updated: "2026-05-07"
---

## What is Frappe Cloud?

Frappe Cloud is a 100% open-source cloud hosting for the Frappe stack. Watch the following video to learn more. 

<iframe src="https://www.youtube.com/embed/jvzTPIycW7o?si=OhsJ0LbrpTAWktGz" width="800" height="473.33333333" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



---

<!-- page: cloud/cloud__is-it-scalable.md -->
---
title: "Scalability"
space: "Cloud"
url: "https://docs.frappe.io/cloud/is-it-scalable"
updated: "2026-05-30"
---

Frappe Cloud supports both vertical and horizontal scaling. 

- **Vertical Scaling**: Frappe Cloud has a diverse set of plans to choose from across cloud providers. They provide a range of specifications be it for sites or servers. (Find more information on plans [here](https://frappe.io/cloud/pricing).) 
- **Horizontal Scaling**: Frappe Cloud is equipped with autoscaling. This feature allows you to set up a parallel application server (in addition to your primary server) on demand. You can do it manually, or schedule it based on your load spike expectations. You can also set thresholds on compute to scale automatically.

Additionally, for enterprises with extremely variable and/or growing workloads, Frappe also provides consulting for architecture and performance. 



Watch this video to know more:   

<iframe src="https://www.youtube.com/embed/fc8xZNeq8DA?si=qyJvyGX0RF7nB3Jh" width="800" height="450" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>

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
