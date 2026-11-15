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