<!-- Frappe documentation: cloud, part 1 of 3. Index: docs/INDEX.md -->

<!-- page: cloud/cloud__app-plan.md -->
---
title: "App Pricing Plans"
space: "Cloud"
url: "https://docs.frappe.io/cloud/app-plan"
updated: "2026-02-16"
---

You can create different pricing plans for your marketplace apps, offering different services according to your needs.  

e.g. Customization, Priority Support, etc:
 
![](/files/CleanShot%202025-08-27%20at%2014.58.07@2x.png)

### How do customers subscribe to your app plan?

During app installation on a Frappe Cloud site, the user gets an option to select a plan. They can also change the plan from their site dashboard.

### Where can I see my paid plan subscribers / customers?

In your marketplace app dashboard, under the subscriptions tab.

### How are customers charged?

Currently only **monthly recurring plans** are available. These are charged on pro-rata basis, i.e. if the customer uses your app's $30/mo plan for 10 days and let's say uninstalls the app, they will be charged $10 for that app at the end of the month.

  
> Note: We don't link specific branches with the app plan. i.e. 
> It is not possible to do feature isolation based on paid or free App Plans.

  


  


  

<!-- page: cloud/cloud__bench-analytics.md -->
---
title: "Bench Analytics"
space: "Cloud"
url: "https://docs.frappe.io/cloud/bench-analytics"
updated: "2026-02-16"
---

We have now added a feature to expose bench level metrics.

Available under the `Bench Analytics` tab on the server page
![](/files/Screenshot%202025-09-04%20at%205.42.51%E2%80%AFPM.png)

Smiliar to how users are exposed to site level analytics, it is now possible to see how benches in a selected release group are performing and early detect problems
using this as well.

We currently expose the following metrics

1. **Memory** - Shows how much RAM is a bench in a release group eating up over a period of time ![](/files/Screenshot%202025-09-04%20at%205.45.32%E2%80%AFPM.png)
2. **CPU Time** - Shows the amount of time your CPU is working on a process. ![](/files/Screenshot%202025-09-04%20at%205.46.37%E2%80%AFPM.png)
3. **Network I/O** - Inbound and outbound network traffic from your bench. ![](/files/Screenshot%202025-09-04%20at%205.48.30%E2%80%AFPM.png)
4. **Disk I/O** - Disk level read and write operations performed by your bench. ![](/files/Screenshot%202025-09-04%20at%205.50.06%E2%80%AFPM.png)

These metrics above should ideally help in early identifying problems and also providing deeper analysis of problems

<!-- page: cloud/cloud__benches.md -->
---
title: "Private Benches"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches"
updated: "2026-02-27"
---

With private benches you can unlock the pull power of Frappe Cloud. To understand what a private bench is, first you have to understand what [Benches](https://docs.frappe.io/cloud/what-are-benches-and-bench-groups) are.

## Public Benches

Any site you create using the `+ New` button from Frappe Cloud dashboard home page, is created under a bench that is maintained by us.

![](/files/m2B2oK6.png)



We call these benches public because any user can create site on them. Users have no control over the bench environment, i.e., you cannot add custom apps, update the existing apps, etc. You can see your sites which are on a public bench group under the **Sites** menu inside the dashboard.

The bench environment is fully managed and maintained by the **Frappe Cloud team**, including all updates, security patches, and infrastructure management.

## Private Benches

In contrast to public / managed benches, private benches **are under your control**. You get to choose what apps to add (you can add your own custom apps too!), what apps to update, what region to deploy onto, SSH Access, Server scripts (v15+) etc.



![](/files/CRyWZQp.png)

  


Only the sites that you create can live on your private benches.

To learn how to create a new private bench visit [this link.](https://frappecloud.com/docs/benches/create-new)

### Pricing

You can only create sites on USD 25 and above plans. This is because private benches consume more resources than a simple shared site.

> Note: You are not billed for the bench groups you create, you are billed only when you create a site inside the bench group.

## How to unlock Private Benches

This feature is not available for trial and is only available after adding a payment method to your Frappe Cloud account.

Step 1: Update payment method.

Step 2: Create Private Bench > Add Apps > Deploy.

Step 3: Create a new Site under the Private Bench.

<!-- page: cloud/cloud__benches__app-patches.md -->
---
title: "App Patches"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/app-patches"
updated: "2026-02-16"
---


> **Note**: This is an experimental feature, please view the Limitations section before using it.
> 
> 

The App Patch feature allows you to apply a change to an app on your Bench. It's meant to be used for quick but tentative and small fixes. You can choose to apply the patch across all the deploys on the Bench or to just a single Deploy.

Limitations
-----------

App patches are meant to be quick but very tentative fix, do not use to push changes that are meant to persist.

Changes applied to your app using **App Patch** will not persist. If your server or container is restarted the app patch will be removed, and the **Status** displayed will not be in sync.

If you want the change to persist, you should commit the patch code to your repository and create a new deploy.

If your server or container has restarted, you might have to apply the patch again. You can do so by clicking **Apply Patch** from the **Patch** context menu, under the **Patches** tab, under you **Bench Group**.

> **Note**:
> The patches will be removed upon the next deploy at which point you will have to re-apply the patch.

Patching Frappe or 3rd Party Apps
--------------------

As patches are temporary fixes, if you want them to be a permanent fix you can choose to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the app (for example: ERPNext) and commit the patch as code.


Applying a patch
----------------

There are two ways to apply a patch:

1. Clicking **Apply Patch** from an **App**'s context menu in the **Apps** tab under your **Bench Group**.![](/files/DGCXgBk.png)
2. Clicking **Apply Patch** from the **Patches** tab under your **Bench Group**.![](/files/Nu4MZq3.png)

On clicking on **Apply Patch**, the following Dialog will be displayed:

![](/files/E6Q0Xq8.png)  
  


* **Select app:** Select the app the you would like to patch. This is not visible if opened from an **App**'s context menu.
* **Patch URL:** Enter the URL of the patch. Here is an [example patch](https://github.com/frappe/press/pull/1302.patch).
* `File button`: Select a patch file instead of selecting a **Patch URL.**
* **Select deploy:** Select a bench under the current **Bench Group** to patch.
* **Apply patch to all active deploys**: Ignores **Select Deploy** and applies the patch to all active benches under the current **Bench Group**.
* **Build assets after applying patch:** Rebuild assets (calls `bench build`) after applying the patch. To be used if for instance the patch alters a JavaScript file.

Once the values have been set, click on Apply Patch to create a **Job** to apply a patch. You can open the App Patch job to view the status:

![](/files/BHnPAWe.png)  


Reverting a patch
-----------------

To revert a patch, you can click on the **Revert Patch** button under **Patches** tab, under your **Bench**. This will create a new **Job** to revert the patch.

![](/files/OnClrxS.png)  


Deleting a patch
----------------

A patch can be deleted only if its status is **Not Applied.**

**On Failure**
--------------

To avoid a **Failure**, ensure that the patch can be applied to the **Deployed** commit of the **App**.

If you do see a failure such as this:

![](/files/Lks2AIs.png)  
  
  


Fret not! It either means that:

1. The **App Patch** has already been applied or reverted and the **Job** tried to re-apply or re-revert it.
2. The **App Patch** cannot be applied.

In case of point 1, you can try running the opposite action, i.e. if an **Apply Patch** failed then try **Revert Patch** first before re-applying it; and vice-versa:

![](/files/QYYUb73.png)  

<!-- page: cloud/cloud__benches__bench-config.md -->
---
title: "Bench Config"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/bench-config"
updated: "2026-02-27"
---

You may set site config variables on a bench so that it [applies for all the sites](https://frappeframework.com/docs/user/en/basics/sites#common-site-config-json) deployed under it.

![](/files/DGXrOWZ.png)



### Special case: http timeout

You may also set **httptimeout** in seconds (default: 120) as a special case to specify time gunicorn workers wait for request to process before throwing 504 request error. This will affect the custom api endpoints you define.

![](/files/nAlWmZH.png)

<!-- page: cloud/cloud__benches__create-new.md -->
---
title: "Creating a new bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/create-new"
updated: "2026-05-22"
---

Click on the `+ New` button from your Frappe Cloud dashboard under **Benches**:

![](/files/edTLUpG.png)



Select the Version of the Frappe Framework you want (also represents the "bench version"), select the Region for the bench and name the bench as per your requirement.

![](/files/amtAijP.png)



![](/files/MdqtqqK.png)



Then click on the `Create Bench` button. Once the bench group is created, you will be navigated to the bench group dashboard page. A bench is not automatically deployed, you have to click on the `Updates Avaliable` button.

![](/files/uqiLtTf.png)



and click on `Next`: and then deploy

![](/files/sAjufuZ.png)



You can check the deployment status in the **Deploys** tab. Once deployed, you have your own shiny new private bench ready for some magic!

<!-- page: cloud/cloud__benches__custom-app.md -->
---
title: "How to install a custom app"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/custom-app"
updated: "2026-07-24"
---

You can use your custom version/fork of the vanilla Frappe Framework.

:::caution
We do not provide support for modified versions of the framework.
:::



You can do so by simply following the add app flow inside your Bench.

![Screenshot 2024-11-20 112324](/files/Screenshot 2024-11-20 112324.png "Screenshot 2024-11-20 112324.png")

This will replace the Vanilla Frappe Framework with your custom fork / version.

## Note

Please ensure, that the app being added, has a valid `pyproject.toml` file along with a key advertising the frappe version, like such:



`[tool.bench.frappe-dependencies]`  
`frappe = ">=16.0.0-dev,<17.0.0"`

<!-- page: cloud/cloud__benches__debugging.md -->
---
title: "Debugging"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/debugging"
updated: "2026-02-16"
---

Getting access to custom apps means you get the power to deploy whatever you want. This also means you can easily break your bench if things go wrong. But with [ssh access](https://frappecloud.com/docs/benches/ssh) you will also be able to perform some level of debugging to figure out the cause of issues.


> **Note**: Please **ONLY** use SSH for debugging purposes. The bench setup on Frappe Cloud is different from the usual production setup you'll find in self hosted instances. Therefore, you can essentially **break** your bench by running arbitrary bench commands that change configuration. Eg: `bench setup supervisor`
> 
> 

Things NOT to do after SSH
--------------------------

The following is a list of things that can break your smooth flow of operations on Frappe Cloud unless you know what you're doing.

1. Install apps in bench. If you do


```
bench new-app my_awesome_app
```
OR


```
bench get-app my_awesome_app
```
it may seem like it works without issue but the app will only be available for this particular bench version and will not persist across bench updates

2. If you did the above anyway *and* install the app onto a site, this will prevent you from updating your site. If you do reach this case, simply uninstall the app from your site.

3. Edit frontend (css,js) files. For the time being `bench build` seems to break all js/css for the bench. This should be fixed soon, but if do you run into such a case, you can recover by updating your bench from dashboard and updating your site.

Reading the logs
----------------

After ssh-ing into the bench, you will see certain files in the `logs` directory that are of interest

1. `web.log` and `web.err.log`. These correspond to the STDOUT and STDERR streams of the web process. These handle the individual web requests to your site.
2. `worker.log` and `worker.err.log`. These correspond to the STDOUT and STDERR streams of the background workers. These run the background jobs.

The above files are usually the areas of interest when you're debugging. But similarly, all the files in the `logs` directory correspond to the processes listed when you do `supervisorctl status` in your bench. Different issues will have you looking at different logs in your bench.

Read logs with the `less` command. To start reading from the bottom, use `less +G`. Vim keybindings work in `less`. Press `q` to quit.

`tail` is also a similarly useful command. `tail -f` allows you to read output as it is being written to the file.

Bench
-----

You can use bench commands for debugging. `bench doctor` is a command that shows you the status of background jobs on the machine. When you make code changes to files after ssh, you need to run `bench restart` for the changes to take effect.

Database Queries
----------------

You can access the SQL console with `bench mariadb` command. This console is useful to see current status of the database. Eg: You can see running queries with `SHOW PROCESSLIST` command.

Supervisor
----------

Supervisor is the process manager within your bench. In a correctly functioning bench, all the processes should be in `RUNNING` state when you run `supervisorctl status`. You can also use `supervisorctl` commands to start and stop the processes listed. `bench restart` uses the same.


> This means there is no `bench start` command that is running your bench. It is similar (not same) to how `bench setup production` works
> 
> 

Connecting to Redis CLI
-----------------------

Once you've ssh'd into the bench, you have access to the `redis-cli` command. Which will allow you to inspect the redis instances in your bench. You can connect to the same with the following commands


```
redis-cli -p 13000 # cache server
redis-cli -p 12000 # socket_io
redis-cli -p 11000 # queue
```

<!-- page: cloud/cloud__benches__editing-bench-dependency-version.md -->
---
title: "Editing Bench Dependency Version"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/editing-bench-dependency-version"
updated: "2026-02-27"
---

Your Frappe Cloud bench has a few dependencies such as Python, Node, etc. The versions of these can be viewed and edited by navigating to the **Dependencies** tab under that bench:

![](/files/4EbJP2R.png)





> **ℹ️ Info**
>
> The "!" mark in the circle shows that the version is custom.

## Changing the version

To change the version of the dependency, click on the `...` menu button on a dependency row and click on **Edit**. This will show a version edit dialog:

![](/files/XDz2VK0.png)



Select a version from the drop-down menu and click on Update.

## Setting a custom version

To set a custom version, check the **Use Custom Version** checkbox:

![](/files/ySt40BM.png)



Enter your custom version and then click on Update.

> ⚠️ **Warning**
>
> Ensure that the version you update to actually exists and is supported. If it does not exist, future deploys might fail.
>
> Check the following links for dependency versions:
>
> - [Node Versions](https://nodejs.org/en/about/previous-releases#looking-for-latest-release-of-a-version-branch)
> - [Python Versions](https://devguide.python.org/versions/#supported-versions)
> - [Bench Versions](https://github.com/frappe/bench/releases)
> - [Wkhtmltopdf Versions](https://github.com/wkhtmltopdf/wkhtmltopdf/releases)
>
> A **custom dependency version** might not work as expected. Please test it locally before you update it on Frappe Cloud.

## When is my dependency version changed?

For your dependency version change to reflect, you have to [Update your Bench Group](https://frappecloud.com/docs/benches/updating_a_bench). After the update is complete, the new bench will be using the updated version.

> **ℹ️ Info**
>
> Once you click on **Update** in the **Edit Dependency** dialog. The dependency version is updated in our system and is applied on subsequent deploys.
>
> The current deploy remains unchanged.

<!-- page: cloud/cloud__benches__process-status.md -->
---
title: "Process Status"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/process-status"
updated: "2026-02-16"
---

To view the status of managed processes on your deployed bench, navigate to the Sites tab on your Bench and select the View Processes option from the `...` menu:

![](/files/VyuxkZm.png)  


On doing that, you should see a dialog that lists all the managed processes on your bench, their current status and uptime:

![](/files/8x4ZzyH.png)  

<!-- page: cloud/cloud__benches__ssh.md -->
---
title: "SSH Access"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/ssh"
updated: "2026-05-11"
---

With **private bench** groups, comes a whole new power to SSH into your bench group and run arbitrary commands. You can SSH into a particular version of your Bench Group using this feature. Here are the steps required to SSH into a particular bench group:

## What is SSH?

If you're unfamiliar with SSH, we highly recommend watching this [video](https://www.youtube.com/watch?v=v45p_kJV9i4) to get started.

## Add SSH key to your Frappe Cloud account

Visit the **Settings** page in your FC dashboard and scroll to the "SSH Key" section:

![SSH Key Addition Section](/files/ssh-key-list.png)

Clicking on "Add SSH Key" button should open up a dialog with an input box. Enter your **SSH public key** in this input box

![](/files/NfD2mqs.png)



### About copy/pasting keys

It's in your best interest to use one of the following commands to reliably copy your ssh key into your clipboard. Afterward, you can simply paste into the above input box.

#### Mac OS

```
pbcopy < <your SSH folder>/id_rsa.pub
```

#### Linux

Pre-requisite: [wl-clipboard](https://github.com/bugaevc/wl-clipboard)

```
wl-copy < <your SSH folder>/id_rsa.pub # Wayland
```

If the above command fails, try below. Needs: [xsel](https://launchpad.net/ubuntu/+source/xsel)

```
cat <your SSH folder>/id_rsa.pub | xsel -ib
```

#### Windows (Git Bash)

```
clip < <your SSH folder>/id_rsa.pub
```

> Manually selecting from text editor and copying can lead to invalid keys. If you *have* to select the key, please **cat** the file and copy the output.
>
> ```
> cat <your SSH folder>/id_rsa.pub
> ```

## Generate SSH certificate &amp; SSH

Navigate to your bench group dashboard and click on the three dots beside your bench group as shown in the below screenshot. You will see a drop-down with multiple options you can click on the SSH Access. If you have correctly [added your SSH key](https://frappecloud.com/docs/benches/ssh#add-ssh-key-to-your-frappe-cloud-account), the SSH Access option should be visible.

![](/files/NfpXryi.png)



Clicking on the button will open up a dialog:

![SSH Access Cert Generation Dialog](/files/ssh_access_dialog_cert.png)



Now, click the **Generate SSH Certificate** button. This will generate an SSH certificate for you, valid for 6 hours, which you can then use to SSH into your bench group:

> Note: These commands only work on Linux and macOS machines.

![SSH Access Certificate](/files/ssh_access_dialog.png)





> Note: Everytime you need SSH access to a particular version of a bench group, you will need to generate a new SSH certificate. This certificate is valid for 6 hours. After that, you will have to regenerate the certificate from the bench group dashboard.

Follow the instructions shown in the dialog (copy-paste the commands into your terminal). After you have successfully added the certificate locally, you should be able to run the given `ssh` command to gain access to your bench group:

![SSH Terminal](/files/ssh_terminal.png)



That's it! You can now run commands you like `bench restart`, `bench build` and more. Have a look at the [debugging](https://frappecloud.com/docs/benches/debugging) guide for things you can and shouldn't do.

### How it works?

The ssh works by generating a certificate using the public key you provide. The certificate can **only** be used on a system containing the private key corresponding to the public key given and hence secure.

## FAQ

### Access denied on SSH: Private key contents do not match public

If you see the following error on your local machine.

```
identity_sign: private key <your SSH folder>/id_rsa contents do not match public
  

```

This is probably because the key you've added on Frappe Cloud does not match the one you're using for ssh on your local.

The fingerprint you see in your dashboard

![fingerprint dashboard](/files/fingerprint-dashboard.png)



should match the output of `ssh-add -l` (as ran on a linux environment)

If they don't match, please review your local setup. [Github's ssh docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) are pretty good.

### Received disconnect from host: Too many authentication failures

If you receive this error even after adding the correct keys, and it is likely that you have 3 or more keys in your system, it's possible that the ssh certificate doesn't get the chance to be tried out before all the other keys and thus end with auth failure.  



To circumvent this, you can add the following options to pick your key corresponding to the certificate only

```
ssh -o "IdentitiesOnly=yes" -i <path_to_key> 
```

where **path_to_key** is path to the private key of the key you added on Frappe Cloud. Should be something like **<your SSH folder>/id_rsa**

> Please **DON'T** rename the files. Both your private key, and the certificate should have matching names. i.e if private key is **id_rsa**, certificate filename should be **id_rsa-cert.pub**. If either filename is changed, the ssh will fail with Permission denied (publickey) error

### SSH from powershell on windows does not work

Windows users using Powershell (or Windows Terminal) need to execute the following command ***before*** pasting the certificate:

```
$PSDefaultParameterValues['*: Encoding'] = 'utf8'
```

If you're using command prompt, the above command is not required. Please checkout this [issue](https://github.com/frappe/press/issues/798) for details

The certificate should be pasted in the `.ssh` directory under your user folder like so:

![](/files/LVRChP9.png)



where `id_rsa.pub` is the certificate generated and copied from Frappe Cloud for the public key `id_rsa.pub` with private key `id_rsa`

Here, the username is `balam`. Your user directory will be based on your username.

### Cannot copy files over SSH (SCP)

Our ssh sessions are provided over a proxy connection and thus scp and other tools that depend on it will not work.

Alternatively, you can upload the files to an external service such as Google Drive (as a zip) and download the same using [wget](https://github.com/tldr-pages/tldr/blob/main/pages/common/wget.md) after ssh-ing into your bench group.

For downloading files (eg: logs), you may zip the required files and put them under the **/public/files** directory of any of your sites and download the same from **/files/filename** route of your site.

> NOTE: Above action should be done with care so as to not replace any existing files in the directory.

### VS Code over ssh does not work

Same reason as above. VS Code uses scp to make this happen.

The recommended method is to push updates to your custom app on GitHub and then [update your benches](https://docs.frappe.io/cloud/benches/updating_a_bench) and sites.

### You must supply a key in OpenSSH public key format

Your ssh key should look something like:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC05RWHZSNEMPyzzY5MVZ/KBt5UCh6eUIRL0yp3oSFpsFECt4tGCdwQxJ9tggflh/JZ2rFZ8K4oznvp54qDAIjxNdOMLsiloMUqTh3CXWkApD7TRot9nHOuKISw8L/tguINkJ3xxaHIZidyZFabQeC5zlkLBRupPo/smN0WTkdGa1qcgSODnv3ZUKAWV+RXLEfdHjkBllNNYXWsBO43YdPj3wEUWpVR060c9gXxcXJVLWizXP4M5O/N6zN038FK7USWh3She3yFYE1gsUx2mFpPwjUtsehtrlMHs9Fx+RmMnnmoZLdlaWodudn0ePqo5K+MVenhmMu5GcoiPOKrEC4XhQPuTagnfBsSh05XshZ8eYRwJBDLZ7RpiKdQD92Uz36JO/LtItVJmqyxPa8UNoGr5ty3CdRDggilUXCUx9yvPlW0N2GxTDQprFXTeqc0WD5f5SXpbJ6GPHHjPatnJev7neFH+Rua4pmx5JJanM7B7zSCueKyMqsHgIAhOTjrj1s= your-name@your-os
```

The **your-name@your-os** part is optional

### What is username for PuTTY

Given the ssh command looks like

```
ssh username@hostname -p 2222
```

- username is the bench group name. Eg: **bench-0001-000001-f1-mumbai**
- port is 2222
- host is the proxy name, which should be something like **n1-mumbai.frappe.cloud**

### I can't ssh and none of the FAQs help

Don't panic. Please create a ticket on [support.frappe.io](http://support.frappe.io) with the following details:  





1. Output of your ssh command with the `-vvvv` option. Eg:

```
ssh <bench-name>@nx-region.frappe.cloud -p 2222 -vvvv
```

> Do not copy the above command as is. This is an example. Add `-vvvv` to the command you get from dashboard.

2. Output of

```
ssh-add -l
```

3. Information about your operating system and your SSH Client

> OS: Windows / Mac OS / Ubuntu  
> Terminal (Windows): Powershell / Command Prompt / Windows Terminal / Git bash

4. A screenshot of running the command and the output

### No sudo privileges

We do not provide root access within the bench. You very likely do not need it. If you need dependencies installed. You can [add them in your app](https://frappecloud.com/docs/faq/installing-app-apt-dependencies) itself.

### Certificate invalid: expired

In the rare instance that your bench has been deployed for a duration longer than a year and not updated since, attempting to SSH will lead to an error like so:

```
Certificate invalid: expired
frappe@10.13.2.101: Permission denied (publickey)
```

In such cases, please update your bench so that new bench version gets deployed onto which you shall be able to ssh

<!-- page: cloud/cloud__benches__updating_a_bench.md -->
---
title: "Updating a Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/updating_a_bench"
updated: "2026-03-09"
---

You will see an update banner on your bench dashboard whenever an update is available for any of the apps installed on that bench:

![](/files/JRLCR26.png)

Clicking on the **Show Updates** button will open up a dialog box where you can choose which apps to update (yes, we do have selective app updates!). Deselect the apps you don't want to update and click **Deploy**:

![](/files/KkCTePY.png)

You can monitor the progress of your deploy in the **Deploys** tab:

![](/files/lgISmb0.png)

When you click on a deploy it takes you to a screen showing each stage of the deploy.

![](/files/Screenshot%202025-09-15%20at%206.21.33%E2%80%AFPM.png)

For deploys in the running stage a `Fail Build` button will also show up which can be used to stop a build once it has started.

![](/files/Screenshot%202025-09-15%20at%206.22.17%E2%80%AFPM.png)

Fail build prompt

![](/files/Screenshot%202025-09-15%20at%206.23.48%E2%80%AFPM.png)

Proceeding with this confirmation will fail the build.

## Bench Provisioning & Queueing

Once your build phase completes successfully, the system moves into the provisioning stage. You will notice a **"Benches In Queue"** banner in your **Sites** tab:



![](/files/image99af66.png)
*Benches In Queue*

**What does this mean?**

To ensure server stability and optimal performance, we process new bench deployments through an automated queue. Your bench is currently "in line" and will begin installing on the server as soon as a processing slot becomes available. No further action is required on your par, the worker will pick up the task and start the creation process automatically.

![](/files/image55a1fb.png)
*Bench Created From Queue*



## Checking deployed app versions

Clicking on the three dots on the deploy page will show an option to view app versions.

![Screenshot 2025 11 13 at 8.35.04 PM](/files/Screenshot%202025-11-13%20at%208.35.04%E2%80%AFPM.png)

Which will lead to a dialog showing all apps deployed and their versions.

![Screenshot 2025 11 13 at 8.36.21 PM](/files/Screenshot%202025-11-13%20at%208.36.21%E2%80%AFPM.png)

These apps can also be redeployed using the button shown below.

**The "Redeploy" option will only appear in the following cases:**

- Deploy succeeded  
- Deploy failed

In cases where a deployment succeeds but the bench breaks temporarily — for example, due to:

- Connectivity issues  
- No space on the server  
- Manual deployment failures

—you can create a new, identical build and attempt the new bench again using **Redeploy**.

> Note: You cannot deselect **Frappe Framework** if you want to update **ERPNext**

> After Bench is updated, the sites (as long as auto update is enabled) shall auto update during non-working hours. (1 AM - 4 AM)

## Auto Deploy Via Commit Markers

Deploying a bench can be automated using the `press-deploy` **commit marker**.

### Deploying all applicable benches

To update multiple benches where an app is installed, include the marker in your commit message. For example:

```
Added new changes to custom app press-deploy
```

This automatically deploys all benches owned by the team where the app is installed and have a `auto-deploy` tag on them.

![](/files/image6db661.png)

### Deploying a specific bench

You can also target a specific bench by including its identifier in the marker. For example:

```
Added new changes to custom app press-deploy-bench-10202
```

This deploys the specified bench template (`bench-10202`) with the changes from the custom app.

### Conditions where deployment will NOT occur

A bench will not be deployed if any of the following conditions are met:

- The bench is not owned by the team creating the new app release
- The bench is not enabled
- A deployment is already in progress for that bench

## Yanked App Releases

A marketplace app release may be marked as **yanked**. Yanked releases are withdrawn and should not be installed or used for updates.

Because of this, you may occasionally see a message like the one below when updating a bench. 

![](/files/imageb26663.png)

This typically indicates that the available release has been yanked and is therefore skipped during the update process.

To resolve this, ensure that a valid (non-yanked) release is selected for update.

<!-- page: cloud/cloud__benefits.md -->
---
title: "Benefits"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benefits"
updated: "2026-05-07"
---

## Why Frappe Cloud?

Frappe Cloud is the recommended cloud platform to host Frappe apps. It takes the hassle out of hosting and managing Frappe apps so you can focus on what truly matters: building and growing your business.

1. **Effortless Hosting** – Deploy your Frappe apps in minutes with a fully managed infrastructure. No server headaches, just smooth performance.
2. **Seamless Scaling** – Frappe Cloud grows with you whether you're a startup or an enterprise. Upgrade resources as needed without downtime.
3. **Automatic Updates & Backups** – Stay secure and up-to-date with automated updates and regular backups. No more manual maintenance.
4. **Optimized for Speed & Reliability** – Our cloud is fine-tuned for Frappe apps, ensuring fast load times and high availability.
5. **Built-in DevOps Tools** – Get staging environments, database access, logs, and more—right from your dashboard.
6. **Transparent Pricing** – No hidden fees, no surprise bills. Pay only for what you use, with predictable costs.

---

Watch this video to know more about **benefits of Frappe Cloud for business users**. 

<iframe src="https://www.youtube.com/embed/pYwv4QAPjXg?si=Sqh9mt-f5Gtrq_EU" width="800" height="450" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



---

Watch this video to know more about **benefits of Frappe Cloud for Frappe developers, consultants & partners**.  

<iframe src="https://www.youtube.com/embed/sAUr_RO01-A?si=jBU90V63c9LWouS7" width="800" height="450" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



---

<!-- page: cloud/cloud__billing__bill-payments.md -->
---
title: "Bill Payments"
space: "Cloud"
url: "https://docs.frappe.io/cloud/billing/bill-payments"
updated: "2026-04-29"
---

Your account balance accrues over the course of the calendar month based on  
usage of your sites. We apply GST taxes to Indian customers.

We automatically invoice and charge your account's default payment method on the  
last day of every month for the month's usage.

## Current Month's Usage

You can check your running usage amount in the Dashboard.

Go to Billing in the left pane. Here you will see the usage amount to date. This  
amount is updated every day based on the number of Active sites you have.



![](/files/Screenshot 2026-04-29 at 1.40.41 PM.png)

## Managing Cards

You can add cards from the Payment Methods section in the Billing Tab.

Click on **Add Card** and enter your billing address and card details.  
It will automatically become the default payment method.



![](/files/Screenshot 2026-04-28 at 11.27.19 AM.png)
*Payment Methods tab in Billing showing card details*



## UPI Autopay (*Supported only for Indian customers*)

UPI Autopay lets you set up a one-time mandate with your **UPI ID**. Your monthly Frappe Cloud subscription is then automatically debited — no manual payment, no missed invoices, no service interruptions.

### How to set it up?

1. Go to Billing →  Mode of payment and select **UPI Autopay**.
2. You will be redirected to the mandate setup page. Click **"Setup Autopay"** and complete the authorization via your UPI app.
3. A one-time ₹1 authorization charge is made to confirm mandate creation.
4. Once authorized, your UPI account will be auto-debited every month end.

![](/files/Screenshot 2026-04-28 at 7.10.41 PM.png)
*Setup mandate pop up form for UPI Autopay*

### How auto-debit works?

 At the end of each billing cycle, you will receive an SMS notification about the upcoming debit. The actual debit happens 25 hours after the notification is sent.

### Things to know

- UPI Autopay mandates have a maximum limit of **₹1,00,000**. This mode of payment is recommended only if your monthly invoice is below this limit.
- If your invoice amount exceeds your mandate limit, the auto-debit will not be attempted. You will receive an email notification asking you to either set up a new mandate with  a higher limit or pay manually.
- You can cancel your mandate anytime from the Billing → UPI Autopay tab and switch to a different payment mode.

<!-- page: cloud/cloud__billing__billing-cycle.md -->
---
title: "Billing Cycle"
space: "Cloud"
url: "https://docs.frappe.io/cloud/billing/billing-cycle"
updated: "2026-03-06"
---

Overview of Frappe Cloud's Billing Process

Frappe Cloud billing cycles are monthly. Each site is microbilled on a daily basis. When you select a plan, the monthly amount is divided by the number of days in the current calendar month. You are charged every day based on the number of sites you have each day.



![Billing Dashboard](https://cloud.frappe.io/assets/press/images/docs/account-billing.png)

  


You can access and update your billing information from [/dashboard/account/billing](/dashboard/account/billing). The dashboard also shows information regarding the current usage from all your sites.

> We finalize invoices on **the last day of each month at 6 PM IST**. Sites created after this point will be a part of next month's billing cycle.

## Use Cases

Here's an attempt to explain the process by considering a few use cases:

### Single **plan** throughout the calendar month

When you select the `$100` plan for your site `raftel.frappe.cloud`, every day `$3.33` is accrued to your monthly usage in case of a 30 day month. For the month of April, the estimate would look something like


| -   | Base Plan | No. of Days | Rate      | Total     |
| --- | --------- | ----------- | --------- | --------- |
|     | $100      | 30          | $3.33/day | $99.9     |
|     |           |             |           | **$99.9** |


This rate may go to `$3.23` in case of a 31 day month or `$3.57` in case of a 28 day month. This means that you are charged no more than `$100` for hosting your site each month. For February 2024 (leap year), this would look something like


| -   | Base Plan | No. of Days | Rate      | Total       |
| --- | --------- | ----------- | --------- | ----------- |
|     | $100      | 29          | $3.45/day | $100.05     |
|     |           |             |           | **$100.05** |


### Multiple plans throughout the calendar month

Another instance of hosting a site `laugh-tale.frappe.cloud` on `$200` plan. After 15 days, you need more CPU time and decide to upgrade to plan `$500`. For a 31 day month, you get charged `$354.84` in total. Here's the break up.


| -   | Base Plan | No. of Days | Rate       | Total       |
| --- | --------- | ----------- | ---------- | ----------- |
|     | $200      | 15          | $6.45/day  | $96.77      |
|     | $500      | 16          | $16.13/day | $258.07     |
|     |           |             |            | **$354.84** |


### Site dropped in the middle of the month

If you drop your site `arabasta.frappe.cloud` 4 days into the month, you will be charged for those 4 days.


| -   | Base Plan | No. of Days | Rate      | Total     |
| --- | --------- | ----------- | --------- | --------- |
|     | $200      | 4           | $6.45/day | $25.8     |
|     |           |             |           | **$25.8** |


> Even if you might drop all your sites mid-way, you will receive the invoice at the end of the month.

<!-- page: cloud/cloud__billing__disable-account.md -->
---
title: "Disable Account / Cancel Subscription"
space: "Cloud"
url: "https://docs.frappe.io/cloud/billing/disable-account"
updated: "2026-02-16"
---

If you no longer want to use Frappe Cloud services and you want to disable your account, follow these steps:

1. Login to your dashboard
2. Drop all the sites and servers
3. Click on Settings in the top bar
4. Under Team Actions section, click on the Disable button against Disable Account![Screenshot from 2023-12-04 19-41-08](/files/Screenshot from 2023-12-04 19-41-08.png "Screenshot from 2023-12-04 19-41-08.png")
5. After you confirm, your account will get disabled


	* Your sites will get suspended
	* You won't be able to create new sites
	* Your billing will be paused


> Frappe Cloud is not responsible for any refunds if the above steps are not followed properly before disabling or closing your account.
> 
> 

<!-- page: cloud/cloud__billing__payment_options.md -->
---
title: "Payment Options"
space: "Cloud"
url: "https://docs.frappe.io/cloud/billing/payment_options"
updated: "2026-02-16"
---



In case you are not able to add your card or have issues with card payments, you can wire us the money.

The minimum amount that you need to transfer is ₹25000 for Indian customers and $300 for everyone else. This amount will be added to your account balance and it will consumed based on your usage.

After you have completed the transfer, please open a [Support Ticket](https://support.frappe.io/helpdesk/tickets) with the payment details like Reference Number, Payment Amount, etc.

### Wire Transfer (USD to USD transfers only)

| Name of Bank | HDFC Bank Ltd. |
| ------------------------------- | ------------------------------------------------------------------------------ |
| Address of Bank | 1st Floor, Sanghavi Square, M. G. Road, Ghatkopar (W), Mumbai - 400086, India. |
| Currency | USD |
| Account Number | 50200043297249 |
| Account Name (Beneficiary Name) | Frappe Technologies Pvt. Ltd. |
| IFSC Code | HDFC0000998 |
| SWIFT Code | HDFCINBBXXX |
| Account Type | Current Account |


### Payment in other currencies

| Name of Bank | HDFC Bank Ltd. |
| ------------------------------- | ------------------------------------------------------------------------------ |
| Address of Bank | Dheeraj Kawal, Ground Floor, LBS Marg, Vikhroli West (Mumbai) 400079, India. |
| Currency | INR |
| Account Number | 01632320001931 |
| Account Name (Beneficiary Name) | Frappe Technologies Pvt. Ltd. |
| IFSC Code | HDFC0000998 |
| SWIFT Code | HDFCINBBXXX |
| Account Type | Current Account |

### PayPal ID

You can also send us the money via PayPal at this email: **billing@erpnext.com**


### Tax Details

PAN Number: **AAACW8099E**

GSTN: **27AAACW8099E1ZX**

<!-- page: cloud/cloud__binlog-browser.md -->
---
title: "Binlog Browser"
space: "Cloud"
url: "https://docs.frappe.io/cloud/binlog-browser"
updated: "2026-02-16"
---

### What is a Binary Log?
The Binary Log (Binlog) in MariaDB records all changes made to the database. This includes SQL statements that modify data (INSERT, UPDATE, DELETE) and DDL statements that change the structure of your tables.

### What is the Binlog Browser?
Binlog Browser is a GUI tool that lets you view your database’s binary logs. You can check which query ran, when it ran, and on which table it was executed.

![shape 6VgHcwX BE D LDcpXMVN at 25 12 09 01.14.54](/files/shape_6VgHcwX_BE-D_LDcpXMVN%20at%2025-12-09%2001.14.54.png)

### Where to find it?
You can find it in the sidebar under `Devtools > Binlog Browser`.  
If you don’t see the option, make sure you have completed your Frappe Cloud onboarding. If it still doesn’t appear, please contact support.frappe.io.

### Who can access it?
Right now, only dedicated database servers with at least 8GB RAM can use this tool. Once the feature is more stable, it will also be available for servers with 4GB RAM.

### Why do we need the Binlog Browser?
Binary logs are stored in a binary format, which makes them difficult and resource-heavy to read manually.

You might use the Binlog Browser for debugging, such as:

- When some data looks wrong or missing. Binlogs can show which query caused it.
- When binlog file sizes suddenly grow. Binlog Browser helps identify the queries responsible or shows which database had heavy writes.
- When doing point-in-time restoration or checking that no writes happened after a backup. Binlog Browser helps confirm this.

### How it works?
The Binlog Browser depends on another tool called the Binlog Indexer.  
The Indexer converts binary logs into metadata that can be queried quickly.

If the indexer is not enabled, you will see a page like this:

![imagea979cb](/files/imagea979cb.png)

### How to enable the Binlog Indexer / Browser?
Please refer to the [documentation](https://docs.frappe.io/cloud/database-server-actions#enable--disable-binlog-indexer) to enable it.  


### Automated Binlog Indexing
By default, Frappe Cloud runs a job every hour that indexes 4 binlogs.  
During this time, you cannot access the Binlog Browser, and you will see a page like this:

![imagefb1862](/files/imagefb1862.png)

You will need to wait for the job to finish.

### Binlog Indexing Status
If your binlogs are not indexed yet, the Binlog Browser will show no results.

To check which binlogs are indexed, click the `Binlogs` icon on the top-right.  
This opens a modal showing each binlog, its size, and its index status.

![image6af702](/files/image6af702.png)

### On-demand Binlog Indexing
If you need to index multiple binlogs urgently, you can select the binlogs and submit an indexing request.

![image0376db](/files/image0376db.png)

After submitting, you will be redirected to a page where you can track the job status.  
Once completed, you can return to the Binlog Browser to access the newly indexed binlogs.

<!-- page: cloud/cloud__cant-connect-to-mysql-server.md -->
---
title: "Can't connect to MySQL server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/cant-connect-to-mysql-server"
updated: "2026-02-16"
---

```
ERROR 2002 (HY000): Can't connect to MySQL server on '10.1.1.1' (115)
```

You may see this error when **restoring** a site or during an **update site migrate** job. This likely happened as the mysql server restarted as it didn't have sufficient memory for the operation. Changing the **database server** plan for more memory should fix this. To change plan of your dedicated database server, refer [this guide](https://frappecloud.com/docs/servers/plan)

<!-- page: cloud/cloud__change-notification-email-of-team.md -->
---
title: "Change notification email of Team"
space: "Cloud"
url: "https://docs.frappe.io/cloud/change-notification-email-of-team"
updated: "2026-02-16"
---

1. From your Frappe Cloud dashboard go to `settings`> `Profile`
2. Browse to `Notification Setting` and click on `Manage`

![](/files/imagebde6b6.png)

1. Click on **new** and select the type to billing and update the email ID and `Update Settings` Similarly you can customise notifications for other types to.

![](/files/imagec787ec.png)

<!-- page: cloud/cloud__change-ownership-of-server.md -->
---
title: "Change ownership of Server"
space: "Cloud"
url: "https://docs.frappe.io/cloud/change-ownership-of-server"
updated: "2026-02-16"
---

At the moment, changing server ownership through the dashboard isn't supported. However, you can submit a request by raising a ticket at **support.frappe.io**, and we'll be happy to assist you.

<!-- page: cloud/cloud__change-team-of-bench-group.md -->
---
title: "Change Team of Bench"
space: "Cloud"
url: "https://docs.frappe.io/cloud/change-team-of-bench-group"
updated: "2026-03-10"
---

You can change the team of the site by using the **Transfer Bench** feature.

1. Select Transfer Bench option from the Actions tab in your Bench's dashboard.

![](/files/Screenshot%202025-08-20%20at%203.57.05%E2%80%AFPM.png)

2. Fill in the fields and click on **Transfer**

![](/files/Screenshot%202025-08-20%20at%204.18.57%E2%80%AFPM.png)

3. The team that is supposed to receive the ownership will now receive a mail to accept the ownership. Click on **Accept Bench Group Transfer** to accept the ownership of the Bench Group.

![](/files/271fd2b6-b11a-48e6-ad5f-28099df46c2c0b59ef.jpeg)

<!-- page: cloud/cloud__common-issues__build-might-fail.md -->
---
title: "Build might fail"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/build-might-fail"
updated: "2026-02-16"
---

If you have come across a similar Dialog such as the one below while updating your bench group, it means that the underlying reason for why your previous build failed has not been addressed.

![](/files/mohwHpR.png)  


How to fix this?
----------------

1. First navigate to the Deploys under the current Bench Group:

![](/files/JOmCeK8.png)
2. Then click on the last Deploy (which should have the status *Failure* with a "!" next to it):![](/files/6ly6YW3.png)
3. Under the Deploy, notice the red banner and click on the View button:![](/files/qH07S6Z.png)
4. On clicking View, you will see a dialog with details about the failure and how to fix it.![](/files/lLBqzfJ.png)
5. Follow the steps in the dialog, or under the linked *Help* article and then retry the update.

  


  

<!-- page: cloud/cloud__common-issues__debugging-app-installs-locally.md -->
---
title: "Debugging app installs locally"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/debugging-app-installs-locally"
updated: "2026-02-16"
---

If your deploy has failed at an **Install Apps** step or at the **Run Validations - Pre-build** step, chances are that there is some kind of error in one (or several) of the apps on your bench group.

![](/files/6inBnfg.png)  


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

![](/files/zxILVOH.png)

<!-- page: cloud/cloud__common-issues__incompatible-app-version.md -->
---
title: "Incompatible app version"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/incompatible-app-version"
updated: "2026-02-16"
---

If you have been seeing a message such as this it means that an app on your bench group is not compatible with some other apps.

![](/files/dsrx1dI.png)  


Going forward, I'll use the example of *HRMS*.

*HRMS* depends on *Frappe.* Not just any version of *Frappe,* but a version that satisfies the version (or version range) specified by it. For example: **>=16.0.0-dev,<17.0.0**.

This requirement is mentioned in an apps `pyproject.toml` file. For [example](https://github.com/frappe/hrms/blob/c1704c9767b9c78b23d67cb6b0514afc084cc0dd/pyproject.toml#L69):

![](/files/JGEWytA.png)  


To fix this, you will have to change to the correct branch**:**

* Navigate to the **Apps** tab on your **Bench Group**
* Locate the app to be updated
* Click on **Change Branch** under the `···` menu button:

![](/files/OFMGoDr.png)  


If you are unsure which branch to change to, you can check the app's version by checking it's `__init__.py` file, [example](https://github.com/frappe/frappe/blob/6fb6c4035cb4bd17e22143f7c483af34a296ca0c/frappe/__init__.py#L52):![](/files/xY9UkHC.png)  



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

![](/files/xuXDeMs.png)  



> ℹ️ **Tip**
> 
> To set a custom dependency version view [this documentation page](https://frappecloud.com/docs/benches/editing-bench-dependency-version#setting-a-custom-version).
> 
> 

You should see an **Edit Dependency** dialog pop up:

![](/files/Uma6lVx.png)  


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

![](/files/xuXDeMs.png)  



> ℹ️ **Tip**
> 
> To set a custom dependency version view [this documentation page](https://frappecloud.com/docs/benches/editing-bench-dependency-version#setting-a-custom-version).
> 
> 

You should see an **Edit Dependency** dialog pop up:

![](/files/Uma6lVx.png)  


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

![](/files/R0Aw7pM.png)  


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

![](/files/ceICxKm.png)  


After this is done, you will have to add the correct app. Check the next section (**App is not present**) for this.

### App is not present

To fix this navigate to the **Apps** tab on your bench group and then click on **Add App**:![](/files/S6IlTRy.png)  


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

![](/files/GHCwZ91.png)  


Then it means that the `vite` build dependency wasn't installed when your app was being installed.

Why does this happen?
---------------------

This can happen if your project has two `package.json` files such as this ([repository](https://github.com/frappe/gameplan)):

![](/files/od75sCA.png)  


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

![Screenshot 2025-01-31 at 1.15.44 PM](/files/Screenshot 2025-01-31 at 1.15.44 PM.png "Screenshot 2025-01-31 at 1.15.44 PM.png")
2. Open your Superset dashboard and go ahead with connecting a new database.

![Screenshot 2025-01-31 at 2.53.56 PM](/files/Screenshot 2025-01-31 at 2.53.56 PM.png "Screenshot 2025-01-31 at 2.53.56 PM.png")
3. Choose **MySQL** as database type.

![Screenshot 2025-01-31 at 2.54.49 PM](/files/Screenshot 2025-01-31 at 2.54.49 PM.png "Screenshot 2025-01-31 at 2.54.49 PM.png")
4. Fill in all the required details and ensure the **SSL** checkbox is checked. Then, proceed.

![Screenshot 2025-01-31 at 2.56.20 PM](/files/Screenshot 2025-01-31 at 2.56.20 PM.png "Screenshot 2025-01-31 at 2.56.20 PM.png")
5. You will see this message upon a successful connection.

![Screenshot 2025-01-31 at 3.19.46 PM](/files/Screenshot 2025-01-31 at 3.19.46 PM.png "Screenshot 2025-01-31 at 3.19.46 PM.png")
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

![Screenshot 2025-01-31 at 1.15.44 PM](/files/Screenshot 2025-01-31 at 1.15.44 PM.png "Screenshot 2025-01-31 at 1.15.44 PM.png")
2. Go to Looker Studio and click on **Create New Data Source** !

![Screenshot 2025-01-31 at 1.39.14 PM](/files/Screenshot 2025-01-31 at 1.39.14 PM.png "Screenshot 2025-01-31 at 1.39.14 PM.png")
3. Search for **mysql** in connector list and choose the connector from Google.

![Screenshot 2025-01-31 at 1.40.34 PM](/files/Screenshot 2025-01-31 at 1.40.34 PM.png "Screenshot 2025-01-31 at 1.40.34 PM.png")
4. Fill up the database user's info and click on **Authenticate**. 

  


**Note :** You need to check **Enable SSL** and must provide the SSL certificate. Check the representation image of **Step 1** of this documentation to get the idea from where to download the certificate.

  


![Screenshot 2025-01-31 at 1.45.07 PM](/files/Screenshot 2025-01-31 at 1.45.07 PM.png "Screenshot 2025-01-31 at 1.45.07 PM.png")
5. Choose the required table and click on **Connect**.
6. After that, you can see the details of the table and create required reports. 

![Screenshot 2025-01-31 at 1.59.10 PM](/files/Screenshot 2025-01-31 at 1.59.10 PM.png "Screenshot 2025-01-31 at 1.59.10 PM.png")
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

  


![Screenshot 2025-01-31 at 1.15.44 PM](/files/Screenshot 2025-01-31 at 1.15.44 PM.png "Screenshot 2025-01-31 at 1.15.44 PM.png")
2. Open your Metabase dashboard and click on **Add database**.
3. Choose **MySQL** as Database Type and fill all the database user related information.  
  


**Note :** Ensure that `Use a secure Connection (SSL)` is checked.

  


For **Server SSL certificate Chain**, check the **Step 1** and download the certificate first. Next, open your operating system's default text editor and copy- paste to metabase. 

![Screenshot 2025-01-31 at 2.14.10 PM](/files/Screenshot 2025-01-31 at 2.14.10 PM.png "Screenshot 2025-01-31 at 2.14.10 PM.png")
4. Once all the details filled, click on **Save**.
5. If everything works fine, you will see your database in the list.

![Screenshot 2025-01-31 at 2.19.23 PM](/files/Screenshot 2025-01-31 at 2.19.23 PM.png "Screenshot 2025-01-31 at 2.19.23 PM.png")
6. Wait a few minutes for the table schema to sync, then you can view the metadata.

![Screenshot 2025-01-31 at 2.26.22 PM](/files/Screenshot 2025-01-31 at 2.26.22 PM.png "Screenshot 2025-01-31 at 2.26.22 PM.png")
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

![Screenshot 2025-01-31 at 1.15.44 PM](/files/Screenshot 2025-01-31 at 1.15.44 PM.png "Screenshot 2025-01-31 at 1.15.44 PM.png")

Step 2: Install MariaDB ODBC connector
--------------------------------------

1. Download MariaDB ODBC Connector v3.1.x ([Download link](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector)). 


> **Note**: Please avoid installing v3.2.x as it has a [bug](https://community.fabric.microsoft.com/t5/Power-Query/Excel-Power-Query-issue-with-MariaDB-ODBC-driver/m-p/4320893) that causes it to not work with Power BI.
> 
> 

![256](/files/256.png "256.png")
2. Install ODBC Connector.

![ss2 1](/files/ss2 1.png "ss2 1.png")  


![ss3](/files/ss3.png "ss3.png")  


![ss5](/files/ss5.png "ss5.png")

Step 3: Setup Credentials in ODBC
---------------------------------

1. Open **ODBC Data Sources** with **Run as administrator.**


> **Note :** If you have installed ODBC connector of x64 version, then you should open `ODBC Data Sources (64-bit)` and if you have downloaded and installed x32 version, then open `ODBC Data Sources (32-bit)`
> 
> 

![ss12](/files/ss12.png "ss12.png")
2. Click on **Add** button in **User DSN** tab.

![ss19](/files/ss19.png "ss19.png")
3. Choose **MariaDB ODBC 3.1 Driver**.

![27](/files/27.png "27.png")
4. Put the **Server Name** , **Port**, **Use Name** , **Password**, **Database** in the required fields and go to next page.


> **Note:** Currently If you try to click on **Test DSN**, it will fail. We need to do few more configurations to make it working.
> 
> 

![ss14](/files/ss14.png "ss14.png")
5. No information is needed on the current page. Proceed to the next page.

![17](/files/17.png "17.png")
6. No information is needed on the current page. Proceed to the next page.

![18](/files/18.png "18.png")
7. In current page, make sure to check **Verify Certificate** & **Force TLS Use** checkbox.

![ss17](/files/ss17.png "ss17.png")
8. No information is needed on the current page. Click on **Finish** to save it.

![ss18](/files/ss18.png "ss18.png")

Step 4: Configure MariaDB ODBC In Power BI Desktop
--------------------------------------------------

1. Open Power BI and click on **Get Data From Other Sources**.

![ss6](/files/ss6.png "ss6.png")
2. Search for **ODBC** and click on **Connect**.

![ss20](/files/ss20.png "ss20.png")
3. Choose the ODBC connection from the list. It should be the same you have created in **ODBC Data Sources Administrator** in **Step 3**.

![21](/files/21.png "21.png")
4. Now, it might ask you for username and password. Choose **Windows** from the sidebar and click on **Connect**.

![25](/files/25.png "25.png")
5. Once connected, you will be able to view all the tables and their previews.

![257](/files/257.png "257.png")
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

![Screenshot 2025-01-31 at 1.15.44 PM](https://frappecloud.com/files/Screenshot%202025-01-31%20at%201.15.44%20PM.png)
2. Open your Zoho Analytics dashboard and go to **Import Data** page.

Search & Select **MariaDB** from the list**.**  
![Screenshot 2025-01-31 at 3.28.14 PM](/files/Screenshot 2025-01-31 at 3.28.14 PM.png "Screenshot 2025-01-31 at 3.28.14 PM.png")
3. Change **Cloud Service Provider** to **Other Cloud Services** and fill all the required details.   
Make sure to check **SSL** checkbox.

![Screenshot 2025-01-31 at 3.37.43 PM](/files/Screenshot 2025-01-31 at 3.37.43 PM.png "Screenshot 2025-01-31 at 3.37.43 PM.png")
4. Choose the tables to import and Schedule it.

![Screenshot 2025-01-31 at 3.39.33 PM](/files/Screenshot 2025-01-31 at 3.39.33 PM.png "Screenshot 2025-01-31 at 3.39.33 PM.png")![Screenshot 2025-01-31 at 3.41.40 PM](/files/Screenshot 2025-01-31 at 3.41.40 PM.png "Screenshot 2025-01-31 at 3.41.40 PM.png")
5. You will be able to see the data sources in your dashboard.

![Screenshot 2025-01-31 at 3.48.50 PM](/files/Screenshot 2025-01-31 at 3.48.50 PM.png "Screenshot 2025-01-31 at 3.48.50 PM.png")
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





![Configure compute allocation in Dangerous Actions](https://github.com/user-attachments/assets/1ac674d7-34c7-44e5-9209-efd76c17a776)



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

![](/files/imagee17cda.png)

**Resolution**

Create the file and add the required dependency section.

---

### 2️⃣ Missing `[tool.bench.frappe-dependencies]` Section

**Error Meaning**

The `pyproject.toml` exists, but the required dependency section is not defined or not in the exact format as mentioned above.

![](/files/image7f70a5.png)

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

![](/files/image49e8dc.png)

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

![Screenshot 2024-11-20 112324](/files/Screenshot 2024-11-20 112324.png "Screenshot 2024-11-20 112324.png")

This will replace the Vanilla Frappe Framework with your custom fork / version.

<!-- page: cloud/cloud__daily-usage-limit-reached.md -->
---
title: "Daily Usage limit reached"
space: "Cloud"
url: "https://docs.frappe.io/cloud/daily-usage-limit-reached"
updated: "2026-05-25"
---

![](/files/image1ab73f.png)

This happens when you exceed CPU hours allotted for your site. If you're confused as to how you reached your CPU hours limit, you can check the **Insights** tab of your site.

![](/files/image59cb58.png)

Here, you can scroll down to **Advanced analytics** to see:the **Slowest Requests** and **Slowest Background Jobs** graphs. This will give you an idea of which endpoints in your site take most time/requests. We can take a look at the following graphs as an example

![](/files/hyEEfqL.png)

Here, the red bars are seem to take relatively long and should be looked into.

![](/files/uhKZI97.png)

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

![](/files/image26b043.png)

## Storage Breakdown

If you want to check disk usage by every table in your database, you can click on the `Storage Bar`

You can then view usage by each table

![](/files/Screenshot%20from%202025-05-30%2018-07-06.png)

## Database Processes

If you want to view all the active database queries, you can view them from the same page and even kill the query if it's stuck.

![](/files/Screenshot%20from%202025-05-30%2018-08-50.png)



## Database Locks

MairaDB lock report helps to find active locks on the specific database. This helps with investigating `lock timeout error` issues.

![](/files/image7740af.png)

## Slow Queries

Slow queries usually affect the performance of your site. You can find all the information about slow queries.

![](/files/Screenshot%20from%202025-05-30%2018-09-10.png)

## Time Consuming Queries

Sometimes there are queries that execute very fast but run very frequently and, in total, consume a lot of your database's CPU time.

These queries don't always affect database performance, but the results can help you further optimize your code.

![](/files/Screenshot%20from%202025-05-30%2018-09-20.png)

## Full Table Scan Queries

If queries lack indexing or have issues, they can cause full table scans, which hurt your database performance the most.

You can find these kinds of queries and optimize them for better performance.

![](/files/Screenshot%20from%202025-05-30%2018-09-27.png)

## Index Analysis

Other than that, you can click on `Suggest Indexes`, and the system will try to analyze slow queries and provide suggestions based on that.

![](/files/Screenshot%20from%202025-05-30%2018-09-49.png)

<!-- page: cloud/cloud__database-server-actions.md -->
---
title: "Database Server Actions"
space: "Cloud"
url: "https://docs.frappe.io/cloud/database-server-actions"
updated: "2026-08-13"
---

On **Server Actions** page, you will find several options for database configuration.

![image9765dc](/files/image9765dc.png)

## What is Binlog &amp; Why It's required ?

The **Binary Log (Binlog)** in MariaDB is a crucial logging mechanism that records all changes to the database - such as SQL statements that modify data (INSERT, UPDATE, DELETE). It does **not** log SELECT queries.

Binlogs are primarily used for:

- **Replication**: Keeping replicas in sync with the primary database.
- **Point-in-time recovery**: Restoring a database to a specific moment in time.

For example, if a site is accidentally deleted or broken due to a faulty SQL query, in that case binlogs combined with the last available backup—allow you to **roll back to a specific time** and recover your data.

## View &amp; Purge Binlogs

You can view binary log file sizes by date. If you're running low on storage, it's possible to **purge old binlogs** that are no longer needed.

![](/files/482719248-8eb4ca2d-b434-42c8-bf76-0e672384f3e5.png)

![](/files/img2.png)

![](/files/img3.png)

## Manage Binlog Retention

By default, when Frappe Cloud provisions a server, MariaDB has a **binlog retention period of 14 days**.

If your site handles a large volume of transactions and binlogs are filling up your storage quickly, you may choose to **reduce the retention period**.

Alternatively, for compliance or auditing purposes, you can **increase binlog retention** as needed.

You can manage these settings directly from the interface:

![](/files/482719805-9d2688b7-0a96-458e-aba1-186e417a56a9.png)

## Binlog Auto-Purging Based on Size Limit

Binlog files can occasionally grow rapidly, consuming a significant portion of your disk space. If Auto Add-on Storage is not enabled, this may lead to storage exhaustion and potential downtime for your server or application.

The Binlog Auto-Purging feature helps prevent such issues by allowing you to define a size limit for binlogs. When the total binlog size exceeds this limit, the system automatically purges older binlogs to bring usage back within the specified threshold.

![image3b13b3](/files/image3b13b3.png)

## Enable / Disable Binlog Indexer

The **Binlog Indexer** converts binary logs into a readable, searchable format, allowing end-users to explore and query binlogs using the **Binlog Browser**.

To **enable** the binlog indexer and browser, click on `Enable Binlog Indexer` under `Database Server Actions`, then confirm the action.

![image16cc0f](/files/image16cc0f.png)

To **disable** the binlog indexer and browser, click on `Disable Binlog Indexer` under `Database Server Actions`, then confirm the action.

![image7a1581](/files/image7a1581.png)

## **Default Configuration for Database Servers:**

- When a server is created with Auto Add-on Storage enabled, binlogs can use up to 75% of the total disk capacity.
- When a server is created with Auto Add-on Storage disabled, binlogs can use up to 20% of the total disk capacity.

These are the default limits, but you can adjust them based on your requirements.

**Note :** This feature is not available for database servers configured with replicas.

## Performance Schema

If you own some dedicated server, you can enable/disable the performance schema as per requirement.

![](/files/Screenshot%20from%202025-04-09%2023-05-01.png)

## Manage InnoDB Buffer Pool Size

If you want to change innodb buffer pool size, you can now do that from Frappe Cloud dashboard.

![](/files/Screenshot%20from%202025-04-09%2023-06-19.png)

## Manage Max Database Connections

When you create a database server, Frappe Cloud set a default max connections based on the total memory on the server. In case if you need more database connection, you can increase that from dashboard.

![](/files/Screenshot%20from%202025-04-09%2023-11-58.png)

## View Database Configurations

If you want to check all the configuration of your dedicated database server, you can use the `View Database Configuration` option.

![](/files/Screenshot%20from%202025-04-09%2023-13-16.png)

Currently, it's not allowed to change in variable. If you need some special configuration, please reach out to support.frappe.io

## Database Audit Trail

For compliance purposes, if you need a database audit trail, you can enable it from **Server Actions** in the Frappe Cloud dashboard.



Database audit trail has two capture modes:

1. **Only write queries :** Captures queries that modify the database, such as changes to databases, tables, or rows. Read queries are not logged.
2. **Read and write queries :** Captures all queries running on the database, including `SELECT` queries. Since read queries are also logged, the log size can be **at least 3X larger**.

![](/files/image701fa8.webp)

The cost is **2 INR per GB per month**, based on your log's storage usage. All audit logs are uploaded to S3, so they won't use additional disk space on the server.



We recommend keeping **at least 20 GB of free disk space** for audit logging. Audit logs are rotated and uploaded every **2 hours**, so you should have enough free space to store up to 2 hours of logs locally on the server.

### Accessing Database Audit Logs

From the server actions, you can view all the stored audit logs.

![](/files/imagea17bff.webp)

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

![](/files/oAAWNad.png)



## Create Database User

Click on `Add User` button to open the modal for creating database users.

1. **Read Only Mode :**

![](/files/LIaAMBi.png)

2. **Read Write Mode :**

![](/files/rnKuRtd.png)

3. **Granular Mode :**

> When you begin configuring `Granular Access`, the system will load your database's table schema. This process may take anywhere from 30 seconds to 5 minutes, depending on the number of tables in your database.

You can set the **Read Only** or **Read Write** mode for each table individually. Additionally, if needed, you can restrict access to specific columns within a table by selecting the columns you want to grant access to.





![](/files/0GCIfFc.png)

## Edit Database User

If you want to modify the permissions for a specific database user, you can easily do so by selecting the **Configure User** option in the row menu. This will allow you to adjust the user’s access levels and permissions as needed.

![](/files/7yIJjuJ.png)



You can make the changes to the user's permissions and save them. Once saved, it may take some time for the updates to take effect.

> Please note that if the database user previously had **Read Only** or **Read Write** global privileges, any changes you make to their permissions will not take effect immediately. These changes will only apply to new connections created after the update.

## View Database Credential

Click on the three dots in the row and select **View Credential** to view the details for that specific user’s credentials.

![Screenshot 2024-12-03 at 12.18.52 PM](/files/Screenshot 2024-12-03 at 12.18.52 PM.png "Screenshot 2024-12-03 at 12.18.52 PM.png")



After selecting **View Credential**, a modal will appear displaying all the necessary information to connect to your site database.

![Screenshot 2025-01-31 at 1.15.44 PM](https://frappecloud.com/files/Screenshot%202025-01-31%20at%201.15.44%20PM.png)



## Delete Database User

Click on the three dots in the row and select **Delete User** to remove the database user.

![Screenshot 2024-12-03 at 12.16.58 PM](/files/Screenshot 2024-12-03 at 12.16.58 PM.png "Screenshot 2024-12-03 at 12.16.58 PM.png")



When you click to delete a user, a confirmation modal will appear. Once you confirm the deletion, the selected database user will be deleted.

![](/files/EMGuv7B.png)



## Access Logs

If you want to view all the SQL query pass through FC SQL Proxy service, you can click on `View Logs` button.

![](/files/Screenshot%20from%202025-05-29%2015-09-12.png)

You can filter search result by some keywords or client IP.

![](/files/Screenshot%20from%202025-05-29%2015-08-47.png)

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

![Database Access CLI](https://frappecloud.com/files/database-access-cli.png)



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

![](/files/mSVGlQQ.png)
* Select the log you want to view from the log list

![](/files/1xDxcYJ.png)
* Filter, sort and search through the log file as you need

![](/files/6dMT07r.png)


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

![](/files/Screenshot 2026-03-10 at 11.01.58 AM.png)

3. You will be asked to confirm the name of the Bench you want to drop.

![](/files/Screenshot 2026-03-10 at 11.02.35 AM.png)

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
  
Once your v15 site is moved from public/shared to private bench group, server script will be enabled automatically.![](/files/nRVHZHi.png)  


  

<!-- page: cloud/cloud__faq__app-installation-issue.md -->
---
title: "App Installation Issue"
space: "Cloud"
url: "https://docs.frappe.io/cloud/faq/app-installation-issue"
updated: "2026-02-16"
---

If you have been seeing the *Attention Required* status badge next to your apps:

![](/files/j6PGkOJ.png)  


It means that Frappe Cloud could not fetch the source code of your application.

This can be because of multiple reasons, here are two:

1. The **App Installation ID** of your app is missing or is invalid.
2. An **invalid URL** is being used to fetch your app.

Please see the specific sections to find out and fix the cause.

Invalid URL
-----------

To figure out if your app has an invalid URL, navigate to **Apps** under your Bench Group's page and ensure that the *repository path* of your app is correct:

![](/files/bw19HP3.png)  


The *repository path* could have changed due to a repository rename or other reasons.

If the *repository path* is invalid, you can first remove the App by clicking on the three-dots menu button and selecting **Remove App**:

![](/files/bzqZifI.png)  


Then re-add it back in by clicking on **Add App** and then **Add from GitHub**:

![](/files/CuJcgo1.png)  


If your App has been re-added in correctly you should not see the *Attention Required* status badge anymore.

App Installation ID issue
-------------------------

If the *repository path* is valid, you might be seeing the *Attention Required* badge because of a missing or invalid **App Installation ID**.

This could be due to one of these reasons:

1. The repository visibility has been changed.
2. Repository access has not been granted to Frappe Cloud.
3. Frappe Cloud has not been added as an app.

  


To help us fix this issue you will have to re-install Frappe Cloud as a GitHub app. To do so, follow these steps:

1. Visit the Installed GitHub Apps page ([link](https://github.com/settings/installations)), and click on configure next to Frappe Cloud:![](/files/cckfzkr.png)
2. Ensure that your app is present in the list below if you have not checked **All repositories,** if your app is present then move onto step 3.![](/files/BJgiZQm.png)
3. Uninstall Frappe Cloud:![](/files/C2DqXWK.png)
4. Reinstall it by clicking on **Connect To GitHub** from the apps page on Frappe Cloud:![](/files/N7PHguf.png)
5. Complete the authorization flow:![](/files/TotaLcx.png)
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

![FC Cluster](/files/fc-cluster.png)

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

![Attention Required badge](/files/Screenshot%202022-08-16%20at%2012.36.46%20PM.png)

This means that we are **not able to fetch the latest updates from the associated GitHub repository** for the app. This happens most probably because the Frappe Cloud GitHub app does not have the permission to access the repository. 

Please make sure Frappe Cloud app has proper permissions from GitHub settings:  

![](/files/EDYZBF1.png)

![](/files/sSXn2kA.png)

You can then retry fetching the latest update:  

![Fetch Latest Updates in dropdown](/files/fetch_updates.png)

### Workaround: Attention required even after trying the above

If you're getting the error even after adding and removing the app on Frappe Cloud, please visit <[https://github.com/settings/installations/](https://github.com/settings/installations/)> and then click the configure button next to the **Frappe Cloud** Github App.  

![Configure Frappe Cloud Github](/files/Screenshot%202023-04-04%20at%2023-03-52%20Build%20software%20better%20together.png)

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

![](/files/sXSiPap.png)



You can also see queries that aren't necessary slow, but frequent enough to increase cpu usage from the [Database Analyzer](https://docs.frappe.io/cloud/database-analyzer) tab of your site dashboard:

![](/files/v2VTZt7.png)





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

![](/files/banner-suspension76f79b.png)

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

![Database Storage report](https://user-images.githubusercontent.com/9079960/196618374-5b268f58-b213-458f-8390-8b8beb404cdf.png)

#### Clearing logs

More often than not, log tables can take up a lot of space. You can control size of log tables with: **Log Settings**

![](/files/image62a6b4.png)

You can safely add additional doctypes such as **Deleted Document** to this list. The system will only let you add supported doctypes to this table. If you attempt to add unsupported doctypes, it will throw an error like so:

![](/files/image1dbe27.png)

To allow deletion for your doctypes within your app, implement the staticmethod within your doctype controller like so 

![](/files/image9d54c7.png)

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

![](/files/NmMkuTf.png)

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

![](/files/bXPJqgZ.png)

ref: [https://frappeframework.com/docs/user/en/basics/site_config](https://frappeframework.com/docs/user/en/basics/site_config)

#### Add allow_cors from Site Config tab of your site dashboard

![](/files/image216e0f.png)

### Scheduler not running in my site

At times, it may seem that the scheduled jobs in your site aren't running at the specified time. This could be due to a lot of things. You can check the status of scheduler within your site by going to **RQ Job** doctype.

> For v13 and lower, you can view **Open** **Background Jobs** page for the same.

If scheduler is running, you'll see status like so

![](/files/eob8616.png)

#### Dormant days setting

You should also check **Run Jobs only Daily if Inactive For (Days)** setting within **System Settings** as well. All your scheduled jobs will run once daily regardless of their specified frequency when no user **logs in** to the site in specified number of days.

![](/files/dI3yf6y.png)

### Need 4096 bit https certificate

You may need a 4096 bit tls certificate for some custom app integration. For this, you need to, first, get a custom domain. This is because the certificate for the frappe.cloud or erpnext.com domains are 2048 bit and is shared by all the sites.

Once you add a custom domain, you can raise a ticket asking to make the same 4096 bit. You can download the public certificate for sharing purposes as seen in this SO answer.

### Inbound and Outbound IPs

Often, you may need the IP addresses used by your site for whitelisting or blacklisting reasons.

You can get the same from within your site dashboard under the **Overview** tab.

![](https://frappecloud.com/files/3MWe7ri.png)

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

![](/files/Xgy4bag.png)

Clicking on these will essentially allow you to access the **Backups** tab of your site, from where you can **Restore Backup on another Site** easily

![](/files/wBiX2Ld.png)

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

![](/files/Screenshot%202025-08-20%20at%203.43.37%E2%80%AFPM.png)

### India Compliance credits not correct after restore from backup

After restoring a site from backup, you may notice from your India Compliance account page that the credits shown are not the same as it was on your previous instance. This happens due to a bug. In such case, you can logout and log back in to fix it.

![](/files/Screenshot%202025-08-20%20at%203.40.36%E2%80%AFPM.png)

![](/files/7a1bfec8-75c3-4120-9679-32abb65e060b.jpeg)

### Allow Changing System Timezone within site

You cannot change timezone under system settings once it's set. However, you may change user timezone under user settings. This will convert time in user's timezone when showing it to the user.

### Increasing the database size availability for shared hosting

Currently, Frappe Cloud does not offer à la carte options. To increase your database capacity, you’ll need to upgrade your site to the next available plan. You can view the pricing here.  
Also you can use the Database Analyzer tool to see which tables/doctypes are using the most space within your site itself. More often than not, log tables can take up a lot of space. You can control the size of log tables with: Log Settings.

![](/files/balu-user-timezone.png)

### How do I Deactivate my site ?

The deactivate site feature makes the site inactive and inaccessible on the internet. When deactivated the site enters into maintenance mode and the user will still be billed for the site. Please refer to the below screenshot to deactivate your site.

![](https://docs.frappe.io/files/maintenanc_mode.png)

This action is not very dangerous and can be reverted, but please make sure to verify yourself before Deactivating any site on your account.

![](https://docs.frappe.io/files/deactivation_confirmation.png)

### I am not able to upload large attachments

By default, the file upload limit is 10Mb which can be overridden by setting the `max_file_size` parameter in the Site Config.

Setting `max_file_size` will still not work if you are using Cloudflare Proxy (Orange Cloud) for your Site's domain because Cloudflare blocks large file uploads for free customers. This can be fixed by turning the proxy / orange cloud off in the Domain Records checkbox.

Please check this reference for more details on cloudflare's rate-limiting.

### Rest site to clean state

From your site dashboard > go to Actions > Dangerous Actions > Reset site.

`Note:- This will reset your site's database to clean state`

![](https://docs.frappe.io/files/imageb35d11.png)

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

![Screenshot 2025-01-31 at 1.08.30 PM](/files/Screenshot 2025-01-31 at 1.08.30 PM.png "Screenshot 2025-01-31 at 1.08.30 PM.png")
2. Click on the first option **Connect to your ERPNext Site**.
3. Choose a title for your data source. It can be anything you prefer, then continue.

![Screenshot 2025-01-31 at 12.55.02 PM](/files/Screenshot 2025-01-31 at 12.55.02 PM.png "Screenshot 2025-01-31 at 12.55.02 PM.png")
4. This may take a few minutes. Once it's complete, you will be redirected to insight's dashboard.
5. Open Data Sources and you will be able to see you database's tables.

![Screenshot 2025-01-31 at 12.57.00 PM](/files/Screenshot 2025-01-31 at 12.57.00 PM.png "Screenshot 2025-01-31 at 12.57.00 PM.png")
6. Now you can write query, reports. For more details, check the documentation &lt;https://docs.frappe.io/insights/introduction&gt; .

Second Scenario
---------------

Insights is installed in different site and you need to connect with that.

1. You need to first generate a database user for your site. Follow this [documentation](https://frappecloud.com/docs/database-users-and-permission-manager) to create a read-only user.

  


Typically, it takes a few seconds to configure the database user. Once it's complete, click on **View Credential**

![Screenshot 2025-01-31 at 1.15.44 PM](/files/Screenshot 2025-01-31 at 1.15.44 PM.png "Screenshot 2025-01-31 at 1.15.44 PM.png")
2. Go to insights setup page &gt; &lt;https://test.com/insights/setup&gt;

![Screenshot 2025-01-31 at 1.08.45 PM](/files/Screenshot 2025-01-31 at 1.08.45 PM.png "Screenshot 2025-01-31 at 1.08.45 PM.png")  


**Note :** If you have already completed setup and this page is not appearing to you, go to &lt;https://test.com/insights&gt; and click on **Connect Data Source**.
3. Click on **MariaDB** and continue.
4. Fill in the required information and make sure to check the **Use SSL** checkbox.

![Screenshot 2025-01-31 at 1.26.50 PM](/files/Screenshot 2025-01-31 at 1.26.50 PM.png "Screenshot 2025-01-31 at 1.26.50 PM.png")
5. Click on **Connect**
6. Once connection verified, click on **Continue** button.
7. This may take a few minutes. Once it's complete, you will be redirected to insights dashboard.
8. Open Data Sources and you will be able to see you database's tables.

![Screenshot 2025-01-31 at 12.57.00 PM](/files/Screenshot 2025-01-31 at 12.57.00 PM.png "Screenshot 2025-01-31 at 12.57.00 PM.png")
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

![](/files/regional-coa.png)

Also, you can have Chart of Accounts setup via your custom application, which will include tax ledgers.

## Sales, Purchase and Item Tax Templates

To make applying taxes easier in transactions, ERPNext allows you to set up Tax Templates for sales and purchases. This helps new users correctly apply taxes to invoices to ensure they are compliant.

![](/files/regional-tax-masters.png)

In cases where an invoice contains multiple items with different tax rates, an Item Tax Template should be auto-created. For instance, in India, there are GST slabs of 5%, 12%, 18%, and 28%. Since a single sales invoice can have items from different slabs, the tax must be defined at the item level.

## Regional Tax Setting

The final goal for tax ledgers is to provide reports as specified by the tax authorities. While tax ledgers are created in the Chart of Accounts, the system needs a setting to identify which ledger corresponds to which tax type. The India Compliance app, for example, has a GST Setting page for this.

![](/files/regional-compliance-tax-setup.png)

This settings page can also store other country-specific configurations, such as API details for e-invoicing integrations.

![](/files/regional-compliance-setup.png)

## Workspace for Regional Taxation

Your regional compliance app will include several DocTypes, such as:

- Setting page (for tax ledgers and integration details with the system of tax authorities)
- Additional masters and transactions are required for creating compliant invoices
- Link of Reports
- Link of User manual and help videos

![](/files/regional-links.png)

Do create a Workspace or sub-workspace that lists all these DocTypes, pages, and reports, grouped logically. This makes it easy for new users to find compliance features and helpful resources.

## Onboarding Help

You can create a step-by-step onboarding guide to help users set up the app. For reference, you can look at the onboarding flow in the Thai Taxation app.

![](/files/regional-onboarding.png)

## Reports

The success of a regional compliance app depends on providing accurate reports in the exact format and with the names specified by the tax authorities. It is extremely important to build these reports correctly. They should be grouped within the app's workspace based on their importance.

![](/files/compliance-reports.png)

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

![image6357ec](/files/image6357ec.png)

This list should tell you about the target resource or resources, reason for the request, time for expiry and when was it requested. The list is sorted by last updated. So most relevant requests will be kept on top.

Clicking any row will open a dialog with more details. It can show a list of resources and any additional permissions if requested.

![image17afbf](/files/image17afbf.png)

Pending requests can be accepted or rejected. Once accepted, access will be granted for a limited amount of time. This includes any additional permissions mentioned in the request.

Already accepted requests can be revoked. This will instantly remove the agent’s access to mentioned resource. Please note that when there are multiple accepted requests against a common resource, all of them will have to be revoked for complete denial of access.

You will get a email and in-app notification when an agent requests access for one of your resources. You will also be notified when there are any updates on said request.

That’s it! There is nothing else you have to do. Your data will remain secure and untouched by anyone other than you!

### What should I as an agent do?
You are on the other side of this see-saw. Your role as an agent is to request access to a particular resource. There is no special page to do this. Instead, you can go a resource’s page and click on Request Access button. This will open a dialog asking for necessary information.

![image4c3a4a](/files/image4c3a4a.png)

Ideally, you should ask for minimum required permissions depending on the need. More permissions can be asked later.

You will get email and in-app notifications whenever there is an update on the request. If the customer accepted your request, you can access the resource. All requests sent from your team can be tracked anytime in Access Requests page. This is the same page as customer, except you can see outgoing requests as well.

Clicking any of the rows will open up a dialog with it’s details. Like customer’s ability to revoke an accepted request, you can forfeit an accepted request. This will ensure you don’t keep access to a certain resource even after the issue is solved. Customer will get a notification regarding the same.

In addition to Access Requests page, you can see individual resource statuses in their own page. If you have access via request for a resource, a button with unlock icon will be shown on the top bar. This button opens a dialog with relevant permissions and dates. There is also an additional button to re-request access with or without permissions.

![image277c18](/files/image277c18.png)

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
**![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcoObKj79cLk85P5mYHY7Qx8YKTBMVgyXF6x1KFdWEMFbvtfPzswWs4fXkgQNj0AfyueLfToZAs0NbtLM2gRYPP2UmNCZ0RUrSW87r66TvanbYzmtRrWNp_r8r3ym2GUeMWBk5Av3-QYv8NK8HRJmVkibM?key=rRX4NjLc9xksOOZOmvo7iQ)**  
  
Select the appropriate plan you want to change your site to and click on the change plan button to change your site plan to the newly selected one.**![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcZC4TImcI60Or59EyJh8DuFv8tsrmY2O4gXG3J3yx9RxiDriyKZVQcQoTIomJL_AUqBeXe_8ogOAjOpRCJ3ReSh5oIA7zWeLrvq5RWZ5HddbgQ0bdHm4IuuNCdpcv8K14Ofy6rHFZBfsUJVN_hGZul6PvE?key=rRX4NjLc9xksOOZOmvo7iQ)**  

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

**1.** From your site’s dashboard click on the Update button.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPfVM3BldiLYJRE7hDz7zq9rX6HNv7mF-RaS-_b3e6jYb71CwuMcPx73FqeNdB4A6TBZ0K5tUpPvhbcL_2bWdelUVIe9YmqkP8ymLrnRqldjOXWVITt_JWLPPRtgyiTSiKNXiLEGR0wlRtHe6dTg5zbTg?key=CiJyoIIvFgjiTDtchgP-BQ)  
  
**2.** Click on the “**Configure**” button.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcwr2K1iA7FTgVoh4DD5XaIT4OMiX6ncBk7DV7uaQ6wQH0CokP3YN4hYdfjVcifi94qXXG59nBSxOoeXjR1itknT7wXA8P8WOLBzStI-pJRwQ4eZuCrfO863gBSET4y0qcufwosmosKEvfqrW2gPPNwue0q?key=CiJyoIIvFgjiTDtchgP-BQ)  
  
**3.** Once you click on the Configure button you will see a pop-up, you can toggle On/Off the “Enable Auto Update” option.  
  
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPHeo4m-0VhkQ8oMh13FPeemYczVENNmIb0f1NQOe2pqNiFuEwtJwQoErL5StGm7wVtoRrwIW7Xdrja53kjyTwgtu7MhhfjvxQZtVurQq8Vr53NXfqqzN23r8YC18LoKDrMMWT2vP3cJ_aKG_jBF-Xuw5u?key=CiJyoIIvFgjiTDtchgP-BQ)  


  

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

Go to the Apps tab from your Frappe Cloud dashboard.![](/files/2ZmfimM.png)  
  


Click on the three dots of the app you want to uninstall from your site.![](/files/2CxpKvg.png)  
  


From the drop-down select uninstall.![](/files/moQ6fvZ.png)  

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

![](/files/cB5BL8z.png)  


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

![](/files/RPsrZjb.png)  


Enable the **Use in place update** checkbox. The action button will now say **Update site in place** instead of **Deploy and update site**.

Once you click the **Update site in place** button, you will be redirected to the update job:

![](/files/ThE8xUs.png)  



> ℹ️ **Info**
> 
> If the Update Bench In Place job fails, Frappe Cloud will try to recover your bench by running the Recover Update In Place job:
> 
> ![](/files/i9rbFzl.png)  
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
