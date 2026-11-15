<!-- Frappe documentation: cloud, part 1 of 9. Index: docs/INDEX.md -->

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

  


  
