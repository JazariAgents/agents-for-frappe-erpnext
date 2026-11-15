<!-- Frappe documentation: framework, part 13 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__customize-geolocation-map.md -->
---
title: "Customize the Geolocation / Map field"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/customize-geolocation-map"
updated: "2026-02-17"
---

If you want to show a map in your DocType Form, you can add a field of type "Geolocation". By default, it looks like this:

[Screenshot on the live page: orginal_map]  


There are many ways to customize this field. We can change global values like the default location and zoom level. And we can customize how individual objects on a particular map are rendered.

Change the map defaults
-----------------------


> Note: these changes require a custom app and will apply to all maps in your system.
> 
> 

By default, it shows a street map centered on Mumbai. This is not configurable via the GUI yet. But, using a custom app, we can change the map type, start location, zoom level, etc.

Start by creating a file `$MY_APP/$MY_APP/public/js/map_defaults.js`. In your `$MY_APP/$MY_APP/hooks.py`, add the JS file into the `app_include_js` hook:


```
app_include_js = [
    "/assets/$MY_APP/js/map_defaults.js"
    # ...
]
```
Now, frappe will load this file for all desk views (i.e. for logged in system users).

In `map_defaults.js`, we add the following lines:


```
// Make sure we have a dictionary to add our custom settings
const map_settings = frappe.provide("frappe.utils.map_defaults");

// Center and zoomlevel can be copied from the URL of
// the map view at openstreetmap.org.

// New default location (middle of germany).
map_settings.center = [51.57, 9.866];
// new zoomlevel: see the whole country, not just a single city
map_settings.zoom = 6;

// Use a different map: satellite instead of streets
// Examples can be found at https://leaflet-extras.github.io/leaflet-providers/preview/
map_settings.tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}";
map_settings.attribution = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community";
```
Restart your bench and reload your browser window. Now you should see the customized map:

[Screenshot on the live page: custom_map_defaults]  


Change how a particular map is rendered
---------------------------------------

In order to change the look and feel of a particular map, you can overwrite the controller methods of the Geolocation field. This can be done with a **Client Script** or with the hook in a custom app.

By default, everything drawn on the map is blue. Let's overwrite the method `on_each_feature` to make all polygons red:


```
frappe.ui.form.on("My Doctype", {
    setup(frm) {
        frm.fields_dict.MY_MAP_FIELD.on_each_feature = function(feature, layer) {
            if (feature.geometry.type == "Polygon") {
                layer.setStyle({color: "red"});
            }
        };
    }
});
```
The result looks like this:

[Screenshot on the live page: red_polygon]  


Other methods that can be overwritten include `point_to_layer` and `set_style`. Read more about these methods [in the Leaflet documentation](https://leafletjs.com/examples/geojson/).

<!-- page: framework/framework__user__en__database-migrations.md -->
---
title: "Database Migrations\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/database-migrations"
updated: "2026-02-17"
---


A project often undergoes changes related to database schema during course of
its development. It may also require patching of existing data. Frappe comes
with a migration and patch system tools to handle these scenarios.

When there are schema changes in your app, to migrate your existing site's
database to the new schema, you should run the command.

```sh
bench --site [sitename] migrate
```

## Schema changes

You can edit a DocType to add, remove or change fields. On saving a DocType, a
JSON file containing the DocType data is added to source tree of your app. When
you add an app to a site, the DocTypes are installed (database tables are
created) using this JSON file.

> For making schema changes, you must enable Developer Mode.

On running a `migrate`, all apps migrate to their current version. First, we run the "before_migrate" hook to sync user permissions. Then the actual patches are run, which migrate the various apps. After this, we sync the following components:

- Database Schema
- Background Jobs
- Fixtures ([read more](/framework/user/en/python-api/hooks#fixtures))
- Dashboards, Desktop Icons and Web Pages
- Updates Translations
- Rebuild Search Index for all routes

Particularly for DocTypes, we compare the MD5 hash of each DocType JSON with the hashes we have stored in the DocType database table. If the hashes don't match, we reload the particular DocType. This technique is called checksum comparison, you can learn more about it [here](https://www.computerworld.com/article/2819393/unix-tip--comparing-files-with-checksums.html). Finally, we run a "after_migrate" hook to finish the migration. You can find the commands run for the individual processes at [bench-site-commands](bench/frappe-commands#site-commands)


> Note: Up Until `v13` DocTypes were synced based on the modified timestamps in the JSON file. This method was error-prone so we moved to the more robust hash comparison method. You can read more about it [here](https://github.com/frappe/frappe/pull/14246#issuecomment-928942292)

When you remove or rename fields in the DocType, the corresponding database
columns are not removed from the database table, but they will not be visible in
the form view. This is done to avoid any potential data loss situations and to
allow you write related data migrations (patches) which might need values from
old fields.

> Frappe doesn't support reverse schema migrations.

## Data Migrations

On introducing data related changes, you might want to run one off scripts to
change existing data to match expectations as per new code. We call these scripts **patch** in frappe.

### Writing a patch

To write a patch, you must write an `execute` method in a python script and add
it to `patches.txt` of your app.

It is recommended to make a file with a patch number and name in its path and
add it to a patches package (directory) in your app. You can then add a line
with dotted path to the patch module to `patches.txt`.

The directory structure followed in Frappe is as below

```sh
frappe
└── patches
 └── v12_0
  └── my_awesome_patch.py
```

The patch can then be added to `patches.txt` by its dotted path.
```
frappe.patches.v12_0.my_awesome_patch
```

### Schema during patch

The DocType meta available in the execute function will be as per the old JSON.
This is so that you can write migration code assuming you still have the old fields.
After the patch is run, the new schema is applied to the DocType.

If you want to have the new schema during your patch execution, use the `reload_doc` method.
```py
import frappe

def execute():
 frappe.reload_doc(module_name, "doctype", doctype_name)

 # your patch code here
```

### Post-Model sync patches [v14 / develop branch only]

Often your patch might not require access to database schema before DocType models are synced with database. In such cases it's better to keep the patch in `[post_model_sync]` section of `patches.txt`. 

`patches.txt` supports INI-like file format where two sections specify when a patch should run - before or after doctype schema migration. Post model sync patches do not require reloading any doctypes as all doctypes are reloaded before executing them. Here is example of such patches.txt file:

```python
[pre_model_sync]
app.module.patch1
app.module.patch2

[post_model_sync]
app.module.patch3
app.module.patch4
```


### One off Python statements

You can also add one off python statements in `patches.txt` using the syntax,

```
frappe.patches.v12_0.my_awesome_patch
execute:frappe.delete_doc('Page', 'applications', ignore_missing=True)
```

### Patch execution order

Patches run in the order they are defined. All lines in `patches.txt` have to be
unique. If a patch has been run before, it won't run again. If you want to run a
patch again, add a comment that will make the line appear as new.

For example,

```
frappe.patches.v12_0.my_awesome_patch #2019-09-08
```

<!-- page: framework/framework__user__en__database-optimization-hardware-and-configuration.md -->
---
title: "Database Optimization - Hardware and Configuration"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/database-optimization-hardware-and-configuration"
updated: "2026-05-10"
---

A major part of optimizing performance while using Frappe Framework is optimizing the performance of the database. Thankfully, the performance of MariaDB/MySQL is a well understood concept with many resources to understand it in depth. Frappe is no different from many other web apps that are built on the same database, so if you know how to optimize for MySQL, you already know how to do it when using Frappe Framework.

Architecture and Hardware 
-------------------------

We recommend separating the database server from the application server. The following are some reasons for this recommendation:

* Application server can often have load spikes and dynamic memory usage patterns. Hosting it next to Database server affects overall performance.
* Database like to have consistent availability of hardware resources to perform well. This includes access to as much RAM and IOPS available as possible.
* Database and Application server often benefit from different type of hardware tuning and configuration.

### CPU

We recommend starting with at least 2vCPU. Numbers of vCPU determines how much "true parallel" work your database server can perform. You should setup some monitoring on database server (see monitoring section below). When your utilization is constantly hitting 60% or stays above 50% for prolonged period then you might need to upgrade vCPU count to allow more parallel compute resources.

### RAM

Accessing data from disk is orders of magnitude slower than accessing it from memory. Databases use RAM for "Buffer Pool" which acts as cache for actual data on disk. A well tuned and well equipped database will not be accessing disk for reading data &gt;99% of the time. As your database grows and you need a lot of data accessible very fast then you might have to consider adding more RAM and reconfiguring the server to utilize available RAM.

We recommend starting with at least 8GB RAM.


&gt; Note: It is recommended to not rely on SWAP for database server. Databases already implement all the logic necessary to work with limited memory, adding swap just duplicates that effort. You should keep small amount of SWAP memory for safety but lower swappiness to minimum possible value.
&gt; 
&gt; 

### Disk and IOPS

Do not cheap out on disk storage and IOPS. Consider getting at least 3x storage than what's actually being used. Your database will naturally grow over time and you don't want to upgrade every time it runs out of disk. AWS for instance, also gives you more IOPS with additional storage. We recommend starting with ~2000-3000 IOPS and monitoring usage to check if you need more or can do with less.

Start with at least 50GB disk and consider ~3x of your current database size. E.g. If your database is 20 GB then consider getting a server with 60GB storage or attachable volume.

### Scaling resources

We recommend scaling vertically for as long as possible, roughly this means vertically scaling till at least 64vCPU/128GB RAM. You can use insights from monitoring setup to decide what component needs to be upgraded. Keep in mind that most cloud providers will bundle resources into "instances" so it's not straightforward to just upgrade one part of the system.

If you think you've hit the limit of what you can achieve with single machine then you can consider setting up a database replica. Frappe Framework can be configured to route all the heavy reads to a replica of the database to reduce load on the main server.

Configuration
-------------

Databases provide 100s of knobs out of the box for tweaking different parameters of database performance. It is essential to at least have the most important knobs tuned properly so you can maximize your hardware capabilities.

### Bufferpool - `innodb-buffer-pool-size = 5G`

The most important parameter you need to tweak is Bufferpool size. This also has the worst default configuration for historical reasons, so if it is left unconfigured, you're not utilizing your hardware at all.

Bufferpool as previously mentioned acts as a cache for data present on disk. The rule of thumb for size of Bufferpool is:


&gt; "Bufferpool size should fit your working set of data"
&gt; 
&gt; 

It's simple to state yet quite hard to quantify. Your "working set" of data is data that you access every day, data you want to access really fast and won't accept random slow downs for. Let's take example of ERPs to understand how to pick somewhat ideal bufferpool size and consequently RAM size.

1. Your site has database of 80GB.
2. This database is generated over 4 years.
3. You believe last year the DB size grew by 20GB and in ERPs mostly you're accessing 1 year's data for all kinds of reporting and validations.
4. So ideal bufferpool size to start with is 20GB.
5. Ideally, bufferpool should consume ~60% of RAM. So you should go for 20 / 0.6 ~= 33GB RAM.

You can setup monitoring on bufferpool usage and understand if you need more or less. Two most important metrics:

1. Bufferpool hit ratio: If it's more than 99% then most likely you do not need to add more bufferpool size.
2. Utilization: If your utilization is not close to 95%-100% then you definitely don't need to add more bufferpool.

Bufferpool cache fills up over time, so you need to measure this after few days of operation. You can type `SHOW ENGINE INNODB STATUS` to find these stats. This gives a lot of output but here is the important part:


```
----------------------
BUFFER POOL AND MEMORY
----------------------
Buffer pool size   2790528
Free buffers       1594
Buffer pool hit rate 999 / 1000
  

```
### Other parameters

Following is the configuration we use at Frappe. You can start with this and tweak certain parameters. Most important parameters are explained in some more detail below.

* `innodb-flush-method = O_DIRECT`: Bypass certain operation and do "direct IO".
* `innodb-flush-log-at-trx-commit = 1`: Improves durability of system by writing to log at every commit. Do not compromise on this durability for small gain in performance.
* `innodb-file-per-table = 1` : Create one file for each table.
* `slow-query-log = 1` and `slow-query-log-file = /var/lib/mysql/mysql-slow.log`: Store any query that runs for too long in log file. This is useful for retrospectively finding out which queries should be optimized.
* `query-cache-type = 0` and `query-cache-size = 0`: This disables query cache, which despite the name is now widely considered to be detrimental to performance.


```
[mysqld]
# GENERAL #
default-storage-engine          = InnoDB

# MyISAM #
key-buffer-size                 = 32M
myisam-recover                  = FORCE,BACKUP

# SAFETY #
max-allowed-packet              = 256M
max-connect-errors              = 1000000
innodb                          = FORCE

# DATA STORAGE #
datadir                         = /var/lib/mysql/

# BINARY LOGGING #
log-bin                         = /var/lib/mysql/mysql-bin
log_bin_index                   = /var/lib/mysql/mysql-bin.index
expire-logs-days                = 14
sync-binlog                     = 1

# CACHES AND LIMITS #
tmp-table-size                  = 32M
max-heap-table-size             = 32M
query-cache-type                = 0
query-cache-size                = 0
max-connections                 = 500
thread-cache-size               = 50
open-files-limit                = 65535
table-definition-cache          = 4096
table-open-cache                = 10240
tmp-disk-table-size             = 5120M
max-statement-time              = 10800

# INNODB #
innodb-flush-method             = O_DIRECT
innodb-log-files-in-group       = 2
innodb-log-file-size            = 512M
innodb-flush-log-at-trx-commit  = 1
innodb-file-per-table           = 1
# NOTE: This has to be configured based on RAM. Consider ~60% of available RAM. This example assumes 8GB RAM.
innodb-buffer-pool-size         = 4.8G
innodb-file-format              = barracuda
innodb-large-prefix             = 1
innodb-old-blocks-time          = 5000
collation-server                = utf8mb4_unicode_ci
character-set-server            = utf8mb4
character-set-client-handshake  = FALSE
max_allowed_packet              = 512M

# LOGGING #
log-error                       = /var/lib/mysql/mysql-error.log
log-queries-not-using-indexes   = 0
slow-query-log                  = 1
slow-query-log-file             = /var/lib/mysql/mysql-slow.log

[mysql]
default-character-set           = utf8mb4

[mysqldump]
max_allowed_packet              = 512M
  

```
Monitoring
----------

Frappe doesn't have any specific monitoring tool for MariaDB, we recommend setting up observability tools like Prometheus with Grafana for dashboards.

* Inbuilt slow query log: See how often slow queries get logged and find most common slow queries using tool like `pt-query-digest` from Percona toolkit.
* Set up Prometheus and Grafana with following exporters:


	+ [Node Exporter](https://github.com/prometheus/node_exporter) - Provides overall system stats. Useful for monitoring CPU, RAM and I/O.
	+ [MySQLD Exporter](https://github.com/prometheus/mysqld_exporter) - Provides ton of useful metric from MariaDB's database engine.
	+ [PMM](https://docs.percona.com/percona-monitoring-and-management/setting-up/client/mysql.html) - Percona's toolkit with pre-built dashboards.

We consider following metrics worth tracking:

1. CPU usage - Constant near 100% usage implies you might need more CPU power to handle the load.
2. RAM - RAM usage of well configured database will hover around 90%. Usage close to 100% means you're likely to swap or crash the system. Usage significantly less than 90% implies you are not utilizing all available RAM for bufferpool cache.
3. Disk I/O - Once database server has sufficiently warmed up, disk reads should be minimal. All read load will get served up from bufferpool and only updates need to be written to the disk. If you see a lot of disk I/O that could imply insufficient bufferpool size or queries that require temporary files to be written on disk.
4. "InnoDB row reads" - A sudden increase in number of reads might imply increase in traffic or introduction of unoptimized query.
5. "BP Miss ratio" - Should be &lt;1% for the most part. If it's high then your bufferpool size is likely not adequate.
6. "Innodb Row Lock Wait Load" - A high lock wait load implies you have contention problem where multiple workers are trying write to same resources but getting blocked. Typical solution to this problem is to queue work instead of doing it in parallel. There might also be unoptimized queries causing locks to be held for long durations.
7. "InnoDB Buffer Pool LRU Sub-Chain Churn" - Bufferpool maintains list of database pages as an approximate LRU. Activities like logical backups can potentially read entire database on disk into bufferpool causing eviction of most used pages. It's ideal to take backups during non-working hours to avoid this.

### Further reading and references

* &lt;https://mariadb.com/kb/en/innodb-system-variables/&gt;
* &lt;https://mariadb.com/kb/en/server-system-variables/&gt;
* &lt;https://www.percona.com/blog/innodb-performance-optimization-basics-updated&gt;
* &lt;https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html&gt;
* &lt;https://docs.percona.com/percona-toolkit/&gt;

  

<!-- page: framework/framework__user__en__debugging.md -->
---
title: "Debugging"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/debugging"
updated: "2026-05-10"
---

## Server

When you run the `bench start` command during development, the log from each process of the Procfile is logged in the terminal window.

```
▶ bench start
14:55:17 system | redis_cache.1 started (pid=4085)
14:55:17 system | redis_socketio.1 started (pid=4086)
14:55:17 system | redis_queue.1 started (pid=4088)
14:55:17 system | web.1 started (pid=4089)
14:55:17 system | socketio.1 started (pid=4090)
14:55:17 system | watch.1 started (pid=4094)
14:55:17 system | worker_short.1 started (pid=4096)
14:55:17 system | schedule.1 started (pid=4095)
14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.257 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.264 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4088, just started
14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.264 # Configuration loaded
14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.265 * Increased maximum number of open files to 10032 (it was originally set to 4864).
14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.262 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.268 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4085, just started
14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.268 # Configuration loaded
14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.269 * Increased maximum number of open files to 10032 (it was originally set to 4864).
14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.262 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.270 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4086, just started
14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.270 # Configuration loaded
14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.272 * Increased maximum number of open files to 10032 (it was originally set to 4864).
14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.285 * Running mode=standalone, port=11002.
14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.285 # Server initialized
14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.286 * Ready to accept connections
14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.287 * Running mode=standalone, port=13002.
14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.292 # Server initialized
14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.292 * Ready to accept connections
14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.294 * Running mode=standalone, port=12002.
14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.294 # Server initialized
14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.295 * Ready to accept connections
14:55:17 system | worker_long.1 started (pid=4098)
14:55:17 system | worker_default.1 started (pid=4100)
14:55:18 socketio.1 | listening on *: 9002
14:55:20 socketio.1 | { Error: connect ECONNREFUSED 0.0.0.0:8002
14:55:20 socketio.1 | at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1191:14)
14:55:20 socketio.1 | errno: 'ECONNREFUSED',
14:55:20 socketio.1 | code: 'ECONNREFUSED',
14:55:20 socketio.1 | syscall: 'connect',
14:55:20 socketio.1 | address: '0.0.0.0',
14:55:20 socketio.1 | port: 8002,
14:55:20 socketio.1 | response: undefined }
14:55:24 web.1 | * Running on http://0.0.0.0:8002/ (Press CTRL+C to quit)
14:55:24 web.1 | * Restarting with fsevents reloader
14:55:24 watch.1 | yarn run v1.10.1
14:55:24 watch.1 | $ node rollup/watch.js
14:55:25 web.1 | * Debugger is active!
14:55:25 web.1 | * Debugger PIN: 321-355-865
14:55:26 watch.1 |
14:55:26 watch.1 | Rollup Watcher Started
14:55:26 watch.1 |
14:55:26 watch.1 | Watching...
14:55:26 watch.1 | Rebuilding frappe-web.css
14:55:27 watch.1 | Rebuilding frappe-web-b4.css
14:55:27 watch.1 | Rebuilding chat.js
14:55:28 web.1 |
14:55:28 web.1 | test print
  

```

When you write any print statements in your python code, it will show up in the `web:` process log if it is a request/response, or in one of `worker_` processes if the code runs in a background job.

&gt; If you are a VSCode user, you can debug right in your editor by setting breakpoints in your code. Follow these [steps](Debugging in VS Code / Debug Adapter Protocol) to set it up.

### Logging

In case you're running production, you'd need logs all the more to keep track of as much information about your Frappe environment.

Out of the box, logs are stored under the `./logs` folder in your bench. From Frappe Version 13, logs are available at site level too, under `./sites/{site}/logs`.

These site logs are created by the Frappe Application, while many of the bench level log files are generated by the processes that support your Frappe environment. Checkout `Procfile` or `supervisor.conf` in your bench for more information.

&gt; Learn more about Frappe Logs [here](/framework/v14/user/en/logging) and the Frappe Logging API from [here](/framework/v14/user/en/api/logging).

### Console

To play with Python API, bench provides an iPython shell. After you run the following command, it will import frappe, initialize it and also connect to database.

```
▶ bench --site [sitename] console

In [1]: frappe.get_doc('Task', 'TASK00004')
Out[1]: &lt;erpnext.projects.doctype.task.task.task at="" 0x10825d710=""&gt;
  

```

## Client

Client side debugging is as simple as adding a `debugger` statement in your JS file. You must open your DevTools in your browser for it to pause on the statement.

```
frappe.db.get_value('Task', 'TASK00004', 'status')
    .then(values =&gt; {
        debugger
        console.log(values);
    })
  

```

### Console

To play with Client API, you can open your browser's console and use the globally available `frappe` object to explore and run methods and access properties.

[Screenshot on the live page: Browser Console]

 *Browser Console*

&gt; Learn more about the Client API [here](/framework/v14/user/en/api#javascript) &lt;/erpnext.projects.doctype.task.task.task&gt;

## Debugging in VS Code / Debug Adapter Protocol

[Screenshot on the live page: vsc debugging]

Checklist for proper functioning.

- Update `Procfile`
- Get Visual Studio Code (duh!)
- Install [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Update `launch.json`
- Start Debugging

Caveats:

1. Disables Auto Reload Feature (However You can achieve the same results by manual reload (⌘⇧F5))
2. Disables Werkzeug Multithreading

**1. Update** `Procfile`

*Caution: This modifies the behaviour of* `bench start`

Comment out a line (prepend # to it) from the `Procfile` (located in the bench directory) that looks like this.

```
web: bench serve --port 8000
  

```

We will run this process from VS code instead of running it with `bench start`.

**2. Update** `launch.json` Add a configuration to your `launch.json` in VS Code that should look something like this (This more or less does exactly what the removed line from Procfile does).

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Bench",
            "type": "python",
            "request": "launch",
            "justMyCode": false,
            "program": "${workspaceFolder}/frappe/frappe/utils/bench_helper.py",
            "args": [
             "frappe", "serve", "--port", "8000", "--noreload", "--nothreading"
            ],
            "python": "${workspaceFolder}/../env/bin/python",
            "cwd": "${workspaceFolder}/../sites",
            "env": {
             "DEV_SERVER": "1"
            }
        }
    ]
}
```

Paths mentioned in given configuration assumes that you have `apps` directory as your workspace directory (The directory you open `code` with). `workspaceFolder` is a vs code variable that points to (if it's not obvious from its name) workspace directory.

You are not forced to use `apps` as your workspace directory, however do remember to change `workspaceFolder`, `pythonPath` and `cwd` accordingly.

**3. Execute** `bench start`

This should be kept running as usual.

**4. Start debugging**

VS Code -&gt; Debug Panel (⌘⇧D) -&gt; Start Debugging or With a keyboard shortcut(⌘⇧F5).

### Explanation

**1.** `program` and `args`

```
"program": "${workspaceFolder}/frappe/frappe/utils/bench_helper.py",
"args": ["frappe", "serve", "--port", "8000", "--noreload", "--nothreading"],
  

```

Does exact same thing as `bench serve --port 8000 --noreload --nothreading` which is same as

```
cd sites
../env/bin/python ../apps/frappe/frappe/utils/bench_helper.py frappe serve  --port 8000 --noreload --nothreading
  

```

`--noreload` diasbles werkezeug's autoreload fetaure and `--nothreading` disables multithreading.

**2.** `cwd`

```
"cwd": "${workspaceFolder}/../sites",
  

```

Above command must be executed from `sites` directory.

**3.** `env`

```
"env": {
    "DEV_SERVER": "1"
}
  

```

`bench start` creates an environment variable `DEV_SERVER` and set it to `1`. Socket.io doesn't work correctly without this (long story).

Running only `bench serve` doesn't set this variable so you need to explicitly set it.

**Note:**

Currently, frappe runs with `use_reloader=True` and `threaded=True`, VS Code Debugger for some reason doesn't play well with these features, [Django and Flask](https://code.visualstudio.com/docs/python/debugging#_debugging-specific-app-types) also have this problem.

<!-- page: framework/framework__user__en__desk.md -->
---
title: "Desk\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk"
updated: "2026-02-17"
---


Frappe Framework comes with a rich admin interface called the Desk. It reads meta-data
from DocTypes and automatically builds list views, form views, report views, etc
for your DocTypes. Desk is to be used by users of the type "System User".

In this section we will discuss what views are provided by Desk and how to configure them.

- [Workspace](#workspace)
- [Awesomebar](#awesomebar)
- [List View](#list-view)
- [Form View](#form-view)
- [Grid View](#grid-view)
- [Report Builder](#report-builder)
- [Tree View](#tree-view)
- [Calendar View](#calendar-view)
- [Gantt View](#gantt-view)
- [Kanban View](#kanban-view)
- [Desk Theme](#dark-theme)

## Workspace

When you login, you're presented with the Desk, it features a persistent sidebar with some standard items based on app modules.
Each sidebar item links to a page called Workspace.

[About Workspace →](/framework/v14/user/en/desk/workspace)

[Screenshot on the live page: Desktop]

## Awesomebar

Awesomebar helps you to navigate anywhere in the system, create new records, search in documents
and even perform math operations.

[Screenshot on the live page: Awesomebar]
*Navigating ToDo using Awesomebar*

## List View

List View is generated for all DocTypes except which are Child Tables and Singles.

The List view is packed with features. Some of them are:

1. Filters
1. Sorting
1. Paging
1. Filter by tags
1. Switch view to Report, Calendar, Gantt, Kanban, etc.

> Learn more about the [List API](/framework/v14/user/en/api/list).

## Form View

Form view is used to view the records in a Form Layout. This view has a lot of
things going on. But the primary purpose of it is to view and edit records.
A document can be assigned to or shared with other users and it can have arbitrary
attachments and tags, all of which can be seen in the form sidebar.

[Screenshot on the live page: Form View]
*Form View*

When you scroll down to the bottom of the form, you will see the form timeline.
The form timeline shows emails, comments, edits and other events in a reverse
chronological order.

[Screenshot on the live page: Form View]
*Form Timeline*

> Learn more about the [Form API](/framework/v14/user/en/api/form).

## Grid View

Grid view is used as a table in the form view to insert multiple records.
User can configure the columns of the grid view from the form.

[Screenshot on the live page: Grid View]


## Report Builder

Report Builder is a generic tool to customize and build tabular data from a DocType.
You can select columns to show, filters to apply, sort order and save this configuration
by giving your report a name. You can also show Child Table data and also filter
documents by their child records. You can also apply *Group By* on a column with
aggregation methods like Count, Sum and Average.

[Screenshot on the live page: Report Builder]
*Report Builder Features*

## Tree View

Frappe also supports tree structured records using the [Nested set model](https://en.wikipedia.org/wiki/Nested_set_model).
If a doctype is configured to be a tree structure, it can be viewed in the Tree view.

[Screenshot on the live page: Tree View]
*Tree View*

## Calendar View

Calendar view can be configured for DocTypes with a start date and end date.

[Screenshot on the live page: Calendar View]
*Calendar View*

The configuration file should be named `{doctype}_calendar.js` and should exist in the
doctype directory.

Here is an example configuration file for calendar view for Event doctype, which must be set in the `event_calendar.js` file.

```js
frappe.views.calendar['Event'] = {
 field_map: {
 start: 'starts_on',
 end: 'ends_on',
 id: 'name',
 allDay: 'all_day',
 title: 'subject',
 status: 'event_type',
 color: 'color'
 },
 style_map: {
 Public: 'success',
 Private: 'info'
 },
 order_by: 'ends_on',
 get_events_method: 'frappe.desk.doctype.event.event.get_events'
}
```

## Gantt View

Gantt view uses the same configuration file as calendar, so every DocType that has a Calendar view has a Gantt view too.

In case certain settings need to be overridden for the Event DocType's Gantt view (for example the `order_by` field) the configuration can be set in the `event_calendar.js` file with the following content.

```js
frappe.views.calendar['Event'] = {
 field_map: {
 start: 'starts_on',
 end: 'ends_on',
 id: 'name',
 allDay: 'all_day',
 title: 'subject',
 status: 'event_type',
 color: 'color'
 },
 gantt: { // The values set here will override the values set in the object just for Gantt View
 order_by: 'starts_on',
 }
 style_map: {
 Public: 'success',
 Private: 'info'
 },
 order_by: 'starts_on',
 get_events_method: 'frappe.desk.doctype.event.event.get_events'
}
```

[Screenshot on the live page: Gantt View]
*Gantt View*

## Kanban View

Kanban view can be created for any DocType that has a Select field with options.
These options become the column names for the Kanban Board.

[Screenshot on the live page: Kanban View]

## Dark Theme

[Screenshot on the live page: Dark Theme]

Frappe Framework has a first class support of dark theme. To switch the theme, click on your avatar on top right of the screen and click on "Toggle Theme". Once you click "Toggle Theme", you'll see following modal from which you can easily switch between available themes. To switch to dark theme select "Timeless Night".

[Screenshot on the live page: Desk Theme Modal]

**Note:** You can also press CTRL + SHIFT + G to open this modal.

<!-- page: framework/framework__user__en__desk__attachments.md -->
---
title: "Attachments"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/attachments"
updated: "2026-02-17"
---

Frappe allows attachment of files to documents. Users with **Read** permissions on a particular document will also be able to access the files attached to it. Users can also access the File Manager from the sidebar.

[Screenshot on the live page: attachments-sidebar]  


How to Attach a New File
------------------------

There are several ways to attach a file to a document.

### Select File

[Screenshot on the live page: attach-from-disk]  


### Drag and Drop

[Screenshot on the live page: 2023-08-28 13.28.01]  


### Uploaded File

Attach a file a that was previously uploaded, to a different document.

[Screenshot on the live page: 2023-08-28 13.33.07]  


### Web Link

If you use a separate server for files or use online services like Dropbox or Docs, you can attach a file by providing a link to it.

[Screenshot on the live page: 2023-08-28 13.34.48]  


### Camera

Attach Images by taking a photo using your device's camera.

[Screenshot on the live page: Camera]  


File Manager
------------

All the attached files are listed in the File Manager. You can access these by navigating here:

**Home > Tools > Files**

[Screenshot on the live page: Screenshot 2023-07-31 at 8.01.55 PM]  


Import Zip
----------

You can also bulk import multiple files at once using the Import Zip feature.

1. Go to **File List > Menu > Import Zip**.
2. Upload a zip file.
3. After the zip file is uploaded, it's contents will be extracted and each file will be created as a new File record.

[Screenshot on the live page: Importing files from zip]  



> Note: Hidden files (files starting with `.`) are not extracted when importing from a zip file.
> 
> 

Export as Zip
-------------

You can also bulk export multiple files at once using the Export as Zip feature.

1. Go to **File List**.
2. Select multiple files.
3. Click on Actions > Export as zip.
4. After the zip file is downloaded, you can import it in another site using Import Zip feature or send it across via email.

[Screenshot on the live page: Export files as zip]  


Cropping Images
---------------

You can crop `.jpeg` and `.png` images by clicking on the crop icon.

[Screenshot on the live page: Cropping images on upload]  


Optimizing Images
-----------------

Images can be optimized to reduce their file size. Currently optimizing an image does the following:

1. Resizes it to fit a max-width of 1920px and a max-height of 1080px, while preserving the aspect ratio
2. Uses optimal encoder settings
3. Reduces the quality to 85%

**Toggle optimization during upload**

[Screenshot on the live page: Toggle image optimization]  


**Optimize an already uploaded image**

[Screenshot on the live page: Optimize saved image]  


Limits
------

A limit of 10MB is applicable on file size per attachment by default. For self-hosted users, this can be changed by setting `max_file_size` in your site's configuration file.

### Attachments per Document

You can limit how many files can be attached to a specific document.

#### Step 1: Navigate to Customize Form


> Home > Customization > Customize Form
> 
> 

#### Step 2: Select Document Type

Select the document type for which you'd like to set this limit.

[Screenshot on the live page: Select Document Type]  


#### Step 3: Set Limit

Set the value of **Max Attachments** to the maximum number of attachments allowed for this document type.

[Screenshot on the live page: Set Limit]  


Once you're satisfied with the changes, click the **Update** button. That's it! The maximum number of attachments per document will now be validated every time a new attachment is added to a document of this type.

<!-- page: framework/framework__user__en__desk__printing.md -->
---
title: "Printing"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/printing"
updated: "2026-02-17"
---

Frappe framework has first class support for generating print formats for documents and also convert them into PDF. Frappe uses [Jinja](http://jinja.pocoo.org/docs/2.10/) as the templating language for print formats.

Print View
----------

The Print View can be accessed from the form view of any document. A Standard print format is generated for all DocTypes based on the form layout and mandatory fields in it. [Screenshot on the live page: Print View] *Print View*

Print Format Builder
--------------------

To Customize a print format you need to create a copy of the Standard Print format and customize it using the Print Format Builder. These print formats are user editable and are not bundled with the app as files.

[Screenshot on the live page: Print Format Builder] *Print Format Builder*

#### Custom HTML

You can also add Custom HTML to your Print Format. Just drag and drop the Custom HTML button in left sidebar into your Print Format Editor.

In the Custom HTML field you can use any valid HTML with [Bootstrap 3 classes](https://getbootstrap.com/docs/3.3/css/) for styling. You can also use [Jinja Templating](http://jinja.pocoo.org/docs/2.10/) to add dynamic content to your HTML. See [list of methods](/framework/v14/user/en/api/jinja) available to use in Jinja templates.

[Screenshot on the live page: Custom HTML] *Custom HTML*

#### Custom CSS

To change styling in your Print Format you can also add custom CSS.

> Click on Customize > Edit Properties to add Custom CSS

[Screenshot on the live page: Custom CSS] *Custom CSS*

[Screenshot on the live page: Custom CSS Preview] *Custom CSS Preview*

Advanced Print Formats
----------------------

Print Format Builder is limited if you want to completely change the layout of the Print Format. You can also write your own HTML from scratch and build the print layout you want.

To create a new Print Format, type "new print format" in awesomebar and hit enter.

1. Select a unique name for your format.
2. Set "Standard" as "No".
3. Check "Custom Format".
4. Select Print Format Type as "Jinja"
5. Write your custom HTML

> If you set Standard as "Yes" and Developer Mode is enabled, then a JSON file > will be generated for your Print Format and you will have to check it in to > your version control with your app.

[Screenshot on the live page: Custom HTML in Print Format] *Custom HTML in Print Format*

Print Formats for Reports
-------------------------

Frappe allows you to create custom Print Formats for your Query and Script Reports. These print formats cannot be created using the UI.

To create a Print Format for reports, create a HTML file named `{report-name}.html` in the Report folder.

For example, check [General Ledger](https://github.com/frappe/erpnext/tree/develop/erpnext/accounts/report/general_ledger)

#### JS Templating

These print formats are generated on the client side, so we can't use Jinja. We use an adapted version of [John Resig's Templating](https://johnresig.com/blog/javascript-micro-templating/). It looks similar to Jinja so you don't need to learn anything new.

Here's a snippet of JS Template.


```
{% for(var i=0, l=data.length; i<l; i++) { %}
    <tr>
    {% if(data[i].posting_date) { %}
        {%= frappe.datetime.str_to_user(data[i].posting_date) %}
        
            {% if(!(filters.party || filters.account)) { %}
                {%= data[i].party || data[i].account %}
                <br>
            {% } %}

            {{ __("Against") }}: {%= data[i].against %}
            <br>{%= __("Remarks") %}: {%= data[i].remarks %}
            
    {% } else { %}
        <b>{%= frappe.format(data[i].account, {fieldtype: "Link"}) || "&nbsp;" %}</b>
        
 {%= data[i].account &amp;&amp; format_currency(data[i].debit, filters.presentation_currency) %}
 
 {% } %}
 
{% } %}
```
  

<!-- page: framework/framework__user__en__desk__reports.md -->
---
title: "Introduction"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports"
updated: "2026-02-17"
---

## What is Frappe Framework?

Frappe, pronounced *fra-pay*, is a full stack, batteries-included, web framework written in Python and Javascript with MariaDB as the database. It is the framework which powers [ERPNext](https://erpnext.com), is pretty generic and can be used to build database driven apps.

<div align="center">
	[Screenshot on the live page]
</div>

## Why Frappe?

The key difference in Frappe compared to other frameworks is that **meta-data** is also treated as data. This enables you to build front-ends very easily. We believe in a monolithic architecture, so Frappe comes with almost everything you need to build a modern web application. It has a full featured Admin UI called the Desk that handles forms, navigation, lists, menus, permissions, file attachment and much more out of the box. [Read more here](/framework/user/en/basics/why).

## Key Features

1. Full-Stack Framework: Frappe covers both front-end and back-end development, allowing developers to build complete applications using a single framework.
2. Built-in Admin Interface: Provides a pre-built, customizable admin dashboard for managing application data, reducing development time and effort.
3. Role-Based Permissions: Comprehensive user and role management system to control access and permissions within the application.
4. REST API: Automatically generated RESTful API for all models, enabling easy integration with other systems and services.
5. Customizable Forms and Views: Flexible form and view customization using server-side scripting and client-side JavaScript.
6. Report Builder: Powerful reporting tool that allows users to create custom reports without writing any code.

## Installation

Before you can use Frappe, you need to install it. We have a complete [installation guide](/framework/user/en/installation) which covers all possibilities, this guide will also help you understand the backend stack.

## Learning and community

1. [Frappe School](https://school.frappe.io/lms/courses) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [GitHub](https://github.com/frappe/frappe) - Explore the source code, contribute, and collaborate with the Frappe community.
3. [Discussion Forum](https://discuss.frappe.io/c/framework/5) - Hang out with our growing community on our forum, ask questions, help others and be a part of the community.
4. [buildwithhussain.dev](https://youtube.com/@buildwithhussain) - Watch Frappe Framework being used in the wild to build world-class web apps.
