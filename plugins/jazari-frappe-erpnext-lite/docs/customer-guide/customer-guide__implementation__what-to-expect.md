---
title: "What to expect? (Lifecycle)"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/what-to-expect"
updated: "2026-07-21"
---

Choosing the software is the decision everyone focuses on. But the software is rarely why business-software projects succeed or fail - the *implementation* is. Industry studies of ERP projects have consistently found that a large share run over budget, over time, or fail to deliver the expected benefits, and almost always for the same reasons: unclear scope, poor data, inadequate training, weak change management, and an underestimated effort. Very few fail because the software couldn't do the job.



This section sets honest expectations about what implementing Frappe involves - the phases, the timeline, who is accountable, and the risks that actually sink projects - so you go in with eyes open. The depth here is aimed at larger deployments; if you're a smaller business, the same shape applies in a lighter, faster form, and we flag where.



## The implementation lifecycle

A well-run implementation moves through six phases. They overlap in practice, but the order matters.



**1. Discovery and planning.** Before anything is configured, the implementation team - usually your partner working with your stakeholders - maps how your business actually operates: your processes, your data, your reporting needs, your integrations, and the gaps between how you work today and how the system works out of the box. This phase produces a scope, a plan, and a shared understanding of what "done" looks like. Time spent here pays back several times over; skipping it is the most common root cause of later trouble.



**2. Configuration.** The system is set up to match the agreed scope - company structure, chart of accounts, modules, roles and permissions, and the workflows your business runs. For most businesses, a large portion of needs are met through configuration alone, without custom code.



**3. Customisation and integration.** Where your processes genuinely require something the standard system doesn't do, customisations are built - and connections to your other systems are established. Frappe's architecture helps here: ordinary adaptation (custom fields, scripts, workflows) doesn't require heavy development, and integration *between* Frappe products is near-zero because they share one platform. External integrations use the REST API. Keeping this phase disciplined - customising only where there's real business value - is one of the biggest levers on cost and timeline.



**4. Data migration.** Your existing data is cleaned, mapped, and moved into the new system. This is consistently one of the most underestimated phases - see [Data migration](https://docs.frappe.io/customer-guide/implementation/data-migration).



**5. Training and user acceptance.** The people who will use the system are trained, and they test it against real scenarios (user acceptance testing) to confirm it does what they need before go-live. This is also where change management earns its keep - see [Change management](https://docs.frappe.io/customer-guide/implementation/change-management).



**6. Go-live and hypercare.** The system goes into production, often in phases, followed by a period of intensive support ("hypercare") while users settle in and the inevitable early issues are resolved quickly. See [Go-live](https://docs.frappe.io/customer-guide/implementation/go-live-and-beyond).



## Typical timelines

There is no single answer, because timeline scales with scope, complexity, and the number of entities and integrations involved. As a directional guide rather than a promise: 

- **A smaller business** with standard processes, a single entity, and little customisation can often go live in a few weeks - sometimes self-serve, sometimes with light partner help.
- **A mid-sized business** with several modules, some customisation, and real data migration typically runs a few months.
- **A large or multi-entity business** with significant customisation, multiple integrations, and phased rollout across locations can run from several months to a year or more.



The honest variables that move these numbers: how clean your data is, how many customisations you insist on, how decisively your team makes decisions, and how well change is managed. Of these, *your* responsiveness and discipline often matter more than anything the software or partner controls.



## Why projects go wrong - and how to avoid it

Since most failures are predictable, they're largely preventable. The recurring causes, and the antidotes:



- **Scope creep** - endless "while we're at it" additions. *Antidote:* a clear initial scope, and a deliberate decision process for changes.
- **Over-customisation** - rebuilding the software to mirror old processes instead of adopting better standard ones. *Antidote:* customise only where there's genuine business value; treat the standard way as the default.
- **Poor data** - migrating years of messy data and expecting clean results. *Antidote:* clean before you migrate, and migrate only what you need.
- **Inadequate training** - going live with users who don't understand the system. *Antidote:* train against real scenarios, and don't compress this to save time.
- **Weak executive sponsorship** - no one senior owns the outcome. *Antidote:* a named sponsor who clears obstacles and keeps the organisation committed.
- **Underestimating change** - treating it as an IT project rather than a business change. *Antidote:* manage the human side deliberately - see [Change management](https://docs.frappe.io/customer-guide/implementation/change-management).



The rest of this section goes deeper on the parts that most determine success: who is accountable, choosing a partner, data migration, change management, and a clean go-live.



---