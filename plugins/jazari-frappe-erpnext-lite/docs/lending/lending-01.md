<!-- Frappe documentation: lending, part 1 of 3. Index: docs/INDEX.md -->

<!-- page: lending/lending__api-documentation__charges.md -->
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

<!-- page: lending/lending__bank-account.md -->
---
title: "Bank Account"
space: "Lending"
url: "https://docs.frappe.io/lending/bank-account"
updated: "2026-01-06"
---

Non-Banking Financial Companies (NBFCs), maintain different disbursement and payment accounts that are crucial elements in managing the flow of funds for loans and other financial services.

A disbursement account in the context of NBFCs is used to manage the release of loan funds to borrowers. This account is an integral part of the loan process, where the NBFC controls the outflow of funds to ensure they are directed correctly.

A payment account in NBFCs is used to manage incoming funds, primarily loan repayments, and other payments related to financial services provided by the NBFC.

Frappe Lending allows users to map these accounts in the Bank Account master.

To access the Bank Account, go to:


> **Home > Lending > Banking > Bank Account**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Product, it is advised to create the following:

* Company
* Bank

**2. How to create a Bank Account**
-----------------------------------

1. Go to the Bank Account List, and click on Add Bank Account.
2. Enter the bank account name, select the bank, add the ledger from the chart of accounts and check "Is Company Account" and add the company.
3. Save

[Screenshot on the live page]  

<!-- page: lending/lending__borrower-portals.md -->
---
title: "Borrower Portal"
space: "Lending"
url: "https://docs.frappe.io/lending/borrower-portals"
updated: "2026-02-23"
---

TBA

<!-- page: lending/lending__branch.md -->
---
title: "Branch                                          "
space: "Lending"
url: "https://docs.frappe.io/lending/branch"
updated: "2026-01-06"
---

Branches are physical locations or offices operated by financial institutions, such as banks, credit unions, or specialized lending companies, where customers can go to apply for loans, manage their loan accounts, and receive personalized assistance with various financial services.

Frappe Lending allows users to map these branches into the system to follow branch-wise accounting

To access the Branch, go to:


> **Home > Lending > Loan Transfers> Branch**
> 
> 

**1. How to create a Branch**
-----------------------------

1. Go to the Branch List, and click on Add Branch.
2. Enter the name of the branch.
3. Save

<!-- page: lending/lending__charges.md -->
---
title: "Charges"
space: "Lending"
url: "https://docs.frappe.io/lending/charges"
updated: "2026-01-06"
---

When you take out a loan, several charges/fees may be applied in addition to the principal and interest. These charges vary depending on the type of loan, the lender, and the jurisdiction. Common charges during a loan include.

1. **Processing Fee**: Some lenders charge a fee to cover the administrative costs of processing the loan application.
2. **Prepayment Penalty**: A fee charged if you pay off the loan early, compensating the lender for lost interest.
3. **Insurance Premiums**: Some loans, particularly mortgages, may require insurance, such as mortgage insurance, which protects the lender in case of default.
4. **Documentation Charges**: A fee for preparing the legal documents associated with the loan.

These charges can significantly impact the overall cost of the loan, so it’s important to understand them before committing to any loan agreement. In Frappe Lending you can configure charges as follows.

To access the Charges, go to:


> **Home > Lending > Taxes and Charges > Charge**
> 
> 

[Screenshot on the live page]  


**1. How to create a Charge**
-----------------------------

1. Go to the Item List, and click on Add Item.
2. Enter the charge details like item code, item name, tax details applicable if any, etc.
3. Save

**2. How to apply a charge on a Loan**
--------------------------------------

To apply any charge on a loan you'll have to create a Sales Invoice, the steps for which are as follows

1. Go to Sales Invoice List, and click on Add Sales Invoice.
2. Select the loan account on which the charge has to be applied.
3. Add the charges that have to be applied, taxes will be auto-applied if configured in the charge (item) master.
4. Save and submit the sales invoice.

Loan Demands for respective charges based on the invoice due date will be generated

<!-- page: lending/lending__e-signing.md -->
---
title: "Integrations"
space: "Lending"
url: "https://docs.frappe.io/lending/e-signing"
updated: "2026-06-08"
---

# eKYC India

The **eKYC India** app provides India-focused identity verification and electronic signing integration for Frappe applications.

It supports a complete two-way integration with Digio:

- **Frappe to Digio**: Sends eKYC and eSign requests.
- **Digio to Frappe**: Receives webhook events and automatically updates request status.

This integration is designed to work with any Frappe DocType, not only loan documents.

**GitHub:** [https://github.com/frappe/ekyc_india](https://github.com/frappe/ekyc_india)

## Digio Integration

[Digio](https://www.digio.in/) is an Indian regulatory-compliant platform for Aadhaar-based identity verification (eKYC) and electronic signatures (eSign).

### Digio Documentation

| Topic                               | Link                                                                                                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Environments (Sandbox / Production) | [https://documentation.digio.in/digienvironments/](https://documentation.digio.in/digienvironments/)                                                                                             |
| eSign Webhook Events                | [https://documentation.digio.in/digisign/api_integration/webhooks/#webhook-events-for-digi-sign](https://documentation.digio.in/digisign/api_integration/webhooks/#webhook-events-for-digi-sign) |
| eKYC Webhooks                       | [https://documentation.digio.in/digistudio/integration/webhooks/](https://documentation.digio.in/digistudio/integration/webhooks/)                                                               |
| Webhooks General Reference          | [https://documentation.digio.in/webhooks/](https://documentation.digio.in/webhooks/)                                                                                                             |


---

### Setup

- Go to **Digio Settings** in the Frappe Desk to configure the integration.

**General Settings**

- Request Expiry In Days: How many days before an unanswered request expires on the Digio side.
- Generate Access Token: Returns a one-time token in the response (needed for Web SDK flows).
- Send Sign Link: Digio emails a direct signing link to the customer.
- Notify Customers: Digio sends email/SMS updates to the customer at each status change.

**Environment — Sandbox / Production**

Digio provides two environments. Use **Sandbox** for testing and **Production** for live transactions. Only one can be active at a time.

For each environment, fill in the URL and the API Client ID / Secret obtained from the Digio dashboard.

> Sandbox credentials must be requested directly from the Digio team.

[Screenshot on the live page]

**Enable e-Sign for Document**

- Document Type: The Frappe DocType to enable (e.g., Loan Application).
- Send Request: How the request is delivered to the customer — Email or Mobile.
- Request Recipient By Document Field: The field on the document that holds the customer's email or mobile number. The dropdown auto-fills with eligible fields from the selected DocType.

Example: Loan Application sent via email to the applicant:

[Screenshot on the live page]

---

### eKYC & eSign Flows

**Setting up the Workflow**

1. Create a Workflow for your DocType (e.g., Loan Application) from the Desk.
2. When adding a Transition, choose the appropriate action from the dropdown:
  - Send eKYC Request — for identity verification
  - Make eSignature Request — for electronic signing

Both actions are pre-created when the app is installed.

[Screenshot on the live page]



**How each flow works**

eKYC Flow:

- A workflow action triggers an eKYC request
- Frappe sends the request to Digio using the Aadhaar / PAN / DigiLocker template
- Customer receives an email/SMS with a verification link
- Customer completes verification on Digio-hosted page

eSign Flow:

- A workflow action triggers an eSign request
- Frappe generates a PDF of the document and sends it to Digio with signer details
- Customer receives an email with a signing link
- Customer completes Aadhaar-based electronic signing

---

### Webhooks

Digio sends status updates to Frappe automatically after each customer action. The webhook URL to register in the Digio dashboard is:

```
https://<your-frappe-site>/api/method/ekyc_india.ekyc_india.doctype.digio_settings.digio_settings.handle_webhook
```

Please follow the steps of [Webhooks General Reference](https://documentation.digio.in/webhooks)

[Screenshot on the live page]

---

### Digio Request Log

Every request sent to Digio and every webhook received is logged in **Digio Request Log**. Each log entry shows:

- The Digio request ID
- Whether it is an eSign or eKYC request
- The current status
- Which Frappe document it is linked to
- The full response from Digio and the latest webhook payload

[Screenshot on the live page]

<!-- page: lending/lending__form-builder.md -->
---
title: "Form Builder"
space: "Lending"
url: "https://docs.frappe.io/lending/form-builder"
updated: "2026-02-23"
---

Frappe framework, by default, has a [visual form builder](https://docs.frappe.io/erpnext/user/manual/en/customize-form) out of the box, which can be used to customize existing forms.

In the context of a loan origination system, users can customize the form and add their own properties. Below is a quick video of how the standard Loan Lead form can be customized

<!-- page: lending/lending__future-cashflow-report.md -->
---
title: "Future Cashflow Report"
space: "Lending"
url: "https://docs.frappe.io/lending/future-cashflow-report"
updated: "2026-01-06"
---

The **Future Cashflow Report** shows the upcoming repayment schedule for active loans as of a selected date. It lists each loan along with its disbursement, product, and the scheduled payment dates. For every repayment, the report breaks down the principal amount, interest amount, and total payment expected. This helps lenders plan and project future cash inflows from borrowers.


[Screenshot on the live page]

<!-- page: lending/lending__introduction.md -->
---
title: "Introduction to Frappe Lending"
space: "Lending"
url: "https://docs.frappe.io/lending/introduction"
updated: "2026-01-07"
---

## What is Frappe Lending?

Frappe Lending is a comprehensive Loan Management System (LMS) designed to streamline and automate the entire loan lifecycle, from loan origination to closure. Built on ERPNext and Frappe Framework, an open-source low-code platform, it provides financial institutions, NBFCs, and lenders with the tools they need to efficiently manage loans while ensuring compliance and reducing operational overhead.

[Screenshot on the live page: Frappe Lending]

## Why Frappe Lending?

1. 100% open source & API-first – Everything is open source and is end to end REST API compatible.
2. Scalable & trusted – Designed for high-volume lending.
3. Complete loan & financial management – Manage loan origination, disbursements, repayments, and accounting—all in one place.
4. Built-in compliance & risk monitoring – Automated DPD tracking, NPA classification, and regulatory reporting ensure compliance without manual effort.
5. Accounting, billing & taxation - Integrated ledgers, invoicing, and tax handling keep your financials accurate and audit-ready.
6. Custom workflows & role-based access - Define approval steps, automate processes, and control access with role-based permissions, ensuring smooth and secure operations.

## Key Features

1. Loan Booking
2. Portfolio Management
3. Collateral Management
4. Lending Models
5. Loan Accounting
6. Collection Management
7. Co-Lending

## Under the Hood

1. **ERPNext**: ERPNext is business management software that helps companies stay on top of their operations, whether it’s tracking inventory, managing finances, handling projects, or keeping customers happy.
2. **Frappe Framework**: A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

## Community

GitHub - Contribute to Frappe Lending and explore its open-source code, issues, and discussions

<!-- page: lending/lending__loan-application.md -->
---
title: "Loan Application"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-application"
updated: "2026-05-31"
---

A **Loan Application** is the formal request record used to evaluate and process a borrower’s loan request. It captures applicant details, product selection, requested amount, repayment inputs, co-applicants, supporting documents, and collateral proposal (for secured loans). This record is the foundation for credit decisioning and loan creation.

To access Loan Application, go to:

> **Home > Lending > Loan > Loan Application**

## Prerequisites

---

Before creating a Loan Application, it is advised to have:

- Company and Loan Product setup
- Applicant details (Customer or Employee)
- Loan purpose (if used by your process)
- Document checklist and co-applicant information (if applicable)
- Collateral setup and security prices (for secured loans)

### How to create a Loan Application

---

1. Go to Loan Application List and click on Add Loan Application.
2. Select Applicant Type and enter applicant details.
3. Select Company and Loan Product.
4. Enter Loan Amount and review repayment inputs.
5. For secured loans, add Proposed Pledges.
6. Add co-applicants and documents if required.
7. Save and Submit.

### Repayment details (term loans)

For term loans, repayment method can be based on either repayment periods or fixed repayment amount. The system calculates payable values and validates consistency between amount, interest, and tenure inputs.

### Secured loan details

When **Is Secured Loan** is enabled:

- Proposed pledges are required.
- Security quantity and price are used to derive value.
- Post-haircut values contribute to maximum eligible loan amount from proposed collateral.

### Applicant and duplicate handling

For customer applications, contact details can be used to identify existing borrowers. Where relevant, existing borrower information can be reused to avoid duplicate customer creation.

### Company and policy validations

Loan Application enforces key checks such as:

- Loan product must belong to the selected company.
- Loan amount must respect configured product-level limits.
- For secured loans, requested amount cannot exceed collateral-backed maximum from proposed pledges.
- If sanctioned-limit controls are maintained for the applicant, application amount is checked against the sanctioned limit context.

### From application to execution

Once approved, Loan Application supports operational progression:

- Create **Loan** from the approved application.
- Create **Loan Security Assignment** for secured applications.

<!-- page: lending/lending__loan-demand.md -->
---
title: "Loan Demand"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-demand"
updated: "2026-01-06"
---

**A loan demand, often referred to as a demand for repayment or demand notice, is a formal request made by a lender to a borrower, requiring the borrower to repay the outstanding loan balance. This is the stage when the accumulated interest and the payable principal component of the EMI becomes due.**

These loan demands are automatically generated by the system as soon as the payment date for a specific loan is reached. To create these demands manually user can run the Loan Demand Process.

[Screenshot on the live page: Loan Demand]  


Once the loan demand is generated for the interest component, the accrued amount is moved to the customer-receivable account

 [Screenshot on the live page: Loan Demand Entries]  


  


  

<!-- page: lending/lending__loan-disbursement.md -->
---
title: "Loan Disbursement"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-disbursement"
updated: "2026-01-06"
---

**Loan disbursement is the process of releasing the approved loan funds from the lender to the borrower or directly to a third party, such as a seller or service provider, depending on the type of loan. This marks the stage where the borrower can access the funds for the intended purpose, such as purchasing a home, car, or funding a business. This is also the stage where the lender starts loan accounting in his system.**

To access the Loan Disbursement, go to:


> **Home > Lending > Disbursement and Repayment> Loan Disbursement**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Disbursement, it is mandatory to create the following:

* Loan

**2. How to create a Loan Disbursement**
----------------------------------------

1. Go to the Loan Disbursement List, and click on Add Loan Disbursement.
2. Enter the loan account number and the disbursement amount.
3. Optional user can also select the bank account ledger of disbursement or else the default one from Loan Product will be used
4. Save

**3. Withholding Security Deposit**
-----------------------------------

Optionally users can withhold one EMI as a security deposit while disbursing the loan, for this all the user has to do is enable the "Withhold Security Deposit" checkbox during the disbursement.

[Screenshot on the live page: Security Deposit]  

<!-- page: lending/lending__loan-interest-accrual.md -->
---
title: "Loan Interest Accrual"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-interest-accrual"
updated: "2026-05-31"
---

In accounting, accrued interest refers to the amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out. Accrued interest can either be in the form of accrued interest revenue, for the lender, or accrued interest expense, for the borrower.

[Screenshot on the live page: Loan Interest Accrual]

In Frappe Lending, interest accrual is processed through a background job as per company accrual policy. During this process, the amount of interest accumulated between the previous interest accrual date and the process execution date is booked as income and corresponding accounting entries are posted. This amount temporarily sits in the accrued/receivable side until the demand for this amount is generated.

[Screenshot on the live page: Interest Accrual Ledger]

### Types of interest accrual

#### Normal Interest Accrual

**Normal Interest** is the standard interest charged as per the loan terms, reflecting the regular cost of borrowing.

#### Penalty Interest Accrual

**Penalty Interest** accrual is imposed on delayed repayment amounts. It is applied on overdue EMI components. In Lending, a portion related to interest component can be tracked as additional interest for internal accounting treatment.

[Screenshot on the live page]

### Additional scenarios and behavior

#### 1. Accrual is not always daily

Accrual frequency is controlled by the Company setting **Loan Accrual Frequency** (Daily, Weekly, Monthly). The scheduler checks whether the run date is an accrual day and posts accrual accordingly.

#### 2. Company day-count convention affects interest amount

Per-day and total interest are affected by **Interest Day-Count Convention** at Company level (for example Actual/365, Actual/Actual, 30/360, 30/365, Actual/360). This directly changes divisor/day treatment used in interest calculation.

#### 3. Behavior differs for term loans and non-term loans

For term loans, accrual is processed schedule-wise and aligned with repayment schedule breaks and accrual frequency breaks. For non-term loans, accrual is computed from last accrual date to posting date on pending principal.

#### 4. Penal accrual starts after grace period

Penal accrual is posted only after crossing **Grace Period in Days** configured on Loan Product. Penal rate comes from loan penalty rate when available, otherwise from Loan Product penalty rate.

#### 5. Additional Interest component in penal flow

In penal accrual processing, the system may derive and post an **Additional Interest** portion (especially interest-linked penal component) separately for accounting and demand handling.

#### 6. Line of Credit month-end scenario

For line of credit products using **No Interest Accrual Till Month End**, first normal accrual starts from the first day of the next month instead of accruing immediately from disbursement date.

#### 7. Freeze date handling

If a loan is frozen, accrual boundaries are restricted using freeze date so accrual posting does not continue beyond allowed freeze logic.

#### 8. Written-off stage accounting behavior

For written-off loans, accrual handling is more restrictive and posting behavior depends on write-off stage and related dates. This prevents incorrect income recognition after write-off cutover.

#### 9. Overlap protection for normal accruals

System validates overlapping normal-interest accrual windows and blocks duplicate overlapping accrual postings.

#### 10. Required setup check

If Loan Accrual Frequency is not configured at Company level, accrual processing throws an error and will not proceed until setup is completed.

<!-- page: lending/lending__loan-lead.md -->
---
title: "Loan Lead"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-lead"
updated: "2026-06-08"
---

A **Loan Lead** is the first-stage borrower enquiry record used before creating a formal loan application. It captures basic applicant profile, contact details, requested loan amount, product preference, and proposed tenure. This helps teams qualify incoming opportunities and prepare them for application processing.

To access Loan Lead, go to:

> **Home > Lending > Loan Origination > Loan Lead**

## Prerequisites

---

Before creating a Loan Lead, it is advised to have:

- Loan Product master
- Basic applicant contact details

### How to create a Loan Lead

---

1. Go to Loan Lead List and click on Add Loan Lead.
2. Select Applicant Type.
3. Enter Applicant Name, Email, Mobile Number, Loan Product, and Loan Amount.
4. Enter Proposed Tenure and other profile details as required.
5. Save and Submit.

### Individual vs business details

- For **Individual** applicants, Date of Birth is captured and age is derived.
- For **Business** applicants, Company Name can be captured.

[Screenshot on the live page]

### Contact and verification readiness

Loan Lead includes contact references and verification status placeholders (mobile/email verification tracking) so teams can manage lead readiness in a structured way.

### Convert to Loan Application

After the lead is qualified, it can be used to start a Loan Application with key details prefilled (applicant contact info, loan product, amount, and tenure).

<!-- page: lending/lending__loan-management__api-documentation__apply-charge.md -->
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

<!-- page: lending/lending__loan-management__api-documentation__bulk-update-loan-security-prices.md -->
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

<!-- page: lending/lending__loan-management__api-documentation__get-dues.md -->
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

<!-- page: lending/lending__loan-management__api-documentation__get-sanctioned-customer-limit.md -->
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

<!-- page: lending/lending__loan-management__api-documentation__proposed-repayment-schedule.md -->
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

<!-- page: lending/lending__loan-management__api-documentation__transactions__loan-booking.md -->
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

<!-- page: lending/lending__loan-management__automated-accounting__posting-date-and-value-date.md -->
---
title: "Posting Date and Value Date"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/automated-accounting/posting-date-and-value-date"
updated: "2026-06-05"
---

In Version 16, The **Posting Date and Value Date** concept explains how Lending keeps accounting posting separate from business transaction timing. **Posting Date** is the date on which the accounting entry is posted in the ledger, while **Value Date** is the actual transaction date used for business calculations and loan processing.

This separation is intentional in Lending and supports immutable accounting while still allowing backdated loan activity to be recorded correctly.

## How it works

In Frappe Lending, two dates are used for many transactions: **Posting Date** and **Value Date**.

This is intentional. It helps Lending keep accounting records stable while still using the correct transaction date for loan calculations.

**Posting Date** is the date used for ledger posting. In normal use, it stays as the current date so accounting entries do not disturb previously closed periods.

**Value Date** is the actual date of the transaction. It is the date Lending uses for business calculations and loan processing.

This means a user can enter a backdated loan transaction today, but the books can still post it in the current period without changing old accounting periods.

Common transactions that use this pattern include Loan Repayment, Loan Write Off, Loan Refund, Loan Disbursement, Loan Interest Accrual, Loan Demand, and related accounting entries.

## Simple Understanding

For example, if a repayment, write off, or refund is entered later than it actually happened, Lending can still use the correct transaction date for loan calculations while posting the accounting entry on the current date.

This keeps loan processing accurate and protects accounting records from being rewritten in old periods.

For Loan Disbursement, use the disbursement date.

<!-- page: lending/lending__loan-management__collateral-management__sanctioned-loan-amount.md -->
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

<!-- page: lending/lending__loan-management__collection__loan-foreclosure.md -->
---
title: "Loan Foreclosure"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/collection/loan-foreclosure"
updated: "2026-03-02"
---

There will be many scenarios where a borrower might want to foreclose the loan, before completing its actual tenure, by repaying all the applicable dues.

## **1. Creating the foreclosure payment**

Creating a foreclosure payment is the same as creating any other Loan Repayment in Frappe Lending.

For posting a foreclosure payment, select the repayment type as "Loan Closure". Post the applicable closure amount and submit the entry. If the amount is incorrect, the system will give a validation.

[Screenshot on the live page]
*Loan Closure Repayment Type*

## **2. Applying foreclosure charges**

Users can also add charges during the foreclosure payment, as shown below. While adding any charges to the foreclosure payment. Make sure to include those in the total repayment amount as well.

[Screenshot on the live page]

<!-- page: lending/lending__loan-management__lending-reports__alm-audit-report.md -->
---
title: "ALM Audit Report"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/alm-audit-report"
updated: "2026-06-03"
---

The **ALM Audit Report** provides an ageing-wise view of loan obligations as on a selected date. It shows overdue components and future scheduled amounts bucketed by ageing ranges, with principal, interest, penalty, and total values for each loan. This report is useful for asset-liability monitoring, maturity profiling, and portfolio risk review.



[Screenshot on the live page]
