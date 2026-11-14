---
title: "Get Sanctioned Customer Limit"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/get-sanctioned-customer-limit"
updated: "2026-03-12"
---

This example can be referred to get the sanctioned limit against a particular customer

Endpoint: GET /api/resource/Sanctioned Loan Amount?filters=[["applicant", "=", "Sanctioned Amount Customer - 11"]]&fields=["sanctioned_amount_limit"]

Response

```json
{
    "data": [
        {
            "sanctioned_amount_limit": 3000000.0
        }
    ]
}
```

