# bench adapter — Undo and restore

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
| Back up a site | `bench --site {site} backup` | no | `docs/framework/framework-03.md` lines 2396–2493 |
| Restore a site from a backup | `bench --site {site} restore {path}` | YES — irreversible: replaces the whole database, take a fresh backup first | `docs/framework/framework-03.md` lines 3195–3290 |
| Restore selected tables only | `bench --site {site} partial-restore /full/path/to/<name>-partial-database.sql.gz` — needs a **partial** backup made with `bench --site {site} backup --only "DocType A,DocType B"` (a full backup is refused: *Full backup file detected*), and the backup's full path (a path relative to the bench folder is refused as *Invalid path*). Tested on Frappe 16.56: only the backed-up tables went back; everything else was kept. | YES — irreversible: overwrites the selected tables, take a fresh backup first | `docs/framework/framework-03.md` lines 3096–3137 |

## The three that end sites

- `bench drop-site` archives the site and drops its database. A full backup is taken first unless
  `--no-backup` is passed — never pass it.
- `bench restore` replaces the whole database. Everything created after that backup is gone.
  Downgrades are refused by Frappe.
- `bench reinstall` wipes the site and installs it fresh. There is no partial version of this.

Always run `bench --site {site} backup` first and tell the user where the file landed.

