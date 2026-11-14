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