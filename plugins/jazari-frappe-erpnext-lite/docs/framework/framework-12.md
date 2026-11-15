<!-- Frappe documentation: framework, part 12 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__bench__reference__execute.md -->
---
title: "bench execute"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/execute"
updated: "2026-05-10"
---

The `bench execute` command lets you run Python functions from the command line. This is useful for running one-off tasks, debugging, or executing custom scripts.

The command automatically sets up the database connection and initializes the Frappe framework for the site, so you can directly call functions that interact with the database without any setup code.

## Basic Usage

```bash
bench --site [site-name] execute [path.to.method]
```

## Simple Examples

```bash
bench --site frappe.test execute frappe.clear_cache
```

This runs the `frappe.clear_cache()` function on your site.

```bash
bench --site frappe.test execute frappe.utils.get_site_info
```

This runs the `frappe.utils.get_site_info()` function on your site and prints the output.

## Passing Arguments

You can pass arguments directly after the method name:

```bash
bench --site frappe.test execute frappe.get_doc User Administrator
```

This calls `frappe.get_doc("User", "Administrator")`.

```bash
bench --site frappe.test execute frappe.db.get_value DocType User name
```

This calls `frappe.db.get_value("DocType", "User", "name")`.

### JSON arguments

Arguments are automatically parsed as JSON when possible:

```bash
bench --site frappe.test execute frappe.db.exists User Administrator
```

The string "Administrator" is kept as a string, but numbers and booleans are converted:

```bash
bench --site frappe.test execute some_function 123 true false
```

This passes the integer `123` and booleans `True` and `False`.

## Named Arguments (kwargs)

Use `--` prefix for named arguments:

```bash
bench --site frappe.test execute frappe.db.get_value --doctype User --filters '{"name":"Administrator"}' --fieldname email
```

This calls:

```python
frappe.db.get_value(doctype="User", filters={"name": "Administrator"}, fieldname="email")
```

### Boolean flags

Named arguments without values become `True`:

```bash
bench --site frappe.test execute frappe.get_list User --ignore_permissions
```

This calls `frappe.get_list("User", ignore_permissions=True)`.

### Mixing positional and named arguments

```bash
bench --site frappe.test execute frappe.get_list User --limit 5
```

This calls `frappe.get_list("User", limit=5)`.

## Running Python Expressions

You can run Python expressions directly:

```bash
bench --site frappe.test execute "frappe.db.count('User')"
```

You can call different types of Python callables:

```bash
# Method on a returned object
bench --site frappe.test execute "frappe.get_doc('User', 'Administrator').reload()"
```

## More Examples

```bash
# Clear cache for a specific DocType
bench --site frappe.test execute frappe.clear_cache --doctype "Sales Order"

# Get a document
bench --site frappe.test execute frappe.get_doc User Administrator

# Count records
bench --site frappe.test execute frappe.db.count User

# Run a whitelisted method
bench --site frappe.test execute myapp.api.my_function --param1 value1 --param2 value2

# Check if a record exists
bench --site frappe.test execute frappe.db.exists User guest

# Get configuration value
bench --site frappe.test execute frappe.conf.get developer_mode

# Execute a DocType method
bench --site frappe.test execute "frappe.get_doc('User', 'Administrator').get_fullname()"

# Chain operations with Python expressions
bench --site frappe.test execute "frappe.get_doc('User', 'Administrator').add_roles('System Manager')"
```

## Profiling

Use the `--profile` flag to see performance statistics:

```bash
bench --site frappe.test execute frappe.db.get_list --profile --doctype "Sales Order" --limit 1000
```

This prints the top 50% of function calls sorted by cumulative time.

```bash
        42084 function calls (41224 primitive calls) in 0.094 seconds

   Ordered by: cumulative time
   List reduced from 801 to 401 due to restriction &lt;0.5&gt;

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/2    0.000    0.000    0.091    0.046 {built-in method builtins.eval}
        1    0.000    0.000    0.091    0.091 &lt;bench execute&gt;:1(&lt;module&gt;)
        1    0.000    0.000    0.091    0.091 ~/frappe-bench/apps/frappe/frappe/database/database.py:830(get_list)
     11/1    0.000    0.000    0.091    0.091 ~/frappe-bench/apps/frappe/frappe/__init__.py:1337(get_list)
       31    0.000    0.000    0.073    0.002 ~/frappe-bench/apps/frappe/frappe/database/database.py:183(sql)
       29    0.000    0.000    0.072    0.002 ~/frappe-bench/apps/frappe/frappe/query_builder/utils.py:126(execute_query)
     18/5    0.000    0.000    0.071    0.014 ~/frappe-bench/apps/frappe/frappe/utils/caching.py:125(site_cache_wrapper)
    20/12    0.000    0.000    0.070    0.006 ~/frappe-bench/apps/frappe/frappe/model/meta.py:72(get_meta)
      7/3    0.000    0.000    0.070    0.023 ~/frappe-bench/apps/frappe/frappe/model/utils/__init__.py:132(is_virtual_doctype)
        2    0.000    0.000    0.069    0.034 ~/frappe-bench/apps/frappe/frappe/model/meta.py:149(__init__)
       31    0.000    0.000    0.066    0.002 ~/frappe-bench/apps/frappe/frappe/database/database.py:371(execute_query)
       31    0.000    0.000    0.066    0.002 ~/frappe-bench/env/lib/python3.14/site-packages/MySQLdb/cursors.py:162(execute)
       31    0.000    0.000    0.066    0.002 ~/frappe-bench/env/lib/python3.14/site-packages/MySQLdb/cursors.py:325(_query)
       31    0.000    0.000    0.065    0.002 ~/frappe-bench/env/lib/python3.14/site-packages/MySQLdb/connections.py:276(query)
       31    0.065    0.002    0.065    0.002 {function Connection.query at 0x10be545c0}
       16    0.000    0.000    0.056    0.003 ~/frappe-bench/apps/frappe/frappe/database/database.py:592(get_values)
        2    0.000    0.000    0.034    0.017 ~/frappe-bench/apps/frappe/frappe/model/meta.py:166(process)
     31/2    0.000    0.000    0.034    0.017 ~/frappe-bench/apps/frappe/frappe/model/document.py:187(__init__)
        2    0.000    0.000    0.034    0.017 ~/frappe-bench/apps/frappe/frappe/model/meta.py:157(load_from_db)
        2    0.000    0.000    0.034    0.017 ~/frappe-bench/apps/frappe/frappe/model/document.py:233(load_from_db)
     11/1    0.000    0.000    0.025    0.025 ~/frappe-bench/apps/frappe/frappe/model/qb_query.py:26(execute)
    27/13    0.000    0.000    0.022    0.002 ~/frappe-bench/apps/frappe/frappe/query_builder/utils.py:62(get_query)
        2    0.000    0.000    0.021    0.011 ~/frappe-bench/apps/frappe/frappe/model/meta.py:422(apply_property_setters)
        2    0.000    0.000    0.018    0.009 ~/frappe-bench/apps/frappe/frappe/model/document.py:304(load_children_from_db)
    27/13    0.000    0.000    0.018    0.001 ~/frappe-bench/apps/frappe/frappe/database/query.py:215(get_query)
        2    0.000    0.000    0.016    0.008 ~/frappe-bench/apps/frappe/frappe/database/database.py:514(get_value)
    27/13    0.000    0.000    0.015    0.001 ~/frappe-bench/apps/frappe/frappe/database/query.py:344(apply_fields)
        1    0.000    0.000    0.014    0.014 ~/frappe-bench/apps/frappe/frappe/database/query.py:1280(apply_field_permissions)
        1    0.000    0.000    0.013    0.013 ~/frappe-bench/apps/frappe/frappe/database/query.py:928(_get_cached_permitted_fields)
        1    0.000    0.000    0.013    0.013 ~/frappe-bench/apps/frappe/frappe/model/__init__.py:216(get_permitted_fields)
        1    0.000    0.000    0.013    0.013 ~/frappe-bench/apps/frappe/frappe/model/meta.py:677(get_permitted_fieldnames)
        1    0.000    0.000    0.013    0.013 ~/frappe-bench/apps/frappe/frappe/model/meta.py:720(get_permlevel_access)
        2    0.000    0.000    0.013    0.007 ~/frappe-bench/apps/frappe/frappe/__init__.py:384(get_roles)
        2    0.000    0.000    0.013    0.007 ~/frappe-bench/apps/frappe/frappe/permissions.py:522(get_roles)
        2    0.000    0.000    0.013    0.007 ~/frappe-bench/apps/frappe/frappe/utils/redis_wrapper.py:230(hget)
        1    0.000    0.000    0.013    0.013 ~/frappe-bench/apps/frappe/frappe/permissions.py:530(get)
        1    0.000    0.000    0.012    0.012 ~/frappe-bench/env/lib/python3.14/site-packages/redis/client.py:1163(get_message)
        1    0.000    0.000    0.012    0.012 ~/frappe-bench/env/lib/python3.14/site-packages/redis/client.py:979(parse_response)
        1    0.000    0.000    0.012    0.012 ~/frappe-bench/env/lib/python3.14/site-packages/redis/client.py:960(_execute)
       13    0.000    0.000    0.009    0.001 ~/frappe-bench/apps/frappe/frappe/model/meta.py:108(get_table_columns)
       13    0.000    0.000    0.009    0.001 ~/frappe-bench/apps/frappe/frappe/database/database.py:1356(get_table_columns)
       13    0.000    0.000    0.009    0.001 ~/frappe-bench/apps/frappe/frappe/database/database.py:1337(get_db_table_columns)
```

## Running on Multiple Sites

Execute a command on all sites:

```bash
bench --site all execute frappe.clear_cache
```

Or specific sites:

```bash
bench --site site1.local --site site2.local execute frappe.clear_cache
```

## Notes

- **Database**: Changes are automatically committed on success and rolled back on error
- **Return Values**: Return values are printed as JSON; `None` returns print nothing
- **Error Handling**: Errors exit with an error code and print the full traceback
- **Security**: Any Python function can be executed, not just whitelisted ones - use carefully in production

## Using the --args and --kwargs Options (Legacy)

&gt; **Note**: The `--args` and `--kwargs` options are the old format and are not encouraged. Use the direct argument passing methods shown above instead.

You must use the `--args` and `--kwargs` options with Python syntax. These values must be enclosed in quotes and will be evaluated as Python code (using `eval()`), not parsed as JSON.

### Pass a list of arguments

```bash
bench --site frappe.test execute frappe.db.get_value --args "['User', 'Administrator', 'email']"
```

### Pass a dictionary of keyword arguments

```bash
bench --site frappe.test execute frappe.db.set_value --kwargs "{'doctype': 'User', 'name': 'Administrator', 'fieldname': 'enabled', 'value': 1}"
```

### Combine both

```bash
bench --site frappe.test execute frappe.db.get_value --args "['User', 'Administrator']" --kwargs "{'fieldname': 'email'}"
```

<!-- page: framework/framework__user__en__bench__reference__list-apps.md -->
---
title: "bench list-apps\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/list-apps"
updated: "2026-02-17"
---


## Usage

```bash
bench list-apps [OPTIONS]
```

## Description

List all the Frappe Applications installed on the specified site. The
information shown by the command is fetched from the **Installed Applications**
DocType which tracks the latest version of the apps, the site was migrated to.
The global default `installed_apps` is used as fallback.

Multi-site support has been added in Version 13. To see the summary for all
sites, run the command with site's value as `all`.

## Options

 - `--format`, `-f` Choose the format for listing apps installed on the
 specified site, options being "text" and "json". Default is "json".

### Examples

1. List apps installed on all sites.

 ```bash
 bench --site all list-apps
 ```

1. List apps installed on all sites in parsable JSON format.

 ```bash
 bench --site all list-apps --format json
 ```

1. List apps installed on a specific site in text format.

 ```bash
 bench --site {site} list-apps --format text
 ```

 ```bash
 bench --site {site} list-apps -f text
 ```

 ```bash
 bench --site {site} list-apps
 ```

<!-- page: framework/framework__user__en__bench__reference__migrate.md -->
---
title: "bench migrate\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/migrate"
updated: "2026-02-17"
---


## Usage

```bash
bench migrate [OPTIONS]
```

## Description

The migrate command updates the site's state to the current available apps. It
performs a range of tasks, in order:

- Run `before_migrate` Hooks
- Run Application Patches
- Synchronize Database Schema and Background Jobs
- Synchronize Fixtures
- Synchronize Dashboards, Desktop Icons and Web Pages
- Updates Translations
- Rebuild Search Index for all routes
- Run `after_migrate` Hooks

This operation also updates the `touched_tables.json` file for the respective
file and updates the App Versions in the "Installed Applications" DocType.

## Flags

 - `--skip-failing` Skip patches that fail to run
 - `--skip-search-index` Skip search indexing for web documents

## Examples

1. Run migrations on an existing site.

 ```bash
 bench --site {site} migrate
 ```

1. Run migrations skipping rebuilding search index for web documents

 ```bash
 bench --site {site} migrate --skip-search-index
 ```

2. Run migrations skipping any failing patches.


 ```bash
 bench --site {site} migrate --skip-failing
 ```

> Note: Skipping failing patches is not recommended for production use

<!-- page: framework/framework__user__en__bench__reference__new-site.md -->
---
title: "bench new-site"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/new-site"
updated: "2026-02-17"
---

Usage
-----


```
bench new-site [OPTIONS] SITE
```
Description
-----------

Create a new Frappe site. This operation creates a new folder under `./sites` which will contain all the site information for the site and also creates a new database in your DBMS with all of Frappe's Modules and DocTypes installed.

The site config, which can be found under `./sites/{site}/site_config.json` maintains information about the site's state. For more information about it, check out [this guide](/framework/v14/user/en/introduction).

If site creation fails due to any reason, you'll be prompted as to whether you'd like to rollback the changes made, which are the creation of the site directory, and the creation of a database and database user.

Options
-------

* `--db-name` Set the Database name for new site - also used as the database username if not specified separate
* `--db-user` From v16 onwards, choose the database user name OR specify an existing user+password combination
* `--db-password` Set the Database password for new site, or password for existing specified database user.
* `--db-type` Select the Database Type for new site, options being "postgres" or "mariadb". Default is "mariadb"
* `--db-host` Set Database Host for new site
* `--db-port` Set Database Port for new site
* `--db-root-username` Specify Root username for MariaDB or Postgres
* `--db-root-password` Specify Root password for MariaDB or Postgres
* `--admin-password` Specify the Administrator password for new site
* `--source_sql` Initiate database with a SQL file
* `--install-app` Install app after installation

Flags
-----

* `--no-mariadb-socket` Set MariaDB host to % and use TCP/IP Socket instead of using the UNIX Socket
* `--verbose` Add Verbosity
* `--force` Force restore if the site or a database with the same name already exists

Examples
--------

1. Create a new site.


```
bench new-site {site}
```
2. Create a new *PostgreSQL* site.


```
bench new-site {site} --db-type postgres
```
3. Create a new site while skipping the interactive prompts for


	* Submitting the Site's *Administrator* Password
	* Submitting the *MariaDB Root* Password
	
	
	```
	bench new-site {site}
	   --admin-password {admin-password}
	   --db-root-password {mariadb-password}
	```
4. Create a new site with non-default and autogenerated values.


```
bench new-site {site} --db-type {type}
   --db-name {name}
   --db-user {user}
   --db-password {pass}
   --db-host {host}
   --db-port {port}
```
5. Create a new site with a MariaDB non-root user with database creation privileges.


```
bench new-site {site}
   --db-root-username {user}
   --db-root-password {pass}
```
6. Create a new site with an app *(available on current bench)* installed.


```
bench new-site {site} --install-app {app}
```

<!-- page: framework/framework__user__en__bench__reference__partial-restore.md -->
---
title: "bench partial-restore\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/partial-restore"
updated: "2026-02-17"
---


## Usage

```bash
bench partial-restore [OPTIONS] SQL_FILE_PATH
```

## Description

You may want to restore only specific tables you've backed up to a site. You have
likely taken partial backups using the `--only`, `--exclude` options in `bench backup`.

The `partial-restore` command may be used to restore sites using partial backups. The
partial backup files may be gzip compressed or plain SQL files. In essence, you can
restore anything from SQL files using this command.

## Arguments

 - `SQL_FILE_PATH` Path to the database source file. The path may be relative from
the bench directory root, or the sites folder. It may also be an absolute path.

> To learn more about relative and absolute paths, on Wikipedia click [here](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths).

## Flags

 - `-v`, `--verbose` Add verbosity

## Examples

1. Restore with partial backups on a site.

 ```bash
 bench --site {site} partial-restore -v {/path/to/sql/file}
 ```

<!-- page: framework/framework__user__en__bench__reference__reinstall.md -->
---
title: "bench reinstall"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/reinstall"
updated: "2026-02-17"
---


## Usage

```bash
bench reinstall [OPTIONS]
```

## Description

Reinstall a site with the current apps. This will wipe all site data and start
afresh. This is considered a destructive operation, hence, contains an
interactive confirmation prompt by default.

> Note: This feature only exists for **MariaDB** sites currently. In the future,
> they may be extended for **PostgreSQL** support as well.

## Options

 - `--admin-password` Administrator Password for reinstalled site
 - `--mariadb-root-username` Root username for MariaDB
 - `--mariadb-root-password` Root password for MariaDB

## Flags

 - `--yes` Skip confirmation for reinstall


## Examples

1. Reinstall a site skipping the prompts for:
 - Confirmation for operation
 - MariaDB Root Password
 - Administrator Password

 ```bash
 bench reinstall --site {site} --yes
 --mariadb-root-password {db-pass}
 --admin-password {admin-pass}
 ```

1. Reinstall a site using an alternative user with *DBMS SUPER* privileges.

 ```bash
 bench reinstall
 --mariadb-root-username {db-user}
 --mariadb-root-password {db-pass}
 ```

<!-- page: framework/framework__user__en__bench__reference__restore.md -->
---
title: "bench restore\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/restore"
updated: "2026-02-17"
---


## Usage

```bash
bench restore [OPTIONS] SQL_FILE_PATH
```

## Description

Bench CLI can be used to restore an existing site to a previous state. Using the
`bench restore` command, a site may be restored with the specific database and
file restores. Downgrades aren't supported for Frappe Sites; when a downgrade is
detected, an interactive prompt will pop up before the site restore begins.

The least requirement for performing a restore operation is having the database
file on your local filesystem. The specified path may be relative to the bench
or sites folder, although absolute paths often work best.

The specified database backup file may have the `sql.gz` or `sql` extension. For
public and private file backup archives, the default is `tar`, but since **Version
13**, compressed archives with the extension `tgz` are also supported.

> Note: As of this point, there's no way to restore only files using this
> command.

## Arguments

 - `SQL_FILE_PATH` Path to the database source file. The path may be relative from
the bench directory root, or the sites folder. It may also be an absolute path.

> To learn more about relative and absolute paths, on Wikipedia click [here](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths).

## Options

 - `--db-root-username` Root username for MariaDB or Postgres
 - `--db-root-password` Root password for MariaDB or Postgres
 - `--db-name` Database name for site in case it is a new one
 - `--admin-password` Administrator password for new site
 - `--install-app` Install app after installation
 - `--with-public-files` Restores the public files of the site, given path to
 its archive file
 - `--with-private-files` Restores the private files of the site, given path to
 its archive file

## Flags

 - `--force` Ignore the site downgrade warning, if applicable. This is **not
 recommended** unless you're fully aware of the consequences


## Examples

1. Restore a site with files

 ```bash
 bench --site {site} restore {path/to/database/file}
 --with-public-files {path/to/public/archive}
 --with-private-files {path/to/private/archive}
 ```

1. Bypass DBMS root interactive prompt by passing values in options

 ```bash
 bench --site {site} restore {path/to/database/file}
 --db-root-username {db-user}
 --db-root-password {db-pass}
 ```

1. Specify new app to install after site restore

 ```bash
 bench --site {site} restore {path/to/database/file}
 --install-app {app}
 ```

1. Specify custom database name for the restored site

 ```bash
 bench --site {site} restore {path/to/database/file}
 --db-name {custom-db-name}
 ```

1. Reset the admin password for the restored site

 ```bash
 bench --site {site} restore {path/to/database/file}
 --admin-password {admin-pass}
 ```

<!-- page: framework/framework__user__en__bench__reference__set-config.md -->
---
title: "bench set-config\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/set-config"
updated: "2026-02-17"
---


## Usage

```bash
bench set-config [OPTIONS] KEY VALUE
```

## Description

Bench provides a wrapper command to insert or update values in the site config
files. You can update values in your site's `site_config.json`, along with the
bench directory's `common_site_config.json` through the same command.

To read more about site configuration and understanding key precedence, refer to
the docs [here](/framework/v14/user/en/basics/site_config).

## Flags

 - `-g`, `--global` Set value in the Bench's Common Site Config
 - `-p`, `--parse` Parse given value instead of string. You can use this to set
 dict and list values. This was `--as-dict` in earlier versions.

## Examples

1. Enable tests for given site.

 ```bash
 bench --site {site} set-config allow_tests true
 ```

1. Enable tests for all sites.

 ```bash
 bench --site all set-config allow_tests true
 ```

 Using the above command, each site's `site_config.json` will have the
 key-value `"allow_tests": true`. This allows running tests on all of the
 sites.

 ```bash
 bench set-config -g allow_tests true
 ```

 Using the above command, the bench's `common_site_config.json` will have the
 key-value `"allow_tests": true`. This will allow each site on the bench to
 have tests run unless they have a value defined for the sma in their
 `site_config.json`.

1. Set a dict value in your site's `frappe.conf`

 ```bash
 bench --site {site} set-config backup '{"includes": ["Not", "ToDo"]}' --parse
 ```

 You can now access the list in code as `frappe.conf.backup.get("includes")`.

<!-- page: framework/framework__user__en__bench__reference__show-config.md -->
---
title: "bench show-config"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/show-config"
updated: "2026-02-17"
---

Usage
-----


```
bench show-config [OPTIONS]
```
Description
-----------

The applied configuration for your sites gets applied as a combination of the bench directory's `common_site_config.json` and the site's own `site_config.json`. Bench provides an interface to view the applied `frappe.conf` values for your sites. You may choose to access this information in tabular or JSON formats.

To read more about site configuration and understanding key precedence, refer to the docs [here](/framework/v14/user/en/basics/site_config).

Flags
-----

* `-f`, `--format` Choose the format for listing apps installed on the specified site, options being "text" and "json". Default is "text".

Examples
--------

1. Show site config for all sites in JSON format.


```
bench --site all show-config -f json
```
2. Show the site config in tabular form.


```
bench --site {site} show-config --format text
```

```
bench --site {site} show-config -f text
```

```
bench --site {site} show-config
```

<!-- page: framework/framework__user__en__bench__reference__transform-database.md -->
---
title: "bench transform-database"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/transform-database"
updated: "2026-02-17"
---


> This command is added in **Version 14**, and supports only **MariaDB**
> 
> 

Usage
-----


```
bench transform-database [OPTIONS] table
```
Description
-----------

The `transform-database` command allows you to manage the settings of your site's tables. At this point, you can switch engines and row_format settings for select tables on your site database.


> MariaDB 10.6 deprecated the COMPRESSED ROW_FORMAT which was Frappe's default option for a very long time. This command was added to handle upgrades to later versions of MariaDB. For more information on this, refer to the [PR](https://github.com/frappe/frappe/pull/13954).
> 
> 

Options
-------

* `--table` Comma separated name of tables to convert. To convert all tables, pass 'all' **[required]**
* `--engine` Choice of storage engine for said table(s). Options available are *InnoDB* and *MyISAM*.
* `--row_format` Set *ROW_FORMAT* parameter for said table(s). Options available are *DYNAMIC*, *COMPACT*, *REDUNDANT*, *COMPRESSED*.

Flags
-----

* `failfast` Exit on first failure occurred

### Examples

1. Consider a scenario where you'd want to change the engine of a table *"tabAccess Record"* to `MyISAM`. You may want to do this if it's a log table that's dealing with huge volumes of writes and very little reads.


```
bench --site {site} transform-database --table 'tabAccess Record' --engine 'MyISAM'
```
2. You've upgraded MariaDB on your current server from 10.3 to 10.7 and you want to convert all the tables that used the COMPRESSED row_format to the new default, ie `DYNAMIC`. You'd want to run the following command.


```
bench --site {site} transform-database --table 'all' --row_format 'DYNAMIC'
```

<!-- page: framework/framework__user__en__bench__reference__trim-database.md -->
---
title: "bench trim-database\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/trim-database"
updated: "2026-02-17"
---


## Usage

```bash
bench trim-database [OPTIONS]
```

## Description

Deleting DocTypes from the list view may not delete their corresponding tables from
the database. Migrations may leave ghost tables in your Site Database at times. This
 may be done for the sake of redundancy, for recovery in case your data is corrupted
 or lost, or simply, in cases of human error.

This command drops any tables that seem to be remnants like the above mentioned. It will
attempt a partial backup of the tables before dropping them. In case, these tables were
required, and were dropped errenously, you can restore them in your site's database using
the [`partial-restore`](/framework/v14/user/en/bench/reference/partial-restore) command.

## Options

 - `--format`, `-f` Set output format. Available options are JSON and Table. Defaults to Table.

## Flags

 - `--dry-run` Show what would be deleted.
 - `--no-backup` Do not backup the site prior to the trimming.

### Examples

1. You want to figure out what data will be deleted if you run this command? Run it with the
 `--dry-run` flag.

 ```bash
 bench --site {site} trim-database --dry-run
 ```

1. Want to build over this command and need the data to be machine parsable? Set the output
 `--format` to **json**.

 ```bash
 bench --site {site} trim-database --format json
 ```

<!-- page: framework/framework__user__en__bench__reference__trim-tables.md -->
---
title: "bench trim-tables\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/trim-tables"
updated: "2026-02-17"
---


## Usage

```bash
bench trim-tables [OPTIONS]
```

## Description

Docfields removed from a particular DocType may not be deleted from their
Database tables. This is by design to prevent premature data loss in Frappe.
This won't be problematic for the most part, however, at some point you may face
issues due to this lingering data.

Some benefits of regular table trimming are:

- Smaller backup sizes
- Reduced time taken to backup sites
- Reduced Site Database Usages
- Optimized queries in case of `SELECT *`
- Database is clean and doesn't have anything hidden or redundant data

This command modifies the schema of tables in your site's database. It will by default,
take a full backup of your entire database before modifying them. In case, these tables
 were modified errenously, you can restore your site to it's original state using
the [`restore`](/framework/v14/user/en/bench/reference/restore) command.

## Options

 - `--format`, `-f` Set output format. Available options are JSON and TEXT.
 Defaults to TEXT.

## Flags

 - `--dry-run` Show what would be deleted
 - `--no-backup` Do not backup the site. This is not recommended since this is a
 destructive operation.

### Examples

1. There maybe a lot of lingering columns taking up the space. Perhaps you figured this out
 when you got an error that row size limit has reached while customizing your DocType. To
 be sure that there aren't any ghost columns, or old hidden fields taking up the space, you
 can be sure by running

 ```bash
 bench --site {site} trim-tables --dry-run
 ```

<!-- page: framework/framework__user__en__bench__reference__uninstall-app.md -->
---
title: "bench uninstall-app\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/reference/uninstall-app"
updated: "2026-02-17"
---


## Usage

```bash
bench uninstall-app [OPTIONS] APP
```

## Description

Remove Application and linked doctypes, modules from the site. Executing the
vanilla command will check if the app exists on site before attempting to delete
its modules and doctypes. The application may not be necessarily installed on
the bench to run the `uninstall-app` command.

## Flags

 - `-y`, `--yes` To bypass confirmation prompt for uninstalling the app
 - `--dry-run` List all doctypes that will be deleted
 - `--no-backup` Do not backup the site
 - `--force` Force remove the app from site

## Examples

1. Perform a dry run to see what would happen on running it on a particular
 site.

 ```bash
 bench --site {site} uninstall-app {app} --dry-run
 ```

1. Don't take a backup before the application uninstall operation.

 ```bash
 bench --site {site} uninstall-app {app} --no-backup
 ```

1. Use force to uninstall application from site.

 ```bash
 bench --site {site} uninstall-app {app} --force
 ```

2. Skip the interactive prompt for confirmation of uninstall.

 ```bash
 bench --site {site} uninstall-app {app} --yes
 ```

<!-- page: framework/framework__user__en__bench__resources__background-services.md -->
---
title: "Background Services\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/resources/background-services"
updated: "2026-02-17"
---


Running an active Frappe environment requires the running of various system
level services and some Frappe processes.

The system level services, apart from your choice of database solutions and
Redis will depend on your deployment architecture and strategy. As for the
Frappe services, they are defined in the
[Procfile](/framework/v14/user/en/bench/resources/bench-procfile) for development benches
and config/supervisor.conf for production benches.

System Processes
-----------------

These processes are handled at a system level and may have configs setup via
bench or some other Frappe deployment management tool.

 * MariaDB/PostgreSQL (Database)
 * Redis (Queues for background workers, and Caching)
 * NGINX (Reverse Proxy for production deployment)
 * Supervisor (Process Management for bench's non containerized production deployment)

Frappe Processes
----------------

These processes may be triggered manually or via a process manager. However,
they are defined in Frappe's codebase and are managed by the same.

* WSGI Server

The WSGI server is responsible for responding to the HTTP requests to frappe. In
a development scenario, `bench serve` or `bench start` start the Werkzeug server.
For production setups, Bench uses Gunicorn (automatically configured in supervisor).

* Redis Worker Processes

The worker processes execute background jobs in the Frappe system.

These processes are automatically started when `bench start` is run and for production
are configured in supervisor configuration.

* Scheduler Process

The Scheduler process schedules enqeueing of scheduled jobs in the Frappe
system. This process is automatically started when `bench start` is run and for
production are configured in supervisor configuration.

<!-- page: framework/framework__user__en__bench__resources__bench-commands-cheatsheet.md -->
---
title: "Bench Commands Cheatsheet"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/resources/bench-commands-cheatsheet"
updated: "2026-02-17"
---

### Printable Bench CLI Cheatsheet

Grab a A4 size printable cheatsheet of the most important Bench CLI commands [here](/files/Bench Cheatsheet v1.1.pdf). Download, print and put it on your desk!

### General Usage

* `bench --version` - Show bench version
* `bench version` - Show version of all apps
* `bench src` - Show bench repo directory
* `bench --help` - Show all commands and help
* `bench [command] --help` - Show help for command
* `bench init [bench-name]` - Create a new bench (Run from home dir)


	+ `--python TEXT` Path to Python Executable.
	+ `--ignore-exist` Ignore if Bench instance exists.
	+ `--apps_path TEXT` path to json files with apps to install after init
	+ `--frappe-path TEXT` path to frappe repo
	+ `--frappe-branch TEXT` Clone a particular branch of frappe
	+ `--clone-from TEXT` copy repos from path
	+ `--clone-without-update` copy repos from path without update
	+ `--no-procfile` Pull changes in all the apps in bench
	+ `--no-backups` Run migrations for all sites in the bench
	+ `--no-auto-update` Build JS and CSS artifacts for the bench
	+ `--skip-redis-config-generation` Skip redis config generation if already specifying the common-site-config file
	+ `--verbose` Verbose output during install
* `bench --site [site-name] COMMAND` - Specify site for command
* `bench update` - Pulls changes for bench-repo and all apps, applies patches, builds JS and CSS, and then migrates.


	+ `--pull` Pull changes in all the apps in bench
	+ `--patch` Run migrations for all sites in the bench
	+ `--build` Build JS and CSS artifacts for the bench
	+ `--bench` Update bench
	+ `--requirements` Update requirements
	+ `--restart-supervisor` restart supervisor processes after update
	+ `--no-backup` Don't take a backup before update
	+ `--reset` Ignore local changes and update
	+ `--dev` Enable developer mode on the new bench and install developer dependencies which are required for running tests.
* `bench restart` Restart all bench services
* `bench backup` Create a backup of the default site.

Backup will be saved to `~/frappe-bench/sites/{your site}/private/backups/`.
* `bench backup-all-sites` Backup all sites


	+ `--with-files` Backup site with files
* `bench restore` Restore


	+ `--with-private-files` Restore site with private files (Path to tar file)
	+ `--with-public-files` Restore site with public files (Path to tar file)
* `bench migrate` Run patches, sync schema and rebuild files/translations


	+ `--rebuild-website TEXT` Rebuild webpages after migration
* `bench migrate-env [python-version]` Will migrate the virtual environment to the desired python version
* `bench --site [sitename] set-admin-password [password]` Will reset the administrator password
* `bench destroy-all-sessions` Destroys all sessions

### Config

* `bench config` - Change bench configuration


	+ `auto_update [on/off]` Enable/Disable auto update for bench
	+ `dns_multitenant [on/off]` Enable/Disable DNS Multitenancy
	+ `http_timeout` Set http timeout
	+ `restart_supervisor_on_update` Enable/Disable auto restart of supervisor
	+ `serve_default_site` Configure nginx to serve the default site on
	+ `update_bench_on_update` Enable/Disable bench updates on running bench...
* `bench setup` - Setup components


	+ `auto-update` Add cronjob for bench auto update
	+ `backups` Add cronjob for bench backups
	+ `config` overwrite or make config.json
	+ `env` Setup virtualenv for bench
	+ `nginx` generate config for nginx
	+ `procfile` Setup Procfile for bench start
	+ `production` setup bench for production
	+ `redis` generate config for redis cache
	+ `socketio` Setup node deps for socketio server
	+ `sudoers` Add commands to sudoers list for execution...
	+ `supervisor` generate config for supervisor
	+ `add-domain` add custom domain for site
	+ `firewall` setup firewall and block all ports except 22, 80 and 443
	+ `ssh-port` change the default ssh connection port
	+ `requirements`Update Python and Node packages
	
	
		- `--node` Update only Node packages
		- `--python` Update only Python packages
		- `--dev` Update only Python development dependencies.
* `bench set-nginx-port [sitename] [port]` - Set site's port in Production

### Development

* `bench new-app [app-name]` Creates a new app
* `bench get-app [repo-link]` - Downloads an app from a git repository and installs it


	+ `--branch [branch-name]` Fetches specific branch of app
* `bench install-app [app-name]` Installs existing app
* `bench remove-from-installed-apps [app-name]` Remove app from the list of apps
* `bench uninstall-app [app-name]` Delete app and everything linked to the app (Bench needs to be running)
* `bench remove-app [app-name]` Remove app from the bench entirely
* `bench --site [sitename] --force reinstall` Reinstall with fresh database (Caution: Will wipe out old database)
* `bench new-site [sitename]` - Creates a new site


	+ `--db-name` Database name
	+ `--db-host` Custom database host URL for remote connection
	+ `--db-port` Custom database listening port (eg. port other than the default 3306)
	+ `--mariadb-root-username` Root username for MariaDB
	+ `--mariadb-root-password` Root password for MariaDB
	+ `--admin-password` Administrator password for new site
	+ `--verbose` Verbose
	+ `--force` Force restore if site/database already exists
	+ `--source_sql` Initiate database with a SQL file
	+ `--install-app` Install app after installation`
* `bench use [site]` Sets a default site
* `bench drop-site` Removes site from disk and database completely


	+ `--root-login`
	+ `--root-password`
* `bench set-config [key] [value]` Adds a key-value pair to site's config file
* `bench console` Opens a IPython console in the bench venv


	+ `--autoreload` Reload changes to code automatically
* `bench execute` Execute a method inside any app.


	+ Eg : `bench execute frappe.utils.scheduler.enqueue_scheduler_events`
* `bench --site [sitename] mariadb` Opens SQL Console
* `bench --site [sitename] export-fixtures [--app TEXT]` Export the [records defined in the app's hooks](/framework/v14/user/en/python-api/hooks#fixtures) as JSON files.
* `bench run-tests` Run tests


	+ `--app` App Name
	+ `--doctype` DocType to run tests for
	+ `--test` Specific Test
	+ `--module` Run a particular module that has tests
	+ `--profile` Runs a Python profiler on the test
* `bench disable-production` Disables production environment
* `bench serve` Start a development web server on `0.0.0.0`


	+ `--port` Start the web server on a different port (default: 8000)
	+ `--profile` Add a profiler middleware that prints exactly which backend methods get called, how often and how long it takes.
	+ `--proxy` The development server may be run behind a proxy, e.g. ngrok / localtunnel
	+ `--noreload` Disable automatic restarting of the server when files change.
	+ `--nothreading` Disable handling of concurrent requests using threads. Can lead to unexpected behavior when multiple threads are required (for example during PDF generation).
	+ `--with-coverage` Measure code coverage and create a report `coverage.xml` in the `sites/` folder. Also activates `--noreload` and `--nothreading`.

### Scheduler

* `bench enable-scheduler` - Enables Scheduler that will run scheduled tasks
* `bench doctor` - Get diagnostic info about background workers
* `bench show-pending-jobs`- Get pending jobs
* `bench purge-jobs` - Destroy all pending jobs

### Data Import

* `bench data-import` - Imports Bulk Data from .csv, .xls or .xlsx


	+ `--file` File Name
	+ `--doctype` The DocType
	+ `--type` Insert/Update

<!-- page: framework/framework__user__en__bench__resources__bench-procfile.md -->
---
title: "Bench Procfile\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/bench/resources/bench-procfile"
updated: "2026-02-17"
---

`bench start` uses honcho to manage multiple processes in **developer mode**.

### Processes

The various process that are needed to run frappe are:

1. `bench start` - the web server
2. `redis_cache` for caching (general)
3. `redis_queue` for managing queue for background workers
4. `redis_socketio` as a message broker for real-time updates / updates from background workers
5. `web` for the frappe web server.
6. `socketio` for real-time messaging.
7. `schedule` to trigger periodic tasks
8. `worker_*` redis workers to handle async jobs

Optionally if you are developing for frappe you can add:

`bench watch` to automatically build the desk javascript app.

### Sample

```
 redis_cache: redis-server config/rediscache.conf
 redis_socketio: redis-server config/redissocketio.conf
 redis_queue: redis-server config/redisqueue.conf
 web: bench serve --port 8000
 socketio: /usr/bin/node apps/frappe/socketio.js
 watch: bench watch
 schedule: bench schedule
 worker_short: bench worker --queue short
 worker_long: bench worker --queue long
 worker_default: bench worker --queue default
```

<!-- page: framework/framework__user__en__blog-post.md -->
---
title: "Blog Post\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/blog-post"
updated: "2026-02-17"
---


**A Blog Post is an article on your website.**

Blogs are a great way to share your thoughts about your business.
It helps keep your customers and readers updated on news related to your business.

In the age of the internet, writing assumes a lot of significance because when
people come to your website, they want to read about you and your product.

To access the Blog Post, go to:
> Home > Website > Blog > Blog Post

## 1. How to create a Blog Post

1. Go to the Blog Post list and click on New.
1. Enter the Title, Blog Category, Blogger, and the Content.
1. Enable Published and click on Save.

The Blog Intro is a short description of your blog that appears just after the
title and before the content.

[Screenshot on the live page: New Blog Post]

You can write your blog in Rich Text, Markdown, or HTML. If you want to write
simple content pages, Rich Text and Markdown are great options.

> Learn markdown in a few minutes at [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

[Screenshot on the live page: Blog Post in Markdown]
*Blog Post in Markdown*

View your Blog Post by clicking on **See on Website** in the sidebar.
[Screenshot on the live page: Blog Post]
*Blog Post*

Readers can comment on the blog post. The guest user will have to enter their **Name** and **Email** to comment.

[Screenshot on the live page: Blog Post]
[Screenshot on the live page: Blog Post]

Check the **Disable Comments** option if you'd like to disable the ability for readers to add comments to the current blog post.
[Screenshot on the live page: Blog Post]

[Screenshot on the live page: Blog Post]
*Adding Comments Disabled*

Readers can give likes on their favorite blog posts.
[Screenshot on the live page: Blog Post]
[Screenshot on the live page: Blog Post]
*Like*

Check the **Disable Likes** option if you'd like to disable the ability for readers to give like to the current blog post.
[Screenshot on the live page: Blog Post]
[Screenshot on the live page: Blog Post]

When a reader comments on a blog post or gives a like, an email is sent to the blogger with a link to the comment/like on the blog post.
If the blogger doesn't want to receive any email he/can uncheck the **Enable Email Notification** checkbox.
[Screenshot on the live page: Blog Post]

## 2. Features

### 2.1 Blogger

Blogger is a user who can post blogs. To create a Blogger, go to:
> Home > Website > Blog > Blogger

You can mention a short bio about the blogger and also set an avatar here.

[Screenshot on the live page: Blogger]
*Blogger*

The preview will be shown at the end of the blog post.
[Screenshot on the live page: Blogger Preview]
*Blogger Preview*

### 2.2 Blog Category

You can group your blogs into categories. To create a new Blog Category, go to:

**Home > Website > Blog > Blog Category**.

[Screenshot on the live page: Blog Category]
*Blog Category*

If you click on **See on Website** in the sidebar, you'll be redirected to a
list of blogs under that category.

[Screenshot on the live page: Blog Category - General]
*Blog Category - General*

### 2.3 Meta Tags

Meta tags are HTML tags which describe a page and its content to a search engine or a social media platform. A meta description provides a brief description of a webpage.

In HTML, the meta description tag will be written as follows:

```html

 

```

Under the SEO section, you can add the meta description and image for your blog post. ERPNext will generate a preview of the blog when listed as a search result by Google.

If you leave this section empty, the blog introduction or the first 140 characters of the blog will be shown as the meta description. In the same way, if you leave the meta image empty, the first image in the blog will be selected.

[Screenshot on the live page: Google Search Preview]
*Blog Post Google Search Preview*

On submitting the blog, you can also preview how the blog will look when shared on a social media platform like Facebook or Twitter. To check this, use the debugging tools offered by the platforms:

- Facebook: [Sharing Debugger](https://developers.facebook.com/tools/debug/)

- Twitter: [Card Validator](https://cards-dev.twitter.com/validator)

- LinkedIn: [Post Inspector](https://www.linkedin.com/post-inspector/inspect/)

To check the post preview, simply enter the webpage/blog link in the tool:

[Screenshot on the live page: Facebook Sharing Debugger]
*Using Facebook's Sharing Debugger Tool*

Using these tools, you can optimize your blog post for sharing.
