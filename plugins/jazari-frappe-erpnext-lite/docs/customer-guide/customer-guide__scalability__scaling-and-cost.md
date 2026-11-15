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