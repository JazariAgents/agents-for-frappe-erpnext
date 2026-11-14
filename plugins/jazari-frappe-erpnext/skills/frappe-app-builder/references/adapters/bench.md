# bench adapter — Build a Frappe app from scratch

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
| Create a new Frappe app | `bench new-app {app}` | no | `docs/framework/framework__user__en__tutorial__create-an-app.md` |
| Create a new site for an app | `bench new-site {site} --install-app {app}` | no | `docs/framework/framework__user__en__tutorial__create-a-site.md` |
| Bundle app assets | `bench build --app {app}` | no | `docs/framework/framework__user__en__basics__asset-bundling.md` |

## The three that end sites

- `bench drop-site` archives the site and drops its database. A full backup is taken first unless
  `--no-backup` is passed — never pass it.
- `bench restore` replaces the whole database. Everything created after that backup is gone.
  Downgrades are refused by Frappe.
- `bench reinstall` wipes the site and installs it fresh. There is no partial version of this.

Always run `bench --site {site} backup` first and tell the user where the file landed.

