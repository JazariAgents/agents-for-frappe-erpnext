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