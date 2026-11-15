---
title: "Monitoring"
space: "Cloud"
url: "https://docs.frappe.io/cloud/sites/monitoring"
updated: "2026-08-25"
---

Frappe Cloud collects metrics while your site runs: request counts, request duration, background jobs, CPU time, and uptime. You read them on the **Analytics** tab of your site.

## Site Analytics

To open the charts, go to your site in the dashboard and click the **Analytics** tab.

The tab opens with six charts:

| Chart | What it shows |
| --- | --- |
| **Daily Usage** | Cumulative CPU time of the requests today. The line marks your daily CPU limit. Watch this chart to know when to upgrade the plan. |
| **Uptime** | Uptime of the web worker and the scheduler. The monitor server probes the site every minute. |
| **Requests** | Number of requests per minute. |
| **Requests CPU Usage** | CPU time that the requests used. |
| **Background Jobs** | Number of background jobs. |
| **Background Jobs CPU Usage** | CPU time that the background jobs used. |

![](/files/image3c0c87.png)

Two controls at the top of the tab change what all charts show:

- **Absolute from ... to ...** sets a start date and an end date.
- **Relative** sets a period that ends now, for example the last 24 hours.

You can also drag across a chart to zoom into a shorter period.

Note: Analytics start only after you complete the Setup Wizard on the site.

## Investigating high usage

The charts that name your slow endpoints are under **Advanced Analytics**. This section is closed by default.

1. Open the **Analytics** tab.
2. Scroll below the first charts, to the heading **Advanced Analytics**.
3. Click the heading. The section opens and loads the charts.

The section holds these charts:

- **Frequent Requests** and **Slowest Requests**, by path.
- **Frequent Background Jobs** and **Slowest Background Jobs**, by method.
- **Requests by IP**.
- **Frequent Slow Queries** and **Top Slow Queries**.
- Duration charts for the paths that are slow most often. They appear only when that path is slow on your site. One chart names the reports, one names the document methods, and two name the doctypes and the actions of the saved documents.

![](https://cloud.frappe.io/files/gszsZA1.png)

The list is sorted, so the first entry is the slowest. The long red bars are the paths to examine.

![](https://cloud.frappe.io/files/xKtypi1.png)

To read these charts and to act on them, see [Site Slow: 504 Gateway timeout](/cloud/site/common-issues/site-slow-504-gateway-timeout).

## Database Storage Usage

Frappe Cloud syncs the database usage of your site every 6 hours.

### How to refresh the database usage on demand

If you changed data and want the current number, start a refresh yourself. You can do this from the **Site Overview** page or from the **DB Analyzer**.

The refresh also purges the Information Schema cache. After the refresh, the usage from Frappe Cloud and from the DB Storage Report of the framework agree.

Note: You can refresh once every 15 minutes.

![](/files/imagecdfe78.png)

![](/files/image4e6986.png)

### Why Frappe Cloud and the storage reports disagree

The number from Frappe Cloud can differ from the DB Storage Report of the framework, and from the DB Analyzer.

Frappe Cloud reads the table sizes with its own parser. The parser does not use cached data, and it does not slow the database down.

The DB Storage Report and the DB Analyzer read the Information Schema tables of MariaDB. MariaDB caches that data and refreshes it only in some conditions. The reports can therefore show old numbers.

To make the numbers agree, refresh the database usage from the **Site Overview** page or from the **DB Analyzer**.

## Monitoring Disabled

A monitoring server tests every minute if your site is online. It sends a request to the primary domain of the site:

```
https://example.com/api/method/ping
```

The site must answer with an HTTP 200 status code and this body:

```json
{"message": "pong"}
```

### Why monitoring becomes disabled

Frappe Cloud turns monitoring off when the ping does not arrive, and sends you a mail. These are the common causes:

- The primary domain expired.
- The DNS records are incorrect.
- Cloudflare, or another CDN in front of the site, blocks the request.
- A custom app makes the ping endpoint fail.

### How to enable monitoring again

1. Open the **Site Overview** page of your site.
2. Click **Enable Monitoring** at the top of the page. The dialog shows why monitoring stopped.
   ![shapes at 25 10 08 15.06.33](/files/shapes%20at%2025-10-08%2015.06.33.png)
   ![Screenshot 2025 10 08 at 15 07 33 Frappe Cloud](/files/Screenshot%202025-10-08%20at%2015-07-33%20Frappe%20Cloud.png)
3. Click **Check & Enable Monitoring**.
   ![Screenshot 2025 10 08 at 15 12 42 Frappe Cloud](/files/Screenshot%202025-10-08%20at%2015-12-42%20Frappe%20Cloud.png)

If the test fails, the dialog shows the cause and the correction.
