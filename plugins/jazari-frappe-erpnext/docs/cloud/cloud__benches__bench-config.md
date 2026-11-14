---
title: "Bench Config"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/bench-config"
updated: "2026-02-27"
---

You may set site config variables on a bench so that it [applies for all the sites](https://frappeframework.com/docs/user/en/basics/sites#common-site-config-json) deployed under it.

![](/files/DGXrOWZ.png)



### Special case: http timeout

You may also set **httptimeout** in seconds (default: 120) as a special case to specify time gunicorn workers wait for request to process before throwing 504 request error. This will affect the custom api endpoints you define.

![](/files/nAlWmZH.png)

