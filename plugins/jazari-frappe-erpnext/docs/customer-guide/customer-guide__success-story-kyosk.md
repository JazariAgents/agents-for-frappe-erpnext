---
title: "Success Story: Kyosk"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/success-story-kyosk"
updated: "2026-06-22"
---

**Kyosk** started using ERPNext in 2021. As their scale of operations and breadth of use cases on ERPNext grew, so did the data volume and performance load on servers. By 2024, the database had grown to around 350 GB, with the General Ledger table alone holding nearly 60 million entries, summing up to more than 55 GB in size. Key financial reports (like Trial Balance, AR-AP reports, etc.) started taking longer to generate and sometimes even time out due to the sheer size of data. 



Kyosk’s IT team approached Frappe with this problem. Frappe engineers stepped in and did a deep RCA on the issue. It was revealed that the customer was working on an older version of ERPNext, which did not feature the “closing account balance” calculations that make report generation lighter (as the old version ingested the entire historical GL data before processing reports every time, leading to heavy load on compute). Even upgrading to the latest version was difficult owing to the suboptimal indexing of data and inefficiencies in running of the closing voucher tasks.



Frappe’s engineering team worked tirelessly along with a local certified implementation partner to resolve these challenges. The solution involved refactoring the closing balance and closing voucher logic, introducing optimised indexes, and tuning report queries for very large datasets. The results were dramatic! To give you an example, the Trial Balance report (which earlier took 15-20 minutes) started loading in under two minutes. 



This engagement shows how complex, high-volume environments benefit from proactive OEM involvement. With Enterprise Application Support plan in place, even seemingly intractable problems at enterprise scale can be addressed quickly and effectively, ensuring that Frappe apps continue to deliver value without forcing a costly move to proprietary ERP systems.