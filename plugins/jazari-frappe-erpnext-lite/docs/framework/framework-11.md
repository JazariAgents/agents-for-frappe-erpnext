<!-- Frappe documentation: framework, part 11 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__bench__frappe-commands.md -->
---
title: "Frappe Commands"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/frappe-commands"
updated: "2026-02-17"
---

The Bench CLI utilizes the module`frappe.utils.bench_manager` to get the framework's as well as any other Application's commands present on the current bench directory.

This page is concerned only with the commands that exist in the Frappe project, that are a direct part of the CLI tool. These commands are defined under the [frappe/frappe](https://github.com/frappe/frappe).


> For references of any Bench commands, checkout [Bench Commands](/framework/v14/user/en/bench/bench-commands).
> 
> 

There are four major command types in Frappe inherited by Bench during command executions. They can be broadly grouped into

### Site Commands

Set of commands used for site-specific operations. These are the most frequented commands to alter the state of your sites. These commands are accessed by using the `--site` option along with the site name (or "all") if you wish to run the operation *(if possible)* for all sites on the bench. These commands are defined under the module `frappe.commands.site`.

#### Site Creation

Create a new Site on your bench. By default, all sites created on your bench will have only the Frappe Framework installed on them.


```
bench new-site {site}
  

```
For more information and examples, see the [bench new-site](/framework/v14/user/en/bench/reference/new-site) reference.

#### Site Backups

You can use the Bench CLI to take backups on the sites of your bench. You can manage the site's database and files backups and have more control over the operation.


```
bench --site {site} backup
  

```
The Bench CLI also deletes the older backup files from your bench directory. By default, it deletes backups older than 24 hours from the backups directory.

For more information and examples, see the [bench backup](/framework/v14/user/en/bench/reference/backup) reference.

#### Site Restores

Bench CLI can be used to restore an existing site to a previous state. Using the `bench restore` command, a site may be restored with the specific database and file restores.


```
bench --site {site} restore {path/to/database/file}
  

```
The least requirement for performing a restore operation is having the database file on your local filesystem. The specified backup file may have the `sql.gz` of `sql` extension.

For more information and examples, see the [bench restore](/framework/v14/user/en/bench/reference/restore) reference.

#### Partial Site Restores and Backups

Since Version 13, Frappe has support for taking partial backups and restoring them. Partial backups can be taken using the `bench backup` command directly. As for partial restores, the `bench partial-restore` command may be used to restore the partial backups to an existing site.

For more information and examples, see the [bench partial-restore](/framework/v14/user/en/bench/reference/partial-restore) and [bench backup](/framework/v14/user/en/bench/reference/backup) reference.

#### Site App Management

You can install or uninstall Frappe Applications available on your Bench. To add Apps to your bench using `bench get-app` checkout [the docs](/framework/v14/user/en/bench/bench-commands#frequently-used).

##### App Installation

The easiest way to install a Frappe Application on your site is through the Bench CLI. However, the application must be installed on your bench prior to that.


```
bench --site {site} install-app {app}
  

```
In this operation, Application `meta`, `modules` and `doctypes` of the specified site are installed on the specified site.

##### App Uninstallation

Uninstall an app installed on site. This is a destructive action and consists of removing all app-related data from the site. Hence, a backup is taken before uninstalling said app.


```
bench --site {site} uninstall-app {app}
  

```

> Note: From Version 13, even apps not installed on the Bench can be uninstalled from the site.
> 
> 

For more information and examples, see the [bench uninstall-app](/framework/v14/user/en/bench/reference/uninstall-app) reference.

#### Site Migrations

Run patches, sync schema and rebuild files, translations and indexes on a particular site. Find out how site migrations work in [the docs](/framework/v14/user/en/database-migrations).


```
bench --site {site} migrate
  

```
For more information and examples, see the [bench migrate](/framework/v14/user/en/bench/reference/migrate) reference.

#### Site Deletion

Drops the database and moves the site directory from `./sites` to the `./archived_sites` *(unless specified otherwise)* folder on your Bench.


```
bench drop-site {site}
  

```
For more information and examples, see the [bench drop-site](/framework/v14/user/en/bench/reference/drop-site) reference.

#### Reset Site Data

Re-install all installed Applications from your specified site. This completely resets the site.


```
bench reinstall {site}
  

```
For more information and examples, see the [bench reinstall](/framework/v14/user/en/bench/reference/reinstall) reference.

#### List Installed Apps

List all the Frappe Applications installed on the specified site. The information shown by the command is fetched from the **Installed Applications** DocType which tracks the latest version of the apps, the site was migrated to. The global default `installed_apps` is used as fallback.


```
bench --site {site} list-apps
  

```
Multi-site support has been added in Version 13. To see the summary for all sites, run the command with site's value as `all`.

For more information and examples, see the [bench list-apps](/framework/v14/user/en/bench/reference/list-apps) reference.

#### Setting the default site

Sometimes typing `--site [sitename]` for every site command can be tedious. You can set the default site for the terminal session by setting the `FRAPPE_SITE` environment variable.


```
~/frappe-bench
❯ export FRAPPE_SITE=mysite.localhost

~/frappe-bench
❯ echo $FRAPPE_SITE
mysite.localhost

~/frappe-bench
❯ bench console
Apps in this namespace:
frappe

In [1]: frappe.local.site
Out[1]: 'mysite.localhost'
  

```
#### Access site in the browser

To access a site in the browser, you have to remember the webserver port on which bench is running and then type out the full URL. There is a bench command that does this for you.

Running the following command will open the site url directly in your default browser.


```
# open site.local in the browser
$ bench --site site.local browse

# this also works
$ bench browse site.local
  

```
You can also login as a user by passing `--user` option.


```
$ bench --site site.local browse --user test@example.com

$ bench --site site.local browse --user Administrator
Login URL: http://site.local:8000/app?sid=<generated-sid>
  

```

> Note that this command:
> 
> * Allows login as any user only when developer_mode is set to 1
> * Allows login as Administrator regardless of developer_mode
> * Prints the login URL only when user is Administrator
> 

#### Site Operations, Debugging and Development

Here are some operations you can perform on your site via the Bench CLI to update your site state. You may never have to use some of these, but they exist just in case.

* **add-system-manager**: Add a new system manager to a site.
* **add-user**: Add a new User with specific roles to a site.
* **add-to-hosts**: Add the specified site to the hosts file on your system.
* **build-search-index**: Builds search index for Websites. Refer to [Full Text Search API Docs](/framework/v14/user/en/api/full-text-search) for more information.
* **disable-user**: Disable user on site.
* **publish-realtime**: Publish realtime event from bench.
* **reload-doc**: Reload schema for a particular *Doctype* and refresh the specified *Document*
* **reload-doctype**: Reload schema for a particular *DocType*
* **remove-from-installed-apps**: Removes the mentioned app from the site global value of `installed_applications`.
* **run-patch**: Run a particular patch via the Frappe Patch Handler.
    - **execute:** This allows to run one-off Python statements
    ```
        bench --site erpnext.site run-patch 'execute:frappe.db.set_value("User", frappe.session.user, "default_app", "frappe")'
    ```
* **migrate-to**: Command to migrate your local site to a Frappe Hosting Provider's service.
* **ngrok**: Create a temporary URL and share it with anyone, and they can access your local site in their browser. Primarily built for aiding with the development of third party services.
* **set-password**: Set the password for any user.
* **set-admin-password**: Set the password for the Administrator user.
* **set-last-active-for-user**: Set users last active date to current datetime.
* **start-recording**: Starts the Frappe Recorder for the specified sites.
* **stop-recording**: Terminates the Frappe Recorder for the specified sites.
* **use**: Sets the default site on the bench.

### Database Maintenance Commands

Set of commands that are related to database management and maintenance. These commands offer more control to your site's database. You may want to fine-tune your deployment to fit your site's needs over time.

#### Table Transformations

The `transform-database` command allows you to manage the settings of your site's tables. At this point, you can switch `engine` and `row_format` settings for select tables on your site database.


```
bench --site {site} transform-database --tables {tables}
  

```
For more information and examples, see the [bench transform-database](/framework/v14/user/en/bench/reference/transform-database) reference.

#### Table Trimming

Docfields removed from a particular DocType may not be deleted from their Database tables. This is by design to prevent premature data loss in Frappe. This won't be problematic for the most part, however, at some point you may face issues due to this lingering data.

Some benefits of regular table trimming are:

* Smaller backup sizes
* Reduced time taken to backup sites
* Reduced Site Database Usages
* Optimized queries in case of `SELECT *`
* Database is clean and doesn't have anything hidden or redundant data


```
bench trim-tables [OPTIONS]
  

```
For more information and examples, see the [bench trim-tables](/framework/v14/user/en/bench/reference/trim-tables) reference.

#### Database Trimming

Deleting DocTypes from the list view may not delete their corresponding tables from the database. Migrations may leave ghost tables in your Site Database at times. This may be done for the sake of redundancy, for recovery in case your data is corrupted or lost, or simply, in cases of human error.


```
bench trim-database [OPTIONS]
  

```
For more information and examples, see the [bench trim-database](/framework/v14/user/en/bench/reference/trim-database) reference.

### Scheduler Commands

Commands to manage and review the scheduler and background jobs' statuses for the sites on your bench. Defined under module `frappe.commands.schedule`.

* **disable-scheduler**: Disable scheduler for specified sites.
* **doctor**: Get diagnostic info about the status of the scheduler for all sites (if unspecified) and active workers on bench.
* **enable-scheduler**: Enables scheduler for specified sites.
* **purge-jobs**: Purge any pending periodic tasks, if the event option is not given, it will purge everything for the site.
* **ready-for-migration**: Checks if a particular site is ready for migration by checking the existence of any pending background jobs.
* **scheduler**: Change the state of the scheduler for any site from *pause*, *resume*, *disable* or *enable* state.
* **set-maintenance-mode**: Set the value for maintenance mode in the config for specified sites.
* **show-pending-jobs**: Get diagnostic info about background jobs.
* **schedule**: Start the scheduler process for your bench. This process manages scheduler events defined in the `hooks.py` file. You can find this command mentioned in the bench config for your process manager too.
* **worker**: Start worker process on your bench. The process this starts will manage all background jobs started on this bench.
* **trigger-scheduler-event**: Trigger a specific scheduler event for the specified sites.

### Frappe Utility Commands

Frappe Utility commands that can be both, site or bench specific. These commands are defined under the module `frappe.commands.utils`.

#### Displaying Site Config

The applied configuration for your sites gets applied as a combination of the bench directory's `common_site_config.json` and the site's own `site_config.json`. You can read more about this, [here](/framework/v14/user/en/basics/site_config). Bench provides an interface to view the applied `frappe.conf` values for your sites. You may choose to access this information in tabular or JSON formats.


```
bench --site {site} show-config
  

```
For more information and examples, see the [bench show-config](/framework/v14/user/en/bench/reference/show-config) reference.

#### Updating Site Config

Bench provides a wrapper command to insert or update values in the site config files. You can update values in your site's `site_config.json`, along with the bench directory's `common_site_config.json` through the same command.


```
bench --site {site} set-config KEY VALUE
  

```
For more information and examples, see the [bench set-config](/framework/v14/user/en/bench/reference/set-config) reference.

#### Display Version Of Installed Apps

The `version` command displays all installed apps and their versions.


```
bench version [OPTIONS]
  

```
With version 13, the `-f` / `--format` option was introduced. This option allows you to display additional information about the branch and last commit. For more information and examples, see the [bench version](/framework/v14/user/en/bench/reference/bench-version) reference.

#### More Commands

* **add-to-email-queue**: Add an email to the Email Queue.
* **build**: Builds assets for the Frappe Applications installed on bench.
* **bulk-rename**: Rename multiple records via a CSV file. *Example File Format (Without Header)*:



| Old Name | New Name | Merge |
| --- | --- | --- |
| HR-EMP-00001 | EMP0001 | FALSE |
| HR-EMP-00002 | EMP0002 | FALSE |
| HR-EMP-00003 | EMP0003 | FALSE |
| HR-EMP-00004 | EMP0004 | FALSE |
| HR-EMP-00005 | EMP0005 | FALSE |
| HR-EMP-00006 | EMP0006 | FALSE |

* **clear-cache**: Clear cache, doctype cache and defaults.
* **clear-website-cache**: Clear Website cache.
* **console**: Starts an IPython console for the site. Use with the `--autoreload` flag to reload changes to code automatically.
* **data-import**: Import documents in bulk from CSV or XLSX using data import.
* **destroy-all-sessions**: Clear sessions of all users (logs them out).
* **execute**: Execute a particular function or method with a given set of `args` and `kwargs`.
* **export-csv**: Export data import template with data for DocType.
* **export-doc**: Export a single document to CSV.
* **export-fixtures**: Export records from a site to your Frappe Application, as JSON files. Fixtures are defined in your app's `hooks.py` file.
* **export-json**: Export doclist as json to the given path, use '-' as name for Singles.
* **import-csv**: Import from your CSV file using data import.
* **import-doc**: Import (insert/update) doclist. If the argument is a directory, all files ending with `.json` are imported
* **jupyter**: Starting a Jupyter Notebook server.
* **make-app**: Creates a boilerplate Frappe Application.
* **db-console**: Start the interactive DB console for your site. This command is an alias over commands: mariadb, postgres
* **mariadb**: Start the MySQL interactive console for the mysql site.
* **postgres**: Start the PostgreSQL interactive console for the postgres site.
* **rebuild-global-search**: Setup help table in the current site (called after migrate).
* **request**: Make a request as Administrator with Arguements to a Path.
* **reset-perms**: Reset permissions for all DocTypes to their default settings.
* **run-tests**: Run Python tests on the specified site.
* **run-parallel-tests**: Run Python tests parallelly on CI.
* **run-ui-tests**: Run Cypress UI tests.
* **serve**: Start the webserver for the bench.
* **watch**: Watch and concatenate JS and CSS files as and when they change.

### Translation Commands

There are two ways to manage translations. Until v15, translations are commonly based on CSV files. Starting from v16, frappe manages translations using the .po file format from GNU Gettext. Custom apps can either continue to provide CSV based translations or switch to the new format.

#### CSV Files

Set of commands to manage CSV based translation files. These commands are defined under the module `frappe.commands.translate`.

* **build-message-files**: Build message files for translation.
* **get-untranslated**: Get untranslated strings for language.
* **migrate-translations**: Migrate target-app-specific translations from source-app to target-app
* **new-language**: Create a `[lang].csv` file for the given application.
* **update-translations**: Update translations for set language between files.

#### Gettext / PO files

Set of commands to manage Gettext based translation files. These commands are defined under the module `frappe.commands.gettext`.

* **generate-pot-file**: Generate a POT file. This is creates the base file that contains all the translatable strings of your app and serves a a template for translation files for specific languages.
* **compile-po-to-mo**: Compile PO files to MO files. PO files are human-readable. In production, translations are read from MO files, where the translations are complied to an optimized binary format. This command creates MO files from your PO files (this command also triggered by **bench build**, for convenience).
* **migrate-csv-to-po**: Migrate your app's translations from CSV files (old) to PO files (new). Please run **generate-pot-file** first.
* **update-po-files**: Sync the language's PO files with POT file. This way, new translatable strings are added to your PO file, where they can be translated, while outdated ones can removed. You might want to run **generate-pot-file** first.
* **create-po-file**: Create a new (untranslated) PO file for a new language.

<!-- page: framework/framework__user__en__bench__guides__adding-custom-domains.md -->
---
title: "Adding Custom Domains to your Site"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/adding-custom-domains"
updated: "2026-02-17"
---


You can add **multiple custom domains** for your site, just run:

 bench setup add-domain [desired-domain]

On running the command you will be asked for which site you want to set the custom domain for.

You can also setup SSL for your custom domain by using the options:
```
 --ssl-certificate [path-to-certificate]
 --ssl-certificate-key [path-to-certificate-key]
```
Example:
```
 bench setup add-domain custom.erpnext.com --ssl-certificate /etc/letsencrypt/live/erpnext.cert --ssl-certificate-key /etc/letsencrypt/live/erpnext.key
```
Domain configuration is stored in the respective site's site_config.json
```
 "domains": [
 {
 "ssl_certificate": "/etc/letsencrypt/live/erpnext.cert",
 "domain": "erpnext.com",
 "ssl_certificate_key": "/etc/letsencrypt/live/erpnext.key"
 }
 ],
```
**You will need to regenerate the nginx configuration by runnning `bench setup nginx` and reload the nginx service by running `sudo service nginx reload` to put your custom domain in effect**

<!-- page: framework/framework__user__en__bench__guides__configuring-https.md -->
---
title: "Configuring HTTPS\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/configuring-https"
updated: "2026-02-17"
---


### Get the required files

You can get a SSL certificate from a trusted Certificate Authority or generate your own. For self signed certificates the browser will show a warning that the certificate is not trusted. [Here's a tutorial for using Let's Encrypt to get a free SSL Certificate](lets-encrypt-ssl-setup.html)

The files required are

* Certificate (usually with extension .crt)
* Decrypted private key

### Prequisites

1. You need to have a [DNS Multitenant Setup](https://frappe.io/docs/v14/user/en/bench/guides/setup-multitenancy)
2. Your site should be accessible via a valid domain
3. You need root permissions on your server
4. You need a valid certificate generated through a trusted Certificate Authority or a Self-Signed Certificate.

To generate .crt from private authority, generally you would have to generate a CSR (Certificate Signing Request). You may skip this step if you already have a certificate (.crt) file. To generate a CSR and the corresponding key file, run the following command:

 openssl req -new -newkey rsa:2048 -nodes -keyout mydomain.com.key -out mydomain.com.csr

You need to upload this CSR (.csr) file to the private certificate authority (eg. GoDaddy, ComodoSSL) to generate a valid certificate (.crt) file against it.

If you have multiple certificates (primary and intermediate), you will have to concatenate them. For example:

 cat your_certificate.crt CA.crt >> certificate_bundle.crt

Also make sure that your private key is readable only by the root user:

 chown root private.key
 chmod 600 private.key

### Move the two files to an appropriate location

 mkdir /etc/nginx/conf.d/ssl
 mv private.key /etc/nginx/conf.d/ssl/private.key
 mv certificate_bundle.crt /etc/nginx/conf.d/ssl/certificate_bundle.crt

### Setup nginx config

Set the paths to the certificate and private key for your site

 bench set-ssl-certificate site1.local /etc/nginx/conf.d/ssl/certificate_bundle.crt
 bench set-ssl-key site1.local /etc/nginx/conf.d/ssl/private.key

### Generate nginx config

 bench setup nginx

### Reload nginx

 sudo service nginx reload

or

 systemctl reload nginx # for CentOS 7

Now that you have configured SSL, all HTTP traffic will be redirected to HTTPS

<!-- page: framework/framework__user__en__bench__guides__diagnosing-the-scheduler.md -->
---
title: "Diagnosing The Scheduler\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/diagnosing-the-scheduler"
updated: "2026-02-17"
---

If you're experiencing delays in scheduled jobs or they don't seem to run, you can run the several commands to diagnose the issue.

### bench doctor

This will output the following in order:
- Scheduler Status per site
- Number of Workers
- Pending Tasks


Desirable output:

 Workers online: 0
 -----None Jobs-----

### bench --site [site-name] show-pending-jobs

This will output the following in order:
- Queue
- Tasks within Queue

Desirable output:

 -----Pending Jobs-----


### bench purge-jobs

This will remove all pending jobs from all queues

<!-- page: framework/framework__user__en__bench__guides__lets-encrypt-ssl-setup.md -->
---
title: "Using Let's Encrypt to setup HTTPS\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/lets-encrypt-ssl-setup"
updated: "2026-02-17"
---


## Prerequisites

1. You need to have a [DNS Multitenant Setup](https://frappe.io/docs/v14/user/en/bench/guides/setup-multitenancy)
2. Your site should be accessible via a valid domain
3. You need root permissions on your server

**Note : Let's Encrypt Certificates expire every three months**

## Using Bench Command

Just run:

 sudo -H bench setup lets-encrypt [site-name]

You will be faced with several prompts, respond to them accordingly. This command will also add an entry to the crontab of the root user *(this requires elevated permissions)*, that will attempt to renew the certificate every month.

### Custom Domains

You can setup Let's Encrypt for [custom domains](adding-custom-domains.html) as well. Just use the `--custom-domain` option

 sudo -H bench setup lets-encrypt [site-name] --custom-domain [custom-domain]

### Renew Certificates

To renew certificates manually you can use:

 sudo bench renew-lets-encrypt



---



## Manual Method
### Download the appropriate Certbot-auto script into /opt

 https://certbot.eff.org/

### Stop nginx service

 $ sudo service nginx stop

### Run Certbot

 $ ./opt/certbot-auto certonly --standalone

After letsencrypt initializes, you will be prompted for some information. This exact prompts may vary depending on if you've used Let's Encrypt before, but we'll step you through the first time.

At the prompt, enter an email address that will be used for notices and lost key recovery:

[Screenshot on the live page]

Then you must agree to the Let's Encrypt Subscribe Agreement. Select Agree:

[Screenshot on the live page]

Then enter your domain name(s). Note that if you want a single cert to work with multiple domain names (e.g. example.com and www.example.com), be sure to include all of them:

[Screenshot on the live page]

### Certificate Files

After obtaining the cert, you will have the following PEM-encoded files:

* **cert.pem**: Your domain's certificate
* **chain.pem**: The Let's Encrypt chain certificate
* **fullchain.pem**: cert.pem and chain.pem combined
* **privkey.pem**: Your certificate's private key


These certificates are stored under `/etc/letsencrypt/live/example.com` folder

### Configure the certificates for your site(s)

Go to your erpnext sites site_config.json

 $ cd frappe-bench/sites/{{site_name}}

Add the following two lines to your site_config.json

 "ssl_certificate": "/etc/letsencrypt/live/example.com/fullchain.pem",
 "ssl_certificate_key": "/etc/letsencrypt/live/example.com/privkey.pem"


Regenerate the nginx configuration

 $ bench setup nginx

Restart the nginx server

 $ sudo service nginx restart

---

### Auto renewal (experimental)

Login as root or a user with superuser privileges, run `crontab -e` and enter:


 # renew letsencrypt certificates on 1st monday of every month and get an email if it gets executed
 MAILTO="mail@example.com"
 0 0 1-7 * * [ "$(date '+\%a')" = "Mon" ] && sudo service nginx stop && /opt/certbot-auto renew && sudo service nginx start

<!-- page: framework/framework__user__en__bench__guides__settings-limits.md -->
---
title: "Setting Limits for your Site\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/settings-limits"
updated: "2026-02-17"
---


> Note: This feature has been deprecated since Version 12

Frappe v7 has added support for setting limits and restrictions for your site.
These restrictions are set in the `site_config.json` file inside the site's folder.

 {
 "db_name": "xxxxxxxxxx",
 "db_password": "xxxxxxxxxxxx",
 "limits": {
 "emails": 1500,
 "space": 0.157,
 "expiry": "2016-07-25",
 "users": 1
 }
 }

You can set a limit by running:

 bench --site [sitename] set-limit [limit] [value]

You can set multiple limits at the same time, by running

 bench --site [sitename] set-limits --limit [limit] [value] --limit [limit-2] [value-2]

The valid limits you can set are:

- **users** - Limit on the number of maximum users for a site
- **emails** - Limit on the number of emails sent per month from the site
- **space** - Limit on the maximum space the site can use (GB)
- **email_group** - Limit on the maximum number of members allowed in an Email Group
- **expiry** - Expiry date for the site (YYYY-MM-DD within quotes)

Example:

 bench --site site1.local set-limit users 5

You can check your usage by opening the "Usage Info" page from the toolbar / AwesomeBar. A limit will only show up on the page if it has been set.

[Screenshot on the live page: Doctype Saved]

<!-- page: framework/framework__user__en__bench__guides__setup-multitenancy.md -->
---
title: "Setup Multitenancy\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/setup-multitenancy"
updated: "2026-02-17"
---


Assuming that you've already got your first site running and you've performed
the [production deployment steps](setup-production.html), this section explains how to host your second
site (and more). Your first site is automatically set as default site. You can
change it with the command,

 bench use sitename




Port based multitenancy
-----------------------

You can create a new site and make run it on a different port (while the first
one runs on port 80).

* Switch off DNS based multitenancy (once)

 `bench config dns_multitenant off`

* Create a new site

 `bench new-site site2name`

* Set port

 `bench set-nginx-port site2name 82`

* Re generate nginx config

 `bench setup nginx`

* Reload nginx

 `sudo service nginx reload`


DNS based multitenancy
----------------------

You can name your sites as the hostnames that would resolve to it. Thus, all the sites you add to the bench would run on the same port and will be automatically selected based on the hostname.

To make a new site under DNS based multitenancy, perform the following steps.

* Switch on DNS based multitenancy (once)

 `bench config dns_multitenant on`

* Create a new site

 `bench new-site site2name`

* Re generate nginx config

 `bench setup nginx`

* Reload nginx

 `sudo service nginx reload`

<!-- page: framework/framework__user__en__bench__guides__setup-production.md -->
---
title: "Setup Production"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/guides/setup-production"
updated: "2026-05-10"
---


&gt; **WARNING:** We DO NOT recommend installing on bare metal servers. Recommend way of setting up production sites is using docker images. You can find instructions here: &lt;https://github.com/frappe/frappe#installation&gt;
&gt; 
&gt; 

You can setup the bench for production use by configuring two programs, Supervisor and nginx. If you want to revert your Production Setup to Development Setup refer to [these commands](https://github.com/frappe/bench/wiki/Stopping-Production-and-starting-Development)

#### Easy Production Setup

These steps are automated if you run `sudo bench setup production`

#### Manual Production Setup

Supervisor
----------

Supervisor makes sure that the process that power the Frappe system keep running and it restarts them if they happen to crash. You can generate the required configuration for supervisor using the command `bench setup supervisor`. The configuration will be available in `config/supervisor.conf` directory. You can then copy/link this file to the supervisor config directory and reload it for it to take effect.

eg,


```
bench setup supervisor
sudo ln -s `pwd`/config/supervisor.conf /etc/supervisor/conf.d/frappe-bench.conf

```
Note:

* Use `--skip-redis` option if you do not need to generate config to start redis servers. e.g. `bench setup supervisor --skip-redis`
* For CentOS 7, the extension should be `ini`, thus the command becomes


```
bench setup supervisor
sudo ln -s `pwd`/config/supervisor.conf /etc/supervisor/conf.d/frappe-bench.ini #for CentOS 7 only

```
The bench will also need to restart the processes managed by supervisor when you update the apps. To automate this, you will have to setup sudoers using the command, `sudo bench setup sudoers $(whoami)`.

Nginx
-----

Nginx is a web server and we use it to serve static files and proxy rest of the requests to frappe. You can generate the required configuration for nginx using the command `bench setup nginx`. The configuration will be available in `config/nginx.conf` file. You can then copy/link this file to the nginx config directory and reload it for it to take effect.

eg,


```
bench setup nginx
sudo ln -s `pwd`/config/nginx.conf /etc/nginx/conf.d/frappe-bench.conf

```
Note: When you restart nginx after the configuration change, it might fail if you have another configuration with server block as default for port 80 (in most cases for the nginx welcome page). You will have to disable this config. Most probable places for it to exist are `/etc/nginx/conf.d/default.conf` and `/etc/nginx/conf.d/default`. In the latest nginx installs, the file is in `/etc/nginx/sites-available/default`

<!-- page: framework/framework__user__en__bench__reference.md -->
---
title: "Commands Reference"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference"
updated: "2026-02-17"
---

Manual for the commands under Frappe & Bench, accessible via the Bench CLI.

## Site Commands

1. [new-site](/framework/v14/user/en/bench/reference/new-site)
2. [drop-site](/framework/v14/user/en/bench/reference/drop-site)
3. [migrate](/framework/v14/user/en/bench/reference/migrate)
4. [backup](/framework/v14/user/en/bench/reference/backup)
5. [reinstall](/framework/v14/user/en/bench/reference/reinstall)
6. [list-apps](/framework/v14/user/en/bench/reference/list-apps)
7. [install-app](/framework/v14/user/en/bench/bench-commands#install-apps)
8. [uninstall-app](/framework/v14/user/en/bench/reference/uninstall-app)
9. [show-config](/framework/v14/user/en/bench/reference/show-config)
10. [set-config](/framework/v14/user/en/bench/reference/set-config)
11. [restore](/framework/v14/user/en/bench/reference/restore)
12. [partial-restore](/framework/v14/user/en/bench/reference/partial-restore)

## Frappe Utility Commands

1. [version](/framework/v14/user/en/bench/reference/bench-version)

## Database Maintenance Commands

1. [transform-database](/framework/v14/user/en/bench/reference/transform-database)
2. [trim-database](/framework/v14/user/en/bench/reference/trim-database)
3. [trim-tables](/framework/v14/user/en/bench/reference/trim-tables)

## Translation management

1. [generate-pot-file](https://frappeframework.com/docs/user/en/bench-generate-pot-file)
2. [migrate-csv-to-po](https://frappeframework.com/docs/user/en/bench-migrate-csv-to-po)
3. [update-po-files](https://frappeframework.com/docs/user/en/bench-update-po-files)
4. [compile-po-to-mo](https://frappeframework.com/docs/user/en/bench-compile-po-to-mo)

<!-- page: framework/framework__user__en__bench__reference__backup.md -->
---
title: "bench backup"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/backup"
updated: "2026-02-17"
---

Usage
-----


```
bench backup [OPTIONS]
```
Description
-----------

Backup sites specified. Executing the vanilla command will create a database dump, compress it and save the data under the default backup location `./sites/{site}/private/backups`.

In case a current site is set, simply running `bench backup` command will backup that site.

Options
-------

* `--backup-path` Set path for saving all the files in this operation
* `--backup-path-db` Set path for saving database file
* `--backup-path-conf` Set path for saving config file
* `--backup-path-files` Set path for saving public file
* `--backup-path-private-files` Set path for saving private file
* `--exclude`, `-e` Specify the DocTypes to not backup seperated by commas
* `--only`, `--include`, `-i` Specify the DocTypes to backup seperated by commas

Flags
-----

* `--ignore-backup-conf` Ignore excludes/includes set in config
* `--with-files` Take backup with private and public files
* `--compress` Compress private and public files
* `--verbose` Add verbosity

Examples
--------

1. Backing up with the site's private and public files.


```
bench --site {site} backup --with-files
```
2. Compress the public and private files (if required). This saves the file under a `tgz` format instead of the default `tar` format.


```
bench --site {site} backup --with-files --compress
```
3. Change the path where the files backed up will be saved.


```
bench --site {site} backup --backup-path {backup_path}
```
4. Change the path for a specific backup file. For each unspecified option, the respective file will be saved in the default location.


```
bench --site {site} backup --with-files
   --backup-path-conf {conf_path}
   --backup-path-db {db_path}
   --backup-path-files {files_path}
   --backup-path-private-files {private_path}
```
5. Add verbosity for the various stages managed internally via the Bench CLI.


```
bench --site {site} backup --verbose
```
6. Backup only certain doctypes on the site.


```
bench --site {site} backup --only 'ToDo,Note,Task,Project,Sales Invoice'
```
7. Backup all tables except certain doctypes.


```
bench --site {site} backup --exclude 'Error Log,Access Log,Activity Log,Version'
```
8. Backup complete site ignoring the `frappe.conf.backup.*` values if specified.


```
bench --site {site} backup --ignore-backup-conf
```

If the backup process happens to fail (any exception is raised) - the files will be deleted to avoid using extra disk space.

<!-- page: framework/framework__user__en__bench__reference__bench-version.md -->
---
title: "bench version\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/bench-version"
updated: "2026-02-17"
---


## Usage

```bash
bench version [OPTIONS]
```

## Description

The `version` command displays compiled info about all the apps installed in the
current bench directory. You can choose your preferred output format: plain
text, JSON or ASCII table. The `--format plain` option displays version
information as plain text, just like `bench version`, but with additional
information.

```bash
$ bench version --format plain
erpnext 14.0.3 version-14 (4e88dcf)
frappe 14.0.1 version-14 (f8ec3d7)
```

The `--format json` option displays version information as a formatted JSON
string. This is particularly useful if you're building tools over the bench CLI.

```json
$ bench version --format json
[
 {
 "app": "erpnext",
 "branch": "version-14",
 "commit": "4e88dcf",
 "version": "14.0.3"
 },
 {
 "app": "frappe",
 "branch": "version-14",
 "commit": "ef0a5e9",
 "version": "14.0.1"
 }
]
```

The `--format table` option displays version information formatted as an ASCII
table.

```bash
$ bench version --format table
+-------------------------+------------+------------------------------+---------+
| App | Version | Branch | Commit |
+-------------------------+------------+------------------------------+---------+
| erpnext | 14.0.3 | version-14 | 4e88dcf |
| frappe | 14.0.1 | version-14 | f8ec3d7 |
+-------------------------+------------+------------------------------+---------+
```

## Options

 - `-f`, `--format` Choose the format for showing versions of the apps
 installed in the current bench. The available options are "plain", "table",
 "json", "legacy". This value defaults to "legacy".


## Examples

1. Get human readable information about the installed apps on current bench,
 with commit messages.

 ```bash
 bench version --format plain
 ```

1. Get bench version information in `JSON` format.

 ```bash
 bench version -f json
 ```

<!-- page: framework/framework__user__en__bench__reference__drop-site.md -->
---
title: "bench drop-site\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/drop-site"
updated: "2026-02-17"
---


## Usage

```bash
bench drop-site [OPTIONS] SITE
```

## Description

Drop an existing site. In this operation, the database is dropped and the
respective site's folder is moved from `./sites` to `./archived_sites` *(unless
specified otherwise)* on your Bench. A full site backup is taken prior to this.

## Options

 - `--db-root-username` Username for a DBMS user with drop database privileges.
 Defaults to *root*
 - `--db-root-password` Password for the DBMS user
 - `--archived-sites-path` Specify the path to move the site's folder in

## Flags

 - `--no-backup` Skip backup prior to site drop
 - `--force` Force drop-site even if an error is encountered

### Examples

1. Skip the interactive prompt by passing the root password.

 ```bash
 bench drop-site {site} --db-root-password {db-root-pass}
 ```

1. Skip taking a backup before site deletion.

 ```bash
 bench drop-site {site} --no-backup
 ```

1. Move the site's folder in a different folder instead of the standard
 `./archived_sites`.

 ```bash
 bench drop-site {site} --archived-sites-path {path/to/archive}
 ```
