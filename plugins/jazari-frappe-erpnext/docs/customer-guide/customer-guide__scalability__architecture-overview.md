---
title: "What's the architecture?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/architecture-overview"
updated: "2026-07-02"
---

This page explains, at a level useful to a CTO or IT lead evaluating Frappe, how the software is structured - both on a single machine and across a production cloud cluster. You do not need this detail to *use* Frappe, but you do need it to assess deployment, scaling, and operational risk, and to follow the vocabulary used throughout the rest of this guide. 



## The foundation: a full-stack framework

Everything Frappe builds sits on the **Frappe Framework**, a full-stack web framework written in Python and JavaScript. "Full-stack" here is meaningful: the framework includes, out of the box, everything needed to run a site in production - a database layer, caching, background jobs, real-time notifications, user authentication, and a REST API. You are not assembling these from separate components; they are configured when a Frappe site is set up.



The modern user interfaces are built with **Frappe UI**, a Vue-based component library for single-page applications on top of the framework.



## The core concepts: apps, sites, and benches

Three terms describe how a Frappe deployment is organised. Understanding the relationship between them is the single most useful thing in this page.



**Apps** are the installable software - the code. `frappe` (the framework itself), `erpnext`, and any custom application you build are all apps. Apps are installed into a bench and can be shared across multiple sites.



**Sites** are isolated tenants. Each site (for example `site1.local` or `mysite.com`) has its **own database**. This is how one deployment can host multiple, fully separated environments - different companies, or different entities within a group - without their data mixing.



**A bench** (`frappe-bench`) is the deployment unit that ties it together. A bench contains a `sites/` directory and an `apps/` directory, plus an isolated Python virtual environment. Because each bench is self-contained, a single host can run multiple benches - which is what lets you run, say, different Frappe versions side by side for different sites.



Putting it together: **apps are installed into a bench, and a bench hosts one or more sites, each with its own isolated database.**



`[PLACEHOLDER: embed the Framework architecture diagram — Sites (site1.local, mysite.com) over Apps (frappe, erpnext, custom_app) over the runtime layer (Node, Werkzeug, Redis, Background Jobs) over Python Virtual Environment, alongside the MariaDB/Postgres database. Source: Frappe Framework docs "Architecture" page.]`



Underneath the apps, each bench runs the supporting processes the framework needs - the web server, Redis (for caching and queues), Node, and background job workers - against a database, typically **MariaDB** (PostgreSQL is also supported). Each bench spawns its own web, Redis, and Node processes, which is what keeps benches isolated from one another.



## At production scale: the Frappe Cloud cluster

A single bench on a single machine is the right picture for understanding the concepts, but it is not how a production system runs at scale. In production on **Frappe Cloud**, the same building blocks are distributed across a cluster of servers for performance, isolation, and redundancy.



A typical Frappe Cloud cluster separates responsibilities across server roles:



- **Proxy server** - runs Nginx and routes incoming traffic to the right place.
- **Application servers** - each runs Frappe and handles the application workload. A cluster has several, so load is distributed.
- **Database servers** - each runs MariaDB. Application servers communicate with their paired database servers.



`[PLACEHOLDER: embed the Frappe Cloud cluster diagram — Proxy Server (Nginx) routing to multiple Application Servers (Frappe), each paired with a Database Server (MariaDB), every node running an Agent. Source: Frappe Cloud docs "Architecture" page.]`



Two further components make this cluster manageable and reproducible:



- **Agent** - a small Flask application that runs on the servers and gives Frappe Cloud's control plane (called **Press**) a way to issue commands to the sites and benches - creating sites, running upgrades, taking backups, and so on, programmatically and reliably.
- **Docker and Ansible** - the cluster is built on Docker (to package and run the software in consistent, portable containers) and Ansible (to automate provisioning and configuration). This is what allows Frappe Cloud to stand up, configure, and maintain servers consistently at scale.



A more complete production picture adds redundancy for each server role and the networking that ties the cluster together. Frappe also publishes a short video walkthrough of the Frappe Cloud architecture, which can be embedded for readers who want the visual explanation: [How does Frappe Cloud work?](https://youtu.be/KIohic6ML5o?si=CZeqrzXhXIFhiS88)



## Why this matters for your evaluation

This architecture has direct consequences worth noting. **Site-level isolation** (each site has its own database) is the basis for cleanly separating entities, environments, or business units. The **separation of proxy, application, and database roles** is what lets the system scale horizontally. And the **Agent / Press / Docker / Ansible** layer is why a managed Frappe Cloud deployment can be operated, upgraded, and recovered reliably without your team doing it by hand - which is the operational burden discussed in [Frappe's business model](https://docs.frappe.io/customer-guide/about-frappe/business-model).



If you self-host instead, these same components are yours to assemble and operate; the architecture is identical, but the operational responsibility shifts to your team. The trade-off between Frappe Cloud and self-hosting is covered [here](https://docs.frappe.io/customer-guide/getting-started/self-hosted-vs-frappe-cloud).