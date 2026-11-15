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



