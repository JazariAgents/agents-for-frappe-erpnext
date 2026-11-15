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