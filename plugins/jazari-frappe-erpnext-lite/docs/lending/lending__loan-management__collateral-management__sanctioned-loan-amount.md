---
title: "Sanctioned Loan Amount"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/collateral-management/sanctioned-loan-amount"
updated: "2026-05-31"
---

A **Sanctioned Loan Amount** record defines the total sanctioned lending limit for an applicant in a company. This limit acts as a control point to ensure that total active/sanctioned exposure for the applicant does not exceed the approved amount.

You can create this record manually, but in some secured-lending flows it is also created/updated automatically.

### Duplicate control

Only one Sanctioned Loan Amount record is allowed per Applicant and Company combination. System blocks duplicate entries for the same pair.

### How this limit is used during loan booking

During Loan Application and Loan validation, Lending checks:

- the new loan amount being booked, and
- total existing sanctioned/disbursed outstanding context for that applicant.

If combined exposure exceeds Sanctioned Amount Limit, loan booking is blocked.

If no Sanctioned Loan Amount record exists for that applicant and company, this specific limit check is not applied.

### Is manual creation required?

It depends on your flow:

- In direct collateral assignment flows (where securities are pledged directly for an applicant), the system can auto-create the Sanctioned Loan Amount record if missing.
- In loan-application-driven secured flows, the record is typically not auto-created at the time of assignment from the application.

If you want sanctioned-limit enforcement from the start of underwriting/booking, maintain this record explicitly for the applicant-company pair.

### Automatic update behavior

Once a Sanctioned Loan Amount record exists, secured-lending events can update the sanctioned limit automatically:

- On pledge submission in direct assignment flow, limit can be created (if missing) or recalculated.
- On security release/unpledge, sanctioned limit is recalculated.
- On loan security price updates, sanctioned limits of affected applicants are recalculated.
- On shortfall processing, applicant-level sanctioned limit can be synchronized with current effective security-backed value.