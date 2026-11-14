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