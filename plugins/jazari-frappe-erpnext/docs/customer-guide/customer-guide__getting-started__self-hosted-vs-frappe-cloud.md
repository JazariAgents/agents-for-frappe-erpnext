---
title: "Where to host the app and data?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/getting-started/self-hosted-vs-frappe-cloud"
updated: "2026-07-21"
---

Because Frappe is open source, you have a genuine choice in how you run it: on **Frappe Cloud** (managed by Frappe) or **self-hosted** (managed by you). This is a real decision with real trade-offs, and it's worth making deliberately rather than by default. This page frames the choice; the cost dimension is covered in detail in [Total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco).



## What each option means

**Frappe Cloud** is managed infrastructure. Frappe handles hosting, upgrades, backups, monitoring, security, and uptime, and provides first-party application support - you focus on using the software. You choose your cloud provider, region, and plan, and the operational work is done for you. See [Frappe Cloud plans](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing).



**Self-hosting** means running the software on your own infrastructure. You have complete control and the raw infrastructure cost can be lower - but you take on all the operational work: installation, upgrades, backups, monitoring, security patching, disaster recovery, and scaling. The software is the same; the responsibility shifts to your team.



## How to decide

The honest decision comes down to a few questions:



**Do you have the operational capability?** Self-hosting business-critical software well requires real DevOps capacity - people who can manage upgrades safely, monitor the system, handle backups and recovery, and respond when something breaks at an inconvenient hour. If you don't have a dedicated team for this, Frappe Cloud almost always works out better, both in cost and in risk.



**How critical is uptime?** If downtime seriously hurts your business, the managed monitoring, recovery, and support on Frappe Cloud are hard to replicate yourself without significant investment.



**Do you have specific control or residency requirements?** Some organisations have data-residency rules or internal policies that mandate self-hosting or a specific environment. (Note that Frappe Cloud's multi-region, multi-provider options satisfy many residency requirements without self-hosting - see [Frappe Cloud plans](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing).)



**What's the true cost?** Self-hosting can look cheaper on raw infrastructure, but the staff time, the risk of failed upgrades or downtime, and ongoing maintenance often make Frappe Cloud the more economical choice once everything is counted. [Total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco) includes a side-by-side comparison.



## The usual answer, by size

- **Smaller businesses** almost always choose Frappe Cloud - there's rarely a reason to take on infrastructure work at that scale, and the self-serve model is built for it.
- **Mid-sized and large businesses** mostly choose Frappe Cloud too, for the managed operations and support, often on dedicated servers (see [Frappe Cloud plans](https://docs.frappe.io/customer-guide/pricing/frappe-cloud-pricing)). Some with strong internal IT and specific control requirements self-host - a legitimate choice the open-source model fully supports.



The key point is that this isn't a one-way door. You own the software either way, so you can start on Frappe Cloud and move to self-hosting later, or the reverse, as your needs change. That freedom is itself a benefit of the open-source model - see [What open source means for you](https://docs.frappe.io/customer-guide/about-frappe/what-open-source-mean-for-you).



For self-hosting, the installation steps live in the [Frappe Cloud documentation](https://docs.frappe.io/cloud/local-fc-setup). 