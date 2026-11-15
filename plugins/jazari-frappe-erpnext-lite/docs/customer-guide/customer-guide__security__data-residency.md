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