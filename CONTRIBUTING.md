# Contributing

Thank you for helping. The most useful contribution is a report that a step is wrong on a real site.

## Report a wrong step or a bug

[Open an issue](../../issues/new/choose) and include:

- your Frappe and ERPNext versions (the plugin prints them when you connect),
- the plugin version (`/plugin` shows it),
- how you are connected: Frappe's MCP server, `frappectl`, an API key, or the browser,
- what you asked, and what happened instead.

Remove customer names, keys and anything private before you paste.

Security problems do not go in a public issue. See [SECURITY.md](SECURITY.md).

## Change something

1. Fork the repository and make a branch.
2. The plugin lives in `plugins/jazari-frappe-erpnext/`. Each skill is a folder under `skills/` with a
   `SKILL.md` and its guides in `references/`.
3. Check your change:

   ```
   claude plugin validate .
   claude plugin validate plugins/jazari-frappe-erpnext
   ```

4. Try it in a session without installing it:

   ```
   claude --plugin-dir plugins/jazari-frappe-erpnext
   ```

5. Open a pull request that says what you changed, which Frappe version you tried it on, and what you
   could not test.

## Ground rules for changes

- **Say only what was checked.** A step either was run on a live site, or the text says it comes from the
  documentation. Do not write "tested" for something that was not run.
- **The safety rules have one home.** What counts as a change to an existing record is decided in
  `skills/frappe-connect/scripts/frappe_safety.py`, which the MCP guard and the API helper both use. Change
  it there, and add a case for it: a rule that allows more must show why that is safe.
- **Never weaken a refusal to make a task easier.** If a rule blocks a legitimate task, open an issue first.
- **Plain words.** The guides are read by people who are new to ERPNext, in English and Arabic.

## The bundled documentation

The pages in `plugins/jazari-frappe-erpnext/docs/` are Frappe's, under CC BY-SA. Do not edit them by hand;
they are copies. See [NOTICE.md](NOTICE.md).

## Licence

By contributing you agree that your contribution is released under the [MIT licence](LICENSE).
