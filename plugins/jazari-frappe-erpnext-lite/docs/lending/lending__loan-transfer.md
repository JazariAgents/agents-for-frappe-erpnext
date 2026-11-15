---
title: "Loan Transfer"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-transfer"
updated: "2026-01-06"
---

**A loan transfer within branches refers to the process of moving a loan from one branch of a bank or financial institution to another branch within the same organization. This can occur for various operational, logistical, or customer service reasons. The underlying terms of the loan, such as the interest rate, repayment schedule, and principal balance, typically remain unchanged during such a transfer.**

Frappe Lending allows users to transfer loans from one branch to another and move all the internal accounting as well.

To access the Loan Transfer, go to:


> **Home > Lending > Transfers> Loan Transfer**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Transfer, it is advised to create the following:

* Branch (This should also be configured as an accounting dimension as well)

**2. How to create a Loan Transfer**
------------------------------------

1. Once you are done configuring the Branch doctype as an accounting transfer you can go to the Loan Transfer list, click on Add Loan Transfer.
2. Users can optionally select an applicant if loans for only one applicant have to be transferred.
3. If any entire branch is being merged into another branch or being split from other brach users can just select the **From Branch** and **To Branch** and save the document.
4. On saving the document all the loans linked to the **From Branch** will be fetched and Journal Entries are created as per the current net balances that have to moved.
5. Once the user submits the document, the branch is updated in the loan record and the journal entry is submitted.
