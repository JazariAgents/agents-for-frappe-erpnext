<!-- Frappe documentation: lending, part 3 of 3. Index: docs/INDEX.md -->

<!-- page: lending/lending__loan-write-off.md -->
---
title: "Loan Write Off"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-write-off"
updated: "2026-05-31"
---

A **loan write-off** refers to the process by which a lender formally acknowledges that a loan is unlikely to be repaid and removes it from its balance sheet as an asset. This is an accounting action that reflects the lender's recognition of the loss associated with the uncollectible loan. However, writing off a loan does not mean that the borrower is absolved of the debt; the borrower is still legally obligated to repay the loan, and the lender may continue to attempt to recover the funds through various means.

To access the Loan Write Off, go to:

> **Home > Lending > Loan Adjustments > Loan Write Off**

**2. How to create a Loan Write Off**
-------------------------------------

1. Go to the Loan Write Off List, and click on Add Loan Write Off.
2. Enter the loan account and the principal amount to be written off.
3. Save and submit.

On submitting the Loan Write Off entry the loan is marked as written off and the accounting entries are posted as below.

[Screenshot on the live page]


### Write-off amount validation

Loan Write Off validates that the write-off amount matches the pending principal amount for the loan at that point in time. This prevents partial or excess principal write-off through this document flow.

### Settlement write-off vs regular write-off

- **Regular write-off** is used when the loan is moved into written-off state as part of delinquency/write-off processing.
- **Settlement write-off** is used in settlement-oriented scenarios where write-off is created as part of closure/settlement flow.

Both flows update written-off totals and status handling, but settlement behavior is controlled separately through settlement flags and repayment status transitions.

### Auto write-off trigger scenario

System can auto-create loan write-off when DPD crosses the Company-level threshold (**Days Past Due Threshold For Auto Write Off**) during classification processing.

### Auto waivers

Write-off flow can automatically create waiver entries with internal write-off waiver marking for pending components such as:

- Interest Waiver
- Penalty Waiver
- Charges Waiver

This helps clean up non-principal pending components while moving principal to write-off.

### Recovery after write-off

Write-off does not end recovery. Repayments can still be collected through write-off recovery flows such as:

- **Write Off Recovery**
- **Write Off Settlement**

These repayment types use dedicated write-off recovery accounting paths and help track post write-off collections.

<!-- page: lending/lending__loan.md -->
---
title: "Loan Booking"
space: "Lending"
url: "https://docs.frappe.io/lending/loan"
updated: "2026-01-06"
---

[Screenshot on the live page: Loan Cycle]  


**Loan booking refers to the process of officially recording a loan in the financial institution's system after it has been approved and the terms have been finalized. This is a critical step in the loan lifecycle, as it marks the point at which the loan becomes an active obligation for both the lender and the borrower.**

To access the Loan, go to:


> **Home > Lending > Loan > Loan**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Product, it is advised to create the following:

* Applicant (Customer, Employee, or a Member)
* Company
* Loan Product

**2. How to create a Loan**
---------------------------

1. Go to the Loan List, and click on Add Loan.
2. Enter the loan details like loan product, applicant, tenure, posting date, etc.
3. Save

3. Repayment Frequencies
----------------------------------------

Irrespective of the repayment schedule type users can select a frequency like Monthly, Weekly, Bi-weekly, Quarterly, One Time as per their requirement. Based on this frequency the repayment schedule will be generated.

[Screenshot on the live page]  


4. Adding moratorium during loan booking
----------------------------------------

A **moratorium** in a loan context refers to a temporary suspension or postponement of loan repayments for a specified period of time, during which the borrower is not required to make any payments towards the loan principal or interest. The moratorium period is usually granted during times of financial hardship, economic downturns, or in special circumstances such as the COVID-19 pandemic. It allows borrowers relief from financial stress, giving them time to stabilize their finances before resuming regular loan payments.

To add a moratorium, the user can mention the Moratorium Tenure and moratorium type at the loan booking stage

[Screenshot on the live page]  


There are two moratorium types available, if EMI is selected, both interest and principal are not applicable and if the Principal is selected the only interest is payable, and the principal component is not applicable.

5. Revolving limits for Line Of Credit loans
--------------------------------------------

**Revolving limits** in **line of credit loans** refer to the maximum amount of credit that a borrower can access and use on a recurring basis. A **line of credit (LOC)** is a flexible loan option that allows borrowers to draw funds as needed, up to a specified credit limit, repay the borrowed amount, and then access the credit again without having to apply for a new loan. This process is known as revolving credit because the credit becomes available again as the borrower repays it, up to the original limit.

[Screenshot on the live page]  


6. Loan Account Freezing (Death Marking)
----------------------------------------

If the borrower dies or is unable to make the repayments due to any circumstances the loan account can be frozen. Upon freezing the accounts the loan interest accrual and demand generation stops.

[Screenshot on the live page: Freeze Loan Account]  

<!-- page: lending/lending__masters.md -->
---
title: "Masters"
space: "Lending"
url: "https://docs.frappe.io/lending/masters"
updated: "2026-01-06"
---


# Applicant (Customer/Borrower)

Endpoint: POST /api/resource/Customer

Request Body
```
{
  "customer_name": "New Ventures LLC",
  "customer_type": "Company",
  "email_id": "info@newventures.co"
}
```

Response
```
{
  "data": {
    "name": "CUST-00003",
    "customer_name": "New Ventures LLC",
    "customer_type": "Company",
    "email_id": "info@newventures.co",
    "owner": "test@example.com",
    "creation": "2025-09-22 10:00:00.000000",
    "modified": "2025-09-22 10:00:00.000000"
  }
}

```

# Charges (Items)

Endpoint: POST /api/resource/Item

Request Body
```
{
  "item_code": "DOC-FEE-01",
  "item_name": "Documentation Charge",
  "item_group": "Service",
  "is_stock_item": 0,
  "is_service_item": 1,
  "stock_uom": "Nos",
  "rate": 500
}

```

Response
```
{
  "data": {
    "name": "ITEM-00004",
    "item_code": "DOC-FEE-01",
    "item_name": "Documentation Charge",
    "item_group": "Service",
    "is_stock_item": 0,
    "is_service_item": 1,
    "stock_uom": "Nos",
    "rate": 500,
    "owner": "test@example.com",
    "creation": "2025-09-22 13:00:00.000000",
    "modified": "2025-09-22 13:00:00.000000"
  }
}
```
# Loan Category

Endpoint: POST /api/resource/Loan Category

Request Body
```
{
    "loan_category_code": "LAP",
    "loan_category_name": "Loan Against Property",
}
```

Response
```
{
  "data": {
    "name": "LAP",
    "loan_category_code": "LAP",
    "loan_category_name": "Loan Against Property",
    "owner": "test@example.com",
    "creation": "2025-09-22 17:00:00.000000",
    "modified": "2025-09-22 17:00:00.000000"
  }
}
```

# Loan Product

Endpoint: POST /api/resource/Loan Product

Request Body
```
{
    "product_name": "Personal Loan",
    "product_code": "LN-PROD-00004",
    "rate_of_interest": 8.5,
    "repayment_schedule_type": "Monthly as per cycle date",
    "maximum_loan_amount": 50000,
    "is_term_loan": 1,
    "min_days_bw_disbursement_first_repayment": 15
}

```

Response
```
{
  "data": {
    "name": "LN-PROD-00005",
    "product_name": "Personal Loan",
    "product_code": "LN-PROD-00004",
    "rate_of_interest": 8.5,
    "repayment_schedule_type": "Monthly as per cycle date",
    "maximum_loan_amount": 50000,
    "is_term_loan": 1,
    "min_days_bw_disbursement_first_repayment": 15,
    "owner": "test@example.com",
    "creation": "2025-09-22 15:00:00.000000",
    "modified": "2025-09-22 15:00:00.000000"
  }
}
```

<!-- page: lending/lending__npa-classification.md -->
---
title: "NPA Classification"
space: "Lending"
url: "https://docs.frappe.io/lending/npa-classification"
updated: "2026-06-05"
---

**NPA (Non-Performing Asset) classification** in loans refers to the categorization of loans that are overdue for a specified period and are no longer generating income. In simple terms, when a borrower fails to make principal or interest payments for an extended period, the loan is classified as an NPA by the lender. NPA classification helps financial institutions monitor the quality of their loan portfolios and ensure they take necessary actions to manage risks.

Frappe Lending has out-of-the-box NPA classification processes that help users manage NPA loans efficiently.

## 1. Days Past Due update

Loan Classification process runs every day and updates the count of Days Past Due (DPD) for each active loan. This count is also updated in near real-time when repayment and related loan events are processed.

[Screenshot on the live page]

Users can also track historical day-wise DPD data in **Days Past Due Logs**.

[Screenshot on the live page]

## 2. NPA Marking

NPA marking is based on DPD crossing configured threshold values.

Important correction:

- The threshold used for NPA marking is primarily taken from **Loan Product** (`Days Past Due Threshold for NPA`).
- Company-level DPD threshold is used for **auto write-off trigger**, not as the primary NPA marking threshold.

When DPD crosses the configured NPA limit, loan is auto-marked as NPA.

[Screenshot on the live page]

This threshold is evaluated based on the oldest overdue EMI demand path used in classification processing.

[Screenshot on the live page]

## 3. Manual NPA marking and unmarking

There are cases when users need to override system behavior and manually mark or unmark loan as NPA.

- **Manual NPA Marking** allows user override even if normal threshold conditions are not currently met.
- **Manual Unmark NPA** allows user-driven reversal, but system applies guardrails in specific scenarios.

Once manual override is used, system behavior follows override flags until user changes those flags again.

## 4. Additional Details

### Watch period after restructure

If a normal restructure is approved and the loan enters NPA context, system sets a watch period end date using company setting **Watch Period Post Loan Restructure (In Days)**.

During watch period:

- NPA-linked classification handling uses watch-period-aware behavior.
- Manual unmark operations are restricted before watch period end date.

### Linked customer/loan NPA propagation

NPA status updates propagate through linked active loans of the same applicant context, with logging through NPA log records and DPD logs.

### Freeze-account impact on DPD/NPA

If loan is frozen, classification and DPD processing apply freeze-aware boundaries, including demand/accrual reversals and DPD recomputation behavior for freeze transitions.

### Line of Credit behavior

For line-of-credit loans, DPD is tracked at disbursement level and aggregated to loan-level max DPD for overall status handling.

### Auto write-off trigger link

When DPD crosses Company-level **Days Past Due Threshold For Auto Write Off**, system can auto-initiate loan write-off creation in classification flow.

<!-- page: lending/lending__past-cashflow-report.md -->
---
title: "Past Cashflow Report"
space: "Lending"
url: "https://docs.frappe.io/lending/past-cashflow-report"
updated: "2026-01-06"
---

The **Past Cashflow Report** helps track all repayments made by a borrower on or before a selected date. It shows details of each loan, including the applicant name, loan product, and the amounts paid toward principal, interest, additional interest, charges, penalties, and any excess payments. This report is useful for reviewing past repayment history and understanding how much has already been collected from borrowers.


[Screenshot on the live page]

<!-- page: lending/lending__process-loan-classification.md -->
---
title: "Process Loan Classification"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-classification"
updated: "2026-01-06"
---

The loan classification process is a daily process that is used to classify the loans for credit bureau reporting. This one single process updates multiple parameters of a loan like days past due, marking or unmarking the loan as NPA, and updating the classification codes. Users can also run this process manually to do an ad-hoc classification.

[Screenshot on the live page: Process Loan Classification]  


The classification codes and bucket can be configured in the Company master under the loan tab

[Screenshot on the live page: Loan Classification Ranges]  

<!-- page: lending/lending__process-loan-demand.md -->
---
title: "Process Loan Demand"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-demand"
updated: "2026-01-06"
---

Demands are generated by a demand generation process the doctype for which is called Process Loan Demand, even for manual creation of demands this process has to be used rather than creating the demands manually.

  


[Screenshot on the live page: Process Loan Demand]  

<!-- page: lending/lending__process-loan-interest-accrual.md -->
---
title: "Process Loan Interest Accrual"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-interest-accrual"
updated: "2026-01-06"
---

Loan interest accruals are done via a process called “Process Loan Interest Accrual”. To process the loan interest accrual manually a user has to use this doctype where they can enter a posting date up to which interest accrual has to be done. Optionally a specific loan or a loan product can also be provided

  


[Screenshot on the live page: Process Loan Interest Accrual]  

<!-- page: lending/lending__repayment-schedules.md -->
---
title: "Repayment Schedule"
space: "Lending"
url: "https://docs.frappe.io/lending/repayment-schedules"
updated: "2026-01-06"
---

**A repayment or amortization schedule is a detailed table that outlines the payment plan for a loan over its term. This schedule shows each payment's breakdown between principal (the original amount borrowed) and interest, helping borrowers understand how their loan will be paid off over time.**

In Frappe Lending while configuring Loan Products users configure Repayment Schedule types for term loans. Based on that configuration whenever a disbursement is done against a loan a repayment schedule is generated based on the disbursed amount and the type of repayment schedule

To access the Loan Repayment Schedule, go to:


> **Home > Lending > Disbbursement and Repayments > Loan Repayment Schedule**
> 
> 

No user input is needed for this. This is by default generated based on the information captured at the Loan Booking and Disbursement stage. This helps customers visualize a tentative payment schedule and helps in keeping track of the demands and interest accruals. An example of this can be seen in the below image.

[Screenshot on the live page: Repayment Schedule]  


  

<!-- page: lending/lending__suspense-accounting.md -->
---
title: "Suspense Accounting"
space: "Lending"
url: "https://docs.frappe.io/lending/suspense-accounting"
updated: "2026-01-06"
---

**Suspense accounting in lending** refers to the practice of temporarily holding or deferring the recognition of interest income or interest payments in a **suspense account** until specific conditions are met. This typically occurs when the interest on a loan becomes uncollectible, uncertain, or disputed, and the lender decides not to recognize the interest as income until the uncertainty is resolved or the payment is actually received.

Frappe Lending comes with automated suspense accounting for NPA Loans for both interest and charges.

Users have to configure the appropriate suspense accounts in the respective Loan Product.

[Screenshot on the live page: Suspense Account]  


Once the accounts are configured, as soon as the loan becomes NPA, a Journal Entry is automatically passed for the outstanding interest, penalty or charge amount and the amount is moved from regular income to suspense account.

[Screenshot on the live page]  


On receiving the payment the amount is again moved back to the regular income account.

<!-- page: lending/lending__workflow-bre.md -->
---
title: "Workflow (BRE)"
space: "Lending"
url: "https://docs.frappe.io/lending/workflow-bre"
updated: "2026-06-04"
---

The **Workflow (BRE)** feature in Lending is used to apply business rules during document transitions.

In Lending implementations, this is commonly used for journey steps such as screening, underwriting, approval, rejection, eKYC trigger, or eSign trigger.

This page focuses only on Lending-specific usage. For full setup and general concepts, refer to the references at the end.

Below is the default workflow on the Loan Lead document.

[Screenshot on the live page]

## Transition Tasks in Lending

Transition tasks are linked from the Transition Tasks field in each Workflow transition.

Task source options include:

- Webhook
- Server Script
- Custom methods defined in hooks.py using `workflow_methods`

Example hooks entry:

```python
workflow_methods = [
    {
        "name": "Your Task",
        "method": "my_app.workflow_tasks.your_task_method"
    }
]
```

Once configured, the named method appears in **Workflow Transition Tasks** and can be selected like other task types.

## Actual Example: Loan Lead Workflow

The current Loan Lead workflow in Lending uses these states:

- Incoming
- Scrubbing
- Pre-Qualification
- Pre-Qualified
- Qualified
- Rejected

Typical transitions:

- Incoming -> Scrubbing using action Run Basic Rules
- Scrubbing -> Pre-Qualification using action Run Pre-Qualification Rules
- Pre-Qualification -> Pre-Qualified using action Run Knockout Rules
- Pre-Qualified -> Qualified using action Converted to Application

## What Is Scrubbing Stage?

**Scrubbing** is the data-readiness stage before eligibility checks.

At this stage, the Loan Officer verifies that lead information is clean and complete, for example:

- Applicant name, mobile, loan product, and loan amount are present
- Date of Birth is available for Individual applicants
- Contact details are valid and usable

This ensures that **Run Pre-Qualification Rules** runs on reliable data.

## Flow Example: Scrubbing -> Pre-Qualification

### Action: Run Pre-Qualification Rules

At this transition, a Server Script can validate first-level eligibility checks such as:

- Age range (example: 21 to 65 for Individual applicants)
- Mandatory field completeness

Example Server Script (Workflow Task):

```python
errors = []

if doc.doctype != "Loan Lead":
    frappe.throw("This task is only valid for Loan Lead")

required_fields = {
    "applicant_name": "Applicant Name",
    "mobile_number": "Mobile Number",
    "loan_product": "Loan Product",
    "loan_amount": "Loan Amount",
}

for fieldname, label in required_fields.items():
    if not doc.get(fieldname):
        errors.append(f"{label} is required")

if doc.get("applicant_type") == "Individual":
    if not doc.get("date_of_birth"):
        errors.append("Date of Birth is required for Individual applicant")
    else:
        today = frappe.utils.getdate()
        dob = frappe.utils.getdate(doc.get("date_of_birth"))
        age = today.year - dob.year
        doc.age = age
        if age < 21 or age > 65:
            errors.append("Applicant age must be between 21 and 65")

if errors:
    frappe.throw("<br>".join(errors))
```

## Workflow Transition Tasks Mapping

Configure task in Workflow Transition Tasks:

**Loan Lead - Pre-Qualification Tasks**

- Task: Server Script
- Link: Pre-Qualification Validation Script
- Enabled: Yes
- Asynchronous: No

[Screenshot on the live page]

Then map in Workflow transitions:

- Scrubbing -> Pre-Qualification -> Transition Tasks = Loan Lead - Pre-Qualification Tasks

[Screenshot on the live page]

## References

- Workflow: [https://docs.frappe.io/erpnext/workflows](https://docs.frappe.io/erpnext/workflows)
- Workflow Transition Tasks: [https://docs.frappe.io/erpnext/workflow-transition-tasks](https://docs.frappe.io/erpnext/workflow-transition-tasks)
