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