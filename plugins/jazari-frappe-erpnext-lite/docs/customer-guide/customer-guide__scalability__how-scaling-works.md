---
title: "How does scaling work?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/how-scaling-works"
updated: "2026-07-02"
---

To evaluate scalability with confidence - or to brief your technical team - it helps to understand how a Frappe application is built, because the architecture is what makes it scalable. You don't need to be an engineer to follow this; the core idea is simple.



## The request–response model

At its heart, every Frappe application works the same way as most web applications: a **client** (a user's browser) sends a **request** to a **server**, which does some work and sends a **response** back. When you open a document, your browser asks the server for it; the server assembles it and returns it.



What looks like one action is, behind the scenes, many smaller requests. Opening or saving a single document can translate into dozens of smaller operations against the database - fetching linked records, validating, writing, recording the change. This matters for one reason: **when something is slow, it's rarely that "everything" is slow - it's that one of those many small operations has become a bottleneck.** Scaling is the discipline of finding and relieving those bottlenecks.



## The components

A Frappe deployment is made of several components, each of which can be scaled independently. From the architecture (covered also in [Architecture overview](https://docs.frappe.io/customer-guide/scalability/architecture-overview)):



- **Application server** - runs the Frappe Framework (Python). This is where business logic executes. It runs multiple **workers**, each handling one request at a time; more workers means more simultaneous work.
- **Database server** - MariaDB, the system's source of truth. Every request ultimately reads from or writes to it. *This is the most common bottleneck at scale.*
- **Redis** - handles caching and the queue for background jobs.
- **Background job workers** - process heavy or scheduled work (reports, bulk operations, payroll runs) away from the user-facing path.
- **NGINX** - the web proxy that routes incoming traffic.
- **File storage** - for documents and attachments.



Because these are separate components, they can sit on one machine for a small deployment, or be spread across many machines for a large one - and you can scale the specific component that's under pressure rather than over-provisioning everything.



> **For technical evaluators:** ERPNext is a standard three-tier application - MariaDB database, a Python application server, and a JavaScript front end, all on the Frappe Framework. Each tier scales with established, well-understood techniques rather than anything proprietary, which means your DBAs and infrastructure team already know most of what's needed. The deployment unit is the **bench** (multi-tenant; each site has its own database), and benches can be replicated across machines connected to the same database and file system.



## Why the database is usually the bottleneck

Frappe applications are data-intensive, so as data grows, the database is where strain shows first. The intuition: a database needs **indexes** to find data quickly, the way a book needs an index. When your data is small, everything is fast even without good indexing - you can read a 50-page pamphlet front to back. When your data grows to the size of an encyclopedia, the same approach crawls.



This is why scaling problems often appear *months* into a deployment rather than on day one: the data simply hadn't grown enough to expose them yet. The good news is that database bottlenecks are the best-understood category of scaling problem, with the most reliable fixes - covered next.



> **For technical evaluators:** the single most reliable rule of thumb is the **working set** - roughly, your most-recently-used data (often the last year) should fit in the database server's RAM, because RAM is orders of magnitude faster than disk. If your last year's growth approaches your server's RAM, it's time to upgrade the database. Most database performance questions can be answered by looking at this relationship plus the slow-query logs.



---