---
title: "Posting Date and Value Date"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/automated-accounting/posting-date-and-value-date"
updated: "2026-06-05"
---

In Version 16, The **Posting Date and Value Date** concept explains how Lending keeps accounting posting separate from business transaction timing. **Posting Date** is the date on which the accounting entry is posted in the ledger, while **Value Date** is the actual transaction date used for business calculations and loan processing.

This separation is intentional in Lending and supports immutable accounting while still allowing backdated loan activity to be recorded correctly.

## How it works

In Frappe Lending, two dates are used for many transactions: **Posting Date** and **Value Date**.

This is intentional. It helps Lending keep accounting records stable while still using the correct transaction date for loan calculations.

**Posting Date** is the date used for ledger posting. In normal use, it stays as the current date so accounting entries do not disturb previously closed periods.

**Value Date** is the actual date of the transaction. It is the date Lending uses for business calculations and loan processing.

This means a user can enter a backdated loan transaction today, but the books can still post it in the current period without changing old accounting periods.

Common transactions that use this pattern include Loan Repayment, Loan Write Off, Loan Refund, Loan Disbursement, Loan Interest Accrual, Loan Demand, and related accounting entries.

## Simple Understanding

For example, if a repayment, write off, or refund is entered later than it actually happened, Lending can still use the correct transaction date for loan calculations while posting the accounting entry on the current date.

This keeps loan processing accurate and protects accounting records from being rewritten in old periods.

For Loan Disbursement, use the disbursement date.