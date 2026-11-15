<!-- Frappe documentation: lending, part 1 of 1. Index: docs/INDEX.md -->

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

![](/files/qV5zp9G.png)  

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

![](/files/Documentation Charges.png)  


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

![](/files/image805ead.png)

**Enable e-Sign for Document**

- Document Type: The Frappe DocType to enable (e.g., Loan Application).
- Send Request: How the request is delivered to the customer — Email or Mobile.
- Request Recipient By Document Field: The field on the document that holds the customer's email or mobile number. The dropdown auto-fills with eligible fields from the selected DocType.

Example: Loan Application sent via email to the applicant:

![](/files/image0ec627.png)

---

### eKYC & eSign Flows

**Setting up the Workflow**

1. Create a Workflow for your DocType (e.g., Loan Application) from the Desk.
2. When adding a Transition, choose the appropriate action from the dropdown:
  - Send eKYC Request — for identity verification
  - Make eSignature Request — for electronic signing

Both actions are pre-created when the app is installed.

![](/files/imagea3cdec.png)



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

![](/files/image5715dc.png)

---

### Digio Request Log

Every request sent to Digio and every webhook received is logged in **Digio Request Log**. Each log entry shows:

- The Digio request ID
- Whether it is an eSign or eKYC request
- The current status
- Which Frappe document it is linked to
- The full response from Digio and the latest webhook payload

![](/files/image6fff0b.png)

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


![](/files/future_cashflow_report.png)

<!-- page: lending/lending__introduction.md -->
---
title: "Introduction to Frappe Lending"
space: "Lending"
url: "https://docs.frappe.io/lending/introduction"
updated: "2026-01-07"
---

## What is Frappe Lending?

Frappe Lending is a comprehensive Loan Management System (LMS) designed to streamline and automate the entire loan lifecycle, from loan origination to closure. Built on ERPNext and Frappe Framework, an open-source low-code platform, it provides financial institutions, NBFCs, and lenders with the tools they need to efficiently manage loans while ensuring compliance and reducing operational overhead.

![Frappe Lending](/files/Lending%20Dashborad.png)

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

![Loan Demand](/files/Loan Demand.png)  


Once the loan demand is generated for the interest component, the accrued amount is moved to the customer-receivable account

 ![Loan Demand Entries](/files/Loan Demand Entries.png)  


  


  

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

![Security Deposit](/files/Security Deposit.png)  

<!-- page: lending/lending__loan-interest-accrual.md -->
---
title: "Loan Interest Accrual"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-interest-accrual"
updated: "2026-05-31"
---

In accounting, accrued interest refers to the amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out. Accrued interest can either be in the form of accrued interest revenue, for the lender, or accrued interest expense, for the borrower.

![Loan Interest Accrual](/files/Loan Interest Accrual.png)

In Frappe Lending, interest accrual is processed through a background job as per company accrual policy. During this process, the amount of interest accumulated between the previous interest accrual date and the process execution date is booked as income and corresponding accounting entries are posted. This amount temporarily sits in the accrued/receivable side until the demand for this amount is generated.

![Interest Accrual Ledger](/files/Interest Accrual Ledger.png)

### Types of interest accrual

#### Normal Interest Accrual

**Normal Interest** is the standard interest charged as per the loan terms, reflecting the regular cost of borrowing.

#### Penalty Interest Accrual

**Penalty Interest** accrual is imposed on delayed repayment amounts. It is applied on overdue EMI components. In Lending, a portion related to interest component can be tracked as additional interest for internal accounting treatment.

![](/files/mdgdQXJ.png)

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

![](/files/image1bcc52.png)

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

![](/files/image7a201a.png)
*Loan Closure Repayment Type*

## **2. Applying foreclosure charges**

Users can also add charges during the foreclosure payment, as shown below. While adding any charges to the foreclosure payment. Make sure to include those in the total repayment amount as well.

![](/files/image3eceec.png)

<!-- page: lending/lending__loan-management__lending-reports__alm-audit-report.md -->
---
title: "ALM Audit Report"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/alm-audit-report"
updated: "2026-06-03"
---

The **ALM Audit Report** provides an ageing-wise view of loan obligations as on a selected date. It shows overdue components and future scheduled amounts bucketed by ageing ranges, with principal, interest, penalty, and total values for each loan. This report is useful for asset-liability monitoring, maturity profiling, and portfolio risk review.



![](/files/image37a8d9.png)

<!-- page: lending/lending__loan-management__lending-reports__applicant-wise-loan-security-exposure.md -->
---
title: "Applicant-Wise Loan Security Exposure"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/applicant-wise-loan-security-exposure"
updated: "2026-06-03"
---

The **Applicant-Wise Loan Security Exposure** report shows collateral exposure at applicant level. It lists each applicant’s pledged quantity and current value by security, along with the percentage share within that applicant’s collateral portfolio. This report is useful for borrower-level collateral analysis and for checking diversification of pledged assets.



![](/files/image390004.png)

<!-- page: lending/lending__loan-management__lending-reports__disbursement-analysis-report.md -->
---
title: "Disbursement Analysis Report"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/disbursement-analysis-report"
updated: "2026-07-13"
---

The **Disbursement Analysis Report** shows a tranche-wise view of all loan disbursements. It helps you see how a loan was paid out in parts (tranches) and what charges were taken on each payout. For each disbursement it shows the loan account, disbursement ID, applicant, tranche number, interest rate, maturity date, disbursement date and disbursed amount, along with the charge type and charge amount for any charge on that payout. You can filter the report by company, applicant, loan product, loan, or a single disbursement.

This report is used to check how a loan was paid out in parts over time, and to see the charges taken on each payout.



![](/files/imageef3a87.webp)

<!-- page: lending/lending__loan-management__lending-reports__loan-repayment-and-closure.md -->
---
title: "Loan Repayment and Closure"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/loan-repayment-and-closure"
updated: "2026-06-03"
---

The **Loan Repayment and Closure** report lists posted loan repayment transactions for a company, with loan, applicant, repayment type, overdue amount, principal paid, interest paid, penalty paid, and total payment. It helps track repayment performance and closure-related repayment entries recorded in the system. This report is useful for repayment monitoring and period-end review of loan collections.



![](/files/image1ffbf6.png)

<!-- page: lending/lending__loan-management__lending-reports__loan-security-exposure.md -->
---
title: "Loan Security Exposure"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/loan-security-exposure"
updated: "2026-06-03"
---

The **Loan Security Exposure** report shows company-level collateral concentration by security. It displays total pledged quantity, latest price, current value, portfolio share percentage, and pledged applicant count for each security. This report is useful for identifying concentration risk and understanding how much of the portfolio depends on each security type.



![](/files/image1b28d5.png)

<!-- page: lending/lending__loan-management__lending-reports__loan-security-ledger.md -->
---
title: "Loan Security Ledger"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/loan-security-ledger"
updated: "2026-06-03"
---

The **Loan Security Ledger** report shows security movement history for a loan or applicant. It lists pledge and unpledge transactions with date, security, quantity, and related loan, and can also show running balance quantity when a specific security is selected. This report is useful for tracking collateral movement and validating current pledged quantity.



![](/files/imagee33123.png)

<!-- page: lending/lending__loan-management__lending-reports__loan-security-status.md -->
---
title: "Loan Security Status"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/loan-security-status"
updated: "2026-06-03"
---

The **Loan Security Status** report shows the current and historical pledge status of assigned securities. It includes loan security assignment reference, applicant, loan, pledge status, pledge time, quantity, security price, and security value. This report is useful for operational tracking of pledged assets and for verifying security records during audits or reviews.



![](/files/image2e4b81.png)

<!-- page: lending/lending__loan-management__lending-reports__loan-statement-of-account.md -->
---
title: "Loan Statement of Account"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/lending-reports/loan-statement-of-account"
updated: "2026-06-03"
---

The **Loan Statement of Account** report gives a transaction-wise view of a borrower’s loan movement for a selected period. It combines disbursements, demands, and repayments in one timeline and shows debit, credit, and running balance for each loan. This report is useful for reviewing how a loan balance evolved over time and for reconciling borrower-level activity.



![](/files/imagea60240.png)

<!-- page: lending/lending__loan-management__setup__company-level-setup.md -->
---
title: "Company Level Setup"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/setup/company-level-setup"
updated: "2026-07-13"
---

**Company Level Setup in Frappe Lending defines default policy controls used across loan products, repayment behavior, classification logic, and accrual processing.**

To access Company Level Setup, go to:

> Home > Accounting > Company > (Open Company) > Lending tab

## Prerequisites

---

Before configuring the Company Level Setup, it is advised to have the following ready:

- Company master
- Loan Classification master records
- Loan Demand Offset Order records

### How to configure Company Level Setup

---

1. Open the Company record.
2. Go to the Lending tab.
3. Enter policy values in Loan Settings and collection configuration fields.
4. Configure Loan Classification Ranges
5. Save.

### Additional Information

#### Enable Loan Accounting

When enabled, lending transactions follow accounting-enforced flows and related entries become part of accounting-ledger-driven processing. In day-to-day operations, this setting is used to determine whether loan accounting rules should be applied for lending transactions under that company.

#### Restructure Limit % (Overall)

Defines the overall restructuring cap as a percentage. This value is used in restructure limit processing to calculate permissible restructuring exposure against outstanding position when branch-level limits are not set.

#### Enable async reversal of GL for future demand and accruals

When enabled, the reverse GL Entries created on cancellation of Loan Demands and Loan Interest Accruals are not posted immediately. Instead, the reversal is deferred to background scheduler jobs. This keeps cancellations of future demands and accruals fast by moving their GL reversal off the main transaction. It applies only to Loan Demand and Loan Interest Accrual cancellations.

#### Async GL Reversal Start Date

Defines the date from which async GL reversal takes effect. Records cancelled on or after this date use the deferred (background) reversal; records cancelled before it use immediate GL reversal. This field is mandatory when async reversal is enabled.

#### Watch Period Post Loan Restructure (In Days)

Defines the post-restructure watch-period length. This watch period is used during NPA and classification handling after approved normal restructures, and it controls when certain status transitions can happen.

#### Interest Day-Count Convention

Controls how per-day interest is computed for accrual calculations. Depending on selected convention (for example Actual/365, 30/360, Actual/Actual), the system changes the year divisor and day treatment used in interest amount calculation.

#### Minimum days between Disbursement date and first Repayment date

Provides a company-level default minimum gap between disbursement date and first repayment date. This value is inherited by Loan Product when not explicitly set there, and is used in cycle-date schedule logic to avoid too-early first installments.

#### Collection Offset Logic Based On

Defines the intended policy basis for collection offset strategy (NPA Flag or Days Past Due). In current code paths, actual demand allocation routing is driven by loan state (standard/sub-standard/written-off/settlement) and configured offset sequences; keep this field aligned with policy governance.

#### Days Past Due Threshold

Represents company-level DPD threshold used for collection policy configuration. In current implementation, NPA thresholding is primarily product-driven, so this field should be maintained as a policy-level control value and for future-ready setup consistency.

#### Days Past Due Threshold For Auto Write Off

Defines the DPD level beyond which loan write-off processing can be triggered by the automated classification flow. This is used during daily DPD evaluation and write-off initiation checks.

#### Collection Offset Sequence for Standard Asset

Default demand-allocation order for collections on standard assets. Used as fallback when Loan Product-level sequence is not set.

#### Collection Offset Sequence for Sub Standard Asset

Default demand-allocation order for sub-standard/NPA collections. Used as fallback when Loan Product-level sequence is not set.

#### Collection Offset Sequence for Written Off Asset

Default allocation order for recovery collections after write-off. Used as fallback when Loan Product-level sequence is not set.

#### Collection Offset Sequence for Settlement Collection

Default allocation order used during settlement-oriented collections (for example full/partial settlement flows). Used as fallback when Loan Product-level sequence is not set.

![](/files/imagea67f87.webp)
*Company Level Loan Setup*

#### Loan Accrual Frequency

Defines the accrual cycle at the company level (Daily, Weekly, or Monthly). Scheduler and accrual processing use this value to determine whether a date is an accrual day and how accrual breaks are generated.

#### Configuring Loan Classification Ranges

Different regulatory bodies (like RBI in India) require banks or NBFCs to classify the overdue loans as per some standard nomenclature

These ranges can be configured in the company as shown in the example below. Once these ranges are configured, the loan classification process, along with DPD, also updates the classification code and classification in the loan account as per the current DPD value

![](/files/image510dbf.png)

<!-- page: lending/lending__loan-management__tools__loan-repayment-repost.md -->
---
title: "Loan Repayment Repost"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/tools/loan-repayment-repost"
updated: "2026-07-13"
---

Loan Repayment Repost re-processes a loan's repayments from a chosen date. It cancels and re-books every repayment on or after that date, so the accruals, demands, allocations, GL Entries and classification that follow are regenerated correctly. Use it to fix a loan after a backdated change or a wrong entry, without manually cancelling and re-entering each repayment.

To access it, go to:

> Home > Loan Management > Loan Repayment Repost > New

## Prerequisites

---

- The Loan to repost
- The date from which reprocessing should start
- The specific Loan Disbursement, if only one disbursement needs reposting

### How to configure

---

1. Select the Loan, and optionally a Loan Disbursement to limit the repost to it.
2. Set the Repost Date. Every submitted repayment on or after this date is loaded into Entries To Repost.
3. Choose the reprocessing options based on what needs correcting.
4. In Entries To Cancel, list any repayments that should be cancelled outright instead of reposted.
5. Save and Submit. Short reposts run immediately; reposts older than 6 months run in the background.
6. Track progress on the Status field.

### Fields

---

- Loan: the loan to repost. Required.
- Loan Disbursement: optional; limits the repost to one disbursement.
- Repost Date: reprocessing starts here. Entries before this date are left untouched; entries on or after it are cancelled and re-booked. Required.
- Entries to Repost: auto-filled list of repayments that will be reposted.
- Entries to Cancel: repayments to cancel permanently instead of reposting.
- Cancel future EMI Demands: reverse EMI demands on or after the Repost Date before reprocessing.
- Cancel Future Accruals and Demands: reverse interest accruals and penalty demands on or after the Repost Date.
- Clear demand allocation before repost: reset affected demands to their original outstanding and clear old allocations first.
- Delete GL Entries: hard-delete old GL Entries instead of reversing them.

### How it works

---

On submit, the repost runs in two steps for the selected loan and date window:

1. Cancel — each repayment on or after the Repost Date is reversed (demands, security deposits, restructures and GL Entries rolled back). Entries listed in Entries To Cancel are cancelled outright. The loan's paid totals are recomputed from repayments before the Repost Date.
2. Re-book — the remaining repayments are reprocessed in order: demands and accruals are regenerated, amounts re-allocated, reschedules and write-offs handled, and GL Entries recreated. A closing accrual and demand run brings the loan up to date, and if the loan is now closed, its classification is refreshed.

![](/files/imagef98ce5.webp)

### Background processing

---

If the Repost Date is more than 6 months old, the repost runs as a background job and its Status is set to Queued. If it fails, the changes are rolled back, the Status returns to Draft, and a comment with the error is added so it can be retried. A repost that is already Queued or In Process cannot be submitted again.

<!-- page: lending/lending__loan-management__tools__process-loan-statement-of-accounts.md -->
---
title: "Process Loan Statement of Accounts"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-management/tools/process-loan-statement-of-accounts"
updated: "2026-07-13"
---

Process Loan Statement of Accounts generates the Loan Statement of Account report for a set of applicants (Customers or Employees) and emails it to them as a PDF, on demand or on a schedule.

To access it, go to:

> Home > Loan Management > Process Loan Statement of Accounts > New

## Prerequisites

---

- Company and Loan Product masters
- Applicants (Customer/Employee) with valid email addresses
- An Email Account to use as the sender (for sending emails)

### How to configure

---

1. Name the document and select the Company, From/To Date, and optionally a Loan Product and View.
2. Set the Applicant Type and Select Applicants By, then click Fetch Applicants.
3. Set print preferences (Letter Head, Orientation, Terms and Conditions).
4. Set email content (Sender, CC To, PDF Name, Subject, Body).
5. To automate delivery, enable Auto Email and set the schedule.
6. Save, then use Download or Send Emails.

![](/files/image1fca1f.webp)

### Fields

---

- Company / From Date / To Date / Loan Product — report filters. From/To Date are mandatory unless Auto Email is on, in which case the window is derived from Filter Duration.
- View — report layout: Detailed or Grouped.
- Applicant Type — Customer or Employee.
- Select Applicants By — how Fetch Applicants collects recipients: by Loan Product or All Loans.
- Applicants — the recipient table (Applicant, Name, Email); at least one required.
- Letter Head / Orientation / Terms and Conditions / Page Break After Each Statement — PDF print preferences.
- Enable Auto Email — send automatically on schedule; reveals the schedule fields.
- Sender / CC To — sending Email Account and copied recipients.
- Frequency / Filter Duration (Months) / Start Date — schedule for auto email (Frequency: Daily, Weekly, Biweekly, Monthly, Quarterly).
- PDF Name / Subject / Body — email content, all Jinja-enabled.

> Jinja: Subject, Body, and PDF Name support [Jinja tags](https://jinja.palletsprojects.com/). All document fields are on the `doc` object and the current row on the `applicant` object (`applicant`, `applicant_name`, `email`).  
> Example: `Loan Statement Of Account for {{ applicant.applicant_name }}`

![](/files/image6e6e3a.webp)

### Actions

---

- Download — generates all applicants' statements as one combined PDF.

![](/files/imagee8524b.webp)

![](/files/imagea3f23e.webp)

- Send Emails — queues each applicant's statement to their email (CC'd as configured); applicants without an email are skipped.

- Scheduled sending — when Auto Email is on, a daily scheduler sends statements automatically when due.

<!-- page: lending/lending__loan-migration__loan-import.md -->
---
title: "Loan Import"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-migration/loan-import"
updated: "2026-02-23"
---

> Available from version-16 onwards

For migrating existing loans or closed loans from another system into Frappe Lending, the standard **Data Import** can be used. A dedicated Loan Import template is available to structure historical loan data correctly. The import process functions like any other document import in the system.

## **1. Prerequisites**

Before starting the import, ensure the following records already exist in the system for all loans to be imported:

- **Loan Product** (ensure it is fully configured, including accounting accounts like Loan, Payment, Interest Income, etc.)
- **Company**
- **Applicant** (Customer or Employee)

## **2. Preparing Data for Import**

To import historical loans, the Loan Import template must be populated and then uploaded via Data Import.

- **Download the Template**: Go to the **Data Import**, select **Loan** as the Document Type, and download the template. It will include all standard Loan fields as well as fields specific to migration (prefixed with "Loan Import Details").
- **Key Fields to Fill**:
  - **Migration Date (Mandatory)**: This field is **required for migrated loans**, regardless of its current `Status` (for example, "Disbursed" or "Closed"). This date acts as the cut-off point for historical data.
  - **Loan Import Details Table**: For loans with multiple historical disbursements, one row per disbursement must be added in the CSV, using the columns prefixed with `(Loan Import Details)`. The most critical columns are the **opening outstanding amounts** (Principal, Interest, Penalty, Charges, etc.) as of the `Migration Date`.
    ![](/files/imagec31cc7.png)
- **Upload and Import**: Once the file is ready, upload it in Data Import. The **"Submit After Import"** option should be enabled so that all created Loan documents are automatically submitted.

## **3. What the System Does**

After the import is complete, the system processes the data differently based on the loan's status:

- **If the loan's Status is "Closed"**: The system creates a simple Loan record with the provided `Migration Date`. No other transactions (like repayment schedules, demands, or interest accruals) are generated for this loan.
- **If the loan's Status is "Disbursed" or "Active" and Loan Import Details have been provided**: The system builds a complete loan history. For each disbursement row, it automatically creates:
  1. **Opening Loan Balance**: The loan's outstanding balance as of the migration date.
  2. **Loan Disbursement**: A record of the historical disbursement.
  3. **Loan Repayment Schedule**: The future repayment schedule based on the loan terms.
  4. **Loan Demands**: Demands for the outstanding principal, interest, penalties, and charges as of the migration date.
  5. **Loan Interest Accruals**: Accrual entries for the outstanding interest amounts.

## **4. Importing Repayments for Migrated Loans**

After migrated loans have been successfully imported, their historical repayment transactions can also be imported. To do this, use the standard Data Import for the **Loan Repayment** doctype. This allows the complete payment history for each migrated loan to be brought into the system.

<!-- page: lending/lending__loan-outstanding-report.md -->
---
title: "Loan Outstanding Report"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-outstanding-report"
updated: "2026-01-06"
---

The **Loan Outstanding Report** in Frappe Lending provides a detailed view of active loans, their repayment progress, and overdue amounts. It allows filtering by company, applicant, loan product, and specific disbursements for easier portfolio tracking.

### Key uses:

- Monitor outstanding loan principal and interest.
- Identify overdue amounts.
- Track EMIs raised, paid, and overdue.
- Review repayment history for specific loans or disbursements.
- Compare total payments made against loan amounts.


![](/files/loan_outstanding_report.png)

<!-- page: lending/lending__loan-partner.md -->
---
title: "Loan Partner"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-partner"
updated: "2026-06-05"
---

**Co-lending in loans** refers to a partnership between two or more lenders, to jointly provide loans to borrowers. In a **co-lending model**, both lenders contribute funds to the loan, share the risks and rewards, and provide more accessible and affordable credit to a broader range of customers. This model has gained popularity as it allows NBFCs to leverage the lower cost of funds from banks, while banks benefit from the NBFC's reach and expertise in specific markets, particularly in underserved or rural areas.

Frappe Lending allows users to onboard and manage these operations for a co-lender using the Loan Partner document.

To access the Loan Partner, go to:


> **Home > Lending > Co-Lending > Loan Partner**
> 
> 

## 1. How to create a Loan Partner

1. Go to the Loan Partner List, and click on Add Loan Partner.
2. Add partner code, partner name, partner loan share percentage, and repayment schedule type.
3. Save

## 2. Co-Lender Repayment Schedule

Once a loan partner is tagged to a loan whenever the loan disbursement is done, along with the borrower schedule a co-lender schedule is also created to track the co-lender share in a loan.

![](/files/LnoWqXJ.png)  


## 3. Co-Lender Accounting

During the disbursements and repayment accounting entries for the amounts payable to the co-lender are also posted

  

<!-- page: lending/lending__loan-product.md -->
---
title: "Loan Product"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-product"
updated: "2026-06-09"
---

# Loan Product

**A loan product can be categorized as an offering given by a NBFC or a Bank to its borrowers.**

Frappe Lending allows users to define different loan products along with their various attributes like the rate of interest, schedule type, etc.

To access the Loan Product, go to:

> Home > Lending > Loan > Loan Product

## Prerequisites

---

Before creating a Loan Product, it is advised to create the following:

- Company
- Loan Category

### How to create a Loan Product

---

1. Go to the Loan Product List, and click on Add Loan Product.
2. Enter the loan product details like product code, product name, rate of interest, repayment schedule type, etc.
3. Save

### Repayment/Amortization Schedule Types

#### Monthly as per repayment start date

If this option is selected a monthly repayment schedule is generated upon loan disbursement as per the repayment start date selected by the user. For this option, there can only be one active repayment schedule at a time, so if multiple partial/tranches are disbursed for this schedule type then a new active repayment schedule is generated and the old schedule is marked as inactive. Here users can also change the frequency of payment to weekly, quarterly, or one-time instead of the monthly default.

#### Pro-rated calendar months

If this option is selected a monthly repayment schedule is generated upon loan disbursement with the payment details as per calendar months. In this option user also gets to choose whether the payment date should be the End of the current month or Start of the next month. For this option as well there can be only one repayment schedule at a time.

#### Monthly as per cycle date

If this option is selected a monthly repayment schedule is generated upon loan disbursement as per the cyclic date selected by the user in the loan product, however user can override this at the time of loan booking. For this option as well there can be only one repayment schedule at a time. Here also users can change the frequency of payment to weekly, quarterly, or one-time instead of the monthly default.

#### Line of Credit

This repayment schedule is useful for line of credit loans where an upper limit is sanctioned and multiple disbursements are made within the limit. For this repayment type there can be multiple active repayment schedules with different payment frequencies.

#### Flat Interest Rate

This option is useful when interest is handled as a flat-rate schedule across the tenure. It is generally used in products where repayment breakup follows a predefined flat-interest pattern.

![](/files/image62124e.png)
*Repayment/Amortization Schedule Types*

### Additional Information

#### BPI Recovery Method

This field controls how broken period interest (interest between disbursement date and first EMI period) is recovered. You can recover it as upfront deduction, amortize it across tenure, add it to first EMI, or add it to last EMI.

![](/files/image38c5af.png)
*BPI Recovery Method*

#### Cyclic Day Of the Month

This is used with Monthly as per cycle date schedule type. It defines the day of the month on which repayment is considered due. It helps standardize due dates across borrowers for operational convenience.

#### Days Past Due Threshold for NPA

This value defines when a loan should be treated as NPA based on days past due. Once borrower delinquency crosses this threshold, the system can treat the account as non-performing.

#### Minimum days between Disbursement date and first Repayment date

This field ensures that the first repayment date is not too close to disbursement. If the gap is smaller than this value, first repayment can be shifted to the next eligible cycle so borrowers get a minimum initial repayment window.

#### Excess Amount Acceptance Limit

During final repayment, if borrower pays extra and the excess amount is within this limit, loan can still be auto-closed and excess is parked in customer refund handling. If excess is above this limit, the excess amount can still be parked in customer refund account but the loan may remain open.

#### Auto Write Off Amount

During closure, if a small shortfall remains and it is within this limit, the system can auto-waive or write off the residual amount and proceed with loan closure.

#### Grace Period in Days

This defines the number of days after due date during which penal interest is not charged. Penalty interest starts applying only after this grace period is crossed.



![](/files/image8e3385.png)
*Additional Information*

### Excess amount acceptance and auto write-off limits

---

![](/files/MWMNZoX.png)

If the final repayment made is short of some amount and the amount is within Auto Write Off Amount, the amount will be auto-waived and the loan will be closed.

Similarly, in case the borrower makes the final payment with some excess amount and the amount is within Excess Amount Acceptance Limit, the amount is parked in the customer refund account and the loan is closed. If the excess amount is more than the acceptance limit, the amount is still parked in customer refund account but the loan still remains open.

<!-- page: lending/lending__loan-refund.md -->
---
title: "Loan Refund"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-refund"
updated: "2026-01-06"
---

A **loan refund** occurs when a borrower receives a return of a payment they made toward their loan, either in part or in full. This typically happens in specific situations where there was an overpayment, a mistake in payment processing, or other exceptional circumstances that require the lender to return the funds to the borrower.

Frappe Lending allows users to make such refunds using the loan refund doctype.

To access the Loan Refund, go to:


> **Home > Lending > Loan Adjustments > Loan Refund**
> 
> 

![](/files/5qiRaAd.png)  


**1. How to create a Loan Refund**

1. Go to the Loan Refund List, and click on Add Loan Refund.
2. Enter the loan account and the amount to be refunded.
3. Save and submit.

<!-- page: lending/lending__loan-repayment.md -->
---
title: "Loan Repayment"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-repayment"
updated: "2026-05-31"
---

**Loan repayment** refers to the process of paying back the borrowed amount (loan principal) along with any interest and fees over a specified period, according to the terms agreed upon between the borrower and the lender. Loan repayment can occur through periodic payments (monthly, quarterly, etc.) or in a lump sum, depending on the loan agreement.

To access the Loan Repayment, go to:

> **Home > Lending > Disbursement and Repayment > Loan Repayment**

**1. How to create a Loan Repayment**
-------------------------------------

1. Go to the Loan Repayment List, and click on Add Loan Repayment.
2. Enter the loan account, repayment type and the amount to be repaid.
3. Save and submit.

**2. Collection Offset Sequences**
----------------------------------

A **Collection Offset Sequence** in Loan Repayment refers to a structured method used to determine how borrower payments are allocated across loan components such as principal, interest, penalty, and charges. This ensures transparent allocation, especially for partial payments.

Frappe Lending allows users to define 4 collection offset sequences under the Loan tab in Company:

1. For Standard Assets (Non-NPA loans)
2. For Sub-standard Assets (NPA loans)
3. For Settlement Collection
4. For Written Off Assets

![](/files/phjd9KM.png)

**3. Advance and Pre Payment**
------------------------------

Whenever a borrower makes an Advance/Pre-payment, the loan is rescheduled and a new repayment schedule is generated based on the type of payment.

- **Advance Payment**

  A payment is treated as an advance payment when the repayment type is selected as Advance Payment and the excess amount falls between one EMI and two EMI amounts (for term loan validation flow). In this case, upcoming EMI handling follows advance payment rules.

- **Pre Payment**

  Any excess payment outside advance-payment criteria is generally treated in pre-payment logic. Excess amount after applicable interest adjustments is pushed toward principal and schedule is adjusted accordingly.

In both types, EMI amount generally remains the same while tenure or the last payment adjusts as required.


### Loan status-based repayment restrictions

- If loan status is **Closed**, only selected waiver/adjustment types are allowed.
- If loan status is **Written Off**, repayment is restricted to **Write Off Recovery** or **Write Off Settlement** (except internal write-off waiver flows).
- After **Full Settlement**, only waiver types (Interest, Penalty, Charges) are allowed for subsequent entries.

### Full Settlement backdate restriction

Full Settlement cannot be posted with a value date earlier than the latest existing repayment date for that loan (or loan disbursement in line-of-credit context).

### Validation for waiver amount

For Interest/Penalty/Charges Waiver, waived amount cannot be greater than the corresponding overdue amount available at the time of repayment.

### Validate Normal Repayment behavior

If **Validate Normal Repayment** is enabled in Loan Product, amount paid in Normal Repayment cannot exceed payable amount.

### Line of Credit (LoC) specific behavior

In LoC loans, repayments can be linked to a specific disbursement. Allocation, schedule closing, and certain validations are performed at loan-disbursement level when provided.

### Security Deposit Adjustment repayment

For Security Deposit Adjustment, amount paid cannot exceed available security deposit and cannot exceed payable amount (except adjustment-specific flows).

### Auto-close and auto-waiver scenario

During repayment, auto-close logic evaluates shortfall and excess conditions against Loan Product settings such as Auto Write Off Amount and Excess Amount Acceptance Limit.

If auto-close condition is satisfied, system may auto-create one pending component entry to complete closure flow:

- Interest Waiver
- Penalty Waiver
- Charges Waiver
- Principal Adjustment

### Write-off recovery collection behavior

When loan is in written-off/settled recovery path, repayment allocation includes recovery-aware handling of pending waiver balances and accrued components to ensure correct collection tracking.

### Source of offset sequence (fallback rule)

Offset sequence is first taken from Loan Product. If not set there, system falls back to Company-level sequence for that asset state.

<!-- page: lending/lending__loan-restructure.md -->
---
title: "Loan Restructure"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-restructure"
updated: "2026-01-06"
---

**Loan restructuring is the process of modifying the terms of an existing loan agreement between a borrower and a lender. This is typically done to help the borrower manage their debt more effectively, especially if they are experiencing financial difficulties that make it challenging to meet the original loan terms. Loan restructuring can involve changes in the interest rate, repayment schedule, loan tenure, or even the principal amount.**

Frappe Lending allows users to define different loan products along with their various attributes like the rate of interest, schedule type, etc.

To access the Loan Restructure, go to:


> **Home > Lending > Loan > Loan Restructure**
> 
> 

**2. How to create a Loan Restructure**
---------------------------------------

1. Go to the Loan Restructure List, and click on Add Loan Restructure.
2. Select the loan account and fill in the restructure date, previous details will be automatically fetched.
3. Fill in the details like new tenure, new interest rate, how previous pending interest and penalties are to be handled, if the security deposit has to be adjusted in principle, and lastly, select the new repayment start date and save.
4. A new restructured repayment schedule will be generated as per the new terms selected. Verify and submit the restructure.

**3. Capitalization of due interest and charges**
-------------------------------------------------

During restructuring, users have an option of how the pending accrued/unbooked interest and charges should be treated. They can either add that amount to the first EMI post-restructure or Capitalize (add the pending amount to the principal amount). 

![](/files/sPii7Fb.png)  

<!-- page: lending/lending__loan-security-assignment.md -->
---
title: "Loan Security Assignment"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-security-assignment"
updated: "2026-01-06"
---

**Security or collateral assignment in loans** refers to the process by which a borrower pledges certain assets as security or collateral for a loan. In the event of default, the lender has the legal right to seize or sell the collateral to recover the outstanding loan amount. This assignment is a way for the lender to mitigate risk and ensure repayment, particularly in cases of secured loans.

Frappe lending allows users to assign multiple securities/collaterals against loans and enforce certain validations during the loan cycle.

To access the Loan Product, go to:


> **Home > Lending > Loan Security > Loan Security Assigment**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Security, it is advised to create the following:

* Loan Security

**2. How to create a Loan Security Assignment**
-----------------------------------------------

1. Go to the Loan Security Assignment List, and click on Add Loan Security Assignment.
2. Select the loan account against which the security/collateral has to be pledged.
3. Add the Loan Security, add security price manually if Loan Security Price is not configured
4. Save and Submit.

![](/files/RcKN8aG.png)  

<!-- page: lending/lending__loan-security-price.md -->
---
title: "Loan Security Price"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-security-price"
updated: "2026-01-06"
---

A Loan Security Price is the security/collateral rate pledged against a loan for a specific period. This rate is auto-applied if a loan security is pledged/assigned against a loan during that specific period.

To access the Loan Security Pricie, go to:


> **Home > Lending > Loan Security > Loan Security Price**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Product, it is advised to create the following:

* **Loan Security**

**2. How to create a Loan Security Price**
------------------------------------------

1. Go to the Loan Security Price List, and click on Add Loan Security Price.
2. Select the Loan Security, and enter the rate and validity period.
3. Save

![](/files/QGjMbdX.png)  

<!-- page: lending/lending__loan-security-release.md -->
---
title: "Loan Security Release"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-security-release"
updated: "2026-01-06"
---

**Security release in loans** refers to the process in which a lender relinquishes the claim or lien on an asset that was used as collateral once the borrower has fully repaid the loan. Essentially, the asset, such as property, vehicles, or other pledged securities, is "released" from the lender’s control or interest, returning full ownership rights to the borrower.

If a security/collateral has been assigned to a loan, it has to be released before the loan can be closed.

To access the Loan Security Release, go to:


> **Home > Lending > Loan Security > Loan Security Release**
> 
> 

**1. How to create a Loan Security Release**
--------------------------------------------

1. Go to the Loan Security Release List, and click on Add Loan Security Release.
2. Enter the Loan account, loan securities along with their quantity to be released
3. Save

![](/files/Jd7dYBF.png)  

<!-- page: lending/lending__loan-security-type.md -->
---
title: "Loan Security Type"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-security-type"
updated: "2026-01-06"
---

**A loan security type is a way to classify securities/collaterals based on types.**

Depending on the type of loan security, you can categorize a security under its respective type like stocks, bullion, property, etc.

![](/files/BrXjKoR.png)  


To access the Loan Security Type, go to:


> **Home > Lending > Loan Security> Loan Security Type**
> 
> 

**1. How to create a Loan Security Type**
-----------------------------------------

1. Go to the Loan Security Type List, and click on Add Loan Security Type.
2. Entry security type, haircut, and loan-to-value ratio.
3. Save

<!-- page: lending/lending__loan-security.md -->
---
title: "Loan Security"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-security"
updated: "2026-01-06"
---

**A Loan Security is the actual security that is going to be pledged against a loan.**

During a loan process, if the loan for which the customer is applying is a secured loan then some security needs to be pledged against that loan. Loan Security specifies the actual security that is going to be pledged against a Loan.

To access the Loan Security, go to:


> **Home > Lending > Loan Security > Loan Security**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Security, it is advised to create the following:

* Loan Security Type

**2. How to create a Loan Security**
------------------------------------

1. Go to the Loan Security List, and click on Add Loan Security.
2. Enter the loan security name/code, loan security type.
3. Save

![](/files/xzZMDAj.png)  

<!-- page: lending/lending__loan-settlemets.md -->
---
title: "Settlements"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-settlemets"
updated: "2026-05-31"
---

**Loan settlement** refers to an agreement between a borrower and a lender to resolve the outstanding loan balance for an amount less than what is owed. In a loan settlement, the lender agrees to accept a lump-sum payment that is less than the total outstanding balance in exchange for closing the loan. This is often done in cases where the borrower is facing financial difficulties and is unable to repay the full amount of the loan.

To make a Settlement Entry, go to:

> **Home > Lending > Disbursement and Repayment > Loan Repayment**

**1. How to make a settlement**
-------------------------------

1. Go to the Loan Repayment List, and click on Add Loan Repayment.
2. Enter the loan account, repayment type as Full/Partial or Write Off Settlement and the amount to be repaid.
3. Save and submit.


### Full Settlement vs Partial Settlement

- **Full Settlement** is used when borrower and lender agree to settle the loan in one final settlement event.
- **Partial Settlement** is used when settlement collection is done as part of a negotiated recovery flow but full closure is not completed in the same entry.

In settlement-type repayments, collection allocation follows **Settlement Collection Offset Sequence**.

### Write Off Settlement scenario

**Write Off Settlement** is used when the loan has already moved into written-off state and a settlement recovery is collected afterwards. This is different from normal full settlement on active/disbursed loans.

### Important validation cases

- Full Settlement cannot be backdated before the latest repayment value date for that loan (or that disbursement in LoC context).
- After Full Settlement, only waiver entries (Interest, Penalty, Charges) are allowed as subsequent entries.
- Write Off Recovery / Write Off Settlement entries are only allowed when the loan is in written-off lifecycle.

### Line of Credit (LoC) settlement behavior

For LoC loans, settlement and repayment entries can be linked to a specific disbursement. In this case, validation, schedule status updates, and some settlement checks are applied at disbursement level.

### Auto-close impact during settlement

During settlement posting, system evaluates auto-close conditions using Loan Product settings such as write-off limit and excess amount acceptance behavior. Based on these conditions, loan status can move to Settled/Closed as applicable.

### Recovery allocation after write-off

For write-off recovery and write-off settlement collections, repayment allocation also considers previously waived components and accrued pending components so that recovery accounting remains consistent.

### Offset sequence source

Settlement allocation order is taken from Loan Product first. If not set there, Company-level settlement sequence is used as fallback.

<!-- page: lending/lending__loan-transfer.md -->
---
title: "Loan Transfer"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-transfer"
updated: "2026-01-06"
---

**A loan transfer within branches refers to the process of moving a loan from one branch of a bank or financial institution to another branch within the same organization. This can occur for various operational, logistical, or customer service reasons. The underlying terms of the loan, such as the interest rate, repayment schedule, and principal balance, typically remain unchanged during such a transfer.**

Frappe Lending allows users to transfer loans from one branch to another and move all the internal accounting as well.

To access the Loan Transfer, go to:


> **Home > Lending > Transfers> Loan Transfer**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Loan Transfer, it is advised to create the following:

* Branch (This should also be configured as an accounting dimension as well)

**2. How to create a Loan Transfer**
------------------------------------

1. Once you are done configuring the Branch doctype as an accounting transfer you can go to the Loan Transfer list, click on Add Loan Transfer.
2. Users can optionally select an applicant if loans for only one applicant have to be transferred.
3. If any entire branch is being merged into another branch or being split from other brach users can just select the **From Branch** and **To Branch** and save the document.
4. On saving the document all the loans linked to the **From Branch** will be fetched and Journal Entries are created as per the current net balances that have to moved.
5. Once the user submits the document, the branch is updated in the loan record and the journal entry is submitted.

<!-- page: lending/lending__loan-waivers.md -->
---
title: "Loan Waivers"
space: "Lending"
url: "https://docs.frappe.io/lending/loan-waivers"
updated: "2026-05-31"
---

# Loan Waivers

A **loan waiver** refers to the cancellation or forgiveness of the interest or charge component of a loan for a specific period or in particular circumstances. This means that the borrower is either not required to pay the interest accrued on the loan, or the lender refunds or credits the interest that has already been paid.

To make a waiver, go to:

> **Home > Lending > Disbursement and Repayment > Loan Repayment**

**1. How to create a Loan Waiver**
----------------------------------

1. Go to the Loan Repayment List, and click on Add Loan Repayment.
2. Select the repayment type as Interest, Penalty, or Charges Waiver.
3. Select the loan account number against which the waiver is done and enter the waiver amount.
4. Save and submit.

Once the waiver entry is submitted the overdue demands are knocked off as per the amount waived and the waived amount is updated in the respective demands

![Loan Demand Waiver](/files/Loan Demand Waiver.png)

On submitting an Interest Loan Waiver, below are the typical accounting entries that are posted

![Loan Interest Waiver Accounting](/files/Loan Interest Waiver Accounting.png)

As you can see in the above screenshot income booking is also reversed in case the waiver is done on a non-NPA loan.


### Different types of waivers

- **Interest Waiver**: Used to waive due interest exposure. In waiver validation, system considers overdue interest and other pending interest components applicable on the loan at waiver time. On non-NPA loans, income reversal entries are also posted.
- **Penalty Waiver**: Used to waive penal dues. This covers pending penalty components and related penalty-side outstanding at repayment time. For non-NPA loans, penalty income reversal behavior is applied.
- **Charges Waiver**: Used to waive charge demands (processing charges, penalty charges, and other configured demand charges) that are outstanding against the loan.

### Auto waiver

In specific closure situations, waiver entries can be auto-created by the system after repayment submission.

- Auto-close eligibility is evaluated from loan closure conditions such as shortfall within product-level write-off limit and acceptable excess handling.
- If auto-close condition is met, system recalculates pending amounts and creates waiver/adjustment entry automatically for the pending component.
- The system can auto-create one of these entries based on what is still pending at that moment: Interest Waiver, Penalty Waiver, Charges Waiver, or Principal Adjustment.

This makes final closure smoother by automatically clearing small residual components without requiring users to manually post separate waiver entries.

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

![](/files/aH2TgZJ.png)


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

![Loan Cycle](/files/Loan Cycle.png)  


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

![](/files/loan-repayment-frequency.png)  


4. Adding moratorium during loan booking
----------------------------------------

A **moratorium** in a loan context refers to a temporary suspension or postponement of loan repayments for a specified period of time, during which the borrower is not required to make any payments towards the loan principal or interest. The moratorium period is usually granted during times of financial hardship, economic downturns, or in special circumstances such as the COVID-19 pandemic. It allows borrowers relief from financial stress, giving them time to stabilize their finances before resuming regular loan payments.

To add a moratorium, the user can mention the Moratorium Tenure and moratorium type at the loan booking stage

![](/files/chocp3b.png)  


There are two moratorium types available, if EMI is selected, both interest and principal are not applicable and if the Principal is selected the only interest is payable, and the principal component is not applicable.

5. Revolving limits for Line Of Credit loans
--------------------------------------------

**Revolving limits** in **line of credit loans** refer to the maximum amount of credit that a borrower can access and use on a recurring basis. A **line of credit (LOC)** is a flexible loan option that allows borrowers to draw funds as needed, up to a specified credit limit, repay the borrowed amount, and then access the credit again without having to apply for a new loan. This process is known as revolving credit because the credit becomes available again as the borrower repays it, up to the original limit.

![](/files/MuuLwuj.png)  


6. Loan Account Freezing (Death Marking)
----------------------------------------

If the borrower dies or is unable to make the repayments due to any circumstances the loan account can be frozen. Upon freezing the accounts the loan interest accrual and demand generation stops.

![Freeze Loan Account](/files/Freeze Loan Account.png)  

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

![](/files/I6hNEJV.png)

Users can also track historical day-wise DPD data in **Days Past Due Logs**.

![](/files/FCMD2WD.png)

## 2. NPA Marking

NPA marking is based on DPD crossing configured threshold values.

Important correction:

- The threshold used for NPA marking is primarily taken from **Loan Product** (`Days Past Due Threshold for NPA`).
- Company-level DPD threshold is used for **auto write-off trigger**, not as the primary NPA marking threshold.

When DPD crosses the configured NPA limit, loan is auto-marked as NPA.

![](/files/ZfADryn.png)

This threshold is evaluated based on the oldest overdue EMI demand path used in classification processing.

![](/files/xL1t3ZO.png)

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


![](/files/past_cashflow_report.png)

<!-- page: lending/lending__process-loan-classification.md -->
---
title: "Process Loan Classification"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-classification"
updated: "2026-01-06"
---

The loan classification process is a daily process that is used to classify the loans for credit bureau reporting. This one single process updates multiple parameters of a loan like days past due, marking or unmarking the loan as NPA, and updating the classification codes. Users can also run this process manually to do an ad-hoc classification.

![Process Loan Classification](/files/Process Loan Classification.png)  


The classification codes and bucket can be configured in the Company master under the loan tab

![Loan Classification Ranges](/files/Loan Classification Ranges.png)  

<!-- page: lending/lending__process-loan-demand.md -->
---
title: "Process Loan Demand"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-demand"
updated: "2026-01-06"
---

Demands are generated by a demand generation process the doctype for which is called Process Loan Demand, even for manual creation of demands this process has to be used rather than creating the demands manually.

  


![Process Loan Demand](/files/Process Loan Demand.png)  

<!-- page: lending/lending__process-loan-interest-accrual.md -->
---
title: "Process Loan Interest Accrual"
space: "Lending"
url: "https://docs.frappe.io/lending/process-loan-interest-accrual"
updated: "2026-01-06"
---

Loan interest accruals are done via a process called “Process Loan Interest Accrual”. To process the loan interest accrual manually a user has to use this doctype where they can enter a posting date up to which interest accrual has to be done. Optionally a specific loan or a loan product can also be provided

  


![Process Loan Interest Accrual](/files/Process Loan Interest Accrual.png)  

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

![Repayment Schedule](/files/Repayment Schedule.png)  


  

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

![Suspense Account](/files/Suspense Account.png)  


Once the accounts are configured, as soon as the loan becomes NPA, a Journal Entry is automatically passed for the outstanding interest, penalty or charge amount and the amount is moved from regular income to suspense account.

![](/files/rOuGyGM.png)  


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

![](/files/imagefa2bc7.png)

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

![](/files/imagefddc9f.png)

Then map in Workflow transitions:

- Scrubbing -> Pre-Qualification -> Transition Tasks = Loan Lead - Pre-Qualification Tasks

![](/files/image5abb72.png)

## References

- Workflow: [https://docs.frappe.io/erpnext/workflows](https://docs.frappe.io/erpnext/workflows)
- Workflow Transition Tasks: [https://docs.frappe.io/erpnext/workflow-transition-tasks](https://docs.frappe.io/erpnext/workflow-transition-tasks)
