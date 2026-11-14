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