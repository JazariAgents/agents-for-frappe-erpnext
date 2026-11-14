---
title: "Why open source?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/about-frappe/what-open-source-mean-for-you"
updated: "2026-07-21"
---

"Open source" is one of the most misunderstood phrases in business software procurement. To some buyers it signals freedom and control; to others it raises concerns about cost, support, or legal risk. Both reactions contain some truth. This page explains what open source actually means when you adopt Frappe - practically, commercially, and legally - so that every stakeholder in your evaluation is working from the same definition.



## The plain definition

Open source means **the source code of the software is publicly available, and you are licensed to use it, read it, modify it, and run it yourself**. With Frappe, the code for ERPNext, the Frappe Framework, and the other applications is developed in the open on [GitHub](https://github.com/frappe). Anyone can inspect exactly how the software works, and anyone can run it on their own infrastructure.



This is the opposite of proprietary "black box" software, where the vendor holds the code, you license the right to use it, and you cannot see, change, or independently run what you have bought.



Watch this video to know more: [What is Open Source software?](https://youtu.be/Ggymc5_pWyA?si=5zBJUn3CNfczVPzv)



## What this gives you

Three benefits matter most, and they grow more valuable with the scale and criticality of your data:

- **Cost Efficiency:** Open source software is free to use, eliminating expensive licensing fees and recurring subscription costs. This saves you money, and also allows you to use it for custom development.
- **Flexibility & Customization:** You have full access to the source code, enabling you (read, your developer team) to easily adapt and tailor the software to fit your unique business processes and workflows. 
- **Enhanced Security:** With a global community of developers and security experts continually reviewing and auditing the code, vulnerabilities are often identified and patched much faster than proprietary software.
- **No vendor lock-in.** Because the code and your data are yours to run, you are never trapped by a vendor's pricing changes, roadmap decisions, or commercial pressure. If you ever want to move - to a different hosting provider, to self-hosting, or to a different partner - the option is genuinely open to you. 
- **Rapid Innovation:** Development is crowdsourced. That means, it is not limited by the 100-odd developers employed by Frappe, but the entire community (which currently has 30,000+ developers) contribute collectively. This allows features to be built and issues to be resolved much quicker than isolated corporate teams.



#### Disclaimer: Open source does not mean everything is free

This is the single most important correction to make. Open source refers to the *licensing of the code*, not the *cost of running the software in production*. The software licence costs nothing. But operating business-critical software in production involves real, ongoing work - installation, upgrades, backups, monitoring, security patching, performance tuning, and scaling as you grow. You will either invest in doing this yourself, or pay someone to do it for you. This is precisely what Frappe Cloud and Frappe's partners provide, and it is where the genuine costs of a deployment lie. [Pricing and total cost of ownership](https://docs.frappe.io/customer-guide/pricing/total-cost-of-ownership-tco) covers this in detail.



## Why Frappe chooses this model

Frappe's open-source commitment is not a marketing posture; it is core to how the company operates and earns. Frappe describes it as part of "responsible capitalism" - the view that the value created by software is built on the contributions of many, and that sharing the source code creates a healthier ecosystem for everyone. Commercially, this works because Frappe earns not by restricting access to features but by hosting and supporting the software well, through Frappe Cloud. [Frappe's business model](https://docs.frappe.io/customer-guide/about-frappe/business-model) explains how the open-source model and the commercial model reinforce rather than contradict each other.



Here are some opinion blogs from Frappe on open-source: 

- [Free or Open Source Software?](https://frappe.io/blog/open-source/free-or-open-source-software)
- [Working in open source](https://frappe.io/blog/open-source/working-in-open-source)
- [The question with commercial open source](https://frappe.io/blog/open-source/the-question-with-commercial-open-source)
- [Giving back to open source](https://frappe.io/blog/open-source/giving-back-to-open-source)
- [Thoughts on open source communities](https://frappe.io/blog/open-source/thoughts-on-open-source-communities)
- [Charity for Free and Open Source software](https://frappe.io/blog/general/charity-for-free-and-open-source-software)
- [Open source software is safer](https://frappe.io/blog/engineering/open-source-softwares-are-safer)
- [Open source is not freemium](https://frappe.io/blog/open-source/open-source-is-not-freeium)
- [Money, power and open source](https://frappe.io/blog/culture/why-open-source)
- [Why open source?](https://frappe.io/blog/open-source/why-open-source-principles)
- [Building a self-sustaining open source business](https://frappe.io/blog/community/building-a-self-sustaining-open-source-business)



## A note on licences

You may think the intellectual property of open source projects is completely unprotected. That's not true. There are legal licenses in place. 

Different parts of the Frappe ecosystem are released under different open-source licences:

- **Frappe Framework** is licensed under the **MIT Licence** - a permissive licence. This matters if you build private or internal applications on the framework: MIT does not require you to publish your own code.
- **ERPNext** is licensed under the **GNU General Public License v3 (GPLv3)**. Its documentation is licensed under Creative Commons (CC-BY-SA 3.0). The ERPNext name and logo are trademarks of Frappe Technologies Pvt. Ltd. 
- **Newer Frappe applications** (such as CRM, Helpdesk, etc) are released under the **GNU Affero General Public License (AGPL)**.



## Frequently Asked Questions (FAQs)

**If we customise this, will we be forced to open-source our proprietary business logic?**

For the customisation that the overwhelming majority of businesses do, the answer is **No**. Configuring the system, adding custom fields, writing client and server scripts through the interface, and building pages in the no-code Builder do **not** trigger the viral clause of these licences. As Frappe's founder has put it, such customisation is like a document written in Linux, or a page published on WordPress - it does not inherit the underlying software's licence. The licence obligations are relevant primarily when you *redistribute* modified versions of the software itself. For internal use and ordinary customisation, your business logic and configuration remain yours.