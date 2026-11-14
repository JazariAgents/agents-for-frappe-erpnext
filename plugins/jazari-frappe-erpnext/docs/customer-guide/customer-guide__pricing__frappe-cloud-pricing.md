---
title: "How to choose the right plan? "
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing"
updated: "2026-07-21"
---

This page explains how Frappe Cloud pricing is *structured* and how to reason about choosing a plan, whatever your size. For current prices, the live source of truth is **[frappe.io/cloud/pricing](https://frappe.io/cloud/pricing)** - figures move over time, so we describe the model here and point you there for the numbers.



## The first decision: Site plan or Server plan

Frappe Cloud offers two broad types of plan.



**Site plans** are the simplest way to run Frappe. You don't rent a server or manage infrastructure - you get a ready-to-use site running on **shared infrastructure** that Frappe Cloud manages entirely. Behind the scenes, Frappe runs your site alongside others on shared servers in a controlled, isolated way, handling scheduling, limits, and stability for you. Pricing is **compute-based** (you get a daily CPU-time allowance), starting from around **$5/month**.



**Server plans** give you a full virtual machine. You decide how many sites run on it and how its resources are used, and you pay for the **resources** - CPU, memory, and storage. Server plans make sense when you run multiple sites, when workloads are consistently heavy, or when you need predictable performance. They cost more than site plans but give you far more control, performance predictability, and room to scale, starting from around **$20/month**.



**How to decide.** Ask three questions: *How heavy are my workloads? Do I expect usage spikes? Do I want simplicity or control?* As a rule of thumb:



- **Start with a Site plan** if you have a single entity, few integrations, no major usage spikes, and no DevOps team. You can always upgrade later.
- **Choose a Server plan** if you are a mid-sized or large company, run multiple entities, are a services company serving multiple customers, have high transaction volumes or complex workloads, or if uptime and performance are critical.



How this usually shakes out by size:



- **Smaller businesses** typically start on a **Site plan** - it's self-serve, needs no DevOps team, costs little to begin with, and covers a single entity comfortably. This is very likely your starting point, and that's exactly what it's designed for.
- **Mid-sized and large businesses** typically start on a **Server plan**, for the control, isolation, and predictable performance that heavier or multi-entity workloads need.



Either way, the design lets you begin where you are and grow into the next step - starting on a Site plan and moving to a Server plan later is a well-trodden path, not a mistake to avoid.



## The second decision: cloud provider

Frappe Cloud is a **multi-cloud platform**. As of writing, it supports four providers, each at a different point on the cost–performance spectrum: 



- **Amazon Web Services (AWS)** and **Oracle Cloud Infrastructure (OCI)** - enterprise-grade reliability, compliance, and global scale; the typical choice for larger or regulated businesses.
- **DigitalOcean** - a middle option.
- **Hetzner** - the most cost-efficient; best suited to development, testing, and demo environments, and lighter workloads where mission-critical guarantees aren't required.



For enterprise production workloads where uptime and durability matter, Frappe recommends dedicated **AWS or OCI** instances.



You don't need to know the providers' internals - Frappe Cloud is an abstraction over all of them, so you get the freedom to choose without managing the differences. Frappe's engineers publish a detailed [provider comparison](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas) in the documentation for teams that want the depth. 



## The third decision: server location

The rule is simple: **lower distance → lower latency → higher performance.** Each provider offers multiple global regions (AWS the most), so choose a location close to your end users, or one that satisfies any **data-residency requirements** you must comply with - a point that often matters for enterprise security and regulatory reasons. 



## For Site plans, that's nearly it

If you've chosen a Site plan, your path is: **choose provider → choose region → choose plan.** Site plans range from around **$5 to $200/month**. What changes across the ladder is your **compute-time allowance** plus a few features that switch on as you go up:



- Lower tiers include automatic app upgrades, automatic backups, and custom apps/scripts (via private benches).
- **Offsite backups** (more durable than standard backups) begin at the mid tiers.
- **Product Warranty** and **database access** begin at the higher tiers.



Remember that the "compute time" a plan quotes - e.g. "30 minutes of compute per day" - is **CPU time, not login or business time.** See [pricing philosophy](https://docs.frappe.io/customer-guide/pricing/pricing-philosophy).



## For Server plans, two more architecture choices

Server plans involve two additional decisions, both about how the server is configured.



**Unified server vs separate servers** - do the application and database run on one server, or on separate ones?



- *Unified* is simpler and more cost-effective; good for smaller or medium workloads.
- *Separate* gives better isolation and headroom for heavier workloads. **Separate servers are the recommendation for enterprises.**



**Dedicated instance vs shared instance** - are the underlying resources reserved for you, or shared at the provider level?



- *Shared* costs less but comes with some performance variability - recommended only for **dev, test, and demo** environments.
- *Dedicated* gives predictable performance, provider guarantees, and full isolation. **Production workloads should almost always be on dedicated servers.**



After the architecture, you choose the plan itself. Here features are largely the same across plans - what varies is the **server specification** underneath. The guidance from Frappe is sensible: start conservatively and upgrade when needed.



## Enterprise Hosting and enterprise services

For very large enterprises running mission-critical workloads, Frappe offers **Enterprise Hosting** plans with additional **enterprise services**: 

- **Priority SLAs**
- **Technical consulting**
- **A dedicated account manager**



If uptime, guarantees, and direct support relationships are essential to your operation, this is the tier to look at.



## A summary of the decision path


|                 | Site plan                                        | Server plan                                                     |
| --------------- | ------------------------------------------------ | --------------------------------------------------------------- |
| **Best for**    | Simplicity, single site, quick start             | Control, scalability, predictable performance                   |
| **You pay for** | Compute time (CPU usage)                         | Reserved resources (CPU, memory, storage)                       |
| **Steps**       | Provider → Region → Apps → Subdomain → Plan      | Provider → Region → Unified/Separate → Dedicated/Shared → Plan  |
| **Typical fit** | Smaller businesses / single entity / quick start | Mid-sized & large businesses / multi-entity / heavier workloads |


A closing note from Frappe worth keeping in mind: *choosing the right plan is more art than science.* Start exploring, choose conservatively, and upgrade as your needs become clear - the model is built so that growing never means redesigning everything.



> **Note:** Not all variants, plans, providers, and regions are available in every combination. The live pricing page reflects current availability.



---