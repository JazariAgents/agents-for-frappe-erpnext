<!-- Frappe documentation: lending, part 2 of 3. Index: docs/INDEX.md -->

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
