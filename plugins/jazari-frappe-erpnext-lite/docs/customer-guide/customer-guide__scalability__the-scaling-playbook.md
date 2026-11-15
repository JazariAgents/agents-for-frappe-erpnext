---
title: "What are the scaling mechanisms?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/the-scaling-playbook"
updated: "2026-07-02"
---

When a Frappe application needs to handle more, there is a clear, layered sequence of responses - moving from the simplest and fastest to the most specialised. Most businesses never go past the first one or two layers. This page walks through all of them, so you can see that there's a known path at every level of demand.



## Layer 1: It works by default

For the large majority of workloads, the default configuration is enough. Frappe applications are designed to be scalable out of the box, and a well-provisioned standard setup comfortably handles the needs of most businesses - including many that consider themselves "large." The first thing worth knowing is that you likely won't need the rest of this page.



## Layer 2: Scale up the resources (elastic compute)

When you do need more capacity, the simplest answer is more resources - and on Frappe Cloud this takes minutes, not a project.



- **Upgrade in minutes.** Move to a larger plan and the system reconfigures automatically - more workers, higher memory limits - without you touching any configuration. On self-managed infrastructure the same upgrade means manual reconfiguration and a restart.
- **Stay ahead of limits.** Frappe Cloud sends alerts at 80% resource consumption, giving you time to upgrade before users feel it. You can also downgrade if you're over-provisioned.
- **It's immediate relief.** Scaling up reliably buys headroom: a growing business gets the certainty that it can keep working while any deeper optimisation is planned, rather than hitting a wall.



This is the right first move whenever resources are genuinely the constraint. Its honest limit: beyond a point, adding resources stops helping, because the bottleneck is no longer raw capacity but something specific that needs fixing (Layer 4).



> **For technical evaluators:** on dedicated infrastructure you get guaranteed resources, which is why it's recommended for serious production workloads - performance is predictable rather than shared. Worker count scales roughly with available RAM, so upgrading a server adds parallel capacity automatically.



## Layer 3: Autoscaling and horizontal scaling

Scaling up makes one server bigger. **Horizontal scaling** adds a second server to share the load during peaks - and Frappe Cloud now does this automatically.



When load rises, a **secondary application server** is brought up alongside your primary one: it syncs the same benches, takes a share of incoming traffic (an identically-sized secondary handles 50% of requests), and keeps the system responsive - with **zero downtime**. When the peak passes, traffic returns to the primary, the secondary shuts down gracefully (finishing queued jobs first), and you stop paying for it.



You control it three ways: **manually**, on **thresholds** (set CPU/memory limits that trigger a scale-up automatically, with email notification), or on a **schedule** (pre-arrange capacity for predictable peaks - a month-end close, a sale day). Billing for the secondary is hourly and only while it's active, at a 10% discount on the primary plan price. 



This directly answers a common enterprise worry - predictable or sudden load spikes - without permanently paying for peak-sized infrastructure.



## Layer 4: Find and fix the bottleneck

When more hardware stops helping, the work shifts from provisioning to optimisation - finding the specific component that's slow and addressing it. This is usually the database, and the techniques are well-established:



- **Indexing.** The fastest, most common fix: add the right database indexes so queries that have slowed as data grew become fast again. Identified by analysing slow-query logs.
- **Right-size the database server.** Ensure the working set fits in RAM (see [how scaling works](https://docs.frappe.io/customer-guide/scalability/how-scaling-works)); upgrade the database tier when last year's data growth approaches available memory.
- **Read replicas.** For read-heavy workloads - heavy or constant reporting especially - a replica database holds a copy of the data so that reads and reports run against it, leaving the primary free for transactions. Configured case-by-case for workloads that genuinely need it.
- **Optimise the code path.** Sometimes a specific operation does more work than it needs to. Profiling tools pinpoint exactly where time goes in an operation, so engineers can streamline the hotspot.



> **For technical evaluators:** the platform ships with the tooling to do this - slow-query logs, query analysis (EXPLAIN), a built-in request **recorder** that breaks a single user action into its underlying queries so you can see precisely what's slow, and Python profiling. On Frappe Cloud these are surfaced in analytics dashboards without SSH; self-managed deployments can use the same underlying tools directly. Database-level options extend to MariaDB replication, MaxScale, and Galera; Redis scales via Redis Cluster; the application tier scales by separating web and job workers onto separate machines and separating read/write queries across a replica.



## Layer 5: Architectural options for extreme cases

A small number of workloads - very high transaction volumes, very large multi-year datasets, or unusual data shapes - call for architectural changes. These exist, and they're how the largest deployments run:



- **High-throughput ingestion.** When an external system pushes huge transaction volumes (e.g. e-commerce orders, IoT), a custom API can insert pre-validated records in bulk, and integrations use queuing, retries, and back-pressure so they don't overwhelm the system. Often the better answer is to post *consolidated* summaries rather than every micro-transaction - worth discussing with your accountant what detail you actually need in the ERP.
- **Report scheduling and materialised views.** Heavy reports can be pre-computed on a schedule or run on dedicated reporting capacity, so they don't slow interactive use.
- **Multi-entity federation.** For large multi-company or multi-branch groups, each subsidiary can run its own instance, with only summary-level transactions posted to a central entity - so each entity scales independently and the centre isn't burdened with every micro-transaction.
- **Custom front-ends.** The standard interface handles a wide range of needs, but a team can build a custom front end on Frappe's REST API for specialised high-volume screens.
- **Refactoring.** Because the software is open source, a genuine hotspot can be profiled and the relevant code rewritten - an option proprietary software simply doesn't offer.



> **For technical evaluators:** federation can be synchronised via event streaming; the entire codebase is auditable and extensible through the app/hooks architecture, so optimisations live in your own apps rather than as fragile core edits - which keeps upgrades clean (see [migrations](https://docs.frappe.io/customer-guide/implementation/data-migration)).



These last layers are specialised work, and they're where Frappe's expert help comes in - covered in [the honest limits and when to get help](https://docs.frappe.io/customer-guide/scalability/limits-and-seeking-help).