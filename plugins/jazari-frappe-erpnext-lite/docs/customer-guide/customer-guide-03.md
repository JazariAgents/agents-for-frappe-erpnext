<!-- Frappe documentation: customer-guide, part 3 of 6. Index: docs/INDEX.md -->

<!-- page: customer-guide/customer-guide__pricing__frappe-cloud-pricing.md -->
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

<!-- page: customer-guide/customer-guide__pricing__pricing-faq.md -->
---
title: "FAQs on Pricing"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/pricing/pricing-faq"
updated: "2026-07-21"
---

The questions customers most often ask about Frappe's pricing, answered plainly.



**Is Frappe Cloud more expensive than self-hosting?** 

Not always. Raw infrastructure can look cheaper when self-hosted, but Frappe Cloud often reduces hidden costs - DevOps effort, downtime risk, failed upgrades, and long-term maintenance. For most businesses, the staff time and operational risk of self-hosting outweigh the infrastructure saving. See [Total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco) for the full comparison.



**How do I decide between Site plans and Server plans?** 

Site plans are shared, compute-based plans for simple setups and quick starts. Server plans give you a full virtual machine with dedicated or shared resources, suited to larger, more flexible deployments. Smaller businesses usually start on Site plans; mid-sized and large businesses usually start on - or move to - Server plans. See [how to choose](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing).



**Can I start with a Site plan and move to a Server plan later?** 

Yes. Many teams start with a Site plan to try things out and move to a Server plan as requirements grow. The migration effort depends on your setup and usage. The pricing model is deliberately built so that growing does not mean redesigning everything.



**What is Product Warranty?** 

Product Warranty is support from Frappe's engineers for fixing **bugs** in Frappe apps (ERPNext, Frappe HR, Frappe Framework, etc.) and in Frappe Cloud itself. You raise tickets from the support portal and engineers respond within a stipulated response time. Note that this covers bug-fixing, **not functional support** - functional and implementation support comes from your partner. See [how Frappe works as a company](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company).



**Is Hetzner suitable for production?** 

Hetzner is best for development, testing, and demo environments, and can handle production workloads that are **not** mission-critical. For workloads where uptime and durability are critical, Frappe recommends dedicated **AWS or OCI** instances. Choosing Hetzner means prioritising affordability over consistent performance.



**Do I need deep technical knowledge to use Frappe Cloud?** 

No. Frappe Cloud is self-serve and accessible, while still offering advanced options for teams that want more control. The platform abstracts away the underlying cloud providers' complexity.



**How do payments work?** 

Two modes: 

- **Pay by card** - the monthly invoice is charged to your card at the end of the month.
- **Prepaid credit** - you top up a credit wallet (card, PayPal, or region-specific methods), and invoices are deducted from the balance monthly. Keep sufficient credit to avoid service interruption.



**What about the costs beyond hosting?** 

Hosting is one line in your total cost. Implementation, data migration, customisation, training, and ongoing support are real costs with any business system, including Frappe - though they scale down with your size. The licence-fee line is zero, and upgrade and integration costs are structurally lower, but budget for all components honestly - [Total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco) shows the full picture.

<!-- page: customer-guide/customer-guide__pricing__pricing-philosophy.md -->
---
title: "How does pricing work?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/pricing/pricing-philosophy"
updated: "2026-07-21"
---

Before any numbers, it is worth understanding *how* Frappe is priced, because the model is fundamentally different from most business software - and the difference works in a growing business's favour.



## Two costs, kept separate

With Frappe, it helps to separate two things that proprietary vendors usually bundle into one licence fee:



- **The software itself costs nothing.** Frappe's products are open source. There is no per-seat licence fee, no feature paywall, no charge for the software.
- **You pay to *run* the software well.** Hosting, infrastructure, backups, monitoring, upgrades, security, and support are the real, ongoing costs of running the software - and they are what Frappe Cloud charges for.



This is the single most important reframing for anyone used to conventional software contracts: you are not buying a licence, you are paying for the operation of a system you already own. [What open source means for you](https://docs.frappe.io/customer-guide/about-frappe/what-open-source-mean-for-you) explains the ownership side; this section covers the cost side.



## Compute-based pricing, not per-user pricing

Most business SaaS - ERP, CRM, and the rest - is priced **per user**. Every person who might need access is another seat on the bill, regardless of how much they actually use the system.



This model has a structural flaw at any size. It assumes every user is equal and needs access all the time. In reality, ten people reading data lightly may place less load on a system than two people running heavy reports all day - yet per-user pricing charges you for headcount, not for use. Worse, it means your software cost rises **linearly with your team size**: every new hire increases the bill, which is effectively a tax on growth. Smaller businesses often feel this most sharply - when you are 15 or 50 people, paying per seat for software only a handful use heavily is hard to justify.



Frappe takes a different position: a business should pay for **how much it uses**, not for how big its headcount is. This is **compute-based pricing** - you pay for the work the machines actually do, not for how many people log in or how long the system stays open.



The practical consequence is the line that matters most:



> **Cost is tied to usage, not to headcount.**



Your system can be open all day, with hundreds of users logged in, and still cost little if there is no heavy processing happening behind the scenes. As your business grows, cost grows gradually and predictably - not as a straight line tied to employee count.



## What "compute" actually means

"Compute" is precise, and it is easy to misunderstand, so it is worth being exact - particularly because the distinction affects how you read a plan.



Compute is **CPU time actively spent processing your work** - running a report, saving an invoice, importing data, sending emails, executing background jobs. It is *not* the same as the time your system is open, the hours your business runs, or how long a user sits on a screen.



> **Compute time ≠ business hours ≠ screen time ≠ login time.**



When a user creates an invoice, the CPU is not engaged for the whole time the form is open. It works for milliseconds at a time - when the system pulls a customer record, when it saves the document - and only that active processing time counts. An ERP can be open all day across a large team and consume very little compute if the underlying processing is light.



How this plays out depends on whether you are on shared or dedicated infrastructure, which is covered in [Frappe Cloud plans](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing):



- On **shared infrastructure**, compute means the CPU time your tasks actively consume - you are charged for the processing you actually trigger.
- On **dedicated infrastructure**, compute means the resources you reserve - CPU, memory, and storage that are yours regardless of moment-to-moment use.



## Why this is built this way

A useful analogy is a co-working space. On shared infrastructure you rent a desk - affordable, with the building, power, security, and maintenance handled for you, and you pay for the time you use it. On dedicated infrastructure you reserve a private room - more expensive, fully yours, and the bigger the room the higher the price, but once paid you use it however you like.



The point of offering both, across multiple cloud providers and server architectures, is to avoid forcing every customer into the same cost model. A small business should not pay enterprise prices; an enterprise should not be boxed into SMB constraints. For a growing business of any size, the lasting benefit is that the model lets you scale without redesigning everything - you adjust plans as your needs change rather than renegotiating licences.



For many customers, this is the single biggest reason Frappe Cloud proves dramatically cheaper over time than per-user alternatives.

<!-- page: customer-guide/customer-guide__pricing__total-cost-of-ownership-tco.md -->
---
title: "What are all the costs involved?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco"
updated: "2026-07-21"
---

The price of a Frappe Cloud plan is only one line in the true cost of running a business system. To compare Frappe against alternatives honestly - and to budget realistically - you need to look at **total cost of ownership (TCO)**: everything you will spend across the full lifecycle, typically over five years.



The components below apply to any business, but their *weight* depends heavily on your size. A smaller business will often find several of them shrink to very little - or disappear - so read this as a complete checklist, not a bill everyone pays in full.



This page lays out what goes into TCO so you can build a complete picture. 



## Why licence price misleads

Buyers routinely compare software on the headline figure - the per-seat licence, or the monthly subscription - and are then surprised by the real bill. The licence is often a *minority* of lifetime cost. The components below are where the rest lives, and they vary enormously between options. A system with a low licence fee but a costly, high-risk implementation can easily cost more over five years than a higher-licence alternative that goes live cleanly.



Frappe's advantage starts from an unusual place: **the software licence cost is zero.** But that makes it *more* important, not less, to account honestly for the other components - which is what this page does.



## The components of 5-year TCO

**1. Software licensing.** For Frappe: zero. The software is open source. For proprietary alternatives, this is the per-user or per-module licence, usually paid annually and rising with headcount. Over five years and a growing team, this is frequently the largest single line for proprietary systems - and the one Frappe removes entirely.



**2. Hosting and infrastructure.** What you pay to run the system. On Frappe Cloud, this is your Site or Server plan — compute, storage, and bundled support - as described in [Frappe Cloud plans](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing). If you self-host, this is your own servers, plus the staff time to operate them (see [the self-hosting comparison](https://docs.frappe.io/customer-guide/getting-started/self-hosted-vs-frappe-cloud)).



**3. Implementation.** The cost of getting live - configuration, process mapping, and the partner's professional fees. This is usually a significant one-time cost and varies with the complexity of your operation. It is covered in [Implementation - what to expect](https://docs.frappe.io/customer-guide/implementation/what-to-expect).



**4. Data migration.** Moving your data out of existing systems and into the new one. The effort depends on how clean your current data is and how many systems you are consolidating. Underestimating this is a common cause of budget overruns.



**5. Customisation and integration.** Adapting the system to your processes and connecting it to other tools. Frappe's structure helps here in two ways: ordinary customisation (fields, scripts, workflows) doesn't require expensive development, and integration *between* Frappe products is near-zero because they share one platform - see [the product portfolio](https://docs.frappe.io/customer-guide/about-frappe/product-portfolio).



**6. Training.** Bringing your team up to speed. Costs depend on the number of users and the depth of training. Frappe School and partner-led training are the usual routes.



**7. Ongoing support and maintenance.** What you pay year after year to keep the system healthy and supported. On Frappe Cloud, platform and app support is bundled into your plan, with Product Warranty and priority SLAs available at higher tiers. With a partner, this includes support for your specific deployment.



**8. Upgrades.** The cost of staying current. This is a frequently overlooked line for proprietary ERPs, where major version upgrades can become full re-implementation projects. On Frappe Cloud, upgrades are automated and managed, which materially reduces this cost over a five-year horizon.



> **If you're a smaller business:** several of these components are light or absent at your scale. Implementation may be something you largely do yourself (or with a few hours of free onboarding from Frappe - see [how Frappe works](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company)); data migration may be a simple import; customisation and training may be minimal. In many SMB cases, your real ongoing cost is close to just your Frappe Cloud plan. Don't let the eight-line model below imply a heavier project than yours actually is.



## A simple TCO frame

To compare options fairly, lay out all eight components across five years for each candidate system:






| Component                   | Year 1 | Years 2–5 (annual) | Notes                                       |
| --------------------------- | ------ | ------------------ | ------------------------------------------- |
| Software licensing          |        |                    | Zero for Frappe; per-seat for proprietary   |
| Hosting / infrastructure    |        |                    | Frappe Cloud plan, or self-host + ops staff |
| Implementation              |        | -                  | One-time, partner-led                       |
| Data migration              |        | -                  | One-time; depends on data quality           |
| Customisation / integration |        |                    | Lower where products share a platform       |
| Training                    |        |                    | Front-loaded, with some ongoing             |
| Support / maintenance       |        |                    | Bundled into Frappe Cloud plans             |
| Upgrades                    |        |                    | Automated on Frappe Cloud                   |


The pattern that usually emerges - most pronounced for larger, growing organisations: proprietary systems front-load less implementation but carry heavy, growing licence and upgrade costs across years 2–5; Frappe carries comparable implementation but near-zero licence cost and lower upgrade cost, so the five-year total bends sharply in its favour - especially as headcount grows.



## Self-hosting vs Frappe Cloud

Because Frappe is open source, self-hosting is a genuine option, and some businesses with strong internal IT choose it. It is important to compare honestly: self-hosting can make raw infrastructure look cheaper, but it shifts real, ongoing operational cost and risk onto your team. Frappe's own comparison frames the trade-off clearly:






|                    | Self-hosted                   | Frappe Cloud                          |
| ------------------ | ----------------------------- | ------------------------------------- |
| Deployment         | Manual, via Linux shell       | UI-based, containerised               |
| Upgrades           | Manually configured cron jobs | Scheduled and managed from the UI     |
| Backups            | Manual, error-prone           | Automated, including offsite          |
| Monitoring & logs  | Manual configuration          | Automated, always on                  |
| Disaster recovery  | Manual, error-prone           | Automated, always on                  |
| Access control     | Unrestricted                  | Granular, at site/server/bench level  |
| SSH access         | Yes, without logging          | Yes, with audit logs                  |
| Analytics          | Not available                 | Detailed resource analytics           |
| Utilisation alerts | Not available                 | Proactive (CPU, memory, disk)         |
| Frappe app support | Not available                 | Available for first-party Frappe apps |
| Pricing            | Complicated, unpredictable    | Simple, fair, predictable             |


The honest summary, in Frappe's own words: self-hosting is *not always* more expensive on paper, but Frappe Cloud "often reduces hidden costs such as DevOps effort, downtime risk, failed upgrades, and long-term maintenance." For most businesses - and especially SMBs without a dedicated ops team - the staff time and operational risk of self-hosting outweigh the infrastructure saving. But the choice is genuinely yours, which is itself a benefit of the open-source model.



## A note on honesty

This guide would rather you budget accurately than be surprised later. Frappe removes the licence-fee line entirely, and reduces upgrade and integration costs structurally - but implementation, migration, training, and support are real costs with any business system, including this one (in proportion to your size). Plan for all eight components, and compare like-for-like across the alternatives you are evaluating.



---

<!-- page: customer-guide/customer-guide__scalability__architecture-overview.md -->
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

<!-- page: customer-guide/customer-guide__scalability__do-frappe-apps-scale.md -->
---
title: "Do Frappe apps scale?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/do-frappe-apps-scale"
updated: "2026-07-02"
---

This is one of the first questions serious buyers ask, and it deserves an honest answer rather than a reflexive "yes."



The honest answer is: **it depends on your specific workload - and Frappe is more scalable by default than most people expect.** A confident "yes, it scales infinitely" from any vendor should make you skeptical, because real scalability is never unconditional. What matters is understanding *your* constraints, knowing where the limits actually are, and having a clear plan for the rare cases that need engineering. This section gives you that.



## What "scale" actually means

When people say "does it scale," they're usually conflating two different things, and separating them makes the conversation precise:



- **Latency** - how fast the system responds to a single action. Opening a document, saving an invoice, running a report. When users *complain* about performance, they're almost always complaining about latency ("saving takes ten seconds").
- **Throughput** - how much the system can process over time. Ten thousand invoices a day, payroll for tens of thousands of employees. When users *worry* about scalability in advance, they're usually thinking about throughput.



The two are related - very high latency on an operation drags down throughput - but they're diagnosed and solved differently. A good scalability conversation asks about both: not just "how many users," but "how many doing what, how often, and how fast does each action need to be?"



## More scalable than expected - some real examples

Without naming customers, here is the kind of scale Frappe applications run in production today:



- A **payroll run for 30,000+ employees**.
- A **stock-broking platform processing millions of transactions per day**.
- A deployment spanning **500+ warehouses across 13 companies and 40 branches**, sustaining continuous transaction volume.
- A migration that **processed 100,000+ invoices in a matter of hours**, replacing a legacy enterprise system.



These aren't theoretical benchmarks; they're live systems. They don't prove that *any* workload will work unchanged - they prove that Frappe's architecture reaches serious enterprise scale, and that when a specific workload pushes a limit, there's a known path through it.



## How to read the rest of this section

The reality of scaling is that it's a layered playbook, moving from easy to expert:



1. For most workloads, **it simply works** at the default configuration.
2. When you need more, you **scale up resources** - often in minutes.
3. When resources stop being the answer, you **find and fix the bottleneck** - usually in the database.
4. For unusual or extreme cases, there are **architectural options** and expert help.

The pages that follow walk through this: 

[How scaling works architecturally](https://docs.frappe.io/customer-guide/scalability/how-scaling-works)

[The scaling playbook](https://docs.frappe.io/customer-guide/scalability/the-scaling-playbook) 

[How scaling relates to cost](https://docs.frappe.io/customer-guide/scalability/scaling-and-cost) 

[Honest limits and when to get help](https://docs.frappe.io/customer-guide/scalability/limits-and-seeking-help) 



> **If you're a smaller business:** most of this section describes what's possible at the upper end, not what you'll need to do. At your scale, Frappe runs comfortably on default configurations - you can read this for reassurance that you won't outgrow the platform, and skip the technical depth unless you're curious.



---

<!-- page: customer-guide/customer-guide__scalability__how-scaling-works.md -->
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

<!-- page: customer-guide/customer-guide__scalability__limits-and-seeking-help.md -->
---
title: "When should you seek help?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/limits-and-seeking-help"
updated: "2026-07-02"
---

A guide that only listed strengths wouldn't be trustworthy. Frappe scales further than most people expect, but it isn't magic, and being straight about the edges is part of helping you make a sound decision.



## What isn't trivial today

A few things are genuinely hard, or not yet available out of the box:



- **Data archiving.** Automatically moving very old data out of the live system isn't a built-in feature, and it's hard to generalise - because business logic determines what can safely be archived (last year's invoice may still have payments being settled this year, so it can't simply be cut off). For now, archiving older data is handled case-by-case rather than by a single switch. 
- **Database sharding.** Splitting a single very large dataset across multiple database servers (so old data lives on cheaper storage) isn't a packaged offering today. It's a recognised future need for the largest, oldest deployments rather than a present capability.
- **Unbounded, automatic, infinite scale.** Frappe allocates real resources to your system rather than scaling limitlessly on demand like some cloud-native architectures. In practice this matches how essentially all serious ERPs work - and the handful of architectures that scale "infinitely" also scale their bills infinitely, which is rarely what a business actually wants. The autoscaling described in [the scaling playbook](https://docs.frappe.io/customer-guide/scalability/how-scaling-works) handles real-world load spikes; it is not a promise of limitless elasticity.



Stating these plainly matters more than glossing over them: it means you can trust the capabilities we *do* describe.



## Scaling well is a skilled job

The honest conclusion from years of running large deployments is that scaling a system to serious volume is **a multi-disciplinary, high-skill job.** It draws on database expertise, infrastructure knowledge, and understanding of the application's internals. Most of the time the fixes are well-understood and even routine - but identifying *which* fix, *where*, takes expertise.



This means an organisation expecting to operate at high scale should plan to either build that expertise in-house or buy it. That's not a quirk of Frappe; it's true of any system at scale. What Frappe offers is that, because it's open source and built on standard, widely-understood components, the expertise is broadly available - your own DBAs, your partner's engineers, and Frappe itself can all work on it, rather than you depending on a single vendor's closed support queue.



## Where to get help

There are clear routes when you need expert hands:



- **Your partner's engineers** can do most optimisation and scaling work as part of your engagement (see [implementation](https://docs.frappe.io/customer-guide/implementation/what-to-expect)).
- **Frappe Premium Support / scalability consulting** is available for fast-growing companies and mission-critical deployments. This is where Frappe's own experts help with the non-routine challenges - database performance optimisation, profiling and refactoring code, designing background-job and staging-table strategies, and architecture-level scalability consulting. It's aimed squarely at organisations pushing into territory that hasn't been routinely battle-tested. 
- **The open-source community** - a large base of developers and partners who run Frappe at scale and share approaches openly.



## The bottom line for your evaluation

Put together, the scalability story is: Frappe runs at genuine enterprise scale today; for most workloads it simply works; when you need more there's a clear, layered playbook from one-click resource upgrades through to architectural options; cost scales with usage rather than headcount; a few advanced needs aren't yet packaged; and expert help is available through multiple independent channels. That's a defensible, honest basis on which to decide.



> **If you're a smaller business:** none of the limits above will affect you. They describe the frontier of very large deployments. At your scale, the platform's defaults are more than sufficient, and the relevant takeaway is simply that you have abundant room to grow.



---

<!-- page: customer-guide/customer-guide__scalability__scaling-and-cost.md -->
---
title: "What is the cost of scaling?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/scaling-and-cost"
updated: "2026-07-02"
---

An honest scalability discussion has to include cost, because the two are inseparable - and being clear about this upfront prevents unwelcome surprises later.



## Scaling is real, but it isn't free

The plain truth: **scalability does not mean your costs stay flat as you grow.** If your workload increases - more transactions, more data, more concurrent users - you will need more resources to handle it, and more resources cost more. Any vendor who implies that growth is free is misleading you.



What Frappe's model *does* give you is that cost scales with **actual usage** rather than with headcount. Because pricing is compute-based, not per-user (see [pricing philosophy](https://docs.frappe.io/customer-guide/pricing/pricing-philosophy)), your bill tracks the work your system genuinely does. A growing team that uses the system lightly doesn't cost dramatically more; a workload that genuinely intensifies does. That's a fairer and more predictable relationship between growth and cost than per-seat licensing - but it is still a real relationship.



## When money is the right answer, and when it isn't

There's an important judgement here that's worth making deliberately:



- **Scaling up is often the right first response.** When you're genuinely under-resourced, adding capacity is fast, low-risk, and frees your people to keep working. For a business where the cost of an hour of engineering exceeds the cost of a larger server, paying for resources is simply the rational choice - and for many enterprises, the incremental hosting cost is minor relative to the value the system delivers.
- **But money stops working past a point.** Beyond a certain level, adding resources yields little, because the constraint is no longer capacity - it's a specific bottleneck that needs engineering (see [the scaling playbook](https://docs.frappe.io/customer-guide/scalability/how-scaling-works)). Pouring money into a bigger and bigger server at that stage is like adding highway lanes to fix a problem that's really about road design: you hit a ceiling quickly. At that point, targeted optimisation is both cheaper and more effective than more hardware.



The practical implication for budgeting: plan for resources to scale with your workload, and recognise that at high scale, some spend will shift from infrastructure to expertise (optimisation, consulting). Both are legitimate costs of running a large system - with any platform.



## The fuller cost picture

Scaling cost is one input into total cost of ownership, alongside implementation, customisation, support, and the rest. The complete five-year framework - and how to compare it honestly against alternatives - is in [Pricing and total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco).



> **If you're a smaller business:** this is largely a non-issue for you. At your scale, a standard plan covers your needs and your costs stay modest and predictable. The cost-of-scale conversation matters most for organisations running heavy or rapidly-growing workloads.



---
