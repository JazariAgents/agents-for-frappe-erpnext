---
title: "Request Timed Out"
space: "Cloud"
url: "https://docs.frappe.io/cloud/private-benches/common-issues/request-timed-out"
updated: "2026-08-24"
---

# Request Timed Out

*(screenshot — not bundled; see the live page URL in this file's front matter)*

One action took longer than the HTTP timeout of the bench. The default timeout is 120 seconds. The proxy stopped the request and returned 504. The dialog has the title **Message** and the text **Request Timed Out**.

The server is not at fault. The code behind that one action is too slow.

If the site shows **Request Timeout: Server was too busy**, read [that page](https://docs.frappe.io/cloud/site/common-issues/request-timeout-server-was-too-busy-to-process-this-request) instead. That error is a database lock.

## Find the cause

1. Read the [slow queries](https://docs.frappe.io/cloud/faq/mariadb-slow-queries-in-your-site) of your site. A slow query is the usual cause.
2. If the queries are fast, the Python code is slow. Do the same action from `bench console` after you [connect with SSH](https://docs.frappe.io/cloud/benches/ssh).
3. Time each step of the action there. The step that takes the most time is the one to correct.

## Correct it

- Make the slow code faster. Add an index, or remove work from the loop.
- Move work that is always slow to a [background job](https://docs.frappe.io/framework/user/en/api/background_jobs). The user then does not wait for it.
- If you cannot change the code now, increase `http_timeout` in the [bench config](https://docs.frappe.io/cloud/benches/bench-config). This hides the error. It does not correct it.