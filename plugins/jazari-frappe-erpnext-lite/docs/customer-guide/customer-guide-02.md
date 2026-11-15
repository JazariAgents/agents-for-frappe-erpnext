<!-- Frappe documentation: customer-guide, part 2 of 6. Index: docs/INDEX.md -->

<!-- page: customer-guide/customer-guide__competitive-comparisons__frappe-vs-proprietary-saas.md -->
---
title: "Frappe vs Proprietary SaaS"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas"
updated: "2026-07-02"
---

If you're evaluating Frappe, you're almost certainly evaluating other options too - and you should. This part of the guide compares Frappe with the systems enterprises most often consider alongside it, as fairly as we can manage.



A word on how to read these pages, because it sets the right expectation.



## Our approach to comparison

We've tried to write these comparisons the way a good advisor would, not the way a salesperson would. That means three commitments:



- **We name where the alternative genuinely wins.** Every product here is chosen by serious organisations for good reasons. A comparison that pretended otherwise would be worthless to you - and you'd see through it. Where another system is the better fit for a particular need, we say so.
- **We focus on durable, structural differences** - licensing model, cost structure, how the products are built and delivered, customisation, lock-in - rather than feature-by-feature checklists that go stale within a release or two. Specific features and prices change constantly; the structural differences are what actually shape your experience over years.
- **We don't tell you what to conclude.** Each page ends with "consider the alternative if…" and "consider Frappe if…" so you can match the choice to your own situation.



One caveat worth stating plainly: competitor products, editions, and pricing change frequently. We've described them as accurately as we can, but you should verify current specifics directly with each vendor before deciding. Where something is especially prone to change, we've flagged it.



## The recurring themes

A few differences come up across almost every comparison, because they flow from how Frappe is fundamentally built. Rather than repeat them on every page, here they are once:



- **Licensing and cost model.** Frappe's software is open source (no licence fee), and Frappe Cloud is priced on compute/usage rather than per user. Most alternatives charge per user, per month - so their cost rises with headcount, while Frappe's tracks actual usage. Over five years and a growing team, this is often the single largest cost difference. See [Pricing and total cost of ownership](https://docs.frappe.io/customer-guide/pricing/pricing-philosophy).
- **One platform vs a suite of parts.** Frappe's applications - ERP, CRM, HR, Helpdesk, and more - are built on a single framework and share one data model, login, and permission system. Several alternatives assembled their suites through acquisition or as separate modules, so integration between them is more involved. See [the product portfolio](https://docs.frappe.io/customer-guide/about-frappe/product-portfolio).
- **Ownership and lock-in.** Because Frappe is open source, you can access your data and code, customise deeply, self-host, and leave if you choose. Proprietary alternatives keep the code closed and the exit costlier. See [what open source means for you](https://docs.frappe.io/customer-guide/about-frappe/what-open-source-mean-for-you).
- **Delivery model.** Frappe is product-only and delivered through certified partners (or, for smaller businesses, directly on Frappe Cloud). Some alternatives sell and implement directly; others are also partner-led. See [how Frappe works as a company](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company) .



Where a comparison turns on one of these, we point back here rather than restating it.



## The comparisons

- [ERPNext vs Odoo](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-odoo) - the closest open-source comparison
- [ERPNext vs Zoho](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-zoho) 
- [ERPNext vs Tally](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-tally) - primarily India
- [ERPNext vs SAP Business One](https://docs.frappe.io/customer-guide/competitive-comparisons/erpnext-vs-sap-b1) - SAP's mid-market offering
- [ERPNext vs Quickbooks](https://docs.frappe.io/customer-guide/competitive-comparisons/erpnext-vs-quickbooks)
- [ERPNext vs SAP S/4HANA](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-sap-s4-hana) - large-enterprise ERP
- [ERPNext vs Microsoft Dynamics 365](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-ms-d365) 
- [ERPNext vs Oracle NetSuite](https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-oracle-netsuite)

<!-- page: customer-guide/customer-guide__getting-started__self-hosted-vs-frappe-cloud.md -->
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

<!-- page: customer-guide/customer-guide__implementation__change-management.md -->
---
title: "How to manage the transition?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/change-management"
updated: "2026-07-21"
---

Here is the uncomfortable truth about business-software projects: the technology is rarely the hard part. The hard part is people. A perfectly configured system that your team resists, works around, or quietly ignores is a failed project - and this, more than any technical issue, is why implementations disappoint. Change management is the deliberate work of bringing people with you, and it is too often left to chance.



## Why it matters more than it seems

New software changes how people do their jobs - sometimes how they've done them for years. That provokes real, predictable human reactions: anxiety about competence, attachment to familiar tools, suspicion of why the change is happening, and quiet resistance from people who were never asked. None of this shows up in a feature comparison, and all of it determines whether the system actually gets used as intended.



Underinvesting here is the most common unforced error in the whole project. The cost of good change management is small relative to the implementation; the cost of skipping it is a system nobody fully adopts.



## What good change management looks like

It isn't complicated, but it has to be intentional:



- **Executive sponsorship that's visible.** Someone senior must own the outcome and be seen to back it - not just approve the budget, but communicate why this matters and stay engaged. When leadership treats it as important, the organisation does too.
- **A clear "why."** People accept change far better when they understand the reason for it. Explain what the business gains and - honestly - what's in it for them, not just for the company.
- **Involve users early.** The people who will use the system should be heard during discovery and testing, not handed a finished thing. Involvement turns potential resisters into advocates, and surfaces real-world problems while they're still cheap to fix.
- **Identify champions.** In each team, find the respected, capable people who can learn the system early, help their colleagues, and carry credibility you can't impose from above.
- **Communicate continuously.** Tell people what's changing, when, and what it means for them - before it happens, not after. Silence breeds rumour and resistance.
- **Train properly, against real work.** Generic training doesn't stick. Train people on the actual tasks they'll do, with their actual data, close enough to go-live that it's fresh.
- **Plan for the dip.** Productivity often drops right after go-live as people learn. Expect it, staff for it (see [hypercare in Go-live](https://docs.frappe.io/customer-guide/implementation/go-live-and-beyond)), and reassure people it's normal - so a temporary dip doesn't get read as failure.



## Scaling to your size

- **Larger organisations** should treat change management as a named workstream with an owner, a communication plan, and identified champions across departments. The more people and locations involved, the more deliberate this must be.
- **Smaller businesses** need the same principles in lighter form: be clear about why, involve the team, train on real tasks, and have leadership visibly behind it. With fewer people, communication is easier - but the human reactions are identical, so don't skip it just because you're small.



The throughline: **you own this.** A partner can advise and train, but the credibility, communication, and sponsorship have to come from inside your organisation. It's the part of the project no one can do for you - and the part most worth doing well.



---

<!-- page: customer-guide/customer-guide__implementation__choosing-a-partner.md -->
---
title: "How to choose the right partner?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/choosing-a-partner"
updated: "2026-07-21"
---

For most mid-sized and large deployments, your partner matters as much as the software - they are who you'll actually work with, and the quality of your implementation rests largely on them. Frappe has a network of 180+ partners across 50+ countries, of varying size, specialisation, and experience. This page is about choosing well.



## How partners are organised

Frappe certifies and tiers its partners, with tiers reflecting their scale of business and track record with Frappe. A higher tier signals volume and experience, but it is not the only thing that matters - fit for *your* situation matters more. You can find partners through [Frappe's partner directory](https://frappe.io/partners/list). 



## What to look for

Weigh these when evaluating a partner:



- **Relevant experience.** Have they implemented for businesses like yours - your industry, your size, your complexity? An implementer who knows your sector will anticipate needs a generalist won't.
- **Functional depth, not just technical.** The best partners understand *business processes* - accounting, manufacturing, supply chain - not only how to configure the software. Ask how they'd handle a process specific to you.
- **A real methodology.** Good partners have a structured approach to discovery, configuration, testing, and go-live - not an ad-hoc "we'll figure it out" style. Ask them to walk you through how they run a project.
- **References you can talk to.** Ask for customers of similar size and industry, and actually speak to them - about what went well, what didn't, and how the partner handled problems.
- **Local presence and language**, if that matters to your operation and support expectations.
- **Capacity and continuity.** Do they have the people to staff your project properly, and will the team that sells it be the team that delivers it?
- **A clear view of support after go-live.** Implementation ends; the relationship doesn't. Understand how they support you once you're live.



## Questions worth asking before you sign

A few questions that surface a lot, quickly:



- How many implementations like ours have you done, and can we speak to two of those customers?
- Who specifically will be on our project, and what's their experience?
- How do you scope and price - fixed, time-and-materials, or phased - and what happens when scope changes?
- How do you approach data migration, and how do you handle messy source data?
- How do you handle customisation requests - do you push back when standard would serve us better?
- What does support look like after go-live, and what does it cost?



## Red flags

Be cautious of a partner who: promises a timeline or price before understanding your processes; agrees to every customisation without questioning whether it's needed; can't provide relevant references; is vague about who will actually do the work; or treats the project as purely technical with no interest in your business outcomes.



## A note for smaller businesses

If you're a small business with standard needs, you may not need a partner at all to start - Frappe Cloud's self-serve model and free onboarding can get you live (see [how Frappe works](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company)). Consider a partner when your processes are complex, when you lack the internal time, or when the cost of getting it wrong is high enough to want expert hands. You can always engage one later.

---

Read this blog to know more: [A guide to working with Frappe partners](https://frappe.io/blog/community/a-guide-to-working-with-frappe-partners)

<!-- page: customer-guide/customer-guide__implementation__data-migration.md -->
---
title: "How to migrate data properly?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/data-migration"
updated: "2026-07-21"
---

Data migration is the phase businesses underestimate most, and the one that most often causes delays and go-live stress. Moving from your existing systems into Frappe is rarely just a copy - it's cleaning, mapping, and reconciling data that has usually accumulated inconsistencies over years. Treating it seriously from the start is one of the highest-return things you can do.



## Why it's harder than it looks

The data in your current systems is rarely as clean as you think. Duplicate customers, inconsistent product codes, missing fields, obsolete records, and reconciliation gaps are normal. Migrate that as-is, and you carry every problem into the new system - and undermine trust in it on day one. The work isn't the moving; it's the cleaning and deciding.



## What to migrate - and what not to

A useful discipline: migrate what you *need*, not everything you *have*.



- **Master data** - customers, suppliers, items, employees, the chart of accounts. This you almost always need, and it's worth cleaning thoroughly.
- **Open transactions** - outstanding invoices, open orders, current stock balances. Needed to operate from day one.
- **Opening balances** - financial balances as of go-live, so your books are correct.
- **Historical transactions** - years of closed transactions. Here, be selective. You often *don't* need to migrate full history into the live system; keeping it accessible in an archive or the old system for reference is frequently cheaper and cleaner than migrating it all. Decide based on real need - legal retention, reporting, audit - not on instinct to keep everything.



## How migration works with Frappe

Frappe provides structured ways to import data - typically via spreadsheet-based import tools that map your source columns to the system's fields, with validation to catch errors before they land. For larger or more complex migrations, data can be brought in programmatically through the API. Your partner usually leads this, building and testing the mapping, running trial imports, and reconciling results. 



The pattern that works: **map, trial-import a sample, reconcile, fix, then do the full run** - never a single untested bulk load straight into production.



## A sensible sequence

1. **Audit** your source data and decide what's in scope.
2. **Clean** at source where you can - dedupe, standardise, fill gaps.
3. **Map** source fields to Frappe's structure.
4. **Trial migrate** a representative sample into a test environment.
5. **Reconcile** - do totals, counts, and balances match the source? Have users check records they know.
6. **Fix** mapping and data issues, and repeat the trial until it's clean.
7. **Final migration** as part of go-live, with a final reconciliation before you rely on it.

## For smaller businesses

If you're small and your data lives in a spreadsheet or a simple system, migration may genuinely be straightforward - clean the spreadsheet, use the import tool, check the results. The principles above still apply (clean first, reconcile after), just at a lighter weight. The free onboarding from Frappe can help with a basic import (see [how Frappe works](https://docs.frappe.io/customer-guide/about-frappe/how-frappe-works-as-a-company)).



---

<!-- page: customer-guide/customer-guide__implementation__go-live-and-beyond.md -->
---
title: "What to do post Go-Live?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/implementation/go-live-and-beyond"
updated: "2026-07-21"
---

Go-live is the moment the new system becomes the real one. Handled well, it's an anticlimax - things simply work. Handled badly, it's where months of effort unravel in the first chaotic week. The difference is preparation and a realistic plan for the period right after.



## Going live: phased or all at once

There are two broad approaches, and the right one depends on your size and risk tolerance:



- **Phased rollout** - go live module by module, or location by location, over time. Lower risk: problems are contained and lessons carry forward. Slower, and it means running old and new systems in parallel for a while. Usually the right choice for larger or multi-entity businesses.
- **Big-bang** - everything goes live at once. Faster and cleaner once done, with no prolonged parallel running, but higher risk because everything is new simultaneously. More viable for smaller, simpler deployments.



There's no universally right answer; the more complex and critical your operation, the more a phased approach reduces risk.



## A go-live readiness checklist

Don't go live on a hope. Confirm, explicitly, that:



- **Data is migrated and reconciled** - final balances, open transactions, and masters check out against the source.
- **User acceptance testing is signed off** - the people who'll use it have tested real scenarios and confirmed it works for them.
- **Users are trained** - and trained recently, on real tasks.
- **Integrations are tested** - connections to other systems work end to end, not just in theory.
- **Permissions and roles are correct** - people can do what they need, and can't do what they shouldn't.
- **Backups are confirmed working** - you can recover if something goes wrong (on Frappe Cloud this is managed; verify it's in place).
- **A support plan for week one is ready** - everyone knows who to ask when something doesn't work.
- **A rollback or contingency plan exists** - what you'll do if a serious problem surfaces.



If any of these isn't true, the honest move is usually to delay rather than push through. A slipped date is recoverable; a botched go-live erodes the trust the system needs to succeed.



## Hypercare: the critical first weeks

The period immediately after go-live - often called "hypercare" - is when issues surface and users are least confident. Plan for it deliberately:



- **Heightened support on standby** - your partner and internal champions available to resolve issues fast, before frustration sets in.
- **A clear channel for problems** - people need an obvious, easy way to report what's not working and get help.
- **Rapid triage** - fix the urgent things immediately; queue the rest visibly so people know they've been heard.
- **Expect the productivity dip** - it's normal as people adjust (see [Change management](https://docs.frappe.io/customer-guide/implementation/change-management)). Reassure, support, and it passes.



Hypercare typically runs a few weeks, tapering as issues drop and confidence rises.



## Settling into steady state

Once the system is stable, the relationship shifts to ongoing operation:



- **Platform and software health** is handled by Frappe Cloud - upgrades, backups, monitoring, and bug support (see [who does what](https://docs.frappe.io/customer-guide/implementation/who-does-what)).
- **Functional support** for your specific deployment comes from your partner.
- **Continuous improvement** - most businesses keep refining: adding modules, improving workflows, building on what they've learned. The system should evolve with you, not freeze at go-live.



A closing thought worth holding onto from the start: a business system is not a project that ends, but a capability you operate. The implementation gets you live; the value comes from using it well over the years that follow.



## For smaller businesses

A small, standard deployment may "go live" almost casually - you've been testing with real data, and one day it's simply your system of record. The checklist above still applies in spirit (reconcile your data, make sure people know how to use it, confirm backups), just lighter. The free onboarding and Frappe Cloud's managed platform remove much of the operational risk that larger self-managed go-lives carry.

<!-- page: customer-guide/customer-guide__implementation__what-to-expect.md -->
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

<!-- page: customer-guide/customer-guide__implementation__who-does-what.md -->
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

<!-- page: customer-guide/customer-guide__introduction.md -->
---
title: "Introduction"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/introduction"
updated: "2026-07-21"
---

Choosing business software is not only about features. You are also choosing how your data will be managed, who will implement and support the system, what it will cost over time, and how easily it can adapt as your business changes.

This guide brings those questions together. It is written for businesses evaluating ERPNext, Frappe HR, Frappe CRM, Frappe Helpdesk, or any other product in the Frappe ecosystem. The aim is simple: help you make a decision with fewer assumptions and fewer surprises.

## Who is this guide for?

The guide is meant for everyone involved in the buying decision. In a small business, that may be one founder or operator. In a larger organisation, it may include business teams, IT, security, finance, procurement, and leadership.

Each reader will care about different questions. Business teams will focus on process fit. IT will examine architecture, integrations, and maintainability. Security teams will ask about controls and evidence. Finance and procurement will look at cost, contracts, and vendor risk. The guide is designed so that each person can go directly to what matters to them.

## What does the guide cover?

It covers the questions that usually shape a serious software decision:

- Who Frappe is and how the company works
- What the products do and how they fit together
- Hosting, security, scalability, reliability, and support
- Pricing and the full cost of ownership
- Implementation, migration, adoption, and upgrades
- How Frappe compares with other options
- Customer stories from different industries and use cases

## How is this different from product documentation?

Product documentation explains how to use the software. It shows how to configure a workflow, create an invoice, manage leave, restore a backup, or build an integration.

This guide answers the questions that come before and around product use. It helps you understand what you are buying, what responsibilities come with it, and whether it is a sensible fit for your organisation.

## How should I read it?

You do not need to read it from beginning to end. Start with the questions that are unresolved for you. If you are early in the evaluation, begin with the company, products, hosting model, and pricing. If you are already deep into the process, go directly to security, scalability, implementation, support, or comparisons.

Partners can also use the guide with customers. It creates a shared reference for discussing what the product can do, what needs configuration or customisation, what the hosting platform manages, and what the customer must own internally.

## What can this guide not replace?

The guide cannot replace discovery, a product demonstration, a proof of concept, or a detailed implementation proposal. It also cannot guarantee that every statement will remain current forever. Product features, prices, plans, and policies change, so time-sensitive details should always be confirmed before a final decision.

What it can do is help you ask better questions, understand the answers, and spot gaps before they become expensive.

<!-- page: customer-guide/customer-guide__introduction__is-frappe-right-for-you.md -->
---
title: "Is Frappe right for you?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/introduction/is-frappe-right-for-you"
updated: "2026-07-21"
---

Frappe can support organisations ranging from small businesses adopting their first structured system to enterprises running complex operations. That does not make it the right choice for everyone.

Fit depends on the problems you are solving, how much flexibility you need, how you want the system to be hosted and supported, and how willing your organisation is to participate in implementation and change.

## Frappe is likely to be a strong fit when...

**You want connected business applications.** Frappe offers applications for ERP, HR, CRM, support, analytics, and other needs on a shared technology foundation. This is useful when you want data and workflows to move across functions without maintaining many disconnected systems.

**You value ownership and choice.** Frappe products are open source. You can inspect the code, customise it, choose where it runs, and retain the option to change hosting or service providers.

**Your processes need adaptation.** Frappe supports configuration, workflows, scripts, integrations, and custom applications. It suits businesses that need more flexibility than a rigid, ready-made product can offer.

**You expect broad usage.** The software itself is not licensed per user. This can be valuable when many employees, suppliers, customers, or other users need access.

**You are comfortable working with an implementation partner.** For most mid-sized and large projects, a Frappe partner handles discovery, configuration, customisation, migration, training, and functional support.

**You want room to start small and expand.** A business can begin with one application or a simple setup and add more products, entities, integrations, or infrastructure as its needs grow.

## Frappe may not be the best fit when...

**You only need a narrow, standard tool.** If the requirement is limited to basic accounting, invoicing, or one simple departmental workflow, a focused product may be quicker to adopt.

**You need a highly specialised capability out of the box.** Frappe can be extended, but building and maintaining a niche capability may not be sensible when a specialised product already does it well.

**You want one vendor to take complete responsibility.** Frappe, the implementation partner, the hosting platform, and the customer each own different parts of the outcome. Your team will still need to make decisions, provide clean data, test the system, and lead adoption.

**You cannot invest in implementation or change.** Even a good product needs process decisions, data preparation, training, and user involvement. Complex organisations should not treat implementation as a side task for IT.

**You have a non-negotiable compliance, certification, deployment, or technology requirement that is not currently supported.** These conditions should be checked before spending time on detailed evaluation.

**You need every process to remain exactly as it is today.** Frappe is flexible, but copying every legacy process into a new system can create excessive customisation and long-term maintenance risk.

## Is company size the deciding factor?

No. A small manufacturer may have more demanding ERP needs than a much larger services company. Complexity matters more than headcount.

The useful questions are: How many entities, locations, and countries are involved? How much data and transaction volume will the system handle? How many integrations and customisations are required? How critical is the system to daily operations? What security, availability, and compliance obligations apply?

## How should we confirm the fit?

Use a focused evaluation rather than relying on a general demonstration.

- Identify the most important business outcomes and workflows.
- Test those workflows using realistic scenarios and data.
- Separate standard capability, configuration, customisation, integration, and gaps.
- Validate the implementation approach and the people who will deliver it.
- Confirm hosting, support, security, compliance, scalability, and upgrade requirements.
- Estimate the full cost, including implementation and internal effort.
- Speak with customers whose industry, complexity, or scale resembles yours.

At the end, you should know both where Frappe fits and where it does not. That is a stronger basis for a decision than a long feature checklist or a confident sales promise.
