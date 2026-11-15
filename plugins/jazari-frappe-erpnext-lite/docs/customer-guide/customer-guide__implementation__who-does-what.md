---
title: "Who does what? (Operating Model)"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/who-does-what"
updated: "2026-07-21"
---

One of the most common sources of confusion - and finger-pointing - in software projects is unclear accountability. Frappe's delivery model makes the division of responsibility clearer than most, precisely because the roles are structurally separate. Knowing who owns what, before you start, prevents the "I thought *they* were handling that" failures that derail projects.



## The three parties

**Frappe** builds and maintains the products and the platform. Frappe does not implement (see [how Frappe works as a company](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company)). What Frappe owns:

- The software itself - features, fixes, and ongoing development.
- Frappe Cloud - hosting, infrastructure, upgrades, backups, monitoring, uptime.
- First-party application support - bug-fixing in Frappe products and the platform, available through Frappe Cloud (Product Warranty and higher tiers; see [Pricing](https://docs.frappe.io/customer-guide/pricing/pricing-philosophy)).



**Your partner** delivers your implementation and owns your customer relationship. What the partner owns:



- Discovery, scoping, and project management.
- Configuration, customisation, and integration for your business.
- Data migration.
- Training and go-live support.
- Functional support for your specific deployment after go-live.



**You** own the decisions, the people, and the business change. What you own:



- Defining requirements and making decisions promptly.
- Providing clean data and the people who know your processes.
- Executive sponsorship and driving adoption internally.
- User acceptance testing and sign-off.



This is the single most important distinction to hold onto: **Frappe stands behind the product and the platform; your partner stands behind your implementation; you own the decisions and the change.** Each is accountable for what it actually controls.



## A simple responsibility map


| Activity                                            | Frappe | Partner | You |
| --------------------------------------------------- | ------ | ------- | --- |
| Software development & fixes                        | ●      |         |     |
| Hosting, infrastructure, upgrades (on Frappe Cloud) | ●      |         |     |
| Platform & app bug support                          | ●      |         |     |
| Discovery & scoping                                 |        | ●       | ◐   |
| Configuration & customisation                       |        | ●       | ◐   |
| Data migration                                      |        | ●       | ◐   |
| Training                                            |        | ●       | ◐   |
| Functional support (your deployment)                |        | ●       |     |
| Requirements & decisions                            |        | ◐       | ●   |
| Clean data & subject-matter experts                 |        |         | ●   |
| Executive sponsorship & adoption                    |        |         | ●   |
| User acceptance & sign-off                          |        |         | ●   |


● owns it · ◐ contributes



## If you self-host or go direct

Two variations on the standard model:

- **If you self-host**, the infrastructure responsibilities in Frappe's column shift to you (or your partner, if they manage hosting for you) - installation, upgrades, backups, monitoring, recovery. [See Frappe Cloud or self-hosting](https://docs.frappe.io/customer-guide/getting-started/self-hosted-vs-frappe-cloud).
- **If you're a smaller business going direct** (no partner), you take on the partner column yourself, with optional help from Frappe's free onboarding for the basics. This is workable at small scale and with standard processes; as complexity grows, a partner becomes worth it.