<!-- Frappe documentation: framework, part 16 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__guides__basics__apps.md -->
---
title: "Frappe Apps"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/basics/apps"
updated: "2026-02-17"
---


Frappe Apps are Python packages which use the Frappe platform. They can live
anywhere on the [Python
path](https://docs.python.org/2/tutorial/modules.html#the-module-search-path)
and must have an entry in the `apps.txt` file.


### Creating an app

Frappe ships with a boiler plate for a new app. The command `bench new-app
app-name` helps you start a new app by starting an interactive shell.

```
 % bench new-app sample_app
 App Name: sample_app
 App Title: Sample App
 App Description: This is a sample app.
 App Publisher: Acme Inc.
 App Icon: icon-linux
 App Color: #6DAFC9
 App Email: info@example.com
 App URL: http://example.com
 App License: MIT
```
The above command would create an app with the following directory structure.
```
 sample_app
 ├── license.txt
 ├── MANIFEST.in
 ├── README.md
 ├── sample_app
 │   ├── __init__.py
 │   ├── sample_app
 │   │   └── __init__.py
 │   ├── config
 │   │   ├── desktop.py
 │   │   └── __init__.py
 │   ├── hooks.py
 │   ├── modules.txt
 │   ├── patches.txt
 │   └── templates
 │   ├── generators
 │   │   └── __init__.py
 │   ├── __init__.py
 │   ├── pages
 │   │   └── __init__.py
 │   └── statics
 └── setup.py
```

The boiler plate contains just enough files to show your app icon on the [Desk].

### Files in the app

#### `hooks.py`

The `hooks.py` file defines the metadata of your app and integration points
with other parts of Frappe or Frappe apps. Examples of such parts include task
scheduling or listening to updates to different documents in the system. For
now, it just contains the details you entered during app creation.

```
 app_name = "sample-app"
 app_title = "Sample App"
 app_publisher = "Acme Inc."
 app_description = "This is a sample app."
 app_icon = "fa-linux"
 app_color = "black"
 app_email = "info@example.com"
 app_url = "http://example.com"
 app_version = 0.0.1
```
#### `modules.txt`

Modules in Frappe help you organize Documents in Frappe and they are defined in
the `modules.txt` file in your app. It is necessary for every [DocType] to be
attached to a module. By default a module by the name of your app is added.
Also, each module gets an icon on the [Desk]. For example, the [ERPNext] app is
organized in the following modules.

 accounts
 buying
 home
 hr
 manufacturing
 projects
 selling
 setup
 stock
 support
 utilities
 contacts

### Adding app to a site

Once you have an app, whether it's the one you just created or any other you
downloaded, you are required to do the following things.

Download the app via git

` bench get-app https://github.com/org/app_name`

Install the app to your site

` bench --site site_name install-app app_name`

<!-- page: framework/framework__user__en__guides__basics__frappe_ajax_call.md -->
---
title: "Frappe Ajax Call\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/basics/frappe_ajax_call"
updated: "2026-02-17"
---


In Frappe Framework, you can manage ajax calls via frappe.call. The frappe.call works in asynchronous manner ie. send requests and handle response via callback mechanism.

## frappe.call Structure

```js
frappe.call({
 method: "",
 type: "POST",
 args: {},
 success: function(r) {},
 error: function(r) {},
 always: function(r) {},
 btn: opts.btn,
 freeze: false,
 freeze_message: "",
 async: true,
 url: "" || frappe.request.url,
});
```

#### Parameter description

- `method`: dotted path to a whitelisted backend method
- `type`: String parameter, http request type "GET", "POST", "PUT", "DELETE". Default set to "POST".
- `args`: associative array, arguments that will pass with request.
- `success`: Function parameter, code snippet, will after successful execution of request
- `error`: Function parameter, code snippet, will execute after request failure
- `always`: Function parameter, code snipper, will execute in either case
- `btn`: Object parameter, triggering object
- `freeze`: Boolean parameter, if set freeze the instance until it receives response
- `freeze_message`: String parameter, message will populate to screen while screen is in freeze state.
- `async`: Boolean parameter, default set to true. So each frappe.call is asynchronous. To make call synchronous set parameter value as false
- `url`: String parameter, location from where hitting the request


## How to use frappe.call ?

### Calling standard API

```js
frappe.call({
 method: 'frappe.client.get_value',
 args: {
 'doctype': 'Item',
 'filters': {'name': item_code},
 'fieldname': [
 'item_name',
 'web_long_description',
 'description',
 'image',
 'thumbnail'
 ]
 },
 callback: function(r) {
 if (!r.exc) {
 // code snippet
 }
 }
});
```

- Param description:

 - `doctype`: name of doctype for which you want to pull information
 - `filters`: condition specifier
 - `fieldname`: you can specify fields in array that you want back in response

### Calling whitelisted methods

- On the client side we specify the server side `method` to be called. This is a dotted path through the python modules on the server side, where the last part is the method name.

 ```js
 frappe.call({
 method: "frappe.core.doctype.user.user.get_all_roles", //dotted path to server method
 callback: function(r) {
 // code snippet
 }
 });
 ```

- The above request calls the server-side method `get_all_roles`, located in the file `$MY_BENCH/apps/frappe/frappe/core/doctype/user/user.py`:

 ```py
 @frappe.whitelist()
 def get_all_roles():
 // business logic
 return value
 ```

 > **Note**: any server side method that should be accessed via `frappe.call()` needs to be whitelisted, by using the decorator `@frappe.whitelist()`.

<!-- page: framework/framework__user__en__guides__basics__how-to-enable-backup-encryption.md -->
---
title: "How to Enable Backup Encryption\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/basics/how-to-enable-backup-encryption"
updated: "2026-06-19"
---

Files created during the backup process can be encrypted using an auto-generated key.

## System Requirements

For MacOS, ensure that [gnupg](https://formulae.brew.sh/formula/gnupg) is installed in the system. Use the following command to install gnupg:

```bash
brew install gnupg
```

Most Linux distributions already have GnuPG installed, and the current version will likely use GnuPG 2.0 by default.

## Encrypt Backup option

1. Open the **System Settings** form.
2. Inside the *Backups* section check the *Encrypt Backup* checkbox.

![Encrypt Backup option(Enabled)](/files/encrypt-backup.png)

The system uses an auto-generated key supplied by the **Site config**. If no such key is found, **a new key is generated**. Any System Manager can later look it from the **Download Backups** page.

It encrypts the public and private files as well as the partial backup files.

## Backup Encryption Status

1. Encrypted backups are stored at the same location as the general backups: `YOUR_BENCH/sites/{site}/private/backups`.
2. Encrypted backups can be downloaded from the **Download Backups** page.
3. Encrypted backups are differentiated using the `key icon`.

![Encrypt Backup option(Enabled)](/files/backup-page.png)

## Backup Encryption Key

1. To get the backup encryption key go to the **Download Backups** page.
2. Click on the "Get Encryption Key" button and verify your password.

![Encrypt Backup option(Enabled)](/files/backup-encryption-key.png)

Copy the key to restore the encrypted backup files.

## Restoring the Encrypted backup files

1. The `bench restore SQL_FILE_PATH` can be used to restore the files without `--backup-encryption-key` as it is automatically picked from the Site Config.
2. In case of an unsuccessful restoration due to a wrong key `--backup-encryption-key` can be used to provide the key to restore the files.
3. Usage:
  For full backup files  
  `bench --site {site} restore --backup-encryption-key {key} [OPTIONS]`  
   For partial backup files  
  `bench --site {site} partial-restore --backup-encryption-key {key} [OPTIONS]`

## Manually decrypt encrypted backup files

```bash
gpg --yes --passphrase $BACKUP_ENCRYPTION_KEY --pinentry-mode loopback -o $OUTPUT_FILE -d $INPUT_FILE
```

<!-- page: framework/framework__user__en__guides__basics__sites.md -->
---
title: "Sites\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/basics/sites"
updated: "2026-02-17"
---


## Sites Directory

Frappe is a multitenant platform and each tenant is called a site. Sites exist
in a directory called `sites`, assumed as the current working directory when
running a frappe command or other services like Celery worker or a WSGI server.

You can set `sites_dir` with an environment variable `SITES_DIR` or pass
`--sites_dir` option to the frappe command.

Apart from the sites, the `sites_dir` should contain the following.

#### apps.txt

`apps.txt` contain a list of Python packages to treat as Frappe apps. Every
frappe app that you intend to use in your site should have an entry in this file.
Also, they should be in the `PYTHONPATH`. For more information, refer
[Frappe Apps](/framework/v14/user/en/basics/apps).

#### common_site_config.json

`common_site_config.json` is an optional file. Configuration common to all sites
can be put in this file.

#### assets

Assets contain files that are required to be served for the browser client.
These generally include *.js, *.css, *.png files. This directory is auto
generated using the `bench build` command.

#### languages.txt

`languages.txt` is an autogenerated file which maps every language to it's code.

## Site

A site is a directory in `sites_dir` which represents a tenant in Frappe Platform.


### Directory Structure

 site
 ├── locks
 ├── private
 │   └── backups
 ├── public
 │   └── files
 │ └── testfile.txt
 └── site_config.json

* `locks` directory is used by the scheduler to synchronize various jobs using
the [file locking concept](http://en.wikipedia.org/wiki/File_locking).

* `private` directory contains files that require authentication to access.
Presently, it is limited only to backups.

* `public` directory contains files that can directly served. In the above
 example, `testfile.txt` can be accessed by the URL,
 http://site/files/testfile.txt

* `site_config.json` contains site specific configuration

### Site Config

[See configuration options for `site_config.json`](/framework/v14/user/en/basics/sites#site-config)

### Site Resolution

While responding to an HTTP request, a site is automatically selected based on,

* `Host` header in the HTTP request matches a site
* `X-Frappe-Site-Name` header in the HTTP request matches a site

It is also possible to force the development server to serve a specific site by
starting it with the following command.
 `bench --site SITENAME serve`


### Adding a new site

To add a new site, execute the following command in your bench instance:

`bench new-site SITENAME`

### Set a site as the current site

To force a site to be used as the default site, execute the following:

`bench use SITENAME`

To make sure, check the contents of `currentsite.txt` (found in the `sites` folder of your bench instance) and it should have SITENAME.

<!-- page: framework/framework__user__en__guides__basics__translations.md -->
---
title: "Translations in Your Custom Frappe App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/basics/translations"
updated: "2026-02-17"
---

# How to Add and Manage Translations in Your Custom Frappe App: A Step-by-Step Guide

---

## 1. Create the `translations` Folder

**Step:**  
In your custom app directory, create a folder named `translations` at:

```
apps/your-app/your-app/translations/
```

**Why?** 
Frappe automatically detects this folder. It follows a convention-over-configuration approach, so placing your translation files here ensures they're recognized without extra setup.

---

## 2. Add Translation CSV Files

**Step:**  
Create a CSV file for each language in the `translations` folder. For example:

- `ar.csv` (Arabic)
- `es.csv` (Spanish)

**CSV Structure:**

```csv
"source_string","translated_string","context"
"agent","توكيل",""
"continue","إستكمال",""
```

**Why?**

- **Column 1 (`source_string`)**: The original string used in your code (e.g., `_("continue")`).
- **Column 2 (`translated_string`)**: The translated version of the string.
- **Column 3 (`context`)**: Optional. Use it to clarify the translation context.

The third column is optional and may be left empty.

---

## 3. Use Translatable Strings in Your Code

**Step:**  
Wrap strings in your Python, HTML, or JavaScript code using `_()`:

```python
from frappe import _

def my_function():
    message = _("continue")  # Will be replaced with "إستكمال" for Arabic users
```

**Why?**  
The `_()` function marks strings as translatable. During runtime, Frappe replaces them based on the user's language preference.

---

## 4. Build the Site

Only needed if you're using `__()` in custom frontend JS and changed the JS files

**Step:**  
Run the build command:

```bash
bench --site your-site build
```

---

## 5. Verify Translations

**Step:**

- Switch your user’s language to Arabic (or target language) in Frappe.
- Check if `_("continue")` now shows as `"إستكمال"`.

**Why?**  
This confirms that Frappe correctly maps the source string to its translated counterpart.

---

## Key Notes

### Language Codes
- CSV filenames must match Frappe’s language code (e.g., `ar` for Arabic).
- You can find these codes in **Frappe > Language settings**.

### Folder Location
- The `translations` folder must be at the **root** of your app’s package directory (not inside a submodule).

### Performance
- Translations are **cached** during build.
- **Always restart bench** after editing translation files.

### Fallback Behavior
- If a string isn’t translated, Frappe will use the original (source) string.

---
## Do i need to build or migrate the site?

NO, frappe loads translations **dynamically at runtime** from your `translations/lang.csv` file, based on the logged-in user’s language preference.
you just need to refresh your browser or clear-cashe if necessary.

`bench build` only needed if you’re using `__()` in custom frontend JS and changed the JS files

---

## Example Workflow

1. Create:  
   ```
   apps/my_app/my_app/translations/ar.csv
   ```

2. Add entries:  
   ```csv
   "welcome_message","مرحبا بك!",""
   ```

3. Use in code:  
   ```python
   _("welcome_message")
   ```

4. Clear Cashe:  
- use it if translations don't reflect immediately
   ```bash
   bench --site my-site clear-cache
   ```
5. Build:
 - only needed if you're using `__()` in custom frontend JS and changed the JS files
   ```bash
   bench --site my-site build
   ```
6. Test in Arabic interface.

---
## Explain Context?

context is nothing but a meta-data,
to explain to the one who will use this translation when and where to use it.
because sometimes you have the same word with different meaning

as example:

```
"charge","شحن",""
"charge","رسوم",""
```

here we have same word but different meaning (different context to use)
so, to filter it we have to give it a context

```
"charge","شحن","mobile phone charge"
"charge","رسوم","invoice line"
```

in code:

```
_("charge") # here we don't know which meaning (context to use)
_("charge", context="mobile phone charge") # here we mean شحن
_("charge", context="invoice line") # here we mean رسوم
```

<!-- page: framework/framework__user__en__guides__caching.md -->
---
title: "Caching"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/caching"
updated: "2026-08-28"
---

One of the batteries included in Frappe Framework is inbuilt caching using Redis. Redis is fast, simple to use, in-memory key-value storage. Redis with Frappe Framework can be used to speed up repeated long-running computations or avoid database queries for data that doesn't change often.

Redis is spawned as a separate service by the bench and each Frappe web/background worker can connect to it using `frappe.cache`.

Note: On older versions of Frappe, you may need to use `frappe.cache()` instead of `frappe.cache` to access Redis connection. 

### Redis Data Types and Usage

Redis supports many data types, but here we will only cover a few most used datatypes:

1. **Strings** are the most popular and most used datatype in Redis. They are stored as key-value pairs.

```
In [1]: frappe.cache.set_value("key", "value")

In [2]: frappe.cache.get_value("key")
Out[2]: 'value'

```

2. **Hashes** are used to represent complicated objects, fields of which can be updated separately without sending the entire object. You can imagine Hashes as dictionaries stored on Redis.

```
# Get fields separately
In [1]: frappe.cache.hset("user|admin", "name", "Admin")
In [2]: frappe.cache.hset("user|admin", "email", "admin@example.com")

# Get single field value
In [3]: frappe.cache.hget("user|admin", "name")
Out[3]: 'Admin'

# Or retrieve all fields at once.
In [4]: frappe.cache.hgetall("user|admin")
Out[4]: {'name': 'Admin', 'email': 'admin@example.com'}

```

### Cached Documents

Frappe has an inbuilt function for getting documents from the cache instead of the database.

Getting a document from the cache is usually faster, so you should use them when the document doesn't change that often. A common usage for this is getting user configured settings.

```
system_settings = frappe.get_cached_doc("System Settings")

```

Cached documents are automatically cleared using "best-effort" cache invalidation.

Whenever Frappe's ORM encounters a change using `doc.save` or `frappe.db.set_value`, it clears the related document's cache. However, this isn't possible if a raw query to the database is issued.

Note: Manual cache invalidation can be done using `frappe.clear_document_cache(doctype, name)`.

### Implementing Custom Caching

When you're dealing with a long expensive computation, the outcome of which is deterministic for the same inputs then it might make sense to cache the output.

Let's attempt to implement a custom cache in this toy function which is slow.

```
def slow_add(a, b):
    import time; time.sleep(1) # Fake workload
    return a + b

```

The most important part of implementing custom caching is generating a unique key. In this example the outcome of the cached value is dependent on two input variables, hence they should be part of the key.

```
def slow_add(a, b):
    key = f"slow_addition|{a}+{b}" # unique key representing this computation

    # If this key exists in cache, then return value
    if cached_value := frappe.cache.get_value(key):
        return cached_value

    import time; time.sleep(1) # Fake workload
    result = a + b

    # Set the computed value in cache so next time we dont have to do the work
    frappe.cache.set_value(key, result)

    return result

```

#### Cache Invalidation

Two strategies are recommended for avoiding stale cache issues:

1. Setting short TTL while setting cached values.

```
# This cached value will automatically expire in one hour
frappe.cache.set_value(key, result, expires_in_sec=60*60)

```

2. Manually clearing the cache when cached values are modified.

```
frappe.cache.delete_value(key) # `frappe.cache.hdel` if using hashes.

```

### `@redis_cache` decorator

Frappe provides a decorator to automatically cache the results of a function call.

You can use it to quickly implement caching on top of any existing function which might be slow.

```
In [1]: def slow_function(a, b):
   ...:     import time; time.sleep(1)  # fake expensive computation
   ...:     return a + b
   ...:

In [2]: # This takes 1 second to execute every time.
   ...: %time slow_function(40, 2)
   ...:
Wall time: 1 s
Out[2]: 42

In [3]: %time slow_function(40, 2)
Wall time: 1 s
Out[3]: 42

In [4]: from frappe.utils.caching import redis_cache
   ...:

In [5]: @redis_cache
   ...: def slow_function(a, b):
   ...:     import time; time.sleep(1)  # fake expensive computation
   ...:     return a + b
   ...:


In [6]: # Now first call takes 1 second, but all subsequent calls return instantly.
   ...: %time slow_function(40, 2)
   ...:
Wall time: 1 s
Out[6]: 42

In [7]: %time slow_function(40, 2)
   ...:
Wall time: 897 µs
Out[7]: 42

```

#### Cache Invalidation

There are two ways to invalidate cached values from `@redis_cache`.

1. Setting appropriate expiry period (TTL in seconds) so cache invalidates automatically after some time. Example: `@redis_cache(ttl=60)` will cause cached value to expire after 60 seconds.
2. Manual clearing of cache. This is done by calling function's `clear_cache` method.

```
from frappe.utils.caching import redis_cache

@redis_cache
def slow_function(...):
    ...


def invalidate_cache():
    slow_function.clear_cache()

```

### Frappe's Redis Setup

Bench sets up Redis by default. You will find Redis config in `{bench}/config/` directory.

Bench also configures `Procfile` and supervisor configuration file to launch Redis server when the bench is started.

```
redis_cache: redis-server config/redis_cache.conf

```

A sample config looks like this:

```
dbfilename redis_cache.rdb
dir /home/user/benches/develop/config/pids
pidfile /home/user/benches/develop/config/pids/redis_cache.pid
bind 127.0.0.1
port 13000
maxmemory 737mb
maxmemory-policy allkeys-lru
appendonly no

save ""

```

You can modify this `maxmemory` in this config to increase the maximum memory allocated for caching. We do not recommend modifying anything else.

Refer to the official config documentation to understand more: &lt;[https://redis.io/docs/latest/operate/oss\_and\_stack/management/config-file/](https://redis.io/docs/latest/operate/oss_and_stack/management/config-file/)&gt;

### Implementation details

#### Multi-tenancy

`frappe.cache` internally prefixes keys by some site context. Hence calling `frappe.cache.set_value("key")` from two different sites on the same bench will create two separate entries for each site.

To see implementation details of this see `frappe.cache.make_key` function.

#### Complex Types

Frappe uses `pickle` module to serialize complex objects like documents in bytes. Hence when using `frappe.cache` you don't have to worry about serializing/de-serializing values.

Read more about pickling here: &lt;[https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)&gt;

#### Client Side caching

Frappe implements client-side cache on top of Redis cache inside `frappe.local.cache` to avoid repeated calls to Redis.

Any repeated calls to Redis within the same request/job return data from the client cache instead of calling Redis again.

#### `RedisWrapper`

All Frappe related changes are made by wrapping the default Redis client and extending the methods. You can find this code in `frappe.utils.redis_wrapper` the module.

<!-- page: framework/framework__user__en__guides__data__import-large-csv-file.md -->
---
title: "Bulk Data Import Guide"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/data/import-large-csv-file"
updated: "2026-02-17"
---

When importing very large datasets (e.g., more than 5,000 documents), it's recommended to use the command-line utility `bench data-import` instead of the web interface. This approach avoids web request timeouts and ensures a more reliable import process.

## Example Command:

> `bench --site test.erpnext.com data-import ~/Downloads/Activity_Type.csv`

## Command Help

> `bench data-import --help`

### Command Usage: 
> `bench  data-import [OPTIONS]`

This command allows bulk import of documents into your site from CSV or XLSX files.

### Options:
| Option|Description |
|----|--|
| `--file FILE` | Path to import file (.csv, .xlsx).Consider that relative paths will resolve from 'sites' directory *[required]* |
| `--doctype TEXT` | DocType target to import *[required]* |
| `--type [Insert\|Update]` | Insert New Records or Update Existing Records |
| `--submit-after-import` | Submit document after importing it |
| `--mute-emails` | Mute emails during import |
| `--help` | Show this message and exit. |

### Note:
* The `--file` option can be omitted if the file path is provided as a positional argument.

<!-- page: framework/framework__user__en__guides__data__using-data-migration-tool.md -->
---
title: "Using the Data Migration Tool\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/data/using-data-migration-tool"
updated: "2026-02-17"
---


> Data Migration Tool was introduced in Frappe Framework version 9.

The Data Migration Tool was built to abstract all the syncing of data between a remote source and a DocType. This is a middleware layer between your Frappe based website and a remote data source.

To understand this tool, let's make a connector to push ERPNext Items to an imaginary service called Atlas.

### Data Migration Plan
A Data Migration Plan encapsulates a set of mappings.

Let's make a new *Data Migration Plan*. Set the plan name as 'Atlas Sync'. We also need to add mappings in the mappings child table.

![New Data Migration Plan](/files/new-data-migration-plan.png)


### Data Migration Mapping
A Data Migration Mapping is a set of rules that specify field-to-field mapping.

Make a new *Data Migration Mapping*. Call it 'Item to Atlas Item'.

To define a mapping, we need to put in some values that define the structure of local and remote data.

1. Remote Objectname: A name that identifies the remote object e.g Atlas Item
1. Remote primary key: This is the name of the primary key for Atlas Item e.g id
1. Local DocType: The DocType which will be used for syncing e.g Item
1. Mapping Type: A Mapping can be of type 'Push' or 'Pull', depending on whether the data is to be mapped remotely or locally. It can also be 'Sync', which will perform both push and pull operations in a single cycle.
1. Page Length: This defines the batch size of the sync.

![New Data Migration Mapping](/files/new-data-migration-mapping.png)

#### Specifying field mappings:

The most basic form of a field mapping would be to specify fieldnames of the remote and local object. However, if the mapping is one-way (push or pull), the source field name can also take literal values in quotes (for e.g `"GadgetTech"`) and eval statements (for e.g `"eval:frappe.db.get_value('Company', 'Gadget Tech', 'default_currency')"`). For example, in the case of a push mapping, the local fieldname can be set to a string in quotes or an `eval` expression, instead of a field name from the local doctype. (This is not possible with a sync mapping, where both local and remote fieldnames serve as a target destination at a some point, and thus cannot be a literal value).

Let's add the field mappings and save:

![Add fields in Data Migration Mapping](/files/new-data-migration-mapping-fields.png)

We can now add the 'Item to Atlas Item' mapping to our Data Migration Plan and save it.

![Save Atlas Sync Plan](/files/atlas-sync-plan.png)

#### Additional layer of control with pre and post process:

Migrating data frequently involves more steps in addition to one-to-one mapping. For a Data Migration Mapping that is added to a Plan, a mapping module is generated in the module specified in that plan.

In our case, an `item_to_atlas_item` module is created under the `data_migration_mapping` directory in `Integrations` (module for the 'Atlas Sync' plan).

![Mapping __init__.py](/files/mapping-init-py.png)

You can implement the `pre_process` (receives the source doc) and `post_process` (receives both source and target docs, as well as any additional arguments) methods, to extend the mapping process. Here's what some operations could look like:

![Pre and Post Process](/files/mapping-pre-and-post-process.png)

### Data Migration Connector
Now, to connect to the remote source, we need to create a *Data Migration Connector*.

![New Data Migration Connector](/files/new-connector.png)

We only have two connector types right now, let's add another Connector Type in the Data Migration Connector DocType.

![Add Connector Type in Data Migration Connector](/files/add-connector-type.png)

Now, let's create a new Data Migration Connector.

![Atlas Connector](/files/atlas-connector.png)

As you can see we chose the Connector Type as Atlas. We also added the hostname, username and password for our Atlas instance so that we can authenticate.

Now, we need to write the code for our connector so that we can actually push data.

Create a new file called `atlas_connection.py` in `frappe/data_migration/doctype/data_migration_connector/connectors/` directory. Other connectors also live here.

We just have to implement the `insert`, `update` and `delete` methods for our atlas connector. We also need to write the code to connect to our Atlas instance in the `__init__` method. Just see `frappe_connection.py` for reference.

![Atlas Connection file](/files/atlas-connection-py.png)

After creating the Atlas Connector, we also need to import it into `data_migration_connector.py`

![Edit Connector file](/files/edit-connector-py.png)

### Data Migration Run
Now that we have our connector, the last thing to do is to create a new *Data Migration Run*.

A Data Migration Run takes a Data Migration Plan and Data Migration Connector and execute the plan according to our configuration. It takes care of queueing, batching, delta updates and more.

![Data Migration Run](/files/data-migration-run.png)

Just click Run. It will now push our Items to the remote Atlas instance and you can see the progress which updates in realtime.

After a run is executed successfully, you cannot run it again. You will have to create another run and execute it.

Data Migration Run will try to be as efficient as possible, so the next time you execute it, it will only push those items which were changed or failed in the last run.


> Note: Data Migration Tool is still in beta. If you find any issues please report them [here](https://github.com/frappe/erpnext/issues)

<!-- page: framework/framework__user__en__guides__database-settings__postgres-database-setup.md -->
---
title: "Postgres Database Setup"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/database-settings/postgres-database-setup"
updated: "2026-05-10"
---

Use following command to use Postgres as database for your new site.

`bench new-site &lt;site-name&gt; --db-type postgres`

**Note:** Make sure you have Postgres version 9 or greater installed in your system.

<!-- page: framework/framework__user__en__guides__database-settings__setup-read-from-secondary-db.md -->
---
title: "Setup read operations from slave/secondary mysql system\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/database-settings/setup-read-from-secondary-db"
updated: "2026-02-17"
---


In normal, the system does read and write operations on the same database. As data size increases or the number of concurrent activities increases, you may start facing a lag in operations.

One immediate solution to avoid such delay is, separate out the read and write activities, i.e. read all data from replica / secondary database and write all information to master / primary database.

Now, in frappe, you can split read and write activities between master and replica.

## Steps to setup readonly environment

1. **Pre-requisites** :
 You should have setup for [MariaDB Master-Slave](https://mariadb.com/kb/en/library/setting-up-replication/) or [Cluster](https://mariadb.com/kb/en/library/getting-started-with-mariadb-galera-cluster/) environment.

2. **Configurations for read-only replica** :

 In your site_config.json, add following keys to enable read from replica / secondary system.

 ```
 ...
 "read_from_replica" : 1/0 # to enable disable read from replica
 "different_credentials_for_replica" : 1/0 #if database creadetials are different on replica then set 1 else 0
 "replica_host" : "IP address for replica" ,
 "replica_db_port" : "Replica DB port",
 "replica_db_name" : "Replica DB name",
 "replica_db_password" : "Replica DB password",
 ...
 ```

 **Note**: If you have enabled MariaDB master-replica environment, then DB name and DB password are same on both.

3. [Grant access permissions](https://dev.mysql.com/doc/refman/8.0/en/grant.html) for master host on slave / secondary system.

<!-- page: framework/framework__user__en__guides__deployment__email-notifications-for-failed-background-jobs.md -->
---
title: "Email Notifications For Failed Background Jobs\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/deployment/email-notifications-for-failed-background-jobs"
updated: "2026-02-17"
---



Frappe handles failure of jobs in the following way,

1) If a job fails, (raises exception), it's logged in Scheduler Log and  `logs/worker.error.log`.  
2) Keeps a lock file and would not run anymore if lock file is there.  
3) Raises LockTimeoutError in case the lock file is more than 10 minutes old.


You can configure email notification for scheduler errors. By writing a file, `sites/common_site_config.json` with content  




```
{
  "celery_error_emails": {
 "ADMINS": [
 [
 "Person 1",
 "person1@example.com"
 ],
 [
 "Person2 ",
 "person2@example.com"
 ]
 ],
 "SERVER_EMAIL": "exceptions@example.com"
 }
}
```

One limitation is that it'll use local mailserver on port 25 to send the emails.

<!-- page: framework/framework__user__en__guides__deployment__how-to-enable-social-logins.md -->
---
title: "How To Enable Social Logins"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/deployment/how-to-enable-social-logins"
updated: "2026-02-17"
---


Use Facebook, Google or GitHub authentication to login to Frappe, and your users will be spared from remembering another password.

The system uses the **Email Address** supplied by these services to **match with an existing user** in Frappe. If no such user is found, **a new user is created** of the default type **Website User**, if Signup is not disabled in Website Settings. Any System Manager can later change the user type from **Website User** to **System User**, so that the user can access the Desktop.

#### Login screen with Social Logins enabled
![Login screen with Social Logins enabled](/files/social-logins.png)

To enable these signups, you need to have **Client ID** and **Client Secret** from these authentication services for your Frappe site. The Client ID and Client Secret are to be set in **Desktop > Integration > Authentication > Social Login Key > Client ID** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**. Here are the steps to obtain these credentials.

> Use **https://{{ yoursite }}** if your site is HTTPS enabled.

---

### Frappe

This is assuming you have two 2 sites built on Frappe Framework. Site A is `https://sitea.com` and Site B is `https://siteb.com`. You want to use `https://sitea.com` as the login provider and setup Social Login on `https://siteb.com` to login via `https://sitea.com`.

1. Go to `https://sitea.com` which is the login provider
2. Go to OAuth Client list
3. Create a new OAuth Client
4. Enter the App Name (Something that identifies Site B)
5. In Redirect URIs and Default Redirect URI enter `https://siteb.com/api/method/frappe.integrations.oauth2_logins.login_via_frappe`
6. After you save the document, App Client ID and App Client Secret will be generated
7. Go to `https://siteb.com` where you want to setup Social Login
8. Go to Social Login Key and create a new one
9. Enter Client ID and Client Secret obtained in step 6
10. Select Social Login Provider as Frappe
11. Enter `https://sitea.com` as Base URL and then save the document.

### Facebook

1. Go to [https://developers.facebook.com](https://developers.facebook.com)
1. Click on Apps (topbar) > New App, fill in the form.
1. Go to Settings > Basic, set the **Contact Email** and save the changes.
1. Go to Settings > Advanced, find the field **Valid OAuth redirect URIs**, and enter:
 `http://{{ yoursite }}/api/method/frappe.integrations.oauth2_logins.login_via_facebook`
1. Save the changes in Advance tab.
1. Go to Status & Review and switch on "Do you want to make this app and all its live features available to the general public?"
1. Go to Dashboard, click on the show button besides App Secret, and copy the App ID and App Secret into **Desktop > Integration > Authentication > Social Login Key > Client ID** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**


---

### Google

1. Go to [https://console.developers.google.com](https://console.developers.google.com)
1. Create a new Project and fill in the form.
1. Click on APIs & Auth > Credentials > Create new Client ID
1. Fill the form with:
 - Web Application
 - Authorized JavaScript origins as **http://{{ yoursite }}**
 - Authorized redirect URI as
 `http://{{ yoursite }}/api/method/frappe.integrations.oauth2_logins.login_via_google`
1. Go to the section **Client ID for web application** and copy the Client ID and Client Secret into **Desktop > Integration > Authentication > Social Login Key > Client ID**



---

### GitHub

1. Go to [https://github.com/settings/applications](https://github.com/settings/applications)
1. Click on **Register new application**
1. Fill the form with:
 - Homepage URL as **http://{{ yoursite }}**
 - Authorization callback URL as
 `http://{{ yoursite }}/api/method/frappe.integrations.oauth2_logins.login_via_github`
1. Click on Register application.
1. Copy the generated Client ID and Client Secret into **Desktop > Website > Setup > Social Login Keys** and **Desktop > Integration > Authentication > Social Login Key > Client Secret**



---

### Office 365

1. Go to [https://portal.azure.com](https://portal.azure.com)
1. Create a new Azure Active Directory > App Registration.
1. Click on New Application Registration
1. Fill the form with:
 - Application Name
 - Select Accounts in any organizational directory (Any Azure AD directory - Multitenant).
 - Application Type - Web app / API
 - Redirect URI as
 - Homepage URL as **http://{{ yoursite }}**
 - Authorization callback URL as `http://{{ yoursite }}//api/method/frappe.integrations.oauth2_logins.login_via_office365`
1. Click on Register application.
1. Go to the section **Overview** in Azure Portal copy the Application (client) ID into **Desktop > Integration > Authentication > Social Login Key > Client ID
1. Go to the section **Certificates & secrets** in Azure Portal and create new client secrets copy than copy Client Secret by adding into **Desktop > Integration > Authentication > Social Login Key > Client Secret**
1. Select Office 365 as Social Login Provider
1. Click Enable Social Login and Save
1. Go to the section **Token configuration** click add optional claim
 - Add Token Type > ID > Email


---

<!-- page: framework/framework__user__en__guides__deployment__how-to-migrate-doctype-changes-to-production.md -->
---
title: "How To Migrate Doctype Changes To Production\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/deployment/how-to-migrate-doctype-changes-to-production"
updated: "2026-02-17"
---


#### 1. DocType / Schema Changes

If you are in `developer_mode`, the `.json` files for each **DocType** are automatically updated.

When you update in your production using `--latest` or `bench update`, these changes are updated in the site's schema too!

#### 2. Permissions

Permissions do not get updated because the user may have changed them. To update permissions, you can add a new patch in the `patches.txt` of your app.

 execute:frappe.permissions.reset_perms("[docype]")

<!-- page: framework/framework__user__en__guides__deployment__migrations.md -->
---
title: "Migrations"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/deployment/migrations"
updated: "2026-02-17"
---


A project often undergoes changes related to database schema during course of
its life. It may also be required patch existing data. Frappe bundles tools to
handle these scenarios.

When you pull updates from any Frappe app (including Frappe), you should run
`bench migrate` to apply schema changes and data migrations if any.

## Schema changes

You can edit a DocType to add, remove or change fields. On saving a DocType,
a JSON file containing the DocType data is added to source tree of your app.
When you add an app to a site, the DocTypes are installed using this JSON file.
For making schema changes, it's required to set `developer_mode` in the
configuration.

On running a sync (`bench migrate`), doctypes in the system are synced to
their latest version from the JSON files in the app.

Note: Fields are soft deleted ie. the columns are not removed from the database
table and however, they will not be visible in the documents. This is done to
avoid any potential data loss situations and to allow you write related data
migrations which might need values from deleted fields.

Note: Frappe doesn't support reverse schema migrations.

## Data Migrations

On introducing data related changes, you might want to run one off scripts to
change existing data to match expectations as per new code.

To add a data migration to your code, you will have to write an `execute`
function to a python module and add it to `patches.txt` of your app.
Alternatively, you can create a new patch interactively by using following command:

```
$ bench create-patch
Select app for new patch (frappe, hrms, ecommerce_integrations, erpnext): frappe
Provide DocType name on which this patch will apply: User
Describe what this patch does: Improve Indexing
Provide filename for this patch [improve_indexing.py]:
Patch folder '/home/ankush/benches/develop/apps/frappe/frappe/core/doctype/user/patches' doesn't exist, create it? [Y/n]: y
Created /home/ankush/benches/develop/apps/frappe/frappe/core/doctype/user/patches/improve_indexing.py and updated patches.txt
```

It is recommended to make a file with a patch number and name in its path and
add it to a patches package (directory) in your app. You can then add a line
with dotted path to the patch module to `patches.txt`.

The directory structure followed in Frappe is as below


 frappe
 └── patches
 └── 4_0
 └── my_awesome_patch.py

The patch can be added to `patches.txt` by adding a line like

 frappe.patches.4_0.my_awesome_patch

The metadata ie. DocType available in the execute function will be the latest as
per JSON files in the apps. However, you will not be able to access metadata of
any previous states of the system.

#### One off Python statements

You can also add one off python statements in `patches.txt` using the syntax,
 execute:{python statement}

For example,
 execute:frappe.get_doc("User", "Guest").save()

Note: All lines in patches.txt have to be unique. If you want to run a line
twice, you can make it unique by adding a distinct comment.

For Example,

 execute:frappe.installer.make_site_dirs() #2014-02-19

<!-- page: framework/framework__user__en__guides__deployment__packages.md -->
---
title: "Packages\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/deployment/packages"
updated: "2026-02-17"
---


> New in [Version 14](https://github.com/frappe/frappe/pull/14123)

Packages are light weight apps that you can directly build from the Framework UI. A Package is very much like an app and a collection of Module Defs.

You can make apps directly from the Framework UI (without using the command-line) using DocTypes, Server Scripts, Web Page etc. High quality apps can be build from the Framework directly. These apps can be bundled in a "Package" and then imported to other sites.

To add a module to a package, you have to set its "Package" property. This is available for "Custom" Module Defs

### Creating a Package

You can create a new Package by creating a Package object. You can set a README and a LICENSE. A Package is designed in a way that it can be pushed to a git repository.

Once you have created a package, you can add your custom Module Defs to that package.

![Package](/files/package.png)

### Making a Package Release

A **Package Release** will export all the package modules in the `[bench]/sites/[site]/packages` folder like an app, and then bundle the folder in a gzipped tarfile `[package]-[version].tar.gz`

You can then download the package release and import it in another site

![Package Release](/files/package-release.png)

### Importing a Package

You can create a **Package Import** and attach the exported package on a new site. If you check "Activate", the package will be extracted into the `[bench]/sites/[sitename]/packages` folder (existing files will be overwritten).

The system will then *migrate* this package to the database similar to how an app migration works. Files that have not been changed will be skipped unless the "Force" check is applied.

A log is created with the output.

![Package Import](/files/package-import.png)

<!-- page: framework/framework__user__en__guides__desk.md -->
---
title: "Desk Customization\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/desk"
updated: "2026-02-17"
---

Articles related to customization of Frappe Desk

1. [Formatter_ For Link Fields](/framework/v14/user/en/guides/desk/formatter_for_link_fields)
2. [Making Charts](/framework/v14/user/en/guides/desk/making_charts)

<!-- page: framework/framework__user__en__guides__desk__formatter_for_link_fields.md -->
---
title: "Formatter For Link Fields"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/desk/formatter_for_link_fields"
updated: "2026-02-17"
---


In case where a code and a name is maintained for an entity, (for example for Employee there may be an Employee Code and Employee Name) and we want to show both the ID and name in a link field, we can make a formatter.

#### Example:

```
frappe.form.link_formatters['Employee'] = function(value, doc) {
    if(doc.employee_name && doc.employee_name !== value) {
        return value + ': ' + doc.employee_name;
    } else {
        return value;
    }
}
```

Notes:

1. Both the primary key (`name`) and the descriptive name (e.g. `employee_name`) must be present in the document. The descriptive name field could be hidden
1. This needs to be loaded before the document is loaded and can be re-used for all forms. You can also add it in `build.json`

<!-- page: framework/framework__user__en__guides__desk__making_charts.md -->
---
title: "Making Charts\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/desk/making_charts"
updated: "2026-02-17"
---


[**Frappe Charts**](https://frappe.github.io/charts/) enables you to render simple line, bar or percentage graphs for single or multiple discreet sets of data points. You can also set special checkpoint values and summary stats. Check out the docs at https://frappe.github.io/charts/ to learn more.
