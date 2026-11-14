---
title: "Loan Booking"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/transactions/loan-booking"
updated: "2026-03-10"
---

To book or create a loan, follow the examples below.

### Based on tenure (Repay Over Number Of Periods) 

Endpoint: POST /api/resource/Loan

Request Body

```
{
    "applicant_type": "Customer",
    "applicant": "_Test Loan Customer 2",
    "company": "_Test Company",
    "posting_date": "2024-04-01",
    "docstatus": 1,
    "auto_create_disbursement_on_loan_booking": 1,
    "loan_product": "Term Loan Product 4",
    "loan_amount": 500000,
    "penalty_charges_rate": 25,
    "repayment_start_date": "2024-05-05",
    "repayment_frequency": "Monthly",
    "repayment_method": "Repay Fixed Amount per Period",
    "repayment_periods": 12,
    "loan_charges": [
        {
            "charge": "Processing Fee",
            "amount": 100,
            "treatment_of_charge": "Add to first repayment",
            "doctype": "Loan Disbursement Charge"
        }
    ]
}
```

Response

```
{
    "data": {
        "name": "ACC-LOAN-2026-00232",
        "owner": "test4@example.com",
        "creation": "2026-03-10 08:47:19.534436",
        "modified": "2026-03-10 08:47:19.573803",
        "modified_by": "test4@example.com",
        "docstatus": 1,
        "idx": 0,
        "applicant_type": "Customer",
        "applicant": "_Test Loan Customer 2",
        "company": "_Test Company",
        "posting_date": "2024-04-01",
        "status": "Sanctioned",
        "is_imported": 0,
        "auto_create_disbursement_on_loan_booking": 1,
        "loan_product": "Term Loan Product 4",
        "loan_amount": 500000.0,
        "repayment_schedule_type": "Monthly as per cycle date",
        "rate_of_interest": 25.0,
        "penalty_charges_rate": 25.0,
        "disbursed_amount": 0.0,
        "maximum_loan_amount": 0.0,
        "is_secured_loan": 0,
        "is_term_loan": 1,
        "repayment_start_date": "2024-05-05",
        "repayment_frequency": "Monthly",
        "monthly_repayment_amount": 0.0,
        "repayment_method": "",
        "repayment_periods": 12,
        "moratorium_type": "",
        "moratorium_tenure": 0,
        "treatment_of_interest": "",
        "maximum_limit_amount": 0.0,
        "utilized_limit_amount": 0.0,
        "available_limit_amount": 0.0,
        "days_past_due": 0,
        "loan_restructure_count": 0,
        "tenure_post_restructure": 0,
        "cost_center": "Main - _TC",
        "disbursement_account": "Disbursement Account - _TC",
        "payment_account": "Payment Account - _TC",
        "loan_account": "Loan Account - _TC",
        "interest_income_account": "Interest Income Account - _TC",
        "penalty_income_account": "Penalty Income Account - _TC",
        "total_payment": 0.0,
        "total_interest_payable": 0.0,
        "total_principal_paid": 0.0,
        "total_amount_paid": 0.0,
        "is_npa": 0,
        "manual_npa": 0,
        "unmark_npa": 0,
        "freeze_account": 0,
        "fldg_triggered": 0,
        "written_off_amount": 0.0,
        "debit_adjustment_amount": 0.0,
        "credit_adjustment_amount": 0.0,
        "refund_amount": 0.0,
        "excess_amount_paid": 0.0,
        "doctype": "Loan",
        "loan_charges": [
            {
                "name": "13r97cuucg",
                "owner": "test4@example.com",
                "creation": "2026-03-10 08:47:19.534436",
                "modified": "2026-03-10 08:47:19.534436",
                "modified_by": "test4@example.com",
                "docstatus": 1,
                "idx": 1,
                "charge": "Processing Fee",
                "amount": 100.0,
                "account": "Processing Fee Income Account - _TC",
                "treatment_of_charge": "Add to first repayment",
                "parent": "ACC-LOAN-2026-00232",
                "parentfield": "loan_charges",
                "parenttype": "Loan",
                "doctype": "Loan Disbursement Charge",
                "__unsaved": 1
            }
        ],
        "loan_import_details": []
    }
}

```

### Based on the amount (Repay Fixed Amount per Period) 

Endpoint: POST /api/resource/Loan

Request Body

```
{
    "applicant_type": "Customer",
    "applicant": "_Test Loan Customer 2",
    "company": "_Test Company",
    "posting_date": "2024-04-01",
    "docstatus": 1,
    "auto_create_disbursement_on_loan_booking": 1,
    "loan_product": "Term Loan Product 4",
    "loan_amount": 500000,
    "penalty_charges_rate": 25,
    "repayment_start_date": "2024-05-05",
    "repayment_frequency": "Monthly",
    "repayment_method": "Repay Fixed Amount per Period",
    "monthly_repayment_amount": 30000,
    "loan_charges": [
        {
            "charge": "Processing Fee",
            "amount": 100,
            "treatment_of_charge": "Add to first repayment",
            "doctype": "Loan Disbursement Charge"
        }
    ]
}
```

Response

```
{
    "data": {
        "name": "ACC-LOAN-2026-00236",
        "owner": "test4@example.com",
        "creation": "2026-03-10 12:13:03.291227",
        "modified": "2026-03-10 12:13:03.326418",
        "modified_by": "test4@example.com",
        "docstatus": 1,
        "idx": 0,
        "applicant_type": "Customer",
        "applicant": "_Test Loan Customer 2",
        "company": "_Test Company",
        "posting_date": "2024-04-01",
        "status": "Sanctioned",
        "is_imported": 0,
        "auto_create_disbursement_on_loan_booking": 1,
        "loan_product": "Term Loan Product 4",
        "loan_amount": 500000.0,
        "repayment_schedule_type": "Monthly as per cycle date",
        "rate_of_interest": 25.0,
        "penalty_charges_rate": 25.0,
        "disbursed_amount": 0.0,
        "maximum_loan_amount": 0.0,
        "is_secured_loan": 0,
        "is_term_loan": 1,
        "repayment_start_date": "2024-05-05",
        "repayment_frequency": "Monthly",
        "monthly_repayment_amount": 30000.0,
        "repayment_method": "Repay Fixed Amount per Period",
        "repayment_periods": 0,
        "moratorium_type": "",
        "moratorium_tenure": 0,
        "treatment_of_interest": "",
        "maximum_limit_amount": 0.0,
        "utilized_limit_amount": 0.0,
        "available_limit_amount": 0.0,
        "days_past_due": 0,
        "loan_restructure_count": 0,
        "tenure_post_restructure": 0,
        "cost_center": "Main - _TC",
        "disbursement_account": "Disbursement Account - _TC",
        "payment_account": "Payment Account - _TC",
        "loan_account": "Loan Account - _TC",
        "interest_income_account": "Interest Income Account - _TC",
        "penalty_income_account": "Penalty Income Account - _TC",
        "total_payment": 0.0,
        "total_interest_payable": 0.0,
        "total_principal_paid": 0.0,
        "total_amount_paid": 0.0,
        "is_npa": 0,
        "manual_npa": 0,
        "unmark_npa": 0,
        "freeze_account": 0,
        "fldg_triggered": 0,
        "written_off_amount": 0.0,
        "debit_adjustment_amount": 0.0,
        "credit_adjustment_amount": 0.0,
        "refund_amount": 0.0,
        "excess_amount_paid": 0.0,
        "doctype": "Loan",
        "loan_charges": [
            {
                "name": "pl99ban7nn",
                "owner": "test4@example.com",
                "creation": "2026-03-10 12:13:03.291227",
                "modified": "2026-03-10 12:13:03.291227",
                "modified_by": "test4@example.com",
                "docstatus": 1,
                "idx": 1,
                "charge": "Processing Fee",
                "amount": 100.0,
                "account": "Processing Fee Income Account - _TC",
                "treatment_of_charge": "Add to first repayment",
                "parent": "ACC-LOAN-2026-00236",
                "parentfield": "loan_charges",
                "parenttype": "Loan",
                "doctype": "Loan Disbursement Charge",
                "__unsaved": 1
            }
        ],
        "loan_import_details": []
    }
}
```

