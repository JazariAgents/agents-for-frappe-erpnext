<!-- Frappe documentation: framework, part 4 of 6. Index: docs/INDEX.md -->

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

![Browser Console](/files/client-side-debugging.png)

 *Browser Console*

&gt; Learn more about the Client API [here](/framework/v14/user/en/api#javascript) &lt;/erpnext.projects.doctype.task.task.task&gt;

## Debugging in VS Code / Debug Adapter Protocol

![vsc debugging](/files/vsc_debuggin.png)

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

![Desktop](/files/v14-workspace.png)

## Awesomebar

Awesomebar helps you to navigate anywhere in the system, create new records, search in documents
and even perform math operations.

![Awesomebar](/files/awesomebar.png)
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

![Form View](/files/form-view.png)
*Form View*

When you scroll down to the bottom of the form, you will see the form timeline.
The form timeline shows emails, comments, edits and other events in a reverse
chronological order.

![Form View](/files/form-timeline.png)
*Form Timeline*

> Learn more about the [Form API](/framework/v14/user/en/api/form).

## Grid View

Grid view is used as a table in the form view to insert multiple records.
User can configure the columns of the grid view from the form.

![Grid View](/files/configure_grid_columns.gif)


## Report Builder

Report Builder is a generic tool to customize and build tabular data from a DocType.
You can select columns to show, filters to apply, sort order and save this configuration
by giving your report a name. You can also show Child Table data and also filter
documents by their child records. You can also apply *Group By* on a column with
aggregation methods like Count, Sum and Average.

![Report Builder](/files/report-builder.gif)
*Report Builder Features*

## Tree View

Frappe also supports tree structured records using the [Nested set model](https://en.wikipedia.org/wiki/Nested_set_model).
If a doctype is configured to be a tree structure, it can be viewed in the Tree view.

![Tree View](/files/tree-view.png)
*Tree View*

## Calendar View

Calendar view can be configured for DocTypes with a start date and end date.

![Calendar View](/files/calendar-view.png)
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

![Gantt View](/files/gantt-view.png)
*Gantt View*

## Kanban View

Kanban view can be created for any DocType that has a Select field with options.
These options become the column names for the Kanban Board.

![Kanban View](/files/kanban-view.png)

## Dark Theme

![Dark Theme](/files/Screenshot 2022-01-18 at 3.35.44 PM.png)

Frappe Framework has a first class support of dark theme. To switch the theme, click on your avatar on top right of the screen and click on "Toggle Theme". Once you click "Toggle Theme", you'll see following modal from which you can easily switch between available themes. To switch to dark theme select "Timeless Night".

![Desk Theme Modal](/files/Screenshot 2022-01-18 at 3.47.33 PM.png)

**Note:** You can also press CTRL + SHIFT + G to open this modal.

<!-- page: framework/framework__user__en__desk__attachments.md -->
---
title: "Attachments"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/attachments"
updated: "2026-02-17"
---

Frappe allows attachment of files to documents. Users with **Read** permissions on a particular document will also be able to access the files attached to it. Users can also access the File Manager from the sidebar.

![attachments-sidebar](/files/attachments-sidebar.png "attachments-sidebar.png")  


How to Attach a New File
------------------------

There are several ways to attach a file to a document.

### Select File

![attach-from-disk](/files/attach-from-disk.gif "attach-from-disk.gif")  


### Drag and Drop

![2023-08-28 13.28.01](/files/2023-08-28 13.28.01.gif "2023-08-28 13.28.01.gif")  


### Uploaded File

Attach a file a that was previously uploaded, to a different document.

![2023-08-28 13.33.07](/files/2023-08-28 13.33.07.gif "2023-08-28 13.33.07.gif")  


### Web Link

If you use a separate server for files or use online services like Dropbox or Docs, you can attach a file by providing a link to it.

![2023-08-28 13.34.48](/files/2023-08-28 13.34.48.gif "2023-08-28 13.34.48.gif")  


### Camera

Attach Images by taking a photo using your device's camera.

![Camera](/files/file_uploader_camera.gif)  


File Manager
------------

All the attached files are listed in the File Manager. You can access these by navigating here:

**Home > Tools > Files**

![Screenshot 2023-07-31 at 8.01.55 PM](/files/Screenshot 2023-07-31 at 8.01.55 PM.png "Screenshot 2023-07-31 at 8.01.55 PM.png")  


Import Zip
----------

You can also bulk import multiple files at once using the Import Zip feature.

1. Go to **File List > Menu > Import Zip**.
2. Upload a zip file.
3. After the zip file is uploaded, it's contents will be extracted and each file will be created as a new File record.

![Importing files from zip](/files/import_zip.gif)  



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

![Export files as zip](/files/export-as-zip.png)  


Cropping Images
---------------

You can crop `.jpeg` and `.png` images by clicking on the crop icon.

![Cropping images on upload](/files/crop_image.gif)  


Optimizing Images
-----------------

Images can be optimized to reduce their file size. Currently optimizing an image does the following:

1. Resizes it to fit a max-width of 1920px and a max-height of 1080px, while preserving the aspect ratio
2. Uses optimal encoder settings
3. Reduces the quality to 85%

**Toggle optimization during upload**

![Toggle image optimization](/files/toggle_image_optimization.gif)  


**Optimize an already uploaded image**

![Optimize saved image](/files/optimize_saved_image.gif)  


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

![Select Document Type](/files/select_document_type.png)  


#### Step 3: Set Limit

Set the value of **Max Attachments** to the maximum number of attachments allowed for this document type.

![Set Limit](/files/set_max_attachments.png)  


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

The Print View can be accessed from the form view of any document. A Standard print format is generated for all DocTypes based on the form layout and mandatory fields in it. ![Print View](/files/print-view.png) *Print View*

Print Format Builder
--------------------

To Customize a print format you need to create a copy of the Standard Print format and customize it using the Print Format Builder. These print formats are user editable and are not bundled with the app as files.

![Print Format Builder](/files/print-format-custom.gif) *Print Format Builder*

#### Custom HTML

You can also add Custom HTML to your Print Format. Just drag and drop the Custom HTML button in left sidebar into your Print Format Editor.

In the Custom HTML field you can use any valid HTML with [Bootstrap 3 classes](https://getbootstrap.com/docs/3.3/css/) for styling. You can also use [Jinja Templating](http://jinja.pocoo.org/docs/2.10/) to add dynamic content to your HTML. See [list of methods](/framework/v14/user/en/api/jinja) available to use in Jinja templates.

![Custom HTML](/files/print-format-custom-html.png) *Custom HTML*

#### Custom CSS

To change styling in your Print Format you can also add custom CSS.

> Click on Customize > Edit Properties to add Custom CSS

![Custom CSS](/files/print-format-custom-css.png) *Custom CSS*

![Custom CSS Preview](/files/print-format-custom-css-preview.png) *Custom CSS Preview*

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

![Custom HTML in Print Format](/files/advanced-print-format.png) *Custom HTML in Print Format*

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
	<img src="/files/hero-image.png" style="margin: 0 0 0 0;">
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

<!-- page: framework/framework__user__en__desk__reports__query-report.md -->
---
title: "Query Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/query-report"
updated: "2026-04-21"
---

Query Reports are reports that can be generated using a single SQL query. The
query can be simple or complex as long as it generates columns and records.
These reports can only be created by a System Manager and are stored in the database.

To create a Query Report, type "new report" in the awesomebar and hit enter.

1. Set Report Type as "Query Report"
2. Set the Reference DocType - Users that have access to the Reference DocType will have access to the report
3. Set the Module - The report will appear in the "Custom Reports" section of the module.
4. Write your query

> If you set Standard as "Yes" and Developer Mode is enabled, then a JSON file
> will be generated which you will have to check in to your version control. You
> should do this only if you want to bundle Query Reports with your app. The
> Module will decide where the JSON file will go.

![New Query Report](/files/query-report-example-1.png)

### Columns and Filters

> Added in Version 13

You can configure the columns and filters in the Report document. Here you can set the label, width, format (fieldtype) for the columns and filters.

Filters can be used as formatting variables in the query. For example a filters of type `customer` can be used as `%(customer)s` in the query.

![Standard Columns and Filters](/files/report-columns-filters.png)

#### Example

```sql
SELECT
 name, creation, production_item, qty, produced_qty, company
FROM
 `tabWork Order`
WHERE
 docstatus=1
 AND ifnull(produced_qty,0) < qty
```

### Formatting columns (Old Style)

Alternatively columns can also be formatted by specifying the label of the column in a particular format: `{label}:{optional fieldtype}{optional /}{optional options}:{optional width}`

If you have configured the fields and columns in the Report itself, you do not need to use this style.

#### Example (Old Style)

Here is what a query may look like:

```sql
SELECT
 `tabWork Order`.name as "Work Order:Link/Work Order:200",
 `tabWork Order`.creation as "Date:Date:120",
 `tabWork Order`.production_item as "Item:Link/Item:150",
 `tabWork Order`.qty as "To Produce:Int:100",
 `tabWork Order`.produced_qty as "Produced:Int:100",
 `tabWork Order`.company as "Company:Link/Company:"
FROM
 `tabWork Order`
WHERE
 `tabWork Order`.docstatus=1
 AND ifnull(`tabWork Order`.produced_qty,0) < `tabWork Order`.qty
 AND NOT EXISTS (SELECT name from `tabStock Entry` where work_order =`tabWork Order`.name)
```

If you notice there is a special syntax for each column, we use this information
to format the Report View.

For example: The first column `Work Order:Link/Work Order:200` will be rendered
as a Link Field with the DocType Work Order and the column width would be 200px.

![Query Report View](/files/query-report-example-2.png)
*Query Report View*

<!-- page: framework/framework__user__en__desk__reports__report-builder.md -->
---
title: "Report Builder\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/report-builder"
updated: "2026-02-17"
---


Report Builder is the simplest type of Report and can be created without any
code. It will only show the records of single DocType as well as child records of
Child Tables.

#### Saving Reports

By default a Report View is generated for all DocTypes. The user can also save
multiple Reports based on different combination of filters, ordering, columns,
etc.

![Report Builder](/files/report-builder.gif)
*Report Builder*

#### Updating or Deleting Custom Reports

Any custom report created by a user using Report Builder can be then updated or deleted by them from the Report View.

![Update or Delete a Custom Report](/files/N67ee2X.gif)
*Update or Delete a Custom Report*

#### Printing

Reports can be printed from the Menu.

![Report Builder Print](/files/report-builder-print.gif)
*Report Builder Print*

#### Group By

You can also apply group by clause on columns and use aggregate functions like Count, Sum and Average.

![Report Builder Group By](/files/report-builder-group-by.gif)
*Report Builder Group By*

#### Keyboard Navigation and Editing

Since report builder is a view of single DocType, they can also be edited.

![Report Builder Editing](/files/report-builder-editing.gif)
*Report Builder Editing*

<!-- page: framework/framework__user__en__desk__reports__script-report.md -->
---
title: "Script Report\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/reports/script-report"
updated: "2026-07-22"
---

Anything that can't be achieved using Report Builder or Query Report can be  
achieved using Script Reports. As the name suggests, these reports are built  
using Python scripts. Since these reports give you unrestricted access via  
Python scripts, they can only be created by Administrators. These reports are  
meant to be written during development and be a part of your app.

> To create Script Reports you must enable Developer Mode.

To create a Script Report, type "new report" in the awesomebar and hit enter.

1. Set Report Type as "Script Report"
2. Set "Is Standard" as "Yes"
3. Select the Module in which you want to add this report
4. In the module folder (for example if it is Accounts in ERPnext the folder
  ill be `erpnext/accounts/report/[report-name]`) you will see that templates  
  or the report files will be created.
5. Write your python script in the generated `{report-name}.py` file.
6. You can add filters to your report by adding them to `{report-name}.js`

![](/files/Screenshot 2026-07-01 at 15-32-20 Balance Sheet.webp)
*Script Report*

### Standard and Custom Reports

> Added in Version 12

Verson 12 onwards, you can make custom Query and Script reports in Frappe Framework. In custom reports, the script can be added directy in the Report itself and you can use the [Script API](/framework/v14/user/en/desk/scripting/script-api) functions of Frappe Framework.

### Columns and Filters

> Added in Version 13

You can configure the columns and filters in the Report document. Here you can set the label, width, format (fieldtype) for the columns and filters.

Filters can be used as formatting variables in the query. For example a filters of type `customer` can be used as `%(customer)s` in the query.

![](/files/Screenshot 2026-07-01 at 15-33-52 Test Report.webp)

### Writing the script

#### Custom Report

In custom reports, you can use the [Script API](/framework/v14/user/en/desk/scripting/script-api) and write the script directly in the Code section.

```python
return frappe.db.get_all('User', ['first_name', 'last_name'], filters = filters)
```

#### Standard Report

The generated `.py` file comes with a boilerplate for your report. There is one method named `execute` which takes `filters` and returns `columns` and `data`. You can use any combination of python modules and SQL queries to generate your report. The `execute` function looks like this

```python
from __future__ import unicode_literals
# import frappe

def execute(filters=None):
 columns, data = [], []
 return columns, data

```

The `execute` function is supposed to return the `columns` and the `data` to be shown in the report by default. A developer can optionally return a few paramters like `message`, `chart`, `report_summary`, `skip_total_rows`.

The following are the parameters that can be returned by the execute function

#### columns

This is a list of dictionaries. This holds all the columns that are to be displayed in the datatable in an order.

**Note:** You only need to return columns if you have not specified them in the Report

Example:

```python
columns = [
 {
 'fieldname': 'account',
 'label': _('Account'),
 'fieldtype': 'Link',
 'options': 'Account'
 },
 {
 'fieldname': 'currency',
 'label': _('Currency'),
 'fieldtype': 'Link',
 'options': 'Currency'
 },
 {
 'fieldname': 'balance',
 'label': _('Balance'),
 'fieldtype': 'Currency',
 'options': 'currency'
 }
 ]
```

#### Results

This can be a list of lists or a list of dictionaries. This holds the data to be displayed in the report

Example:

```python
data = [
 {
 'account': 'Application of Funds (Assets)',
 'currency': 'INR',
 'balance': '15182212.738'
 },
 {
 'account': 'Current Assets - GTPL',
 'currency': 'INR',
 'balance': '17117932.738'
 },
 ...
 ]
```

#### chart

Contains the configuration for the default chart to be shown in the report.

#### report_summary

This is a list of dictionaries that stores the important values in the report and is shown separately in the top section on the UI.

Example:

```python
[{
 "value": profit,
 "indicator": "Green" if profit > 0 else "Red",
 "label": _("Total Profit This Year"),
 "datatype": "Currency",
 "currency": "INR"
}]
```

> Note: These arguments are supposed to be returned in the specific order as follows

Here is a script report from ERPNext: [Balance Sheet](https://github.com/frappe/erpnext/blob/develop/erpnext/accounts/report/balance_sheet/balance_sheet.py)

#### Adding filters

To add filters in your report define the fields and their fieldtypes in the  
`{report-name}.js` file. The filter values will be available in the `execute`  
method as a dict.

```js
frappe.query_reports['Balance Sheet'] = {
 filters: [
 {
 fieldname: 'company',
 label: __('Company'),
 fieldtype: 'Link',
 options: 'Company',
 default: frappe.defaults.get_user_default('company')
 },
 {
 fieldname: 'periodicity',
 label: __('Periodicity'),
 fieldtype: 'Select',
 options: [
 'Monthly',
 'Quarterly',
 'Half-Yearly',
 'Yearly'
 ],
 default: 'Yearly',
 depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
 }
 ]
}
```

Similar to the `depends_on` property that controls the display of fields, in  
Version 13 we have introduced `depends_on` for Script Report filters. This can  
be used to determine whether the filter will be visible based on the value of the  
condition in `depends_on`.

![](/files/Screenshot 2026-07-01 at 15-28-33 Balance Sheet.webp)
*Balance Sheet*

![](/files/Screenshot 2026-07-01 at 15-28-38 Balance Sheet.webp)
*Balance Sheet*



> *Protip*: To navigate directly to a Report of any of the above type, type its  
> name in the awesomebar and hit enter.



## Snapshot Reports

An advanced report generation engine. It requires manually rewriting report to use OLAP databases.



1. Enable 'Snapshot Report' in System Settings -> Advanced. This sets up a background job that syncs data from MariaDB to DuckDB
  ![](/files/Screenshot 2026-07-22 at 16-22-22 System Settings.webp)
2. Enable 'Snapshot Report' checkbox in Report master
  ![](/files/Screenshot 2026-07-22 at 16-23-07 Trial Balance.webp)
3. Rewrite the report using the `execute_snapshot_report` method in your report module.

```python
def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.
    
    This is the main entry point for snapshot report. When 'Synced
    Report' is enabled in report, framework will call this method 
    every time the report is refreshed or a filter is updated. It 
    accepts the same filters as normal execute. But a utility method - 
    get_latest_sync, is also imported.
    """

    from frappe.database.duckdb.database import get_latest_sync
    columns = get_columns()
    data = get_data()

    return columns, data
```

<!-- page: framework/framework__user__en__desk__scripting.md -->
---
title: "Scripting\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting"
updated: "2026-02-17"
---


Frappe framework allows you to script the standard models and views directly within the framework without additional code.

Different ways of Scripting:

1. [Client Script](/framework/v14/user/en/desk/scripting/client-script)
1. [Server Script](/framework/v14/user/en/desk/scripting/server-script)
1. [Script Report](/framework/v14/user/en/desk/reports/script-report)
1. [System Console](/framework/v14/user/en/desk/scripting/system-console)

<!-- page: framework/framework__user__en__desk__scripting__client-script.md -->
---
title: "Client Script"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/client-script"
updated: "2026-02-17"
---

A Client Script lets you dynamically define a custom Form Script that is executed on a user's browser. If you choose to utilize non standard tools or libraries, make sure to test them on different browsers to ensure compatibility across your userbase.


> In Version 13, **Custom Script** was renamed to **Client Script**
> 
> 

1. How to create a Client Script
--------------------------------

To create a Client Script

1. To add/edit Client Script, ensure your role is System Manager.
2. Type "New Client Script" in the awesomebar and hit enter to create a new Client Script document.
3. Select the DocType whose form you wish to customize.
4. Update the script using the preset template and save.
5. Head over to the DocType you've customized and see the changes.

2. Features
-----------

As compared to the restrictive nature of Server Scripts, everything is fair game in Client Scripts. This is because the frontend APIs are secure by design. You can utilize all of JavaScript APIs, along with Frappe's and any other JS or CSS library you might've customized Desk with.


> The validations you add through Client Script will only be applied while using the standard form view accessible through the browser. In case you wish for those to be applied through API or [System Console](/framework/v14/user/en/desk/scripting/system-console) access too, use [Server Scripts](/framework/v14/user/en/desk/scripting/server-script).
> 
> 

3. Examples
-----------

### 3.1 Custom validation

Add additional form validations while creating or updating a document from Frappe's standard form view.


```
// additional validation on Task dates
frappe.ui.form.on('Task', 'validate', function(frm) {
    if (frm.doc.from_date < get_today()) {
        msgprint('You can not select past date in From Date');
    }
});
  

```
### 3.2 Fetching values on field updates

Fetch `local_tax_no` on changing value of the `customer` field.


```
cur_frm.add_fetch('customer', 'local_tax_no', 'local_tax_no');
  

```
### 3.3 Customize field properties

Make a field `ibsn` read only after creating the document.


```
// make a field read-only after saving
frappe.ui.form.on('Task',  {
    refresh: function(frm) {
        frm.set_df_property('ibsn', 'read_only', !frm.is_new());
    }
});
  

```
### 3.4 Customize field properties

Calculate incentives on a Sales Invoice form on save.


```
// calculate sales incentive
frappe.ui.form.on('Sales Invoice',  {
    validate: function(frm) {
        // calculate incentives for each person on the deal
        total_incentive = 0
        $.each(frm.doc.sales_team,  function(i,  d) {
            // calculate incentive
            let incentive_percent = 2;
            if(frm.doc.base_grand_total > 400) incentive_percent = 4;
            // actual incentive
            d.incentives = flt(frm.doc.base_grand_total) * incentive_percent / 100;
            total_incentive += flt(d.incentives)
        });
        frm.doc.total_incentive = total_incentive;
    }
});
```
### 3.5 Filter email recipients

You can restrict the available emails via a **Client Script**. Every form can specify what email addresses should be selectable. This reduces the cognitive load for the user and avoids sending emails to wrong recipients.

`CommunicationComposer` (the email dialog) will check if there is a **Client Script** supplying filters for the "recipients", "cc" and "bcc" fields. For example, if a **Quotation** should only show email addresses linked to the recipient of the **Quotation**, we can add the following script:


```
frappe.ui.form.on("Quotation", {
    get_email_recipient_filters: function (frm, field) {
        // field can be "recipients", "cc" or "bcc"
        if (field === "recipients") {
            return [
                [
                    "Dynamic Link",
                    "link_doctype",
                    "=",
                    frm.doc.quotation_to
                ],
                [
                    "Dynamic Link",
                    "link_name",
                    "=",
                    frm.doc.party_name
                ],
            ];
        }
    },
    // ...
};
```
The filters are referring to the **Contact** DocType and it's *Links* child table.

Even with filters, it remains possible to paste arbitrary recipients.

### 3.6 Set default email recipients

In standard processes like **Sales Order** -> **Delivery Note** -> **Sales Invoice**, the email recipients are often pre-defined. For example, this could be done in advance by the account manager.

You can set default email recipients via a **Client Script**. Every form can programmatically supply it's own default recipients.

`CommunicationComposer` (the email dialog) will check if there is a **Client Script** supplying default recipients. For example, if your **Quotation** DocType contains a field named *BCC* (`"custom_bcc"`), you can add the following **Client Script** to use it as default BCC in the email dialog:


```
frappe.ui.form.on("Quotation", {
    get_email_recipients: function (frm, field) {
        // field can be "recipients", "cc" or "bcc"
        if (field === "bcc") {
            return [frm.doc.custom_bcc]
        }
    },
    // ...
};
```
  

<!-- page: framework/framework__user__en__desk__scripting__script-api.md -->
---
title: "Script API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/script-api"
updated: "2026-02-17"
---

List of restricted commands that be called in Frappe Framework Server Script, Print Formats and Script Reports

**Note:** This is only applicable for in-app scripting. If you want more features, you will have to create an "Application" and write the event handlers inside Python Modules

### Python Modules

Following python modules are available

#### `json`

Python standard module `json`

### Formatting

#### _ (Translate)

Translate a string

Example: `_("This is translatable")`

#### frappe.format

Format a value based on its datatype

Example: `frappe.format_value(value, dict(fieldtype='Currency'))`

#### frappe.date_format

Format as default date format

#### frappe.format_date

Returns date as "1st September 2019"

### Session

#### frappe.form_dict

Form / request parameters

Example: Request parameter `/page?name="test"` can be accesssed as `frappe.form_dict.name`

#### frappe.request

Request object

#### frappe.response

Response object

#### frappe.session.user

Current user

#### frappe.session.csrf_token

CSRF token of the current session

#### frappe.user

Current user

#### frappe.get_fullname

Returns fullname of the current user

#### frappe.get_gravatar

Gets the user display image from `frappe.utils.get_gravatar_url`

#### frappe.full_name

Fullname of the current user

### Documents (ORM)

Document access and editing

#### frappe.get_meta

Get metadata object

#### frappe.new_doc

Create a new Document record.

#### frappe.get_doc

Get Document. You can also save or execute any method exposed by the document.

Example: `frappe.get_doc("User", frappe.session.user)`

#### frappe.get_last_doc

Get the last Document of a particular DocType with a given set of filters. Defaults to last created.

Example: `frappe.get_last_doc("User", filters={"name": ("like", "%@apple.com")})`

#### frappe.get_cached_doc

Get Document (or cached)

#### frappe.get_mapped_doc

#### frappe.rename_doc

#### frappe.delete_doc

#### frappe.get_system_settings

Get system default settings

### Database

Database access API

#### frappe.db.get_list

Get list of record filtered by current user's permissions

Example: `frappe.db.get_list("Customer")` will return list of customers

#### frappe.db.get_all

Get list of all records

#### frappe.db.sql

Run a SELECT query

Example: `frappe.db.sql("select name from Customer where name like 'm%'")`

#### frappe.db.get_value

Get a value from a record

Example: `frappe.db.get_value("User", frappe.session.user, "first_name")`

#### frappe.db.get_single_value

Get value from a single type document

Example: `frappe.db.get_single_value("System Settings", "default_currency")`

#### frappe.db.get_default

Get default value

#### frappe.db.escape

Sanitize value for database queries to prevent SQL injection

#### frappe.db.set_value

Set a value

#### frappe.db.exists

Checks for existence of a document. Returns `name` of the document if exists else `None`.

#### frappe.db.commit

Allow users to make explicit commits in server scripts like custom scheduler scripts.  
Note: This won't work in any DocType Event server scripts

#### frappe.db.rollback

Allow users to rollback changes via server scripts.  
Note: This won't work in any DocType Event server scripts

### Query Builder

#### frappe.qb

Query builder API to run SELECT queries.

Example: `frappe.qb.from_("Task").select("*").run()`

### Utilities

Utility methods and functions

#### run_script

Run a server script (return values in `frappe.flags`)

#### frappe.msgprint

Show a modal on the server side after as a part of the response.

Example: `frappe.msgprint("Hello")`

#### frappe.get_hooks

Get application hooks

#### frappe.utils

Methods in frappe.utils

#### frappe.render_template

Render a Jinja template

#### frappe.get_url

Get url of the current site via `frappe.utils.get_url`

#### socketio_port

Port for socketio

#### style.border_color

Returns '#d1d8dd'

#### guess_mimetype

Returns mimetypes.guess_type

#### html2text

Encode HTML as text (markdown)

#### dev_server

True if in developer mode

#### frappe.log_error

Generate Error Log with a traceback

#### FrappeClient

Connect to a Frappe site using a requests session

### API

Make external API calls from Frappe.

#### frappe.make_get_request

Make a GET request.

Example: `frappe.make_get_request('https://example.com')`

#### frappe.make_post_request

Make a POST request.

Example: `frappe.make_post_request('https://example.com', data={'username: 'test'})`

#### frappe.make_put_request

Make a PUT request.

Example: `frappe.make_put_request('https://example.com', headers={'Auth': 'Bearer xyz'})`

### Email

#### frappe.sendmail

Send an email. [See docs](https://frappeframework.com/docs/v14/user/en/api/utils#frappesendmail)

Example: `frappe.sendmail(recipients=['test@example.com'], sender='sender@example.com', subject='My Subject', message='<p>Hello</p>')`

<!-- page: framework/framework__user__en__desk__scripting__server-script.md -->
---
title: "Server Script"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/server-script"
updated: "2026-04-27"
---

> Note: Starting from version 15, Server Scripts are disabled by default to improve security on shared benches.
>
> You can enable them on your bench using following command.
>
> ```
> bench set-config -g server_script_enabled 1
> ```
>
> If you're hosted on Frappe Cloud you need to [create a private bench](https://frappecloud.com/docs/benches) in order to enable server scripts. Public shared benches DO NOT allow use of server scripts.





A Server Script lets you dynamically define a Python Script that is executed on the server on a document event or API

## How to create a Server Script

---

To create a Server Script

1. If your site is being hosted on [frappe cloud](https://frappe.io/cloud) here is the [help article](https://docs.frappe.io/cloud/enable-server-script) explaining the steps to enable server script, In case of self-hosted accounts, set `server_script_enabled` as true in site_config.json of your site.
2. To add/edit Server Script, ensure your role is System Manager.
3. Type "New Server Script" in the awesomebar and hit enter to create a new Server Script document.
4. Set the type of server script (Document Event / API).
5. Set the document type and event name, or method name, script and save.
6. Features

---

### 2.1 Enabling Server Script

Server script must be enabled via site_config.json

```
bench --site site1.local set-config server_script_enabled true
  

```

### 2.2 Document Events

For scripts that are to be called via document events, you must set the Reference Document Type and Event Name to define the trigger

- Before Insert
- After Insert
- Before Validate
- Before Save
- After Save
- Before Submit
- After Submit
- Before Cancel
- After Cancel
- Before Delete
- After Delete
- Before Save (Submitted Document)
- After Save (Submitted Document)
- Before Print

### 2.3 API Scripts

API endpoints can be created on the fly by using the **Script Type** `"API"`. The name of the endpoint depends on field **API Method**. All APIs created using Server Scripts will be automatically prefixed with `/api/method`.

For instance, a script with the **API Method** `"delete-note"` may be accessed via `/api/method/delete-note`. Using Frappe's frontend request library, you could use `frappe.call("delete-note")` in your client scripts.

Guest access may be enabled by checking **Allow Guest** for the created APIs. The response can be set via `frappe.response["message"]` object.

API server scripts also support IP-based rate limiting which you can enable by checking "Enable Rate Limit" and specifying how many calls can be made in a given time window.

### 2.3 Security

Frappe Framework uses the RestrictedPython library to restrict access to methods available for server scripts. Only the safe methods, listed below are available in server scripts.

For allowed methods, see [Script API](/framework/v14/user/en/desk/scripting/script-api)

### 2.4 Using Server Scripts as libraries

You can use a server script as an internal method by setting `frappe.flags` value in script.

### 2.5 Comparing changes

You can diff two versions of server scripts using "Compare Versions" button.

![Server script diff](/files/server-script-diff.png)



## Examples

---

### 3.1 Change the value of a property before change

Script Type: Before Save

```
if "test" in doc.description:
    doc.status = 'Closed'
  

```

### 3.2 Custom validation

Script Type: "Before Save"

```
if "validate" in doc.description:
    raise frappe.ValidationError
  

```

### 3.3. Auto Create To Do

Script Type: "After Save"

```
if doc.allocted_to:
    frappe.get_doc(dict(
        doctype = 'ToDo',
        owner = doc.allocated_to,
        description = doc.subject
    )).insert()
  

```

### 3.4 API

- Script Type: API
- Method Name: `test_method`

```
frappe.response['message'] = "hello"
  

```

Request: `/api/method/test_method`

### 3.5 Internal Library

> New in version 13

Call one (`script_1` script from another `script_2`)

Script 1:

```
frappe.flags.my_key = 'my value'
  

```

Script 2:

```
my_key = run_script('script_1').get('my_key')
  

```

<!-- page: framework/framework__user__en__desk__scripting__system-console.md -->
---
title: "System Console\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/scripting/system-console"
updated: "2026-02-17"
---

System Console helps you run Python commands for debugging based on [Script API](/framework/v14/user/en/desk/scripting/script-api)
. It is allowed only for users with role System Manager.

To access the System Console, search for it on the Search Bar.

![System Console](/files/system-console.png)

### API

The methods exposed by the [Script API](/framework/v14/user/en/desk/scripting/script-api)
 can be accessed via the System Console

### Logging response

To print the response, use the `log` method.

<!-- page: framework/framework__user__en__desk__workspace.md -->
---
title: "Workspace"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace"
updated: "2026-02-17"
---

Workspace is the first page you land on when you log in.
It also has a dedicated sidebar where you can rearrange the workspace position according to your convenience.

The workspace itself is a tool to build user-specific pages. 
It comes with some standard workspaces which are listed in the `PUBLIC` section in the sidebar and are visible to all users.
You can also create private workspaces which will only be visible to the logged-in user(owner) in the `MY WORKSPACES` section. 

Let's build one and check out some cool features.

###Create New Workspace
1. Click on **Create Workspace** button.
2. Enter Title and click on Create.

![Create Workspace](/files/CreateWorkspace.gif)

###Create Child Workspace
1. Click on **Create Workspace** button.
2. Enter Title.
3. Select Home in the Parent field and click on Create.

![Create Child Workspace](/files/ChildPage.gif)

###Workspace Blocks
The workspace block is a building block for the workspace page.
These blocks can be placed in different variations to build an ideal workspace for a specific use case.

[Learn More →](/framework/v14/user/en/desk/workspace/blocks)

![Workspace Blocks](/files/WorkspaceBlocks.gif)
###Sidebar


![Workspace Sidebar](/files/WorkspaceSidebar.png)


There are two sections in the sidebar `MY WORKSPACES` & `PUBLIC`.


You can create as many private workspaces as you want.
It will only be visible to the currently logged-in user(owner) under the `MY WORKSPACES` section


All the standard workspaces comes under `PUBLIC` section. 
You can also create more public workspaces. These workspaces will be visible to all users.
 


[More →](/framework/v14/user/en/desk/workspace/customization#customizing-workspaces) 



>Only users with **Workspace Manager Role** can create, edit or delete public workspaces

###Customization
Workspace has two modes **Read Only Mode** and **Edit Mode**. You can start customizing your workspace by clicking on the **Edit** button.
[Customizing Workspaces](/framework/v14/user/en/desk/workspace/customization#customizing-workspaces) and [Customizing Workspace Page](/framework/v14/user/en/desk/workspace/customization#customizing-workspace-page) are two different things.

>Adding new blocks from the workspace document will not work as the new workspace doesn't know exactly where to add that block (at which position). You can update the existing blocks from the workspace document but it is not recommended either. The best practice would be to use the new workspace builder UI to do all kinds of customization.

<!-- page: framework/framework__user__en__desk__workspace__access.md -->
---
title: "Access"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/access"
updated: "2026-02-17"
---

Workspaces can be restricted based on Modules and Roles.

### Modules

Users can have access to different modules and standard workspaces are visible based on access to those modules.

In the below GIF you can see when Website Module access was removed for user John Doe, he was not able to see Website Workspace. ![Module Access](/files/ModuleAccess.gif)  


### Roles

Users can have access to modules but what if you still want those users to not see the standard workspace of that module. Then you can restrict access based on the roles given to that user.

Check below Example:

Jack Doe is a manager with Workspace Manager Role. He only wants user with Website Manager Role to see the Website Workspace.ence such a configuration is made as follows: ![Role Access 1](/files/RoleAccess1.gif)  


To test this, Jane Doe is given the Website Module access and not given the Website Manager role. Due to the configuration done above, she will not be able to see Website Workspace as shown below. Where as John Doe who has Website Module access and Website Manager role, will be able to see the Website Workspace. ![Role Access 2](/files/RoleAccess2.gif)  


### Default Workspace

The default workspace that will be shown when the user first logs in can be configured for each user. By default, the user will be shown the workspace they were last in. The default workspace can be selected using the "Default Workspace" field of the User settings form, that can be accessed through the "My Settings" option of your avatar menu.

<!-- page: framework/framework__user__en__desk__workspace__blocks.md -->
---
title: "Blocks"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/blocks"
updated: "2026-04-14"
---

Blocks as the name suggest are the building blocks of the workspace.  
You can add different types of blocks, edit them, and arrange them as per your need to build a fully customizable workspace.

There are currently 9 blocks. We will keep adding new blocks in the coming future.





Let's go through each of them:



![Blocks](/files/BlockListd3d92d.png)



### Heading

A heading block is used as a header for any section or paragraph.

![Section Header](/files/SectionHeader.png)

![Paragraph Header](/files/ParagraphHeader.png)

### Text

Text block is used as a paragraph or description for any section.

![Paragraph Block](/files/ParagraphBlock.png)

Both **Heading** and **Text** has an inline toolbar.  
Currently, we have limited tools like header size from H1 to H6, bold, italic and links.

![Inline Toolbar](/files/InlineToolbar.png)

### Card

A card contains several links that can be used for quick navigation.  
The link item can be a DocType, Report or Page.

![Card Block](/files/CardBlock.png)

### Chart

You can add any **Dashboard Chart** on the workspace using this block. 

![Chart Block](/files/ChartBlock.png)

### Shortcut

Shortcut block is used to quickly navigate to any DocType, Report or Page.

![Shortcut Block](/files/ShortcutBlock.png)

Shortcuts can be customized too.  
You can select the view in which it should open, and can add filters that will be applied when you open the selected view.  
You can see the number of records based on the filters applied on the shortcut as a pill.

![Shortcut Features](/files/ShortcutFeatures.png)

### Spacer

It is used to add some space between two blocks.

![Spacer Block](/files/SpacerBlock.png)

It can also be used to position other blocks by adding white space before or after the block.

![Spacer Separator](/files/SpacerSeparator.png)

![Spacer Separator Output](/files/SpacerSeparatorOutput.png)

### Onboarding

The onboarding block is used to guide first-time users when they land on your page.  
It has steps to follow to learn a specific module.  
For each step, there is some description on the right section or there can be a link to a video.

![Onboarding Block](/files/OnboardingBlock.png)

### Quick List

In the quick list block, we can see recently updated records of selected doctype.  
We can also add some filters.  
While in the read-only mode we have the option to refresh the list, update the applied filters, create a new record and open doctype's list view.

![Quick List Block](/files/QuickListBlock.png)

### Number Card

You can add any existing **Number Card** on the workspace using this block.

![Number Card Block](/files/NumberCardBlock.png)

<!-- page: framework/framework__user__en__desk__workspace__customization.md -->
---
title: "Customization"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/desk/workspace/customization"
updated: "2026-02-17"
---

Workspace has two modes **Read Only Mode** and **Edit Mode**. You can start customizing your workspace by clicking on the **Edit** button.
Customizing Workspaces and Customizing Workspace Page are two different things. 

##Customizing Workspaces
All customization done to the workspaces can be done through the sidebar except for creating a workspace.

Let's see what all customizations we can do:

###Edit workspace details
You can update the title, and icon, make it parent or child and can make it public or private.
![Edit Workspace Details](/files/EditWorkspaceDetails.gif)
###Create Duplicate
You can create a duplicate of an existing workspace and can add or remove some blocks from it as per your need.
![Duplicate Workspace](/files/DuplicateWorkspace.gif)
###Delete Workspace
Delete an existing workspace.
![Delete Workspace](/files/DeleteWorkspace.gif)
###Hide Workspace
Hide your private workspaces.
![Hide Workspace As User](/files/HideWorkspaceAsUser.gif)

Only `Workspace Manager` can hide public workspaces.
![Hide Workspace As Workspace Manager](/files/HideWorkspaceAsWorkspaceManager.gif)

###Rearrange Position:
You can drag & drop the workspace from the sidebar to change its position or make it a child/parent workspace.
![Rearrage Workspace](/files/RearrangeWorkspace.gif)

>**Save/Discard** buttons are only used to save workspace page customizations. All workspace changes done from the sidebar get saved as you make them.

##Customizing Workspace Page
Customizing blocks in a particular workspace comes under this category.

Let's see what all customizations we can do:

###Add a new block
![Add Block](/files/AddBlock.gif)
###Edit an existing block
![Edit Block](/files/EditBlock.gif)
###Remove or delete an existing block
![Delete Block](/files/DeleteBlock.gif)
###Resize the width of a block
![Resize Block](/files/ResizeBlock.gif)
###Rearrange the position of a block
![Rearrange Block](/files/RearrangeBlock.gif)

<!-- page: framework/framework__user__en__discussions.md -->
---
title: "Discussions"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/discussions"
updated: "2026-02-17"
---

You can now add a discussions component on any web page of the portal. The discussions component allows logged in users to enter and share messages with other users. This component can be used for discussions or to setup a portal where users help each other with their queries.

![Discussions Component](/files/Screenshot 2022-02-07 at 3.34.37 PM.png)

### Steps to Setup the Discussions Component

1. Open the web page document on which you want to add the discussions component or create a new web page and save it.
2. Scroll to the Page Building Blocks table.
3. Under Web Template select Discussions.
![Page Building Blocks](/files/Screenshot 2022-02-07 at 3.56.53 PM.png)
4. Click on Edit values.
![Edit Values](/files/Screenshot 2022-02-07 at 3.53.57 PM.png)
5. Enter a Title, CTA Title and select the Web Page as the current web page name.
6. You can check Single Thread if you want the discussion to be single threaded.
7. Save the page.

<!-- page: framework/framework__user__en__email-groups.md -->
---
title: "Email Groups"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/email-groups"
updated: "2026-02-17"
---

Email Groups are a powerful tool for managing and automating email communication with subscribers, clients, or any group of contacts.

The **Email Group** is created under the Email module, where it's set up with a unique title. Each **Email Group** is automatically named using the 'Title' field, ensuring easy identification and management. Managed primarily by the "Newsletter Manager" role, this ensures that only authorized personnel can create, modify, or delete the groups.

The *Total Subscribers* field dynamically displays the number of subscribers in the group, offering a quick view of the group's reach. **Email Groups** are linked to individual **Email Group Members**, allowing for easy management and segmentation of subscribers.

The *Confirmation Email Template* field links to a specific email template used for sending confirmation emails.

The *Welcome Email Template* is used for initial engagement with new subscribers. It is sent immediately after they have confirmed their email address and sets the tone for future communication.

After successful confirmation, subscribers can be directed to a custom *Welcome URL*. This can be a landing page or any relevant content, providing immediate engagement with the new subscriber. If the *Welcome URL* is not set, subscribers will be taken to a generic confirmation page.

The option to add query parameters to the *Welcome URL* enables personalized interactions and tracking of subscriber engagement.

![email_group_with_welcome_url](/files/email_group_with_welcome_url.png "email_group_with_welcome_url.png")  

<!-- page: framework/framework__user__en__form-tours.md -->
---
title: "Form Tours"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/form-tours"
updated: "2026-02-17"
---

Frappe provides an easy way to generate form tutorials for your complex doctype with very little configuration.

![Form Tour](/files/form-tour-display.png)  


Creating a Form Tour
--------------------

To create a Form Tour, type "new form tour" in awesomebar and hit enter.

1. Enter Title. For eg., 'Creating a Custom Field'
2. Select Reference DocType.
3. Add steps defining each fields.
4. Save the document.

![Custom Field Form Tour](/files/custom-field-form-tour.png) *A Tour to explain creation of Custom Fields*

Configuration Options
---------------------

### Form Tour

1. **Is Standard**: To make a standard Form Tour which will be stored as JSON. Can only be set while developer mode is on.
2. **Save on Completion**: If checked, the last step of the Form Tour will prompt the user to save the document.
3. **Show First Document Tour**: If you want to show the tour of an existing document instead of a new form, enable this. As the name suggests, it gives the tour of the very first document created for this DocType.
4. **Include Name Field**: For some doctypes, the name is set by the user. On enabling this, the name field becomes the first step of the tour.

### Form Tour Steps

1. **Field**: A field from the selected doctype. This will be highlighted with a Title & Description.
2. **Title** & **Description**: To describe the field for its use, impact, and other hidden wirings of the field.
3. **Position**: The position of the highlighting popover is decided by this field. There are multiple options to choose depending upon the position of the highlighted field.
4. **Next Condition**: A code field which expects a valid JS condition which applies on the document. For eg., for a Task DocType Tour, we can check if task priority is set before going to the next condition by setting next condition as follows:

`eval: doc.priority != ""`
5. **Is Table Field**: To be checked if the field to be highlighted is under a child table.
6. **Parent Field**: Table field from the selected doctype. Only visible if **Is Table Field** is checked. Allows user to select a child table field.

Triggering the Tours
--------------------

Once you are done describing the Form & its fields, you are now ready to trigger the tour by using Form API. You just have to initialize the tour with appropriate `tour_name` and then simply start the tour with `frm.tour.start()`.


```
frappe.ui.form.on('Your DocType', {
    onload: function(frm) {
        const tour_name = 'Your Form Tour Name';
        frm.tour.init({ tour_name }).then(() => frm.tour.start());
    }
});
```

<!-- page: framework/framework__user__en__guides.md -->
---
title: "Guides"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides"
updated: "2026-02-17"
---

Frappe is a full-stack "batteries included" framework. It has libraries and APIs for everything from authentication and scheduled jobs to managing different currencies, reports, as well as building forms.

In this section we will try and cover the most commonly used API on client and server side that will be useful for app development.

1. [Basics](/framework/v14/user/en/guides/basics/apps)
2. [App Development](/framework/v14/user/en/guides/app-development/custom_action_link_field)
3. [Deployment](/framework/v14/user/en/guides/deployment/packages)
4. [Reports and Printing](/framework/v14/user/en/guides/reports-and-printing/getting-information-from-another-document-in-print-format)
5. [Portal Development](/framework/v14/user/en/guides/portal-development/)
6. [Data](/framework/v14/user/en/guides/data/using-data-migration-tool)
7. [Integration](/framework/v14/user/en/guides/integration/google_gsuite)
8. [Database Settings](/framework/v14/user/en/guides/database-settings/setup-read-from-secondary-db)
9. [Automated Testing](/framework/v14/user/en/guides/automated-testing)
10. [Desk](/framework/v14/user/en/guides/desk)

<!-- page: framework/framework__user__en__guides__app-development__adding-custom-button-to-form.md -->
---
title: "Adding Custom Button To Form"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-custom-button-to-form"
updated: "2026-02-17"
---


To create a custom button on your form, you need to edit the javascript file associated to your doctype. For example, If you want to add a custom button to User form then you must edit `user.js`.

In this file, you need to write a new method `add_custom_button` which should add a button to your form.

#### Function Signature for `add_custom_button(...)`
 ```js
 frm.add_custom_button(__(buttonName), function() {
 // perform desired action such as routing to new form or fetching etc.
 }, __(groupName));
 ```

#### Example-1: Adding a button to User form
We should edit `frappe/core/doctype/user/user.js`

 ```js
 frappe.ui.form.on('User', {
    refresh: function(frm) {
        frm.add_custom_button(__('Get User Email Address'), function() {
            frappe.msgprint(frm.doc.email);
        }, __("Utilities"));
    }
 });
 ```

You should be seeing a button on user form as shown below,

![Custom Button](/files/add_custom_button.png)

<!-- page: framework/framework__user__en__guides__app-development__adding-module-icons-on-desktop.md -->
---
title: "Adding Module Icons On Desktop\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-module-icons-on-desktop"
updated: "2026-02-17"
---


> Frappe version 12

To create an icon for your app, you have to edit your app's `config/desktop.py`. In this file you can add a `get_data` method returns a dictionary with the module icon parameters.

You can also create a dropdown list of actions available on this module and actions available on the page when you click on this module. To achieve this, create a file `config/MODULE_NAME.py` (replace `MODULE_NAME` with the name of one of your app's modules).

## Example App Library Management

`config/desktop.py`:

```python
def get_data():
 return [
 {
 "module_name": "Library Management",
 "category": "Modules",
 "label": _("Library Management"),
 "color": "#589494",
 "icon": "octicon octicon-book",
 "type": "module",
 "description": "Library management"
 }
 ]
```

`config/library_management.py`:

```python
def get_data():
 return [
 {
 "label": _("Library Management"),
 "icon": "octicon octicon-book",
 "items": [
 {
 "type": "doctype",
 "name": "Article",
 "label": _("Article"),
 "description": _("Manage Books"),
 "onboard": 1,
 },
 {
 "type": "doctype",
 "name": "Library Member",
 "label": _("Library Member"),
 "description": _("Manage Members"),
 # Not displayed on dropdown list action but on page after click on module
 "onboard": 0,
 }
 ]
 }
 ]
```

Note: Module views are visible based on permissions.

<!-- page: framework/framework__user__en__guides__app-development__adding-social-login-provider.md -->
---
title: "Adding Social Login Provider\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-social-login-provider"
updated: "2026-02-17"
---


This guide discusses how to add a social login provider to frappe via pull request.

### Add your provider in `SocialLoginKey.get_social_login_provider`

```
providers["Frappe"] = {
 "provider_name": "Frappe",
 "enable_social_login": 1,
 "custom_base_url": 1,
 "icon":"/assets/frappe/images/favicon.png",
 "redirect_url": "/api/method/frappe.www.login.login_via_frappe",
 "api_endpoint": "/api/method/frappe.integrations.oauth2.openid_profile",
 "api_endpoint_args":None,
 "authorize_url": "/api/method/frappe.integrations.oauth2.authorize",
 "access_token_url": "/api/method/frappe.integrations.oauth2.get_token",
 "auth_url_data": json.dumps({
 "response_type": "code",
 "scope": "openid"
 })
}
```

### Add provider key in exact same type case in options of `social_login_provider` select field on `Social Login Key` DocType. e.g. `Frappe`

Once the user adds a social login provider and enables it the `Authorization Code` is sent back by the provider api server on to the redirect_url mentioned on the same server. You will have to add a whitelisted method allowing guest access in `frappe.integrations.oauth2_logins`. e.g. `login_via_office365`

There many implementations of OAuth 2.0 + OpenID Connect. Here we'll discuss two ways of accessing openid information.

#### User Creation via OpenID Profile Endpoint

example:

```
@frappe.whitelist(allow_guest=True)
def login_via_frappe(code, state):
 login_via_oauth2("frappe", code, state, decoder=json.loads)
```

#### User Creation via id_token

example:

```
@frappe.whitelist(allow_guest=True)
def login_via_office365(code, state):
 login_via_oauth2_id_token("office_365", code, state, decoder=json.loads)
```

<!-- page: framework/framework__user__en__guides__app-development__connected-app.md -->
---
title: "Set up a new Connected App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/connected-app"
updated: "2026-02-17"
---

You can use **Connected App** to allow your frappe instance to access other web services on your behalf.


> This example shows how to connect to Google Mail, but you can use any service supporting OAuth 2.0.
> 
> 

First, create a new **Connected App** and give it a name. Most providers offer an URL like `/.well-known/openid-configuration` where they publish all OAuth endpoints. Enter this URL and click on "Get OpenID Configuration".

If you don't know this URL, please go to the "Endpoints" section and manually enter the *Authorization URI* and *Token URI*. The Authorization URI is where you will be redirected to give your consent. The Token URI is the endpoint where the system can exchange an authorization code for an access or refresh token. Please check the documentation of the specific integration or third party service to get the right values.

![new_connected_app](/files/new_connected_app.png)  


Now the configuration should look like this:

![fetched_openid_config](/files/fetched_openid_config.png)  


Click on "Save". Now you should see a new read-only field called *Redirect URI*. Note that the last part of it is specific to your **Connected App**. You'll need to register the Redirect URI with your provider (Google, in this case).

Copy the Redirect URI, head to the third party service and create new OAuth 2.0 client credentials. You will need to specify the authorized JavaScript origins and the Redirect URI you just copied. Enter the domain name of your frappe instance as authorized JavaScript origin. On a production server this might be `https://erp.mycompany.com`. For local development you can use something like `http://localhost:8000`.


> It is crucial that the authorized JavaScript origins and the authorized redirect URIs are correct. Otherwise you will not be able to connect.
> 
> 

![Create OAuth 2.0 client credentials](/files/3-get-client-credentials.png)  


Copy the client ID and secret from the third party service to your **Connected App** and save.

![client_credentials](/files/client_credentials.png)  


Next, you'll need to define what scopes your system needs to access. In this example, we want to connect to an email inbox, so we need the scope `https://mail.google.com/`. For other use cases, please check the available scopes at your providers' documentation.

![scope](/files/scope.png)  


Lastly, we can define extra parameters. The Google documentation states that we'll need the parameter `access_type=offline`, so that for our server can access the email inbox in the background and keep refreshing the access token without user intervention. If we don't pass this parameter, the temporary access will quickly expire and we'll need to log in again and again.

![extra_parameters](/files/extra_parameters.png)  


Now you and your users can click on "Connect to ..." on the top right. This will open a new browser tab that shows the third party service's consent screen. After this, you will be redirected to your frappe instance.

![connect](/files/connect.png)  


In the backend, your server will exchange a code that it obtained during the redirect for a temporary access token and, optionally, a refresh token. These can then be used to access the third party service on your behalf.

<!-- page: framework/framework__user__en__guides__app-development__custom-module-icon.md -->
---
title: "Custom Module Icon"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/custom-module-icon"
updated: "2026-02-17"
---


If you want to create a custom icon for your module, you will have to create an SVG file for your module and set the path to this file in the `desktop/config.py` of your app.  


This icon is loaded via AJAX first time, then it will be rendered.

Example:

```py
from frappe import _

 def get_data():
    return {
     "Frappe Apps": {
     "color": "orange",
     "icon": "assets/frappe/images/frappe.svg",
     "label": _("Frappe.io Portal"),
     "type": "module"
    }
  }
 ```

> PS: A great place to buy SVG icons for a low cost is the awesome [Noun Project](http://thenounproject.com/)

<!-- page: framework/framework__user__en__guides__app-development__custom_action_link_field.md -->
---
title: "Custom Action in Link Field"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/custom_action_link_field"
updated: "2026-02-17"
---


You can add a new custom link option to the standard link field by defining the function in the namespace `frappe.ui.form.ControlLink.link_options`.

In the `frappe.ui.form.ControlLink.link_options`, you have access to the link field object.

### 1. Adding Custom Option

```js
frappe.ui.form.ControlLink.link_options = function(link) {
 return [
 {
 html: ""
 + " "
 + __("Custom Link Option")
 + "",
 label: __("Custom Link Option"),
 value: "custom__link_option",
 action: () => {}
 }
 ];
}
 
```

Once a function is assigned to `frappe.ui.form.ControlLink.link_options`, the link field will have a new link option:

![182354398 c1fc9f55 4464 4683 bb74 982ec2546f71](https://user-images.githubusercontent.com/7310479/182354398-c1fc9f55-4464-4683-bb74-982ec2546f71.png)

<!-- page: framework/framework__user__en__guides__app-development__dialogs-types.md -->
---
title: "Dialogs Types\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/dialogs-types"
updated: "2026-02-17"
---


Frappe provides a group of standard dialogs that are very useful while coding.

## Alert Dialog

![](/files/show-alert.png)

Alert Dialog is used for showing non-obstructive messages.

It has 2 parameters:

- **txt:** The message to be shown in the `Alert Dialog`
- **seconds:** The duration that the message will be displayed. The default is `3 seconds`.

### Example

 show_alert('Hi, do you have a new message', 5);

---

## Prompt Dialog

![](/files/prompt.png)

Prompt Dialog is used for collecting data from users.

It has 4 parameters:

- **fields:** a list with the fields objects
- **callback:** a function to process the data in the dialog
- **title:** the title of the dialog
- **primary_label:** the label of the primary button

### Example

 frappe.prompt([
 {'fieldname': 'birth', 'fieldtype': 'Date', 'label': 'Birth Date', 'reqd': 1}
 ],
 function(values){
 show_alert(values, 5);
 },
 'Age verification',
 'Subscribe me'
 )

---
## Confirm Dialog

![](/files/confirm-dialog.png)

Confirm Dialog is used to get a confirmation from the user before executing an action.

It has 3 arguments:

- **mesage:** The message to display in the dialog
- **onyes:** The callback on positive confirmation
- **oncancel:** The callback on negative confirmation

### Example

 frappe.confirm(
 'Are you sure to leave this page?',
 function(){
 window.close();
 },
 function(){
 show_alert('Thanks for continue here!')
 }
 )

---

## Message Print

![](/files/msgprint.png)

Message Print is used for showing information to users.

It has 2 arguments:

- **message:** The message to display. It can be a HTML string
- **title:** The title of the dialog

### Example

 msgprint("**Server Status**"
 + "

---

"
 + ""
 + "* **28%** Memory
"
 + "* **12%** Processor
"
 + "* **0.3%** Disk
"
 + "
", 'Server Info')

---

### Custom Dialog

![](/files/dialog.png)

You can extend and build your own custom dialogs using `frappe.ui.Dialog`

### Example

 var d = new frappe.ui.Dialog({
 'fields': [
 {'fieldname': 'ht', 'fieldtype': 'HTML'},
 {'fieldname': 'today', 'fieldtype': 'Date', 'default': frappe.datetime.nowdate()}
 ],
 primary_action: function(){
 d.hide();
 show_alert(d.get_values());
 }
 });
 d.fields_dict.ht.$wrapper.html('Hello World');
 d.show();

<!-- page: framework/framework__user__en__guides__app-development__executing-code-on-doctype-events.md -->
---
title: "Executing Code On Doctype Events\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/executing-code-on-doctype-events"
updated: "2026-02-17"
---


To execute code when a DocType is inserted, validated (before saving), updated, submitted, cancelled, deleted, you must write in the DocType's controller module.

#### 1. Controller Module

The controller module exists in the `doctype` folder in the Module of the `DocType`. For example, the controller for **ToDo** exists in `frappe/desk/doctype/todo/todo.py` (version 5). A controller template is created when the DocType is created. which looks like

 from __future__ import unicode_literals

 import frappe
 from frappe.model.document import Document

 class CustomType(Document):
 pass

#### 2. Document Properties

All the fields and child tables are available to the class as attributes. For example the **name** property is `self.name`

#### 3. Adding Methods

In this module, you can add standard methods to the class that are called when a document of that type is created. Standard Handlers are:

1. `autoname`: Called while naming. You can set the `self.name` property in the method.
1. `before_insert`: Called before a document is inserted.
1. `validate`: Called before document is saved. You can throw an exception if you don't want the document to be saved
1. `on_update`: Called after the document is inserted or updated in the database.
1. `on_submit`: Called after submission.
1. `on_cancel`: Called after cancellation.
1. `on_trash`: Called after document is deleted.

<!-- page: framework/framework__user__en__guides__app-development__exporting-customizations.md -->
---
title: "Exporting Customizations to your App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/exporting-customizations"
updated: "2026-02-17"
---

A common use case is to extend a DocType via Custom Fields and Property Setters for a particular app. To save these settings to an app, go to **Customize Form**

You will see a button for **Export Customizations**

![](/files/export-custom-1.png)  


Here you can select the module and whether you want these particular customizations to be synced after every update.

The customizations will be exported to a new folder `custom` in the module folder of your app. The customizations will be saved by the name of the DocType

![](/files/export-custom-2.png)  


When you do `bench update` or `bench migrate` these customizations will be synced to the app.


> Warning: Using this feature whenever a customization are synced all property setters and custom permissions are replaced on site with what's specified in the code. If this behaviour is not desired then you should not use this feature. 
> 
> 

<!-- page: framework/framework__user__en__guides__app-development__fetch-custom-field-value-from-master-to-all-related-transactions.md -->
---
title: "Fetch a Field Value from a Document into a Transaction\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/fetch-custom-field-value-from-master-to-all-related-transactions"
updated: "2026-02-17"
---


Let's say, there is a custom field "GSTIN" in Supplier, which should be fetched in Purchase Order.


### Scenario I: You want to keep this field updated

In this scenario, the custom field will be updated automatically based on the value in Supplier when you save the Purchase Order and will be re-updated everytime you save the Purchase Order. Since this field needs to be updated automatically, it overwrites user input. If you want to allow user input, refer to Scenario II.

#### Steps:

1. Create a Custom Field **GSTIN** for *Supplier* document with *Field Type* as **Data**.
 ![](/files/gstin-field-supplier.png)

1. Create another Custom Field **GSTIN** for *Purchase Order* document, but in this case with *Field Type* as **Read Only** or check **Read Only** checkbox. Set **Fetch From** as `supplier.gstin`.
 
![](/files/gstin-field-po-s1.png)

1. Go to the user menu and click "Reload".

1. Now, on selection of Supplier in a new Purchase Order, **GSTIN** will be fetched automatically from the selected Supplier.
 
![](/files/po-gstin-s1.png)

### Scenario II: You want to allow user input if value not found

In this scenario, the value is fetched from the Supplier the first time the Purchase Order is created. If the value is not found in Supplier, you can enter it manually. The value will only be fetched on saving Purchase Order if the field is empty.

#### Steps:

1. Create a Custom Field **GSTIN** for *Supplier* document with *Field Type* as **Data**.
 
![](/files/gstin-field-supplier.png)

1. Create another Custom Field **GSTIN** for *Purchase Order* document with *Field Type* as **Data**. Set **Fetch From** as `supplier.vat_number` and tick the checkbox titled **Fetch If Empty**.
 
![](/files/gstin-field-po-s2.png)

1. Go to the user menu and click "Reload".

1. Now, on selection of Supplier in a new Purchase Order, **GSTIN** will be fetched automatically from the selected Supplier. If GSTIN is not found in supplier, you can enter it manually.
 
![](/files/po-gstin-s2.png)

<!-- page: framework/framework__user__en__guides__app-development__generic-oauth-client.md -->
---
title: "Prerequisites\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/generic-oauth-client"
updated: "2026-02-17"
---


- [Connected App](/framework/v14/user/en/guides/app-development/connected-app)

 **Connected App** stores the client ID and secret, scopes and endpoints of the platform you're integrating with.

## Getting started

> This example uses Google, but you can use any service supporting OAuth 2.0.

Your integration will most probably need a settings doctype (for example, "Google Settings"). Here you create a link field to **Connected App**. A System Manager can later create a **Connected App**, enter the client credentials and link it to your integration. You will know which **Connected App** belongs to your integration via your settings DocType.

```py
google_settings = frappe.get_single('Google Settings')
connected_app_name = google_settings.get('connected_app')

connected_app = frappe.get_doc('Connected App', connected_app_name)
```

Now you have an instance of your **Connected App**, containing the credentials and endpoint URIs. If a user didn't connect yet, they can open the **Connected App** and click the "Connect to ..." button on the top right. Alternatively, you can get the authorization URI and use it for your own custom button or redirect:

```py
authorization_uri = connected_app.initiate_web_application_flow() # optional
```

Once the user is authorized, you can get an authenticated session like this:

```py
session = connected_app.get_oauth2_session()
```

> If the user is not authenticated at this time, they will be redirected to the authentication page.

Now you can retrieve any allowed resource from the target platform:

```py
session.get('https://www.googleapis.com/oauth2/v2/userinfo')
```

If the access token is expired, the session will automatically try to refresh it.

<!-- page: framework/framework__user__en__guides__app-development__how-enable-developer-mode-in-frappe.md -->
---
title: "How to Enable Developer Mode in Frappe"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-enable-developer-mode-in-frappe"
updated: "2026-02-17"
---

When you are in application design mode and you want the changes in your DocTypes, Reports etc to affect the app repository, you must be in **Developer Mode**.

To enable developer mode, update the `site_config.json` file of your site in the sites folder:


```
frappe-bench/sites/{your site}/site_config.json
```
Inside the `frappe-bench` folder, run


```
bench set-config -g developer_mode 1
```
OR, manually, write `"developer_mode": 1` inside the `{ .. }` of `site_config.json`


```
{
  "developer_mode": 1,
  ...
}
```
After setting developer mode, clear the cache:


```
bench --site {your site} clear-cache
```
Some apps might require additional dependencies to build and test in development mode. Install them using bench:


```
bench setup requirements --dev
```

<!-- page: framework/framework__user__en__guides__app-development__how-to-create-custom-fields-during-app-installation.md -->
---
title: "How To Create Custom Fields During App Installation\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-to-create-custom-fields-during-app-installation"
updated: "2026-02-17"
---


Your custom app can automatically add **Custom Fields** to DocTypes outside of your app when it is installed to a new site.

To do this, add the new custom fields that your app requires, using the Frappe web application.

In your `hooks.py` file, add `"Custom Fields"`

 fixtures = ["Custom Field"]

Export fixtures before you commit your app with:

 $ bench --site mysite export-fixtures

This will create a new folder called `fixtures` in your app folder and a `.csv` or `.json` file will be created with the definition of the custom fields you added.

This file will be automatically imported when the app is installed in a new site or updated via `bench update`.

Note: You can also add single DocTypes like "Website Settings" as fixtures

<!-- page: framework/framework__user__en__guides__app-development__how-to-improve-a-standard-control.md -->
---
title: "How To Improve A Standard Control\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-to-improve-a-standard-control"
updated: "2026-02-17"
---


Frappe has a couple of elegant and useful widgets, but some times we need to edit them to add small improvements. This small article will describe how to add new resources to the standard widgets.

Let me explain first our goal:

> Add `many` alternative translations in `numerous records` and in a `lot of doctypes`

Look the highlighted sections in the __goal__, we have _many translations_ to add in _many records_ and in _many doctypes_, so, we heave a **many of work**, so we have a lot to do right?

The answer for this question is: _-Of course not! Because we know that if one element exists in many records and in many doctypes, this element is the `Control` or `Widget`_

So, what we need do, is improve your goal based on the `Control`, to reduce our quantity of work.

But, where will we find this magic element, the control? _-For now, we can look it in the JavaScript sources - let's look now at [Github](https://github.com/frappe/frappe/blob/develop/frappe/public/js/frappe/form/controls/control.js)_

> Don't worry if you don't understand the code for now, our goal there is simplify our work.

Let's go ahead with the thought!

We know where we need to make the changes, but how will we dismember which are the controls that are affected by our feature and which aren't ?

We need to keep in mind, that `Control` are instance of `DocFields` and the `DocFields` have a field that is very important for us in this case, the field that will help us to dismember which are affected by our feature and which aren't is the field `options` in the `DocField`.

_-Wait!, we understood that the field `options` can help us, but, how will it help us?_

Good question, we will define a word to put in the `options` of the `DocFields` that we need to include the feature, this world will be **`Translatable`.**

> If you forget how to customize the options of a field look [this article](https://kb.erpnext.com/kb/customize/creating-custom-link-field), it can refresh your knowledge.

Well, with the defined word in `options` of our selected `DocFields`, now is time to code:

_-At last, we think we would never stop talking!_

```js
 frappe.ui.form.ControlData = frappe.ui.form.ControlData.$extend({
 make_input: function(){
 var options = this.df.options;
 if (!options || options!=="Translatable"){
 this._super();
 return;
 }
 var me = this;
 $('\
 \
 \
 \\
 \
 ').prependTo(this.input_area);
 this.$input_area = $(this.input_area);
 this.$input = this.$input_area.find('input');
 this.$btn = this.$input_area.find('.dialog-btn');
 this.set_input_attributes();
 this.$input.on("focus", function(){
 me.$btn.toggle(true);
 });
 this.$input.on("blur", function(){
 setTimeout(function(){ me.$btn.toggle(false) }, 500);
 });
 this.input = $this.input.get(0);
 this.has_input = true;
 var me = this;
 this.setup_button();
 },
 setup_button: function(){
 var me = this;
 if (this.only_input){
 this.$btn.remove();
 return;
 }
 this.$btn.on("click", function(){
 var value = me.get_value();
 var options = me.df.options;
 if (value && options && options==="Translatable"){
 this.open_dialog();
 }
 });
 },
 open_dialog: function(){
 if (this.frm && !this.frm.is_dirty()) {
 new frappe.ui.form.TranslationSelector({
 doc: doc,
 df: this.doc,
 text: this.value
 });
 }
 }
 });
```

_-Other letter soup, for my gosh!_

In fact, it IS a soup of letters, for a newbie, but we are not a beginner.

Let me explain what this code does;

 - At line 1 the code overrides the `ControlData` by one extended `Class` of itself.
 - The method `make_input` checks if the docfield is **`Translatable`** to make the new `Control` if not, it calls the *original* `make_input` using `_super()`
 - The method `setup_button` checks if the docfield is **`Translatable`** to enable it show a `dialog`
 - The method `open_dialog` invokes a new instance of the `TranslationSelector` that we will create in the code below.

<!-- page: framework/framework__user__en__guides__app-development__insert-a-document-via-api.md -->
---
title: "Insert A Document Via Api\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/insert-a-document-via-api"
updated: "2026-02-17"
---


You can insert documents via a script using the `frappe.get_doc` method

### Examples:

#### 1. Insert a ToDo

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert()

---

#### 2. Insert without the user's permissions being checked:

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert(ignore_permissions = True)


---

#### 3. Submit after inserting

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert(ignore_permissions=True)
 todo.submit()

---

#### 4. Insert a document on saving of another document

 class MyType(Document):
 def on_update(self):
 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert()

----

#### 5. Insert a document with child tables:

 sales_order = frappe.get_doc({
 "doctype": "Sales Order",
 "company": "_Test Company",
 "customer": "_Test Customer",
 "delivery_date": "2013-02-23",
 "sales_order_details": [
 {
 "item_code": "_Test Item Home Desktop 100",
 "qty": 10.0,
 "rate": 100.0,
 "warehouse": "_Test Warehouse - _TC"
 }
 ]
 })
 sales_order.insert()

<!-- page: framework/framework__user__en__guides__app-development__overriding-link-query-by-custom-script.md -->
---
title: "Overriding Link Query By Custom Script\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/overriding-link-query-by-custom-script"
updated: "2026-02-17"
---


You can override the standard link query by using `set_query` via the Client Script DocType from the desk.

The `set_query` method takes one of two formats: `set_query(field_name, options_function())` for regular fields, or `set_query(field_name, child_table_name, options_function())` for fields in child tables.

### 1. Adding Filters

You can add filters to the query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
 frm.set_query("bank_account", function() {
 return {
 "filters": {
 "account_type": "Bank",
 "group_or_ledger": "Ledger"
 }
 };
 });
});
```

A more complex query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm){
 frm.set_query("bank_account", function(){
 return {
 "filters": [
 ["Bank Account", "account_type", "=", "Bank"],
 ["Bank Account", "group_or_ledger", "!=", "Group"]
 ]
 }
 });
});
```
---

### 2. Calling a Different Method to Generate Results

You can also set a server side method to be called on the query:

```js
frm.set_query("item_code", "items", function() {
 return {
 query: "erpnext.controllers.queries.item_query",
 filters: frm.doc.enquiry_type === "Maintenance" ?
 {"is_service_item": "Yes"} : {"is_sales_item": "Yes"}
 };
});
```


#### Custom Method

The custom method should return a list of items for auto select. If you want to send additional data, you can send multiple columns in the list.

Parameters to the custom method are:

```py
def custom_query(doctype, txt, searchfield, start, page_len, filters)
```

**Example:**

```py
# searches for leads which are not converted
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def lead_query(doctype, txt, searchfield, start, page_len, filters):
 return frappe.db.sql("""
 SELECT name, lead_name, company_name
 FROM `tabLead`
 WHERE docstatus < 2
 AND ifnull(status, '') != 'Converted'
 AND ({key} LIKE %(txt)s
 OR lead_name LIKE %(txt)s
 OR company_name LIKE %(txt)s)
 {mcond}
 ORDER BY
 IF(LOCATE(%(_txt)s, name), LOCATE(%(_txt)s, name), 99999),
 IF(LOCATE(%(_txt)s, lead_name), LOCATE(%(_txt)s, lead_name), 99999),
 IF(LOCATE(%(_txt)s, company_name), LOCATE(%(_txt)s, company_name), 99999),
 name, lead_name
 LIMIT %(start)s, %(page_len)s
 """.format(**{
 'key': searchfield,
 'mcond':get_match_cond(doctype)
 }), {
 'txt': "%{}%".format(txt),
 '_txt': txt.replace("%", ""),
 'start': start,
 'page_len': page_len
 })
```

**Note:** `@frappe.whitelist()` is used to expose `lead_query` to the client-side
and `@frappe.validate_and_sanitize_search_inputs` decorator is used to validate and sanitize user inputs sent through API or client-side request to avoid possible SQLi.

For more examples see:

[https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py](https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py)

<!-- page: framework/framework__user__en__guides__app-development__running-background-jobs.md -->
---
title: "Running Background Jobs\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/running-background-jobs"
updated: "2026-02-17"
---


Sometimes you may not want a user request to be executed immediately but added to a queue that will be executed by a background worker. The advantage of doing this is that your web workers remain free to execute other requests and longer jobs do not eat up all of your resources.

Frappe uses Python RQ to run background jobs. The following example illustrates how you can enqueue a job:

```python
import frappe

def long_job(arg1, arg2):
 frappe.publish_realtime('msgprint', 'Starting long job...')
 # this job takes a long time to process
 frappe.publish_realtime('msgprint', 'Ending long job...')

def enqueue_long_job(arg1, args2):
 frappe.enqueue('myapp.mymodule.long_job', arg1=arg1, arg2=arg2)
```

This will enqueue `long_job` to the queue `default`. Other available queues are `long` and `short`. You should choose the appropriate queue based on how long you estimate your enqueued job to execute.

Starting Version 14, you can also enqueue jobs at front of the queue by passing `at_front` as `True` in your enqueue call.

#### Called delayed actions on Document objects

You can also called delayed actions on document objects, for example in Stock Reconciliation if there are more than 100 items, it is executed as a background job.

Example: you can call `doc.queue_action('submit')`

Note: This only works for `save`, `submit`, `cancel`

You can also push certain actions to the background if you anticipate the execution is very large.

For example:

```python
def submit(self):
 if len(self.items) > 100:
  self.queue_action('submit')
 else:
  self._submit()
```

#### Debugging

If you are on `bench start`

You will see logs in your terminal.

Note: default worker does not auto restart, so you will have to kill bench and start again after you make changes.

<!-- page: framework/framework__user__en__guides__app-development__single-type-doctype.md -->
---
title: "Single Type Doctype\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/single-type-doctype"
updated: "2026-02-17"
---


DocTypes have a table associated with them. For example DocType **Customer** will have a table `tabCustomer` associated with it.

**Single** type DocTypes have no table associated and there is only one Document for it. This is similar to the Singleton pattern in Java. Single DocTypes are ideal for saving Settings (that are globally applicable) and for wizard / helper type forms that have no documents, but when the DocType is used for the Form UI.

The data in Single DocType is stored in `tabSingles` (`doctype`, `field`, `value`)

#### Examples

In Frappe, Single types are **System Settings** and **Customize Form**

<!-- page: framework/framework__user__en__guides__app-development__trigger-event-on-deletion-of-grid-row.md -->
---
title: "Trigger Event On Deletion Of Grid Row\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/trigger-event-on-deletion-of-grid-row"
updated: "2026-02-17"
---


To trigger an event when a row from a Child Table has been deleted (when user clicks on `delete` button), you need to add a handler the `fieldname_remove` event to Child Table, where fieldname is the fieldname of the Child Table in Parent Table declaration.

For example:

Assuming that your parent DocType is named `Item` has a Table Field linked to `Item Color` DocType with decloration name `color`.

In order to "catch" the delete event:

```js
frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // You code here
 // If you console.log(frm.doc.color) you will get the remaining color list
 }
);
```

The same process is used to trigger the add event (when user clicks on `add row` button):

```js
frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // You code here
 // If you console.log(frm.doc.color) you will get the remaining color list
 },
 color_add: function(frm) {}
});
```

Notice that the handling is be made on Child DocType Table `form.ui.on` and not on Parent Doctype so a minimal full example is:


```js
frappe.ui.form.on('Item',{
 // Your client side handling for Item
});

frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // Deleting is triggered here
 }
);
```

Handlers are:

1. fieldname_add
1. fieldname_move
1. fieldname_before_remove
1. fieldname_remove

<!-- page: framework/framework__user__en__guides__app-development__using-html-templates-in-javascript.md -->
---
title: "Using Html Templates In Javascript"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/using-html-templates-in-javascript"
updated: "2026-05-10"
---

Often while building javascript interfaces, there is a need to render DOM as an HTML template. Frappe Framework uses John Resig's Microtemplate script to render HTML templates in the Desk application.

&gt; Note 1: In Frappe we use the Jinja-like `{% raw %}{%{% endraw %}` tags to embed code rather than the standard `&lt;%`

&gt; Note 2: Never use single quotes `'` inside the HTML template.

To render a template,

1. Create a template `html` file in your app. e.g. `address_list.html`
2. Add it to `build.json` for your app (you can include it in `frappe.min.js` or your own javascript file).
3. To render it in your app, use `frappe.render(frappe.templates.address_list, {[context]})`

#### Example Template:

From `erpnext/public/js/templates/address_list.js`


```
<p>
    <button class="btn btn-sm btn-default btn-address">New Address</button>
</p>

{% for(var i=0, l=addrlist.length; i&lt;l; i++) { %}
    &lt;hr&gt;
    {%= _("Edit") %}
    {%= addr_list[i].address_type %}

    {% if(addr_list[i].is_primary_address) { %}
        {%= __("Primary") %}
    {% } %}

    {% if(addr_list[i].is_shipping_address) { %}
        {%= __("Shipping") %}
    {% } %}

    {%= addr_list[i].display %}
{% } %}

{% if(!addrlist.length) { %}
    {%= _("No address added yet.") %}
{% } %}
```

<!-- page: framework/framework__user__en__guides__automated-testing.md -->
---
title: "Automated Testing\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing"
updated: "2026-02-17"
---


Frappe Provides you a test framework to write and execute tests that can be run directly on a Continuous Integration Tool like Travis

You can write server-side unit tests or UI tests

<!-- page: framework/framework__user__en__guides__automated-testing__integration-testing.md -->
---
title: "UI Integration Testing\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/integration-testing"
updated: "2026-02-17"
---


You can write integration tests using [Cypress](https://cypress.io). It is a NodeJS based full-stack testing framework which doesn't rely on Selenium.

To write integration tests, create a `.js` file in the `cypress/integration` directory.

### Example

Here is an example of an integration test to check insertion of a To Do

```js
context('ToDo', () => {
 before(() => {
 cy.login('Administrator', 'admin');
 cy.visit('/desk');
 });

 it('creates a new todo', () => {
 cy.visit('/app/todo/new-todo-1');
 cy.fill_field('description', 'this is a test todo', 'Text Editor').blur();
 cy.get('.page-title').should('contain', 'Not Saved');
 cy.get('.primary-action').click();
 cy.visit('/desk#List/ToDo');
 cy.location('hash').should('eq', '/app/todo');
 cy.get('.list-row').should('contain', 'this is a test todo');
 });
});
```

### Running Cypress Locally

Cypress uses any chromium based browser installed on your system to run tests. Every app has it's own cypress test suite.
For example, to run test for the `frappe` app, run the following commands

```sh
cd ~/frappe-bench/apps/frappe
yarn cypress:open
```

This will open the Cypress Electron shell where you can run any test manually or run all of the tests.

![](/files/running-cypress-tests.gif)

<!-- page: framework/framework__user__en__guides__automated-testing__qunit-testing.md -->
---
title: "UI Testing with Frappe API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/qunit-testing"
updated: "2026-02-17"
---


You can either write integration tests, or directly write tests in Javascript using [QUnit](http://api.qunitjs.com/)

QUnit helps you write UI tests using the QUnit framework and native frappe API. As you might have guessed, this is a much faster way of writing tests.

### Test Runner

To write QUnit based tests, add your tests in the `tests/ui` folder of your application. Your test files must begin with `test_` and end with `.js` extension.

To run your files, you can use the **Test Runner**. The **Test Runner** gives a user interface to load all your QUnit tests and run them in the browser.

In the CI, all QUnit tests are run by the **Test Runner** using `frappe/tests/test_test_runner.py`

![](/files/test-runner.png)

### Running Tests

To run a Test Runner based test, use the `run-ui-tests` bench command by passing the name of the file you want to run.

 bench run-ui-tests --test frappe/tests/ui/test_list.js

This will pass the filename to `test_test_runner.py` that will load the required JS in the browser and execute the tests

### Debugging Tests

To debug a test, you can open it in the **Test Runner** from your UI and run it manually to see where it is exactly failing.

### Test Sequence

In Frappe UI tests are run in a fixed sequence to ensure dependencies.

The sequence in which the tests will be run will be in `tests/ui/tests.txt`
file.

### Running All UI Tests

To run all UI tests together for your app run

 bench run-ui-tests --app [app_name]

This will run all the files in your `tests/ui` folder one by one.

### Example QUnit Test

Here is the example of the To Do test in QUnit

 QUnit.test("Test quick entry", function(assert) {
 assert.expect(2);
 let done = assert.async();
 let random_text = frappe.utils.get_random(10);

 frappe.run_serially([
 () => frappe.set_route('List', 'ToDo'),
 () => frappe.new_doc('ToDo'),
 () => frappe.quick_entry.dialog.set_value('description', random_text),
 () => frappe.quick_entry.insert(),
 (doc) => {
 assert.ok(doc && !doc.__islocal);
 return frappe.set_route('Form', 'ToDo', doc.name);
 },
 () => assert.ok(cur_frm.doc.description.includes(random_text)),

 // Delete the created ToDo
 () => frappe.tests.click_page_head_item('Menu'),
 () => frappe.tests.click_dropdown_item('Delete'),
 () => frappe.tests.click_page_head_item('Yes'),

 () => done()
 ]);
 });

### Writing Test Friendly Code with Promises

Promises are a great way to write test-friendly code. If your method calls an aysnchronous call (ajax), then you should return an `Promise` object. While writing tests, if you encounter a function that does not return a `Promise` object, you should update the code to return a `Promise` object.

<!-- page: framework/framework__user__en__guides__automated-testing__unit-testing.md -->
---
title: "Unit Testing"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/unit-testing"
updated: "2026-03-06"
---

## 1.Introduction

Frappe provides some basic tooling to quickly write automated tests. There are some basic rules:

1. Test can be anywhere in your repository but must begin with `test_` and should be a `.py` file.
2. Tests must run on a site that starts with `test_`. This is to prevent accidental loss of data.
3. Test stubs are automatically generated for new DocTypes.
4. Frappe test runner will automatically build test records for dependant DocTypes identified by the `Link` type field (Foreign Key)
5. Tests can be executed using `bench run-tests`
6. For non-DocType tests, you can write simple unittests and prefix your file names with `test_`.

## Writing Tests for DocTypes

### 2.1. Writing DocType Tests:

1. Test cases are in a file named `test_[doctype].py`
2. You must create all dependencies in the test file
3. Create a Python module structure to create fixtures / dependencies

#### Example (for `test_event.py`):

```
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import frappe.defaults

from frappe.tests.utils import FrappeTestCase


def create_events():
    if frappe.flags.test_events_created:
        return

frappe.set_user("Administrator")
doc = frappe.get_doc({
    "doctype": "Event",
    "subject":"_Test Event 1",
    "starts_on": "2014-01-01",
    "event_type": "Public"
    }).insert()

doc = frappe.get_doc({
    "doctype": "Event",
    "subject":"_Test Event 2",
    "starts_on": "2014-01-01",
    "event_type": "Private"
    }).insert()

doc = frappe.get_doc({
    "doctype": "Event",
    "subject":"_Test Event 3",
    "starts_on": "2014-01-01",
    "event_type": "Public"
    "event_individuals": [{
        "person": "test1@example.com"
    }]
    }).insert()

frappe.flags.test_events_created = True


class TestEvent(FrappeTestCase):
    def setUp(self):
        create_events()

    def tearDown(self):
        frappe.set_user("Administrator")

    def test_allowed_public(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
        {"subject":"_Test Event 1"}))
        self.assertTrue(frappe.has_permission("Event", doc=doc))

    def test_not_allowed_private(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
        {"subject":"_Test Event 2"}))
        self.assertFalse(frappe.has_permission("Event", doc=doc))

    def test_allowed_private_if_in_event_user(self):
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
        {"subject":"_Test Event 3"}))

        frappe.set_user("test1@example.com")
        self.assertTrue(frappe.has_permission("Event", doc=doc))

    def test_event_list(self):
        frappe.set_user("test1@example.com")
        res = frappe.get_list("Event", filters=[["Event", "subject", "like", "_Test Event%"]], fields=["name", "subject"])
        self.assertEqual(len(res), 2)
        subjects = [r.subject for r in res]
        self.assertTrue("_Test Event 1" in subjects)
        self.assertTrue("_Test Event 3" in subjects)
        self.assertFalse("_Test Event 2" in subjects)
```

## 2. Running Tests

This function will build all the test dependencies and run your tests.  
You should run tests from "frappe_bench" folder. Without options all tests will be run.

 bench run-tests

If you need more information about test execution - you can use verbose log level for bench.

 bench --verbose run-tests

### Options:

```
 --app <appname>
 --doctype <doctype>
 --test <specifictest>
 --module <module> (Run a particular module that has tests)
 --profile (Runs a Python profiler on the test)
 --junit-xml-output<pathtoxml> (The command provides test results in the standard XUnit XML format)
```

#### 2.1. Example for app:

All applications are located in folder: "~/frappe-bench/apps".  
We can run tests for each application.

- frappe-bench/apps/erpnext/
- frappe-bench/apps/erpnext_demo/
- frappe-bench/apps/frappe/

```
 bench run-tests --app erpnext
 bench run-tests --app erpnext_demo
 bench run-tests --app frappe
```

#### 2.2. Example for doctype:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype "Activity Cost"
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.008s

 OK
```

#### 2.3. Example for test:

Run a specific case in User:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype User --test test_get_value
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.005s

 OK
```

#### 2.4. Example for module:

If we want to run tests in the module:

 /home/frappe/frappe-bench/apps/erpnext/erpnext/support/doctype/issue/test_issue.py

We should use module name like this (related to application folder)

 erpnext.support.doctype.issue.test_issue

##### Example:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --module "erpnext.stock.doctype.stock_entry.test_stock_entry"
 ...........................
 ----------------------------------------------------------------------
 Ran 27 tests in 30.549s
```

#### 2.5. Example for profile:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype "Activity Cost" --profile
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.010s

 OK
 9133 function calls (8912 primitive calls) in 0.011 seconds

 Ordered by: cumulative time

 ncalls tottime percall cumtime percall filename:lineno(function)
 2 0.000 0.000 0.008 0.004 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:187(insert)
 1 0.000 0.000 0.003 0.003 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:386(_validate)
 13 0.000 0.000 0.002 0.000 /home/frappe/frappe-bench/apps/frappe/frappe/database.py:77(sql)
 255 0.000 0.000 0.002 0.000 /home/frappe/frappe-bench/apps/frappe/frappe/model/base_document.py:91(get)
 12 0.000 0.000 0.002 0.000
```

#### 2.6 Running Tests without creating fixtures or before_tests hook

- When you are building a feature it is useful to write tests without building test dependencies (i.e build fixtures for linked objects), with `--skip-test-records`  
- You can also skip the test initialisation script with `--skip-before-tests`

Example  

```
bench --site school.erpnext.local run-tests --doctype "Student Group" --skip-test-records --skip-before-tests
```

### 3.0 FrappeTestCase

`FrappeTestCase` is Frappe Framework specific TestCase class extended from `unittest.TestCase`. Inherting this class in your tests ensures:  



1. `frappe.local.flags` and other most used local proxies are reset after test case runs.
2. database - a new [database transaction](https://frappeframework.com/docs/v14/user/en/api/database#database-transaction-model) is started before testcase begins and rolled back after tests are finished.

Usage 

```python
# app/doctype/dt/test_dt.py  
  
from frappe.tests.utils import FrappeTestCase  
  
class TestDt(FrappeTestCase):  
 @classmethod  
 def setUpClass(cls):  
 super().setUpClass() # important to call super() methods when extending TestCase.   
 ...
```

## Writing XUnit XML Tests

##### How to run:

```
bench run-tests --junit-xml-output=/reports/junit_test.xml
```

##### Example of test report:

```
 <testsuite tests="3">
 <testcase classname="foo1" name="ASuccessfulTest">
 <testcase classname="foo2" name="AnotherSuccessfulTest">
 <testcase classname="foo3" name="AFailingTest">
 <failure type="NotEnoughFoo"> details about failure </failure>
 </testcase>
 </testcase></testcase></testsuite>
```

It’s designed for the CI Jenkins, but will work for anything else that understands an XUnit-formatted XML representation of test results.

#### Jenkins configuration support:

1. You should install xUnit plugin - [https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin)
2. After installation open Jenkins job configuration, click the box named “Publish JUnit test result report” under the "Post-build Actions" and enter path to XML report:

(Example: *reports/*.xml*)

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
