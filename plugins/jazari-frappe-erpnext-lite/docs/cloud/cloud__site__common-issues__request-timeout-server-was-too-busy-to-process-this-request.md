---
title: "Request Timeout: Server was too busy to process this request"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/request-timeout-server-was-too-busy-to-process-this-request"
updated: "2026-08-24"
---

# Request Timeout: Server was too busy to process this request

*(screenshot — not bundled; see the live page URL in this file's front matter)*

The server was not busy. A query waited for a row lock, and MariaDB stopped it after 50 seconds with error 1205, `Lock wait timeout exceeded`. Another transaction held that lock. This is a bug in the application, not a limit of the plan.

## Find the cause

1. Do the action a second time. While it runs, open the [process list](https://docs.frappe.io/cloud/site-process-list) of your site. The list shows the query that waits and the query that blocks it.
2. If the process list is empty, read the [slow queries](https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site) of your site.
3. Search the Error Log for `QueryTimeoutError`. The traceback names the code that failed.

A new [controller hook](https://docs.frappe.io/framework/user/en/basics/doctypes/controllers#controller-hooks) or [scheduled job](https://docs.frappe.io/framework/user/en/api/background_jobs) is the usual cause.

## Correct it

- Keep transactions short. Do the slow work first, then write to the database.
- Update rows in batches. Commit after each batch.
- If two jobs write to the same document, run them one after the other.