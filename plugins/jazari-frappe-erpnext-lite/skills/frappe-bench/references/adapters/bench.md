# bench adapter — Run bench — sites, apps, backups, deploys

## Contents

- how to run these
- commands used by this skill
- the three that end sites

bench runs on the server, over SSH or a terminal — not over HTTP. Ask the user to run these, or run them
only where this session genuinely has shell access to that server. On Frappe Cloud there is no bench
directory: use the dashboard equivalents in the frappe-cloud skill.

## Commands used by this skill

| Capability | Command | Destroys? | Bundled page (read this) |
|---|---|---|---|
| Understand bench and the bench directory | `bench version` | no | `docs/framework/framework-03.md` lines 1065–1100 |
| Run bench CLI commands | `bench --help` | no | `docs/framework/framework-03.md` lines 1102–1450 |
| Run site-scoped framework commands | `bench --site {site} --help` | no | `docs/framework/framework-03.md` lines 1512–1918 |
| Create a site with bench new-site | `bench new-site {site}`: give the user this command without `--admin-password` or `--db-root-password`, so bench asks them, and let them run it | no | `docs/framework/framework-03.md` lines 2997–3094 |
| Drop a site | `bench drop-site {site}` | YES — recreate | `docs/framework/framework-03.md` lines 2580–2632 |
| Back up a site | `bench --site {site} backup` | no | `docs/framework/framework-03.md` lines 2396–2493 |
| Restore a site from a backup | `bench --site {site} restore {path}` | YES — irreversible: replaces the whole database, take a fresh backup first | `docs/framework/framework-03.md` lines 3195–3290 |
| Restore selected tables only | `bench --site {site} partial-restore /full/path/to/<name>-partial-database.sql.gz` — needs a **partial** backup made with `bench --site {site} backup --only "DocType A,DocType B"` (a full backup is refused: *Full backup file detected*), and the backup's full path (a path relative to the bench folder is refused as *Invalid path*). Tested on Frappe 16.56: only the backed-up tables went back; everything else was kept. | YES — irreversible: overwrites the selected tables, take a fresh backup first | `docs/framework/framework-03.md` lines 3096–3137 |
| Run migrations after an update | `bench --site {site} migrate` | YES — reversible | `docs/framework/framework-03.md` lines 2937–2995 |
| Reinstall a site from scratch | `bench --site {site} reinstall` | YES — recreate | `docs/framework/framework-03.md` lines 3139–3193 |
| List the apps installed on a site | `bench --site {site} list-apps` | no | `docs/framework/framework-03.md` lines 2879–2935 |
| Uninstall an app from a site | `bench --site {site} uninstall-app {app}` | YES — recreate | `docs/framework/framework-03.md` lines 3574–3628 |
| Read and change site configuration | `bench --site {site} set-config {key} {value}` | YES — reversible | `docs/framework/framework-03.md` lines 3292–3355 |
| Show the current site configuration | `bench --site {site} show-config`: do not run it yourself, because its output holds the database password and the encryption key; ask the user to run it and tell you the one setting they need | no | `docs/framework/framework-03.md` lines 3357–3406 |
| Execute a Python method on a site | `bench --site {site} execute {dotted.path}` | YES — irreversible | `docs/framework/framework-03.md` lines 2634–2877 |
| Trim unused database tables | `bench --site {site} trim-database` | YES — recreate | `docs/framework/framework-03.md` lines 3465–3515 |
| Set up a production environment | `sudo bench setup production {user}` | YES — reversible | `docs/framework/framework-03.md` lines 2292–2352 |
| Run several sites on one bench | `bench config dns_multitenant on` | YES — reversible | `docs/framework/framework-03.md` lines 2223–2290 |
| Configure HTTPS for a site | `sudo bench setup lets-encrypt {site}` | YES — reversible | `docs/framework/framework-03.md` lines 1956–2021 |
| Add a custom domain to a site | `bench setup add-domain {domain} --site {site}` | YES — reversible | `docs/framework/framework-03.md` lines 1920–1954 |
| Understand the bench Procfile | `cat Procfile` | no | `docs/framework/framework-03.md` lines 3865–3905 |
| Check background services | `bench doctor` | no | `docs/framework/framework-03.md` lines 3630–3682 |

## The three that end sites

- `bench drop-site` archives the site and drops its database. A full backup is taken first unless
  `--no-backup` is passed — never pass it.
- `bench restore` replaces the whole database. Everything created after that backup is gone.
  Downgrades are refused by Frappe.
- `bench reinstall` wipes the site and installs it fresh. There is no partial version of this.

Always run `bench --site {site} backup` first and tell the user where the file landed.

