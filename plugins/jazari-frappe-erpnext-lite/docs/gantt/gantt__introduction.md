---
title: "Introduction"
space: "Gantt"
url: "https://docs.frappe.io/gantt/introduction"
updated: "2026-01-06"
---

## What is Frappe Gantt?
Gantt charts are bar charts that visually illustrate a project's tasks, schedule, and dependencies. With Frappe Gantt, you can build beautiful, customizable, Gantt charts with ease.

You can use it anywhere from hobby projects to tracking the goals of your team at the worksplace.

[ERPNext](https://erpnext.com/) uses Frappe Gantt.

![](https://github.com/frappe/gantt/raw/master/.github/hero-image.png)


## Why Frappe Gantt?
We needed a Gantt View for ERPNext. Surprisingly, we couldn't find a visually appealing Gantt library that was open source - so we decided to build it. Initially, the design was heavily inspired by Google Gantt and DHTMLX.


## Key Features
- **Customizable Views**: customize the timeline based on various time periods - day, hour, or year, you have it. You can also create your own views.
- **Ignore Periods**: exclude weekends and other holidays from your tasks' progress calculation.
- **Configure Anything**: spacing, edit access, labels, you can control it all. Change both the style and functionality to meet your needs.
- **Multi-lingual Support**: suitable for companies with an international base.

## Installation

Install with:
```bash
npm install frappe-gantt
```

Include it in your HTML:

```html
<script src="frappe-gantt.umd.js"></script>
<link rel="stylesheet" href="frappe-gantt.css">
```

Or from the CDN:
```html
<script src="https://cdn.jsdelivr.net/npm/frappe-gantt/dist/frappe-gantt.umd.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/frappe-gantt/dist/frappe-gantt.css">
```

Start using Gantt:
```js
let tasks = [
  {
    id: '1',
    name: 'Redesign website',
    start: '2016-12-28',
    end: '2016-12-31',
    progress: 20
  },
  ...
]
let gantt = new Gantt("#gantt", tasks);
```

## Discuss
If you want help, or have ideas to improve Gantt, please head over to the [Frappe Forum](https://discuss.frappe.io/search?q=gantt). Alternatively, open an [issue](https://github.com/frappe/gantt/issues/new) on GitHub.
