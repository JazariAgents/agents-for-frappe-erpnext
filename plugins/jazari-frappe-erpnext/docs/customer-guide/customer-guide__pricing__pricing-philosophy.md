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