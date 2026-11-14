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