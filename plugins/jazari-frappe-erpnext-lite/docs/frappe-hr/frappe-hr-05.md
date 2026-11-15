<!-- Frappe documentation: frappe-hr, part 5 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__india-payroll__professional-tax.md -->
---
title: "Professional Tax"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/professional-tax"
updated: "2026-07-03"
---

# Professional Tax

Professional Tax (PT) is a state-level tax levied on employment income in India. India Payroll automates PT deduction on every Salary Slip update based on the employee's **Employment State** and **Gross Pay**.

> **Statutory reference:** Article 276 of the Constitution limits PT to ₹2,500 per person per year.

---

## 1. How to Enable

1. Go to **Payroll Settings → India Payroll** tab.
2. Check **Enable Professional Tax Deduction**.
3. Save.

[Screenshot on the live page]
*Enabling Professional Tax Deduction*



Once enabled, the `Professional Tax` salary component is automatically injected into (or removed from) each Salary Slip's deductions table when the slip is saved.

---

## 2. How It Works

The `apply_professional_tax` method runs via `apply_regional_deductions` hook:

```
Salary Slip (before_save)
    │
    ├─ enable_professional_tax in Payroll Settings? → NO → skip
    ├─ salary_structure set? → NO → skip
    ├─ employment_state from SSA → not in PT states? → skip
    │
    ├─ frequency = monthly?
    │       └─ _compute_pt_monthly(gross_pay, state_config, month, gender)
    │
    └─ frequency = half-yearly?
            └─ _compute_pt_half_yearly(doc, state_config)
                  └─ cumulative gross across submitted slips in period
                     − already deducted PT = this month's PT

```

The computed amount replaces any existing `Professional Tax` row.

---

## 3. Employment State

PT is determined by the **Employment State** set on the **Salary Structure Assignment** (not the Employee master's state field). This allows an employee transferred mid-year to have the correct PT rule applied per assignment.

To set it:

1. Open the **Salary Structure Assignment** for the employee.
2. Set **Employment State**.

> **Validation:** When PT is enabled, saving a Salary Structure Assignment without an Employment State throws an error, preventing silent mis-deduction.



[Screenshot on the live page]
*Employment State in Salary Structure Assignment*

---

## 4. Supported States & Rate Tables

### Monthly States

These states deduct PT every month based on gross pay slabs.


| State              | Slab (Gross ≤) | PT Amount (₹/month)    |
| ------------------ | -------------- | ---------------------- |
| **Andhra Pradesh** | 15,000         | 0                      |
|                    | 20,000         | 150                    |
|                    | Above 20,000   | 200                    |
| **Assam**          | 10,000         | 0                      |
|                    | 15,000         | 150                    |
|                    | 25,000         | 180                    |
|                    | Above 25,000   | 208                    |
| **Bihar**          | 25,000         | 0                      |
|                    | Above 25,000   | 200                    |
| **Gujarat**        | 5,999          | 0                      |
|                    | 8,999          | 80                     |
|                    | 11,999         | 150                    |
|                    | Above 11,999   | 200                    |
| **Jharkhand**      | 25,000         | 0                      |
|                    | Above 25,000   | 100                    |
| **Karnataka**      | 25,000         | 0                      |
|                    | 41,666         | 150                    |
|                    | Above 41,666   | 200                    |
| **Madhya Pradesh** | 18,750         | 0                      |
|                    | 25,000         | 125                    |
|                    | 33,333         | 167                    |
|                    | Above 33,333   | 208                    |
| **Maharashtra**    | 7,500          | 0                      |
|                    | 10,000         | 175                    |
|                    | Above 10,000   | 200 (₹300 in February) |
| **Meghalaya**      | 4,166          | 0                      |
|                    | 6,250          | 16                     |
|                    | …              | …                      |
|                    | Above 37,500   | 208                    |
| **Odisha**         | 13,304         | 0                      |
|                    | 25,000         | 125                    |
|                    | 41,666         | 167                    |
|                    | Above 41,666   | 208                    |
| **Sikkim**         | 20,000         | 0                      |
|                    | 30,000         | 125                    |
|                    | 40,000         | 150                    |
|                    | Above 40,000   | 200                    |
| **Telangana**      | 15,000         | 0                      |
|                    | 20,000         | 150                    |
|                    | Above 20,000   | 200                    |
| **Tripura**        | 7,500          | 0                      |
|                    | 15,000         | 150                    |
|                    | Above 15,000   | 208                    |
| **West Bengal**    | 8,500          | 0                      |
|                    | 10,000         | 90                     |
|                    | 15,000         | 110                    |
|                    | 25,000         | 130                    |
|                    | 40,000         | 150                    |
|                    | Above 40,000   | 200                    |


### Half-Yearly States

These states compute PT on a cumulative basis across each half-year period (Apr–Sep or Oct–Mar). The full slab amount is charged in the **first month** of the period, and nothing more until the next period.


| State          | Period            | Slab (Cumulative Gross ≤) | PT Amount (₹/half-year) |
| -------------- | ----------------- | ------------------------- | ----------------------- |
| **Tamil Nadu** | Apr–Sep / Oct–Mar | 21,000                    | 0                       |
|                |                   | 30,000                    | 135                     |
|                |                   | 45,000                    | 315                     |
|                |                   | 60,000                    | 690                     |
|                |                   | 75,000                    | 1,025                   |
|                |                   | Above 75,000              | 1,250                   |
| **Kerala**     | Apr–Sep / Oct–Mar | 11,999                    | 0                       |
|                |                   | 17,999                    | 120                     |
|                |                   | 29,999                    | 180                     |
|                |                   | 44,999                    | 480                     |
|                |                   | 59,999                    | 720                     |
|                |                   | 74,999                    | 1,080                   |
|                |                   | 99,999                    | 1,440                   |
|                |                   | Above 99,999              | 1,560                   |


---

## 5. Special Rules

### Maharashtra — February Rule

Maharashtra employees earning above ₹10,000/month pay **₹300 in February** instead of the usual ₹200. This ensures the annual total equals the constitutional cap of ₹2,500:

```
11 months × ₹200 + February × ₹300 = ₹2,500

```

This is handled automatically by the hook, no configuration required.

### Maharashtra - Women Exemption

Women earning **≤ ₹10,000/month** are fully exempt from Professional Tax in Maharashtra. The hook reads the `gender` field from the Employee master and sets PT to ₹0 automatically.

### Half-Yearly Incremental Logic (Kerala, Tamil Nadu)

For half-yearly states, the hook:

1. Sums **gross_pay** from all *submitted* salary slips in the current half-year period (excluding the current unsaved slip).
2. Adds the current slip's gross pay → cumulative figure.
3. Applies the state slab to the cumulative → **total PT due for the period**.
4. Subtracts PT already deducted in prior slips of the same period.
5. Charges the remainder (minimum ₹0) on the current slip.

**Result:** PT is front-loaded in the first month of the period, and zero in subsequent months once the slab amount is paid.

<!-- page: frappe-hr/hr__india-payroll__reports.md -->
---
title: "Reports"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/reports"
updated: "2026-07-09"
---

# Reports

India Payroll ships the following reports, accessible from the **India Payroll** module.

---

## ESIC Register

A month-wise ESI contribution statement showing each employee's gross wages, employee contribution (0.75%), employer contribution (3.25%), and coverage status. Use it to prepare the monthly filing for the ESIC portal.

[Screenshot on the live page]

## LWF Register

A state-wise Labour Welfare Fund deduction register showing each employee's deduction status for the selected month — whether LWF was deducted, it was a non-deduction month, the employee is exempted, or their state has no LWF. Use it to prepare the remittance challan for the State Labour Welfare Board.



[Screenshot on the live page]

## Bank Mandate Report

Lists each employee's net pay alongside their bank details (account number, IFSC, MICR, payment mode). Hand this to your bank or upload it to your ECS/NEFT batch processing system for salary disbursement.



[Screenshot on the live page]

<!-- page: frappe-hr/hr__india-payroll__tax-regime-selector.md -->
---
title: "Tax Regime Selector"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/tax-regime-selector"
updated: "2026-07-03"
---

Indian employees choose between the old and new income tax regimes at the start of each financial year, and payroll is processed according to that choice. The regime that results in less tax differs from employee to employee, depending on their salary, rent, investments, and employer contributions.

The Tax Regime Selector computes the annual tax under both regimes for an employee, recommends the one with the lower tax, and records the choice on the employee's Salary Structure Assignment so that payroll uses it.



To access the Tax Regime Selector, go to

> Home > India Payroll > Tax Regime Selector



[Screenshot on the live page]

## 1. How to select a tax regime

To compare regimes and save a choice for an employee:

- Open the Tax Regime Selector. The Payroll Period is set to the active period for the company and the Employee defaults to the logged-in user. HR users can select any employee.
- Confirm the Annual Gross Earning. It is fetched from the employee's latest Salary Structure Assignment and can be edited.
- Enter the employee's declarations in the table below.
- Review the comparison shown on the right. The recommended regime and the resulting saving are highlighted.
- Select a regime and click Save Regime in the toolbar.

[Screenshot on the live page]

The Payroll Period is mandatory. If no period covers today's date, the page will prompt you to create one. An employee with no Salary Structure Assignment cannot be processed.



## 2. Features

### 2.1 Declarations

Declarations are entered in a table grouped by exemption section. Deduction components already present in the employee's salary structure, such as EPF and employee NPS, are matched by name and prefilled. Enter the remaining declarations directly.

Sections that do not apply to the employee are hidden: `80GG` is hidden when the salary structure includes HRA, and `80TTA` or `80TTB` is shown depending on whether the employee is a senior citizen.



### 2.2 HRA Exemption

If the salary structure includes an HRA component, fields for the monthly rent and whether the employee lives in a metro city are shown. The HRA exemption is calculated as the lowest of the following:

- Actual HRA in the salary,
- 50% of basic salary for metro cities, or 40% for non-metro cities,
- Rent paid minus 10% of basic salary.

No exemption is applied if no rent is entered.

### 2.3 Comparison

The table breaks down detailed comparison between the two tax regimes, showing which exemptions are applicable in New and Old Regime  

### 2.4 Saving the regime

Selecting a regime stages the choice and updates the comparison. Click Save Regime in the toolbar to commit it. After confirmation, the Income Tax Slab is set on the employee's draft Salary Structure Assignment.

:::note
A regime can only be saved while the Salary Structure Assignment is a draft. Once the assignment is submitted, it is read-only, the selection controls are hidden, and the tool will not overwrite the existing slab.
:::



### 2.5. Notifying Employees

The notify actions prompt employees to make a choice before their Salary Structure Assignment is submitted.



To notify a single employee, open their Salary Structure Assignment and click the Notify to Select Tax Regime button. The employee receives an email with a link to the Tax Regime Selector.



To notify several employees at once, go to the Salary Structure Assignment list, select the draft assignments, and run the same action. Only draft assignments are mailed; submitted assignments and employees without an email address are skipped. A message reports how many employees were notified and how many were skipped.

Emails are sent to the employee's preferred email, falling back to the company email, and then the personal email.



[Screenshot on the live page]



## 3. Declaring tax exemptions

The declarations entered in the tool are used for the comparison only; they are not saved on their own. To record them as the employee's official declaration, click Declare Tax Exemptions

This opens a new Employee Tax Exemption Declaration, prefilled with:

- Selected employee and payroll period,
- Monthly rent and metro-city flag, if the salary structure includes HRA,
- Row for each declared sub-category and its amount.



[Screenshot on the live page]

Review the document and submit it as usual. The declaration is then available to payroll and to exemption proof submission, the same as one created manually.



## 4. Setup

The first time the page is opened on a site, it creates the Income Tax Slabs and Employee Tax Exemption Categories if they do not already exist. This runs automatically, is idempotent, and requires no manual setup.



## 5. Related Topics

- [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
- [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration)
- [Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab)
- [Payroll Period](https://docs.frappe.io/hr/payroll-period)

<!-- page: frappe-hr/hr__india-payroll__tds-filing.md -->
---
title: "TDS Filing"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/tds-filing"
updated: "2026-08-31"
---

India Payroll files the quarterly salary TDS return for you. It reads the tax actually deducted on submitted Salary Slips, reconciles it against the challans you deposited, and then takes the return through validation, the TXT file, the FVU and e-filing, without you touching the RPU or the FVU utility.

The end result is a filed return with a provisional receipt number, the FVU and Form 27A stored on the record, and, for Q4, Form 16 certificates for every employee in the return.

## **Contents**

- [Setup](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#setup)
- [Recording challans](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#recording-challans)
- [Creating a return](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#creating-a-return)
- [Filing the return](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#filing-the-return)
- [Fetching the CSI file](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#fetching-the-csi-file)
- [Skipping validation](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#skipping-validation)
- [Submitting the return](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#submitting-the-return)
- [Revised returns](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#revised-returns)
- [Form 16](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#form-16)
- [Filing statuses](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#filing-statuses)
- [Troubleshooting](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/tds-filing.md#troubleshooting)

## **Setup**

### **1. Sandbox credentials**

Go to **Payroll Settings &gt; TDS Filing**.

Sites hosted on Frappe Cloud have credentials provisioned for them, so there is nothing to enter: the section shows a note saying the credentials are managed for you. Every other site enters its own pair from a sandbox.co.in account:


| Field                        | Notes                                                                                           |
| :---------------------------- | :----------------------------------------------------------------------------------------------- |
| Enable TDS Return Filing     | Only appears once a credential pair is available.                                               |
| Use Sandbox Test Environment | Checked by default. Test keys only work against the test environment. Uncheck for real filings. |
| Sandbox API Key / Secret     | From your sandbox.co.in account.                                                                |
| Sandbox API Version          | Defaults to `1.0.0`.                                                                            |


### **2. Deductor details on Company**

**Company &gt; TDS Deductor Details**:


| Field                                       | Notes                                                                                             |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| TAN                                         | 10 characters, format `ABCD12345E`. Validated on save.                                            |
| Deductor Type                               | Company, Firm, Central Government and so on.                                                      |
| Responsible Person Name / PAN / Designation | The person responsible for deduction, as per income tax records. PAN format is validated on save. |


The company PAN is the existing **Tax ID** field on Company.

### **3. Salary component**

At least one enabled Deduction component must be marked **Is Income Tax Component** (or **Variable Based on Taxable Salary**). That is what the return reads to find the tax deducted on each salary slip.

### **4. Employee PAN**

Each employee in the return needs a valid PAN on their Employee record. Where a PAN genuinely does not exist, the placeholders `PANNOTAVBL`, `PANAPPLIED` and `PANINVALID` are accepted.

### **Permissions**

**TDS Return**, **TDS Challan** and **Form 16** are available to the **Payroll Manager** and **System Manager** roles.

## **Recording challans**

Create a **TDS Challan** for every deposit you made for the quarter. This is what the return reconciles against, and every deductee row has to point at one.


| Field                            | Notes                                                             |
| :-------------------------------- | :----------------------------------------------------------------- |
| Company, Financial Year, Quarter | Used to find the challans for a return.                           |
| Deposit Date                     | The date the challan was paid.                                    |
| BSR Code                         | Exactly 7 digits.                                                 |
| Challan Serial No                | As printed on the challan.                                        |
| Total Deposited                  | Must equal the sum of the breakup below, if a breakup is entered. |
| Amount Breakup                   | TDS, surcharge, education cess, interest, fee under 234E, others. |
| Deduction Month                  | The salary month this challan pays for.                           |


**Deduction Month** defaults from the deposit date: TDS for a month is deposited by the 7th of the next one, so a challan dated 7 May is taken to pay April's deduction. Set it explicitly when that is not true.

Challans must be **submitted** to be picked up by a return.

A challan may hold more tax than a single return draws from it. The balance stays available for another return, and only over-drawing is treated as an error.

## **Creating a return**

Create a **TDS Return**, pick the Company, Financial Year and Quarter, and save. TAN and deductor PAN are pulled from the Company. Only one return per TAN, financial year, quarter, form and return type is allowed.

### **Deductor and responsible person**

The return carries the full payer profile that NSDL asks for: address, contact, GSTIN, branch, plus the same for the responsible person, and the government deductor fields (state code, ministry, AIN) where they apply.

To avoid retyping, link an **Address** or **Contact** in the corresponding link field and the individual fields are filled from it. The link fields only offer records linked to the return's company. Anything the linked record cannot supply (post office, PAN, deductor type) is left for you to fill in.

### **Fetching deductees**

Click **Fetch from Payroll**. For the quarter, this finds every submitted Salary Slip of the company that carries an income tax deduction greater than zero, and creates one deductee row per employee and month with:

- PAN and deductee status
- Month, date of payment and date of deduction
- Amount paid (gross pay) and tax deducted
- The challan whose deduction month matches the row. Where a month has more than one challan the earliest wins; where the quarter has exactly one challan, every row maps to it.

The table is fully editable afterwards, so overrides, surcharge, cess, lower deduction certificates and the new regime flag can be set by hand.

Re-fetching clears and rebuilds the table, so any manual edits are lost.

The totals section shows the total amount paid, total tax deducted from the rows, and total tax deposited from the submitted challans for the period.

## **Filing the return**

All four steps live under the **File Return** button group, and they run in order:

```
1. Validate  ->  2. Generate TXT  ->  3. Generate FVU  ->  4. E-File

```

Each step runs in the background. Press the button, the status changes to show the step is running, and the return updates itself when the step finishes. A step cannot be started while the previous one is still running.

### **1. Validate**

Screens the return for the issues that typically trigger a departmental notice.

Before anything is sent, the return checks itself and reports any of these against your own data:

- **Deductee PANs.** Every row must carry a valid PAN or an accepted placeholder. Failures are listed by row number and employee name.
- **Deductor profile.** Any deductor or responsible person detail still missing is named.
- **Challan reconciliation.** Every deduction row must be linked to a challan, and what a challan has already given to earlier returns plus what this return claims cannot exceed the tax actually deposited on it. The message spells out the deposited amount, its breakup, what is already utilised and by how much the claim overshoots.
- **Deposit coverage.** Total tax deducted must not exceed total tax deposited through challans for the quarter.

When the step finishes, the report is attached to the return and its contents appear as **Validation issues** on the dashboard. Reported issues do not block the next step: the check is advisory, and it is for you to judge whether an issue matters.

### **2. Generate TXT**

Produces the NSDL text file, attached as **Form 24Q TXT**. Regenerating it clears the FVU and Form 27A, since they were derived from the previous TXT. The CSI file is left alone.

### **3. Generate FVU**

Needs the TXT and the CSI file. Attaches the FVU as **FVU File**, and the Form 27A PDF separately so it can be previewed and printed.

### **4. E-File**

Files the return. On success the return records the **Provisional Receipt Number**, the **Token Number** and the **Filing Date**, and attaches the receipt.

## **Fetching the CSI file**

The CSI (Challan Status Inquiry) file comes from OLTAS and is required alongside the TXT to produce the FVU. It is an OTP-verified download against the deductor's TRACES-registered mobile number.

Click **Fetch CSI** and:

1. Confirm the TRACES mobile number and the reason for the download (TRACES requires at least 20 characters). An OTP is sent to that number.
2. Enter the OTP. The CSI file is downloaded and attached to the return.

You can also skip this entirely and attach a CSI downloaded from the TIN OLTAS "Challan Status Inquiry" page directly to the **CSI File** field.

## **Skipping validation**

**Skip Validation** moves a return straight to TXT generation when the validation check cannot complete.

It skips that check only. The PAN and reconciliation checks still run. A reason is mandatory, and it is recorded on the return along with your username and shown in the validation issues panel.

## **Submitting the return**

A TDS Return can only be submitted once its filing status is **Filed** or **Accepted**. Submitting marks the return as final.

## **Revised returns**

Set **Return Type** to `Revised` and fill **Previous Receipt Number** with the provisional receipt number of the return being corrected. The TXT is then generated against that receipt, and the FVU is generated as a correction rather than a regular filing.

## **Form 16**

Once a **Q4** return is Filed or Accepted, a **Create Form 16** button appears. It creates one Form 16 record per employee in the return's annual annexure, carrying gross salary, total taxable income and total tax deducted. Employees who already have a Form 16 for that financial year are skipped.

On each Form 16:

- **Generate Part B** builds the salary and tax computation.
- **Request Part A (TRACES)** requests the TDS certificate from TRACES. It is only allowed once the linked Q4 return is filed.

Both run in the background. The certificates are attached as **Part A PDF** and **Part B PDF** when they are ready, and the status moves from `Requested` to `Available` (or `Failed`).

## **Filing statuses**


| Status             | Meaning                                                                               |
| :------------------ | :------------------------------------------------------------------------------------- |
| Draft              | Created, nothing filed yet.                                                           |
| Validating         | Validation is running.                                                                |
| Validated          | The validation check completed.                                                       |
| Validation Skipped | Validation was deliberately skipped, with a recorded reason.                          |
| Generating TXT     | The TXT is being generated.                                                           |
| TXT Generated      | TXT file attached.                                                                    |
| Generating FVU     | The FVU is being generated.                                                           |
| FVU Generated      | FVU and Form 27A attached.                                                            |
| Filing             | The return is being filed.                                                            |
| Filed              | Receipt number recorded. Ready to submit.                                             |
| Failed             | The last step failed. The filing log carries the reason.                              |
| Accepted           | Recognised as final. Set it yourself if you track departmental acceptance separately. |


The status also appears as a coloured indicator on the form: green for Filed and Accepted, red for Failed, orange for everything else.

## **Troubleshooting**

**The Filing Log is the first place to look.** Every step appends a row with the action, its status, the time and the message it came back with. It is the record of everything the return sent and received.

**"The background scheduler is disabled."** Filing steps cannot run without it. Ask your administrator to enable the scheduler, then try again.

**"'Generating TXT' is still in progress."** The previous step has not finished yet. Give it a few minutes.

**A step failed with an upload message.** Run the same step again; it starts a fresh attempt.

**A step is stuck.** Any step that has not finished in three hours is marked failed, so the return never sits waiting indefinitely. Run it again.

**Everything is kept on the return.** Alongside the TXT, FVU, Form 27A and CSI, the exact data submitted is attached for audit, together with any report that came back. Reports are copied onto the return rather than linked, so they stay available after the filing portal expires them.

<!-- page: frappe-hr/hr__integrating-frappe-hr-with-biometric-attendance-devices.md -->
---
title: "Integrating Frappe HR With Biometric Attendance Devices"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/integrating-frappe-hr-with-biometric-attendance-devices"
updated: "2026-02-04"
---

**Background**
--------------

The Attendance punch logs from the biometric device are check-in and check-out logs of an employee. Frappe HR has a provision to store these logs in a document called Employee Checkin.

Attendance can then be marked based on the [Employee Checkin](https://docs.frappe.io/hr/employee-checkin) records and the [Shift Type](https://docs.frappe.io/hr/shift-type) of the employee by using [Auto Attendance](https://docs.frappe.io/hr/auto-attendance)

Hence, integrating your Biometric Device (*or any access control system that collects IN/OUT logs*), can be done using the following steps:

### **1. Setting up Auto Attendance to mark attendance from the Employee Checkin**

Before you import/sync employees' Check-in and Check-out logs into your Frappe HR system, you will have to set up the employees and their shifts to be able to generate attendance using the Auto Attendance feature in Frappe HR.

Please refer to the following link to set up Auto Attendance: [Set up Auto Attendance](https://docs.frappe.io/hr/auto-attendance)

Once you have set up the employee master and assigned shifts to the employees, you are now ready to proceed to the next step.

### **2. Populating the Biometric Punch Logs into Frappe HR's Employee Checkin**

Depending on your biometric system and its features, there can be a lot of ways you can populate the Punch logs into Frappe HR:

1. **Use the Data Import Tool**:


	* The simplest possible solution (in terms of implementation complexity) would be to generate an Excel/CSV of the Check-in/Check-out and use the built-in data import tool in Frappe HR to periodically import the logs to your Employee Checkin Document
	* Please refer to [Documentation on Data Import Tool](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/data/data-import) for more on how to do this.
2. **API Integration**:


	* You can automate the process of syncing the Biometric Punch Logs by integrating it with the available API in Frappe HR.
	* This method requires some technical knowledge and you should probably get in touch with your Frappe HR implementor or Biometric system vendor.
	* Steps:
	
	
		1. You will first need to create a [user](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users) in your Frappe HR instance that would be used for creating logs since this API method requires login. Make sure this user has all the required permissions to create Employee Checkin.
		2. [Generate API Key and API Secret](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users#210-api-access) for the user which will be used for authentication.
		3. Make sure you have set the [Attendance Device ID (Biometric/RF tag ID)](https://docs.frappe.io/hr/auto-attendance#3-setup-attendance-device-id-field-in-employee) for the employees based on your Biometric Device.
		4. The API implementation details can be found [here](https://github.com/frappe/hrms/blob/d2529e03f92bf50efb65d3163bfcfdacbcf0b8f5/hrms/hr/doctype/employee_checkin/employee_checkin.py#L63-L109) and the API can be accessed at: `/api/method/hrms.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
		5. You can write a script to send a POST request to the API. This endpoint finds the relevant Employee using the employee field value and creates an Employee Checkin. Details of the API endpoint:
		
		
			+ URL: `/api/method/hrms.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
			+ Method: `POST`
			+ Params:
			
			
				- `employee_field_value`: The value to look for in the employee field. This will be the Attendance Device ID found in your biometric logs and also set in the employee record.
				- `timestamp`: The timestamp of the Log. Currently expected in the following format as a string: '2022-04-08 10:48:08.000000'
				- `device_id`: (optional) Location / Device ID. A short string is expected.
				- `log_type`: (optional) Direction of the punch if available (IN/OUT).
				- `skip_auto_attendance`: (optional) Skip auto attendance field will be set for this log (0/1)
				- `employee_fieldname`: (Default: `attendance_device_id`) Name of the field in Employee DocType based on which employee lookup will happen.
				- `latitude`: (optional) Latitude of the shift location if shift location is assigned.
				- `longitude`: (optional) Longitude of the shift location if shift location is assigned.
			+ Response: Returns an Employee Checkin document object which was inserted.
3. **Set up a python script on your computer to integrate ZKTeco or similar devices**:


	* This method works only for ZKTeco or similar devices that use the ZKProtocol to communicate over TCP/IP.
	* This script is available at: [github:frappe/biometric-attendance-sync-tool](https://github.com/frappe/biometric-attendance-sync-tool).
	* Please follow the instructions given on the script page to set it up on your computer.
	* This Script pulls biometric logs from a supported device and uses the API mentioned in the above step to push the data into Frappe HR.

**Frequently Asked Questions**
------------------------------

### **1. How do I select a Biometric Device which is compatible with Frappe HR?**

If you are using method 1 or 2, you don't need to worry about compatibility.

However, for the third method, the push biometric app internally uses a script that is compatible with the devices listed over [here](https://github.com/fananimi/pyzk#compatible-devices). Typically, any ZKTeco or similar device that uses the ZKProtocol to communicate over TCP/IP should work. As far as buying the device is concerned, we suggest you opt for a device trial with the vendor if possible, where the device can be tested with the sync tool, as it's dependent on multiple factors when it comes to compatibility.

### **2. How do I know which method to use for integrating my biometric device with Frappe HR?**

Method 1 is feasible in any situation but requires you to manually import logs periodically. Methods 2 and 3 need some monitoring and work for a one-time setup for the log syncing to be automated.

**For a single location set up:**

In the Push Biometric Device approach, the tool needs to be able to communicate with your biometric device via TCP/IP. So, it is usually the case that it needs to run on the same LAN Network as the biometric device. To sync these fetched logs to your Frappe HR instance it uses API access. This works best when you have a single location set up.

**For a multi-location set up:**

In this case, we usually recommend method 2 where most biometric vendors provide services to sync the biometric device logs from multiple locations to Frappe HR via API access. Method 3 (push biometric attendance tool) can also work in this case if you have some networking knowledge.

  

<!-- page: frappe-hr/hr__interview-feedback.md -->
---
title: "Interview Feedback"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-feedback"
updated: "2026-02-04"
---

**Interview feedback refers to the information and comments provided about a job applicant after an interview.**

The Interview Feedback doctype allows you to assess a Job Applicant's Skills and comment on the Interview in general.

To access Interview Feedback, go to:


> **Home > Human Resources > Recruitment > Interview Feedback**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Interview Feedback, it is advisable you create the following:

* [Interview Round](https://docs.frappe.io/hr/interview-round)
* [Interview](https://docs.frappe.io/hr/interview)

**2. How to Create an Interview Feedback**
------------------------------------------

1. Go to the Interview Feedback list and click on Add Interview Feedback.
2. Select the Interview, Interviewer and Result.
3. Selecting the Interview should automatically populate the Skill Assessment table with the Skills defined in the Interview Round corresponding to the selected Interview. You can then fill out stars for each Skill based on the Job Applicant's performance.
4. Fill in the Feedback section with general feedback regarding the Interview (optional).
5. Click on Save, and then Submit.

[Screenshot on the live page]  


**3. Features**
---------------

### **3.1 Feedback Summary**

After submitting the Interview Feedback, you can view a summary of all the feedback associated with the Interview under its [Feedback Tab](https://docs.frappe.io/hr/interview#3-2-interview-feedback).

### **3.2 Interview Feedback Reminder**

You can [configure](https://docs.frappe.io/hr/hr-settings#4-2-send-interview-feedback-reminder) Frappe HR to send reminder emails to Interviewers for their Feedback.

**4. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Job Applicant](https://docs.frappe.io/hr/job-applicant)

  


  

<!-- page: frappe-hr/hr__interview-management.md -->
---
title: "Interview Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-management"
updated: "2026-02-04"
---

Frappe HR makes it easy to manage and track multiple interview rounds for job applicants interested in joining your company.

Using this sub-module, you can:

1. [Define Interview Types](https://docs.frappe.io/hr/interview-type) (optional)
2. [Set up Interview Rounds](https://docs.frappe.io/hr/interview-round)
3. [Create Interviews](https://docs.frappe.io/hr/interview)
4. [Fill out Interview Feedbacks](https://docs.frappe.io/hr/interview-feedback)

  

<!-- page: frappe-hr/hr__interview-round.md -->
---
title: "Interview Round"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-round"
updated: "2026-02-04"
---

**Interview rounds are a series of interviews that a candidate goes through during the recruitment process. For example, technical interviews, HR interviews, etc.**

The Interview Round doctype enables you to define and set up these rounds for future [Interviews](https://docs.frappe.io/hr/interview).

To access Interview Round, go to:


> **Home > Human Resources > Recruitment > Interview Round**
> 
> 

**1. How to create an Interview Round**
---------------------------------------

1. From the Interview Round list, click on Add Interview Round.
2. Enter the Round Name.
3. Enter the Interview Type and the Expected Average Rating (optional).
4. You can assign Interviewers, authorizing them to provide feedback for upcoming Interviews of this round.
5. You can also enter Designation to filter Job Applicants during Interview creation.
6. Fill in the Expected Skillset table by clicking on Skill and creating Skills as shown below.

[Screenshot on the live page]
7. Save

[Screenshot on the live page: 135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1]  


After saving the Interview Round, you can [Create Interviews](https://docs.frappe.io/hr/interview) directly from the dashboard. The assigned Interviewers can then provide [Feedback](https://docs.frappe.io/hr/interview-feedback) for the created Interviews.

**2. Related Topics**
---------------------

1. [Interview Type](https://docs.frappe.io/hr/interview-type)
2. [Interview](https://docs.frappe.io/hr/interview)
3. [Job Opening](https://docs.frappe.io/hr/job-opening)
4. [Designation](https://docs.frappe.io/hr/designation)

  

<!-- page: frappe-hr/hr__interview-type.md -->
---
title: "Interview Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview-type"
updated: "2026-02-04"
---

**Interview type refers to the various types of interviews conducted by an organization, such as panel interviews, walk-in interviews, etc.**

Interview Types can be used to specify the type of interview for a particular [Interview Round](https://docs.frappe.io/hr/interview-round).

To access Interview Type, go to:


> **Home > Human Resources > Recruitment > Interview Type**
> 
> 

**1. How to Create an Interview Type**
--------------------------------------

1. Click on Add Interview Type.
2. Enter the Name and Description
3. Save

[Screenshot on the live page: image]  


**2. Related Topics**
---------------------

1. [Interview Round](https://docs.frappe.io/hr/interview-round)
2. [Interview](https://docs.frappe.io/hr/interview)
3. [Interview Feedback](https://docs.frappe.io/hr/interview-feedback)

  

<!-- page: frappe-hr/hr__interview.md -->
---
title: "Interview"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/interview"
updated: "2026-02-04"
---

**Interviews are formal meetings between Job Applicants and Interviewers to assess whether the former is suitable for the Job Opening they're applying for.**

Frappe HR allows you to maintain a record of all Interviews conducted with Job Applicants.

To access Interview, go to:


> **Home > Human Resources > Recruitment > Interview**
> 
> 

**1. Prerequisites**
--------------------

Before creating an Interview, it is advisable you create the following:

* [Interview Round](https://docs.frappe.io/hr/interview-round)
* [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**2. How to Create an Interview**
---------------------------------

1. Go to Interview list, click on Add Interview.
2. First select the Interview Round and then Job Applicant. Order is important.
3. Enter the date (Scheduled On) and time (From Time & To Time).
4. Enter the Resume Link (optional).
5. Click on Save.

[Screenshot on the live page]  


After saving the Interview, you can reschedule the interview using the Reschedule Interview button. You can also directly [Submit Feedback](https://docs.frappe.io/hr/interview-feedback) from the dashboard.

> **Note:** Only Interviewers associated with the selected [Interview Round](https://docs.frappe.io/hr/interview-round) can submit Feedback.

**3. Features**
---------------

### **3.1 Calendar View**

Scheduled interviews can be viewed in a color-coded calendar format by going to the Interview list, clicking on List View, and selecting Calendar.

[Screenshot on the live page: image]  


### **3.2 Interview Feedback**

After an interview has received [Feedback](https://docs.frappe.io/hr/interview-feedback), you can click on the Feedback tab to access a summary of the feedback. This summary includes the overall average rating, the distribution of ratings for each Feedback, the average rating for each Skill, and the individual Feedback comments.

[Screenshot on the live page]  


### **3.3 Tracking Interviews**

Interviews related to a Job Applicant can be easily [tracked](https://docs.frappe.io/hr/job-applicant#3-2-tracking-interviews) from its dashboard.

### **3.4 Interview Reminder**

You can [configure](https://docs.frappe.io/hr/hr-settings#4-2-send-interview-reminder) Frappe HR to send reminder emails to Interviewers for upcoming Interviews.

**4. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Interview Type](https://docs.frappe.io/hr/interview-type)
3. [Interview Feedback](https://docs.frappe.io/hr/interview-feedback)
4. [Job Offer](https://docs.frappe.io/hr/job-offer)

  
