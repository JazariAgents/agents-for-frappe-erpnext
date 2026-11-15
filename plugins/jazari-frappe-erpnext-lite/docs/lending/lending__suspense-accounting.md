---
title: "Suspense Accounting"
space: "Lending"
url: "https://docs.frappe.io/lending/suspense-accounting"
updated: "2026-01-06"
---

**Suspense accounting in lending** refers to the practice of temporarily holding or deferring the recognition of interest income or interest payments in a **suspense account** until specific conditions are met. This typically occurs when the interest on a loan becomes uncollectible, uncertain, or disputed, and the lender decides not to recognize the interest as income until the uncertainty is resolved or the payment is actually received.

Frappe Lending comes with automated suspense accounting for NPA Loans for both interest and charges.

Users have to configure the appropriate suspense accounts in the respective Loan Product.

![Suspense Account](/files/Suspense Account.png)  


Once the accounts are configured, as soon as the loan becomes NPA, a Journal Entry is automatically passed for the outstanding interest, penalty or charge amount and the amount is moved from regular income to suspense account.

![](/files/rOuGyGM.png)  


On receiving the payment the amount is again moved back to the regular income account.

