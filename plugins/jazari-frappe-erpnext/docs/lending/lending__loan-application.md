---
title: "Loan Application"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-application"
updated: "2026-05-31"
---

A **Loan Application** is the formal request record used to evaluate and process a borrower’s loan request. It captures applicant details, product selection, requested amount, repayment inputs, co-applicants, supporting documents, and collateral proposal (for secured loans). This record is the foundation for credit decisioning and loan creation.

To access Loan Application, go to:

> **Home > Lending > Loan > Loan Application**

## Prerequisites

---

Before creating a Loan Application, it is advised to have:

- Company and Loan Product setup
- Applicant details (Customer or Employee)
- Loan purpose (if used by your process)
- Document checklist and co-applicant information (if applicable)
- Collateral setup and security prices (for secured loans)

### How to create a Loan Application

---

1. Go to Loan Application List and click on Add Loan Application.
2. Select Applicant Type and enter applicant details.
3. Select Company and Loan Product.
4. Enter Loan Amount and review repayment inputs.
5. For secured loans, add Proposed Pledges.
6. Add co-applicants and documents if required.
7. Save and Submit.

### Repayment details (term loans)

For term loans, repayment method can be based on either repayment periods or fixed repayment amount. The system calculates payable values and validates consistency between amount, interest, and tenure inputs.

### Secured loan details

When **Is Secured Loan** is enabled:

- Proposed pledges are required.
- Security quantity and price are used to derive value.
- Post-haircut values contribute to maximum eligible loan amount from proposed collateral.

### Applicant and duplicate handling

For customer applications, contact details can be used to identify existing borrowers. Where relevant, existing borrower information can be reused to avoid duplicate customer creation.

### Company and policy validations

Loan Application enforces key checks such as:

- Loan product must belong to the selected company.
- Loan amount must respect configured product-level limits.
- For secured loans, requested amount cannot exceed collateral-backed maximum from proposed pledges.
- If sanctioned-limit controls are maintained for the applicant, application amount is checked against the sanctioned limit context.

### From application to execution

Once approved, Loan Application supports operational progression:

- Create **Loan** from the approved application.
- Create **Loan Security Assignment** for secured applications.