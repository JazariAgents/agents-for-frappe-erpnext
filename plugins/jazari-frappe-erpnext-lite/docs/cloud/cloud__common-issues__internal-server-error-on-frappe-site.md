---
title: "Internal Server Error On Frappe Site"
space: "Cloud"
url: "https://docs.frappe.io/cloud/common-issues/internal-server-error-on-frappe-site"
updated: "2026-02-16"
---

More often than not, this error represents some application related issue. If your site is on custom bench group, then you can investigate the same with [logs](https://frappecloud.com/docs/logs) or [ssh access](https://frappecloud.com/docs/benches/ssh). It is a possibility that your custom app is throwing an error. You can view the same in **web.error.log**. Refer our [docs](https://frappecloud.com/docs/benches/debugging) for the same.

If you occassionally get a pop-up with the same message, it is likely that a background job is failing. In such cases, checking your **Scheduled Job Log, Error Log** and **worker.err.log** file should help.