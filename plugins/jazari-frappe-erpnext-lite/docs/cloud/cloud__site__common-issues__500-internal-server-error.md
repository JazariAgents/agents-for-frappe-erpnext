---
title: "500 Internal Server Error"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/common-issues/500-internal-server-error"
updated: "2026-02-16"
---

This usually indicates an application related issue. If your site is on custom [bench group](https://docs.frappe.io/cloud/benches), then you can investigate the same with:

#### Checking bench logs (Option 1)

1. Go to your site's **Bench Group** dashboard and check **Sites** tab

![](/files/image84f365.png)

1. Click on **View Logs**

![](/files/image471f35.png)

1. Open **web.error.log** and scroll to bottom. You should be able to see the traceback:

![](/files/image89f8fe.png)
*In this example, the site can't connect to the database server. Restarting the database server might a solution here.*

#### Using SSH Access (Option 2)

Alternatively, you can locate **web.error.log** after SSH Access. Please check the docs [here](https://docs.frappe.io/cloud/benches/debugging)

If you occasionally get a pop-up with the **Internal Server Error** message, it is likely that a background job is failing. In such cases, checking your **Scheduled Job Log, Error Log** and **worker.err.log** file should help.