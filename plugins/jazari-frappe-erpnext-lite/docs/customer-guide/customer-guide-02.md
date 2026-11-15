<!-- Frappe documentation: customer-guide, part 2 of 2. Index: docs/INDEX.md -->

<!-- page: customer-guide/customer-guide__security__infra-network-security.md -->
---
title: "How is the infrastructure secured?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/infra-network-security"
updated: "2026-06-22"
---

Infrastructure and Network are the most foundational layers in Frappe Cloud. While they are technically distinct, they are addressed together for security owing to their interconnected nature. Here is what makes Frappe Cloud secure in these layers. 

---

## Globally recognised cloud providers

Frappe Cloud runs on established cloud infrastructure providers, including Amazon Web Services (AWS), Oracle Cloud Infrastructure (OCI), Hetzner, and DigitalOcean. These providers offer:

- Physical data centre security
- Network segmentation
- Redundancy, and 
- Baseline DDoS protection

This leverage is passed on to users by default. 

---

## Reverse Proxy

Traffic entering Frappe Cloud is routed through proxy layers before reaching application servers. The proxy server secures incoming traffic by acting as an intermediary that masks the server's true IP address, inspects data packets for threats, and filters malicious requests before they reach the backend. 



Here is an architecture diagram of Frappe Cloud (traffic enters from the top). Notice that Proxy sits at the entry point. 



![](https://drive.frappe.io/api/method/writer.api.embed.get?id=24erat618m)

Here are some specifics of how proxies protect the servers.

- **IP Masking:** The proxy exposes its own IP address to the internet, shielding the internal network and server IP address from attackers.
- **Packet Inspection & Filtering:** The proxy scans incoming traffic for malware, SQL injection, and cross-site scripting (XSS) attacks before allowing it through.
- **Access Control:** Proxies enforce security policies, allowing or denying traffic based on rules, which prevents unauthorised access to sensitive data.
- **SSL/TLS Termination:** The proxy can handle encryption, decrypt incoming traffic to inspect it for threats, and then re-encrypt it before sending it to the internal server.



The proxy essentially acts as a protective barrier, preventing direct internet-to-server connections and implementing security policies. Frappe Cloud uses Nginx as the proxy. 

---

## Ports

All communication over networks inside Frappe Cloud occurs over port 443 using HTTPS. Other ports are restricted to necessary services only.

---

## Firewall

Frappe Cloud (as of Feb-2026) relies primarily on provider-level firewalls such as AWS Security Groups. A native firewall layer is under development. This will be a comprehensive firewall with proxy-level, web application-level, and server-level filtering.

---

## Rate limiting

While for DDoS mitigation, Frappe Cloud leverages provider-level protections, there are application-level rate-limiting mechanisms as well to further reduce exposure to volumetric attacks. 

---

<!-- page: customer-guide/customer-guide__security__isolation-mechanisms.md -->
---
title: "What are the isolation mechanisms?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/isolation-mechanisms"
updated: "2026-06-22"
---

Frappe Cloud supports Multi-tenancy. Rather, it is one of the major reasons why the Frappe ecosystem loves Frappe Cloud. However, with great power comes great responsibility! Multi-tenancy means multiple customers reside on the same server and share the same resources. Does that mean they can intrude into each other’s space, making multi-tenancy less secure? 



Well, the answer is No. But to understand this concept further, one must understand the entity hierarchy in Frappe Cloud, viz. Site » Bench » Server » Cluster.  

---

## Frappe Cloud hierarchy

The smallest unit in Frappe Cloud is a **Site**. A site generally represents one business. It has its own database, its own data, its own configuration.



Multiple sites run inside something called a **Bench**. A bench is like a container that holds one or more sites, usually running the same version of ERPNext or Frappe apps. The bench has everything a site needs to run. 



Benches live on **Servers**. A server is simply a virtual computer on the internet with a CPU, memory, and storage. Servers can be of 2 types: 

- Shared - means multiple customers are on the same machine. They “share” the server resources. 
- Dedicated - means one customer gets the entire machine. The resources are “dedicated”.



Multiple servers in one location or data centre are grouped to form **Clusters**. All servers on a cluster work together so that the system can handle failures, upgrades, and high traffic more gracefully. 



To summarise, the hierarchy looks like this: Site → Bench → Server → Cluster. This structure allows Frappe Cloud to support everything from a single small business to large, distributed enterprise systems.

---

## Site-level isolation

When users choose site plans, they share the server resources with other Frappe Cloud users. The sharing is managed by Frappe. In some other cases, users get a site from Frappe Partners (or even other service providers in the ecosystem). In that case, a dedicated server is rented by the Frappe Partner and, in turn, shared by all of their customers. 



While these settings prima facie look insecure, they aren’t. In Frappe Cloud, each site has its own database. Logical separation ensures cross-site access is not possible. In essence, while users may face the “noisy neighbour” problem affecting the site performance, data security is ensured through virtual walls built between sites. 

---

## Bench-level isolation

The lowest Site Plans on Frappe Cloud (e.g. $5 per month or ₹410 per month on AWS/OCI) offer sites on Public Benches. Public benches host multiple sites (running the same version of Frappe apps or Frappe Framework) in one container. This is where the Site-level Isolation (explained above) is the only layer of isolation. 



However, isolation can be strengthened further through Private Benches. In this case, a user gets their own container to run the site/s. All dependencies, workers and services are “private” to the user. When deployed on a private bench, vulnerabilities remain contained within a container, thereby providing another layer of isolation over Site-level Isolation. 



Private Bench plans start from $25 per month or ₹2,050 per month on AWS and OCI. On Hetzner, even the lowest plan (i.e. $5 per month or ₹410 per month) comes with a Private Bench. 



Note - Public benches are not infinite. Users on public benches enjoy bench-level isolation from users on other public and private benches by default. 

---

## VM-level isolation

When users go for server plans, they get an entire virtual machine (VM) for themselves. These VMs could either be dedicated instances or shared instances. In either case, all vulnerabilities are contained inside the environment. Dedicated instances provide stronger isolation as well as optional static IP allocation.  

---

## Cluster-level isolation

Cluster configurations allow communication only within the cluster network. Isolation is enforced at the database, container, and infrastructure levels. For more details, refer to the Infrastructure & Network Security section. 

---

<!-- page: customer-guide/customer-guide__security__logging-monitoring.md -->
---
title: "What about logging & monitoring?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/logging-monitoring"
updated: "2026-07-02"
---

## Visibility Is Essential to Security

Security is not only about preventing incidents - it is also about being able to detect, investigate, and respond when something unusual occurs.



For this reason, modern cloud platforms rely heavily on monitoring and logging systems that provide visibility into the health, performance, and behavior of systems.



Frappe Cloud incorporates monitoring and logging systems that allow the platform team to observe infrastructure activity, detect anomalies, and respond to operational events.



These systems form a critical part of the platform’s operational security model.



---



## Infrastructure Monitoring

Infrastructure monitoring systems track the health and performance of servers and application environments across the platform.



Monitoring systems collect metrics related to:



- CPU usage 
- Memory usage 
- Disk capacity 
- Network activity 
- Application performance 
- Database queries





These metrics help identify abnormal behavior that may indicate system issues, performance degradation, or potential security concerns.



Automated alerts notify the engineering team when certain thresholds are exceeded or when abnormal conditions are detected.



---



## Log Collection and Analysis

Operational logs provide detailed records of system events.



Frappe Cloud collects logs from multiple sources within the platform, including:



- Application logs 
- System logs 
- Deployment logs 
- Database performance logs 
- Error logs 
- Scheduler and background job logs





These logs are aggregated and analyzed using centralized logging systems.



Centralized logging allows engineers to quickly investigate issues, trace operational events, and identify patterns that may indicate security risks.



---



## Customer-Visible Logs

Customers also have access to several logs through the Frappe Cloud dashboard.



These may include:



- Application error logs 
- Background job logs 
- Slow query logs 
- Deployment logs





Access to these logs helps customers troubleshoot issues within their application environments and maintain visibility into system activity.



---



## Monitoring Tools

Frappe Cloud uses a combination of monitoring tools to observe infrastructure and application behavior.



These systems typically include tools such as:



- **Prometheus** for metrics collection 
- **Grafana** for visualization and dashboards 
- **ElasticSearch and Kibana** for log aggregation and analysis 
- **Alertmanager** for alert routing and incident notifications





These tools provide the operational visibility required to maintain platform reliability and security.



---



## Incident Detection

Monitoring systems continuously analyze operational signals to detect issues such as:



- Resource exhaustion 
- Infrastructure failures 
- Application errors 
- Unusual traffic patterns 
- Performance anomalies





When abnormal conditions are detected, alerts are generated so that engineers can investigate and respond.



This early detection capability helps prevent small issues from escalating into larger service disruptions.



---



## Operational Accountability

Logs also provide an important accountability mechanism.



Operational records allow engineers to review historical events and understand:



- What actions were taken 
- When those actions occurred 
- Which systems were affected





This transparency supports incident investigation and helps improve operational processes over time.



---



## Continuous Improvement

Monitoring and logging systems are not only used for troubleshooting. They also provide insights that help improve the platform.



Operational data allows engineering teams to:



- Identify recurring issues 
- Improve system performance 
- Strengthen reliability 
- Enhance security protections





Over time, this feedback loop contributes to a more resilient and secure cloud platform.



---

<!-- page: customer-guide/customer-guide__security__security-assessments.md -->
---
title: "What security testing is done? "
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/security-assessments"
updated: "2026-06-22"
---

## Security Is a Continuous Process

Modern cloud platforms operate in a constantly evolving threat landscape. New vulnerabilities are discovered regularly in operating systems, application frameworks, and third-party dependencies.



Maintaining security therefore requires a continuous process of identifying, evaluating, and resolving potential weaknesses in the platform.



Frappe Cloud follows a structured vulnerability management process designed to detect and address security risks before they can be exploited.



---



## Vulnerability Sources

Security vulnerabilities can originate from several sources, including:



- Operating system packages 
- Application frameworks 
- Third-party libraries 
- Infrastructure configuration 
- Application code





Because Frappe Cloud runs a large ecosystem of open-source software, monitoring and addressing vulnerabilities is an ongoing operational responsibility.



---



## Vulnerability Detection

Potential vulnerabilities may be identified through several channels:



- Internal security reviews 
- Automated dependency monitoring 
- Infrastructure security scanning 
- External security research 
- Responsible disclosure by the community 
- Customer-reported security issues





Open-source software ecosystems often benefit from strong community oversight, which helps surface potential vulnerabilities quickly.



---



## Vulnerability Classification

When a potential vulnerability is identified, it is evaluated based on its severity and potential impact.



Examples include:



- **Low severity** – minimal security impact 
- **Medium severity** – limited exploitability or operational impact 
- **High severity** – potential compromise of system integrity 
- **Critical severity** – risk of unauthorized access or data exposure





Security vulnerabilities are treated as high-priority issues and are handled through the platform’s incident management process.



---



## Patch and Remediation Process

Once a vulnerability is confirmed, remediation actions may include:



- Updating vulnerable software packages 
- Deploying patched versions of dependencies 
- Modifying infrastructure configuration 
- Deploying application fixes





Critical vulnerabilities are prioritized for immediate remediation, while lower severity issues are addressed through scheduled release cycles.



The open-source nature of Frappe Framework and ERPNext allows security fixes to be reviewed, patched, and distributed quickly.



---



## Security Updates and Releases

Software updates are an essential part of maintaining platform security.



Frappe Cloud provides mechanisms to deploy updates across customer environments through controlled upgrade processes.



These updates may include:



- Framework security patches 
- Dependency updates 
- Infrastructure improvements 
- Platform security enhancements





Customers can apply updates using the upgrade tools provided in the Frappe Cloud dashboard.



---



## Responsible Disclosure

Security researchers and members of the open-source community play an important role in improving platform security.



When vulnerabilities are discovered, responsible disclosure practices encourage researchers to report them privately so that they can be investigated and resolved before public disclosure.



Frappe encourages responsible reporting of security vulnerabilities and investigates such reports promptly.



---



## Security Culture in an Open Ecosystem

Because the Frappe ecosystem is open source, the code powering the platform is publicly visible and auditable.



While this transparency requires careful security practices, it also allows:



- Independent review by developers 
- Faster identification of issues 
- Community participation in improving security





This collaborative ecosystem contributes to the long-term security and resilience of the platform.



---

<!-- page: customer-guide/customer-guide__success-story-kyosk.md -->
---
title: "Success Story: Kyosk"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/success-story-kyosk"
updated: "2026-06-22"
---

**Kyosk** started using ERPNext in 2021. As their scale of operations and breadth of use cases on ERPNext grew, so did the data volume and performance load on servers. By 2024, the database had grown to around 350 GB, with the General Ledger table alone holding nearly 60 million entries, summing up to more than 55 GB in size. Key financial reports (like Trial Balance, AR-AP reports, etc.) started taking longer to generate and sometimes even time out due to the sheer size of data. 



Kyosk’s IT team approached Frappe with this problem. Frappe engineers stepped in and did a deep RCA on the issue. It was revealed that the customer was working on an older version of ERPNext, which did not feature the “closing account balance” calculations that make report generation lighter (as the old version ingested the entire historical GL data before processing reports every time, leading to heavy load on compute). Even upgrading to the latest version was difficult owing to the suboptimal indexing of data and inefficiencies in running of the closing voucher tasks.



Frappe’s engineering team worked tirelessly along with a local certified implementation partner to resolve these challenges. The solution involved refactoring the closing balance and closing voucher logic, introducing optimised indexes, and tuning report queries for very large datasets. The results were dramatic! To give you an example, the Trial Balance report (which earlier took 15-20 minutes) started loading in under two minutes. 



This engagement shows how complex, high-volume environments benefit from proactive OEM involvement. With Enterprise Application Support plan in place, even seemingly intractable problems at enterprise scale can be addressed quickly and effectively, ensuring that Frappe apps continue to deliver value without forcing a costly move to proprietary ERP systems.

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-ms-d365.md -->
---
title: "ERPNext vs. MS D365"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-ms-d365"
updated: "2026-07-02"
---

**Microsoft Dynamics 365** is Microsoft's family of business applications - ERP and CRM delivered as a set of cloud apps closely tied to the wider Microsoft ecosystem (Microsoft 365, Azure, Power Platform). It's a common alternative for organisations already invested in Microsoft, so the comparison often turns as much on ecosystem as on the ERP itself.



## Who Dynamics 365 is for, and where it fits well

Dynamics 365 spans multiple applications - including Business Central for SMB/mid-market ERP and the Finance & Operations apps for larger enterprises - plus CRM-oriented apps, all licensed individually and integrated with Microsoft's broader stack.



In fairness, there are situations where it's a strong choice:



- **Heavily Microsoft-invested organisations** that want tight integration with Microsoft 365, Teams, Azure, and Power Platform. 
- **Teams that value familiarity** with Microsoft's interface conventions and tooling.
- **Enterprises wanting a single large-vendor relationship** spanning productivity, cloud, and business apps.



If your organisation is deeply standardised on Microsoft and values that integration above all, Dynamics is a natural fit.



## The key difference: an ecosystem of licensed apps vs an open platform

The central contrast is how the system is composed and paid for.



Dynamics 365 is **proprietary and sold as separate apps, licensed per user per app**, with much of its value realised through the surrounding Microsoft ecosystem (and often the Power Platform for customisation, itself licensed). Costs and capabilities are spread across multiple SKUs, and you operate within Microsoft's commercial model.



Frappe is **open source and unified** - one framework, one data model, broad functionality included, customisation built in rather than via a separately-licensed platform.



For a buyer: cost (per-user-per-app licensing, potentially across several apps, versus usage-based hosting with no licence), coherence (a composed set of apps versus one platform), and ownership (closed versus open) - see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas).



## Criticisms customers and partners commonly raise

*Commonly reported experiences*, not universal facts. 

- **Licensing complexity** - multiple apps and SKUs make it hard to predict what you'll actually pay. 
- **Costs compound** across per-user, per-app, and add-on Power Platform licensing.
- **Fragmentation** - the "Dynamics 365" line spans quite different products (e.g. Business Central vs Finance & Operations), which can confuse evaluation and limit portability between them. 
- **Heavy partner dependence** for implementation and customisation.
- **Best value only inside the Microsoft world** - much of the benefit assumes you're all-in on Microsoft.



Frappe's structural answers: one platform instead of many licensed apps, usage-based pricing with no per-app multiplication, customisation native to the framework (no separately-licensed tool), and an open codebase you own.



## Where Frappe fits best

- **You don't want cost spread across per-user, per-app licences.** Why it matters: usage-based pricing on one platform avoids the SKU-stacking that makes Dynamics' total cost hard to predict and prone to growth.
- **You want one coherent system, not a composed family.** Why it matters: a single framework and data model means consistent behaviour, easy app-to-app data sharing, and no portability gaps between sub-products.
- **You aren't committed to the Microsoft ecosystem** - or don't want your ERP's value to depend on being all-in on one vendor's stack. Why it matters: Frappe stands on its own and integrates via open APIs, so you keep your freedom of choice elsewhere.
- **You want customisation included, not separately licensed.** Why it matters: adapting Frappe doesn't mean buying and learning a separate platform.



## In short


|                  | Dynamics 365                         | Frappe                          |
| ---------------- | ------------------------------------ | ------------------------------- |
| Model            | Proprietary, multiple apps           | Fully open source, one platform |
| Typical pricing  | Per user, per app (+ Power Platform) | Compute/usage-based hosting     |
| Coherence        | Composed family of apps              | Single framework + data model   |
| Cost as you grow | Rises with users, apps, add-ons      | Tracks usage                    |
| Best value       | Inside the Microsoft ecosystem       | Standalone, open integrations   |
| Lock-in profile  | Proprietary; ecosystem-tied          | Open across the stack           |


**Consider Dynamics 365 if** you're deeply invested in Microsoft and want tight integration across its ecosystem above other considerations.



**Consider Frappe if** you want one coherent, open platform you own - usage-priced, with customisation included, and without tying your ERP's value to a single vendor's wider stack.



---

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-odoo.md -->
---
title: "ERPNext vs. Odoo"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-odoo"
updated: "2026-07-02"
---

**Odoo** is the comparison most prospects evaluating Frappe will also run, and for good reason: it's the other major open-source business-software platform, and the two share a similar promise - a broad, customisable suite without the lock-in of traditional proprietary ERP. Because they start from such similar premises, the differences that matter are more subtle than in the other comparisons, and worth understanding precisely.



## Who Odoo is for, and where it fits well

Odoo is a broad suite of business applications - accounting, CRM, inventory, manufacturing, HR, e-commerce, and a large catalogue of additional apps - popular with SMBs and mid-market companies worldwide. It's known for breadth of functionality, a polished interface, and a large ecosystem of apps and partners.



In fairness, there are situations where it's a strong choice:



- **Breadth of ready-made apps.** Odoo's catalogue of built-in and marketplace apps is extensive, and for some niche functions you may find a ready Odoo app where you'd need to build or source one on Frappe. 
- **Polished out-of-the-box experience** in several functional areas, with a long track record across many countries.
- **A large global partner and developer ecosystem**, which can mean easier access to local implementers in some markets.



If your priority is the widest possible catalogue of pre-built apps and you're comfortable with Odoo's commercial model, it's a credible option.



## The key difference: the open-source model itself

Here's the distinction that matters most, because it surprises people who assume "both are open source" means the same thing.



Odoo operates on an **open-core** model. There's a free Community edition, but a significant share of functionality - and much of what larger organisations end up needing - sits in the paid, proprietary Enterprise edition. In practice, the open-source version and the version most businesses actually run are different products. 



Frappe does not do this. The applications are **fully open source** - there isn't a feature-locked "real" version held back behind a paywall. What you can run for free is the complete product; what you pay for is hosting and support, not unlocked features. (This is the open-core-vs-hosting distinction covered in [Frappe's business model](https://docs.frappe.io/customer-guide/about-frappe/business-model).)



For a buyer, this has two practical consequences. First, **cost trajectory**: Odoo's Enterprise edition is typically priced per user, so cost rises with headcount in the familiar proprietary way, whereas Frappe's compute-based hosting tracks usage (see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas)). Second, **lock-in**: on Odoo Enterprise you're depending on proprietary components again, which narrows the open-source exit advantage; on Frappe the whole stack stays open.



## Criticisms customers and partners commonly raise

These come up repeatedly from Odoo users and implementers - *commonly reported experiences*, not universal facts, and Odoo works to address them. Still, they recur often enough to weigh. 

- **The upsell to Enterprise can feel like a funnel** - production-grade needs tend to sit in the paid edition, so "free and open source" turns into a paid commitment sooner than expected.
- **Costs compound on two axes** - per user *and* per app/edition - and some users report being surprised by what wasn't included. 
- **The Community/Enterprise split causes friction** - community modules can lag, and some third-party apps don't track Enterprise cleanly.
- **Upgrades can be painful**, especially with customisations. 
- **Partner friction at scale** - reported tension over partner terms, and a per-user model that gets expensive in a way that sits awkwardly with the open-source positioning.



Frappe avoids these structurally, not by goodwill: no feature-gated edition (no funnel, no split), compute-based pricing (no compounding with users or apps), and managed, automated upgrades on Frappe Cloud. Not perfection - every platform has trade-offs - but the structural causes above simply aren't present.



## Where Frappe fits best

- **You want genuinely complete open source.** With Frappe there's no feature-locked edition waiting to charge you as you grow - the free product *is* the full product. Why it matters: your access to capabilities, your data, and your code never becomes a negotiating lever a vendor can pull later. What you evaluate is what you keep.
- **You expect your user count to grow.** Frappe's compute-based pricing means cost tracks the work your system does, not how many people can log in. Why it matters: a per-seat model effectively taxes hiring - every new employee adds licence cost whether or not they use the system heavily. Over five years and a growing team, the difference compounds into one of the largest cost gaps between the two.
- **You value a single underlying framework.** Frappe's apps are built on one framework with one data model, and customisation uses the same consistent tooling across every app. Why it matters: you learn one way of extending the system, your customisations and integrations behave consistently, and connecting apps to each other is near-effortless because they already share a database and permission model - rather than stitching across modules that behave differently. 
- **You want predictable upgrades.** On Frappe Cloud, upgrades are managed and automated. Why it matters: upgrade pain is one of the most common long-term complaints with any business system - when staying current is a managed service rather than a recurring project, you keep getting security and feature updates without the cost and risk of a migration each time.
- **You're served by Frappe's partner network, or you're small enough to self-serve.** Why it matters: you get local implementation expertise where it's available, and if you're a smaller business you can start directly on Frappe Cloud without waiting on anyone - flexibility that suits both ends of the size range.



## In short


|                       | Odoo                                                       | Frappe                            |
| --------------------- | ---------------------------------------------------------- | --------------------------------- |
| Open-source model     | Open-core (Community free; Enterprise paid/proprietary)    | Fully open source                 |
| Typical pricing       | Per user, and effectively per app/edition                  | Compute/usage-based hosting       |
| Cost as you grow      | Rises with users and with apps/features adopted            | Tracks usage, not headcount       |
| Breadth of ready apps | Very broad catalogue                                       | Broad, on one shared framework    |
| Upgrades              | Reported as painful with customisations                    | Managed/automated on Frappe Cloud |
| Lock-in profile       | Reduced on Community; proprietary dependence on Enterprise | Open across the stack             |


**Consider Odoo if** the widest catalogue of pre-built apps is your top priority and its commercial model suits you.



**Consider Frappe if** you want fully open-source software with no feature paywall, usage-based rather than per-seat cost, and a single consistent platform you can own and extend without limit.



---

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-oracle-netsuite.md -->
---
title: "ERPNext vs. Oracle Netsuite"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-oracle-netsuite"
updated: "2026-07-02"
---

**Oracle NetSuite** is one of the longest-established cloud ERPs - a single, integrated suite delivered purely as software-as-a-service, popular with mid-market and larger companies. It's often on the shortlist alongside Frappe for organisations wanting a unified cloud ERP, so the comparison is a common one.



## Who NetSuite is for, and where it fits well

NetSuite is a cloud-native, all-in-one ERP covering financials, CRM, inventory, e-commerce, and more, with strong multi-entity and multi-currency capabilities. It's frequently chosen by growing mid-market companies and multi-subsidiary businesses.



In fairness, there are situations where it's a strong choice:



- **Multi-entity, multi-currency, multinational operations** - NetSuite's consolidation and global financials are a long-standing strength. 
- **Companies wanting a mature, unified cloud suite** with a single vendor and a long track record.
- **High-growth businesses** that value a system positioned to span finance through operations as they scale.



If unified multi-entity cloud financials are central to your needs, NetSuite is a capable, proven choice.



## The key difference: a closed SaaS suite vs an open platform

The core contrast is openness and the commercial relationship.



NetSuite is **proprietary, subscription SaaS, licensed per user plus modules** - you rent access, you can't self-host or access the code, and customisation happens within NetSuite's own framework (SuiteCloud). It's unified, but entirely on Oracle's terms.



Frappe is **open source and own-able** - unified too, but you can run it where you like (including self-hosted), access and extend the code freely, and pay for usage rather than seats and modules.



For a buyer: ownership (rented and closed versus owned and open), cost (per-user-plus-module subscription versus usage-based hosting), and exit (difficult versus genuinely open) - see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas).



## Criticisms customers and partners commonly raise

*Commonly reported experiences*, not universal facts. 

- **Aggressive renewal pricing** - a frequently-cited concern is cost increasing notably at renewal once you're committed. 
- **Cost grows with users and modules** - the base suite often needs additional licensed modules for full capability.
- **Customisation can be costly and specialised**, often requiring NetSuite-specific expertise or partners.
- **Lock-in** - no self-hosting and no code access make leaving hard.
- **Implementation and add-on costs** that can exceed initial expectations.



Frappe's structural answers: no licence and usage-based pricing (no renewal-leverage dynamic), broad capability without module-by-module licensing, accessible customisation on an open codebase, and a genuine exit because you own the software and data.



## Where Frappe fits best

- **You don't want to be exposed to renewal leverage.** Why it matters: when you own open-source software and pay for usage, there's no "we have your data, here's the new price" dynamic at renewal - your costs aren't a lever a vendor can pull once you're committed.
- **You want a genuine exit option.** Why it matters: the ability to self-host and access your code and data means the relationship stays healthy precisely because you *could* leave - the strongest answer to "what if this goes wrong?"
- **Cost should track usage, not seats and modules.** Why it matters: NetSuite's per-user-plus-module model compounds as you grow; Frappe's usage-based hosting doesn't.
- **You want unified ERP without the closed model.** Why it matters: you get the single-suite coherence NetSuite is valued for, on an open platform you control.



## In short


|                  | Oracle NetSuite                  | Frappe                           |
| ---------------- | -------------------------------- | -------------------------------- |
| Model            | Proprietary SaaS (rented)        | Fully open source (owned)        |
| Typical pricing  | Per user + modules, subscription | Compute/usage-based hosting      |
| Renewals         | Reported to rise at renewal      | Usage-based; no renewal leverage |
| Hosting          | Vendor-only cloud                | Frappe Cloud or self-hosted      |
| Cost as you grow | Rises with users and modules     | Tracks usage                     |
| Lock-in profile  | High; no code/data exit          | Open across the stack            |


**Consider NetSuite if** mature, unified multi-entity cloud financials from a single established vendor are your priority and the SaaS-only model suits you.



**Consider Frappe if** you want unified ERP you actually own - usage-priced, host-able anywhere, with a real exit and no renewal-time surprises.



---

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-sap-s4-hana.md -->
---
title: "ERPNext vs. SAP S4 HANA"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-sap-s4-hana"
updated: "2026-07-02"
---

**SAP S/4HANA** is the enterprise-ERP heavyweight - the system many of the world's largest companies run, and often the incumbent Frappe is measured against in big enterprise evaluations. The two are built on almost opposite philosophies, so the comparison is less about features and more about what kind of system, cost structure, and relationship you want for the next decade.



## Who SAP S/4HANA is for, and where it fits well

S/4HANA is SAP's flagship ERP, aimed at large and very large enterprises with complex, global operations. It runs on SAP's in-memory HANA database and is typically deployed on-premise or through SAP's cloud programs.



In fairness, there are situations where it's a strong choice:



- **Very large, complex global enterprises** with deep, industry-specific process requirements that SAP has refined over decades. 
- **Highly regulated multinationals** that need exhaustive country-by-country localisation and the assurance of the category's most established vendor.
- **Organisations that have standardised on SAP** across the business, with the in-house teams and budget to run it.



If you're a global enterprise whose processes are already built around SAP and whose scale justifies the investment, S/4HANA is a serious, capable system.



## The key difference: weight, cost, and ownership

The distinction that matters most is the kind of commitment you're taking on.



SAP S/4HANA is **proprietary, heavyweight, and expensive to own** - substantial licensing, specialised (often costly) implementation talent, long implementation timelines, and significant ongoing cost. That weight buys depth, but it also means the system tends to dictate terms to the business rather than the other way around, and leaving is a major undertaking.



Frappe sits at the opposite end: **open source, lighter to deploy, and priced on usage rather than licences and seats.** You own the software and your data, customisation is more accessible, and you're not locked into a single vendor's roadmap or commercial leverage.



For a buyer, the practical contrasts are cost (SAP's licence-plus-implementation model versus Frappe's no-licence, usage-based hosting - see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas)), time-to-value (months-to-years versus typically faster), and control (closed and vendor-directed versus open and yours).



## Criticisms customers and partners commonly raise

These come up repeatedly about S/4HANA - *commonly reported experiences*, not universal facts. 

- **High total cost** - licensing, implementation, and specialised talent make it one of the most expensive options to own. 
- **Long, complex implementations** - projects are often measured in years and carry real failure risk.
- **Rigidity** - adapting SAP to unusual processes can be hard and costly; businesses often reshape themselves around the software.
- **Specialised, scarce talent** - SAP skills are expensive and not always easy to find.
- **Heavy vendor dependence** - deep reliance on SAP and its ecosystem, with a costly exit.



Frappe's structural answers: no licence cost and usage-based pricing, a lighter and faster implementation, accessible customisation on an open codebase, and no lock-in. Not perfection - SAP's depth is real - but the cost-and-control causes above aren't present.



## Where Frappe fits best

- **You want to own your system, not rent it under a vendor's terms.** Open source means your access, data, and code are never leverage someone else holds. Why it matters: your long-term costs and choices stay in your hands rather than the vendor's.
- **Cost discipline matters.** No licence fees and usage-based hosting. Why it matters: for most organisations outside the SAP-scale tier, S/4HANA's total cost is hard to justify versus the value delivered - Frappe reaches enterprise capability without enterprise-ERP cost.
- **You want speed and adaptability.** Lighter deployment and accessible customisation. Why it matters: a system you can stand up faster and adapt to your processes (rather than reshaping the business around the software) delivers value sooner and stays aligned as you change.
- **You'd rather not depend on scarce, expensive specialists.** Why it matters: Frappe is built on widely-understood open components and delivered through a partner network, so the expertise to run and extend it is more broadly available.



## In short


|                  | SAP S/4HANA                            | Frappe                      |
| ---------------- | -------------------------------------- | --------------------------- |
| Model            | Proprietary                            | Fully open source           |
| Typical pricing  | Licence + implementation + maintenance | Compute/usage-based hosting |
| Cost as you grow | High; rises with scale and seats       | Tracks usage                |
| Implementation   | Often years, high complexity           | Typically faster            |
| Customisation    | Deep but costly/specialised            | Accessible, open codebase   |
| Lock-in profile  | High; costly exit                      | Open across the stack       |


**Consider SAP S/4HANA if** you're a very large, complex global enterprise whose scale and process depth justify the investment, and you have the teams and budget to run it.



**Consider Frappe if** you want enterprise capability without enterprise-ERP cost and lock-in - an open, usage-priced system you own, deploy faster, and adapt freely.



---

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-tally.md -->
---
title: "ERPNext vs. Tally"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-tally"
updated: "2026-07-02"
---

**Tally** (TallyPrime, and long-running TallyERP 9 before it) is the default accounting software for a vast number of Indian businesses - ubiquitous, trusted for compliance, and deeply familiar to accountants. The comparison with Frappe is really a comparison between a focused accounting package and a full business platform, which shapes everything below.



## Who Tally is for, and where it fits well

Tally is primarily accounting and compliance software, with strong bookkeeping, statutory, and GST capabilities tailored to Indian requirements. It's used by an enormous base of SMBs and their accountants across India.



In fairness, there are situations where it's a strong choice:



- **Small businesses whose primary need is accounting and statutory compliance** - Tally does this well and is deeply trusted for it. 
- **Accountant familiarity** - a huge base of accountants know Tally intimately, easing bookkeeping and filing.
- **Low cost and simplicity** for straightforward accounting needs, with minimal setup.



If your need is essentially accounting and Indian compliance for a smaller business, Tally is a proven, economical fit.



## The key difference: an accounting tool vs a full business platform

The central contrast is scope.



Tally is **fundamentally an accounting and compliance product.** It does that core job well, but it isn't a full ERP - capabilities like manufacturing, complex multi-location inventory, CRM, HR/payroll, projects, and cross-functional workflows are limited, absent, or bolted on, and multi-user/multi-location operation at scale is constrained. 



Frappe is a **full business platform** - accounting is one part of an integrated whole that also covers inventory, manufacturing, sales, purchase, CRM, HR, and more, on one open, customisable framework.



For a buyer, the contrast is breadth (single-function versus full ERP), scalability (constrained multi-user/multi-location versus designed-to-scale), and adaptability (fixed product versus open, customisable platform) - see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas).



## Criticisms customers and partners commonly raise

*Commonly reported experiences*, not universal facts. 

- **Not a true ERP** - businesses needing operations beyond accounting outgrow it. 
- **Multi-user / multi-location limits** - constrained for larger, distributed teams. 
- **Limited customisation** without specialised TDL development.
- **Weaker cross-functional workflows** - accounting is strong, but connected operations (order-to-cash, manufacturing, CRM) aren't its design centre.
- **Modernisation and access** - desktop heritage; remote/multi-device and integration patterns can lag modern cloud ERPs.



Frappe's structural answers: full-ERP breadth on one platform, designed-to-scale multi-user/multi-entity operation, open customisation, and a modern web/cloud architecture.



## Where Frappe fits best

- **You've outgrown - or will outgrow - pure accounting.** Why it matters: the costly moment is migrating once operations sprawl beyond books; starting on a full platform means accounting and operations live together from day one.
- **You run real operations, not just books.** Why it matters: manufacturing, multi-location inventory, sales and purchase cycles, CRM, and HR on one system remove the disconnected spreadsheets and tools that grow up around an accounting-only core.
- **You need multi-user, multi-location scale.** Why it matters: a platform built to scale avoids the ceilings a desktop-heritage accounting tool can hit.
- **You want to adapt the system to your business.** Why it matters: open, accessible customisation replaces a largely fixed product.



## In short


|                              | Tally                   | Frappe                              |
| ---------------------------- | ----------------------- | ----------------------------------- |
| Scope                        | Accounting + compliance | Full business platform              |
| Model                        | Proprietary             | Fully open source                   |
| Operations beyond accounting | Limited                 | Full ERP (inventory, mfg, CRM, HR…) |
| Multi-user / multi-location  | Constrained             | Designed to scale                   |
| Customisation                | Limited (TDL)           | Open, accessible                    |
| Architecture                 | Desktop heritage        | Modern web/cloud                    |


**Consider Tally if** your need is essentially accounting and Indian statutory compliance for a smaller business, and you don't expect to need much beyond that.



**Consider Frappe if** you run (or will run) operations beyond accounting - a full, scalable, open platform where books and business live together.



---

<!-- page: customer-guide/enterprise__competitive-comparisons__erpnext-vs-zoho.md -->
---
title: "ERPNext vs. Zoho"
space: "Customer Guide"
url: "https://docs.frappe.io/enterprise/competitive-comparisons/erpnext-vs-zoho"
updated: "2026-07-02"
---

**Zoho** is a broad family of business applications - CRM, books/accounting, people/HR, desk, inventory, and dozens more - popular with SMBs for its affordability and ease of getting started. Its ERP-like capability comes from combining many apps (often via Zoho One), which makes the comparison with Frappe largely one of *one platform versus many apps*.



## Who Zoho is for, and where it fits well

Zoho offers a large catalogue of individual apps that can be bought separately or together (notably the Zoho One bundle), covering most business functions at an accessible price point. It's especially popular with small businesses and individual departments.



In fairness, there are situations where it's a strong choice:



- **Small businesses and departments** wanting affordable, easy-to-start tools for a specific function (CRM, accounting, helpdesk). 
- **Breadth at low entry cost**, particularly via the Zoho One bundle for smaller teams. 
- **Quick self-serve setup** without implementation effort, for straightforward needs.



If you're a small business wanting affordable, ready-to-use apps for relatively standard processes, Zoho is a sensible option.



## The key difference: many apps vs one platform (and depth at scale)

The central contrast is architecture and what happens as you grow.



Zoho is **proprietary and composed of many separate applications**, licensed per user (per app, or bundled), that are integrated with each other but are still distinct products underneath. This is excellent for getting started cheaply, but as needs deepen, the seams between apps and the limits of each app's depth tend to show - and it remains a closed, rented model.



Frappe is **open source and built as one platform** - a single framework and data model spanning ERP, CRM, HR, and more, with the depth of a true ERP (e.g. manufacturing, complex inventory and accounting) and the ability to own, host, and extend it.



For a buyer: coherence (many integrated apps versus one platform), depth (light-to-moderate versus full-ERP depth), and ownership/cost (per-user proprietary versus open and usage-based) - see [the recurring themes](https://docs.frappe.io/customer-guide/competitive-comparisons/frappe-vs-proprietary-saas).



## Criticisms customers and partners commonly raise

*Commonly reported experiences*, not universal facts. 



- **Depth limits** - individual apps can feel shallow for complex needs (e.g. serious manufacturing or advanced accounting). 
- **Seams between apps** - "integrated" apps can still behave like separate products, with inconsistencies and integration quirks.
- **Outgrowing it** - businesses commonly start on Zoho and hit ceilings as they scale, prompting a move to a fuller ERP.
- **Per-user cost** that adds up as teams grow, especially across multiple apps or the full bundle. 
- **Support and consistency** concerns reported across such a large app portfolio.



Frappe's structural answers: full-ERP depth on one consistent framework, genuine single-platform behaviour (shared data model, one login and permission system), an architecture you grow *within* rather than outgrow, and open, usage-based ownership.



## Where Frappe fits best

- **You want room to grow without outgrowing the system.** Why it matters: starting cheap is easy; the expensive moment is migrating off a system you've outgrown. Frappe gives full-ERP depth from the start, so growth means scaling one platform, not replacing it.
- **You want genuine single-platform coherence.** Why it matters: because Frappe's apps share one data model and permission system, a customer or item is one record everywhere - not data synced across apps that each behave a little differently.
- **You need real depth in core operations.** Why it matters: for manufacturing, complex inventory, or serious accounting, an app-suite's per-function depth can fall short where a true ERP doesn't. 
- **You want to own and adapt the system.** Why it matters: open source and usage-based pricing replace a closed, per-user, per-app model.



## In short


|                 | Zoho                          | Frappe                          |
| --------------- | ----------------------------- | ------------------------------- |
| Model           | Proprietary, many apps        | Fully open source, one platform |
| Typical pricing | Per user (per app or bundled) | Compute/usage-based hosting     |
| Coherence       | Integrated but separate apps  | Single framework + data model   |
| Depth           | Light-to-moderate per app     | Full-ERP depth                  |
| Growth path     | Often outgrown at scale       | Scale within one platform       |
| Lock-in profile | Proprietary, rented           | Open across the stack           |


**Consider Zoho if** you're a small business or department wanting affordable, ready-to-use apps for relatively standard needs.



**Consider Frappe if** you want full-ERP depth on one open platform you own and grow within - avoiding the migration that comes from outgrowing a suite of lighter apps.



---
