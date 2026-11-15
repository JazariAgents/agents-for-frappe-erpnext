<!-- Frappe documentation: customer-guide, part 4 of 6. Index: docs/INDEX.md -->

<!-- page: customer-guide/customer-guide__scalability__the-scaling-playbook.md -->
---
title: "What are the scaling mechanisms?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/scalability/the-scaling-playbook"
updated: "2026-07-02"
---

When a Frappe application needs to handle more, there is a clear, layered sequence of responses - moving from the simplest and fastest to the most specialised. Most businesses never go past the first one or two layers. This page walks through all of them, so you can see that there's a known path at every level of demand.



## Layer 1: It works by default

For the large majority of workloads, the default configuration is enough. Frappe applications are designed to be scalable out of the box, and a well-provisioned standard setup comfortably handles the needs of most businesses - including many that consider themselves "large." The first thing worth knowing is that you likely won't need the rest of this page.



## Layer 2: Scale up the resources (elastic compute)

When you do need more capacity, the simplest answer is more resources - and on Frappe Cloud this takes minutes, not a project.



- **Upgrade in minutes.** Move to a larger plan and the system reconfigures automatically - more workers, higher memory limits - without you touching any configuration. On self-managed infrastructure the same upgrade means manual reconfiguration and a restart.
- **Stay ahead of limits.** Frappe Cloud sends alerts at 80% resource consumption, giving you time to upgrade before users feel it. You can also downgrade if you're over-provisioned.
- **It's immediate relief.** Scaling up reliably buys headroom: a growing business gets the certainty that it can keep working while any deeper optimisation is planned, rather than hitting a wall.



This is the right first move whenever resources are genuinely the constraint. Its honest limit: beyond a point, adding resources stops helping, because the bottleneck is no longer raw capacity but something specific that needs fixing (Layer 4).



> **For technical evaluators:** on dedicated infrastructure you get guaranteed resources, which is why it's recommended for serious production workloads - performance is predictable rather than shared. Worker count scales roughly with available RAM, so upgrading a server adds parallel capacity automatically.



## Layer 3: Autoscaling and horizontal scaling

Scaling up makes one server bigger. **Horizontal scaling** adds a second server to share the load during peaks - and Frappe Cloud now does this automatically.



When load rises, a **secondary application server** is brought up alongside your primary one: it syncs the same benches, takes a share of incoming traffic (an identically-sized secondary handles 50% of requests), and keeps the system responsive - with **zero downtime**. When the peak passes, traffic returns to the primary, the secondary shuts down gracefully (finishing queued jobs first), and you stop paying for it.



You control it three ways: **manually**, on **thresholds** (set CPU/memory limits that trigger a scale-up automatically, with email notification), or on a **schedule** (pre-arrange capacity for predictable peaks - a month-end close, a sale day). Billing for the secondary is hourly and only while it's active, at a 10% discount on the primary plan price. 



This directly answers a common enterprise worry - predictable or sudden load spikes - without permanently paying for peak-sized infrastructure.



## Layer 4: Find and fix the bottleneck

When more hardware stops helping, the work shifts from provisioning to optimisation - finding the specific component that's slow and addressing it. This is usually the database, and the techniques are well-established:



- **Indexing.** The fastest, most common fix: add the right database indexes so queries that have slowed as data grew become fast again. Identified by analysing slow-query logs.
- **Right-size the database server.** Ensure the working set fits in RAM (see [how scaling works](https://docs.frappe.io/customer-guide/scalability/how-scaling-works)); upgrade the database tier when last year's data growth approaches available memory.
- **Read replicas.** For read-heavy workloads - heavy or constant reporting especially - a replica database holds a copy of the data so that reads and reports run against it, leaving the primary free for transactions. Configured case-by-case for workloads that genuinely need it.
- **Optimise the code path.** Sometimes a specific operation does more work than it needs to. Profiling tools pinpoint exactly where time goes in an operation, so engineers can streamline the hotspot.



> **For technical evaluators:** the platform ships with the tooling to do this - slow-query logs, query analysis (EXPLAIN), a built-in request **recorder** that breaks a single user action into its underlying queries so you can see precisely what's slow, and Python profiling. On Frappe Cloud these are surfaced in analytics dashboards without SSH; self-managed deployments can use the same underlying tools directly. Database-level options extend to MariaDB replication, MaxScale, and Galera; Redis scales via Redis Cluster; the application tier scales by separating web and job workers onto separate machines and separating read/write queries across a replica.



## Layer 5: Architectural options for extreme cases

A small number of workloads - very high transaction volumes, very large multi-year datasets, or unusual data shapes - call for architectural changes. These exist, and they're how the largest deployments run:



- **High-throughput ingestion.** When an external system pushes huge transaction volumes (e.g. e-commerce orders, IoT), a custom API can insert pre-validated records in bulk, and integrations use queuing, retries, and back-pressure so they don't overwhelm the system. Often the better answer is to post *consolidated* summaries rather than every micro-transaction - worth discussing with your accountant what detail you actually need in the ERP.
- **Report scheduling and materialised views.** Heavy reports can be pre-computed on a schedule or run on dedicated reporting capacity, so they don't slow interactive use.
- **Multi-entity federation.** For large multi-company or multi-branch groups, each subsidiary can run its own instance, with only summary-level transactions posted to a central entity - so each entity scales independently and the centre isn't burdened with every micro-transaction.
- **Custom front-ends.** The standard interface handles a wide range of needs, but a team can build a custom front end on Frappe's REST API for specialised high-volume screens.
- **Refactoring.** Because the software is open source, a genuine hotspot can be profiled and the relevant code rewritten - an option proprietary software simply doesn't offer.



> **For technical evaluators:** federation can be synchronised via event streaming; the entire codebase is auditable and extensible through the app/hooks architecture, so optimisations live in your own apps rather than as fragile core edits - which keeps upgrades clean (see [migrations](https://docs.frappe.io/customer-guide/implementation/data-migration)).



These last layers are specialised work, and they're where Frappe's expert help comes in - covered in [the honest limits and when to get help](https://docs.frappe.io/customer-guide/scalability/limits-and-seeking-help).

<!-- page: customer-guide/customer-guide__security__access-control.md -->
---
title: "How is access controlled? "
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/access-control"
updated: "2026-06-22"
---

## Why Access Control Matters

In any cloud platform, the most sensitive operations are not performed by automated systems alone. Engineers, administrators, and operators sometimes require elevated access to infrastructure in order to maintain the platform, investigate incidents, or resolve customer support issues.



For this reason, managing **privileged access** is one of the most important aspects of platform security.



Frappe Cloud follows the principle of **least privilege**, meaning that individuals and systems are granted only the minimum level of access required to perform their responsibilities. Access permissions are restricted, monitored, and granted only when necessary.



This approach reduces the risk of accidental misuse, unauthorized access, or internal security threats.



---



## Platform-Level Access Controls

Access to the infrastructure running Frappe Cloud is restricted to authorized engineering personnel responsible for operating and maintaining the platform.



Access is controlled through:



- Secure identity management systems 
- Role-based permissions 
- Controlled authentication mechanisms 
- Access revocation policies





Administrative access is granted only to engineers who require it for infrastructure maintenance or incident resolution.



Engineering access to production infrastructure is restricted and periodically reviewed to ensure that only authorized personnel retain access.



---



## Controlled Operational Access

Operational actions on Frappe Cloud are typically executed through the platform’s orchestration system rather than through manual administrative access.



The orchestration layer (Press) manages infrastructure activities such as:



- Creating servers 
- Deploying applications 
- Running upgrades 
- Triggering backups 
- Managing site operations





Because these actions are executed through the platform itself, they follow defined workflows rather than relying on manual commands executed directly on servers.



This architecture reduces the need for engineers to log into servers directly and ensures that most operational actions occur through controlled system processes.



---



## Customer-Level Access Controls

Within each Frappe Cloud site, customers retain full control over their own application-level access permissions.



ERPNext and Frappe applications include robust role-based access control mechanisms that allow organizations to define who can access specific information and actions.



These controls include:



- User account management 
- Role-based permissions 
- Document-level permissions 
- Field-level restrictions 
- Two-factor authentication 
- IP-based access restrictions





These controls allow organizations to enforce internal security policies within their application environment.



---



## Access to Dedicated Servers

For customers using dedicated server deployments, infrastructure access is more flexible.



Customers may be provided with:



- SSH access to their servers 
- Administrative control over their environment 
- The ability to configure additional security controls





In these cases, customers are responsible for managing access to the server environment, including credential management and internal access policies.



Frappe engineers may access the server environment only when required to resolve operational issues or support requests.



---



## Access Logging and Accountability

Operational transparency is an important aspect of secure platform operations.



Administrative actions performed through the platform are recorded through operational logging systems. These logs help maintain accountability and assist in troubleshooting operational events.



Access logging enables the platform team to:



- Review operational activities 
- Investigate incidents 
- Diagnose system issues 
- Improve operational processes





---

<!-- page: customer-guide/customer-guide__security__application-security.md -->
---
title: "What app-sec mechanisms exist?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/application-security"
updated: "2026-06-22"
---

Infrastructure is important. Network controls matter. But most breaches begin at the authentication or permission layer. The application layer is thus the most critical security layer. 



Frappe Cloud relies on the security model built into Frappe Framework. It is a Python and JavaScript-based web application framework that all Frappe apps are built on. Even Frappe Press, which is the heart of Frappe Cloud, is built on Frappe Framework. As mentioned in earlier sections, Security is fundamental in Frappe’s product philosophy and thus, Frappe Framework is also built with necessary security features. 

---

## Two-factor Authentication (2FA)

2FA (or even MFA) exists precisely because phishing and brute-force attacks are common. Even if a password is compromised, the second factor reduces the risk. Frappe Cloud is equipped with 2FA (the two factors being password and OTP). 





---

Roles & Permissions

All Frappe apps are equipped with Role-Based Access Control (RBAC). Permissions can be configured at multiple levels:

- Role level
- Document level
- Field level

In practice, this means organisations can strictly define who can see, modify, or approve specific data. (Remember #2 of the Frappe Security Philosophy?)





Team??







---

## Data Masking

All Frappe apps come with a feature for Data Masking. The technique replaces real data with realistic yet fictional data, ensuring that while the information remains usable for business processes, it cannot be reverse-engineered to reveal the original, sensitive data. Masking is especially important in business software such as ERPs because it protects sensitive, confidential, and personally identifiable information (PII) from unauthorised access, particularly in non-production environments like testing, development, and training.  



At this point, it is also important to distinguish between masking, encryption and permissions.

- **Masking** hides the value of a field but acknowledges its existence. **Permissions** remove visibility entirely. Both of these are techniques used in application security, but for different purposes. Masking ensures that the user is able to know the existence of the field (which is often important for regulators and auditors), but without revealing the real data. Permissions can remove the visibility entirely (regulators or auditors will need special access). 
- **Masking** replaces data with fictional values, keeping the system functional but real data confidential. **Encryption** transforms data into unreadable, reversible values using keys. Masking is used for protection at the UI layer (viz., protecting information from users), whereas encryption is a technique used for securing data from attackers.

Note - The next section is dedicated to the topic of Encryption. 

---

## Brute-force mitigation measures

Apart from 2FA/MFA (covered above) and Rate-limiting (covered in the Infrastructure & Network Security section), the following mechanisms can be built using Frappe Framework to help in protecting against Brute force attacks. 

- Password complexity enforcement 
- Account lockout/delay 
- CAPTCHA/Bot detection
- IP blocking

Are we doing any of these in FC?

Any of these are ready features in Framework?

Any case studies to prove the rest are possible?



Note that Frappe Cloud does not proactively monitor and block IPs or geolocations.  

---

<!-- page: customer-guide/customer-guide__security__backups-recovery.md -->
---
title: "What about Backups & Recovery?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/backups-recovery"
updated: "2026-06-22"
---

## Why Backups Matter

No system is immune to failure.



Hardware can fail, software bugs can corrupt data, users may accidentally delete records, and infrastructure outages can occur. For this reason, every cloud platform must implement reliable backup and recovery mechanisms.



Frappe Cloud includes multiple layers of backup and recovery mechanisms designed to ensure that customer data can be restored when necessary.



These mechanisms operate at both the **site level** and the **server level**, allowing recovery in a wide range of operational scenarios.



---



## Automated Site Backups

Frappe Cloud automatically generates backups for sites hosted on the platform.



These backups typically include:



- Database data 
- Public files 
- Private files 
- Application configuration





Backups are generated periodically and stored securely so that they can be restored when required.



Customers can access their backups through the Frappe Cloud dashboard and download them if needed.



---



## Server Snapshots

In addition to application-level backups, Frappe Cloud also supports **server snapshots**.



A server snapshot is a time-based copy of a server’s disk state that can be used to recreate the server environment or recover data at a later time. 



Snapshots capture the complete disk state of the server, including:



- Operating system 
- Application environment 
- Databases 
- Files





This provides a powerful disaster recovery mechanism when infrastructure-level recovery is required.



---



## Automated Snapshot Policy

Frappe Cloud automatically generates server snapshots periodically.



These automated snapshots are taken every **24 hours and 48 hours**, and are retained temporarily for recovery purposes. 



Customers can also create **manual snapshots** at any time through the dashboard.



Manual snapshots may be retained for longer durations and used for purposes such as:



- Major upgrades 
- Infrastructure changes 
- Migration safety points 
- Disaster recovery planning





---



## Snapshot Recovery

When recovering from a snapshot:



- Temporary servers may be created from the snapshot 
- Backup files for selected sites can be generated 
- Customers can download database and file backups





Recovery operations do not automatically overwrite existing sites. Instead, they generate recovery backups that can be restored safely.



This approach reduces the risk of accidental data loss during recovery operations.



---



## Consistent vs Inconsistent Snapshots

Frappe Cloud supports two snapshot modes.



**Consistent snapshots** temporarily stop database and container services before capturing the disk image. This ensures reliable recovery but may introduce a short service interruption of a few minutes.



**Inconsistent snapshots** capture the disk state without stopping services. This avoids downtime but may require additional steps during recovery.



Both options allow customers to balance uptime requirements with recovery reliability.



---



## Disaster Recovery Philosophy

The disaster recovery strategy of Frappe Cloud is based on three principles:



1. **Multiple backup layers** (site backups and server snapshots)
2. **Offsite storage** for backup durability
3. **User-accessible recovery tools**

These mechanisms ensure that recovery can occur even in scenarios involving:



- Accidental deletion 
- Software corruption 
- Infrastructure failure





---

<!-- page: customer-guide/customer-guide__security__compliance-repository.md -->
---
title: "Compliance Repository"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/compliance-repository"
updated: "2026-07-02"
---


| Document                     | Description                                                                                   | Link                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Information security policy  |                                                                                               | [https://drive.google.com/file/d/1eEU_f7gMX6iFwqe_yd_022n23VrNhsMd/view](https://drive.google.com/file/d/1eEU_f7gMX6iFwqe_yd_022n23VrNhsMd/view) |
| Backup policy                |                                                                                               | [https://drive.google.com/file/d/1LGBAas8-YvS_guqVahN4g3UKbV3ydOm-/view](https://drive.google.com/file/d/1LGBAas8-YvS_guqVahN4g3UKbV3ydOm-/view) |
| VA/PT report                 | for infra with the findings along with the revalidated report where findings have been closed |                                                                                                                                                  |
| Application Security report  | with the findings along with the revalidated report where findings have been closed           |                                                                                                                                                  |
| Network Architecture diagram | Please check with Shadrak                                                                     |                                                                                                                                                  |
| DR and BCP policy            |                                                                                               | [https://drive.google.com/file/d/1bcnlwRc9T3rpTcpATz4mtVJRlaN38Ly3/view](https://drive.google.com/file/d/1bcnlwRc9T3rpTcpATz4mtVJRlaN38Ly3/view) |
| Incident Response Plan       |                                                                                               |                                                                                                                                                  |
| User acceptance Policy       | Not Available                                                                                 | Not Available                                                                                                                                    |

<!-- page: customer-guide/customer-guide__security__data-ownership.md -->
---
title: "Who owns the data?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/data-ownership"
updated: "2026-07-02"
---

When businesses trust Frappe with their data, they typically have 4 questions: 

1. Who owns my data?
2. Who else has access to my data?
3. Will my data be used for any other purposes (apart from for my application instance)?
4. Does Frappe have to access my data?

Note that the first two questions are often just inquisitions, but sometimes also from a compliance point of view (e.g. for GDPR). This doc aims to address both intents. 

---

# Data Owners

The question “Who owns my data?” is relevant when Frappe apps are hosted on Frappe Cloud. **On Frappe Cloud, customers retain full ownership of their data at all times.** The data is stored inside Frappe Cloud sites. That includes the site’s database, uploaded files, application data, and the site’s config. All of this belongs to the customer organisation that created the site.



From a legal perspective, **Frappe Cloud acts as a hosting and platform provider, not the owner or controller of the business data stored on the platform**. Here, customer data refers to the electronic data and information submitted by the customer to the services, including information stored in the database of the site instance. 



TL;DR - Frappe’s role is limited to providing the infrastructure, platform tooling, and operational services required to run and maintain the hosting environment. Data is owned by users who own the sites. 



> **Frappe is GDPR compliant** and adheres to other regional data protection laws such as DPDPA. Please refer to the Compliance Repository for more details.  

---

# Sub-processors & Role of Infrastructure Providers

Frappe Cloud relies on trusted infrastructure providers to deliver computing and storage capabilities. These **providers act as sub-processors, meaning they provide infrastructure services but do not independently process customer data**.



As of the last update of this page, Frappe Cloud offers infrastructure from the following cloud providers:

- Amazon Web Services (AWS) [https://aws.amazon.com/](https://aws.amazon.com/)
- DigitalOcean [https://www.digitalocean.com/](https://www.digitalocean.com/)
- Hetzner [https://www.hetzner.com/cloud](https://www.hetzner.com/cloud)
- Oracle Cloud Infrastructure (OCI) [https://www.oracle.com/in/cloud/](https://www.oracle.com/in/cloud/)



Additionally, Frappe uses infrastructure from the following providers for experimental and internal use: 

- Scaleway 
- 



These providers supply the physical servers, storage infrastructure, networking capabilities, and regional data centres on which Frappe Cloud runs. While these providers host the infrastructure, they do not have application-level access to customer databases or application environments. Access to customer data stored within their environments is governed solely by Frappe’s security architecture and the configurations/settings controlled by the customer (e.g. Roles & Permissions, Authorisation).

---

# Frappe’s Access to Customer Environments

The question “Does Frappe have access to my site or server?” has 2 underlying sub-questions:

1. Does Frappe have unlogged/uncontrolled/unrestricted access?
2. What level of access does Frappe have?

**Frappe does not have unrestricted access to customer data.** Frappe teams cannot directly see customer data. Nobody, for that matter, can access customer data without permission. Even Frappe engineers do not access customer data without consent. If access is required for any operational reason, such as resolving a support ticket or responding to a platform incident, Frappe engineers explicitly require consent from the customer to get access. Even after consent, the actions are logged to ensure accountability. 

Do we have a doc on this? Or maybe a screenshot?



Note that Frappe Cloud manages the underlying infrastructure. To do that effectively, **the platform may perform certain automated operations** such as creating sites and servers, running upgrades, triggering backups, and monitoring logs. These actions are performed through the orchestration layer (Press), which executes controlled commands on servers. **Access is not arbitrary or manual; instead, it occurs through automated platform workflows.** This ensures that these actions are controlled, logged and traceable (for debugging or auditing purposes). 

---

# Data Usage (Beyond Application Instance)

**Customer data stored on Frappe Cloud is not used for any secondary purposes,** such as:

- Advertising
- Data resale
- Behavioural profiling
- Marketing analytics
- Model training (for AI)



**Frappe does not analyse, mine, or commercially exploit customer data stored within customer environments.** The data remains confined to the customer's application environment and is processed only as required to provide the cloud service.



**Frappe Cloud’s telemetry systems may collect activity data** such as infrastructure metrics, logs, and performance statistics. These are used strictly for:

- System monitoring
- Debugging
- Security 
- Reliability improvements

Such **telemetry does not involve extracting or analysing the business data stored within customer databases.**

---

# Customer Responsibility for Access Control

While Frappe Cloud provides the infrastructure and platform security controls, customers remain responsible for managing access to their application data. This includes:

- Creating and managing user accounts
- Assigning roles and permissions
- Enforcing internal access policies
- Securing access credentials

All these are features of the Frappe application and/or the Frappe Framework, and are configured inside the customer’s application environment, and are thus called “Application Security” controls. This guide contains a detailed document on the topic. Find it here. 

---

# Summary

To summarise Frappe’s data ownership model:

- Customers retain full ownership of their data.
- Frappe Cloud acts as a sub-processor platform and delivers infrastructure services from select infrastructure providers.
- Infrastructure providers host the underlying hardware but do not access application data.
- Data is not used for advertising, resale, or analytics outside service delivery.
- Platform operations are controlled through orchestration systems rather than uncontrolled administrative access.



This separation of ownership, control, and infrastructure responsibilities ensures that customers maintain authority over their data while benefiting from a managed cloud environment.

<!-- page: customer-guide/customer-guide__security__data-residency.md -->
---
title: "Where does the data reside?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/data-residency"
updated: "2026-06-22"
---

Data Residency means the geographic location where customer data is physically stored. Organisations need to comply with regulatory and contractual mandates that restrict where their data may reside. This doc clears the air around 3 most commonly asked questions around the topic: 

1. Where does Frappe store user data - Regular and Backup?
2. Where can users access data from?
3. How does Frappe help in complying with data residency compliance?

---

# Application Data Residency

Frappe Cloud is a multi-cloud hosting platform. It allows users to deploy applications across the globe through multiple infrastructure providers (viz. AWS, DigitalOcean, Hetzner, Oracle Cloud), allowing customers to select the geographic region where their servers and application environments are hosted. As of the last update of this page, Frappe Cloud has clusters (i.e. data centres where servers are rented) across Asia, Europe, the Middle East, Africa and North America. 



When a server or site is created on Frappe Cloud, the region selected during deployment determines the physical data location. Note that the availability of locations depends on the infrastructure provider selected and the server type being deployed. By selecting a region during deployment, customers ensure that their databases, files, and application environments are stored within the selected geographic region. 



Refer to the table below for the locations of Frappe Cloud clusters (by provider). 


| Amazon Web Services                                                                                                                                                                                  | DigitalOcean                    | Hetzner                                               | Oracle Cloud (OCI)                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| Mumbai, IndiaLondon, UKFrankfurt, GermanyN. Virginia, USAZurich, SwitzerlandBahrain, Middle EastSingapore, AsiaCape Town, S. AfricaJakarta, IndonesiaUnited Arab EmiratesSydney, Australia | Singapore, AsiaToronto, Canada | Ashburn, USAFalkeinstein, GermanyNuremberg, Germany | Jeddah, Saudi ArabiaJohannesburg, S. Africa |


---

## Data Residency vs Data Access

It is important to distinguish between **data residency** and **data access**.

Data residency determines where the data is stored physically. However, authorized users may access that data from other locations via secure internet connections.

For example:

- A server hosted in Frankfurt may be accessed by users in India. 
- A site hosted in Mumbai may be accessed by teams globally.

Access is controlled through authentication and encrypted network connections rather than geographic restrictions.

---

## Compliance Considerations

Many regulatory frameworks require organizations to ensure that certain types of data remain within specific jurisdictions. Examples include:

- Financial sector regulations 
- Healthcare data protection laws 
- Government or public sector compliance frameworks 
- Regional data protection regulations such as GDPR

By selecting appropriate regions during deployment, organizations can align their infrastructure with these regulatory requirements.

---

## Backup Residency

Backups created by the platform follow the same regional infrastructure architecture. This ensures that backup data is stored within the same infrastructure ecosystem used by the deployed server or site.

Offsite storage is used to ensure durability and disaster recovery, while still maintaining the regional architecture of the infrastructure provider.

---



---

<!-- page: customer-guide/customer-guide__security__encryption-key-management.md -->
---
title: "Is the data encrypted?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/encryption-key-management"
updated: "2026-07-02"
---

---

## =Encryption in transit

Here is a fact list:

- All customer traffic inside Frappe Cloud is encrypted in transit using **HTTPS** with **TLS 1.3**. 
- Encryption strength includes **AES-256**. 
- Certificates are issued and renewed automatically via **Let’s Encrypt**, which is a free, automated, and open Certificate Authority (CA) run by the Internet Security Research Group (ISRG). It enables users to obtain, renew, and manage TLS/SSL certificates at no cost. 
- **Wildcard certificates** are supported. That means all subdomains (i.e. sites made on Frappe Cloud) under [frappe.io](https://frappe.io) and [frappe.cloud](https://frappe.cloud) (which is the default domain of Frappe Cloud) are already certified. For custom domains, certificates still need to be obtained. Do we facilitate, or is the user supposed to get? 
- **Communication between the application server and the database server** is also secured via TLS.



In a nutshell, Frappe Cloud ensures that data travelling across networks, whether between user and server or between internal components, remains encrypted and therefore protected against interception.





---

## Encryption at rest

Currently, database encryption at rest is **not enabled by default.** Note that:

- File storage is maintained in an as-is format. 
- Backups are not encrypted by default. 
- However, **Passwords are encrypted.**



There are some enterprise deployments that require encryption at rest. Such requests **can be catered to on demand**. 



Having said that, there are a few mechanisms in place to secure data at rest:

- Data storage utilises **secure object storage services** (e.g., S3-compatible systems). 
- Access to storage is controlled through **infrastructure policies**.

Anything else?



---

Encryption is a foundational control in modern cloud platforms. It ensures that even if data is intercepted, accessed improperly, or stored on shared infrastructure, it cannot be read without the appropriate cryptographic keys.



Frappe Cloud uses encryption mechanisms to protect data in two primary contexts:



- **Data in transit** - information moving between users and the platform 
- **Data at rest** - information stored on servers, databases, or backup systems





These mechanisms help ensure that customer data remains confidential and protected throughout its lifecycle.



---



## Encryption in Transit

All communication between users and Frappe Cloud services occurs over encrypted HTTPS connections.



Transport Layer Security (TLS) is used to protect data transmitted between:



- Web browsers and Frappe Cloud sites 
- APIs and application services 
- External integrations interacting with hosted applications





TLS encryption prevents attackers from intercepting or modifying traffic between users and the application environment.



This protection is particularly important when users access systems over public networks such as the internet.



---



## Encryption at Rest

Customer data stored within Frappe Cloud environments is protected through storage-level encryption mechanisms provided by the underlying infrastructure providers.



These protections apply to:



- Database storage volumes 
- File storage systems 
- Backup storage 
- Snapshot storage





Infrastructure providers such as AWS, OCI, and Hetzner implement encryption capabilities that protect stored data from unauthorized access at the storage layer.



These protections ensure that raw storage volumes cannot be read without proper authorization.



---



## Backup Encryption

Backup systems are an essential component of data protection. However, they also represent a potential risk if not secured properly.



Backups stored by the platform are protected using the storage security mechanisms provided by the infrastructure provider.



These backups may include:



- Database backups 
- File backups 
- Server snapshots 
- Recovery archives





Because backups may be stored offsite for durability and disaster recovery purposes, encryption ensures that these copies remain protected even when stored outside the active application environment.



---



## Encryption Keys

Encryption relies on cryptographic keys that allow systems to encrypt and decrypt protected data.



For infrastructure-level encryption, key management is handled by the underlying infrastructure providers through secure key management systems.



These systems enforce strict access policies for cryptographic keys and protect them using hardened infrastructure designed specifically for secure key storage.



By leveraging the key management capabilities of the underlying cloud providers, Frappe Cloud benefits from mature and highly secure key protection mechanisms.



---



## Application-Level Security

In addition to infrastructure-level encryption, application-level controls within Frappe applications help protect sensitive information.



These controls include:



- Role-based access restrictions 
- Permission-based access to documents 
- Authentication protections such as two-factor authentication 
- Secure session management





These mechanisms ensure that sensitive information remains accessible only to authorized users within the application.



---



## Encryption as Part of a Layered Security Model

Encryption alone cannot guarantee security. Instead, it functions as one layer within a broader defense-in-depth architecture.



Within Frappe Cloud, encryption works alongside:



- Network security controls 
- Access control systems 
- Infrastructure isolation 
- Monitoring and auditing mechanisms





Together, these layers ensure that sensitive information remains protected across multiple stages of the system architecture.



---

<!-- page: customer-guide/customer-guide__security__incident-response.md -->
---
title: "What is the Incident Response?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/incident-response"
updated: "2026-06-22"
---

## Security Incidents and Operational Events

Even the most secure systems must prepare for the possibility of incidents.



A security incident may include:



- Unauthorized access attempts 
- Exploitation of vulnerabilities 
- Infrastructure outages 
- Data integrity issues 
- Service disruptions





Incident response refers to the structured process used to detect, investigate, and resolve such events.



---



## Incident Classification

Issues reported on Frappe Cloud are categorized based on severity and impact.



Examples include:



- **Critical incidents** – systems unavailable or major outages 
- **Vulnerabilities** – security issues that may expose customer data 
- **Bugs** – incorrect behavior of specific features 
- **Functional queries** – configuration or operational questions





These categories determine how quickly incidents are investigated and resolved.



---



## Response and Resolution Targets

Response and resolution timelines are defined in the Frappe Cloud support policy.



For critical incidents:



- Initial response time may be as low as **30 minutes** 
- Resolution targets depend on issue severity and complexity





Security vulnerabilities are also treated with priority and are investigated within defined response windows. 



These targets apply during defined support hours and may vary depending on plan level.



---



## Incident Reporting

Customers report incidents through the **Frappe Cloud Support Portal** by creating a support ticket.



If necessary, escalation paths are available to reach senior engineering leadership.



Support escalation channels include:



- Frappe Cloud support team 
- Platform engineering leadership 
- Executive escalation paths





These escalation channels ensure that serious incidents receive appropriate attention.



---



## Incident Investigation

Once an incident is reported or detected, the engineering team performs a structured investigation.



Typical steps include:



1. **Detection** – identifying abnormal system behavior
2. **Containment** – limiting potential impact
3. **Investigation** – analyzing logs, metrics, and infrastructure events
4. **Remediation** – resolving the underlying issue
5. **Recovery** – restoring normal operations

Operational logs, monitoring tools, and infrastructure telemetry assist in diagnosing issues.



---



## Monitoring and Detection

Frappe Cloud operates infrastructure monitoring systems that track:



- System health 
- Resource usage 
- Application errors 
- Deployment activity 
- Network anomalies





Alerts generated by these systems help identify issues early and trigger investigation.



---



## Customer Communication

During major incidents, customers may receive:



- Updates through support tickets 
- Incident notifications 
- Resolution updates once the issue is resolved





Clear communication helps ensure that customers understand the nature of the incident and the steps taken to resolve it.



---



## Continuous Improvement

After significant incidents, the engineering team performs internal reviews to identify:



- Root causes 
- Preventive measures 
- Infrastructure improvements 
- Process changes





These reviews help strengthen the reliability and security posture of the platform over time.

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
