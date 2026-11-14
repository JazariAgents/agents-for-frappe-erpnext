---
title: "Bulk Update Loan Security Prices"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/bulk-update-loan-security-prices"
updated: "2026-03-12"
---

Using this api endpoint user can update multiple loan security prices. It is recommended to update in batches of 500 in a single request

Endpoint: PUT /api/method/lending.api.update_loan_security_price

Request Body

```
{
    "data": {
        "Test Security 1": {
            "loan_security_price": 700,
            "valid_from": "2026-03-01",
            "valid_upto": "2026-03-04"
        },
        "Test Security 2": {
            "loan_security_price": 1000,
            "valid_from": "2026-03-01",
            "valid_upto": "2026-03-04"
        }
    }
}
```

Response

```json
{
    "message": "Loan Security Prices updated successfully"
}
```

