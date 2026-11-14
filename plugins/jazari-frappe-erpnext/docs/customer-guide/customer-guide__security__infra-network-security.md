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