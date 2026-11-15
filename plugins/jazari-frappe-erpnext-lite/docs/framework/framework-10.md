<!-- Frappe documentation: framework, part 10 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__basics__users-and-permissions.md -->
---
title: "Users and Permissions"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/users-and-permissions"
updated: "2026-02-17"
---

Frappe comes with a user authentication system. It handles user accounts, role based permissions and cookie based user sessions.

User authentication system in Frappe comes with a lot of features out of the box:

1. User
2. Role
3. DocType Permissions
4. Permission Level
5. Role Permission Manager
6. User Permissions
7. Restricting Views and Forms
8. Password Hashing
9. Password strength checking
10. Throttling of login attempts
11. Third party authentication like OAuth, Google, Facebook, etc

User and Role
-------------

A User record represents an authenticated user who can perform authorized actions in the system. A User can have multiple roles assigned to it. A Role describes what actions a User can perform on a DocType.

![User Roles](/files/user-roles.png) *User Roles*

For example, the role **Blogger** has read, write and create permission on the doctype **Blog Post**, but only read permission on **Blog Category**.

![Role Blogger](/files/role-blogger.png) *Role Blogger*

DocType Permissions
-------------------

DocTypes can have a default set of Roles applied when you install your app. To configure roles for a DocType you must add them in the Permissions table in DocType.

![DocType Permissions](/files/doctype-permissions.png) *DocType Permissions*

If you expand the row, you will see many more options that can be configured. ![DocType Permissions Row](/files/doctype-permissions-detail.png) *DocType Permissions*

Here is a list of them with their explanation:



| Option | Explanation |
| --- | --- |
| Level | [Permission Level](#permission-level) assigned to this role |
| If the user is owner | The restrictions will apply only if the user is the one who created that document |
| Read | Allow read access to the document |
| Write | Allow edit access to the document |
| Create | Allow create access to the document |
| Delete | Allow user to delete the document |
| Submit | Allow user to submit the document |
| Cancel | Allow user to cancel the document |
| Amend | Allow user to amend the document |
| Report | Allow user to view the report view |
| Export | Allow user to export records in Excel/CSV |
| Import | Allow user to import records using the Data Import Tool |
| Set User Permissions | Allow user to apply user permissions for other users |
| Share | Allow user to share the document with other users |
| Print | Allow user to print the document or generate PDF |
| Email | Allow user to send emails for that document |

Permission Level
----------------

Permission Levels can be used to group fields in a document and apply separate roles to each level. By default all fields have permlevel set as 0.

![Permission Level](/files/permission-level.png) *Permission Level*

Role Permissions Manager
------------------------

Role Permissions Manager is a user tool to manage role permissions. The default set of permissions show up here and can be overridden.

![Role Permissions Manager](/files/role-permissions-manager.gif)  


User Permissions
----------------

User Permissions are another set of rules that can be applied per user basis. It can be used to restrict documents which contain a specific value for a Link field.

For example, to restrict the User John such that he can only view **Blog Post**s that were created by him, i.e, Blogger **John**. A user permission record with the following values should be created.

![User Permissions Example](/files/user-permissions-example-1.png) *User Permission Record*

After creating the user permission configuration, when the User logs in to see the Blog Post list, he will have a restricted view of blog posts that were created by him.

![Restricted Blog Post List](/files/user-permissions-example-2.png) *Restricted Blog Post List*

Automatic Roles
---------------

Certain roles are automatically hidden to users, this simplifies writing doctypes that need catch-all permissions. Following are automatic roles:

  


1. **"Guest"** - This role is allocated to everyone, including unauthenticated users.
2. **"All"**- This role is allocated to all registered users. This includes website users.
3. **"Administrator"** - This role is **only** allocated to `Administrator` user that is created by default.
4. **"Desk User"** - [New in v15] This role is allocated to all users whose user type is "System User" i.e. they are system users and not website users.

  


Restricting Views and Forms
---------------------------

Frappe Framework allows you to configure what modules, doctypes and views are visible to the user. To configure which modules are shown to a user go to the **Allow Modules** section of the User form.

![Allow Modules in User](/files/allow-modules-in-user.png)  


To hide a doctype from a User, remove the read permission from a Role using the [Role Permissions Manager](#role-permissions-manager).

To control permissions for Pages and Reports, use the **Role Permission for Page and Report** tool.

![Role Permission for Page and Report](/files/role-permission-for-page-and-report.png)  


Password Hashing
----------------

Frappe handles password hashing out of the box. They are encrypted and saved in a separate database table named `__Auth`.


```
MariaDB [_baa0f26509a564b6]> select * from __Auth;
+---------+------------------+-----------+-----------------------------------------------
| doctype | name             | fieldname | password
+---------+------------------+-----------+-----------------------------------------------
| User    | Administrator    | password  | $pbkdf2-sha256$29000$Xss5pxSC8F5rDSHEOEdo7Q$in
| User    | test@erpnext.com | password  | $pbkdf2-sha256$29000$y7mXMoZQau09RwiBsLaWsg$h.
+---------+------------------+-----------+-----------------------------------------------
  

```
Password Policy
---------------

Frappe also supports password strength checking. It can be enabled from **System Settings** in the Security section. The Minimum Password Score field validates how strong the password should be.

![Password Policy](/files/password-policy.png) *Password Policy*

Login Attempts
--------------

Frappe allows you to configure how many consecutive login attempts should be allowed before locking the account for a set time period.

![Login Attempts](/files/login-attempts.png)  


Third Party Authentication
--------------------------

Frappe supports third party login providers. To setup a login provider you need to setup a **Social Login Key**. Learn more about it [here](/framework/v14/user/en/guides/integration/social_login_key).

<!-- page: framework/framework__user__en__basics__virtual_docfield.md -->
---
title: "Virtual DocField"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/virtual_docfield"
updated: "2026-02-17"
---

A Virtual DocField is a dynamic attribute of a given Document (or Record). It's a calculated attribute that isn't stored in the site database. This could be used for representing values that may be functions of other static Document attributes.

![Person Record](/files/Screenshot 2022-02-14 at 1.55.38 PM.png)
*Person Form*

The age of a person is a function of their date of birth ie if you know a person's birth day, you can figure out their age. Age is also a continuous value; it may change every year, or month, or day, even hour depending on what type of granularity you wish to have. Another attribute is a Person's name. Most common implementations will have a First, Middle and a Last Name, and for the view it would be all of them together like "Jon Raphael Doe". Although saving the full name as a separate attribute may not make so much sense when the strings can be easily concatenated. These are a couple of instances where Virtual DocFields make more sense.

![Person DocType](/files/Screenshot 2022-02-14 at 1.55.08 PM.png)
*Person DocType*

Here we've added three fields to Person; two for First and Last names which are stored in the site database, and one that utilizes this data to populate the third field "Full Name". In this instance, the options field takes input for the return value of the respective virtual field.

![Full Name - Virtual DocField](/files/Screenshot 2022-02-14 at 12.18.20 PM.png)
*Person DocType - DocField*

We discussed the possibility of fields that depend on attributes in the system so far. But this could easily extend to something that doesn't depend on your DocType data alone. You may also want to fetch the statuses of multiple external services in their place, or anything else that you can map here instead.

## How to use Virtual DocFields

The steps involved in making this work are:

### 1. Define a Virtual DocField

Defining a Virtual DocField is fairly straight forward. Just checking on the "Virtual" check box under the DocField's configuration does this. Virtual DocFields don't create a corresponding column in the DocType's table. This makes the field "Read Only" in the Form Views.

> Note: Avoid making existing DocFields virtual unless you know what you're doing

### 2. Define a source for the field

The first step only adds a sort of a placeholder for the values. Without adding some code that dictates what the field should show, there's no field itself. There's two ways of doing this:

* By extending the DocType controllers

Adding a Python property with the same name as the virtual field should do this. This is the most flexible way to do this; you could daisy chain an internal API request, or fetch the data from multiple data sources, sky is the limit.

```python
class Person(Document):
 @property
 def age(self):
 return frappe.utils.now_datetime() - self.creation
```

* Using the `DocField.options`

This is a bit more restrictive given it allows you to write code directly from Desk. [Utils allowed in Server Scripts](/framework/v14/user/en/desk/scripting/script-api) and Document attributes can be accessed through this. Equivalent of the above property maybe as follows:

```python
frappe.utils.now_datetime() - self.creation
```

The above mentioned `Person.full_name` example uses Python's f-string feature to achive this in a similar way.

> Note: This should be preferred for relatively smaller scripting. Lookout for in-compatible types errors while using this


## Impact on internals

If you're wellversed with the physics of the Frappe world, this feature will appear quite predictable.

### Backend API

The `DatabaseQuery` methods or `Database` APIs will not return virtual values since they don't live in the Site Database.

![](/files/Screenshot 2022-02-14 at 2.01.58 PM.png)

### REST API

The `/api/method/frappe.desk.form.load.getdoc` and `/api/resource` APIs utilize `Document.get_valid_dict` which will compute Virtual values too. These APIs are used to render the Desk Form views too.

![](/files/Screenshot 2022-02-14 at 1.58.33 PM.png)

### Database

There's no footprint of virtual fields in the respective DocType's table. However, you may find corresponding records to give some evidence of their existence in the Custom Field, DocField tables that store DocType's Meta.

![](/files/Screenshot 2022-02-14 at 2.03.18 PM.png)

## Virtual Tables on Non-virtual DocTypes

> Note: This feature is only available in nightly (v16) version. This feature is considered experimental.

A **virtual child table** is a virtual field of type "Table" that is computed at runtime. It behaves like a normal child table in many respects:

* The virtual child table appears in the form (grid) under the parent document.
* Its rows are computed dynamically (e.g. via a cached property or descriptor).
* It is read-only (you cannot write into it through the usual ORM methods).
* The parent DocType does not persist these child rows; they exist only in memory.
* The descriptor method for the virtual table can return either raw dictionaries or `Document` instances.
* When loading from the database, the virtual child table’s descriptor is triggered to populate the children rows.

Virtual tables are useful for displaying computed/aggregated data or summary of related data stored elsewhere.

### Defining a Virtual Child Table

To define a virtual child table, you add a new field entry in the parent DocType with "is virtual" set to 1. Logic for dynamically fetching the virtual table has to be defined as a cached property on the DocType controller. 

Note: You MUST NOT use `@property` for virtual tables, only `@cached_property` and other equivalent non-data descriptors are supported.



```py
class User(…) :
    # This is a cached_property (or a non-data descriptor) returning computed rows
    @cached_property
    def virtual_sessions(self):
        # return a list of dicts or list of Document instances
        sessions = get_session_logs(self.name)
        return sessions
```

In this example, when a `User` record is loaded, the framework invokes `User.virtual_sessions` to fetch child rows, then initializes a virtual child table `virtual_sessions` in the form context.

<!-- page: framework/framework__user__en__basics__why.md -->
---
title: "Why Frappe Framework?\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/basics/why"
updated: "2026-02-17"
---


Frappe was built to power our flagship product [ERPNext](https://erpnext.com).
The core philosophy at Frappe is write as less code as possible. We prefer
configuration over code. If a feature is generic and we need it, we put it right
into the framework.

This has enabled us to build and maintain a complex application like an ERP
which has thousands of features with a small team of developers.

### Rapid Application Development

After setting up Frappe Framework, you can be productive in no time. Creating
models, wiring controller code and updating views are all handled by the
framework.

### Batteries Included

Anything that might be needed by a modern web application is probably built into
the framework already. PDF generation, Emails, SMS, Web Pages
you name it. If there is something missing in Frappe Framework, we might already
be working on it right now :)

### Easy Deployment

Bench is the all-in-one tool to manage all things Frappe. It handles app
updates, database migrations, generating configs for nginx and supervisor,
scaffolding new apps and much more.

### Multi Tenant

Bench supports multi-tenancy out of the box. It means you can spin up multiple
instances of apps with separate databases on the same codebase. It also supports
port-based multitenancy where you can set up multiple bench environments for
different versions of apps.

### Extensible architecture

Build powerful extensions on top of Frappe by creating your own apps. Apps can
bring their own models or modify existing ones in Frappe.

<!-- page: framework/framework__user__en__bench-compile-po-to-mo.md -->
---
title: "bench compile-po-to-mo"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench-compile-po-to-mo"
updated: "2026-02-17"
---

### Usage


```
bench compile-po-to-mo [OPTIONS]
```
### Prerequisites

Existing PO files in your app's `locale` directory, holding translations for at least one language.

### **Description**

The PO files hold translations in human-readable format. Before they can be used by the application, translations need to be compiled to binary files (ending with MO). The binary file is stored in the `sites/assets/locale` folder of your bench.

For efficiency, this skips compilation if there are existing MO files which are newer than the PO files.

This command is automatically executed along with `bench build` and `bench update`. You can run it explicitly in your development environment, when you just added some translations and want to see the result in the UI.

### **Options**

* `--app` This parameter let's you specify an app, in case you want to update the PO files for one app only. Default: all apps.
* `--locale` This parameter let's you specify a locale, in case you want to update the PO file for one locale only. Default: all locales.
* `--force` Force re-compilation, even if the PO files didn't change.

### **Examples**

Compile ERPNext's german translations.


```
bench compile-po-to-mo --app erpnext --locale de
```
This reads translations from `apps/erpnext/erpnext/locale/de.po` and compiles them to binary. The result is saved to `sites/assets/locale/de/LC_MESSAGES/erpnext.mo`.

<!-- page: framework/framework__user__en__bench-generate-pot-file.md -->
---
title: "bench generate-pot-file"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench-generate-pot-file"
updated: "2026-02-17"
---

### Usage


```
bench generate-pot-file [OPTIONS]
```
### Description

This generates a template file for translations, holding all translatable strings of an app (but no translations). The template file will be written to the file `[app_module]/locale/main.pot`.

For many of our apps, this command is run automatically on a regular basis via *GitHub Actions*.

### Options

* `--app` This parameter let's you specify an app, if you want to generate the POT file for one app only. Default: all apps.

### Examples

Re-generate the POT file for ERPNext:


```
bench generate-pot-file --app erpnext
```
This will extract all translatable strings from `apps/erpnext` and write them to `apps/erpnext/erpnext/locale/main.pot`

<!-- page: framework/framework__user__en__bench-migrate-csv-to-po.md -->
---
title: "bench migrate-csv-to-po"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench-migrate-csv-to-po"
updated: "2026-02-17"
---

### **Usage**


```
bench migrate-csv-to-po [OPTIONS]
```
### **Prerequisites**

Please make sure your app has a POT file already. If not, you can [generate one](https://frappeframework.com/docs/user/en/bench-generate-pot-file).

**Description**

This command reads in your existing translations from CSV files, matches them with the existing POT file and writes the result into`[app_module]/locale/[locale].po`.

You will only need this command while switching from the old translation system to the new one.

### **Options**

* `--app` This parameter let's you specify an app, in case you want to migrate translations for one app only. Default: all apps.
* `--locale` This parameter let's you specify a locale, in case you want to migrate translations for one locale only. Default: all locales.

### **Examples**

Migrate ERPNext's german translations from CSV to PO.


```
bench migrate-csv-to-po --app erpnext --locale de
```
This reads translations from `apps/erpnext/erpnext/translations/de.csv` and translatable strings from `apps/erpnext/erpnext/locale/main.pot`. The result is saved to `apps/erpnext/erpnext/locale/de.po`. If you're happy with the result, you can now delete the CSV file.

<!-- page: framework/framework__user__en__bench-update-po-files.md -->
---
title: "bench<strong> </strong>update-po-files"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench-update-po-files"
updated: "2026-02-17"
---

### **Usage**


```
bench update-po-files [OPTIONS]
```
### **Prerequisites**

Existing POT file and PO files in your app's `locale` directory.

**Description**

This command syncs your existing translation files with the existing POT file, which holds all translatable strings. It removes all outdated strings and adds new ones.

You'll want to run this command after you regenerated the POT file with translatable strings. In case you are using a dedicated platform for translation management, the platform might also take care of this step for you, so that you won't need this command.

### **Options**

* `--app` This parameter let's you specify an app, in case you want to update the PO files for one app only. Default: all apps.
* `--locale` This parameter let's you specify a locale, in case you want to update the PO file for one locale only. Default: all locales.

### **Examples**

Sync ERPNext's translatable strings with the file holding german translations.


```
bench update-po-files --app erpnext --locale de
```
This reads translations from `apps/erpnext/erpnext/locale/de.po` and translatable strings from `apps/erpnext/erpnext/locale/main.pot`. The result is saved to `apps/erpnext/erpnext/locale/de.po`.

  

<!-- page: framework/framework__user__en__bench.md -->
---
title: "Bench"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench"
updated: "2026-02-17"
---

Bench is a CLI tool to manage Frappe Deployments. It provides an easy interface to help you setup and manage multiple sites and apps based on Frappe Framework.

However, the term bench may mean different things depending on the context. We use the term "bench" to refer to the CLI tool and the directory interchangeably. This may get confusing a lot of times.


> "Did you update the bench?"
> 
> "Yes, migrations for the latest version were smoother this time around."
> 
> "What?! I told you to update the CLI tool!"
> 
> "Let's hope our clients like Version 13"
> 
> 

To avoid these type of situations, we will refer to **"Bench"** as the bench directory and **"Bench CLI"** to refer to the CLI tool.

To install the bench CLI and setup a Frappe environment, please follow the [installation instructions](/framework/v14/user/en/installation).

You may be surprised to know that a lot of the bench commands are provided by the Frappe Framework, not by the Bench CLI directly. In general, these are the commands which work on a specific site (can use the `--site` parameter). Even commands like `bench update` only provide thin wrappers around Frappe Framework commands such as `backup` and `migrate`, along with some other essential bench and system-level operations.

References
----------

1. [Bench Commands](/framework/v14/user/en/bench/bench-commands)
2. [Frappe Commands](/framework/v14/user/en/bench/frappe-commands)
3. [Command References](/framework/v14/user/en/bench/reference)
4. [Extending the CLI](/framework/v14/user/en/bench/extending-the-cli)

<!-- page: framework/framework__user__en__bench__bench-commands.md -->
---
title: "Bench Commands\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/bench-commands"
updated: "2026-02-17"
---


This page is concerned only with the commands that exist in the bench project,
that are a direct part of the CLI tool. These commands are defined under the
[frappe/bench](https://github.com/frappe/bench).

> For references of any Framework commands, checkout [Frappe
> Commands](/framework/v14/user/en/bench/frappe-commands).


## Using the bench CLI

```zsh
➜ bench
Usage: bench [OPTIONS] COMMAND [ARGS]...

 Bench manager for Frappe

Options:
 --version
 --help Show this message and exit.

Commands:
 backup Backup single site
 backup-all-sites Backup all sites in current bench
 config Change bench configuration
 disable-production Disables production environment for the bench.
 download-translations Download latest translations
 exclude-app Exclude app from updating
 find Finds benches recursively from location
 get-app Clone an app from the internet or filesystem and...
```

Similarly, all available flags and options can be checked for commands
individually by executing them with the `--help` flag. The `init` command for
instance:

```zsh
➜ bench init --help
Usage: bench init [OPTIONS] PATH

 Initialize a new bench instance in the specified path

Options:
 --python TEXT Path to Python Executable.
 --ignore-exist Ignore if Bench instance exists.
 --apps_path TEXT path to json files with apps to install
 after init
```


## Commands

Under Click's structure, `bench` is the main command group, under which there
are three main groups of commands in bench currently, namely


### General Commands

A set of commands that don't classify broadly in the other commands. Commands
such as `init`, `get-app`, `find` come under this category. These commands
belong directly to the bench group so they can be invoked directly prefixing
each with `bench` in your shell. Therefore, the usage for these commands is as

```zsh
➜ bench COMMAND [ARGS]...
```

#### Frequently Used

 - **init**: Initialize a new bench instance in the specified path. This sets up
 a complete bench folder with an `apps` folder which contains all the Frappe
 apps available in the current bench, `sites` folder that stores all site data
 separated by individual site folders, `config` folder that contains your
 redis, NGINX and supervisor configuration files. The `env` folder consists of
 all python dependencies of the current bench and installed Frappe
 applications have.
 - **restart**: Restart web, supervisor, systemd processes units. Used in the
 production setup.
 - **update**: If executed in a bench directory, without any flags will backup,
 pull, setup requirements, build, run patches and restart bench. Using
 specific flags will only do certain tasks instead of all.
 - **migrate-env**: Migrate Virtual Environment to desired Python version. This
 regenerates the `env` folder with the specified Python version.
 - **retry-upgrade**: Retry a failed upgrade
 - **disable-production**: Disables production environment for the bench.
 - **renew-lets-encrypt**: Renew Let's Encrypt certificate for site SSL.
 - **backup**: Backup single site data. Can be used to backup files as well.
 - **backup-all-sites**: Backup all sites in the current bench.

 - **get-app**: Download an app from the internet or filesystem and set it up in
 your bench. This clones the git repo of the Frappe project and installs it in
 the bench environment.
 - **remove-app**: Completely remove the specified Frappe App from the current
 bench and re-build assets if not installed on any site.
 - **exclude-app**: Exclude app from updating during a `bench update`
 - **include-app**: Include app for updating. All Frappe applications are
 included by default when installed.
 - **remote-set-url**: Set app remote url
 - **remote-reset-url**: Reset app remote url to frappe official
 - **remote-urls**: Show apps remote url
 - **switch-to-branch**: Switch all apps to specified branch, or specify apps
 separated by space
 - **switch-to-develop**: Switch Frappe and ERPNext to develop branch

#### Advanced Setup-based

 - **set-nginx-port**: Set NGINX port for site
 - **set-ssl-certificate**: Set SSL certificate path for site
 - **set-ssl-key**: Set SSL certificate private key path for site
 - **set-url-root**: Set URL root for site
 - **set-mariadb-host**: Set MariaDB host for bench
 - **set-redis-cache-host**: Set Redis cache host for bench
 - **set-redis-queue-host**: Set Redis queue host for bench
 - **set-redis-socketio-host**: Set Redis socketio host for bench
 - **use**: Set default site for bench
 - **download-translations**: Download latest translations

#### Development

 - **start**: Start Frappe development processes. Uses the Procfile to start the
 Frappe development environment.
 - **src**: Prints bench source folder path, which can be used to cd into the
 bench installation repository by `cd $(bench src)`.
 - **find**: Finds benches recursively from location or specified path.
 - **pip**: Use the current bench's pip to manage Python packages. For help
 about pip usage: `bench pip help [COMMAND]` or `bench pip [COMMAND] -h`.
 - **new-app**: Create a new Frappe application under apps folder.

#### Release bench
 - **release**: Create a release of a Frappe application
 - **prepare-beta-release**: Prepare major beta release from develop branch


### Setup Commands

This command group consists of commands used to manipulate the requirements and
the environment required by your Frappe environment. The setup commands used for
setting up the Frappe environment in the context of the current bench need to be
executed using `bench setup` as the prefix. So, the general usage of these
commands is as

```zsh
➜ bench setup COMMAND [ARGS]...
```

 - **sudoers**: Add commands to sudoers list for allowing bench commands
 execution without root password

 - **env**: Setup Python's virtual environment for your bench. This sets up a
 `env` folder under the root of the bench directory.
 - **redis**: Generates configuration for Redis
 - **fonts**: Add Frappe fonts to system
 - **config**: Generate or over-write `sites/common_site_config.json`
 - **backups**: Add cronjob for bench backups
 - **socketio**: Setup node dependencies for socketio server
 - **requirements**: Setup Python and Node dependencies

 - **manager**: Setup `bench-manager.local` site with the [Bench
 Manager](https://github.com/frappe/bench_manager) app, a GUI for bench
 installed on it.

 - **procfile**: Generate Procfile for bench start

 - **production**: Setup a Frappe production environment for the specified user.
 This installs ansible, NGINX, supervisor, fail2ban and generates the
 respective configuration files.
 - **nginx**: Generate configuration files for NGINX
 - **fail2ban**: Setup fail2ban, an intrusion prevention software framework that
 protects computer servers from brute-force attacks
 - **systemd**: Generate configuration for systemd
 - **firewall**: Setup firewall for system
 - **ssh-port**: Set SSH Port for system
 - **reload-nginx**: Checks NGINX config file and reloads service
 - **supervisor**: Generate configuration for supervisor
 - **lets-encrypt**: Setup lets-encrypt SSL for site
 - **wildcard-ssl**: Setup wildcard SSL certificate for multi-tenant bench

 - **add-domain**: Add a custom domain to a particular site
 - **remove-domain**: Remove a custom domain from a site
 - **sync-domains**: Check if there is a change in domains. If yes, updates the
 domains list.

 - **role**: Install dependencies via ansible roles


### Config Commands

The config command group deals with making changes in the current bench (not the
CLI tool) configuration. The config group commands are used for manipulating
configurations in the current bench context. The usage for these commands is as

```zsh
➜ bench config COMMAND [ARGS]...
```
 - **set-common-config**: Set value in common config with parameters -c, configs
 or --config
 - **remove-common-config**: Remove specific keys from current bench's common
 config
 - **update_bench_on_update**: Enable/Disable bench updates on running bench
 update
 - **restart_supervisor_on_update**: Enable/Disable auto restart of
 supervisor processes
 - **restart_systemd_on_update**: Enable/Disable auto restart of systemd
 units
 - **dns_multitenant**: Enable/Disable bench multitenancy on running bench
 update
 - **serve_default_site**: Configure nginx to serve the default site on port
 80
 - **http_timeout**: Set HTTP timeout


### Install Commands

The install command group deals with commands used to install system
dependencies for setting up a Frappe environment. The usage for these commands
is as

```zsh
 bench install COMMAND [ARGS]...
```

 - **prerequisites**: Installs pre-requisite libraries, essential tools like
 b2zip, htop, screen, vim, x11-fonts, python libs, cups and Redis
 - **nodejs**: Installs Node.js v8
 - **nginx**: Installs NGINX. If user is specified, sudoers is setup for that
 user
 - **packer**: Installs Oracle virtualbox and packer 1.2.1
 - **psutil**: Installs psutil via pip
 - **mariadb**: Install and setup MariaDB of specified version and root password
 - **wkhtmltopdf**: Installs wkhtmltopdf v0.12.3 for linux
 - **supervisor**: Installs supervisor. If user is specified, sudoers is setup
 for that user
 - **fail2ban**: Install fail2ban, an intrusion prevention software framework
 that protects computer servers from brute-force attacks
 - **virtualbox**: Installs virtualbox.



## General Usage

This section covers the general usage of the Bench CLI, enough to get you
familiar with the basic usage.

### Create a new bench

 The init command will create a bench directory with the frappe framework
 installed. It will be setup for periodic backups.

```zsh
➜ bench init frappe-bench && cd frappe-bench
```

### Add a site

 Frappe apps are run by frappe sites and you will have to create at least one
 site. The new-site command allows you to do that.

```zsh
➜ bench new-site site1.local
```

### Add apps

 The get-app command gets remote frappe apps from a remote git repository and
 installs them. Example: [erpnext](https://github.com/frappe/erpnext)

```zsh
➜ bench get-app erpnext https://github.com/frappe/erpnext
```

### Install apps

 To install an app on your new site, use the bench `install-app` command.

```zsh
➜ bench --site site1.local install-app erpnext
```

### Start bench

 To start using the bench, use the `bench start` command

```zsh
➜ bench start
```

 To login to Frappe / ERPNext, open your browser and go to
 `[your-external-ip]:8000`, probably `localhost:8000`

 The default username is "Administrator" and password is what you set when you
 created the new site.

### Update bench

 Update all apps and sites from your bench directory. This operation performs
 backups, sets up requirements, build asstes, runs migrations and restarts your
 process manager for you.

```zsh
➜ bench update
```

### Update Bench config

 To update the common site config for your bench, you can use the
 `set-common-config` and `remove-common-config` commands under the config
 command group. To learn more about Frappe Site configurations available,
 checkout the [Site Config](/framework/v14/user/en/basics/sites#site-config) and [Bench Config docs](/framework/v14/user/en/bench/bench-commands#config-commands).

 To add or update an existing config key, you can run something like

```zsh
➜ bench config set-common-config -c enable_frappe_logger true
```

 To remove an existing config key, you can run something like

```zsh
➜ bench config remove-common-config enable_frappe_logger
```

## Bench Manager

For a UI based approach to managing your deployments, checkout [Bench
Manager](https://github.com/frappe/bench_manager).

```zsh
➜ bench setup manager
```

You can set it up easily on any existing bench by running the above command.


### What this does?

1. Create a new site `bench-manager.local`
1. Get the `bench_manager` app
1. Install the `Bench Manager` app on the site `bench-manager.local`

You can use this site to manage your bench operations through
*bench-manager.local*'s `/desk` view.

<!-- page: framework/framework__user__en__bench__extending-the-cli.md -->
---
title: "Bench - Extending the CLI\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/extending-the-cli"
updated: "2026-02-17"
---


Along with the framework commands, Frappe's `bench_manager` module also searches
for any commands in your custom applications. Thereby, bench communicates with
the respective bench's Frappe which in turn will check for available commands in
all of the applications.

To make your custom command available to bench, just create a `commands` module
under your parent module and write the command with a click wrapper and a
variable commands which contains a list of click functions, which are your own
commands.

The directory structure with a Frappe App `flags` may be visualized as:

```bash
frappe-bench
|──apps
 |── frappe
 ├── flags
 │ ├── README.md
 │ ├── flags
 │ │ ├── commands <------ commands module
 │ ├── license.txt
 │ ├── requirements.txt
 │ └── setup.py
```

The commands module maybe a single file such as `commands.py` or a directory
with an `__init__.py` file. For a custom application of name 'flags', an example
may be given as

```python
# file_path: frappe-bench/apps/flags/flags/commands.py
import click

@click.command('set-flags')
@click.argument('state', type=click.Choice(['on', 'off']))
def set_flags(state):
 from flags.utils import set_flags
 set_flags(state=state)

commands = [
 set_flags
]
```

and with the context of the current bench, this command maybe executed simply as

```zsh
➜ bench set-flags
Flags are set to state: 'on'
```
