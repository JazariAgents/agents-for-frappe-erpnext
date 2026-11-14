---
title: "Charges"
space: "Lending"
url: "https://docs.frappe.io/lending/api-documentation/charges"
updated: "2026-08-12"
---

## **1. Levy the Charge**

The `loan` and `value_date` fields are custom fields added to Sales Invoice by the Lending app. `value_date` is the date on which the demand becomes due.

### **Endpoint**

**POST** `/api/resource/Sales Invoice`

### **Request Body**

```json
{
    "customer": "Jane Doe",
    "company": "Sanction Finance Pvt Ltd",
    "posting_date": "2026-03-05",
    "loan": "LOAN-0001",
    "value_date": "2026-03-05",
    "items": [
        {
            "item_code": "Processing Fee",
            "qty": 1,
            "rate": 1000
        }
    ],
    "docstatus": 1
}

```

### **Response**

```json
{
    "data": {
        "name": "ACC-SINV-2026-00014",
        "customer": "Jane Doe",
        "loan": "LOAN-0001",
        "value_date": "2026-03-05",
        "grand_total": 1000,
        "docstatus": 1
    }
}

```

Submitting this invoice creates a Loan Demand of `demand_type = "Charges"` and `demand_subtype = "Processing Fee"` for 1000.

---

## **2. Check the Outstanding Charge Amount**

Pass the charge codes you care about to `calculate_amounts` to get the payable amount for those charges only.

> `charges` must be sent as a **JSON array**, so this call has to be made as a POST with a `Content-Type: application/json` body. Sending it as a GET query string passes the value as plain text and the call will fail.

### **Endpoint**

**POST** `/api/method/lending.loan_management.doctype.loan_repayment.loan_repayment.calculate_amounts`

### **Request Body**

```json
{
    "against_loan": "LOAN-0001",
    "posting_date": "2026-03-10",
    "payment_type": "Charge Payment",
    "charges": ["Processing Fee"]
}

```

### **Response**

```json
{
    "message": {
        "total_charges_payable": 1000.0,
        "unpaid_demands": [
            {
                "name": "LM-DEMAND-00021",
                "loan": "LOAN-0001",
                "demand_date": "2026-03-05",
                "demand_type": "Charges",
                "demand_subtype": "Processing Fee",
                "sales_invoice": "ACC-SINV-2026-00014",
                "outstanding_amount": 1000.0
            }
        ],
        "pending_principal_amount": 100000.0,
        "interest_amount": 0.0,
        "penalty_amount": 0.0,
        "payable_amount": 0.0
    }
}

```

`unpaid_demands` gives the invoice-wise breakup, which is useful when the same charge code has been levied more than once on the loan.

---

## **3. Settle the Charge**

### **Endpoint**

**POST** `/api/resource/Loan Repayment`

### **Request Body**

```json
{
    "against_loan": "LOAN-0001",
    "value_date": "2026-03-10",
    "repayment_type": "Charge Payment",
    "amount_paid": 1000,
    "mode_of_payment": "Cash",
    "payable_charges": [
        {
            "charge_code": "Processing Fee",
            "amount": 1000
        }
    ],
    "docstatus": 1
}

```

`applicant`, `applicant_type`, `company` and `loan_product` are fetched from the loan, so they do not need to be sent.

### **Response**

```json
{
    "data": {
        "name": "LM-REP-0042",
        "against_loan": "LOAN-0001",
        "applicant": "Jane Doe",
        "repayment_type": "Charge Payment",
        "value_date": "2026-03-10 00:00:00",
        "amount_paid": 1000,
        "total_charges_paid": 1000,
        "payable_charges": [
            {
                "charge_code": "Processing Fee",
                "amount": 1000
            }
        ],
        "repayment_details": [
            {
                "loan_demand": "LM-DEMAND-00021",
                "demand_type": "Charges",
                "demand_subtype": "Processing Fee",
                "sales_invoice": "ACC-SINV-2026-00014",
                "paid_amount": 1000
            }
        ],
        "docstatus": 1
    }
}

```

The `repayment_details` table shows exactly which Loan Demand — and therefore which Sales Invoice — the payment was applied against.