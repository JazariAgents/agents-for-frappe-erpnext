---
title: "Get Dues"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/get-dues"
updated: "2026-03-12"
---

This API returns the dues against a specific loan on a specific date.

Endpoint: GET /api/method/lending.api.get_due_details

Request Body

```
{
    "loan": "ACC-LOAN-2026-00116",
    "as_on_date": "2026-03-01"
}
```

Response

```json
{
    "message": {
        "overdue_penalty_amount": 0.0,
        "overdue_interest_amount": 6684.69,
        "overdue_principal_amount": 100000.0,
        "principal_outstanding": 100000.0,
        "overdue_total_amount": 111684.69,
        "applicable_future_interest": 161.33,
        "unbooked_interest": 0.0,
        "applicable_future_penalty": 0,
        "oldest_due_date": "2024-12-15 00:00:00",
        "overdue_charges": 5000.0,
        "available_security_deposit": 0,
        "written_off_amount": 0.0,
        "excess_amount_paid": 0.0
    }
}
```

