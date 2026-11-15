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