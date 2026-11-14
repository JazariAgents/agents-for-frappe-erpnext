---
title: "Proposed Repayment Schedule"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/proposed-repayment-schedule"
updated: "2026-03-12"
---

This api endpoint can be used to generate a proposed repayment schedule and present it to the borrower

Endpoint: GET /api/method/lending.api.get_repayment_schedule

Request Body

```
{
    "loan_product": "Term Loan Product 4",
    "loan_amount": 25000,
    "rate_of_interest": 12,
    "tenure": 6, // default frequency is monthly
    "repayment_frequency": "Monthly"
}
```

Response

```
{
    "message": {
        "loan_amount": 25000.0,
        "rate_of_interest": 12.0,
        "tenure": 6,
        "repayment_start_date": "2026-02-27",
        "repayment_periods": [
            {
                "payment_date": "2026-02-27",
                "principal_amount": 4314.0,
                "interest_amount": 0.0,
                "total_payment": 4314.0,
                "balance_loan_amount": 20686.0
            },
            {
                "payment_date": "2026-03-27",
                "principal_amount": 4123.58,
                "interest_amount": 190.42,
                "total_payment": 4314.0,
                "balance_loan_amount": 16562.42
            },
            {
                "payment_date": "2026-04-27",
                "principal_amount": 4145.2,
                "interest_amount": 168.8,
                "total_payment": 4314.0,
                "balance_loan_amount": 12417.22
            },
            {
                "payment_date": "2026-05-27",
                "principal_amount": 4191.53,
                "interest_amount": 122.47,
                "total_payment": 4314.0,
                "balance_loan_amount": 8225.69
            },
            {
                "payment_date": "2026-06-27",
                "principal_amount": 4230.17,
                "interest_amount": 83.83,
                "total_payment": 4314.0,
                "balance_loan_amount": 3995.52
            },
            {
                "payment_date": "2026-07-27",
                "principal_amount": 3995.52,
                "interest_amount": 39.41,
                "total_payment": 4034.93,
                "balance_loan_amount": 0.0
            }
        ]
    }
}

```

