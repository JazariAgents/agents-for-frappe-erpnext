---
title: "Apply Charge on a loan"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/api-documentation/apply-charge"
updated: "2026-03-12"
---

This API endpoint can be used to apply a single charge to a specific loan 

Endpoint: POST /api/method/lending.api.apply_charge

Request Body

```
{
    "loan": "ACC-LOAN-2026-00116",
    "charge_type": "Preclosure Charges", // Charge will be auto created if does not exists
    "based_on": "On Outstanding Principal", // Other options ["On Total Payable Amount", "Flat"]
    "percentage": 2, // Not applicable for Flat rate
    "amount": 200, // Applicable only for flat interest rate
    "charge_applicable_date": "2026-03-06" // optional parameter, add only if charge has to be applied other than the current date 
}
```

Response

```json
{
    "message": "Charge applied successfully for amount 2000.0"
}
```

