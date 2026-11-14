---
title: "Charges"
space: "Lending"
url: "https://docs.frappe.io/lending/charges"
updated: "2026-01-06"
---

When you take out a loan, several charges/fees may be applied in addition to the principal and interest. These charges vary depending on the type of loan, the lender, and the jurisdiction. Common charges during a loan include.

1. **Processing Fee**: Some lenders charge a fee to cover the administrative costs of processing the loan application.
2. **Prepayment Penalty**: A fee charged if you pay off the loan early, compensating the lender for lost interest.
3. **Insurance Premiums**: Some loans, particularly mortgages, may require insurance, such as mortgage insurance, which protects the lender in case of default.
4. **Documentation Charges**: A fee for preparing the legal documents associated with the loan.

These charges can significantly impact the overall cost of the loan, so it’s important to understand them before committing to any loan agreement. In Frappe Lending you can configure charges as follows.

To access the Charges, go to:


> **Home > Lending > Taxes and Charges > Charge**
> 
> 

![](/files/Documentation Charges.png)  


**1. How to create a Charge**
-----------------------------

1. Go to the Item List, and click on Add Item.
2. Enter the charge details like item code, item name, tax details applicable if any, etc.
3. Save

**2. How to apply a charge on a Loan**
--------------------------------------

To apply any charge on a loan you'll have to create a Sales Invoice, the steps for which are as follows

1. Go to Sales Invoice List, and click on Add Sales Invoice.
2. Select the loan account on which the charge has to be applied.
3. Add the charges that have to be applied, taxes will be auto-applied if configured in the charge (item) master.
4. Save and submit the sales invoice.

Loan Demands for respective charges based on the invoice due date will be generated

